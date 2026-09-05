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
<img src="https://cdn4.telesco.pe/file/fK9E2iL09PAcfkBnyrTi4PSNrmDCnb6pBZolFUEdYxRLFkQVg5xVmPK4Ab0-PgcqjBDnhSO9aL1iMsLOzNRF7kp7iCgpebXVMz1GubhEmOQOIjIf4oMLbWH_g_VGM0iMHXByNIapYX49KnM_5mXVEssh8T-Ph50pfQ6Twjg5z4Kk2wOSkfzeFtoYltdQ1aQ3j5lpi3BysBLpOxQh0jU83AFh_DAXpj0BJfDLv3k2MYTbYOfQHvVG_7sYVdnwgbsz8wRpd4UOoOsfgf4cvXNe2cqWbpkY3G0sqtTq2LpQxPZk6saOrrBFNBZOyJhdONF12aZ3j1A0x7KgOU5UZf-DmQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 602K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-14 21:59:09</div>
<hr>

<div class="tg-post" id="msg-29131">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7875374a88.mp4?token=LNCLMkBCQMnJCaOAZX68IUptbWAk2pYXbwDue7eWZPZUUKjctyrddsWysnSwzejNh14khzPPSqHwPrQmOLZ6KuYO9vINd_OmNsJmfZRCjctZhODllzGv8KQxVWzXc8V_o-YfNUNK0O1Ca1rCsAbwU3M8ObGjjYwMFJZGCe0d4XzUNumsG3f6TwmWZGRrB5kFJ5r-kxazeE6UgafBEA6JA851lgMrINihnhRX86QjrJaxuktRU9Q0ndG9rrHiQal8dejlmuy-RfopmGk38XstcgUQDUykby3DoYVRtYIQ25fZYXGk_BSNPNxAlPPM8CWPAUfYKQNsEirRnMOaNpFhtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سهراب بختیاری زاده سرمربی استقلال: صالح حردانی بارها ازش بی انضباطی سر زد و بهش تذکر میدادم اما توجهی نمیکرد. برخورد من فقط بخاطر رفتار حردانی در مسابقه دربی نبود. تا زمانیکه من دراستقلالم او دیگر در این تیم جایگاهی ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 3.02K · <a href="https://t.me/persiana_Soccer/29131" target="_blank">📅 21:57 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29130">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gnHZaJ64ATF9kzONk3Ck1LUpnt9RCKPYKSv3KgWrZHKMjJaCan4DAOcD5jNxOwSLMP25NQcNIgV23Nj9NoauS6-wZx46MTpcbv0jFMHPvLjz6M9U6QUCtOZkPDRudYqY2-2bhsKJnSqDXpFrpZlzvTldPmxq0-WSLw3Hpd_O_-CGaHoa71V6SVm_PbwHIU09Lz0cnvp2uQXwE43l2rt-LBAHrgsCyENbGd9iBKyA0cGhmvBrqYpcOFGFJ8QQjwDOCE2benEhHeD6hg6qQC4U2R1kAlzk3VLVI9-VaPhn2wfLyvjLhUU-OwkmuKXTzptDOTFYXdOpRhznHUxDyummMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول رده‌بندی لیگ برتر در پایان دیدار امشب تراکتور برابر گل‌گهر؛ باپیروزی امشب مقابل گل گهر شاگردان جواد نکونام به پنج پیروزی با کلین‌ شیت درفصل‌جدید رقابت‌های لیگ برتر رسیدند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 6.26K · <a href="https://t.me/persiana_Soccer/29130" target="_blank">📅 21:52 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29129">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NwvgUdaQLB47huEDjWHBasqgFLVLvOn0pl4G_Sh8FGjQzvRc3BGJamvYOh33gd1EnrBD7aC00YaNbBrzlA5IihgUD8s-bRKjv3fCt8pcy0paD6DGrA9WJ1634hIO7MSDDJb-9uWDJ5-f4h4u3kgvxzs_9zPEjvUgd9wmAmqfu-VWA8QcjFTLzp1gtnIMebfckW4TY8X1A2c1rnwUmKx2Qyq7Nc7pAy9cfWv4C1qkNgg_tDRHD1qF7gDnTiVN0jAEpJVKduPSm5e01Lre_8oNU6_--FDjVJ5GwI57fz1j9tL2YRqm4ibOkWAm1REO3YxofUVH_3trKQsqKEWJvMm_yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
🇮🇹
🇮🇹
درهفته‌سوم‌سری‌آ؛
اینترمیلان در دیداری تماشایی و پرگل بانتیجه‌سه بر دو ناپولی رو شکست داد. اینتری‌ها در این بازی دو هیچ عقب بودند اما در نهایت سه بر دو سه امتیاز بازی رو از آن خود کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/persiana_Soccer/29129" target="_blank">📅 21:39 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29128">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">‼️
صحبت‌‌های تند خداداد عزیزی سرپرست تراکتور علیه امید عالیشاه بازیکن گلگهر: اصلا مال این حرفا نیست! در اون حد نیست درموردش حرف بزنم. اگر حداقل یک بازی ملی داشت، بیاد صحبت کنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/persiana_Soccer/29128" target="_blank">📅 21:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29127">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/313c2c9c97.mp4?token=j5xcIltAidjp56eyE4nccj-Lxct1lG3m4TYsnLdD_FLJgS1CQALDKfaGHdHucTrrHxsjTltqFJh0f7a-xg4ZOEJAtP5_SH4UuNrF5-Py9QPu9f36-C0bAmmeHppu-unocIE4Jv590OjQK95k00ho8HrRKSQWlLXLrN0pwGnLQVaPH5Ijibu0tIh_UBReRQcXn3l_3V2gEnnmaIZn7Ogm588iBp-g9UBu9ZBiKTRK33xTNKcVyYbSjEIZrIz4JOz6nCsU6gbB0_W6rIFbf_vh0yljk1RWFpZVf-GfhrkdGxfAgi3sivWH8cI7XPFXukYZC82kpkPyDQZ8XQTnW1oWWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/persiana_Soccer/29127" target="_blank">📅 21:13 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29126">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uJKMq5MBB8Oo6-xtiCmEEh88TtZvZGFESZ4Fgtpz2IhXMNxwWXnZu3e-XnPIMRfN5pwWlYxtH283bMgo3RYmnjNx8xG267N1XEVuh3PyCDaNhUloEkaO6iQPNiZRk6JsXhw4_RkQpVpl939Sp5LrTDuBnLwvS4qlAcp9KvYzksW-fRQS1WdwLgm_ELaAcVNq3iPg384QlDRGCIkVl12gw8JPXY16viIG7HMGeD7ZNZszWMNOw2XRpq8vA70Fvn01jP5jxOfaBuY21X8shoYhY1sSJ5ksqRvh6A4E0higQpJc7MGj6CeizafHQAj7otILvPGROLs7c1gds5ThrHaB4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
روشنک مسئول مسابقات لیگ: یه چند روز صبر کنید مشخص می‌شود استقلال قهرمان‌ اعلام‌ میشود یاخیر! احتمالا امسال جام حذفی رو برگذار نکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/persiana_Soccer/29126" target="_blank">📅 20:51 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29125">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JoB1OqMz16KKwAmY1fRYX5FAtsHYpHZFDTa99AOPMdZF524bEGFDrahTfwOtThuFDTs-_7wcvxj-zu2mas6FtP-SQJ8TdZZRow9VwlOGEJhiw9TQ3vRRggHByz6KjvFkXQwWXGnA2z1r3srRGoPelkS-X3NtHMFRndcBnifsRdkorQIBCWaq-NwlxQgje8M5T0IWIUMW1AY3Nbcnp22UQRoGjCrO7rEK7CK9lX23GGifafoUYafWIH8OpszAlefu5eg0sTVR5u7aTxmMU9633aKawHVPiDaW1QZIZjq84uow_i88P0eV6TvsinkrthO3zNXNwJHMH-T9XjPkXlRsGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
پیغام‌سهراب‌بختیاری‌زاده به بازیکنان استقلال با خط‌زدن صالح حردانی در بازی با آلومینیوم: کاپیتان تیم هم باشید اما نظم و انضباط تیمی نداشته باشید جایی در تیم استقلال نخواهید داشت. از هیچ نامی نمیترسم و به راحتی کنارتون خواهم گذاشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/persiana_Soccer/29125" target="_blank">📅 20:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29124">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SZPt2mIiOiii9SfGn1V0cDAx2kFk0n0iZkuOo7W0rWBsfpklfR7YsgXF1tJnxOEz6sWULSl1OkFE6t7tUvfsQ03keJ6kxQFDIf18bjTQsRZgw_mQrhnsRLv1FEDvwTRZljHbu7rh43B7tsLTbgcY8nLxOWSZ7YrYENWkPeZDfHd0gCSgT-TGJ7rnhhlS38u6RAI_Xh5nCkZE2KlfLjzOh9orA5MLIB33gIerl9e5wUbrpzgaC_JbZgjM-0hACbNSqqAv7_0v8saEtiR2i3-h-HF3lvwTUAe8LKYHBtCcaMf2KabsQeTrUzZ5r8gnS6XeysMN404xoQ_R3S7TIlsJFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی؛ اعتراض شدید بازیکنان گل گهر به تصمیم جنجالی داوربازی‌امروز با تراکتور؛ در حالیکه بازیکنان گل‌ گهر برای ضربه کرنر در محوطه جریمه تیم‌تراکتور بودند داورکرنر را به ضربه دروازه تغییر داد و بیرانوند سریعا حسین‌زاده را تک به تک کرد. بیرانوند در حالی مسابقه…</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/persiana_Soccer/29124" target="_blank">📅 20:25 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29123">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/397e2179ee.mp4?token=dpJW6g5Rjux4UW_z44MDQq6mscylka6YnuGCfvj6GTtMks-M1eXzow-IAProOsFsBveI6N85XKsJwBIo0RJz1DYCFlf_HrqagfuwLRI_KKdgRXPKBHHgu23bQOdhkpeieH4DdhuSDAGP-EmtyVLN3EMuGLhcqsPFYAEhg95ViXs0Obgh19tWZaSOQyPXiCJmKARdwHnEEuSgKEKhxtF_H4zjq597eynS6DrH-Cz01m-yYOnzHPPvobzyslhujvZ4efSz6vf3Ayfl5Rb7aPqW1r2DsyEcoCCZshNXHaDklI6LQfCaDlqyoOqcwZKQraeFGZjDbXxG78uOIf-vSWt5-pFON0zaRFv64E8Q8tAEtJEqBhWkl_pLqe_CzIDLNdI8bq1I4qBddNCt4GeUPIgVTG-8JuCTcukdoiuW7zdTHPDK2P0xIEJnASWHC5Hme5PJk1y0T9tSEjbp0zRfJGYVfR10hDT0WInQ6OmdGbq5V1AV1V-BI9Csm_GOl0jvtWy4f3oOFpkCJmjoYBOg9GV1w0d1Fg3r1kW9C33R_rVxdiH4o3nec0eHrP5c4djk8jBGignSI9unRSyNNGsWMO6lUGXKZxy7JCAkAPNwbxJ2H_IaFIqHHSMX_YFM94zkstSX_7GqfYRDJQeyFdz2gWpNwJCIqBOyq8cPt6yu0cug2mI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
چهارمین گل حسین‌زاده؛ گل اول تراکتور به گل‌گهر توسط امیرحسین حسین زاده در دقیقه 43
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/persiana_Soccer/29123" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29122">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y3u7zN2tjDQzp1DPz_FKwiaMetFl-LS4p149dHZL4DASuVc7Kw4-bc8jYZvIfW9kepv0Ym8S-gVvN2uxtniTBYlClUe-zR7-X58QUWhcijoZjddXROdgOpVTPxBgqOrrAARKL4oQvbNUw9Eqf29qKGTi0TgOOcT05CgJYw8r9ByAf5ducG7OG9zYi301KtdMb1g2flvqOi01UvyR41VwtjPCqeCe4BdETW6PMvAH7qU9vkplZH5nJt4HGW6CqW0V8YmZllDvkgbPXHIMb1VeJrygTNwvbOxuTPalD8OcPKlBqNlM3c7T9qhBw_ynod5PTQdUUlJorC2a9KLgS-Bwhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
ارلینگ هالند ستاره‌نروژی منچسترسیتی که امروز تک گل پیروزی بخش تیمش رو به تیم لمپارد زد به رکورد 300 گل زده در تیم‌ های باشگاهی خود رسید؛ نگاهی بیندازیم به‌عملکرد کلی‌این غول نروژی درمستطیل‌سبز. این فصل به احتمال بسیار زیاد هم اخرین فصل حضور هالند در سیتی خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/persiana_Soccer/29122" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29121">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lfokdBVAU6grW5pAAh0wsu8bKTJFn3S-oswTJbJESxCIpWHim0HVdZPEApj6yX5DQoXS-dA4g0wCyVQ3Nzzmm5qBqJ0jsAwCs1yM9wJZxTliTlasQKxLbAu8l2iNu6rXxzs8n_xRnqOJ_DHY7mb4gyhyWnJhOduB5DR-0MNNVEAr9xwaUcKidsMcSXLCP3Fba9azOksZwWwJdMkhtlFwcyCoEuXU3xKtnf6RlGq96nS8unQ4r1ZPC6JQZPrjI_xvYP2-6MYYsblrtHqLNodqhyMNqN0wt5YiqNTUwkpvwP4IOVxXKLNPxOgFBJ4u-13KU8f9JkivZ2iT7O5fEfdhjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔸
هفته پنجم لیگ عربستان
🇸🇦
الاتحاد
🆚
النصر
🇸🇦
⏰
ساعت ۲۱:۳۰
🔴
بیش از ۴۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/persiana_Soccer/29121" target="_blank">📅 20:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29119">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fedqSG8yGwum-Y49iHJDlOoaGV5azJym7WmEyOIdXKajHhejboNYG2MqJWDo217QndVGS_QA2dQMwz6BZgJtV25oOlVeRWvknFmG4IELFVhX7RzL--22tj-5z_uqPZSY-X6jfFKqgeTwMvYhyn9yvWKuh3uC2qXvsVy7B0mDMPCSR5qrPIncPazQbI99YnhLSI5aRXRf11atY7rUQ01y34vpbNaPvxt2FAfduKtN7WPhmc2MZh-km4nO8-nFwtGVoDK-Aiwu06BXGgSNMYMQGhwwTXxir_p6ZER8arzTNYuQgAyeQJrQbMrD3xiWwboNrZQnO0LD1DX_heOSXiJMAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fDzUGwconhZO35XvDTlMzraXzb--yicwbjvby9SElzQCBxtqO7LZeQlngwZYdDt3pgAq28MAxbZo5bqlBdtZR9SaKPwCkHpkX--e9toJsAfDkAXD2w4273ZPqahxf6pH2CMLuF-4mrWVH2Wzp0ASknyYOhishjdsrMymEEXFTl5phR7-J6GFunQw5JfxwNMwZkfhiv6FpZnHHuGaoRgFu1hNo5vHUBfKuKZX-AESZO14Xtj_rKcZgmr9gsfQODIkOsD3gBnIQXZfXImo2kFf_P1-MV03Fm1YyLePnaa3pOljBBLopcOFOFVksHAvyojGQQ-VRoSIckp4_Pqmd7fxxQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇹🇷
خبرنگار باشگاه گالاتاسرای ترکیه هستن که میگن امسال گالا قهرمان سوپرلیگ ترکیه میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 32.4K · <a href="https://t.me/persiana_Soccer/29119" target="_blank">📅 19:46 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29118">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DARHFybZGpY54D9fP342nFE-N5G8jM_SXz7oXq7BnNPRfOkjldt-TlZvdY9dTpYexrH8F5PftGWQofDZCqH8rki7PGFmk0bQnNE71i8N2Enx9nYT2dme6PbvjAbits8wrre3lu1X4vMQe6dIFm_qzRLNOfyU-HPmZEF3-c2d3v6cLQAO7O1QnrvNtBPKRfGKzQUYUbjuoAH5ISK2fqFhT5Adhmli5wFAapBgqnKWkYwWG7ZCHbL3hazG_dBQs3pS2NE6p7RsAR8ywzbDm0tx8R36tuO57XwBcRifo6cRVtatMDFdDAprpKpWD8Op_OoxhhVG4ja7rJKmuzUHCCbWaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
ترکیب کهکشانی و پرستاره بورسیا دورتموند اگه در سال های اخیر‌ ستاره هاش رو نمیفروخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/persiana_Soccer/29118" target="_blank">📅 19:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29117">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fdd45dc7a.mp4?token=QA2-oUbJOg4C-FIiRJTWYA5m7F6ZZMIhv7ordwXYEGXDbjMUJ3m5fYWdd9t6erDfQOE4boMH05PejmyJ6p-C4FiC73Vh7wb1DmR0PuSG8kaeKvXaHfpZPDzkj6sZFHFEGoBEkEZjJbPOO_Y6xoF0S7IaTy2v84cXR3MxBct4zTOwGwSxKTKDHglXJCu1CbHg6Rg2RDiio5Xcds8zqDMQSpHxvHFE8j7DgqD62qnwf6H7JRKOyyyKb3aYspPN87K2NIsWiT3Jp-hztJHVu-x-lYCar7ZgZpCZDi-HmhzDLLigdrmM6alvmuijhvR7U1cxkXZAjkmiVDjtfY5NSJmcMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📊
برترین‌های لیگ برتر پیش از شروع هفته ششم رقابت های لیگ برتر؛ حسین زاده، بابایی و بیرانوند بهترین گلزن پاسور و گلر در این فصل لیگ برتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.3K · <a href="https://t.me/persiana_Soccer/29117" target="_blank">📅 19:03 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29116">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFfSZ2BVOqIksreZvLFlXGzn8bK1KLnVISCbYNmOnuqPXKbpI9n40BZyfnzUnXkW8ICmVIWI6urzrouIr1_Y4bbXpCP_bQTfMe1SXiiXRhx_sCWfBr2wRCDwJxuO9aBM_k26MoYqEFbfjEgD7wCW26V6m5ZaMwmxDzUWD3KAf5bdEVwiUQGWccO3ii_xahqxLvsXaNmr_pT7kgf0NSu8dkJNoHwVK0iN7mGqDd_CCe5wR9lDadPBWLiElyvhOE-_dfo8JCTsNLZZjMyH_wrC1ls8yliXEne-ptqemcEPDkGXNMaIpQJZxPR9ZEWsZdgMFf8cXuhT4QLGC_zJrL3pFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هانسی فلیک سرمربی بارسا: یامال یکم از ناحیه خصوصی احساس ناراحتی‌داشت و امروز جدا تمرین کرد، اون مشکل خاصی نداره و با ما برای بازی بعدی سفر میکنه، فردا تصمیم میگیریم بازی کنه یا نه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/persiana_Soccer/29116" target="_blank">📅 18:34 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29115">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oK_68ZN1nHLWoN9e9tIPrxnQQ9jiPgJ25OSth3eC8ygMWr3PJ11DcYNGxO_vL9s1ONGS0LvGwbLfCtOunYLQUpUuRPe1gHkyxKll31bLJ5eFI8P2cfNpcrSMGdFe16jHb6XCln3NoBlREiLOxecr1djSfYrvauE5Qb-rlsqLdy3TXNnZl8kgigCs0_Ma02heSZ7KdQcKOkj-71hAyc0sI97IwetVzK8_7YywrFpHX8XTKYjyNrh3eZVL-zSh8pjSy2M6leNjisAQeFEGc5w2MGMrvVH3DMpn9WuHXsQsmVM2XGpzNCZ8ItHVyii8bRWlSPEhlIHFcRlJIJD5xKI7bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لامین‌یامال درمورد دوس‌دخترش گارسیا: هیچ دختری تا به این اندازه منو شیفته خودش نکرده بود؛ این هشتمین دختریه که لامین یامال تا سن 19 سالگی باهاش وارد رابطه میشه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/29115" target="_blank">📅 18:22 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29114">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c8b6e65ab.mp4?token=PuSPnQNto5TX_uUSFoffTTdGZrSXVcjMervnHF7KIoby-ib-zbDwD7dhuWdFr0vOXM9RSO4QJ9zt1BFV9DeKu5LAbLeHexHgWFZ3ehxsvL1lC3CKSVulUInjrjSOuy30cALLWQCe3GNBHAztjzSZ_ihN4xBX9IOceGG6h061u8PKy4BKgJ4m61DSsgeUzwbSLTZCEIDZcpPHgRDYyGLBPAnd2WFzJczAqxnhx5FICz4BZ4qzttpLE3PhL9YTqCOJWs0koxXErSDalBQlc_OAFUpvfUuBpLqTmuRnm9IkEPqWP4pWWCwJ9nM7IQEoYcOoOTzUDzNKSN4dmI6PzcQ9iQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فرصت‌سوزی‌های‌عجیب و غریب وینیسیوس و امباپه در بازی شب گذشته مقابل بتیس که منجر به اولین باخت کهکشانی‌ها درفصل‌جدید شد باعث شد دل هواداران رئال برای یه بازیکن بشدت تنگ شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/29114" target="_blank">📅 17:54 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29113">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RtjtEOmcsnJXQyrMlch-s5XgZyAsnQ47t3iGLQADUGTYbWcvZqx0MikOl28YOZAxC2dvdHWJmYdjQ4WbeZD4O4uCKS9pN_Vxk4loYDmXs5co4mQ8PmUmTHH2HeJvfwq-l8fgxG-3-yxkCvsR6RgEkZxTtJzYychji_PBSkxluNvT51yBwzq5n3agBgYD14H8UKKLiVbDXEx2SnbGbFn_aWwKBZGc6-zdAi81D1SfDZSJyp92ldQezL6gvBNbxI9mj2UKwKctT1SUUrs9_zKZ0YzfKOFfJCFQVA2aE3ljsMH3HJTpRSUMGmq7yUsFmQTwVYRRXkSaorx4msO0gysZvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🟢
باشگاه‌آلومینیوم‌قرارداد مهدی مهدوی مدافع راست 20 ساله این‌تیم روچهارساله تمدید کرد. هدف باشگاه اراکی درامد زایی از این بازیکن در نیم فصله. رقم فروش این بازیکن 450 هزار دلار تعیین شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/persiana_Soccer/29113" target="_blank">📅 17:42 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29111">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=UtI7-NnGdnwyzaOGamBOxUKzQKMy4P-TywNABOcn3A1twl-oeDkhSKGUhwB9WPsE8O2pUC2Pv1LV_hkfeHygldVQOq3_w32c_-0aCq6BBAJgeQE1zuLkRYra0yjWNEDxf6Fd5LDXxo92WPW7cOrHGXgGOuTkIPcggeh-ay8igxPMLt7S__RzPgmSO50_2MPR1OElTtoCfjonvm-BAAKN1nqrPLC6BKaxK-FIx3GCQUxDU5Vlc-MkMskUOhVRHn6_ZTDKiZ_4rgpsSpuXrwsXUWdWsTiGaNP1npxjaNLddxiMMDuj8c8y7daoOL2m9jih6GYCYZXdxeh6dmrzaVq9gA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ca78fd8d27.mp4?token=UtI7-NnGdnwyzaOGamBOxUKzQKMy4P-TywNABOcn3A1twl-oeDkhSKGUhwB9WPsE8O2pUC2Pv1LV_hkfeHygldVQOq3_w32c_-0aCq6BBAJgeQE1zuLkRYra0yjWNEDxf6Fd5LDXxo92WPW7cOrHGXgGOuTkIPcggeh-ay8igxPMLt7S__RzPgmSO50_2MPR1OElTtoCfjonvm-BAAKN1nqrPLC6BKaxK-FIx3GCQUxDU5Vlc-MkMskUOhVRHn6_ZTDKiZ_4rgpsSpuXrwsXUWdWsTiGaNP1npxjaNLddxiMMDuj8c8y7daoOL2m9jih6GYCYZXdxeh6dmrzaVq9gA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇪🇸
خنده‌های‌تلخ‌ومعنادار ایسکو کاپیتان تیم رئال بتیس پیش از دیدار شب گذشته با تیم رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.3K · <a href="https://t.me/persiana_Soccer/29111" target="_blank">📅 17:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29110">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/abQQEqLYzw2NvKF0P68I-0N3ZIJWJwavjnsp-A6SaczeDcmp8y5o2cXH1fHs0kE1gZp51kzUbICpLuU-uyVvJHxsjqTtJLC2DDHZkqyApoQLk-dtOiFCcIPzFaQ8gBlxChwb7Lkye0ZWzf5i2EMth2nF3Sc2LzI4m4s4tFYHltFUke-y1SVlF1Ez7wNPXHmECQt3nhK_wCfOmOXa8b2iSRBXr8dHJffTsTNL4CexAcI7039o4y6BFYcLdkBDtqcGdUU4DENxWh-BuMcTiCGOIuQsGbQ19RkQBPtngSIurGO5lXACWbhXUrVDRj-RgYTuTm6gHX8ArhfK_adlZpmIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#فکت؛ درپایان‌دیدارهای هفته‌ پنجم تنها تیم تراکتورِ جوادنکونامه که‌موفق به‌ثبت پنج کلین شیت متوالی شده و هیچ‌تیمی‌دروازه این تیم روباز نکرده.
‼️
همچنین تیم‌ های استقلال، تراکتور، آلومینیوم و فجر تیم‌هایی هستند که شکستی متحمل نشده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29110" target="_blank">📅 17:15 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29109">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l00_fjHICW7sldOWsOoTNR03WFIqHxKss2-d39TuTCXbW-wGraYDBXc6tx10JhHEPWmiwP0peWSAZW3zdShrYDPrUsEHmKKV6Z9TBjylKuNwRhQGE3aQ7Ji1K8nY0tx9nlQvwPRNzqpeMD_elI89Ernv7jNVtsReaiN09888ww5W-XntX7vKAua8VBbVUQWI0xOX-FAz98z27zJM4_1Rz5emb7AOrw_ILbD2zc6OYcbwPB0RhLG2o-ecNkib2kwb8ofz33vLXWxB9qrxosU8B2NnMpti8QFoUIH4-R9-T4GFAm1SyomyChH_wekTjXOlvFRmt5LzXbSFq9GMDYo1IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمد خلیفه گلر قرضی آلومینیوم اراک علی رغم تلاشی که کرد دروازه‌اش مقابل شمس‌آذر باز شد و در واقع گل بخودی بنام محمد خلیفه ثبت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/29109" target="_blank">📅 17:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29108">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lkSZWHyVOU0WjdABo0njIqlxCs1lJ3oGDYluxq4x2bNsHf4OebF37t4Vg9d4cFqk7g68z1yk75z71qovIQaWNzlpNa7nb5FZxvTqCCHdWqrreTiP2SEe6rRRfBYcQLdYx3UxRKL7nGDthz43g0slYJWkwvgKT8_DrJjsg7fKjoRiXeeG-M0qGLVVBHvg10GDdVeItyBE9nVfzf1S3_ksfqLCUD4J4qDDPLgCwrMOFMQ-BYOJMiSjj2EpJ-ce8PgIPHAHaUIFk4CcWQNdgVyQFyQG0lrcOaPIEXFlF25V1pxifsrxUFRcNWEi2nci9bZbY0quVAv261ZMdt-_oB8y4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
برخلاف شایعات مطرح شده؛ عارف آقاسی مدافع میانی استقلال مشکلی برای دیدار با آلومینیوم اراک نداره و فردا برای آبی‌ها به میدان خواهد رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/29108" target="_blank">📅 16:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29107">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sxtgmmfKvnq2A4DidvOtpdu87xHF6zYptHKOuWK_HnPyFqOnR5uxovfPTBIg0a5pVFBnbjuXYWRNqVW-O58YrAaBNCJ7q6-SOf7xj81onrhE--Ne6Ale3-Cf211Nikd0WSXt6qPVitl6_t01CI1Wp79tKVFRne_LQ8UMyt73zl_KgHwF_m6BGGyaOZuZQt-2ftT0nmjii6WpBd-JkftNDfo_eWuQRO_NpEmzQ9BPAWHIhVgxHegyuGpSU2plMJ3vOL6E8Dah_goguD7a7rpkRDQ9xfpnuh12pLeMx_PhV73H7UV7tNrXfyyoJL3Z1dwyPNqWGFvv6RvKsE-BGD2Jbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
خبرنگارمعروف‌شبکه DAZN ایتالیا که گفته اون اوایلی که بعنوان خبرنگار مشغول به کار شده ماریو بالوتلی مهاجم ایتالیایی سابق میلان بهش پیشنهاد رابطه جنسی بامبلغ‌بالا داده که او رد کرده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.4K · <a href="https://t.me/persiana_Soccer/29107" target="_blank">📅 16:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29106">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d3e17cbd64.mp4?token=eik8Va73xn8AhZVz1_RBi4cFEn5m-Ns8s-WCPVm5DOl15GLQNlw-8fGJnqogbyqM58sIFxrhHv1PYYP6XMniDBNhQsz4BTKdvGT-rasw1-cZ_y4tZZmxQBzdMdF1yyDJ3Gjf7qtqbBypr64ESKkDN5E-p1dydbQ9RduMp68Gb2fcuYaHeL9nFojDVVd-qh1I1T5a6jpakIe2jRdxzZzSnscyLHZ19bgwGG_-4QH3KzUWTA0wUeSTekzlzoqID3ImFElbXkqVBAW9ul1z1UaGZrg_WMQtwljEPnllX5789HBKCvQB1A3bQ_Lu366-Z5QRH_HEitkAaVcx97lvmF4OBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پوگبا:
فوتبال‌خیلی‌قشنگه ولی‌خب نامرده. ممکنه امروز عاشقت‌باشن ولی‌فرداکلاً فراموشت کنن. امروز میتونی یه‌کارخفن بکنی، فرداش دیگه هیچی نیستی. من دیگه‌تمومم‌میفهمی؟مُردم. پوگبادیگه وجود نداره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/29106" target="_blank">📅 16:20 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29105">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MAlzaRuulhHwYERNKQuS1Jk3m_TbByVhDzFTBjB4IIGzAKn6vnHPZtC2-PuSM_a858Ni-pZ7wM4zJvCYfWJovfx_ZArDGF2NSg6r-N3nwpvII1mqdMuOsDApmRzd8ku4giub6Wnn2PZwaNrZlfBPyMy1jzYztZUbMiy_mBmD-GCDwbTbE6ETdnqFynvJYeN1HxEzMYYrvgL8RQcbKmAEFqWA0WlF8AzJlK0trnan5U9fscwDLiZbyX25hZfvYwqvOURhGZ4beunrElbxmITZoKw5WH3kK5TgOhdglY7Mn_BPb0S_A70_gS2zPHF3lJEqsBgjOVSPhR_LR2huo4_rYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
برخلاف‌ ادعای‌ خبرنگار ازبکستانی؛ طبق پیگیری‌های پرشیانا از ایجنت خواجه اکبر علیجانوف انتقال او به پرسپولیس منتفی‌نشده است ولی باشگاه پرسپولیس باید همانطوری که با رقم مدنظر سرگیف موافقت کرد با رقم علیجانوف نیز موافقت کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/29105" target="_blank">📅 16:10 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29104">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BrgbmCotTZEJjCN7yIKrnr2dmdItcDiB4QpIMTzgBdqab-W5q-dNL18m7pM66DOu3hQuitRMWEdPx-lNkkzHIdgW58Lsw-egN6RsUhjJJKs_BtXzrhZ6GfC2gkJjr-CbwgaJm-SMAF0GCSoLZvc9eJ_6KehOwqaZ0UR_JfUA5JkydWLmRWMKT4IfJlOPjBlfW4cKiDGQhjpqbUKy8jAIi6gj1trWhr_baDuvJphwkFpE3FFWWxaZtqsmppMl3Uhq4aCfnw8jh9CmyP-gpp2Pm0pMQhypVNGbqbhNwwCaw9bRr-v3Lrn8hzg96uni9NLlObVyrdetN4FKI6pYJV2Gfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آنتونلا همسرلیونل‌مسی:ممکنه درپایان فصل لیگ ‌MLS؛ لئو مسی تصمیمی بگیره که همه رو شوکه کنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/29104" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29103">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cjDW7bZnDtweiGO5ydTyneQuVfigqGKjY5wSIvURi919J--y-WCQ7f1SyCbRQgivlnkwkqP3bMuQbJUtqWE3r4zwjeEwmUs4KEb3zRVchQ1DlDfzFHHvgiCjNd1Yt3jqiiDTZQak3PXsmXQz8WsPXWwX8BcWCCdNhNXapmJRMdmU4OP3VBalR0hJMi8mh93_8puySX_5JGR2ADx-3r7qiRmLDM740MsCG5ryFVYeBdFde7Kd7ZEhOXo-FM-Q85GeDsoICaxxFMQojLJYqwInSmda88rySnLW9af57JqGS3cZm0TVYKo5JYPx0ItX-_cN5PmlUBETnOzLgNJtX4ucSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نادر محمدی باز هم روی پرتاب‌ هایش پاس گل ساخت؛ هرچقدر تو لیگ ایران قدر این پرتاب‌هاش رو نمیدونستن و مسخره اش میکردند تو لیگ روسیه هر هفته داره پاس گل میده. چقدر هم خوب انداخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/29103" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29102">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c7nPEv-2MIgB-5wXaS8DFZkPxwYxbRYWeFoZQvWJ6bpO8RdHG7EhRWE-gKzID-IfJqGX9NjwODbLIxldQ0kqvst8377kyaBVec6j-cJzDY2Ye8ipacl_m9lMWsntAyBksp6y3rTWtMbSgcovH-R-xXjJx3OqUKiVlT6x-0qThWZXa6s9h_nNklAbHniH5sqpAX84SxC5Ia2mXmG64dVVIL7ceRKgz6t2C0yRwHD6-2_tWpdLsVcq5VFL5Tp1_h-6WIfuU6Q32J7kuJLSyCBMYaU4HQyMcEMtdJmaNmrSvDCnkyNtO3IZoUcOUY-xmbUzaoEhfZx6XwGCxVELIekMNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته ششم لیگ برتر ایران
🔴
تراکتور
🆚
گل گهر
⚪️
⏰
ساعت ۱۸:۱۵
🔴
انواع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔵
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/persiana_Soccer/29102" target="_blank">📅 15:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29101">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u6-yn4_jX1IEjLVfqu21Yh-E84p7l8XzL--a7IZxztjeF1rnOmq79t7t1DE6ZnuJ27jFs2ZBvu6o9Bpl5_ZnRcd7fStKoah4WuVaL9JfvAw1D2Mb7K1K_M_3SfEVHiKaO_6qfGkjUcyUQlfuh-OZCl6B-CDPaO8teUHUXbGrLUNW5G_T9xn2Iw2OppMtt8z2wgz7fBatKzcu7JwsQ9jBfvGDBMbljZgpJJ5Lta-spva7mX7U1-HuChQ9FLhlVnayURntAxNqkZ445EHoHvBKlQjEzsAgxXYpYT-fXinglAZHucE3MWsqIdS6Bvku73cJz6ehKo4vHdpVzwCZLFIi1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌رسانه‌پرشیانا؛ صالح حردانی مدافع راست تیم استقلال بعد از دیدار با آلومینیوم به تمرینات آبی‌ها بازخواهدگشت و کنار گذاشتن او برای همیشه توسط کادر فنی آبی پوشان صحت ندارد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/29101" target="_blank">📅 14:30 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29100">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2VRMkdNrokvwjM436R7KGbg-YNPikpOMpjwFBtTX7r_sGhnHTW37Rja5SurNwrMUCUOofKeSlUz7SV3j1FK_buepLngnnJ7bgRNEbbHnW0ZcCtL15PX3EdGpmkxSCsJSEzXfCWfRpzHcoQ6qr7KyKsH4GcWpAZnNpdRKWNHqlbLQjzrSY6tW9wQalaZ3Zok3wldZ7WLp4n0C0Tn7FV3hT7p8p0Ewa-T3FkVIxE2foZLw6fvNZaFAk4nZ5W6GL-GJZjtMXy3xsSBnifHEh-9g9LB0OO0zOX8gnSDFsD-Gr3bPiS-N3va0XoYHUtGpKmFNolQ9MJakyPZjeIF5H48yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
همانطورهفته‌پیش‌ازتغییرات مدیریتی باشگاه استقلال خبر  دادیم و امروزهمه رسانه‌ها این خبر رو پوشش دادند. حالاطبق اخبار دریافتی رسانه پرشیانا؛ مالکان باشگاه پرسپولیس درپایان‌نقل‌وانتقالات قصد دارند تغییراتی در مدیریت سرخپوشان ایجاد کنند.
🔴
طبق‌شنیده‌های‌مو…</div>
<div class="tg-footer">👁️ 50.8K · <a href="https://t.me/persiana_Soccer/29100" target="_blank">📅 14:05 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29099">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WFd8RE17VbsAEIaIpIaq9gedMts79L09eI4CZM8He0ehfJOqdw12veZFXcq46UDxJ17NwV3ODw9d07xeL4agQaxBdOIi-JqMnd3wDXfVVOgLX2sS2Q0eAAFOjIOZXLGZZIssIMPkoAp2WuU54aXXd-nvZpg_K4OZk_syTYCcChKKMk55fZg82L2nQWmipNSWkFlHOHUAV5nwUtKlMqwlaEFZNSP1-SSh2orF6rDVV-dv8uIMKogymZIdCOZu75kRXi5fLCDJOftaAh3tGX1-ZmoYVG2VqpKeaaAruEkM4qKpAf9LBstmDQr-ib4aPxvEybG7j3APUXOPhO8UPMfP0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ریکاردو آلوز ستاره پرتغالی سپاهان تا اواخر هفته جاری به ایران خواهدآمد و در تمرینات سپاهان حاضر خواهد شد. او مشکلی برای همراهی طلایی پوشان زاینده رود در لیگ برتر نخواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/29099" target="_blank">📅 13:41 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29098">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z3jLaxrmUPDCizc2ohLL80aqgWSPy-iOcr8fy4unbn56RxUhRO9KC0LkkqbK8dnQN2VnWERcxHcpofszwSmCNFybUnCzSpf8D5X7CQuEywXbkNET8vLit0jBMIAo9A0gfICZPm23WqSsxNG3w-f50ZtspWBe1JLBV4dA20b5_AzT3UbTIGdqcpnqh-HjMoIntFAezQjyz0pBbHkxoGkEWPhAwUpoSQubTzVNozu8QLskNoDeLkpgTdY5XtWYo_VS2b3QOTvEGl0oM1Bt4Alu1EJfs6KK-PUi18iRCPDWiXcd7znMuXdhOB1xRANPrC0E4B5nFQtADE3ir4DNGCKV6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29098" target="_blank">📅 13:16 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29096">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JFid__ILmYzZbUFoAubXxIogmn9GXqLLyWm6QDa6BAyFmF-npF02PNI4nceQqo6W0yziSr5-n3Z-SAdugzt706tcvhwUQ2xMDVe--sA-hyl_31npL7Jnrz7RZVclQoGLkyNyJw29DFWQcSki7J2Hx9Fpy7GbJ_YwxpssZpugKp5S6sAkIMnju1i4tL4y1X2JROr7wWzGqSlFQfJxw4t9ybMmqiOArwSzYORviFJZPl3zepukNtF-JpnArImmkxfOo1KlN1JqsNeDPBGEdh8FOA307D2vE7e8XqfoKm8fG6PDzH2uRKzuSpe8drWL64G9J6TfNTFo2f5LP3PN-kDcsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HPnPp3xjViI4P5lXFVx9NCxw0v1fgP9UpoLHbPvBs9lq0_dac6_G1nVP3-i8iwM5PXPBNKKULaZA_e-Ch7Ejcy-zZMkoRaKtl-AJUSbhck6a6ZRQUNYLiYmz3GxhPOwuwZoujgPOJYGnfkRHCQ6Z8a_AI3Dh9sqwzjNurBcaabf9gfb3oueEITSzWdw44f8HUcaMgnIsxGQ2mZrsb6b01KU5m2Ty8BIhCpF2lvsG8DKVRdTwdH21Fnnif3E--xomRHpYQW2bjWLt41o8jVo-j3cobsggQrTQonj8y9j6t8boYH0ZfwVclLFoASDy2_ioAn4LHAoUTWErw8QNIYxMwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوترکیب‌متفاوت از تیم منتخب هفته پنجم لیگ برتر بر اساس نمرات سایت متریکا و سایر رسانه‌ها. بازیای‌هفته‌پنجم امروز شروع میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.8K · <a href="https://t.me/persiana_Soccer/29096" target="_blank">📅 13:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29095">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IFOqDs8Joo2mNbgP6srmvH8HnXl718mnpf1XpPT6km5LsdNk3IOMhb58EsMcq-CxBbz_fJ-bLvVksXL9OEoPMKzLrDaAyceHIMEisxTCKUud6y0LR5G8XVWduqf-gSXzoX9p9KyIdoFxDwg_gZAF0rOJwfQT5SbhDd6tWiCLYWKUsZwvB13WQ9Sk-fK45fOE46av58SggNVO1E8h6yaP-lDxF7hM4jwdGD37PdGsqF50hJJA2_CYYVDWrLbKeMxBL4NVS9ZDXLNjUVaRhzANj_yYMNW_8_uYwtQPlHt9uVViT6Ri1nj01eAuXYjTh53vsz7gfEvO40LnwDNQupde-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ویدیوکامل‌قسمت‌اول سریال جدید "مرد سه هزار چهره" برای دوستانیکه علاقمند به دیدن این سریالند.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/persiana_Soccer/29095" target="_blank">📅 12:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29094">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bba3aff6a2.mp4?token=Gj3jS6zpzoEnH0xIdwl2f4tmJZxCd9bqXrtCR8TwZWQoluGD5bB7Cdpg-xfgCNNpBI4Lg11EONKTUoUmsAoJZNuCQVnOFttMNbK52ZCA8shAAphslN0EP4KHI5df9MTSKA8IGzxZY15wREAFabE5Dua4r14G4QqqqgatUaXMoWyBBtH_qGXDXVFo2k-u00jg3__IaAnqmwD91l4o7GIdaGM8Apl03RKq4yM5CwJnOqQtn07wji5JcChg5LSaoEricf5KwovEgpXvlXaUWor0sKFMHc0__sCE8upBr89kVVQ6LpjFNkCjVnufWFrk92nmJE5XMIlhS6A20Laj5FlnPw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
والنتینا با اجرای سه حرکت یک‌ضرب قدرتمند و تماشایی با وزنه ۷۸ کیلوگرمی در رشته وزنه‌برداری.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29094" target="_blank">📅 12:14 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29093">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QJtYuHCMTNARYo2IC7nDbxw2dw8AY_dZA862IwEusPwLvuNtSXB892PU47V0okKy047X5flnakBeseN1PfUP1ol1uPYcpa-drab66AOqF_z6HQ9_DWbqmLCDUN1yOg1uMxloa63Dke77vK8VK0ZoFF-4Ylliwr8wcbt0h6gquAFJjQJJP2YVVOy5Pu8P5U2gYjQm9K6_HEvFo20rQMPmuJmOPs6ENoNS3YggWOQ_liNA096KM6aFNe6-90uya1ExAP2urjwkS8jM3NFAiu-y5c82uW-o4nQZGCVGWvBGi9zWAVM_4tD5j6cbJNIXDvlyJiaKKaKXYZsBw6s1e4khuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دراتفاقی‌جالب؛ فرشته‌کریمی‌کاپیتان 37 ساله تیم ملی فوتسال از دنیای فوتسال خدافظی کرد و با قرار دادی 1 ساله به‌تیم‌فوتبال‌بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29093" target="_blank">📅 12:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29092">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lgu0xdBPj8jweTlCoxVX7CxZoAZ79MZT-hJdV865B4cXkQlKtgGLYYFDXeaTATnu5qoqYUZ-upi2uqg_mcrm3JMJ5L37BFlMz7e1PHepdGPAEaUEvV37NtuTmN_FbwQtSR917KIc6ASBih8RYA0XGcP5OsyTT_ldn3P1Z7ANMjdpJ-MThIDYmJBb6vLCHNIQnsOSjIoufQFz9v7HIL54S8-ZiCFNJPLsQjiEMXzpQFecPscIaAobj8vm4nIYac8R961BseapEFB-UOyMWOpw7JxjjeAIwCQSj0jqajRG-pru5cs05tipZSOnSFiBkqvSMALvsd4iWxTn2G8PVHnV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ سهراب‌بختیاری‌زاده سرمربی استقلال به سامان تورانیان مدافع‌راست 23 ساله این‌تیم برای دیدار با آلومینیوم اراک آماده باش داده و به احتمال فراوان حردانی از لیست آبی‌ها خط خواهد خورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.9K · <a href="https://t.me/persiana_Soccer/29092" target="_blank">📅 11:45 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29091">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iAtrAP2T43sUJ4WNda-6f78fIX-sNOoXxSC-93mGvqFs_8w-_IwnZaItIyFUkbKVr11zpBSpxmSLoa-9pdvcRzcpqBcXfCxDIax2mcZLnSFRNvNRXzNS2Oh2Vqdj8cS9oQHspsPtK6oo3RnWvmwy4R88_V3JTBnyNWqm3w00RH4Fn6iolIvMogj0sO4rwshbgiKlLRThwLlQP3QEXI1DquL0VtPw1h6zgbyDot9XyBA5HaZzAKWcmEJ3SA8hXwrq7xv2eKfHqNZUwoLu3MYMUYFqvxLgJSYK2T6Eh_B7PxZ73P3r8gL6XFZT8XriyghupQcT0t_AshjcZa7CPrRyUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ محمدحسین صادقی وینگر پرسپولیس اصرار به جدایی و گرفتن رضایت نامه‌اش از این تیم داره اما مدیریت باشگاه به نماینده او اعلام کرده تنها اجازه جدایی قرضی به او رو خواهیم داد. ظرف 24 ساعت آینده تکلیف صادقی مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/29091" target="_blank">📅 11:35 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29090">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇹
سسک فابرگاس سرمربی‌موفق‌ باشگاه کومو درکنار خانواده‌اش؛ از دختربزرگش که در تصویر مشخصه‌ پرسیدن رویایت‌ چیه؟ گفته روزی بابام بشه سرمربی تیم بارسلونا و تیم ملی اسپانیا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29090" target="_blank">📅 11:21 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29089">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH2OOZ6fL942OQaQK9-ngH8K1qkqLxy_tRxUYmaQwNaQhyv7qpHEvZOxLdfjg1e6a1QrCWE0sl57EJl-2N3FrlxQW99eQmtBDa3eGmRfFkgt3MRnmWy6Np8JIM3CKY2WespEeO_4PRahMfpd_fz6Ww9tW7fvJjr1XekmK-h6atuLKnJYhj7KIfE2jUF5RVeUY4alsn3jyVwwy3Mim-MYsxqUCivRDolzrahV0-AcLFRV-bmZBTn1r8lt8xfjTPO6i0r9Y6Zb667D1RqnzweIqyNhPrqkbLEo86khS2077X-Qt9fgoU2LBmSDbPgSY3Ptes95LkYwvTUkuKxeoEMtjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/persiana_Soccer/29089" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29088">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/527972a3ec.mp4?token=TnPg-gCPtpiHL-KsNc8RDupqSfG03TBWwM5h7bxsqOY2ldKMbRc5QonlDfxzmAWQWmoX-dto3H853AGx5ttFJqEPt3BYBUzlN8yvTauzov6k3tZoEkgLvea8bAYxpji-r8DBaqP_ed6oTKIEdiYBJXEF1fIFk_JnSvHct7taIR8y1SDub_a4jb-f-So_JVWALsLk8k2DHGekx6FhfbZUMwUPCY9N7EoUnE_z3Q8QC4_p_tf9zIIyySqxefj0U_HQQ1lEG2MaS2WD7J9GUFBEa75ezHt2PziU9etBaFQ3xRNIi-u1wq68bEZ_tfzJPdhRLJcbzJ4RbuuEeFuSdSrdcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/persiana_Soccer/29088" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29087">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hksjnNB2lERVmlVx_lI20VIGOsHBcantPaPW1eVtwZLKB4hqMipX7upvzAkF7kXlgBRpbVSiR3I8syWMabhEDGKgtTnLq2SATe2nh5zNifLDRgEkpcJzQGRg3X4dlygr9b0uZde1Yu3oWAs07NPuw9fOpSeKiH7SF1aBa7ZDc9HBG0pjVgkhhkPsCTiCpy_YzdJLrK6IF2J51enkEuewxw2tEVbEfrA8xILBnqDPOAC44IsOADu9F6DFCRcgZuGVcCWvhJ7LMSx-qqlVU1cReZ8hk-TlSmkC3QxfP0GOBd0AGc3xHehX-KccqDi49twM1RW-uQrZeEvA8XOsejLf3A.jpg" alt="photo" loading="lazy"/></div>
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
🎰
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
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29087" target="_blank">📅 11:09 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29086">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5nUS8EAuI8Q6gsicYED3HeQTzJxsiwowlxGqpVG8yPIoEXpdlfU187tdOiv_yn3xvzny7RizC-rsmq4p5Q9Ic5X6CkuK8P0ATvJl6EH8Vtr-Kns84Qmo32P1IhHH5Bn9Y8HnfxIKeVa4wHq154deNvH0CJBj-oIZUp14lzis_wPWDLC_bFeYow_zfdkZuNlC2xw2moSmqWRtW8JEBB4eiXgCF5uerFkKQdljOvbZh2UVvd3OFF--CmNWpJJqxdN5hp-XlPX45XVTUBysytP-V9sl9GVVHQrVEkBjrxFuJ6oBYXX8OVzl5pmrWIAcjSC_pnn3kzh_5LMSfqWlVassg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عملکرد رافینیا ستاره برزیلی بارسلونا در این باشگاه وقتی بازوبند کاپیتانی روی بازوش بسته شده: 29 مسابقه، 25 گل زده، 12 پاس گل.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29086" target="_blank">📅 10:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29085">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KyEKdvvS1w2qrJ0LiAZGYgZeqZHLl66MLv0y7663aYvmo9lMs7TOz3_1DcPLzkvCuAifJHDipMFrk3F6Uy5K1TKh301_LRY31hiQ4PosQTrEkCycVrwfkXa0LUjRjywz19yCxqvfkUuK1UrAicH5_Rc4oD5yiLgshpvzw-VdpyzYMFJbluFlUgi5HyBKHZaCdAlWMNWS57mgGa2YeIJrdYl5wFFKyBww9iN1OpLouUjsolm6cghgfDpUuh3h81BknpTl9hqRS17Fuhef5NhJNB7gNixn7hY2dhBJv4DZWOrq3_3NI66RpL5uPhTGBiLrKHDxF-UeIQrEwNPQuXKMtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#تکمیلی #اختصاصی_پرشیانا؛ درخصوص فرهان‌جعفری هافبک‌تهاجمی 20 ساله ملوان همانطور درروزهای‌اخیرگفتیم هم مدنظر کادر فنی پرسپولیس هم مدنظر کادرفنی استقلال؛ درصورتیکه حسین نژاد رسما قرار دادش رو به استقلال امضا کنه به احتمال فراوان فرهان جعفری راهی پرسپولیس خواهد…</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/29085" target="_blank">📅 10:27 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29084">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kVCrUfGaqoWnk9jrsM_xAEZBrKkK5uwsTgl7MALpUaAOS20jXemnO-p6kIx6DKrLtPx1H08R0PTkA49aGp9XBfOH_WkohoRUxEfJ6BfTu-NcMQXX57drGP7IDe7yxhuv3hIG__dk__jA79ziOjLogS32jfcXVEZRKS-aj8l9raPmUZeIApInsEPovDdlWdz4Gf7_pJC8DBkq5bbyhhOONjmVMx9wiHlrP9ZsYydqYwtNmff2K4FwRjzxAwkiAHo-kK-2zgOZO9kakTQIOjsFOyaGvXkjl96C23qF9YCEZL8Z_RHoAxKaOYyB5AZfvgvPW0ztRFrx5I0OV2EA8G4p6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
اعلام اسامی داوران هفته ششم لیگ برتر؛
پیام حیدری داوردیدار استقلال‌شد. میثم حیدری هم داور بازی پرسپولیس. بازیایکشنبه و دوشنبه برگزار میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29084" target="_blank">📅 10:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29083">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TLeAePrSs5JA5C7AFnmIs957Kp41Q95SiX9pfZpoRGf6-tWL4F3EnG8MxO6-akPEGbls4bkIVc9MuFscLWpFau0Vp3yHCv9gBIkdFoSvaYWNFldFjpNfJLacy14oOVMt_e1PoEUF0DKzSkiYaBM-der539UdO3rzqI8AM7RtWoD9uS9pZgLN8uizU96rcbMJvY0vYhxCszd-pUMkXvngIfGrfo_Mg6Qy9mTjuQU4qf8ogBzQQpfGbqvRYa1URUuoxzbnC4z0EgkdiGLZ7QnOOR1HUnaYGn8IxQK-dYor0lBy6fbVtF9NCRYzXFpf0zqImbtzM1NDblOdkM6jS5LP-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
معاون‌وزارت‌ارتباطات خبر داد: حتی اگه جنگ بشه هم اینترنتمون‌قراره‌برقرار بمونه و همین که الان اینترنت وصله‌نشون‌میده حاکمیت تصمیم جدی داره دسترسی مردم به شبکه ارتباطی کشور حفظ بشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 83.3K · <a href="https://t.me/persiana_Soccer/29083" target="_blank">📅 01:53 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29082">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CAhHO7y2F7U6-QoTjc7DktF8xgDD7xe4RT0p_g1GS5PbgaMlt4yX4FhCb4KFQWcejMk8vmVDZM_Du64kDzDx5nGW1-UwY23qScbyYl1EXcjOtq7lR9g0H8iBFbHGFUy3GscA7Mh9TT14HWtHkMeH1vTEJKcSQFXs3OpslbLCki4SyE3QfbGLiqeOqZGOPXTY-kj_WZYgWqRLu_DQpv4Ln_7IO2KXvbUHbu23NuXDeRWUHsFFk0BRlqNrWPq3A6dmk4EndIt9BHy1TG0p50r_1_HwZEm9xUQsN6Bv0Wnl0pF78mozKLjD1zqu80iqPI8LKcdKanilDFPrHJRGsdnwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 76.3K · <a href="https://t.me/persiana_Soccer/29082" target="_blank">📅 01:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29081">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pfq_zW4UADcp7eWDJN3k4fwBqMC08Ml8dctsjwy-871-obAwxDG21gEihOjl118RzNXHaqCtPHiJvKk2JIJijVHkjp6kU7UY4SFmzoS5gv8FqBO7b8p5kWLqZ2MaKJ-e3jLLfY3YEvwHs9EH7ooam4gnKvp2LV67CFMJ_Ygxo2GOXv4uWyBePwm3zne8pPly2GM7O5WH0riNt_CBL3P83Ikr7-QHcHU0cgvZ3KCHOFYndcnE_zm2shzIr-uSEcGMRaOo9NrPHdY6YOSEDBdPYUyb0uNn8lcXZMupi7tNH_D7tGpXQPEv5nW9uHP0Q3X2p_OsRm2cChMh596IisK3pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ باشگاه‌ماخاچ‌قلعه‌روسیه به ایجنت‌ محمدجواد حسین‌نژاد اعلام کرده که در پنجره نقل و انتقالات ژانویه "نیم فصل" بادریافت یک میلیون دلار رضایت‌نامه حسین‌نژاد روصادر خواهند کرد. سعادتی این موضوع به مدیران استقلال و هلدینگ رسانده. حسین نژاد درپایان فصل…</div>
<div class="tg-footer">👁️ 79.3K · <a href="https://t.me/persiana_Soccer/29081" target="_blank">📅 01:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29080">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNo-x4s6CtzWhCcXc9pxiyGQWdb6I33NJkZFMeav45OEUNhE4vXfb3YCOon9MINysawdRXMxBg7hvpqhMhJCsbFDYcdQ-uZx5O8CUTAVJ4AUOtLP7r-JsTi7dgO5QIjwkt6q3B77HQi-QHeWkFGWYJPr5NMeE12ffv3oXFdcPCAmF5m5PrOoVVhmQJJxDIpwlqmOHIHBo-C7ShkdDI9nerphIq42ByeZshkcfYIk3JyMj2x99TvBzSc-X9Efcgr4AiniMyT-YjiYCA36W891Qq0QMOWXbVx8tIg5pMdzoKeTVWrpZZiGWpSliIkwAB2rojteGvOOKURPLPlDj04UDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 96.1K · <a href="https://t.me/persiana_Soccer/29080" target="_blank">📅 01:17 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29078">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UL3IgvPq6xfiffTvwianQXXMEH283d5nmEJ2upohcPY8kIOfHgY9Upj8efU47R_-LbOr38QEfTX0YRy-lAfG1A9V5f353dpf2ZUaWOEMdyhPYyrIsYsgaLmQVHCe2s6lewlVMGbhDftucDLGuTQSivNwCZMokFFtCy3jHUL7uFqtLyUVz3ZXCbIvFLiwDLR1nZGFwUrEGQYy-Ljy9JrYnPehnTMTql7wvhBmzrQfNDW4RNZGpyMAJV2ig-MsLlNJ5dypbSMrBlUyIige0Qgb8bmVreUGHIfrw16-noDsNpCw8WHJ7NrEz37MP6Xlfimh9BcdDV8HM5CVNU9gevz8sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ اهداف مهدی تارتار درصورت‌ماندن‌درپرسپولیس در نقل و انتقالات نیم‌فصل‌لیگ‌برتر:ابوالفضل‌رزاق‌پور مدافع چپ فولاد، محمد قربانی هافبک دفاعی الوحده، فرهان جعفری هافبک تهاجمی ملوان. جذب یک مهاجم جوان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 93.4K · <a href="https://t.me/persiana_Soccer/29078" target="_blank">📅 01:07 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29077">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eEWaUkdesOqXtgBMxUxxSQ9oH3DMxX-CRLh40ZU0ZLx8Uxx8w_zZP71wfRYjH90JaDAyCgAuWlq8OWfP77kpo30hR8R3QobXpftdObILLECsmvdZbicLazXFimS2SDrWwrVHNiGuH4TW39w6l5P__7t77BRCCXo3rlfiz_dGfeXmVoidc-6Fhr-HHtmdXooDqj-gpWaOBmZ0mLfEgdBRVrK20rTRZjs4cXNFMjc_f4DN86iheZtOSyk4amnOSghhhe16GCScWcmLT3tGJLDBm3Q49Hpmw1F1OftCBWDnGLW-wLvD2l2DxTXKNDyp1vvmXwMOvr-cJXtQ6_G_QQjSdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌دیدارها‌ی‌‌‌‌امروز
؛ از جدال مهم سیتیزن‌ها با کاونتری تا دوئل شاگردان نکونام و رحمتی در تبریز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 91.4K · <a href="https://t.me/persiana_Soccer/29077" target="_blank">📅 01:01 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29076">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hfNBlxp9RF_vXOgOcxuJUvrbl4GBra-FBw_1Vf1EhwXjRkEA4KFaXjAFXi9OI-Q_TPltJvIO7pFVrPVOTjrtNWqJEtSo6dkdrDfpvtlcT_Fh-sQ1PBTfTHWUMO1iwijqkbPefLZ23Yn7hDgdAkSm-EdUmyrEh3JT7hwY5KxmK4Ujac2JpipHVhYOioMtvmQl0NYJDIlBbWF2TtQaPWn6dkA6JL0GwkNPGDv41TafGsoFxGzPj4zTXKz_Sr25PJphgexeqHDletULWuH9iGUL30DdKVT5e4DpgXnkfSZqPA9l_TR6c4BqdGoF5Ps_8mnn2tdjX70oero5M8paR-KQIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌‌‌‌‌دیدارهای‌‌‌‌دیروز؛
ازبردلک‌لک‌ها با دبل ایساک تا شکست همزمان و عجیب رئال مادرید و PSG
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 70.6K · <a href="https://t.me/persiana_Soccer/29076" target="_blank">📅 01:00 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29074">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qlav1IT0-570124oPYtArymsDlKHpk5ml-8nSwc_VWgFBT2Svgwa2XIFNEz2_PYaJYO3oJ8TiM5sx5aeY5xiHz81MWTI6FrobCFP3xADKL1A8GLUNmllEQMYEX06uYIa3fmLjYqL5_KFzOJ7I5Jl3CvOXv13AhlGI6poGE2FVTOzK7NoPwk1ZWR7XpMQBlGwpKWKmuTo9JDySOLt1SmWnriNb7grMYO4MqvOKh84wl3lnG2_VZxNYR8yl3XvZ9rqDKmrYB-XYw3_spUZJs-hP_tFjQFz9UeqqlCYhKpKVf6twWWTefO9xxkANkyesqc2Yxvv_LCjY1jv5_25Qwvopg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
عملکردخیره‌کننده لوئیز انریکه درپاری سن ژرمن: سه قهرمانی لوشامپیونهه، سه قهرمانی جام حذفی، یک قهرمانی سوپرکاپ فرانسه، دو قهرمانی لیگ قهرمانان اروپا، دو قهرمانی سوپرکاپ اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/29074" target="_blank">📅 00:49 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29073">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRhqNyBEtqY6E4OkYgbiGyMTxgySm2Vfa9Q3hsxpH3zkal3vkBQeAdUT7BP0FABr4VCludKo2jY0pOQzmn2v7qqd3nVyVPAEx5rZCjCgamDTEiGz9p0eZuqiGbpiSU33i5EcO4bqyDqzr8H_dVDszRggDag8_IVFTv0DGq6eA1jSNykX5d7YHWuylGn9tXpDBA5YZSR3ykeozs2hwDY8CvjMu8NrFE8h5wKSJIc5jv96a0iD9822gOlKw-5mTBLhDUatrwR0QJB-x6fC29eaGeLfvQXSm_sG3vZ5lSmWnbGk1lN3U_d8-asGb31Lv06F2Istn8i-1tq0HITDWAsjOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا|اولین شکست فصل شاگردان ژوزه مورینیو مقابل‌ گربه‌ سیاه خود رقم خورد؛ رئال مادرید باز هم نتوانست در خانه بتیس برنده شود‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29073" target="_blank">📅 00:43 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29071">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HRbVZxgLlH8kfuowAFTzBZFNPgFsZUv3iGb6MlMw7ASEmo816oZLKVObPpJ6G4Mz5xiKmtSJHajEEYhpnlS6EX4zB8crHV8mc1b0uLyX8ntNNyaGkiKZ_LcrWF4iii8tSA_VKau74VvmxRtukbbCZ3qNpb0-fgfFF14OAUli0E93Q1oakwiiHrlB66C9zNV1n_qdc4iyQ8Wuq5t4sUp2U7k4rgmtPRN0moXljeWCIJt2S_J2yE79HyMioNVKzqgbC1SIZvoIITabIHE5ZTWdthIJWiZI1IWBC2x23BGTXcL9jhNSV7eWtQWgkVT1_1IwJRhRA7yQXgsjtScSAljZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
👤
شاگردان آقای خاص بالاخره طلسم شکنی میکنند؟! رئال‌مادرید از آگوست سال 2021 تا به الان نتونسته تو ورزشگاه بنیتو ویامارین، ورزشگاه خانگی رئال‌بتیس این‌تیم رو در رقابت‌های لالیگا شکست بده و امشب هم تو همین ورزشگاه با بتیس بازی داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29071" target="_blank">📅 00:37 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29070">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bF_pyorcLobQatTzzlOOQM5N9qX8My0NhqC_Zyfo9Wb8pgyFV7ZuZMHAn1OVDBPWRZfVEAN4ThJN0KXO0VUC3F8LYpxytwNeF-nWrq4iSSSMw_yYNgU6HnYZiwu6Cdvd92ITM5choyKM1k0gRKdUTK0lABzXcCNXtUv_SZgeQKeX4UGOMmld_usiBUdF6L8bo8rNFmQW9jAjlV6BzSx3NGQv6AgitqXFVMqstxnu03ZSXFK67VOGO7HvvIa2uEZ37umJjfobCX6vCYkZwg98s3sS7MBubodbh97FMtNqbutKxS09xi-CXkUeB-qrz_fUxVf0cIrOdJJUviF2n40txQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/persiana_Soccer/29070" target="_blank">📅 00:28 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29069">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‼️
سوپرگل‌دیدنی‌عبدالکریم حسن مدافع چپ قطری سابق پرسپولیس در بازی امشب تیمش الشمال مقابل الشحانیه در هفته اول رقابت های لیگ ستارگان قطر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67K · <a href="https://t.me/persiana_Soccer/29069" target="_blank">📅 23:57 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29068">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLVKzCVo6-d13wGBt8tAufDoNdrcPs6Wdx3Tb9hOX30N-GVOIjOQ1fqC6ms4_B1D0EmIlcOgkG-lfu6ibFskeLtcCOS9n9PodzHPxQu5ZuCoqP8aZNkKBWqDDtwDlxdpW959BG42WG7OSVeb6_x3gJ7xSXUpdPwVao3m_pTTu-H8i9eub1vu0Eb_TeUt_dD6ARENBRdlX6qr_f2bgNUVmykmOJKM7vQgRQ4UfpOi64H1VKx_1P-0o8V3OsMgVUsXQLDmW1zeCpgvSK4l2TtR3Uk3YpzWyORHNaJT7IUTlliJ9_klYxKlp0pHbru738ScF8qvcZ5y-Gb0mIgS8I2QBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پاداشی باورنکردنی برای نمرات خوب؛ یه پدر مادر کرمانی به پسر ۱۸ سالشون قول داده بودن اگه امتحاناش روخردادقبول بشه دوس دختر ۱۷ سالش رو براش میگیرند. ماشالا پسره هم کم کاری نکرده و تاتونسته‌درس‌خونده و همه درسارو با نمره بالا قبول شده و همین چند روزپیش‌رفتن…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/persiana_Soccer/29068" target="_blank">📅 23:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29067">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eg_V1tALA3iYRSwU602KUkLthTPf3IqibbEoWpI2DHtc0jYBPDFhmGni7PcUJSl1LMB6yYl64hidjaokh_TtQFu3Fcd6xrB5TomAlMNOAbxiD4r_g3mjgHESe6PsybHRUeVvq998lMCjDGDWNEX9OsLk_9g6e0rBgQgM0W4JGkxcu8shNBemC5kJFT2QJOXJHXZo8ig7McOKQzF5OG-oVeo_Pj05-efFytvWTy-IgupczXT-2qpukvq1KtRfqgf9M0nKd19iwb8S_HxRq9QJhoRyQb27uXwI5piG1yeCmleeW1mxZOYlsLtMmjIC9FkRxbiEQmRBvF3AaM1OCtLtTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
پرافتخارترین باشگاه‌های ایتالیایی از حیث گرفتن انواع اقسام‌جام‌ها؛ یوونتوسی‌ها با اختلاف در صدر!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/persiana_Soccer/29067" target="_blank">📅 23:25 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29066">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LcEHJR8YV45hv2_GbVibzbf_FcxERwBx7EgqHxp0jzcuc023TskIrBwUDrzLfgFCqpIaoj8OFNFnICqNW24cLDzqUep9NgW6WsDYrJzyLWg470HXZmrZxGKLl1UEvtaH2IPfP-6SXo-WD7QnjETnqk6PgsqetO3DJ9WXPXjY-f6x1-hODySKAQskf_lr01-DZ6Da43iQxOyDx-ybE13AxQjeDv7tuNVu2WJdxopOJE9RBt73Y-PxgdPBQE1BUai_snfs8n-dpG4Y5h4vIdsQqmcRDT2oBFV08L_pelPWFYTPcENCJyxUvS6ai0h_SroVbiOGMhmT9qJyE6TL1K-RFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رگی لوشکیا ستاره فصل گذشته تراکتور که با قراردادی دو ساله به این تیم اومده بود بعد از جنگ قراردادش رو فسخ کرد و با عقد قراردادی رسما به الظفره امارات پیوست.  این هافبک آلبانیایی در ۲۵ بازی برای تیم فوتبال تراکتور ۶ گل به ثمر رساند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/29066" target="_blank">📅 23:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29065">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnwoQhPEcaZaxrENHXdMd99ruzpnXDZyEZZqW6Fso7vdo42_U4GDtlE95db-doWGrXexPdfwKmPVxJa1e22ek-9Xp-te2J4xMebenZzPbz_8HzbdyzT9ZBmPvPNnPo823oTMizNvArT1F7-jIqi1tcjzaLK0Oqmd6oVNV3tpZ4ldz2iK3WkrIiI4xy--RMwpI7Ln4U4Owh28o53kh8FajkX6_0ceH7jmSWml-T9fPpoKSbP9QZG7G0h_oWqvSP6G0hWKt9LP-Nme8LXJSP09ijsoh3ZBgRbRJ0jlUkycwM4gv0udRvKeX6c0kmrlF_vArcEA9ovne6pfc6RJsRhLbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/29065" target="_blank">📅 22:54 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29064">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sEiRk5PPfGKDv0CTt8JX0ZhFz1Gq-c2FECpxT_Z4-n84kEUGsDYJ5q_S9-HJTG4dRsAGxT5TrXtxXMjQGAd0rtmHTKwVAUZP2xGqxR9Ml6X8RPz-5snW4FHIl_mzGxnfiLJseZHaV4VcPSuuQycfBg2mZSMOLxwsFuIfO1ULXCKOJT4VNkfdlzgJZ-a2QJ0KDMTZ91sTv0u2_Hxc_yJbNma36cim3toGFOdTJTP8Vk412vmmxSBseLjMTXnj4CkvFvkYhICfPxe1UnGobCzA_j2OI_W9WM6YJnMGxgYIbgSGYfoKUnopjsnfTfz51Fl5iHeiOqJij839A1vLoxF4Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میزان هزینه لیگ‌های معتبر اروپا تو فصل نقل و انتقالات؛ لیگ‌جزیره بااختلاف بیشترین هزینه کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.5K · <a href="https://t.me/persiana_Soccer/29064" target="_blank">📅 22:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29063">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L5rrsPn6TYioAXqk_Vd07HJDBGF-d2TukUxb3_XB5uacJpKDrSa8ZS-f-MNefSByhKC8DCJoLncqYBjOjh3U_kQZWczCuqyc-n74iKbAX_D08Sxb9yICtzuyn_O88HguB4YkYCbsuhhEfQ4Ujf69orXn4uWlVptKD108APs8pWuqt9iDLCnS-5Go8afQa0tX727hYleSro5qAh7qstebEtxrO_O9DTsiqSzfsOmp_D3xVRdR6dlxlt_EuebI55PdeN29BFpeeDQNgH-1eY4TklUDgZRyowdAHq4fZJyT7RMGv8XSKi3viHYcLeA2AT7u5yqHpTzRQqwG2NZCSCP6MQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ ویدیو صحنه‌ای صالح حردانی در بازی با پرسپولیس اصرار داشت کاشته بزنه اما به توصیه سهراب بختیاری زاده یاسر آسانی پشت توپ وایساد وباعث اعتراض‌کاپیتان آبی‌‌پوشان به کادرفنی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/persiana_Soccer/29063" target="_blank">📅 22:38 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29062">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PonZa-9KgIPfmAgxYlkCOXJnND_Pe-sfCilBraemtVKaerUJI5KMWvtPYuG8ZCzoAO6KHNtwcLOgWAJOvVLMdoaN2xXx3IJLJ781Nzb2WPl7Sp7LZ7Le6wVmirzAdY06bMS52mcZbHSs2ok5EshLH1MwSkAldQs9L7ie0b0Zjxcj7gCIMf-E4WNFcMRXArPmDanqJ0HvIEXq8Nlt3S7WuPnRuFBetX0y1hX5lTarfV0GL91WyUPK5QXwfe9BrHr3_5fj8Hhd4cmlEqHBBBoK1we-QorEEBDgD55hItVQBH1fUb-Mm1NSa7iAyjmc7VxS2CB4YCOGy9d8KUY27iNruQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
فرصت‌سوزی‌عجیب‌وغریب و دور از انتظار طارمی 34 ساله در اولین بازی خود برای الوصل!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/29062" target="_blank">📅 22:19 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29061">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pLQ7I3MMXfSZ-8bIDQAilOxRpq4BCeJGIq5cc0yAKGXD-g9u5VLB8HDWQz2KGuhMn1RcnxBjDzhcaiOdqynsX6Sa6UDfE-lGtw-XOCCZYRo-UQ2ZLraUfM3omyz49W-BF7SvqE5_5CuDDc3hLBucIV1pGXIe0gd2RIHakB6qpG8IJm9kywWdrOIwjWy-w1mfO243yeEyKVxrM-r0WHKA4wrRs4ShCRuLOAtFZwnFy2Z6SAKRv0SkbI7YRGwYMXBco5MhYM-nHffMbkG7jvjocmIOTKjDh-xOEkcVwH3Fs6r7OW0ZHQH2qUk8FrZxhw8jHyvOBuMX0ahv8kJKq3Q8iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛ شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29061" target="_blank">📅 22:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29060">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=P5u_sQnVAzlBjsSNisO-juuhAGYYse3oOlbJrQbgwlVgwJ17Z32GiCFaCxhkjEVhjp1JvY5XiSWtUEc3CaPUILGWGcrqfWxSSwg9I833ZApQqCsCamOk3X49p3teryL3Qh-7zTos6tBM-9m7X3LU8UwRWqFwl0ptLFda4Rju72R75iI0TrlEsyJ7LMHptSm6TzMm1KrUapzshBBNDPetXHT5egKLckk8cM6kelvdwF_pOQI6ROEAwoe_zwSFRsspp2Dm7OSR37UsSpxDNlUElxYTZsxLTm1tYctTnUJKI1RJFGQojNAXAzNriW2JeIk0UPIF4WmjHltctO5kR2Lctw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34787ce1a0.mp4?token=P5u_sQnVAzlBjsSNisO-juuhAGYYse3oOlbJrQbgwlVgwJ17Z32GiCFaCxhkjEVhjp1JvY5XiSWtUEc3CaPUILGWGcrqfWxSSwg9I833ZApQqCsCamOk3X49p3teryL3Qh-7zTos6tBM-9m7X3LU8UwRWqFwl0ptLFda4Rju72R75iI0TrlEsyJ7LMHptSm6TzMm1KrUapzshBBNDPetXHT5egKLckk8cM6kelvdwF_pOQI6ROEAwoe_zwSFRsspp2Dm7OSR37UsSpxDNlUElxYTZsxLTm1tYctTnUJKI1RJFGQojNAXAzNriW2JeIk0UPIF4WmjHltctO5kR2Lctw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سکانس کامل مخ زنی به سبک مهران مدیری در سریال جدید او بنام مردسه هزار چهره که از امشب فقط جمعه‌ها از شبکه سه پخش خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29060" target="_blank">📅 21:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29059">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUFoc0d3PwTqs02tcIf4lOemuR0DvL6MUuaGt8TYz9j2MkbapKaqen3Zw1pjn17YFFLTdocEhK2h_APKLxXpNEKKXiphCisYi2PSwCxPCB9-YETGCaVdxuXtxvgs25sgvneE-L9-AWq_M1W-CygAG9Lk6PgHthWPfM5_wqH5qehfHhV2wT64d74VISU9MyeB4m1G35AYzjnAHcZ2M9woFp0zUKZi1R-cshDmskedQOUs5JS4HGi0qRQcopYFGF_49Ax0-I8fQn242Ks4MivmozZ7iSE5LoRYk7vrObq2ulu0N90fVIJinJhU21Whdwzayf8WSXr7Z-J6ZZKdCSj0KQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته چهارم لالیگا؛
شماتیک ترکیب رئال مادرید برای دیدار مقابل بتیس؛ ساعت 22:30 از پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/29059" target="_blank">📅 21:14 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29058">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=rfUZV90s-m5SxNax-th9iq3XILjXNf8VMvO0h2pgoW2HaA9lKAX9hBMeVloVC_-D8NptXKIXwipx6w2sO350gtrz8SsshHt1AOaF6csQl1EyHSTSfK1kXLL_5M016ukWl6-9hjcZl-xtBHw2bTFVefDzh3RpnEHiKQvLtexNv750a7dsSKBEJja28pBqIE7TzWef9K1BxU0KPXBu7_y1xehoaXB2x2VUHitwmKzUxD7eOVNWDVbtmD3b6z0VEjvvQ9xiC1Elu483neiCAntN70ctorHd6OVoYTWT4Z3UwPGQQlNrpBfBRDb1L0QjSVl8-oPWnOf7hPmwGHZxQxW3rw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf2bf71bb.mp4?token=rfUZV90s-m5SxNax-th9iq3XILjXNf8VMvO0h2pgoW2HaA9lKAX9hBMeVloVC_-D8NptXKIXwipx6w2sO350gtrz8SsshHt1AOaF6csQl1EyHSTSfK1kXLL_5M016ukWl6-9hjcZl-xtBHw2bTFVefDzh3RpnEHiKQvLtexNv750a7dsSKBEJja28pBqIE7TzWef9K1BxU0KPXBu7_y1xehoaXB2x2VUHitwmKzUxD7eOVNWDVbtmD3b6z0VEjvvQ9xiC1Elu483neiCAntN70ctorHd6OVoYTWT4Z3UwPGQQlNrpBfBRDb1L0QjSVl8-oPWnOf7hPmwGHZxQxW3rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
استامپ‌من‌کیه؟ بریده‌ای جذاب از سریال مرد سه هزار چهره. امشب‌اولین قسمت این سریال پخش شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29058" target="_blank">📅 20:56 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29057">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=oBiGbD0PvP3fRpQev9eG6A7Xa28V5dNOp1-evUp8xeMx0h1j5x2PRdfeKXUUj5jH3rxERfEO27AA3RwAbOnp1RCM0TU0kMpQ-xz9XruRh0l2zHSP_zlqvDCTrQBl9hQxlh-I_eXVUHzmKNzw-B366AprpuNloxO0MRcUUwyBzbC83Eyf7HQcya5BuXei5F3X3St1byMjQhuqQzSXzFwho5NXn-X52kH3rVb7WYj4fU0-ksp-j0whfQyln6Bs1PBaOjVvLBGwYelrKS34sll5ELvS3AM372sND5KM_5XpoLNQgWqqJCOHsVgN0hHI-f2bdzZ7d4kr2C8HocAO3DfvkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e99ae53e7.mp4?token=oBiGbD0PvP3fRpQev9eG6A7Xa28V5dNOp1-evUp8xeMx0h1j5x2PRdfeKXUUj5jH3rxERfEO27AA3RwAbOnp1RCM0TU0kMpQ-xz9XruRh0l2zHSP_zlqvDCTrQBl9hQxlh-I_eXVUHzmKNzw-B366AprpuNloxO0MRcUUwyBzbC83Eyf7HQcya5BuXei5F3X3St1byMjQhuqQzSXzFwho5NXn-X52kH3rVb7WYj4fU0-ksp-j0whfQyln6Bs1PBaOjVvLBGwYelrKS34sll5ELvS3AM372sND5KM_5XpoLNQgWqqJCOHsVgN0hHI-f2bdzZ7d4kr2C8HocAO3DfvkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇷
🇰🇷
سون هیونگ مین کاپیتان کره جنوبی:
من همیشه‌گفتم‌که‌کریستیانو رونالدو الگوی تموم زندگی منه اما بنظرم لیونل مسی بهترین بازیکن تاریخه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29057" target="_blank">📅 20:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29056">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fwfjxsuOI56ROXUZq93BdjVgeSTdaIxI_lhYzmBh7hoyqjZM0LFn_8N0dFSJXDczGui_3IjjHNNkPES6Rdx5slGk1WpGIwEFSNbZIHXjzSnzrqqTf2qYmqQ2yb380d1tZu0Xp0gP8rs-xF-9hrQDUBngHRaxoEcFj0US8JaYXNuAwNiaY_kBAgmTKeTiEpdfxJcy7XGtb6O-w5jhn3fpi3ihlb4h6PSwVdRqe29rTVAUE6JkL7DU2x2CGSuxnrI0gqgAor0Lf4iYLRS-DXOwOPz84N27yL4jiCzhemgZo9d9yLq6ctwQGeypVHqx0zPc9_R3qcmFGRPGsJwbWBnM8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
👤
طبق‌اخباردریافتی‌رسانه پرشیانا؛ در کنار جذب‌بازیکنان‌جوان‌لیگ‌برتری؛جذب محمدجواد حسین نژاد و مهدی‌قایدی دوهدف اصلی‌هلدینگ خلیج فارس درنقل‌وانتقالات نیم فصل لیگ برتر خواهد بود!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/persiana_Soccer/29056" target="_blank">📅 20:05 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29054">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/b0azUj9ZjdexM5Xyf9Ky0VtiA2qX4PWYApI0rtn-EevnTyoq-IJdnLeMG0xwCHfqAOCsZ5xjzlUtJRodAd1mG7EUnbf7IiPdLCw4IbVXzqWuaTtAVjIUbg3xvZFRZBmsAVSGLPPC2ORSinHdnTNtoisJtmqb3wCb7iWaxkus5O-JEMRRKjilejwrGVxp2c_XX3EOexSmRnDRRqgruUW6mLQt9AuOeCx9-nW3mGAGloJx8AdSf9NvdtgA5PmE5ziKaFkrANeS_pf-wReOpZ3TB5iO-7SOKqsyqghrj4jCSAIoYnDOooB3GIzjzzm20G8e3CYelZMSnbXb_uZ4p-tpsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OrfbVtAgxQrOiZJF6dfxfvSE0Ilr5G2nuMGqtLues010lZgsPyJ9CeIFRqr0rfiyZzYQgZxMvMHScro9DtImNJMTYfC9ZJXUrpp43uxXJoZ4KIei_2rYDmC5ok__U_SKKVNzKL48d_c_1wGiDYpJUk_jUY5XVu3oba-k-4YSsV9UHn45Ix1DNY9IYDKFvYxOvPFuQHZaXErpQy_rg0z8lQ2VzIaaxS-1V8VhzcpgwqrdKDHnBJazMILgpTIul4PCKeKvdZOTlvR5DGp1TxqYNXazEl9iCyZsxbeNhKQP4FQ7zZK2emaCheyRsStViZ0jGrRu7gnMXOyMRutnQEf9GA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
نادیا خمز دختر خانوم پاکو خمز و شوهرش برای ماه عسل رفتن توکیو ژاپن؛ تو کامنت‌ ها ازش خواستن یسرم به شمال ایران بزنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29054" target="_blank">📅 19:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29053">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q2EwWCEfDx6bnUCblUmPnfv8KwrMm0z_9NHfUhErulSqdSAegyGE5k3T-LEmIRFXivAEozFWbbx1KokOHNpNMBefkEq_xpUe9nw_dBtOGe7ltMGurQLtwpOprlzRXIj-akxQ1p6B4SmiXEf9yHHff6Xkq92k1XwXWNpg7OK6c5BDAuYNwBA5XgIiZ__OoonCP0BA-SEW6eZwz1YVVdYFIF4WDvoBpUSgpEl9MvIlAmgKJew-VRZJDx89HlB0aCXYnlnv6ULf1oJcywWy6aMHrdXcgRNAaXSH0ERSdpZFdk_DPN0ECHbH5DgMhJx6kthAsUbMNt9pmjQuhh_W7z7d4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه‌جنوا ایتالیا به‌این‌شکل‌از استفان الشعراوی ستاره 33 ساله ایتالیایی جدید خود رونمایی کرد؛ الشعراوی یه زمانی در میلان فوق العاده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/persiana_Soccer/29053" target="_blank">📅 19:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29052">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=ay9j8kYna3_i3sBzrY9KBFxI-1GD_2HLb7NJYGHcPiKBXGW9zYIiqMBzJG2oDN8hCYaxGsl4uONad_xvoLJYJkBUv946fBX8pAwOo4M043_OpufcxKeu7gYw3wi4GrvC-J4Dm01K6zc9U3G8zPor3HLKrM3ZIc1A2btAXN44mlMO1a8WdoMEDrIYjEfUeF3ddFBvkrgZGrGJKV7YptNyRYuChraZEsaVlvIrFUlA4bmTHFEWXXxCptgLY8lD7GOG2pifjkWEPdIES3NlK1uhaYw5RtKsXRjOIf4od9oWtHiX3xRxN18RxdkLNQhpWj0ykvDRxsU0_NgOEapAXTP_rlRuSw8XjoaCz64o3fE52c8MUICvr_dHMw-IG7N5IeCtQmK9aCqsPxM6pFk4qbIltPO2GkA8pyAy65BAQ14O3TNC4jrdhNVwbAFtALggkZgGpuP-d_YeAOOp5qaadKxkqHtpZikF1ipuGQXBdvRlllu5VUR1gLSHuzJPp1dJ0LKH6pwSF7A35seo12NpxVvfeCEqKiXXhJkmiWz6NxCl4y08m_5cmf6dHl5hp-0_r290eGiu7Smri3kk-ukoH_Zi73N2R8CWter6mvZzjylHB2C1TfEIwpYFIkfWGUYQtC_aoAyo7oH6s348Ts-Tm4dQfUySIdCLnvaRjeGYJd2q1SI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ef0797e3.mp4?token=ay9j8kYna3_i3sBzrY9KBFxI-1GD_2HLb7NJYGHcPiKBXGW9zYIiqMBzJG2oDN8hCYaxGsl4uONad_xvoLJYJkBUv946fBX8pAwOo4M043_OpufcxKeu7gYw3wi4GrvC-J4Dm01K6zc9U3G8zPor3HLKrM3ZIc1A2btAXN44mlMO1a8WdoMEDrIYjEfUeF3ddFBvkrgZGrGJKV7YptNyRYuChraZEsaVlvIrFUlA4bmTHFEWXXxCptgLY8lD7GOG2pifjkWEPdIES3NlK1uhaYw5RtKsXRjOIf4od9oWtHiX3xRxN18RxdkLNQhpWj0ykvDRxsU0_NgOEapAXTP_rlRuSw8XjoaCz64o3fE52c8MUICvr_dHMw-IG7N5IeCtQmK9aCqsPxM6pFk4qbIltPO2GkA8pyAy65BAQ14O3TNC4jrdhNVwbAFtALggkZgGpuP-d_YeAOOp5qaadKxkqHtpZikF1ipuGQXBdvRlllu5VUR1gLSHuzJPp1dJ0LKH6pwSF7A35seo12NpxVvfeCEqKiXXhJkmiWz6NxCl4y08m_5cmf6dHl5hp-0_r290eGiu7Smri3kk-ukoH_Zi73N2R8CWter6mvZzjylHB2C1TfEIwpYFIkfWGUYQtC_aoAyo7oH6s348Ts-Tm4dQfUySIdCLnvaRjeGYJd2q1SI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
#فکت
؛
رودی‌ژستد،کوین‌یامگا و یاسر آسانی سه بازیکن‌خارجی‌تاریخ‌باشگاه‌هستن که در شهرآورد های پایتخت موفق به گلزنی شده‌اند. جالبه هر سه تاشون با گلزنی مانع باخت تیمشون شده اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/persiana_Soccer/29052" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29051">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=hqKqf1re0rlkBZkBjQd4utRs669_5WWNs0Pp2jJUAkllTPh0Da0-LKvSenX_P5w5tpPdYOoIOd56m86x0e8W-u3jRMShtvmLMB7BxStMWPwasSvotVnPNzdp5M342YGxe333IpCDgJ8JfiyCASEckUNnKuHYR9OpAwLj0-HqeP-fyf8YEg2eg1FHAr5Zha9DtghBvdqtao-KZR4EZx46a2BPUSW_HsmTX4P79W4BOCxHHtSUt0nIvN4MY2hcywPM3rWpBg46NcZNOMriNV1O2r5a5Ccz2E2tY65IaHhUti0B-c7rbB_prOziwj0JzM6PzKZ1rHUFjgh-93ERuJtBRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d8c83a1c1d.mp4?token=hqKqf1re0rlkBZkBjQd4utRs669_5WWNs0Pp2jJUAkllTPh0Da0-LKvSenX_P5w5tpPdYOoIOd56m86x0e8W-u3jRMShtvmLMB7BxStMWPwasSvotVnPNzdp5M342YGxe333IpCDgJ8JfiyCASEckUNnKuHYR9OpAwLj0-HqeP-fyf8YEg2eg1FHAr5Zha9DtghBvdqtao-KZR4EZx46a2BPUSW_HsmTX4P79W4BOCxHHtSUt0nIvN4MY2hcywPM3rWpBg46NcZNOMriNV1O2r5a5Ccz2E2tY65IaHhUti0B-c7rbB_prOziwj0JzM6PzKZ1rHUFjgh-93ERuJtBRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇫🇷
تفاوت‌تجربه‌بازی‌درپاریسن‌ژرمن و بارسلونا از زبان فران تورس فوق ستاره اسپانیایی جدید PSG!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29051" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29050">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsaI8grN2ovEGhXpZ_VE-IOOZHnislSXyQQsobiN8axTdgtJlZOYlK6PyhZyiN1eSkcQbctYWzzhg1S2ScszuPvrmA_b8z_Y-PYN_nAB2JkGJwgRbYArc_mO86r2hRZKh1PsUuJeOkuoz9LdrWsFOzK6T0yLrvwlY8DwUqxZ5l1dgpTru0W-WX_WXoRDno5AFKYvpnvEfKMlrr3Qwfq7zGQFl2Bzbp5uFYID_1BeUoAJ5kB5HxFENHnJkus9yLZx777_3o0O8iXM382ssWXxYMqfxf5wK2GSLXyKcfAlZPzpdrvXNDUqJiowTmljG3cjHToMUZZWu7A3XhPlA4UG7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
هفته سوم لیگ فرانسه
🇫🇷
پاری سن ژرمن
🆚
موناکو
🇫🇷
⏰
ساعت ۲۲:۳۵
🔴
بیش از ۵۰۰ نوع آپشن پیش‌بینی برای این بازی در‌‌ بتگرام
🔼
با بالاترین ضرایب پیش بینی
💵
واریز و برداشت ارزی و ریالی
❗️
🔥
۳۰۰٪ بونوس رایگان بر روی اولین واریز
❗️
💸
۱۰٪ بونوس روزانه واریز رمز ارز
❗️
🎁
فرصت را از دست ندهید! همین حالا پیش‌بینی خود را ثبت کنید و از بونوس‌های ویژهٔ Betegram بهره‌مند شوید.
🔴
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/29050" target="_blank">📅 19:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29049">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sq7iSx-MtSqulyRhz650TrZLtdkdLzrcFzDGniGylGX_21gGcFbEhpM9sWnwUDG8xUI-SsXupZiAu2fYd92_1v71cRf8ogFVXHg197aXVvZOoar1Ham4VDgDwT9mytLCKy_O09urgfhDcWNCRg37TDjPHlsLQnRHBg1V8GmqLFgeLuoz3QDtfVrNuarh9vK1JEa5Fv4MdpBy6InRLrQjtesWNt2D6Erb2MwZ0OkVCsWYq8RiYMdBkBPIm43s6KLxhV0-f8Nt2yisIhuSBUIzjHhigfbjfzgKRaiW2teJv13GNdTc7O4BtDqFRsnb5ejqZlE3377M0inTDZCPL6cNOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
عمق اسکواد بارساِ هانسی فلیک در فصل جدید رقابت‌ها بعد از جذب ژسوس و اتمام نقل‌وانتقالات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/29049" target="_blank">📅 18:48 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29048">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WVUBr5Ok8r9oomCVd_Ig7yRsoPrrsmNr8oQkH_4QUAmMHnz7-92eBQykUA1oZTWy5H0VzZwxcFD5oSt0ZBkxGofFx-ZbEL-6mqUPlqqUYxUe-qHDMLxX3sBK64poLJWGNh_ccCdUA07I6YgjDSW3gZ2Begyjc2hZu8TuvX6Xv7AbATNDJ65nPlWF1e3i7vRqRfvGYonmOspbdH7N6LgsdnvTBpvSYUOpR7wgeGnhyoUcyKZs3Of0yZTmL0KsTMCsyYqYq0kT9L6cxp2DiO5qm-VrruIftkJ9366svW1uAgek51D5WVzghSsSe33LHXyypKuRw-rWRI0lGUIwlq6QEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ یه‌موضوع پیش‌پاافتاده‌ست ولی چون زیاد پرسیدین لازمه یه باردیگه‌بگیم؛ استقلال در سال 1399 و 1400 دوبار درضربات‌پنالتی پرسپولیس رو درجام‌حذفی شکست داد اما طبق قانون فیفا ضربات پنالتی صرفاً به‌معنای‌تعیین تیم صعودکننده به مرحله بعدیه و نتیجه در آن…</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/persiana_Soccer/29048" target="_blank">📅 18:39 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29047">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gAogLBciz3FtptDMtYN-vVwFlRGfRbOzNljU2bNoDbrLbcyHD_IEoNokNuUbF3nKIZ3hzu_wqYHmAXcG457eq5Fs3tT6nysrWiQ5DvThjfqHEo1iUrKeCFJvR4KqjNPa3AbBSOra9UfNRnHE0Dyuv6vCp7XrTwsJTP1yZD0G4zH3HXSDIEWCkaMmbBgkujbwIqQDxrC0TkvUjoB3fwVaSuRAsYjVuWrSJD85ArVCgY1fv4go-sANavfkOTUFXS8MUAEE48Xs9w1Cjglb-MxFGRDEXL0qI7fnLYTmS-PWN66ZJyNzltGZbOlgqzaWYZ-WnGg1HK1gSEj-w5JcPWvnuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اندرسون تالیسکا ستاره برزیلی سابق النصر که در لیست‌فروش‌فنرباغچه‌اسماعیل کارتال قرار گرفته بود باعقد قرار دادی دو ساله به الجزیره امارات پیوست. تالیسکا سالانه 5.5 میلیون یورو از اماراتیا میگیره!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29047" target="_blank">📅 18:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29045">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lAcZBga73Parw7CKZHRkzwtG0fxv30kMBQAuaBAbYrH3n8Dca54lZSvIsKabYUcFAWZ9kWq_UhiujMI89QxPQj88KksmWY4-rreLX8f5DYPu5S7lv-lm2JbWnDL93_bXdoLPFG8_pzOKDY7kK6FMPcbSRLS7H0mBpCsrhPURuXAWrqW63dYrFJCE9MzGi3rYCU4xj5R7nWg3nzm-Gsznpiinz5kcWBXB6dg5lglUFLV1JwhRiqjYOUL8q1eyoeLcQbT5qnWXPK0Zd_liGwbMfRmSFzAC_qfFF1kVxztLeAJxxehuB6QCHF2rUZFXvGP0FvFibC0Pp_NM5PiBppyoNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=CnxLfdoweN50MBtxpXrKCM23xccH4dF42Hg3WTEKbCdcy4RYkr48FszBNnx6xiE0XNlJmTa5dSIyZDqJrV7TXSRHkp-S_1cLlQBZ5BkIyy6Bigx8dYO-zR6zmEc_9mmUpGZs2AsaXz1lZhiq58fMRuB2pJGYLBQgmZcEsykuXQ5EoFEvWfowAmtbakFseYnxy2V_SP9XRoyUtHjZkcwQffX0SePOg95XzKyuW07t24YfmzE9UzaB6ChybdZ3xrfsDeQLd08V4mU8-FvnPv2QtCR_qtHRBdZwaPb4T3xSroxwWaWvwkKmhTOyC69ed9Srn89OSuvcXAAsQih9ys_zcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/656f3ff7ee.mp4?token=CnxLfdoweN50MBtxpXrKCM23xccH4dF42Hg3WTEKbCdcy4RYkr48FszBNnx6xiE0XNlJmTa5dSIyZDqJrV7TXSRHkp-S_1cLlQBZ5BkIyy6Bigx8dYO-zR6zmEc_9mmUpGZs2AsaXz1lZhiq58fMRuB2pJGYLBQgmZcEsykuXQ5EoFEvWfowAmtbakFseYnxy2V_SP9XRoyUtHjZkcwQffX0SePOg95XzKyuW07t24YfmzE9UzaB6ChybdZ3xrfsDeQLd08V4mU8-FvnPv2QtCR_qtHRBdZwaPb4T3xSroxwWaWvwkKmhTOyC69ed9Srn89OSuvcXAAsQih9ys_zcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
زهرا گونیش ستاره تیم ملی والیبال ترکیه که بخاطر علاقه‌اش‌به‌کشورش پیشنهاد لژیونر شدن و حضور در رقابت‌های‌لیگ‌برترایتالیا رو رد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/29045" target="_blank">📅 18:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29044">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=KUawZx0VOtU480TatNEynSI0D9C6nhVeNtMgD10n7JEocuGwR4ZA8bWZvft1mZMne6r7J_Q8Qu7wig0tHxnYLv68M4VSZ4MHJdYNfT6KJTsSrB7Ry1xIIE-D82eEiYXIP5tcHeo8toW-HZx-EmacM0Ml57cIFn1VdFeNrj9ucjeAJeWMeU5IGnm8S0AliKQtIHONM3LWuuFgGmPrHky8xbQ2OAh3x_tC5zACHvCUmaWhlOKU2tx4uyVeak6Oz8AV-O36-dKLWJ4EvXvp1pmY1o00QMex2age6C3rsRqCFOAbaXUIhxnaoeyFYo5jy2EoAxOyUhlx0XO1QMhh3ma97A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40fd4582cc.mp4?token=KUawZx0VOtU480TatNEynSI0D9C6nhVeNtMgD10n7JEocuGwR4ZA8bWZvft1mZMne6r7J_Q8Qu7wig0tHxnYLv68M4VSZ4MHJdYNfT6KJTsSrB7Ry1xIIE-D82eEiYXIP5tcHeo8toW-HZx-EmacM0Ml57cIFn1VdFeNrj9ucjeAJeWMeU5IGnm8S0AliKQtIHONM3LWuuFgGmPrHky8xbQ2OAh3x_tC5zACHvCUmaWhlOKU2tx4uyVeak6Oz8AV-O36-dKLWJ4EvXvp1pmY1o00QMex2age6C3rsRqCFOAbaXUIhxnaoeyFYo5jy2EoAxOyUhlx0XO1QMhh3ma97A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درخصوص آخرین وضعیت اوستون اورونوف در پرسپولیس‌دیروزتوضیحات‌کامل رو دادیم. در این حد بمونید مهدی‌تارتارمیخواد اونقدر نیمکت‌نشینش بکنه که خودِ اوستون اورونوف درخواست جدایی بده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29044" target="_blank">📅 17:20 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29043">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tkDRPFGNqD2JVNYhXI4kuH2KMUliwJGKNnc2TPVuh_8w1wEQ4iNAB5u7yqz6Um9QocVyEdN07TyNVsdj-10FEJKL1vH14HWNK-P2fzqTHlqwq-juq8t5m7LTBVyWJx8LGdQHSg0idIzHfhSmgsHz5m42LbEyaZRClQcmOId113Fc9cA2_z1FlWRvaerzDTr_xSwuGIBU0pZxGnjTe1_Yax-WSIWhCL81U_JF_M56v3BNtZDuyOpRzUKX7BBKgAFDvBg_B5grzHMltiytyP9-0A8LnxTRCTjLNyHvb9JvO6xdKx5SmHuK-e6mLrezPQpv_GP9BYIonNu_yOK81_S8cA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نظرسازمان‌لیگ‌عوض شد؛ دیدارهای هفته هفتم لیگ برتر براساس تاریخ قبلی در روزهای 19 و 20 و 21 شهریورماه برگزار خواهد شد. پیش‌تر اعلام شده بود به‌خاطر بازی‌های آسیایی تیم امید دیدارهای این هفته رقابت های لیگ برتر به تعویق خواهد افتاد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29043" target="_blank">📅 16:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29042">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🔵
👤
بعداز تنبیه علیرضاکوشکی توسط کادر فنی تیم استقلال؛ سهراب‌بختیاری‌زاده سرمربی آبی‌ها این بار صالح حردانی رو به خاطر چند مورد بی انضباطی موقتا از تیم استقلال کنار گذاشته و احتمال زیاد در بازی با آلومینیوم سامان‌تورانیان فیکس خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/persiana_Soccer/29042" target="_blank">📅 16:41 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29041">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oxrubZnL7dunrZENcj218YEDA7SuukFbYB_RRuN91HExRvtdAOIgIcywguOCq-wRH4P6UIvRXUsZ74QIhFoMGfeyHUCJdrfwRceVKKx0vhRL36k8IpTCFMTrc1NZ1Z9VI7LKQimOFVhBWiih0nUubk6PEZ5dJxzh5_fD2dTwApRaN0NKdR5DK2EVQSgTnG4uYGyWRdzGwNN4r11cS8psfTpm60W6Lvfb-U1o9UsBSzEIurKBOEW66nsBL0zo-Id-BkujCqHMbhQ41Hyt-w7yKJrmf0eXEi_kqa7f8YTmtF88mYY0ueVYbKgzhdW-NmkpFr50_XYX6sSn4yHJvCBamg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ دلیل ناراحتی سرمربی استقلال از علیرضا کوشکی این صحنه است که وقتی دربازی با نساجی تعویض شد با بختیاری زاده دست نداد و به حالت غرغرو رفت نشست رو نیمکت تیم استقلال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29041" target="_blank">📅 16:22 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29040">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rcnmsyo5FE3vJr8xWgI42lxdEHBfMCCkP7Y7ArZOmJb5oNcqQnyMloJKMWUAY__FYxblT_3SzUJnPxOy_p3ZHH_PWXJk4hCdwymBY1G6hhG4AsXhyGJTrAyZQM_Y1k2C65tYVnkLn3GaAjsUf35CDxkRo9lyNqch2fj7IeNearbhbQ6NVtRPBtcMp7FrKcoF2bbK3SaVgTHMDCtvk6lhi2qrvOweFdgtg3csoZWZSNisgif-SzBm6U_16UYvJt6228_o5AEXg2CJd9UWDBt7LXfeGiNMuFrJXPBSC6o_nWmuLE3zW3_aHque3Q0V05C_FTOZ6rCDTXj6sa2uQJ2KQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌دیدارهای هفته ششم رقابت های لیگ برتر؛ بازیایه‌هفته‌بخاطربازی‌های تیم امید به تعویق میفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/29040" target="_blank">📅 16:07 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29039">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iF4Qe2uelReX6cAXAs0x-Wmdykog7wYlQbBemegdSuTpNvEEv_Utq69v4M73g9fgjhH-3aUzGEoptfbyY2eEJpyLqZAKwVCl9ILJaSDWGdryDxbsJPKkYT_F6VY1Jj0MOmOJNXORUVji6PmZVPFt6U2_gNNM63IoamM60sGyH8azpPHWsXLqJk_lyvpCAAlgG_0NgSSqrwBK_en8Vcu0E2BvNEAMoBjvY31YdnQfNwNc1UkvWDM4lwmyBDKVKI-3WbrLFy0gp-UW6RFJbxfrZ3vehiF9tHBNNcG178TTE7_UBqDtwyXJcSIfBXWe2PPjojvK5_mWz1dNAqL7rF9VHwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2fa8ecb976.mp4?token=MP9jt5SqBgW3m0J_GHFOk0ZZbHyityri-N6f__648WuhqZvrxUJss4ahYzxAfeg0p7IQWniUr4L1XLYVZnR2yJBFqWk3hOVgN9gzSJ29OKUWlUNU7d-cZ74tyvgkgjq3DyJJ2OjWteQOBWfiJq1iHR9l98s8i2JP8xK6K9iQpgfAb02X1rZFDOG8lvOcKkw0of09icWms1XMzeCBv5AC4HLWBY5orKZ2JWT6ktFxtQj7NeHxIFfLf1ALfEbBtxsWdkYIoCDvtDL9Jj0Sg3IW10-0K1_cyViOHvEoJ0hwjNDL3MHfz_wwpYffq-4LbiwajWh55x73z61er1zf84__iF4Qe2uelReX6cAXAs0x-Wmdykog7wYlQbBemegdSuTpNvEEv_Utq69v4M73g9fgjhH-3aUzGEoptfbyY2eEJpyLqZAKwVCl9ILJaSDWGdryDxbsJPKkYT_F6VY1Jj0MOmOJNXORUVji6PmZVPFt6U2_gNNM63IoamM60sGyH8azpPHWsXLqJk_lyvpCAAlgG_0NgSSqrwBK_en8Vcu0E2BvNEAMoBjvY31YdnQfNwNc1UkvWDM4lwmyBDKVKI-3WbrLFy0gp-UW6RFJbxfrZ3vehiF9tHBNNcG178TTE7_UBqDtwyXJcSIfBXWe2PPjojvK5_mWz1dNAqL7rF9VHwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نکات‌طلایی‌درباره‌قطعات‌مهم‌خودرو؛
این پست رو یجایی سیو کنید، رعایت کنید که هزینه الکی رو دستتون نشینه و برای دوستانتون هم بفرستید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29039" target="_blank">📅 15:24 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29038">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wk2mcYkiZdaZHgoHOBefPQOScphrgcWqeP08xPrkyLXvOECXWCpfSG5LFwaFcLKfYo7gmvm33OdRX4LAKAx_EP-C1POH5rEWJaJAKZ8rYDlu3J1cX2J7mQaCyF1iarJ8iElJcnC6Gleot9d7SfCrHRskyU_1WnETafzZ5mISh2RZpU8xRf1lLXBU6x2ukkIxzLfMcXA7rtE7RVpxDet_tWHjPNNunvW5AzqgDvOTNMqLEcahM0uDv5XxTfEDXYtlwGbta_K-apeEYdBhmFJvvF1EE4boaKLaimimuz7WXr8UVsfYqg1q_AedLbgiKaDehF2zMCwpsNiBVBsIGSMbXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ باشگاه پرسپولیس قرارداد زینب عباس‌ پور مدافع میانی جوان تیم بانوان خود را تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/persiana_Soccer/29038" target="_blank">📅 15:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29036">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aOiQTrIKyQHw7fdxeExtKvwXwkGLmeeqTRgDU5vg06z2Vfx4drb6EYbKVUUCvkllk2BdQiPNef5voQtPJmBoTdcYtgneCXmkx64aZf8fJpgYsQaVi_5wvF9PZP34iyn2BCm2eJVH1WjLuDzfBBtTTUFu0Xq20DTX1KmPx1csqPL35L09kEUfr9JozwC_aE7t638oken0avDJGDlXMlgNM07JUE4HKR-TQqfADGghPDeSWueGJQZED8vta1Eizdh3ykwDbz6hf4Kr3BomhU8u61LKUkow2nD3zHghMIBQ8HlhGYDGIo9vqxWfspNQglrXkvCsuUymM5FztuvNC4mEZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e-08Wj2oel_6-8eVLTunqRcKCfV18Ygg4QUMrNYaIqxJ2-lBfkR6S1nBd-pbOhsWYvdnupwLHxyfNgG3qWNFtK7miITuv13-_m49YF9f_PdYVN_I0YPM4bZXKywuXAO6KtaJOpXn6M-zIxBlCwkI2Ay2fiAJytmqLpeGd5RoHrC28E1EMzdRoetrFEZixr7FOE58UTr3GHO3MmNEKY0NMOa0AglHrlHW8WOGOABWKdUov_yd7mJkUJLjilMxai2zVs5wY5crfxb5k__0HNCh6bB8cKN-a8GnpgC4rRZumQsTcLnECauqeu9zlb1BsEsx9ZoU-iCrCzI51f8mTbhLlQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/persiana_Soccer/29036" target="_blank">📅 14:45 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29035">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQzAb168qweCyp417eX3g0L6a8t2RsfIoc2Xve7QsEJL4rhCDE5cDVkJZA8XocA2QsUhS1EcHVLoH44yTGHHhTFjgZ6Of51_7N6bBx2BELi79BRwZrMXMQ5BZTYnUDWZE1ivEPEqw8uiOArP0d88uGfiECBCRA_dqlbVNZcGxixqWg2xI9bTtipBWFJpaPh1-LfWY8ggjOOQH8I8p5R5-MZ-VtXwFQzYKR3vkmQvY9Ilxea8Rlx4HcfjWKbCg7AA5tlrFcprYhNbTJHEpHupvxg6L96-wCkLz9o3XrK6h-TA9ABHF5P4NKIcm1uSkUCehJToWnvEaKiw1R0UfYmI3XWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75386b7e5a.mp4?token=oS-UlZnyWjAWuoX3Xgo6KKTMMI0ThoLQV1l1gbQEzoKv_kHNUOU9vr5_-gfW5tBMI7jPBeP1Dh_cPxNvJc5cmabtB7yXcyhjWgQMyRQkQZFAUlSZPmkPefIjIgP2igvhOzQcdPWYfNoKHY5gwvk-1_wfR6PqVuu65cnFipKvXi1rDKiyUxJQE6AWdJVFdw2Hy8Mco4JjjhQsAEbt1GPcvyFSlpbmDxzIAZWTq3K-raMDdOerDdMqm_slxChOk2TtY2TYZSmHoVPxazhgP8f3EUX5njjwIiTW7lK0bj3KCjxvvY6k-px0vi5dx07rvv3I99cWBmERhoOKOc73B1jjQzAb168qweCyp417eX3g0L6a8t2RsfIoc2Xve7QsEJL4rhCDE5cDVkJZA8XocA2QsUhS1EcHVLoH44yTGHHhTFjgZ6Of51_7N6bBx2BELi79BRwZrMXMQ5BZTYnUDWZE1ivEPEqw8uiOArP0d88uGfiECBCRA_dqlbVNZcGxixqWg2xI9bTtipBWFJpaPh1-LfWY8ggjOOQH8I8p5R5-MZ-VtXwFQzYKR3vkmQvY9Ilxea8Rlx4HcfjWKbCg7AA5tlrFcprYhNbTJHEpHupvxg6L96-wCkLz9o3XrK6h-TA9ABHF5P4NKIcm1uSkUCehJToWnvEaKiw1R0UfYmI3XWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لبخونی‌صحنه‌جنجالی شهرآورد 107 پایتخت؛
کاپیتان تیم پرسپولیس غیر مستقیم به سامان فلاح میگه من کاری میکنم به تیم ملی دعوت نشی‌ها!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29035" target="_blank">📅 14:17 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29033">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O39iGuEb20bPSq1QCz7kRqjWozThnCWKywxArUK83BppxNDiSMw_J58dr_V7orn74zFeiHurxsUjXTG9dka93KYqNJvhL6Zk-GxPxLcW9sPrUP-7VB0vnEGDa-W7ajhLtkSS4_3dlL4spthwl9rJ-8Qq2Ax2cZZIhyjsuequr4rOyDSSHZVQRc-DvmGfEhuF9eSis9DybhBWUREP18qwLG-2aSyf_bkeyqfCM6mwqZyQ0CqBQN0olOqaAeCeyGW1K8NeNoM0hu4V3w1s0HfsxU3EXv4lceSc1_8gt1lHsK9PmCjr-Py4FeA55szQYCYwgLnHM7NifqPqSnU2_jUZ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aHWKYA_xTYcs0eTY2QT4r8lTfxeLl7NlKkwG567j1OHNX5Qjm-1KbuIYZeUC3XRFB9DhBCE8OQIhv5bMYXKarGQl_N_5RCdkkjjGOdBUYFVV7QgN2u1oi72CT8504XIxvk9t8X5vFZZ9XAWp9tZhZwJZL12OEgch5wpgjbXKtCIaE4EqTA2o-cXQ242AG3vGeX7LfjcWfCBDCoJ3Y2yv8AsMFTPmfDeaLDNq7qtWjNMk8Re9IVJt5maUOaP6Xqg3JlLmakTHWMzxny3QE_haaGSoGwKaNDUns-GfLX3d4AjX48muFFWUgXCMCQ0QG__CYKman_NDz7P09rbWYbTkkQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/29033" target="_blank">📅 13:55 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29032">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DSLDMAW8OD7kIIAjCTscsLo2h9w7Y2en3psIcZk8d_PxGFvjLsEFzy1hQnbwa00oLvu32TWnVWS-NFjJb6gVnWJIcPdGKHCh2h7MS9LWIl4TSyNauo9DJu2Uhbd99PwTMEUPuMllmFmjJjctp-4IKLqMkinKcLjXJU4tPrn7ZPZyobYhf-yvf_iaM2hqo3mQm5PgqHwSn5nIGT_J9DKtFIsiHEhvN8-ZCxeAH2nThGPnn3q0kzPxg-juU2QBlixYMGYU_gKfsUHBvEBGsdVjgKvWdR1ydmcprCGTMr0o2vAHwPjvvyvxXenTkqdQcL_HyiALtc3ufJTSidTc_R3LLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
🤩
دیگو سیمئونه سرمربی‌‌اتلتیکو مادرید:
3 بار درآستانه گرفتن کاپ‌قهرمانی چمپیونزلیگ پیش رفتم اما هربار کریس رونالدو اونارو از من گرفت. قطعا اگه رونالدو نمیبود من الان سه قهرمانی UCL داشتم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/29032" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29031">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=Siuj8fsxzbWNcFOsbXkTaWtC2o5wBvV-Y-0tdGxJKikZ8Q4RaHTGrUVc59s7xwNNyrur91U0Nwz-dg9n50sJ0a9PaekFCpq_V6ytYwNFZZIHoaJNOWW4mi0wWb_HsZlsrKg_l2_KwTM8fil5G-j-j524AAs4YlxZMvHX2T4GUEemCJWi_VLVMzwXcH6IkGohN9nzzNbME0Fjwed54HA77tahb-fCXr-MeWODlFPzw8PHeX9-d5cLj4dmPRFSI-0EtndgvY30XPP2BXHdo-umtwoGEN2zns4Pky9Ebfdp9Xh2uB-9z1J_21C4qY38tOv2VhfOL-L-3JE2wQzZq1z0pCsp12qY3wVQdF9_3R-cxFPKYhEwBz_iY199F_FR2dRKODg0RhR4wh3squjXqntQ7koFzxOW46iJo53_lu-pg1KJawY3gCAhyIIOMj-E3bLXzv8fopRoff0pl3ZC71gw8Cab6Rp749dYR2N6_whHhZt_zh6XIVtYo5y-RG4VhE8ZRsD0SaeP6i4orpItfmKnyWxP07NTWnWWig2_QRkWB44ZKYtZ4J5k-kJY-mM0UWHFpzrg9KqNsI_BzN7kbi3-1f05yqXFNE0JfRqbrBdIKNVe2016cO1B5mxGp8frTRDMMROVUT8OxZbuKU7fE2oJ391ykZa6qgEvDrm6XYmAAdo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/989a5b2f6a.mp4?token=Siuj8fsxzbWNcFOsbXkTaWtC2o5wBvV-Y-0tdGxJKikZ8Q4RaHTGrUVc59s7xwNNyrur91U0Nwz-dg9n50sJ0a9PaekFCpq_V6ytYwNFZZIHoaJNOWW4mi0wWb_HsZlsrKg_l2_KwTM8fil5G-j-j524AAs4YlxZMvHX2T4GUEemCJWi_VLVMzwXcH6IkGohN9nzzNbME0Fjwed54HA77tahb-fCXr-MeWODlFPzw8PHeX9-d5cLj4dmPRFSI-0EtndgvY30XPP2BXHdo-umtwoGEN2zns4Pky9Ebfdp9Xh2uB-9z1J_21C4qY38tOv2VhfOL-L-3JE2wQzZq1z0pCsp12qY3wVQdF9_3R-cxFPKYhEwBz_iY199F_FR2dRKODg0RhR4wh3squjXqntQ7koFzxOW46iJo53_lu-pg1KJawY3gCAhyIIOMj-E3bLXzv8fopRoff0pl3ZC71gw8Cab6Rp749dYR2N6_whHhZt_zh6XIVtYo5y-RG4VhE8ZRsD0SaeP6i4orpItfmKnyWxP07NTWnWWig2_QRkWB44ZKYtZ4J5k-kJY-mM0UWHFpzrg9KqNsI_BzN7kbi3-1f05yqXFNE0JfRqbrBdIKNVe2016cO1B5mxGp8frTRDMMROVUT8OxZbuKU7fE2oJ391ykZa6qgEvDrm6XYmAAdo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.5K · <a href="https://t.me/persiana_Soccer/29031" target="_blank">📅 13:47 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29029">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbJa1lsIly8AjP1bTpLpMBF6YsVT05nP0hZzxghqHk2PcAZX9xsOMfnAJu07-G3ii4L4JHZNiY7yB6bmXD-SmNUMpzybeaRNvV59pGqZx3OjdcC25e5zNptsGCqcJ0rlMnxuTrszeuDIHtrwDNLs8CWqketg37E4ccbyt4O9tmyu-F7kvwYaZEL3DuFMm2trTATsyO0Oq84TllK9RgWOE9d88KXggZAyh6kNVbMsY65MFn7r5MHO9VU8XRvFN5WDSHcRYFAtBujPCfGkerazViYktTnTttZh_11EayuMgijBPYzkFrEGgH92OQdMbp2HwYvzfjV1Mvbvf9CXmyNR2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟣
🇦🇷
نشریه ESPN: احتمال اینکه لیونل مسی و لوئیز سوارز درپایان‌فصل‌جاری رقابت‌های‌لیگ MLS ازدنیای‌ فوتبال‌ خداحافظی کنند بسیار زیاد است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/persiana_Soccer/29029" target="_blank">📅 13:13 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29027">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P271S5EoRlksWzxfGhrCI6tbm-wmPyye1v48a_ekG2eF1RGxU0hAzXDsU3I-PqFzQCKptVUmTIPWvb9qHhX3vPhHu_3RzHspLYs67axPnc_to8y8aGsIaoOaThmKGFwWeXMgOfkPaq88fvkm_xMckKY4WapMAcy5vyf4EHwRB-asEeZTDbCqlzKiZsrjJnMuSRzN0JAuzKEJWDLsa-MyTKajojysKcpPBjVSD89rbrS1dfNqLqIFga6eieeUNABIfikUOrdE5DdRXkiLmb_mA6tBIBRu1tdq233RPKcL6dCiLBhf5EobfdWetUGyPL1LrgffqB43j7xv7OD2jvApjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tmXoZkmnHl6QU6PZKfbgJ6qrXAwueIjK2IsFTQvdbHmIghSLpVYXynLZK3yqY8C12uJGpHXb8POZUbKSvximLvrFcQ_wx1WeCOgOPqaC3W3DCuZbXQD0rpZHPGHbXShfrpmgVY0FxQ6NNWEEHz5d9-cxTB1qJCmdUxD0TU9Q_TY3kyISFvSMUNgPQ4uDqvRMEAlV83zZxeTJ3amxbFFETon6L92ae1BH7sqP52_hGbOzTuWPqQuw0iVV1sEgaBKqjmcDiHA1xCH9Ntmujknpp2rkn4nu8fEqRx-Sh-_CcRxeDUkiEIl9z2YGawbKjqLvpd-hLe9ilj_0zFxjXT_QdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
ترکیب تیم منتخب بهترین نقل و انتقالات لالیگا و لیگ‌جزیره در این‌پنجره؛ باهم اگه بازی کنند بنظرتون کدوم ترکیب خفن‌تره و میبره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/persiana_Soccer/29027" target="_blank">📅 13:06 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29026">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I2LyOiq2Z2QTuo36uSum5C5oeZe7Gc_2E0cjO0PRv-Vj5Z2fp2sDlsng8VHifGYwm9e2D7q4q0sUOadmtV9-KuGhDSh4SfEw7P7zf62dfgAjfCAiPmg7hN1Mv1HcksaWruuNADuCiH5Emm6m6PtKuqB1RYcthuMxqMn5z052R1xNC6jLTfpV5B2Cd53scRn6-1gsA9P_1B2iplPozSDwQ99FTExjqw9LBirFzcophwOV5uZPegMMjTt2liSR1UMADhxceJu5qFiDFYdlFRbe_iAi_e6x9x8Y-gVRVSxAwSeOGtfr_DvleM9tHT9AcS_7WbuQFUA_Ahzz86Sc2x7XuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
سمیه‌اسماعیلی‌ستاره‌کُردستانی ملوان با عقد قرار دادی دوساله رسما به تیم بانوان پرسپولیس پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/persiana_Soccer/29026" target="_blank">📅 12:31 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29025">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkpWTLTKmuXfvxTodODj0D3zhEcQ7yZi0JzmfAsaYfqti2bpDGt0r8BM6uu5ayxBgkd7gAhNyjZ4vP8SuhkSUjjWLpAN2Ui4vnIsNspVbzuESbHP37zSF6Yu9KwQxnFG5oj2rpQ_6XfEvPphdUYW0pxgJv9-Mvz662VbJ10bD3jrcYrLvE3oqiPZ-1hiwmyR5DRxbBtYYKjDKm1NNklw0KjP87MFJF1xoN4f42sanTAf-2puUAdJ4FwTUEPG66dS4-7MEQxHql4Q9B3bVN565RXlPxwZwhwfuk6wp_o6snzW6yy7LOByBOvhE61HArzJKdykhpo5CB_M_9bGF57y7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29025" target="_blank">📅 12:27 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29024">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BhORXgzI3oOD1IPWAzRkE4AHce-xkxqn2S-TAaBa1rGZ5y8L_NXVSIlC4djjSk_GZxjBuQMLOz_kdVJ-dGRFEWQpghNpZOuCJfdoC5EnNRuFfxYniGb3k7BmknpF7GieqWltNDUfinuPdUrs_RJEVj4cZxQ1ssDijgBEta-e9KCkf3E102Z8dkPgVoqGe1YnPFLOAHkI6YSOYXSYIMKQai_b9EAEa7oLrZqqo4I-TTG_gWqffAo4IVFVoxDcn--KTFnJFgGnR6TL1ta5ah_7ZAKE6fyvyCh3YTgGUZg0AbuGvqGz-lDL06bPCk-qMleHOkktbsr2cvbOJkESSDGlPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سه‌نفری‌که ثابت کردند که هیچوقت برای شروع دیر نیست با حضور علی‌آقای دایی از ایران؛ اسطوره دوست داشتنی مردم ایران فوتبالش‌رو از 23 سالگی شروع کرد. ماهی رو هر وقت از آب بگیری تازست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/29024" target="_blank">📅 11:44 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29023">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=SOqdNmgXqGEHWnf9K2RITO5lXz-z-RPON2aMrF7eYxJ08I5p2PRWdk4DiktVHWSyqlVIq9SUS2tzMVPVLK5W8MVSa-E_IZ40ZsEiur-ygPF_n8sCuEPbOVBlM8hxqWI6LC6ak97lQ5veoKOJpUkmQv_aYuCx5osWj5cb3VoLiuqAd1h1FPNN0OeMGDVeHhwyefOJvs9IBk0zlZrXz0DJlx0ci0bctu-W6_Z1vh0wJmmHowNvvx_AlmAveGOuU0dCFrypdwpb6MOB_RW6Y3aIqkabP-sm8c9-h-ccwafDg35mx9dIOJlfTQXg6vAGXsHgUi3kpo-dzbnkMyrGRrcQuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ebccea1a.mp4?token=SOqdNmgXqGEHWnf9K2RITO5lXz-z-RPON2aMrF7eYxJ08I5p2PRWdk4DiktVHWSyqlVIq9SUS2tzMVPVLK5W8MVSa-E_IZ40ZsEiur-ygPF_n8sCuEPbOVBlM8hxqWI6LC6ak97lQ5veoKOJpUkmQv_aYuCx5osWj5cb3VoLiuqAd1h1FPNN0OeMGDVeHhwyefOJvs9IBk0zlZrXz0DJlx0ci0bctu-W6_Z1vh0wJmmHowNvvx_AlmAveGOuU0dCFrypdwpb6MOB_RW6Y3aIqkabP-sm8c9-h-ccwafDg35mx9dIOJlfTQXg6vAGXsHgUi3kpo-dzbnkMyrGRrcQuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
👤
👤
بوسه و درآغوش گرفتن کریم باقری مربی‌پرسپولیس‌توسط‌سهراب‌بختیاری زاده سرمربی جوان استقلال در پایان مسابقه جذاب شهرآورد!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/persiana_Soccer/29023" target="_blank">📅 11:12 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29022">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">▶️
تمامی گل‌های هفته پنجم رقابت های لیگ برتر؛
دیدار هفته‌ششم مسابقات از فردا شروع خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/persiana_Soccer/29022" target="_blank">📅 10:46 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29021">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vpak0v2TMiCO4yZL8n9OciTWAvH_k3uNEpdh0wrcyd7bfxpXhMfPu9L8QipRi_TIkzmzg0eav6phT7GJQP_J4-RyGggeHjWpJmGzJxqCv7zBMveGkxLyT1ncekD_OJYhCb6QsjHmWai5FLtJpQJSXSyN_3Mlju-AHZ1Nnz27ZQcuPTOiWIdUJdIQE6khbU4R4yrIfEgyjPM6GkuN1qSRyGL2MQ1gHUaKbf2DAGmBj3at55f8wSmhHEhyfCQrg7qRTEkYZr4F3FReiWBj6TgMPsK6ocnukx6aRTBdgghhJK5eGTDg_yKkfBk1COlz9zXYZvjL-5qGhUK-47Y6F1r5wQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق شنیده‌های ما؛ باشگاه استقلال در نیم فصل تموم تلاشش روبکارمیبره تا رضایت نامه مهدی قایدی رو از النصربگیره و این‌بازیکن‌رو به استقلال برگردونه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/persiana_Soccer/29021" target="_blank">📅 10:30 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-29019">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VV3Yq6mMfKUzbtR0wNSteeitVPG37ScJ6rAxEs6n4yQucELmR4llu1zOd0zIHuV59PCPGA93HMM5oMVpqEV0cIvPXqQL3fZ_hudzcT4ow-jOBaPtK0-U6aaisXFVY0X1bjRQzDPlIHkh7ivZrmeFO79RYkKal-eCA9noqZ1Sjc0glOjlLvL7bxMkiXShS5XVPXMuAdUh4PXrbt9ysh1Ae6nqJqP8GXV0BuvVFNRDte4x3bwEHflRT8UvPYqdlzfFdBA8l3DkGgnKa466NYWHp0ojxKtGGV25cUBmPTb6zbTCY9OmzCbrIpvBS8yElIZpEOVGEm3ocdtlqcd0XNMxvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AHrKTM-7XYrBH3uFqw3hH4MzK4VhDI45lvay5gfrlI0Xb-Q-BDAWk0J5Hp6P6lHWzlZebEbQ5rx6GwRHMvs10O3kqdQO3Cyob8zGmrP7ZmiI2koI0GFpM1XVah5VYa45UOESjJiK3hZCUfoQJm9W42FWFb0H96oCQhHhkMZyzVFgBeti-STy4Vk0DkTHunnrM5kF0GG-JDU_GGP-d12dBSM9eDbIo4MV6ETF0fee8_oTtbD1hXcjfdQrpakSm4sMTvdbOkve2eb7xgMuLz1getvuw6K3fAtHROO-g4qgPDEYYCyAVqHxEaNe3o1LfRe-FyphFxXT1045vsVnMCEbEA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
دوستاره‌‌جوان‌تیم‌ملی‌والیبال و فوتبال ایران.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58K · <a href="https://t.me/persiana_Soccer/29019" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
