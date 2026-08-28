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
<img src="https://cdn4.telesco.pe/file/WSHzpSj7pqB5SVSmmF2bVr5-z6Mgrhu9PaCa4KS19uyC4FSUxEAg1LOzsCYx5wDBlIar74yQf70IPVqHA9LfwRKLCchaN3ta6Z3aNoWWMyi3o7csRKRi5t1qiuzuBJmjxKu7O1rP10MPCkVcuVn2T4bpbQQpV3HvhDbMWQN_Wj6Bl6ysnTLCWEcZUIOMmHZGdqpg7uyHiRp7TPvE4S_-2w6gtrQeLCH9RILi3IPuVy1MmSgHVMahskdzgNvWBzlirhd1D5nZJL7j5kY3E48KeG_CCDmI07k0cT7wgdJePZUz_Ej4R6pa09F09F3mxBAT-iQcIQKnO3lqAhg0Zy__OA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 640K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-06 05:04:32</div>
<hr>

<div class="tg-post" id="msg-28601">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q1ZyggpBevHT6HKVddAiq41IxT0iXCQo0_4oJ9-E2UH7dbrU-JwyPmOR-cX5U_oGyddu6ItsTRSeipUlUy87FsXqmYwFJMGOPneaOrPZwX0zdI5iRGq3-ho3WI9PRoP9Hghcn1dtJFLXwBPygCpKreg6Kr2Y_iX4bGoAYuGw7zXwLp9iAYsD2Y6VV0hdr0gZVS5zBAFxBavC9TyKpok7udy-E21JBGH1oYR3wK7skqU334gJOYw_atOvt3zYPlJ36ap6yzId2mo3iH4pbOWDaeZtZtY2_oS3S4Zx8EpLeNHt82JwrvB3yXBNvOKTDXGqDJPPvq8uOfjpg7UFQZilHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
جدال شاگردان سهراب با فولادی‌ها در هفته چهارم و دیدار افتتاحیه فصل جدید بوندسلیگا
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/persiana_Soccer/28601" target="_blank">📅 01:50 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28600">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bcBewzjCn97lXEZRGOE08h0kP3VFJCueDrZdht3cbY18yb5BcUltXMxF26IuohUeAyE0nCh0qipu1brT_d-y3ackXxqIyxbMRzOazmaJcv4Xv_sPXZ-NMsCZpDKACodwMbnCTA5PX5Zi2SdWCYZWIVVjnGmaiG07C8_T39SIC5j_SQw8N26uyEFBJ2ynCn1Rcf0mr9hkK-TSmTLv1I3LWv2vPtGlqFvBz2pZFOwRHphdG20BqLKpXuBC7FpAO_lruWn5KRY5uzo0Xtm4kyH3E-T8zYPeUSqcV1cFbMeHzXJzBkevTz49zmwiaiaC8Tv2hwWbh3ulJYLkA2qlPQzSIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
برد آبی‌اناری‌ها در اولین تجربه حضور رودری و صعود چلسی در شب گلزنی دنی ولبک
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/persiana_Soccer/28600" target="_blank">📅 01:48 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28599">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kT8wZt7zf0CVbsy4e0C9k1isd2KQve0_h_wzZvk9aTXhHXbXrP8i4BcOquLqee2Z1JbWSn-JM8Cwc-QGkiQlDmYQPcQ3WUy803sxuaLbXLGx_zdBNffSIj_B78fUCFoRzRLzmQzcjcQm-Kk78x0wSNCN4JmlR3EMXUkBwe78_2xexPgp34dOunFwtjCoiEbtVl94M0OTiK6W4bOq_Mu8-Rvzw0BvqYoLL1DLX20DZUCTDi_uaNf6YcrAMdko62-xlHNB0NslyxeI3lF71ehWhOTyvfJZOZj4hw0TgIeW_b13JwME5-Ksg7q1MI1l8cwDVZ6_vjX_o2gfIbsxfrkeYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/persiana_Soccer/28599" target="_blank">📅 00:42 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28598">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mGLQ6Sy9mEvbjiaKwpfjev5_y-YbSniHsiCpdsbMjdeEuWeVT_F3k7ICk_vgYzWvynd7dGO9anqBzkq3lGCk_GUxJu6pAr9i1RnWMut2L-CRJ8xEHo92Fzbxu8rBFtIKNFpbtnjkqPuVlpJGCN4Y-6VCvxdrUEUfIzSvgCJLojbI1RVAnbIlU1hP3ax966kZxctO-dly2i3mlXw4HNc3I9bX7UaGwNNLKb-ZQkrTOD-tfu8mOy80kMNWpyC2AnZGDhqPSlFeAJF5PsvBe25jxMvpsb2-eya6jB-0RWUZUx8aUCTK4ddWWpqOWb28Ij1axCzww8ZSEPye4EyNPTn9tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل زده و پاس گل از سال 2020 تا کنون؛
کیلیان‌امباپه‌وکوین‌دیبروینه در صدر جدول.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/persiana_Soccer/28598" target="_blank">📅 00:31 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28597">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d099f34763.mp4?token=qbBUSp7sCWNZcdK1z2uT6_PKM4MkS_P_N3qE_P0N5ke9hlSj5taB24q423hPPmVOLH29WGHsdjZTW72RFJM8BZTwr2YVUULbsBP8x2AdurPJ9OK4Gse2WUo08K11r8kbhAeDQQlmbHV0yR_p0Z3UG6KJubKdum4tZXnUb6H5LHbEwK05-2kaGk32JsQWOcTizxfpde7z6_Wz_M_9BRC3G2fNDTCPNMhAkOy2OzBXJbrxxLmw3jKGrbzfxNiyKBVdl-czNMAv_lqkQCF8CwXh8EjlaZOBVMCPKV__apY4-SKR_9kw6iHouYgCoIRaJ19sM9BidTr8zX9IAF9BqISDrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d099f34763.mp4?token=qbBUSp7sCWNZcdK1z2uT6_PKM4MkS_P_N3qE_P0N5ke9hlSj5taB24q423hPPmVOLH29WGHsdjZTW72RFJM8BZTwr2YVUULbsBP8x2AdurPJ9OK4Gse2WUo08K11r8kbhAeDQQlmbHV0yR_p0Z3UG6KJubKdum4tZXnUb6H5LHbEwK05-2kaGk32JsQWOcTizxfpde7z6_Wz_M_9BRC3G2fNDTCPNMhAkOy2OzBXJbrxxLmw3jKGrbzfxNiyKBVdl-czNMAv_lqkQCF8CwXh8EjlaZOBVMCPKV__apY4-SKR_9kw6iHouYgCoIRaJ19sM9BidTr8zX9IAF9BqISDrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
انتشار تیزر رسمی سریال کمدی «مرد سه‌ هزار چهره»؛
آغاز پخش از جمعه ۱۳ شهریور از شبکه سه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/persiana_Soccer/28597" target="_blank">📅 00:15 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28596">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OsocyBPRn1MnqTI26-p4wwDCBgsTOaVmwNZiqM-UB3CqB5udmL4IL4VVvP4sK1KNhdnZYj_DMz1f7M2w3xQ-N4VikowYssIudWs4lr1ebdChVrTGb5vkcRF49E8eVOzCVU5HEw7-8l-9wE7Jz29ILv640wSTPI_JmZzNbZe3Vkdv-JTIrVZ7Vqvuoxe6mtG20LlHUEn5Gx8MwDx_ZPLYtD3NgIt0irWD30tg0uiJOnzLql9VGGefHElB-IDJriP0zClb_ZathG4olQff8b9H7Lr4KwUW29Tcc2uRGk6L65P1RUcrQHbZbn_jTzNT6tOYN-3v1ygRPq5FEVqSoGpiAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
ترکیب احتمالی استقلال برای دیدار فردا مقابل فولاد خوزستان در هفته چهارم رقابت‌های لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/persiana_Soccer/28596" target="_blank">📅 23:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28595">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZZu_jwM6LwQlcTrQG_32Kg0GM9tRfWZrDm1m0Tctg2T3KkF7sFNbM2N7Z1gfroI_8FUwqWqB1zNt8pZWcv2LqzwyTczylQ3DjJpjz3L4Bi0o1aUyqYAs-Jyvw9GXn_rSyaZKf8-zC9QiRKj-dT8OIdHUFWBPNwNJUuW1tADmJZ1QkRnyiQHEdwsZymCIkp58f9ygXbkxmYYt51fMT2Klv5wLJWpmINdqWz6VkCzpydXKKMAIVpoOrN8PsBgNHLOwuEBDNY60we7jDCeJeUZgVyvAaeav0NgkBkJ7VquqAWg0v_NUzkNbDubK43WGcafMi5le7MiNNSav6CesfvPJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/persiana_Soccer/28595" target="_blank">📅 23:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28594">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f_czT5bHFA6BKhHTp-pMGZ2GgiTxy7V2ZyW3weF84LQU6SrJf7uisLhRLhuvE1p1vTTLl0GeTYk3WGL7ArPwx6rZHsd3p0Jl0Q5Pw9Y8q9vJaEd-et5lMrSJecop0ctME-jzhCldtgfD7vZ90bA2Zpu6aRNyJy75BOQYpD3uQ8bWAK2dZRWnT3Upv7hAi7n6wYtjViAk-2TiL06INqZZilv_zZLqygckcohZhoJQ976U0g-pjkZbFqozWzgYuerdnDZSMGpAOAGvir-61NXTQ2SzSME9g0bY26Esksd8rBDFnkMZgtdwL1Ce2BowJRjD6K_w-ap1yY8O5HntarZUwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
⚽️
🤩
بیانیه‌جدیدباشگاه اتلتیکومادرید: تحت هیچ‌شرایطی خولیان الوارز رو به بارسا نخواهیم داد. تنها تیمی‌که‌موافق‌هستیم آلوارز رو بفروشیم آرسناله و هیچ گونه مشکلی هم با این انتقال نداریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/persiana_Soccer/28594" target="_blank">📅 22:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28593">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Tg1dCBu23UBOHgFsw0sM2exXSVgJ6n6r1hLjVcZPoupDROaY86kFAl2y0L9CNCdHC01mq8NlclzEcPY8n0IR7bQ7pd1EtEiSLAOKAyijmqihZC8Ms8SybKfsWF_gV9UsVuNvr78nKgO_vbAmKJ2bBOlMzdVg2H9wULps4uVdbSzLAhO4mAbJ8vN3yqX72qXVk4aQ-juSgHOzJlN8cg7YsrGg9DbDF1VKz0Y3zz2d4SSsdu0vzwgxXBse_jnr8AsbcpIAx4KWzyh2qYpTKNx788ZZFhUsdlRU0ptedakW6OJxOi35toqAgc9YoEDJW-X8fh1ZBhbzqdDopvIv5l9HQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
بعدازجذب دنی ولبک؛ چلسی ساعتی قبل جردن هندرسون کاپیتان36ساله‌سابق لیورپول رو به خدمت گرفت. حالاجالبه‌بدونیدکه هدف ژابی آلونسو از خرید ولبک و هندرسون‌بحث‌فنی نیست فقط‌وفقط میخواد تجربه تیمش رو بالا ببره چیزی که توی تیم خیلی کم وجود داره و رختکن تیمش یه رهبر…</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28593" target="_blank">📅 21:42 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28592">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fbQY7ttCNkKJJ5dM3VmO5KfCECC-OAEohFAGLhsJEj4xMyj_0py1X3O2MhJGFBraGSJA5Uz8IPHi_l7D3gaVNTktZxSn3rorXgNMx5iAnQZRzaP6MAxdq4wkkFO2LbLoAhlAPRKGtsRMJvwVoUTxn7ahSvOc6EZ07A6XcwityuAFdwjpXPhJCJZIiyygRat1Ivux8D2RRiRpEMBVdUILIrKB4h1hJpRrY3KVPhOIRFITC2eTxzPgG57vTFN7yjr1c31JvZxsqkaTTceebZOdq63ZWGVV3W_VvT1Wyyar5aCII5m6cyD1Mm47K3pB7fHfEfp4o-nqro5cf0FozZ-nWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مهدی تارتار به مدیریت‌تیم پرسپولیس گفته اگه پیشنهادی با رقم بالا برای فروش اورونوف به باشگاه ارسال‌شدمیتونن اورونوف رو بفروشند. حقیقت اینه تارتار اورونوف رو نمیخواد و میخواد فراریش بده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/28592" target="_blank">📅 21:30 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28591">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A4KgIesEiDK1zrT2GCrkoKbc5wvxxYqhW42KaRKjtYf_I_0PUIS1areuSafqd6KPpj0unLecawmK0cabl_raviecmziP_fqrovIqD-78LvjBZRj1fTaskmHqt6X7ZWep-arbUdPK96VL5i-LTAi-7Z5McHp1QgY7wLhZgcd5T9jfi9fFhHEzjxKYU2BuFeIrlaSkyl6h6xfhvJ1ml7ygft4PV2_wuPWK6YjsjkAv5z2fGnNQluvstyOVp_KLA60exKV_95P_7IzPwZHCiLILWRuG5x0jflxTC4JL0AvAsvxNiKaTx2RdkeBbVR65od-_Hm56bYLP1gJ16oqsMWugWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک‌ترکیب‌بارسلونابرای دیدار حساس امشب مقابل اتلتیک بیلبائو؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/28591" target="_blank">📅 21:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28590">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AKyD_KRTaCpPYvY3MeSTyQOijd_GYtww7sxhc2wdf5RDhmIms1ZNGFVkUvhWM1fVRQDUgIOCbl5QePmQNF6_MKBtc1ckRXNWFLhH2-991Y1zMe2HD3jxxKSkMiNDUQh-w8fZGOA2AtNONu1joSQPqRVhji8G69isgfAm9fEgFiZRsxaSZdfQ0xq5plKdQfuv7n70Lpv1QbZ5S-sfX8e1qG3suby1I58LWyCW_atpIWF-ssuv5GSyblNWiUJcaAcGR3G_hIkKElWImoMxmAam1A6_nVcWjtAEK003wRZbEotDVbBmw5Xdqh1IBTNzkfrSSEig6gMLs98Q4eahvy28Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.5K · <a href="https://t.me/persiana_Soccer/28590" target="_blank">📅 21:09 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/016588e26c.mp4?token=RUv4a3aCf2LBS-AR0hM4hu32S9W9A25fSd5KLxki2iDInAfkNdyb7c0-kGH8ClBlTUOBKqZfLARvlm8g8LRsxOVBoE12WS1-ky5KmjsM9wQOG547JeMo3AW7TzGmzEDSvoXmvhylYI2lcH0Xyg_k4_bVfS2QpYZn37-E1kOoSOiOaNFEzpcxBSmqpGYFtsQJT8Wi47qwvulUIehIvn79EfXfRIjmgzsAZxWJ26iwWhful1vO6-SIS27FkdIhlnro6dBu24SshXrBDTQQn2JSQ3zLwfEBEDIBeLLOC7lH2eKaC8Yoy8Q92jnnrlLmMYxGr9omiZoWkf0h0HLTtayUYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درد و دل‌های علیرضا منصوریان سرمربی الطلبه عراق باخبرنگان‌عراقی بعداز دیدار این هفته این تیم در لیگ‌ برتر عراق که با پیروزی تیمش همراه شد: 8 ماهه که هیچ دستمزدی از الطلبه دریافت نکرده‌ام.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/28589" target="_blank">📅 20:43 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DAYUhZQmm4qQ_Q8iGN9CD0nQpSSHxJDdpxXh9JTm2IzcSSKPHkseP51Yk_mKFzpmVEA8Zv1SqEWOitbux6h1zzay0Tsk20MCUYeFMipVl_Jf8-WF2lf44hc1tgBDKzG_pe3knneoK8xvzAx7Dhav-idbuo72WHpv6wDZNcvb6sbMPMXcrZqRMLlm_7ZP8kUye8vwPGQtqGXi7ciSRo0J4E9MgFaKxeIWlXCkCzxNVv06lD0NELS8k3HCiXErYKlyJawoea6O_ib1os3qwtUhEOTMvBhzbmRekCcdzvfH1B6k-Slz9Lgbfdk61_pPYAf9ah5BTPUCgV6xwTb4Ltgemg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
⚪️
آرسنال و رئال مادرید درمرحله گروهی لیگ قهرمانان اروپا بهم‌خوردند؛ آرسنال‌تنها تیمیه که رئال مادرید درتاریخUCLاون رو نبرده است. برنامه کامل بازی هارو در پایان مراسم قرعه کشی میزاریم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/28588" target="_blank">📅 20:11 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoHnguWcfNw8d1dEAaRPHncb_N73ZT_YmNyTP8IWdMyauDKjZ-yJ-Fy4cl7-FlLInx01mAhzl7uQ5BtThJu9BthiUqnGUPl1B1VCqxKtQpye8iqcyy1otEFFUf0_T1GnlpkyMOoU_8COp5er_Sg2wzBCmizVIc_7KELOoMqOx9yHJkxFCyMLT8xUi1maOyDl0kbUQQFHqXNFqVN2-57qPsvfphYjitoYvQLq416EigZxx-r8CGi40_tLyj06rCAGaZXwVGgpEg0NqOK57s_kmSSZBHRupm3bECp5dWMtPF0In9CQeJTHWdkiARi_orQPx6QFFUOPtIHyMHs3sp4VFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
سید بندی فصل جدید UCL مشخص شد؛ قرعه کشی مرحله‌گروهی‌هم امشب ساعت 20:30 برگزار میشه و مسابقات از اواخر هفته آینده شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/28587" target="_blank">📅 20:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28586">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQWiFtZcueHreMpzc1Ip5BYrPs7gGoRjivRc3hXgskudZgpaoxoY8JWspMooEaHQKOkQ--7b6zIIQP9bf4kwDrLLntUBMMdFA4ZBpCp2Fjf4wjBrRbXc9DoYecnGq2VgABkioixXcRbJGKqa4ymbwTZKsbuHiItofnoEjtivMontataOW_9el5LViy7svISjZEJSdZtuVdTiTyWKgvpA1i7EY1QzJ9S0z-YI9PXC5-sOU2rlM-8ay-6yt3BWIHljhmKgi_um2swVYAU5NTHx_GuE82jKFZBnCc4pYHxM9g5Ab-3IazNdGfpg6H3uzuuHgkT9Iob59Z8A_4BR2yUbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام‌پیمان‌حدادی‌مدیرعامل پرسپولیس؛ پرونده نقل و انتقالات سرخپوشان در این پنجره بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/28586" target="_blank">📅 19:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28585">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ry5jK_sFiv3ycjltH9v7ufowszfe8P_k3kxEBBYP5OgXVfwzyM5uZGueJ0LEZFUAQpYv29GcvP2cEl-AFAI1JntXYYaWigI6TL4LZZda9E8Q2YMvGYcWD9xBhVGmpG4fAb-NGBgY3MAZb7YySA_3c2Iy00MwMus2To-maOkgQGwtq9WD7Npgi5f6_q1Qtlqc5d2VGfUGURo1Gkv1i6YeroUVBn54qwhzDqQidEiCnbM8BUmvTlnM_CtZ4EYrGpU6Z2Nz1j38vIRoVohkjI6i_IZzNE_zw8BTN28VuC7XlnwLyBJa2aLYCsCczRZwIF23l5sx2_oqdSce50ApOpln2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گرانقیمت ترین بازیکنان آزاد ایرانی در ترانسفر مارکت که تا به این لحظه به تیمی قرارداد نبسته‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/28585" target="_blank">📅 19:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28584">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nST7ms-ITcXgO0wnL7exLWG7S6hjOH0yViuVIyPoPpULAumwSyVTLhPKM3-5fDSckLhWyQvETQOqm9qaFlEHpGCqnmEY5FFJXBWDerREGIocoHxKwTGFRa7Hd2GaIp4puhZrqP9xWqR9362FtUcEFtc80IIbWobxJE6d7wI6_UKe38qLb4ogK5K4US6CYjq-jR_XbmOGhg_Q-4NnzmvQr4pfCtXEkbUrylWgismgo-DN6jSjCcLuiAhp0l2DqU7EicAxlu2Ist2L16NOBeGNRnyrejBdwiCkTsP8uYs9DZrO4gwmI9TvvWFtTj-LRAUfNEsVvmK64pzSae2tlr4vMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق شنیده‌های رسانه پرشیانا؛ علیرضا بیرانوند دروازه‌بان‌تراکتور رایزنی‌های‌خود را با نهادهای ذیربط برای تمدید معافیت‌تحصیلی او به مدت دو سال دیگر آغاز کرده و پالس مثبت هم نشون دادند و به احتمال زیاد بیرانوند شهریوربه‌سربازی‌نخواهدرفت. سهرابیان نیز به همین…</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28584" target="_blank">📅 18:37 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28583">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OTC8_E7oR-UdF4Epie-KGWDolv1U8jkiXXHB3TKILdk414CuOeCOiNufgRgH337-XLWjb5hZ71D5AS2SNPFpW3txFmJxyLldhtfr9_cu0T8OJL3yP3wkRs3Q6S-36OGNUaB9GhgWrCiSN43JlysHwN11FzZF5yJFR41VpO_Pc76yvwlrKe_EXgnS2rTNwpHis-4zZBek70j6M8DibOyQQ4pwlcN8-9D3E7gjuJjP61o82qu5Ssgyw5ukYVaqFAzy9kQZFKTpLD-pFHBKm_eLrH_Zws7MkAuo0QjupQlUZAQ97i9yOSyOx2u5xZt7TZB7MO4SvuWxqBJQtgwQHAho2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇪🇬
با اعلام رومانو؛ عمر مرموش ستاره مصری 27 ساله منچستر سیتی با عقد قرار دادی چهار ساله به‌تیم‌تاتنهام پیوست‌. این یازدهمین ستاره من سیتی بود که بعد از جدایی پپ از سیتی جدا شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/28583" target="_blank">📅 17:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28582">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dsu-qjBud8-sOYP2UyijEe9jK8E-PFXb6_0MXrAtvk8rCU5kefLaKqr8Z6ErFR7BKAQ58XothK0b0FPi0-PAaLILHqGovPZmue0-ijH8260HkcFSk9QJpVnP2uW1lz4IZtdZtrTalwJ5LHZ4F5e8m0bZ1pJbbQJGFwmG5H7Ty8Ar6vLmPDTDa2-LptksDEPChtvia9-vDH69h51brGuMBFieA-4Pfqk_CzC5-HV_zUX6X9m2mIwLVHPMLqIfQGZwzZcyD4qnTArmMoh2cFaZwCN1GcWp8-h_P1JsWvzBEuJyEg14sfHLoTNVeD20ll14iH7YtwKOzK1QT5hy7IFp9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
#اختصاصی_پرشیانا #فوری؛ باشگاه آلومینیوم اراک رقم‌رضایت‌نامه مهدی‌مهدوی مدافع‌راست جوان خود را 300 هزار دلار اعلام کرد. باشگاه پرسپولیس طی روز های گذشته با ارسال نامه ای به این مدیران باشگاه خواستار جذب این مدافع راست شده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/28582" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28581">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c66lvqwC8cak9LIPf7c79oxS8xoznuFPTACSmmGdEDh4YMr3Ea2AYIdXPAotRucwW9C9UciqW5U4J2zimXAfNP0orUBPlFjDkEAPMi0KAQ29xV7JHYqcZ_uw_Mso7FPLZYPOGraigKeCuQOtJ_2eR41CM06jqKK60rHQywbQyu1ExnBdQZk7-aPLGQu6P6Te2WjodzgUYlWCSX4yYjuKxPT5nAYYCY947FxGtk0UmsxCAuA6AGbK626aWKmgJ4BXOydJuwSTOc3rmc5g30YmKD8yIvb-x7Cu_VyFTOESTvREBBCopIAx85d1M9AZQNWc-WL5LnQuHG3gI1e7FxFlRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
⚽️
🤩
#تکمیلی؛ همچون روز گذشته؛ خولیان آلوارز در تمرین امروز اتلتیکو مادرید شرکت نخواهد کرد. آلوارز میخواد سران اتلتیکو رو تحت فشار قرار بده تا با پیوستن او به بارسلونا موافقت کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/28581" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28580">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAOILHjCn8LkXoouW_0_c_L6owpB5OCcNDxc_wzloHgqUMim7sRRlGupo4T6uclGoOpJz-opeySAiLPLLQEemlKQMznarszTpmhA2ME2-Y3ZW6uTtR-RtSopFrkhSgWSHiVcXDvSVGHmVBBmi22x9v3_OZUjVd-OJ2paf5eIl8rx9DX2KvVdYMrqqxf8IwPDrN3kPARGNdYG8gZw-wdPYjILRu-5W_AYho-bFvmZ9pS8JUHYrQR0atkBHIk5_haML_Y3zyVcFATUFeRLU2S19xv7DMmagTEzGqaObimoLxK74SvanMpYtJRCjr0Va1GA0MYcQqqw1xS5jqv3FlPgMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴
جام اتحادیه انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
چلسی
🆚
لوتون تاون
🏴
⏰
ساعت ۲۲:۰۰
🔴
بیش از ۲۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ شرط رایگان بر روی اولین واریز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7=</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/28580" target="_blank">📅 17:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28579">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/odMgJCnKR_mdJjorNla1mlAOfMb77W0x6ibP532vI9KMpuuzMeEHSoG9VIMLR-7EmJeHzDCMcvupcCK2DyCthfB81qGMmct7JJabqHkUF8lw5c4gimYgCobgTVH_yLIB_3k6j8V3AJl74_LbonjT7yiADwTrrjIvy09d3jUaZWJ3UJWrk5zDRgYyc1Iv7HhdAxwNePzXqtC5gec_2dlF16sDpQQvb40Hl7nSecgMWQsizLyOW_k9ORIMeJ2BMUQoAtHC-BIapRYYAqYf5NWA7G9dJArZLvQciB0H354zJvefiEOef9p8rj5cEC0pVOfJhiKmM-Pc-8PY5mMJ27lTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔵
تاییدشد؛ بااعلام باشگاه نساجی؛ کوروش اژدهاکش وینگر18ساله تیم پرسپولیس با قراردادی قرضی به این تیم پیوست. همچنین یعقوب براجعه مدافع راست جوان سرخ‌ ها نیز با قراردادی قرضی به‌همراه بند خرید قطعی به نساجی پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/28579" target="_blank">📅 16:48 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28578">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MENZoSyVQgiTmJE8yP8nNBpwLPdviQtppa8ltLasfIcAu70dft92_UVJeR5hQmO9XiHllXerAkYS6WgQm0CohIPEROcjoMAJKr-1QnI17GgCwq2zHWXm4LFa8vqDJtdnf-3OP7ZwLmym74rWIVl_As223GBXzftRTlTQTCJ_TfdoAcGKIxLbucT9_1X7XGEXskr2WEpDtmCm8cYqG8eXUSBIovCxQdwTnypAU5HOarMVoRHBvJaLxDPYXZC8RqnpUNfVHfP6LqCxN2qopFAb5V-Vt8P2T8iHy-aYWx7NoYUa9dF0dq5W_9SIhNkOfktTnwqNJLnmd-8fEypssAVkAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وزیر ارتباطات:
پرونده فیلترینگ باید در کشور بسته شود. بزودی‌بادستور رئیس جمهوری فیلترینگ فضای‌مجازی برداشته خواهدشد و تموم پلتفرم‌های فضای مجازی بدون فیلتر در دسترس خواهند بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28578" target="_blank">📅 15:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28576">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oufxqEOv6f9pjGeKtdxhUpACgzRUtjGDl32yA07BUWL9EUFdMPnexPXb2w7euG0K375fqmXMTOGv0kfPJmFjs3vXBiQuQgvNZ9aUlqmQ1Jov9VWl0odkfWwz5JJ9NAnjrNmppW8LTqAzZuLmmhSicReTRb3A58B-eP6lMnOd0UswR1n3ajKfnV3-Gt1ToBIRFx1qo920KAhaSg-csTu64rkrMVJufU41FiP9feD30DAALBDRvXS73fziz_3XEzqbINKQZl8tv3lhwZzQq9U0FF0Qh_Qf3AWxBXTHy-je6_B6YxozButwfR9ylbeh6mmn6hT_75qm2YB1y872_Q2T3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/28576" target="_blank">📅 15:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28575">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVp4Ih-_sA4NIWF5GjEzXQvXtdRecjIammqc0Jjs7WrhhaKqlxKF0LJaPJsDxZQpJq8cQw6ztXZJXAryHK5Cdu5X_aGuAEB7FSuJk70SYIqVlatEHIn_BV2viPHLBGgvLHKhCXfalZOX5rybT09RhbquPL6Ylv0j1xmz6eWcCZ9Ty9v_exjhuWCcTSmpke_fDtaHP3heAS7XLF1tjarM3U83zyfq5hvgUevZ6Y-AR9PAKdEoNn4HOFNP4ibcHKaSsJYpxOWXnG1T4kDWamJcTMt1x8gSCaMBsYM06pBxfj3XF6kqF2FENCBfhAtAGXiUpaFRRrW2OMNCNWHguhWhEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.5K · <a href="https://t.me/persiana_Soccer/28575" target="_blank">📅 15:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28574">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=sg48RpIqPpdy2dL7Mj0qXN0uwzFVlAF8bNTF30dlPEDQ-1VREmB2chZxPVL3pNLRuAPGyg96U29mNOwv16jbRtRXlKVDSjxvq4D4LDt1q3Mc3fbI4yqx6yUBRuYzec9JxL4J8NqCelh7yFtejkRY0A5PO7ZtlWuMO10HKhGw_f7vny4qCMJr5v2kymAUX_RMRkgTZwruif3Gaxj5kxl4unugkB250hmRB54gIoMgM_OKA9fVE7lu9lwTDaNJ5mfmJ6Em8R-XjvcXLb-LrJqMtOsNnREqRiq8Zk2Y4tOHd3kg0CLyItH-nncEPbIqIPOXji00Y9ceYTS0v1v5X8RQtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/22cb4cd7d4.mp4?token=sg48RpIqPpdy2dL7Mj0qXN0uwzFVlAF8bNTF30dlPEDQ-1VREmB2chZxPVL3pNLRuAPGyg96U29mNOwv16jbRtRXlKVDSjxvq4D4LDt1q3Mc3fbI4yqx6yUBRuYzec9JxL4J8NqCelh7yFtejkRY0A5PO7ZtlWuMO10HKhGw_f7vny4qCMJr5v2kymAUX_RMRkgTZwruif3Gaxj5kxl4unugkB250hmRB54gIoMgM_OKA9fVE7lu9lwTDaNJ5mfmJ6Em8R-XjvcXLb-LrJqMtOsNnREqRiq8Zk2Y4tOHd3kg0CLyItH-nncEPbIqIPOXji00Y9ceYTS0v1v5X8RQtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
خبرنگار در پایان دیدار با سوسیداد:
امباپه میتونه به رکورد ۶۰ گل رونالدو در رئال مادرید تحت هدایت تو برسه؟⁣ ژوزه مورینیو: من چهل گل با جام قهرمانی رو به ۶۰ تا گل بدون جام ترجیح میدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/persiana_Soccer/28574" target="_blank">📅 14:46 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28573">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XchnbTvXTYoB0kCW5nyoMAqF0GN21ESWX59A4FEOLwAWf6-yPEQRqO3gTpNNL-FzWJNY-cMnH2QSz0ip6tHLtmY56VhPWyaoIBVhAanqfJwCbQH9PGnp7uu9lw7jtrbm-I3HIuFaJjMga6mwQejBw5h6Kh8NsyMI0mWxqM73R6XCtHMBQ7LzGqwz8-T0JqNO-uMxcHcC4xilzAP6-JUneexnuwL0z3hg-2LhI2NQ8FhZWFdK-Md0JgBB6N1rLgGPgHWhulB4X2ddW3yWIf8SAvF6BCpfoWRqwOLSu9Iolv4ITUEU0CbCjK-U2uhO2iWupApq5f6H5GazLOp0B826gQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
زنی باطرح‌شکایتی مدعی‌شد که توسط سرایدار منچستریونایتد در دهه ۸۰ میلادی مورد تجاوز قرار گرفته. این سرایدار در سال ۲۰۰۹ فوت شده و شاکی به تازگی شکایت خود را ارائه کرده. باشگاه منچستر با اعلام اینکه این موضوع ارتباطی به باشگاه ندارد و طی این ۴۰ سال اطلاعی از آن نداشته، بمنظور عدم مزاحمت این زن برای خانواده متوفی مبلغی را جهت جلب رضایت وی پرداخت کرد و پرونده بسته شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/28573" target="_blank">📅 14:12 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28572">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVZXBHjN-GhGJk-QxdZvEFXg8dRv9kvfdAh-jgcEmt9vwVk7Omz1oK5aqtMWHI8SSV2B2K4D0d8OtWOmsSo42qRkARjlgF3hTAePvkK-9LODkufAUew4l_HjJcsQVYgN4kMgvIlNkPIz8LUfZRZPS6VPS7gq50abq2nza7DzEJpr3t8q1dJnyeRWuURvaxRslF31k8fDdXTGlS0LlhYA6Q0_kQq5F_G9dYHuJrMvMVtceaJgZcrau7FwHmFUvSrHMjzLpsmnGMoG-UUzPY0tBsy6NKZ2yaUSODZF2pyt90e00Wq26bps5Lg7RN0HO77Xicg4yrSdK3bR8EZ6-A4zeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
⚫️
از سری اتفاقاتی که فقط واسه تیمای ایرانی رخ میده: استقلال قراره تو هفته اول لیگ نخبگان تو ورزشگاه السد میزبان خود باشگاه السد باشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28572" target="_blank">📅 13:33 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28570">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TIRMan7XSTT59p1ZdS7aNxe9dXN30qqWqJRwcnf9VqbJRy_G35PE7LdJ-4Fn9wRWwH_Ajeu-i_98MalouTij01i1mJEyZT6YwQnqgPc5KStA8c4_Qh-fGrhlx6n4STepjJVbYiXZ9NL7nw2IJmiXe32so88Q40bgxhJKJgENl-Ax5BmzLtjp23RqjtL9VVpb8RbBLdCoJ_W1hF5n7kgBgZJdoTruB8NEjto2jZ8cCTQZDMYejPn0KB7jmGWteQa9nB9nQ5V4CSv2incv7lf8ORIG42iLQnJPS-wrtJeSZUsjZggQ-AndWNMG3NrfN6sjLrRBFnj-R7ZX-vfKd8mXgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/geRkUXAOvhgyFsPgFprG2DnSHVyN68gAW78bMTRA4Xs96Vicr5NR0Un1OJaJrPvubFNW9y3Rz_jDRaHTh7L1Wcz8q4obT8ATzuwRfUb21NROII49d04F1UEYk9O7XTDnW4aTtVsaqwvLnDLVcQGs8bjZexKxt9O_dNuSL31-0489LVN1NDAMBEjkMabM-7cbB0hrByfFrY_FwW68uh3aEvYTu30h888CxUVexHr1DeWnxQipnM7hM0WOEjgE63LBZNjEhgm-pztlDlkRp8fJK8GlStSJwHZQ1r-2bVO-tzY_36mfXMuZB3Nq9bHGoGhvZsDeioInODGTqOU4YwvReA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
باشگاه میلان بعد انکونکو؛
ساموئل ریچی ستاره جوان خود را با قراردادی قرضی تا پایان فصل به کومو داد. ایجنت ریچی پارتنرشه که خبرنگار شبکه ایتالیایی DAZN نیز هست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/28570" target="_blank">📅 12:41 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28569">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XMBLXVl-r7QZVPNpjoMgMVr8JauDM7Hh4rhwf6rnCLlH_z5_MSBMQCCzSmma_uen-IXdJ0Y1Uo6hjNJemzGNdPka5V7NsQTZBBUFwqBCMFNnIA6gcwRrayv6mVPuuubcIm4x-BTt2wCM3GJ1NQ95U_-pIoQ0YulGbkGb6NvCMaRRHDZiD2623PQyqKoDM2sYORGVbCs2B3_hqv-4kt96X2yiAHKkIPeJ5LHdHs6OXvXIGXUsi4WvDcRVNxYr7nZ6aAhNiAySG4StOIn0edKgi9AEhJseHU6yQcMdNuz7n1dw_NsNuc10ze93Az6f0s_1xR_dJmzMKJ6bs6oPw9aAIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
باتلاش‌پزشکان‌باشگاه‌ استقلال؛ روزبه چشمی و جلال الدین ماشاریپوف درلیست بازیکنان استقلال برای دیدار فردا مقابل مس شهر بابک قرار گرفتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/28569" target="_blank">📅 12:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28568">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk0GgKYQLgbviZm4mkvsxi8qTpgKNVX33HD2YEnGod4hPvdDaZg-w1ZFXeM5HBKiytqsDE-_-_goVEcRfyVUJVjt5TF_x9yAsd5YsrMrLnt6t0CPv9ZhUkUioT8Bly2zKdMMrT8Zc5QDPNc7M0EoM9JZpwyyy5DHlBHW9KGhOc9MrmRmAsRvmpk5C2t2vl6VLH1n8e059aUVTsUlMqSzFqjfaN5suhzpxIBy9Tj5iywtQy0HRavJrYdTEH0sdW3HoSj69ofMx6TQ5zWPZEFyM9xYR5HVHNV9UplaNXvGBxTlZVQRE84I5nAtPvf0LFt427EoSXoc4CJ0V9zzjVRm5WuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b570a2c1a4.mp4?token=bhvgevVE9RbCebdCL0eQ9ESGMDBfcVJbem91O55WS4MdVQVkZKfrD_ryg_21GIaR680pVVjUlSykGdp8Cmh5NVUoKQ6CqOtDJnXLQ3D0TZZehoLwPxg-yQQMuL5iMuaaTHVgvgJ_-wbQNsIQcyU9Aqe4PWr1PE1LnGDZ-Ykg2j9EvRSQMA-OiB13xZMh707NRdp537OgIagqfmwUZKAKIjWtG8zECYHIPwEudEUl_s9GoyB5M70wH6UeBLxmZ-WqVXG31NIOGD5ygKpDZK6_qHyl_ccP1OLJAXqjYVtfgWPbXFwKQm56-XQJuung_VKdCfJBQaKqGsjGja_us9VLk0GgKYQLgbviZm4mkvsxi8qTpgKNVX33HD2YEnGod4hPvdDaZg-w1ZFXeM5HBKiytqsDE-_-_goVEcRfyVUJVjt5TF_x9yAsd5YsrMrLnt6t0CPv9ZhUkUioT8Bly2zKdMMrT8Zc5QDPNc7M0EoM9JZpwyyy5DHlBHW9KGhOc9MrmRmAsRvmpk5C2t2vl6VLH1n8e059aUVTsUlMqSzFqjfaN5suhzpxIBy9Tj5iywtQy0HRavJrYdTEH0sdW3HoSj69ofMx6TQ5zWPZEFyM9xYR5HVHNV9UplaNXvGBxTlZVQRE84I5nAtPvf0LFt427EoSXoc4CJ0V9zzjVRm5WuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیشب گندوزی بازیکنی که قبلا مارسی بود در جریان بازی‌فنرباغچه و لیون‌حسابی رومخ هوادارای لیون رفت از زمان گرم کردن که فاک نشون میداد تا بعدازسوت‌پایان که اونجوری خوشحالی کرد و دیگه کار به دو سه پارت دعوای سفت و سخت رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/persiana_Soccer/28568" target="_blank">📅 11:49 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28567">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u53EVKJo-lyT4TltcXHLFU0XNm7VE05rPV20QX4-X0rKO_Xt1yEP8roJIvN1mM2ZVuoFrNTUCX0JuAzI3bLxb0S8AKj-iKrgOv9XJjPWmYXuDEp8Un4HqCPLEYl2Y_aOERoDYxdYHZQtKVZ0C2uRPSxEEytBNgUJv_1vpUPXkIshoEOCPETfEvECNTidkseXXaX_v4MMCptzdOtura8PpAn9ZwgrJRFL8zs7TMT_pi8NDoLiZAOY1KnA871fdqEdGdQdCb2-_ae5fOBUjIWZHbk4xBwtSJzq-OSMKQp48RAzUF40llkisb4bizFLRBAcVsei7EJ0UWqU807kbDLeog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/28567" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28566">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJnSVoSXAE7V46EpnD6NQsgJQOSozbCLL5ttv6Kyf8DhPnKFxtDzX-bKQ-F2frVF_2b_ZY-rxVE5zLCeKew50HZgbrsc91ivg3MtD5jeKDmqSeNRhvHGfD-snT79QgfAX29Hv0G_NvGZo08qpQUu1LB1az28c2Gacyntqni3Mv6yvNq_YxoJ4KJzmZNavSGF3riZgWumuZ2vjXISIfeHGHrr9zYTyMsScBNT5qYY50wGCdSz8ljXLJry7pEHcN2-s9OJ_t0rvcku5rXVdEnNDmzD0RCLiuRnEdt0p3D6o_cBqmK5KIOAo6k3ZXuZYEpy3jvrG_DIANc8Xf6NwUdHcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛بردلی‌بارکولاستاره‌فرانسوی PSG در آستانه پیوستن به لیورپول قرار گرفته. توافقات شخصی بین او و باشگاه لیورپول انجام شده است. بارکولا گفته‌که‌نمیخوام PSG بمونم سران پاری‌سن ژرمن هم گفتن لیورپول 140 میلیون یورو بده بند فسخ قراردادت رو فعال میکنه. لیورپول…</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28566" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28565">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qDg_cuwJHC2gzElGh1ja6ZMgPg9j2XUnyfJTOxDP5FJi4e58FmlnFOB3rMRczQP_goINe8y800o3OXAEWKF2NWc0YtIg7mT2jxSmMF_j5CH9HFmQdpAi5WDE4d6DVBMRP8ocfRw8eKEzv8sXg6vd9zX6FzAKsMiW6W12y0nDIIE9RJ5QAFPCLOxfS2RAmF6xc1-B234JCXYrid8sFIUZDHb2eG8oIed5Swhdjyrq3O5zPnrGoZw-h8Dm-VAJm_wP5gsQf0GJwgDWQyF9Ae7JCDxzdn0ayDJCWj_G_2JtQbVFQOgC6FoJcStgjOs81MIEWjbmx0q4sLkhITRFIJ4zwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
سایت جهانی WePari
🔥
😃
😃
😃
😃
😃
😃
😃
😃
🔥
بازگشت باخت به صورت هفتگی
🔥
پرداخت جوایز سریع و امن
شارژ حساب از طریق ارز دیجیتال و انواع ووچر
┅━━━━━━━━━━━
🎁
کد هدیه ثبت نام: Wepari2
👽
ثبت نام کنید.
👇
📱
نصب اپلیکیشن اندروید کلیک کنید
💳
آموزش شارژ با کارت بانکی
💸
آموزش شارژ با یو ووچر
💰
آموزش شارژ با ارز دیجیتال
🌐
آدرس سایت
👇
til.ac/0L4vyJf
til.ac/0L4vyJf
📲
کانال تلگرامی
#وی_پاری
:
✅
@Wepari2</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/28565" target="_blank">📅 11:28 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28564">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🇪🇸
🤩
با اعلام رومانو؛ هکتور فورت ستاره جوان بارسا به دلیل زندگی در اسپانیا آفر دورتموند رو رد کرد و با عقد قراردادی به رئال سوسیداد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/28564" target="_blank">📅 10:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28563">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=ikUr6_x0pFPzyFlXm19h3264F1Ake3LsZzJMtlJMGIniN69EtYREAgVY5bbc4IYkZqjWgrX6SgqKPvVB9ypRfED0dH4A7CKaFEYsaVPtMTYakzC1qMTkQ93VOaYiT_XDxWmmQsaeNKdFzHHNGquWKmkkmmsTJzrwMqlKSN54kTFg6-f6uUrUOItZmIOpQY6o0YErZHP6c1PcwhbPOtxncPMzeVRuc_KhcEO6fxhrHhiqjuR5Yw3Y-JkbuMMyUCfVGnmq8RnmvxV2-mNCHieoB0gR35YPcA8jLpI3ZtVpTpQ9pPuamUC87LL0TGtEVdf-PGgIQgE0mTf2wMDqv0QwlA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed9d6f5b21.mp4?token=ikUr6_x0pFPzyFlXm19h3264F1Ake3LsZzJMtlJMGIniN69EtYREAgVY5bbc4IYkZqjWgrX6SgqKPvVB9ypRfED0dH4A7CKaFEYsaVPtMTYakzC1qMTkQ93VOaYiT_XDxWmmQsaeNKdFzHHNGquWKmkkmmsTJzrwMqlKSN54kTFg6-f6uUrUOItZmIOpQY6o0YErZHP6c1PcwhbPOtxncPMzeVRuc_KhcEO6fxhrHhiqjuR5Yw3Y-JkbuMMyUCfVGnmq8RnmvxV2-mNCHieoB0gR35YPcA8jLpI3ZtVpTpQ9pPuamUC87LL0TGtEVdf-PGgIQgE0mTf2wMDqv0QwlA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
چند حرکت فوق العاده خفن و البته ساده حین ورزش کردن برای درآوردن سیکس پک‌های شکمتون درکناریک‌رژیم درست به قطع کردن قند مصنوعی و مصرف کم روغن در برنامه غذاییتون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28563" target="_blank">📅 10:20 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28562">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">‼️
این تیکه‌های فان داداشمون به امیر قلعه نویی و مهدی طارمی مهاجم تیم ملی عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/28562" target="_blank">📅 10:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28561">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQCYzt9Ehq8so-VudfZyUBoweWPxlOBPo3nJRw3kBRVjiqz0hCDAIE1UVs1R6yPOmSBUPiayJMMWRgHZ81Fx8YtsZuMQ7fzsvR7aoCiVnyKHyHYZhn4G043SHHzkSnzgiODrg1yHcsFA4jWn6JwkO70QnC956v4w0P2ZOfR4fBKJ_mlncsuoJvqk1AB7orFY0AOFDcbkDLkH0Cwps-U8b8hUcuCwAfCOBMy_XU5Q3FRt8Q7LsVxhptnbd-BJl5x94fvM8G4hfXk2reOi55VndCXsGkdyPwqTf4XOpA_Jr7ynkXghLBu6_7XKzCJc3e6dzuIqx0k1jbHJTpV2gWvNhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/28561" target="_blank">📅 09:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28560">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pn_ouAP5_lfoBCi_H3HHqJNt42TPg2w9rMpsLyzG4Or5D9ytntoR1AD8Ade_cxBEhvYSU0tMyhW_87jBY6L4DEXNaH63k1q759JVAxL2RkOAqmEnHGlkRFI3neis_XXSvdAZIojaIhavLqKe7lU7l0VnBWVOOnQwz7dC_ZLL1v2UsJYz-hNcoRmEf0dURaY_YTwh9LaALHtBcGo8NSrCjeuPnhDVWwqVfIqs0Ua8eFHe5GnDcDCF_wBVQ6qjpEY7l1JeYH50s94CoJ8iULDiPLUj28bEOI3CswtehHmEWGReQXHG5ZwLZOO0JmCk4JFAQ7PpnyHw3myumzProBNJGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛باشگاه‌تاتنهام‌امروز100 میلیون یورو به باشگاه‌منچسترسیتی‌پرداخت‌کرد و از ساوینیو ستاره 26 ساله برزیلی جدید خود رونمایی کرد؛ سیتیزن ها دراین پنجره 12 بازیکن خود رو فروختند که بیش از 400 میلیون‌یورو سودخالص کردند. الان هم میخواد حدود 140 میلیون به…</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28560" target="_blank">📅 09:17 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28559">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vM5MBST3iUJNz9Z6YNlSgdknpaxEL_iurgrQsHujR4Sl2exWKFbWvSNHbd4NYYoFvyrSiMJU9GbAHjKxKPczthG4_l-auV02mR_Arazk0Vq16lxw0iBCxWc1Zxk6PT7G0zWI6fy2GO--IRpwmdUJNf6AD4Z_JZOEZKle0EmZGXHcH2Skulw_KlS-l7bigKiHp6uvKuKqybNyiN4qOLPNXmYcLhVyhtTMW7d-zhKQGQzPONTQGVMCFejocPTUGhtGv_zGy2SWz1yfqbT3HtmzVTjAWB8l-dQ9Ygq01qe67i5C0tDD9ScRMAU9xQbtXn-aek_l6_fmIGAguxyWGHR_iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🗓
#تقویم
؛سال2021درچنین‌روزی؛
کریس رونالدو فوق ستاره پرتغالی سابق رئال مادرید و یوونتوس با عقد قراردادی دو ساله به منچستریونایتد بازگشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/28559" target="_blank">📅 09:05 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28557">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrUQhcIgc5eLv20bYJoHQA4fG0WQKu4Xdn9bTifNq1Sxkvxj-dt2IdzOc0_RwRJtC6a_G9dlDkHKZInRleXB9-I64Vjqy2Vp8GbOAoUzAo0-jBp8UyzH-_yki8e2wewFkdT6vrx3tL9I2APLIq58sMY8zSLYoysxuegzSNMA2U85RCBpZXcTsmS8_dCb9AeCdxRTa7QaXY8A5ALX36lKVVa3xpuuNZewgJrI05vCIOXHp4WOZbKlrl4S-F8cKsrFWFpgKuUQV2Ult7y8KyGzx1mcJL7EcuIdp_sdTzpAU8Thof89MT52xaaedvOoDqy5szsCNLgKwj1vN4BHTvvHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌‌امروز؛
دوئل‌جذاب‌تیم‌های هانسی فلیک و ادین‌ترزیچ این‌بار درلالیگاواستادیوم نیوکمپ
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/28557" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28556">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XcSARUZQndfOQVle3wqaapNThP6Jq3OcbpXN12w35bO03Ipj0Rrxzu3__AzhLIykBLNEhjTBK_C8RSbXhkcCXKPn6FC9iiOsZHrXtZoo3q821iqYl5vKXAzKhm9e3adEAIGgXjXxHD_fuiEEcdPvW7unEs8DtXbBSERXAoYXbtycK-3BIKQC2Jz6Qq2N-n3kmAeIY5WWi3wnjROWBz6AkiIFfIOQa6JLWvRlBaZfjaW_dlnTbcDhfGFZXXtHBsEWHf-SEen52YDdFwlsR7x1psaewJrb3BDo4e_GAVvoP03Q6p-OEOm25SJX3YOzUECi-Np7uPaMIZpN_2yTdt9BLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌ دیدارهای‌‌ دیروز؛
از برد رئالی‌ها با هتریک امباپه تا صعود یاران کارتال به دور گروهی UCL
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/28556" target="_blank">📅 01:57 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28555">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=j5TYWgb28XqmLYunguyyjmZut_ljkagmGjeqZbi1h-9PAROAxCmA9iv3Hkwmw-ZuS7XHC68e9vzbDrQCDCqGmIRqn7JYtOkc3Q1yCvVBUhev6PGIoLXnRkNoJzX0svC61yr9a6ZOrYDHIgu__c2v07JzHckhy9hPzfOz3KQyGUHSHDVnYjJjoFKDvJoJHJcMWgXgHV82RxO0kOzF25yKo5oB5im1lXWcCXmvn6bUwR_aVUWIW8MdT-4lL1KnEzLNyfH7dR6f1ZHl3mKszz1N2feHlwtr9kvDoRvAceBU6adIrQpeP23q9UryQeSTTv_SxDmCjN2Bw7Mll3W4NOVHAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60b5eee892.mp4?token=j5TYWgb28XqmLYunguyyjmZut_ljkagmGjeqZbi1h-9PAROAxCmA9iv3Hkwmw-ZuS7XHC68e9vzbDrQCDCqGmIRqn7JYtOkc3Q1yCvVBUhev6PGIoLXnRkNoJzX0svC61yr9a6ZOrYDHIgu__c2v07JzHckhy9hPzfOz3KQyGUHSHDVnYjJjoFKDvJoJHJcMWgXgHV82RxO0kOzF25yKo5oB5im1lXWcCXmvn6bUwR_aVUWIW8MdT-4lL1KnEzLNyfH7dR6f1ZHl3mKszz1N2feHlwtr9kvDoRvAceBU6adIrQpeP23q9UryQeSTTv_SxDmCjN2Bw7Mll3W4NOVHAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#هشدار
؛این‌ویدیوکوتاه‌از صحبت‌های مهم دکتر علی کرمی مدیرآزمایشگاه‌کنترل کیفیت مواد غذایی ببینید درباره مصرف آب معدنی برگاتون میریزه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/28555" target="_blank">📅 01:44 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28554">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B1oewQh4HFdQ3CrWt0htAqwQvn13h-z3X9KoW_NQg8ANRoZbvvCW2uhHQgJDQPeepq40y4HWapZxnt6QSpmpGuvY4LRCn4YxP1D5qy2tWjW-OqwPIJSWjrCsktYm5cNfSbr8UHcednMxEj1ndC8iwgbz3fRO3loFJ5PbPVqMmneb_zz49PFMimsNmrBrlEI8XVoCvQ6n70bFclszDVtowQ0v9TYLmViXiQsoWmff3i-EBSXD9ELiSnNMsM5THvxeO47p2v6b8TLq0XPs6ouYCvCzS1o0x9kx0xNXjuGbhm_wUDi0mD9KiC8TjtWVO6iuREX68Vv7iOMol7SOeyxkkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/28554" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28553">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uw7X7V5TnRsIseQiEwkSubMo4MgmaSEa6eC5rUjVaOqFS0TAsdO6lCvC0wPwh6dp0To-MYySyd2Gci68d-70YXGIePh2ECdmJBts5Ps5Qz7MMq2lG4uFHvNtYlKiSEbe9CaZ3cmxtM_zi1L1w3KhRjtrF4DBnwZG3aCG8bdQTl5elbgEuKQiMWr9BdYhFDVoBA5jv4i8shRQUJUk7UvHRLQwKpeAI3NXPOQ2xFW6t69kgT_8sGqvy0LQm6YqSaSiTJH5U1eB8dBnsTj2HzRf4G1Jb9LkrZL2QXizmG82aUPbObx3NmYET6iq7xtbzSqfetKt8fQ_r3PTzI8lwMiUxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
🔴
#اختصاصی_پرشیانا #فوری؛ مدیریت دوباشگاه‌پرسپولیس و نساجی مازندران امروز بر سر پیوستن قرضی کوروش اژدها کش به جمع شاگردان مجتبی‌حسینی به توافق‌نهایی رسیدند و اژدهاکش با عقدقرار دادی یک‌ساله به نساجی  مازندران پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/persiana_Soccer/28553" target="_blank">📅 01:18 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QSkJ40Hczt85JLfIPnxTayvgy9eVIlxWA3_mXgfDYq4naW53X2XCwMI_Ije7ZweF46T-1gAffWYuNCEy6bKSZo_8jZI5D_NBBkpc-yLV6dODo5lkd_09vzdOttls7HHaJ1-zyn8xTt5NMqY9WSopm5Y7VlyxXV90B1VChNNPKyTZ_x4FhOQLhJSPqiz_Z2Z-TX3wv2C12xLR7-xNNZtbFm221Zydzj49pgqarm9a9GSAoGUwI4qMI4xJvdks602IiQQ9-r_OKxBluehkwJK8Mw36y5FDRW2OTwZXrlh-jJGHw34wQXezNw0StfCJA6KsNZPFNlsCLyofOMmrClIh8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇹🇷
فنرباغچه‌امشب تو بازی‌برگشت‌پلی‌آف‌نهایی لیگ‌ قهرمانان اروپا در خارج از خانه لیون رو ۲-۱ شکست داد و با اسماعیل کارتال به چمپیونزلیگ صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/28551" target="_blank">📅 01:02 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JwYu_qbR1MGyeRZgK_Wqex7Ijt8dP3I6yvd5wfazKqKv6ZIzwNEwrAXpDIuG90kZ0isfNKYY3hRyv2iCUglL4NZr806pqY49dyh1xiNs-M1SO1TOISQOt6iDv_crql_mvF-DU35bA1VjJod7SvZraAioQfxNfcGtyPpxoCelRhlvu6I89WLZA7VZ5wgVelvp3uGkbfTdhjCNI2b5WWH5OGu1MjX2aerNsse4OrqdQ7Mncz_T0xFLDcmK8khWLOu-Idp9nQHUYmVyhlVCz1cYbJiiAU_9i4pr--olOHsja_-pKi0lh_ypYD695Yl21HJtSr7-ncfRv0OfIgzuKhKQ0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
شاگردان مورینیو در هفته دوم لالیگا با درخشش وهتریک امباپه چهار بر یک از سد سوسیداد گذشتند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28550" target="_blank">📅 00:51 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D3nDx5oI5zHpo-0GOK9AAC79kdtw_5xhl7CZbT6cuTuJ73PfJ8fXLfLhbZwSum40AqYmxSJlNQuwG-s1W3JIaH18OqEDQW5sRYKkQ_wihoYsdKnhsfKL9p79By_9fq_M9hfzof4rkmKTsKC5DsH7nWor_VRbiJzw0bchR8AYA2y9fwc5nGWMlZ4r8O465bxDnlZjtrWZTTGC5Iiicbw57DZ_aSotEpAKq_hMNTr6O0xwSzyDqbJsVSGov234EkqrBYozuQX2V9tbup0K-ropjTJyw291y7h-BE4ZnI6yvudpCAX7CVtVwpI6_sISQSiARVcO7I-1b4_kXAqwBydS9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/persiana_Soccer/28549" target="_blank">📅 00:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kSVFWt6DjSgeuqySUSq0XKh6_GnentZbdeVLVecDG4k29tiHh8ZQBgvdmHk_CKTpG_af3Adp1JNnW2CiORgWfItrWiVGZDP9xdEk5MBI4rNJbvgGn3B5PrtRrYbTKIrFjVdq8PvLVyiseL8es9zRzh5yXA6f3u9sKWbwJa-DiWwdiuSJKlPeko8hXqyhZCbgJSsPJd_WBoL7m_8YE0ASSMTZVWyHm86gQ8obOC-ZI_qA8WQrgmwPRv7-LkHBWvxmUOg7EMer1erCwctKuKH1TSKwmy6pjVOeZY24Zdy4Bd97Kwg3mEH9Iz_cniHWfRbzJuv5ksTdoTndjOxr-0f5dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
راس ساعت 24:00 روزچهارشنبه پنجره نقل و انتقالات تابستونی لیگ‌برتر فوتبال‌ایران بسته خواهد شد. بعدش باشگاه‌ها درصورت جالی خالی در لیست خود میتونند که سه تا بازیکن آزاد رو جذب کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/persiana_Soccer/28548" target="_blank">📅 00:07 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">‼️
ویدیویی‌دیگرازجشن‌فارغ‌التحصیلی دانجشویان رشته علوم ورزشی این بار دانشگاه آزاد تهران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/persiana_Soccer/28547" target="_blank">📅 00:00 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28546">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3K2eAQ0uQ8LRhFVHU7bmigqTAAOmB0oKfhqAcvj-2R9MtjsDmAKeSI0_HiJSNFTqcHbMGHbuha5nGe_YLJXRbBoM-14zO35mtNQUme4VqlAGkA-XkjY4ol8bnD3hidDOqb2e0hMan4ZbG3sqn8aUbZ7WOMDfjW7NKyOqbgO9NH48Yt8Np9oRuDjBU1cpD1GqOnnUPYtm3IKK7-l8XbC19r8PJI1jOY9Ve-qmYkSH_5zxjLjcshL4H6741CYZyTqZg7Nf9VI47qtm8Giz80_o-ALra2n33OS48p_4PuU3Y-CF3GYl5hdu2le6CzJetGBXOkVIQyHj2DKExtapMOJxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای‌هفته‌چهارم رقابت های لیگ برتر؛ شش دیدار روز جمعه برگزار میشه، سه دیدار شنبه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28546" target="_blank">📅 23:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28545">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fwk0ZIzwDJC30lFpBRLX--b5Ikx7Mo8P2bzQzuGpl4dRnHr7ETVk69CsEgfXhoSPj-wdBFtao1Fa8FtVY02Rj8Vmbeq5Bv5tKsDVlznNFL7f4Z-jIjg3SXFyhO_HklS0RpXE2-Cb3XRzX5e8Rh1GmSETvMKkfgnWj9O6lRPkZb3Nn5P5VrSf-fMPELM-mah1iy1_we8umvka8Ij1sItH-2IGZkpDOWsAPQMPOD8eKcEiUoktY8zDR3ZQowzGjs6G_GHPRSAab6sE1yovOg9vFNUGsGgsUf0evaA2c06UkYCpvuqQ6Me924nYHeU6vUusaYV0pb7rVnaLJQNmdgIR0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
طبق‌پیگیری‌های‌پرشیانا؛‌پاسخ‌فیفا به درخواست باشگاه استقلال برای‌جذب 3 بازیکن آزاد بعد از بسته شدن پنجره نقل و انتقالات تابستانی لیگ برتر منفی بوده و پنجره ابی‌ها درنیم‌فصل رسما بازخواهدشد و این باشگاه مجوز جذب بازیکنان مدنظرش رو داره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28545" target="_blank">📅 23:23 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28544">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🗓
#تقویم
؛ 3 سال پیش درچنین‌روزی؛ لیونل مسی تو اولین بازیش درلیگ MLS این گلو به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28544" target="_blank">📅 22:40 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28543">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KEBIu_0wArbhoFXMLUtmt60ZGYQDZFF34bnx0Ap1dh1sUS5MTvYqnaVfmQJ9kG0rCxQJQ38AGxuE3VzL2lFSypK9bs3EAGsKKsNMiPXDdjER3-Yt_3NvxSReYd6svo0cZllZknICPFV5VdvUpsMni3XpbR_TtvEnHn6WnoMZl8yztaGD3m44fOyYLPHjkbItqzd4A8o2Fx17OvYv47Ndg6L4OiVfrS1zea9VzkqkEZKSg74Wtzwmh-G4YbpQt96cf22ddE8zE2A6z6Cu-39Kwxns_F8vx9X7nLRFpoSqYWFjccCOpEOTvE3LXCl4K9gPlE07GDjJlDOC-mNuXgXaQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تکمیلی؛ اولی واتکینز ستاره آستون ویلا با عقد قراردادی سه ساله به الهلال پیوست. عربستانی ها برای این انتقال 60 میلیون یورو هزینه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28543" target="_blank">📅 22:27 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28542">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=fDk2-3hqXGwhAKkxv3r6QUKjMGmwiYB0_RLejsfltkc7ZibuiqqVCXYBiCEHanOWqCWXUPKLOwjxRLr8djCEp8Q28c73ewDyhcrcsBKLwU3bAIZE3ziHJg-pg1Svo4UMRIEat9kwlgItXGSJ731egg5KGlDaBkssgrKz5ctSHc8T0RuF8Kf2i_yBTa08mJOK6WMDDjKvAPcc0MkaJqVY_R2OFuNw8Gv7zxaHSRLd_ZT5OEFaJImjWXwagvLg9ev6T4hFarjvy-VH4w32hmjhXEaSMWJbi0M9Ly2vqEzAmzcImzy8A7AqPq_gyYRfavS8SppJ5tiZQsrOroMNUPt45A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ad00b2ad3.mp4?token=fDk2-3hqXGwhAKkxv3r6QUKjMGmwiYB0_RLejsfltkc7ZibuiqqVCXYBiCEHanOWqCWXUPKLOwjxRLr8djCEp8Q28c73ewDyhcrcsBKLwU3bAIZE3ziHJg-pg1Svo4UMRIEat9kwlgItXGSJ731egg5KGlDaBkssgrKz5ctSHc8T0RuF8Kf2i_yBTa08mJOK6WMDDjKvAPcc0MkaJqVY_R2OFuNw8Gv7zxaHSRLd_ZT5OEFaJImjWXwagvLg9ev6T4hFarjvy-VH4w32hmjhXEaSMWJbi0M9Ly2vqEzAmzcImzy8A7AqPq_gyYRfavS8SppJ5tiZQsrOroMNUPt45A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
رسانهTRTاسپورت: بعد از جذب لوکاکو، باشگاه فنرباغچه‌بدرخواست اسماعیل کارتال سرمربی ترکیه ای خود خواستارجذب رافائل لیائو شده و قصد داره با آفر سنگین او رو از منچستریونایتد هایجک کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28542" target="_blank">📅 22:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28541">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gJuUs0OL8iR0TW9WSahODDGFkwmsx8jAZYJS1iFMej1foi9jb7DZcVBdTz68Ushul0OHExcvSjCcPyx8oAzmcg-vtrWlCNJaistvj1W6OdmTUFvutsD-8p_b9_zVwlpk1nhO2W-Fqiofqsdsx-DUxwUn_QjLZPEHTM9nYD4RXu5Y8mmOhLTf7wrGXRGKdAS4BtnusjG3JpYeJn8hVLe4b_JF3mHGi9vx0TeD312jGfBjlL1FRMG--uxbWxEXDv-S5KnFdUBVZxQZ9mVG8Tih_FlRoEoNUUKKHzeBlZHHELaOqGwfVTaIrZ17LRwaZJs570hQRZPRm6JEE5oVADM98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
آستون‌ویلا با پرداخت 65 میلیون یورو به چلسی نیکولاس جکسون ستاره‌سنگالی این‌تیم رو جذب کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28541" target="_blank">📅 21:41 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28540">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YbT91QeIpwgVknJUZLE3xN0moJurAlpaMHl_vd7b3T7IntDq07-w4raD7fJzDOX_JEyeO9ZDhyBgLWMo1hhp5P0Zpwm88Sgj6gouYrDblhsvCy5GRyDl2sF97sj5Wchuoog7BhNV4IYZi7xW_tGOm3jIkvmwCwrn3yIvQ7h9P9QvzG7uM52mQ3waARKIclKBNk1AmRf7MwY9e5k_9KihMJBPEF9Ceru1UwXSCANelLJiaJaJ-zkGKcZl-Qx_cgjkF44Sf7xEsLDhfxfGnP1mbos2bMZXuiDqqx_8fpGS2OZfuXd5PHikDDrJAiRJ9dkl7G3UDnEIcjaLNkEg5WJNuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌دوم‌لالیگا
|شماتیک ترکیب رئال مادرید برای دیدار امشب مقابل رئال سوسیداد؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28540" target="_blank">📅 21:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28539">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TIT6SqWLICNwMlCVuuoybLtYxL0pushYIWz706cPNgFoyTTuiUNVYCD6cal4V7ihuMA83T6XdEu6LldxT0qY-rE_vfy_ZeDxDYPtTdwe28OCJDJMTy73nOgEB5rIf_ZEgSc9Vmn80qcSMUiahHjyd2TchZqRpOT9XvxWaRVJcZuoD95rLbw8LrdJyM3Pz0oyuz5Udr1lDq-7bA9JscOQZpLqLWPlfgjg1pMqTL3rJDA-6i9dBsJZS40E4OUNM42DfaLn9AXeB9MHOL_xljwSuEmQKkCJ9tPrch-GQy7jN9HVTQdTddL7Ekt7pSHqtUpCCHQn9FhmBZe-GOxGyD-hgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛مقایسه‌قیمت‌دیروز و امروز پلی‌استشن 5، آیفون 17 پرومکس و سامسونگ S26 اولترا
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28539" target="_blank">📅 20:53 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28538">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EKI8LqwgiV32gM_NhIaFHWwhN_M2DReg9b-0zOmiWtH9c2ofsvd-G5GjiiuoVDrQJq8wzWxvpFvRsicf4ceWq9XQpveuckluOLsuSRFa-jk7n13pBvFb5FFJ2LICa6QaPrUTyxsz6u6atdkI02yWKoK7kCDK7c5dtj3xPxlCOXSXhWgig7exRM6_Y9xhMWGyYipXOroYjgSP3xjCe_ReG5cFI4vnPhMkb3RIR6bSU11EWv74d2J4SgMRvaAtNe1L6CWruS781Xg0RqdGpxGZfKS0EKC6VGMwumA7wdK5TCyZKTsk9oEyXR80FmA4rgasFdDCXKGuZGyafQvmpQVt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ خولیان آلوارز تمرین امروز اتلتیکو رو پیچونده و گفته دل درد دارم نمیتونم بیام تمرین اما یه‌کمپ‌دیگه‌رزرو کرده و انفرادی میخواد تمرین کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28538" target="_blank">📅 20:43 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28537">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/03aba91807.mp4?token=PVc57LGNEbIetu-5Ujk3zEX6hEhchbDE72uRzzaIVaK25zwLn96qG13Zv1yl-SCmpMr5nI9UnR-simcGdSt10x-XuxYexepVVtOUJn3n6Mzakw86VKIjOZ71B4vXS2ujmDoKR7K1ly5feHxKYqYI6KJfi7CQHSoTAK_83oRI3sRixligluY0FOfh0G9GkO1hI2qsz8XCr4IonahxSg6dWsMShVsld64mbrerRiLOXyFxuzMra-lEnD1DUEHR5AUzG0a_63RDbctVI0yZ_0TK-jspviea0h3Ap7A0GPVg1lfWu8KvN5TefOnKcK19jLRPaW3DVXp6z0hf8POx6TMr9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/03aba91807.mp4?token=PVc57LGNEbIetu-5Ujk3zEX6hEhchbDE72uRzzaIVaK25zwLn96qG13Zv1yl-SCmpMr5nI9UnR-simcGdSt10x-XuxYexepVVtOUJn3n6Mzakw86VKIjOZ71B4vXS2ujmDoKR7K1ly5feHxKYqYI6KJfi7CQHSoTAK_83oRI3sRixligluY0FOfh0G9GkO1hI2qsz8XCr4IonahxSg6dWsMShVsld64mbrerRiLOXyFxuzMra-lEnD1DUEHR5AUzG0a_63RDbctVI0yZ_0TK-jspviea0h3Ap7A0GPVg1lfWu8KvN5TefOnKcK19jLRPaW3DVXp6z0hf8POx6TMr9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
ویدیویی از سیوهای حبیب فرعباسی دروازه‌بان بی ادعای استقلال در سه هفته ابتدایی لیگ برتر که سه کلین شیت برای آبی‌ها به ارمغان آورده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28537" target="_blank">📅 20:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28536">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=jBpNJvyDd2jTJi--VPBTi64io7gtAmTGTrFMDKnT91tHGQIKOSOA94NzrqWN9Ir0UiytRnZPsI-g4SDOWpegcwEk252-aDTGQyQT7S37bSWmfabpOuywEkSSxsdfPY0RuW5olmlbwEO-am7mdh4VLBUNaudL9P4kmCPJSEb4eYHv_zSYZDqclRRSV3hJf7uxyLnxcC0QyhAxC9f20PIoFsSsxeT6HfXetOXTMwFqzd_yMlusfVAUFHmBNIVoL9iIvGhwDY7zFedV2epziUcxFtJOnCj_OzDBzn6L_Nj5E-wxqAKxwKgejsNII5jMBJEcqBXZOPTxjD_GFiHHDbtYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8aeff973be.mp4?token=jBpNJvyDd2jTJi--VPBTi64io7gtAmTGTrFMDKnT91tHGQIKOSOA94NzrqWN9Ir0UiytRnZPsI-g4SDOWpegcwEk252-aDTGQyQT7S37bSWmfabpOuywEkSSxsdfPY0RuW5olmlbwEO-am7mdh4VLBUNaudL9P4kmCPJSEb4eYHv_zSYZDqclRRSV3hJf7uxyLnxcC0QyhAxC9f20PIoFsSsxeT6HfXetOXTMwFqzd_yMlusfVAUFHmBNIVoL9iIvGhwDY7zFedV2epziUcxFtJOnCj_OzDBzn6L_Nj5E-wxqAKxwKgejsNII5jMBJEcqBXZOPTxjD_GFiHHDbtYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
آیفون ۱۸ پرو رسماً ۱۸ شهریور معرفی میشود
‼️
اپل با انتشار دعوت‌نامه‌ای رسماً اعلام کرد که در تاریخ ۱۸ شهریور ساعت ۲۰:۳۰ شب به وقت ایران رویدادی برای معرفی محصولات جدید خود برگزار می‌کند. انتظار می‌رود در این رویداد علاوه‌بر آیفون ۱۸ پرو و ۱۸ پرو مکس، شاهد رونمایی از اولین آیفون تاشو با نام اولترا باشیم. اما احتمالاً خبری از مدل استاندارد آیفون ۱۸ تا بهار ۲۰۲۷ نخواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/28536" target="_blank">📅 20:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28535">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O42hC20ASxiNXNzyYDqTigN3UE4QKnJUB5vaSCaezmTc-qcoRhMD-Qxax0UU9XV3YIGTA0ycCU2HFKW9WGWWlK9syDYqIn8MXdHGhOlVbOVjj_A3xhIfTFB_peKxxNijbZPsBUl0xyRtXDAsvkPoTJZdiHVpoA009UFdl9x7Y7Ubw68CqN_RuJZju_lTQkC5kAdll74TbR5Kvg9tAnZhLVsmNeHzEQ2neX2IudQRmOZ0gDg6BZCdA_QPnNvTe0kAT0vwB6Jhw7Je48EpT_aNLGCMA6M8d8apkROO0kbIsi89GYq5XM4h9Jz4SjHjc5MKM7HoGuDAIIfW_fTPiE7cbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
#تکمیلی؛ هکتور فورت ستاره جوان بارسلونا در آستانه عقد قراردادی چهار با دورتموند قرار داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28535" target="_blank">📅 19:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28534">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=CMfSk5m46hVZcGd2srbIT1wz9KxW9NDAtBQPh_naXgefMWjOUIM0YJhJ7G0O8jBUobSw7gna1qBzs3AtOyJJIsk0tnwvmJSCrsB9dmU2XX1X395Lb4ghEfvZQkOVyG57GWKeBInBdeDrrpgzzPYXgybTxbh1xQzU0Q4fi3OH1O3EQjB-HWFR-HnbH87MBZFYxtvbKmyK0wI04EZ7mL9YHaef2IbQ04xmTt6pni7xLSf0OBWM5RY49DrefVxAgP8OJFgIyEBKvv7Aqe-DSS9tb8J7idCuH2akJwlc0pwDIx_i5s5S2XkPLMg4AbXpsu4_m_pqMfih1GLSkTqgV2NvzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/28b7c5b23d.mp4?token=CMfSk5m46hVZcGd2srbIT1wz9KxW9NDAtBQPh_naXgefMWjOUIM0YJhJ7G0O8jBUobSw7gna1qBzs3AtOyJJIsk0tnwvmJSCrsB9dmU2XX1X395Lb4ghEfvZQkOVyG57GWKeBInBdeDrrpgzzPYXgybTxbh1xQzU0Q4fi3OH1O3EQjB-HWFR-HnbH87MBZFYxtvbKmyK0wI04EZ7mL9YHaef2IbQ04xmTt6pni7xLSf0OBWM5RY49DrefVxAgP8OJFgIyEBKvv7Aqe-DSS9tb8J7idCuH2akJwlc0pwDIx_i5s5S2XkPLMg4AbXpsu4_m_pqMfih1GLSkTqgV2NvzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
صحبت‌های جالب عادل درخصوص یکی‌از پیمان کارهای ایرانی استادیوم 105 هزار نفری نیوکمپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28534" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28533">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iDjhNxgk_lHHuf4Y0S6FPYENVDcYfQE5fk4DlmCHl-c4gqY3ilzcL7_Fk-8w4sLq8w0G2qzNY_mnRhHHF0H0rIetDtmUoO-9pbC7mxlRsRHgZrUFdKpWMZR-QLAYw0bBIhiFWkFQN5j3xEMpx8uZxEetLWdcAbthxhmWFfUqSzIDZQx-JC_bbLern-_jjstiQ7ldwz7gW6wpK7F8YomQnuCD42PlV27RxedjZ89aVUew2QCfdt4kdLjk_5Ln6o_EfWj5L5-ky0_BYRUGP1S7qXncNjVuHZCmn7pKFye0gBqfQBoGe3F5lrzSKmj3T0hgHSvXw1eLfROUJhDu4hqXwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
عمق اسکواد بایرن‌مونیخ در‌فصل‌جدید رقابت‌ها؛ این فصل آخرین فصل حضور نویر خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/28533" target="_blank">📅 18:05 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk2LjhzBACo7b21erYRffowk3p9eNUDxfrj5KKBYsS8gkx3uLmjvXdB4c5AaUlmdI2iTjDLmwfNaXfJCrGDG-AGTC-Yq5um8LNKGj5oaJYWzLxWzIA4BlI1b-34fAwAtFJc6WE2GqiVF_CMlLEh-AaXQHpR0MdoXsjaC4d98gpU2NVbDWTUj34HysOxDYPdB8m72RY33cq6A8dJ5Ic5pK55e1ijeng7uK3R7Ba9zQcN4wofCtXy_TPlrffnYxXqG4gdB3EP90wEwKIsgn3_vHwFSD64PR2fxsiTMaA8cT5ojuxSdPLl4_W-yCPLGpg3_w17MmixSmMDTM6hDOpkYK8eU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285e0b6a0.mp4?token=Tbuvpn5cK09C9yL9tLoEKtQYIN-8NdtdTxSeJ0tnfVJFE5PX6lWPOMaxLX8MuHxPCJMSc6-e63qC3KUsio0tSvipFG6ttp84BqEBZUT7eP4S_crCG9kLDheCACnrlLDXeCQO43A9KEn6dgQXzmiR-Rk-Pc6xrD2FDCj7I0bxfXhTBIxyyWvXowneGAqDWXR8kowiOGg1f9a0Gvk5CPn0UnFbi8JZzMzVSSUqhK3H5GHDdd3378WJKIwIHakUH6j5gOGQEjr_etCHhCpmjM9WQ1w-DO9xFLUb-uWwzQzuECQI6oCoEMOd2CP57Pq9UGCT6RYf6w1hT1bAeLH1KLkSk2LjhzBACo7b21erYRffowk3p9eNUDxfrj5KKBYsS8gkx3uLmjvXdB4c5AaUlmdI2iTjDLmwfNaXfJCrGDG-AGTC-Yq5um8LNKGj5oaJYWzLxWzIA4BlI1b-34fAwAtFJc6WE2GqiVF_CMlLEh-AaXQHpR0MdoXsjaC4d98gpU2NVbDWTUj34HysOxDYPdB8m72RY33cq6A8dJ5Ic5pK55e1ijeng7uK3R7Ba9zQcN4wofCtXy_TPlrffnYxXqG4gdB3EP90wEwKIsgn3_vHwFSD64PR2fxsiTMaA8cT5ojuxSdPLl4_W-yCPLGpg3_w17MmixSmMDTM6hDOpkYK8eU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28531" target="_blank">📅 17:29 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28530">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bp8Qx6WgBONXxZSRMmSp8uTZRY9HIOzJ3wEtwhPNg4UqwU3Y4oumZy9zTTD2KQdvOYoFQPdv8WIyisDj3ApuQd6MFLDmatBnIM6nsT5D-_vYse_Gq03D0HSY110Z1AIWMh-cD5ujd9RdtNRXD3-kP10N7n25Q5g0w1h3DfZYjexb8oQtu7iRMHaZoFu_fO9-GblrVfsyeVQDUmqEyci1tuzFCQpOJW-0siReMYlY_k4AXyh0ONtD3RmPLXxHAH3kCGDCdIe4oBibJ6G75ipPEGvuk_o3QnOX1fJ9AsWdIOkwkL4DQQT7hsUarcWtBGm4Fc7Jw_20B8YAYNrED-qdRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی_پرشیانا #فوری؛ اهداف‌ باشگاه‌استقلال درنقل‌وانتقالات نیم فصل: مسعود محبی یا مجید حسینی، ماهان بهشتی وینگر راست‌ ملوان، مهدی گودرزی هافبک تهاجمی گلگهر سیرجان یا فرهان جعفری، محمد محبی وینگر چپ تیم ملی، محمدجواد حسین‌نژاد هافبک تهاجمی ریوآوه. جذب…</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/28530" target="_blank">📅 17:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28529">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=MpL5SxLhbK1RKstyBxc2oVkUVhESeBmf9rW63VqI35oilHoe771gxhsunqn37VCSmZqkJoyGXvT4IgE7OHD3cEKhud8A6YbIEIyHFj_RSxgbDaJI8dxBJVtm-b8rWyoLdVWDJ3gUmktgI2ux1MAcLGqaNLIMHAm3thSOn_IAu9OEZrlFAqmJn8Wgd6nPhqoMM1fNjByAI3u9FQqcnrkV4i1XUjp-0pb_HPtLRo8VL7X0FS6aTKBpuKemdVeNn3IhK20gx4CBQk_oFeT9mZt8ibPk2Vvj0E6W4EkPk788TEJB9B2OOW17251jmqwxLryv9flEuYy6iuKuuqukl9UbBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89d94e3b8.mp4?token=MpL5SxLhbK1RKstyBxc2oVkUVhESeBmf9rW63VqI35oilHoe771gxhsunqn37VCSmZqkJoyGXvT4IgE7OHD3cEKhud8A6YbIEIyHFj_RSxgbDaJI8dxBJVtm-b8rWyoLdVWDJ3gUmktgI2ux1MAcLGqaNLIMHAm3thSOn_IAu9OEZrlFAqmJn8Wgd6nPhqoMM1fNjByAI3u9FQqcnrkV4i1XUjp-0pb_HPtLRo8VL7X0FS6aTKBpuKemdVeNn3IhK20gx4CBQk_oFeT9mZt8ibPk2Vvj0E6W4EkPk788TEJB9B2OOW17251jmqwxLryv9flEuYy6iuKuuqukl9UbBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دبل‌دیدنی شهاب‌زاهدی برای جوهور دارالتعظیم در بازق امروز این تیم؛ زاهدی در یک ماه اخیر بعد از پیوستن به جوهور دارالتعظیم موفق به زدن پنج گل شده. شهاب زاهدی این فصل فوق العاده آمادس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/28529" target="_blank">📅 16:49 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28528">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLKdMnzc19SziswECxTwovBHPuGd6mAx9Md_W5fARkQLUp7DGurHUQAWyWvdeG-aeN-zIdO9IeWI3pBEREd8cN7TEEat5inyBHeCtPjlfJYVqSlSLkz7RW_uzJ-W87UsZ00AJkrIeB01vY3TFs2NRCeFvLieNELxjSP00UXiIjtYAS2I2wJp-cr9qyUQ-zlHyBuJlRzHzFxq3I4zydwQrqbfjMN7NCSfOq3w5wmGE7p-yzpdCGhK4gMNoTel9uR4eNhlUmV-mPMxrnTl9Uxb91aHEBVnPpgkSnROZKq5v-wPR7wzuOfFJIzN0fBXL_4JfWm8LCuFohl2ntJjA5WKXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌روزپیش‌گفتیم‌باشگاه‌خیبر قصد داره که ابوذر صفر زاده مدافع‌چپ‌جدید این‌تیم‌رو به شکل معاوضه با حسین ابرقویی‌به‌پرسپولیس بده که همون رسانه‌ای که خیلی‌ادعاش‌میشه که از همه چی باشگاه خبر داره تکذیب کرد و گفت اصلامدنظر مهدی تارتار نیست الان زده تارتار گفته…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/persiana_Soccer/28528" target="_blank">📅 16:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28527">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dl4H_lIpEW76u_1TUzJHRzrJ4kyEpfU7e26BNKO77E_9ST-GmWXEcHTjkM4KN49eZvj3YBvgWTt_xeEA6dTm6bd2Qq4Dv0yQeo8FLbGpQVXOxOPPLCHtgxtE2wAa-CM2Zu9cGQYubsZ4dXHfo61O6cqRRPxJnthbNj4MpcZYaz5YOTezX-3fF4QeejGkni7oM6pAdtpYoDKyqS_psdQsKxgbwY0Q9GYeEWh2yVYFPKZX7afvjDiCEoMIhwoPW8VMD6ClABuabjNYM8R5oEomdBIuOGM3btk7sx6o2LrDQpvOc4UocUqtPAtD-rwTWB3ImsX7B1OOk_z5UalHzJm2kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🔴
باشگاه خیبر خرم‌آباد پیشنهاد معاوضه ابوذر صفر زاده مدافع‌چپ‌جدید این تیم با حسین ابرقویی مدافع میانی پرسپولیس رو به مدیریت سرخ‌ها ارائه کرده است. صفرزاده فصل گذشته درملوان بود و در مقطعی شاگرد مهدی تارتار دراین تیم نیز بوده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28527" target="_blank">📅 16:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28526">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hQGGkxJnxv7z19H9VRlCFhLG6f9naUdRRwiGBXsryHBZa65jMcQ-Kx-QKJHKlqCaDPyCXNZ5bIfYrS52J92V-yv_TPZ856kw8H8umNnQN_cKLsGGml8ZG4bbta7d4ozV8-QR3f7Q3mLKVD5P7X_scYiWhf4xPlCX-GuFGK_3t8GqW3aYZZw2-r_VuUHnumnsFun4waNfRLuXkHESPiI1-J5szHhW9rpUXW9yIIqYmT2l_kXPDmuOG2pK76GUIn4kJbNev__Al4QyMqxPuAxFB6JYfFkt_KrIZpFKXXmXUkFnIMl9NjJJJitXU6MbSKz2xMZgJjvnRf0fs9UH8cKhVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
همسر مارک کوکوریا از خودش خوشحالتره بابت پیوستن شوهرش‌به‌رئال و تو اینستاگرامش عکس‌های قدیمیشوشیرکرده و نوشته:«ازبچگی‌رویای‌این رنگ‌ها رو داشتم و امروز زندگی‌این‌هدیه رو بهم داده که این لحظه رو کنار تو تجربه‌کنم. رویایی که همیشه وجود داشت به واقعیت تبدیل شده. زنده باد مادرید!»
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28526" target="_blank">📅 16:08 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28525">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/de78SNs7gFRXsKBn-2Ad2hU31C8pOQHaQehunI2yXMNjdkSr5yQyauNUPhVEMqvvwpmKIo9tiCyFsWKaeTw_17YiQtONoNVt0hkATX4GsEPOofvQbYeugw_BUQvstJ7KNN30tag1Ft7YylF4PrItExdUO9ITn5o7EtJD2UUN5bWChUDVs88ngDSP0JnGS4lEk2sqXoO3KNmjc_Rly6ca0LoyzfsdD3UliNUaMw31prYxngC1io5_SWPgVSXn3A9VrbuKFmkbyjy5r8crRClHEGUCHWT9BVfhzXQWcI6zxsMs_bTXPcT68CmNuOLVtNsR-jbhBAxv30u8qLgbFemTRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛نیمار اندرز مدافع‌راست‌سابق لگانس که اخیرا با قراردادی 5 ساله‌به‌استقلال پیوست بعد از توافق بین دو تیم باقراردادی قرضی شس ماه به اس. خوزستان پیوست و نیم‌فصل به‌جمع‌آبی‌ها برمیگرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28525" target="_blank">📅 15:42 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28524">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=I7OPV9UHvNJa0X0sF_noX11m22NLZO_z40Ro5IAUmwaIT8kmM9jbp3ooX1yGhi5RgMd7krI8H8elR0IwJRmer9R1ArRhoYf37f4xmlATQH0sXn1FmFVW59NOo-kBI192EHMgk7ZK7SYIyrmZoNJGSuU97mFHqq4GIUrVZ4WfVVYeToe9M5Gkkqa4c7uKWLmnGPDyCRFv4zxpvUvlNrsIVgJr7H7SQSq1MG70fOyKmymulsrts2jAZMsaEVe1L6l3f9ugK8IW94Ct4vthDuHR9pfcJPYcTp466ueoHYCbRtycoFf2b03YNmuqam-vXOe02EvsjbDt4CQafa8QT24sEVUcOl4LGcXydoVmRKNKG12TEpWaWUHjjJ9BmWPUu7roZaUDTSlE7TehryY70f5lDh6kQ-6CZQWMBvAVXsERZQN1-nebBGrp56rhH8fbZs_RYAA3Kxaq2HQa7X1EL20xIdqDxHAJcyVPlAd_TJfNMtFORxUl4yOgy_CVMBArDkAP32egYZiOX41GMcRjQVPp57JLntP_AvPNpkfZ-xJcypPl5P3zAoDh6hEjQ1o6S_YgQAt8NT_VuibItTaGmtu1c82-RneUm3xRKs_Zm0oV3hQHaobsfSgVQsHBbMmDqv7BFs4NapFZ1OchTTh5EjlEk0RtaJFusg-BaefqZOtXsJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe78b2623e.mp4?token=I7OPV9UHvNJa0X0sF_noX11m22NLZO_z40Ro5IAUmwaIT8kmM9jbp3ooX1yGhi5RgMd7krI8H8elR0IwJRmer9R1ArRhoYf37f4xmlATQH0sXn1FmFVW59NOo-kBI192EHMgk7ZK7SYIyrmZoNJGSuU97mFHqq4GIUrVZ4WfVVYeToe9M5Gkkqa4c7uKWLmnGPDyCRFv4zxpvUvlNrsIVgJr7H7SQSq1MG70fOyKmymulsrts2jAZMsaEVe1L6l3f9ugK8IW94Ct4vthDuHR9pfcJPYcTp466ueoHYCbRtycoFf2b03YNmuqam-vXOe02EvsjbDt4CQafa8QT24sEVUcOl4LGcXydoVmRKNKG12TEpWaWUHjjJ9BmWPUu7roZaUDTSlE7TehryY70f5lDh6kQ-6CZQWMBvAVXsERZQN1-nebBGrp56rhH8fbZs_RYAA3Kxaq2HQa7X1EL20xIdqDxHAJcyVPlAd_TJfNMtFORxUl4yOgy_CVMBArDkAP32egYZiOX41GMcRjQVPp57JLntP_AvPNpkfZ-xJcypPl5P3zAoDh6hEjQ1o6S_YgQAt8NT_VuibItTaGmtu1c82-RneUm3xRKs_Zm0oV3hQHaobsfSgVQsHBbMmDqv7BFs4NapFZ1OchTTh5EjlEk0RtaJFusg-BaefqZOtXsJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🟡
صحبت‌های محمدنوری سرمربی صنعت نفت خطاب به بازیکنان در رختکن به سبک نقی معمولی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/persiana_Soccer/28524" target="_blank">📅 15:39 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28522">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rcV7WHyGJv4BorVnevPyHt6UZcWuY4IeR459qAT-OtQ75jN2qQsAiGuffSamd8UdP66WwUCO74UUhjMpUTjLBHuWyeE1jvwwfz7onK8dVd92qEoFNHJ3M-k3J-hElmaCq32VPY1ye0C2N__RTzekVxZe0xc-_YhPzm72_UUNSbQKLEwXF-Hv_KBUdIx_BkZSqh1F5e4Q3zi6TAZrs5sDNwmVJObnoqwI_ov_L3NpjgPKTrNSoUNzWwuz0hkHrz2inb_Yn2M3Ktfg8E4Nqt0iEHoiMtwwN_MJtLLPHoJTSyN9ktegPGpS83R4mGH0EGT3Ra4mK4LwqDswTaWCZjiz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AXkaVcljP9Bb4wMofTK0I-AWzXxHXFSZFxDykD8nww9x4yk4GppEvq5uEX1SnbRYWW2s5MlYZ2rV2z8_yMU64Rww8AN8oKgTdrYjXoz0u6b9glkQnuzKvVtpnszlAWGjKf8Tu5Ey8yA95KrzQKZ85-tRq7LywnsKxYQwcU4pNgH14bm4LOoN0npcy7PHkr8UpmCCGmvxtqKrkOVevoKM4wLNpiymn7v_3JTcZQr6JryX61CGzeLpaTky0myYlsHx7CesdYpr0v_2EQyHntZT5wcfgEyP4A1gHKvmvHRRUETrb-jyAvxfJ7VIoRn5jDdLQcr9CATxoK2S7YNdSws4fQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">❌
جورجینا رودریگز همسر کریس رونالدو قبل و بعد از آشنایی با فوق ستاره تاریخ فوتبال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28522" target="_blank">📅 15:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28521">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vW7CT7AK3nDsmu4XbCKg7RgOmtCk284ddz1TmA446Yv1SU2BfwwFqqdNoXStplEPpUrH-Jwn_OF8vRMAIFaHKGgx4rx3hURkk5d18AqZZPsDAop9RdrSJ_MrTmgHa2wmRK-HiHJd6LCVdVwO0H0TdPpKs28q6fvok1K-3XlYZ6c3S-SBxmG6nVEeHo3GAwlFuHuwVKMWzT7i6eZ6gIKF2p8HJYrSpm0mzSp2RMptziJwhCwW1B4IDaEN39W9z5RUHOYilN5zlcmB-TjHM220vgEu_dg1OAtRbPL-1KkOotzm5YaR63d1zuXAqT-jx6FLfUXqz6243bOwJ_Nw5n_KBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
درحاشیه‌دیدارهای‌این‌هفته لیگ‌عراق؛
یه بازیکن عراقی بعدگلزنی‌واسه‌تیمش لباسشو در آورد و دویید سمت جایگاه تماشاگرا تاباهاشون خوشحالی کنه ولی هیچ تماشاگری تو جایگاه نبود، بعدشم که برگشت به زمین‌گلش ردشد و بخاطر درآوردن لباسش کارت زرد دوم هم گرفت و از زمین مسابقه هم اخراج شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.6K · <a href="https://t.me/persiana_Soccer/28521" target="_blank">📅 14:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28520">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Gq4acCR5CZmuaFvOFvchq6btPdpi52AYawUMs26FE47kC4dc0hg0_cgw7p5j1P5OpwhUk6YC3riHULfsWXc-1IRU0jI7aXbKPN6SZ2vq__WmEm09-gXYgQLM_3NSRvXfh_xdMrvFpUGFmVRY6-q4xsfOUBxSL4KQ-Z-8VxTYwphBUHv2ohEH64sjMG1LxWmbk5lTGHsUkl9Vqvs2z8fAt9lQ9XK-ItUoF9c9j8XL7dxgdmimLn8viwu7mg6vfxQ3rpNaxH7D2JPwjPA3a1KF8EL2FVHtOkgItqCZc1Pe4y1q_l6V_YnAjjjvIpIuLBtD9fA20YasBdXSLey0pwszng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رامین رضاییان ستاره 36 ساله‌فولاد از هواداران این تیم خواست که دربازی روز جمعه مقابل استقلال کل ورزشگاه فولادآرنا روپر کنند و از مدیریت باشگاه فولاد نیز خواست که بلیط فروشی رو رایگان کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28520" target="_blank">📅 14:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28519">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JUboVP7HYq7qEf5Yzc13MtVSQy7Anw7uKnQkWoREL9kBE-KGRKlGA8ru5RTCZEc_ZjN07_0eDqNpoanNApCkPplF-3bfdI5jB0cumt88l4TV7966V3QLpvP25hXKPKgE56VPD8tjw0WNksRegkTZ9Chqe6KDw-OFzfgJmsvdAIDcIX6W6XEW6ReTzZqmUw3Ng_wDW1Ys8yWxR7i2_delH-tsV-f9rLcxlrb_PfO_c2cHipIb4GOi-ruIns84OjWIw6nEXOlfjwj74qbDcasC_Y8VYDN9fUl3zbAF6U8gGlJlBhHE7xzHNcXO-vGDu30NgIwQRqpoCNhtG-9WinTE5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دولت دو کشور آمریکا و امارات براش ویزا صادر نکردند و مسابقات‌جهانی‌مستر المپیا رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/28519" target="_blank">📅 14:14 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28518">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F44TcFuK_8_swOc9cbEOF22IrbadLmR6cmqlPweK_rCjDFVCeRKVMx21mD9tORmWwZGmL_S4Z0VKjnwau7qcne8_NTaFvZOTjyqR5GWDiwylvcOwbtSRJ9SbgG2-kKaqptmq4UyqOf5CO0Kxi3n-jydfajTFfAs2Hy5Ehat2BmSpKW13TMtM9HK3_azVwgLIzeIZBy_M2bqTuGAcFDYxsOWuiXvJeYhasrbOU8fLDXELDRINO8p6RGoow1Wmlf4JogNMj-c5htq_I8Vo5q1Bi9F5KAWeayLa6pZRvhdDP4DcRy8-4c1F31pP0-XEV1cdj3vcGEEyYSYEPf5XWHRAkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇲🇦
سانتی‌آئونا: ایوب بوعدی ستاره‌مراکشی لیل درآستانه‌عقدقرارداد پنج ساله با منچستر سیتی قرار دارد. توافقات بین دو باشگاه در حال نهایی شدنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28518" target="_blank">📅 14:04 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28516">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=a0G4Jaef-LBkRy6ZYlnPjLf72alUnt2gP3IFJJ5lyFKjcfWXj3xXYKDYSL2SRVPMLLXv30oL26-qkO7o_peekOw_DvT2McRoiB-7bJLWKhyJZixDxubacJ0-sIwUOLPGG7h4Fkhk0yyBROP1sjPfO715Meg0NnTU_jRUPjiqEy3kMv64eFXD9Slrpw61hzbIlT-dJ10btIAA0FBnZfXAM1qoeb-3Dfy7HCRi7YT1AxLJZSKX8fmjg2UMDfqZRstitu7fdqNtIRODTg1OKASE79Rk66zzGQV4SkoOTTxg3cVxNuPSlFb0xCLegLCg9DovcrS2NfVhqFR0fWi4Ui6li67WGoyccEGrjJK6Vjjq-AeoTxbq5-zkUQZZ34IxBIq66oqXebEqCtUQn0HTIPgpj7kqSiRDA_m6IbQxTZ4UOhAiWqxef9BBoOUL7aXt3s3quYH6cmHmztR14NdiAvZifYXmIA1cZ6j9t_UasAl8CM4vYtiympvya9urPBiT4B0jOrGtI6En7uh4ySN-9jIIc5XSKdocowTviBYv1GFWF9OX4VwBaPIQkHbL72mmFQ6Cc8QzGHP0QOgxPQ5NVJARICxVsDpJ1G-AVVySei7N1rfzL3YVzr3ERlcMfSrpblwUkl2OehTxfAi7yt2R-0kAcXdg8nUNfgu9XEgQcEMhqu8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a17541dbb.mp4?token=a0G4Jaef-LBkRy6ZYlnPjLf72alUnt2gP3IFJJ5lyFKjcfWXj3xXYKDYSL2SRVPMLLXv30oL26-qkO7o_peekOw_DvT2McRoiB-7bJLWKhyJZixDxubacJ0-sIwUOLPGG7h4Fkhk0yyBROP1sjPfO715Meg0NnTU_jRUPjiqEy3kMv64eFXD9Slrpw61hzbIlT-dJ10btIAA0FBnZfXAM1qoeb-3Dfy7HCRi7YT1AxLJZSKX8fmjg2UMDfqZRstitu7fdqNtIRODTg1OKASE79Rk66zzGQV4SkoOTTxg3cVxNuPSlFb0xCLegLCg9DovcrS2NfVhqFR0fWi4Ui6li67WGoyccEGrjJK6Vjjq-AeoTxbq5-zkUQZZ34IxBIq66oqXebEqCtUQn0HTIPgpj7kqSiRDA_m6IbQxTZ4UOhAiWqxef9BBoOUL7aXt3s3quYH6cmHmztR14NdiAvZifYXmIA1cZ6j9t_UasAl8CM4vYtiympvya9urPBiT4B0jOrGtI6En7uh4ySN-9jIIc5XSKdocowTviBYv1GFWF9OX4VwBaPIQkHbL72mmFQ6Cc8QzGHP0QOgxPQ5NVJARICxVsDpJ1G-AVVySei7N1rfzL3YVzr3ERlcMfSrpblwUkl2OehTxfAi7yt2R-0kAcXdg8nUNfgu9XEgQcEMhqu8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تقلید فوق العاده صدای گزارشگرهای فوتبال ایران همراه با نظر خود گزارشگرها درباره تقلید صداشون. جفت ویدیوها عالین حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/28516" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28515">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o23J1MzMUFl3gjJcBEbrhi00Q-Oa5qhWGaQDgKB7SN_5RuGF0Z87e09HoEMrafEo1DSXFvtxePKQ9gq8hViJsGb9tkP0Kps-lv4ZFz1z0MjttxwT8-rJRYdcgmKbNimn67LpFfxNDSmsUMczg8ZO6hYv27HkaA6h-rW6uWbHWsezhGb9YrGKZye1tp9sC0GE7njBqpXsdz-zr84Gtcq_hSYwmGT29I471QtBbiykaF1Ig7ID844CYZqL8MZOQSlMsbfx34CJeS9gzveAp6uUJkYtPfqeDla2TfpYid7UT4UxhLGZ9bOd2adtmd4focDMm_joShiLeAp2dYTJFIO_VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
النصر دیروز درهفته‌سوم لیگ عربستان درحالی تونست سه امتیاز شییرین این دیدار رو بگیره که از دقیقه 12 بازی10 نفره‌شد و دو هیچ‌از حریف عقب بود اما در نهایت با درخشش مانع سه بر دو برد.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/28515" target="_blank">📅 13:35 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28511">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o2xLWpP79v46DNeipYyKskW8Sn5QSdSP7U0Apsgk94L02lsCF-XrCNbuoQJxeznuksFw9tI45q7LagBNisiYubNf7NGMoSmIgCyBoTW-xdgzRNqbq0TnlzW9JtgQ0MbfLMeNpM6IrUoWcARyRCZjnWodIztIXyIxBdHbzCFLjd8TdsNOeBmg6kXbdF3dyKsy_CDF4a3GuZPaWLpgC9vv10orfKVETsHDbo8efcVdVUkTsNHjZyF3tuCI0UYEllR--7_QT5AODCirg0AhbiG7jy0aw91Ix5LBKJsOAk2qISlZkIdhO-0isdLyYVKaDZISCfqa4TI01BrYdyXeY0-NOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قلعه‌نویی‌قبل‌از دریافت‌پول‌های هنگفت
🆚
قلعه نویی بعد از دریافت پول‌های هنگفت از دولت! شاید شما فراموش‌کرده‌باشین ولی‌تاریخ که الزایمر نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/28511" target="_blank">📅 12:58 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28510">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CFVKCfDs_5Rfs1CSRw67VnOsk6hRh99FkppIR7ERYZQo4GfuFvfNbLYG0jXUgQOMUaWxHbN2GjSDeVRkXIgGiVMxN_WjV9VQhHefm3_jR7TDDaaSNQxIxtD8-8CrHt6HkcVt9dLc4JwKNTaFrW_UMRmn9POIn-lGctjMkjDNB5Wtg55Z_SoqxpnMLo5jCg3WgDpBbkxWBVOdywGPxl6RrNpsHEyCfyWPha7ovj_fPo4jlwpl76rqgi6TRSyo9PcQaCuheyuuTec6JbWmiXSkXfA3Bpp1qMJ_BUMe8cL-ZsPzei1cK7KSuuoNkrvRk7b82Wm4idpCif8kXJRtMGciZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
نشریه اسپورت: باشگاه اتلتیکو مادرید آمادست که خولیان آلوارز رو با دریافت 150 میلیون یورو به تیم‌آرسنال‌بده و توپچی‌هاهم برای پرداخت این رقم اعلام آمادگی کرده‌اند و حالافقط‌رضایت الوارز باقی مونده. سران اتلتیکومادرید به آلوارز گفته اند تو رو به هر تیمی که…</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/persiana_Soccer/28510" target="_blank">📅 12:30 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28509">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M6P5lQp5cqrFV-ZY09bz7wA7MKpwdipCH945x79I_nMuvEWXOs165Vq2bNnscz0lOnnmx-MxjuMrvbfwxBE7CLxkFUdTOFUe0LgHALkh1PPk3zJDgbGGBkh8KeRpd5I7Z4J7zTmXbnwPBEYUviPMParmvAc85hV5BjYJrMswfnPoQ6VK8wq7sG223gMchlB2BoD2iBtye-FYc5tEnG57eEbe5jtEgjGFHLQDnLIByGaKer8_q-euCzaioVh6x_P50BWt7cP8BKkS1Prfx2w00HHks6hJpeiH2ngvCpb-P2yFcFWYDQKBuIAMVjOe07nZu7e2ANL0ericAN8TM06ddQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
بااعلام‌پزشکان پرسپولیس؛ ابوالفضل جلالی مدافع چپ پرسپولیس به دلیل مصدومیت از ناحیه کشاله ران 4 الی 6 هفته دوراز میادین خواهدبود و دیدار با دوتیم تراکتور و استقلال رو از دست داد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28509" target="_blank">📅 12:12 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28508">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WH6DLrJRlqUMDkc6JeraAjIf-CP0a_MBHOyHbgMZM25GnS6SOSpjbMQQsL9IZYx-qJ5NbL9JwpejOxRi7ZV3qrbNsFJSU0TrpPChq3HcWY2V40idENuYXH4kISUpvYid7Ii1ZH2xy8dFRq9tih90iekY7x4BGhnP4n4h_5aKjKcZo50LsEBQOiospedhGicOgY3Ck-dXQTjUjWqBelQnjOdOjmvEtwWg18y5z_4l7p7qNUF9fqT_nfVFDbQzfulpANu-rdJu1mCWLhKZAPlH4-1mVaDSzfGWFOILzv2Tri3qgNhSlUdYAh1otvOmLhOt5RSdoc6UGPjt5bJiJYK6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگار کوپه:
آدمای داخل باشگاه میگن که تو خیلی ریلکس و آروم هستی. مورینیو: عه؟ پس تو یه منبع داخل باشگاه داری. خوب شد که بهم گفتی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28508" target="_blank">📅 11:15 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28507">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=LH64UrRgWHKp7p2YVxk5Whft6qW6UkNsEGWK1ptfhFF6ExHhj2uGCmLwdzpLDFhU5Y5ub6_RH0Ttl8KZanklHqZbqeDVPGfUQwQeYYzQJsscGu1pVXXTcnptaR_lmiitU2j7SjIPzld_1cRoCp175CrHHlw8paTaxbI_1kVjWH0sd2Z2lJLyV0JB5Nvq8O2esFouHx-QqCPjd8bj_o09-qDrKw_Hm4KlnJHb-WV91VkVH5-mwHLUTdDz9qOcbcC9hKxDGuS4XQ4nZgivRDcxi4tSpkDw-g5PT9CkhyzFeEvkarL6hPCoaRSFUnF3dc4qqKFQ9P3FEl-kQ84qmJ7kdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/099bc5af8b.mp4?token=LH64UrRgWHKp7p2YVxk5Whft6qW6UkNsEGWK1ptfhFF6ExHhj2uGCmLwdzpLDFhU5Y5ub6_RH0Ttl8KZanklHqZbqeDVPGfUQwQeYYzQJsscGu1pVXXTcnptaR_lmiitU2j7SjIPzld_1cRoCp175CrHHlw8paTaxbI_1kVjWH0sd2Z2lJLyV0JB5Nvq8O2esFouHx-QqCPjd8bj_o09-qDrKw_Hm4KlnJHb-WV91VkVH5-mwHLUTdDz9qOcbcC9hKxDGuS4XQ4nZgivRDcxi4tSpkDw-g5PT9CkhyzFeEvkarL6hPCoaRSFUnF3dc4qqKFQ9P3FEl-kQ84qmJ7kdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
گل‌های دیدار فوق‌العاده تماشایی و مهیج امشب دو‌تیم چلسی
🆚
فولام درهفته‌اول لیگ برتر انگلیس.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/28507" target="_blank">📅 11:01 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28506">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRKZsFK2n-G70GDJrN5Z27D1DjWzLGhrgmne71TCCOycaa9pZc-IxTXZc9rpkMBebsb9dg7gsT9CPrsu4v2i1-_l-FX1tWmRD7F0Eg8UtJXRf09jzys_oQSuj-sJjrd5F4ZAkYT3pa5lL5kbvnNJwwRkmAjSJ3RvLmP2VOg_-cjjvU1AE0N0GlOJQekMeU9ke3iOb0bnDiamlCSqsoDqioYwAgbA8iJo_RWF_gSrO-Q96VJ6b7ZxtscwdzhbJgGlO4Dc1DNtA5pW7jiSAjoyCk9Xki2DxtCznF52Udn6jIeAqbbViXlcaTFfbKfqJrCfy3P3ZJl2HPuOXJOq_Ohykw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باتوجه به‌ سوالات‌زیادی‌که پرسیدین؛ بعداز پیگیری‌های دقیق از مدیربرنامه یاسر آسانی بااطمینان‌ کامل اعلام میکنیم که‌فسخ‌ قرارداد یاسر آسانی درسامانه فیفا ثبت نشده و تنها یک نوتیس برای باشگاه‌استقلال فرستاده بود و هیچ‌مشکلی برای همراهی…</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/28506" target="_blank">📅 10:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28505">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NfdfEjbW6ld7n62C8FlviyJk3PTL1v2ASn9Wq0BIbcB7J7qiowJ8_wtiambJe3dJGjAjw3Z32qO1__3d7fIHzU8IPnsjg6ZgNUBcyTRxcgVB6l3IXwICghR9KsDc1QwGfkc9A7X2HKStGbEzY220b5p98ddXAvhmP_Ie6_SLwRjqaTFD1KlVq_0RVK8jDeUAJBVHUgbV_boVJF0S1yGiSRtbb2qJxPHEfno-ySVZNssXnJi-3LFbIlQAiz_WSH_pXiYwHNz1oYJeZEYjN2jY2DkpdIKLOngizPruwzKasskxytBTQNuXYXRq83UMzbYLfLGUk6OGuwoCy8n0qVy8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#فکت؛درصورت‌پیروزی‌استقلال دربازی روز جمعه مقابل فولاد در اهواز؛ سهراب بختیاری زاده به تنهاسرمربی‌تاریخ‌استقلال تبدیل خواهد شد که فصل جدید لیگ برتر رو با چهار پیروزی پیاپی آغاز کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/28505" target="_blank">📅 10:02 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28504">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iq_W2EgWrvlTnXxkvEZWefsjZz6JFc41UPQ7Dxpl9T2NrG70QMutibrew04zhlgZk14yortAy_E_vsxlLkZXmacxS6Z_Ug3w1w19NKHAHAEvbCpVEthKA5BfLn2JtFDEzf5XaeyURLr4GymqmNLZIlF9h2CpFHZA9lP2Z7OROrNe36WeNBMFXSgIbML6Xz47ORF_1ydVRIPhWBKtftKOWxSdXmZsRvKSYjQYAarTXTwBs9-bjiK9_IIe4ecKIOrzzsD6ZIOb9WwA4Bo2wd-FIfAnQmDAytIdtcSLCR48WtN47jeRwGg2wf0IcGLMoEo-OxL6lW-wrRxsT96dgJv1MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته‌چهارم رقابت‌های لیگ برتر که روزهای جمعه و شنبه پیش برگزار میشوند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/persiana_Soccer/28504" target="_blank">📅 09:44 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28503">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aK_GiP48JAnIF4fU8uN6gRngK_uccEPaxIoDpr7RQUXSyPjjYKZdAvsQYyDSJtDnp-t8xA-0UzhHvTMxWyit0S2BFDZ84TG0SKqHRRJFPo22RKEmkR1uPcoq9lKt7K9mIzrqO4E_pC7-JZik-RXRat_yvFLeEBIeZVgd-xpn7yZleumvvDnGiiz0RPjpBHcIAcTMrS7jvZyyNcPXZaRuPSr_Mrkdm_9I3mHKeXGZ5sOm4JUCx_zTJKNvAhqWdVyLbnXMkzamImzlRQR2bJgM5ISRFK2u6LkD1uVD-0T7J7eSi-W8O2cfFtvzSyedTu9acNmXfm64awaOWyGUj3HnTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دیوانگی‌مطلق‌درسوپرلیگ‌بلژیک؛
رویال آنتورپ با نتیجه ۴-۱ مقابل خنک شکست خورده بود و تنها ۱۰ دقیقه تا پایان بازی باقی مانده بود، اما در اتفاقی باورنکردنی‌توانست‌بازی را برگرداند و به تساوی ۴-۴ برسد. سه گل در تنها هشت دقیقه برای‌رقم‌زدن یکی از باورنکردنی‌ترین بازگشت‌های‌فوتبال درفصل جدید
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/28503" target="_blank">📅 09:25 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28502">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjxCJK9NxE3hIbtN0qtgdPTj6vsht2DZr6e9HhybVVN01owUxeOwFBhRfjiaOWJL0TQ7NSWpBRqSVyxRU6XIuxeZJuCwPot1TFGPr19zcT1TSTSOUFYVd4u8Ht-CFpLgOVCm0jEDD1zcUpITkikCc0KB2_zoJWPMtphQGd6tBTToyr8VD5Wr1k0mw4HgN6cH4QDprHxWnK_iewyqZcE2QtPYDOfqptNgttRgtKI0eWsqiQeNQUxRVu6A9axRZ418Ruxzxp_8Oj_uBxVfuj94s2i8i6TrL-yh_hu6ymLGsghnbAY4aAsre6M7cKo_wqECWtokBmWHMRZ0kr3emSMywA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
قدمت‌تیم‌های‌حاضر درلیگ‌برتر فصل 1405/06
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/persiana_Soccer/28502" target="_blank">📅 09:03 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28501">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SqOYFFmY2PSmKyEMnhrwhDzyOrIP428BlxFvqMxJO82Egucww2d4z-DCFRqTj1CWp2j9T0mjThAYCNnFO5-rWfsjVKQmOTPDzlBjXHRNfkIMfJaps-TqjRIiqmaDZp5YUWXSfujYocNrfWy_y8H1z5_-X1kR6fpkRHpfsgIIY_cJqFWAiEUFbQ3EvfSvztdFsWUJ6XeWiXud5f-gFHL5WZIElURMeWxW5XDebyAw2ZD2sncRZNEpDNCqNpIsNpDQveZu9arUL3KVWLA6rO9uDd66wwEzyDoVcDxJ5vNHzVDq4K2jsxCCg00rdXwUtNwS2SrxA3VrlMd87BO7i0SwZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇩🇪
مارکو رویس در گفتگو با رسانه‌های آمریکایی اعلام کرده به احتمال زیاد در پایان قراردادش "خرداد ماه" از باشگاه لس‌آنجلس‌گلگسی جدا خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/28501" target="_blank">📅 01:28 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28500">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dY8RNzu1gUpvMa4Vai1Q-1wa9tGE59QMy3jPGYJyxhq1CIFQjyN8yqNq6sOH2Crlqt5CE064cYzGwBfgPntir3Fr2tItL-maLKT6huH6L8OeRMMKMbIngWt2d9YNmhw2Gr74e7YiU68myGzQ09ahnIfnosNYVC4WI_EUhAEo741hwxL2xfPjGl4Pzp_nDOfQvG-Sp6U8G01TGZpUJVSN3MflTliR586pzkj_amJaF-sIQt-PwUZC3MXuSdXN5PYQIHyI89ekm9l_B44SbPgbLDUL7UiOnooXF0E3EzkDMdmdz4V7cmqC5L6O9QdVQ2oOS_b9dzgSO50VeCOYMDpoiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌دیدارها‌ی‌‌ امروز؛
دومین آزمون مورینیو با نبرد کهکشانی‌ها برابر سوسیداد در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28500" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28499">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/akfVIlQvlDIcp4Vc6v4NeZivKzZ1QqZfQ1YSyMw2EmT1UTQemMkzg5I0lJsviLhGnLuobnG72kOWeMAKm6ZITBtq48KlvTPp-xxYttQuA7wI54kxD5AEj_bSM7IhT8qzXoeNaCUWC926AMpKZst69pEBOe_DZ9qO50Y6NjAeeeIPCnpyBSVwFkooKxGnhbbCxhYcZpMWlxFGlymrvqEpv0KGtQkw4L_D_gH0_AyUTRtlwKmz_UZ-Cd1hN20aYDJYrAR46gVss778KAOgoiBUoBFJeXPsyaGoqrzDN0U6yYL9SGWzdbXQbSxiskb8ddiRGLV8X7CRVkyw2PMmsNOGdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌دیدارهای‌‌دیروز؛
بازگشت‌دراماتیک شاگردان پوستکوگلو با درخشش ژائو فلیکس و سادیو مانه
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/28499" target="_blank">📅 01:26 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28497">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gwja7eafv76PwhbZJGdAmuytrc3CFLClq8rKVWTNM367BCiPRaBlLleTueajp5gQDjD0UOTal4EFxaI038o7wgKg0gf_TF9tt1pDzA-EFfbpACsz-a_kL6tAXcwiuPDA3oROEpxzfHisnqxJ0qex1gtFKVJ_jZLM1qXZ2_cRRX0KCcicmO0FhrQ1ymADZRd35l2xjbt9zO7FCA6-MIKgYLp0dKjTEj0ioJRGwVB-NOxeSMSJGrUaRw2CoO_568HLQFQMT7YwmahwDc6VmjHGgLrO68jYHM9ZqxvQ53f0wFM3k-vTYVVU4sGhvhLzZU7XJsjm5r_3VEKZdEg-owWC-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔵
#تکمیلی؛ باشگاه آستون ویلان پیشنهاد 45 میلیون یورویی الهلال برای‌جذب اولی واتکینز ستاره خط حمله این تیم روکرده و قصد داره با 70 میلیون یورو این بازیکن رو به عربستانی‌ها بفروشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/28497" target="_blank">📅 01:06 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28496">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=lYH6h4Fd4Vft9NsqgtWqeMkYR8YQlOMvL91mnocDt2dYs4VtnWFR_A-NsxUQ6L4FHoQi3CaGiKFwpEqKv9cti2sfpDZWwWsujDYJL9Pb1nP96B98dwZnHb5IvcTFsl2PrBCCyEN2KKpf9tjLxpjYkC1Hmfxt9vcsZCLFhXbui21hfr3m46LWI0RQzUDf-_LLV9GpqF26Wrz716VJ-trx6BHUMk0RzI307BBib2a6Sve-nKrlmH-3qq3soUmcEKREzNG6aZehhPZtHLCQN5jnRxbi3H9kX3I10OoxbnELMdO1N0dqzzS-yQ1U6yZbRcdYFgaMbJ4mPgoHNozVeqUONw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/122f8acbbd.mp4?token=lYH6h4Fd4Vft9NsqgtWqeMkYR8YQlOMvL91mnocDt2dYs4VtnWFR_A-NsxUQ6L4FHoQi3CaGiKFwpEqKv9cti2sfpDZWwWsujDYJL9Pb1nP96B98dwZnHb5IvcTFsl2PrBCCyEN2KKpf9tjLxpjYkC1Hmfxt9vcsZCLFhXbui21hfr3m46LWI0RQzUDf-_LLV9GpqF26Wrz716VJ-trx6BHUMk0RzI307BBib2a6Sve-nKrlmH-3qq3soUmcEKREzNG6aZehhPZtHLCQN5jnRxbi3H9kX3I10OoxbnELMdO1N0dqzzS-yQ1U6yZbRcdYFgaMbJ4mPgoHNozVeqUONw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نادر محمدی هم یه تنه تمامی قوانین فیزیک رو داره نقض می‌کنه؛ در جدیدترین اقدام این پرتاب 45 متری رو در لیگ یک روسیه انجام داده که کرک و پر تموم رسانه‌های دنیا از این پرتاباش ریخته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/persiana_Soccer/28496" target="_blank">📅 00:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28495">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=txDebkLUEiVltwuz_GQgLInCzyAaniK8lC6IWDxD4oJH43F3KpnuBFvnkBZOzWGeRnipzhd2jOWrOKSg97CrwXU9tL-GvVRAn0sAoLP0FRoQADgkZXy1Rkw2jfOPQ_VRKlCMpdu5LmYjCgG57qnlxcdwNEKwiC8eHG995PgQ_TCeOKL0YPOBnnNTBcDzHXnQP5SCUwNW2PnGJsouGCuwWL9OFpqVrISD5z6D643PAUbVpGbMcrfRnNRqAMjfex2dIX7ZOHIgQJw4ABL4NvQ1m-mCCDwklpvHkR9EVIeb55k-udR2pLuvFm1QfFy2jTmm8yA1-zGmbIMO712UVJwGOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/61cd0ed9f9.mp4?token=txDebkLUEiVltwuz_GQgLInCzyAaniK8lC6IWDxD4oJH43F3KpnuBFvnkBZOzWGeRnipzhd2jOWrOKSg97CrwXU9tL-GvVRAn0sAoLP0FRoQADgkZXy1Rkw2jfOPQ_VRKlCMpdu5LmYjCgG57qnlxcdwNEKwiC8eHG995PgQ_TCeOKL0YPOBnnNTBcDzHXnQP5SCUwNW2PnGJsouGCuwWL9OFpqVrISD5z6D643PAUbVpGbMcrfRnNRqAMjfex2dIX7ZOHIgQJw4ABL4NvQ1m-mCCDwklpvHkR9EVIeb55k-udR2pLuvFm1QfFy2jTmm8yA1-zGmbIMO712UVJwGOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز اولین‌تیزر سریال «مرد سه‌هزار چهره» به کارگردانی و بازی مهران مدیری منتشر شد؛ مجموعه‌ ای که ادامه‌ماجراهای «مسعودشصت‌چی» را روایت می‌کند و قرار است از اوایل شهریور ۱۴۰۵، به‌صورت هفتگی از شبکه سه سیما روی آنتن برود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/28495" target="_blank">📅 00:34 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28494">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t-UrOvClJpWe33USIqMzCbATD5ViaFc9qAg8w231-e5lN6vLX2TJl9JBRomGZJiA1FlrLgiCtPujMN6k1M4v6lXDkMoEkkOupQtkEotyB-_AZjJC-cFDJukjl-HoCFOKqJEoOa-PzGz4Z6DzDsDBMAhczVkN4fn8YVozGNBr_zlBTmXj7mbUlUQJmu4pOmeIPTAbbFX3s4LfJrmuBfv32XO-2WYUHcEISk8QLaw_vnRaDMoyveieTwVs706KmeCVe22mdTfQHmZE56AVCfrGqbrdYadxFzzpA5rqXoJnIPdFfW6wD7SxCJu9t7i416MeGv4nTAaUSZrqbXLhmdITnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📱
استوری اوستون اورونوف که گفته مصدومیت جدی نیست و مشکلی برای همراهی سرخ‌ها ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/28494" target="_blank">📅 00:11 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28492">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hrJuM_y3kPYlS9_qxml5c6DGqjQLlEFeWtb3YMUhVENHOPEYkX3rWk_3arp-2cy8IPfeZ_w1teyFtoCh9EuAtwcdEjZxIPPi4VPy3zVITHgFAMuHrzbPs1o-on2ZwC_UwW64Jzjic73I9B5dFZXX0St5Fcx5y61LVC4OSgNoGE3CPUgWJuklBOhXcqdbNl5hIji_ow83YDk4TSbM1noCu0LtnmMasjaaIiSPreR0_JPQoCQY-8eRXNfKgBztJLCuI86INm2R2W09DRzrq-t9ZXoUlpP0qL8JhrTR8GnkoqpIiYOyH8684MUWG0fSxPkeOxmzcaUsGwnbMrkaPddqgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qbUsss326nNZzwixwRiS71NFi7tflyL3lHFlXUhrXMqczhndr2fW28ZOxQRSXfYOvwghKykqEPoD5-qNus2anNVrunRMAZvWpP7YGknr0ynQx5V87HzRS8MTgH88u-MXOrnXXRYa-5ZmfLxY_zZ3_6nrhQnPD10a_TN_7REz9D4tK1Lu2axjK2hf3MH963y4smdxNmqzZvflDdG17flpbnccWla5t2ya0y8Je2vblYshOsfRcc976lA3rvL7YKfYbIDAoa5gmm4AutClYXIjQm-WCgaljeKG0fpjRG9WgxRpTZCL3__0Tb03O63D1ZJSsAowHyL9iqf4faEfw9dCzQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#فکت؛ عملکرد حسین‌ حسینی دروازه‌بان سپاهان در تقابل‌های‌ خود با استقلال: چهار بازی، سه شکست، یک‌ مساوی، 5 گل خورده. 0 پیروزی و 0 کلین شیت!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/28492" target="_blank">📅 23:45 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28491">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pny6norCTnYltQaVM0aDA3Fcb5QdwWANePVT8yL6SxUkgrv9yqxXJXY7lz-8F25yko4Hfk4R3yiYol9f6jIDe8Hyy9xkn9mLkjV6y4BJ7ZiHGD1n3Wes6OkcYAUJQEwtpv18994JLG4PNASlLzS9wDrrWrvqnt_5qE8AkWlxAa-6PX31SJJVRgiwAV75w75XAnyl5OfzBcMiuk-9insWwqCg8YJe1NErddqJGr5s5v--OLpVfNEc17dy7Cmky-zSdrTlomFxHqWbqDVmv-uwQVgl7o47TJ-ZUO4wOIshWJo2_4fla3DIDFEsHthxR0V6qmUqXK-P56JVwEHBQVyOyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ مصدومیت اوستون اورونوف از ناحیه‌قدیمی همسترینگ بوده که بارها در این ناحیه مصدوم شده. فردا از او MRI گرفته خواهد شد و میزان دوری از او از میادین مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/28491" target="_blank">📅 23:33 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-28490">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d926debd47.mp4?token=OxW-cb7IJCVotM7DqJVkK3Gav5Izdm5FIQ-SyKzqNDdckpYbF5Kk9-BtvOPxtH6wfwnz1OU6zlfF5OZrjos8zDkfQC86QZiGUx58WARlPbowIrRXt1NGen5nRiINRYut9BMKidLlRPfzbGkm0EbeCnJxVlqNqgfjjo7hyAjQLYu2SfK7Fq0pR7sXZNuaxQjrXV3HW-AifOV5Teebz5cIX5H6xRhMn6KgnXTpW6Dsq76tYW0N7pLt-0jeux4beD9-_pX1sg64OeD_UTCsseBrTBNWrjgP7TW-huAryo1iMzqgIPlcxwor7kw7AHukBuN44N4iO8hWkRzkFlXCtFw8cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d926debd47.mp4?token=OxW-cb7IJCVotM7DqJVkK3Gav5Izdm5FIQ-SyKzqNDdckpYbF5Kk9-BtvOPxtH6wfwnz1OU6zlfF5OZrjos8zDkfQC86QZiGUx58WARlPbowIrRXt1NGen5nRiINRYut9BMKidLlRPfzbGkm0EbeCnJxVlqNqgfjjo7hyAjQLYu2SfK7Fq0pR7sXZNuaxQjrXV3HW-AifOV5Teebz5cIX5H6xRhMn6KgnXTpW6Dsq76tYW0N7pLt-0jeux4beD9-_pX1sg64OeD_UTCsseBrTBNWrjgP7TW-huAryo1iMzqgIPlcxwor7kw7AHukBuN44N4iO8hWkRzkFlXCtFw8cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇱
ژاوی هرناندز سرمربی‌سابق بارسلونا با عقد قرار دادی تا پایان جام جهانی 2030 سرمربی هلند شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/persiana_Soccer/28490" target="_blank">📅 23:27 · 03 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
