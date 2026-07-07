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
<p>@persiana_Soccer • 👥 421K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-16 07:59:57</div>
<hr>

<div class="tg-post" id="msg-25120">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psHrTiXJr1kvjGvEPpIR7jCPE8qjlaj1NaI_JHEVCg7fd-9D7TEBe2PZW8hZFAtrl4wKfS0_jB_6ytaVdfhZ0tnckkzlQ0Tr_fvJvTJeqpOnzZW_5wdoqcM5YJfAVh2qkfAX3eUqxUih4_Cs5gBKXhtxrP94iLZE_s1huqGjFJGti6TGfO9F2BdL-A22PD43KnZUhwL2tRs3KvUP70gQqXO5mN0XcpAERDyn-0tiBLjMuDW1TnGYeVDpZdTkPE6ZkVAXQadaVRMGMzafXPB2ZENSxyOFppw0vPK61dPal7JCS_ZQrw8QpcxLoKp2PNvg5-tyjVteXSRBFlPRmSyuWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
اگه نیمار جونیور روهم به عکس اضافه کنیم؛ چهار نفرازکسایی‌که فوتبال روبشدت برامون قشنگ تر کردن. کسایی که روزای قشنگی واسمون ساختن. کسایی‌که اسطورمون‌بودن رفتند، اونم برای همیشه؛ آقای‌مسی لطفاشما تا ته این مسیرو برو. بارها گفتیم که‌هم‌مسی‌هم رونالدو بشدت برامون…</div>
<div class="tg-footer">👁️ 7.51K · <a href="https://t.me/persiana_Soccer/25120" target="_blank">📅 07:04 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25119">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VyNbj_Br7AD55aQOXyVYG-UnrRA4eXscyupVA0B90XkqiK8ZQqhP6q8DjCj_rWe-q_-WKc4ZK-mkb28K_eJNH-l-vsWTKiPKwYx2rtOp6H6DqaqhKhSmXR-P_sx_l4HkA8TXseptNIkzLlyqnFTPB5NStmpj89FJzMxyYcpZyeAtl4SO3AnWJEVYZDXUnnwjfQeJKf7oevj2yAX-kzVXX0wV5RCptoYIIKkhhaQkLWUQSPEZEJhJUSjXrrfrAZG87qMtfFE-nn97TlRWVybT7bRKm3aqu7UlErMGu7YUZfKKQg6Q3T3Zvske-03IZr7Sp9VndBBjUOCiQozOYEyUjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
دو ویدیو از کریس رونالدو و صحبت هاش در پایان‌بازی امشب: در این سال‌ها تموم تلاشم برای موفقیت تیم ملی کشورم به‌کار بردم و سه قهرمانی به ارمغان آوردم‌. وجدانم دیگه راحته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/persiana_Soccer/25119" target="_blank">📅 03:25 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25117">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e026475ce9.mp4?token=fKHmTfIbgfBbaMjjH2dnkctf_Rz7Js-ZNKyWYx42VVYEUzK50hRj3E-TcLXBm_N72p9L-syirrKW6bOCwb3SP4dC2FwZ8-Gcs5GaVQ3yfbTnPVanICefmuuSuKxDG6-XBNYi-WTAPDNGxhFKsUiV9a1ATk0DD6m45jPrfR2VZG5xFq41uNEakQVMrJo73FJMyPxpM4wTqsHeQIjZkxW0mzz3XmedrriiQ_LhrkndxCs70Ok1QtA9ct1077R2X3HaWaPjA7UUEUGXG6dp-lgUB62QQPYU1hFkjPwNPIyhl3OgskgjBiENJUaYGnDE5ADKlKYJ5XZ3Hp8t0__ORfyGwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
کریس رونالدو: من تموم تلاشم رو کردم اما خب نشد که بشه... زندگی ادامه داره. من یه قهرمانی تاریخی دریورو 2016 دارم که ارزشش برابری میکنه باقهرمانی درجام‌جهانی. این آخرین جام جهانیم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/persiana_Soccer/25117" target="_blank">📅 02:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25116">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f1QYt4LbGiiwW7BUTDjdplohEJR_5Az0gYUrCAdgRLauxgsaHi2vXuHZSim9tKuVZrCvjjJQyjVsCd91dosI4iSItxi09_v3aJ2pbDkJDVo3E0H3W6nFPQTaubqWyjw2YliPUEvpSxOjdLcz4ZKe1J-QdQafZBoIqsrTp8Zt2TeXbSqcZO3ineUB9mEF5wZQM_PjG7mbah-4iCiMdXWQdHTyBIItTsGk6Dk1NEdunma0Of4jaku_eBtj4RawJJd6SQbAbpba6JLlg8glUidp4yZhxYGktFA8kE-LBiGXR_kDcrhJh0nSIJR18qm8S8iiOSHqTfC6Nco_TLjJbWK4Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/25116" target="_blank">📅 02:05 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25115">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C0KWt4HOdJs83CDuQfVJBj8NQeXG32Ku5JC-2xhC-smXBZay3B482dtRVs8Brlchofupi0JvVp4XcfMT3HbPcjm5rQ0qrzT4O0QNGCzEF9YMUV_yYknuwzEnPmnDjF5yjn5dUMzcSfx6Jw6vUsv0YzpmdyfJKH8h5taoaABFJaTXpsj01uavqfmk49KmPZwInhFFQjWsfjrFb5Ui1QPXc2MOVOk4_IGHi7ApRsB8zG92N0ttQgRqk4K_qnrCxkL0NqmZXC3sa0BKck1bv46jzbxLH8pfU2P2ftfjhj8Vhpt0s2Xln7ADZtPY9KkdVl7LGZq-XKbSw6N1fqvepvOQvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم‌ملی‌اسپانیا درپایان مسابقه به این شکل رفت کریس رونالدو رو در آغوش گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/persiana_Soccer/25115" target="_blank">📅 01:38 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25113">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5k9Jn677BX4k7b2w8zbWXUCyeJ3CKlNLzJyrpgjpLTUWsosA4TRcm1gk2UBZNOF-J4SEwylF6YXUZ2zhnJVM7srcBM5nCM98UjUl2GNQUza2i5Xo6lnIVdIMLZH8iZDa_OaPZS76XlCXyclZg-k4BEDWJiNhCnLrMEdA2L3XTRPnQ07ArAB3Oe_EYpx34BAxXulTDzHTbeUrkVAbVpR1WU7DRtYbljJ1QzfUrUH31QGLPTodGMftjWAoEudQHu50L83meVBFDWfnE11wTgCv13aSOtlDh4BB8QxlmyAclWI_3KhI8j6jbmavUulN4nlUtjLCCHU6HJCmGLEEiTRLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فوتبال درعین‌ زیبایی، می‌تونه همینقدر بی رحم باشه... در آوردن اشک دو فوق ستاره محبوب فوتبال جهان درکمتراز 24 ساعت؛ روبرتو مارتینز هم بعد از عملکرد افتضاحش ازسرمربیگری پرتعال استعفا داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/persiana_Soccer/25113" target="_blank">📅 01:31 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25112">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pb5QkBO2JSMRNspylkW15V9otVsYZeEJHE5yfo_sKhEZw7sqynMjw6RqPfPYenhhJKFPNNOpn4wOf-9gJi2UhvRoQCfCUO6I5g1aJesQxb8rb8iRiaJXN5UXoBcCkmoJpYC-IJVEd1SeZ4yAush8C9mSgaYBdWw0X86ZThGl05tra8IktaIq7BRjwLhzKxbXKf-WRcNzsmuhxLWQmfML8paWWzq8CAOFHmbAApc5sdejc7m0JlL454Rd1J4m9id31oY6F4NLlpb1-zB_zEE6hN4IZ2wfGmgmfHIRKpAufFNOG09vtA_gnRsTpMA0fUnJOZK-kDbAgBNQ1zrQYXda9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
صحبت‌های تامل برانگیز عادل فردوسی پور درباره کریس رونالدو درپایان‌دیدارامشب با اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.1K · <a href="https://t.me/persiana_Soccer/25112" target="_blank">📅 01:24 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25111">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kwn4wDTPr1GG3mhw7UKL-SDihYeZSte-nr5c2DbPh-Zjrs_ogHhnDqSsG5AId30gsUpKjcuPVefyJXb_dVJmWjAn38KoxAsAbmrEc5ClYw4GWEW3oVsEM-CYONjS35Nbb0W8KHmSX6ipBToXcMv_1tYb2IEX7bssG7_1GfqT5MviGUyFIhOyDBrqhKqevh2WEAZSfvD5xcr-5xQFP0Hvz5tEZH2SPL2oXnVHdEcqSmP2e63bLOLTOhCWfYeCUt7MllOE0mLipwQN2nO8b1_Y01lJcr5u0xh05ar3pU-z35F2669J70DHvVPxBg2LurExeAdeYreSXi2Vo0nVjHlh3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
ازجدال‌شاگردان پوچتینو برابر بلژیک تادوئل‌تماشایی یاران لئو مسی
🆚
صلاح
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/persiana_Soccer/25111" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25110">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ru-QcQ0ODka4n6mAtW3DICWJ3BCQukgBb5kizb6nXzoz6QsLH90te5O-koG4ylTqumZBexIFBh0f193yWfrdVb-Px-U-TAOpXfIXvE8buHUpTZEjW1PQGMSaXYyCRP3kZvv_Q0Mz_gVA98Dnr642j88nlF53wSpXzPxJrRZnlfIEOTkshIGwFu0uRMw8jwCaI1NgOJblm5w_tFWFBOsq5v0aWLotKpNufrhDyn_SNpfKULcX3XvaF93bGiFZ-NMspZazj4ZlgMY1z7jjFlSQ0Z9bg0OyhCd_tuaIblIvRGq6ZQp-DZLfO9qBR-LWobuXerFPRxm24SFOXG6h_QXq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
صعوددشوارماتادورها با گل دیرهنگام مرینو و برتری انگلیس با درخشش بلینگهام
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/persiana_Soccer/25110" target="_blank">📅 01:17 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25109">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/persiana_Soccer/25109" target="_blank">📅 00:57 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25108">
<div class="tg-post-header">📌 پیام #90</div>
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
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/persiana_Soccer/25108" target="_blank">📅 00:53 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25107">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SU0Vp0hZ60PeTAcYMF-w3EHElaU_YRMFha62l6dZUYlGDkt2kEBKr-aqy1mbBjpio6plyyMT48zSmjaBdBsCiZ7GpkyqYW6w4I8jdj515Un7ou2ZuwLkG852DNC1EkSXQ76q434JW6uRSnNNWHiLCC8xnZ3Nv_x7sqvsXMRqBNm59z2W9re_2gUTFFIAfCsaxROpeHZVrA-YYVZniIiw-wMdu7cLJ81UFLoaH-50Arv2BvuxCndZEHdlM3ERG2ZHwtdBIwWJcfxpyE4XOtKoIurahQxjrrBUl3VVaMk7F3T6PB2E5qBg8seICe3x9706Hwr5gtFHFljnG_nIb_DUUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
اشک‌های‌تلخ و دردناک کریس‌رونالدو اسطوره تاریخ فوتبال جهان پس از باخت مفت مقابل اسپانیا.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/persiana_Soccer/25107" target="_blank">📅 00:50 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25105">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BThcbZ29ANqVovn3e3_AoeixZDIQRiy30_x0x3KB9L9Y_wGiT8TLtjFnJGTsjT-bEiTjwf24R5xJ9f8Sv7Hj7-jZj1WVmNKZL4hnuIZM8y8Tb8E4ySWIfggG1a-Zgz0fEi2W2ae6-vxEB2hw3oWU8_-CiBeVUt67RBlpt_8QAF6Gul70amW9pfDz0XOjE0rVhFX38Mb0PN-m5OIZKMiT2tqTmUv78ZOv4cDrRdE7Z1A19tSPyaKAyiJfGSbMJfIF_0AHrL9QN_pVGAjHDJZzEhJnCZ2oDVjfKUXLU0W-FA0cBF4OkyS-dAbbAjoATjkuJK5ZCXgiyfFY6nHikEHLOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
پایان رویای تاریخی قهرمانی در جام جهانی برای کریستیانو رونالدو 41 ساله؛ نشد که بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/persiana_Soccer/25105" target="_blank">📅 00:43 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25104">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kz0t554u7v5GOA-Lvsrmrk_TNbR4x7avf5LWHNNiDCY-Uqom4EcRfrl3iGiqOzSZ3c3N3UcUcs-93whN-RVbV5kXDi-ooefBifm3IQhhrQaTDH8pdkWBNihueT0rGHs4QllGQgnVz8ImJr4LWS3Yas-v61gv_9bCj842-XfGtbLBRXzArr2MIO7MmEUg9mSUgnHfYYMIllk_7EtSET4-6ghF8LFs7ZsGLio8nBPs1fD8-PmTzOmN4ga5WEaYrPrz8_HCDJDX_P23pJKDUR_35hUNa5uZY-4TaUEcxJbECz3Dxj8C4sCkgiSWD9Z1Df0dIvYUIiCozi93hIpjXHVYig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی؛حذف‌تلخ‌یاران کریس رونالدو از جام جهانی با قبول شکست مقابل لاروخا؛ اسپانیا به مصاف برنده بلژیک - آمریکا خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.7K · <a href="https://t.me/persiana_Soccer/25104" target="_blank">📅 00:35 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25103">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NqjzMmVCe6iFi-c_NEGgdMaJiMpcGStyFa-OgNyHFMNQkOMdQCxK60S3ICPGVGiclCLbIBw4i82PbRrkcTKIW9yb-1kh-oHzV1-l5wg5zMBeYX8M3XbQedF4hdPhqT-uZZayctYlJreUOJNLYMgOJVu7w4ARorI0ECrzxgSc48QIatPRXFvn8Jo8nqbxbaDbd5cRuCQP2_adxVbaKFqQBbhUnJ0MTqq3t5uLLm3Clc1B_OIg2ITTh1NW1Z0MHJID2vNmgJY08TpWgse5jc0sA0jKnnR16ff0knxW823trsy87Bqm00LUX4NUE5-rRv3sHLIiK99mc0UcYf_mCAlcrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇪🇸
آخرین تقابل دوتیم ملی اسپانیا
🆚
پرتغال با شاهکارکریس‌رونالدو اسطوره پرتغالی فوتبال جهان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/25103" target="_blank">📅 00:33 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25102">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzUJ623KiYA_JbDRnmSNe1LIz6_nzgunlwuS_yJup1big9pOhsNWG546xUdHhYBarE9TadMwrBpEyacGLdLY5vznCqPgfqBhmMskBnTkqjoqhUwtUxaAuzke0IfL9mKrOZkg-pFYWQwUAoyP0q0Vrcj_b2yDhiMlQ9sQNNTx6Xlx5CevKzd4AOIS8BRXfr4GrmZdZTyu62IIIWBDhGF2AsI4fUeS_p-A1dRlTD9kxpV_BFZyGLY_eKlpk3TfHF93eGRiuBrlQSFJELRgiHqqfP90NqTZ97iwXtcv4HT_UPouOw0vtgyxYLrE1RZy52H7dOwxHD8BQXDAe0RM0R-99w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
#تکمیلی؛ به احتمال‌بسیارزیاد مدیریت بانک شهر با رقم 65تا باعلی‌نعمتی و نماینده‌اش به توافق خواهد رسید. مهدی تارتار بجای امین حزباوی که در لیست اوسمار بود خواستار جذب نعمتی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/persiana_Soccer/25102" target="_blank">📅 00:00 · 16 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25101">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/apoU4lr7c2RI5b0WFyGgidEw9pGZnKXw_M-aW_y3gZBC6wQnVhwWb9sUV0BoFrwIhSdhWVvIp5SduG0nAr4tK8xlSnGp-PC88Vhw_9Lbuz34GRGZivvbADyVnAiIG_03Omn7vySw_zHPgEv3HqN137OEN-du7niVVcOHCMzZINjjxpW3fHrRKKQq8-3pc5Ig1P6HIunLPGviuXUdXEQOIimBajfHL7YVN_r6rvQOK-ehRG4FpdhrXGImigd9oEqr9ze4bazfTDwWD30jVkZHnL9FPJTf3JHicoR0wx6tCx22SLRSelghP3w9Iya-bXug6GNzR_zza2hCUqWENM4gUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه نساجی برای فروش دانیال ایری به باشگاه استقلال دوهفته زمان خواسته تا درصورتیکه پیشنهاد بهتری برای‌فروش این‌ مدافع‌‌جوان‌ملی پوش دریافت نکند این بازیکن با قراردادی چهار ساله آبی‌پوش شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.4K · <a href="https://t.me/persiana_Soccer/25101" target="_blank">📅 23:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25100">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P-_Q_GL9S6N8cVb5M5jEF4I8szBleZXXfi9AnWeDlQU8FJzISx5swZBV8Me-4sqFWrdXnFlRKWbPpNJpt2pFMDmJGzGixHkWoSlyRPdfBKIgpQsydajdhp7Zdl_N6hGGqRM_KGeqMPH4uW3KzU2gscPAN7FctQu8_Ow4vKqdmofn2M9gmWqzDiRoVIs6n4Rlod65dfxKvEGer82oKd-1vHCBUltUsyMUMQ0bJFuDVkyPkgh8Hwc5XRLsdusXrbacMEtO8wOlcLtCZMncgDV0musWLekJHgl4b43F0_isBowEwvHw59FOnocL9TYnupHw7p4d0PB4-CkyaufGXQENUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ آرمان اکوان برای عقدقراردادی دو ساله با باشگاه‌پرسپولیس 80 میلیارد تومان خواسته که نسبت‌علی‌نعمتی رقم بسیار معقولیه و پایین‌تریه.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/25100" target="_blank">📅 22:29 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25099">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IL34ugje_g1o0i3gBiINFw_P04cL-YLeVeeiOC2uSIH3E8j6iFespdlLpkbagvjhPY2vKAkg0z361PUadXwGgTIAX1nHf0V1CHjU2_LFRxv8at6djA4N-ZXYYs5bT3eRflolYhoCwuf2B1CmprzVga-em31I7Jo-FxHaA6fx1iMfQvX_f559j28Bke9_iwk_ZuVBBDi1SWASG1OPfQQh9hHkq311NxGfQdJ2wLYQFpv4-zYW0NO1kkVTcnoCNgeb9KwSD3L1p6DwhA8ciOKNOZ-WnwuVKRCgIXqbUnkIlHlPjG6vuWhsySH8aoo-VzIlFzeSwka9GeHhg3f3A2vDbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">▶️
ویدیو جدید تاتیانا کائر پارتنر ویکتور فورت بعد از عمل کتف این بازیکن و جشن سال جدید 2026
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/25099" target="_blank">📅 21:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25098">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcDakIYAVDM7rElHAGtjwS6iDFPyrEaADAcEy6-O674aH8_QiRZHW8OKTqwHB6CitEg-fCFc6setbvELOYSPAP8MUcSNclw6dvyGDIQMtezeFNQgUDp11n0KGQYQ1-wu2GaQG677vM2W-OXCXMhAvYk1G6Sk0bIUlc1B-T9cT97pEUlLScCdao_b1PtbZzvySrbBZT3zOwprSzFokl_7loUPdDD2RjXYh2tBDKyLJJV_EAz0FrjCqYLDaJI6cNViqAynXRO-kMy6wTZnRMiMre2I0ygj4RoFkXkY-0cX4z8Cy4LqyplL369PNXeJXPDM6F1AN0mS6qRAbsnwkI2jHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/25098" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25097">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R9_lzevNhXIr5tIhE-v97XOsaHmBbw-kshQgZaCS4dQ4yBEsyJgBMdMmyoujgAPyEYzInXU8wPYhEg_U_pu7fKrksQ6op4AZyKnavZ8XiethAdOLvWN5gzGf3fldYILbfRKk6SWAdVigvpuMbdTiXgOY3oWKC5EN5auyNsaF2cFtOnGVPNHBPI3JHncGx3XX9Vqeafyqx1fUiiUhDzORNBd65c7d2YPY0MRHuUhBiCx8ABsUHayW6Gu-AtDQjXHax6IkIpV_boKNaLQ_J2CP4kittFMkcB6moAToXkNcAdI5ex_zq98bZF4mhQN2Dx7DACA44XVp9ZxBa82DqPvC8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/25097" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25096">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/persiana_Soccer/25096" target="_blank">📅 21:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25095">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jd3VHxKAB_tl5u2dtiCVhqa03-1Lr3oTJA1tD4t1myc819aq4cxrD8Ji2ltJ1UM8uX_ULFcH2npYpbk4DKefpghz4kzqeDV5nqY7FRtYcOgBUKdVZtiyedsVBC7bgBEnAZvN-RxsNCSbWUkXVpsXeAtTtq0Kt1q0RmklqzXyghSUMZatdr9H3fZ5H8JDkgBNTOUioTxLRLayar7S7xOzCSUQxc9f9-1M7DD8Km8kUVbFrB6zEar3ik4bzbTamItgTA4t1CizZD0nUeyPvx9KAvCJ4rrNjFh5GDZxUibsaE8t1UT8qaqU9PVjWFKl4voWBMBEifW_PrT1NKxOKH5pHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇵🇹
مقایسه عملکرد کریس رونالدو با لامین یامال ستاره جوان اسپانیا در مسابقات تیم های ملی خود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/25095" target="_blank">📅 21:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25094">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MfoQ1NTWbtWdkJLZY0RTtjTauxiy2gjnmQW14VUJbFgfcGBwUb1G59YUZ2m6AASj9fADbWmEmkCyggcUom3YJu0PdUS8oiZw0taveiGiWYFJYLDUJ5rtSSzqVIMQ6zaljMg-W4GFiitIsAmoMimoHR6ao7TYMq54UkJLXGXxqklBfPCoTkPEaIY7fu8JL-ja_8hQPPctq3wy3LapteI_k2gv19x44NnbWsXfUhQyoiOLEHxZ9LBbCljLUiJBSbCM1VliU1Ly8Sjg02b-huG6ckeHVn_U79DLavA8t-c0Zi6u7f8HVf7GFb3l31o3E0oIoRFrFX93aZocT-TaD4E9MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/25094" target="_blank">📅 21:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25092">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qKPHm8hhFwGT_0-p9Nw1PhgalIX0mwuQ7Yu-9yqpNmNVO9NswuAfoleLKaKSQWk_ihcGTpyqW4hOSftmN_JUOKiPs4cstCsSkgqp2myKUrRYfaToEpsWmLHzV33gM7cf-Si8RJOc-Er2iwmxqkia8OEi02fdT77t1fpl62386LHy02GN9iFuwvrcOQNDoRxJ5_aaxJlXnCLuANFnyPxFprmmC8tZZTeGiIMDuObIlUgfI1T7xDSvWLgwGCsm0DoJzXGRm59oZjmtgGOnm2y6onzGXYhLm752Gb79Po9h5HbA5SQaZehpMwYsHdzNu74piop-A66dAdSKxyDPpJWqxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCfqU02up3RMtyT7t5PjxY7c0UfRbb6iHQTlWlNWx9MRhO6uY1CLrdR1HspbxYDJBRVs9OMAmyrY3PfdOurleizqYdl3RrRGitf6QWW1UHSLVLRdkYsWALeFRAri3GVgz9cYbsCvl1-AileqFSBiEzFIiN3LBg9sBY4yUE8s5xMsutqnfCBcpSGRD6vubpNHmOP6DDV4b-t4nFxNVeMWOcWggO_sASA6JlTXjYuh1lv9ZheW3KgHNaTCgZIMObAAlCLbyT9I6lWQMmD08OVZcRLjTjMEFtx6piKb6qIDF1pH1uCF7YZBQESTPahHnxhfPYVxRjWtbbnM18FLE1u2Fg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
یک‌هشتم‌نهایی جام‌جهانی 2026
؛ شماتیک ترکیب دوتیم اسپانیا
🆚
پرتغال؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/25092" target="_blank">📅 20:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25091">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/alZKvSsKYOEmxgKXZJqUe9DfzpT52GBM2wfu8Z00-6GH2kMVoF72ysB0Lhd0hkP-1nOAaPb73mPC29dO7dQISX5o4f4CI5yR3nKuFPR551OWNMm7BTIG-ZtJdktwR-Tm1Tq-hwe0O4m_RTYbKQLwgNBUg_YbKmbkt3frHN7yMWHPComaaXwj_zQxbuvkZLmLtgDlgiYaIS6HzBZajbdunngnPI_tvo686jdVRuAGoUB79pRpDuCNtT1Jzr6pGjkuiwa1zA_LNQ5QtHGvtlA09NOetLKrbetOETMdd1mFsqgHe7YR373awLIHuvH0QKgRNGGyOYwaZOK2dRN8l5B75Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ مهدی تاررتار نام سه مهاجم خارجی رو به مدیریت پرسپولیس داده تا شرایط جذب یکی از آن‌ها رو فراهم کنند. بزودی اطلاعات دقیق‌تری درباره این سه مهاجم میگیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/25091" target="_blank">📅 20:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25090">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cf4iLmDp9zOKvNL6eWVjA9zWCv-K9_TlDzlj_h7u7EHdkRYB_gwKEM2NSJHeXyFwoVOtQED55GdgrNNBVpZXEsHhec0CvqJartMgZgr84bHQv0Pje1ajd5OZmvv-byS4QbZLccvX5Tb2TehA83-2lXtjZiaxrzxwZ2aXwR3B4eI58eN9dUIvK_JnOgdNF1mkvPj1Tn3q4WRl0yXm2Q_ZM2LBcod2fWp7PrRCJhnFDBAMSNb8hj3tcdIUKHunVQKLDrLrYRGfjkuiKE4ItOOr_VY8UVq0M7fCCYLvoDByscEIgZBKMT6rdP0VoKsJBHf0V7GAs6CrsgINRFR_bqH2UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛سهراب‌بختیاری‌زاده امروز به عارف غلامی مدافع میانی‌تیم‌استقلال گفته دیگر نیاز نیست در تمرینات این تیم حضور پیدا کنه و او رو در لیست مازاد آبی ها قرار داده تا دنبال تیم جدید باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25090" target="_blank">📅 19:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25089">
<div class="tg-post-header">📌 پیام #73</div>
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
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/25089" target="_blank">📅 19:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25088">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iYOZId8la9J_OrJz-2oib_w_l1VNBzOjKdI06eljQQhyETKiRZ8TSeRxvtHlInlR91gCqMrGHg65zNSuJ_b2M5kg3mA2UoRu1AiXhteE9hiWUQjb-CXySXUEci7gaOvPNydVSpW86w9WysyrSBOH-LoF5eEdsnVfD5mvMjZuDeZmrRMhBE8qie8SFSvhQz2IrW-0wjbCSqVfGpqZB8N2Wg_m7eDCkbH19-vFngoa8cGrQMQ3J9rDrD5neHtEM5JOquyMMtMYZlDrqpl1aQL3rrnQ1Z0J0xzW84A_Y5m0th5vZAaw1bRWCgW5dIhUZ1VdkYmOMMddTfYZv9u3OEdLHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
⚪️
طبق‌اخبار دریافتی پرشیانا از مدیریت باشگاه پرسپولیس؛ مدیریت باشگاه ملوان رقم فروش فرهان جعفری ستاره خود را 35 میلیارد تومان اعلام کرده‌!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/25088" target="_blank">📅 19:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25087">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G_A9fbrn0L-igIHrhzL6cyxC-jkEVG6qIoNuQMZl-mF2arWobtNtsFHC6Ktvwua0eYbCfBnaafwCW05IKsIlgBGJ9Ry0NM15_9YLvinnlg1sRuKV5lsz9OUgqm84EIdQaYDJaUjFEzgcLLz09rGmzDmSGqqO9IV-lrzeBfFSxmuFQWaA6R-NR-XeZatGDELiuVBJhdiTFzeVX7xEy0_SNx54YBkqou81GisfpKDJa728jilProOFlkzEmvUjjHj9YAYqaLo_AsFvE6Of5G-bCsg3LaxpXlzcDTbMqq4KFdaTobXZriVuIBtsUQTLd5Rz2rPfQHl52Wqv4Mcm-YUXyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛آرمان‌اکوان مدافع میانی گل‌گهر سیرجان علاوه برسپاهان از پرسپولیس نیز پیشنهاد رسمی دریافت کرده است. مهدی تارتار از مدیریت پرسپولیس خواسته‌اگه‌باعلی نعمتی سر مبلغ به توافق نرسیدند با ارمان اکوان قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25087" target="_blank">📅 18:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25086">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Huz19JsNzZmoSZ7AFSKJADiA6CBXZMJf0qXptbLbKiYhSpPh4dTVLwxuE7z0LdEyf5zHZMZ7NFWfnGOauSkvwVSWsQlZikd_-QItQ-X-aynBU_aF2C3fUEbxu9a8-tDgFrrJdbqNeFMPuasB6QLD-mI3a1_YOB2jDOVSxXuh6BD9w3LZ5O0WIPZTesDKDxV35daSYcqP3e51DKVlX5emptJJkZJapx68Eb4FUK3tj7wKHKAp_tYPCIy5wIf3Qui-qjOC69lYqm8DQTpJfKoB195Cis8Yr44AyViM9ExqEQamaqHjDZASu0wtyI2vnuVLitxgHUvKx0jM5fZvx7k7Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25086" target="_blank">📅 18:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25085">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uIctb_9H-xI-UzRIaBncqi7SPdSJeqTgzjgud2VnUvKplnf37_8wkTNRyQvF4T_Ke2nTzRbiCpSjwo0C9PvLcySs3NiTCaXZ4NUZsqNp-iWBAuEtCHuuIT_W9xz8UYJ7fUUK_Dky3SoLqVJgCeepsgH2bbfWeQ2_EwFm5cGpx2x6ng5A9iUZAcXckm_Gn7uCv9y2ECvb91Q7neysb45Dvy9ZQJ55uZmgzoYP0e1p1RRU0vlmLKRnR4DAFg8UIyTNfg3D01N9szWK99FOknLmEFi6ECAQCV_x4QjZkWs_GXEz_C77pzLu6wUjntzRtd0H-SL9-vKmQo4vqofm3OJgLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
بااعلام‌ایجنت دوماگوی دروژدک مهاجم کروات تراکتور؛ قرارداد این‌مهاجم‌گلزن بااین باشگاه به پایان رسید و هم‌اکنون بازیکن‌آزاد بشمار می‌آید. دو باشگاه پرسپولیس و سپاهان به دنبال جذب او هستند.
‼️
اولش دراگان اسکوچیچ باهاش حرف زد... بعدش مدیریت باشگاه سپاهان با…</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25085" target="_blank">📅 17:52 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25084">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WKSu_egjIpn6XdM6QEnpFBezL_SZUoBmyl00W69x4T_XX89OHnpEBW8IVG2EtWkA1OPue4l7-ZB3X9qavWw-nRLkfCdx-GT5dLKyr-TPL-1k0vuNbg85pXLpKmKhDUvGCzMYE2ltVqbHfkIdPGMEKy_y9HZrpeD9B3x8lbjOmStXK1b8NbGMledbNm0ZIHy0zFKy3ZBgq-SujniG5lDRRVxhEMHtVBjhjOmi7CQtwQ7s0yNWtmC0wQLmRyMv-VTkapxh62IRzIVdD7r1pDJNvQYkpF11TbSxqWNn_upIHd3enmHrkUw4upK_RVDulWMH-YzlEWV_sAoTASMPHh75uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ مایکل کریک سرمربی جوان منچستر یونایتد به سران این باشگاه انگلیسی خبر داده از بین کاماوینگا و شوامنی دو هافبک فرانسوی رئال مادرید یکی رو در این تابستون براش به خدمت بگیرند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25084" target="_blank">📅 17:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25083">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pp887QrACfUQ52kI1yRvwYWiFL-mFLLTiDKM4ztlxbmyT6PZ-frsJgSzjyLka-IwvCrIiGlVYbnq8OdDFypUk1lJx8jMtyZjKTcJsY8H5HkMV4NZNST7SoyA88ryS6vH3IXerLb5eqkdA8_RR3OxcunaD60HcThR8xzn8dBsuGcz9PusymozJ-MuB7dkefjc73qZQZXTwALQ0YBf3poqq0bW3UsZpZ62cZZP3LnXCCu32tHbhm8U4Y2DvKURvSnFLXqh9J8NAnu5zYIVIKbqd3XSynUT2bu2DZcBsALl8hDZZwRpw5IxDtG6dMLS6CG-wTq5YvYc-_N7hVLkOsjaSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇳🇴
‏چهار بازی هفت گل؛ اندازه کیلیان امباپه گل زده با یه‌بازی‌کمتر؛هم‌‌تیمی‌های امباپه با ارلینگ هالند مقایسه کنیدوببینید چه شاهکاری‌خلق‌کرده این بشر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25083" target="_blank">📅 17:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25082">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AI6_bAPMo9UDYA31kbl9PJje8hKZRzBAQqV_KsOGI68Aq42Ky8SOBBMfZ0jiAx_zay0AtzK-22p_IrvpT823gpLZhXiktINIo1QAfnCScIj1sULiCrhrNi2bfeztCMY3uPc3sUl9P7dvFmKde6-YeGT-Fy9pAG8wPBhvKbTKr15eN1-SVji8-yP-bkfj2UryTzemKNsVWZzgPGfOv0tnxk-t8RYXGNwTTUGKxvZBVfe54PczfWxyZiYEjruNZa6U48Bzg5AwvfffI7lSN3jo1arZFO123ejhTDGpE0F0H9MmF-OdfiqBjzh9LcuXt5XyGcFQ8naolOVI8lmOlvOGtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
رستم‌آشورماتف مدافع‌ملی‌پوش ازبکستانی تیم استقلال:
ما از مرحله گروهی جام صعود نکردیم و حتی موفق‌به‌کسب یک برد هم نشدیم، اما با مراسمی بسیار بزرگ از ما استقبال شد. نه فقط من، بلکه سایر بازیکنان هم در این فضا احساس راحتی نمی‌کردند و باخود می‌گفتیم چرا تا این حد از ما تجلیل می‌شود؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25082" target="_blank">📅 16:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25081">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUxDO6bShYI_BSAXHBTjYr6mQRmp2mI_VvSgbGX16Xr405X1L0vWt7LoNGdXF9ytqTjh7Q7jegTnucsQJTLCvzw7TDadzrYBe7NPQk-VLXmPHGtCXyW6Hge41_ws3Lnt17apKbp35sSdeVIBvvd8gkvDgtQ3z57roqPqu96JY5rmVrgMwGiVVjArE8enZJOrsU2q-cuxAX5EjQ7rFyOKSbxklUH2etzn8wfJtpSENE9QynoHLYHoLEwFW-_1Cjz_jBKtlThII8VExfwTGhR4d5OrP5CNfncZxsGf27BPF1t8rtGm2xNZY5Kt15AzqCdeOsG0WEs1ZINknZxdpgwVsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
لی کانگ‌ این هافبک هجومی کره‌ای فصل پیش پاری‌سن‌ژرمن، با قراردادی به ارزش ۴۰ میلیون یورو راهی‌اتلتیکومادریدشد.کانگ‌این در پاریس ۱۲۴ بار به میدان رفت و۱۶گل و۱۶پاس گل به نامش ثبت شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25081" target="_blank">📅 16:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25080">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a_LPF7L8w47tw1-VSz8xaoayHjZr91KwbyM6KbdEjqR73mDMeY8kABdiq_k91zKEPrAs3eK-LhIcWcAi_Sr5Y_5I1Ezs0FTKO_ELdYgypccPhfopTLCinxaimMpWWe55jQyXYXYSNsezfoyP82XwvbXrVbsnY3X4lc2Q2tl3yLyrapr5TN0_3uYw9MjIdDd6UHjDgFsAhW1Nklp6pyiYyICrjfijIFI5gcwg1JFRzrNNjQQ44JVqHfTbfguU6yYiZ37V3-i9oImu0X8-evKP41Rvav2__wPAD-M8_6zzYIP2th1nB-B-waawyKWgRzzgX5XUa9PDinvEEO50j6-vVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عارف‌غلامی مدافع‌استقلال‌تابستان سال قبل قراردادی دو ساله با آبی‌ها امضا کرد اما کادر فنی به تاجرنیا اعلام‌کرده‌اند درصورت عقدقرارداد رسمی با سید مجید حسینی دیگر نیازی به غلامی ندارد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/25080" target="_blank">📅 16:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25079">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Niv19a_nzy5ppqgx9dkNs_ZtHAG6dL5k2ddgchEkcS7CahT8j0KlJqUGwoB5MXMSiFdpT9SLaZLjw9rMcvI2qR7gSrmJg03nOUA4ufncCd9fr9g8NG05qzn7e3DlWfjf16Ras4BE3Ri15vYUwPRPsq-Gq0rbZ7J1349weCFxkGFvYDXAdzsFYzpPOinTcOCOP7gpXnnoFltMRd7AdrjH8utpoTnP2YWtIvJ68h1p1c4p_qCwm3jgA2oUWltspcREqXmybay1_NfRTkvOqq45qRmZnq_ClrjnP0ixawOuZCUHoPo2ILPKXRpTWNB1Cjefa-6dkwoXU--w0rKj2IALuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ مهدی تارتار سرمربی تیم پرسپولیس درجدید ترین اقدام خود تیوی بیفوما و دنیل گرا رو درلیست مازاد سرخوشان قرار داده است و این دو بازیکن نیز بزودی از جمع سرخ‌ها جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25079" target="_blank">📅 16:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25078">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p4KVl68s9lyOpyciNuL8ExBJgyk96gAi2rT2C11T1Mi8aWezXHFDK-sp3Krc0GsBLSbmcTB_TmuUdWxrBRqSTCdl7C5wP2GeseANOO4V5MKcSj_SyaOYGQ6ZLHIcleMykG6LJ879LUQ1A8BuznKdAYoFDTQFERb8fPd5BJude81wrouyZLD0O_E8UDuVRPZWNvmsRbrPaa5Qrif9EOxhC-nwhk9abySdOYMcZv0JidSrUpquQFSqzwzyx6Yn8wr2Ww26bxoRMhnOAsbl3RGgsdqtYDzOWA9iOZjcSHMivc6mA2jdWxk-fLABArT7VRAc02h5SwfmIKguVCplho9JDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه پرسپولیس در تلاش است که در نقل و انتقالات تابستانی یکی رو از بین‌احمدنوراللهی و محمد قربانی جذب‌کنه و تماس های اولیه رو با ایجنت این دو شروع کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25078" target="_blank">📅 16:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25077">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZiybW76rVV7ayvE-tYPnT_NQ3y8QMtuZRsnCxHLH_DK5DW4R9-sSxO3EZiFm5X1R8x_7HiGIy-Yt6-caQJ-TSjg6r5I6uRzp-tqTedS_KGo6vUn1R7hoP3gLspTWzuT63RAbc5U_Cqwn-wglGRIIci78BZ3CT_9ab-sJmn3gX_2IcQiohHr3SB1udQY8nmJpaere8rslf_jC15uN3XXKHX2heQoUVaI_l3CWV9knqSeg0YrJRs8aN2CQUBtq5A5VYGdQ0yhJc8ghrFamannGRDAaeDM2ygayuJXolORXlqFz7l6k2GAMGajlpNV0UgrHUQhwf2NESQZJlIc7aixCWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.6K · <a href="https://t.me/persiana_Soccer/25077" target="_blank">📅 16:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25076">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/If0RvWOc5aXa4EBPbPZmZUCR_pMjnKvsAqwW0e3myqthUTU2nPoT2iviRJU9WUH7VfU1EfG3oVcsN5C74FdXhwwy2PzICKfMXlVisunfLGrKoZlmV4KawpFNF1ZZ4_i_-xmB0qOLuEA8JGmvrYXPitDuJH-sDxB-FS3k3GCAshrMpH5Mr-XBPb3l4g5aaZRT29vN7Yle5n8lFWQfVogJaKvZmAuXXFJ0daXrIUvY6SXpoMeohOYPFmhELW6fdNku33ZFPnRkZP6ZvhNm5wWZtdfukNqYLZLZejP3X87d3Zxgx1Xtm7ShtvC4TZLmcne8zw1BPslNSKd5VGBdC3xdbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25076" target="_blank">📅 14:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25075">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=or9HeL2Zm3FTuA3iOv6fAn9ell6pKhTdazhx7WUtmWq2kFGV9em9ggP0k9sQjgwYRva9VcMqnlPyx8KZWsA4dcfRuOgLwgA1u80BczhOJQToC_FCp_vzmgLIIGqwRQ3drAIZdiKs3V5XojaifrAZlwWEuSKksE3ZsECPGzFTPjpzUCGNB2zHTXD7iGBZ8ZcXqiwZaPqC8xxA_Gctq6AfNAebXMUAX7VB1aWEKCPajTO_PJFynPMgVrcK5dixYTfAmvBfujnOPSQSlLOP7AQId-K08qc9WFSaYJSIzQrud9_MORtlLCJF9qn122JPCltdRK9UJz-utm0Kd7BrSuHh6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e147ba88a9.mp4?token=or9HeL2Zm3FTuA3iOv6fAn9ell6pKhTdazhx7WUtmWq2kFGV9em9ggP0k9sQjgwYRva9VcMqnlPyx8KZWsA4dcfRuOgLwgA1u80BczhOJQToC_FCp_vzmgLIIGqwRQ3drAIZdiKs3V5XojaifrAZlwWEuSKksE3ZsECPGzFTPjpzUCGNB2zHTXD7iGBZ8ZcXqiwZaPqC8xxA_Gctq6AfNAebXMUAX7VB1aWEKCPajTO_PJFynPMgVrcK5dixYTfAmvBfujnOPSQSlLOP7AQId-K08qc9WFSaYJSIzQrud9_MORtlLCJF9qn122JPCltdRK9UJz-utm0Kd7BrSuHh6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
درس‌بزرگ‌کیلیان‌امباپه و هم‌تیمی‌هایش در بازی مقابل پاراگوئه: تو زندگی ازاین‌آدمای چرک و بیهوده زیاد هستن مهم اینه تو زندگی کنی و تسلیم نشی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/25075" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25073">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DHSJHsVZcXmNYs9Vw-dUOe1nDh91qTNI4Q9z8xkL6Xz-iz4hAjKNW5WiTz_ILWgDEOmAfa8USL5Ym4KGi3K7zOr3vMcV3L6b5_PeQsoS3FwwH1kCjEvqrO0U1hq2tivSYP5Yx8QvXGG7V-KTXcavYQs6VNsMhKXJkrx7TzNo8KkVKQA1swoEe5iT1aXjXjAwMlEjv1yJLcZZgyzMy2vV6d1CEDpN8y4JLq5mkEucjhq28QiCmx5r_bhfqP_woEq-BkBX8AulaU8KkHv_Br4MC6_FLoKtK6LPaFwSeW95RHoD8yoBohIjikSiSON8_V_-X3UJZAhlQKw6glA59rIslw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/abyUIOHTWhSSeLgwoIdPzp4DOX3Qz3e39X8Nr5_Ksx-19X1PptVZxLdFjZwGXfgRP6ywcHyc3pDWTNVYAALvNNDgQLJ4OIiqqEVpqC5zhhgZsxRnJDjSFZxuoJ18wGtm-yimwG_zOEfv6fog9zuRWr53r_6wjlRGUH0NqrAPtV_DIOqnTwM5SQnXQ4Ys_4WFpesK4knM5I0Jze7qQVmQBLp76kzpwbaYHUrJSboC7i_R0h8raFlNMqc8-6Cwjm_n_xxFnSw6fT6ap6ydvG1LHKnzJ7uBTzrwsdUzfff8tf0FVunqd12J6Ml6q_gDRSI9u8xzZCPpq179whOqgxn9Qw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25073" target="_blank">📅 13:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25072">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qSyw8qbECtydB7MYJbInCOCwDw5aY3QTbvfPTPt_03vv_OSHHYqX-1sQF_A2kiKQySGIZGAZjahURSXYs2a9-VAFU5PIqw5sSWS8wHkf1vNjTP8wImMf4DzKQND-hibqEveP2rLhrD0KJOFViSeraLa4VMMEw5U22CRRgLwyz5tIU3HC2bC8xhPTFpY1dBubHiVER4yigMEu6cG8pPyxklH9GDpOpVjULpiffJs3Q66KYDbpaNDYFkAuEo74DIA3azvw-zcv8F9jwwab2mf7nN_l2wIQ3NImGnDwqip8rInhUyIsda1j1COawzwY_i-a2tG4qEQnXOhyau9m016cYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه‌ عملکرد کسری‌ طاهری
🆚
پوریا شهرآبادی مهاجم جوان سال آتی پرسپولیس و احتمالا استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25072" target="_blank">📅 13:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25071">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mWL1ZlMYQJsR1bXSV1pUjOHFN9FVXYj-yg4vJmOQryW7fEAKexFDdkbAujSUptdHVZfwUpembXEYdk7wYwY6Q15wPCtBCC0sq75iLDrxLJgoEYqDShrl6qzGr0ZuJBDTdGpl7C6OL_RNQ1nLod_6eD3D-zOMXYRAmG7HhfDPaowT8GDVkLFN5qVYquV2p0idf_OzpkWMiwXq8WIFTK57wZa01mC6h137iShLN8HQrg8DfwVXN4HT5QQ_Imww55UbwoVai-I23_vWygK7V7Jlc6CUQQYcwgQQDgncAc0APERIMTIIUjuoBojlHBGuSiulrAFmoPgTymYaxr2jdxj2Ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
کارشناس‌داوری‌ دیدار انگلیس
🆚
مکزیک توسط مارک کلاتنبرگ: تمام تصمیمات فغانی درست بود. او بشدت روی بازی‌تسلط داشت. علی فغانی نشون داد لیاقت این‌رو داره‌که مسابقه‌فینال‌رو هم سوت بزنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25071" target="_blank">📅 13:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25070">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uxm9KrJydn1sqtKU67CDvgpcZOGoJI2_zHpn7rrby9XFMAYvQ6DubR7xkqMz4Pcwj7agV_RRVi53Jb6FlpsdkWoz2ZAFh26NbrwkXadjeigOD_QeSjipzFjwMugmbGDmygSPC3hsrEjxnKwVmp2cDvBjcKJejUILcLS3KulVoc4fPL0A2BFZ9emcxn8Ti4Q3EyAtzIfGe0pOON7D9ze7Av3JJX-Z60HFQPRP6tViO_nmLsWXe1xQ2s8P6sg9SoRD-t871yrHmcH48yMw_jxk8P9GifsY9nSlw-rkpLeo5cWAXrEnZFHcU2rXA0ByLTmGNU5gu2f4C6moGIh8Yb3vfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همان طور که دو ماه پیش نیز خبر دادیم؛ امید عالیشاه، مرتضی‌پورعلی‌گنجی، میلاد سرلک و سروش رفیعی درلیست مازاد مهدی تارتار قرار گرفته اند و به شکل قطعی از جمع سرخپوشان جدا خواهند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/25070" target="_blank">📅 12:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25069">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rFsky7NSx81dK44GWmQ_OQ3MIkPuc3DTOv5l9ubmu50iChXyk6dye5r5_g-NB4YsW458lr0mzVxh63zpViLUAXRCNRoV3e9hane9p4mXJJurfbInlZ49CQOKDoWUAPVFEtG8w3NoA74BCWLaANPk-D3PA5lRWOUEmyz60Q9yRix5-Q5BCaIIW1AeZi2lWndsiEhX89hGmVQKWQRJ9PfU-f5M0ZrPm0Z6MFTUO9WdA_GzzXSGvEQQbIBTJ7_nlvw3ognDg-BQ9tuAqxrslP4T7xrA46VqSdlPY9sgd0IDfd1OBRyjC_vWb0KbmZDoSBmTFDx5xvCIJoRS2HoKQElzaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/25069" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25068">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfpXaNNnyccC6d9PhkyAy_0Et3_QxsqpdVUJb5uG2BOs6ixI6z5cHLoK-PpXSVLms2zbvE_Y87DzHa5gWxt9U_l_U7dNg8bJcyXBufrtGc1ahpxwDwVxhc6Ct30J8mBjpJXe7BF9wh7Ho_dgIXsWUsKPJv8M7WkkO-8MA1mqn2FdZgjDzfV9zgtaNp07yioZ4u-dtGrOgrm-L3LduVJrCzBHI_v0gKkEIeBoj6bUwi_FN2rrwf5WQVyw_oLOrnXfpwWhuqkdQOeO_963ypxHSincnsB6TwAz1WsKHXo7gP7EXb1H9FrWofyURpW-VviPNhLrhfNSA7yKTytRRLReig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟠
🔴
طبق آخرین شنیده‌های رسانه پرشیانا؛
باشگاه پرسپولیس با احسان محروقی مهاجم گلزن فولاد خوزستان واردمذاکره‌شده تا درصورت توافق نهایی با این مهاجم قراردادی سه ساله امضا کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/25068" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25067">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=nFYLgnNKUqoIphpHBSx4VPPlNNYk2q3MDGM0kNneFKJ7b0GbrSMeozEFXj1P1FkM8FUISS6EjbjtPfeqM0ropBBDqRXuU1AiAyjbqCixBBjlB21tIonc8cpT42pUyledAX6WHPNY28B2X8fHtywjaCW3UfSTBZ9UEODnpyCc2jTmWt3QG4Zo_joBW7IaFv_JwWH34nNaqapgvZU8ZgpCZZ4z060vngeedVAxm6G9xMfAX4_BTP62PxlwoTuYS4dXV6akqj_v3iVq_WU34zZ1q24lDL9Ze666b-dzvzvQ-nBrQPiZIA8AsXqZ1QATBhcB3QMcOAzE8Cv3A13UxuEyeQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/19dbd7ccdd.mp4?token=nFYLgnNKUqoIphpHBSx4VPPlNNYk2q3MDGM0kNneFKJ7b0GbrSMeozEFXj1P1FkM8FUISS6EjbjtPfeqM0ropBBDqRXuU1AiAyjbqCixBBjlB21tIonc8cpT42pUyledAX6WHPNY28B2X8fHtywjaCW3UfSTBZ9UEODnpyCc2jTmWt3QG4Zo_joBW7IaFv_JwWH34nNaqapgvZU8ZgpCZZ4z060vngeedVAxm6G9xMfAX4_BTP62PxlwoTuYS4dXV6akqj_v3iVq_WU34zZ1q24lDL9Ze666b-dzvzvQ-nBrQPiZIA8AsXqZ1QATBhcB3QMcOAzE8Cv3A13UxuEyeQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇷
🇧🇷
ویدیویی‌ازهایلایتی نیمار جونیور در تیم ملی برزیل به مناسب خداحافظی او از بازی‌های ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25067" target="_blank">📅 11:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25066">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRPDRzTwT7cJF3qja5CPW57RY1MeMMfD0npMTPRBakCqs9HqEaYOVMuwVXm3E0p8vKoI_D6w-VJ60E3VgVPvW6WcfFOWZ2UGRz4qpEpa0KCn6kK-cVMwDjDZBMTL68LA4kGrJjmmm1Dza-jkcPt8P5FWoEHPeth0917q8yZ0kbIESYYZQU-xNr3vSNGHp6dwgPC0gUYqh_t7ES9aVLIR0IoXG31ygutA_lTNbLHR3_fZSj8p72aAEVGatXKxe13WqIcpXi8099Xf7YeRFH0m2xtO5MM9JlMFDxWJGVI71bDZWfAGN-5AuKSvQF16ldNNDoXGZphOJ5FastNg5RI-uQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی_پرشیانا #فوری؛باشگاه‌استقلال برای جذب دانیال ایری پیشنهاد فروش عارف غلامی، محمدرضاآزادی + 30 میلیارد تومان به نساجی داده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/25066" target="_blank">📅 11:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25065">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hdN_58akhYmaRehxWYMNzRJ_6hn5LPjZqqhsb1S1zrJs7_lx_lg71KNsnQSVyjTDrSuN4iC2ldmp3xchA2FJZLtqiLRkbozAWz81Y6hmz1OnSfKHEU80jH2c6hLn5_FRpf4Wy1AKwsLZhP2Gt0blYFVxh-orrXsLr3YvEc8Oefbh7AwWzAuus5nntMZtOWk2U8OblfEg01hrhDppvLvmrRdej9biBNS9guZ8G4dq4dkN5zyM0a08bBvngZ5pNKkdm3bh3poxITKm1krbmO2ylVPKqlSQ8NH68U71MOjvoMod-rW27FvZUGXtJb-zKtCHITiRopdXfU3x3b47EfFtyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ طبق شنیده‌های رسانه پرشیانا؛ علاوه بر امید عالیشاه و مرتضی پور علی گنجی، سروش رفیعی دیگر بازیکنی است که در پایان فصل قطعا از جمع سرخ پوشان پایتخت جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/25065" target="_blank">📅 11:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25064">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=XS1Gdc-IY2lSetCF1IE9Koc1K_Ocoeoe8U_Z3t11mTJon0yZk0NyVEEi1nadxYFXgdEH9MBlrj56Z4ijEORLkg7K1ssT7HRqdjmyOwZfzSR_KU1H0pAXeXdjBB4d31sUA4bfLzX1S1a6-f0r1A9m7VabJK67S4NBcQWflorQK5Sil83YWn9F0MPt_X22YFfrBMeQ9J1-EGxCTvvOqXdP-No4w_n4QLieu-BtnUgUfovfu77H6NTBAZ9BUrCjlJguqwVRw3rqV0dEFAhuSsTpqbTB9rSSE6K2Onh0HY93LpFQFSvYVrfs5k2FrykcoqeAr40kOe11K-DainMKud-DxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9398d6a28e.mp4?token=XS1Gdc-IY2lSetCF1IE9Koc1K_Ocoeoe8U_Z3t11mTJon0yZk0NyVEEi1nadxYFXgdEH9MBlrj56Z4ijEORLkg7K1ssT7HRqdjmyOwZfzSR_KU1H0pAXeXdjBB4d31sUA4bfLzX1S1a6-f0r1A9m7VabJK67S4NBcQWflorQK5Sil83YWn9F0MPt_X22YFfrBMeQ9J1-EGxCTvvOqXdP-No4w_n4QLieu-BtnUgUfovfu77H6NTBAZ9BUrCjlJguqwVRw3rqV0dEFAhuSsTpqbTB9rSSE6K2Onh0HY93LpFQFSvYVrfs5k2FrykcoqeAr40kOe11K-DainMKud-DxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
هایلایتی از عملکرد علیرضا فعانی عزیز در بازی بامداد امروز انگلیس-مکزیک؛ چه کیفی داره خدایی یه‌مرد ایرانی‌ الاصل تو بالاترین سطح فوتبال جهان به‌این شکل میدرخشه. تنت سلامت علی آقای عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25064" target="_blank">📅 10:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25063">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=FPdgtMf25VgRb5ZtGi5N1mkzelmIjv6QQg3XorCDbjKJp_R8NF3OyZiWYs2LnVf8e8OYvKspiegAMK58_M5-MzpfauxC1vfakNMD6xeeMTB0HKOwo97BUItknxI6utvwIJ0Gd07V6MfZSGSOvI97_TRe3Yn3woyegWzM2YiSHhTLuELdhn20AOc05V97AplBXbXrCxV_VliKnLPDgmNYKbM1FhOApkuuWlNc3B1hCdoATud43XyOSvNpcw2HYYIsu276kiiSTpQhJ3gtqGCURQcgUblxOxkCKT1DLI11sEc7dxwcbOOT7f-EQB9sPHro_Ul6tq3M4Tv1MQ2IahFVRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2866a16ef2.mp4?token=FPdgtMf25VgRb5ZtGi5N1mkzelmIjv6QQg3XorCDbjKJp_R8NF3OyZiWYs2LnVf8e8OYvKspiegAMK58_M5-MzpfauxC1vfakNMD6xeeMTB0HKOwo97BUItknxI6utvwIJ0Gd07V6MfZSGSOvI97_TRe3Yn3woyegWzM2YiSHhTLuELdhn20AOc05V97AplBXbXrCxV_VliKnLPDgmNYKbM1FhOApkuuWlNc3B1hCdoATud43XyOSvNpcw2HYYIsu276kiiSTpQhJ3gtqGCURQcgUblxOxkCKT1DLI11sEc7dxwcbOOT7f-EQB9sPHro_Ul6tq3M4Tv1MQ2IahFVRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌ های جالب دکتر انوشه از دلایل علاقه شدید بسیاری از مردان به فوتبال و مستطیل سبز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/25063" target="_blank">📅 10:39 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25062">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=L-NqOJ2ajvMjSlMHE4mgagrGdgX9xaj9poXWDsoLUSiLlGXdJk5VvqHjOYJACO3ecyV3sJDABjYjK1gQLQklnnJx1EplkRhWS-8vT5DEqFVFoLUt3mBFzswKNJb-fNbyb_G3Zk0SbC9fYPJrYsRABEvRrVdPUxDm9B_rFvq_ymwcWPXCCVrL8wfBwIWRtlV2mq0-iodYmW5xgSJgQSHUofcHPpbqoTvH61vIgY-lVKk1UPOeDw5dd8j87lTMOwAKlB7c_LPXD1zH3NgtQ7t4hot8skJM-OmE_OoaoCsURe2xWtbSZztAnyAsae3GrbmmfWDev2T07069fqhB534WBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c09d93bfad.mp4?token=L-NqOJ2ajvMjSlMHE4mgagrGdgX9xaj9poXWDsoLUSiLlGXdJk5VvqHjOYJACO3ecyV3sJDABjYjK1gQLQklnnJx1EplkRhWS-8vT5DEqFVFoLUt3mBFzswKNJb-fNbyb_G3Zk0SbC9fYPJrYsRABEvRrVdPUxDm9B_rFvq_ymwcWPXCCVrL8wfBwIWRtlV2mq0-iodYmW5xgSJgQSHUofcHPpbqoTvH61vIgY-lVKk1UPOeDw5dd8j87lTMOwAKlB7c_LPXD1zH3NgtQ7t4hot8skJM-OmE_OoaoCsURe2xWtbSZztAnyAsae3GrbmmfWDev2T07069fqhB534WBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
حسادت عادل‌به‌حال‌خوب‌نروژی‌ها بعداز پیروزی ارزشمند و تاریخی‌مقابل برزیل و صعود به ¼ نهایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/25062" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25061">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=gB0m4C5lIj1QJjYaOo5BKOe3gnkDliDzPY7sA4bW2suJmnBKRANdYOnpMkBYUiO49TAwSoRY9KYl0o_QBfkKd5z629dGrjw9YRxH8A9sMdZOGpSuBVB_fWzRYCGnl7FmTa0BpClLvQ4wUBKcm1e0mp3TBQMjwOEDTFVEtj9uLOEmKfmm2EXTondwu7QsRAfPOPr_ESIKPwqOuRrV9FihctQ2sGWuEAP0P1XYIHVV2fVvDiTPPNxu0pvadyXYjudBZPgefIdMAyZGf1zcviuzQXUqlbqRH5tFPqZOlvkKqqd-xKgoUCPXXAvBUocw9TXZFd4FllC6pRjBXJxtiTwPiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/daac7485e4.mp4?token=gB0m4C5lIj1QJjYaOo5BKOe3gnkDliDzPY7sA4bW2suJmnBKRANdYOnpMkBYUiO49TAwSoRY9KYl0o_QBfkKd5z629dGrjw9YRxH8A9sMdZOGpSuBVB_fWzRYCGnl7FmTa0BpClLvQ4wUBKcm1e0mp3TBQMjwOEDTFVEtj9uLOEmKfmm2EXTondwu7QsRAfPOPr_ESIKPwqOuRrV9FihctQ2sGWuEAP0P1XYIHVV2fVvDiTPPNxu0pvadyXYjudBZPgefIdMAyZGf1zcviuzQXUqlbqRH5tFPqZOlvkKqqd-xKgoUCPXXAvBUocw9TXZFd4FllC6pRjBXJxtiTwPiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خداداد عزیزی از صحبت‌های جواد خیابانی دیگ رد داده میگه باید در پایان جام جهانی بستری شم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/25061" target="_blank">📅 09:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25060">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏆
ویدیویی جالب از نظر دختران خارجی درباره بازیکنان ایرانی و نمره دادن به قیافه ملی پوشان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/25060" target="_blank">📅 09:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25059">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=YkP19_6R3Z_LDzGol9km1HEXEbX0Q-lwHi3BPBZqcG2gTyQPm-cfTyxMAeaZ-ten6yLw-jK8V3PBWbmzoN5txXPCRilgCVQsgNyplUy_b6WzecJWo-0TT7Q-ZzBd7R0rbqMWP60QQHyGz4G8RJMWNDD8fAIqxkN4qei8bGah7jDczg_LrD1pHpPw89faj-719msMxdCr4gRnPLdv3DiG3wfPGWNxrc5Hoj26n0UcLgwpgvE3WMkHJ5Ag11rtZfEOulnjZW7cjtl_l-C8HkQj2nnjQfZeG05H8AiaDOB8JlonS7EVgYxO53YMJspmp0w1ZB5UqwIQcqUWyrzUvH0b8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/529bb11b1c.mp4?token=YkP19_6R3Z_LDzGol9km1HEXEbX0Q-lwHi3BPBZqcG2gTyQPm-cfTyxMAeaZ-ten6yLw-jK8V3PBWbmzoN5txXPCRilgCVQsgNyplUy_b6WzecJWo-0TT7Q-ZzBd7R0rbqMWP60QQHyGz4G8RJMWNDD8fAIqxkN4qei8bGah7jDczg_LrD1pHpPw89faj-719msMxdCr4gRnPLdv3DiG3wfPGWNxrc5Hoj26n0UcLgwpgvE3WMkHJ5Ag11rtZfEOulnjZW7cjtl_l-C8HkQj2nnjQfZeG05H8AiaDOB8JlonS7EVgYxO53YMJspmp0w1ZB5UqwIQcqUWyrzUvH0b8jzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هری‌کین بنده‌خدا درپایان بازی با مکزیک صداش بالا نمیاد خبرنگاره‌جلوش رو گرفته میگه حرف بزن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/25059" target="_blank">📅 08:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25058">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GfyOEKd3nrszq9m9d6xASt4vozwI7bQsu7WJ1lSgW4DCT1sPTvc-cvPyEcnxtiUf9HyQkwqci_yeHmQHMjr9KHyHd8238a0LLpIirW9y9jTQRXUICOYNPIV6OQwgDMp9nCW_LSe7tLkcdFvecPf_ziy47bOwV3PjoUrlTTjdi75eobMBhtxtreyAjDOypwQrxoEV6D_GHgstl1zlDnPU7JCr503W15ki_9jfflTVGbAibSwJ6lo0VYxsMtrhjd3LfgFALSxVgWaUTB0m-3noGRgDwldxqX3ATte0rPY19kai_wrc_UBMWtA_AA8xPu0nEZxGYY2MNPnt88AEalI5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
مرحله یک‌ هشتم نهایی جام جهانی 2026؛ پیروزی‌ارزشمند و البته نفسگیر سه شیرها مقابل مکزیک میزبان و صعود به ¼ نهایی رقابت‌ها.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/25058" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25056">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FFS1I99-Kg_bKAKko0iPLO4PWQpr-JAatK9iytoh0ToH8_fqSHG4MfbyvcQZuv1eb7Rq_0arVAwC4P2F4WenGB99sN0FVuQqitBQMfP6uPT-zornVOUmDw4OOA6qzGJwDfjmS-Voy_FayziwFoGqhnXl5mgLJy2ORuxAQ5whm7nORENXXaRy-nhGJQIAxhhymysKN8a8kFVdifCEMcmTtW2dFZwbHISyJr4s9sdDwFpPedyGWcxykNwpIpz0FgTUibjUlVnk4PYDKJSN95Y2f3BtqUXpgyg_8_g40sW2KCMRl4c26v-ISL3R0JsZenbK-7szxojQ9KCi87qpM3O8Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S5KNkzWPutJ3otfrYGgugPi-pDOsQvKa4KxiSzSlsCyVxDPv-O5Io2pm2VQ6XsfX78qmBgXMt0jJc4mTtQPUCUeKD1Niq7oXyBHxVJ8v38s6DSGJiBB2HNYve7uPrEP4N0k_N2emR7rJCO_9QLUD1sd7BEbUBCQCyThhqKy47eqVbq5DSnSncR2YD5YujbAdnsjldHuWIECGxKurAWegJrO_ZET3hBsDPnL5SoY4jY91J3pgC_shEvJq2d5KPhcIStyV6RFIEsFkJHxZySI5BKpJ6DpHS5MzeBQ13_J4EtndkO_YWLdyoI5aRJizUb1WRUWGKbSNIUcH5dllt7TJXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/persiana_Soccer/25056" target="_blank">📅 07:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25055">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KW6Ntq19j_22vyc1HRVb_Tz2TC2o68v9r7p6KqqHI2z_6zgSTUAWua9x-A2Cb6U2QEJQZDDe8laC1w5i2gqQLCNcvLVnUyijiMpcirB0cCzLyQi-mNeNVp1Psij4mYhpMTR0ZueUxx7KsB3tW_j5Soh7YrxPLbsAaMNmttRGRURNywyO5vrQ1EXvBF0Nklzp9Tx-ialVz-MDAdH4YxrLH-tW_fSX_VlcWaId6681G3VTRKn2DGj89AlWz86kHM7xtGef9JxoN_-u3AFooE_Hc6bWqMbCe2vHQU0CZuS-u8EirvIr8gztA_uFXiAJEQzkqRhwKKu6HA_aM9P6ZJCgGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌ نهایی‌ جام‌جهانی؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
مکزیک؛ ساعت 03:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/persiana_Soccer/25055" target="_blank">📅 02:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25053">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/A5k5VNX01gFs_BosjjZwEy-TvrFlmUf9JIhksKSG5VxkdLRm4dSeS5zhdQayVUQg4C1saNduCVWuyTVE_KMSg0Z4iLVPUCmz36VNaA-xD6cK9pJkePeQMMO6FnKhHlziFQ_PW88ub-pJ_PFg4XPalcTbO5AKXvydJOCRTKta-c969Wozz5vQcLDfOqVhEsxVNcuteIQT5DhS4ZQnhLQbktTKSxhdpwjGycGP3zDrTPIFsXyr0iiGxN5-Cg80f1x4E7BDKBV8YAM1dHJW1FNzTOBEEKdpSr02LA60FJIHhUr3T1-RyOO8Pz3Sb-ERMZ0Ojwd8CEHRyKnA9Vaiomr-zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/M9Hy50MOrOcso4zNNeAfZ49OOWeoyG2jkcLhL8fuhApOIR7XP1KzZxazGtJ4jLcP0DkvBQvOBEpV6uO1aOhZXVPTCOPZXJ3I2dtwJ4FlIEeZg_0IgsRXAgHnBf2BCRsnxR08YgnFGx1ttX4A2nbM3qYZ62rgCri6FIW5_DgbUkyvwy-CIq8YsQpfsruOm5OyILyz1eaRxygDDOjS0up1WYNwjKxFI1G5GmchaiaerOs7i0qiGqxvJ5XPBVUgOGbwW5akf6lag8pUmCKRlo0MCU5KqHnTo5T0bXoTsVJJ-Xf2zmaVdmOtGXFDxKNyb12c6WD4y4gpKUl22DatuHjRcg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛ از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/25053" target="_blank">📅 02:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25050">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbqudchtSrjF4Av3at1CAjygSm5KXdkS1ynwkJo0skeWNlVRSJwYvKq_sdS7gKYRfcttPxYM815XxE_GPEapLuRmlzs7Q2AIN15ybBEwe2l_XJLvbtlpYyNDD5tqI1TNbTXDIl-vkPrGwPwncE54LiNAffrRwzJuIr8ehsd63D0InrChiXUhrx3GTjk8czjPfWSzO-LyGs6UtuWn9_odsIBGxzavB7kCMP8qFZCpXqXbt1IiQ0LvyT6Hw1IHbEQhgXWAfBjHR9e68awx09WMqBL94gCurbPz60KTGvHb0hn8Zu1AYILdXWyoZ0GnEC_0nTo_ZyfcFthMGITX0AG0zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باز هم ناکامی تیم ملی برزیل در مرحله حذفی جام جهانی؛ حذف سلسائو در مرحله حذفی شش دوره اخیر جام جهانی این بار با کارلو آنجلوتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 74.2K · <a href="https://t.me/persiana_Soccer/25050" target="_blank">📅 02:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25049">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WtJn1ATttGk0Dzj6e2xg-ey_o1XhIy0unRLqLuu3_M1yFrmZlUjnk-KmhTX1XI0AQeJTBuvUSwzc8Cspe4KMwBamJHT-I5BuiK7YIXZnPXGK8mh8QvqC3cKZGHnMZPphSUA2u6puQc0DIRGovAmT3Tg0JfL7BWC0RrMiyR4WDoqdGSb6h9KpkOMnlQ78JkKA4gduHNbLvugixeNgB1J0poHA9K2pUfpShhhOCXVMYL2iJ2Ig18lfECJheAR5_WfP2b_-S1JixVFef_p36f6QhnudjyIwuUffX8MEFC_SYVraNrCDuh6heyvkszl4KhL6iDtHUpUgMLWReTe6uUaWcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 74K · <a href="https://t.me/persiana_Soccer/25049" target="_blank">📅 01:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25047">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tet1pjVD03_z1P-XhE_HI8o-DsHvHa6qtytSxGIWmgPfQSF_yL-cHkS_ZwMRdA3u9G0qZ1In9zZaX8PuB6OYoqDvODlA0QoAafOxSP52Cx222pflfRYKI2FqQWd4KdQsNADIHYk1rvSmgtQskwaassugdKMlS166ZcjHO3abZ3vLfQnQnyXNNhmYp321ahZSppT5Mz46Oek_EJ9ypoIxsxidbBAAPS9OBqCbOqHKhIN48dD7S7SIhOO4hwhH5Vz5ocdOhv23pl_aqI_tI_46ttyU8kEU5g5lsxCwlsl3zm6Ho1RUnz1YUADFtCgtK5U8d2pLuN7W3azs-GomdIHvaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارها‌ی‌‌‌امروز؛
از نبرد خانگی مکزیکی‌ها مقابل انگلیس باقضاوت علیرضا فغانی تا جدال فوق‌ العاده حساس و تماشایی یاران رونالدو برابر اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 72.3K · <a href="https://t.me/persiana_Soccer/25047" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25046">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oVVYTL4RyNMJRxYR0T4OkqRYqTrxiVQ0nqNkjEiObVsQV5NayR-npIFrZqUOm3QiTh_Kl3AXE8JvgoYtwRfpO-dzElAYSr2XDWDNivsuqW9Td8wOd2s1yjoJoVbAWMAwc1Wz_L2V4IH7uR7gMXq2jqt0-1N8yPRpEsTZ3SzTPAz46-Kcp_TfEy2Fvt410nIYvbXnwNE5WUHG5SUyzBsV38187fInhMef7U2j_4FEe-YP7cSXN0csHItPx4c-yRQiVnkgmpDOKtl1rrBFsbh4YdUF1MXwci-aQHKwlLmiuPLuuyLHiYIL4n794BQIAUqsomKGmEYCVG0kd12wlF7woQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌ دیدار های‌ دیروز؛
صعود فرانسه و نروژ با درخشش‌ادامه‌دارامباپه و هالند و طلسم‌ادامه‌دار تیم برزیل مقابل‌تیم‌های‌اروپایی در دورحذفی جام‌جهانی
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/persiana_Soccer/25046" target="_blank">📅 01:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25045">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G6I4p9RlIgHteqeNNSNGBe7L0Z_wDoXcIPJm3rs0yvL-5222W1VzYTDMxS7k15c4tpTpyWMGU52b3pxYADOfwzdoNlXyFe3qF8MdaqnvclbGiby9uReObWf1vi878unAZAsozCKD4WVgKXBMVr5GmzDj5zekl27J61aNSp-8K80ERA1WokGzYkHEzMH8dulxu_BYoNrl6S688xi0jGpwwEFzwtD8soIrXbLAd90j2niqove0K8HHa1Wb9F9zN05HBsaatpxTpzWgxSExhT88A554Tkt2s9vqnY3fWTYdRQ4IbsG71gSa7BctansN8q4gYzm8oKof-G9mo6t2whd1qA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/25045" target="_blank">📅 01:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25044">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇳🇴
خوشحالی هواداران تیم ملی نروژ از صعود این تیم به یک‌چهارم نهایی جام؛ نروژ به مصاف برنده مسابقه دو تیم انگلیس - مکزیک میره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/25044" target="_blank">📅 01:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25043">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sj1Y7kyCMBS-aFcFmvpYpwk0aRsFsCkWOKRnVlkSXdiyiSV5Y7MVSArPl_LHScFGxWw43MFqm1nJP_OSBwQFINrfPM3EICbQNn-NBdrYaFYPvyumNjYCsEsaPBGbrVhnlFd1nB-d_tOfALphiUX003akTwHFf3vNV1KvQi6vaYqbAWr4k9lTwpoE4UjnsAYNlECvZ7lJ0HpHYV6gUUNZkvEE6TH4u6nD0PNFoYX7SEIbgoEMvdxa5eSjFfq5sHAjij6MONzhgJzPyYnt7NP3pCwAZ-lBdk9s82ez5nyyfBbVbMi_LEEdeUGD4VUWUaW5mcqidG5Ppcse0PKVOC3mMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی‌جام‌جهانی2026؛حذف شاگردان کارلتو از جام جهانی با امضای هالند؛ دو موقعیت دو گل؛ هالند یه تنه نروژی‌ها رو به مرحله بعدی برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/25043" target="_blank">📅 01:36 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25042">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2de979c355.mp4?token=C-7nGWKo37U1FoduziuZw1L9SNnaSv8O__hTF1qZTEXKEtlZbJcTVusUlPdhg1Dh6AmlaUekkoXrEooMuP0ibUhDA0FZpR7_lbjIEwJmRU_R_-nArlVMdt5ceamP6e1XNUtVcKMXosFPI8W988R0dcZ828r5FZJPney59E52wddh2vzfdCelCv6uuiQehACv7eVjaKK-OBpiFTlv3HNA-mNKs9F8VF31_S89iTOWJ55zu36p3zhMRcQF3O7wfim-M5mA2fH3kxaYkPY03Ky5BguQYczvHDnjlqiqMSDWVChzL--651E9BButHx5YcN_C7FFNQTvI8PEKS2sUrn7GOQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2de979c355.mp4?token=C-7nGWKo37U1FoduziuZw1L9SNnaSv8O__hTF1qZTEXKEtlZbJcTVusUlPdhg1Dh6AmlaUekkoXrEooMuP0ibUhDA0FZpR7_lbjIEwJmRU_R_-nArlVMdt5ceamP6e1XNUtVcKMXosFPI8W988R0dcZ828r5FZJPney59E52wddh2vzfdCelCv6uuiQehACv7eVjaKK-OBpiFTlv3HNA-mNKs9F8VF31_S89iTOWJ55zu36p3zhMRcQF3O7wfim-M5mA2fH3kxaYkPY03Ky5BguQYczvHDnjlqiqMSDWVChzL--651E9BButHx5YcN_C7FFNQTvI8PEKS2sUrn7GOQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/25042" target="_blank">📅 01:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25041">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=lVNGyUfV1OWHnAAHQPZyRDk9lluhm1IAaATyAvsM4HLJIDDr8bzdckHbq8E96RDis13uoer9euR9Jv01IaKJ9uiCNceXsPkMC83PUguGvZu93izjyZfmNLwXGKcp_uqzL-a-JLbwZzSdj-GltVKGsQP808HQnvMV7NsXM_5wv6edRBy1wC_dYtxeqRubU9gDXlep_c_nAcgvKQgZyK9NoVVqp24XNVU3GoWGCfT88T7LKAk_prTKa2MFu2XnE_qPsIVu4wnghd4ozdaYaSQBnB2Pxo9rOAgfnFxgdX2BrVkzKkszawZXKpN_xBIu1g7m8eHHHS-rt5tHorI9_EF9Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae7cbb0612.mp4?token=lVNGyUfV1OWHnAAHQPZyRDk9lluhm1IAaATyAvsM4HLJIDDr8bzdckHbq8E96RDis13uoer9euR9Jv01IaKJ9uiCNceXsPkMC83PUguGvZu93izjyZfmNLwXGKcp_uqzL-a-JLbwZzSdj-GltVKGsQP808HQnvMV7NsXM_5wv6edRBy1wC_dYtxeqRubU9gDXlep_c_nAcgvKQgZyK9NoVVqp24XNVU3GoWGCfT88T7LKAk_prTKa2MFu2XnE_qPsIVu4wnghd4ozdaYaSQBnB2Pxo9rOAgfnFxgdX2BrVkzKkszawZXKpN_xBIu1g7m8eHHHS-rt5tHorI9_EF9Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/25041" target="_blank">📅 01:11 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25040">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=TSvWVAF-0H6jrPoOiY5T9pBRXYIw8RsOUfFX2jPuggNXUPdwJ76UkmuUpMsdiKxoMtt9fM0JQggS1k3R-P7c5BaDCtLsOzMJAVcvW8-TGLORX7InUXL638kZAG4eklyC03zRD_UnVQLAZLm1Tk1iIrXv_h3RvjBQi7H6MWgVnm7XjnY5gWy2edISoyLtDjbf0YXLgnCI19tsjCejFfygLdNXXrjYk60BX-MGEIUWzvu6TJ69s36rC2U22WvhfxDtbv8ljCPfDGcPJ-qVgRF6dL_nlR6Q_yaqpQwQvHh03QnUyH2Vk8V91QsIZ4ThqKCqzKvDdzvw-TQX-JhhZfe4jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8897e8ba1a.mp4?token=TSvWVAF-0H6jrPoOiY5T9pBRXYIw8RsOUfFX2jPuggNXUPdwJ76UkmuUpMsdiKxoMtt9fM0JQggS1k3R-P7c5BaDCtLsOzMJAVcvW8-TGLORX7InUXL638kZAG4eklyC03zRD_UnVQLAZLm1Tk1iIrXv_h3RvjBQi7H6MWgVnm7XjnY5gWy2edISoyLtDjbf0YXLgnCI19tsjCejFfygLdNXXrjYk60BX-MGEIUWzvu6TJ69s36rC2U22WvhfxDtbv8ljCPfDGcPJ-qVgRF6dL_nlR6Q_yaqpQwQvHh03QnUyH2Vk8V91QsIZ4ThqKCqzKvDdzvw-TQX-JhhZfe4jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
کریستیانو رونالدو:
خدا کنه آخرین جام جهانیم نباشه، تا شماها بتونید بیشتر منو اذیت کنید!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/persiana_Soccer/25040" target="_blank">📅 00:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25039">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qu3o5BBaAHahrpP6W0QuNGGPxI-Rv4Hshfh4h-VGhi0enx6b2WZlQU2xW6sMjb6gIxwfsiO9D3nXHMRN8xaxgEmvKhutCzYm0rOrNGxZeRR-TvxNLgeUbLk6im-gvWv1ezi_kwHvBD3Zb-U0QD6Smmm3SZdE_Ao6azAZh20ksd48pi7J1iUnJVMxd5kAfuT5p3zrHs8tw0Dvu3TU0YyrfgHuBIcbp0CAhoFLuUbRpMwEkXuKPGQO_lQGzecgNksg8sl6KJIrGbztqsOmlE14YYJLIzc2mf7-gjnW-kXPWUktJuumpw8CUs3tLNHY8ik9jC_FpDzXs6pYtdGVPypxSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇳🇴
پدر ارلینگ‌هالند ستاره‌نروژی منچسترسیتی:
شاید روزی در آینده نچندان دور هالند رو در تیم رئال ببینیم. ممکن است اتفاقات هیجان انگیزی رخ بدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25039" target="_blank">📅 00:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25038">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8Ik1cRvlZMnRIKBMfnZktfrGT4nk2aZfzIJQ1-fKMxx1PMAN94X_66qPJlFUtrXg0Vc0_0p31GEm9OVSDSLY1KKU35gbSmJf77tJALjgp964-JfIhi0Su-XihzGqaCNt08VzHJwU7QiGfRcyM8fx8tkWrhW70BqTd_1ia73uRbOXmVxpI_95McKQVldCfbu1rqYtAqGn5vBsqjcj0yfQSs8DrVpUqiQOEgY3y55FHrXZPYcIPEbvEyMhtJbZgxot44Zp-obS_4ZYGjp2dz_ec6-Z_BVCLnABfQEdBCb_wKmyQlFuwwzzqFlqB2CLz-9EPMaLvKnS97sGKul0HvKLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ کارلوس کی‌ روش در بخش دیگه‌ ای که از مصاحبه‌ اش به تعریف و تمجید از مردم ایران پرداخته و گفته من حدود 12 سال اونجا بودم. اگه روزی ازباشگاه‌های‌ایران‌پیشنهاد رسمی‌ دریافت‌ کنم ممکن است به‌آن‌پاسخ‌مثبت بدهم. من برنامه‌ای برای بازنشستگی ندارم و علاقه…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25038" target="_blank">📅 23:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25037">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mt0MjiLCUm1kO0UVO1RBRujnY_vKFjV1NkJm2q0SUl_j9jPwGehPPHiclIRz0aqo-nqB8xK_dJcEfi_i1TsfEBkHI5tq1wncpSa4xrM1mswEiUuYWioE0DjKVmPG_cyqLDMTyN_i8mU7oNbrIjRo12ZJnEgcno-53jgKkQpg-gUxdNg0cOf13BxJpA-bSrBYpagBygemQiaUJsCmduIp0oiqKLf27JmryPapPB9_BJ6zBT7MulCAPbEdjAV0BCVoKKkHhkDXRXdjhnv1jK1NzZuAtVPKEEQm5F4VsRNQNmlAQFaQhCW58_8HkqN0C_1a1Up5JzKRFGV8-2v965qm2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باحذف تیم‌ملی‌غنا از جام‌جهانی؛ به احتمال زیاد کارلوس کی‌روش به زودی قراردادش رو با فدراسیون فوتبال این کشور فسخ خواهد کرد و جدا میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/25037" target="_blank">📅 23:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25036">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=a4JaL_is-rfvqTk-eYhrDKOdMfgp5abBaYiAg9jnjDtJDxi4bqjb4WkbyRKzjPBLl66Hk5HaHIQ1OoLJcq-q7R6kd9SEkEUFXjUGIuI6OgXiLgDbhSlVkEmHjIQbxEYfwIZkCDE-9cJoxQ32d37MKTUnd-LMUJoITfGMOIfEkLTI0xFKzE6CIx-9t7-EJIwvHExqUtt33A3OllHP6jIf16g-xHlnvLZdh3nOVhxYa0PxHWbutnyGwGWas7W6ZIL40omib3dTb9iH--pWVUe163Ml2Gg3JqsyQzIRd5Ou972lo-UF3bF8ZP0gcCc2vbhukcMDaKMYqRhw1xe59xll5K8l955AKvcxFAtYyw1K32vwkkBqf5G1JM9JPbRJFyoVT6cXec1mg25zcXa9AQnUYTS1gDH6VdoOpCoa7kykvFikCMhJu_hs2ZBLR1Ny7slCy-_ST1L2kn3C4k1geMy4vJXAZNEtCxC9GZtB6-mxCZG_hAAO6x3B2flVoH9gwv4QWADcafKhqhuxUCjYyGKjfLO8vQYY6yhv54UaU_5idS7qyMpnXPpkZBXNKUkVOyicUtLZJP9F2Nt9mK3WmmwCptRh4R3LUjWy86p42LqK9zq9jMqJmg1cEI8jVXoyFOUbow5g0RKzBa02zFZ-G_TeZ-hbZS42O9OUtvF-OH77bOU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/81c1096e89.mp4?token=a4JaL_is-rfvqTk-eYhrDKOdMfgp5abBaYiAg9jnjDtJDxi4bqjb4WkbyRKzjPBLl66Hk5HaHIQ1OoLJcq-q7R6kd9SEkEUFXjUGIuI6OgXiLgDbhSlVkEmHjIQbxEYfwIZkCDE-9cJoxQ32d37MKTUnd-LMUJoITfGMOIfEkLTI0xFKzE6CIx-9t7-EJIwvHExqUtt33A3OllHP6jIf16g-xHlnvLZdh3nOVhxYa0PxHWbutnyGwGWas7W6ZIL40omib3dTb9iH--pWVUe163Ml2Gg3JqsyQzIRd5Ou972lo-UF3bF8ZP0gcCc2vbhukcMDaKMYqRhw1xe59xll5K8l955AKvcxFAtYyw1K32vwkkBqf5G1JM9JPbRJFyoVT6cXec1mg25zcXa9AQnUYTS1gDH6VdoOpCoa7kykvFikCMhJu_hs2ZBLR1Ny7slCy-_ST1L2kn3C4k1geMy4vJXAZNEtCxC9GZtB6-mxCZG_hAAO6x3B2flVoH9gwv4QWADcafKhqhuxUCjYyGKjfLO8vQYY6yhv54UaU_5idS7qyMpnXPpkZBXNKUkVOyicUtLZJP9F2Nt9mK3WmmwCptRh4R3LUjWy86p42LqK9zq9jMqJmg1cEI8jVXoyFOUbow5g0RKzBa02zFZ-G_TeZ-hbZS42O9OUtvF-OH77bOU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇵🇹
🇵🇹
درگیری‌رونالدو بامارسلوبچلرخبرنگار برزیلی در کنفرانس مطبوعاتی پیشاز بازی پرتغال-اسپانیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/25036" target="_blank">📅 23:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25034">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ROElCbykxsMz73E7NekZT4o22aa2NfeC245wLhPigZDuWM6Xz42mJxEIoWJWFE3Izt3lB4-o9eg7g_UtXT7iPE6_U_NfboGTIiLkSnydt0xxIXAKUjc3DLgUTDj2ShsZj9l55T5SHjcpEDm6JOcJM9M35gBYIOSXGMtcWHalhFx8gXJOkLAyTtBNXcnvamBQlrdPdoPqUXJ77z4Pm6Q2Czyg8J4XyCDvEpjI0ay3Eq8AknV2ec1D8_RacjZcwuKSVdg-XvqBwCJOARWzrKRaQITXRcO03DIFoTMgpNrpfFpI8qNej-3kNTaemdTcQuTftrXp1AFWHquLst_TN7x0FA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ علی نعمتی مدافع‌ ملی‌پوش سابق باشگاه فولاد برای عقد قراردادی دوساله‌باپرسپولیس خواستار دریافت مبلغ سالانه 75 میلیاردتومان‌‌شده‌است. درصورتی‌که بانک شهر با این رقم موافقت کند به زودی پوستر رونمایی از مدافع جدید سرخ‌ها…</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/persiana_Soccer/25034" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25033">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvVYFjQKgIAaPghDn4zYC-hCVCMA3dTHGk_YZF2B1yUZ2Tri64FXtNNRqz5hw3MNy4Be-5oOuCkl9pXtgPxeiQxu4mpL-LQ0AGkgchHm9anNo99iliGZ6rNsNTIcOdPU9iDly1N8E3kLBxqIzl7t9ZKioIcg-J0W_y14LyBJ617NAia8UTTDcaQY5kUGHve6KJ5-aNZHnR5aOCgU_4yl0kihPdRgUpfpwpedXyvhI1Hd1E6Ue9zAh3ihjtPRDEEJybYWM0d3-5ZjsS5-U3oi0miaoMSPc_m-BH__F8sl4qZfFvGlXSutBP1sDh22rTjz75P9SNx1YiUY44PHBiGcUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی 2026؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/25033" target="_blank">📅 22:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25032">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromفوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YXKSSy6TRvbpB_i8SShlFkmp-OfZmVahtnT586RDzfxzaUXr4bnJ-CdxD-GhJN11APpxqW2Hhg3Hd9N-ifpTDQvXu4c9wDyBwL8Q-YuqRClt32Gyz2umy6f1fZB4RAU45dWe-_-8aenb4HxpXQbsCDpgKYUzle5Vjhv9mrFXn-m1m2muGs35RCjN7L8ifGP1PJsyhuegLnOT5x69TVN3YSp1DMy1c7Wde_0AMBsSPnp6fRtQsA7Ik8c26-cRo2JH2YUn-c-4im4DR8dL58tYduqomwKkpEPHsfAMwHTHIMf2IuRc6OUDANO0ejjZ4e1HR3wgkokjA70kt9mcsIQotA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/25032" target="_blank">📅 22:58 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25031">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pMeYQXpFPi95YIRB-uI2F6dpqMJ1wOgRzj38wSGNTBAyMfgpD6tYAfg5cDf-Bo7s05lG1C-cvZtA0uRmkrYPm0UOF5nzCXy8FIoBk1h-N4wl9B923BJencerCHXZ_OzWNszLQjntGTkLwl-LXiQrejveZmjgjT_-DXU-fgactDmh6xHf5XkhdEM1BV_wTxlEZjV6cNiFm-WLtmWePeXiSCNaRZv95NCSmyxu9HjawZVMg7SPx93lJx8OTXNs8hqSbW0-hfXcWMUjoJm45CJunmhjYzSFkZ603M0OpkpOTC6ckDLACzjGiDM_uF-o-qnChlITZCYvI9dO8nVPHt44sA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
باشگاه پرسپولیس برای تقویت خط هافبک خود؛ احمد نوراللهی و محمد قربانی 23 ساله و ملی پوش رو رها کرد و قراردادی 2 ساله با پوریا پورعلی هافبک دفاعی30ساله‌ سابق گل گهر و تراکتور بست. پورعلی درتراکتورِ اسکوچیچ کامل‌نیمکت‌نشین بود.. پوریا پورعلی جانشین میلاد سرلک…</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25031" target="_blank">📅 22:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25030">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fn8wD3cNhCEeQLa0yehqUa_YDezFZ8s8UjJJvP_cfDx-rGqqlVS0tNiTtAoVYpN1OGCDs2bS1mAd1QUjit99ha84n6konh22GkZERaAdSwPvXJUF2GFddghiz0WwKm0wiRxZEoQYNhvb3ME5Hhnd_I4_uGs5fxPowPPOYNATH6_gfReCHKMG_JhRZ1bJAovhxkij7EfdtWHP2LNRJ4d5trcVm1Gbu0c3NMpfMClQI_MJGzszVt1t9GFhPU4Rm2IT9z7_Zgm6Pfj1oYJ6smq822tZesoYg9Hs-nvfdAa71Dh54xBWoAmoUdP0dKJ7lbyB-hK3xIeipm6Rmiy3LF5SBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#اختصاصی_پرشیانا #فوری؛دراگان اسکوچیچ سرمربی‌سابق‌تیم‌تراکتور و نماینده رسمی‌اش از شب گذشته بایک‌باشگاه‌لیگ‌برتری در حال انجام مذاکرات نهایی است و به‌احتمال بسیار زیاد فصل جدید او رو درلیگ‌برترایران خواهیم‌دید. مقصد جدید اسکوچیچ فوتبال ایران رو سورپرایز…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/25030" target="_blank">📅 22:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25028">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eFmR4uMIirHeaZulTuftQYsNH0YT2tKc7IdrcGul-gKRWOpQ1u0x4dGXUEQTMM8fOnkB9Dk__CPCnatkjcQrxqOxiSHCQiUBBnk-LdSVSA4TLWDShc0QwbqDWdxV4VJvyrP6Qt4mSr-ueMTgm8jKOqtgxqUjSujfGz7SXrGl5FmxJ5Q3M1i9kRd8xJyOfLQOjU9tdDGOpFFZWS-Aq3Z_wmbOyRVG-oHDXxPFt4qh2BWxJz3eqh-bzzn7Cv30CpRf43n5xoFQw8fDFhCv9_9OA1uLlsNkoRZv24NFWEf8cl_AiQfjvRWpgnkOa-U3KnUNsiItHWvLtSAFhzf0XvJE0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GZ8rfewOJA58tJ422HO4Zu7uOBcA9dkQy2L1EgFSGqKr8ZNasqIR8s0aS9BD3Vkuu_-CwWHoe5SAmADw1vECeF_DXTFkKueiUYnMYP3rV4z-x1E4JS6iP30rpClnxBi_aM0nxFHMgTRM0tmCa8SOrLlDqJp6IjJ8PwoYVGqeJGYTSnUYbwG0YViMGdzoGqt2Rxs2QjWfvlH7MMYm4hkwB7N-47w7dwNz1_OeHOF_D-8V1dWUATQu9JHJ9fV8dKdHJ0QUbT7d0U_lOLTCDZ1NKPxOcurq8fE-Pf_kRJ9vAx8Mc6WqGZxLg0wC7w5eaMrWMIGFgCGAY1y44UEd5yX8-g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
یک‌هشتم‌نهایی جام جهانی
2026
؛ شماتیک ترکیب دوتیم‌ملی‌‌برزیل
🆚
نروژ؛ ساعت 23:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25028" target="_blank">📅 22:10 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25027">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P3Fd42WcqEOUM2XrcSiiR6qmTzVO-YOLIODP7QQ96q1N25X-4RRX9Do5pIROrjP2vztFD_GariWyVfxjNdt4UnS8NlYXOylOm823kwbSY_mHe_5MDxGHChQHprqubBIKXnozyJUlzzrarAQEhw492WBI1ujC8ujGIH9fh-sopf8a1vLFiSWKh-cVb_UykPPbaOLd-OfMl0q405Uwpthc0WjH2U6O7Jrrx7jCvCARYOsiTYS5d3pk8RUKwEzOT5QikkRNg8cVBqcmL3GVJ38mjTuAu5pbsS2VvicKVM9j8l1b7iHaWBO2o9Oa_A9yj9_UGB8WPL319AuNNH_fFoQ02A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
تشکر دونالد ترامپ رئیس جمهور آمریکا از فیفا برای بخشش‌کارت‌قرمز بالوگان‌مهاجم‌تیم ملی آمریکا. بالوگان حالا می‌تواند مقابل بلژیک به میدان برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/25027" target="_blank">📅 21:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25026">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CT2ZOLnjmGX198xNlH1rHxHYYPmA3xxc-DurMjyCdGrUgUAUaoEkiJBocY3ieVOvK3lr0vG3kZJBWxB5AhvKwcjg4UO5YbtIYYJH58gYzENvuATnkQILPv_YyVolPomENOWVJfx0bd95t2JJ2LR2LtlG1foUV49ByU3RNfTvzd6iZCrJAlZNTcKpOzYCsXNFjbxRLccHKeyNAEhA_u_Y2mcu4MqaMt_cOHL2f3dz7u8wsZxo8JitwWFwi-TdDsxsaNqubcujvBEbEIXU6mW-lOFd_O-qssl8hNBasyDVxcNQDxRlWtN4WL5J96NxzjdbfNOrppCYDEi7aE1aWmRV3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اقدام انسان دوستانه همسر رونالدو؛
جورجینا برای کمک‌به‌زلزله‌زده‌های‌ ونزوئلا پنج تخت اورژانس به یک بیمارستان اهدا کرد و ۵۰ هزار یورو  پرداخت کرد تا برای خونواده‌های آسیب‌دیده غذا تامین بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/25026" target="_blank">📅 21:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25025">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Spz8abB-TZzYu7ahdWneg5F4dPQEvLUADbb2qTBfnrbv5jgjlfqE7ofpbwoJhkk_CTVp7d6maPSWM99tj5kSoFfy_VuQqEgzDPEuJ7TMAOSiDbQ6Xy4p1evdYx2StcZqy1xaTYkcRZ-BkpWHUNrSd5-jQN95Y7ccFXoScU6nhuhBoA11KA_JmdtXobg_JeEZesopLzBhXQuZ3C73nbLEm9TEo-EfZpsmYJA9A3EmAM3tCnHgyjvX5sifOPTauU9dwKF8pcrEpEK_kBOjzT_he6vtTVSJ9q_Ko5PVeF2A5_pdjTWIZsOX0f27IEaV1TrwI13mLaVAQdOO6XBR_HX6NQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوراللهی نامزد جایزه‌بهترین‌بازیکن ماه لیگ امارات شد؛ احمدنوراللهی‌بازیکن‌ایرانی تیم اتحادکلبا امارات بهمراه مهندعلی، تادیچ، کوجو و کریم البرکاوی نامزد دریافت جایزه بهترین بازیکن ماه ادنوک لیگ شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/25025" target="_blank">📅 21:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25024">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GERc4Dr5lgq8wrU6Y23QcMZSUBvncg0GZoticUfw_lJTDLF-ZttLDx2I2QCl5uBu8RKLcfXWnMhM9YSSSIf3CToqMbjNexeSR3kOHSOvJmVVF--6m8BVXejcrA9QvE0FP0MS0Mz3v2tHY0IxltrChVpHFeIN_A-Xzw1nyP-_mz9A0iaHnjNC5dua7fP0niCL0vhrWfyQy4a_AaUS4iF_mIOVkgJtr609xn2eotQ7G6IMDJaVVQzBo793CQHrnnvR629J9c10uzijR8vK0s8YRgwKayzqfjhdzamaj9Yq1MLz9jw7s_S3oqwQFLsWGhfetcoLfBB8OTXEolhRv01eEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/25024" target="_blank">📅 20:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25023">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PN6zMdK1ezpUjErSc5AVx3rmfkn-FHam6EsuU3Z4YDtJQtnHS1UlAft-I_DeoyDKUhYQr2DHh_nsGHwGS6y2d-5ciu8xiyMhZE0-egwN1xgiUxn-vTtq4qg9AeAUejrVN6FJRnbYxYGPeRwg26E3q-B6Y6_QgnJ7MxyrtRyyOdrNAxqgqJ78sxh-MtW4JSahFbKgvL94feJcnwLb-zJP7-xs9PL668r1Xrr_5iRzkvXRwFtSX_9g0maVqNbJx48kej0zv4ZHR2SQci6m1tVF5bsHvBFqNw0JwD9Lsz4393OEtE5POYzCDVhSN__IVO51YGbKJtDhBklq8IqeMmrbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
مهدی رحمتی سرمربی موفق فصل قبل خیبر خرم آباد با عقد قراردادی 3 ساله به گل گهر پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/25023" target="_blank">📅 20:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25022">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=twxqeKQ_by5Fb5WJh7sKmAck1zCPFllwfj58pIPjM27OBNCKT-UMX8p9_i2bK9Tq6a0GjVQTq3CJY6k_Jwnh-ZPLI_Uu2si6y1AUjIOVdHVmserSgN9HIddDLMD23n-LDXZB5HE58i1QGwG7figv7H-mOh8aNFeE-8ctRpCicAchl8iX-1Atp31RU6XOQ-78t5GsFrgN99OKBQfdHj9AnZHeh9kLcKxqsAIMsiwAPmGYizEyz5BWfLi_hM7Vmg929ix6cLG90homZnRxvNDsRbWopVWWYFjHKDfGm8Tc0jS4bz6ody6PiRY6ytreM2pVFQP2M691M5gjm8kmugU88A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9652d5ab0d.mp4?token=twxqeKQ_by5Fb5WJh7sKmAck1zCPFllwfj58pIPjM27OBNCKT-UMX8p9_i2bK9Tq6a0GjVQTq3CJY6k_Jwnh-ZPLI_Uu2si6y1AUjIOVdHVmserSgN9HIddDLMD23n-LDXZB5HE58i1QGwG7figv7H-mOh8aNFeE-8ctRpCicAchl8iX-1Atp31RU6XOQ-78t5GsFrgN99OKBQfdHj9AnZHeh9kLcKxqsAIMsiwAPmGYizEyz5BWfLi_hM7Vmg929ix6cLG90homZnRxvNDsRbWopVWWYFjHKDfGm8Tc0jS4bz6ody6PiRY6ytreM2pVFQP2M691M5gjm8kmugU88A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
تایید خبر اختصاصی روز گذشته پرشیانا
🔴
مهدی تارتار سرمربی سابق تیم گلگهر با عقد قرار دادی 2 دو ساله رسما سرمربی تیم پرسپولیس شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/25022" target="_blank">📅 19:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25021">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=DF_3P7zdeaphGYmqOcfn8IGxOz-AEjHd-9d7vNyp-Da5tIMlHYzBRm9EpIjWlqXBy62V0mdc8DaazGUi6NvU2r-2_942JdFFOVNWijyAyLfngH9mIfXdWpiAf_gNmBrJfi89fERPKvWKW0lqNHQrxISh2Vbu6gqwkm6mk2BLznk-oyEEtNt3aNUrSuFRoo6QSTJj0gZ1ndx50fxO5BL1dA-vQIzgKRWJdjxjCQW-2Qqyg7RjugKv6AA5ldRm6bzS9w9yzftWFfBwOM3hPmnl1L20CADUZ1TEDQeWvOCyk7Q3zbkAPuX8-9mlv9ep1ki1W1mXl6bJxwaApWZbh4FZoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/89b613cca1.mp4?token=DF_3P7zdeaphGYmqOcfn8IGxOz-AEjHd-9d7vNyp-Da5tIMlHYzBRm9EpIjWlqXBy62V0mdc8DaazGUi6NvU2r-2_942JdFFOVNWijyAyLfngH9mIfXdWpiAf_gNmBrJfi89fERPKvWKW0lqNHQrxISh2Vbu6gqwkm6mk2BLznk-oyEEtNt3aNUrSuFRoo6QSTJj0gZ1ndx50fxO5BL1dA-vQIzgKRWJdjxjCQW-2Qqyg7RjugKv6AA5ldRm6bzS9w9yzftWFfBwOM3hPmnl1L20CADUZ1TEDQeWvOCyk7Q3zbkAPuX8-9mlv9ep1ki1W1mXl6bJxwaApWZbh4FZoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
همراهی‌رایان‌شرکی باکیلیان‌امباپه در پایان بازی با پاراگوئه: لازم باشه توی کثافت، شیرجه میزنیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/25021" target="_blank">📅 19:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25020">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnoFlivZpbiXr707fdE91E5mOi4Cewhzr9VC149zkLnS1BCs3z2qERmdWbyza_GFE3Cdq1fYfWIOAxHW7MCVHVRkTKVif9gAH23oZAhkXzrT_0iAtPmfVEE6-zgBwmBXHjoyOVvSa_T23nKqO_tZfrHVt_tP-DjVDtZs_tycZtOIrjOWSQx9K4D3kKxZKIJSXr_m7-BbD-psDZHWP8PsZnpXEYb00RFd8n_9so87eDhkMuMOf1_xIv3UV7jDabZe7j_TGYg7fq45Cg2mMkIqDKrNGfkQHpwTLac8v_jTWoIn_NKWePqk5JdTMWYLJygpEnqAQFInlpZrwOcpmXn58A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
تیری هانری اسطوره آرسنال:
کیلیان امباپه در سن30سالگی‌به‌رکورد 1000 گل زده خواهد رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/25020" target="_blank">📅 19:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25019">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9ftQgap2_Xnl4Z9KcdcCuv5jG-1oiLQ2X3Br3jzTZsXjjmvh1hsJSgez_NhANoOC8SN9UYBVrl3Nd981ZCDjzeFglVVHK-LUMpgIZVPochHMHUNgdjUADY_JCfhL-IGG9i1rMENeo3t4t0vsUFv7bbKboczpeaQv9Ros4ZmZDBPm6ZOGlkk9a6UsG8-snhRzMEmtLQm2zABA0ylskwY60OTJaBv4JKMi2_5sDdOG_iypeoFE05j-CZ9Z2SbHqq1HBYkkAqvNCfNgHiY5yTZ9AwhEvcsgWLjP6zEPC7Rnf8asmHMpF8D44b4VTVrouacAFeoGy5D1uvV08_1gggDfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
دیدار فوق‌العاده‌حساس‌وجذاب فرداشب دو تیم پرتغال
🆚
اسپانیا رو عادل در آپارات گزارش میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25019" target="_blank">📅 19:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25015">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgriYf3w5ucruJrt4XcsCM9_TDwa_04_4KmcoHf-EPl8IL4uqsHaa2YNTFMoVR4djGecVHoH8W0XgxpINtyMhG0xgCx5smyxCA9N2CIQModho-s7rxqMma8pDxmnQ56unHPmmPTREO63snDgavIYy0qPc7TvL2khDq_tXZSG-IRHW-Tyo_YLrR27B2U7gJDhYdPoiokMxK0MvGHdAeyctDK8ejY2oy_Hq33k3XOf5_cL3sq0OTRDgHRnK7ejsSM-lqXcQln980cyMSgq4qtMNsfYG9jx6CPe5BQV3VJX5F6omfuTM0xm8Teoih-ViMLUmpIT-wQhdgJA8BGgbVKjOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراگان اسکوچیچ: مدیریت‌ تیم پرسپولیس به شان‌وشخصیت بنده توهین‌کرد. تو عمرم ندیده بودم مدیران یک باشگاهی این‌چنینی با گزینه سرمربیگری خود برخورد‌کنند. اگر شرایط مهیا شود روزی دوباره بعنوان سرمربی یک باشگاه بزرگ به ایران برمیگردم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/persiana_Soccer/25015" target="_blank">📅 19:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25014">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AA7SMk0kGDs6Ize8N_UgZ9IE6iRRhVEyOOPAXJLsXlxO78qjMRHsuaysm3X0l2LPZJqwmVd0_vs-70xOweFzqYcNN8o0r1NOrYS0pBcgX8HwwYuLSSzJl6_HI5lu6V1iqB-qy7mfg_Ek6mA9y6H3xMRhi3KMRTDnBcPbuyQARGuMcM1LcmR1QhgWMxX7pSwGkIRCc1EEziI8H6UK69m37Ga5pDfqRuU0e0YtB0rEXAiEIOrKfk11HZQSwy9K3obUjQYqQl9ybgxQYT5_vuCCClRoHkJVpidAbiqGNHKOS0eaSl351LHV4-kXP3dN5ayR4jrKcZRBVOypQcB9yP9AVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Aparat Sport [3.6.2].apk</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/25014" target="_blank">📅 19:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25013">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmVW6lyllCU8QUL7WN7Jgy1MF_MCSzULKgzlfxk_u4Kvg2TV69Ane-UyG3rgO0o7nC5cA4N93uL5S06ts6h95O_vN4B5-MXkObehgmw9aJCeZ2WjtblpbT_-9EoIVaUToF7jAEKVWk-vTPbQejFDp3_obBzN0QGH3960Pso5mRbR2VRGEobpHEPQxzcjfoQnEuJ3ntQl_EQooiWhB7D0D36ngPPnRhmRzhDG7yMI29BHbPHwavLThkGRj8vfBpdlOFMdpZMAEIWb_BBBsRoD5ztNLoKPOuKpwTSBBH4wFLC3P90MFu0-ri9_30kvdu_zFaVsKAmEK5nK7IyKeaJE8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد.. مهدی تیکدری، مدافع راست 29 ساله فصل گذشته گل‌گهر سیرجان، با امضای قراردادی دو ساله رسما به باشگاه پرسپولیس تهران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25013" target="_blank">📅 18:44 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25012">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_t1iGsQSZZwt0pDxnunSnYpUwerK7haI_1nr4m4FglYMdC4Grr9WS1Lqalfu7XGric-WeQ3gnT6zdFoRJAFWeoNeeRRYLx_9Z5XeerhF5mRZgJqjKnrLelcbi8HRj5sAgE4QroMZlki_LFZJ0RmiQJx5KsNXZIPi404IXA22hqnrUkNsBP0lVAGHV_62tIgMhF_Tqd39V23flVM3VKQ3S_31vWMt1JWZfQdfh2c71HtUBOJjen0EYh5sfhoLE9nLI1rEH46siI8Ut-O8-XvfbKPQ8McUEU0fHNHYkFfk5hBWYIi4a6EbTOmul-agnNGivtanxcs0kBoMcFq8nN6dQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ مهدی تیکدری ستاره فصل قبل گل گهر سیرجان که دوبار تا آستانه عقد قرارداد با دو تیم سپاهان و استقلال پیش رفت درنهایت‌ ساعتی قبل با عقد قراردادی دو ساله رسما به پرسپولیس پیوست‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/25012" target="_blank">📅 18:21 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25011">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PfZi4TSQK6coGwetUN4UK0icUIz0z7rb0luxBP__3TprUhcxE4aP9vB5I4Gst7SJsdyTVz5mgM0JDpkC3APjgrHqPF0yhiezAWdg5yzPxk0AJ7gZPUHR0F5T_cLG6aF2YbfeNkYDHQea3gwe7I5qbYha__wRQxLsWj1mpq8iYpyCbEwA6SYBcAc8_-dJf9y973YGtR8mDUpKoggCvU9PL551z-eP9F4Oj8uMVb7QHKy9i3hxLxybZqzJo1S59OIGsj7cqHrliYzi05IJCl8QCM6_i6AoS64Db7Gp4Y8AKPitJUzPYStQ4V0pKOOz8pqPG2CYn54SZBKsX8O0155WkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌آلومینیوم رقم آخرفروش محمد خلیفه رو به باشگاه استقلال اعلام کرد: 60 میلیارد تومان. ایرالکو تخفیفی 10 میلیاردی به آبی‌ها داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25011" target="_blank">📅 18:17 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25010">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7Ig7z3MU3bqyv4U_Z9mK6ShyC61ke28VbOXNmdZsDTIdLvL76L2gvxW0KcOZP8mbL9LziN5Ww0lHhGoH6esfenuQtPEtpVauALIzEjVZOUmJ_lRGXFn6qtL1xTYuDJ7Ns9bzHCEu-DZ2jpmcUgtZD4tc2wLImd5LnTW3784qvWfJUMqbqihsUURAEvFZO2JDfT8sIbzFA2sbwbHXdp4t6BdoeQpf58vMr8v3KI6pvW0IGZA6osHHYxLDrpBWvplbjrHFMRwPXBwno5PmCLpwrk5VYxGd49S8YYVGFKschrUfJXKf6CqQIFqsCLo2CJhx2X5YfXv79OuR4pWp46ZwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
14 روز و 14بازی دیگه‌از جام‌جهانی باقی مونده بعداز اون‌باید 1440 روز برای دوره بعدی صبر کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.5K · <a href="https://t.me/persiana_Soccer/25010" target="_blank">📅 17:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25009">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=LoFeSjak-kdOPWxNghjYJcbe9VTS2dC12OqbXOt8MfIClOeeo6ZtHAWDIfeKI7ceu4S4vbJo25qB20FL-3ps7-LA3EZ3rSRPsHmEG8kldVZI3jKOkhMLabETNvXK7mL-61kH7Vs_-YVI9UbdukiDqBQtmXN_kaTHJTZrmXYL6Ns9O4CxEB2YwOFR7bgwlJUPhRZm-0wvFygCgXDPPXYXHPSzWIX2MZvyWH4cjmolwesrTWd7AlBA5UFGTVjKX0IVZzOkCgfb1AVor_Tg-Nc41bqkZrrP3VP2dChGAQjLW5mDz27CFyloF3VGcRJfF2Cz4IbBCcVe8vMogi4a7Y9Now" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b051966bf.mp4?token=LoFeSjak-kdOPWxNghjYJcbe9VTS2dC12OqbXOt8MfIClOeeo6ZtHAWDIfeKI7ceu4S4vbJo25qB20FL-3ps7-LA3EZ3rSRPsHmEG8kldVZI3jKOkhMLabETNvXK7mL-61kH7Vs_-YVI9UbdukiDqBQtmXN_kaTHJTZrmXYL6Ns9O4CxEB2YwOFR7bgwlJUPhRZm-0wvFygCgXDPPXYXHPSzWIX2MZvyWH4cjmolwesrTWd7AlBA5UFGTVjKX0IVZzOkCgfb1AVor_Tg-Nc41bqkZrrP3VP2dChGAQjLW5mDz27CFyloF3VGcRJfF2Cz4IbBCcVe8vMogi4a7Y9Now" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
ریمیکس امیرقلعه‌نویی هم بالاخره منتشر شد؛
دهنتون سرویس این چه سماییه درست میکنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/25009" target="_blank">📅 17:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25008">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8fTXZWCtvpXK_hIUNN1aTFKfsVHUVCM3FqcfGv6DBm9DqEKuDoeCH4zQUQnSJBSNmranTDO6xxwbS5uoMy7D_vCQNyKF7kYHYT3dBqP8QapLCU9Vj-NXLXS3oMUKZd77nuhYVr_vO6elPjasq65rxMM5lvPeJ8c8PknYiWutLnbfc9eCR0ulaCVbQKHH6_ljr0hTYsP9PxxdxUypCHvHofj5M_T9XGk05mM5POgUXqkATWh5A3RetY-7mSBbb7E48go0kr0ovUjHGUq3FkgnNbKv9bS1Sjrtwq_bwRc5_fh0XYBlipFnlSCWKRx235yJhO26XOCOXH0AFSO8J0zxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
سرمربی تیم‌های مدعی ایران در فصل جدید:
‼️
استقلال: سهراب بختیاری‌زاده، پرسپولیس: مهدی تارتار، تراکتور: محمد ربیعی، سپاهان: محرم نویدکیا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/25008" target="_blank">📅 17:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25007">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=TPcDWxv7LUiEaKzbcsB2tkPDoKdGHRbCpfVCTau0S9xFf6VUYAgzt2n_9QaCeojra_pIt2hf5ViGKofRP-L7b1jUbafZehtXgxEHTnIzYWoNoLf_KHt7aMLFsY-FLNWqPXJwImP2etfM18cuzM_pN_wfUijqjbPgfMyvdMORQdFeVEurO8NT-tuFLKYOZkwukDNC0bJQudhLfjbnojFpaTqavYVEQs73a-_zroW7Fsiv1uZR-Ymc8e-f3sEnPqkNkfmsHRiXl_Gi9tjM8q-4PIO8jd2adjoXM_ybHkcSi1voYx5rXPhh7r3zj1k0GDAWPygJk0Cj8sNiS-ZK2B9dtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eeaaa6b3cd.mp4?token=TPcDWxv7LUiEaKzbcsB2tkPDoKdGHRbCpfVCTau0S9xFf6VUYAgzt2n_9QaCeojra_pIt2hf5ViGKofRP-L7b1jUbafZehtXgxEHTnIzYWoNoLf_KHt7aMLFsY-FLNWqPXJwImP2etfM18cuzM_pN_wfUijqjbPgfMyvdMORQdFeVEurO8NT-tuFLKYOZkwukDNC0bJQudhLfjbnojFpaTqavYVEQs73a-_zroW7Fsiv1uZR-Ymc8e-f3sEnPqkNkfmsHRiXl_Gi9tjM8q-4PIO8jd2adjoXM_ybHkcSi1voYx5rXPhh7r3zj1k0GDAWPygJk0Cj8sNiS-ZK2B9dtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ویدیویی زیبا از تحلیل جذاب گل دیدنی لیونل مسی به کیپ ورد دریک‌شانردهم‌نهایی جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/25007" target="_blank">📅 16:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-25006">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0K2293JSwkKaFOAGnjcYOcWdvsnkfga3MkUvnonNoIGgY0VaJoK1W4lX8ueN12bOFpF6-YcpsDv1ADVHk-eQW-ZLDwwECJharBRZ9eH8FyuQFQpEpDNrgB5znkKSZM9_8K3hqMOT8WqyzW3AIzs_i8fQacsAQqIOeealgQaRkkTr3OnnhQvQ9BeAaTu1pHIxxeOFHkD5-a4NlW792E1TxpkW92P6sCY1-DUbPoixb2I6X_oKUGdjTWCrQ_-OLGgpAmLT3AmNmqJl98T5BF814DmtvQ6OCsk9KVunOCLI37H_3ZLt52P9EcUAMTerrPdQmSzrJq5Hl1nflujTKnjPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
باشگاه استقلال و تراکتورتبریز امروز صبح با ارسال نامه‌ای به فدراسیون فوتبال خواستار افزایش سهمیه خارجی تیم‌ها از عدد چهار به شش شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.7K · <a href="https://t.me/persiana_Soccer/25006" target="_blank">📅 16:34 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
