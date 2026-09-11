<div dir="rtl" align="right">

<style>
.tg-channel-box {
  max-width: 800px;
  margin: 0 auto;
  padding: 16px;
  font-family: system-ui, -apple-system, 'Segoe UI', 'Vazirmatn', Tahoma, sans-serif;
  background: #fafafa;
  border-radius: 20px;
  line-height: 1.7;
}

/* حالت دارک برای کسانی که تم دارک دارن */
@media (prefers-color-scheme: dark) {
  .tg-channel-box {
    background: #1a1a2e;
    color: #eee;
  }
  .tg-post {
    background: #16213e;
    border-color: #0f3460;
  }
  .tg-post-header {
    background: #0f3460;
  }
  .tg-footer {
    color: #aaa;
  }
  .tg-text a {
    color: #7eb6ff;
  }
}

/* کارت پست */
.tg-post {
  background: white;
  border-radius: 20px;
  padding: 18px 22px;
  margin: 20px 0;
  box-shadow: 0 2px 8px rgba(0,0,0,0.08);
  border: 1px solid #e5e7eb;
  transition: box-shadow 0.2s;
}
.tg-post:hover {
  box-shadow: 0 8px 20px rgba(0,0,0,0.1);
}
.tg-post-header {
  background: #f3f4f6;
  margin: -18px -22px 16px -22px;
  padding: 10px 22px;
  border-radius: 20px 20px 0 0;
  font-size: 13px;
  color: #4b5563;
  border-bottom: 1px solid #e5e7eb;
}

/* نقل قول / فوروارد */
.tg-forward {
  background: #eef2ff;
  border-right: 4px solid #3b82f6;
  padding: 8px 14px;
  border-radius: 12px;
  margin: 12px 0;
  font-size: 13px;
  color: #1e40af;
}

/* متن */
.tg-text {
  font-size: 16px;
  margin: 14px 0;
}
.tg-text a {
  color: #2563eb;
  text-decoration: none;
}
.tg-text a:hover {
  text-decoration: underline;
}

/* تصاویر */
.tg-photo {
  margin: 12px 0;
  text-align: center;
}
.tg-photo img {
  max-width: 100%;
  border-radius: 16px;
  box-shadow: 0 2px 8px rgba(0,0,0,0.1);
}

/* آلبوم */
.tg-album {
  display: grid;
  grid-template-columns: repeat(auto-fit, minmax(150px, 1fr));
  gap: 8px;
  margin: 12px 0;
}
.tg-album-item {
  overflow: hidden;
  border-radius: 12px;
}
.tg-album-item img {
  width: 100%;
  height: 150px;
  object-fit: cover;
  transition: transform 0.2s;
}
.tg-album-item img:hover {
  transform: scale(1.02);
}

/* ویدیو */
.tg-video {
  margin: 12px 0;
}
.tg-video video {
  width: 100%;
  border-radius: 16px;
  background: black;
}
.tg-dl-btn {
  display: inline-block;
  background: #3b82f6;
  color: white;
  padding: 6px 14px;
  border-radius: 24px;
  font-size: 13px;
  text-decoration: none;
  margin-top: 6px;
}
.tg-dl-btn:hover {
  background: #2563eb;
}

/* فایل */
.tg-doc {
  background: #f9fafb;
  border: 1px solid #e5e7eb;
  border-radius: 16px;
  padding: 12px 16px;
  margin: 12px 0;
  display: flex;
  align-items: center;
  gap: 12px;
}
.tg-doc-icon {
  font-size: 32px;
}
.tg-doc-info {
  flex: 1;
}
.tg-doc-title {
  font-weight: 600;
}
.tg-doc-extra {
  font-size: 12px;
  color: #6b7280;
}
.tg-doc-link {
  background: #3b82f6;
  color: white;
  padding: 6px 12px;
  border-radius: 20px;
  font-size: 12px;
  text-decoration: none;
}

/* نظرسنجی */
.tg-poll {
  background: #fef9e3;
  border: 1px solid #fde047;
  border-radius: 20px;
  padding: 12px 18px;
  margin: 12px 0;
}
.tg-poll h4 {
  margin: 0 0 10px 0;
  color: #854d0e;
}
.tg-poll ul {
  margin: 0;
  padding-right: 20px;
}
.tg-poll li {
  margin: 6px 0;
  color: #a16207;
}

/* فوتر پست (تاریخ و بازدید) */
.tg-footer {
  font-size: 12px;
  color: #9ca3af;
  margin-top: 12px;
  padding-top: 8px;
  border-top: 1px solid #e5e7eb;
  display: flex;
  gap: 12px;
  justify-content: flex-end;
}
.tg-footer a {
  color: #6b7280;
  text-decoration: none;
}
.tg-footer a:hover {
  color: #3b82f6;
}

/* هدر کانال */
.tg-channel-header {
  text-align: center;
  padding: 20px;
  background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
  border-radius: 28px;
  color: white;
  margin-bottom: 24px;
}
.tg-avatar {
  width: 80px;
  height: 80px;
  border-radius: 50%;
  border: 4px solid white;
  margin-bottom: 12px;
}
.tg-channel-header h1 {
  margin: 8px 0 4px;
  font-size: 24px;
}
.tg-channel-header p {
  margin: 4px 0;
  opacity: 0.9;
}
.tg-channel-desc {
  background: #f3f4f6;
  padding: 14px 20px;
  border-radius: 20px;
  margin: 16px 0;
  font-size: 14px;
  color: #374151;
}
.tg-last-update {
  text-align: center;
  font-size: 12px;
  color: #9ca3af;
  margin: 16px 0;
}
.tg-telegram-btn {
  display: inline-block;
  background: #1e88e5;
  color: white;
  padding: 8px 18px;
  border-radius: 30px;
  text-decoration: none;
  margin: 12px 0;
  font-weight: 500;
}
.tg-telegram-btn:hover {
  background: #0b5e8a;
}
@media (prefers-color-scheme: dark) {
  .tg-channel-desc {
    background: #1f2937;
    color: #d1d5db;
  }
  .tg-post {
    background: #1e1e2f;
    border-color: #2d2d44;
  }
  .tg-post-header {
    background: #2a2a3b;
    color: #bbb;
    border-color: #3a3a52;
  }
  .tg-doc {
    background: #252535;
    border-color: #3a3a52;
  }
  .tg-forward {
    background: #1f2a3a;
    color: #90cdf4;
  }
}
</style>

<div class="tg-channel-box">

<div class="tg-channel-header">
<img src="https://cdn4.telesco.pe/file/Z4wiiuiVe61UCx3MfhDVZoJfvttJy6ziEJxQM6q0EBAqKuT1xPMaaA5zmyWug2XWvUsibuGr8ZT-vkAtNbtCDDOkDsNMaAsK1PhgWtWmXzXuBZYfzqeC0Q_Ly6YanQnIKTOzLe0ZsznJ1XP-PSmZIr9Jh931rOU7xL6JL53I-8fCFju36Vwh3E5DG6jqMxUYr0nCs_UQf4as2ULk75ITWkRWU4TdaaGXj7h-yS1GZiHvGonYKB5yujj7zYLyizQlRpJv1RjKv_sfxvswYiAB7k5C0N0DSQBsB3I4jpL5atg_ne1sa_DFGQCfJLiq9ZkdTpAasb3MAEBxOi7NIpCzFw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 111K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 22:23:04</div>
<hr>

<div class="tg-post" id="msg-71486">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68083de4e6.mp4?token=jdw2dpTGKLfatf7UBQOiarE1LHz7BngQG98-CikeYjwou0FcIkTbBEWQBmh9ySjDbtlSB8bH5QHnwHdtZLs_DGx-NiSNBsSqKIYtTBf27OPjz2I6UTLcLFLAmQIC0XaPxDPhRT1QtsM66NRO--jg39zShgqLRt_Ujj0VKq8UrSvOd0kJhOSST1Wg7sTNgAgCSROiQEMLM-jrbohWa5de14Vfd9HNW-t92Zw6HelVM_iMX8311YAVurdUtD551GK_J1Oh5WnhvHdvPZ1_-VwpDC0NW0dl5rc99WVU85lsxHZn2REVPD8JFotG7TUTAtkcIC4gtzZw2Y32tcKuzlNO3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از یه دختره که پارتنرش یه ترنسه
@News_Hut</div>
<div class="tg-footer">👁️ 2.27K · <a href="https://t.me/news_hut/71486" target="_blank">📅 22:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71485">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9c1f7e0a7d.mp4?token=qvlaFC2XEZx1XEEdLOs1zuxjJaCtWNNvxkMq4aYy7q65hZwPBtM-2br85XflTHU3eMsWIKC8aNdin1ydx23zG41WVwcvtSZ4qYWln4zYkwgDFPz28wAKmPr8fFkPsBS5sbIfxGtL_Ws01pZO4t5vj6aEhK_lRzN9BSX4TEu8Gl72p0v49v-DeXeHEmSGCtuuFT_a_hlQRJFK8iR9b2ngCSi4-UhvKC8ZhFSOnB5vbYFEuDCNs6zolrWdRA5Tf89nbZXPjcUTOjjsWokS_ZIWwkCYFlQlOwA5IqXl32tyaa-J_OFxJzWlLjcbwDm_Poojn52IVa0f22lk1gJyky2J4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
حرفای زن دعوت شده به صداوسیما درباره ترامپ و نتانیاهو:
ما میخایم با پول حلقه های ازدواجمون طناب داری بر گردن نتانیاهو و ترامپ بندازیم
درست ۷ کیلو و ۲۰۰ گرم طلا به قاتل ترامپ جایزه میدیم
ما میخایم خون بر شمشیر پیروز بشه
از مامان های محترم تعهد گرفتیم و به مقدار توانشون طلا کمک کردن که به قاتل ترامپ بدیم
از ارزشمند ترین دارایی هامون می‌گذریم تا ترامپ کشته بشه
@News_Hut</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/news_hut/71485" target="_blank">📅 21:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71484">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">🚨
🇮🇷
۱۰ دقیقه پیش، نیروی دریایی سپاه پاسداران یک موشک کروز ضدکشتی را از سیریک به سمت تنگه هرمز شلیک کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/71484" target="_blank">📅 20:58 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71483">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dcbed492f8.mp4?token=Yc_edyAsiHaBz9dHEgOkRYADvRC01dO_S31xLHE7hxrPJUcWLmSn92Uqgxnap8aYhiSoqabNzWf4dt_GPdgJtDP9N5fv1lUlS67sEGeku70pbgfhTb_C8SMQvju0zHTTQ1ULh9PrmpjHti28yMIMHUk_8x1khzAvxzYuxBL07zqSX3FZaxrKmvn2fb_GHzlfR-sadQVJHM7D85yRKrxUWdov_yjBCckyAz0huwU9HVf0GqgZS5n7cLQSSLg6dARy69wqEBfg-1PAxzj4d4hbHFQxpY6k6sCKM7GFL6VSfoybvOREmgXrqtFVc_oiQRCZeIceZx_aVIWD4NAwo53NfA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇯🇵
آتشفشان ساکوراجیما در جزیره کیوشو ژاپن فوران کرد و خاکستر و مواد آتشفشانی را تا ارتفاع چند هزار فوتی به هوا فرستاد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/news_hut/71483" target="_blank">📅 20:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71482">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2d66564850.mp4?token=C0BRAkfKGtI2j4jK0kfricER-s2X5PziNKW3Yz_qKNvrvstnoATaUxGFlFN8R49pJ2Uqp_Q432ANUCQhCh28pa3gvKcdkNN0QA0cspiajGpAairEULSEOjgLlzKIja9BwgDkDcg59iQ1r917KnjbUh39S_BnGFMgpREuvyppCVXx9NOnfMyHh1H898ylLV1FsK5Bhp3mJLvl_XHKFiga4y0QGjCUjY80GbU6H7UNqek37AiukcirUDXHvTJvllo9O5f160m1d4s6gqVs34B2WBJjM91dNWknH1JUod31OWn4aqUgLmP6725FDSN3Fg5PG0-kz517aKIWFbOXYv5zDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇮🇷
صحبت های عجیب
پوریا بختیاری کارشناس اقتصادی در مصاحبه با علی ضیا درباره ابراهیم رئیسی:
نزدیکان رئیسی گفتند که حاج‌آقا خودش اقرار کرده که اقتصاد متوجه نمی‌شود.
بعد گفتیم خب، یعنی باید برای رئیس‌جمهور کلاس اقتصاد بگذاریم؟
گفتند نه، کلاس اقتصاد که نه؛ حاج‌آقا ذهنش می‌پرد و خسته می‌شود. بیاییم موشن‌گرافی بسازیم.
ما یک تیم انیمیشن آوردیم که برای رئیس‌جمهور مملکت کلیپ‌های اقتصادی درست کند. قانون هم گذاشته بودند که هر کدام از کلیپ‌ها بیشتر از سه دقیقه نشود، چون ذهن حاج‌آقا می‌پرد.
ببینید چقدر این موضوع تلخ و «دارک» است که برای رئیس‌جمهور مملکت و بالاترین قدرت اجرایی، بروی انیمیشن درست کنی تا بلکه اقتصاد را بفهمد!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/71482" target="_blank">📅 19:37 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71481">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c90c5de5a1.mp4?token=PhD6V8B_UjbUKcC6yPu4Lx9gPWUCO1bWBnB0OMBK_HWsw34zCnqmgdAzdck-ebh9fQIrDi5Wq-sRzwten_U6wvXVcHmrBLgncrMLLnycfZT4dcTExy2xvv3XjB_OMW0mugNrN58I9_tSFBeCfDnfKmlzf0_rS0EYFe9KW8L1ot9IRQP8zTOB1VbkdfVzQW-PJpca6iBhUumpxkaLIkXIgjaK6FwpS4YmAfxA0jdB80ZhB0nVf6JFh7LDfrvfuer5SAOBoVtL_K3_eYTssvLnMh8KsxDkWjYV9paSZcVp0HFv2JD6l2zF-fht8PQE9qAmmjVTE2A-SMNjXlDVQdaKGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
اوکراین پایگاه دریایی نووروسیسک روسیه - بندر اصلی باقی مانده ناوگان دریای سیاه - را با حمله ترکیبی پهپاد و موشک در طول شب هدف قرار داد.
لیست خسارات تایید شده قابل توجه است
؛
ستاد کل ارتش می‌گوید سه کشتی جنگی (مین‌روب ژلزنیاکوف، ناوچه حامل کالیبر، دریاسالار اسن، و کشتی پهلوگیری پیوتر مورگونوف) به علاوه انبار سوخت مورد اصابت قرار گرفته‌اند.
اطلاعات و OSINT اوکراین، ناوچه دریاسالار ماکاروف، یک کشتی موشک‌انداز بویان-ام (غیرعملیاتی ارزیابی شده)، کشتی گشت‌زنی واسیلی بیکوف، چندین قایق موشک‌انداز و دو رادار دفاع هوایی در نزدیکی گلندژیک را اضافه می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/71481" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71480">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71480" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/71480" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71479">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kva-lxxIwH3mH8gUW2hvHc2W6yK-ML_sTxHdLHxNSClQeeHwr09w5LMvmHd9AFGA_sCLbLVY8LkJODSKKsYDn1CDl6-TKUWcjGKV9Z_KvlQ9BAvMCVFHm_TDhyRJ6DNK06t1WC4ROZAYZ-YOdVhqb0X-Y-ttuXbpR-WJpQIeRz9BmaJumOy3TQvWLIzjyiTShwCrpY9nWystkLhsXuR66QnLV89QbQ0DBTy0m47jNEh3zzMwcJb37CEQnGlxuhqJ2x036gtHizkKGZLuxFRm4FZo1ZyNiMUBb2KpQl2rG8LzQ-M_gi4FwkNxtsHJ40oimFihSt9Ox5Oqz4K8rvvvNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
آماده‌ای هیجان واقعی رو تجربه کنی؟
🦖
در
TrexBet
، دنیایی از اسلات‌های جذاب، بازی‌های کازینوی زنده و لحظه‌های هیجان‌انگیز منتظر توئه!
🦖
صدها بازی متنوع
🦖
تجربه‌ای سریع و روان
🦖
هیجان در هر اسپین
🦖
🦖
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/news_hut/71479" target="_blank">📅 19:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71478">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hADUewyMLtkbS6r0yJr2o_5q8XCijdHuKiUA9hKY-DGXnXyNR96NgFdiHNejDPa64a1F6IQya5Rjl2ce4zTKLE9tvOWNuAZBsMqW1WCRQV7zKoLTGrCRL6HxnZRIYgX_UR8C6nJxrhMHJor596FTXZ9HjTX3Hpg9M-iM38GCFrTZqjlKt9QSom2_QMOHAcQOVvUGedFtaMRS1KyutpCqYgC6TwlPLASjxcgeyDO4ajDKk5k05Oyluz1cw8WUNlB-vrOSlNkgNmicnriYxYQcHqw9gyqzLswAYOKRgBT-uqn4iluYA-SKBIGG5s89d9HT2IIVSmgMunE3vKg41uZ3-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⏺
🇮🇱
🇺🇸
نخست‌وزیر نتانیاهو:
می‌خواهم برای رئیس‌جمهور دونالد جی. ترامپ، خانواده‌اش و مردم آمریکا آرزوی «شانا تووا» (Shana Tova) داشته باشم؛ سالی نو همراه با شادی و سلامتی.
در طول سال گذشته، ایالات متحده و اسرائیل با یکدیگر به پیشرفت‌های تاریخی دست یافته‌اند. ایران و محور شرارتِ آن، ضعیف‌تر از هر زمان دیگری شده‌اند، در حالی که اتحاد میان آمریکا و اسرائیل قوی‌تر از همیشه است.
من به رئیس‌جمهور ترامپ بابت اعمال محاصره علیه رژیم شرور ایران و فشار اقتصادی بر بزرگ‌ترین منبع بی‌ثباتی در جهان، تبریک می‌گویم.
مردم اسرائیل در مقابله با نیروهای ترور، در کنار مردم ایالات متحده و رئیس‌جمهور ترامپ ایستاده‌اند.
در سال پیشِ رو، ما همچنان به تلاش برای امن‌تر ساختن جهان برای همگان ادامه خواهیم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/71478" target="_blank">📅 18:49 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71477">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0625ae5db9.mp4?token=Z08VJALKYBaIwVoZDUPfB8D4KUeB-mOayFAEFAFM6mUf0YpJG7hSRwdXiXGnRxh7fD0nGUUKrhDP33SHxcOhP16SfsumQXf4I61-ngf28eF0qreRMrshcYOGDfUj_ev2JqNBa0pa8spAQEBJktooOZ3lbu9ns1RzjIrnllz3IUo5SKgLBw-zCfp76krYjx_fT6f2hlpVcnNIjTYI3VxsI0-OYmA1fbVVcB1l65QQm7LayL3Lpfp5MS-pQIkoV9uvWfTlk9f_FOi4efLBg7_BM_ao-X0ufzt3F3tTTRH00h5s0yYkekgfBffDB-v_VLswmAotmSrWO3yZ4CTJul7bFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
ما به نیروهای نظامی‌ای که هم‌اکنون در تلاشند تا اطمینان حاصل کنند بزرگ‌ترین حامی تروریسم در جهان — یعنی جمهوری اسلامی ایران  — هرگز و به هیچ وجه به سلاح هسته‌ای دست نخواهد یافت، ادای احترام می‌کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/71477" target="_blank">📅 17:59 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71475">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3dd606e096.mp4?token=Ns8YaXynhZMf5bR1xMXfJF_nyD_Iv-_aT54yKcfG6l65HFnGcUP9fFXxwnWLy79eZuhgq214Wzcx-DZJG78_ARaiWYKzREFBrN4AnPHGtVvxo37DXWjs6LpZwRJ4dZg3ub97Xt03O9SR9Ax9epkdiCDI8iy2KEwG55O2DIWpRB-LoM4ICdUM04lV6N97sH0_ndHFvsmnZSH0DLIs6jPpecCAt5Lfg28Ffhko2s3NrYVPvxPPCsKgiB_OovPpcJCIXMVF2t6jGb6zSyRVk3jqrHF2UnTfBi0VyIIAQaCbgCtX_H0y3kmiOj8dTvxzGK3ZRI2IIHDNvBy4uKi3STjoFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ واقعه ۱۱ سپتامبر را به جنگ خود علیه ایران پیوند می‌دهد:
به همین دلیل است که امروز می‌جنگیم. ما چاره‌ای نداریم؛ تنها گزینه، پیروزی است. ما سرسختانه می‌جنگیم. برای پیروزی می‌جنگیم.
@News_Hut</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/news_hut/71475" target="_blank">📅 17:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71474">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c788d5732.mp4?token=Ke7G666fnBDuSqVeRfrzIamHgZGT_2D-5JpU9iodfJH7TB4cZzk0ELlkr7YxjK48B_GolV0AHmtBrrkWocnwGq0KLKNkBbwqwAZlohPnMnraiU6qmjjPGeostQSSV7xrKyylP2SlEQX-yD75bhJ0WqzMGbJZj9jbNvYx634mLQmB0rpOHQ60afEcaC-mdscBaXbWnN3RRCNuFic94kQfAhbNzefkM_TJ9E1wTrF-XyVZrtlHGYxdsbK-79TLRB5dQNEIVMqNawOY5czKe3oShyCGaZ6esPcZ8tNZAYSCj9yraPpIeDc3beb-EnCmqYrRYnX57nbapnSu7vKfOv0qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
اسکات بسنت وزیر خزانه‌داری آمریکا:
آنچه اکنون در مورد ایران شاهد آن هستیم، حیوانی است که در تنگنا گرفتار و زخمی شده است.
این آخرین نفس‌های رژیمی رو به احتضار است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/news_hut/71474" target="_blank">📅 17:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71473">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/971b0d1003.mp4?token=Fdc7vizF_QeTsUpKKquxzSvArMpEcHekrho-VrBewobSD4FVzXQSwYZXlW-cxvY9g2i1L0g-i7YYOMOVjQsgjEZM4cEFFc4-z_wudl0kf1g3bntsIi2igCM0Qljvlj_SBUpSdqq4yf7RKZUpCNe4_ThCX-zJUjuoqkuvhgKcije1mMJG_9gwt05IQfF5AgkdSCz9h9FydenzQ-A6Oe7ApuZS0G9G7fSQSOC5VFYV272E16AyTRiohdpgXrzY1Hidgu6XdN1UR8dhl8CQTo0WWGAIoNLZOVFb1-wYNQ_t7rpzwxYQDe-h4IkHjO_B-8GDgU_OG2ZM3M_H8k2otBlIAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇱
اعتراض ربات های انسان‌نما در مقابل وزارت امور دیجیتال لهستان و سردادن شعارهایی با مضمون«ما خواهان قانون‌گذاری هستیم»و «از مشاغل دفاع کنید»
😳
@News_Hut</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/news_hut/71473" target="_blank">📅 17:13 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71472">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff3ddeb433.mp4?token=F15lPqRGbVJa6UzlXxbkkL7ErTLskhprJX3Qq-f2QtKAS3Lc0-NMwvf0Xv03Qgx4rHXJ6Gjjli16Ee_jv0gO0T8LVl0LxsDEV4MLdFpFB1zODspzbhu50EbFjbjPuzeGIl1wruWTNWdlc6b5C0BCUFRW7eSz_VkvjT051yH1TUTvLYMpQyMuAobXpzpRZ5NkEmT-TrZpe6tOGWKaGPqCMxX-I6q_A3oyIssKvYxzI0o_PBJKA77I2K3wFDZ5JAeWhosZyRzcwMH_MZaSQlkScAme0DYQLcSGp7S74HF22KgH6rAaN-ULeBoJ2o8RJCZMNHz35o2JV2SzIiq9b8DXFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
🇶🇦
هم‌زمان با نخستین سالگرد حمله هوایی اسرائیل به دوحه (قطر) در سپتامبر ۲۰۲۵ — که نخستین حمله اسرائیل به خاک قطر محسوب می‌شود — تصاویر جدیدی از این رویداد منتشر شده است.
این حمله، مقامات ارشد حماس از جمله «خلیل الحیه»، مذاکره‌کننده ارشد این گروه را در جریان مذاکرات آتش‌بس هدف قرار داد.
اگرچه رهبران ارشد حماس از این حمله جان سالم به در بردند، اما شش نفر، از جمله پسر خلیل الحیه و یک مأمور امنیتی قطری، کشته شدند.
این تصاویر جدید که منبع آن‌ها شبکه تلویزیونی «العربی» (Al-Araby TV) اعلام شده، لحظه اصابت را از زوایایی که پیش‌تر دیده نشده بودند، نشان می‌دهند.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71472" target="_blank">📅 16:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71471">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e182f67792.mp4?token=jfYj0hTg41jEoLjo97geIA8myNaHMVgA9iOgVMhRKLK_73uOCNpU1n50oqIxsfIuFsH-rf0VmCTtfdYHvA3tgtAsvFe60yl2iLKY6Oeft8q2L92oLyCA-av9x0HTzKjqqd7yCMos8PUycWEQx89EiIvalJRjex9i6FlNmEgcC-NJw6njlRkGMV_7WhOn8c-AV8uX1lq9ITQzWlQycRu2y_NEtl5RFG3iIE6eXGZk5iVplyIZve8FYqSWBhkHorFKAvzxWKJdM0ZdX-vcpSrmBVeEqyq58MU5R2J2ZViSsSa5nWKJHWFC9ni4gLCsma7lJl9njB_iox3TZ9KZXpJ63A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
توصیه های این بانو درباره وظایف زن مرد توی ازدواج ۳ میلیون ویو گرفته واقعا مفید بود
😏
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/71471" target="_blank">📅 16:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71470">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f28a9989cd.mp4?token=qaInI9hoBYDs-ZWoxaSiq71mNIia5rs5d21CK3fV3WtwKi40GkZ0NGLeGhqg0tLzNzcDmGvVHOjph-1hsIXWq6FQyMiFzMfKxCchWsvgd3NuNZBdKg4T-p1TdpZcARdGHVHAZ-izq6jZfji7oQ60kIOXaRruB6Qb4ImGagveGc-3ELNnXStYI53xmdhqZVuHRbaoOk9N2RMOsMYJIu2cPYDy4mh80ONCepGNUdwpuXIdGiZEgsKwMWLfufxgK-THijuCVjyph916HL5MVC1FYaKMmTVIE26yoaWKklsTDgFaerX8aab0KKNfU1ZMyg4GnQ8iHEWc9gLg6EwGLdoXDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
شرکت پخش فرآورده‌های نفتی:
موفق شدیم رقم ۱۰ هزارتومان را در پمپ بنزین‌ها نشان دهیم و برچسب‌های صفر ثابت را بردارید
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/71470" target="_blank">📅 15:31 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71469">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fc8b06f7d.mp4?token=QADaBRGfwhJ91Jz1X_yIlNwJRQSidiluZDBMsdJtmomjMZS5gnVaOfDuoWoc-ZFAj8cBdpsMgyMgZZYr7u9DEcEerEO6-KMB4vYuv2qBO6PE_0YnKXbbazCxqDnOdM3P7EbPHIxOu7SxnJHUbEwjY3fqjD7Pl1VnVo-_SJCtG9JKzNOg0nzPiUiMsqCso7S49LAkEHmVxgp5vV3HdNj3fSGzRoHf9C-g3xBKA1kucBSu8-xQxGEuhBwJex1CZD4Yce8UkUFHC6u3HzaLRRqWxxYQFF7ozNppsTbX6qVJBGXRmLSOFNN8UkxAAT43lsP5nJPVWIO6FGFNVRPb9PAuDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔞
اگه بدون کاندوم رابطه جنسی برقرار می‌کنید؛
این پست رو یه گوشه‌ای تو تلگرامتون ذخیره کنید که یه روزی بدجوری به کارتون میاد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/news_hut/71469" target="_blank">📅 15:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71465">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54fcf2b7ac.mp4?token=Y9jrafRa63HcEi9nLkjogY5zcSze2Aag92Nm6L8QK1RrsxVZEJw2be6obvFveSC1ScCXVbIR1i6WEp2_VvrbIHkHY7ktvUjOfpYFoIqlzrT-8ayQA0ZkiUiGxTC6G4xZcKpeK8T0SQ4kY-syADzpd7Ltly2xXDWwlid6gpCIPCdnlS1Ub4yULJmXBgRJbn2SPgmCfOx8j-YhduBaLjuAcWeGIpxuXHTh-1GnnpWkZoX97ViC1fCTK2Xpl1N4Hn_OtRSc56Cw-0Htn14fl-7KTEq7lQ_6UjInooheIuw5pTDYfK4hPcPRha0kFSRKwqKTQ3SCRZeQg2xXdDpRsjBAOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
🇺🇸
در ۱۱ سپتامبر ۲۰۰۱، شبکه تروریستی القاعده به رهبری اسامه بن‌لادن، حملاتی هماهنگ‌شده علیه ایالات متحده انجام داد.
🗣️
در این عملیات، ۱۹ عضو القاعده چهار هواپیمای مسافربری را ربودند.
🇸🇦
۱۵ نفر تبعه عربستان سعودی.
🇦🇪
۲ نفر از امارات متحده عربی.
🇪🇬
۱ نفر از مصر.
🇱🇧
۱ نفر از لبنان.
دو هواپیما به برج‌های دوقلوی مرکز تجارت جهانی در نیویورک برخورد کردند و هواپیمای سوم به ساختمان پنتاگون در ویرجینیا اصابت کرد.
هواپیمای چهارم نیز در پنسیلوانیا سقوط کرد؛ پس از آنکه مسافران برای بازپس‌گیری کنترل هواپیما تلاش کردند.
در مجموع، ۲٬۹۷۶ نفر در این حملات کشته شدند و هزاران نفر نیز مجروح شدند.
تحقیقات گسترده FBI، ارتباط مستقیم این حملات با القاعده و نقش این شبکه در سازماندهی و آموزش هواپیمارباها را تأیید کرد.
پس از حملات، آمریکا عملیات نظامی در افغانستان را با هدف سرنگونی حکومت طالبان و مقابله با القاعده آغاز کرد.
اسامه بن‌لادن سرانجام در ۲ مه ۲۰۱۱ در پاکستان کشته شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/71465" target="_blank">📅 14:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71464">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇹🇷
پهپاد «آکینجی» (AKINCI) ترکیه اکنون با موفقیت موشک‌های UAV-300 و UAV-122 ساخت شرکت «روکت‌سان» (ROKETSAN) را آزمایش و شلیک کرده است.
نقطه عطف این آزمایش، شلیک موشک بالستیک مافوق‌صوت UAV-300 بود که با اصابت دقیق به هدف در فاصله‌ای بیش از ۲۵۰ کیلومتر، توانمندی آکینجی در انجام حملات بالستیک دوربرد را به اثبات رساند.
موشک کوچک‌تر UAV-122 نیز در جریان این آزمایش با موفقیت شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/news_hut/71464" target="_blank">📅 14:02 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71461">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ccd5a9f3c7.mp4?token=APX9lVhZU0ialwtyozX94bbJtaknDCAKVBlRnPSg4lD1D9GD_Lu28SsKQiG8ekiVROdqTyWPSTx8xB21PjOuQvG3zFO9Kxx0G4feyjR-h1uJ5GfVqn_ApCZ0zm55pXK13H0sdnFHBteZT0SODEb_5XcWFgcAC3ItZQQCNrtBmvzG1tNPnMdagoKPk01zcN6HCJfEifJQgiLLCVAeJ32FRg6BOH4AzcmqLKTOvd4PLVPhWabxDYrSY-3Zy6riqlO93vfh8Hk9HobIhuwrODgEFikMKydfWpM_4IPZUQy8GLvSnXeA42skbQc_7HPq1Xb-KUbSL1xgigD-Xa84nBobLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
حمله شناورهای بدون سرنشین (USV) اوکراین به بندر سوچی در منطقه کراسنودار روسیه
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71461" target="_blank">📅 13:20 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71460">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWGfMfxSbYpyJ-d3OUimRnWnd5xCyF7vSLyAkM5gSHubV3fBwRjMGliw2xf071tY_mYUzLhO_uXfWol-S-2XvKpEyvw-p1hvnZTlYMRGOBdQCxRlJx2cO5e67YlgQnxVJnH0BVhSBnfP9JheA8lQLZpP7uSgbkO2K8d8zIIRJh21gZjALdf3Wa6hWFkmzbxeIlGr9TVYfoeY7CY5CNxndzC3bydtwaJoVMlWatdyQjEIyaA55MiJc6Lx0PzaksZbY98ZMJ1cskYXUHKTXPVJPuRgqE7T_UT76WiYEIXgsxaxm4ova0STtPevRWZNgw856ngo69cHHII_ZzhFqCmc6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇾🇪
🇾🇪
حوثی‌های یمن جزیره پریم (میون) را تصرف کرده و کنترل خود را بر تنگه باب‌المندب تکمیل کردند.
⏺
🗞
خبرگزاری رویترز نیز در گزارشی جداگانه اعلام کرده است؛
حوثی ها به شهر ساحلی «ذوباب» — که درست در کنار این تنگه واقع شده — رسیده‌اند.
حوثی‌ها اکنون تقریباً تمام نوار ساحلی یمن در دریای سرخ را در کنترل خود دارند.
این دستاورد سرزمینی را می‌توان از نظر راهبردی، مهم‌ترین پیشروی در کل جنگ یمن دانست.
جزیره پریم در میانه این تنگه ۲۹ کیلومتری قرار گرفته و عملاً آن را به دو مسیر کشتیرانی مجزا تقسیم می‌کند.
تسلط بر این جزیره و همچنین نوار ساحلی مجاور آن بدین معناست که حوثی‌ها می‌توانند کشتی‌های عبوری را با استفاده از توپخانه و تسلیحات کوتاه‌برد تهدید کنند؛ نه صرفاً با موشک‌های دوربرد و پهپادهایی که از مناطق داخلی‌تر شلیک می‌شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/71460" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71459">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71459" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/71459" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71458">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYPH6B9NTq2OOGuDuyIp5zKhHRktqySza1PlT_cqg6gOv5mkv9QccFI2O1yNUiQ9R3jBAwjXsPxLEAJAgYN2FhWpgvcu-OG6y5jos1yNk-5ljsvN-ih6TtdCQ95MDPw91AUUohHfEddc13b51Y_-dGtOlSscSUPRSnr2YwSHlZcIar0BUcg3e_vMNlo4gxbzSCwzCqx3dtyW1rbbByTNeN5RUeMVxvoU7HL_jLDL8nv-dLGtLpXeAzRFq9ji75IIv7IxdxftBVKsXIa1cWo1QmFhhE20wVmly2k08ym7IHfqgxNq2hAiRvCLndtnmR2l68Em3JSc7HhDyplQ8Pmhog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
والنسیا
🆚
سویا
فیورنتینا
🆚
ونزیا
شالکه
🆚
انیون برلین
مارسی
🆚
رن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/71458" target="_blank">📅 12:54 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71457">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4149a89627.mp4?token=wARcd5p148YlDvw_ezcgpfqw9eehQuTADDrLeLOg2HNQJBKjSUSoVcEtFewg0Rt406d3_gecjsKmAcgN-UzSMQgG7Io0aap_7VVNhoXS1HFeQdQwbIXCo9Rj_0fNX78pmld4MvHziKRt7jZwBx_OxmHuwBGe5-aCxqrbTe2A6LIApPalq1U9YRyhiDh0wsaPpZEjc0B3jmK9QwBzxJXkGwt2v5ZiJk3P1TQ651sh0cEsVBqFb2QFwUzMYtwz39PgCWlB-HCMNzuoV1ewX0SQ_KvpJCTGCRnRT0LxKL5TcrBAXVMHzuYPFGt8n_v5B0-EYb_DvXN8nI5_vyDkPj8dKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
کارشناس صداسیما: ما ۵۰۰ میلیون تُن طلا داریم.
ـ مجری:  الحمدلله
+ کل طلای استخراج شده تو جهان ۲۲۰ هزار تنه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71457" target="_blank">📅 12:03 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71456">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/27045da6d6.mp4?token=GXOjyDTTlKTq1FsI5dFfLjL3HGdzMNkVHR_7VruxDaVCXjnkphDunqSwjcbU1xPnCKMp3LWqxIkYM3xh_QGAQ7Pgq8slLXWyKS0iYWY4EjUfYZ3aQxCZjOWUo2t0ZKOt9Zirjti598Gwi2EcRPYQPRGRRsNhhfJj8wnIPVGLCrfuwJdLSUnSuDpklvMsTT07b4TIbYx7VS4O5xGlE3sNCtUMHER26J-Ddaii6qZtHhmeiG4R7O_Z1S8xSYldP1QD4dppn9Megif-cZQsb6E0ggg0yK-gBi-vZrel5OjSIM4H70cL9cXLcOTP9Rm61c7wLkGbDAmzXSa2n6YKkjmitg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر به زنش گفته دست پختت رو سگم نمیخوره! اونم برای اینکه شوهرش رو ضایع کنه، رفته غذاشو گذاشته جلوی سگ!
در نهایت سگه این شاهکارو خلق کرد:
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/71456" target="_blank">📅 11:34 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71455">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c6ecedd2b.mp4?token=RvgOThWCk30BNbhADIwMoqi5QeVsm9vkQKFrxWZUe9M5sV6YjE0OC0z3cl0VNs4qnw6s_J_Kdzl5Qk2H95f9SmQ7txlM0JWoAUiJis1Wv2SXj2daEZUsBu56QvOpymv-C-JU2NPwQc6uaWpRBGw4B12Otv6w04UGc9ggiXsm-GwnGgu4ceU0IX7aoBFNm6URamxC3eDWaCcZCeEXAcljEhXCO_dMnCO58jdWL-zq6Xr_Zw7MHM-OlkoaDGyrhLm0H4O1WdsWZOb8c3zf3BctVqODs6il-ejkPScM8wc1xdAe_3ziwZvik1FKnrUZNbeQFFSdHaFsyhws4pIslm0jPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
این آقا یه ویدیو از چینی‌ها گذاشته که یه شیشه‌دودی واسه ماشین ساختن که با یه بیلبیلک میشه درصد دودی بودنش رو کم و زیاد کرد؛
حالا به جای اینکه پشمای ملت از تکنولوژی بریزه، 98 درصد کامنت‌ها اینه:
بهترین مکان واسه اونایی که مکان ندارن
😟
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71455" target="_blank">📅 11:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71454">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c4f2b29b.mp4?token=PgiT8J66GuhSYCyzzcnzOWQIP--SkJZOgE44OZ5O4J9juGHhrZ4EU-9k787XsKUtc0Fp7NFxBuylVk9d5g2zeHj4ebkKCX4qmcTaMqwdth3PsW9ZgnBIyfXzPJ_CfEmSjGl3BkBXAWuzJN6iPQeV92Zh8wkVUgstRedbU7WX4MFa3Yzn2wMjIgT81MlZrNJ8F0Lli3K0qQ7aXek-QLgObgcafVvoGy1EtpA1j-abwAiII5Yi3zzKf93UYVa77zSV9gbZ2kbSYnfdmO-SuGFN6ePv1HuJasJCpFZbEe9PkIeuApKDcfXk1M3SOeNXOBa0DChqxxd8PKVT2dCQd_2f4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
از سالن زیبایی مذهبی برای عروسی رونمایی شد، از آپشن‌های خاص این سالن میشه به این موارد اشاره کرد:
رد شدن از زیر قرآن هنگام ورود به سالن.
عکس گرفتن با سران مملکت که کشته شدن.
پخش مداحی و قرآن به جای موزیک.
داشتن وضو توسط پرسنل قبل از میکاپ.
خوندن نماز دسته جمعی برای خوشبختی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71454" target="_blank">📅 10:30 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71453">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3b9e0d9418.mp4?token=tlyBjmBMgPsIsklYbo3XFBMrLjYrCO2fE9otVooe4VfGyID3Ok16f-SZdNZKPV9bKVex9GiiKp-sAX2JwxZQoNlxUgXgxSks2SBxq_zRrugk5KaPCBDhKN8pyfFixXfqSmRbIvSiQRAm06081L42LIcJyUGQhml8QOKUYpchEZdf3WsZVfZuvg1z9wpZf-X_WDQUTKezg1DeW7Rq57ZESPwG-A89tkVVJxm5xPqy3YY4i6QM_HGk3qc6crKTwhHBISJnV--rIb0Vf1g3tDt28WIUpESeutZfilB9Hq0Bkiqfm8pAijFUxNhUYZ8eyrfvG32NnrGe4Vw_Wkzv3pHkpg6anZ-UuSfMkKqnZ0OVHrTdXxYXwmFeDs72UTq8GmeQHHWBwsOjFlKVtby_zIRWvl9zonfJem93J7bmYkqdzOgsq7TQEU-rm3fF47431ak1gPJXdriBlkGxZcorsd-rHTy1cxiATFiaxzmqvUntpQcW7OHN1xIgFJJm8VLR-jav5ZgWyB9mDOFMoZgo9EdvnESP7yxtBv4zBfk4Fvj2DR2BxZMCSdOhsqw2XLdn652IKa_LfzM82eIIVIJxCdkCjabYWneCU8MXQ3sljUzBbNmzBD-MM8I-nh_0iaihD3wXJHS70uufmyPLdMkMIDXY21sApaKNu8hZEB3idfa1TyI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه دختر موقع پریود اومده نوار بهداشتی استفاده کنه و با یه صحنه شوکه کننده مواجه شده!
خودتون ببینید...
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/71453" target="_blank">📅 10:04 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71452">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6849173423.mp4?token=fQhnPMJmzMItG44aVNnVnpqBFGNwJqyJOpgy22Y8h_FGbO54zdhDra5OkaSXESTEpc6uEWPDW5gEIeFkSKDApK-JH3FKsYtzkIamPYbGD7EPhXA5nHAzLweJGlOHrtEK77FfdFWNVcIfNRWu5GVyfHMGfcDR1gH_0gcwM7DDquhLIvRrpm8M4w6U1sOxWv2iSnxKfAl1Wm8fYQyoT0dn-bDNlPn86qqQy3SE_B0cWIk6bne0KVyTeccYVRigKMYL0uW_HgWG06K8IO_JrOgwTAMyOhN9416Q0gdSne7uDhTwpG39puedTkd1MfGGUdW1mD8DKSE1lB4dYJ9mM_xYX5BLXP4NCn67GsVExU-U_jSpsm3BuIt5EtjtiU98-lfkYbnlzgpQW648fBRJQ3Qd6D-I9PsgjUeUk1UpDV31cmxoh2n7xSlEJx7tl_8bgBi4YRpcq0LUnQBivgo_JETyRXFL0LTwvg2iJUoXk4g93heYLmkZUfBpoQtqFE_iirb3zHQEAGR4F5ljo0KVDubsP2SiGHieqLynSl3cMVD09IzfSP0Z_y-KJbaPfRiy0vlN8B50zNAgoUq11CozUys7Q7985sc5lhZGWyBYCc2-FvP42ARZNCRXUy_f3673YPJt2E5lKDGen7KwVkgaQWF1QK-k0f8E7lSh4J2Cdnmz10Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
❌
ویدیویی پشم‌ریزون که ارتش اسرائیل از عملیات تخریب تونل‌های زیر ارتفاعات علی‌الطاهر در جنوب لبنان منتشر کرده
😨
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71452" target="_blank">📅 09:32 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71451">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c57019ecf0.mp4?token=YX9XZ2KJMgRu_PAtBVZONCyZbmUmxsLHwDssR7rFJyHGrCoGHS8SeEWwzCxuhbcYrgZZxQ7gs-U68eyNngLZP0eA5o-FmIwdpwH0qZBzYZhlJHElzPpCtBv_JxKHh--K6ek-0f7XpHKlp5qxFreg1SudfqHRk_VwYR_vJOmwwae2oTZhRyVAbG7AyL0wo9G0zsdz613afOWCAlIWCa3fgYeQL-i3TaJbqGs4iZoGGkWIdlWzfh_Kn6tCoWdJPzFz08n87rfEa6TusekjLE57qKcWeRll9rBwyj3-VuS1CkcU8grBO0rm6_uuhPbLrmyIvz8xe6ua8Pru1DyiB-degw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
ترامپ:
اگر ایران سلاح هسته‌ای داشت، ما با آن‌ها تماس می‌گرفتیم و می‌گفتیم: «جناب، آیا ممکن است با هم دیداری داشته باشیم؟»
آن‌وقت رفتارمان با آن‌ها بسیار متفاوت می‌بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/71451" target="_blank">📅 08:45 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71450">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/534815e8ce.mp4?token=neSr7lUO0bss5hqV_mnBkQfdcw3smCYFKqKv10RnqVE3pEW5e3EQu1XteImYOeHjc23xFd5v8dRdFebmwTSkMSJGDMy60QG5kzAqtt0sv8ur0LsVT4cQFpr-83IYGINlCeS6TOSLzyWn3qabLtNAWlfSozYolnrFZE80Rt76l5EFQ9kSkEuFlaMAe4Mwj6jLaTWnIFEMlSIODRog3gZEgK71O8ggT9MXytsvDcLtlhxcbk1WglX3SmRJVuWsqsKRAYZXBteHvLXix0OTmCwrNd-e4aXXAbLYlyigMTmpZzVpSg-xXrcwcGK3w5alBWbnHNPOFp1O5gVmqcSUFFxYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
دیشب ما ۲۲ قایق را از تنگه هرمز بیرون راندیم. می‌دانید، ما کنترل تنگه را در دست داریم. آن‌ها کنترل تنگه را در دست ندارند. آن‌ها هیچ‌چیز را کنترل نمی‌کنند.
آن‌ها تورم ۳۰۰ درصدی دارند. حقوق ارتش خود را نمی‌پردازند. حقوق نیروهای انتظامی‌شان را هم نمی‌دهند.
و بالاخره زمانی فرا می‌رسد که ارتش و نیروهای انتظامی دست از شلیک به معترضان برمی‌دارند. شگفت‌انگیز است که چطور آن‌ها [تاکنون] چنین کاری می‌کنند.
می‌دانید، چین با استفاده از تانک ارتش این کار را با موفقیت انجام داد. یادتان هست؟ کشورهای دیگر نتوانستند. ترکیه نتوانست این کار را بکند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/71450" target="_blank">📅 08:40 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71449">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fa815d3aa.mp4?token=tUMXReSKukfGoFVL21oLNxgP0B1uWW7DBM_jbCehHIRoKl4T1f0SB5N2X9oz8ZCaV-PqUnapyw1AQQnHSuUuTbPx6Bk4whVMvvQWnX4TxCJxT86ZkE97zPnRYHT3PFgsSiaALGGNTvB0-6Gk2HxH8S997JlPs-xRwLAlrcjQ8DPf9vt1fGFqRrGsFSXnrmlZhh42VUP-T3Q1crZkxcTB4K25NrMZh-UMkr2xOWJLCDTIw0CCy1CjXwrrU-SSgbUl8cgDPlQWd9KMBGsfprW6nXr0QNKK0_PFMRPjiekEPkKtLMgYR0SmSwCvwyV0noh4oY7XG18wMIMkzx4_sBnI3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
حتی نومحافظه‌کاران هم می‌گویند اگر قرار است وارد ایران شوید، باید تمام‌عیار وارد شوید؛ فقط بروید و کارشان را تمام کنید.
🇺🇸
ترامپ:
خب، شاید به خاطر انتخابات چنین کاری نکنم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/71449" target="_blank">📅 08:33 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71448">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2230f2a78e.mp4?token=MGiXWHuFxSCXP_ED4jWJX6GQMfyNbIZUytkYElmynz5jfSzgQTL81IqofyCRPSXF1kjPSelqmlugaV9osmC8LktEax22L5q5SDfydQ_dcGzqRzsGN9UBpCLpdDJZlSF_Yekj0LltMuJZE4KTL0QSWvBlwoL8VVBXelj14vgEwQCLiBm27yycAoSQPh3GTxED9TrqBmlQ02nm6BsTbEwSy_NkXJotV7qemQsAAKo9LD3esXch-GK6UDVC8Lz6OAbY-HbSz8VmLiAD-4BAV-OYd0_VXHZk4wgrUfmCICuP4W_LX8XD-hoD5cWWLH3kztz1b6NACKl8shV17kYlrAqWiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ما توان نظامی ایران را درهم کوبیده‌ایم، پس چطور آن‌ها همچنان موشک شلیک می‌کنند؟
🇺🇸
ترامپ:
آن‌ها همیشه می‌توانند موشک شلیک کنند. آن‌ها تعداد زیادی موشک داشتند و هنوز هم تعدادی دارند؛ هرچند بخش عمده‌ای از توانشان نابود شده است.
تولید موشک برایشان دشوار است. بخش اعظم تأسیسات تولیدی آن‌ها از کار افتاده، اما همچنان موشک در اختیار دارند. آن‌ها همیشه تعدادی موشک خواهند داشت، و ما [موشک‌هایشان را] سرنگون کردیم.
آن‌ها ۱۱ موشک به سمت ما شلیک کردند و ما تک‌تک آن‌ها را سرنگون کردیم. البته اجازه دادیم دو تا از آن‌ها رد شوند.
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/71448" target="_blank">📅 08:25 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71447">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a731a8039.mp4?token=gS7LGelhAU-_sssbz-dFYMB3MoEk3gw73uCPSKuVZUTx6byq4pftQoBbpnh9Beb2PUdE5BQsnxBKsUCcKyGmA26IsWhNVzB2_WAmJiTvUxu5hxNeJaaOSSiguTm9EiGm1aZvwp68AqH6I8RUNs050AlFaBEp9ZwDBUv8MtyhZh5rVbeVocSLaPdLhJYok-VTzDKQh9OIZV4u9U3fnoHDc_ncF0gAgw2ixyooJTpJCQcCZBvYSfWPq1_q5OBoT_gJusgWjECOqKcVbo6NnQaYF4Wbo1SsoLBhppdL9xSYvhimM6NJEWDzGtCTB-LUnKv5ldvFdc2B7erc3-DxNvpKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇺🇸
پرزیدنت ترامپ:
ماجرا درست پس از انتخابات به پایان خواهد رسید.
نمی‌گویم چه زمانی، اما فکر می‌کنم درست بعد از انتخابات تمام می‌شود.
آن‌ها به‌سختی و با لنگ‌لنگان پیش می‌روند؛ در مخمصه‌ای عمیق گرفتار شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/71447" target="_blank">📅 08:15 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71446">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dedfdd2dfa.mp4?token=QHcofGujYe7m8V2B6N0RfqcMaFiASDYGv0z6sl2_eKYFGYTVcEl3Yx8Xy6aKHjGEGrQJ8O4ZL8K1enIKCfDnnCcl1WVIAPxzrsFpLb3YII8mX2dkpJBwIpHEXUktkWEtrHeMtT2Mndkqz99yYTebZa5In5UfFtDO40CDfOcwI0nFVWgr6aNoR9vUJBMMCduqSLLw_TQUXXw5kB5hgBHyJkdBzGZLdyDvrA4EuQmbhQhudbz0mwYuavss3gMujQjD9ogUUwlTd6AWI5DSZ-MUm0VpfbBbaxSdodt7qXbpfNSr8GbG8tturHV2owlTjvjk9SjIa8ORHXj_zomVWKBZLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
مجری:
اگر ماجرای ایران پیش نیامده بود، با خیالی آسوده به سمت پیروزی در انتخابات میان‌دوره‌ای پیش می‌رفتید؛ ۲۲۵ [کرسی].» آیا حسرتی دارید؟»
🇺🇸
ترامپ:
«نه، من به واژه "حسرت" اعتقادی ندارم.
آدم همیشه ممکن است کمی به کار خودش شک کند؛ چند نفری هم این سؤال را از من پرسیده‌اند.
اگر قرار بود دوباره آن کار را انجام دهم، دقیقاً همان‌طور عمل می‌کردم. من توانمندی هسته‌ای آن‌ها را از بین بردم.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71446" target="_blank">📅 08:00 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71445">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در TrexBet، بین ۲ تا ۴ عکس چالشی منتشر می‌کنیم که داخل هرکدوم یک Promo Code یک‌دلاری مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.  18:30 → اولین شکار  20:00 → شکار دوم
🦖
• شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت…</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71445" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71444">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSE6IIzfNzfo6leLFDoaUUbKY2phQ6O_zsIZqIQQbugG60XIx2d_fPYxXpO6gXyPJxkeGHDohYcrJJzTAiCMhOrkNiAAtqU3F3QeaX9V3OjL7GjVoDr0mbaJv0vAYaBaVo_itZr0GhscufbX2FCct21lF2iU6xbLgkwqZt6O1VEFbjIcm3CG8cXYLPk1C8fPJClcAd2hKzmOLU3VhRSuUtanNnNRP4xXWlRjSeyUXnzRk5Gw3aHxaXZjhHtoXgwpFEIWrfjw9nxRIwctiDvK06sffGNH8DscvlHR6b8McPL6_0J3ca9LLLS4Rr4xarHuM_i-qUjOF8SLkRCOu8jqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فردا، شکار شروع میشه...
🦖
• هر روز در
TrexBet
، بین
۲ تا ۴ عکس چالشی
منتشر می‌کنیم که داخل هرکدوم یک
Promo Code یک‌دلاری
مخفی شده!
🦖
دو زمان، دو کد، دو فرصت شکار 1 دلاری.
18:30 → اولین شکار
20:00 → شکار دوم
🦖
•
شرایط دریافت جایزه
🦖
فردا ساعت‌ها رو یادت نره...
ممکنه کدی که دنبالش هستی، فقط چند ثانیه با تو فاصله داشته باشه.
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71444" target="_blank">📅 01:35 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71443">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eQk1zsFOLaVKShNuZNgrE3rmN3bpHfqHjxFvN7kO5QE5UtCtA1ANIElT3cGoJtjhgoktoYKGt52XeBY3L1ItYNB6ZcnVaVwE5sMiqjNozZHzabxy1zyRECpVLlcSi5oevacb_PSvR97X4YTaW7sBr_Q_UFY5XlYfzJCOBUYmeYlV1JVbgCdlAM96CyySsBNmJBO3o6qHtK57Y4QXEcm21Gs5ZKl6-lTj9re1vmB36Lr31zY3tDe9pvtwPRQI-tKLMlCW280Qm-mp1dStyUC0ZhFZu0vumsVQo3z3jlPSDyCDAx9rjTu3wNu3x9jiFmV8LZ0_JyZCbmf2tXAc5EiQcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💸
🛢
بهای نفت خام برنت به ۱۰۹ دلار در هر بشکه رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71443" target="_blank">📅 01:19 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71442">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NZKP3Fd86EUk9r6R3ZbjhsD_Ie6BYw3Fgj8ltCmrd-N4C1tJXsk27jhl8RNUTIL2aVR26D1xXxcklvdsTkpmOI1pvusAMBoj7NKSbTcWQTmyUtp23Gdgs9sv_kURHLfdgLd1bVCOjnvjja25rK3d6s57MDV0o7OPl7XFhd_1akEldKST2xmI4_ztt97sxbQBfvP3S2wlfQNGJUytYegZN8UZzyHTBljgBxXASMHaHfrkdsFBFeYPGEoAuOaJoSSh3UTs6VQH5M1bENaE4Y2vQ0Y8Uovq2O0izZQqWq1I1zyh0-VK9t7fhSUDg7VrMlOEsuUxh3M8pI0zfqBcZjNKnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
❌
🇸🇦
میدل‌ایست:امروز برای نخستین بار، حوثی ها خط لوله «شرق-غرب» عربستان سعودی را هدف قرار داد؛ خط لوله‌ای که نفت خام را از «ابقیق» به «ینبع» در ساحل دریای سرخ منتقل می‌کند.
تقریباً هم‌زمان و در حوالی ساعت ۱۷:۵۶ به وقت هماهنگ جهانی (UTC)، کانون‌های متعدد آتش‌سوزی در شش نقطه از مسیر این خط لوله شناسایی شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71442" target="_blank">📅 00:57 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71441">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cllPT-3136iZ7oRkQSeup1xEQlRXgklpSaq4g3cWlk53qb2xce2w50omY66bFuMRCY2-SDBOEisk8fNkUU0MBLoSzfrT_U6yDt3oyoqBKsp3bqYuCsHclIWNDkOR7IX6badHNf7pkoap0O0vuKIGGU-FIWhiHJtdaCfXFshEtVbk7W8GKfEoVZEWxZbtLSoPoWR1Ls4rs7_vMHAbwpYTcje3BFZSqsX5uxYrHsf99vAEiYsBA8Z-BaOLY-y1jDzH0yeKNSRCZcWF6U3BgKiXbM07t5um5VRZ2Ro1fe2-mY4dO-jDJgKo1-ZMZJg0gGr8S9a4Kn87Vd1Lc5nMIm0s9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
دو شناور در تنگه هرمز، در فاصله ۴ مایل دریایی غرب عمان، هدف قرار گرفتند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71441" target="_blank">📅 00:36 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71440">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">⏺
🇮🇱
❌
🇱🇧
ارتش اسرائیل اعلام کرد که برای تخریب زیرساخت‌های تونلی در زیر ارتفاعات «علی طاهر» در جنوب لبنان، بیش از ۱۱۰۰ تن مواد منفجره به کار گرفته شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/news_hut/71440" target="_blank">📅 00:28 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71439">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=lkMy2QUq15zHy-t3dLU3h79qdAgnEXDAVFNHQvXY2HjL5hUHBIximc6UjvIkanabeJzVVGT8ZfFYLbmlTz-toorgvXlTbqSiziKvxe5bBxxrnuOiHcmi1Z9hqnqP1b5_4rshTSPB5fmvuqTesDabycFrST5GQ_bZ3rnh8hbUSjUo79mKTE3AuOXKNtNpwxCOxx5czy7a_H53GWKFJ50bq_p7_wzX1WxmMN3d-i7HRbGxPFss7p4lS5zSTaF5h9dRXwnxukaTTTidV3Vv6imI9vvMZ-dKayRMDxA4uC7XZbtsZwmtEO1gI_gUyBwluGgW_SGT0UIC9EL1BGreqItL1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae4183a669.mp4?token=lkMy2QUq15zHy-t3dLU3h79qdAgnEXDAVFNHQvXY2HjL5hUHBIximc6UjvIkanabeJzVVGT8ZfFYLbmlTz-toorgvXlTbqSiziKvxe5bBxxrnuOiHcmi1Z9hqnqP1b5_4rshTSPB5fmvuqTesDabycFrST5GQ_bZ3rnh8hbUSjUo79mKTE3AuOXKNtNpwxCOxx5czy7a_H53GWKFJ50bq_p7_wzX1WxmMN3d-i7HRbGxPFss7p4lS5zSTaF5h9dRXwnxukaTTTidV3Vv6imI9vvMZ-dKayRMDxA4uC7XZbtsZwmtEO1gI_gUyBwluGgW_SGT0UIC9EL1BGreqItL1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
ویدئو دیگر از تخریب کامل پایگاه عماد ۴ حزب‌الله
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71439" target="_blank">📅 00:12 · 20 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71437">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tokWszePMWSVmFe5z6ZFTVGfxZzlgNREHIHcRSsRCCf6yBJw2RCzOK34hTLcIvDL5667nzmNo-5ycrLDvE-TUpW22KckPKly-sez9WXJYrl2DkFZgNlcGSSfujmH3ltkbE2k5LgZnCTpmgHkesaRMTDiI4Ce8b48XuQexxZXOXi3mltoZROWh91i6Mu5ijx43ag-7Ew1B5oVQnNtY-oblAq8v1GezBwTilQh-28y85bQ-vRUouRey8oJJ5Ro3JAjhzQ_oWTGOM6Ax9YPdAq3v99fI26dQb0vbhl5pjT0EfpSCg5x0luQd1lp3wN0ov2leeBPkaB8N697CTgxK5x04w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f4770f428.mp4?token=tokWszePMWSVmFe5z6ZFTVGfxZzlgNREHIHcRSsRCCf6yBJw2RCzOK34hTLcIvDL5667nzmNo-5ycrLDvE-TUpW22KckPKly-sez9WXJYrl2DkFZgNlcGSSfujmH3ltkbE2k5LgZnCTpmgHkesaRMTDiI4Ce8b48XuQexxZXOXi3mltoZROWh91i6Mu5ijx43ag-7Ew1B5oVQnNtY-oblAq8v1GezBwTilQh-28y85bQ-vRUouRey8oJJ5Ro3JAjhzQ_oWTGOM6Ax9YPdAq3v99fI26dQb0vbhl5pjT0EfpSCg5x0luQd1lp3wN0ov2leeBPkaB8N697CTgxK5x04w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
🇱🇧
#فوری
؛ارتش اسرائیل عملیات تخریب تونل های زیر ارتفاعات علی الطاهر را شروع کرد.
تصاویری که لحظه انفجار تونل‌های زیر «ارتفاعات علی‌الطاهر» در جنوب لبنان توسط نیروهای اسرائیلی را در همین لحظات پیش نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71437" target="_blank">📅 22:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71436">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/249279a367.mp4?token=AnuRZtms80vSbBsDhjDUKeOtNcIOe3U9115QDgZ1q4S9-Zs6O9LCUl5EGNYdr_T5gZYXt8wnelpCpP83RsoeIbVtV7EO277_Xst7ioixTm7VqDMdiNwDbt5FG_hw2sLOHdqyt4iVziIUae9d92fT3O2dxEDmMgoRkIuy2ivqb_uX4jyysF_gF1nKoUAI-gTnPfHe9LaHKW4G0BNeMxtupQMyssKIpPE0ZodaXu0psChlqzvOavU1ihm0I83Zu8SFIPxKOm9tE3BrbwCbtjoUHSCqevfBfNRoGzhpgdPe9q3URG2KqTZrKDF58RNXo_MKlCVPvhI4CqWCjDBHBu-fsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/249279a367.mp4?token=AnuRZtms80vSbBsDhjDUKeOtNcIOe3U9115QDgZ1q4S9-Zs6O9LCUl5EGNYdr_T5gZYXt8wnelpCpP83RsoeIbVtV7EO277_Xst7ioixTm7VqDMdiNwDbt5FG_hw2sLOHdqyt4iVziIUae9d92fT3O2dxEDmMgoRkIuy2ivqb_uX4jyysF_gF1nKoUAI-gTnPfHe9LaHKW4G0BNeMxtupQMyssKIpPE0ZodaXu0psChlqzvOavU1ihm0I83Zu8SFIPxKOm9tE3BrbwCbtjoUHSCqevfBfNRoGzhpgdPe9q3URG2KqTZrKDF58RNXo_MKlCVPvhI4CqWCjDBHBu-fsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇱
#فوری
؛نخست‌وزیر نتانیاهو درباره ایران:
رئیس‌جمهور ترامپ امشب اعلام کرد که ایران بار دیگر در تلاش است تا به سلاح‌های هسته‌ای مجهز شود. این سخن درست است.
پس از آنکه ما توانایی فوری آن‌ها برای تولید بمب‌های هسته‌ای را از بین بردیم، آن‌ها دوباره دست به کار شده‌اند.
من اینجا، در کنار «دیوار ندبه» و در آستانه «روش هشانا» (سال نو یهودی) به شما قول می‌دهم: تا زمانی که من نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.
هم‌زمان، ما در حال ضربه زدن به محور ایران هستیم؛ نه تنها ضربات سنگین در نوار غزه، بلکه در لبنان نیز. ما ارتفاعات «بوفورت» را درهم کوبیدیم و اکنون در حال نبرد بر سر ارتفاعات «علی طاهر» هستیم.
اقدامات بیشتری در راه است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71436" target="_blank">📅 22:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71435">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">یه بوهایی میاد، مثل اینکه آماده دارن آماده می‌شن تا دوباره مراکز هسته‌ای ج.ا رو بزنن
#hjAly‌</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/71435" target="_blank">📅 21:18 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71433">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3OPYeH6J9E5ZjIhbUBjONNcRRabVaIrxKuMJA4Qy8ois7PJPRHM52M38ZXuxiTMDGy0KZgH4BF1TNFjlLcJNqcHr4c71zhocDsC_tcByJ2FsrsSyxvazYl85fvh6bqjj7GgiArmY9Qi0R0j_Lr0SD2khLavHadxm5GVheI8IGL_-acwJ9tDfbYKejIEhIsb1IISqtdnyxlN_HWxWMrRpjlocfOuf1_Hn5D_zz5I396s-k508ksAVf1N9Wm1EAZBZOrT3X8blCZ76Gewldk7Pz7gWG41BEnFVW2A9h0ZOKYCBN73U_vI64IOzCiqu-STWEhnkum5HoisJdFJVM9KYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d882666df.mp4?token=OYUNuBUHSHlhrfbybO5e2sov3UHt1-tg_l-LjH9Ah2QeBs9azDqGJ-yIHk6thz_CO7yjziCD_Nga_U1n7STPcUPjGlggzv5KQTiP7fawN6RuVpCUogMNsb9U-KGIqjaZPzbcaih6-Tjc85iPxwzdj67cc3K0DxTgmt3oUrAkvVMvccNcgTTS334XeQUqYPPp1DDGvltF6ajmIu_fLtLA3v13SuJqQmulHnVMM3zrAJ6FOWZ0Ec7IzqWPYODNZj1V1yzw-wt2_2_mtjp7Lr2CBxLBQ81MffbCimnF-AVIParRt0OHkxtQH13Cb3p_Vz2lwiBr-c3ccHgOeS3T3Q87EQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d882666df.mp4?token=OYUNuBUHSHlhrfbybO5e2sov3UHt1-tg_l-LjH9Ah2QeBs9azDqGJ-yIHk6thz_CO7yjziCD_Nga_U1n7STPcUPjGlggzv5KQTiP7fawN6RuVpCUogMNsb9U-KGIqjaZPzbcaih6-Tjc85iPxwzdj67cc3K0DxTgmt3oUrAkvVMvccNcgTTS334XeQUqYPPp1DDGvltF6ajmIu_fLtLA3v13SuJqQmulHnVMM3zrAJ6FOWZ0Ec7IzqWPYODNZj1V1yzw-wt2_2_mtjp7Lr2CBxLBQ81MffbCimnF-AVIParRt0OHkxtQH13Cb3p_Vz2lwiBr-c3ccHgOeS3T3Q87EQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇷
نیروی دریایی سپاه پاسداران انقلاب اسلامی  اعلام کرد که یک فروند «سیل‌درون» (Saildrone) — یک شناور سطحی بدون سرنشین (USV) که برای نظارت و شناسایی دریایی به کار می‌رود — را در ورودی تنگه هرمز هدف قرار داده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71433" target="_blank">📅 20:54 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71432">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
بلومبرگ:
آژانس بین‌المللی انرژی اتمی می‌گوید فعالیت‌های جدیدی را در سایت بسیار مستحکم کوه پیکاکس ایران شناسایی کرده است، اما هنوز هیچ مدرکی مبنی بر آنچه در داخل این مجتمع زیرزمینی اتفاق می‌افتد، ندارد.
رافائل گروسی، رئیس آژانس بین‌المللی انرژی اتمی، گفت بازرسان به این سایت دسترسی پیدا نکرده‌اند و به تصاویر از راه دور متکی هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/71432" target="_blank">📅 19:45 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71431">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=AefI8q4jn24kAUMA6xikcwwxVjGIpfpjYPWIV-MIsRUuittNDGvBdadabjzfox4Zqhm973YTmonZXUCYvGWRBn0eTjz-38OG7zkCIYT-llWvNpdFSHWhBiT9Ei4gvNedja17nJ4tfAbnGOc3fQyfyvxtagwr1mk822SQlibT5BrTPiFkYY9crqIjrKw0-VRBZWo8_hAFDofupqpJdxG45oxlU2oOicLX8f0DWueA9JK9i2DpxQZZ9_IFI7xoA4_UsWvCAV6k_nMVTobe3Qfrfo4tBJzUYjHjfyd2oCN1l_At5K_7Yi6UwdJUldc6utVje48LfNcX02193Ow2Caspr1Ma6tIG_LWQVT3quQu7flhLOaSUN6XEtBkvg6mFyLkysxEBw4brsts6p5nw6RwixVlHczvKJjuo7_eVSlKRXDQNzQE_jsh-8kNwEZKfm2FmhfhCyJ5X9ZUKvF1m6sQ18q2lCbuwTnA4CZd1-OR_5Q-6Q6U4x4a_A6arJn4EAsovjK42Mj5bomBmUslfK7tIlOyBfCTKt0rS-0r72dcr08ojwkAdYMU0OOewCVWTTSAgTwLma1n0ovFAk9MyPC0wt4Syy2L_oR_QQBfAjnUZBQ4ivy6XE7qEDDXfH3iPLEkvcuqs5soJOtk_A9QYkBH3T3UbAEKx8wYJyxdOSTE53Fs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3ebe5e9d2.mp4?token=AefI8q4jn24kAUMA6xikcwwxVjGIpfpjYPWIV-MIsRUuittNDGvBdadabjzfox4Zqhm973YTmonZXUCYvGWRBn0eTjz-38OG7zkCIYT-llWvNpdFSHWhBiT9Ei4gvNedja17nJ4tfAbnGOc3fQyfyvxtagwr1mk822SQlibT5BrTPiFkYY9crqIjrKw0-VRBZWo8_hAFDofupqpJdxG45oxlU2oOicLX8f0DWueA9JK9i2DpxQZZ9_IFI7xoA4_UsWvCAV6k_nMVTobe3Qfrfo4tBJzUYjHjfyd2oCN1l_At5K_7Yi6UwdJUldc6utVje48LfNcX02193Ow2Caspr1Ma6tIG_LWQVT3quQu7flhLOaSUN6XEtBkvg6mFyLkysxEBw4brsts6p5nw6RwixVlHczvKJjuo7_eVSlKRXDQNzQE_jsh-8kNwEZKfm2FmhfhCyJ5X9ZUKvF1m6sQ18q2lCbuwTnA4CZd1-OR_5Q-6Q6U4x4a_A6arJn4EAsovjK42Mj5bomBmUslfK7tIlOyBfCTKt0rS-0r72dcr08ojwkAdYMU0OOewCVWTTSAgTwLma1n0ovFAk9MyPC0wt4Syy2L_oR_QQBfAjnUZBQ4ivy6XE7qEDDXfH3iPLEkvcuqs5soJOtk_A9QYkBH3T3UbAEKx8wYJyxdOSTE53Fs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
جورج دبلیو بوش درباره افغانستان:
این باور وجود دارد که همه خواهان آزادی هستند؛ و ما این را در افغانستان دیدیم.
برخی می‌گفتند: «خب، آن‌ها نمی‌خواهند آزاد باشند؛ آن‌ها... می‌دانید، اصلاً تفاوت را نمی‌دانند.»
البته که آن‌ها تفاوت را می‌دانند.
دختران جوانی که برای نخستین بار در زندگی‌شان به مدرسه می‌رفتند، تفاوت را درک می‌کردند. زنانی که پزشک و استاد دانشگاه می‌شدند، تفاوت میان یک جامعه آزاد و یک جامعه استبدادی را می‌دانند.
و متأسفانه، آن زنانی که در مسیر شکوفایی کامل استعدادهایشان گام برداشته بودند، دیگر فرصتی برای تحقق آن پتانسیل کامل ندارند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71431" target="_blank">📅 19:40 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71430">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71430" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71430" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71429">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCrQ3amZyseU3R4omfeNvbmRgtWA7b4p6nCrhWMcJ9V34lGhgGVsURLn0EGjBJ9HLvWGFBu9BMWhYKqKBIXWvquPsRtPLFXlxfz5s-DrGVnnlQHK-cte1EHHw9hD1IjHkuyLXlcDiKbLMZjMNPF9efoZcLnzMhGoHP4xsV4iKIftHPUqIcpRaqYwv6L8Los4OKA0p95vhUi5PTwAn8OUVwJup_aQEO2ODDYcKp6iCxB9cW9Gb1F-DA9u7Hgc8tejADCLQrZBtQSoMEyd1WPYFpd7UrzlyLSxssaG5x7XhVnYl4cq4Tk1Cj8kV-g8nRBNVDbX3lZBOk3MDElnw6SmSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فوتبال اروپا امشب دیدنی‌تر از همیشه!
🦖
بازی جذاب صباح
🆚
منچستریونایتد را در سایت بین‌المللی
TrexBet
پیش‌بینی کنید.
📊
نگاهی به آمار ۲ تیم در تقابل‌‌های اخیر:
صباح: ۵ بازی, ۴ برد, ۱ شکست و ۱۳ گل زده
منچستریونایتد: ۵ بازی, ۱ برد, ۲ تساوی, ۲ شکست و ۱۰ گل زده
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/71429" target="_blank">📅 19:39 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71427">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=tjvxZi28h0GkGBjw_LYlDpZjgF2VXP3prAwFIJLWiiN9XCJ35mSHgeA3T6K-XFQrru9Qai5oWWkCeNj1HpuQzmYr1BnrLNBw_a-Z1ICUBeIKTIwdswC9dMDtYQtA4rGmDtB7jrVveMxCTPYKuSGk-d_Sn4Nz946LpNEPokFQ-byD74ioleZ1kfR4LWYFj5KG5kzmIl3XSiGkRgLUrQp-CD3FaKD6DEeHgmOFWBDP1vhaiw4q8lzYKDi30q-TxhRCU_IA_zgsJwXkbvJ24UAioiBM0ebqf1dTsQBVcyibEacUXrC-kHhw10UXOL8sqs1vHMIxnsRmC75wEMDuDR4emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd5897a7d3.mp4?token=tjvxZi28h0GkGBjw_LYlDpZjgF2VXP3prAwFIJLWiiN9XCJ35mSHgeA3T6K-XFQrru9Qai5oWWkCeNj1HpuQzmYr1BnrLNBw_a-Z1ICUBeIKTIwdswC9dMDtYQtA4rGmDtB7jrVveMxCTPYKuSGk-d_Sn4Nz946LpNEPokFQ-byD74ioleZ1kfR4LWYFj5KG5kzmIl3XSiGkRgLUrQp-CD3FaKD6DEeHgmOFWBDP1vhaiw4q8lzYKDi30q-TxhRCU_IA_zgsJwXkbvJ24UAioiBM0ebqf1dTsQBVcyibEacUXrC-kHhw10UXOL8sqs1vHMIxnsRmC75wEMDuDR4emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
🇾🇪
تنش‌ها میان نیروهای تحت حمایت عربستان سعودی — یعنی «نیروهای ملی» (NRF) و «نیروهای امنیتی ملی» (NSF) — و نیروهای جنوب یمن که پیش‌تر وابسته به تشکیلات جدایی‌طلبِ منحل‌شده‌ی «شورای انتقالی جنوب» (STC) بودند، رو به افزایش است.
فرماندهان جنوب یمن مسیر عقب‌نشینی نیروهای NRF و NSF را در کریدور جنوب‌غربی «عدن-لحج-تعز» مسدود کرده و از ورود این «نیروهای شمال یمن» — که کاملاً مسلح هستند — به قلمرو جنوب جلوگیری می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/71427" target="_blank">📅 19:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71426">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V_d84FDf5RV7Ii93PDNGcbd9iRJFCypDFH-e98O4nL_fCpyln4mmAFhvtlQalKOsQDPFtJySSqlcWnz7Y5U35Mgb74Yf-ubaU6lc_nD204XGTDF-UVFeIEp-d7PG25Rax4jWFZA63mhHtqXkFEqqqTid-DuvIU1ydBvmJOpV67SBXl6FJjwOW-eKFLBBeSlv3pXPP8Lqd07yShs60vLn9vnV_aTzzo6PPzUGsNgPxpj_FG9gVvIU2rUw9QrkfVpS-XDxRmqDVGzNWARRCPo6zGI4e8v3mag7agayAbAEKFfi5CcyxLk3kFvTsnN9PpfYiLhTZ4U8ud8Xnhv36dtsBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇨🇳
🗞
به گزارش رویترز، ایران از یک سازوکار محرمانه و شبیه به تهاتر برای تبدیل درآمدهای نفتی به اعتبار جهت خرید کالاهای چینی استفاده کرده است؛ اقدامی که به تهران در دور زدن تحریم‌ها کمک می‌کند.
طی سال گذشته، مبلغی بین ۲ تا ۲.۵ میلیارد دلار از طریق یک «سازوکار ویژه» (SPV) جابه‌جا شده و صرف خرید اقلامی همچون دارو، وسایل نقلیه، تجهیزات مخابراتی و — دست‌کم در یک مورد — تجهیزات پدافند هوایی به ارزش میلیون‌ها دلار شده است.
این سیستم شامل نهادهای مرتبط با چین و ایران است که مدیریت درآمدهای نفتی را بر عهده دارند؛ بدین ترتیب که حدود ۷۰ درصد از وجوهِ تحت مدیریت شرکت چینی «چو‌شین» (ChuXin) به پروژه‌های زیرساختی اختصاص می‌یابد و مابقی آن برای پرداخت به تأمین‌کنندگان چینی، به آن سازوکار ویژه (SPV) منتقل می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71426" target="_blank">📅 19:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71425">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🍏
اپل از نخستین گوشی هوشمند تاشوی خود با نام «آیفون دو» (iPhone Duo) رونمایی کرد.
این گوشی در حالت بازشده، باریک‌ترین آیفون ساخته‌شده تا به امروز است و نمایشگری ۵۰ درصد بزرگ‌تر از آیفون ۱۸ پرو مکس (که به‌تازگی معرفی شده) دارد.
قیمت مدل ۲۵۶ گیگابایتی آن ۱۹۹۹ دلار تعیین شده و عرضه آن از ۲۳ اکتبر آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/71425" target="_blank">📅 18:15 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71424">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/HnJII3mIfz1m6OR5CKlRqLgWMj_YNgTqGt9GSi7-HNh0vflO_Mg4qrU0_Aw2h2LdPdnfj4yM-s0bPLviVp2ZA79GuJxkx5d_-p7Tvf26_EiQ5NPd6Uc-8cRVduGu2CV-Ay_UwE6rh4413G6mwyWhsn4x4rQfCz6gAu1tjiJAHrAex9WmwyNI2CRWmwXyo311L3cmWc6toPbTH2HvfgRFZKT2FEEscHAGchSIOh1CBZrKayQFK0CAFOclV9ZX9mvGZzKt7UmJK2WGf120WL7rBq0R2lR01oFxv37yqmAWeLjYfwou7slRkhGvKpaHIm7uR-JJh1OWgArPSqZCbsH4_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شروط عجیب پدر عروس برای ازدواج
😳
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/71424" target="_blank">📅 17:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71422">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cJHE2MO7OESVRtnsHBgtkxhGbIhskyHZ0UUKaPVveYoOpKeZcrpLzLxekXYMBycuXhjFBYQK5o38cZIZAJwIlfttQpK6ELP9EY93TIVo1gIv_MNQOA9j3lzmIQdhn9FLiTc2LoXUTlzsyduFflEiBU_l5OjjXlb4SPRT7XG8EIVfh18Kxy-bWmh5GVEgO1tKn1bSS6yjcQIg6lL6T831voul_DBYCq7a3XH3NC8QBk7p8O8bQUVq5bfQCV3Up7oIXSrcW_3PPcPyr8t_ZdowH5jKCajXZL6fSBXfLDCRJMqoTiCG3EGY2hzhN0sgge2fOrr-Z3UcH1lpYvt-BWiLZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=GDVbhi9eWd6Efq-TrN9SF8a3AJg517cC886QfNRz52SjMyITyTkYPQHaOP08gtUjJA3LRgmXGfpSXf4krMk-YvAPo-foq4BBsjLdgimYyLXjV2ayNcObvS6AewckaBznWvMs8-U8X5zOypLg-dshtmyiVsACoH6vJyQjLaJtqixj0ozWBUizXrUZrqiCoSzST3puOJJMo9XpO7DRj_3iIKBAR_kYY0g80wiXMX0zmqu913g9rOC1E5u5nlPbyllo-X8rPayO5hd_FnQs2L7DLN0Qu-AvRjX4hYLk636rC5E2_6RmaZf4beqNr3usybUZfaHQuEdp9PlN812wHBgClQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dfa56bc26.mp4?token=GDVbhi9eWd6Efq-TrN9SF8a3AJg517cC886QfNRz52SjMyITyTkYPQHaOP08gtUjJA3LRgmXGfpSXf4krMk-YvAPo-foq4BBsjLdgimYyLXjV2ayNcObvS6AewckaBznWvMs8-U8X5zOypLg-dshtmyiVsACoH6vJyQjLaJtqixj0ozWBUizXrUZrqiCoSzST3puOJJMo9XpO7DRj_3iIKBAR_kYY0g80wiXMX0zmqu913g9rOC1E5u5nlPbyllo-X8rPayO5hd_FnQs2L7DLN0Qu-AvRjX4hYLk636rC5E2_6RmaZf4beqNr3usybUZfaHQuEdp9PlN812wHBgClQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
⁉️
به گفته تحلیلگران CSIS، تصاویر ماهواره‌ای امسال «افزایش آشکار فعالیت‌های ساختمانی» را در کوه عمیقاً مدفون پیکساکس (Pickaxe Mountain)ایران نشان می‌دهد.
آنها ارزیابی می‌کنند که این سایت پوشیده از گرانیت «احتمالاً» به عنوان مکانی محافظت‌شده برای کارهای مرتبط با هسته‌ای، احتمالاً محل مونتاژ سانتریفیوژ، غنی‌سازی اورانیوم یا سایر فعالیت‌های «مرتبط با سلاح‌های هسته‌ای» در نظر گرفته شده است.
این تحلیل افزایش فعالیت جاده‌ای، ورودی‌های تونل تقویت‌شده و مرتفع، جاده‌های داخلی آسفالت‌شده و سایر کارها را نشان می‌دهد که نشان می‌دهد ساخت‌وساز از حفاری به سمت توسعه داخلی تغییر کرده است.
اطلاعات اسرائیل حاکی از آن است که ایران می‌تواند سانتریفیوژها را به آنجا منتقل کند، در حالی که ترامپ اخیراً هشدار داده است: «ما ممکن است خیلی زود پیکساکس را بزنیم» و افزود: «ما همه کسانی را که در حال حرکت هستند می‌شناسیم.»
پیکساکس حتی برای سنگین‌ترین بمب‌های متعارف سنگرشکن پنتاگون نیز بسیار عمیق دفن شده است. سی‌ان‌ان گزارش می‌دهد که ایالات متحده برنامه‌های حمله عملیاتی برای این تأسیسات دارد و به مطالعه راه‌هایی برای حمله به سایت‌های عمیقاً مدفون ایران ادامه داده است.
چند روز قبل از شروع جنگ ایران، پنتاگون همچنین یک قرارداد اضطراری ۱.۲ میلیون دلاری برای آماده‌سازی در یک مرکز آزمایش زیرزمینی گرانیتی در محدوده موشکی وایت سندز (White Sands Missile Range) صادر کرد. منابع به سی‌ان‌ان گفتند که این کار با توسعه و آزمایش قابلیت‌ها علیه عمیق‌ترین تأسیسات زیرزمینی ایران مرتبط بوده است.
ارتش به‌طور جداگانه در حال توسعه یک «نسل بعدی نفوذگر» است تا جایگزین نفوذگر مهمات عظیم مورد استفاده علیه سایت‌های هسته‌ای ایران در طول عملیات میدنایت هامر (Midnight Hammer) در سال ۲۰۲۵ شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71422" target="_blank">📅 17:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71421">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=uAk8dVDqNNWmRbzl97LYFlPtXOamHehVgU72BISQx3MINENKYHDBfpH59PNB7QNMKThTzi1fXcR4_Mtiqng2-BSqEA2__4XZ6CFNYDD4PDUXuGrb5Bp601PdCQOkPztjJie1xpUMs5LQbAWcyY3ddJYgU5O7lNYMkad0QgI59O7rIvVcwN1dvjFYIsKeYXcWsViKJfcPthEgq5cxqpAjVv61Xcd2lTTq3d9HDXDxt5crfXPOI-Y9Sk0spsf9xFkunAr2EwsHMPP7EHL2ekDjamrrra5FDD_5zig84O2OMkiSI7p-GXUCmoJ5WqgbF0ltmEVnoMIr6uLZeII8vrG8Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e8709946e.mp4?token=uAk8dVDqNNWmRbzl97LYFlPtXOamHehVgU72BISQx3MINENKYHDBfpH59PNB7QNMKThTzi1fXcR4_Mtiqng2-BSqEA2__4XZ6CFNYDD4PDUXuGrb5Bp601PdCQOkPztjJie1xpUMs5LQbAWcyY3ddJYgU5O7lNYMkad0QgI59O7rIvVcwN1dvjFYIsKeYXcWsViKJfcPthEgq5cxqpAjVv61Xcd2lTTq3d9HDXDxt5crfXPOI-Y9Sk0spsf9xFkunAr2EwsHMPP7EHL2ekDjamrrra5FDD_5zig84O2OMkiSI7p-GXUCmoJ5WqgbF0ltmEVnoMIr6uLZeII8vrG8Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
عباسی معاون وزیر راه و شهرسازی دولت سیزدهم:
آقای رئیس‌جمهور!
مگه نمی‌گید هرکی می‌تونه کار کنه بیاد؟
من می‌تونم
کجا بیام؟
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71421" target="_blank">📅 16:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71420">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4aea684770.mp4?token=fGwMZyEOZ-PgFXyhxhgf0Uz6ZJvDZ4qKnA3K8DjYUOS9XxP_Rn-5GGSZQw-FclhoihwF8UjqkW0NbSkUqhRd9-_hunCzDBJwpCzPGoaPwMOZHWuHfBHuBnYwifzhAJGyEb-YdLm_uQ3K-pX-kpp-SXv0MHqx1_rMbxqPNZQpt5y6VOZ5IyUKGa0D4iVL5HwLnGqE7M2s63qmKmuUEczXhQqcSdvUxbvTNZ7maYfVT-687juUSh16oQgdSRC3kAXg-C5KxOjbf57qsoQvFeIB-eBx-nFKPlnIGpTopf0zB-aIrWWsYq9TdX0eKm0Hcg0yvaFQjG6iN0oGjc1DSi25YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4aea684770.mp4?token=fGwMZyEOZ-PgFXyhxhgf0Uz6ZJvDZ4qKnA3K8DjYUOS9XxP_Rn-5GGSZQw-FclhoihwF8UjqkW0NbSkUqhRd9-_hunCzDBJwpCzPGoaPwMOZHWuHfBHuBnYwifzhAJGyEb-YdLm_uQ3K-pX-kpp-SXv0MHqx1_rMbxqPNZQpt5y6VOZ5IyUKGa0D4iVL5HwLnGqE7M2s63qmKmuUEczXhQqcSdvUxbvTNZ7maYfVT-687juUSh16oQgdSRC3kAXg-C5KxOjbf57qsoQvFeIB-eBx-nFKPlnIGpTopf0zB-aIrWWsYq9TdX0eKm0Hcg0yvaFQjG6iN0oGjc1DSi25YTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
حامیان حکومت این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین، دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، ذلت نمی‌پذیریم.
بنزین رو کم میگیریم، ذلت نمی‌پذیریم.
دلاری گوشت میگیریم، ذلت نمی‌پذیریم.
مهریه کم میگیریم، ذلت نمی پذیریم.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71420" target="_blank">📅 16:02 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71419">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=lCzLzps1zciRp24oMZ6gLnmrHGGGwYDwefbhlUw3vQ8_UO2pmtNSUsYI123ra46lVdRV_hNtjYktzaEFnwLbJWQSBm9LmiMvVUBHexSJJwUO36WRC6ookJ55BNtxCm8_TjVT6PZAmkZMRu4lg4Tz_LpvjupWh5KPdWB8SBwv6Ai-rL_3UgORAJCpQoW-Sc-3sQO5CslCv9HeLa5FzIr5R6_nUkjWwyNf_R8ofyB1tONO1liAzrxzGpOF34OVrSki9Pq1gkgADI7Lbc__MgQ2qVfR5RpF9fZ9ADweFN3ViOv_4Jm2yXF43srTW-XQnHS4JZ7fbF_u8hi3fL93zeaZfQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1669b7ca35.mp4?token=lCzLzps1zciRp24oMZ6gLnmrHGGGwYDwefbhlUw3vQ8_UO2pmtNSUsYI123ra46lVdRV_hNtjYktzaEFnwLbJWQSBm9LmiMvVUBHexSJJwUO36WRC6ookJ55BNtxCm8_TjVT6PZAmkZMRu4lg4Tz_LpvjupWh5KPdWB8SBwv6Ai-rL_3UgORAJCpQoW-Sc-3sQO5CslCv9HeLa5FzIr5R6_nUkjWwyNf_R8ofyB1tONO1liAzrxzGpOF34OVrSki9Pq1gkgADI7Lbc__MgQ2qVfR5RpF9fZ9ADweFN3ViOv_4Jm2yXF43srTW-XQnHS4JZ7fbF_u8hi3fL93zeaZfQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
رقابت رژیم جمهوری اسلامی با اپستین در کثیف بودن:
یه مرد ۴۲ ساله دختر ۱۴ ساله رو به عنوان زن سوم صیغه کرده، بچه حامله‌ست است و داره سزارین میکنه
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/71419" target="_blank">📅 15:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71417">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=NArIEKp4lPDk8MMZgk47wfuE8iL6xH92dGnHkIQ_5pW4GQewHAv-J30bk88T_vXMOu35XTsKUMaR-WECXPURvDJUScisCG2TvBP3AkKhz98GsoKr1Q_6bt8m7RYGaYN4QA_IPOnVpZl4acU6DWeo_ZOYSTHhvvXSAej7NJZbJvZuhnt53Rja8UBGUNqlpkWHxUchSZ5Y-2xVdVS5WcWc3Q9UNV20bgFw4T9U-xpJfD6KhdF3x_IU3bmcVkJiFOS_wjRSUoCfw3ScncfRVONs33aB8GFQ1guwku0b8H7TAns-EYDn-1jbT7S_4Wn_lX2_0kK-ex0lufyKzSqTLJBKdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e97f71ba05.mp4?token=NArIEKp4lPDk8MMZgk47wfuE8iL6xH92dGnHkIQ_5pW4GQewHAv-J30bk88T_vXMOu35XTsKUMaR-WECXPURvDJUScisCG2TvBP3AkKhz98GsoKr1Q_6bt8m7RYGaYN4QA_IPOnVpZl4acU6DWeo_ZOYSTHhvvXSAej7NJZbJvZuhnt53Rja8UBGUNqlpkWHxUchSZ5Y-2xVdVS5WcWc3Q9UNV20bgFw4T9U-xpJfD6KhdF3x_IU3bmcVkJiFOS_wjRSUoCfw3ScncfRVONs33aB8GFQ1guwku0b8H7TAns-EYDn-1jbT7S_4Wn_lX2_0kK-ex0lufyKzSqTLJBKdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو وایرال شده از مراسم ازدواج فوق لاکچری «سامان گوران» بازیگر؛ کمدین و مجری صداوسیما
سامان گوران ۲۶ مرداد ۱۴۰۴ در صداوسیما: نتانیاهو از موتوری جنس میگیره که میگه برنده جنگ شده. نمیزاریم آب خوش از گلوی اسرائیلیا پایین بره.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71417" target="_blank">📅 15:01 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhPilUqIVvg37JNoH-3XpeCu46FeGMhV6U4P6aaVTve1LPpAgacvzYTq3PmWfTQQ4BWsxFnJcnpxIXxS-qeJpG55AVBG-CGDTSxBtmGDtvhyC7j-fnJpR9DzGu87TeFISZHmNKFLV18yn_pU3XzMlYWBQ7nYRZn_zeqQQQh41WmlCoDbB9-NgNgXI34lgoFnds3pBxrtlZ01t2EaSrczA6VVa-_8vnQQ2Cd3DanLRQqT7aBR76_tOyzv0jfuw_OW1_Yo-QAY18Mks24X27AZi8WwvcPxcBixfLjgnwHUwnP052XIzdlXxgB37wn1KQt7Q-hn1xLRvSy62_BePzGf4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LuzJkkj9mUNB5gc-w1eV-P90nOZlJDfjWBPo_IIiTK4A9YdgP84n_7_5WQw13MC3qY5gsu6evcU3dBwoiXqIfPBTyVU7-ckR4XZYFUNgQUe-W_lutvKM069uncCgTv5tBi-DfnJ5QBgiTxT82u9bKWUkBJTkvFehROMGy7OmX5La15AHg0SN3OELnVgidN8oKvAzZ_MK5AcTtLLgaJZ-ytxNkTEiGU6TLtb6YGkIz8Cme8awHuW4IWPPVsK5oNw0fAw8POi-h2j32_-0zuE_gtu_BE7eI-TYheHv1-mq2_mo48oWvXtqx7qNF-WRhZGBWEyw1LVZWYUT7iyai7mG5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/epzgdmZ6PtY4i7UwsIPmmwFRFQYNEqFVlEOzcsOdtm9cekZkKy13-SeDHd0PvEgqj8UcSCLtXeqJaR-vPnLf3Mz5v8W1gBoCb71yZOGo971f5K8PTkuX16qr8BR2GKW1WOmCf4XoNpe6CST8eCjRdbeIL6DPbqS7j2SF6o_gmHMe1CFqAMETB9OSwaRdws2eQUouIWToDMytYaorodXKlP-m_tsBVeisK1mOsmUjEwGSTxh1_mFuBvQUP2Iql_Szi5g-dKWE33QroeTSuqL87LAPee1KFWwE5vy_SEUvXpYHhunLrQn6IJk2iIWgxrb72-n1WiwWcw8DXK3lP2GCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OwUrq9uwaR6_iXmpfBxuUzG0OYzSs-82rDnRA1EKuYRgtdO86qs53cfhGxB8a53aJCcb_-g2F0pN8RomkWJJD1rbI_8NfSN5EqklM4onuVDx_f4rt9Q5qAtm--wvIfsLa1GujWSa76R_sY7sVVOkWAvqdXAbd8UmHkUQtq2fMiCqn-SZyvv16YyLjoFylUvhRKKtT6wvcQn3z5CBxN0zHlmIkleLYPYCHZvRGEZ7c_zFfHEukQxzbVAb3AVo6e6Sm66piZMaEsNXyA5FMXCEgBs7veMDdElX9vQnEKOyELbYj8ysdoNDa2fda6-ITFMT_aUSibAleueoDS90IN8ggQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇯🇵
👀
شب‌های ژاپن هم قشنگه
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/71413" target="_blank">📅 14:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=TdvkmWSq2fYhRgkgASLPGszETpfrW49p1u49tIH0jQOwgyDuB3GKfO3DsKn0beYtn3lahBu7nmsyZWQ6OXpzf6nCeD8O42HiqYaq99ajg17RpwvmMcQQGsvuLtYdcDqtiuoVGT0Bi102kBGjLnJOqxq2O_KS36StUxpFkqGu_pWb9UTLALsO0AMfvbtKjO5oXqer454QE5M39ACQS89dFh2HJiFlXqQMHNEbNYpSi9b-BInKH92FTbPukmGIjH2VsfaAxqR7K2WnmFNB0GB_uiPxsCO33HtH6-73JShU0LawD7esTG4RdDdTcy0cqyXFe4-yeGVXeg5SKnjSqotppg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63d4414bb2.mp4?token=TdvkmWSq2fYhRgkgASLPGszETpfrW49p1u49tIH0jQOwgyDuB3GKfO3DsKn0beYtn3lahBu7nmsyZWQ6OXpzf6nCeD8O42HiqYaq99ajg17RpwvmMcQQGsvuLtYdcDqtiuoVGT0Bi102kBGjLnJOqxq2O_KS36StUxpFkqGu_pWb9UTLALsO0AMfvbtKjO5oXqer454QE5M39ACQS89dFh2HJiFlXqQMHNEbNYpSi9b-BInKH92FTbPukmGIjH2VsfaAxqR7K2WnmFNB0GB_uiPxsCO33HtH6-73JShU0LawD7esTG4RdDdTcy0cqyXFe4-yeGVXeg5SKnjSqotppg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇮🇱
یسرائیل کاتز وزیر دفاع اسرائیل:
به مناسبت سال نو یهودی، می‌خواهم برای جامعه یهودیان ایران سالی نیکو را آرزو کنم و برای آنها سالی خوب و امن آرزو دارم. شما بخشی از تاریخ پرافتخار یهودیان هستید و همیشه در قلب ما خواهید بود.
و برای مردم ایران آرزو می‌کنم که در سال آینده، ایرانِ آزادشده از سرکوب و استبداد را به خانه خود تبدیل کنند.
با توجه به این احتمال که به دلیل خفگی اقتصادی و فشار سنگینی که ایران تحت آن قرار دارد، تصمیم بگیرند علیه اسرائیل اقدام کنند، به رهبری ایران هشدار می‌دهم: هر حمله‌ای به اسرائیل، به هر دلیل و در هر مکانی، با پاسخی قدرتمند مواجه خواهد شد که ایران را با ضرباتی سخت‌تر از هر آنچه تاکنون متحمل شده است، هدف قرار خواهد داد؛ از جمله تأسیسات انرژی اصلی آن که منابع و توانمندی‌های لازم برای ماشین جنگی و تروریستی ایران و آسیب‌رساندن به شهروندان اسرائیل را تأمین می‌کنند.
به دستور نخست‌وزیر و با دستور من، ارتش اسرائیل آماده و در حالت آماده‌باش برای اجرای این مأموریت است.
چنین ضربه‌ای ایران را ده‌ها سال به عقب بازخواهد گرداند و رژیم آخوندها را بیش از پیش متزلزل خواهد کرد؛ رژیمی که مردم ایران تا این اندازه آرزوی سقوط آن را دارند و مشتاقانه در انتظار فروپاشی آن هستند
.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71412" target="_blank">📅 13:47 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHacPgBHrzPoUIUEkgSgk9k2WHSFeGuwxmSnM5VwIXLPWsJ_0JDAZpgLriVv8sXwtnYqGRX7eV85bMI6tG_6PLjC7Nj215xmcuJxSHGc2d29qTGC_tOxQrZ7cWlG-8YiWpc-Wm99QuAoQmXAp059R87IjIzMbjZU3tA-NSium6TB628jSj8B-USFWYAWun8u_Sfa1nke8zKMtcrm4LnCtbkUE0aiN6NC-hlPyne4gkEZaCRjVIJhhF2jG6x3oYkulNy6J8WlYIKYuuZNjAlwOo5lHPO4FKJ1tiFeX3PSw0BwctBrvPric7tssBTBe23mDp7HFnKaoUwAACIqgtpTmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
توییت سفارت جمهوری اسلامی:
سرآشپز رضایی در حال آشپزی‌ست..
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/71411" target="_blank">📅 13:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=nj2GfqOTnoGwAgnetJi_7MbD5AFrERpt36hg4KZlEnIulFY-IYletqSg-VRlt5npPFE9h_Ch6eqc62UtYBdm54cooWhAxIe4gr8qWLMIirkLlDTCmATdxjxshPF7foqB6wohSwgf7u1L69pxh7B-WSgkolWTkEnOul61eQqUpJL0M8xYPAoSj5Y8GkOnbsLzwulNm2kO2Hs28SBcED1EMzM6hcSdn0SBgAJRFb7xn6z3uId9Bbc2pXdDX2MNjS46zWWeqPh70_VW1r3yDbBiYsB-OuYqwMqghrKreCoXPcm7Ly2u2qCWyLO9E-onNgSbUeSvQTOX_MVRDrTtAO1iCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb607ca379.mp4?token=nj2GfqOTnoGwAgnetJi_7MbD5AFrERpt36hg4KZlEnIulFY-IYletqSg-VRlt5npPFE9h_Ch6eqc62UtYBdm54cooWhAxIe4gr8qWLMIirkLlDTCmATdxjxshPF7foqB6wohSwgf7u1L69pxh7B-WSgkolWTkEnOul61eQqUpJL0M8xYPAoSj5Y8GkOnbsLzwulNm2kO2Hs28SBcED1EMzM6hcSdn0SBgAJRFb7xn6z3uId9Bbc2pXdDX2MNjS46zWWeqPh70_VW1r3yDbBiYsB-OuYqwMqghrKreCoXPcm7Ly2u2qCWyLO9E-onNgSbUeSvQTOX_MVRDrTtAO1iCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇦
❌
🇷🇺
انهدام پهپاد شاهد روسی به وسیله‌ موشک اوکراینی
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/71410" target="_blank">📅 12:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
ترامپ درباره ایران:
باید بگویم که این به لطف «نیروی فضایی» (Space Force) است؛ پروژه‌ای که فرزند معنوی خودم محسوب می‌شود.
از همان لحظه اول، ما می‌توانیم همه چیز را ببینیم.
حتی می‌توانیم برچسب روی کت آن‌ها را هم بخوانیم؛ «محمد الفاید»... «میامید» (Miamid)... البته هیچ‌وقت «میامید» نیست؛ هیچ‌وقت «محمد جونز» هم نیست.
«محمد»... «محمد العزوری». و این نام دقیقاً روی همان برچسب نوشته شده است. ما می‌توانیم آن را از فضا بخوانیم. باور می‌کنید؟ از فاصله هزاران مایلی، داریم نوشته‌های روی لباس یک نفر را می‌خوانیم.
ما دقیقاً از اوضاع خبر داریم، اما متوجه تحرکات مختصری در منطقه «پیک‌اکس» (Pickax) شدیم.
به ایران توصیه می‌کنم که دست از شیطنت و کارهای زیرکانه بردارد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/71409" target="_blank">📅 11:55 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTRuUjGFHqdfDstsNNJin-sKWFoV4b9DNxcMbrgXx68Y_J6aRnJofeR5z1v2hlR4-iCp723y5xzfEpHNuVEN6BJy50FO9TuFfd0yuC1OlgeVkuYnF9FqRQkRiKeKdmDCWDNqouU9N_7oHDRVHRuRmSmYZlaHUpH7xLn19tPlyL4RryywA7VPfbdztL9MUI7lZ7Bav6HtZs93zMRtQZHMnSpDBFEsR1kyDNhb3T6dreD8jd0i19sb_RbqmE7qEugF5Ps9TrfPgmL2nBWMFMhLBzwWK1bN6Eh1VQ-6HZcXQNXXCbAQkbSjacFo0TK_KFNNZhzjue8YcQtl71GmDD8hXyBA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f498f58530.mp4?token=nldc6oqBcwWuJEM8g6z1-hkzGSWD9IgyievpZ_iGmknmbItl1zo7BKbyTQVH_ojG1AVgXCsUEua8GTcjvwJtqpFHgwMVgZguYOYp6EshO_wNFdWGpAYIRT6N3yGCu76MU8c9oS7KZ13Ya-tMVG3g2bdFiqZ6FQkaNTjBuifTq6ebbRfl-PFkyENqduvGpcdOTg5b3Bsh5FUevhuZE6VVVGmNRKAXNxUT_24Ir0tJ4fG-8WgjHSrcKzY2jEmLwXQv7OhBrghvYE-_a2pSmsxe6gxEWRTEEbLwbMC-c969aDXAhe1zk9fiEUXGiTXuODncS5sZLu9d4PU5pSQXjLrMTRuUjGFHqdfDstsNNJin-sKWFoV4b9DNxcMbrgXx68Y_J6aRnJofeR5z1v2hlR4-iCp723y5xzfEpHNuVEN6BJy50FO9TuFfd0yuC1OlgeVkuYnF9FqRQkRiKeKdmDCWDNqouU9N_7oHDRVHRuRmSmYZlaHUpH7xLn19tPlyL4RryywA7VPfbdztL9MUI7lZ7Bav6HtZs93zMRtQZHMnSpDBFEsR1kyDNhb3T6dreD8jd0i19sb_RbqmE7qEugF5Ps9TrfPgmL2nBWMFMhLBzwWK1bN6Eh1VQ-6HZcXQNXXCbAQkbSjacFo0TK_KFNNZhzjue8YcQtl71GmDD8hXyBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامپ:
دو نکته وجود دارد. اگر من برجام را لغو نکرده بودم و اگر آن‌ها را با آن بمب‌افکن‌های فوق‌العاده‌مان — آن بمب‌افکن‌های بی‌نظیر B-2 — هدف قرار نداده بودیم، الان آن‌ها سلاح هسته‌ای داشتند. و من مجبور بودم با عنوان «رهبر عالی» خطابشان کنم؛
مثلاً: «جناب رهبر عالی، حال شما چطور است؟»
اما حالا دیگر نیازی به این کار نیست. اگر آن‌ها سلاح هسته‌ای داشتند، من به رهبر عالی زنگ می‌زدم و می‌گفتم: «جناب رهبر عالی، حالتان چطور است؟ آیا کاری هست که بتوانیم برایتان انجام دهیم — البته به جای اینکه حسابی بمبارانشان کنیم؟»⁩
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71408" target="_blank">📅 11:42 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=CMnhe_fri_n5Y_GPThNC28aAeEJLku29rn-wUVlHx-0fkex7KDMUUo32_M2epKNM6JN9759x5X63PyBNwacXJzk8S2U_GPA3gUrBU2-c4Rs217Y9hSsI0z8nKCuqjVu-qbOLK2NkmWIQ5VaZuotd8E_xKH3z4ky82BjKfIekTmyk1N0nmgPMbFuhgJwP0pXV86hhTivkjA_-KLJtjGalLRqKghou01Wr8D9_92VWMQwWZRPnoPB3LkXosdjGiVbQojMO4G6Uv7H_bHcEEkUXOzQxXIoopiT4wLxZ6bQBtuxWNVJsLwcl16fpJjMphFN-53CfEA2tSlsZtYUWoVhO9U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1bfc54b65c.mp4?token=CMnhe_fri_n5Y_GPThNC28aAeEJLku29rn-wUVlHx-0fkex7KDMUUo32_M2epKNM6JN9759x5X63PyBNwacXJzk8S2U_GPA3gUrBU2-c4Rs217Y9hSsI0z8nKCuqjVu-qbOLK2NkmWIQ5VaZuotd8E_xKH3z4ky82BjKfIekTmyk1N0nmgPMbFuhgJwP0pXV86hhTivkjA_-KLJtjGalLRqKghou01Wr8D9_92VWMQwWZRPnoPB3LkXosdjGiVbQojMO4G6Uv7H_bHcEEkUXOzQxXIoopiT4wLxZ6bQBtuxWNVJsLwcl16fpJjMphFN-53CfEA2tSlsZtYUWoVhO9U0V7s1jEEZWV7ttrF7dOmhELOjYem9X5xAyh4KuiDj4e68oWts4a_uStY7eVevpNj54Y8AVSej7g9rBBHk4PfayC5u7SLDoe1r-NbnvchNrknSbMPaoEFcMzeQEZXpcoXMo4641YuFn36ZGbs6qowSO2iyl-sx65TUODBLwoBs_MKSD7X89ipvT2LB7GV-8eKVioFCu955WNjCZSgTK6z2hoD1mdbzvEILxtTiyLkNkyNr_XDaN5uYVScO7yeI3tjUKbd4nyqsCq6W3aHiPNJE1iUTxdLp8aHBSUxWPREDR8dJj5wf6iSGP8GgdwdKtt4plJFafXXxMvyKvsKIODno" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
املاکی:
به نظرم باید اسم آن تنگه را عوض کنیم. باید آن را «تنگه ترامپ» بنامیم.
بالاخره باید سودی هم برای من داشته باشد. قرار است نامش «تنگه ترامپ» باشد.
خانم‌ها و آقایان، می‌خواهم خبری را اعلام کنم: ما آن را «تنگه ترامپ» خواهیم نامید و مطمئنم که رهبران ایران از این بابت بسیار خرسند خواهند شد.⁩
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71407" target="_blank">📅 11:34 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2660237e39.mp4?token=SAl023RPOkzgvpZEHbilJ2Zm23FE0ZBLgVnthOb7ZVBcDBT31mF_4lbQZtjBrNIim68tPUtSGXaagd6Z1hnvDJzuXRwVyAyoe-x7pHlYB-d_eJHZkGkNEW5mgAVqrMHoZQ_De__T1wAa7vGdUnljAFNNFoF5anQOsmGwI5_0BSNXibyjE7ikgEFL_tRsBtmFaGrkO-6Drn7ZIgAF2yVuCXbAKjXuQhfoipFq6g5cHumiWvsQLTohiQP25OObvS5oR6IREEt0kCgMnHIjlA9_s9uA4HpQsq2sIG7kDQ9Tx8-aRGFDaOIIFfBGIPnD_E9bhMuc6-yr8KTb_W_edVRStg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2660237e39.mp4?token=SAl023RPOkzgvpZEHbilJ2Zm23FE0ZBLgVnthOb7ZVBcDBT31mF_4lbQZtjBrNIim68tPUtSGXaagd6Z1hnvDJzuXRwVyAyoe-x7pHlYB-d_eJHZkGkNEW5mgAVqrMHoZQ_De__T1wAa7vGdUnljAFNNFoF5anQOsmGwI5_0BSNXibyjE7ikgEFL_tRsBtmFaGrkO-6Drn7ZIgAF2yVuCXbAKjXuQhfoipFq6g5cHumiWvsQLTohiQP25OObvS5oR6IREEt0kCgMnHIjlA9_s9uA4HpQsq2sIG7kDQ9Tx8-aRGFDaOIIFfBGIPnD_E9bhMuc6-yr8KTb_W_edVRStg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
اپل از AirPods 5 هم رونمایی کرد؛
▫️
ترجمه همزمان و زنده
▫️
نویز کنسلینگ فعال قوی‌تر
▫️
صدای فضایی شخصی‌سازی‌شده
صدا رو جوری تنظیم میکنه که حس کنی از اطراف و جهت های مختلف مياد؛ مثلاً تو فیلم انگار وسط صحنه ای تنظیمش هم متناسب با گوش و سر خودت انجام میشه.
اکولایزر تطبیقی نسل جدید
ایریاد خودش لحظه‌ای صدا رو بررسی
میکنه و بیس، زیر و بم و جزئیات صدا رو خودکار تنظیم میکنه تا بهتر به گوشت برسه.
تا 5 ساعت شارژدهی با نویز کنسلینگ روشن
💸
قیمتش تو آمریکا 149 دلار اعلام شده.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/71406" target="_blank">📅 11:30 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/71405" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/71405" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYjXdO0AAfxzxpUktrUjYe6fpwU5hDfiLfayvsJ6zz-C4exfPV2XUUpCaWfwzf5raDQ_JU_V-CGVn0ndiwOul4gREiVK1EZXDhkGcm4wRxyEByHtsCAadt3LUtz-cu2jlZd3q33lY8_d6pY_lVql8AT604FgiBCIV-FvM3GmDHi79gh7su6AusuScI5WrTdHFR7X1dpWuj9lN5W_uEN3PzBiurKn48FWsJeXFF0dfgak40t48mQ4nXBLB5PzIGLZb356XY0_c3JofFstcj4DpK8132EkPwM6eVfj5VbBPMeHLdIWpee6GJtPN5WbQb2OFSmIFZLsCsfL4kcDK7_G7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پیکان
🆚
استقلال
⚽️
رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم
در ۵ بازی اخیر :
⚽️
پیکان : ۲ برد، ۲ تساوی، ۱ شکست
⚽️
استقلال : ۲ برد، ۳ تساوی
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/71404" target="_blank">📅 11:29 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71403">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/86c3602295.mp4?token=krYSoaZH3jfaVHfBDUGCFw6mAl0vP1x_heHJ1-TwxalfHstUIp3lfwhFUA27GdMV8JtjN8gDIOLsl1dsEJ8OuoqOoGDdnZvhk5gstQ-rPY-75W2IpEZ7feaOmr-9SDdrzAlcRyNP0kuGzunr6fYdXIOJWo1OyxfKCraKCaQOfOE9anb97-JKmQuqkOiJYnFVkogv8iozd71oVccaxQVZQbGGNGW91qngD8pp7vxTOcBFQTs-ZTjKJdza8W1LmLR184VRrKCbWSCHcmuq_zVjEtgEiegTJuK7f7l7aah51AxXvtD54wOa2gt-LU-ncSH6gDsWwi5T1d2anTG6BxWd_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/86c3602295.mp4?token=krYSoaZH3jfaVHfBDUGCFw6mAl0vP1x_heHJ1-TwxalfHstUIp3lfwhFUA27GdMV8JtjN8gDIOLsl1dsEJ8OuoqOoGDdnZvhk5gstQ-rPY-75W2IpEZ7feaOmr-9SDdrzAlcRyNP0kuGzunr6fYdXIOJWo1OyxfKCraKCaQOfOE9anb97-JKmQuqkOiJYnFVkogv8iozd71oVccaxQVZQbGGNGW91qngD8pp7vxTOcBFQTs-ZTjKJdza8W1LmLR184VRrKCbWSCHcmuq_zVjEtgEiegTJuK7f7l7aah51AxXvtD54wOa2gt-LU-ncSH6gDsWwi5T1d2anTG6BxWd_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
رئیس بی غیرت دانشگاه سمنان: از همه دانشجوهای عراقی معذرت میخوام، قول میدیم براشون جبران کنیم!
دانشجوهای عراقی فرزندان ما هستن و نمیذاریم کوچیک‌ترین آسیبی بهشون برسه.
اگه خدایی نکرده یوقت اذیت شدن معذرت میخوایم و بهترشو براشون جبران میکنم.
تمام افرادیم که برای دانشجوهای عراقی مزاحمت ایجاد کردن، بازداشت شدن و انداختیم‌شون زندان.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/71403" target="_blank">📅 11:00 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71402">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=eW9_nbCzw2dBVWQJPRVtQsC-siVhLsxD2O3242QOUb1bgPV0-TV_MytahIAi0Ha-HjWSTvIGSYkkjACRr7-VtWqPTfC7O1VTo7V4dMwOL6mHYdu-urpVZovQdjzAZk3HbDXeNgPFOGB0zy1QW8d1KaYpdRnFZWzLRSvB0CYFluV0bdULkScCXRgTT_PYdjVG97Vfgj-U36Sat-DU9HLHbOa4OQT7MDjs6u4m9GZCGAHABrWFT273VXZ-TeVcrHriCAXC8MO90s6i0Kb5LQ68a4FsIb5psU9vQt8R1fSDKbfRK8_77uZpaC5tzBm92jmpVzxYZ2tA6Ai9dpe9_TLb-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1423e28a88.mp4?token=eW9_nbCzw2dBVWQJPRVtQsC-siVhLsxD2O3242QOUb1bgPV0-TV_MytahIAi0Ha-HjWSTvIGSYkkjACRr7-VtWqPTfC7O1VTo7V4dMwOL6mHYdu-urpVZovQdjzAZk3HbDXeNgPFOGB0zy1QW8d1KaYpdRnFZWzLRSvB0CYFluV0bdULkScCXRgTT_PYdjVG97Vfgj-U36Sat-DU9HLHbOa4OQT7MDjs6u4m9GZCGAHABrWFT273VXZ-TeVcrHriCAXC8MO90s6i0Kb5LQ68a4FsIb5psU9vQt8R1fSDKbfRK8_77uZpaC5tzBm92jmpVzxYZ2tA6Ai9dpe9_TLb-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن‌
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/71402" target="_blank">📅 10:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=AQ6DNo4rDUSUJvnm40KOK74xgg4t-jOwVNzyc24yx9YwzsvRwkY3gnQISH2klX0LehP_wfOJ1l64QLicXfPg3gXvJQPJRTMd64T3gOk3Ky0y9Hxu-0DnLbhcgTeGnc0bezKYcii4FPwI7P20pJyLjrAY8uI7LCf0XyqfhCF4wzzbDvO3Rr8XGgH1lTQGSyE2Cpwn1uatIJbP64SnzfYYf8KjNHzeaOybbNCqq-mtCrreOANUsK6itMFWJZ5hpotftXhK9AfPM9NXf0h07w1BWGtDGHm8zvx21GXHYHXXkJCi78JgQPVvkKP4K9ijlQNfErH5NerXcTMTVnuoMR4ouw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13a43f0b92.mp4?token=AQ6DNo4rDUSUJvnm40KOK74xgg4t-jOwVNzyc24yx9YwzsvRwkY3gnQISH2klX0LehP_wfOJ1l64QLicXfPg3gXvJQPJRTMd64T3gOk3Ky0y9Hxu-0DnLbhcgTeGnc0bezKYcii4FPwI7P20pJyLjrAY8uI7LCf0XyqfhCF4wzzbDvO3Rr8XGgH1lTQGSyE2Cpwn1uatIJbP64SnzfYYf8KjNHzeaOybbNCqq-mtCrreOANUsK6itMFWJZ5hpotftXhK9AfPM9NXf0h07w1BWGtDGHm8zvx21GXHYHXXkJCi78JgQPVvkKP4K9ijlQNfErH5NerXcTMTVnuoMR4ouw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇮🇷
«موسی غضنفری آبادی» نماینده مجلس؛
فقط به خاطر این کلیپ کوتاه ۱ دقیقه‌ای از «شاکر بوری» بلاگر اینستاگرام شکایت کرد و به ۱۳ ماه زندان محکومش کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/71399" target="_blank">📅 10:03 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EoOQRqto5WlfqTJJU4Q87XV--zNi2WNhaUHFMAfmAa1qORNhpaZp25TiJRLeNqmFbw54c-S5HIytdpMtsydPEUZ4zxYz8goEyGd1LJw9Cy59TBBQ2QSew0J4osMQanEQpebBaDnRSJcm7Yq6GS5Peig63iLxriq-wYIZdvX4hZjsgn0SCG8Kam6-aE-ZUMyQ54R6qFbq8UtkHavoESNPUM4YE8-rUyc09UfQ7Q5XBgSQOp_5IsBi9wQzoC8RU12Jz50d_V3b3m85fHpaMvaz1GTiisD6MC_TocHosu55lY-KX6aCIf80ceykzVvKpx4DylPMXq-vldd0SQ5AzaAnKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇵🇰
🇸🇦
رویترز:پاکستان در پی حملات گسترده گروه حوثی‌های یمن به عربستان سعودی، پیام هشدارآمیز ریاض را به ایران منتقل و از این کشور خواست تا حملات حوثی‌ها علیه عربستان را مهار کند.
اسلام‌آباد پیامی به تهران ارسال کرد و از آن خواست تا با استفاده از نفوذ خود بر حوثی‌ها، از بروز یک بحران منطقه‌ای گسترده‌تر جلوگیری کند.
به گفته یک مقام ایرانی، ایران در پاسخ اعلام کرد که «کنترلی بر حوثی‌ها ندارد.»
با این حال، دو منبع ایرانی به خبرگزاری رویترز گفتند که تهران حوثی‌ها را به تشدید حملات تشویق کرده و وعده تأمین بودجه و تسلیحات بیشتر را به آن‌ها داده است.
پاکستان اعلام کرد که هرگونه نقش نظامی این کشور ماهیت تدافعی خواهد داشت و بر حفاظت از خاک عربستان متمرکز خواهد بود، نه انجام عملیات در یمن.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/71398" target="_blank">📅 09:32 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71393">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/D4eB047gZtpzvG_2ekNh_eeRt30hlXNvQ8CObait5KVyoQAwOfNK0RbOYJGcECT1Qm97knTt1P5afBTUOWVNtLdWZPIIvwJTsa2-21rHz8hVdWCxKYKrShLRF-V7uco3YaklrF32_NJVGj15EWHPhuej7DIzt_KD9Bwg4MYWD4TISLe72gqGjRIEn4JH_ATNm4HXRC4Wk6aItL4_I17ybzbQjQ-bo1XA5M2krhgUuFZyjaP6exT7HTe47ebRKIx1m-_THRK_1yoTB0Cb8tM453iVs_lRxpK5XM_f7akrehXPjt_lmt_KwhDBckLAAVu1VkARlM5FUs1-_X9q7hGGdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AguXttLO6qv6c5ZjrW0nSdHx1B6Y7WAesCan5TqgzECTwoFUB_5nLoD3ZCrm2JUyBBHmEgfldXaAe0YWUF7u9y9DSwkDtC88_4KWiGRvHawgN4o5Yq8tFf5XqZ9pVlmJrcAX1qrKb3gf8u7oI96sVqDNnX67MRg5tzZMyTzeagYjTdJLZPy0s4a3i-dqvVlSJ_ZTZEH_7XZtipXxQu2MHKxcw5BE3QiNwYlVdS_AhSiv1JcQhxr5rwGFyLcgn64AnmAI9s9KfKdqS8yAorEjO8DefmOkBxOv6lait5jry6CGFMgPFOQVSPpcLwCqdv56qyn9YxZED-kgYxPL0qVJPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hH07oPwadfXiZD7PskXnJBIu9RcdTqDyGfIusJstOSnImplpVceLoMIfPrE6tyZU6c5bAj-4R_orECgQquCVLLKRt7mP59DY_HZEboYvt9Pc5eRvabial-sefczzcypFCRHMpnBayoQVPLNQHZVLoLsEHA-ccNUEsDJv62Lt7A0BLHqM7GeH7TTBLH7yazFBytApyGJxr9ZJdDfOP5OGjFf_kEQNVxb0J77wuLVBEu-LunfTOssYC7yFDq_LRr3cxn-UGX-tzBkXuEZQGmeiZFkcMVIANw6kGVqlB1P-pJ8ljOlvljKnhMz9W7lQ0K7CRfT3mz-9-yhZCPyjh9oEsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UmYzy2ZwvYPbJue2rf2QjTR3DjwKxg4Ltncz1iTOOBeVyTEfL-DDmQ-YO-eTD28-YhpT1yw8KrScn87u7oMA7ZQRia8um401BCapPNL8ypoMBozaALi1xv6i-zgyzXJ2-YvIjJvsRFu_m7Q7xe6UlOf_ek55e6mTo3niBzrGVlQs6GB4A2SXyO4tGU1PMkhNVXGohyc1ooEMHY8DoXdo6iQTwz7DnzhMDH-KZl_NcY0t1HYxlmMEi9eWFurrRM3z3yDgZVWHOC-P-y5RgCOZ8hPscgQ2GRE2p1ughi4WJ5fRhcAxgc9sXQ_D5WcqCwdARGYO_kq7QL9_J4fjr1JKFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=e6NoUXiAbjUG-F5dFt-IDJ0XLLOZkJfFkA6SJruFPXHvSCVJ4mxw15VLPzbU4safGsmLGVHaPWTKyI8VyQ1mFOOoyh9rtkuwfNz3wR709n6qCpWJSXdz9d-t9l-CgGwimh2Yxv--bMR0ZCkFlXjplvGcElcx0tvMXXiEQZPsQVHCdI15ZCFsZqfYtiSZ_0LQfbGI5BmiJhGQD-WPgRQb7h4EJoh6CcmnnSow51YE9iTGamw95DRVd8228JXj-JU_s8SCkYvI8NnjbfpXbqsaGJrlAjAh8cKEfNugMAKfDyR2E_k1CWBiXovtPvpRnGPMuZgeDG_jGq_sKRWQJMHdSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7c5fed9d1b.mp4?token=e6NoUXiAbjUG-F5dFt-IDJ0XLLOZkJfFkA6SJruFPXHvSCVJ4mxw15VLPzbU4safGsmLGVHaPWTKyI8VyQ1mFOOoyh9rtkuwfNz3wR709n6qCpWJSXdz9d-t9l-CgGwimh2Yxv--bMR0ZCkFlXjplvGcElcx0tvMXXiEQZPsQVHCdI15ZCFsZqfYtiSZ_0LQfbGI5BmiJhGQD-WPgRQb7h4EJoh6CcmnnSow51YE9iTGamw95DRVd8228JXj-JU_s8SCkYvI8NnjbfpXbqsaGJrlAjAh8cKEfNugMAKfDyR2E_k1CWBiXovtPvpRnGPMuZgeDG_jGq_sKRWQJMHdSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🍏
شرکت اپل با انتشار این ویدئو، رسما و شرعا از آیفون 18پرو رونمایی کرد؛
🎨
این گوشی تو چهار رنگ عرضه می‌شه:
• زرشکی / شرابی (Burgundy)
• مشکی تیره (Deep Black)
• آبی یخی (Glacier Blue)
• نقره‌ای (Silver)
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/71393" target="_blank">📅 09:04 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71392">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/71392" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71391">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/a_Zk9cZhMJuaBSbdHprMpdAMa7PSlgO33hmQT8i2-O1Wlhs9HBsOSjxwz-JKkM6DXlgxKNkGdvgWntC3QkjGv-l5l0XHKcJKMcV3v5U7ChUdOkMl0UJcNTW9ae1uZyxw-3f8pWwO_TSH-ccPaxk6k5-qynxBzFYhkrgt7ghuEOe3YrnT6s9lLmVTG9fv9iP8vDYl14-uA_ECMkVIl4j9WojXj8NvmiNgaAAv7OxUm2a1pcqAWXRoPAVutiHOibNlm30ZfK_ZJfjhj9r_Zj47VVWDNACo4gQy4maT3UwVXX8chE4LZECYP6G_TWWEG9W9UoHO9Pd1eXxQus7k_t3yuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😶
🚨
🚨
این کانال باعث ورشکستگی خیلی از سایتای بت شده و پلیس FBI برای دستگیری ادمینای این چنل جایزه تعیین کرده
🔥
https://t.me/+bDapVmvigDhmYzZk
https://t.me/+bDapVmvigDhmYzZk</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71391" target="_blank">📅 01:37 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71389">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xj5_tBJm-Tx2cWjfj-uu7PVzHqAsVXh7QWGXuKf6zzjSEoZfGNUHpFrJtC8AN-JpzjE7oVqYXHPy3PnbI5n6x9tVGJdgPSvi8eCF3QNQMnJjVmDCK2qJ73yOMAdr7esjpVYPKh4D6oebOm5zzJalMTkSzvQgbO_qUltxiZhy5gjC-Xnr1UBa4hkSvTVB8G8DUNFtpn46U_7NRDcxsWXCx8ROwe0cX9eyZmJGDbdg692HBj6ws5DQjBWlET38j4G_2iPxsEvKPwL5Pyln-iZTy0PbVP0pAaUF927koY9D7RuH0iA1JOexLKQqpHewp0sz_jwLVrf-kzXXa5waYTHfOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PTSCqi1a7Zg-tNJO29h8q06Bd5exOhHU9oarNDfuXYMA9faW1qIwsxuVQ-vngUSjjnuMqpzfjKtxSYv918BLzNt35lq6za4S96iDEX1WQQRt3bb8rtdlHgPYq8YHZapwbOIjYqyihIdb4AQ9WaYtbcrTRhHUwvszf0p0qPgDyXfMnWYE8QnSR8gais4NdNsNCiGOE3zkOkwSSEsMqiWRhxgqhRdAbY-W2DqUhCvEJbU_X1lbVIsHTVwb0RO9qDDOTWDjBOKzRoTlL_lSgAFqVNaPfx_TpQbxr1LKbKZCURnQxnWKbGd4V4-iMaHtZlrCLWJvkVeYVntruj3RuqM6UQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⏺
به گفته منابع عربی حوثی ها وارد منطقه حیس شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.5K · <a href="https://t.me/news_hut/71389" target="_blank">📅 01:26 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71388">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🚨
فارس:دقایقی پیش صدای چند انفجار در مناطق ساحلی سیریک و قشم و مناطق ساحلی شهرستان میناب گزارش شده است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/71388" target="_blank">📅 00:51 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71387">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
گزارش ارسالی از قشم:
قشم هم در خونه ما لرزید
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71387" target="_blank">📅 00:33 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71386">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
دقایقی قبل صدای یک انفجار مهیب همراه با لرزش زمین در کوهستک (هرمزگان) شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/news_hut/71386" target="_blank">📅 00:31 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71385">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=Icb4Xe5lFDaO-wuxyG9qCF8w1feb-0iTF4GDF2VDVRZIveN2jr3HMvIkfHB7idVcXpDdQwCAYXJ8ZA3Yx3p9YDdKFl8wUHrVAqgttFQTqPw1r29lECaHJIKXC6UTvIUDosL2fh584fwWMESCbY_0KQeVauaxAbrGbfH5777Q6zCa2A17dg4yasl5_SPK-L3GS8fjuBDm66PZuV0i9FL52KUZ2cxPm4bruVMfl_EvpEA8Ctr7EgfI-y-8_aJqQnXnkar4gFeKuCHNDE2I5XNHruPr-WKu939hCvq8UqaUEhPFWSGBsv-mW6WX58Mo1wvmaE6IDpb_w86wHJJ4uc43Cw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/240fbc3c81.mp4?token=Icb4Xe5lFDaO-wuxyG9qCF8w1feb-0iTF4GDF2VDVRZIveN2jr3HMvIkfHB7idVcXpDdQwCAYXJ8ZA3Yx3p9YDdKFl8wUHrVAqgttFQTqPw1r29lECaHJIKXC6UTvIUDosL2fh584fwWMESCbY_0KQeVauaxAbrGbfH5777Q6zCa2A17dg4yasl5_SPK-L3GS8fjuBDm66PZuV0i9FL52KUZ2cxPm4bruVMfl_EvpEA8Ctr7EgfI-y-8_aJqQnXnkar4gFeKuCHNDE2I5XNHruPr-WKu939hCvq8UqaUEhPFWSGBsv-mW6WX58Mo1wvmaE6IDpb_w86wHJJ4uc43Cw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🇺🇸
#فوری
؛پست جدید دونالد ترامپ در تروث سوشال:ترامپ ویدئویی منتشر کرده که در پایان اون بخشی از سخنرانیش در زمان آغاز حملات مشترک آمریکا و اسرائیل به جمهوری اسلامی آورده شده که میگه:
🇺🇸
ترامپ:
این رژیم به‌زودی درخواهد یافت که هیچ‌کس نباید قدرت و صلابت نیروهای مسلح ایالات متحده را به چالش بکشد.
🎙
سخنگو:
او به جهانیان یادآوری کرد — همان‌طور که بارها و بارها گفته است — که آمریکایی بودن، نمادی از چیزی شکست‌ناپذیر است.
اگر آمریکایی‌ها را بکشید، یا هر جای این کره خاکی آن‌ها را تهدید کنید، ما بی‌هیچ عذرخواهی و درنگی به سراغتان می‌آییم و شما را از بین می‌بریم.
ما آغازگر این جنگ نبودیم، اما در دوران ریاست‌جمهوری ترامپ، آن را به پایان می‌رسانیم
جنگ آن‌ها علیه آمریکایی‌ها، به انتقام ما از آیت‌الله‌شان بدل شده است
🔴
ترامپ:
خطاب به مردم بزرگ و سرافراز ایران:
لحظه آزادی شما فرا رسیده است.
وقتی کار ما تمام شد، کنترل حکومت را به دست بگیرید؛ این حکومت از آنِ شما خواهد بود.
@News_Hut</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/news_hut/71385" target="_blank">📅 00:21 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71384">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در سیریک
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/71384" target="_blank">📅 23:51 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71383">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=Wwf40oqTcCMOgl3v9nNF6iO4I9qlnaylVvffjgc-P25CKpXRJoAJZlmvSwfvuGEGZlFZhGsy_YNkjtkizFFkJbAvmIEbwnGcHhbnodCZNIO-X7HIirMHuUDZJvyW9-KO_UMLHM-A1IlsEteQ0Fhibmgo6Xf3bVWE0uLEDyUC_Wwmc1m3Ronr5OGL8bb-KrLN40YYKXmZ8N4GCeKzaaLOcFtYiYNux6rwThaTbtelvePn9vKsQ78DrUaR_UXWtEOQYE_07RGpBMCJeISVFruQ6DR0CgNC35NC9JZE6rxNsuiU1kLuZ-o5jwceAcU2xv3fztJ07fjSfoAaJLZ2XJtDizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/364cd7494f.mp4?token=Wwf40oqTcCMOgl3v9nNF6iO4I9qlnaylVvffjgc-P25CKpXRJoAJZlmvSwfvuGEGZlFZhGsy_YNkjtkizFFkJbAvmIEbwnGcHhbnodCZNIO-X7HIirMHuUDZJvyW9-KO_UMLHM-A1IlsEteQ0Fhibmgo6Xf3bVWE0uLEDyUC_Wwmc1m3Ronr5OGL8bb-KrLN40YYKXmZ8N4GCeKzaaLOcFtYiYNux6rwThaTbtelvePn9vKsQ78DrUaR_UXWtEOQYE_07RGpBMCJeISVFruQ6DR0CgNC35NC9JZE6rxNsuiU1kLuZ-o5jwceAcU2xv3fztJ07fjSfoAaJLZ2XJtDizzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
⭕️
پرزیدنت ترامپ:
انجام کاری بسیار فراتر از توافق هسته‌ای.
چیزهای بسیار بیشتری از هسته‌ای وجود دارد.
ما به توافق هسته‌ای خواهیم رسید، این ۹۹.۹ است، اما چیزهای بسیار دیگری روی میز خواهد بود که سه ماه پیش روی میز نبودند.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71383" target="_blank">📅 23:48 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71382">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo41abbwGei1KsHOqo4xujtqWMov13qdE5K7acdYeEJJcKeIIpB8TxW7d4k8UP8oBCop3wmmNOHKGbQvKhMFU055X9QDScIfUu3nSr-9YtyUpJ1COhZzmD5dNuvsmf2rrL4HwjaW_7ccOdTiD1LTMtEug4InnkuUpKlKna7IXhCuuFEBIVeWShapCzkRJkqm43wB5V4SC3wj-V1-6AiC5rFwMEDBO3GOPaP_DRdNZRFIG9bXbXf4qRchJwAhD_PQy3Tk__J25S6ZpBheQ3mbFdklBMCK6yMRqBZB0ms5FYfXuo7lE-wDe7xA01dzTP68c51RjSWk208Bq-Lyp_klX_PzE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b8c1afb2e.mp4?token=IkcD5r_tvmhvOuneo8f0_qYj-4PQpotPPcZLG6NXWICYDmD7-6zG6LMGKzcoch52d_soqxPWhmsFJ0LA1QSRyF9CPuKilLheV8OtOfR3TrUo8Bm98YfpUx87AOeRTdOxx0mgKCycI9HfP3NDngQ9eqToaZlfe2PBu4X9dvvFZ2ub1WoydSUQWNjeBef3XyCX2fgowbyKwJ1sNZ0N-Wdmzr-tAbxDS56M4IWuy_oJ63_gfaHjCWdCo7fCmI6TZUm5bWj5jsMLN-VEqLdGko3clZ-JQ138jGw_PPczmvLsswIWYkJNZ3czZQq6EfEMoZibtmfjvph9EmJ1bwyYKkDo41abbwGei1KsHOqo4xujtqWMov13qdE5K7acdYeEJJcKeIIpB8TxW7d4k8UP8oBCop3wmmNOHKGbQvKhMFU055X9QDScIfUu3nSr-9YtyUpJ1COhZzmD5dNuvsmf2rrL4HwjaW_7ccOdTiD1LTMtEug4InnkuUpKlKna7IXhCuuFEBIVeWShapCzkRJkqm43wB5V4SC3wj-V1-6AiC5rFwMEDBO3GOPaP_DRdNZRFIG9bXbXf4qRchJwAhD_PQy3Tk__J25S6ZpBheQ3mbFdklBMCK6yMRqBZB0ms5FYfXuo7lE-wDe7xA01dzTP68c51RjSWk208Bq-Lyp_klX_PzE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
در مورد ایران؛ آیا انتظار دارید که [چنین روندی/مذاکره] زمانی آغاز شود؟
🇺🇸
ترامپ:
راستش را بخواهید، جف، ما به دنبال چنین چیزی نیستیم.
در ابتدا می‌خواستم به توافقی برسم، اما اکنون کار از آن مرحله خیلی گذشته است.
در حال حاضر چیز زیادی از کشورشان باقی نمانده، بنابراین ما به دنبال آن نیستیم.
بله، شاید مذاکره‌ای صورت بگیرد، اما این چیزی نیست که ما در پی آن باشیم.
🔴
این جنگ بلافاصله پس از انتخابات ما پایان خواهد یافت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/71382" target="_blank">📅 23:45 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71381">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtlbdTjdFcps-U_HRc-HkoPMHbT0CCQEFoNKl38FLR5WhmrB_L7EqHjKyxbI5V2MduGQ8F2t2yDWQUjB8cj2AOTmrYuShJ7LL3Q-Z2aWZuc0RmIrxNyJUIuge6a6swKnNKBAyfuLnecacS4a8rTk-ziBMnT-F4LdeBqvwXpybDn_QFn4d1fqM_aD29LIHdh2hiGA3V3tgM_a_5qDhykz7TfFsa_fjS5dYA32SmdJQviC7ok_5JINaDM6Z5E272ocxxxvn4HZEp2pcMjaJeHAX_aAVmD2tCCdoGuX0K9UvSmT5w6mi9ZcLUR3IsKJTSNUUoEeBZM-EMy5bMjZz6a10pSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/088801b967.mp4?token=HnLbcj2nc3SAzfo0iwtlBncD62C9jXCMoQEvmyjRBBAHORuJwmLhl8_-6TdY9QiiWaEvm0ouJE8PRHUGpEoMTJA3ogX2el3tLXiT2iDOJSA365YOo2cMq-HutFRRptWrnjCZp955Vw4hve1FZWrHVOz-nI5iZFATWeVnr-spXNXaZ9QoKd5KXl_ukmnsA2jWkZ1aOuwvu_B6mZjns-wiQsz4CDgp3v2EQ4mx6lwrzLCfGEXYAgZVuOab0xDaOMVJpfwtBPekDo4ApuEnVhP9VgA-EiG9kDgWI9tdociMI9xQ8tKNuFtmcQ9Ixoc9GOJ7xbn_4Lz1rRm6eWYB-nnMtlbdTjdFcps-U_HRc-HkoPMHbT0CCQEFoNKl38FLR5WhmrB_L7EqHjKyxbI5V2MduGQ8F2t2yDWQUjB8cj2AOTmrYuShJ7LL3Q-Z2aWZuc0RmIrxNyJUIuge6a6swKnNKBAyfuLnecacS4a8rTk-ziBMnT-F4LdeBqvwXpybDn_QFn4d1fqM_aD29LIHdh2hiGA3V3tgM_a_5qDhykz7TfFsa_fjS5dYA32SmdJQviC7ok_5JINaDM6Z5E272ocxxxvn4HZEp2pcMjaJeHAX_aAVmD2tCCdoGuX0K9UvSmT5w6mi9ZcLUR3IsKJTSNUUoEeBZM-EMy5bMjZz6a10pSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
لطفا شهربازی که میرین هر چی رو سوار نشین؛ بعضی موقع‌ها همچی مناسب نیست و شیطنتتون گل نکنه بخواهین یه تجربه کنین.
این فقط دیگه نریده بود تو خودش...
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/71381" target="_blank">📅 23:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71380">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owrLj8d47cJGEEoa1lXWAR-hf4E64bdv6MAoPrAdJZXvqhTnvfhRxj2ja1iwwn1Fa2aiTM1lkWK1IwREIk7PjySs8FfbCsxVO33yOTsXW0XdFOMYa75_4PLxUMNOukJjw5jWCDidCLqNPKdeWgG8Q5r2_FqU5eSOhWZgyYYuMskJQR7zjoU0YVF4fassNvS4lCs0KCi1eijcw28UrYWf3Et57sJrmKraIy97G0XuLD8CmBtQdbcMV2mJZJY3WH__90c6OxKOcAbptX9j1fvDG3YAalZJ4dH1jHNki4ZSp_zd4LyjEwMtyLRiJj8VdKAezjwoEsUg9H8dCfuuRm74PDTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0632abba0.mp4?token=pBur4a-deGVXVXT6sfGvL_s9QFpgv74GPzU4FNIGop-cbbo_KVYVIsA35yWY6nkzQb1GapEpHMfWXsYxvCosKs0H5-aFgtNKFF72lUqKJi0GBp-soBkeJD5I67jK57hlTHNfei56EOdTpxttlaOUkfzOKySPIFo-mIU7GFOGXCYqGThP_tYWsFCcRPzKfLbZi44jk8Szoi5wqZ7z1-OtwgU4KQ4sskFBa3CLYVWNmNUv30DPPza8X8i5TU2TOaeoqMQ87bMO8ue5VpoL1vB7EX4ZH_wvlWjONz0nhe5n2IXt28Zi2Fb7DFLtltF8XHlUxmc8xITH7k-vW9TPna1owrLj8d47cJGEEoa1lXWAR-hf4E64bdv6MAoPrAdJZXvqhTnvfhRxj2ja1iwwn1Fa2aiTM1lkWK1IwREIk7PjySs8FfbCsxVO33yOTsXW0XdFOMYa75_4PLxUMNOukJjw5jWCDidCLqNPKdeWgG8Q5r2_FqU5eSOhWZgyYYuMskJQR7zjoU0YVF4fassNvS4lCs0KCi1eijcw28UrYWf3Et57sJrmKraIy97G0XuLD8CmBtQdbcMV2mJZJY3WH__90c6OxKOcAbptX9j1fvDG3YAalZJ4dH1jHNki4ZSp_zd4LyjEwMtyLRiJj8VdKAezjwoEsUg9H8dCfuuRm74PDTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
#فوری
؛پرزیدنت ترامپ:فکر می‌کنم جنگ بلافاصله بعد از انتخابات تمام می‌شود.
دلیلش چیست؟
چون دیگر نمی‌توانند دوام بیاورند.
آن‌ها به‌شدت تلاش می‌کنند بر انتخابات تأثیر بگذارند تا گروهی ضعیف و مطلوبِ خودشان سر کار بیاید؛ کسانی که کاری به کارشان نداشته باشند و بگذارند به سلاح هسته‌ای‌شان برسند
تمام خواسته‌ی آن‌ها سلاح هسته‌ای است، و اگر به آن دست یابند، کل دنیا دچار دردسری بزرگ خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/71380" target="_blank">📅 22:43 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71379">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=OLWGpWDC9EdMOU89fImAuJvQRzuEyKTWOZ8U5u-jtvURmIwMKeo8TcjhMO5JbSUeUgE9FyxiDWgLReJHySyx6y9xnxb50Eptf_NsGj2sUSlgviPRZwuuwlJCrFph1zQoz_xgkkvXZgtWQUOHh5YAK0tmkAdJ4uYGbaGu7xfAJhWDHOVuH6Y9zJxs0ijhATOZ9Tjyc23EYPD4N1l_UcxNSDAZS7zqRP4cr8rX1RfzRh7GMKTMXHOXXv8hAPMw_N3ydIaW0fSwQ0eC5h2wpWiiFgAPh0Z23SSdLpng29l0M33pMeHIobY3fCuvvME2ZUZ6romkVvh-S2cz61MW9Ran7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1f6c19e60d.mp4?token=OLWGpWDC9EdMOU89fImAuJvQRzuEyKTWOZ8U5u-jtvURmIwMKeo8TcjhMO5JbSUeUgE9FyxiDWgLReJHySyx6y9xnxb50Eptf_NsGj2sUSlgviPRZwuuwlJCrFph1zQoz_xgkkvXZgtWQUOHh5YAK0tmkAdJ4uYGbaGu7xfAJhWDHOVuH6Y9zJxs0ijhATOZ9Tjyc23EYPD4N1l_UcxNSDAZS7zqRP4cr8rX1RfzRh7GMKTMXHOXXv8hAPMw_N3ydIaW0fSwQ0eC5h2wpWiiFgAPh0Z23SSdLpng29l0M33pMeHIobY3fCuvvME2ZUZ6romkVvh-S2cz61MW9Ran7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خبرنگار:
شاهد حملاتی در تنگه هرمز بودیم.
🇺🇸
پرزیدنت ترامپ:
خب، این حملات... این حملات کار ماست. ما 9 تا از کشتی‌هایشان را از کار انداخته‌ایم. بله، می‌توانم بگویم که این حملات از جانب ما انجام شده است. اما... و خواهید دید، خیلی بیشتر از این‌ها خواهید دید... وقتی که به آن ضربه بزنند؟
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/71379" target="_blank">📅 22:31 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71378">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=UQ_-6mSEgFDwf7NM6EIcJtb4XgDeN0-jUcc7u4jVX-9rFAW2kJcZYvMw-vbrkkUI-BylW67iczYkxWB54IzXXDNQnII--jU5ukficmu-OSuCOw7DN9_g0i_jrDqu5f9OqRqJn9RpaxgLgHbA-A1MMs199puOHTUQvnd5IFRVavpTXtNWnHdtYNqellkcuVFpCeSfUnV8zbKVgVP8XswC2UU6ZzmgFK0FmsiQ39wEl3tY67oSrv67-m3WhyDvhKYz8kFNL0uVOpPyhM0U_3aqOhwZI--Q7xMCHE2T2jZI9VgAGLu5NKT9E7oAi-y50MHdlJuJYlxPm7yTH1gwLbHeZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c27e89aeff.mp4?token=UQ_-6mSEgFDwf7NM6EIcJtb4XgDeN0-jUcc7u4jVX-9rFAW2kJcZYvMw-vbrkkUI-BylW67iczYkxWB54IzXXDNQnII--jU5ukficmu-OSuCOw7DN9_g0i_jrDqu5f9OqRqJn9RpaxgLgHbA-A1MMs199puOHTUQvnd5IFRVavpTXtNWnHdtYNqellkcuVFpCeSfUnV8zbKVgVP8XswC2UU6ZzmgFK0FmsiQ39wEl3tY67oSrv67-m3WhyDvhKYz8kFNL0uVOpPyhM0U_3aqOhwZI--Q7xMCHE2T2jZI9VgAGLu5NKT9E7oAi-y50MHdlJuJYlxPm7yTH1gwLbHeZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت ترامپ:
کمی بعد، اما درست بعد از انتخابات، چون آنها دوست دارند اوضاع به این شکل باشد، اما درست بعد از انتخابات، قیمت نفت رو به کاهش خواهد گذاشت. قیمت‌ها پایین خواهد آمد و فکر می‌کنم قیمت بنزین را پایین خواهیم آورد، به زیر ۲ دلار در هر گالن.
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/71378" target="_blank">📅 22:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71377">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NSbzTPQrs41OfNh0LiVCEcB-ovEMzEFo0GYMKmLZSpmPVa4ZgzaLdgigaLqYSwGZ08E08FVXxhOhB12wrhxbDW4IERQiK7vc9YGJ3wcrvfdi6bqz7fEX7kqRuag88RC8ok-sfu-nHrcerH2VGHrhIsGPPtWdu9aqe086E57NVlBlcEFwOEN-nRdyrltMV9OwAnaA_madlxdW6lxYt6sYwDXLXvAR4k5ObGh5RBEu2_kSboRT-yammOXyWS5yjN3i9a-NqSeP_BVm3Up0HPuA-IhkQisD30lUfU8KFBcjsnPGrFsGrrTlsnTQCs3mAb4svvRPfOiGkxXDOu2zzqmGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/34c7f74659.mp4?token=NSbzTPQrs41OfNh0LiVCEcB-ovEMzEFo0GYMKmLZSpmPVa4ZgzaLdgigaLqYSwGZ08E08FVXxhOhB12wrhxbDW4IERQiK7vc9YGJ3wcrvfdi6bqz7fEX7kqRuag88RC8ok-sfu-nHrcerH2VGHrhIsGPPtWdu9aqe086E57NVlBlcEFwOEN-nRdyrltMV9OwAnaA_madlxdW6lxYt6sYwDXLXvAR4k5ObGh5RBEu2_kSboRT-yammOXyWS5yjN3i9a-NqSeP_BVm3Up0HPuA-IhkQisD30lUfU8KFBcjsnPGrFsGrrTlsnTQCs3mAb4svvRPfOiGkxXDOu2zzqmGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یه هموطن بعد از گرونی بنزین زد به سیم آخر و از بالا تا پایین مسئولین رو یکی کرد.
حاوی الفاظ رکیک، هندزفری لازم
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71377" target="_blank">📅 22:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71376">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKf9UNP1yuOSJf96XaxAxp2BtavUEMVb36GeeGagkNoRDLJ9n5sgSFjupKFhfms1pu86aE_fomj8AfzkrVpzQXB_J2_MdFCjme3fCNtGZlFD-jLCYPHRNqZGs4tltGKw3WTsQF_NgFtZloDQS6yWe-3rO5rfZFruH49b2KUV9KkRF-0DnEZcHuzxOsy4sqbYgBOU6WMmoLNXDVKE9o53ephoB7DA8jDNJQvI2l-cD7kn5Bh1xsCOlKGFTuNkEY_loOxKI4HUT--PInsHRm7q6eyyqfGO9Srkb8rqeKHTyIKayvpZR9HAPrbkwgML40K7zeQQfiTdwRunKJQZ-qmeBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
🇺🇸
🇺🇸
به گزارش «نیوزنیشن»، دونالد ترامپ همچنان در «بال غربی» (West Wing) حضور دارد و طبق برنامه، هنوز عازم دالاسِ تگزاس نشده است.
ترامپ در حال دریافت گزارش اطلاعاتی به همراه جی‌دی ونس (معاون رئیس‌جمهور)، پیت هگسث (وزیر دفاع) و ژنرال دن کین بوده است.
احتمال می‌رود این جلسه پیرامون موضوع ایران باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/71376" target="_blank">📅 21:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71375">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d22f299161.mp4?token=IatKLcovIictCdYtORRY11LzWOgIaB-gsvE9sGFouYQZD9r_vx9QoeUNrjFt3avVf0aAxEHheNyJgkHUsuL3ji6utn0ftFO_3tp98b3rjWVWMF8YB7e_F3XH70KGzPi1CdH9d29pyG0kS1DBu5oJwGmnaaNRJTm8RGBlPyG-ipW1S6NR02LHesNwda6HO1BagmFDKOJy7L7vEhflbxruGUm7D-hwCOKWEcnG03a-fUy4rp_pE4Vs5bj13yM3pyFgGY_Oxgz65atGv2BADvksMvKfnFvcpEk4AKdFWPyD2IW9nsAwgVDcfacLRjGOkwRvLvN3uxBKsC_z2POY1b5vtA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d22f299161.mp4?token=IatKLcovIictCdYtORRY11LzWOgIaB-gsvE9sGFouYQZD9r_vx9QoeUNrjFt3avVf0aAxEHheNyJgkHUsuL3ji6utn0ftFO_3tp98b3rjWVWMF8YB7e_F3XH70KGzPi1CdH9d29pyG0kS1DBu5oJwGmnaaNRJTm8RGBlPyG-ipW1S6NR02LHesNwda6HO1BagmFDKOJy7L7vEhflbxruGUm7D-hwCOKWEcnG03a-fUy4rp_pE4Vs5bj13yM3pyFgGY_Oxgz65atGv2BADvksMvKfnFvcpEk4AKdFWPyD2IW9nsAwgVDcfacLRjGOkwRvLvN3uxBKsC_z2POY1b5vtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🤡
اوستاد خوش‌چشم تحلیل‌گر ارشد صداوسیما:ما به سوی یک درگیری تمام‌عیار و کوتاه‌مدت در پاییز می‌رویم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/71375" target="_blank">📅 21:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71374">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iJgU4XWqIGWCrov04i_KqZH0sIfikWFCA_GKfbgcp6_q944RWP2Hgn_avyriGNe1Y0Xa1Nzn9zlg7kEJadPNQMuEtr0HtfX076dREJkINZ0g8Dw1UEX-DxE-T_nqIqp24-mpra8qFLg6Ub5v0GWRh4zq8Vh1gaNXS8kZbRvVDAUE4Mysli7uPkapxAiwNpZ1zvqJcjiW8FDlUUDXa_Lk2fpLJcH-9MeVDpd-fkl9P5LSy1ckXQySMyYo5604FOHJ5-geQ5hCTPEg5Xk916Kt3md9foyEJ-8lh-AQNYNzgHsmhUuwTk5xdNMagQHBt9Zsc2Nvmw2p429AQGNk1iwkHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">☄️
تصویری زیبا از رعدوبرق دیشب تهران.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71374" target="_blank">📅 20:50 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71373">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=PyKciRq9wL2jQd8tSijWmRdwdPbDTExQK4YxlkLBpTks4ojz9dJCciJ4w1deSYhAnoXq-IoTo_ceIW83nFE-JdHTMu8hzICa8ociXTcQyVEfAvnvIg1rAB4Ix8bsiJ35LiXN2M57a7algxe8tW8ZhBQYn23U-DlgHhc99clFcnlAA6vgzMSKF_2v6wDU1_a0iOndu1nkySx1c4Z0613YTMFzCgs4sEdOyn2-vSgIAu8kQAk31qaEZ6fGMwNmNwlLgYpcJuMbaKr6HNkdxIjd4o4B2LWtP4viOe2WbabTF1PSR2Rs9SmS-ZzIFV_gZWwlco9rz4YOu0bJwvn-NVKDrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69c9063c46.mp4?token=PyKciRq9wL2jQd8tSijWmRdwdPbDTExQK4YxlkLBpTks4ojz9dJCciJ4w1deSYhAnoXq-IoTo_ceIW83nFE-JdHTMu8hzICa8ociXTcQyVEfAvnvIg1rAB4Ix8bsiJ35LiXN2M57a7algxe8tW8ZhBQYn23U-DlgHhc99clFcnlAA6vgzMSKF_2v6wDU1_a0iOndu1nkySx1c4Z0613YTMFzCgs4sEdOyn2-vSgIAu8kQAk31qaEZ6fGMwNmNwlLgYpcJuMbaKr6HNkdxIjd4o4B2LWtP4viOe2WbabTF1PSR2Rs9SmS-ZzIFV_gZWwlco9rz4YOu0bJwvn-NVKDrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇷
⭕️
#فوری
؛شورای حکام آژانس بین‌المللی انرژی اتمی امروز، ۹ سپتامبر ۲۰۲۶، قطعنامه‌ای را تصویب کرد که بر اساس آن، موضوع هسته‌ای ایران به شورای امنیت سازمان ملل گزارش می‌شود. این نخستین ارجاع از این نوع در حدود ۲۰ سال گذشته است.
۲۳ کشور موافق قطعنامه بودند.
روسیه، چین و نیجر مخالف بودند.
۸ کشور ممتنع دادند و یک کشور رأی نداد.
🔴
قطعنامه با ابتکار آمریکا، بریتانیا، فرانسه و آلمان ارائه شد.
دلیل اصلی اقدام آژانس، عدم توانایی بازرسان در راستی‌آزمایی کامل مواد و فعالیت‌های هسته‌ای ایران و پاسخ نگرفتن درباره آثار اورانیوم کشف‌شده در برخی سایت‌های اعلام‌نشده عنوان شده است.
آژانس همچنین می‌گوید به دلیل محدودیت دسترسی، نمی‌تواند با اطمینان درباره میزان و محل ذخایر اورانیوم غنی‌شده ایران اظهار نظر کند.
⚠️
اقدام بعدی در شورای امنیت خواهد بود و هرگونه اقدام الزام‌آور جدید در آنجا با توجه به حق وتوی احتمالی روسیه و چین با موانع جدی روبه‌روست.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/71373" target="_blank">📅 20:29 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71372">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=OGJZamcXzbodBv6WvIH7WUACKkJG9NaPnaMoBDQ1SLKsuV5bPMjDcV4VJBmJr2kF2vdLngSuuBDq5bcEjn5YZ3sHkMBKiFd4CfZVMNRsTJS4ckxeD1QBbbRWqSswdxvdgqf4oMTyti2VcF77zxljC2hjFkeWR5_PBpz4FMlgt29DJ-QPyYf2n7WronrdCjBYqtmNsMNFDfT_BoAY622J9e81-yVKNFB1ed2RCoap0UXiIXnbsTHQJbDazXwkpnOkiijFi1rZiyuu1UOcx7FSdAfmPVGAZcNWtIlF5FBgoNLgziSOlUNUUNRooQiG3wBYKNiSWMQtXUiH1PcnZ7WJSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4fc965eb9f.mp4?token=OGJZamcXzbodBv6WvIH7WUACKkJG9NaPnaMoBDQ1SLKsuV5bPMjDcV4VJBmJr2kF2vdLngSuuBDq5bcEjn5YZ3sHkMBKiFd4CfZVMNRsTJS4ckxeD1QBbbRWqSswdxvdgqf4oMTyti2VcF77zxljC2hjFkeWR5_PBpz4FMlgt29DJ-QPyYf2n7WronrdCjBYqtmNsMNFDfT_BoAY622J9e81-yVKNFB1ed2RCoap0UXiIXnbsTHQJbDazXwkpnOkiijFi1rZiyuu1UOcx7FSdAfmPVGAZcNWtIlF5FBgoNLgziSOlUNUUNRooQiG3wBYKNiSWMQtXUiH1PcnZ7WJSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇦
🇾🇪
ساعاتی پیش، چندین حمله هوایی عربستان سعودی در حمایت از عملیات «شورای رهبری ریاست‌جمهوری» (PLC)، مواضع حوثی‌ها (انصارالله) را در جبهه مأرب یمن هدف قرار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/71372" target="_blank">📅 19:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71371">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
شنیده شدن صدای انفجار در جاسک
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/71371" target="_blank">📅 19:25 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71370">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgo44cI1fK7V4Nkj_K8u6zcGALMm8qmDA9BTrrsQYFNjlA0mZ0mtezqt6yqK5wKcjXIITWnfzmXhZg95TZsW1-QubWDYqRZh0Ivcs6Uvztl4DIaEGu4jQbaIH-d33sE08EoOV3bfm8WaxHqLGYAkWd1ILF4sfRhFYTfldsw5uR0xnhQmrBIEsWSBpGN7VJ9Tpdm7MaBCpvI2O-Pxbs1jTTdjWMWL3q9digzbTCL-vnrX4-QbI-grW3cmCnqia2Qq1NBvKF4-QcmcWALWb0M48Z5h7vxlw72Nv70dUb1i17pB1wmMWZ8OCkL8Nl-dXhcTIqk_xtwvWzuwc_86eLEhmFHc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cb4ebfee62.mp4?token=sQ-kB8zsbUe9O5OL4U0NNApGJ-fy3U5rO-z8IDIF-cHCxvOpW-F84FkBaxK3aXt7P86ZPOgdg7DhEy8WdtYb1VJeyKfn3zLDoFCXZ2eiZMqlkQPbOc-34QMv3wkcfMYdSoRGBsI0GSYiNg5V1jqPAVnYyEcesSm_q-STvKyRlBja8vvGG3pUUuXo5y1BjghrEARiG1_behb6IGTIwyqh_Bfrl8txnNIp7ZDMDLFP1NLisjwW-JP_ZpjkVeZ9KcCZ0nYFn9cdSRS8Y1c0sFbmzItfDPpLE-NKjT0LFuYHVJKPLrd-hUS3VeLrzXqE1n5H_NB7Jgv70ilJK3nHDtxPgo44cI1fK7V4Nkj_K8u6zcGALMm8qmDA9BTrrsQYFNjlA0mZ0mtezqt6yqK5wKcjXIITWnfzmXhZg95TZsW1-QubWDYqRZh0Ivcs6Uvztl4DIaEGu4jQbaIH-d33sE08EoOV3bfm8WaxHqLGYAkWd1ILF4sfRhFYTfldsw5uR0xnhQmrBIEsWSBpGN7VJ9Tpdm7MaBCpvI2O-Pxbs1jTTdjWMWL3q9digzbTCL-vnrX4-QbI-grW3cmCnqia2Qq1NBvKF4-QcmcWALWb0M48Z5h7vxlw72Nv70dUb1i17pB1wmMWZ8OCkL8Nl-dXhcTIqk_xtwvWzuwc_86eLEhmFHc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
پسر‌بچه ارومیه‌ای که چند وقته به شدت ویدیو هاش وایرال میشه موزیک جدید داده بیرون
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/71370" target="_blank">📅 19:03 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71369">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=hIAqLWCZXNHYFOdwSDPBI4OCAAK0kgjhzlbCbxvK6VreYSSVLWjpZxgRRF5qvxe1Uq20QAfWu3-mSDuRwTk50KpV-U6XMX5_TNEUIMkYPfnz0XFBtVNllk2F2Mp5_aHIABq6HvnofXaSHJ7_1zH6En83tizyjd84lzt-rSky-hKl9MFbckPF0MsC02wxOl0ZRAMLb8FPjonzSwTZpSnwKhUZJoFUWF8D5OQnLf_jueaVDcdpsulWeliqrxideCbGl3HBsOTJzAItooyo_Of7wVfDMwb6rLHlOodLRoOtyWb9X2cIgJZU1V2HvtmyUHxkhl0_s4RJ9pkSUsjLVP1HwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/696aa56e23.mp4?token=hIAqLWCZXNHYFOdwSDPBI4OCAAK0kgjhzlbCbxvK6VreYSSVLWjpZxgRRF5qvxe1Uq20QAfWu3-mSDuRwTk50KpV-U6XMX5_TNEUIMkYPfnz0XFBtVNllk2F2Mp5_aHIABq6HvnofXaSHJ7_1zH6En83tizyjd84lzt-rSky-hKl9MFbckPF0MsC02wxOl0ZRAMLb8FPjonzSwTZpSnwKhUZJoFUWF8D5OQnLf_jueaVDcdpsulWeliqrxideCbGl3HBsOTJzAItooyo_Of7wVfDMwb6rLHlOodLRoOtyWb9X2cIgJZU1V2HvtmyUHxkhl0_s4RJ9pkSUsjLVP1HwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز تو بجنورد، فردی که سال‌ها با معلولیت شدید تو یکی از خیابون‌های شهر دیده می‌شد و مردم هر روز بهش کمک می‌کردن؛
به محض دیدن پلیس کامل درمان شد و درلحظه به‌طور کامل کاملاً شفا گرفت.
طبق گزارشات این فرد روزانه چیزی بیش از 20 میلیون‌تومان درآمد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/71369" target="_blank">📅 18:15 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71368">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=MAMp52OZ9w6A4mw78CjIMpFoWh7lPmxLaMJnATPKLDxla60LQuMhrCU21rJzKpRKSEVvlqOK8LV3X36wblNgzdpisSwC-HXo5qpBBzJrinMQB96cgH7I04PgI2MVzagQ6M_pzmTNXF9-sTudq9rtIv1XJ2rbct9qZgl1RtVfNn2b0DolDIgCZcri4eEnFaF5LmUsLpevNG6_6uidgNLi7p6_w_iKHVnzE_zE4IPDKwH6G4xvUD0KQt0ZBrE4IWJkRjH91grH7SvW0nnaqkiBcaZeOm7XtMixeYUWTQOHXgXL-Yc3jdAfg3jLDBsciYqdVyknovr_Q8c3NHMWfqyUeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a8d769b56.mp4?token=MAMp52OZ9w6A4mw78CjIMpFoWh7lPmxLaMJnATPKLDxla60LQuMhrCU21rJzKpRKSEVvlqOK8LV3X36wblNgzdpisSwC-HXo5qpBBzJrinMQB96cgH7I04PgI2MVzagQ6M_pzmTNXF9-sTudq9rtIv1XJ2rbct9qZgl1RtVfNn2b0DolDIgCZcri4eEnFaF5LmUsLpevNG6_6uidgNLi7p6_w_iKHVnzE_zE4IPDKwH6G4xvUD0KQt0ZBrE4IWJkRjH91grH7SvW0nnaqkiBcaZeOm7XtMixeYUWTQOHXgXL-Yc3jdAfg3jLDBsciYqdVyknovr_Q8c3NHMWfqyUeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازی مناسب برای جوانان خاورمیانه ای:
یه سایته یه بازی ساخته، میری توش بمب اتم مورد علاقت رو انتخاب میکنی و میزنیش تو شهر مد نظرت و بعد بهت میگه چند نفر رو کشتی
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/71368" target="_blank">📅 17:34 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71367">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bpM9UsPaS4ltVVjFJ0FAgHzhSnpltp4zW7xj_mYDZD8Eknu--t4gI5ffqv8dapcKhJyuwyT8siTUBNc0Vbgu_9rjVbX55LzCLCPMOrcpQpIVN-xEQ2KYqIZT-KV6sUjZqG6b4CJ0X4FTqCCnPeLPha4V1UpBRzamJd2k4vwWkja_Y0sifdnBu1zi3XqvHvPpl0TDgwn0ll7ANiEALEw3_3kjoGW018aAxvQROhw599PzGyZaYButauvFQ-gL9X7ab8VSlUwi2pG3oSfLT740_o_GzgmdLu1_6jndU-vKoJbqgkvjDV9Q4rsLP-S_1WgDkPFyKsBxCjlYHgrgasjDKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⭕️
🇮🇷
🇺🇸
📰
سی‌ان‌ان:ایران به سرعت در حال ساخت یک تأسیسات هسته‌ای مشکوک است که در اعماق کوه گرانیتی نزدیک نطنز - ملقب به "کوه کلنگ" - دفن شده است و تصاویر ماهواره‌ای افزایش ساخت و ساز در سال 2026 را نشان می‌دهد.
این سایت احتمالاً برای محافظت از سانتریفیوژها یا کارهای غنی‌سازی فراتر از دسترس بمب‌های سنگرشکن فعلی ایالات متحده طراحی شده است.
ترامپ تهدید کرده است که به آن حمله خواهد کرد ("ما ممکن است خیلی زود کلنگ را بزنیم")، اما بزرگترین بمب غیرهسته‌ای پنتاگون ممکن است به اندازه کافی عمیق نفوذ نکند.
نشانه‌ها نشان می‌دهد که ایالات متحده در حال حاضر روی این مشکل کار می‌کند: یک روز قبل از شروع جنگ، یک آژانس سلاح‌های کشتار جمعی پنتاگون قراردادی اضطراری برای تعمیر یک تأسیسات آزمایشی زیرزمینی که در گرانیت در وایت سندز حک شده بود - مرتبط با شبیه‌سازی حملات به عمیق‌ترین پناهگاه‌های ایران - امضا کرد.
یک بمب "نسل بعدی نفوذگر" در حال توسعه نمونه اولیه است.
تحلیلگران CSIS می‌گویند کلنگ هنوز عملیاتی نشده است، اما ساخت و ساز از حفاری به ساخت و ساز داخلی و سخت شدن تغییر می‌کند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/71367" target="_blank">📅 17:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-71366">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=CW9Pe5knfXVhOzN5K96DQ8cNN2-Knc-6vtKHkcQvFIDKefs55zeQcyxYbWyfUsKKCyNP9QHbb6_QieQSAvxlrIMUFCp_lT74rUTNEgKmzfXKJg1ls5oyctsJGtxTMRuAQ1GhLjrPNwd1ALh7xAqih9nmJg2dRtAG3uVQMGT8yByNfnAAVdEXue55NyBcZgPip_MMFyZCF8SdNPQl8WKTu2wekzhitZtsuFWVDrKchBGjh7TGWd6CrPwcRJhpWt_WCLsllQHVvoBa4D_hdY3DQ8s_psY4JnEmie1qOeeaNtIgyfQ5SyWDqbsFzYdQm6B6XVWxxuhbRtMrLZfph2bs2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6e3b3343.mp4?token=CW9Pe5knfXVhOzN5K96DQ8cNN2-Knc-6vtKHkcQvFIDKefs55zeQcyxYbWyfUsKKCyNP9QHbb6_QieQSAvxlrIMUFCp_lT74rUTNEgKmzfXKJg1ls5oyctsJGtxTMRuAQ1GhLjrPNwd1ALh7xAqih9nmJg2dRtAG3uVQMGT8yByNfnAAVdEXue55NyBcZgPip_MMFyZCF8SdNPQl8WKTu2wekzhitZtsuFWVDrKchBGjh7TGWd6CrPwcRJhpWt_WCLsllQHVvoBa4D_hdY3DQ8s_psY4JnEmie1qOeeaNtIgyfQ5SyWDqbsFzYdQm6B6XVWxxuhbRtMrLZfph2bs2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یه نفر مسی رو پیدا کرده بهش میگه بگو علی تولدت مبارک
😔
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/71366" target="_blank">📅 17:09 · 18 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
