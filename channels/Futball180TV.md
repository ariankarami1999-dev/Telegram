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
<img src="https://cdn5.telesco.pe/file/m51dmwXhcIGukHD-4zyFjn-wfXOEgzVfysImEuOILdut0QuXa4tM5z1LfdT1v4XlNcOIATxOGAucvYdSEVqF5OHxhmQVX0NHF0rh05D0ifeACeNS2qjr7ECe33wRTwW7HiA8TXgKLSeTwWPRJThLbyCD_AppRQXdnEFU_8RUyCuNv0yzBTftOX4nf4VHVCvC0YPK-YCNiv1rB639nXlMse9hV2bhdNp42ZbazJUWzOPdNxq4LetAP7NdAvBR5eNi3OWMZQ5M79GqWPWbeN4Pq3Im5qXhmyDKqQhUSxnjIUT2xsEbgjoXBvImPmO_2_hL3mPfCkmZovyDx28uVuEfFA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 401K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-03 20:53:33</div>
<hr>

<div class="tg-post" id="msg-107263">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=kmmujNFiH0_FSk6qu9hwrNFGOqrGbfNCjRntdTX8MiYsUr302Xig9YcXHSmLbcmcPmK3ZkV0T2kKQvGTmuxLIjL0LNz3_rR6gGKuZr_-hA2jYfZitptASAB_7CTjQmzbbu_uPJqa2DJYnupWmVVb8Mo8foS9Ak4IwWp0j9JygzqIQkWvri74NLNyHg0Ek2KjtLZjuk7B81HBIroofiKKrTy79Iwz9RntFwUIViBZxxFVoDQcCvFtJLC-XKeTl3cogC7lzlweyfXYkQQDHGYzVedorrStMdTtdnQh2b9MHw1TiAnBRQtfPBcR8k3NCPPbiEvdisFXEakybdLDM0RgPg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29c2608c24.mp4?token=kmmujNFiH0_FSk6qu9hwrNFGOqrGbfNCjRntdTX8MiYsUr302Xig9YcXHSmLbcmcPmK3ZkV0T2kKQvGTmuxLIjL0LNz3_rR6gGKuZr_-hA2jYfZitptASAB_7CTjQmzbbu_uPJqa2DJYnupWmVVb8Mo8foS9Ak4IwWp0j9JygzqIQkWvri74NLNyHg0Ek2KjtLZjuk7B81HBIroofiKKrTy79Iwz9RntFwUIViBZxxFVoDQcCvFtJLC-XKeTl3cogC7lzlweyfXYkQQDHGYzVedorrStMdTtdnQh2b9MHw1TiAnBRQtfPBcR8k3NCPPbiEvdisFXEakybdLDM0RgPg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تقلید صدای جالب یاسر آسانی توسط حسین گودرزی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/Futball180TV/107263" target="_blank">📅 20:42 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107262">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🔺
✅
🇬🇷
روایت شنیدنی نوید استادرحیمی از تیم‌رویایی یونان که در سال ۲۰۰۴ قهرمان یورو شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.43K · <a href="https://t.me/Futball180TV/107262" target="_blank">📅 20:30 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107261">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=ttf6jZbOYA0bfKDZBe2ANR0v6V2sMk1iucajqa559imi5oMh5LmfKgotViNIlXMm8a1w-ZfNIIbv3n7Sib1EYHc_bho89xEcwafSzS8gaJsZPdeTJaKNOL__dNYHVTXFAdntjAfwHuczcF4_NbTrKuU1HwBXBnWPY3PCTHiEsAZM1Q12evxb_xFpbUVskqF1jl5LytSwUZByaGy36uDu4bMZtBRIScSonYEvHx73JbwbWdyKahGVP2aT_jzRJCagRircAStxKylEm4mqzBR8jRyyuEphqlQa0uGxI3r_JuTy1wyQ-UHGhwXyAYj6RkwfrPvKsO_mvYbonVWPVNxWXHVmyMHRD7dRDwH2ejdNih26AtsSa3rUQjkDQUfeW9LE5gmIbjsgoeueu8imdNMv-t5raewFHDw8pvE-uLOd-7MHYH5vYiODq5olBnUkCcY099MvZyNpoJmePUlizU514ysqOT3fXQQgMyZkCBWKDL0cMHEjlwPR4-1zjuGcYcu4dNO36bF__y0rsN4NXKkF0Vate-lrYts5DwcshnZ9JHaqUtc_9QG2o49ImukAjJpzQdOn64yW9SQXsrmNHDG9no8C5ZXbOgs5wFryNYz75ZZG77bfkCyoUiYOo4jq4HndULPkf7iSljeYtslp3BqsungsBqw0V7SYLhyjt0dW69g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19b5e1f435.mp4?token=ttf6jZbOYA0bfKDZBe2ANR0v6V2sMk1iucajqa559imi5oMh5LmfKgotViNIlXMm8a1w-ZfNIIbv3n7Sib1EYHc_bho89xEcwafSzS8gaJsZPdeTJaKNOL__dNYHVTXFAdntjAfwHuczcF4_NbTrKuU1HwBXBnWPY3PCTHiEsAZM1Q12evxb_xFpbUVskqF1jl5LytSwUZByaGy36uDu4bMZtBRIScSonYEvHx73JbwbWdyKahGVP2aT_jzRJCagRircAStxKylEm4mqzBR8jRyyuEphqlQa0uGxI3r_JuTy1wyQ-UHGhwXyAYj6RkwfrPvKsO_mvYbonVWPVNxWXHVmyMHRD7dRDwH2ejdNih26AtsSa3rUQjkDQUfeW9LE5gmIbjsgoeueu8imdNMv-t5raewFHDw8pvE-uLOd-7MHYH5vYiODq5olBnUkCcY099MvZyNpoJmePUlizU514ysqOT3fXQQgMyZkCBWKDL0cMHEjlwPR4-1zjuGcYcu4dNO36bF__y0rsN4NXKkF0Vate-lrYts5DwcshnZ9JHaqUtc_9QG2o49ImukAjJpzQdOn64yW9SQXsrmNHDG9no8C5ZXbOgs5wFryNYz75ZZG77bfkCyoUiYOo4jq4HndULPkf7iSljeYtslp3BqsungsBqw0V7SYLhyjt0dW69g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
🇮🇷
بابک مرادی بازیکن سابق استقلال:
🔺
به ولله برای خودم اشک نمی‌ریزم. مگه میشه ایرانی باشی و با این همه ثروت کشور از گرسنگی بمیری؟ وطن مثل ناموسه، برایش جان هم میدهم اما الان شرایط اصلا خوب نیست
🔺
در مراسم عروسی‌ام چهار هزار تا مهمان داشتم و پول یک خانه را خرج کردم اما فدای سر همسرم چون به عشق اون عروسی گرفتیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/107261" target="_blank">📅 20:04 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107260">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=PGN5v3H-ABodRQ_ZzQeV-NkztbAWLMqZWBGMTh2_8zDvrlHx-cQYvO6AU1Bb8eDvUF1sCs_lUPOV5iA3mVBD2fLLGlZ5NBnJ0KUA7ouDnltd8LyvcUDEwHwZG79ALwa0CKms-lHS2bfrZg7v0EObcJICXkFj5n6y9UWc6Fx8DifAjfEhcZTo4AmzitWcIAmQ_K-eSATqFW7zpX1r19cBc_mSDffFqTKtH8F59B9NZb2NKoLs11jt8Jy6U1RoWNgVGbnH1P1kUyZsuZX0vttbG6Idsl9XXwdfiVXFBoZL2Q3jFjZQUsGlMQxsJCD2BTx1fONQDOrg-aRc96_Z-EAjvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a1de71c42.mp4?token=PGN5v3H-ABodRQ_ZzQeV-NkztbAWLMqZWBGMTh2_8zDvrlHx-cQYvO6AU1Bb8eDvUF1sCs_lUPOV5iA3mVBD2fLLGlZ5NBnJ0KUA7ouDnltd8LyvcUDEwHwZG79ALwa0CKms-lHS2bfrZg7v0EObcJICXkFj5n6y9UWc6Fx8DifAjfEhcZTo4AmzitWcIAmQ_K-eSATqFW7zpX1r19cBc_mSDffFqTKtH8F59B9NZb2NKoLs11jt8Jy6U1RoWNgVGbnH1P1kUyZsuZX0vttbG6Idsl9XXwdfiVXFBoZL2Q3jFjZQUsGlMQxsJCD2BTx1fONQDOrg-aRc96_Z-EAjvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🐐
👀
مورگان راجرز: رونالدو بازیکن مورد علاقه منه اما من در نیمه‌نهایی جام‌مهانی در برابر مسی ۳۹ ساله بازی کردم و باورنکردنی بود، تصور کن در دوران اوجش چی بوده، نمیشد در برابرش کاری کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.76K · <a href="https://t.me/Futball180TV/107260" target="_blank">📅 19:33 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107259">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=iCVXhut5TEnunDrfDgZOfWXiJNeGgjGtF67emjWrR4SmCU_7Fa0Y2XkzDT8pQF8gfGCZoM3AEiVJOaR-LygQHRCIbiHyh3u0WX5zrihci1LvR61j01oQ3JeEmqOclN-Vmv8tyHmHbRQJ_zLXWZHBPOTmuKZbgWri07bdbUtrXAzSDCHJt4z3RkJDPtkSlDpdJhqmFkpNjy-ST0nEWcCuIDMtJLg-q5_Jardsf34C_FozUJm_dDrbfL2blO_mSIn11sSnsHnx_MJdnpZ6B5J8cn_9JEan46vTYPN-b1GXpQSgic00OcqDKOSTlEq87lYbDk_UNR-8n3m4vgNcDYnxOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/203f6a5b45.mp4?token=iCVXhut5TEnunDrfDgZOfWXiJNeGgjGtF67emjWrR4SmCU_7Fa0Y2XkzDT8pQF8gfGCZoM3AEiVJOaR-LygQHRCIbiHyh3u0WX5zrihci1LvR61j01oQ3JeEmqOclN-Vmv8tyHmHbRQJ_zLXWZHBPOTmuKZbgWri07bdbUtrXAzSDCHJt4z3RkJDPtkSlDpdJhqmFkpNjy-ST0nEWcCuIDMtJLg-q5_Jardsf34C_FozUJm_dDrbfL2blO_mSIn11sSnsHnx_MJdnpZ6B5J8cn_9JEan46vTYPN-b1GXpQSgic00OcqDKOSTlEq87lYbDk_UNR-8n3m4vgNcDYnxOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خایه‌کردن ترامپ از پرواز جنگنده‌های آمریکا در مراسم استقبال از رییس‌جمهور چین!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.68K · <a href="https://t.me/Futball180TV/107259" target="_blank">📅 19:03 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107258">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=Dj8MOUvkNOuK8a83VivKAO-aucDTXAZFDtq2sMWHqGoCxvyfJ_qMuFBln8f3Wn5z6z7YyEyKakAd31MBgdJEWqUBzHLOUVXjhSYn7pK-A3hZIOL1prQGaP2Mk6KrI5AaBqn2jeZeip6KSRDzTX8ZnzO7k00U2E9sh2Rd4gOrnx2UUml4xYiDThknLw-HDt30ej_2BWjz09yKRA9cbwvmsZ93sxzO215oXn-T-rlfDwOQdW0a-Ecz_CzZGDLge--inilZ0rPqSv1EDkyYg0E5AkL8vK25GKtmaKTjYJgeEoX_3Y4EbwAHOpDNYvERaXDQapEghUIZ2x8YQmYS4kekHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9c567de51.mp4?token=Dj8MOUvkNOuK8a83VivKAO-aucDTXAZFDtq2sMWHqGoCxvyfJ_qMuFBln8f3Wn5z6z7YyEyKakAd31MBgdJEWqUBzHLOUVXjhSYn7pK-A3hZIOL1prQGaP2Mk6KrI5AaBqn2jeZeip6KSRDzTX8ZnzO7k00U2E9sh2Rd4gOrnx2UUml4xYiDThknLw-HDt30ej_2BWjz09yKRA9cbwvmsZ93sxzO215oXn-T-rlfDwOQdW0a-Ecz_CzZGDLge--inilZ0rPqSv1EDkyYg0E5AkL8vK25GKtmaKTjYJgeEoX_3Y4EbwAHOpDNYvERaXDQapEghUIZ2x8YQmYS4kekHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
🇳🇱
در بازی هلند-آلمان چه گذشت؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/107258" target="_blank">📅 18:44 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107257">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VSLWbbWqJm7XskMnXNjhSXzO4XK9hZnJaM8pBVb51QdsACjzX_rtcPA7-ydZceaL6dMnaZMSajCuEF8ak-GWaTUOd6UgnIpo_ToAkhjXI8m434tR-Ab_lsN0PRVb7wsbf3tjoECqQKVjKjTWJV9-bvBlnodE9CHorjY1YE7sgl-LIUquQSgfx6csYIpH4tz9Ot4grLPR2D0AZOJxkSVdpWpavOvRrWdA8-4l0rqbzDzbxrxkKv_GSroksbkIUNoc_PQPMGaNy5gYs9hgQ0jl8vQhuJyMJPqwJRjXyMuNp2TLdpnq1I7T7Op39bWjaV2irpnDpLM_4JupdnVKwkPmSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇮🇷
🇮🇷
پرسپولیس در دیداری تدارکاتی مقابل چادرملو با یک گل شکست خورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107257" target="_blank">📅 18:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107256">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=bwgWjteTYRzV_ZWZXWd_IZHPwGAOsmE7Xp-JqtTW-iJFYGi1jFYPtEC9fgsnIXR373j88caSCdGTkHz0sYefVEuDx7NDGC1tUFHP1nv8zdGqeRp7wohxcHI8-CWHsMPpvPR8_A8mvoukRfM9eN-nl8Xq_tOCST4Jw_JZ70Wr10XHPcmazw4_qkAmLbVvabOovLbIU1dy19kWpWw5WEfOTPmERF2onQHGX_OzLXLgAcl6kYBdRjDsFRg1po8N9FFzd92NZS1XQfqi8X9eSpU_A5XBgC-TfMjSTrfcckAzTg4WsSZh6onNRcuDYupQiCdlgSPxz0A6Uu9VQyWFbGr6jA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68163d1ee3.mp4?token=bwgWjteTYRzV_ZWZXWd_IZHPwGAOsmE7Xp-JqtTW-iJFYGi1jFYPtEC9fgsnIXR373j88caSCdGTkHz0sYefVEuDx7NDGC1tUFHP1nv8zdGqeRp7wohxcHI8-CWHsMPpvPR8_A8mvoukRfM9eN-nl8Xq_tOCST4Jw_JZ70Wr10XHPcmazw4_qkAmLbVvabOovLbIU1dy19kWpWw5WEfOTPmERF2onQHGX_OzLXLgAcl6kYBdRjDsFRg1po8N9FFzd92NZS1XQfqi8X9eSpU_A5XBgC-TfMjSTrfcckAzTg4WsSZh6onNRcuDYupQiCdlgSPxz0A6Uu9VQyWFbGr6jA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
👀
واکنش رسول‌مجیدی به شکست عجیب روز گذشته تیم‌ملی ایران در مقابل ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107256" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107255">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107255" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/Futball180TV/107255" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107254">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WW7BOQVTeBTC5MATlUHLUWNZjCHgIrcJ3OqVIiGO6gHyjWHFkpJ_xBe52opFe6pHuuoZLayZmoI4f3ZlM2AIFccPWu-x8oT-PpLZZRovN4qcQgRJXbpGLsy2b1a03TzGDPs5KMP8g77ShRzjL6QchemYwrTYvyTbqt5fqocxovxPnRlPSVgwR1WPgTNiB-Su1fD-v2utWZGYO-nTi5SrLl49VgQm6VBXNWXczTeZekxm4Oex_1nXN0db94w_6VdhEVjcMc-q2YzSaKRi6ExoL2EuoHGF9r6NHcxmmZPUfLe36b8tvcPrviW0zVeWJeeUF1klrPb-M6rKstUDwHqjKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز فرانسه
🆚
ترکیه
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
فرانسه: ۳ برد، ۲ شکست و ۱۲ گل زده
ترکیه: ۳ برد، ۲ شکست و ۹ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/Futball180TV/107254" target="_blank">📅 17:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107253">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">‼️
🇮🇷
اشتباه عجیب مریم‌یکتایی گلر بانوان استقلال در بازی مقابل خاتون‌بم که‌دروازه‌اش باز شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/107253" target="_blank">📅 17:41 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107252">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v18VBI0SDTvCFMsvCJcyiFPbsi_q00Td3ICadZRqRPvpYLBf3dwPIFkD608KM-HqiK7RqlqHVyZsIC82Hj4VX7PXQszZPJhpfvanO5YazDzDGo6-eZZFXrvs7pOxbA2oO0ejmO4af_b729OknMZxva4BZVjV-sZx5uT_M8yP1vXy3FvCY4F9heOK_gx_b6qdNt9YJg8w9hYAJbPi9kY7wn6DiqoUZ_txpTR9N3DkbCuHtYaAuH0ob1CjayQX39ONsWDWFtSqC3_xQEzv1VTRACk-mjVmtOb-sJeWQ1uGLSeXrF-XPqzcQ4x2MFmFu0Tznb855D8b3MM3CSvPO22idA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
دیوید اورنشتین: درحال حاضر جریمه کسر امتیاز محتمل‌ترین سناریو است. در صورت شدت این موضوع، ممکن است حکم سقوط سیتیزن‌ها نیز صادر شود!
⛔
🔺
سناریوهای احتمالی برای سیتیزن‌ها:
🔺
❌
توبیخ و جریمه مالی.
🔺
❌
کسر امتیاز از منچسترسیتی.
🔺
❌
کسر امتیاز + سلب جام‌های…</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/Futball180TV/107252" target="_blank">📅 17:29 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107251">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLMbWiBpwLCaeYZTdpdMQPyn4ETQpQYkolC16HowlVZKTlWDjGC1Dk6Z5GvpBuBXj0JcuPnZDrPKrPCd4xlbL_5gxecuGCvNk0SDOKE2U2URaccceQiMhh6CfI49R4nahigHapqfZa-Bqfryw2fyccqmD_jJwdap8uayYArtbtsWMH-kfDq79aHK6nEE814WZs8VrWAQmZvBujmzrnqh-kW0A02yiKm7edquEOSoLx-qqKcZQBvhk1l2deCZ0ZUmcQKhxKkc8DsNn-EvA7z-NqLde_S81pAd-B69a9jBZQTBv1HW8zZK6_5ki6BFbUblMYUAwbOgt740z2wfcRytOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/107251" target="_blank">📅 17:22 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107250">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZzCwsNsLj7PKplPfdmFgxUwhWmGGw1l_J5_UgCE31rvn2hUW1K1HFDrpwSqyoaD_R-iO8eI1cXi6xlCI-pLaNHEUI610wlzSxNPjcoBcftLuJxrXL-9iJbPMTbxYGindrbIWXSvBEFOm6Puc7YZeQ2fcTOsIW3p_yElBpgWPNJV4oaSS3R-P-ZLrwKc2onVfLd-UolMqNFNZ1SDg0mv3M7dn6yhNtHyUp6f4Y6sx29bzv393sdntRtSdGRQvXcB6olEwJX541GoFLTZr_KqC1-DBPvPCvoxoyy2r3sk0NcvS9yPzSmE7Jso3AI1_xo_Ltf-o5fOgjQe90b2hA8khw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
‼️
منچسترسیتی در پرونده ۱۱۵ اتهام مالی مقصر شناخته شد
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از اورنشتین، منچستر سیتی تقریباً در تمامی موارد اتهامی مربوط به نقض مقررات مالی لیگ برتر انگلیس مقصر شناخته شد. انتظار می‌رود این باشگاه به حکم صادره از سوی کمیسیون مستقل اعتراض کند. هنوز در مورد تحریم‌ها تصمیمی گرفته نشده و روند رسیدگی ادامه دارد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/Futball180TV/107250" target="_blank">📅 17:19 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107249">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/638e170672.mp4?token=o6Rgj3yrWD1UXba66yH_D5ph0D9C5mOXuYl2aV2KBWRHb713N673Z0Splch9VVE-vd4h69ZSR-AojInoK6j7oKSphtMtkBqQOKwSXidE9xQZC2e4fj5TOeNvDcE5Tuausr66DUtX2I2V6t0CFCbW0uIFlzcrXZbuF5BeXeGnmKPvjZMqpXIOcYNk9jZyp3KLJ-NudEogjRHhgpVbrobbXL2Gn3aKRVbgkXzWiT47Dqbx7UhIAr2bBozXujQQmm__dkknMf1in5mVh6LX6C8kKMRWH23kgeH46unVg-SwdIcPNpQ5__pZSl6vKBnpoP4qZylcg3iC0QAutABq-Guwqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/638e170672.mp4?token=o6Rgj3yrWD1UXba66yH_D5ph0D9C5mOXuYl2aV2KBWRHb713N673Z0Splch9VVE-vd4h69ZSR-AojInoK6j7oKSphtMtkBqQOKwSXidE9xQZC2e4fj5TOeNvDcE5Tuausr66DUtX2I2V6t0CFCbW0uIFlzcrXZbuF5BeXeGnmKPvjZMqpXIOcYNk9jZyp3KLJ-NudEogjRHhgpVbrobbXL2Gn3aKRVbgkXzWiT47Dqbx7UhIAr2bBozXujQQmm__dkknMf1in5mVh6LX6C8kKMRWH23kgeH46unVg-SwdIcPNpQ5__pZSl6vKBnpoP4qZylcg3iC0QAutABq-Guwqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚠️
🎙
هادی چوپان: من حکومتی نیستم هنوز فکر میکنم دارم خواب می‌بینم؛ وطن‌پرستی دلیل حکومتی بودن نیست.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/107249" target="_blank">📅 16:55 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107248">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=u6GSNZxJV0FBEkXbdrWrOo0diARNdIrd7RE-m8FGsM3barXQABhTAIqO11y7xgnO8GSt2OMfNl2pLbhYQPHUeAm0Qg-Wtio2apMrHPP-Bp9s-ILFYmchMKc-5IlZfmuNvoB-XXZ7eMPnXi4IqpkE-zOdQRADah8dSXieohKQE3tvOoY0F9l0OBPvh5Pdot4GLVIW66b5xfST4KIsos0d7UGoi_sH3v-rNNMD08cPv3kIaVC4igvPbBHWMsyxPk62MqrRq9Ilf69USZFmeWSoWriA-SQNGtUIsyeu5TshAN4ziLKSjGNRroW47AykJLSl57hE8YAJ3tox-0HFrC3eHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74e4e43dca.mp4?token=u6GSNZxJV0FBEkXbdrWrOo0diARNdIrd7RE-m8FGsM3barXQABhTAIqO11y7xgnO8GSt2OMfNl2pLbhYQPHUeAm0Qg-Wtio2apMrHPP-Bp9s-ILFYmchMKc-5IlZfmuNvoB-XXZ7eMPnXi4IqpkE-zOdQRADah8dSXieohKQE3tvOoY0F9l0OBPvh5Pdot4GLVIW66b5xfST4KIsos0d7UGoi_sH3v-rNNMD08cPv3kIaVC4igvPbBHWMsyxPk62MqrRq9Ilf69USZFmeWSoWriA-SQNGtUIsyeu5TshAN4ziLKSjGNRroW47AykJLSl57hE8YAJ3tox-0HFrC3eHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👀
🇪🇸
عادل فردوسی‌پور: کاش زلاتان ابراهیموویچ یه روزی برای تیم دیگو سیمئونه فوتبال بازی می‌کرد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/Futball180TV/107248" target="_blank">📅 16:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107247">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c917893c10.mp4?token=uwfjjEA3cOBmxuL-Vt4KGTnTJhoXDDftRTudOkf6wBmjSDKWNcWu65CFYmvL1Ql1-xwm1N-kTXCoVmlEY5R8PQ2mF0N-jEeQK3oZoV7Fn7UkvZdB-l34SX8mVAv0oLCkI4bdkHheLb8dDDZ4SqMjphOd1CQOSWv6GYS0imd5qjr6hYNgda5c7Te_IKwuFyklySYMnpd5HtsEE7XbDuGSGNjEQweFGZgqm64DuGTS95GOGLaqbZcYGzp3U5m199FDu3NBvi292OIFNcJaw0SusvTFAmNBMGoeqAVoqTuvQIjzte6w4JaJe1HTvKa0GicFswjo5mc8gYLMchjSdhLyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c917893c10.mp4?token=uwfjjEA3cOBmxuL-Vt4KGTnTJhoXDDftRTudOkf6wBmjSDKWNcWu65CFYmvL1Ql1-xwm1N-kTXCoVmlEY5R8PQ2mF0N-jEeQK3oZoV7Fn7UkvZdB-l34SX8mVAv0oLCkI4bdkHheLb8dDDZ4SqMjphOd1CQOSWv6GYS0imd5qjr6hYNgda5c7Te_IKwuFyklySYMnpd5HtsEE7XbDuGSGNjEQweFGZgqm64DuGTS95GOGLaqbZcYGzp3U5m199FDu3NBvi292OIFNcJaw0SusvTFAmNBMGoeqAVoqTuvQIjzte6w4JaJe1HTvKa0GicFswjo5mc8gYLMchjSdhLyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
🇪🇸
صحبت‌های شنیدنی رودری درباره تفاوت‌های اساسی فلیک‌ و پپ‌گواردیولا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/107247" target="_blank">📅 16:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107246">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=ivlbW-WsEf3JcC1u1bSlZxxzQ9iqpb1KCg7p3Q3PRIoz5hyMSsNSldP6VxoW7BEV5KcpkWfKV1MbWXgJuhFJKkcNTuT8KGzJzQcgAgAgfjhHlUh7oOkyytT-BgYddQ2bbG2vNFxEEP0bvmN9kXf9hmunK5Cyk7NPr71Wo9x5dW8yEDS-G3aCofkf5jI00F0es2_zvBFg_XKrYqmP5mORfQ1mantd4dHkLpNFQzbm-ytc8w5KlUB333HhKbzxuywr63hB-uyThkFk3uIcwvJvMXFlxEYRDNKa0LSav6wor0Bl2DNa_sCcOeWprIFyoC2A0apx3YeD9CmzU49emT993w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a6854f7f8.mp4?token=ivlbW-WsEf3JcC1u1bSlZxxzQ9iqpb1KCg7p3Q3PRIoz5hyMSsNSldP6VxoW7BEV5KcpkWfKV1MbWXgJuhFJKkcNTuT8KGzJzQcgAgAgfjhHlUh7oOkyytT-BgYddQ2bbG2vNFxEEP0bvmN9kXf9hmunK5Cyk7NPr71Wo9x5dW8yEDS-G3aCofkf5jI00F0es2_zvBFg_XKrYqmP5mORfQ1mantd4dHkLpNFQzbm-ytc8w5KlUB333HhKbzxuywr63hB-uyThkFk3uIcwvJvMXFlxEYRDNKa0LSav6wor0Bl2DNa_sCcOeWprIFyoC2A0apx3YeD9CmzU49emT993w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو آندره‌اونانا گلر ترابوزان‌اسپور از روزهای خودش در فیفادی؛ معلوم نیست چه غلطی‌میکنه
🥸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/Futball180TV/107246" target="_blank">📅 15:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107245">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=h1InUWFNykoNPie36IiYqNgoOnJ1pKpJtEiFK4GXsqXpJV1SsL9efDo6jYY_3Z0sqiLaQQVkYekvLOe-dB3-xUW6fL5yjpk0kHZdYd19s_RH_zqcAbingn1e7AjYiXM5GTrcU24AlCVMnP7N389pkPchke77Vcb77MhcZVHxkXlLACRo6jIo1MssEWsZiWUy87GqJb0zRUYkshjUnJd3RmdyjHvX9rQR2Uvb_KmH66GzGFdiOvqA9yRH9MShhAvfmzYKG6KXF1B8PrLmad-dwRLjTC5Vk7FFRqPtD02bCh3WQ2ZRPpEZQ2qDRG_ujIpKWZqTmk1a_AlMs9eHuEdVzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d52babf07.mp4?token=h1InUWFNykoNPie36IiYqNgoOnJ1pKpJtEiFK4GXsqXpJV1SsL9efDo6jYY_3Z0sqiLaQQVkYekvLOe-dB3-xUW6fL5yjpk0kHZdYd19s_RH_zqcAbingn1e7AjYiXM5GTrcU24AlCVMnP7N389pkPchke77Vcb77MhcZVHxkXlLACRo6jIo1MssEWsZiWUy87GqJb0zRUYkshjUnJd3RmdyjHvX9rQR2Uvb_KmH66GzGFdiOvqA9yRH9MShhAvfmzYKG6KXF1B8PrLmad-dwRLjTC5Vk7FFRqPtD02bCh3WQ2ZRPpEZQ2qDRG_ujIpKWZqTmk1a_AlMs9eHuEdVzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
گل‌خوشکل سون‌هیونگ‌مین مقابل اکوادور که تنها با یک‌گل دیگر به بهترین گلزن تاریخ کره تبدیل میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/Futball180TV/107245" target="_blank">📅 15:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107244">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=ea02kPz5rRkXNBnBx9MW97Eu4BvJjISJ6NtNQxag3O6rj5jDrJZqxq8R6drxXNfFxUm-OT6-9PEcNouy4I5aQwA7IG8X3PT9i_FAFt1Vi_u1qIqCuF2NoA6hKS7mJcU5gSOcjKVwc7LZaON4Z4bLShkFSS9Iw2T5nWIQFBlFDJ1hjHSYtwGj8WBP8Pe8MGs0Z5EaVi1vcJEzQTNi7mQulo1waducG7w9ZwkFwecj3adKkFTgpuHl3IW2fSG-EwSXDDxwX7VKJ_5rbrpwwBAe6I7swcnFrpdkf1eP06ii8GjUBrHl8y3PRKuDpzEmC9xJ9c8CzweBHkwqCKjNRObnak1avvG5buz7A0ewLyIXWfQreKXGkeJWh4fM1QN0pnM1pbCqCc22eG4-ynqfAoJPbj2cKYz_4pxPFFNFYmXk_RirJnuIsi6xrju8D-y2_GzNrG_ih6Mz3cOGsg-kxMSH_VFF7sY7ry8HJkC-MnFgGdlYNFjWfwAI26ki-9A0teNv7YcKlVFJTxDBXFA3hvIzeLCevi1K-HKU2eFYtbnMDCr5aCtBRAmjwJxcTtiO_iimNnJ1rqly5QkauootknX0EIVYmVDnhMj9CNvc0U8LfNVV32ZYZSpZ-faQuApGrFWP-RgswmuqEJgoZqZPPqzq1aXoMJ3Bz-7_jvhOxc2dZBM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22947aa27d.mp4?token=ea02kPz5rRkXNBnBx9MW97Eu4BvJjISJ6NtNQxag3O6rj5jDrJZqxq8R6drxXNfFxUm-OT6-9PEcNouy4I5aQwA7IG8X3PT9i_FAFt1Vi_u1qIqCuF2NoA6hKS7mJcU5gSOcjKVwc7LZaON4Z4bLShkFSS9Iw2T5nWIQFBlFDJ1hjHSYtwGj8WBP8Pe8MGs0Z5EaVi1vcJEzQTNi7mQulo1waducG7w9ZwkFwecj3adKkFTgpuHl3IW2fSG-EwSXDDxwX7VKJ_5rbrpwwBAe6I7swcnFrpdkf1eP06ii8GjUBrHl8y3PRKuDpzEmC9xJ9c8CzweBHkwqCKjNRObnak1avvG5buz7A0ewLyIXWfQreKXGkeJWh4fM1QN0pnM1pbCqCc22eG4-ynqfAoJPbj2cKYz_4pxPFFNFYmXk_RirJnuIsi6xrju8D-y2_GzNrG_ih6Mz3cOGsg-kxMSH_VFF7sY7ry8HJkC-MnFgGdlYNFjWfwAI26ki-9A0teNv7YcKlVFJTxDBXFA3hvIzeLCevi1K-HKU2eFYtbnMDCr5aCtBRAmjwJxcTtiO_iimNnJ1rqly5QkauootknX0EIVYmVDnhMj9CNvc0U8LfNVV32ZYZSpZ-faQuApGrFWP-RgswmuqEJgoZqZPPqzq1aXoMJ3Bz-7_jvhOxc2dZBM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🎙
صحبت‌های جنجالی هادی‌چوپان درباره جاویدنام مسعود ذات پرور: منو شیر شاه، سلطان و شاه خطاب میکرد! عکس منو از باشگاه ها پایین میکشن؛ ولی من بخیل نیستم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107244" target="_blank">📅 14:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107243">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947PlzHmdIzfdxZ6gj5QTlL7KLu6hcwvSSQ4OQXIhPcMltu-41MrNbDwzHrCuCDQMC6cCsKGjgX8Hn8ptdhLBWvDDEbtxeE6_nPXTS4WzC4gxS3DBTGre-nAJ4c6XdRbQGXCuSaPQ9EXw5kI54slQmE3c6GLt2r1olqdBDFQugEre7ZAHtNrcDrOlMQQYYHrM8P9gjEFYwvXMXjC5CpbX5UwxlgRgi7VzTb7GzPTCUiF2-yucRahK80bEnNZwEK5l0U35_xgl53TIr3gz7hHJtHU4OfMxkV-Q_4KpRA7QCLXPjGsgrbf24jPty1R4iKMwjGcamB95I-JT-yvCkKTr034" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e55638e04.mp4?token=vFdDOMgXbaZOlkKUB8k8oXb4dG6iD2S16CmWZY-aO3UzxpQYuvtQXuejgaMT8kumnzw7iLg_VOj4Ii3GvuHCyiaYkBxhw2zwJjryaXnTdQmYdoRHG3xyXygsOHrHlDliI4uVFSKG-D-6OWxS8bcdTNQ0VD1tzg52Q_8hMwNTUgDkMFcjVYvZ14NnUZfrqJtDZp3NczZqq-itRo2JldsqycVfeDZxeww340S4T88LEr6k5ChL6obgbgbsJHN_6ktGO8MXrhjKHDDAt4JD3t1eSsAC4iABOIjQ5vcDDj8nIxxWydmOorNwnWvDjooKFWb_r8IRbLhFd3c21YKVjWl947PlzHmdIzfdxZ6gj5QTlL7KLu6hcwvSSQ4OQXIhPcMltu-41MrNbDwzHrCuCDQMC6cCsKGjgX8Hn8ptdhLBWvDDEbtxeE6_nPXTS4WzC4gxS3DBTGre-nAJ4c6XdRbQGXCuSaPQ9EXw5kI54slQmE3c6GLt2r1olqdBDFQugEre7ZAHtNrcDrOlMQQYYHrM8P9gjEFYwvXMXjC5CpbX5UwxlgRgi7VzTb7GzPTCUiF2-yucRahK80bEnNZwEK5l0U35_xgl53TIr3gz7hHJtHU4OfMxkV-Q_4KpRA7QCLXPjGsgrbf24jPty1R4iKMwjGcamB95I-JT-yvCkKTr034" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
به‌مناسبت بازگشت زیدان به فرانسه یادی‌کنیم از این عملکرد تاریخی اسطوره مقابل برزیل در جام‌جهانی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107243" target="_blank">📅 14:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107242">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🎙
👍
احمدزاده سرمربی سابق ملوان از کمک‌های اسطوره احمدرضا عابدزاده می‌گوید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/107242" target="_blank">📅 14:02 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107241">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIetZCyyCaYc8E4uen1dMRUmRfluM17zUURQknpboeyV7r_uVFKfz5Ywk9KF-VotkaT34LE1nQGihfbPT1tIeBbDs-UDci5qWWHrBbHljYdX-rCw2Ks0-zla70GTgX7BzBN7hD553VgcPv5MtNLiA3XTI3NPLLu09vOvpJhTiqOmDu3oD6xBaaYiOBTLmvc2GO30q4XubsBYSK91u1YlfCtkxgeHokUu3aPuOj7vQr_MZ2OVDG88dgrCE-hMHN4G2h5C3ghtxx5ZrKfa7uHaCDUxKUqUbWMf2wof5x6YQbNQWqYXlZmt3z-JgK07P1_mHqwoEpxIXk4IR91jfcoJB_5ljI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f13d64d651.mp4?token=ZJdtoPHAGUqTV-dj7vMyaEFbC_QExjonk0S3W0g4_t_viXn88CrP47MtqaQV5Ey0mm0kOZsngseuV0Bc8J1A7gInndt9l1QZo4-caxOH14mYQ3Zr-OPnY04ASWDBRVX2Su33rG7FOkoqdnC6hWksa1zD6eZg_TAYOtG67J7A-WRBjo5ujuq7A3dBC2xSF6tCies7nfeVe8OYh5-qAZOVNboR8Wa7SdQqnlMT0G7n4MKvyAoZFO82ji3S7CfGM1kezEeVYXH63ftFU90OIOWRUSGx7h0OW13n4z_oVZVtudNaNBgIAfzkWiebQv5Ltj6Kur8Gl1J6Zt8SuJLD1MIetZCyyCaYc8E4uen1dMRUmRfluM17zUURQknpboeyV7r_uVFKfz5Ywk9KF-VotkaT34LE1nQGihfbPT1tIeBbDs-UDci5qWWHrBbHljYdX-rCw2Ks0-zla70GTgX7BzBN7hD553VgcPv5MtNLiA3XTI3NPLLu09vOvpJhTiqOmDu3oD6xBaaYiOBTLmvc2GO30q4XubsBYSK91u1YlfCtkxgeHokUu3aPuOj7vQr_MZ2OVDG88dgrCE-hMHN4G2h5C3ghtxx5ZrKfa7uHaCDUxKUqUbWMf2wof5x6YQbNQWqYXlZmt3z-JgK07P1_mHqwoEpxIXk4IR91jfcoJB_5ljI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
اولین‌گزارش نیما‌تاجیک پس از ترک صداوسیما و پیوستن به پلتفرم اینترنتی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107241" target="_blank">📅 13:35 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107240">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=akRmL5gF41ukOl5n71uphik_QwuQGYuj4jLq11ad8x4oPXUk7tExUJKX6RmaD18fmODRtaDnkXkZ4I8w1HyKd3-I9C1pp_LZx7kc9UOZEM8UcsRJnECEM6-mB8w3fUEOGofYd2NAz1AfOWzKZTuZPK13bjH11ooIGQRtm1TQUb2w_e-QQG0TgGJ3lRwiy3Rw_9GydgDJl9HA3q6hVgN_N2xcgp7T3X-dDIWpzz7ladTFLO70LVvWyly5jM2Z4wsL5AwC2ixa69aYLMk1EYJg-ARJtBwyxVmYCfs8BSmzOxbF60BgxpqY4A1qZYpLhiaH_jumj8_54cniLwXQ5-NqUQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c2e9fe0aa9.mp4?token=akRmL5gF41ukOl5n71uphik_QwuQGYuj4jLq11ad8x4oPXUk7tExUJKX6RmaD18fmODRtaDnkXkZ4I8w1HyKd3-I9C1pp_LZx7kc9UOZEM8UcsRJnECEM6-mB8w3fUEOGofYd2NAz1AfOWzKZTuZPK13bjH11ooIGQRtm1TQUb2w_e-QQG0TgGJ3lRwiy3Rw_9GydgDJl9HA3q6hVgN_N2xcgp7T3X-dDIWpzz7ladTFLO70LVvWyly5jM2Z4wsL5AwC2ixa69aYLMk1EYJg-ARJtBwyxVmYCfs8BSmzOxbF60BgxpqY4A1qZYpLhiaH_jumj8_54cniLwXQ5-NqUQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
🇮🇷
🇮🇷
رد رشوه میلیونی برای امتیاز دادن به استقلال
🔻
اتفاقات هفته آخر فصل ۸۱-۸۰ لیگ برتر؛ قهرمانی پرسپولیس بعد از شکست باورنکردنی استقلال به ملوانِ محمد احمدزاده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107240" target="_blank">📅 13:10 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107237">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WF8mm97NeRPGmqU17lvgKe0xW-29nhSwxhjyxihD2rj6Ik9nl06tjb8iaWEn1Amjd50a5dzvP02AoI4-SWyokXa0tyuDVc1L6ZO-8KVuKso4Jg1MCfqXm4shJMEFBji3RFo31XkfdDyIOQpyNFVXdLjqlu8AkCqrp0maXgv2lNP9PjxJk6HjoCAvyyR1Amyseqf_hEWepg7e-j0pfhvKwQkfGtX9jLamui6-kpAta3aKEdjJpKceJgR9zRxbCgjUVP3LCl_NBGp5Wot-J8wZ1e08pO2UMw4XeunM50Zv5q7a3TlxNTUHulk8AL0CqPDfQoHOdZYXbjo8R8Tk8_OMuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EH9_7LSPs_pToWXNAaZFrB5ze617QqlrQ9m9rb3TIyK-h-cAYpIzmvy8vhy96XxW4O6hQ7pahPu-6N3ayofjO8-p13jy4tPXFwIcQCZVfRNoL-hYXv16LwM5lppBaXipTvfkowOeVE56znn1lG1-4KdozVFo8tVMhjtWN51CivrmEtIQSbuout-Ct-OSVTF5T532aqn8W4u4oPFpgFaYZiJVaKkmt9M3MwO56QgEx1iSK2Ln0Xv1G5gY60jvwEvR_QuqcZM1g4-ISTqblVt-X82pQhmk2vSgYH6pEJv-h2dJALrTGuepgAN0Bi5PzBSXjftE8LB85v7qb8xCCsFNbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dWFQFfqo4ZWfZsjPr2SqoGEu9EJqOiU9YInzLDReGfJS4WyzRdeOcDxAvwbS7Y-gTj_ep4qlJ2FktqAK9EDmpXM2kWRfoTJfkYehRJrBHSNKtvpaccWqMBCFH395qjU_qCBmBRKvxZPZmdr1eFZ4WE2ihluBe3oljQX9BmoVLO3gLPgHiTXR6x3yclDx8L8nyg5YOY2ELabw4kN_L7mSW-yLlagVcKbcoroiR_ct2xKMygYnrdnE72rs2H_gLt8ASJLPw8OPiLhVlGsA7nreIO3owaFPVHAGYKvohcE9PgDsYxdhVyVpTrsg-Er6-bF9dTejljIbxUFt-EhAqLfPZw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
🐐
🇦🇷
تصاویر اسطوره لیونل‌مسی در آخرین جلسه عکاسی با تیم‌ملی آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/Futball180TV/107237" target="_blank">📅 12:45 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107236">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMay0YFVtrGoMQZ-ZLt2f4P1sKGQgZJMfHVqWLfklu65iuauvjtEHzNaoGbu-4_3Hs4hfniBeWvj2MjBBOAF1tS2TaUUEin6TEOCNzzDIqszJQen0Xjh6Y7TqcPrz8KnKJXdsNvyVaf83XAv186B-ilf6BvF4P6GyMYNSfe_LnMyghtQTjyl80o8SXyMOtJXPSydmpJTKlrsPRobcv-hll9KW_mVr4f90_MRYTPGIQ4flpccgELXDkojOcrDXyaH1OKavOJudUYUSpwy9B0p0ElCmg9sAkNXnbAxSjC0yfskPr1OzeWugtR_uKJYTrdCDHbfs8rocQu81fdBg9BIFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
ترکیب‌رسمی برزیل مقابل استرالیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107236" target="_blank">📅 12:39 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107235">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGtegCR1JTNvJd51mauzvDaCDD7RAXNm0h2zyHwp15COXEycexSfYsBLn59LTvQIXH0X0vaapvkOSB1kh37UvMKHVQk1TG0zb8DU5j9mA4z86HgAUF8sZIRJZmXsEUvOEgHMD9Lxhp6HG6DklVPZ1zaFDjGXtOXJwndVFDKDdv0-k4CwM3_5JVJKEz-spuLWasR2ZnPW_L69VhfmK8O9ZdhkYhxuqehVDaFm0jhAcyl3fzgL5TPnGMAbOqvVJkIl3-W-XLArDfDDvnqZU3POcmI_22Fyh6ZI3rQogIwbTOC0wb4sV9o2eseSbtpvjqLcJ_Qfqt1Bfg92wBaz6MSPPUhUkI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4d91b2fef.mp4?token=RQeB3KqSDDGgFF91NOGG5WbpGtyIZAn8hnDq9hyzkDtGUXAtDxtQIzTnjamPlY9pX42B1oWMzVjUZMj8ipeYGl8jlJls6LkYLX0hbpIGhCQNF0mU2fcK2aUNPBi2qtFsfyFQW5Fvcp5aankstMQ7ZPYrPjtyPDDZTHCxU1g173GTJ3DQADUuERuIXSFlb9wefqdgnOZYBsj4ot0TGAHisZW1E4aYHhnexTciAe9tkOiQtbghW-500Ao35_GGUQeb94BOpAKJsrgkfq4tukFxqPlp1ifPAOyUwH_BPslDwd6G-JnFfP9RRHnmXC5bDg7h9DgbpsoI9GqZb5WWdaGtegCR1JTNvJd51mauzvDaCDD7RAXNm0h2zyHwp15COXEycexSfYsBLn59LTvQIXH0X0vaapvkOSB1kh37UvMKHVQk1TG0zb8DU5j9mA4z86HgAUF8sZIRJZmXsEUvOEgHMD9Lxhp6HG6DklVPZ1zaFDjGXtOXJwndVFDKDdv0-k4CwM3_5JVJKEz-spuLWasR2ZnPW_L69VhfmK8O9ZdhkYhxuqehVDaFm0jhAcyl3fzgL5TPnGMAbOqvVJkIl3-W-XLArDfDDvnqZU3POcmI_22Fyh6ZI3rQogIwbTOC0wb4sV9o2eseSbtpvjqLcJ_Qfqt1Bfg92wBaz6MSPPUhUkI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
دلیل عدم دعوت مهدی قایدی به تیم ملی؛ ناراحتی قلعه نویی از عدم واکنش قایدی به صحبت‌های یک مجری در یک گفت و گوی تلویزیونی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/107235" target="_blank">📅 12:38 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107234">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=tDgf_bpJjl0SsJeaNUXj5wTEOG-A40QqiR-XRDmpFYN1Fv1vlL2vErbCfhKqQl3uR8YaPdDSotINDNjHWATxSMQKGmDSN680C53s2d4LuJDlJhdGNWfudODlHHcWg6iOea2Z1GvZFYyLTE2VZ8KY_XMZXD3NfTZJGGR2ZHJHlbjCnhbkhTG-aTxSuQxT9v95G1_yURDMYVxXZ_OI2kQDpKoZoF5MvohGyMpDCGk3EIDGGaIbvlFRAWfIT983cw2S2NCJeA4zqOfTYK1q6PlI3wt26Gjojdr3JFZmGWQ4sXPyTt9XSPmk-rvLqRThkpz1kAiSGVs0WjMmXBiagsAeTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f256fb52d3.mp4?token=tDgf_bpJjl0SsJeaNUXj5wTEOG-A40QqiR-XRDmpFYN1Fv1vlL2vErbCfhKqQl3uR8YaPdDSotINDNjHWATxSMQKGmDSN680C53s2d4LuJDlJhdGNWfudODlHHcWg6iOea2Z1GvZFYyLTE2VZ8KY_XMZXD3NfTZJGGR2ZHJHlbjCnhbkhTG-aTxSuQxT9v95G1_yURDMYVxXZ_OI2kQDpKoZoF5MvohGyMpDCGk3EIDGGaIbvlFRAWfIT983cw2S2NCJeA4zqOfTYK1q6PlI3wt26Gjojdr3JFZmGWQ4sXPyTt9XSPmk-rvLqRThkpz1kAiSGVs0WjMmXBiagsAeTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‼️
درگیری با عارف آقاسی و تهدید سامان فلاح؛ دلیل دعوت نشدن کنعانی‌زادگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/107234" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107233">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107233" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/107233" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107232">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/To6mk0TJwPzHyKm3MNeaaU88XnP2pKzG9dn5KCCMM-YwdMA5aDDpjMTrCjZ0ZrW4vgAqAy-2Zm-lzZv-XwGnTr6zjzWa0Wwi3mk5epHrswl1_8aljPytsHhJps20cMGGxvIpfZfIPfxS2WTdCnK6KAxwRfOTtjGDVPPT_fZpj0-Z8oxNRMKrFiKf1FnuHga7I3n7ZsgH62egMIWT6sqkZF7KTP1RD7OudtiyWg5BadnTn0ZvGtMgK5U59nsa_Fmtpl92cr4PnmTmsZNPfUA__zhLCfU8MPb52EEM1HgqApf6n22r3qqVoZUWLc7U4-gPQqtBwqksUtip2SbrRQWo3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
بلژیک
🆚
ایتالیا
فرانسه
🆚
ترکیه
برزیل
🆚
استرالیا
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
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/Futball180TV/107232" target="_blank">📅 12:37 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107231">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=qdqveDhSwYxyn8ShLBd9M-E5m0rHavZcKloZwVqVJEXYM49y7Jwa1WKCGsDXRCrv1nqg0DU_0RadT_4KNtB6QZ_Frzk8585TCQ6sNZWxbCMcImhBk3gLf7lJSn18kwrHWqSSpCmhmaQh09tLNp78HYaODb9ATDPZW2fCpJfmnVBdkY-1kdI1p6fgcMNcFro87HUpZBU9VMXZufz5lDrzlJm80ZE4BJ9wnNbdpB5oRQgrWjw4MvxfgjDa8qfHMEWOkMq4FaIJHH5Q7gLC6dqjeX0cBIQdbTdxKaEIN5yVlev-CQ_wPWKfhcVg-BuYZY8ofNFCv2q_WsdWt1zEpFJdEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e518e3928.mp4?token=qdqveDhSwYxyn8ShLBd9M-E5m0rHavZcKloZwVqVJEXYM49y7Jwa1WKCGsDXRCrv1nqg0DU_0RadT_4KNtB6QZ_Frzk8585TCQ6sNZWxbCMcImhBk3gLf7lJSn18kwrHWqSSpCmhmaQh09tLNp78HYaODb9ATDPZW2fCpJfmnVBdkY-1kdI1p6fgcMNcFro87HUpZBU9VMXZufz5lDrzlJm80ZE4BJ9wnNbdpB5oRQgrWjw4MvxfgjDa8qfHMEWOkMq4FaIJHH5Q7gLC6dqjeX0cBIQdbTdxKaEIN5yVlev-CQ_wPWKfhcVg-BuYZY8ofNFCv2q_WsdWt1zEpFJdEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
🟥
بازیکن تیم‌ملی اسرائیل دیشب بخاطر این شادی بعد گل مقابل اتریش با کارت قرمز اخراج شد!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/Futball180TV/107231" target="_blank">📅 12:14 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107230">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">❌
بهانه‌‌های عجیب حسین‌عبدی در بدو ورود به تهران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107230" target="_blank">📅 11:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107229">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=nFLSd8MFjB1G2dt9a8PyBXcAIxhgMwzUorKq570OjTkoxfYLGg72CVmLt6M9dS2DFQzCzHs5mCh8XxnllleCL7NdNxGsURLs5uIUD9pk1bSbopM4qMrGdP__S9ElbiyVGtyTTLzHJk2cjGLQKA2aXtViw0WyKPOPQupYqIfzJuVb6b6vGg_A4QU4ymtZVd3IoeUcSqkkUNFIWe4K4leHTjXmdTASRmNfRtcZrmu3CzzoDLGOLee3vHJ7yeF9NFAeeNUukI5k30Fkz5YYuiRSbnoqlSHg4o1J1shVB2IqLkG2VI7FzBdt49SCAZ_-AgwHMwPFovujAB0WDMtRTpXZMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e764af88a2.mp4?token=nFLSd8MFjB1G2dt9a8PyBXcAIxhgMwzUorKq570OjTkoxfYLGg72CVmLt6M9dS2DFQzCzHs5mCh8XxnllleCL7NdNxGsURLs5uIUD9pk1bSbopM4qMrGdP__S9ElbiyVGtyTTLzHJk2cjGLQKA2aXtViw0WyKPOPQupYqIfzJuVb6b6vGg_A4QU4ymtZVd3IoeUcSqkkUNFIWe4K4leHTjXmdTASRmNfRtcZrmu3CzzoDLGOLee3vHJ7yeF9NFAeeNUukI5k30Fkz5YYuiRSbnoqlSHg4o1J1shVB2IqLkG2VI7FzBdt49SCAZ_-AgwHMwPFovujAB0WDMtRTpXZMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💥
دیدار هانی رامبد پرافتخار ترین مربی بدنسازی دنیا با بهروز تابانی قهرمان سنگین وزن ایران حاضر در مسترالمپیا 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/107229" target="_blank">📅 11:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107228">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🎙
صحبت‌های شنیدنی محمد احمدزاده سرمربی سابق ملوان که این‌سال‌ها به شغل دیگری مشغول شده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107228" target="_blank">📅 11:05 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107227">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PQTy69f2B6IysheouyY8xGX77UNRuR3-HxTzWOSpkwg0z6vANl0VU6afJHcgqGfNFyallvPpF8-mNDD4xlXEvhS_lrg1cnPeMFcAo71eHy4eLjFjOSqnwJJLgIyG56CuBDa9ncYcEvyO0HJmLUbJHIgiPWWyOl-M_nb_p1Q5gdP8CTQq3KEQN4tNWJgInuEIXppzZHSieMGR1xALynEH9Qlw82uRggKej9ZmGqGEF2qRrPLuLXqceM72zhNGDeMtB_G9d6UalIpJf495WhyYFzj6xJQG3d4NY_ZHAf-riEuWAhLne0OGRSLBIu1zQaDs03tJ7iNZ4WoZML1RxleigA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عذرخواهی اسماعیل قلی‌زاده بازیکن تیم‌ملی امید و استقلال: از همه مردم عذرخواهی میکنم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107227" target="_blank">📅 10:59 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107226">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D9-CCF7fk3zIxIbEw_wqMSNf2PfcXk5jts7QRhc3tWrngvOry-NQXVvfIBz3xRn38zw5EnuO73nebNpCiWl_BwEITVbe0kiXQbx0pnSAf0JBu0mfahtBp-6jIQnQcM_7n-gZOha1kzQkZl-nUdLUDC8c61Yykh7_9mol4F0lEI-p5a7nk5LuhNjFrajTYRN9nnL8daKGrsUa3ngdSAcXQksEZpZBZJc7APYn2_y1LOfIWLBrDDk47Bso_q6FW2FvMWKfzsuoZ_Irz76iPYVTPnKEuQUf9it6gGM-hQhqAUwGEdl5UdGRC_y5zWXcjmLTYRnF3a-g4aIdL3sltOZyfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🎙
تیبو کورتوا: بدون شک من عملکرد بسیار بهتری از کاسیاس، نویر، بوفون و ... داشتم و خودم را از آنها بهتر و برتر میبینم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/107226" target="_blank">📅 10:40 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107225">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bbYQr0wUhHQPdNmo0dyFxF34s8LI59kej7EVeg-6GR9pcVWHEfNZV6wzap-fbVlhNf9z9ABfWcab7UcpY8Gx7bn53AnS1z56_xSz7MGHy_5fEbpxaClXa8avCJ3ZUg58zTgCi-gDNADKMJtJ_gdfx4cq4VVn0UF4I_gEM6wmbeNu6SrRBWxrQ3Ibnsev95xbZVcs8lN43H90PHSiccdyx4h1Ii_gSfDKKKuh-Yl7VYlYXJD7GLboKnbOUCMV1fAL8NMYpG-uOw96rK_OY4zbCpyPw_RLj7XZVdh7D7XGIJ5l4s5DFJ3CZiHJz9s5W3Cn1DNtcmqj8rdqnJ4Mdb3tqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
🇪🇸
رودری ستاره بارسلونا:
🔻
"من در حال کشف چیزهای جدید هستم. بازی با پاریس در ماه آینده، به همراه رئال مادرید در ال‌کلاسیکو، تجربیات جدیدی خواهند بود. احساساتی که قبلاً نداشته‌ام و مشتاقم به عنوان بازیکن بارسلونا آن‌ها را تجربه کنم. و اگر مجبور باشم یک بازی را انتخاب کنم که بیشترین اشتیاق را برای آن دارم، پاریس سان ژرمن را انتخاب می‌کنم، زیرا آن‌ها در حال حاضر بهترین تیم هستند."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107225" target="_blank">📅 10:15 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107224">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19143fc835.mp4?token=lkNvsCixUtOlBUFAAmjMQNc6L9FRCXPU1JdEmxYJreLjRR3-dCEmyvz0E7GV8teIBTR3cfJUJJMlD1qsNIvRc8DoeSmk440DmQMSoL0g2U5-NZEfKhcXy13y-BvQHLQE5kp6NT9Reoe-WhoYY4opb-ncJJA-hUrLEug-LBSJMf2QTlX0NfwRUPaKtpFfX0V_b1YzPFpTMZHR7d0C2jFtkXigEEN-bMV2cekpJzmQWHgynBIgayTPsxB6mjrBJ53sVKngSOHGiSj0dRwckEQGSvD3tjbqm6MY_F2uxEdT3sbrt572JHjybp1ezgXmG-JyDQz9Djk72LulPhCa4ZmcDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19143fc835.mp4?token=lkNvsCixUtOlBUFAAmjMQNc6L9FRCXPU1JdEmxYJreLjRR3-dCEmyvz0E7GV8teIBTR3cfJUJJMlD1qsNIvRc8DoeSmk440DmQMSoL0g2U5-NZEfKhcXy13y-BvQHLQE5kp6NT9Reoe-WhoYY4opb-ncJJA-hUrLEug-LBSJMf2QTlX0NfwRUPaKtpFfX0V_b1YzPFpTMZHR7d0C2jFtkXigEEN-bMV2cekpJzmQWHgynBIgayTPsxB6mjrBJ53sVKngSOHGiSj0dRwckEQGSvD3tjbqm6MY_F2uxEdT3sbrt572JHjybp1ezgXmG-JyDQz9Djk72LulPhCa4ZmcDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌صحبت‌های بامزه ابوطالب‌حسینی رو برای دوستان خرج‌نکنتون بفرستید
😆
😆
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107224" target="_blank">📅 09:50 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107223">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=MRjQERcZNdil07T3cAlEm6DlPLIWQGTRWkMfHXoIx1fhHBz7qeS2hWHL8TUwvjyi95teKq7oSU0QA5peESrcAgCPwG9QQ9GMcBtAjeaYegr3_Wm5AJifqt15z1MgnAM4Te_rLflI3GQtfNjKWSUAioPevhhUbS2GO6o3Ut08qVuMkYbhnlFaBWebK56PoCNi6IU1JgKKT3INu_-pqNf6MaY9_zcdiHtujHOkoYaCkJdjMUNxaMkBID0814f6zBA-0WNO4nJpQST3GvyCMX4ieuSIidB3hD3KJdgiLma8ADzwAyQ4PVQ6h6hyZnC8UMKNCi1Xm116_j_kTyqOAFrjBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/444d39e31d.mp4?token=MRjQERcZNdil07T3cAlEm6DlPLIWQGTRWkMfHXoIx1fhHBz7qeS2hWHL8TUwvjyi95teKq7oSU0QA5peESrcAgCPwG9QQ9GMcBtAjeaYegr3_Wm5AJifqt15z1MgnAM4Te_rLflI3GQtfNjKWSUAioPevhhUbS2GO6o3Ut08qVuMkYbhnlFaBWebK56PoCNi6IU1JgKKT3INu_-pqNf6MaY9_zcdiHtujHOkoYaCkJdjMUNxaMkBID0814f6zBA-0WNO4nJpQST3GvyCMX4ieuSIidB3hD3KJdgiLma8ADzwAyQ4PVQ6h6hyZnC8UMKNCi1Xm116_j_kTyqOAFrjBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
و بشنوید از زندگی سخت دیومانده
‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/Futball180TV/107223" target="_blank">📅 09:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107222">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=j1nZEQBLOEawjbLrTvgzvoCDXThwKaNlCQp8ZMV_r_Xcw6p_0BUqrseYTx4iTQzhLphe5fNsYrLpXa863ZxtwYCqveWATTfXeMshLw_-UfSKXOoWNroyJps5HE_wNRYGnCZO-TaX5CnL4SSPtX1SBgK_mSGiRlcToSmpjrYuI5A126Ty_s6Bgs_08dP2EuSKnAb-bMJb7s9ZYQ2VFBgzoSTON9j0tgnf3DlzCVcmNHARgPf8hMfM7W8ixQvp_Efu_arDOzPMR9vMNlUI9r9ZVyLdUomVUkxnpR2cMpBzoxikrvk7GPOP2BzXeiCbQQ0PUR09pOW6qO2k4ONI1iXp0wQLgwnxOyphaiBXkO29zq1F1onXvTNW7OT0zvO3Dsh3HffZCp1SbmmGOmdS9NPdlOAG5BUR3BkTfQm2HdtMaKeK7rE8LmkmwKtpb7URJ0oW_CHOLO9aDdpqpg2niOdAOCW-jxq5iZFpT5SVBJdlLQFLs-BNrBPzBf6R1I_uPPFZuzBOsn5zSPH6VIiQryeaKXvsruJjY7ni7rpt1PCQz7671Qhvyb1bIIq2LpEWQOgqljIwunfeDiS-8fYoxENdSINC7kEpkSGKSeDRC1Ukj5WnYYk1GVXdBLKWC1isWej8blkXOdcXy1KLW1gX0zab1PkAj6Pj4m5MWFeEx0yHIhs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/73d0f84bdc.mp4?token=j1nZEQBLOEawjbLrTvgzvoCDXThwKaNlCQp8ZMV_r_Xcw6p_0BUqrseYTx4iTQzhLphe5fNsYrLpXa863ZxtwYCqveWATTfXeMshLw_-UfSKXOoWNroyJps5HE_wNRYGnCZO-TaX5CnL4SSPtX1SBgK_mSGiRlcToSmpjrYuI5A126Ty_s6Bgs_08dP2EuSKnAb-bMJb7s9ZYQ2VFBgzoSTON9j0tgnf3DlzCVcmNHARgPf8hMfM7W8ixQvp_Efu_arDOzPMR9vMNlUI9r9ZVyLdUomVUkxnpR2cMpBzoxikrvk7GPOP2BzXeiCbQQ0PUR09pOW6qO2k4ONI1iXp0wQLgwnxOyphaiBXkO29zq1F1onXvTNW7OT0zvO3Dsh3HffZCp1SbmmGOmdS9NPdlOAG5BUR3BkTfQm2HdtMaKeK7rE8LmkmwKtpb7URJ0oW_CHOLO9aDdpqpg2niOdAOCW-jxq5iZFpT5SVBJdlLQFLs-BNrBPzBf6R1I_uPPFZuzBOsn5zSPH6VIiQryeaKXvsruJjY7ni7rpt1PCQz7671Qhvyb1bIIq2LpEWQOgqljIwunfeDiS-8fYoxENdSINC7kEpkSGKSeDRC1Ukj5WnYYk1GVXdBLKWC1isWej8blkXOdcXy1KLW1gX0zab1PkAj6Pj4m5MWFeEx0yHIhs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
❌
زیباترین ورزشگاه ایران، درست در کنار یک آرامستان؛ بررسی شرایط عجیب ورزشگاه تیم نیکاپارس چالوس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/107222" target="_blank">📅 09:01 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107221">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107221" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/Futball180TV/107221" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107220">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcwOHoP084WtLQNGUxFTgLFusH7DYtL722bags1aTQHyOPce-eXRWllEwAcHBpmsmAD_6yZelaYMeH98uw1zxIqCD8SWLheRTy0vNghVSUIHsgO6jB9Sp6wqxcJneUHf9TWmVe6qLut5BbMFXNiWZG4RqnCD4e_e-Fb5EoKXKVHOKrnxgnUDLz-UaR1OP9_WpFOW84w1VJDGVQIJh0ml_tLfU5wwnVFJ32bxIE74wGi8wzn8nylVdlpj5qugLT0XD2fGuKOMDQAlYTfAHx6FAE1KT9mZu3809lXk6neNp6eFKs7nNPTIeXt9Kk7fjJyCzx_5qQoDNo1_k7y0Ho2ssg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
با اولین واریز، بیشتر دریافت کن!  فقط در سایت جهانی
TrexBet
🦖
بسته خوش‌آمدگویی ویژه
TrexBet
تا ۱۰۰٪ بونوس واریز
🦖
تا ۱۵۰ چرخش رایگان در ۴ واریز اول
🥇
واریز اول:
۱۰۰٪ بونوس + ۳۰ چرخش رایگان
🥈
واریز دوم:
۵۰٪ بونوس + ۳۵ چرخش رایگان
🥉
واریز سوم:
۲۵٪ بونوس + ۴۰ چرخش رایگان
🏅
واریز چهارم:
۲۵٪ بونوس + ۴۵ چرخش رایگان
🦖
🦖
🦖
🦖
🦖
🦖
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107220" target="_blank">📅 01:25 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107219">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q4xRK0S6cBpcZg3a4ZPfXFMTREMruJCodSD2EiwGRkYJys2vfwP4PJOle8IkJMkSrAvQOhCe0zOgxSdxMuAifLo_vBThgZ-IU1YoZB1lg20Mc0AOzgJfneDWvnoqqmgMRrEWHH6V9LfLPc_Bmo3nK3BQ_V154sEdkDxeCYe1dfHwDKFpnD4kHoEA0iVJJlK1YZ3V9g4tbzQ9u7eo4lX4hXnNb7pD58BKR3GwFcC750wxVDSvcIdcn5YXLWK3cdvHDXnc3eZKeeAtO3_PMl6bRkQew_pwC1RJAlaX_TLFbx-LukdxP3fki8Boa-v488IRek_9ACOoVNf8wA3Ogk570w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
دین‌هویسن مدافع رئال‌مادرید: شکست مقابل اتلتیکو تقصیر من بود و بابت این موضوع متاسفم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107219" target="_blank">📅 01:09 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107218">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qthPkEl4AJQMzKg58H9gMACU35TmQcz3MBsfUSkNI2BP1xMHTpil6V4-seev26xk9ekOSspPnMu-b40lgljRiS8d39hd02megWAUMp5ENzdV7ZmCeO0D9xa7XOuHO18Ov7_a74_3w5ccModk-ie_zYiqZfO6GY0x3_Di_h1cXVuqPs-9coldk2awCgxI77K9i7CP0y3m0wwuF7fIhDlKiWS9frGNtk974_oiuRzsZzZ0CUh1zQwPUFttjr8oRv61htk-1ZjBKy8JbHdE53RAH5xzihd7CNGKbnXDdNNMPJ_ijEYbaAS8WSfYO9yUr4a-ySnpn6tz-4zWsUkk7co8lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🇮🇷
مبین‌دهقان بازیکن تیم‌ملی امید و الوحده امارات مورد توجه سهراب بختیاری‌زاده قرار دارد و در نیم‌فصل قرار است مذاکراتی برای جذب این بازیکن از سوی استقلال آغاز شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107218" target="_blank">📅 00:53 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107217">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=OSf_isdaL8lg7IgkCr5yf466uSs40DEmspsVgA7RwbJ-Z9njmNoYeOU6Xr35aAhZ9QgeTOdgYCGYblzQNGKgDiJypDrPBiZoz531rvgAe3xHI0aIZV9Xb7rgJpbilhB3VURfWbH5cCP8bf7jfOztU3OgUzjqMFTF19YW__GXdov9rmNFbB7Z1isVTUS_1ZysLo4EAVmQe4mF85hAsZMATzm9LJXtXT_582xwGgg_h36jaCmfMdw5N6WNVzee_BMUNAwaQa8O3fbmg0TpwJK00WW9PfdNrxR1lQlITZ6HEzHJ1AZPdryuRjjvaXp4dM3sefYnZ6q6XDiJs9e8ol4OoDHYBoI4YRXmQhVyt7Ujfw8W7UU1S7wCw9Rp0H785chCffhIQ8zrUWRhUVYrX0c3buZzQz8-f3Oi4dPz9DkYxWR_UlYiNzjVLEVmw3X_vv0KwyuqlGPtkbilzrR2Mn-Dn2Q9TEhhboy7Vln0qUGrugqvPyubkZ_o87H1dnmgeKdMXh0aTyHIAe61-WKJSh-EsFNqv8cqNpobMA2NLJZGSE3ThifEIQu1SqdHhfMzRtbbQgFkciVsRo64GgV6V6iQk5cI_WXjOdM_07HojNneM-8FIla6LH-KswN0AXzNi-AjampIswZr1tcnQNkey-EBBT2i3mxBfZ6QrdliVEEdgK0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c410e310.mp4?token=OSf_isdaL8lg7IgkCr5yf466uSs40DEmspsVgA7RwbJ-Z9njmNoYeOU6Xr35aAhZ9QgeTOdgYCGYblzQNGKgDiJypDrPBiZoz531rvgAe3xHI0aIZV9Xb7rgJpbilhB3VURfWbH5cCP8bf7jfOztU3OgUzjqMFTF19YW__GXdov9rmNFbB7Z1isVTUS_1ZysLo4EAVmQe4mF85hAsZMATzm9LJXtXT_582xwGgg_h36jaCmfMdw5N6WNVzee_BMUNAwaQa8O3fbmg0TpwJK00WW9PfdNrxR1lQlITZ6HEzHJ1AZPdryuRjjvaXp4dM3sefYnZ6q6XDiJs9e8ol4OoDHYBoI4YRXmQhVyt7Ujfw8W7UU1S7wCw9Rp0H785chCffhIQ8zrUWRhUVYrX0c3buZzQz8-f3Oi4dPz9DkYxWR_UlYiNzjVLEVmw3X_vv0KwyuqlGPtkbilzrR2Mn-Dn2Q9TEhhboy7Vln0qUGrugqvPyubkZ_o87H1dnmgeKdMXh0aTyHIAe61-WKJSh-EsFNqv8cqNpobMA2NLJZGSE3ThifEIQu1SqdHhfMzRtbbQgFkciVsRo64GgV6V6iQk5cI_WXjOdM_07HojNneM-8FIla6LH-KswN0AXzNi-AjampIswZr1tcnQNkey-EBBT2i3mxBfZ6QrdliVEEdgK0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بومیان استرالیایی این‌شکلی از بازیکنان برزیل استقبال کردن
👀
💥
🙂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/107217" target="_blank">📅 00:31 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107216">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uLkMVoht9j8wAsE34qYM3VzMONruXVUBkzS5_8gr_7nB2kZ-mwvsNysNpcilkXs5Dpe6T1NFs9MHHFcMrsrX7gotmsFPuo7wLriVaCUi65WRv4qkB3epFSFhqJIhX2BRBwSS8nSkMwKfIfREwnEBSybjI6hgGUZZFq31IO9uxCRUsCppzviCTlOpWCIWU3x42aKmL9bZSXhKX72HNvOegleJz7-PfdeDlgQlX6Vb-OCjSIJFg2BQurZl0IzwY4UhSjgYJDOsFcfXQ_TqFZjpmyWmCqco32swZU2T3da3pqII0NLLpz1r3GtoLbdwjLTyYdyR9GsB2P3m_wSRWKXf3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
نتایج‌بازی‌های امشب لیگ‌ملت‌های اروپا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/107216" target="_blank">📅 00:27 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107215">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/salvQVOmS9zN_rQipLQvUoJacpQvgDnkyVbiiqTqBRRsVTVVx3ITrJHGTu37T8JEjjbmJKdYZRKuQdv5rvifT_YPyjl71A0nR-n2hmkjsYlyDV4V2CLEBKKF0AP66vMtjT1chiHcL1_VJ4LtzhEirr9g3Rdtfn9R1IOwt3MmuIK0MtJXwG8Ricv9xJU1COll7GJ2Odr8pVt6AKSwIU_sE6Ieo2YfgDCbRg-4mHE__jRInbOAqmDp7OCOAHqxvBTi5MPikdpgrGW89xVCPUw_6GWxRobAhAmWw4b_CaV8AI-Dx6r0wSoLxaZBxrz2ja05G6e_wzLfMWszWvylQnOgSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107215" target="_blank">📅 00:24 · 03 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107214">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
⚠️
خداداد عزیزی: چرا همش با ازبکستان بازی میکنیم و میبازیم؟ با این تیم در جام ملت‌ها هیچی نمیشیم. بازیکن جوون هم که نداریم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/107214" target="_blank">📅 23:43 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107213">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KASq78VOYU8e81p2ejpeD-4ZC_-HRUYd-JluHyTat56W0VP7RT9pmLTxN0d0_x5aiMHKWOjWHDltmMq8c09aCiLR_ZjbucGrlRyaxNG2tgSXU7C6S-gq6FptSa2UCvfMns8Mbysg2c1YkSID3DbihW8tyOgC2J17_38g3Y2iAnqTwSTowWerTWjkg-pRnLd6pMpx21JNvrxVT_Jp-asJOrGAT5WN0g2Rh1O0-4vq_VpTmgkZeLG6SP2mhH_XXqzu7h9IcT-xSRL2zN_s5cSAyo1AxurNXFEoOKgwuWXs3nk4UJpEefovhdMrpbFg6fr-pjdYkhLL1m9Qt5sTl-1n4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رونالدووووو زدددددد</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107213" target="_blank">📅 23:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107212">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107212" target="_blank">📅 23:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107211">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YqMvbh7HwyhmXLL3jGV-fO-bBbA9UrjVBYPVNhwFLY3IxNawIqx_QBvs2A7r5ucyyZ9Zd1E7VSKIygti4HqK5vxHCZY1tGYEdEkH5hCtG5xKfwn7ie9Dg9E8gUBODQUhHIMxsOwqXg20XFE6q70txozkjbpz8XGlzt4PgFBQ7T7kaYaNJ4ZHpZ2yitZCOnJCeeyXc_LXOjdz3Cymyhp95fF4135GcIUfwK-QGAF0xzBfU2ersKeOgfZsttMd9Ah7YIf0Mu_MrTyyvL6TefyPwI0PzbiF9U4wEuN7sD4cHye593hqYz2ngxtOVK4zgqJwcBLEo2qdSXSFZiZdm0_kwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐐
🤕
اسطوره رونالدو امروز اینو گل نزد تا به روند درخشان‌ خودش ادامه بده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107211" target="_blank">📅 23:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107210">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XJUQtCsz5W3BBSA5zkl8nT-Djy2KLy6Ul4-Zeoc4QfIqQNJG7vy0mXaganTfEFgI8wgmKQCj18BXnfncM-oEvKs2yE4HyQppoFY9_alMvj73BNtBXEmAp6S5POkRhQFfIjpKvv08S83LwXlZIJ_45ohwj8wcv8sm2rebqi4dgaq5JDOWEqj_trvlWHoDRG7brDTlpvlNnC7zN1rk8Hs8jEBS7WSnI4Liu_gqQ46vHYkCnEEgRhgA46ZCJ6wy_dDJJCmQXmU7SGbVrj1vPicUo5hvSFtD6MWR6N5k9GCy6jYMJvnRYg0yEjSpnYIYXd15zA0tUX2XRcYJZoZKq0NBbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇺
🇳🇴
هالند اولین بازیکن تاریخ لیگ‌ملت‌های اروپا شد که به رکورد ۲۰ گل زده می‌رسد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/107210" target="_blank">📅 23:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107209">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZQDTlNSfHdprkMFg2MRySMBzJk2tOKeacFWSJYZiReaz8Ds9nMvO6jvOKPUHyUFEdJJphNKA9rPH20khwhgunXMLgUM53hPrEQXTpGNR0eUGnNhFNL_nPpoCyz1ANiVmPOfNMBR0CX2ro9y5Slk2WA5cMzs9Zs45CwejkzPB1YzEhEX9PNsSL7vFc14TLcs-Uzm12FYlPEuZDBuNzt5c61_ZOsp-yf5BTmVjt0ijglhubC3bOd4glny-XrxAU9kF-o31uroKlxdRbKrigdkGH0fGFDwKuTbWa4QggnaEz6XY0VDaGpq8wkDV85ItvHRZQATrRguxzJQS87v-pqjTc4A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a0f7b1f262.mp4?token=lmbARgmBz2U2VnhFYhG64wsqdM3iU-V9S7vwHP7Fldq2VbhP6j7-OsqIuqiC9YnTWeBB74xudBkPbdcnN7h7WGhfWsGu8g_HsnDPHnQH2b-tgYFWmnPP8wk4rbd8TROye90E0e_6aV5qP-yTet_TPrCQEeX6voNXAD6iYW7AYja37SQFRE0d7nBnZXzeahumkOpz2DSHZztKNPLUi5V3CsI8Rwg-YTrn14njhzA6C0VZ9ihQb9SxTNa_69z6TSrQJ3QmdOgEV0CZCBaC7aR1U3EymeALlEbVG1IP3mBBum9gJ6zMGmG4kMC9eh7OE6CMCMoR4bwcsc-K4oxp7O-TZQDTlNSfHdprkMFg2MRySMBzJk2tOKeacFWSJYZiReaz8Ds9nMvO6jvOKPUHyUFEdJJphNKA9rPH20khwhgunXMLgUM53hPrEQXTpGNR0eUGnNhFNL_nPpoCyz1ANiVmPOfNMBR0CX2ro9y5Slk2WA5cMzs9Zs45CwejkzPB1YzEhEX9PNsSL7vFc14TLcs-Uzm12FYlPEuZDBuNzt5c61_ZOsp-yf5BTmVjt0ijglhubC3bOd4glny-XrxAU9kF-o31uroKlxdRbKrigdkGH0fGFDwKuTbWa4QggnaEz6XY0VDaGpq8wkDV85ItvHRZQATrRguxzJQS87v-pqjTc4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل‌اول آلمان به هلند توسط انمچا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/107209" target="_blank">📅 22:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107208">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=M6AwpXofjSNp4PvHVwnAa9daKflu9YBJ35hPrq4dilKeKI5wdH4l-BMTLRBytbESrgHr3aLNI2F4vZl5ia9TboY6jSCjumgfo9AzP_t08_gp9ctYFHk77nRXHTXxssyHx8lTJlG6Q6hwURTifPTwEiPmmBaFurXQalcmAVGyZkIcSS7ZAQOYSzTRZhXGiPO0qp6kjip1s-ZddAgaS0CBwIsqXfx33wgxB1Od6u3cpWuGqgrLAlN0si-UEb7OunbabTQ_ZwgCNVZhHYiH_qBns6FxttLL-YZRK2YsA-MNntQkryGkTdfJX44SsWOA7UhsV3qZEy_7xEeoOmEbwqEfqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf1a30387c.mp4?token=M6AwpXofjSNp4PvHVwnAa9daKflu9YBJ35hPrq4dilKeKI5wdH4l-BMTLRBytbESrgHr3aLNI2F4vZl5ia9TboY6jSCjumgfo9AzP_t08_gp9ctYFHk77nRXHTXxssyHx8lTJlG6Q6hwURTifPTwEiPmmBaFurXQalcmAVGyZkIcSS7ZAQOYSzTRZhXGiPO0qp6kjip1s-ZddAgaS0CBwIsqXfx33wgxB1Od6u3cpWuGqgrLAlN0si-UEb7OunbabTQ_ZwgCNVZhHYiH_qBns6FxttLL-YZRK2YsA-MNntQkryGkTdfJX44SsWOA7UhsV3qZEy_7xEeoOmEbwqEfqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نتانیاهو وسط سخنرانیش یه دفعه پیجر درآورد و گفت اینارو یادتونه؟
اگه یادتون نیست، حزب‌الله خوب یادشه، چون ما با اینا، منفجرشون کردیم.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/107208" target="_blank">📅 22:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107207">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305c017139.mp4?token=vKX7rWyXft2zEjkQLsgvzj5wpnadvL0JmgReAKqGM1u1JJ1gadioXiloCNK2lj34kW6xLxblNONd5dk9AU5GeCSbhTnQLe1v_RztsHioief1urk92dVGNJrdHYl4UEq1cb1Vt5AupTbJwGHMC9KdqGTb6R08K5DCVdFEJfld6LoUqHJkYvL-_xIDxK84goTfANFN0DBcC6Dfouti4iLBH8t1hUXNZalpXiWK6J91D-j3xnCHTNq8P0nKTpj0Iau0fWBG6jteJW-4qTSaRzpohMDSA_MMzovsJWyZkCejaDHBi9KxexQoHZyGr3PLeN3Bg9oWXvME7-18EloZILSX8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305c017139.mp4?token=vKX7rWyXft2zEjkQLsgvzj5wpnadvL0JmgReAKqGM1u1JJ1gadioXiloCNK2lj34kW6xLxblNONd5dk9AU5GeCSbhTnQLe1v_RztsHioief1urk92dVGNJrdHYl4UEq1cb1Vt5AupTbJwGHMC9KdqGTb6R08K5DCVdFEJfld6LoUqHJkYvL-_xIDxK84goTfANFN0DBcC6Dfouti4iLBH8t1hUXNZalpXiWK6J91D-j3xnCHTNq8P0nKTpj0Iau0fWBG6jteJW-4qTSaRzpohMDSA_MMzovsJWyZkCejaDHBi9KxexQoHZyGr3PLeN3Bg9oWXvME7-18EloZILSX8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
نابود کردن تأسیسات هسته‌ای ایران
کار دشواری بود؛ واقعاً بسیار دشوار بود.
اما برای من، این یکی از
آسان‌ترین تصمیم‌هایی بود که در دوران نخست‌وزیری‌ام
گرفتم؛ چون اگر این کار را انجام نمی‌دادیم،
همه ما کشته می‌شدیم!
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/107207" target="_blank">📅 21:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107206">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22263541ab.mp4?token=H93NTyKI9Zexz91eOBVD9l73jq5sa1ycIIkpr_9nsk_8Nd8CNYw5c_OBs-GK1ZllfO_VfFtCRjlrt9HytBBLFa4KT6N6Zz7TGXmqTRlYYzzoRLagB1Y8e_tOebw_bvfuPHZ9mW3yPNXuV95ZnpZ0mB4jbkAc3n88NtFPdJ6p93R1WS_3Jm7ZDtaDb6AJZL0IYFtHpzbAkUyqHBMarGYkLsRI_GWC6z-I58UmaGdop_ddN4Mv1aifMcRcjnqfJV35vOCSBA2WXXjTf2Y6kbhqAgSnGOWFDUSpZBLKjRL-csfvMV-2peyza4VI0JRZnySDlJ5rkGZLEKnsJvqR7PkrMJ0xSqSHE4FZhGyz0AbHJTb6ueJyDfLObrHBqoQJ2LBSvF1tg4r7fSNivOFazcq0O76YoNueXJ_8j0-gPU9NfLex83b3kT7YK0ksmXjMUZqKCc6O6NUkOVVq7ZS0MBmRvU79M_11tBC7cENErEwDd2k2SMh6dHjwqD-Fav5RzJK36ze-RZUAG5UBX6tFPxTSoq-zfI2OX3bde44yRwvkoxuYdvDMin3wJ6MK7JCJPSDeHTkdm6mPwZAwp6uahoCiLOabYB_q6L9ea1-WKzYQAV6fzjTdmzCBYTHM9y34r_mJcScScprdycGsKqV1FFHmQrCx2Rg3G8fOGvYuJjzpRh8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22263541ab.mp4?token=H93NTyKI9Zexz91eOBVD9l73jq5sa1ycIIkpr_9nsk_8Nd8CNYw5c_OBs-GK1ZllfO_VfFtCRjlrt9HytBBLFa4KT6N6Zz7TGXmqTRlYYzzoRLagB1Y8e_tOebw_bvfuPHZ9mW3yPNXuV95ZnpZ0mB4jbkAc3n88NtFPdJ6p93R1WS_3Jm7ZDtaDb6AJZL0IYFtHpzbAkUyqHBMarGYkLsRI_GWC6z-I58UmaGdop_ddN4Mv1aifMcRcjnqfJV35vOCSBA2WXXjTf2Y6kbhqAgSnGOWFDUSpZBLKjRL-csfvMV-2peyza4VI0JRZnySDlJ5rkGZLEKnsJvqR7PkrMJ0xSqSHE4FZhGyz0AbHJTb6ueJyDfLObrHBqoQJ2LBSvF1tg4r7fSNivOFazcq0O76YoNueXJ_8j0-gPU9NfLex83b3kT7YK0ksmXjMUZqKCc6O6NUkOVVq7ZS0MBmRvU79M_11tBC7cENErEwDd2k2SMh6dHjwqD-Fav5RzJK36ze-RZUAG5UBX6tFPxTSoq-zfI2OX3bde44yRwvkoxuYdvDMin3wJ6MK7JCJPSDeHTkdm6mPwZAwp6uahoCiLOabYB_q6L9ea1-WKzYQAV6fzjTdmzCBYTHM9y34r_mJcScScprdycGsKqV1FFHmQrCx2Rg3G8fOGvYuJjzpRh8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بنیامین نتانیاهو، نخست‌وزیر اسرائیل:
«
۱۴ سال پیش
، روی همین تریبون ایستادم و یک
خط قرمز
ترسیم کردم. قول دادم مانع از دستیابی
حکومت ایران
به بمب‌های اتمی شوم؛ سلاح‌های هسته‌ای که برای نابودی اسرائیل هدف‌گذاری شده بودند و می‌توانستند
تمام جهان را تهدید کنند
.
ما دقیقاً همین کار را انجام دادیم.
این کار
بسیار دشوار بود.
»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/107206" target="_blank">📅 21:48 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107205">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=PO0LTqiUKADtFZg5aWAWHKU72k1ab44UkamnP7WezXqA5N6TvOfKfVNatLMLLBaDOJD1iQyC7Inhe9QFQec086BJrYr8yrgvqoReuXgkrybME0_zrYu7Y5FWMzzrMKPhrJbO1ECbiZOdePNieloVhP2NEkW8irSr0daOgesV1QMImpGoFxMubaegHYIee7arQEu93ooC4OZMpawgvUyzIBfK7ELjqoRjfwcRpGoz_NbZ8n9rQpSfHmAWwGfh0RA6xrtX0dGb6ZAkCae1p1uljYUCWd3S5n0NpYFq-GFUkHV_rwfS47TUDWnvEpbtJBr12gAiKTxNfV8KgQvxhUJsKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ca9f3311b.mp4?token=PO0LTqiUKADtFZg5aWAWHKU72k1ab44UkamnP7WezXqA5N6TvOfKfVNatLMLLBaDOJD1iQyC7Inhe9QFQec086BJrYr8yrgvqoReuXgkrybME0_zrYu7Y5FWMzzrMKPhrJbO1ECbiZOdePNieloVhP2NEkW8irSr0daOgesV1QMImpGoFxMubaegHYIee7arQEu93ooC4OZMpawgvUyzIBfK7ELjqoRjfwcRpGoz_NbZ8n9rQpSfHmAWwGfh0RA6xrtX0dGb6ZAkCae1p1uljYUCWd3S5n0NpYFq-GFUkHV_rwfS47TUDWnvEpbtJBr12gAiKTxNfV8KgQvxhUJsKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
سانسورهای تلویزیون که مغز رامبد جوان سوت کشید موقع گفتنش!
🎙
افشاگری باور نکردنی رامبد از سانسورهای صداوسیما: بعضی از افراد آنجا مریض جنسی هستند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107205" target="_blank">📅 21:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107204">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nWMClLLBVO0g3KKYnLYvxw0KVADRp5evwFdobo8EhjHMi1617tQYf1ppr_0c3fJ_V6v8VstQ68t4c3Nzry8AF61zEuH0LaWtKe3sFJjYREtbPh6hf3xtrC-7KTuOEQ8P5yV8MJOW_E0jrBXwC0rUwEYsiy15FBIB-gJWX-sq_Rdfqd99i7HutDuZccnDVdLLNSWEMriOsaqTw62e1XvM9P54dH-8xBQ3kKEZfF_RIdgk6Ku0grCb5-lCGfN0cYU6Ylms3u5uoOHSzlKgPn5JN6unV3pID039C5QpmRsCDY4RI0Es0r9RqClDjma68s7BtLyLvQc_obPgc4zKieZqnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
ترکیب هلند و آلمان/ ساعت 22:15
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107204" target="_blank">📅 21:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107203">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SFESeUKgHVAz5DJvTJXpP53UxVrs_awgYM2B9c9VLDdpzBTZk8RUQfpIe-jowYkkfsS80bAAbjBzaIrb-78xwx_ZltPXYaoQHAZD-RnfC2_kXva3WMKlFsK5OqRHux1wcDVkg9-mK9LXsxERuPK4xB4t7nRejcVAzjD9RyyHloMDYz3LphkHVmgXd0xTc3lJmMIhD0m4B7eFUMjqR8OfGSS_xMJRD5Inw9yJCZcNISc9ISEm2mG5NdtBTFSrCus9kIHcZ02BRMmGoZGVu9FsQuJrwTPpBTeq3SoHWNaTu8ytg2l-ts4LqITq4YC9bCe6VQrqp-yJ5AOPzuO5_87XbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
ترکیب تیم‌ملی پرتغال مقابل ولز با حضور رونالدو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/107203" target="_blank">📅 21:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107202">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=CBe-Rde2RZ6jqXMkW-JOV1ojR8YkmCvGbS72kAxH8DdbWK1KqgS_Re00yWtMyUeEvPs7HqOU_zUTwWrnw6vmtZokcy90NZO5rHDhTZ0xeHmpBCXI5dpmmJSp_yPVycRCETtLojrOOwTsscFewi3nYe61klC2D_50dA2QvNJSL5qOvSq1IEyJssC0CxfhcomSmg7trWwcPb936Ah-90WGGrkDN3QAVsteoGbIXS8UX9FFW8qLzB_nMgAkDWctgiDp6gq8EN6qPmcyD6tiriC20Vdrg06nWbT4Z0d1BohA-AKrYTEF_tLU2M__2P6g15XQ4m3njfPovLUDe40wSJ50sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6388e432cf.mp4?token=CBe-Rde2RZ6jqXMkW-JOV1ojR8YkmCvGbS72kAxH8DdbWK1KqgS_Re00yWtMyUeEvPs7HqOU_zUTwWrnw6vmtZokcy90NZO5rHDhTZ0xeHmpBCXI5dpmmJSp_yPVycRCETtLojrOOwTsscFewi3nYe61klC2D_50dA2QvNJSL5qOvSq1IEyJssC0CxfhcomSmg7trWwcPb936Ah-90WGGrkDN3QAVsteoGbIXS8UX9FFW8qLzB_nMgAkDWctgiDp6gq8EN6qPmcyD6tiriC20Vdrg06nWbT4Z0d1BohA-AKrYTEF_tLU2M__2P6g15XQ4m3njfPovLUDe40wSJ50sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
مجید جلالی: میلیون‌ها دلار خرج مربی خارجی شده اما برای ایرانی‌ها هزینه نکرده‌ایم به همین دلیل است که می‌گویم قلعه‌نویی از مورینیو بهتر است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107202" target="_blank">📅 20:46 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107201">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qxZsFXpjrm2bjneX9DUdQ2ZB51upT90uqDG-U16t6qDSEjxUb-pHVAEg_UVkzCqHlOGOY2jN255ud8coIuWeMY5HXVgLgyLTnaED4ck0da1DOFDUYp60b-BfrkUoCAr_TXc0e4oHee_aXMeK9Qta04wTiioQsNwGpcOIHfUYmYHx_s-F2hjz_YWaVwiVMtawKUG0jlwxbd25L9KeRdG1fKxJZUksxCyF0VneFWQLtUGi1WkV9P4_lavOwSskZ_hNVrx6_vKMI0HwoCURCRQWfyAmAtFr4vCHinWhOxV4698dWpwPVA1GLbfnckejp-fgYq9S7AnoQtvn9GWkjn4zBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔻
🇩🇪
اسکای اسپورت: بایرن مونیخ در حال بررسی امکان اقدام برای جذب دنی اولمو از بارسلونا در پنجره نقل‌وانتقالات ژانویه است.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/107201" target="_blank">📅 20:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107200">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=iiuz4RcYlrubUL0TyTiCozjvh3M8ZcCRPzsd9AWrg8Ka5ljb3A-wvVUKJ2ER1_oyscKPcVP3wKIe8uCiyMoPsKRiy2Jk7ct2o7H0-U_hTqS1ZuoFtj6xph_WcvGA2QA7sDawdVoV4XQECBqhsdJYZK4BUXt0qKrOfv23rIzw0k_l1BXL0aFhA1w5tmyIZ9OBXL46PvQbnSJIfL8S5lbSLPoTLmeucK3PkYnO6XSi_9Ct-9FTh4rvstowjTo7ItziWnc82dSHmEuyNMHvGT5CMoVQ4J7bo-X2BmnZ3T5qRxpfEtXDZXyGH7UEIBqsJWURqF7NLi4r4RyJU5u4RL87HKIWdiW3ahprItQTkZzZxfCRphS670TsqnWP0GiV0GObi0jk34av78XwdgSMliXae7SVpLpFHUbc_VapH-q_LbN0tcM9WJE1cTDlG52kCTKEgN1d8O2JMgg264AC3jsWM7krshsdfAdeHo0y8yVStn3NIE8QLi0lYV5DKRxSONHRNqlUDWbDCL3A2tKHwgnhnH8g_GFZc-fKXIS0D4yqUKZyqpQAK0h2wMQh6S2zo6oKWZhRY_rQdK3eWDp6ZGW3LPOS1EOrpniRbkj9ss29Kd6_IkifQyg2YARIqPt2JZ95Z6s9sYuqw0qRvPAPqCgGBgMS4q8S3pplbAlklNqm5eM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc376d50be.mp4?token=iiuz4RcYlrubUL0TyTiCozjvh3M8ZcCRPzsd9AWrg8Ka5ljb3A-wvVUKJ2ER1_oyscKPcVP3wKIe8uCiyMoPsKRiy2Jk7ct2o7H0-U_hTqS1ZuoFtj6xph_WcvGA2QA7sDawdVoV4XQECBqhsdJYZK4BUXt0qKrOfv23rIzw0k_l1BXL0aFhA1w5tmyIZ9OBXL46PvQbnSJIfL8S5lbSLPoTLmeucK3PkYnO6XSi_9Ct-9FTh4rvstowjTo7ItziWnc82dSHmEuyNMHvGT5CMoVQ4J7bo-X2BmnZ3T5qRxpfEtXDZXyGH7UEIBqsJWURqF7NLi4r4RyJU5u4RL87HKIWdiW3ahprItQTkZzZxfCRphS670TsqnWP0GiV0GObi0jk34av78XwdgSMliXae7SVpLpFHUbc_VapH-q_LbN0tcM9WJE1cTDlG52kCTKEgN1d8O2JMgg264AC3jsWM7krshsdfAdeHo0y8yVStn3NIE8QLi0lYV5DKRxSONHRNqlUDWbDCL3A2tKHwgnhnH8g_GFZc-fKXIS0D4yqUKZyqpQAK0h2wMQh6S2zo6oKWZhRY_rQdK3eWDp6ZGW3LPOS1EOrpniRbkj9ss29Kd6_IkifQyg2YARIqPt2JZ95Z6s9sYuqw0qRvPAPqCgGBgMS4q8S3pplbAlklNqm5eM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
خیابانی: تیم‌ملی با امیر قلعه‌نویی تا دلتان بخواهد به تیم ازبکستان باخته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107200" target="_blank">📅 20:10 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107199">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=cRoyeluz41d7cp7_m1moZ0-Qnm9-yVBf2Efe9mrfqG8RyzXmYrRZGz3P4kb35voNBwe3vFZIlln-kaFe4N0WUchxzwG7Fg1cgB9zjGnYRlSpLzFjcWdixqVR4Ga8ZjuYUV4kYVSEB42Ny-3lXhH4XE9yZWe7ZVZyd1eObcGY2IRLlUEDLXqxEGNaVgEFy8afyDC6pWn30PLQHXZcybHpsf2VJaxssfNqr8HRIb4yhlpOt7Y3VmLNTL37l4LWtxBAZyZQb1K9heSAz9aXtGnrF-hQ0J64kGbk9CrGvVhGJfQpx0dr2YmInb5-ipuZ5iFn9lKTZCzft8WXPb-fv2vP2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89362fa6a8.mp4?token=cRoyeluz41d7cp7_m1moZ0-Qnm9-yVBf2Efe9mrfqG8RyzXmYrRZGz3P4kb35voNBwe3vFZIlln-kaFe4N0WUchxzwG7Fg1cgB9zjGnYRlSpLzFjcWdixqVR4Ga8ZjuYUV4kYVSEB42Ny-3lXhH4XE9yZWe7ZVZyd1eObcGY2IRLlUEDLXqxEGNaVgEFy8afyDC6pWn30PLQHXZcybHpsf2VJaxssfNqr8HRIb4yhlpOt7Y3VmLNTL37l4LWtxBAZyZQb1K9heSAz9aXtGnrF-hQ0J64kGbk9CrGvVhGJfQpx0dr2YmInb5-ipuZ5iFn9lKTZCzft8WXPb-fv2vP2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
انتقادات تند جواد خیایانی از بازیکنان تیم ملی امید
: برای کره نه مدل مو مهم بود نه قیافه. بازیکنان میلیاردی دو زار بازی نکردند!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107199" target="_blank">📅 19:53 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107198">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eWUBiZxEuntiDqCZ_uhSyRIF55YvgXGBqB7XaeeO4Rq8BuzyvJ_2EBrwcuDut_34H1iS0Fp2k5ebdDXZmIzm0wniT_ASxyeV01MNpQm10d3oukLtnbfJvBblgaDW4JcCBJkp6p4aje1WLlV2PrkOpsu095HU6l1t4wRp5rEE79WAXNrCznltcR72BQCB0xM2JNIpnS8k-7fokieBSE9zrRiptf7WCDDkWM114qqQWigZmVz0a11zoPSHwihJUuRkPYsYY72YDtYEMN266-VP5b5QvBEO-3dLtJ3JN9Ja47eFNbTVx3uaQTpHjI6BiRv2bAFGTdJ_WL126gACtlWFjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
🚑
رئال‌مادرید اعلام کرد که ابراهیم کوناته دچار مصدومیت شده و مدتی از میادین دور خواهد بود. به گزارش برخی منابع، این بازیکن به دیدار ۱۰ اکتبر مقابل ویارئال خواهد رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/Futball180TV/107198" target="_blank">📅 19:41 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107197">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=uaMWtcbaFVkX7f4w1yMBpzJ34vPTE6XppjvmIa-lYvtsWEp0jhO0djzYO-s_Bh225sKMUoOSCgiRGXDe6BQIrUgZ5kK-l1y7dUIg6xEfDdmRgJdt3G3G0QLO0abH_3roz72VjouwYzQDLnf7LQRer1XPOO53x7HyynR_lTionw1-HNJ2qx-Ct5H1bX09v7PHtG4i730KHXFaFyrwfCmS-ZbJuBEdQuv8joV6Gv8DNa7HRsoB8FkVnAHzpvaj9OYcSylT1vw0vsNlNdnTu41_VPYri0h6jwBBgBYEzPPgUV6cewHunSfJuu19QUnsLgn5t8zn5aK0WNFxq2kWIMEu7nGlr89QUbty37FnDHCfAJEAyWY1OKn6uiFKYeWwUZo3wJSuKc6Of3xEQQEpNgJn3G9lxXqWRL7iDw41UP1BXMeCk8-pIacmsHtUnkquKaVZH8zOchEp_-KZKcZ4TQcCDxrCkUPrWVJAAwKl6OyjkOHxMaGcPd4xI5n9Uw0IfVKlEJKdz7eihJIM8Bovm4qN1jMxCrT9gQ8MOAJSUW12fnzla7up9qGUs1um-riCdf6Wj0_JZW7sM4-upyKLhwqVf5upOZ_krCexmbqYiuF-z8R-Y_XgZ6uMX2ZSNdiyetsmv3GqNU558AJg2Djygl4kcx0n8j2JTyrU8KxVvOj2DDI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0cb36555e1.mp4?token=uaMWtcbaFVkX7f4w1yMBpzJ34vPTE6XppjvmIa-lYvtsWEp0jhO0djzYO-s_Bh225sKMUoOSCgiRGXDe6BQIrUgZ5kK-l1y7dUIg6xEfDdmRgJdt3G3G0QLO0abH_3roz72VjouwYzQDLnf7LQRer1XPOO53x7HyynR_lTionw1-HNJ2qx-Ct5H1bX09v7PHtG4i730KHXFaFyrwfCmS-ZbJuBEdQuv8joV6Gv8DNa7HRsoB8FkVnAHzpvaj9OYcSylT1vw0vsNlNdnTu41_VPYri0h6jwBBgBYEzPPgUV6cewHunSfJuu19QUnsLgn5t8zn5aK0WNFxq2kWIMEu7nGlr89QUbty37FnDHCfAJEAyWY1OKn6uiFKYeWwUZo3wJSuKc6Of3xEQQEpNgJn3G9lxXqWRL7iDw41UP1BXMeCk8-pIacmsHtUnkquKaVZH8zOchEp_-KZKcZ4TQcCDxrCkUPrWVJAAwKl6OyjkOHxMaGcPd4xI5n9Uw0IfVKlEJKdz7eihJIM8Bovm4qN1jMxCrT9gQ8MOAJSUW12fnzla7up9qGUs1um-riCdf6Wj0_JZW7sM4-upyKLhwqVf5upOZ_krCexmbqYiuF-z8R-Y_XgZ6uMX2ZSNdiyetsmv3GqNU558AJg2Djygl4kcx0n8j2JTyrU8KxVvOj2DDI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
حمله تند خیابانی به فدراسیون: باید چه کار کرد که کادرفنی تغییر کند؟ نتیجه افتضاحی برابر ازبکستان بود. آقای قلعه‌نویی نمی‌توانید تیم را جمع کنید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/Futball180TV/107197" target="_blank">📅 19:38 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107196">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cM9XwQqlWdNsM-MB6e6j4UVSdhyHh9Y8G3WbTAI8TLoOPLU3-8l1tSeFTdUeshNuARMkynUcDtSJp6aTM-bFEAyIjXrqXe-CDEFSS9iPx8AcxgqDf0vPwmPpSCc62c1O-irf9ju-AJ8qyp_uzO965Clj5pL1SW456izk21t5rLDjtHppcbOUj11yZgQo9HZvms-ze5VkOP-IDHWSvokduv--seQ2g2lZ10xC9KOUTLhSKbjP_6ulO8lrzhs9uK_gyxXw1zDBSBOvTvlfaVPb9nk1uPWQo5QNBMaLFWOh9iyxV0zElmfZaMKyBHt63wlrde0znlec9qV2o7erQyAbzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
پایان‌بازی دوستانه؛ به پیرمردها امیدی نداشته باشید؛ قلعه‌نویی با دستمزد ۱۵ میلیاردی پیش به سوی یک جام‌ملت‌های تاریخی می‌رود!
🇮🇷
ایران
1️⃣
-
3️⃣
ازبکستان
🇺🇿
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/107196" target="_blank">📅 19:35 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107195">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHcqYNkyGo-sB0gf2dp1zsNVAJTgRZmAihxYVY7d8YCv3aBZqNJ2glXQ1RRWFimvB7weHB0iJVQiEM7rtOuNW_-E2qdOFsQdx1AabrxyuXskRZC9VHcAgJizWUohGgNC9ZDCj9Lh5NBp5InXj9QrF1ZbMQ__2WzSn2QwfGN-HvKRICiaI74qJUziM3PN2TCPXYyJW3wNFAS183J5n5RHgPtUrTk2CiFwPG6mIYNGVyrz3_Y_G99TPmj0eNePcRYhCXFQAYZm-4_Bo7N3g0zg4e8aV8V0-U_eaIrAKtVrHIGgN9msPFe0FHB65kqxBjfBLSiN0AYsfULtPs6v8e-BDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107195" target="_blank">📅 19:28 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107194">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=VTKpt29s9bJnJLDDEExprwiR2esUuxQhdwroaxDKtADb3Dh0Azbgf8sWRMvuMDkmbyFqSokDB1L2AbO6xjxKmxis5_cTTS2JBTx7vjJHDPHyYkSpW2pVvqoIP8TWTFL-k5FcL-5EoA8naxzDGnQoJQwfh2K5YUlvjQSzKmOO8cyvInbBM_j2TmX9x2FA6P2HvakTJP3Z1gfKFfbFtvU1IcM5rHAoB-_VdyCwboibTJJhc5YhfzgJ0sg9WkWZatFXboJd3ATj73llTXx7rDnR_4voetQlXB7bJC71srxOVEERpDlsvGTyL7cAD4YfG8HoF1aykbYJ_r66nbW5b-YIVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c533284b0a.mp4?token=VTKpt29s9bJnJLDDEExprwiR2esUuxQhdwroaxDKtADb3Dh0Azbgf8sWRMvuMDkmbyFqSokDB1L2AbO6xjxKmxis5_cTTS2JBTx7vjJHDPHyYkSpW2pVvqoIP8TWTFL-k5FcL-5EoA8naxzDGnQoJQwfh2K5YUlvjQSzKmOO8cyvInbBM_j2TmX9x2FA6P2HvakTJP3Z1gfKFfbFtvU1IcM5rHAoB-_VdyCwboibTJJhc5YhfzgJ0sg9WkWZatFXboJd3ATj73llTXx7rDnR_4voetQlXB7bJC71srxOVEERpDlsvGTyL7cAD4YfG8HoF1aykbYJ_r66nbW5b-YIVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
گل سوم ازبکستان به ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107194" target="_blank">📅 19:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107193">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=M63IM0vwkLej_zignaMEyLmo2kI1Og-0BCYyz93keNMo-n1LVDEf5pn-Ci7ppknzWoau1R-89uWxaPXar7HtJnKNqW0nUiTpyW-jRIbffQZXXzwCtOF5Z5viKnswzYyb7pbANpGMlVjP4R92gICJZr5--fY5MK0kGw8ZNCBKH6YVa76zB2QNSTJutjcspzvlN6TY771tFF0dkcpteQh2P7aBTVOHhmECwfCUmunqR-wbzLIArFSoozZI_LAlB8imxf_EroCPomVoIyxd-ldrrypunR1Z_MEpvVpzbcL9B5Gh4E8Ugd_yv_kvzZzUVMM1eBoD76q2K2Ox-nHMbTSypA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5cf2bcda94.mp4?token=M63IM0vwkLej_zignaMEyLmo2kI1Og-0BCYyz93keNMo-n1LVDEf5pn-Ci7ppknzWoau1R-89uWxaPXar7HtJnKNqW0nUiTpyW-jRIbffQZXXzwCtOF5Z5viKnswzYyb7pbANpGMlVjP4R92gICJZr5--fY5MK0kGw8ZNCBKH6YVa76zB2QNSTJutjcspzvlN6TY771tFF0dkcpteQh2P7aBTVOHhmECwfCUmunqR-wbzLIArFSoozZI_LAlB8imxf_EroCPomVoIyxd-ldrrypunR1Z_MEpvVpzbcL9B5Gh4E8Ugd_yv_kvzZzUVMM1eBoD76q2K2Ox-nHMbTSypA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
گل‌دوم تیم‌ملی ازبکستان مقابل ایران
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/107193" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107192">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=O0a3EojUL7_zlRbVBm7BtVNNuzv9lklB8rITAe3_3L20xvVJwW47HB0UrBtV93FYYL4EISPKDJJpYaEASXBIS7ifuuzmo9O1v3V4lRVeUAa7HqCo8eJok4aCZMY_gVS7ZfoyiLsGd7qpYBKtOZCE0kBqq3B6BTAlPP8_GsLQo87iEgzC9p1kxYAF01v6wH95vAmTAXR3V_1mbBvRQh-bz7s6cAYeXIq7y30vRE_RnOb7tZ3mqfghbM5rjzr9ZC56iz3bPD8rgtQMhSvNGUBKn7AmbgjY1GeuhPDKBzDrSr1NYcpupZ6-W1j4ObbIr3JM6Fe9Y7tMj8WVnI0ULVenRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb2cea4974.mp4?token=O0a3EojUL7_zlRbVBm7BtVNNuzv9lklB8rITAe3_3L20xvVJwW47HB0UrBtV93FYYL4EISPKDJJpYaEASXBIS7ifuuzmo9O1v3V4lRVeUAa7HqCo8eJok4aCZMY_gVS7ZfoyiLsGd7qpYBKtOZCE0kBqq3B6BTAlPP8_GsLQo87iEgzC9p1kxYAF01v6wH95vAmTAXR3V_1mbBvRQh-bz7s6cAYeXIq7y30vRE_RnOb7tZ3mqfghbM5rjzr9ZC56iz3bPD8rgtQMhSvNGUBKn7AmbgjY1GeuhPDKBzDrSr1NYcpupZ6-W1j4ObbIr3JM6Fe9Y7tMj8WVnI0ULVenRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
لحظه اعلام پنالتی برای ازبکستان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107192" target="_blank">📅 18:49 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107191">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/592ed07452.mp4?token=WyICj5GuUvy0q53n-_rcorjLX-FLQUQ8uP6P_Zvxd0Puh4L2X6oDIMkQBmA6eaULz4UzfUiyC0KxA3AqUMSUwvXn5t2mfXREg5jkb-zoNwvs5k0izFzCuKHQN5BTHWr22K7Mzdd2czcmDrYG7u2fPr68X0i5NN16KDQH56visJnHs9GI0t-pT--jEbbelfWvnYoir4t8AQiyu-GHbInDkMsMMG3Xgd9ojT-ux8LWSpl8AbLqepfIX490mADWskePtegyOzuj3ZykYLAleeU9rbUACcge5aefYuPnjvFG5xm6JJpEx_tfv7u5FbmsIM8sFfiOdsiANnpQ2wt_zAyS4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/592ed07452.mp4?token=WyICj5GuUvy0q53n-_rcorjLX-FLQUQ8uP6P_Zvxd0Puh4L2X6oDIMkQBmA6eaULz4UzfUiyC0KxA3AqUMSUwvXn5t2mfXREg5jkb-zoNwvs5k0izFzCuKHQN5BTHWr22K7Mzdd2czcmDrYG7u2fPr68X0i5NN16KDQH56visJnHs9GI0t-pT--jEbbelfWvnYoir4t8AQiyu-GHbInDkMsMMG3Xgd9ojT-ux8LWSpl8AbLqepfIX490mADWskePtegyOzuj3ZykYLAleeU9rbUACcge5aefYuPnjvFG5xm6JJpEx_tfv7u5FbmsIM8sFfiOdsiANnpQ2wt_zAyS4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
گل اول ایران توسط رامین رضاییان(49)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/Futball180TV/107191" target="_blank">📅 18:42 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107190">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XBExPE3tjFB-CeqOpdAVZLJZqwYA8tozmCgJ8o-9uSXREwZyA2StFfz9QESEq7QOvG94vJHQU-el2W3oC80aYpaRrf1LqeaPznWpjjSuN-4dmpHja_-eaOpuLS4RfRX4EzVTEFKnU6aZvycknGCV6yZm3Zv1Lm1vF7dpud4A1AnWYCjgsJQLAl8833S_MB2AdD5ZZRcriBLoKug4NmExR8iq7rIW6hde6BMbOKDoABUkupowdqJy3zhnikFAYYmh1NaF_MMAwAJeEpjq4pleio1S6wpnaAdfrWohaeudK1YqEofqhlwP212x5Lt5fnaMo4Bm6RznbwWbqFcUkKsBPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا روز ششم مسابقات آسیایی ناگویا کشور چین تونسته ۱۳۰ تا مدال بگیره که ۸۰ تاش طلا بوده
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/Futball180TV/107190" target="_blank">📅 18:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107189">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXKO3DDsj21FKz-ddfnECUErxbcSHhoiW10Q6nxVidrNchWcy_ScX-sGsDkLT26A-chMBO43XSvbvBXgM140k6AwwlRDFLqm814LqgvoHpAoVC73VJkzmxIKHF-63l4dcttGRj9GOckhJPAHkWqscHUFimPh4d0l9MvSYNmiIodrZRdgfH8B6UQZs9iT48UBeogji_8kTiJemyP26POpkCFWxWI4nY-DgRfjw6Q9Ag2FxGjSwTgba2NSpGH_SjxPyCU2AMZndBH9sXFiEOFIsJq9Q7u8nvXSs8xwrmvwKXBwWbLfeEwiFA2B_9xpnFRB59dwtYBTAVLxPYeyJhv83A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
🙂
واکنش یوز ایرانی وقتی می‌بینه اسمش رو به این قرمزایی که تو زمین هستن لقب دادن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107189" target="_blank">📅 18:21 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107188">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q0Y7PzC_Swhgv31M3AMrg7owvj2OL_GK0UwVanYkuSx1ViRgf2oe-RBhpdFsnpe-i0E9FQAGKE3igLfihT0ggnzyd005CXE7kO5CLf4dgd2RSc_jNqFMaX7Cq8stWnqZNUpveDSEnid_Rh55WdDFXrckXAciaUkHo19KZUR3TkV9XB-HTzVi2kQh3fr5xqh9622w2lWP4RiYgyRl7BRKgZPL2ZmhmQi_lGz1HLQLDrIm7a0kPq41HQQVyIi2P3IVLGjafiLS1oY4zarKQOkjiGs5MppZXSZT_y9aRzQrZdBd1JZXipRwgFgLoGcVSrcClKEQgVLrln8otiCX34KZXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚠️
فلسطین برای ادای احترام به تیم قلعه‌نویی در دیداری دوستانه با نیوزیلند دو-دو مساوی کرد تا یاد و خاطره جام‌جهانی برای ایران زنده شود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107188" target="_blank">📅 18:17 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107187">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i25cscnarjpryqmub3jSw6kG4awEuHlEfqWiKTXyvIk55O4KqBnhigCVDoWGKBTxmiehUcc9VQO7-K_lRLb1Ubu6n1qhAtQupAfe4aBkIJx1V8Aa11dm3FUXN9hAd45MgctQoeYXfH-SzyU41LiM-V4-FbQJCtqz2x9AnP03UxtJzEXwEiYX4EBGAXTeqwJ4fuqmJ9yFUtCKcJJstthnVJnnKaIoqlq5012ZOlQ4DqQvQC-ujSfvBE4nvo1h633dZojdQ0L-q1GwdI0YLd9T7SR089w3PxbSBKxMCvg26P4IX9oFZzZ6NiyJZpB3WcLcqNG742_xdExB60hJbG7LRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
ترکیب احتمالی برزیل مقابل استرالیا که بالاخره احتمالا شاهد حضور اندریک خواهیم بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107187" target="_blank">📅 18:16 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107186">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TWbWO1QBq_IgtEuQZnzQwPJl4QkF1we7P-WzZYZ3e5T4tlo_z33Q4-bhZOoUMBy0LaCpSMY91PR5pMypWb2MJD2Re-P3mPWhnwrK0sFlGuRpPKdiF_8MKXaxsevUPApXyCWdKafU4veKBaxOmVGJuht_JuIYGSxtmRMGHVZxi7j3dMz6YeergyfBuP_8iM1f4F62Ki1SW2DH_Jas8hWYtt7942pLnUPYpeeb3BJ9jEz2SJrrkLOd32MR4EkPLwfqz9d2ISHFjfGDlm9UwLOinsmKlnHZAXo-iq2NLHxwaUouD4kJH9tI6wa7TvGVjtZTE4nxowU1is6_taTHePA5uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
لامین‌یامال: درحال‌حاضر در فوتبال اروپا هیچکس شبیه من فوتبال بازی نمی‌کنه و همین تمایز اصلی باعث میشه که خودم رو مستحق توپ‌طلا ببینم. البته لیونل‌مسی همواره در سطح فوق‌العاده‌ای بازی میکنه‌ و باید احترام زیادی براش گذاشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107186" target="_blank">📅 17:56 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107185">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=JsZdyoqPSpxU_IXjCW_P7v87KQM4pzbS9Rn6jwFniUXnWxR1nXI2E2dPOFb-D6kWGqIItH-HnK3kkVL5tzJfvehuxg09BVuhJTaNWONYk8M1-Ali9wWA9A2rlXQBRq3ERvUQvQaQY5wQrSd79sV465xWc-G5SlhQ_BpxBHc0NEK0vqyRKLyQyWoKfHVU5uwpRqn0_E1cxqJljkpGArk3q4ARaERX3Pb3T9vNRZN9lgvP5Q4yEQPxoM2FRnoS9vxYuVgZCBgqtXBhdubeSo4fGiXgvrpCUBJKiLdhR1nSf0_kP3Q6xpyTsyZn3JQ-XURYXiUTEJ7ZNtBe9zCjH9JfRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9718ff60b3.mp4?token=JsZdyoqPSpxU_IXjCW_P7v87KQM4pzbS9Rn6jwFniUXnWxR1nXI2E2dPOFb-D6kWGqIItH-HnK3kkVL5tzJfvehuxg09BVuhJTaNWONYk8M1-Ali9wWA9A2rlXQBRq3ERvUQvQaQY5wQrSd79sV465xWc-G5SlhQ_BpxBHc0NEK0vqyRKLyQyWoKfHVU5uwpRqn0_E1cxqJljkpGArk3q4ARaERX3Pb3T9vNRZN9lgvP5Q4yEQPxoM2FRnoS9vxYuVgZCBgqtXBhdubeSo4fGiXgvrpCUBJKiLdhR1nSf0_kP3Q6xpyTsyZn3JQ-XURYXiUTEJ7ZNtBe9zCjH9JfRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
اشتباه عجیب از حاج‌صفی؛
گل اول ازبکستان به ایران توسط شاه‌مرادف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/Futball180TV/107185" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107184">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107184" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107184" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107183">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zwhd6joav6Z9qCE3ZgKIJGgXED0TJ2vVosJADKyfuyOjjV4F6Gz8pXj8UubvEii3QzTvKFnC7ZKPoeLdJvEY_mWxC1QKqdXwcDkhkGUfbPYN9BCrDs5GDItBKOxXmpWbzn_Cc87xfRN1aWjs6oP8clx2SZVbAs2M12hAdkIY6qo4nmWZ91C3ggkamijTH2CHxy08OLklMG61VCv4LmQZUJ6GrFSCqhoih3-IWVEDrV1IoAXvjDoLwoP5UwDneEIJs3ftCaeWqGGH7tT10qfvlsgUadKtuEUwlzeXofV1RdEvD0_St3N5BRGwqhq4vIKcCkJ4R5jhfDuNYAoY2x_yXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز
ولز
🆚
پرتغال
را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ولز: ۱ برد، ۳ تساوی، ۱ شکست و ۱۱ گل زده
پرتغال: ۲ برد، ۲ تساوی، ۱ شکست و ۸ کل زده
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
🦖
هیجان بازی، وقتی بیشتره که انتخابت حساب‌شده باشه!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/Futball180TV/107183" target="_blank">📅 17:47 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107182">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rjBNFoy14M2aGBb9TBvICtE6WHrYnRvGxOz2e5O7K0uI7mFYW4Vq--Few_GXNa8QJYpNRtmjEwr0BqAn_ekSQtIwwPiLyVx6kWm6_17eMkpqlZkjsrFRalA7IKh_t0OXDAS3dIe-LBs0VYHGWHvI1beKBobnowld39Yu_i0PYmEh7jrYo0Uck53a_bgY8TSfJla7EleKY8XHcvYLEWk1balILttPI81mMaeRL-1X3CWL4_rVPnDs6y2A6hbrM7_QalW2FOLlfrbSBlCX45rdPNvDnl3Agq-p07X1cdYjoa8NHf1ZsvTTUun090693wKOhNaOKgxDcF4PEzLjPI7NdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
بازی دوستانه؛
ترکیب ایران مقابل ازبکستان
علیرضا بیرانوند، سامان فلاح، علی نعمتی، صالح حردانی، احسان حاج‌صفی، سعید عزت‌اللهی، امید نورافکن، محمدمهدی محبی، آریا یوسفی، مهدی طارمی و دنیس اکرت آینسا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107182" target="_blank">📅 17:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107181">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=mHAV4blLtMgy5It-4oyRejmdENlpgpqvc_dmenNGhRvnpijwWJyPIIdYBbQZp6aEU96mM-NMP1uC66nrvAIB-6_lpYNOiOIVzP5ZUgfGYgBPuN6-xxbGMaR-BLebvjidP6SiwPB5l2e6KlCt5NBexrEwD2tfXkPWwhoVoHUk0kncAfRg1RwZMr3SMMK4LtVLY2Yb3g75GHjsIVm2ZKImIngj2SKOiA0E9FsekoieIwFCujn8ky22GAtaJlNwo3p1gm7nquPL2HrWxY62hGOeXkCdJLx4RdDc8VO2X3dNY-gqMQFC8bpkg2OBX5xRLMrcV9xus7ty5970NUD-qsVMRg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6be9bc4836.mp4?token=mHAV4blLtMgy5It-4oyRejmdENlpgpqvc_dmenNGhRvnpijwWJyPIIdYBbQZp6aEU96mM-NMP1uC66nrvAIB-6_lpYNOiOIVzP5ZUgfGYgBPuN6-xxbGMaR-BLebvjidP6SiwPB5l2e6KlCt5NBexrEwD2tfXkPWwhoVoHUk0kncAfRg1RwZMr3SMMK4LtVLY2Yb3g75GHjsIVm2ZKImIngj2SKOiA0E9FsekoieIwFCujn8ky22GAtaJlNwo3p1gm7nquPL2HrWxY62hGOeXkCdJLx4RdDc8VO2X3dNY-gqMQFC8bpkg2OBX5xRLMrcV9xus7ty5970NUD-qsVMRg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
سوال‌کنایه‌آمیز خبرنگار ازبکستانی از قلعه‌نویی بابت عملکرد ایران در جام‌جهانی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107181" target="_blank">📅 16:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107180">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=N4gKDuQQle95PDJH1ppV0_bnWCFHR5zL5VnmoDJuQCrjcodhyMbIkIjyVeDvaI0bY0v8Uniy1JJCnjRC4yAEFuS7-uDjTHDQ_9PI0tgltPrMrTePlsWx4SkhL-ncdNj-qqkAKX8uDSHN5T3C7AsCQQRDECnnpn8Joh-5lPnmIlg99xdr4dR7IaRLNZwxU4Ze8g2r2CePxq-MhXCZNCjmh7prQJuaOqNbHGezTT8GwEkZXxHap_rYLbYutHhlPjmeLxbmAu6V0KCv8NuRRP49m4GW1qoUUVqrl-fOITYiuR6C79Wg9PjuTioxMeyBmeSVZLRzrq7BciiNA8Hu_IJrLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8a2786f81.mp4?token=N4gKDuQQle95PDJH1ppV0_bnWCFHR5zL5VnmoDJuQCrjcodhyMbIkIjyVeDvaI0bY0v8Uniy1JJCnjRC4yAEFuS7-uDjTHDQ_9PI0tgltPrMrTePlsWx4SkhL-ncdNj-qqkAKX8uDSHN5T3C7AsCQQRDECnnpn8Joh-5lPnmIlg99xdr4dR7IaRLNZwxU4Ze8g2r2CePxq-MhXCZNCjmh7prQJuaOqNbHGezTT8GwEkZXxHap_rYLbYutHhlPjmeLxbmAu6V0KCv8NuRRP49m4GW1qoUUVqrl-fOITYiuR6C79Wg9PjuTioxMeyBmeSVZLRzrq7BciiNA8Hu_IJrLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👏
🔥
🔥
صحنه‌جالب از بازی کبدی دیروز بانوان ایران مقابل هند که واقعا محشر بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/Futball180TV/107180" target="_blank">📅 15:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107179">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nz-cI0qKb3sEg6PzqpGHjyC8tIxfsRrflS-6fASlG6Ku5XxBC26GloOQZV38WrradTVVFarzrKxUJo9jK_PJ8ks_e-w8jmJhpGNAdBk_moWk4H7O9IWHzmoESH_4Gb5DqH6iIlU4_kalB8u-mrMQfPSX_xW_rtkQiTb7e-WMDetkkq2l-A6IQXFCBDMhep5o3_DMTnR3MQh7eIN1onh1aSmB3lmV0dQWiOrV96mfzITl_G9YnPI8rO_7a8aex1U8Nr6WCuseEPhkAhcmbJ_xeL9DT2nDf9EgUQVbdcBPKNuAsQy48BT5aGmHlEqxI0F4ikxLqqATqMz9jh1m1I89AQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
📱
استوری امیرحسین قیاسی درباره لیست جدید قلعه‌نویی و عدم دعوت از مهدی‌قایدی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107179" target="_blank">📅 15:29 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107178">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🌟
مروری کنیم بر ادن‌هازارد نسخه جام‌جهانی ۲۰۱۸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/107178" target="_blank">📅 15:15 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107177">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/773eb10873.mp4?token=kB2rv9r_QawDsrbGRbTNbo6DWcqYK7iU7JdHRYdfhNStah0d-OXTK64ZOrCaPOnc6abCJ6h9sJm6ymLgY36fnLz4qopkesfZhWcNfoWQS_N0wWqZxw-OZ7Ees9R4j0AU2byPDVYKhG14iqURQmNFZHhEUUSnGgytmi4PAk1lw_-e4nVNYQGtjbC9PmqBC_1n3gek1ClKuqJ8euW50Q6uya9Zo5kKSXk6VGd9sEbAAIBLz_wozfFGNeakw0DibsV6rs_pvUkB5-XITY3Udl6YccYWtf6DLUmrSyPk8Kwe_Q7aGJ48EUpMIYhrSE6b4J6GCgpz4OJO5lbbWOjnndSpWAWCNJ2Wf6ucbVvPo97xTTqfCQy2CXhXe2YZcLLyWE98Mvadlq_cvoX6M89KfCwxlNOuY0h3aJb4a1c-RaUZXjme2vW_CavIILFfbInhpVmrDuHKxfDoN7h2Pg9jrVM-uCDjroJUMk9umnb3_aZdO8enL29vaDu7S6aa4ptXlgl9KlLDW5nKq0ZNRD9ar40WylNXNhvR6_gctKb1fsMKHJH0TASNbwhfrylOk-NcULXA66-EzVv4qtht5Pld5WhPokplnOy8UTa4yI6ATJZIxp_1MjBj7u61yGx5oUx9KJTYEoZ-RhwIoqaraZguDvklgBgUm21Nbo7HPGsuyenchG8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/773eb10873.mp4?token=kB2rv9r_QawDsrbGRbTNbo6DWcqYK7iU7JdHRYdfhNStah0d-OXTK64ZOrCaPOnc6abCJ6h9sJm6ymLgY36fnLz4qopkesfZhWcNfoWQS_N0wWqZxw-OZ7Ees9R4j0AU2byPDVYKhG14iqURQmNFZHhEUUSnGgytmi4PAk1lw_-e4nVNYQGtjbC9PmqBC_1n3gek1ClKuqJ8euW50Q6uya9Zo5kKSXk6VGd9sEbAAIBLz_wozfFGNeakw0DibsV6rs_pvUkB5-XITY3Udl6YccYWtf6DLUmrSyPk8Kwe_Q7aGJ48EUpMIYhrSE6b4J6GCgpz4OJO5lbbWOjnndSpWAWCNJ2Wf6ucbVvPo97xTTqfCQy2CXhXe2YZcLLyWE98Mvadlq_cvoX6M89KfCwxlNOuY0h3aJb4a1c-RaUZXjme2vW_CavIILFfbInhpVmrDuHKxfDoN7h2Pg9jrVM-uCDjroJUMk9umnb3_aZdO8enL29vaDu7S6aa4ptXlgl9KlLDW5nKq0ZNRD9ar40WylNXNhvR6_gctKb1fsMKHJH0TASNbwhfrylOk-NcULXA66-EzVv4qtht5Pld5WhPokplnOy8UTa4yI6ATJZIxp_1MjBj7u61yGx5oUx9KJTYEoZ-RhwIoqaraZguDvklgBgUm21Nbo7HPGsuyenchG8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🎬
۵ پاس‌فوق‌العاده بیرون‌پا از لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107177" target="_blank">📅 14:50 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107176">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=bhku98c9QUGd3h0eKw2WDuvIzy7vFdFt2MShU-PIKyWjwu8XoDY12i9XTke6chaYcEc4uC_gGHpvM2TBPfANLNUXhH6PtAWklOaxBNtsYLPclkGQHDepkK8EyxnEdw46bKfkg1xD1uATSQ8Gvt0bPYom4k5LeJhEuFW3XWOjSTvoBdE4C36QPIJEiXR86LGsezzg6yoCHekmHBi4J_CqUqKPZvZMneibKdIK-n_Ao5aB3vDN_Z-xcbAU1ovz4zHRm3w_Amcl1_WI8hsIoVK_jIXXSIwZbCZebgpsCtX3MQtxu6asvRp2rt5y5fIycQhvqmokIwO8XZ1-BrCu2EFJQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e78c32e4ce.mp4?token=bhku98c9QUGd3h0eKw2WDuvIzy7vFdFt2MShU-PIKyWjwu8XoDY12i9XTke6chaYcEc4uC_gGHpvM2TBPfANLNUXhH6PtAWklOaxBNtsYLPclkGQHDepkK8EyxnEdw46bKfkg1xD1uATSQ8Gvt0bPYom4k5LeJhEuFW3XWOjSTvoBdE4C36QPIJEiXR86LGsezzg6yoCHekmHBi4J_CqUqKPZvZMneibKdIK-n_Ao5aB3vDN_Z-xcbAU1ovz4zHRm3w_Amcl1_WI8hsIoVK_jIXXSIwZbCZebgpsCtX3MQtxu6asvRp2rt5y5fIycQhvqmokIwO8XZ1-BrCu2EFJQYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🐐
جوری که دیروز ژسوس سرمربی پرتغال از اسطوره فوتبال کریس‌رونالدو تعریف کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/Futball180TV/107176" target="_blank">📅 14:25 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107175">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NEBzg-4FGec820r6kqD41IlpEoYXY2fh1Q0JTt64RvOVFIUbInKzX719DPk1Y3V7D2UICgiyL_V8v8WhR0LsSyIsIaixvDJeFwaMQ0YMav7pBnxgYY41kJQzBu3ZymPGzVsfaQtNHtVDLlHxUli1juG4x86LUkG3QIPkYsV4VOxsGuQ1u57uCcpLu-a4XbcdMZSv2SbvXq329mET0U_E3Nmu-0RfPEUT7wt0X2x1Vh8Nrjz7fK12HTNlvuDkCRMGtMrVKyu0mAez9JGX28IOPLh2WcSuZRkiJ8EAe6TsbvyG8MxVIIy_eLmys2Ooe6MvIdMd6J8KkrOcUwF9IuVmYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
✅
🤩
علیرضا فغانی از استرالیا و موعود بنیادی‌فر از ایران به عنوان داور در جام‌ملت‌های آسیا قضاوت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/107175" target="_blank">📅 14:06 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107174">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=RtegRsFjovZaeuLykBbibSkKVB_D8xLlayNYjfohbDqyMhZ3o3ISBvQ9wd_oSxnOwy294DAuV0dANIGOlDyjgiOGwdj5Aid7b0zaP6NKyj3Pvn07G24NchuERYrE2yXYrG1IFm4JtDVAjI-mMweYEXTRjZs9G-182YipdTlPCu2-WjbD4jxVReRQ6KSYMMydOJASxUE5jH7twe5ijTp4KLGcqxOlITpNVupZ5fETPtsF73IZfIxMygPmZOUhIlPJLipggyrTvFmeSWopQL1u3fWklVE9wEAOvELsD-orMGVSEleeJ4WaAxqR5ukPsrwRFmp2UOwC11uXfoSD1H7u7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7a03c344b.mp4?token=RtegRsFjovZaeuLykBbibSkKVB_D8xLlayNYjfohbDqyMhZ3o3ISBvQ9wd_oSxnOwy294DAuV0dANIGOlDyjgiOGwdj5Aid7b0zaP6NKyj3Pvn07G24NchuERYrE2yXYrG1IFm4JtDVAjI-mMweYEXTRjZs9G-182YipdTlPCu2-WjbD4jxVReRQ6KSYMMydOJASxUE5jH7twe5ijTp4KLGcqxOlITpNVupZ5fETPtsF73IZfIxMygPmZOUhIlPJLipggyrTvFmeSWopQL1u3fWklVE9wEAOvELsD-orMGVSEleeJ4WaAxqR5ukPsrwRFmp2UOwC11uXfoSD1H7u7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
شاید حق با پیمان یوسفی بوده باشه
❌
🎙
پیمان یوسفی پیش از شروع لیگ برتر در برنامه تلویزیونی خطاب به سخنگوی فدراسیون فوتبال: زمین و تماشاگر که ندارید، لیگ را پلی استیشنی برگزار کنید
🎮
دیروز: قهرمانی تاریخی پلی‌استیشن بازان ایران در آسیا و حذف تیم ملی امید از مرحله گروهی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/107174" target="_blank">📅 14:02 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107173">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=DEqkOh_FopcJkPoT8DnKSg41lgeZcIKYBYBqMM1gj_cl7PIGv33HtfmiFQdnNX_R5NIQnyOF3O0R1B7U9b_QoXZRZzF2AxxYnOREE6LEnXYCZVCBAfyoleUD43MpLaaK3hrkZElTAlTHa_WYjUtOR49fhPE0WQ-VQgiJMz173kn938AvYJmX2Y-lxJhDUCdXpJQsnUcMX3DEyMr9BZL5-F8FjxYHmTSOA69SFE7GuhGH2oTChLa-vh3PpDfEx--t1SOtMGt6mPMQ7--38UZVR78ExkNXnOqcTqXFWuINEvFqCCKvccKjqg2TYZ9vHF76ah_Hwqy0rkARYE20JXmFQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/383a3af1e5.mp4?token=DEqkOh_FopcJkPoT8DnKSg41lgeZcIKYBYBqMM1gj_cl7PIGv33HtfmiFQdnNX_R5NIQnyOF3O0R1B7U9b_QoXZRZzF2AxxYnOREE6LEnXYCZVCBAfyoleUD43MpLaaK3hrkZElTAlTHa_WYjUtOR49fhPE0WQ-VQgiJMz173kn938AvYJmX2Y-lxJhDUCdXpJQsnUcMX3DEyMr9BZL5-F8FjxYHmTSOA69SFE7GuhGH2oTChLa-vh3PpDfEx--t1SOtMGt6mPMQ7--38UZVR78ExkNXnOqcTqXFWuINEvFqCCKvccKjqg2TYZ9vHF76ah_Hwqy0rkARYE20JXmFQzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
صحبت های جنجالی هاشم بیگ زاده درباره ستارگان تیم امید ایران؛ از انتقال به پرسپولیس، ده میلیارد هم نصیب دانیال ایری نشده است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/107173" target="_blank">📅 13:33 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107172">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی  «پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/107172" target="_blank">📅 13:13 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107171">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=XQ62VFcwGi81xUWrgZFTt-uYRYW89tRsmt6Dw3McGvzhpMbUdTOPpDm-NeezlSK0v3dbirrFVXvU7T0qq2_gaaDQjHPJT9o62b4YxRgO3xIDjN-AsYxfO8wE6AnEJe3UxvE8JgI4xh6hBt7pXjrAqGrVPSQuIK9lNo2X49-UUHuowDj0LpMhX7EtfHa9k1aKEnJhgBqKAh8Nwi2eHgtVEFGU4eIOpg1ILHNI-Qx3vRvdDiOne3iyQPwXfR2TkwR8jy1PALeAb5mrCAvHtUXeF5pRuzk_2eiY0cEB_AnRjColUAZ__4LrK1MkgVQmiR0x9R-jVJcCKsm39zAvQYG2mZhyatxhngQO2DcYDUATcYENnKNhKO2H_8DAXcQ5xCBSTEc6449DbYYG3upK2LNzkraMNpORhkof0MALVns1sNd-dl2RXoN47rPotKyhHpN_jUz2j5_STDVx-FQ8FWJZUu9Ohd88t6tYqbmZrEzFXaXgMFszf2POst6ZxyDarBTMScoz1toOB_nb2-fvyn6xlr8LGfdv4I1BLDW6XUSwh8_YprXK6iQnnbnCH4wElqJeKXNGp7Z5MyNC8mqhqbMo53i73e4JQnjUkb0Q_8GXEoflwKRoSDCmHocR-nL-asDC6PVkF4O73ESXlERODdK-5DVB4pEGaHHspe8hBghISZo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5bd37ffa3.mp4?token=XQ62VFcwGi81xUWrgZFTt-uYRYW89tRsmt6Dw3McGvzhpMbUdTOPpDm-NeezlSK0v3dbirrFVXvU7T0qq2_gaaDQjHPJT9o62b4YxRgO3xIDjN-AsYxfO8wE6AnEJe3UxvE8JgI4xh6hBt7pXjrAqGrVPSQuIK9lNo2X49-UUHuowDj0LpMhX7EtfHa9k1aKEnJhgBqKAh8Nwi2eHgtVEFGU4eIOpg1ILHNI-Qx3vRvdDiOne3iyQPwXfR2TkwR8jy1PALeAb5mrCAvHtUXeF5pRuzk_2eiY0cEB_AnRjColUAZ__4LrK1MkgVQmiR0x9R-jVJcCKsm39zAvQYG2mZhyatxhngQO2DcYDUATcYENnKNhKO2H_8DAXcQ5xCBSTEc6449DbYYG3upK2LNzkraMNpORhkof0MALVns1sNd-dl2RXoN47rPotKyhHpN_jUz2j5_STDVx-FQ8FWJZUu9Ohd88t6tYqbmZrEzFXaXgMFszf2POst6ZxyDarBTMScoz1toOB_nb2-fvyn6xlr8LGfdv4I1BLDW6XUSwh8_YprXK6iQnnbnCH4wElqJeKXNGp7Z5MyNC8mqhqbMo53i73e4JQnjUkb0Q_8GXEoflwKRoSDCmHocR-nL-asDC6PVkF4O73ESXlERODdK-5DVB4pEGaHHspe8hBghISZo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
بازگشت پرواز تهران به تاجیکستان از مرز هوایی بدلیل آغاز رسمی محاصره هوایی
«پرواز هواپیمایی وارش» از تهران به «شهر دوشنبه»؛ پایتخت تاجیکستان؛ از مرزِ هوایی لغو شد و به فرودگاه خمینی بازگشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/107171" target="_blank">📅 13:07 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107170">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=OyFLIpYYTYux0XmXyEWKsJm1CFME3HhbCP6pXqzCAB8CL8c_lHrPEo1iuve72srpTB_ckNKqwp5dxb_FzAk58LTiCPpbviXPwH6Y1QIvqazETdYY_G3nVm5dWWlHt9ZiPcsum6LfE-pIUR7YXmdA9m9_YT65h51FUlkNeRW2XF-M8yldFc4DOJav4WCIg1ybktKoKvKBIkYYvN6h4jgIpyuW3CpCURT7MBbZBoWSfqg36S9MhNu0Y9R83SA9gF5S1m2cgf8sbcvstfuj47MVlk4GuE7mUtHZUfqAR8DiB8xNzm6xXv5yePuKaDhK-g-F3uJUzD68B_OerCZI_y9FSBAalvfoUdalL_VpTScVWzPKvOVeZlkZ0TOz5TWLRzTaKd5zx4ZGEhlB0ERLzQ7DktM2xkAfZlbRuuXVVNkn-UQx4WycaoQ99CxLzYYud_aK9L0K9tJCH-TuOgeG_4zPiwGYfCocbsAzuW7N4kuZNlj_Vqq1F8hqHiHe5Jb8UrwJ2Du8xAukD_VzmSW2IWD2CMwn6Q0BmmgO4sRXuCEr7D_YHK3u4n6JjZzpq_8AczN4vJp6UKbzdc1qJNx6vOO0FpLQBIKg1wYVd4XN8OjzWEfw2S7Uhy-sfTIYYZTqUI0MFKyKJK1cvrASnK6Y9gILgU8qJLsBILfJ_QKnb4l6hh4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1178f7a6a1.mp4?token=OyFLIpYYTYux0XmXyEWKsJm1CFME3HhbCP6pXqzCAB8CL8c_lHrPEo1iuve72srpTB_ckNKqwp5dxb_FzAk58LTiCPpbviXPwH6Y1QIvqazETdYY_G3nVm5dWWlHt9ZiPcsum6LfE-pIUR7YXmdA9m9_YT65h51FUlkNeRW2XF-M8yldFc4DOJav4WCIg1ybktKoKvKBIkYYvN6h4jgIpyuW3CpCURT7MBbZBoWSfqg36S9MhNu0Y9R83SA9gF5S1m2cgf8sbcvstfuj47MVlk4GuE7mUtHZUfqAR8DiB8xNzm6xXv5yePuKaDhK-g-F3uJUzD68B_OerCZI_y9FSBAalvfoUdalL_VpTScVWzPKvOVeZlkZ0TOz5TWLRzTaKd5zx4ZGEhlB0ERLzQ7DktM2xkAfZlbRuuXVVNkn-UQx4WycaoQ99CxLzYYud_aK9L0K9tJCH-TuOgeG_4zPiwGYfCocbsAzuW7N4kuZNlj_Vqq1F8hqHiHe5Jb8UrwJ2Du8xAukD_VzmSW2IWD2CMwn6Q0BmmgO4sRXuCEr7D_YHK3u4n6JjZzpq_8AczN4vJp6UKbzdc1qJNx6vOO0FpLQBIKg1wYVd4XN8OjzWEfw2S7Uhy-sfTIYYZTqUI0MFKyKJK1cvrASnK6Y9gILgU8qJLsBILfJ_QKnb4l6hh4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔺
🔸
مرگ مغزی فوتبال ایران طی دو دهه...!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/107170" target="_blank">📅 12:45 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107169">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mtivD0MlFB2kM8HXlhWKQzcRXFUijmFAkbDOLHXRG8F2v-Iwqu2QySxrubN8Dkn_EeT9t5rARNelUypaV0W7Tq-GqmGoqaHnM9uwrVVaWuCLxrt8Yhr3-N5fHPF1PU62Zi17nlfcEOT1ONftY_YlSeRl6FOV381waxWQxN4EIqGOnvCqZjzMHziZC-BOJZR7ze0LKj6hXZEFPxg-bz13Gb9Wl66e6u-pmIS0UiVIwNMHlPHrjhkXJazitKO47zpaPAvPShgoQuAbrL29C_BMIy8TrLtaQcVzawUOprwOSn_5fAGQlRhEXvodHvoK4ydkxcnovG6p5CcxWBR5YhAO0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/261876d28b.mp4?token=mtivD0MlFB2kM8HXlhWKQzcRXFUijmFAkbDOLHXRG8F2v-Iwqu2QySxrubN8Dkn_EeT9t5rARNelUypaV0W7Tq-GqmGoqaHnM9uwrVVaWuCLxrt8Yhr3-N5fHPF1PU62Zi17nlfcEOT1ONftY_YlSeRl6FOV381waxWQxN4EIqGOnvCqZjzMHziZC-BOJZR7ze0LKj6hXZEFPxg-bz13Gb9Wl66e6u-pmIS0UiVIwNMHlPHrjhkXJazitKO47zpaPAvPShgoQuAbrL29C_BMIy8TrLtaQcVzawUOprwOSn_5fAGQlRhEXvodHvoK4ydkxcnovG6p5CcxWBR5YhAO0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
🇩🇪
هلند - آلمان⁣ امشب ساعت ۲۲:۱۵⁣
🔻
اولین تجربه یورگن کلوپ و ژاوی روی نیمکت دو رقیب سنتی⁣؛ کلوپ: شرایط هر دو تیم مثل همه اما من نسبت به ژاوی بازیکنای بیشتری رو در تیم ملی هلند میشناسم!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/Futball180TV/107169" target="_blank">📅 12:20 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107168">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=hRQVXbpBqC_yksfJMdWZ9xNYxMR0InngjZUOBZO5V8QXQwNmFwhal0N8Qs-yERfadhI5qEt5C9hUVEfhHnrjlTiOsDjyNwRyCde-LP7n0RhS7vv_OdpYm9gltuYI00rawGTg5TOqCTE46bDV3EZC6aA9_kbWC8dJokqrslr_fupaf8HpNfwscrCcrtlDGXELYRst-9Fd3JbyHgaEL8t2eNSFlQkkU-qP1jxh99g9AasDU4jgSE3WpfpeTQRrWt_RT1ja4dfFVMbkaARCDmNdQpZcRtIWFfbgTkMuxM_Z-7Ztif3OPaGPC0Fvj26mACtBVFnqtdSnSQF_CdDIziMeWJPKS0FXtSSNX0_B2-9pXRQIJDVeqfuRFKe1AyhiejyRa_U_6I7ZDDq9HULtnHOcPT8i_qubH2YPMizKMIagIwUu5Fk7qO-vnkC0-h8Vzn2wAa5WRi7alozlnUAdnYSm4TXiW3ODc5A_Bgt1ZI0onC0E0-DcOYOe-tMKFTM7FLy9LFSnTfdU0GBxhBZjtRC0j_9B753vMuLTG2u6Z87gA5XnNy6mHwJuYdxeqDYgetO6jQWJX1VDWRZqqmNvKkTMEwJ2cGeB5DHrxXHCH2yIw8mDY3DmYUHuskr0WdQ1YXkc849zuZZx2bzTOuVsPomqrpF-mB7iOYw0A6NRxQ4oaSE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/20e89ae843.mp4?token=hRQVXbpBqC_yksfJMdWZ9xNYxMR0InngjZUOBZO5V8QXQwNmFwhal0N8Qs-yERfadhI5qEt5C9hUVEfhHnrjlTiOsDjyNwRyCde-LP7n0RhS7vv_OdpYm9gltuYI00rawGTg5TOqCTE46bDV3EZC6aA9_kbWC8dJokqrslr_fupaf8HpNfwscrCcrtlDGXELYRst-9Fd3JbyHgaEL8t2eNSFlQkkU-qP1jxh99g9AasDU4jgSE3WpfpeTQRrWt_RT1ja4dfFVMbkaARCDmNdQpZcRtIWFfbgTkMuxM_Z-7Ztif3OPaGPC0Fvj26mACtBVFnqtdSnSQF_CdDIziMeWJPKS0FXtSSNX0_B2-9pXRQIJDVeqfuRFKe1AyhiejyRa_U_6I7ZDDq9HULtnHOcPT8i_qubH2YPMizKMIagIwUu5Fk7qO-vnkC0-h8Vzn2wAa5WRi7alozlnUAdnYSm4TXiW3ODc5A_Bgt1ZI0onC0E0-DcOYOe-tMKFTM7FLy9LFSnTfdU0GBxhBZjtRC0j_9B753vMuLTG2u6Z87gA5XnNy6mHwJuYdxeqDYgetO6jQWJX1VDWRZqqmNvKkTMEwJ2cGeB5DHrxXHCH2yIw8mDY3DmYUHuskr0WdQ1YXkc849zuZZx2bzTOuVsPomqrpF-mB7iOYw0A6NRxQ4oaSE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
🇪🇸
آنالیز ویژه برای درک قدرت بارسلونا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107168" target="_blank">📅 11:55 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107167">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPuuK17ie0YlqNxpK2FJMxfZnJEYGHFWtys0m3sHxse7EL352SKnYJzuCBhLhPpuI9GNs3_XODt3cRdUWnwuyTDJKtF2bOJD2voJuEGbXD-7Aymh8OLZrhFd2h0CBogxDOwKLiKYir86et3moKvicoT7YNdSi9ykzVsRifX6hhshDdKtHfGj7CuCsDNWEt3HOeApd1Feb-hrHbcwJOY2aeOvrJM72MIZbv_RDeii9HxdHQTl0bM85lerJ0Oh2oJaNtaDdGrdQAnlTDkK3_UjP5sYzDhI5pzpkT23I_Z8Om7LpTAxkp3NIhpBPaGneNPvIsP2y7O4iSieYMaJUwRilQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
5 بازیکن برتر از نظر تعداد گل‌ها و پاس گل در لیگ‌های معتبر اروپایی تا به امروز:
🔻
رافینیا دیاز – 17 مشارکت (گل و پاس گل).
🔻
لامین یامال – 14 مشارکت (گل و پاس گل).
🔹
کیلیان امباپه – 10 مشارکت (گل و پاس گل).
🔻
مایکل اولیسه – 8 مشارکت (گل و پاس گل).
🔺
فران تورس – 7 مشارکت (گل و پاس گل).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/107167" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107166">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/Futball180TV/107166" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/Futball180TV/107166" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107165">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOwPSFPmNKSUtmORnbl85qRufo5Jv6-zumNsWjjBKrLXg1oWm6Lc88gSU_AQwnZhotW9rWPMbvdR6uNEdNZB-v7U8HnDlUKS8-GHudiFOEqeBMOiR6IzClhxJS1UgVJU9ySa4si3c_cmVgErpEBI1XAsvxR63pjz5Pi87ngxSW5Y8Vr26zkA7qu05Pr24_4M6-wnMwA0uHQ8L7DR8-dBMG_-1EIj-8p2AEfxHL8cgqu-UMB4QOWAc2AoDeJSUPb9NvjTzLq-YIxRm34iTw6wFGbjnS9p1cuQaBrNjP5Uc_Jdgpm7bDjuHzUs9b0bmPlY3LMXGMVl8h7S-aR2Q-xphg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
آلمان
🆚
هلند
دانمارک
🆚
نروژ
ولز
🆚
پرتغال
اروگوئه
🆚
ژاپن
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
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107165" target="_blank">📅 11:32 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107164">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dNUkkflbrImLzRIBgq8IZDOiGIMp66ERm6phmuhFa3I0XPJgLnxKMQL5l1wr8C5ubOMOfT9V1jDhpI71fUfAq8JikGl58gaUs7T9wqnzuZpd7kEjH44jEhCNrEhQ-Z3tgx3hP_MdV0kwI-5toc4zUd9f5FU79Brn7_O_4UBgO2zcl8_e2FiL5sArKm4OJJIf4gMXuHY3uqstPR38YpSvTojQSqH0ifgALVTpJgxAnuDRVshMI0v33PXgLHJzE8yd1nmXCWQSuL3xMeKCWpQ1lQOQZgTY5WBWz8qgdGWELF0hnA-6fW79NaXvBeT0owJmzCGoE34HARd7tZl4I9WgAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
✔️
🔥
بیشترین تعداد گل/پاس‌گل در لیگ‌های برتر اروپا از ابتدای سال 2026:
🇪🇸
لامینه یامال - 24
🇩🇪
اولیسه - 24
🇩🇪
کین - 23
🇮🇹
مالن - 22
🏴󠁧󠁢󠁥󠁮󠁧󠁿
برونو فرناندز - 22
🇪🇸
رافینیا - 21
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/107164" target="_blank">📅 11:05 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107163">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=Q0lQqLTEqkoiZ1wqsORVK--xqe7OAh9pMwFDqNfqe9KHhNqa9gJg5FhP6TBW6mn9elM8umJkFV6VtY-PCeCxXqPL4iHedBSokmtAUZjg13MZMcNWA-VWs9kzLhqq-k6R-E2ul9cGUkpYwTOOP0QYVVFP2rVX2buaoJwzJjcsM7JCuWB-qUUe6adp5v0YFQIspQ2NWmeZE_3xC4soUv0rOQ3gh0_ZcsL2a4Liq7TJ1xVfBWaj_VQ0S-YfHbGikQMBS4pDAk02wdoK8gukvhDsL0h6NOD3eW1atjSSjppIK_BFwPp-WGHTj5vbrO577uu45V3D9TzgAA-s_IcoflOOSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7f3392248d.mp4?token=Q0lQqLTEqkoiZ1wqsORVK--xqe7OAh9pMwFDqNfqe9KHhNqa9gJg5FhP6TBW6mn9elM8umJkFV6VtY-PCeCxXqPL4iHedBSokmtAUZjg13MZMcNWA-VWs9kzLhqq-k6R-E2ul9cGUkpYwTOOP0QYVVFP2rVX2buaoJwzJjcsM7JCuWB-qUUe6adp5v0YFQIspQ2NWmeZE_3xC4soUv0rOQ3gh0_ZcsL2a4Liq7TJ1xVfBWaj_VQ0S-YfHbGikQMBS4pDAk02wdoK8gukvhDsL0h6NOD3eW1atjSSjppIK_BFwPp-WGHTj5vbrO577uu45V3D9TzgAA-s_IcoflOOSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
🎙
صحبت‌های جالب دکتر محمدحسین پور غریب درباره اهمیت ورزش: ورزش اوقات فراغت نیست!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/Futball180TV/107163" target="_blank">📅 10:40 · 02 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-107162">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=mo0Mm2jOmAymp0xzmFNiqOdDZzDyqglYjyNQicxmOTcij_2o16iPXwoKlvzqQra7sl1NgAt9v9-Z5RoNsBX95llbRiLrlXBy0HF-7JoD6b186Iz_r7VY3pyJmQgsfy5PCpIWu-edwXM9ywdRTFV2dz0bsyHPiSJ88gzCfM-PiKUTbVZiCROvNB1S0C4TeYbhtxgIbU5J3dE4Pw0qeiEPJZd-eSjys4AC7ug-iwSJqoqnKRr8PJYrK6bzguYOZYV4LyY2WYD1vsJE7h9iuWHaPmInRCLop2vHusI3TUvQyuF-YG9joh9UGMBi-pJ061xu-bhaCWIuuKXL-6l7Kdm2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d50e15c35.mp4?token=mo0Mm2jOmAymp0xzmFNiqOdDZzDyqglYjyNQicxmOTcij_2o16iPXwoKlvzqQra7sl1NgAt9v9-Z5RoNsBX95llbRiLrlXBy0HF-7JoD6b186Iz_r7VY3pyJmQgsfy5PCpIWu-edwXM9ywdRTFV2dz0bsyHPiSJ88gzCfM-PiKUTbVZiCROvNB1S0C4TeYbhtxgIbU5J3dE4Pw0qeiEPJZd-eSjys4AC7ug-iwSJqoqnKRr8PJYrK6bzguYOZYV4LyY2WYD1vsJE7h9iuWHaPmInRCLop2vHusI3TUvQyuF-YG9joh9UGMBi-pJ061xu-bhaCWIuuKXL-6l7Kdm2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اول مهر به روایت تصویر؛ صادقانه ترین مصاحبه مربوط به سال تحصیلی جدید
😆
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/107162" target="_blank">📅 10:15 · 02 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
