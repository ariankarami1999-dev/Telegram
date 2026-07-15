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
<img src="https://cdn4.telesco.pe/file/dxqpSRbA1xS9BN8Q3JEwY6Nu9W1COBz_7JWtds_bJfEuHltUyOkbrHLi6ruPanWHZ8_i-UAFJi3KXWPpjhdJIHe2WS3FCtIj3nni1a5owFUQ-SLyfCd5HMPJOOor08fN-RDCXd6shx35kLi4XE2iCkQOstc1r0fU5AlWqkDylXlsPqI5UycDO6Nwjl4EFRw6nt2xAT1R8hV12bL2zcH7A_Gd87ujpXeqNUjojUd7uZsUOF5nWnVTmrACUtPfFEKRhpt_Pj1Jyc2pXyJaf1B37WeyZXDB6RUsuibDvNBT_ZFuB81CpoQSxZxRS5cUC-UaQkqWlMGhMXeQt9YmgjxSAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 459K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 10:05:15</div>
<hr>

<div class="tg-post" id="msg-25736">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8e4998f7f.mp4?token=VO8HMxzJWBsCctLvx5tqSGwwqXTsp-a1uILpCuFolVoHjoB5cRQ0gqgpN0nrB-BI2VMPxbPHxSGjQRcJdpOBoWQcTem05o6keRkPJ_Wa96v-YAAmhh4clqw_8Q_p3ZInQ6AjQCXgU701VlJn8lfpuzJO1T-Ih5X5GPqdUyEz4Onwf4ipZKjqgSdZX6-vFw0kv3CPoM_j9jNIG2ymtIeP0wEeEytYvVj1jGnxQEcazgn55l_V5I8A5xRFUrlkerPODst0FFvrKeNPLxKTSEbO4TNQsAOpIlX37S5WLZB_dIZAkOgApG9oWVVSuubxM9OWduFHQxMc_hJYDlngFYD7JQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/persiana_Soccer/25736" target="_blank">📅 09:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25735">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CvOBbOZfBTWbmpeJhPODZfEtupRRRFqUeT3J6WG7kKC9sNB8pSJ6vyIT976TGTpaYw69mACJxL8IrZdNxw4JwW3RBAs0zQ6hg_6ITtrL5qg8UXrmj3ziIOoJvQaQo-Azv6KockadoinxLjd18DBArA0F0H0GUutadzfZgk9XMWbq4bY37HOy-K4ZcL42ondJHJ9skgBs2ByhwkAYhqhwW7GXwvUQGTRTlyJxuhtL-QUpw0RE-ArNVahDoKRedLbJdKqxFr2dMgvlWbB9xx0kpXfGfdHlmiECo434lzNvOSroT5doCMVnFYPHwhNEQM2pB7aZI0cUZ0Uc3FyLFYakvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضعیت‌بین دو‌نیمه فینال: بیژن ویالون بزنه شکیرا شیک، کی میخواد جلو این ترکیبو بگیره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/persiana_Soccer/25735" target="_blank">📅 09:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25734">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n5a_Fz6mUt0mH2M6SH7cr0e7KP0czjdwgiebObXnVysctzWgTRMXGtrjNG0GI7ySx3li53T_BP80qAfuL-TWv8NwxNpRuV681liXNUcTs4CdKDuqiBt9mStEEro2cAMGOTDyTSdhiRK8YR-2Jlm8NuZwQa8yvjUBHJYFhBycSmqqGi6eXe2zlPsa21wtMmexMdlRa5VH7AuscLZXszUTaejLz9qiraXI_KHXaIEvzOE6IcoVFa5-q1eWKoGmSmETuPG-k4qaUpOHxt8wMkDgztKvcdBATpjesajUJ90BlvS06VlMqJHteZHbu_dp7TSzySsUfc_Jh_iUMK83LR6ZFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
گویا فوق‌ستاره‌انگلیسی‌ها شارژشده؛ دوس دختر جود بلینگهام: فردا یک‌ورژن‌جدید و فوق العاده ازبلینگهام مقابل آرژانتین خواهید دید. مطمئن هستم جود میتونه انگلیس رو به فینال جام جهانی ببره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/persiana_Soccer/25734" target="_blank">📅 09:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25733">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0f3f3f6d3.mp4?token=Q47ubYABGQhgijM8wJuVrCXLKG3_TUb7pdtpsiCMfvanBEevqKqOZ8RGPt73gdb4KCtvVrzHoIHOiTU5fUvJ6YBUygkDa0O4e1IkaJ1XO-bmOw-l_dCQqW2uKjEgxE_KvCn8K-kO2syQMGBna7oCdVDCekwUv7TJHXZFuy8McLxoKf9hqjJc_zH2NEFCTzCGvjV266F68ob0IaUtJbO943QJ9fws_frPI-nZQgdDkqa2rX-6EowvhryAuX0OZyRR9G4mVXZp8G_QBVZ2WC3jVeOeI-PrXSCYBBvNdEnCmeZMaL8II6I7l9LiV3Tk1Be1ku8_aoBM-riyfx4Ekb-we0aMItUYgQAgBj_E1Oyz_pbGTDndFem2hxWWKGziLIIa1RJtGWI3lhrc6A4hRj3bwtJXBQ34czDC18V7QCrvKKVnoI5zEX0UFe1lLFQzEISYOQJbSqJGvq_5INIV05hGrmBz_WkjUhmEsGnnYPo_-r39aqX19YNAQ7_PivME4Q1yokauEcmOAwt-HPKl9xkVLC_HhmFCt6SJ9CEuDcQ17Ftz369kn3fr6D6TYXvAwWmQumPecyrlRRdVPc7vDS4MeyF1JvCFEbu1-0owKv9HpUN_5yNazYtDjXsgmphd5zd9qMb9zP06n-RQxlYcbcVyAE5G6FYnG7lO8zsn-l2E6ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
ابواطالب حسینی در برنامه دیشب خود خواننده آهنگ‌معروف "جناب‌سروان ولم‌کن" دعوت کرده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/persiana_Soccer/25733" target="_blank">📅 09:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25731">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b512fOGI-5V7KbPwI72KeBdgI-u-VWldwKSUuXmHcjqbL_MXPNLg-P7wB_LJgDjn44qpYSo_R7lSWan6hvqQc4GnbqBsexfmo9w4zxZ7XLdmT1ZOXL-HzktSq_HOulvdcZ8keIEntM97lxQxugTjRYLRgWmMT37rp7FEpLrvntArAs4hgyOilAvltbe71Om5Jr-VfeVb6YrjMsY9KCSxq5dEz4gO3RJDiNfShr2BUo1uJr9OIZ1TvEhleaH0f16tbwodpWLYOJwSfI79gezKIyAiPNXgt2_gHaEcQ9Tk8HQuQEog0KGDwz6IEWO6fU9hgc8Au1OAzTeDBkSAP6m_Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فکت؛ تیم ملی اسپانیا با رکورد تیم ملی ایتالیا برای‌طولانی‌‌ترین نوارشکست‌ناپذیری در تاریخ فوتبال ملی مردان برابری کرد. 37 بازی بدون شکست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25731" target="_blank">📅 02:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25730">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oem9qpJOtXsdSezFGb1gw2DJXjfo-xTc4HGH_Ot7rODoD3hDquVFPUT38cR3uqQi0MGa3Et7sgyh4e9kIG1VZQMVpM3NCIR9J5Cgj1etlj5_AJXYY9ZEwmcDW1dbs508ih0SGrdQQQYbqC3OeNwpJfT_Q6zvVnOWxW6U2c0ywUFkFDpmUyYUGQR8wTr7WmzDDOdnXLc36DkbFjdO0QvoudZRUxDHWhx3e1HjOQ3t8mV904Jmisx8iGsG9gfVDnCl_rkjklt_neTCpVsqI7x3czgrtrl7wJwz6aSrxkeovmH6W6iWAorZ8UZpXcav3zwBD9laj1DqMVJObi2TiGUlJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درسته که کیلیان امباپه امشب تو زمین نتونست گل بزنه؛ دقایقی دیگه گل رو توی تخت خواب میزنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/persiana_Soccer/25730" target="_blank">📅 02:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25729">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpxoPMK5xe93eWcMpICWYARTqa73n8hxxVpaL5QRu96qAjDP4LEQ5thHCcxKhFjmTBwngrrAyH9nEl2ATQKa7PYMe8NWGnkKqn77D0IgcqQDMS3vElkMrQjrdUsPhwA1tS18bXek5urmolJ_3QNaJBeuk59C-C0fhSvFV_1KqoJez7__4O6Vu6oosv5q5sdDsVpbxT2EPv3_LsOLZT-f4KPBldV40aJn70FBTHvECAcNVqs5Hc5Vkub-Sg5ShaU-qBEc5a5iBw0o7SoqUSa0N8GcfSWrz3zfG_Q82JR5XSgeQWMyjA5mVEbFayNQA0GdzxQ-ZGfhApXfRYFRWviZlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
جود بلینگهام ستاره‌انگلیسی‌هاگل‌هایش در جام جهانی رو به دوست دخترش که قبل هر بازی به او روحیه میدهد و او رو شاداب میکنه تقدیم میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25729" target="_blank">📅 01:51 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25728">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJQ34acsS189yaWTHx1mOYY5gJbhu5nxxHGQ1NDsFAeqzLCgK99lNjcZgz0jeIep-xdg8cxT-XWrvt4CTOCwHlZqHL0SWDwLaWEedMpoBb_krfX9Z-_QGG2E5QqjVihbxg3GKt9Se844HUknXYjfBekDwdkRjRw2HxhsNIyIVTHotR59NQgwneP2gE6DhNxl5dUN19nugel_gF4afNhuV2f3VloYt-lxqIeXTkcksGeunV4j_SFkNscHuBTO0HDl8U7p53_ktmxyD8f6XDnNTywFnbKeCyVBa6su-ff-V3xl4lTvjKbLQHSjc9pYCkaYqmcxYcCfCtmxcPOPWVYVhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.2K · <a href="https://t.me/persiana_Soccer/25728" target="_blank">📅 01:42 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25727">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/50f8c52913.mp4?token=sCEL6Ghu7jZam2EicwhkFdH4rdQpxTGk-YPS0RUMUr94pmuh8zo2LLhbLm7SUnfsV2MhI30UGo_cmebZqM7wOju897gnoOS6FFFCQSYcGfJkkFKdxqAFLqTDW-vt8DLI3sJGDBnpVk5nz6OmyzILl_3ICySUVTEb8d-UDPrA4Iy2yBB4bojSyTh86g6mV--5-oK8n2YmSgwr3dF-FbQ1KQkYdigk7FN7ZQEEpLZB6ebPnhLLbWPFUJEPsgx2e1RAwhJwD8PtqT_OWVA2YFNWaJHJwuBJZnRGTtrQSWbZQAXN3cbmwPDCV6HaziJZXo5gDJDQDJjEM1g-3FJLUZv6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آقا یکم جمع و جور تر بشینید امباپه هم اومد:) فرداشب یه ستاره دیگه به این قاب اضافه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/25727" target="_blank">📅 01:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25726">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGMHT60lXFwxiJ6BYiC1U7KnpCUBUHQ3uUocKZwRAqo63O9LcQt7C28suwii0CiXl0d_hVCzWOV7Gm3uQue0yW8g-LAh8OYvNjN3xMErt38HpCB_uvuefiNOIiO_xLiKIcgJ-NO0ZzzThe9Skk6e9dcp-tWM9L-ucJ_cDFNwqk359lTgG4EyKrs9c4BZ-53IgE0LMBvGQaP40nIM8rNr9fvai1emU95vHA69TEK1ApqMP2Is1h39BkytJhaFWjYYoGwAfWD9-E3-OW2DzReS9HJgv5oprSJI9PJlc9g30nSFJr2RrwByZKukR51KCMQ7JnyV_AFILKawd023uZ13hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇪🇸
🇫🇷
استر اکسپوزیتو دوست دختر اسپانیایی کیلیان امباپه امشب تو تخت: آخه من چکاره‌ام؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/persiana_Soccer/25726" target="_blank">📅 01:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25725">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W8mBkTBzs-Cgph1A_WzXP4LuBYWeaPnq1S9wNDz-CgU0vPf61iK_sVAFxp2RYWOoq_R75ft-9C-I_5i7wHmIzqR53AL0lPkBOeR4nfgLrP5-id-h9hxWfMxxGYjynjegs-ODaGSzjTBqzbgoIo5RLrEqsTPjSCtvKGvsBNG3KknxNVkdMaVm1samDfAWJwEV2hLZmyR_h3er9zOn9gMwugbFCyKUpDk_CEAjwDcho-zReZaBVxyRCmdD9-iwcuXhuvv6c15b_U_IMgejRGPnSsadExUAg0Jda1VUeBnUVP7rU25t9NCQ4YZpvITo8slWLTmN0fnNyb5SvEf2zREzDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فکت؛ امسال سال‌ خوبی برای دیکتاتورا نبود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/persiana_Soccer/25725" target="_blank">📅 01:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25723">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IlEekSHKfllcM7yk4G1FZ8wN4BFLc7nFVTfOZZhsMu9khEMXp6infbqSbISxpISqYgHfMI_lGxLi_9Bi6xAY6fcG4tXYTeKc3blr5aickVrXUvZ95ZW1gZWaUVxMCObpkxvJq1fVrUCAiwfIXrro580WuEwQbTmr16zm3acoT7K2NbOaEJej21ebWGcElnKYbGEXulam_KMhge7u1CNJPVWI79EQ0eLSpx12d_B3vo20StLScfgu9BX6n54zyQeM_ntz8ftkdPXg6JneFNIWtL1OitJ3PGSVjnd6q0QX9FV3hDBvtRKEluj8-azN6QpsSk9p1u1mXukDlovj_Y2zVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dH-oJtKIele4S4cI4AmUOh9ocUZ_ZO0orx2rYKJ33cmli87SBbT3-QaBqlXJNiyvKQNncCUp-2qqLsZNeVT3Dcl3vun-qH7jldQ0SIVXUAwhgGSZWLTHs0tIeh4lBqND35AL9xu0_jaa2tj59rKg4azG_4Zq4oxthp6cwVBtgGormAY4B5s8sAhe8C5SYbYd4n83-Viks4OiL88u17pyX634SSmpwBIp7jLdsZC7iqliTeXY3GZ1OmDnwoZ9OCIdRM8Y9LO-CDJMsw9qfdZ2CMuQYiRFNhtVonASPeIoAqyUJB5umKe5SRDryyIMrew3a7xZ8Twk517EcmNqzmjvNA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">Voice message</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25723" target="_blank">📅 01:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25722">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R61qpiPap0R-u2vpbNVVcAZY3pmuak5_4-Pdph3F6LgbKexJgigLMGT5qkwchXF2UEsf9S2x5yegCuthhFXid-ngJUaWDmPvhVBTRAJwbe74ieW5FnA9iGzHbvzdwv4qdS44gFQoRJMnZYRCFWGVJNDxXGp383hYgTi55N834vk0qTpmXRo5TCYieAuuyslVJU0HYbmmUBxmYIdCzEpExa-kNO3Ho_lc8NzccIo86surYJXAOIdqZuPNul_C6XojkoeQILr8JPJSGjiiJe8RUA3eu954nLCtifP7kw32MlbxDgva_kcOuBysyAw02eam9iRWOpTH4sKBgaBlAv_-tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
جدال تماشایی انگلیسی‌ها برابر یاران لئو مسی درنیمه‌نهایی جام جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/25722" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25721">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pt3LIVuUh3ZsjB1Dw6_8ldm3JhYeeXhgrbh_ps2UZNZc8P9Ixlpj1JB8HkKM2Sz05iLStMHecFsFTniy9YUOiboB3bM_-zz4oTUW3Sf5H7HzmEySQ0GerAE2Hb8pMNu5YzztPEw9rD1hHnRxIBaNHdHt3h9Nu6wDXeirsHcyuZav8EuB1uPodOH81kIEb3oLWEeD4jKmFExyyc2oTWPAYwdrAKcom7zVHLXPjDjXI5lwBCj3QxQrE571ggTin9nNtZvg8gmWWI4GFMpqi98hwbqrSAhUupyyVFjeDogh_LA1YKVRe9GdJMs0fghwYcx3klJPLhqU3jfNB2BPDwavEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتیجه‌تنها دیدار‌ دیروز؛
راهیابی اسپانیا به فینال جام‌جهانی با نمایشی منظم مقابل شاگردان دشان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/25721" target="_blank">📅 00:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25720">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcyB35bvZu9XHV1vhMX_fAiy4K4h-NWllhkx9Qx5Nd-fS2vcqAph8rtcNgjrmDHxf1nb9aUVfHxvhKmSMiPQSqG4i7lw4KY066B7rYtosQQSd23n_2zpmWCIdt6jHMRoiAckqfjcbwSOYVulmYZzyNyx6vFWaWCdTgU_kjUiuRykD4A3pHBFD2ZM6Xw262veA3sRiDOubULrK5mqBMjewq9HX_d7xAt2iK6BXgOInTKQ8AYGctlwsUqputT2SZOCvFUqU4SVfQqsheF58yFs7XNP5rCAjDiLXwqqqvYiVdfvB8CkUHlwnboA1sOg_C76SuMdIedPGP6x02_FNlmjUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
#تکمیلی؛ زین الدین زیدان برای قرار داد 4 ساله بافدراسیون‌فوتبال‌فرانسه به توافق کامل رسید و در پایان جام جهانی 2026 جانشین دشان خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/25720" target="_blank">📅 00:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25718">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RiKVeqflHnqx6S_JyknpwZnblAolpZ_IMm4LWD5nC9ZB6U1ViZzpfPtoCuARES2whKSG7xkvHupoWJJ7nngqOWtes86q4iaHqpSK3n48OvjWmnHiz8N-u1ZzrnFtXi14lUsafrTfrqCN7K3SJ-rXJD2p8_eTbkVQXTkQNXAYmRpGkb-vyaPUQvimyIn94m4Wp8sQgsfr43Cgf6Xpe3wdO089pxZUUATqgB40Gvah7O2MOy4n-DQrLp6uv4g2zU1raLMTFTHrA0f0D7_iLHEhjmkCc3BjJjyB8m7PSzZlHvceBqktxKJ6SDHkDaUUkOTpXqS4rCCJr285NtkON5KuFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OG0ySUQPDFlXak4x5S0Yore-8E57wvc5oz4Y2nzEXjsc0dUHmlG5L87KdgOicIDckR4otl4fL1G9LEXB0V4JuBoru3hywGV_9h7ytUlWxS_rXYJLU0PQuGYRcIW7veiAfBWZDOWuT3x9i8fn0XUK6fUsZ9gKZ92EpiZyR67x46yGMCLK93Tk_WZ0z2aG4mA352l3WcwmzgfbokItmDJ8U71eRsItqGC1NTojWlmb75IyvFSD1PAX32ejIXDSAqRcX-KFBroR-i75KHJ1e-dTSLLJBQd8oNSTBkV20EE9CIC4k6vSOcazr-jFYke83Hgar-6v5ICl2JsF8r5Vxuur3w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/25718" target="_blank">📅 00:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25717">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P8cdOqqxHgPT4CqNs01bxwU2J7mfRk842DFPuSUTUS8F95-InmHCmV_D9IFEgyK8Upfnj7yMdgjlcu3NY7iE5su3xZ-GNYhhZKIhoV3LyaCTUQPgvBSXIENpAnWLPrBUXvO0Tnih9MxOkUvRvIcfK7slCfnCOuu_RgoZ-Ms4rFdVwHOnUxD3TiJQ28emZ4dxMvwzRzxTE1aXNIRzs5is4z49a95Uvhh0xxINzh0C8_kdP0M-RyeTjXJ0YMQr4RHKBJUjWBTLL_aEGkva6AbhcLR9x4m678_Hxa2jvOCZEqbW8tXTO3EqabyfpiHIohcq7Ihi23gSdCuRnRUba-vx5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ پیروزی قاطع و ارزش مند لاروخا مقابل‌یاران‌کیلیان‌امباپه با طعم صعود به فینال جام؛ دیدیه دشان حرفی برای گفتن نداشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25717" target="_blank">📅 00:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25716">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PDQTBZbd_BrxGpQkzRm8JLY6Boy67c6UK0DFRn3OYcMwzsneouqGD2JDXfWwc58RFm0l422hR4KWQB5eycrZQh1-sCuExvt5pOI6vSLbetmiUV-pR1v1RWrrvdWSePZTyzx7vVYf52Odh_oihiu9wN6atWMiBvoiHfXLXArn1l-vGxtkRHeoZSuWEJe9WvED8lqXQLKyp4vGi8MkaUGopYEqySMyec8OiD_KPAk4afk_O-oSYvCFFvTghiwjnGfhzEuBTFeHdFsPLk9Oqkh0AeT1YPh2zFq-jPQvspmsSQED7nn-sAw4qmVfGTLSV555pwSqyiF7WtPmJLrgu0qvLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/25716" target="_blank">📅 00:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25715">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D7CdIG7FtWFB-sgKlXwG_deBgO7XBCaZvUFjKwWOooxYWtcLm1wPWhjHH9RkyaOgBDpBYDuxcfC8LUN1eoklXyCZa3hNOzJykNrJnUOp9cZWaeDzTDB65AW-9G7hYElCQARgGS3g3KmUGMabsTNkY5TPIqggrXrC5SrDvEH1C507hWTGPJr5sEXWF9Oa77Y25UQ7APEwDp53bgTxhQAtiP937hqlKE2gks9ZtYWPmuvW6f9tdRAQicXygwPslXcU14KPGnuS_z0OZrZLPL6vM1uhoFGlpbSzEMoLRGYn_6V2-xuTieEVoy9TwQYfNPt34SBBVQ0mTgIvoXto-9ZJnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/25715" target="_blank">📅 00:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25714">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVCnBdSGyfz9SBe1g70_UQJ7vvYNpo_6nalvnGozjj8YHZQwYWJJdfQj4VRgwv2g_0bcc1GIp_AGUsI0GEqkK__n61tHtEfzt5LjnW3Sy9Uaf3iK2BHyAxRdN3CMFqAjx0rOhT4GFHBPpivfDOOc_a8pvododuvzjuBcsMhfvgledkqlSeRJ0DqAT4S2fSGMjKRyA-51fxeOY8L00u4cJTpdggMYbpljzK7YUFgeBW8ArYm5uF1n8bdZzPuC2BsqMfvNvcVUT1LsscmJQuuq015hG5mafkCClT0uhA2y2znaRAQLVCZNrzyNl2bhAfupv0VzOgVwVS37dbb5FVNRMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
وریا غفوری کاپیتان‌سابق‌استقلال درگفتگو با عادل اعلام‌ کرد دیگر نمیخواد بعنوان دستیار فعالیت کنه و به همین خاطر پیشنهاد کادر فنی آبی‌ها رو رد کرده. وریا میخواهد سرمربی تیم لیگ برتری شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/25714" target="_blank">📅 23:48 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25713">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vct-i5wFP8bD2Z_lRkGsP0EwnTss3ur7snb6IWMc-Oq2Tk3MpHE-71MjZJrA9thVyN-NbmCAoTVcfDtdSSZ2Agfjnio9YDeFPLlbuZGeuevO-1ff9K7wcOzDA4TLqBJxNQLpTf1kR_a_PWzXykazeb2p0HkXxr8iCCEstRuBmhbrUzuRMwCRqp-qW_1QudNbHRMM_gQm_hVAWKj3qGDgmaW9hS2aA4IMnN_Oxe0TSgHYnoVd643VyiII0N3URuyYgZr9b_YDtuiDXQLq39hPxf_WC1YPj2eR-NSrs1g_8kUxm0KNpUvwtNwn6IZlwiQjKhS51R8IrMxTiPsQUXp0aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار نیمه اول دیدار اسپانیا
🆚
فرانسه در نیمه نهایی؛ برتری نسبتی ماتادورها در نیمه اول؛ رودری با نمره 7.2 بهترین بازیکن نیمه اول این بازی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25713" target="_blank">📅 23:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25712">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI4_h7lSGAvgX2ctnn6sbtbWrkaSydQR1lt-dmdHMXiOb6gzfEquYSvSykT6btRqTHmGWcBfyl08LPLYcS5BfTaFZ3ELRqBTcXiIwtTjG5TB6rjFcvWLJljtAs2iQ7lRokYlTsPJiworUB8LR-L2c8LR7xl1ok6tXs-qsROVTLWuWSEG89RfFFOjU0QVjnXT4M_9LofuAkmDNWdCW_TDPNDn1-wUmK-mY34sXUhSJ7PygWpKQY7KoxIPT7DUH3dXv3vsd4YRFcuwPSzW5tzPaCNlbwvaG8_GhaE5SDKr5wz-iXrZt8M0k77aDuTUSK6m9aAi-jbBRR4K2yX4-Ut0Lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/25712" target="_blank">📅 23:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25711">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SURVbIs-qSSe-4CBisPr8IOj18RUTpdvxFg42Q8aBIBm0lGnOgVVeJ0R8GFJFzemgTJ74yPUsKCbbES5HJh7xZfWszAhTucxnrR_x0w8uW-n5C5FqM_JTLd_B0rOvR0DN8E0FnPK6C6uPgkut2WIMdP9hLKfek8m2s5DlLuEpTthh64aHb3RK_7uIR6HJIyu-m7Pe4HM1TAkYObZkEvMOJ7SHwNosGMoNYHMVgOQLz4VLehcxV3xViT6pwJII-gpDxm6QgTZ89NJkcFJhM6-WaZfJV2EjwAZ14-FbNZzUyNleHhoepDyyYDO3C_giYG-vdG80jflUsCSILeG8FPe8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
بااعلام باشگاه فجر سپاسی؛
فیروز قربانی سرمربی جوان‌ونسبتاموفق‌ شیرازی‌ها از این باشگاه جدا شد. بر سر مسائل مالی به توافق نرسیده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25711" target="_blank">📅 23:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25710">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwAhyv9H0f-VRc6aUm0RHEvEk9AlJdwbTBJzgQMZjO_kqaVqwVFn5EdNcQzX2doRCjzYqUcc13TM7RJnxF1gMTSALgPeuoRqPkbXs3-_0wAfGbMPseoM1iun-qDge0mLRKVfAXUZ58Utqs7woHfn8qDl9_YDWHGIGT_ncmq3hGlu-zCmn10yu4eW7gLpVUH7ySYpphi-On9mQGtNlDzv5hQQqcBpyeCe-vUmqlkXbwXDd_kk-qot8kaNo0lOVOUQm6Ewx-uCeT4CDQYuq-ZZPS6XLK01iUb3WDUEirFs3xwxYKycaJopP8jJkZaWZoiDqIUSCYc5j18XDn5-sopvYC1I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3fb85979f5.mp4?token=oPAvqlZBcj1GjAw6ldLW-XcQpegXeigXOLi-aqRrzC4hpYCSwzW4BdcjUOvysuz7UBp8_BxDqynkO-fMXnd8-Z8ap_UO_mQpeCVwqvVWePoBscu6kePFp3nHvyatO-guX0y_kxlpUsSCVZz7LQVOgl1KiYY7bgOfurG4JWRmyJ0Q7Fs8CiK_oQgOUvQMEk6X5E40ro65NWoZVBvyDuxKiM3jW5ygYwOphQr44GI7gwZzyTW39DEcezPGhObfy2VapXI5QPe2l967t1rturz6Gv8iV01cuPVbHZEp-nQAlTmSIobB4nSoT7Oou5fVhZxzUoR72292U2sidtjGzcPWwAhyv9H0f-VRc6aUm0RHEvEk9AlJdwbTBJzgQMZjO_kqaVqwVFn5EdNcQzX2doRCjzYqUcc13TM7RJnxF1gMTSALgPeuoRqPkbXs3-_0wAfGbMPseoM1iun-qDge0mLRKVfAXUZ58Utqs7woHfn8qDl9_YDWHGIGT_ncmq3hGlu-zCmn10yu4eW7gLpVUH7ySYpphi-On9mQGtNlDzv5hQQqcBpyeCe-vUmqlkXbwXDd_kk-qot8kaNo0lOVOUQm6Ewx-uCeT4CDQYuq-ZZPS6XLK01iUb3WDUEirFs3xwxYKycaJopP8jJkZaWZoiDqIUSCYc5j18XDn5-sopvYC1I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
خاطره‌جذاب‌وشنیدنی‌فیروزکریمی‌کارشناس‌بازی اسپانیا
🆚
فرانسه از تسلطش روی زبان انگلیسی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/25710" target="_blank">📅 23:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25709">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=X8aliGJimeS6UL86bfJTZjMhV8xWLq4fSUlI42d_4xAuBkfCr--jNrPAU-S0_gWNOh7bymj_epFt4g8T3x5sVDrLoWIk9QLF-gwpsMBg0ypB9hmgiid6fSku-WRFTriKLmB-fioSsmgTmtjgPUIDUOr-M8E-3DAIvYWQT6w0aa0TYjrLq7CknQ5kzicOxlzM5LSKIvnMeooSFDoH4dPF7xJFQ6WIeUF4M_tT2Jg7KgQKyI4fJeCqLXobk6OTJusFXMsXg0HUK7L521zQy9ouxp8vWIYeY-1xCH3U_sniAZBfhN0jZrwIVWEr4_lnaTKYHCl-I8-CyC8vFW87MQdM8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2e6f94a364.mp4?token=X8aliGJimeS6UL86bfJTZjMhV8xWLq4fSUlI42d_4xAuBkfCr--jNrPAU-S0_gWNOh7bymj_epFt4g8T3x5sVDrLoWIk9QLF-gwpsMBg0ypB9hmgiid6fSku-WRFTriKLmB-fioSsmgTmtjgPUIDUOr-M8E-3DAIvYWQT6w0aa0TYjrLq7CknQ5kzicOxlzM5LSKIvnMeooSFDoH4dPF7xJFQ6WIeUF4M_tT2Jg7KgQKyI4fJeCqLXobk6OTJusFXMsXg0HUK7L521zQy9ouxp8vWIYeY-1xCH3U_sniAZBfhN0jZrwIVWEr4_lnaTKYHCl-I8-CyC8vFW87MQdM8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
آندرس اینیستا اسطوره اسپانیا خطاب به عادل فردوسی‌پور: باعث‌افتخارمه‌که باشما حرف میزنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25709" target="_blank">📅 22:45 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25708">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mT9TePksLMB1BRH0d_IkCUlH-9MO1HtFRDPDyTRY1PoZbuVCLQ-UxMuZ5AuJDUupLs8Ws9pKXYJJn2JEDAMXgZemyEJn5G64AGpL0xH4m2W2BuSMvI6SGBCQeUgAawNCY0oLm5DE4HjpC7hhWuu8NnMMz5UytPn1_jQ6hVvSJ3GoxVJBzf7us_jZaYk7KHnOsGeurSvCaqvfc4tNB8E9pcSr4XyG89le1VBHl8I_uS3CnojCXcjKyS5wXARJFmYRpAzVePvODRvPE4TDD68XLyUl_EuQ-eiFHhb-IPVtVDquqXHJzuGUwE1JdiNLGiGfoUJ4WsqpaKEDELJitQjTlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25708" target="_blank">📅 22:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25707">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b12zcN-s4aptLa8HqIKUMN_tw0n5KCf2NwaQ9_qz5f1QBm1XIzWdvTbCMzu-jBg1UbSUl0SeCcbnuJqLZoSNWxTsTOh0X7GSTutaV7lz1W2eTUTtSNch9nmiyT44TOL-vqJPaBDE2wYBhVKg8Zq6av6vOn1g45NQDHSB4l1r6nPbFGSPrSI8kPVdTc6tK1K_L06Gsa-R8qSlVE9RVJzDnSLmIvvEwvgw27LiaJRdouEa8bTjtgbbwOIWHS8qfy1-MDy0mQgkBxpiIurOIcLY5EVb1lkwqCLJmFZVMLGhj5crOt9pUCjRcBeFk3v1OgJDfCvfTyRrs8zi4lr_NF22xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛ شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25707" target="_blank">📅 22:10 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25705">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Fg8Gst_BdCKSTuJEH26yWhWhj3VEQgLQdZc8_s7gfwXH5YKKa3Q80yiy5MRLQJrLo8RQr_jtabPiNIB_-uO-q68QBGO1oJgiHoOz8CS1H549rw9869coWy4kAFJ1HGcJQD9PzIvcRgyj35crfo5FVBvCfmToaHviiY8QkgMJVSJsD3SqOojLf-3vD0Uv1qtAIwqaIzpc3tuBgR-riFjdjfo_hpyKgWwYOlMawA4gx4AyQMJdq3FDTiGeRSZXV8m9mW6fk0wR51BZErJpzNyJkwFnBYWsi0ipYPAI7CV7YV2AEKRyasXtXUbFh3Ktnv0bGQjb241bCOviAkn0iiAyTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h6h_7xTasqZVTz4HoUf5W0rAjDsP_HMw3jmHYbdZ5eh00JvYp-GPyBNTVNe3IaSfUptKj-dPgqnPkLZnmLtip14CDsHVdpyMNsqr9xyM2qKWQbjM-acQDFaCYfI759IQzX9TRxVHbQZG8EG_6F_8q_7vBwd-_j_iDGPcgHzgMWWXG2Z30Pau9PJ0a9XT1y27FQBIwbhl5oImbq_wlJFYjKFMHiiE21HzTDLfu-_m0tR4xem5cvGwwGTUAvVlSyIjsztlv6fMZpm8QAfXrXHyiwl0RwQMp60UwI-08ox2nz-vkm7v2OTF_L9ABBi5ffbvE3gc2h2kbQ3YYoc7frKflQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
خبرنگار معروف‌ شبکه ایتالیایی DAZN که معتقده تیم‌ انگلیس قهرمان جام‌ جهانی میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25705" target="_blank">📅 22:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25704">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V00ZeuZ605uFEC2Tc_LoULFXNeZkHclLrXjQjYb1VltfpGmhql77Mb9-5fn9s2Qvr5Qxp5Z7VfnNsHP3VvXCBf3VxACNCXb5MMzfylcQh-IqZLZgXKP_Ui_2rGJ10wwSD4Dj9FGjWZMvEwTXYneWHxoKtxxiXL48-6dSsIzYOFdkryt6OfEPtrkHVZlCwZDwvSEkMLYmZpu9spby6BGm8aNFNbzbzDdbOZ5ObSC_Dqv24eR1qASY2c0wAp8XXuABKti9zqmwOo3P3oQo9Ari4d4LUQTLxv9gnhJUr_QLvIx3ZnzMZHlOXfAYmr1lyhcTyB3Uh4u1xwWW1D6gY0MbdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
شهاب‌زندی‌‌مدیرعامل‌‌تیم‌نساجی: برای خرید یک بازیکن‌دیگر از روسیه باباشگاهش‌به‌توافق رسیدیم که روی 1.8 میلیون‌دلار این‌بازیکن تهاجمی روبخریم اما خودِ بازیکن حاضر به امضای قرارداد نشد. پدر کسری طاهری به نماینده از خودِ او امضازد و به تیم‌ما اومد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25704" target="_blank">📅 21:58 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25703">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lm2XopEJvD94zTVNKfYlQV0MVOTam7aINfcpgEzlIqXHI0X1QItvXMGVFGtF8tVCbo5LDBfnQxPWwMbHh_Xd4BeaHbkzxZaG3jR45Yk1LM8ytYsbN3GkZseh_4Xc5YA8CPseSvfymVtDPBPkhOoWjPQGR6lBLCc9NgXaKC2y_wjU77nJUL1jZhN2xoEL_cayiqzljjzIe5WvjRg2hruZZebCEoKWt_GCX0EfRGEUQiE3udH9DU72mUMb0LBiIjbIi1mMiBvV9L4BH2L90iI15y_Zkn3axzxtqn00HJjLyk__5rar1Wg3jjjSFM8cVhibl7Vn8XXQFHBYrcjtixDlbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
طبق‌نتایج‌یک‌نظرسنجی‌درکشور پرتغال، اکثر مردان حذف‌شدن رونالدو ازجام‌جهانی را سخت‌تر از جدایی‌خودشان‌ازپارتنر و کاپلشون توصیف کرده‌اند!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/persiana_Soccer/25703" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25702">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cm9AYySOVWC1Q4g3jigTrdKFji-VkiYDp1hLJDMSS0S8s81V4hvcO4IAolrsBvNd7ydjcwfs8FjlH0wvy0mJfyhIGq63_HF6JmJM5U16pdqoFufDqjeNdx74krc-zclvsL15bbUF5vObb5hbxiEe6l_5zaAnm9FAy60J2PGYmDYOabn2rZMvquWmhHPTuIEkWkDiUwx-jBsiEidv0fzxhidmPmcDtv5uAtejYj1sDOosVmoGt0eMJo-hUpYB16zfV5ZF_cdf3Om1yh18ZG_9mOcf1XtoC_2_1hRShxg1ebELI5ltm7ZEzKetH9om6gaw9piD_D_cyGfqpbt-_QKAmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💰
۵۰۰ دلار جایزه نقدی + ۱ گیگ اینترنت رایگان!
🎁
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
🔥
نیمه‌نهایی جام جهانی ۲۰۲۶
فقط کافیه نتیجه بازی رو
قبل از شروع مسابقه
درست پیش‌بینی کنی.
🏆
۵۰۰ دلار بین تمام پیش‌بینی‌های صحیح بصورت FreeBet تقسیم میشه.
🎁
علاوه بر اون، همه برنده‌ها
۱ گیگ اینترنت یک‌ماهه رایگان
دریافت می‌کنن.
⏳
فرصت ثبت پیش‌بینی محدوده؛ بعد از شروع بازی دیگه امکان شرکت وجود نداره.
👇
همین حالا وارد شو:
https://t.me/betegram_bot?start=p7_r4EF37DCE</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/persiana_Soccer/25702" target="_blank">📅 21:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25701">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbB4FIRtm5WalOxlmTlsMAZCfLMmi51rfj2vQ35bzqilHdNz_FpkTPZv_JUv5WlFG0dUB8jT640CACEvdM4fqu-RuEq2gcLdaUPVKDAENHBJOP5l-8zsmne_i3cJ6dJkUSYxB4wV_1ENk-9G9NoBspvXF-dMyFSdphNN2Cl59p6BhDZWd_ejrdefAG75JGB3VZi-iYgLpY227O8iKx_iXuo_AFxpCYXnHebJZtS_ci8x409Myd6w0wBwAG_ug_0KQMPxlbgGoevtwYaZHg5fMIUE79tgaFNgBenqrkK3bBFSUfdveJpz330_tRqRNQyCHzxjn3kF06hIDqeJn3hCuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
با اعلام وکیل اسپانیایی منیر الحدادی؛ این ستاره اسپانیایی به خاطر مسائل خانوادگی "بارداری همسرش" و آرام‌نبودن وضعیت‌منطقه برای جدایی و فسخ قرار دادش با باشگاه استقلال به توافق رسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25701" target="_blank">📅 21:41 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25700">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hKQZXayWGWTBP9u7n-JekPN-lVm3pIvvU__8xSMhFOXXZqzEndC87aNaStSRL0k40DkzDqJJPCsRyizksk60Fs8S9MtThOTYeXYKjF--tD9YgFZfCink9hYZtA6A6MqVw8WpowwWLdO8B0VIAcQDPNvSNI-osWis3GWwOLg3sJ8BFAycuSuDgpIHL8kXNMSoyOXC2YrZsHD-E3vfe21vOzzbKyWPhZPWMp_ODkSwhz25M5vX7xm1Ocrp2upryQ9sNlzsre1nWpySTezLWSMjdcExBp7xpZkpLOgGANF7lvxP0loIW3CZRn2VXbEFHJUnXCx21apMLKAga_pfVS4Y6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🔴
طبق شنیده‌های رسانه پرشیانا؛ هفته آینده جلسه‌‌ای بین ایگور سرگیف و مدیریت باشگاه پرسپولیس برگزار خواهد شد تا مدیریت‌سرخ‌ها این بازیکن رو برای‌موندن دراین باشگاه برای فصل آینده متقاعد کنند. سرگیف بخاطر مسائل خانوادگی قصد داره فصل جدید رو در لیگ برتر ازبکستان…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25700" target="_blank">📅 21:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25699">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oQOHwmGYU3gSa-ge4YFwopBsyu2h3jGPTkwRhRzAHplBEHOXjxk-tX-WdJkEqsp3P5sCbLCdZRj7x7kNGDuq5N6PsmiKBHKKxUkF7js5ID8-nfXiSzX2edGLQvyOvz-l_mneFF3DdC8eiLgZXi2pwGbVA7d4gE7mNzmI-Rrzk6g1X0lH7qAgA_TCHjR-RAhlDH3dmGOhnOgABs-guGARpwmoulJwzsSdpwVn11oSSsaftAyejJU10WrvTFZzAxdU9xT629kOEG2xXgqGbqN6n2EWuuBz8aJ41SgoRFXjFQClWg6_GGNPNcXFN_Pi5EmBaSxGiy0QSOpfVe4S9KlL8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛ آخرین پیغام منیر الحدادی به مدیران باشگاه استقلال: وضعیت منطقه آرام باشد این هفته به ایران باز خواهم گشت امادرغیر اینصورت باتوجه به شرایط خاص همسر و به‌دنیا اومدن فرزندم نمیتونم باهاتون کار کنم و ازای فسخ قراردادم مبلغی برای شما واریز…</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25699" target="_blank">📅 21:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25698">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=UBuaglWEDNaLAdXzuEa16QRNQYYK4tifax2PtnLM6ESr2mNJrNXa9rZj3TqQnHe9Bo4BoYY5OD0dyGGS_RLp7_5jRm5ppNMsIWmNN9HExseD4OMLBKFPmN8uXdDitDzkWxiS0UGNr4O3yeCxKbuGhGykNiqmw4SoKgr-cWP7YT0xsJPFZHQzyFi8iaKpx-_pQNWTn30nouWSDuQ3zq4FBHRCDahGGzvyud5RWYkTBxlCeBg55PX5jLnJtx-2zf6PTwY2MYwudW9LISgVjRRviCG-jwTFEj3bZRy6BPFkxcaJnVCjMLwocyeBcKdAtFePIhyVo69GyE8lojA8crnQjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b34e61019.mp4?token=UBuaglWEDNaLAdXzuEa16QRNQYYK4tifax2PtnLM6ESr2mNJrNXa9rZj3TqQnHe9Bo4BoYY5OD0dyGGS_RLp7_5jRm5ppNMsIWmNN9HExseD4OMLBKFPmN8uXdDitDzkWxiS0UGNr4O3yeCxKbuGhGykNiqmw4SoKgr-cWP7YT0xsJPFZHQzyFi8iaKpx-_pQNWTn30nouWSDuQ3zq4FBHRCDahGGzvyud5RWYkTBxlCeBg55PX5jLnJtx-2zf6PTwY2MYwudW9LISgVjRRviCG-jwTFEj3bZRy6BPFkxcaJnVCjMLwocyeBcKdAtFePIhyVo69GyE8lojA8crnQjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇧🇪
خرید خوب‌کریک‌برای‌شیاطین‌سرخ؛ یوری تیلمانس ستاره 29 ساله تیم ملی بلژیک با عقد قرار دادی چهار ساله رسما به منچستریونایتد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25698" target="_blank">📅 21:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25697">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jf62uGHMcJ1Zyd7M57fgBHXJrLd5ovncv4O8mNMIZAtBuPzHp5lLgDuT6FuYF6S70s9GzsgVC9PQa5xQM7JLMZ0qx2_jpcPDe2WoDe-c7qgl2f6E8_GbcKjiKYRHyHAaBg-wasAYUpVQWfqageDeLAymDXnhAc3karyHevxoLkKc5o1HWl28uIxR0KeJ82bH-K1pWPM9Ts9NLTdvZltaaBw0apV8Y9w8BpnP40_ZbtkIKyfzkE8FYSxFG_Gt2K8cViomLJHMnXwrYzRtdPs2Izg6tsZgsyi5BL3jgJboMEcJO5gy9i4GiSO3Z0YI_zOuTzLbM32tvK09nE2cDRMrIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛پوریا لطیفی‌فر ستاره‌جوان گل گهر امروز از سیدمهدی‌رحمتی‌بابت موافقتش باجدایی از این‌تیم‌ و پیوستن به پرسپولیس تشکر کرده‌. همانطور که‌درروزهای اخیر نیزخبردادیم تمام توافقات بین سه طرف انجام شده و به احتمال زیاد این انتقال بزودی انجام خواهد شد و لطیفی‌فر…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25697" target="_blank">📅 20:57 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25695">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQWBAbMAF5-HVqPWIcXgmmDbPDihTrV2iuyM52-mLYUvgbzv4KWGZPj42VSoBBQtEDH8ZI0s3an3W8R5NvV9Xs1N5voEg4IO7KVo-cg08B-D11bDNSN1guOUUr6on1iUT0BvjVzBFbYVCH0e9mp0crjiukywPUebtwRLJwFgj3irBcvcavpfjIqcymc_QsaXCzAUGNK4kB6CWekCi8aPXhHMePuq1ICOweVjEgK0ciKQDC_0nz4MB1z56XKrHaoS2doti2zS_7WDdwIYSY2T4T43vyeih6IfXUiThug_fZBM_OFECAiTFXv1Z1uZ4eVlZ86J4WmH4VNEx9IN-aKf6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mxc_iNJvs3Gg1_n-YZLOTPTJIdkuZcHAm7V137NLmpWuFAiznZPAMzc8Tzof67egxAU4R_oohRTHxFU7ZLh0cZxAOIn74WPXp_8rfnDF44kA9lFGRcQX0nXL_YeatuwGgnTQdcxyh0xLHQ-JQ5xn_2GS_cXD7B3m4TeRDOngYa4x1Z31oSNvUIKed5hZVwhkp1bhDYS-BriY0xPtrzIUtcJ0EesNxmbNuL076aUuxYfztRF9bj8KUcdz275UtNJjLKyAD4gYVdlND5sfsCDXdW24ypMIC02lFwp25H8-c7sdJ8lHD7LNH3xNl5imL8C2HWeERSfQHDv1HBTu-wYuJA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
نیمه نهایی جام جهانی؛
شماتیک ترکیب دو تیم ملی اسپانیا
🆚
فرانسه؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25695" target="_blank">📅 20:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25694">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HKiO86q_cd5YiiED4varEk-FQtXZhLBDX71l-dcpmxvEBOdcPLJQMjpBmR2ESgMnyKMhYB7EUzgrxC7Pl41mAeKpWuIK42iPQkx_iSkfCsHaDHbePxa7nA2TSs86CdqWa0Tt1F0ccY3cjkHq46e_GTNaKp0LhEfEQJQYlt4AjHt104RXD8ki243KNscS-ZgFYl2EA80BxTyPGIUDkZqlx2reOiitZSoOMFQCHSnDejwzj3tveE80wV-48WhFgJbmSuZE1Bhn7QoZ-djAh8DtQ5BFio7vnnpw5cIfRKB16BW1Ogk9EGm8q8z0Imj38sBbT8y_7WqQs0P27dJ1gKxCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
کمیته‌داوران‌فیفا پس فردا عملکرد نامزدهای قضاوت فینال‌جام‌جهانی رو برسی میکنه و به گزینه نهایی دست‌پیدامیکنند. علی آقای فغانی در این جام جهانی سه‌بازی‌قضاوت کرد که به بهترین شکل ممکن هرسه بازی رو در آورد. یه کوچولو شانس باهاش یار باشه قطعا فینالم بهش میرسه.…</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/25694" target="_blank">📅 20:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25693">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s8mzSE6mdVzfsAkG4VOToq375MV0wb6_aoqQzXefAuv3XHUS_wWSI3_ZSZfSwpwSzztEaaGtb-BBcc7FS1nNWeXkQ7_PJPR8jn7i7jwdwWt6J5VvWtM924v_b77_CMAGLV80xxHyDWNPXRab23Rf1otn0ub1Qwyo8B9uczwaVhz0qlmbtN-mKY8ybHQVejW5RK0FSswFxJdlZUfrNoT32H3la2vl47nfQ-7UK0bHNxxYILU498URfnAtdQIGKsLQkXV31cO4dgaU7uAWFez6PHmb010Thh4PX4S3Tf954gSQZIwr2jQwLi4IVn3Qqaw7QJFTVAT2UnYz0BpMwbshQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25693" target="_blank">📅 20:24 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25692">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQuTwuP9LrFpz4sNCGjmcG_xx1Hz1birNXtzFKkwilkCrmIGtiBRU2WoJGGkdn2sPmhmlv3KUrXwGSP3WfHR4vJy4zYChHfFKx9nAprPjjFqTuylQz1tPSpfec2S36Zu7gnaKhv-B3pfbmm9TUwxGi7RNeb4LGhF21HIWGrdT1FHbsDSh0W3vQLKI6uJcIN0CC2SkAYa-argIwOkU5JljMypJOQ-EZfjcZZGJdlQkpRvClaAnknI70m-x9dd1Fq6GbTDx7y9_6fqgNX9GlypMa7f_Hlyum9bYF1BwPvirBwaA1a0hoteGoxzo44MbWeJQqXgwOuynTJvaYwQpKL4ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
👤
یاسر آسانی ستاره استقلال ساعتی قبل با ارسال نامه ای به مدیریت آبی‌ها خبر از فسخ قرار دادش با این‌تیم بدلیل عدم پرداخت مطالباتش داد.
❌
مدیربرنامه‌آسانی: باشگاه هیچ‌علاقه‌ای به ادامه همکاری دو طرفه نداشت و از قصد مطالبات آسانی رو پرداخت نکرده تا او قراردادس…</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25692" target="_blank">📅 20:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25691">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RxPDoMygvFzggMHKNfskm4T6YocC5sM0QvZtHYEvjkFdjJPX8SZUGWtSYYaFkKnQMLO7UjCHVquKor3jbZcKiQIsd4V1gk8_7xe37trcoZlBW0PbHMgU-Y4HgFuIMIxoF9CxpCBeoyPcfENAewEUAK6zYhqu1zLzwr-aWSnW_8L-B2aGYEqXqhffS_8wQNLEW9XFHDEAAZmsEtnnrre6xLhGKAdnZwm_y_lc1LodBl_kZeh-VsfxL2nimHcmJY6weBMTSlqNbNH_2XhNVeMAmiLxekicOhUYi9IyOAJhajToZ_XuPQEsV-QzI9mTb7gFAWGVYqbF_fAE1u3zrglNrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
رئیس‌هیات‌مدیره‌باشگاه استقلال: یاسر آسانی و منیر الحدادی با باشگاه استقلال قرارداد دارند و به ما قول دادند هفته اینده به ایران برگردند. امیدواریم به قراردادشون پایبند باشند و آن‌ها رو داشته باشیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25691" target="_blank">📅 20:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25690">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">آخرین‌آرزویی‌که مادر عمو پورنگ داشت. فقط اونجا که میگه بالاخره‌آوردمت. عمو شما بلیت بهشت رو با همین نوکری کردن مادرت گرفتی خدا بهت صبر بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/25690" target="_blank">📅 19:49 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25689">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FyTpXfVLIG-olxwH9Vj_nP6hjqPtimwqIe6sdZ8Kf8wiQZi-VsuUGAqETkg555U_cN6PoxKDAlA8jzAYsAiEAVkjY9x67gevG5cvxp3lGWsJSdHEvCzjF7EKJCAqYMbEYTCUgXjJe0XnF8Vdh4rm7lkyiHN-EXg-YEP9rknagV_zQmIB4Cq-D1Vv5LivTuvG95YmEYQT_d6OknY0HOL1LnngiG3ph9Wwpor8w4eEekozJ8MMBapWjgd9G7JeqJwtnATjkQwJpStkrgFhPNd4ix7_BZHX7CUzi0JJFZVymKjrVtgymRX9jzSDqG-ybWen7cA3vc6VON2npdXYIxXYgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/25689" target="_blank">📅 19:44 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25687">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ_dQo-OE13vb_MHq65z7RchvJum8LVM_n_IjQCujmURzUiTQLXTnmNpwYORDOPUtkcJDhIzcLHlN4cYPS1oCDAOSh0rrH_m0BTvFWOKsJjQHwImGG_zui8NBYcHL8CSdRCgQmWGIxOnf_qhK8xUOlgVBui2z3OswdDYBep6VDSB0N4CmoxW66B_c1nt7mNyNqE47NBkPIUD4LZW7pdUN3H4NxNwXES4XgjqSgBf3hQtM_CpOAMUEKbEK3Y2--W2Ff2FHwVdHZha9cUtdUMfFB-jENtnuDCrhtJGDmL7Xf3bF6_WEQTfNYeOF4JArn6cpB6xwEF5Atsuo_kXbzY3MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bBOGdmCo1Ga9sDXB1XuGY0GbYHD1lQR4HKP7VeqBHljw_b9i3ZYpO1MVHAk0L_nF4yyXEbj9HlPX0cWLxj6Hd8DQ_0mm5AruegwSTNMKiYLTDTwIrGX-4xLmRkJ3TOKpYpr9185cYsPi8ucvGVGxRiOoM17tq-TxRA-QkIVcXRZRdiS-x6PsS86JJ6VuvGBf4ngIg7IocXoSTm9_wM1iHkBaBPsUPADD9N5GXRWdaCXhwbepiwpRDP9ZpSzLCCMpowP_x-hOpRq8iwP47Fxb2wvtSieQOxvq6KzROZWxRPeq2ZY6Hy74J1GcqLOni7gZzi57LFTf2oHKegtGCyx8eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25687" target="_blank">📅 19:35 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25686">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dcqFbYHB6kx9511HX-cc4ypDrlMJjRcSNaonmF2iD_btTQK_k1oCVzcVDO39k7SHW1umLPuqh7bcpxcjkFM3cLaFHETXYo1UWRvN6qpvlMW9Z06AUfdACvcQ8Ef-9CDlIMYr7Yfae06EH7HDFu3bPuWrTQR5R16XtuBqV6AISjebXoyxcpZpvQX0sFOYPUo0ooXiwQupqAAG-g_v-wToRVTKu7l6hXKbuldYA-cS9FqwQRP4bzQE1REVy5Puvlz0KrOy_qa6AIrD272oSXKcnRtiPCKQIp_-MFRBHwKzqVc3GB3i4RT8DdxiooGDX2X9IVaLqFAf6BvPo0X0qz6wbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛ با جذب مجتبی فخریان سیدمهدی رحمتی موافقت خود را با فروش پوریا لطیفی فر به پرسپولیس با رقم 600 هزار دلار به‌مدیران تیم گل گهر سیرجان اعلام کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25686" target="_blank">📅 19:26 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25685">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tV7EqIe20AKv0KyxnRVF1v9uTc3FBnR_okQVWoAOwjd9JhVLkfUfl4saIsUhh4gYfoQborVuseNAV0SoayfV0uoTUH3FLJ4wa3bxG-XB_2PmlO0F9RtHq9YACxLDvkZFiVtOiPE4HgzYqLz2rzu8IJiHO9tyX3k4W95DJR0dW3RCC48lRGMmt9BLitCpQnhFCCczlfmA_mn_YXFFc0gqx8nb2U7BIrxtbxxgZ-2c_gCqk2riCkUDcUlctl6FhPyG1HrSjXRQGwI6mXl0OIFJGZO3ytM7W2MjH_Fpsl0M4xzsXpjVoUWCnU83SWcvgzFvorJ-zLO8X7FLDXd22vX26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا؛باشگاه‌استقلال علاوه‌ بر پین؛ با یک‌مربی اسپانیایی که بالاترین مدرک مربیگری اروپا رو داره در حال انجام مذاکرات نهایی است و به احتمال بسیار زیاد با او قرارداد امضا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25685" target="_blank">📅 19:12 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25683">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RElDTFQG59OF1AsNHRWTfqNikQVlT3X-g7jz3azUtc5tECy8LDMeukHLymQD905xfFr8XaolqifT1C0G8-e4k6b0s56nitk3PQ9UhkNtbx7rjWW8_uJ2N3RBxPaRhYRnzbhrFfUGbnZfSAlJuc0NzWjmt4-RkO720k0aBUKsqHTtbsRLxcimpKY4bk7OSEKZ1sybt2h6NMopYRXQEwuDR_-oI7UGpyDjgyJXWufDIFXKnysXFhwm3Ate-sIuLoWNSyM4LNLznQhF0N1UqAgr6eryI23pWVGFmn5MJXpFmhporFdpcygbxqLO8yRQObLc0o8J0gRV7CBwpTf7ad456Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Jue--wQ8CVpeF7Uu0LaSUCG3ipRulg2MROLZaLSiEyaYHm-15R5txZXk5IHIltjvaaWGPE7Dvmn9SSLfSPqE56q3MOrgpjhHVO9HenpofFLia9SBzvLDPDQmQgx9H8KzfcEw0E6rCtW3O9aDHuUvgrqZFL1hlQ4OYfSH6DCmkyKsXtuQaYTiOZEVNqFclysKmkcGn4yaUDsRwNIYsbylg3K1oIxGC7r0HTj40C19Mn9bsI1IDn-N8bRiKEEkZ3EVIlIFtr1rRz8R2k1t0n2pMjyLXu-eY4YCv4U0uOYM5TLxpEjcKQCMG7204JYYUkzdZHPUgFzyxxltu6HtWG81TA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇫🇷
عزیزم این نیمه‌نهایی جام‌جهانیه خیلی مهم تر از چیزیه که فکرش رو میکنی؛ نمیتونم جلو اسپانیا از عمد بد بازی کنم چون کشور توعه:
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/persiana_Soccer/25683" target="_blank">📅 18:46 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🏆
40 سال پیش، بازی انگلیس و آرژانتین یک چهارم نهایی جام جهانی 1986 گل دست خدا و گل قرن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25682" target="_blank">📅 18:38 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25681">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iOJ1rdN8uFux-7dCQHh1q9o4ZDJsZ02MvY_YskGT8Z6O4Rgaxg7P9Un4tmhfcJqJl1kM-zpkLfv-DWCZP4OwXC6D6MVTzAxbXIi0z5Mzhy5n6PEfqJi-VROPxlVeEIipFiZhnAh2OYFNI0hrcHFF1EBGFUsUIv-JvAE4HzcP9iBxmxCKlxv5ylfzgGbNU5SagOeuC1hQkLonoWFkBoHtO-YX5BWNdChuz9iRS4ORg8uz8ZE0gZSq59EXwY8ioxziRWfklDZIL5mw7K_TK6KjIa8JSdbIET7SvgUk0WClFlnCKE_S_4WCeaGEONu0yCFIN5iasbPYZd_wL4SnhHDxQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
در انتظار دو دیدار در نیمه نهایی جام جهانی
🕐
فرانسه
🆚
اسپانیا؛سه‌شنبه 23 تیرماه؛ 22:30
🕐
انگلیس
🆚
آرژانتین؛ چهارشنبه 24 تیر؛ 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/25681" target="_blank">📅 18:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25680">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpIr2a-Lk7DQ6_G-vC7Hizzzp38nWq4cq8c1e5XsHjBEaepnA-ojjSV8XQdXeh7Qk-2aMIihzCvPBcfH_z7BkFSZT4o8tjtqUrBx34-wxjVB-SzcIH6RRGvjVwRvE6XTxO87MrcXAE6upMuJ1cfJWhpCUi5twNsnJy2perhHTOXRiVgjRPOk_e8Du0I4verP2kypo80PPXcg8TwdC6TTnop2ZZIpd65ptkuovlzPVephEJ4twTa2yLZVwzTWp3csZSEt7KFkan8D5vVu6xIgUMhLe11ft0VEIzPGQwi-hVqh45cGSACsKAH-OWJH7Kr9nbMV3SIoiEsQ3u_eVFsoew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
🔴
🔵
#اختصاصی‌پرشیانا #فوری؛ باشگاه خیبر خرم‌ آباد رقم رضایت نامه مسعود محبی مدافع جوان این تیم رو 350 هزار دلار اعلام کرده است. یه چیزی حدود 65 میلیارد تومان. دو باشگاه استقلال و پرسپولیس به دنبال جذب این بازیکن جوان هستند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/25680" target="_blank">📅 18:11 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25679">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WSD7lSltgKp6VgtLQMyYsqlKAkQ4YEHPy0sjwLXQ862Hu62v2rKu1V7kHHtqFO9b7Xc4fhfEkALPBPZTQ3F5lgNDbenrHPAmFxMbm4wUX6XWZcxTgjId2C4iutdLiLoCpVSKvxsbT7CeXi38IPoZdAYu4RgWsRPOtwTMs5-ocM29uKm_KZoJmCA2fgo8n4XTxJ85Ax_rDDC9GfUw0DZ6zSPds_acHT1u9MCLsc0UMIsVz030SpBOIKuoZcpThqyzQ2GTUJdw6OX9ZU31rmg6NF5vuDb09PI4CwzvJquACPhs0DB36L5y6MmEPmLDprEaUyUoc83KTLp3jO1YYyeK9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی_پرشیانا #فوری #تکمیلی؛ آغاز مذاکرات سرخپوشان با ستاره سابق برایتون!
🔴
بعداز صحبت‌های شب‌گذشته علیرضا جهانبخش در فوتبال برتر؛ صبح امروز پیمان حدادی مدیرعامل باشگاه پرسپولیس با کاپیتان 33 ساله تیم ملی ایران و مدیربرنامه‌هاش تماس‌گرفته و پیشنهاد مالی…</div>
<div class="tg-footer">👁️ 81.8K · <a href="https://t.me/persiana_Soccer/25679" target="_blank">📅 17:59 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25678">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VKbIcnMJgfWXaIxIHvTxTJoVj6dLZ2V3eBdW1wq2_fING9SrgW6GwfoTx_sAKVCMxI28OgPSG7NHAAa8eGGwUWnMJEYu8fnxmmv3jAfMal7jxo3xCJF10AZ7l5ntKCV_siiN_TXpxaXmnwJAT4sCewKCsanLB8S1g5mh5KmPKE0PRcCfEqXcL0WNrHZiDRKNAs6uixCxcq8zdVcUJMee8HqQdkFQg7zZbLUe2i4_ED825TDcP7UOWYdIRFeQaC2tApujcy3NZwjHfrj6YBeLIhYsMNMqkboR0HD2oXbi3ju2j2dF9w1zKmpWiJOqgmqzfLm_E5NYhnczqC9iIZ-7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی: تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 85.4K · <a href="https://t.me/persiana_Soccer/25678" target="_blank">📅 17:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25677">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qZHYBZkXR8__3pB5VvQf-pnFK51AUo79sFELqVB0UIfJaUS8rjNC8E9dL9Rr7O1QUcf2I9Bho2zx8jIFA6hpSOi-TPUIh2i5qty_C8f7SwamQF9tSGeSWpDX5lSZCVmdcUptS14hGOwUEMnuVoQOhV6bHEW9sL8VeXRr226nrpMpKq5LuhUWpldvgGVZrP4HDu8rbifY4BwiscIxuRG6Pr-3M13wBxyhwd0Dz2cNKswBW0gB0Oddh5VGhcrsRe_z5cct2ZUurhE1uqxZB_7Gm2jz23JNSMVHYkX6nAu4eUXnyt7JTPI0itvpxVh9EmwKg_OFgNCovtQfJLW5c7SPZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مسی، نیمار، رونالدو و هالند اگه دختر بودن:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 83.2K · <a href="https://t.me/persiana_Soccer/25677" target="_blank">📅 17:33 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25676">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKYo4HyLORFhYR4Wpn4OEmHcABFYebQfEURJfH4cnEVZ4cfvqK7rYZICuPozVg4_yTNg7_3KBI_ucpKWV3LGfRWF0lmMiCCShQZnUfr8k0LFnuoxtQzbMptSGRS9eIFj9XpR7P7wjPY3UQ37e8Nt4xxgy4iKL4tQl8xBlPYPJ8USESkioN4jQxLgXz-ZoxhTwht9Rk9J1548t2BYgCrlfzCvzrfaC41perqE0TGdR3QSnkELqLAyFmOhZAqc0Q5CgD2h2S2QnigvR9H6kKEBmtTNLAT_7LwgQtKZWUpEKYTpr3KKCfZM1xH0wJ3XZ_MV9KLeMTLMwYId49BbVWTg2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد... علی کریمی هافبک سابق استقلال با عقد قراردادی 1.5+1 ساله به سپاهان پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25676" target="_blank">📅 17:15 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25675">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z0dHa0WzL_siDBvTmEkHZIBenanQ2vtpFggDo4MHb1_Y1JqVVzYpqc-u23PpqrscQk4aMAJ9wxeT7pyjlEEjasL15uZciM1uQadOBSln3ofEXyhXekFB7kP3qCenzckvQzHYfM04fUs39FsNh_KB7hU2Wfv0A0HKg3UMzXH_wQtnAHNmnNEHHugRgZAyOlO6vNwltraq8HfOEk6RKhNqHAKD9OaYcA0MPH_uySBxXev9pjT6DcZREGYAbERgmJPMgq-ATDbx3uLVp4w-h_jnb7_7t0ZbuenEQDhqKgKkxz0W-eLgZS1m6tsVYXfKzFAModDExgOP2grBxbw6QhaXqQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ طبق پیگیری‌های پرشیانا؛ یاسر آسانی به باشگاه استقلال قول‌داده که از شنبه هفته آینده به تمرینات آبی‌ها اضافه‌شود. خانواده او علی الخصوص همسرش از وقوع جنگ احتمالی بین ایران و آمریکا بشدت نگرانه و مدیریت باشگاه با او صحبت کرده که خطری آسانی روتهدیدنمیکنه.…</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25675" target="_blank">📅 17:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25674">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A-6bMMxq9k2_8ldm83gmjRJ-qbTONkUcY7wJS486Qv80VEhlF-LxvKBpBoz0Xtzia6mYj8laWI0UtnR6UXyf8B0Cq9wZHH6ieYVfnycKkO93eE915z1bifv6bfEpHdG2RmfSEJQHj1lWrCYWh42lW0sWLt9KOoIy7gPAyh-PbFndybVV1keJWs5jzzCG324mLjiIZDR5uu7k_Bkswqa70oOrm5KwVXQl29_L-O3c4ADO0eJqHiLekaOAAcgz9ZD6BYuYgIV-PQ4IB3JnNhSUYn3xrCmif7S---InYn3uTFlJhM1a_KjydeXUrg8w4lmFN0k3Sfa3h9VZnJxBkn7zUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آندرس اینیستا اسطوره فوتبال اسپانیا و باشگاه بارسلونا مهمان امشب برنامه عادل فردوسی‌پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/persiana_Soccer/25674" target="_blank">📅 17:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25673">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=GYbZNn3HtQ1AwvRHif-Mn9KAPBJRDrfi5rirnX-AuWi5E05ORm2_rxacQRQEl2qNPGiUwsmLHW7wtwdrGAiXZuwh5ua3KYKuftOMgh1KTKdv4AXHLMFjV7_C-aOk1ztAekrkoh9XqBXy8PvQbSXUHBUnaPPHc-yMW2jmv_O5qgB5U5XH24cullqoyvcZsJOgZugCl2GLDbCrknX8wGJMluFZbr05140dNtAoiC-VjLHJ4Q1LjXI8yZiTRDDxs_1Uo3H3Z4Yl6B3btrq6gWA2pLyor4K-K8sLqKU1sH7mrXSk3p4CKfV-VFMQVYEKWCHN9FgTiH9OWWg7u9eFNPkxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1aeff2dd56.mp4?token=GYbZNn3HtQ1AwvRHif-Mn9KAPBJRDrfi5rirnX-AuWi5E05ORm2_rxacQRQEl2qNPGiUwsmLHW7wtwdrGAiXZuwh5ua3KYKuftOMgh1KTKdv4AXHLMFjV7_C-aOk1ztAekrkoh9XqBXy8PvQbSXUHBUnaPPHc-yMW2jmv_O5qgB5U5XH24cullqoyvcZsJOgZugCl2GLDbCrknX8wGJMluFZbr05140dNtAoiC-VjLHJ4Q1LjXI8yZiTRDDxs_1Uo3H3Z4Yl6B3btrq6gWA2pLyor4K-K8sLqKU1sH7mrXSk3p4CKfV-VFMQVYEKWCHN9FgTiH9OWWg7u9eFNPkxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
#اختصاصی_پرشیانا #فوری؛طبق‌اخبار دریافتی پرشیانا؛ اگر اوضاع منطقه آرام باشد در جام ملت‌ های آسیا سرمربی خارجی روی نیمکت تیم ایران خواهد نشست. با امیر قلعه نویی قطع همکاری خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.9K · <a href="https://t.me/persiana_Soccer/25673" target="_blank">📅 14:42 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25672">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HbPZrduybxblVz8ecW5IcWX3SauOtdRE2rEHLl0uLEYicM6cfyf9gjJPZGcY_Z5StQJp2eIZoEZkxMemPTpSpP1-CK2lsQiZyNwL7ZMbMBh4gWzIGALAAFDyrthQqVFpgzBHIwrrCKvE7s4kLDjlcCDA34eoLebbNxUmR38RYDgFtSIKjJ1xEKQIqG16_wfSZlJkt6y_uVx3FvHzVM0z0FIOSrtp9YOyaFMSxWz2k4OPOAV8X_XH5HIZCRfZgGBqJaOECnE5eLrOv4couwf8h1-Uzzh118UBubvo1yxYGJ2DcqU_tbI6H4iaJb7107UP94S3ea9EzXH5M8lqC8zXlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#فوری؛فرناندو پولو خبرنگارمعتبر اسپانیایی: بارسایی‌ها یه‌فرصت 72ساعته به اتلتیکو برای خرید خولیان آلوارز به ارزش 100 میلیون یورو داده است و سران اتلتیکو رو تحت فشار قرارداده تا زودتر این انتقال انجام شود. آلوارز به اتلتیکو اعلام کرده تحت هیچ شرایطی فصل آینده…</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/25672" target="_blank">📅 14:34 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25671">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=E41V_PuU8ggIqZ76G89U6Vs7n2hSr5knRy0XrgVwCOZIR0Fc9WBNEOHIhrmGP5xiTWqFc7uIZw3Q4Zo2HiJ6RpaZ0lweEVbDBhvVPUGWQCaqB2I6x1Ck-xfuq-vmJJxjPb4_PRmSpcmYwEsEC3UWFi29tGTVZnGWAx_EsSPpF-SWr07gWiVCCAkYPW6hHBxwKXaRccEXyxt7M3pn32Rv5MXxwnoSN0FyxVlEWVMZwYo3B3INeBzjAdN7UCtM-wmsrkI21wswWIZYN4fMekfs5hDOLplPMKqBYJ00YSdhZmXlNQSQMeXluT5R7nE00nmjWArE-nYxwFnr0Ba-nfTLjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3bc72012ce.mp4?token=E41V_PuU8ggIqZ76G89U6Vs7n2hSr5knRy0XrgVwCOZIR0Fc9WBNEOHIhrmGP5xiTWqFc7uIZw3Q4Zo2HiJ6RpaZ0lweEVbDBhvVPUGWQCaqB2I6x1Ck-xfuq-vmJJxjPb4_PRmSpcmYwEsEC3UWFi29tGTVZnGWAx_EsSPpF-SWr07gWiVCCAkYPW6hHBxwKXaRccEXyxt7M3pn32Rv5MXxwnoSN0FyxVlEWVMZwYo3B3INeBzjAdN7UCtM-wmsrkI21wswWIZYN4fMekfs5hDOLplPMKqBYJ00YSdhZmXlNQSQMeXluT5R7nE00nmjWArE-nYxwFnr0Ba-nfTLjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
کریم باقری اسطوره‌باشگاه پرسپولیس:
تو عیدها و مناسبت‌ها هرکسی بهم پیام بده جوابش رو میدم. اصلا برام‌فرقی نمیکنه طرف روبشناسم یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25671" target="_blank">📅 14:14 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25670">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=C48bE76VT18VL9LG9fa18tdpWiOi_weau1q0cq_rZRIv5EwK0ynB9VE2l6AfHKCjXohqAYG2BTLgtbJDqd3TN2BmvUPF2lM8RHHBmfmIqBSxYqWYlq3kSRBGLDIRDZYMUtKJSoqDXPWDU6j0jn9661-4FLIUYvNW3onFgns37JNvYmS_pWKTObKs13sdUj96bVjVjr9BnGHD7wQDP872DCdCtSlpq3HkczO1DNenep5p4zHCfljBXf-xIYj5S8lzrUt_JkcXb6HLc6m8J0bpi2x20nuVB3pohy4gIunj9lWyXbWrxcMz-skszUq_kleXWjkKowMtkClLrG-rMnlbCJNFO-DA1qN9HGVbUy8BkrlUfabFGixZK3tgj2pi5hA3xzpgzhhkY_L3bxscyKMF0MLK7faZuh0-PrQyxb1uW25QQx0-X-07Fg1Jh9AIeJb_402cbjW7j_89fCn7n-uW7eZP6O0o1y_kw8VUO2S4RWKbLmFFIUW_ccw5laDlY23hRk-E9YQHzjBjThl29BqZIMr_0wyIZThofPX4lWvEmIPINVUg88qRi6cZ3QRu8mrPnH-4cIAaKEPRebpTERfRhSrc4UQIFQaBH0JExh4egWV2UGRuY4wwqVa0s_SLwlZxltwt9SC4r_7j3vc9TrAdfK55I7dDCKRk7ukil35vXVI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb91ba980d.mp4?token=C48bE76VT18VL9LG9fa18tdpWiOi_weau1q0cq_rZRIv5EwK0ynB9VE2l6AfHKCjXohqAYG2BTLgtbJDqd3TN2BmvUPF2lM8RHHBmfmIqBSxYqWYlq3kSRBGLDIRDZYMUtKJSoqDXPWDU6j0jn9661-4FLIUYvNW3onFgns37JNvYmS_pWKTObKs13sdUj96bVjVjr9BnGHD7wQDP872DCdCtSlpq3HkczO1DNenep5p4zHCfljBXf-xIYj5S8lzrUt_JkcXb6HLc6m8J0bpi2x20nuVB3pohy4gIunj9lWyXbWrxcMz-skszUq_kleXWjkKowMtkClLrG-rMnlbCJNFO-DA1qN9HGVbUy8BkrlUfabFGixZK3tgj2pi5hA3xzpgzhhkY_L3bxscyKMF0MLK7faZuh0-PrQyxb1uW25QQx0-X-07Fg1Jh9AIeJb_402cbjW7j_89fCn7n-uW7eZP6O0o1y_kw8VUO2S4RWKbLmFFIUW_ccw5laDlY23hRk-E9YQHzjBjThl29BqZIMr_0wyIZThofPX4lWvEmIPINVUg88qRi6cZ3QRu8mrPnH-4cIAaKEPRebpTERfRhSrc4UQIFQaBH0JExh4egWV2UGRuY4wwqVa0s_SLwlZxltwt9SC4r_7j3vc9TrAdfK55I7dDCKRk7ukil35vXVI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
رونمایی‌جالب‌از شباهت مربیگری پپ گواردیولا و فیروزخان‌کریمی دربرنامه‌جام‌جهانی شبکه جم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25670" target="_blank">📅 14:02 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25669">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjAG-ZukTZ8OsJRE10AfFyIms_FgR3lkHfaOBXSC3K9l_yUGqQVYTRcYG5MghOYbz3Vl5aIi3Y60choXIrvmRnWs3LXpQNOJ781-sPKEpFJYFJCgVICC6j9QWukBED1HqefAQ71F_0_sV7nBgR7pyS-Iw6mm8eLcHDMlsoWAKi1YC7xnEXehCm0Osg1Ic2hqMUkjmHwks2mPOxkGolKfztIwJ_SOqjrOmk8_XJLmd73UzgQaAfJ1Ap8hvw1-OOI0-IG20T8LVbWYm2XedUGMOjP2Kqu8lQkQCtKcELTXjTZFJBPWZIjWSRhesQZ_Dx5tSXAwd7MNfC9BxgrrXVHEQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
‼️
کرک و پرتون بریزه
؛ رئیس فدراسیون فوتبال سنگال گفته که: من‌اعتراف‌میکنم که بعد از حدود 10 سال متوجه‌شدیم‌پزشکی‌که همراه تیم ملی بود، اصلاً پزشک‌ورزشی نبود؛ بلکه متخصص زنان و زایمان بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/25669" target="_blank">📅 13:52 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25668">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd10299011.mp4?token=HmYzhlkQctSlQ4CnkVrRyOA-PokE85LN4KjxLWQSfYWEIvKB1bXuJpf3qKL420wcPlKDMA8Qt7_PAdILDbfUa3fRQ2olMUYMcXZhWh4uzhP7xpvErR3_3qandXghxsaxKH2Jam4-3b9wXsTEMsEX9CZPh4ULYs31j7cTI0CsNzcUtz5YUpKifIH2aoxMX8R5Ka8WHaBO_4sSmbLb3P7sNv19Sl9opqLzB2Aj8EYiw-axcsPs8lxAZEVQbSmtyXkFbz8ObY7cLIB3jeSE3xRPrDTEU7akiI756pIOB9_JdJ7VyQZVGhestCrOXPlaiQ1Z1ZzqQIHLmcDqUrbpvdeeBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd10299011.mp4?token=HmYzhlkQctSlQ4CnkVrRyOA-PokE85LN4KjxLWQSfYWEIvKB1bXuJpf3qKL420wcPlKDMA8Qt7_PAdILDbfUa3fRQ2olMUYMcXZhWh4uzhP7xpvErR3_3qandXghxsaxKH2Jam4-3b9wXsTEMsEX9CZPh4ULYs31j7cTI0CsNzcUtz5YUpKifIH2aoxMX8R5Ka8WHaBO_4sSmbLb3P7sNv19Sl9opqLzB2Aj8EYiw-axcsPs8lxAZEVQbSmtyXkFbz8ObY7cLIB3jeSE3xRPrDTEU7akiI756pIOB9_JdJ7VyQZVGhestCrOXPlaiQ1Z1ZzqQIHLmcDqUrbpvdeeBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/25668" target="_blank">📅 13:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25667">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=kkh2mbfGDY9JMKfwuba_eXoaJkUaIjy769jQJQSHKyj7cvu4rbqqepMirYPoiNCtuagmTJ-B6vLkAkYv0n-Pw8vMQsAa0hpKcfoiMnKsIyJPAobvf1fDaoRCjHxK60ddyJxKWm-WsevIchO9OzB8Z4rxlPYKzG1lqK6oE9SJ93PGtf3H_te0tH1wrFBgiEPzKwz0PbqAGKzaGUc0TyzLXUM8GE3sSv4gY1syNyG6sN68Bg0jbQZUgck3080L3wtq58fe6QS9sgkik3r-PcBUx2FWz1pE6lWyK8MCSz2ZIpKQeXbz4kx_ntTyXOOgasuKtM_nnyqP4NhjGhjWEDCuFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3e0f878ea.mp4?token=kkh2mbfGDY9JMKfwuba_eXoaJkUaIjy769jQJQSHKyj7cvu4rbqqepMirYPoiNCtuagmTJ-B6vLkAkYv0n-Pw8vMQsAa0hpKcfoiMnKsIyJPAobvf1fDaoRCjHxK60ddyJxKWm-WsevIchO9OzB8Z4rxlPYKzG1lqK6oE9SJ93PGtf3H_te0tH1wrFBgiEPzKwz0PbqAGKzaGUc0TyzLXUM8GE3sSv4gY1syNyG6sN68Bg0jbQZUgck3080L3wtq58fe6QS9sgkik3r-PcBUx2FWz1pE6lWyK8MCSz2ZIpKQeXbz4kx_ntTyXOOgasuKtM_nnyqP4NhjGhjWEDCuFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🔹
فدراسیون فوتبال و سازمان لیگ بزودی خبر به تعویق افتادن لیگ برتر تا اوایل مهر ماه رو منتشر خواهند کرد؛ با این‌ شرایط موندن بازیکنان و مربیان خارجی در ایران سخت و سخت تر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/persiana_Soccer/25667" target="_blank">📅 13:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25665">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h5o_4xTeBMQ9YFfpOjZzMhhv5QYpn86h8z97NV5SD5s-0_6cdSf2StJW0EoBuLHY5ANnYaWz5__IiCgQLM9yNnzeFuAO-39xTsZiWE9SUn2R1i9rWqr_5rYBXHNJZnssyWzHvQPVHCyANk6rTTWRs9ue4k-2Z9YzeEaPoTpMwYL88ZVwrKjJ9fNKju82azwngFFyd8KO5S4BHH3UL19WmMexx2JGppznfwdHo7D3ZRckCKvTeOXxcA3L3s3GSmecNCLug4-nnH7gH8SAsjBo1AZ5bKzgIDBo0kVa1cnItUoEs4rCMjQoPcF77xS1fu4c2b-zMOVu6XtnfTfISvPgzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=EfbpNz1hvVMP3OY6VJWF8uo2RpOgpjBQSx2IpBkgHX9qhhHpR8P43Y5pzzGr_O5HimNg3Tu9v1HZk_qIa8tYBb-4BFTaSxSkgrhgPZRwBK-qt2GVuIPgdOm1X0iuE9fncWiHPhcizBQZOS87IquwXXfSxvdp7jqz4CpZAFV3ynsKRZLDrULiFmgAii3R_XHVKej6WDLh1yV1LREwgNWbNMFeaBVNXeIOqeon2LDXoamXrsFdQHVGzu_xY2XUwsSAKq1CRXwZRrCek1CJJ8urtL1jfXVtY2eBRFMJbnBJ589ZGkbivp5oyEkJwd4jauTrsTPoidPeiiE80bzxEHfdHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700f8025d4.mp4?token=EfbpNz1hvVMP3OY6VJWF8uo2RpOgpjBQSx2IpBkgHX9qhhHpR8P43Y5pzzGr_O5HimNg3Tu9v1HZk_qIa8tYBb-4BFTaSxSkgrhgPZRwBK-qt2GVuIPgdOm1X0iuE9fncWiHPhcizBQZOS87IquwXXfSxvdp7jqz4CpZAFV3ynsKRZLDrULiFmgAii3R_XHVKej6WDLh1yV1LREwgNWbNMFeaBVNXeIOqeon2LDXoamXrsFdQHVGzu_xY2XUwsSAKq1CRXwZRrCek1CJJ8urtL1jfXVtY2eBRFMJbnBJ589ZGkbivp5oyEkJwd4jauTrsTPoidPeiiE80bzxEHfdHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
بیژن مرتضوی خواننده‌وآهنگسازایرانی با تصمیم فیفا در بین دو نیمه فینال جام جهانی ۲۰۲۶ به اجرای زنده ۱۱ دقیقه‌ای خواهد پرداخت. عمو بیژن بابت این یازده دقیقه مبلغ ۱۷۰ هزار دلار نقد میگیره از فیفا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/persiana_Soccer/25665" target="_blank">📅 12:55 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25664">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R2XoBVSLuS1y5RvaGe0ixcSQeVOUKTfP9c1co65iJYsZpbP5rqYUvccNMvuVXxIJvjRveUeRfgw_WSYt3ki5m4xc3MRNrIm8UM1kblHGnT8d8-iqNmOir72JpyKW5mDA80uMn3uWhdoREgIFfrUG3UJjTpNG1rBrCCFdCghq2GdpCvpudxZxsBaVcQYRkPQshGMxebLrd2dIfIIn_m4NeHZgpYQ-2mYZFlswCqvrFej9FxQ9bsWzQD6SSxZn3_yq1_JItCrKsCEfh_g6fDJWFfcqGtaTWd4-PxKIlkybtsOpE--aH3gSOLZEstMqRGfLI-Dr-G-ErpoDCxoA1sOxTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟡
🔵
#اختصاصی_پرشیانا #فوری؛ مدیریت باشگاه‌سپاهان‌برای‌جذب‌قطعی‌سامان تورانیان مدافع راست آبی‌ها به باشگاه استقلال نامه زده. با توجه به اینکه‌باشگاه‌استقلال‌تمایل به‌جذب امید نورافکن داره و مذاکرات‌مثبتی با او نیزصورت‌گرفته درصورت باز شدن‌پنجره آبی ها این معاوضه…</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/25664" target="_blank">📅 12:36 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25663">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=qpTpN_D9iF1lz90whpcb7Ra5zT5DcCDzosHVapjSRqgUi8nvM_iionxN9UxNgzEoeNIVYFCMMCFVlryZfnXtZQU-VDcXFH2pXQkcsAMtOFufWHdh-6HkspVvUgjZnprmOpfbTirq4p9iL70yRJGRqAMlc5-osVb1u75PAHWMyYfFnhQmDC5Kyy_qsbG1j-hplZOYYtCUVclbGx4qclHLsmK24Drc2BGomEBOvRw0qo9Fth7l4NuFFwrNpu_0MC5X3T2MlBSm-L2xEIIiP59SRGNosWut5EjKEJWK9ghz2ekO0GdAab2BMCw-09a4kknqlFiWrTNIf5OpYCKyWxn3MA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f07accb99f.mp4?token=qpTpN_D9iF1lz90whpcb7Ra5zT5DcCDzosHVapjSRqgUi8nvM_iionxN9UxNgzEoeNIVYFCMMCFVlryZfnXtZQU-VDcXFH2pXQkcsAMtOFufWHdh-6HkspVvUgjZnprmOpfbTirq4p9iL70yRJGRqAMlc5-osVb1u75PAHWMyYfFnhQmDC5Kyy_qsbG1j-hplZOYYtCUVclbGx4qclHLsmK24Drc2BGomEBOvRw0qo9Fth7l4NuFFwrNpu_0MC5X3T2MlBSm-L2xEIIiP59SRGNosWut5EjKEJWK9ghz2ekO0GdAab2BMCw-09a4kknqlFiWrTNIf5OpYCKyWxn3MA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🖤
متاسفانه مادر عمو پورنگ صبح امروز درگذشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/25663" target="_blank">📅 12:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25662">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtSJPQ1cdRLer5Q5quitpAJ4n7cBlr4w3v9rI-Lul_xt9AswZTD1HKg-I50E_PpYPYhWSgtTFBXRcvZCzosMiaNyGAdbHuSGNuXSlZJnwaLnDlIOJynt1x65_5SVtugWO-rA2GH2E6HJpiZ4PeK0CAZyRIv9fI5yVeeFjnYT-itqPyFt1Nf038-ZUtqJaADgNm8CRldtpNqTD4DGOturM-G4tgVEE2bP9E-Rbft1ah-9ov7z4GwxmucaSy1Cyqu8ARd9wIiE9NE97zwVyvk4ZfvQo1FP9FU1NOBd7qurte-Q1nX-kpkpop_YFJk6eRSjrVR_hkuDfxP9kVsex3cTkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏐
برنامه‌دیدارهای روز 24 تیر لیگ ملت‌های والیبال؛ هفته سوم لیگ ملت‌ها از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/25662" target="_blank">📅 12:19 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25661">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqQGAv9G-2ZgeEardUZd_1kG93277CnB8hw9xTYYCBdF0sJ1y1jBRvAwQs8DXL0Vlnw5cdptXB-mL2bSDHQ021sNtnix0n1UO81gwbEpRbziJQt2J6HPcuxuKKXZWmnu2ftmDJy2qLin0BI7_Lra5zHYsIb70m5cQwwCOWrvHsX5HgOBKyAl94X8w3oHri71aJ9_EHWtCGpfDcXTCe1SWB-q0YjeJE9KeCclMZOv_l7RlYkqWCC-ogjv3IuA1ILTrzZZc421Zx8pDtrRnM1nVIrRoXf4rcsEMToec0SXWs6OwVvTPPYmg5T6DH5nmNsMj6KE8paEmgwEI5PIdXwmSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
اولین تصویر از حضور یاغی جدید فوتبال ایران درتیم‌جدید؛ سیدابوالفضل جلالی بعد از پنج فصل با لباس آبی امروز با لباس قرمز پرسپولیس دیده شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/25661" target="_blank">📅 12:05 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25659">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I7T86WFzWGjvykM05QuzWkwYgjWBCga8CoY2h6eV3PNyOQsJLGIDi1IjeEYCzztAWfTYrXOtyn-mibQd5LksDnwzVSKAfwSY4PKAWtjFWTcTjTjE7i-o_SJ5YmTCAHBQFjFWSfERHeW7wpx2qKetLnGWOIYOIQfqqsDg9ob3l0UrAMkBdhzOyB-h4pa14hsCRXmMlatQPKGppUKWxa0jsQAtMCZbw9Mx2INCVcbZf1XtbI-T9tGrTCTIKVc0-kflJFInRPaiFWof-0ouAflQDX8e66jBjFINxkIL5VGYsb0NU2rFQ_XRQxWbnJEzLz60V8wSQYLzqAeTFHET-2y-Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
#فوری
؛ افشاگری‌برگ‌ریزون عادل فردوسی از امیرقلعه‌نویی:
ماجرا از این‌قراره که چند روز قبل از دیدار بانیوزیلند؛ امیر قلعه نویی به مهدی تاج زنگ میزنه و میگه‌من تو فشارمالی‌قرارگرفتم و همین الان 140 میلیاردتومان‌میخوام‌اگه‌جورکردی خب دمتگرم اگه نکردی من انصراف میدم و روی نیمکت تیم ملی دربازی هفته اول جام جهانی مقابل نیوزیلند نمشینم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25659" target="_blank">📅 11:53 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25658">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sSeilSWop7IZraEXgCbkZ5ylIb4rH1g96bnhyMUWSdtNL1uFM3V_Z_5DrlyCoizwpoDvQE-1MGU2wKa-BaU7G37o4-t-8Tfp7c7nZwyn9ZdR07Md2cr732V9lKwCTPSRNsB97MkFfN-3m9ynClufCXPSALLpAEYAe2WPyqXYQQg8ZmucKPp1U_2dZltCLL7eZNEyfEENp0FDAkENgRdk391YSkRt4WXjVsT_pvuniGPHlxPBOeVpCfeg1tGcejOMhdFLQRCGziIMCigM2vBiI0yANc7dcCY-Sh-aYvRTqyG7QjY6OjK0SwjVsAMV75etmmQkOE9n2iAtuoAev8-CXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
5 داور نامزد اصلی قضاوت مسابقه فینال رقابت های جام جهانی؛ علیرضا فغانی در رتبه سوم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/25658" target="_blank">📅 11:40 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25657">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=Ljz8EuEZrpabpXUnXvU37E1ZLHspbUgrpOPhJwXNhAQ8izZsjywMHOQDUgig5cca_r2TzU-q8rOMxjo4r2-lH3bABQEOJUknyZbeFD-VL0AsrvsscRjfMj5PuR9oqGvESHsD7FsBKlvsjXFbPeow6np-8Qgvir9utudtb3pOCwWAwNfd4LfmRwsVuJt8ZTNkGS7uyUb3j73YioB7G-VYuhPCxuRHFjGOYBsq4ONjhPAaiqy3TeLeqkGQ6FuQSErzBFem9blRE7ZfxMeLFuc01LaICGr6Wolgh1oObAySJNceraAyTAiFXK3TYItBTIO3AJG8yv4laZNvNIxJSsI8Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91bb7a3c33.mp4?token=Ljz8EuEZrpabpXUnXvU37E1ZLHspbUgrpOPhJwXNhAQ8izZsjywMHOQDUgig5cca_r2TzU-q8rOMxjo4r2-lH3bABQEOJUknyZbeFD-VL0AsrvsscRjfMj5PuR9oqGvESHsD7FsBKlvsjXFbPeow6np-8Qgvir9utudtb3pOCwWAwNfd4LfmRwsVuJt8ZTNkGS7uyUb3j73YioB7G-VYuhPCxuRHFjGOYBsq4ONjhPAaiqy3TeLeqkGQ6FuQSErzBFem9blRE7ZfxMeLFuc01LaICGr6Wolgh1oObAySJNceraAyTAiFXK3TYItBTIO3AJG8yv4laZNvNIxJSsI8Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری دختر علیرضا بیرانوند گلر تیم تراکتور دربرنامه‌امیرحسین‌قیاسی: بابام خودش استقلالیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25657" target="_blank">📅 11:13 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25656">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=bWbxWFIBciR5uuxNXDB3AoWzXxYV-ysJJy1BhqJsErx8NkOGQF24jnUiMr8_Ihj1ax2dwOexzOS1_GB_PDDIsaiyAhw6IbnRQEx7Ll5B3xhVEx29Rxa4LaMG9X1nhFAmvq6K6beP2QkLPG5NX2Jf3sLT8n-a_XN-R5YBebY9mYLMq7q7WvOwz5Q-sL98RYxmQNzzkqW40B7-1sCdWthJO7KJ3SCLTjVUtBmFPWoC9as5gmYlZEsWrZ39dSFn8aZ3L_ORjcK6lFXaBn1T1xDI4MfGc-rUf2UuaGocZ79rIEz3SWQFvRJc79GeiJ1AKjj3p6kIA-90v_4ZYvVm8-HyOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c1f067d59f.mp4?token=bWbxWFIBciR5uuxNXDB3AoWzXxYV-ysJJy1BhqJsErx8NkOGQF24jnUiMr8_Ihj1ax2dwOexzOS1_GB_PDDIsaiyAhw6IbnRQEx7Ll5B3xhVEx29Rxa4LaMG9X1nhFAmvq6K6beP2QkLPG5NX2Jf3sLT8n-a_XN-R5YBebY9mYLMq7q7WvOwz5Q-sL98RYxmQNzzkqW40B7-1sCdWthJO7KJ3SCLTjVUtBmFPWoC9as5gmYlZEsWrZ39dSFn8aZ3L_ORjcK6lFXaBn1T1xDI4MfGc-rUf2UuaGocZ79rIEz3SWQFvRJc79GeiJ1AKjj3p6kIA-90v_4ZYvVm8-HyOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کسری طاهری مهاجم جدید نساجی:
من اونشب تو شوک دعوای آقاخداداد باجواد خیابانی بودم که به یک‌باره‌رسانه‌ها خبر دادند که پیوستنم به پرسپولیس منتفی شده. بله از الان به بعد بازیکن نساجی هستم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25656" target="_blank">📅 10:51 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25655">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OFXgdo6-U3HvxqSgG76fJZ5eVjfhaclEGCAQpIEjAYuN3Ts7msDb6tQKc7xSrIvWDeJO4tedeey-QOehGtUdnK_XhTpZX8pPlR63zsrXt74skuihXYh6L9ogbrytI6ifqg18fd_ZWufgGn9xBm1U6mJQmLQh6kUVM21vI0h7Q3zyPF9ATChl4POIwCiYuQqseKtQeFbYCf5HE7sAoO4eGnmaLLbkCsU1GH1ygLuRCSKSpHUvM1Wt6Pn7aiB6_KEyUoJKD48m6I0x9iYvazefij5B0Yq-GkHnpiK3SBJrAXizcRcXDvI14kgMKTJNP32iLzXVjU7eoYSQs8Uj0cOdyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدشد؛ باصلاحدید کادرفنی استقلال؛ آرمین سهرابیان دیگر مدافع میانی استقلال در لیست مازاد آبی‌ ها قرار گرفته و بزودی از جمع شاگردان سهراب بختیاری زاده جدا خواهد شد. پیش تر عارف غلامی نیز در لیست خروج استقلالی‌ها قرار گرفته بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25655" target="_blank">📅 10:27 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25654">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=OpLykqA3SgLGSI522oK_FLs-mhtZJeAMKbZV_D5R0fy1svXbagNe5LMHMey94bYN7ncX1UA_IZeqNH6wG5QeiCJE2utjK2uzvcWM0diLZ8q62E47QFu15Wu9ash8mCi2TBQleYfUS9DF4b1D4vqKBvtFKDZ1IQMfSmEoMuJJv9z_IXOpUzYLQZ6MKaoxwvqh-Z1H51Q-2S-Q5zkcp4kQ8ljI1wER2Z5A3IuIG8amaueDG_l_xUFPZiuq6y9F2qPg0ZbrHUTjIAxDHCtPo8R2oQLP2mNl0GtK4i-E6YvDj0Kni70gMkYoscZSUZlcobYurKKwyfyhGkMiwVKmRaGa5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5705053c4.mp4?token=OpLykqA3SgLGSI522oK_FLs-mhtZJeAMKbZV_D5R0fy1svXbagNe5LMHMey94bYN7ncX1UA_IZeqNH6wG5QeiCJE2utjK2uzvcWM0diLZ8q62E47QFu15Wu9ash8mCi2TBQleYfUS9DF4b1D4vqKBvtFKDZ1IQMfSmEoMuJJv9z_IXOpUzYLQZ6MKaoxwvqh-Z1H51Q-2S-Q5zkcp4kQ8ljI1wER2Z5A3IuIG8amaueDG_l_xUFPZiuq6y9F2qPg0ZbrHUTjIAxDHCtPo8R2oQLP2mNl0GtK4i-E6YvDj0Kni70gMkYoscZSUZlcobYurKKwyfyhGkMiwVKmRaGa5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های ایسان اسلامی درخصوص درگیری شدید دوشب‌پیش جوادخیابانی
🆚
خداداد عزیزی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25654" target="_blank">📅 10:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25653">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=IRx7aD3FsyAJ9q6QBnV3Tm9aanfF_ylHz4vdpBX2sHUIUGZTAlicwBUtr6CpPp9X3sDJHbqh3rgWcRukT5gx57BfwwTHG_u0tZarsxhHahlPUUYXCNiTHadv6z-AmOhbaEvDCNXM1pYl69VXh08jqM1a-O6fJqScdOsSjjkg7DJALU_NdrYmGkwfOHRxzJd8w_lNDD2K6BHENu1yUBowh-96SqfIRvt4yBkT0EzjT4P5fa9d4HAHHEZMlKn4Zne4wxFuf7jTSblymNtw4wR8hQWakpeqhhRIaVXwy4PF-MYwPGGcSwkjZHS2dw_Mr9AQ1piVRV1dwu7u3ng0Qh8X-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d33fe4e361.mp4?token=IRx7aD3FsyAJ9q6QBnV3Tm9aanfF_ylHz4vdpBX2sHUIUGZTAlicwBUtr6CpPp9X3sDJHbqh3rgWcRukT5gx57BfwwTHG_u0tZarsxhHahlPUUYXCNiTHadv6z-AmOhbaEvDCNXM1pYl69VXh08jqM1a-O6fJqScdOsSjjkg7DJALU_NdrYmGkwfOHRxzJd8w_lNDD2K6BHENu1yUBowh-96SqfIRvt4yBkT0EzjT4P5fa9d4HAHHEZMlKn4Zne4wxFuf7jTSblymNtw4wR8hQWakpeqhhRIaVXwy4PF-MYwPGGcSwkjZHS2dw_Mr9AQ1piVRV1dwu7u3ng0Qh8X-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند: توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/25653" target="_blank">📅 09:39 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25652">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=SO-6b3ZlY7tAqagQX9WqhPqFKK3Fdwh5rHPZ6e9KP4dcIriga08W04Y3svABdk7tWYMVja3ndTjLMoKvBQiYKLU6BLUrrceRnbeGrNvweTuiejEOhADiLNetMnyWctsmloWA0zzoyZnCaKjNpU089VIL-k74Q9Qk1KwfoPuw88kLUqoc8DQU_GHR4w_VJ4bV7kg8nnQa5aBMH-wZtmqRZ2lddWi0JyWGA7nN4TOV5H44ciZPERWXytdbhe2QrGr1nPeErG3tHMtbjg4VxSlibxkTLPeDzc__vzelNaEvAsymlKdKyFOizXIcEvqINE9rVV3hG-ilVBktXywlkoUItRe6_-j2aRfy0lJMecqt32CeVFHARvCBuhSkYowQNERSMAJI8j3Kz-D8GiNhXoJBhBfxAzzrhaGaZgGX5TSyFXPfTRL9sb2i2sWjjlwb_S3ousmkWi9J-ytuNCh2dgK2Yeg6a-TXaPAvxnKcQT_uWEiGivWUpRn9Kav9BRMDRDwK9Pw0oqtcRhEl_cD3y7DB3_0U_tli5MHTHvf0ARtb_3ZrZIpKta9sFGEqhikAYM4ug_lMjUzsToyOLFM6mvOIS1xNxLsc4yEBoVqL9_d9tr1KBPrlOW1E0R4TNrBFn24KtlShVw_kMqKIla5db7kdQlbED1zD-_ykQQVEmo3ZKBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c3b52fc8.mp4?token=SO-6b3ZlY7tAqagQX9WqhPqFKK3Fdwh5rHPZ6e9KP4dcIriga08W04Y3svABdk7tWYMVja3ndTjLMoKvBQiYKLU6BLUrrceRnbeGrNvweTuiejEOhADiLNetMnyWctsmloWA0zzoyZnCaKjNpU089VIL-k74Q9Qk1KwfoPuw88kLUqoc8DQU_GHR4w_VJ4bV7kg8nnQa5aBMH-wZtmqRZ2lddWi0JyWGA7nN4TOV5H44ciZPERWXytdbhe2QrGr1nPeErG3tHMtbjg4VxSlibxkTLPeDzc__vzelNaEvAsymlKdKyFOizXIcEvqINE9rVV3hG-ilVBktXywlkoUItRe6_-j2aRfy0lJMecqt32CeVFHARvCBuhSkYowQNERSMAJI8j3Kz-D8GiNhXoJBhBfxAzzrhaGaZgGX5TSyFXPfTRL9sb2i2sWjjlwb_S3ousmkWi9J-ytuNCh2dgK2Yeg6a-TXaPAvxnKcQT_uWEiGivWUpRn9Kav9BRMDRDwK9Pw0oqtcRhEl_cD3y7DB3_0U_tli5MHTHvf0ARtb_3ZrZIpKta9sFGEqhikAYM4ug_lMjUzsToyOLFM6mvOIS1xNxLsc4yEBoVqL9_d9tr1KBPrlOW1E0R4TNrBFn24KtlShVw_kMqKIla5db7kdQlbED1zD-_ykQQVEmo3ZKBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
به‌ بهانه بازی امشب فرانسه
🆚
اسپانیا در نیمه نهایی یادی‌کنیم‌از بازی دوتیم درجام جهانی 2006؛ فرانسه‌ای که به زحمت از گروهش بالا اومده بود به اسپانیای آماده خورد که هرسه بازی‌گروهی رو برده بود و اغلب فکر میکردن فرانسه رو هم میبره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/persiana_Soccer/25652" target="_blank">📅 09:32 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25651">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PzdbeeQYXqrLS8G4iUiqCk_o5dPUAI_Z2gNKm8ITOCsKZCftrqHpMPlh5jPn01GKalMVfPMR_GHUUuXiWKfTf2tctrwVSSPiCEMj1NbTaCqS8XyJyVY3xW3gLMKpm1uPb--PzIsaZbiC7Qimpb0QVU9rRyvHrlfcQahIxmaA2YclMtDj5ARrJaK9TUUBlBF8ArpZDli8Bx7Zaqwdwn5xwjce01Sd5yKmhiB1_IUq1H2aDkQwUA-62sDuXJP3nl24HFD3A5uwx5g54D1uC18RsXQCYrX3iSyaAXPLkbbGQAqOra-bMkiN4Klzsym_A15zatO8KOZHkoWhh884mwKCuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
#تکمیلی؛ با توجه به اینکه قضاوت دیدارهای نیمه‌نهایی به علیرضافغانی نرسید؛ شانس ایشان برای قضاوت بازی فینال جام جهانی بسیار بیشتر شده.
🔴
فکرکنم‌دیگه هممون دوست‌داریم که آقای فغانی فینال رو سوت بزنه. انشالله که نخوره تو ذوقمون و فغانی بعنوان داور فینال جام…</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/25651" target="_blank">📅 09:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25648">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=AMb4YFcjEhvCHJxws2C5Ddi7GGWMRGFDP898XRR8YTRSpsxJeQdOvEz7s7X4emHCboVR-UBBBciFsrh7GYLXmcsMR50G9HM66KMVZ2pCZ7K8j8XD3Er7gOyez7lW9UoqBV9f4tdLVDpT9K6muLUNT_QUb86O6Dqwc05qKby4ydF8bmdc_RWH-793UE44S-W6czfAabRiVGp_V3ycQCgA4nKheCu2qVqr4A9GtMNBq8J0IqtccnI9gksUlvF5-zueURL2gt2SLTS4ejnWWUAWN7tDyG2PjZC802RC6rDOYu03osEeE7weDeaGnHrc0unJTXHA3czS60XqZPHSAhA9dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/298c4f2fe3.mp4?token=AMb4YFcjEhvCHJxws2C5Ddi7GGWMRGFDP898XRR8YTRSpsxJeQdOvEz7s7X4emHCboVR-UBBBciFsrh7GYLXmcsMR50G9HM66KMVZ2pCZ7K8j8XD3Er7gOyez7lW9UoqBV9f4tdLVDpT9K6muLUNT_QUb86O6Dqwc05qKby4ydF8bmdc_RWH-793UE44S-W6czfAabRiVGp_V3ycQCgA4nKheCu2qVqr4A9GtMNBq8J0IqtccnI9gksUlvF5-zueURL2gt2SLTS4ejnWWUAWN7tDyG2PjZC802RC6rDOYu03osEeE7weDeaGnHrc0unJTXHA3czS60XqZPHSAhA9dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
👤
افتادن شال یکی از مهمون‌های امشب ویژه برنامه عادل فردوسی پور؛
تعجب عادل عالی بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/25648" target="_blank">📅 01:21 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25647">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxUF5RvnKtKZlXXEZ2I-nqEDCoFd2M0buVy2JBe9I-NmVOWuzk1NqSNX-TyF55FLsVOBmx7jX6XTj5muDifbFrkxPhTVgq0UtAWswh_MldAAU8UUUt9lT-VE6cawnpCG1hOK1Eh_y-euv3uSKfNk9TRGeg3BQRcqqeaIHMHLzfB1PJKNv9CQ8VQyyzr9VzTez7bKqp6WODRJbbjhc5AQRG66zh75Bam_yJvPuxokuawrAhDhwct8nwAx8zNlcUiXY9juqAhEaBF4pk3dZdphygwUoEBEdUZ1bk6HPQDav2fCAwisCH8wWfo4Eb7oCHvkjO6RgiiE28Aut7z7ocfvgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
👤
علیرضاجهانبخش کاپیتان 32 ساله تیم ملی:
تا یکی دو هفته آینده از باشگاه جدیدم رونمایی میکنیم‌. اگه‌ایران‌بیام بین استقلال و پرسپولیس یکی روانتخاب میکنم که از همین حالا انتخابم رو از بین این‌دو تیم کردم اما همچنان دوس دارم اروپا باشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25647" target="_blank">📅 01:08 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25646">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ai9BIVlzE97yQ39Wg79uHUQNO3CRztYNJeorXYSbkvddMRWytnhkKNjBy-NIB50jtZMcp5VvZWd-QqHOBJwD7Xc0I3riMJgkO6fBOx7vdnOdt7_CpRlf-_QLBu1vxNg9wRSvugfXDOpXe-lAYWLUf2EHcXCMOQubWPk08OKH81EAptLbOvB84IQKMJzBuPbG1oZo-nvx58dk9l2hU7qMstecCd6gA5V413MImvcOUuYht8Tt1Z9ITdW-n1ezlj4jysmelnR_2F1_BwRT817bU0UaXIFbxFrrytEJgabI7x_VhVq-2Q0fHLBne0dfmeQqimfZ9SCsdcrpaikaumg3Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تنها دیدار مهم امروز؛
نبرد فوق‌العاده حساس دو تیم فرانسه و اسپانیا در نیمه‌نهایی جام‌جهانی 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25646" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25645">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=oUzCtrMKLTWGcgyyAr186ies-QpRIo5PyMO26wi-8CrEEW5I5ZE50Vs7KNtcatDDNPDQYU26iwJAnZ_bmfYs-vbvEuA53HunzM0d3Rcnep1i0qVxfcpEmg1_xi0KDHifq4NBpB5oJAuHqnd7SjW5tDYgKr-Y8SwiXaPbK66zT9ewxT8EZZJosa2epyztwpmMcuxzzgQxt3HCiIcA3dzs_NAYFp-Uhs3hhR5pIkznaw5kVKmtqoIB9S29E2Jtix7OvADpJVM65AQ-OzAE8c0CZr6DddHAaCdKi_SSmCZMJkDb20k3IUcrW-7dYAqqpaQftWazA1Q3Pzxcq7PP7C-42Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e63bfe28.mp4?token=oUzCtrMKLTWGcgyyAr186ies-QpRIo5PyMO26wi-8CrEEW5I5ZE50Vs7KNtcatDDNPDQYU26iwJAnZ_bmfYs-vbvEuA53HunzM0d3Rcnep1i0qVxfcpEmg1_xi0KDHifq4NBpB5oJAuHqnd7SjW5tDYgKr-Y8SwiXaPbK66zT9ewxT8EZZJosa2epyztwpmMcuxzzgQxt3HCiIcA3dzs_NAYFp-Uhs3hhR5pIkznaw5kVKmtqoIB9S29E2Jtix7OvADpJVM65AQ-OzAE8c0CZr6DddHAaCdKi_SSmCZMJkDb20k3IUcrW-7dYAqqpaQftWazA1Q3Pzxcq7PP7C-42Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فکت؛ازوقتی‌توخل‌به‌‌یارانش‌اجازه‌داده بازیکنان انگلیس دراردوی تیم‌ملی‌میتونن با پارتنراشون رابطه داشته‌باشند جود‌بلینگهام یه تنه این‌تیم رو به مراحل بعدی جام برده. انگلیس دیشب با دبل بلینگهام برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/25645" target="_blank">📅 01:00 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25643">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCnOzCD0ijP211biNzJLjOnrI1aMcLy1MB0oERocNyyJl2mj-UAaFP37WQ6XDTPwOC_XnNjE28KNMmXuEc-Vd6UvTUpMnR42qpMT4PK1ypbYlR_yAd0BuigQHvrQPAUAxQ5kUL-SgmdTmi4Veuoch360CwkDb3mcvmkZDnnUnHM70KeAeLmIssHIzjNZa9jUofW7v4JJaGIngL6YHlsLXzJa3iYNStYXhOjC91gb9WrBjp5XZxI4FmdK94Xr0zYxDK2xt75hKBpsIvbHQkKg7EONLd4na8gdf57SlezQ2C8v5Hfy0EKNfECrq1nDM143sBZrBrXdPxKdOUPTTryxpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇹🇷
با اعلام باشگاه فنرباغچه؛ اسماعیل کارتال با عقد قرار دادی دو ساله رسما سرمربی این باشگاه شد. ارزش قرار داد دوساله کارتال پنج میلیون یوروعه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25643" target="_blank">📅 00:43 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25642">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TWbusqt0GPXETGPQW6g0x-hs-c58iVXxTyRNdrADiNh-0VWFdaBS1HedI2GrN9namcuwbenmdHX9erbrhPGd0KTUZEJnSf41gmDLwexDVAUPLA87frSGZiaEuT6OvWhlkN9IIrbY1EhgJhI7iGR7v860SHT_7t0OHlHOrcKj0MnrDd-lvgn5CHp6pKC5HWBAfxMOfyw5UWyClwL5MX3xv61NI8ReXb5raf20vnvh8rNaEIvmvcZ8nznzPqdT5KCHPEhZMPHDYAdcvsxFHqp0KbC71ypIlm9Q5V_PsuHewtOkbuY7GeuEhwOQoceGU2hnvLVkrCrAGZNqJEvpMhriFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98ca4a5638.mp4?token=TWbusqt0GPXETGPQW6g0x-hs-c58iVXxTyRNdrADiNh-0VWFdaBS1HedI2GrN9namcuwbenmdHX9erbrhPGd0KTUZEJnSf41gmDLwexDVAUPLA87frSGZiaEuT6OvWhlkN9IIrbY1EhgJhI7iGR7v860SHT_7t0OHlHOrcKj0MnrDd-lvgn5CHp6pKC5HWBAfxMOfyw5UWyClwL5MX3xv61NI8ReXb5raf20vnvh8rNaEIvmvcZ8nznzPqdT5KCHPEhZMPHDYAdcvsxFHqp0KbC71ypIlm9Q5V_PsuHewtOkbuY7GeuEhwOQoceGU2hnvLVkrCrAGZNqJEvpMhriFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای شدید و مجدد خیابانی و خداداد عزیزی که مجبور شدن پخش زنده برنامه رو قطع کنند:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25642" target="_blank">📅 00:29 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25641">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=PSlghxY_DsqH9YhMmPY_AnkvaFhdkxeqMXWzulnbntqNs7dwwhezQ8dqTuXqzhk0HZLEcFS_mZUPBZWxLWArZlg2tZ9qXQ-r4rNpVYm0y3KfPqIe1zg3pXZDWRGZKPL9UB1m9cCmDGjfwFymRGo1NovVwo2iaNOIlwb-HCdYiZqxqwNCy9RWb9WIwBVofIBEDxKfa4WAJch3sdQoxDKOnxyXeBWTDfLn0yAY2ysvZ7qh1IubxUIGuGo-Obth6eO7ckdufj-TuuaXf3JHl7Wsw4JTwsO-3sGg_Yk1TTWbbmI6Jci5JSnN9iONqbux11BksoKKt135MGd1X5H4EAeKLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d3d13a462.mp4?token=PSlghxY_DsqH9YhMmPY_AnkvaFhdkxeqMXWzulnbntqNs7dwwhezQ8dqTuXqzhk0HZLEcFS_mZUPBZWxLWArZlg2tZ9qXQ-r4rNpVYm0y3KfPqIe1zg3pXZDWRGZKPL9UB1m9cCmDGjfwFymRGo1NovVwo2iaNOIlwb-HCdYiZqxqwNCy9RWb9WIwBVofIBEDxKfa4WAJch3sdQoxDKOnxyXeBWTDfLn0yAY2ysvZ7qh1IubxUIGuGo-Obth6eO7ckdufj-TuuaXf3JHl7Wsw4JTwsO-3sGg_Yk1TTWbbmI6Jci5JSnN9iONqbux11BksoKKt135MGd1X5H4EAeKLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
فیروز کریمی درباره‌انتخاب دومادش بعنوان سرمربی تیم پرسپولیس: انتخاب خیلی خوبی بود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25641" target="_blank">📅 00:18 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25640">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FjDNziu1SuBT6MwUMsMOfuolallIkya5JTgJk-s7a-wWTKTlgt0iJNl-EyiXq5Ozu120dcZCos1ZB3XaJK3vdE-AHq6cIKY7ucKXZcuUE4PH2L-nO5kcwzUble-g9IZpSLjcpHANLiAnoS87dQtza76qs-Z7hcWZ3ww1zvLej-Bv90oDoYOoZABuzPz0ObKQcrsG93h_Ds700z75wocQ83DUjIosPcq50y_dxHD20-CpBcwxhxZqibZJcLcKrXZDU4l0OW4d2F9I_bT-cvM1Cb41tk0gySHWhQONd4HLhJJ2HNw9xpda9j96c12ztc6rXmv_9FF2wr1y8zjkOjiypw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇮🇷
رامین‌رضاییان ستاره‌استقلال درسفر خود به فرانسه‌کیفی‌از برندمشهورHermes به همراه داشت که مدل‌آن Birkin 40 است و قیمتی حدود 21000 دلار دارد؛ معادل 3 میلیارد و 800 میلیون تومان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/persiana_Soccer/25640" target="_blank">📅 00:07 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25639">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/giNLe7w3N799h26oP7Lf0DhJQtEEY7qqJYVteGkId1bP9XBpL714fsMF4835Fu3g1Qus6kVw4-F-rrV43C5bxyI8ZOUOAgwXVktssT_w9hbZ_jHyedlUpnA8e1qak2DCUVRwGJHtS0EaMe2Yejx-LM-NT2Pxm2kXtbQ3LRvggrVK_kcjXCNx5LSQpwQ0D1gKeDNy_6MwYrBEs3tj9uQy1hM20TyFmQkbvrV8pD4UxRS22_UrcScPmmHIIscVQWM_iQKf23Ff6cwUjxGUk2tp7L6onI29JaFEtzbH87dEwZNajRouEnbvnyXmY0j8qO_uF2-Qzz0ed8n5JGvJS3BDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ باشگاه پرسپولیس باارسال ایمیلی به‌باشگاه‌‌الاهلی‌خواستارجذب رضا غندی پور مهاجم 20 ساله این تیم شد. اماراتی‌ها پیش‌تر مبلغ رضایت نامه غندی پور رو 2 میلیون دلار اعلام کرده بودند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64K · <a href="https://t.me/persiana_Soccer/25639" target="_blank">📅 00:01 · 23 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25638">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TsovVj68DbgkwaMyD6HqLPVVLYLLo5-VGiutyu9OsmiXsD2KJhkenjKKl4kHxaQ_4YPNPCvVGy-mSRDqI8MU3hjfcBV3PiyzmOSaamTHG8aL6v879jlpMdFX8XkUYLCdEMeAHCTFEFzqbIxbfUrn0O62qFkNVTGPsaDb6Jwn0Na9fR8ABhzpD6s-IFuViPaNv0Rijq_s0fc12c7OjgHosyIshWzggXJoTFF2kSLC-1NFPNycO87l6rlPAqz6Vwrww3mpAjW4-iDEpjwG8PBd4MfQV1jUMhabiWhQHccTYOaKXklGvUNQmw2PI9lIP3szbWPg4CzNkMzg06F0-pygkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
این صحبت‌های مدیرعامل تیم نساجی نشان میدهد درصورتی که باشگاه استقلال در جذب جواد حسین نژاد عزمش روجذب‌کنه با مبلغ زیر 3 میلیون دلارم میشه این بازیکن رو خرید. فقط مذاکرات باید حرفه‌‌ای‌باشه و بی‌تعلل مثل آقای زندی‌. گفتنی است باشگاه استقلال برای جذب حسین…</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25638" target="_blank">📅 23:55 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25637">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=eS6OZAUfvttXd1HGwcux2YbGOBSdSe8N2e5ANP5kAGSHakFoVjRE8bLRprlF0kYemCaOLk_3sBRnEJVlvFyAm1nvEwy2ETh0CQhpWRG_Z4WIm5DuGVyDxI0MKjSAgr9ufp-VWOdw8UnYGgwarZMd_-JfS6xzqk3jPJiSohXTmVnHCDFhKt5bLlmIlECieblXGZ1JaYctm7wfsUY-t3_kpm6Bz_aEAd5bNjambqciEVjHRBoLzKZTuKLUPC7g7u-2IMGJZ1JyCdY0XOZpAZnpT_JAQtY72dInw_VIFI3pG23_O9gohqgbMlUlOMWkF0W-mFkMAfLB5D6QUyATkG6CqA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8ae1ae07d.mp4?token=eS6OZAUfvttXd1HGwcux2YbGOBSdSe8N2e5ANP5kAGSHakFoVjRE8bLRprlF0kYemCaOLk_3sBRnEJVlvFyAm1nvEwy2ETh0CQhpWRG_Z4WIm5DuGVyDxI0MKjSAgr9ufp-VWOdw8UnYGgwarZMd_-JfS6xzqk3jPJiSohXTmVnHCDFhKt5bLlmIlECieblXGZ1JaYctm7wfsUY-t3_kpm6Bz_aEAd5bNjambqciEVjHRBoLzKZTuKLUPC7g7u-2IMGJZ1JyCdY0XOZpAZnpT_JAQtY72dInw_VIFI3pG23_O9gohqgbMlUlOMWkF0W-mFkMAfLB5D6QUyATkG6CqA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علیرضابیرانوند:
توقع‌داشتم‌عادل حتی به دروغ از من حمایت کنه و بگه‌مورینیو از من تعریف کرده:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/25637" target="_blank">📅 23:37 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25636">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=srhamrbxv-nTxYVudH2YOGhgtpeB4j32q_rysXqZgCGydCL-sO_tM5SBfs8H1qyDj8uDAcL69A3XBklB5OxJjwuosDkhiEdRL9QVYRi1VaXbjuIYkduuCPeahMmz16EAJ3kHAA8_Y403SOUP0e97WOTcNFYiko8NfpDGGUcbYJFyyhnSWEjd3N4WzVdAGH77xtJsU___MNdpay2AU-fRh3RfRay5b63awLZi6qwMxSI91BM2flY-s7Ch7D9vRVvXEpfquAamfOn1UwRb-zcLb-klqC-sqS3jSBj7MPE3Ouf8yuCTDK2vK10iq07lgLOJeZX1dcqLdHVohJC403dqdg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4483a354d.mp4?token=srhamrbxv-nTxYVudH2YOGhgtpeB4j32q_rysXqZgCGydCL-sO_tM5SBfs8H1qyDj8uDAcL69A3XBklB5OxJjwuosDkhiEdRL9QVYRi1VaXbjuIYkduuCPeahMmz16EAJ3kHAA8_Y403SOUP0e97WOTcNFYiko8NfpDGGUcbYJFyyhnSWEjd3N4WzVdAGH77xtJsU___MNdpay2AU-fRh3RfRay5b63awLZi6qwMxSI91BM2flY-s7Ch7D9vRVvXEpfquAamfOn1UwRb-zcLb-klqC-sqS3jSBj7MPE3Ouf8yuCTDK2vK10iq07lgLOJeZX1dcqLdHVohJC403dqdg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
وسط برنامه زنده شبکه ورزش برق رفت!
رسول مجیدی مجری‌برنامه: بازماانتقادکردیم نذاشتن ای‌بابا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25636" target="_blank">📅 23:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25635">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HC5qR8WDGbjwpqFErbT-02OFOK-3QXeO7EIbRlFMRIDPyYMsUEk_KIjKanvA-jOcW_m1ew-dE26bdCUgmR_-UTMAyRJ-EG1f10gXjr1jlpqsMSdlF_oe2O-tmF0fXryWgTxp41Nz-sG4qPwgSFa99HGnhMSrOFVMQUl3e4GR6HfZSlhVazV0qeQmEP0RW9rg0SMAMu1Ymzj1AlBJ2NzP3-BPsHpli8CH-txiV9nkJSaP1a-aBiLqwKTfSLdEY46kvIduCojaU0kcsZQL2wth0sAP3DoC4oHEVyoCpfIQ1oKvvsVek3Y9-DZxTdNExW2fXDkinfX-hCfoAHHOYNuReg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
خوزه فلیکس دیاز: مایکل اولیسه به سران بایرن مونیخ اعلام کرده میخواد بعد از جام جهانی بلافاصله جلسه فوری باهاشون برگزار کنه تا تکلیف نهایی‌اش‌مشخص‌بشه. اولیسه میخواد که در همین تابستون از بایرن جدا شه و راهی رئال مادرید بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/persiana_Soccer/25635" target="_blank">📅 23:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25634">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BC5pktEWcNSsU_z6oMEAIKKDeiqhVNsBkIflnFOOzKAJD9n4bjcNdFuw45hz60mczsTUUAw1lqHVd-Zaa-wYob2thXY6IVQgsdzVApyndoz7sQyn2qCcOK4scfDnB08fQO5ltYnAQyGQzdVIbOBSIBtTpaDgI4zH2DswcIrBSCUMxhHtvsO-jE9BoraBnW4eF8fQIsHbZ_ZqowuPqQnpW1JnOQQMEX3pDyjJ9OChhhsr1ypGp2P6Z9svalbRb8RjKdmg6tTw2Cnwj91-RhZHzak-0n1Wn4aDzlTo4LmInjmyTeo72FCgQa_ppCKWerfAAuHdv5oEE8h8DejKD4srKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏆
خبر شوکه‌کننده دنیای فوتبال؛ جیدن آدامز بازیکن ۲۵ ساله تیم‌ملی‌آفریقای‌جنوبی که همین چند هفته پیش در رقابت‌ های جام جهانی ۲۰۲۶ هم به میدان رفت، به علت افسردگی خودکشی کرد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/persiana_Soccer/25634" target="_blank">📅 23:06 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25633">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p_QPn_IvGbUlQzseI-Jxnu-BoCnKLBO-9Dk_EzEPSAR5Hb63X6ij_1NsyaYz3ZFeaAiqCOnIJAJONAvik2d9SRYzixQu_lj6R6LDz7ix3-U6lYXkQE6nJNDb_2yR91UyzVpkKe93uO9bxKbPnCmQeQDw1GAwW6HqFj10C1QiaMVFhpaeiz2W6CcpGH2GeorJDORr0cW8bojyEjN3hE8Vd9zYj0T8WvXQE4h6JjzJv_L6UZPYzGfz91aIMch9c1pQO1-X8qk62WEwEn5g99c4Ew2a1JkDwJeP_vxUVlKiYdlNcCbpfy5-1pgHR0XPiDcO5swKNRWQFLyLIZIEC7dYXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال ساعتی قبل بازمصاحبه‌کرد و گفت کار انتقال محمد خلیفه و بهرام گودرزی نهایی شده و باشگاه بزودی پوستر رونمایی از این دو بازیکن رو منتشر میکنه‌
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25633" target="_blank">📅 22:47 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25632">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BdNOsQ8SpEpso_q537Ien4xgWyQmdgVIvtVljCzOKAPEVoCUEr_k17718sHAKOdo_4-j_w_zLhdnP5YYw-k20cr6xlT88bY_YJmk8DR_q5RoSg4iiohGEcHk0Gr9sMXvD2ufe4577fmtR5jRVooE3X9p0x5Jz4Ey-9p9_XnLpH28KTmS3UuugtBgMIIQnolcMQqkfgy9mlfdK7n3o1lVpP_R7DtjZhnzC-SEWmPWB7u8-vvV86N3BRSMvFjfNWkc-ORJcTtMffjniiu_Z7sN18K2-EPkzDYUzpLm-iGqqQG3p1-EsaStJpHB__fkG84zY9-D41rd0-n8Ut2RoSDvvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
نادیا خمز دختر خانوم پاکو خمز سرمربی سابق تراکتور هم با پارتنرش ازدواج کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25632" target="_blank">📅 22:24 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25631">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=SAER6A4IufBcTpSBhYqVfi7Sk0LXFy8xqVHRDIDuXRahSn84FXVQ0nwDtIpU8Rgg4BDjHYXqWrf1utjdweRq5pFYlRmvh9dL6qoPJryCgMpH-6FuA7qQmsFCUwJiMh_GeNu5Rsk8y3wVjrtaF5SQih-9Mc91O2Tma14rfqAEaAsWeX4YK_X7r5_cDml-8ajyBR7bL4G1UqQ8-OnJrfNp4EfQSZosw-F73u7mhYVXmfBqEGvVC951X0q24-B0_Vy8mBknPiEeZQTpmb0K2s3LMXuvUywMLiuysbTEAMbHC_n5PNpook0gpHZk5TEm8ChbgVDsRQ_aoLLWzy3ul3fvGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e4c24c7d9e.mp4?token=SAER6A4IufBcTpSBhYqVfi7Sk0LXFy8xqVHRDIDuXRahSn84FXVQ0nwDtIpU8Rgg4BDjHYXqWrf1utjdweRq5pFYlRmvh9dL6qoPJryCgMpH-6FuA7qQmsFCUwJiMh_GeNu5Rsk8y3wVjrtaF5SQih-9Mc91O2Tma14rfqAEaAsWeX4YK_X7r5_cDml-8ajyBR7bL4G1UqQ8-OnJrfNp4EfQSZosw-F73u7mhYVXmfBqEGvVC951X0q24-B0_Vy8mBknPiEeZQTpmb0K2s3LMXuvUywMLiuysbTEAMbHC_n5PNpook0gpHZk5TEm8ChbgVDsRQ_aoLLWzy3ul3fvGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تیم استون ویلا یوهان مانزامبی پدیده ۲۰ ساله سوییس در جام جهانی رو از نیوکاسل هایجک کرد با پرداخت ۷۰ میلیون یورو. اینجا هم مارتینز ازش میپرسه میای ویلا که میگه آره آره بزودی میام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25631" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25630">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BzMJpaKeWikLl8xDRFaUr0_OBGxwRBnOR4umonB0wVNGyYfrdcLrg9-4g5CEDuIBG25MdSVPyNb6VcCQlUPK3ZmoeWrXR9F7rNm19xz15XuCbzhBTe0CNgr0vDvZ6OQ4RMUlt5DfI7gt1KkD840bI_wUOz-OsKq0_Lw0EDixdS1vsurOL-1snB9O76N3QWrcMehZkCG1prKsbEOpP5N-23i7jWLX7PEtuDBf5avcJQaxDJoCqp-_rWrQBNtKQ--IaBzAzZBA9Hf7tSzPjSDSzZfpRbga3RgsM-Idh3XyrH88v7AU0jKcmEC7o52AMu-4G7x3-z0M6-lPYDfmsop4yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
پارتنر جود بلینگهام ستاره انگلیس هستند که قبل از هر بازی حسابی به جود انرژی میده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/25630" target="_blank">📅 22:12 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25628">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rpvSgIUOGhdNlZXd-roU9aQvHmYDcKwWrzHptjd5Y-Bk9kYDZwMEO-M005vXEKCNWCvGlgJgZkVUOCAL3A8vd1ainQKx6WCAwIv_RuZNQO6sNqeuoGfzw5JnWgcWvGqbhzKM2d_PoDaU83n7n-BG2_8qQiYJYoeyAOmQQZpdUaDfxAkux2Dzaxv1R1REgo5E0j6eI-QmxN72Fx4n6ZO_eL4kgTtk6kPFcsGnqozFCH13Uswp2hr9shTmkwArraa-Yn_VMn7s5YirofOT5DqAT5tcMD2lJaPJZKeDzAKBGitnlFnev7nUidD2ehvnOu_Cj7FfGZzabJ3tnF5IyoEciA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
#نقل‌‌انتقالات
؛
کرارنماری‌وینگرسرعتی 19 ساله آکادمی فولاد با عقد قرار دادی به تراکتور پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/25628" target="_blank">📅 22:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25627">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fK1nCorK6fivV7CgfOk4ufcNlc7WlJ5fp-EaY-33hXIB4ntCnDKEwA2iyVAJuLh49jr_wxOhLxevizajuiCa8sZCUQpuBzRJ9-XB7_S7zvOC_WZfIH-UDCOG_Vn6otY3FwNodOvPHlLb0BjzvBV4RceY2iOziAJK9LzBGhxDun2EJJOJ2eAsigtfxtwcX-cBfbZ-jBrqaXJjjZcTbg92mZyccLKQpW_kJH5uS_99kMmDuIsS6sErxeIxs_vFoeMYlfpaTpKWU4ZSHXrNKxAnMXyn290o4Q3TlP9mHTuKLHeH4o2CBQcGn46XEjo-1AB2PCTZOSHiyqLZH74lKUfWNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌فوری‌نیویورک‌تایمز: ترامپ رسماً به کنگره اطلاع داد که جنگ با ایران از سر گرفته خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/25627" target="_blank">📅 21:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25626">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bZx9DMnBIs7F-j0ikmx_ldf4dkk05BVlNJ23GAomaGRyuLZe2xCEVgTTtDN8jL6-SByitZvQ7ITMoiXJC4eWtSkqCbq8KGgeWSmw-qv7D7O1EJfUJeA7CwQb3zYZBQowEzQM5Jysue2n0B76nApptGZbv1PSEFqsQFdHb8UOy7rlkrkZe0oJ7deoYF8DU7nLxvTtdYQ46vAqmk1KP-eRevwy-c7Nue0ceI2fJ2Jg4Y_UWsjt5F3N7ei0fc6R3Pd68j4jS3K3EzpROU3EnCM72ZcwQGkkVG9Sg_e99KU91KMuticsZTc-7sTTzXMtSZGIQSomEwX0i-1N0F_Ar-DEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
برنامه مرحله نیمه‌نهایی جام جهانی 2026
🗓
سه‌شنبه 23 تیرماه
🇫🇷
فرانسه
🆚
اسپانیا
🇪🇸
⏰
ساعت 22:30
🗓
چهارشنبه 24 تیرماه
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
آرژانتین
🇦🇷
⏰
ساعت 22:30
‼️
دیدار رده‌بندی‌ جام جهانی ساعت 30 دقیقه بامداد روز یکشنبه 28 تیرماه و دیدار فینال هم ساعت 22:30 همین روز…</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/persiana_Soccer/25626" target="_blank">📅 21:41 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25624">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GrK4xi-fgoJZBOxmffZeOgnyKEeRm18VxdYWyr5IJm93HFFREOaFbKYzopA-Lrf9pJWYuYqSd_9-8u0cA5wJxBiZeSd2AFsHj9rSNrYV_dS2jnWOBuTM0w5V1qFtoXi3El3alGnQrBa_kV1CbSSVKDiheEHL9ZYyABsEEZY1FcmWVjky_KMeYQYFjuOkzDi25r2Lww6YMvb_eFlT1p33kS2oO0p4OSELch3hmpAe1Qzbbse1NaWiIM6A7Ld1iE8eXs1AXxbnDFi2Y4bIOSDh_Q21IwIf43nym3Er31nq2_iLPSBekD4HXMc1-wzB-porUwSvn2CI7Yc-jDuDNFGisA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IXUZe976z18as5NTJ5Ox9PluY7Ao2g3RO6PACVPd_EFnu5M-a1tkT06yBJpWVrTKke4mvsNPXK3piojflgQQOZpbNVPe7M_mHr_OCi-V-oGXc1OE5NYbfzT2KFODLL4uYG49iAb0SL5yuzbxAfR60oMMyoBUG8ddpcQaLM22DOS4PcLXS4hTDsWxVtLIF8u-UDAvc9vGVy_THwOAe8ZjfrZu3BKUNNJuPMOuu8xP38BfWD3-CxSjeI-825wXgCQB4jRrNW89oiHfef9rmA4WvNdNfVCrDlAqGtvmGaLaXa3GPsVnQecawR0IAPBIQmZCFTMGO4s23t6wLHGX3Ex8ng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🎙
نادیا خمز دختر پاکو خمز: من علاقه زیادی به‌فوتبال ندارم اماامروز همراه‌پدرم بازی ایران مقابل مصر رو دیدم.ایرانیاخیلی‌خوب بازی‌کردند اما شانس باآن‌هایارنبود وگرنه میتونستند با اختلاف دو الی سه گل مصر رو شکست بدهند. امیدوارم ایران به مرحله بعدی صعود کنه و…</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/25624" target="_blank">📅 21:32 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25623">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rX9HzebBhJi8lQwKoAuhpuUmtjKObkCPgUvBawmOraggEeoVkvxzXk-YKjFUWVrjBqvLZtXgNSfNHRW1qWrS-HsffE8H56HVL4ltC5xneiSHJ28Qaya2Sx89Qv-kPsqByuMuQtS86WkEZmviN3H5jb6KM8i2J0s7quzcs2CO6zVZmmEcp2kCyqnQ1fovQShZaGwFj2HzdpLrTw6iB2KiNojrCVKqw5o3hBwizpRM16Z91X3omnkbnGge2NNl_8l0veZ4u1AD7c1rgQiiOjDrmhZ5WhYqRO4Ncenj_Ox4c_3Z_rkxHVJJoMfA833xtFpn43tf_a6eh1i_ljNCVZfAeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ محمد خلیفه ظرف 48 ساعت‌آینده قرارداد چهار ساله خود را با استقلال‌امضاخواهدکرد. حالا درصورتیکه پنجره باز شود از ابتدای فصل برای آبی ها به میدان خواهد رفت و درصورتیکه پنجره باز نشود قرضی شش ماه درآلومینیوم بازی خواهدکرد. در کل شماره…</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/persiana_Soccer/25623" target="_blank">📅 21:14 · 22 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
