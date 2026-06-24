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
<img src="https://cdn4.telesco.pe/file/ONWm_RBiQtHKKk4qpirnmPYnSDcPFu7acWTLAJ-_JCScXByFAjIZZjfKsKSQuUAFsPhFObPTrGNIVvUVArI2ninB2Jr-CEj5ejdOCkpirJUwvTPo5TAb67guXSPSWh_-Hge2T2DQNkYAY2-pt-7alXRP0K4fgsaD-j_wS7yCYqeptJmfMh8ZlR0CaXJjgd2oWqx0tg16n-ZaH4ZnYOKegg2olLM4oQhzro4kRT_N4A0Rwkzh-rLJ-UTuFumakpUhe7Kk786Vb_4iu8xYrYF-aaGtlFwOBQe3cG6IxJNaCRbhR-Nso_ERh_P8eXLoOEX2Yxf8Z9ShZg-a0dG7E5k7Ig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 314K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-03 13:27:32</div>
<hr>

<div class="tg-post" id="msg-24203">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bn8HVGbXprb6iz_jFb6ElXXyrz32umzbMaL1t8KzxWge21mWQ8N3WeKys6QtwdGEP_kjoEQhaLqxFlKCzSG7-nKpkb5C6ngiYwxEhM7d0Ld3dMCA7FjnXvcTfvusuJWUwMU09-LtyBTTwhEzqr8AC_iQwHfsMkH5obZT6lrZ5qJadXpg0t2OthbM7Ds5WthP97SKmcd68CIqKdFdClfI70FTdfrt46BOF-XzuGRbfc9jVXtnAAPeRE6GNrb0QtdSG-SLg15yq1Yd1Lmr5npeqfgHhOdO1ow8SAqq0tuvSUGDhchaAZpSgSDxoQO2QY4iGky13aCkPo8LrIvBdgDF9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.96K · <a href="https://t.me/persiana_Soccer/24203" target="_blank">📅 13:06 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24202">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZHUqv069rTkrqIomXc1-6XG0izO7JtK6_c3_GAFu1yJ9bRheaR9fpM1K6VK-lEekHo9Ibz98N3Qm9zUOwnDV8yWTvVfH_w7O76VJKrTK1uECrTBjkRflxpuiZFzS8IEuDfZ5ZtjnT3LvKJClsbgnFpWvyen25RQkSQSWpDdXwaTakvquZ6ALtS2Q9bhGd7eUj36IcGZuIDUiYBP__3U_lNirqUQMe-XsZwy-45-8-6CfGiX4URslL_MbQRNgTjnR4S-nBCSZmdHDpMxXZJv3alDggXbWaoXJws6FTHrdUvEkADRRolCrI8LhFPuhf5u6Wp9oCptBaQAZSTVV3ACoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/persiana_Soccer/24202" target="_blank">📅 12:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24200">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBGflQFANh9WP0Y8q_98wvkNTt0BAWqiPRKyvoSc5HhKXO-rcXS8V50zBTrIhmGjb4RM8ufJOqkF2fnCj--HgraXyseFzlZNd9irGLIH7Z67NXaaNdGOTrmPLKVcQomqsG5-kXKJlg46Y7pvnpH0fPhh4Otqp9q-cLVXQsLkheeDwBwtG23o-GEZqLyAgKWUPYM58GKPdzYjLgO27Q2yUtrTKqdDjg3WezSYUuxhrwatIm-AOmMNG4sT3oSW2gkV3K6WcUJh5VsJRHvB6vMaK7uWg55IFRQc1Qn8YSvH8s1zB4mX0APtA0UzgOmgOOYhnqvU98fP8LsO3SvTjUpSqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d824e9cab0.mp4?token=OQpINFtm7Il9SwGyzs5LgJT7qfbsoT-zT_iOGgsAXplecbxiyeoL-spQa_gvsO-Wc9qps9gP-5f3PEhQeHi6U63vHIHEr8V4dzFNr_cddaupNsa8jECxgAfAMU9ntt_8VW_jk-nYhAj0Dc7Vwrbb3cKKAZ9rYpEfZNIPaHoKdGaMB-KmPbk3A37jwNUsstDTd-JyWlDakWzJBytRmpjxe7B4tchMHXwlImXDLTne7l7HhbhOjDKj7ZUa04rmW2oG9U_PzaaSSNoD9L9BRHiGu5etcZeybOFtwbpA5rpwPR98I65GvIzXXjlDAKZiP5Yg7fwl4e6NpoQlErd9JbIcYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
اگه جدول رقابت‌ها همینجوری بمونه؛ پرتعال
🆚
آرژانتین در یک چهارم نهایی بهم خواهند خورد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/24200" target="_blank">📅 12:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24199">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NSTZJiDycVWlwVAbc8qEbtPcoOpSyva0MPzNnJGQ-ev9yHFMeBdN-82LbsJt6IYGzonFIal_FzX7DLBMsSpOnkiC8nJKC94EDzIZjfR2izebOwcvY-Rgpt2YZaNmIKKEZgl3diOiEarr-s5PUoCLvgU1eO5UVObCODH0Cnqsq5SSIUAe08w_OYme2HdaXSRhFqKLmjj6nkVPT6tChfWvuzyxSVc6-4z8wlvo6EepBzydheyPij48tIw7DaU9RX3zJDeUhED89VdGtKUOIJ5h4WVg9TkEKZcZrgiepLO1MtrynoCi2aFNMUVOHIudbC8bmJYqy-AH6VeQ98DNVd-zuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پردرآمدترین سرمربیان حاضر در رقابت‌های جام جهانی 2026؛ سرمربی‌ایتالیایی سابق رئال در صدر.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/persiana_Soccer/24199" target="_blank">📅 11:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24198">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2111536884.mp4?token=RJy3HA6QitwFacTqeFI3W2k9gARBJ7IWcrYJOCbE6x8AplApIRM0wveER8pTrZeRPx86J8LVmz_1l2vEtexp-jS_FSu7pIfOkF6qDueT9RFvC4lP2-VoXFpFiDFyy06H0Gug4J0BtQrF3GU6vGIiyaqYKIZ8buFCzR4iOWFTcoSygEs5BMbgepdCRVoSsqHfMbmsJbbrfb7zBwwZ7v7q_buHuAwV2MfXxpWdIB2j9JKqXT-0fMisZ1gtSgloOYw4JxcADIwUhVjP6iKmfjjdmfqNv_kdrU_AMjqyg4Lly6XODqTjt1b9r7vaHAq971DDt4ZkLWDHW1cAjEglETd1NA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
ابوطالب‌حسینی‌شاهکاره؛
میگه تا بازی بعدی یه 6 7 سانت کم کنیم تا قهرمانی جام‌جهانی میریم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/persiana_Soccer/24198" target="_blank">📅 11:51 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24197">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👤
👤
جواد خیابانی محمد جواد رو گیر اورده بنده خدا دهنش رو سرویس کرده؛ عالیه ببینید
😂
😂
😂
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/24197" target="_blank">📅 11:35 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24196">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSHvBeorLanqXn2DtnJsg0FdAgcSYlSrpoc8XsEEcMYAnCZEwLFqx1JCMi0cLvdF3wPDFDNn0AkZiOY0wpg-sPoegYVwTqSbFRqM_eNa5yJc0SS2LwcizD0JrZLwUDYIFbArjGv_eKmFE_1SlmCBOM63Gw7OjIYuTnqu1KbR0E0jBBO0xkCOJJ4gTiDA_onkx3x_nV6XaPcLEUwId7pObjCfOKO6II228eifMPoyNOz6CAFp5_aLyRSIFKSRfEhSqdKI5_WIvX4iH2CJx3djP7gCpsgb0Vk0l8mgnO5HJGcHFo4uXaRxtKPxcDvWPV3vkCa7cVTQ7ipIZRItrL6jjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی اسطوره‌آرژانتینی فوتبال دنیا و باشگاه بارسلونا امشب 39 ساله شد؛ 1158 مسابقه، 916 گل زده، 414 پاس‌گل، هشت توپ طلا فوتبال جهان، قهرمانی ارزشمند در جام جهانی 2022.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/persiana_Soccer/24196" target="_blank">📅 11:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24195">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=XsHHzd2QNthgaVzTClvdwvIga_6BDRJkq5EEnlbEX5YzdNze-AQpBPMdBRkXU1nUYhwWRTfzsJ0mDtpiTSYQafAksetTkNWVO1FZFtt7GK7s29mep-yLZkL7wuc9y1Od7SE-hMHrn1T4Ud5bpQXPNxUyOvEEFgMnn8fYaXdfEpqNDmfcj7-VKi9GX6zRj73qN2BbRGafYgXsE1MM926xpTnhvM38D1trVhvxFHJyqYShADdMcM3Hs3wKksVD2fsrYh4aDchbOcsnL6yEU0LMgvu6NkBhDoijdDPo6V4EW9tyQVQJFXVuxL2tW58nkT9OcBt-swxz1-0Pp6eu1s4LFg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cf639d4b.mp4?token=XsHHzd2QNthgaVzTClvdwvIga_6BDRJkq5EEnlbEX5YzdNze-AQpBPMdBRkXU1nUYhwWRTfzsJ0mDtpiTSYQafAksetTkNWVO1FZFtt7GK7s29mep-yLZkL7wuc9y1Od7SE-hMHrn1T4Ud5bpQXPNxUyOvEEFgMnn8fYaXdfEpqNDmfcj7-VKi9GX6zRj73qN2BbRGafYgXsE1MM926xpTnhvM38D1trVhvxFHJyqYShADdMcM3Hs3wKksVD2fsrYh4aDchbOcsnL6yEU0LMgvu6NkBhDoijdDPo6V4EW9tyQVQJFXVuxL2tW58nkT9OcBt-swxz1-0Pp6eu1s4LFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های انگیزشی و زیبای کریس رونالدو اسطوره پرتغالی فوتبال درباره زندگی ورزشی‌اش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/persiana_Soccer/24195" target="_blank">📅 11:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24194">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yllf0_JiGgQZ1NPViuA0DarAd0uWwe6FJZpKvukPCW99e9H45YcprXJ9EKwTaMeUm8iGU3iy914UOYPUJsfYGVZ0OqcRfoG3s-ymKn3wvm7_OmCQ6CXAAvcRL0Uw46YOe-ceg1SomnGt_C7mftcul88T7DF3jz6peQdvv41ssWdHvftSoOZxhD95vWaCoMCRIL4l68PJrB1KKlG4352VtwAgbswAs9IhveO9zvl2mzU4S7OSBRe7HuZnUjSHrTGIXLH43mqV68lGAnqnYEXq2D7Axw-uhm0MB6omZJxZ3vkjRBVZX-gIKbXW6pNnfHmDWtFf0OpE3FrCH64CJgUVgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ تا دقایقی دیگر جلسه نهایی بین مدیریت‌پرسپولیس و اوسمارویرابرزیلی برای جدایی توافقی برگزار خواهد شد. باشگاه با اسکوچیچ تموم کرده و فقط باید اوسمار فسخ کنه سپس از سرمربی جدید سرخپوشان پایتخت رونمایی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/24194" target="_blank">📅 10:47 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24193">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=USWOYz8EODXgGoorgEKwyRbAzkymtbUA1QeTWNMZxLS2VOhhY8DlGxOTp3hp_ACcJOcyhlNSLRmt4VCxghy1GNGBwrNHrdjEXGqiicVjfPZE8yFl5K2X5LSpc73kI62oCemC4Z4LcTDdK21O7gZyQEnfOKhi0X_EP3Us8thoLRHGu-HSgf8FNn8THJqNXNO7BkfVHPpc6tz13iJdXwZX5lrSIaxy_Uq35v7fQnNvAfjUkylRo9NRRVttTAwn5izTwxhbATPCQ4koxBK0DJtfHqQaau9_Fcyp3duhfvOw5uGlYRiV0jJLEtjm_1fDIkcZbw5Evj5ERAD-oLP74iICJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f67895d89f.mp4?token=USWOYz8EODXgGoorgEKwyRbAzkymtbUA1QeTWNMZxLS2VOhhY8DlGxOTp3hp_ACcJOcyhlNSLRmt4VCxghy1GNGBwrNHrdjEXGqiicVjfPZE8yFl5K2X5LSpc73kI62oCemC4Z4LcTDdK21O7gZyQEnfOKhi0X_EP3Us8thoLRHGu-HSgf8FNn8THJqNXNO7BkfVHPpc6tz13iJdXwZX5lrSIaxy_Uq35v7fQnNvAfjUkylRo9NRRVttTAwn5izTwxhbATPCQ4koxBK0DJtfHqQaau9_Fcyp3duhfvOw5uGlYRiV0jJLEtjm_1fDIkcZbw5Evj5ERAD-oLP74iICJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بااعلام‌ابوطالب؛
رونالدینیواسطوره‌برزیلی‌فوتبال جهان در سن 46 سالگی به دنیای فوتبال برگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24193" target="_blank">📅 10:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24192">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=JiqbJNr_18wSBjnOtFMf6zT9ziLMvvXOvSFMQU_m1C21CuLo0IanjQrvib7H7UP0SWHQtLBhmsdEF33d8nD6mmqNXih6oGqTC9NBH6lakmIcCOK5VsSk6S_TJKwwcWnbzvARnW1FqjPPPx4HBpG9-BSLiA9nAoIDqBWmDYm7jVckMDdVNLmQKYx8ssxCYbBQeZfhUuaaxGcnTI3X0IjrbTF8m-76HVvQSCNZtCB6ynXZrVV3F_cn-HjawR06LeDDA4gLMKg2kmFTbeuIq69cD5PF0cxJC3J9pdS6FyegvIrVJPSQX8rekWbYe8dQzrCRfofzYS4X5qrao7NLTtW3ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac231ff126.mp4?token=JiqbJNr_18wSBjnOtFMf6zT9ziLMvvXOvSFMQU_m1C21CuLo0IanjQrvib7H7UP0SWHQtLBhmsdEF33d8nD6mmqNXih6oGqTC9NBH6lakmIcCOK5VsSk6S_TJKwwcWnbzvARnW1FqjPPPx4HBpG9-BSLiA9nAoIDqBWmDYm7jVckMDdVNLmQKYx8ssxCYbBQeZfhUuaaxGcnTI3X0IjrbTF8m-76HVvQSCNZtCB6ynXZrVV3F_cn-HjawR06LeDDA4gLMKg2kmFTbeuIq69cD5PF0cxJC3J9pdS6FyegvIrVJPSQX8rekWbYe8dQzrCRfofzYS4X5qrao7NLTtW3ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
سفر پر هیجان لامین یامال ستاره 18 ساله بارسا و اسپانیا خارج از زمین؛ 6 دوست‌دختر تا اینجا
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/persiana_Soccer/24192" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24191">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ar8HuLpiqNiDmJSBYdXdrcjP7XAm-7d8I-z3XMjYVVnVIJ0zc0hWJzpaTkzy5EpnaO2roa9Vvuoc04vzclsye9Zg_BCmdRH0iVB-OZJA3Wja9m_en2Lqw2RY2nlcg74_EfnrVxTMEJcPncnJ_jLxCpOp0DxZdph2oG7yea-AK1GwbhTktI8Fh82_9fG3YFqQWXIc4rl65N77ZPF761elnfSrWL0nindZuYF-mo4D4zyLdnigMdKFW9ZVN8xU4YkcJtJ5JlaLHvvX1GOW8SDeUvdZN8d7BdmBHrHHxTUuFt2q4-50aBMkpm0UaK3XgnfxZejyjFsEJ_l2TAxTZmsh9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جداول12گانه مرحله گروهی جام جهانی 2026 پس‌از پایان‌هفته‌دوم؛ تاکنون‌صعود تیم های مکزیک، آمریکا، کلمبیا، آرژانتین، فرانسه آلمان قطعی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/persiana_Soccer/24191" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24190">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XKAon3g-DHrvamiSd3ef6VOaMGBE7RzYb2-sf8WRk-VBaPulf1lAfLXESQ7ChdM_u9tjrkG7r17BCAMXO4c3rJN5BGHWbGSqAdEmy_qtd0mLKn5pqLnfzdE-d3l3FuE5b_tZUuJTM4I-gONwpqXhQX2gGDWGk7SWvs4t-8nBKLYgKPgsvvq9cbY-nO7m5EBlLOfnnHjYqlXv1cneQRfvh-BJJ2DSNVjwtDWtnI4jA7tZ5xaElbqOHQ0G4aR7cQyA25Ides6lnoFB_DSz3ob8ADPLebSzVvNwX8uU89SPNAok1AaIa5vAAgdySDqw6VkNXe3dHvEYMwgqeQ1EPbxiZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
دیگه بازنده مطلق نباش
🅰️
🤩
🤩
🅰️
بابت هر شارژ موجوی اضافی بگیر
🤩
🤩
🅰️
کش بک بابت هر باخت
✅
این بونوس ها بدون
#قیدو
شرط و نامحدود هست
.
💵
با بت اینجا همیشه به سمت سود حرکت کن
🔼
⌛
پشتیبانی 24 ساعته
🌐
betinja.bet
🌐
betinja.bet
کانال بونوس های رایگان
r3
@betinjabet</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/persiana_Soccer/24190" target="_blank">📅 10:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24188">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HjdltuBNpZQx4fBR_R8njC7SaMMxDZK_K_yrhgvgfQOXXIU0kzXLEQpHWq2gJQmzrJlVXUmF4AK2w-sU-mNnEq5UELiqigt-ryO0s7G37XyQefZW0WUSQCM5vH9koFaYzSLTlo5T4vtjv-yH9vdB9uSWxAEea_LcbAv51qmaDEmNWsgCmWXRx7kieeOp1SPKz1Tvh_1dg6PfFleniZ8ui58meFn8CWr5xfu9TfGiMqSG4aDFkqGpbQ1v3FJHxB287jvZB9e4CWF5iFqWg1SVIY2vRmH3Y1q3ePi1rozgdyz8_gVsZEtNd58QnmxixU0Xv428GIjfYFULoejJR8jQOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sqxIt4pPBl8Iv_09LBYhupd1mjKTl1RbeNHaYvjAVXTg-lUYY3_vXoSQi35ODS0pRkq8wq8Cb38nrbwWd-kbErBt8j1MH-6cXbKl1XmS5jwR-NmtnokYU3hMfdUcfxDxCK49hYQ06rpiJeZdOFHpGOXTvuCXxOrRWkhGhx8v3hmrqcFcQ_RrFBTaQdW6fBrsjtGljUrKBpyMvoqJC9YPO64DCAlOEY_5LhUmtX2SxAVW4bLd7zhQ_KEI6ijATYwnrj9YvpjRHcAcT2Ca98xxiwgZ_ptoh7OJQ-mxGRD43jcQLKLrx_E-twNi_-dtPKFVuibTMANkE6HW_Y16Von7Lw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🎙
هانده‌ارچل‌بازیگرمعروف‌ترکیه‌ای:
فقط بازی های پرتغال درجام‌جهانی رو دنبال میکنم و برای این تیم و کریس رونالدو آرزوی قهرمانی دارم.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/persiana_Soccer/24188" target="_blank">📅 09:59 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24187">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c00a317fa.mp4?token=v2mJ4FFFwE5QX6cFA1mQTwdM5uvx39yJQKAfulb1zQgTfCGeVUmiuCEvDt9yZ86xH-HoONMt9PTYViRJxEMpqrwsumIOk5brblX9ny8IV3HifWH8Qfy9REt2Fp4GkYCSVzLNinj4_xhBjlqdsg7zcDmfNG22wB6EMRlVaw8qtNAolP-mwbE5hpSvsJcfA-qMGJUqxTQ9SxSsWHK7p7-ex6l_R2OC43mFQQLVI1snXKFTOHrkRT5m9AAf8jAPCZaGEIZS9vIiGShOPw8teQoHJTphav78GrxITzKlt1GbvA3JN4Qkj1p8dgnHWPNid1rmP3Alpobq99cdgVwbLu4I3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
🇳🇴
واکنش‌جالب‌ارلینگ برات هالند به دیدار بعد با تیم ملی فرانسه و امباپه: «فکر می‌کنم فرانسه ما رو شکست میده و احتمالاً قهرمان هم میشه!»
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/persiana_Soccer/24187" target="_blank">📅 09:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24186">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uEGhjTckE9m32F-fEE9k1C3NLh6B5WOo7h8oOdHxN9zx04umprsWnCa8K2B1fPpJdMsv1vEeKoPA2dTop0ZxAUGpUBV9l45B9ThqK66PqfiEP_uEpmYgXQ0fZ-yTN3F7lJcqr_An-5VeDyaK8P6sC74NJ07WB9X23RuRADU0sDhhU51HENhIn89NEKcnGvA34e-etCTsTi6F7mp7PWAe1Vr-yg3RJQHQEs-MkyL1ThKP5JzL2ciw2hoQho54J0_S5yxn8_a5JduAHk8p33t_RFcmWtxwWz-8oQaKTwpjR2reo69_4nK6xSpoeI99RrXKhM-zc2PcTMzPDTQdsiW2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برگام! کارلوس کی روش درنشست خبری بعد از بازی امشب از نانا کوآکو بونسام جادوگرغنایی تشکر کرده. جادوگره گفته که کارخیلی سختیه ولی تلاش میکنم که غنارو چند مرحله بالاتر ببریم. فعلا با این اسکواد شخمی و در گروهی انگلیس و کرواسین صعود کرد‌
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/persiana_Soccer/24186" target="_blank">📅 09:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24185">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCdE8g22sUsF908lDDCSLoK3wtFe4CGgGSp7ziQkiNaHqO9yUzTriHcbC1-Hx_DHLdkgVeJCyTuP_yf1I0O5wNoxQ7azMGC2AFxVvjcdlIkoEvPsarchjJWSA3M7bzkVi6YLUCQfqSlEe6rsKcaDJqm8S9l3gWkivpmC_cXfrvP4Mh4HnVgu3HMkArcUvZJsLYPcq705ksBrtnO5Xb7AFBiLcx73VG5yT83cmD_bCoOnLKuuRdrAwAv1U0F1_4yPSUqXLwKYzFxlmV7t_1XzwC_W18590j0RGogwHUwOyG6b_uAg5FzBZPqyJ2T9icnu075-EyDaYm_dNby8TQK4DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌دو دیدار بامداد امروز جام جهانی؛ دومین پیروزی کلمبیا و صعود به مرحله حذفی؛ اولین پیروزی کروات‌ها در جام جهانی و امید به صعود بمرحله‌حذفی درگام آخر مرحله گروهی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/persiana_Soccer/24185" target="_blank">📅 09:11 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24183">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7nC6p-fwKb4ZR9MB-_1J8mWdVvJ7V1aF9_aNJ8fANBU-S8AHvTRx0JsNX5lM4Lz-I6jWfv_W5wO65cTQdv_UfO9Sbsh_gEdfXIwp9uyrEXX0JVpN0ecsbOsINvQYotgCHx77tUk4nZmm0juo4HRTLq31mF_reUxIJ9XhRxbK5EcJOgYbfVqSoMWvfU6Dqdez1STQliU50SJTFobppZ2PqDCrGVZPvrQf6gKftwsRVHCg8wyQ8RLqb_UVTcr2G8z0UNtdl10O8drJ1fhnUvioGeCj7UDTUMK-WWjYc4AV51cezxDAxCZT0XtlvbLXPJQPNxfPU8CgMdjdFgAHKR8_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ioIQSCPXrYH-TN3l0r7vP5VCr-mVhGZXaOCXZ4p0TGRcPSPO7VLyqg5LcfBaPuCrIYDSmM_QQ-zxiXXpv9kcnCdsMYjRcfBuxpBz5H5eYEYxOAnyi-SW5_WCvhKLYoIwDaz0HjpiPJrzhqDVi8UzPaMVLUe2108m5uLz5XFfLgh9lDUcquPjzvkn6p4IgpUgeDiajQJygdG5CYg6bjLTTbdcl6LDh-EzAfndI1amIp-S0llGuNT0RV6tPzbmhcZvjBr-XSDmZPWoOu-EE9mrziuP1gWxEzTmo6R2f9nswT-duoJAu15S_V-h26HriiHCb_jC61Sh3H5lJ9FTKWy6Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛ آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.2K · <a href="https://t.me/persiana_Soccer/24183" target="_blank">📅 09:04 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24181">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dZRuFP4VdpZhSj1f9TlDscExBlnT8_fOH8KfuG8W90ANPgcdA3oyYuMOORdLaFkkSPAWmgHSct3BYLy7WDafPLxKtjLA0_KrV9YE5FQ-uOTrUOvm2_b8W7jUT7-3Dk83pAUJs27KtFtRW8wNITF3Mhvalx7J-AFEWhYj5cAgsFrknUUUurZ8PQQ5TWDrsfGwe8lgi8dFX2D7epYIVG-h76pjuzC6hAbYScCaDnUu7JtppCOPHOH8mubNdMqI7lFBmQB6guIn6F6yG-kcDdVEtbkKi3I2ksTfiRzRQnPbja4jHUjrHu8xCc0qa6cp4fic7yQaT23z4joUxrpswc2zmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جادوگر تیم‌ملی‌غنا: گفته بودم که اجازه نمیدم امشب هری‌کین موثرمواقعگشود. همین تیم انگلیس دوره قبلی‌شش تا به‌تیم ایرانِ کی روش زده بود اما امشب حتی نتونستن به بار دروازه مارو باز کنند. به کی روش بابت صعود تیمش تبریک میگم. هدف غنا حضور در جمع هشت تیم برتر…</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24181" target="_blank">📅 02:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24180">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UBmHoo_0OB76ilsry7vHxrPrQKaTGRYss59OpjstdyFvH4NE0oDwdZatO9-xiz10i6Il24WfHDkmkeBsYqbELxMBbCFNnVlW4o7rxjDS9riR31MYp_zkB11THusvREDoZG-b7cPZB6yJvhcUe6Ic75LEpnMGzkMMs6x7H1YcoEh6CzhTpAAWV08KxmXvK6I7Ot_g5NLP0vzgQau753KiuGKELp5G8wU9MXUACHeqpSnYje-34oSwi53m9bJE3-_NScBWjF9EPvy9Hjz4KebjLmjl2u_2eSyimXPwG5k8d-p0mybFjUnnby2Y0HjtWVUztK7jzFUng5Xu497lYdSzig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
آغاز تقابل‌های جذاب و حساس هفته‌پایانی‌دورگروهی جام جهانی 2026
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/persiana_Soccer/24180" target="_blank">📅 02:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24179">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XInp01QSc3RsNTVZGVzWISbwX2hOqQGSOGQfUzHJPGeD3Hn0XkTJcHDtAncdT7qdENxFNxYRO4msNsRKKD_ehY3vRdWinT8hqRICSsH37OfPs6tSEPmXqD-Vjp9BqKlxnrv45leuv0uNVsl7o88xYPARFzUDrt5euNzXnvWC8zpIt1EYfg0UQBbVIFfX1nEJUZlbo6ZXpPeZz8Tn9XSOJHavYGRY27_vvp3BkacvA__wdCtSaU0dInlJ7eDUOXHx2t-Aij-GLVh7vzGjeGCDykIIGEz0yw5THtIkCKZUSq2BWmu8Nl_Pc5ViugpCF31wgu-RFvJsj6Y6nxjCN8iXFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از بردبی‌دردسریاران امباپه تاآتش‌بازی پرتغالی‌ها با دبل رونالدو و توقف انگلیس.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.3K · <a href="https://t.me/persiana_Soccer/24179" target="_blank">📅 02:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24178">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc844d2c9c.mp4?token=iDLHQqEjdPSKR1m8YHv5wMG1fYJKZheEUuUB5JgAyXlQmPOM7LUx6KgOipJ1Z5DYreu731fypiVE7N_yAfaTEVHyuHNhepp5gkTdAUIsU5t3tm5jFDSr9pgprLkZb4dNfYeEDkFU4fFg4szIwTSTTQV-UygxKtkCVCQ0cXh0calk1tZtzNrCEh7MPMpF55ueBY6Cr9smOtBJBJ-76zMHcic-VVqfYGoyeQhYQiYa3r-Dp6oIKeFrKebwvEeeVNs1JPMEawr8-s1wALpFSKf6BwNT9AXP9CeXhP3zIQsi-TaVla6OJhcw3DynRJHdgvXfi2ap6IQkk5gwMlWDG0kkag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عکس رو باز کنید ببینید هری کین که سه فصله داره چشم‌بسته‌برای بایرن و انگلیس پشت سر هم گل میزنه چی رو خراب کرد. تازه سه چهارتا هم زد یا گلر میگرفت یا مدافعان از روی خط برمیگردوندند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24178" target="_blank">📅 01:53 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24177">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qRnurzl1iaN2326R_TJu4UL9CpzzfzVfOGNReBufgbbTbv_WgDWAVGNzij3mEy_SVyL0Ofj7I56HI4Z2L13ciCM7aiOk_lau4RajZ0bh8umQgN63zVifYL1ENYyair3c-MdJ7FuyWl6hYwyADa8Qrzw0kBd2K-7yU1RYYMBWfdtbZIZkP6FwwElP5p0V3CLa9tIseuAQeUtS9EuBAURkZgmUniMCcTwO-lHvkZ1G89Kf7pPut7SMd_o4W0K2c3PHw6UNFUKFxsAtEpPCaz0L6IGuclZkpNno7b2tGFeQUWoWD9tFdrdPw44xqTM69BdS6WCxJN4wN4dBrBLz8BGB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/24177" target="_blank">📅 01:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24176">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ozZPyj6bG_XtqXuchIUD12Kb09hzkU8-HbU517Cn5tpUKFuI0Xa-NaGXZ0KOUWhlBKettUCgFVV6wXyw3gPp5EDzoaUMeC2Lo4qFjslfZMs1myde5T38J97CKZcELao6WdTWAKET7g-9wcKtGS7_i9UwF6ElaoG_9u4Ei0C8I6jMm2D2hOFfdvpNLvj9MjOWJPkbyJzqRXB5h3FguBOurd19yrA6m3W1C4f3FAZDN6cza_O1YsCmtv1EG-0Cl6U4-Gnhid4Dm1RorWYw1ZbM5w911TqZzAXBJS1MPEWRxdJDpeePFywf5i3_fSSE8j1cnOx-bZHS8km4GmBJfwZ1BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
کین واقعا طلسم شده بود؟ هری کین که امسال انواع اقسام گل برای‌انگلیس و بایرن در نقاط مختلف زمین گل‌میکرد امشب‌همچین موقعیت صدرصدی رو به آسمون کوبید. چند موقعیت دیگم گیرش اومد که بازیکن غنا توپ رو از روی‌خط‌دروازه بیرون کشیدند.
🇬🇭
غنا
0️⃣
-
0️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
…</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/24176" target="_blank">📅 01:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24175">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=iKx93E9_v4siASwJ6INVdn9_CnR02FLhtaDPUJ2JsSRvea2beCrtM98QBmMMb-iGt2HVHWZoyQzHmL66shoK-I6IbO8S7AMlwm6EigmBbZapPxoTMCQYWYFyhdaEWXWMSDmwV3nok5ES_7VlbF5In91xMNzKtWp9kafw3rIJi609v4C208utrOjn9Cqx16xbE1nBp3qHZhEOWS2WJ23Xo0wMFpHYXxon_Y1AytfaOti7pSxyb57YvxKzf3A5caQuslUCVc3uG3L7tGWrRBwXb5ta1hEq27Fmh7db-VgsimVy_6wD3TmuisZQwXuFQyrUQarmrsLZ67rrmfOsq-9HYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d277b50bd3.mp4?token=iKx93E9_v4siASwJ6INVdn9_CnR02FLhtaDPUJ2JsSRvea2beCrtM98QBmMMb-iGt2HVHWZoyQzHmL66shoK-I6IbO8S7AMlwm6EigmBbZapPxoTMCQYWYFyhdaEWXWMSDmwV3nok5ES_7VlbF5In91xMNzKtWp9kafw3rIJi609v4C208utrOjn9Cqx16xbE1nBp3qHZhEOWS2WJ23Xo0wMFpHYXxon_Y1AytfaOti7pSxyb57YvxKzf3A5caQuslUCVc3uG3L7tGWrRBwXb5ta1hEq27Fmh7db-VgsimVy_6wD3TmuisZQwXuFQyrUQarmrsLZ67rrmfOsq-9HYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/persiana_Soccer/24175" target="_blank">📅 01:32 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24174">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKxh6Bas7bPvPd-x0Gtv_JqAHTKnnVII3NzoVtUMXsZQ_P6RLKlgjGLiDbwaGhUYrlsPTX-ZrN2IVfk9AUfuaMbIN2pxJQIMBe0ne5ktml5e7yGtsKM5OmrnOMyZh1Rx1Q8EXzWTs36I1aFCzvCo_3OyXsIlwOAjUFMLpFeZvt0FmselamnGPSqAzIBB1v3S-DdR_PJTUfK6Y7e3Q29omWywQjuuCRcsoBkoqdJwoRqOZYy6XS-VOW7QPUZ689127o1XacLN3c-yu-2HqyFuFcYk6kXMwP_byZLvkvrqzR6PRX9vjSyfmhzgjeJGK5xGlHRGj5CPKyhOH3ZIrZIJ-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/24174" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24173">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RMmUPkDtmkcOKIv13FecbefU54uu4_MsZ97dsHxuUbISSnERHzpIZrjMK2q6OSGzFJAsJ6ux4N_2swwY4dobk6xmWMpBB0BidP9-xm-PMuLefQtRCKgzIb0AlsfqR3qZ2g-aNAsZEynddxJZHbt4XVRKPOj-mL0BXT2JVdeKvf0KSpLH2YwWmLzVoGYLbBxUB_Aptx9VoIorxVwKvRNcuG3V62eOaRuOwUFV02dqBqWC-cWOW7z0HRfHVG1uHxeGMyn9bgG-9f0MQSq5_TUWKIvAikGuZesu_IfFgC3pP83VtEN5l5qeelO13CR0qmuZAUmM1p6A2oLTnaab52fDww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا
😄
😄
😄
😃
دلار درآمد با معرفی دوستات
🤝
با معرفی هرکدوم از دوستات به وینرو میتونی تا
🤩
🤩
🤩
🤩
دلار درآمد داشته باشی
💰
🔝
فقط کافیه دوستتو به وینرو دعوت کنی و کسب درآمد کنی
این پاداش پول نقده و لحظه‌ای به حسابت واریز میشه و به صورت‌آنی‌میتونی‌برداشتش کنی
💰
💣
بالاترین بونوس‌ها فقط در سایت وینرو
پیش بینی کن و برنده شو
📺
تلویزیون لایو برای پوشش بازی ها
🛍
بالاترین ضرایب ممکن
💰
expert tips bets
🎰
راستی با اولین واریزت هم میتونی تا ۲۰۰ درصد شارژ اضافه از ما هدیه بگی
🔤
Winro.io
معتبرترین سایت ایران
🔤
Winro.io
کلیک کن و درآمد کسب کن
📱
کانال اخبار و هدایــا eA2
🌟
📱
@winro_io</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/persiana_Soccer/24173" target="_blank">📅 01:31 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24171">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=EHNolO2rc6SYm3M96MwgD9xkC9Ms-B2HwD5gz_F4ZrNxHMjkkJ5GN20h2qjwhYRfwy5lIQgJgMz8Epwb2ypnjsaEnDrL8Z6T6o4f1WfSMlgwEkkjLDePlZuA4ZJvqhqLfFawu58PuHkoifL0Z1II4L2l-dqzvYI0L89AywI-WHgFBtloiHeXyCniUCrnkjREhRApkr9Q--LA3GVM6oIgzpy9xQ0biCN47q7vAdN-gFN7FdoPHZ58aBOOKgZ-KVzUcFtlMa8yUOp9IgrD0FcM-4DEHplOnTgCQIQknUoPDPnBYHHK-psPtThPOCHJYlR0xHYcH190I9-Yz6slNh4JXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0d760ac60.mp4?token=EHNolO2rc6SYm3M96MwgD9xkC9Ms-B2HwD5gz_F4ZrNxHMjkkJ5GN20h2qjwhYRfwy5lIQgJgMz8Epwb2ypnjsaEnDrL8Z6T6o4f1WfSMlgwEkkjLDePlZuA4ZJvqhqLfFawu58PuHkoifL0Z1II4L2l-dqzvYI0L89AywI-WHgFBtloiHeXyCniUCrnkjREhRApkr9Q--LA3GVM6oIgzpy9xQ0biCN47q7vAdN-gFN7FdoPHZ58aBOOKgZ-KVzUcFtlMa8yUOp9IgrD0FcM-4DEHplOnTgCQIQknUoPDPnBYHHK-psPtThPOCHJYlR0xHYcH190I9-Yz6slNh4JXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.2K · <a href="https://t.me/persiana_Soccer/24171" target="_blank">📅 00:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24170">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZnzcXi4VhY_axKvqoYRO2rfQnf7fLayxJmCB05UkLqK7j48x3RGororqUIAXF5Kqq3umjwVbub3SAo3kuSf_phg0Xvg7jFj32zT8fKys3Xn60JVvz2rt1Zj9WXvoIglTkTOsqh3hIl0kMO9c_OaDsiTXJRBiV4SGm3AcvLwuISPNJb4BKtMdGBNtli4pmeAudprAf4MKXtXBflqSUnVRmrHEQ_1AYvxam9SDhk4PVuKXxjWX_ay-XpgPwV9ZkIPsH-pHLe7lz2kc5Q0Poo5Tz_sp9zj0sgDIhylyeKzAR0i106ddi97lUePfE9J610v9sQjfH_fQtfAQjP8V1IrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان: یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم،…</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24170" target="_blank">📅 00:22 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24169">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=YWPLLIZAERUoaPX4LSlFZbt2qp4P0rS45OyDGfCx9GnIoY81aOBgGvimfaLLx9mI1Bqpq4Za4csi2B9AIWCGRdEiBxAj7UFblrL9rb4nX1QKEbm1F8cYK4EqdD5U2TpmqTgYHN_MIx-eONCDEXzYIYNiQXs41WcsuIq88dvzEsDl-X-xtnobJNaYXuKzMupoy2xHTCVKEd_zGCLeGCJjLiWDwcFnStYkK5yR9aoB9AXOT7ojy_uH-Mmsc6DDBLoFG5KChYIxIeP0mQR2ZFwfegrmgVBDbA-48RMFNMqaQ87zp0aG1eT5NgX9rz6hZ3aI1EMXuBSqqBViEDSCPtp81TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59b8e3fdc2.mp4?token=YWPLLIZAERUoaPX4LSlFZbt2qp4P0rS45OyDGfCx9GnIoY81aOBgGvimfaLLx9mI1Bqpq4Za4csi2B9AIWCGRdEiBxAj7UFblrL9rb4nX1QKEbm1F8cYK4EqdD5U2TpmqTgYHN_MIx-eONCDEXzYIYNiQXs41WcsuIq88dvzEsDl-X-xtnobJNaYXuKzMupoy2xHTCVKEd_zGCLeGCJjLiWDwcFnStYkK5yR9aoB9AXOT7ojy_uH-Mmsc6DDBLoFG5KChYIxIeP0mQR2ZFwfegrmgVBDbA-48RMFNMqaQ87zp0aG1eT5NgX9rz6hZ3aI1EMXuBSqqBViEDSCPtp81TzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو کاپیتان‌تیم‌ملی‌پرتغال بعد از دبل برابر ازبکستان:
یجوری رفتار می‌کردن که انگار من دیگه ازفوتبال خداحافظی‌کردم و تموم شدم! اما من تحمل کردم، مثل همیشه؛ چون من بیش تر از هر چیزی به کار و تلاش اعتقاد دارم. سخت بود واقعا، باید بهش اعتراف کنم، اما خب. مادوباره برگشتیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24169" target="_blank">📅 00:12 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24168">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DlMIOJlw_iShtuWZ79GtAT_N28fkQm0ROkVh92OISlfVGBSXHWZtQc-8ZzOjL20RgyRrOYDqrP3xeNOyHZC0gHpsiEDbpF5-gxF3E0V1QaH-WtMv4WjqNXExmBgjSb1_hgGx4ffQbzO_22VmknPdouRL-CfE2zNmG6luI2O8jfakT_EQVMzpA9et5BLj4a-c79IoAyyubf3vfZzj4nk6c67cRlsr3RcrVs8hz3EoPWuQq3fJKxv_uUZQJEMxC9JjEz3k0HyCFftHFQovmSooFLetAOSlduYn2zOaFE0YSbPdDQtLxUUfUbSJLOhTLAJh3tgUOJZJ0c06uAEYOErTgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
رونالدو بادبل‌دربازی‌امشب‌وکسب‌نمره9.1 درسن 41 سالگی بعنوان بهترین بازیکن زمین انتخاب شد. رونالدو در پایان بازی گفت من برگشتم به بازی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/24168" target="_blank">📅 23:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24167">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CRT8US5GyT2anTnut20lx5G8o2iFC9ZyN6WJqZiGdM5ONJaSfnhSo13UxKRE3z8F3br5WTVz1jirbadQp62hFFm0Yxdb9UsIYy9BtvOwUj7usZ_-AyQ12qq8h_H_xx5RGYn9LoSK6ea9RpUbBddIC8dUXe8zdES3fvUs_Chp7Z8FmIH7G9JfV-_etx9AayxJ7aGFf5T-9lbAiiFB4VnqTzdMiBO4q0yN7bGgqCxmAxAbvWeUYiwlI-uLQGjIg24H30vwGjrf-2IwNIqlhZey9CBQrVxVjzDBWVuExKH2ipzCJLdL0qU6qJbTK-BrXkzVCx2YOVOeZWsfM4OYLMt7NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
چندساعت‌پیش‌مادر دیدیه‌دشان سرمربی فرانسه فوت شده و این‌سرمربی‌برای‌مراسم خاکسپاری قراره به‌ فرانسه برگرده و در بازی روز جمعه مقابل نروژ در هفته سوم روی نیمکت خروس ها نیست.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/24167" target="_blank">📅 23:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24165">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=C7VaE95hO7YATwn0Ro1Q6lMbaFLqkywLoS6pBeSuamm-q6ng8YjCHaVamt5RtzRYVuzcFHKAsFvkZlMcCId15x5T4oeNU814TWxufgA8xdzSo5k06zxj45C2_OCvmAzuphXQkthaQ_1JhCjvFCLnXnmJx7OAH2oT4dUnNxkE810gp7lngSil6fCY1bAzvUxwyyTpZWl6jgLBZvpoKtp8NdMy3c8y73Kj3uH2YmEF9N2df5MaY40DaMvPZFYGto8YznG7EQwbN1u-J2_0fp_w3jt0CLYQTgQbbsCk8C4xvT5HyqMkg9ObWOJuWo3wMWoVdeDvbjTtgyOavRQXLCtCag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e38cb7e207.mp4?token=C7VaE95hO7YATwn0Ro1Q6lMbaFLqkywLoS6pBeSuamm-q6ng8YjCHaVamt5RtzRYVuzcFHKAsFvkZlMcCId15x5T4oeNU814TWxufgA8xdzSo5k06zxj45C2_OCvmAzuphXQkthaQ_1JhCjvFCLnXnmJx7OAH2oT4dUnNxkE810gp7lngSil6fCY1bAzvUxwyyTpZWl6jgLBZvpoKtp8NdMy3c8y73Kj3uH2YmEF9N2df5MaY40DaMvPZFYGto8YznG7EQwbN1u-J2_0fp_w3jt0CLYQTgQbbsCk8C4xvT5HyqMkg9ObWOJuWo3wMWoVdeDvbjTtgyOavRQXLCtCag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هر چی تشویق تا حالا دیدی فراموش کن، دیشب نروژی‌ها به سبک وایکینگ‌ها کل استادیوم رو به وجد آوردن؛ هر کجا هم فرصت بشه تو کوچه و خیابون این تشویق‌شونو انجام میدن
😍
😂
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24165" target="_blank">📅 23:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24164">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hS6__bZMZuKC-DVp2Ngh8b93p5rnHVz--dfFvmoob3lOKw3VwC076eG0BSN-TUU9OMUNA7EfIkcKDepiKcT7CVvTUs7JpXppJgvQ_EczHNDRENYEM6VwXXQch2fFnMbyLV-N02bUjWcyqWKdtTXsn5wItdM0ZKlQ1m7PzWmMiBFfdOZEPsq23DhyqWzfDEFnMU9zilDyf7G5GSX4wHn5VFoTdhlEiZm7-103qITwdX9xbV0_1dkXawWmcniEk5iKM1IGP7kWStoeq8KFXR6_mmHN1KchRTx7xwAPTLdhMsh6bBbTiKCgm2lR4AATbFfl2yMfYLlGKiaNuu6D6WCphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24164" target="_blank">📅 23:16 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24163">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=C7UDvve7MuAk6q94xKbNLr82kvY7vOSwegQrYljc5KeHuzfpDJ5Pkz_5emfuEYEmG-VlT45abDfqfDp8hvaKl4Fju9KJ-23wOfzIGClkLzMF4yUqME5oeFcSItDK4wvm6MQzK-OzQ1fYv26EB2YqA4YHfFuEGhdakJVwMFXWVXbFizfXy8NveKC__RmmLaIkJKOJ56Y-Biw3WjHaU2kIJDRTtYevON16pldPIiZ-6MfHVNIoVb_qC2aXHGJ_p0Cy1_wxHTDTkyXdjLKm2cdZolzT5OnOoAYS8PnGMO6on2NE2QEek8IZAY0jIBIDDSZ8eUXDQQ6gwCpMWU9QnwPaUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/41c27664f5.mp4?token=C7UDvve7MuAk6q94xKbNLr82kvY7vOSwegQrYljc5KeHuzfpDJ5Pkz_5emfuEYEmG-VlT45abDfqfDp8hvaKl4Fju9KJ-23wOfzIGClkLzMF4yUqME5oeFcSItDK4wvm6MQzK-OzQ1fYv26EB2YqA4YHfFuEGhdakJVwMFXWVXbFizfXy8NveKC__RmmLaIkJKOJ56Y-Biw3WjHaU2kIJDRTtYevON16pldPIiZ-6MfHVNIoVb_qC2aXHGJ_p0Cy1_wxHTDTkyXdjLKm2cdZolzT5OnOoAYS8PnGMO6on2NE2QEek8IZAY0jIBIDDSZ8eUXDQQ6gwCpMWU9QnwPaUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24163" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24162">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4DDaN1wdOiA-Kiu4GQv6nJ4d8OuowsIpduPgmvIpfXf7uUa8sJpf_Y0QWzBtnP2xgYZKHOUg8hmIAyF1X0SeWlbBXRCFwx1CKAX_RSDOtOZW0ifo-FhM3pdzGG_9MWCGmoDYp4COb5qfwPScUMk5_b6aqQeJ2EwfJf67nmuxg3BmVbNBtYByQclupNqx2toz9ZjWBTc-XuV5yknVcQhjlUAhGvXfTLTG6603wwdaX8adjmcdSK--YTDmWWgluBueobrGVyfosxsfmsqX5MCohSFgk2jPfCVzydkJWNGiAcphmunmvJbbmIv7YEG0FsKW8bj435H0zOjfFUCJCs6_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24162" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24161">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CBG4Mh8vEIc-YFW7vmxi4ZVIgIBEwAmCLC5jxDI6ZAvcKUZtr1-Y3OgTApEg8oUF4a3zn6CPValzFkpOMG89awTD0QfbfqFEOCCN9k0RxBZCZM6Kq7XyOKmT092ujjrDujDYToOeoIGK4YTEjvq6Vvf87ph0BdkXyp4LsQVRja42YumRdXSERimIxwdmvTGVNmlMAobu7SLcDgkleSdRGPW-jGHgk1o_dSMOLpcFgBpY-DRn0fdd6X8Ywi45D8ehHXsU-FCaDLMpsaYnYoIhgL9k2kJjz3f2TsuAHjwNCTeaDlpBfgPMhGt1_EYCVAhLhVKLNogHEKOTpVajoW8oCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
⚽
هر گل، هر لحظه و هر شگفتی را از دست ندهید.
امشب میلیون‌ها نفر مسابقه را تماشا می‌کنند…
تو هم به جمع آن‌ها بپیوند.
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24161" target="_blank">📅 23:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24160">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f6TjH1qeXZqh6RhJ_utemFr0iDCWWuCBsg6-Bkwcd487IC0so9xrbODkwz_QQwPOYXXu9D1EoEEKFaUrusLC0RF7mrHKr71n02v75wkpWC9hxRt9puivasfJmfz5UVvnJcLHupRiqVttJ8SDFGdHvA2suwK1H2g5I-1P2XcIZJ9nBHZ07jFwmEg62oE-cHbE2sCjVpKG4pzp6okyRD9Busyd_TdSKvnyT-F3uP6i2LVCt-0fA7B0KC10-nVlNvGPuF9tiTRg-9CZhkTsI68YCwdk0nEbePX7hnYxQFuZZ8EdmMHmcd_rEocJjmWycYMvc5zy6v41JRPitNVRtD--XQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇷🇺
👤
#فوری
؛ ادعای رسانه‌های روسیه‌ای:
بعد از درخشش دربازی‌مقابل بلژیک؛ باشگاه زنیت روسیه به دنبال عقدقرارداد دوساله‌با علیرضا بیرانونده و قراره بزودی با مدیر برنامه هاش مذاکراتی داشته باشد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/persiana_Soccer/24160" target="_blank">📅 22:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24159">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GN0obxnY7wwHXgS6jD92glBaaM8qI6kpxP1yWL52rhpo3OCAASUuptIj_6ZcQaY5MrNqMG9dFsneLHRuVka9O5cegunp4txzRv-RcoHwewKxPts3HDAG0AqWvMk0jog7N_PbwFGL0nPN6_5f5z7TjkE-3ug5mhW1pCCCXNUwKmJwkF4ktXQQgAWSOOrVrdgrevcEqLiYMK89l-4zEDfWbxANNbUk5YqMdWq6SWJ9Cr9zDghwG-vtlec9EW_ziXXTMwEE7uG03i6nUSS7BRTgTA4uQRMui3Xxflgcc5hik_MgxOYCCjmKA_Aqhd0yVm5GsYaxL2yS_eNksu40LPJNew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
هفته دوم جام جهانی 2026؛ پیروزی پرگل و قاطعانه پرتغال‌مقابل‌شاگردان‌فابیو کاناوارو در شب درخشش‌دوباره CR7 با ثبت دو گل در این مسابقه.
🇺🇿
ازبکستان
0️⃣
-
5️⃣
پرتغال
🇵🇹
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/24159" target="_blank">📅 22:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24158">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-JFV5WhFay_JnLDykujOuwsoV7KqjqL7X_Fmc0gJNqb1b0VK4nql2Fq8PtT7vwTwXWCxKwPWhZVsfKmtcQlQxwBYP----j3Cpr61sUNCZiggD3Ac02lqjFO-7ZSug6rez5iuipVRLKjbPIx6prLSkKXqDUz9cPEj05tAniYuaal_DeZOn_jt1iy3F_OrXo3vig6aeE_Qe8Brafxc95e7rv5i-fK94F8jHYBHL4SH7rawfMbxkhIswOyokeq5SEboEOkUiHmO4hSbRq5YCtN4aTEXLHPe8OFsnwJ8qxrorMTh7HOOsWyo_2C3v8-Rc1Xv865IqZtCklWXzvnbRYcvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.2K · <a href="https://t.me/persiana_Soccer/24158" target="_blank">📅 22:32 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24156">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dU_RB6FuNBiIjIPuD-1xmiJUdxeUAN2ckZdopr37RLTKzuODrZFl7yOXrQuuMZ6s-uy1-VgrMeU6EIjg4NGmk07_6khApZiVtQbXWRtXGVoMp5saGDFLlSIQ44BoFNzMOHguQNMxM9FHS8e6vL_FOFUeVAwbMd76W_RYIP65EDeew1B5H3-VwkpYw37faquIhZTeSqCIDywcFoexQKwEDxw6FTpmBDKRtHW-yuAOSZAHVjXXlTXy4_e3ScHuS-hEqZ-kfKq1MT0ybbcqwlfQOTVKJxF8_zC9gZZ6lhs9Tc4bWR5K9IHlsuxZ5c9TrBgRy1DBkKvDDczYtIxSfZoFxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N46nkOH_C1UDtrTFIosF8vDGHVZoQZzb47aPpGD8VhHSoTwLrZ0DUXjlqq_l5GzSfkTkJ3frFrZ_Og1KLGpx4kyWRUaXSvWMX9C9b3ZgZU2sBb6ZHp9KU6sJEm_E35uss_qLCZxl5HB-bDTkoCEuiLsCunK23KWCv2eNJ_sQYqoFFjT5ZtnsgTE3oZuJU1nCB8eg_tIdS51qDG-r7IlhoDKlfNEgDUecSdm29vsKy6yW6_5S18AUrk8R_4g--UjJjtun1mTLC665pctXvXnqTwytYqiZgIL-8CDK4CPtGAdGFMse9qN2Hga4dXS6-dtlDqnQF2LyRlhwxJEWeuMr3g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
جادوگر تیم ملی غنا: کار بسیار سختیه اما تمام تلاشم رو بکار خواهم برد که با طلسم هایم غنا رو به جمع هشتم برتر جام جهانی 2026 برسونم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24156" target="_blank">📅 22:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24155">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_4z4NYbFN_HxNbFAExuQPc9BiWnFt_FoSjP4ZzW71s8-n7mxPx_EFLPbgN34EEMxsEQ5cKgP8Dj4jRSn2H85Jh6dpZjkRPFp34BOWnrLJ1vjZE9_HNbMHPk8ojm6BMmviFTuDc8Kiuv9ighbKx1SMwBbLWzdTUkbrl3ntyZ7kTkp2gRNEIS0ur8eAUGbGN2v9vAAvD7Z77LrtsRUpq77--jX7hPs1joR5-TmLuDp_oqa_2pTQnZQ22gbSVhMR9DTlOzyqyuBuUAc-Eny9Lwsr9cdnSTZiPGTO4nGH-smtFlwg-VgWiLOItWbf3MeDZ44URB5FAs6RV6UoeGhV_FUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
🇵🇹
بازیکنان ازبکستان به این شکل گل چهار پرتغال رو به خودشون زدند. رونالدو سمت ژائو نوس رفت با او رو در آغوش گرفت. بزرگی یعنی این.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/24155" target="_blank">📅 22:07 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24154">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=EJoN174EfQlY6NrzirYCkE3gaY_H3SBDUXqRQg6f1hGTfJu0wydExnObwQ6fDrVdhusSEugrOd8ChDnkQtDFLQFO-J950E3ikuL6WQIRUI7y1bfnu3k3kJ-PqHiCJypQVfAb6Q6hxxEZDOiEvYpJ5XDKXXGsJ6KRiOtQlcds4Ca4OVTZ0N-OTBuXPRGXMp6e1QcOoOy2bCnErssQEaE9VyYq8VOFV2743qndEm4uXW7g4KeKiZ54dHZoYxLqSdMRhb1C5CppaBLZ2JArEcxlyM_HQoZvP97fX6DeFuUm-Hvhq28FF6auB2fuWSDmjjb_RXJOYH1M3GmqFgH3THCFkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a29fa94bc.mp4?token=EJoN174EfQlY6NrzirYCkE3gaY_H3SBDUXqRQg6f1hGTfJu0wydExnObwQ6fDrVdhusSEugrOd8ChDnkQtDFLQFO-J950E3ikuL6WQIRUI7y1bfnu3k3kJ-PqHiCJypQVfAb6Q6hxxEZDOiEvYpJ5XDKXXGsJ6KRiOtQlcds4Ca4OVTZ0N-OTBuXPRGXMp6e1QcOoOy2bCnErssQEaE9VyYq8VOFV2743qndEm4uXW7g4KeKiZ54dHZoYxLqSdMRhb1C5CppaBLZ2JArEcxlyM_HQoZvP97fX6DeFuUm-Hvhq28FF6auB2fuWSDmjjb_RXJOYH1M3GmqFgH3THCFkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
#فکت؛ کریس رونالدو به جوان‌ترین و مسن ترین بازیکن تاریخ پرتعال تبدیل‌شد که برای این تیم دررقابت های جام جهانی موفق به گلزنی شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24154" target="_blank">📅 22:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24152">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WenGE_zY5OIr2Bb-j-r7Nvle_7LFDr1xUI70BQtISooLAkH6D1L7Y6G1b6eDwlw4Dtu2rIUb6YmGUsm5cWFGrRxE_-ieeTXL8HRFEZvXyT-8cst9BoIprYUBSeRN8fHcP37T0KQZimWRxjhvnPCotEzMiW6yZlVrzJtwOio6mZHLTnsUdDtR6Qc4VIz8uo-RVOMG0EYE1zWGZp2gqVAllKHj6mba5S487L0IDTZeE6-bBRtu5W_uY3ozGRfXYi7ZNGfWIGQhl3qqwpRzJqf1qkW6yJ0ON-amK39RVIycPagQXqjoYrJt7fH04pSz_Uxpf-1hin7yB4ahNyVodVqTuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
👤
دبل کریس رونالدو در بازی امشب تیم ملی پرتعال مقابل ازبکستان؛ این‌دهمین‌گل کریس رونالدو درتاریخ‌جام‌جهانی‌بود. یخورده بازیکن بهش کمک کنن قشنگ‌میتونه‌برای‌آقای گلی رقابت‌کنه. این 975 امین گل‌تاریخ کریس رونالدو در کل دوران حرفه‌ایش بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/24152" target="_blank">📅 21:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24151">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=WujZv0pnrHVI9kIhomI4PDfmpc3Tebc0RE4mbX6ok72oUQn2wzVriRUuXhQwxWAAJ5WqDHK5HPtZJodgLSymZuofIrLZAPr9KnzAhp_F6gixFmt2aOvPULGwVTc8iRI0lWhwpr3EoDeLgP3jtM8u5wXUpMwsF3MhL9IwdiBmXOhqlgmrVKMRLDfwCl8YMRNNkm81BH3aNcg-wWkOCRru4kLA555KHL5Y-clCTSYd813IDuv3e-Sp8VSrTKoa3Cm8_SsO2nCK-dQROfM9xfXRTiEhKpVigznSORZpYZZQbtK1nIcZWLFs4H0EfBt3jCDIyd0IWY5kA3Uq-O9ofsKG-g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/df5b6d9df2.mp4?token=WujZv0pnrHVI9kIhomI4PDfmpc3Tebc0RE4mbX6ok72oUQn2wzVriRUuXhQwxWAAJ5WqDHK5HPtZJodgLSymZuofIrLZAPr9KnzAhp_F6gixFmt2aOvPULGwVTc8iRI0lWhwpr3EoDeLgP3jtM8u5wXUpMwsF3MhL9IwdiBmXOhqlgmrVKMRLDfwCl8YMRNNkm81BH3aNcg-wWkOCRru4kLA555KHL5Y-clCTSYd813IDuv3e-Sp8VSrTKoa3Cm8_SsO2nCK-dQROfM9xfXRTiEhKpVigznSORZpYZZQbtK1nIcZWLFs4H0EfBt3jCDIyd0IWY5kA3Uq-O9ofsKG-g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24151" target="_blank">📅 21:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24150">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c38410752.mp4?token=jcg-OnDPEmzrzZV1-1tkKbNE62freP1wNSKPjc-UK-2IJcU8fLH84VRTosmo10GcdrMR3ZncpBFrS-ZgrWf6z5-1-vOAwqWr1txuoePAEtYtx-tXSiy4Aupc4H3AHZpHRQI0JeSHPmwlNnsual7Z9VQJdtlaE2jSF8_u2xaUYHb1H54LymRQ48QUR8UijF2jt7Gyu4nFW5VTMlod5TwLdtOz194gez-e9M25NW9pCDPT3S-wqlim__-ElwDzezoIXY6oaXylbKTGdtVWHxZYn_ex3MxM7Y6zkA4xCUXrjTDAghR50rsW5nS7rtzVlm7MUqbd4MrkslL1Q7XDSPq0Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c38410752.mp4?token=jcg-OnDPEmzrzZV1-1tkKbNE62freP1wNSKPjc-UK-2IJcU8fLH84VRTosmo10GcdrMR3ZncpBFrS-ZgrWf6z5-1-vOAwqWr1txuoePAEtYtx-tXSiy4Aupc4H3AHZpHRQI0JeSHPmwlNnsual7Z9VQJdtlaE2jSF8_u2xaUYHb1H54LymRQ48QUR8UijF2jt7Gyu4nFW5VTMlod5TwLdtOz194gez-e9M25NW9pCDPT3S-wqlim__-ElwDzezoIXY6oaXylbKTGdtVWHxZYn_ex3MxM7Y6zkA4xCUXrjTDAghR50rsW5nS7rtzVlm7MUqbd4MrkslL1Q7XDSPq0Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
👤
موتورگلزنی فوق‌ستاره پرتغالی فوتبال جهان روشن شد؛ گل‌دیدنیCR7 در 40 سالگی به ازبکستان درجام‌جهانی؛ رونالدو به‌اولین بازیکن تاریخ تبدیل شد که در شش جام جهانی پیاپی موفق به گلزنی میشود. این نهمین گل CR7 در تاریخ جام جهانی فوتبال بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24150" target="_blank">📅 20:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24148">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ab3271383.mp4?token=vApQEFfXm8rDBfjS4Fd_Xcgb6MN05a_SEesyXClCUw_03Unw3vCUmu-iGIDzNYQb00A8YOedxH3dYycna1urWs7zIFTjngaaxS2sOCg3vVGWKt_efRCbpUxEGQnGsm2bYGaAaCUmCmQ0wCCiRbPKaycJVOpMAqUWtvT7bKx7ADiF-x_8scDNTXxyJ6wAhfs6osAWT494bwlM750cxkchGb7p73SBvpDLInCg0Xx42uixoxV-xAUKNF7jOCNyOdXawAu4NtoKNOw7I5ApeIIYr1ZiPOrcuytiuP2VQx2cuMIs6jn_OCidXoG03IRV9beekFsGHL4Z0STS_xGaxgMZiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.8K · <a href="https://t.me/persiana_Soccer/24148" target="_blank">📅 20:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24147">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iMkwgIiK0sSB3hmdF8Ct26p1AxqX5rvZDSfUy5KEYE4eEGU6zrsHJYLe9e0AkJinmtgShUzxAwAWur0z8zYjjL0DlQxhgAhq-lNEwM6KujwhzPOhrIAD6P7RIqn42yk3eK0bh0WF9-mX1gJwWnX4sd69qxYPw6TDgGydYdwF4_sLI3OBzgdfeQeO9KV9EQnz13iUfOvqxC-GD8ftfycuP8aAXBnBq5k0C-75k7tK0me0HWiDYlf7rzn7Q9D2eWA5e6kEy1evbpC3tT3D_CuU6gvO9PBl3_nTrWg6nyK--YwLOsIgMd972j9-x106tK0gKm9qRTNGWr1ciQE6dPjFmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛خواستیم‌بعدِ بازی امشب ایران با بلژیک جزئیات‌مذاکرات‌روبگیم اما رسانه‌های دولتی نزدیک به پیمان حدادی جزئیاتش رو منتشر کردند.
‼️
دراگان‌اسکوچیچ درمذاکرات‌امروزخود با باشگاه پرسپولیس دوشرط‌سخت گذاشته است که یخورده مدیران باشگاه رو برای عقد قرارداد…</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/persiana_Soccer/24147" target="_blank">📅 20:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24146">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z1gnpopHoLiDn1V_roPcBmvwlIaqVx9INNLAtnukaGAXo7XzfX0AXCMDsLjCWt7s57_1dt5VB9fmULFzpm_qTfylENHvROITRz72eNTayUSu9i2QSZe1KTdQPjcOHaTP3Ftc3x0ZC1sHcNkzlfUa41EYj2Fznyo_EHrYTqqg0R-3kqnkzILNifkKibvleAECn66nlTQty9q1_giy60r_7tV4L6tNW8rSal4YS9Y3L5LkeRuXaMYKPTiK7YdZ3wGmuCu56Vt2SX3FhW6_b9O4tI8mgn8jtvh8JgW0XBJoXoJUhx0z8yWJtbFjRm9twlKOI39v_KPYzJVehsnK5SFSKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه پرسپولیس دقایقی پیش نویس قرارداد رو رسما برای دراگان اسکوچیچ ارسال‌کرد تا باامضای آن اسکوچیچ باعقد قرار دادی دو ساله سرمربی سرخپوشان شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.2K · <a href="https://t.me/persiana_Soccer/24146" target="_blank">📅 20:18 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24145">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A1TlD_CfUVgyhKB1kQoD1FA1vnYawc-vYP6Tv6_8FJExkVPDf-9GOtB8ZBvS4lZ4SLLCvAjFhSgA_AdZIXzYs8lZtl2joyuYzrCTInzuPcJb8DXBC5vWsikDTm6yvz_0MWChKzR5bCIxYf8dwlmmDyvXxAuXLK6-ynPeJYtrYmv8hkKs2qMhFa8CDQVffWlpx1_wTeoghOOmeC2_1GcZi3BEba1xLuD1uTkHHHlbGUVIyRFo8ACE-pD5bSJejMxRAYeOwqFlvsEGN7czsBRfurb6a0MRNRpVKYcbegumcu9KBdY-SpgKhuhsaMI7uIRFMz72qFHW2AGuusk08KFQ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا؛ باشگاه استقلال امروز باارسال‌نامه‌ای به باشگاه شباب الاهلی امارات خواستار جذب قطعی رضا غندی پور شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24145" target="_blank">📅 19:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24143">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qubVVEIHmROZELhtjIo6wcP86QmM8IvuEve3dEquy4jbAJYLMDTpUaxXNS84LXclnowpVL789KkxgMGB1rk8mzXIKl5FFPZ-0zdwNWlP2DxAJUx42NCH2U-5mfuvwtGwj-FctPQnF08ecldJUHoZ25TYmjypDZq9rd0OxLgQ8WAo2GkTGLDqbQFTViHyGc09kzIRsInFRkxmD7_8T7v5g3FK6KzThpaPLZ5QyVBG4o5AHKxh21iGPKuw6gYXwBUBRQGwYvQYcokFH2Zgsm4oiW2lgzdzJ1mcGDiKNwr_mkP1xAT7AkbkIuZrFHawdQKDZeUe6P8vcu05Ur018Uc5BQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIqNOs9MIwhVACdHqsW-b7AaKE1s8Ex6W6ARMu5LGBOT2byla42_DN6T_UCYcJNg_iP0rkFc1_4NTeRujc_2-7D0YUgpuJ6wq1QE9Wg5agn8E99yQS08-KdGxnXPzaiCQO0n-EnR5kU2ZPEMZ8FAhhsAjAEM_XI9KPYlbrQgutOW7qA11VZNsDrEVNX_bG4eKeY0OuHx431svzO3KOrm0ZqnySbk4dMUE3ZBgoKLgjSm2_yIVzjLyWC2lUZRikw419RLZXYcgerjxZYHRHr_hWrwmPPkflRJQaYsXHyV57uWH6k_ZYVBThsuWxK2cu4FOVz2N5ZHn1qlBmIaiyPiUQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026
؛ شماتیک ترکیب دوتیم‌ملی ازبکستان
🆚
پرتغال؛ ساعت 20:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/persiana_Soccer/24143" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24142">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vdXNr7qMDD5kUXxgAs3lzBM7fSZxsT2MuRmrgdn5s2jBZuG-DnzCAzQy4YFgoZ5I0YgqyGR08sT9MNC6DNTV7HyZIV-7anVSTDPtxQo-K3MzsFh_JZ2KTXPwq5KERjhiHbj31uKPRc0vAnO5qIF4Ldx-oI3G1tTxeo66xJufK0e4mDCstS8cTLQ0KmJj-wwvQ1wrsoIeg7Of_6CYxwnLWMf9czmqct9kZsqOGv6Eo9h2tu3K-5GJK0du5SW0XI9CL5rFgtyqT6p8g2xlVvg6RCOEsDJzHUlA-CcczeTXHgYx6d71IHhUS3pBy5-jWsQlZGq5ISz5cE5v7yI5_hkEdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#نقل‌وانتقالات
|داوید دخیا سنگربان اسپانیایی 35 ساله فصل‌گذشته فیورنتینا آمادگی خود را برای بازگشت‌به‌باشگاه منچستر یونایتد اعلام کرده‌. دخیا میخواد دو فصل در منچستر یونایتد بازی کنه و با پیراهن این تیم از دنیای فوتبال خداحافظی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/persiana_Soccer/24142" target="_blank">📅 19:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24140">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=iOT26kQAM77kNY2n57Z8KeJTjh-K3tEwRnTXmzHxrLH-vdSorzNQe7IdMku2TzfljOvIicYmLEP3LomYVaPAfje7J3IYWM_CGTIj0T3Sa3-zki001U_roVtISZJbTlL7LmT5A62udJdbJgyYDjootrcZpWRwwSQYQr_ij0xKil8GAZ6iYAoxBL5CDxrCMH-CUj_FOM0TR55jYcj28lm_KNc3MCfOwcC3E1chV8YOLC47vN_vOAZ86D3EoQO-011868vSE7MhFY5BvoIVTRVihT7ExdWFekZkTfaWHH5y8PJJgZeI6SOb-2TrlfP20L1qq4Kkm8MtBMMRa_sMKJkOtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/caa974ea07.mp4?token=iOT26kQAM77kNY2n57Z8KeJTjh-K3tEwRnTXmzHxrLH-vdSorzNQe7IdMku2TzfljOvIicYmLEP3LomYVaPAfje7J3IYWM_CGTIj0T3Sa3-zki001U_roVtISZJbTlL7LmT5A62udJdbJgyYDjootrcZpWRwwSQYQr_ij0xKil8GAZ6iYAoxBL5CDxrCMH-CUj_FOM0TR55jYcj28lm_KNc3MCfOwcC3E1chV8YOLC47vN_vOAZ86D3EoQO-011868vSE7MhFY5BvoIVTRVihT7ExdWFekZkTfaWHH5y8PJJgZeI6SOb-2TrlfP20L1qq4Kkm8MtBMMRa_sMKJkOtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه ابوطالب حسینی به مجری شبکه افق که به مهمون‌هاش کفن‌هدیه‌میداد؛ فقط خنده پشت صحنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/24140" target="_blank">📅 19:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24139">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1gqooj05Zpw7_IdOjbLgiR7hVwtG7xGtWsHzdY7cH7g6QAU0Mfqcc8MlIcDuGyrjsaO8bOtbe7kMlBKNPHMu-dZkY-9pKdDu63kGa7iYHpBjT07BsJqjpejvTaKT17JNzUXKTdJU6RHYik5_VGVqo0r8CEs5i7xGaXyqP8xron-clQrE4CS5TbMMqaRJykWRhD-I_OecJu5Dd3R82qMWJlwkqxW7M7Zjy2tECC4XQjLX_teQyixwhNwdMKuWz98sPfiQ_ni7EIW0Zp5ysprzjfSRCM1OpC8r4RpaoSnWmG_feDoSobytZxpMnk6BMkYxbYRmIbJyqkQUgc5bK2uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
⚽️
#تکمیلی؛ یه جادوگر غنایی که در بازی هفته اول جام جهانی غنا مقابل‌پاناما یه‌همچین حرکاتی در ورزشگاه‌انجام‌دادوغنا دردقیقه 90+5 گل‌برتری رو به پاناما زد گفته‌برای‌امشب هری کین رو طلسم که نتونه موثر بازی‌کنه. این جادوگر سال 2014 هم مدعی شد که با طلسم های…</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24139" target="_blank">📅 18:55 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24138">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HxCaY1jtbg3AAoehYJ1WiEgU5ZDNGfar-8gddSeyQDsqBomBeyZ-V828HrpcC5nr5yo34jZQ4rLySUw4fbg_F6LmtoGSt8XvZE9uMfZjbv98259MlBEBm6CcNBGRH7xiaBVZNhuxV4yyJOVzggT7rTHbueSX945dgemCJiG9EzXHnJmZwUNdWW3RqlT0hOTzxorCHP4KqLrMucv1v2ySWLVKvOkRNTshM9qef6w6vfKwpzERoZJSdkclKLgOinvjDT1KLAZx7Xk6Y0DRGra-WSpm7DMPxplsAHfZ-ze6KoxDbN2FTIwgr7R6n9LHwLdLy9nv6vgMcnsATcFynFk9zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
بازیکنان‌تیم‌ملی آرژانتین اینجوری از گلزنی لیونل مسی خوشحالی وذوق‌میکنه. از اونور کریس رونالدو گیر یه عده‌آدم اسکل و احمق و تازه به دوران رسیده مثل ژائو نوس افتاده. وقتی رونالدو داشت تو رئال و منچستر آقایی میکرد تو دهنت‌ بوی شیر میداد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.4K · <a href="https://t.me/persiana_Soccer/24138" target="_blank">📅 18:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24137">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oMJnEyCfv2Ef6JBb49L7uIo0LIpPnkNnpFhzkFWQqwn0Qfon36eQthe7Zex45U44TmvGFVmnOses8aXRL44Fgrv2G53TqaCr3KHzwmOEmRf3c-xVP3TUDfq2inDkuI3ggUyXP_48x6I9l_Z012_d2whqW1ZGwJ7V872NopuRLBjQotL4600AsHsbcw8so6Aqpdhj1x2jmOra9aLasw0G6O39RSAj-Q3y8tOPxuEHRKaCBHSc0VnPbTCnAU0U3kfs6h6HxsFLSdHZRaciSKETlZXiuD0N4wXhTLNqkvNXaAypZknGlMeb9dMwURXgFmpzXEYc0UYzCLKpMYOuUQ2ZmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔵
#اختصاصی_پرشیانا؛ باشگاه استقلال دیروز با ارسال‌نامه‌ای خواستار جذب یوسف مزرعه وینگرچپ تکنیکی 21 ساله فولا خوزستان شده بود که‌مدیران باشگاه فولاد رقم رضایت نامه این بازیکن رو35 میلیارد تومان به آبی پوشان اعلام کرده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24137" target="_blank">📅 17:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24136">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m8spNeI2PBFwiIa86TdUFgxw3VTpnNxn--tQlaMgFfIdHeOK0Jj0kRDVgIzs3b75IX23F5Y4GEVpBwPj2eg300ZA4Q3Xv-jcK4MZ7O3eK1h4kd4eimRplBkT8sCZhxLbOjrtqvTZFbEeczgeMVZcR47kBZ7m7NU4SVRk55c9IYi-gL0qxc5uI1dAPCcuG08iSytciCwK532uqcMUsDDqK_bm84z1f3xphqWN7kdRrVWqr-IOTdHSPZnVd9T5dl-7x1iRTdbLLlt9pUj9_XY5R2SqvG_MYKOKAKXpVIho-jbLvt_SPTyjKv_S-HNgQeoFNuV8ggXT6U-vTnDu36A2xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛ باشگاه چلسی آمادگی خود را با فروش انزو فرناندز به باشگاه‌رئال‌مادرید درپایان جام جهانی اعلام کرده: 120 میلیون یورو بدهید انزو رو ببرید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/24136" target="_blank">📅 17:38 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24135">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kv0Yb2hbF3qtoR8n84Zj39Sy38Ct-UzeHXVCivWSRZ3Tk0cGAUbWeSCbD303t5hVVtCux00RqqEtOvKcwF3Eb3Xc6Ql6qglCTD7c0S2OgwYKuhwmTVL4q2ezNVAO_I5STyupTsr6VO5bzLKCach2isqIvZ0eq2mdnGCqjJZ9M0q9uB17f6WFj_8XS3rjVDQYUiT6iBpWVJvkokh7regVjqZucgNCtc7wOoBLfNKWN3WPShrwvjTuWFPRI3OIx9G7Pma4IAIG9lHXxj421XnpKXkGR-eItuKFXu3knMz0V73Obl48OaaokZScLuHxk7x0aIGXECsBPkAu7MJfY-0OgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🟡
🔵
🔴
👤
طبق شنیده‌های رسانه پرشیانا؛ رضا غندی پور مهاجم‌فصل‌گذشته الوحده امارات به دنبال بازگشت به لیگ‌برتر است و مدیربرنامه های او این بازیکن جوان رو به چهار پنج باشگاه بزرگ ایران پیشنهاد داده است. به احتمال قریب به یقین غندی پور راهی یکی از چهار باشگاه بزرگ…</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24135" target="_blank">📅 17:09 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24134">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpj9CYPnl5bcteTVf0hO8LMoWWCwwYEOuN60DEe2ixK-M_SCCBRTDu7Qe760dPMS9njTcBNlrxrZNzmjFClUG54V1NsLveCKXDy1ssKJqRsFqrgdauKDgFIdqa9QeAfEMm9SFDhfhoPGuMdLytirUVPqFu8yqjI2SlFjDKVr0MgENyzuhqZeyWqXkVJvxeEzMlq9JXDZjqqImgMW_tA311Y_i7SW7tgPu4J_trhrwrJH7svSlO-d1MH79znhLIl9z85iZxY3ptaYn9OJU10N94_InIoJgkuToPRQhfEbvWylRnBX7Tnux0iBOXEaat2CVeT8n8fo7fmqqjSCxoS1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
مارکو یوهانسون دروازه27ساله سوئدی تراکتور برای فسخ‌قراردادش با این باشگاه به توافق رسید و بزودی از جمع پرشورها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/persiana_Soccer/24134" target="_blank">📅 16:57 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24133">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇦🇷
🇦🇷
تمام18گل لیونل‌آندرس‌مسی فوق ستاره 39 ساله تیم ملی آرژانتین در ادوار مختلف جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24133" target="_blank">📅 16:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24132">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">⚽️
تمام گل‌های روز گذشته رقابت های جام جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/24132" target="_blank">📅 15:54 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24131">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=rHLYaowwLGRjSI-j9tCHkTpX7LAY5f_aiVGWFWc8ScDT4efZ27JKKj7yL_tvBqkYAoGBzNOFVRJHqDETpcwAiblBuMYOJ0QbR6V_LYzWvNzRGDwjLX2DxfjS2sYzy9czG84aeBgUoxj9otmXq7Dv-i6inoqijt04wba8OO3MspCwoqev4zr7Vyx0PzpPzgFHi38ryrwZJwtl29JpzoQepW_BrCn0vLXA7H6tSr7OuTpqqF-CqRIYwtlaWHbuKorn3ugkjDh5HBMhuC9EyRl5ENOF3Xn2DWMOLj_fFmotmWhmmWZYQ6F1ppIjKvXqpcFBlrHYsbsm4ZMxzh_juJvqPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/85fe00b3fb.mp4?token=rHLYaowwLGRjSI-j9tCHkTpX7LAY5f_aiVGWFWc8ScDT4efZ27JKKj7yL_tvBqkYAoGBzNOFVRJHqDETpcwAiblBuMYOJ0QbR6V_LYzWvNzRGDwjLX2DxfjS2sYzy9czG84aeBgUoxj9otmXq7Dv-i6inoqijt04wba8OO3MspCwoqev4zr7Vyx0PzpPzgFHi38ryrwZJwtl29JpzoQepW_BrCn0vLXA7H6tSr7OuTpqqF-CqRIYwtlaWHbuKorn3ugkjDh5HBMhuC9EyRl5ENOF3Xn2DWMOLj_fFmotmWhmmWZYQ6F1ppIjKvXqpcFBlrHYsbsm4ZMxzh_juJvqPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
زلاتان‌درخصوص‌لئومسی:
من تو دو تا جام جهانی هیچ گلی نزدم ولی مسی تو دو بازی پنج گل زده! براش‌خوشحالم‌امیدوارم همینجوری‌ادامه بده.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24131" target="_blank">📅 15:41 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24130">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rY_ZzEDAmHu3o1gclbKDQ6hsfLpnZu-IWUWe25b3F2SH2FNr6GL92hXpHJ-UkaZALCDXx-tRVw6NqNLxbkgvdqLV0fqRGmoMDHFVZd5GEm7JFBR6V8HluJFNktPODf1NY4VRmVVKIpuThhlo_Kik1WY6Y7QsShJuX0WBjlz4KzddT4sJZn4IDDM33UIHXP4LgBUvPDy86l5If9YYpJyh8b0xPi42Zq5feq-cGvWWYHchclYdFk85I6Y2xuyT5JeCzysQUSCAJLqrqcPmC3CwaQDNqiBkHsqu1pf-TmniYQf9E8adCPS4Gmy6YxklLS1IjhRxnaYHDyDfMbNijoSebw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
فرمانده روبرتو پیاتزا درتمرینات تیم‌ملی والیبال باقدرت هدف گیری 100000 از 10؛ عالیه ببیتید‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24130" target="_blank">📅 14:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24129">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_fSteotHreUTNz7qlFB0kFVsukIuYE2U9O7b4m_9ZebeL4tD0jIfiQuEgiHY7UVGwd2ZbgJYrOzagwTZWo1-zlo3wrj_6-bYaWo20LkyT6nDab83oOcK2y_s7A6fMzCq6pRnVAVeiqsFI0Dcy_f4A5koEjTQrQiMLpmuwHNvcme2VyWSbqWUM9GzqhW4glFYVQVDZJ6jIrW9PblXpoib9XvzTzsLc0Zg0J-1_Qjq_1wy1Q8QgP-VUGlCoJv9oNntMA00ENTQIL_oKFptM84SroLgThisewnCsESQHCDjjZCJ1s5rhG8hcQh5QLPzxFZmczgmAfS5ZPG-ifiE_affg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇪🇸
نشریه مارکا: ژابی الونسو با آلوارو کارراس تماس گرفته و از او خواسته به چلسی بیاد. کارراس هم گفته با رئالی‌ها توافق کنید من آبی پوش میشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24129" target="_blank">📅 14:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24128">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K-ac_Iziqp05kAYzgdaLF5V4Rd4VqTwmmfXxYzTkZjhm0fdBXW3xhjIKHwiXGKoQtoT1nVAtfsHuOaIrvYOm857eLwjXZQJ2ZP4UYseGcXICAdP0tHV7kwMvo-xYFt2WD7j_RcEcx8rdzPH13FyG3nH95tx3p1pdKk4RkIO0CyUzUrGpLYk2zti37cZGKcyz9yhT_3TsygTsnGQrntNVck0SDuSvw7Qv8N6vzhnevJPecgkj7saQaii3yxmVaM0o6U0H_XeEHb7UGqSPQfM7Rv50NMFY0l2ZKzl-8qLmdUSor6tHO89IztywK17M5mAzNx671E58cWq6x_3CyGdF6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24128" target="_blank">📅 14:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24127">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=f4uUfWN1APq4ZI7rNhaOE0FF6EZ0mQlwkJW53edGqN84m98K8Oiah3Vj4Rmpc8vOoUvZsIPBHPv8NggM6O07TNjB14b8PERwriRHhLqDLAr_zvkleGSxurPal-TxW4A8xrex3iSz62oeimaEyoSlZiqFF5wDcOFwOXJpKpyaOIl17ee4TCfhppnyr1t2n3Z7yoInWEj3QA-661U9f52PlEWEevwsIqb9M60y9ZyCrgD5TfCmFSqCEY6n6AnfKzqH8-QyqyWo5yzdesshNmfPNxG4_8IQTEZuOKoUfcqSolyAuniZH60H7WK31WOWcwqLuOOE-tcWxLutguvp-ucOgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c20859db3f.mp4?token=f4uUfWN1APq4ZI7rNhaOE0FF6EZ0mQlwkJW53edGqN84m98K8Oiah3Vj4Rmpc8vOoUvZsIPBHPv8NggM6O07TNjB14b8PERwriRHhLqDLAr_zvkleGSxurPal-TxW4A8xrex3iSz62oeimaEyoSlZiqFF5wDcOFwOXJpKpyaOIl17ee4TCfhppnyr1t2n3Z7yoInWEj3QA-661U9f52PlEWEevwsIqb9M60y9ZyCrgD5TfCmFSqCEY6n6AnfKzqH8-QyqyWo5yzdesshNmfPNxG4_8IQTEZuOKoUfcqSolyAuniZH60H7WK31WOWcwqLuOOE-tcWxLutguvp-ucOgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
جادوگر غنایی: هری کین رو برای بازی با انگلیس طلسم میکنم، قصد ندارم آسیب جدی بزنم فقط به اندازه‌ای طلسمش‌ میکنم که نتونه موثر باشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24127" target="_blank">📅 13:42 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24126">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZG9FWNIYoeAzUVKp7NcjWUDJTmaAbgOPyeOC7N57JiPGwmEhgJ_K70L0MjUzeDGINIgayr0RNpaZdNxqr0gmS8iMVzBzLGTrwWBqk3dARdWUVWpriImVrkduhbNX6Y5vFSkL-ANdOJzgB26f4yyRT57ZeQabeGNm7kla94jysTlhif3Hlo2DnK5oC28_H8qTRSgWDrZjMMSb5CCeU9E2-3lzEi1kA2eUHXp1haQ74iynrEcZvD38uhHhqqJS_lI102ZFXF-SX5F674n8Ig8HZf1oY1_7nTqaup1eLo9Dk-MQk7c-RuQkUjIc-ya6T3YXPQ7ZU4y_i6BfZLYdnKMtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
سه ستاره جام جهانی 2026 تا اینجای کار؛ رقابت برگ ریزون لیونل مسی 38 ساله با دو فوق ستاره جوان فوتبال جهان این بار در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24126" target="_blank">📅 13:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24125">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VMwaeA-6nwHP__PypJjTiCUCcZtz5p9Y3BxPObPLFhqgEsOg_lViGCZpqVakkF_IhpFG_wMKR-4Qo3Ly8H1sogY1UdEJ3xfHj0G9dVqSS9VmFhvDx41wf97cdUz0oP8_GBCEm0bf0qiJ-imORa87tnsQy2mFLs28KS0YtnqRz7rBJuQNV31i4r8oYzfPHjks-x7Bcl_ek3Ld_pf5LdJbdX0ebHX_fEL46xXMOQsNtHyhuo4Q1o3gXBwPt1HhMxf_YeYEA3jo7F3481uAbRc_jEUc8IT379RX3NohdA5eUWJmJ2x94aJoYBnjnMEa_pLTyDYkeE7y-FUqa9fZBjYngw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
یکی از خبرنگاران در نشست خبری قبل از بازی انگلیس-غنا از کارلوس کی روش راجب باخت سنگین با ایران به انگلیس درجام جهانی 2026 پرسیده گفته اصلا یادم نمیاد. مطمئنید که من سرمربی اون تیم بودم؟ من یادم نمیاد به انگلیس باخته باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24125" target="_blank">📅 12:44 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24124">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2VQ_BpBg0hChDFDpaqcKS6TUevaZJL9rLn-08NPgDeM0u2PTjjvUIEfoJ2t9uzQI-L-XiyLygUJHxiAISfXiuLxTF9NbzPk2Mc8rdI9ccz8V6E0430W1f2-naFxAlJRmPRtgag4Sjiyfhqcfy8mRqvEcYzV7FCOccRtscVPptZ4Hl51mIqkygpgBuT_dsq9FWNSpf8dxMDRCQCJ1qsRiE7dL3ZWdqYfB8MuemSpe2aoneP-_rGPzS-J90RmSwfUPJUpsxeY1QUFyynmKwCNfCi7C_v_h4796UFjIaMpUrrrJYT0y2QrWKV-iluc6AbVHSUCKE42jJlWcoWkbVlM_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24124" target="_blank">📅 12:12 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24123">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBr2UKhzu2_bwRAne38KOj4Q6qfz1z0U56taC_v5Dm_eQGfux5bBk-xY0G-nlPOxE3p5n2m-4ZssZf3MXKUZbfeE9T4DdHjRohHxEcrft6aFQNiF8209QqhAHiJ6kw-bRcg3bNoyL5gPS5XMoK3MobZEAahpQHfkPrebKzRSiWoIzM5Z6MdhSd2EvT-9YzObXMuCgelxNzGqa2-ZVEJkCQR8VGexmMWYQUL0LGpRY1SOrnv92im88hWTUwLyvoNhmYYGbUVWCHT2Y9ycbbBWGzh8x7DduFYpNvC4WiPlevSudkX12ftQGOaaIU2WXmFngz_IThFlvRnOblXHMrmNmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌نساجی‌مازندران درگفتگو با ایجنت دانیال ایری مدافع میانی ملی پوش 21 ساله این تیم رقم فروش او رو 90 میلیارد تومان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/24123" target="_blank">📅 11:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24122">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K6VmxLt8HFwm17ORYwTGOQOzRpAmg_T44sJhdlZz--CmLT7YVkJtjHxkkFNkHdtvc67BI2UTrLbF9EoBb-Pbsyk0idLILS545wGy02MwZxplkyF3Wn670VxxouffucwSVzqGLzNmlq53TamtAudqsimumqVKblLIsoOYxUg-DNqCXNp_pFRcGeuKQZlxJHXNyqAZywqFvVoyeOE9MU_gpEzPB_s4iKKtAUe2YJfaAotZSJdWNoOLsBhsGtK_a3vVAknCEB3Fe_wnaiSKuRVWzXOZpMngy79yGgMyD6PREYHBClRgi1vCA55IGLNVw8ic_BvIrG_-apDcMYGlzgtTiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
سه گلزن برتر رقابت‌های جام جهانی 2026؛ ارلینگ‌هالند هم بانروژی‌ها داره غوغا میکنه. دو بازی چهار گل‌زده. اگه هالند درتیم بهتری حضور داشت که اسکوادش بهترمیبود و هردوره درجام‌جهانی حضور میداشت قطعا الان هالند رکورد کلوزه رو زده بود.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24122" target="_blank">📅 11:27 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24121">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vjOMU6FmVJF71kQfXzmhU0dkDZ7CSVVRQci3YtgvUG9nLHlW7TH-kRtMFiR0O1LZfBwMPr5vWlaOevjFtqlGJ5h8ioaQ4PlZxrFCzJ9pUs3zQovUWe_YgcLdRpLqsIkHeGAN3QCi4YtZ9BgYMQyyNfbSQ-cFa4ctOo1orHdxOjdlnhW-IxZ7snQLfrMTMb43jpMMXDLfo9T72V8PJYcyaxCm99xqgO4TmWypvWkPzDtpGbsdiqmsDq4zYfV-RrloWULjRgfv6ep2MoESZiXKBKqXIyEzU3qmA48FLYrKBS0KEePB2vr5Y90H_quUen5L8SIzb6R1TpwAjSUYVXP-jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
عملکردخیره‌کننده‌ لئو مسی درسن 38 سالگی: 50 بازی، 50 گل‌زده، 30 پاس‌گل؛ همچین لئو مسی درکل‌دوران حرفه‌ای خود 916 گل زده و 414 پاس گل‌نیز به‌ثبت‌رسانده. یه پاس گل تو جام جهانی بده عنوان بهترین پاس گل‌تاریخ‌جام‌جهانی هم میگیره.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24121" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24120">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=RX4J_w_ObyZtn6P6Ov4lqcruWdi_lP_e61IOheKjI4R_woY8VZfiHEu04cA-UNAwMvBQEiGchi81b6tieKHyVe4GypWXyYvsYOqAssi0ZjIjoph7sDnWVWxpBBmBjFYe6Y0A6ps5_vwVFV48vvCIKSrlBBPPs4O-0cB0DgcaXSVpSjdnZTkHtNbmLmvRiFaM0EN_R3tavqvvJF-qiDGKyBt2lGvDa7-GD7shK75EVfPZpDxv4I4DECBMlVfIuW7Exo8cPbBzCw5bNP67vd2ZlbVslI1Xzw3J5d0f-qFI_apdCtOge8AY43ckGJNUW1F1cVnJw7GTIDtDr5Rad9Dh2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/858e98f07e.mp4?token=RX4J_w_ObyZtn6P6Ov4lqcruWdi_lP_e61IOheKjI4R_woY8VZfiHEu04cA-UNAwMvBQEiGchi81b6tieKHyVe4GypWXyYvsYOqAssi0ZjIjoph7sDnWVWxpBBmBjFYe6Y0A6ps5_vwVFV48vvCIKSrlBBPPs4O-0cB0DgcaXSVpSjdnZTkHtNbmLmvRiFaM0EN_R3tavqvvJF-qiDGKyBt2lGvDa7-GD7shK75EVfPZpDxv4I4DECBMlVfIuW7Exo8cPbBzCw5bNP67vd2ZlbVslI1Xzw3J5d0f-qFI_apdCtOge8AY43ckGJNUW1F1cVnJw7GTIDtDr5Rad9Dh2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دخترای‌اونور آب واقعا عجیبن، از دخترای کشور خودمون بدترن؛بدجور روبازیکنای ایران کراش زدند‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/24120" target="_blank">📅 11:24 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24118">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RgNI7FmMk2aXigbl37UnH7tJky_eaItIK4VrUWUWQZ63O9KLkud7Uzw7I9QWX_i49FCUS3kBs2mBd18udoikiEAbGsr-uNACohuAKNi2mtG2ldMG2VsrK-KcoMppNI2hY0LPqFvvrs0IcD3fMLldflvA2dMMBjRh8l_M_rGHs22zLNzN_wxI1fPnDClJdf_06ntKWu5qMftoZASNAc59bkkc0bSo88CS9OYcMqVvivo9uiDBWaGVvsN1AocBaqC0HrX9RH45Kok5Z9XHPe7Lfapma-It_OL4YLUbI9bPRF2IjzdhCbhyt6OJ5IkCsyZKsR0tIZ_uabduyH1HRjMcgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛پرسپولیس 5 تیر بمصاف چادرملو میره و برنده اون بازی روز 9 تیر با گل‌گهر مسابقه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/24118" target="_blank">📅 11:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24117">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C29KF6CnqRh5A_yr-3xaULTj9zEh_pEzYhSWJ3Q5-hasgp6k-JM_2VIXnr8kmqYK_UkGpit9chue9exGaqR_3salka_-CkfyUT1GJDD2u-cdnzZBFRwygwy_oatH3AgdJwh4SabB1xi13wA7tFzdDyC8GOx2i8AfTVAUfybp856SWu7eWjpLfUEcustkMqbzHEK1x4dW3RZA4wOO-cs7ljoR39ZRsDLlIp0joLoGec3Vdc1EItaCuuPIbsbxpG04ZjX8V3CimXGe_D_KrXORQYk2fnm7jfOdkEQ5GaiLF0rbNI6jJjvC2whPRPFuxRaSxGFOu_Si6ILvVmcneQ4_qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#فوری؛ طبق اخبار دریافتی رسانه پرشیانا؛ مدیریت باشگاه تراکتور منتظر فسخ قرارداد اوسمار ویرا باتیم پرسپولیس‌ است تا با این سرمربی برزیلی برای‌پذیرفتن‌سکان‌هدایت پرشورهاواردمذاکره شود. اسکو در پرسپولیس، اوسمار در تراکتور؟ باید صبر کرد و دید اوسمار ویرا برزیلی…</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24117" target="_blank">📅 10:51 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24116">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdhdhITzNB-YaaYKNW-qC8s6GlEW9DZ0s7UiJLBCV69Ke3xBzhIdUAgVdpUopOnzSSsrkRt12xFgOvwepW41oCP3CSXq87MuYHC92xHBy57HcxdiVkUgH8EzgqnlYE0DoVPWA27SDbjbIJ_Y-zOub2JXJ8oz-FuUJ97wLWr_mNGPtcfQKDCMvCSAtSv3DjQVRhFpZgL4qaoTB3Bq0BgLsgoru47zDrL6qcMyoWuH29zD7bbRrIdbSPYpSpjA23g7QXN1TlOZVMWkeJTmRCh_oIPUYoB53NtCqA4ga62TeOYXTkHlRTNADvgiZHIZgUPR-ldF8HOqJ6E87UzreHQMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال زیاد دراگان اسکوچیچ کروات روز دوشنبه یا سه‌شنبه همین هفته وارد تهران خواهدشد تاکارهای‌معارفه‌اش بعنوان سرمربی جدید باشگاه پرسپولیس در هتل اسپیناس انجام شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24116" target="_blank">📅 10:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24115">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=G5P4bywyvk7aL8pNitZHFhd17Y8i0FMoKvsaU4Z7y4DnESrWCFIHchCR9h073WssiHEewX0aD2P0S1VpJkU6iMLPT_U9PnOY9Zu2IpnTA1HgTO9JHu7vMomKYUuuzGhh3Z2EkQ2YIpO4NvrwHNSXzAuttjCWMO-Jq4-ZTYdQLmWsHeecVQUrzT0knTZN8xNCDvWy08-xo_PYm9S-3eXcYsTYpG8ZtC1P5PO3daBxL89Gx-1S9LnBmQdvkVyV7q3Use5nW4Xjhtymxdx33-n5HpMWBJa7G4ZwQTz9N-3LGt_qBPu8MnErlm-2EIM6lc0ZCYnBOWOh-oNRwiMXvN_G0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac7529e6e9.mp4?token=G5P4bywyvk7aL8pNitZHFhd17Y8i0FMoKvsaU4Z7y4DnESrWCFIHchCR9h073WssiHEewX0aD2P0S1VpJkU6iMLPT_U9PnOY9Zu2IpnTA1HgTO9JHu7vMomKYUuuzGhh3Z2EkQ2YIpO4NvrwHNSXzAuttjCWMO-Jq4-ZTYdQLmWsHeecVQUrzT0knTZN8xNCDvWy08-xo_PYm9S-3eXcYsTYpG8ZtC1P5PO3daBxL89Gx-1S9LnBmQdvkVyV7q3Use5nW4Xjhtymxdx33-n5HpMWBJa7G4ZwQTz9N-3LGt_qBPu8MnErlm-2EIM6lc0ZCYnBOWOh-oNRwiMXvN_G0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یکی‌از یوتیوبر‌های آمریکایی وسط بازی ایران در مقابل بلژیک عاشق یکی از دختر‌های ایرانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24115" target="_blank">📅 10:00 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24113">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=KYAOQtUOtHnMUxSr-yp08AJIjZ6sdiDws8hwR3qemjsc8H9KjbLSDO-omFttWPiG9mUxMVRz878DzknG9k-ALTdN6W2QgZfpirJpIALZhvknIBgyabVnTKBhLjEK0rxUGVUT1rdcqKbEseJao5IvbGrUhaccP04NKAMU5koreit1iScve3tYKgl3JNLlWamc35NiLxJQ6GHsTr9ceq2IB7WqnwPG7SzXDlcFZF7pv3pxQ4N0lXXcXKizNnPEajebUvrtE05qLqTk1vfU6TTcEM_KckyaWyT7Qpj6eS7gN8wDsnuPCABvmzjd1t4X6Fb2JeV475-Jy5lXo10lGNvwnQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5bb65aa0.mp4?token=KYAOQtUOtHnMUxSr-yp08AJIjZ6sdiDws8hwR3qemjsc8H9KjbLSDO-omFttWPiG9mUxMVRz878DzknG9k-ALTdN6W2QgZfpirJpIALZhvknIBgyabVnTKBhLjEK0rxUGVUT1rdcqKbEseJao5IvbGrUhaccP04NKAMU5koreit1iScve3tYKgl3JNLlWamc35NiLxJQ6GHsTr9ceq2IB7WqnwPG7SzXDlcFZF7pv3pxQ4N0lXXcXKizNnPEajebUvrtE05qLqTk1vfU6TTcEM_KckyaWyT7Qpj6eS7gN8wDsnuPCABvmzjd1t4X6Fb2JeV475-Jy5lXo10lGNvwnQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
عادل دیشب باز هم اللهیار صیادمنش مهاجم ایرانی لخ پوزنان لهستان رو به ویژه برنامه اش برای جام جهانی دعودت باز کرد هم به لهجه‌ای گیر داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24113" target="_blank">📅 09:40 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24112">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZjAXrGZ5ZPxiQAcwFFTobQaOwlNK5K_mXfHTMW_5kEkPZ2tBZPmi7-6tlAo5o84d_NJ3eswCqOCXDJfcZb5u3x9dgVEPDQDuuMeVFGb61NheAcZw02vsuStEywZE302uEVX8mihqdWDBxlUDYlsUCWPMP6usvcBeUvLWzrrGCxbV2IO8Oq8lOLUk0hQ6yJ9l9MfajlMMTzRi_XZXApX-mAig8K-evbynWvWEnKqdlFz9h1C9Jq9YR631OjVHoCyytT3ZUImCjj98VGNXwzovN2-aFeo4T4pohWnQQg8fiy6u6lD7zvFv6hpLJMzYzjYSqq5obSOrMaPzxhPL926b2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24112" target="_blank">📅 09:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24111">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GS8-AudpHsF7MGfQaMmtB0_H5uPqIurTMBcBV2E1f7E0blsfMpvtWDsPEFOymZrociPmI7KvsPA1XFrFJPPbDSNt1TMlD2EtOcSMYuK9oblrSrdjNGMBR-PxlMC__qT4rjio91VEVgpe9BiNg58Ynj6cak5xhvQEY7gsMzvc5mj9FflutZJpgUrD2eCIhFM81VVq0pBolbJl8ohZlTN7kFaZeqfZ_XN9JiZeG_At6HoikuIMWpZcohQ2LpZGN0u_FWPO2Toy1e5-6mgluqCdWNPDv_R4kOisKCc5SZwn3ZtdnoHZ3jKAsbicCQZ39NgXF5EKWpGfQz07vpRGsktUbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24111" target="_blank">📅 09:02 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24110">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ttj0E57-xWcYNF5ppY6DvI1CccXH4VqB7UAc0L3TXTEhcQPUj9G_ebScAEGyBd432ffwTQ0Sah_YH3oyvtFNVCknoJXpHqspBBm6hAsdSu_iNyJUUoMtEDKEt80u0i5xOcNTbZF49qy3ghtw3OEzgvBdrKQmOHw8jZp6v720fIwSXximGiEHNGhXysib6tPHgmYn202nwKf5LANk9DF-nUaLhAF7SIk3V7m-5E4yA_GCqdqq2P6aVWwckFOjZVY9B9gP0m1r8GwxB15iaNeg6IHFrknqo6uTy54a5xmnvChqPr-hJrfpUYPtBaXqP05Jq_EBdQ1rmeZwZ_YoB9o85A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول‌برترین‌گلزنان‌تاریح‌رقابت‌های جام جهانی بعد از هتریک لیونل مسی و دبل کیلیان امباپه
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24110" target="_blank">📅 06:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24109">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24109" target="_blank">📅 06:17 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24108">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/degW7AXxN27aIhFkPnqP087ujJtt2gCfYP8a742FY5rJyPQkcwaTFD60u1AU80v5OgSf8ZO1IRVTlVLpMLL3GTpXTkd13kb7L8GLUPc4eWXQbXGRLBZLtsSRVSssm_R35Fe2myAzN0gxFe3aZxs7MPp5L_SZZcI33Cxq2-jwOGynkC06RIblzfP57Ww7ND2sM2W3gXzm36ijVkri0UKaF5iaOpHVc93JXyaIogefjVPhilrHLcp1iSSL_cVV_Wt2ngw6uJMXVr2JUUrTLXHc1xC2Ik7odrOH0KnExpVL_S3EOvCfP_VohhcXFLsrjwo6IroQJfCGX8SeKtgC4y9sOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
گل‌های‌‌بازی‌امشب‌فرانسه
3️⃣
-
0️⃣
عراق؛ صعود راحت خروس‌ها به مرحله حذفی با درخشش امباپه، دمبله و اولیسه مثلث خط حمله خود؛ کیلیان امباپه بااین دبلی که کرد تعداد گل های خود در تاریخ جام جهانی رو به عدد شانزده رسوند و بعد از لئو مسی به رکورد تاریخی کلوزه ژرمنا…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24108" target="_blank">📅 04:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24107">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">⚽️
هفته‌دوم‌جام‌جهانی2026؛ شماتیک ترکیب دو تیم عراق
🆚
فرانسه؛ ساعت 00:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24107" target="_blank">📅 04:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24105">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h51F-hA2AYyke7y_7Lcf8OGjcGzslzrco1t21GYQcdGjgE31hcp3UNBTPy_PMQaNtE8kUN5ucbSKTEgaSPlmTxDQksu6vRLLxSd_eJaNajO5555zffE4imhEMr-byIHOUTQ09OP0uzV7bOyC5UU-iE5fDe6BH-VWdleCHms5AF99LoK0Utn09M_492xm4zqHbLI-K8TEFjTSAUOH6avkf0dSHXD6ZU0XcUuwGUtc0sVYQkMf2JonfMbrpP2HShtVFe9R8VKFM1M7B0Lqn1HwPS8HErD7fuM-RQqlm0zW9hht9cbHMjF9L_foRm_pBQcugW2NW3_Mqf--X2VwEOADhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#تکمیلی؛ رومانو: شماره 9 فصل آینده تیم بارسا به احتمال99درصد خولیان آلوارز خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24105" target="_blank">📅 02:43 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24104">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSIlPn6YgPh3qYNNjeTK9SI_ITQnEz1tWkK2TELq05Dxjb0rGcVScDn-aTB150WO7Qwn7YI9AndzMqa_--cjao5NyoR9EhxUq4qi8BB-hf_KBMNXXa28_yPDwMv8eOl_1ZzieR7pEdeTRM-mHQ4MjkJHc4nNXsGKpxXzDOP_kl5zU6Dno1kDEjqwCDlFoz_FzRDuG8SkNol2N4KR4DJCT-VHou2_vBGnn_GTlWkEutSdBbNj_9iGJiOViRbbCBpR9bQ1KPr4TAbu2rqUi-C2RKCl-PUHUPD3YoQbMtsCUPSfX-scrxP_2KYWywEIRtUob7Zy5Zj1iKSIqxrOyCkFEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
پیشنهاد تراکتور به مهدی هاشم‌نژاد: 3 فصل 250
🔴
پیشنهاد پرسپولیس به هاشم‌نژاد: 3 فصل 180
‼️
ستاره ملی پوش فصل گذشته تیم تراکتور بزودی تصمیم نهایی خود را برای فصل آینده خواهد گرفت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/24104" target="_blank">📅 02:25 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24103">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bgl-1RS5WLv7nZdUNtbAhW9kVVVU1VH9kjcvDefxMvoMBUopp8yzEjzzgUYJKW-fYxm0uhikQZbeKu5YbnysQtDTSbWclxVgZUu2qnUzwgIRRhIq_iZkf7HdmiEhQDdl11LbljJBwVsh49Z_UXY-wQ7LFHlvbjqtrDmYui8mBcyYt2vP00LZG3tb_KCryB8q8WJvq-LguZQ0-WCf31AyTnvnDHf9k_o85WC7T_eFdOqhXLj6qQe4TGHDB0p2F0lgFN0kLL_HpTu3JS93gwhdauKFquPoCjLcOaRYvbou0eHk25dmv2uwY45GImUBYZc2uqC3oyE8v9HtJbZHIaHl4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚽️
فیفا برنده‌اصلی جام جهانی
؛ مروری دقیق بر ترازنامه‌ مالی ۶ دوره‌رقابت‌های جام‌ جهانی نشان می‌دهد که بزرگ ترین تورنمنت ورزشی جهان، برای میزبان‌ها یک‌قمارِپرهزینه برای کسب اعتبار، و برای فیفا، یک دستگاه چاپ پول بدون ریسک است.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24103" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24102">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=ZkICUFzOnheAPWZxFKrweQJ8yjAFcCAoE9moyhENRNya0YQPDGTy0MlMvafrh8ty5xdgwehlOyzWGjp3qzhFKaCBgwNZwiXF9AdMTDZUkLjkAATjLKP9SW9hm2hscVbeLB0DoSb8gg2E-9Z031qKoGv64CyaMi4Qms_jty6WIw0LKmj4wV3GlwerY4bGv7TJG8EEJMFk-0tHki3VZmdce9K1AsVSf1my26oSVsy-10olxicG313IvLMNzVQuzhsKXEN18ZktURQs38QAKGxjr4Eo2rw-WoR_KoV5h0ySKnpl6pCAdCBQoVvtyjSVV05l2C7VGDgrQbSWP0I_62qnkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6ad27d0d3.mp4?token=ZkICUFzOnheAPWZxFKrweQJ8yjAFcCAoE9moyhENRNya0YQPDGTy0MlMvafrh8ty5xdgwehlOyzWGjp3qzhFKaCBgwNZwiXF9AdMTDZUkLjkAATjLKP9SW9hm2hscVbeLB0DoSb8gg2E-9Z031qKoGv64CyaMi4Qms_jty6WIw0LKmj4wV3GlwerY4bGv7TJG8EEJMFk-0tHki3VZmdce9K1AsVSf1my26oSVsy-10olxicG313IvLMNzVQuzhsKXEN18ZktURQs38QAKGxjr4Eo2rw-WoR_KoV5h0ySKnpl6pCAdCBQoVvtyjSVV05l2C7VGDgrQbSWP0I_62qnkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جمله سنگین زلاتان ایبراهیموویچ در ویژه برنامه جام‌جهانی: من فالوور ندارم، اونا پیروان من هستن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24102" target="_blank">📅 02:21 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24099">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c65Up4ptVlFQ09hl4zaJ2gsDZ6l9v60i918MwYJjqr4gWLvmCJWH7BEOKpDDYlO2llhfJ0eQeIKLe24S54F9PqcjMfMv0Cktf5Dr4b8gks5llh2OSoe8gisM3b6K80GU7sEF_gs3JprvqFXQiS46rFr1imNtF-sDE7UPErtqt1qMIhci3L1XtpkUeBMNAfna6jTG135RQ-IzVWk-Zq1Z74iXdmuIGCnHedGrDFJpwQXK1c2KTZtMv6shnpkg7F8leCsbZmbMBvGKNklyUr_AY7BuS1KrIVgXjBDCjvBU2QA4fXscdQNYINlZXi_j72YZ6Xd29Ydsev2OyDMsT_-AmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🤩
#فوری؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد: میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/24099" target="_blank">📅 01:37 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24097">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVJrz8l1ZH--WKj_HfMVneKVu5ykcpNDKmOJ8RP4eshl1JkwSPXYHx7JKPxvisQ3pDrmr9bOyCqEUUMtA8sGuFr6uSxbtQ3e5PG4xpV0qdMUGV9FncAr5_ImznmB1TQ_2FUfbAyUfaGsdGepF6R34AKfVZfQ4GEae3kqtn3GN5_UfxB7rm46p4eyRUwUp8tKR46ZDroZYcbrkiDZh9O7qcwOLDN4fi30dAw8eaE1pNlrAauQCQuRSgT5sCqfXaIsfdOlDpmM5h9VvWNN5Vudh352HUCzMqQe-nz-MNk7KI5ZcRXJF7wvj_vymhLMplZQq2ziVR7zoH3cACU3UcURIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ اگه فردا دراگان اسکوچیچ قرارداد خود را با باشگاه پرسپولیس امضا کند بلافاصله یکی ازستاره‌های خط‌حمله تراکتور رو جذب خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24097" target="_blank">📅 01:30 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24095">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=pOAjlissVNFe2ekw49WqrS15y3f0slrdWPxFl0nHuzak1Pm6BhAW1bXv6u2LBxicBRbJPzxx6fLbib75COQJi3_j4ZMYUE7TxUnrHREhB7PNzxFTXu0kWXD5Fx45H4JBK6t3tKl3Ee_GR1vgBwIE6eNced5Z2Jsi3_o9LtFMFs79evUb3LLkPEZL3TOjJEdsLfyhK8CSkEY1xE3g_j_K69I7d2oSeCb7v4ubHgGRkclixfeTdQFmBtzu36Cjb8-nnksGh0387o04iJoEpBsxEPLb1HgjkwNdC5lNn61bYTjalrtoykla4hGuU6zpqERHAZ5RTSvNAsbCJYe-8NmkSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f709c9542d.mp4?token=pOAjlissVNFe2ekw49WqrS15y3f0slrdWPxFl0nHuzak1Pm6BhAW1bXv6u2LBxicBRbJPzxx6fLbib75COQJi3_j4ZMYUE7TxUnrHREhB7PNzxFTXu0kWXD5Fx45H4JBK6t3tKl3Ee_GR1vgBwIE6eNced5Z2Jsi3_o9LtFMFs79evUb3LLkPEZL3TOjJEdsLfyhK8CSkEY1xE3g_j_K69I7d2oSeCb7v4ubHgGRkclixfeTdQFmBtzu36Cjb8-nnksGh0387o04iJoEpBsxEPLb1HgjkwNdC5lNn61bYTjalrtoykla4hGuU6zpqERHAZ5RTSvNAsbCJYe-8NmkSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🤩
#فوری
؛ خولیان‌آلوارز درخواست خروج از اتلتیکو رو داد:
میخوام به‌رویام برسم؛ با افرادی که باید داخل باشگاه صحبت می‌کردم، صحبت کرده‌ام. بهترین گزینه برای آینده‌ام، انتقاله؛ رومانو هم گفته: منظور آلوارز بارسلونا هستش و اونا به توافق شفاهی باهمدیگه‌رسیدن؛ رابطه‌سیمئونه و آلوارزبسیار سرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24095" target="_blank">📅 01:19 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24094">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=Rk1zZGNwJ-91u0T6jeJ0-z2u0LQOL0UNrQZEV-aeO5t2PAeTym-5ZG3Cn7DgPFw4ZWHFXr8exFQPor_BB3A_veQZ5rFLI0939FnlDNOVgS33g-yGS77ZimF3VjzcYVT1CtieT_uBeca_veEEmy9epgoE55sHWXqHgHdy35wjs6Ben-T_kxfFE_86MdtRkMThMOaIET6PDy3GvJedzggYL0whDs2Vea2NDmpIxtQEneOuj7LBqrO7bJfv6af2ORtD7DpxaRCOVfRiFZC02Bnw7nDXN2NG3jyScdUd0Skl-jkf6lu6rxBx4ce_pw5bgQ2Q1l61dcJkk_oD0XCmKYW6BA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6f0643b9d.mp4?token=Rk1zZGNwJ-91u0T6jeJ0-z2u0LQOL0UNrQZEV-aeO5t2PAeTym-5ZG3Cn7DgPFw4ZWHFXr8exFQPor_BB3A_veQZ5rFLI0939FnlDNOVgS33g-yGS77ZimF3VjzcYVT1CtieT_uBeca_veEEmy9epgoE55sHWXqHgHdy35wjs6Ben-T_kxfFE_86MdtRkMThMOaIET6PDy3GvJedzggYL0whDs2Vea2NDmpIxtQEneOuj7LBqrO7bJfv6af2ORtD7DpxaRCOVfRiFZC02Bnw7nDXN2NG3jyScdUd0Skl-jkf6lu6rxBx4ce_pw5bgQ2Q1l61dcJkk_oD0XCmKYW6BA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
صحبت‌های لیونل‌مسی کاپیتان تیم ملی آرژانتین در پایان مسابقه امشب مقابل اتریش در جام جهانی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24094" target="_blank">📅 01:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24093">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GQqp8bvlEu3QVGdeyTcVOaQc54a4qaGehy367vh3c5w4Eq1AkbTFsLhmLWqGnn_tdBYauJguoGLJzecOKS4ojGtLuE7Ydy5lrPHkA8Sre_XFM8QmQU2diYH27KGvaqYcVl5ExAXQLrjuUrhrl1aUAfs18vTnIV5XZpGx_lkqnLLo0qsnobCyCPo5kyNYSSoFusKQDBgA1RK2vrYsLR-ZlZs41ZyxdkjHBAiKJhhRhQHVbkGI0ED3_3ZblapiwhxdoGdSEEtffPwLDvQn_OzMWUBTbAMZKd_9Zc3_YUSTpJo9HRUG4TKzVCGh6Y2xmB6RR-uOyFPQMD6m2f28QJEu5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌ دیدارهای‌ امروز؛
از مصاف یاران رونالدو مقابل ازبک‌ها تا جدال مجدد کی‌روش و انگلیس در مسابقات پایانی هفته دوم جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24093" target="_blank">📅 00:14 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24092">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hps4_55jDMGdExPzcZJ9AVfCpu2_ODlViLvxiAuCyE0mPYNmC0XvOanLoER3GdUcF4BNuc4HtiYx6eQ6PTiH0jhDDEyC-NWY7b_OvUOfVJih-xJ0wkLVWjTfT2dXmks7Ad_gKlWcofvWuTnm0LSBKidAkDuX7c84Qge7dYcbSMyIJF8JBOrE0lpEcuxIf1-nljJhaRU9_VpiMGoKU45eknABZa0v9ULKuv8dAT_OvU1k7L6wVeHmjRAHHwT_Gfn4MC7mp8cs0HvLVFNEnOTqRsuW1L07P6Q513PyKumPSvOA-HGnnF5-kJYX6-zI7CUQM3ci-Xz6UzIRwsw6INHEqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌دیدارهای‌‌‌‌دیروز؛
از درخشش ادامه‌دار مسی این‌بار برابر اتریش تابرتری‌مصری‌ها با اثرگذاری صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/24092" target="_blank">📅 00:13 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24090">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uh9HCIY_F1xdOVToNMBNW2qg-tSDu31UDZWkEVsEx0kogTY_R6JtMulSBvwI2mPI919HetKBPcmYVsu0ZxGoO_TuJfN4BtZXAcIwpy9KK0uYeGrL-dt4COcs__5hwQLRetTp9hMbtTFdl4WE75LE2DG6eKFn7WSCQf8YxA4KT2pSDmPP9AoqQ4_-WT6KneugXnYYkUKIO1icrRGjzVP5Bai42lMDXFDB32CDIPZdP3LP6MjH14O7ZNLfvc2K0RVlt4qFdkcAMoahQVD_p99XGT3fY51g91iSXLAzbGZ-nMWG9LppSqJVp0eGNiygDf-YXJ7oY02Vw6vZgPb-S_QhpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بادرخواست بختیاری‌زاده سرمربی استقلال؛
عارف آقاسی مدافع28 ساله‌آبی‌ها در تیم موندنی شد و حتی به‌مدیریت باشگاه اعلام کرده در پایان پنجره قرارداد او رو به مدت سه فصل دیگر تمدید کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24090" target="_blank">📅 00:05 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24089">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cz1jPgkV43D1oqht9NtWJJ0VWFu5z8Ayby7Ls6196-WtQdiCDLnY6fuqei5en4GtSE90_Q36QdNSUutTwsGOomTPvyEbH7DcCXHKwqi777c1yERNnI1kb4ZWQ5cvQOGW4twrj8GLunb8xeCTk1ZI2QiLWem5-anUwpYA1qrk7yr-m87vGAwSURiFj-cWLnUlhWi_HheV0VbbtyettSTs5nH9rUJ3FAqxNjWDLEgTndx1iU6JHeFz0JRrqFovZg7x2upU8jMBRosnM5WV1htxMItZ57JSnQgrZYd_dA6IXuV-j7O5ahqayYP891tswQ0TshMpdh1qagEw6wUkzQYR0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
تافرداشب مدیریت باشگاه پرسپولیس تکلیف سرمربی‌ فصل‌پیش‌رو خود رامشخص میکنه یا با اون دوشروط دراگان اسکوچیچ سرمربی‌سابق‌تیم تراکتور کنار میاد و او رو میاره یا با اوسمار ویرا ادامه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/24089" target="_blank">📅 23:51 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24087">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YBUBlErgYk2B-MnWVyR01ApqcXTHPuNuWGK-LDhjHL8GWkW834D6zwQcC-ge0Rt4RN8AiPKg7H_aUszsYQZlGErW6EioLNStU4ZUuJaLqTKWtYdxzZ1w4htz_03v2vKBjCA-7svVGq6bYuynlb5EEzaPwhyvep3J4aJG_pGLXP4wuZ5vSiGJm3Yyfg4OgQBTCgAYlH74LgmHtjCFFewVHg5nHkQiiQytWgqoTfdEpY1pP99rZpTE11taKWYTa7owY1M_vvUsqjcmwGWMK0tGfD9fMlWILYuU6mkMeh2ck9S1Zh8z648kOb_aIFeTfM_OyE0PndSWXhBpAyFTijKrzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHan47JNI2tY8jUADRY3L3RwzKmHAhAUqYGee4ThWE7PXLy6jsqr62PeAumxdqtAHbLqQNKzbvsG9d097HHpCjMiWbRg5kZw7SS97Fh8yZav11CV9JvUVA6c0WFdfvym2VqleXiNSqGWjdmWF-Chq0HykkcTp-uAf3NpDI_Be2AU2WacQ51C_zRS9NO05SUg3JPWUjk9ShSwLF8VpcFPk3GDPhwq6dFkHH8D8o3Zx1sDWNwLl6aaRafPrtHhoz2u6vUDnp26KYkbWNLRYFK3XIha6bz-YqIr378gSdNm_YMTprNwbTTmcqb8hbRisQIfJhe5cnGnSztdYXUB8KLdww.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⚽️
چهار تیم ملی که تا به امشب به مرحله بعد جام جهانی 2026 صعود‌کرده‌اند؛ آرژانتین امشب به لطف لئو مسی دومین پیروزی اش رو بدست اورد با شش امتیاز مقتدرانه به مرحله بعدی‌رقابتها صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24087" target="_blank">📅 23:13 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24085">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7535185668.mp4?token=brAL47GfD_iHHIKDa_6bJYTe3Z5z0QrSVp7n5XxyRjp-lvpo22sXIZLSB3Feh3eeQt24HhebMGpAn_WhnMn8UP3_gZFvncCpA6ETRIDVclaeYIv8Ik1r8vxLi9AX0tj4TIbxqcIHEUhyZzjLjEwh5MeSP3pksnq8kT7vL7mbkjKLF--58PHUgDZd4mG7STEX7a-lJ1GHiIrg1y1Hyxj2jrUALhzakgvBMjEX6wutsOKWSU6HxYmLvZo9ufgy7WF5bzfezOmFBWeIE4UfdJz-TCJGTzlCHddZmxDtZ1D8bnWiUnYcWIQbBCoKxhLf8cNPe_U5cWJELJ6P5_fLewPpPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7535185668.mp4?token=brAL47GfD_iHHIKDa_6bJYTe3Z5z0QrSVp7n5XxyRjp-lvpo22sXIZLSB3Feh3eeQt24HhebMGpAn_WhnMn8UP3_gZFvncCpA6ETRIDVclaeYIv8Ik1r8vxLi9AX0tj4TIbxqcIHEUhyZzjLjEwh5MeSP3pksnq8kT7vL7mbkjKLF--58PHUgDZd4mG7STEX7a-lJ1GHiIrg1y1Hyxj2jrUALhzakgvBMjEX6wutsOKWSU6HxYmLvZo9ufgy7WF5bzfezOmFBWeIE4UfdJz-TCJGTzlCHddZmxDtZ1D8bnWiUnYcWIQbBCoKxhLf8cNPe_U5cWJELJ6P5_fLewPpPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24085" target="_blank">📅 23:10 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24084">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xo6rT6GHVUuLsANzXKNXRx2puT_-JWg8ygGwFhV5_LSkqE5wSTwwN8kPDj23OPlh3IFlrImQDBMD4cglZimCbPbJfrMoniK0Y8mBK-oUB41KAuj59ktOwuruY1x-OovFZ9Akn_Ocx8UaLGKklYbvQn1BZeMSRL4C6nVKNkTWXvavNI8WKRCZIFDHHIybXhzB5-30mfia1LgkrwIvon7oZJzeGcFMeGHYQICkMJmNHbQ0QjPU_4PmTBf5F9kt0Xcn6XET7s3DBswhvUvr8zFcfyVkZu24fVV4OeonttHnjgT17HeDYc-n3IwmyDib4fJkdu71a-VDmo-S0QfW03-ocw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24084" target="_blank">📅 23:02 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24083">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4YvxmA-3QDx1KQfWlIlCz-EZvcEJxD2BZYqPogvA6DFzrWg4Qa8gbJ4LY0vfQaRnlZLGfL_YVaN7w_jAx0he4SzQ2lsvV2A65e-BIvRnJG4DZqn1aIFBsZrefD0f4PxKK0mQQEzcauiLNMDMf9u-hf_vvJnZJ-RuqcwTyZOqkVh2tVdEFvy5ZeRfhMmjvpMW-hghVA_qrehKHGCbDYDcbuCgU8T5k6QOdmaRtPtxwq0EK2w4mA4sL_IPzDj53ixL9aRCoRyH33q8nUoPOHauiL-dz5j8ZlCbxZUpDPn_jcB4oWsVyxl_tjqFPzsq2GrgzmF6yLRzeKZyPxvDLFeww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نمره درخشان لیونل‌مسی در دو بازی آرژانتین در رقابت‌های جام جهانی 2026؛ لیونل مسی 38 سالشه که اینجوری داره گرد و خاک‌میکنه. واقعا لئو و کریس جفتشون تکرار نشدنیه. هیچوقت به‌این دو نفر توهین نکنید جفتشون به شدت دوست داشتنی هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/24083" target="_blank">📅 22:57 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
