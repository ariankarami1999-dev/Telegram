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
<img src="https://cdn4.telesco.pe/file/YmqNIKjdIh--LI_sOAN07dVg4VPClKAAHfZAWQDq62PLwbYs2lU0lTtHtf1Kc9kb3BdCNLS_RpAy4BV9OFOs9iCKiZr38F-z_bHxHhmz0J_oB2tKI303t5Z0VWXbMMyeUG7lWOuJytFOzD93UxHTRIPBnLXze3tF0yOC3R4isKa8DwuCZWSX6AQ5XJS4yWxM3WOuMuKt-PeTMIl3u8XBESYQTAzve9XlSDxyf-CKCy5s6xbj46F06uz-8JZYdFbxivJQLj8L4qM66ZEvIT21u23ATjd1chxIkHi473gyKLRw_hM3BIws8TefpE4KJxXCZN_l88vSe3JQEjt9rchuYQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 105K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-10 18:42:43</div>
<hr>

<div class="tg-post" id="msg-72631">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qe73pjQiiRg9_yZDML463Yq9ogFeP_tEfXxgWtSAEE78U3oVduYURij0KVLumG0oUTtwFoVqgxqNqXuIAb4O05o_sy7MzcbL_Q6jwyZ_bpJZEhgUzX_QJu-WxapD6qeFvTMXI7VQpr_ERsThyBuzTn7mhQDPYSDNBbNVNvPU08T5oj5t_d1N1wwJuTL5SzV2CGQ-CkbBNElNKU7LwcDJnXMiXA415M_g9H1jC6QD-aXYKUcZhoO7_AHkYTEF8hmt97oqTA7_c5XAr3zO1zrlMkszmanhelLuQCNz6fCHk8tm_jQWpSKJoPCl-R01Ad0M7E_denxKwKvGMkK3lRo92Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش «اکسیوس»، با وجود اینکه هم دولت ترامپ و هم تهران علناً اعلام کرده‌اند که خواهان پایان دیپلماتیک مناقشه هستند، دیپلماسی میان ایالات متحده و ایران همچنان در بن‌بست قرار دارد.
رویکرد دو طرف نسبت به مذاکرات، تفاوت‌های بنیادینی با یکدیگر دارد.
ترامپ خواهان دستیابی به توافقی سریع، پرسر و صدا و احتمالاً فراگیر است؛ در حالی که ایران مذاکرات طولانی‌مدت و غیرمستقیم با تمرکز بر ترتیبات محدودتر را ترجیح می‌دهد.
بی‌اعتمادی عمیق نیز بر پیچیدگی‌های این روند دیپلماتیک افزوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 2.61K · <a href="https://t.me/news_hut/72631" target="_blank">📅 18:26 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72630">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">ترامپ در تروث:
اروپا به‌تازگی موافقت کرده است که حجم عظیمی از ذخایر کلان گازوئیل خود را آزاد کند.
این فرایند بلافاصله آغاز خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 6.42K · <a href="https://t.me/news_hut/72630" target="_blank">📅 17:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72629">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=KPOV29ZnzXP-4AOcTcuGVgXldj_8nrmKZdr9E4dMZl3nfMLH9YR3NiEG5oDjLjcmFAiIlZ51-hBuZKlgint3KBrFKwV1K75Cnm0BsaYnJ9oxJhE3Cbt1jvujy80zvZBKa2OmX4N8VSwNo8KuddgU7Al65_W95Au2NCJDaA_TTm-m-NyHnvZCXAFSOmOJtEoXVUDMqRD_HTyer1eiEc8IANh5ZBe70u5QgdpX9tkLsE8LQdsvgaFxicYCsDBLLilmQUm88-guvTJvSQXKj7VxhoE0eOCOwWPFLZHBeMPosMH1J6sGK4-DoZcKM4M4_NMIJnVcPW0-JoOJL188JFcA6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd453b2fe8.mp4?token=KPOV29ZnzXP-4AOcTcuGVgXldj_8nrmKZdr9E4dMZl3nfMLH9YR3NiEG5oDjLjcmFAiIlZ51-hBuZKlgint3KBrFKwV1K75Cnm0BsaYnJ9oxJhE3Cbt1jvujy80zvZBKa2OmX4N8VSwNo8KuddgU7Al65_W95Au2NCJDaA_TTm-m-NyHnvZCXAFSOmOJtEoXVUDMqRD_HTyer1eiEc8IANh5ZBe70u5QgdpX9tkLsE8LQdsvgaFxicYCsDBLLilmQUm88-guvTJvSQXKj7VxhoE0eOCOwWPFLZHBeMPosMH1J6sGK4-DoZcKM4M4_NMIJnVcPW0-JoOJL188JFcA6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر لینک کلاس مجازیشو میده به دوس پسرش و پسره هم با دارودسته رفیقاش میپرن توی کلاس و همچین صحنه ای رو رقم میزنن؛
این وسط یه کاربر با نام عباس عراقچی هم دیده میشه:))
@News_Hut</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/news_hut/72629" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72628">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72628" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 6.39K · <a href="https://t.me/news_hut/72628" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72627">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b9yhuTmQZJwNLyt4c5uUB6QfQDNLPAr-8KJVdvbhxMCrxSZvJ8VT1SYfZznjdgCmAw5Kj1gsVF38rzCdLDI2FDJWwdrFK0QB0X0afLQlzfjSvWj68UBl_MXS8cMNpI95LUpT0G7IBZrD1CkFBE-daJwA76BKaoHwzi4zt6N4WinaP6SBr1UNqsdBIFDe6iTlKlHIQKuLjd7pQi85a916KA_ta_CRoSGVTMo1hHg110NctTbe_NDlmFXFVGuCnFzv2XJHGBT3ygOpWl_zpehHNfJJuJG_LmTuOFDxYiCR-UrNUbH7iGG2nKmfv9Zu9x4frEKad0GhH8CFeH0p8uPnXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز ایتالیا
🆚
فرانسه
را در
TrexBet
پیش‌بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
ایتالیا: ۳ برد، ۱ تساوی، ۱ شکست و ۷ گل زده
فرانسه: ۳ برد، ۲ شکست و ۸ گل زده
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
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/news_hut/72627" target="_blank">📅 17:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72626">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=eGXKoK0tP_a35y0cxJXcf-oczn5SJg5rV9Er8DS0GS8aX7PHZb_Ed7AhSAM-uTxfQvWKvOv1kh2t0fyvyzY6oP-Zb1u4zguoh1fUlU-tPYFZ2rgfjw5N0SSwflu_RZT4LIThSVpuUFKaEc7s10B-XqgU8CShw99hM_mCSvIiwjzQEJOno4cGzIpdw0oxx3MOHpj2UUgfJLtPUlF33-FfKir8jhHJi27ybyck6ygatvQaYOT6DvNWBritx-jryowjG42Rqzi6Rr51X1i-NftAcY9v4HY007Ndxoj7Dhfh09soBCQaoFCdex3w_hqiKEEj2Q04hun_AC5FK2X3cIi2Gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/11e067ea31.mp4?token=eGXKoK0tP_a35y0cxJXcf-oczn5SJg5rV9Er8DS0GS8aX7PHZb_Ed7AhSAM-uTxfQvWKvOv1kh2t0fyvyzY6oP-Zb1u4zguoh1fUlU-tPYFZ2rgfjw5N0SSwflu_RZT4LIThSVpuUFKaEc7s10B-XqgU8CShw99hM_mCSvIiwjzQEJOno4cGzIpdw0oxx3MOHpj2UUgfJLtPUlF33-FfKir8jhHJi27ybyck6ygatvQaYOT6DvNWBritx-jryowjG42Rqzi6Rr51X1i-NftAcY9v4HY007Ndxoj7Dhfh09soBCQaoFCdex3w_hqiKEEj2Q04hun_AC5FK2X3cIi2Gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">احمد مجدزاده: آقای پزشکیان این اخطار آخره، اگه استعفا ندی، استعفات میدیم.
@News_Hut</div>
<div class="tg-footer">👁️ 8.28K · <a href="https://t.me/news_hut/72626" target="_blank">📅 17:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72625">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=EZJ_K1emhNORIs4qj-R6JcDi5Na2MltRQ33rdaVS7NjOeHwF4bFxxRZZoq3C5pz57DPIi1lfS9bOL5DVz0zmFhrgblb497vwNM-gQ2JRb66SjB1oVbzKfSgb2862zJ6gMGsvbxOWlm5fNk16yZzzfdAyyNm4xLFiZ7j2Lg7lvMIoOSyfhJLk2PdkUV-vn3MfCFeWuNG5eKWYqOrV_TXELXXgdyOA9wA7vUTIjQotzZFsDc8g_i7g2rXqxYy_X5uGWpBiPrgCpEMf0ovvY8-wQaKHRF1AnWiNGqW3krX30IK2dXU3xp0MU01Txa8ZmTvzVym6MF-vkwWltF3z9TfBIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad77de0b54.mp4?token=EZJ_K1emhNORIs4qj-R6JcDi5Na2MltRQ33rdaVS7NjOeHwF4bFxxRZZoq3C5pz57DPIi1lfS9bOL5DVz0zmFhrgblb497vwNM-gQ2JRb66SjB1oVbzKfSgb2862zJ6gMGsvbxOWlm5fNk16yZzzfdAyyNm4xLFiZ7j2Lg7lvMIoOSyfhJLk2PdkUV-vn3MfCFeWuNG5eKWYqOrV_TXELXXgdyOA9wA7vUTIjQotzZFsDc8g_i7g2rXqxYy_X5uGWpBiPrgCpEMf0ovvY8-wQaKHRF1AnWiNGqW3krX30IK2dXU3xp0MU01Txa8ZmTvzVym6MF-vkwWltF3z9TfBIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو وایرال شده از بانوان پولدار تهرانی که میرن توی یه سری کلاس ها شرکت میکنن پول میدن تا برن اونجا گریه کنن و تخلیه بشن.
یسری انقدر پولدارن که نمیدونن پولاشونو چیکار کنن.
@News_Hut</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/news_hut/72625" target="_blank">📅 16:30 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72624">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=HOhzxWLQhPkgvtsx_vY2aDHeIc559JmFI8zIoEmqoJtEXfFRffKtmbvJZokOrFfFfeXy71ljD-159eMhJasPJXA0hI7ptrxevBVi3cGLlvWoweCcCo5C6XCGpWP_mMQnfLMXB93Zixe0anROYz-loeLRC3mNS_9vIWzdmcwudmiVkuO_zJr3wTsWf5xB88zGTFE0qlDZW0wIvuiYjMBhvNfIlcM5M4oqz24VD8a6Y1Svk_1gToW4dxHyN98pTkbCO47_UnvjHH8bXitUaL_ws20aLG3pKGpBfkzpWadWQKhUoqWlfFBb29xs6Qu-KLELRvxG4LuX9zRieN3aPMyYhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aa3ebce38d.mp4?token=HOhzxWLQhPkgvtsx_vY2aDHeIc559JmFI8zIoEmqoJtEXfFRffKtmbvJZokOrFfFfeXy71ljD-159eMhJasPJXA0hI7ptrxevBVi3cGLlvWoweCcCo5C6XCGpWP_mMQnfLMXB93Zixe0anROYz-loeLRC3mNS_9vIWzdmcwudmiVkuO_zJr3wTsWf5xB88zGTFE0qlDZW0wIvuiYjMBhvNfIlcM5M4oqz24VD8a6Y1Svk_1gToW4dxHyN98pTkbCO47_UnvjHH8bXitUaL_ws20aLG3pKGpBfkzpWadWQKhUoqWlfFBb29xs6Qu-KLELRvxG4LuX9zRieN3aPMyYhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دانش‌آموزان دبستانی در قزوین، در مقابل مدیر و ناظم مدرسه که آنها را با شلنگ تهدید می‌کند شعار می‌دهند؛
«این آخرین نبرده، پهلوی برمی‌گرده».
@News_Hut</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/news_hut/72624" target="_blank">📅 16:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72623">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=cqjygdbvakyKhJkUI9OBBxGenh05QzI1qxY1s6PC2ebwxiLnE4E-tTMshIIUFfni9D2FkNvJFoUPYCnVohLl5EdaxEhq06Xd68c9ecvXDCFIj4iSvwyjYlkcLVai2UQgjAm-nimNC09lOq7dgOD3NfqPCZn4L53-H89d8LcOB7vfU0wfqiZV1Ntmch_6XTF9icqcM4oQLYYEhxpyUzk0Kbb1kY1T28C2OGAI4zfJICoeplM0HB4kVGN2GlJN4W1bpk6PojeVSEooTpsSbipfXAkxhlaM-hTcPdKYkMMw2noc0-yJrSqS3TIhx2g-674xTih5UsdRL9XC8RLJrl3pmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0d885465ad.mp4?token=cqjygdbvakyKhJkUI9OBBxGenh05QzI1qxY1s6PC2ebwxiLnE4E-tTMshIIUFfni9D2FkNvJFoUPYCnVohLl5EdaxEhq06Xd68c9ecvXDCFIj4iSvwyjYlkcLVai2UQgjAm-nimNC09lOq7dgOD3NfqPCZn4L53-H89d8LcOB7vfU0wfqiZV1Ntmch_6XTF9icqcM4oQLYYEhxpyUzk0Kbb1kY1T28C2OGAI4zfJICoeplM0HB4kVGN2GlJN4W1bpk6PojeVSEooTpsSbipfXAkxhlaM-hTcPdKYkMMw2noc0-yJrSqS3TIhx2g-674xTih5UsdRL9XC8RLJrl3pmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه دختر ۲۲ ساله تو تعویض روغنی با دوست پسرش در حال سکس بوده ژل روان کننده نداشتن بجاش از روغن ترمز استفاده کردن، روغن ترمز باعث خوردگی شدید پوست گوشت آلت تناسلی دوست پسرش شده و‌ بر اثر سوختگی درجه ۳ پسره فوت کرده، دختره ام بعد ۲۰ روز تو ICU بودن اومده پیش دکتر!
@News_Hut</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/news_hut/72623" target="_blank">📅 15:35 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72622">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdlogpJK4EXOZRqaiIYhFo6Uzh-6L58keEVQybdijsZXorvJenGVmIdQP-e7er8rizlsjhN4sHMpdk08GcTUT6Q7tgucFFHfEWZz4JqFxdEjc_EmaaZRw565_epyPgVWcnQZ7bbqXNbV2eexHJsJmLXjBD5O4WzgnHJvX50zPDc_2kNmFZ2ahqhZ2syPGUz5M20z1iC7eT_uIh2Grh3DENARxqMyNQ4IdJ9ddJjO_P67GuydOfHDsbn7Fwj-25Cr5zrU5ULd7I3bM10rzcXtbWo3ChXhETsD52VCRqOfvlNdhcCbP-Hs6iz_mCdLwoWabCBZiaJauHafDKOgpZc66Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کارشناس رژیم، علی قلهکی:
ماجرای «پروازِ فلای دبی» هم چاشنیِ اتفاقات آینده است!
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/72622" target="_blank">📅 14:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72621">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=a4z5aTkKywsko8Qrd-DLQLlQxxTR5Z7ms23pEeSLielJXhklAIxRCg0ZGUyFYXLug6Y6U0HBtAIjzxS1t_cPqDrZWk5g2DDjL-ii5Jf5dOzmmbmURtEZcV6sM8beH2DuDcvImPjlupSOMT657nByf9ECKFVQaGNHtgrhpaoFoyWjPhgxeotJyFukVOmvoHUYLvtQ6XIeEJEDONys21oT0E08TuyvXZ9A2xrDmp2_L9jSVMt6n6EL2IGywx-TJ4gXEHvqrmerEEaKjmUaRBOnf8OwtokR2kzlzf4MRZOJLVD8dm1EBoHwrReGQb2ZF_GGlRjavgtraZhmZ59RRd8Jbg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d8bb7d42b5.mp4?token=a4z5aTkKywsko8Qrd-DLQLlQxxTR5Z7ms23pEeSLielJXhklAIxRCg0ZGUyFYXLug6Y6U0HBtAIjzxS1t_cPqDrZWk5g2DDjL-ii5Jf5dOzmmbmURtEZcV6sM8beH2DuDcvImPjlupSOMT657nByf9ECKFVQaGNHtgrhpaoFoyWjPhgxeotJyFukVOmvoHUYLvtQ6XIeEJEDONys21oT0E08TuyvXZ9A2xrDmp2_L9jSVMt6n6EL2IGywx-TJ4gXEHvqrmerEEaKjmUaRBOnf8OwtokR2kzlzf4MRZOJLVD8dm1EBoHwrReGQb2ZF_GGlRjavgtraZhmZ59RRd8Jbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دو خانم محترم، آبروی ایران رو خریدن و باید سر تعظیم جلوشون فرود آورد!
یه توریست و بلاگر خارجی اومده بود ایران و با دوچرخه میخواست بره یه شهر دیگه.
دو تا خانم دیدن شبه و خطرناک و تاریکه، برای همین تا مقصد، دو ساعت تمام اسکورتش کردن!
حالا این بلاگر پستشو گذاشته اینستا و تمام دنیا به مردم ایران افتخار میکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/news_hut/72621" target="_blank">📅 14:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72620">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=KQkN9dl3UXKc3ZszE_5Afll0JuEMPsgE6SPxDaHtXFi99sZWvO2Dp5ul19rlnI69k_5z5j2Rv73fA1biwJMU9Hmke4SPlI5dHgElmMWzBDYFJlxpIxhxepgYRdQcXIg0nBzwCqvk00DR-Hm2hVqS4BmmmdazFzn898ZbZSAnSATBqG6mw1QHoEwMRFRzotNPSLIaogOOlYBNz0La6mXWplx6sEbymoGkDWeULfh8QnYud8qvOsF1Irn8tlhRHdjelIrhY4-Bvxq77029W0a0-2r8J1N6mNzaELuiXUbIsU3iJQy1xdwQ0JFWvZigZgo1BF_WD4GKBEb6cSWIEoUKjxMdBz43kjcISmrmPbVldpsTsXK4f6iEdUEifki--L8PWGQgrctiN58XedZhKi3ZVOxF4tFPG25kg6hKT4KCxNrHtZ6MrURHEaP7HPTTeAXr7nZrmw5fpwDLTezAkNClbYljLxaXYC7bTA89y2Lh4XVRO3xEO-HGn74mgMBi5JimT5DDtHWI5BY_TBindP0Ym0Bf6infPXnvm-e10HYYK5wc08HmdsQBnkZnhrKBb288I1SluQijAMvi1eLZhYSlRaYcAzo4SiXEXRBy8ZcFTHjzImlCF9dB4HruOJEXuynRDV5gmSOpcBqgiLWxucIlJLeb6uRdevNptGEeG344Lpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b6c59bf1bb.mp4?token=KQkN9dl3UXKc3ZszE_5Afll0JuEMPsgE6SPxDaHtXFi99sZWvO2Dp5ul19rlnI69k_5z5j2Rv73fA1biwJMU9Hmke4SPlI5dHgElmMWzBDYFJlxpIxhxepgYRdQcXIg0nBzwCqvk00DR-Hm2hVqS4BmmmdazFzn898ZbZSAnSATBqG6mw1QHoEwMRFRzotNPSLIaogOOlYBNz0La6mXWplx6sEbymoGkDWeULfh8QnYud8qvOsF1Irn8tlhRHdjelIrhY4-Bvxq77029W0a0-2r8J1N6mNzaELuiXUbIsU3iJQy1xdwQ0JFWvZigZgo1BF_WD4GKBEb6cSWIEoUKjxMdBz43kjcISmrmPbVldpsTsXK4f6iEdUEifki--L8PWGQgrctiN58XedZhKi3ZVOxF4tFPG25kg6hKT4KCxNrHtZ6MrURHEaP7HPTTeAXr7nZrmw5fpwDLTezAkNClbYljLxaXYC7bTA89y2Lh4XVRO3xEO-HGn74mgMBi5JimT5DDtHWI5BY_TBindP0Ym0Bf6infPXnvm-e10HYYK5wc08HmdsQBnkZnhrKBb288I1SluQijAMvi1eLZhYSlRaYcAzo4SiXEXRBy8ZcFTHjzImlCF9dB4HruOJEXuynRDV5gmSOpcBqgiLWxucIlJLeb6uRdevNptGEeG344Lpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) یک یگان دریایی آبی‌ـخاکی آمریکاست که هسته اصلی آن ناو تهاجمی آبی‌ـخاکی USS Makin Island (LHD-8) است و در مأموریت فعلی، سیزدهمین واحد اعزامی تفنگداران دریایی (13th MEU) را نیز با خود حمل می‌کند.
این گروه از سه شناور تشکیل می‌شود:
USS Makin Island (LHD-8) — ناو تهاجمی آبی‌ـخاکی از کلاس Wasp
USS Anchorage (LPD-23) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
USS John P. Murtha (LPD-26) — کشتی انتقال و پهلوگیری آبی‌ـخاکی
چیست(13th MEU)؟
13th Marine Expeditionary Unit
یا سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا یک نیروی اعزامی تفنگداران دریایی است که برای عملیات و واکنش سریع در مأموریت‌های خارج از خاک آمریکا سازمان‌دهی شده است.
در کنار ناوهای ARG فعالیت می‌کند.
ترکیبی از نیروهای رزمی، پشتیبانی و عناصر هوایی
تجهیزات و هواگردهای همراه:
همراه با 13th MEU، هواگردهایی از جمله F-35B Lightning II، MV-22B Osprey و AH-1Z Viper را در اختیار دارد. F-35Bها متعلق به اسکادران VMFA-211 هستند و از ناو USS Makin Island عملیات می‌کنند.
این گروه تا پایان نوامبر به منطقه می‌رسد.
@News_Hut</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/news_hut/72620" target="_blank">📅 13:55 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72619">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=Os-_FVNq0yB6pDonkisE_Una4Rlm-knp3qawt1Z8vQFCYdGvLq_Y2q1_kVQBF3kXyyOSU-fzprIXkO0pqOXMsi03hYF1cCcKKk7fQdJr5rimVfVPS8qm6muKC4xoMt3tL8ARRNK2O9gtGYvdTWA8I3XTJDl6xsgUtR_er-CS56pRZpAc0IkRjoOedcgN0LFc94q5q7b_mLKFDipU0ZOgI-RmEo-hdZQCyEFL_iPowSHylhQ_vDQEIdCaC80DT_5deGDicbvA6wek5VurnN9J29grWKlEy5i_t4X0otyFbE3q4DxrrOCMfCCi-pFnbY9xqjQc6c04X8aN1ap3tNBVQTL1pTUir_9h19bovL3D-xnP979eShyZqJtAK6mvPb08fS4sf_tkvsFOWZs1ppvsIE7oq_sBmfRCBVPvGO1vQfC6T1BDYZaaDgLN7d2tU2GVxMBGRqxnOwDdIHlCuGhJMlGJF_cL-a4K29BvcwmFPP7OaVjsXMvQMatam3irfCcIOdAtk5QFp8DhR_jMgmmJRnErd6ezFk_rM2IeBCzPptWedSwrN1lWiCRHLxfUPF3QJq6e91-qBTJnkMNRayvXt-PpDlevWn6zJfztxddGv53u8Nl6g8WHy1JOEiBXikHE2Pkg_penssaN_BnNkv5zrqoSsX_kaQpwRrdBLDlm5ZE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2a1a8f77f.mp4?token=Os-_FVNq0yB6pDonkisE_Una4Rlm-knp3qawt1Z8vQFCYdGvLq_Y2q1_kVQBF3kXyyOSU-fzprIXkO0pqOXMsi03hYF1cCcKKk7fQdJr5rimVfVPS8qm6muKC4xoMt3tL8ARRNK2O9gtGYvdTWA8I3XTJDl6xsgUtR_er-CS56pRZpAc0IkRjoOedcgN0LFc94q5q7b_mLKFDipU0ZOgI-RmEo-hdZQCyEFL_iPowSHylhQ_vDQEIdCaC80DT_5deGDicbvA6wek5VurnN9J29grWKlEy5i_t4X0otyFbE3q4DxrrOCMfCCi-pFnbY9xqjQc6c04X8aN1ap3tNBVQTL1pTUir_9h19bovL3D-xnP979eShyZqJtAK6mvPb08fS4sf_tkvsFOWZs1ppvsIE7oq_sBmfRCBVPvGO1vQfC6T1BDYZaaDgLN7d2tU2GVxMBGRqxnOwDdIHlCuGhJMlGJF_cL-a4K29BvcwmFPP7OaVjsXMvQMatam3irfCcIOdAtk5QFp8DhR_jMgmmJRnErd6ezFk_rM2IeBCzPptWedSwrN1lWiCRHLxfUPF3QJq6e91-qBTJnkMNRayvXt-PpDlevWn6zJfztxddGv53u8Nl6g8WHy1JOEiBXikHE2Pkg_penssaN_BnNkv5zrqoSsX_kaQpwRrdBLDlm5ZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره عملیات «چکش نیمه‌شب» (Midnight Hammer):
آن‌ها تمام بمب‌ها را فرو ریختند؛ بمب‌ها مستقیماً از طریق مجراهای هوایی به داخل این... خب، کارخانه‌های مواد مخدر فرستاده شدند؛ واقعاً کارشان همین بود.
هم بحث هسته‌ای در میان بود و هم مواد مخدر.
آن‌ها مشغول تولید مواد مخدر بودند.
به این کارخانه‌های مواد مخدر و تأسیسات هسته‌ای، ضربات بسیار سنگینی وارد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/72619" target="_blank">📅 12:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72618">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/MN_LDcklptL00HFWquWo4G1I3hSeebr1PXKfrZC6oUnwJWM6t4KQJFhRsqxx8Afq50QploWQ8HEuGc-T6EJymuc-9kXwngFW9jnj7Aeu-hUNAXPvPeb2mrx2f2_MBnu1zQ0WjFERig9wIj2Xue5-TMAD2D_n2CzEn4ZbGvxakm6LUnHTP-0Ut3z0J1WDJU9st0Y6UjetBBh7LRl7taLh8ll1k8sKCwcNmMeEm91FKDVy-X3OZpxnX-MXNd7Wvr93wlaZMPr61thV2QdDBjHuAyD3R5s7EoVXxPHvDYD2IYKLEczPuDMNpGAVU4H45v6hT-wBPKI6j2h-aIUyKuYIxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوووووری
؛ آکسیوس به نقل از یک مقام آمریکایی گزارش داد که گروه آماده آبی‌ـخاکی «مکین آیلند» (Makin Island ARG) و سیزدهمین واحد اعزامی تفنگداران دریایی آمریکا (13th MEU)، پایگاه نیروی دریایی سن‌دیگو در کالیفرنیا را برای استقرار در غرب آسیا ترک کرده‌اند.
انتظار می‌رود این نیروها تا پایان نوامبر به منطقه برسند.
این گروه شامل سه ناو است:
ناو تهاجمی آبی‌_خاکیUSS Makin Islandاز کلاسWasp
ناو ترابری آبی‌_خاکیUSS Anchorageاز کلاسSan Antonio
ناو ترابری آبی‌_خاکیUSS John P. Murtha از کلاسSan Antonio
این گروه همچنین ۱۰ فروند جنگنده F-35B Lightning II و حدود ۲۲۰۰ تفنگدار دریایی آمریکا را به همراه خواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/72618" target="_blank">📅 11:53 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72617">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72617" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/news_hut/72617" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72616">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGlWCVlOFtjVOdin9xYtYEXxkbaRgDAGqadm20otpI7D6iJgTBueivoQMUdftWXpyB_Kau5vt7WVvp5bIiz3I2gVVf3YUAaYIy7x8A-ysCaOpUj7-KKfkbtWWdnmkMV09eXOQJiqmeCbcvGy7ne40vL51RCuZHLSe5VpEAW5HBA_eaT_kF5-yPMzOWxEnxxS5TCnXxgJO9lAtgl-jrsWGAT_O4g5EDX0kX91V6u6DIVUr754JRif0XgAEqqGragiT2y-iyNJdKLP-E8GnSxCKaQs6qoXG3XGpxAE6WDhjSdn2LVz5v4WKmv3YKJigM1fx9d1LRtRGBB-E2xyc15fnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین المللی
TrexBet
ترکیه
🆚
بلژیک
ایتالیا
🆚
فرانسه
سوئد
🆚
بوسنی
نروژ
🆚
ولز
ونزوئلا
🆚
کره‌ی جنوبی
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
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/72616" target="_blank">📅 11:52 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72615">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1127789805.mp4?token=mIGXUNoaXFh7gPkIYh-5jUK8qfmFQ0ihcy3hIG8m37hqq3e_hcNdv5XnBT0ME_Fw04n7JO_L1Z7LitVwUr1SMyYLRoeTWowYRmkXtIp7joR7CdEG52vU0gBtBS9W-uxuiwgM6UmJFYx-KqlKXbWjwloWh77L1Of0r-qM5x8X-8m2AU8klh8LBgSUzGnJ7u1CM32qepAhjtFRbRh2ugSuMEtR_hnuCGrFn5d9JeU8c_YUekVIpx3EviAHQiNzjX81i_Zmfkh6-AQiqyOMcfa5XLWexH9fpwlT_2SwamCyHQ993MMOa1cu3zyJdXKo5DfemPbAH6cS5hZ7YuOKcMmNJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1127789805.mp4?token=mIGXUNoaXFh7gPkIYh-5jUK8qfmFQ0ihcy3hIG8m37hqq3e_hcNdv5XnBT0ME_Fw04n7JO_L1Z7LitVwUr1SMyYLRoeTWowYRmkXtIp7joR7CdEG52vU0gBtBS9W-uxuiwgM6UmJFYx-KqlKXbWjwloWh77L1Of0r-qM5x8X-8m2AU8klh8LBgSUzGnJ7u1CM32qepAhjtFRbRh2ugSuMEtR_hnuCGrFn5d9JeU8c_YUekVIpx3EviAHQiNzjX81i_Zmfkh6-AQiqyOMcfa5XLWexH9fpwlT_2SwamCyHQ993MMOa1cu3zyJdXKo5DfemPbAH6cS5hZ7YuOKcMmNJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی هند یه میمون یهویی وارد مشروب فروشی شده و انقدر مشروب خورده که به این روز افتاده :
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72615" target="_blank">📅 11:00 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72614">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oX5kfykdfByqslIolmRaT_1MPyiymJ84yN7QqeIgo3JFdmjjhkxnHnuDqKgZxsqfL7cYrmWqreWKAEE_x9RrjZiYBNT7cctG37dQF7W3K9lvYRq9okB9ysqsZn0IUQ8miHHmReppsxY-MAS6BKoH-4YnslzCll137RNioCfO3RwsCrSwR_CFChAdU5zlXEfOuMKYOrPY_s-SkUCiBx63QduhoHs50h-pvVOg6Ez_5yBrEw14ILtKVohf6Hg_HHUqxR5454fOMa_xcZzlwjiUSNKkx8-xI1cqsrRnvk6xOeuGX-vimBZBUoYFCOLe9E4bhyDl0-ILg5nIiJ_Wed55ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسنت، وزیر خزانه‌داری آمریکا:
ایران در ماه سپتامبر حتی یک بشکه نفت خام هم روی نفتکش‌ها بارگیری نکرده.
دولت ترامپ در حال قطع کردن مهم‌ترین منبع درآمد حکومت ایرانه.
عملیات «طرد اقتصادی» در حال قطع کردن شریان‌های اقتصادی‌ایه که به تهران اجازه داده برنامه‌های تروریستی خودش رو تأمین مالی کنه.
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72614" target="_blank">📅 10:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72613">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c00080542.mp4?token=HLvRpidriE3cC9jHtFyTn1_1xJW2A2BrSj_BEQwHAZv6IDUUOkvDw_8crbzCxLzQa65diOYbkIEHTQRq4nJDxpv8I332eDyaHOjyDuLtI4WtsvdTU0ZOyB-a26suE2Pma9HTxbmrIaOsAMauYPzDvo_4_pjRomAGHjYVC_5WfhUezil6NbGPO_lG3SE1BuD3SKYEDg0N-_EB1nadrjhB0QGknyDvSNnOoWBilitAsAr4wiOOqqgy_K7PXtM429m2q28vjgatyFqojLBU7PALZNYgIx4_9NOJGIVztSrtM6WJ08sYB8iIQbm7NjmU2nsOnzEDaHEyOSviIo7MU0O3FQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c00080542.mp4?token=HLvRpidriE3cC9jHtFyTn1_1xJW2A2BrSj_BEQwHAZv6IDUUOkvDw_8crbzCxLzQa65diOYbkIEHTQRq4nJDxpv8I332eDyaHOjyDuLtI4WtsvdTU0ZOyB-a26suE2Pma9HTxbmrIaOsAMauYPzDvo_4_pjRomAGHjYVC_5WfhUezil6NbGPO_lG3SE1BuD3SKYEDg0N-_EB1nadrjhB0QGknyDvSNnOoWBilitAsAr4wiOOqqgy_K7PXtM429m2q28vjgatyFqojLBU7PALZNYgIx4_9NOJGIVztSrtM6WJ08sYB8iIQbm7NjmU2nsOnzEDaHEyOSviIo7MU0O3FQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک اخوند در تجمعات شبانه: دو شب پیش رهبری نیم ساعت در تجمع شبانه حضور داشتند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/72613" target="_blank">📅 09:58 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72611">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/a16936d012.mp4?token=MbIEgO4Lp-ke3HGcY8cOM6tuXZfwjhYjSizN9B_CUcl11hRN2uDAf1NUqPmNOPt9Yq4-c-ndQSwm1zAALokheQwFfxj0F4lvtMlmaYu9Fm4D2R85RfkX7872TZLZbo8GmEZB4QAbmOXI9nyXE0vkc6uaMuPKNI6S9-np_BhsWJK94_1kFBmtH2ThLMJrrEneLSl4x3y0Ws3oWSloDdkqWAE6hFxMfeIq2-NXTUVFmEkdY1zGDObBWXx90LirjxwA2-x12RwtsDq3SWkAmVBSRraoYq2McTn-z15EqkzyR8tdps4NfWr7dsYhbYa32r8DSLCOwWUeL8sVJgvkZ8WcZA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/a16936d012.mp4?token=MbIEgO4Lp-ke3HGcY8cOM6tuXZfwjhYjSizN9B_CUcl11hRN2uDAf1NUqPmNOPt9Yq4-c-ndQSwm1zAALokheQwFfxj0F4lvtMlmaYu9Fm4D2R85RfkX7872TZLZbo8GmEZB4QAbmOXI9nyXE0vkc6uaMuPKNI6S9-np_BhsWJK94_1kFBmtH2ThLMJrrEneLSl4x3y0Ws3oWSloDdkqWAE6hFxMfeIq2-NXTUVFmEkdY1zGDObBWXx90LirjxwA2-x12RwtsDq3SWkAmVBSRraoYq2McTn-z15EqkzyR8tdps4NfWr7dsYhbYa32r8DSLCOwWUeL8sVJgvkZ8WcZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به تازگی توی مملکت یه سری مهمونی میگیرن که توش با تم و استایل دهه هشتادی شرکت میکنن :))
@News_Hut</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/72611" target="_blank">📅 09:31 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72610">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hPn71wKBS12huEJgnsE04nmKbXGjJ5Ms78YZQepC97SD7l1R2y0enp_E4lE-0edcujGVlg_AgSXJobh24rqFvkjE0uoz5jDT7M3mPOl3pKYXE8sQUPpG91TgpjkHzo5WQPL8Xbvfkdxmk3UOpzkDZuNOrD4O5zImKxID4mItkgiax69nCQdoJGyMV0NVWqD-rp8INIFOWt8pZXPXwR9ySZGVGif8CWynclVeZg9TI59zU7qtV1vQHo_npA-e_JIHEwoBhI0oJOwuNGRJFwC3XkWhgQA2UuFZ-CfTI802-sd-lsz06QfrX_SZGCWx-JegmP5SxOdExZU0JFxATcUMjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خزانه‌داری ایالات متحده با اعمال تحریم‌های جدید علیه بخش‌های خودروسازی، ریلی، تولیدی و فولاد ایران، دامنه «عملیات طرد اقتصادی» (Operation Economic Outcast) را گسترش داد؛ بخش‌هایی که به گفته واشنگتن، با کاهش درآمدهای نفتی ایران در پی محاصره دریایی آمریکا، اهمیت فزاینده‌ای یافته‌اند.
وزارت خزانه‌داری مجوزهای جدیدی برای اعمال تحریم‌های بخشی علیه صنایع خودروسازی و ریلی ایران صادر کرد و شرکت‌های بزرگ خودروسازی از جمله «ایران‌خودرو»، «سایپا»، «ایران‌خودرو دیزل»، «پارس‌خودرو»، «زامیاد» و دو شرکت «نیرو موتور» را در فهرست تحریم‌ها قرار داد.
همچنین تأمین‌کنندگان خارجی در اندونزی، امارات متحده عربی، ترکیه و هنگ‌کنگ به اتهام تأمین قطعات خودرو برای تولیدکنندگان ایرانی و کمک به حفظ شبکه‌های تدارکاتی بین‌المللی آن‌ها، تحریم شدند.
@News_Hut</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/news_hut/72610" target="_blank">📅 09:03 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72609">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72609" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72609" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72608">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nd5jrcx0xapkMyvM7echGpNQvEtqnKQLsEyS8pp_yaKgZyvUJ4yZdRGjusNHA6BrqW-eWf0WB8Pj7XWW478qZaU3qWINDng3dJFYlK95A8fhdEmdq_r8V6gywVewry_7oH2yIWQ5DHdl73jBdjEecWE4Fjj3nsY603yAAjWD8VibNYa9U9Svfqdm4wbry6BFJYq3cuh2fyELwQrpe-E_VPLmV_eSALwwGml8dKSgSbTzfL47W_KpqnMbscRZzt6KhGaoEG9C1Wlv8SRhf0JE4rgo8EjBimWE26RF-e0a_6GlOtzEtD3hsi-1YCgR7zIcF64cO7F974iojEKBqZ4eFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72608" target="_blank">📅 01:59 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72607">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5821a90294.mp4?token=IOt4K9mfj4BOvo3ZAQK45E8U_rw3REsCfLF9kz6n7sjLmE26OAoDm09VvqjRHSgu_-DlOLQlYLdlDuijyXK3z8uEjdYrZF1WA_VvXAluEAprSUM6WNSPHaCkpwsgVVl6wwWjDu0OLq4UyCUddmRR1SNFdDoHdKsZRq9z00CRUgLhsEZsKdtTfJpNeCFgosA9qp5BlWAXSdsq1n2y5JJHS5bZWPpacA-SptoAcSkRGdmsTlDb53V5DNNm9H3rOVLe5diOBwmh1QavHzWFGvACU6Wkvs8iD8X5yub5UY1s4WQ0DBiLJq00VUbmb39siBuKf73gQm7b6oncLt80EsfW8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5821a90294.mp4?token=IOt4K9mfj4BOvo3ZAQK45E8U_rw3REsCfLF9kz6n7sjLmE26OAoDm09VvqjRHSgu_-DlOLQlYLdlDuijyXK3z8uEjdYrZF1WA_VvXAluEAprSUM6WNSPHaCkpwsgVVl6wwWjDu0OLq4UyCUddmRR1SNFdDoHdKsZRq9z00CRUgLhsEZsKdtTfJpNeCFgosA9qp5BlWAXSdsq1n2y5JJHS5bZWPpacA-SptoAcSkRGdmsTlDb53V5DNNm9H3rOVLe5diOBwmh1QavHzWFGvACU6Wkvs8iD8X5yub5UY1s4WQ0DBiLJq00VUbmb39siBuKf73gQm7b6oncLt80EsfW8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ترامپ درباره ایران:
یا کار بسیار درست و هوشمندانه‌ای انجام می‌دهند، یا عمرشان چندان طولانی نخواهد بود.
وقتی با آن‌ها توافق می‌کنید، بسیار محتمل است که به آن پایبند نمانند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72607" target="_blank">📅 01:47 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72606">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=ptN_nNAEmrLw5CLN6wgaHSfv6fZdIouN-Ow_gzZppDaP03gmdkCYurDFO_M5n1JY4ZDdHtX40V4z4VBvnmG1ByoGBhd941EuRVKq0hkTE6Ev5s0ZI593X_8py7wsTnD7Ge7VfTYqv_9GbHxf89b_3lH_iRJ_rdmZNtfMK_SjU81RzDuIDHVp8Z8GDK8Az-1hcS5BEjmhSPxh_epvE57Xc-txktEoIDkQZNXGebmpPCPluuvJJp1fqxJBUs-AvCDA-aE61F9OT5Ino2PcIAI6WKKIWqQgHBe31RTPe4xyIuH4rvvmXVNoq1AtunmNh7suOTEz6LDTzc_VqwGvGGtF7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd837a9d25.mp4?token=ptN_nNAEmrLw5CLN6wgaHSfv6fZdIouN-Ow_gzZppDaP03gmdkCYurDFO_M5n1JY4ZDdHtX40V4z4VBvnmG1ByoGBhd941EuRVKq0hkTE6Ev5s0ZI593X_8py7wsTnD7Ge7VfTYqv_9GbHxf89b_3lH_iRJ_rdmZNtfMK_SjU81RzDuIDHVp8Z8GDK8Az-1hcS5BEjmhSPxh_epvE57Xc-txktEoIDkQZNXGebmpPCPluuvJJp1fqxJBUs-AvCDA-aE61F9OT5Ino2PcIAI6WKKIWqQgHBe31RTPe4xyIuH4rvvmXVNoq1AtunmNh7suOTEz6LDTzc_VqwGvGGtF7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
ایران در فوریه ۲۰۲۶، تنها سه تا چهار هفته با دستیابی به سلاح هسته‌ای فاصله داشت؛ شاید هم زودتر.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72606" target="_blank">📅 01:43 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72605">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69424629e7.mp4?token=mNb5tTEMgfc1wlvUA3m6L-7Q5xjQLgXtHITa-ZjgwJT6fKzrH2EICERa-K2qriYpt51rXKQZ0k2qqiwGrldlakNaTiYT6dnClSkad3MuXfhUGGg2VkA4f7mHp1C6wVDIG-bQSAYLEX7a-6WFNl1Imm41rxm8s6Y4Xu3xPeZ60KMqFzjAZW-ETI-pq-f91E7Yt8tpD-uMl6TDMpyI6LQrEXvuUCWeNurWpP45kAchAxo7m5GUuJ3OmUqFZ3vR_8YDP9JEPFfR4lRte25VJkUZyzgBDbZ7YPtD3nI3b3Khd-nRtQMcjoXfVR0vXwuk4TN_9E2NPJ1fvndOLcqH7D8HrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69424629e7.mp4?token=mNb5tTEMgfc1wlvUA3m6L-7Q5xjQLgXtHITa-ZjgwJT6fKzrH2EICERa-K2qriYpt51rXKQZ0k2qqiwGrldlakNaTiYT6dnClSkad3MuXfhUGGg2VkA4f7mHp1C6wVDIG-bQSAYLEX7a-6WFNl1Imm41rxm8s6Y4Xu3xPeZ60KMqFzjAZW-ETI-pq-f91E7Yt8tpD-uMl6TDMpyI6LQrEXvuUCWeNurWpP45kAchAxo7m5GUuJ3OmUqFZ3vR_8YDP9JEPFfR4lRte25VJkUZyzgBDbZ7YPtD3nI3b3Khd-nRtQMcjoXfVR0vXwuk4TN_9E2NPJ1fvndOLcqH7D8HrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ونزوئلا:
ونزوئلا تماماً تجهیزات روسی و چینی داشت. ما همه آن مزخرفات را از کار انداختیم؛ آن‌ها کار نمی‌کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72605" target="_blank">📅 01:42 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72604">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=An8TkrIEFzaOSQECfx075JwFJeQIJ-ZTzPPInQeytcuVbMIhsdV6N8YE-2raZdgtLVR3UL_-etY-MQTFI9rz8TEkU80UbsWagIOeeTK-OSp1khvLGJpNrYOM_nczBOkO7Nfh8b4iM2XagbUkXfqNzMpqNwcZuYgJ3h8qmBgMYpt1RhqZMiGqihBFujmJ0DxvRgOpkQeCBqdPY-4a5yevXjhAc3dvnegwmFxvF03M0ZsqKvcjMFWlseACSxDJL488VL3i3-XIschz5sYUSYj-2hCkc7duyJVM1LnQODLdxMFWVXuq9XQFoJJxjwyypppAxfsCRUz9TPhw7t5DZGYZHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2bdd7600.mp4?token=An8TkrIEFzaOSQECfx075JwFJeQIJ-ZTzPPInQeytcuVbMIhsdV6N8YE-2raZdgtLVR3UL_-etY-MQTFI9rz8TEkU80UbsWagIOeeTK-OSp1khvLGJpNrYOM_nczBOkO7Nfh8b4iM2XagbUkXfqNzMpqNwcZuYgJ3h8qmBgMYpt1RhqZMiGqihBFujmJ0DxvRgOpkQeCBqdPY-4a5yevXjhAc3dvnegwmFxvF03M0ZsqKvcjMFWlseACSxDJL488VL3i3-XIschz5sYUSYj-2hCkc7duyJVM1LnQODLdxMFWVXuq9XQFoJJxjwyypppAxfsCRUz9TPhw7t5DZGYZHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رؤسای جمهور [پیشین] ایران دیگر با ما نیستند، اما سعی داریم با فرد فعلی خوش‌رفتار باشیم.
بالاخره باید با کسی کنار بیاییم، مگر نه
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72604" target="_blank">📅 01:39 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72603">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ترامپ درباره ایران: ایران آماده تسلیم شدن است. ما همین حالا خیلی راحت پیروز خواهیم شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72603" target="_blank">📅 01:37 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72601">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9371c09764.mp4?token=vrbjtN5HWRpyQJZwRjiYCPnOPmo5mD7kwvo6nGPUGsTjJQhGd8_EUxfStwUeaaC4g3YU3nrq_mlM7OAQ7G0JPmDJDc4kgp3_s_oQTC68l2LQJ-yqoEuUBnipxMONzDUP-d-oYp-kZUgpZQx64z13LUpaWttA_qtzlD6HVAf-riSa8coBwUhvIfb8SVzSIox_jDZD-47QhGcwyCEyTYWFBZl2V2qViNIvj8U4DL4zuBOpp31byMYmPKsQ3qgICnwNRdI9mHDfvNjxp1kf0U9QQJXdt6x2q2wBCqcxuug3mL6Xm31N0WmXOK_MEgLrGVCLfqMwaWbMPNspxKGSOxSb3g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9371c09764.mp4?token=vrbjtN5HWRpyQJZwRjiYCPnOPmo5mD7kwvo6nGPUGsTjJQhGd8_EUxfStwUeaaC4g3YU3nrq_mlM7OAQ7G0JPmDJDc4kgp3_s_oQTC68l2LQJ-yqoEuUBnipxMONzDUP-d-oYp-kZUgpZQx64z13LUpaWttA_qtzlD6HVAf-riSa8coBwUhvIfb8SVzSIox_jDZD-47QhGcwyCEyTYWFBZl2V2qViNIvj8U4DL4zuBOpp31byMYmPKsQ3qgICnwNRdI9mHDfvNjxp1kf0U9QQJXdt6x2q2wBCqcxuug3mL6Xm31N0WmXOK_MEgLrGVCLfqMwaWbMPNspxKGSOxSb3g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛مامور های عربستان یه شخصی رو که قصد انجام عملیات انتحاری داشت در مسجدالحرام (خانه خدا)دستگیر کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72601" target="_blank">📅 00:51 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72600">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=CX_9PaLKB___ODfROQnB3_iUFhMSvkPqfVnn27I_pX6laFTLsf6kfLYeIzuLe_6QLiX0XEt5Xy3uLTox3Z8MOKkWcs5uDsn5RdeZSRDzWW-ekLg2jbwXdGQFi9D5UvO-qzXQSFzfioWI0BXo2lHLiR4IP4qu-9n8nzDNzaYsLKMDikbot5HKN7ho1s49yU66cgo9YHMqqtdahmL63lJknI3XwwjGAxAg87h86FpXTUSOGnzjExUuRSEGV4pK79eSbzSjEkdqDgkJQyc1rJMjXZXWFr4WIfvZgBU5EzBoGFFguLRw8mp7ThcChlnWM7kLZbfjc3gb0h8yJAT4dcDy1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c38d02b25b.mp4?token=CX_9PaLKB___ODfROQnB3_iUFhMSvkPqfVnn27I_pX6laFTLsf6kfLYeIzuLe_6QLiX0XEt5Xy3uLTox3Z8MOKkWcs5uDsn5RdeZSRDzWW-ekLg2jbwXdGQFi9D5UvO-qzXQSFzfioWI0BXo2lHLiR4IP4qu-9n8nzDNzaYsLKMDikbot5HKN7ho1s49yU66cgo9YHMqqtdahmL63lJknI3XwwjGAxAg87h86FpXTUSOGnzjExUuRSEGV4pK79eSbzSjEkdqDgkJQyc1rJMjXZXWFr4WIfvZgBU5EzBoGFFguLRw8mp7ThcChlnWM7kLZbfjc3gb0h8yJAT4dcDy1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سؤال: آیا ایران در حادثه «آر.ای.اف فیرفورد» (RAF Fairford) نقش داشت؟
ترامپ: بله، ظاهراً همین‌طور است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72600" target="_blank">📅 00:15 · 10 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72599">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gb3-XUfYTp9OZsd1QhFZdMnN8nwM6Y1T_MVDZmXuRW-PWoZ1xWS6SMADX3rCQFdEhAft9XQg72ivJ8Wc0lgMmi2QtN70icWE-ZY6LWehv1Ao4p8ZIHQyxRCvM-mTpgs60sElSZ3A4n_FleU-wzYc7LcJyurmU-UH51tjZj1vg4XyryU2HLpFPY4V-z2dKiCXYl9bL1uOYJ3pELkn4Pb0cCITShqqOjIiDPbehDksiIkUBPvK0Lt2rO8kjfi0Uc6dRpcA7exp0a390vGZTpPF15DbZx5ayocrStSB-L3zhYtMlTYwtZobtTOxHZXF3m0KMmwXy7cjd3wmpHbyO1sw-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش وال استریت ژورنال، ده‌ها نفتکش ایرانی و مرتبط با ایران در آب‌های آسیا سرگردان مانده‌اند، زیرا ایالات متحده فشار بر کشورها و شرکت‌هایی را که به کشتی‌های درگیر در تجارت نفت تحریم‌شده ایران خدمات می‌دهند، تشدید کرده است.
حدود ۲۰ نفتکش خالی ایرانی تنها در سریلانکا سرگردان هستند و برخی از خدمه با کمبود غذا، سوخت و آب شیرین مواجه هستند.
از زمان اعمال مجدد محاصره تنگه هرمز توسط ایالات متحده در ماه ژوئیه، کشتی‌های دیگری در نزدیکی مالزی، هند و چین سرگردان شده‌اند و از بازگشت بسیاری از کشتی‌ها به ایران جلوگیری کرده‌اند.
واشنگتن همچنین به سریلانکا فشار آورده است تا از تأمین کشتی‌های تحریم‌شده توسط شرکت‌های محلی جلوگیری کند و به آنها در مورد تحریم‌های ثانویه هشدار داده است. فشارهای مشابه و افزایش اقدامات تنبیهی در سایر نقاط آسیا، بنادر و شرکت‌های دریایی را به طور فزاینده‌ای نسبت به خدمات‌رسانی به کشتی‌های ایرانی بی‌میل کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/72599" target="_blank">📅 23:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72598">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=knfB_Xm0s8IiG0LbOM2zDxX8Mg3RdJ2J9Vs1-Nyu48DUqvA3RDB9-TjSPJmkOtYlRbvlFujiVPHFVagvwfxQQ9XXJ2jN7vPxp1M2URupmCH3zWrLGelOpJvbf3W2_hWBeAunT3V3JHd8OPK-YBaGVG6cu6v3GH8ONJclxSvXIofO7OFDs8eYvC7-PNA_IKK1WJY0in1zPkqk1-2jPugOXxdo1RrnVkKm-lAmk_3AJ5DpdU55SFcmYi7z6czrY8052tZtrL3zvPIcALpd_vo0FcAOqjEzi7x7NORmySwA7PwfVy4U0kGkt_6IskPZQynTubLomXvzrpwypYfVFfX2Yg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bce71f4cf.mp4?token=knfB_Xm0s8IiG0LbOM2zDxX8Mg3RdJ2J9Vs1-Nyu48DUqvA3RDB9-TjSPJmkOtYlRbvlFujiVPHFVagvwfxQQ9XXJ2jN7vPxp1M2URupmCH3zWrLGelOpJvbf3W2_hWBeAunT3V3JHd8OPK-YBaGVG6cu6v3GH8ONJclxSvXIofO7OFDs8eYvC7-PNA_IKK1WJY0in1zPkqk1-2jPugOXxdo1RrnVkKm-lAmk_3AJ5DpdU55SFcmYi7z6czrY8052tZtrL3zvPIcALpd_vo0FcAOqjEzi7x7NORmySwA7PwfVy4U0kGkt_6IskPZQynTubLomXvzrpwypYfVFfX2Yg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با پیشرفت هوش‌مصنوعی، حضور و غیاب تو مدارس هم شکلش عوض شده و به این صورت با تشخیص چهره انجام میشه :
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72598" target="_blank">📅 23:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72597">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fsiuOKKMH5ET3rCPDV1PGSetHND1imlApRdoIIJed4iD0Jn_dY6cID_th-gheA3re1Kutmw_a_OhBUoejzrU-HXq3u88LJ_RIplSJzXPraah0YuCmvCjEkQqSIBoLyvTgt1eL-Qh7s_jIIT_-FNv2PP_XDvyWaxslaHiQC5--GUK187dTKFveU1KWx0nc7dBGG4QCjEEmmDPnreoWKWImFcTo-TJ80Tib3X8L-DmeVxRwXcMtn_oyx4VOO1-qxR9LEV-GNJsSfvmSWhsbISTyhayb0LfbqvYCAqfyuDviOjqElDcjkzkAZf2q1Nv6_QP_CNMYxHQFY5IbUuLtayNbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛پلیس بریتانیا اعلام کرد که یک تبعه ۲۷ ساله با تابعیت دوگانه بریتانیایی-ایرانی را در مرکز لندن به ظن «تدارک اقدامات تروریستی» بازداشت کرده است؛ اقدامی که با حادثه روز یکشنبه در نزدیکی یک پایگاه هوایی در انگلستان (که مورد استفاده ارتش ایالات متحده است) مرتبط دانسته می‌شود.
دو ملک در این منطقه مورد بازرسی قرار گرفتند.
مأموران مبارزه با تروریسم همچنین از مرد دیگری که تبعه ۲۶ ساله بریتانیاست، بازجویی کردند.
ویکی ایوانز، هماهنگ‌کننده ارشد ملی در بخش پلیس مبارزه با تروریسم، تحقیقات مربوط به پرونده «گلاسترشر» را «بسیار پیچیده» توصیف کرد و اظهار داشت که تیم‌های تخصصی در حال پیگیری «چندین خط تحقیقاتی» هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/72597" target="_blank">📅 22:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72595">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kfFxQ-YeTYzMbxhlaAWLjnCmqz_kGhBYDh2DJa4DopqhbDSZim926XgoyDYhGO_7elUtAg-Sc2qwZvdUviI0z2aqXjk6ZO2PcmubkxsmGjDMdcFkYLYfTP5xQvFxySSWAEnbuIGRKKDTFFrNp6ohWcDV2r2dIawSZyz8bSUS6qoT3oAAXWtOMLzlN5IVbrSU0Dorw75MZvFQst1Tekg8PeZrZshRGAHHXYljimX-AVYSgEdD4zs9tOKctOtqO4dnPnSrLNAFhmBcaS0ZVjzPpxWzV-FECii7Yjh7gS8JSFkazPnmfY1ue1hDkyZg06iJLPd-KmeaK3VKoMHG4gncbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=TRespzmiIBfVoGXrGQasIoCjwm4QFKhzkg9HKPLM_OKwhv0j84vezMI21_V2956ClkPlwBUmaNHhTsjgN0kr28YXtQHlWzuRhHhDtwn5LVtmvzM8vBb-cV07tSsHIqmkDYl9uMViJU2O35SJCVm5CnXa9ymgN7Eu3h0gT4CDexqXZvj21D7TSlOCXXRGAMo0GA-b0plyTT5tjT35ihCeArE6zm0TMD3TmPl-xM2jOTIkRk0QojO3JY5Me5tDh_2AnO8rXcb2IeMnyVkB5QI9r6Zq7qm3AltEi5o_NrgY1VSDyRwrn24fjYTEfSXnlz6RHcOtliNuUxfQk7J2KF_9Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7b5d4066c.mp4?token=TRespzmiIBfVoGXrGQasIoCjwm4QFKhzkg9HKPLM_OKwhv0j84vezMI21_V2956ClkPlwBUmaNHhTsjgN0kr28YXtQHlWzuRhHhDtwn5LVtmvzM8vBb-cV07tSsHIqmkDYl9uMViJU2O35SJCVm5CnXa9ymgN7Eu3h0gT4CDexqXZvj21D7TSlOCXXRGAMo0GA-b0plyTT5tjT35ihCeArE6zm0TMD3TmPl-xM2jOTIkRk0QojO3JY5Me5tDh_2AnO8rXcb2IeMnyVkB5QI9r6Zq7qm3AltEi5o_NrgY1VSDyRwrn24fjYTEfSXnlz6RHcOtliNuUxfQk7J2KF_9Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ترامپ در‌تروث پستی از اعتراضات دی‌ماه ایران منتشر کرد که مردم در آن شعار میدهند «امسال سال خونه سید علی سرنگونه»
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/72595" target="_blank">📅 21:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72594">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK2evUeObznr2h-HWjtzhmc4Lg4-bQppsjnepNmDw8iB8eeBfYuVo8_5BQu1AiMl5RHtjNC_64gihFAcytGstprG18487V4PclcnyRaX2Y8oLQwoulUKqjVtNfgDGxvxOtfZasaJ1MRdYsaJipyWhxJG42_czT8FoS6_bI65rOwI8lv-kClu8WQbXj9Ac6gf7X0n6y_9axOkeWpPKvfMP-AFqsnFez1LRqz00RhEGPF9f5Qmw-bIoIg7rj4Jspv000-IXnpDqawFISJVKw2_5St7jLw0eL74GM_2Gl1zNv_xHtRs3l3Uc8m5kcc2yVb30UEMvxBpDazYXXF0fH4pkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرزیدنت ترامپ:
«گفتم برای از بین بردن تهدید هسته‌ای ایران ۴ تا ۶ هفته زمان لازم است، اما این کار را در یک شب انجام دادم. زمان باقی‌مانده برای اطمینان از این بود که این تهدید دوباره بازنگردد.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/72594" target="_blank">📅 21:36 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72593">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=hNovZY88ObPBr3L3b83Qfc3fjDN6rgUn0UV6xdoVSpA20iXm5m4pBzQeiuhaoumeuM2VdkmHvcAPI2PcDB5qG70h0iBlJxYWTR1DfKuqHJI9NSh1syQt42DeUiFYnmvvXlTlUkxpyu0N4sJw1rNSma_ikL9jXhxW8eCXo1JxsNslZc-D1mwbBNjCS8GMOKNaKegpbDzK3KA7O9_-AhsxnFa322lpLRDtAJPrLd3ZgNixQ7Gaz-CMJOB37hG_-kjL12PUCcP1oPkk54jMrNLuoGx10X1rSSyOc1PvqgUSjcWr9qaaM8ofYC0cr5SY-aBnm_UqWSQcBAbVhP_6KK2dnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/210cf276f7.mp4?token=hNovZY88ObPBr3L3b83Qfc3fjDN6rgUn0UV6xdoVSpA20iXm5m4pBzQeiuhaoumeuM2VdkmHvcAPI2PcDB5qG70h0iBlJxYWTR1DfKuqHJI9NSh1syQt42DeUiFYnmvvXlTlUkxpyu0N4sJw1rNSma_ikL9jXhxW8eCXo1JxsNslZc-D1mwbBNjCS8GMOKNaKegpbDzK3KA7O9_-AhsxnFa322lpLRDtAJPrLd3ZgNixQ7Gaz-CMJOB37hG_-kjL12PUCcP1oPkk54jMrNLuoGx10X1rSSyOc1PvqgUSjcWr9qaaM8ofYC0cr5SY-aBnm_UqWSQcBAbVhP_6KK2dnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیتر دوسی (از شبکه فاکس): آیا ممکن است این خلبان [در پرواز فلای‌دبی] توسط سپاه پاسداران در آنجا منصوب شده باشد، یا به طریقی دیگر افراطی شده و سپس تلاش کرده باشد هواپیما را سرنگون کند؟
ترامپ: بله، ممکن است همین‌طور بوده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/72593" target="_blank">📅 20:54 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72592">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=H1xmBW4GraL-RgLkbUvuRwBDLFrHJMe7_TThKri5hejkpuQc95qVTmuaI6VHlPTFcBjYlHdBOTEzKSBy0-dLZceG0Hc6ebQEY7S17M62vBlZgpdrzr_qa4wckbUeFIPEdaUGHdVFK82MRNm9Fo5c7cVOTqOyCfuI3qGUNvH5TZuQF9LcHqxb-CztzyiXJXMLJVT3AIq9A7gvmcSQ2J-YYpUR6oFgIw7HgEKQq2e4rBMQ35nA7563x4-Ah4F6fDYL7c5_UzULzPp-KDGTzhKesNbFuXr-do2gKfanWv7MREH5dJFmrNHKd4HQgXIae87oBsil44m8whOfHmBfvSvOzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/31205a46fc.mp4?token=H1xmBW4GraL-RgLkbUvuRwBDLFrHJMe7_TThKri5hejkpuQc95qVTmuaI6VHlPTFcBjYlHdBOTEzKSBy0-dLZceG0Hc6ebQEY7S17M62vBlZgpdrzr_qa4wckbUeFIPEdaUGHdVFK82MRNm9Fo5c7cVOTqOyCfuI3qGUNvH5TZuQF9LcHqxb-CztzyiXJXMLJVT3AIq9A7gvmcSQ2J-YYpUR6oFgIw7HgEKQq2e4rBMQ35nA7563x4-Ah4F6fDYL7c5_UzULzPp-KDGTzhKesNbFuXr-do2gKfanWv7MREH5dJFmrNHKd4HQgXIae87oBsil44m8whOfHmBfvSvOzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اظهارات ترامپ درباره احتمال دخالت ایران در حادثه هواپیمای فلای‌دبی:
بر اساس آنچه می‌شنوم، پاسخ را «بله» می‌دانم، اما در حال حاضر مشغول بررسی آن هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/72592" target="_blank">📅 20:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72591">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=pSHdJv2qn_noWYTCcVs2N_unPY5Ugg1vYQVSq3zsQ5fADonLzoTpwnGsBy2_bm198Z86sP0FzBSSL2k6pt9YJ-dlwrdKYT_-MyAMeEQ7Ke8i33AQbp5m3F7RdMrXNcZ3ta9AS4Tm2veszOkiA2-zvi2D7MTMLyhrzKA2RH2l3RpL2E_w8Gc4U6CeC5mnqx_Ni13EvPKMjUia9hsk72Powsx-5Fd3x_PPBPWgy2zvWh7IqifwEYjv3N2AqK909Ys_qDWFxJuNJdnsbizFg2x572sQEB3bMEiZclieYTpY8cKwa046-rqSS7ypL7HRrBCkczmbIO5QeKaRpD_XvTHYdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b0dca1ef0.mp4?token=pSHdJv2qn_noWYTCcVs2N_unPY5Ugg1vYQVSq3zsQ5fADonLzoTpwnGsBy2_bm198Z86sP0FzBSSL2k6pt9YJ-dlwrdKYT_-MyAMeEQ7Ke8i33AQbp5m3F7RdMrXNcZ3ta9AS4Tm2veszOkiA2-zvi2D7MTMLyhrzKA2RH2l3RpL2E_w8Gc4U6CeC5mnqx_Ni13EvPKMjUia9hsk72Powsx-5Fd3x_PPBPWgy2zvWh7IqifwEYjv3N2AqK909Ys_qDWFxJuNJdnsbizFg2x572sQEB3bMEiZclieYTpY8cKwa046-rqSS7ypL7HRrBCkczmbIO5QeKaRpD_XvTHYdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#مهم
:سؤال: در مورد نیروهای نیابتی ایران، مثل حزب‌الله، چطور؟
ترامپ: سرنوشت آن‌ها به سرنوشت ایران گره خورده است؛ هر مسیری که ایران طی کند، آن‌ها نیز همان مسیر را طی می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72591" target="_blank">📅 20:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72590">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">ترامپ درباره ایران:
به جرئت می‌گویم که صددرصد مردم — از جمله در سراسر جهان — با دستیابی ایران به سلاح هسته‌ای مخالف‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72590" target="_blank">📅 20:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72589">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سؤال: اگر ایران پشت آن حمله به هواپیما باشد، آیا دست به تلافی خواهید زد؟ آیا آمریکا تلافی خواهد کرد؟
ترامپ: ضربه بسیار سختی به آن‌ها وارد خواهد شد؛ نگران نباشید.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/72589" target="_blank">📅 20:43 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72588">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8061e95725.mp4?token=iaGUyFln2PsXUAtVNUHpF6ET94QQynPVL6KsikmSvlhLIjgHqzC-kbF1IovqqBCebhMV67p2dDiolbXDpLaYhAXJdcDkPRsw1Xxh-WvFUtMlDYw1fdJb0hnnAQSH_Ul05bXwsIalzLM2NBndMfkG60Ty03AHdayO2gAF7YmqrOsox3ln8ltgoR6Q2NT6WzIqS6_2elY5tpa-SH_WWKv_U4PXRY8x0ElPaloDJszit5nRhJR0eJad_z0p8KhnH7YZ_clXhbRvmpUY_MqhckxHfgYLN5tHjSWeh-UTTakV8XG_v9e9UBh1wEXFZjrAxLXZg70XkuqWYc1LKgDd5i142w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8061e95725.mp4?token=iaGUyFln2PsXUAtVNUHpF6ET94QQynPVL6KsikmSvlhLIjgHqzC-kbF1IovqqBCebhMV67p2dDiolbXDpLaYhAXJdcDkPRsw1Xxh-WvFUtMlDYw1fdJb0hnnAQSH_Ul05bXwsIalzLM2NBndMfkG60Ty03AHdayO2gAF7YmqrOsox3ln8ltgoR6Q2NT6WzIqS6_2elY5tpa-SH_WWKv_U4PXRY8x0ElPaloDJszit5nRhJR0eJad_z0p8KhnH7YZ_clXhbRvmpUY_MqhckxHfgYLN5tHjSWeh-UTTakV8XG_v9e9UBh1wEXFZjrAxLXZg70XkuqWYc1LKgDd5i142w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛رئیس‌جمهور ترامپ درباره ایران:
اکنون باید تصمیمی بگیرم: یا ایران توافق را امضا می‌کند، یا دیگر وجود نخواهد داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/news_hut/72588" target="_blank">📅 20:28 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72587">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ درباره ایران: «آن‌ها نمی‌توانند سلاح هسته‌ای داشته باشند — و نخواهند داشت.»
انها توافق کرده اند که سلاح هسته‌ای نداشته باشند.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72587" target="_blank">📅 20:24 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72586">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">خبرنگار: لارا ترامپ گفته است که جنگ با ایران ممکن است انتخابات میان‌دوره‌ای را برای شما به خطر بیندازد. آیا موافقید؟
ترامپ: ممکن است. [اما] باید کمک‌کننده باشد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72586" target="_blank">📅 20:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72585">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=dBy3uin3cA4oXyfhWLaEsOFVxsAsvwEXTD4Fdx9PPMYKvAni8bqw4T7obhgFhQeykfirn1vWHOw9yvdRDD9LXwhlVAW19XbgqT1KwTeSwIR9cL20srMmnObWWMGfq0mqkneLD10Jj8YqdH8AZSTFZ1UIIfxk8Hd-5WfFrKyfnXXI2teUpOP26CZjEW-1k-vJ0cAw5ZHMs7i_oSPYB_-5TdTkIeRh7LvUA2GxwmWT-7UVhOP3ZlOm1nfLeUNWF5RjNKjcAuViS4hWAhAcU_7ztCE-DHzrWDRTUnm6sR7bBi9qhZE7EOqL7y_tTQNmDCI7liz-vtCba8ZlnKeaqRrSug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/72ce76f49c.mp4?token=dBy3uin3cA4oXyfhWLaEsOFVxsAsvwEXTD4Fdx9PPMYKvAni8bqw4T7obhgFhQeykfirn1vWHOw9yvdRDD9LXwhlVAW19XbgqT1KwTeSwIR9cL20srMmnObWWMGfq0mqkneLD10Jj8YqdH8AZSTFZ1UIIfxk8Hd-5WfFrKyfnXXI2teUpOP26CZjEW-1k-vJ0cAw5ZHMs7i_oSPYB_-5TdTkIeRh7LvUA2GxwmWT-7UVhOP3ZlOm1nfLeUNWF5RjNKjcAuViS4hWAhAcU_7ztCE-DHzrWDRTUnm6sR7bBi9qhZE7EOqL7y_tTQNmDCI7liz-vtCba8ZlnKeaqRrSug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛ایالات متحده در حال اعزام گروه ضربت ناو هواپیمابار «یو‌اس‌اس تئودور روزولت» به خاورمیانه است.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو کشتی تهاجمی دوزیست در اطراف ایران مستقر خواهند شد.
@News_Hut
| NBC</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72585" target="_blank">📅 20:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72584">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a42198336a.mp4?token=TODsXm8I8q36Q9rKFCs4U9YOAPq1R18zDzYb7R7s4Z9z45MZqtQjo6kmtNQtJbJY6TuHvU561bVou1JJZD9GSAhQ47reaiRXMc2qvTB_fnYKhmjSIptYheR6SD4aJfZikc-DAP8jbvMgza_iiiALgIG2ysQOe5GaIAo8BTX4xW56P9g_aYH5zDNbN4x4Zmi4mc4h4w4UA0mcdaKZJH90tZe6eNj5z6ucatNQS1s810kGaGmfV2FdUz39CGJQlas_99JLf8KKU_yzb7BgdXpDmMaDMS0autdtJhskNg655x8i3m1NVv1RvmuFu2lsS5fxm4MlAa6w-zVEnNMKTFhuHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a42198336a.mp4?token=TODsXm8I8q36Q9rKFCs4U9YOAPq1R18zDzYb7R7s4Z9z45MZqtQjo6kmtNQtJbJY6TuHvU561bVou1JJZD9GSAhQ47reaiRXMc2qvTB_fnYKhmjSIptYheR6SD4aJfZikc-DAP8jbvMgza_iiiALgIG2ysQOe5GaIAo8BTX4xW56P9g_aYH5zDNbN4x4Zmi4mc4h4w4UA0mcdaKZJH90tZe6eNj5z6ucatNQS1s810kGaGmfV2FdUz39CGJQlas_99JLf8KKU_yzb7BgdXpDmMaDMS0autdtJhskNg655x8i3m1NVv1RvmuFu2lsS5fxm4MlAa6w-zVEnNMKTFhuHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">درگیری ثبت نامی های خودروی لاماری با شرکت وارد کننده، که ادعا می‌کند به دلیل محاصره دریایی چیزی وارد نکرده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72584" target="_blank">📅 19:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72583">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=SpwDMyK0NyISh97xLYsQhpFtldl2Nrqebu98VEFeX8yJGNyIHOySOCxqDqjqrGMi84Iu26_e2ve2NW41kpg-Xj4gmCoO3jE4ovEtCF7KTkwEgDAIPTljO1LRoBC7jJQHYlC63sN90MKX9tA4w6rFyfWOsnczALIUTfXQ6kuay2ylA1yr2e_aVQdbxVBlH5KFx2UWO09w1ZQP-DJNFrXR_86aQdWPfrQkGu_SEjrS8mlmvUiWWj7e-FoX2t3ZCy_rziItY0B1Xxc9Yk2q9ccRliOmXL361JdRDrC1lQ1rbeRKxOR2zpR3SCNY2E47d31sXEzczghFJKNPVe5LqcR9ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5610e80a6.mp4?token=SpwDMyK0NyISh97xLYsQhpFtldl2Nrqebu98VEFeX8yJGNyIHOySOCxqDqjqrGMi84Iu26_e2ve2NW41kpg-Xj4gmCoO3jE4ovEtCF7KTkwEgDAIPTljO1LRoBC7jJQHYlC63sN90MKX9tA4w6rFyfWOsnczALIUTfXQ6kuay2ylA1yr2e_aVQdbxVBlH5KFx2UWO09w1ZQP-DJNFrXR_86aQdWPfrQkGu_SEjrS8mlmvUiWWj7e-FoX2t3ZCy_rziItY0B1Xxc9Yk2q9ccRliOmXL361JdRDrC1lQ1rbeRKxOR2zpR3SCNY2E47d31sXEzczghFJKNPVe5LqcR9ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهنشاه آریامهر:
«کلمه‌ی شاه در این‌کشور (ایران) معنای ویژه‌ای دارد و همه آن را می‌پذیرند. ممکن است اهالی روستایی دور‌افتاده در کشور درباره‌ی اتفاقات جهان چیزی ندانند، اما آنها معنی شاه را می‌دانند!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/72583" target="_blank">📅 19:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72582">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72582" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/news_hut/72582" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72581">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVxnPMkAGq5hJ7833lYJLfLVUe4f4Dcb4pC0y7rAqTa_iaiotQgu67vGXcXD2Tjj0ZyszLuHlP74rwq4vbBDZcR1oKnkG0hJyxVyl_55HQNR_HazdSj8SQ9pNG7kpKI69fby-94LxSnVt3rFfvTGQSj5rmPj6ZOLj8ZcXc78oqqGdxvyTp7x5npL6L-CZO0pAL7UekmoYjYHtGA-4s0hOTD8JlmpTVtV2mw8afrAm2Jhmrm8eF5ZKkMev0JBwGUH-L2FFU7_APS24QWu5BwHHuI3gejalaokxXNZGccr2LosPyeY8qffUV4ENbfhB8Vdw8UON86OUCGDheLBwOS32Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤩
نبرد هیجان انگیز پرتغال
🆚
دانمارک را در
TrexBet
پیش بینی کنید!
📉
نگاهی به آمار ۵ بازی اخیر دو تیم:
پرتغال: ۳ برد، ۱ تساوی، ۱ شکست و ۵ گل زده
دانمارک: ۲ برد، ۲ تساوی، ۱ شکست و ۱۰ گل زده
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
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/72581" target="_blank">📅 18:59 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72580">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">#مهم
؛
یک
مقام آمریکایی:
ناو هواپیمابر «روزولت» و گروه ضربت همراه آن، سن‌دیگو را به مقصد خاورمیانه ترک کردند.
گروه عملیات آبی-خاکی «ماکین آیلند» نیز دوشنبه گذشته سن‌دیگو را به مقصد خاورمیانه ترک کرد.
حدود  ۲۲۰۰ تفنگدار دریایی در قالب این گروه آبی-خاکی به خاورمیانه اعزام می‌شوند.
تا پایان ماه نوامبر، سه ناو هواپیمابر و دو گروه عملیات آبی-خاکی در نزدیکی ایران مستقر خواهند شد.
با این تمرکز نیرو در خاورمیانه، فرماندهان گزینه‌های متعددی برای مواجهه با ایران در اختیار خواهند داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72580" target="_blank">📅 18:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72579">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/poXXVB6xyYa_Ls0dVuOJivVswr3p8G8zUcFhVK885PILeP77e1SyP0W5Yl-9Hl8YkZr5HyWYmYLDA3W62I4M-fcIWNuNd6Pc5U4F2SEQFLt7u1vo-Yy7QprBpamT7AOvyFdc-m_8bPjtJHUk35WYmbgcur7gOze8md6odsYYzmXfKVmPtPPmlkGQdKQjnXOKFXIu02DAOxV_wB9lQlPklKuoJsshJ6fu-owsRegvAfwhdI1a1ErrEAlZq0FFKDv2QR7UlEfUfeBqLUDy0BtUIIKtdYyPWG3g4BhxyMeKIaWNJxj_SQd2jEqyOTLPY8wKJ_wbuVwk8gEIQr8A2fsqIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امیرمحمد، خواننده آهنگ سنی نردن گوردوم، از بدن فوق جذاب و عضلانیش رونمایی کرد
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72579" target="_blank">📅 17:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72578">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=em_LE4u3Dd3gb0URYBVR_T11Fw6KU9eHAMZ6W1R0Oj0a_6NzcuUo5qAxmfnYwabgEDByzKSXLNQN7eQ6rdvYWcVMXX4q2uhmSRvYf49f0lbv7_Y39RFWIkJt_Y-D70ndfjTNc-xaShi984aDbv3Vii7-Lzd3g0gSlkSKHH8D6veKMOQxousyGOiiDL7ogv0duBKX0sR1CRYfL6P_7grit-BfyAS76Mxju2AVICEOMcCFkfVB-rVOZRhEhjeWfSPmZzOPawGh9TuPeC_knwWR6mPUrA7rP_yt1TUFaX3TbIhEsKKbtQEGKGjzLTdsCm2wUCH0v1V9PpK6X6kRQYMY5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6f32d27e64.mp4?token=em_LE4u3Dd3gb0URYBVR_T11Fw6KU9eHAMZ6W1R0Oj0a_6NzcuUo5qAxmfnYwabgEDByzKSXLNQN7eQ6rdvYWcVMXX4q2uhmSRvYf49f0lbv7_Y39RFWIkJt_Y-D70ndfjTNc-xaShi984aDbv3Vii7-Lzd3g0gSlkSKHH8D6veKMOQxousyGOiiDL7ogv0duBKX0sR1CRYfL6P_7grit-BfyAS76Mxju2AVICEOMcCFkfVB-rVOZRhEhjeWfSPmZzOPawGh9TuPeC_knwWR6mPUrA7rP_yt1TUFaX3TbIhEsKKbtQEGKGjzLTdsCm2wUCH0v1V9PpK6X6kRQYMY5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جزئیات حملات آمریکا به ایران از 28 فوریه تا 8 سپتامبر ( ۹ اسفند تا ۱۷ شهریور ) :
@News_Hut
| thecuriospark</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72578" target="_blank">📅 17:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72577">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=Z5qC4rtMwWLrJH0uSk3VVNdO2WMBgFsHkMGKsWFghbHxRgxDuvf3vGlz-Q6Md7UDhkcyy65dmzruUFd1_ZDHnFOyastBEzvBHDuc0b-a_OAPtUh8USwkiJjWUcID2hEfYBpXQQNFrGR90-KACYok2H-Jyggv-LeXOkyDum0iSPj9HBBig6rLVCVhj0rdL7mnH-oy0KQeIHb0JZVXKFUY-rRW9dtODdMZ_sR8Y7mlCpSQhInCnFWK35pylzzerC9M_pfwqMSO2ItoPMxo5MlLfLHxqOy-pO0E6dwYJ9Nh-0MesHoVWKvbKGh-S_yiXllMwNx8Y6oxMeRfEGAoXTGKkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a8db6d91d.mp4?token=Z5qC4rtMwWLrJH0uSk3VVNdO2WMBgFsHkMGKsWFghbHxRgxDuvf3vGlz-Q6Md7UDhkcyy65dmzruUFd1_ZDHnFOyastBEzvBHDuc0b-a_OAPtUh8USwkiJjWUcID2hEfYBpXQQNFrGR90-KACYok2H-Jyggv-LeXOkyDum0iSPj9HBBig6rLVCVhj0rdL7mnH-oy0KQeIHb0JZVXKFUY-rRW9dtODdMZ_sR8Y7mlCpSQhInCnFWK35pylzzerC9M_pfwqMSO2ItoPMxo5MlLfLHxqOy-pO0E6dwYJ9Nh-0MesHoVWKvbKGh-S_yiXllMwNx8Y6oxMeRfEGAoXTGKkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو رقص این خانم ایرانی تو وان ترکیه وایرال شده و واکنش‌های مثبت و منفی زیادی رو در پی داشته:
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72577" target="_blank">📅 16:33 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72576">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=abeILJ_PsIwdtIgKwsnzilPvvPu3zSoqRJF5D_h2EROFc2wS2hz3nHU3hDOwJvDKWrDIKGpyNSpzmCjNitUyJr2fY1ZSZIeb_sS4iirpuTxHP_90NgSqsL8s0yogOA4UIYEdZzmw-c0LA5Sg-IvFF1MuHdcP6MYKQ8-SytbjAaxfOZRxgwpiK7Q8gNIJqUiq-1tVWra3q7nzmrx5dW00LwP-b1w4F5Uc_9Sg803GtjfIkt30kegJzWxwQ19_v8DIPMMcVw3ByrKuwl_NJjeS8OqgjyOz0dOFUJl04bDiqf4XfoK27k0xMSbM8FeNJtJ7Ls75eWGjL_eiW4WCC1HI3A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a415ffdec.mp4?token=abeILJ_PsIwdtIgKwsnzilPvvPu3zSoqRJF5D_h2EROFc2wS2hz3nHU3hDOwJvDKWrDIKGpyNSpzmCjNitUyJr2fY1ZSZIeb_sS4iirpuTxHP_90NgSqsL8s0yogOA4UIYEdZzmw-c0LA5Sg-IvFF1MuHdcP6MYKQ8-SytbjAaxfOZRxgwpiK7Q8gNIJqUiq-1tVWra3q7nzmrx5dW00LwP-b1w4F5Uc_9Sg803GtjfIkt30kegJzWxwQ19_v8DIPMMcVw3ByrKuwl_NJjeS8OqgjyOz0dOFUJl04bDiqf4XfoK27k0xMSbM8FeNJtJ7Ls75eWGjL_eiW4WCC1HI3A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حساب اسرائیل به فارسی در پلتفرم ایکس:
حالا که بحث هواپیما گرم است، یادی کنیم از هواپیمای کیش.ایر که 31 سال پیش در مسیر تهران به کیش با 174 سرنشین ربوده شد.
زمانی که سوخت هواپیما تمام شد و در شرف سقوط بود، اسرائیل تنها کشوری بود که به هواپیما اجازه فرود داد و جان صدها بی‌گناه را نجات داد.
جمهوری اسلامی هرگز نتوانست پیوند بین دو ملت ایران و اسرائیل را از بین ببرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72576" target="_blank">📅 15:52 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72575">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">ترامپ اظهار داشت که ایران خواستار توافق است و درباره پیشنهاد آتش‌بس ایران که در آخر هفته رد شده بود، ترامپ گفت پیشنهاد ایران برای باز کردن تنگه هرمز کافی نبوده است.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72575" target="_blank">📅 15:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72574">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">سؤال: نتایج نظرسنجی‌های شما هرگز تا این حد پایین نبوده است.
ترامپ: این ارقام ساختگی هستند. من هر کسی را که امروز نامزد باشد، با اختلاف ۲۰ درصد شکست می‌دهم. نظرسنج‌ها فاسد هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72574" target="_blank">📅 15:23 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72573">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">سؤال: اگر «گادی آیزنکوت» در انتخابات اسرائیل پیروز شود، آیا آمریکا می‌تواند بهتر از زمانِ «نتانیاهو» با او همکاری کند؟
ترامپ: خب، نمی‌دانم. حرف بدی درباره‌اش نشنیده‌ام... فکر می‌کنید او پیشتاز است؟
سؤال: او نامزد اصلی اپوزیسیون است.
ترامپ: خب، خیلی‌ها بارها «بی‌بی» را تمام‌شده دانسته‌اند، درست همان‌طور که بارها مرا تمام‌شده می‌دانستند. من بی‌بی را دست‌کم نمی‌گیرم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/72573" target="_blank">📅 15:22 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72572">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">سؤال: گزارش‌های متعددی وجود دارد مبنی بر اینکه پیش از ۷ اکتبر، به نتانیاهو درباره احتمال وقوع حمله هشدار داده شده بود.
ترامپ: امروز برای اولین بار این موضوع را شنیدم.
سؤال: گزارش‌ها حاکی از آن است که مصر و امارات به او هشدار داده بودند.
ترامپ: فکر نمی‌کنم؛ به نظرم اگر او خبر داشت، حتماً اقدامی در این باره انجام می‌داد.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/72572" target="_blank">📅 15:20 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72571">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ترامپ:
اگر من رئیس‌جمهور نبودم، عربستان سعودی الان وجود نداشت؛ اسرائیل هم همین‌طور. آن‌ها از روی کره زمین محو می‌شدند.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72571" target="_blank">📅 15:19 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72570">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟   ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم،…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72570" target="_blank">📅 15:17 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72569">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">سوال: شما در ابتدا گفتید که جنگ با ایران حدود شش تا هشت هفته طول می‌کشد. اکنون وارد ماه هفتم شده‌ایم. می‌توانید توضیح دهید چرا این‌قدر طولانی شده است؟
ترامپ: فقط به این دلیل که می‌خواستم فراتر بروم. آن‌ها را از میان برداشتم. می‌توانستم همان‌جا متوقف شوم، اما می‌خواستم پیش‌تر بروم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/72569" target="_blank">📅 15:14 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72568">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.  ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.  سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟  ترامپ: چون با نابودی ایران، صلح را…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72568" target="_blank">📅 15:11 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72567">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سؤال: در مورد ایران، آیا قصد دارید پس از انتخابات میان‌دوره‌ای، حملات هوایی را تشدید کنید؟ گزارش‌هایی در این باره وجود داشته است.
ترامپ: ممکن است. ما سلاح‌های زیادی در اختیار داریم.
@News_Hut
| Time</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72567" target="_blank">📅 15:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72566">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سؤال: هفته گذشته گفتید که ممکن است ایران را نابود کنید. این همان واژه‌ای بود که به کار بردید.
ترامپ: بله، این کار را می‌کردم. چنین چیزی ممکن است.
سؤال: چطور ممکن است «رئیس‌جمهورِ صلح» خواستار نابودی یک ملتِ کامل باشد؟
ترامپ: چون با نابودی ایران، صلح را در جهان برقرار می‌کنیم. به عقیده من، تا زمانی که ایران وجود دارد، هرگز نمی‌توان به صلح دست یافت.
@News_Hut
| time</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/news_hut/72566" target="_blank">📅 15:05 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72565">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">نتانیاهو با مسافری که به توقف حمله به کابین خلبان فلای‌دوبی کمک کرده بود، ملاقات کرد و به او گفت: «بدون شما، می‌توانست یک یازده سپتامبر دیگر باشد.»
یانیو حیون، لوله‌کشی که هنوز پیراهن خونین به تن دارد، گفت که مهاجم را خفه کرده و کنترل‌ها را به عقب کشیده است.
او به نتانیاهو گفت که برنامه‌های تحقیقات سقوط هواپیما را از تلویزیون تماشا می‌کند و به این ترتیب می‌داند که چگونه باید کنترل‌ها را به عقب بکشد.
او هیچ سابقه هوانوردی یا نظامی ذکر شده در گزارش‌ها ندارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72565" target="_blank">📅 15:01 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72564">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=nhSh8E_8PgvxgIxjgzZSZb8iKVZE4eH5D6Gnm6KPvNghGXlZdrLQ9a0Ho6SyOG8iIGihVzedRyM62wtqSGCnFfeCkYrv4wb1Cs-g0g_I-oSsGBmas3hPWUK7ES5jZZN7f5WZKbDgkjRChRvCIKKjowhcOmxYOPFyh6OQpupE_niYpfYe63pp747U6MJuLqWOqWw4pnhp1p4XX6TTaMvOdkXZRx-ENSqqiVtGw8Q86Ze8DP02sfzQJEPctSWHX-OZgjLfGY0M0tVZMhKOliBp4bz0ULpNNljmLx1O6M7S6yNjPm3Qv1AU9kZSvly79IA2vTNovHFWpsGM7vnzzSoyWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ff0687bd0f.mp4?token=nhSh8E_8PgvxgIxjgzZSZb8iKVZE4eH5D6Gnm6KPvNghGXlZdrLQ9a0Ho6SyOG8iIGihVzedRyM62wtqSGCnFfeCkYrv4wb1Cs-g0g_I-oSsGBmas3hPWUK7ES5jZZN7f5WZKbDgkjRChRvCIKKjowhcOmxYOPFyh6OQpupE_niYpfYe63pp747U6MJuLqWOqWw4pnhp1p4XX6TTaMvOdkXZRx-ENSqqiVtGw8Q86Ze8DP02sfzQJEPctSWHX-OZgjLfGY0M0tVZMhKOliBp4bz0ULpNNljmLx1O6M7S6yNjPm3Qv1AU9kZSvly79IA2vTNovHFWpsGM7vnzzSoyWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام جمهوری اسلامی:‌
گروه‌های مسلح آموزش‌دیده در امارات و اسرائیل وارد کشور شدن، مردم در محلات مراقب باشن.
جریاناتی در محلات استقرار پیدا کردن تا عملیات‌های ترور انجام بدن.
اومدن نتانیاهو به امارات رو جدی بگیریم. طرح نتانیاهو اینه که به‌جای اسرائیل از امارات بجنگه.
+البته این چیزا رو میگن تا تو اعتراضات احتمالی بخاطر تور و گرونی بهونه قتل‌عام دوباره مردم رو داشته باشن!
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/72564" target="_blank">📅 14:21 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72563">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eGX1GsVH-aa96mFehXC33biRRWveyTlTmSpWQEy7Hp0WTeQgXhnSJs1hljfMLYgTX8uY3_lV2fpF5L9-Q_anrf0e4b5frOY81DRFwNomHJaD_WZNluHGS4hystu0-klSCop8f6INF_5Y10fYTHX5DM3ModoFaGmLP7Rbf7Z-zk1-IkIOpCzMoYopA-8x9HUYJes1Kt1nrjKiZdQwKWt4i0DmFIHKgbQih_ax-BAQ-K2WMdQ2WmEmLqpJKMfc9q_1bJfOs-wVoSo4-oSVGc0hi8PjHGf0lu20bQxOczp0-LSsqPsjUACaG3AafP1TDvCUeAYTR0utFKOEQqErQP916g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ گزارش نیویورک‌پست درباره هشدار اسکات بسنت درباره اقتصاد ایران رو بازنشر کرد.
بسنت: ممکنه ظرف دو هفته «چیزی از اقتصاد ایران باقی نمونه».
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/72563" target="_blank">📅 13:44 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72561">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VtA3uXt52kbTEdnZhbNNsnQMu3748xH5lqk_vOh73-qfxUAqjnQrAfqw-nsAC8tHvCRW5T_7YWOlIUkm1BCoxRbPfscQ03Zknc57JvMRsLTm0281ne9rhX8e5RMeF--2hwoITWH3QKdLi1xmjW-1AFjKy0D_mg0quldVrKGW2CJJb7ocnQ0E1TKANmjm4y6B8sVIzAdsf2lRzV7q8_QY5Sh8IX79GyimR96-BlR3MdHNlqYFWz2yzoomQ7Zivj-e29vO9NFeyrKAwVDm4jv-yz1sTO3cdoKy13vb9PIbuEdABAOh3rNfBGbj2PjtDpjWpkj3AwdjXLLWXoiXRwyBWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PDOtaU43VFMLKYtXZa_Cj0t0fyvfGDWPADtdn8QJAWZgl__nxNW-1jF54Kzv4aKecTkeNDBDieFUozrSLYHz7POM1WIQvNxGpFh8yLLv6gVufhexlVcwGyGEnBPDCf9yAcaJA9k-Eq2mJvPlV2QnXTuQqUiwEMtb8F9fAJtTfx7fHyRzltUWExCC8r5lk_BX4rcgg3hMHAjF47I_iRQvxJw46sctJ5F31yNqIZLSFPuRdQXdKHlwb5yijlqq3zg8rtDKqrgGjnGJUcf8ZOOi7TlfARlsIyPhOxvIUCDSpswEmq4fXTVCdXRTXKCULuWg7yE-jPRPnU7eqo4TuFt7PQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بیژن مرتضوی که همین دو سه روز پیش گفته بود شایعات باور نکنید و نمیام ایران دیروز لایو گذاشته که اومده تهران
+پست چند ماه پیش بیژن!
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/72561" target="_blank">📅 13:09 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72560">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/565ee82707.mp4?token=Jdl79ZK_7DauCRU_nR9dL8hlHFSctVxSMsdswdQKMBObWCbCLwhvvkrmyCSCp1FmNBhpnNTb6fKmWRMnF9xCOQPsFpxFK0ywtqNOu4G3BVdgqPNCfeHZdjwfPE3HIGb0RN1qjfHkl1mqcR2fHwc_VK8h3vRTP1dv_qqr1WA5h-1Y1gd3GL_jRhZ3ytkmm2_bJaK4nSzxTAB9H3jEBfNWNLRA_JMd874nUUNIjfKt06Y_Jjb8C5KOkPe0OopqHGQXF0JVM90_z674RllX-Jn1tiVtq0w2RdQ_0FCF7IBz2h8oMCyGLFGfcbpzOI6XvejvMARo4fpk05zn0eW_BM6tjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/565ee82707.mp4?token=Jdl79ZK_7DauCRU_nR9dL8hlHFSctVxSMsdswdQKMBObWCbCLwhvvkrmyCSCp1FmNBhpnNTb6fKmWRMnF9xCOQPsFpxFK0ywtqNOu4G3BVdgqPNCfeHZdjwfPE3HIGb0RN1qjfHkl1mqcR2fHwc_VK8h3vRTP1dv_qqr1WA5h-1Y1gd3GL_jRhZ3ytkmm2_bJaK4nSzxTAB9H3jEBfNWNLRA_JMd874nUUNIjfKt06Y_Jjb8C5KOkPe0OopqHGQXF0JVM90_z674RllX-Jn1tiVtq0w2RdQ_0FCF7IBz2h8oMCyGLFGfcbpzOI6XvejvMARo4fpk05zn0eW_BM6tjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محمد حافظ حکمی معاون وزیر ارتباطات و فناوری اطلاعات با اشاره به قابلیت‌های فعلی استارلینک و فعال شدن قریب‌الوقوع «Direct to Cell» تو سط ماهواره‌های استارلینک و امکان اتصال مستقیم تلفن‌های همراه به ماهواره گفت:
«اگر استارلینک فراگیر شود، وزارت ارتباطات و شورای عالی فضای مجازی را باید شهربازی کنیم!»
اگر قابلیت اتصال مستقیم گوشی‌های موبایل به ماهواره‌های استارلینک فعال شود، سازوکارهایی مانند رجیستری تلفن همراه عملاً کارایی خود را از دست می‌دهند و شناسایی گوشی و مالک آن غیر ممکن خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/news_hut/72560" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72559">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72559" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/news_hut/72559" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72558">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8Fas8Jl1f8Ami4bgLihU1cQvBCJxJXKXEqYqO_Zi2kT5rjRrpKSmpikD7ea46dVqphqOWwUY8cfzxoqKWHxMfZDQ4SRjHpi7VHyYpyMBpG6ZEDh_pmCESQ3p9ucVmw5jOAuJ4ECCcqLyXxCK0kE3lsPcM6fG_osSI7v6ObO4GKaXwmNz_eacz2AlVQ8zia00VaUV1VwvlOLRJ6cMke7tCMLKTO5nfANGqL6xNI5PLqtSl87377QZ_7Li4tSlw_aHnIocWJwknjW1RYIdz1uG6kqXlPagh2GtHiQvRP54CMFkvHpQHkWTtB6I3sQsJiYGJI5Q5XRcih2Fe5YpbZL5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
صربستان
🆚
آلمان
هلند
🆚
یونان
پرتغال
🆚
دانمارک
نروژ
🆚
ولز
بولیوی
🆚
آرژانتین
اکوادور
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
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/72558" target="_blank">📅 12:46 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72557">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RJ2YZQwhsPwFKjtyttluev5EmNZazSB5Cz8N1Z9ymJpoDbzbIDmhG7qeDE9LVLjSamSJJI936OqoW19cPf6qL8p0OVgD8kQqmq1KvRcrn9Wi6zLs9fKvkDKtJvJi-nhWFvmhH06MWtVxfe2ZBcZrI3ItQSbjjAsu6EOZil-evFkCkiYrJO7Npw46m_eJt1gwszoQktTY29lJy2NMMVQdh8IecZMYE4gplexPWHOdlGSHTDyAq4Tagmtze0LTzjzMtD_BWUAuc-7ko-WAY39yYytwgo8B4PE1m22NTf0rTtL7i6dxn_JGO-Sv6dYikG29EihAMVpHuXUpNL-U4hCrcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام اعلام کرد که نیروهای آمریکایی در چارچوب محاصره بنادر ایران، مسیر ۱۲۵ کشتی تجاری را تغییر داده‌اند. این رقم نسبت به گزارش روز جمعه، حاکی از تغییر مسیر ۳ کشتی دیگر است.
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/72557" target="_blank">📅 12:00 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72556">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=bGV7K3b68lcg4y-SddnENB9H4YMH4LuCbwgHXqp1rZWuNl2IklNk9_NhNb4nSfeaEf1hByEanyzk0f2psw6RMKtmhJhCbO4xoNofL5TBeQTR31J4HP9nrnVrI99tkBty8TwaSYpTNzPcaZ5Hk5zhVRURFJXIpJ-FaUPfOJbI7EWlmgPRZ4W0pH3nIIQD-LgKZ5oQIjX-3AWC1UOvicxn8MNntVGHnVc6XYM8S5PqQ4ChWqJYaLcSlY87anrwvJqaajoCdRUBetgTvNmrbXIJBZX8HVFASgC4VWFwYdkk74ByGWWSgbdla8AXwJA9b5JAwHohxR2W1r64Ai798Ipnfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1be557ff64.mp4?token=bGV7K3b68lcg4y-SddnENB9H4YMH4LuCbwgHXqp1rZWuNl2IklNk9_NhNb4nSfeaEf1hByEanyzk0f2psw6RMKtmhJhCbO4xoNofL5TBeQTR31J4HP9nrnVrI99tkBty8TwaSYpTNzPcaZ5Hk5zhVRURFJXIpJ-FaUPfOJbI7EWlmgPRZ4W0pH3nIIQD-LgKZ5oQIjX-3AWC1UOvicxn8MNntVGHnVc6XYM8S5PqQ4ChWqJYaLcSlY87anrwvJqaajoCdRUBetgTvNmrbXIJBZX8HVFASgC4VWFwYdkk74ByGWWSgbdla8AXwJA9b5JAwHohxR2W1r64Ai798Ipnfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند نفر از هموطنان رفته بودن شمال که توی مسیر پلنگ مازندران رو هم دیدن:)
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/72556" target="_blank">📅 11:53 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72555">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mDa07HTBdhwcton7WvS5e-9ZUtKlNlwC2HSAeHdJvk-H-B5gP2Xkhi1KBwbLq7EcQP3MLEVzCkMr7rzujTOBBwz9mgTV3Y6p9d109lWVoWwvbD53aykhh9FiPURn-t3_uqW4wOsgjq897dTJMslewCDvLLDe8Z6AwNQrStSZSgCMBYzXGThuJLXS5OEXvKLp0S2K_XRxg5cyzRAnafdS1N0qtQq-lt0g8NEBFesWKgPriOLqmHWuPvlzTjEwu9__q0H375pY2Uh0BsEJ0iilPjuEFdgVWffUnc5SeDzX83VZdWYkzwcJWF8iq7_bHBaXTDx51GYIxXJDYwJXjL2V2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#مهم
؛اکسیوس:مارکو روبیو وزیر امور خارجه بعد از اینکه مذاکرات میان آمریکا و ایران در روز دوشنبه به بن‌بست خورد،به هیئت نمایندگی ایران ازجمله عباس عراقچی دستور داد که فوراً امریکا رو ترک کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/72555" target="_blank">📅 11:15 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72554">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=cB8MPhPXtPHbjllXcQRYdCwsukof5JstI1BUn0gqkoC9fZ3vAzlK8IUMJkFOIg_UGzb8QO8hLiaTM5ltE-eKj-unTTTHeAAvPX3SRrhB_auqPmukxCygo1-eQ-vdj5OJp1nOiyA-AXqNaXKpleJILDerKkq3Ef5cDTY4ZwQgzWCiOm0E4xcAEV5HOAZfKAXRV23EcShIQknkvhVzpRAnm2pHTAzY3dZgPR_08VQfJ18c0j0R7kMn10PwcX6ntuxEiAHjPLPWy6hdU4Wn5sTdH4VH7WSL8xl5J2FM2tYo5ASk512vbg1-K9VZVpPMsEYdYVIHk_pWnOB3YeWqvJjY9w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/74ab0dda5d.mp4?token=cB8MPhPXtPHbjllXcQRYdCwsukof5JstI1BUn0gqkoC9fZ3vAzlK8IUMJkFOIg_UGzb8QO8hLiaTM5ltE-eKj-unTTTHeAAvPX3SRrhB_auqPmukxCygo1-eQ-vdj5OJp1nOiyA-AXqNaXKpleJILDerKkq3Ef5cDTY4ZwQgzWCiOm0E4xcAEV5HOAZfKAXRV23EcShIQknkvhVzpRAnm2pHTAzY3dZgPR_08VQfJ18c0j0R7kMn10PwcX6ntuxEiAHjPLPWy6hdU4Wn5sTdH4VH7WSL8xl5J2FM2tYo5ASk512vbg1-K9VZVpPMsEYdYVIHk_pWnOB3YeWqvJjY9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توی یکی از وبینارهای مملکت بین یه دختر به اسم "پرنیان" که پزشکی قبول شده بود و "اشکان" که کنکور مردود شده بود، یه مسابقه برگزار شد.
نتیجه جوری شد که همه آخرش ایستاده اشکان رو تشویق کردن:
@News_Hut</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/news_hut/72554" target="_blank">📅 11:06 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72552">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/DnAJVO68yZu_ltcN3WqhXG9KGKwWS_7O6LVtOZKknqchMbFmyyTwCSwsg8gLWTKyWtvZPxLrK1O-J9I8vdoiBPswUd5IU_tM-sh9sWgMCAzPbWbDRp6tkySjOxSbCifbl4YUoV4Cdqo_bayD3o-MIznfaDCBHRXrHGWt1WFIpLrbSxkrHpF3BOtzTKrBzfT0wj4__ccW39bWFAs9BJbR19rHogVoWj2W0mh021Ll58ZQ23BBbDcc46qYFwDsGajA1BqqWZVQhQ1e-1chERIlIM7ffI5IRzVbhoFMsbBlvEIp96AgMgYhB60lqZnV6-X_0sHF7vDapCwMaMAYhw60Jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OHKYACcLE7YdVlI9goEg881N-BUzm9hV-0QlRS6JhYo_F3ZqPhpYjzv0WBTiK8DD8tO-a9eBKiNHQ3eD4YLUTV1e7lHwfiFNfAkx8QqG4yMoD7G833c-wZnAgS2zLVPuUo26pzfleMNKTNVpGczVQcZJrFUGdaQUAggLekgzR4wnvbWPjAbrbt_32de_bRePdaVZP5KjS3fVQQBV1JuV18x6XyK8sl7fWqYKZeogedZJgHfNZ06-4trjdA97cXjjs_f9v9N4r92BSCDr70utnFqWR7UE-DfHUv2lXLh4y_l5rOhyN5VGsozuiq5EWoglCR3UtSbnCJiVMXujut349A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی از حامیان حکومت: من 13 ساله که یه بیماری درمان نشدنی دارم، دکترا قطع امید کردن و گفتن و تا آخر عمر درگیرشی.
تا اینکه یه شب رهبر شهید اومد به خوابم، بهم گفت درسته من کشته شدم، ولی مملکت رو اداره میکنم.
یهو اسمم رو صدا زد، مصطفی! رفتم جلو و بهم انگشتر هدیه داد، صبح که از خواب پاشدم دیدم الله اکبر! هیچ اثری از اون بیماری نیست و کامل شفا گرفتم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72552" target="_blank">📅 10:32 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72551">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=kJecFyBXwljlclq_QERA23iAep58UJwlfAHQJ4H-7DD1RcnQkwFvvbsHKU720dOis-77co2O1m0u9HxoSbttsbi0zpgzoX8oJl8vsNKjr6y9mcuVBxwIm4Ug_wzA8c9hs5RREj__R9lZI2f24NQ6RsNuF-QkjE-D_Z2cbW8yaEAyIhny8CBlAv3yOihDhgy0Hvc7EV_s4nZb8gY7yEx9Pys_Trje1GIQlJh2cTnylhvRm3v1KAdC_UnmNH3K4mBPilJDTNH8z8DnrvzmpPQBEe4DFQ3LjuyxR3UxO6ZWdsrq8ZfkG2phM2Z5JwWDCUZrw6T58s8oggPRxJVMo97tEA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/b14d6c45e3.mp4?token=kJecFyBXwljlclq_QERA23iAep58UJwlfAHQJ4H-7DD1RcnQkwFvvbsHKU720dOis-77co2O1m0u9HxoSbttsbi0zpgzoX8oJl8vsNKjr6y9mcuVBxwIm4Ug_wzA8c9hs5RREj__R9lZI2f24NQ6RsNuF-QkjE-D_Z2cbW8yaEAyIhny8CBlAv3yOihDhgy0Hvc7EV_s4nZb8gY7yEx9Pys_Trje1GIQlJh2cTnylhvRm3v1KAdC_UnmNH3K4mBPilJDTNH8z8DnrvzmpPQBEe4DFQ3LjuyxR3UxO6ZWdsrq8ZfkG2phM2Z5JwWDCUZrw6T58s8oggPRxJVMo97tEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از کلاسای دانشگاه مملکت، یدونه پسر، با ۵۰ تا دختر، همکلاسی شده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/72551" target="_blank">📅 10:03 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72550">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Ze24Cm1t0Enn8oo3y0y_7XCIVyK9jhWL60MDeCRNKMbduJLrw_Mri16r1DaUhNYlVkIBZGYr0NY-18lIaYcrXpI0W0pcTpoG8FTFP0OnC4BksqTR7j-enUPxpjmz0tII-IMbkaEG81VzgXz7Fdg3G4blopMupKw-ICoVq-n9mFvGYrVrs_W37sdQc9L2egQSz1BghtKrBUtpcHjz9d1_13xWm_2L-0kyJi-N4G4w21pG035JbwrOiYzLi8B9H3TgsoepyIv-cW4EfhEAhIxR9jRFMiqhgXFGIM4vQE8A-n7ZSiH08013JQFEpuHiRB3aoXNc7XyNzUcyLEtIyTAgjIAZSw3qTG2aGqktJoyT5M8ajbMC911waE872TVu5Znc09Q2jC9Hfh0xcsB7y0hknnrWiKMzRSuH5GZQBvUjV-f_u6nbVTTMDdCj3qrM30hXzeP59Iy3NcEdrNZHCPBSQkgyMyqCZAYVXPKdWgCQ5Q8cwvVgneR-rOwLwlAZvlQTisvkCuZKGw2XChY2tTeItK0n3Vcvp_wd5Gda2Z8q5xhahUrXSniIldcpuB4ZeJaimrrmuR5cOYOvhtN6Z7W5fwsTdjhg2C-5OIaQwy8SE_SCf5VRoYw4T7ZAhvv9FkCcZrEEJ0g_tqU2NA0KQMgfsTTSAcv2JdCQZRgi5I6gpLI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/969c5e0df6.mp4?token=Ze24Cm1t0Enn8oo3y0y_7XCIVyK9jhWL60MDeCRNKMbduJLrw_Mri16r1DaUhNYlVkIBZGYr0NY-18lIaYcrXpI0W0pcTpoG8FTFP0OnC4BksqTR7j-enUPxpjmz0tII-IMbkaEG81VzgXz7Fdg3G4blopMupKw-ICoVq-n9mFvGYrVrs_W37sdQc9L2egQSz1BghtKrBUtpcHjz9d1_13xWm_2L-0kyJi-N4G4w21pG035JbwrOiYzLi8B9H3TgsoepyIv-cW4EfhEAhIxR9jRFMiqhgXFGIM4vQE8A-n7ZSiH08013JQFEpuHiRB3aoXNc7XyNzUcyLEtIyTAgjIAZSw3qTG2aGqktJoyT5M8ajbMC911waE872TVu5Znc09Q2jC9Hfh0xcsB7y0hknnrWiKMzRSuH5GZQBvUjV-f_u6nbVTTMDdCj3qrM30hXzeP59Iy3NcEdrNZHCPBSQkgyMyqCZAYVXPKdWgCQ5Q8cwvVgneR-rOwLwlAZvlQTisvkCuZKGw2XChY2tTeItK0n3Vcvp_wd5Gda2Z8q5xhahUrXSniIldcpuB4ZeJaimrrmuR5cOYOvhtN6Z7W5fwsTdjhg2C-5OIaQwy8SE_SCf5VRoYw4T7ZAhvv9FkCcZrEEJ0g_tqU2NA0KQMgfsTTSAcv2JdCQZRgi5I6gpLI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اولین موشک اتمی جمهوری اسلامی در  ایتا و روبیکا آزمایش شد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/news_hut/72550" target="_blank">📅 09:30 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72546">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/A1tWef9zhltds_w4dADzDOMncQFiBPnzkP5BDRtftu7YxFxM16SQivW3UwRoB1Eaek2GH7OTGiR2_E4mCWohLRAlEymSgg82riSm7d1Nle9dO-YPfA438HUmJYih2Z-iJh-lsOMT1VYtaU8bFu3VXEn8MghF9x4X12KmjQaZgFUEDO8twQCFUdHgJ-aAvexM0LSkvqXds4rRPymVJ4KoRqDtZt54hneccMS0QmWE1rrD7Dv5qt5OnKR0E4lfEQpeJc2Cq5vACNY1LkI3J6ncuB98suWbjn5hNcwmF9MLV1dRovsDhV5boGYrnd-s6WKFPY1ApAfxAKUJW1-QVsQzUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/oAEGNs4Nnw7R_jNK-XNGplGBBX5_GBq7F28yL8Kv6dfJZ8OIGz6HfX1zFwConBUrkmyDLNxu57Et0tagW6XSi5HmNZh30wbKnxePvFM_L_5ik9V-Z-l0aj003xJrcbqFPn7Rw0a5z4pwPcNi5TMTuPqbO6Jo8N1zyY1DW8k2hCnM8T8AnkrJa-Gd0tHdfQrkqk5UBI_F7hehvkb1LoyDb9H9froFN4aXs2R6_D9gwKMW2mmUhv7lbW76CY7mZGl4DfAbpgvcKfaJ0IbtZ0mC0dDqhBUMRjXApnwkWrb066P6xqn46RDa5Eb-B1YX65NhJdxBDjYKqDrL3jk9nmI5nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VwgjprHq-jhKoTcFVgwqNHLrOYoCT-WFwHgbE3Nw7SB-ftltC_iRuYdKOfh2LqzwtRHvcbfNVDnwXozp-o6hxr-P_dJpHzfugSK8WOjVm02AUecjWRT8LYzLcfUh6iR74g4TQ1wA1QCWR54ijyJmgQ8ztEy8HXA9N5CHcOnxbsFNbDQ-S2OGf9kvZe8jUIAv0nskRp49_SKn3C87p0JwpnIKlBRITtvqFVfoBTnz7S_v7H9m1gsTh9QPgU4K0AduUUJBa8AsW2MXk8pd17L3hWK6p0ysMw4RfqAjtHyL6CrbuCxm4fV1BHWoL3k88KpiCqRndNCWJ24evvZC62Lkmg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=SwUrMXkfbj_jkXqLPUu7VHXOCCprxac7xIOiS_hYsdv17qfDjxkHcdoA-_h1OlilLNO7_Bg9nxpKcGpjng_86UOxQMsQIohD-JjOl3r4NadvcDmbj12YHAOSC0o6XrdtT2eNL9fGACtYyg4EqFfZsrujitCOHO2vwOLpsLtJpvMHarzCylbgtkG7zCUOIykMLsUmCtLWyIiqIClpach_lV2E43_sFIebqv-wJoqCKN2WG4ptB_V92wSEW227xXr0i43QsIt9Td3A1hXtkmeLjZdqHmh3yUMg1yw2XGvLhluURcmXZO82gJtyZkmG_KjMM67aOqkSUSi5h6jN82BxFA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/eb63ca7239.mp4?token=SwUrMXkfbj_jkXqLPUu7VHXOCCprxac7xIOiS_hYsdv17qfDjxkHcdoA-_h1OlilLNO7_Bg9nxpKcGpjng_86UOxQMsQIohD-JjOl3r4NadvcDmbj12YHAOSC0o6XrdtT2eNL9fGACtYyg4EqFfZsrujitCOHO2vwOLpsLtJpvMHarzCylbgtkG7zCUOIykMLsUmCtLWyIiqIClpach_lV2E43_sFIebqv-wJoqCKN2WG4ptB_V92wSEW227xXr0i43QsIt9Td3A1hXtkmeLjZdqHmh3yUMg1yw2XGvLhluURcmXZO82gJtyZkmG_KjMM67aOqkSUSi5h6jN82BxFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دارن خودشون به جنایت جمهوری اسلامی اعتراف میکنن!
دو روز پیش توی بندر کنگان، مامورا می‌ریزن خونه یه نفر و جلو خواهرش به رگبار میبندنش!
انگار گزارش داده بودن اینا گازوئیل قاچاق میکنن و مأمورا ریختن در خونشون، تا پسره درو باز میکنه، به رگبار میبندنش.
پسره، باباش جانباز شیمیایی جنگ هشت ساله بوده و خونوادش ۲۰۰ شب و هر شب توی تجمعات شبانه شرکت میکردن!
حالا خواهرش پست گذاشته که مردم راست میگفتن، این حکومت قاتله، ما اشتباه کردیم، داداشم و رفیق بی گناهش رو به رگبار بستن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/72546" target="_blank">📅 09:04 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72545">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/72545" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72544">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/news_hut/72544" target="_blank">📅 01:41 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72543">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dxp1EogqqpJUnmck4DW6IYsRBB9ncBMHdhpEU3B3w8S8VMdGm-LYRWYOHkpB5ASjttFMKXnCP2ucCCYtSV5pNECOnbHRac9C06Yr66PnEEtuQg-egkJX-zKdRsiYt-9uGLjwseYxJ3bPvnKte2PiuXHzl6EhLeOO1adQqv2WV8AGg2spyw2d8riSF5y6APk_-ab4_JuUIZ8zTyi1-0fG5wghHlo3ShGkUXl1z3a-7fvXqBcf5xG1Swo_QhgU3ZbHDvOVzXiOW32bNx3wRI6AfQqInSiuMTZptMfMCFHzprSWoZ0D6K_q0lmRCyMxkLXRRRoep96wf4zIMVXa9slC-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرواز پنج فروند سوخت‌رسان آمریکایی در نزدیکی تنگه هرمز؛
+دارن نفتکش رد میکنن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/72543" target="_blank">📅 01:29 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72542">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=Rp16dWwwHV1AiKK0WBmJpkoVZRAMFP22Kpzfzu-bUhgXI4C086OOCjDDRW-b_kI9IdEEoLjHPFeXeiyK2qGx5MKWRMD4LU5F7ToEqD0cEzQFKQNjdK38O44D_2n-3Fmm3KgrXjT22_NVpizx2x94oNXmFytJtCfrJQ9dDKTCtWbiRLAZcL2Z1JiyPAka75NdgDjYASnW9dsoQnL30s16DDVNfUAd448ztnWcXcqIb_gHX9SmpdDmwMPRISY4EnZu7jZKh-7UspsyShBFMq2Z6oPViY9EQ6NCAUdke-cPjBhnkKLtSu79hT8B1SgJgyfCWPxLEQJXvwgFoKylzBZQNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d22a56348.mp4?token=Rp16dWwwHV1AiKK0WBmJpkoVZRAMFP22Kpzfzu-bUhgXI4C086OOCjDDRW-b_kI9IdEEoLjHPFeXeiyK2qGx5MKWRMD4LU5F7ToEqD0cEzQFKQNjdK38O44D_2n-3Fmm3KgrXjT22_NVpizx2x94oNXmFytJtCfrJQ9dDKTCtWbiRLAZcL2Z1JiyPAka75NdgDjYASnW9dsoQnL30s16DDVNfUAd448ztnWcXcqIb_gHX9SmpdDmwMPRISY4EnZu7jZKh-7UspsyShBFMq2Z6oPViY9EQ6NCAUdke-cPjBhnkKLtSu79hT8B1SgJgyfCWPxLEQJXvwgFoKylzBZQNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوال:
شما ایرانی‌ها را دیوانه توصیف می‌کنید. چطور می‌توان با آدم‌های دیوانه به توافق رسید؟
ترامپ:
شاید هم آن‌ها را منفجر کنید. ما باید در این باره تصمیم بگیریم. یا آن‌ها را منفجر می‌کنیم یا توافق می‌کنیم. زمانش دارد فرا می‌رسد. ماجرا خیلی زود به پایان خواهد رسید.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72542" target="_blank">📅 00:51 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72541">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=oyCjKohJe9H_arL8mIFQUb9zmE57D_wNIGqk9LKYoIBAKIab88LxFYxHpUGhQZTtjepRmTQ4wLDUXZ4vOFLzg0avg3WVE9Etp00hynfK2Fqm2VTcWvNx3j5sZUYiTY8GtGn6e32S52Tv5eiCLuAhga-aOsBm9kx5pJFIuWT_uoqK1QYh7sreZfET0_y3LuI5kO9wkadcnzSoT0SgoknvAVuUex7xRk8o2I1Dz1DJbzQX9fn7HLab7TyUsYknz2sxDMQeTIl4LdNCQu42kKD26TqtRF0Ae4MRlBoRtLapSOyXsseEXo2JWRk2NSRf2jemvSvXyCGWQZZWJu4nCeypqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/02359c50e8.mp4?token=oyCjKohJe9H_arL8mIFQUb9zmE57D_wNIGqk9LKYoIBAKIab88LxFYxHpUGhQZTtjepRmTQ4wLDUXZ4vOFLzg0avg3WVE9Etp00hynfK2Fqm2VTcWvNx3j5sZUYiTY8GtGn6e32S52Tv5eiCLuAhga-aOsBm9kx5pJFIuWT_uoqK1QYh7sreZfET0_y3LuI5kO9wkadcnzSoT0SgoknvAVuUex7xRk8o2I1Dz1DJbzQX9fn7HLab7TyUsYknz2sxDMQeTIl4LdNCQu42kKD26TqtRF0Ae4MRlBoRtLapSOyXsseEXo2JWRk2NSRf2jemvSvXyCGWQZZWJu4nCeypqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
رهبران ایران با تمام قوا برای به دست گرفتن کنترل می‌جنگند؛ اما کنترلِ چه چیزی؟
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/72541" target="_blank">📅 00:49 · 09 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72540">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=O6sF9ABmbPXvHylpY8_DuV3bmHvd7wKidXdMhmXJFJW-0Bh-JgerCUOzU7-_KL82tTy3B50213YKeiOW3cWgkqLXMjjcVMHk9Pq-ZlQtk3YFttlz1vr58FftB8bEB3uaOeoCsfnfLE7SprDAYm0DTZwlfZeGjFb-fBg0uibl3aD2AWFwalvshGQk4ZVmWjIBsYqFEGITWTaQvsbYlYS8EEeSZ7hB1bfR81ob4SpB9BhUnWcBsNxKEmch1JNQufc698eGKqeZuilw9dwt_FbChrFEJ3zXy5zhHOXQMzA4_-yDjwQd5hF52Io2IG_Y5gocPDhz5j6wT0rpQ-OoklJhGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fe1c6438a6.mp4?token=O6sF9ABmbPXvHylpY8_DuV3bmHvd7wKidXdMhmXJFJW-0Bh-JgerCUOzU7-_KL82tTy3B50213YKeiOW3cWgkqLXMjjcVMHk9Pq-ZlQtk3YFttlz1vr58FftB8bEB3uaOeoCsfnfLE7SprDAYm0DTZwlfZeGjFb-fBg0uibl3aD2AWFwalvshGQk4ZVmWjIBsYqFEGITWTaQvsbYlYS8EEeSZ7hB1bfR81ob4SpB9BhUnWcBsNxKEmch1JNQufc698eGKqeZuilw9dwt_FbChrFEJ3zXy5zhHOXQMzA4_-yDjwQd5hF52Io2IG_Y5gocPDhz5j6wT0rpQ-OoklJhGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنجاقک‌ها زیباترین مدل رابطه جنسی رو دارن.
اونا بهم متصل میشن و شکل قلب تشکیل میدن و تو همین حالت پرواز میکنن و... تا کارشون تموم بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72540" target="_blank">📅 23:32 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72539">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=Ncwj-W8KZP4NOnh3R7NmexQQLSqya0Ws5TNl4wd_bcJYaRFWNN8kbCYYecQ9Tzz8DHf0ZCBvpQL1j_sgkZNHOdUT5Go3fuLaPxO50rrSEA_Vw0zCsWzldbEy2JOq1jSvw1mBQ-r-oSBRi8p_YCOI5WhKL_X3SKGcHkOU_dBsBIA42-sIvSWOWu-hdJZyqiPzZHLWw6lb_xDYLjSJOau5hRyxhaKHaidA1dP17ak2AEXn4N68QznxVu3gPDuuRxYoadRoiUw3_DfdV3yLX5FuXASbWRJgDIeyrbMVaIQxJZ0FEnWBQlRNtchwUooo8LfogCSc58MpMVCYie7BaxdfUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5a16c7cb51.mp4?token=Ncwj-W8KZP4NOnh3R7NmexQQLSqya0Ws5TNl4wd_bcJYaRFWNN8kbCYYecQ9Tzz8DHf0ZCBvpQL1j_sgkZNHOdUT5Go3fuLaPxO50rrSEA_Vw0zCsWzldbEy2JOq1jSvw1mBQ-r-oSBRi8p_YCOI5WhKL_X3SKGcHkOU_dBsBIA42-sIvSWOWu-hdJZyqiPzZHLWw6lb_xDYLjSJOau5hRyxhaKHaidA1dP17ak2AEXn4N68QznxVu3gPDuuRxYoadRoiUw3_DfdV3yLX5FuXASbWRJgDIeyrbMVaIQxJZ0FEnWBQlRNtchwUooo8LfogCSc58MpMVCYie7BaxdfUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای زیبای این پسر در مورد وضعیتی که برامون ساختن، ارزش اینو داره که ده بار گوش کنی و براش دست بزنی!
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/72539" target="_blank">📅 23:04 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72538">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OXCSTAiChnMmSCMNVRUqpRjsChuQQQlqpK4-ej_5RWghYwIbNLgAhM8oWNGU06vfwoqCFgjnb80aUg1gM-5OkHkkwyoScNgW-uuA3HyClYsWxdI3oeV8IB7uGTexEWJbg6ZTtA9VMZHyZflHNdndwP7iwLZgyzJRl3CBMUE6ftg-sC6wucs1bk2TrL9Y-32GqiMVwVNuFXR7l5itSZPpTPhvazfnFh0oVrQa0yEZgfX5BEnozpfTyuKQTVPDcGRLm0d9ckS16E1lYnSEbVB2PWSb3HliVpd996sZ-KEJH_bErDBVYTPtyR0ZdgsYhB92KSaJJY4uLXOL3Nh0CvKYdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شرکت بوئینگ با پیشی گرفتن از نورثروپ گرومن، برنده رقابت نیروی دریایی ایالات متحده برای پروژه F/A-XX شد؛ قراردادی به ارزش بیش از ۲۰ میلیارد دلار که به توسعه جنگنده نسل‌بعدی نیروی دریایی برای عملیات از روی ناوهای هواپیمابر اختصاص دارد.
انتظار می‌رود این هواپیما در دهه ۲۰۳۰ وارد خدمت شود و جایگزین جنگنده‌های F/A-18E/F سوپر هورنت و EA-18G گرولر گردد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/72538" target="_blank">📅 22:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72537">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">رئیس‌جمهور ترامپ درباره ایران:
ما تقریباً کنترل کامل تنگه هرمز را در اختیار داریم؛ البته باید بگویم کنترل کامل، اما هر از گاهی آن‌ها مین‌گذاری می‌کنند و اندکی در وضعیت اختلال ایجاد می‌کنند.
با این حال، ما عملاً کنترل کامل تنگه هرمز را در دست داریم.
در سه روز گذشته، حجم نفت عبوری از تنگه هرمز بیش از هر زمان دیگری در تاریخ این تنگه بوده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72537" target="_blank">📅 21:34 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72536">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درباره عراق: داریم با کله از آنجا بیرون می‌آییم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/72536" target="_blank">📅 21:26 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72535">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=uZjhwNqXR77HNOgP9MDisRz2cLHZIRXj9YRmOUQVimBjRmDaBcOOgWKQuNQgZ4xDJLa9f9Hvwjd9yIOt1yXft8GcM_dp7IQX5iantp41B885Jd3ev2rdQI_GXWDTTIalZBwPfnwlK2nbbCfiyU83tRFsVmzhUtWVynq82Dyf4psGDjZl1m6r3ZpKX6dugAZE-oBW1fweGBFWlF9YEhhwFl1ZMQXep2ntfAZDHuQ8l_Tkhk3NbTPUkSndvValMdbPLB5p-cGaFEx0zGp5zKMd2HdzewDxmoML-KEqSTkrIi3jUedco3rhsikORJxZQaam84catX7ugx-fcyk1C2vd5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/88278c6cad.mp4?token=uZjhwNqXR77HNOgP9MDisRz2cLHZIRXj9YRmOUQVimBjRmDaBcOOgWKQuNQgZ4xDJLa9f9Hvwjd9yIOt1yXft8GcM_dp7IQX5iantp41B885Jd3ev2rdQI_GXWDTTIalZBwPfnwlK2nbbCfiyU83tRFsVmzhUtWVynq82Dyf4psGDjZl1m6r3ZpKX6dugAZE-oBW1fweGBFWlF9YEhhwFl1ZMQXep2ntfAZDHuQ8l_Tkhk3NbTPUkSndvValMdbPLB5p-cGaFEx0zGp5zKMd2HdzewDxmoML-KEqSTkrIi3jUedco3rhsikORJxZQaam84catX7ugx-fcyk1C2vd5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فووری
؛ترامپ درباره ایران:
خیلی زود شاهد وقوع اتفاقاتی خواهید بود.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/72535" target="_blank">📅 21:24 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72534">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مَردی پنج ساله به بایدن فش می‌ده که چرا از افغانستان کشیده بیرون، الان خودش تمام نیروی نظامی آمریکا رو بعد ۲۳ سال از عراق خارج کرد
#hjAly</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/72534" target="_blank">📅 21:23 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72533">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsaOh2cuFmo3SkXrLhCB98Z9MwUw13VzSjLamBHp94B4NuOeP6gtf7OPErDxnY3Crh5sH9SKrLnpV6o7e7l_jxnDwh49zCc2sx6FOMRX3jZZ9XOVYd398g9ZHP58JUAONR7MmzrfLUT0tzC5tcQJmc_ACJ43Hz_MNmzPtcTvEFGi25ZoiyGJcdUA6QeyJE9VNjWwS_BavHKjVZYWesnAhUh43oZqFy6KRGtLZpjSs97KAKFr8cxw829RYVBOC_0Dqml31jgIfZtJKeKbl2GE_kx06bgxc_8UNLFuTC-AgzEpJMCWCpTyORc8g2vafCIJiyAvcg9mWZYvxZrPO0N1HnFE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5af74dbf4d.mp4?token=pkrqloHLrLNpnnT_XJ37RmbE8mg79o6tUX82DX5Su32YPygQAczQOUmnXX_-3Ej8E7JhFWC2my3mcEr4orHkvtfeawrML8JRr3Cl9E4iizjmAqUJRNd0Tyxg8XFU_rgpkRL7kTf0Sm7SYcS9xWmcpwg4XjENHCxSksuWpake9bQv0CgKvazV-i69XJKeOKTTcLBXqh2IsanPt9Hk6zDTHqttKx6ByKrEc-VcyzrzkF-9mOyL8NjDOWgv7KsnoWa6FF6A3I2nzIdX8PrHqNKRRIKH1P39Lq7QY30YiuUpn5TcABaZacfleiFHUxllNCyrx1R_0XkOYu0CoOByR68CsaOh2cuFmo3SkXrLhCB98Z9MwUw13VzSjLamBHp94B4NuOeP6gtf7OPErDxnY3Crh5sH9SKrLnpV6o7e7l_jxnDwh49zCc2sx6FOMRX3jZZ9XOVYd398g9ZHP58JUAONR7MmzrfLUT0tzC5tcQJmc_ACJ43Hz_MNmzPtcTvEFGi25ZoiyGJcdUA6QeyJE9VNjWwS_BavHKjVZYWesnAhUh43oZqFy6KRGtLZpjSs97KAKFr8cxw829RYVBOC_0Dqml31jgIfZtJKeKbl2GE_kx06bgxc_8UNLFuTC-AgzEpJMCWCpTyORc8g2vafCIJiyAvcg9mWZYvxZrPO0N1HnFE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛
اندی برنهام نخست وزیر بریتانیا:
شواهد محکمی وجود دارد که نشان می‌دهد ایران در وقایع آخر هفته در پایگاه نیروی هوایی سلطنتی «فِیرفورد» (RAF Fairford) نقش داشته است.
در زمان مناسب توضیحات بیشتری ارائه خواهیم داد، اما می‌توانیم این باور خود را تأیید کنیم که ایران در این ماجرا نقش داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/72533" target="_blank">📅 20:50 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72532">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">#فوری
؛کانال ۱۴:
بنیامین نتانیاهو نخست‌وزیر اسرائیل طی ساعات آینده با ترامپ تلفنی صحبت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/72532" target="_blank">📅 20:11 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72531">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e30841564f.mp4?token=sdsBBTyh0vjO6fi_BWJbpkuJWD3AkKEaNv83hFYUTqM0JAWaky_c4X7C0bP_Kq5TsJhroVRzDCeULCH-Fa7d_dvGCtMk1NzlZNimBUkFn7LaIzCwEke7TQkzFGSA9vccrTC5RJ5kCjB0JOgDmhJWZYnvCpTeEMS4l4XTPZuaTYVsC_OhLy_0YHBMr9Bz8q6qHZDNQtPHsEfpsG8YDnPaPrQ9845E-fH-juSPK6DDaGHoTkUfXQRJZoI6BD8sAZz7dPr9yvU3LB3xxBaNm0nR7m9QwgM_7T3-fXCb3SOUhVM9dhaCeJ88KkoL95kxuMjIXm2SxyI5yLw29HwBpMbpEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e30841564f.mp4?token=sdsBBTyh0vjO6fi_BWJbpkuJWD3AkKEaNv83hFYUTqM0JAWaky_c4X7C0bP_Kq5TsJhroVRzDCeULCH-Fa7d_dvGCtMk1NzlZNimBUkFn7LaIzCwEke7TQkzFGSA9vccrTC5RJ5kCjB0JOgDmhJWZYnvCpTeEMS4l4XTPZuaTYVsC_OhLy_0YHBMr9Bz8q6qHZDNQtPHsEfpsG8YDnPaPrQ9845E-fH-juSPK6DDaGHoTkUfXQRJZoI6BD8sAZz7dPr9yvU3LB3xxBaNm0nR7m9QwgM_7T3-fXCb3SOUhVM9dhaCeJ88KkoL95kxuMjIXm2SxyI5yLw29HwBpMbpEDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آشیانه‌های مرکز پشتیبانی لجستیکی شهید اثری‌نژاد نیروی دریایی سپاه پاسداران در شیراز، پس از عملیات خشم حماسی:
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/72531" target="_blank">📅 19:33 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72529">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ENvLBwUmr45CL30ao0I_Nh6UF_jTJwiuIIRpR1V3p3f0JR0eLKFsJT6pMKFmuD0og3a6cNdbmN2kNo6GOm43nc9RdXB2lh9Aj549xUD2wsQiNVtJ5NZgIyLGm9GOrALiARoIOAlnv95pzP0lDoV7y34VAinPK1TwupnMSiO6RV9Lcik69PfXqyBtuRQpPI5bKTT2y2pYNE4GbvuKz0Dj50kwEkojbwRZMIULTWdFaqYRq2ikUIDrIvkWuBwxrnXng6SrGWp7NY9ziPMXHgCNw92h5aXDxqSN4ZT-L4JZI5-6QbfB537RIkLU2AQXYGLGDe3t3i9fwetr-7uMY8Go5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OGvUozn3ZkiSn2WQ6EirUpH6VJwhc5z25N3ShyPgKJQMd-hXrLvlK_75YirlQvNpZ0WCAf9lLepbXieDHjPP_TadXbIivSmgyzCWE-UVjv9iF5ffpqd1mEV7uCKQd5qHSLfSWtArho6KGgPkzrrMG8drMmrdEyd1q0LOjCDWn7ZPtdvu8KbP_SUPNA00kwa8vjRsqdOH6uYNpr1WzEajLUpLjuTLQWc5Uzv07HmLJ-_eNvP2iPhTMm2mXkbdC4UxtUvsoPKA4KEkPb6E8M1IQl0wBQSSvQ3aNl8A0dbb_MwHLw0f0OvojohUD6rg9Z2zhVX4mfEuF4DH_y4qnbiiBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پرتاب موشک از استان فارس
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72529" target="_blank">📅 18:55 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72528">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">نتانیاهو درباره حادثه پرواز دبی:
«یکی از خلبانان، خلبان دیگر را با چاقو مجروح کرد و ظاهراً تلاش داشت هواپیما را به همراه سرنشینانش سرنگون کند.
هواپیما وارد حالت چرخش شد و شروع به سقوط کرد. یک مسافر اسرائیلی و یکی از اعضای خدمه وارد کابین خلبان شدند و خلبان مهاجم را خنثی کردند.
یکی دیگر از اعضای خدمه پرواز نیز موفق شد هواپیما را به حالت پایدار بازگرداند و از وقوع یک فاجعه بزرگ جلوگیری شد.
خلبان مهاجم هم‌اکنون توسط مقامات سعودی مورد بازجویی قرار دارد.
به دستگاه‌های امنیتی دستور داده‌ام برای مقابله با تهدیدهای احتمالی دیگر آماده باشند.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/news_hut/72528" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72527">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/72527" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/72527" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72526">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BylYqxjRv8pqp-5mVaOJ4vJZoas1_Cl9VVSJddOFt5dxxwVOJaAe2z2inbl5zedtMqexImTbq33iVitSDEpEH1zR_0o07ZYYnNVlnh1Ma5uk3rO7n-e9B64FOk-iJ3v0jHBsRljZrlBNVi6dRj4bFClWmAsodRrrRDHwZN756ucaVuFXC9wFyYuOqLoj6nwIflJLKKqFFiYxztuEPWLhC6M0VWBYcPU44SVlZbk6oNpYWlecKBsgGLAu4XJ4T8l7O-aIbvQtYzN7cQbIa0bxg5GOImdoVfvZlQo3Zr3yovPuPAHkRXfijbyiu-hRe9WculOduyC7xdLFkkm6xBMoaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
همین الان وارد سایت شو و شرایط آسان‌ش رو مطالعه کن!
💰
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72526" target="_blank">📅 18:31 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72525">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=sPVBMi3fRv_NAzA6FUHfPNTu5SC9j5TQ-zuRAzV1kIyEtEkxqvH0kRu_0kNzimH6pUpHfkDycL8nYDyIKnvcY6heJnNrxab_W2TKJnB0bkFCC3Ps0wSs9_8f4oG8E6dEPuCfdOHhIIjpG_Aj_GU9ywwWLCRA8Dn0Y6GHH0spvnF00oN7KG0l4yjMgK5RltdnAHhm7Hqs3Un6tgv2LnCM_f0MCgHnwMee_CaPMcNjdH030YkQs59JsK7VQXEbaakNrftNj7Gs3O2C0alj1FpRe7E441jn3OA02JoLxitGT4d3LaX1jHyMWNmrVkfw7GtgfvHLsAvlQQWL6cpwd_iQEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fbae6ebe2.mp4?token=sPVBMi3fRv_NAzA6FUHfPNTu5SC9j5TQ-zuRAzV1kIyEtEkxqvH0kRu_0kNzimH6pUpHfkDycL8nYDyIKnvcY6heJnNrxab_W2TKJnB0bkFCC3Ps0wSs9_8f4oG8E6dEPuCfdOHhIIjpG_Aj_GU9ywwWLCRA8Dn0Y6GHH0spvnF00oN7KG0l4yjMgK5RltdnAHhm7Hqs3Un6tgv2LnCM_f0MCgHnwMee_CaPMcNjdH030YkQs59JsK7VQXEbaakNrftNj7Gs3O2C0alj1FpRe7E441jn3OA02JoLxitGT4d3LaX1jHyMWNmrVkfw7GtgfvHLsAvlQQWL6cpwd_iQEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏عاقبت لایی کشیدن در نهایت همینه؛
ممکنه چند بار تو رانندگی از روی دست فرمون خوبتون موانع رو رد کنین، ولی بالاخره یه روزی میرسه که ممکنه یه همچین صحنه‌ای برات رقم بخوره...
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/72525" target="_blank">📅 18:15 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72524">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=RbpAqCEFSkzpqZlhNmwTu_Rm8lwTB2e_IqX5GtRiPfvFJUxxreMyaeOw6GQDauWu6bNty45PKidmcvRVZrPtLXK4kvKXAvzH1yE5GYuKjsV-JovlaWpd5wqB7a-V7r__r8eiswMB0cDKEcw4tkfy1s5iL61Iw2PhOLg0J3o-J1NYntaSnSRZ2SUwHbQl_5snxDsJe1bH2KmXcnJF966TGDMP3bvq-PeykwM7AzQMMU9lLXsmi8LotjSsivzVGko5L0SVnC_4e8K11oExDenyySuFihXKvzqobssy2Mh_93nyW8Wbd9UZrHHqR4rh-FLW5CfrLJ9nBfPbOjAEypGD9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8caf88eae.mp4?token=RbpAqCEFSkzpqZlhNmwTu_Rm8lwTB2e_IqX5GtRiPfvFJUxxreMyaeOw6GQDauWu6bNty45PKidmcvRVZrPtLXK4kvKXAvzH1yE5GYuKjsV-JovlaWpd5wqB7a-V7r__r8eiswMB0cDKEcw4tkfy1s5iL61Iw2PhOLg0J3o-J1NYntaSnSRZ2SUwHbQl_5snxDsJe1bH2KmXcnJF966TGDMP3bvq-PeykwM7AzQMMU9lLXsmi8LotjSsivzVGko5L0SVnC_4e8K11oExDenyySuFihXKvzqobssy2Mh_93nyW8Wbd9UZrHHqR4rh-FLW5CfrLJ9nBfPbOjAEypGD9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرزیدنت ترامپ بعد از دیدن این کلیپ تمام ناوگان های دریایی شو جمع کرد و دستور داد همه برگردن امریکا
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/72524" target="_blank">📅 17:29 · 08 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72523">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=aad6NDgA1nfi-Oicjc_u9X-66eqBip_XmXAbygHepCJKOX2n1QHfLLFc6Py-Pjq-4aUNQhpCH3QnwVs_-tX2VVBqE2Pz6Lbzr2Ol5nAN6i-z0NulopacpEQPdKXpigEL6zJKhFGQC_HXNeticyQgw_G_RpXfFvGE_slPbDFR1UGgxKVHgP9TdRkIv-QqKRYuiFxpYH4deUlJ2UQZ5oUX6DeAQlKCiG_VPl5rJI-3BijE83O8h0kSUvHwC5swkZC474bpWFIlzIH81QSgb2QIC_xCQjvuKjpVCndT7OG8jHq9UN0_3yVH4_c6bKytf033Y7i_4gIb0umPvPSFYTPDPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f862c5d3f.mp4?token=aad6NDgA1nfi-Oicjc_u9X-66eqBip_XmXAbygHepCJKOX2n1QHfLLFc6Py-Pjq-4aUNQhpCH3QnwVs_-tX2VVBqE2Pz6Lbzr2Ol5nAN6i-z0NulopacpEQPdKXpigEL6zJKhFGQC_HXNeticyQgw_G_RpXfFvGE_slPbDFR1UGgxKVHgP9TdRkIv-QqKRYuiFxpYH4deUlJ2UQZ5oUX6DeAQlKCiG_VPl5rJI-3BijE83O8h0kSUvHwC5swkZC474bpWFIlzIH81QSgb2QIC_xCQjvuKjpVCndT7OG8jHq9UN0_3yVH4_c6bKytf033Y7i_4gIb0umPvPSFYTPDPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یه پسر بچه دهه نودی با اجرای رپ خیابونی، این شکلی کلی مخ زد و از دخترا شماره گرفت و بوسش کردن.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/72523" target="_blank">📅 16:40 · 08 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
