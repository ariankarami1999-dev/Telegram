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
<img src="https://cdn4.telesco.pe/file/EO0Bb_JHu0cFOZvaT0eEsTScVUdqID8C85REbE7mNDK9OQqx4b1nAgYtTMc-YT-g_3Sw0l88g3DXi8iRgQez8q5P_V70wsJM969k96u1aLl184wNPQ6MvxX315jGIhFxf6HaGCCDiIsDgcNQMlB_BsxNc7dh_M-0R3548TfZopx6mNlYWyUUJr5ZHbVgwRBIOkPOl2iARAmajqS-8EModarv48BvDp969nFclUzJoBCiTfNrmiPK045PeD4rbzhbDX6nBgQNDGasdpTZhYbr0jHBsQ3lty3r1Zrn31uCKtjELRmY4JgTpjrFJq8CzWsUpVP9tfNbGlGokP7IJ8N2KQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.46M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-21 08:11:45</div>
<hr>

<div class="tg-post" id="msg-697906">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
شانه خالی‌کردن ترامپ از پیامدهای سیاسی جنگ با ایران!  ترامپ جنایتکار:
🔹
اصلاً اطلاعی ندارم که جنگ با ایران چطور می‌تواند بر انتخابات تأثیر بگذارد.
🔹
تنها چیزی که می‌گویم این است که ایران نباید سلاح هسته‌ای داشته باشند.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 12 · <a href="https://t.me/akhbarefori/697906" target="_blank">📅 08:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697905">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8088544705.mp4?token=SPyHsSsDRlbTNSO2QEVoS-maXvOzxBrL3D05iVpX4VnI34oNsMQf_GfajIzdQs7mJJ4gcmlZalis3nEjwb4lPYpWlxGru4EWEnjm2nr1tjLpQUU-keEIgRTLzgkJ4cfAiocVKhwWg8jK7F2oCud29Hrxv-lh6o9HN7aBu76HHdHEReKBBmGJTfyjZxJFlgpFuJKPF-8vOJ5B4va9LEOK8DsEYR9xSic3HgWaclT_d04PnlR-PJ7MiQTMWqiI2y-ZYuP738Q9eBbVe3xa-Rv96uEUXBMeqwy5k8KrMfW4oC6V84exGA5wlM-eCaMlfkZOiDntH6Q0xwd9k7tm4dArmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8088544705.mp4?token=SPyHsSsDRlbTNSO2QEVoS-maXvOzxBrL3D05iVpX4VnI34oNsMQf_GfajIzdQs7mJJ4gcmlZalis3nEjwb4lPYpWlxGru4EWEnjm2nr1tjLpQUU-keEIgRTLzgkJ4cfAiocVKhwWg8jK7F2oCud29Hrxv-lh6o9HN7aBu76HHdHEReKBBmGJTfyjZxJFlgpFuJKPF-8vOJ5B4va9LEOK8DsEYR9xSic3HgWaclT_d04PnlR-PJ7MiQTMWqiI2y-ZYuP738Q9eBbVe3xa-Rv96uEUXBMeqwy5k8KrMfW4oC6V84exGA5wlM-eCaMlfkZOiDntH6Q0xwd9k7tm4dArmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجیه ترامپ درباره گدایی گازوئیل از روسیه   ترامپ:
🔹
توافقی که من با روسیه در مورد گازوئیل منعقد کردم، در واقع یک توافق برای من نیست. این توافق برای بقیه جهان است.
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 1.02K · <a href="https://t.me/akhbarefori/697905" target="_blank">📅 08:10 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697904">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">♦️
مایک جانسون، رئیس‌مجلس نمایندگان آمریکا: جنگ تحمیلی علیه ایران احتمالا بلافاصله پس از انتخابات میان‌دوره کنگره پایان می‌یابد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 636 · <a href="https://t.me/akhbarefori/697904" target="_blank">📅 08:08 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697903">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e2540866c3.mp4?token=dcgzg1KaKde4ZDrLwLz7bUcL85x3paKf-3tv7FuUOhUYSBQdzkwRghoM2yaVmLL0WQ_dXRsU9nV7l0_WE-D5rGQWb-u9Kah1PHzFbP4FGYR3quPYFIk-pden_I4Q5-kj9-E0XT2yGsriSP-1yUUoZ_b0ue5TA1B67ea0UVF6bBlSycbwQLADE3o0WkJ61FL9ejotDtZOJsaww1PZMu7xVfZj5TaqkIcPelG47sXJjAuEYxTRbLABzqEW-SL0ZeAc9EK13PFYr24coaiDZipFAdZP990GsAMOZmrKDDHsJCsMsuhtqhjRgoS9wKlsy0zX9VLiWmyionXEalw-sOHc8r8eMra3QUXyL4LtXofJCtz0G1FWu3g5D7UWEmG8-bd0niTZCiuABlwmXwWRECCjxMo9UEcGPTFJ2H5nSjGo7zy19X5peLRXQlvRAjH4lYX6NT6snRNxLSthwCz7D3FgCxYaHTtpkAhLiMYUbUXe3r4BpK5Sgc1RDJHS0N2mVPlVbVjh-xrHM7Uk7v2nVyY7ZBjNQ_w9rDNHBKex738vHwZIG_FySv53VhvgJJennMhBAgRVls6U13pzduzrWJvck6CPJpPT-WnCNYPz9WdGXAioRa_kST6qmjScfwj_YJJDd_AY12levtewx_KEgWiVRd7Y92t3mJOwFNdK55s0vPw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e2540866c3.mp4?token=dcgzg1KaKde4ZDrLwLz7bUcL85x3paKf-3tv7FuUOhUYSBQdzkwRghoM2yaVmLL0WQ_dXRsU9nV7l0_WE-D5rGQWb-u9Kah1PHzFbP4FGYR3quPYFIk-pden_I4Q5-kj9-E0XT2yGsriSP-1yUUoZ_b0ue5TA1B67ea0UVF6bBlSycbwQLADE3o0WkJ61FL9ejotDtZOJsaww1PZMu7xVfZj5TaqkIcPelG47sXJjAuEYxTRbLABzqEW-SL0ZeAc9EK13PFYr24coaiDZipFAdZP990GsAMOZmrKDDHsJCsMsuhtqhjRgoS9wKlsy0zX9VLiWmyionXEalw-sOHc8r8eMra3QUXyL4LtXofJCtz0G1FWu3g5D7UWEmG8-bd0niTZCiuABlwmXwWRECCjxMo9UEcGPTFJ2H5nSjGo7zy19X5peLRXQlvRAjH4lYX6NT6snRNxLSthwCz7D3FgCxYaHTtpkAhLiMYUbUXe3r4BpK5Sgc1RDJHS0N2mVPlVbVjh-xrHM7Uk7v2nVyY7ZBjNQ_w9rDNHBKex738vHwZIG_FySv53VhvgJJennMhBAgRVls6U13pzduzrWJvck6CPJpPT-WnCNYPz9WdGXAioRa_kST6qmjScfwj_YJJDd_AY12levtewx_KEgWiVRd7Y92t3mJOwFNdK55s0vPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توجیه ترامپ درباره گدایی گازوئیل از روسیه
ترامپ:
🔹
توافقی که من با روسیه در مورد گازوئیل منعقد کردم، در واقع یک توافق برای من نیست. این توافق برای بقیه جهان است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/akhbarefori/697903" target="_blank">📅 08:07 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697902">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0951251d29.mp4?token=rD-VBkbtcsd5x3ty15fSw0OnjbcrD0rhbgzb6FeXKykNcmlIh95fkkv5cTv-XiApgKM5HT1K1sdOP9vEhxpWfPgBsgSp6M8aJccbMqdeLr4pkLrf1w-sZ93ICn9_WvJNwcAEx5U-MwI0Y_Ajw_fXdDBO2exSCt5suqt0VcGsQ4lVVX39DvYWv-lvyOGJiaK_Ml-0z7C0sSZb7dSW2FCb4Rn7umst5bJaRiQYJy0P-qqHbvyTFtY-DgOXL8gRIlW4Y33tXAd-iY6xEbvh_CKb0H94jWE62DDU3_FJ6I7cNzPS02ATmKFPwbnH394oRhpknN_Kxd5TYvtwZ-8WOmuESQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0951251d29.mp4?token=rD-VBkbtcsd5x3ty15fSw0OnjbcrD0rhbgzb6FeXKykNcmlIh95fkkv5cTv-XiApgKM5HT1K1sdOP9vEhxpWfPgBsgSp6M8aJccbMqdeLr4pkLrf1w-sZ93ICn9_WvJNwcAEx5U-MwI0Y_Ajw_fXdDBO2exSCt5suqt0VcGsQ4lVVX39DvYWv-lvyOGJiaK_Ml-0z7C0sSZb7dSW2FCb4Rn7umst5bJaRiQYJy0P-qqHbvyTFtY-DgOXL8gRIlW4Y33tXAd-iY6xEbvh_CKb0H94jWE62DDU3_FJ6I7cNzPS02ATmKFPwbnH394oRhpknN_Kxd5TYvtwZ-8WOmuESQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انهدام پهپاد ارتش سعودی بر فراز یمن بر فراز منطقه «بنی مطر» در جنوب غربی صنعاء
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/akhbarefori/697902" target="_blank">📅 08:06 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697901">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">♦️
ادعای معاریو: برآورد نهادهای امنیتی نشان میدهد اگر ایران [به اسرائیل] حمله نکند رویارویی به بعد از انتخابات موکول خواهد شد
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 2.16K · <a href="https://t.me/akhbarefori/697901" target="_blank">📅 08:04 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697900">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v2YS7-6IGx74YKP5zjqRROACWRI1ji5iEq2xK1iLCmRWR1vWg02kjegaAsXEI766uOg4PkIxLkRctvIYi4jGgmcEsKsYw9icCXvVZQRqEAFQL3YpaQLy7Tx54Wlp4dJxD-J_DLv83kaMA1o_G3NbCs7oXGsal4QK10DHpomR7fwpsQ_26ajTsl-mnseaPe4wq5isgvsw-6QyorfMmNvmoyKZo_xnL-wgTNRv_lY3ZzMJeQj1vU9A0TcUYZgW9-FvxZa2AUeJa2joa2hKeCdPN97KKrAbH_1SUc2qut9Gj-B6PD_daKgivewMZfGn_Tz0y5DHW_NNnGIj-u6f2A0y9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ادعای ترامپ جنایتکار: کمک چین و روسیه به ایران در سطح پایینی است!
🔹
من نظرات زیادی از چپ‌های رادیکال احمق و دیوانه می‌بینم که چین و روسیه به جمهوری اسلامی ایران کمک می‌کنند.
🔹
آنها چیزهای زیادی برای از دست دادن دارند و ما خیلی سریع از آن مطلع می‌شویم!
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 3.38K · <a href="https://t.me/akhbarefori/697900" target="_blank">📅 08:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697899">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GzDkGt32WRuoTR6v5eYMAq5j_M-w90xWmvieTPhYowBLKzU3JE9UWHGjem7UaRVJAnkHmEii3_cg3bfENIWcFlvzIaUFF6ue8dT5FrpVtFLogQ6ZjLEV--iAWowkeECciN4zHNeZ4UD3KKY_ORniortSVyqHuAPnMoPb42_Jnr8BNvS-EU9iYye5LJrN10iJqqZsamcXOmoXLzw-V82viOTFA9CAyQghVIUgubhlnqRiWcLiRk4ya83U3bR3s0OI9uuoFBKhoUOukETHz8wc8SYciz2XHezNgpz_0TAOOX2dzLKFuaw3M_DM1E0I1_V2Vb733fGJ_J58w22tom5dcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز سه‌شنبه
۲۱ مهر ماه
۲ جمادی‌الاول ‌۱۴۴۸
۱۳ اکتبر ۲۰۲۶
سه‌شنبه‌ها
#دعای_توسل
بخوانیم
⬅️
متن و صوت دعای توسل
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/akhbarefori/697899" target="_blank">📅 08:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697898">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBVEUe_t9OuUtxyCeOHFjj6ghmL2SGSbmxC9bKKeCmyz4z9mxt8N33bFyS6P67v4kxrRkqYi5UZ11tvqKiVjF4AG5nSVT1fz7dXEGWPVppQDpsyAByTt3078l3dP5Bu5pNz7J_NHsm0oIxrRFyh_XulGbcwTnM0wZE3Kf6vCagMj6uTLM_ETmt4solV-1NozcbGGqiJJ5Jha7zYWJBcPLBOQI8CEq0tk_Rn3SSzynXQupyioCoX2Qn6Sn27t3Q9_W4I1KZtufaWCvsSJG0f5SPttA_YNFXFutAUvyAR02N13gijXzTFQy9Q3Z0RNc_7midNBg67Tda0h6CSVPr82wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
اطلاعیه برای سهامداران بورس
🚨
بعد از 6سال رکود در  بورس رشد بعدی بازار بورس در راه است که میتوانید سود های چند صد درصدی از بازار بگیرید
معرفی ارزنده ترین سهام بورسی برای سود عالی در کوتاه مدت
اگر نمی‌خواهی از موج بعدی بازار جا بمونی، همین حالا عضو شو
👇
https://t.me/+cq_pNphz1rg3OWZk</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697898" target="_blank">📅 00:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697897">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n2i9qRZO38h7h9XgRv2LWUPy_bHDmQzcfO5O_CWMb5tTw2EeRESfZuW9MUX0-YSQ2HhCzyXUwvWT1KzxnYzAtSlhXgONCncifGMkQloujER5CF9kizgjVF_csXq9t7BSHZpi0CxcaToosST7QX-VXk3g2egGrhs8gPE5Ev5jDdVPD-cjVxZfzaY-KAIXsBUJn6U0cJElX07Z8c_7Eo4c0ub_yDpgciscvBt8vr8T9OeAyQOWRoaHsQAALmXmUdPJoTLixPdnwXyOZmjG9TeZ1TlIP_BP2kdsHJNir1nnyD_rApvH_9eVkV883Ysa2io9kuOoXFONj8PKBSaTLQmFog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ست سوییشرت و شلوار مردانه بالنسیاگا مدل Hami
✔️
جنس پلی‌استر سبک و باکیفیت
✔️
فری‌سایز مناسب L و XL
✔️
مناسب هوای خنک بهاری و استفاده روزمره
✨
شیک، راحت و خوش‌فرم؛ مناسب سفر، دورهمی و پیاده‌روی!
📏
قد سوییشرت: ۷۲ | قد شلوار: ۱۰۰ سانتی‌متر
🔴
قیمت 1,650,000 تومان
✅
پرداخت درب منزل
ضمانت تعویض سه روزه کالا
برای خرید کلیک کن
👇
https://memarket24.ir/product/fast/51854/180124/</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697897" target="_blank">📅 00:30 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697896">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N9YbjMLvhzqbjVfvdqpd-zKEEd1nQdjy12Y_GNXGI1CMMoPgRJV1FOkSmdjE8M9WMZJQa_WPwaDrAW7AZ9sXBsHa5HkkihZRT0NcfIovF1vK1yB3oEF-_Ba9-7fjHyM1979kg1FiCnHqC3eCXI1gF0FTSTDRWZ9-Nli0d_Z5VwymFLhuO74F0Ow4Ux8f1vtaeNNSVihqvvfNVPQu2pGyzJ1bKtfuNxEDtwxyw7UTGkUtc_muwXfUuv_jYfWyqyIn-f6tbi2M5tflMUuoA7z6phPwGJ_OZdzMCizBEziix9bAyXaACqCyn7x9nFvEi8UeVhut8pQ1178InVCf9fCn1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فرمانده کل سپاه پاسداران: «هیچ قدرت فرامنطقه‌ای حق ندارد در تنگه هرمز و خلیج فارس تهدید کند، حضور سلطه‌جویانه داشته باشد یا مداخله نماید.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/akhbarefori/697896" target="_blank">📅 00:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697895">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FI8obtDXk3MF4ubDdpWLw2YaLm_8HQRdiy29olpkVpzbRFb8efOdQYc_rP7_9jnE1Ka_QdYqgF4NGdtcqb8iyqiDlNf38JNKXTgSsxOHkqShEDT0LGu7V9jHwbJJgOXpvNPOu5_fEuTzRYDHpMvModwFfCV2nuoi72lGLPWrUS8nZpAzJDzSNa0uKT199LRiMmQJET5ec1T3VEcePZPmaC9b0GRrn_fgHfWdIwydbtL3Zat5h5xCuwhkdG-CDVTGrmi3f1YqWqEIm3T3xjUuV4DI3Saus6Oqc_yzQ6ez9-NJAwd7Lyu9pi2IdZrcTS6_q9mLPxG_Tu93ZEE_w9g3fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بازیگر بریکینگ بد خودکشی کرد!
🔹
آر. جی. میت، بازیگر سریال «بریکینگ بد» که بیشتر به خاطر ایفای نقش «والتر وایت جونیور» شناخته می‌شد، در ۳۴ سالگی در تگزاس ساعتی قبل خودکشی کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/akhbarefori/697895" target="_blank">📅 00:22 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697894">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromروزنامه دیجیتال خبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hGjTkktsn8euZDqWG8INypkNHMxNMXsbH7EaexuOvLQEhHDQ3rfuDT8dJXXyRl5WO72qM36XZe6hMx5vD6tFfyh6ECKz5ltgpdUTonxx4DLy2_Hz8Lyqb5DauIRWLwBhQUrOrL2ZveoooYuuVp-G7Pmfcjgg8umfE9FRjP618BfDcMAGyE2cVSa6BvkInfZNZ6xSkdgRJoyW8ohifPqgpnQ1JbvsQKbUkge5lHUund8QyabaqBDSF4l-Uu1Qez4CGdq418pVtUs-PhY3hpSbPGqb0R4Cm6JhcO9nnPF7AgLgPP4_7ZqI-YSDyeqe5lCUZ_eQGlyz2q-ry1i-yTQkmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سگ‌ نازی‌آباد
🔹
رفتار تحقیرآمیز ترامپ با زلنسکی، بار دیگر سیاست منفعت‌محور آمریکا و بی‌اعتنایی واشنگتن به متحدانش را به نمایش گذاشت. ترامپ که در مقاطع مختلف زلنسکی را هدف انتقاد قرار داده، در تازه‌ترین موضع‌گیری خود خواستار انتخاب رئیس‌جمهوری جدید برای اوکراین شد. رویکردی که پرسش‌هایی جدی درباره اعتبار تعهدات آمریکا در قبال متحدانش مطرح می‌کند، همچنان که می‌بینیم کشورهای عربی هم بازیچه او شده‌اند. اسماعیل بقایی، سخنگوی وزارت امور خارجه، با یادآوری جمله‌ای منسوب به هنری کیسینجر گفت که «دشمن آمریکا بودن خطرناک است، اما دوست آمریکا بودن مرگبار است.» او همچنین با نقل عبارتی از جعفر شهری درباره آمریکا، گفت: «بعضی‌ها مثل سگ نازی‌آباد هستند». کنایه‌ای به رفتارهای ناسپاسانه و بی‌اعتنایی به روابط و تعهدات آمریکا، حتی در قبال نزدیک‌ترین متحدان.
🔹
هشتصدوهشتادوچهارمین شماره جلد یک خبرفوری
#تیتر_یک
@rozname_fori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697894" target="_blank">📅 00:16 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697893">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
انفجارهای جدید در خمیس مشیط عربستان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697893" target="_blank">📅 00:15 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697890">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qjiiahnfmKkcOTNnPY5fuoRrYraDwo-rDDxnQOz8e4hTQuSup4aVN0uCzNZImZEJvb3aPvPUOludd_snmeLCXlsimwaT5X9qGsCdbskSarKNmZUD0LBgetvIGJ5kWJ5HUWx6-rgDe2CcKAe9RteNc3PHLgspNWeG_3SUYlSvbB-eiL3SA6wczTEVn6lpOZ89wsOlaCspLCsBk3oXr6atcHyWiFegOsJVreuaXDOmpnDzqJqWcOKH5-9iLIQjGBXPbuX-JFbOTrwbw7eEZcd7VX2wxvLu24zI0RujGHc2PQgldoF3FSy_BJgTZFyHt1tfRA0o0bX9jqcwMQ_XLfVE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SnLIQsKugj2m6BDmyHb7oluszrkXIct2J6Adc6EZDIfXj8D-MBw8TQJkoohx8iG3l-dg5xy1Of-NWWsmAQjPlrKCImPMHQV57_1JKdGGQFw3k5xJEPxZKxlJ9srMnTBnzyWNTkf62IXdAJZ3BFndoF0irmMZRf-zj0QqYj07zyUYV5KcDX1VrBu0Jp5nN2cmlvrfqTB1okksAR6M5Lxg1mcEQPsL41pd977xMlJPs6iaRTAzD_YZnCbog1LZV1BHf9hc694RUoW4ywVvrwMdpRwf-2Y4SLSECjE3ezoJzA3JgNWJtj_WBzk5K4cftf1TeX7Mo5IQaZsftRfnPZljQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tyW3VZOjGIQOvPKu8XkAVfKmKbgH51TZzteMIQj5LJTTsO42HIKbyH7zB1cg3ICd9C-lWpcmCUfxXlUx9k25NcCqPftoKyNJ8S6KZbh2tNF359al-EIMS1gUo9qQ_a4TJfdZDQ2DlB71e3FSFggn-rZnhHMbn4YgK0geL-nZ5LoxyMc9qEEGJ7NZWPT0gnGt_vVCH9j8XFZCQegbxu0A-UFTGDhJuZJNApit3yP25rhc3UhX1AVo6I1y9UVKq_4cg5-ucrVe-Vp8snSbpNg77tdhDj_OJ0qJfOYrZd-2abOQ1RZZ1r6vg8dCfST7thnIEziZPqwOH85TGtyn9Xf_Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
راهکارهای ساده برای پاک کردن سرسخت‌ترین لکه‌های لباس
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/697890" target="_blank">📅 00:09 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697889">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromخبرفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FryOL6dOnCecaNM_5N-zLDlbzA9Flkkg0mxEdqViLCTVwRFMe6q0-OMiaplgc5xCaVA7a2f4v-4pNzcyce6zmgUe-wohx9rZJy3iSQO1fWbyJl1cOLJ8p1J8OKAo8ca_1gwzlbAnRErPTn_IYstNllmZz4WlQ1snIrTwpj8wbksCPrzENUGEuGrLHsJc2A7GnUJZLLwy2GjgGKJz2ODl7DK3X9TcyFpKZiM_5dokeUlw8DIDA4eLcqCCCCKfPwH5Q2NIuoAn7Hnd684eEp7Tdq4xGzG4M6nrT0ew7k_Iu-hIeZyfJ5rG8zWy90V4pRqh_q286Dm_Q0snmXj0EWoLpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
با هم دعای فرج را برای سلامتی و فرج آقا امام زمان(عج) می‌خوانیم
🔹
با قرائت دعای فرج به این جمع میلیونی بپیوندیم
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/akhbarefori/697889" target="_blank">📅 00:00 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697888">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0hv_PJh-nbrHMT0wLW_aTPFN-cMIHjZBeMs-TP0edhoodcWnY6rKU0pe_AohvOQhcaqwfvggIc__P4FLNC4r_-HGyl5B_g4sul5FtNjC_DXFRjyZgRXW-HFCvCaospVl-AvOOYiJQ-iGviA4ltB-ccJJSPGEV3bvmcnJXKXNVWHg1ezrt5ijB5kjIXoLcKFqQkusscCcPVugCEGcZpnQ8GCzTP_zDjnIGI-l7C7mTFEt7djpd20WR5QO8w1LLVX2_gtk43_qnNu4tpcdREFWWBmt3DGeqx_YZi4SSRD9R4vjhXsO3mXu_6aX4e3V9amE5_AMYFpQv1IQFj-R-vkOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت خبرنگار BBC از ترس نتانیاهو از پخش مستند ویژه نازا
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697888" target="_blank">📅 23:59 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697887">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
دقایقی قبل؛ ریاض عربستان تحت حمله موشکی یمن
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/697887" target="_blank">📅 23:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697886">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عضو کمیسیون آموزش: زیرساخت آموزش مجازی بهبود یافته و در صورت مجازی شدن، با مشکلات کمتری مواجه خواهیم بود
عبدالوحید فیاضی، عضو کمیسیون آموزش مجلس در
#گفتگو
با خبرفوری:
🔹
زیرساخت آموزش مجازی کشور نسبت به سال گذشته بهبود یافته و مشکلات پیشین تا حد زیادی برطرف شده، بنابراین امسال در صورت مجازی شدن مدارس، دانش‌آموزان با مشکلات کمتری مواجه خواهند شد.
🔹
غیرحضوری شدن مدارس سایر استان‌ها به‌جز هرمزگان نیز در صورت نیاز و متناسب با شرایط تصمیم‌گیری خواهد شد.
🔹
در صورت بروز شرایط جنگی هم پروتکل‌های مشخصی برای مدیریت وضعیت وجود دارد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697886" target="_blank">📅 23:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697885">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixKEfjxq3vNClXHJQ7VxJuEz5QqrmkPiaaSkleu7CvYybZcrfK0zatESarvcg9b4lGWYrxmz1MFOLxIIZfLUeCDTt98uWHaWa_xsvPASRJmDiPwmWmcxQV7P6eiz18ZSelVBFFtTc7EUQoACSoIOu8_3ZV1lpW86HqIfGhTYbi2qIXTG43CfEO6CrCjDiznugK6ZStjjf14Fo8W-3oawPBCDmEZGkJDmYUtrJH7uY73cgOt2Pmja6Xr2UkWP7MWgBUCJAfqetPRDG_fhcDgRkYvrJbUZ0_4Tfcl8Cdh7MVf3K-ixb9CngOWXb2zwd9PX89zPQ19UrqEjcPqjOyrADA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
گل دوم استقلال توسط حسین گودرزی
🇶🇦
الغرافه ۱ - ۲ استقلال
🟦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/697885" target="_blank">📅 23:49 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697884">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
نظرسنجی مرکز پژوهش‌های مجلس: ۶۴.۷ درصد مردم ایران برای دسترسی به شبکه‌های اجتماعی خارجی از فیلترشکن استفاده می‌کنند
/ باشگاه‌خبرنگاران‌جوان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/akhbarefori/697884" target="_blank">📅 23:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697883">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7HBZ-sIge-vgNjvu0V_gu153c-uN8iCToNUVhrL5RrbLdj77AjJDh9HcyH1vc1qRUVN7DPfXOLDlLNySN2ZsUgeA5Vz5mUP2YI7gJhynXc0EdCZMkpD4bbCDb3UcM6dux0W1IufvwExL_8BiXJA8z38d1NIlpJOeHxJwJ84wiIeFgHL1LVK-OBSuMCPjaYiavMPEUQJQMghPaFobb1fxvvRcyree1YuV9jHee5wx9Dhxa-eHirJetgltrukqYEpXdZpIDp00tE8zjhwi9M5ENNnXwiV6oFTC4O96fOVQbNF6tLwgcdECrcBse73fbfqeOdwFLxYdR5IgReB5sLwWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
این نمودار، اهمیت تنگه هرمز را خیلی شفاف بیان می‌کند
🔹
بورس لندن: نفت برنت فیزیکی به ۱۵۴ دلار رسید، اختلاف قیمت کاغذی و فیزیکی نفت پس از کاهش تردد کشتی‌ها از تنگه هرمز در حال رسیدن به ۵۰ دلار است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/697883" target="_blank">📅 23:40 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697882">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/156e9b4045.mp4?token=R1mFQWgsqc14P2-FymtJtl9iiq3ExV8Um6XR7RjCgKFvazAwZv8Dvy8lAERSuOAQ2_7WQHhj759fS7ZG7gmJ48rAw5yyvrkvanUz_1rEnaHweZsFhFTC0E4mw0_ggkD-j1Q9DYv2nfdPBg0tkU0hu8v2OCD_2AzbcAjqjEFBgmBRFyDUURuzanYAq8rA8G468NiZSe4Q1RG6pAwBUMObdJUu7tZRzPbyjVXyp2uIt8HUpCdPXxmqplMWtdKhYMVu8seMvU3uGhpyypJGjCQCFbKaE_JFuLfMDRR1ox-KeMojrNTPEMIQYWuj00rsC5aqrZYamk1hish7S0snTMiKhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/156e9b4045.mp4?token=R1mFQWgsqc14P2-FymtJtl9iiq3ExV8Um6XR7RjCgKFvazAwZv8Dvy8lAERSuOAQ2_7WQHhj759fS7ZG7gmJ48rAw5yyvrkvanUz_1rEnaHweZsFhFTC0E4mw0_ggkD-j1Q9DYv2nfdPBg0tkU0hu8v2OCD_2AzbcAjqjEFBgmBRFyDUURuzanYAq8rA8G468NiZSe4Q1RG6pAwBUMObdJUu7tZRzPbyjVXyp2uIt8HUpCdPXxmqplMWtdKhYMVu8seMvU3uGhpyypJGjCQCFbKaE_JFuLfMDRR1ox-KeMojrNTPEMIQYWuj00rsC5aqrZYamk1hish7S0snTMiKhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گوش‌پاک‌کن؛ وسیله‌ای برای تمیزی یا عاملی برای آسیب به گوش؟!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/697882" target="_blank">📅 23:38 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697881">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a375c1540.mp4?token=v2F0I5y2p9NkULHmH_gGaumYAYeL3OXXt0uoeS-j_iACUlJtbGlsEk5VJsDzF8zXdNypBdpQ9FtWEtUF1emCeFczWhTtAaTSrTdnEVdpht8PXob2BeDxZskoJ3Yra7_UFIJs4SZuh3vVbVqY0T3EGbRldS5J5zqzJo_BZw-ctjIzL8tCdZgV7Co9Ncs_QWtGmFxtLsPQU8ZZ2fYqZH2uMR0zJFWLBniWtwgeROS1_o1u3YOt_SRgaEWdObvKb3Jwpti-HJ2mF5aetDf8U1-RsB3xnt0oMHcuWD1azzvmCoDFiWFvz1wdh9__ht6xBLz8_ACUKmrgYuveKBrETehJUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a375c1540.mp4?token=v2F0I5y2p9NkULHmH_gGaumYAYeL3OXXt0uoeS-j_iACUlJtbGlsEk5VJsDzF8zXdNypBdpQ9FtWEtUF1emCeFczWhTtAaTSrTdnEVdpht8PXob2BeDxZskoJ3Yra7_UFIJs4SZuh3vVbVqY0T3EGbRldS5J5zqzJo_BZw-ctjIzL8tCdZgV7Co9Ncs_QWtGmFxtLsPQU8ZZ2fYqZH2uMR0zJFWLBniWtwgeROS1_o1u3YOt_SRgaEWdObvKb3Jwpti-HJ2mF5aetDf8U1-RsB3xnt0oMHcuWD1azzvmCoDFiWFvz1wdh9__ht6xBLz8_ACUKmrgYuveKBrETehJUDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علیرضا مطلبی: برای موفقیت، فقط خوب کار کردن کافی نیست؛ باید در صنف درست، کنار استاد درست و در زمین بازی درست یاد بگیری
برای ثبت نام همایش بزرگ استاد مطلبی در مشهد از کد تخفیف BMT72 در لینک زیر استفاده کنید
👇
https://evand.com</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/697881" target="_blank">📅 23:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697880">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/InHNcRZ0JiGY_b3xeT3w6IX1cS_LEj2bh8vnl28ShTeTafyIrfBabFaRK0SQCb620DP7PO4XeeVKVlpSt0eIhBF9DPcRMlb-Y3jAQiMh04vTCKGgkGDVMRsr_6dhPzcaR3tUchUEl237uGm8dftm1Zj8e6h2FLpSIH0YnI4A_DYLnFLuCFts695kNTaUiImdAt-viDg-cwlAxJJXQjGilkfoIxq_dmFEpmqzfW_W886ma21O8wLZkPpNJa7ofQmU-grmqPlShYul5VX1Wx5OiqOWMSfd9ZWU8O0ZK4uV0wuUcWEF8QxF154eyRMIL08rWErdg1YvfNG1hzlk5NEQCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
همراه اول از مدال‌آوران ۶ المپیاد جهانی تقدیر می‌کند
🔹
همراه اول در ادامه برنامه‌های باشگاه نخبگان برای حمایت از استعدادهای برتر، مدال‌آوران المپیادهای جهانی کامپیوتر، هوش مصنوعی، ریاضی، فیزیک، شیمی و زیست‌شناسی را به طرح تقدیر سال ۱۴۰۵ اضافه کرد.
🔹
این باشگاه پیش از این نیز از نخبگان المپیاد نجوم، رتبه‌های برتر کنکور و مدال‌آوران بازی‌های آسیایی ۲۰۲۶ تقدیر کرده بود.
🔹
هدیه همراه اول به این نخبگان شامل سیم‌کارت دائمی ۰۹۱۲، مودم پرسرعت 5G و یک سال اینترنت رایگان است که با هدف حمایت از استعدادهای برتر و دسترسی آنها به امکانات ارتباطی و دیجیتال ارائه می‌شود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.8K · <a href="https://t.me/akhbarefori/697880" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697879">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/38b4159a2f.mp4?token=HBav84xH7pyLNCbzZN3P-5U3OZtyypZ9UT9WdlgmBrEgqGOmoGi4Cg2bdt_EVmokvxJTthQGaiaO--a7Uu5CG-IUz3q6ezMtIwQm3idenD_5ZJKs9XUTjVCzFKP8RHCWfoh9-BDGXfreq7IVk7vWUSYPOXzl3OhV5_UMNt5mB6Fjhk2EflHmxLq8fsMH4WnyXhEFIaus-5ZMTM1p4Mj-8IYXZhuDmZtKVatCR_YPMl67sEamQ7Ya9gsgmS7XJRLk3Q3WEfzXxYw3ppFpR0ELcpsUcm0A3DOxBGCSieCexO5F9AXTbQSrwsXQ892JguabA0nxK8iGuMrcM2GVjz1Rew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/38b4159a2f.mp4?token=HBav84xH7pyLNCbzZN3P-5U3OZtyypZ9UT9WdlgmBrEgqGOmoGi4Cg2bdt_EVmokvxJTthQGaiaO--a7Uu5CG-IUz3q6ezMtIwQm3idenD_5ZJKs9XUTjVCzFKP8RHCWfoh9-BDGXfreq7IVk7vWUSYPOXzl3OhV5_UMNt5mB6Fjhk2EflHmxLq8fsMH4WnyXhEFIaus-5ZMTM1p4Mj-8IYXZhuDmZtKVatCR_YPMl67sEamQ7Ya9gsgmS7XJRLk3Q3WEfzXxYw3ppFpR0ELcpsUcm0A3DOxBGCSieCexO5F9AXTbQSrwsXQ892JguabA0nxK8iGuMrcM2GVjz1Rew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
دقایقی قبل؛ ریاض عربستان تحت حمله موشکی یمن
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697879" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697878">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZZlHQZx14qKG0zNBzFhjcgocfAO61pFn6pg16-lLXiXkXdxQ1iaWtfr7PY0EmlGrHvXb1erQlDOMWngOd3GNSeyNW2YZf4vnTkyifHCVcOBsvxLQBPdlThWWdBTNZsgrtRVVC4seqx9lLkNLX7dqhYPziOIpVi4yOSiuYluxg4XmZyTfYojilrpQp6c26yeW8LkIXcdycEW9zDUclGbyYBeS7xrFGPXyXymeOkGFGgH5ISkl6AS3ZhQIv7jpOtbV8cZ_1qVtE_hzb1z6zEUijT09DZjEHVKVucrzyp6EAJ-wwOJAu0147ucCwPOp8pZxlNRnp58UilKBXRYXItdMKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
خبرفوری رو در سایر پیام‌رسان‌ها هم دنبال کنید
🔹
خبرفوری در ویراستی
👇
https://virasty.com/akhbarefori
🔹
خبرفوری در روبیکا
👇
rubika.ir/AkhbareFori
🔹
خبرفوری در ایتا
👇
eitaa.com/AkhbareFori
🔹
خبرفوری در بله
👇
ble.ir/akhbarefori
🔹
خبرفوری در سروش
👇
Splus.ir/AkhbareFori
🔹
خبرفوری در روبینو
👇
https://rubika.ir/akhbarefori
🔹
خبرفوری در گپ
👇
gap.im/AkhbareFori
🔹
خبرفوری در ای‌گپ
👇
iGap.net/AkhbareFori
🔹
خبرفوری در واتساپ
👇
https://whatsapp.com/channel/0029Vb1RfOdJkK71F9wpxh3F
🔹
خبرفوری در اینستاگرام
👇
http://instagram.com/_u/akhbare.fori
🔹
سایت خبرفوری
👇
http://khabarfoori.com/</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/697878" target="_blank">📅 23:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697875">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری گرافی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oNM-NRIoaeTc5dQUp1U9mPXwufEzmH9Nj52wwGOxeQxoFRBuChFAQJFdFAPzxWVpkeA4l-phypviRfSO2v9U843Wo5TTQPVb_q2XER8rq4GETpeJpZ2lx7A3gKkEK9CwCSZ1C2WE5R-dH4iy_KaltUKGwCVB44FzZZt_SjlrPD2ZLH0WFl7XyJkGFnjw-n-EhDAUtbD65rx151_MhiPrRJu4LCtWbTvQZrObxx9EjThHp8vbMmsIEZ6aRjaw4zapbnRO7Mn1r-8AlvQPoODihDUp2TFPbxAngv5zUvodxmaGOJxIvpohP7YwR2QKh_xepmrpRf4HwfTiTlNwicPUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cmAlXPB-D8cZD46U2h1Ryq0ldZmaGweYaPu-uoH8DVlIydamGA6rYvD1zeW_2sL6Hd02s-bw8HShcVhHDTdbUn6WN26vfzlN-YLjD0yE8lRyfnDmFKF4y8Eb-Ip1lg2xgY_jpxBxZn6k1wVY4hiUPt9eWTf9UNAFlur3NcFQKtjy8vswfFd8YbR6Z9Mg3mE0OF1yyWdpdq_a-vhR2ijXCWYxJiRZK4DkjkzS7RPob7lg-Q7Zo7L3Gfm1ug0K4tgK90o35sywp_4Q7L9SzoLxuPZG8eGHAMf85zOoIgj8ugEpkixhGStJvazf3XNPdcPZhCy933aiIlO2Yng4_91New.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aB3U9bTDcWiCFdbaI92EC5m-e0TlBQN-_FAA3UXOP4k0tRQVSJuRXaBTpIqVvVOYTB61zpGW3HjmbS8sr2CLOVEqAPgA5XSA1dyhmyYkrusQ-KBWl9J01AtwEWlS40_RN4ZjlP6GAYD8Y9IpqMw38AfRCF9LiqbjckynR5O3wvhwYz6dOjMVM5xewHnk3dOmij9UoT7arNibVMGECGEGVZ-L-5fUChKNi-_R9FczQBTfl8fMvsUozy-IgvdzsLFTAnM9Zp74BpytgQnRnLi_ViN-1sexoRaRrgiRKQ3juaWKbjZylrn4UPiggs36hGp9c-r6DpHsF59XPto78ITgrQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
پشت‌پرده زندگی برندگان نوبل اقتصادی ۲۰۲۶
🔹
برندگان نوبل اقتصاد ۲۰۲۶ به چه ایده‌هایی رسیدند که نگاه دنیا به پول و زندگی اقتصادی مردم را تغییر داد؟ جزئیات علت انتخاب رو در این پست ببینید.
#اینفوگرافی
@Fori_Graphi</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/akhbarefori/697875" target="_blank">📅 23:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697873">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IUBZnKWPh_o-TYxStO9xyCTrciSd5OtXovJUUXRCJEB8iGYSBZERecggZ4GLL4mPBTawUWbhPIUwDS2y9_2aIgivpyXnc2yVQB2n4MbvCUEAniVcT-BQQ7bjs9Iuzhv5GjK_JMMmJzAMRZAbeCSQZrXyKc9zA7m17fHTaXbUGOX1Lvj8iZZTMqYDAFUcLjuMr9xuKgq6vT9fhGMH43-pQhka1Q2ofrpTJNTL1tUk_n0fRNpwq9DeLYqynHlePuQyX2DLwYeHnUKi_I9kmnYAiX2brHMmnMxxBYMck4BZEPHEQy7rfOIIsxMGlblX8DO17wA7ZjFnrm8adHLRzhv7Ng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GmUrS5cp7upitePFjSWDz5l_vkpqG9KbMRIYQH06d0sT3SLyBXJh4lQAOoKqe0x2fJT_eTu3W7NHc6AqnVWd-pjbItyeM9UQX6OwzTX2OaTrQ-hdCqWvyBo7PDX9zWvJzm7bxnJmo2OXqxK7EE0XebiT-i7hbX7Rm_7GjmRcpe79uRsWGL7-GHog18coI3uuRzcGPBHPSMImKLqmM6mBIwXKHbiLPbG1BEw5ZP2mxBRCYagKJB466KtOdqTKk1ucqcI9EWLDghDQf9P1dIsc9yYYllIRBFq9Ro4bQf1VZLKoRgGGrXrFyS5N1KiOPDN8fO_5C4sf4rX5bqbBDE1M3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
یه عکاس تونسته پدیده‌ی نادر اسپرایت قرمز رو ثبت کنه، نوعی رعدوبرقه که فقط چند هزارم ثانیه تو آسمون ظاهر می‌شه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/697873" target="_blank">📅 23:17 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697872">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/908fc98dc7.mp4?token=u_jOaNmxCMjkPumrUwswihrdwuB3r7TJ5yh3Cz8-czVfSOCaoKTgcX51gWixxVbXwTb7tF5oW4wWL_cfOEhFCMzvO10bazZGPD0AIwl8iJHIhMevgpYt-NwsEELZoipqfHdVyEN9Keup4FonrL_gC5kqv16D8-guM65b4WNlsK92O-RABxmSo3p9NgwAcF89HTWfgA9MAProg_FjgFSv4kCIXUZSGKU3OwXvXH5J0-pKDcxtjKqiZxOPddL_K1AsyvzuZz0AycOq2s0NUuefd-1vQuq45QxvDVkE_TO9djAOgYQ4wpknmQwpKbJj9Jf2e5q7OP8qK9dmKdjvZTa34A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/908fc98dc7.mp4?token=u_jOaNmxCMjkPumrUwswihrdwuB3r7TJ5yh3Cz8-czVfSOCaoKTgcX51gWixxVbXwTb7tF5oW4wWL_cfOEhFCMzvO10bazZGPD0AIwl8iJHIhMevgpYt-NwsEELZoipqfHdVyEN9Keup4FonrL_gC5kqv16D8-guM65b4WNlsK92O-RABxmSo3p9NgwAcF89HTWfgA9MAProg_FjgFSv4kCIXUZSGKU3OwXvXH5J0-pKDcxtjKqiZxOPddL_K1AsyvzuZz0AycOq2s0NUuefd-1vQuq45QxvDVkE_TO9djAOgYQ4wpknmQwpKbJj9Jf2e5q7OP8qK9dmKdjvZTa34A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گل تساوی الغرافه قطر به استقلال در دقیقه ۴۷
🇶🇦
الغرافه ۱ - ۱ استقلال
🟦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.9K · <a href="https://t.me/akhbarefori/697872" target="_blank">📅 23:12 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697871">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g6g9-d-u9S4yJsY-ToE3wLunVQR4Z7tMPX8pe9PSdBVsVLK8r8qf3Xa8eQgMmsAob0dRZ6B1amOBMviSD4eAFU5E14MCZTid7mKtqlHQwOamJ5bowb-lt_O6LVdKUIT2ZsAz4kOa5_-WJiqNkeq9QLic0pX3T1Pm0g3Z8gPF_csN3AabdqLd3Yvp6m-3JtM5gKTOXNRQCJ60eZ9oo-44XPyD3JuODfHROE4bph2rBChNGu40XLG4S2qs2ESs9C2cNgI5sqP7qR7UQnoXKDmcqh4oc_f8_HhHkEKGGnStOPtKR_R0yWjML0_3cFe_Sfwo1I6_ABD0aNImfnNBNVa-0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
۲۰ میلیون تومان اعتبار دیجی‌پی برای همه!
امکان دریافت آنی اعتبار از جاباما فعال شد
⚡
دریافت آنی
۲۰ میلیون تومان اعتبار
💳
پرداخت هزینه اقامتگاه در ۴ قسط
✅
بدون نیاز به ضامن و وثیقه
🏡
اجاره انواع ویلا، کلبه و بومگردی
اعتبار ۲۰ میلیونی دیجی‌پی رو همین حالا بگیر
👇
https://www.jabama.com?utm_source=telegram&utm_medium=paid_social&utm_campaign=digipaycampaign_news</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/697871" target="_blank">📅 23:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697870">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه مالی فیروزه | Firouzeh</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QRwUxn1621tFJQ-87pM14zd7PoL0ULRjmNV_zems5U17ly-_roDRh2-_fdA5KLC_eMv9tgEkPBsYeH3rGPcGlWkcgHenmkr0eTxXnxYvVBMo9U_IPqNb7x1C8GvX-KP5BwriF_Hs_7FmUI8scvTpIN_pg6l0fyepX9zo5SZONzEtXXVZQpCQ6iLQVKKME40lCIBPQlgH9SrTzI82Iz_kqKSgiLVWpn2ZfHV0auvWMVQ4QBwnCI8vqOa5jt2NhKjPmHAJEoRLuNRY_M1NYoOKT9U_Aj3kqEG4fNuI8vwseK5DVq-QKvrAsIMb6hPCsL16ofHmtKrMdC7B-01QXZFGNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🪙
🪙
فروش محدود شمش طلای فیزیکی ۱۸ عیار فیروزه
مبلغ هر قسط به قیمت روز خرید تقسیط می‌شود.
💰
بدون بهره
💰
بدون کارمزد
💰
بدون ضامن
خرید قسطی شمش ۲ گرمی
🔷
با پشتوانه
گروه مالی فیروزه
https://firouzeh.gallery
https://firouzeh.gallery
🔙
مشاوره تخصصی و رایگان سرمایه‌گذاری
🔜
+982191079672
💎
@firouzeh</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/akhbarefori/697870" target="_blank">📅 23:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697869">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">صد میدان 13- میدان سیزدهم، زهد</div>
  <div class="tg-doc-extra">علی مقدم</div>
</div>
<a href="https://t.me/akhbarefori/697869" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
شرح کتاب صد میدان خواجه عبدالله انصاری
🔹
میدان سیزدهم، زهد
🔹
زهد به معنای به‌ دور ریختن اضافات می‌باشد. هنگامی که بیداری الهی در درون شخص شکل گیرد، فرد به مرحله‌ی زهد خواهد رسید.
🔹
در مسیر معنویت (سلوک) می‌بایست وابستگی‌هایمان را از همه به جز معبود یکتا از بین برده و داشتن ظاهری معنوی را پیشه کنیم.
🔹
آنچه از خداوند برای ما باقی می‌ماند، هیچگاه توسط افرادی دیگر ربوده نخواهد شد.
🔹
جهان، جایی‌ست که بر پایه‌ قانونی فیزیکی به نام عمل و عکس‌العمل استوار است، بنابراین هیچ زمانی درگیر بازی‌های ذهنی نگردید و بدانید پاداش رفتارهای خیرتان به شما باز خواهد گشت.
زهد در سه چیز بکار آید:
🔹
اول زهد در دنیا: هرکه دولت این جهان را از دشمن خود دریغ ندارد
🔹
نشان زهد در دنیا سه چیز است: یاد مرگ_قناعت به قوت‌(روزی یا هر نوع خوراک)_همنشینی با درویشان
🔹
دوم زهد در خلق: هرکه او آزرم خلق وی را در حق مداهن نکند
🔹
زهد در خلق را سه نشان است: دیدن سبق حکم_استقامت قدر_عجز خلق‌
🔹
سوم زهد در خود‌: هرکه به چشم پسند در خود ننگرد
🔹
نشان زهد در خود نیز به سه چیز است: شناختن کید و دیو_ضعف خود_تاریکی استدراج
#صد_میدان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/697869" target="_blank">📅 23:04 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697868">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d779adada9.mp4?token=s78E3rIhOnlLkvCETfPjhs1nU42FzZIozqg8jiGJf2Mqi_lo5-Ve_PP3iuOOslDwGq5PiOS8kT862S9bnmJwOl3F6xINHvj16gKuEwMMKhUKVdycR-7v-YH6hke1Z4NZw_gT7WWZZwnmnMMmoxx7w33QCZ3ZYyOIbqFQa7drF7IVPC6H2Z6PN_qIib928ADJlc2dP-Zv4G-m8T-nDeP6ps97Mw--Bq0RJmovKy_01M3rOn4UZDfCL9UZwoQbC68bO6Ym9Zy_Z1KXrSacMrEdYTeXd_EeCQX0n--9lw7Op4xNLWyxW41FQMquD0MEibaw0BZXNW0rZ_GSO2WtPm79zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d779adada9.mp4?token=s78E3rIhOnlLkvCETfPjhs1nU42FzZIozqg8jiGJf2Mqi_lo5-Ve_PP3iuOOslDwGq5PiOS8kT862S9bnmJwOl3F6xINHvj16gKuEwMMKhUKVdycR-7v-YH6hke1Z4NZw_gT7WWZZwnmnMMmoxx7w33QCZ3ZYyOIbqFQa7drF7IVPC6H2Z6PN_qIib928ADJlc2dP-Zv4G-m8T-nDeP6ps97Mw--Bq0RJmovKy_01M3rOn4UZDfCL9UZwoQbC68bO6Ym9Zy_Z1KXrSacMrEdYTeXd_EeCQX0n--9lw7Op4xNLWyxW41FQMquD0MEibaw0BZXNW0rZ_GSO2WtPm79zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یحیی سریع: یمن با موشک بالستیک فرودگاه ریاض را هدف قرار داد و اصابت موفق بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.3K · <a href="https://t.me/akhbarefori/697868" target="_blank">📅 23:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697867">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c00563939b.mp4?token=avKsHPtxydRGQ6CSe11zvF6sOxvi-wSFarKdLWSWsj0MIPVR7iO0Pz6GN-9VgGV0nS4NPySz1ol-nWEn3gn0fjXBx72xhMLtxPeoyuoVB_3VhQu_OR_vc99R7Z8GI4uiqicGStAFwWHidurl71vpTJiT4ASa6FIYbAVUqd6TMr2-BjlQVfp_98awTGnSdv0_3wjQReBm6cDAEprVTFW5t8RnX2Gz7ClwQrXUvi5UNNap_QTU6aTkkaQz080ygUQq8PUvDDlOuSXL3nHk3M3eXPg9oWwAJNI1r6la6RGMIG63vIvE2qP2NQJbxTLPnluUHkq8eH0dtQUUrCdjqqHeqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c00563939b.mp4?token=avKsHPtxydRGQ6CSe11zvF6sOxvi-wSFarKdLWSWsj0MIPVR7iO0Pz6GN-9VgGV0nS4NPySz1ol-nWEn3gn0fjXBx72xhMLtxPeoyuoVB_3VhQu_OR_vc99R7Z8GI4uiqicGStAFwWHidurl71vpTJiT4ASa6FIYbAVUqd6TMr2-BjlQVfp_98awTGnSdv0_3wjQReBm6cDAEprVTFW5t8RnX2Gz7ClwQrXUvi5UNNap_QTU6aTkkaQz080ygUQq8PUvDDlOuSXL3nHk3M3eXPg9oWwAJNI1r6la6RGMIG63vIvE2qP2NQJbxTLPnluUHkq8eH0dtQUUrCdjqqHeqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌏
هفته دوم لیگ نخبگان آسیا؛ سوپرگل استقلال به الغرافه توسط آسانی
🇶🇦
الغرافه ۰ - ۱ استقلال
🟦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/akhbarefori/697867" target="_blank">📅 23:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697866">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oAqZ2x-XotCKGPycxlWcEJod_iKDbVvjJkfHe5XwlrvfuP4u0h_SDYbq_nkf2ia-Z_Dqorll31Z-KmZe9ZnnCDNLx4GGHRnle0j3p07CW_ywKuyxuN-Jnx_-lpTDWop0AYZh5aj1jynItkBRcE8nJiXVS3JxAf_T7L30fg5ewwQkh0-3SeWvlphnwx5krzaDYvtaujvR_3HKPsWxUHJOmGclrKiJcv9HvHmwpceBAmLIfET0w9_jNDDU7uOzuA4sZunseSh5uQlz3j_y85iBEGgfiMeLCmes5QiHlN8EfP5m8MWcSWDN2yn1pyta72fh2x3MiIWRGTIJz4nTcu-mUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
یحیی سریع: بار دیگر به همۀ شرکت‌های هواپیمایی، کارمندان و مسافران می‌گوییم: به‌جز مکه و مدینه، آسمان و فرودگاه امنی در عربستان وجود ندارد؛ از سفر به آن‌ها خودداری کنید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/akhbarefori/697866" target="_blank">📅 22:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697863">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GFqby8lSkC5MdrHoO2fqHeM0wMriCeXHhDQ5v61JoaMhas8rqVRdY6kKwAYxWLnmrYAEGObG7eTivXydR7nXu10P8UgpMdoA_6yOrhGGrfOLijC_mTsrhrcFvSNgWI14BmIMBmOS9gVwseZtBjnOhh3rWoqmy8YnvfxLTxjZdDMBleqCnhsOoBjHnb2ZIUSuGkyhEHhBOW-kYPceAIL0D8b6_2hk_717AioYEkXk7hWyN3WyzIPe5oOObow-zCYLPuuuCYMwdSSYMlnaT0F9h-Pet9_H7msozmNphHUVYjjtkdcBqaF29ONdUQStIv37nweUNh22b_Y2wyDV1ppeXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RphVtPZUMiAwsM_rLaUgbV9Kyy27R8NnTi8hWV7SGmco-bXCLhNtszLrE-9TrXVU10RNaf46VVLYWJ9OUKAirB-YLiJuN1qb4SCCfJn9C57Hp2oFkew63xfBhmGW1_SQbyu4ggWgNhHkbefc6xExjvVxIPGsqG_1jWe-D3tSwkgqu6WWV2NMCjRi4z61PbFgffCX1fLDKeRLKifHM0J2P4p8Hc3FJ3kVC-tZTokzvmzOpmEzzNX75WfWYuVfiVedtW1pJcBuCiq4sFgue1rY9_R4LNAxN6h7Ju7RT6-lpPo2GjrkNkAle-I7D2T0EBx-VcaFRIkZTTdpgL4WggRxog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cRtv_Z0t_46bdHSYrkA5TxCxpRV5TtJbWUmA6mgFV_TMvsAkRx9Oc2VwOEnh3FXdg-3Tsdyc9ceElD85b3WI7yh7BZvGBOZf3c_z5zvt2GNaMLGReWEUYbmkf9v4JdVM-mnJhsFXhGTYRbzqAM74ZvUj-9V0NEI4WOWxB1Wj-0jGAvQEKSga3gXQxYva9ry_cp34JrE6uzdjLnjxVIPuY5Zd__1S1sejZncOFxPcapAdhoGZb8TO8L_m38gAOZ6ozpGTXThORAcxrUv_DaBS9fs6wusDBa-HgzHZOpYcqDUELaqyj7TN36KwjyQDPxxr1CarK_CaCsv_39yQysFEvQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
تصویر ماهواره‌ای آتش‌سوزی سوپرنفتکش هدف‌قرارگرفته
🔹
نکته، محل اصابت است؛ جایی که نفت خلیج فارس توسط آمریکا کشتی‌به‌کشتی می‌شود.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/akhbarefori/697863" target="_blank">📅 22:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697862">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uckeYCcChoLkEEWSEvWctTLDxx1gD8atxNa7IrGkyoJT4F5Ho3Bkwc9OTSOrz2MrZp74mKKNcKvTBOOBKRjwvy8eXFNe0zI-H3V8vDo6mvC2fo8NYlpjlQVfBNpozYdUnn1omxByyKKbr1Er6FYzHq1rXcPQ3gLovB-d9dM7QU2oRLEbf22EimLplh_lGHw4gxkXcGlvSFmvtHzibWfIrSmmBBt9UKUnFYtLRL8pXVjHIHn3XlfWLI1y2f-YZov6piGmkGNfZrrwXoBQZ6ox2gwIWN9vMDQsZKWMRuMF1aDrqBc8FjeEcznlYSOvHKEyBxUMWZwAJOA9_0olalB-0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اسنپ حامی تحصیل ۵۴ دختر عشایر خوزستان می‌شود
🔹
اسنپ با همکاری مؤسسه مهرگیتی و پلتفرم روستاتیش، طرح «مشق مهر؛ مسیر هموار مدرسه» را برای حمایت از ادامه تحصیل ۵۴ دختر عشایر مقطع متوسطه دوم در شمال خوزستان اجرا می‌کند.
🔹
این ۵۴ دانش‌آموز از ۷ روستا برای رسیدن به تنها مدرسه این منطقه، با چالش رفت‌وآمد روبه‌رو هستند.
🔹
اسنپ قصد دارد هزینه سرویس مدرسه این دانش‌آموزان را برای یک سال تحصیلی تامین کند تا مسیر تحصیلشان هموارتر شود.
🔹
در این طرح، ۵۴ دستگاه تبلت نیز به همراه محتوای آموزشی آفلاین و خودآموز بارگزاری شده بر روی آن‌ها در اختیار دانش‌آموزان قرار می‌گیرد.
🔹
ارزش این طرح نزدیک به ۴ میلیارد تومان است. در این طرح روستاتیش شناسایی و معرفی مناطق و مهرگیتی هماهنگی سرویس‌های رفت‌وبرگشت و تحویل تبلت‌ها را بر عهده دارند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697862" target="_blank">📅 22:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697858">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeVVhA8G5SyBTHoOKSOLUOQbUpUtR0R7NjeBp5puew5iLMMp_-n1EGNpULq_oFMYFJZ6phzE8_N6wfX-yWZrpCtAinshQC3lB1KmdtoHgA7mpTf4heW0Adua8N0BsOoNXuIRHk15-aFnUH4nqDDeBrnltINQ0rlerddImS7FY3WKp4Mga0KQEMrunsGj-Y1cVx75ZnxAKfJVA4d-O3TvJccA6boWISuchX7RB2X9zJJ4bVaKa2M1Eq0DUR8nyVtAL5MZWCwCd3CKC-yNG29w_BOem-ICyy1eRfljAOBrfEGq9gQazBYe7X5I5GBxltc3pvV6od3gK3VCJcAZi51-hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WUCY4cwtbFgBIqOPnRxQ_tEJ6WDoV_1EL4AxOD8iANIIVqu5l4hjGSFTKcLO6t5qGaf4Tz0ZjdKmp5HfAeudxeEf4sRdMICQxyCT1lJ4mq2hFYnKmyqtbYsqh3ZkapmYnj2Mxbv0sl8pfGrbhmjUcBBbDbB_d_zEZ5FQD4NcQn7hAqTEIOnhcttARIN2VxxomDP2hau7ZMOxUx5Z0ln8kkf1LIJGo7RDV_KvSLP0OYVOKLgXE9WWFOu0zy5HgvWCzzK4ADW0wpTJm66lZRHMNDtRQkXN2ExXh2mOtpftJQYMCDqCXjArhGrAh11auaBQsvMCjs_VldcIiRgeGOt8Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j4n05dEjTfLy8lMiWz8LZkbS84M51Pqfm4A5uTXUiOl7zPUGHkWtbz3XK8WFM_oLOokmSaZpce8ImBlMdOQp_ENAWhlmHm-4wMZqxX_sAEixt8Ok8Taq2CE-CjbZUlH2ramPVTxWto00xUPzpRP6E7eAjda-npk3RGzJtVT4frX7IGNDMmVISUmOJeYbK4ix89dgOYRV6DNjBlV2tjmSobAbHVmNqM5hp-lhDjmd10e7GUK7SwmRHVwkOmNBT_DNUU1bIV3FiXlG48dNbZhIHztW3xSmBRYcDzfUbxH35apeSOjDIGsmt4RlyHb57MJtV533lQDdZBNWmbE6fX7plg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mfx4AcpXR9XQDEIot0_0AP5AlKoubxJWAG6m_b2rqY1Lez1sWWH8KYw0VaU9FbPLFJ39cKeHUl1y7NNf3kXezbt9h7pXscwJjljn5VNmOlYkf-AJHsFKuI-6X1pEgJad641_pBL2fQWrNNvKWO62v-Jd95s-sbJdeL6j-6h7ECQ5s761xWSw1Xgdd_9kS_BnuIoFmbEj6NQkRs8YZQ6zL43eAXZWgBXY4xSDwbLPPjwVqEPEm7z9OnLAcncR20bywbYtqtr6lxlhs_U03yEbtrtRIse0BjmLmvwTZoGolCeDScZnHxYEAUOXiXsb_7sMEa533A1ePxC_Bz75jSP6GQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
این مکمل‌ها را با هم نخورید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.8K · <a href="https://t.me/akhbarefori/697858" target="_blank">📅 22:52 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697857">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
یحیی سریع: یمن با موشک بالستیک فرودگاه ریاض را هدف قرار داد و اصابت موفق بود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/697857" target="_blank">📅 22:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697856">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b2b6d2969.mp4?token=JR9SuW-6uZFbZkJGEFXG0sXBoEhLrL3xsooHpLpgg6nR2WWkXK3FU9gXc4FoOrAEjZF_VBZSXcYWr6eahXQTQNYOu0j_BRk9XDn_6k91zYfOvw4_yXie2yCvxsIPPYpwt01yGniZxi0bXBUaLdSpHO5y_c7N8m89XNJWcyYxibq95KOUN8P02WSHPKC0puXeJFh2BwpN6WYSCIexs3M7lKT3Xno15o9soYZafQOaH-Y9Hib0I4mcjTYCYB0zONmSUTSG8zq8k3TJzeJIfSxkbaDnVzBjkfHaNLsTfyNqeaVfTLDPdi1iZK9C0nayI9wO7tykjBJqc5ksQSI7yzhvAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b2b6d2969.mp4?token=JR9SuW-6uZFbZkJGEFXG0sXBoEhLrL3xsooHpLpgg6nR2WWkXK3FU9gXc4FoOrAEjZF_VBZSXcYWr6eahXQTQNYOu0j_BRk9XDn_6k91zYfOvw4_yXie2yCvxsIPPYpwt01yGniZxi0bXBUaLdSpHO5y_c7N8m89XNJWcyYxibq95KOUN8P02WSHPKC0puXeJFh2BwpN6WYSCIexs3M7lKT3Xno15o9soYZafQOaH-Y9Hib0I4mcjTYCYB0zONmSUTSG8zq8k3TJzeJIfSxkbaDnVzBjkfHaNLsTfyNqeaVfTLDPdi1iZK9C0nayI9wO7tykjBJqc5ksQSI7yzhvAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
انصارالله وارد مراکز دولتی تعز شد؛ مجاهدان یمنی عکس رشاد العلیمی، مزدور عربستان، را پاره کردند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697856" target="_blank">📅 22:46 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697855">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">♦️
آتش‌سوزی‌های گسترده در ریاض
🔹
به علت حمله انصارالله، بازی النصر عربستان متوقف شد
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/697855" target="_blank">📅 22:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697854">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
بخشنامه جدید درباره حضور و دورکاری کارکنان به زودی ابلاغ می‌شود
حسین رحمانیان، سخنگوی سازمان اداری و استخدامی کشور در
#گفتگو
با خبرفوری:
🔹
سازمان اداری و استخدامی پیشنهاد جدیدی درباره حضور و تردد کارکنان که یکی از محورهای آن دورکاری کارکنان می‌باشد، به دولت ارائه کرده و این پیشنهاد در شرف ابلاغ قرار دارد.
🔹
درباره دانشگاه‌ها، فعلاً تأکید دولت بر تداوم روند فعلی است، چراکه حضور دانشجویان علاوه بر آموزش، در ابعاد تربیتی و اجتماعی نیز اهمیت دارد.
🔹
در بخشنامه، یکی از مواردی که تأکید شده این است که در خانواده‌هایی که هر دو والد کارمند هستند و فرزند خردسال دارند، ساعت کاری یکی از والدین حتماً باید شناور باشد.
@TV_Fori</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/akhbarefori/697854" target="_blank">📅 22:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697852">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64dd363ecb.mp4?token=pRgQZwjJyMJ5PqXuYTZISiZk9aFez57nYtOhwJLj4tqrHKz02pii3C-2OJv8kfeLgROLspjTYluHxIVeVeCgHeh880Yv8bef0qvEwXlOEDGVEhryTrHh-MushhhlzJqzXIl_ZhcE8oyqGLgVS5iYh_gKFrJxGHjTuJx1KMmsgvYRkK0Ba1YqLU6dBryfDhEt3Cy7FPiItNLfZN5mtI-Xcztc4zzm47R7NUhrQODIY5JbVcjzAHivC2tIrviJ9BnmjOWMcxC7IQuHluz4Xp5FeD-2wbMpKIgmhGN3YM9lQWpEG1JuD0zNPEHo7FkyQVXF3ARAxHXn0IIjIqO8KoneXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64dd363ecb.mp4?token=pRgQZwjJyMJ5PqXuYTZISiZk9aFez57nYtOhwJLj4tqrHKz02pii3C-2OJv8kfeLgROLspjTYluHxIVeVeCgHeh880Yv8bef0qvEwXlOEDGVEhryTrHh-MushhhlzJqzXIl_ZhcE8oyqGLgVS5iYh_gKFrJxGHjTuJx1KMmsgvYRkK0Ba1YqLU6dBryfDhEt3Cy7FPiItNLfZN5mtI-Xcztc4zzm47R7NUhrQODIY5JbVcjzAHivC2tIrviJ9BnmjOWMcxC7IQuHluz4Xp5FeD-2wbMpKIgmhGN3YM9lQWpEG1JuD0zNPEHo7FkyQVXF3ARAxHXn0IIjIqO8KoneXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدئوی وایرال شده از‌ یک مراسم جشن فارغ التحصیلی دانشگاه
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/697852" target="_blank">📅 22:36 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697851">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf45bfc93f.mp4?token=dhep6N-GbPv0IOtv24Btw8tLwlrwuDg1uLCE6BjMPSBsrtsOfnckq2jYDvSaW5qSKbq0NdbZvo8RvHWu5qYkukYPtcMVe4qg7J58LcpjRL_R77Bg9m644mo5H-MWdWGXglfc5tQuVJkATKUA7FI1YGuXDTl-EguylaQ6GRJZ27ORNJDQJT5kfPpc8daVfuqWkMtn7LCJaU64poBXVcnXoeSJZ0rcjkD9K82n5wl9UmxBkPK7lWdPqLNpSz2wLG2G9jBjFJDiKYsM4winjvIiIsoDk8EpK_BTHNQUMFpP4GjpCRx45LKH_GEPR7eM9evQpBW7vFBD9neei4kpc8bc_njjyYGiminAQbMutoM39Ghu387PbVmJo3SiCwFnOXNuZuHHIGrSEBZw05pZFdfz7Kw209FAlcPgR0rJvFAvw_G4YOAWBm9F0MtA8Wa9E8Oyic4-sKPaX7klUz7X1eVF_i1F11gqOzo3kUIv3nm01uof6AHjkTVx2stPkn1eoEtmUIWDpgW1Oyas1KeTWJjFsD45Qu5gAbelgnnGpcJLugyfQirfSI-Mf2XAObtSjtvAeackxgnGqwKYz7flbKPtqxilOGjzY3YURVIUhQXx-9HdX-1Z5S6jigq9o2LcSTT_aGHy7-0plWoj60HIttWmbavj9GgolGtL5HoDWW5YH2M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf45bfc93f.mp4?token=dhep6N-GbPv0IOtv24Btw8tLwlrwuDg1uLCE6BjMPSBsrtsOfnckq2jYDvSaW5qSKbq0NdbZvo8RvHWu5qYkukYPtcMVe4qg7J58LcpjRL_R77Bg9m644mo5H-MWdWGXglfc5tQuVJkATKUA7FI1YGuXDTl-EguylaQ6GRJZ27ORNJDQJT5kfPpc8daVfuqWkMtn7LCJaU64poBXVcnXoeSJZ0rcjkD9K82n5wl9UmxBkPK7lWdPqLNpSz2wLG2G9jBjFJDiKYsM4winjvIiIsoDk8EpK_BTHNQUMFpP4GjpCRx45LKH_GEPR7eM9evQpBW7vFBD9neei4kpc8bc_njjyYGiminAQbMutoM39Ghu387PbVmJo3SiCwFnOXNuZuHHIGrSEBZw05pZFdfz7Kw209FAlcPgR0rJvFAvw_G4YOAWBm9F0MtA8Wa9E8Oyic4-sKPaX7klUz7X1eVF_i1F11gqOzo3kUIv3nm01uof6AHjkTVx2stPkn1eoEtmUIWDpgW1Oyas1KeTWJjFsD45Qu5gAbelgnnGpcJLugyfQirfSI-Mf2XAObtSjtvAeackxgnGqwKYz7flbKPtqxilOGjzY3YURVIUhQXx-9HdX-1Z5S6jigq9o2LcSTT_aGHy7-0plWoj60HIttWmbavj9GgolGtL5HoDWW5YH2M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گادی آیزنکوت، رقیب اصلی نتانیاهو کیست؟
🔹
بر اساس نظرسنجی رسانه‌های عبری، احتمال موفقیت آیزنکوت؛ رئیس سابق ستاد کل ارتش رژیم اسرائیل در انتخابات پیش رو بیشتر است. البته راهبردهای اسرائیل در قبال ایران فرقی نخواهد کرد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/697851" target="_blank">📅 22:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697850">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">♦️
کسب‌وکارهای اینستاگرامی چطور زنده ماندند؟ گریزی بر حیات آنلاین‌شاپ‌ها زیر فشار رکود
🔹
با سخت‌تر شدن الگوریتم، افزایش هزینه تبلیغات و افت بازده پست و استوری، فروش در اینستاگرام بیش از هر زمان دیگری به دایرکت وابسته شده است. مشتری پیش از خرید سؤال می‌پرسد، قیمت و موجودی می‌خواهد و انتظار پاسخ سریع دارد؛ بنابراین بخشی از فروش مستقیماً به کیفیت و سرعت مدیریت این مکالمات بستگی دارد.
🔹
اما پاسخ‌گویی دستی به حجم بالای پیام‌ها، هم پرهزینه است و هم محدود. ادمین نمی‌تواند شبانه‌روزی و بدون تأخیر پاسخ دهد و هر تأخیر می‌تواند به از دست رفتن مشتری منجر شود.
🔹
به همین دلیل، ابزارهای اتوماسیون دایرکت مانند «دایرکتم» به بخشی از فرآیند فروش بسیاری از پیج‌ها تبدیل شده‌اند؛ ابزارهایی که پاسخ فوری، هدایت مشتری و فعالیت ۲۴ ساعته را ممکن می‌کنند.
🔹
اینستاگرام امروز فقط یک ویترین نیست؛ یک کانال فروش مکالمه‌محور است. کسب‌وکارهایی که دایرکت را جدی گرفته‌اند و آن را با ابزار مناسب مدیریت می‌کنند، شانس بیشتری برای حفظ فروش و ماندن در بازار دارند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/697850" target="_blank">📅 22:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697849">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
در لابلای خبرها، داغ‌ترین‌ها را ا دست ندهید
🔹
🔹
روایت فرمانده سپاه تهران از اداره کشور به مدت ۱۰ روز بدون فرمانده کل قوا
👇
khabarfoori.com/fa/tiny/news-3251961
🔹
بازی انتخاباتی با کارت جنگ؛ ایران باید نگران چه سناریوهایی باشد؟
👇
khabarfoori.com/fa/tiny/news-3251951
🔹
پوتین در دور زدن تنگه هرمز به کمک آمریکا رفت
👇
khabarfoori.com/fa/tiny/news-3251782
🔹
پارسا پیروزفر تغییر چهره داد
👇
khabarfoori.com/fa/tiny/news-3251796
🔹
شب آتشین در تنگه هرمز/ چند کشتی متخلف هدف قرار گرفتند
👇
khabarfoori.com/fa/tiny/news-3251979
🔹
خبرهای جذاب را در خبرفوری کلیک کنید
🔹
khabarfoori.com/hottest-news</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/697849" target="_blank">📅 22:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697848">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t2ZbVt0oXq_o68e5e6N6fg43Q9jbNht7GNAVGk-IPSi6Yrh6YwufsHgNiTYc-mNCPkJ5s2oG6_WyGd9o_HyfLt7N_lv1zOXTbBnpMCHZTnmCJfkuno0V_mFeh90Xvn043FQxKBNGKX_VgOm9xK1HtJOXuNP6C9J8oBo41o1sw3ttUwfavirfXaOtMFZ3QuPLCdP2RCwEAFFg0k3zpkmw65UU6DFSKN5gq6aNddsgA0JHqYZu-IdNsCNKqfIL_DA2im6sWVFIQeIGGmp0xdaW_ccPBN9pQoLEgiYVOgKpiR7J70Ud7wAd3ojDZ35zkNlRlKL0DOaPdkhD8M4rM634eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پتروشیمی‌های اسرائیل و ۶ کشور منطقه در بانک اهداف احتمالی ایران
🔹
بر اساس اسناد و نقشه‌های منتشرشده از سناریوی پاسخ متقابل که توسط رسانه امنیتی جریان منتشر شده، فهرستی از حیاتی‌ترین مجتمع‌های پتروشیمی منطقه به‌عنوان اهداف احتمالی و راهبردی واکنش موشکی معرفی شده است.
🔹
بر این اساس، در صورت آسیب به زیرساخت‌های ایران، مهم‌ترین مراکز تولید و صادرات محصولات پتروشیمی که از ارکان اصلی اقتصاد و زنجیره تأمین انرژی منطقه محسوب می‌شوند، در بانک اهداف قرار خواهند گرفت.
🔹
این فهرست شامل بزرگ‌ترین مجتمع‌های پتروشیمی در اسرائیل، عربستان، قطر، امارات، کویت، بحرین و اردن است. از جمله این مراکز می‌توان به مجتمع‌های بازان، کارمل اولفینز، گادیو و حیفا در سرزمین‌های اشغالی، مجتمع‌های سابک، ساداف، سعودی کایان، پترو رابغ، الشرق و الرازی در عربستان، قطر انرژی، QAPCO، Q-Chem، QAFCO و QAFAC در قطر، بروج، ADNOC و Fertiglobe در امارات، PIC، EQUATE و Kuwait Aromatics در کویت، GPIC در بحرین و Arab Potash Company در اردن اشاره کرد./ جریان
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/697848" target="_blank">📅 22:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697847">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb3ff4a47.mp4?token=i7J85PhVSGBbayDwHWaoo18RQ9GSjT5Qj6aCxTTjn_S0bV1Nt4bVSfDla2V9fYO3t-w_7WzkQ0qs7N8--ljRxzuMLgCT5srHmZg7MmAje7nXHKBKwWT4vXRsNmTs3Zr2kq5sj7QlAStTPoSJ4r_nEkZS1prj4e5KCTmEiMtkIIy0nz7AK4XZUby-e98vuZb5kgnPYkaGcYeb5taOUvgpH36raDILsdivi8Xdsa7v3PnZTPt17GM4O44rpxiHtjEQXB854rDZ6ecWM-PGy1RdWV8cgpxUKtPnNMVQBp2NKht1ENWjABWKRekSjzQtFovEM_UEhAc4zrx5e4aLM-O4ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb3ff4a47.mp4?token=i7J85PhVSGBbayDwHWaoo18RQ9GSjT5Qj6aCxTTjn_S0bV1Nt4bVSfDla2V9fYO3t-w_7WzkQ0qs7N8--ljRxzuMLgCT5srHmZg7MmAje7nXHKBKwWT4vXRsNmTs3Zr2kq5sj7QlAStTPoSJ4r_nEkZS1prj4e5KCTmEiMtkIIy0nz7AK4XZUby-e98vuZb5kgnPYkaGcYeb5taOUvgpH36raDILsdivi8Xdsa7v3PnZTPt17GM4O44rpxiHtjEQXB854rDZ6ecWM-PGy1RdWV8cgpxUKtPnNMVQBp2NKht1ENWjABWKRekSjzQtFovEM_UEhAc4zrx5e4aLM-O4ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌏
هفته دوم لیگ نخبگان آسیا؛ سوپرگل استقلال به الغرافه توسط آسانی
🇶🇦
الغرافه ۰ - ۱ استقلال
🟦
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/akhbarefori/697847" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697846">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdblV2qgZmwQ8u7hl3NSGldc5C6_-norXY4Wr2BcjMvhhgRCyCXDXsUqxgi1w7mMFRProgG0MlqZG_LQKF6vnqXpP0mgxXfatP6O-R4Mt2Xc7VtrZVVAwSHfroXKgcr1dJhvi20hoaP2LpcaOM7qCeCpbscHtJ2Xo628ax91IrXo0pvt9cRuYjk3SPDZBf8ygi4aXPnbnYeSnQgYg4wWwA_wFSV8Z2WhchE7n54wXOf1CySNYiA17xftZVpAjNAagTtIk0uDEHxoC8foDa1EfpUoLoCxqiMOClbRRSaK9i6wePXX-I9oNTqIo669FtSLrXHLvCO-95vWBFln03hTqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
برخورد نفتکش متخلف با مین دریایی در اطراف تنگه هرمز
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697846" target="_blank">📅 22:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697845">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e32ece65f.mp4?token=Nxgj-SCJmyCak9Hkh3a5QFxPz8SyzaAHD_cUJpyZtzcwyf6Y4tggJIglptxeFya5zQ8DnQ6iFawA6mCiEBITdbLgHcMWeK_l9iyBOfvQsw6YXdKLlhdARad15-r7jxNqiTQnmZ8nVu6jFVJKfMMu6jm-ERwrXP8OYhWo2krYO6ety6rcYxSAx0nTRobsiljzxZkgHpTWCqqKMEKvll5IApTNk7_RLd8dYt1Ud3blYYTTeqv2nWuU3-EwpCzy72F2vp5vmCU2-4qMwnEJgfYqRrkG9Nj1HEJrKwVlh_sJ8b7vL791yAT66_k7JaMg0eyb06wnv3IC6xzb3oO3v95XFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e32ece65f.mp4?token=Nxgj-SCJmyCak9Hkh3a5QFxPz8SyzaAHD_cUJpyZtzcwyf6Y4tggJIglptxeFya5zQ8DnQ6iFawA6mCiEBITdbLgHcMWeK_l9iyBOfvQsw6YXdKLlhdARad15-r7jxNqiTQnmZ8nVu6jFVJKfMMu6jm-ERwrXP8OYhWo2krYO6ety6rcYxSAx0nTRobsiljzxZkgHpTWCqqKMEKvll5IApTNk7_RLd8dYt1Ud3blYYTTeqv2nWuU3-EwpCzy72F2vp5vmCU2-4qMwnEJgfYqRrkG9Nj1HEJrKwVlh_sJ8b7vL791yAT66_k7JaMg0eyb06wnv3IC6xzb3oO3v95XFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماجرای فیلم قدیمی کتک خوردن معلم چه بود؟
🔹
بازنشر فیلم قدیمی کتک خوردن معلم با انتساب نادرست به تبریز خبرساز شد؛ بررسی‌ها نشان می‌دهد ویدئو مربوط به بیش از ۱۰ سال پیش و یکی از روستاهای لرستان است.
🔹
خانواده دانش‌آموزان بعداً برای دلجویی رفتند و معلم آن‌ها را بخشید.
#اخبار_لرستان
در فضای مجازی
👇
@Akhbarlorestan</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/697845" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697844">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad52e9f20a.mp4?token=PUU05csEWsJwtx9hwCkua6eYmZr-Vw-pE5WfmdK6XeUa1Hwdp6E8xe7jy_WMrpWV__oZMY_5YSaLfARXsQsXV0By3ryPCs1YDjpPOPyK9NvynMQB5GfXNFAvJiZ8GGyqtgSHQsQa5wHORgueW6QJ_OM1cm2UuzeTUGdwzI5xZ9T6HMZyGtyUSVSfext-5DKlzbLAAtdSrq5JdKgQbSEyjJe43YbTR1Z9U41bflOROAgIQWbNmlb2RDi7xIG_JflY4bXU0nxfa3qkw7pd_6JeRrNrdAcBB8RmNLrgc1kPwH2j2M4PF1v9AVHz-hagLe00JcUsEfdhRo67UBzCInZpLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad52e9f20a.mp4?token=PUU05csEWsJwtx9hwCkua6eYmZr-Vw-pE5WfmdK6XeUa1Hwdp6E8xe7jy_WMrpWV__oZMY_5YSaLfARXsQsXV0By3ryPCs1YDjpPOPyK9NvynMQB5GfXNFAvJiZ8GGyqtgSHQsQa5wHORgueW6QJ_OM1cm2UuzeTUGdwzI5xZ9T6HMZyGtyUSVSfext-5DKlzbLAAtdSrq5JdKgQbSEyjJe43YbTR1Z9U41bflOROAgIQWbNmlb2RDi7xIG_JflY4bXU0nxfa3qkw7pd_6JeRrNrdAcBB8RmNLrgc1kPwH2j2M4PF1v9AVHz-hagLe00JcUsEfdhRo67UBzCInZpLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ماروشکا؛ طلای کمیاب باتلاق‌های شمال
🔹
ماروشکا (Rubus chamaemorus)، میوه‌ای کمیاب که فقط در باتلاق‌های سرد شمالی رشد می‌کند. نارس قرمز، رسیده طلایی.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/697844" target="_blank">📅 22:14 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697843">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">♦️
دریافت خدمات شفاف خودوریی در اتوپلازا
امیر پرویز فرزان، مدیر اتوپلازا:
🔹
ایده اولیه اتوپلازا از اتو اکسپوی تهران شکل گرفت‌ و در آنجا با شناسایی معضلات شرکت‌های خودرو و مصرف‌کنندگان، به فکر فراهم کردن جایی افتادیم که افراد بتوانند خدمات را بدون دغدغه و شفاف دریافت کنند.
🔹
در اتوپلازا علاوه بر خرید و فروش خودرو، بخث تعمیرگاه، خدمات پس از فروش و سایر خدمات خودرو را نیز فراهم می‌کنیم.
🔹
علاوه بر این، یک سوپر اپ لانچ کرده‌ایم که بخش بزرگی از دغدغه مصرف‌کنندگان را می‌تواند رفع کند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/akhbarefori/697843" target="_blank">📅 22:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697842">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f5184a4d.mp4?token=Dn_xgVnwSo20JbMjwIKfZM8lPGnY6FZS59GW6JtpC6go3-raFKL-L84de1NoDwdUWOwRtZxeXqKClqsLqpoKpthzA7Lyxk5R4dT3Ve-2dX28HQGE0imQI7l-uqRyjqBSnBOFV4rD0ig_D8m8HPIkwU7j5hYjiSzp8GR7hVBa4-zDDCjKrwXksYwOYTLb73EnVvtOjnDcHtZpr5ZAgHR827ymlsClwJY0__Q2loIOmc9FcWXrn83PlIbu6LUHiCwZoUpIgiopGsVt1B8n86ppbFCOuBe0VHEtYCYp_k_esahyqPkszcR7tGvj1aby9mgwm8y0BgUp4cBWW1ODvuKzsQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f5184a4d.mp4?token=Dn_xgVnwSo20JbMjwIKfZM8lPGnY6FZS59GW6JtpC6go3-raFKL-L84de1NoDwdUWOwRtZxeXqKClqsLqpoKpthzA7Lyxk5R4dT3Ve-2dX28HQGE0imQI7l-uqRyjqBSnBOFV4rD0ig_D8m8HPIkwU7j5hYjiSzp8GR7hVBa4-zDDCjKrwXksYwOYTLb73EnVvtOjnDcHtZpr5ZAgHR827ymlsClwJY0__Q2loIOmc9FcWXrn83PlIbu6LUHiCwZoUpIgiopGsVt1B8n86ppbFCOuBe0VHEtYCYp_k_esahyqPkszcR7tGvj1aby9mgwm8y0BgUp4cBWW1ODvuKzsQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خبرهایی درباره وقوع انفجار در ریاض
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/697842" target="_blank">📅 22:09 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697841">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
دو کشتی متخلف دیگر در تنگۀ هرمز هدف قرار گرفتند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/akhbarefori/697841" target="_blank">📅 22:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697840">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a4636fc05d.mp4?token=opX1XDQ322HW0Md31hqm4H7X-UhziTc68XI17tMjZEN2Ted-b5dJiNaGQmGGLVqgPZS6EsDlK2ISaUGE_8Kb37r1lmWiXMYqDfrFuXDUOehpP6OkoKhxkDec8-fpuAM0Hl44BwTm1TF_Ellqa1PkR78tJvQ0fPK_XlnQrnLrMAHi9iIs-QpKnkxkl30THjNyQsHAo8KyqwbOIUp0v_9uDBJprI1UsoNTXxk6yzbnmS3kekhepM45y2inmT-RMn-4QWOc_xrUcOgS3s_1RMNSh7Z2v7Ra-fveLaRC26B_XyLq-CkUlATx8f3cV1JqbAIUB1Q9OKsDux1defXxA4eocg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a4636fc05d.mp4?token=opX1XDQ322HW0Md31hqm4H7X-UhziTc68XI17tMjZEN2Ted-b5dJiNaGQmGGLVqgPZS6EsDlK2ISaUGE_8Kb37r1lmWiXMYqDfrFuXDUOehpP6OkoKhxkDec8-fpuAM0Hl44BwTm1TF_Ellqa1PkR78tJvQ0fPK_XlnQrnLrMAHi9iIs-QpKnkxkl30THjNyQsHAo8KyqwbOIUp0v_9uDBJprI1UsoNTXxk6yzbnmS3kekhepM45y2inmT-RMn-4QWOc_xrUcOgS3s_1RMNSh7Z2v7Ra-fveLaRC26B_XyLq-CkUlATx8f3cV1JqbAIUB1Q9OKsDux1defXxA4eocg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
توصیه یک پرستار به مردم: تغذیه خوب، ورزش و استرس را جدی بگیرید!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/697840" target="_blank">📅 21:58 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697839">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a6N302k0Nza3nV1Sfls9-dPilV33nHH62vlq37C6gGfhAGIYd_tiPdmV1f5DmVhmHMSAA26p-AE0NShyviMXimtRQ7Jf4u1eClgVmkYdi6tHLUUeVyxcqgz253qjsyRm0NT3hpFXtZe1844pnZPkzoaHBHh1OtuvSHdzeZP67q10ZCGLvYLBOi9NY-E4BQJjRBCY8qu8JwO1bcfnnqa_6BGI_NVMtzJh2uSJZPuXVD2FrEMJeBtWvkp2nYvMl1oAgDZ8xT1I3jcxOsDAZW0c92eLyl2mT4tXE1lJdP7rR0fMQRM26kfnUjsyClPvuIJ6TS7Pls__gopqclGmc-dTBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دارو در محاصره گرانی و بدهی | قیمت‌ها تا ۴۰۰ درصد بالا رفت | بیمار هزینه بحران را می‌دهد
🔹
افزایش چندبرابری قیمت دارو، تأخیر بیمه‌ها در اعمال پوشش‌های جدید و انباشت مطالبات تولیدکنندگان، زنجیره تأمین دارو در ایران را با فشار فزاینده‌ای مواجه کرده است. همزمان، اختلال در حمل‌ونقل دریایی و دشواری واردات مواد اولیه، خطر کاهش تولید و کمبود برخی داروها را افزایش داده است؛ وضعیتی که در نهایت می‌تواند هزینه درمان را برای بیماران سنگین‌تر کند.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3251849</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/akhbarefori/697839" target="_blank">📅 21:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697838">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
محمد البخیتی، از مقامات ارشد انصارالله: یمن از هر تحرکی در عربستان با هدف سرنگونی محمد بن سلمان حمایت می‌کند؛ چه مردمی، چه مخالفان، چه از داخل خانواده سلطنتی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/akhbarefori/697838" target="_blank">📅 21:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697837">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/697837" target="_blank">📅 21:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697834">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mX-X9AUJO3TfmuplxxFyM2lhUUwMMKxullFZMhosDyzcA--OvcIVrR3mM7VqpbULV9VeOz0mf_QzwTWj_9mxMO4ZRFadDtRoDvfkgWnZS-B8T2WEjDCUj4dwdQVuzJfK-_EHEsxA7Xgk8M_jY5TJI-ajMqQknGaTYXc5iJGDom-ZSk73tJ-7xoxzYuOlnWjfm8GtgTCuWQqCbWFffLfllVnRruMYiQiYPoSwl3vWcFOOAulcdE51o6P8wPPxR4C3yseJ2rRLyoJGDOQGcosNrZOdIWDhzTocxgI9wC7EZ-MRM-PoDne7uLhZCdT3o4XxBuquOT9eWXUwQZe1XzNRrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hyO5f9mQSPyYALSBt41v1RZrcO4NIM8RTDDBdp5j0-RC6pdXW2gBBoLhATIT0LBaFvKhlV8e4gS5wP7MZwL8oY30l644-vP8QvWDA6R-19D2mE8-_7EdynZtXN3-_09WifDjO0d1fWHOxYGMXfO6SkcVq_1UtABNLbiFuwHC9P4Nvsqpl-oe9iSeJh_3a0jU-X3RtC5k35tWJ9d23N-BmlU1gaGnOEkQLrAHxyz1dzimixHAypYrOiJvbhSGxgMAKiodjSWwYlM-nVNFfEybALrPKn2t4-uq04RuNwX-fSV6dTF2HYoLxId9PmQu-duazdkt-wyrChxR9gXwR6avrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lu5NvITSo8meRzc2rNrlIyBEysP7qblf6751pnll31pbyvWKsi6J3KRHw5faQzMYj-jhKrDreL5WUirLBc9LCjA5DoT1qqo7_m40jvBCy8gXhjX5B8T2SAannVy3DuHxI2WOb1QasihgjTNWtpNme8uXfk3AjowNWIsH7ZJ6FIDxONnpiCkVJJv236pBgPTpBfm-x3ZrwPp69tZEcPmT-tDTWhaQec3cKvvx7R4RVJkv7I2fsFYOOKbvle6roHqwJmxWIZCyqJP7bRh2FiGFiY2HOqntQihUlrvAgrUEXZqp-rKqnbukK03fBtcHBrQWKhwiXgeqp-VgCt56Mts7YQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
۶ مدل دوغ مزه‌دار خانگی
🥛
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/697834" target="_blank">📅 21:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697833">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
اتوپلازا؛ تجربه یک سبک زندگی متفاوت
امیرحسین افراسیابی‌پور، معاون استراتژی و کسب و کار ایران نوین:
🔹
اتوپلازا قرار است مقصدی باشد برای عاشقان خودرو و فرصتی برای خرید آن، چه خوردوی صفر کیلومتر، چه کارکرده.
🔹
در اتوپلازا، تمامی خدمات اعم از خدمات پس از فروش، اتوتیونینگ‌، صافکاری و بسیاری موارد دیگر انجام می‌شود.
🔹
استراتژی ما به غیر از بحث خودرو، ایجاد فرصتی برای تجربه یک لایف استایل متفاوت برای افراد است.
🔹
افراد علاوه بر دیدن و مقایسه خودروها، با امکانات در نظر گرفته شده نظیر فودکورت، سوپرمارکت و ... می‌توانند با آمدن به این جا یک سبک زندگی را تجربه کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/697833" target="_blank">📅 21:50 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697831">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8bd6d50b8a.mp4?token=T4F_XtvihN5lRqvfhWJerlPtUfWoLZMdnHwy0zewohV2DFNeNBCrvFbpEQeREimr-qshNznY59oqttmhmMo0JPmANDFcFQAiVd1OFYlTbm-gsHN_IyZXZTS8t867krs9ZDQZ1EIzcSfqHt8HhBtseIg5FvyF15uhflIFEQ2RJZpVMH8PT9PLPYexaf_UwWPr4jjxt6Z1lqnmHFzM0KgUnKbsKl_qMdLaYIQOqwKVbv9nCANGlYrkFJliSMH9mGBj2FxQ339uco7We2uJKwptRDPWOk8Ad7bjQ8P5Y9BGqOTohE5blLWCP49_Hy-F3vEe7hbRmC_pui50-MYqQVTX_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8bd6d50b8a.mp4?token=T4F_XtvihN5lRqvfhWJerlPtUfWoLZMdnHwy0zewohV2DFNeNBCrvFbpEQeREimr-qshNznY59oqttmhmMo0JPmANDFcFQAiVd1OFYlTbm-gsHN_IyZXZTS8t867krs9ZDQZ1EIzcSfqHt8HhBtseIg5FvyF15uhflIFEQ2RJZpVMH8PT9PLPYexaf_UwWPr4jjxt6Z1lqnmHFzM0KgUnKbsKl_qMdLaYIQOqwKVbv9nCANGlYrkFJliSMH9mGBj2FxQ339uco7We2uJKwptRDPWOk8Ad7bjQ8P5Y9BGqOTohE5blLWCP49_Hy-F3vEe7hbRmC_pui50-MYqQVTX_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا دو تا مستی دارن
هم زهره‌ماری سگی
هم قرص اکستازی
ابر انسان تاریخ و رهبر آزاده‌گان جهان
در سخنرانی‌های مختلف بارها از سقوط آمریکا و آزادی قدس شریف و مشخص شدن بی‌فایده بودن مذاکره با آمریکا و دولت‌های غربی گفتند اما باز عده‌ای نپذیرفتند و...
و این امام حکیم و پیش‌بینی کننده دقیق و عالم بزرگ در این سخنرانی می‌فرمایند؛ اونروز من نیستم، اما شما هستید و میبینید
ای رهبر شهیدِ عالی مقام دست ما را بگیر و راه به ما نشان بده
ان‌شاءالله قدر پسر ایشان، رهبر علیم، خلف منور و با درایت و با زکاوت ایشان را بدانیم</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/697831" target="_blank">📅 21:43 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697830">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N8k0l0Z6l54v8aZt1ynRkNrw26vfgDXeDHXC0Wl9MYLPfBFgjRM9SU3NJ3wLutXzviZUT4RaebymCRUSefh1RCo4i43ob1n_MV0Nh5Tb1zAYuRx2oAbnzb3Yg22KTzz15UfIQAgdMpc9V5ub3Ce1TFLBKRAdfbBPxhjpr32jFJQ4RhPNtt3EVtsaMJ2fQbVsvHBWD9OyOlLfb2ajUmEXt4S-imkTSS8Ci4jvn9hQ02RbXOs9jixxIyeSUiG5iLkLoy9Ys_M6gHHTShmBqUByYXP2IInH7uevreRfPYbe9O77KTtmp4W5ldAG9c71hJShm6vqCYbSamrIDYWE9JtMgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلوهن میزراهی به نقل از مجاهد یمنی: عربستان سعودی آتش‌بسی یک‌ماهه پیشنهاد داد، اما صنعا آن را رد کرد
🔹
یا باید راه‌حلی جامع برای جنگ حاصل شود، یا جنگ ادامه پیدا می‌کند، یمن برای نمایش‌های استعمارگرانه وقت ندارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/akhbarefori/697830" target="_blank">📅 21:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697828">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
خبرهایی درباره وقوع انفجار در ریاض
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/akhbarefori/697828" target="_blank">📅 21:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697827">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">♦️
رئیس پارلمان ترکیه: پیمان دفاعی «مکه» علیه کشور مشخصی تشکیل نشده و حتی ایران نیز می‌تواند به آن بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/akhbarefori/697827" target="_blank">📅 21:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697825">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
لیگ نخبگان آسیا | توقف تراکتور مقابل نماینده قطر در دومین گام
🔹
تراکتور ۰ _ ۰ الشمال قطر
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/akhbarefori/697825" target="_blank">📅 21:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697824">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
اتوپلازا برای خودروها شناسنامه دیجیتال می‌سازد
مهدی معظمی، معاون نوین‌ ونچرز:
🔹
در حال حاضر اکوسیستم دیجیتال اتوپلازا را تهیه کردیم و قرار است از آن رونمایی کنیم.
🔹
این اکوسیستم دیجیتال شامل تمامی تجربه خودرویی است که کاربر در فضای دیجیتال می‌تواند داشته باشد از بحث خرید و فروش تا بحث بیمه، خلافی و ... .
🔹
نکته مزیتی اتوپلازا نسبت به بقیه پلتفرم‌های موجود این است که شما عملا یک شناسنامه خودرو برای ماشین خود می‌توانید داشته باشید؛ چون این سیستم صفر تا صد خدمات خودرویی را ارائه می‌دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/akhbarefori/697824" target="_blank">📅 21:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697823">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">♦️
بلومبرگ: با تشدید حملات، نفت‌کش‌ها از خلیج فارس دور می‌شوند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/akhbarefori/697823" target="_blank">📅 21:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697822">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba0abd97f.mp4?token=lS8-rS2bGxG_Xi7-eu4LRMG3-1AQKQW1-1dBx50l7kdiVsby8BwrrbL8jbg0nn5YTBju-Y3lyzo3UoNZd_dj_XMaiJHq_i9v-arT-S_FH8YHJh1SHG_1U6kav3c4gRKUEBgoSqFfywy7rVTBh8zTiFg2X6SRUm0mryThKf3jY1XyMZWHj2TJ7AY7uDjWsDs8AuSHDVr_NjFZsrP8nAeLMmxL85WUUN2nQYwZQ4M5RdWv4BQOSSoXtRkA-kN8vnXB8iLzRPnSdB4V4hTQgx1hHTS_erjUAI2gHZ9SDRWrndrkqgxiyo4a8-P-ZldLzB07UWbXPVaodZewEKQ0fDxjBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba0abd97f.mp4?token=lS8-rS2bGxG_Xi7-eu4LRMG3-1AQKQW1-1dBx50l7kdiVsby8BwrrbL8jbg0nn5YTBju-Y3lyzo3UoNZd_dj_XMaiJHq_i9v-arT-S_FH8YHJh1SHG_1U6kav3c4gRKUEBgoSqFfywy7rVTBh8zTiFg2X6SRUm0mryThKf3jY1XyMZWHj2TJ7AY7uDjWsDs8AuSHDVr_NjFZsrP8nAeLMmxL85WUUN2nQYwZQ4M5RdWv4BQOSSoXtRkA-kN8vnXB8iLzRPnSdB4V4hTQgx1hHTS_erjUAI2gHZ9SDRWrndrkqgxiyo4a8-P-ZldLzB07UWbXPVaodZewEKQ0fDxjBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
♦️
سناتور کریس مورفی: ایران در چند روز اول جنگ، پایگاه‌های چندمیلیارددلاری آمریکا را با خاک یکسان کرد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/akhbarefori/697822" target="_blank">📅 21:23 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697821">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/282047dccf.mp4?token=cChv0Nlo6w08Nga8Naoqpn6VD2fKXNz2Yf3qqSrbCDN4aVJJFQiBXey-ZyjBjMc0kpG3i8d1V15w2LAxRCbYkPxMMYzKG3HdiVHFI4xjIlC09jQ9Oe2hsbtnBE6ftwO8XzeUYAaFrt6sahdVCxQlTfN-9n94pBRBSb0KvCmTgf6IT9Dxm8RPFBEjOwyMeRXNSWW92ifgvTIVQWrjbMQsdhzLOCgSABpdR8m1mvOr_Pgn85SOuV4otXlQlbO5dkdLbA68KLgsggdwvqh-83G_2sU0Czinf6GzlMwU2xmZq56XGLCV4Yvk0qqcZHTRZ67AU9AL5I7E_fYcepG565eiEVWdhP9-FYTQp-M-ErJgAHULZbG9o3ah8n-maBnSuyr1V5fP3b-YjcQa4Ui0sZfiXYdLnCdChdmZLdse6kUQO2CcAQjUQ6PW3s0ZmjUJcF0NtzQL6-31EMCITPmffRdYLUeDRXN1ZStJj1eyYKRW-C__m7UQ1Fh-Um6doaoaNBqtn0UCXTDOfuqqBoIrdQRlNz9qBfpuBQCn619JSUgB_Kom1Od-LMc9tJPMRa9gGMIkBjZ5I_6iyafZUt6OpK6banUlHc5QTT5NfrC688ZkUvkiLcPDsA9IX-UFTxdgAJ53Nv5dPd_ul1UnZCkPA68sQHftU-q1MbNbAKSBgr3LAx8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/282047dccf.mp4?token=cChv0Nlo6w08Nga8Naoqpn6VD2fKXNz2Yf3qqSrbCDN4aVJJFQiBXey-ZyjBjMc0kpG3i8d1V15w2LAxRCbYkPxMMYzKG3HdiVHFI4xjIlC09jQ9Oe2hsbtnBE6ftwO8XzeUYAaFrt6sahdVCxQlTfN-9n94pBRBSb0KvCmTgf6IT9Dxm8RPFBEjOwyMeRXNSWW92ifgvTIVQWrjbMQsdhzLOCgSABpdR8m1mvOr_Pgn85SOuV4otXlQlbO5dkdLbA68KLgsggdwvqh-83G_2sU0Czinf6GzlMwU2xmZq56XGLCV4Yvk0qqcZHTRZ67AU9AL5I7E_fYcepG565eiEVWdhP9-FYTQp-M-ErJgAHULZbG9o3ah8n-maBnSuyr1V5fP3b-YjcQa4Ui0sZfiXYdLnCdChdmZLdse6kUQO2CcAQjUQ6PW3s0ZmjUJcF0NtzQL6-31EMCITPmffRdYLUeDRXN1ZStJj1eyYKRW-C__m7UQ1Fh-Um6doaoaNBqtn0UCXTDOfuqqBoIrdQRlNz9qBfpuBQCn619JSUgB_Kom1Od-LMc9tJPMRa9gGMIkBjZ5I_6iyafZUt6OpK6banUlHc5QTT5NfrC688ZkUvkiLcPDsA9IX-UFTxdgAJ53Nv5dPd_ul1UnZCkPA68sQHftU-q1MbNbAKSBgr3LAx8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عمر درستاران فرزند عبدالقادر، از عناصر گروهک تروریستی جیش‌الظلم، پس از دستگیری، طی روال قانونی و تایید حکم در دیوان عالی کشور به دار مجازات آویخته شد
🔹
حملهٔ تروریستی به مقر انتظامی شهرستان راسک، حمله به مقر سپاه شهرستان راسک، حمله به پایگاه پارود، حملات…</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/akhbarefori/697821" target="_blank">📅 21:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697819">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8511f449f5.mp4?token=Y7gZwwVRxc81A884Xz2SEKXiEHjfDJYvEMKGdiKMBqKeaxNYI8y53AS3GCNNNyuF1DS00V_OgX42K0qXs-JSQgvocBQHeLUn4gGyWSrFPQ9T9ryxz3VSTh8nFCEh07u_mKmyosDLNLVL9qoFkwi8MjuOFdi7zOfXqA_BYfnJ0u3XoB0Rlc7PmrJJLVCwoOyNGlygEPi2r_noDP4TQVTjzU2PByBI8HI5tjaxczBnyMjQuPrwO7q2v9yU5Zm5x-OjBkNSK1TE7204CtCb_dmrys3voSD_6Xt55xlH4evWUkC276lnwpJgDMxfkBVd5nVn1hNYrhMXBOpV9GRsLz5ifg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8511f449f5.mp4?token=Y7gZwwVRxc81A884Xz2SEKXiEHjfDJYvEMKGdiKMBqKeaxNYI8y53AS3GCNNNyuF1DS00V_OgX42K0qXs-JSQgvocBQHeLUn4gGyWSrFPQ9T9ryxz3VSTh8nFCEh07u_mKmyosDLNLVL9qoFkwi8MjuOFdi7zOfXqA_BYfnJ0u3XoB0Rlc7PmrJJLVCwoOyNGlygEPi2r_noDP4TQVTjzU2PByBI8HI5tjaxczBnyMjQuPrwO7q2v9yU5Zm5x-OjBkNSK1TE7204CtCb_dmrys3voSD_6Xt55xlH4evWUkC276lnwpJgDMxfkBVd5nVn1hNYrhMXBOpV9GRsLz5ifg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
یه اشتباه بزرگ که خیلی‌ها موقع آرتروز زانو انجام میدن
🦵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/akhbarefori/697819" target="_blank">📅 21:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697818">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
صنعت خودرو در قاب یک تجربه تازه با اتوپلازای تهران
🔹
اتوپلازا تهران، با فضای نمایشگاهی و حضور خودروهای متنوع، تصویری متفاوت از مواجهه با دنیای خودرو پیش روی بازدیدکنندگان می‌گذارد.
🔹
اتوپلازای تهران با تلفیق ۹۰ شوروم تخصصی، خدمات کامل فنی و اداری و فضاهای تفریحی و رسانه‌ای، زنجیره کاملی از تجربه مالکیت خودرو را زیر یک سقف گرد هم آورده است.
🔹
این ویدئو مروری است بر دنیای جذاب خودروها از سایبرتراک تا خودروهای کلاسیک و نگاه مدیران آن به تعامل میان صنعت، متخصصان و سبک زندگی علاقه‌مندان.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/akhbarefori/697818" target="_blank">📅 21:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697817">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf871b5840.mp4?token=gRRFhrpHKNPIoiBEX9QzR_X9Ky6OQFT3p26ztXDEPcR3XlOciIxP5PGsHlqK0y-rkVUvMSuOMXW_ZY_MLxWqou0gEbsSReSMTZ2G4uGayaIaHJ5dmRxT_xeKJDNjSTF7zEXDPzYwbQ07-2TGgvoKLoKjAvps4yDl2ezqRNI9GbLRpgPsD_x-R7hqkgWglKaMRakRvpUykMF658GT4GR-L2FNe2fGiq0Z1ZGXZGp1MmS8i8DSfHmEc5V9diJ5XAmN88a7_esZCpOHmB6lJdYezF-EqDQ2RXg1jk0j3BhCO8oUa9R6tXOjKrmCE3xMXvYqW8H7i9VFELkOmh3H3ZNJ2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf871b5840.mp4?token=gRRFhrpHKNPIoiBEX9QzR_X9Ky6OQFT3p26ztXDEPcR3XlOciIxP5PGsHlqK0y-rkVUvMSuOMXW_ZY_MLxWqou0gEbsSReSMTZ2G4uGayaIaHJ5dmRxT_xeKJDNjSTF7zEXDPzYwbQ07-2TGgvoKLoKjAvps4yDl2ezqRNI9GbLRpgPsD_x-R7hqkgWglKaMRakRvpUykMF658GT4GR-L2FNe2fGiq0Z1ZGXZGp1MmS8i8DSfHmEc5V9diJ5XAmN88a7_esZCpOHmB6lJdYezF-EqDQ2RXg1jk0j3BhCO8oUa9R6tXOjKrmCE3xMXvYqW8H7i9VFELkOmh3H3ZNJ2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پوشاک گراد میزبان شما در نمایشگاه شیراز اکسپو ۲۰۲۶ خواهد بود
سالن حافظ
غرفه ۴۳ و ۴۴</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/akhbarefori/697817" target="_blank">📅 21:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697816">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">♦️
‌وال‌استریت‌ژورنال: تلاش حکومت سعودی برای تبدیل‌شدن به قطب هوش مصنوعی اکنون با خطرات جدیدی روبه‌روست؛ چراکه دیتاسنترها جزو اهداف [یمن] هستند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/akhbarefori/697816" target="_blank">📅 20:56 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697815">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/363ff53db7.mp4?token=YbRG-DbEQ_UXqUzG2GF6zTMMbC9kMyMExmdku3J9V_Ie9VLcA3Pntoj1NdFTuADRdcr9U8UZgWjkfeFOYTG-hNTs_4YoxPJNGD0EKsu-cs_IgnoXL-bChQXMLMIURX19dUoy_BBwgeSrIqjM8pS2-4IcrYHWbeLtl8_zkclO68ZeYadd-i5XSLhJl8vcwJGpgNHwdJeH7gegOdll2QcKzTz9QJs_6YVMuhYRkyp8IRNgqAsnckTPJACROuv_dDJLYoQgl1qro2bzH-ZORZz6PrKXZ87i1UEhie095-f4rk-3Vpa3D-cXARri9J9tZ13kpk0kitCxlSnKEr7KErfI3zE0ncIllGQj18JM3NFXCt7bdjS8_2fyOt8EDEQvIIk9JlM1CBNVFiZM_YZdlhyPJK6DjdKrM13I4wTX-0TWvhqXg9NkJzZqWpECDDFHF_iXPZ2k-nDIr_yU2NZGOhTeGSot7sUPgzfQm-xs2uUeJ3gOlxk58OXuBJxnZzQjjYRvKmqkSQfMgBZVgRYPaK5UyT3oWfq6ltVgThbkUEMTmmXztHBf_imrYZC3SXwl1Lxm5MFX731n5Uts7lWy0KdB0G0CR-mkkcvG83CVL7e0iJRYbo_pgFd_S4v_JavN6uEvDlVq0aV3MXALRmhwApEkAO25O0ne3ajpd2aIRBtbjMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/363ff53db7.mp4?token=YbRG-DbEQ_UXqUzG2GF6zTMMbC9kMyMExmdku3J9V_Ie9VLcA3Pntoj1NdFTuADRdcr9U8UZgWjkfeFOYTG-hNTs_4YoxPJNGD0EKsu-cs_IgnoXL-bChQXMLMIURX19dUoy_BBwgeSrIqjM8pS2-4IcrYHWbeLtl8_zkclO68ZeYadd-i5XSLhJl8vcwJGpgNHwdJeH7gegOdll2QcKzTz9QJs_6YVMuhYRkyp8IRNgqAsnckTPJACROuv_dDJLYoQgl1qro2bzH-ZORZz6PrKXZ87i1UEhie095-f4rk-3Vpa3D-cXARri9J9tZ13kpk0kitCxlSnKEr7KErfI3zE0ncIllGQj18JM3NFXCt7bdjS8_2fyOt8EDEQvIIk9JlM1CBNVFiZM_YZdlhyPJK6DjdKrM13I4wTX-0TWvhqXg9NkJzZqWpECDDFHF_iXPZ2k-nDIr_yU2NZGOhTeGSot7sUPgzfQm-xs2uUeJ3gOlxk58OXuBJxnZzQjjYRvKmqkSQfMgBZVgRYPaK5UyT3oWfq6ltVgThbkUEMTmmXztHBf_imrYZC3SXwl1Lxm5MFX731n5Uts7lWy0KdB0G0CR-mkkcvG83CVL7e0iJRYbo_pgFd_S4v_JavN6uEvDlVq0aV3MXALRmhwApEkAO25O0ne3ajpd2aIRBtbjMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تصاویری دیده نشده از شلیک موشکهای کروز ایران به سمت کشتی‌های متخلف در تنگه هرمز
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/697815" target="_blank">📅 20:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697814">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IQBoqYN5BBDAEJcjJcUlx8G5oslDtRlThGJF7AUnOu9JqEELKl3KX31L65P_iH1twb3ngzmp2bidDWMp1WIDgJmdKL5KFxtyks_cIe_ZnqQsTNLROkZpGldzbe2XssJ2W8T6493aCD64ic87BGpMH4r5hW7L-AlgF17902sG46ctcsUf0tMqno8LUw5fhWTVYePSvSpVjgqkqhOJnjt1bREA_Jb3Jm5tXocKxAz0qmThb_6s9kuD1jloLRe9xHXwoV571o8hdZHvDIIJ39xqKS9xyCJySmymnoiGQ9sPuRK_JwN5mKXSwHWWVKI2MATKRNiRK9LxoR-INti34fk8tA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سفارت ایران: مهلت دوهفته‌ای او به پایان رسید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697814" target="_blank">📅 20:42 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697813">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
عضو سابق تیم مذاکره کننده آمریکا: ممکن است آمریکا در تلاش باشد ایران را به حمله اول تحریک کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/697813" target="_blank">📅 20:41 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697811">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfP45LnWt-BHPdBFPncXAjcutrDYkGUp7pEORr_q4nVawq31b1qk2UdZTKeeQY64b4m-7NMHrwljrmFzknAOJxMLXLRvZ8Um53zXzL7U_crQhRnmdIXd0hqiTRTanE1vyUcbdg9a5aAAntVRwVTeMCopryS1wf0LUwFnBC7HOgUylEkAeLp5nRezvJ25bwVUmvueTZSwhgKeOPyOyRONgaD8x8P1H-d9_VJlDYplJYQn4JgP1nYnajY7dKM_0v7NU0Qh7jf-v_w7lNowEVUW8sIWRyO1pmBRCwZESYU2P2ctlqijMT1vlOOEjIowHfuXt3gG4Pbb7lc2QpF_EvDqrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bc8d410d.mp4?token=SV9SvB3P0JjcIb8N9MViMpUe5WUqXYbtKTRhoLHyQa2MQL3mICvkM4Ag8R4nNI1_3VCpOBdBC9GMpaPee3veeXcVdp3cpIk7mVZrmYE9GaXyLTKBhxFF6izEDlWZ-FI70U3smOR0HBDtw50UEQk6IxxVrWKF6RsKJvuIIjngg66r1IqpyywiluHITmbt7jhjiPRlEF0gTeywIBFLD7-tzW8CkVrmLJObV5bHH-jmBamt7HvvOY4PxBm0SNjUATiHZNCNmWUBghi2r8BgRaD-kkkNNJssahPdmCfyl_kcNKIlJUlNejjzwBisWjskqqQeJj8RrWr0wHF3fvWBhjsjxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bc8d410d.mp4?token=SV9SvB3P0JjcIb8N9MViMpUe5WUqXYbtKTRhoLHyQa2MQL3mICvkM4Ag8R4nNI1_3VCpOBdBC9GMpaPee3veeXcVdp3cpIk7mVZrmYE9GaXyLTKBhxFF6izEDlWZ-FI70U3smOR0HBDtw50UEQk6IxxVrWKF6RsKJvuIIjngg66r1IqpyywiluHITmbt7jhjiPRlEF0gTeywIBFLD7-tzW8CkVrmLJObV5bHH-jmBamt7HvvOY4PxBm0SNjUATiHZNCNmWUBghi2r8BgRaD-kkkNNJssahPdmCfyl_kcNKIlJUlNejjzwBisWjskqqQeJj8RrWr0wHF3fvWBhjsjxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله جدید یمن علیه عربستان سعودی و ستون‌های دود از تأسیسات انرژی در شهر الهفوف، واقع در شرق عربستان سعودی، به چشم می‌خورد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697811" target="_blank">📅 20:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697810">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
زلنسکی: قیمت‌ گازوئیل به حملات ما به پالایشگاه‌ها در روسیه بستگی ندارد؛ این موضوع به انسداد تنگه هرمز بستگی دارد؛ همه می‌دانند!
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/697810" target="_blank">📅 20:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697809">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">♦️
شریعتمداری، مدیر مسئول روزنامه کیهان: کابل‌های اینترنت جهانی از زیر آب‌های تنگه هرمز و خلیج همیشه فارس برایمان دست تکان می‌دهند می‌گویند؛ چرا نقش ما را در این جنگ فراموش کرده‌اید؟ ما نیز در این آوردگاه، جان‌فداهای امام راحل، آقای شهید و امام حاضرمان هستیم‌
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/akhbarefori/697809" target="_blank">📅 20:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697808">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1198c495c.mp4?token=rgK2qbgxUoBRll2PXP5qYccleVmKH_KRTp-VqLfOeMpE9Tg0GKFpctZqfOmQLX5FQd0bbqNYaa8A3jjwmDsYGPVjpb5mP1nRsfMMKh0VZ0eM733fdkiksyUAjSO7n3SaQCKW85puZTnlV18a2XKQG551R41t-tCoEF80GdFvvALRHmpRmLt9sdjR6gd5fnRvkPB0BM0Jdre93fLSOdktNRElEJF85p6uT30-ZtI3EwdBMsRhZGY-6XJa-iWJSF0kPe-y-9Gf5FtORplq6MGAye2O6WKvVHvYdNNW13bIOXnwnoOmt5BxEypJesDt6Ecl3gIjdCF2whMHXR3YEALYKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1198c495c.mp4?token=rgK2qbgxUoBRll2PXP5qYccleVmKH_KRTp-VqLfOeMpE9Tg0GKFpctZqfOmQLX5FQd0bbqNYaa8A3jjwmDsYGPVjpb5mP1nRsfMMKh0VZ0eM733fdkiksyUAjSO7n3SaQCKW85puZTnlV18a2XKQG551R41t-tCoEF80GdFvvALRHmpRmLt9sdjR6gd5fnRvkPB0BM0Jdre93fLSOdktNRElEJF85p6uT30-ZtI3EwdBMsRhZGY-6XJa-iWJSF0kPe-y-9Gf5FtORplq6MGAye2O6WKvVHvYdNNW13bIOXnwnoOmt5BxEypJesDt6Ecl3gIjdCF2whMHXR3YEALYKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بعد از حموم چجوری موهاتو خشک میکنی؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/697808" target="_blank">📅 20:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697807">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
بارزانی، رئیس اقلیم کردستان عراق، تأیید کرد که میانجی ایران و آمریکا بوده است/ ایران همسایه ماست و این جنگ، جنگ ما نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/akhbarefori/697807" target="_blank">📅 20:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697806">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5Rl7OsWxnlqMu2l72eK_eCyckXaArXUuu5igAEwVgxMmxvSzV7-FvhC2cnO35iqQfTV1zsUabW18FZXpVX62xd8w-DV1-iEAP8XxapCl5WlCn1F53Uj9NT-suqxDqBshVjTXQvj9WmyoaoLAq4-E_bCkdttGhOApyMFLwt-Ik87ioUA3N4k7RVDM6doFm4DIjTnemJXLGZTqsmfbYW0BMkZplvltmhHKnTMaTdcuyLSOKCLOIz4mnO6VP4iTYAKGxUtzn4U0x767GYYBqqvgWTh0-oxg52URo08h5AZNvGwAOgNvLji236E7iG1Z_dMW0yXIedMbT7kv09xfu0gcXDk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/147c7ee345.mp4?token=lm5jdjyqAJVYkJ2BOyUNwfprdrUJT6fNod_F0mNz8CBV5HbOuhLFb0oe2ORsvLJURcDMbqLKEaSZ5EoGg7aGl0-lr_K6NwsqARSkwd0wvOiu_V2Aml52V6uznmo5DQu2801Q8sihDl5lo5rCY_X7HlhDyFeqHo3KOGM0iTPmCV0imWCJfsisuUhtXyZEkzVgy8ZNTY28uJyE6SXUz5bvAD_iJqd95W7vOuRYNlSosl8Gwuxsfe4Nwp9rM9bLDPz0m-nTMTNtwqVirytlFzZNuXSgJ9woY_le14X2TyYLdFMKAA_DD6eY_Is6jYRzCSw4SI6ontLlsDFp7j-IY8Ws5Rl7OsWxnlqMu2l72eK_eCyckXaArXUuu5igAEwVgxMmxvSzV7-FvhC2cnO35iqQfTV1zsUabW18FZXpVX62xd8w-DV1-iEAP8XxapCl5WlCn1F53Uj9NT-suqxDqBshVjTXQvj9WmyoaoLAq4-E_bCkdttGhOApyMFLwt-Ik87ioUA3N4k7RVDM6doFm4DIjTnemJXLGZTqsmfbYW0BMkZplvltmhHKnTMaTdcuyLSOKCLOIz4mnO6VP4iTYAKGxUtzn4U0x767GYYBqqvgWTh0-oxg52URo08h5AZNvGwAOgNvLji236E7iG1Z_dMW0yXIedMbT7kv09xfu0gcXDk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
سفیر پیشین ایران در بیروت: پیجر من قبل‌از انفجار به‌صورت فینگلیش نوشت «یک پیام فوری دارید»
🔹
اولین‌بار بود که با چنین پیامی مواجه می‌شدم؛ روی صفحهٔ پیجر نوشته بود که «برای مشاهدهٔ پیام دکمه را فشار دهید» و به‌محض فشاردادن دکمه، پیجر منفجر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/akhbarefori/697806" target="_blank">📅 20:20 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697805">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
۶۰ کشور طی بیانیه‌ای مشترک اعلام کردند متعهد به آزادی کشتیرانی در تنگه هرمز و مخالف با وضع عوارض بر کشتی‌ها هستند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/akhbarefori/697805" target="_blank">📅 20:18 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697804">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0943e68ce3.mp4?token=aQH5IODBeiJ1kiSuzdZPN5BSPVXmdHGDQzA360imeMgoUmi5fKK03Vvsxg4KzqPdkXfN5NGERsXKGz_WM59Z9t5Id-F6C4zcT-B8N0KZZdV-VQAGGzQ9T9WlSi2RibaeiQKHORLP9zfxbj3rN197_2PimHqG4xBFYgNMRharFS8apPN7Q6XyAD_CzDpJQj1Ez3aC5HU5aLPZqN83ktq3UdE1s3mOEpHhRVHhuod_uCYSLIt0YeMYJs0YuA6bgiyLykprYnOyXVXQuy4ch-rhNgJLM1c9OX9IVAbPBZQE9psAZbKxkCwt5oFota5YjDNJdUPtSyYVloT52ZeGiKyf-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0943e68ce3.mp4?token=aQH5IODBeiJ1kiSuzdZPN5BSPVXmdHGDQzA360imeMgoUmi5fKK03Vvsxg4KzqPdkXfN5NGERsXKGz_WM59Z9t5Id-F6C4zcT-B8N0KZZdV-VQAGGzQ9T9WlSi2RibaeiQKHORLP9zfxbj3rN197_2PimHqG4xBFYgNMRharFS8apPN7Q6XyAD_CzDpJQj1Ez3aC5HU5aLPZqN83ktq3UdE1s3mOEpHhRVHhuod_uCYSLIt0YeMYJs0YuA6bgiyLykprYnOyXVXQuy4ch-rhNgJLM1c9OX9IVAbPBZQE9psAZbKxkCwt5oFota5YjDNJdUPtSyYVloT52ZeGiKyf-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
جان مک‌آفی، برنامه‌نویس در سال ۲۰۱۹ پیش‌بینی کرد هوش مصنوعی طی ۱۰ سال به پیشرفت عظیمی می‌رسد و در صد سال به دشمن بشریت تبدیل میشود: ربات ها قدرت می‌گیرند و چاره ای به جز بمب اتم نداریم
🔹
او ۲۰۲۱ در زندانی نزدیک بارسلونا درگذشت ۱۷ ماه بعد ChatGPT منتشر شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/akhbarefori/697804" target="_blank">📅 20:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697803">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a30c6a92d4.mp4?token=r2AkJEOXTxHkz1bRH8jyrSKae3H0sIepKCD36WBbp-OLFZwb2g_cYVdWh_fTjyuKzd8NcwE7pPh48D_ZyVayLsPbgl-K1sCAxLQJNF3KSkWjKYQcG5qOa7NqXwS1TWqA6OSUYZq7YsNxeJstaO5h4H5svJvSoWBbZYRkwaSeY_3Aw-tUXZ9-4Q3-DexaVOLJwkZvQx42qDdax8f1T5scEHIGaR2skxajpmKu2vj6kvy7H-qc2DnwbbfVWwqzSZD51EDKhaMINpL7i_V2GwsrXk-94LlUrnGh9TumU_r4uUbzBUER77bpezWOwYSGiQ01k2VY9wU9e0w6BG1CaMsFQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a30c6a92d4.mp4?token=r2AkJEOXTxHkz1bRH8jyrSKae3H0sIepKCD36WBbp-OLFZwb2g_cYVdWh_fTjyuKzd8NcwE7pPh48D_ZyVayLsPbgl-K1sCAxLQJNF3KSkWjKYQcG5qOa7NqXwS1TWqA6OSUYZq7YsNxeJstaO5h4H5svJvSoWBbZYRkwaSeY_3Aw-tUXZ9-4Q3-DexaVOLJwkZvQx42qDdax8f1T5scEHIGaR2skxajpmKu2vj6kvy7H-qc2DnwbbfVWwqzSZD51EDKhaMINpL7i_V2GwsrXk-94LlUrnGh9TumU_r4uUbzBUER77bpezWOwYSGiQ01k2VY9wU9e0w6BG1CaMsFQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اعتراضات دانش‌آموزان مسلمان و والدین آنها مبنی بر ممنوعیت ورود دانش‌آموزان با پوشش اسلامی به مدارس در آذربایجان
🔹
بیش از ۹۵ درصد از جمعیت آذربایجان را مسلمانان تشکیل می‌دهند و معلوم نیست علیف به چه علت این تصمیم را عملی کرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/697803" target="_blank">📅 20:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697802">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">25-1 Ane Manaee (1404-02-14)Shahre Moghadas Ghom</div>
  <div class="tg-doc-extra">@Aminikhaah</div>
</div>
<a href="https://t.me/akhbarefori/697802" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
تفسیر سوره محمد| جلسه بیست‌وپنجم؛ بخش اول
🔹
واگن‌نشینان واپس‌گرا؛ عقب‌گرد به حیوانیت پس از هدایت، با "تسویل سازی"و "تلقین تدریجی (املا)" شیطان. [01:08]
🔹
تأملی بر ابتلای حضرت یونس و قومش، و سنجش "توقع" با "تفضل" در ترازوی الهی.   [12:28]
🔹
تمثیل قطار هدایت و استعاره واگن‌ها از سطوح قرب به خدا و انسانی که مسافرمسیر تقوا ست. [19:40]
🔹
فهم اینکه "در موقعیت خوبی نیستم" کلید رشد معنوی و آغاز تغییر و رحمت الهیست. [26:57]
🔹
استغفار، گشاینده درهای نعمات مادی و معنوی [31:00]
🔹
جلوه‌های خلقت الهی در دنیا، مُشتی ست نمونه خروار در برابر صحنه‌ی هنرنمایی بی‌پایان او در بهشت [34:36]
🔹
ثروت، شهرت و ظواهر دنیایی؛ عامل فریب خوردگی انسانِ محروم از حکمت حقیقی. [37:53]
🔹
هر چه انسان به تقوا و اخلاص نزدیک‌تر، مسیرش خلوت‌تر، سخت‌تر و پرمقاومت‌تر [44:46]
🔹
”خلوص نیت” تنها راه رسیدن به قرب الهیست. در این مسیر، رضای الهی محور همه چیز و فراق از محبت الهی بزرگ‌ترین رنج است! [49:40]
#تفسیر_سوره_محمد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/akhbarefori/697802" target="_blank">📅 20:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697801">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff025506a2.mp4?token=EkBHKd00OTCuYs-w5kR25AepKZ6ya7Qj8bCngXFe9iwEkHODhTLnWIegggSoJbN_MYuvLuZZnOtRBya201hM659sfBgGSlfRPdgc7XEPQ_6AeXGhjR5omJ-l2Ft2LRUHkvddgKGa4_LhHHTpa87hrt_uC974fPtseooaPcJmneLwfrbqRiOF_FG1yvXEMtPY7UFoCFJkTJiIlJSoBGliDLGZ_7PkBDlSzeGq9r4P_qyomeuOBgsflCd9MN-ueYAlpvM0xt0hjUvmyCSbxfCE8tWgWedQdtlLDGjP6f6cdNhR-qoYFs8Zx7eywBan7g-y1N3z0ijk0KV9d6Mb6Y_otg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff025506a2.mp4?token=EkBHKd00OTCuYs-w5kR25AepKZ6ya7Qj8bCngXFe9iwEkHODhTLnWIegggSoJbN_MYuvLuZZnOtRBya201hM659sfBgGSlfRPdgc7XEPQ_6AeXGhjR5omJ-l2Ft2LRUHkvddgKGa4_LhHHTpa87hrt_uC974fPtseooaPcJmneLwfrbqRiOF_FG1yvXEMtPY7UFoCFJkTJiIlJSoBGliDLGZ_7PkBDlSzeGq9r4P_qyomeuOBgsflCd9MN-ueYAlpvM0xt0hjUvmyCSbxfCE8tWgWedQdtlLDGjP6f6cdNhR-qoYFs8Zx7eywBan7g-y1N3z0ijk0KV9d6Mb6Y_otg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تو هم همیشه با برگشتن نوار لبه وسایل چوبی خونه‌ات مشکل داشتی؟ با این ترفند آسون خودت تعمیرش کن #ترفند_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/akhbarefori/697801" target="_blank">📅 20:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697800">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">عرضه مستقیم و بدون واسطه انواع فرش و تابلوفرش دستباف، با بالاترین کیفیت و قیمتی استثنایی!
با حمایت از کالای ایرانی و هنر دست هنرمندان برجسته‌مان، زیبایی و روح هنر اصیل را به خانه‌تان هدیه دهید.
✨
چرا باید سر بزنید؟
حذف کامل واسطه‌ها و تنوع بی‌نظیر طرح و نقش
مناسب برای سرمایه‌گذاری و زیبایی دکوراسیون منزل
خرید مطمئن مستقیم از تولیدکننده
📅
زمان: تا ۲۴ مهرماه
⏰
ساعت بازدید: ۱۱ الی ۲۲
📍
آدرس: نیاوران ، خیابان باهنر ، خیابان فیضیه ، اردوگاه شهید باهنر
منتظر حضور گرمتان هستیم! برای کسب اطلاعات بیشتر پیام دهید.
📩
📞
09127599612</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/akhbarefori/697800" target="_blank">📅 20:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697799">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">♦️
دو درخواست پزشکی علیرضا بیرانوند، شامل آسیب کتف و ارجاع به کمیسیون اعصاب و روان، رد شده و او باید اول آبان به خدمت سربازی اعزام شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/akhbarefori/697799" target="_blank">📅 19:51 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697798">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1723a778d.mp4?token=IvHlzT2rnKGGrjbRhYEA9W72-A6p2E5TVKzTQ8cRb_bO16ZSIgHWqbEDHgKCiIj0bSdjJmqtZYmguKwoXlF1CCz6H7bVanHGhU3MseJLT3KV12hVrlvcHIvqB2Cf5_sM1li-ZsdfEQoVzFfraZJJC3XSn8Kr2ZzyrDp_8pDcRzIhA5eX9okXQeRP8SN9xMmFPEs_diK8KlZ9-9eQf77-VC7VLHVjcC1Tycr74rctnDGubs0KBt2--83PlzsXgU7sRK3ccfdxVfPzm93IY2TmIZ1t_1ZzJrhviBtRKQL-pbq2XgsK0Dbndr0lLZW58wCG6tXYbZMnPpMMV_H9GXWJzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1723a778d.mp4?token=IvHlzT2rnKGGrjbRhYEA9W72-A6p2E5TVKzTQ8cRb_bO16ZSIgHWqbEDHgKCiIj0bSdjJmqtZYmguKwoXlF1CCz6H7bVanHGhU3MseJLT3KV12hVrlvcHIvqB2Cf5_sM1li-ZsdfEQoVzFfraZJJC3XSn8Kr2ZzyrDp_8pDcRzIhA5eX9okXQeRP8SN9xMmFPEs_diK8KlZ9-9eQf77-VC7VLHVjcC1Tycr74rctnDGubs0KBt2--83PlzsXgU7sRK3ccfdxVfPzm93IY2TmIZ1t_1ZzJrhviBtRKQL-pbq2XgsK0Dbndr0lLZW58wCG6tXYbZMnPpMMV_H9GXWJzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عناب؛ میوه‌ای کوچک با خواصی بی‌نظیر
😍
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/akhbarefori/697798" target="_blank">📅 19:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697797">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
سخنگوی کمیسیون اصل نود: زمستان سختی در پیش داریم
🔹
پالایشگاه‌هایی که مورد اصابت موشک‌های آمریکا و اسرائیل قرار گرفته بود، فازهای بسیاری از کار افتاده بودند. قسمت قابل‌ قبولی از این کار جبران شده است، اما هنوز به نقطه مطلوب نرسیده است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/akhbarefori/697797" target="_blank">📅 19:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697796">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=WL16jTBCPV7dNUmN2vi-hixqGieU7Ft3dVyCCvREBCr5ObNpuOCamlQ6kN0zCni9aglDXNhnT9BR4O-EuOLz5DsKS6osaVwxibKdlcvxI_0lJpxv_7GLR5a2BzNF8thNYd-ewigUIgjSbtI_64nU-miMuNIkURNy29amSec0sbNkTROCRUFi_yMeWjQ-tckRy1cZfZ3dSOLjcqLPPDYgVwxpFqZv2Z5pFneeWVyEkdY2CNG9YBKGkrQlkis-vQ6082iC6ofTya7i9T_Xkg26hDy3TM_KtT9yeHGOGLMSSienJAac3jZTOQcmOs-DDu_MkRfRfw9rfDwBNsahnNjrdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/714fb5cb99.mp4?token=WL16jTBCPV7dNUmN2vi-hixqGieU7Ft3dVyCCvREBCr5ObNpuOCamlQ6kN0zCni9aglDXNhnT9BR4O-EuOLz5DsKS6osaVwxibKdlcvxI_0lJpxv_7GLR5a2BzNF8thNYd-ewigUIgjSbtI_64nU-miMuNIkURNy29amSec0sbNkTROCRUFi_yMeWjQ-tckRy1cZfZ3dSOLjcqLPPDYgVwxpFqZv2Z5pFneeWVyEkdY2CNG9YBKGkrQlkis-vQ6082iC6ofTya7i9T_Xkg26hDy3TM_KtT9yeHGOGLMSSienJAac3jZTOQcmOs-DDu_MkRfRfw9rfDwBNsahnNjrdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عکست رو با این کدها به هوش مصنوعی بده تا این خروجی‌های فوق‌العاده رو بگیری
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/akhbarefori/697796" target="_blank">📅 19:30 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697795">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W61gos6hn2oCux8QaFOGFodAwikIOELE73d1tdKRSWMt7GtIdtKe4lkmXhbccGMDQVJgXH62sASf74sKCvOoE9OmXwLD4U-5sze-2DbDhifJY0KBdkcP0bjqyxUcWAEd3QjVRKCaoGHdEzEbj6l5RJSf1hWUwuhrcEEnJM6YxKtLS59r5FEiNGoPCBLX7V7r_qFNQLtrsjRaLAMZAnXSpmkfhQGnQToOIqC7EgzHb91e4jIZ6BcWO2vGFfqmT1qcP2U_BnUdF7cNzY9fmJbHg6Q9GjSJv-ZTACywPpUtGpCIl83845Z6jbtDdaairNRPE5ZgHOwNr7TtP2IVUWENGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سازمان تجارت دریایی بریتانیا: گزارشی با تأخیر دریافت کرده است مبنی بر اینکه یک نفتکش هنگام عبور از تنگه هرمز به سمت خارج از آن، هدف اصابت یک پرتابه قرار گرفته است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/akhbarefori/697795" target="_blank">📅 19:29 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697794">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">♦️
ادعای لندن: حمله نافرجام به فرفورد به احتمال زیاد در ایران هماهنگ شده است
🔹
پس از حادثه فیرفورد، تحریم‌های بیشتری علیه ایران اعمال می‌کنیم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/697794" target="_blank">📅 19:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697792">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">♦️
رئیس پارلمان ترکیه: پیمان دفاعی «مکه» علیه کشور مشخصی تشکیل نشده و حتی ایران نیز می‌تواند به آن بپیوندد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/akhbarefori/697792" target="_blank">📅 19:16 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697791">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d32Bdbgd-A-ko0XBbtbEDfD7y8rPJOHH5mzzMIAeE2Fl1IhA3ZZ8GxswB8mzKJ3XerHxZwKoXH1cPXekabDRt5SLoeik0rC4ZmA6nrrEdtk_2d6HbGwpF9k6xXvirOx1d4ny9wgq8Z_QH89b_xO6srYs_o_C4plPAdBo0pm1I9DgRjYukFEjS8k1ByAb-P38WiL10Y1nai5QHHgiTkCq5oS4j7V0OI-5qZtv4Q6W8zqjZV9oNmDcHHHdARLBYpU3s_LsWYhwGwM3dtCAXHTBV-qZobLWLPqT904iR1H4GoDiYZlERBpveayRYeUGjGSNmnqDeDTP5e1TOn8KzPO7VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت نفت خام برنت به بیش از ۱۰۶ دلار در هر بشکه رسید
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697791" target="_blank">📅 19:15 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697790">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bFCWZxoWG1jX_itwuG1R-yUDXpZIhedcA38TSnJNizZ6K934Lmdy83FcsTVfjq-MB6t6m6PCR1SMVHRQ1QAsbVHlI-XbERjuc_MnD5krrIGEDTguNYmqH-kuKBf88Pfsgkpmdvr-4A9-dgOHzDDiHh9r04UsSK3u0WTOnR6PeWt8-Ld7TrTXbGTf8QdlSBHd-ZVJuKxzOinsNl4GPeJ3t-KTBNTjhY5eLN8JScMsyYo4BcQVCByv7TjQ00S3_NPRo6CAf8J0tcXe5lanzkrXiWCMYcSXoZDRF1tcLawsfElIzbOgK9hbt8JdWC0dxcRIpp2tOo6p2hKL_edzEKVfXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهار نوسان دلار در سایه محاصره اقتصادی | آیا فروش ۱۰ هزار دلار به هر کدملی اشتباه است؟
🔹
بانک مرکزی با آغاز طرح فروش ارز تا سقف ۱۰ هزار دلار به هر کد ملی و اعلام تزریق ۲ میلیارد دلار به بازار، به دنبال مهار نوسانات ارزی و کنترل انتظارات تورمی است؛ سیاستی که در روزهای نخست اجرای آن با کاهش محسوس نوسان قیمت دلار همراه بوده است. با این حال، تداوم این ثبات به میزان منابع ارزی در دسترس، نحوه قیمت‌گذاری و چشم‌انداز تحولات سیاسی و اقتصادی وابسته است.
گزارش خبرفوری را اینجا بخوانید و نظر بدهید
👇
khabarfoori.com/fa/tiny/news-3251807</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/akhbarefori/697790" target="_blank">📅 19:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697788">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eGhp240HHPaEbfiaD3k0XUohZNN6URA__HNU0h0zlEf9o9tpaG6rEqa-JXDwxAeMK8qJeqJFsqMI1jmXN-ViVQH5s8LtCLqKEVZ8o25YYOTZaBL88_vaJ2fAYRTPNYN8Qeacg2kVDrYoSNWORwssosxSjm4z78i2fu8SM8TTog0uJwoIonfxfwfj0zxmteOD4ZkH4_mtRnjYwAQ0YeBP_ILR4v3BLAadtKp1httE18GQkXvN6L2PB-hEU8D3cx2KuBHtp_HIETidM6XF3lfHUyJsGEQmqApRrjxLMZpTYTMwHcmOdNadYyR1zFnQK9p1WtuCooGZ4CXr8zTKbO3-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uRMdOxnd5J4XyK2E8bJNSff-sTPbMu-xzjM0QFz_624xgDfGDypvEob2WFdr6hFi-0HK6OxqpeJxwcM47I4bRH2G0OUPOV1tuahLdX1WX2HIZnSCiNKZYzR693d_kHJ427YghBPjJssonwmv3v9io8BmHzAcd69KRR5FwohVWdEqnz5I0YqB_kU5GcxZP4cQgOTIyMkKsJnLkXJI4jAbY2GRA1qcvAQsB-jpEQ4zMowTp0sjyz9zzkKu9wEGTDyxRsZnFBKOY3LRgJfVrxq5qBC7r3Ng8WieOkUinrVo40HKC2Ed9wFlI9ZXb01h5MAxgkST_GelCw_LCIU3xKd6gw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
گوگل از دستبند Fitbit Edge با نمایشگر اولد و شارژدهی ۷ روزه رونمایی کرد
🔹
دستبند Fitbit Edge با نمایشگر OLED حدود ۴۶ درصد بزرگ‌تر از Fitbit Charge 6، حسگر نوار قلب و قابلیت تشخیص ضربان نامنظم قلب عرضه می‌شود و با هر بار شارژ تا هفت روز شارژدهی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/akhbarefori/697788" target="_blank">📅 19:06 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-697787">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ادعای گاردین: پس از دیدار مقامات آمریکایی با یمنی‌ها و اطمینان از اینکه کشتی‌های آمریکا هدف حمله قرار نمی‌گیرند، واشنگتن از حمایت نظامی از عربستان خودداری کرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/akhbarefori/697787" target="_blank">📅 19:00 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
