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
<img src="https://cdn4.telesco.pe/file/jv5RsXZJTwr-9OF_Sc2Swus_8lRIF-IoUdzF4bGTNCYz-u_wHC_F9u8OL5bjhwOiTWCRvGfgm-B7S-nmT1BbdFXuCfBnOg6zKwTE3zfGr3lAiEPIPl71TrPf7crJNoMozh01qUdA3kmu1fB-rkHaT9BUfwnDPgDyan6u5MOnMP7rogXpChHq9A90XohYWbkZOnAeqD_5Q20Yxxe0Rd0ubBz4_K8JVAO4U0frii41EKUmZ6COrUc8Vlckn7WVgeQEWrldttbjQBXQfjJL_XKL7VktX5wXjlUMpjFNRNzRkXyHLE2hgfxINVYQ7ntvmJoZ1eQEMu3kVvlrxwsE_OVK6A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 414K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 02:28:55</div>
<hr>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QYt4LbGiiwW7BUTDjdplohEJR_5Az0gYUrCAdgRLauxgsaHi2vXuHZSim9tKuVZrCvjjJQyjVsCd91dosI4iSItxi09_v3aJ2pbDkJDVo3E0H3W6nFPQTaubqWyjw2YliPUEvpSxOjdLcz4ZKe1J-QdQafZBoIqsrTp8Zt2TeXbSqcZO3ineUB9mEF5wZQM_PjG7mbah-4iCiMdXWQdHTyBIItTsGk6Dk1NEdunma0Of4jaku_eBtj4RawJJd6SQbAbpba6JLlg8glUidp4yZhxYGktFA8kE-LBiGXR_kDcrhJh0nSIJR18qm8S8iiOSHqTfC6Nco_TLjJbWK4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.97K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0KWt4HOdJs83CDuQfVJBj8NQeXG32Ku5JC-2xhC-smXBZay3B482dtRVs8Brlchofupi0JvVp4XcfMT3HbPcjm5rQ0qrzT4O0QNGCzEF9YMUV_yYknuwzEnPmnDjF5yjn5dUMzcSfx6Jw6vUsv0YzpmdyfJKH8h5taoaABFJaTXpsj01uavqfmk49KmPZwInhFFQjWsfjrFb5Ui1QPXc2MOVOk4_IGHi7ApRsB8zG92N0ttQgRqk4K_qnrCxkL0NqmZXC3sa0BKck1bv46jzbxLH8pfU2P2ftfjhj8Vhpt0s2Xln7ADZtPY9KkdVl7LGZq-XKbSw6N1fqvepvOQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5k9Jn677BX4k7b2w8zbWXUCyeJ3CKlNLzJyrpgjpLTUWsosA4TRcm1gk2UBZNOF-J4SEwylF6YXUZ2zhnJVM7srcBM5nCM98UjUl2GNQUza2i5Xo6lnIVdIMLZH8iZDa_OaPZS76XlCXyclZg-k4BEDWJiNhCnLrMEdA2L3XTRPnQ07ArAB3Oe_EYpx34BAxXulTDzHTbeUrkVAbVpR1WU7DRtYbljJ1QzfUrUH31QGLPTodGMftjWAoEudQHu50L83meVBFDWfnE11wTgCv13aSOtlDh4BB8QxlmyAclWI_3KhI8j6jbmavUulN4nlUtjLCCHU6HJCmGLEEiTRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb5QkBO2JSMRNspylkW15V9otVsYZeEJHE5yfo_sKhEZw7sqynMjw6RqPfPYenhhJKFPNNOpn4wOf-9gJi2UhvRoQCfCUO6I5g1aJesQxb8rb8iRiaJXN5UXoBcCkmoJpYC-IJVEd1SeZ4yAush8C9mSgaYBdWw0X86ZThGl05tra8IktaIq7BRjwLhzKxbXKf-WRcNzsmuhxLWQmfML8paWWzq8CAOFHmbAApc5sdejc7m0JlL454Rd1J4m9id31oY6F4NLlpb1-zB_zEE6hN4IZ2wfGmgmfHIRKpAufFNOG09vtA_gnRsTpMA0fUnJOZK-kDbAgBNQ1zrQYXda9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwn4wDTPr1GG3mhw7UKL-SDihYeZSte-nr5c2DbPh-Zjrs_ogHhnDqSsG5AId30gsUpKjcuPVefyJXb_dVJmWjAn38KoxAsAbmrEc5ClYw4GWEW3oVsEM-CYONjS35Nbb0W8KHmSX6ipBToXcMv_1tYb2IEX7bssG7_1GfqT5MviGUyFIhOyDBrqhKqevh2WEAZSfvD5xcr-5xQFP0Hvz5tEZH2SPL2oXnVHdEcqSmP2e63bLOLTOhCWfYeCUt7MllOE0mLipwQN2nO8b1_Y01lJcr5u0xh05ar3pU-z35F2669J70DHvVPxBg2LurExeAdeYreSXi2Vo0nVjHlh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru-QcQ0ODka4n6mAtW3DICWJ3BCQukgBb5kizb6nXzoz6QsLH90te5O-koG4ylTqumZBexIFBh0f193yWfrdVb-Px-U-TAOpXfIXvE8buHUpTZEjW1PQGMSaXYyCRP3kZvv_Q0Mz_gVA98Dnr642j88nlF53wSpXzPxJrRZnlfIEOTkshIGwFu0uRMw8jwCaI1NgOJblm5w_tFWFBOsq5v0aWLotKpNufrhDyn_SNpfKULcX3XvaF93bGiFZ-NMspZazj4ZlgMY1z7jjFlSQ0Z9bg0OyhCd_tuaIblIvRGq6ZQp-DZLfO9qBR-LWobuXerFPRxm24SFOXG6h_QXq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=US1OW27K1SUkm48wxbdqYDXLBwrSKVcAAcs029PsN_wLWdyNguOd8enqdjPBgelooQR0ubZs3jNuWZIt1jJ_UVs5WAIkjU80y-djNRaZJYe3-3NzcOoGZJObVPHKS1wu4sRJ4TT27GIndvmq8Ou25YcXgMu059xEj5tnA2uonwRtJtgtJt00EQ4E_y1TbH2bkSTKYpuozmpQKEZWWulekreZB9gUE_VFrt5lliP0O3S7KPUsdwOfF44B4dlK4WosCfJI9AnekK0h83m3wCMqXYuEWDSdeaxRfulDtLjgUaAK9huDttVGS_jf_Knzf3XE_bwMBpeb3WVHzpvmnFQnMSgSuM0rEbLAQHiE1TpyhqIx_DxaZf0IRVmlB45hCh4b_qIFdReRy7qM4UeN3aiw0CfyKa3ZtubyCbhAIhtk5CSTSJ2zOHNEWCTEpVcRIdfBmYzTzA9aEpc54bn5Nj6LEMYT5bhCLSb1p392t9U6yyPjwK-YzNMroUgVJuDoO-umE7tJHTrw4jgpiSyYEpobp5a6BZYCh0o4hWQ3eawKH3itI48nIxNGXUH7HhGLqCkVWJe1Z59s_grNfwZRdUta8jgGLM35x0plD2hux6Gw-QV_5H0rjABd40JhelMIUDIrkoZ8sSWtj8ckll0RkQhb1yQVwEVrcXWdTHEkoKKTHsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ec0bc9761.mp4?token=US1OW27K1SUkm48wxbdqYDXLBwrSKVcAAcs029PsN_wLWdyNguOd8enqdjPBgelooQR0ubZs3jNuWZIt1jJ_UVs5WAIkjU80y-djNRaZJYe3-3NzcOoGZJObVPHKS1wu4sRJ4TT27GIndvmq8Ou25YcXgMu059xEj5tnA2uonwRtJtgtJt00EQ4E_y1TbH2bkSTKYpuozmpQKEZWWulekreZB9gUE_VFrt5lliP0O3S7KPUsdwOfF44B4dlK4WosCfJI9AnekK0h83m3wCMqXYuEWDSdeaxRfulDtLjgUaAK9huDttVGS_jf_Knzf3XE_bwMBpeb3WVHzpvmnFQnMSgSuM0rEbLAQHiE1TpyhqIx_DxaZf0IRVmlB45hCh4b_qIFdReRy7qM4UeN3aiw0CfyKa3ZtubyCbhAIhtk5CSTSJ2zOHNEWCTEpVcRIdfBmYzTzA9aEpc54bn5Nj6LEMYT5bhCLSb1p392t9U6yyPjwK-YzNMroUgVJuDoO-umE7tJHTrw4jgpiSyYEpobp5a6BZYCh0o4hWQ3eawKH3itI48nIxNGXUH7HhGLqCkVWJe1Z59s_grNfwZRdUta8jgGLM35x0plD2hux6Gw-QV_5H0rjABd40JhelMIUDIrkoZ8sSWtj8ckll0RkQhb1yQVwEVrcXWdTHEkoKKTHsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pC_JBvSVc6Q5scUVJ9m1fPasXDmUZOD-2WxesskKJkyPwqBWQUzoCMurJcV55jy-FEFeRtKKwzwOZYOEkw9U663J_Fxi07cLq1WHceBQp9946-dpHSfK-AwTdoqP24b4PDuLXNz_zmpURzI3Q0akDC5Gb8BmWb0XRPWt8968MzCVyAZv_MzlkYCXcluP1WJbYFOB8i5-kKXmIQY4H8b4vrOSzMZ3oGSVj_8Jgg0YmoSbCNVcdASe7LSPFnAmwq2Na4F2_Sr0v8NmCdUWhCLY4viM_NJ_lyjw1SHdWa3oUBnbR8CNiFzKUeM9DwXeHmz1spW5Z77ktJWWeRTs7j4Fdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a9ae9f6e2.mp4?token=pC_JBvSVc6Q5scUVJ9m1fPasXDmUZOD-2WxesskKJkyPwqBWQUzoCMurJcV55jy-FEFeRtKKwzwOZYOEkw9U663J_Fxi07cLq1WHceBQp9946-dpHSfK-AwTdoqP24b4PDuLXNz_zmpURzI3Q0akDC5Gb8BmWb0XRPWt8968MzCVyAZv_MzlkYCXcluP1WJbYFOB8i5-kKXmIQY4H8b4vrOSzMZ3oGSVj_8Jgg0YmoSbCNVcdASe7LSPFnAmwq2Na4F2_Sr0v8NmCdUWhCLY4viM_NJ_lyjw1SHdWa3oUBnbR8CNiFzKUeM9DwXeHmz1spW5Z77ktJWWeRTs7j4Fdoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
مرسی کریس‌رونالدو بابت‌تمام‌لحظه‌هایی که برای ما فوتبال دوستان‌ساختی تو مرد تموم نشدنی فوتبال هستی دهه‌هفتاد-هشتاد باتو خاطرات‌زیادی دارن
💔
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU0Vp0hZ60PeTAcYMF-w3EHElaU_YRMFha62l6dZUYlGDkt2kEBKr-aqy1mbBjpio6plyyMT48zSmjaBdBsCiZ7GpkyqYW6w4I8jdj515Un7ou2ZuwLkG852DNC1EkSXQ76q434JW6uRSnNNWHiLCC8xnZ3Nv_x7sqvsXMRqBNm59z2W9re_2gUTFFIAfCsaxROpeHZVrA-YYVZniIiw-wMdu7cLJ81UFLoaH-50Arv2BvuxCndZEHdlM3ERG2ZHwtdBIwWJcfxpyE4XOtKoIurahQxjrrBUl3VVaMk7F3T6PB2E5qBg8seICe3x9706Hwr5gtFHFljnG_nIb_DUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BThcbZ29ANqVovn3e3_AoeixZDIQRiy30_x0x3KB9L9Y_wGiT8TLtjFnJGTsjT-bEiTjwf24R5xJ9f8Sv7Hj7-jZj1WVmNKZL4hnuIZM8y8Tb8E4ySWIfggG1a-Zgz0fEi2W2ae6-vxEB2hw3oWU8_-CiBeVUt67RBlpt_8QAF6Gul70amW9pfDz0XOjE0rVhFX38Mb0PN-m5OIZKMiT2tqTmUv78ZOv4cDrRdE7Z1A19tSPyaKAyiJfGSbMJfIF_0AHrL9QN_pVGAjHDJZzEhJnCZ2oDVjfKUXLU0W-FA0cBF4OkyS-dAbbAjoATjkuJK5ZCXgiyfFY6nHikEHLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz0t554u7v5GOA-Lvsrmrk_TNbR4x7avf5LWHNNiDCY-Uqom4EcRfrl3iGiqOzSZ3c3N3UcUcs-93whN-RVbV5kXDi-ooefBifm3IQhhrQaTDH8pdkWBNihueT0rGHs4QllGQgnVz8ImJr4LWS3Yas-v61gv_9bCj842-XfGtbLBRXzArr2MIO7MmEUg9mSUgnHfYYMIllk_7EtSET4-6ghF8LFs7ZsGLio8nBPs1fD8-PmTzOmN4ga5WEaYrPrz8_HCDJDX_P23pJKDUR_35hUNa5uZY-4TaUEcxJbECz3Dxj8C4sCkgiSWD9Z1Df0dIvYUIiCozi93hIpjXHVYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqjzMmVCe6iFi-c_NEGgdMaJiMpcGStyFa-OgNyHFMNQkOMdQCxK60S3ICPGVGiclCLbIBw4i82PbRrkcTKIW9yb-1kh-oHzV1-l5wg5zMBeYX8M3XbQedF4hdPhqT-uZZayctYlJreUOJNLYMgOJVu7w4ARorI0ECrzxgSc48QIatPRXFvn8Jo8nqbxbaDbd5cRuCQP2_adxVbaKFqQBbhUnJ0MTqq3t5uLLm3Clc1B_OIg2ITTh1NW1Z0MHJID2vNmgJY08TpWgse5jc0sA0jKnnR16ff0knxW823trsy87Bqm00LUX4NUE5-rRv3sHLIiK99mc0UcYf_mCAlcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzUJ623KiYA_JbDRnmSNe1LIz6_nzgunlwuS_yJup1big9pOhsNWG546xUdHhYBarE9TadMwrBpEyacGLdLY5vznCqPgfqBhmMskBnTkqjoqhUwtUxaAuzke0IfL9mKrOZkg-pFYWQwUAoyP0q0Vrcj_b2yDhiMlQ9sQNNTx6Xlx5CevKzd4AOIS8BRXfr4GrmZdZTyu62IIIWBDhGF2AsI4fUeS_p-A1dRlTD9kxpV_BFZyGLY_eKlpk3TfHF93eGRiuBrlQSFJELRgiHqqfP90NqTZ97iwXtcv4HT_UPouOw0vtgyxYLrE1RZy52H7dOwxHD8BQXDAe0RM0R-99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apoU4lr7c2RI5b0WFyGgidEw9pGZnKXw_M-aW_y3gZBC6wQnVhwWb9sUV0BoFrwIhSdhWVvIp5SduG0nAr4tK8xlSnGp-PC88Vhw_9Lbuz34GRGZivvbADyVnAiIG_03Omn7vySw_zHPgEv3HqN137OEN-du7niVVcOHCMzZINjjxpW3fHrRKKQq8-3pc5Ig1P6HIunLPGviuXUdXEQOIimBajfHL7YVN_r6rvQOK-ehRG4FpdhrXGImigd9oEqr9ze4bazfTDwWD30jVkZHnL9FPJTf3JHicoR0wx6tCx22SLRSelghP3w9Iya-bXug6GNzR_zza2hCUqWENM4gUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-_Q_GL9S6N8cVb5M5jEF4I8szBleZXXfi9AnWeDlQU8FJzISx5swZBV8Me-4sqFWrdXnFlRKWbPpNJpt2pFMDmJGzGixHkWoSlyRPdfBKIgpQsydajdhp7Zdl_N6hGGqRM_KGeqMPH4uW3KzU2gscPAN7FctQu8_Ow4vKqdmofn2M9gmWqzDiRoVIs6n4Rlod65dfxKvEGer82oKd-1vHCBUltUsyMUMQ0bJFuDVkyPkgh8Hwc5XRLsdusXrbacMEtO8wOlcLtCZMncgDV0musWLekJHgl4b43F0_isBowEwvHw59FOnocL9TYnupHw7p4d0PB4-CkyaufGXQENUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL34ugje_g1o0i3gBiINFw_P04cL-YLeVeeiOC2uSIH3E8j6iFespdlLpkbagvjhPY2vKAkg0z361PUadXwGgTIAX1nHf0V1CHjU2_LFRxv8at6djA4N-ZXYYs5bT3eRflolYhoCwuf2B1CmprzVga-em31I7Jo-FxHaA6fx1iMfQvX_f559j28Bke9_iwk_ZuVBBDi1SWASG1OPfQQh9hHkq311NxGfQdJ2wLYQFpv4-zYW0NO1kkVTcnoCNgeb9KwSD3L1p6DwhA8ciOKNOZ-WnwuVKRCgIXqbUnkIlHlPjG6vuWhsySH8aoo-VzIlFzeSwka9GeHhg3f3A2vDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcDakIYAVDM7rElHAGtjwS6iDFPyrEaADAcEy6-O674aH8_QiRZHW8OKTqwHB6CitEg-fCFc6setbvELOYSPAP8MUcSNclw6dvyGDIQMtezeFNQgUDp11n0KGQYQ1-wu2GaQG677vM2W-OXCXMhAvYk1G6Sk0bIUlc1B-T9cT97pEUlLScCdao_b1PtbZzvySrbBZT3zOwprSzFokl_7loUPdDD2RjXYh2tBDKyLJJV_EAz0FrjCqYLDaJI6cNViqAynXRO-kMy6wTZnRMiMre2I0ygj4RoFkXkY-0cX4z8Cy4LqyplL369PNXeJXPDM6F1AN0mS6qRAbsnwkI2jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OJMmjybs0FQvbmaf-tbDt5652utRliKrx0_qZBUJUN799Zp6dm6ZbF0VyU5mNeJfx3ojhxh6a5iiWHQQPRK15DfD9oFCyN8tNqR4skorCU9cluaENE_0Qq1y85c3xJdcUdJEUnigKSDmwljpwh-cYIzj9rtUf9dy_3HjddRSpAsBSHXdNZ3rwnJNnHVjMr2heqFy5zJgAkqpy5GAiI29q09D76Kacv5Z6s3H8beE2_jhpsHC_YOxS9hRNta77VG9Orypi9KrU7dG68Lym4BGCv0Wjd2OQjoZPx8skaMaYUs8b5LRRcS6xETEP7LAqmQiUG7ZkdSzl3E_ugWOoPegfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.4K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IA6aBSJEbh5SO1w5AOjGCpQ7YHCdq4WXyx4SRDylksPfF3q1Gh5_XVVCru3f9kHYrzs85LdwND6h-T2IquIyaotVpj7_uIvAGjTpzEUC7E-xd1Tw81j9K0IDQ5kuIpVR4JYULVX3BoGQjAWZJ5RTUfaYfkUZ8RNv0XDo2dQjZoCCzcP-_1oPW9i1Q_5GPENhZ8nhcSY9m-cIzb2H4F9R5rxEpvwXkRDQGF9NVhJQj4tN0k_IftIy-nNNP-cLc1UINP95MLFPQ2BtyZUaDD1nLPfKWrHyHmuRBTwP_1bX91jT5tfXSPpXu4JWCotP2uv7MGtzPfiXfcwU8oW4fxYBow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
پیش‌بینی خودت رو ثبت کن!
🇵🇹
پرتغال
🆚
🇪🇸
اسپانیا
🎁
جایزه ۱۰۰۰ دلاری بین تمام کاربرانی که نتیجه مسابقه را به‌درستی پیش‌بینی کنند، تقسیم خواهد شد.
⏳
فرصت شرکت فقط تا قبل از شروع مسابقه
👇
انتخاب شما کدام است؟
🇵🇹
پرتغال
یا
🇪🇸
اسپانیا؟
🎁
جایزه به‌صورت فری‌بت و مطابق قوانین سایت پرداخت می‌شود.
https://t.me/betegram_bot?start=p2_r4EF37DCE</div>
<div class="tg-footer">👁️ 32.2K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/blxsZRunyg-iJoRwNfltssY7jldyzl3AkIDtl6gfXchS_K7d-9Z9yVN5fjNOlxoBDXV32CS1jltt84-MfrqZMwk1dTzqOHT_wovyzMwgDZXKOKLrPyMPxegNPtGyruB7gPORYzrwsP5yRZOOGG_LoO-SGvBfZuQXmRUfZkDItet_7lH4Skb17aDr1vwKx3Bc7JOaM_Bnfh0pvlxCA3F9TbBEF7EpnFqR9k4ZY9LbsbRBnsP6hGGG9-SZGAOdVGXBB8K8RzRoCZlcPkO2UPD8r0AHmDENaUH-dULJg2VTDcXWIfR2MRUrWPIoDylovKJ_Nu6fLrD-LlFJoq6kXc5dSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkNz-7wJA4tpdsciNasX9K88NEFiiUItO0PFAJzshY34nB4pZ8RrhvnJsgc1Z_7iXsSR4TGg-_zgKM2GY487fXJ0GEqXwHP69lVfLc9Hnn0acbd75ZhmtqXVPXU6iC138DFnPlirJWMuMZWcW_iBESZgtI8HQIJIU3YHrOHc-mPMGhLV-sfdCn-XBeS-VMWM7B4E9qcczzuuqjvK1sSWMLPOxzBlImFEVK9ccRgND1Vp-d4YlsfF6Q8MFJOZ2Ybs7etmJxWsu_iPu29J6znZ8z3AmW8RM51FhOPrjEHgg9Jzn6Jx49QIvE6O5zaAziO3MX8Gt61X53r-_zK2u-vlSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l27Zv0blkLa6Sq-hr85jRJ50D9IxXR5qiHIG8FdgQLIMhbCgYxQ3SXDPPmNsVFfpXLtesx7cPN2n3pbe3ilA0TXofZI1vXdSsNLIXLjy32IS9sFJqj-7vn6hhPi5mpCekMZ-JHHZbf1A-px0DFohfmLm-h77xMkq6zmpSmAXa3D91iRIt-bsS0IPln1NlC4zsYt6QqvRLRBqiOc_bOPG4YxnzUcmWVWNFAXKT6sZfmlaPhse6-MLgjlOVnws0dfVXIeYCYtbv7AKZxB1kkfWKBY6B7lfiKU-cv4phyAQbKk1pEHZ9lRVfdTzg_Ey_-IcDDTGDHSEfqPy2nP2rD30Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IHFNnEPe_8BdpyrPRZlgUCw6AYtAJMZCMIzmJIYdRgYJjOB6rHPJnGRWgohX0VJjU_Jg0vz5ClHcm5FX-nsbOfmbKSh5u-3oyo9XqreqdLqVK1L6aaVQm4qqcxmgYu4iFflIm92BBCxYNvmHSifyyrtFzqhDgIySS1pYTvhh2--8hHYeSM519PeWOisdDi0lUvNMOYl_DDx3i5_MXRHAxCLHZlZ9y035q1sV-pCl3APBmdDORBmUIbq91NBA18VHqHUXYKmfra8ZKL5EBDv6-jUgagLWXL_yql2xITp--9XLxtW6N35-9gXwmY_fI0RWqV0SBzwON_efK0fQ_VM2Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rgv29uWkuaByt302QSMmkjqWq4YDCNmYoPLU8z94N1SHw6TCZvrt99lhGyYcN43VrJrzKmHtZfjj2RG6wpT2rkfwGQ5Oa2GrxoldfXsDxrZoxWhyxVvw2MrGaJhAKitPc3cUwbsm2l_Z--XDo-OqjRcUra4Ajz0Zw_1ucocMknoiHKUfxBhETpqcG5n6xQeo4YUpB8rECv4K52XFkvRmettfZ71Z0ZAitGPiwuO9WT81VItmQMLJ1L2lAdl6VchxbEWP0BVCQf7ChRGubA-_-SFVBxTBERg6WC1YyR4C6tkOZeUiOzmFAjBexSQZ1QFNDxPzBe7Hr3ZcX70DejEggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8N7CkeRJbrGnQuWIJXDEFX00cqI4HE9Ds97lVAatYClPt-r3jTZMtAYzrGNdODughGhTUcrnfeYRWruWyqOKZMaxFjxGSPnUTpsoxI2tVKu7p9qiKutmWW8aoK72Cl6XuJimLFkYNDY-s3ohtDYHNMVfGz8mggsfXYSthT6_1zVl630Txn9FqnUPAhtPVoeO-iKSM6jLxubxeGtUuSnliYo7Y2fHTxMWUd93GPCBDjzi4OUPnhJjbHGa-dRhgSdzy3ly3oddWonUenO45zmGefKi5muw1_2AuWDt-kGRfGvLmOfONkAPU8rU7BpTJ2fALNjMu37mCY2N3E8DcPEcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/24c947b2fe.mp4?token=MlIHgXPh4qP7Kxr3EB5gd4-tYWRwbTVzFqgHUh8YLm6FuRGZyZNt_lI4G7Zvo0qIcTfniTN8Z7FbsrOoVHm1eysJYuAqcGygQCXWRjhcz6Gaxx3644ulENv4FNbn7IGFPYmCIWw5mE3_Yh_YjdeBMEu0O4RDIyQ4PZin9x0PTFz7ecLLFBzlD9LI94Xamgy4AUvzJiXsFL8fSAsH6xV0_-eyY0iM9hMLc5hZU4pOBNcorU-MVk0t4n9IuvWk92LmQ92gJwg5NwMytsIVYOmpevwAZMmA1JAXpkcxcl2FxNsPXbwAtPLnk5KuFsYdmBXT6TrJUe8eywG5XXd7S9f_GoY4PnnZkcZ-GZVKJWVZED2r1Jx9ITdX4-t6Zhwmq_v4jPNP6m1ROKvfeQ90uaetJAyzNFkw2cvoibcxjUjqDEPZThr1CocmZwNOZoaP0ulU3JKpKXH-OsbFR6VurLcqP1NtKjo1NGbVGSj6du73GwSux9eVhSobkbbzcl895oROUBFMzd3_3boPVBNV69oflpzM7IViZ6kA0_5MKUQRd-Isy1uFolVwrq78ElAnNwKGWhMbNZ2fYMrHrKq3IgQqjL9AdxVF2sbuDJgmD1wGyF6ljWDXS7vygT1me3rYmfNG-K-SmoEZ0IJ2lvJ9SulXgPPxZ-66nTs9XFehgxBUGQA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دونالد
ترامپ رئیس جمهور آمریکا:
نمیدونستم که‌ کارت قرمز گرفتن به چه معنایی هست، اما وقتی شنیدم که به‌این‌معنیه که شما نمیتونید در بازی بعدی بازی کنیدگفتم‌این بسیارناعادلانست. چطوربازیکن رو واسه بازی‌ای که هنوز برگزار نشده جریمه می‌کنید؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MB1x6NC-iiRiczoWmmGgxLns5JJLd3cWL4b30emzT1TruAatRTMh6RFcxTd9PlTGObAdI8xXMz1iT357DV_aUi4V3sNVi6I0t7VYwh5kkrNkp1ZJGAvsyk4r7uOFxw7l-M53zIp0mJvuIXNiumJvu_mA0nH93Jl1V4NFXowQwhmAlonFpHzuA6GZznVuBjZ2Diyi6Ueok5hNC3NCHPNmXPxjioUofvPPFK9xwdB8i1TVErAeb22G3ra0FjKEd1-lvSfVMFmbY6Mgwa3yllm5oXVwCzl7cMUaFAepi0OaiA_as_oO614pOQmEGwLqBDkvM40rHr2KVJvLp0wJqUnkAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pxhMIaw21gr57EMmvOSpQ9y_yPDVJY_ROmR4_wR_oEqoYM88zhBaSSD0hDNb_rnzbxzii_ZSW9lRSQ4DDQJ8LsMHUWH1R2Nrz2k6OaMxvEymIvZ4H_fpEmZcEGdqch4eiFFEArT-IeS-cFv1bmAIb_LtpnX_umiiksA0EAP40vclptE_k1pPYNw43tr7LfKAbzCo-aDs_NXBUNLbJqBB1Sg0xnitHryFCc76SHc7vVM60QhfVV0EwTwSvtnfa3TSY34QSjeR6uZzlvt2pHSAXNRtf4UulEgdQ_Gabvs2PJjB_ZwM7EEVH8WiKCygCuzOLP1557cJNFe-4SvHqxoqDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LXEYrNfFR0ui5w61Wkb88stMMMMv1oohBDR5bC6iLNGEhkx8zgzVW-Rzp6Q22H9rGuH2ygxD4GMnbhqzB8vxdhoKgEuVnoOMTAiY9M3qZipbQjabCa9QXYN6rsCggPjyAEbYYcYqISB1EztG4kd9whcWpNDfgGXArKhTT_w0f1sdUA-atAwIoELGPHeKMjtgaE29UUPcoeeSbMyaeqk9gt1EANLb5YlcMXD7471wjGANvt9PJgLGC_BxpRNTV7AtuX1SLGFOb6qB4vD5_biumWA3yUdXeXIX5pMdnIVH4y_4mGjp4ofvEsjC0ga60RjrqjhiBlGEF-RaKUE6-i2YWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mKzrWkHRvLs-uOQjwmpZnWZVq8TqwFJCkYvAj0qLnAXHychwHvYC3CNgPN09WKmS1E-X0CSEg2zyKR__WejJpBSSEuQbubG73vcHzJ5wS3PKegjY_muV8tzDq2oMhsU-1vHMX1loacscxl8IJl-zi-APp0fIaMzkKRuL2swLq0NoeQczM3nvzVNOMfFVlJ5NJf_CsLhdkTU7zewyN7064k6-fzTSeyNMoQmkTQELQzKgeClXj379aelD8F1pfpYSIHWcvaHV0_NhNj2yyoAEXtQo01zv5vTNMLtkNDcZlL533-8IX1G12RVWhiWpT7fcGHJGUJ9AEbisoTZYDOKh9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rmKcfckfUyMbgxUlIKcJczzzgxk-6mlgT27Z7RvSdJgwySqTgrTGuam9Rn_wZPnjngFGQfdTm-ymfbUujE0M7K9QEWBbKf8lbv6IL0BNfwhFedgVwfI9s1R75zp7njbESWJJcvGsFJkqlZU_Jrh8XlOlKRL4SDnG1_9WtX8reinsWx3Ji6AOrI_XrGsADCwmQMcxn2uRcYRr4VLkHco5eUwgRTFCs0hFaGFzNtIvrsCHBsWQ3h44d6uhpq47oNEcGzkxxgZCjscBXnHoUXusPwS8MQ7mzVR-JXPoyRHhOfc-olBsUCuPKbOjonwzjDx-lZ1zgpRIivE7ok_h0EckAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kcNePoO5K3P52q1k5SEjSfLThauOiRb9-SQYl79kQMs2eo7cd3U-V9g0obA5z1KwV5YnIO--pEoUTfiBSTzdDSP_PO5N05UfBD_WhJlwciN7VfY3yW4lJoDcvrMWlPghBDvDxggnfRC-TMxEJXhgLxUK-SnOyJiAzQFtCWt1qdwtBEuQUKfuH5KBT8W1BeEiwZp7fqShVZM5OuOPza-1Fg_ECHOJaUImU_app4d8tnIa9JsD_V3ohU6KrU1XjJvsxXg3PMH02x7wKOGwMQLI4iyEoFsUhvinlBuEZMwUf_HPZd8sa_ILYgJgb8ZYaFkY7klGhwYbzYtvzDZTMAbQGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wv33PDrxW0R47Y8Z8qPrkS_vB6FSbZvLWiFeTCH372PMYKhttmjPtr2-HdMZTvJcO2MZ1kBpAmT7q6CtuAfSA2MRHx4X9L6aE8E2R-46ViGpMrzHiL_ghoTbxgqN0s5j_rMr3eQhJFpe1ThHO9WylAjYabuK2syuTY3a9KY3cqDxJ35H5gbbWSYdWEIgVi73Dtt_JtrohIC57kjmqp0QCO8riXvHk5DzwgLY1b2HWKCRYezAa9uSAtlYh9DzYSsdcB1Nh7mbowWbli1BGw8lQLjwnYql2hNg4zsNVAg9uEiCEcJbL-a07uab4NoQS39hre2Y17Up5N9M-EZjqD2Uww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nwjBJI36Bc_iEi2nKhajL7HokReJFnECTG2IHyfVHqjWbMQyQRf9DPIRHSfIcdEGacpe-fJ7MOTWRf-hhybq7fEpxvRJMeOz7h5z7LAcnZzEoiPuLvjbjYfgqChFFAEHVtpkkiXi2W22U4rbTXTfg_Yic9zNs618p7G5AfZPE6f3wrSgXuvxw_fZ8iSKU5Yi5Yn9-RiQdlHYYaPjJ57kMm_fbDNzQxncWkhxG250qAF3_rrnK4gCcLalgya9ZkkymSKyMSw_RGKm51wfw5usPhlkaxobgoPqw4eQR-jkfF8VgABUPqkYFhdo_VWTCsNaKSk-ZTrhzxs6g51IVbABTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Es-YXevwXZ9d17ACmRPENexkVB_VCoqxcsNnVVaJ1ybpWxll2U3e6S0BCe33sMouBx_Sgo5usmK71e11Rh4UCD2j8O67LFp0B-iN-JY-xNk9v-YFL8JaT34m-JzbJ2ALJmkerzsk3Isv66PXM-K6rS7vA0vwRVx-Vmaln1UMjqv5tLR79N7h2ULsegOkPU824rxxeAsRXaz5t4kTbWuKRpiEMvzyWJcfRmEXlpl-umrLs6BZmY7eewuuyum5Mux2xbZoZu7MeiLsZ22YbsGFir774kM1gSDvu-5B5dKmFKtrIRbGTXS1YIIBI3BHeU_r0SNnGwixh2UkG6eiHJtuVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OGCRnOWdc86_ulxOrzs3flT2ObGGXaKa10lix4bN_zGXPiqjkLsl6H6fvCH5H2zUKfMTODjhbB-AU-VhRtwdeE0TU-wbXSa5M6C36FWOEt4H2kIrKKfcKXyON_lSYyNn7rsySDJ8CWw-EQfSBzwPJITEgLTC6Nur6oGoQi9eBPKbE05puK5-5ccPQF5w4kKUeFg7Ml9hdS7r8kjT7kvo5ZKsaGx5a0Sw2dlw5CwSxDucyp0QyKQ5-5Ev3XzgfJccjALZbE6PGomaNoNWEQWiHFfLC43F-kMqQ2x53Z4RVm7QR11lficx9kW48p0XsZm2W2CF2BWaY9LKHaobCmvStw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4KVl68s9lyOpyciNuL8ExBJgyk96gAi2rT2C11T1Mi8aWezXHFDK-sp3Krc0GsBLSbmcTB_TmuUdWxrBRqSTCdl7C5wP2GeseANOO4V5MKcSj_SyaOYGQ6ZLHIcleMykG6LJ879LUQ1A8BuznKdAYoFDTQFERb8fPd5BJude81wrouyZLD0O_E8UDuVRPZWNvmsRbrPaa5Qrif9EOxhC-nwhk9abySdOYMcZv0JidSrUpquQFSqzwzyx6Yn8wr2Ww26bxoRMhnOAsbl3RGgsdqtYDzOWA9iOZjcSHMivc6mA2jdWxk-fLABArT7VRAc02h5SwfmIKguVCplho9JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZAX__n-x_eKeIQpAqRsNKKOck5I1tfv_ZPv7hWSKlp-phxvMWinfnOg6d6Yc1zVvHthMY50IKqaQnT0Mcajen7JUhItNBO8Aqrs-iZ7jwPbQI3XXP6CKjhha1uQiiwrm-LihKJHWRRU_yg8PJUzGcsdtWqYKjZEv-PbCwyzVraQKKyshIVT-5L-AJbFV1ohMPjUNcejfnXOw1I54tZ0IQCpONMDd5dC0SmCw45WkEwUsTT_i8iIJwLbhE-y0vJdw410WS0nHdYa20UzZ153pSq49_Dt7X0ZE7Gb470oE8ZqSn4CiVCT4Opg27wEJl889JauXPdjeeA8VIs2bqECfng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A62YeORBEqOd7lDyi3pTKs8q7wpggFWY0i22_qRN8xeEOmcZJdAyUPwsTdsIo16oZtk6gxLJ0MclufRyRbR-z-TnRh2fvb9PZPEXcl9AgtovuYSVRLXmjTeFLcReqFtgYFnMsIV8Sevf2nl0_pXS2lgZJXDzih-5xxuAiQT6KrBCGdQAb2nyTq_-_bWvZRtq9zdWymXoA61mmiLBZHNpnq4hQrhffDtv-hJJbN7ejN1BpW8prCCX6wAhHASUI0BYrmMQ1gJT90CARk-nxjL_bjGqTNA9g3GwpMMo5yzZ1Ye7Z5nymikCNClci4B_Y6_GgMILNzZ9Yc_BIlENFuEQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=WVxSQLaS-44OLYeZYCKa5gbZ2ju2lJdNu6uXstrua7rgE_ufE-4Kg09SUEifMA11_p4jDcZXWcAqK8yRRgsE2bnSlVHWFvRFaaqxKgEznSZra1EsDJA4Yoyn2djYH2ilApwpNP2t8PeupB9Acu5C9h8N_U4RgKfx2oXQlB1VpM249pRcaYFIcpZh4cVj9QlcscnEuWkNxoXwz8s_8MLzxWHPapR1hMjDYU7-WgfSAYoTQoMFcRFc7gKMC2LVCanFK99ZKCaRUVrY7GD09M9JsuJCIS0RmdZJFiHAD84yCJEOXR74iWbtvrXzUF2KP_gDOyK5GAxwfgBAFORxIGrXBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=WVxSQLaS-44OLYeZYCKa5gbZ2ju2lJdNu6uXstrua7rgE_ufE-4Kg09SUEifMA11_p4jDcZXWcAqK8yRRgsE2bnSlVHWFvRFaaqxKgEznSZra1EsDJA4Yoyn2djYH2ilApwpNP2t8PeupB9Acu5C9h8N_U4RgKfx2oXQlB1VpM249pRcaYFIcpZh4cVj9QlcscnEuWkNxoXwz8s_8MLzxWHPapR1hMjDYU7-WgfSAYoTQoMFcRFc7gKMC2LVCanFK99ZKCaRUVrY7GD09M9JsuJCIS0RmdZJFiHAD84yCJEOXR74iWbtvrXzUF2KP_gDOyK5GAxwfgBAFORxIGrXBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSH8-X5E43xJYN5kzNZJIkof-nwHRadEfjIQIQy-OfGkL49m77uMLLh5YLer-QKDNQ1dKEwnmNaAQgPIfTZ-Va4d4LAHsdDXZFqaCW4ULO-nz-XG6OUeadXUQkn0LRoAh6HZ9tWhiNyotCRpihxZxNVw17W5VEUfndVrAHuDVdJqQzBe5YAZdFmNW3ma-5IC4-VWMYiIckXPEMTUZC0qNZ4zqi1rIwwqlzdMQKb_Ki9Qyd7Jkmc3Dkwzq9nnnb1x71B8uAE2C0BzJ7zhaN9u6eq8EGEQn4iz6Jozjh31NapdtB1O0YPobNKz5aoNz1Z0MnezTZh5_LkMLi5rtfk2IA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vYpsuU0F7Db91lkw2stWe9Oi1uGV_k6s9laUJ9OmmMlqhsJjzfja4NlIatEIXuWH2TifamnKoOlOl3urojmvAtyumxGA02lh-esG5_MCOPDlPbExi_jwJTZJuVoTy0NqGhA_0i0ENbNBqcXgEwlXUTTB9ZaxO8gjqOfiUfPV-2XdICrbwDhE6HiKY5rGmTCdKav7rYAC_t0Ef8BdBIwf23vJr63Y_UiI2bnGWCoPdYP1ORxjFPd53_P-JfQOtVUDXzzM7QzaQMK4Oc1iN3K87HBFqrhwoJcDFyhJqPoiuC14U2wLAskpyd6SnFj2H0Lv5mYSSYdPgH1gnbUO0gnx9w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C7QVFh23o2Ayi17-KJ-VZmQ04TFWpqG43_tyP-00WLIIENGpCDROt5kyr7IQPxUh4h-FWfV_Gu_qKMkizPgsh_iy-umpf0T3q9g5z0Nl-haEW4mBlsSy6bUhIZJ5oiVgMBaz422AdH7UgOaL284tjcnD7oHwNbP_FT009DTiM7dfdo7XId6G_R1ckImeUeqd1uCGbNvG2tG-VDFPlHF0yY0J_PRdz4tODGVKyHUlkB8MSutIQLe1hZgOSH869kc65o27hgrIaAxtgSwJ1UlE-Ci7V-w6md_9gysk1WGFMl5Vt2SbhIEsxyFq91vb79NDmIGVqeoAGy0pbbuCPlubUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lHe2Azby2S-9W5shxq5UyNSzSI_y2EsX8Ph8Jhbdq0OzHhOdqRVBvSWOyB6_tBf40QdlKsgSo2asDRXj7PKFzt9Sttwkp_Fp1mMDj8YdI57JF6OtCkQc8De74mDVbShDMevft6xO7M5HtfU1rLJQMr_TG8J3iFsBH3sUbBPCCEMBq6u5W9o7tCfDe8uwQcP-n9nAh1fsvpYztjyrSJ5wJ9VMKFiYGq5GaiHWaoIkbYj-y92y54Jzs_i0CFCxeaJBash1GlyRRqVLSWYLxNQ8jS8BK9ruZfBfFCaVbt1QyzdtAGJzC7F-RcAPvq4AQ-os_UoaefMVMoPyAM8NReRCLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHRyiiMLQRUORNRe7mra8mPHrVFeYYs_HSvY7G9YluaNG394MzKMkHkXB0vY8xg23uWnR0NBGU4RzagmIkxJPxb5fshXUwTL2R0otSl2coC6UycVBSMDb8e40-AYNq6Lf4kbOk0J-nnJQRROWrecTMuDaojPEZNLc_BtR2_skdYYAH9eiY52M5mg6mjVW9lFRBhn_UmTqHAJYz89_EBROm6VNmvl_06OwCzwHvJ8_qmZPNlxS8lD-pZsNl9NeyzXTWDJkxKsBJ8ttfQTRYxZJZf1amuNJZenMM5aMBTpipH2099s_WAk1t5CEb1Y2OfSuRrhD-TnhtwN4FFjhBvDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3u1zFo5vR-nu97moXX_W_T-pUOU4Jr8mIUttzAbUXzBymIDkJRLpaihGSoZa7yA1v6_R4x3AaU-tf94EOgINiwdXu-ZfegvAtIBXacSylFKb-RXCNwfAe8jRB5x5WoHj7vbGotktPeCyx5GuvggOZ9dl15W4k35WOP5lycaOknpIhJdkIaXlWOTr3FgKjso1HKm2o0FF-zE7bGRjqb7_u1tYmgELHMvwqEVqRdBkPb2eAMiTeoLf03p807lIJcKPOK1Jn3ZRwLYtud1Nw7MxDNhNQBbRQ9RjE8MFGjd_h3NFtpNHU5OakMHKd6Ov5s6NdbaYPUCZLl_V9zZg7JsQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XV0DYBuLsurIG4FCWbUT8veYEYtXj5WCx51FHwfQr7iLwx97FgyHPYu6B6ZWZ-85-SZslyU918G3oFzc-HlsTjvKuQrrHALEAlD_ctBjwLN9Af8MTBJw6S67nC6cjouS6HmOC_7J4mh7AWbOhCZjIbYqrYCTzhPOiScybvktZNzC7ARx4X-3U_r7ERJFAYjurV5Ol0l7zrKiht_tJU-n7tFgQrUqFsPeAHiuCk4daWqoxE59TwvjGItt54AzAaTeJ9LDs-Z1cKTO_duGsyCb6HbW6PElVP4vkmh0BQKlrA3WbczetPjmc7xkrCAPkN-FSbtI22WG5IgXS9mR0i1atw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=ZdOM6cOlzlP0YC5ofucdpsy4X9vrt6Pw1tF5FRisLs6ZxLHhwez1q1z0gw5PbbY66rhZ2Cj7HI9ROda_GuzfXd-KKpY0ILq7jkNketzzOOx6HOL5Q-uM3pjbHaCrbMqUj9JwfLBPqEVzpsfbUFGAatgHWB_-xBE-U1B2N8rMfPenXhBb1_wdVvyvQpt1FOqvzVZtZOUFOsJTlYJQDJhYzASqC7SVebPBafhPvJtbhmbJ4JjvRqBrWP_rPLV7xeXZ8Q-hD9xsXsXP1m-6Os2LRxd5qpcHQajHzvM9v6BDwODd1-4EUM7Ev4Xex1EoIdtJUKhebOE8NiTOejeFTfBdxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=ZdOM6cOlzlP0YC5ofucdpsy4X9vrt6Pw1tF5FRisLs6ZxLHhwez1q1z0gw5PbbY66rhZ2Cj7HI9ROda_GuzfXd-KKpY0ILq7jkNketzzOOx6HOL5Q-uM3pjbHaCrbMqUj9JwfLBPqEVzpsfbUFGAatgHWB_-xBE-U1B2N8rMfPenXhBb1_wdVvyvQpt1FOqvzVZtZOUFOsJTlYJQDJhYzASqC7SVebPBafhPvJtbhmbJ4JjvRqBrWP_rPLV7xeXZ8Q-hD9xsXsXP1m-6Os2LRxd5qpcHQajHzvM9v6BDwODd1-4EUM7Ev4Xex1EoIdtJUKhebOE8NiTOejeFTfBdxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l34sqmnj4lLtuR8QxwBLf-2iAuYImVazTuK4-ARF-Fi7Q84vUnWnDLPY5KtADv8sX5DXH4BXqzMuMXHahtI0mGliGNCn3Sx5QByxjm8v6xbXhqGV4ynl0GmN_3LozdJaRlE7vVaLXo5yjZrQeRao6wvCy8rGToSCHCrdYGsO68UenDeTU0ga7uxAUsNen2vhevvOIKxOAfuBOSY4ahcEmEXKKcNfGItYlEhbZ0bYRghbvzSJJMQtNKteFtvHxpLXckw96AcKRjN33MbaLXeSHS8GP9nt0Hv-hv9U4sY9O4v-S4xzjhOX3ZQs6Xfz6j4fB-llrq_YY-kbl6V25h4EwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LgYvgcTPiiBMVhnNJgepGaKMKpKGv2WqZ6AIv7t-JCefJeKleXRWpcTcfdwCvSiBAPZwD4yWVA2s5kIo-el9nD1jKWqaBS6uIGNAVkrpH9R0YhUYzRU2M49dvU1g0DVzc38TPU1LWLel0KcZvajR7SuNmRGk-k6dBsrTpk9zNVcDLFcduH_PDB4fxDNCFHz7nQkhbtGOV7cnJGOqA63D-oBeJD8sYy17iOt6sjyIrI6yM5Ttxnsf3KWc9vTFh1DjjrSLXQWNzJZwW4Q5agGKE9yA-DReUtN0gBc72xpzTLkHpPu9RfO-D_2LGQ_kXTQ1LP_5B8iDhWuVIG6xJD1hgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=avZZViGxoTYrdXUJZCuTbVlWbh35RliSgm4BQVTjykMJ6mutpYiAuNULTLfDicWnxyM_LBHeZyMBgH7lhGMqtDrw7VJ_leda0xGbO3G9FtBOzRJcjuEwNX6OujfxrgXNgH62IZ5n9PgnLFrRv384ObYr26KQwgMeqcqofV1VKw0zYpoQAGNfhCTA1K6w5F6j1tpL8BKZmmMuoTarhzh6Sbit24iMTRMX_9iL9sSBjSqcGfRB5XpDfVlFZ-qOKOCl3h7kKgW7DLj-EE9HVizAl331P1Vwc5s_WNLZLQz3YctHkftH9gLU1VmReJbKxTmXagGNZxIsxlvRVy59-MUEuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=avZZViGxoTYrdXUJZCuTbVlWbh35RliSgm4BQVTjykMJ6mutpYiAuNULTLfDicWnxyM_LBHeZyMBgH7lhGMqtDrw7VJ_leda0xGbO3G9FtBOzRJcjuEwNX6OujfxrgXNgH62IZ5n9PgnLFrRv384ObYr26KQwgMeqcqofV1VKw0zYpoQAGNfhCTA1K6w5F6j1tpL8BKZmmMuoTarhzh6Sbit24iMTRMX_9iL9sSBjSqcGfRB5XpDfVlFZ-qOKOCl3h7kKgW7DLj-EE9HVizAl331P1Vwc5s_WNLZLQz3YctHkftH9gLU1VmReJbKxTmXagGNZxIsxlvRVy59-MUEuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=uAbG3bb8oXg4i-x0cptfGg92JddSh0aFjrE_xWn72lKkwjxbxYtET1sq0sEfiEf-7LtbjUtF-n9lmqgx6-x4svoxYDWkY1iGfnTntt5l9RpwOzYSNKwzSRPRBf5tljab53CXbnWT7P2AVzfsGt8XKiM6DFT1yyRXBwHFu__DlEzrxjZOC_B9BR4dCuH7BcxC9PWJ5d85uY2JHwuxqUf2nrM1c0cBfsyFQ-UjtVQICRDfE7wsLtSWiXQB_ygLlfvKaVTVk5HVn-UBBUCtGeE3n9OZv1J2Xo1dGc8zsEjvfHZ93L_BWw2HtAyhFHlvPrWIx4HLe5TfqyMZFjJ3OcQggQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=uAbG3bb8oXg4i-x0cptfGg92JddSh0aFjrE_xWn72lKkwjxbxYtET1sq0sEfiEf-7LtbjUtF-n9lmqgx6-x4svoxYDWkY1iGfnTntt5l9RpwOzYSNKwzSRPRBf5tljab53CXbnWT7P2AVzfsGt8XKiM6DFT1yyRXBwHFu__DlEzrxjZOC_B9BR4dCuH7BcxC9PWJ5d85uY2JHwuxqUf2nrM1c0cBfsyFQ-UjtVQICRDfE7wsLtSWiXQB_ygLlfvKaVTVk5HVn-UBBUCtGeE3n9OZv1J2Xo1dGc8zsEjvfHZ93L_BWw2HtAyhFHlvPrWIx4HLe5TfqyMZFjJ3OcQggQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=v_1LH_W04JQjNLDjLUb9QoagcBd6EUjhIEdFD2W0s3yasE7JEbwU5CyOeaXUcSVDoHRwlermyb6FOmkChIseqhpr62wjFuvnYAE-i3wkFpmd2nv6jpR42Gpq9Wyr3RTgU87pQasPHJdz4GDCAjZcr_RmPnsn9Iuk5fl6wsVtMTX3urrsHDWhOiLG2ELYu0RKWeaC249meR9i-x1bl7zWzdPdFleBxc7nJ5g7a9PQcVIDhHlEfXcSdWqnLThHBHQVtZjireFW4SylPwQKmrJhs1tqn8VZM5RXc5PGEy8Dg-5Be-Pe2UZkKLCcGVH9Sisv4Bdq-4G1iEBGuFPbROcXEw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=v_1LH_W04JQjNLDjLUb9QoagcBd6EUjhIEdFD2W0s3yasE7JEbwU5CyOeaXUcSVDoHRwlermyb6FOmkChIseqhpr62wjFuvnYAE-i3wkFpmd2nv6jpR42Gpq9Wyr3RTgU87pQasPHJdz4GDCAjZcr_RmPnsn9Iuk5fl6wsVtMTX3urrsHDWhOiLG2ELYu0RKWeaC249meR9i-x1bl7zWzdPdFleBxc7nJ5g7a9PQcVIDhHlEfXcSdWqnLThHBHQVtZjireFW4SylPwQKmrJhs1tqn8VZM5RXc5PGEy8Dg-5Be-Pe2UZkKLCcGVH9Sisv4Bdq-4G1iEBGuFPbROcXEw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=ZwH3LzWz6P7jE5ioUyYozcqzzW3gi2jx8CgnrvcVz7sSGCeEhM0Kg3y7yKzTr8WPEU6R2KSVAPvILNDg_2UwKekC2izmd2SykDBRc0Uw21_ls2mcn-e38jp4PhTb4Mleq_Ir48qsMjhsft0R89Z9IuS2OYdeBE354MxzCu0XpoJ2gpBRzBmto_pKp-sQxKsAuApFMAVgyscXkCVdC2q1avLdmxU93p6wteD3NB9i8no6Y9_MlfCC7yXTD8QpgFnUHXUs-SMu0jjQE7-Fn51CYqZELm1PGdBvsGJib-LAs20ZdPpyXyOaVeNJfeHXLnyXmIGr1p1E5jjxOF7aC1f4Rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=ZwH3LzWz6P7jE5ioUyYozcqzzW3gi2jx8CgnrvcVz7sSGCeEhM0Kg3y7yKzTr8WPEU6R2KSVAPvILNDg_2UwKekC2izmd2SykDBRc0Uw21_ls2mcn-e38jp4PhTb4Mleq_Ir48qsMjhsft0R89Z9IuS2OYdeBE354MxzCu0XpoJ2gpBRzBmto_pKp-sQxKsAuApFMAVgyscXkCVdC2q1avLdmxU93p6wteD3NB9i8no6Y9_MlfCC7yXTD8QpgFnUHXUs-SMu0jjQE7-Fn51CYqZELm1PGdBvsGJib-LAs20ZdPpyXyOaVeNJfeHXLnyXmIGr1p1E5jjxOF7aC1f4Rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=U2xnBA96YBGWUH5nCtxrGqmMbVdYj0QOxes8VRJCj_GKQR9_41whnqozaLHGrJ1ob3pRdHVKLwutm6y5poCFvX9prTGIJDPeBnYR6zzO07f4wDIKawSTVeEuP3QubnXPA5-a2YuPVCs7S4fcyFPE1aiCYK-AxUQI4F19C3a0vBYD0246COSn72SfW0U3Ah_fisaRu1xhH-014zqhacyp3bD3B5gv0v74y15TCMrsI0FHurdXj4Hdmj1tWJLehS_0rVpXs0uzC5GAk8LbhFy4hswi9gSFQhSNkxx-bu1ONUyE9kPC-v-UexWG4uBkG5ycK8k5pZOMmkKi93NhDH2XPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=U2xnBA96YBGWUH5nCtxrGqmMbVdYj0QOxes8VRJCj_GKQR9_41whnqozaLHGrJ1ob3pRdHVKLwutm6y5poCFvX9prTGIJDPeBnYR6zzO07f4wDIKawSTVeEuP3QubnXPA5-a2YuPVCs7S4fcyFPE1aiCYK-AxUQI4F19C3a0vBYD0246COSn72SfW0U3Ah_fisaRu1xhH-014zqhacyp3bD3B5gv0v74y15TCMrsI0FHurdXj4Hdmj1tWJLehS_0rVpXs0uzC5GAk8LbhFy4hswi9gSFQhSNkxx-bu1ONUyE9kPC-v-UexWG4uBkG5ycK8k5pZOMmkKi93NhDH2XPoi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qhfqlmOxRuAtddgbdWBXTCLVCDXLqk7b-wC8EztXXDvTY-mNVUKTakJr7tinpVkWLQzjAS4TZBIT17aVDft6V0CPFDMcbHgYWNLQCJeY5vBbxSehyNc6BMQ8egBZ5wbx0MYP0ITiB_g2yDUSLhrki9n6IammfU4lIb_EH9cT7zeLSKdZFODtV9ODQ6O1VlSJVBtDBYIeaq6_MgYOAXIPGbByygkeqrKeD7AL-Wgb813kxsD-dSp7Kp5w5wbusom7D2Y0MEShQXfWrPwM20s88hkKq06aEGakGAeOXuph5K6HNdlguUKMT99C8jl0lNlixCP-3r23oKvl-MVczxBVMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qGD4OicNJiEpWdJhsFSXVikS2qFOBQuN-Ny4-nme7EisC1l7AkzHlu9kg4V95-cunX2kw8OyEjm6nQ8eaD2kszDlPckE10rLpafiiuwNfAqlzovfLgfv5r-EJImrIeKvhvTE5fGhJWsRN9xlG4JmrV8nAINGCd2YDkKQTBgAvvDZWzgfl7kScUsOmxauSARMXRYgd0P3QBFTTSQ8CC3TGjfqjq0wULr7QQFfFJyr4WOh87v-EmEexA5bJUAlDqDkdCKzpGTfcO-OKETCpwqP2AL-g5TGlfDk194L9RqIIrYhXLI58-keRtjk5uMtIbLXL8uRyGS4kyCxsPmXrBF2TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QupX1dQ6IWfhL9lOIt_ghAj5v-9nzrbE64dVqUzY4x-0cGXhktLuUlTG1so64qBcl6Y7WepzCsb6ro8ySNHwJBMxiQJds_bGVC2CsBCwfnIbr9IaiZa4yFHT_BJBpVkL5jrT0mrOhGmijCLt7PAKo8fcSQ7aqO6COESWQjyV6-AOK6mckPatd1jB3Q1UDzP6DmVIiLYlgYf396zRvhJb5d-f9oLnl-tqcBAu5qkS5uioddwICJeiPyzUv15kCfUS95I_kXy9KwTB9YR6N5jj2orwO9Xyo5ZPqPBhKEnSepcZrhIf8YqATePkOFMeoX_P37r9zvwSIY80n3pe107K7A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BBEtMaXvWOZek65qo5jA0R4bXakQcFZhnBNpSCayCdcw_q5lFnS09H077bvJx6Nd1SadyDvFo0kl5A9Sc6TCG5rmv_xcibBEOppIX5y5eiwPYX7BeuzV9Fsz_QazsdAzMW1WJrAGhP0iCqGEl_O5QwjfE-ybGUmSeJsw-QBOAhf6_CkrE4BK9PprtiNwW8zpgea8nVPl6tiBQwS_l-ZYGxVTXFUyGH0Pb57D767oWK87OF8Pcvmm-7q9HpIr6gWweQG7wMN-Cu3LdsCJW2xjr6acZ6hq6nby46HRkV4IagdXFk2RMqh_bJlBSOzb3-F_5RSRpQ4sgrG1aaROdIX9KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QMuZqTqmp2jf1J9nmK3NSgZm5yUkQ9xpLy72tBtHDOB_c2Mg-wV659AHkzUfiIJEwkGOdLkMjf1xGpxrcGW8xUt7Zd8M9BJarmbE2bLRtxs2KbuQfZyazJzKipM6FJFZFmod6ucNrNOILRZkyjUIpahMXqHsjWad6ImqlSxyXUWN9jqJPaL9LXWbChwKMT8AkwQ7ux3IkOs4IUaPv2DfaDl4OKXQFu4Y5o72GZD_IEKJcHV2lql-EPhRNQ05hUwkPgfGSpnwpXhYhYXXmvR-RROYi0VpmQOpC3ucYGwT9wXwbpjvLB2srepwy2csqG_4U0hur-J3ZPLdFKzEkeLJeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AtukKE9Efn8wWuWqEu8PRYtwrky7EJ9wfovOMGUMosYuTmvyXqPEP8W24T2NXdmLvezZhFyLPDnNuCVbngXBGLW976uxbj-Vrx-g0axRUvLH9WKo5rC-U7_Ju7_hjSIPHprsDxrRx_uKcXGgEXnaxxYzXkvUmJHrjcVmSf7Bys4OsO3uVRpiOTU_Bqt1Ip_nrs4dr8-CIcJoed7Vq0VlB4FX_Bpm8KuGG-uRTLwR6CSGaKjI2SvANeCGySYwrsGshjE1WTrAQ82kVdYo41cD7tBcRsnPf-IHrxdfR5del3-NhYIqJQbKSeFjTnlRg-H5L1wySJHTrmZknKrjEQhbcQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TaRsbyXbw0q9QnoZbH2rqrjvP6jH1-UKS7tuMQ0cnMqdz0HzyNH_ac3E3YPzgYnzmDYBj5LTY2TJd9aIAEbWtZPSWu6tC3ajzPY2Yl9SMMywmzwhfCiykKJKGhpImmTD6IqoYCVZtXXI1uTlnPdIYCYZUcMeHCgjUNNe65kPkFysNRh8VLYL0O3JRi6KJMMOQWGbvH_2-Fc57fHIvX5vDq5pkpukaRG4yBOz4-Lr8t0718-NDfC7y1gPmGidc730o8t1bwQ26aSy7k7Zgiwo0ZRhD8H4hX0nzdaqMBNN2XBU5d1JVLKl9Fg6zkxMhUJUMB3bgEXTp4JROB2w7LEVWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PWv-snTBmT8JtUPxggJ0-bUp5MjKATrsDranUs_pHshBjdFZL2lQ7bCvvxU7pH6N6jwpBJ0UWslV7gU4uzO1wYEr8vMusf8nPIWxSaS4seQjtLhw9w26gZRPCiGR3_wQdi-hByBVI6JGHu7hlwE9kc0iRPjXSFrKABrYgumTvwIwFkc1zDFpEGNoChu1Qkp7Kk66fIQAqOaN51M5QE9Z5J3QDPNHB_vEwppy3SrPv4RlYAdzyZJ7D5im5l0AxnesRT-pf6KPj-azrVPJsHng6ZLTxgeTfXOeg9p3rw5y47lSpFutiujJYi5viGsTowQ4LF5xlmDMPUxocAX-P8Qpng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 73.4K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y_G072Cycej9Kho6QZ__T61beqAwNMCBQFXbwdcHR7Nq7alUVXWFtcNHqkwTh3Kdsi3KxGxuo7KuxvIVfqwPJnuPEDn2Khy1FhgKbD3_FwczjvIAtmxOKEF7K6qeWUzRiTYNuuTNxS62p23_qYm2VwuzipEQdVgfC4QwAnfCFB1yzOpH_e01IHdHfa3BtkrwJfBzlqpeqamxzRvGZ7bQYdHTEDCdRDzLZ65PjH8kTYdhym3ZKHGYnGw80jo_doFM0gtbSZU_sAuvx3CSykhzQEpVo03_DhSMi4hd4O9EjFkvcDRf6206qX4P3On-owH-z5uscf9N844MdVCUETl7VA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 71.7K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1KX3kLRoS_D5Mq1LgPmJKZQkOCkgXQMbFvvSLlunV_aQ0rAoYrPF9-pmK06y0JXvCKjvQH-ALXd9DlYSVQXMIAnQGQs7gsGxOu2-o_EyiBDkzLMv4BZnRmDwTOh3i-hKSI83sbC557v3B-8hGfNdEW1JKL9fi7W9m_DcM7n9dJqLkyfJdGorGpO8Slh9k98lLMVkrgTtqXXMISjrKTVW20KmpaDNh0eKxCo5Vi2b6CkQaFuSG019pSRuU8sDLU7RqYCniGSUM-C1g4Upn4u2h1aLnCMqK7lzvt6u1Hmzqm6wlSIva0GQzFegJyX3NV-6XVC-pYKz7ER9KugXqnZZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dzE67VEefkxOk_rtH6CeRosobA-5BmfSGLDtUAtW0Zkz7-VlB5Fk3dJ5cMrj2PjtDjZAJi3SfZqxHTtdrSqRCXyJBNtsPfNSPY45yNUmQQEE3tw5jHknytkledJXoHYtsV9dcVd4euNJv8ez2EIB-GILGGs5ZY6PS5LdSopwGjEBKbLUPTI0qRf48PRw_GzzbywCZ5L7QA9WOQHPKlbC-YMN63OnygScZnOkxpxC_KS1AnCZ6AuEA5YYTT8b7oGCEXG7NCqQkr3E9XYaVuGeEueRe0Tn0OvI0NNXJzj_n3NUgbcua9MY9pzQVOnmZs6cGZNGk72qKYS8zSBj2Tgnbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZWBTRuQeXQ-MsyYPl6y41xFcxydhLpSmoFMzNtnTLBo9WJgDBUWMn8KnCYdk9pZ14WDy8_xTuaAzmM8H9JKADMuRuWk87sNL1Z8ET9QFlmt7xDfh5BpjDqQj-34O3zXVv2kBXeOdAFf00NxjGf70IIV2mHe2a0BvJaQU85wD6Kxny8_Lwwq8aq8ajjKyNAAz-MQhHEGfFFYwY33as8XIs-rBzrsbpBpAts62UbGfcp2hQGruC_7t5bhxgFYV3B0RJjV9_-WhZcvZ616dVWToPe35vNH9j1CglzNh4TvD4JPiOMR12Cskupkww-0JQxuwp-Our5SbUB8sQnFkm2xeqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=Ebh1L_fgr29szpSnA0ovVCNDQZ9lQUhB5oM9jtdvz991aQ0fBm2cd5bldMM2HEjcIdWI40w62_3BHmrI6qfsqPaOFua9hv4PZZ7rMBmYY4RnfF1ikyJBvWN2Dx2BqB91rxm1Y5qXKqT39I-n-zOHu4HqhhXqgWbctTWhFMDA6h94VPh3k416_-tUqNjuPd7-hkJa59tQXgIQ1Gkd_tFQ9HKme4E_ufUfSocToMLMSsJ9-ZajuLsgE4_Hfz0YUnSmdLpfvmuiJMcx7i514TPI3wGhp1KMaqUgPp7NZCtyevDczkHYDYOOLwRfTIB35XEV8jrnATuIwKd3DIqtiYD6AA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=Ebh1L_fgr29szpSnA0ovVCNDQZ9lQUhB5oM9jtdvz991aQ0fBm2cd5bldMM2HEjcIdWI40w62_3BHmrI6qfsqPaOFua9hv4PZZ7rMBmYY4RnfF1ikyJBvWN2Dx2BqB91rxm1Y5qXKqT39I-n-zOHu4HqhhXqgWbctTWhFMDA6h94VPh3k416_-tUqNjuPd7-hkJa59tQXgIQ1Gkd_tFQ9HKme4E_ufUfSocToMLMSsJ9-ZajuLsgE4_Hfz0YUnSmdLpfvmuiJMcx7i514TPI3wGhp1KMaqUgPp7NZCtyevDczkHYDYOOLwRfTIB35XEV8jrnATuIwKd3DIqtiYD6AA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.5K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=mwIDzgCD6qagFvfhPIrDy16myuZjWCMxM5V9LNfl9zWOw3NaNCY3ZZBwFXTnBFsCcEX-gguba8QTCATlXiU8v0JJy6CnpCpQv0Zegp3ukgc1xV6GUVyDuihB1tqO-ZQEWSTvigEfLQ1YEGbAr7ptw3mQw83pQzdfUuAcjv2H-yN3HzUGIt_O2lzPWk5dSDgqg7jUZeyQE2nG1LNIRg5aN7dcmaTRv9hszsoS-GhEIbN4UWmJ-eqJfcrohXst_O2-0mPWBygpI1gqEWM63VpWkbRmL8o4X0g40KVhVtFEqdnNHnxhDAeE-A8JWcLNblxD1A1vC3HOI7EpJAZ66XyCRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=mwIDzgCD6qagFvfhPIrDy16myuZjWCMxM5V9LNfl9zWOw3NaNCY3ZZBwFXTnBFsCcEX-gguba8QTCATlXiU8v0JJy6CnpCpQv0Zegp3ukgc1xV6GUVyDuihB1tqO-ZQEWSTvigEfLQ1YEGbAr7ptw3mQw83pQzdfUuAcjv2H-yN3HzUGIt_O2lzPWk5dSDgqg7jUZeyQE2nG1LNIRg5aN7dcmaTRv9hszsoS-GhEIbN4UWmJ-eqJfcrohXst_O2-0mPWBygpI1gqEWM63VpWkbRmL8o4X0g40KVhVtFEqdnNHnxhDAeE-A8JWcLNblxD1A1vC3HOI7EpJAZ66XyCRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=B9wFm4gfnDoxNz7SKUnW84pZyJ_9SwVKn8_i5SaVuMzsj3TF-h3swZQDGkd3G_LgB9wGk0PIYnDawQ8bNp95wC4YWCzHLQ1ckMRc40ywduwxHxUCqcrdXiLg-OTAYeX19D0Ddgkfc_bT5Vc7kBdqDVDa6fY8StBtG31pvEP40EUjc9vLmVJwFqXnnn9vAy0ILVc8aW_bJ2HWBNXktcJ6kod79ZMbVo_IhotQO7i_U0-RzxqdED9V4CsY_gGjhquBI859UgpHOaHv_fapVyvLecD4xjsrVp2ZvOeC2-6tODppYveeQuF9pnPdLanuqPBQuCDcgc_5LpLTHytUbCxI5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=B9wFm4gfnDoxNz7SKUnW84pZyJ_9SwVKn8_i5SaVuMzsj3TF-h3swZQDGkd3G_LgB9wGk0PIYnDawQ8bNp95wC4YWCzHLQ1ckMRc40ywduwxHxUCqcrdXiLg-OTAYeX19D0Ddgkfc_bT5Vc7kBdqDVDa6fY8StBtG31pvEP40EUjc9vLmVJwFqXnnn9vAy0ILVc8aW_bJ2HWBNXktcJ6kod79ZMbVo_IhotQO7i_U0-RzxqdED9V4CsY_gGjhquBI859UgpHOaHv_fapVyvLecD4xjsrVp2ZvOeC2-6tODppYveeQuF9pnPdLanuqPBQuCDcgc_5LpLTHytUbCxI5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jpL0yLe3Rhg6sb5CSDrOlzVlNP0g1k6QeAKdPgAdoooBUTcrDu9jB9uSs44LDeStDadd9XeDff2cm5Lm0CtKy40rHWhh-7JS8bjzAtcjFfoYxE4m66R7XFOfsdsQBgE7KhiVTIfJybjwT7dwEcfjcAdhsEPldOuWFpmRXNJiO4N11H6Ai8G_8i_4KGzDQC9qaGJeg8yH4Q02fSkjGGMCTE5Ok9jQ5zHqCMAeDsJSKAOevnE8z3-Wbn9HXH6-J9iGQ37gdMHN3ea3tPr-qZrMY41xYMDVJ6f_Nx1lhG865VQVyJJ9b3JsWCMG6qwwfbFjRYdsazr31dJY3FhQxPOqHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l2CirhGNeKzfKpH2B2VuhcpEGbgm6PbDmUOVQHn8GAkbtg4gBT3VnW-Wrswlyk-xQkIXMKTK6VobaixUQ8Q0SFCxO_vGqAWY0zk5EgwAAVwDFjn-C1m8-ynXOOU8ZMKX1uJ-vtL13nPdAYkx60u22GtM1okXpd5U_SYJAZ0x6OZ_o8cb-1JbCcqHQVShQiU5mu_3p7eZwfdRCBkwDDkMXPObUQ4-F2Ya_GwggojwI47bLAnHWVR66Bj1jT6kIJxcx2RAs5zNZyOss_JzP1weE1mKZlkYdXbquBCXGn0P5K16OjYxu0VshUTwmDl_M-G8oa16gFEdvdQ_h6a_6dJ3UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b4C1xGub5ZHmtr0UsqkbVmk9uUH0KhMfkEaxV7l4kB1ToeayxqVTMN-Mqu0J8Y6JioZB7-vpB8Yu0qTdGYdCZm4_1drtwaFEnNb7wVcMWofpQBFXwmsS3l-sXB1JB46fsWyPdRVw3c4JEdehauRSkwpqUEmq4M0DnxDUdeHPsAR9R4xFiy1Igs38AZm-z3iunx-TO_J5mZVgEtGPdiwrt0QcDUTA3px201HpFhOwQ34XP_egGKWAXnyE1ljjUt6hCbCwjWJJt-xk1sr_dJ4dnU5x5Gnbi2mX80rvovRnK0UNcFyv8MsSZFJx94KbBdOqzXN0GpkIh73_kLPwL6QAwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=ZFbkj2MYtPefa1-MMhFsnS9UWZzisJnHhivNxyEQTUigr4YTEoWJ3wciK4zY-tAzqSPG5X-PnED37G-VEttorjvZdDn-MaD4l0YicCcfxSSXJ8NMFAIYX2tsRB_u5806fY6FN2dT7v-abo5lBtq-bWoIl3Q8xnbdSXEu3bbZhvBAxlNELk5H7kfYjtFdiro9rUVD4aoUFou6PAZWWYru_ENe8ZfN9NyUW-XYZk_JlCodbKEpDAJxvjpdcf2iHGmPy6osaIab6SBs3DLPnHzaLv4k0fE-kD3n6kCWic-1pJanEmU24MvyBVZFSqzVZYNGAjcVYD_4RfPHWpA0O5PoY6ctOnIa0pjjTjw6SVGGTXe3NCviibKiGqfObVez1A1FCDK3Xn2BfgiQLcAT_ArI0lLLp1sykyOI1yXtL0enAiSYilmF2CiaW5pUO3jQbBPdzaHNPhc8vn-2Gb2zC1xU-h6zU1zLoX3iA3Ku2rQm2j5kz23TPEb72a0eX4ouxdtVufULj6-wb8l4wepWtgLZbtFseIEtY0y0gwfqZnrOkv4Fqqj5aNNgts-CZHkKnKXmE4jUmdot53WThMCoSyLYwBzc_r6Jxw-EaXegorGwqXSr2HdvT3k_3H6IFjFNq0MKVMvqqPPnSmKMavLcl4hPKwCCOvjvnrHYbj4HE2QkR5o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=ZFbkj2MYtPefa1-MMhFsnS9UWZzisJnHhivNxyEQTUigr4YTEoWJ3wciK4zY-tAzqSPG5X-PnED37G-VEttorjvZdDn-MaD4l0YicCcfxSSXJ8NMFAIYX2tsRB_u5806fY6FN2dT7v-abo5lBtq-bWoIl3Q8xnbdSXEu3bbZhvBAxlNELk5H7kfYjtFdiro9rUVD4aoUFou6PAZWWYru_ENe8ZfN9NyUW-XYZk_JlCodbKEpDAJxvjpdcf2iHGmPy6osaIab6SBs3DLPnHzaLv4k0fE-kD3n6kCWic-1pJanEmU24MvyBVZFSqzVZYNGAjcVYD_4RfPHWpA0O5PoY6ctOnIa0pjjTjw6SVGGTXe3NCviibKiGqfObVez1A1FCDK3Xn2BfgiQLcAT_ArI0lLLp1sykyOI1yXtL0enAiSYilmF2CiaW5pUO3jQbBPdzaHNPhc8vn-2Gb2zC1xU-h6zU1zLoX3iA3Ku2rQm2j5kz23TPEb72a0eX4ouxdtVufULj6-wb8l4wepWtgLZbtFseIEtY0y0gwfqZnrOkv4Fqqj5aNNgts-CZHkKnKXmE4jUmdot53WThMCoSyLYwBzc_r6Jxw-EaXegorGwqXSr2HdvT3k_3H6IFjFNq0MKVMvqqPPnSmKMavLcl4hPKwCCOvjvnrHYbj4HE2QkR5o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k48lJlPkXRLN9Mywfdsa31Oe7PBllquEWQUYDxhqOnSVUeazMW_WJbhTsGJXri3akhQ9NNkGU_P1pSqSD-zWLKkulwUz0rABGX0_uzPZv0RMNjXl0dcEiofpKyoFwwh9ECFn9kpwKjomaKZW2hZIw26YhIsV3Sz0GJ5OrIvpv2utgaW95BXx8z76YtrAmO1lMfr_2y58ul1yJBAfyvoX-o4PdiKUCDBS1eXviNv1-4C5gRpQdRRJJg2_4v3P01jO1jVFEdkZMtQy6S5jbSAe24owMaGnust7IRWShPy8ceMAci2eC_KLOZZaNhRiRyglKcsfF8jCMOavieY-tswtdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kp0IP_UGBxvuPdUZSTKJC84NFeTrfyvQejtO12VAbbmP5P-zO9rFSVNhzL9oMbsANJONQubx6ND4XgGDv-zIcu4uGZbzSFvbUjCotIADYMLx87oPwlLZ_udDQzC_Kn3HWzmuQmOA94wWRTrfFsfo41iVADuz7j9pMMpLdWjfPa39aPNLfCKkM_qpfe-wTKm4XkEnUxDDzcd1-VnNz6wPj-oDbAxFBbCU5L8cuAC6r2MWqLlle5EBzfzaRDoAEvUTl1xa-HnFXYVNpZINJ760JzpO_APS5pC7SsHINJT_59PRM7sr58u_F3yR7HQOO4Vfna9xYT1Dl0QGFP30Y6OlhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K9AlFKoUYFlQh4vhOxcQ1HWAvn8YsQ4YZi-tHXHmiLktI-M-4H8pktvoxNmQF0WHSURaYIVWjR4iONk-oU18OCltkQq4bvH6vBJthNK_Pl7rsCa-aR65POb1C_iXSJGDGO4_PL96j5S77UHraD2PDASIOuGLrZYLzLpaz30SwQ5TNyacvh7M-dGqvR7oF8-YbUBz7ZDUQ62clb0tXLcq8wKYvuvc6djp2TqLZt0qILA09zhdunjPUliIrAu3elFVzWkZDwnMeVRWkcMC7mAaEF6jpkEmBSsfnmNk4z3JhRRscMlQIPpBbKpsYpHuigN1qW76FJq6DgrfRg_8XRF4cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📣
🔥
بلاخره انتظار ها به سر رسید
🚨
👤
نود جورجینا همسر کریس لو رفت
🔥
👇
🚨
👈
گزاشتم تو لینک زیر بگا نریم
👇
https://t.me/+wYDPG2ky70AwODU0</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dT3f7zVwWVwmdK_lC4i2VG97YZ1Wr0nLNx2mDyZNCoc1GJ8r-2qUfD4J03gkcjwzAaumcxOdDlxWJu87rwaw4kcdr1Wk7ngpx2E0yBmAjiVCtZlzULfV5aeuoFZb8FfomK7jPpcJTatV-896Gw5PB7x02O9GOCFJuKrGWgWCy5HRvI0g-gEwIMgs2LYNi3KkCIJq926T8IVJndmRnhLAJRSQWB5igsuvwhhOfiisd-FSGnT5Ai26NqstJXwEbhg277I6ISRoc50Z_8UkMuneSR-2Tz7fEsBLZv923483xomZtvsuTkRcaVNl8xtQMRUn5UJLFs76_NAgCIiMrsPv5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_av_bx-_B8BtdIGyQNskzwLajN9IQhvOgUX2TGTGGkUf3Ti5UCUPgP4GyOlzonmiWIEugKn1NVKH_DdQm6BOIdXkwHyAEC-pV_qIUtjx93sMfZd4iC_myf1Vk0HyeF4AGXvjbHIE8SY8gjQ040oeXosqvcTfiriWFg5GkRrDfDF21XY9tfdS3PR1pafVRCujFTAvkflCgIajh2fZn0z73fw38OMUCT4SfwxJMXVPiap7vuFUPyCgzkpH_8Sd0CjytvTXR6Z-MhzD76corTCu2Ug0tBT9JGY-6Txs-U5gNaYwSUOawhMca4GdRUdlSdw0qwugVt08JBD4Gd_3lRm3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V9e5vPFz-UtKqRTYo3XB9SvWX52a4z75v3TCS1x1NcMqZtcWTEqIoBA7Cbda0kj1VanGI22QoJQs5_RDG1tcyFHjlk3XDTcVI8uoHf_23ovVVisugZ-oXAFz3ZjHtBTP-yPYg33St23vhV5shBz1WIFmk1Xp801qAoFWOo-1AGmW21cKd63sh6fPd6pELe7_xVOTbMxjtnOnEkefxFbPir4DXFnZRQaRUZwWTTqmVhkxHGzTBDYTuKT_XWj8Pq1FDP4HevjY9-zJlrz4PC1cmuc4w93KTH3kIX81zeOzBBmM9sfGcXwXAHR8JzH7dKLoh2tn7dnkxJ9GpdgNuYpBmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ttCoTv8hkhEE6MwzfAwdeCwsDLBwkMReN541Mc-BYAG4wx7YjLyn7N--0oVvXvUZti0WV3vUIVPekyHsULGO6bhmlrn9F6Aiu4ewz7qzcki1fFzB46_u0ihiwOy9hEZ1gJAIW6L58Fors4I25YCvTcbF4mAQkfmdixctYN1EZA06rhCHrXSgHybwAudqsJaufqHin0dQQeUdEJVcmoaYfUOOTj91nkn8zkUFpyMgEuTobGl17yMZgBIFfWMCsHYCA5ybDXwvTJypQSLgDTPKil9GRPiAJnyC0XgKGpXt7zo3G7QouohLO7RrdVLaAPXWNeg8SuLtbmDrpxSCd3TgLw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LtdanN8jww0_D2-aPY9gRS5I0NZ60hBf-73AWY9GKN9IbVnfGhKpLz6UJZ2VMXMZ5pVeleeK3bdQWEx0KbpJpoJ24ftQFdmsnFMsrGje-7PectHfzupEQCbMrUURmpVxJ6bo28a5IJh26R8uW_zKvBoTamVs6FJNZu8CIB6jMtPrm7L7RX-xcDm2BYrgy7i6xvpLXUvnzDQHNZaecz0ZwQx9Gd6xqAf3bFncCnECgd_rF38Za8UGXG_vlOE4KBOFnGZGiEpXAeqmvB1OWS5HwzoaqBjLvLGwYFgLLpORJ2NeUU1gKSiBNv5CNUc2NO7fJN9AHqDfXIFpTzgbIX55ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v39v1fIP2oblpIoubCuC8uwTbn1cFfMn5v1n8UiF_wbMsPxmEIlbHPfP8yZ7uBG6rWIkOed_Qk41Q8_YfMxybt-amsVD6Ku2x57oGpDuWF2Kur9gVZUtMdlk6Gpir_VNu0UtWsQfqoR7BzCsWxbk9FYV1IH3OTXZPkZtw-2t5VYkE0OTmegOsgWduzHbRJmDL32NsubOX8bjbXJa-l_HBZ181VTAyYWmaBo9hZz9cowgySKwS4PnwxfqklQvVK5neZ0TFaFaRnIvHScZZ2n8f9wiZMzzW7LQzKnyAPiEkjdG4y9UmorBjVZ8TYBX2GECGjWBbjBUzSHIpN9pi9zMcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVyRj9VLFpWlSGsOTNw5e4EdqrxVfP9nP-WxbEKVH3EweZP2B3X0hvqUCfUv9-siL_KLIoscyH2uDWnsidxOrpoFTm1LunXH4rp0uQlID4nMi18t-R71sePmlC-g1dPRg5riDXCEqlZ4BCASnub0bBmWf28Q5QC0sKVs0vkpN70m2UB0LszyxqQLLr_XZnwWsP0Y2-doK_e5He7Md-yCFfsNELQ0fOeAqIsprv9mNDjE0gTg5JqLQfbSv_RODVsm9GfA0KqVeGAMLxGUOyWpI22XfsZHqLXW_gsql-aceJIHOoMGgbfhmpViNe-36EMQbb6OPV7-q6516bqJpqbQEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDGYoBgYU914wYpFPE33PhGInax0t3KsLDXX8jdhtzzpktkSe_YZwz7BtBSMnC0YHLv8QJl988cJ9CQFY3C4yFMbstMQfYHCZzFWBbVSfKtqIohFCLnpMKGGFBi-dF1elLq5ptGoNOLhKiJH_QRi2zjoMuU3dpst61butS7StidYgNEq-rnurKbTsQGku13rh9p_V_JSbZekwfk-GEP5CdxGl3gAZLROSC_WRwFHUeJ8bo8Qo2VGouFAjIeVMaxr2XvwXsuMOKpcoBSYTc8Py0he1k1hJVTw7SS0oMUAxQ0bMw7l0lzpkdIjO2ljX4Cr3B5Shs9Tm2I7Us-DUKDQRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GrPH7y0XA2k49U-dqTfpk-jNjl5megyChLZmir6zc0SZv9Tht_yxxWwCgsQrpo9iOCHV-PxfV4YAQUiiQ1E6JeBzkLqVa7j2KXaA4HNdabPXIuGPSNWf_5I1NfgNSnNSMH906OSkP_BdSwVsf1ODfhLfvmwEALktmC7fpCRauldKbMA-7K8zp01xdXxxbHyzEeJBdGQOLHW2okp_d-G1gjZX6vRqrcSO2rHX8CJlZ3uibz766qcWLaZvu5z-qjzTD1eXqgsC680r1ZzqubMEIoPoDWCpDzLubVSD25AMYzZvlc0y5hudk_-z8f6DQcYob_lG4dcfJHTLzCU5UBMc4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=rBywc6og78c4yC19i3NChCp7da2ri4EcCnC_WOJHpyc_dQBFnl9JBIEn6MEdJmuf1tlPg-IFOcd520Id9aeuLO0QZb73lq6Xh-wQZzyhS2Cq5QtdI5hn4zcr9N9rbkKas4p8MT6IJDrJ2DffStW0xYp0t9bYQl9Mia2xug023LCZQWbjA_xNeaulo6NmhNln3O-6ldVi7o7zAwaKKvCpxlOz8EB6A5ACeyOEVkN5O9mc9Ab2s68pbu5t_DLpX8SszipRvifOqMzrslxr_iH-rbu_Bj8yz15wvZt8Ys7UjMxPmChfj73HCsT3D3B0d5xMykuHYn9GNJNF1x8ruOtG9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=rBywc6og78c4yC19i3NChCp7da2ri4EcCnC_WOJHpyc_dQBFnl9JBIEn6MEdJmuf1tlPg-IFOcd520Id9aeuLO0QZb73lq6Xh-wQZzyhS2Cq5QtdI5hn4zcr9N9rbkKas4p8MT6IJDrJ2DffStW0xYp0t9bYQl9Mia2xug023LCZQWbjA_xNeaulo6NmhNln3O-6ldVi7o7zAwaKKvCpxlOz8EB6A5ACeyOEVkN5O9mc9Ab2s68pbu5t_DLpX8SszipRvifOqMzrslxr_iH-rbu_Bj8yz15wvZt8Ys7UjMxPmChfj73HCsT3D3B0d5xMykuHYn9GNJNF1x8ruOtG9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=rue1FmsRYVxJvsm6vmMSkJTEza1VWbPqIVfTMNvi-UTlW5lA1ggdRfYnovQKlvYNoErpEBYOsskzz-ckKhLFTMSg3gOjB0hbWFne8Rg6UF5-YqJr9P-g6c709dgOXBMeEV6JS7w3OYyTpqiE_AM2x_4OhKgHOnG7G3Pn72OAE_hHZXWXKOH2cB0VMQ58r_kApWnqTfA6hBPpP3J0BHdeDi1OZadGOo_V7smlcZBQevVaFqwlxf0nEJ5qgTAmk95czp3fkS9DMmC441Sl1eT0W_mHGDQv0V6Ga4VnkW-qVxpz8OTHjfUYOu67tNqQdwz2urC9uSpnaJbbmzApe9SnFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=rue1FmsRYVxJvsm6vmMSkJTEza1VWbPqIVfTMNvi-UTlW5lA1ggdRfYnovQKlvYNoErpEBYOsskzz-ckKhLFTMSg3gOjB0hbWFne8Rg6UF5-YqJr9P-g6c709dgOXBMeEV6JS7w3OYyTpqiE_AM2x_4OhKgHOnG7G3Pn72OAE_hHZXWXKOH2cB0VMQ58r_kApWnqTfA6hBPpP3J0BHdeDi1OZadGOo_V7smlcZBQevVaFqwlxf0nEJ5qgTAmk95czp3fkS9DMmC441Sl1eT0W_mHGDQv0V6Ga4VnkW-qVxpz8OTHjfUYOu67tNqQdwz2urC9uSpnaJbbmzApe9SnFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ohYdXmHjzp7PvFxTyBYOfqOuAKcG3D4NdCIVh6yosAkUXO6TYBJb8yaF6lHcmRRf9MjjwRE6Y5rO-8FZvYqsQcxySAKjZOlfLY4zLyklHXJaZKjyQT1bMPsYtNx5T3XHfOPjX2XfS2h1j3muPZckpdcOlUJ5BKt28Z6uHRXvkfP6kufErFGbSbQyDEZL14Pw8-Bl36ewegwe848OJzxn2J6GopeJUoxpY07z8iwShH841jNzZm_afbXMGIoP6WzUwzAowlb1KvkAUJsrxmOeKPRjmCPuj-gbwJKMzLmfU0t_Jd0Q5gaJwsqhWBWo2XNl2-2SFDK6xWJJ2JaOnnqdlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryr70JiBC_EvWyxpaSl1tai2b-NeSuLMJR9xRwyQmzfwnwjwum7II0VcmPgNpEfgHIlh5Npt4e2JRBT2SgMDvZRhMP0sCjm5hGVGdxVIlBNDWM6Wnp2zigXGrpFe484Oh1a89-yFpnjEv50NhyvuPBzBSrB2yNpW3q2ryHuJBTK2Jx2_kLsqehQMhXeHO8rp7j62wWLxdJZdle15d3LmdO0qRcA0VdlaymezuIIdcuM1-N2W4m3Gs0FTi3twCliRVoIQpKxBSeMvZc34meDC7uC5px4xqV5cflcH8GihhFVI7wh0GdK5SZYAiEy56mQUMhz8gZIknIr-mlZUr6ZVDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e1pVn6RV7P2fCwjWWi2Clsc3cmPAYNhAYWqA40KXye61-QCpG0VQCUUbPEb7iczWxmo1LlXVK30DbUjtfpmtxaZI04WThotrfCtXm6Apx2gEoHllZ0bag2HibEBGw9abr5C3YENGXodOM61o13FjTu3ZS3Z_A6C0lUKg-z20afSJSteMaHzL9RsU5mBAYl1IqdD5JOTF1_4M400s3EfiB8QirKEuwxJwVZI0Pvbh9Cq21vYkxaOOWW9LS7Vcw86C_AS5VzU9tU33btQtF4WMyoMPeAu-iG6_fsYejhRc13ZjW1oEIVWjo5J1XGGaivHqAmi2nktdEXd851stH1Rp5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iEOEpn6aYRrCek3i2Yr5xjqZ0VEtQJONa7htFI1hD8fovoF4JDD_nxml3eGinciSmV_Imu-Pxh3-G7IMvorSb9a2iwS0v6-6dN6WMhe84WwxZD2ODKY73CjsgyIXoX4AjlAZBcJrLfIrY3mDOmyKlNfIAhE0gyWpgBrVM6U9Qg0VKV1mBF0rxgjAU8kYcISDtuiM2K6fE3H-x1ODRP_DTo6OsDlxAxAnNkYEcXKWIO1BlGmhVHWEQNon93o7B0xvLqGOidmQ942V6iixaShGsLS1FrLjqOU3fySPl8knYUbfp5lGg9zHU9yvrABe-YG1MZvbkOqt1zi2MTT9TA_7ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWDBjsw_OMgCyUAWwA3s3eRnYjITVn_QCP8EJUQ69tKbuwmdc3LGNFQecCm1VLCnTUXQMXlfAhJ3yyae3SrAdSEDqMDgwGPsWD8WGCim2-B9SB7j3Kg_TOlBt1IhYDciJ9EK9dICftGveuxMlQ12hGUX0569q0LNTSi-8FLSAkTFaFkK050ODJlYyqGOC7usHU-rDtNjY1gACCYmcZFyLrUiCkZlwfkqBajHe-VW2vHCSUFuVDRSqqEho2DdXPOvRHixf1hPwLRrfzXmVI2O3rw0SXAd2zZmyA9UyDS385yWN_e5UEOT_SSXP-MHmvFYQI1Q_DFIs6-yTj_b1OCvBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HGI6QYN64DLJ4a4JF27IenebIWPwQfP7UryavMmIaCBWi6ni1wapBYskgZVNgg07hPysOw6x2adkEnh1d-ilg-cHfxm0ucyyZgjqGk6C1BzN_zvKw_djbpvjLuVgUqvSyjAQKR5F_JzqeXtJs6ilbgtFT1W9VnYa3GjKip9BFpHpK43WNYIzTUimjpWC_Qkzj6ww5gQ5q5qmKulPj7vNJIDMxMFOMWdMBuxNJXi_QWxrzouwyPQZ6EPgAVCkLDHrssn1Ra0CJnyEPCi7jsQDsz6NCarjBEHzq8ZoSgpIPURxhXrgePPUpS_O1_JI60c3tGsnSEmS8JSsINqxSu40NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g66o_5dDZnTgUp8SWbZy4XSVR_tyDGmy50J1eQVfr3FKiHS4508qC5aCgpnn-j7CWq2EmfUiNhGA9NgNYli1NjK4GAmlexlozEJJ95KYUAzKDgzbG43p52jNdB5LudcLdkVdPlu6WTi0isCig1V90PGr9dQPLSzZfPNewe22lAUcoKyWLGql6ttBnUly94wKNjETZjPYheKlEs9b5hHabCmTidpkc259DEktzOu4V5-992FuHKeCVqgfCjlR3mvQzEiHCwU79erMFJ5BxaXcr8NGNjWBo5GPT05wyeyf0belrwJV4XGaTJPo1Ar5m4-U6zSKaDPWzklcpFYoQdaqTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzisfHhRhR9zEa1IYpqnAfv0uZVUkPoQ2XvXGg2iEotI7aem-NON62RtOFamIMD4wxvLIO7xnuWXiiZaVlRlJPnfv3AZ9nEeOcLIgaiNPGv4iM2EPRNJPg5bVrwsVC5Xd_ojIS-8yZRD53WdJz2Ig7jDD3WbCEPk1VtvKvV_9Z85PCBpZu1jyNh_bu0sqC_sQkc1ln70mqfJ0x1Nxt57HtmD4x4I3A7G1K0mOvzz1smtfZkt1E2TH6NlVwQgehTqGwiEsr2D2WOTEiWQSyhJiVitoQs57yAKcjCYlOsOe9vRDEu4vWOoExUaylBdYZOf4HNaaISfEgNEgFgpBdPPlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=drRwCRUUkOtbiVBHjCdPpH3qgLsgwUM7LUr_yidF91EhaMezI-rU4N8KQTqlUpMoYTdCg3pXRStoGGqko4l0wew2nco6vH5p6xvSmBYCLkROj6bkRfDgc_0h6SZGobxfI5fAqxiVc_USECIZp9HKmwN4il9drWnCZKz1o4_bkzYT1BppIJ7Bpc6d36whqAxQM4jLaNrO_KmjEQdnjq5yE6Y2m65vBnp8bSHoMsLuX_XBMPIvNCeakPMz-uNCKfLwnEjE_OFiuvkxtfFUsBcy7kh8cc8vHmRPuf5On_kNxBZOpO4NExkhXo-1Dk6fmM6PTg7RTTbrWP3rzwFPkPPsXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=drRwCRUUkOtbiVBHjCdPpH3qgLsgwUM7LUr_yidF91EhaMezI-rU4N8KQTqlUpMoYTdCg3pXRStoGGqko4l0wew2nco6vH5p6xvSmBYCLkROj6bkRfDgc_0h6SZGobxfI5fAqxiVc_USECIZp9HKmwN4il9drWnCZKz1o4_bkzYT1BppIJ7Bpc6d36whqAxQM4jLaNrO_KmjEQdnjq5yE6Y2m65vBnp8bSHoMsLuX_XBMPIvNCeakPMz-uNCKfLwnEjE_OFiuvkxtfFUsBcy7kh8cc8vHmRPuf5On_kNxBZOpO4NExkhXo-1Dk6fmM6PTg7RTTbrWP3rzwFPkPPsXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.9K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ANyRykNUBtBRX1xmlUj29sxQVTb_EOtHpSjmQ30r5B4sw3I2pOHBAOsI1SW2ECGNU2gs3_VQMvjngbzP-6mxAOTEfJnAXa6g9V9WeLENVW9rxp1GZsuuR0NJlR9YutyX6-YsJKNM6CU-QsyF7VFfBLdzU43g90fnr5yWX37eW7RCX-mYhBHW4Cfabt45tjD4jcgNRduxQaAG-QWXjy_Z5TXSFN1jh7LyoyQ0YhjmFHxKoCTkWIyJHR1I2nelFhw34AW2dmxiiWKTgPiiEMUomdgduwKNBPhuISK24lu1IvY5XyRaoclRjfj86xLjVFZGgGSB6v6ihLzfiJWhAtoa1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=QIJMgDN2H73oc0SZNPE03I0RNSmL-slksDq7PcTkedze7WPGmB2mmWUGWzd0JqHd6MvvXG03Jxxt1-S7cD93UNkqIE2SdZ9VQ9P3ZK_ADx7VEQYPYIwyXH05PLHIZLJJjtLdE77jreTVyXdjZqUji_B0OjsMANtt_2cWhRpEoZJJCPbj1xVRUjQQW8bfip7S4lT3vFUzOa2aDkqSIMhBmJpFHIZCBJl_gRp_xdEcs9H2yZhzzSXcOpKUTDi2N1fJQhmYP3G5yR4-8ZqEYKW2wa01w00SLykql710Su4EOg0ApMRSCOcqM01u2Pg354OIh3VP1U3BidVgx2u-H8f9XQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=QIJMgDN2H73oc0SZNPE03I0RNSmL-slksDq7PcTkedze7WPGmB2mmWUGWzd0JqHd6MvvXG03Jxxt1-S7cD93UNkqIE2SdZ9VQ9P3ZK_ADx7VEQYPYIwyXH05PLHIZLJJjtLdE77jreTVyXdjZqUji_B0OjsMANtt_2cWhRpEoZJJCPbj1xVRUjQQW8bfip7S4lT3vFUzOa2aDkqSIMhBmJpFHIZCBJl_gRp_xdEcs9H2yZhzzSXcOpKUTDi2N1fJQhmYP3G5yR4-8ZqEYKW2wa01w00SLykql710Su4EOg0ApMRSCOcqM01u2Pg354OIh3VP1U3BidVgx2u-H8f9XQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxA6sovTETRKPV3Hsai8B7diytykpwskSzFAzdROBrHP5sKJcomOLMMenN0rlf9zs6By_YbjnMYoU8eiS8_zKHaTHP6l-4H6OaabcFkLkXTDVIb5ktNBugJ7VR4_AVJBcu4awK_oPc1lzW4lsDnbZW8eaL1U0PgMCR-1Hy0it89hSYAFWsI6F4J4N3oQCQdWQFERdE238YbVunDPnQLMdCy-tPfonssnse_KjqdFxvv3tyY7dUbAh8Ad7nPZkfvUXR3Hb74mvx8djCBOaM_cOT23bhgjRyaIDZvhp_iJQT4Fu5IG3lsvAk2Wq1E_bddSuD7B9HH8vnV-8OorjanD2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25005">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eLQkLnEB1gR0PDNRFSfbv12dnA3Rjoz-R3ImNnWTmcwtBn5zK47XC1XnkqPCPkujPrF07qdmJRyAiY8h_XQLeKzaijM9RPJg9Xwhe0CW7EIcBrllyfuVGcGEb-kHIweYNoe0BtjB-y0vZy27nkJpl4XDmTkF57iQPSBhnVWGTW1WPnZk-Z0wpXWMHxIRFM6IrJNW5LxOgdTWOg4ygVIjWjDAl5uIgpwL1g75PC9iPQPRFLAGxJMRWgBeN36Uv-H023bDNV4MNqHHzf2wANNqZ7ZAdsnOgKC_L26tNSCUjES_layjPEDYyGMMyEFo1udoCcH3L3GMhwpakoebEsy4NA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#نقل‌وانتقالات|پیغام پرز برای وینیسیوس جونیور: یا تاقبل‌از اتمام نیم‌فصل قراردادت رو طبق شرایط باشگاه تمدید کن یا قطعا تو رو میفروشم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/25005" target="_blank">📅 16:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25004">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=bO0aRV6y8pfdLzY7ZjW4hXHnT3dxmn9Sotwb4q_HRbpLiHRLw_MUA39zz0S9u2vCu32gSpptIGS-xwLog-QruT8Bf26bO2ji8J4huibyjONCUmJT4v4iCJatiOjkPMdN9NrVuD6HA7L4dYxVPhRL_tput_CX91vlSByntqbw4-ZiyfMfwYDfCvDpT4wSdglgZia0SGMvEZgavrNpWHiYsSdYm0sWgX9Sikiz_l9wNzwhzDfhoLYFjgQgafzxMRG_x0XNWjQhBorgNZzJBjyMIro4NSw1DqnHbPHJtvSiUkmq4u48I2pHeZGlaPN2ubN3lHWvxDx6JSNidNCaTxt1aA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aa6c0365f.mp4?token=bO0aRV6y8pfdLzY7ZjW4hXHnT3dxmn9Sotwb4q_HRbpLiHRLw_MUA39zz0S9u2vCu32gSpptIGS-xwLog-QruT8Bf26bO2ji8J4huibyjONCUmJT4v4iCJatiOjkPMdN9NrVuD6HA7L4dYxVPhRL_tput_CX91vlSByntqbw4-ZiyfMfwYDfCvDpT4wSdglgZia0SGMvEZgavrNpWHiYsSdYm0sWgX9Sikiz_l9wNzwhzDfhoLYFjgQgafzxMRG_x0XNWjQhBorgNZzJBjyMIro4NSw1DqnHbPHJtvSiUkmq4u48I2pHeZGlaPN2ubN3lHWvxDx6JSNidNCaTxt1aA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی‌ازهواداران تیم‌ملی‌مکزیک رسیدن جلو هتل بازیکنای‌انگلیس‌که‌نتونن خوب استراحت بکنن: بامداد فردا ساعت 3:30 بازی مکزیک و انگلیسیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25004" target="_blank">📅 16:22 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25003">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">‼️
یه‌ویدیو سه‌دقیقه‌ای‌جالب و تامل برانگیز درباره زندگی شخصی و فوتبالی مدافع تیم ملی کیپ ورد
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25003" target="_blank">📅 16:08 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
