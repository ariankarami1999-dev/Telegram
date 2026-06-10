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
<img src="https://cdn4.telesco.pe/file/PGqyEqUtd610dwLFnQxhjIAX8EZDXSSnPsmic5sQp4kiXpSxBFjnoLFjOZna8MCyfIlIijoEg8AMlvqfBAGLBwD-WedCcKluuXbRpS1-IpWmAD04ONSs3wfoKYwLntoqxOqOg1rGbMZj6FqWoppj-w7VryBayZSoSN9NV4YtYbmtCJnbweab0h6ZVDmf-ZTnCKzciRV5cn9xpa4GtaXlMWNP1HWjwhdxXMna5gjLinBLcHQR0Q4RHHWXzgSmD-wtBfTzesCGUeLZDKb8olSrl0iX4sRVdypmLYKgxsrFji2MOw4b9DXMDRyvnbnG622dV3PtoQVyaTbhdgfkWILkJg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 258K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 06:07:11</div>
<hr>

<div class="tg-post" id="msg-78059">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/78065d6e7d.mp4?token=TE3-8eTh3hyqE1wyo4UkoYAu5x4_X28Giwn_H2PwPdWlH3AMlkR689BPoMhZxJClGYiWknIylz2qhU4_39soA3gJBJcC0buaIn9udibOMUm9wy0ovEmOdbd00zEDdY88H6NndCxpHqV5cnxaqjj0-jGN58PITnrM9xH9OPyVdY_vcNaUDAMGFkVTQK1gXfXeODyrRhHKapGE3aee3b6ePQyNPpy0CCfF8fspGZtpTxqF8AN0s59HbTTJfpj6mVatctyx1ROOh8zkNqcrPvGKH6r0zArLEYFatFuLeq3IluBdV-PQjDZnJi7jwhalqXEcOqdKPGFGuqeNyb-CvI7Plg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/78065d6e7d.mp4?token=TE3-8eTh3hyqE1wyo4UkoYAu5x4_X28Giwn_H2PwPdWlH3AMlkR689BPoMhZxJClGYiWknIylz2qhU4_39soA3gJBJcC0buaIn9udibOMUm9wy0ovEmOdbd00zEDdY88H6NndCxpHqV5cnxaqjj0-jGN58PITnrM9xH9OPyVdY_vcNaUDAMGFkVTQK1gXfXeODyrRhHKapGE3aee3b6ePQyNPpy0CCfF8fspGZtpTxqF8AN0s59HbTTJfpj6mVatctyx1ROOh8zkNqcrPvGKH6r0zArLEYFatFuLeq3IluBdV-PQjDZnJi7jwhalqXEcOqdKPGFGuqeNyb-CvI7Plg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  الصواريخ الإيرانية تدك الاسطول الخامس الأمريكي في البحرين</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/78059" target="_blank">📅 05:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78058">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الموجة الصاروخية التي دكت دويلة الكويت</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/naya_foriraq/78058" target="_blank">📅 05:50 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78057">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/78057" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔴
الفرار الفرار..</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/naya_foriraq/78057" target="_blank">📅 05:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78056">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D2HbC5oXyiV0vQ-JGh3fnHH7CYIc3QCj90Yk1UeQ3lflWTW2Eq4ludk6k0dha24unf9ANLWyko9qPoHFteDUkBjqzZLtNySix8dYMEaQXtUbcdnd5RqbxtlMxsDcHu0GkLEVR7mUNH3N93wEvzABqXM_wDcKMsIIjdZExfMFOezCQ2SmQVt3JYDg6fEXNUNFgGgZ_IX_lgMqeSDMUCQ8ZGyawIMXw7h8jO6sBeeX8-IGMU-PkoPdtGpTae6udH0ksT2Ccl4f3EZtekElvwCfWWMeUnTfVIG0BrsqgKQfwJ5n36LPIqARLT5EGg-czu7LKCa-YnP85EES3o716wkyvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/naya_foriraq/78056" target="_blank">📅 05:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78055">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ايران احد دول القوى العظمى حاليا سوف ترد على امريكا اقوى دولة بالعالم وتهين امريكا مجددا كما اهانت وفرضت معادلة بيروت اسرائيل   وسوف نرى من لا يرحم</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/78055" target="_blank">📅 05:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78054">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/naya_foriraq/78054" target="_blank">📅 05:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78053">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات في الكويت</div>
<div class="tg-footer">👁️ 5.71K · <a href="https://t.me/naya_foriraq/78053" target="_blank">📅 05:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78052">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb26d0c0e4.mp4?token=gZRpzJ1EVCZQxWFOV2FQvCV7Pcx6HNKpZ3Vi4mUvbV-YkcLXqmGDiRP7scCO17RQEA-Vp5WFS7_eK3AdSq-mTsagNm_aP4T9kQkTYfMouVxq9W1FXku9foEeSLskCMqx4ox_veajfRrsrpMKQbYQvVo38krjwdN6O-agsv_bAC3EtFCJ6UNO4wtPHNDx993Jt3aDQ7cql2ylr2n7vgy8v8oCRV8anFRqJlC6syIJjObwGbqm2kKEZVJ2_cF3-TaIws7NxehR5DZ3BLj_T3182oLFzySVBdn9Mm9Ie4pTobIuU7Tau-7-Esjnv73PpN_fCb54-w4r2GaPzC38MIhsTQqWUbp_5-KiQ9krjgJYIG8yRyooniMZkq3d2VSPHinQ8lQ8Dhm2jdo9rymPvHclZhvVDluFUtvBxpTNp6S9fpUoERKg068YRoIbB1agdpyY_moDk8V7nSdeBrQc_bYoiSe2KiQ7bs9KWxkWRsaBzEh4_G0RpmqY2DDW7o43E5Y1zBtykS2jnqcB1VAaSSOvgDBa82g1PBiQh5YB-HrQdOigCRy1ud3sswFdc4HQXjvFwX7I3aJ2r_kCdWNIVuoza8_0XZbHXpTM29muvjg8KibMjraiHMr9N6sAk-iMTx5WgKzS_O8fr2tFezD4CUSfCQV0LP58AgmZ38v6sqJo7xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb26d0c0e4.mp4?token=gZRpzJ1EVCZQxWFOV2FQvCV7Pcx6HNKpZ3Vi4mUvbV-YkcLXqmGDiRP7scCO17RQEA-Vp5WFS7_eK3AdSq-mTsagNm_aP4T9kQkTYfMouVxq9W1FXku9foEeSLskCMqx4ox_veajfRrsrpMKQbYQvVo38krjwdN6O-agsv_bAC3EtFCJ6UNO4wtPHNDx993Jt3aDQ7cql2ylr2n7vgy8v8oCRV8anFRqJlC6syIJjObwGbqm2kKEZVJ2_cF3-TaIws7NxehR5DZ3BLj_T3182oLFzySVBdn9Mm9Ie4pTobIuU7Tau-7-Esjnv73PpN_fCb54-w4r2GaPzC38MIhsTQqWUbp_5-KiQ9krjgJYIG8yRyooniMZkq3d2VSPHinQ8lQ8Dhm2jdo9rymPvHclZhvVDluFUtvBxpTNp6S9fpUoERKg068YRoIbB1agdpyY_moDk8V7nSdeBrQc_bYoiSe2KiQ7bs9KWxkWRsaBzEh4_G0RpmqY2DDW7o43E5Y1zBtykS2jnqcB1VAaSSOvgDBa82g1PBiQh5YB-HrQdOigCRy1ud3sswFdc4HQXjvFwX7I3aJ2r_kCdWNIVuoza8_0XZbHXpTM29muvjg8KibMjraiHMr9N6sAk-iMTx5WgKzS_O8fr2tFezD4CUSfCQV0LP58AgmZ38v6sqJo7xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي العنيف الذي استهدف قاعدة موفق السلطي الجوية الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/78052" target="_blank">📅 05:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78051">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba8298737b.mp4?token=OVNHQU-J4dZn63_TAbiEzmMEclhReC8MTKp9OnH4V6JBlsiaa-Zhxcu79gloIo0sJCWngVXOfjNJ0Blo226IPXnxfjqaSO-CLxXTTMQgzvyds3Jq9VL70pYV8KlTWo54ydYooAE-IiiC2Jd-nhlp8HRX8QVbHdJlGJ-VkjA7dGnyBga4dcXK21mxWHhJVLet3Sx153TXaNP9_oqrJ3ztXGfKuqTkOfvpWZJa_TPcywmh2g-r9HN8EKZLXW04cMYmV_VUmhGjaF9u16RvbeuAaMYEnJF7g6ejoOeM3ktfWRw9StFAGxcki6tLWNmAC7gdW3qU_6S0t5w1rXW4nKlqBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba8298737b.mp4?token=OVNHQU-J4dZn63_TAbiEzmMEclhReC8MTKp9OnH4V6JBlsiaa-Zhxcu79gloIo0sJCWngVXOfjNJ0Blo226IPXnxfjqaSO-CLxXTTMQgzvyds3Jq9VL70pYV8KlTWo54ydYooAE-IiiC2Jd-nhlp8HRX8QVbHdJlGJ-VkjA7dGnyBga4dcXK21mxWHhJVLet3Sx153TXaNP9_oqrJ3ztXGfKuqTkOfvpWZJa_TPcywmh2g-r9HN8EKZLXW04cMYmV_VUmhGjaF9u16RvbeuAaMYEnJF7g6ejoOeM3ktfWRw9StFAGxcki6tLWNmAC7gdW3qU_6S0t5w1rXW4nKlqBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">منظومة الباتريوت الأمريكية تفشل في صد الصواريخ الإيرانية التي دكت قاعدة موفق السلطي في الأردن</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/78051" target="_blank">📅 05:38 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78050">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/15dc0901a7.mp4?token=MCqKzmr_CzKhNmyoTXZZBtReMmngUQggH47ySXFCdPUTZUSJGa_el7OnQsFDfdpD_BCVgRqX90QbEGOxy7ZobDtUJTSVQ5q0apga9gpyNjxMai0jGNMJ4hjQNWwkJP0rvMl7dLP8UKkREAwn5L_edtvQZQPRDfS5o9VdaSRNQIUJbZ4X0CAO3Bn7r3IXqcYtocrNoKFQdssYwwrpcQS5TZfVZuTOzpO-iE6H2UIY852ICGFHfBPniq8PkHqIeVLdyLxjU-zS4LDqZj7mfB1fD4V3m5hpP66MzaaiDQy1d8jl9AuqTdVwZWnKKWPiPkrJGkHuPxRK9cFwtvJzC7-uJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/15dc0901a7.mp4?token=MCqKzmr_CzKhNmyoTXZZBtReMmngUQggH47ySXFCdPUTZUSJGa_el7OnQsFDfdpD_BCVgRqX90QbEGOxy7ZobDtUJTSVQ5q0apga9gpyNjxMai0jGNMJ4hjQNWwkJP0rvMl7dLP8UKkREAwn5L_edtvQZQPRDfS5o9VdaSRNQIUJbZ4X0CAO3Bn7r3IXqcYtocrNoKFQdssYwwrpcQS5TZfVZuTOzpO-iE6H2UIY852ICGFHfBPniq8PkHqIeVLdyLxjU-zS4LDqZj7mfB1fD4V3m5hpP66MzaaiDQy1d8jl9AuqTdVwZWnKKWPiPkrJGkHuPxRK9cFwtvJzC7-uJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الأردن بعد الهجوم الصاروخي على قاعدة موفق السلطي الجوية ومحاولات الاعتراض الأمريكية الفاشلة</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/78050" target="_blank">📅 05:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78049">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">من الهجوم الذي دك قاعدة موفق السلطي الامريكية في الاردن</div>
<div class="tg-footer">👁️ 6.7K · <a href="https://t.me/naya_foriraq/78049" target="_blank">📅 05:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78048">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/949ed3e240.mp4?token=JH_8FyJqWw1xBCvKzKkTLjXk3092546UtmcEyLKPwZZHqgcSRwhxvmYSb_Xax8VwxoH-p-rOse72DQkpINXFC3muZHi5XlS9U8QoLy4kUxBBOiKIYHGyoHtVSQHMTwEHCwAlBSs1_khHYrNIl8AL2TuHsR7VcTBwxmCbS2kC4OICLVsXCTUyAPl13Ikt1jbez4dybvUIFn69160jLzkOxGqPhI3a8elMHStKLIXI_UFH5KHAYfNK-rDey479QD9XJKp9vm8mnYm9oGhvPdd9Ohp2L1aY8RRN0GOmhD2G0NfTQzKelnW203JEpgknhUgffTMZAog8GGtP42l9y5hryEczd_HYaVvUp13IL-s61Fp00a5cbHQ1_Ct-K8rzorYdy4ggwPv3PyxZAx5bHbTf17LLuOMaKNEhknQ2a3x-qfhLU9VQS_Y9i1YJYDqAANS_9SeBX1W16WW0ARA7aozBC8xFurZJRkbxOeFUS3WibYGQpDNFR1mC583uj7lTA1dxciBKcjtv47wvxLje1awTy4PYeeMGpMYZ7hEcaNvNd3eMoRQZwXiDzW6nVQGDmWs-IJKseCrtFqfL9eiG0xC8BuhRHPvmbLG83j4xEgxJrtMB0HHG7Iu-mPx_BDJRY6JKM19VgchK_pccCKTzHXS_mNM7ydmu0I8ssUJHsdFttRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/949ed3e240.mp4?token=JH_8FyJqWw1xBCvKzKkTLjXk3092546UtmcEyLKPwZZHqgcSRwhxvmYSb_Xax8VwxoH-p-rOse72DQkpINXFC3muZHi5XlS9U8QoLy4kUxBBOiKIYHGyoHtVSQHMTwEHCwAlBSs1_khHYrNIl8AL2TuHsR7VcTBwxmCbS2kC4OICLVsXCTUyAPl13Ikt1jbez4dybvUIFn69160jLzkOxGqPhI3a8elMHStKLIXI_UFH5KHAYfNK-rDey479QD9XJKp9vm8mnYm9oGhvPdd9Ohp2L1aY8RRN0GOmhD2G0NfTQzKelnW203JEpgknhUgffTMZAog8GGtP42l9y5hryEczd_HYaVvUp13IL-s61Fp00a5cbHQ1_Ct-K8rzorYdy4ggwPv3PyxZAx5bHbTf17LLuOMaKNEhknQ2a3x-qfhLU9VQS_Y9i1YJYDqAANS_9SeBX1W16WW0ARA7aozBC8xFurZJRkbxOeFUS3WibYGQpDNFR1mC583uj7lTA1dxciBKcjtv47wvxLje1awTy4PYeeMGpMYZ7hEcaNvNd3eMoRQZwXiDzW6nVQGDmWs-IJKseCrtFqfL9eiG0xC8BuhRHPvmbLG83j4xEgxJrtMB0HHG7Iu-mPx_BDJRY6JKM19VgchK_pccCKTzHXS_mNM7ydmu0I8ssUJHsdFttRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تنقض على قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/78048" target="_blank">📅 05:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78047">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">الصواريخ الإيرانية تنقض على قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 7.03K · <a href="https://t.me/naya_foriraq/78047" target="_blank">📅 05:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78046">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cfbe5f47d8.mp4?token=YS27DrKbW0F0fOJusjlJxzfrzs2weOliHswvUpCcWI576lJh9nTrFYC38h2Exkc5_30GIcojtuxinNSwcMG3g1J-g11fti3zgS0LCZ0UC7UWtbRn6oL5s2rOzmx2b8uWB2JwyoR5F5B0ZGfVvzTNqm_HqTKWyjLGsKVgf1UIv499fO8rS5HDzt3nqzyctIWbDHdDASFKiXnjAFaJ6l4-8ionWZatnTRtJdECL4rYommtQtu2mkS46SuiVNoR9_kvwwBmUGJQyWJrLJeJdLrF_8ADKK-Nl6Wq1yaWuCw57RKpkkfwjSG3k5rxHlVTHuh68iKhrTxEZL1vSiYXx71XHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cfbe5f47d8.mp4?token=YS27DrKbW0F0fOJusjlJxzfrzs2weOliHswvUpCcWI576lJh9nTrFYC38h2Exkc5_30GIcojtuxinNSwcMG3g1J-g11fti3zgS0LCZ0UC7UWtbRn6oL5s2rOzmx2b8uWB2JwyoR5F5B0ZGfVvzTNqm_HqTKWyjLGsKVgf1UIv499fO8rS5HDzt3nqzyctIWbDHdDASFKiXnjAFaJ6l4-8ionWZatnTRtJdECL4rYommtQtu2mkS46SuiVNoR9_kvwwBmUGJQyWJrLJeJdLrF_8ADKK-Nl6Wq1yaWuCw57RKpkkfwjSG3k5rxHlVTHuh68iKhrTxEZL1vSiYXx71XHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">موجة صاروخية كبيرة تدك القاعدة الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 7.69K · <a href="https://t.me/naya_foriraq/78046" target="_blank">📅 05:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78045">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2823842b74.mp4?token=sOFUS4WrdUFQD1hDaLRvjIppw9TZqCzDUNKKu_cpVAHfYTaCM07jFxVaWrgKgdfm2TQ8YWdvvz-Z-b10FSuz7k4NCGGUHa73c-wbEwuOh75hsD6_i2fZEPIbfJ1t01kNSbkv-0xNoEo2ho_GYR5NWrFnhixvEEMhFYxOenxlq7ch9cEDTjFXRqJxzTTbu1ouEIjr3sFyG4tnFSFSckvIQNZP_pXCfAxITDm-WHMRgkKdd-g1HiAuisoO0wv9Zp-G8XjjGKOyoAHP63s7pXIkJ-RqbeK4Fhs93fcUoLl8W6_EipcIIfl264IMFNngvoIwfSzr7M-KqTnX20CnwBKw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2823842b74.mp4?token=sOFUS4WrdUFQD1hDaLRvjIppw9TZqCzDUNKKu_cpVAHfYTaCM07jFxVaWrgKgdfm2TQ8YWdvvz-Z-b10FSuz7k4NCGGUHa73c-wbEwuOh75hsD6_i2fZEPIbfJ1t01kNSbkv-0xNoEo2ho_GYR5NWrFnhixvEEMhFYxOenxlq7ch9cEDTjFXRqJxzTTbu1ouEIjr3sFyG4tnFSFSckvIQNZP_pXCfAxITDm-WHMRgkKdd-g1HiAuisoO0wv9Zp-G8XjjGKOyoAHP63s7pXIkJ-RqbeK4Fhs93fcUoLl8W6_EipcIIfl264IMFNngvoIwfSzr7M-KqTnX20CnwBKw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالتزامن مع الهجوم على القواعد الأمريكية.. طيران مروحي في سماء أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/78045" target="_blank">📅 05:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78044">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">دك القاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/78044" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78043">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac9f250df5.mp4?token=tZuDGeAIZOj6nRmsFVzSVaycgenyO1kSoQxFPH6HqSQbDoIrpooYuMy0N4Q45SBa6SlVcYbLERl7grJAAMLq-hzUCBwej0yQWIm5AAvrsAh7Fux7PC7x4bacX3lTVzwUL52z4iZZPT-K1n9JRpG6NGTZH3SfR3slfT6X4w6c-5DCmgW9V8KoJqG31JvspnEqPR12FrL7nGTICC6V1D8MBJP9C7XK4cPwdhO5v_X-oLVipiLIWfzyRNk3rzJgjbQnwTWo_Rf_Qa7EmeKAuQm9jQSeNDrgTLZUv5Da4567dd0FJDbi2P7JU0DcDKrIuyETUA-H75aCFmxyj2d9tFfmiVda65EMvEA7jylX-Ou9khCPfPyUk_xIYxNgVBqkj6ucG9aLBsrV-XO9A3kg7_LMFgYMVJuF08yI_dtfRk53oud9R9AotQxLeeGBo0ik7ptvpXLBoEW_mhj-AdbEwNPQ4f_NBDiNgixaz8cRORKRgtMJT5zqF2Po4bI-FltwdfRpiq5J4zgANzSPNR8A9s1zZX2iJtswhJYiLh73Ady62k85LwRvDvqyYikq8dAb0wdO2Zu93ZbTn9qDF3WcAO3xX0RH3j3q-4AnqfsdNcP_A5Gq1iIixvnNOA22eMnnqgY8QpG7ywGI2vvB6nM-acyZuz8ONZl2fJ-LrZD3kpMVDnk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac9f250df5.mp4?token=tZuDGeAIZOj6nRmsFVzSVaycgenyO1kSoQxFPH6HqSQbDoIrpooYuMy0N4Q45SBa6SlVcYbLERl7grJAAMLq-hzUCBwej0yQWIm5AAvrsAh7Fux7PC7x4bacX3lTVzwUL52z4iZZPT-K1n9JRpG6NGTZH3SfR3slfT6X4w6c-5DCmgW9V8KoJqG31JvspnEqPR12FrL7nGTICC6V1D8MBJP9C7XK4cPwdhO5v_X-oLVipiLIWfzyRNk3rzJgjbQnwTWo_Rf_Qa7EmeKAuQm9jQSeNDrgTLZUv5Da4567dd0FJDbi2P7JU0DcDKrIuyETUA-H75aCFmxyj2d9tFfmiVda65EMvEA7jylX-Ou9khCPfPyUk_xIYxNgVBqkj6ucG9aLBsrV-XO9A3kg7_LMFgYMVJuF08yI_dtfRk53oud9R9AotQxLeeGBo0ik7ptvpXLBoEW_mhj-AdbEwNPQ4f_NBDiNgixaz8cRORKRgtMJT5zqF2Po4bI-FltwdfRpiq5J4zgANzSPNR8A9s1zZX2iJtswhJYiLh73Ady62k85LwRvDvqyYikq8dAb0wdO2Zu93ZbTn9qDF3WcAO3xX0RH3j3q-4AnqfsdNcP_A5Gq1iIixvnNOA22eMnnqgY8QpG7ywGI2vvB6nM-acyZuz8ONZl2fJ-LrZD3kpMVDnk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دك القاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/78043" target="_blank">📅 05:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78042">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 7.94K · <a href="https://t.me/naya_foriraq/78042" target="_blank">📅 05:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78041">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 7.95K · <a href="https://t.me/naya_foriraq/78041" target="_blank">📅 05:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78040">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/526ac24d33.mp4?token=cfvydZKFC5sVHDdy9-tgorE62EIL1_woJFWroBS65z8E4mtGZb305qsEkMzat3Uuc3Xg8sAkgllxONgf9pAHOUhQVfeSPcUyA8Xyi-KsldenuI9K3dfYbTemaocoEUtGRs5YqqaK454LHuxL6k-xRQz5Hagj5QURleR8GfytueNCij3zlVlvwZLVKYqY8JBVXH8LDVJXlYodH7IO215MI2K2nNkYs_qkX16DPnTTOMDoOrL_cjhPhb420IYfQbf26ogRGupa1MFt9ob0ftENm8olLp5uazJjKKXy9lPeZ9O3VKG4fNkO9La64Te56eIzFdwNKbjIKXTEV48hlxAD2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/526ac24d33.mp4?token=cfvydZKFC5sVHDdy9-tgorE62EIL1_woJFWroBS65z8E4mtGZb305qsEkMzat3Uuc3Xg8sAkgllxONgf9pAHOUhQVfeSPcUyA8Xyi-KsldenuI9K3dfYbTemaocoEUtGRs5YqqaK454LHuxL6k-xRQz5Hagj5QURleR8GfytueNCij3zlVlvwZLVKYqY8JBVXH8LDVJXlYodH7IO215MI2K2nNkYs_qkX16DPnTTOMDoOrL_cjhPhb420IYfQbf26ogRGupa1MFt9ob0ftENm8olLp5uazJjKKXy9lPeZ9O3VKG4fNkO9La64Te56eIzFdwNKbjIKXTEV48hlxAD2Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر  توثيق يظهر لحظة اصابة صاروخ إيراني في دويلة البحرين</div>
<div class="tg-footer">👁️ 8.61K · <a href="https://t.me/naya_foriraq/78040" target="_blank">📅 05:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78039">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJ4ND5NwhBY0RrsinvcmzXpSEnaSCvo1yYK6JqqyEuxrF4e1XlpNBYQt2VjOl0MC4SteNazYLK8mJoR9lKtj_JvXwPZRLlDTnb3wxhfsfCvgZ_9fnnVFb3lnCeVCufiZhztDIzSiWE5L04UIy2BI1g_HAhDar8xonpF2T3Q41aeB71GNoIs2dV1nM2AcQaS6CL9lQIkH8XnJbUIxKhWa16DKyMN91uafx5CXDIzX34p6ssZmM9Sz1Qvx0t1klvm8Q5pmCDqFCdubBswLHePaHRD-AOU-5sttNNUt8VrbV-SJ7rsQ1927643ipjBzMcr7DakOt5UNEqpj5GkP_-9NwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر  توثيق يظهر لحظة اصابة صاروخ إيراني في دويلة البحرين</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/naya_foriraq/78039" target="_blank">📅 05:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78038">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3909c382.mp4?token=VRcUiP5p4AmKJPE0G5D2I56gLt6L9oBRbsQFe8-bDiZFDMh5Bxv0lty3e63wysunh6UgBjPF0wrqf4YHvLYXBUfgCIEM8H7L4q-LxHOQEsPy_icTR8jSxmKZlr8WfxIq-7qMh1dfPY3rEPX0jyLdFyNFYQotmylqtfzS2pOmiwd_dYRNUlznCMWtrdBkNBxPk8__LrTTjHJ79LbzMSQkaPNWunJGdwjzB7NqQolMIV6uItcN4r6kbqxSTxhtOs6ER_7Rp3jE-Ijnmr9fpuCHpR4es2kMN0shR28_VB-Yubym_PN7iFoppANsI8oWy4Qiks4Xrx65PaIqRMU22-7WGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3909c382.mp4?token=VRcUiP5p4AmKJPE0G5D2I56gLt6L9oBRbsQFe8-bDiZFDMh5Bxv0lty3e63wysunh6UgBjPF0wrqf4YHvLYXBUfgCIEM8H7L4q-LxHOQEsPy_icTR8jSxmKZlr8WfxIq-7qMh1dfPY3rEPX0jyLdFyNFYQotmylqtfzS2pOmiwd_dYRNUlznCMWtrdBkNBxPk8__LrTTjHJ79LbzMSQkaPNWunJGdwjzB7NqQolMIV6uItcN4r6kbqxSTxhtOs6ER_7Rp3jE-Ijnmr9fpuCHpR4es2kMN0shR28_VB-Yubym_PN7iFoppANsI8oWy4Qiks4Xrx65PaIqRMU22-7WGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله أكبر
توثيق يظهر لحظة اصابة صاروخ إيراني في دويلة البحرين</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/naya_foriraq/78038" target="_blank">📅 05:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78034">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZKJiTKux5whC3J_6ENUe9O4E2kKIJxGCtc4OWWRvDm0-XSutVykjHF6OI0YsNdOcSvaTnCz_hMYY_BdwA6VBkCLoHsl5nnTmRcyWoLEOo7r1x9lKc74q9tIrj2TLXqWQJj-ywdsBWdhI7S8w5fLJmHO9WRrPzwxTwDrYmnnFibgTDXD2HfPXdMZk9HvHuWSNb04r1uyJfbR1h6WR1xUwZSKsv4Wq8ALyMB20R2E8rC9btBah1umuwf4SBkoFuzmRQsD5QRFO7etek8FCmKJvjjkxvyzLjbPffiLHMPZF8j8b9_4SI-L7st2eiBM9b_HdyIhr4gmfUruwFPjtupQuoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J0zaWfJOzTe-V12f_pXaxX6WqYORnD9QBM7BdURXfpr0ran4GmIKgDSDMUuQtXdyATPaqnayTHFUjP5EMKTCsKDs5uBz1gQwSQzPCN45WQwjPCFjrsrPaJmf-3blEkRFWZYsguUNEWrh9xZXFaFmunhyJftUuzZjfbnE-u75c2WpI9yZ5MJhh7hKRSWUpOefQP8IQQl6SIMW5UnrBXkg8CBXj-8BnafJZcb562kS2qUqPgfzbAInqolQkYnnU3NNM-OpIwpcpLSAOrVZ-Qzs_uHgeA1kPOvy7OfyXA-VHZ2QsoVDIhM0CLKWyf1ITNz7yhCZAMFVhfrVjMBoFcf7dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">انفجارات في سماء البحرين</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/naya_foriraq/78034" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78033">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hWSI5dOluxi7XaMPvlxim7NfcNlyWDW8NZhW4gd6-AGFESQXMX4gBFVw1UPQgiezXhKXvTAgMYqOXdEdvtUPQVa-FWN9R2IaygAV3X2ec2XWDfKCkNF_mkdOY5lZEKYwR3pwmoF6SHgUcebiApa_hacK5KtVRb3YBzW_vQyZrg9uLJnXmuB9Omithn8ToaKe-mfV1LL1tLwDGuPGZhJo0oTmji_J7J1ztJuIEIB1rhQ-zfgW9bhJaZOaGVvCcnfp2ZENdtESlGt3Fx5y-2B7sk_huOgO7_SFUzlz5Y1zB4QcVIOKnjEfSMUckz3M7o00si_tNEd-_vq9R4Pfo4J19Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/naya_foriraq/78033" target="_blank">📅 05:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78032">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/78032" target="_blank">📅 04:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78030">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇺🇸
الجيش الأمريكي:
نفّذت قوات القيادة المركزية الأمريكية (سنتكوم) ضربات دفاعية ضد إيران في التاسع من يونيو/حزيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي في اليوم السابق. وقصفت قوات سنتكوم مواقع الدفاع الجوي الإيراني، ومحطات التحكم الأرضية، ومواقع رادارات المراقبة قرب مضيق هرمز، باستخدام ذخائر دقيقة من طائرات مقاتلة تابعة لسلاح الجو والبحرية الأمريكية. وجاءت هذه العملية ردًا متناسبًا على الهجمات الأخيرة التي استهدفت القوات الأمريكية والسفن التجارية الدولية العابرة للمياه الإقليمية. وتؤكد القوات الأمريكية يقظة واستعدادها للدفاع ضد أي عدوان إيراني غير مبرر.</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/78030" target="_blank">📅 04:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78029">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">استهداف مسيرة معادية في سماء مدينة جم بمحافظة بوشهر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/78029" target="_blank">📅 04:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78028">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇷
القيادة المركزية لخاتم الأنبياء: ردًا على عدوان الجيش الأمريكي الإرهابي في مناطق جنوب البلاد بذريعة إسقاط مروحيته، استُهدفت بعض القواعد الأمريكية في المنطقة بهجوم قوي شنّه الجيش الباسل للجمهورية الإسلامية وقوات الحرس الثوري الإسلامي. على الجيش الأمريكي المجرم…</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/78028" target="_blank">📅 04:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78027">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
القيادة المركزية لخاتم الأنبياء:
ردًا على عدوان الجيش الأمريكي الإرهابي في مناطق جنوب البلاد بذريعة إسقاط مروحيته، استُهدفت بعض القواعد الأمريكية في المنطقة بهجوم قوي شنّه الجيش الباسل للجمهورية الإسلامية وقوات الحرس الثوري الإسلامي. على الجيش الأمريكي المجرم أن يعلم أنه إذا كرّر عدوانه على الجمهورية الإسلامية الإيرانية، فسيتم شنّ هجمات أشدّ وأوسع نطاقًا على مجموعة الأهداف المحددة في المنطقة.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/78027" target="_blank">📅 04:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78026">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">دوي إنفجار في مدينة الأهواز مركز محافظة خوزستان الإيرانية.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/78026" target="_blank">📅 04:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78025">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1a62fc64e5.mp4?token=WqDjZdpfj2Dj1KkoOwDtXojgIi6iCbENMi5cJYHQjxrP960LfejbzFVeeJrxayY5NbXbV-Cyr3dqUJt5I9q9z-Axih3EblTcoKxfDT7gBl0M2nWolp9rG-vw6bdBmE4YzaCq8pOb60JdnUseaMvSJac4BASbzsq906pM9g38rJBEmDbgox4QkN1hKnfri45sQmdz177I7N94xVKTrlsdxtn8eCE6ASgRk1mTYPAH9lf8AGUYgkFgB-Y7xZ35dr0BnLw450QR7bVk3tjv7a66ftoyawXNAWzG8kBhMHPW0dRIwmcZPQxWTBnCWIJw-kxJ34bFG5C7RKKU3E-a4YjPtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1a62fc64e5.mp4?token=WqDjZdpfj2Dj1KkoOwDtXojgIi6iCbENMi5cJYHQjxrP960LfejbzFVeeJrxayY5NbXbV-Cyr3dqUJt5I9q9z-Axih3EblTcoKxfDT7gBl0M2nWolp9rG-vw6bdBmE4YzaCq8pOb60JdnUseaMvSJac4BASbzsq906pM9g38rJBEmDbgox4QkN1hKnfri45sQmdz177I7N94xVKTrlsdxtn8eCE6ASgRk1mTYPAH9lf8AGUYgkFgB-Y7xZ35dr0BnLw450QR7bVk3tjv7a66ftoyawXNAWzG8kBhMHPW0dRIwmcZPQxWTBnCWIJw-kxJ34bFG5C7RKKU3E-a4YjPtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الدفاعات الجوية الإيرانية البطلة تستهدف مسيرة أمريكية في مدينة جم بمحافظة بوشهر</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/78025" target="_blank">📅 04:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78024">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تفعيل الدفاعات الجوية في بندرعباس وقشم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/78024" target="_blank">📅 03:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78023">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=hvydm-Z6ioO8yKGNo5R7rl7a357laAo02pzPWYKKgkkTtvDFZTA7hSenXeTh-uIk4kGkjc1ec_FefpX3uo0jkq3kCuDoEuIw-fyeFQUCTwlpIgX7PJ3nAu9dPaxOcQVXfN0QAKXTtSakCoUgo6lYbjirTMYn4iK71Sf924A2DNRYEH_F6yHkDXbjXCzJS-mtL5Hj6x460p0V6BlT02GosShCvRZ2qUCfW_nFhRoi-uIKRknraqDYyMd4hlrElF6ycDxDHbSEeeFEviKgZS_ES6yek19yPmtISbcQazm3PHmsJ28oGNG-nOOZzk7VIqcGe__Ax3IA9xhzTVJwdwjlKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6cfd4aa891.mp4?token=hvydm-Z6ioO8yKGNo5R7rl7a357laAo02pzPWYKKgkkTtvDFZTA7hSenXeTh-uIk4kGkjc1ec_FefpX3uo0jkq3kCuDoEuIw-fyeFQUCTwlpIgX7PJ3nAu9dPaxOcQVXfN0QAKXTtSakCoUgo6lYbjirTMYn4iK71Sf924A2DNRYEH_F6yHkDXbjXCzJS-mtL5Hj6x460p0V6BlT02GosShCvRZ2qUCfW_nFhRoi-uIKRknraqDYyMd4hlrElF6ycDxDHbSEeeFEviKgZS_ES6yek19yPmtISbcQazm3PHmsJ28oGNG-nOOZzk7VIqcGe__Ax3IA9xhzTVJwdwjlKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف مسيرة معادية في سماء مدينة جم بمحافظة بوشهر</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/78023" target="_blank">📅 03:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78022">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/78022" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78021">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/78021" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78020">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">مجدداً.. عدوان أمريكي على ميناء سيريك</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/78020" target="_blank">📅 03:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78019">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">العدوان الأمريكي الغاشم طال خزانات المياه في ميناء سيريك بجنوب إيران.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/78019" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78018">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">تفعيل الدفاعات الجوية في جاسك الايرانية</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/78018" target="_blank">📅 02:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78017">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">العدوان الأمريكي الغاشم طال خزانات المياه في ميناء سيريك بجنوب إيران.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/78017" target="_blank">📅 02:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78016">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🌟
‏
مسؤول أميركي لـ بوليتيكو
: لا شيء تغير .. الاتفاق مع إيران لا يزال قريبا.</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/naya_foriraq/78016" target="_blank">📅 02:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78015">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الجيش الامريكي يهاجم مناطق في جنوب إيران</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/78015" target="_blank">📅 02:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78014">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇮🇷
عراقجي: رغم هزائمها في ساحة المعركة، اختارت الولايات المتحدة اختبار عزيمتنا. قواتنا المسلحة الجبارة لن تدع أي هجوم أو تهديد دون رد. غادروا منطقتنا إن أردتم الأمان. تاريخ الخليج الفارسي حافلٌ بفصولٍ عديدةٍ عن المصائر المأساوية للغزاة الأجانب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/78014" target="_blank">📅 02:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78013">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cMfKqrE6sI9ESNXmXNmVWm2v6Z1VWFwKd7PC-XhDlrIcdyIOgGLoCkkrkQKdkaPGDubg-bPYRRBCZSXqBXDiEfPNCjKFgR4e9VeecVmq1FtRiL7CQwev26w9yCQbvcz-F5TTQec-lPNmJU5CohhuT02VoHk8_yt-oGHP1G7AKBTThT0JhqdQx4PgUQJn7G096QxxDWzCshv3JswDu_FzpZ0y64ifUURtG68sBRbgTJLtfS7IMwonQjsLvAQcl_yYb5tYMUbgrxRZPlXANIoNs4g0hLImXJhaDBx8CPpk84HMcPGsJcx8PGica3jdTdvu-3UK439NcN7065aTB0HYIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
عراقجي:
رغم هزائمها في ساحة المعركة، اختارت الولايات المتحدة اختبار عزيمتنا.
قواتنا المسلحة الجبارة لن تدع أي هجوم أو تهديد دون رد.
غادروا منطقتنا إن أردتم الأمان.
تاريخ الخليج الفارسي حافلٌ بفصولٍ عديدةٍ عن المصائر المأساوية للغزاة الأجانب.</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/naya_foriraq/78013" target="_blank">📅 02:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78012">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/736cdfac05.mp4?token=OplhQDShquKZ0LOc64uf82ej85ukhkSkm3RUHffEBqSxfxbCQvrGaT82SPBgUgnTftyNBIjxP6-IcKb3raWG3RLm6aBSsiWsIdilQeWp5y6fy1EHSAL582BS4DWcewD7tjBt5fpuFN4lgeno83MiNw4gVTVx5zs0hi8R565IRSMYQ0uEWlmjIG648XW8XBdbONdX7UdZLJjR5FKeUtVOqIYFIFZ2edIgWzEkJT7GetDRjswakhYVaoJ9qR-NmSA0UIqh8sNhVjjLKHXDzrPbWdspzYLFjRdhe9HqySVw3dNvqwQEmOBTGsMSt9BOZ7Nv4pIvLgjF4BFhXUTuqZjskQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/736cdfac05.mp4?token=OplhQDShquKZ0LOc64uf82ej85ukhkSkm3RUHffEBqSxfxbCQvrGaT82SPBgUgnTftyNBIjxP6-IcKb3raWG3RLm6aBSsiWsIdilQeWp5y6fy1EHSAL582BS4DWcewD7tjBt5fpuFN4lgeno83MiNw4gVTVx5zs0hi8R565IRSMYQ0uEWlmjIG648XW8XBdbONdX7UdZLJjR5FKeUtVOqIYFIFZ2edIgWzEkJT7GetDRjswakhYVaoJ9qR-NmSA0UIqh8sNhVjjLKHXDzrPbWdspzYLFjRdhe9HqySVw3dNvqwQEmOBTGsMSt9BOZ7Nv4pIvLgjF4BFhXUTuqZjskQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
التلفزيون الإيراني حاليا</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/78012" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78011">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قال رئيس مجلس النواب الأمريكي مايك جونسون إنه تم إبلاغه للتو بضربات ضد إيران كانت "دفاعية بطبيعتها".</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/naya_foriraq/78011" target="_blank">📅 01:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78009">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pIc7uAQYQrsInJWY_25DF8G-jb07pInyWyQSbTmN-ZvUF5i3q3vxSPGRzOKZ29P9CNyFGe-h5ZfA-76-yFlfVsw2Eapt9VzTaz1T5T42nmahckDeGpbw9xQQzAYFjpT9l5D0p78BH7vEBhUnGsP-TRfnwMwdRaR2gTuedx48ZM6w441piOfpDlmvNfcd_SvqKUP6saCs4D16W62emR06sgcXkbW5oflcneacaaLhLcd1blMLp8fkMv3CdFZ11B6bz_EUgRS_xaaCkW9AMWLM7DTDfSqlrmpfqE_Y9QDz61Y8bcfudTSSnpXBxbGtg_xrjYaoOAAYxtNwJmA0HkslLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حركة طيران طبيعية في قطر ودبي والبحرين حتى كتابة الخبر ..</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/78009" target="_blank">📅 01:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78008">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BbjV33_XLyw5v_7GJPLOd1jaxHsx45Wx0JlLII6yUCVwg0QCAaDtNnzjiQkWqy_-8TxzTuAYHTxbm_-Hfjjd7vX-VeXk7ZWRk0bB294OQzD8Oip2Z6aZrfqoHxhNLqXONeDXL0hk7WE6L0v9JV4Hbp0127t_jbaPJwL9P5tTScSVcyy8t3L07zIETpCeeTfiLMRUFTBzSGgabpWPZzfxqjvXOEteb6SGoDl0aSDo_s8E2LlN35lM-iwP6AVH3n9-8Jtyw5xbBN5WZBjHGTI_atb-gJrmvTnPGufkWOWlsHHEtmdXHQWCBTuN1oYXIUGSAH5mKhahfBv8-Xgv1pUgFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تستمر القوات الجوية الأميركية بعمل خط صد تجسسي قبالة خليج فارس تحديدا بسماء السعودية وبواسطة طائرات انطلقت من قاعدة خرج</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/naya_foriraq/78008" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78007">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KFiYCD0gQvVwEPCv-9RxAOplDqLhQz2waj0RFxyF6DcDhdDDppk4ziuQIduHgO0k5XQFTVK8Kkz0wpRtBbKyUVmDjep_eBTrJ4z-N0tRW2J9loeupmsIoVxf-kFnfflsiNluGgucMUm67nOK9g9BxwFriLA-RwhnrxfcQKlsrpl2FDDSbY3TC2F8_FLr9jNfnM5AIA56WbmjDUK1dM6O8MUYNA2RlQ2W6xnZRNzLHrpnb0hv2NDk956Q8mR3v7c358y1zAxv7dj9KhsiPl1qTJ9gDfpEnzTMMx1msYfFNaUBJsbYUhakzqpkrR4OKW6GVdvQ4i2df5EhUxXXJcjzRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ويليام بولتي، الذي يعمل عن كثب مع تولسي غابارد، سيتولى منصب المدير بالإنابة للاستخبارات الوطنية يوم الجمعة 19 يونيو.
وسيستمر في منصبه كمدير وكالة تمويل الإسكان الفيدرالية، ورئيس مجلس إدارة فاني ماي وفريدي ماك</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/78007" target="_blank">📅 01:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78005">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 27.8K · <a href="https://t.me/naya_foriraq/78005" target="_blank">📅 01:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78003">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uooZuRscRjc2XTRLVWgJA9zayAFX22F_eE190tRI17b2llPgBodA5wLT66QbTa1wU-0b9HoGtdPx49_4ocvcKdeu-f7AaZkyhXZJEynDmgmqOhm1D5v7Zg73-F2_E3msNagd0GIVTpaj1H4uRdUmtS3mK0E7SUo5zA8uo1SRZ4lSbhULs7A7SWUkgrpV-WKLMUqoRksatTStgqdqvAeFEpjL-5-LibyTikc5tctv4VcAqBWcjMi2TI0xSNWp7fM_ZugYQkJ-1nNyrobAMoC4YALjxxCtxVKUGl6zi17IASM9nv24dXsBB11GXRPkI0qHExpSdPCY0SfIvInnRKBRpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">It seems MBS wants his country to get f*ck from Iran again
🫣
. PM 8 spotted over the Persian Gulf flight from KSA sky
✈️
..</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/naya_foriraq/78003" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78002">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‏مسؤول أمريكي: هاجمت القوات الأمريكية عدة أنظمة دفاع جوي وأنظمة رادار إيرانية حول مضيق هرمز</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/naya_foriraq/78002" target="_blank">📅 01:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78001">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">😆
We didn’t mention F 15 because Kuwait air system defense are already ready</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/naya_foriraq/78001" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78000">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/naya_foriraq/78000" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77999">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-poll">
<h4>📊 Which airplane will Iran destroy this night ?</h4>
<ul>
<li>✓ CH47</li>
<li>✓ UH64</li>
<li>✓ UH 60</li>
<li>✓ MQ9</li>
<li>✓ MQ4</li>
<li>✓ A10</li>
<li>✓ C130</li>
</ul>
</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/naya_foriraq/77999" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77998">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">مصدر بالحرس الثوري لنايا
ننصح الشعوب المسلمة في غرب اسيا التي تسكن بالقرب من القواعد او التواجد الأمريكي بالابتعاد فورا عنها بمسافة لا تقل عن ١٠ كم ..</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/naya_foriraq/77998" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77997">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">ايران احد دول القوى العظمى حاليا سوف ترد على امريكا اقوى دولة بالعالم وتهين امريكا مجددا كما اهانت وفرضت معادلة بيروت اسرائيل
وسوف نرى من لا يرحم</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/77997" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77996">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ايران تعلن أنها سترد بقوة على العدوان الأمريكي</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/naya_foriraq/77996" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77995">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">الدفاعات الجوية الإيرانية تتصدى للاجسام المعادية في سماء بندرعباس</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/naya_foriraq/77995" target="_blank">📅 01:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77994">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">تفعيل الدفاعات جوية في بندرعباس</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/naya_foriraq/77994" target="_blank">📅 01:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77993">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ترامب : هذا رد على ما فعلوه بمروحيتنا الليلة الماضية، وأعتقد أن الرد يجب أن يكون قوياً جداً، وهذا ما يمثله هذا الرد."</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/77993" target="_blank">📅 01:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77991">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=fvRa8BSsOm0d2IycJmwStELNuz8qWVQ0m6Xm4lhsDxFKIWphVMu35Q5AFKDYmaHncRkxcBS5SimlcK_TPKMFMMYBMDNAc0IO9DMVwK0VBGd55tIkJpjT11S9yh0Xy5ab2D6CqmUeGqHxFkKvg4Xm3hbIj8oHkCki4csbwHuFuZiStAhX05ku3P0NOS4yN_Hb-FWZzi8fXMskVV9aY2IbcwLyyQ4AthWQ3EXGfxTsVacZ0mVaGdDEZ2WMG7jI-lrSvhC9INAMuw8RtblT_WcgBoP_3TUAYK7q1Rl5lnctvX7h1g7J4TtqE_J7uPGbcbhAZ8ZMNt11dFj5_ZAZqMpq8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0aca6ef1dd.mp4?token=fvRa8BSsOm0d2IycJmwStELNuz8qWVQ0m6Xm4lhsDxFKIWphVMu35Q5AFKDYmaHncRkxcBS5SimlcK_TPKMFMMYBMDNAc0IO9DMVwK0VBGd55tIkJpjT11S9yh0Xy5ab2D6CqmUeGqHxFkKvg4Xm3hbIj8oHkCki4csbwHuFuZiStAhX05ku3P0NOS4yN_Hb-FWZzi8fXMskVV9aY2IbcwLyyQ4AthWQ3EXGfxTsVacZ0mVaGdDEZ2WMG7jI-lrSvhC9INAMuw8RtblT_WcgBoP_3TUAYK7q1Rl5lnctvX7h1g7J4TtqE_J7uPGbcbhAZ8ZMNt11dFj5_ZAZqMpq8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/naya_foriraq/77991" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77990">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/77990" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77988">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الجيش الأمريكي: بدأت قوات القيادة المركزية الأمريكية (سنتكوم) اليوم، الساعة الخامسة مساءً بتوقيت شرق الولايات المتحدة، شنّ ضربات دفاعية ضد إيران، بتوجيه من القائد الأعلى للقوات المسلحة، ردًا على إسقاط مروحية أباتشي تابعة للجيش الأمريكي أمس. وتُعدّ هذه المهمة…</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/77988" target="_blank">📅 00:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77987">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/77987" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77986">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">سمع دوي 4 انفجارات حتى اللحظة</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/77986" target="_blank">📅 00:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77985">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/naya_foriraq/77985" target="_blank">📅 00:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77984">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">دوي انفجارات في ميناء سيريك بمحافظة بندرعباس جنوبي ايران</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/77984" target="_blank">📅 00:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77983">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">⭐️
رشقة صاروخية من لبنان نحو الشمال الفلسطيني المحتل.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/naya_foriraq/77983" target="_blank">📅 00:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77982">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
تلقت المنظومات الاستراتيجية في "إسرائيل" توجيهًا لرفع مستوى التأهب تحسبًا لتصعيد محتمل مع إيران.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/naya_foriraq/77982" target="_blank">📅 00:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77981">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🇺🇸
إعلام أمريكي:
قال العديد من أعضاء مجلس الشيوخ إنهم يعتقدون أن إيران استهدفت عن قصد طائرة هليكوبتر من طراز AH-64 Apache تابعة للجيش الأمريكي، ويتوقعون ردًا أمريكيًا في المستقبل القريب.</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/naya_foriraq/77981" target="_blank">📅 00:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77980">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇷
مصدر عسكري إيراني مطلع:
لم تُنفذ أي عمليات عسكرية جوية هجومية في مضيق هرمز خلال الـ ٢٤ ساعة الماضية.
إذا ارتكب العدو عملاً إجرامياً آخر بذريعة إسقاط مروحية عسكرية، فسيواجه رداً حاسماً.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/naya_foriraq/77980" target="_blank">📅 00:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77979">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c218f38b76.mp4?token=vhJOrsSf2SthfsS2az1RyMhfMEeoD2A5rrmK_u6XcyzyouLhqBfd2LY-qL-9ZZEN46iJcHtUKYkVzAZ4-HdTVkkJBoxo9IZg1wQTJxK9a9ZIqN_U5Zo_y26DCGpU0dRdiqafX-GAe0bX-BW27YpaDgElHPFbcIX4t3dv2PUX1AVMVp_0h3xWjkLQgdydndNs0KYJuvlIcTdz8twcOAoQ9OmrQik2YUdunUZZ9S_4ep_GDrolVnKo2eNU7dFmRBD53HfYBYw7g5o_6u6hR8oOhf8OCwe4YAFGCgbGB_a5qkS-2sAwl25wb9akf-zllxOoO8xvnx9Ytev9xwF5HOxr0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c218f38b76.mp4?token=vhJOrsSf2SthfsS2az1RyMhfMEeoD2A5rrmK_u6XcyzyouLhqBfd2LY-qL-9ZZEN46iJcHtUKYkVzAZ4-HdTVkkJBoxo9IZg1wQTJxK9a9ZIqN_U5Zo_y26DCGpU0dRdiqafX-GAe0bX-BW27YpaDgElHPFbcIX4t3dv2PUX1AVMVp_0h3xWjkLQgdydndNs0KYJuvlIcTdz8twcOAoQ9OmrQik2YUdunUZZ9S_4ep_GDrolVnKo2eNU7dFmRBD53HfYBYw7g5o_6u6hR8oOhf8OCwe4YAFGCgbGB_a5qkS-2sAwl25wb9akf-zllxOoO8xvnx9Ytev9xwF5HOxr0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🇮🇷
جي دي فانس حول إيران:
قد تتم الصفقة في الأسبوع المقبل، لكن قد تتم أيضًا بعد أشهر من الآن.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/77979" target="_blank">📅 23:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77978">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">⭐️
إعلام العدو:
رصد اطلاق صاروخ من اليمن.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/77978" target="_blank">📅 23:37 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77977">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇮🇷
مساعد وزير الخارجية الإيراني: إيران لا تقف وراء الهجوم الذي تعرضت له مروحية أباتشي الأمريكية فوق مضيق هرمز.  هناك احتمال بوقوع حوادث كهذه بشكل غير مقصود بسبب الأجواء المتوترة بمضيق هرمز.  لم يكن هناك أي استهداف متعمد من قبل إيران للمروحية الأمريكية فوق مضيق…</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/naya_foriraq/77977" target="_blank">📅 23:33 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77976">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⭐️
سماع دوي انفجار مجهول في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/naya_foriraq/77976" target="_blank">📅 23:19 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77975">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">⭐️
سماع دوي انفجار مجهول في محافظة النجف الأشرف العراقية.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/77975" target="_blank">📅 23:18 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77974">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromأثر</strong></div>
<div class="tg-text">هناك حكاياتٌ لا تُروى بالأسماء، بل بالظلال التي بقيت على الجدران بعد انطفاء المعارك.
في ليلةٍ بعيدة، كانت مدينةٌ صغيرة تواجه العالم وحدها. وكان ثلاثة رجالٍ يتقاسمون خريطةً ممزقة، وقليلاً من الضوء، وكثيراً من الإيمان. لم يكن أحدٌ يسأل من أين جاء الآخر، ولا أيُّ رايةٍ يحمل، فحين يشتدّ الحصار تسقط الألقاب وتبقى الأخوّة.
مرّت السنوات، تبدّلت الوجوه، وتغيّرت الفصول، لكنّ بعض العهود لا يطالها الزمن. تشبه أشجار الزيتون التي تنحني للعاصفة ولا تنكسر، أو البحر الذي يعود إلى شاطئه مهما ابتعد.
لهذا، حين تضيق الأرض بأهلها، يعرفون أنّ هناك قلوباً في الضفة الأخرى من الحلم ما زالت تسهر معهم.
حکایت‌هایی هستند که با نام‌ها روایت نمی‌شوند؛ با سایه‌هایی روایت می‌شوند که پس از خاموش شدن جنگ‌ها بر دیوارها باقی مانده‌اند.
در شبی دور، شهری کوچک در برابر جهان ایستاده بود. و سه مرد، نقشه‌ای پاره، اندکی نور و ایمانی بزرگ را با یکدیگر قسمت می‌کردند. هیچ‌کس از دیگری نمی‌پرسید از کجا آمده است یا پرچم کدام سرزمین را بر دوش دارد؛ زیرا وقتی محاصره سخت می‌شود، لقب‌ها فرو می‌ریزند و برادری باقی می‌ماند.
سال‌ها گذشت؛ چهره‌ها تغییر کردند و فصل‌ها عوض شدند، اما برخی عهدها از دسترس زمان دور می‌مانند. شبیه درختان زیتونی که در برابر طوفان خم می‌شوند اما نمی‌شکنند، یا دریایی که هرقدر دور شود، باز به ساحل خود بازمی‌گردد.
از همین رو، هنگامی که زمین بر اهلش تنگ می‌شود، آنان می‌دانند که در آن سوی رؤیا هنوز قلب‌هایی بیدارند که همراهشان شب را به صبح می‌رسانند.
There are stories that are not told through names, but through the shadows left upon the walls long after the battles have faded away.
On a distant night, a small city stood alone against the world. Three men shared a torn map, a little light, and an abundance of faith. No one asked where the other had come from or which banner he carried, for when a siege grows severe, titles fall away and only brotherhood remains.
The years passed. Faces changed, and seasons turned, yet some covenants remain untouched by time. They are like olive trees that bend before the storm but never break, or like the sea that always finds its way back to its shore, no matter how far it has wandered.
And so, when the earth grows narrow for its people, they know that on the other side of the dream there are still hearts awake, keeping watch beside them through the night.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/naya_foriraq/77974" target="_blank">📅 23:12 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77973">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🇮🇷
مساعد وزير الخارجية الإيراني:
إيران لا تقف وراء الهجوم الذي تعرضت له مروحية أباتشي الأمريكية فوق مضيق هرمز.
هناك احتمال بوقوع حوادث كهذه بشكل غير مقصود بسبب الأجواء المتوترة بمضيق هرمز.
لم يكن هناك أي استهداف متعمد من قبل إيران للمروحية الأمريكية فوق مضيق هرمز.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/77973" target="_blank">📅 23:09 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77972">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🇮🇷
مصدر مطلع مقرب من فريق التفاوض الإيراني:
لم تُرسل إيران أي مقترح جديد إلى الولايات المتحدة.</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77972" target="_blank">📅 22:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77971">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇮🇶
اندلاع حريق قرب سجن بغداد المركزي مقتربات مطار بغداد الدولي</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/77971" target="_blank">📅 22:48 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77970">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سماع دوي انفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/naya_foriraq/77970" target="_blank">📅 22:43 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77969">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6702ff2d3c.mp4?token=tOqX3nE4WjjvzsHpjavc40jXGUkrA9pRwoyN7-O-3y8paiQOdfHcak_UQizU_kGrvbbIcKBWbW5x4cQiVX7N6cVfHKhwj7W6FPxbmi0qUezVY6LDidkvNYwxSW_u9KchX9L-1kj6uWO6_-hES8REVqaY8WKCLWLge5HkuTyodHCZQXfuuYg6nH-HjMwVbj20HwAtQlfLkIrCr6lvFkL28jFWX2t4k9uWASY-QYL7Jkl2K_dk4P1ZzuTaGBc5pjOAJL981OJAdh2DpcN8QKnRNtgFhAnM4Cb3EWJNuCR7MvT2V02YTT42W8Hhnc2hQCUfnhh9dChQp-j0nMB6M1Goqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6702ff2d3c.mp4?token=tOqX3nE4WjjvzsHpjavc40jXGUkrA9pRwoyN7-O-3y8paiQOdfHcak_UQizU_kGrvbbIcKBWbW5x4cQiVX7N6cVfHKhwj7W6FPxbmi0qUezVY6LDidkvNYwxSW_u9KchX9L-1kj6uWO6_-hES8REVqaY8WKCLWLge5HkuTyodHCZQXfuuYg6nH-HjMwVbj20HwAtQlfLkIrCr6lvFkL28jFWX2t4k9uWASY-QYL7Jkl2K_dk4P1ZzuTaGBc5pjOAJL981OJAdh2DpcN8QKnRNtgFhAnM4Cb3EWJNuCR7MvT2V02YTT42W8Hhnc2hQCUfnhh9dChQp-j0nMB6M1Goqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طيران حربي في سماء محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/77969" target="_blank">📅 22:41 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77968">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dceed2faf2.mp4?token=Pp2yB6AELJFVJO-YWWofLPZ-wKS2we9YO1H0c5p3zU7ZpVMykivFxUIVgYfFtMWBh8lOh4yzgzw36YRlQIbzIWA8ymuUY7qQQyL0q6Qt3PklvASUHbu79mO9rhdk_6FetBnUKL8NHUsjwq0M_AFSrq0VIn5FSM56c3xGeZAifPz2eOCXqz0c3P2wV2cPhhsNHo6TjL0Cn2mlTdNtfBxOCwxWLMWd238qm6fiU5qzHw-StnuD5nCHSjbHqQJLQWmEs6m7yE2gKRGmplTAvo5YHI5DG1DuM7v9qzRgRv4kGQ0qOwQrKev6ABeBTE_no1gylGSsmAMoPyDOjWSW9ZV-nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dceed2faf2.mp4?token=Pp2yB6AELJFVJO-YWWofLPZ-wKS2we9YO1H0c5p3zU7ZpVMykivFxUIVgYfFtMWBh8lOh4yzgzw36YRlQIbzIWA8ymuUY7qQQyL0q6Qt3PklvASUHbu79mO9rhdk_6FetBnUKL8NHUsjwq0M_AFSrq0VIn5FSM56c3xGeZAifPz2eOCXqz0c3P2wV2cPhhsNHo6TjL0Cn2mlTdNtfBxOCwxWLMWd238qm6fiU5qzHw-StnuD5nCHSjbHqQJLQWmEs6m7yE2gKRGmplTAvo5YHI5DG1DuM7v9qzRgRv4kGQ0qOwQrKev6ABeBTE_no1gylGSsmAMoPyDOjWSW9ZV-nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
تحلق سبع طائرات تزويد بالوقود تابعة لسلاح الجو الأمريكي حاليًا فوق الشرق الأوسط، ست منها تحلق بالقرب من الخليج الفارسي</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/77968" target="_blank">📅 22:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77967">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سماع دوي انفجار في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/77967" target="_blank">📅 22:38 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77966">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">نايا - NAYA
pinned «
⭐️
قابل توجه دنبال‌کنندگان ایرانیان عزیز  ما هیچگونه فعالیتی در پیام رسان‌های ایرانی (ایتا، بله، سروش، روبیکا،...) نداریم ؛ در صورتی که تصمیم به ایجاد کانال یا هر گونه فعالیت در این پیام رسان‌ها، از طریق کانال اصلی خود اعلام خواهیم کرد.
»</div>
<div class="tg-footer"><a href="https://t.me/naya_foriraq/77966" target="_blank">📅 22:35 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77965">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">⭐️
قابل توجه دنبال‌کنندگان ایرانیان عزیز
ما هیچگونه فعالیتی در پیام رسان‌های ایرانی (ایتا، بله، سروش، روبیکا،...) نداریم ؛ در صورتی که تصمیم به ایجاد کانال یا هر گونه فعالیت در این پیام رسان‌ها، از طریق کانال اصلی خود اعلام خواهیم کرد.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/77965" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77964">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VsCsNAR26zFvZ2AW7RKGb2tto1pZLkg7sa8PF8dV3P2CQiuT8b5gA0Pi3t0qV9gkZTYeYv2LRlUG80DIZvArJgCoVllLKaVScSEFdg9Jl2sp-v6vF3VGp6-cj1n24qGcx52_hgh3hCgjMew4u2N8m0PbuHdW93ObHVZMX-vtC88s7W3oHkhGJ7I-18zQUCi2cKSMQbwdx7FWoLlOta7ulg4pbQPATsPLGGAB9H1FrLzfquowe28ZHRE6Sg2ka2NYrc5vsH2lMQJb6kuSN3lRgIvYLknu9XhhWNQ9Xe_upHVloyfcU9xwkUzo82uEoWPZgIxYgpruqBHGvdkBh6Izzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇺🇸
تحلق سبع طائرات تزويد بالوقود تابعة لسلاح الجو الأمريكي حاليًا فوق الشرق الأوسط، ست منها تحلق بالقرب من الخليج الفارسي</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/77964" target="_blank">📅 22:34 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77963">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🇮🇷
عراقجي:
بمجرد الإعلان عن موعد مراسم وداع الإمام المجاهد الشهيد وجنازته ودفنه، وتحديد القدرة الاستيعابية لاستقبال الزوار الأجانب، ستقوم السفارات فوراً بإصدار تأشيرات الدخول للزوار.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77963" target="_blank">📅 22:28 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77962">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي الإيراني:
القوات المسلحة في أعلى مستويات الجاهزية القتالية والدفاعية، والحمد لله، تم إصلاح الأضرار.
القوات المسلحة على أهبة الاستعداد للتصدي لأي شر أو عدوان على أعلى مستوى.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/77962" target="_blank">📅 22:13 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77961">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🇮🇷
مسؤول إيراني:
مروحية الأباتشي الأمريكية لم تكن تحلق فوق المياه الدولية.
سنرد بقوة وبشكل فوري على أي هجوم أمريكي تتعرض له إيران.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/77961" target="_blank">📅 22:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77960">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">⭐️
الناطق باسم القائد العام للقوات المسلحة العراقية صباح النعمان:
عملية حصر السلاح بلغت ذروتها المُلزِمة ولا خيار خارج مظلة القانون.
-إنهاء المهمة العسكرية للتحالف الدولي أواخر أيلول المقبل استحقاق غير قابل للإرجاء.
تكامل منظومتنا الأمنية يشمل البيشمركة كركيزة دستورية.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/77960" target="_blank">📅 21:58 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77959">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JcMxIF4eihdNiO9Sr8qwFKaxATdbpJ4O1InmYH-UESJBOMsCnMPCG51BPrFjXsQwVF_ggCrQiX8WyjtWYJoZlaPHbI3Njz2U8Uaecmy9reGD-4RPilL-tbzE0hEN-cUlc52yhr_84IS3wN9Dd4x5wmr0h6tbywnPBiPZs2zceKRKkqps1DKlrjqCPMbAbAR7y68sQ-C4I4zf7cEcQ4Cvx29PxKJIGcW4uXgW8h9TRptqfZUicsJ2mSofTJT09q4PzZsg1g7Jm3cZn-HSV-o3zagxJJRwwFhbVnYX_DKmwzDYZ_1tb2Omd7l1bRuOet1KFSZnIHzfG2E_HOMIBNzhpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنجعل عاليها سافلها
بلا أسقف بلا خطوط حمراء بلا قيادة بلا تفاوض ، سوف نشعل المنطقة .</div>
<div class="tg-footer">👁️ 9.48K · <a href="https://t.me/naya_foriraq/77959" target="_blank">📅 21:57 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77958">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/77958" target="_blank">📅 21:56 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77957">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">ترامب بشأن إيران: الأمر في الواقع بسيط للغاية. الفائز هو من يمتلك القوة. نحن نمتلك كل القوة.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/77957" target="_blank">📅 21:55 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77956">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5b4b73175.mp4?token=QLAUOOTSP-IDGaYT99B2tYSDIJ9gbwPSruQ-2MVWrVatVE7CMntjKZQdf_CANzAtegayn3VvN1fjQXDclfLeIfzlvX6yYW44C6IhEOsWZK2mmuyTmUKnUIA-XZrN3yD0yFRVsQzWMNJpkVPAWqmcG5AFTdpPrFJlE7YKfrZpjY3cFgIDO2p1J7McWXLxfERwtyxXd3q5b86EckH9Z5xgTaRPT0xpO0TruLIYfCe7KwBpjCe4MfZEF5sa03CEWyiSOk529Fh2mYI-_-dT_8v2JVLAvK4tl1-Zft5D5PaMKn9qU5cbpv614YH_j-E2WnjgaKWz0X2_Rv8Go8m0fDH10agk6GXHToN9VlhVSQN336PddtrLNEdXdZvqbn8f_25CWkyLG5xugF0MkSvZ0XHxAiYvoumWZFOK1p5Pb0OmSW-6nNWRjKN672dsLZjS5bw_OzvkqywGk7kaZeAkCAwEX7DUj3XMCma80a7Qt86l8MXx0vFalVxFYco4u98EVo7U6tiU3Hh4kI7EvUjRl0pGNVdDcofnjGLoRzg8pYWhOwCIQ_TuWTsQ_9l_0ylLy0FVvi5pTsYS9jCKpH3LmPvaE8oSeQgliJv0oO9Y-EL0M6xCIqzypsQAkPHZHmZlDEOtcZPemmiNQL5PmQAnjnAFW3ayjlTqCHVFboGnKLiSW8M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">We are ready for them …</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/77956" target="_blank">📅 21:49 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77955">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p8I0EA0-LH3hoNcNm2JwnsT-ScafHhCV5Gu4Fce-MhRKAxQUigFq9hqj16-he5h4eZoPFJ9FvMxp7zHRITGf7hz58omzbosFrPLXobrX9aVhQnAMa8f1s7D-Ht4IP6_v4FUlRJ2HJEWr65k8bCh5OJ-eN8sPZIio7QYcrn3H6axUdFoDnSu3g0SXemtcm6e02hp-Lp5jBQvqpXOxL3qoFOUTX2UiZgDbPHmDBsJPXcK0pSzlJmbS9m5TA9Nf-kobJsrmIq-mJ10UuSuujsZp6Y9eeh3y8yoG_0BuYaq1usTCaS9RP7jl213vDa1_n6vZnQnpySgxKHyNRvJVWcDYSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
‏
إن القوات الأجنبية القريبة من أراضينا معرضة لخطر دائم بسبب أخطائها البشرية، أو الحوادث العرضية، أو احتمال وقوعها في تبادل إطلاق النار.
‏لتقليل المخاطر، فإن الحل الأمثل هو رحيلهم.
‏نحن نفضل لغة الدبلوماسية، لكننا نتحدث لغات أخرى أيضاً.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/77955" target="_blank">📅 21:44 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77954">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🇮🇷
عضو في البرلمان الإيراني:
إذا كان الأمريكيون يعتزمون انتهاك وقف إطلاق النار أو شنّ أي عدوان، فلن تتهاون إيران مع أي طرف في الدفاع عن نفسها. جميع القواعد العسكرية الأمريكية في المنطقة تقع ضمن نطاق قدراتنا الدفاعية، وسترد إيران بحزم وحسم على أي تهديد إذا تجرأ العدو.</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/77954" target="_blank">📅 21:36 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77953">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">⭐️
إعلام العدو:
أمريكا سلمت ايران عبر ابو ظبي ٣ مليار دولار لكي لا تقصف اسرائيل مجددا.</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/77953" target="_blank">📅 21:31 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77952">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">🏴‍☠️
إطلاق صواريخ اعتراضية فوق نهاريا دون تفعيل صافرات الإنذار.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/77952" target="_blank">📅 21:11 · 19 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77951">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🇺🇸
مسؤولين أمريكيين:
غير واضح إن كانت المفاوضات مع إيران ستستأنف بعد تعهد ترمب بالرد على إسقاط المروحية.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/77951" target="_blank">📅 21:09 · 19 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
