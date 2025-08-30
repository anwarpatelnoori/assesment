const observer = new MutationObserver((mutationsList) => {
	mutationsList.forEach((mutation) => {
		if (mutation.type === 'childList') {
			// Check if the added node matches the selector
			$(mutation.addedNodes).each(function () {
				if($(this).is('[tabindex]') && $(this).find('[title="Is Active: "]').length > 0){
					$(this).children().addClass("bg-danger");
				}
			});
		}
	});
});

// Start observing the body (or a specific element) for changes
observer.observe(document.body, {
	childList: true, // Observe when child nodes are added or removed
	subtree: true     // Observe changes in the entire subtree, not just direct children
});