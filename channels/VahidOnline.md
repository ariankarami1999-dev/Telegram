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
<img src="https://cdn1.telesco.pe/file/iNJq6HRv1iSh9syM0L2i4vFiqmQcSCKhVWbtLGsijnwbmG_AjurnhsxAQAPlOBVZ2nhcrl153S3q5eKl3ERkqhEUs2ablaVfmcTW1KKMidqNIpFW-_69-ZPILirI2muPOagoT7p0lj-IGBVXv2l1Pyi-lhjf_a-OEla2KkqebA9IbsAFga4K2-fR_bwuujT8LManFk68jFJRsdDJmnC2oyuI0SvKNtvf5qpliBPMpcvtdLF6f1hGDG3xpbB_WNS_eGZDSsyu02qCJWL9A2vaIEcEsDO9Z2vRzG2D8yruYkdycTXqC7hiTq4111aTTpRBNaXnSg03TMNBCIUkq7mpgA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Vahid Online وحید آنلاین</h1>
<p>@VahidOnline • 👥 1.35M عضو</p>
<a href="https://t.me/VahidOnline" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ارسال پیام:@Vahid_Onlineinstagram.com/vahidonlineتلاش می‌کنم بدونم چه خبره و چی میگن. اینجا بعضی ازچیزهایی که می‌خواستم ببینم رو همونجوری که می‌خواستم بهم نشون داده بشه می‌گذارم.استوار بر حمایت‌های مردمی:ماهانهvhdo.nl/patreonیک‌بارهvhdo.nl/paypal</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-08 20:58:30</div>
<hr>

<div class="tg-post" id="msg-76746">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8thB-H5TYNNu7Dt21rI6zLRpAmmsbn7hkud3lt8hO8r7qam4tw9Iur5fs1tA32c1CLTCxQE-GoIwvydtFMSJ_JpCG-9mn9IPLw3SEJeDW86uw_bSDRVicMXQ3Ljye7EQeKB6-CqNUKNnB53gGZXYBv1tOj1eh8B4l1w1XyuXhhZBOlyMTjTjiKvqMRoOls8WdAEjU-5EvvjD_k0SMFTO8hNB-053ZXToah35lyOTccc52qoUogPluk7-IEI8PZpJCc1grr2FT9nNqqZ_1iu0iocqXIpmpF8zGxlchX0ARPYQpI61hv21sCh4clLR47LqI1yLiLqkZLzfLxua9HFQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوسف میری، ۱۷ ساله شب چهارشنبه سوری در خیابان حافظ اصفهان با اصابت گلوله بسیج به سرش کشته شد.
یوسف میری سه‌شنبه ۲۶ اسفند ۱۴۰۴ هنگامی که در راه بازگشت به خانه بود با مادرش تماس گرفت تا برایش غذا گرم کند اما پیش از آن که به خانه برسد با شلیک گلوله به پشت سرش کشته شد.
یکی از دوستان یوسف به ایران‌وایر می‌گوید: به مادرش گفتند به اشتباه به پسرت شلیک شده و اگر جنازه‌اش را می‌خواهی بهتر است سکوت کنی تا جنازه را تحویل بدهیم.
دوست یوسف همچنین توضیح می‌دهد: مادرش مرتب یک جمله را تکرار می‌کند که بچه‌ام گرسنه و تشنه بود می‌خواست بیاید خانه شام بخورد ولی آن بی‌رحم‌ها نگذاشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/VahidOnline/76746" target="_blank">📅 17:52 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76745">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Az7brEX0nNzt3N1-r_sf_3kvyxeaZTdNgtF7ncNJR2oazrxb-iPKtduAgphuXwX0vIyx9gpIjhpBMDW5357lRJvindmM4xBQL6EJ9jzbZyq70Y_zeLsQ3PcB_TghZjpgk14L4VbQ9laUr2Tk1WGaz3Elq99FJ6CeipFCR2kI-KuTuC2mEQjDCeV1g7S7P1Zs6gq9pM6lMq9WUTxhUkZacW_1u-4Tfgv_yguwC3D_hHbK0BslLdDkRHx4b7eH8JjQ_KlgMbJJgtn7SVCO-zbnSbhBcpLENS9ObRyqNLtGPt1mTtvzYUslx8R5a7ETdeE5Z9u3Vl9OiM-kL4eYISUsxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدر البوسعیدی، وزیر امور خارجه عمان، روز دوشنبه در گفتگو با رادیو مونته‌کارلو بین‌المللی اعلام کرد که این کشور به آزادی عبور و مرور در تنگه هرمز و اعمال نکردن هرگونه «عوارض تردد» متعهد است. او تاکید کرد که اعمال چنین هزینه‌هایی به‌طور بین‌المللی ممنوع است و عمان به این مقررات پایبند باقی می‌ماند.
این اظهارات در حالی مطرح می‌شود که ایران نیز از برگزاری جلساتی میان مقامات تهران و مسقط برای بحث در مورد مدیریت آینده این آبراه، طبق مفاد یادداشت تفاهم ایران و آمریکا خبر داده است. با این حال، گزارش‌ها حاکی از آن است که دو کشور تاکنون پیام‌های متناقضی در خصوص عوارض و مسیرهای تردد در این گذرگاه حیاتی ارسال کرده‌اند.
وزیر امور خارجه عمان همچنین تاکید کرد که مسئولیت اصلی تضمین امنیت تنگه هرمز و پاکسازی مسیرهای کشتیرانی بین‌المللی از هرگونه خطر مین‌گذاری، بر عهده جمهوری اسلامی ایران است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/VahidOnline/76745" target="_blank">📅 17:50 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76743">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/W44LC14yc9y8HRnkIU-XtXIZL671QGXuLwdrK1o7OEEfN0qdAlGrV3soPj-VTxOfDad0vZkQe7g-dxmlH9rqhsIggnkqqdd86VOFJIOj-8Mg-AtvIBe5LiiAv9LS6wMiOEmrYhMzTWNP_oFIeI45Zc4q34Wp7iKaCTGt6nexTJd8sIPYl3vSbz5o59u8Z57c6XM0XMn9PT0C4mKYAKW1MPXumRihW8p97NViHW0DzSSY1EvH1Ozr4_cQxUtHiaRBFrFNdxd88IUPTSFJFQk0hpmUZY13gawD-byZYodT9NwwvVBA2eqPnZaCaKql8YyL8NkzX7RvJytVj5EWMC_g5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/YwNirGljwg2tSdmhz3sCt_ku6aMXkizY0jNdkvvZhXFYu8djWT5aEyCDJfe4opIyprqFDPAkAcqIFbp89Qv-TtVr8qotwSIpWCNruMPGRYiuwZOB9B3YRuDAos2W-YTVfxFLx5d4u_0W6aL8U1dYrh-g1gBto403jXi4rdroJ1Lu32zFSM8TOeJJYmaauZ1GbCx4le9DdhjL7dU9eL_NxbZBx-QQY9tGj2dSm0m1rkW6f1f-2hKvgDAUWUHStDrq_iLLOghVx9T_wLrts5Hd7zwEgxcS_enjFMj1JKoLD5QlN-vhhHHTCO583DbWzVxMrqCcc19Z4CV14ZmrndC6Dw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پست عراقچی با فوتبال، ترجمه ماشین: از زمین فوتبال تا میز مذاکره و تا میدان نبرد، هر گامی که ما ایرانیان برمی‌داریم، بخشی از مبارزه‌ای بزرگ‌تر است: دفاع از شرافت و کرامت مردم عزیزمان. araghchi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/76743" target="_blank">📅 16:58 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76741">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/jFLYVj9n7Kua9T0viJX9W9Jk3oMsVByexLhturDXzRdhpYSt6PYLuYJCHG22qt2rzvQacvVZ3xhIdeWMOn64zqeGTEJg-uPt-PNLuJZ8TF-H2la1ViVk3CcOvpiMxEgmaKY21B2pSjQb6e2m6sJ14MANKc-5-FqjIjpb1Brj-Jn5VqejBXw3djBa-PA_NqGSY2fLWMXUVyVijUWRuK3zlRhDYEoC0jtloR8XE2xbEfFQzWAvLPziYYIPApi6xdCEVeKJMqbI413yAeoX3WCs5p9nXK8ic5BAGTOxachUTZZRL8kRflSi3giouRyZZUKzsmSXi2jQwXs1Sh7cV36Okg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/GCfpbJPD9Mlwq3S__bswimuHXPkId0v-6wghddew7ufJgO2JRQLAaI-HrQmRZKKStZMEwog8pmktOqNTMJ_8tNi1tqtQBl5-yyqR36uViQfjYcAhoBuIrPHZoJ2UnLYeLzmLOZsjkj0Y3yvSJGBmi9qmLrUZLYOSanH4B4A9fb14MfW8k0YAjIp-u3Ot4tfM7gIIrOliGeDvquaLw9-IOJR_xYIpK0Svq8EVTrWPc5N2j25OExJPRUtZ5PGrm9eu37rtriBZR8BR6r4aF-VrqRtfV_-wZDHHSuxRc4gVlFQ7I303IX_91SPmehZIomXHLFmMwwTlriA-qHdYpy2KGQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دونالد ترامپ در پستی نوشت: «ایران درخواست دیدار کرده است. (این دیدار) فردا در دوحه خواهد بود.»
پیشتر کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده جمهوری اسلامی، گزارش برخی رسانه‌ها مبنی بر برنامه تهران و واشنگتن برای مذاکره در روز سه‌شنبه را تکذیب کرده بود.
کاظم غریب‌آبادی، مسئول تیم فنی مذاکره‌کننده ایران، امروز گفت: «هرچند رایزنی‌ها با قطر از جمله در خصوص پیگیری اجرای تعهدات طرف مقابل، طبق روال، در جریان است اما خبر برخی رسانه‌ها مبنی بر برگزاری گفتگوهای فنی کارگروه‌ها در دوحه تایید نمی‌شود.»
او در ادامه گفت که «اولین دور گفتگوهای فنی در چارچوب کارگروه‌های تعیین شده، با فراهم شدن شرایط و پس از توافق در خصوص تاریخ و محل آن، برگزار خواهد شد و رایزنی‌ها در این خصوص از طریق کشورهای میانجی ادامه دارد.»
@
VahidHeadline
«کارولین لیویت»، سخنگوی کاخ سفید اعلام کرد «استیو ویتکاف»، نماینده ویژه رییس‌جمهور آمریکا در امور خاورمیانه، و «جرد کوشنر»، مشاور ارشد پیشین کاخ سفید و مشاور غیررسمی «دونالد ترامپ» در امور خاورمیانه، روز سه‌شنبه در نشست دوحه با نمایندگان جمهوری اسلامی شرکت خواهند کرد.
@
VahidHeadline
ترامپ در پستی دیگر نوشت قیمت نفت خام وست‌تگزاس اینترمدیت به ۶۹ دلار رسیده و رو به کاهش است.
ترامپ در این پیام نوشت این قیمت از سطح پیش از آغاز «خلع سلاح هسته‌ای ایران» پایین‌تر آمده است.
@
VahidOOnLine
🔄
توییت خبرنگار اکسیوس:
به‌روزرسانی: یک مقام کاخ سفید می‌گوید فرستاده ویژه، ویتکاف، و جرد کوشنر امروز به دوحه سفر می‌کنند و روز سه‌شنبه با نخست‌وزیر قطر و دیگر مقام‌ها برای گفت‌وگو درباره توافق ایران دیدار خواهند کرد. روز چهارشنبه، تیم‌های فنی آمریکا و ایران به‌طور جداگانه با میانجی‌های قطری و پاکستانی دیدار خواهند کرد.
BarakRavid
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 166K · <a href="https://t.me/VahidOnline/76741" target="_blank">📅 16:47 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76740">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sUCnjvC4-WCzpvkkBDjr7HRi3ItMNU_bzBMlm8N6YDroMW9-BN33dopvcfU6GW4PEk1PAPmHdI6QnNkPnWs-59oGwz__MCr-Q1S3dJjpHESsPWJ_vV6Tt1b98zLpGlHveJnXIvh7F7CZi3Hh2-CR8TrNm0-223kmqOr_VpObhg0b9MciAULct0HPK-ogvAOM21CpUjV5KdC3GSbFj5vvfv2oR--vuEbYr-IfMKYpo3Qrzkx3P8dej5G7xNC_wZZsopHm-PGPV_yokdhx2W479pA_oK7SbTmHYEmsWeNxPAfRNSRaJHyyytqhl_jATf0n43L8p39x6M5Z7T_LwsEU0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رئیس‌جمهوری اسلامی ایران روز دوشنبه هشتم تیرماه گفت: «براساس برنامه‌ریزی‌های انجام‌شده، شش میلیارد دلار از مجموع ۱۲ میلیارد دلار منابع ایران در قطر آزاد و به کشور بازگردانده خواهد شد».
مسعود پزشکیان در دیدار با شبیری زنجانی از مراجع تقلید شیعیان در قم گفت: «برای بازگشت بخش باقی‌مانده این منابع نیز پیگیری‌های لازم در حال انجام است».
او زمان مشخصی را برای آزادسازی این رقم اعلام نکرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/VahidOnline/76740" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76736">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TkVpeCwIIcxlbrEOosAtiCXwklpMEV5H3ph3DnNyEmgFNUUfoaHY9zQ02tEsaJb1cTvT2fbz4-SjiQPgts3qQepzZNU-8Vl0uGOsVctlzx1W0CcxgxjQSnzHnTp2b7NLsTn7jFq9VwIVY_eFoGHEUTfS7LA_2mJLHciJlTbvOnl-K9fWDFxk5TEfdRFTBvHB8JwNWhkk-O-nPDvySkuxNIhRaX7nYKkZSISjNQRXVMGAK1kMnQTeZtljegrL0q_PYVJ2x2RVJ1Jd9JQRnKR9ksypIyXGDpUv9r4FDAUYYGAn6YA06Q0VWO1uj5Or-owvPbYRFD6c2OjisqxQlBIXew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ez5iOtT-lECtdoQsHFTTMk6VakJRCLkrbKXMxKcblGilx3onAepTwJZLxnHaP04at9ebPGfY9Vo3PMvP6klAUlzmIKjH27O0YqhA3lngl4BLNTgS0Kl8aDaTprvGltDB2jDQ2FZD9NLKlcMadbOt6r_AQxfVov8T0KjzxZ_JGD2sZ28iwwHm7nBb-9vLdxE8ydqeXWsUmKDb_DxpdkIIGoNWrXpyerXSTljyIMX1Haassk995x2KQRncYK6GoD860YsVYAmpJHpb88FocEi7tv-JD_5zbeFDgf5i2d88AdspockzcpFrHoI9VWAiwE-mQutc8XVvGWAmC3e63HioYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VLvK4tSFT_iOk-kfdqlCB8fRHT4Ub1hucQ5qQhSMuAd50VpI_z9BsC-G5mpFbMF0R8tNNPcz1pG1mr6QqzU5ooQy4tDRLvLZaagqQQfPyqNQAx0X95Rj6eVLRkbF-05qEtxwUSr7KbnxwVawbw2denbbf5_V6AW6KHNjb0XPpTNUaRj4Ffk-iSxHkzGEwlghAyEx3tRi4LWE5ptfDj_1ku5AbYwTqEww0D1q264bHymav6qeowR8L4xqqTesVsnDzgZbm7zv6_VHtaKlSN0g2UlUrIgErWJSKoC4bzRqt1BsTdBrB1UjrE4K1Mc0mjh2kjlDb9GJw6YByoEqWHT-ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=nuZxvPmXdUB9kw_Ej2HmSNa0SGU59sV2fPyesc-zh8TOAClcdqLe9tmv53ffHIIJd3OdOsDLCCClwaCaIRBxNRdjiyAV_Y-K6X_SKM2gFwk467lLFpuJo7xX5lwh4mKwPuEu5ODrz5mtgxiaKnm1rx1fsZVEeGsC2u77fd2PoxbMhcKp3rHWi6Z0vxzdIwD7pszAfDw0ViJ3y68uLkBnGVo719XyIO-V0xtDxuYtBjwknF7_pTuhmOmGBTUf-2tYiMOFLN2Xcmg_G8uS2ovaizNKltNh4XEHNLW93ntZmdCVQdHootK5tcafzuYWE2IRpXrOVhlAiPK6wZJ5a_tIVEu4NK9hKNouPS1DTdDOHY911HydOFVZjHEkkjnZQXvpdSRVMk1x8FJDr_7Bun8QBF9-dKz6jBp1pMo12QnLle7WESfFQtSQapcEPgeHH8TMyQBpTDUOGSZ_ajA984-o2_LXTfBQqlUVpZR2ROVI2B_DMwb3L9SoDUm8Xj3-TbTlVIIIBsXRnaQMufe_C5ko6ABCAhz1v-irimI5dKmP1uKkfQHvzCusT1fiP9RJxfOOyJLPJ-qISDwzmwXYq1jj1npq5_RbvCBArnDPModSCNjQb5-ZxCAmVpAPaVxtAtEWIc_RNTeuLnPk3Wc-e8sr6sJxhGwhKlGtsLNYYC2LUiI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b61d44fd1.mp4?token=nuZxvPmXdUB9kw_Ej2HmSNa0SGU59sV2fPyesc-zh8TOAClcdqLe9tmv53ffHIIJd3OdOsDLCCClwaCaIRBxNRdjiyAV_Y-K6X_SKM2gFwk467lLFpuJo7xX5lwh4mKwPuEu5ODrz5mtgxiaKnm1rx1fsZVEeGsC2u77fd2PoxbMhcKp3rHWi6Z0vxzdIwD7pszAfDw0ViJ3y68uLkBnGVo719XyIO-V0xtDxuYtBjwknF7_pTuhmOmGBTUf-2tYiMOFLN2Xcmg_G8uS2ovaizNKltNh4XEHNLW93ntZmdCVQdHootK5tcafzuYWE2IRpXrOVhlAiPK6wZJ5a_tIVEu4NK9hKNouPS1DTdDOHY911HydOFVZjHEkkjnZQXvpdSRVMk1x8FJDr_7Bun8QBF9-dKz6jBp1pMo12QnLle7WESfFQtSQapcEPgeHH8TMyQBpTDUOGSZ_ajA984-o2_LXTfBQqlUVpZR2ROVI2B_DMwb3L9SoDUm8Xj3-TbTlVIIIBsXRnaQMufe_C5ko6ABCAhz1v-irimI5dKmP1uKkfQHvzCusT1fiP9RJxfOOyJLPJ-qISDwzmwXYq1jj1npq5_RbvCBArnDPModSCNjQb5-ZxCAmVpAPaVxtAtEWIc_RNTeuLnPk3Wc-e8sr6sJxhGwhKlGtsLNYYC2LUiI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
مبین یعقوب‌زاده یک سال بود که مادرش را از دست داده بود، زمانی که  تنها ۱۷ سال داشت، در ۱۷ دی ۱۴۰۴، در اعتراضات خشکبیجار رشت، با شلیک نیروهای امنیتی کشته شد.
🔸
سرگذشت کامل او را در یادبود امید بخوانید:
https://www.iranrights.org/fa/memorial/story/-9117/mobin-yaqubzadeh
@IranRights</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/VahidOnline/76736" target="_blank">📅 16:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76735">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=ad5sXKo_BqD47HqlJumKPDKAA42E_gMmZQlJaRSzkCSQEFHSi4qHcNtI5_UbMM_GGtl7e8qiPuj2Lpq0U_c3GeN2gLXTG_EB5ZDraPVtxDQESYZ5bxvuRKhyC0zulfN4CMsCDSmCVy1mv_nBH_1Y98Dou9i_IKo8MitjLAbxGR-CGtwWMYPyI99QoKGOzz9y2QSXenUMhU8lT9K4q2AnBdA_B_4fEGZAPaHdRWGIJpX5wlVYcc5_-ShZDXmDQIUbX3q7UJ7lPM0NnugThX2rXqsBdNJiNECx1nm_2ZCZ-q2tH1tL3EUP9rr9-VEEZ6O9PYKfu1BKMqr07yGEtugXVg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2ac12c0761.mp4?token=ad5sXKo_BqD47HqlJumKPDKAA42E_gMmZQlJaRSzkCSQEFHSi4qHcNtI5_UbMM_GGtl7e8qiPuj2Lpq0U_c3GeN2gLXTG_EB5ZDraPVtxDQESYZ5bxvuRKhyC0zulfN4CMsCDSmCVy1mv_nBH_1Y98Dou9i_IKo8MitjLAbxGR-CGtwWMYPyI99QoKGOzz9y2QSXenUMhU8lT9K4q2AnBdA_B_4fEGZAPaHdRWGIJpX5wlVYcc5_-ShZDXmDQIUbX3q7UJ7lPM0NnugThX2rXqsBdNJiNECx1nm_2ZCZ-q2tH1tL3EUP9rr9-VEEZ6O9PYKfu1BKMqr07yGEtugXVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">(
⚠️
صدای بلند)
ویدیوی دریافتی با شرح کلی: "جنوب کشور، جنگ اخیر"
انفجارهای مهیبی در یک اسکله رو نشون میده.
از زمان و مکانش اطلاعات بیشتری ندارم، لینک یک صفحه اینستاگرام رو فرستادند که نسخه اصلی این ویدیو رو دیروز بعد از ظهر بدون هیچ توضیحی منتشر کرده و پست دیگری هم نداره.
Vahid
آپدیت:
در پیام‌ها میگن خرمشهره.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 313K · <a href="https://t.me/VahidOnline/76735" target="_blank">📅 04:44 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76734">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/TY9zl9n0YPQeZyGBnZBTCPqGMFyKS1v2TzMDCOKvuyLo7RcA_7g9eFLR7bblhb_s5KWwcdAhDYtIf8PNMbS71Kj_llKAj2C5E2c-tiluz8D0lpz3ubVETdYUTWAF7wDoBJ8NzBEyEEowptS5zvR3SjwqYL26akt12x84bxE8kOUgBV_CAJJhezUFbP1K3GqEpw-kFaE8xyUMM6newef8yib5kMpt7buonLJJfg0Q_KmWxHUu3ASHdlNZQj_MyafnkJcMeVKfvKHgkSImMs5yg0jnIdK1Y8rHJ8K4pBiRcYSPf04GhLNvA0SxoKFg0NOXkvmPl4BSiL0YzVx9mVOM1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آکسیوس در نخستین ساعت بامداد دوشنبه هشتم تیرماه به وقت تهران (عصر یکشنبه به وقت آمریکا) به نقل از یک مقام ارشد آمریکایی گزارش کرد که ایالات متحده و ایران موافقت کرده‌اند که حملات علیه یکدیگر را متوقف کنند.
براساس این گزارش دو طرف قصد دارند روز سه‌شنبه در پایتخت قطر دیدار کنند تا به اختلافات خود در مورد تنگه هرمز رسیدگی کنند.
براساس گزارش باراک راوید یک مقام ارشد آمریکایی گفت: «ما تصمیم گرفتیم تمام فعالیت‌های «رزمی» (جنبشی/kinetic) را متوقف کنیم».
همزمان یک مقام دیگر آمریکایی هم به آکسیوس گفت که هر دو طرف «فعلا» عقب‌نشینی خواهند کرد و «شناورها می‌توانند آزادانه حرکت کنند» چرا که قرار است گفتگوهای فنی ادامه یابد.
هر دو مقام آمریکایی و یک منبع سوم آگاه، دیدار برنامه‌ریزی‌شده برای روز سه‌شنبه را تایید کردند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76734" target="_blank">📅 00:16 · 08 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76733">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/B8346g5u7zlwdiJxBCz7Ay5j93NpZC_syj8Z1abTPi-zFdN4tDHtexErXOkeR7AOiDZQZ3svLW8JQ7_YMi5297TcJ6pT_nSaqp2UXp_POF0XzP5ir8lo_jh_-wAgXrjUGHfhscxA6PiCGYMGe8pqHdvHydtPBlYsDv2rQPWWKCRNo-XIOvBgLkR6mWXZnofS1zCRpkcNCq7GVbH4tr6S5o1yY2dooKLmaubEdcFOTDELx0GD8FIKPpd4bZYObAU07T5HJ93aGCvGDPcRIvSjPLdzmOcWjIKM28X_PU2dHf0wYb2fT_DzeCpJ5Ax2vfk0AMMvRPMwak5gkv59jD8m5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از آن که روز شنبه - ششم تیر - نزدیک به سه‌چهارم اعضای مجلس ۸۸ نفره خبرگان رهبری در ایران، در بیانیه‌ای شبیه «فتوا» خواستار گرفتن انتقام کشته شدن علی خامنه‌ای، رهبر پیشین جمهوری اسلامی از دونالد ترامپ،‌ رئیس‌جمهور آمریکا و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، شدند، دبیرخانه این مجلس روز یکشنبه - هفتم تیر - در اطلاعیه‌ای، این بیانیه را «نامرسوم» خواند و درباره آن توضیحاتی داد.
در بیانیه روز شنبه که ۶۳ عضو مجلس خبرگان آن را امضاء کرده‌اند، آمده بود که اگر «مسلمانان متدین» به این رهبران آمریکا و اسرائیل دسترسی پیدا کنند، کشتن آن‌ها «وظیفه شرعی» آنان است.
اما در اطلاعیه روز یکشنبه دبیرخانه مجلس خبرگان آمده که هیئت رئیسه این مجلس مفاد منتشرشده را «غیرمعمول و نامرسوم» توصیف کرده و اعلام کرده است که محتوای آن به بررسی و بحث بیشتر نیازمند است.
به نظر می‌رسد،‌ اطلاعیه دبیرخانه مجلس از اختلاف نظر و شکاف میان هیئت رئیسه و بخش مهمی از اعضای این مجلس حکایت دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 358K · <a href="https://t.me/VahidOnline/76733" target="_blank">📅 20:41 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76730">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lVhplFC9ksCcRg7sg8ElqGArTUKxnxXw5Y1F9iyOqI9yBoHnglqIYiFB7h83Qi_8jBSRwugAyCk3uvRXhiaG9j9DmCRvXIo13nPkZpdQCWa4iCdImgZdogBjc4-F6oKgs0wic7vlunYP39QXdxzNmqPrkbsZ75skPWOZ3Oy_htJYj77O6OUBoNRZMVnF9G4Wl2iDvb-tVxd_4tzE00YPxXPmXoPdh7cp9r4foFjLVX9pkSpKkdVT61ACEmmR-af4Afmesag1oeRDWFSJl9Nd2mPmBf7AnGB9misSDixp91bKjwzdlQLrA9KN88F42ooNzhXqRuklDrXXkXy0ETWwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LumTNxiisx0bMTYO6BLDVE_2fBm2g4h49-89u6JpoEASU505rgGAGM8iB-kC5r_ibJzFm2ZC256f1gK5w9q5NXJnkhNcVlZ1S-9rnhhnu2V3o7_j0eh7L5vvMAL1n6o41qoWCKwXQjSdH8Bae1xh91AQ30B7Ipv2ChKlsOhY82yPP1UAxPKUFEn8Z-l6g8EQEFjMJ_fjDwbUcBrYla65RX4eqTI41H11RQP5WBpmG29gCmfbxiGt-1o7VGRLECnxL0UlqFuvcpVOYPcjnWfQxhiZWsx9bmPos9VDVxND6T51JKRS-4O3jUtXoEWZwFPYw6YvntJXXMPMqI_x_ueeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/biP06kuK5_8NkXmMNQIRZZSKBHSatrmOwLgjyJV1aG-ozqRIhLeRjjoQQqKNpNsXa2glKPzg5UcKNoxQ9XUvXRHOCPA6VO8rNZncX0vaV3OiEvsDD1RO2wKIxkLLWaSLFoPbYavcpwuvY069K5Uoss_f-2uilixJQzLhCVF7cdJ_KBGUVGGwmNKw4akF6uk4im7GTYjX3-jRCHzgqKPNjZf37EJg0pc_k9KcAoxINngev4EDyf37gPC0ivv4rNfn1Yr3lzeRgIp4vkBIb--7bRpjN1Y7cnYyRcxqK8y8VoHbRPeAbTeZ8rBEzdF2jqeCSkT6eCfLDEU1W8CRvpGgnQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بحرین گفت که یک ساختمان مسکونی در استان محرق هدف پهپاد ایران قرار گرفته است اما مجروح یا مصدومی گزارش نشده است.
تصاویری که دفتر رسانه‌ای پلیس بحرین منتشر کرده است خساراتی را به طبقه فوقانی یک مجتمع آپارتمانی نشان می‌دهد.
ایران بامداد یکشنبه اعلام کرد که به تلافی حملات آمریکا، پایگاه‌های آن کشور در بحرین و کویت را هدف قرار داده است.
بحرین و کویت این حملات را محکوم کردند.
بحرین همچنین خواستار جلسه فوری شورای امنیت برای پاسخگو کردن ایران شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 332K · <a href="https://t.me/VahidOnline/76730" target="_blank">📅 19:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76729">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JnzAqKcvMs29iFmWWz-m8Um01X6xf7DnazVwsa4Gv8QjCzE7OI3qBf8HpayD-eY1qkLEwkAysdFrHMaeM6cq6S_KW-hH4Ax7Ye_Dg5K0eUtUf3kvTUzLbdpAGl_NNy5R2D2ivdRBcFOuygP1Cyo0g2il4JVGgPfAT-DHqRo-ZZUwMVbE9xSvh5H5cjHvZR5462EcJSLIGo6TRA1JHeF0jIGqiGaRmhtZN1DXf4Qc5dpHotQ7itwgTyEzJQPwSFog2j6hLLilXtvVd4Sxv_PJzUQNEy8hZ_NIlMc23TZXmSWrwfY8ppDKRpcF82dVbHvVU8hU_vdXr5KgwR_VlDaz8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">افزایش قیمت دلار آمریکا و دیگر ارزهای خارجی در بازار آزاد روز یک‌شنبه، هفتم تیرماه، هم ادامه یافت.
روزنامه هم‌میهن خبر داد که قیمت دلار در بازار آزاد در روز یک‌شنبه به ۱۷۲ هزار تومان رسیده است.
این روزنامه قیمت یورو، واحد پول اتحادیه اروپا، را هم ۱۹۴ هزار و صد تومان ثبت کرد.
روز شنبه، ششم تیرماه، قیمت دلار آمریکا در بازار به ۱۶۶ هزار و ۷۰۰ تومان رسیده بود.
این افزایش قیمت بیش از پنج هزار تومانی در بازار دلار در حالی است که در پی امضای تفاهم‌نامه میان ایران و آمریکا، روز چهارشنبه ۲۷ خرداد قیمت هر دلار آمریکا به حدود ۱۵۳ هزار تومان هم کاهش پیدا کرده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 315K · <a href="https://t.me/VahidOnline/76729" target="_blank">📅 17:36 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76728">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2CZczy-NwFKU4i_v3yQGSjMexP3wlvYuA5b_iU0gE4vWIdpr1w4Hh9nEK02pEFbE6m4V53VOHef2CEp6gER0bQFnKOEDMS_ciP0vVTwffEPCeBWufW4AeSZRbPpqPT2DGfGeNDku5_8grHT1Lu6ZYqtniX5_l4DJA6mYEbQ2Ija-qMtDVRSOz-aKFdtWF-oBD41MMN_jZ7vhhLjA6GiBuCMGuKzIWogn4ogk6dL8Nyo0l9Qdn4ptFKuVoTb0nyFLEjeiovwKVvyGMGi4G8yNF0RD2D5lzM-zLDYF7gbKv2taREDxDu_U0CE6ICGRJ73ZvdQtzhswen20_iS5dB7CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجتبی خامنه‌ای، سومین رهبر [اعلام شده] جمهوری اسلامی، در پیامی مکتوب به مناسبت هفته قوه قضاییه، از دستگاه قضایی خواست پرونده‌های مربوط به آنچه «جنایات آمریکا و اسرائیل» در جنگ‌های سال‌های ۱۴۰۴ و ۱۴۰۵ خواند را با جدیت در محاکم داخلی و بین‌المللی پیگیری کند.
او در این پیام که به مناسبت سالگرد هفتم تیر و هفته قوه قضاییه منتشر شد از قوه قضاییه خواست رسیدگی به پرونده‌های مربوط به جنگ را تا صدور و اجرای احکام ادامه دهد و مدعی شد چنین روندی می‌تواند از تکرار این‌گونه اقدامات جلوگیری کند.
مجتبی خامنه‌ای از زمان [اعلام] انتصاب به مقام رهبری جمهوری اسلامی تاکنون در هیچ مراسم عمومی، سخنرانی یا برنامه رسمی حاضر نشده [و صدا و تصویری هم از اون منتشر نشده] است. سایر مقام‌های حکومت تاکنون توضیحی درباره این موضوع ارائه نکرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76728" target="_blank">📅 17:35 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76727">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=YpZtD7a6KhAYiYWWJD3E9PW0pdiC1tQ5y3sYcIdXT2DUKkn4q-RK_cD9UFxJJ23EDjXllNcdxvCiO-SBkKtcDmID2RCGpKeyK84lctjvNJjYAt-BUlfBZ_yAq842Z11m_0VytNNzgPt91MbG0Og-uG58OEMTqYgObyQZf8W8m2t_6kgBLWWw6rcWMEC4C3KBEGLbESzMN7CNw3rXTh-SrplF_MEXpRfVVX2obmnrLq0UFF6s1QtWaruqRSPrZDEESb_1vWqMQ1YnDcZL10dJN88pB4hPjlaE181DlI_iaIiAhE-mP2cNByBFw2DwKAlFbDwJ1VFOSXb5-gJ44jkpRw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dbba8d2b1d.mp4?token=YpZtD7a6KhAYiYWWJD3E9PW0pdiC1tQ5y3sYcIdXT2DUKkn4q-RK_cD9UFxJJ23EDjXllNcdxvCiO-SBkKtcDmID2RCGpKeyK84lctjvNJjYAt-BUlfBZ_yAq842Z11m_0VytNNzgPt91MbG0Og-uG58OEMTqYgObyQZf8W8m2t_6kgBLWWw6rcWMEC4C3KBEGLbESzMN7CNw3rXTh-SrplF_MEXpRfVVX2obmnrLq0UFF6s1QtWaruqRSPrZDEESb_1vWqMQ1YnDcZL10dJN88pB4hPjlaE181DlI_iaIiAhE-mP2cNByBFw2DwKAlFbDwJ1VFOSXb5-gJ44jkpRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عباس عراقچی، وزیر امور خارجه جمهوری اسلامی، روز یک‌شنبه هفتم تیر در کنار همتای عراقی خود به آمریکا هشدار داد که «ایجاد ترتیبات موازی» برای تنگه هرمز «صرفاً به پیچیدگی اوضاع، افزایش تنش‌ها و تأخیر در بازگشایی این آبراه حیاتی منجر خواهد شد».
در پی امضای تفاهم‌نامه میان تهران و واشینگتن، آمریکا هفته گذشته مسیر دوم را برای عبور کشتی‌ها از تنگه هرمز معرفی کرد، مسیری در نزدیکی سواحل عمان که از دسترس ایران به دور است و می‌تواند رقیبی برای انحضار ایران بر این آبراه باشد.
در واکنش به این اقدام آمریکا، سپاه در دو روز گذشته به دست‌کم دو کشتی حمله پهپادی کرده که بلافاصله پاسخ ارتش آمریکا را به دستور دونالد ترامپ به همراه داشته است.
در واکنش به این رخدادهای تازه در خلیج فارس،‌ عراقچی که برای دیدار با مقام‌های عالی‌رتبه عراق به بغداد سفر کرده روز یک‌شنبه در نشست خبری خود با فواد حسین، همتای عراقی‌اش، چنین گفت: «بر اساس این تفاهم‌نامه و پس از رفع موانع، تنگه هرمز ظرف مدت ۳۰ روز تحت مدیریت انحصاری ایران به ظرفیت پیش از جنگ باز خواهد گشت و مسئولیت اجرای این ترتیبات تنها بر عهده جمهوری اسلامی است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76727" target="_blank">📅 17:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76726">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tZT5RP7DxWQfFMqrtphzpDnzJGUYXcGMFNYPEXJr7sxGOptZr-KEmQACbJJhi7ACEbR18NyvHC_BjRcmK6RxuafSmADYXJGEI3KMQBaWSk7d0ApER7gp_jxURC3zlx0duNH2barp6aSg1FMtRtb4Gthm1BsW33oWiiivJoWR4vsQHv693GDw3obP-XV90eoUHX3Ccs6bSaT82M2ZtRtsqt20W9OENr3OB2oUydLlP2KQ8O_z-4cziy1Zk_PrNwx0zLoYhXxGtDQtffOV4Li_-DyWaO5e6lyP9WgPwTRi3OEKOegc6adCmO6phx5t3qTS-hyzJWoX0MXJ0rUTIoRy7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تقی چنگلوایی» فعال محیط‌زیست و داوطلب مردمی اهل بهبهان، در جریان مهار آتش‌سوزی گسترده در «کوه بدیل» زاگرس جان باخت.
تقی چنگلوایی هنگام مشارکت در عملیات مهار آتش‌سوزی، بر اثر شدت آتش و حرارت بالا و در پی انفجار دستگاه دمنده‌ای که به دلیل کمبود امکانات برای اطفای حریق از آن استفاده می‌شد دچار سوختگی شدید شد و جان خود را از دست داده است.
رییس اداره محیط زیست شهرستان بهبهان در گفت‌وگو با شرق نیز تایید کرده است که آتش‌سوزی در منطقه شکار ممنوع بدیل واقع در شمال بهبهان هم مرز با منطقه حفاظت شده خائیز هشت شب جمعه پنجم تیرماه شروع شده و هنوز هم ادامه دارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76726" target="_blank">📅 17:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76724">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">میثم پیرفلک، پدر کیان پیرفلک، که در جریان اعتراضات «زن،زندگی،آزادی» در ایذه کشته شد روز یکشنبه هفتم تیرماه پس از حذف ایران از جام جهانی در واکنش به حرفهای رامین رضائیان، نوشت: «خدا بخواد نمی‌شه که نمی‌شه آقای رضاییان.»
رامین رضاییان، پیشتر گفته بود: «اگر خدا بخواهد پیروز می‌شویم و دل مردم شاد می‌شود.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76724" target="_blank">📅 17:30 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76723">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/PKBfYpRFVqBvCgNnx9Zqe_NqQOsEoI484DHrhFxEkKMdS-0AmhPSkCDPN7ijdk6-Iqsyr0fHg_nutsUulNjuMoY-7Ryf7Obzffx7kpCiL2l2gWnLmASiYxYcwecAebTyqC8v38UGCgUGXleN4gIls7X7hdj6fX2Cc74_Mx6fD6FyzzYXACKSDnx3tPnziKzdeumJarUQXQqX5MbEGqNBOi5VKfAn5pVOTC2JBU7xWnB_hURbsBSWzaMSF_3klKdvTq14jD4t8YQjVf7BMdrtuI_D6TdVtG0KdRSldCO1dcnG7nkayywANL-aSYMqtzj16nyP3LyZPJMk0GX-3YJ8Ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیدار الجزایر و اتریش در مرحله گروهی جام جهانی فوتبال با تساوی سه بر سه پایان یافت؛
نتیجه‌ای که آخرین شانس تیم ایران برای صعود به مرحله حذفی را در آخرین ثانیه‌های مرحله گروهی جام از بین برد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 354K · <a href="https://t.me/VahidOnline/76723" target="_blank">📅 07:50 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76722">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/NukO8K57APis5I28uf8yAZjgUUxWNGaNJ6GHlo8LaDwBlttbMYdR2lwqiWZV_RT6FkmlPpsgmXQvCiON8MhCzvMPqrNkO7lJv2YkxCYzaY0hgRX0No4fFT4AkUUk-HJrGLzlJiGFdoKkyZAr_BAJ6N8kACIosOfyb5tZOoeIKgRD1vxDZ9HzLufXnf87dhpskidtDGDN3V767-ZBWSIHrQF_oeDFnFqqxT_wQNSUAYfGkCQtPhPj1E3XkQyFaBMGjUI8RZL_z74oA8gUEyMY91wdkMQOXHewu-GooZKO14U3y-PqSXZN12aIa-KkoW_MvbpT0GHZFDm1lq6nSFrHBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روابط عمومی سپاه پاسداران، با انتشار بیانیه‌ای از حمله مشترک موشکی و پهپادی به مواضع ارتش ایالات متحده در منطقه خبر داد.
بر اساس این بیانیه، نیروهای دریایی و هوافضای سپاه در ساعت ۲ تا ۳ بامداد یکشنبه، ۷ تیرماه، هشت زیرساخت کلیدی ارتش آمریکا را در پایگاه «علی‌السالم» کویت و ناوگان پنجم دریایی در بندر «سلمان» بحرین هدف قرار داده‌اند.
سپاه این عملیات را «پاسخی قاطع» به حملات هوایی بامداد یکشنبه آمریکا به پنج پست ساحلی ایران در جنوب کشور دانسته و واشنگتن را به «نقض عهد» متهم کرده است.
در بخش دیگری از این بیانیه، با اشاره به اینکه کنترل ترتیبات عبور و مرور در تنگه هرمز بر اساس «تفاهم‌نامه اسلام‌آباد» بر عهده جمهوری اسلامی است، تاکید شده که از این پس با کشتی‌های متخلف قوی‌تر از گذشته برخورد خواهد شد.
سپاه پاسداران با هشدار به ایالات متحده اعلام کرده است که هرگونه تجاوز احتمالی بعدی، حتی اگر علیه اهداف کم‌اهمیت باشد، با پاسخی «خردکننده» مواجه می‌شود.
@
VahidOOnLine
متن خبر منابع حکومتی:
🔸
سپاه پاسداران خبر داد: عملیات قاطع موشکی و پهپادی در پاسخ به تجاوزهای آمریکا/ با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد
🔹
روابط عمومی سپاه پاسداران انقلاب اسلامی بامداد یکشنبه با صدور بیانیه ای از پاسخ قاطع نیروهای دریایی و هوا فضای سپاه به تجاوزهای اخیر آمریکا خبر داد و تاکید کرد: من‌بعد با کشتی های متخلف قوی‌تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه‌ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت. دشمن بداند نقض آتش‌بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
در ادامه این بیانیه خطاب به مردم عزیز و شرافتمند ایران اسلامی آمده است:
فرزندان غیرتمند شما در نیروهای دریایی و هوا فضای سپاه طی عملیات مشترک موشکی و پهپادی در ساعت ۲ الی ۳ بامداد امروز یکشنبه هفتم تیر ماه، با پرتاب موشک های بالستیک و پهپاد به سوی هشت زیرساخت مهم ارتش کودک‌کش آمریکا در پایگاه علی السالم کویت و ناوگان پنجم دریایی در بندر سلمان بحرین آنها را منهدم کردند و تجاوزهای اخیر آمریکا را با قاطعیت پاسخ دادند.
دشمن متجاوز که نقض عهد و پیمان شکنی در ذات او است، به بهانه مقابله نیروی دریایی سپاه با کشتی متخلف، اوایل بامداد امروز، به پنج پست ساحلی جمهوری اسلامی حمله کرده بود.
بر اساس تفاهم نامه اسلام آباد ترتیبات کنترل عبور و مرور در تنگه هرمز با جمهوری اسلامی است و من‌بعد با کشتی های متخلف قوی تر از گذشته برخورد خواهد شد و برخورد با تجاوز احتمالی دشمن به هر بهانه ای که باشد ولو مانند دیشب و امشب تجاوزها به اهداف کم اهمیت باشد، پاسخی خرد کننده خواهد داشت.
دشمن بداند نقض آتش بس خلاف بند یکم تفاهم نامه اسلام آباد است و توقف کلی روندها را در پی خواهد داشت.
🔹
و ما النصر الا من عند الله العزیز الحکیم
در خبری دیگر:
نیروی دریایی سپاه پاسداران بامداد یکشنبه هفتم تیرماه، با انتشار بیانیه‌ای در واکنش به حملات اخیر آمریکا اعلام کرد «شلیک‌های کور آمریکا به سیریک» معمای اشراف این نیرو بر تنگه هرمز را حل نخواهد کرد.
در این بیانیه آمده است شلیک به «متخلفان» راه عبور را به دیگر شناورها یادآوری می‌کند. همچنین با تهدید پایگاه‌های آمریکایی در منطقه تاکید شده است: «حساب پایگاه‌های آمریکایی منطقه جداست. جهنم را در این روزها تجربه خواهند کرد.»
@
VahidOOnLine
رویترز به نقل از یک مقام آمریکایی گزارش داد در پی حمله‌های موشکی و پهپادی جمهوری اسلامی به کویت و بحرین، هیچ گزارشی از تلفات نیروهای آمریکایی یا وارد آمدن خسارت یا آسیب عمده به تاسیسات آمریکا در خاورمیانه دریافت نشده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 369K · <a href="https://t.me/VahidOnline/76722" target="_blank">📅 04:07 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76721">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=AB5SEAvC7JBekhQvedqaLx1Ngm9e8thNcpOO-yyg1s8bUzzRusRKj_KClwvLqZXIH4AklotRb4QeJBWXXuf9c_IyEiXFKGtz0F9MASFjP84NGJWUVCuvcQGSufJZ6HS8Y_0k1bEeYzvP1xsq9XMUnJ7S8bm7mrX9Hla5Gx3AVYHglidpIYm27BHESKr0bkAcvQyfQejODETkktjoFMMghavjn8nY3zxR_96D1VLCOmvQB-14_9NCGpyhm0jP0NT6RQjP52XlSJd4OY8OT8rplUy2vSvc-Qd7rv2epFClsdZK-FnIHzbXD3PSp6D-nBN0LFfLqmMzz3T6PnSoPSbWUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/f7b676ffd6.mp4?token=AB5SEAvC7JBekhQvedqaLx1Ngm9e8thNcpOO-yyg1s8bUzzRusRKj_KClwvLqZXIH4AklotRb4QeJBWXXuf9c_IyEiXFKGtz0F9MASFjP84NGJWUVCuvcQGSufJZ6HS8Y_0k1bEeYzvP1xsq9XMUnJ7S8bm7mrX9Hla5Gx3AVYHglidpIYm27BHESKr0bkAcvQyfQejODETkktjoFMMghavjn8nY3zxR_96D1VLCOmvQB-14_9NCGpyhm0jP0NT6RQjP52XlSJd4OY8OT8rplUy2vSvc-Qd7rv2epFClsdZK-FnIHzbXD3PSp6D-nBN0LFfLqmMzz3T6PnSoPSbWUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیام‌های دریافتی تایید نشده:
سلام آقا وحید از منطقه [...] بندرعباس چندتا موشک بلند شد به سمت دریا رفت
سلام ساعت ۳:۳۹ صدای انفجار بندرعباس
یک دقیقه بعد: الان یکی دیگه هم زدن
درود همین الان اطراف بندرعباس دوتا صدای انفجار
ساعت ۳:۳۶ دقیقه
صدای دوتا انفجار از راه دور تو [...] بندرعباس شنیده شد، فاصله دور بود اما موج انفجار تو [...] حس شد
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 328K · <a href="https://t.me/VahidOnline/76721" target="_blank">📅 03:46 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76719">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/IMyhEqS5NQby67X6gA4U-FecbQMQ2WYNbpMx9V7Kdgf_LWzKZ4ub3t6n5KhgWLK0wAhL5Nvgbg2CmqZrSErOJpNpahiiWGQlsFzlQGVgqCeGpWg8RDsf_f3eWFZ7sHuFNEAxUXL8T9MMPdpM8KXhOCqOmvbfcTGDA12fdtSecVBJOaomptxKHbVkkhuYp4GXLNn3j-dgj1wEVYXgH1krzAu7Q22xR9y_y-X18QHeT8vwL_e7_DLtPUPNKrSRewJPr-toiZtPEk1A2SZwz7nmUj3I-O6JefALW84FiHaqjgTmwn99UMoT09-hl5unHsVnAtNYbJazN5Y8o7-Ct-mS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/fD9d5h9_iKM3ak1ovMAeUhjNl4w6MFuoKl1pjGbzlTvbQSoeVcxobLhYQ5ao-6kkocQrrKMFDcMi3HgPwNszZMGt9xt24GLPEx0wuRrF1OON_wQiWG-hRBgkEAp2N4T9pE4KAcMdcz3OFpzFlJ0VcG104askihkwzeezqapjNdFWHNamDlv7kLEivU1gewW70ZUS9QSmyWib5EeBqhG8y-HyutRUqHrpb5_ytWNBMKI0ywWvEx_vb5QlG9yGoLpXt5qAH1r1DC6tVVYaCGxRMdAL1llAMdRZjt5Q5O6qkMCR6SjqYUlly28BbQl-oiy_aUKwRwliEgEhZBNDfq5xKQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اعلام هشدار در کویت
تصاویر دریافتی
ارتش کویت دقایقی پیش اعلام کرد که پدافند هوایی این کشور در حال حاضر «با حملات موشکی و پهپادی خصمانه» مقابله می‌کند.
@
VahidHeadline
دقایقی پیش‌تر پیام مشابهی درباره بحرین دریافت کرده بودم. الان:
وزارت کشور بحرین، بامداد یکشنبه، با انتشار اطلاعیه‌ای از به صدا درآمدن آژیرهای هشدار خبر داد و از تمامی مردم و ساکنان این کشور خواست تا ضمن حفظ آرامش، فورا به نزدیک‌ترین مکان امن پناه ببرند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76719" target="_blank">📅 03:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76718">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/oAuw_4lxHZbCTT2tOQc8onYIfyeKPqp61VwwP-9nQY1YNQgwXvP0TbpQTnMKA2UqbiccZM8N4kBbmBY6S558NzRcci0eqFFmp6mrTScsW2y7Ar3T7HRpzRpKLroutEogX5bqOT2IViM_41FqRWu_DWkv0XbHi54KiWqzQGFUeEIU9mgW35ESheOb7Elh964sabS8dHDxZMOEteex8ttPN0yqc7xiVdVAM_qbBIT5oG80uASXi5aU15yTb3zdf_G9KCVMrJy28z-c2p4TxzGYYGXX4qgymALCRXVxhC7oh8ILBh3BcdenTGmeZJDnrP8Q11jema0aiBqAVxxPizyjLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: در صورت ادامه نقض آتش‌بس، جمهوری اسلامی ایران دیگر وجود نخواهد داشت
ترجمه ماشین:
هواپیماهای ایالات متحده همین حالا محل‌های نگهداری موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند، چون بار دیگر توافق آتش‌بس را نقض کردند!
بسیار محتمل است که آن‌ها هرگز درس نگیرند!
ممکن است زمانی برسد که دیگر نتوانیم منطقی رفتار کنیم، و مجبور شویم کاری را که با موفقیت بسیار آغاز کردیم، از نظر نظامی به پایان برسانیم.
اگر چنین شود، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
رئیس‌جمهور دونالد ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 294K · <a href="https://t.me/VahidOnline/76718" target="_blank">📅 02:47 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76717">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=fBysTg1AiVF2GTawYYtnQeYO0anfv0GTJ6irsjTxAjz33YiFEq3BYhHRr_K9_leFYlfYmuKtehFPz8eXa2quZdAJxDbFJsCzAjmZ6r8aypZn8LCNIL-1rAaUZZUk8tXmrT_Y2NF9xJekZE3PHSWCLe80yxFK2gS3NkgkaSGil6f_bCKdLHqwgTcvTXgNAOxAoCrLlTRY0pQ7lqXwzPu-M1twgSgur1k944C469a6R7hPGbdkHE-kwFiHZHwFYuTjB86o2mwJKIJq_I0i6AXAk17TCg7f5AsDy3BlGVmTJJ0Ph9FKbHUZiGuyYpvEb8iai8k-Gr7RmSu08dBiF8r41A" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d134b6727d.mp4?token=fBysTg1AiVF2GTawYYtnQeYO0anfv0GTJ6irsjTxAjz33YiFEq3BYhHRr_K9_leFYlfYmuKtehFPz8eXa2quZdAJxDbFJsCzAjmZ6r8aypZn8LCNIL-1rAaUZZUk8tXmrT_Y2NF9xJekZE3PHSWCLe80yxFK2gS3NkgkaSGil6f_bCKdLHqwgTcvTXgNAOxAoCrLlTRY0pQ7lqXwzPu-M1twgSgur1k944C469a6R7hPGbdkHE-kwFiHZHwFYuTjB86o2mwJKIJq_I0i6AXAk17TCg7f5AsDy3BlGVmTJJ0Ph9FKbHUZiGuyYpvEb8iai8k-Gr7RmSu08dBiF8r41A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یارو در «رسانه ملی» جمهوری اسلامی داره میگه چون کشتی‌ها قصد عبور از مسیر «ناایمن» رو داشتند سپاه اون‌ها رو هدف قرار داده بوده!
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 296K · <a href="https://t.me/VahidOnline/76717" target="_blank">📅 02:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76716">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=dTCi-YWP5EQPFw8p0FmtUxIP9qjZwXMF9dhIcW4S8IU7AngpExTc2L92EqU2O3jDfwhEkMzYt0pXDI4dWbaoDft198T0ajBwuDDoa93sd902kdA3XwhQTGYmKpE3U5wUNDMDIV1eLDHAKunZoQqMjxczkGbxBfBYyRpZsQnLDYypIdWiZkEme9f4mMRD083Q1EDul2OERRi5cEvpj37h948nAHrWtu7Y9YbiBkp04ktiEs3msEFwqqMlFeKYx2D5LcXcu50ZNb6Zm0rkQ3DfTz7lHzWYYM7_7Z96eZBONNynKamVbfajKnNVpWalU5ZoR9uEjOSWW99pTq7HC-VcUw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fba5afa7ba.mp4?token=dTCi-YWP5EQPFw8p0FmtUxIP9qjZwXMF9dhIcW4S8IU7AngpExTc2L92EqU2O3jDfwhEkMzYt0pXDI4dWbaoDft198T0ajBwuDDoa93sd902kdA3XwhQTGYmKpE3U5wUNDMDIV1eLDHAKunZoQqMjxczkGbxBfBYyRpZsQnLDYypIdWiZkEme9f4mMRD083Q1EDul2OERRi5cEvpj37h948nAHrWtu7Y9YbiBkp04ktiEs3msEFwqqMlFeKYx2D5LcXcu50ZNb6Zm0rkQ3DfTz7lHzWYYM7_7Z96eZBONNynKamVbfajKnNVpWalU5ZoR9uEjOSWW99pTq7HC-VcUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست سنتکام، ترجمه ماشین:
نیروهای آمریکا پس از تازه‌ترین حمله ایران به کشتی تجاری، حملات بیشتری انجام دادند
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) به دستور فرمانده کل قوا، روز ۲۷ ژوئن حملات بیشتری را علیه چندین هدف در ایران انجام دادند.
پس از حملات دیروز آمریکا در پاسخ به حمله ایران به کشتی M/V Ever Lovely،
به ایران فرصت داده شد تا به توافق آتش‌بس پایبند بماند، اما این کشور چنین نکرد
؛ زیرا نیروهایش یک پهپاد تهاجمی یک‌طرفه را شلیک کردند که صبح امروز ساعت ۴:۳۰ به وقت شرق آمریکا به نفتکش M/T Kiku برخورد کرد. این نفتکش با پرچم پاناما در نزدیکی تنگه هرمز در حال عبور بود و بیش از دو میلیون بشکه نفت خام حمل می‌کرد.
نیروهای سنتکام امروز در پاسخ مستقیم به ادامه تعرض ایران علیه کشتیرانی تجاری، حملاتی انجام دادند. هواپیماهای نظامی آمریکا زیرساخت‌های نظارت نظامی ایران، سامانه‌های ارتباطی، سایت‌های پدافند هوایی، تأسیسات نگهداری پهپاد، و توانمندی‌های مین‌گذاری را هدف قرار دادند.
عبور کشتی‌های تجاری از تنگه هرمز ادامه دارد. نیروهای آمریکا همچنان هوشیار، مرگبار و آماده هستند.
CENTCOM
آپدیت:
بعدا ویدیوی بالا رو درباره این حمله منتشر کردند
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 310K · <a href="https://t.me/VahidOnline/76716" target="_blank">📅 01:21 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76715">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/kMbinelVDVnGijmnpG6O2L-EQ52qq8Fv1AKRAo8IBgZvKf7gv1dqqG5oXoLXoknKrQsBIRWpBw3_75gOrSuuCRVaHotNWSpSwE0ZTk9VVFc96OrgoAmiCxxMUa8GDPfuyrruiLpenB0jkt2LFXDnmAXdpzzhLugmVrbbEs05FA3wAcfRHn0FwkFRcLXSVAXjquoxfBc3LWUD6HliHQhelzDVBOd2Os_OuFJhmWLp6BfV8kDa8vQuQTRYYEan-0s9bIRf71lTWy02Cb4Aa0n22qRZeAL2gJhfxAHxq4VxA0tCaOW-Ley2nogmQ7Ly96kK91NDHqf7MaVNYhbjYumdWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک مقام رسمی ایالات متحده در گفتگو با خبرنگار آکسیوس تایید کرد که ارتش آمریکا، بامداد یکشنبه، هفتم تیرماه، در حال انجام حملات تلافی‌جویانه علیه اهدافی در منطقه تنگه هرمز است.
به گفته این مقام مسئول، این اقدام نظامی در پاسخ به حمله صبح شنبه به یک نفت‌کش تجاری در این آبراه حیاتی صورت گرفته است.
@
VahidOOnLine
پیش‌تر:
صدا و سیما: دقایقی پیش صدای چند انفجار در محدوده روستای طاهرویی سیریک شنیده شد
پیام‌هایی که من دریافت کرده بودم:
صدای چند انفجار.
طبق معمول انگار دوباره نیروی دریایی سپاه سیریک رو زدند.
سلام ساعت 12.41 صدای چند انفجار شدید بندرعباس
همین دو دقیقه قبل پایگاه دریایی سیریک هدف حمله موشکی
جوری زد که زمین لرزید
پایگاه دریایی طاهرویی سیریک رو هم زد
دوتا موشک صداش اومد رو دریابانی سیریک
دکل اسکله سپاه سیریک بعد چهار ماه موشک خوردن مداوم بلاخره امشب کج شد
قشم سمت سوزا صدای انفجار شنیده شد حدود ۱۲:۳۰
سلام وحید جان  تقریبا ساعت 00:45 صدای انفجار هرمزگان .قشم
تسنیم:
در اولین ساعات بامداد یکشنبه  صدای انفجارهایی در سیریک شنیده شده است.
برخی منابع مدعی شده‌اند که صدای انفجار در بندر طاهرویه بوده، اما هنوز هیچ منبع رسمی آن را تأیید نکرده است.
🔄
آپدیت ۱:۰۲
خبرنگار صداوسیما در سیریک به نقل از یک منبع آگاه نظامی: صدای انفجارهای شنیده شده مربوط به اصابت چند پرتابه به دکل مخابراتی در محدوده روستای طاهرویی سیریک است
💥
آپدیت ۱:۰۶
خبرنگار اکسیوس: یک مقام آمریکایی می‌گوید ارتش ایالات متحده در تلافی حمله ایران در صبح امروز به یک نفتکش تجاری، در حال انجام حملاتی علیه اهداف ایرانی در محدوده تنگه هرمز است.
آپدیت ۱:۱۲
خبرنگار صداوسیما در قشم به نقل از یک منبع آگاه: چند پرتابه در محدوده روستای مسن شهرستان قشم اصابت کرده است
آپدیت ۱:۱۷
صدا و سیما شنیده‌شدن دو صدای انفجار دیگر در شهرستان سیریک، منشاء صدا مشخص نیست.
آپدیت ۱:۴۱
صدا و سیما:
برخی منابع از شنیده شدن صدای چندین انفجار در بندرلنگه و بندر کنگ خبر می‌دهند
خبرگزاری صدا و سیما هنوز قادر به تایید قطعی این انفجارها نیست.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 308K · <a href="https://t.me/VahidOnline/76715" target="_blank">📅 00:58 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76713">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qTWRO83ckvuQbvarf28-nEhKmbbB14lgq1ZPfekmmaRqLilE4uHNKmfw_8wD4yWY1oUBMi78_nvZdLCkA7EydyqdwQWylmG0PD6cdqg2zQ3D_dyqT4TGQUCmKdBz77u8azjenrK2z41TGGhD2PO2M7mCInZbSb4yPRM-KMeIc2rLLTGIPoq0gRHdWHtNQMq-wJXaiFMTe_KLjjhrt_suaYO09Aj7B8sNkX5a3Tlsz_ZzhSjqjFvnwxcdUej3Edn795sB333XO5CcytGPWhzds4XWO2vDVCI4beEZtgnYzmfxsUay6vo3i9c6N6PkYgBwrjuBnstTXjfnQL1a0B6JFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/b1zd5ZsRtLf8vTfbGjSULtaO_0_OgwcB4s6yCssqZnQ4zUWB8HxRrKzDcZQrSUuqn1JBIrWmIiFZYoJjyPCMRQyVLIvtkt-4uQOAjnkBvdfggykBnztIpTBIy6LHslD1pZnzQGiAJQiHrjS6KNWdNvpVIkkVbuObLDLbbVSf27JBMijZImNkRBWjIMnx22kGb4bLHaxYwXqAOXJt-qbfv7wqYAjuj9bReXlykZx_IwdB8KVhyUHqmCnsDKMEDUT2rqnPYxkHbLMWlI_scLsIrVd8y4KN67hbUxXZP0Ps2cnSSd9BwCXMbQIKR4KoixikHARFRh-YdBffBT2jtqUtQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رسانه‌های ایران بیانیه‌ای با امضای جمعی از اعضای مجلس خبرگان را منتشر کردند که در آن می‌گویند بازگشایی تنگه هرمز «خلاف تعهدات مسئولان است و خطایی راهبردی شمرده می‌شود».
بر اساس این بیانیه که خبرگزاری‌های تسنیم و فارس، نزدیک به سپاه، آن را منتشر کرده‌اند، ۶۳ نفر از اعضای مجلس خبرگان تداوم حملات اسرائیل در لبنان و «عدم عقب‌نشینی»‌ ارتش این کشور از مناطق جنوبی لبنان را «نقض آشکار» تفاهم‌نامه ایران و آمریکا خوانده و نوشته‌اند بر این اساس بازگشایی تنگه هرمز «خلاف تعهد مسئولان است».
در بخش دیگری از این بیانیه نیز آمده است «بر هر ملکفی» که به دونالد ترامپ، رئیس‌جمهور آمریکا، و بنیامین نتانیاهو، نخست‌وزیر اسرائیل، «دسترسی پیدا کند، واجب است آن‌ها را به درک واصل کند».
این گروه از اعضای مجلس خبرگان همچنین «تثبیت مدیریت تنگه هرمز و دریافت غرامت خسارت‌ها و بازگشت اموال بلوکه شده و رفع تحریم‌ها و خروج امریکا از منطقه» را از مطالبات رهبر جمهوری اسلامی برشمرده و هشدار داده‌اند که «هرگونه سهل انگاری در این زمینه» با واکنش مواجه خواهد شد.
این بیانیه در حالی منتشر می‌شود که اختلاف‌ها در درون طیف‌های سیاسی طرفدار حکومت بر سر تفاهم‌نامه در روزهای اخیر بالا گرفته تا جایی که روز شنبه، نمایندهٔ رهبر جمهوری اسلامی در سپاه، از منتقدان این توافق خواست با «ایجاد اختلاف و لغزش» باعث «سوءاستفادهٔ دشمن» نشوند.
تفاهم‌نامه ایران و آمریکا به‌گفتهٔ مسعود پزشکیان، رئیس‌جمور ایران، با رأی «بیش از ۹۰ درصد» اعضای شورای عالی امنیت ملی کشور شامل شماری از فرماندهان ارشد سپاه پاسداران تأیید و تصویب شده و مذاکرات برای اجرای آن آغاز شده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 306K · <a href="https://t.me/VahidOnline/76713" target="_blank">📅 23:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76712">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=Pv-76sICoreDcFcusleV1nwK9ZuXOjwpTrgrtiX2QEo82BmFpVLEkXYLFhHxpYjD2PF72Cc0u72r3TA96uqDypcsmhU79cBEvr8BGmcpDAH3r4L7e7u9e9sItjvOsz8GD8pEu1ztUnbpTRQiX6-KB9zqPmkWsVzkr_siW7EzCUJjJdiZn3SK813yL86g0DHKBcCOja3bLyjn3fF4SNqlTOlvjxJXu4Fxsroo80ZPLomz8OLX2PNEIIsNxg8PHZ3JTgT8-VkqsRQhA6yTvKNlKhssqZ1o8qgMRTZI3L8DK2Q3IHQyXlVr1y2e3rnwnfJ6zNprSJcd_OQct2anOz38MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/41aa678ed6.mp4?token=Pv-76sICoreDcFcusleV1nwK9ZuXOjwpTrgrtiX2QEo82BmFpVLEkXYLFhHxpYjD2PF72Cc0u72r3TA96uqDypcsmhU79cBEvr8BGmcpDAH3r4L7e7u9e9sItjvOsz8GD8pEu1ztUnbpTRQiX6-KB9zqPmkWsVzkr_siW7EzCUJjJdiZn3SK813yL86g0DHKBcCOja3bLyjn3fF4SNqlTOlvjxJXu4Fxsroo80ZPLomz8OLX2PNEIIsNxg8PHZ3JTgT8-VkqsRQhA6yTvKNlKhssqZ1o8qgMRTZI3L8DK2Q3IHQyXlVr1y2e3rnwnfJ6zNprSJcd_OQct2anOz38MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر اسرائیل در سخنرانی تلویزیونی خود ضمن اشاره به توافق اخیر با لبنان، آن را دستاوردی «بسیار بزرگ» توصیف کرد.
بنیامین نتانیاهو با تاکید بر اینکه اسرائیل در «منطقه امنیتی زرد» باقی می‌ماند و این مسئله ضامن امنیت این کشور است، خاطرنشان کرد که فشارهای مختلف برای خروج اسرائیل از این منطقه به نتیجه نرسیده است.
او با قدردانی از نقش دونالد ترامپ، رئیس‌جمهوری آمریکا و مارکو روبیو، وزیر امور خارجه این کشور، در تحقق این توافق، تصریح کرد که اسرائیل نه تنها "محور تروریسم ایرانی"، بلکه "محور سیاسی ایران" را نیز در هم شکسته است و افزود: «ما به دلیل ساده‌ای به چارچوب این تفاهمات رسیدیم: چون حزب‌الله را به شدت در هم کوبیدیم و حزب‌الله که منتظر کمک ایران بود، آن را دریافت نکرد».
بر اساس طرح پیشنهادی آمریکا که چارچوب توافق لبنان و اسرائیل بر آن بنا شده، نیروهای اسرائیل به‌صورت مرحله‌ای، کنترل مناطق مختلف را به ارتش لبنان واگذار می‌کنند و ارتش لبنان نیز مسئولیت جلوگیری از ورود اعضای مسلح حزب‌الله به این مناطق را برعهده می‌گیرد.
خواسته اولیه لبنان، خروج کامل نیروهای اسرائیل از مناطق جنوبی این کشور بود.
حزب‌الله لبنان، این توافق را «تحقیرآمیز» توصیف کرده و آن را فاقد اعتبار دانسته است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76712" target="_blank">📅 22:42 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76711">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZyUa5lZpkelhv2Sy-xOoW3dncfFIUIs4_V31YhvP1pDv71eeRAfGi7ASY9kd20rkJeBbHRQBfS05XR1oilI4VWCjqEB56yz6mT3-DqDU0S5dTk5WayiC9sCJJBeu4m6X27E27BQ0k55NQUcYPbM78s6fWo9NC_NEr2DumXPiw4w8c8_uwDVegNpG1fomB29ZCuR8zKEcSxYp0_2---cTmEi4kBbov19yZoXyqZhv43_GgP4HtyKqOR2BeBygvJipC0aBIKcoYd2T3VLO3-irZDEggKUFIv4Qup49HsA4zFczE2lY2M4lXtspR97QdIAYNavWfkmOsfplot1Yv_6fZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیام‌های دریافتی درباره قطع شدن برق در مناطق مختلف شرق تهران:
سلام وحید جان
به طور بی سابقه ای کل برق پیروزی و بلوار ابوذر رفته کلا خاموشه محله های این طرفا
توی قطعی برقیا هیچوقت اینجوری سابقه نداشته کل محله ها با هم بره کلا شرق خاموشه
سلام وحید
ما محله نیروی هوایی ، منطقه ۱۳ تهران هستیم. برقا رفته. و اینجور که از دوستان پرسیدم تا  خیلی جاها برق نداره، حتی برق  چراغ راهنمایی  رانندگی هم قطع شده.
مثل یه سری که توی جنگ برق ها قطع شد و حمله کرده بودن شده، چشم چشم رو نمیبینه
سلام وحید جان برق شرق تهران محدوده پیروزی کامل قطع شده
وحید برق  نارمک هم رفته
😐
😑
نارمکاز پشت بوم دیدم تا جایی که افق دید اجازه میده کلا شرق تو تاریکیه
برق سمت نظام آبادم کامل رفته همه جا تاریکه
داداش برق سبلان و نظام آباد و اینام رفته
سلام برق سبلان هم‌رفته
سلام، من میدون رسالت تهرانم، تا چشمم میبینه همه جا تاریکه
بجز مناطق خیلی دورتر
کل نارمک جنوبی بی برقیم
سلام ما نارمکیم ولی برق داریم
نارمک پایین هفت حوض برق هست
سمت رسالت و سرسبز رفته
سلام برق جنوب نارمک هم قطع شده فکر کنم پست دوشان تپه مشکل دار شده
وحیدجان ما نظام آبادیم ولی برق داریم
البته به بیمارستان امام حسین نزدیکیم
وحیدجان برق شهید کلاهدوز هم رفت همی الان
داداش ما کلاهدوزیم دو دقیقه پیش رفت
همه جا تاریکه
سلام وحید جان
محدوده شیخ بهایی تهران خیابان شیراز شمالی هم برق رفت
سلام وحید جان
تهرانپارس فلکه اول
ما برق داریم ولی دارم نگاه میکنم ی سریا ندارن!
برق خیایان شیخ بهایی شمالی رفت
انتهای تهران نو سمت اشتیانی و فلکه اطلاعات برق نداریم.
ما نیروهوایی هستیم برقا تا جایی که میبینیم قطعه
آقا برق وصله چرا الکی میگن شما هم میزارین مردم همه حالشون بده ترو خدا استرس بیخود ندین
برق خیابون مدنی،  نظام آباد همچنان قعطه
نارمک ۴۶ متری غربی برق رفته بود دو سه دقیقه هست که برگشته
نارمک جنوبی، حوالی میدان شقایق هم برق رفت.
سلامت میدان ۷۰ و سمنگان هم رفته بود.
الان بعد ۲۵ دقیقه اومد
وحید جان سبلان شمالی برق قطعه
سلام، زرکش وحیدیه برق قطعه
وحید جان سلام پیروزی چهارراه کوکاکولا برق داره اما کل خیابان نیروی هوایی برق رفته به طوری چشم چشم رو نمیبینه مردم با نور موبایل راه میرن
برق نظام‌آباد اومد
ندیدم مجیدیه رو بگند که برق رفته. اینجام نیست
منتها زنگ زدم و محله بقلی خواجه عبدالله برق هست.
سلام وحیدجان ما پیروزی سمت خیابون شیوا هستیم برق داریم
برق مجیدیه و خیابان کرمان از ۸.۲۰ دقیقه کامل قطع شده . تا چشم میبینه برق اطراف قطع شده
الان. نظام اباد محدوده شرقی امام علی خاموش بود همین الان اومد.
داداش برقا اومد فک کنم یه بانکی چیزی خالی کردن رفتن دیگه
🤣
وحید یرق پیروزی بلوارابوذر اومد
آپدیت: پیام‌هایی از وصل شدن برق در بعضی از مناطق داره میاد.
همز‌مان خبرگزاری فارس:
قطع برق تعدادی از مناطق تهران؛ دلیل مشخص شد
تعدادی از مناطق تهران از ساعاتی پیش با قطعی برق مواجه شدند.
پیگیری فارس از توانیر مشخص کرد، مشکل فنی در یکی از پست‌های ۲۳٠ شرق تهران علت قطعی برق است.
هم‌اکنون تیم‌های عملیاتی و فنی برای رفع مشکل در محل پست حاضر و درحال حل مسئله هستند.
آپدیت:
همچنان که خیلی‌ها پیام میدن که برق ما وصل نشده یک عده که برقشون وصل شده بود هم دارند پیام میدن که دوباره قطع شد. شاید به خاطر همون تعمیراته.
آپدیت ۰۰:۴۰ بامداد یکشنبه:
خبرگزاری تسنیم:
برق شرق تهران وصل شد
رجبی‌مشهدی، معاون وزیر نیرو از رفع خاموشی‌های شرق تهران خبر داد.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76711" target="_blank">📅 20:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76710">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZxLuhCI7od4hOe93MSMar7Jls2LiJy-CRNw3aZGKZzblpo3dYL43RXUDKVJxv3gP-b9Rv6Ex-L-zQKUbq5n6r5JsL0iM440z81sSXu1sqBP3neiYqt91-2y1n-qjAfBrvfQNfNLNnBrUyOhO5vDrWsVdT1mLKtf8PddkPMsKAfY7xdGaM-8NUbAQ2KoM_tls-ZNOQWiq2xSd2rXEnHucgNU_f6QTA_DDm_ICBZYbV2yaYbZ8qrtLGwOm9qS1KkG13RqIv8KXPhoT6KxLu86L1WB4RYuwSD5NGEMl8m45Hk6enApnyZcVq1MhqiFACtEBYS9bR_C0Lbri074P6sicJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رسانه‌های ایران ارائه خدمات بعضی از بانک‌ها از صبح امروز (شنبه، ۶ تیر ۱۴۰۵) دوباره مختل شده است؛ خبرگزاری ایسنا به بانک‌های ملی و صادرات در این زمینه اشاره کرده است.
شرکت خدمات انفورماتیک این اختلال را مرتبط با حمله سایبری دانسته است. در اطلاعیه این شرکت آمده است:
بررسی‌های فنی نشان می‌دهد این اختلال در امتداد آثار حمله سایبری پیشین بر زیرساخت‌های فنی و سامانه‌های متمرکز بانکی پدید آمده است.
هفته گذشته اعلام شد تمامی اختلال‌های پیش آمده در بانک‌های تجارت، ملی و صادرات برطرف شده است.
اختلال هفته پیش باعث شده بود که در بعضی موارد، حتی انجام عملیات خرید با کارت‌های بانکی هم امکان‌پذیر نباشد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 324K · <a href="https://t.me/VahidOnline/76710" target="_blank">📅 17:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76709">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgknjJUey_u93cKR7IWqykNkEf45Rf4E0KMVJVVKuKh85qEB-5yr37EBCFbuvh4qPosijVjffABXYTBjiJZg2QHJYjNTUrtV9QRIsYGWpoP0hr9vlxCLtSEcpMfNOURx3A017HzKgLE3jvaC6Z376NYadO3WkTWtfi5NVSeZSNN-AxYmpTANhaMN5MiiJKCSf7I_85DAaCLJcTWoe-v0Dj6CRTMRLHlZJ-I-XguW4Tyu_7Le7mu0CPQgeEYpl1n35WbV_Hyn6GcvKRthJTAsuxUK1MiHrtb6gSEdMwCfrxnzxTq37t7nJBpP8syXmrCh8rtY83IBtn50MUlQpZk0pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهنام گلخنی، پدر احمد گلخنی، از جان‌باختگان اعتراضات دی‌ماه ۱۴۰۴، روز چهارشنبه ۴ تیرماه در باغباد‌ران از توابع استان اصفهان بازداشت شده و با وجود وعده آزادی، همچنان در بازداشت به سر می‌برد.
کمیته پیگیری خبر داد آقای گلخنی پس از آن بازداشت شد که
در استوری اینستاگرام خود از مردم دعوت کرده بود تا ظهر عاشورا بر سر مزار جان‌باختگان اعتراضات حضور پیدا کنند.
بنابر این خبر قرار بود او روز شنبه ۶ تیرماه آزاد شود، اما با گذشت این موعد، همچنان در بازداشت است و اطلاعی از وضعیت پرونده یا اتهام‌های احتمالی او منتشر نشده است.
احمدرضا (احمد) گلخنی، شهروند ۳۷ تا ۳۹ ساله اهل باغبادران، در جریان اعتراضات دی‌ماه ۱۴۰۴ جان باخت. او مقابل کلانتری باغبادران هدف شلیک مستقیم قرار گرفته بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76709" target="_blank">📅 17:13 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76708">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUvY88qbyicehgnbevHZ1U2rareH6OFXoaOLz2eGSGSzIdztT5_cV-bcx_4kpqM2mJ59seof8biumDameK3RzEZa9DGcoIoqcbtx6jSlUxbywIlMrtxp5dQBetN9iBD302BqkFBsWUaphF6exX0V6BVzxIAtR8MAwErs8wPmMfz1GgEz00MFyds86o7ysQrAjpaTrO5c2jChGqsinih6hzEcQeQ6BMAMhxlCldq6b0WsRjgPcjZepe7zHhht6nh36GStn52cy9lPmfhAZt32dximMpFMO7M35kUA1o1yytFU5dc0EiRG6BGRc1QVymX-JHdvihVYeyR7Ze_NPJkQiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدیرعامل شرکت شهر فرودگاهی امام خمینی از برقراری دوباره پروازهای میان ایران و امارات تا پایان هفته جاری خبر داد و گفت: ایرلاین‌های داخلی مقدمات راه‌اندازی مجدد مسیر دوبی را فراهم کرده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 269K · <a href="https://t.me/VahidOnline/76708" target="_blank">📅 17:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76707">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/REvffQJWtPVa_4Def2i4n1tmuzG9IEbe9vAH83Rm40-ttP5J0dfw_9eefvYkXxpG-fjtxRbI1wy2AyxdH6_sok4TsegEB8ymqnw4sJyuBG_U5_Sq3SKNXJOKrwdwR9mP2AbmIz73Hmat3e4oHYd3E2Nqc6dBDEjQNy8Xx4RBQ6aDulgvfoOU63L_37Q93BapjOQwUqhOC4It_G-mkyiKQnnE1_n8rk5gYMDB2NOmAfDdc-tB6wzu45aztzEo_QvmFwZyaCumYqfiq8pVc5t2UGXb621fXXQclTfNgq3Cglx9EN-FzwH7elfYkHtam5N3OWitF6WyQxi3t-SNrR_M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزارت خارجه بحرین در بیانیه‌ای اعلام کرد جمهوری اسلامی بامداد شنبه با چند پهپاد به خاک این کشور حمله کرده است. این وزارتخانه با محکوم کردن این حمله، آن را نقض حاکمیت بحرین و تعهدات جمهوری اسلامی بر اساس تفاهم‌نامه اسلام‌آباد با آمریکا دانست.
در این بیانیه آمده است حمله پهپادی، نقض آشکار حاکمیت بحرین، تهدیدی علیه امنیت شهروندان و ساکنان این کشور و مغایر با قوانین و عرف‌های بین‌المللی است. وزارت خارجه بحرین همچنین اعلام کرد ادامه حملات جمهوری اسلامی، هم‌زمان با تلاش‌های منطقه‌ای و بین‌المللی برای کاهش تنش، روند صلح را تضعیف می‌کند و نشان‌دهنده رویکردی برای بی‌ثبات کردن منطقه است.
وزارت خارجه بحرین با اشاره به تفاهم‌نامه اسلام‌آباد افزود جمهوری اسلامی متعهد به توقف دائمی عملیات نظامی و احترام به حاکمیت کشورهای منطقه شده بود، اما حمله اخیر به گفته این وزارتخانه، نشان می‌دهد تهران به تعهدات خود و جامعه بین‌المللی پایبند نبوده است.
بحرین همچنین با تاکید بر حق خود برای دفاع از حاکمیت، امنیت و ثباتش، از شورای امنیت سازمان ملل خواست مسئولیت خود را در اجرای قطعنامه ۲۸۱۷ و پاسخگو کردن عامل این حمله بر عهده بگیرد.
@
VahidOOnLine
یک مقام آمریکایی که نخواست نامش فاش شود، به وال‌استریت ژورنال گفت حمله بامداد شنبه، ششم تیرماه ایران به بحرین شامل دو پهپاد انتحاری (یک‌طرفه) بوده است.
این مقام مسئول اظهار داشت که یکی از پهپادها توسط یک سامانه پدافند هوایی زمین‌پایه سرنگون شد و پهپاد دیگر بدون ایجاد هیچ‌گونه خسارت یا تلفاتی، در محوطه یک فرودگاه دورافتاده فرود آمد.
همچنین گزارش شده است که یک پهپاد انتحاری به نفتکشی حامل دو میلیون بشکه نفت خام اصابت کرده و نیروهای آمریکایی دو پهپاد دیگر را که کشتی‌های تجاری را هدف قرار داده بودند، سرنگون کرده‌اند.
@
VahidOOnLine
پس از اعلام دولت بحرین مبنی بر حمله پهپادی جمهوری اسلامی ایران به خاک این کشور در روز شنبه ششم تیرماه، کشورهای حوزه خلیج فارس این اقدام را به شدت محکوم کردند.
این حمله ساعاتی پس از آن رخ داد که سپاه پاسداران از هدف قرار دادن مواضع نظامی آمریکا در پاسخ به حملات سنتکام در بندر سیریک خبر داده بود.
وزارت امور خارجه امارات با صدور بیانیه‌ای، این حملات را «نقض فاحش» حاکمیت بحرین و تهدیدی برای امنیت منطقه توصیف کرد.
وزارت امور خارجه قطر نیز ضمن محکومیت این اقدام، بر لزوم پرهیز از پیامدهای این حملات «غیرموجه» و تداوم مسیر دیپلماسی برای حفظ دستاوردهای یادداشت تفاهم اخیر تأکید کرد.
در همین حال، وزارت امور خارجه کویت این تجاوزات را تضعیف‌کننده خطرناک تلاش‌ها برای صلح دانست و بر همبستگی کامل خود با بحرین تأکید کرد. جاسم محمد البدیوی، دبیرکل شورای همکاری خلیج فارس (GCC) نیز این حملات «خائنانه» را که به گفته وی زیرساخت‌های غیرنظامی را هدف قرار داده، به شدت محکوم کرد. این تنش‌ها در حالی اوج گرفته که از دو شب پیش و با حمله سپاه به یک کشتی باری سنگاپوری، فضای امنیتی در تنگه هرمز به‌شدت بحرانی شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 265K · <a href="https://t.me/VahidOnline/76707" target="_blank">📅 17:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76706">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/bk-hntBTz9kzMZHbeOF00KK9-58zcuK4pOuS_JhxIuxqFVZDgeSddzv5oLQY8GDRLn_Qy-CX7_CD6zexYyzKKMT6fxdO5vQE4kmh2L0_T4_e6ODgkRDcBqeBexOLyQh4RQROPVHAYEzHblBtZ3cdrVbjdtnFr3Iw2ki6dqYMRlcltN5syLKKbxFv613dtCrcZz45EYiigOnmCWd98Li3lhiAmeMsa60S6fXIz3Xv_w3fCjSBbZSS2wglHEMwjUXRxRnzfXLq3s8I5VQ8fPMUO7lMZSCStyyGxB5cB205znTH1f38bCsqz-LZtEnGtntx9DU190RlVH3rlmaRjx-nmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلومبرگ می‌گوید بررسی‌های داخلی وزارت دفاع آمریکا نشان می‌دهد مجموعه‌ای از نقص‌ها در سامانه‌های اطلاعاتی و هدف‌گیری ارتش این کشور ممکن است در حملهٔ موشکی به مدرسه میناب نقش داشته باشد.
بر اساس گزارش بلومبرگ که روز جمعه ششم تیر منتشر شد، یک تحلیلگر اطلاعاتی متوجه شده بود ساختمانی که در پایگاه دادهٔ ارتش آمریکا به‌عنوان یک تأسیسات نظامی ثبت شده بود، در واقع به دبستان تبدیل شده است.
به‌نوشتهٔ بلومبرگ، منابع آگاه گفته‌اند این ارزیابی در سال ۲۰۱۹ در یک سامانهٔ دیجیتال ثبت شد، اما آن سامانه به پایگاه دادهٔ رسمی هدف‌گیری ارتش متصل نبود.
مقام‌های رسمی آمریکا تا کنون جزئیات این گزارش را تأیید یا رد نکرده‌اند.
بلومبرگ می‌نویسد تحقیقات پنتاگون همچنین بر ضعف‌های دیرینهٔ سامانه‌های اطلاعاتی ارتش آمریکا از جمله استفاده از پایگاه‌های دادهٔ قدیمی و نبودِ ارتباط کامل میان سامانه‌های مختلف متمرکز است. این گزارش می‌افزاید هنوز مشخص نیست فرماندهی مرکزی ارتش آمریکا، سنتکام، پیش از حمله از فرایند تکمیلی بازبینی اهداف استفاده کرده است یا نه.
وزارت دفاع آمریکا اعلام کرده است تحقیقات دربارهٔ این حمله همچنان ادامه دارد و جزئیات تازه‌ای ارائه نکرده است. دونالد ترامپ نیز گفته است ممکن است هرگز مشخص نشود چه کسی مقصر بوده و خود او هنوز مدرکی ندیده که قانعش کند آمریکا مقصر بوده است.
ایران می‌گوید در حملهٔ هوایی به مدرسهٔ میناب که ۹ اسفند پارسال در نخستین روز حملات آمریکا و اسرائیل به ایران صورت گرفت، دست‌کم ۱۷۵ نفر از جمله ۱۶۸ دانش‌آموز کشته شدند. شورای تشکل‌های صنفی فرهنگیان تأیید کرده که در این حمله بیش از ۱۰۸ دانش‌آموز کشته شده‌اند و گفته است معلمان هم در میان قربانیان این حمله بوده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76706" target="_blank">📅 17:07 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76705">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/FxXIQc-H78CLFBiOdFTk-BzjPhrGeDqsa_pKLnCfS7YxdOtswSEp1f33wnCw6xjaFXtZeHInT3izQQEjNXpSbQ4MQgMqLf8m7zNi_kr6uuRAVpnAN6t1SEHrY7XPeER0N4P1gCEg3-tpNBAAGihBzNxZMwCSgDJOQaYtt1RKFhpFWB-k97BKOJNSjnIoL7bUiGKHaUA7U9jDMkOCgIMx_ubJFRhjmZWNZmMUIioueziGdLxFJy_VOZZB3hgm8bstz94gslBRKmU17V2iQ5CiPuOedPwdUTlIwoWuX0GByg6xDGaml4_lgQ0rfICdk8HQIQ9I3-D_N1zysFtZCm5Wkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">"یاسین محمودی، نوجوان ۱۶ ساله و اهل رفسنجان در استان کرمان، در جریان اعتراضات مردمی این شهر با شلیک مستقیم نیروهای حکومتی جان خود را از دست داده است.
بنابر اطلاع ایران‌وایر، یاسین محمودی روز جمعه ۱۹ دی‌ماه ۱۴۰۴ در خیابان طالقانی، ابتدای سه‌راه امیرکبیر رفسنجان، هدف شلیک مستقیم نیروهای حکومتی قرار گرفت.
گلوله به ناحیه شکم این نوجوان اصابت کرد و او بر اثر شدت جراحات جان باخت."
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76705" target="_blank">📅 17:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76704">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/LoNG14ew1SQdx9VjCcUkzNgZpvXRtcwG4gPnaK3rLWWhNeOaRJ3jc3t06xgq-dKrRjbWSG55KovISGA6rgrT7MdbJNjjXfpMGbAFK0ZJpZ0KBOmJMdvyaR2YJd0rOX8R734gnTPXcxs1rWylMkHeSzB6ajB716hWtIpSKYiJvMkiHVlSgq9aCx8yvBTRJZ0Gxnh_rr41gk7hZlUIfcZsY5bafssxGSVo4x4eUrN74trmaBtYzUUVSFsDK3bscINFpJA4W922xiWCGNFg2ryNIwVj51X95n4i7865K1ulidrRiiIXuJ3yHYumAjh6zsNfICKtYYcmRb_OBWRM3REycw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسابقه فوتبال ایران و مصر با نتیجه مساوی یک یک به پایان رسید.
بلژیک با پیروزی ۵ به یک بر نیوزیلند و مصر هم با ۵ امتیاز و به‌دلیل تفاضل گل کمتر، به عنوان تیم‌های اول و دوم به مرحله حذفی صعود کردند.
به این ترتیب صعود ایران به نتیجه بازی‌های غنا با کرواسی، ازبکستان با کنگو و الجزایر با اتریش گره خورده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76704" target="_blank">📅 08:46 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76703">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=ZHbVvKP5wnp8LLPO36HZY8GOeC0cJl6BK0aPLbM_NiQpu5tTXbSM0R0FUtkjvO9N0KiXDn5TWYp6TmDLqQ6EL_MIRJ14qYqD42Hk4Yd2GeyEGVJv0_G9dgMFkrhSTRHTEtZiduRJCTbk_ZwhzJG3V8CBmT-S9oJDDHovHpqWx-7iGI1QTYPaH0tujuNNLY5L5ExaZVBUd06paJQ1IvlypRLetnw7rn0hLUKnVCOz4bLtKU3P7Q-JLqt577HpBNQiY78yWFqL6Y2UIf9EJa3z3jdq6PaAcraRJ6BGzXlh6waoYJ49lMn7czblew5oaPc4ZWTu9cAxworj5x0-sa_FvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dd3a93fc06.mp4?token=ZHbVvKP5wnp8LLPO36HZY8GOeC0cJl6BK0aPLbM_NiQpu5tTXbSM0R0FUtkjvO9N0KiXDn5TWYp6TmDLqQ6EL_MIRJ14qYqD42Hk4Yd2GeyEGVJv0_G9dgMFkrhSTRHTEtZiduRJCTbk_ZwhzJG3V8CBmT-S9oJDDHovHpqWx-7iGI1QTYPaH0tujuNNLY5L5ExaZVBUd06paJQ1IvlypRLetnw7rn0hLUKnVCOz4bLtKU3P7Q-JLqt577HpBNQiY78yWFqL6Y2UIf9EJa3z3jdq6PaAcraRJ6BGzXlh6waoYJ49lMn7czblew5oaPc4ZWTu9cAxworj5x0-sa_FvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم  ترجمه ماشین: حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری  تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی…</div>
<div class="tg-footer">👁️ 380K · <a href="https://t.me/VahidOnline/76703" target="_blank">📅 06:00 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76702">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYP2kNQ3-ShxkuzdXM0U7CnRznbhGesLPCWstbd6ZoL5hJljJEXMy0ACAgFOULDCcSu7IAmhgxvocUNsK6_BXHPL3moqv501qYkdTkXw33RgaCLIQ0zVrN3oAJakWrZfOc7YbiG58o_oQfsdLgw5XwAjGd6FxdkwHEiF_TziHwzJqXCsV87DzBKnR1AqY0pdfJKZDXGc1yujf6vrh02-cF13UEUOYVixqe8ifzyVAg51BG3Y0QszC0dqLYqVMIX1tBlHhoybVrGczl30nN53icWRPPE8ycZWwmYTd-t1Rl4fZEAXSpfUArq80D0OO_PC7-ArJdwEXNX-i_FcqewOkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌سپاه پاسداران اعلام کرد که نیروی دریایی این نهاد در واکنش به حملات آمریکا به سواحل ایران، مواضع ارتش آمریکا در منطقه را هدف قرار داده است.
در بیانیه روابط عمومی سپاه آمده است که آمریکا پس از حمله به یک کشتی تجاری در تنگه هرمز، به بهانه عبور این کشتی از مسیری که ایران آن را «غیرمجاز» می‌داند، حملاتی هوایی به سواحل ایران انجام داده است.
سپاه این حملات را نقض آتش‌بس و تعهدات آمریکا خواند و مدعی شد در پاسخ، «نقاط استقرار ارتش آمریکا در منطقه» هدف قرار گرفته‌اند. جزئیاتی درباره محل این اهداف، نوع حمله یا خسارات احتمالی منتشر نشده است.
در این بیانیه همچنین گفته شده است که بر اساس بند پنجم تفاهم‌نامه اسلام‌آباد، کنترل عبور و مرور در تنگه هرمز بر عهده ایران است.
سپاه هشدار داد که در صورت تکرار حملات آمریکا، پاسخ ایران گسترده‌تر خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 392K · <a href="https://t.me/VahidOnline/76702" target="_blank">📅 03:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76701">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/iSxhVmC8CIE4iHS4g6Bj6qB1eUyWQ_v_P7TzzJBp-Yu6U8rmTuiovMY0k6TYSVr7Pb9olLaRlXJhOZdn602GbagWWvfwaOUTq5jroi0Ubwg9sy1xgP5xxTXyqT6AOxqFllUldiDKZn2g47WvlRpKHXDY6ZQZdHg0oO_sP_6oyeGzdmx0YGj4JIH-YGLo8OYusU0Gbjx5I3JOwTk77i5DJeQsBsTPbnObT6zC8JS8D-Zw42pL1t5djTT31b77qYA5l06PQzKejn3Ucl7ct09KT5ehulZahKJD9yojxP9ktuFOLBBDq2pN-HK6YuBgjw_vlsnAdtv3mhbcsMTwdx2NfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡️
رسانه‌های داخلی در ایران از درگیری مسلحانه میان نیروهای حکومتی و گروه‌های مخالف مسلح در «ایست بازرسی بانه - سقز» خبر دادند. گزارش‌های اولیه آنها حاکی از آن است که دو نفر از نیروهای حکومتی کشته‌ شده‌اند. همچنین گزارش شده است که پنج نفر دیگر نیز مجروح شده‌اند. جزئیات بیشتری منتشر نشده است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 378K · <a href="https://t.me/VahidOnline/76701" target="_blank">📅 01:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76700">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/nHHEdHxl4sUhPDNDNipAvt3kDim1b0LCEkkEI_-Eg0Xql7ZQDrQ_3XcLlRR9iK6wTqwUn2ViUTE86dOskNS5zsLXcPdayNwM7OPNcP4JhVpT5foG75efiSFXZ1dpoqIsfcWtZEFX5yDqX22mqEeiokUTic5a6oWkVwS9LzzO0bPKG6VAMCLrQuT8_6sTwF5RURMFwBMS0wgkgqy9aaQYJZrml_gARn0waNj9JsQ5dnclpykvzUxighdCYeMMWZtICmFoD5vszjpEEgaft9kOkSUTpapVRUMYDyveINnfUrJu9RGXdkg_llOiIb4_JseqjFvHqLiJk2X-s9aOKqQY4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنتکام: انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادیم
ترجمه ماشین:
حملات آمریکا به ایران در پاسخ به حمله به کشتی تجاری
تامپا، فلوریدا — نیروهای فرماندهی مرکزی آمریکا (CENTCOM) در ۲۶ ژوئن، در واکنشی قدرتمند به حمله دیروز به یک کشتی تجاری که در حال عبور از تنگه هرمز بود، حملاتی علیه ایران انجام دادند.
هواپیماهای آمریکایی پس از آن‌که ایران در ۲۵ ژوئن با یک پهپاد تهاجمی یک‌طرفه به کشتی M/V Ever Lovely حمله کرد،
انبارهای موشک و پهپاد ایران و سایت‌های راداری ساحلی را هدف قرار دادند.
این کشتی باری با پرچم سنگاپور، هنگام حمله ایران، در امتداد ساحل عمان در حال خروج از تنگه هرمز بود.
این تجاوز بی‌دلیل نیروهای ایرانی علیه کشتیرانی تجاری، آشکارا آتش‌بس را نقض کرد. افزون بر این، رفتار خطرناک ایران آزادی کشتیرانی را تضعیف کرد؛ آن هم در حالی که جریان تجارت به‌طور فزاینده‌ای از این کریدور حیاتی تجارت بین‌المللی عبور می‌کند.
نیروهای CENTCOM همچنان هماهنگی و پشتیبانی برای عبور امن کشتی‌های تجاری از این تنگه را فراهم می‌کنند. ارتش آمریکا همچنان حاضر و هوشیار است تا اطمینان حاصل کند که همه جنبه‌های توافق با ایران رعایت و اجرا می‌شود و کاملاً به قوت خود باقی است.
CENTCOM
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 383K · <a href="https://t.me/VahidOnline/76700" target="_blank">📅 00:14 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76699">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Kb0qLz8PQlR-GUx-6W32srdB91vQP6vl6rMtAjTF2rnvThPzTyr4HKkicIyQ1JR7x1rwN1y2HQLPwWvuT2gPU7otqVw3IeEimAHTdRw91ICf-dlbe9tbksLssX7luvrtd_2-iiqsw4Jp87B5JnQetoHILe8zqEHIX8wvLNtrU6ZjU7ekB-k5U5-L5osTnTfYtSdNaLdBASmUNa7dgZFjWTaOpk-7wGbKhnUAAe3VQASApkdV2cmShnAxWjZVJ5PIULb-0Zr9Vg6aLOlYwtdufdHGXzzU7MsjAznnWkfTZ51ENMnLmuwYYfg4FwNEj8_aPBibk-RbeKMJBzCJ0TCpwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صدا و سیما:
دقایقی قبل ؛ شنیده شدن صدای انفجار در طاهرویه سیریک
منشأ صدا هنوز مشخص نمی‌باشد.
اطلاعات تکمیلی متعاقبا اعلام می‌گردد.
من ساعت ۲۳:۳۰ این پیام‌ها رو دریافت کرده بودم:
اسکله طاهرو رو زد  ۳ ،۴ بار
زده بطرف تنگه
سیریک گروگ سه تا صدای انفجار
آپدیت:
تکمیلی| به گزارش خبرنگار صداوسیما در سیریک:
ساعت ۲۳ و پانزده دقیقه امشب صدای انفجار در اسکله طاهرویی سیریک شنیده شد.
یک منبع آگاه نظامی علت این انفجارها را اصابت پرتابه به محدوده اسکله طاهرویی سیریک بیان کرد.
این منبع آگاه نظامی گفت: حدود ۵ ساعت پیش چند شلیک اخطار از شهرستان سیریک به شناورهای متخلف‌ در تنگه هرمز پرتاب شد.
همچنین شنیده ها از شلیک دو موشک اخطار ساعاتی پیش از حوالی کرپان به سمت تنگه هرمز حکایت دارد.
و
خبرنگار آکسیوس به نقل از یک مقام آمریکایی، جمعه‌شب، پنجم تیرماه، گزارش داد: «ارتش ایالات متحده حملاتی را در منطقه تنگه هرمز انجام داده است». پیش از این، صداوسیما از شنیده‌شدن سه انفجار در طاهرویه سیریک خبر داده بود.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 355K · <a href="https://t.me/VahidOnline/76699" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76698">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1ODfUQ_CTuOyXH7sc7sbChXOT-E5-XVz3AJd6ngistyoImg5FH-AJDq4Z9ASTXnK-mWfXNj1LJneivSSAYwslcVo6G7wkFjWikedexZy4mG3axdpLMsBxF94tZlV43pqY-IfIHG6H3S6fgc1HWwbpw36qPZ0yxHIl-cARtOc-rop9XPmkQPhUXVJec9prNIrvapzB1Nl9-jhi1totbVYRti7QfyswdRxjzFPKgo3N4tGtW933nIFfC6aE70fCQUmTh1tnxDPffdhhqaAVx5cTzeG2lllQJpz2efbrimpn8ZOei3WJi2QiQOUamMxJh5rmYbavBHetVLGpQ5JUU9p-uZE" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/83b030969e.mp4?token=eYP_tEYlef5B6bKmWYpsINoiBQxHIaeanis2vpWmPnf1oMgeYe6MDWjfySTYKhRuqqJn8hD2LYlXWEQXHfXc17V1s_vlcdqstP1oAV-dSW9UJ-H3gjkjNk4BGunQ3U-vCwoOBmgBZD6aVYjQ7_Q-IxfGLKdHDXIi2BiZ40VN8G_LdyVovc8UEWgWX7iDgHEyF3mtDiGxdu5mIWxEyAGmSKVeqHLRKfaHaPPj-2my8dlgQPVQJjyoA_g8s72ePoshj9nZHD7zOWXRHAAhZTI4mE-4YfaXB1JlkE3vkB-JWEuC2n3N1FwOgKa93QcANP5FoGEYWxozrPSF8x-N97U1ODfUQ_CTuOyXH7sc7sbChXOT-E5-XVz3AJd6ngistyoImg5FH-AJDq4Z9ASTXnK-mWfXNj1LJneivSSAYwslcVo6G7wkFjWikedexZy4mG3axdpLMsBxF94tZlV43pqY-IfIHG6H3S6fgc1HWwbpw36qPZ0yxHIl-cARtOc-rop9XPmkQPhUXVJec9prNIrvapzB1Nl9-jhi1totbVYRti7QfyswdRxjzFPKgo3N4tGtW933nIFfC6aE70fCQUmTh1tnxDPffdhhqaAVx5cTzeG2lllQJpz2efbrimpn8ZOei3WJi2QiQOUamMxJh5rmYbavBHetVLGpQ5JUU9p-uZE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بخش مرتبط با ایران در سخنرانی ترامپ به تشخیص ماشین
متن  زیرنویس:
https://telegra.ph/trump-06-26-4
بعضی از جملات:
ایران هرگز سلاح هسته‌ای نخواهد داشت. نمی‌گذاریم چنین اتفاقی بیفتد.
و به لطف قدرت و مهارت نیروهای مسلح ایالات متحده، ایران امروز نه نیروی دریایی دارد، نه نیروی هوایی، نه توان پدافند هوایی، نه رادار، و عملا نه تولیدی. ظرفیت پهپادی‌شان ۸۲ درصد کاهش یافته است. ظرفیت موشکی‌شان ۸۰ درصد کاهش یافته است. پرتابگرهای موشکی‌شان ۹۰ درصد کاهش یافته است. رهبری‌شان یک بار کشته شده، و رهبری‌شان برای بار دوم هم کشته شده.
و دیگر هیچ‌کس نمی‌خواهد رهبر ایران شود. گفتند: «چه کسی می‌خواهد رئیس‌جمهور شود؟» بعد همه گفتند: «نه، ممنون.»
این کار باید در دوره ۴۷ ساله‌ای انجام می‌شد که آن‌ها با ترور حکومت کردند. و همین کار را کردند. با ترور حکومت کردند. وقتی مرد یا زن جوانی را می‌بینید که بدون پا یا بدون دست راه می‌رود، یا چهره‌ای که از بین رفته، این به خاطر بمب کنار جاده‌ای بود که ساخته شد؛ ساخته ژنرال سلیمانی، که من در دوره اولم او را کشتم. و آن یک کشتن بزرگ بود.
هنوز می‌توانند شلیک کنند؛ می‌دانید، دیروز یک پهپاد را به سوی یک کشتی بزرگ که وارد تنگه هرمز می‌شد شلیک کردند. چهار تا شلیک کردند. ما سه تای آن‌ها را ساقط کردیم. یکی از آن‌ها؛ فکر کنم؛ ما از دستش ندادیم. کسی آمدنش را ندید و به کشتی خورد و مقداری خسارت زد. اما نمی‌توانند چنین کارهایی بکنند.
و فراموش نکنید وقتی باراک حسین اوباما JCPOA را انجام داد. ببینید، اگر به آن نگاه کنید، باراک حسین اوباما؛ اسمش را شنیده‌اید؟ او فاجعه بود. فاجعه بود. او ۱.۷ میلیارد دلار پول نقد به آن‌ها داد. ۱.۷ میلیارد دلار پول نقد و ده‌ها میلیارد دلار. آن را به ایران داد. فکر می‌کرد می‌تواند دوستی آن‌ها را بخرد. و دقیقا برعکس شد. آن‌ها از پول استفاده کردند و موشک ساختند و هر چیز دیگری.
و من برجام را لغو کردم؛ توافقی که... همان توافق هسته‌ای ایران بود؛ فاجعه بود. ضمنا مدت‌ها پیش منقضی شده بود، اما من مدت‌ها قبل از انقضایش لغوش کردم. اگر این کار را نمی‌کردم، ایران سلاح هسته‌ای داشت. اگر ۱۰ ماه پیش بمب‌افکن‌های B-2 را نفرستاده بودم، آن‌ها سلاح هسته‌ای داشتند. ما آن تأسیسات هسته‌ای را نابود کردیم. بسیار مهم بود.
و آن وقت دیگر اسرائیلی نداشتید. اسرائیل نابود شده بود. می‌دانم در این اتاق طرفداران خوب اسرائیل زیاد دارید. و اسرائیل نابود شده بود و احتمالا خاورمیانه هم نابود شده بود. و ما... آن‌ها می‌توانستند ضربه‌ای بزنند. ما خیلی سریع نابودشان می‌کردیم، اما آن‌ها می‌توانستند به ما هم ضربه‌ای بزنند.
بازار سهام از زمان انتخابات ۷۳ رکورد تاریخی ثبت کرده است. و امروز شمار بیشتری از آمریکایی‌ها نسبت به هر زمان دیگری در تاریخ کشورمان مشغول کارند. این خیلی خوب است.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 329K · <a href="https://t.me/VahidOnline/76698" target="_blank">📅 23:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76696">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/S5ycXEqs827Oo_rdjMIdcx8pH1WXv9SC13Q24fblwdw-ZxRLjObSpyKE02V5_PLAd5bSqzhMmrOcQgx_S1kEIIqcfeYRMKQVt6Eo5wllao9nUn6BGuKRx2PNoEjmnI31-YMJrVVlhrNmk5U4Lb1emoe1UKSMq00isDBmXHXDQRTTn_EbzQI4_b-Y8QWCHhNXMWHBLp1Efq2aUV5v40elFsWnuoGB23WOfMwYqLVN5vSZ86aVQEWKMWh7YpicKm3VIpV4PDSmaaZHl1Lbn6BDeVmZUVqFIvofUnA3edjTR9ghPjBHLCPfsBq9KHFIuNIROScIwtUdwwDVnkqz9oOUXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/H-mDo-QAqOgg84PwBpWh2aW3A1ABz5yI2sz6Rt8_Zw6HrMxG-0AeS39zSWG4ewdikCL8FrxUIUA2bS1apI4GBcZwtD7E52ITzSuHWVpjGV_REmiGq4EAG51uD9CYTmJ24hYMOBHEstB9b_E-BvfNi8NRR2ecTYrcP3NJ3sCPE0_xU1Y6jV2y65zT4wqOFphNuLmbVKLKdmAsAYr7YVY5A4dWRI7q0iRsTcw2NHP-iqiw6g73YtQ2BiuwDIREzNWmtLU2eRJZXvIASD2rBoWlgPDff9_dykRg7lNq6UAqTeBe5vvDydB3JRKA2zViMLZJvuP_t2DdVhu-sMrlQONTuw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، پس از امضای توافق اسرائیل و لبنان در واشینگتن در بیانیه‌ای اعلام کرد: «این توافق دستاورد بزرگی برای اسرائیل است و مذاکرات طولانی در واشنگتن به نتیجه رسیده است. مهم‌ترین نکته این است که اسرائیل در منطقه امنیتی باقی می‌ماند و تا زمانی که حزب‌الله خلع سلاح نشود این وضعیت ادامه خواهد داشت.»
او افزود: «این توافق ضربه بزرگی به جمهوری اسلامی است و تهران تلاش می‌کند اسرائیل را به عقب‌نشینی وادار کند اما اسرائیل، لبنان و آمریکا تاکید کرده‌اند که جمهوری اسلامی و حزب‌الله در این روند نقشی ندارند.»
نتانیاهو تاکید کرد: «اسرائیل در منطقه امنیتی باقی خواهد ماند و اجازه ورود حزب‌الله یا غیرنظامیان به این گروه داده نخواهد شد.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 303K · <a href="https://t.me/VahidOnline/76696" target="_blank">📅 22:31 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76695">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=pIwed5cI2XhHGjQmFEHeYzgmIx8xCx5LzBia_wWOm7EnN3o5W3JZ4AnsUOU2wpcNkSgoepNqyRA-GN4APneIfViAo9sLy8A5VIM0hh-D0j_U11YSXCzXexZ7FvoBYkag-k1-yq-Q1vAsDjMdudSXAHDtnvLJYtJ2ht4LlCkHKwi-dEQ2tdFlq_HWeVhxCEXaM64eiCECkAhj3PQeIEkKHnu_7DPBNVRfxFdyO0XOUXmljZtmZII2RsxkUc6ro2UzFJ_5kZJA1YX-IrPbbkHw-IumHLyD7ag4WVQwxc4j9WiL6begC51lSleSPbxebbZSIXEb30VuitBUthDHdVDOVA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ef9babce7e.mp4?token=pIwed5cI2XhHGjQmFEHeYzgmIx8xCx5LzBia_wWOm7EnN3o5W3JZ4AnsUOU2wpcNkSgoepNqyRA-GN4APneIfViAo9sLy8A5VIM0hh-D0j_U11YSXCzXexZ7FvoBYkag-k1-yq-Q1vAsDjMdudSXAHDtnvLJYtJ2ht4LlCkHKwi-dEQ2tdFlq_HWeVhxCEXaM64eiCECkAhj3PQeIEkKHnu_7DPBNVRfxFdyO0XOUXmljZtmZII2RsxkUc6ro2UzFJ_5kZJA1YX-IrPbbkHw-IumHLyD7ag4WVQwxc4j9WiL6begC51lSleSPbxebbZSIXEb30VuitBUthDHdVDOVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم.
ویدیوی بالا درباره ایران نیست.:
ترجمه ماشین: همان‌طور که دیدید، کمونیست‌هایی که اخیراً در شهر نیویورک انتخاب شدند، سوسیال‌دموکرات نیستند. آن‌ها می‌خواهند شیوه سنتی زندگی آمریکایی را کاملاً نابود کنند.
فروختن کمونیسم خیلی آسان است. همه‌چیز را نابود می‌کند، اما فروختنش خیلی آسان است. صادقانه بگویم، فکر می‌کنم من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. می‌گفتم اجاره رایگان است؛ خانم‌ها و آقایان، از این به بعد لازم نیست هیچ اجاره‌ای بدهید. از این به بعد هر کسی خانه می‌خواهد، نگران نباشد؛ فقط خانه‌ای را که می‌خواهد انتخاب کند. همه غذای رایگان می‌گیرند؛ از این لحظه به بعد همه‌چیز رایگان است. همه به من رأی می‌دادند.
مشکل اینجاست که بعد از دو یا سه سال، کشور به منطقه‌ای فاجعه‌زده تبدیل می‌شود. کشور شکست می‌خورد. همیشه همین‌طور می‌شود. فروختنش خیلی آسان است. آن سال اول، آدم فوق‌العاده محبوبی هستید. همین حالا هم این اتفاق در نیویورک و کالیفرنیا دارد می‌افتد.
اما بعد شروع می‌کنید به زندگی در فلاکت. در فلاکت زندگی خواهید کرد. غذایی وجود نخواهد داشت. مسکنی وجود نخواهد داشت. ارتشی وجود نخواهد داشت. قانون و نظمی وجود نخواهد داشت. هیچ‌چیزی وجود نخواهد داشت. از هر نظر به ساکن جهان سوم تبدیل می‌شوید و همه رنج خواهند کشید یا خواهند مرد. رنج می‌کشید یا می‌میرید. این همان چیزی است که اتفاق می‌افتد. هزاران سال است که این اتفاق با نام‌های مختلف افتاده است.
به شما می‌گویم، من می‌توانستم بزرگ‌ترین کمونیست تاریخ باشم. خیلی آسان بود. لازم نبود کار کنید؛ می‌توانستید در خانه بمانید. مشکل این است که چند سال می‌گذرد و کل آنجا فرو می‌پاشد. همیشه همین‌طور می‌شود؛ همیشه همین‌طور بوده است.
اما متأسفم که بگویم ترور کسانی که با آن‌ها مخالف‌اند، عنصر بسیار مهمی در ایدئولوژی آن‌هاست. ترور برای آن‌ها مسئله بزرگی است. آن‌ها حیوان‌اند. حیوان‌اند.
در خیلی از موارد باهوش نیستند، اما در بعضی موارد هستند. جذب پیرو برایشان آسان است، چون وعده‌هایی می‌دهند که خودشان می‌دانند نمی‌توانند عملی کنند. و دموکرات‌ها هم مقابله نمی‌کنند. برای همین احمق‌اند. مقابله نمی‌کنند. می‌ترسند. من شومر [احتمالاً اشاره به چاک شومر] را می‌بینم؛ از جنگیدن می‌ترسد. آدم‌هایی را می‌بینم که نسبتاً معمولی‌اند و آدم‌هایی که ما با آن‌ها مخالفیم؛ آن‌ها از جنگیدن می‌ترسند.
دموکرات‌ها چرخش عظیمی به چپ داشته‌اند. من به بعضی از کسانی که آن شب در نیویورک انتخاب شدند نگاه کردم. این‌ها از خیلی جهات آدم‌های احمقی‌اند؛ از بعضی جهات از نظر فکری احتمالاً نسبتاً باهوش‌اند، اما آدم‌هایی هستند که می‌خواهند کشور ما را نابود کنند. آن‌ها از کشور ما متنفرند. از مردم ما متنفرند. از حزب دموکرات متنفرند.
حزب دموکرات در دردسر بزرگی است، چون این ماجرا با نیویورک متوقف نمی‌شود. این مسیر، انتخاب شدن را بیش از حد آسان می‌کند. همه‌چیز، به نوعی، برای انتخاب شدن بیش از حد آسان است. بسیار خطرناک است، اما به‌زودی چیزی برایتان باقی نمی‌ماند. مشکل همین است.
از خیلی جهات، آن‌ها اجازه می‌دهند این افراد راه خودشان را بروند و هر کاری می‌خواهند بکنند. می‌گویند نمی‌خواهیم ریسک کنیم و حرف بدی بزنیم، چون می‌ترسیم اگر این کار را بکنیم شغل‌مان را از دست بدهیم. می‌ترسند انتخابات خودشان را ببازند، حتی اگر فقط به گفتن چیزی درباره این نسل تازه آدم‌های بیمار فکر کنند.
آن‌ها آن‌قدر باهوش یا سرسخت نیستند که با طاعونی که در جریان است بجنگند. این دارد درست جلوی چشم شما اتفاق می‌افتد. اگر همان‌طور که با جمهوری‌خواهان می‌جنگند، یا همان‌طور که با من می‌جنگند، با آن‌ها می‌جنگیدند، پیروز می‌شدند. آن‌ها ما را شکست ندادند، اما در برابر کمونیست‌ها پیروز می‌شدند؛ ولی شجاعت این کار را ندارند.
پس خودشان دارند کمونیست می‌شوند و به یک حزب کمونیست تبدیل می‌شوند. این‌ها سوسیال‌دموکرات نیستند. این‌ها کمونیست‌های سرسخت و بی‌خدا هستند. کمونیست‌های بی‌خدا هستند. همه کمونیست‌ها بی‌خدا هستند. به خدا باور ندارند.
به نظر من، این جدی‌ترین تهدید علیه کشور ما از زمان تأسیس آن، حدود ۲۵۰ سال پیش، است. این تهدید بزرگی برای کشور ماست.
درباره ایران هم:
ترامپ در کنفرانس سیاست‌گذاری ۲۰۲۶ ائتلاف ایمان و آزادی، گفت: نمی‌توانیم اجازه دهیم ایران سلاح هسته‌ای داشته باشد. نمی‌توانیم بگذاریم این اتفاق بیفتد.
آن‌ها دارند از شدت نیاز برای رسیدن به توافق التماس می‌کنند. آن‌ها خیلی چیزها به ما می‌دهند. این باید در طول ۴۷ سالی که با ترور حکومت کرده‌اند انجام می‌شد.
رسانه‌های جعلی می‌گویند آن‌ها امروز خیلی قوی‌تر از چهار ماه پیش است اما آن‌ها اکنون خیلی چیزها به ما می‌دهند.
@
VahidOOnLine
📡
@VahidOnlin</div>
<div class="tg-footer">👁️ 291K · <a href="https://t.me/VahidOnline/76695" target="_blank">📅 22:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76694">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=Y3LQ5ufS3U5qtQN_kFExA8825JENUq2_ogRZrZzjZMEnS_0o4c224hlRjaBxj7XUbu_k5B2JTh_bzs6sEvdIlfctLrJc8ZKyDmxG_cTrJTIpMGo4WUYygVUVzMFDAtlcm_JzwMGlhXxEMuc9kx8pysOwawpVFI1JLimEyhOVQ2TOqIf9CUlB_Uo7HTRkhE0NwilXKPro9fcSc67o8JEDbYm2BX_nGEvNhvcfV9-jCO027z48fncvAtIBOA38H6-UeGPdnHWZWKI9qx7YZpNMgJtygnjqZsEZdfuzs399EACvJkoXb2buKeY9xBdlSf27wtIVWos7UD5YoUkiMXrvPA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/33272eb3ad.mp4?token=Y3LQ5ufS3U5qtQN_kFExA8825JENUq2_ogRZrZzjZMEnS_0o4c224hlRjaBxj7XUbu_k5B2JTh_bzs6sEvdIlfctLrJc8ZKyDmxG_cTrJTIpMGo4WUYygVUVzMFDAtlcm_JzwMGlhXxEMuc9kx8pysOwawpVFI1JLimEyhOVQ2TOqIf9CUlB_Uo7HTRkhE0NwilXKPro9fcSc67o8JEDbYm2BX_nGEvNhvcfV9-jCO027z48fncvAtIBOA38H6-UeGPdnHWZWKI9qx7YZpNMgJtygnjqZsEZdfuzs399EACvJkoXb2buKeY9xBdlSf27wtIVWos7UD5YoUkiMXrvPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مذاکره‌کنندگان ایالات متحده، اسرائیل و لبنان پس از پنجمین دور از گفتگوهای دیپلماتیک، روز جمعه پنجم تیرماه، یک چارچوب سه‌جانبه را امضا کردند.
این مذاکرات شامل بررسی پیشنهادی با حمایت آمریکا بود که بر اساس آن، نیروهای اسرائیلی بخشی از قلمرو تحت اشغال خود را به ارتش لبنان واگذار کنند.
پیش از آغاز این دور از گفتگوها، لبنان خواهان خروج کامل نیروهای اسرائیلی از خاک این کشور بود؛ در حالی که برای اسرائیل، شرط اصلی هرگونه عقب‌نشینی، خلع سلاح کامل حزب‌الله و دریافت تضمین برای بازنگشتن نظامی این گروه به مناطق مرزی است.
روبیو در مراسم امضای این توافق‌نامه گفت: «این آغازِ آغاز است. کارهای زیادی در پیش داریم. امروز اولین قدم است و گاهی اوقات، اولین قدم سخت‌ترین قدم است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76694" target="_blank">📅 21:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76692">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=AACS_qPcc5Wn81uDVuyW9iXJwSQLBe2k_aXviiGgJAUmD9EV4dxo2xTH4NrpIcDh5a0e1wbJ32d901TcURFNazbZhm4pQjI8Fg0ICpukXeK7G1v9gRW-2291XEhun6WjlREZO2JyZFEa8VdGFg7QWO09thWBbOpbhX7v9TdSX1a2Xv2krjIy4VLilKfJK9jS8NUu_YFGsM9zrbopFTUc7M2bmNP6CbzypLSIhnoxfcrsOUs8VnswcxCL0oaFC9syeZ9HtiyNUeb6xhf_RzfGZ3g9nd1ZpkRtxtvevnYbDtVodTZza4a4OcUTa6FWd5ll1QX8V-_W1DxiGcrbNfLzvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bade4bfa29.mp4?token=AACS_qPcc5Wn81uDVuyW9iXJwSQLBe2k_aXviiGgJAUmD9EV4dxo2xTH4NrpIcDh5a0e1wbJ32d901TcURFNazbZhm4pQjI8Fg0ICpukXeK7G1v9gRW-2291XEhun6WjlREZO2JyZFEa8VdGFg7QWO09thWBbOpbhX7v9TdSX1a2Xv2krjIy4VLilKfJK9jS8NUu_YFGsM9zrbopFTUc7M2bmNP6CbzypLSIhnoxfcrsOUs8VnswcxCL0oaFC9syeZ9HtiyNUeb6xhf_RzfGZ3g9nd1ZpkRtxtvevnYbDtVodTZza4a4OcUTa6FWd5ll1QX8V-_W1DxiGcrbNfLzvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در حالی که امدادگران در ونزوئلا همچنان در جستجوی بازماندگان زلزله‌های ویرانگر شامگاه چهارشنبه در میان ساختمان‌های فروریخته هستند، تازه‌ترین گزارش‌ها، حاکی از کشته شدن بیش از ۵۸۰ نفر و زخمی شدن حدود سه هزار نفر بر اثر این حادثه است.
بیم آن می‌رود که شمار قربانیان بسیار بیشتر باشد. بسیاری بی‌خانمان شده‌اند یا به دلیل آسیب‌دیدگی و ناامن بودن ساختمان‌ها، از بازگشت به خانه‌های خود هراس دارند.
در کاراکاس، پایتخت ونزوئلا، و شهر ساحلی نزدیک آن، صدای افرادی که از زیر آوار ساختمان‌های فروریخته درخواست کمک می‌کردند، شنیده می‌شد.
پیش از این مقامات ونزوئلا گفته بودند که حدود ۳۰ پس‌لرزه هم پس از دو زلزله شدید روز چهارشنبه ثبت شده است.
در پی وقوع این زلزله سازمان زمین‌شناسی آمریکا هشدار داده بود که تعداد قربانیان این حادثه ممکن است به هزاران نفر برسد.
@
VahidHeadline
هم‌زمانی این زلزله با بازی برزیل و اسکاتلند در جام جهانی خیلی‌ها رو یاد فاجعه ۰۰:۳۰ بامداد پنج‌شنبه ۳۱ خرداد ۶۹ در استان گیلان انداخت که همزمان با بازی همون دو تیم در جام‌جهانی ۹۰ ایتالیا اتفاق افتاده بود.
زمین‌‌لرزه‌ای که حدود ۴۰ هزار نفر رو کشت.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 305K · <a href="https://t.me/VahidOnline/76692" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76691">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TxsWKF-OY38vmxdDZn7ZADcHBu_k_K-r_cHsgrep6DyblZEEuPka26fkcHI6fmax5vBVxt35zJaj_qlecPnAdBc1ciU1GnOLgylzBle0UNtGTrTgkPdW_JLE92UJDEVaSaBJ6GxgnhvpMqoJCQ9-lYnzrEJ0UEoXVS_ZX6EE4imxkf-M0Ixt-06s14hnltD4ofWKYiAT916o09rAlZl2Oe7B4d030iRC4dYGKEcQ-VCmNgfPGFIHc_zVQx_m_hCatx5MUuf9-9X9hXZ3UeHf3FYtkxVWK3YLhuEkUnh3d7sHNAmLjPUFwPBFcLviD32L-HZK4IXGflAmtlEOvMKMxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صداوسیمای جمهوری اسلامی گزارش داد که روز جمعه، پنجم تیرماه، سپاه پاسداران سه نفت‌کش خارجی را که قصد داشتند از مسیری «غیرمجاز» از تنگه هرمز عبور کنند، بازگرداند. این نفت‌کش‌ها تلاش داشتند از «کریدور جنوبی» استفاده کنند؛ مسیری که اخیرا عمان و سازمان بین‌المللی دریانوردی (IMO) به عنوان یکی از دو مسیر موقت برای تردد در این آبراه پیشنهاد داده‌اند.
جمهوری اسلامی با رد این توافق، مسیر پیشنهادی جدید را «غیرقانونی، غیرقابل‌قبول و بسیار خطرناک» خوانده و تاکید کرده است که تنها مسیر قانونی برای عبور از تنگه هرمز، همان مسیری است که پیش‌تر توسط تهران تعیین شده و از نزدیکی سواحل ایران می‌گذرد.
داده‌های ردیابی «مارین‌ترافیک» نیز نشان می‌دهد که سه نفت‌کش پس از حرکت در مسیر جنوبی تغییر جهت داده و بازگشته‌اند و سه کشتی دیگر نیز مسیر خود را به سمت شمال و آب‌های تحت نظارت ایران تغییر داده‌اند.
این در حالی است که به گزارش «لویدز لیست»، بسیاری از کشتی‌ها در هفته جاری از مسیر پیشنهادی عمان استفاده می‌کردند. این اقدامات همزمان با تنش‌های اخیر پیرامون مدیریت این آبراه راهبردی صورت می‌گیرد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 252K · <a href="https://t.me/VahidOnline/76691" target="_blank">📅 19:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76690">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Cy-GZw6grHhjeiOKVzgC35UbCUjEtd1PZ_jq7xG3buVuppWAtv2dkFmEjxGtGFc0KssanzjGTFWF-rFCrLBxqdnpRVFNdXUKERHmN77g5tLAQUUHVwsXBxwYuBIz97mGGG0ODAMd5m7-i9MjSQ5eP24Wi-yw8ehog46s-pP8ZaSgSEsLd-BhuX2a87xwaV6FWIEKrsXeHSu-asz3QeFlZH2TIcr_Z_y_zLhtATSir17PexCnIRA81qUkQcrmR2v7oHq2ROc3R4UGKbqGckHUskBQ6UbUwBS_o8w1zTaASwj5MAzGzx4bsJ7-QUZht4itIFbpKHYha5_uNl3GHaQ35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
جمهوری اسلامی ایران دست‌کم چهار پهپاد حمله یک‌طرفه را به سوی کشتی‌هایی که در حال عبور از تنگه هرمز بودند شلیک کرد.
یکی از این پهپادها به‌طور مستقیم به عرشه بالایی یک کشتی بزرگ و بسیار گران‌قیمت حمل بار برخورد کرد. خسارت وارد شد، اما کشتی توانست به مسیر خود ادامه دهد.
ما سه پهپاد دیگر را سرنگون کردیم.
روشن است که این نقض احمقانه توافق آتش‌بس ماست.
رئیس‌جمهور  دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 237K · <a href="https://t.me/VahidOnline/76690" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76689">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB1WB4sB8mOgquaK7bA03TvU9KsT510aCgLT_8Jm4S_IVFX5OFyDY05bnrkH9un5m6CLDunISGWmzC-5wUuJRKVtIQ6pQOn2mD4tN25ml_q1o2wLW6BenFJkPO64obGuzb3nQpbaq8aNRrGGy6uKg_sdlfVAd_vBxzl331yg3_kFgq-wmoqTyYSONNkVsYFqe3YeLGJ9v-wJ7JC2OsN3T8S2m0SbxreuUvWTGh2WZUKFHZmcm8MXbixvbtwRPnrAoY_hiTQ8-_z1qYpSMIVcLsBGKzg1qUZABmhpWXFPriZcMQP7j2Xy9hxDIgTJN4cyzEpg0H3t2dL92YdaMYPt-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرس تی‌وی، شبکه انگلیسی‌زبان صداوسیمای جمهوری اسلامی، روز جمعه خبر داد که میان ایران و ایالات متحده یک «کانال ارتباطی» در تنگه هرمز ایجاد شده تا از وقوع حوادثی که می‌تواند به تشدید تنش‌های نظامی منجر شود، جلوگیری کند.
این گزارش یک روز پس از آن است که جی‌دی ونس، معاون رئیس‌جمهور آمریکا، گفت واشینگتن و تهران قرار است این کانال ارتباطی را راه‌اندازی کنند و این اقدام را «دستاوردی مهم» خواند.
او در گفت‌وگو با وب‌سایت «آنهرد» گفت که ایران موافقت کرده تا یکی از نیروهای سپاه پاسداران را به دوحه، پایتخت قطر، بفرستد تا به گفته او «در کنار یکی از نمایندگان فرماندهی مرکزی ارتش آمریکا، سنتکام، مستقر شود» و از این طریق بخش زیادی از اختلافات حل و فصل شود..
شبکه پرس‌تی‌وی به نقل از یک منبع آگاه گفته است: «بر اساس بیانیه نهایی منتشرشده از سوی دو میانجی پس از مذاکرات هفته گذشته در زوریخ، این کانال ارتباطی با هدف جلوگیری از بروز حوادث در این آبراه راهبردی که ممکن است به درگیری نظامی منجر شود، و نیز برای اجرای مفاد ماده پنجم تفاهم‌نامه اسلام‌آباد ایجاد شده است.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76689" target="_blank">📅 19:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76687">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/C62nXzqWgDkUaFHQIEkUTYTgZ-u1Xe0Kp6VEr3rHFR77l8IknPbe_ozhSPPv6jQH-NQiv7xmj12sOHcT9aUvfEtl-Fqx_wVDRe3QpTRlH3dNY7n8ScBom3hh21ThlM2cpDw5Pg-LXP2TslRGsVO8NTc5ukTEOZRADy-6Hf4URLrtgvbaiwxoXl5ss1zzc_86hJ3PsR_FUiUFAIdQFURAaP5pa0ehNrZvVYz-SgC_T33cAWFY15-qFlgtvNvMbmk_AdoId7k_9pYljJmyDMufJBZVfklAzvHqG5W_btK2oUQJ1zzFKukusSrwJYkYxvYd5Oocq5veWK-7fDr7rlfa-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uVPjui27mxFjr2LBlO3ZgIheOxWmNG3mAfxmR4VGhW_175vXfNdER0L4Xw9GbH5k0VPqC4Mi6i9oOLBh-kgg9sBxLjB87nqSKAPC3fvQB-onHpaVYRy4P8wmqJOM9esEECvjU4nZkVdpFv-TnwyPP0d0ACYxuYiEgwRReBFxE0uBO_7cedShdQ4kIeAYcncGo3HZqoXPLq_FHfmTf1tZyHjeqqMyXCvkbnFMu8Thz9tH9Km1xuRIbElrtanQ6Lx1_lrYsdYSL6IssR233Z3OfeP0xBka3kMV4vMkS8jXXNXDQQWsy6_fWpjOnRWGvBg9FjxJ8UmiKo3M_27Z-ep5NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کاظم غریب‌آبادی، معاون وزیر امور خارجه جمهوری اسلامی، می‌گوید عبور ایمن کشتی‌ها از تنگه هرمز بدون هماهنگی با حکومت ایران «قابل تضمین نیست» و هشدار داد که در صورت انجام نشدن این هماهنگی، ممکن است مسیرهای تعیین‌شده برای تردد کشتی‌ها به حالت تعلیق درآید.
این اظهارات یک روز پس از آن بیان می‌شود که سپاه پاسداران اعلام کرد عبور امن کشتی‌ها از تنگه هرمز تنها از مسیرهای مورد تأیید ایران امکان‌پذیر است و هر مسیر دیگری که بدون هماهنگی با تهران اعلام شود، از نظر جمهوری اسلامی «قابل قبول نیست» و یک «ریسک امنیتی» به شمار می‌آید.
عمان روز چهارشنبه اعلام کرده بود که با هماهنگی سازمان بین‌المللی دریانوردی، یک مسیر موقت برای تردد کشتی‌ها در تنگه هرمز تعیین شده و از کشتی‌ها خواسته بود تا اطلاع ثانوی از این مسیر استفاده کنند.
@
VahidHeadline
قرارگاه مرکزی خاتم‌الانبیاء، ستاد فرماندهی جنگ جمهوری اسلامی، روز جمعه پنجم تیرماه با انتشار بیانیه‌ای درباره پرواز هواپیماهای اسرائیلی در آسمان کشورهای همسایه ایران هشدار داد.
دربیانیه قرارگاه خاتم آمده است: «حضور و تحرک هواپیماهای نظامی اسرائیل در آسمان برخی کشورهای همسایه در مسیر ایران را اقدامی خطرناک و تهدیدی علیه جمهوری اسلامی می‌دانیم.»
قرارگاه خانم الانبیاء در این بیانیه با هشدار به دولت ایالات متحده نوشته است: «اگر آمریکا نتواند اسرائیل را مهار و کنترل کند، جمهوری اسلامی هیچ تهدیدی علیه خود را تحمل نخواهد کرد و پاسخ به این اقدامات را حق خود می‌داند.»
این بیانیه در حالی منتشر شده که طی روزهای اخیر تنش‌ میان جمهوری اسلامی ایران و اسرائیل بار دیگر به‌ویژه بر سر ادامه «اقدامات نظامی اسرائیل» افزایش یافته است و تهران اسرائیل را به نقض مکرر مفاد تفاهم‌نامه پایان جنگ متهم می‌کند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 224K · <a href="https://t.me/VahidOnline/76687" target="_blank">📅 19:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76682">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ksSeSgl0eDp-v8qGKvofuDM1C8LRphWrr0ucspuuaibO8dUbCGx37GFknuMzOK6sPS93rdX1ZHswe2WtQCNHcMuzrt1pxpzZtvfgYjSFonueIgaLGul19LclQ1bn0VMF3_KkzOiTgpw7lLhIebh9LZ2x8m89KuWztOsSEA1ZczwLL82MMNGZPtjJewPRWzYtzIR4oWMEeO5DJcsqObaolo6Seu12Vj62Mc7ihVZGwEfnaNc0t4g8PXh6WxInSsHj1OXednk_j4Zs8Y7yKbSFLxgEX1K44iqsbVuiS1AcCCpArbKdkr8P21qAFShwRfFe9gWL39mnSF1KEAD6dh1hoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qhxjLvu-bapDXgomFmILkL_KzbnFGJ0hacrvJBCIXc2ddHHMNa8ZRViD4jwip49cJm4Z5KR3Wxblh08zUUrMPhJZfeRXBkaxN-eBuf-35jeEiypGj1T3gF-nie4S9pEbAGZbcYur6sbHSMRqKBv8LYD1UU_05KcLda7WP2H8dfbEFeTYHOMHHZ7GllstKdehQLjf-E1V8jb8SKyg4V_sbdrIUh8Job9xVEa-wcDmrYGsRwlq9soAM7BCbUdMSVIKBYZEC6KwXzDMDRWDu4TB8KOSa1DdV2FCALEUouu3LEfiqz1CNk0b9Pv-Pttp_mlOpJIz0QItuzidqNhDVGoU3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pbQyWd9vbzSIw8MwKVU1wBs1UWwdkSMRp9Q-B15hN3CqCnNY2YQz0-01QF2Oheo3mdEhzFJEcKN-C1jqUz-HgW2OGHa9l9qY66H6WujaNYNQjfRHL20PXFHJpmbRkyIKaM-cvx2-huaUXpEtMBhoBCLkRoWKw1MIpIlsS5gWQCLhshW-BF3k2dB2xRPejWIA5V_j_cD6uiqxtulppmqW02BxrQHjKlJcnAK_98xndAK7mm-a1_AasQiNlTkaE17x5F-A41Pygmu_eeKA5nBRguDAhNmdUojdi0UP_M2u60j5_zzGbofEi46Y1tuuOPMUX-wZeodnu5CB8eT3T10DDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/kazeYcgq3r7xZO_P7hPzytty4Pl4Svlz8w_7Rdz1sJ18JSN3Yc8nw_4Hd-BtrGnyIyVh2hxILF2a0zTBAKvo8nHRdnpuAVMueywLeXjFn59wQt689X3lO92MReElZ7ZjaSBX3u1p9LQ0km55IWq5-b-Z34KByTV3L-uionu0PYZLbbZ5xCixI_BE1zj9d-9WvLJ5oYhMbMOANjofyx2xmZOyNAsgZMGGPsfgMvOXELmjBqdg-LIlHBkbEImG1hIVDGPWo3etnwg0g-8eaatJ45g-nuP_883TabcEK54T5TEQsqrecRwWgneks_bc4WqzXRRHSKEOoFNcPR3_1thYRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WOneGelrHNEEdXjZraaVsitGtyXCRt82V3nsWJW1FPmuVOu9ZwOW2nz-0LiYs7QKPabgFsrDZZog1HoakZO9fL5eWDyE81RYVMbIMI806LmfQug-RxNYQx5PLAnkOGJeEOLRhZyv-JrX0ogqeUHwuUUDKCfcqwUe0gIInWScwTtRniUH04Yhc3AlZe9nb6pElyqP7PQskLkUCjvXYnUEtqnMa0OmPryJhQwxP2aBBUDaodKSkG6xNYI30M2gHMeGQvQ8Yl3LO5trCNjwXEvXf7AEOkXc3UoUmHZuX-_InKm785tO41pOdPbMZWKMe51LNWNC9rWkDyo2nuGYLWsALQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نعیم قاسم، رهبر حزب‌الله لبنان،در سخنرانی تلویزیونی خود در مراسم عاشورا گفت: «اسرائیل هیچ گزینه‌ای جز عقب‌نشینی کامل از هر وجب از خاک لبنان ما ندارد... اسرائیل باید بدون هیچ شرطی خارج شود.»
در حالی که مقام‌های لبنانی و اسرائیلی در واشنگتن مذاکرات مستقیم برگزار می‌کنند، آقای قاسم گفت گروه او «هیچ عادی‌سازی روابط، هیچ پایان دادن به وضعیت خصومت، هیچ دستاوردی برای اسرائیل و هیچ حضور جزئی در خاک لبنان را نمی‌پذیرد... اسرائیل باید با خواری و شکست خارج شود و این اتفاق خواهد افتاد.»
حزب‌الله لبنان مورد حمایت جمهوری اسلامی ایران است و تهران می گوید در تفاهم اخیر با آمریکا و مذاکرات جاری با این کشور، منافع این گروه را در نظر می‌گیرد.
به مناسبت عاشورا شیعیان لبنان تجمعی در شهر بیروت برگزار کردند و عکس‌هایی از رهبران جمهوری اسلامی ایران هم در این مراسم حمل شد.
@
VahidHeadline
یسرائیل کاتز، وزیر دفاع اسرائیل، در پیامی در شبکه اجتماعی ایکس، در واکنش به تهدیدهای اسماعیل قاآنی، فرمانده نیروی قدس سپاه پاسداران، نوشت: «اگر جمهوری اسلامی به اسرائیل حمله کند، بزرگ‌ترین اشتباه خود را مرتکب خواهد شد.»
کاتز خطاب به قاآنی گفت: «به نظر می‌رسد نقش یک جاسوس و خائن خیلی بیشتر از این ژست‌های مضحک تهدید به او می‌آید.»
کاتز افزود: «نه هرمز به آن‌ها کمک خواهد کرد و نه حمله به غیرنظامیان. هیچ‌چیز ما را متوقف نخواهد کرد. نیروهای ما آماده‌اند تا کار را به پایان برسانند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 206K · <a href="https://t.me/VahidOnline/76682" target="_blank">📅 19:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76680">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/tgVjCffv2D2j5vmBGTR4mlyUfkgUkUxN9myicDv_P_rkUU31gycs2SxX-zq9QdnGn8yyif91LaX5cRHY_w_o_wtj95xFkWJOFhxOCbqcoP58SeDjXLy2b_7nzYv8H5dr1n1G0cEZYZ_BIW3hLQhEACLdMLX1zcXh5KYOwJ9g2Wm-3KcNOFW-r3FYV8NNBMRbBggKTsWfN3Riip6cc3cNxp9FTi9BKnAGd5vGX2r0J8o00VPBe21sl9XfNRrQaNPYpgPp_DRGrZVRYAGV5pvF68t-EuRNlHD4StVxq1DN1dZLbol05Ssq8B2Apfcr45KPpkypMda2Ikr5pzovLBAnfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sV39bl3mLW6wpPgGRIpFBmY2D38ox0JdNgGjV6RpQnZp1qtVPaYmBtinUMKbNKp41iJP17zAY6ugobocI35M_wMKrGT9R9czwWJnR1YSVVIGx9LMSS92BPG0CUiKzZaRvpY53oD7ocn0hlNslGxVy5hHeJoHe8SbSZjun58ezuEPVB7hhiHU8eFdK-UkR2j77vY2Lw2Tj4gpVhw8eeIwLWc_XO1iSKumha6bCNAGRbIUdq8xmFDekOeuDQgf6XXbIcWoDbvhWbP0ZhxBvwvqnfblSEPBYzCJwiSem9gGaEgfeyUnu2mrFgoB7hZdZrud5qXfM4OyS4YqDK9iUoeueA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">در نشست وزیران خارجه شورای همکاری خلیج فارس با حضور مارکو روبیو، وزیر خارجه آمریکا، در بحرین، کشورهای عربی حاشیه خلیج فارس بار دیگر بر لزوم مهار تهدیدهای منتسب به جمهوری اسلامی تأکید کردند. در بیانیه پایانی این نشست آمده است که تحقق صلح و ثبات پایدار در منطقه بدون رسیدگی به موضوع برنامه موشک‌های بالستیک، پهپادها و حمایت تهران از گروه‌های نیابتی ممکن نیست.
@
VahidHeadline
وزارت خارجهٔ جمهوری اسلامی ایران با انتقاد از بیانیهٔ اخیر کشورهای عضو شورای همکاری خلیج فارس، آن را «مداخله‌جویانه، غیرمسئولانه و تحریک‌آمیز» خواند و نسبت به آن‌چه «ادامهٔ رفتارهای ستیزه‌جویانه و مداخله‌جویانه در منطقه» نامید، هشدار داد.
در بیانیه‌ وزارت خارجه که روز جمعه پنجم تیرماه منتشر شد، به کشورهای حاشیهٔ خلیج فارس توصیه شده که از همراهی با آمریکا در «تهدیدانگاری» برنامهٔ هسته‌ای ایران خودداری کنند.
این بیانیه همچنین بار دیگر مواضع پیشین مسئولان جمهوری اسلامی دربارهٔ قرار گرفتن تنگه هرمز «در محدودهٔ آب‌های سرزمینی» ایران و عمان را تکرار کرده و می‌گوید همین موضوع «مبنای عمل در رابطه با مدیریت کشتیرانی در این تنگه خواهد بود».
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 191K · <a href="https://t.me/VahidOnline/76680" target="_blank">📅 19:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76679">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AO5u6l3cZtMQmqf7IFvJ44aK0ZIH56AcHUokT6wIAiXQVoyK8t-XJuwQspXGvQvzk4RXbu1PL127YcDeactQpWCQ3oc826ZAu3Ba8ULCt8tTK-8290E1ZwyInmrZNEPqYtQyvCaYFy4x0D43AySFoZaoJx9iudL_YwZoMpzkZaW28WMv543T4zMM9ZHRXnIpdbvPXVgZqymECK4QKg0Jpivvrx5nhTpLc-QPgwZuqlqEdzzdB5jAzBVM1iPGovNdWFNG0f3hvzQ5sH0aI27rzHo7WV4g0aY9T96XIRNd1WCsbvBo6PNIeyWVeZKKPNONOwuqH7YGx6o6FiurfGPisw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‌رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، گفته است که پس از جنگ خاورمیانه، برای اطمینان از اینکه ایران به سلاح هسته‌ای دست پیدا نکند، به یک نظام راستی‌آزمایی «بسیار قوی» نیاز است.
آقای گروسی در جمع خبرنگاران در ژاپن گفت: «فکر می‌کنم هدف این تفاهم اخیر [بین میان آمریکا و ایران] این است که اطمینان حاصل شود ایران به سمت توسعه سلاح هسته‌ای نخواهد رفت. دولت ایران هم به‌صراحت اعلام کرده که چنین قصدی ندارد.»
مدیرکل آژانس گفت «اما البته صرفِ اعلام نیت کافی نیست. ما باید هرچه زودتر که از نظر عملی امکان‌پذیر باشد، یک نظام راستی‌آزمایی بسیار قوی برقرار کنیم.»
ایران گفته است که توافق درباره نحوه بازرسی‌ها و حضور مجدد بازرسان آژانس در تاسیساتی که مورد حمله نظامی قرار گرفتند بخشی از مذاکرات جاری و توافق احتمالی نهایی با آمریکا خواهد بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 189K · <a href="https://t.me/VahidOnline/76679" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76678">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1t2JdfvuEPR1xlz37XMRqHiZV7AWLcZ9gorqizH_hf7G05s-GSzDwMO5KFRAJgslvcogVp7741tRSb8A1SFlJNfqx3fxgn6wRN4KOhmeG_R1_LUgigxdsqJuACzh5klJn0lu4f0T7PpjeEMZZKul8-AYO2-DCXgnIPtl7_lA59y56ZI-zMXgjJ-koQzavl8DdSENyYM0Et_oQXCUQXQIfOD515UIeaZ6KeSsJtE7v56o_ujbE9Z3XdTOA9zjdwFq_r2zPeCMgdNkwBEJ2xrx0oTzDEOetd_d6gA-5XAZncgVt75XBeTZBIE-IWPBGFNheQBjGrlhhGkOwnGs4A-Qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نخست‌وزیر کانادا روز پنج‌شنبه گفت کشورش باید سفارتخانه‌های خود در ایران و ونزوئلا را بازگشایی کند.
به گفته مارک کارنی، فقدان حضور دیپلماتیک، توانایی اتاوا را برای کمک به کانادایی‌های خارج از کشور و واکنش به بحران‌های بشردوستانه، به‌رغم اختلافات عمیق با حکومت‌های ایران و ونزوئلا، را مختل می‌کند.
او در توضیح بیشتر گفت: «تعامل به معنای تأیید نیست. داشتن سفارت، داشتن خدمات کنسولی در یک کشور، به این معنی نیست که ما سیاست‌های آن کشور را تأیید می‌کنیم.»
او در عین حال گفت هنوز در این زمینه تصمیمی گرفته نشده، اما تأکید کرد که این شرایط «باید تغییر کند و حرکت به سمت این تصمیم، کاری است که باید انجام دهیم.»
روابط دیپلماتیک ایران و کانادا از سال ۲۰۱۲ میلادی قطع شده و سفارتخانه‌های دو کشور تعطیل هستند. استیون هارپر، نخست وزیر وقت کانادا در آن زمان جمهوری اسلامی را «مهم‌ترین تهدید برای صلح جهانی» خوانده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 219K · <a href="https://t.me/VahidOnline/76678" target="_blank">📅 19:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76677">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=E91Fhe-R4VMmOloeaqqpLk1VLE0fa4J_QiEDBoKMq5LYbeIvJSjqA6T9P7BMuTENsspm8mEqnuHiaYeQvZKASPmex9uKB4GBKP523dnM12taeucJwD0w9np8FR5_8D9m5VyejPZvJwgy4mzAJwVUGGRuM9Ldg0og7DAN2xH-kdDk0qOvgSp9x_FGBEPOQd_VNqIzKRXRHBuTKW5tG8E-bltdX5X--E5Oim9TmiMu9JNhBC3Nq2aSy0S0r35MxtZlejkaX-iXAm9ZbrqsaBnStmskRYxjd2hMwDLqAmpps-LuvHaAAAk32Hb2MyTGmenB3eVhin40PK9SVSn9oIa-GQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9cb833fa3e.mp4?token=E91Fhe-R4VMmOloeaqqpLk1VLE0fa4J_QiEDBoKMq5LYbeIvJSjqA6T9P7BMuTENsspm8mEqnuHiaYeQvZKASPmex9uKB4GBKP523dnM12taeucJwD0w9np8FR5_8D9m5VyejPZvJwgy4mzAJwVUGGRuM9Ldg0og7DAN2xH-kdDk0qOvgSp9x_FGBEPOQd_VNqIzKRXRHBuTKW5tG8E-bltdX5X--E5Oim9TmiMu9JNhBC3Nq2aSy0S0r35MxtZlejkaX-iXAm9ZbrqsaBnStmskRYxjd2hMwDLqAmpps-LuvHaAAAk32Hb2MyTGmenB3eVhin40PK9SVSn9oIa-GQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودداری ساکنان آبدانان به عنوان یکی از محروم‌ترین مناطق ایران، از بردن این کیسه‌ها به منازل نمادِ «شرافت» و «شورش گرسنگانِ آزادی و نه تهی‌دستان» نام برده شده است.</div>
<div class="tg-footer">👁️ 234K · <a href="https://t.me/VahidOnline/76677" target="_blank">📅 18:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76673">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/SqKdio_pdjkj_AoR17OZ4TLPLacXvWZcpltLrz0-KYWFSRizlKfCBMhQTyvUagDjUIgrtGlh4iuMZljetPRtnSleIN-I7G3PSJBM4D8VfuNA00Da8tYYI2rf_zkQ0OCgwqh_6D5DrTCI7UEFaBUWT6HhEl4It8IRJuoqCvv0mX9JG-DY2pIXCM-5xfAPTbDrS78tLcYS03_hd-Ys1e8mUZQIo0l9ePeT2IwdLlv_KUjMb5yuQYSrGCVuJGel5RE4IAaqnStB2W3Uw2kSatR9Oz1GDP8peP19N-TI_0opeg_ERF9j3RJD36PkOE2xHbWnBlaXB1qMdO44iIeOZCH6DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/a2gfp1sxnHGfUSZ4wh7s3l3xWRKA4z-HP12n2acjC3ncWh1PlEdCnWgavAWx0JHC4POkxjdC16PmjpkVrdhWS8KqNi_JjKSG_1JLnakr5J92FxaxxI-EB781kqYEveA9MGuljQsW1PAQXetnAUi-x0U7L1jkOXVUVzGvwrllkuqs5HG-LW1JQahEMD7IPmjQJA5Pe0EPY8AdGOhT0HI8K2WbJnTn6yAwwb-pGt2Y84J4RLmQsD9lxL-IIc9m4WETwu08pueEvfOsmeVKkLgj47wKlBJyQ-rPfHny1Y20xuAAZD7KjWYjNCfjWF6Y-bAA7f2THaPEHyQWFT5vu6Zo8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/aVMCUizSdnJ8Mqh3sd1jPghhww9uAZ4LiyaiAWA0fD2MAKL8IDZqOyA8uyOll82f4okfUHj_wGm40v6QaWcEgAmhhiOK7PkRn9tVNW6O0jQrBf5Van8IRaZ2ooK85YsGY3Akr3w-Pa9eE1JR2MopXfO1sYH3_E-4Eud38sJmRtHUgdcsEGgxvnZ2RFxEHvcRQSrLgjoZ3hwVuSrefeg8xr4b2M9JgaQE6_lYidHtcfwbW1RrMSZJUzMe2oCQCrDnmSKoW7LAbWgA35hPnxv_zmI_PsM4U9TZXncO7WjqT__UIbwMUIMrSR9LdGDaluUEuECwwO7fvgdmZpx2LoTIkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WEpYuhRh-96hxY95PcIW0Uf_LtPRvQisdkKLOSkNqSVyoXDsu_-yrsQvTy57CaUTHl20pNEZQ18Jo2397RuQ3nSbUeFEVcD3_MJdgTMEP-V-ciH4WozxoXT7oFyHGFxnQUAqakYom3G_0lFg1m5eHCx4HuelV7COsTVQENNre9XSF2LUPXuQeoSqZ6R5LUwbLQrHijEKbnfRtfp8PBwWQXb6E_h9Vykb6UppZA9oJiNMKpo4jtgvMUQurZ5TBcU89wVnuOwcmoDeI6rNr5ZgI5lWVKf7dhBtq8yCRssdKPCmEu94zcUA0sRN3y25pS_RLGVy-Ltd6vtkmwpqhAJM2Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی:
خود امارات الان مسیج زد که اشتباه سیستمی بوده
هشدار دبی اشتباه بوده
دبی ساعت ۵:۱۸ به مدت ۲ دقیقه آژیر زدن ولی گویا تست بوده
اره فکنم دستشون خورده
احتمالا تست پدافند بوده
الرت دبی اشتباه بوده الان مسیج اومد برامون
وحید جان دبی گفت آژیر قبلی رو نادیده بگیرید
🤣
دستشون اشتباه خورده بود
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76673" target="_blank">📅 17:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76671">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/sAdtLzOJbA35tcYh0U1_45jS2m5EHig48tJ6WJt_Y8SnlEcyLNrQ_5ze0ipAUjLaJGOuJeOVA1n9sFuJ9VHII8of4KiaflQl03yc2heq3qrr0MYGyQlAwgw1dYTEmBU9ThAidbcbFaZqCzqWtbsI01DxFc_sWDi0poOIdpCxYur0VB4vIjn2v5a7U1MiP7dQd9gmUBsFKZ8VGrHty6RYOofYLvxbH0kYU6eGx0zJWkYHRWzVs_qp1_jfh-wLl-aW47d_2GBElg01TMPwuqn19yDzDwGA5SmIobmUEm_EZ0EiSshp3MWgC4p4_3cIz9G4W-wRPJhkd_t-uoPZi7xRSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/eGmHRFDlKLjJZbgfND5_KbHSH8ZarNIHFFN1krjyPWvaMFlqhfD2gdIvDwEahJrBlYjKIlcM8a6NyOnDsQgbaQHyuJFawzxy63S7_iM_8w3nYa9TonG79O-5G76LdbPkC0vL1HS2fH7X6uIhVLabkiHSMtLpxRNyXg48JMaNMJ0C-ULWjF0_L7IlL2C_WC_1-ORrNHAutpDnZ14xfJQtEysNyUhPrqMhIhPn1Pg88iegl19PFsX687APAAGconzxDY5avMJZDtReHe36jI2g_c914uEgG7gHlSF0zohfcWssrDFzUkdgqumLxwTwMYVUn_GDkYa8lOss5BR8mDGgvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">پیام‌های دریافتی الان:
سلام وحید جان
الان دبی برای ما آلارم موشک اومد
سلام اقا وحید
همین الان باز اژیر زدن
نمیدونم کجای دبی رو زدند
وحید جان همبن الان دبی آلرت موشک دادن
ما امارات هستیم
هشدار حمله موشکی بهمون دادن
الان امارات دبی دوباره صدا آژیر اومد
🫠
البته خیلی کوتاه بود، و سریع گفتن اکیه
وحید جان همین الان توی دبی برای همه آلارم حمله موشکی اومد
منطقه جمیرا ۲، کایت بیچ ۲ بار صدای انفجار شدید از آسمون اومد
احتمالا رهگیری بوده
📡
@VahidOnline
آپدیت در پست بعدی</div>
<div class="tg-footer">👁️ 299K · <a href="https://t.me/VahidOnline/76671" target="_blank">📅 16:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76670">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=fs7hvNlPLAjzwbJLNPZ25Vu90sDY9WDtDMMMOqHbp_Be1lG_3cqcLClh07Ln00cEJHIV28FC285EH_waJfyV4yxT6TULDnClfdV7SIbHHavTcFepHrT8fjmiF-SMk8i1KN9bqWFai-WJVcKkH5faDDy_27NFyUuRxASB-p0RSrdnbE8csXQHu4b6TqZkOUGkFmlbCBKsjqf5HamWZnFZOcaFTsrnd_pOWDrW5aNEC_Eeh57i_T5sBrJp2SBs8u0lmI2A8WGB685Esb5j2PvExJ2EQx78r2w3FU8J9Q3ynLd2uguU0LNl-fexwGRE8hVNTinmG_lg2QJDVmYkY0DuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d5745e7068.mp4?token=fs7hvNlPLAjzwbJLNPZ25Vu90sDY9WDtDMMMOqHbp_Be1lG_3cqcLClh07Ln00cEJHIV28FC285EH_waJfyV4yxT6TULDnClfdV7SIbHHavTcFepHrT8fjmiF-SMk8i1KN9bqWFai-WJVcKkH5faDDy_27NFyUuRxASB-p0RSrdnbE8csXQHu4b6TqZkOUGkFmlbCBKsjqf5HamWZnFZOcaFTsrnd_pOWDrW5aNEC_Eeh57i_T5sBrJp2SBs8u0lmI2A8WGB685Esb5j2PvExJ2EQx78r2w3FU8J9Q3ynLd2uguU0LNl-fexwGRE8hVNTinmG_lg2QJDVmYkY0DuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک روز پیش از دیدار تیم‌های فوتبال ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶، فیفا روز پنجشنبه چهارم تیرماه اعلام کرد تماشاگران می‌توانند پرچم‌های رنگین‌کمان را به ورزشگاه محل برگزاری این مسابقه در سیاتل وارد کنند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی در دیدار ایران و مصر جلوگیری کند. این درخواست پس از آن مطرح شد که کمیته محلی برگزاری جام جهانی در سیاتل این مسابقه را «بازی افتخار» (Pride Match) نام‌گذاری کرد چون هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود.
ایران و مصر پس از قرعه‌کشی با این عنوان مخالفت کرده بودند. همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای اعلام کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه‌ها را دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76670" target="_blank">📅 06:19 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76669">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/qVmA-gNzSTIGrCWnEKa0nN81EI-ysoWCNL0MPyHmFa2Oq_7Qt4EY12Po_iQkG8f0utJJzYnCVjjBMegp-g4cXqNPxxVkJ7fV0BV7CAlCdBpe6WCMxxn6FKufoWvNOjmfT6eoOrp22fWWKXfXOlm8ygygHtDcCP_r8-r5PrT5n5A30N2JoOUYy_ISiWdoDWm8n_31Gu2s6KgwagEQwNnJwRBxaYRcF80d3wOklXKSqKWK2-JnFjVOduyDiQK5f-QOb84rehT-Zh3_6GmaRk5fOBCYFO5eYeYE3auwuQl5DmLClMZTZsyLtqFdZQkuv0VybnFgqkI_aqdtNCLZAelFWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سی‌ان‌ان: یک مقام آمریکایی به CNN گفت یک کشتی باری در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛
اتفاقی که باعث شد سازمان بین‌المللی دریانوردی عملیات تخلیه خود را در تنگه و اطراف آن موقتاً متوقف کند.
ترجمه ماشین: یک مقام آمریکایی به CNN گفت یک کشتی باری روز پنج‌شنبه در تنگه هرمز هدف حمله پهپادی ایران قرار گرفت؛ حمله‌ای که باعث توقف عملیات تخلیه هزاران دریانورد از کشتی‌هایی شد که از زمان آغاز جنگ در خلیج فارس گیر افتاده‌اند.
این مقام آمریکایی جزئیات بیشتری درباره این حمله ارائه نکرد. ایران مسئولیت آن را بر عهده نگرفته است.
سازمان عملیات تجارت دریایی بریتانیا روز پنج‌شنبه اعلام کرد که یک کشتی باری از سمت راست خود با یک پرتابه ناشناس مورد اصابت قرار گرفته و پل فرماندهی آن آسیب دیده است. بر اساس این اطلاعیه، ناخدای کشتی گزارش داده که هیچ تلفات جانی و هیچ پیامد زیست‌محیطی در پی نداشته است. مقام‌ها در حال بررسی هستند و به کشتی‌ها توصیه شده با احتیاط عبور کنند و هرگونه فعالیت مشکوک را گزارش دهند.
‏CNN برای دریافت نظر با کاخ سفید تماس گرفته است.
توقف عملیات تخلیه چند روز پس از آن صورت می‌گیرد که سازمان بین‌المللی دریانوردی (IMO) اعلام کرد توافقی میان ایالات متحده و ایران راه را برای تخلیه بیش از ۱۱ هزار دریانورد گرفتار در منطقه خلیج فارس باز کرده است.
آرسنیو دومینگز، دبیرکل IMO، در بیانیه‌ای گفت: «پس از آغاز طرح تخلیه IMO، که طی آن چندین کشتی تاکنون با موفقیت تخلیه شده‌اند، تصمیم گرفته‌ام اجرای آن را موقتاً متوقف کنم تا دوباره اطمینان حاصل شود که تضمین‌های ایمنی لازم همچنان برای کشتی‌های موجود در فهرست تخلیه ما و همه کشتی‌های حاضر در منطقه برقرار است.»
او گفت از حمله‌ای در روز پنج‌شنبه در دریای عمان به یک کشتی که از تنگه هرمز عبور کرده بود مطلع شده است و افزود که آن کشتی تحت چارچوب تخلیه IMO فعالیت نمی‌کرده است.
دومینگز گفت: «من همیشه تأکید کرده‌ام که ایمنی دریانوردان در اولویت مطلق است. بنابراین، برای تضمین رویکردی هماهنگ و ایمنی دریانوردی، طرح تخلیه تا زمان روشن شدن بیشتر موضوع متوقف خواهد شد.»
دومینگز یادآور شد که پنج‌شنبه «روز دریانورد» است و گفت این لحظه ضرورت اطمینان از ادامه تلاش‌ها برای تخلیه «هزاران دریانورد گرفتار در خلیج فارس» را برجسته می‌کند؛ بدون آنکه آن‌ها در معرض خطر تبدیل شدن به «قربانیان جانبی این درگیری ژئوپلیتیک» قرار بگیرند.
سازمان مدیریت راه‌های دریایی خلیج فارس ایران روز پنج‌شنبه اعلام کرد کشتی‌هایی که خارج از مسیرهای تعیین‌شده آن حرکت کنند، تضمینی برای عبور ایمن نخواهند داشت و مشمول بیمه یا مسئولیت‌های مرتبط نیز نخواهند شد. این سازمان در پستی در X افزود: «پیامدهای حرکت در مسیرهای غیرمجاز بر عهده مالک، بهره‌بردار و فرمانده کشتی خواهد بود.»
این تحول در حالی رخ داد که مارکو روبیو، وزیر خارجه آمریکا، در منطقه خلیج فارس حضور دارد تا توافق با ایران را به سه کشوری عرضه کند که احتمالاً از بزرگ‌ترین بدبینان آن خواهند بود.
هفته گذشته، ایالات متحده متن رسمی یادداشت تفاهمی را که در آخر هفته با ایران به دست آمده بود منتشر کرد.
یک مقام ارشد دولت آمریکا متن سند ۱۴ ماده‌ای را خواند؛ سندی که مفاد مربوط به بازگشایی تنگه هرمز، کاهش برخی محدودیت‌های مالی علیه ایران و انتظارات برای رسیدگی به برنامه هسته‌ای ایران در مذاکرات فنی آینده را تشریح می‌کند.
قیمت نفت آمریکا پس از جهشی که در پی تعطیلی تنگه هرمز به دلیل درگیری‌ها رخ داد، به پایین‌ترین سطح خود از آغاز جنگ ایران رسیده است.
cnn
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 330K · <a href="https://t.me/VahidOnline/76669" target="_blank">📅 03:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76667">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=UmwS9i5EYLIPol4dtJCPwHOi_56WMKrB-rU-P-1X0j-lCxh5fFzi417-pw5qO0WiSYFAFtoU1DiIFkudVH6ldHfnMVqcaXDxArdeEwxwftSmkYEaTP6Sc4LxNRtush8XWBIYjLr__151_S1JKCCHmoaIHAoNn0Pc3A6GiHP08cCoSgfB-GO9g-ECQZ_vFiOBE26hIiihXwnD663W1Wxxu1u5cn3KbHBkWJP72wIG9o4fczCUa3BW6XWPxzLZCPWKqngoBdfgIxpEnBKZhM8ztVY_4YLfGbnxHQta_k9PVwR2yfU5_peBOBpq2PmXoa59MexIhFz9HUjzo1qjzkd9hg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5fb8daec84.mp4?token=UmwS9i5EYLIPol4dtJCPwHOi_56WMKrB-rU-P-1X0j-lCxh5fFzi417-pw5qO0WiSYFAFtoU1DiIFkudVH6ldHfnMVqcaXDxArdeEwxwftSmkYEaTP6Sc4LxNRtush8XWBIYjLr__151_S1JKCCHmoaIHAoNn0Pc3A6GiHP08cCoSgfB-GO9g-ECQZ_vFiOBE26hIiihXwnD663W1Wxxu1u5cn3KbHBkWJP72wIG9o4fczCUa3BW6XWPxzLZCPWKqngoBdfgIxpEnBKZhM8ztVY_4YLfGbnxHQta_k9PVwR2yfU5_peBOBpq2PmXoa59MexIhFz9HUjzo1qjzkd9hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسرائیل کاتس، وزیر دفاع اسرائیل، در مراسم فارغ‌التحصیلی افسران رزمی در پیامی هشدارآمیز به تهران گفت: «اگر ایران به دلیل فعالیت‌های اسرائیل در لبنان یا به هر دلیل دیگری به اسرائیل حمله کند، با تمام قدرت به آن ضربه خواهیم زد؛ به‌گونه‌ای که برتری قدرت ما را به‌روشنی نشان دهد.»
همزمان، بنیامین نتانیاهو نخست‌وزیر اسرائیل، تأکید کرد، حضور نظامی اسرائیل در مناطق امنیتی جنوب لبنان، سوریه و نوار غزه ادامه خواهد یافت و زمان‌بندی مشخصی برای پایان آن در نظر گرفته نشده است.
این در حالی است که جمهوری اسلامی ایران در جریان مذاکرات اخیر  بر ضرورت جلوگیری از گسترش درگیری‌های اسرائیل در لبنان و خروج نیروهای این کشور از خاک لبنان تأکید کرده است.
همچنین برخی مقام‌های لبنانی و جریان‌های سیاسی منتقد حزب‌الله، تهران را به دخالت در امور داخلی لبنان و تأثیرگذاری بر تصمیم‌های سیاسی و امنیتی این کشور متهم می‌کنند.
@
VahidHeadline
بنیامین نتانیاهو، نخست‌وزیر اسرائیل، روزپنجشنبه چهارم تیرماه  در مراسم فارغ‌التحصیلی افسران نظامی در جنوب این کشور تأکید کرد که نیروهای اسرائیلی «تا هر زمان که لازم باشد» در منطقه امنیتی جنوب لبنان باقی خواهند ماند و قصدی برای عقب‌نشینی ندارند.
او همچنین با اشاره به فشارهای بین‌المللی، از جمله توقف ارسال مهمات در جریان جنگ، گفت اسرائیل در صورت لزوم «حتی با حداقل امکانات» به جنگ ادامه خواهد داد.
نتانیاهو در ادامه با اشاره به ایران گفت: «با توافق یا بدون توافق، تا زمانی که نخست‌وزیر هستم، ایران به سلاح هسته‌ای دست نخواهد یافت.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 335K · <a href="https://t.me/VahidOnline/76667" target="_blank">📅 22:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76666">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DTyWZtgcsuGAGDiQE0aoZf9xnYVPsivcNcEN_tKRngWnVr-BuIU8VR6K1TYSa9BgZU0HVM8TzavLPcGs8UYFoao5rGeSQKF8HhUQyQrPQABcTvTaxaJ2mKMTQVjEtxCD-HaaYOU-DyZOTljUgGmjYzGdxMx8gkGHD-PSTlgY1FzvoIes1_TCZDiYx1oLzv2kajBfzaskuJ83X8JMBeXu84Q8Vvv2vasdZgEAzS9ZSENMf8dDqDHKkv6a5lOsJREbBRSLkZdsnwfU8zZIO0QOhAELwpruQKn2MlcLbJXnv7DfIefn0NTNo-fSEduJSmhR9h2Kq36J2qiBcmv4Fpnjqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری میزان، رسانه قوه قضاییه جمهوری اسلامی خبرهای منتشر شده در برخی رسانه‌ها و شبکه‌های اجتماعی در خصوص ممنوعیت شعار دادن علیه آمریکا و آتش‌زدن پرچم این کشور پس از امضای تفاهم‌نامه را «جعلی» خواند.
میزان نوشت که ریشه این خبر در «سرویس دشمن و در راستای عملیات روانی دشمن» است و تاکید کرده که انجام چنین کاری جرم‌ نیست.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 323K · <a href="https://t.me/VahidOnline/76666" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76665">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/OUzRrJLoHP00FEkjnkWzRRlbjc5_7cj3MHLymvtTM3YDX3xlN2xnGCqxEICUXUaEh0gqiXDkUdplHq3PHcOhWWgvTYKI6gqjq2yMC3eP71h7zLpSVzi3nQuM1rsP0p33FBC_7ZcOKuzd4IS4rZPcFNEBMIE5FQe_BG_MjF-fQYvrpl315djQkMLrT1J2SnTN-R6WfprjlTHgx3sy0eOyLDTwnI5Wlck2ed73eRX2pudo8gSTHtrBXiFTdH-3cEsqonGkoyddK2RkzWzjqoONq-YwroTcw1in44-39SemQkRzwJZzxG_n6-oAWRew03knpPTusqVAxLqoNojIyK570g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جی‌دی ونس، معاون رییس‌جمهوری آمریکا، گفت یکی از مهم‌ترین دستاوردهای مذاکرات سوئیس، توافق اولیه برای ایجاد یک کانال ارتباطی مستقیم نظامی میان آمریکا و جمهوری اسلامی با هدف جلوگیری از تشدید تنش‌های آینده بوده است.
او افزود: «یکی از چیزهایی که می‌خواستیم از این مذاکرات به دست بیاوریم، ایجاد یک کانال ارتباطی در طرف ایرانی برای کاهش تنش بود.»
ونس گفت طرف ایرانی با این پیشنهاد موافقت کرده و گفته است: «بسیار خب، ما یک نفر از سپاه پاسداران را به دوحه می‌فرستیم تا کنار یک نفر از سنتکام مستقر شود و از این طریق بسیاری از اختلاف‌ها را حل‌وفصل کنیم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 298K · <a href="https://t.me/VahidOnline/76665" target="_blank">📅 18:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76664">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZX6moDTb4UWI8ftnoht44j4HRn-rlPMajyU0B91Csa3pVVuqdhViuenGYrbCNjhg_rmh_j5NkMbO3lECyQ1Bx1Bez6f7WuphJnGFmSpq43phhXHxOtcMUMqrxpp7HLhb-i1U1_uiblDuGF1BVxDrzAmnfc-rIFLvMJ7HZ9MXAQYUU78JGrxaqv4YAQ66R0wfYkrX59n66fBsik1qT1nmlh03y5VFM_zW8EAZjP1b6ydAnxs8Eg9oXJ65cC4c0_cPRJ_D9clXJEPBzUFg3-mkOLE0JN5co-jumyzThXzP0DvQr4AXavn2VWPOXlABckuZASQdrPw-0UbNcNZ0VW4lrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، مذاکره‌کننده ارشد ایران، روز پنج‌شنبه گفت اظهارنظر مقام‌های ارشد ایالات متحده مبنی بر اینکه ایران دارایی‌های آزادشده خود را برای خرید محصولات کشاورزی آمریکایی هزینه خواهد کرد، «ادعای دروغ» است.
او در شبکه ایکس خطاب به مقام‌های آمریکایی نوشت: «تنها محصولی که ما برداشت می‌کنیم، همان چیزی است که شما سال‌ها پیش کاشته‌اید: دهه‌ها بی‌اعتمادی!»
این در حالی است که بعد از اظهارنظر دونالد ترامپ، رئیس‌جمهور ایالات متحده، درباره این که ایران با بخش عمده دارایی‌های آزاد شده خود محصولات آمریکایی خواهد خرید، اسکات بسنت، وزیر خزانه‌داری آمریکا نیز روز چهارشنبه تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای «خرید مواد غذایی و دارویی از آمریکا» استفاده خواهد شد.
پیش‌تر عبدالناصر همتی،‌ رئیس‌کل بانک مرکزی ایران، نیز گفته بود که براساس یادداشت‌های امضا شده بین دو کشور هیچ الزامی برای خرید نهاده‌های کشاورزی از آمریکا وجود ندارد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 277K · <a href="https://t.me/VahidOnline/76664" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76663">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">(
⚠️
۲۰ دقیقه، ۳۰ مگابایت، با زیرنویس فارسی)
مارکو روبیو، وزیر خارجه آمریکا، پس از نشست وزیران خارجه کشورهای عربی حوزه خلیج فارس در بحرین گفت هیچ‌یک از این کشورها از دریافت عوارض برای عبور کشتی‌ها از تنگه هرمز حمایت نمی‌کنند.
او افزود کشورهای عربی خواستار اطلاع از همه مراحل مذاکرات با ایران هستند و آمریکا نیز مایل است آنها در روند مذاکرات مشارکت داشته باشند.
روبیو تأکید کرد تهدید یا مسدود کردن تنگه هرمز از سوی ایران «مشکل‌ساز» خواهد بود و گفت: «هیچ کشوری در جهان از پرداخت پول برای عبور از تنگه‌ها حمایت نمی‌کند.»
عمان نیز روز پنج‌شنبه تأکید کرد که هیچ‌گونه عوارض ترانزیتی در تنگه هرمز اعمال نخواهد شد.
این اظهارات در حالی بیان شده که مقام‌های جمهوری اسلامی بارها گفته‌اند در حال مذاکره با عمان برای اعمال یک سازوکار نظارتی و دریافت عوارض برای عبور از تنگه هرمز هستند.
@
VahidHeadline
ویدیوی بالا درباره بخش‌های مرتبط با ایرانه و گزارش چت‌جی‌پی‌تی ازش:
https://telegra.ph/Rubio-06-25-4
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76663" target="_blank">📅 18:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76662">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RvrQpAKfkhb9M4Tu4FiPwdfn3DavJXGTqeR1Yr3wowNmVp3vvzjChJsomiqClqUt7ir9Y6dNqgQavfdB43H2R0YAtA43MI-Hv6ijeXB0PN8vdBluAcab3qRKnTdhJVk7KC8gEM2x6whZSJ50S7Qc-qjrFBeCRNF_gSBGKQtCyIqEgCj-67cxI-mipu8F-a6cTiLhTCSSIOE1hrIAnNXCrIS5XIZ5G4CbAVudaT5IxRX45UjBMT7-Hi8EWr_goOx-g4iZHg-YOuFk92IyYbeG8WZAuy_yCvLdpXEe1oMcCHO9UF28KJAwiy_QA7LwIX9Ths0bQT0W7LG4VH8-Zd_zKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🔴
بنیاد عبدالرحمن برومند دست‌کم ۸۰۶ مورد اعدام را از آغاز سال ۲۰۲۶ در ایران مستند کرده است.
‏
🔸
روند اجرای اعدام‌ها در ایران حتی پس از برقراری آتش‌بس میان ایران، ایالات متحده و اسرائیل شتاب گرفته است. به طوری تعداد اعدام‌های ثبت شده از دستکم ۷۴ مورد در ماه گذشته به ۱۰۳ مورد، تنها در ۲۳ روز نخست ماه جاری رسیده است.
‏
🔸
بسیاری از افرادی که اعدام شدند، در پی دادرسی‌هایی نامشروع، شتاب‌زده و فاقد شفافیت به اعدام محکوم شده بودند. متهمان به‌طور معمول از حقوق دادرسی عادلانه، از جمله حق برخورداری از محاکمه منصفانه و دسترسی به وکیل منتخب خود، محروم بودند و بسیاری از آنان به‌صورت مخفیانه و بدون اطلاع‌رسانی به خانواده‌هایشان اعدام شدند.
‏⁧
#نه_به_اعدام
⁩
@IranRights</div>
<div class="tg-footer">👁️ 240K · <a href="https://t.me/VahidOnline/76662" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76661">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">سپیده قلیان:
تا نت خوبه براتون بگم که اوضاع زندان سپیدار اهواز از دی‌ماه ۱۴۰۴ تا امروز برای معترضین خیلی بدتر از چیزیه که خودم تجربه کردم.
در دی‌ماه تا امروز، بازداشتی‌ها رو توی نمازخونهٔ زندان نگهداری می‌کردن/ می‌کنن. هیچ حقی برای ملاقات، هواخوری، وسایل گرمایشی یا سرمایشی نداشتن، و حتی دسترسی به توالت بیشتر از سه بار در طول روز نداشتن. گزارش بچه‌ها نشون می‌ده که خیلی‌هاشون آثار ضرب و جرح شدید داشتن. حتی نحوهٔ جلب‌شون هم عجیب بوده؛ مثلاً یکی از بازداشتی‌ها رو بعد از دستگیری با موتور بردن زندان و تحویل دادن.
همون‌طور که می‌دونید، زندان اهواز کانون اصلاح و تربیت برای دخترای زیر ۱۸ سال نداره، برای همین کودکان هم کنار بزرگسالان نگهداری می‌شن. زندانی‌ها آب آشامیدنی کافی و غذای مناسب نداشتن.
الان هم بازداشتی‌های جدید در زندان سپیدار در شرایط مشابهی هستن. این جداسازی که سازمان زندان‌ها از دی‌ماه انجام داده، اصلاً تفکیک جرائم نیست؛ فقط شکلی از کنترل بیشتر و آزار و شکنجهٔ سیستماتیک است. زندانی‌های سیاسی رو به بدترین شکل از بقیه جدا کردن، توی جایی بدون نور طبیعی، بدون آب خوردن کافی، بدون دسترسی ۲۴ ساعته به توالت و حمام. حتی نداشتن این امکانات پایه رو به عنوان بخشی از شکنجه اعمال می‌کنن.
#زندان_سپیدار_اهواز
sepideqoliyan
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 302K · <a href="https://t.me/VahidOnline/76661" target="_blank">📅 18:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76660">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b_dGw1pjIUVOhlraRiTFfoQI8ucIOf53zkcUdl7I6ORtHKrJThoEO2oUF0E5Yqrp1WAlagBO2n0Sj4NrtjyKbvPZXIVQTZ96zAEZVWMLbxVUJGKHj1DuZyhFRlu0VAMC8EimuWYqNJvsOOwMbXFl3uX-bHKJtxbPC7QZhoPQhRjFOzrEKEVjBcluL2i5YbilgCeYmWAiY2PJbWpeGU0oL113WVCpDpkJei8pAvHRziSffL74JethMFaFni6FxUdyV1bCc9O8haKHzGW_D8iqLdMBcrUTqEVLf5nB-0RpFY48OAbR9-CGuoSARDBufcpsOlqx-5gIDwSa5OUSZq3kiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سنای آمریکا با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد.
ترامپ، پس از تغییر نتیجه رای‌گیری در سنای آمریکا درباره قطعنامه اختیارات جنگی ایران، از چند سناتور جمهوری‌خواه قدردانی کرد.
پست ترامپ، ترجمه ماشین:
وای! سنا همین حالا رأی خود درباره ایران را از ۵۰ به ۴۸ علیه، به ۵۰ به ۴۷ موافق تغییر داد. رند پال و بیل کسیدی تغییر موضع دادند.
از رهبر جان تون، لیندسی گراهام، برنی مورنو و همه تشکر می‌کنم.
این رأی به ایران هشدار می‌دهد!
رئیس‌جمهور DJT
realDonaldTrump
سنای آمریکا با ۵۰ رای مخالف، ۴۷ رای موافق و یک رای ممتنع، با آغاز بررسی «قطعنامه اختیارات جنگی ایران» مخالفت کرد. این قطعنامه از سوی تیم کین، سناتور دموکرات، ارائه شده بود.
با شکست این رای‌گیری رویه‌ای، بررسی «قطعنامه اختیارات جنگی ایران» عملا متوقف شد.
جمهوری‌خواهان و دونالد ترامپ استدلال کرده بودند تصویب این قطعنامه می‌تواند اهرم فشار آمریکا در مذاکرات جاری با جمهوری اسلامی را تضعیف کند.
رند پال، سناتور جمهوری‌خواه آمریکا، اعلام کرد در رای‌گیری درباره قطعنامه اختیارات جنگی مربوط به ایران، رای «ممتنع» خواهد داد.
او گفت به نظر می‌رسد درگیری‌ها پایان یافته و دونالد ترامپ از او خواسته است تاثیر این رای بر روند مذاکرات را در نظر بگیرد.
رند پال افزود: «رای ممتنع من راهی است برای اینکه به رییس‌جمهوری فضای بیشتر و اهرم قوی‌تری برای مذاکره به منظور دستیابی به صلحی پایدار بدهم.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76660" target="_blank">📅 07:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76659">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qlYH3LZv-pd_aeu9OXOvFdPLgE0v-7irofJ57f-qJOezejNtuu23H33XIHDfDECVvhU0yOK3EPh5rjyjFtFiAR9kNJVID9QZl7NBgfJU961eMX5ygsznH6FuJuLUft8XXRF6hTtdlt7PitA6NdLljFvhL_1DyW06zWRdyB1B334_srMEvyBXltGk6sXhVsBbXc_KqdcjoDXZ4HhOwP3QNikd4BSeOi6x8kczCZLNXImmQjAmZmkcmJmRhTLpuYSRvYmjhS3NydBi4WJGSnULrwoFsHy6QlPGsDhS-GJ469HkfbeAe00FdHuoBGADDkA2IxiGCb-7W_lBHHu3fq0_K4jcYtuVKnp0zDLvivWQMF_iSwiwSvOEyL1jCztiqk6o86LcGSrDwBD7RlAa5Wmk6X6tDf4I-YqFX5QUO-CP2_zAkU8ICa8qds2SvGNcSz5hETStSZUmKCqLg7Q3rOUZ0ZXiE6yx8BA7aIvwv-ExaUCcLKv93H6pEUnnjjKfQkqeySDro6M1XmkUQhYyqciO_DNbkR05uh1fEmwy-StlcaXPJbsmj38Ha_pDnlvVDTE84Lpsgr-bENrqdvJcuD5UykKbaMubxinhVIOMHDbABPKUlotJLs6rgOuawQzdniTH2AvxIqxhzODoXfSenYKK94w-dgYufzdZxrBypivANVc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2898920f34.mp4?token=qlYH3LZv-pd_aeu9OXOvFdPLgE0v-7irofJ57f-qJOezejNtuu23H33XIHDfDECVvhU0yOK3EPh5rjyjFtFiAR9kNJVID9QZl7NBgfJU961eMX5ygsznH6FuJuLUft8XXRF6hTtdlt7PitA6NdLljFvhL_1DyW06zWRdyB1B334_srMEvyBXltGk6sXhVsBbXc_KqdcjoDXZ4HhOwP3QNikd4BSeOi6x8kczCZLNXImmQjAmZmkcmJmRhTLpuYSRvYmjhS3NydBi4WJGSnULrwoFsHy6QlPGsDhS-GJ469HkfbeAe00FdHuoBGADDkA2IxiGCb-7W_lBHHu3fq0_K4jcYtuVKnp0zDLvivWQMF_iSwiwSvOEyL1jCztiqk6o86LcGSrDwBD7RlAa5Wmk6X6tDf4I-YqFX5QUO-CP2_zAkU8ICa8qds2SvGNcSz5hETStSZUmKCqLg7Q3rOUZ0ZXiE6yx8BA7aIvwv-ExaUCcLKv93H6pEUnnjjKfQkqeySDro6M1XmkUQhYyqciO_DNbkR05uh1fEmwy-StlcaXPJbsmj38Ha_pDnlvVDTE84Lpsgr-bENrqdvJcuD5UykKbaMubxinhVIOMHDbABPKUlotJLs6rgOuawQzdniTH2AvxIqxhzODoXfSenYKK94w-dgYufzdZxrBypivANVc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نشست خبری ترامپ و دبیر کل ناتو
در بازه‌های زمانی مختلف از این جلسه ۴۵ دقیقه‌ای، در مجموع حدود ۵ دقیقه درباره مسائل مرتبط با ایران حرف زده شده، به تشخیص ماشین البته:
مارک روته، دبیر کل ناتو:
اول از همه، درباره ایران. واقعاً می‌خواهم روشن کنم کاری که شما درباره ایران انجام می‌دهید چقدر مهم است.
این، پیش از هر چیز، درباره توان هسته‌ای است؛ توانی که ایران عملاً در آستانه دستیابی به آن بود. و این می‌توانست تهدیدی برای منطقه باشد. می‌توانست تهدیدی برای کل جهان باشد. این کشوری است که هرج‌ومرج صادر می‌کند. تروریسم صادر می‌کند. و آن‌ها خیلی نزدیک بودند به اینکه به توان هسته‌ای دست پیدا کنند.
هفته گذشته در گروه هفت دیدید که همه رهبران گروه هفت از این واقعیت استقبال کردند که این توان هسته‌ای تضعیف شده است. این فوق‌العاده مهم است.
و فقط می‌خواهم این را روشن کنم، چون گاهی می‌پرسند اصلاً همه این ماجرای ایران برای چه بود؟ این درباره امنیت و ایمنی است. این یعنی رهبر جهان آزاد مسئولیتی را فراتر از سواحل ایالات متحده، برای بقیه جهان، بر عهده می‌گیرد. و این همان کاری است که شما انجام دادید.
می‌دانم بحث‌هایی بوده درباره اینکه آیا متحدان اروپایی‌تان به اندازه کافی کنار شما بودند یا نه. فقط می‌خواهم یک چیز بگویم؛ می‌دانم شما چنین فکری دارید، و ناراحتی شما را از این موضوع می‌دانم.
اما وقتی به اعداد نگاه می‌کنید، چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های اروپا برخاستند؛ در شش هفته‌ای که این جنگ جریان داشت، تا زمانی که آتش‌بس در میانه آوریل برقرار شد. بخارست، فرودگاه رومانی، مجبور شد به روی پروازهای تجاری بسته شود، چون باید مطمئن می‌شدند که شما بتوانید هواپیماهای سوخت‌رسان را در هوا نگه دارید.
پس این ماجرا بزرگ بود. می‌دانم موارد پراکنده‌ای بوده که واقعاً از آن‌ها ناامید شده‌اید. اما به‌طور کلی، متحدان اروپایی شما در کنار شما بوده‌اند. واقعاً می‌خواهم این نکته را بگویم: چهار تا پنج هزار هواپیمای آمریکایی از پایگاه‌های هوایی اروپا برخاستند.
خبرنگار:
پیام شما به دوست بزرگتان، اردوغان، و مردم ترکیه چیست؟
ترامپ:
من او [اردوغان] را دوست دارم؛ او دوست من است. او وارد جنگ نشد. او یکی از گزینه‌های اصلی برای ورود به جنگ با ایران بود. شاید هم در طرف ایران، چون همان‌طور که می‌دانید طرفدار جدی اسرائیل نیست. و من از او خواستم وارد نشود؛ او هم وارد نشد.
2:11
خبرنگار:
می‌توانم یک سؤال دیگر بپرسم؟ آیا گزارش مربوط به حمله به مدرسه میناب را دیده‌اید، آقا؟ می‌توانید به ما بگویید؟
ترامپ:
نه، آن را ندیده‌ام.
خبرنگار:
چرا نه؟
ترامپ:
خب، باید صبر کنم تا کامل شود. نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند. یعنی می‌توانید حرفم را بشنوید، اما نمی‌دانم اصلاً بتوانند— آن‌ها خواهند گفت یکی از موشک‌های ما بوده.
پیت، نمی‌دانم اصلاً بتوانند آن مسئله را حل کنند؛ از نظر اینکه تقصیر چه کسی بود. چون موشک‌ها از همه طرف در هوا بودند. ببینید، شما انتظار نداشتید— و آنچه رخ داد وحشتناک است. اما موشک‌ها از همه طرف در هوا بودند.
و کسی گفته این موشک ما بوده؟ خب، شاید موشک ما نبوده باشد. اما من چیزی ندیده‌ام که مرا به این نتیجه برساند. موشک‌های زیادی هم از سوی طرف‌های دیگر شلیک می‌شد. پیت، نظر تو چیست؟
پیت:
خب، آقای رئیس‌جمهور، ما این تحقیق را بسیار جدی گرفته‌ایم. و وقتی زمان مناسب برسد، هر نتیجه‌ای که به دست آمده باشد، همان زمان برای اعلامش خواهد بود.
ترامپ:
منظورم این است، اگر به پاسخ درست برسید، فکر نمی‌کنم کار ما بوده باشد. فکر نمی‌کنم ما بوده باشیم. موشک‌های زیادی به سوی آن‌ها شلیک می‌شد.
خبرنگار:
آیا جلوی توافق نهایی ایران را می‌گیرید، اگر شامل هر نوع هزینه‌ای برای کشتیرانی باشد یا [نامفهوم]؟
ترامپ:
بله، برای من غیرقابل قبول خواهد بود. چون تنگه‌های متعددی داریم و اگر برای آن‌ها چنین کاری بکنید، باید برای دیگران هم بکنید. تنگه‌های دیگری هم هست؛ آنجا هم اجازه چنین چیزی را نمی‌دهم. بله، این قواعد بازی را عوض می‌کند.
خبرنگار:
آقای رئیس‌جمهور، فکر می‌کنم رأی کنگره برای پایان دادن به جنگ با ایران، حتی به شکل غیرالزام‌آور، تا حدی بر مذاکرات با ایران اثر می‌گذارد.
ترامپ:
ما در مذاکراتمان با ایران عالی پیش می‌رویم. درست وسط یکی از مسائل کلیدی، که در هر صورت به آن خواهیم رسید، خبر فوری داریم: سنا رأی داده که دوست دارد ترامپ جنگ را متوقف کند. ایران این را می‌بیند و می‌گوید: «این دیگر چیست؟»
حالا، می‌دانید که این بی‌معنی است، درست است؟ اما تعدادشان برای من کمتر بود. چهار سناتور جمهوری‌خواه داشتیم و همه دموکرات‌ها.
دموکرات‌ها می‌خواهند جنگ را ببازند، چون احمق‌اند. برای همین به آن‌ها «داموکرات» می‌گوییم. آن‌ها کودن‌اند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 349K · <a href="https://t.me/VahidOnline/76659" target="_blank">📅 01:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76658">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdur6BPbd5CoMEMb7hvW3kId_OiOSz431ds7_oiP4nqPAMTd15DnHyXa8hVL-gmsYJ4onrIDQoype-MkibupZmwDM1a7a6Eda5N4ml28jAmmFaQ1x__7uHzeThCcKnMbyulKXAjmIznXqKpJWYXAUqdv45YIdlUn9ugfjRgTk1WAmHgcQpe0fqd5ZzlCa3l3dy6SxnsvK7EeA9-DPTdK_erF3NZKVUOmoXbkyJDKP1ECfyPUaAes4vx5yNJM34ZRk-NdZIe7FtQnke02qvB_TGuC62Yu6FVC-hvgR60L7m690m9k-8oqvgW3udfwK_tb5owwVb5Mzqx31yh-JoCrtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به گزارش رویترز دولت دونالد ترامپ، رئیس‌جمهور آمریکا، قصد دارد طرح فروش ده‌ها موتور جت به ارزش صدها میلیون دلار به ترکیه را پیش ببرد.
چهار منبع آگاه به رویترز گفتند که این کار با وجود مخالفت‌ کنگره صورت می‌گیرد. خرید این موتورهای جت تحولی مهم برای آنکارا پیش از نشست ناتو در ماه آینده است.
این موتورها که تولید جنرال الکتریک هستند، نیروی محرکه قاآن، اولین هواپیمای جنگنده ترکیه، را تأمین خواهند کرد.
ترکیه به عنوان عضو ناتو این پروژه بزرگ را در سال ۲۰۱۶ برای خودکفایی دفاعی بیشتر آغاز کرد.
یکی از این منابع گفته است که این قرارداد بیش از ۷۰۰ میلیون دلار ارزش خواهد داشت و قرار است ظرف چند روز آینده نهایی شود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76658" target="_blank">📅 22:48 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76657">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/89b252a095.mp4?token=JShJP-t8QtYzqqDcLQr30oyw0h0bGlVeWVb6rPTCRq2tEuA-uVGmgk8mIaHBoO9MU3xjQkqgL9oTgLQtzx6CdGUfnDo7N7-e-vdFAyEGoTSe2JgLz7kOjwoq5Lrsj9uv1bEM8nQq8m-2tzi2sVln06zCtyt-cVhkzNB4kQeHubozWd6EogLExMB5EXwDFuS_3L5qEvSOYj8WaFEowvOLtlSNPzxY-0G7M_PEe9qtOy28hftXCmuCLi8n8F1PKYgXQ3tyfhAYsKlkoqbLHv4fKvPZ0KZrhiT508NuC3AqIpvvv7KTLZTMtg_RgchGYCIaRr3iKMlHIpfvHR8AlXNLFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/89b252a095.mp4?token=JShJP-t8QtYzqqDcLQr30oyw0h0bGlVeWVb6rPTCRq2tEuA-uVGmgk8mIaHBoO9MU3xjQkqgL9oTgLQtzx6CdGUfnDo7N7-e-vdFAyEGoTSe2JgLz7kOjwoq5Lrsj9uv1bEM8nQq8m-2tzi2sVln06zCtyt-cVhkzNB4kQeHubozWd6EogLExMB5EXwDFuS_3L5qEvSOYj8WaFEowvOLtlSNPzxY-0G7M_PEe9qtOy28hftXCmuCLi8n8F1PKYgXQ3tyfhAYsKlkoqbLHv4fKvPZ0KZrhiT508NuC3AqIpvvv7KTLZTMtg_RgchGYCIaRr3iKMlHIpfvHR8AlXNLFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا:
«هر زمان که وارد یک مذاکره می‌شوید، با یک روند بده‌بستان و امتیازگیری متقابل روبه‌رو هستید. این یک اقدام موقتی است؛ فقط برای ۶۰ روز در نظر گرفته شده است.
در نتیجه آن، ما انتظار داریم آن‌ها به تعهداتی که در سوئیس پذیرفته‌اند عمل کنند. اگر به آن تعهدات پایبند نباشند، رئیس‌جمهور گزینه‌های زیادی در اختیار دارد.»
USABehFarsi
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 319K · <a href="https://t.me/VahidOnline/76657" target="_blank">📅 22:05 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76656">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=Fiu2TuYr7YMigkHDLpvYglkYtUVkNS6cMRU9_I3eQdVkGfH8gPTN-kDj8F5CVpOAVTnnfBG2YPEiJ_fgrIHQ4LA-1klGf3uZGhDNbNa7X3V5gVzkozE7_yyDpUl2SAqcDaATCLObx-H38i67QYJCNq8vFB8WqZffQXWL9OeNUlq3ESfvIuzmD0flBg-8D9Nt5NMc2SmoNBtN_47by4_oUnfpHW5S90jJhsqEAos_K1J1kg0RHdxpwSmecgtKIWI0LjHfHuhHM4i7HT8wpi180jYDBW2O80Od9TGoYUl7DEDz6C33WInrRdVqIYJtz8G8r6WexbF-8pixLZ6mGvrdNA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0ce9ece0.mp4?token=Fiu2TuYr7YMigkHDLpvYglkYtUVkNS6cMRU9_I3eQdVkGfH8gPTN-kDj8F5CVpOAVTnnfBG2YPEiJ_fgrIHQ4LA-1klGf3uZGhDNbNa7X3V5gVzkozE7_yyDpUl2SAqcDaATCLObx-H38i67QYJCNq8vFB8WqZffQXWL9OeNUlq3ESfvIuzmD0flBg-8D9Nt5NMc2SmoNBtN_47by4_oUnfpHW5S90jJhsqEAos_K1J1kg0RHdxpwSmecgtKIWI0LjHfHuhHM4i7HT8wpi180jYDBW2O80Od9TGoYUl7DEDz6C33WInrRdVqIYJtz8G8r6WexbF-8pixLZ6mGvrdNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه آزادی ملیکا ملک‌محمدی
این نویسنده و دستیار کارگردان تئاتر نیمه‌شب ۲۵ دی ١۴٠۴ در پی اعتراضات مردمی، با یورش خشونت‌بار ماموران امنیتی به منزلش در تهران بازداشت شده بود.
FattahiFarzad
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 316K · <a href="https://t.me/VahidOnline/76656" target="_blank">📅 21:24 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76655">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=DHBFPZXO8MuqQGszCRhlBSjXicOC77QTBo-1frJ92n8jhIXbLVrAL8NIbcsh3OTPU4_DRbFviRIaA3GwQqE5XVCSr9T2uh5CKuMJ-RL3gAqMp6SXaX3sszSoNPjJMM1o_Nx_ESMpYFmSD4ts5pfImSWPak0tSATkW_aYXrRZY_43CqDsOb1onl-0hFAijEM1i2nwj6dJBpyVDon4Uxdu_2LHTKtcPJVogzh4l3CRytdHBFbS98e6iZeqANc2gE-xAd6SD0DA-GKPUmxgzPOurVO-XZKGaDJYUmoelfmTonYXW-Khim9sC89dbpZRU6Xlrkr747zPgnwZHEJ5ZUxYSg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4a1f499b5e.mp4?token=DHBFPZXO8MuqQGszCRhlBSjXicOC77QTBo-1frJ92n8jhIXbLVrAL8NIbcsh3OTPU4_DRbFviRIaA3GwQqE5XVCSr9T2uh5CKuMJ-RL3gAqMp6SXaX3sszSoNPjJMM1o_Nx_ESMpYFmSD4ts5pfImSWPak0tSATkW_aYXrRZY_43CqDsOb1onl-0hFAijEM1i2nwj6dJBpyVDon4Uxdu_2LHTKtcPJVogzh4l3CRytdHBFbS98e6iZeqANc2gE-xAd6SD0DA-GKPUmxgzPOurVO-XZKGaDJYUmoelfmTonYXW-Khim9sC89dbpZRU6Xlrkr747zPgnwZHEJ5ZUxYSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دونالد ترامپ، رئیس‌جمهور آمریکا، روز چهارشنبه درباره روند مذاکرات با ایران اعلام کرد که تهران امتیازهای زیادی می‌دهد.
او گفت: «ایران در حال دادن امتیازات بسیار زیادی است و ما با اختلاف زیادی در حال پیروزی هستیم.»
او بدون بیان جزئیات بیشتر خطاب به خبرنگاران گفت خواهیم دید چه اتفاقی می‌افتد.
دونالد ترامپ ساعتی پیش از این اظهارات در گفت‌وگو با شبکه خبری فاکس نیوز گفته بود بازرسان آمریکایی هم با بازرسان آژانس بین‌المللی انرژی اتمی از تاسیسات هسته‌ای ایران بازدید خواهند کرد.
او در واکنش به اظهارات مقام‌های ایران در رد اجازه بازرسی به آژانس گفت: «آنها توافق می‌کنند، آن را کتبی می‌کنند، سپس می‌روند و می‌گویند که این درست نیست.»
رئیس جمهور آمریکا بار دیگر تاکید کرد که جمهوری اسلامی با بازدید بازرسان آژانس موافقت کرده است.
مقام‌های جمهوری اسلامی از زمان حمله آمریکا و اسرائیل به تاسیسات هسته‌ای فردو، نطنز و اصفهان مانع از بازرسی آژانس از این تاسیسات شده‌اند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 321K · <a href="https://t.me/VahidOnline/76655" target="_blank">📅 21:21 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76653">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=kqFaixH1z5pcjeyCH4kYiEH_LdMOEu9ObAdGOPK3rxY1M0BwdDc44uO17_TylifMGmkWetUknePFNV57kX35ylxlbObVaPAUVZzgTnTqCgCgVujbKBKs3YBj_L3vqOcfhvIm0uIqr36_o_vR_ANuMsGkM2KPF3o0f-DHRnCJ7fEIOV1VvFBCtXOj4rXsSIMWL_dQFA5zfiKOslbpo4-lO8mzLIxUgyglAqDzvoD8K84FiJ9CD-UlXhAFB3njvrK5s4ls2lSi4oFXEeKjSZRAS8xYG4ZUXPnLpwt3Mmltgh1AWMEJ9evQleCzRg7sr-CK2GCM4ARK0YitUGsn8y0BtA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/22f6c0cb75.mp4?token=kqFaixH1z5pcjeyCH4kYiEH_LdMOEu9ObAdGOPK3rxY1M0BwdDc44uO17_TylifMGmkWetUknePFNV57kX35ylxlbObVaPAUVZzgTnTqCgCgVujbKBKs3YBj_L3vqOcfhvIm0uIqr36_o_vR_ANuMsGkM2KPF3o0f-DHRnCJ7fEIOV1VvFBCtXOj4rXsSIMWL_dQFA5zfiKOslbpo4-lO8mzLIxUgyglAqDzvoD8K84FiJ9CD-UlXhAFB3njvrK5s4ls2lSi4oFXEeKjSZRAS8xYG4ZUXPnLpwt3Mmltgh1AWMEJ9evQleCzRg7sr-CK2GCM4ARK0YitUGsn8y0BtA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به  پزشکیان دوباره بیل دادند، اگه شهباز شریف جلوش رو نمی‌گرفت فکر کنم تمام اسلام‌آباد رو درخت می‌کاشت.
NR2OH
مسعود پزشکیان، رئیس‌جمهوری اسلامی ایران، در جریان سفر خود به اسلام‌آباد به همراه شهباز شریف، نخست‌وزیر پاکستان، در مراسم نمادین کاشت نهال دوستی ایران و پاکستان شرکت کرد.
ویدیوی منتشرشده از این مراسم نشان می‌دهد پزشکیان پس از قرار دادن نهال در محل کاشت، همچنان به بیل زدن و ریختن خاک اطراف آن ادامه می‌دهد؛ در حالی که شهباز شریف چندین بار با اشاره دست تلاش می‌کند پایان مراسم را اعلام کند.
در این میان، لبخندهای شهباز شریف و ادامه بیل زدن پزشکیان توجه کاربران شبکه‌های اجتماعی را جلب کرده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 336K · <a href="https://t.me/VahidOnline/76653" target="_blank">📅 16:46 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76652">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vtw_2T583vgaEoNPbRDxdQNYODRazJ6dHQBFrRECE1HNzCbIwOi0DqsPxa-T3Jv9ursq9N91B8r9rtx_L_62tr6gyrw9XHSrKSZvT7v1P6QyE_ocNNCpc9lxBSYsNrxqUkRGP1YMTNC4-mILrzSx6DS2wvqCik_YTQZIy6qGzRn39v1z7DmGpAVD5XWV1nTS4wO8B0NAEdR60odjHI757wKTMCbQTSGDNB2cDQD4wNuRy-S-I3bQ-oDBWRTgfiJDQBMGOkRhjmkysDOsH6vCSr2AbSJmkHn9yV2WjklcMWt4PK5XNdj1E0x1nE8K7EVhAjunVjwyhNBVTyr7qqDDTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خزانه‌داری ایالات متحده روز چهارشنبه گفت واشینگتن بر نحوه مصرف دارایی‌های آزاد شده ایران نظارت خواهد کرد و به همین منظور دفتری در دوحه، پایتخت قطر، برای نظارت بر این وجوه تشکیل خواهد شد.
اسکات بسنت در گفت‌وگویی با شبکه خبری سی‌ان‌بی‌سی، تأکید کرد که درصد زیادی از دارایی‌های آزاد شده ایران برای خرید مواد غذایی و دارویی از آمریکا استفاده خواهد شد، حتی اگر ایران گفته باشد که نحوه مصرف این منابع را خودش تعیین خواهد کرد.
او بدون ارائه جزئیات درباره سازوکار نظارت بر مصرف این منابع گفت این وجوه توسط وزارت خزانه‌داری آمریکا در خاورمیانه نظارت خواهد شد.
مفام‌های جمهوری اسلامی در روزهای اخیر با رد اظهارات مسئولان آمریکایی گفته‌اند نحوه استفاده از منابع آزاد شده در اختیار تهران است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 292K · <a href="https://t.me/VahidOnline/76652" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76651">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l1TFdX1QlKG1mzgOBae1aHB0ysctdG7uW_Um5Z2y4B6CQ3V9cYikQmEUtv2W0cYyw8oZBu-mpY40ol8BcZPNEdwP8IFMdBJxs7tTXAwcYGNHkx4Cz7pEKoiLwnDp8DACVPNNFV9nllaHDEhP9u2HJ9Y-f4ppaMhxiTwnBrpYVXtnrjmlVJnDCO95hxIfyiMs6zN2uObAtB4DB1ZWin65x86YxmnR0r-M4TnrS0fK2P2S0G3pP3kK7soceLNDTITH3C1Fw4NKUPDZxCkNNuBdpnrQROeDIIEcJL5Xbs48rEzTIkYLYcIjuCozeDUcSzuZrfaRfOVM4Y2wemaMJ2xmsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معاون وزیر خارجه جمهوری اسلامی اعلام کرد که دسترسی به تاسیسات مورد حمله واقع شده و مواد هسته‌ای صرفا در چارچوب توافق نهایی با آمریکا ممکن خواهد بود.
کاظم غریب‌آبادی روز چهارشنبه در شبکه اجتماعی ایکس با اعلام این که در سوییس هیچ نشستی با رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی «علیرغم درخواست او»، برگزار نشد، نوشت: «هیچ برنامه‌ای نیز برای دسترسی به تاسیساتِ مورد حمله واقع شده و مواد هسته‌ای وجود ندارد.»
او افزود: «این مباحث صرفا در چارچوب توافق نهایی و در نتیجه اقدام عملی طرف مقابل در خاتمه تمامی تحریم‌ها و... بررسی و تعیین تکلیف خواهند شد.»
پیشتر گروسی اعلام کرده بود که سایت‌های غنی‌سازی هسته‌ای جمهوری اسلامی توسط بازرسان آژانس مورد بازدید قرار خواهند گرفت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 275K · <a href="https://t.me/VahidOnline/76651" target="_blank">📅 16:42 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76650">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EUcXR8e6fJuX_P40OkMCxV9TXyXV6Gb3fPFrfPmzeVvplp0VvdtZWEkS_LJc-jPxEtaI89LKDOu4eOXUNC2IPmgtLJqE2XUHnBDYa8i2rEFGyRvQIfJJ0siNDKKOVM_pX2BtFnwJJSVGeEkh2fEIF37V_HUm2aV3qvHgudL6ayWTQHDe5voV-7rUVBy0I7vH116ECnf8xq_hx1G59_tnmYARxAl-t6pEr0-J2d-jBN_MR-FG9ejd1JeQ43EnDHGqymTDnpvOxicCSEo1kY0H9CYf7rKcDcOyiFytPPbbut5pep7zZEQUcyN_vMY3jFKNUPX3eJsRtl_1T0z9pWTbfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه آمریکا، روز چهارشنبه در دیدار با رئیس امارات متحده عربی در ابوظبی درباره تفاهم‌نامه ایالات متحده با ایران گفت‌وگو کرد.
در بیانیه سخنگوی وزات خارجه آمریکا آمده که روبیو در دیدار با محمد بن زاند آل نهیان و دیگر مقام‌های ارشد اماراتی «درباره یادداشت تفاهم رئیس‌جمهور ترامپ با ایران، تلاش‌ها برای تضمین عبور کامل و ایمن کشتی‌ها از ‌تنگه هرمز و اهمیت صلح و ثبات در منطقه» گفت‌وگو کرد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 247K · <a href="https://t.me/VahidOnline/76650" target="_blank">📅 16:41 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76649">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tS_ytJfCGR2libkzbJ4VPMhW7b4MBpyWY9N6riQomdbibOqdH7Qoz9sSd-CPDwXamssbLi9BX-IfsnGR8MPNKhyuoSAKydxRuECCTKFyxHAzWTVBbZx247df-sCrii0rXyJ1sGm_4XgpV9B0KWsllw2kQKXS-N9AlWrNFxBhr2DQiIgii9WbJeJb0PN5zKWJrEhn4Ax_iX3xqiX_rPCXb7EhE6VXtJCq5ARhya7umwZ6qxh5F2vq_r_th2_IXI5g9bJ5kxLjjQfqUOXUuMzzTZMjwT7tnOr0i89Zn25gZxm4EA_yAcF6xlfBSAKQY4oI-Vn6rQc35-e6ewJXahX2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کامران غضنفری، نماینده تهران در مجلس، ضمن انتقاد از تداوم تعطیلی صحن علنی، به خبرگزاری ایلنا گفت که قالیباف طی چهار ماه گذشته بدون هیچ مبنای قانونی از برگزاری جلسات علنی جلوگیری کرده است.
این نماینده مجلس، وجود مصوبه شورای عالی امنیت ملی برای تعطیلی مجلس را «دروغ» خواند و گفت تعطیلی صحن با هدف جلوگیری از مخالفت نمایندگان با روند مذاکرات و پذیرش آتش‌بس صورت گرفته است.
او ادامه داد: «نمایندگان هم از یکی دو ماه پیش از قالیباف خواسته‌اند که اگر چنین مصوبه‌ای وجود دارد، آن را به ما نشان دهید، اما او هیچ چیزی نشان نداده است. بنابراین، این ادعا کاملا کذب و دروغ است.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 226K · <a href="https://t.me/VahidOnline/76649" target="_blank">📅 16:40 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76648">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RjRe5-QDxAVyviEJzI8oJlVbw9mTN7wuVll1WCUQQcquVZXGfGuPxI-l49K2cgo3-qDJSzNNt_n4grCvijsuNrzA4NYs80JPwaULIDfsEWgZqviPR-aO634XjWbCBvKsZ0Kf0PcdRFhDBd49gaMVHIaaHVFntiXBZ__Z1waKfalzeaXZzTUkB6DuLWt2o_wEFSTQ9sJIKgztHwV2pqVnwFXNNQxFd58Ly9Ago0JL55_BI-ua9_BbWu6jo-V4qDja4QswU7iMpQ8pLEflIOpqIy69aXdxxhS_wG9EojJ9mqFjQFaEDAo_PSlztlEbD-Aynrzb1uN-qMhWYpm6PPCttg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
ایران به آمریکا اطلاع داده است که، برخلاف گزارش‌های دردسرساز فیک‌نیوز، «هیچ عوارضی، هیچ هزینه بیمه‌ای، و هیچ نوع هزینه دیگری از هیچ‌گونه‌ای از سوی ایران برای کشتی‌هایی که از تنگه هرمز عبور می‌کنند مطالبه یا دریافت نمی‌شود.
اگر این اطلاعات نادرست باشد، مذاکرات فوراً پایان خواهد یافت!
علاوه بر این، هیچ پولی از سوی آمریکا به ایران داده نشده، یا از پول‌های خودشان برایشان آزاد نشده است.
ما بخشی از پول آن‌ها را، که کاملاً تحت کنترل ماست، برای خرید ذرت، گندم، سویا، و چیزهای دیگر، در اختیار کشاورزان و دامداران خودمان قرار خواهیم داد.
غذا در ایران به‌شدت مورد نیاز است، و ما آن را منحصراً از ایالات متحده برایشان خریداری خواهیم کرد.
از توجه شما به این موضوع سپاسگزارم!
رئیس‌جمهور دونالد جی ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76648" target="_blank">📅 16:39 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76638">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromبنیاد عبدالرحمن برومند برای حقوق بشر در ایران</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BmJ0vYwd3CNvvaYgIgl9X89AHGPmnqjZoB7Poi6hpoPFvz1jAV1vL4WwN1B4c8M2dfADH9qLIs2_D6ss2O8f0SOnUNvP08M9dbepitiN1O4mWbLM9Ijgj_guA3La0dqN44WB4lJoujDo0Kwy1YR7Ktd_aMBZKwJ7UYDTYmnO8TceH6ej3GChKQ7_OdAhknpCjtonHfiA1mvekp3_pTn-lXlVdXLcZch6NKPvg9K8mmDi6o7FHRWDDEU_i4pOXk9q6y8wLLI8ZuHiZQD7XR7aAcgWNXx9n7VF9Yf2jDMXYRW7D17GPPZlMFqWwVwmHWAIfUm4iNscZ_C7UPeGm5FO6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oVPyUxey4OW6GLJbAIbi5Hr9XnItGSk0t2Ska62_RNA1ZpR585DmpCBLETNFeM9_zeyrcJsIPqWHtuvbOjZXgvePTeZa5K6lSfFLQNcrKnNR4887eIqF90bLVWzeiv9Zennp_xu0lNVcLDSWDZNFiihkLlB5z6-6e276LubmfrC9ODPTqM7FwCSOMhVqLMjQ4QjsK8zZuiXvnzhbMMx2s9vnxOoj9_VD-BcCUX2obT5zi0vs8Au8OH6mNPjkZvj_Eym6RFMaliEy8Zd-HVXIwBhy1YBtDUmApNr4Bs9DIMUGmYja_PSaWdXrJv0UDqkvC7HIiBYjViy3wsfaIg-psQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e1UrZD-NGctDeHZriISs-q_3qqZIEVqulwMpU_qAAqmv4G8HWFvASF4xC_61UtzEe7BpggE1ncpm9uC6stg3UvkZfQ01VeUnvV3Ljz5tw40TEQFtnQ0NsbYDLxRa2K3UciYHgT7UhmJkGUX9f8waRxouwdpvXRbeLM6ktcedP_n9c8PCdG09x1-c2atQ74XICvQ6XEmJrLx8g2tK8msc-G9p6FkSf4Csqdm-eKD3ahOvELLCw_icWwjB-82_TZ1lW9u1vWpas1Vvnl2vm6KQ4lGieqOXHcWTEmEHCzp7_9ZL3LRCsN_iks5TWKJif3Lwb8im93n3kx1t-LPNfVsvkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R72fkyjJTnjvs3Kltp73x903-azXf2TFfrWlTrfq12ab0JOHqJyPG47NfGHC7nM9kXQ5NZc7-QnS869OPqjoPziQFUokRcBl7vwBuoiCO77SOyCfHHUinhjZJfPWtO8IHDPguADGBOxd56KeCzwmIgcHh3ndBPuz2ofHKPP4xvNyYg9YxeaN3fH-KovBT_9xe45j3HIJhWhV0b4Ud1xji_8hlMyKJ7s8unSvDFG_Q9mlDbV409fvf0HweTtnXP8NHxNzAb0Uij6uBVe4XpBnIC8yUb4z1ue95RX959kCp6_7SIq0U7qkqok1TrZ50KpjeV-btq5a4nvnopaPnSfGrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jXiFOaSzKkfVGduaGZfr-OkV8LzGHfiJWoanKYfk_WpzExSnYeNinYeJACo_ZrX91xbvNiMk0SEIiTapNt28Gi0fbLbyQMqWD_xYYnH3VmKSDvGwlMdnhpY49dA-MGRYx50YOzGASzkcUPxnYElLcgcz1In7C3JBMtOKf6PiqHxsTszRKciI3KlywSSh7G6LCUbiWl9e9MdjgGo1oolGNF_5bkscmRgUx3KJOnmemJxjYfcSDAY5lDoXcgVWGcTQ_AG2A3EAUby22LT2KcWgh_yKrJEL083Ai5XOR0WEjwWnC0dNwH-nPXWUCC9cjjauk3mFhUE7bob1TBk3XDmD1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aoRXABM9t_F7Uk7wrkUcfxB9s0-hP5qv17VcvRwaMJBqk3GgZ9Axs98URmlaySrwXNaf8A5v-efPmTjRBmj2qNbsAHIolYwvPzytYtTPcnOiT4wFyBl_dBdx0w2u-4qYBxdFR-rKTNsvzGe10U9shdYyxrQVEABlPrs4ghIZ_vI2k-0am4mxqH60Z4PvB9cUc9viLJJFn-DUbg84WGaJ8os96ikUqdbSicW7UU07Cs3thIx0cPJTnlXuYjXbxg3M2TOSdbBRuxXR0pFyL4XrfPiVkn0Rz_3xPT6o1_h3c1nfw0fdBAqdSufy58cvFWEa2Xi1vWM-K3HwfjFE-5F98Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cnK051ZpxnulCUdYagEVMv1BtxLT4F1lQddsKSF-P-QfirVMmhKP3lkN2zCXXFLAqcGyFyfmph-DOJ_iLQD3ZF2rOpoRuWqRSeqmN4gpIysZUfjP1jHzN_NTIQq1xYcYMh0-4622v7k-lsEnEERKcxyL0wZAGsz6cRJ_3vUDcIiddiqufM7NYM51X3ENXc6xP5B9Fklvici9zYAW_GWb8jLxfY99xqT7yPpRedt1Pb62seMjgRp7ERjcmHMlSfH4wEg_7ZAvNQ2ymktpfzvU8b3WyRlCxnRz-I1MoAvFCHgDfBnIitbm2uB1Gj9bSUPqvmONbWdLfI4df64gkKD4Fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PWt8czoZYH4IKX9pToxuI5Q15wHdyzjaELI2-oDKBb85tP6QLxvsJ0bjW-2fOflg1FPJTYBepDCnJc1FplUdXcc-alMDTGstackg1YlYSOD1Ve311IppF2AmD8UCrdSnWefBfe8fAe4pbUkxTufLpitl8cijV8m55G31ln3DPB03GLIBqRXhGAidT36Ao9uSdx6rDPTQBE27HBnVMizhMMam1_iK9EyiD--1hArCj0T3CSJT74_cLgKpjx0SV_neg8vL2xDPzuEuBzDszz3vcv3l9BR7GwVwK2AXJnuNLBfCsBer5mN84FFFhyMs04nf5A7-CVXGy4mDoJ4QSusBYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B6V4-tPP6JeyqKUPn0yIsmwZXg2A5dbQ9q9ZrLx_r96Pu7AJb2sy62-D4SC2HKhXVhJrCv7jF1IXliyFFlL6B6KQHlNTWJZN22mKbGg25a6RxDg81AlBRi0Ck6RwVZ-nHc1vCd5R-0rpdkataU9eMEiGX2pW66D62RIlcZEtevcHow06yfBZM0PdRN31GERwsHM2XyMUFVc_cVeYTbNRFGyPpXUdXWuBQ80Oia-DqWorowjNQs9oyeNYlbAdMr6cDS_v8-eVGyAI5qQqMEMkwFVXIALFfDwZxYrG1jypm1-K_IpP-4-SeFHnBuF0XGU20V76Y7CS1_Zarv7--yi3tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CTjnT8d3XQSvTyCa_DiFQijvjMGBTl3WAhB-AfEkp2j9oOCm5zXsVJjO93Gyz63I-ZJJLazjp8p4V0DXDr8m6MKbOBnwBNQMjFqqER-L9mhzNBy_x0-PsfEEaE-nsyOc6njkTZdnQ26v2QkTwcwdcCzBu5x82QWpOSJh6wtFCoS9pOxD--Hyk683wKfmJNaMCZByNOIbUxlQNv3YfA52AsaM-PnxgXqk_Eh_myeo5SLok-li8f27uHGI2qSezS5ywA0_JnKj53B0Irg_UiQXehkwnY999CaeCUmgYaW4uFd_YEXvaUIIVKFTsGV-wuXTCv4EkaLVpCjWwMl4_r2v4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‏
🔴
مرور قربانیان اعتراضات خرداد ۱۳۸۸
‏اعتراضات خرداد ۱۳۸۸ که در اعتراض به نتایج انتخابات ریاست جمهوری سال ۱۳۸۸ شکل گرفت، جانباختگان زیادی برجای گذاشت، بنیاد برومند تا کنون ۱۳۸ نفر از این افراد را که مرتبط با این اعتراضات کشته، ناپدید یا اعدام شدند را در نقشه اعتراضات خود ثبت کرده است. برای اطلاعات بیشتر در مورد این قربانیان به سایت بنیاد برومند مراجعه کنید.
اگر شما هم اطلاعاتی در مورد قربانیان اعتراضات دارید با ما در میان بگذارید.
‏لینک نقشه تعاملی اعتراضات:
https://www.iranrights.org/projects/protestmap/fa/
@IranRights</div>
<div class="tg-footer">👁️ 276K · <a href="https://t.me/VahidOnline/76638" target="_blank">📅 16:37 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76637">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=kzm5PsNgF19JT5N9V8_KxuM5nJ316lc0S0NaY0Dt-rcmBIHv3RAATUvg7HwBVqahuyRXAx_QUsDKOryilAVJsQQZUuMBnJFy8zDUzWAO4kIpDzUvCN7VDjfsTkeuxAhTfud1IW7tvvK84ZLr-x_spcB9-tww2WEPIpIWXjtibzQ1XjwP1GUtgX_PK4rcZNaio_W7RyNrUPSJ5Pz3CHJUiSxvWEGYNZlnK-FoUUsSI6VkvtP-UG4Mpv2e8x1_nYZq1zgeDAb20OXWKWRoko0C09-I32G9ZZ1yjWQzYmS4vsAUidEZ2VzFCvyxsRCz3x3bKhUuAwbl79i3YBnqFavfZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/e9d338b0f8.mp4?token=kzm5PsNgF19JT5N9V8_KxuM5nJ316lc0S0NaY0Dt-rcmBIHv3RAATUvg7HwBVqahuyRXAx_QUsDKOryilAVJsQQZUuMBnJFy8zDUzWAO4kIpDzUvCN7VDjfsTkeuxAhTfud1IW7tvvK84ZLr-x_spcB9-tww2WEPIpIWXjtibzQ1XjwP1GUtgX_PK4rcZNaio_W7RyNrUPSJ5Pz3CHJUiSxvWEGYNZlnK-FoUUsSI6VkvtP-UG4Mpv2e8x1_nYZq1zgeDAb20OXWKWRoko0C09-I32G9ZZ1yjWQzYmS4vsAUidEZ2VzFCvyxsRCz3x3bKhUuAwbl79i3YBnqFavfZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ترامپ پست کرده
متن صدایی که ازش شنیده میشه به تشخیص ماشین:
از سال ۱۹۷۹، زمان می‌گذرد.
ایران در ۴۷ سال گذشته هر سال آمریکایی‌ها را کشته است.
۱۶۰ گروگان کشته شده‌اند.
۱۸۰ حمله از سوی ایران به آمریکایی‌ها.
رؤسای جمهور پیشین با سازش با ایران، ۱.۷ میلیارد دلار نقد به آن پرداخت کردند و در حالی که ایران به دنبال سلاح هسته‌ای بود، از اعمال تحریم‌ها خودداری کردند.
این می‌تواند ۱۱ بمب هسته‌ای یا موشکی بسازد که به زودی ممکن است به خاک آمریکا برسد.
تولید قریب‌الوقوع یک سلاح هسته‌ای آن‌قدر نزدیک است که آرامش‌بخش نیست.
ایران چه زمانی به سلاح هسته‌ای دست خواهد یافت؟
هرگز.
متشکریم، رئیس‌جمهور ترامپ.
realDonaldTrump
پست دیگری که در واکنش به تصویب طرح توقف جنگ در سنا نوشته:
ترجمه ماشین: بنابراین، من ایران را در گوشه رینگ گیر انداخته‌ام، آماده زمین خوردن، حاضر است عملاً هر چیزی به ما بدهد، و برای نخستین بار در دهه‌ها، حسابی برای ایالات متحده و رئیس‌جمهورش، یعنی من، احترام قائل شده؛ آن‌وقت سنای آمریکا تصمیم می‌گیرد رأی‌گیری بدزمان‌بندی‌شده و بی‌معنایی درباره قانون اختیارات جنگی برگزار کند و به حامی شماره یک تروریسم در جهان بگوید که ایالات متحده کاری را که من با آن‌ها می‌کنم دوست ندارد و من باید متوقف شوم، و با این کار به دشمن کمک و آسایش رسانده است.
چهار بازنده جمهوری‌خواه همراه با دموکرات‌های احمق رأی دادند، و ایران از افراد من پرسید: «همه این‌ها یعنی چه؟»
این سناتورها همین حالا کار مرا دشوارتر کرده‌اند، اما من آن را انجام خواهم داد، به هر طریق ممکن، چون من همیشه کار را انجام می‌دهم!
رئیس‌جمهور DJT
realDonaldTrump
در واکنش به:
سنای آمریکا که در اختیار جمهوری‌خواهان است، روز سه‌شنبه از طرحی قانونی برای توقف اقدام نظامی آمریکا علیه ایران حمایت کرد.
سنا با ۵۰ رای موافق در برابر ۴۸ رای مخالف به این قطعنامه مشترک رای داد.
این طرح پیشتر در اوایل ماه جاری در مجلس نمایندگان آمریکا نیز تصویب شده بود.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 353K · <a href="https://t.me/VahidOnline/76637" target="_blank">📅 06:20 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76636">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Zuih1SmdMmKcKxE1fnVJEoxlOVTF3CETM06sT-zVzCLc7CL6y3FZrPx7AjRICR6PZAkiNkFOVfIA8u8Q5uPBoVBeT_uBtgkTiH-BJIoOShsrZehlPlvX6uM7URRmtgnzhuLK4ch1pjFlLZg0stYLt0kj-LSSD2jNd34xB6YngN-Ad82wiiE4Rz43a_MpPwYc37sgkvmKIVzKwddDse9_FTirWktophzDEYNN-LsVtDa9eDq55SNpo6K4Xm-_IpHfHRwAxA6kEf2EcWE5nKLICUpu1SERZjIYST743HUDfLIN_HY4VAnggyBCE3uYdsVyInl0UfS7akGkHBiQeLpRxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ProtesterCrow
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 351K · <a href="https://t.me/VahidOnline/76636" target="_blank">📅 03:58 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76635">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/sWInefbrPjHmX-vWbJ6rz2bvXzBC1zrJj_SpHigOSFArEED2EJVDW_n-SVts66zPzoiBhqi4nWrGQORe3tLdlxQmvfNrfXtFGdbcH9_yieuePK3_QYa8j9oXQGuZwFirPnil31pXVaOFVOPUsVA7LqyhfhbvreQ9pA4w7tdRtYinSxZf8FvFhhnStcUpeH5f1hQYeC2zfX0BHRu4meS3x_2s-25RBC7qsb8pzI5G1pwURda2JZom7pORJul3FRuyxm4aYa7SoyTUHhj4oMmeuoIHpIy9qHAdEeUPoNSYnvGoL_fjDmQSRD7gTwh61kzll8ZvwUMAZSmbFgnhOwD3Sg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سخنرانی ترامپ در پنسیلوانیا
جملات مرتبط با ایران به تشخیص ماشین:
ما به یک توافق صلح تاریخی با ایران دست پیدا کردیم تا درگیری در تنگه هرمز را پایان دهیم.
راستی، دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد. جای بسیار زیبایی است. این بیشترین مقدار نفت در تاریخ این تنگه است. هرگز چنین چیزی ندیده‌اید. به آن می‌گویند فوران نفت.
مهم‌تر از همه، داریم یک چیز بسیار مهم را تضمین می‌کنیم؛ چون دلیل انجام این کار همین بود. من به همین دلیل این کار را کردم. ۹۹ درصدش برای همین بود: ایران هرگز سلاح هسته‌ای نخواهد داشت.
اما یادتان باشد، این آسان نبود. ما ۴۷ سال رئیس‌جمهور و افراد دیگر داشتیم؛ کشورهای دیگر هم بودند. ما تنها کسانی نیستیم که هیچ کاری نکردند. آنها قلدر خاورمیانه بودند. حالا داریم ایران را بدون نیروی دریایی، بدون نیروی هوایی، بدون پدافند ضدهوایی، بدون توان موشکی، و بدون برنامه هسته‌ای باقی می‌گذاریم.
ما آنها را بدون هیچ ظرفیت هسته‌ای باقی می‌گذاریم، و آنها با این موافقت کرده‌اند. و رابطه‌مان هم خیلی خوب پیش می‌رود، هرچند اگر اخبار جعلی را بخوانید، هیچ‌وقت نمی‌فهمید. فکرش را بکنید، اخبار جعلی.
آنها ارتش ندارند، نیروی دریایی ندارند، نیروی هوایی ندارند، پدافند ضدهوایی ندارند. ما می‌توانیم هر وقت بخواهیم بر فراز تهران پرواز کنیم. هیچ‌کس کاری به ما نخواهد کرد. بعد اخبار جعلی را می‌خوانم که می‌گویند اوضاع آنها خیلی خوب است. اوضاعشان خیلی خوب نیست.
اما اقتصاد ایران خرد شده و پایه صنعتی دفاعی‌شان چنان به‌شدت آسیب دیده که بازسازی آن سال‌های زیادی طول خواهد کشید. سال‌های بسیار زیاد. حالا ما داریم تلاش می‌کنیم به توافقی برسیم که منصفانه باشد.
یادتان باشد، ما مجبور شدیم این مسیر انحرافی را برویم. مجبور شدیم سراغ ایران برویم. نمی‌شود اجازه داد آنها خاورمیانه و ما را منفجر کنند؛ اگر چنین چیزی ممکن باشد. ما زودتر به آنجا می‌رسیدیم، اما آنها اسرائیل را منفجر می‌کردند، کل خاورمیانه را منفجر می‌کردند. اگر می‌خواهید اقتصاد بد ببینید، آن اقتصاد بد است.
یادتان باشد، نفت ما، در میانه این درگیری، از دوران جو خواب‌آلود بایدن هم ارزان‌تر بود. و ما داریم یک آتش را خاموش می‌کنیم. بایدن، کلینتون، بوش، همه‌شان، باراک حسین اوباما ـ اسمش را شنیده‌اید؟ اسم باراک حسین اوباما را شنیده‌اید؟ ـ هیچ‌کدامشان کاری نکردند.
اوباما به آنها ۱.۷ میلیارد دلار پول نقد سبز داد، یادتان هست؟ با یک ۷۴۷. آنها انبوهی از پول نقد را با هواپیما بردند. ۱.۷ میلیارد دلار. صدها میلیارد دلار به آنها دادند و فکر کردند می‌توانند با رشوه آنها را به صلح بکشانند.
تنها چیزی که آنها می‌فهمند همان چیزی است که این آقایان ردیف جلو می‌فهمند: چکش. چون اگر نگاه کنید به کاری که آنها کردند ـ به کاری که ما با ظرفیت هسته‌ای‌شان با آن بمب‌افکن‌های B-2 کردیم ـ آن یک چکش بود. در واقع اسمش را هم گذاشتیم چکش. عملیات چکش.
دمبوکرات‌ها به نفع داشتن سلاح هسته‌ای توسط ایران رأی دادند. و علیه بودجه نظامی رأی دادند. اما من آن را دور زدم.
ایران، ما آنها را از پا درآوردیم. در یک هفته، اساساً از نظر نظامی تمام شده بود. کشوری بسیار بزرگ‌تر، و با ایدئولوژی‌ای بسیار متفاوت. ایدئولوژی مسلمانان کمی با ایدئولوژی کاتولیک‌ها فرق دارد. ما کاتولیک‌ها و مسلمانان را داریم؛ کمی متفاوت‌اند.
... ونزوئلا عالی بوده و ایران هم عالی بوده/خواهد بود، اگر عاقل باشند. وگرنه مجبور می‌شویم کار را تمام کنیم، که کمتر از یک هفته طول خواهد کشید. اما فکر می‌کنم آنها مشکلی نخواهند داشت. آنها کاری را که باید انجام دهند انجام خواهند داد، چون ما باید این کار را تمام‌شده ببینیم.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76635" target="_blank">📅 00:17 · 03 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76634">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=WTWHymtWCHS3WTiHyuMBSlXke-Af9EFzA2IZSyOhtb_POkwmJgz1Z8Y8Uc8k0ZHJ0Hk964-7ghHt3MTlUjUNEQtN6euA539NVr-G73RlGpZrSvQSmXuqcRU_8VK2yf2Cf3Y-cs_53RT7lRKHlSM-IVjDaLyYrMxOAdKVdVrAyIXKPHd1prcwN_6yWsMCBUQ9j0Hyfmw_OGVUGSmVOlOWnkDT39iBggorCHAB6gm_cxXoC_tOt6zBVQ8skGyP1tnCudqwY1T8yOTTSdDSptZqtSkNO722QNUB1Kj64RdFMkl5GU7aaioOeysFsZ13-LC3m_FlZo5cGw3mznQLC6zutw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0dd24797f5.mp4?token=WTWHymtWCHS3WTiHyuMBSlXke-Af9EFzA2IZSyOhtb_POkwmJgz1Z8Y8Uc8k0ZHJ0Hk964-7ghHt3MTlUjUNEQtN6euA539NVr-G73RlGpZrSvQSmXuqcRU_8VK2yf2Cf3Y-cs_53RT7lRKHlSM-IVjDaLyYrMxOAdKVdVrAyIXKPHd1prcwN_6yWsMCBUQ9j0Hyfmw_OGVUGSmVOlOWnkDT39iBggorCHAB6gm_cxXoC_tOt6zBVQ8skGyP1tnCudqwY1T8yOTTSdDSptZqtSkNO722QNUB1Kj64RdFMkl5GU7aaioOeysFsZ13-LC3m_FlZo5cGw3mznQLC6zutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آذر عظیما، خواننده پیشکسوت موسیقی ایران و از نخستین خوانندگان برنامه «گل‌ها»، در ۹۹ سالگی در اصفهان درگذشت.
آذرمیدخت عظیما سراج‌پور که بیشتر با نام آذر عظیما شناخته می‌شد، متولد ۱۳۰۶ در اصفهان بود و فعالیت هنری خود را از سال ۱۳۳۳ با رادیو ایران آغاز کرد.
نخستین اثر او ساخته‌ای از ابوالحسن صبا با شعری از ابوالحسن ورزی بود. او همچنین از نخستین هنرمندانی بود که در مجموعه برنامه‌های ماندگار «گل‌ها» حضور یافت و نخستین برنامه «یک شاخه گل» را با همراهی ویولن ابوالحسن صبا و سنتور فرامرز پایور اجرا کرد.
آذر عظیما در طول فعالیت هنری خود آثار متعددی را در برنامه‌های «گلهای صحرایی» و دیگر برنامه‌های رادیویی اجرا کرد. قطعه «راه شیراز» از شناخته‌شده‌ترین آثار اوست که با ارکستر فارابی به رهبری همسرش، زنده‌یاد مرتضی حنانه، آهنگساز و رهبر ارکستر، اجرا شد.
از آذر عظیما به عنوان نخستین بانوی آوازخوان اصفهان نیز یاد می‌شود. او روز دوم تیر ۱۴۰۵ در ۹۹ سالگی درگذشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 331K · <a href="https://t.me/VahidOnline/76634" target="_blank">📅 23:20 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76633">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=cv3GDyE3nou1uq0ozyL_YFO4ggZoRaniaL2cgCsUxTv40hKccQicHqz3mbRmtsb_z2UgnnLtwXlHfIRLHKuBJ1zGdUXDARerMDgIMqYbek6arFEzfM3O_5BBksdMX-DVc3PShplPskUlNSsD0YlrsxWf3KRi1mLbgYXhwaf5lDX3gx8mkZyhnqJ77DOLzl4EINwph3ZOmpgu-hZ_1ZLR6D8rX_96mo_7cqeNT2vwUQnLVdq5u4lKwxCHPrP_JGFYIBRdPgSTsFnd0MFc-ukK3G3A4SjSIvWtDDqK3PV9Y2D3JizkVWMnFGP5jiUrU5LzjZU94wk5Cy8ZThl2KP2NHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0a9fb0eac9.mp4?token=cv3GDyE3nou1uq0ozyL_YFO4ggZoRaniaL2cgCsUxTv40hKccQicHqz3mbRmtsb_z2UgnnLtwXlHfIRLHKuBJ1zGdUXDARerMDgIMqYbek6arFEzfM3O_5BBksdMX-DVc3PShplPskUlNSsD0YlrsxWf3KRi1mLbgYXhwaf5lDX3gx8mkZyhnqJ77DOLzl4EINwph3ZOmpgu-hZ_1ZLR6D8rX_96mo_7cqeNT2vwUQnLVdq5u4lKwxCHPrP_JGFYIBRdPgSTsFnd0MFc-ukK3G3A4SjSIvWtDDqK3PV9Y2D3JizkVWMnFGP5jiUrU5LzjZU94wk5Cy8ZThl2KP2NHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی بالا رو منابع دولتی با این شرح منتشر کردند:
"تشریح جزئیات اقتصادی تفاهم‌نامه ایران و آمریکا از زبان رئیس‌کل بانک مرکزی"
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 286K · <a href="https://t.me/VahidOnline/76633" target="_blank">📅 23:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76632">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TafqYZsluKJiN1mwuKyneX8sgeOBe6um41QY5qoM0WtGTBusxS5ro1vdTPynsOpUVLriBgNQyaiEW8x9oAncZPDigaeA2W2IJUTGoktBNpiJhs--dCez-k3vhcsi-78Tdx4x0TlTxflweD2hv4LAy_X5EIn9tXVS1M2sc5uihVoUDGxBcv1vEtW4OhZnoGfiVCht345C9KZO_zQwK3Iqgk7wp6EPpGKeOX2eDZqgDSb3MQdGJhAGuAIMAN3HDnu7naKe3Uvo-ZZnWX-hEWY3o4ZPY2TZSo-YekwQmOwQbGQoFm-6u-OkT2XBld1yQ7PbWhtaw6Wq3avnpeD4THKwSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مارکو روبیو، وزیر امور خارجه ایالات متحده، در حضور خبرنگاران در ابوظبی گفت که جمهوری اسلامی ایران به دلایل سیاسی و داخلی خود، موافقت با بازرسی‌های هسته‌ای آژانس بین‌المللی انرژی اتمی در نشست سوئیس را تکذیب می‌کند.
روبیو گفت:
ما می‌دانیم آن‌ها با چه مواردی موافقت کرده‌اند. من نمی‌دانم چرا مجبورند این حرف‌ها را بزنند. سیاست داخلی یا مسائل درون‌مرزی آن‌ها هرچه که هست، خودشان باید با آن کنار بیایند. اما ما می‌دانیم متعهد به انجام چه کارهایی شده‌اند؛ حالا یا آن را انجام می‌دهند یا خیر.
وزیر خارجه آمریکا در پایان تاکید کرد: «اگر آن‌ها به تعهدات خود عمل کنند، فرآیند رو به جلو حرکت خواهد کرد، اما اگر از انجام آن سر باز زنند، رئیس‌جمهوری (ترامپ) باید تصمیمات جدیدی اتخاذ کند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 281K · <a href="https://t.me/VahidOnline/76632" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76631">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=riqemdySH7HelB06MpW-YgzxdoNEdVKLuHinyQdmqOKUShPEWu-Ya9jVFsHDuGrmCji3kTmx-aJDpzt3W30zO56VmAhqU-mDShdxWYDBC5qW3ZD-r8aiuzTkJk9ja6h13PZ9D7tCTgVH0ioB21z3jd0lrRqiZDs2A8b1jDLtmw5gdH6pe1qjKLIr2GsJLqzydkNaEpDVh73k936Txkj1fr3zJ5uQTAEGD0A-wx-Pz6yjbHCiH3dskQqOiqlS7HKzRXNLlD8Mlx1bElH5steHF3wxBoCBkHU9rsFFxR-7vzGPnuQ6YNeCmtpCgrc-CGOW8SbxBoN27jhu03uMtBD2YQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d3ee248638.mp4?token=riqemdySH7HelB06MpW-YgzxdoNEdVKLuHinyQdmqOKUShPEWu-Ya9jVFsHDuGrmCji3kTmx-aJDpzt3W30zO56VmAhqU-mDShdxWYDBC5qW3ZD-r8aiuzTkJk9ja6h13PZ9D7tCTgVH0ioB21z3jd0lrRqiZDs2A8b1jDLtmw5gdH6pe1qjKLIr2GsJLqzydkNaEpDVh73k936Txkj1fr3zJ5uQTAEGD0A-wx-Pz6yjbHCiH3dskQqOiqlS7HKzRXNLlD8Mlx1bElH5steHF3wxBoCBkHU9rsFFxR-7vzGPnuQ6YNeCmtpCgrc-CGOW8SbxBoN27jhu03uMtBD2YQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترجمه ماشین:
خبرنگار:
آقای رئیس‌جمهور، وزارت جنگ برای جنگ ایران ۸۰ میلیارد دلار درخواست کرده است. فکر می‌کنید آمریکایی‌ها در شرایطی که بسیاری از نظر مالی تحت فشارند، از این حمایت می‌کنند؟
...
آنها فقط از این حمایت نمی‌کنند، بلکه آن را مطالبه می‌کنند، چون اجازه نخواهند داد ایران سلاح هسته‌ای داشته باشد.
می‌خواهید دردسر ببینید؟ بگذارید آنها سلاح هسته‌ای داشته باشند.
ما در قبال ایران خیلی خوب پیش می‌رویم. آنها نابود شده‌اند و ما داریم با آنها توافق می‌کنیم. باید ببینیم همه‌چیز چطور پیش می‌رود.
همین حالا، همان‌طور که احتمالاً دیروز شنیدید، ۱۹ میلیون بشکه نفت عبور کرد. این بزرگ‌ترین رقم در تاریخ تنگه است؛ تنگه هرمز.
بازار سهام ما به‌شدت بالا رفته و قیمت نفت در حال سقوط است. امروز برای لحظه‌ای به ۷۰ دلار برای هر بشکه رسیدیم ــ در واقع فکر می‌کنم از آن هم پایین‌تر خواهد رفت. این پایین‌تر از زمانی است که شروع کردیم.
و واقعاً شگفت‌انگیز بوده است. نکته اصلی این است که ایران سلاح هسته‌ای نخواهد داشت.
خبرنگار:
ایران؛ ایرانی‌ها می‌گویند هیچ سفر برنامه‌ریزی‌شده‌ای برای بازرسان آژانس بین‌المللی انرژی اتمی وجود ندارد. آیا این بخشی از توافق شماست؟
ترامپ:
اشتباه می‌کنند. خودشان می‌دانند اشتباه می‌کنند. به ما در داخل گفتند که این را قطعی کرده‌ایم: بازرسی صددرصدی.
و اگر حق با آنها بود، همین حالا جلسات را لغو می‌کردم.
خبرنگار:
و ایران می‌گوید درباره آن توافقی وجود ندارد. از نگاه شما، آقای رئیس‌جمهور، آن بازرسان واقعاً چه زمانی روی زمین خواهند بود؟
ترامپ:
در زمان مناسب. عجله‌ای نیست، اما در زمان مناسب روی زمین خواهند بود.
خبرنگار:
آقای رئیس‌جمهور، به متحدان خودتان که از توافق با ایران انتقاد کرده‌اند چه می‌گویید؟
ترامپ:
خب، فکر می‌کنم هر کسی که از آن انتقاد کرده، در موضع بدی قرار دارد؛ حتی اگر از دوستان ما باشد.
چون ما ایران را در موقعیتی قرار داده‌ایم که هیچ‌کس تا حالا قرار نداده بود. رؤسای جمهور دیگر باید ۴۷ سال پیش این کار را می‌کردند.
ما ایران را در موقعیتی قرار داده‌ایم که ارتشش کاملاً از بین رفته، رهبری‌اش از بین رفته، رادارش از بین رفته؛ همه‌چیزش از بین رفته است.
آنها موقعیت مذاکره خوبی ندارند.
اما با وجود این، پولی که از ایران خارج می‌کنیم، قرار است به کشاورزان ما برسد تا ذرت، سویا و گندم بگیرند؛ باید پول زیادی باشد.
چون آنها مشکل گرسنگی دارند، مشکل غذا دارند، مشکل دارو دارند و مشکلات زیادی دارند. تورم هم دارند. تورمشان همین حالا به ۳۰۰ درصد رسیده است.
بنابراین مشکلات زیادی دارند.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 257K · <a href="https://t.me/VahidOnline/76631" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76630">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MUjxsAdDybT0meN2tVwiPbuFU2xOFqh6UrPK_niytLVroO0RRzqYenfNudxuRPP0Gw0H63JXlvE5YXaleEfIgZaFJNMKpljNvPCVfWZJDBdnDpQzvVAani4K6FKvcd2vBlXp41RRA4IFld9MeGuOrRw8voPid_5hf3ADINdryP-aqFVqn7h3z5oVpRRJQO_lCz8wpiaZB-pAF-q5k8O3PCaiML6q_SvL4xKxxXx9p3fH_-iavzbVmL8WLvmbAzSeajaANcIQC9E8Lc5ev_gnhmro5-M4iyuZeIXXVZJMlfX_UeqQ7fziwocZ3ocj2j_8j9a78DiHys9Syew_hBtjSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رافائل گروسی، مدیرکل آژانس بین‌المللی انرژی اتمی، سه‌شنبه به شبکه ان‌اچ‌کی ژاپن گفت بازرسی از تاسیسات هسته‌ای ایران انجام خواهد شد و هرچه زودتر آغاز شود بهتر است.
او افزود اولویت اصلی آژانس، شناسایی و تایید محل نگهداری اورانیوم با غنای بالا است.
گروسی گفت آژانس بین‌المللی انرژی اتمی به‌زودی با مقام‌های جمهوری اسلامی درباره زمان‌بندی و جزییات بازرسی‌ها گفت‌وگو خواهد کرد.
او تاکید کرد آژانس این بازرسی‌ها را به‌طور مستقل انجام می‌دهد و نیازی به نظارت یا کمک دیگران ندارد.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 256K · <a href="https://t.me/VahidOnline/76630" target="_blank">📅 23:03 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76629">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ug_vfX-6uUtA9wgSKAVMIMoPlTxe2A5x0wbGogSGwOD4OGGnIruIr62ZrPzhER2cGaGd6b87ELnd0GcU_DJTDvBp4CBlew31tMGfHn7YabMaI7gPiVbdmEY-PxhVYfAX_6dHdbakU7W-U380TPzd8-UH5CqTKl6ykADS4ZoBAjx5CWOAiE1lqCnfWWabBTJ7AK-gi8ZcTZHTeXQk8f0e3-zbKRCQIwe61LIvGAbJ0P0k87sOXntsA7bZydcQCmd-buj4lTG25_JFyZd_NJk-S6wd_1VVN5EDL1yIm_N0nkzIV8Gj0XdA0vjFo0KhwY6cVt9Z_ZBYqX_AD1e3B0Dvyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وزیر خارجه آمریکا می‌گوید تا زمانی که گروه‌های نیابتی مورد حمایت ایران به حملات موشکی ادامه دهند، دستیابی به صلح پایدار در منطقه غیرممکن است.
مارکو روبیو که به امارات متحده عربی سفر کرده است، روز سه‌شنبه دوم تیرماه افزود این موضوع «در زمان مناسب» مورد رسیدگی قرار خواهد گرفت.
او همچنین تأکید کرد هیچ کشوری حق ندارد بر تنگه هرمز عوارض یا هزینه‌ای تحمیل کند، چرا که این آبراه یک مسیر بین‌المللی است و بر اساس قوانین موجود بین‌المللی حفاظت می‌شود.
تنگهٔ هرمز از زمان آغاز حملات آمریکا و اسرائیل به ایران در ۹ اسفند پارسال، از سوی سپاه پاسداران مسدود شده بود و تنها هفته گذشته پس از توافق اولیه بین تهران و واشینگتن برای پایان دادن به جنگ تا حدودی بازگشایی شد.
وزیر خارجه آمریکا در مورد لبنان که برقراری آتش‌بس در این کشور بخشی از توافق بین تهران و واشینگتن است، گفت که ما قرار است مستقیماً با دولت لبنان به توافق برسیم.
روبیو تصریح کرد که «آینده لبنان را مردم لبنان تعیین می‌کنند و پرونده لبنان از هرگونه توافق با ایران جداست».
@
VahidHeadline
فرماندهی مرکزی ایالات متحده،
سنتکام
، با انتشار تصویری از ناو هواپیمابر «یواس‌اس جورج اچ. دبلیو. بوش»، در شبکه ایکس نوشت که این ناو در
دریای عرب
در حال فعالیت است.
سنتکام افزود دو ناو هواپیمابر آمریکا همچنان در خاورمیانه مستقر هستند و نیروهای آمریکایی حضور خود را حفظ کرده و در حالت آماده‌باش و مراقبت کامل قرار دارند.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 287K · <a href="https://t.me/VahidOnline/76629" target="_blank">📅 19:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76628">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5986282857.mp4?token=BU7o9Z_IUdGMqO8rwhqyy1SUZR8DfgJ0pWLINYnIxial3xRmc1VsFlQctV-c9WEYDylFrGa6iaV7BgZLODJp1cK8PVTFza4rMblbvswwfbERL8_GWKr4FHH18api1B4iryv6oI3R9GBw1bz9nyvrY4_l6JdsDSBxFCPRJ9epB0WBDFNNIpwmHZSulua9sNmK8o4hpRzR-K5rU_AKD6XzLq3G11hTLyuQMksfn1LRImi3EvSUX8InogQGlRj2AB8BWvhTjR-jU3b0TcGrfe98tcdSic9tW6k6IGK6-KTYEu_BaEk6W6O7h4i6PepxtNt82WYmyjfEwkBcywV3v6eCCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5986282857.mp4?token=BU7o9Z_IUdGMqO8rwhqyy1SUZR8DfgJ0pWLINYnIxial3xRmc1VsFlQctV-c9WEYDylFrGa6iaV7BgZLODJp1cK8PVTFza4rMblbvswwfbERL8_GWKr4FHH18api1B4iryv6oI3R9GBw1bz9nyvrY4_l6JdsDSBxFCPRJ9epB0WBDFNNIpwmHZSulua9sNmK8o4hpRzR-K5rU_AKD6XzLq3G11hTLyuQMksfn1LRImi3EvSUX8InogQGlRj2AB8BWvhTjR-jU3b0TcGrfe98tcdSic9tW6k6IGK6-KTYEu_BaEk6W6O7h4i6PepxtNt82WYmyjfEwkBcywV3v6eCCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نخست‌وزیر پاکستان روز سه‌شنبه دوم تیرماه گفت که در مورد موشک‌های بالستیک نباید استاندارد دوگانه‌ای وجود داشته باشد و تأکید کرد ایران همان حقی را برای در اختیار داشتن آن‌ها دارد که سایر کشورها دارند.
شهباز شریف همچنین به خبرنگاران گفت که در تفاهم‌نامه مورد توافق میان ایران و ایالات متحده هیچ اشاره‌ای به موشک‌های بالستیک نشده، زیرا این موضوع اساساً در آن مذاکرات مطرح نبوده است.
پیشتر برخی رسانه‌ها از قول نخست‌وزیر پاکستان مدعی شده بودند که او گفته است موضوع موشک‌های بالستیک تهران از جمله محورهای مذاکره بین ایران و آمریکا است.
در واکنش به این ادعا، خبرگزاری فارس نزدیک به سپاه پاسداران نوشت که اظهارات نخست‌وزیر پاکستان، «کاملاً اشتباه و احتمالا ناشی از بی‌اطلاعی است».
به نوشته این خبرگزاری، پاکستان در حال حاضر نقش چندانی در میانجی‌گری این مذاکرات ندارد و اظهارات شهباز شریف بیشتر برای پررنگ‌نمایی نقش واسطه‌گری این کشور مطرح شده است.
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 282K · <a href="https://t.me/VahidOnline/76628" target="_blank">📅 18:50 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76627">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vfEMlPDC_5s5eLPnoki3YeHxAPi_a0Uo_rqbkf2MntUXImq8ryo-Ifi4g0TEIOyQwOesHu-VMl4s2lVZrqC2eS4qex-7D6wVgYAHs5HOJff0yA-w7y3_IMBISfokwA7rQja8q37m9Zi-RcVgZK4_qQMrtpm7yUzGKtuwPH6Fc4Uo0PxskwX5U03tSMVbPcWAEvdD4GhceGsXasV9OoUbDn457jf_h1D85sR3fHtmcqDjVTT9hhV5g-LsDJ4Cb_xpR-pKzWOLFX28UYw2AbpE695aGqZIPE7PDtnvsyrzQvDaktq35lK-_RY114pOMvrQMyeazyAOct73JbXMxNZhdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ثریا طالبی، مادر امیرحسین موسوی، فعال فضای مجازی مشهور به «جیمز بی‌دین» که از آذرماه ۱۴۰۳ در بازداشت به‌سر می‌برد، می‌گوید پس از پخش گزارش تلویزیونی از فرزندش در جریان جنگ ۱۲ روزه، اتهام «همکاری با دول متخاصم» به پرونده او افزوده شده است. مهر ۱۴۰۴ صداوسیما با پخش ویدئویی از اعترافات اجباری امیرحسین موسوی، او را به «جاسوسی و همکاری اطلاعاتی و امنیتی با اسرائیل» متهم کرد.
پس از آن امیرحسین موسوی که با نام کاربری «جیمز بی‌دین» در شبکه‌های اجتماعی فعالیت می‌کرد، با انتشار نامه‌ای سرگشاده از زندان اوین اعلام کرده که تمام اتهامات مطرح‌شده علیه او «نادرست و تحریف‌شده» است. آقای موسوی نوشته که پس از ۱۴۸ روز انفرادی، بازداشت همسرش و تهدید به تکرار شکنجه‌ها، وادار به انجام مصاحبه‌ای اجباری شده است.
ثریا طالبی، مادر امیرحسین موسوی، در گفت‌وگو با «امتداد» با اشاره به وضعیت پرونده فرزندش گفت که امیرحسین موسوی از ۲۸ آذر ۱۴۰۳ در بازداشت است و خانواده او همچنان در «بلاتکلیفی کامل» به سر می‌برند.
به گفته او، فرزندش هنگام سفر به کیش در فرودگاه مهرآباد بازداشت شد و خانواده تا مدت‌ها از محل نگهداری و نهاد بازداشت‌کننده او اطلاعی نداشتند.
مادر این فعال توییتری همچنین گفت امیرحسین موسوی حدود شش ماه در سلول انفرادی نگهداری شده و پس از انتقال به بند عمومی، از او مصاحبه تصویری گرفته شده است. او مدعی شد به فرزندش گفته بودند این ویدئو صرفاً برای آرشیو ضبط می‌شود و در صورت همکاری، طی چند روز با وثیقه آزاد خواهد شد.
به گفته طالبی، در زمان تشکیل پرونده، اتهام‌های «اجتماع و تبانی علیه امنیت کشور»، «فعالیت تبلیغی علیه نظام» و «توهین به مقدسات» علیه فرزندش مطرح شده بود.
او افزود پس از جنگ ۱۲ روزه و پخش بخشی از این مصاحبه در بخش خبری ۲۰:۳۰ صداوسیما، اتهام «همکاری با دولت متخاصم» نیز به پرونده اضافه شده است.
طالبی با انتقاد از نحوه انتشار این ویدئو گفت: «فیلم به‌صورت تقطیع‌شده پخش شد؛ به شکلی که این تصور ایجاد می‌شد که امیرحسین در زمان جنگ اطلاعاتی را در اختیار دشمن قرار داده است، در حالی که او در همان زمان در زندان بود.»
او همچنین از شکایت خانواده علیه برنامه ۲۰:۳۰ و رسانه‌هایی که این ویدئو را بازنشر کرده‌اند خبر داد و گفت این شکایت در حال رسیدگی است.
مادر امیرحسین موسوی با رد اتهام‌های مطرح‌شده علیه فرزندش تاکید کرد: «انگ وطن‌فروشی به امیرحسین نمی‌چسبد. او یک فعال توییتری بوده و اگر کسی با ادعای ارتباط با اسرائیل برایش پیام فرستاده، بلافاصله آن حساب را مسدود کرده است.»
بر اساس اعلام وکیل پرونده، جلسه رسیدگی به اتهامات امیرحسین موسوی روز ۱۳ تیرماه در شعبه ۱۵ دادگاه انقلاب به ریاست قاضی ابوالقاسم صلواتی برگزار خواهد شد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 255K · <a href="https://t.me/VahidOnline/76627" target="_blank">📅 18:49 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76626">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/WKadB8UQusztdMS3axEXxBNE7kdGK_hAeMjPh-HH_Cy1mQOkkW4RbCl2oUpmPT4hSLpYThzkKTaLmp5gOBNE6piPzupJt-iytfG7elHfQtaYwFbdvvrMR9v3Yo9zwwQrp3kfONZKHsbdXfJpNVAcbQFSxlbdLabZrw31KsD5Dkv-tTnfWZ3vKSCgdKlMBvPBkrGm8i6jZe7MaYVCWRQiQvmr4_IepwoCuJVOTFmiOvakhnmsC4I753awH0LurKO7Qy3sh9aCqt1dZBbVBzY02FOvXfp9or-9Owv4jpSx1e7GaNoECUrLqqGIVslA82kypRxt3sQ-BfblimXOTQF4ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">Gerduo
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 260K · <a href="https://t.me/VahidOnline/76626" target="_blank">📅 18:04 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76622">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/V1JiQtTmK5LdL11pkIUD5YdgAuBgX1uq4X8FmbLC8-BMatF9pb3tauci20T7NCnZ8JTXPJDj423RHBmmU8mTlw81SRZ5Vajo-WpFyBXHaQr0jXGdKfwTLwDUGhVgRJ3jeeIP_TZvgWpXu9P8avKwxhQQ2baPc3Z7LMzS9qgGIkeXqe5oefh721Jy5iRZiZvF_X3OZAU0cH50Gnq9oG07E6WXMrCBUSqaDzcwZCypfz9gmBrG7UgGVFBpXeIWpYvOmt-VgsJI3Uzk7m3f3JzwH3AqYNk-fo0VRAxl62GCv-idB7p6GMg5mfpFlq1dGtOPbC2ZGU7ZkWDQKjt6NQaq1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/X3Y4-2pyKJDiGg1bPlg1eyxR-7BisVqCqyNs7plpY9NpNL5z2CDbWtC3GsLObJjqzB2s8fF6zFgF8bxeXfrHscSiuPg9f-iSDm0ioCU-DNwh1Kajxv3vPcNBxi6I5vnIsKUt7LZBEeSyi51gzH8KXR70AxbNHtL4t4HjNxl_vc9Xj5zvKohnSJJKrDn8FRKT_HAOvzDEi3a_HZPDhnGpnMh1CFBxSesOneT__5sC-e9EOmgyeDcOO8D9uU_CjBwjQ3EpG-abxzljdzNYCTj37cC_5mz8s6yE-HgXGqzCL_VMu3KCzpXOTLtAW9IbRyF6UsX7tvFNpA9huA2OIN6XZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/v2yzKUC32dsbrZJDTmWz8BH8JUGp0la6YLQ3ukOhZl0qQfb-RkjrAHv1BcNFoc7b-t6jaqBt-0MfQInCEu8gdaf90maQG3YtC545oajq6KUTwQ6rBqNlUuV-2AtObAzSBqmRBm9PMdmhRGX-fHxCjKQmxHXmzhb2320YiBF8RX8GuOJ85Mv5OM9x4G0cMJ6kthvTN92b9zMkVXnVQkqk6E9dCvno5bALVn4o6RFsmsoH3zLOKD5S_g0qNKmffg9zjBgBp2fw7x5eGhe88gU93UfPX4uUj4JBBjWFagxSmfwvGfL0bDY1s-bqGq5EAYwKwlmtwzq5wL_9jzg7rQSZbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/K-Y43J2nt3czBQH7pgY1J9kaB8619MHL7hvnPUDMCC7AMqeY55OV5WhBD2kYrNdhH0BlL4Cf0V-VkgpTIsdk9C9nBGaifDSMTvBJZeH5DuEpmN2azNZgaD2znrTvsLyQXUDLcsPlIhshNC0Rn5hVtKYUjdx6pDR46MoG6qlOR6gDBpHxLbNiW7UIY-UcUtrh2hF6i9UmmCEPj18UXaA3YgOL1NTinVaZOxduXub0cJq73AylrdqSiwy5VsFcJUkywYRBQ6SN8PeLG4q6hGJB4ii5T9q3Cprk9hUL0EMQ7-pHfOq_tAGS6C67jR3X4zqf-E1yF5FWWg61vxM1XIOLog.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">گزارش‌های کاربران از بروز اختلال شدید و قطعی در سامانه‌های آنلاین و پایانه‌های فروشگاهی (POS) برخی بانک‌های کشور از جمله بلوبانک، بانک کشاورزی، بانک ملت و بانک رفاه حکایت دارد. این اختلال‌ها موجب شده مشتریان در انجام تراکنش‌های مالی، خریدهای روزمره و استفاده از خدمات غیرحضوری با مشکل جدی مواجه شوند.
@
VahidHeadline
گزارش‌های مختلف کاربران در شبکه‌های اجتماعی حاکی از اختلال گسترده در خدمات بانکی چند بانک بزرگ ایران در روز سه‌شنبه، دوم تیر است.
بر اساس این گزارش‌ها، پرداخت الکترونیک و انتقال وجوه در چند بانک بزرگ مانند ملی، تجارت، صادرات و ملت با اختلال همراه است.
خبرگزاری‌های فارس و تسنیم، نزدیک به سپاه پاسداران با تأیید این اختلال‌ها از احتمال حمله سایبری به مرکز خدمات پشتیبان خبر داده‌اند.
در همین رابطه شرکت خدمات انفورماتیک با انتشار بیانیه‌ای، با تأیید انجام حملات سایبری، گفته است که «شرکت خدمات انفورماتیک به‌منظور پیشگیری از هرگونه دسترسی غیرمجاز و صیانت از امنیت داده‌ها و دارایی‌های مشتریان، در حال حاضر ارائه خدمات مبتنی بر کارت را به صورت موقت از دسترس خارج کرده است.»
این برای دومین بار طی دو هفته گذشته است که خدمات بانکی در ایران دچار احتلال می‌شود.
چندین بانک ایران اواسط خردادماه هم با قطع ارتباط و خدمات روبرو شدند که به گفته مسئولان دولتی به دلیل حملات سایبری به زیر ساخت‌های خدماتی بانک‌ها بود.
تاکنون گزارشی از عامل این حملات سایبری منتشر نشده است.
@
VahidHeadline
آپدیت:
پیام‌های مختلفی دریافت می‌کنم با نظریه‌های توطئه که فکر می‌کنند بازار ارز و طلا و...  قراره نوسان داشته باشند و نمی‌خوان کسی بتونه خرید و فروش کنه و...
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 251K · <a href="https://t.me/VahidOnline/76622" target="_blank">📅 17:35 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76621">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rbbtSbxpUS4q3l_IcS9IFLLRvs8peqBjDpr5rWZ_OmbS1uOVCk34JC2GFryUTv5Q7P3paR4gt0ujZNdJG9aTNhkj2mWCCLxamThPKWbK4vcu_1oEttjqaarXp1eQc06jSzBO7Q9wXCTYkI_33QmZpV8P3oT4uCU97aluGCJhuiUdUgI7bvypTLMa4tPGuUM0c03JQ4YoSIv9Ffa_mo99yROyUIffrVNei_zw9IYdMyhx_yq4wyoyPvJPjdqDWg83Z2uY7h82m15c-TlcsOvid4pBYMaAQmWDB69tabtkmBkD6ec2Fj1Dvn_gqfdKoQkmdUhSUhPv6y6ZUnSQ3iil9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمان و ایران روز سه‌شنبه دوم تیرماه توافق کردند گفت‌وگوها درباره نحوه اداره آینده کشتیرانی در تنگهٔ هرمز، از جمله خدمات دریایی در این آبراه راهبردی و هزینه‌های مرتبط با آن، را ادامه دهند.
به گزارش خبرگزاری رویترز، در بیانیه‌ مشترکی که پس از مذاکرات مسقط منتشر شد، دو کشور اعلام کردند یک کارگروه مشترک با مشارکت وزارتخانه‌های خارجه تشکیل خواهد شد تا این گفت‌وگوها را پیگیری کند و همچنین با دیگر کشورهای ساحلی و طرف‌های مرتبط رایزنی خواهند کرد.
این اقدام به نظر می‌رسد اجرای بندی از تفاهم‌نامه‌ای باشد که هفته گذشته بین ایران و آمریکا امضا شد و بر اساس آن، ایران موظف است با عمان و دیگر کشورهای ساحلی خلیج فارس درباره مدیریت آینده کشتیرانی و خدمات دریایی در این تنگه، که مسیر حیاتی برای انتقال نفت جهان است، گفت‌وگو کند.
این توافق پس از سفر محمدباقر قالیباف، رئیس مجلس شورای اسلامی، و عباس عراقچی، وزیر خارجه ایران، به عمان اعلام شد. این دو مقام ایرانی با سلطان هیثم بن طارق، پادشاه عمان، دیدار کردند و با وزیر خارجه این کشور، سید بدر البوسعیدی، نیز گفت‌وگو داشتند.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 229K · <a href="https://t.me/VahidOnline/76621" target="_blank">📅 17:29 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76619">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/A2oixhyHDzcYyfUxYeYm3vsf00EjQN9OR2K7Nee_s517acbkCzlpTVxDjRxDXZ4i14xwQnsKj21wzvVj23AJU-gcJQR5xJiyOJdj_jiehNpdW9nq4piHRn_8FkhMvjXEv-fZ7gmTTdgfcyKtcem4Wfx64cig3YvnPetIALNHRUkITkCVTlIWjBO-Xme23x_uM82CSNyD91KeHJgY3nFnEqYErhx_EN-xXyN1X8_j2elLbAF_F8GCmn9I6xOHE9DDxs7SuKse8aB1rGYFzlf0yfyj2eyPCLuAgR4X3a8Ct5O5rJlBLu4DnALiBcFyZovp0OPTK3bR6D9yvxkYpvZ8Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=pn5CBtyK_SfGF7cVkULCaBA26z6GWU_iRPzIJLf5LXwtVuz7kNVdpfytVaUGyPpQnPhH7RSwmDdNh00hJR7S6OXp--Hqij8Ds7GkOoEU077fdIP2mZuWMLNb4ZsxvcinwHapzhFoZsQ5nfwBdjQE7_GU5qsAHPlB6P66S7UTs0tC3P9Vwmz-dF14iz_9zfG1VLUNrSE8KlY5O28MgpuRP4tN73qdoEFznn2ZwZ8Jmf5YRnTfkAZWzdRu3rgJ3w2D5YLW0avyipVUlpWoWzsYCgyTz3Ax9YUH3xKvmv8D6W6rL6ppITDt0lNJo4cv7ETxUk4dp8n0HgH4IQuK0Rxu_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/31a8d92068.mp4?token=pn5CBtyK_SfGF7cVkULCaBA26z6GWU_iRPzIJLf5LXwtVuz7kNVdpfytVaUGyPpQnPhH7RSwmDdNh00hJR7S6OXp--Hqij8Ds7GkOoEU077fdIP2mZuWMLNb4ZsxvcinwHapzhFoZsQ5nfwBdjQE7_GU5qsAHPlB6P66S7UTs0tC3P9Vwmz-dF14iz_9zfG1VLUNrSE8KlY5O28MgpuRP4tN73qdoEFznn2ZwZ8Jmf5YRnTfkAZWzdRu3rgJ3w2D5YLW0avyipVUlpWoWzsYCgyTz3Ax9YUH3xKvmv8D6W6rL6ppITDt0lNJo4cv7ETxUk4dp8n0HgH4IQuK0Rxu_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کامران غضنفری، نماینده مجلس شورای اسلامی، در شبکه اجتماعی ایکس از برنامه شماری از نمایندگان برای «تحصن» مقابل ساختمان این نهاد در اعتراض به ادامه تعطیلی آن خبر داد.
او نوشت که «چنان‌چه مجلس بسته باشد، تا باز شدن مجلس، در همان‌جا تحصن خواهیم کرد.»
شماری از نمایندگان مجلس به تعطیلی این نهاد طی ماه‌های بعد از حملات اسرائیل و آمریکا به ایران در نهم اسفند ۱۴۰۴، اعتراض دارند.
حمید رسایی، یکی دیگر از نمایندگان مجلس شورای اسلامی، یکشنبه ۳۱ خرداد با انتقاد از ادامه تعطیلی مجلس گفته بود در صورت ادامه تعطیلی، همراه برخی نمایندگان مقابل ساختمان مجلس جلسه برگزار خواهد کرد.
حسین صمصامی، دیگر نماینده مجلس شورای اسلامی، نیز در پیامی جداگانه در شبکه ایکس، نسبت به ادامه تعطیلی صحن علنی اعتراض کرده و نوشته است: «بیش از ۱۰۰ روز از تعطیلی صحن مجلس می‌گذرد و نکتۀ تاسف‌بار آن است که در سامانه قانونگذاری، امکان ثبت استیضاح وزیر و صدور بیانیه مسدود شده است.»
انتقادها در این زمینه به خصوص از سوی نمایندگان نزدیک به جبهه پایداری با پررنگ‌شدن نقش محمدباقر قالیباف در مذاکرات با آمریکا، افزایش یافته است.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 210K · <a href="https://t.me/VahidOnline/76619" target="_blank">📅 17:28 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76618">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lizUdzWU38FeR3rNy9xa2lAN7jR2h1eCdCgpQMrYBGqX-O7G918iHjSLouVSTkbPmfALLUVI8yO11CfTYmZIYFN511ihm28A89TbDPWBfbjxzSgchLG6DPJvOsXvj4dOsB6BWGlX7UwQdP2eAlNBujV7xcqjOi3vW5tOz-o5cj7iWH-IOemGfl4Rztmmkx0KkicXmPo7LEoytJfEcuBCoTEmmud2SSYFARfjm4fzjRf0x9-J3dHbkfkjsaTfUr9WUzLpNO0LiWW87SBYghy_ufJx2w_BHZcGf1JBBcQmn_ERVsD55uRMPPTpxJXkicW166xNSogZrE3ISgThhjUAFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کانون فیلمسازان مستقل ایران، ایفما، در بیانیه‌ای نسبت به احتمال اعدام علی صفری، بازیگر تئاتر و دانشجوی دانشگاه فرهنگ و هنر هشدار داد.
این کانون با ابراز نگرانی از طرح اتهام «محاربه» علیه او، از مراکز سینمایی و نهادهای بین‌المللی خواست تا برای نجات این هنرمند و سایر هنرمندان در بند، «فشارها بر رژیم ایران و قوه قضائیه آن را بیشتر کنند».
به نوشته این نهاد، علی صفری، بازیگر جوان و ۲۳ ساله تئاتر و دانشجوی دانشگاه فرهنگ و هنر در جریان اعتراضات سراسری ایران در تاریخ ۱۸ دی ماه ۱۴۰۴در شهر کرج بازداشت شد و «تاکنون اطلاعات روشنی درباره‌ی روند پرونده‌ و وضعیت این بازیگر منتشر نشده است، اما اتهام «محاربه» در تاریخ ۹ بهمن ۱۴۰۴ به طور رسمی به او تفهیم شد.»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 223K · <a href="https://t.me/VahidOnline/76618" target="_blank">📅 17:26 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76616">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GLcw790QJrKWF3owOjnYnRw4wn1nnTFGGq-GzkCJNCwO43PoLKgBKg0wX9TcQ2CcQn0EU26rr7mxyzbxVPN_s8ePZJxGTTf_Odq5jPx3NNYKcfxaWgLxrubM6_rPXtOdMGRzAZsHFqiXv0_a55gM6bzLfaHyBv-cFbo9yGzbjqINQQGQUK3yz8Beum4lR4DhjAYrPZVKaAxZRBe3mzShnLrd9Q7MiU87B0Na_bKNQ3FWRFNRJ8aVUhzPncEDgVofyZxzfTRHY8z2gsl1spMeFrU4Q_u_fXWt-aea-gma8P6ca0B3KyMgVX75MvIbHJ5IQhpMIYzbDJ2NFvpbDl_RZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Mbu4egGvpJO_GWVvQXuRLPChtLSJ3s1yy5F_ZlZE1czld1dFh42YrDP8XysWDf2bwx8GYJ7f_iEBCNVQEJoGdKzvz9B3_QFEk8nWAEje_Qr_Qqpdc0mEFXYvbeb1n-u6L_lX849sq5PnhS2lTjghtM4UTIFuxRJx7mi7Teaq5rAUPh_pwGYEX-mjESJVYKGOzx6qXl-AJwrRoyO4vMAGZPktvVWE7B8lMvbgtVwx-tNMBsRoRtSz4TfK5Oye2mi3Vk22aqcbijH0DWtulyyOwT-T5SzlAa9msUqj3QYKmmA2Lqc0jaMMZKOy904DYkJT1Z2Ktc_Ust58NLRh-rlpXw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/11113460cd.mp4?token=Mbu4egGvpJO_GWVvQXuRLPChtLSJ3s1yy5F_ZlZE1czld1dFh42YrDP8XysWDf2bwx8GYJ7f_iEBCNVQEJoGdKzvz9B3_QFEk8nWAEje_Qr_Qqpdc0mEFXYvbeb1n-u6L_lX849sq5PnhS2lTjghtM4UTIFuxRJx7mi7Teaq5rAUPh_pwGYEX-mjESJVYKGOzx6qXl-AJwrRoyO4vMAGZPktvVWE7B8lMvbgtVwx-tNMBsRoRtSz4TfK5Oye2mi3Vk22aqcbijH0DWtulyyOwT-T5SzlAa9msUqj3QYKmmA2Lqc0jaMMZKOy904DYkJT1Z2Ktc_Ust58NLRh-rlpXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس‌جمهور ایالات متحده روز سه‌شنبه دوم تیرماه بار دیگر تکرار کرد که ایران با بالاترین سطح بازرسی‌های هسته‌ای از تأسیسات خود موافقت کرده و این بازرسی‌ها «تا ابد» است.
دونالد ترامپ در پستی در شبکهٔ اجتماعی خود، تروث سوشال، نوشت که با وجود اعتراض‌ها و «ادعاهای نادرست» ایران، و «هم‌زمان با جار و جنجال رسانه‌های جعلی که هر کاری می‌کنند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهند»، ایران «به‌طور کامل و تمام‌عیار با بالاترین سطح بازرسی‌های هسته‌ای برای مدت طولانی در آینده (تا ابد!!!) موافقت کرده است».
به گفتهٔ او، این امر «صداقت هسته‌ای» را تضمین خواهد کرد. «اگر با این موضوع موافقت نمی‌کردند، دیگر هیچ مذاکره‌ای ادامه پیدا نمی‌کرد!»
نخستین بار، جی‌دی ونس معاون رئیس‌جمهور آمریکا بود که روز اول تیرماه خبر داد ایران با بازرسی از تأسیسات هسته‌ایش موافقت کرده و این امر ممکن است در هفته جاری رخ دهد.
با این حال، مقام‌های جمهوری اسلامی بویژه سخنگوی وزارت خارجه ایران هرگونه بازرسی آژانس از تأسیسات هسته‌ای را رد کرده‌اند.
@
VahidHeadline
پست‌های ترامپ، ترجمه ماشین:
با وجود اعتراض‌ها و اظهارات دروغین آن‌ها در خلاف این موضوع، همراه با هیاهوی مداوم اخبار جعلی، که هر کاری می‌کند تا پیروزی آمریکا را تا حد ممکن کوچک و بی‌اهمیت جلوه دهد، ایران به‌طور کامل و تمام‌وکمال با بالاترین سطح بازرسی‌های هسته‌ای برای مدت بسیار طولانی در آینده، یعنی تا ابد، موافقت کرده است!!!
این کار «صداقت هسته‌ای» را تضمین خواهد کرد. اگر آن‌ها با این موضوع موافقت نکرده بودند، هیچ مذاکره بیشتری در کار نبود!
بر اساس این موضوع و سایر امتیازهای بزرگی که ایران در حال دادن آن‌هاست، من موافقت کرده‌ام اجازه بدهم تنگه هرمز باز بماند، بدون هیچ محاصره دریاییِ دیگری. با این حال، همه کشتی‌ها در جای خود باقی می‌مانند تا اگر لازم شد، محاصره دوباره برقرار شود؛ چیزی که در حال حاضر بسیار بعید به نظر می‌رسد.
پول و/یا تحریم‌هایی که وزارت خزانه‌داری آمریکا آزاد می‌کند، به حساب امانی منتقل می‌شود که تحت کنترل ایالات متحده آمریکاست و صرفاً برای خرید غذا و تجهیزات پزشکی از ایالات متحده استفاده خواهد شد، از جمله ذرت، گندم و سویا از کشاورزان بزرگ آمریکایی ما.
این‌ها چیزهایی هستند که ایران به‌شدت به آن‌ها نیاز دارد. این یک بحران انسانی است و من احساس می‌کنم لازم است همین حالا، پیش از آنکه خیلی دیر شود، کمک کنیم.
گفت‌وگوها به‌خوبی پیش می‌رود!
از توجه شما به این موضوع سپاسگزارم.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
دیروز ۱۹ میلیون بشکه نفت از تنگه هرمز عبور کرد؛ رکوردی بی‌سابقه در تمام دوران. قیمت نفت به‌شدت در حال سقوط است و جهان جای بسیار امن‌تری شده است!!!
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 217K · <a href="https://t.me/VahidOnline/76616" target="_blank">📅 17:22 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76615">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/XHamkv1gcBlSzj2VTQOri_cBpPQ2cLQD7pMklABpON3UYnlZbVZqpIUhN0XThawK688ZAcoPAL0e5OGQN_pXzbY_MhoQazDPwzugxt3DbGmoAzI8xcRGAvEZnpThFlpYOoooM_E8Clof3xTRdvY3UTc5vILMwl9xxGOV7ecSkC1lTeY7AmnjgmKyE24P22PqNls7-LxeVG9z1v1ATDnVV3-KVmlCzEjtXUpfrrNh7KZOJ_FJb-t9qSgHPgP3e1Ib4yBSAiooHmXlDwECNBp-iobdOpjBXI2Ia2R1aELSMlNTDqJBc8XSzbQ_4racWisEdoGx6LndyUUmsc9UFc3T_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری مهر سه‌شنبه دوم تیرماه گزارش داد قیمت  [نان یارانه‌ای، نان یارانه‌دار] در تهران و ورامین افزایش یافته و در برخی موارد به حدود دو برابر نرخ‌های پیشین رسیده است.
بر اساس این گزارش، قیمت‌های جدید از سوی استانداری ابلاغ شده و از امروز روی دستگاه‌های نانینو در نانوایی‌ها اعمال شده است.
بر اساس نرخ‌های تازه، قیمت نان لواش به دو هزار و ۷۰۰ تومان، بربری به ۱۰ هزار تومان و سنگک به ۱۵ هزار و ۵۰۰ تومان رسیده است.
محمدجواد کرمی، رئیس کارگروه آرد و نان اتاق اصناف ایران، نیز افزایش قیمت نان را تایید کرده است.
در ورامین نیز رئیس اتحادیه نانوایان از افزایش ۹۰ تا ۱۰۰ درصدی قیمت نان خبر داد.
بر این اساس، قیمت نان لواش از هزار و ۴۰۰ تومان به دو هزار و ۷۰۰ تومان، تافتون از دو هزار و ۳۰۰ تومان به چهار هزار و ۵۰۰ تومان، بربری از پنج هزار و ۳۰۰ تومان به ۱۰ هزار تومان و سنگک از هفت هزار و ۴۰۰ تومان به ۱۵ هزار و ۵۰۰ تومان افزایش یافته است.
مسئولان صنفی افزایش هزینه‌های تولید، از جمله دستمزد کارگران، خمیرمایه، حمل‌ونقل و اجاره‌بها را دلیل این افزایش قیمت عنوان کرده‌اند.
رئیس اتحادیه نانوایان ورامین نیز گفته است اصلاح قیمت‌ها با هدف ادامه فعالیت نانوایی‌ها و حفظ روند تولید و عرضه نان انجام شده است.
این افزایش قیمت در حالی اعمال شده است که نان از مهم‌ترین کالاهای مصرفی خانوارهای ایرانی محسوب می‌شود و در برخی اقلام، نرخ‌های جدید نسبت به قیمت‌های قبلی نزدیک به دو برابر شده است.
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 261K · <a href="https://t.me/VahidOnline/76615" target="_blank">📅 17:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76611">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/uSBV9geIefOO-oqzXrHBFbMdQlrM565R9WoS3CLYOOly7U5Ybfg9vBFqCmZUtL4piVTRka5eGC2WL7ThAvvE34G6JpKHvbQUeWdjBD4vubXD2Xqp21BIQYGZWktL_IF6ElFod4UoKiMJv1lRzFHA_USuLNpO35fQUJ7puibYghU5bpbPQjGLCfDi8m99dpwapj2EIfimQQ4NCcNnvx59XHok3MY4kG0ZzSCrvCFnTggYu48oGgwXZHAPWVI5NTOYpbi_inbYEmZeXqPIaXG8r2b2n2Tp4aIfiMbQKJrdEZVW1no6lNgsPtjZn2ARg5pxAglu7Ev4Ja4PCDoT4YCUeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h61QRzaMyNk9AMFXiI_iqfTPsesf1P0i4SBieIu-tjjWpfVb0eniDB_N6DvgdNq1urnPqN4NPgqohgmFH5MF78FNRrlJsz6OYzS56sDmwiDbMrMAqcaZMeJLcKWiLLYq2HRFVSP9Mf8AG34EVUfduUHeBwBwx9HgWfxez2Nf2zwSUQIVZh0BTFk5nCfZCX3A1zsC8NQZqsXJx_F6U0PwFOVzCkHPOwpuVGo_OaDiMa_TKBnc0CtsybOyrb0H6UUJ-aIjEN1PzPBemDE92eyflocbOGT5yzOYQE7576XcQS3iwjOetWRauWoqXFO74lZ2b2QphcdkwqVdVQ7Xz1YiEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/AaWVWGNaXASNbm_dxfhTMAkG6icv4acw9uZWMWK-JBWv2C4ujv1S71W3uJPbSSKMsdtEjP61t0rDXIwXnztqkV-8WqtUvcRSTGDCxk8wgleKYd9Ji2z-waTse838A00YpQBBiplKnT6rcyY2Goov1uvWEdhL0cKx-_sjqKk-x_UY_tVdLJ2dFmSIuooBqrEE310n_Ctwfn_5KOtzTdboMHfYY7UQ9Y00ir-43NkQs3-USsSUy7j22KMJF4ZJmREmX3qN0HSBF3jB3Dpgm1ZLCs2IkMy525iZd3SMEFwegKN6QY82pTV5jFmDp9I9IYYxOK3FlSviqc8XvbqGbXKJBA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=P2gt54NAGwj6joPR5Mo37PxtnosfKSdGUQP1tnu88zLonL9W2d_qx98IMqBuKaePcq1ruA2JZMsMSQkvznZP1I-qPfspcIWjoU5meAEz-jiRNKj1s4svaxsN_kBUBUwO8I58OgMgyzPQSTCpyBulMOGPe2miSxbIs_GoXGCoTr9U6s2kOnEsQKhMwQXl1ktE5alu4qOE06Cm5hf_LVlntWc9kGn6TuTtYd1GMzx_0iH9FqSashvc64kT67MBrjfMp6gRTxLidC4Ths62-7sm1IndzBSfa4EkVpOR5oL9tN38kzk8r72gubDehVCuEoYEti8l6-URVV8as2x0tSFuYw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/4b0b4e3582.mp4?token=P2gt54NAGwj6joPR5Mo37PxtnosfKSdGUQP1tnu88zLonL9W2d_qx98IMqBuKaePcq1ruA2JZMsMSQkvznZP1I-qPfspcIWjoU5meAEz-jiRNKj1s4svaxsN_kBUBUwO8I58OgMgyzPQSTCpyBulMOGPe2miSxbIs_GoXGCoTr9U6s2kOnEsQKhMwQXl1ktE5alu4qOE06Cm5hf_LVlntWc9kGn6TuTtYd1GMzx_0iH9FqSashvc64kT67MBrjfMp6gRTxLidC4Ths62-7sm1IndzBSfa4EkVpOR5oL9tN38kzk8r72gubDehVCuEoYEti8l6-URVV8as2x0tSFuYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«امیرمحمد هموله» ۲۴ ساله، ساکن شهرک صدف شهریار، روز پنج‌شنبه ۱۸ دی‌ماه ۱۴۰۴ بر اثر اصابت گلوله به ناحیه سر به شدت مجروح شد.
او پس از تیراندازی به بیمارستان نور شهریار منتقل شد و حدود ۵۰ روز در کما تحت درمان بود، اما سرانجام در روز هشتم اسفندماه ۱۴۰۴ بر اثر شدت جراحات جان خود را از دست داد.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 307K · <a href="https://t.me/VahidOnline/76611" target="_blank">📅 17:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76603">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pxoKWME3aokDvB9fgemKTPetVt281JyYU4UoakPEjyS-rAh34Rd_tq-JEcWoHdlQDtrv_0A_6ZbIivtDSt9LHN5eNMA5jMgSIOetQ8ZP2aV3eusAwAsw2WUuyztlFNq0mlO_fcPt7YlLpvambjNH9_llTO8Z0HBiWS_7UtthC5tAMaB-cu8fO4VD8V-tSwcL4Ib0BaZ0z49PDeft8mv_8C5icTqtQJ_k7OmizY8uqO4mrHKkSZHe4fnqI_r20YvGRm3LgSrhs4JmFett5kDDvr8tf8DObs0q3BVeNC0VaPvznvOzYesfmUY74rJz5Wsmsu10qEsfVMP2licbnTqsJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/Y7p-NNSBxCf4MMn9MBivB8SyV7qTrMMjEW6fFrtJPeRMBwXDeWbstc70eUCw-3rrMx6A6E_Vx0BoQnWslqckhmManXfOEL7ZMrIo2_o4LnZGq6zt_uE9bITaUDfyd5Fq2OneUyShQg0jvMD8pEsoUXOpKTl0ttnbHeJ7RwL5CJjiCr_0_zEwL0c0uehJZPXqxtf6fMhkcXqeCquRrOePmbDZtJ533BjUCjh9a0ykh75j6qQxf161vNEZaN-dhLR2-4L4Oo_64GUA6gBgziy4tME2nGh1Rl0EeuBAvCgN7Br1af77x6CaIGQ5ad63U8pRsof8u75wM36CRY0vU8fxzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pA23lGOgHaZ-9lK4x5B-m2vV3TWmoPWt1_dVlSROB6CzKcV-cjkxP0vcXrE3GafvDdaA8R-u-SgbuylG8aQkspFbEYEhwabhAIL84BCYbDzBYWM8u0_qnEcDJX_9zQnD06yrtB9bZJHXYvWC_-beV6-UT9sOV8HoAyPC7_Wz8qB8kMfsQdVYgYWf-DeoQ0tZSoeeqJCAoXQXAtD27IkWig3Jt7A_zIqtpyh4LWlroDPcxV53RZVJDkBqX0Jrb0Z6sS9BzutBqiNSfFOtYXI7m0UYw3z1vsWa2BITfo5Kof73fEo2yldKgrltp5GVGRBiY1UArEiy8sUtCRSnp--Unw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OmHJ_d8ugQilKZC6O0S_P6EoMGW4PrX5-tOG-fYWUI-SBw1M1Ba7bduXAbRf9Q0PTu_YfSwa4_TNWd9Lw0mNtDIT3gbtXRkfzRLj2LNVCmEdlT3-QYcTP477BhHynqWftDhhL55qesO7KKvCk7DAE6wseTxcv_i6T6GyZOX9MFsfZbHRJ2EG6s2m1O2mnpsiGOm_8lpRL7fDez9XtjnxZIHzOLqdEKYi1e5uCbTnh57GdlStvaoDkC3cEsT5iQpIpL_E33mVLXBa2Zdb9KVBUKqqIwjM7ywjQB7KtDeT30UtEgHxFDGHzw7i4tZK_1rCJvb9fGRdDP22J1Izy-UaIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/pnAGf3g5U1UDmHKWI1tegfGO7HRt5zNPlOXLvzyFkQro-W3v5a8J5f9_9Erak5IbVjgCxRu61BnMiIPnImgma_PDP2fLHr8evkIUJCeobtgpHWk29NEfyULdwHe6pSRazS__RfVbbabvPHmnCYkhYmi2YRKBtjKafYRemec_kZvJHLNtOZIh4oBrstq_Td-LEEjPCiHfsV1d-T_KlfNuR_rWI2ArlC5wXxxVb_bUBFkAgMo75pyhboue8S4Tz9Pc6xCTaE0PwNBTiJEPYR3gDhBN0F9BbqHVfintYbReoCHcg_qwS0xKob21JA2G6EHiCi0WZ4YJVPcxSWzuGiCyrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/OSzmwVLlLDc6JZOkuU56I0gA7khqIM3sXZK66-6TwjDT5a7emmuyusnfjZ2CfsTvEIOScOqBybzLgM-V5V4WzQ1pFcvgRQIuuuGgaPuP_Z5oCeDiccrxUrf6BU29QpxtmJWDG8I9cfX28Rq8pHmW6U3anCIue-gh764r4f970owIhhbgPFb5B6ytwU31hT3cgQst2iot5LB0OoG8HNNLv7vWqeYaN50YldaqHxgi4P7oE2sZLJVQkI1WrVxmpCtb97VRfNLWC9KcFmhJ8a0uYib38jEhPKTUYJpjtvNIR3NB3U4uedLrfeA46lWRYR5Mu-hT-hO0luYpnchfxhIUpA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/RFCrgyEpfq5VMwmB56Fh7Wwf9ZgM_4P7J-07bkJiQXXv2vveP-Hz6LALEYwjodgK9DCgWDgJhz600TfKsrZWCvAwWnEYTt3wv1wKPqWwqUBLZzmnlbcjhlf_xOtpT4dzmH53bKSM6iYFA4sOO37sI9dhxVERIVdpJ_QZ9vE6itHhH5WFDfUwu_QjMALHijqNu7qiQEeTJhaKs7VNQMg4sfOIEwFYb45PgavCqSkUI1KD1hW15_AxPVZAMOrWh8o3U6aRkkRy-cFSOJIeyn6tWa7RR-nPx-tJ7c939fZ-SIZBkNS_uxwG6nzLAkIh6MVU0MtlMKnjB_BkNP7NbNlE9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/BMmYJG6Je4IeMcCsBGbHmqacqp6TeYmuzjzcUfJ8G31IfI-3MEi7r7yFw7XSpoiXws6d2sff6xq8iv_Inj_YusRT6mHhZeN8C1Bk_XczVOK84Q-8UQ_09Ag6Evyo3jW50KvCrGOeHfW3T_tpzKxPK6SECUNW1WYonv9i42mIEMdX1SdvCbFIJg0dMQXVpp8WTlIZkXaFxO7cbMH2zn3tWGRGnrdlmlDSPtc6rqm9pRygndAp_m_1RX7UaqQsUxrA8fqJTvxo9t2cueVU_BUqoebaLMKTq67kV4rpM0bsLeDEsW72ugFcMeEKSoCmfpMhYWRzfo58xD6kcffGUM4cqg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تصاویری که ترامپ پشت سر هم پست کرد + ترجمه ماشینی
دونالد ترامپ، رئیس جمهوری آمریکا، دوشنبه عصر نتایج چندین نظرسنجی مختلف درباره توافق با جمهوری اسلامی را منتشر کرد.
از جمله یک نظرسنجی مشترک «سی‌بی‌اس نیوز» و «شرکت یوگاو» می‌گوید که به عقیده ۸۰درصد جمهوری‌خواهان، این تفاهم‌نامه «بهتر» برای آمریکا، و یا «خوب» برای هر دو کشور، است.
در یک نظرسنجی دیگر، ۶۷ درصد می‌گویند از تفاهم‌نامه اخیر صلح میان دو دولت حمایت می‌کنند.
در نظرسنجی دیگری نیز ۴۷درصد گفته‌اند که این تفاهم‌نامه اثر مثبتی روی نرخ تورم و توانایی مالی خرید مردم آمریکا خواهد داشت.
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 357K · <a href="https://t.me/VahidOnline/76603" target="_blank">📅 02:11 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76602">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aCQROgG9Tk5Awwbq-cftXmoUAgEPM72TjSM-7rxOfFMD_M7u9Q2PHGsDIxrGjGjbipsQTxxJMb3lxD4LXA8FxGsBCvQvPyYzBxRnNb2Tb1i1LyIcf4sqigG2TPe_acgbrgV_c1Uxmgdfdl3d2oJ-XFulI3ZD_iI7pjZwR6GvHegPwLVlasULqzVvjeorG8dFz61srUqerebjhWPSn9jw7kQDfSz_aL3VMFuF64Sq3ZytmoyKQCTU3hsw8Yf001byZxRvQo0faccAWh1c90ffzKvedlYOHOxo4netKVWeSpCK3jY8tq9DfTxbf9-g_msPitVtU3wxo789KQGFaZqykQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محمدباقر قالیباف، سرپرست تیم مذاکره‌کننده جمهوری اسلامی ایران، در واکنش به صحبت یکی از مجری‌های صداوسیما با انتشار پیامی در اکس نوشت: «در یکی از برنامه‌های صداوسیما دیدم که گفتند کاش فرودگاه مهرآباد را می‌بستند تا تیم مذاکره‌کننده به سوئیس نرود. به آن عزیزان می‌گویم اگر به سوئیس نمی‌رفتیم، هر لحظه خون بیشتری از مسلمانان و شیعیان لبنان ریخته می‌شد.»
پیش از این، روز شنبه، یکی از مجری‌های صداوسیما گفته بود: «در کنار بستن تنگه هرمز باید فرودگاه مهرآباد را هم می‌بستیم تا مسئولان برای مذاکره نروند.»
@
VahidOOnLine
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 334K · <a href="https://t.me/VahidOnline/76602" target="_blank">📅 02:10 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76601">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ: اوضاع ما  ‏در مورد تنگه هرمز خیلی خوب است.
‏دیروز نفت بیشتری از هر زمان دیگری از تنگه عبور کرد؛ بیش از   ‏هر مقداری که تاکنون از تنگه عبور کرده است.
‏احتمالاً این را می‌بینید.  ‏ما با یک فوران نفت روبه‌رو هستیم.
‏تنگه کاملاً باز است.   ‏این را می‌دانید.
‏خواهیم دید همه این‌ها چطور پیش می‌رود.
‏اما ما دو چیز داریم.
‏ما یک تنگه باز داریم و کشوری داریم که   ‏هرگز سلاح هسته‌ای نخواهد داشت.
‏هیچ‌وقت، هرگز، سلاح هسته‌ای نخواهد داشت.
ویدیوی بالا:
به تشخیص ماشین، حدود ۱۱ دقیقه از نشست خبری ارتباط مستقیم با ایران داشت.
متن فارسی اون دقایق
ترامپ در پاسخ به سوالی در مورد تنش‌های احتمالی در تنگه هرمز گفت
تا زمانی که ایران به ما احترام بگذارد، نمی‌خواهم بگویم از ما بترسند، تا زمانی که احترام بگذارند اوضاع خوب خواهد بود. 8:15
@
VahidHeadline
دونالد ترامپ، رئیس‌جمهوری آمریکا، دوشنبه عصر گفت اگر جمهوری اسلامی «به توافق خود عمل نکند یا اگر رفتار مناسبی نداشته باشد، من کاری را که باید انجام دهم انجام خواهم داد.»
5:00
ترامپ: نیویورک تایمز جعلی گفت، اوه، وضعیت تقریباً همان چیزی است که چهار ماه پیش بود. نه، چهار ماه پیش، آنها یک نیروی دریایی داشتند، دقیقاً ۱۵۹ کشتی. آن از بین رفته است. کل نیروی دریایی از بین رفته است. آنها ۲۵۰ هواپیما داشتند، همه از بین رفته‌اند. ضدهوایی آن‌ها از بین رفته است. رادار آنها از بین رفته است... همه چیز از بین رفته است. رهبران آنها از بین رفته‌اند. کل کشورشان از بین رفته است...»
@
VahidHeadline
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 341K · <a href="https://t.me/VahidOnline/76601" target="_blank">📅 00:01 · 02 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76600">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=bdo-FEQ7ZwtlG3pTfjYZ_sCr9AmgXWu-ghImazsGztwxxZG7dCo74MzZyJHktlJwSFdgW2LHG37FrjvE6zxjNE_UUhoh1wEgTtxuO82QBH76KO-zFtjGfhGitjhp0foyf0yMCJsn2DS05xd8ICLcpOqnylunJQZDzicGJf09_1YjB6RijCS74_Cjf-v35PSarxiapaL7fehNUzmYGIKRm4xVJhkwLvu3yYR5YDSgW1OOxFeNMiB-DMcd1Ag6KTl61nUovydRamNl4l162EqVo0IhSqjavEpaQMzUk1qS41qWlUG8jZQOhNvbMYw9nD21NEkxBhpXhjtTNnK4zSDCsg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/fee77010b3.mp4?token=bdo-FEQ7ZwtlG3pTfjYZ_sCr9AmgXWu-ghImazsGztwxxZG7dCo74MzZyJHktlJwSFdgW2LHG37FrjvE6zxjNE_UUhoh1wEgTtxuO82QBH76KO-zFtjGfhGitjhp0foyf0yMCJsn2DS05xd8ICLcpOqnylunJQZDzicGJf09_1YjB6RijCS74_Cjf-v35PSarxiapaL7fehNUzmYGIKRm4xVJhkwLvu3yYR5YDSgW1OOxFeNMiB-DMcd1Ag6KTl61nUovydRamNl4l162EqVo0IhSqjavEpaQMzUk1qS41qWlUG8jZQOhNvbMYw9nD21NEkxBhpXhjtTNnK4zSDCsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جی دی ونس، ونس هنگام ترک سوئیس، ترجمه ماشین:
🔸
سازوکاری ایجاد کردیم تا مطمئن شویم نه‌تنها تنگه هرمز باز است، بلکه باز خواهد ماند.
🔸
قیمت بنزین همچنان کاهش خواهد یافت.
🔸
سازوکار درستی ایجاد کردیم تا آتش‌بس منطقه‌ای تضمین شود و درگیری‌های اجتناب‌ناپذیری که پیش می‌آید مدیریت شود.
🔸
ایرانی‌ها اجازه داده‌اند بازرسان تسلیحاتی، بازرسان هسته‌ای، پس از مدت‌ها وارد کشورشان شوند.روشن است که ما این رژیم بازرسی را تقویت خواهیم کرد تا مطمئن شویم آنها هرگز به سلاح هسته‌ای دست پیدا نمی‌کنند.
🔸
بخش زیادی از تیممان را آنجا گذاشتیم. ایرانی‌ها هم بخش زیادی از تیمشان را در آن اقامتگاه گذاشتند تا کار را ادامه دهند.
🔸
این دارد بنیانی می‌گذارد برای چیزی که می‌تواند خاورمیانه‌ای واقعاً دگرگون‌شده باشد.
...
خبرنگار: آقا، خیلی سریع؛ دیروز لحظه‌ای بود که عراقچی وارد اتاق شد و به شما سلام نکرد. شما دست ندادید و بعد او از اتاق خارج شد. آیا احساس کردید به شما بی‌اعتنایی شده؟ آیا فکر کردید این کار از طرف آنها عمدی بود؟ شما آن اتفاق را چطور تفسیر کردید؟
باور کنید، در چند ماه گذشته زمان زیادی را با ایرانی‌ها سروکار داشته‌ام. گاهی آنها را به‌عنوان مذاکره‌کننده‌هایی بسیار گیج‌کننده می‌بینم.
اما ببینید، ما یک نشست خبری کوچک داشتیم.
آنها آشکارا در ایران از همان حمایت‌های
متمم اول قانون اساسی
که ما در ایالات متحده آمریکا داریم برخوردار نیستند.
ما با شما صحبت کردیم و بعد چند جلسه واقعاً خوب داشتیم. چیزی که برایم کمی خنده‌دار بود این بود که بعد از آن جلسه اولیه، نوعی توفان در شبکه‌های اجتماعی شکل گرفت که همه می‌گفتند ایرانی‌ها می‌خواهند بروند. و بعد ما حدود ۹ ساعت دیگر با آنها صحبت کردیم.
بنابراین فقط به رسانه‌ها توصیه می‌کنم کمی به آنچه از شبکه‌های اجتماعی ایرانی می‌بینید بی‌اعتماد باشند.
آنها می‌توانند مذاکره‌کننده‌های گیج‌کننده‌ای باشند، اما احساس می‌کنیم در حال پیشرفت هستیم. ممنون از شما.
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 343K · <a href="https://t.me/VahidOnline/76600" target="_blank">📅 22:17 · 01 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-76599">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ddQqjgIiauH-8SJJpepKyhJQDWlZgGXnrfLfVRaB-05U4CQWWRen_QOSgXueH4MccsfIiUfzatNNza_7HFepKbznPSjp5un5KFWVgpqUmZl9mhPWTqHjJx66AFZH1a7PqWtFLcSvBm7Wt9flS9BjVbAJ_25_qZEIq4ibft8UquWkm0-liBGnSGn_qDgen7u02L0pvK30vkQzyCTAKX0WIh1Dc3mVyzOhoYP9MViwUynDfGbCLFkmQuohDltNli4m-BEWmZPfmF-oDt6CVa4HyATuQYFW3UYmwQ5FVUJPzokZU6bXwgZdxIQITi1yjqhth76KYL_2UcjFcIo82FMllg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست ترامپ، ترجمه ماشین:
همه کاملا آگاه‌اند که ایران موافقت خواهد کرد که برای تضمین «صداقت هسته‌ای» در بلندمدت، بازرسی‌های گسترده تسلیحاتی انجام شود.
رئیس‌جمهور دونالد جی. ترامپ
realDonaldTrump
📡
@VahidOnline</div>
<div class="tg-footer">👁️ 337K · <a href="https://t.me/VahidOnline/76599" target="_blank">📅 20:41 · 01 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
