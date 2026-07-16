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
<img src="https://cdn4.telesco.pe/file/t__wUD5960hfXh1yJzC1VboECe33bVVc130ScU6CzuLMnVPSJ1z8_IElWBps-Ya-jwkz3N-gF55iFyySrQSHJFl4XnWK8TUP-4TV9B1FXWUozqNLN0UW1BiXlXh5PvDY5i5FzPrCUgGUkInFiGcjmwSpJAMMfu5mkyOl3ixhfmbnYSOQxh77fdbFeexTdvgRUGl-n94PUl_BwykOCNRB1jqTfl7Po8aY7OU6oXwjej0mMqQdliB4KoojOuPbKyuq9gSEQM0kJd76mINUPOWVbehrU3VzpVl3nqFsi43_t1IPketbQsb3eea_J0a-UjZT_avp9lx1MddaDI4GNRWb-A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 479K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-25 09:44:46</div>
<hr>

<div class="tg-post" id="msg-25828">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BvfK6r1j7kp5OrV-WT5-nGNaMHzlDuVqUr4BOVH0Tn9EYDd2lkeCdVXJuQXz9gZ0mNd7cEar0uK96W8rxUVCdE5sgYScQPBBYGAkJ9L9u5eJqockFzVGs2t2ZeXZtU4LVjdwJCk91thWbzAd-foSrXm2vcW7YrLzAn8_fE2RKSMSl_mjs30u6tUUYf_sZ5xDfik7IJWplX8nGaBdJpY6DI4PzldMsMXf0xHll3hXJ34Hub2f8Krty2Y1BsNH1YEWdVyGyJQ9xW1CSpS2EM9JYQXY5aJQvP9uciODJSMX2wz-RolSthNYk3iFcFOu9oRbQ7CMxO_7fAY_bdWYjm1WLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jnTUtD4xtpohC7B3_oip3WA9uMaGENyVVIxjTaef5bQ9hm3Sc8R60KLWbDkWLe8_a1A3AHX_0_Y6rDBzfpOVLb5sCOQwVtKleP7kDj8H2eBCt7R15Tb6do1sfb1tcZ-PDI1CZA4NJRS4nU0yEIdl728D43siUhE7z0JNnEQ9LlqywbBsR7XhHg-MHL3DR3p-8tnUIXOUpQJD2J-F5CCs-GKHjZah0Ppry-dpOCtv4c9_kVYuzbwppUwkg2ZjJ-AIw_eGlmlhmIcVZ_bYU1PCh8IB6geeoxatuw7hCkHBMvF5ujUabfqfO-C2yEbVOaobDpvUA3N0XNyZBxInGngp0w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">📊
رده‌بندی برترین گلزنان و پاسورها رقابت‌ها پس‌از پایان مرحله نیمه‌نهایی‌جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 2.43K · <a href="https://t.me/persiana_Soccer/25828" target="_blank">📅 09:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25827">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvCD8qDAeopqRDw6C3vEdY_WK-w5KHw63vbXt8J_g7OTAWAQtckeeOYVj-N3sFAMC64iaXwO1bS__CNGtWQUTTbW1b0wRffrrpKUikxYR8waTHQ8tS6zabkFt8u68MXSicMTQkvLIq4a987MUnVwmm1tdBTZwsjxBlCCXi2_AmnvZ3z6dgmSLnKVS-C-tIO0xZplDAG-6xmx2Xn1HGQsUxeJS2hYktIY0-tfQOZH8lfFSTROlHmCuufuoT6pUyOYCKjTDpQ4Rdrgm_SJd0ZEr7rnKwL3AwY8pVn14qLL6v3znXCQs26X65k3a3lHUVCpAMNsjnsuFXjxHnOqDFGMDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇦🇷
هری کین:
باحذف‌ما من دوست دارم لیونل مسی برای دومین بار قهرمان جام جهانی بشه. من طرفدارش هستم اون سزاوار قهرمانی دوم هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/persiana_Soccer/25827" target="_blank">📅 09:20 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25826">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7c3766c7.mp4?token=YHn1vkZiXT16AZLlpB9jU9z8bGZHHoSwo9_DEvoQaHWtfovlrsPYasQ8gQU_FbACY3TOuFPOlBer22SfA2CDHTpcIR6qrcLmKPD0pv_X4v3wvtx7kAtPk8GyZCsvynxFk-x85QeZUdWL4X8WC4yZ2zMWX9Xn5PbJWPh0jHQHiNYwB85JRbYtZR_Z2dAh8Bp0RrQ2ibG3YHrLaZL74dbLHHeNuTHM3WEv_iuncaOQCT6o00T4be1mQ0KLkzIp9hTZ572JEp86_O-hm6aIBAatSTBfHHDDmTh57RXiU8OKr4Tk48EJIyxHOSfy2p_Kj3s19z_ApLI0plvx1m_OlOHgVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌عادل‌فردوسی‌پور درباره‌قاضی دیدار فینال جام جهانی: شانس علیرضا فغانی بیشتر شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/persiana_Soccer/25826" target="_blank">📅 09:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25825">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nl7yIoSIFVxt7bRdLSt2_wfDcjHE50AiBiqrduLpwfh2jTQGQLNFLfHVcj6oOnsDMQjuRpVsru00WkXRQOue0UWli0mPRuePsUCyK9mdevFrhUPf20KILLN5cH0y8KspkHx0HionXjXj12heDDqvDeuGV-mDg09klreecnKgHnEMcZWlYtbUp3m4RhB3OVsNHmN-sc4uzxHVhbrbNyak6homBNvk_uIdpJRn_1I0mRWp92j-rVqOnf-jOBHWOevgbG5znmPKPTKmLza7efCFNp8a_PJBT2Mo2gHKJDEK69dpdqXA28k6eSo4AkV2j1KvWwAh-z_9AIQcuOnumB9o-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
#فکت؛ تو تاریخ بنویسین، مسی 39 ساله، پرایم هالند، امباپه، کین و بلینگهام رو گذاشت تو جیبش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/25825" target="_blank">📅 02:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25824">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiZZcVtczkCjPLF7wgdNyVFnMYgzv-vbsHjKU_G2pfMTxJOtdI2cWeuYDSQV5CVlICy9OS2duw0PqfPnPpct0b3SyShMhQ6uZVvl1X3LCSvka4ltWR-k3wsNZdfkZfo4zufWVqK2MyvxYsTjckRzhbe008uabGZ4Y8W_wGfMedspg4gJ6mM8znCyguqfFpmHUxebpvH9vR7lOHt16DLK-Af7ndemBd71nrH1q7ONYug71CxIJC8mahsG9MwalLa2neiGTEiAmPmsphAakjpt8-dxaImy-fmwUxrybCZyqxIQlq2XQwl1fqDm7_i0WG6uZxusSx4xjJfuL-nYuyWdBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه ‌تنها دیدار‌ دیروز؛
کامبک دیوانه‌ وار آلبی‌ سلسته مقابل انگلیس بادبل‌پاس‌گل لیونل مسی؛ جام جهانی 2026هم به‌آخرش رسید. روز یکشنبه 22:30 فینال و قبلشم بازی رده بندی. بعدش یکم استراحت و آغاز داغ رقابت های باشگاهی در فصل جدید.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25824" target="_blank">📅 01:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25823">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/29e18a8789.mp4?token=lYeZkKmeX4jzAE6OiDhSElINAJENgkXtl0b9APuvbvRb7NrWufXPFk05UvQrKVdoV3w3flzrdXUhl82pU0wuDKUcRk2Qr9vmce6Kp-EiqxnYu-OcKJAbLu85CZRvLAyz4asz1rKUJPSwIypwVkpkko_O7WLPCyPXuXVcjZpiOUGJRqw-c3T_u7_jh7_ccZbEtlMjYN_cWcDDO6Ue12JNWZtG39lrfCj4z-uh41qHG6k50Xgul1kjXz5DuDF71fu3uE46OZeNtmSQtmVtHBYH80RKHfYEWd1DxmORqtUO-BpvJlYTk1d_C2l326ryMOOjorUk5w3WzzJTr504RZahDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
واکنش‌برگ‌ریزون‌اسکالونی‌سرمربی آرژانتین به گل پیروزی‌بخش این‌تیم مقابل انگلیس رو ببینید؛ چقدر تو خوبی مرد؛ مگه میشه تا این حد خونسرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/25823" target="_blank">📅 01:40 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25822">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🏆
تصویرجالبی‌که ESPN با عنوان " لیونل مسی و بادیگاردهایش" از بازی امشب با انگلیس منتشر کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/persiana_Soccer/25822" target="_blank">📅 01:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25821">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QLrcfHAIJE9i6_dTJ8pU1QiIGR5dBaM2wjsQI70Z3QWfTdsBbojuVhUy_Ab3ycyQW_TSjFKUGlhOIq5K7YTUVF44-jHy33GTj7cPI-A5FL9u7-jkEm7N0s9ITDOoz4Sk5AFhPHwqjF69osqH4bC2amPhk9_K6SW84CaQ-Bs-W1CNZC2ZcKj5eRBX6NjWXvWvP9Qx08EQZmKuICBhmij9bMFwJ-8JvlrrdUXB07sR1M7AF3STd54qdCiC8qOgHx2XoncK1q1eVn6VqU8jDY9a7I-6XJr_aTxi2kgvamWWLUJ7S802s2Nx5h0jV-zy324wFKdoc9xRF92Vwd3sHDXvag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/persiana_Soccer/25821" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25820">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/efd102a0a9.mp4?token=LaaVBJki3vC3xGxCur_sB_YqvAfahrj9Rg0oXOZklCecg0SIUGchnWg33ao4LjdvXxAJx43U7z8QBa8kMkXMyFvV44r0vHicnPTK8CdbCFUsNmbuNqR4S2RSJWDhxDuGf3nDMRs_DNQRuPOWufY0Qh7iWSrAL5kQu8ySkpkiCIFbyMCT8tZ3pztN0Z62SjsaYfQblpenqlxyVS5fzLJ312lY2Lxbo1Bad8k-i9_R8nRvn3DIkyvTR3IBadueBPKnv0lrLiksW1iAaYbtH1tADjzJtsyIFprGO2As50tBavZt4gc4xh7AutHfKETD3PhNgdc_BX3O1LTIOZ9UL_MGPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
سرخیو اگوئرو که امشب بازی دو از نزدیک دید گفته اگه آرژانتین‌قهرمان‌بشه به هرکدوم از بازیکنان این تیم یه گوسی آیفون 17 پرومکس هدیه میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/persiana_Soccer/25820" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25819">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Hj14qodLy0kYEqy2XBeZRnFtikMvYmoVNfQ-CgZXH9vgrbOdC6JX_8g3bDO4uLI9GX2bSiRGvyCbdUiVlY7RheRkYaWYce8pZmGvKskXarP5dPRCWISzbkD9LRaGWZr1BoJVtH6MHx3lW89SaVu2gnYwmBtsJKNk8TN2YZqr3iEIm7v3FzVgnjP0CgWZ7U8fnb31jaOfjjQ244GFyKlyXOkbvscA5Ii5CZgRfGe6ug8yvITVPO8-h8EkLL_HhkILWefYGUM7l85qNQYgVwi3VGjK0vuhP4s3sw5QiRu-ZBR2F-ttHrfC4Z4IOQVp2hI-4VXgXYADU0RL1Z52aRjYxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی‌بالای ۲ میلیون‌سود کرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/persiana_Soccer/25819" target="_blank">📅 01:28 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25818">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CmYJ6fiq_ccNo6ABk7L_Z2u-uJ0o2vpGlF43vplJkrmSP35c74BKqrlKjqq4MtzRuZCaDH2DCYTDVROuD10n4FA_Q889hanbeltrs2lV91iGAqvwqLfZJDWUQwRepXhlZZvHpU0g4iKgm4upbi4tcjLp9caGoZA-quhOdts9SpXs1z_7XhgNNJtZxkzgVPwZGx0NMBqb1-deoP3WkMnVzdQDWgYEUrMw5O6issSi9TPykYwN0OpmkuJytTxmIjMzBlCNijaB0UKtM-obnBwzilLdforuejy_jjVn33xdIcceSRlDATKpAEdBQKLj50Y_RatQ3jUWaPhFiiCpTt64_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
انگلیس‌دقیقه۵۵جلو افتاد و توخل درجا تیمشو تا منتها الیه باسن‌جردن‌‌پیکفورد عقب کشید و ۶تا مدافع گذاشت تو زمین‌چون میخواست تاخودسوت پایان تو محوطه خودش دفاع کنه. تمام این باخت گردن خود توخله. حتی اینکه بعد از عقب افتادن هم میخواستن سانتر کنن هم تقصیر خودشه…</div>
<div class="tg-footer">👁️ 41.7K · <a href="https://t.me/persiana_Soccer/25818" target="_blank">📅 01:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25816">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1FPKZem2D_GqdXjMSEUjAC0k-1NLaVITW7SYVNi8z1JPmd9VnxLPXJHrXRgM5_-krdCqrDQk6g8T907hAFHWyNuJ_ZJjwOw_zw-R_u43P04fvrSDo8pGGSHJ6aQZzitGKInAcmVb-cKwnaWC0W7MAGI1cc0XKRTkSUQl2-kT5NnQ2ee5icMU-gOB67l-CZMDvTTW-x1OnuTGkpym_2ihHI4-I1fvAonMWO3-8pVTpnr6KMTMcmk1ISurhMENHxeoAcTOeOaL77-fM5L5nxSmqCSWqM2JSDyI8cZ6pJCilZRKt_y_I_yf29zHCa51tN-Lh3jO8FROpMnYiWWOItSTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
بهترین‌بازیکن‌جهان؛ اون‌حتی از جام جهانی ۲۰۲۲ قطر هم‌قویتره. لیونل‌ مسی همچنان به نوشتن تاریخ فوتبال ادامه میده. عملکردش رو ببینبد فقط.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/persiana_Soccer/25816" target="_blank">📅 01:08 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25815">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OeP39BCQ9PziENzDbszGIpTEwcVJX-Vg_YKvvTop1Cw4saLAGZUEPRzCiy45BXRpnPsfV4YVF_3Kw97j7ZvrXoMuGZzFFrVL_SMasPbIlDyBcP9_CkmExorirNbSVfybtyNjZ-vKj0l1mgGy2wgkYcCP_pGCNxTRC0kpL147sdjTMogpPb8kOtDSBtPY4rF0vmzA6zjpT0yBegR1I2l6oy_KL9VmTvqE08tzI3021dHH3weByJisSWlK45zUvmGT7x0b52IAHmvAkkasg9X_CJRH_bTGRkMqtLyjtBwBAN4cijVgRdhDKke3444IJBE5L7CKVe5J_G7R1X_2x-UtZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/25815" target="_blank">📅 01:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25813">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PcEFqQhZ0DllI0yiTumTYgOkTUiCeXYtkbix7Z78b8x-eYXkesKG9tXZWD-1AYtQ2jfHpfK1wpj3mw0zqvW7hlsto4Qy4D3zMzdK5CA-vzgZB6xcreujEM2pOAxzf_fKgUl0vesQZnvAngOyNWg-vVaOte6zdnrnKim8KplGN5A-mIDxrvzDoOTOh3d6I5ll7saXcEjufqYOLPQ8UhXpwY6UIr1U2sWvlIBn5-SWZ2ylS90GX2B66MBxZwMmi3ZR0TvHmjjL3QoCRfEriM8cJXq9p5696-wn-CLyofKqmrY-YFSiUGjXAnhmtZ_Wyhz6xS8v_8DwwVXk6lP9vbK5Lw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/25813" target="_blank">📅 00:53 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25812">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MsnydyTGNgktuQxkJT71dQZy8p6wpvuRo4y4zSLaVQlyyQmUj-lHyR6K_DbcMuNg5_nt_8wDQdRh7JL-DAn4y6eFqbYt1_2-p2lVXXeAz2JJEQxjM-kK-xAkkOmIzXCfupLqLytlCqArNB26M0BdUu2ooUZJRbwYWk17CkpjJmSmxsSAlfvofuLQKYWyzYiQVklw9tRJ5J_-6VLqUDtlN3fMUQMM07cX-RnGlioN6fzSgpHi88UdQ-WD9PlkssLaaHUkEl7clf_HOlDAe_7qtfVCOCvArKG001aAB-fU0q-zAjfAKC59UppbP8X5G60emkvoA5IfAn0p1YBnXr0wBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
فینال‌جام‌جهانی2026؛ روز یکشنبه بین دو تیم ملی اسپانیا
🆚
آرژانتین برگزارخواهدشد. امیدوارم قاضی این دیدارحساس علیرضا فغانی عزیز باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/25812" target="_blank">📅 00:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25811">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VOCYWebnztwqiXGijjhcwocz_s9UUNfysrJuw89OiLiztK7wDN0_33SMA_MzRaOcx5ApA1wGl3D2GCNvRQpdxW_3_cUvIAFNryUGQH6UwRIroVpDmAMABA9PYWRDDZmWVHxtyFVQ9QXwbapHSD0iQMKSMkrINbvBNibanUV4qEgldZCMwV_UtApiG_uOMMFvXg4nErV3biLinxbsCrWNsLMCmk6178lJD9puLacQ2UffAeHNdJVhii2sbc7sYBhv_lfIyPqsa2FpBK1QyYuP1Y4Wji5PjzFOx6_nqPMhTzJnQHF-7BQT_BOOVRuIPTa4g04k_5Ry0i23sNkbaWHwig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25811" target="_blank">📅 00:47 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25810">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lf5WluhlqDQyN3MxbTm6rl7L-HLX8NDbWsrxJTSrtmwuk4vuY-_ymfEE28tCHTfGcExAfm0O247rBnS5xOU2gK6vtH-kqN5Vg7X5AGOR9mRL4HzlvQJVLGULYRcGK8zzvwbDAG71RsvJj3EXd7RTf7vtUjGzVmeb2oTEXOH1LO_iutg_rAyFKVPCz8oGvueZrGe5AuTyNVRFrvMOiMxGV7y6gI4K0njNFj64JySlR7ZWhxDXb4LMj7EaRmSiOfx8cOuo5E4pcnU1qx6BTWrV0gzj_sdk-7EnHo4A8bL2G6C9J3oozbZmsMuM5Svh1lqHpRN7uZNU3AXMaRybhKZ4gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25810" target="_blank">📅 00:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25809">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AZZaIPU2bizYWIGbHu56bqYygynfYgJhPKevcgg-gYWLdekVT_kS8zdYG3Y3gt-shLvalyD6djtIsiL0dynGuPeAhJp1-l51Qt14GKdBRd80DOJ9s1YN0PdtTGAybUSBo45BPgUbDRdRxZyePudO3_0lRnpwo0WPGg_2lyZwoGqRF2ftfoMaggOJeVSKz7muNyr2CWavlLLXo09Kdd2AFypFCzEpe0Dd5a1R6kh9w0HEHDwN_T3OMu-5UhfZpe7M7XQkDLKgthBDwvrxmg-nAAKbo_rK85uAB8ILzuF8rqQu3UBx5mgILZWRB_ZzxVpysPMxc66ZfAsBFv3Rbjn-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی 39 ساله با دریافت نمره فوق العاده 8.9 بعنوان بهترین بازیکن زمین انتخاب شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/25809" target="_blank">📅 00:38 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25808">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ovZy_yrznIlZvq2ncejJtQtc33ctt8ch3zSMZf0hiCn-duWoGpERp2JhptA4WZ3LDTKB3uPMre5yfIy3k9izsUbIGXF_0Rxj7uzDBH2ByCStFQPyzeSnKAYTpKgV1gArTTGgMRg6oDhl95ZIjyCh-44pVEBzNlG4jRi9SP-0MbSZBw41BJCPh7p5QmbBNKoppZ3UvqpGRkJHmLiv6POt_XHXpei41plLiEp5qfcxE_A8Lq_Ldi-Acy6-Jf9e1kEbZ_T-XmXSS7ZlU7e1VFpHi2WkDfkfnUfP8Ymw3Gky-9gfgQnMv3a-l40mC7juXDfpSS641vELy5g-xBxPk345Pg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه‌نهایی‌جام‌جهانی؛ صعودتاریخی و دراماتیک یاران لیونل مسی به فینال‌جام‌جهانی بابرتری سخت و نفسگیر مقابل سه شیرها با طعم کامبک.
🇦🇷
آرژانتین
2️⃣
-
1️⃣
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/25808" target="_blank">📅 00:36 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25807">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oj0Wa3xfTQSBBpeA4cKcP1zkwzxSbWaBxh0nDd1kW3qAJKAMjnqjxFfqidLzN0dKc_rvhxBFJhsURhUYjjGyO4FwgwPlyRchufNwCfpJKb-z8zsxXFiAKIQMxiy2NclZRv25VxoFvkic89RwH02wSsEyUvY_Vh9rIPZJh1dRtisdX79gDvmFH6-gcuAbr0FFAi9S9vHDuLjUuBHlhjOnOC-YMtED7Qd-XuAKGmcG0qRxZQLjYVUswV2a3o7LpffA9Cj58k_Q3FqcnmqUQVOMkmJxZTAOeNeg79qQpGO04oaofiReE5qIh-Cz3bFDx1f-hM3KRXI9SUDDoLYyGfgV9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
گل دوم آرژانتین به انگلیس توسط لائوتارو مارتینز روی سانتر فوق‌العاده دیدنی لیونل مسی؛ این یازدهمین پاس‌گل لئو مسی در تاریخ جام جهانی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25807" target="_blank">📅 00:33 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25806">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d89d4e5750.mp4?token=AK5MefpCNRmrwJV6cxBsWVKOpaEl6PQkHmhl7mQJLqURUs33xBSlnKUigyhIG3Zz5VjPZcPrOtFZmbPmJbNoagLmu5WgZAyrblIT5Wz_3KuDrKRylZwUaRtEJ_amFl0z4ZHQFmRRpANQ5x2-hlfyzJ7UCx7F813O5Q-itguOLPuwa9YVeTxZpXsiyXs4pQIvyziR1fX2RROuhkTymG3Yh4UP0SjQ9sbWNM9HU3dIcDq7VmkALyZynVzJDxjFR7RE97VRTYHbmK30-NGjdEe_DVF5HUk4Ur832u81Kih2rOp-vP6naAmLC7obHp_y825s7s4bKlnWrvvjXJYyWV_tng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🤩
انزو فرناندز ستاره آینده رئال مادرید با این شلیک دیدنی مانع حذف آرژانتین از جام جهانی شد؛ دقایقی قبل هم گل دوم رو به انگلیسی‌ها زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/25806" target="_blank">📅 00:27 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25805">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c0c717972.mp4?token=fsaddars4hUrHUiqz2RRNOyv8SPPXo7blEj_geXikWXfhduTCvvEA9Hwzs4pySSTB1PWs6sdfB_TFi-hafqdhT_Qu7yWcsVYipRjfrnzXNVOsOc8H5BRNuwtTPQK0uw5v51VP9z5JUbL2rsj8CAyufdEfHIYZXClZ-Jn4UvZ9FifpMh04jeavHGIX5qQgtLaFo7vTjxETkS40O5AgBLaEPM6QYN8b59unee2x0cFCYWfSqtbQaTBYQhOqmV5oSQuoKyBEEOeVLrr0QOwayC3ifaQAWGFVPZYCgzyM44WhxL1xJHwYLbhrKsx5x_Fz_rquH63HxzsJP9mqHmyJHTFoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/25805" target="_blank">📅 00:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25803">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4db22288ce.mp4?token=nBXRtdhQpMLsmfJR3CfPniXzOSEuuez1-xcGea2pNkFMVp6Er0sgsVFM9NWRjlTtxqE9wWIs6thcI2zohbie10MCuaBv9VIYpFEE4zcMmQA2T_UMb6v0nyk6SjNLPcb6U1GW-8CdcHBZHqSqxShtuzbRIBWSbWdL7b42iHUdQkqHsr1-f1E8nU9EJ6GplXi1g8sTxnInKuRyzjxErFVicVA_BGOLuCSGdA_-BhAYIyPCTUkvpT6qCEPYIpEXLwZ5ZaylSxyBIstkcNV6QDauEO3bYR4hlW5a4IB2CaDVwgvoYX5nKlRqeAuAYGCFcyNF9_jiWwE_nvNKefa8gM-T0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بیرانوند: چرابعضی‌رسانه‌هااومدن‌گفتن مصاحبه‌ های مورینیو درباره من فیکه؟ اصلا فیک باشه وقتی می‌بینی همون‌مصاحبه فیک داره به من روحیه میده چرا توهم نمیای همون مصاحبه فیک رو پخش کنی؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25803" target="_blank">📅 00:00 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25802">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PT8h4aFFdK3Z47n2XQfUpMECbe0nr183DdSplMxP03_SlZqDr6hAKyVCpWl5KqhMnmV7ehr7I11y-EEf8hiMCtJTyvQ5--nOMF1a3NwKOmD1evkZB7RjxiK34rsVqeUbww4MJlsQA_BFsiyvG6ucNbyip_NHrOYZOCFMRdFq0p6Oh9umUBX1DC5r5BGkfC2BvuKCVqnkn0Bhj77JMA9kzI6SHX88BIqTm4T74Ppg3MdTYPFcPuJ10av7rV8MM5-H6uKabO7GwVcDG8WAkXKYONX6Asdh5KxMknlt1tzFc4KMuntZu1UFLoBMg9Mr3eEd_8J9UwLBWGgM-SRYbq_kXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برخلاف اخبار منتشره توسط برخی کانال‌ها؛ درترانسفر مارکت رامین رضاییان همچنان بازیکن تیم استقلال بشمار می‌آید اما همانطور که بالاتر گفتیم دو پیشنهاد داره که درصورت توافق با هرکدوم از باشگاه ها؛ با پرداخت تنها 200 هزار دلار به باشگاه استقلال قراردادش رو فسخ…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25802" target="_blank">📅 23:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25801">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_KXzD6S5R7cXqVGhNgop8WXrMjeCg-dFPGnnCOSFGXEyb7RHeFC44vw49sRrqj4UvVxB82ZLXKHzyScm8jMvVW3VmBIIMhzOlSHhG40n6c0TRMWsID__SHkLDIncD_vVOvd0qY4J-eTCh4_KFk1ZCIJ7mgjUbqn401j77J6hTO1YR-QEKZWVAoWjwSqruJBp-T2qpASbJsN-49ctQbXMtDQPayJ_QLxNx20kOmGTdaqeTTRCPEiNmkkzv-S_74evebnBfo7nBIs4N3FIdDuRlarBKfwzQVlXZgmRPnpYqo7-ENs2hPEkjdevbD_2w6jlmmNhU3ZJbuLe-v4ZBGqdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛ باشگاه پرسپولیس با مهدی زاری مدافع‌میانی سابق گلگهر به توافق‌شخصی‌رسیده‌است و این بازیکن‌موافقت خود را برای‌پیوستن‌به پرسپولیس اعلام‌کرده و تنها توافق و پرداخت مبلغ‌رضایت‌نامه به باشگاه اخمت گروژنی باقی مونده که انتظار میرود ظرف…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25801" target="_blank">📅 23:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25800">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q8axSPAWzmwnKQsPI8bjgwlz7mRCIBI8h1AahwzB4TgQqMFA0J7X0HPlefynVvM0MO7Dp4AG1S24QZnNT1chsIwk0zmm4OKGOZWWINraGp7lO22A32TjO9qfIOoNGr3tckeaS3uG__bBYw_hYpn_SIqzI9TL2zS6BPc1S27pCMKLYIKeVw2sRme9zyu5Qib8ICh9F-DPVjobFAo3vA-zNxf04aQqSajM_DaJVrtD6E3B-3T1Or08t1mDILhAkX2ZC36i79OTz5wT2b3OVEfaNoNSAgYjEj-3SSqTgzseQPffPCr0uh8a-k_mcS1z0BPoeJ5fMolOQqJfs8OoYZOmOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ باشگاه اخمت گروژنی روسیه رقم‌رضایت‌نامه محمد مهدی زارع مدافع 22 ساله‌خود را 1.5 میلیون دلار تعیین کرده‌است. باشگاه پرسپولیس‌نیم‌نگاهی به جذب او دارد. مهدی‌تارتار شخصا با زارع صحبت‌کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/25800" target="_blank">📅 23:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25799">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=ap0dSN4sjfDiBdXNprhX9400RQvbDej8nJfS2sVcBHs_WpqBEsQmbGEjQCi6VS1R2vmjuERGlUVJ8NpxC0ZbK3H2W2bg9QRQ-ZLXZJxWyuAh8SAaA9Vgb-gg8tHQN0IZ3XTueuYgV1Eio4yQJA2Lk4BBoYfCBOU6FnyM8knoyeeX8ynVcr0zoOzDUK5lDxLeCxLbF2JZhomoOPJntQ14BPx4W37fj2MWj9PYxFtUcUWdYY9fIEUdB-5ZFbBISlzve2tEixVxtzOo5t7ohWmnKCAblHXzOSmtplUquKxesLo-elSffMPK7VKe_hRePguZzrBi79Jmvu41Ks7OrY76Vg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30d2d3139d.mp4?token=ap0dSN4sjfDiBdXNprhX9400RQvbDej8nJfS2sVcBHs_WpqBEsQmbGEjQCi6VS1R2vmjuERGlUVJ8NpxC0ZbK3H2W2bg9QRQ-ZLXZJxWyuAh8SAaA9Vgb-gg8tHQN0IZ3XTueuYgV1Eio4yQJA2Lk4BBoYfCBOU6FnyM8knoyeeX8ynVcr0zoOzDUK5lDxLeCxLbF2JZhomoOPJntQ14BPx4W37fj2MWj9PYxFtUcUWdYY9fIEUdB-5ZFbBISlzve2tEixVxtzOo5t7ohWmnKCAblHXzOSmtplUquKxesLo-elSffMPK7VKe_hRePguZzrBi79Jmvu41Ks7OrY76Vg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیکه‌های سنگین کریم باقری: مسئولین سرشون شلوغه. علیرضا بیرانوند خودش یه مجسمه از قلعه نویی درست کنه بزاره خونشون لذت ببره. علی آقا دایی هم میگه نگو بیرانوند؛ بگو دکتر بیرانوند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/25799" target="_blank">📅 22:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25798">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h_yKkza6KYFUfJ1rYTlitJQbmASfdIkQo509TR7drT48e45x-DjibM38TsbW1nX989xXOwLMEhOFWJ2yy5g8bfoqCIKtiN2-MqteOquVC_-FHkNfj8Bnj4oGjp_7fEoDXuO4jrUfxPBLg2WiU0sjjnYes75ejmRhkHt8RjhrXjs_l7zlBzyBPrpBSnQlVRzItiRVtaJSAWgM2fqbMqiGDFrzchJjh3myGTzwlUouTJBjJKi7b1GqHUP9uqgOJc5yfIQWM5q1oSAzL-KOGc8S8g2vLq492ZFKhWfeXF0ZG7rCyTXcetmJSrYZC19xLFGk-6HVSKvSsxB2wGPtEMkQdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
معرفی زیبای عادل خان فردوسی پور از مهمون‌های ویژه‌ برنامه‌ امشب؛ علی دایی: تیم ملی ما وقتی‌حذف‌شد که سردار رو خط زدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25798" target="_blank">📅 22:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25797">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c436909609.mp4?token=nDZXWMK_XfCJhBA3byhQUy2NVnBU2qvM5QqwtiAwt6p-raq4dvidtURD5U1-0nusvqtfWBIvYvpdGRx8Gm0R7F3wne8WbojTt5aXYKxvwZ-jI6mjwGVDTy5qMCiia_c5nirF_MIJO0tcDJeEHqrCmSEOqI6jzyNk-UZO6pCDnOzSKv8FMZvUOFuHRFs2kHOBfLxb8FZ-Qxz1mkCsq8mo_Fz0-HmcEW56Pz6QCFcGGqL86HIxuU7AH7rOQUvBIAvqUAJdbezUQcS_Vjx43cCCFf8__WwYIhOhfx5MYBbQTr_WkrP9p_a1_b3HPXgUIUifGO0XsYMUqGp-oOVhA0f-Fw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c436909609.mp4?token=nDZXWMK_XfCJhBA3byhQUy2NVnBU2qvM5QqwtiAwt6p-raq4dvidtURD5U1-0nusvqtfWBIvYvpdGRx8Gm0R7F3wne8WbojTt5aXYKxvwZ-jI6mjwGVDTy5qMCiia_c5nirF_MIJO0tcDJeEHqrCmSEOqI6jzyNk-UZO6pCDnOzSKv8FMZvUOFuHRFs2kHOBfLxb8FZ-Qxz1mkCsq8mo_Fz0-HmcEW56Pz6QCFcGGqL86HIxuU7AH7rOQUvBIAvqUAJdbezUQcS_Vjx43cCCFf8__WwYIhOhfx5MYBbQTr_WkrP9p_a1_b3HPXgUIUifGO0XsYMUqGp-oOVhA0f-Fw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
طبق دستور علیرضا بیرانوند مجسمه امیر قلعه نویی درمیدون‌ازادی‌ساخته‌شد. بیرو دیشب گفت هر مربی دیگه‌ای بجزقلعه‌نویی این نتایج درخشان "سه مساوی در ضعیف‌ترین گروه ممکن" رو گرفته بود تا حالا مجسمه اش در میدون آزادی زده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25797" target="_blank">📅 22:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25796">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sa00jUY2DWQgW25WwPrAKTKOjl4Ga6_qU50DUuuLwBCcV0dG_c9M2h5aD3f8gmZRNPc3V_IjN68uTkbVnZHRJKRhFu0NV3OcQ_vqF1tlZiYKpZwIIKBRIO4X0oHyGguR7eiy7mifDklww9hp7-co6fUIBwra-rUYOYAhUVpm5rMIJUjWGVjAF-b1txwxqup57NcmrbX5D_iLtDozZ_XviHxRi465-rb3eLMMoJLgErkRkWJrjRXA-jHoUQJZhYo5nNgKgPZR3DtpshZT5fGJZrXUwZlvnyFjlnWR5QJjPs1LGSPcriIOUWmCrg9duLuL-hVwAXCDSzdV3KKnKZp8mA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هفته اینده هلدینگ خلیج فارس؛ تغییراتی مدیریتی گسترده‌ای درباشگاه استقلال ایجاد میکنه و بچه بالاخره از هیات مدیره رفتنی میشه. شخصی که تاثیر زیادی در جدایی ستاره‌های این تیم داشت.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25796" target="_blank">📅 22:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25794">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=OTk9ujVZbFos07okRfz3YeLaGgp7mZpO5qFf3Ag0evd1ilkC5el52H36cdIjDixOSAQRgSkuzhZJcFyv3syrsgnJdN2cuEHyAO-qSr3ZQc0fHDP5PjkZJSTJaQ6FdXaHKnbu1z8eo84LNyes3rjQvUDkK_tUNiyv2uvPX7gc9cy7mAHVZzHP9LuKmCOR10gN8h6cJa4f3YRot0SHbXPPkzVsTBlesIPDX6kzJZX5LOF40fOF4BvQYchnfrzldfSJtBx6XavsFUcqPG8o6jWPUk3aYfrdaNaxu7bwYVvabtlR68tVpx5I-gBU1DhtEkhiX_51SMAAjlWHOYwAoSQkBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/113eaa3d5a.mp4?token=OTk9ujVZbFos07okRfz3YeLaGgp7mZpO5qFf3Ag0evd1ilkC5el52H36cdIjDixOSAQRgSkuzhZJcFyv3syrsgnJdN2cuEHyAO-qSr3ZQc0fHDP5PjkZJSTJaQ6FdXaHKnbu1z8eo84LNyes3rjQvUDkK_tUNiyv2uvPX7gc9cy7mAHVZzHP9LuKmCOR10gN8h6cJa4f3YRot0SHbXPPkzVsTBlesIPDX6kzJZX5LOF40fOF4BvQYchnfrzldfSJtBx6XavsFUcqPG8o6jWPUk3aYfrdaNaxu7bwYVvabtlR68tVpx5I-gBU1DhtEkhiX_51SMAAjlWHOYwAoSQkBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
قابی بسیار زیبا از سه مرد شریف و عزیز ایران در آستانه دیدار امشب دو تیم آرژانتین
🆚
انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25794" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25793">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=v-_USIpqd8E5W7yXVR7uCzWjIt0w8XExtlQCzpue5UxWsJzyGxGYWvuCe95EN7z15JjPU_kpv1nSAFcNFRREAL9DmT3I2aL17i6I64IDICW7GW3pe3WJiLTNWF3kpoFLSS6lbncMZSO_p_GGc3NoOiYY35ku-j_cOxStRz6OqLV3QIOSMN-wzc2znvaiK9MpJhoXFtIhuWP-60yQFLukZawfQfXX_GZvzfYRGF5wJ0CkPMAsyn6b2rRpQwMxaBPASESNxtMgALs-JThTMGf-IVUHzaujFD3-Ud3MIL_RlCOF1f9czEFrEBN9bZ3AHTt3H0Ldbh22fovs7Ok7G3bHZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/558fc696a6.mp4?token=v-_USIpqd8E5W7yXVR7uCzWjIt0w8XExtlQCzpue5UxWsJzyGxGYWvuCe95EN7z15JjPU_kpv1nSAFcNFRREAL9DmT3I2aL17i6I64IDICW7GW3pe3WJiLTNWF3kpoFLSS6lbncMZSO_p_GGc3NoOiYY35ku-j_cOxStRz6OqLV3QIOSMN-wzc2znvaiK9MpJhoXFtIhuWP-60yQFLukZawfQfXX_GZvzfYRGF5wJ0CkPMAsyn6b2rRpQwMxaBPASESNxtMgALs-JThTMGf-IVUHzaujFD3-Ud3MIL_RlCOF1f9czEFrEBN9bZ3AHTt3H0Ldbh22fovs7Ok7G3bHZDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
#فکت؛ ‏بیژن مرتضوی تو فینال‌جام‌جهانی حضور داره، اولیسه و امباپه نه؛ تعز من تشا و تذل من تشا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25793" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25792">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZO3059CRPQbd_qR8E97chrsuMWQv3lqbuVCVH11WBtJ785RKc0XkewHUw3j5P0ERxCXrsCWwKgfcJpCgEzQTGLMHuCKvl5sEQogP71Jyj1M7gptO_EXcqVqM-MzGo2hUQPUKM_SREzRIIB7_SkCl0d1p5QCKOB499ubN6Ypt7fDHbF2jZdqDEZuYQWXFNDKSrQ8ulC9PIMEsjl6xeCZWzg_fqil_rPDizLh3BTPcUoWgSL81ZALKFbIqYsoiA0nYF9tC0m1dDwCTM3F5yFMKGYbauNplRcRPcLH2RuFQsowGoGwW9BXfjIY8z4Wpnc17jJCTKEb83nLEbDHOHBgVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
🇬🇦
#فکت؛ با دبل‌دربازی‌امشب مارسی؛ پیر امریک‌ اوبامیانگ برکورد 400 گل‌زده در دوران حرفه ای خود رسید. امار فوق‌العاده اوبامیانگ در این فصل درمارسی: 18 مسابقه، 10 گل زده و 8 پاس گل.  گرینوود هم که در منچستر سرنخواستنش دعوا بود آمار خیره‌کننده داشته: 15 بازی،…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25792" target="_blank">📅 21:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25790">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AdMrvmEaYK2u-mfWZ8sVhHF17GEVzFwhab2Pikr6enEIVkiehjEpwIBGEPJjuaqvtiBEc6CZn0qWp6gN3bksfRI_0eGXdOyHcVc8Q4_Lk03_9JwFic2XKZD2ffqZoytRs483m21dfFdLYr3OvWIWsmht8jxSc7rLRjW4CUeKt_PSlW6gscm6rl1KhXrlqG5FOA59CW2oxZScIvp_IIhTqjT5Wx2269D2R67gOXnZ3RK_OuAjclgLocQVRcwIEl00dA7_fiAprgpd9AO9H1mdevjfXUmUrrUBHVlsBSdt_f6z_zEwZ1gobZ6wC3g1Ipd_ckd2Ue5YqefftasZ91VXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vbs5eg8nACGdW41MjMN8dC1iuwV5KIJPu7NAJfwiIuu9ckX8E5DaHTzESQDpmEInphA7oFBsP4dzfevc5VQkHy-jn60Cu-zPiS5udmDRb_zCuiL-mtNvMOLBQVluQau2bGMuXpIcgWKddOSeiwS8uEvcQ8x7-HiItUU4xhiSbbLWYYVY_27l8Lh1Qg3eSAi_y80X1WuD5Nzq9450e8H6OX_IngkJDgaiQgJAx5Vo1VKbyR9z2GcxKdJ-ITMPJPY0xoVUkgQ1By3KDOcL9lYEnIrbBoucr3wIp_VpWQlQa2zZvs9hX16FeaX06QMoWwSXI5YHXvxsxQgdxX2aPqRsWg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام‌ جهانی
؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
آرژانتین؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25790" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25789">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfDS0RzRGzh8Lmy1DS3toHUwRDOiHCrCGznoFw-1hR91Vy_ak5ILyV_pxG16914T6eAk_WJjmPn8COeISChkQh2j5cOVyCvda-_UcgGgZwyxCfPfXjFsZ-_RY9El9ZI5NkpjBuI6MYJhWZO2T6Du-d_RDmTxLaYCnZOhYCw4AAc02ef0YWj6chY-52XiFSZlCLvMvMhsh7d4lur04dQ7eCT36qkdPx61xMudeKYwGfZZrRQ5zxoxrUN98Rr9WnWNXve3WsdJGLPVn0iAqmJaM_AusYUtD_NnVS0DByEoSUaqX_iS91EhAydO2Pjm4gKGFVOhNZOQBT8JKxyM-SwzTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25789" target="_blank">📅 20:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25788">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MO0a4XCLz5vc6B8G1nDJMdAXLFnCrtSnArIdjTfPw0Ov8iYUgUuTl2brTRkOHJNkUz3lfv6XSgkrq-vAMI9kYHYMMk5OR3aFPZK4ggbTWbKLDGPBLDiKnL13FZ4gdGSc9MwG0iWXV-4pvqyAsk0PvkWXIRZLTJXw6AkymvlwT2QA6YRMTEMHhGG9fPCJFX2hoormUap09TONaWWbW3V68nyo8k4zeJ2dT1VED-GCC3ONrZHOdnZgrFpcCQr429OtAX2J8DvlV5DGKajnJUGZiyl-TSbHQGoC5qdUfAdTy6w7Ub5ZfBzn8xRBhcPRHVYE_P090fwbVoz8rqDVDJwfFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لئو مسی در نیمه‌نهایی‌های جام جهانی:
دو بازی، یک‌گل،یک‌پاس‌گل،یک‌برد، یک تساوی؛ هر بار که‌ مسی به‌نیمه‌نهایی‌جام‌جهانی رسیده موفق‌شده راهی فینال شود؛ این اتفاق تاکنون دو بار براش رخ داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25788" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25787">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=uPtWE5U6Ke1-EN9xCIj_USHEQVvp2xuZiz4nBM2l8n1Y3AcKZO2UcTVtcoUgUQ9fGyb7fJ6SBnJGB1znefIcJ-EJGMH2Ybg1DvuIBStO7g_-ARUah5hkFWSUcHv7pFcUD93Fl06K6Kw5zT3T8YsnjZkajn5aRaNjPUUCC8CMAwadFemcN1o161lda4-gNCLUkZCr53el-IXRC9S-GAMgwrJ8k4WlrfZGgZvcTI3aMQ0E-hWzl0CIdpRlNe5Op5y63Cg0w_IfGA5oqtJCEy2Fp9jslAUhjtfpsBhaAjrdZX0vnJrGDwyNPFBS2VmtKzXN6MsOltq4oOyCQPz77oDxbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b4c95cb5f.mp4?token=uPtWE5U6Ke1-EN9xCIj_USHEQVvp2xuZiz4nBM2l8n1Y3AcKZO2UcTVtcoUgUQ9fGyb7fJ6SBnJGB1znefIcJ-EJGMH2Ybg1DvuIBStO7g_-ARUah5hkFWSUcHv7pFcUD93Fl06K6Kw5zT3T8YsnjZkajn5aRaNjPUUCC8CMAwadFemcN1o161lda4-gNCLUkZCr53el-IXRC9S-GAMgwrJ8k4WlrfZGgZvcTI3aMQ0E-hWzl0CIdpRlNe5Op5y63Cg0w_IfGA5oqtJCEy2Fp9jslAUhjtfpsBhaAjrdZX0vnJrGDwyNPFBS2VmtKzXN6MsOltq4oOyCQPz77oDxbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇭🇷
چالش ترند این روز های اینستاگرام این بار با آنا ماریا مارکوویچ ستاره تیم‌ملی‌کرواسی با خواهرش.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25787" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25786">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUlyPH0vikn6qCqGaBXzpRV-fhDum0zMho9exIZqd69V1F0v4HStvETVxZ_11ReX7tdhLVaSFnVjdBbCbO7-DJKlbIp8Jtzufp6Cg65jftrXNM2ApwUqUfsPkD2gGMcWJRo28XBKxVa-LbKcJ_HxoztJFWVlGqMD1nfqlEpY2oiyzh_XUKAcQ-FUI6utXDph3wdQe5GGL8iMDa-vlA6LM2UEA10KfVXV6b9Qi400wKKhJSD6TZ4w3Jz6vlbr8kVUbn_oBsHaXDNEwBIA3uBjvvUIeb57dDsBt6SP5feKx4hiXGDIk57Unmb97c-aeBoqgF1-qaJNQSSUmcB7ANb_Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
— آرژانتین
🇦🇷
🚨
۵۰۰ دلار جایزه + ۱ گیگ اینترنت یک‌ماهه برای همه پیش‌بینی‌های صحیح
نتیجه بازی را تا قبل از شروع مسابقه ثبت کن.
🏆
مبلغ ۵۰۰ دلار بین برندگان تقسیم می‌شود.
📶
هر برنده یک گیگ اینترنت یک‌ماهه هم دریافت می‌کند.
🎁
جوایز به‌صورت
FreeBet
پرداخت می‌شود.
👇
ثبت پیش‌بینی:
https://t.me/betegram_bot?start=p8_r4EF37DCE</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/persiana_Soccer/25786" target="_blank">📅 20:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25785">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIGI2oaUpPBrAxhrAbVQlFWN6vpq3P6lGl_WVcy1qIe9kTdhvhuAl8RbIIOXjGXWToJSZ0P35oF1z7k-5NzDrgOLOdtn5F_QEDdmGQLfWdV8GysXhRAlw8Hq2buysCIX06VDaAA5Hp2L3a6KJJIE7DaJlO3JwFleH5XLFbhGxLBS17JzwOBjOhssDMNr-dvjA6rsMIbJ_Zhi03YHY2uM2J3reeKwF1N5hMN_oeJP6OEBgGLKa84-3GWKFde9IxWutblUs_k4rkU5ehUtW-7rs2693HoGp2KI1M6q7MUCncp3p8iw7BEC5bEXZ7ruxf2IYVXSCp8P7eJmnAcaTBjeQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی‌دایی‌ و کریم‌ باقری دوتااز اسطوره‌های بزرگ فوتبال ایران مهمون ویژه‌برنامه امشب عادل هستند. ویدیو کامل برنامه رو در پایان این گفتگو میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25785" target="_blank">📅 20:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25784">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d3tljTi6CFlDkiMZizfTVz2jYcQc1xsrzAly1EyarW6gaGKaD_bJAl5xOPBpRZgCejOCgUSKUKarUqv3rD3NeEQj6pKFKpTwa-EZev8sUiLWH71yutg0lyaUujgaxTT6Mk3YPYPEbfLpOQqRO6nqhX1_6molSiFuw_vqg9ri5n9cfBC5rSoVYhzeeiX4GyLp_r9dXymSQqiu7FIBMSBHZAfT__lLbe7MbgUFUn-udhgIw9TRFP-oVi5rdKJuTI7nTZxEW0TwGcsnwKeaF-AoMU0a50ZC1bc2biCi3vKt1SoKYjBRYPiWAbwpHONd5zhCI3wY5Or6e3HpHg3rohK5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرویس برگ‌ریزون بازیکن جوان تیم ملی والیبال در بازی امروز مقابل تیم ملی اوکراین؛ خودشم فهمید خرابکاری کرده زد زیرخنده؛ اشکال نداره این همشون 17 18 سالشونه جوونن. اونیکه تو 33 سالگی و اوج فوتبالش مفت پنالتی خراب میکنه اون درد داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25784" target="_blank">📅 20:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25783">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AfdVXaoHYw8a3f4SvaeIfB02avHR3AHuCEdkpZQVjCvWFAQWMYl7DkE3gukXxT8FTYMQogAYLUHXilyGINWbRJaMHo4Ms9YHSoNwNX3XD5ZU7huqhPgrcvIKffKKcTj4NQbnyYlZFbSahz3exaCayOCvRWPLza8KczYc2ADLg7ESFv7l6LL1coz96H6SIeYqzMK2-gIQ9Uh2IfFUQ1u1AS9L5Vf4wAMFxIHyCn2_UtTchfvRUA0Bh8i7q7YtQt3a4djQn1P4vySW-vt12V__vE6pqEpXcaB5hp9HAiazKrMuMwTRZ0WKDlH5OUMan4wKySfN3JzhuQ44ETfqNjgGPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
واکنش جالب ابوطالب به انتخاب بیژن مرتضوی بعنوان خواننده بین دو نیمه بازی فینال جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25783" target="_blank">📅 20:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25782">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=SU3GM6RP1HAKvBEuYoAPPkMHklaJ5z-bbXet3MVEjlBc7o7VtCXxvDCn8IiaGkqHPMXXE7erm_bN7tISQ-repZVvOpkryYd0ez0TYIwD1oF48rt2mEKFGq2uYxWZLMKt-6wvzukA7kQxUoOkwt3ZE0GtwQd4e0TwsgNUyumn1DDq7-yXKa8lhY20hpHXLaqJpaB--zbxBuhPexh2T-1KwcPE_u41ge_lM7ucofeU4n8lG5agb9U5SFujGuOZ6iVpIT7YwqP7JdFfD5s43vA-cQ94NVHrOAHD-ilDWFpShlvZnQ1CzL7xZ6nz_n3xccuUy-PGTSkPoY3K1tv1z36qMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87ed733fb0.mp4?token=SU3GM6RP1HAKvBEuYoAPPkMHklaJ5z-bbXet3MVEjlBc7o7VtCXxvDCn8IiaGkqHPMXXE7erm_bN7tISQ-repZVvOpkryYd0ez0TYIwD1oF48rt2mEKFGq2uYxWZLMKt-6wvzukA7kQxUoOkwt3ZE0GtwQd4e0TwsgNUyumn1DDq7-yXKa8lhY20hpHXLaqJpaB--zbxBuhPexh2T-1KwcPE_u41ge_lM7ucofeU4n8lG5agb9U5SFujGuOZ6iVpIT7YwqP7JdFfD5s43vA-cQ94NVHrOAHD-ilDWFpShlvZnQ1CzL7xZ6nz_n3xccuUy-PGTSkPoY3K1tv1z36qMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برنامه بازی‌های تیم‌ملی‌والیبال+جدول رده بندی لیگ ملت‌های والیبال قبل از شروع هفته سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25782" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25781">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=e38boZs32_q_LldFitgk3zEXQndSZqhF8jGogQ9Oo_gz9fmBfo-siw7S5dAJOYZfgk_wZULciNYSmAHvaBrGUXbkwoF33PeG5Ae7fppq_miUjOSl4L-xYge9R5wMl9dzH-BInWsZ3WotvnBUJipSd3Ep9VzxWHDlP-QAETi-FMp3VHpLLXynn0ntDOVHqOhqBadtY7t45cI-I9s1UuNT9ZjfThNrHGLy2UvsQeff44sMLMZB23Bi_HDriBSXPS7kkBxxgKfwDI-GCSGBq8KSc-69jkVKqVnLLSUHg0bNNfBPM0sa1doU2LcTc_cfOPwIxqlre8mQnsFkOXJdgKkjmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a5e427ee9.mp4?token=e38boZs32_q_LldFitgk3zEXQndSZqhF8jGogQ9Oo_gz9fmBfo-siw7S5dAJOYZfgk_wZULciNYSmAHvaBrGUXbkwoF33PeG5Ae7fppq_miUjOSl4L-xYge9R5wMl9dzH-BInWsZ3WotvnBUJipSd3Ep9VzxWHDlP-QAETi-FMp3VHpLLXynn0ntDOVHqOhqBadtY7t45cI-I9s1UuNT9ZjfThNrHGLy2UvsQeff44sMLMZB23Bi_HDriBSXPS7kkBxxgKfwDI-GCSGBq8KSc-69jkVKqVnLLSUHg0bNNfBPM0sa1doU2LcTc_cfOPwIxqlre8mQnsFkOXJdgKkjmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ویدیوزیبا از حضوراسطوره‌های تاریخ اسپانیا در حاشیه دیدار شب گذشته دوتیم اسپانیا
🆚
فرانسه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25781" target="_blank">📅 19:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25780">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=kjU0dfbucV3e_1vMVh1F6q37Bxss4CWgwKOV0CwEaKWSndJp1q7XMl09q9XKyFq3qyREUrGPBYcUvhccdgM6fIJWyWtvC6SMYgJnqigCIUxP43ZhWm_owA9FoiPONxT5IfotOxCHxXBWov2iIZ3UGOVpRMRPJBvhkoRZAXmvzTDvHA6j3qbciw6UcS6aPcQVicFXVJODwVaa2gs0ahowxfViJSyV_LMfY5uIqP7OYgTx3AP5AWgvDt3PQXd5J8CkTxpfjOF4R6cZEj4sH_knRLwo59xkj4_TDfSkC5cYUMOfMMKBE-xHFIqn6DJyM0Z1XROsjFzsLB41ZZfdlp5NCw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f78ae3e4c.mp4?token=kjU0dfbucV3e_1vMVh1F6q37Bxss4CWgwKOV0CwEaKWSndJp1q7XMl09q9XKyFq3qyREUrGPBYcUvhccdgM6fIJWyWtvC6SMYgJnqigCIUxP43ZhWm_owA9FoiPONxT5IfotOxCHxXBWov2iIZ3UGOVpRMRPJBvhkoRZAXmvzTDvHA6j3qbciw6UcS6aPcQVicFXVJODwVaa2gs0ahowxfViJSyV_LMfY5uIqP7OYgTx3AP5AWgvDt3PQXd5J8CkTxpfjOF4R6cZEj4sH_knRLwo59xkj4_TDfSkC5cYUMOfMMKBE-xHFIqn6DJyM0Z1XROsjFzsLB41ZZfdlp5NCw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇹
#نوستالژی
؛ یک زمانی میلان تیم نبود مجموعه از سوپر استارهایی بود که همه جام ها رو میبردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25780" target="_blank">📅 19:24 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25778">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gI4baPDaX6PcpXMoA7wLm3__3K9HsaIItuqMc_2zJvjI5cMFnAKRPqtVKOrFgZO3T6uZ5cEoSMjvx3OvV2IBjGMFJDA-a7Jlm7YVUxRBcI-4AIOwRaTH-_yMzbNnbczT9xcV8dSMxpL0iaNQX_sJo2hcGmeDJqN2fbaBVjuVKo8NIqBE7VgaPCFpGusyyBnwMCIAoXYHwv_oaTOlB806RkVsMjT1EjkMffoWRsiKJkbC3Rnb2wKIIEqgzhGGWmny_S_FeYqFg0hozZoj4PC0YVMA27vRP-bOfcqX205FVhLvfqZUkRarlVJfdXqXGJWdChHOwsTIH49E1Pf8889hyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kQU2J8hU_7-DKwqm-2DP4GDbbvNjYsPHQeujrRg6M8ocRpXKwJyeQmBvnyiElauIHRiq8GA5lkrd6yFVRXAEI9OIuzSeqIkyS_y8V3kd8pasRqxjsturehF3AnW3-KwlKEr9WuksBpGLmL8gXhhPhhOcyIe7VE-inkiOsFmTgl7-c5KgzbJno3p9ndwjSM55P5GyEqHVd4EuMae4Ahb1B7cDYPEZN9caMhRh_GRUEFH2Qr6PQmUHOjJeYeU5bkEumViXKcOk9wUBJVQAnivCBYTDBHmo_xXf2xfpAqRWJPfjNjqB3vSJrs84jz30uhn_1UbhSWVWEVodgec2K3sUzw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔵
👤
مدل موهای جدید مهدی قایدی ستاره ملی پوش النصر امارات؛ اماراتی‌ها رقم فروش ستاره ایرانی‌اش را 3 میلیون‌دلار اعلام کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25778" target="_blank">📅 19:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25777">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lw7sSTGhzwSlCW3ZI-p2F93RPDHpBIAuohbDsX8qtwpif_-b6spL0DLAbaNsHDeXzIlVUoflE9UyyNasVPYDUX8BMGyISTAX5U8pqh9Swhp8wuixTYyM3v73yd14pu4vNRZJX6j4CpMpl9vCVYbM-7sRVgH16qvZ-pkwE1HJS4WXie05I-zLyeCihtRdwdTu8vygHXdXIHfmNH8c-l5x59TUMueDHJ_gdK9LRYCz4wRvZHiKgI_5StglH1E1-KrBzL0ceEAv5nq9LM0PET_VyDrHyq40QbQfjYsC6pJNbeGy9Rc0j0I6FGv229iwyDtiM98pIis0NJdB5UHyNmZWgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛ جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25777" target="_blank">📅 19:02 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25776">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBhWVF_sOP6WvpkDawc0j3RcdOAScshyXLhJo7MZVSChTdzIvMiN-BiU0F5TXNG1cp86Jl9HzpTs9Ltne4QMQG_DWG7wpjtODbwn03fOX3ySHPAcw1khKzstpungqFhh4Z6wuNe2hrEQgOdwX85rOXnZknOBrUpXi3BNv74CUxXqm4MG_UZ3K6IyoKbBgM2WL0Cejdac97ETzI2KgH5Bn5Nuq1pIoBJD7Kgf1onvj1tGsByIQmu0EbDzNPjNVGf-qvfGjTgTBdGz86RyiS2CZT3wv4o88amE_iFWtNsttiUzsPAsKGAxRgBScTfr4LUmngsJHjOoQ2FWeeph_khQ-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سانتی‌آئونا: باشگاه رئال مادرید اماده است هزینه بسیار هنگفتی برای جذب مایکل اولیسه بکنه. بایرنی‌ها به‌احتمال‌فراوان با 220 میلیون یورو موافقت خود را با فروس اولیسه خواهند کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25776" target="_blank">📅 18:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25775">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_p1WWZIPc2P_UywkryHyahoiNSLefUT525uC3pPHq9d-hpfYcNtaaOX2BjH7zZH36UBI2iLgVdcj3-jGMTT66sCuWakojsjGhKpGBE_UtZdSclftK9EcfQT31km8eG5XlyDRAtKAgPBf3fCpi9-IrR5iA9Mw4vFIMBlH2fEcOs09L8dnWfda4hnt1ohPdSC_yNb8tUSQdP4ErrRPn7ZETbgGpv8AjLU4xRi6l0K52qB7coRXcew7alQXoDJqQ6qsPtB7wtbK2kY10m-Lk1G7AeA9gWp9_CA6mAGsvo1AtiohbzB7tiaeIU82qU9Z_XZYcWgCSXedV15T83sWa6YDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🟡
👤
طبق‌‌اخبار دریافتی‌‌پرشیانا؛ احسان حاج‌ صفی قراردادش‌روبه‌مدت 1+1 فصل دیگر با سپاهان تمدید کرد و تا 38 سالگی در این تیم خواهد ماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25775" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25774">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O57qluLcnub7xAGzZEwaulPG6u8Q1f0_ykwHiGQfmwpsxCfMAZ0Pjbpbyt0lMDGwRvRf62cSjkSyDIqQB8M8Nlu4rngqwXQdYrN5oMKCz9PNia-bkTmloiYu7vCJEnylQMgtuZhtCtBOJB2CDgN31uutzf1T6oewd45Y0ynIf7fydJOD3RaSsfSXeEilprbW1o1SZz0yYH2ZhmE6HTLxZEYqNS897REAkwz_h4r71Ev63RKVoo0nWIr5eCcW-CSuTAH6KNfCuNO17RbJIh_k-QLGQexGhaULBKPQWrGkE8vYdXwl-wb3uH3NL5vpxDS3rxwCaBvBFarIMAUu9KxAfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#فوری؛ سانتی آئونا: مایکل اولیسه می‌خواد درهمین تابستان به رئال مادرید بره و این موضوع رو نماینده او به مدیران‌باشگاه بایرن مونیخ اطلاع داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25774" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25773">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Z5wZ8hW2dCxVVGkj0HqgjR9f6hGwVJmAAZvtsSS4KioyyIIQ22X3jzVMH010KoKS-V44OLHa4hk3syU16A0ilQCXoWXn6dAyFv93vqpUe99CZB8iLPQQ0ngTBlJtYr2dvXz5JeMtB8EBym1GWgkA3aK_-0_0qqDEnGkOAZBuJxIWsrmeoPO-MGG5dlIEH3diiNXHb-pfG7Jxk1_ZnvCiWMIQrhIwhw7WwBz7jTWc8jlQ-ffRRhQT7zeWibOCWw2g9yFqGwiWzPxhfGCyG6xMEIKRRY0AQBC1HQhm_iHoNXdUPpcWAFe9kWDrV65gbUngaEjz5pOCMB73NFxWT1uLqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
بازی فوووق جذاااااب
انگلیس
و
آرژانتین
رو با آپشن های تخصصی در
MelBe
t پیشبینی کنید!
💵
امکان شارژ
کارت بکارت
و
هات ووچر
🎁
قرعه کشی و آفر های جذاب با جوایز ویژه
🌐
دانلود مستقیم اپلیکیشن اندروید
🤝
اسپانسر رسمی جام جهانی
🇮🇷
پشتیبانی از زبان فارسی
✍️
حرفه‌ای، مطمئن و درکلاس‌جهانی پیشبینی کنید!
برای ورود بسایت‌فیلترشکن خود را خاموش کنید!
‌
🌐
Link
🔜
MelBet1.net
🌐
‌
Link
🔜
MelBet1.net</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25773" target="_blank">📅 18:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25772">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MxozYDQp_lSAzOdi_2GF4YKp1VqBaHsUIWQazZCsNmz_Govx4MILY75S4obxlOJmq3R0ndOB2zvkqDvuhifssZmVSXTxHrX6Qk4ijkFDnvsb794cbpqi-F551xvwqXIGZjm8wAA0LQlkl5unGFsUGiVQd9BHMg_3yNZX2vRJb0HTY2UWX6DVmhWULFCwGJnR-OO1rVEL0Zarj2aVkFCvJTQq5IFIsuXwHUb34n3qfIEAhZSnx-dHyB8YsyUV16gmHHtMehGg-u6Bm3iN1PsZBBMgcFnMLl6-wsdmpF6aAMtKrnYY7eiJ_ljSDGHem6mFvBIyazR0P3hTnI-VjWo_-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
فابریس هاوکینز: مایکل اولیسه پس از جام جهانی دربارهٔ آینده‌اش بابایرن‌مونیخ گفت‌وگو خواهد کرد. اگر آفری‌بالای ۲۰۰ میلیون یورو برای اولیسه ارائه شود ردکردن آن برای بایرنی‌ها سخت خواهد بود. پرز رویای حضور اولیسه در رئال مادرید را در سر دارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25772" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25771">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lc_NbmdrZs_45tRqnpIS5iCAhNmR-a-rjtJQSMJZJbQyFwKoyHndTUHQKMq2Fvy-CPXqVfsBMB8oBe3enb2FuPt5Hxd4LsPr6--zQ4Np4lnjHKOzHxMqo6dFXglLelRr6RKtrk_LoZ_EWtO8t0SLEfH4O2SW_adNIBMgur8KE90CiKaW7iyNBx4jMmYizXyESRUKfbV6lTESAHooD1ZA7WDZ8sL7aQlMXh-xIdyuBy-OSZ1MHFU_rnGny0wjybp6OrMAAQK2o08Ohm6zkzG_plcZP-EA6-hPrah-dxMoAlbDlGB-btJ6HwT3VBbpZ2sVui3ZA5e9g1rXxluKYvlbOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحالی استقلال پنجره‌اش بسته و دوفوق ستاره فصل قبل‌خود یعنی یاسرآسانی و منیر الحدادی رو از دست داد که فصل آینده نماینده ایران در لیگ نخبگان آسیا خواهد بود. کار بختیاری زاده سخت بود سخت تر هم شد. ممکنه حتی بختیاری زاده استعفا بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25771" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25770">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i-o8__RQtBPj2RkMCPi_7dblo7De8b7WOGZhwq5RjaCiiHI_8hS8SfNkkYeRZ8dX3N4fU4qHeP7nlMxC0GKuadZgw6KpjdN3osQ5vcqUUo9IZCyEPTaD783vihCJai4E2YyL5gh-Sidk1iPlGTjqEQQO0FIaUj9nLjsDASkn_hCDcx1jQbOCWeyZYPNMz4JVLSNzWMH95CVGwrVRN53N6GfAmsZW6eUwDe706iBzSDT3KrPt881v8JWjOuvQ37wruCtkTxxD7VMN7dkQfe8qJxo3STBcuwtTVyKIYvllZkgIhjKg7Kxx59YuICy8jgei_FxiJJ-sULhpNg03IHHHiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیشب‌بعداز بازی فرانسه و اسپانیا درنیمه نهایی جام جهانی؛ خونه یامال تو بارسلون مورد حمله قرار گرفته. دزدهاداشتن‌از دیوار بالا میرفتن که نیروهای امنیتی بارسلون متوجه‌شدن‌وجلو دزدی‌رو گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/25770" target="_blank">📅 17:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25769">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbBDvR6CkyfBh5RLSPmnlmDcBwRgflOQ_Q9tt1upLmRksO6ZcemVOtOP1ce69u2Z0l8D0vS2YqsZhPifuAVMJMHf_uz34L1w1tN1hJGwX8yk-e-j8AXSc1AtVDurEF7HutRLtaE_8OV1qPZiXm1vc5gJpVcEOkAY7SRkHpbv-daXkHcvFpcdLry7NT6d_aRjJBtllXfxOSqerd-1pWuyFHTNfiOVyqtU8znIkkbwA6evGyzfW6_O5suh5wtJceNqeTwCC-R5_XvCiB9DEfyh7M9jhL_3r0yHpmOxrym4E1AU6DrYDc4hfitMQU7N1W_VN_T05DmfF8__YFdM95Idiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری؛ بعد از باشگاه‌‌تراکتورتبریز؛مدیریت‌باشگاه‌ پرسپولیس نیز با ایجنت ایرانی یاسر آسانی ستاره سابق تیم استقلال تماس گرفته و از او خواسته که یاسر آسانی رو برای پیوستن به پرسپولیس راضی کند. حدادی به ایجنت آسانی اعلام کرده حاضره اون رقمی…</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/25769" target="_blank">📅 17:36 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25768">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q01ANzg-5leyi3RVxB--Mtxb20Q5wrmtZkGCR567xA-dBdTmxVWgUsxdZQS-R5ga99PYOKQLk-q_8OhYFG04J17SEKZWCbQd02RCah3GYgNb-FnOiebG61tdYM8TsPu2GpF2Llxk8AACZfFnT5PXm3DYES99Yu0ghuP5cwRtVVdBw0Wo0_Df1ybXBHEE_s9jm08hbGJC59ZigC0q0f6eVFs1p4HOsJnKd5UfZnsCTeL5WTI3e9barcg-qnLJ5uzA_AXoJ8XI18PBxmSLzuWFfm5aVhRC8xdekoRwi_5l3yoAu8jwzmSEBCuAuz8iem4Oj8aKPG-LkUfWrYnDa0sgBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌های بلژیکی مدعی شدند که جرمی دوکو ستاره تیم ملی این کشور دیدار فرداشب مقابل تیم ایران در هفته دوم جام جهانی رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/25768" target="_blank">📅 16:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25767">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVKH2ElIaI7kfT2h-SdcNJBuebsMlDRvx1PZQzSPTPrAy5iO0b1Oezc7N2xtftMI2BANPKb82XX2N3EzUY631zC5Gc-vAFceKsTagN0X7s12F3ie7w-F_XgBJ3DmxxHiIlp3V7jEIiXtZuwaTn5O2vHokBop0W__Pjz82N-rMDXsXUyW9r1fmOnkCQE2T8B_d5yJ7J_99bYWEuShGdMje9v1NLowr231Jr3W02IKnnQ4NSyrvafBjwH3gYctYJJ2wbHfKXzQrRZHDCrXt0o_I07LY1oghfA4aZJ2ISSVrphU72lscXPacGz0w6hy6gVSj5Clnce6lYWCp7Hv4Ghtaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رسانه‌ های قطری:
باشگاه الغرافه قطر به دنبال جذب منیز الحدادی ستاره سابق بارسلونا و استقلاله و مذاکرات رو با نماینده او آغاز کرده است. علاوه بر الغرافه یک باشگاه مراکشی دیگر دنبال جذب منیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/persiana_Soccer/25767" target="_blank">📅 16:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25765">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=kT-QBJ_6bjgE37lEn_tuQOERzjP4by97yjCCw3Rf1gvrEM4Z8MqfQZ3vg3mRFghKlWny6NtZMmwvY3nyQw6fC-RclF1K4rdVCxXe3OriyL-fFhbE6aPSW1lYiJmm15ebmTpDsGGifeITJEZS53Q3RhsyUY8n31KmobxAZ79SK0H3ZDPevXMdv83iw5iA30HhsTePBo867THZx0iNwyH78qGQf0AAcxY3By8FRTbgVpWTFO2qsliMupxuAG_Arctny7TWohMWO08jkEhe8rB6bkjOi1w-UTIgty42kLqNzgW2lXlFNEOQ6e8GAafARGfy2JI6VstpxFG0FAcAA8-4dQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb986dc0f7.mp4?token=kT-QBJ_6bjgE37lEn_tuQOERzjP4by97yjCCw3Rf1gvrEM4Z8MqfQZ3vg3mRFghKlWny6NtZMmwvY3nyQw6fC-RclF1K4rdVCxXe3OriyL-fFhbE6aPSW1lYiJmm15ebmTpDsGGifeITJEZS53Q3RhsyUY8n31KmobxAZ79SK0H3ZDPevXMdv83iw5iA30HhsTePBo867THZx0iNwyH78qGQf0AAcxY3By8FRTbgVpWTFO2qsliMupxuAG_Arctny7TWohMWO08jkEhe8rB6bkjOi1w-UTIgty42kLqNzgW2lXlFNEOQ6e8GAafARGfy2JI6VstpxFG0FAcAA8-4dQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/25765" target="_blank">📅 16:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25764">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vd5tlb9VT-lylYm-LiEClgj7oCk9AOSIMPUTRwStbUV0zrVqefiYoOAzmQ7zdsexmBsC8Nv5mHnqzc5YujtzmYVV85_MfhklwocbrPL79rwN5gNBsRJQ1AH6JDxkKP0tXhLEbEFT-AjKVUCcBUU1p466Q5PJJjUYnUDRo7MdUN5HJ43_j9KjAftkcLJZC2efoJNbQwz6fEc7QCLHv3dQxaBsQekUt6fK24jR28TaLAFoJjIZyAilDqVxkZydD0_wsbn-sL_THioEbnKrwFcJAQHre2kPfdaCtcga40hdfKAJrmhwlv8UT54oW2OVnEK8aGGo4btVh3zWQe5-VihEcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛ فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/persiana_Soccer/25764" target="_blank">📅 16:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25763">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NctWfWV3y5vC3YBeVWYNYGoehiXaBzYjr7cqn9CXTLbA4syizbFiBZ40jE-Cfm-eBBESaKOQGKKYzZFNOPbBPfyptS_ZcfnM4L8TPWOtaPi-Itygpg7dWoY7cci-SeixVY1hjhn8r2TbRAk-OKKyVYDzQ-vWQilLdVfFkD8KiGckCyOZ-qSQAKlpomd5gwvjcHlbDt0uV7j3rD-gFMw40Xz9msS9FTPQvtllzCg15bwOC47UYceD5znj8pN9ZtTrZBCkHW4pIA4qi7NUBtPE9OhVlw6HDzE7pPmUuQAy09q1fn65ShdPXDXjz8DvCC_Z_jxtyhaEynD4WcfT0qXVaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 77.8K · <a href="https://t.me/persiana_Soccer/25763" target="_blank">📅 15:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25762">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOKX-1xW_dzpSFI2HPJTeXeGmlmbUMx0YhOZvFBEghWvNcZiQyBL0pf3dT5vcHbS9nTF9p8TF-rAOJAPKsEKSUAbt2rAuBe8nuYjz021fFm7XEnIhvjS7M1zGCbTXQlyiPVGvWg_yKxxZTVwxnt_XVChqN6eydFuIB1DLPfCEDdFLkHEmGBlZ36NFos4l09UUKuUh5M3uTjBMecVmbrdVe5AeJ8mCumsqrqndGHuH75HJsOcefEQirJzhJmWT7anaC_4KOPkcQRby8JqXd7jWeFxY_J9fApghNmX8IGHF3B7_LKhXh-pHGD7PJYam1m8FQ1WNVI-29omHcbzcs1gcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی #اختصاصی‌پرشیانا؛باشگاه تراکتور از شب گذشته با مدیربرنامه یاسر آسانی تماس گرفته و آفر دوساله‌خود را به ستاره 31 ساله سابق استقلال داده است اما برخلاف‌رسانه‌ها توافقی صورت نگرفته است و تراکتوری‌ها منتظر پاسخ نهایی آسانی هستند. ولی پیشنهاد مالی خیلی…</div>
<div class="tg-footer">👁️ 80.4K · <a href="https://t.me/persiana_Soccer/25762" target="_blank">📅 15:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25761">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=brMlUap9Ma3lw5ti8SjmeidmAFhDvzn1b7KVsvbQXWvlgYkOnYQ7Vq7uo-_c0wPWmNLeqOSLm5-Xxv2ffedvazl-WL9ae5oOmBQIk-fsKSgR0htkmGo2RFs31hZKCr2cau3D8yEanZf3pEmRos_c1dIzcGzvTboAMn7GeDe5X0QqxZOmg1f4XkJ-uPKUDC3y7Jxr5imRHFkzZVOZgVcY0Mq3mow_r7gMe08u7rsTQDpGQVjS9ALl3RtQYfRgWeo57OKISQtMBjlx0kEgrvt6-iep0Wl3CD25TSeEvnBDYtt4U-Ptqcy7q8jkFMcTv1SBfK-eJLS4UHV--iSnnixIPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/33fde3599e.mp4?token=brMlUap9Ma3lw5ti8SjmeidmAFhDvzn1b7KVsvbQXWvlgYkOnYQ7Vq7uo-_c0wPWmNLeqOSLm5-Xxv2ffedvazl-WL9ae5oOmBQIk-fsKSgR0htkmGo2RFs31hZKCr2cau3D8yEanZf3pEmRos_c1dIzcGzvTboAMn7GeDe5X0QqxZOmg1f4XkJ-uPKUDC3y7Jxr5imRHFkzZVOZgVcY0Mq3mow_r7gMe08u7rsTQDpGQVjS9ALl3RtQYfRgWeo57OKISQtMBjlx0kEgrvt6-iep0Wl3CD25TSeEvnBDYtt4U-Ptqcy7q8jkFMcTv1SBfK-eJLS4UHV--iSnnixIPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
حماسه‌ای دیگر از جواد خیابانی در ویژه برنامه دیشب جام‌جهانی؛ از خداداد سوال میپرسه نمیزاره حرفش تموم بشه دوباره یه سوال دیگه میپرسه:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 77.3K · <a href="https://t.me/persiana_Soccer/25761" target="_blank">📅 15:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25760">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W4TgfW_gu5aL2TSJYjpvhsxmVSvWxwghGRxneyMCtSDG-BgidZ72JLAMLFInC5Y13JCHwPyfuONH6BKDDiQqhCuwlvuFQqsMvBctOKYe-YJg7JVpZcs_1Rfiua03sCeSRw7oOfixgJnARzKOhLiyyq0_FQEEagWB0_ptFZI2CK_IKq6XWYZWFEUeCJLrf0U65Pg_W5kxncxAwapUdKGWYbtz72wPr5KmE90VltBIOI67qeuHIcNpE7g0Nwij46N6ZqPzymIKCX9kX-2EE8t45zJPahQ7ksu_Ekyol7_e6Znfk1VA4qzGeq5-b1FLyf53d6-XSZCRlm-QpLwISvPenw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
#نقل‌انتقالات
|اسپورت:
سران اتلتیکو بدنبال جذب رونالد آرائوخو مدافع 27 ساله بارسلونا هستند. مذاکرات باشگاه با نماینده آرائوخو آغاز شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.4K · <a href="https://t.me/persiana_Soccer/25760" target="_blank">📅 15:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25759">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/klQhEm72XqABAmgPIgVfOiwmnlgCQQigtetl2Lm9-6Rd8UOeTBGv1MxNOmbDcThHjwYbfAyzbgIECFCMNDPI6iy410ZX4e38CkcVj9xsvVnQkuS09k9WfmJMlOTnW79thu7WMFJUbw4VHcni_ald1TtWQdtEflGmETehAwqwRLuJ2IeZjiJ1yVgP_T-MXunSIq3GLBN9hiGsUiqrBFyVLMoakMTs9zlfPoGHabVisgCgmZDE2JZrx3V_Pv80pf9bm8yvDITi6kYD_IXw5NLxzQohZcT6TQTYyzhBDiFGPqAnwQMxmKvDiADzrF1xcoXNCj2wWbwxiXj9bF4BTvmjbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25759" target="_blank">📅 15:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25757">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AoU7K3JDVsmgfHlOgMAiruX9KupZZKv_tMLX-V1-uyCarsT-l5NL23IS5h7jGKv4i5ufK5HPkrV0BcHamavArWs-srUzzBiRZtUTmKB93E58a_VCmCjQL8icnqcqCCyMefxtMfMOTjHsCp1ZEd5Duqrc1OmJVTKcZu21gl0q1vFA7ZpKUm36lC9intN-TVjv4y3ui2rn-3qmDaPGMfLzWkGErhCoH6Knd4bSHlqGYosQYhxFU0hbezgSXcMmH5WblMyc-utEyHqMkjCG99gErYK4KUkEmG_0zrlfk80X8hcJ54TXuEdNI1mwcG6yRvXxR18PENT636sQrNgMqA8qgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق‌ پیگیری‌ های‌ ما از ایجنت ستاره‌ سابق استقلال؛ قرارداد فصل‌ آینده یاسر آسانی 1.2 میلیون‌‌دلاربوده که فوق‌ستاره آبی‌پوشان برای تمدید قراردادش1.5میلیون‌دلار درخواست‌کرده که مدیران استقلال با این درخواست مخالفت کردند و به مدیر برنامه‌ های او اعلام…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25757" target="_blank">📅 15:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25756">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pYCCDeCYFyYFSdXBIuZJJq6iNjHNI6c_SPU0uBITIVIJmAv4wyngsrHsP_bJcJAlwI5DomkqYORiOc2W6SawKeCJvvOdcoqO_wTsR--bKfYOiSJf1_pEgggzBqeR_SnpGUu9KeI9RiG21bXt2ljw3dPDJ6I1t9O78c3N6ZxrmuPxydUxQfUXd1X2v3y7KCF-X2U7TWvtq9PPfAL0sixy4FMfIRQRwW1p4MlI2z90AytTXhWHQykdvTPwP12EWqrq0vZW_sWn4ZpSlMlfG20OogO5MJMMt9lX_m8tfn6e5n3AvJnyOXE8Q_WsU_alXTbi-7jtS2HOXIrD2vzFOs-xvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نیمکت‌های جام‌جهانی 2026
؛ چه کسی ماند و چه کسی‌رفت؟ از 48تیم‌حاضر درجام جهانی 2026 برخی سرمربیان همچنان هدایت تیم‌های خود را بر عهده دارند و برخی هم از سمت خود کنار رفته اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25756" target="_blank">📅 14:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25755">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D1WWbEG_0Qw25RVoI162FhwoS5DFMr8geJmuo7zcLFl_mL-LQxxpUy_voY1jvwZ-0inmuAbt7jJfrfVc8n1TFEqaYdxeb8EsBWkv6CpheXJpBOpghVJuQAHC2DV4jt0QCP5VSeF0TpBQJe4q1lhitV5o2Fcq59inmxA56gq08sYC5JoCf2GEzrlV8HbLQ1qWc3E3Jn7ogzxK9g0cVnztvYbOXrwns8PfT7GpOLeG27iWIF6zCi-PzIk1ZEBo_m6eBcYXgY_hemESVysVf778jadcoV0GsGV8Kq2yMc007LRtKoriBAsvU97svGnpb9WPCzmp4uuJOvXQjOe7UnOE8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
همانطور که دیشبم گفتیم؛ سهراب بختیاری زاده قصد داره درصورتیکه تا یک‌هفته اینده وضعیت استقلال سر و سامان نکند از هدایت این تیم استعفا بدهد و این موضوع رو به علی تاجرنیا اعلام کرده. سهراب بختیاری زاده به تاجرنیا گفته با این وضعیت اسفناک آبی‌ها از آسیا استعفا…</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/25755" target="_blank">📅 14:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25754">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XDAy3qKN6CYBtR2ahH_2eAU4ADQ3WpDzibWsKvx3reBTmy19IAEN7JMFbxGsDew4bgDB4aUtqILFd1imIqt1QoXymrDAKlNPf2yjSv6oOW90awLkkZ8XpLlKq3aIg_bnZCynnO8yRMMyMwZQQWgRcs2n7SMmS2AFoD1ciI8CMRpcQDVix9rVEmP8LI_qQ4mbIeteIg4ny5kDumd1lgMV6fQA0fJ6ZwY33Yv4k1oE1DRobsiOZMLfQKeCP8Gb6BlLrIwVHkz6CDrJEu6ZFyqKhlxTsTKMQdOq7V8xx5ZHHtUNDGgZIBK-ckvrPPc-o9aI4T2QgsRz7kuMD9p7NdI4Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
خبرنگارمطرح‌باشگاه شاختار دونتسک پیش بینی کرده آرژانتین میره فینال و اسپانیا قهرمان میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25754" target="_blank">📅 13:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25753">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QpFJvMaId-Uf4vrwF5qVzUxvGb73RQJATcbwyLvFuM8nrTq5XVsJat5kTVGR3DdiL25UDMfxa5QiCuZOXztu2cm2dFKc2TdjTgwn9B56-FnyfySbmqQWYEMTsW8xHPflNmfWbNamZ4aOx5usmcB-u4ZEnGOGBzl1IgRfMD4IVRy92KHBHQyOEkd-rR_pO-twumJwZP5lRY9MuIzOfufBRmhaJLftP00mS-evG2DvOxpASJi1oy6MSfuU9IONxp3_IuIF-NPGArjR0xbIVO9d8TgPLDCkJmypsm9PtrXoNPicM5U4XT_nKcUKn78cBobogDAiTijFwkNnjUNk-Ep58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ممکنه حتی بختیاری زاده استعفا بدهد.</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25753" target="_blank">📅 13:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25751">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8yQEddkkPI_4laDOR47xzSpjyd5UokquXhz87qr4rMWqxsoeCL2yXIihZY4YpaumGhbA1UCC9qf9aou_cJWAfGUF4MiLxkwf-gN3rn_7JJKw7zg-BSBiI75pgwAYgQ0zEwAJFYIzGL3PeonYE_fMkJGggldj1ed6tFKVe8VKldreYPMtXDbrTDCk6JE_9ZwDj2Z7wvkZZQYC9VXREda3ew5s_EKK2IG7-4tnpNk4OU-expOWlehzJJlD3WCifmKmqyvShQy-BA_McAkdMnfxE5E1mpdY64kBQdTIU4DukFRSE8isgkytChqYZArflQ7H3GeVz2cxRGB7RXAIXdUSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
کمیته استیناف حکم خود را درباره پرونده باشگاه پرسپولیس و علیرضا بیرانوند اعلام کرده که باشگاه‌پرسپولیس موظف‌شد که مبلغ یک میلیارد و دویست میلیون به گلر سابق خود پرداخت کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/25751" target="_blank">📅 13:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25750">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/holsCnO_qVc27St_rpaSUim3xXyuTpWDWmVFr1bsQTAEjiucb4GzeDfeJHe3i0s2AdO7T_IhyhicRcWVycfr_qZLpHdh3oyBQBdo2WAuN9C5ck1rCTO7TccxT7eQZ_ds_6OwVZXFYS7n40uhp7RGgISIlytNvmyOx4CO2_Vq0xRayC40cWTz4sdz8W4kRrKIn_9VRiMi4HiQ2MgnooP6Q1y-7ZezdHtDFPTHlu4cKVocm_MmuCHoPeQykmbOm-pN-vZXDBHLgE9g32OB28CJt8UQmOIJCH0CWS-gkaL7sTvADmm8jYZ-LIMhIwPVZceEo1dybFftTZrnQ-v7fEqu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25750" target="_blank">📅 12:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=Z2R_gwPEaAJfyGI9VGHyZg1T2owXopohw2X96kWCD_uSQ95r1OLXee4BMvdXAoTH9XYSzWLQDaDguxfdzHRdxAHscI4VUA3LcTaWMAubPsCUhTcVNxcrJAH7u3fhe4SIZe2aGYXYNcHLX-6lv9jcUD56vsmNI8Mw-vgdEucY-ZUSfZkEyhcJLGgTfBXCzTnM2rirGnbd_AChEbdxWBMEVN1ooZlzNh7Y--POeyWtPl_2HGaXWlZkcaFoAkCgdjxJozFl5P93k9LKZwdpr_FE9CXkZPiNLZHjCmiL6wUieWkkRjKbE2MorseX-Qhg52pqpPYGRWmbQFviNGBDi53o4A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dba39423e.mp4?token=Z2R_gwPEaAJfyGI9VGHyZg1T2owXopohw2X96kWCD_uSQ95r1OLXee4BMvdXAoTH9XYSzWLQDaDguxfdzHRdxAHscI4VUA3LcTaWMAubPsCUhTcVNxcrJAH7u3fhe4SIZe2aGYXYNcHLX-6lv9jcUD56vsmNI8Mw-vgdEucY-ZUSfZkEyhcJLGgTfBXCzTnM2rirGnbd_AChEbdxWBMEVN1ooZlzNh7Y--POeyWtPl_2HGaXWlZkcaFoAkCgdjxJozFl5P93k9LKZwdpr_FE9CXkZPiNLZHjCmiL6wUieWkkRjKbE2MorseX-Qhg52pqpPYGRWmbQFviNGBDi53o4A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/25749" target="_blank">📅 12:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25748">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3kUFeg_1eTRuQnqjvvfeDS_KJj9pPzSmWHGkHKjQaHt8noeTY-PKqZtfzxKycS3cqcVn770H705_fPdMrSJIVKb8DggInZY6CTi15C07i8lA3b39D9jarfLxa1haHOlLVDnlR5xOZ0pW2we_7C-9usdtTkXGfz0paPQ-DL-B4cB_jph-TJ1u22o4uXv2xsPXmbogJf7pXCJzN2Bj5op7jU5KeYOzR100DtLpCFziIfiLo0sD9OM_4ViYQue-nwTlmQWURws-BdhzHGXINi2jAJkngTWzob8rCSrP_HRCJWHSjfH-vF2EMYKS642Cd6kPrmoffhXTZFZ07gip0fQ3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیران استقلال: آسانی برای ماندن مبلغ جدیدی میخواست که مابااین‌موضوع مخالفت کردیم و رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25748" target="_blank">📅 12:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25747">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZSjoD_6XRW3NQvw2jo4rs48xapyz-MO3SG58F-J6LC6nai8I1y3ShQ438pL9jxYYMBtciVdPf2tHWFyzsXEy5YdSxKQSORUo_D6Y54SXjzXHasw4cqpP0CihcSprSdIPnWvfvQTc-3KQl2viVMW5YRRIqQF2rENuN3BsqbACJQ0xiOtUZwn0YmZIdSumzDFdXnkpLRRX7wvCCymvyEBQw-UEqcJXXg32LqqqvoR_WmbhXIM7LbHhNu9NJGXW3Vs252GKCdAFg1z6U81Z5fKYArDXAmO5uwPvOxkPmK6vvPDwSUcSeV4v2Ezp99g48hrzO5OtFFdrIpfAYW57XHAc6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25747" target="_blank">📅 11:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25746">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N7MPbmEOaXq_R6HEmC_fkfZAj6Dtr4VRQwO2Eb5LydtLh51LwqL0Sg6-348q3OU-VTPbLtX-rmw4Pi9ARCPIv4d8IeACiw5fVDfIFRjXlv_PU5Y4vkgMoNFM7FhEz07iZCkwVdobCiN6mG8VQk28Y7FaEWnT07vBGqFqhOF6imKFOF1NgwS6F2RVGNHhhtMvdmiOJ2ur0T4-4ZziXRtupTf6AiL4ZnXZrlJ5gnPCzRl2wHphzcWbrsNDO2Vp6wONE19FFxrPUCPt7J3hwOzMzxRDOoQ6qTtz_0YhQWbio8tM7AKqr82sUIfOGTNXs1uEmfbkHyJGexgm2CkMlniUTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
هایلایتی از دیدار جذاب و تماشایی شب گذشته دوتیم فرانسه
🆚
اسپانیا در رقابت‌های جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/25746" target="_blank">📅 11:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25745">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XvGyQiU6fkCoANOGCSOg8xoYoMdRfz-aIekmxoMvV_pEwq-ar3ieW4DcltPRtDf_IHSrxcK4jq87B2pXG35tq30GOEq7lWapIZhLS4G3RS4fItYeq9RcAnP5qQoJGyJXL3neJGKZzTwz3Q9o0Lj5UJR5HjuhkJuMHKTUP5weUmk0Wf5LTQf08pk_qY9mXyADsddCX5dS4Qh0O5zbh39tGLiw_mOSqK85yZmHaZXdQvzoQVFaiZxnTdA99cCGu9jaPeDMuO-ZkQzb2rdJckRsQGCxfYKEaqXdQJiN3vcKYnYPQ2iQJhDYLoHo6HL1grDoG45nW2m_lcv9p-AKAkOJxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛دیشب‌مدیربرنامه‌های آسانی به ما گفت که‌باشگاه استقلال ریالی به آسانی نداده و به او گفته که‌میتونه بره قراردادش روفسخ کنه ولی اگه بعنوان اولین‌رسانه این‌خبر رومیزدیم قطعا هجمه‌های زیادی به‌ما وارد میشد پس صبر کردیم همه بزنند بعد ما.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25745" target="_blank">📅 11:28 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25744">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DD3j2_n-AeHuYu673-6pxgFJ9jORSwJxPXQWfala50WkGzP0ehmmc_hUdGFQibL0UIrzwQ-v1wW0C_Im88meS3V2wn3l7P5LkxB2P25VmBByRxhP-fDvlpaLNJ_7QjFP_CUxpp72vuruDmWh-Zn7xoYLJRAW1tExxrSy742uAbmfhw74QGHIIQwfovq8fK0G9cthTA0c19fXqvBWwoeiby018Wi-Txu-6qHeHiGDToHz-3nXu5wB7vYOZGdI3r2dW58wJZZVHk-O1FFs43CXfkJYVFA15AUex0nI0E0QrniMo58Gq8RPITgffoGgzkypKCfSocdvU6ORx8r6ckrcCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ پیشنهادباشگاه‌سپاهان به امید عالیشاه دو ساله به ارزش95میلیاردتومان است که به احتمال زیاد به آن پاسخ مثبت خواهد داد و بزودی با حضور در باشگاه سپاهان قراردادش رو امضا خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25744" target="_blank">📅 11:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25743">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=k_2ArS6eEgdsX_9rXBAbx3sihwVE_LqTvMpsvLvdZvcSkCw_6GaELoaCAOH3TUcegtaASPH9vx5Y2Fi-ptcx7o6B6PRg6UTTEbnVch_cSH4shxaS5W1gAbjOTlqCY5f5hyTL7xoJDR_JQbjr5MkCpeHb7HwQZDXm99fdW0WkMGNqeKN8mC-apmq9mh7zX28UWuVcvS7Sewz4e2KjvcqGFhs2cJS6fw9roSMYF_mkb4iuX26tocTpDkX1LZNih-PJlQZdPqdP9qBhCjIXIFvb2UlkpEzuP8NBrTo4vMl2FSTgfO79f1r9ezYBts25DYFn4qG9KZzo4g7G6d5KwkUGvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1866f42adb.mp4?token=k_2ArS6eEgdsX_9rXBAbx3sihwVE_LqTvMpsvLvdZvcSkCw_6GaELoaCAOH3TUcegtaASPH9vx5Y2Fi-ptcx7o6B6PRg6UTTEbnVch_cSH4shxaS5W1gAbjOTlqCY5f5hyTL7xoJDR_JQbjr5MkCpeHb7HwQZDXm99fdW0WkMGNqeKN8mC-apmq9mh7zX28UWuVcvS7Sewz4e2KjvcqGFhs2cJS6fw9roSMYF_mkb4iuX26tocTpDkX1LZNih-PJlQZdPqdP9qBhCjIXIFvb2UlkpEzuP8NBrTo4vMl2FSTgfO79f1r9ezYBts25DYFn4qG9KZzo4g7G6d5KwkUGvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس‌اینیستا اسطوره‌بارسلونا درگفتگو با عادل فردوسی‌پور: لیونل مسی بهترین‌بازیکن تاریخه. از او همیشه انتظارات بالاس. لیونل مسی فراتر از کلماته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25743" target="_blank">📅 10:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25742">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25742" target="_blank">📅 10:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25741">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDYxKmuDHYAYQWRzO7CO9kBLl6J6aOmD_ohWE9Bq_fVXIamwsgmwQe-C26JpFwK_hm6RhQ1fObJJI48lI2LrHZh-g4Nz7IJuYe4soRXqX5G9kDwsf0PSQ2ofH3d1YNLqmDIdJA03qDRlwTy-Pm8bB770wpDfQ_83ZO8jrU6LTrf1vznUFzitVhmunoXohOEM2MzQs6raIYCDZNzrzMRSZgXQA9jLVIyYTsILzAzQ05HD6o6EPskL4J0k7URAOPIWyv8bfroavgDBna1EKB3xUV4kjHGLuzGhIElH0PGd8RBvAeRfPu9uy_lZit8IXV5dYAdii5NeICaDxyySknR7nA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
محمد عمری وینگر 26 ساله پرسپولیس دو پیشنهاد از امارات و قطر دریافت کرده و به احتمال فراوان فصل آینده لژیونر خواهد شد. از این انتقال 600 هزار دلار به باشگاه پرسپولیس خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25741" target="_blank">📅 10:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25739">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fuCkYVFhRiOUBdU8cITfsMAHRqPlpAdvhFmd1ngoBDTe-sed6_b9aZA6fY6jtjrVskcBC_Uw3Ie8aBE66C2AE9b39Rwm7eYkbH81w-SQagtdRCHu9Jb8d-66wfhaKCCQVKP5VfFGa-hQdQSqAhkuz_z8aOIBXhf4puaNDThM155xybEglJ3MX1ph94ES3iuQLdcff86XHsK6fFtuEp5MxRUDMa4h2Z0ydWgM2RiCbKjybqG5KRt7FELObsgwfgPrX8ysA-umUwtK9XBYM7frgGF4IaJGLKpf19Tnmx0ztmZQBtuadM2Jgmix9S2vw67OPE5sZmU-xv-uRkNhGZw52Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم؛ سال 2016 دقیقا در چنین روزی؛ باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25739" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25738">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=KxThJFGTmqNu2Cd90NKOt4tZIcBEcwe3LBhggjmSifhBvRqsk6jCNV2V4bhOz7HT7G0BLmBZIWA6QYkk7MaLmuoe0KfxF_g7iw29crgZncUlNYsoyCkfVV8hpkaHq8vr2I-My_8zzP_Je1Y3Zfof_ZmmGEO0bOgvPJorj9ZJHQnDMa7f-fmZyng7aies4Xqq6raPDX4xQ6ApxdQVi8L4w3N0ovu_RPashULKHTHRnVLp8p-0qrVwT_IQKJjcGI7AWJpXZMngbfpg-DOdcerqTCs--zvyw2cy9HeQGk8MIMs-HiBVJokPLTmGOEdExy63KY7C9x-08fzT7caCLSoj_g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89f9fe6011.mp4?token=KxThJFGTmqNu2Cd90NKOt4tZIcBEcwe3LBhggjmSifhBvRqsk6jCNV2V4bhOz7HT7G0BLmBZIWA6QYkk7MaLmuoe0KfxF_g7iw29crgZncUlNYsoyCkfVV8hpkaHq8vr2I-My_8zzP_Je1Y3Zfof_ZmmGEO0bOgvPJorj9ZJHQnDMa7f-fmZyng7aies4Xqq6raPDX4xQ6ApxdQVi8L4w3N0ovu_RPashULKHTHRnVLp8p-0qrVwT_IQKJjcGI7AWJpXZMngbfpg-DOdcerqTCs--zvyw2cy9HeQGk8MIMs-HiBVJokPLTmGOEdExy63KY7C9x-08fzT7caCLSoj_g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیو لو رفته‌از اعصبانیت‌شدیددیکتاتور کیلیان امباپه در رختکن فرانسه بعد از دیدار برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25738" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25737">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/CsPEEjqrp-qtxGQNw16qGzKTADHm_uFO04GyNnmTVwIFyk8XVjO9PsGjs_RehUIlLyqAdU2jkSMwaaVHdAd-64dEwpXzESYkTBhWypyNJPYkrwZb-fYZgthxEpmcnDRdh8R23l8dbPjmlSG6xCePmZf34WGaKtO-0F_nBpuCES-2YrEc3ddcJQkO_6Iki_wNErwyWsx_aO-vPB0z0OiwSCchTQqJn_MXmDTDKnuRiQyPbqR6X5iJjRqOd0QyoV36NJXoM1zuKr6173bY9STEZ2WRvy_2x1RK_CMFR3q2npjGM8vAllmS9sc9jYqyLGaFQsr3l36n5Pgb2XKoUjRSQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک‌کنم‌اگه‌هرشب‌با ۱۰۰ هزار تومن میومدین چنل بت ماشبی بالای ۲ میلیون‌سودکرده بودین مثل دیشب:)
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet
@FuckBet</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25737" target="_blank">📅 10:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=vLrCvQmhWp40l533Z6GJDYkVV29yP31SBqiL987MzQZc__gFulSxnX6d0M-mups0hjHUmBwwfMehqO3yLH6iF4TJUlQf3GaknXcparu9Xqyvmq5md8bVh5LXYbswFQPWVmKZT5z_a-1vJCNBHBcI4QAqQkNj3KYB3E5upHu7WnB4TPHI14Ms3n_2zjVA-3OejPDpz4LW2Ef68CjwPMkq3p2lO_bSl6KEUBPDwYnlSQ4RvrsRn8mrfpKZEUKAI5d-HThG0YYZ7unh4gvZayZTmedaFJGKUH8AzC72cUSCXUiOW-D3MysIHWsCuZLlKdBDQQFZ8visskhRti6y93f1tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=vLrCvQmhWp40l533Z6GJDYkVV29yP31SBqiL987MzQZc__gFulSxnX6d0M-mups0hjHUmBwwfMehqO3yLH6iF4TJUlQf3GaknXcparu9Xqyvmq5md8bVh5LXYbswFQPWVmKZT5z_a-1vJCNBHBcI4QAqQkNj3KYB3E5upHu7WnB4TPHI14Ms3n_2zjVA-3OejPDpz4LW2Ef68CjwPMkq3p2lO_bSl6KEUBPDwYnlSQ4RvrsRn8mrfpKZEUKAI5d-HThG0YYZ7unh4gvZayZTmedaFJGKUH8AzC72cUSCXUiOW-D3MysIHWsCuZLlKdBDQQFZ8visskhRti6y93f1tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NnUi5D51LwBzDQrjz_CyEMBI8sHYs_rfnJ65vJY6Nfc8_O3dZ7f-zbfIT552Q-6DXbeN1wb0t9OKcCA4G2qNKUG7WWw6GmQozx9pJMjts6a3Q2v2eWzDEtLAXYy8ycwAHJmrkRiXA1iccPcwX2OXj9feAk0yrTIhCle84w5dolulrxLJH5PmL3xjLxhOeCUDCLvpTmfJV2FSZQSsd0D5qMnIxfWdi_pSz1tre9PwfepZBal48nYcVnTgIgl1AifSCmLWGU7b5PScV0pN5AYfk45cWOvUDF8_GeQEjMlGS9QhDYE9he0yfFgrfDEOhy5Nc5q0a7-706VWhpAG1e2K5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u3iGZbZ2prG5rOgfo35zLIQM9QqixUm7EV3QxSwOBmlRDFA1Aag3WUmw4yxsQi_SyCLje3-HxLmqBzW3mPXDbeEWGTPNdt9f7eis7FdM53-LkVPWNdCMsNBL6VSYE4ZWrZHSJhCXOKTGi8Y-j6X2dKo906aW-YmChoK82ZeoeNHMwtIOfyJ4GXzPtpIuAhS9PhL3GBkyMmySJ3SM86MpW_44x8M6gbBbWtwxYm8h5ZQhlvnLLK_Dr_R_9SWWXosbOPyn-aYIwmQHYzFHt8rJbrKVqz4i8nbgUyXfPCEHhanErz9l5kBDWZy41rmCwELFgtfOSlNufceQrF0DyR-Hkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=G4WG8sf87s6yqMJUvHpjXS3le2sI3cCMjwBT_KHTqYcIi58JQ-cgoGUGk1bWjEmEtcIKhi-lVGGxlmv7kPQaUFUhrghTNYZwMVEJvURS5lxxTLNbFbNM6SXoSTHwstirziZQLpEZrIA5DrqPFSxNQGyceSU-osMH_j-smk0DRK70fdfi-WFvoHhjyZMGmb-anUAi-PRsEc5mUhkmWy-fOoyuKXAr1rWJM5mYVrhlCqpcDFd1YB0ewPMpAY4On7ws2Kg8UZePAqyaQQtKysFiP0fuspAj-X4N-cnnOVnfnX7f6N7RWnyowKnWx-ZS5NwUYIwp1CafdtYYuJ_tPANVDa6Q4QColkCcpNKc2d94UtUR0JqJQ_NhzqSrkC0WheexyXZBDOTk5GhLepZ2IkJeRpT1XkOsvkOM-vvlO0I6Was4tgSPJlhsVQf-LaVFogBMZaFPpGdZEaxPmuIjPgPjFHOa1hNcvrbi8DXyAA4aZE1ub8-pHUMKAivRF3VcR4TEFX-32X_Z3KzXeDwsqbL4OXUAyIvMIjbkW_WIGCmVVfFbGFwO-FUyMzb5lVgg6kZ1CEQacKuX8643fekN_FoFdGX1ArY9RDwjnmOcDb-kXXwM39T4to2D92Ak1tvsyNsu6X8e3dPV5DD069v7X-hM1_MAvzhYRejJk9bS1vM8dIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=G4WG8sf87s6yqMJUvHpjXS3le2sI3cCMjwBT_KHTqYcIi58JQ-cgoGUGk1bWjEmEtcIKhi-lVGGxlmv7kPQaUFUhrghTNYZwMVEJvURS5lxxTLNbFbNM6SXoSTHwstirziZQLpEZrIA5DrqPFSxNQGyceSU-osMH_j-smk0DRK70fdfi-WFvoHhjyZMGmb-anUAi-PRsEc5mUhkmWy-fOoyuKXAr1rWJM5mYVrhlCqpcDFd1YB0ewPMpAY4On7ws2Kg8UZePAqyaQQtKysFiP0fuspAj-X4N-cnnOVnfnX7f6N7RWnyowKnWx-ZS5NwUYIwp1CafdtYYuJ_tPANVDa6Q4QColkCcpNKc2d94UtUR0JqJQ_NhzqSrkC0WheexyXZBDOTk5GhLepZ2IkJeRpT1XkOsvkOM-vvlO0I6Was4tgSPJlhsVQf-LaVFogBMZaFPpGdZEaxPmuIjPgPjFHOa1hNcvrbi8DXyAA4aZE1ub8-pHUMKAivRF3VcR4TEFX-32X_Z3KzXeDwsqbL4OXUAyIvMIjbkW_WIGCmVVfFbGFwO-FUyMzb5lVgg6kZ1CEQacKuX8643fekN_FoFdGX1ArY9RDwjnmOcDb-kXXwM39T4to2D92Ak1tvsyNsu6X8e3dPV5DD069v7X-hM1_MAvzhYRejJk9bS1vM8dIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ezWUATlhTooWTYwG0eLAHdwsL6dX-wvMwhHK2FONWCByB-UQE2luOYmzZNurHmI73yxNZAIoaXzEo7fpcxr1Ez6Je7my59OK_bHKFLhghS4QEIpCi_zy-fW35FhPecjr_L72jMBXd7NlJqpsWYUzie6yCwJ-KMxvGQMz45kPky7PmYjjsp4H3RClRrJb8vpX7HfpqM_sjdtXwRorUgHbjjM8nCL0AB_v9Brh7v0i36IB491tM6HA3WivLx74EmwT88GJpUYQb81MGBhaTMgcrgcAXR-ZU7QRidVpRAgGYlNcbQ2hW9xk1gLTz6_fwPgmuvsa93WMCo1qb5w_QCaF0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLudrCHT4ffv1LNJpQmvj0a1ri_l-q4YZ643hD1UY27j0biFCVUnqBscs7zkfGjl59b3W0u68beupi-gsh4SdprQ0QUljKZ1J16SeZ0nYphbZI8BpxnG0bPK5seQ_CGu_Sp2btUBQrhyntxjaRtqWw7UrXaOxEm1Fj9aLQ6hk0qIne4P2y4TBpnOgbC1wlN5h_GxJhQEkA8tKAAKe64Jsn4UeNDlqVDDMbmtl1Qz6lacnmWJGZLIy2P-ZaMhjBORJZXXyFv9Z-a0ZgvMISZ2i4Ey4CPma6y71QYHmT8OX4KJ5tyk7YjlB1L7zVYntEZYxTsvJrn4UKzPiFNhkxBFEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HHfaeL65261AtyOXD0_pNEZdWruViZrScqHBt0BCbCxLef_hAPgeBdGaP3BREvRWowTeIRAaeHnmx26k5HcR6Kd3PidDsENWtgHvEjEs4Lw1n3ZtAoS6vdmMSPypv8GuWFc6evDRjX4oPqCV9QjJBOU4wX8SZIMd8ZXnLys6H1Z4OFFjXwt5LUYCIKeWqqet07DXuiCZo3lgAhv3S1ffAvfdCRWz-FEHUSHtdCkjZjZ59p7PctZLCO9pTGl8cC3BQMhjLbppYa0vO6N5J_mU5I9mLk9IIqeQTtzntKCru0ZbpYOLnkebjnzBKh3_cV8fzo7hMaH5Je6_xNZJf5rWbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIdIER3MibiDTqZIbNRYm_F87-_ndd68MbIcOgbjBuTsNQpyNr0kwY6AUAZGTy3hMPjpLNwHgEauecC6l14Hfl_NnJBaS8eOax99nY7_J4YD5ss-VuGkqsaKV7GEvrnnpusrpnGgYuPUuomYJQ5qxR_CN5xI7kxsqXB4GxBbHK75Ow1kQgZtpO9hMPvrfe2rMPjhpdfrddkE2ixE-wbk8rH6cByVr8r4u3lwSwO7kKKVnEAiFiCtt0cMbiCMcVjIh7RS8orkqcmXQ3KdvZJasy-ctPp_76HQyjFr5kR-tnDMeoZIVIuDwxjjmP43JSCr0xdiFGUChjz-FawGR5okwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=lI6yiHgqwARyiO7YDxSSdUd86pxT89T87DxulPRP3aJRlvYGmsIZKdDUJgT_QR00tXCnQ-Q_Nre93qmXLzX6FB_Gpa5cGF40usaFZ6UtjGpjyI4vaPVVNAin5yVZnFy3cSxZA6enh5h-UTvZEn3KM3760wkQ_3o8G-SVbpgwTKV4fQyNzERgkrTp2BkLrVTnwMT22WBlyMlMPq63E8lqefSbjZ1QDaLrMQnU8g6y7klKrJeBomEUs3BiHvGJRokoMupk_JOa-nsUxtL6OezPmoQ_OeeUd7C0PVS-9B6gClUQ44Pt3L-iW3CtLl1bdeRqefv_QrqyRsiqUPC9JwpQZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=lI6yiHgqwARyiO7YDxSSdUd86pxT89T87DxulPRP3aJRlvYGmsIZKdDUJgT_QR00tXCnQ-Q_Nre93qmXLzX6FB_Gpa5cGF40usaFZ6UtjGpjyI4vaPVVNAin5yVZnFy3cSxZA6enh5h-UTvZEn3KM3760wkQ_3o8G-SVbpgwTKV4fQyNzERgkrTp2BkLrVTnwMT22WBlyMlMPq63E8lqefSbjZ1QDaLrMQnU8g6y7klKrJeBomEUs3BiHvGJRokoMupk_JOa-nsUxtL6OezPmoQ_OeeUd7C0PVS-9B6gClUQ44Pt3L-iW3CtLl1bdeRqefv_QrqyRsiqUPC9JwpQZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ezaf9IaebrzbUnln2St8R1O01SzNrlEfEMHLE2U3K0-VSLeoLvakkyrvExoh0ZguDy3L8FZywgEwInw-kvY8A2zJtmgqx_JpSpm_puHzodFZt_NVrcRFPuT457uU004LInU2UllH8c5t7RatLdq_4l5vl2WG5_GIvqm4v6ypTEcB9RvNM7On5pKtY_Lj0HGor-V-TF6viCngM0NTseFEByU6aQxsZ0uyOjCIyCdxCDneGx0lZJZWjiOYqS70LixyX_Nvk1ht6Lvng3rBsskkp5TDlF7OUxbZEpRnw_bHR0byyMi-TXTV1GeSw72Lhbd-vx8d7ZgikeD-pC8Nz55PLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WU_Jt5udfW31lYtf7gfcUqw4W05tAI1ionXZOplR30zaJHLvCVEDrtt-plpw1avMMYz5EiwfiMFk52hZVBtUlgAZjpidOh8eGCesofq5gT5aZqOhEpZyluhZlbSLO4ke1PvUg6bAGjf5tsZ4qpOLlr3P5FKx4tI03qeYjHAPg-vt3ot3OsZFCbFnaHOHN7_WFfXgBhdTvA-zSYUw1jJ_5RhfRdAFuRJEzhNep2kDK31fAS6MMNFrlndt9tXOkK5tFaM-Mj8-FIVgoEyQRjnrneq9L2zjEvLZhkN3OCZ2dqEio-MuDfJNpGU6N97BZAYrFyLB1uywX-680bZ9yk4x6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pqcByIlxuoKHXzVRs9_m5IK1KhHIvESuQA2MbYwFtsvUAyZ2WtECYYVNQJVIo7bJyFu2c4vbHNuNQPFCOhRzTsgD1fnfLk-xV3iWcXnrhZNFAHIwoMgAQU5IX1xJob8y734SShRMQ55yYpW-M5yDxDHjzlk6vJq_hfprl_lMeuaSFJNBxgyvHu8Kn8UGO4DROOZCJhx8N5d3o-qbsCJoRzoMex_LL6MwLKvGqEIZ0zGVmJ1GQlse1PJRTSHccvgBxWBXq0S1mXWlyrZGGM5r4RTIJqWjRnGATQ0ka07_cK7zRDmM9nw4WoIxT-Zjkxinzq_8b0ZQoQYeeCMY62gDXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Yn2ZafYgxVm81WX5EGuJnrgHqXzP-EzChI4cuw_MG6bgirDByXQFFyx0XilXUK1T7rfF0-1TgTjBm9OF0x5VLhX9_i1IRFCQ8wzOoVvWaSikUw_F2cAh1H7pjfbcwS9IVEXwLEJZG3sZT6xDW6H1pIUaxpw_1BryPIn_Z9ya2rCBLxoMpnWSj6QFk8vPbmrPJ0VMKQbnv1Qd-9TZFrxwDSIYNdvvotJbCrYvZARNLMMAoPzPRWh1MPOgbghBF2nXqhrcBjw21DzVvUX38GVRtC9Zp1_cF3IepAvYQPQ127-A_nS1KO6fQHIkn8wXa8coEfsoL3ZUj-Ol8z9q_9cgng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u5vwl3gCubFat-V5tzPQhThTW-FCql6Liy00yNL3AdRn5fb970ErzyHES4CwHgWBYeeA68T6aFmQP1JiOkEAUziOQWfgpCC7wtn1-YKKTfO9-BcS4DeLOyVPsIBZb_vUDjVVP8U6BK67K1Wq8Y1kTZ6Wl5UkWGyTsPeFRmn5DI0HxvkHgkFvjE0w3uS-Ic2mTHB7R1PytZpxPheJwtwPDr9dh5aEdKwG86mVAfOA2eUfmGqDxRdyL84lwoTi9NIT3M547yG6Jm3OuMGZXhmOy6d7tG0wcOX0Wk3kKVxYm49GRWUNRZ1fcm1pbjtOCWdmXpM5BI_bJew8GkZDK1oFYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlDamQhqXFi8JWvvVnZ_phw218loY-bevZ8ZebT6QXcuX0e1xPySRd6Iz2UJHLbnm02aYJwle6uZSphQdh4Se3JzqdxMDQH9K0_bvWELYNScYKS1k92GDnFBTcQg_ZodRN9gOz_Z_mFnMlvrNTW1xgTa6GuRGvEGcgmZtAC5sAQtSVlDLndfKfaFXwJxhorx3Np-rLSZDSglS00t9HfjS0THiT1NBaDhtprUwz5iQbJ7xo6AOV1NaPLrkxrnWBNFj2N7X-nasi3XrFvY5CqQFuM75IReiB1ujGZsvXzvsKfMeQFFXzYa0i3PoMtJVMKWjTyrfLoFrvDOjCHIWTvPGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUiV_3MTKe8R7mgTL2AbEh4KX9CvJ5RaFwmaDNNAOmo0P-26pBUqfEmqz6JYKqF-lz_-zYBgz92dcH6n_XpK7xcXr-O7pbAFgVDMccVR-vIDzN5_YTGSquQkP5yNb37hYvM9wLd7XxDmNWkqJ9gxR4-WloLwqgZTFCog4MUV7oUEa3tM_d13MREcXYGuIAUpMyBDp6M3U8tNpX-Dz1rr4gaUPkpNF1XdU0b1_fqyMTQ9vwTS3xWVlOE6SWTrWklHSkmgUZtyItCNDpnQ_q5-5xroz8nu_QdjE-crK63dLTvTgBw4OOkGEmJ59GWNM8xsv94wYRIlJRbkFqwrihdAHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/imBEcp_Y_0BFJ6YozGy4L0dR_9VLz0FobUqyAJi2fKUnYosDQKzYAO74aRg9vtWsIekx6dsip4byMubZF_cZdd87adOb38BaO_dObzJmZ61aFl2mNTOJ59Zrv6jU6E9Emb4DYGFCa-GenVsT9P-IlqUbEMlq-C_fz0-QvuMGsbjDNjpS13aIF4QqWUhvePm_3Pxp4TPIDvJka9CCoFlzbsP2x6Dl4AMRRQfQU45WcxrGdXCfUsmoUR6JyDiTZHekTgL-AfOk3t2lQ9Mz3udtK0qsYklZLajWlf01IJfT__IEyeGm4wnbzhQpSfbAWH4wQe4zyPUfNdsKJ7gEf_7OQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ly95w0CMq0nI1BR3LjzNgXiIBr1xFz02gON4nh1LHCm3YrpeoPjaL2VI5wuQTpParaez2FXVv32XemP6qlPN5-Xa2UBVSxkMA_ARlDIO9VrTD_XsWla810gYuNd7sLSIBPJsIx3m4GY41KHNOimF9hTcn_Mp7tcGBHiLBkYmSSvYXkVxRaCJI7nV1mlIftjPyWzkwULTjnGzuUSOr6WVq57QhpuryNe-YqzRTJdMPbL9fnPXRUrYK4CjnpPaeplw7rAWhfnpwts5s6_7-DrMg8MlRQeyiP0Ju8OjJvrU7AQqefr-87UiVya49qwXrb6Frgwk8GFmWpz6OPe8nJ4VGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NbJzk9DXt3GJ3nwgmCaFJaDUkbpX37VrsZrX6waiG5HMPniN5qeqOYEngkpTbPwvOMVBBwect7lalGdQ9n7bmnWs8X2qpu4tmZQtiA2A9gPLKpGmPNwewEuTvVLDhESHt53YfgnFqeKjSW6vQwnTdab85wrhSEzZy7ct9W2M5oWoEFmyvtIgoOOMyAcjA6jFJYxagYPM29J3rl0kQ6LM8vSd2G9y8-8-nyWb1i4YUp4x1wMeDpMqefEwPdeM7KSFRCQ75VyuXYi0Fw75sIQ35bYNFuNngrCTCj_GBJ8fWWZlURqEvQVfreLh8JC4PiMmer-H2ggI9lv5apcJReceug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n18AIBx7nKSWNwosRPXhl0QlsbSa-2y0V4xNSEFvKjnv3lyqejbyaxeq8Kased75hY70XDHzvfn9jWKhf2x0WWm4GvKgj42EOGfkzHb1CeQF1on3nNqI_3hMXA1FYBkOuNzOLjPzeUE6m43nHvUfF6TtHWoMd7brVLkSBe1nrwh0-tUSFXqgL2-HN3QIZAjVp9fIGZk7chGYccaQESBLgO15TVWfKQAsj7Vew8pzg-0EoI26zGzBiy7qMqUuUOf9zp9mDmDfCWRHj2n3mcMmaGwAlcdV2LkFRK-x-ADr7VNlGODkc9xNiN-o52nsyAItGMPUc4edm2NBvc7D25y-lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
