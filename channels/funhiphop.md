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
<img src="https://cdn4.telesco.pe/file/Nln8KtexIZnlWl7nW0vlgJ580O3tZ2xxMB0gTGWXtR9s1FxC0S1_3KWXqyV1WAfnydY8eqGiBRWs0qYU9sETNYIfKEemdNU3OUtEj1wdCegSnOUlBEIxqrhqgJixSfCMgmvRKX3NswJEUh6BiTJJQ2TS49wKXYiXrXPCwfdtjyQkfREidCG_7yGpA4UUHT9Dq6j7pMzqrEDWYjpoNAL44A-wLU8-H37uO49QryaL7QZJCNmbWfHTSwYMXHp0YDS944NSDZ6wBKfH2xSUEDHIoLW4U7CfDwSWiU1fl4x9crCFL0S9xdxzsFBxgUMZ9ra-QUvBWouXTjg02XG0Up76JQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 151K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-28 17:08:29</div>
<hr>

<div class="tg-post" id="msg-75272">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pAKkHq843aQMXdK3h0kDBLVV2E8Ua8znym0v5_ilJRoAgsif8E3Qxy2BE0Lo2fpD9it0y_SgmV75qwBsPrJjisj46IrV4PsrE18GAY2tZaK3hzedFvkIw5sin7gErSGDFm0w6gadwA3Nw_m_cc4qAniUSokZ2rGbGIs6cSREApF-CLNd-rpprZEZ1n9lXNJEC0u9ZfW_6EB9hY_y-oulvoa6Gi9ClyKEDqYTfzgmNvGM0Dnv2LcOKRTN7Ev3c-kBOdQoOWHqWoziAjRUEcKHfC9TO6snUA51eXfpGrCPZ6BquGF3rS5hxCYoECjr7zFOeT2tkCOAYufdi099EV0mzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 841 · <a href="https://t.me/funhiphop/75272" target="_blank">📅 16:43 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75271">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lw--TwXPesRp4lvJiB2k0MwiP7tfP7L986isaR0GQSF4-Y2dE3h0uVTRBzD2UAUZnnRs0obnKP6UqTyKD6cVC0_FmHIJ38sE8lm-BoxVbp5wd8x-0AGvCCTwC7hcQdWLtH7GgjsjHC8trhe6agewLUWg7ReFFY24KkSvYJRN2MaTBXPhfS0gFwrwT4JvEyn2YJyL-NPCkjOMX4pSyUJWDUFZ1btG2NlBMnOmBXubDPtxLysIMEhGMa-tiwD55K741OE5c0GVQfBeAJUlqnmgz3r6V49KScWejUim1cc-dc9CE_iALkaSD3gy58FJZ6CwSaewb6Y8mYvabW8eGK7osg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبر بد واس رئالی ها فعلا قرار نیست جام ببرید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 1.8K · <a href="https://t.me/funhiphop/75271" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75270">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">الحمدالله اقا سالم هست
توضیحات مدیر روابط عمومی وزارت بهداشت راجب زخمی شدن مجتبی خامنه‌ای تو روز اول جنگ:
۱۰ صبح روز ۹ اسفندماه در وزارت بهداشت بودیم که تماس گرفتند و به ما گفتند که حوالی پاستور بمباران شده و جنگ رسما شروع شده است.
دکتر ظفرقندی، وزیر بهداشت همان لحظه تماس گرفتند و جویا شدند که آیا مجروحی یا مصدومی را آورده‌اند و بنده گفتم که تا این لحظه خیر.
آقای ظفرقندی با موتور راه افتادند و به سمت بیمارستان سینا رفتند.
حدود ساعت ۱۲ بود گفتند که آقای سیدمجتبی خامنه‌ای را به بیمارستان سینا می‌آورند.
خوشبختانه اتفاق خاصی برای رهبر انقلاب نیفتاده بود. فردی که در محل چنین حادثه‌ای باشد، طبیعتا چندین زخم بر روی بدن خود خواهد داشت.
این زخم‌ها نیز زخم‌هایی نبود که بخواهد چهره رهبر انقلاب را مخدوش کند یا اینکه همانند امام شهید ما جانبازی بگیرند یا قطع عضو داشته باشند. اصلا اینگونه نیست.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 2.2K · <a href="https://t.me/funhiphop/75270" target="_blank">📅 16:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75269">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kI9s-aXNIdBcYq17H6C4qP7tcJaSOthOFC0b4uAEbybxCWZCRH3AIawsOG1yKdXAl9c72dAn6WbLoCE_HPSR8FZ27p99EbZomHvNq5xdquzPGE2m4L9RZtMw_A5J5vSBGZcBWiMKf-9TI8PWKLpCYuBAlxasD-8Gwj7ajk7o45WMOQslfvQiMyOMHvrSluUDuDw6149EyHeXjxf4uobvN83qQakpdyWHzOXLz2NUyPT90Rn-elCpKPmcSheB4yF2cUp3kGg2yhiDnHUsRVGG48gWadvE4OCPipGm7IwKXn8G_z5HL60VRcO2aG0H_uZt6Kph3M9kXgObeefiyt10Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات کی برگزار میشه؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 2.89K · <a href="https://t.me/funhiphop/75269" target="_blank">📅 15:26 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75268">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNCQLlOdlUd-MdjB9sAXwdauW85LlTYmyn0xNiy1JhZXZYiORtMO5i-gDeIf-7DmmKaRZZfPJKzH1ubI6IqRiibKQ-Dj-w9tp6CJBELdAl-7-LrubxUYTFDv-dgErExnBqhc6t7eXq-v6dE8wkc7WkkLNl87H4W90lBHq1DquQN0V427NmDFLYbtkr_WcoT3kuSIPylynVnBfEwexTwIpAyyOQdjN4O5lg0Z0chyPiqwLi2D2HktG3o_06pgSmk_qRA0k4GnVwddVBZWWK35i9I1hHKWU4y07dauqI9az2jIdKP3v7hfTC12MDluEVn7BOxeOww7NzIvtf_gBf_yjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید   این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست  بنظرم این شرایط باعث میشه که جمهوری…</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/funhiphop/75268" target="_blank">📅 15:11 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75266">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دوستان عزیز در خدمتتون هستم با یک برنامه جذاب دیگه از سیاست با فرید
این چند وقت بدلیل اینکه خبر زیادی نبود برنامه نداشتیم
خب همونطور ک میدونید آرایش نظامی آمریکا در خلیج فارس و دریای عمان کامل شده و هر لحظه امکان حمله هست
بنظرم این شرایط باعث میشه که جمهوری اسلامی قبل از شروع حمله دوباره یک پیشنهاد طولانی به آمریکا بده و باز از برخی از مواضع خودش کوتاه بیاد تا ترامپ رو متقاعد کنه که دستور حمله رو صادر نکنه
ولی این پیشنهاد هم مثل همیشه توسط ترامپ رد خواهد شد و دور بعدی حملات شروع میشه
هدف اصلی حملات حذف یک لایه دیگر از مقامات جمهوری اسلامی هست که به شدت مخالف توافق هستند
تنها چیزی که مشخص هست اینه که ترامپ خیلی زود تصمیم نهایی رو میگیره چون باید قبل از انتخابات کنگره کار رو تموم کنه وگرنه انتخابات رو میبازه و منافع زیادی رو از دست میده
تا برنامه های مفید و جذاب دیگر خدانگهدار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.64K · <a href="https://t.me/funhiphop/75266" target="_blank">📅 14:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75265">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jfgpdGDizzezjy18xKq3bo4LV48LVbz6SFiu8IdC7p2-3i-vUX26qLrCf38mdO5NJcGTYmb3RssM9wj34BTgmmZO3lsXi78O8asjZW0x947UyYuK2yKv9loIFiOKzxpWHsdgu0mZQ2Qj4vvbMtniCRCkx_lkJA7omzoNmPF7Pz713oS3_GMFWIipL2LAxset443nsg1K5lP3r_RDPtamO7kSVf9np10FLWbSHdZcwbBLKl8znrZg2v5ZKlF3QV7B-xSNLJJ1ediqX-ALVCfIhAJrEyqDaynuP-UTfFlhmgi5FReJuXIsdhNgkt7_NXkUOsuYqtz9EDu9tX0Hk7q0Rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">علی قلهکی فعال رسانه ای :
علت اصلی آموزش‌های نظامی این چند روزه در رسانه‌ها و تجمعاتِ میادین، توصیه‌ی یکی از «مقاماتِ مهم» برای آمادگی بابتت فازهایِ جدید جنگ بوده
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/funhiphop/75265" target="_blank">📅 13:56 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75260">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وضعیت شغلاتون چطوره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/funhiphop/75260" target="_blank">📅 13:34 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75259">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">دوستان من شوخی میکنم با رضا پهلوی چون فامیلیم پ داره نزدیکم بهش
شماها بی جا میکنید</div>
<div class="tg-footer">👁️ 4.58K · <a href="https://t.me/funhiphop/75259" target="_blank">📅 12:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75258">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مهدی قائدی پیج رضا پهلوی رو فالو کرد.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/75258" target="_blank">📅 12:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75256">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fYC7GEwqlFQHPMBaLccHY-DNZkr1R1prAkn9O2k9Q-kRr_SjbR0F8DANF2RD9S_WQG69xD1AHnWklpB13E98U2RmW-UnTCSm-8qU-jrr2GIU7NHEFuyMT26JLxEzU7cXQAmX_gVE8tyD8ZxwSQLnP8OqlAN6m5V6m2Zg1V3kuz6glbminEFnEHP5W38cn7QsWB4WW-VOzfn8ziz3oqBaXCAiYX8FCJLcekj4DBVd3OPrSuD9XsSeePpoyLJoaH29PPlE_wIBzGev9bnTX9y4n6D11yd_LMLp_w1SqoX20qp4PWNMpLxrmeQAJ9J38mnBwLh17sTJpGoCc_gzZvZwjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش سردار  به خط خوردن از تیم ملی:
پاک کردن پروفایل با لباس تیم ملی ایران و آنفالوی پیج های تیم ملی
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/funhiphop/75256" target="_blank">📅 12:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75255">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">انتخاب مورینیو هوشمندانه ترین تصمیم پرز در ۵ سال اخیر بود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/75255" target="_blank">📅 12:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75254">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فوری از فرید رومانو: مورینیو سرمربی رئال شد  @Funhiphop | Farid</div>
<div class="tg-footer">👁️ 4.76K · <a href="https://t.me/funhiphop/75254" target="_blank">📅 12:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75252">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">کوروش با آهنگ علی سورنا پست حمایتی از جاوید شاه گذاشته.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 5.25K · <a href="https://t.me/funhiphop/75252" target="_blank">📅 11:19 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75251">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">✈️
وزیر امور خارجه کوبا
دولت آمریکا بدون هیچ بهانه مشروعی، روز به روز پرونده‌ای ساختگی برای توجیه جنگ اقتصادی بی‌رحمانه خود علیه مردم کوبا و در نهایت تجاوز نظامی می‌سازد.
برخی رسانه‌ها در دستان آن‌ها بازی می‌کنند، تهمت می‌پراکنند و اتهاماتی را که خود دولت آمریکا مطرح کرده، منتشر می‌کنند.
کوبا نه تهدید می‌کند و نه خواهان جنگ است.
کوبا از صلح دفاع می‌کند و آماده و مهیا برای مقابله با تجاوز خارجی در چارچوب حق دفاع مشروع است که توسط منشور سازمان ملل به رسمیت شناخته شده است.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.41K · <a href="https://t.me/funhiphop/75251" target="_blank">📅 06:09 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75250">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e0m7_25x9o515TTlzYggsd-Tq2JTkf6CILl0R5K9x0PRO_HN-C1xGXqcDh18BWZXGEFU47Bc-Yy9LYXABS0kiHfAO0UFKP7FRti6EG14m94buMPwcfK_Fq3iRD71Fq249f4gTlVaRdXI113Wo9FXpU_bJ2mRmFmJ2EO1a5226WWDjT6IOOTAfrhIGYOy5X-BpJAlfxttkMtwlSUpVckaLtTPzL16D7jvWdHARXxE9iUuKazvMXGm_UKROV4SfGsWpAZXdj-SXYg-BkL5D2qvkWsy0uTSSCWjiBo43mlWK3bkm3rsrfYZtpzd_oG2TxKVrH9-182TMqc-HKSRcURWwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
تا یادم نرفته اینو بگم؛ مارکت حدود یک ساعت پیش باز شد و تا الان بیش از 500 میلیون دلار پوزیشن لانگ لیکویید شد و قیمت کوین ها دارن به سمت پایین حرکت می‌کنن.
🤩
ترس توی بازارهای ریسکی داره بیشتر میشه و از اون طرف قیمت نفت هم روند صعودی گرفته.
🥵
مجموع این اتفاقات نشون میده بازار فعلاً داره احتمال تنش و خبرهای مرتبط با جنگ رو قیمت‌گذاری می‌کنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.28K · <a href="https://t.me/funhiphop/75250" target="_blank">📅 04:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75218">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PEURrXNWtDsej2FZMfJH4LYm8TaAhZTPEpZs7_jZLWD5_KXv0I4asgAsZkmAmAEYn1PR5miudLysrlAyx56U5iotnAEbbU2qMPjw2nL5Kartpw-R5M1GTx_x7576TxTtOrZoL_EifCJCugmRm_NBmCLnTkpoFfUDzRer7JIXgEvdqj5bHnKYDmNT-1Piv3e51zFWJuTasZJeQJMRIso2kDqsHGKymdL-r2v6GiLkGD1EGeqA0ygPmMsuWxbC4IElVFKE8dULzwJDxHIJS_FjyIS_DZOvI2q78Ec_RDatGSGrclmC4utD0QkX9Dknt2ZJicumQO2TAidSKSyinW5jdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک راه اتصال رایگان که این روزا جوابگو بوده کلاینت (فاطمیون) هست و فقط برای اندروید هست
آموزش اتصال داخل اندروید
لیست ای پی های جدید</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/funhiphop/75218" target="_blank">📅 02:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75217">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fl_mi1GSwqSwZba57SWKB0dt2Icyok4ufh9lOnsnCfwspZgbVCiE2-CGg7V7Yg5O7DHbo5ZFw_mReQa96qYIy1AyNB-YCFZ3imsENin_eToapxOoFJHJfEreW-hvzOlYzD7UySvJzb1mYNEsEU4b1xNpR6BimS5VhweFT6ua7zO04fLfyVfuJyn58JOW3PvXMoRhZsklAwsnxRLsJcc3lOIC9-RAMD47MLuQWtTNXKTbITftSB2lsasBKAzt4duMdABLaj2I1N1lrN_He2oXxRnQiik3yXYEetmKxVzCw5v4-RswZc5-xC_LneEQ4AH6d4Do-XI_ah_Ehua6-sM3cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.38K · <a href="https://t.me/funhiphop/75217" target="_blank">📅 02:06 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75216">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه سری اشخاص دارن توی چنلای خارجی خبری ریکشن فیک میزنن, بعد ادمینای اون چنل هم برا دیسبک اسکرین شات همون مسیج و با اموجی هاش میزارن بهش میگن دمت گرم که ریکشن زدی.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 7.22K · <a href="https://t.me/funhiphop/75216" target="_blank">📅 01:52 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75215">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">لبنان MTV
مسئول جهاد فلسطین، وائل عبدالحلیم به همراه دختر ۱۷ ساله‌اش در دوریس در دره بقاع، شرق لبنان توسط ارتش دفاعی اسرائیل ترور شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/funhiphop/75215" target="_blank">📅 01:42 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75213">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS0ulf_2xtkUw439Xidq1QP30cbkLzfM7THhPQF7fUQ8cqaTNCoEswWi8m32dHce_79hTNFSklduVECayyncrur_CYoL2OENJo1GlmNVeul_yv3wmX0oQ2uyWMI3LXgDFUO9enVCSNqso8d3IsMV4Rp0AnYcR5nuC1F_HBcyfHOlQ0MgtnNYL5gS247fCB9EVYLD_FnM2NAi6Qjr0Il5CoFga9cgEB5pUrf6YHEix3PDHQpqKEUDYP8seehZZkuKtkixOO4joCp4qGYJGRor9VJmuk_ywChHYxA0D-nSxJeWO83B1NVOBUvjriXAVrIfnd6rDn5_aDpNu-hmCI00Zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در ادامه ترامپ این عکس و توییت کرد  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/funhiphop/75213" target="_blank">📅 01:03 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75212">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vk-s9rRdd8yQyS2Wh18sNQKHl4M4w61wM0b6k0iNKbaIZVoaKBCeUGyx-lvc_lnH-rF6tE_XmkMEjPwxRub9wwfK0E0OjK7c7It1S3aubgU_BG4jJErhxSNmkTqsYRqNfGy1_9jpmAaADTBpuqAKH7HitBPxNISjQLUkJOUp8h62U29hkHikBcCZnOyPYhoxwLnR8ZnIBboI1IqcttauO8WSr7AWViToJiKkFIrm_tqO4HtOvBwlmBRQLODwp1HBI4qx0R8glrPmE6dha1HNYmuKewstn9jBczb4lYlXibo_M3gM8CEvjkPhuHZpX5671J9P0HSpAPb4so5xry3p-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکرشو بکن تو 2026 پست های خیلی مفهومی املاکی و مشاهده میکنیم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/funhiphop/75212" target="_blank">📅 00:53 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75211">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">جدی پستایی که راجب ترامپ پوشش میدیم بدجور ریکشن خورش کم شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/funhiphop/75211" target="_blank">📅 00:50 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75210">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">کانال 13 اسرائیل
ترامپ در مصاحبه با کانال 13 اسرائیل گفت فکر میکنم ایرانی ها باید از آنچه الان درجریان است بترسند.
آنها باید مراقب باشند.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/funhiphop/75210" target="_blank">📅 00:48 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75208">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OwmE__nTMycbp-dW9CY3si5W-sWS-H2130gmgsvFYFEgvVsRZHTS1WYssjTHXN5P8rZtrp86Wmg9PSF2HXV2XffM8Ym7Tv99cVacWRBm64L1dj2wXA11wrFedciVU4MggVK6CrP89fXB5bcFU873_ta3TZwi6r6u9XFQF5xFZIORMVBOZbyVdakGXLt2vY302A-fCHYDf-ig1SSCyJWpmty5JMKn2Wb_Jiig_xWtUjo5BZ5DQM4UYSBLSBFA2-8y9EJ6SY_iWT3KIgHVMpFplEUd016WnSR7U2McOUXiSe5xiXVuWE3VwyyJMNEMChzW9gUcT8NFTWsn770vfgku-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوبه خودتم می‌دونی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75208" target="_blank">📅 00:33 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75204">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dhoQp1EUzdWTw_COu9Ip9QG1MM3wz2lWWztuzTb_8h22JtMMISkLgfuowycmMivqZTSHge2N6cCUI4v-jawqqN_JxoIvdYV1WXvtk1F_9sreJXW2R6p75dWs9cV7MvNY7O897ZF9HUoR03sPBqPrVLO0tVzxj13yUgNV7v-jL-IY_kqybgLfsNDfgovPjfbnSwNC21dJPDhyN_6037Wg1BsnuIIvDxi4TARgReumhW49kt5ldamwEPssgJG1FufmDVqmMOnmdWkjOWtlliJfrHFVGN7x0ckKGmRiKjSrsISJ1ZrCTV7QXTYY6sDnng-ByElcttOOAcZ89m1PwiQLig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WiUDVG8BicPWKx1N9QWgKI1lwoWkp7iZgRBgTavQyisOjvoax54xybamtqqNyTNYP93uGkK89mxtHePTYaQOR9Ak8dX-oHL08Vq6T-vhTd-m9vXKsCSNJRKt6rbyWUazGb7ruOa5_xZ0sfplrK3an7p38iaosG3cO0CArMPg0zdpjq3PEwEOqOgBL-2W_FgQhP5llIMnaOaEeCm9UXXvss85DMX7Va1ehuET38UMJEm6SqA267gqDtGvvXiaNdGxtXKdq-l8Z3mGmFlotEZtZm2HsMslprjJTA810VkBvt_h1nZFHPfq9Bj0dTBGbnNS6uomYeqclZ3fUiOxBkxT9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qvdvvwXpwqmBfmRAjxCTJvJpKeFz25Y0ot4SaizMRELZYEvBKsBVzRF8E6rUjrze87L0bqfmRqZg3wGMHMFwayQlqSQpVqHEpNd6oUFVOvh4A-ylmRHBwwpwfc92FfP4bZDNQczleUpWIVo5sDNr4nivj7rZIrF-WOt2lYIzqaeGcpcSWbBxMARdrEIg6EP6zZimFV6OBDHJ87mHBDqQTqJB-oZJxnvXa-4IeN7TLARvpkTsItSfMPd_j95mWHH2xttIfPCRLkwbTJXHTodPyRVRftTQoFNRfdDl3tX671Q-6SJ2sshNCXemcWrQLtHiZzpB8NR-qoA3EjyHefwOYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dSLy0mnvnOtmovwMRK5HQ2xtnS8tPiYaCModnsCPEoUkyApcOBHW6hMlDZOcz3EUBIPve4gORCWgS3pVk3annFnYPEy--gYsXIG-p9AAsgJMhIBcLp1mM2m-TxhIKyLTAUOFgWYq9mjDJ8BhyWL0ahYIXTqHKtQOs-QcCTeFDYnqJqx9XuKZEEUV_fOHPuBu6i0alAEPCAClmq5vw8iXPVbnY2AQTxEqoeeCX8M0TUVsUS2NSHeGBJNkUozY3MT2diOT0pEpco8z-sW2rKmt7oj1mqt_OwsJVUqq6it3VIh_iiEN9CNWVebMcnW_OZ-XSpzEStVvh0D7cA6WDetFTQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فکرشو بکن تو 2026
پست های خیلی مفهومی املاکی و مشاهده میکنیم.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/funhiphop/75204" target="_blank">📅 00:29 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75203">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RRmYAQqyvthOhrEUbtMcVuZLvoepUus1EhQfQGKjRwrrNMD9qDB447gi2J7-8yoDhXM4GeHH7k_bfyYuVJaX2YMop3KS865gUAJfbxCUi7LSVR7MuneuecdW_zZ5TNOIOB8_itx_jwatP8fO3bdTbjQZBCpj4ezt628-GhEkUU7N-CQ34-AXBsQTCv-nHSuLMQ_VEi83Kr7yiuPnOvQnRlBbalrHYOYiEcuCIbfEPImhNEG7aO6h-suUxjplENTRuYdKcYYjy45A31GWXDel_ZJkw6MGS01I36xi8US6og1ydlhplpG4AYu2Ahx0dl7bk3OnzYPy1ud1L0OiXXsDcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/75203" target="_blank">📅 00:28 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75202">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👻
ویتالیک بوترین
ببین آقا یا خانم باهوش هیتلر حتی کسایی که معلولیت ذهنی و جسمی داشتنو هم اعدام میکرد و میگفت برای جامعه مضر هستن.
🤬
خوب حالا یه چیز جالب میخوام بهت بگم
بعد ساتوشی (سازنده بیتکوین) یک شخص هست بنام
ویتالیک بوترین که سازنده اتریوم هست و ویتالیک داستان ما اوتیسم داره.
🤩
عملا فنای هیتلر مخالف زنده موندن چنین اشخاصی هستن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/funhiphop/75202" target="_blank">📅 00:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75201">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=OIue_Cr9icSLBDPWnHxBX1Yuh1V1mP4scD1t4JZ36-vZFsPvVOXMh37MwXvo2iaF3vTdhbLYbijWuO6Ax_WT2CjToaIsim3M3Y-gYlLgA6332YDZOy3wi8MsFiOu-pTlRA6D9nRXFgLE06EMjwv3Vf48kEnjjNM9iXmiQt5yV7p39nG96IqbtUknehuPprPks9lAdAxITT25wmGkdglh5hkEAGr8B-7gPxeJW2Gwjs0Zhnz6hB8bUI-9AMj9V4F7w-a55L3t9MJzimaM2bhRD_J4N4lNIpjyqSXZl_7EzcjshHf-wEe28LYQUhHYd0g_LznKl7Rzbiwl_ALbGpbCwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5adfd6fc37.mp4?token=OIue_Cr9icSLBDPWnHxBX1Yuh1V1mP4scD1t4JZ36-vZFsPvVOXMh37MwXvo2iaF3vTdhbLYbijWuO6Ax_WT2CjToaIsim3M3Y-gYlLgA6332YDZOy3wi8MsFiOu-pTlRA6D9nRXFgLE06EMjwv3Vf48kEnjjNM9iXmiQt5yV7p39nG96IqbtUknehuPprPks9lAdAxITT25wmGkdglh5hkEAGr8B-7gPxeJW2Gwjs0Zhnz6hB8bUI-9AMj9V4F7w-a55L3t9MJzimaM2bhRD_J4N4lNIpjyqSXZl_7EzcjshHf-wEe28LYQUhHYd0g_LznKl7Rzbiwl_ALbGpbCwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75201" target="_blank">📅 00:05 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75199">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">فعالیت پدافند در اهواز
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.53K · <a href="https://t.me/funhiphop/75199" target="_blank">📅 23:33 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75193">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">محسن رضایی:
ابوظبی به عربستان تعلق دارد؛ امارات ابوظبی را به عربستان تحویل دهد!
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 7.29K · <a href="https://t.me/funhiphop/75193" target="_blank">📅 22:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75191">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">کی بود میگفت اروپا اینترنت وصله؟ اونم بزودی قطع میکنیم
خبر مهم شبکه CNN درمورد ایران
:
تهران قصد دارد شرکت‌های بزرگ فناوری مانند «گوگل»، «مایکروسافت»، «متا» و «آمازون» را مجبور کند از قوانینش پیروی کنند و از شرکت‌های کابل‌های زیردریایی حق‌الامتیاز دریافت کند.
همچنین، اپراتورهای بین‌المللی به دلیل نگرانی‌های امنیتی تلاش کرده‌اند کابل‌های اینترنتی را در بخش عمانی تنگه هرمز متمرکز کنند، اما مؤسسه تحقیقاتی «تیلی‌جئوگرافی» تأکید می‌کند که دو کابل اصلی دقیقاً از آب‌های سرزمینی ایران عبور می‌کنند.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 6.8K · <a href="https://t.me/funhiphop/75191" target="_blank">📅 22:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75189">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🤡
د فیلد مارشال ماحسن رضایی
آمریکا یا شرایط مارا میپذیرد یا با موشک مورد استقبال قرار خواهد گرفت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/funhiphop/75189" target="_blank">📅 22:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75186">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGodZillaVPN</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PAiKljxwkHHbWgBln1lbFsFwCLjsM9hWRARBB1VSJafIL7oQqLjrotfUfS8a6tt20oSKjMnbmo5veV8SBKP015VGidHZ3sATUmEWLaPlXQXz8DIPsiIf1V1nbHJVlsYXdElXaG9KiD4MV7HzWY1ag_82AJg87f6Ruy_tquTMK2cma37ronCQwzfxqy9YdNdnzfPkEGF9mfpDCfsd0elipC4d6HaEMpHdZ7Ms961gkkN9BBScxyStVwtcDQbnYya2fnAPKhL6Zx1SgM2hFQ9mhQQMQRp4WHUx5XNEDewSvHconEdjRnCRQIvjrXJWXwQOB2OfdCbOfbmLa4QjD3maZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">➗
پیشنهاد ویژه خرید سرویس
🔴
فرصت ویژه و محدود !
قیمت هر گیگ برای ۲۴ ساعت فقط ۱۹۰ هزار تومان شده است.
و همچنین یک سرویس
1G
هم روی سرویس های 10G بصورت هدیه دریافت میکنید.
این آفر ممکن است هر لحظه بسته شود، زیرا ظرفیت محدود است و پس از تکمیل، قیمت به حالت قبل برمی‌گردد.
❗️
پیشنهاد می‌شود در صورتی که تمایل به خرید یا تمدید سرویس دارید، هرچه سریع‌تر اقدام نمایید
تهیه آنی سرویس:
🏪
@Gozilla_VPN</div>
<div class="tg-footer">👁️ 5.38K · <a href="https://t.me/funhiphop/75186" target="_blank">📅 22:00 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75185">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ گفت من یه پیشنهاد دیگه دوست دارم از ایران دریافت کنم که حمله رو انجام ندم.  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/funhiphop/75185" target="_blank">📅 21:57 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75184">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید  هرکی درست بگه یه جایزه پیش من داره  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/funhiphop/75184" target="_blank">📅 21:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75183">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">زیر این پست زمان شروع جنگ رو دقیق پیشبینی کنید
هرکی درست بگه یه جایزه پیش من داره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75183" target="_blank">📅 21:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75182">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">یک فروند هواپیمای ترابری VIP C-37A نیروی هوایی ایالات متحده که حامل مقامات ارشد نظامی/دولتی ناشناس بود، حدود ۴۵ دقیقه پیش در پایگاه نیروی هوایی مک‌دیل، مقر فرماندهی مرکزی آمریکا فرود آمد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/funhiphop/75182" target="_blank">📅 21:36 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75181">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=iOX-XuOU32QXiAGLyNEL3iHSuNFT38Fl_QTcXHA3SoGK41QAcB9sUnW66ivE1slDVedYHaD2WO9xOtdPadT8WO5kjDlmiscM7iD_vb42_OJ_waBIoHTEkEFAzo9BT1kv2U8e74trEBp-YguSi52iJpqlZ2thQ0J1yhqyXUtF1TmRKbYSJt_D6OIVAcbqZt2TK7yFlx8tquW5jRdvn20U7dUhIfq0zu1aMw-uO32SXJWEe_67yCohU6FtoBq_CX7cP0GHMt3lmRR05XQcCtLeVBB5BxandxV8NM2nZl5L2zG5PsIPjQwhbPOr4GQBQTtR-HBMOK8VvtiMpvVQtAqhsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=iOX-XuOU32QXiAGLyNEL3iHSuNFT38Fl_QTcXHA3SoGK41QAcB9sUnW66ivE1slDVedYHaD2WO9xOtdPadT8WO5kjDlmiscM7iD_vb42_OJ_waBIoHTEkEFAzo9BT1kv2U8e74trEBp-YguSi52iJpqlZ2thQ0J1yhqyXUtF1TmRKbYSJt_D6OIVAcbqZt2TK7yFlx8tquW5jRdvn20U7dUhIfq0zu1aMw-uO32SXJWEe_67yCohU6FtoBq_CX7cP0GHMt3lmRR05XQcCtLeVBB5BxandxV8NM2nZl5L2zG5PsIPjQwhbPOr4GQBQTtR-HBMOK8VvtiMpvVQtAqhsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله بعدی امریکا کوتاه هست و میان یه لایه دیگ رو حذف میکنن و دوباره مذاکره میکنن و فشار میارن که تسلیم بشن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/funhiphop/75181" target="_blank">📅 21:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75180">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">آکسیوس به نقل از منابع خبری در دولت آمریکا:
نشست روز گذشته تیم امنیت ملی آمریکا با حضور ونس، ویتکاف، روبیو و رئیس سازمان سیا برگزار شد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.8K · <a href="https://t.me/funhiphop/75180" target="_blank">📅 21:28 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75178">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjolbI4a334mllpP4QTj8hGWWieF_pKfy3cf4Bh39vN-br9whIeVkpPpwC2IR85s11LZKtLYfaFL1XRX2pH5tNdKIJClXJSVbSz8f1P0DfEyCMW9wPaIk9XOQPgt9zF8K4hgJZWq1YGae472Rv_VWvLETP_dQxc6TxO97MpYhrUnJBOeQsNo8k7m262ExBmgwl7beM_D5zkDhDCCypdSsxhgAIsaL1DQMydhQbcUNOIldlb-l1Y6pu1Ppa7BmCXnvwOKA33tZIif0-m1fb-BSPKH-RTM4qLParM093e8cTWVEEkDmcsiVcMeKmKOAgv7vU_sVv4xyg2xvbY3Uzbzgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47 دیشب : آموزش کار با pkm امشب به حول و قوه الهی: آموزش لانچ موشک  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/75178" target="_blank">📅 21:24 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75177">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جوین شید چنلشون روزانه تخفیف زیاد میزارن:
@awsvpn9</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/funhiphop/75177" target="_blank">📅 21:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75176">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6kNN9FDMUpMPPiSaNbyKteQBUFyz-eALnfIRFTSL0zXSGJu9r_j7tzvn1nRIhPiWcuchmiPEVQbZSQI1EnNX3GU_QFK_1rre5mAPQvGSRWyG4uFZCl2BkU3I2KfdUd7dPSKJiRlpCUcFo9uwYkGxG6AY8nXLPXNq5vyPm-U7Sn_r9Kp6ZrSDtoc7ToMg2vd36SHvbbWBUDawEb2BBEwqv9PCdLKqfyIMiYfHgoiOKXHkYeoe58vQsf77EYsnTT5Ia2d1eozG9ErxfcgOGRbYw5N3UFNUk3zvpsbwBx9nBcKoeRQg6SA9oqchpZhLNbxPlwuC4vXBAQ2jvQbX2Fy7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/75176" target="_blank">📅 21:09 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75175">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی: انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/75175" target="_blank">📅 20:51 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75174">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آکسیوس به نقل از دو مقام آمریکایی:
انتظار می‌رود رئیس‌جمهور ترامپ روز سه‌شنبه جلسه‌ای در اتاق وضعیت با تیم ارشد امنیت ملی خود برگزار کند تا گزینه‌های اقدام نظامی علیه ایران را بررسی کند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.35K · <a href="https://t.me/funhiphop/75174" target="_blank">📅 20:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75173">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">یک سری رسانه عبری:
ایالات متحده و اسرائیل سطح هشدار را برای احتمال از سرگیری درگیری‌ها در ایران به شدت افزایش داده‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/funhiphop/75173" target="_blank">📅 20:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75172">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">ترامپ به آکسیوس:
ایران باید از من بترسد و مراقب باشد.
ما منتظر پیشنهاد ایران هستیم، اگر ایران پیشنهاد خوبی ارائه ندهد، ما به آنها به‌گونه‌ای حمله خواهیم کرد که تا کنون هرگز نکرده‌ایم.
﻿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.57K · <a href="https://t.me/funhiphop/75172" target="_blank">📅 20:40 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75171">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJBAkhexUF4n_mO9dbtxXZf3XoGlwjwr2zKiY4xSn2xeBBjCbe0Jd7NPXK2YNwB_tY3_iiVj6nvac8Ii87SvGCoyvW7rg8V6jpCuTp1BahnGeEdJFDm5rbdXX4HsxqOYkTAHuBd4n-OiiRlqFn5a4dGktFVY4aqqXo1VjRVUzVNVnm0ZJR1aY9k5UB7sIUMVJ_UeZQX6xP-M0aZrqWEVpmE-4G3TRxgTPcn6VOx1lTEUgc6qzS6dR9mus-hY-JUV8TmR3iJ7BrcKAZFRejh9swjG36zqBvY2BWWUEsUO_5IiMds4ONgg1BwJb8JAkrA_8KIaS4JVNNY9PSf0jSFMMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ: ساعت برای ایران در حال تیک‌تاک است، و بهتر است خیلی سریع شروع به حرکت کنند، وگرنه هیچ چیزی از آن‌ها باقی نخواهد ماند. زمان یک عامل حیاتی است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.81K · <a href="https://t.me/funhiphop/75171" target="_blank">📅 20:18 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75170">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c5ZpnY-hFAhCdo3reOK7OFgCVC3C1Gl8wMVrHcSt4c9pUmPg4ja_5Ugro5BdXUohD0lR4MMFbxCFBOjAYCMC_gZlWRBJbigy489-rytDHylE-rxPr96TGDd1oK67jaC5MAdemesRXX0MN5gAEeTfWxRHtgFFrpQw8cEkPUXQR0rv1p0BexkPKzw42vd49FdCC7Jh4yMeRZofEQDR6YStIdEv3z66yMuglgBsn7AH1k_XT7_HSKMhxaFVdP0lbOesgbbdJjm2HVQB0_tS0aIMmGXYuM5y6MXgF6lB5CZ3xQPwiPpep2CyzaBvzG1H-Vkt-9zCKUEdaTOlNe5Yll-EKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیکه خدا لعنتت کنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/funhiphop/75170" target="_blank">📅 20:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75169">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">‼️
یه جای جدید هم پیدا کردیم قیمتاش مناسبه میتونین چک کنین. هوش مصنوعی هارم همرو جوابه هیچ محدودیتی روی سایتا نداره.
◀️
یک ماهه  گیگی 170هزار تومن میده همراه با تست و ساب اختصاصی
ایدیشون:
🔴
@Plus_vpnorg
ایدی کانال
🔵
@PlusVPNorg</div>
<div class="tg-footer">👁️ 4.36K · <a href="https://t.me/funhiphop/75169" target="_blank">📅 20:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75168">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اکسیوس:
ترامپ و نتانیاهو راجب ایران گفتگو کردن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/funhiphop/75168" target="_blank">📅 19:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75167">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">وزیر کشور پاکستان:
پاکستانی‌ها شبانه‌روز برای موفقیت دولت و ملت ایران دعا می‌کنند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/funhiphop/75167" target="_blank">📅 19:17 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75165">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/hVmw8tJg7jldo45xDT3OUJTw_u93fdv5aOmd112Yonpoij3oB6eu4JghNJr4hP21VOtYeeWIhSIDGl0dJOCz_68rj2vIQlkg7bIlZwnYXo3wa_EQ2v7S0AXwc5AWQbLv0JnRO9wngeK4eKtAcF3VweoI6qHrcfaTvhbc6_Lb8nNQ9e9l7HeM0LeouLiZia1UTS2fdexQtDFIKlsCzqS6JHw1q3Zum93CL41hfjf8ZxrXJjEwad68H9VH1VqoKw4Yl_JZbccphMZB5ov90RfozvxAH3TfbJZeUXI1lwHcEpzFRAolfekb0gPfQcsxri01xM6ocS8k-rTzRqQqzeMulQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WJ3WRV8e0QhQhhh0KS6_IGoCsI_rlqXaERt8Ry-hynPo0cZz2eCY4IbzCGgOnfFyiQevpOeOyroeyN57wEFTQxPCJSBHdhrrn7d01mwBXqD9D61NvMUHSJF99-eLOCtHqVJIWqb8Cx3yYzDaIWcHaIJFbFpaDummYOZ-FuT3MKyPTyzguN-fvbqUcB_NSBzqJL0g7sVi3KLvwZWiF4WS1Ie4nHlYWwsTh52jXS0-Kz0Vj6ZujuI8W6Fb3_1-5rRNiz2B8tvipxCf2we4wYO87W2PMh2f5tI5JKI2psdR0Y1u3LzyUMV8sueobh2STu18hACdC-s0H9cVgDGkpX3OzA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آنالیز تصاویر ماهواره ای نشان می دهد ناو هواپیمابر آبراهام لینکلن در فاصله ۲۴۵ کیلومتری از ساحل ایران مستقر شده است
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/funhiphop/75165" target="_blank">📅 19:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75164">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=Jame0w_aYmj-5O1m1ENrGKjlWh7G7z6iGCGxpjFaFqWqyYV_wqOZ0DInya6G7gBOw4e0N1goMvEddGv28-qMfdYPAFD_sCcRfW6e-lEX5NXtOkjPrIEhelPMgRRBEhNNXtZsp2uStjWdZElfXlrg4I_zU_48TpR8wkqjqtkBHAT0AhNrnh3oqLi0aHzJDGNeVvbvvFjF6KGRaa7D50_lf8Mk4OBGCjiXtPO_hS5MSYSo0Cdikz5VVALOTNUtEL2YAYHbK9asDEB6H1BEVVNIPRpEBMmdVJx7dGGLYOJwcSLbYpezNZ-G1xbHR6JlHIoBzX6EaJbkN7j7fbqyWKNOhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6b96b3b62.mp4?token=Jame0w_aYmj-5O1m1ENrGKjlWh7G7z6iGCGxpjFaFqWqyYV_wqOZ0DInya6G7gBOw4e0N1goMvEddGv28-qMfdYPAFD_sCcRfW6e-lEX5NXtOkjPrIEhelPMgRRBEhNNXtZsp2uStjWdZElfXlrg4I_zU_48TpR8wkqjqtkBHAT0AhNrnh3oqLi0aHzJDGNeVvbvvFjF6KGRaa7D50_lf8Mk4OBGCjiXtPO_hS5MSYSo0Cdikz5VVALOTNUtEL2YAYHbK9asDEB6H1BEVVNIPRpEBMmdVJx7dGGLYOJwcSLbYpezNZ-G1xbHR6JlHIoBzX6EaJbkN7j7fbqyWKNOhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.08K · <a href="https://t.me/funhiphop/75164" target="_blank">📅 17:56 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75163">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HCY6YmJGB0VOPTnaKsfk_FRJkMXwwAOK_jRmbPubSEnYMT1d40fcBFumJJ-lj-ELRZl2pXpXgjt6LUoRryhxygLuAzMHrDLZ2PA_emmJ3YB4tiWYANIg0HtLAkLNPtuvSl4VIOxvT9-7E2GZrQxxaNcrsUZQhsMYTImIufx_e0UOnxXZY7HHzpUsQub3pkvo3-1UkH68g5XJRC9VvPj0FgraFfuerB9D1OCKHERHXyi3QGDcLbI9KeHqq5XoaFAmooj9VkaVDpZmMXnFw7MwxEDIA3kzAzAqwNrclk4v6Crk7W5FmkZ6QukvmH4kSppddpCVIQMgiyyIObrTBMXSKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همون همیشگی  @FunHipHop | Reza</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/funhiphop/75163" target="_blank">📅 17:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75162">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">این بدبختای فلک زده رو کی میزنه؟
وزارت دفاع امارات:
ما مورد حملات با ۳ پهپاد که از سمت مرز غربی وارد شدند، قرار گرفتیم.
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.52K · <a href="https://t.me/funhiphop/75162" target="_blank">📅 17:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75161">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">پشمام معین قراره برای آلبوم جدید دریک آهنگ بخونه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75161" target="_blank">📅 16:26 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75160">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خبرگزاری فارس: وقوع چند انفجار در امارات برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 6.83K · <a href="https://t.me/funhiphop/75160" target="_blank">📅 13:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75159">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">خبرگزاری فارس:
وقوع چند انفجار در امارات
برخی منابع خبری از انفجارهای مهیب در پایتخت امارات خبر دادند ولی علت انفجارها اصلا مشخص نیست.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.19K · <a href="https://t.me/funhiphop/75159" target="_blank">📅 13:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75158">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">فارس: آمریکا هم در پیشنهادات خود علاوه بر رد شروط ایرانی، پنج شرط اصلی هم برای مذاکرات گذاشته بود: عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران عدم پرداخت…</div>
<div class="tg-footer">👁️ 6.36K · <a href="https://t.me/funhiphop/75158" target="_blank">📅 13:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75157">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">الجزیره: رهبری ایران پنج شرط را برای آمریکا تعیین کرده است که باید قبل از ورود به مذاکرات پرونده هسته‌ای برآورده شوند: — پایان دادن به جنگ در همه جبهه‌ها (خصوصا لبنان) — رفع همه تحریم‌ها — آزادسازی همه‌ی دارایی‌های مسدود شده — جبران خسارات و زیان‌های جنگ —…</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/75157" target="_blank">📅 13:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75156">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عباس عراقچی در کانال تلگرامی خودش اعلام کرد که کتاب ‘قدرت مذاکره’ به چاپ پنجم رسیده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.92K · <a href="https://t.me/funhiphop/75156" target="_blank">📅 12:49 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">ژابی بنده خدا رفت چلسی
از اونور رئال و بارسا میخوان چلسیو لخت کنن</div>
<div class="tg-footer">👁️ 5.96K · <a href="https://t.me/funhiphop/75155" target="_blank">📅 12:14 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75154">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LMi04jEi0j_E5EBJ20zHttnDtMSGOTFUJjgqqK5tN36DmCsr0n7LncYHmD1k3P2J_xNwhnAapqDqRkxOLvU3ikeJJa3mrZsnwAVZEPdc2MJhfZ2UA0sluhvIkhcLkNOVjVMZWY8Q2ym_ul0kzttJMk0zxCLIKGd8QQvR3a8hJEUJbxiR-kPG7cheMhcD5WJyWIKTawcOYLrAuUuL8SagBlULkOwFZwbjkVxDUDz724x9t4bMsVUI3vZgNjEOEXaZe6tQTBsqed8W8qkfR_LMukVk0AXJUOLZdTpUXmWqH7bBZ1pORDiZyMY862_Y1zCpvp76YQKbavM6y52Z8Amkcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😵
نت بلاکس
آمارها نشون میدن که قطعی اینترنت ایران حالا وارد
روز هفتاد و نهم شده و دوازده هفته‌ست که ادامه داره.
☠️
🤬
این محدودیت گسترده اینترنت باعث شده مردم کمتر بتونن آزادانه حرف بزنن،
اخبار دنبال کنن یا توی اتفاقات جامعه نقش داشته باشن. انگار مردم فقط دارن اتفاقات کشورشون رو تماشا می‌کنن، بدون اینکه واقعاً بتونن تأثیری روی اون داشته باشن.
☹️
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.31K · <a href="https://t.me/funhiphop/75154" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75153">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">😂
معاون سازمان بورس
بازار سهام، انواع صندوق‌های سرمایه‌گذاری در سهام و مشتقات آن‌ها در روز سه شنبه بازگشایی خواهد شد.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.72K · <a href="https://t.me/funhiphop/75153" target="_blank">📅 10:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EWUS4iJPUs1NcTx8CZcx1N4xGaWL8gm8yX4YdkfprXxB6GC8iSsmmamQWe9MCD5SHhZwybflPcfc6pJqhJqlmAAnp4oQ3eUZItsGVeWQxfjJvWAJG0O5eW6utXYkhc2E45h15FDQ2kZKZfIOAlwz12Ael9mm8wFFifIf3OFXDQA_X8fBzQzxfUYTsMnTu0H6Bn5C8Ju7gfK6prPVLU5-d6VqZa7zv1HyfA0w0q2U_CS2CWcV3tWLmqZ5OFmO9RG80LAnJKmZtZKU9GlaycBIoAQ45B7NUP0T8b8UP7xZ2D4ZFC6XFiG6tVDdi59VXgkVALU5BGAJBQIurf-ODJJeAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نمایندهٔ روسیه در آژانس بین‌المللی انرژی اتمی:
کارشناسان غربی معتقدند که ایالات متحده و اسرائیل ممکن است در روزهای آینده، اگر نه در ساعات آینده، حملات نظامی علیه ایران را از سر بگیرند.
اگر این درست باشد، به این معناست که آمریکا و اسرائیل از اشتباهات راهبردی گذشته خود درس نگرفته‌اند.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.9K · <a href="https://t.me/funhiphop/75152" target="_blank">📅 10:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75151">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YH1m40Mir9XeBUbmfTgszTojZ2TJ9GoMUpqe21LvIb9lhAD5cjksuUmGYHpQTMXj7mW2yGg-lJKQGVjeu8DEtjttEETL4YSGLX__AP7YmrQGtTLnGNB-8AJgBW9At7HXrgRMrARZISMsomcGNh9jelHDSwv0Jy8mj0Lwy6KhWTKBflPJ9glsmrgCNFbGS6VuGMLoiWd-LwXPtPeXUMWIyzyypQVYwqcK1YJbK0hq83XTu07D_Rn_2YOABLOEqkrK1GwTimi2vDbCdqtEvpw4oViCqmf0ABh0cA6q8F11vgjnwLLFZBL9UZg191DJkummFE6hjp82PkdRGMZpH-nm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید کاخ سفید
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/funhiphop/75151" target="_blank">📅 09:48 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75150">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jCumKSYCcUWq6Kp4kCgqBMto1nlRpD_hd4pXifixo3S1_4o0-HfnhiUS9MM4xo9E_uv4G_JqnFstd9pnaPFLvuwhimIBrhRRAZNVYqEGNvKUj3fv-Wa8FanKUMu86NlOvOm_MBzkb3qk-yySsEajWFUPy5lfgEWcyUFW1UNFlv8cfnoWMRt8WAKRRymYlEaluT-AM3XV5bwpopAIrHjNrMWsTl1KBqMvU-TCB8zO1OevDXlcgtKradqiNLVdpH3WIhohDe6ht2RDrFvfptNXslH9ZOgb8WpL_bxC5d3ZpUg-M0rd6dh8lOQty-O-WMkcl1EgupP0UCIjg_nsMGWzPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پریشب: آموزش کار با ak47
دیشب : آموزش کار با pkm
امشب به حول و قوه الهی: آموزش لانچ موشک
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.82K · <a href="https://t.me/funhiphop/75150" target="_blank">📅 09:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75149">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">خبرگزاری‌های عبری:  یک انفجار در کارخانه شرکت تامر روی داده است. این شرکت در حال توسعه و تولید موتورهای موشکی سبک و سنگین، از جمله موتورهای پیشران موشک‌های آرو ۲ و آرو ۳، موتور موشک سیلور انکور که هدف‌گذاری شده است، موتورهای ماهواره‌های صنعتی هورایزن و موتورهای…</div>
<div class="tg-footer">👁️ 6.34K · <a href="https://t.me/funhiphop/75149" target="_blank">📅 06:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75147">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KkVlU7nX2rz7_kwo82liQohFGGhNDIZYBHs1zGpqIxWfTsxl6FYpGUHDxdYSBDUL7Vc_fOlYIiCPF02XamPbw2RR_QmZZ8DIrvlI2W7HJ3zue6CU52oQLkHstGoYgV96_sKPWx5NbwfWDJ_4yaHId9HfvCgGA_57enUXwdiU9OY81ZJAbtxJZiufIO2iGTk1tb6cqgX89yL_uBdWbtQ6ZITN8VAMPHwShRtjQID3WlSYBzIbVU6qKmGq7_RpIo6X0px7fxeaGSJvg19vRXjhEUBZ-F2dHn6mw-C1DDU4uh3lhlVB2mIZ3TeGxerkzF1UREYOGN4NezDYkJ05iK2wvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BGJDQD_na5NF8p0qaHwDpwZ4NC8wajQ913Tg3lgB2QgA95d9Lwul4_3HBiGrdTs6amTRKzPpFfWUugeyeoQNcdtKbeTMBdmPDjIwJ5sc0jDcCew8CDMKzapXl5wlFR4Ie_rgAvdr1aHrBIc_DoWsUmE6epDVLgA1CLAiVTd1NDviw7PTJSUrTXt7UCf83Uw-WeiOeqqFG9YTMi2-LmskJ5mw9QoXyDSLe-GF77YhbzrbjzdXJbiMFl72mUfcSAK8CQGUlL8RIeoSJ7n7D2JT-EsixWUvHvr_7tqHUNib5DDaOc4NLWw9EEkSdPcbyej67xmAZqDFYD5PyEBSlTW3cg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">وقتی چنین چیزایی رو پست می‌کنم احساس می‌کنم خرافاتی ای چیزیم.
ولی اتاق جنگ اسرائیل چند روز قبل از حمله قبلی یه ساعت شنی که قسمت بالاش پر بود رو توییت کرد و دقیقا یک روز قبل از حمله هم ساعت شنی ای که قسمت بالاش خالی شده بود رو منتشر کرد.
حالا هم هفته پیش یه ساعت شنی با قسمت بالایی پر رو توییت کرده بود و الان یه ساعت شنی با قسمت بالایی خالی شده...
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75147" target="_blank">📅 05:03 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JGGCiLwLY7blAb6M5qhbwYDz74AjoY0gJTxs-FPjbCSMYsi-kxgW2_48iqJkYoW57gpLw9SDDt6rS1FexsawqxZzCs9KqekhWqJ_WvFHAJJMWx75QP7QbAyyhDO_YbOlWHDfW_W9Zf3cZHoLE1F-GC1-gGOM_nbHe2UVxRattzrYovZCIViOtWRk5uW3l2vndcn6uRYimhShYJa-uvGvaK4yQi8mwmhPAlNKArg9rUKt9ycJkEFHO45d67JZkpcIzC7c7CnjWjKA_UtEA_z3y9g2ApFOa9JFkZ5nTiFT927n-wP0MhCUjv7nQrHI_QOhBkUtJB4Fm-3U6Xi1WNxh2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مجله جدید تایم درباره دیدار ترامپ و شی جین‌پینگ دنیا دیگه مثل قبل نیست که آمریکا تنها قدرت اصلی جهان باشه.
😊
🔜
الان چین خودش رو هم‌سطح آمریکا می‌بینه و این دیدار بیشتر شبیه گفت‌وگوی دو ابرقدرت بود تا مذاکره یک کشور قدرتمند با رقیب ضعیف‌تر.  حتی اگر توافق…</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/funhiphop/75146" target="_blank">📅 03:47 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75144">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">کیر استارمر یا همون نخست وزیر بریتانیا بعد کیر شدن تو انتخابات محلی داره به نزدیکاش میگه تایمر ست کردم از سیاست لفت بدم.
یه حزب راست میانه رو هم داره میاد رو کار که احتمالا به مهاجرا قراره گیر بده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.56K · <a href="https://t.me/funhiphop/75144" target="_blank">📅 02:02 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75143">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اونایی که با شیر و خورشید وصلن کامنت بزارن
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 6.6K · <a href="https://t.me/funhiphop/75143" target="_blank">📅 02:01 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">الان گارد جاویدان باید ضد حمله بزنه
وپن بده به اسم فاطمیون
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.12K · <a href="https://t.me/funhiphop/75142" target="_blank">📅 01:29 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ولی من دیشب چهار ساعت با سرعت نور وصل بودم جدی همش اینستاگرام بودم چسبید</div>
<div class="tg-footer">👁️ 7.07K · <a href="https://t.me/funhiphop/75141" target="_blank">📅 01:22 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">گوشیتونو سه بار خاموش و روشن کنید
برید توی سیتینگ
وای فای رو ۳ بار روشن کنید و بعد ۴ ثانیه خاموش کنید
سیمکارتتونو در بیارید و بزارید تو یخچال(تأثیر داره رو سرعت بر ثانیه)
بزارید رو حالت هواپیما و بعد ۱۴.۵ ثانیه بردارید از رو اون حالت
به سرور شیر و خورشید وصل شدید.
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/funhiphop/75140" target="_blank">📅 01:19 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">مجری: سلام مارو به رهبری برسونید
حداد عادل (پدر زن مجتبی):
من هم از همین طریق صداوسیما سلام شما رو منتقل می‌کنم، امیدوارم برنامه ما رو ببینن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.67K · <a href="https://t.me/funhiphop/75139" target="_blank">📅 01:15 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75137">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mYO7xWCv9TaKZEvr_CM57DJckjnlKp4Ta7jrpRe58TLW7xwJanZ1ASI8uXBfUpiImsXuKUArOb_jlP8_xkssg_Bz__Oje3NRevcUHs-mzIWLOMyTpCugylsRNLlix5MRHT-gbGet7nl9UoAFZL0l-0FVbMIvJybovBIISo0tMcMkkE3kn1hVJ2NARSDNPue7N21PELbnJ-dPWYbnFCOhqd77zoj3zDLo8RzotLG6pfv1xZ9hB-HFbX7zQTjrthPnrh7z3Ehz_FdJm_8INuHkrMLrDMvVDjDsSRhGgY-lKptf5oWve39kipKyhM565TRUJzb83t4SlHRsgv8rdm6uLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V2FmP5T-gJLoKZW5NFe2lTwKzOrDNbD5Q70qvOSYqbCLwfTpn3pmWI2fBXNe0d6dji0Db5nz3fUiv_Et3_cii_DlnIKpOyEKpMhihSIOt0_hENoecAOkfihJsHKDrnK9A7vn6JsBAPsqhG1OO3_HO7zdhhYeI0xM9X8GD3za131d4kS_TwADK6Ed4Ww8wjNQcSpDNq-BWoNjJq-qnsjNg1jySkBHY5HyL_W-bcZK7gTo8Os0KA_kceRG0WwLQ_q8nz9xYuPO3Pu65__I0DUhcbIaRy2VTO8PCHRxWfuyzJuP6dle5zOspRT_-L68rch52goBkM6RvQdXk7TADX4YUg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قبل و بعد جنوب لبنان
اره داداش عباس داره بدون عینک دنبال عینکش میگرده بره مذاکره کنه این جنگ و تو این جبهه هم به پایان برسونه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.45K · <a href="https://t.me/funhiphop/75137" target="_blank">📅 01:04 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75136">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5K09CKezzj8q7g3hAr8RC73KQeIa4eyCG2RDpAk0ihwO30DlImUoggk8xWMT4wTfjMkWDkQC4qO9t0x8o9l2Tj352zv_yc8Q2ThL4ppoLO4i6RYNCdXfTou0naKun9h2HS1PTYr12S2HHE5qhpYFs06krXKy19MIBIw3JZhJzbgaNQBJEqA_tgzU1wRMViJlSyFGzkc6QhD7DrTg65zO1ZgRKa_PGwPmeCKFipDqV7wj2_phU3oYgHwI5eIcf83fw9rjVlXL8XDf5xX-oOxmwQIB-cTqI7Nuo1lnWs21QKJExiFeV1vf8BNL_B95NxR7ND4ifo52VBHsn6WpM2Hiw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فهمیدید چرا صیادمنش تیم ملی دعوت نمیشه؟
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 6.25K · <a href="https://t.me/funhiphop/75136" target="_blank">📅 00:41 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75135">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">علی رضا بیرانوند
با صدای بلند و رسا کف آمریکا سرود ملی جمهوری اسلامی ایران و میخونم.
مخالفا هم نمیتونن کاری بکنن.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.23K · <a href="https://t.me/funhiphop/75135" target="_blank">📅 00:39 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75133">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن  @FunHipHop | ALI</div>
<div class="tg-footer">👁️ 6.65K · <a href="https://t.me/funhiphop/75133" target="_blank">📅 00:11 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75132">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fjc4acxjdsEYurjxm9TYcOgk-sSz_qEEsvoTdb5iXP0U5OLXeVFq3U-_a4h8oGow4BPQ3c4bkTlA2xb1ybzuEE6X5AR61dapnls4sa6xT0sUVNaAa0pVz994A__thkIE5p4s0YW--XDwNcsBSWWVVVco-TKsdZ9CZfn40tCv6WU5zmetkz5MLvRPTpqBXZciLKgaJzrDSm95eL3tHAYuLW8o3QHtJjfi8eMeHG0ebKKl8NFqc5yNc2Y6QmRbH0SmPsHh0HBSHfRQdADYoPnVWz86SShx70S-HFibqotp2uwTe-nhO7OjnSsfeM04sh-pFGqpDA3UFlFZdODH08eJ0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی. این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:  @SonicVPNRBot</div>
<div class="tg-footer">👁️ 6.89K · <a href="https://t.me/funhiphop/75132" target="_blank">📅 23:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75131">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">آقا جدا از شوخی و دلقک بازی.
این ربات سونیک تنها رباتیه که کانفیگ رایگان‌هاش واقعا وصله پینگشم زیر ۱۵۰ عه از دستش ندید اصلا:
@SonicVPNRBot</div>
<div class="tg-footer">👁️ 7.86K · <a href="https://t.me/funhiphop/75131" target="_blank">📅 23:52 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75130">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ONkGvhOutHiMtdgH1z0iDydMHfB4ldCF6luh6kgEKr1ad_TQ6SUJSSALSlB2MPpbt2rxssEqaQ8uFi5U9g0rnruV1zoW-wNJ0RKOnH6E_ACyyzUexKj20y4o-nIxE1GL75zfAoMK8BNgaWMcusLV5dY5YeSbzFA-OyymsYIvrWJKEl8gQXfRngJIpLW-umiERFaDzrlkNZP8Aurn7p8-jyJa-Ppq2YBOe8cGIDLvRNmtp8CotZddjd4j5Q0TZejzWSRHpc3nUOqaEiGTgt6QtZVy_eqqhrvYcdEZBTSIx17c7Um5BGdDSHGg7kjpJdJmmbad8_C_9ouO_H2VGB-CaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ پس از اینکه برای دشمن های فرضی خودش با هوش مصنوعی خط و نشون کشید اومد عکس خودشو شی جین پینگ و به اشتراک گذاشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/funhiphop/75130" target="_blank">📅 23:50 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75127">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWILECmdBnPZCMWIwze5xXNZ8FdzCdLbKZ0fRJ3Vp2A9rGPdSZlfPeKtTY69SIhrIwTiqP6ZrGSHsaeilyRjF-b6YaYa-DxilXgXVvrXqq2ZxIimmTGU704PkwU2IeBjZ0KWf2TrhzIUv-77hDyM38AV4wWhJJn5TLVKVMlCgOOio3Tl74d1SI0kpGm0tSAxwevYwmcabrwlnIIKbNQ90mtzUMQ7raY7OVkXjI1feIg6gzAENQxizBa3P6laZ1H2Y5kzhvCJbbEi9XnwUgtXbJa4jmzLguTQYN0KewW5i_0kzA3toRFOKzNmOssQ4kXcUBP4bq7_6fSOxlRkdSA0hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اکانت رسمی کاخ سفید جمله‌ای از ترامپ رو با عنوان «شوخی نداریم» پست کرده:
اگر شما به آمریکا صدمه بزنید یا درحال برنامه‌ریزی برای ضربه زدن به آمریکا باشید،
ما شما را پیدا خواهیم کرد و شما را خواهیم کشت.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.67K · <a href="https://t.me/funhiphop/75127" target="_blank">📅 23:45 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75126">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترمب: این آرامش قبل از طوفان بود.  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 5.14K · <a href="https://t.me/funhiphop/75126" target="_blank">📅 23:42 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75125">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LGrKNor-WbVbrVjMpKvCHJ8GY6SFORSbnJj11TL9vvybjtcPbSMuo3Hx0E3NQMYGHnw3DkZfESxqC6MjXjWpKoHfZolRxuEvuFiIbsRmNgyafHy3jZVNNruNIV0zZDPE4zMUVKjT-17MMXXKYyqbRtArvzILij09aMmjr2WyobYCuUJy3Xza5dLY8dTyrQmvjvJwsMLeDgayVUh_oV1Pq8c_5FfC5fiQTv85ia9tEke3yUBem_4g9OTwnPRpjVhsDuk2l_wTQNQuT0YVkiWTJKcxom8ZuPHpMtUzu4NnvSMluvykuJ3vtKDm5umBRtfpyn7b3U_XT1nvNjvwxyuIMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب:
این آرامش قبل از طوفان بود.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/funhiphop/75125" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75124">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MtRaczDEIzcTd2H1_l2DJLsExkDFmTYwoQ0gdwuM4ycleTW3CZM7Fi_IWJxuYjtSyudM9WResBXriq41Iv01n_m-vKvmWEa42R_UT6a2do4FxBWFVn-hwn2k1bC3uEBmiNT36B9OgAXlKPo1NnOZBO3lqReMlyRIjxhytoNQj0fchly-ZYQJiwNl-rykIJDpkKLzcGRhCZAR1yjCOrgxF2bewKmUGsyK9-jEOBQUSk2Q1SsSIfPinBpOtSS0lTZqQuwMKPG8WCo55sRNSRwU7beOdx2IkFrF-YqQMf8RclCuI-65nJ1ojMfzH8vFCWOaHeZeKg5wizY_FBM4jqNsbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثل اینکه اداره گاز اسرائیل از دستش در رفته و یه انفجار عظیم با منشاء نامشخص تو غرب اسرائیل باعث طلوع زود هنگام خورشید شده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75124" target="_blank">📅 23:39 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75123">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e26311d996.mp4?token=R1XGNqFVl46lSqLMX2MqvsfJqnICX52LDQX0wUerpy1y8AnpvcBzHvfX6J8UP3WKB8WjLoK-nnNxF2te6Zs9jxIYOA7wySUMG60aVEx498JHeeqf-zKEgl5xx85swXlQ1tSm5imqgAHYQvoYRcEGYth464B3xhK36veNdjmpEtmHbLNqqiuqqt-04Eq_AN8vSDVd0q9Y-4BJkURZrtVs-y733H4RKXlFLspPfc7vx4eiRWovOGMj-o1Oe3iMxLbjPKEvFyOalZi5kyKnQ_e1m23aD_A3VSGMU6BMWjYEKAvFOlzUz7iuZiPXMkpYPyskyjtw4hFJ5rSc3VMYUhCgcQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e26311d996.mp4?token=R1XGNqFVl46lSqLMX2MqvsfJqnICX52LDQX0wUerpy1y8AnpvcBzHvfX6J8UP3WKB8WjLoK-nnNxF2te6Zs9jxIYOA7wySUMG60aVEx498JHeeqf-zKEgl5xx85swXlQ1tSm5imqgAHYQvoYRcEGYth464B3xhK36veNdjmpEtmHbLNqqiuqqt-04Eq_AN8vSDVd0q9Y-4BJkURZrtVs-y733H4RKXlFLspPfc7vx4eiRWovOGMj-o1Oe3iMxLbjPKEvFyOalZi5kyKnQ_e1m23aD_A3VSGMU6BMWjYEKAvFOlzUz7iuZiPXMkpYPyskyjtw4hFJ5rSc3VMYUhCgcQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من که میدونم اینا دنبال کین که ترورش کنن
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/funhiphop/75123" target="_blank">📅 23:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75121">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">به گفته خبرنگاران فان هیپ هاپ نیوز پدافند تهران فعال شده و درحال درگیری با اهداف متخاصم میباشند
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/funhiphop/75121" target="_blank">📅 23:29 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75119">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">هم اکنون صدای فعالیت پدافند در آسمان دزفول در شمال خوزستان
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75119" target="_blank">📅 23:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75118">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZYmFGE1j0B1YnF52iAvRt4k3MFwBHvh1hZ9O7v7rXSSnXMKkKQuJx9ZHP4TBM5uMujvAAgWkSdeV8015DaYMbdFmjAdrYVUP4r8_sIPqa28yO7TqJuI5JTxJgQScdRKzEZGaXUFtjHFRS82hBnPC-KgLvWw-Ff74INVmu40QbflJqkBX6DHGMCGFO3nQgcLZ_AUSMYJkavIocyNA8wsTpkJmU3wrkviH-CaK-3Ees7EgmUcc2a6N8KDArJSxdncrZ651bVZGH2j1Dt7btOP4a-y0tRO2LR9fD2boSje6NO9HrXHo4ij0Ht5hEqNEmB1jXIqSPSaqnhejR5tJflPYeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمین اکانت توییتری محمد باقرشاه قالیباف:
جهان در آستانه نظم نوینی ایستاده است.
همانطور که رئیس‌جمهور شی گفت «تحولی که در یک قرن دیده نشده بود در سراسر جهان در حال تسریع است»، و من تأکید می‌کنم که مقاومت ۷۰ روزه ملت ایران این تحول را تسریع کرده است.
آینده متعلق به جنوب جهانی است.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 6.08K · <a href="https://t.me/funhiphop/75118" target="_blank">📅 23:18 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75117">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">رونالدو از روزی که اومد ایران دیگه روز خوش ندید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/funhiphop/75117" target="_blank">📅 23:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75116">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">النصر فینال سطح دوم آسیا رو باخت و کریس رونالدو باز هم نتونست با النصر جامی ببره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/funhiphop/75116" target="_blank">📅 23:13 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75115">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">درود بر رهبر انقلاب اسلامی ایران
مقامات امنیتی اسرائیل ارزیابی می‌کنند که مجتبی خامنه‌ای رهبری جناح تندرویی را بر عهده دارد که با دادن هرگونه امتیاز در مذاکرات مخالف است و به‌طور فعال در حال آماده‌سازی برای از سرگیری درگیری‌هاست.
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/funhiphop/75115" target="_blank">📅 23:06 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75111">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اینهمه خایمالی قایدی رو کردید تهشم سردار آزمون کیرشو کرد دهن قلعه‌نویی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/funhiphop/75111" target="_blank">📅 22:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75110">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">مهدی قایدی با شرف هم که هستش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.7K · <a href="https://t.me/funhiphop/75110" target="_blank">📅 21:59 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75109">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اسامی ٣٠ بازیکن دعوت‌شده به تیم فوتبال جمهوری اسلامی
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج‌صفی، میلاد محمدی، امید نورافکن، شجاع خلیل‌زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق‌نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قایدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپو
ر
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/funhiphop/75109" target="_blank">📅 21:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75108">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=h-V8aqh27thZcOhLPIkLLpUKhmkba0RKbJcG4VaHovTJZtCh9DfYYgSt-17c6McylbMouYNr2_dYAaC3mpnUg7z-2-FnbdLU0-D4z0HYZapEvk5yvrHZpr_-Wj-y02O4xcsZ1BIUJqmrySAFYy6MZb2asI9XOJ21eRLUy7u-3C0D_qqX_2aHc_hBMkTQscDv1WHJFE3qqGc-yC-wZpLYzcE0-thhW3igIp3PPkwXPoBs0c8_F1h0xumYXapN5g0Gd72tDxCGf33wF1IeikuADGm-h_r0C3BtzK6OGz9xYx70dII2-0hGL7C40RF5Vg-y4NMoxRf0R5BKhJuJ0IbFiA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a985309f1d.mp4?token=h-V8aqh27thZcOhLPIkLLpUKhmkba0RKbJcG4VaHovTJZtCh9DfYYgSt-17c6McylbMouYNr2_dYAaC3mpnUg7z-2-FnbdLU0-D4z0HYZapEvk5yvrHZpr_-Wj-y02O4xcsZ1BIUJqmrySAFYy6MZb2asI9XOJ21eRLUy7u-3C0D_qqX_2aHc_hBMkTQscDv1WHJFE3qqGc-yC-wZpLYzcE0-thhW3igIp3PPkwXPoBs0c8_F1h0xumYXapN5g0Gd72tDxCGf33wF1IeikuADGm-h_r0C3BtzK6OGz9xYx70dII2-0hGL7C40RF5Vg-y4NMoxRf0R5BKhJuJ0IbFiA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">«تروخدا یکی ترامپ رو متوقف کنه» قسمت نمی‌دونم چندم.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 5.54K · <a href="https://t.me/funhiphop/75108" target="_blank">📅 21:55 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75107">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">عجیب نیست دفعات قبلی کسی از حمله خبر نداشت اما الان همه میدونن دوشنبه قرار بزنن؟
@FunHipHop
| ALI</div>
<div class="tg-footer">👁️ 5.64K · <a href="https://t.me/funhiphop/75107" target="_blank">📅 21:51 · 26 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
