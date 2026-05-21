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
<img src="https://cdn4.telesco.pe/file/qVKtTtaQs8NtqspdAxpgljvwLJ3urYk0B6hzFfbaa7azqy_hQDtoWwBfZWXNcRsxHEedhi9gYnnBA49Q3OsE9ue4hN4L86VfpBWsU6E0C2Nf5BaARbE1b5rMYTBV-E8BEMOtXE9eeFgNy5NX9UwvtVvVY1LaWYAPKl3FSReuAeE04sx8bj7qKKDuL_7U7GlOrUWEwUSkS2e5saPn7szmnlx62Ue0jrP66akwr0Ssb-erdVeK3dAv6Y2lMCseApTGM0bguE-ORniYqGdbqL9BBtc3jlXbldOQpdsE8ZUgfRf0VzVaohKCQ1LBR7eByxV_lCqYbUFdSD3HJ-46pXHNig.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 3.94M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforii</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-31 17:27:22</div>
<hr>

<div class="tg-post" id="msg-653403">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">♦️
رفتارهای غیرانسانی مقامات رژیم صهیونیستی با اعضای کاروان صمود، صدای کارشناس صهیونیست بی‌بی‌سی را هم درآورد!
🔹
مئیر جاودانفر، تحلیلگر صهیونیست: انتقادات نتانیاهو از رفتارهای بن‌گویر، کاملا سوری و ویترینی است؛ این‌دو در انجام این رفتارها شریک و همکار هستند.
🔹
بن‌گویر قبل از ورود به کابینه نتانیاهو، ۵۶ بار کیفرخواست داشته و ۸ بار هم متهم شده بود.
🔹
این‌ افراد مدام به فکر جنگ هستند؛ چراکه آنها فقط بر أساس جنگ و خون‌ریزی می‌توانند بقاء داشته باشند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 304 · <a href="https://t.me/akhbarefori/653403" target="_blank">📅 17:25 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653402">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aP_H2vv337ip1RZfG557c1WbukEq4IbN70HDkSeQO3R0pToEusC7218aF4Uoot07idpoUR8gCb_arZoBrB9gJfxBzybIXmSa3D0cfqNukrV8Akx_9E4OThG-vFb69b2wzwJzZut3JhcsRMfcSk13QkuBck-vG_s9sx1rFuO6DanlE-ZG-sS8PedSDob_5FdFMOnagvu0_iiB8ME5NGN-XoY4ntLDuSfWUXAMOROoHVsO_D3x7x6ElCoX5qWadHRy2MMlf60QU7M410pWAsW0wsNEDSlRn89MEHJinbHyttjeB1zmzvNG3MFNuoZncbtrf9UPxbszGJbjk3rwx4mj3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
غول نفتی امارات: تا نیمه اول سال ۲۰۲۷ جریان کامل نفت هرمز برقرار نخواهد شد
🔹
رئیس شرکت نفت دولتی امارات متحده عربی ادنوک نوشت: حتی اگر جنگ علیه ایران همین حالا پایان یابد، جریان کامل نفت از طریق تنگه هرمز تا قبل از سه ماهه اول یا دوم سال ۲۰۲۷ به حالت عادی باز نخواهد گشت.
🔹
این چشم‌انداز از جمله بدبینانه‌ترین پیش‌بینی‌های مدیران ارشد صنعت است و تاثیر اقتصادی طولانی‌مدت جنگ علیه ایران را برجسته می‌کند؛ جنگی که به گفته آژانس بین‌المللی انرژی، به دلیل مدیریت تردد در تنگه هرمز، بزرگترین بحران انرژی تاریخ را رقم زده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 423 · <a href="https://t.me/akhbarefori/653402" target="_blank">📅 17:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653401">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/630c1a7be9.mp4?token=SWSplZpuZSo7Q3sLdOcn4NQMMqAoVr2PO0eSp6uuaKvmjvYRUnwEqqD7bON0NXE9GT8PKeowzV_tnlBpxWEMp5AfVbgNa0g8dwdavQJGXtu72s4YalqLI18ACjrJvs17Mo_IXQNE5aHTVWuiX6RqPahrpgipXvhePYqJDBpnmdTtJmXAM0n_BN9Ohuj0-_xzh791jDL2gjLIhRDyyvvubvlC7iM4wr4Gc0fSo4gGrb1CXGGYrFBhYw2VHwV3RQ9mZzyTdG5aB4alR4Eu-CxPflsiDWTBeTVaZLApJ5eONvit5_6RL3oXbeCLjYbtmcSFNl05OW3xdbpwIrlVsUNwYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
افشای وضعیت سربازان آمریکایی پس از حمله مرگبار ایران به پایگاه آمریکایی: نه پناهگاه داشتیم، نه آمبولانس؛ فقط رها شده بودیم!
🔹
افسران آمریکایی در گزارش جنجالی شبکه «سی‌بی‌اس» آمریکا: انتظار داشتم ببینم صف آمبولانس‌ها به سمت ما می‌آید یا چیزی شبیه به آن، اما خبری نبود. حس کردیم که تنها مانده‌ایم. بی‌توجهی بسیار زیادی به ما شد که این غم‌انگیز و دلسردکننده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/akhbarefori/653401" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653400">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E0LHIb-y--UkZ8BvCgrMqKAa3atL5BbfMskFTYWbabtp_EDBU9jwldRp9y9Wa4E2RBgOAc2_sfseh68JMG-O6a_Q6mhYfblGDTTbWx8S6qJya7HeaEF5qmypbLiNbwwqXcqOV1fR96Z8wu3ZvKWiqh0iouwrJ0pSLM7a807Rq3Htu93x1rQ7i2o-XXOsCH5jVv5IH5_DNXNgH1DI28UArJXQ0mP3YCYIcmbxbpERMvc2DQsX5nUF6EUdV08Z6CdlTQk7WDW8WUtrfkttcSxkQIVj-dReGDRP42Yslu2Vt8xEPFVPUU7fjsDo4ZwzoFEmxRq6I-WJ0GWdlbjE9EF1dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شگفت‌انگیزترین عینک هوشمند رونمایی شد؛ دیگر نیازی به یادگرفتن زبان نیست!
🔹
گوگل با همکاری سامسونگ، تازه‌ترین شگفت‌انگیز عینک‌های هوشمند را رونمایی کرد. این عینک‌ها بدون نمایشگرند و تنها با دستورات صوتی کنترل می‌شوند و رقیب مستقیم عینک‌های «متا» هستند.
🔹
با این عینک‌ها کاربر فقط با نگاه کردن به یک شیء یا مکان، می‌تواند مسیر رسیدن به مکان مدنظرش را متوجه شود،  تماس‌ها را جواب دهد، پیام‌های متنی ارسال کند و جواب‌ها را از طریق جمنای به صورت صوتی دریافت کند
🔹
اما غافلگیری بزرگ، ترجمه همزمان صدا است. این عینک می‌تواند در یک مکالمه زنده، صحبت‌های طرف مقابل را فوری به زبان شما ترجمه کند. حتی متن‌ها (مانند تابلوهای خیابان) را نیز برایتان می‌خواند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.43K · <a href="https://t.me/akhbarefori/653400" target="_blank">📅 17:10 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653399">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/64d9f1e65f.mp4?token=MJK1AwQmsStzaExEacXryRUzjBNXKXveCc6p-uU_yv2j2o3rDH4wri7j8M-PMNilHtmiJUxtdDHvJW1TJMXfHZPTHS15CkWFn5z0hRw0rbDPCBAegjuiaWTWqdxfOytDqItUTbkZ7l5HQXRHHwYcqCwpop4mGMIhDMiG2HE0DjP3-PuXoZfg0vGXudVx2PlWgxGG4WY1sK6GCORsxpcfkgFkG_v8zzBahi-CQvp6JCB4CqxLZpMxxKSDdNsBQfaJ1UOYHgRPVYNam66wgCGZ12lBzZzT84C1QVQGWhRHKZNNZpr9ihv2kFaSKQSBO-JMro-fCi-5Rv0_VwWQZGmmkw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیگیری اتاق اصناف برای توسعه اینترنت پرو
🔹
فرشید شمشیری، عضو هیئت‌رئیسه کمیسیون تخصصی تلفن همراه و لوازم جانبی اتاق اصناف ایران، می‌گوید محدودیت اینترنت بین‌الملل، خدمات پس از فروش و تعمیرات نرم‌افزاری موبایل را با چالش جدی روبه‌رو کرده است.
🔹
به گفته او، بسیاری از تعمیرات تخصصی به دانلود فایل‌ها و آپدیت‌های حجیم نیاز دارد؛ فایل‌هایی که گاهی حجم آن‌ها به ۲۰ گیگابایت می‌رسد و بدون اینترنت پرسرعت، روند خدمات مختل می‌شود.
🔹
شمشیری با اشاره به اینترنت پرو تأکید می‌کند حجم و سطح دسترسی فعلی پاسخ کامل نیاز صنف موبایل نیست و اتاق اصناف همچنان پیگیر بهبود شرایط برای فعالان این حوزه است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/akhbarefori/653399" target="_blank">📅 17:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653398">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ur1FWWifK7S5njGd_K1ybPOFmNktWxRKlAmuaDvbwcnr9pYp0dSZfO_RvfUPFSvKT0Dd2ktyxJvZAPoy6ITWO2MqM0hFr0dh2-2aV6Jrk61rJ9j5P8CHi-9GPnyECIU3tdqq47B5cvqVSgfuwm2l0Vr1wNmmflWX8bTtsl4gbGRv8PXwOuTf4Yu8wlliQn_I7RpaMoWHklzRh6rEoc1Y-aUyAytWhRepz-LmwX512cjK30cRMiCaQCJa41K1shwGKfFZ9oiHIHw0QnbpW9pb9tmc3WACu1aL8EIQkM81ShA0j11DWz_OOE6UQupqjkcWIQoJ5A5OC3CIE7nY5fhEag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
روایت وال استریت ژورنال از «شیخ‌نشین کوچک نفتی که بر اثر جنگ ایران منزوی شده است»
🔹
کویت پس از حمله عراق در سال ۱۹۹۰ هرگز به طور کامل احیا نشد و اکنون بار دیگر در بحران فرو رفته است.
🔹
با بسته شدن تنگه هرمز و آسیب‌های ناشی از حملات پهپادی ایران، صادرات روزانه ۲ میلیون بشکه نفتی کویت متوقف شده است. این امر جهان را از حدود ۲ درصد از نیاز هر روزِ خود محروم و منبع اصلی درآمد کویت را هم قطع کرده است.
🔹
تقریباً تمام مایحتاج غذایی و آشامیدنی جمعیت ۵ میلیونی کویت اکنون باید از طریق مسیرهای زمینی عربستان سعودی با کامیون وارد شود که هزینه آن ۶ برابر بیشتر از حمل و نقل دریایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 1.73K · <a href="https://t.me/akhbarefori/653398" target="_blank">📅 17:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653397">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
کارانه پرستاران ۶ تا ۷ ماه معوقه دارد!
احمد نجاتیان، رییس سازمان نظام پرستاری کشور در
#گفتگو
با خبرفوری:
🔹
برای کارمند اداری بعد از ساعت یک عملا دورکاری وجود ندارد و این کلاه قانونی است که آقایان می‌گذارند چون نمی‌توانند بگویند ساعت کار را کم کرده‌ایم.
🔹
از آن طرف برای برخی از نیروهایی که مجبور هستند به طور شبانه روزی کار کنند، هیچ امتیازی دیده نشده است؛ دولت باید برای این موضوع فکری کند.
🔹
درحال حاضر کارانه پرستاران بین ۶ تا ۷ ماه معوقه دارد. یک پرستار متوسط در ماه ۵۰ ساعت و بیش از یک کارمند عادی کار می‌کند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/akhbarefori/653397" target="_blank">📅 16:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653396">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">♦️
نظرسنجی تکان‌دهنده در آمریکا: جنگ، ما را ناامن‌تر کرد و ایران را به بمب نزدیک‌تر!
🔹
تازه‌ترین نظرسنجی مؤسسه امور جهانی (انتهای آوریل) تصویر شگفت‌انگیزی از افکار عمومی آمریکا پس از جنگ‌های اخیر ترسیم کرده است.
🔹
بر اساس این نظرسنجی، نزدیک به نیمی از آمریکایی‌ها (۴۹ درصد) معتقدند جنگ‌های اخیر نه تنها امنیت امریکا را افزایش نداده، بلکه کشور را ناامن‌تر نیز کرده است.
🔹
در سایه این ناامنی، اکثریت (۴۳ درصد) نگران‌ترین سناریو را باور دارند؛ احتمال دستیابی ایران به سلاح هسته‌ای اکنون بیشتر از قبل شروع جنگ است. ۵۸ درصد از پاسخ‌دهندگان از نحوه مدیریت جنگ توسط دونالد ترامپ ابراز نارضایتی کرده‌اند./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.76K · <a href="https://t.me/akhbarefori/653396" target="_blank">📅 16:15 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653395">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">♦️
وزارت خارجه رژیم صهیونیستی خبر داد: کلیه فعالان ناوگان جهانی صمود از اراضی اشغالی فلسطین اخراج شدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.58K · <a href="https://t.me/akhbarefori/653395" target="_blank">📅 16:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653394">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pp1sTqR8rd06cWrqP1Ykmr7zshQs3yRRhWDKdbuWAoU02XhUSAscjHEyOdqm7ba8tvS86Cg5lpKBqxIcHBqf7PNoaGUang2Pz9IYyujXZzFMO-DLeMLKwiFhXIHYXM7WQm1WtOFnFqrF-T-6Q-_WGoFbkzirMwNJylruyuYs6EuSSOSfUCM2fYHdOrCVTeiOAGtMmJjefAUV-KC45Hz-VtSTShD_iTPkwrAnKCJihG-gVN62XPS19cGMu9I1I-IDTfvyAk_ZkaaKImN5Jf_a8EVDJ3YQRO6tOMIfQH3fYoii9m-hcngfyHnT1OU973S5zxWLLqCyWOqC4ep0wRt58w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این فراخوان کافی‌ست به پویش «نبض ماندگار» بپیوندید و با ثبت کارت اهدای عضو، سهمی در ادامه زندگی دیگران داشته باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به سرشماره ۳۴۳۲ ارسال کنید
یا به لینک زیر مراجعه کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
پس از ثبت‌نام و دریافت کارت اهدای عضو، تصویر کارت خود را برای ما ارسال کنید تا در این حرکت انسانی و ماندگار کنار هم باشیم
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/akhbarefori/653394" target="_blank">📅 16:07 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653389">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OERmXVOMVD4JZzPei-4BxKhA3quQRuXakH7VWZ0D_r6piIv-TfGfNIt_RBLueMYq1gx3lNsFLesTVBhZ_2m8OejqIEjEWeDGuMAPLrOCLr7nH_3kl9x2iwC_FQETx7z_W3witwAWfnLieqW0oEdNUeQD3k1v976WKcCsbROoHkRJrmY4XYW5E9mVy9x4QDtG9nGbrC4uRt80_Ps2pHKN-GIw9t0Lpvplw8cXZ1ofUjm2N0DVeB2Cs3TNeFnVR-uHO51JJ4LIz44O4JrQMcV8F3CDM0mH04HXhw8FMKkoU0jrz6Oh-92fokC9-y-tAw3pzvfYicZ2B5XLJ_2D76eRbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZGhUYp3mSfKlEqsOdXXq-MovUEL1L9kNgZIjOQ4tt59hdNkddtOxa1QP9WL-mtqMqJloO32eLmo7Sw9Q14Ly396uQNCKbRZvH5SJ1JTZ2dYEBdR7YB1ujuBRtbJt8_uCyGHsPlgy3GR2V1y99TxCsMEQyunn8E9xYqf80MaVEiLgvJ2WaGwie2V8QRuEO9vE5g9RvCc0bIHGIWqqZG4r1ZDbbKlVBlIcmEbA5cQ_2f3Yx-BYfIXf-KxPseFlxdLYPpU1mo16v2dYybTDR5umISOIrtJfC_H0fXQU865pkfr5CidreC3VgczlSTjXLwffngUta2RTGfKDUVJ2r1NpFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/G1zmxA2jHmDmGqtjPM5AttQVUnCINUTJGPXMrTC799xUdoYvXEXhxA0AXeQwgs-3SG9XpRYPWxQQjY1NyDXZwostz8ctIYTEgBj8wbYC9QAQl8ACFkYcB1g2v60gJX2MvL6LDryKRS_GtmFjGGxIwlMNipwODD0SfVIJN9TS26aeL5ihJhgzam_l4vSqWsd5eG5pLwjVSROOX4lxbUUNvQXJsLrlKH1T1_TDdJNRYYdCFi-pLc1UpryQfTKNTjYFfaJbg3VhT9Qc1br_KKCNRvkOZDoAOqojM2iEdGzZyk2hVwgG8DTiAWemd0u8Z_2RuZ3od9fIEe_QMrkDJ-_mOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n6oWlqoRVj_zYtqCv1mRrGq350kmrZx7yQEwA10MtaVoUi4dCoZkzayc_lWVjFW47ezhUQSJoSqirpWOHrrG25UZVjhzTgE3z90GAHh1Y2c0h4aCtDRjXu6XCL2fi-Ya2OxDtP0AbKmS5tuAR71xGuAc6iEdfpAsgTqeVoHZjYn0YnKQNCADwGkJbMRoSMb4XESafgymsmXAOCgyKZlD7T339EWTXGnh9F_JMsTlnlpvIct9eF-B8PLpB2LSYkpQq2ztXvx1q357aGMw-CyYeJtKtyfb0arZS5l90W3hyBwwr2ihA5Vzy3YXW8IosbEU5UTCeDxqUXa5ymoBsDeSFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/URvJPe1xaNf1yRcqbXaFpDMAY_YFouGa-BIcIkTPAnfb3CEpsRU83I61QyMA6n_Fs7_wnptNepU3ornRjxd_-fCMaoO-qE6-_czNpCFFsgqq3nNv_5_S58OOCuWXNYXfpawta8rM_3HtY86KrgeL5cGB8oelN9P6W9XkoZ2SnkMKYssoVrfLJ3KWjTfHZBERmXJABWkXIptLeGFXCevUSwrhyCgYFPQENiQaLoT5RNj_GkLbprUVL1mgKgpR4Wc5hokcHfcNXRBelVTnXdEbi0rDdxeiBdQIH92KmUHFsalt7enPchWfrPG2pNJOy9CZ0Ex6NuwqKAnFOFJqw86yJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیدار فرمانده کل ارتش با رئیس‌جمهور
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/akhbarefori/653389" target="_blank">📅 16:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653388">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7fee370e6.mp4?token=E19xl6r2c9jnW3krGIWKzW4Hb0Cx8SJVVVRx3hF3W3OBzA-cbU_HkNWUX0KGumdYASTNwYnhNucD_92Rhdeuq7MrbMydsw248nFN9ejJMXUjt28c3hwjYte-RIOjs14kMtcqNbxzu1ToNLG2p6Svp6QtHF4bmf6vJhPLLc0lGrgr636emZHFFOxPtJa6570cJjFvXP9TSQANlJXWJj_aiOW71yHyrm6gUDZp4bNsK2MlCdALq4EVXFfppf9JbF2EBB8imz5pHhWnlsJ09Bbdw3w-LMK0AuELZVz8tATijntkN_9ZRKqZJpkDe0rOENWx10zv_gD3QxVlUAJec34rLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
۶۰ درصد زایمان ها در سال گذشته سزارین بوده و تنها ۴۰ درصد طبیعی!
🔹
اما این عدد تنها عدد شگفت‌آور خبری نیست؛ در این بسته خبر رسیده که قرار است به زوج‌ها تسهیلات خرید جهیزیه داده شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 3.79K · <a href="https://t.me/akhbarefori/653388" target="_blank">📅 15:53 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653387">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M7Bvd18uO-tfOXp2pMwoyeWsVlb_HgFwtvAULHZL228gIa7xw__DvN_XYKFv2U4oi9RtJl0xUBuT7pSMUOLbI7_YHJU7iS2znRff937TRFDimUXdaneG9WLwKCHEBkFCh-MimS7wAaAgkzG5Ba3wSN6W4ERVpEBIewdZTXqv8fTYeeMaQsIKWFvWHQs-oks3kp9duAry2hbBtR9x0a5Su9X6ymdRiqNvyTjI27mPjrt_nLZk1nyUAgxcBWFiWP2RVRzVW8RCuD4yrStP_Ryd3wbr642Enb5DfkUz9N9Fb1c8N6Wk9M3Jns1XsHX34Bgdsq-X_JVkNy-Ug8XzE2_Nww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بقائی: اروپا از تجربه نازیسم عبرت بگیرد و از بی‌عملی مقابل رژیم اسرائیل دست بردارد
🔹
سخنگو وزارت خارجه: تصاویر وزیر تندروی رژیم اسرائیل در بندر اشدود که شخصا فعالان دستبندزده کاروان بشردوستانه «کمک به غزه» را تحقیر می‌کند، عمیقا تکان‌دهنده است.
🔹
این تصاویر، خاطره‌های تلخ تاریخی را زنده می‌کند؛ زمانی که رژیم نازی، متعاقب بهره‌مندی طولانی‌مدت از مصونیت مطلق در برابر جنایاتش، خود را استثنایی، معاف از هرگونه پاسخگویی و فراتر از قانون دید.
🔹
اگر غرب همچنان شکاف بین ارزش‌های ادعای‌اش و رفتارهای عملی‌اش را عمیق‌تر کند، باید منتظر تکرار درس‌های بی‌رحمانه تاریخ باشد
🔹
اعطای مصونیت بی‌پایان و سکوت در قبال قلدری و قانون‌شکنی، هرگز موجب تعدیل این رفتارها نخواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/akhbarefori/653387" target="_blank">📅 15:50 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653386">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">♦️
تقدیر وزیر اقتصاد از عملکرد منطقه آزاد کیش در جنگ رمضان
🔹
در ایام پس از شروع جنگ تحمیلی جاری، با وجود شرایط ویژه جغرافیایی جزیره کیش، محدودیت‌های پروازی و آسیب‌دیدگی بخش‌هایی از بندر تجاری کیش و بندر چارک، سازمان منطقه آزاد کیش با اجرای تمهیدات عملیاتی، فرآیند تأمین و توزیع کالاهای مورد نیاز را مدیریت و روند قانونی خروج خودروها را تسهیل کرد که منجر به آرامش عمومی در کیش شد.
🔹
محمد کبیری، مدیرعامل سازمان منطقه آزاد کیش، در سفر به تهران و در جریان پیگیری موضوعات اقتصادی جزیره با مقامات ارشد وزارت امور اقتصادی و دارایی و دولت، گزارشی از نحوه خدمات‌رسانی، اقدامات انجام‌شده و نیازهای پشتیبانی جزیره ارائه کرد که این گزارش با قدردانی وزیر اقتصاد از عملکرد سازمان منطقه آزاد کیش همراه شد.
🔹
مدنی‌زاده، وزیر اقتصاد ضمن تقدیر از عملکرد منطقه آزاد کیش گفت: تجربه مدیریتی سازمان منطقه آزاد کیش در این دوره نشانه‌ای از ظرفیت اجرایی مناطق آزاد در مواجهه با شرایط پیچیده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.53K · <a href="https://t.me/akhbarefori/653386" target="_blank">📅 15:47 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653385">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VjhsppqWCx_7RGkrnOQjSK5HL6iONbOeZU-daP4B8rHY2r1xdv5x9P1beOSOzp67iPEsG-Ti2zgd2dcOC9t1t6yHd9ZBiOyGPTs_kEYWY2KnStPKaXV0NDAneRL1zZns7fDtGip-QwaU1g-J-DiGQR8CrcQ0HhYEYz7voroaSbNLxhJWiR8UEcCHgQ8uAkxU9l9RclGFzY5S8Zcg70jY3SFE8KgTAD-o8z-Ud_D877nxIT5EAcheVd0Uj9DfgpcjMv-AqNmnFg4wxhVHKmtYOydmhI0ud_AVtPvPvNPJL8D7fUAyINK-CvKPavWskGxtSqwc162uRiC6eBGaq4HMTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادامه انتقاد ها به خط سفید و vpn فروشی در مجازی؛ یک فعال رسانه ای از فشار بر کسب و کار هایی که برای بقای خود از اینترنت پرو استفاده می‌کنند انتقاد کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.92K · <a href="https://t.me/akhbarefori/653385" target="_blank">📅 15:40 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653384">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d438d2ebbe.mp4?token=mWUxUjoL3EAPN6u1xG5MGAxw4mIaDm1mVG1LRDTTTHijhRYoBfMoGoU8F5MWtjSNaWznptJqwU8JYstPJg9iYSwzUYuPR55t_1GIGbdzXOpp3PVTxhUHLDGStJouc9z6wruOr9ToUZfMhc4XEzl9pxaZSRVLPnNAXzOhwpC7Bu7253pp2pQXBr1Y83oKDxNsJAQdN2WjL_pEIG5ZuI8r1BP4fr4Z1XJWhLMPW-bqQHGzlyzJDEke9N7AfSOMYmh65so98xbBgXR8qKAfXELwTIB755qFc9wFWioV4BqDyw76pT1iRAgmz5VpO219OzYuitZSeQ3nh9AF6bDqBCQVig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
فراخوان خبرفوری برای روز اهدای عضو؛ «نبض ماندگار»
🔹
همراهان عزیز خبرفوری، برای شرکت در این پویش کافی‌ست با ثبت کارت اهدای عضو، قهرمان زندگی خود و دیگران باشید.
🔹
برای شرکت در این پویش:
عدد ۱۲۰ را به ۳۴۳۲ ارسال کنید.
یا از طریق لینک زیر ثبت‌نام کنید:
https://ehdacenter.ir/api/gateway?code=120
🔹
بعد از دریافت کارت، تصویر آن را برای ما بفرستید
👇
#نبض_ماندگار
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 3.87K · <a href="https://t.me/akhbarefori/653384" target="_blank">📅 15:39 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653383">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/irQRqkVQ82ILUd18-EDi_zaXkgK91eRy0nfiGMtEO9sOwq45ovroNWm8Ks1ZJFyRC-90eNUlzsaGvedI3K6kPD9GNGGl-EYQr_DJhgFflOHGF31LSKCAOKnHL1eQoJfr9o-hOd1wW9JaKPyUJxKg0CVRIbRDsmtQX26MiFpcjqibBO_WpkhReCyhjT2suiS9wKGgSroqGVgXkBWf-Jmdamwuyfb5j6n8UH6ytY7F_Boa5WxnRm6dtbItXhaOonKiYv6j38zhRMZSOHCkiH7UnImAb7HN-v7vmdgpTpTH2qV09gJgn37AvtjqgiMheHz3Z1kg_xSgzSYQwQIOqemCdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پزشکیان: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت/ دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند
🔹
رئیس‌جمهور، در دیدار با فرمانده کل ارتش جمهوری اسلامی ایران : نیروهای مسلح، به‌ویژه ارتش مؤمن، مردمی و انقلابی، در جریان تحولات و تهدیدات اخیر با آمادگی عملیاتی بالا، اشراف اطلاعاتی، انسجام فرماندهی و توان رزمی مؤثر، اقتدار دفاعی کشور را به نمایش گذاشتند و اجازه ندادند دشمنان به اهداف شوم خود علیه ملت ایران دست یابند.
🔹
دولت با تمام ظرفیت در کنار نیروهای مسلح قرار دارد و از برنامه‌های راهبردی ارتقای توان دفاعی، پشتیبانی لجستیکی، نوسازی تجهیزات، تقویت زیرساخت‌های عملیاتی و افزایش توان بازدارندگی کشور حمایت خواهد کرد.
🔹
امیر سرلشکر حاتمی: ارتش جمهوری اسلامی ایران با بهره‌گیری از تجربیات میدانی، تقویت آمادگی عملیاتی، ارتقای هماهنگی میان نیروها و به‌روزرسانی ظرفیت‌های رزمی و پشتیبانی، آمادگی کامل دارد تا در برابر هرگونه تهدید، تجاوز یا اقدام ماجراجویانه علیه کشور، پاسخی قاطع، پشیمان‌کننده و درخور اقتدار جمهوری اسلامی ایران ارائه کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/akhbarefori/653383" target="_blank">📅 15:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653382">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">♦️
رییس جمهور در دیدار با فرمانده کل ارتش: ارتش با آمادگی عملیاتی بالا اقتدار دفاعی کشور را به نمایش گذاشت
🔹
انسجام ملی و اقتدار نیروهای مسلح مهم‌ترین پشتوانه امنیت کشور است.
🔹
دولت با تمام ظرفیت از تقویت نیروهای مسلح حمایت می‌کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/akhbarefori/653382" target="_blank">📅 15:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653381">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07ada4d4a.mp4?token=oP70LR-5eBMe_sXA3CCpVKCyJ5c3_6DOEKIVDivFT1Vm42gZHlL-gu0vH2tA72yfikiboNZyMOvb2w95igJrkHXcE0A0x0f42KMMSbyfYe9saolFJpOfh-YBfMC6kniX23RBRre_gDTlw7NAtR6vYC1lIiy_yk7YhTlPlfjRrqasGCxayIY4cC4JZt12OLYvYe76HWNXVQrKnvifQlQP5xiodR-dbLqW6gmiowbqDcCsWJB1hGF-IzMlxqPisxNfNfUVxJ4oI4V97-mRkAXQMMPSimENUDkR-xzIjZFMxwyL63z7azd4pI52YaKy-yh4-xye30BcLKB50FGNImkFFA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مخبر: رئیس‌جمهور و وزرای دولت برای حل مشکلات معیشتی مردم بی‌وقفه تلاش می‌کنند
🔹
مشاور رهبر انقلاب در دیدار تولیدکنندگان و فعالان دام و طیور: همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد.
🔹
دشمن آمریکایی‌صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می‌دانیم این بخش جنگ برعهدۀ تولیدکنندگان در سنگر امنیت غذایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/akhbarefori/653381" target="_blank">📅 15:22 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653380">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k0OGVdfhWu8Nh3p7D3YYtlmlXhKI5-BLtOWK6rsgnefMh-XGqhJuv8sPrMA9dSVzXj16b9b7lBXoW13dIUW_lqYokfY_j4p3453lJHs5E69L0vw9l-dHH0pzT3jazP_LU6YxY0AiNaU_kpnuYUBU1X4GYEvonkaeivGq2Nik2Ha0Hd9QFTlMsylNDVShXOpxdwuI1t50BXD031GT3y1guI0rjSNOANPYf_4sf3ePRzHMDzCzcUYQLrKT6YlLgTkPk556Mw6X8FAxyBuKuTcP8O9moLICfdCw63VaXrBbgK3rQGJvP-trHfOtHH8ravY5CR6Ph1NAtUzDCX1Cg0yRKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سهمیه ۶۰ لیتری بنزین خرداد، بامداد جمعه شارژ می‌شود
🔹
۶۰ لیتر سهمیه بنزین خرداد ۱۴۰۵ خودروهای شخصی بدون هیچ‌گونه تغییری بامداد جمعه (یکم خرداد) در کارت‌های هوشمند سوخت شخصی شارژ می‌شود.
🔹
همچنین سهمیه سوخت خودروهای عمومی و خدماتی مطابق جدول سهمیه طرح مدیریت مصرف سوخت شارژ می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.15K · <a href="https://t.me/akhbarefori/653380" target="_blank">📅 15:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653372">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vb07DoXqzejont6LQiC-XOeCBsDfBOEScKxPXQxmpLjc-zJ37xM_rw8dvT6_CPX14iEAtZrbCva8nAllf9gISX4bk49e3ObjTAf-_OLFWNLGRZWF_toxX-NcPRGuPs8k4Ur9yKGsE8IsLI6uBALKnDCBCSP3jeWAv7vf61BbzyKJ0lILC9tqwueEXWgi9_q5uE9Agx29AQfawzpt2BiouAwX-0hufUYgTZ7RZCya1v8O_VmfJ-tFJXWAp_4TwSS4f53bcZY1ePUu0Xr9cjcV_sF139kXjX4c89-QkrQ9_OgkXuJR-oEIW5KmPidz_OtJVyfuqJeLae5T3dyqM0mvxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tSDNPT8N8J_uvTd4uajrrzrK0qtoLaSy3JyqQPqb1XlGCG2clUHe7O0bHkatHl1N2sz3nVb6C8wNx05DsF-twsTpPTwNTV7YNgufFaVaoqeNFwSq0Q6a1iyJbDwD2BB4mH9tnuCcUVLXT1yiOsANHHcss7-cizknmcof4HBrtU6MAjglnWKnZCreJPOm2t2oE1p_ahq1WXUrREGBsDAC_mmYwyp_ozsnzjv9Tgnud1Ak_ScqE0aD7ureS7eSs6EDrevQ68OPcs4OlMSTLvLRb07aklwuSyJM5t_xv4DZawNChTcAXN0VWNIFsIjy_4_HAWl2SaxeunfJ47RGADXYLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pOk7p-VuEleSwmCERz50FYUj3eaiIuD4VpcLY-5o436e8DEdChNckkXblgO4XwxDbGpwSlLKbK7wjaRZIbMio7tBEhaH8LiItMW9ZJKgKXmQCteZvo9Ewz94KKZVYhIZZl0_3F__pJQHKSV_ojBG19Y6y-uSo9d5ct9fQH7Fj_894X3RXwB3bAFMFtkzTwcITpnG4QPgGvAXIc0fhNAAZZaE9cTCjgVPf7IDyi-I7zEEnFc_xPhvGKEKpDs6yF4xoYXp3mwl-Gj9Ch9W5gBy9FDLO0ulwd1KrS4jrl-GEveI0A112s7C4mhG93Di2WrbF0XRdFeTdgklrywq_JdV0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FobAF7CEPNumFtUgljfNUanYm4pBs6-apf265aTcWNUdaKI61pzKL8i5xzI7ZLQlU1drIT1x6M9ST8_uIqjtCFilQ_j4rganF2cEfT2opbtOIIrpwKHCFtrZHgIveU1D6fDUyuPK63NKYWgmxQw65O9S0F5J0sglhn_FwiIq_LylYE2Spn0MffLMQlrT5yvZDuvMIv5MlPD2gcx8G5VvvHXl9diZZEY_4V0WfqLNYYwOYHtG52Bw41olDpi083e7ztzeVMXTuqUtNx4csUqiRSzYhpF6LGq2_3_IGtaM4UvrVpv-ZxN4VVvm32DCkn3VRpwFwG4BORlA-F9mPIO-xA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ny0q37-MEedq52riTyr6LsqCJ0joCj6kwJxSDzYpp9ts1ohQOgzbeAeJxO9BBVDcCWuFbGM9ZOesg5TeaTh2AP6XlP79zu63lKsKzVYkVqsjRmLSzKiZ0BenlRyQh6IlxEkSYRgAcnXLRremEBN5lj-A7xmPZGBeQzb4LsCoEYDq93lcHU4z6wNAp5mbiP7U6Qg8O_QNSDL77HF8vZGl81EidDS3BuAONkKjyVV0L1bg0DMDXX1P-zt6NqgtsWrtHxnWN0un04S2Zk6Qq03GpThOzqz4KhIWYfMaX8Qi2IpDYERH0Vc7D4z7aAODeyggsg8LhO_8VLEUyBU2ZutyDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nxqOvcR9X0Vn9e92gtcp4Iog_QRwY_byT3vHu48OjiDeLwrd7TVRRUomydg2wi2Q2XoTq47N31JBk6PvH9IWxJSNZYfYseBCDyzQiZCKYHG2GDNgKdS6kflZ7Ge5UQEOkiJ7PTh0AdhdZfZBsjWGS76DK7GE4W8FeasYQdGMYchUsXHpQKfSfe_4zkiGeakalDRORqZF62p3Rn8A6rEeZh6HOo15paQE-xh1dOLXHMDk3t_WlCcg124JbxybtYFPN6CNCaEYTqZaETj29S_JKUWCoQhUCVcpYAGWnL0uyhB2teBXekr0FD5pIDUhU6HCkgjaU-UUT6ITwSEDClxpWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AlV38GdwhC_lHOxzAjOHg_zmnqYvZzqjg8zEd56CX0SuRYtced4W_hUIGOT0GWLmlm9M2KjhbBMHbllmTxO3nrap9ycElYntGlQUQ1h-n7eN8MYQsYSpZ6eU0BHn-7n-WIphAngQZXJzyDc2gB6UCvAxuw5cgJXHfMh-DnZyRGtXOrPDIQoJu5bNqP-8XxSIG4sLSeMpjhLvza78_hIzF2SoI-52l-W2rd84m6-vBbft_4TirWYNLg-yA5TO1Y_AfnYv08MgSIROOJmex9FSp7EF3nYTCBuV0F-AZfm2MKvoC6lHPYpQyklnEmOds39rTrGgfQOddnW-hTtwS_4fmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KzFOgh09nI0lwTvz6sDiiEzLQIRe1GwABhjZGpzuJiF67uey-Lk_GTAHBVdlsU7i9vqWduwReb1T2qCxlsNxTjyxIhICvfG1Rz1pjBUPQ1vrQafmsZUPnV5CqLjB9ingW0o_lOGQVkW91X9B8fvSktbMuxwlAjH0YnqpEl_cU2beFilL1PV6w0lVEK34e3w9y41XPHZm3g68QoviFCwKTamNEQmlg2RfcHiACTq4K_3n0eBSaX2Ry7LpSEdToKx8Ez2hsedbSFXdFWzQIieuyLUg3T_aBHYxmh8USk8lNfxEaQq3ATB14t3uM7oTllk0dOs4D5BfJhibL7c6IaHziw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ویدئومپینگ شب گذشته میدان آزادی به مناسبت هفته جمعیت و همزمان با پویش «جان ایران»
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.19K · <a href="https://t.me/akhbarefori/653372" target="_blank">📅 15:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653371">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/229a942a29.mp4?token=GRawaUcqSMSqdQGw31_tvZrv-5OTtIt4BrboKkG4QyS0mQ9KQXc5QEajqNdFntInmnrSmX4g5ZGWw4LmiyhL_xMKRxkMrFj0j35bMNETg5I2Y59Eu8jsckn7WFIdliOQU2i5FSBPI38eyhc2AupL2zH2ZYz3wp9Y5-6Ol-sofavjT4xWC_Oh9Sl1dSZaCh9qsF3lsN70CHtzsB-c4N-E2us0AfKw0ClOndktOOmcEns-R_vpQB6tSVHbjY7I4tIgB3UNURWR3Alg2Ng85D-1DcuAz00Qdc6h_qRwi4ijq_XwtZO6zraO6Y6xO2zgRVoHJAfVZTspG9j2rz2qblqvUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/229a942a29.mp4?token=GRawaUcqSMSqdQGw31_tvZrv-5OTtIt4BrboKkG4QyS0mQ9KQXc5QEajqNdFntInmnrSmX4g5ZGWw4LmiyhL_xMKRxkMrFj0j35bMNETg5I2Y59Eu8jsckn7WFIdliOQU2i5FSBPI38eyhc2AupL2zH2ZYz3wp9Y5-6Ol-sofavjT4xWC_Oh9Sl1dSZaCh9qsF3lsN70CHtzsB-c4N-E2us0AfKw0ClOndktOOmcEns-R_vpQB6tSVHbjY7I4tIgB3UNURWR3Alg2Ng85D-1DcuAz00Qdc6h_qRwi4ijq_XwtZO6zraO6Y6xO2zgRVoHJAfVZTspG9j2rz2qblqvUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
بازگشت بیش از ۹۰۰۰ واحد راکد به چرخه تولید با نهضت احیای صنایع در دولت شهید رئیسی
🔹
با راه‌اندازی نهضت احیای واحدهای صنعتی در دولت رئیس‌جمهور شهید، بیش از ۹۰۰۰ کارگاه و کارخانه راکد و نیمه‌تعطیل به چرخه تولید بازگشتند.
🔹
احیای واحدهای تولیدی راکد و اشتغال کارگران، یکی از دغدغه‌های اصلی شهید رئیسی تا آخرین روزهای خدمت بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.55K · <a href="https://t.me/akhbarefori/653371" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653366">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/U33gwu0crTHGXdOJJ5tpEk2RwC6s6lYZzYZA_EPIIc7SkAUqo8p2AmV2OzWsfEBZCK-KiULGdzEi9TlH0y3bo-7lOCulyyu9hX1I9rYoV7YcLXziP-jF56eFYdLJ8V3P68Njs0s1P-SPF8Yq4hd4NLWKIviVh_aTdG3lmWBOEd6G63dUYqBLRZOxzfdqqhmJKEU7pStSIHWw4eBcdmB_k_pct2GIT9JBTX_3jIysP3RoH0qVinZJxJCIm2od1FbvBPpi_Lhqr-6A_nUn36RDOq_XYa3KxVh-7-jsBw8-jSxDnl63syTithTA0Xk7N_1iix1gQmsvlthDuCy4Mrll3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TqIqhxiihvEDy7XkczHxnqS6bbC1-Zh4bOUAGJvghaEnRitNXi4FGsYmAUKT6ztteR2fwFCJpD842oXYOLY8dTVBULXnjlkdzTpGevXZgXuY_Ovma2d5ZFRpnPmtEa8VSVCE7-zupsgOEuadfcCb1nA_aItGg350E9347v2p9m5Fi5z2Dh8VpLJjimAuZ7QQo5Agll1cwCQgyAPa33dzw_XQCMVDSxXYlQGV_HJUWpNZbE5ojSd0TTWPCuQ2DVD8tfN1XhPtGg2XuEzAn_WsMnQ8EYMgUlBQ5KOk3W2zD85YwS003Nv-SyhE21mENxobs5N7AsGVGxW5aKHwFvyhzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TfAELnSbz6pjWFyT3AoTkaZ9XpuZB-RLcGIpWW5CuQ_NFiDzGXiwcIoWnmUM0qJ2IB19jVI9UECr4xwyxuJ9PsHxjto4LXsbukCwnuujD_5ifAENYS5MNC1fXKEV3Prjwg5TldW5zhctpT62-1vAOh0wWMkdfecocBxD7EqlkPsKdt21pnda6zCEoUXf16oUxySjvsHxps45dvK1scoZLCzJSIUIMDWejcqaYS6B783RzxI_ZvLA8KEZ9g-y4Iq8AWKcHp_JJs4YZmERuw2fPj0QYizm0o18fBvurHXzU1ECPbVd9rl4fJX0ME-MQQudap4gxW6ay7IthPOozME2tQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qaSFXPmuVnudVJpCJnLmmr4ZkxfCSnpU724A1B2sw0OFUJ8_NHMi_h-OdddGDniWFt6SEWLyWaL5lAoM5GXO8m2wdM6mRpLYR9hublVqxSY-dyHcwFvF7AGR2t3OIPtI6M23jnxwQHoZ9yEreZ7BQpc_fGWeGNtQfBVcQHqwI1farzJBhAqWk-wB8TbtevW_h-Fk-XLZaEjCK5n8mez2KFIJm5jwONKfklqUkWX0CLFqOYMl4JC77oHRq5e26aZXoXkvijg7zA8dwv8j6x-Alwlvb28zp_1EU6b8b7vVMgYoPHhLvPIQCeVgL-HJp93zJ1nF5StrNk_2LJU1yM2KdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKsUgVQMgNu41v14XJkubn_sCLHOWHg1oakQ_4dVbTyAr3Y07wMwWHD3QZD2AFkhzpBt3cB7pF2uLLmKVJ78Q0nG0qRuRt09cppgh2SBKV9lPAkx19aufRj1GtaSZmZPqyiAjyoUX8swXhW95WE26N7rYqPDl483RySror8Dh1eGH3b2YitblLU7-AyQhBCBHcGjt9OsUTle9jSKSu1xFAUB4epnDpvNaxSiyEymmyrmSYPq5ZIXD-X2lIT_j9ioJCLhV1rqdkKFL3-MoQmsWoC9NafQabE4mbrvutlKAnfzJ2cHncuAeu6NPRjb2vH2L8ssZwQ1R9bxW7p34YTIHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
‌‌
پویش مردمی نه به پلاستیک
🔹
مخاطبان عزیز خبرفوری،  همراهی و مشارکت شما در این پویش، می‌تواند به کاهش آلودگی‌های پلاستیکی و حفاظت بهتر از طبیعت کمک کند.
شماهم به این پویش بپیوندید
👇
#نه_به_پلاستیک
@na_be_pelastic
@Alo_fori</div>
<div class="tg-footer">👁️ 4.22K · <a href="https://t.me/akhbarefori/653366" target="_blank">📅 15:06 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653365">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
عبدالرضا داوری: احمدی‌نژاد ممکن است گزینه آمریکا و اسرائیل باشد!
عبدالرضا داوری، مشاور پیشین محمود احمدی‌نژاد در
#گفتگو
با خبرفوری:
🔹
به نظرم نیویورک تایمز بد نوشته است و احمدی‌نژاد در حصر نبودند بلکه منظور آن، تور حفاظت بوده است و وقتی سپاه برای شخصیت‌ها تیم حفاظت می‌گذارد طبیعتاً، اطلاعات ترددها و ارتباطات آن‌ها را دارد.
🔹
وقتی محافظان احمدی‌نژاد را مورد هدف قرار می‌دهند، یعنی می‌خواهند او را از تور حفاظت خارج کنند. احمدی‌نژاد می‌تواند گزینه خارج از کشور یعنی آمریکا و اسرائیل باشد و این امکان وجود دارد.
🔹
این مطلبی که نیویورک تایمز نوشته است می‌تواند یک سناریو غیر واقعی نباشد. هیچ اطلاعی از شرایط فعلی احمدی‌نژاد ندارم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/akhbarefori/653365" target="_blank">📅 15:00 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653364">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dH3hUmGfkFQV7zOuyXakovAKapFv3rZHBbe1PEHKJaQsaq5RzrXEMZLBOyILDgqA6bLhO9rHv_rSyOcjbMkxApmbfGlrZsG3efJ0R4PJ0G54QBunAJ8f8GmzuaYdAF9yOap49e03BZLKVRNmQR3sSqSB3Qq8_fvXpM7M30c3Zikfoq0XymRNwIXtBujYuaBhbQCCZLMCDvdU8NCzsKJ6iOE11KlUWddtiknmtg1ZdYJOz2uQ3fgqS2Xg_FUywh_VxHjvsh2jpWJzkoRCZRhyA8Y_IvdoFAi4VZTug9GrE1nBrFH6TsF99SgVL4UTdgy5B0XqErNaKqDwbR3-OgLG4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مخبر: ظرفیت‌های کشور از مشکلاتش به مراتب بیشتر است
🔹
مشاور مقام معظم رهبری در جلسه با فعالان عرصه امنیت: دشمن به ناکامی نظامی رسیده؛ اکنون تولیدکنندگان باید با همت خود او را در عرصه اقتصادی نیز به استیصال برسانند.
🔹
جنگ اثرات اقتصادی سختی دارد؛ حتی یک مصاحبه می‌تواند شاخص‌ها را جابه‌جا کند. فشار کنونی بر مردم را باید در نظر داشت اما امکان رفع مشکلات طبعا وجود دارد و به همین دلیل مقام معظم رهبری در پیام آخر خود بر رسیدگی و توجه به معیشت مردم تأکید کردند که نیازمند تلاش مضاعف است و خوب می دانیم ظرفیت های کشور از مشکلاتش به مراتب بیشتر بوده و خواهد بود.
🔹
همه باید به دولت کمک کنیم تا با اقدامات لازم، گشایش‌های بزرگی انجام پذیرد. دشمن آمریکایی-صهیونیستی امیدش به فشار اقتصادی و تمام شدن تاب‌آوری مردم است و خوب می دانیم این بخش جنگ برعهده شما تولیدکنندگان در سنگر امنیت غذایی است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/akhbarefori/653364" target="_blank">📅 14:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653363">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvbTikaLoS1x_nkyjiV2l0OiwGA69SP5CEk2FwqgsAZkEKjtJl5_YAom5Mil9gHaoTzTKvdS4J0Lm3HyXSiqznOXNzpy8HFUjraNHPSslPTUxoN0vLvT_fVWA_rGUiGAoSiMQtG1dgrYhl6zjT7UnZ80N5WDPMuyD_kXQV4xxwxA734MS30c0zzn7DXcjLsZarGYJGu-R6tGu71L-ZERjk7jV4MEM8JlRYVgWVbvJ-HQaIsHIFQoE_9ROYGiEPicmsJpOflpwcqapMnJGgxu1iGUhmyZ17-s532DgekMAMz8fEy5QVYsRALFPxRPCY0_oA-IuWja3xxc-sQPaxUTJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا دشمن پتروشیمی را هدف قرار داد؟
🔹
صنعت پتروشیمی ایران با دو بال «ارزآوری» و «تأمین خوراک داخلی» به‌ عنوان یکی از حیاتی‌ترین ارکان اقتصاد ملی شناخته می‌شود.
🔹
این صنعت با صادرات ۲۹.۲ میلیون تن محصول (معادل ۳۹ درصد کل تولید) به ارزش ۱۳ میلیارد دلار، موفق به کسب ۲۷ درصد از کل صادرات غیرنفتی کشور شده است.
🔹
این یعنی از هر چهار دلار صادراتی غیرنفتی ایران، بیش از یک دلار مستقیماً از خروجی مجتمع‌های پتروشیمی تأمین می‌شود.
🔹
در سوی دیگر میدان، ۶۱ درصد باقی‌مانده تولیدات این صنعت به‌عنوان خوراک و مواد اولیه به چرخه صنایع داخلی تزریق می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/akhbarefori/653363" target="_blank">📅 14:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653362">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d61faaa0fd.mp4?token=XzUXBnnLJ7jwvxTZ0A7K4PmyvzVUs9HiTiJP5Zr4q5NFmXbO5XlTIAroiHLKCAwu6jxHG96izb3mdJ8Oa528UlOD6iIvIdP_WdHgvVSN4mzGG6sGo_lYQt114PWMQGWg_9Jc33LwKZebmPazvhhV9_5cD5WpTkUGXo5F3m_628Sa8lw0UhYCDWx_lkl2-BfHVbCKNgXr4mUHAps70At3adgzGu_LziMwY60YFlIWNAlmQBbq-89R10hSjhJ3TLQxK-DfzM-wlrVgEEsW88dh5u438DKbq0Zcv_opoTZRfRlK-OGDyPpkBEln_MruLFIi49o14AKCioU_dqXjLopM6ZPpYo2hix5sJRvF2R0fkXl2jbk8P88qqoj6jajEVhgOFrfO8OPL6Dz_w1Kbsd787aL1f0aktqr4gVBRCeA-nesIj_r4V-S-mXM-9KSH2JtJzBrDM-ArzN1V6On4tTd8iF2clJwYiV5em5oitn0Bm_BgGSydCKEe9duaqaBbMsxw_ijGtSwrpom6_etMOAAr_2knzkyth3flEcVRwYm-2BmpiNhvUNByLKMOhAwbF-t9gxmuzh7bsYrXfvZgct1NPU9KkfkwKSh5nAXnY3Oe14qGLvv3TlAzdvJQI7mCjENMD9dwEXVWx22JN-i4JloxufjZqmgnb-gbHUUgUnSSWxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d61faaa0fd.mp4?token=XzUXBnnLJ7jwvxTZ0A7K4PmyvzVUs9HiTiJP5Zr4q5NFmXbO5XlTIAroiHLKCAwu6jxHG96izb3mdJ8Oa528UlOD6iIvIdP_WdHgvVSN4mzGG6sGo_lYQt114PWMQGWg_9Jc33LwKZebmPazvhhV9_5cD5WpTkUGXo5F3m_628Sa8lw0UhYCDWx_lkl2-BfHVbCKNgXr4mUHAps70At3adgzGu_LziMwY60YFlIWNAlmQBbq-89R10hSjhJ3TLQxK-DfzM-wlrVgEEsW88dh5u438DKbq0Zcv_opoTZRfRlK-OGDyPpkBEln_MruLFIi49o14AKCioU_dqXjLopM6ZPpYo2hix5sJRvF2R0fkXl2jbk8P88qqoj6jajEVhgOFrfO8OPL6Dz_w1Kbsd787aL1f0aktqr4gVBRCeA-nesIj_r4V-S-mXM-9KSH2JtJzBrDM-ArzN1V6On4tTd8iF2clJwYiV5em5oitn0Bm_BgGSydCKEe9duaqaBbMsxw_ijGtSwrpom6_etMOAAr_2knzkyth3flEcVRwYm-2BmpiNhvUNByLKMOhAwbF-t9gxmuzh7bsYrXfvZgct1NPU9KkfkwKSh5nAXnY3Oe14qGLvv3TlAzdvJQI7mCjENMD9dwEXVWx22JN-i4JloxufjZqmgnb-gbHUUgUnSSWxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
شکار فرماندهان اسرائیلی یکی پس از دیگری در لبنان
🔹
یگان اطلاعاتی حزب‌الله با رصد دقیق تحرکات ارتش اشغالگر، راه را برای پهپادهای مرگبار مقاومت باز کرده تا فرماندهان میدانی دشمن را یکی پس از دیگری هدف قرار دهد. از فرمانده تیپ ۳۰۰ در شومیرا گرفته تا فرمانده تیپ ۴۰۱ که هنوز در کماست.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.46K · <a href="https://t.me/akhbarefori/653362" target="_blank">📅 14:29 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653361">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r51xX2dMvZYvQ-xkQ5yTyGSqGstuBRmzZlF4EnG7i3N06vfkVNDB6dalUu4cniDasq_f5BOspmkrlA6K9F1yY6ceWXJMJdRhrVcsS9n5oMMlcgSjP16Z3B4xckW6GsUCtr9OgestNPCeTsSlXZhrHbuvsBiTar0ypBIlWzt-5t3mGPztyj_SDuSyGFgCq2kD0BE_UEmygo9ppM25gD94qczSWnDx8srg4axtBFXTVPTtM7vFITI96FmdAHfCIrgB10wxAiLKi3ogTYB-s3dbQz1Miu8zjJZ3fyd1FLxEoe0rMdWkcb-kVKVLbz4u7ktGIT3mjTXJ-9RN9MvVoPAaHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاعیه جدید پویش ملی جانفدا: لطفا با توجه با توانمندی های خود و برای بهره مندی و نقش آفرینی موثر و متناسب با کارها و نیازهای مهم کشور در دوره جنگ و پساجنگ، جهت تکمیل اطلاعات ثبت نام خود با ارسال عدد ۲ به سامانه ۳۰۰۰۱۱۵۵ اقدام نمایید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.34K · <a href="https://t.me/akhbarefori/653361" target="_blank">📅 14:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653360">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
مهلت دو ماهه مجلس به بانک‌ها برای تعیین تکلیف تسهیلات مسکن
🔹
رئیس کمیسیون عمران مجلس:
🔹
در حال حاضر حدود ۴۰۰ هزار پرونده متقاضیان معرفی‌شده از سوی وزارت راه و شهرسازی در بانک‌ها در جریان است.
🔹
تأکید مجلس بر این است که بانک‌ها حداکثر تا دو ماه آینده پرونده این متقاضیان را تعیین تکلیف کرده و تسهیلات آنها را پرداخت کنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/akhbarefori/653360" target="_blank">📅 14:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653359">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0168d013f3.mp4?token=iBPNR60c8gUNYv9lC5xxIGEydUJmmvFd_gq4w9KQCwKGA2fojlzR7rUBeA81K5Lo-RQwzEXM9stA9RPJNsUjC4NC0FKcH-RlAHhzyFI4AFqqoWtzZlvWOo6IFwsV6YvKJIDFaWjzHjs1FWfOoATlWvJxIDM7NeFgZrHbwe_h0pmV_K4-WBsOuFwCA03jgN9jwaY0xVJHAUC6iSqMaPe8LsuRbJm9kg2U3HLNKaIqDO2Nrh3xOB2C6drfkIGELa9lxphSoZ5_Fq3xJ2gpFXZ41qiQIEV_qyZQ13vzJc8ONnN1YNxjN6E6-BYudr10G_y6Mm2QKod0GA_wTeFYFTMQvAuaCxt_tyOP6P1T_3_vblknrAZncGcbjuQt9VdnbrQ3h1H-PpeGyrD-3_iMavmSPHussbO7ymt_wOKED8HuE_I1esM382Mnytm6vOpXJjuQH8GOM3XEYHn5zcl0Wm1B5SaetJ2-R5Da288qDRvcVlqcvCRuuaJUOljbeQ6hVMYoSGSaz16lPszK8i2j-Px2cpfZ7vRZed00eWTKGl48GUJne7HyzkaeiRhOBBsBMM1MwN0e4bW3oiDQJ4IokTQEyC4L7EkofirljCxd92G2HwhH4XwUNrF7VCaJ_79xLC5xWulgr5yRuSiN66WtJRr1dJ26mmO9EGPFAUPregnnPZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0168d013f3.mp4?token=iBPNR60c8gUNYv9lC5xxIGEydUJmmvFd_gq4w9KQCwKGA2fojlzR7rUBeA81K5Lo-RQwzEXM9stA9RPJNsUjC4NC0FKcH-RlAHhzyFI4AFqqoWtzZlvWOo6IFwsV6YvKJIDFaWjzHjs1FWfOoATlWvJxIDM7NeFgZrHbwe_h0pmV_K4-WBsOuFwCA03jgN9jwaY0xVJHAUC6iSqMaPe8LsuRbJm9kg2U3HLNKaIqDO2Nrh3xOB2C6drfkIGELa9lxphSoZ5_Fq3xJ2gpFXZ41qiQIEV_qyZQ13vzJc8ONnN1YNxjN6E6-BYudr10G_y6Mm2QKod0GA_wTeFYFTMQvAuaCxt_tyOP6P1T_3_vblknrAZncGcbjuQt9VdnbrQ3h1H-PpeGyrD-3_iMavmSPHussbO7ymt_wOKED8HuE_I1esM382Mnytm6vOpXJjuQH8GOM3XEYHn5zcl0Wm1B5SaetJ2-R5Da288qDRvcVlqcvCRuuaJUOljbeQ6hVMYoSGSaz16lPszK8i2j-Px2cpfZ7vRZed00eWTKGl48GUJne7HyzkaeiRhOBBsBMM1MwN0e4bW3oiDQJ4IokTQEyC4L7EkofirljCxd92G2HwhH4XwUNrF7VCaJ_79xLC5xWulgr5yRuSiN66WtJRr1dJ26mmO9EGPFAUPregnnPZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: آمریکا صلاحیت ندارد برای مذاکره تعیین‌تکلیف کند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 5.85K · <a href="https://t.me/akhbarefori/653359" target="_blank">📅 14:14 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653358">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
راز رفتار متفاوت ترامپ در چین فاش شد!
🔹
ترامپ را که همه با تحقیر، داد و رفتار تهاجمی می‌شناسند… چرا مقابل چین ناگهان آرام، حساب‌ شده و حتی مودب شد؟
🔹
جواب شاید نه در سیاست، بلکه وسط تحولات ترسناک چین پنهان شده باشد.
🔹
این ویدئو نشان می‌دهد چرا حتی آمریکا هم مقابل «ابرکارخانه جهان» محتاط حرف می‌زند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 6.59K · <a href="https://t.me/akhbarefori/653358" target="_blank">📅 13:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653357">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bqKep6-HwqBmh-2b5CXFx17LuCqDubfL7FS7fUaNutiSd1qS8EVywWYLsPNxt-tChrQjuZsv2eaITMXzcDfAWL5fW7aBA2EYxtwrRekXaxwflixYse5xfciaRHPwrkZFkfgq7buR1JNnT2iozc9UpQtQZpMxnPY6MSuFc1ec3o2H0ABq8qEHnrwowD8xWg7KgFQhcricPZbJEXGBm0uQ6RKU5Jfo4SveYP5ePr_N6S2UVrEwgoZp-PQmhXp4MLJ_2xIZNpVzzjgJf3_4VOKowlXzbVQ_b52MiBEgajJexi27WT_rVQvhoFukQuXYLbgQJgqq70UC-EC-QS_H-r89zQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جزئیات ادعایی گفتگوی پر تنش ترامپ و نتانیاهو بر سر ایران
یک مقام آمریکایی به سی‌ان‌ان:
🔹
نتانیاهو روز سه‌شنبه گفتگوی پرتنشی با ترامپ داشت. نتانیاهو ناامیدی خود را ابراز کرد و به ترامپ گفت که معتقد است به تعویق انداختن حملات مورد انتظار یک اشتباه بوده و رئیس‌جمهور باید طبق برنامه ادامه دهد.
🔹
یک منبع اسرائیلی: در طول این مکالمه یک ساعته، نتانیاهو خواستار از سرگیری اقدام نظامی شد. مذاکرات جاری، نتانیاهو را ناامید کرده است. نتانیاهو استدلال کرده است که تأخیر فقط به نفع ایرانی‌ها است./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/akhbarefori/653357" target="_blank">📅 13:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653356">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">♦️
اسامی ادارات پرمصرف برق اعلام عمومی می‌شود
🔹
معاون وزیر نیرو: به ادارات پرمصرف برق، اول اخطار داده می‌شود و در صورت تکرار و رعایت نکردن، فهرست اسامی مشترکان پرمصرف برق به صورت عمومی اعلام می‌شود.
🔹
در مناطق غیرگرمسیری یک ساعت قبل از تمام شدن کار باید دستگاه های سرمایشی خاموش شوند.
🔹
در صورت رعایت نشدن مصوبه، برق آنها قطع می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/akhbarefori/653356" target="_blank">📅 13:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653355">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">♦️
الجزیره به نقل از یک منبع پاکستانی:
🔹
مقامات ایرانی از پاکستان زمان خواسته‌اند تا خواسته‌های آمریکا برای مذاکره را ارزیابی و بررسی کنند
🔹
اورانیوم غنی‌شده، گره اصلی در مذاکرات آمریکا و ایران است.
🔹
فرمانده ارتش هنوز در پاکستان است و سفر او به ایران بستگی به نتایج سفر وزیر کشور دارد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.42K · <a href="https://t.me/akhbarefori/653355" target="_blank">📅 12:49 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653354">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
واکنش کوثری به اقدام امارات برای دور زدن تنگه هرمز؛ آنجا را زیر آتش می‌بریم
اسماعیل کوثری، عضو کمیسیون امنیت ملی مجلس در
#گفتگو
با خبرفوری:
🔹
قبل از جنگ به امارات نامه دادیم که این مکان ‌هایی را که در اختیار آمریکا گذاشته‌اید اگر بر علیه ما استفاده کنند، ما هم این حق را داریم که برعلیه آنها شلیک کنیم.
🔹
می‌خواهند لوله بکشند خب بکشند، اما این گونه نیست که بگوییم پایگاه‌های آن‌ها در امن و امان است و حتما به ضرر خودشان می شود.
🔹
اینها می‌خواهند بگویند چون ایران تنگه هرمز را کنترل می‌کند، ما هم استفاده نمی‌کنیم و به آن طرف لوله می‌کشیم.
🔹
ما هم می‌گوییم حالا که شما این کار را می‌کنید؛ یعنی می‌خواهید به آمریکا و رژیم اشغالگر اجازه بدهید که از سرزمین شما بر علیه ما استفاده کنند. ما هم هیچ موقع گذشت نمی‌کنیم که آنها به راحتی بیایند و آنجا را قطعا زیر آتش موشک‌های خودمان می‌بریم.
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.46K · <a href="https://t.me/akhbarefori/653354" target="_blank">📅 12:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653353">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">♦️
آمریکا تهدید کرده که ویزای هیئت فلسطینی در سازمان ملل را لغو می‌کند، مگر اینکه «ریاض منصور»، سفیر فلسطین، از نامزدی خود برای معاونت مجمع عمومی سازمان ملل انصراف دهد!
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/akhbarefori/653353" target="_blank">📅 12:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653352">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">♦️
۲۰ ملوان ایرانی ساعتی پیش به میهن بازگشتند
🔹
سفیر ایران در پاکستان: از اقدام انسان‌دوستانه و خیرخواهانه دولت محترم پاکستان برای پیگیری آزادی ۲۰ ملوان ایرانی که به دلیل توقیف کشتی‌شان در آب‌های سنگاپور در وضعیت نامناسبی قرار داشتند، صمیمانه قدردانی می‌کنم.
🔹
در این راستا، از تلاش‌های خستگی‌ناپذیر نخست‌وزیر محترم و وزارت امور خارجه پاکستان، به‌ویژه معاون نخست‌وزیر و وزیر امور خارجه و سایر نهادهای ذی‌ربط، تشکر می‌کنم.
🔹
این ملوانان پس از تلاش‌های دیپلماتیک از سنگاپور به اسلام‌آباد منتقل و ساعاتی پیش به میهن عزیز خود بازگشتند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/akhbarefori/653352" target="_blank">📅 12:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653351">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bikMjEExAnP13-qEPrRpRcJgyti18QktuBk9A2fSxyR62uUN56RNLEBhboQ6tmPaWPYZv05IzFmpL77D-xHR7l7SLnstOvamq4GfIXLguncsBpSinvdOyehIAVA8V4pMxO1oCSoPXqzA7x2hnsmpi6uY9QWFXt2DsRcKfGtUpy6rDBjQIn1FliPc3ege_hGxeAFsUyuFy_EVLEabWH3nEemIaWrTrEqziF8DX6u5RUXSAHJ_3pT3Ym9NjGCOGuRzQUKVXX4smysx06dn3pTTDv44W-iWj91bsQmCtnNxMDogVoJ7aqJDGVRVJDakkzw5XLXTcRI0ZSJm-prB1gLQWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
عملیات شکار پرنده‌های آمریکایی
🔹
۴۲ پرنده آمریکایی در جنگ با ایران از مدار عملیات خارج شدند؛روایتی از هزینه واقعی جنگ در آسمان خاورمیانه.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/akhbarefori/653351" target="_blank">📅 11:57 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653350">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BkHsfLQO9cS30_Iyny0EsBpBT0qcglPy8icnOVq6rrDgxX4sfFO82_SZlAeodyHOI2yyBpIDL4xTPX21VOT1sR-gGKdJTpW_DKSLJY152iI3f2W5oQ98hylB1NbNvW9EVAXLJjFdnqYaRL8IQJ1dI7biQiK5YB1pUIaaIh73pW-XSvsYUZLivy0uQreYanLZf6UzoWquiVeuvVh-3NWzdXiE3DWMfFZyvhuROPxSJTiakteK-F8WY1oaQQyfnthi_1RysEo2_fVqbb_zrAch7sgDBkVySrhu4t6utMubO9mxzWLgTBGFSLjLZk4H4MHjp2_Z8jR2JTRgO2CcAsTS5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
شهر گناه؛ چگونه با وجود جنگ، تجارت جنسی در هتل‌های دبی رونق دارد؟
🔹
به واسطه جنگ و تنش‌های اخیر بسیاری از کسب‌وکارها در دبی با کاهش شدید مشتری، افت فروش و رکود گردشگری روبه‌رو شده‌اند؛ اما در میان این بحران، بازار تجارت جنسی همچنان فعال و حتی پررونق باقی مانده است.
در خبرفوری بخوانید
👇
khabarfoori.com/fa/tiny/news-3216745</div>
<div class="tg-footer">👁️ 7.92K · <a href="https://t.me/akhbarefori/653350" target="_blank">📅 11:44 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653349">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bc0005ed4.mp4?token=jgWLnUowRKD7OBHGXUAR21OoLugkxCYgYJXAsgsQmmQc1NsX3OrVmSd03Y4T1E4qckM0rCnObO0OOIaRyiqG6X7AczP9r4s7xXBJgFa79JrpoRo_FMqOMo2ltPNrU0LMmigJhIRB5pTZHopyFxTlWXN63LNF0cOWx4ne9mGFbwGqnx7HtoC1NuQ1gG_Nrc9zMccTMegtOFiKPzifRSj1IUiLZ4wW_hP0zDFQ2HGYWNpNmIHvNbXlDFkLNPidv_k99Pjk8-xyluMYXvCUqDwN5c0sBrcSwDnI4jcewzEAT1uzsiqgqZr-Q20AE6vJRQK4Zr-hnbdQPVc9t--pFstZ6YUOeCvjfMR3R8hj7KLFr3wO-TDqtB2O3wYjhi4fQPQveBR49qCVs6ckG6h3QNXXLBc5WdXCzm6uJat3UmheB0nLn79vvdHsr9JP_XEA174HQsFapLlpHbl0miT4tWGTKmseW9G-Tu3mCqxQcX_tg_oGvu1J9JEyomXMK6f_PjJExkDPnOxX8Lz5MLQLYgJ0hBC2TcWjdAHRrHRBDVuRPvvv2j0D3QoxM680M7cerDiF1JUZ3QlAA0CSzFATtq7uoFtFBGw-aOL9Ddi2D1HXM8_Pyw2xUHd8A30Sh3_w8tWMTH4TmRXzrBuq_6jjULNqe1-pH6NSi5dC3b4GgM-Ftgc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری شرکت قطعه ساز کروز از تحویل قطعات به سایپا
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/akhbarefori/653349" target="_blank">📅 11:35 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653348">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43cc421836.mp4?token=TAYvDZG8b0hsPWRxUIO_BlY2KGrcDfpAvCeQ3hD7kV-9W6jcMNQyTtplboKBuQDMVkPEjlydsG90j1q3tv3P4x_HPflsoAMFMYqy4KmctSOulooYhOXH14LO2iiIZ25z09kFuyj6ZcURRvyEvR-YV7B51RkfTEFyL-Qdqki0KnKRMPaEcwWpeg7nBnY4DD2Ws0BiavK0Z4Abix9lcb-3uwY4AtDtrVwPl4Ho2hGU0GKZsabYQXxpaDWMyfdyNWIAb9UGkjIevkoU1MQ0JNpTIGYhLp0l0KVxJlXHR6wS1K87EMUAiRB81jOoboB9zxgoT3_kTUT9w3pkuNK6xgJ6bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">توقف اسکرول. شروع کاوش.
به بهترین کانال‌های تلگرام غوطه ور شوید—انتخاب شده، دسته‌بندی شده و تنها یک کلیک فاصله.
🗂
کل کاتالوگ را اضافه کنید</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/653348" target="_blank">📅 11:26 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653347">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQ8G5OtYt53cDCkhZLl1MUYlrvIBsSuUWjioI8lz0fJXPLZUiOlDt9wYsZ4LLc38-GiOvlOTzOpIyCUKb1yMsWabduD8Xt6NVmf7lKYjZG1AwZgNL9unwuF7t54UZQP3Z46Blj1OojgdwbPGbZvMmnJ5s1h7HpJ7RNP_NwYjhEqVwrJ_g8xhyN4g4-I6xQePPeJZsSSzh0XNkrwIkA0u16stQoIfFEf4_QSMZeL15Nt6bWGGr5GiqIr7SFn_YgaVvyelAOjAVWYI-YdJ5z7u8aNDxJHFNqcD7PdkhPN3ScUI2mnSUyVbWmJFjOYMIWnmGy1GxaoBuXDLh2QKIgWnww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اطلاعات آمریکا: ایران به‌سرعت در حال بازسازی پایگاه صنعتی نظامی‌‌اش است
🔹
ارزیابی‌های اطلاعاتی آمریکا نشان می‌دهد که ایران سریع‌تر از انتظارات در حال بازسازی پایگاه صنعتی نظامی خود است و تولید پهپادها را از سر گرفته است.
🔹
«ایران در طول آتش‌بس شش هفته‌ای که از اوایل آوریل آغاز شد، بخشی از تولید پهپادی خود را از سر گرفته که نشان می‌دهد به سرعت در حال بازسازی برخی از قابلیت‌های نظامی تضعیف‌شده‌اش در اثر حملات ایالات متحده و اسرائیل است» این بخشی از گزارش امروز به استناد اظهارات «دو منبع مطلع از ارزیابی‌های اطلاعاتی ایالات متحده» است.
🔹
طبق این گزارش به نقل از چهار منبع آگاه، «بازسازی توانایی‌های نظامی، از جمله جایگزینی سایت‌های موشکی، سامانه‌های پرتاب و ظرفیت تولید سیستم‌های تسلیحاتی کلیدی که در جریان جنگ نابود شدند، به این معنی است که اگر آمریکا بمباران را از سر بگیرد، ایران همچنان تهدیدی قابل توجه برای متحدان منطقه‌ای واشنگتن است».
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.58K · <a href="https://t.me/akhbarefori/653347" target="_blank">📅 11:23 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653346">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/904502ae0f.mp4?token=FalXlY-J0Evhk9iotqUgj90Di7ZAp1jCSw_CU2QDNNAgCQg_To1twVgK4REwZw9sv1dQsTlk4NET0OadTqFPCKGNalgYv2lHMP4IUYfQalIybDUEfUtr7O1JYdhAl7Hg7h6WPbZj7aCWV2qTVAPKaSMPDs35cVSpvDskgTIZWwUI9CerjomS92PJhb1auDQGOfij_eOH3P4AtXr8WPtXcM0KZlKQ6Xmjf_-2TFPCMq7bJMNvfzqwE2fNSMr2H0LLpfD0BCWzGJl2nDAnkB8EaJY2j3qnhlNpcQAG9zr_XS23jsC-7OC2SlzGK6wVraR-6JJIE3W6DxrUa7n7smSs_Lo04nZ5ccrnzDnJmU_qqEVOXBTRDSrs6UV4cwBDXvoilJ_0x02DrV59ZSgwASpf9TdjM9iYcPBNP6RGHqvTA3KuFf07_yrce301lHt_sjgt-sDZEU8g-edDp5fp8-ZKBwo4cHR3xOJcwxBK722oWCtHhUELXq0evk5Zp42A5V_QdxKaZx0T-6GyLN5DJUlxmErEUrQURIe9FNm0tGSAgW06MqqsgLb5pJ-C7wXFkHlylE6vFNq687OYRJtdEqMXvcXc64VruZmIdzz8OtgyQakl5t3qdt834uLLzf7jTlhMD4Qip529LoLUX9DaQZfbhfJ3Hng2lN_oWDISgaNTE8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آیا جنگ با پذیرش پایان صنعت هسته‌ای ایران تمام می‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.87K · <a href="https://t.me/akhbarefori/653346" target="_blank">📅 11:20 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653345">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
سایت اسرائیلی واللا: فرمانده تیپ ۴۰۱ که در لبنان به شدت مجروح شده بود، پس از عمل جراحی برای خارج کردن ترکش‌ها در ناحیه سر، همچنان تا این لحظه بیهوش و با تنفس مصنوعی زنده است
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.36K · <a href="https://t.me/akhbarefori/653345" target="_blank">📅 11:09 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653344">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">همخوانی مردم میدان انقلاب در سالروز شهادت رییس جمهور شهید آیت الله رئیسی
خواهران:
آری؛ چون شهیدِ جمهور
سرباز دین خدایم
من هم خادم‌الرضایم
برادران:
مثل رهبر شهیدم
در این جبهه جانفدایم
من هم خادم‌الرضایم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.6K · <a href="https://t.me/akhbarefori/653344" target="_blank">📅 11:05 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653343">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee64f10908.mp4?token=LF6RiPv-k87Q7vOZE3fPTSkgHL8B2GMH4Q2E9k9idM0qOmvvUv4OHSXstYEa-_KwF92nDqs4Q74mYkVBuD8N6_xnkTrwxDsBvukzPH9pV72rzjCaN3Jm1I_i2C0966LRN6f9Go49W12NrOxYNdcXM6YRiHPY4TCEnAgJTQ-CmdSL56TPVr4Iors-3Sjqt0EKTsuHdOcTSJLH8-coAu0LV95JNQNdFBXqLtR6Chvm0-ZND_TRbR1_Xf_FNzcgzNjQ5uD9bYARZVhA3qIYP8uzTBSFHU8pBVSHOta2L7zXaWjXeUvpZ2Cwl7NCHAS1r3_tVLiIAJTZVjaauMRf4mxeGok_pK5rYsS3eoblUxBssGrKEZLLWRsf0qLL1l46pmgbloIS7X2UyAU4QKadIxCS4JjrDFfYX6MZZTL5UsaDRI5DIg5DepmcvTTXJBsAG9a1F_VKump5CNrWXOLWrFAW4L5hutKqenD_l4wuwghGVAqVk7CAwr4ZlAqQ5hVJpXSHhzed0LJCMqqq0j7CO4F_wIuWmgrbf4GpUa8yDoF8HjDHhAbO0fQyJJ4VoXMom_juBqxJBwe4us3gm3nm85bXUkIybKqWSwaL6jOBv3IZqV_tZfdQ34Q_uD9mOP0M605ciJjxsCnW9zcxkLGxOCOCMqjzLHLgihbJbv8CNQRPVa4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee64f10908.mp4?token=LF6RiPv-k87Q7vOZE3fPTSkgHL8B2GMH4Q2E9k9idM0qOmvvUv4OHSXstYEa-_KwF92nDqs4Q74mYkVBuD8N6_xnkTrwxDsBvukzPH9pV72rzjCaN3Jm1I_i2C0966LRN6f9Go49W12NrOxYNdcXM6YRiHPY4TCEnAgJTQ-CmdSL56TPVr4Iors-3Sjqt0EKTsuHdOcTSJLH8-coAu0LV95JNQNdFBXqLtR6Chvm0-ZND_TRbR1_Xf_FNzcgzNjQ5uD9bYARZVhA3qIYP8uzTBSFHU8pBVSHOta2L7zXaWjXeUvpZ2Cwl7NCHAS1r3_tVLiIAJTZVjaauMRf4mxeGok_pK5rYsS3eoblUxBssGrKEZLLWRsf0qLL1l46pmgbloIS7X2UyAU4QKadIxCS4JjrDFfYX6MZZTL5UsaDRI5DIg5DepmcvTTXJBsAG9a1F_VKump5CNrWXOLWrFAW4L5hutKqenD_l4wuwghGVAqVk7CAwr4ZlAqQ5hVJpXSHhzed0LJCMqqq0j7CO4F_wIuWmgrbf4GpUa8yDoF8HjDHhAbO0fQyJJ4VoXMom_juBqxJBwe4us3gm3nm85bXUkIybKqWSwaL6jOBv3IZqV_tZfdQ34Q_uD9mOP0M605ciJjxsCnW9zcxkLGxOCOCMqjzLHLgihbJbv8CNQRPVa4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خدمات مترو و اتوبوس تهران تا چه زمانی رایگان است؟
🔹
شهردار تهران: به علت اینکه در شرایط کنونی نمی‌توان مجدد خدمات اتوبوس و مترو را پولی کنیم تا تعیین تکلیف طرح ارائه شده در شورای شهر تهران خدمات اتوبوس و مترو رایگان است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/akhbarefori/653343" target="_blank">📅 10:55 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653341">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YLv0sWyexIfRQHLyYmrFbMgCarW5B-eeRsn0Zt7VU2Z6OXv3NVsFAXvlSHwhiZQEy4yPe2y5WkkE8_Rr-kkdhmgOCumIlOin7PfospFkb07Pl6qvhL-KqGCpRYuJ7UXgovleClDm_dpg0a76cscwgye_0qt0ls6DCa4RpReKbDoefMNYhSopTEq3rbMXcirqHIMZ8kAeniWLWgv6_j_dPpsQ_wdtihbdm6tMLzH5B6vNUQEVSMsLJrvSgl11wDYfRlOlG1azH8vOzhURS9pxbn1g0wvyfuCTZb1jU1rMMHpiigi4daC1EQCv8qol3GNGggTCUR4zTAWL588Si8Z_Yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a3utNg7CyGubtyXbUtqE59sBAPCkeOG5Hkay3WvsSgckojB7mrbQQcjHfo0XwazKlyYZMYnOS4fZvDwS8txaKuKpznuoHOi8om9yBuDm_0LDhNhxp6lmDMJU5gUxBiLyGSyus-4mtfNKh6GXGWvun1oqUjEZ3iBorid1adgjRZluemm8YHGHikxIxPldyr5vrCu5nvcx3BNggTO6ksOX7xX4dolg7fB6DGyXsneGE5rW9aNJXrypFOtvDagFp9yZmx9D-qyjQ3gEDUSd5YQptJcwBoRSVH-Z1llWeRQbpAkwDuRAjxkpQD3s9BtdTtrPFLi87M7tlYnKXgIVhKkJsA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
زمین می‌تواند خانه‌ای سبز باشد یا انباری از زباله؛ تفاوتش در انتخاب‌های ماست  شما هم به کمپین #نه_به_پلاستیک بپیوندید و تصاویر مربوط به این کمپین را برای ما ارسال کنید
👇
@Na_be_pelastic #نه_به_پلاستیک</div>
<div class="tg-footer">👁️ 7.81K · <a href="https://t.me/akhbarefori/653341" target="_blank">📅 10:52 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653340">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U72MmivYrk18SkSDffJ9trWWYE-an21Cs51Nh2YnivVcOZ_40Vs--t1MMEdCwNOc5ZFUf-XR07V8QwbQDcrBx2O_gVp-h2Flewni6A8zo_2d7a2WVeNpsU3_0A4nfAtWwpTODkWu0OAU_R_hlYrA71cbD8OB7anikJBGw85wYjvPSdTqKCG4xWDMjP0hU1Vk-f-WZNfSakJmpbzXkVuYS_8j2kFidsFz2LETcWGjzDUOXiSRv3HilrKbD3UIA4x_k4KQqeJBFGwm60q7M0aF361s8yT_eWwJ9gkrsueKn2MJWFon7srDXsScqxRwEDsAEVx7EwMwRiTIL5_PR-t0bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اعتراف زنجیره‌ای افسران اسرائیلی: ماندن در لبنان بی‌فایده است
🔹
رسانه‌های عبری امروز تصویری شفاف از بحران ارتش اسرائیل در جنوب لبنان ترسیم کردند. از اسرائیل هیوم و «هاآرتص تا معاریو و والا همگی از زبان افسران خط مقدم روایت می‌کنند: مأموریت نامفهوم، استراتژی نامعلوم، ناتوانی در برابر پهپادها و در یک کلام: یأس و ناامیدی.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.05K · <a href="https://t.me/akhbarefori/653340" target="_blank">📅 10:33 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653339">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sHxVN-ak9pDG0vlAw_yhtSJHNWqEFQNVZh92eblFld-u0DfmnKxtqBvRNbC1EM0pHUX5YBcnF_5j2C9BmU72-QJwksicZ16q_sJp8D0MaBpNRES75srdkX0CT75pH7rjn8iPZg6Y4pHt_cyaiKLpuwgwlMVKtcvkyTDIywtb4PbU0_0Le0DcTWMVsLadTfwm2iH0CKyp2O16u9G4MxdSjb6e25H-yPdhNSiE_ZKuNEMTIilzLLtSowKcdu2OvZZXzntNB5eM9eCmRGMKYDotZrhFtnfxkJVl3hrla6mrqHi2gild4RXi0ksbCZRV6ulTo_CB-I8Y1ZD4Ha8am1siEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
اردوغان خطاب به ترامپ: حل اختلافات واشنگتن و تهران امکان‌پذیر است
🔹
رئیس‌جمهور ترکیه در گفت‌وگوی تلفنی با همتای امریکایی خود، ضمن استقبال از تمدید آتش‌بس میان امریکا و ایران، تأکید کرد: دستیابی به یک راه‌حل معقول برای پایان دادن به اختلافات دو کشور امکان‌پذیر است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.77K · <a href="https://t.me/akhbarefori/653339" target="_blank">📅 08:59 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653338">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jp-IM8rdQ9gQULKV5XeUNOODJxHcc24HpoEvnPE7b7iSDG_ZJNmyUKUIxEaABnPCzlIET8AjDMwbqI52Q0rF10_vVXacANAz7fkQb0IRfkc3wbar8XQz2E-xjUK-0SM9i0PF5QC5Q4JR07b8lvOHRPPH6Oea_pDEKT9FxNfnIAKpTAduoDhTi9YJKXLzcxnPNELlYb-m-5hSW-OhZEd8JdPV26AS66O_HJ8n2QnpjYQ7lxgeLtaxClN0pwx7Vl_fzH5IdbnJcA3Rw_bpZMAshnkKeEwyFdMgMfX9SpQtYUlqpXR0I7gVH8q9BtIK6Rcm3WB2TM9_hIn_tMI3VDIrgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مهر بررسی کرد؛
🔹
بحران تنگه هرمز؛ بازنده واقعی محاصره دریایی کیست؟
🔹
تنگه هرمز به عنوان گذرگاه حیاتی عبور نفت جهان پس از تجاوزات ۴۰ روزه علیه خاک ایران و متعاقب آن، انسداد آن از سوی جمهوری اسلامی و نیز محاصره دریایی از طرف آمریکا، دوباره در مرکز توجه جهانی قرار گرفته است.
🔹
از نگاه ناظران، بحران تنگه هرمز نه تنها یک تنش اقتصادی است، بلکه یک چالش بزرگ سیاسی و دیپلماتیک نیز برای آمریکا و متحدانش ایجاد کرده است.
🔹
پس از آغاز تجاوزات و تقلای واشنگتن برای کنترل مسیر اصلی انرژی جهان، متحدان سنتی آمریکا در ادامه همکاری با کاخ سفید دچار تزلزل جدی شده‌اند؛ وضعیتی که پیامدهایش فراتر از میدان نبرد انعکاس یافته‌است.
🔹
بحران هرمز نشان داده که هزینه‌های سیاسی این محاصره برای آمریکا و متحدانش بسیار فراتر از میدان جنگ است؛ تردید متحدان، فشار برای راه‌حل‌های دیپلماتیک و واکنش‌های جهانی نسبت به استراتژی‌های یکجانبه‌گرایانه آمریکا و ستیزه‌جویی رژیم صهیونیستی همگی ساختارهای سنتی همکاری را تحت فشار قرار داده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/akhbarefori/653338" target="_blank">📅 08:46 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653337">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af6e54b6e3.mp4?token=Be_1PqCm8tU4V5AbRMCVFwSsvm2gzuBVA1TtAGBGZELY19c5W-priRtXC_IKeCHqq_NqKNY5OX0N5sKoje_GMOxzevyLVZ9QxXZeLQ2zXEwb-kTvGqxQZ-KkpwL029y0cN7oKgDnna1zwyZ4hI4dn_M4K90U6eVf6qfvjYfRAAImO0V7E8nsLWtxtzbmHrmppSm7Tu9JP9sbRz8cfsBvJryupWWR04KBbdz76xH67263zyp-LqgP2pXdm9q7mXT-wfN0uhkh8d8PtFO1wZGAN7AWA-SkQ8gf050SoHvRZvEJzdeS55FNjoOolrWhlSfb_j_CmyMB10gnmkvJLg4FZVAlqnXD-tZ6PeTPv9K5mPIs6HsDS0MeB_Ix5groJ5RXIg7tBgxojr_C55cXk2cERVfneN0RgfV6Ce7HR_67KHSfNevQSo1wXPEP6LuhsIKtjoHd8CeWk0O-dUzu1xZVWn5OIyH2H6IBdVKb0PIByHUu3gkM3L05RfhDYBr_wLvBjTSOWKYUpp3KEMsgsZKi9ZtUX7XFvfAdABL2Io1rZpdQutMvBqCxUxnK19k1ViC9nTM9CfpNqtcMlKBPqCJD0T1vDXA4mZwhABedwfz4CVXzGPkBLStS2zOpiPp6nwOjKyCvDCAOyiHhEnTfUUtFlx4toT7SaWHZGoAQACXG3OM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af6e54b6e3.mp4?token=Be_1PqCm8tU4V5AbRMCVFwSsvm2gzuBVA1TtAGBGZELY19c5W-priRtXC_IKeCHqq_NqKNY5OX0N5sKoje_GMOxzevyLVZ9QxXZeLQ2zXEwb-kTvGqxQZ-KkpwL029y0cN7oKgDnna1zwyZ4hI4dn_M4K90U6eVf6qfvjYfRAAImO0V7E8nsLWtxtzbmHrmppSm7Tu9JP9sbRz8cfsBvJryupWWR04KBbdz76xH67263zyp-LqgP2pXdm9q7mXT-wfN0uhkh8d8PtFO1wZGAN7AWA-SkQ8gf050SoHvRZvEJzdeS55FNjoOolrWhlSfb_j_CmyMB10gnmkvJLg4FZVAlqnXD-tZ6PeTPv9K5mPIs6HsDS0MeB_Ix5groJ5RXIg7tBgxojr_C55cXk2cERVfneN0RgfV6Ce7HR_67KHSfNevQSo1wXPEP6LuhsIKtjoHd8CeWk0O-dUzu1xZVWn5OIyH2H6IBdVKb0PIByHUu3gkM3L05RfhDYBr_wLvBjTSOWKYUpp3KEMsgsZKi9ZtUX7XFvfAdABL2Io1rZpdQutMvBqCxUxnK19k1ViC9nTM9CfpNqtcMlKBPqCJD0T1vDXA4mZwhABedwfz4CVXzGPkBLStS2zOpiPp6nwOjKyCvDCAOyiHhEnTfUUtFlx4toT7SaWHZGoAQACXG3OM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
متکی: با اولین شلیک آمریکا، جنگ زمینی را آغاز کنیم
🔹
وزیر امور خارجه پیشین کشورمان پیشنهاد کرد اگر آمریکایی‌ها جنگ سوم را آغاز کردند، با اولین شلیک آن‌ها، ما جنگ زمینی را آغاز کنیم؛ یعنی رزمندگان ما به گرفتن پایگاه‌های آمریکا در منطقه، با گرفتن اسرا، مصادره دارایی‌ها و امکانات نظامی‌شان اقدام کنند، این عمل، توصیه مقام معظم رهبری را در رابطه با غرامت‌هایمان نیز عملی خواهد کرد؛ زیرا اکنون ماه‌هاست که می‌گوییم غرامت باید پرداخت شود، اما هیچ پاسخی دریافت نمی‌کنیم.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/akhbarefori/653337" target="_blank">📅 08:32 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653336">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
۲ تروریست عضو تشکیلات مخفی گروهک‌های تروریستی تجزیه‌طلب به دار مجازات آویخته شدند
🔹
رامین زله فرزند کمال و کریم معروف‌پور فرزند کمال عضویت در گروهک‌های تروریستی تجزیه طلب، به جرم تشکیل گروه با هدف برهم زدن امنیت کشور، قیام مسلحانه از طریق تشکیل گروه‌های مجرمانه ، تیراندازی و اقدام به ترور در راستای اهداف گروهک تروریستی پس از رسیدگی به پرونده‌ در مراجع قضایی و تایید حکم در دیوان عالی کشور به دار مجازات آویخته شدند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/akhbarefori/653336" target="_blank">📅 08:31 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653335">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FCpfU-uKigS-LQmoQzr8k16yVB5UAnoTkpTJao2Bs6sg-2vQP662IPP4-WXlXW0LE63M8AbnVqG7_s7fxZbtdR-8s7iCRrhmyDTH4ypVz8sUMnl3xDEg_4cn00HSoJgcfLttHdwibzqEphl0N7SyrHb6lfFaeabcs0rEa_dwQpnzhpsnvlNTKb5SoMq6H3hNZCe9N-bKZcLrc0iOgZNETatF-z26SvUxohTBloFRuxqdaUxmbmmAf7u1pz75-1urnWSA06zUxltdlatB9jLX6qpXWQqPogomXjrChO0lf9ZeDoA6p5xZV5ypS69mHeKhNBA-kqQ-JxT0w4EEWqUhBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ولایتی: نقشه کریدورهای منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند
🔹
مشاور رهبر معظم انقلاب اسلامی در امور بین الملل: اکنون نقشه کریدورهای (راهگذرهای) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
🔹
ترامپ در پارادوکس «تهدیدهای روزانه ایران» و «مشتریان عصبانی پمپ‌بنزین‌های آمریکا» گرفتار شده؛ او برای مهار تورم داخلی خود محتاج ثبات بازار و کاهش قیمت انرژی است.
🔹
از سوی دیگر، تغییر محاسبات در قفقاز و کمرنگ شدن واژه تحمیلی «کریدور ترامپ»(زنگزور)، نشان داد که اکنون نقشه کریدورهای (راهگذرهای) منطقه را نه با تهدیدهای واشنگتن، بلکه با واقعیت‌های میدانی تهران می‌نویسند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/653335" target="_blank">📅 08:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653333">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌سوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بهرام چوبین</div>
</div>
<a href="https://t.me/akhbarefori/653333" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بهرام چوبین؛ و پادشاهِ شکاک
🗓
وقتی در سازمان یک نیروی «ستاره» داریم، چگونه غرور کاذبِ مدیریتی می‌تواند حکمِ نابودیِ کسب‌وکار را امضا کند؟ و چرا برای یک نیرویِ متخصص، مهارت‌های سخت (Hard Skills) هرگز جایگزینِ سیاست‌ورزی و درکِ قواعدِ بازی نمی‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.35K · <a href="https://t.me/akhbarefori/653333" target="_blank">📅 07:19 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653331">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3868b761.mp4?token=NYCi7_1C8GMycgpgu1Ek6BsmAJEO9ShPhEhZ048NHIJE5AQv_TJex02aXRykP98XlPNS5GRkXUwJB_In4beH31vHr_UunXWFLXlme51r3MybgOwuYtlAbiSgFGnFDI31KZiKxbI6Byjf9ek4aOsq3xmg7yxBoaOXxwKu4PG7673EawX90KxboCcG_YVvMbu7HzUDdwp3jqvg9LesngxtJgyFXc2pgDf7AqFs2NVVhpPYiCzrtdWrxZ7RIoToAFvd5ZYdQ9rs8sEOtgC2WHVx1dtrzrvcWUzClmD316pO5MJ4uzQk66WQR9nQdzOZHNWjAiN78mPVNkMSPy3ibz5OrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3868b761.mp4?token=NYCi7_1C8GMycgpgu1Ek6BsmAJEO9ShPhEhZ048NHIJE5AQv_TJex02aXRykP98XlPNS5GRkXUwJB_In4beH31vHr_UunXWFLXlme51r3MybgOwuYtlAbiSgFGnFDI31KZiKxbI6Byjf9ek4aOsq3xmg7yxBoaOXxwKu4PG7673EawX90KxboCcG_YVvMbu7HzUDdwp3jqvg9LesngxtJgyFXc2pgDf7AqFs2NVVhpPYiCzrtdWrxZ7RIoToAFvd5ZYdQ9rs8sEOtgC2WHVx1dtrzrvcWUzClmD316pO5MJ4uzQk66WQR9nQdzOZHNWjAiN78mPVNkMSPy3ibz5OrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهرام چوبین و تراژدیِ مدیرانِ کوته‌فکر
#پادکست_کافئین
| قسمت بیست‌و‌سوم
☕️
در این اپیزود به سراغِ سرداری رفتیم که تنها با ۱۲ هزار نفر، ماشین جنگیِ یک ارتشِ چند صد هزار نفری را در هم شکست، اما قربانیِ ناامنی، پارانویا و عقده‌های شخصیِ پادشاه خود، شد.
بهرام چوبین ثابت کرد که تحقیرِ یک نیروی نابغه، چگونه می‌تواند پایه‌های یک امپراتوری را ویران کند.
هر روز صبح با یک شات غلیظ از تاریخ آمادهٔ شروع روزتان باشید!/مدار
از اینجا ببینید و بشنوید
👇
https://www.aparat.com/v/elhxc81
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.49K · <a href="https://t.me/akhbarefori/653331" target="_blank">📅 07:16 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653330">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzhaxBV13vLXbZIZqUM7ITamYXoyvzjk-MgSBO27rRS4IOqGvIVUfNfv2we2cgYSEY1g_GHeu4o-fp2SAVUL5u0Y4l-Y9SS2R7RTNLVAKnG2iDTHJwX4tvxP-QwJ-KHy81gWsE4VXJxCast4h9Wob9hH2aduH_nwliYfv3ZwnwUuYDQzColmPHp1uVaigzyTXO8U-hrCCvzWyn8hIXuNlHrYdhz1kXZyy9Ue-Vnk1Wp98A_tgepTs58MhAi4c4PjRhkwde7unjBVDM4FCA_HIO3pCePqsCLdb-eUC9j5dQEtaZVXrifZJ3k6Ni6me4KPrI6CXAg7Mm6doAzVlvnZag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هر روز خود را آغاز کنید با:
بِسْمِ اللَّـهِ الرَّحْمَـٰنِ الرَّحِيمِ
🔹
با خواندن دعای عهد و چند دقیقه گفتگو روزانه با امام زمان (عج)، پیمان همراهی و خدمتگزاری‌مان را تازه کنیم.
#صبح_نو
امروز پنج‌شنبه
۳۱ اردیبهشت ماه
۴ ذی‌الحجه ۱۴۴۷
۲۱ می ۲۰۲۶
پنج‌شنبه‌ها
#دعای_کمیل
بخوانیم
⬅️
متن و صوت دعای کمیل
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/akhbarefori/653330" target="_blank">📅 07:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653329">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">♦️
ایروانی: رژیم صهیونیستی بزرگترین قاتل غیرنظامیان در جهان است
🔹
سفیر ایران در سازمان ملل در نشست شورای امنیت سازمان ملل درباره حفاظت از غیرنظامیان گفت: شورای امنیت به دلیل کارشکنی یک عضو دائمی که خود متجاوز است، در انجام مسئولیت‌های خود در مواجهه با این نقض های فاحش شکست خورده است.
🔹
شورای امنیت نباید در برابر تهدیدهای مکرر و روزانه رئیس جمهور ایالات متحده علیه ایران، از جمله تهدید صریح بمباران ایران و بازگرداندن ایران به عصر حجر، نابودی زیرساخت‌های انرژی، اقتصادی و صنعتی کشور، هدف قرار دادن دانشمندان هسته‌ای و مقامات ارشد ایران و حتی لفاظی‌ و تهدید بر نابودی تمدن ایران، ساکت یا بی‌تفاوت بماند.
🔹
رژیم صهیونیستی بزرگترین قاتل غیرنظامیان در جهان است و شایسته هیچ پاسخی نیست.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.88K · <a href="https://t.me/akhbarefori/653329" target="_blank">📅 05:45 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653328">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">♦️
فرستاده ترامپ: زمان بازگشت و تقویت حضور نظامی آمریکا در گرینلند است
🔹
فرستاده ویژه رئیس‌جمهور آمریکا در امور گرینلند، در جریان اولین سفر رسمی خود به این جزیره راهبردی، بر لزوم احیای جایگاه پایی و تحکیم حضور آمریکا در این منطقه تاکید کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.33K · <a href="https://t.me/akhbarefori/653328" target="_blank">📅 05:43 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653327">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
ایروانی: شورای امنیت نباید در برابر تهدیدهای مکرر ترامپ ساکت بماند
🔹
سفیر و نماینده دائم جمهوری اسلامی ایران نزد سازمان ملل گفت: شورای امنیت نباید در برابر تهدیدهای مکرر و روزانه رئیس جمهوری آمریکا علیه ایران ساکت یا بی‌تفاوت بماند.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/653327" target="_blank">📅 04:42 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653326">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">♦️
مدارس سمپاد برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی رایگان شد
🔹
رئیس سازمان ملی پرورش استعدادهای درخشان: حق‌الثبت برای دانش‌آموزان دهک‌های ۱ تا ۴ درآمدی به طور کامل رایگان است.
🔹
دانش‌آموزان تحت پوشش کمیتۀ امداد امام خمینی(ره) نیز در زمان ثبت‌نام آزمون‌های ورودی از پرداخت هرگونه هزینه معاف هستند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/akhbarefori/653326" target="_blank">📅 04:01 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653325">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">♦️
همسر یکی از اعضای کاروان صمود: هیچ خبری نداریم که زنده هستند یا نه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/653325" target="_blank">📅 00:41 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653324">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T9MzOiGkmlEaks2vojjVYh-3x1peHFELNGBUlnyy6Bc8ZDUP0NeOpfRvkiB_bmOWmO_uZlbHkOFCSP695Zw-64IpAtfMBQkk7LMzP8MzVAm_P9zy0p0uj3E_p9Olpg2KwZ3ZyevQgVA0YJPAz2obqZCt_kHTStnvq0OMWXRviyfuzUE6A7WEllrqWXIh4431uguxJK7YSuWsZPcrhi82TB0yVHvCXszUObXMMgmXpeQ1neVrzHL6uBzwAlfzkDG2iW5NW6CDcY5rt1u5d2ySp2ojrT0zZoHHxyYpAO7Wtvc4YTMuXFOUdCPjxZW2RZW0YVZ4LYAwAJY2fuaOjxpgOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک کاربر در فضای مجازی
چرا خط های سفید احراز هویت نمی شوند ؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/653324" target="_blank">📅 00:30 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653323">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MPXWMzbTIqO_Q2uy8MOseZwiveq8mkLvszmZBOnTXxIWAV3CXUFmty4tSVATsple39dM7iG2pRitAEJoxqGd7NXcMMsMm8_n7pwRBOZ0sk_hVd2EOybsCKWjctqFiYOgmo1UMnM63gSy9pAJ91pDqztV8aPP0PR8csorepGfJ-wpwA49XSgU1mfVe3EMFzor_v3AISQ6zABmO7pF--wYpcId8hv6ylXxzi9NHuP67AY4Dk2K1YHf_dd-Uz8A4hvowGQazZWQu7ljEAAa-toVxffo91jaWWE_Gr4LO0o72ivgAGR-4NocKHT7S-1W-LcJYAWNwMxYFMDdR3RjGwIS4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه دیگه کسب و کار های زیادی نجات پیدا کرده چرا یه عده عصبی اند؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/akhbarefori/653323" target="_blank">📅 00:28 · 31 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653319">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7OuJ4OIqcidaYNJfSFzzd2S8hJT7B1MC-FVwFMpr8Q692ompasMeeXW7InbR9ygM9iscHSgRgs6npWBvdlEUD4Oiu3wGT3PqARr-rjKp7QWisB1HYxToT38B9le4bFcNgDcm7ze5sjGJOxW_E0lKQbqi41Ndjzey24D64sMpNsRHesC1T3Rhd0s7aXT6zL3j5IW8kU9SiEwpX-cGzIHoUvXvrEkjj6GmDUGbC9md793hfNNdwOTWPvybUf7z_I7k1uDy_OTR91Ia-8Rp9RCSZd8aijhatLU8weDL2d1atI148ILjQd234BKPQMch56t088oAR9sCoYdMPQ-WOtFIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/N44oKwFRV47fKumTj9q459Cshiv7PLZ3rMxJKlVufg37apw17pspGZM1F3Nf319GA9X6ni-NgGcISQ8_Wkz4RcUGxiG8-QUzyTL0A4QxDtSmXkkgz03k7bauvyp-HCBW2TR7KOrMx3Jyf6MkdZQApFpBj8UcRA8WN2k-22DO6hE4DXtyNpM0SHq4vLqubtycDySpc1Hs2U8sDyv3VknctbceD0RLdN1b_Lk2kgm7Jow1YBVwnlg7Q80aXadKNFcfP7nhhnH7zzXCgc-bZJ48rjhr2JYDglcEaHR9fZu6jqqd8rQXhz6BloZVwSEI3fiMEgc7rsp7HC3lUMl7k6iQ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fJPa5qOZROydddbLyuL3dhHW5yV3Ncz_wK-dEaY-2DHoXVSge46eH967kJkDgxriHbBM9g68ra8dldS9mQo72WCxEbAJnW-gG5EMq_VqlDI93KXeWC8x_jHwSboso80kwETXy36ciBQ8uIgW3rylJ3pafqftHQSagF1QU6yfB2a-Nh4uJgqYnvB94WBH2Vt9aXgwLdairudK-fjMR1Od2SpgVk4NDk3dPHuZlbcGjDJJxyXfECSO_WnESPKf8qy-WSB2nc3huK7emDCyZNiHoxmH54YEObfOpzSu_SEX1B1qHcLpFYAs5g5hhIMCaCVh-NJeoV8-H5lLJ9RfvQ2uIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tR2bYfJ_lnFdYnWhAeUdi40IzH0nHCNmnmrKAF9Hw3YeL2_tb3Kidn77Vxj1bGMxZv8MhU21m67FSCKAGLVanrLtozWy6D_sqHMrSoH479Xtb2Oxdcu3Xj1S-r5I2c_8uAjKs9hW1J_0Hy3V43OYEB_PmoKewuKTjw_PZzuJR8XCWq9aPF32eRD8fqkNLkb9cJwYALrGdgKzCu35n447T_0J0YIVtNrr3OOehvqPsNgnYx6E4DtwQY-nMoAXXq4VOJraB4H5PuyZy7rb4_siMLSyHpidmlsFmHZMsF1fjs48i4jQbHAultmKk3HD4NC8R8NoN4nT_z8yUCidZoPQnw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
شیراز در حصار ریزگردها
🔹
با ورود سامانه گردوغبار به استان فارس، امروز وضعیت شاخص آلودگی هوای شیراز با ثبت عدد ۴۵۰ در وضعیت خطرناک قرار گرفت.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/akhbarefori/653319" target="_blank">📅 23:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653318">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQBBbZltERBRDdAjZ3gS5q3Hx3GGvMxO2i7ToSnX2tCeWStmm4jv5xgoPbcLCX6xPm2hWD9AjW-lVbM8do-w5sSfqTwa71T2Cze8Ag0SR5v9vIhnrX8wcp1eHFScpnG1ydrTmqLBrNL7fGxfzM6PlVUgseDsgFcj5tQ9eD9q-oNhpLq57sylRC47jykEbUWT7R1oO1UWLzUC12tYGUS_c5F67KINFX62Z_PNbzBaYjMqjM8DW92u1rXSN8qOglRj5-lEQTEjbXLk3J1du5ZLz0St1OY3bvYIhSqsHKja-RhISZCmIE-NNspPv5I-p-b_UQhJQT0V3PHtFLooYLmGKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نیکی: عملیات نظامی پرهزینه آمریکا در تنگه هرمز شکست خورده است
🔹
روزنامه ژاپنی نیکی نوشت: بیش از ۱۶۰ نفتکش در خلیج فارس گیر افتاده‌اند، زیرا ایران کنترل خود را بر  تنگه هرمز افزایش داده است.
🔹
عملیات نظامی پرهزینه ایالات متحده در بازگرداندن عبور و مرور پایدار در این آبراه مهم شکست خورده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/akhbarefori/653318" target="_blank">📅 23:52 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653317">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">♦️
دلیل عقب‌نشینی ترامپ فاش شد | ایران به توانمندی نظامی تازه‌ای رسیده است
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216606</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/akhbarefori/653317" target="_blank">📅 23:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653316">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">♦️
پلیس سیستان و بلوچستان از هلاکت ۲ نفر از عوامل شهادت ستوان سوم امیرحسین شهرکی که عصر امروز در سراوان به شهادت رسیده بود خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653316" target="_blank">📅 23:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653315">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/82f94bdb13.mp4?token=M4lVT2xL_E7I6id-dsRaCLRjDw8qHT16-l2HWNq2OCgVA0XcqeydnZR59lQFgJFgcWBhRDm4CYVSithnlTO4mgDh9-geHJfkoHXp8VC6pMr-aUTmgqjK9qoafW_M8rkSDWW4MVoUj9NZ7scFEWnacFe1tL3GCp6_lipyDRF20AoaQEW5Ivq_wkN92jM--QmKn6fF6Mc_6peLI-8IK84Oca-CUrdI1vYtDJXqJW_0-YFVuqSnO4XA6Ng5efUE3DqgFeMwiK0YvDyIM9aaKrHJAWF5krzdKBxc0SQP-ejtPmiYRTkAsQnzWV2U52US5uJvlwTE0aDQsObgdzcLWi3VCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/82f94bdb13.mp4?token=M4lVT2xL_E7I6id-dsRaCLRjDw8qHT16-l2HWNq2OCgVA0XcqeydnZR59lQFgJFgcWBhRDm4CYVSithnlTO4mgDh9-geHJfkoHXp8VC6pMr-aUTmgqjK9qoafW_M8rkSDWW4MVoUj9NZ7scFEWnacFe1tL3GCp6_lipyDRF20AoaQEW5Ivq_wkN92jM--QmKn6fF6Mc_6peLI-8IK84Oca-CUrdI1vYtDJXqJW_0-YFVuqSnO4XA6Ng5efUE3DqgFeMwiK0YvDyIM9aaKrHJAWF5krzdKBxc0SQP-ejtPmiYRTkAsQnzWV2U52US5uJvlwTE0aDQsObgdzcLWi3VCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عاصم منیر، فرمانده ارتش پاکستان، در راه تهران
🔹
عضو کمیسیون امنیت ملی مجلس: عاصم منیر فردا حامل پیام جدیدی از سوی آمریکا به ایران است
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/akhbarefori/653315" target="_blank">📅 23:36 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653314">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i19CC4aDb0xFyCWt77U2N87SNZKUd-4Qdp0GHZaUdl-ItSPYRmQq4FjJ-RjJ5b5GVSYtyRRbIXyT64QqOGxNhY8fBF5iXn1L_ZadybSWk5diPKVPOLM2eUOzmCzogsfGf-iuskRnKL7uGbqAYvovD9yL0KPc4PB3-QzMQch0BcScapAJ-k5QRoOtD5A1tFrOj3R7umTGZp-zOLk35ge4UEBoAaivifUyQvMw_QstXjg2wqFm8lECEP4RP4ZZRUacDIBgroz1L1E6fEv2rTkfOdN-SMhSXMfjcg-0WyvbAUT5NBt7UgZs-Z0xMqjmE7u3Bnv1oZSOcr_OaQa6EwlC3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
بیش از ۸۷ فعال در اعتراض به ربوده شدنشان توسط رژیم اشغالگر و در همبستگی با ۹۵۰۰ اسیر فلسطینی در زندان‌های این رژیم، دست به اعتصاب غذا زدند
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/akhbarefori/653314" target="_blank">📅 23:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653313">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">♦️
معاون نیروی دریایی سپاه: دست به ماشه‌ایم
🔹
اگر ترامپ در ذهن خود فکر می‌کند که با زور و ناو می‌تواند تنگه هرمز را باز کند بداند که همان نیروی دریایی که گفتی از بین رفته، تو را در قعر دریا فرو خواهد برد.
🔹
دشمنان ما بدانند اگر فکر می‌کنند با زدن زیرساخت این ملت عقب‌نشینی خواهد کرد، اشتباه محض است و این ملت در این ۴۷ سال نشان داد که خاک می‌خورد اما خاک نمی‌دهد.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.86K · <a href="https://t.me/akhbarefori/653313" target="_blank">📅 23:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653312">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
احتمال اصلاح برنامهٔ توسعه و بودجه ۱۴۰۵
🔹
رئیس کمیسیون زیربنایی مجمع تشخیص: باتوجه‌به شرایط جنگ در راستای اصلاح برنامه ۵ ‌ساله و بودجه ۱۴۰۵ بررسی‌هایی انجام و پیشنهادهایی آماده شده است.
🔹
همچنین جلساتی برای تهیه پیشنهادها جهت تدوین پیش‌نویس سیاست‌های کلی پساجنگ برای بازسازی و اصلاح برنامه‌ها برگزار شده است.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/akhbarefori/653312" target="_blank">📅 23:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653311">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">♦️
از کنار داغ‌ترین خبرها و گزارش‌های امروز ساده عبور نکنید
🔹
احتمال اعلام توافق نهایی ایران و آمریکا تا ساعات آینده
👇
khabarfoori.com/fa/tiny/news-3216395
🔹
رمزگشایی از پیام مهم سپاه به آمریکا
👇
khabarfoori.com/fa/tiny/news-3216611
🔹
گزارش جنجالی یک رسانه آمریکایی درباره رئیس دولت نهم؛ دوران گذار با احمدی نژاد!/ ادعاهای عجیب نیویورک تایمز درباره حصر و مجروح شدن او
👇
khabarfoori.com/fa/tiny/news-3216619
🔹
عکس فوتبالی شکیرا اینستاگرام را منفجر کرد
👇
khabarfoori.com/fa/tiny/news-3216595
🔹
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه
👇
khabarfoori.com/fa/tiny/news-3216539
🔻
ویدئوهای جذاب را در آپارات خبرفوری ببینید
http://aparat.com/Akhbar.Fori</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/akhbarefori/653311" target="_blank">📅 23:26 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653310">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tno-s0DuRgdZAvnSDbc3MBT_EtY4goIYCQKeo6u2Nk13s5B3T3Y-ksWg7cgTm1wKnOokDhMZDIpHDq1MNR_QPmcxEtGu-tJqShHlh5pM6yAnYxEqWFv8yv41IfvEhDBWoRCZQMH4yQQWp1l1cEUvkasDSzNHigDPnyUC5b0yrcBEalFe4nC321iUU75oT8vmDSr-Athee76OZg4qlaEZOpj0UNdvoaxX7i-Uc3P-dvYkH0Z4uoCSvOi25x5Zt18VyIKLyY7oivavhBdolTfLe0iljoScI_-D1pA5j7mmfR_vKyAhc2uMKxk27SKyo2CJVMLr3PXHqX80uLR0FehNbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
رکورد ۴۲ ساله شکسته شد؛ سقوط ۱۷.۸ میلیون بشکه‌ای ذخایر نفت آمریکا
🔹
آخرین آمار از کاهش بی‌سابقه ذخایر نفت خام آمریکا حکایت دارد. در هفته گذشته، مجموع ذخایر تجاری و استراتژیک (SPR) این کشور با ۱۷.۸ میلیون بشکه کاهش مواجه شد.
🔹
این رقم، بزرگ‌ترین کاهش هفتگی از سال ۱۹۸۲ (اوّلین سال ثبت داده‌ها) تاکنون محسوب می‌شود./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/653310" target="_blank">📅 23:20 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653309">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f94115f3.mp4?token=I2sZcE46KtLXVbH8KUQsn8gx7cfuCGC7Gt2Xql4wOPBSYZkTKbtLXqRQJXG6UQPQe1G3myeHQRuSQcxJIzb2TRVoBGcQkKmgPDETRWB2kUWe3c01lgkliYx4WHlNrK4dof4L9rccAH3FL388Inn-MAouY_Ce2DObLpXYuzHQDUnChdwYRHcshjJMweRL6DVoxNLX4iJX5z379DawW9ynRgzR_pm6tCkmN4tCv6UjwULE7BbIzpqmG9Tg5-KOApby693h1odlMdQwOW4oRKFlSHXOV5ruAo9o4w7PpqSo-t96lZh1A3nypQNg3veaidhbNmurdmt82pQUTx1r4FtZ5lSxfKmpeU-lUb_4opC-oE6ZcB6hNq8y_hdw0GqIdXnOs33pm2tllB7BT7fc_PnlpsXNCnsnvNbCSg2AieOokfy_dyABME6cpnRVhx0vNVdBZ7yixnmFQrc0eKh2Hv0N4mQLOvBsXxJvzBo1NQDr2FcARqcMdHxzX99NekhYk429QBbP8442saqQYtxqHWz9cc__IlNGY7Lnf_Y9YSb8uoUPI_D1Rxn9mS8PoBKh8rCWMyrliOtp1UBTXdbv5cUuL8KlMwqpQCiuGWnkEAK9g0M85p3G2nNevlKKyyIzm3Jd47sa94uo9UOzjHXR6VUTkAtQdQw8Ra_m2RKWWn8f9rg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
با پشتوانه مردم می‌توانیم مقابل آمریکا و اسرائیل بایستیم؛ ما آینده خوبی داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/akhbarefori/653309" target="_blank">📅 23:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653308">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X1xnmIcde9g3h73P9Zse3Ly-Y3zO0Q5RRuEbV7MWiSVva1KlSoU7HMQnN5Lxvde5SDVYGVE_SjckNPA-zNQh7h2hUbNPqdJMeOZHSZ116Q_dbHsWg5bPe41E9pdAONqQGt9MjRQmrXzUX7UcGevLWaxuXUAHkg4CYORyLKGOP-TUU-Qco5DuZBEFhC6I0ZgWiIolHHyjee69SJ-Cwg-JKS6IEd6AMPSMK2InMVEUaRTEPGNq28kfmIONyH0_zG6YpAwaP5yqBOWEuNrZt4Jgm9FePSiK_9itNarZSb8Q10ydhWwg7hOT3_TayDRco0LvuVb7PF1mCNcM5BjC68ikgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
پیشنهاد تمدید خودکار قراردادهای اجاره‌خانه روی میز سران قوا
🔹
وزیر راه‌و‌شهرسازی: پیش‌نویس مصوبه‌ای شامل تعیین سقف برای افزایش اجاره‌خانه‌ها و تمدید خودکار قراردادها تهیه و به نشست سران ۳ قوه ارسال شده است که در صورت تصویب، بلافاصله ابلاغ و اجرایی خواهد شد.
🔹
تعیین نرخ دقیق در استان‌های مختلف برعهده شورای مسکن استان‌ها خواهد بود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/akhbarefori/653308" target="_blank">📅 23:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653307">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">قسمت بیست‌و‌سوم - پادکست کافئین</div>
  <div class="tg-doc-extra">بهرام چوبین</div>
</div>
<a href="https://t.me/akhbarefori/653307" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🎙
پادکست
#کافئین
🎧
▶️
بهرام چوبین؛ و پادشاهِ شکاک
🗓
وقتی در سازمان یک نیروی «ستاره» داریم، چگونه غرور کاذبِ مدیریتی می‌تواند حکمِ نابودیِ کسب‌وکار را امضا کند؟ و چرا برای یک نیرویِ متخصص، مهارت‌های سخت (Hard Skills) هرگز جایگزینِ سیاست‌ورزی و درکِ قواعدِ بازی نمی‌شود؟
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/akhbarefori/653307" target="_blank">📅 22:59 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653306">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cd95c8661.mp4?token=dXs55NQccUDUO95_Jrx86Fzxywyx4i7P74xkrb74omHN09iKU_lRsGUrbVpt_b651CdUCRcn7_XNtJoUF7qPViuVkyr7G8OE4-b8zjzt5CIXkW5MSD19JQnnvctVU0jykGomGZjVJ7zJr8OjVCCYNh2OlpJKthDBLuuxnAKIfNwQK6GD2NqiUoy-KRMMIGRUwmCim4kWYtOG5I7M9Ma1Rv2Bjv43-JtcfhefCENRzP5qRJaAFICoNofhEUqQ5uAjoah5zybYOHZQYwKridmkFOMGWkERvLwTgWWN4GueyggQkfK6LQmq_GFSfkfOyfpg7to5Y78mjgGlGLRbNuxejw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهرام چوبین و تراژدیِ مدیرانِ کوته‌فکر
#پادکست_کافئین
| قسمت سی‌ام
☕️
در این اپیزود به سراغِ سرداری رفتیم که تنها با ۱۲ هزار نفر، ماشین جنگیِ یک ارتشِ چند صد هزار نفری را در هم شکست، اما قربانیِ ناامنی، پارانویا و عقده‌های شخصیِ پادشاه خود، شد.
بهرام چوبین ثابت کرد که تحقیرِ یک نیروی نابغه، چگونه می‌تواند پایه‌های یک امپراتوری را ویران کند.
هر روز صبح با یک شات غلیظ از تاریخ آمادهٔ شروع روزتان باشید!
از اینجا ببینید و بشنوید
👇
https://youtube.com/@caffeinepodcast2025?si=yIYlag9mUMtn0O8D
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/akhbarefori/653306" target="_blank">📅 22:58 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653305">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TgIOfsouFE6Qtq72nFqxSXG3YdNGiJ9Ahy0F5y9N5M886qeqT1s970X5g9abtK64doqzzAfbDkp760Dbs15__3STkpLfjzzo2qgeY-2lHxwGonlHg6X9olUqs63d7C1kIr0iDOHLO77vGryag0AEeybLKeKfTBsV-vGNCM5CpTGr8OlbjIyGXmaZet4MLY8J-M6UDnzgLRDc6F0OPqaJWbjPNiclH99j4izT4QkmG3P00zEMpU9EigH6RnE2THGjDN8E4nI1r2db-KxWH8-strH2rZ0zQQNKN2D12Zu_yijp6KOdieXt2AXAyheQYrEeRrMGSai2HCdiT9OjnqG81g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مک‌گورک: سوال مهم این است که جهان چگونه می‌تواند با بسته‌ماندن طولانی تنگه هرمز سازگار شود
🔹
فرستاده پیشین آمریکا در امور خاورمیانه: درباره ایران، سوال کلیدی دیگر این نیست که این وضعیت چه زمانی پایان می‌یابد؟ بلکه این است که جهان چگونه می‌تواند خود را با بسته ماندن طولانی‌مدت تنگه هرمز تطبیق دهد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.64K · <a href="https://t.me/akhbarefori/653305" target="_blank">📅 22:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653304">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a6ed86ac2.mp4?token=qAo8VawF5fc_TSAA0I7R9GfJE9KYYoFery6Di-DIH889jrnQIzy89z3X-7qQ77PmYiTNFwlcERMc2n9WJRehv9OkbpdjRZHL1ngDmCYnMnXYAbVcFF_3hWmdqeoqZ1oFqYPozei8EioLWgLtLYeuV2R3nWd1P7II1nIzCQKVB0NNwDj3Swpi9KxVa3Qet89b-V_D5O33e7ZyXqxVQxR2zwenfia2FNMAY0TOJVUorP41tQYIQVa3mdusPAHpUSAqsPee9lYY5AbANLu_VhL1nJ4vWJd_NaQ_HjUvmddI-BpYdkMdwxNC8elUFG_RKwWbOq25ucJwOQs8-RSJjSC77w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
زاکانی: پشت سرمان بمباران بود اما ما به آسفالت کردن خیابان ادامه می دادیم
🔹
آمریکا نباید احساس کند که می تواند کشور ما را به کشوری جنگ زده تبدیل کند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.68K · <a href="https://t.me/akhbarefori/653304" target="_blank">📅 22:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653303">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5H2tpZfzoeHHqaTORzTddr6-lxrf2g1ct2bCuFOO5QqBVVEVDDVLHvD4-_tJ8XcYZOnIMLlS4bAS-sHn_VZsE6ViE7xCKGSNik6zmBAXia_fAZpcQI-NPimOXg_U7QzHOSU5oDZKK5u7PWKIwZdD14JWKnYCXWVcWgXS_H-lirOGnyXdE-ZSlGAkyLiQbclTtycMTgan4G_yLemuVY2QN4Vqt6eUYYqr63Cbyk8jMRgYZmdMP9aq6Wk7a7WlNWkAebNFZq5NohC6FLOWtYP3QC_tOLmPUos0LVi7W9VlHn-SGQ8Nrd3XtukIB3G2pyL8zZVfvBVjr7ypPjEwWZHKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
جنس بدنه گوشی‌های آیفون تغییر می‌کند
🔹
اپل قصد دارد از نسل بعدی آیفون، تیتانیوم را برای جنس بدنه کنار بگذارد. منبع این تغییر، عملکرد ضعیف این فلز در مدیریت حرارت است که باعث داغ شدن بیش از حد دستگاه می‌شود.
🔹
در مقابل، نام فلز مایع (Liquid Metal) به عنوان جایگزین اصلی مطرح شده است. این آلیاژ که با ریخته‌گری دقیق تولید می‌شود، استحکام فوق‌العاده، مقاومت در برابر خوردگی و انعطاف‌پذیری بالایی دارد./ خبرفوری
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.32K · <a href="https://t.me/akhbarefori/653303" target="_blank">📅 22:50 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653302">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACzsjStI2mOh18Rt_i0TP0DEkZCOPaHETyAW2NXlnFMN2UgIaKWhG_qE7PgN58kibJHIOxuDIbn8D590ye7kmcfIW8bwUbNbAa1LNezNyhhJTzRaRsmhg0XTHJwKCj2Ejfb8i0fT4_c2R4tzz8ZEBKbmzTSsxxoAv5Z1Uoz_uw6-FpLiXpblJ6ztCSl4tRwpqSMzqKMbL7EhotMF2sb6wUzlflL1VT4lowSNvXPzs_7vN23qiLPgnnqkbq1YcYCqxCDhrs_wbHYuHX6EZnqb7Wve7Mpbfb0J6M68JvHIAMQdYsHaiXn_mmEZk8ljaAXpL_Bw2RrKUpTEvOtsGgJp3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
سردار قاآنی: پیروزی‌های ناوگان صمود ادامه دارد
🔹
دیوارهای تزویر آزادی های تمدن غرب را فروریخت و فاشیست صهیونیست را بیش از پیش رسوا ساخت.
🔹
فلسطین را باز به کانون توجه جهانیان بازگرداند.
🔹
رژیم صهیونسیتی مغلوب را که به تشدید سرکوب و جنایاتگری دست زده، سریع‌تر از قبل به نقطه پایان نزدیک کرد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653302" target="_blank">📅 22:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653301">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">♦️
واشنگتن تایید کرد؛ سقوط ۴۲ فروند هواپیمای نظامی آمریکا در ایران
گزارش جدید سرویس تحقیقات کنگره آمریکا:
🔹
از آغاز جنگ علیه ایران، دست‌کم ۴۲ فروند هواپیمای نظامی آمریکا از جمله جنگنده و پهپاد، منهدم یا آسیب دیده‌اند. بر اساس این مطالعه، برآورد هزینه وزارت جنگ آمریکا برای عملیات در ایران نیز به ۲۹ میلیارد دلار افزایش یافته است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.67K · <a href="https://t.me/akhbarefori/653301" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653300">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">♦️
فرماندار جیرفت از کاهش شدید سهمیه آزاد جایگاه‌های بنزین این شهر از ۲۵۰ به ۸۵ لیتر در روز خبر داد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/akhbarefori/653300" target="_blank">📅 22:35 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653299">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
معاون بنیاد شهید: حقوق فرزندان شهدا دوباره به حساب مادران واریز می‌شود
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/653299" target="_blank">📅 22:34 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653298">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
دارو داریم، اما مریض نمی تواند بخرد!
همایون سامه‌یح نجف‌آبادی، رییس کمیته داروی کمیسیون بهداشت مجلس در
#گفتگو
با خبرفوری:
🔹
متاسفانه مشکلات دارویی کشور رو به افزایش است که دلایل مختلف خود را دارد.
🔹
قیمت داروی پلاویکس (مورد استفاده در سکته و جراحی قلب) طی ۲ تا ۳ سال از حدود ۷۰ تا ۸۰ هزار تومان به حدود یک میلیون و ۳۶۰ هزار تومان رسیده است.
🔹
داروی ایرانی این دارو با نام «اسویکس» در حال حاضر در دسترس نیست و فقط نمونه خارجی در داروخانه‌ها موجود است؛ به همین دلیل با وجود موجود بودن دارو، بسیاری از بیماران توان خرید آن را ندارند.
@Tv_Fori</div>
<div class="tg-footer">👁️ 9.22K · <a href="https://t.me/akhbarefori/653298" target="_blank">📅 22:31 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653296">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/758abff899.mp4?token=hwZ78iMtsIZVQVWzHkl2LV888yvE1S61Mo22aeNWBN2SClXRarbQeoOOJRl8VnQIumsgT1bC7f444enDgnbJwI9Fbre92PCIz06-KrUi1r0S1xsPt24J6RMQ8hFS_5FBrgzKLNNtbsRK1TZITxnil5VyaEYN3m5z4McDgkoE2kCLfwTePfLDua66afhnX4s8d21u6Xc42-uvlpLlMLYIHNSszLg3UDpPktDKI-ZX6bV7XZL83KZ7TfKPe6yfMYVTppcBnnaP4WmCVeAbay5uJb9KczH2j8-dF3w_8ztg3rnL0Q7UcjMl8F8lIdpfZszjND5PeRjRp-x6EH6rRJUX439XF7L1LgZq_IwGY2pzTx-U0ppwFJm2FOvMjqQKCzZ35H4hWYSOG-Z7yj74Ck7YWWS_kWxCx0oZAomNtdjiRy9AsWQMaDFvf7e2Chivqk0pSso1f9_OFDn-_gz8kdeTk7s3C35c-5GjWZPi2cYvxw-5_u9HrSGmWrHcbbfP6j-a13kRdHl9c2-1SlC_ZvxBHRW4BGU_lhUJ3CMkpcVnIlXLozTY6fr2JTJCAPFGrZeDCBPA57c7pDTakMqHX2k3xW1FTT3IrA9oeVTOs0Ndcet_M3KIWYDz8z72WEuQUFrvr95yznsrcp5q6mLsGzB39NrFR8YOERuffl9T5h927c8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عقب نشینی‌های پی در پی پس از به پاکردن آتش جنگ بی‌محاسبه؛ این حکایت حال و روز رئیس‌جمهور آمریکاست
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/akhbarefori/653296" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653295">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">♦️
سه پیشنهاد برای خروج آمریکا از بحران ایران
🔹
یک تحلیل راهبردی در نشریه The Hill اذعان کرده است که آمریکا پس از حمله به ایران، نه تنها به پیروزی نرسیده، بلکه تنگه هرمز را نیز از دست داده است.
در این تحلیل، سه اولویت برای توقف بحران ارائه شده:
🔹
ائتلاف بین‌المللی برای بازگشایی تنگه هرمز با مشارکت اروپا (قابلیت مین‌روبی) و چین (بزرگترین خریدار نفت ایران)
🔹
احیای کنترل تسلیحات و میز مذاکره با حضور آمریکا، ناتو، روسیه، چین و ایران
🔹
گسترش پیمان ابراهیم با پیشرفت ملموس در مسیر تشکیل کشور فلسطین و گنجاندن عربستان./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/akhbarefori/653295" target="_blank">📅 22:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653294">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B2pwg3b55BpTC6pLc8NAK2kSKAoBUcoSBBijmiceWCmDpq7YfblhiKbnuXhOQ6DN9y5hcVR2azd0u_kMhEZmjYwQxBUt7a3LAEtky97DB1nbSWKhJMOmLb4-u8_bgQf_dXmNSI8AUu0I6rcI0av8jz-rCu3LPSEiVe-MyAj5QNZW1rfTWdaQ6sRtO2GmyokSC3gECzFenM23GogunOPUB9p0_1OiR437X3wK_n80HFEY4AHtgt_mafHAMaimrJlLFetq-gUuZB2Yzq1pOSfx-1egUVVoRKfqQ7sjATCt5RQGLmNA_mfr6cFZdkpQsv3udUIr3Gs5L5YWDwD6wQXjtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزت زمانی؛ معاون سازمان تبلیغات اسلامی در نشست خبری پویش «جان ایران»: پس از انتشار پیام رهبر انقلاب، تاکنون بیش از ۷۴۵۰ گروه مردمی در لبیک به فرمان ایشان، حمایت خود را از پویش جان ایران اعلام کرده‌اند و این بیعت مردمی پس از جمع‌آوری امضاها تقدیم ایشان خواهد شد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 9.09K · <a href="https://t.me/akhbarefori/653294" target="_blank">📅 22:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653293">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9052bbd568.mp4?token=LK1ZYof7Cv85mSKBCoel8uYzklJLOVr36vvv5Y1_-CpZBsA0mBsDUPft1WTdWoYH81BK8iv9X-IcqQuqwcucI3EkPNcqQLE-J_IRAZ30y8K2PciBYyk1-fG5FPE1lFB_xmuxQL1jfh0n91XU3yG-yHPwfepYtms_-45ebaTc66tuSpFXarlyLcKKImLLOT0AOoIQkd15nUwvdJPktZPyWsG96pMe1I0L9afwABoSAeTsqt7eRv3rSoFxHerrCn94fItnoZjyE1y330sAPA83pFGedR9Kg1h3xwovuFtfuStiJEEDMojUT_b0Ifn2FEDla2e3PbJgmDAHhHZwLAKBBRHLPoLH04loUZF8gaGuS6xNq7rchWU4asRshx8rQ-pNZ04xmxWq1JKZ3wOKUkmrz-efMql5T-WFpx5xqr0R2p6ZZ50XOJ25xCv_w8NkTHDR7h2wc1gqHY7u9Jn09yMy5DLd2e3KC0gg2dpuTaonLcFln0qp1cm2sznqlvVJzI2twhHCGUDSVlCFmTXo0VCMzXG-O5Xd8W7rGlm6dcgit0DsniXIFKm7n8o8_Cw_kAUKXCbJWXnxSiCJ1nTAaBdX1i3EgNlj5sJ2LpPVXW2uKpRZ8HB3rbknpXmFSJ2rkSN0ZFGqZfU16FB3CWA2n3kK0hmP2L52XdHSl8sjnRTxPO0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">روایت شیرینِ مادری که ۶ فرزند دارد
از سختی ها و خوشی های مادر بودن در برنامه «جان ایران» شبکه سه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.85K · <a href="https://t.me/akhbarefori/653293" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653291">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سخنرانی استاد رائفی پور</div>
  <div class="tg-doc-extra">مراسم دعای ندبه_جلسه 52</div>
</div>
<a href="https://t.me/akhbarefori/653291" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">♦️
مراسم دعای ندبه - جلسه پنجاه‌ودوم
رائفی‌پور:
🔹
0:07:20 تفسیر ۷ نام جهنم در قرآن
🔹
0:19:00 تفاوت عذاب گناهکاران در کتاب تورات و زردتشت و اسلام
🔹
0:41:20 ویژه بودن اسامی اهل بیت در حروف ابجد
🔹
1:05:30  تفسیر ۱۱ بخش خطبه غدیر از ابتدا تا ظهور
🔹
1:46:30 بیعت با حضرت علی (ع) ۳ روز به طول انجامید
🔹
2:07:00 چرا یهودیان در قرآن لعن شده اند
🔹
2:14:00 خداوند حامی دشمنان صهیونیست هاست
#دعای_ندبه
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.99K · <a href="https://t.me/akhbarefori/653291" target="_blank">📅 22:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653290">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
تروریست‌های سنتکام در اطلاعیه‌‌ای مدعیِ تعرض به «یک نفتکش مرتبط با ایران» شدند/ نفتکش بدون آسیب همچنان درحال حرکت است
🔹
سنتکام در اطلاعیه‌‌ای، مدعی شد مسلحینِ این گروهک تروریستی ساعاتی پیش، وارد یک نفتکش حامل پرچم ایران شده و پس از «بررسی»، از آن خارج شده‌اند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/akhbarefori/653290" target="_blank">📅 22:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653289">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">♦️
اکسیوس: قطر پیش‌نویس توافق جدیدی برای کاهش تنش‌ها میان تهران و واشنگتن ارائه کرده است
🔹
هیئت دیپلماتیک ویژه‌ای از سوی قطر در اوایل هفته جاری برای پیگیری این پیش‌نویس به تهران سفر کرده است.
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 8.01K · <a href="https://t.me/akhbarefori/653289" target="_blank">📅 22:00 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653288">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7d5bde06c.mp4?token=VBbdVhyQl6IFKRH0fzRENG4NWqR_ttjFgCIp0Av3zS7M26yjyli7kw9SslzIrYHFRjQcgvDR6g87niJVkA6aNzVi4dw3_PsY1QUoLNcmrwXJU-LHqXipLl8R2CmOKKHYYaOFpThD0Cu6quUOvEIhtmSLMpE08LKsns0t_heLkqMY_r0FtP18EbqkMYmXSjY4mlaj20WvQOpx8sQbqkUYZsxy-JqpKTu6iznUrQRcbMygWgcFguUsIgFm_XmBEUTsR5uHaFb_hm69hx8e3l96LIiuJAsQG55SzDv9eaCYB62I46UzgNU30BaM-AMoJb7uTh7-9DgJdK2Ko1YvTTFsLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
عدد واقعی جمعیت ایران چقدر است؟
🔹
تازه‌ترین داده درباره جمعیت ایران منتشر شد، نکته حائز اهمیت تعداد افرادی است که در سن ازدواج قرار دارند. از دیدن دو عدد در این بسته تعجب خواهید کرد!
@Tv_Fori</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/akhbarefori/653288" target="_blank">📅 21:55 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653287">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eao8ME2m2Uz60ngKrAKaZGPXuGzmrxDwvZnkpXlBX4UJ5JhxHbtKfPDtcclqudZJYcUq-DTpS0ZtIC5ZQ262UwfyAJD9IApmpqEzsVMA3oHSixrl3eftVCDBEXlkVtRL1h1MbSc_-44UjfHc94UuIBk5L9rGTuJnUyzb8GJiQwxSabWIOev6QNjjSyoB14yZoxc9HppmvGbkFzwtMc9vewdR-eWOCrzrkvhfvNu0JWH2b3RFNU0Oriv7iBxHAPiukSLKPkCVN6FQfr0lMBxS-oZBvGaGFoXFr5rem-ZJBisE7BFexW4djaZxPc9YlGIlXQOs9xZv77CP2jn7n-vwSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
استقبال متفاوت پکن از ترامپ و پوتین | پنج نشانه روشن از دو نوع رابطه | از صرف چای تا موسیقی پیشواز
🔹
چند روز پس از سفر دونالد ترامپ، رئیس‌جمهور آمریکا، به پکن، این بار ولادیمیر پوتین، رئیس‌جمهور روسیه، وارد چین شد و با شی جین‌پینگ دیدار کرد.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3216539</div>
<div class="tg-footer">👁️ 7.74K · <a href="https://t.me/akhbarefori/653287" target="_blank">📅 21:48 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653286">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66d570f341.mp4?token=srdhxH44Z0RGRWjLMLCaAoXCckMp6cBxjMjK4KvamRe-4nvFND4VyNcEnUWqHM1TbG1HfI8UKsZ8qIlNRm6fUkTq2cxhZNcmxW7-qc7OdnW_sxtkOr0_YdTNNlrFnq-N802XOi3wxMoxdGftzYelMgaLf1yQa9TR9dk9XriB5KTiy4EKkfh-jhsj_J0_XXTd142qBCkv_s1rcwccahFAI1uJJinQdHRm3v2CtubmxTT8A-sjjrUF86aN_WEofKgCfoxqG49x41f_ubIuODyA3dSecqGZxwza8DrxIRb2ZqgS7s6w2UVKfThK1hEn79WhKyPPzFmwLyljqgwkC3ut9rkrbrQlFD_akVSvJOQ3cgMZ2N2bSiuesHc2EvJ4pcz-QyVL3jAPIvIcZq9RRUq1fpqhDzzwAp6rs0Prr70v-mRCLMkq8Hf2T_wcWXTY3Qc1NStAEEjCCY5So3fxFvrgJ3G5gJiHsJV3SLq2vKU7jS82X-cMLGx23DkXh1bsA4kFlN3w1ZLfWTO_waaz-zV-hEzqVyKNnPd3eYFALMyP9d5DtSMCxYTcW8o7swxEbjT5_C2SsDvn1yrIO7jnOAOveEwbJoJLZeNwccBl1_ffKcyZf6Sx5D-Az-HWfJralqiNJooiw5LAXKelbOhhzySR87uHtzF4P2X62LofsxpaPq8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گفت‌وگوی تلفنی رهبر شهید انقلاب حضرت آیت‌الله العظمی خامنه‌ای رضوان‌الله‌علیه با همسر شهید رئیسی، پس از حادثه سقوط بالگرد
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/akhbarefori/653286" target="_blank">📅 21:47 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653285">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a05e0804ab.mp4?token=Mk4SKdzma1-j6n7qFDPAClhqKuVIBkjIvoNkkViW5Onr6YHOJEYoF_OauPX7yEpoIOC0jwk8MuaZBaqMEHq_MgtCdyZBOnUfPfNfsE6i10bw6RtnzhHhNbhIAlryEoLb34_Lz_tbcNrJ7qx_-MLrx2Trppa1076vILch5hF02KOEdk9n53QOqZYSzOhufV7ZY3qdHH3yTQrR33dfouQywrJxnaoBrsxsENBlNsovXi6i2EgY56_DISz6OsHm6IZh1UfArwDNx7M84DdU1WIP6VSjvtCq6ipaE31yApQbNJlkhIfWc4uPVZJHFvo2OpEBB0trfL6krhvEkPWkBUyuTQENavylVoXSPeS76HPGNMRSRZ7EIubwF7JWUBfIoMIZI_jPn_6wXcHoO1v0kz8qKVt_94P9qbG7Xod-qN5eCDDBJ6n53uqdNsI-ChciWyzkAnHmWH0kCQRxD5vZq-HVVO5pmZP_pLma96YdbA1ZCSePRpBlabLmBoYxHy9GePE3tg_tzUGgJC0_FxD0VY_7oydalT3UqQISXhirc-7F18-V6Q0fu_F4nI7xB4TS1kr9lHi6Baw_zCgkbHU7eF7vEyi1EjZGiaHPw-NFcGbsMuRl4Cycj9kglylD-depEV-JViGvI8QJWneggEhv6KegLj_BJ4vI5Xln3Sz7z_xY2q0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظه‌ای که این خبر را شنیدم...
🔹
در سالروز شهادت شهید رئیسی، صدای مخاطبان خبرفوری را می‌شنویم؛ روایت‌هایی از لحظه‌ای که خبر شهادت شهید راه خدمت آیت‌الله رئیسی منتشر شد و قلب میلیون‌ها ایرانی را متاثر کرد.
الوفوری را دنبال کنید
👇
@Alo_fori</div>
<div class="tg-footer">👁️ 7.84K · <a href="https://t.me/akhbarefori/653285" target="_blank">📅 21:45 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653284">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
شکار دو تانک مرکاوا توسط حزب‌الله
🔹
حزب‌الله: دو تانک مرکاوا در شهر حداثا در دو عملیات مورد اصابت قطعی قرارگرفت؛ همچنین حملات موشکی به تجمعات پشتیبانی دشمن انجام شد.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/akhbarefori/653284" target="_blank">📅 21:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653283">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">♦️
جنگ با ایران ۳۰۰ دلار از جیب هر آمریکایی کم کرد
🔹
از زمان شروع جنگ ایران، قیمت بنزین در آمریکا به میانگین ۴.۵۰ دلار در هر گالن رسیده و مصرف‌کنندگان تنها در ۱۰ هفته گذشته، ۴۲ میلیارد دلار اضافی برای بنزین و گازوئیل پرداخت کرده‌اند.
🔹
به طور متوسط، هر خانواده آمریکایی بیش از ۳۰۰ دلار بیشتر از حالت عادی برای سوخت هزینه کرده است.
🔹
این پژوهش توسط «آزمایشگاه راه‌حل‌های اقلیمی» و «پروژه هزینه‌های جنگ» دانشگاه براون انجام شده است./ خبرفوری
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.5K · <a href="https://t.me/akhbarefori/653283" target="_blank">📅 21:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653281">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c63ea7c9e7.mp4?token=ofBDi_FQ-2K7x9RyMyVSnaqKxnKKQU3rl-esyZ5U3UoLs58enApkSqBXLTut-eCNJY85QIIuF4iuvHdIeUk_ce7sLXw5PEt3V5aKAzf1pGkvYoiyIkT1Uy2b6Ei-cI-xq7w2iHve8-JibBxh3otTzCXRrfG3vZE-FHMhMysd8E9A5I08o93cQ72it4HWtFoc7cGaxcq7kx-c3TI2IbRKoK7fhMx_hDRFe5Id6MolZSrcvBuJnROz10p_RyKamNjMXIbP3Kl_QZqMKhVR_YEHrI_c92TYJGjBiOXKAuWiR0eKV7zae6rF0_oVFfVwyIJfZSMpo5pglbrIkxKRz6OzqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رفتار وحشیانه با کاروان صمود، برای رژیم صهیونیستی دردسرساز شد
🔹
سفرای رژیم در جهان یکی پس از دیگری احضار می‌شوند
🔹
بعد از بازداشت کاروان صمود توسط نظامیان رژیم صهیونیستی و برخورد‌های زننده و انتشار تصاویر آن در رسانه‌های جهان، بار دیگر جنایات وحشیانه رژیم تیتر یک رسانه‌های دنیا شد.
🔹
همزمان با این تحولات، دولت‌های دنیا مخصوصا کشورهای غربی، یکی پس از دیگری سفرای رژیم صهیونیستی را احضار و بابت این رفتار خشن بازخواست می‌کنند.
🔹
تا کنون ایتالیا، کانادا، فرانسه و هلند سفیر اسرائیل را در کشورهای خود به دلیل رفتار غیرقابل قبول با فعالان بازداشت شده کاروان ناوگان جهانی صمود احضار کرده‌اند و با توجه به فشار افکار عمومی، پیش‌بینی می‌شود دولت‌های بیشتری، دست به این اقدام بزنند.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 7.04K · <a href="https://t.me/akhbarefori/653281" target="_blank">📅 21:37 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-653279">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573359b1bc.mp4?token=N85IgcYG_VHYaufh-m3qeM5-IFb8KqO_cAZTSdT0Jt7YQGoLC0JMygeXUSx5Qg94vK8x6nJUQmNJNjvm0DFy9B3gibrImM0Z4gBcbsM6gc7dLOcVSLBhrl8oP2IE41ykhZQ4eXTR1f5ij--D_0EM9LjesEPeYHW1aTgtS8HFxW-N1Z5J6bB__1sV9uDxRgbMeYY-lCS5HHWZNagRF4HXjwTsAE4H1FUFq8gmrv3Xve0WIIyWMmSmMSffjTRUX6fEbFTyhie8eA6g74iwhXUH6SwNUH_UatFZ06FwlEooJn-RBGpj91ub9C8uleQ7jBlvnS9cNhMlB4y4_e06BTHmvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزیر نیرو: معادل مصرف چند کشور کسری برق داریم
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/akhbarefori/653279" target="_blank">📅 21:35 · 30 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
