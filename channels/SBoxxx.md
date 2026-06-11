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
<img src="https://cdn4.telesco.pe/file/gHuhhFvElCmFI3oXmlrBWIu1kW3QhjIVPMp1163IrJC7PqYJhxWDgC_GIVKGsb3DMWX_3ZfD799Ayy0heRIj1MoU-JU_hHjuOhtqo722i9zat0876Y-t4Xn_b-aD-WGlN_SYkmwk2XmfW8Ih65tARgOO1jl4AXbygJyFPY50AO82hIMMNjyS0I8rH7Z0T6-CT-mby6JEoHYQ73IbtC7MTUL0Nfa-YDLfCTiMzCcBfwiORkP86pKEZ4Y0iimLsBQTnhibrAdYesHqjaYZ8Z8qLQ4ihPVkX7Ynx96HVyvgWJANG7cg2y9Tq2EE2h3KdvpkhCpSi8y6DYthW_LoSi1sBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.1K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 تاریخ، ژئوپولیتیک و بازارهای مالی</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-21 06:16:46</div>
<hr>

<div class="tg-post" id="msg-17289">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">— مرکز فرماندهی مرکزی ایالات متحده پایان حملات آمریکا علیه ایران را اعلام کرد.</div>
<div class="tg-footer">👁️ 914 · <a href="https://t.me/SBoxxx/17289" target="_blank">📅 04:38 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17288">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">انفجارهای شدید در بحرین</div>
<div class="tg-footer">👁️ 923 · <a href="https://t.me/SBoxxx/17288" target="_blank">📅 04:36 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17287">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرماندار اشتهارد:
صداهای انفجار احتمالا مربوط به انفجارها در خارج از استان از جمله ملارد تهران است.</div>
<div class="tg-footer">👁️ 941 · <a href="https://t.me/SBoxxx/17287" target="_blank">📅 04:35 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17286">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سردار موسوی:
تنگه مقدس هرمز را ناامن می‌کنید؟! منطقه را برایتان جهنم می‌کنیم</div>
<div class="tg-footer">👁️ 964 · <a href="https://t.me/SBoxxx/17286" target="_blank">📅 04:32 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17285">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">آیا ایران در صورت حمله آمریکا، کارت برنده هسته‌ای دارد؟
پپه اسکوبار گزارش می‌دهد که اگر ایالات متحده جنگ علیه ایران را از سر بگیرد، جمهوری اسلامی می‌تواند به سرعت برای انفجار یک وسیله هسته‌ای در خاک خود اقدام کند؛ نه به عنوان یک اقدام جنگی، بلکه به عنوان یک نمایش غیرقابل برگشت و مستقل از توانایی کنترل تسلط تشدید تنش.
یک سوال واضح: آیا ایران می‌تواند در صورت لزوم به سرعت یک بمب هسته‌ای بسازد؟
به گفته استاد MIT، تد پاستول، ایران در حال حاضر مواد کافی (۴۵۰ کیلوگرم اورانیوم ۶۵٪) برای تبدیل آن به سوخت درجه تسلیحاتی برای یک بمب هسته‌ای کوچک دارد. و با همین مواد، آنها می‌توانند حداقل ۱۰ بمب از این نوع بسازند - به اندازه‌ای کوچک که روی موشک‌هایی که می‌توانند به اسرائیل برسند، نصب شوند.
چگونه؟ با استفاده از یک ترفند ساده: پیچیدن هسته هسته‌ای در یک "بازتابنده نوترونی" (ساخته شده از اورانیوم ضعیف شده یا سایر فلزات). این کار نوترون‌ها را به هسته بازمی‌گرداند و واکنش را کارآمدتر می‌کند.</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/SBoxxx/17285" target="_blank">📅 02:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17284">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ایران در حال آماده‌سازی برای انجام یک حمله بزرگ علیه اسرائیل با استفاده از سلاح‌های جدید است.</div>
<div class="tg-footer">👁️ 2.22K · <a href="https://t.me/SBoxxx/17284" target="_blank">📅 02:10 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17283">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">خب موج اول گویا تمام شده.
به نظرم از جمعه موج اصلی حملات شروع بشود.</div>
<div class="tg-footer">👁️ 2.24K · <a href="https://t.me/SBoxxx/17283" target="_blank">📅 02:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17282">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">بیانیه روابط عمومی سپاه پاسداران انقلاب اسلامی:
پس از نفوذ یک فروند جنگنده اف 16 به حریم هوایی خلیج فارس و شلیک موشک از سوی سامانه پدافند هوایی سپاه پاسداران، هواپیمای مهاجم متواری شد.</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/SBoxxx/17282" target="_blank">📅 02:05 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17281">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است  هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/17281" target="_blank">📅 02:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17280">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">یمن به آمریکا هشدار داد - درصورت ادامه حملات به ایران سکوت نمی‌کنیم</div>
<div class="tg-footer">👁️ 2.36K · <a href="https://t.me/SBoxxx/17280" target="_blank">📅 02:02 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17279">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-footer">👁️ 2.33K · <a href="https://t.me/SBoxxx/17279" target="_blank">📅 02:01 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17278">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">فاکس نیوز گزارش می‌دهد که اهداف بعدی نیروگاه‌های برق در ایران خواهند بود.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/SBoxxx/17278" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17277">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">📡
حسین اژدهایی ؛ خبرنگار ویژه صداوسیما در بندرعباس:  در قشم و چند شهر دیگر صداهایی شبیه انفجار شنیده شده است که هنوز محل آن نامشخص است</div>
<div class="tg-footer">👁️ 2.31K · <a href="https://t.me/SBoxxx/17277" target="_blank">📅 01:59 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17276">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=RUBVG0oli9ykV4YMS86RhkKgXai0v8M_n-JzxKjQ3EJnWNbvpGDdyRQocU9GVg0Gge1-O33Qd9mtE2NZAz0pGVgzSo3lXANmb1KDCnih9hw60CQrOir9TaNR3lEquLi5ENbRM8ZSIYIBEoL3fnnjKjjIAUq5GehWB6DjBHb0MXjFQ3Dcv6ToRkYsKLjyoqFYuRHb85XDqxfFSkaa5rupophsFPy2MwUGHTIZwUOgUMwbPDdnz6ui8FVu5yDLlh_wb3VVANmOb5ve857CoDiOZQ1RnhjM0TqMIAyJ969nG8CNjs6y6YMFIsm9u3t2tahKZsGb0gJ21f_Eau61smUtYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34cf9de796.mp4?token=RUBVG0oli9ykV4YMS86RhkKgXai0v8M_n-JzxKjQ3EJnWNbvpGDdyRQocU9GVg0Gge1-O33Qd9mtE2NZAz0pGVgzSo3lXANmb1KDCnih9hw60CQrOir9TaNR3lEquLi5ENbRM8ZSIYIBEoL3fnnjKjjIAUq5GehWB6DjBHb0MXjFQ3Dcv6ToRkYsKLjyoqFYuRHb85XDqxfFSkaa5rupophsFPy2MwUGHTIZwUOgUMwbPDdnz6ui8FVu5yDLlh_wb3VVANmOb5ve857CoDiOZQ1RnhjM0TqMIAyJ969nG8CNjs6y6YMFIsm9u3t2tahKZsGb0gJ21f_Eau61smUtYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این را بفرستید خب</div>
<div class="tg-footer">👁️ 2.32K · <a href="https://t.me/SBoxxx/17276" target="_blank">📅 01:57 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17275">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است  بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/SBoxxx/17275" target="_blank">📅 01:50 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17274">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">درگیری‌ها در تنگه هرمز بین سپاه پاسداران و ایالات متحده در حال وقوع است
بر اساس منابع محلی، سپاه پاسداران و نیروی دریایی ایالات متحده به طور فعال در تنگه هرمز درگیر هستند.</div>
<div class="tg-footer">👁️ 2.44K · <a href="https://t.me/SBoxxx/17274" target="_blank">📅 01:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17273">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 2.55K · <a href="https://t.me/SBoxxx/17273" target="_blank">📅 01:41 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17272">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mSjJ5Lw5XmyO3m11ziSntFlNfhQJHUpNfhk5_S9KN9zjB5nD-98qZ3N2hPQUOLVT5B5_ifOw9LIUprC4OcfDWmUICXdP3Zz_Q0j4ttJ2jfn8Qg0ammT0Tbohpghw9xovYAsEqFYwxAjmrd5mgZGCTgMtW-bADL0eBPmWFvMfA_aNyEHAD-NpDKWHH1wXpav6CqhRuajyLvS08T9w021MzPJumY6SiQbbIXWrhxczJrcOpv9yNAbEhka-cmX4e72NqNQIgVX_o6mjMUVsu_DxzgkloVu-l0-Ov6LkryX3zb0a1vgZsx2Luy4d8dKqUruPp2wiwmuQ7b6iANJD4FHwdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مناطق مورد حمله آمریکا</div>
<div class="tg-footer">👁️ 2.63K · <a href="https://t.me/SBoxxx/17272" target="_blank">📅 01:40 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17271">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=WK8LsVMD2iIQJT6WCDigdhlBbFjpx9Q34L9OmK6vpcpeQyQXGdULlPomCSuSLnAFatdaZlmmL-Gp9aBUusCBE8A4KpWdHRoRB-9NWB5Bj5iuWMQuIM_O6O63Xts9RdcFLSbf0jWg7Yzjom9_oMrfqB_PErIXBRobEBXuw6ujCexmxfrooUGMwCb0H0Qa1SXoFAw7dN7QIKKgKhTAlXNwMIH5S3x4ixtedy7nbiFBdbzVxLaii-cFr64tEX5OhOuZA1Yt5Pkj2FLA_qD4jnxt7wGbwqXosCa9oX27SOqmHAIUQQAYpVKTo6i6tAiHGzzkmHEEGnuO-TQFpaWIF__LhQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7111d88fe1.mp4?token=WK8LsVMD2iIQJT6WCDigdhlBbFjpx9Q34L9OmK6vpcpeQyQXGdULlPomCSuSLnAFatdaZlmmL-Gp9aBUusCBE8A4KpWdHRoRB-9NWB5Bj5iuWMQuIM_O6O63Xts9RdcFLSbf0jWg7Yzjom9_oMrfqB_PErIXBRobEBXuw6ujCexmxfrooUGMwCb0H0Qa1SXoFAw7dN7QIKKgKhTAlXNwMIH5S3x4ixtedy7nbiFBdbzVxLaii-cFr64tEX5OhOuZA1Yt5Pkj2FLA_qD4jnxt7wGbwqXosCa9oX27SOqmHAIUQQAYpVKTo6i6tAiHGzzkmHEEGnuO-TQFpaWIF__LhQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/SBoxxx/17271" target="_blank">📅 01:30 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17270">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KOJf7vCPQJ01y9LDz8K3vmrVhqpgspfOxCaAsmVoenetQp5lcnIq83nSczKsbWOE83D4tlVSkITyd3Rf5DhB4rWbrs9sxAXGM3mhV8qpjiHqIDIoL4yYrGMCYw6Bzj6_VRGthXzoUwBr34RcvdPbjVjrQocO-i8ImbGhpO42zm-ymnTUIN-w5I1TTcLdDnFFs8wQTxHX7MqC6q_3AaxqSi1TjkxaQu8-rgB8I9c7RqEBQYRIPjiKLMoN9nQqaZZPiYHo0mujQFXLzn-Gj8QSiIED53NJezm_CWq2mOLX12cpGy_BBQDTr2jF7NfIJX2FdSeoOlKmCBpcrNNXVeV6tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💪
صداوسیما جمهوری اسلامی ایران به نقل از ارتش آمریکا ، خبر از تهاجم این ارتش به مواضعی درخاک کشور ایران داد</div>
<div class="tg-footer">👁️ 2.8K · <a href="https://t.me/SBoxxx/17270" target="_blank">📅 01:28 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17269">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">یک مقام آمریکایی می‌گوید حملات به جنوب ایران شامل «صدها هدف» خواهد بود و به مدت ساعت‌ها ادامه خواهد داشت</div>
<div class="tg-footer">👁️ 2.83K · <a href="https://t.me/SBoxxx/17269" target="_blank">📅 01:27 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17268">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">به نظرم میخواهند بگویند راه مذاکره (تسلیم) باز است و در ضمن به کنگره هم بگویند که اینها حمله نیست بلکه دفاع از خود است.</div>
<div class="tg-footer">👁️ 2.88K · <a href="https://t.me/SBoxxx/17268" target="_blank">📅 01:23 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17267">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">یک اصطکاک ریزی بین آمریکایی ها و اسرائیلی ها قابل مشاهده است که به نظر بعد از لو رفتن قضیه جاسوسی اسرائیل از سیستم اطلاعات نظامی آمریکا ایجاد شده.  اما به نظرم موقت است و راهبردی نیست.</div>
<div class="tg-footer">👁️ 2.85K · <a href="https://t.me/SBoxxx/17267" target="_blank">📅 01:22 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17266">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">یک کارخانه پتروشیمی متعلق به مجتمع گازی پارس جنوبی احتمالاً در عسلویه هدف قرار گرفته است
هنوز مشخص نیست که آیا دود دیده شده ناشی از سقوط ترکش است یا یک برخورد واقعی.</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/17266" target="_blank">📅 01:15 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17265">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 3K · <a href="https://t.me/SBoxxx/17265" target="_blank">📅 01:14 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17264">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله دفاعی دیگر چه صیغه ای است؟!</div>
<div class="tg-footer">👁️ 3.03K · <a href="https://t.me/SBoxxx/17264" target="_blank">📅 01:09 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17263">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیروهای فرماندهی مرکزی ایالات متحده امروز ساعت ۵:۱۵ بعد از ظهر به وقت شرقی، با دستور فرمانده کل قوا، حمله‌های دفاعی اضافی را علیه چندین هدف در ایران آغاز کردند. این حملات در پاسخ به تهاجم بی‌دلیل و ادامه‌دار ایران است.</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/17263" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17262">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.  @U_S_CENTCOM</div>
<div class="tg-footer">👁️ 3.1K · <a href="https://t.me/SBoxxx/17262" target="_blank">📅 01:08 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17261">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromU.S. Central Command</strong></div>
<div class="tg-text">U.S. Central Command forces began launching additional self-defense strikes today at 5:15 p.m. ET against multiple targets in Iran at the Commander in Chief’s direction. The strikes are in response to Iran’s unwarranted and continued aggression.
@U_S_CENTCOM</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/17261" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17260">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">صدای انفجار از بندرعباس</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/SBoxxx/17260" target="_blank">📅 01:07 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17259">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">شلیک موشک از غرب کشور</div>
<div class="tg-footer">👁️ 3.01K · <a href="https://t.me/SBoxxx/17259" target="_blank">📅 01:06 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17258">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">تسنیم:
انفجار در سیریک</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/SBoxxx/17258" target="_blank">📅 01:04 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17257">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">انفجارهایی در سیریک و جزیره قشم (منطقه تنگه هرمز) گزارش شده است.
سامانه‌های پدافند هوایی اکنون در غرب تهران فعال شده‌اند.</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/17257" target="_blank">📅 00:58 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17256">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">خداوکیلی ببینید گیر چه اسکل هایی افتاده ایم!  اینها برای فرزندان ما تصمیم میگیرند!</div>
<div class="tg-footer">👁️ 3.09K · <a href="https://t.me/SBoxxx/17256" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17255">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">به نظر می رسد جنگ قطعی شده.</div>
<div class="tg-footer">👁️ 3.2K · <a href="https://t.me/SBoxxx/17255" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17254">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گزارش موسسه مطالعات جنگ از کمک های نظامی و اطلاعاتی روسیه و چین به ایران  روسیه از تلاش‌های ایران برای بازسازی توانمندی‌های نظامی خود در دوره آتش‌بس حمایت می‌کند. نیویورک تایمز به نقل از مقامات آمریکایی گزارش داد که روسیه قطعات پهپاد را از طریق دریای خزر به…</div>
<div class="tg-footer">👁️ 3.16K · <a href="https://t.me/SBoxxx/17254" target="_blank">📅 00:55 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17253">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">سخنگوی کمیسیون امنیت ملی مجلس:
در جنگ ۴۰ روزه وسعت آب‌های سرزمینی ایران افزایش یافت، در جنگ بعدی شاید وسعت خاک ایران افزایش یابد.</div>
<div class="tg-footer">👁️ 3.07K · <a href="https://t.me/SBoxxx/17253" target="_blank">📅 00:46 · 21 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17251">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">ادعای منبع پاکستانی به الحدث:
ما امروز از امضای توافقنامه صلح، دور شده‌ایم.</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/17251" target="_blank">📅 23:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17250">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">مسئول ایرانی به المیادین:  آماده اجرای نسخه جدیدی از جنگ هستیم  شبکه المیادین به نقل از یک منبع امنیتی سیاسی بلندپایه ایرانی اعلام کرد که  اگر ترامپ این‌بار در محاسبات خود مرتکب اشتباه شود، قیمت نفت با صدایی بلندتر با جهان سخن خواهد گفت.  این مسئول ایرانی…</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/SBoxxx/17250" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17249">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">مسئول ایرانی به المیادین:  آماده اجرای نسخه جدیدی از جنگ هستیم
شبکه المیادین به نقل از یک منبع امنیتی سیاسی بلندپایه ایرانی اعلام کرد که  اگر ترامپ این‌بار در محاسبات خود مرتکب اشتباه شود، قیمت نفت با صدایی بلندتر با جهان سخن خواهد گفت.
این مسئول ایرانی تصریح کرد تهران برای اجرای نسخه جدیدی از جنگ آماده است و غافلگیری‌هایی در انتظار دشمنان است.</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17249" target="_blank">📅 23:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17247">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">لینک ویدیوی نشست امروز با نیما</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17247" target="_blank">📅 23:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17246">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ادعای خبرنگار الجزیره: واسطه قطری تهران را ترک کرد   واسطه قطری تهران را ترک کرد. به گفته وی سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.   منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای…</div>
<div class="tg-footer">👁️ 3.83K · <a href="https://t.me/SBoxxx/17246" target="_blank">📅 23:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17245">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">ادعای خبرنگار الجزیره: واسطه قطری تهران را ترک کرد
واسطه قطری تهران را ترک کرد. به گفته وی سند توافق برای حل برخی اختلافات که هنوز به دلیل تغییرات آمریکا پابرجا هستند، نیاز به کار دارد.
منابعی در تهران می‌گویند هرگونه حمله به ایران به معنای پایان اجرای آتش‌بس است و واسطه‌ها در حال حرکت برای جلوگیری از هر درگیری جدیدی هستند.</div>
<div class="tg-footer">👁️ 3.85K · <a href="https://t.me/SBoxxx/17245" target="_blank">📅 23:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17244">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شبکه CNN: فرماندهان جدید ایران ریسک‌هایی را می‌پذیرند که اسلاف آنها از آن اجتناب می‌کردند
حملات موشکی این هفته ایران یکی از جسورانه‌ترین اقدامات تهران برای بازتعریف خطوط قرمزش است و نشان می‌دهد که رهبرانش آماده پذیرش ریسک‌های بزرگ‌تر هستند. تغییر گسترده در استراتژی ایران با حملات اخیر گامی رو به جلو بود. این تحولات نشان‌دهنده یک چرخش بزرگ‌تر در تهران است؛ جایی که نسل جدیدی از رهبران در حال کنار گذاشتن رویکرد محتاطانه و تدافعی سنتی جمهوری اسلامی هستند.
آنها اکنون به جای اتکای صرف به بازدارندگی و صبر استراتژیک، تمایل بیشتری برای پذیرش ریسک و به‌کارگیری اهرم‌های نظامی، اقتصادی و منطقه‌ای خود جهت شکل‌دادن به تحولات خاورمیانه دارند.این نخستین بار در دهه‌های گذشته است که یک قدرت منطقه‌ای ابزار، ظرفیت و تمایل به کارگیری قدرت سخت در برابر مانورهای نظامی اسرائیل و آمریکا را دارد.
تهران به دنبال ایجاد یک معادله جدید است. رویدادهای اخیر بار دیگر ثابت کرد که رهبری فعلی ایران بر این باور است که هر آنچه از طریق دیپلماسی به دست نیاید، در نهایت از طریق قدرت قابل دستیابی است.</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17244" target="_blank">📅 23:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17243">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XtbBIV7iO-cjwIZQoIYLT6kDpaJe3HGJmH54enqqH_e818MDzHWrvoTx_mznL2D_Ay6nIuE8qzWywFdqzQVJq5Ak1eWALPr40jJOsxBE5dYOkarLgUaepZy5P-AbMX6ZZqnl4TQIZKkhggdychr2c8BBxdM1jop2iMsnSXCDzyL_kxd-s0zOvltAoebcn6uExj9C68dguJ9odHjeDeW4YD1E81KzIkhyvuPSwwScGTWjJVbycaSXQ9XJ6bz6dV4YibJg0CSHKosfMbITd_T29hR65Tf9LwXZdxA3feAe0hUbi9eg59QVtdNKv5QarLnyKJh_UFfgjAdOUzfm9eUziA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آتش سوزی در میدان قیام تهران</div>
<div class="tg-footer">👁️ 4.51K · <a href="https://t.me/SBoxxx/17243" target="_blank">📅 20:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17242">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SArTqxq-MW9lxMa-yDmLQZBPvOugc1QgoR5ZGNSSGvtdmDuW5KARv5hnxQwVKIyPKXykMkS29JVMzjPSeYFb4vaaHDbd0LJ9XVAtneIZHPFXAbAW0KeE6svjMLQlun5RhHdDHBKfOVpEDgYxa_q-j9CyOnK1va9O2FS774JVmC86KFRYkN1Bz7lXyeTa24HMOjAC1GLgFL1wQbmoMpnyiMapOgdPuFcnHDQKN-u0IvVrINQvm7DbUOD9P25xZTBwCh9y61FQAl6glKgflpzRhP9BgEmyBKURmFqC8OIyZwyB9I57uxaoK-BJIwmjYS3kH1W0AMbqsPPpaHitq6tk8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا نفتکش «سیتی بلو» را در خلیج عمان هدف قرار داد  سنتکام: نیروهای آمریکایی نفتکش «سیتی بلو» را در خلیج عمان مختل کردند. یک هواپیمای آمریکایی پس از سرباز زدن خدمه از دستورات، موتورخانه کشتی را هدف قرار داد. از آغاز محاصره در ۱۳ آوریل، سنتکام ۸ کشتی متخلف…</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17242" target="_blank">📅 20:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17241">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آمریکا نفتکش «سیتی بلو» را در خلیج عمان هدف قرار داد
سنتکام: نیروهای آمریکایی نفتکش «سیتی بلو» را در خلیج عمان مختل کردند. یک هواپیمای آمریکایی پس از سرباز زدن خدمه از دستورات، موتورخانه کشتی را هدف قرار داد. از آغاز محاصره در ۱۳ آوریل، سنتکام ۸ کشتی متخلف را هدف قرار داده است.</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17241" target="_blank">📅 20:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17240">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ا ترامپ:  «ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/SBoxxx/17240" target="_blank">📅 19:40 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17239">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">تصویب قطعنامه ضد ایرانی در شورای حکام ( ۲۱ رأی موافق ، ۳ رأی مخالف و ۱۰ رأی ممتنع
)</div>
<div class="tg-footer">👁️ 4.46K · <a href="https://t.me/SBoxxx/17239" target="_blank">📅 19:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17238">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ا ترامپ:  «ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.48K · <a href="https://t.me/SBoxxx/17238" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17237">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ا ترامپ:
«ما بسیار به رسیدن به توافق با ایران نزدیک بودیم، اما آنها مدام ما را به تأخیر می‌اندازند و به ما بی‌توجهی می‌کنند».</div>
<div class="tg-footer">👁️ 4.42K · <a href="https://t.me/SBoxxx/17237" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17236">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">لینک ویدیوی
نشست امروز با نیما</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/SBoxxx/17236" target="_blank">📅 19:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17235">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❗
ترامپ: من نزدیک به صدور دستور حملات جدید به نیروگاه‌ها و پل‌های ایرانی هستم - فاکس نیوز</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/SBoxxx/17235" target="_blank">📅 19:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17234">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59886795a.mp4?token=Hk-75xA2AX6an5_1yurnzs6HXn76QZoIRWjcUwoorzc7SSc5MxddIzI27iAblaoFqEAkyLLQCU1r2Mv4wq50Jli2-uS9HtpoVBymw0RKvW2zd7Yu5O5Lb-p0iYa6PQVnoL_loP9DqECkbZDavRccHGPrvl8Sjjwfivm3K4MwTm-sPa46PoaxIeWznfnpSeQdBLAsv3c1n3vvr2cgsZgPTHblgM2TaLnUAgSXfKth1XGi_a0lzi8RIAUfcxli6pkZuvlr7U9h9r7ndhUzereaneVFj32rJi6gpH9DpR1C3fJiApul4M1v-HGO0rM5_0ooU1P5WzCOi6OJ7RPq7QY4Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59886795a.mp4?token=Hk-75xA2AX6an5_1yurnzs6HXn76QZoIRWjcUwoorzc7SSc5MxddIzI27iAblaoFqEAkyLLQCU1r2Mv4wq50Jli2-uS9HtpoVBymw0RKvW2zd7Yu5O5Lb-p0iYa6PQVnoL_loP9DqECkbZDavRccHGPrvl8Sjjwfivm3K4MwTm-sPa46PoaxIeWznfnpSeQdBLAsv3c1n3vvr2cgsZgPTHblgM2TaLnUAgSXfKth1XGi_a0lzi8RIAUfcxli6pkZuvlr7U9h9r7ndhUzereaneVFj32rJi6gpH9DpR1C3fJiApul4M1v-HGO0rM5_0ooU1P5WzCOi6OJ7RPq7QY4Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/SBoxxx/17234" target="_blank">📅 19:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17233">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">ترامپ درباره ایران: امروز دوباره به شدت به آنها ضربه خواهیم زد.</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/SBoxxx/17233" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17232">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عجب گیری کردیم به حضرت عباس</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17232" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17231">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/SBoxxx/17231" target="_blank">📅 19:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17230">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">باورتان میشود این دو جمله را ظرف چند دقیقه گفته؟</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/SBoxxx/17230" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17229">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.16K · <a href="https://t.me/SBoxxx/17229" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17228">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">❗
ترامپ: ما به شدت به ایران حمله خواهیم کرد</div>
<div class="tg-footer">👁️ 4.09K · <a href="https://t.me/SBoxxx/17228" target="_blank">📅 19:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17227">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">این یعنی نه ایران و نه روسیه از این جهش بهای نفت حداکثر استفاده را نبرده اند؛ ما به دلیل محاصره دریایی آمریکا صادراتمان افت کرده (پست ریپلای شده را ببینید) و روسها هم به دلیل حملات سنگین پهپادی اوکراین.  عربها هم که عمدتاً ضربه دیده اند و لذا بزرگترین منفعت…</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/SBoxxx/17227" target="_blank">📅 19:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17226">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">جالب است بدانید در جنگ جهانی اول، عثمانی متحد آلمان بود و در جنگ جهانی دوم هم نازیهای آلمانی با گردان های پان ترک مورد حمایت آنکارا در میان تاتارهای کریمه بشدت همکاری داشتند.  اساسا یکی از دلایلی که استالین تاتارهای کریمه را بعد از بازپسگیری اوکراین از نازی…</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/SBoxxx/17226" target="_blank">📅 18:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17225">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">اردوغان:  «هشتاد و پنج سال پیش، سکوت و بی‌عملی در برابر هیتلر منجر به از دست رفتن هشتاد میلیون جان در سراسر جهان شد. تمام بشریت بهای جنون هیولای خون‌آشام را پرداخت کرد.  امروز، همان اشتباه تکرار می‌شود. نسل‌کشی‌هایی که توسط قصاب غزه، نتانیاهو، و کابینه او…</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/SBoxxx/17225" target="_blank">📅 18:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17224">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">اردوغان:  «اجازه دهید این را بسیار شفاف بیان کنم: هیچ‌کس نباید به دنبال ماجراجویی برود و هیچ‌کس نباید خود را به واگن شبکه نسل‌کشی‌های صهیونیستی ببندد.  اگر هر کس سعی کند بر حقوق و منافع ترکیه و ترک‌های قبرس در شرق مدیترانه تجاوز کند، می‌خواهم بدانند که پاسخ…</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/SBoxxx/17224" target="_blank">📅 18:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17223">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترکها در ظاهر می گویند اردوغان موفق شده ترامپ را متقاعد کند تا از این طرح جلوگیری کند اما به نظرم این پلن A شان بوده و پلن B شان شامل ورود مستقیم نظامی به ایران همراه باکو برای اشغال شمال غربی ایران بوده که پیشتر اشاره کرده بودم.  در هر صورت، در راند بعدی…</div>
<div class="tg-footer">👁️ 3.59K · <a href="https://t.me/SBoxxx/17223" target="_blank">📅 18:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17222">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">نتانیاهو از تشکیل اتحاد جدیدی علیه «محور شیعه بنیادگرا و محور سنی بنیادگرا» خبر داد.  این اتحاد شامل هند، یونان، قبرس، کشورهای آفریقایی، کشورهای عربی و کشورهای آسیایی خواهد بود.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17222" target="_blank">📅 18:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17221">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ارتش اسرائیل تأیید کردن که در جریان حمله موشکی ایران به اسرائیل در اوایل این هفته، خساراتی به پایگاه هوایی رامات داوید نیروی هوایی اسرائیل وارد شده است.</div>
<div class="tg-footer">👁️ 3.71K · <a href="https://t.me/SBoxxx/17221" target="_blank">📅 18:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17220">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ارتش اسرائیل تأیید کردن که در جریان حمله موشکی ایران به اسرائیل در اوایل این هفته، خساراتی به پایگاه هوایی رامات داوید نیروی هوایی اسرائیل وارد شده است.</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/SBoxxx/17220" target="_blank">📅 18:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17219">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MFvp5NW9_QCu8UF1w0hZ47R5kjeCAuuwxYh0biwpUKiWDUAFL2PsJYEoG6kQb_wkd3E8js2NvKuhPcSiQVraaE4WIDpvV-0K1SUsprF-JfyegeZnqbY2zHjGNh_2IZ3qU-56WS6p62WLiLX4lfdnaz-4h3scWDtLWr04v6LUWdPctTHNMX_2g_5EgwwTFKT9o2qdsDU12db90P3vhuecs6GS2upkm-4Vh0theJ8PA22gazcwD8-H7ay-bK8XS7EePw5X_iH3MItYOOp6oEG7HQwp--vq_8BJoltD2dg2e7CLDOh6arHsj9iPQtBxZOdKEiiRGVLnhCl8Pm7tNqMj6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تولید موشک‌های بالستیک تاکتیکی کره شمالی به شدت افزایش یافته است.
کارخانه‌های این کشور تولید موشک KN-23 را افزایش داده و کیم جونگ اون دستور داده ظرفیت موشک‌های بالستیک و کروز طی پنج سال ۲.۵ برابر شود تا نیاز روسیه تأمین و کشور در برابر هر سناریوی آمریکایی مقاوم شود.
کارشناسان کنگره آمریکا مانورهای صعودی این موشک‌ها را پیشرفته‌ترین دستاورد تسلیحات تاکتیکی کره شمالی توصیف می‌کنند. نوع بزرگ‌تر آن حامل کلاهک ۲۵۰۰ کیلوگرمی است، از سامانه‌های AEGIS آمریکا فرار می‌کند و سال گذشته ۱۰۰۰ فروند از نوع کوتاه‌برد آن در خط مقدم منطقه غیرنظامی مستقر شد.
کیم جونگ اون شخصاً از کارخانه‌هایی بازدید کرد که از اهداف فراتر رفته بودند و این توسعه را وظیفه اصلی ارتش بازسازیشده کره شمالی خواند.
این کشور همچنین تولید مواد هسته‌ای درجه تسلیحاتی را دو برابر کرده و موشکهای هایپرسونیک خود را آزمایش می‌کند،</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/SBoxxx/17219" target="_blank">📅 17:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17218">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">از امشب ساعت 21 در ورزش سه؛
💡
جواد خیابانی و خداداد عزیزی در بر جام 2026
🏆
متفاوت‌ترین برنامه #جام_جهانی2026(بر جام) با اجرای جواد خیابانی و خداداد عزیزی
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 3.97K · <a href="https://t.me/SBoxxx/17218" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17217">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromورزش سه</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2f8d3318cf.mp4?token=ceeMFF996syU_imShiNpfzLw8sE-nLy2cIwWqBmfvBGDXs_fK6jDzX7qBovIJI5xpNlV6V1leymCF66B3GSFTw99MB2PXkWnqhc2rrSaOWBnoXBU07XCukssGxYDFKsO3qQEVkgsD4f1FhZhoqamAxnzajKP44TBSIc4G7TQXcRDatW6FJ5GxOs_-ESCycSgFeBlIDqOLXLX17QARsa_itfjhp_z3A5YulprdFuyvM-nMNMRPOTsfFdHezRQB6f3c1aIz_ERiFxNWQm5R8nvgfWF5T0DL0VE_dxTItH2t782gpa1rMk0feMkaXTbAWWSoKIGMuAbgGxeBwfPqwQzQwfCUdx-2WKueb6I1vc42OdMImkhyQVGWZRU72hOjQap1TlfJLecvJti19-C0ZRSsEfPElJlzEwtlZe-HhOX2L8SN4VVrfSpQBm4wafKhYELOo_vAXD_9y0c9FaFwnq7n9udQXjkJmeiA7gevcQwbmIWgJWKRUHyVVWXVgUaEbeCWaPbMC9VaFHBP2oAHk7zx0yjsfEnmxAIxq9vyrLnw3xokpvhVvcYhxyxUbIJwPi_nNJskdKO3Ca9LejvABd8y883QAqnUqS53tLRtJZ8Jj_rVi22tqacqsR0M1oH0wN-J8nSIkc1TmO-g3g5hvIMWRZKY_MPVcxlylQieXv5rng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2f8d3318cf.mp4?token=ceeMFF996syU_imShiNpfzLw8sE-nLy2cIwWqBmfvBGDXs_fK6jDzX7qBovIJI5xpNlV6V1leymCF66B3GSFTw99MB2PXkWnqhc2rrSaOWBnoXBU07XCukssGxYDFKsO3qQEVkgsD4f1FhZhoqamAxnzajKP44TBSIc4G7TQXcRDatW6FJ5GxOs_-ESCycSgFeBlIDqOLXLX17QARsa_itfjhp_z3A5YulprdFuyvM-nMNMRPOTsfFdHezRQB6f3c1aIz_ERiFxNWQm5R8nvgfWF5T0DL0VE_dxTItH2t782gpa1rMk0feMkaXTbAWWSoKIGMuAbgGxeBwfPqwQzQwfCUdx-2WKueb6I1vc42OdMImkhyQVGWZRU72hOjQap1TlfJLecvJti19-C0ZRSsEfPElJlzEwtlZe-HhOX2L8SN4VVrfSpQBm4wafKhYELOo_vAXD_9y0c9FaFwnq7n9udQXjkJmeiA7gevcQwbmIWgJWKRUHyVVWXVgUaEbeCWaPbMC9VaFHBP2oAHk7zx0yjsfEnmxAIxq9vyrLnw3xokpvhVvcYhxyxUbIJwPi_nNJskdKO3Ca9LejvABd8y883QAqnUqS53tLRtJZ8Jj_rVi22tqacqsR0M1oH0wN-J8nSIkc1TmO-g3g5hvIMWRZKY_MPVcxlylQieXv5rng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از امشب ساعت 21 در ورزش سه؛
💡
جواد خیابانی و خداداد عزیزی در بر جام 2026
🏆
متفاوت‌ترین برنامه
#جام_جهانی2026
(بر جام) با اجرای جواد خیابانی و خداداد عزیزی
🆔
@varzesh3</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/SBoxxx/17217" target="_blank">📅 17:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17216">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وزیر اسرائیلی میکی زوهار در پاسخ به اظهارات اردوغان:  دیکتاتور اردوغان اگر جرات کند ما را آزمایش کند، سرنوشتش بدتر از ایران خواهد بود.</div>
<div class="tg-footer">👁️ 4.49K · <a href="https://t.me/SBoxxx/17216" target="_blank">📅 15:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17215">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">❗
ترامپ: من نزدیک به صدور دستور حملات جدید به نیروگاه‌ها و پل‌های ایرانی هستم - فاکس نیوز</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/SBoxxx/17215" target="_blank">📅 14:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17214">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VaWnKyARqUQ2YKMGl4mr3DIR4kAS89It6AN-lZLLF1eqpKfvwauudPsbppSPoTkxAoiMjpMwSQOs4mrdu2FQ7sOf64P07iKbX8oi3NkaU76dMQZKYG1rtInMhwm6p8mBlhGfzoZFGC-p31GWOKHGYE4tYB18KPfsWwOCXOcgcRu3iGZN6z0fGQSb_1AFUO99RdXHORu3dFHYU-Veswn1_4-WJuBaJKbzi6vay7gEF1d-Z2TvioNScFnGPgHkF49VP7sdouuX6vPExORd6Y4G2fA7EiapU86xi81h9izF8EaQhAsZMVpoqHcD9rNbOPd48rCmAZvxSlS7XxugxAlDIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/17214" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17213">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ترامپ:
نیروی نظامی ایران کاملاً به هم ریخته است. بخش زیادی از آن، مانند نیروی دریایی و نیروی هوایی‌شان، دیگر وجود ندارد - آنها کاملاً شکست خورده‌اند.
ایران فقط حرف می‌زند و هیچ اقدامی نمی‌کند. قلدر خاورمیانه مُرده است!
آنها برای مذاکره بر سر توافقی که می‌توانست برایشان عالی باشد، خیلی دیر کرده‌اند
،  حالا باید بهای آن را بپردازند!</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17213" target="_blank">📅 14:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17212">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رجب طیب اردوغان رئیس جمهور ترکیه : «حملات نتانیاهو و شبکه جنایتکارش علیه سوریه و لبنان به نقطه‌ای رسیده است که نه تنها این دو کشور برادر را تهدید میکند بلکه اکنون ترکیه را نیز تهدید میکند.»  امنیت ترکیه تنها در هاتای شروع نمی‌شود ؛ بلکه در حلب ، دمشق و بیروت…</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/SBoxxx/17212" target="_blank">📅 14:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17211">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rjt74EL0qyvCqtlKPlXABQ44uqO6Bq2ZpSf1GJ7_4bOiL-ooC6_kI3eJYeqb-Xg1i-bEQEa7Re6tzNB2sLYSdtqJ9Ky1bdx7UdoQxjBk6AiwHJWLg-asy8ESQ-ST5hZt9nYtXRA0rYNpPuVIIT2T-Nq1cFEFbqV-JRFYmTUtPtckQgkLMG3y30nVng8ZS3nomcUafzOsOhHjS_rebU1vfpGY5rJfnkFhaRnk29HNk5D6Qet9Pp7XeYHlreBdddWDFPJGcyOc9Oxozrwum2UjYJ6VEs-i5VhferAHIFcs0vbX6RkEqPt24S0rpW_TYwfYr-t-O3AJP7cfsH5FMU5j6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متن کامل گزارش کنگره آمریکا درباره هواگردهای سرنگون شده ارتش این کشور در جنگ با ایران:  بررسی کلی  در ۲۸ فوریه ۲۰۲۶، ایالات متحده آمریکا با هماهنگی اسرائیل، عملیات‌های نظامی علیه ایران را تحت عنوان عملیات خشم حماسی (OEF) آغاز کرد. این درگیری شامل نبردهای هوایی،…</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/17211" target="_blank">📅 14:07 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17210">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/veqtKToY6CgsswZRq68P5sXEY-LuJMBhHjHW2voyUv84Z4Rst50iQRp9N7tjFr1Ww8vGPKHZJ-0CfhRoHqg7-pqNTuodZ9MKhxOzQVNlbbUSouSznBzrnnrPKtmNUzt8_xMdGk2uWHrF27SeJQHdqacsUY-jPDFSs-xqH5d61Lh1iPYVoRNXL1EJHptohx1XlKKNpqWpuI3t6hJycTqhXxStfnVvuKZl6lila3awxH4WA3VA1yph4URK6zq7yf88K9rdSrBLOR9gM03-1zcONm0ii9PWSJztzGdCHY0cGIhwdWbAz9I-5NgGRA_gniG5z7zOz1EErVWxbs7M6v7TIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رجب طیب اردوغان رئیس جمهور ترکیه : «حملات نتانیاهو و شبکه جنایتکارش علیه سوریه و لبنان به نقطه‌ای رسیده است که نه تنها این دو کشور برادر را تهدید میکند بلکه اکنون ترکیه را نیز تهدید میکند.»  امنیت ترکیه تنها در هاتای شروع نمی‌شود ؛ بلکه در حلب ، دمشق و بیروت…</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17210" target="_blank">📅 13:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17209">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">اردوغان:   حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/SBoxxx/17209" target="_blank">📅 13:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17208">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">اردوغان:
حملات اسرائیل به سوریه و لبنان اکنون به تهدیدی برای ترکیه تبدیل شده است</div>
<div class="tg-footer">👁️ 4.53K · <a href="https://t.me/SBoxxx/17208" target="_blank">📅 13:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17207">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">ارتش  آمریکا از شامگاه شب گذشته تاکنون در سه موج حمله مراکز راداری و کنترل فرماندهی سپاه (زیرساخت های کنترلی تنگه هرمز ) و دو مخزن آب در قشم، سیریک و جاسک را مورد تهاجم قرار دادند.</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/17207" target="_blank">📅 10:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17206">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">ارتش  آمریکا از شامگاه شب گذشته تاکنون در سه موج حمله مراکز راداری و کنترل فرماندهی سپاه (زیرساخت های کنترلی تنگه هرمز ) و دو مخزن آب در قشم، سیریک و جاسک را مورد تهاجم قرار دادند.</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/17206" target="_blank">📅 10:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17205">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔶
سنتکام: حملات ما پایان یافته است</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/17205" target="_blank">📅 08:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17204">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">سپاه هم اعلام کرد که حملاتش پایان یافته است.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/17204" target="_blank">📅 07:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17203">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔶
سنتکام: حملات ما پایان یافته است</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/SBoxxx/17203" target="_blank">📅 07:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17202">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fc5a29e1d.mp4?token=tJkStcukZ6pREBX0uBpOOoqXwchkt5P8mcT5TB5m4-oq2yn2eT_Our6lCbtzf7bXy95L_5KNG38ZiZwORVwTBq9R2_7hrgLE-MDgNDy8WmOxW2Bj157dVLWyxWJdjJPLqIuFdDfuEYdL1yjBR8s93ziwoF-KABvtoVJXDcSggOV3iingrm3waywCOgheg_l7SUL2ZLSOMX7-HADw0OnDhw9lA_t64mEBEbutCDcdYTd93v8Usy-3CciiFAtx2wG-2DxF5v-gTiDb7r_7AcNkDWQX5sixOxfbw0flcX-z92N3y4YiApW9fy9S5HpFFohihJvGAvqCEFlh6ueN1E00uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fc5a29e1d.mp4?token=tJkStcukZ6pREBX0uBpOOoqXwchkt5P8mcT5TB5m4-oq2yn2eT_Our6lCbtzf7bXy95L_5KNG38ZiZwORVwTBq9R2_7hrgLE-MDgNDy8WmOxW2Bj157dVLWyxWJdjJPLqIuFdDfuEYdL1yjBR8s93ziwoF-KABvtoVJXDcSggOV3iingrm3waywCOgheg_l7SUL2ZLSOMX7-HADw0OnDhw9lA_t64mEBEbutCDcdYTd93v8Usy-3CciiFAtx2wG-2DxF5v-gTiDb7r_7AcNkDWQX5sixOxfbw0flcX-z92N3y4YiApW9fy9S5HpFFohihJvGAvqCEFlh6ueN1E00uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداوسیما !!</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/17202" target="_blank">📅 07:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17201">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">— یک مقام آمریکایی به نیویورک تایمز گفت: «ادعاهای سپاه پاسداران مبنی بر انجام ۲۱ حمله به پایگاه‌های آمریکا در منطقه کاملاً نادرست است».</div>
<div class="tg-footer">👁️ 4.84K · <a href="https://t.me/SBoxxx/17201" target="_blank">📅 07:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17200">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔶
سنتکام: حملات ما پایان یافته است</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17200" target="_blank">📅 05:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17199">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">خبرنگار صداسیما در سیریک:
در پی حمله امشب دشمن آمریکایی به سیریک، ۲ مخزن آب بخش بمانی مورد اصابت قرار گرفته و آب آشامیدنی این بخش قطع شده است.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/17199" target="_blank">📅 02:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17198">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">فوری | نیویورک تایمز درباره مقامات ایرانی: حملات هوایی آمریکا به پنج پایگاه و تأسیسات رادار و توپخانه در سواحل جنوبی هدف قرار گرفت.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/17198" target="_blank">📅 02:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17197">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ترکیه هم به شمال عراق  روسیه هم به اوکراین</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/SBoxxx/17197" target="_blank">📅 01:53 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17196">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">پاکستان هم به افغانستان !</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17196" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17195">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">با وضو و غسل جنابت وارد شوید</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/17195" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17194">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوستان آماده بازگشت به فضای روحانی بله هستید یا نه؟!</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/17194" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17193">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اسراییل حملات به بیروت را شروع کرد</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/17193" target="_blank">📅 01:22 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17192">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">خر تو خری مملکت را ببینید:‏
در حلی که «صداوسیما»، «زیر نویس شبکه خبر»، «منبع آگاه نظامی در تماس با خبرگزاری نهادِ نظامی»، «معاون وزیر خارجه»، همگی «ساقط کردن بالگرد آپاچیِ آمریکا توسط ایران را تلویحا را تکذیب کردند!»، ناگهان «سخنگوی کمیسیون امنیت ملی مجلس» گفته: «دستِ رزمنده‌ای که بالگرد آمریکایی را ساقط کرده می‌بوسم!»</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/SBoxxx/17192" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17191">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اسراییل حملات به بیروت را شروع کرد</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/SBoxxx/17191" target="_blank">📅 01:17 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17190">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">رودان چه شد پس</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/SBoxxx/17190" target="_blank">📅 01:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17189">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">فهرست اولیه اهداف آمریکا:
💢
پایگاه دریایی سیریک
💢
پایگاه دریایی جاسک
💢
موقعیت پدافند هوایی بندرعباس
💢
باتری موشکی ساحلی میناب
💢
باتری موشکی ساحلی قشم
💢
بندر قشم</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/SBoxxx/17189" target="_blank">📅 01:13 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-17188">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خدایا آن ده؛ که آن به!</div>
<div class="tg-footer">👁️ 4.63K · <a href="https://t.me/SBoxxx/17188" target="_blank">📅 01:00 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
