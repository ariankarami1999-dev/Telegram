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
<img src="https://cdn4.telesco.pe/file/NeDnU-n1HsV2ECaadhJeWzAy7hxOTmaza1KHJwzd570GgiL7PbNbmXiYrsedGnaMlfVeBUmYGAXCE_Gnc-QNRvFfR4SArASGdPL7X3Sshfnhm9AunJie9y3a2h4i49XFOhoizDUMTU7k1X6Hw0p3VGagb5NAja6-oBbTxA_i3z_urUKdtBvLTlAiz22Pb_RkBx6qZTCxvCbAoAold_GQbNjSXUnsipX1nRcrlT729wV3YvS_6s_TMOcn5Kk-LS2_JSawIIS0yXigr4oRwY3G6A_i8g5C6AD6ThzKzHtsS17yF5Jk0HvRDVc3HXesTGal9dRo9iSt4cc41wmdP3Y3EA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 442K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@adspersianaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-06 12:39:35</div>
<hr>

<div class="tg-post" id="msg-30603">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HZzgBWSPnWswPX1CBuzPZ23tbw5i2NIl8W21trGfHFtfC5NBZJCAEnP3jzhxc3h3Lms-FgwYF6jmNwj2YZghos0Bcy7KZLpiYLoUkBtuM5VebHcSnMEADQWyp-vWEWTOnz1LYh-6EXFFAa6EkgQliCDgrs3tkUKk3meVaAVduA8jCl-TuesGKcJgQwpkRvPcGlbvSbzgeHaLE0o0RqrYheqxE86jO5C_t6kKKTjlWofp2I71owaoDl9P69ThdkTwmmNpK8xiNP3rE8Vh8GXD68PtKgowQrW8nH9AbzWe2_M60Rhm4fl6b6WGrVy7bSd1GB99FY6pKD4zP_bRFRKhHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید شد؛ حسین عبدی سرمربی تیم‌ملی امید از هدایت این تیم استعفا داد و از این تیم جدا شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/persiana_Soccer/30603" target="_blank">📅 12:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30602">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adyOfgFGFnJjuh8UuyYPZpdAM-zSzWck-KhDwJjgqSAKlAPsDc_8ELFKFsjwaF0fIwgpKL_-Ome5ZIRV1D8OYRwS6jgnp87AW5Vf8IILe11j6EIk5yTzDytGXt9nkNnBV1esFc-_Zcr-uoj3bA5GhEgGnI82-ztMrRw__bVIHuf61WVYfYbQEGhZ-NO_J8bvl968tFGlJSH5n--naEa6EfoKh_szHRaGswtGPP46feQrsKKZL8M1EQQ2-eHST1vrDr2pm4ratw3HUV4C1UMFL8nborCDL3qm-6IoS9KO2fP8tO_IEPZsEuUSjMYrgvyRQJ2EYMhOAjFtr56XkJKqaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سپاهانی‌هایی‌که‌درپایان این‌فصل قرار دادشون به پایان‌میرسه: محمدامین حزباوی، آرمین سهرابیان، هادی محمدی، احسان حاج صفی، ریکاردو آلوز، آرش رضاوند، سعید واسعی، مهدی لطفی، کاوه رضایی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/persiana_Soccer/30602" target="_blank">📅 11:40 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30601">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WO9SF_tkFSeUwNPSLGpeQk3KEIO7gd-jqV-crj_BGhDwpO8_Y9d9emD26JS5hhMCWIQh4_58Mz_ek2_VYJgIQfaigZ6mbIDlZDQRLuNTwMz_Bg9cmFuDiQbm5-PEhWsR_SPC0L4m1neOB6D6hbbNr_fyF9J4QnESoGQDMh4Q9fGIWhyg5mvr_ePW1GsOmo-UfLTp9iW7yG3E2jcYoyioYZKdOnxvxMZkRKbyvsOpQgcjPFD8y3grzTskpkZ1R4qCCmz9a1OMR03zW-qQy3DAqfDX850icSbx2oypQqFbiDvQA_Kk9XRgz9wbJlMgzguJO1G60Rq15Jahyc2aJ9B8hQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
🇵🇹
گل‌های‌دیدار امشب‌دوتیم پرتغال
🆚
نروژ در هفته دوم لیگ‌ملت‌های‌اروپا درشب استراحت CR7
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/persiana_Soccer/30601" target="_blank">📅 11:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30600">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eUEfx2qA8nTegU2YF4PhFGfTm9amHAH-G1Md5r2j3udNUp90gyICaJTOn9u3CAMablujrqlO4Le6L7SsOCK_72F5Ly5cP7WVheNWZEtDfDKFrlBCLLPbLUzo5nmLwoSU47o-uUyPxV5uf4PwjVX4S6unuPtfoOL7R4ehHBIkvyL4l4okH1hieiQBhGFYgTQjhmeRzN0L8wVfHb7BY8OW7or2DMHA3Z1qznzU-_Tl_5pfy12Os0KKboPd0gCI6iW2fNAOgujsSBrt5PVtaP9S0iNuZwDatK4G-4gb-YteR09ExF7Alt28euHtzH8wAVj1HwKjynL1MGe00qAkNY5iew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
ادعای‌رسانه‌های‌ازبکستانی: آسانوف ستاره جوان ازبکستان از دو باشگاه تراکتور و استقلال آفر دریافت کرده و نیم فصل راهی یکی از این دو تیم میشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/30600" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30599">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qPgl5VQzWV_ZXNXIgdONXDJ5KMceqFf-O52striaxCIgXJIfwyAPJ2mLMYrpL1JavGKkEyG5k16sC6FLu2CUXURm7HiKvWXyuHR3Kj9nCSmMC3HsVuy4rmYta0gEEOjuJuLlwBBxZqMS5MiCPgrNAyUNBB8Ce3Kn9egalp4raIPcfPTQh_wwozH7Jn7HMZZ8ja1kz5ZUZFbusqPXHmSqtnAHFOPRH39O_W9sKEchqVZWsP-wr6S_hc_Ifa_2RIDECzr8WD9IsopxtVdv4K2_BY4X3QrAUs42LjwswaWtcVB8oQhtH_0XDXFladdO06YwxiCLAPZPQFQL8k1RDS-_mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هایلایتی از عملکرد درخشان لیونل مسی در بازی بامداد امروز اینترمیامی در رقابت‌های لیگ MLS.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/persiana_Soccer/30599" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30598">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/persiana_Soccer/30598" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
#جدیدترین
نسخه اپلیکیشن بدون فیلتر (WEPARI
)
🎁
کد هدیه 100 دلاری:
Sport100
ثبت نام آسان
☹️
✅
r6
🖥
رابط کاربری راحت و سریع
📲
کاملترین برنامه موبایل
🇪🇸
اسپانسر رسمی لالیگا
😮‍💨
بونوس
100
درصدی اولین واریز
💵
بونوس صد در صدی واریز یکشنبه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/30598" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30597">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🔥
هنوز توی
Wepari
با
این همه آپشن خفن و ضرایب فوق العاده ثبتنام نکردی
⁉️
😀
😃
😄
😁
📌
بعد میاید سوال میکنید کدوم سایت معتبره
✔️
🎖
اگه میخواید توی شرطبندی موفق باشید و درآمد کسب کنید در اولین قدم باید سایتی با آپشن های بی نظیر و ضرایب استاندارد و امنیت مالی بالا داشته باشید
🙂
🎁
کد هدیه 100 دلاری
:
Sport100
🔄
همین حالا از طریق لینک زیر ثبتنام کنید و وارد دنیای جدیدی از شرطبندی بشید
🆕
🌐
ورود به سایتwepari با فیلتر شکن</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/persiana_Soccer/30597" target="_blank">📅 11:15 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30596">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BsfpvXekcQyqcdDLKxeaOUtQjHqO4dLxK1wptZZSGITqcdRiO2Gm7S7ORXm8WnaUm0JAjM_b_ByjsX27oqmh5w_fpuwiw6-Sjsp-HWut6knBRc9gK5oGVLbF5ZjRzOPs0I6S0cjbbltCOudwmK-yF-9SdrfNwiSLFe0Zlp3P7P2QZLcEHxBsunetyemjOt83zwAJgQV2w-ygzsMmT8mr-3EG8fghYyGQsoPGrduK7PcMzlw1OTZGU64UceDIHpk1yI1JS-KmAClyMVpWEzOeIgczhRjGpiiHsktecvYThZsDXOR5LVnvP-k7xdZ1j8bAot40ixQby_ZZ2gqE5ATzqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔴
🔵
سایت‌چمپیونات: شیرزاد آسانوف هافبک میانی ۲۳ ساله‌ازبکستان‌از تراکتور و استقلال آفرهایی دریافت‌کرده و احتمالا راهی یکی‌از این دو تیم میشه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/30596" target="_blank">📅 10:48 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30595">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/njbGmoqtayDmQcGMBco6xv3OPX8oyo0MqdMk06pRTqlWDLcVYxic15fgKt8vPPqjAv49oMFYkN89olP8d2VVQ_DknmvpJSxDjuX6zlEpaeO96sPCUjhdvTQz8phz94Wxxy6SHvAFboyxZUckabYHT_g_slBS73cs0eJcacmyC_9clnBvt2onSVsHsA-jlbPoB88lCfw2mtmhmGXwrTgLomdHjuL-Edeaqdo0POTSiHbERhLTSFP_8gH5LRLBWFYbnKp11NGXsfCeFXF96hvsNRBQO6uYFlFC0VlCj6cWbI36hHm2sfbm7yi2_1QvkiaZQScruTb3ukwHxFhk-OkVbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
استقلال درپست‌وینگر از بین‌ مهدی‌قایدی، یوسف مزرعه و یادگار رستمی سه‌ستاره النصر امارات، فولاد خوزستان و فجرسپاسی دو تارو قطعا جذب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/persiana_Soccer/30595" target="_blank">📅 10:24 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30593">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GFaYN4ac8dELxEUad6ebRlc0aRTwaJKahX7UERe0TEzVLbQg6vEKFfuHN-ximO_6YNxfD8EENSw2DVBg3D67MYG4o72qPCT_5ijYno_4nCSPx8frpYGUD-DpYDXc7WkmFlJFd5mc8x0XW7H4ZZ-thGmGNrHRgpOcUXrR-eNIVpSH1TwRa8iJZPeEsMhVcESpXgdqmx7PX24bUQ5ackR0OA3Dnvb4MrLbYShtJPHQhMNdCKdClGDU06de3Vxp2njV_GQceWctjlElO_o5OiBRIGRaDvEffC1eFhDHARzy30dDhoKAmOfm7Tn3ayqZkclWDQYhcVGquW2RDyoGRmHgbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b3c75c1227.mp4?token=iKgJhAo1SilNKLybDujok1p7T8gectisaIC12FUxPOk1k61vnSoSNwHHovOfStKbx4uyulryzYp33vTsn27OgPP79iw6rdBhjviL60eo9B500JdxJHpc5JrCoSBAQIQiFjTUV-fwEGZMiqJG-FDKrKmv0SN5XchpA5D0ZMOhw-c51qjYQB94mjmA-eM7P-A6RVBGRcQrMX9I6i-zOjx4xAIE_j7_-g6gokQJUykv5iRD6OXfM7yQYQGP9loYfzI10imbh3cexpDPiiGDrbOf9qkDAjQXQwFBxBIk-HSbse0PKeKLxia3VHYWWjGmhftGbR279Lb90ut8w_-l-rhh8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آیدِن‌اسکپیومهاجم ۳۶ ساله آنگیلا که موهای بسیار بلندی داره در بازی اخیر این تیم در دقیقه ۶۹ به زمین‌بازی اومد و دراون مدت کوتاه باعث شد که دوتا از بازیکنان کارت قرمر بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/persiana_Soccer/30593" target="_blank">📅 09:59 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30592">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelKlhLTFX4x-Z_VdnaYoF6ZYC3PvGNUZavrrM-82hkOtMrKu0NPSpWb4nvUGxSc4gz2UxQK4-B5Avkg3-40eHyeKEp4i1Llo-WawlMvmtIM3GYc__nJIuMb_BShnVr3TxX_ky_-swOTrV5F8uqEslQPY4Of3JweH5ReJkSJ9AW-FfGbB6iLORt1p9v3pHLCsMM11Oa9411pafjxjssTDV1Denb3XwvxFz5AoWB3XnzXXcy91IxJ6oJ-ISiZEprnKQy_CK2Uv2JwxFulQImcn3cGF4ckU3oSsJoIQ_14VRt0LqOJu9WS10PkEmbvgWB-b2L2pqYMhzckrE3iGUutjfcsk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe3abfdd06.mp4?token=CfUn0ki9yAqFFXDKhvfFJ0_WqYU6ifUvr-MN2zTRlXuAWFJDSWL7V5GbXMMwvU8TyKoRrTmkoTOrYJuIKcww_DZRs3NHh9y4xNW73SpqaLJiAtgg0Q7w1flycaHq5aKfAKjDRXi4oylZuko54Rwy9V6WQCcW0il3qmLIG3dIk_rd0JoYIZDMdAoyby4A683IPKgOtQ_lju5lsmptbG6kzfAzDUFhkFTuUaLW4QYfkhhjDNJ4_TKBaAb2Cnwybif6-hito31oV3LeqQrp0uj5PgTOwNb5QEIRef2t6tqZwjrQPoThLZpRqEyUgLHmTZG5bbuycbk5I_tx9a2nKBKelKlhLTFX4x-Z_VdnaYoF6ZYC3PvGNUZavrrM-82hkOtMrKu0NPSpWb4nvUGxSc4gz2UxQK4-B5Avkg3-40eHyeKEp4i1Llo-WawlMvmtIM3GYc__nJIuMb_BShnVr3TxX_ky_-swOTrV5F8uqEslQPY4Of3JweH5ReJkSJ9AW-FfGbB6iLORt1p9v3pHLCsMM11Oa9411pafjxjssTDV1Denb3XwvxFz5AoWB3XnzXXcy91IxJ6oJ-ISiZEprnKQy_CK2Uv2JwxFulQImcn3cGF4ckU3oSsJoIQ_14VRt0LqOJu9WS10PkEmbvgWB-b2L2pqYMhzckrE3iGUutjfcsk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
سوپرگل‌تماشایی‌لیونل مسی فوق ستاره 39 ساله اینترمیامی در بازی بامداد امروز این تیم. این 931 امین گل دوران حرفه‌ای لئو مسی بود.
‼️
این‌کاشته 76 گل‌مستقیم مسی ازروی ضربه آزاد در دوران حرفه‌ای‌اش بود و او راتنها دو گل با رکورد تاریخی 78 گل مارسلینیو کاریوکا…</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/persiana_Soccer/30592" target="_blank">📅 09:44 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30591">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=jfit6_Pjx1abThf4eLWRHcykR-bynWqXFFaouYSkGN3fffzqFEw6n7fYJdjzW9JC7vvjpstjdm_4dQwl_qIwHMR0y6dSyBLsm8KvizE2w0TPv35CxQ7HUs2CX-w7aN1W3kbfIeo1OjeU9Mj-eiEZ04vXhJsZFq4mOjpgcaNpYhzWPGwNNYO5DIH4J1asHpdXDxsWvl8kHyOChQX8DMoTyV3ifr_DnMFlB3kW2AbwyEQUagBdQ_vvDmf4AIKlQfPB1X1CiQVmWMiJxelvMk_C1P6DSj1EWVA_ErDzSequ8v7OHxZqlv0xVCC_TyjPD-CIb5FVMNFjfrEbsWLmIiKWwA0eg_wqLnfskmTKIsXfUK9aif33zGHfWV-h_z5U4t4LCReUuzFQ5-YJOTSDvuV_B-asFdqPMLpaZLt-KwYyWWKnRifej_LjFh9u_AiulmNq7rhPkjS9waJFK0Xt6PtTl8u25eVks5OWpGjEWdNgnAaKX8QXkFo6sLlI-Y6GU002O0P4ftE8zlheluPouiFwFOTnX0eI4MqtjsUkLtTFTWRNayhXwN-IO0UKMl5L3kujVylpl4-Lj91sVdoIdUR-UO4OwJh-LdIAbT6nwb-3k3Cr1YYitcfkh4gYYh4Uiv4UDhuj8EQCBdWPtjNCFHPRRyUnmbjPoTUERTz_c9vYwMM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb5b7e2b5.mp4?token=jfit6_Pjx1abThf4eLWRHcykR-bynWqXFFaouYSkGN3fffzqFEw6n7fYJdjzW9JC7vvjpstjdm_4dQwl_qIwHMR0y6dSyBLsm8KvizE2w0TPv35CxQ7HUs2CX-w7aN1W3kbfIeo1OjeU9Mj-eiEZ04vXhJsZFq4mOjpgcaNpYhzWPGwNNYO5DIH4J1asHpdXDxsWvl8kHyOChQX8DMoTyV3ifr_DnMFlB3kW2AbwyEQUagBdQ_vvDmf4AIKlQfPB1X1CiQVmWMiJxelvMk_C1P6DSj1EWVA_ErDzSequ8v7OHxZqlv0xVCC_TyjPD-CIb5FVMNFjfrEbsWLmIiKWwA0eg_wqLnfskmTKIsXfUK9aif33zGHfWV-h_z5U4t4LCReUuzFQ5-YJOTSDvuV_B-asFdqPMLpaZLt-KwYyWWKnRifej_LjFh9u_AiulmNq7rhPkjS9waJFK0Xt6PtTl8u25eVks5OWpGjEWdNgnAaKX8QXkFo6sLlI-Y6GU002O0P4ftE8zlheluPouiFwFOTnX0eI4MqtjsUkLtTFTWRNayhXwN-IO0UKMl5L3kujVylpl4-Lj91sVdoIdUR-UO4OwJh-LdIAbT6nwb-3k3Cr1YYitcfkh4gYYh4Uiv4UDhuj8EQCBdWPtjNCFHPRRyUnmbjPoTUERTz_c9vYwMM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟣
🇦🇷
بهترین گلزنان چپ پا در قرن بیست و یکم؛ لیونل مسی فوق‌ستاره‌آرژانتینی با اختلاف در صدر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/persiana_Soccer/30591" target="_blank">📅 09:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30589">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ALpMGnodzvG-YuHUB-WeUoC3kbM9eaAZc-PByh5qS4Crew7mLYijPYJQH38hIMxxDB_mgha7O6M7YqK3tnzEZFvYwWpOz4dxwj1Q06u73U0-O04BFEtMJTOBcatcF3sn6QGZmWhH8hb8GsIL0zYJqssyXKtg1XwD1nsv14SNsQsbJsT2DiLJosCOgIMHnmHJWeZZTXy5kpl_ieShH5WkuTvzBLHvvGUEODwO_OMz7QogGIRpRJqMuVKNqBoFwlt1BZW8MYz-oD2WWU5npmHWDPCMojppwO9PaKbTr20mvBYoLC1E2pNT16_WwxFjawEyCVSWktjoPPJqkdzWi_r0mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l1HhnJ5CZLiezPrmneSRk5Nw0Sa9_d89Gk5nGoNGPDTCuIn6SGoADuXlR_6Fs2DNhoA0ZyBMMvihabIhXylt5X4LtEI9nciEP_g_1ivU2v-7iJ_1Ze-59H0LpFDxy1CExz8LmeRU_UlcXSAlfV_SJf8EV-YOHXPxWVGHi7x6xUk_oRkizrM1Y-m90fmPBAS1psP3refdSq6uAIryF-33__VQ2ygy4x37MCniaQTe-xTIPuFlmFYUMp45j5kC49wL7hvTKfVMxYUl6-7Q_7-0efWAZGZJXilZ7EQlMw7kkxGrRKKziG88XgMy_YR_iwZcXKDDPagJaWpunGOYKZ5kdQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/persiana_Soccer/30589" target="_blank">📅 01:42 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30588">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CLDbd9pw1PojICQXadBrd-zYBPSaupVkH7SnrhJceLwm8aDU5xYGF9IFQb3kW5fcyDwdvj1ySp-3ZYY1Hi4KgiCW8be0Od4sqQWeZPnINYxVSMBsQlVkMJQev1x7q_G8cfhQ5FZGdmASPMH_qRansZT8i8Sgf-KoRohGYkFXWRXcQ4U16KzheWyk7hDp6xzAmqYhA3kd5agyRjXnO9SmFPeViYukAj3dgPG5Cl1cqzmwq_Yfkbp7U_Mqoa3ycPXJgyT_-7ZN84lU3oRH4Pld0cm1DU2jdHQKp5PuHR1tqVhwszX2JY27h15FV7nvi4RSf7hzoWvymKPgierLNqGu9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🔵
#تکمیلی؛ طبق آخرین اخبار دریافتی رسانه پرشیانا؛ روز شنبه هفته پیش رو باشگاه استقلال 70 میلیارد تومان به‌ملوان‌پرداخت خواهد کرد و با ماهان بهشتی هافبک تهاجمی 17 ساله این باشگاه قراردادی به مدت پنج سال امضا خواهد کرد. تمام توافقات بین طرفین در روزهای گذشته…</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/30588" target="_blank">📅 01:26 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30587">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YPWWaE3aorjXuKiynQRW5jpEd07BywvZVZDLUsEY2DzJeYvDEzGBMHymJph8izK2y0tqP0gBOkQm7Hxhtl5Qkq_90e7ksLGHddnsMgoZddAj0eO5lhXzVKJyLhMRGyGS10dEgdDkAqCH50nkpD_mSWoFLPNkKhVcghHBNU3lWsRFL7R6bGJytypUToHYgpgoTsD0SKyHg9js2Z_9NkhMQa7E7qB12sXmIJ27dl5jEgNVy7b5FgBZwGnoVd2BZucheqQG3ZL0wQFAi323ECUvKgyue1PzMC2CKXNQ3DHUHy3QYziM_SEVEnkoRhn0dbe-E_FPEemfBt8t5QED6nL4rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نگاهی به عملکرد و افتخارات شش کاندید توپ طلا 2026 در فصل گذشته فوتبال اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/persiana_Soccer/30587" target="_blank">📅 01:22 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30585">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgTwp3C2adBwlljqs9InR1-cWWXSiRSTj9UCzHhWCeVTgCP3bQ4ijrJq1VHsvUfLUlBSlj90XijW2WoFoPYsRa49CDbBWmfJzH95vXAd0tpWLZQC2qweE6U7w_TfDtJglU6xP3rf1VlCTtkA4D0DncasgYmLSsi6liwRUuR3fZNCwtMY6qp7ffyLVyYONv8n9JBetGuc1mmEws-o4bFM3o6vBn5rs8ySAtFpjRSULyh8d1HyXQIJLu6rUXJ8TTZCmdq_1cbwWm-30ZLCHyXE8XERd9bGIGABU8zrQw4_uctysb9NtvUGQ_L3Um6YWthlyLQXZfl0bZRP9vZHa7zDHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌ دیدارها‌ی‌‌‌‌‌‌‌ امروز
؛ دوئل بلژیک - فرانسه در غیاب امباپه و رویارویی کره‌ای ها با شاگردان فورلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 40.4K · <a href="https://t.me/persiana_Soccer/30585" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30584">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eBPPR_ba9DwwoCvJOzgYzOFUcZPiqpdI5QIxg5QpM1jtXrJbYRPcHl2RKMOfHYoQKtd5j8ffFij5t_6Rd0VOKeVIdktINuRKzTZjW5-qjMLcuAcZPctkZTXLu1RSR8ASp_urhnUYimMReNuUzA69vd937avcF1wPKfQvyQ0jnbdtpSybb3GBWJdR01jLUhogPL0tTXiDl15XTpaeOKeUklHeT1cSlgCGcFA3-_idYF8xtZgHVtH_t69nyhnxKycfwMtmS0vJOt558hcVQqXEQ7EN8GrVQLXvVt3Hv-MTGljmztgwmLqjttqgMFSgyuU3fSlNkCcTJ9x-eizOfLE-VQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
اولین برد ژاوی با هلند و 6 امتیازی شدن پرتغالی‌ها در گروه با برتری دشوار در خانه نروژ و شکست عجیب ژرمن‌ها با کلوپ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/persiana_Soccer/30584" target="_blank">📅 01:20 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30582">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.4K · <a href="https://t.me/persiana_Soccer/30582" target="_blank">📅 00:30 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30581">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XeSefepN5_G_5ipAv9WFg88VGQ-X-eNmRU0ObVeDseaYlI75TaJ2vi01x7dg1r3hKuCslIhzRyasqCdC66FoX4Ehx5M1H2rAoz60VM8LlkL0tHWWD8FNh2vtHF4lK3diTkS5Fc6wEja569b7IRWGroy9cbhZrq7OWPdbNpPSFwj-Zyh9nNzGM7irlUZkyg-k9Tw2ztwj9EZjK6_GyejOKb3ev886lST1WBlBruQod1KfLKtqEEuQd97NJOMUiHOjwRQj-i9J2HF3BzV-NV-tEK1kj2xs0VVzDHtmTwWjBu0-mSgJ3aIwwZ16OjPr4ns4z43t42fmAIptaLNZLiW9BA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
درهفته‌دوم لیگ‌ملت‌های اروپا؛ پرتغال در شب استراحت مطلق کریس رونالدو با درخشش گونزالو راموس دو بر یک از سد یاران هالند گذشت. آلمانِ یورگن کلوپ هم یک بر صفر به یونان باخت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/persiana_Soccer/30581" target="_blank">📅 00:27 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30580">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLbdzfJnKqhkpI0m6gkBfR9bc3j93Qyt533siiF78sZc359Ii1eNPDdoHgBxy01y9LydhClEE9to2bQ0dzqCDqJKIXPmWNti8j7B2-KpRxdC1LHlI0riaBWiTvS2fVBLiKBtZeNO9GN22NKwN2mUNI2WSoMC_dBEQqdRmu1ezjQB_BflJ5F6HsNv8r43uT4j8p-qBPoo3_EKd4bLgSJqFz2UIwMX2HE46YIdwhqKgFjuiJrHoQYe0yxIiJ6kcIqs9hxi7eMWpj2q8wCdJtX47Cb6mi9WUQ1U4NEf9LMYJFu8gBGiV1TTjJ4arpPw00JmuDp5fGzCFsJdBIKo7Jqafw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
خورخه ژسوس سرمربی پرتغال در واکنش به نیمکت نشینی کریس‌رونالدو: رونالدو بهترین مهاجم و بازیکن فیکس تیمه؛ امروز چون میخواستیم دفاعی‌تر بازی کنیم و کریس رونالدو 2 روز پیش بازی کرده بود تصمیم گرفتم امروز بهش یه مقداری استراحت بدم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/persiana_Soccer/30580" target="_blank">📅 00:17 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30579">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1j7lGiUumkkmO_4rnORn6kRLJ34eHemfONZVmLcrAwtZyJpNcYrLr1UDMvfPu9XehDyC5kcwRW38FRv9aslJlm8n5FnPZ8hV8TGOD3us2vcsJddL08Qku_Y3vGl4DL2BN-XAmLcySt759Uv36LQXkg51HshTBDxzXgPNmcZAfnKABk08my2S35wRTcBqtxK2Dn64vG6WraNEIe01ibeC8vJnfKFNfxso7VzNdkDHtYHzUxM1jk1EpOn3_9w_WN7iP1kDEBY5wrwLatnmQttxzxIqTiE3o3S8QMCy4lqJlar8QbJh_N7rXIiFL6ey43mNG73cfW941U4epXmlrcmRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
دوایت‌بایکس‌فوق‌ستاره‌باتجربه آمریکایی که سابقه بازی در NBA و لیگ‌ برتر ایران رو داره با عقد قراردادی یک ساله به تیم بسکتبال استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/30579" target="_blank">📅 00:02 · 06 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30578">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dEHN12W8beprAraymzAikEwvJqWzmA0Qc1_5fax6h29nV-lFeSNJUB84DDlFvpVZ_QDssee237e7kJ53cEQUEvf76F5KTH8ExXDzD6w3ZVcBtJUs1CbAMxSIdliBtpyy9rW3m5BSHGWiBdfO4uYn4S0iaba7ojOkzN13dyVOGaboSna33Dza2Zc6iBvYTas_IYeY_7PBrEHNPFjLLRZjsKrvsfD-pUhi524nNmGaL5unXJJFqhyNlpmcwTMlMWfDMLzqFY8BI59OUo8RrPxy_eaOUvr9yKhJmaMaY1Fu1YjRrS8kHkstUQAtD1QiW9k4w62YQzREPokoB5CpVuzM3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پیمان حدادی مدیرعامل تیم پرسپولیس: به یاد بچه‌های مینابم که شده جام حذفی امسال رو برگزار کنید و اسمش هم بزارید یادواره شهیدان میناب!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/persiana_Soccer/30578" target="_blank">📅 23:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30577">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IV79CUWQMDfYfZIkVSJUzfS4FrXlab0a_7XOw5P_GFGgXa-t9vpKBCtHCN4erRDQxl7TIcx9PhcyWY22mLQTgRT2yZ2n5mVyGqfA8YFBKiP_Ht_JYCCKWu8Gy_Y257k-yRltgVb2KlcWPADpcQz6di93xuUVU-jYT_Agluu_h9WuoB5KntHyfgUN0VwsVbwmw5sVSt4E7XPSHwvXvWHUl66E1Rx1Oy_StRBzCU9Pt_47D-JC9HeBV4jB7SXXyi69mTH0Fo2QwrcI9UAHADaR4GkalfDZCLlHPgrs6E8_0mM8NvYWPU_u9VUAb9IxQsoD7-lkSo5hyHdCFllnSrby8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
هفته‌دوم لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی پرتعال
🆚
نروژ؛ کریس رونالدو روی نیمکت پرتغال قرار گرفت؛ ساعت 22:15 از شبکه پرشیانا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.3K · <a href="https://t.me/persiana_Soccer/30577" target="_blank">📅 23:34 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30576">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XjIjb5EefVHga-eT4QuQguYeDRTbv9FFlLw5C1OcQwm2GvnKYpoh3lD8SZQs2rOYQ3XxnnsbfK8_qdcMIrGxXNYR-J-U4rNKUx5XwVQpFyzzZ_KPe3tBhNSXcT2-H1Eh3e_crCnRctQV-XwyCrKwMRitGi9K02oB0iqRKoi63yJH12rGQKplozw2Ggv8HRtgVpxTe2M6BmKhPzV-zJb-3zgoqYvjXVGKoGUeLIo8qroVILtd7QtTnAfAXI-BWVSEwDfSqcW5aoN6J66aW9yYQKepqKvC7PuBaczGl5dZUU0J4cQ0eahOtP4Pp1OrUIYUzqR9eGf01TVB1enVOYTqBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 43K · <a href="https://t.me/persiana_Soccer/30576" target="_blank">📅 23:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30574">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/qVmlAAfZIrXVJbleGUdXxAuNBq1VeA363JToF8eQrMYQVyO5Mm-KJy8zGOa5vPCIfbcXvnBRi6BHt5yMfmxjuTSKtZgOG9FgLc_ZO6iy2UEWLwqLgILqy0axvjZ0QUjGn1WQRqMTdaRq_sL0tB4OEsxVZlL83Hh4DSe7gF8EZZ4_Fd8yGKY3iSMJKKF9-bQAx03hPv7-KJ2WfWjC8T_u5VYmZb3Gz3jHlXLT_XFwZJ0IEp9ZJHPfZeDM4e0BKPqJmU_6duktBd2tX31f9LIfe3qhvgWH5G_IBquAIEiO98UYFlazbHCDGUIDHPhuMQTRozh25Mw_IZwrsIMCdDg63Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cgWFFFQLOHLRcvyqyvuhf7QMSuoneOvc23bM_oDtoZ4XxdLgJss84GEWqz55LGGKIKujQaL0vlipn0mXIPe_yD3vE47YNZ6FKBmkM0BU28hmz4JObSvZ2xwGt2fTp27bEWEZ8Q3kFHgQ-kMR3JgyO2zLGJ4XapLGSFG0znY8k5AvoE9WEBEH0jZfSiC3O3_IS0Ygmr-pO_0h3UBwq2jQkOAPNYtVduuf5-avZW0wa5hAjRRWV-sxDTZdCkHA2fCGIBEMK214M1D3Nz_hs7DL65Bk1jxrwamF5l5tnKsI0dRhtS3vxhGC8JuFHYsiYsTDa-rLjtC8tMjAofbZpFWRDg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌دوم لیگ‌برتر بانوان؛ آتش بازی پرسپولیس مقابل قوی‌های سپید انزالی و شکست آبی پوشان پایتخت مقابل خاتونی‌ها در ایستگاه دوم لیگ.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/30574" target="_blank">📅 22:40 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30573">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djHcEPmzaishCQE4q0UwjHyrFFPCPAATbYyCG7dgnjyDlHaysfohe1D23ATtbEZz-jBydnlFqLgIPkgniqfyw07e1zn9dIGH49LqP6k0giesHqmLeXxOT3EH_vMPU-rt7yLi7h08SRBqEc4eUAAER2tQPVn-GXqpOU3KOPKHMVxCBK7_jBSY4A2iy_Nt-zR41XT6iVDvxDtStX7zvmUYMxomDh65GHnvL16ayYkP7NDRDZXC_gB-73U_PKFT8crhqxEoGg7KFDrEI6z97Bfm9iMEEUQnQKWwuK0Crt8hfAOljqPCNGEpEJf5-wR2ejL38dqjg_kIN9kQBJrb-57HKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلش‌ بک به زمانی‌ که مثلث‌ BBC امان به تیمی نمیداد. چقدر زود گذشت دوران لذت بخش فوتبال!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30573" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30572">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=oZcZi0WzJz8RsL74y0H3p5ShnzHif5vYQVS2gahRZxSrSwS6g0Wla-6t0kp8MogIHuqFCW4u_yhAS-mIGF0wHindou6hm7ARmBXzaXJ6852263zZDXbE17uu0bQWXm7UJUNFiimV0Runn-Hox6MjT3HpIdZggcm3ddaPyk1WvTGQfu5qBZGhYW4tD3MywgI7YSkgsQCGBIAELA0U9GXJuqFX2H_iKkovdUNqAgmDi1G5njrNK9JMTCPL0dh4Sn-E1YWkUlZxu76WD8dubT1LYKaABY3xl-Yh1De_3Z24VeafVCFogSVDx0B60URvnL6WRbso9OdT46028L-n7ng_AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7922a3fb1b.mp4?token=oZcZi0WzJz8RsL74y0H3p5ShnzHif5vYQVS2gahRZxSrSwS6g0Wla-6t0kp8MogIHuqFCW4u_yhAS-mIGF0wHindou6hm7ARmBXzaXJ6852263zZDXbE17uu0bQWXm7UJUNFiimV0Runn-Hox6MjT3HpIdZggcm3ddaPyk1WvTGQfu5qBZGhYW4tD3MywgI7YSkgsQCGBIAELA0U9GXJuqFX2H_iKkovdUNqAgmDi1G5njrNK9JMTCPL0dh4Sn-E1YWkUlZxu76WD8dubT1LYKaABY3xl-Yh1De_3Z24VeafVCFogSVDx0B60URvnL6WRbso9OdT46028L-n7ng_AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
یادی‌کنیم‌از این‌صحبت‌های جواد خیابانی درباره خواهر ارلینگ هالند در جام جهانی در برنامه زنده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/persiana_Soccer/30572" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30571">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ln-eOs7GO8bxZIj8hdTQB39BLdE9kQQPQBELFMoe-h1TXU7Ezk_Gakt_ePRs_AP8rkvmFcTW33vlfZicYMaWj3xK0YojuoRnFL7WhOB5ylkWoZWPVxhZOmbO82v8zkeNNfcc9XtV60pLOrLxaOaeRrCHENAQfdzAP8Y13FoBEqNN0pYswaHpRQjRNz8wTMTE7SFYoFx32TxyDAq4vDdRLfjrX-WmYMyNGP582_BwLzWk0JAZ6zgIzMR_sarfDf7EdiGs3YhsM4Ota_YkJ5-xM-Q3gguqhihqzAlmmBiSH1VOPKxpT0pB6_IQ2Ag3EA0snRQVjMj63TCwa1TiVeestw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
CHELSEA. MORE THAN A CLUB.
🏘
اینجا جاییه که عاشقای چلسی مثل خونه توش زندگی میکنن.
💭
آخرین اخبار، قبل از همه
🔼
نقل‌وانتقالات و حواشی داغ
🥅
پوشش کامل بازی‌ها
📊
آمار و تحلیل‌های جذاب
از استفوردبریج تا قلب تو؛
🤔
Welcome to the Blue Side.
❤️
👇
@CFC365
💙
همیشه یادت باشه آبی برای ما فقط یک رنگ نیست، یک هویته.</div>
<div class="tg-footer">👁️ 44.3K · <a href="https://t.me/persiana_Soccer/30571" target="_blank">📅 22:24 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30570">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_vQKmm7Jk44qh_gP3iN7HgNIKIyVRTGfN__-ELAgAotRfN2HCHA8ywMONKDjCt7QDjgTAIxkupTCUIYxPhGdbzSzK2TYXqaTcJu796fB_opl2-0t62Isy8t3CSPfBuxHTwlk8Rxrsx_VG1-sZrBq38Dg1cjNtaG61MeLbrrtDrwaSk5o_ZO1cGl__frXtUHafktvoXHpmuarZQiEfdR3D5pV8OiRGq3L2-ahDXL2gHuvwJ1cw-P7XD7r5SwxsIS1OIE8TDnW34gEqCaFFViXbfSRm3ep7rv_MClYV6LYgw_GnE7bi_0XH8LfWaxtYm8Tk3D5yGQxBKJtXj-ADIPaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
#تکمیلی؛دولت‌آرژانتین دراقدامی قابل توجه روز 14 مهر رو دراین‌کشور تعطیل رسمی اعلام کرده تاهمه‌ بتونن‌ آخرین بازی لئو مسی با پیراهن آرژانتین رو ببینند. حالا اینجا یادی‌کنیم از پاس گل تاریخی او درجام‌جهانی‌که هشت بازیکن انگلیس محو کرد. پاس جوری بود که انگار…</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/persiana_Soccer/30570" target="_blank">📅 21:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30569">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c0GmQO66Zc1w8EkaffeYSJwC3iFBBCcHAbYyxaLUvAaT_sGSxcCMvfUnrR7AmY3qaPQQjmHhgc_6BAStgRUHuOdfX9JjLvPDTosbnye_2QgaDpvmLIOR_s4VVxhuKnfhEuj1rVTdLoFQfATrRRC-_ou9U2iMMgW5uX5ggXSayzqveWf5SEqa3-0xFPkZPRsZ5lC6hbRlKBytEBPCuxErfCH4rM8EfHHxAaXRnWvbIv3R_Mp8nyNPUxFtgGIX6COA3dwPsUsYtKyfTKgYIhk3Zx2x4lA6duax7Ttr577Lfoq4O8qEPqSpxqIzLCPqLQ2jcvf_Aevsn9YXJ0JyYoFQOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان: بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30569" target="_blank">📅 21:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30568">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKG35SrmdICwSLgiUMbkrljNtOzJT9vjlklxOP8xAw7HzKvLnWa59ptTMUq-kVU2ZfIiTCY1nELAtloUBpMTd5t5erJEzBlwrVJ0o2MJr5q-QSnsE3pBJ4DTt4SYjsNadIrHiqfb8d98ebtmw3ziC-mjXTOdbtaldhtniA2wuZUoxGIQI2CUqEppkbk2WNdu3_HMRXmO_JefavPiFOp2pQ_Mw_1Odiai8F8h7JF29eJ60cy8hD9G9u-CvwJ-2HijscX0GnTpfQaRuA3hzoP1uUycrlTAO8Q1NmAQr8XsxCU_P7O8YXUueHxHZFViJZG2fsfvn6LjOYZOgiHXtMhyoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟡
👤
ژائو فلیکس ستاره پرتغالی النصر عربستان: موقعی‌که کریس‌رونالدو به گل شماره 999 برسه همه جای‌زمین‌دنبالش‌میگردم تا پاس‌گل شماره 1000 اونو خودم بدم و اسممو تو تاریخ جاودانه کنم. با توجه به جدایی رونالدو در نیم فصل از النصر باید تو تیم ملی پرتغال این پاس گل…</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/30568" target="_blank">📅 21:22 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30566">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B_-JrhjHNh1vE7_gW156N1EspejFr5k6RDcAG-OECnxQdq0cp3cjegnFDlAS-XI4kcHbYfJKS8bpn0uPhlTrVfwaPQpfXpCleUvk6Wap2YP_6KpSgunjjbOqvx6bO_J3amZCQr6PmI0OsedB-pGJOW00Ca27rbEZCaH6cCmUVJ2JRnkCKS1hfOvu31ccopl9vD35zQpiI2lh4ZDzF19pdMex5JlmQvI1bg4lfxjsD2NfIja-ODDytmYby4FjYkHy5t94vf_3kyotSjEa2EqG8cECUQEKyKQSnqtzUJleJRHRxNgDoF30o1kVr6SQQIamKW0_IMO-iepLllNXnu1i2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mu0B7qIuSfILTXBQogkfMRwZ39lymYWHMIEb-Gs-J96G2fW1y_QKP3D6_C10cYGBcsK70q4AEnVhwZ21HKhDyhr3xOEpSrZ9-okgcKz3U54tRox5jpFLsKauUihOEkiTOQY8rRZc663QH3EopQfjX_boMvtuFswSz2FJHd5_fAb-nWGnz1YmPRaP5ZswejTETDJVmFzUVnJJ-OUClenSvrTRtAjmvFUEIELeQQH01N1GxB-TZbazC4A3YXKkI4UUNQyvJpsILlelqKs5l5o-lpLqV5V7I7eV3cZMW5m45HtRHeeRFwo-aI_5xhhjkseYTxnnm4X16CEg4DVGVhikhw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/30566" target="_blank">📅 20:57 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30565">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e6ppwF4MkgaKtFjo1r9nY8gVylUYmRwqzLVc_h-zvKLXoCfGRGfhwe2KmcIdgELQCLSt2MtxIt3o0wnWiRUlMdhbrbJTy0WryqyRigfuwzvhKT1AJlr0sAozmGZnvjw5Cg87EZb4FY3ZyrPnRusr7R_uLbGqrI776gmfHrGcPt3XfQ9QjnjTaz4BR5qQRxvrAaLSMGi7Vq-VxJeAH25ZSXdpSrcGPDZ5Zb8l09AVxPf1Zm0xNUatlY_BEK3M50cp0zx2aajpZ2Ty5IZ7sYHVckwTsuL_RoH7XfHVojdIZGI96rLdrBL6xp3Dg7oF5jk_pjCOhwvWw-4D5gv-ZIMyhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/30565" target="_blank">📅 20:38 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30564">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IshsGo2JGDTWH_J6Ch6kaVLjCoJUjsKHSC6U611QGw5fEidHv02uHmM67TV_LuiGqlzvqVEtXAdobM5-UrlyjRGwVNHdP3oiqBdKYowcFewxYo3ouHOePBsLBgWDvWPSbmQng2K76ectYl_W_Y6-GwHGQhOuRSV7K8bnCoPUdA-9jwNTzpUWDb0pnDGpwpMYFU45uMPatw2goL6kxTwWYYVDebD3h1MZ3HkRhMu045Lu1oWEgyve44a1K1powMgFEvmfv_mWv8YYZcSLn3ylUqcdIACWFaQA8xcCJXGlq2cq9fRsSy-mb_LcL3JQzR8qZLCEnOkG7lyFbdu8CrjNQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛مهدی‌تارتار سرمربی تیم پرسپولیس روزگذشته به‌پیمان‌حدادی‌مدیرعامل سرخپوشان قول داده درصورت برگزاری جام حذفی در این فصل سه گانه رو برای این باشگاه به ارمغان خواهد آورد.
‼️
مدیریت باشگاه پرسپولیس هم امروز به سازمان لیگ و فدراسیون فوتبال نامه زده و گفته…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/30564" target="_blank">📅 20:15 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30563">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CCtDP6Wgsu1tvFm3e7skmxg_WwVTrF3cMLZ3UHDEUBmwCbb_pL-4bTY2mQXsBOKlKot8Sl46_NcXdw9qyaIaQTpYQRDU6uY6_e4zsORRa2H0GIUt0Ru8QeuRX1p5flZ1cSenaTrNKVgtZ0wfvkb9dSN_dp4QxOlfDlk1aSWgLGAjQ4Jp6NMe1SInDDlYL15ShT-kMcoukNM2Q7VbF1D5OZBPNQFt77dNKUCw-qZZtr8wwY4nhNmpuLLwiWy2LrmYpzUENn6nvSvk1wx0T1jYlwixtu27P4m-YEUpDsRdf_d68Upl7BO6bmyBsDsMoS-qCaIu6pwnOUNdaVT3Mvo8Zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول برترین گلزنان تاریخ؛ ارلینگ هالند ستاره 26 ساله منچسترسیتی‌که تا کنون موفق به زدن 370 گل شده گفته که هدفم اینه تا سن 33 سالگی به رکورد هزار گل زده در کل دوران حرفه‌ایم برسم. در حال حاضر کریس رونالدو نزدیک ترین به رکورد هزار گل زده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30563" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30562">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n34X4MzV2B_I-olf9lVisXADiU79WmSSFWdWu6BvkQQsrdfh50Bji1g-4Lj8oV-lNwsyvX6PhqICb7GuqfjLnKsYQi43_ysJqufCEWDVVUFhcETuquAePYN1K-D7R81JAzwBub0I0E8yJJaIM9N80vtX2gvjE-Vl_JB9qQJ9Sw8yfoeujkvl0vupZjBINfrFPBYV2yIK7kU_YjEjzST2lDH5hAji5G4MkcP43WyRVjKTkiGZBtv7VOHP3BXlpfEMmJuauvwkI7uLSFtI87P6z7tuzV0S7tcGlEu20kcqTLnizIlz8JczpYA4hr6cNG7Rqoc4yk1HstIrvKh9JJdhDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/persiana_Soccer/30562" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30561">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jQD0aBEcrI-1gKNS-IkrrmnsZFNl9WGpSQqxWoS1kLRCsWkqjgTTk-1U7wCsFpWixoSCMZOPqCvzqwZEBXZ4_IBJ3x0l1WCSICDzHZwuptm3jHsLUqKUQKxr-E_z4ZyVH8_pSWkXtV2nbwB3vllts_qWQxKtQ7stRI88kqX0xEAo4EWNG_zXUmWTynqtLBxH0Tuic9obqo5kCJATX262r4Op24fBDPnBuecgioyloiAX5wZizVcTtlPZnLhjbrO1SY4-1p6y_f0U0Feo7gV7zey3oSaS4YA4Q_0BPhM70xLPZdx34886Utmz-YdsTWmMdvVU8VZMdzH0RIxeUdPo_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💖
فرم Vip امشب با
ضریب 2.
0 بصورت رایگان قرار گرفت, برای مشاهده بقیه فرم ها وارد لینک زیر بشو
👇
https://t.me/+laf8I3RIuq42MDk8
💵
فوتبال های اروپا شروع شدن و هروز فرم های ضریب بالا وین میکنیم
میگی نه؟ فقط یه شب
بیا آمار چک کن
🫡
🔻
اگه میخوای فقط تماشاچی نباشی و با گوشی تو دستت سود کنی این چنلو گم نکن
⬇️
https://t.me/+laf8I3RIuq42MDk8</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/30561" target="_blank">📅 20:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30560">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sq00gD8DfgBuf3-Yy4i1hP27Q10H8EC9XmnlXcB9kvkapYLlt7N81dU1lhmcQrhnREwVLHukBIpa9BIXivy0xaDnGPF4pycmrh9HzDa_ovZS0kqpvc9UIUEVUSV6sgSnoHdeAQbgdJjz6dA9wt3hxqSuPkQI_b4p6QS6Ha1e4pR6rkIYC4qEitLxH_5cqInRspISwYrCTivLpTphudUTl17AEFde41RItqY7LgMJOtwI5GPKB3fEbb1ez5ILRP_KtVCg1V6ENV-bxskbuh3JrFbNM81kd-uugYCxw8twQ_9p9GWA5bAjMwNupUb4cp9xz3lHuFMbBN-iYxqmDqsTSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه ال‌ناسیونال: اولیسه خواهان بند آزاد‌سازی ۱۷۵ میلیون‌یورویی درقرارداد جدید با بایرن‌مونیخه و گفته درصورتی تمدیدمیکنم که این بند رو بگنجانید و هر باشگاهی "رئال" این پول رو داد بند رو فعال کنید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.1K · <a href="https://t.me/persiana_Soccer/30560" target="_blank">📅 19:50 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30559">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76d469366f.mp4?token=kOkECJbWiQa2w9BZX-in-O4ytYQV1Ax2Ao0CIaW7vGemSTw9AWQkFAQBifJEVS72PR07cma3PYyjor_4D85wVlkXtujhuCwf9xpBq3GHhEk_fyDb0UCYK5ICf-vUDphyJdZUFryaEEaPEmAFBupRcSOOLJ7hXUkdyfzIsGcYMc8a_JFx6Y_XzZQbBNwPJdPzMBLv8K-LOrpUYZjw7vdRjucpR0wFTpiAYJIymkezLbTapv6JIYoJGAzWcNxHAftZzVLn-Re7iqnOY2p-wJeT7ohMNsqLAdHgtgPVvwSMSb9McWOt9P3IDkb3AEXZX4msYGqCIgd44AwPpE6Fkc8wv6v1D1pg2N9eQSdvqqDgWhLVYCz-5cgqcSXg3m5Vc0oelY4zXq2tOodzC4GWXRnnNjoI0yFBTzQTf5iqatl0ynEyehg_dSrS3-8CjhgNaagD9XDjCwRedvhyG1GtVJWyT-VAvwHdoPmY68-YAXe66PSJuUwQR3lb3LLSGK-cu8rd2cRwAb5i4BIJArBDEEwtu-M9ipnlsIzRb3XJUxc68QQ7MQ9QZkw5MZqod_3GWA4IRNUUfJxHL2BUUcU3TsrkB7YzzeNGKPc1A9uz4qpfKHK27KWWRe6tIKmHPHR5yOVnClHFOIpAnPsgTXT9-td5uhfLt98bFbb51biKqs88U68" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
🇩🇪
ویدیویی‌از پاس‌های‌تماشایی و خلاقانه تونی کروس دردوران حضور در رئال؛ زیدان در مصاحبه‌ای گفته‌بود کروس بهترین‌هافبکی بود که زیر نظرش کار کرده و به داشتن همچین شاگردی افتخار میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/30559" target="_blank">📅 19:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30558">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wCQV3rdXksS8gAPous77XHNtlEY_k7xuID13ewmGJ7rTyVlY-Q2lqH51UMKUwXs5imU7ltxWQQKXTkCW7noKpZk3hMoZkZiJj4jem4AWUmGYb4298JHowDp7P3akj4Jjy8BMaeSax83OWnSGHtDa2kgI5k8uG_q-JAFE2Q2BE_OBdyP-jMtGeMDFbROVtuQMFh57gdW3V8Ti5Osys14-JyCyRb15_CrhmwlgtDerixbbNy87QEnSjuuqdg6bCnnKA4PK4yMDYGPXtJGYR1_jflpA_0KsXTrAasRfka-5f44_lt83JoEnTsZmmvijv4nV-I0TPgx3NVXZPF7B62epXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#فکت؛ سید حسین حسینی اولین بازیکن مطرح تاریخ لیگ برتره که برای خودش فن پیج زده و سیو هاش رو باتعریف‌وتمجید ازخودش تواون قرار میده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30558" target="_blank">📅 19:04 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30557">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYNjHkdGJRtHMAWKxjZ_Ur3S-VDj0B5dwpc5yVDslNWSN5J9E7Yt_euXFM6rdSLRtyGEroN26No6typx28bND-FzNdM7gzRPUq1AZD7o5zR9UJsMVYWHw7tVeBCR2ST1MWUDuwwucuXoUrkGLNZ-G-S3dvUCkV3twAi1UtT2tnlld6BBrGJ2has3vmm6DTFDYj2jHHhhcXilRsLKQ3JP62Ai271Cpp6yYhapeKmvxwJYjd0PxLIKOY7spG8g7JCVkWfQ7XV3FVYI6oAAntp-XkC2ds6DJUnYfeEIFGxSmnSjqTwZgpd7efeGC7vllP_FVrkjMmEvY7jCQjZoQJ2aOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30557" target="_blank">📅 18:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30556">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7389e745f9.mp4?token=LGHPS1XezkZIw8xxnYl_OcneG3F8YIMhiJ6Kbgpo8licJ5AjqymcHRmXBoYos_HlOliplujjHkvKDHDFi931R00kg-HQC2XMfnfbxfKcrQ2VSbC-WBhFpoSuM1TV-0jwzBGT9hZIkBcCrVlNwbSKZvZ1VwOjhhTcCF9D9Zi4NdcHyYRt6-_vbMqp9gCjeLB_hvzn-1-7MCg9O4Bhd-Q8K7oDsLWnZgPfe9z9EzTHssu5Z5nhjWp810rEAfym7OYEw8sPEEYDVPvlssM0zQ-ArOZKpix84Xot410UUqr1FetaZaQibd7__3f8m2re5ekPatV5l0S48Ex5I1qEcPCkCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/30556" target="_blank">📅 18:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30555">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxFVB4vIaP1pggD2JtmRIBrxplV_LsDrIUi44_I7jdO2V1K3gAvZiVV_lS-gtesMV-gLsdmZGmOeP9TshGE_Nq5PxyakMNaZxqf4IjzW_NxvA9TuNRcRYC-ah2O3_6UUDw3WOam8DfIg3-L7LFLqkXHrTxyrklhmFJ4CUxBpU6KuYRcpwT9TntT1Kx0kgv6r6i6qUnoh2dKoan7KAEg_vyMVaq1RNriRoIQHyYpvNNNNmB8Ck1ScM-u4jqRMcjSM7t9ggWwaBxrnCsqYNT6x-D4bRw0zKBlRjHQHRR64B2nD63gHgkUhwDddUFm__18v7QCoxyRNRQZGRIlSmB5LQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه گاتزتا: روبرتو مانچینی در زمان حضورش تو منچسترسیتی دوتاقرارداد بسته بوده. یک قرارداد رسمی با خود باشگاه به ارزش 1.69 میلیون یورو در سال و یکی‌هم یه قرارداد باالجزیره‌امارات برای فقط چهار روز کار مشاوره به ارزش 2.03 میلیون یورو! هردوی این باشگاه ها…</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/30555" target="_blank">📅 17:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30554">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tVoNXAh7QIYC9wciXON4eQW1N56uG7tuDMTt1MvKZlqyQ6_Fevoi_91QCpwfih-4QCL7KD7AW4Ms5n3ZEPyfXzjUdw496QwySKqDhe7EZVy1xolP5TaAgUxXz7v99WT3EkcZ8cYjPsPdOisM02wi46OhWjh7Y14O2YvIPLYkKDeGdjB3cRM0xYZWhUG8JzsEtucFUG0zYZrZV0Ujq-Av-mYVY7gNFvDqlc3-nUDXiyWXP5gdbg2-bph7j9oH2uJ-z3DheetylH6fZGosRXFLmgdm44eQINjykzQa0hksLzxacL1D9asyxzI38CNygCLbexjG3WiKxvl0KvV8A14iUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
حالا که بحث تخلف من سیتی داغه یادی کنیم از 3 فصل شاهکار فوق العاده لیورپولِ یورگن کلوپ که زیرسایه قهرمانی های منچسترسیتی پپ دیده نشد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/30554" target="_blank">📅 17:44 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30553">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/krncJDph2zQU3402ZGIFYg9av82j6DIx5i3sOnQM5-Z4zrXpX7j2ffOT3uqHNVgE02rONSWaUsh3ithcaAwyvSVMCsup7fbkTTvQ2HsamYmdvUVUuPJVDgoCun3dPky82hGxDkrQXldRtAQViFynFKIWBLk0qvc_Ocn9cWYRLbAHXjJJv5s_K94Ckc5E04NPhsetH47kh2r_rZxJv_uY1Fx3SUL6pka8fnZsIydwQxnZV3sQB1fHn1a-jmuDB32mcyVXUkEIwDq4XFEV8EZKOWOndseTsgYbINM7ic4MlqyhSZ-C_l9CgFxjSffatQCfO-jQ5AHohKDWejtdampFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
سال2014
: کروس به‌رئال‌پیوست‌. 8 هزار هوادار رئال مادرید در سانتیاگو برنابئو از او استقبال کردند.
🗓
سال2024
: کروس با پیراهن‌رئال از دنیای فوتبال خداحافظی کرد. 80 هزار هوادار او رو بدرقه کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/30553" target="_blank">📅 17:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30552">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vs35xb2OKsvMFPGuYvM0S7uYiM_3qzWWzlBFX05xIMqNSK-MrAsmpn50TV9H5Y2Siz965C6VQ9uAQLe2q0iAlyb7MjdQeAn2o4fQVnztEr2uXrac7-Ljt-hCyuvpilkTvbULloi8fzCFYZHkv3SQI7FOIFlLUci1puKTSgq9HX1Af9Yl-1zWqUs6t5VVgaQWZ2KQYmR5LSlAZZPKgJJ3K6I7W-tm3_b8D7UwiOvJStGnGtgOpizZci9M9fSEoJhTHXfF-V4HpRjasTuelmdg0Tv25HXmXka0NeoYuG1V3L5tHLK3GiD-CMsSnNVsmUPL-lHo-SrsLX2jyJpj96FcJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
آخرین شکست تیم اسپانیا در مارس 2024 مقابل کلمبیا بود این طولانی ترین روند شکست ناپذیری یک تیم اروپایی در تاریخ تیم ملیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/30552" target="_blank">📅 16:55 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30551">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FFNY816gG9GwlA4koRwSRO3wl1l6rVoUqNqDtnT5v5fET_CgoS8fWfukE04WcKBszrJFKvur9i7QFuaXCPa_bTlAFgt3RHW0XSxbaJlyq00SM3MDL5pb7GfUpQ9syuuu_wyTEnWBs11-IUwy_FHRRsZUZE24oODPsS8rN14_GDrhHT7E1AXXS1yE233GEIDQUtPCa0LMbnfxlbrpD3VSBWDBla-2qlnKfv0J6NXk4_yu9OF4xV9MALE82yjr50VjzXE5tibOdH0jwlJtMSisObEmHKp2o7mQRXYOqNygIgPfSLIimcSdYzlzKqdgFV8T5B3fGplJehaAunaQ6Tx8Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
جما اتکینسون، دوست‌دختر سابق کریس رونالدو گفت که بعداز جدایی‌ بهش‌پیشنهاد پول داده بودن تا علیه او صحبت‌کنه: وقتی‌از هم جداشدیم به من پول زیادی پیشنهاد شد تاپشت‌سرش بدبگم؛ ولی من قبول نکردم، چون واقعاً هیچ چیز بدی برای گفتن درباره‌ش نداشتم پس دلیلی هم نبود که ازش بد بگم. هنوز هم کریستیانو رونالدو رو از صمیم قلبم دوست دارم.
​
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/30551" target="_blank">📅 16:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30550">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‼️
#تکمیلی؛ مستر المپیای امسال قهرمان تازه‌ای به خودش دید. نیک‌واکرآمریکایی قهرمان مستر المپیای 2026شد. سمسون‌داودا، درک‌لانسفورد و اندرو جکد هم رتبه‌های 2 تا 4 این مسابقات رو بدست آوردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/30550" target="_blank">📅 16:19 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30549">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iUIjWO6nnW0odS0FHaouc5_06G8t9Jyn2ctvKkpJk-WQuCpS3i7TFWXyuQBJI16VqJWz5jJI7fcs37yLh2-OBCjj52VhMim5ZxXtdRnMZXSyk7_jYU3eZ2_Hor3KvE12CFhmbZuC9QCkIu68Qr4XejKLSBFV9wq1yc2lpq0q_oN0TJ6WceYjl7lb4P1lQfKZGNTGGrsrXe0eMF0sdHrshz-Q1K4gepBjFkS0lT5o3Il4bWEikfTxT0mKEJnmGzPlh8aBb_jCVMp9kB8Pb3j7cwk7XyRFOOmQJf3F2__hAKkcyn0KpGQZDXXWOLGkMuvju_OTV6G6bGtuE8amSAgJpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
حجت کریمی مدیرعامل تراکتور: هییچگونه مشکلی با اهدای جام به باشگاه استقلال نداریم و این موضوع رو به مدیران فدراسیون فوتبال گفته‌ایم.
‼️
رسانه‌رسمی باشگاه تراکتور: بانظر حجت کریمی مخالف هستیم و مخالف اهدای جام به استقلالیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30549" target="_blank">📅 16:08 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30548">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8b814e56a.mp4?token=DVNB5AZdVez3AHB_aj0uMReuG9cPsdH7_5UISqG11f4WWan5Ue8tYkhr1Dz8TQcRRLzPXxyGjoRlZe3XZHuIBPF-RyvHYALVHqFwakqAfrvPblWpVTlAWe_Xpko96YSSYmUCzH7YktZBbtPQRg3BC4RXLZJWCxs0LQLJv18lrr8Wj7Iz3joE5iJAVHMXy0Pb5cmsbzuzUVIOYAjFTdVcNGL0EGy8446NVsBJpUqlnFmh1goIVQDaXZAC4CGqTDsEyM7ZKX4MhZLuvH9wLcERbol1GZvU_6pNlv77b4GdPXopia-OEPPeanIYN2hdf4b0Ed_bVKD6iUmX-_i1D3qCAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#تکمیلی؛ سازمان لیگ مجددا کارت بازی علیرضا بیرانوند رو به مدت یک ماه تا پایان مهر ماه برای تیم تراکتور تبریز صادرکرد و این دروازه‌بان میتونه که در بازی هفته هشتم با استقلال تیمش رو همراهی کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/persiana_Soccer/30548" target="_blank">📅 15:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30547">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mnvjytxZ8GFREhe0-l9mJTAM_MNWpzCi-V647q2B50YsFv8_7v7KfG-heS-y1EVmpAnwnlBEuJYwmcOTLIdsqkKpsgkZrreZPiJ61HTz3A8-tlACZJq0DYu8ryEi67urr01XWHOve2cV63P3-sMTStBuSRVrdhCTNsJ9lBlZ0b1HGzmBiJwE6fW0j10yrRIy8joHLncEt_iYPKsGqUwF-zw264rwOyEyzJQzCMWdgYSuYkswqemiXDMzNdnqkQNaIlQh10cCJ4jiRI5gXxenWMWH5sedM_qZ1TxlA0jHhJDPT8plDN5O0u78NhFUqh0BRwn0XRfZp6G-PbpW1XsT8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
عملکرد خیره کننده ژائو فلیکس ستاره پرتغالی النصر دراین‌فصل: 17 بازی، 15 گل زده، 4 پاس‌گل، 9بازی دریافت‌جایزه بهترین بازیکن زمین، نمره 9.1  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/30547" target="_blank">📅 15:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30545">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k8PxtsqpRS_dR7vuX6E_B23qVM6Y0VYUiEmV2YUhXQZFEJ8SxOPT9DYRIznpni-OEuzV-7YG_ZvS1bmlHqbST5lxTVBVUN7T76b8mcvfeC0qihOrTEuoyoDqTPo-WxUMsOlybfLyXLycXaObsYl7fxoL0xd181sjfN6POkyR8rhUC7aZbVeq3f07HOgjJt9L47iBfjp0MbEURIbK6i4Q8UbuufJTlPwVdOktCoFpEtgyhu7MXS4jxJuzd23geP55C0EhZb-IXItJzC9F7Ysj_vucyMTMds-Ms1Z54ik_rz_J6gpoFMH7u8GD9b83A9acnD1Meeyt3-alT8XfvxzvoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SRpZ-ur5LnOz18IByL_VbDmnnuRhYPad0kqbSCC2RYJH3PMF9iD3Q8Afh0Mcc1jb7Wj0VQ9cVCYS-FE38SITjrHvMP0XLJgkFxAM14UYHdJGx3GZ3jJGlSVtyXHwMjl_ggSLU4qWs0XwzOOpYOPeLp9aLJg9k23HyrL9RquUlDiYgCjc5myolbUNGsmUsDLj2VdjAufMYoiLKo8_LP_SXmidN46PQ4Ih-I1vRf4BhSMjrcPwu_E63Mo0F0P_ln36_WxJGi4IltILJaR2qx9T26IpU-ywL7ELwxiiIPu1GAjxsvANPZsuXVHyuOlL_UCURwrE2Y8LHYPeKJWG_Rpuxw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30545" target="_blank">📅 15:01 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30544">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C53bDhRV_1G0eZDsxSU43AxMYTt-zkrePN4a2Qo3L3aP-m7BQKuMGHjApy0P3GxDm3eWiZTCnTu7S37thmnCbKkrax4wZOvNrc87Y5-cmz42CcWvg8NrXt_Z_-A9dgDEroFUMj7cHqiNNXlqDtPLVGxn92oBHlgJ393JF0SXbQ20RsNIhLLcEl74VjNFOjD0XTaHnI-jBjN1QKVERYhmSI04ZNJOmD1GsaR_ZqOxz3cFHP3BNaetwIhOeinfjlof6oEf8gf5MPILsjG8s_FaXotzVgQi1ZeYJn463Epk6850WAwX7HLufyGMliQfgxkVCb998no4QnPIDx8wEzKkGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/30544" target="_blank">📅 14:37 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30543">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TKB16l8LtLenIQfSxpmQvtrzHyL59LPleTC1h_yVuXo1jdlN3wGqhasdSzBZ4DAvjRy40F3rxjI-B9cISEcAQu_KlnGRBloGlKcMEv6tA7H5HMNKDLUKJcB4LoKOxVQI_jxZTZWS2Mw0MJnvNGQXf_X26E2X8BhbkfZrPgm0WMNVT23S5_vu4K97kTGoRKmhLqsI_LsgBBqTOsVRqVds6RA5uCwEgoJFFqFepDUMGk3LvTRG4Mg5RZxx7k2IS2LaBGHtWJiqc8A9Jm8XE-dOFrrJ8PKIT5HT1bXd7GJ4JuhC0SGAfKZI-QSNUq5hEc3C-IhhbvyWFtBsnNppbagEYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تابانی‌به‌فینال‌مسابقه‌مسترالمپیا 2026 نرسید؛ بهروز تابانی درجمع ۱۰ نفربرتر مرحله مقدماتی دسته اوپن قرار نگرفت و از صعود به فینال رقابتا بازماند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30543" target="_blank">📅 13:59 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30542">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc0fcb29e0.mp4?token=s5qNO1h4olFrhvnLDKHBzJ6ZSo7j-DhOvZEr8JvNJ3Ng8mYKVRXVWkKRL8W-jTuOaEEoZOzLWMTctSGLQsrgAXeY-gjBvazAtnj_PXQIMGi4-3V1XxXt9ifEdf0hCnbEEfTh30Kbb9RfBfHt4S3E4uhuNmXEf1pePSdPhKoLK4XMmtBQVl4DdUfoTo_0ghVMy8LcAQ1V1TeGHKOX8xlKs1A6beSBW_pF8AmsqDSvGZz0DaLX5EhCgdTdZSFtnffs2HXxX597Vcimogl6gdRhaTjtyYFOnUepERLNvbE0Jd7ChYiXZfPupcvuCmp_YIomx_EnojiWY00FAUq0klhr5pgUR3V3VH_PSScQdUr9625GfNsbVypsuZXMyVB2WLgUfIEdZyIHWin_aTBq6wqoeuGBGGGwqhQ2gmye3pg2yleiERgBbuBvUPn5sakVHoq0JA0cB0-Oi4GtCnEr0wc6wkKTRzKGQZduQ_iDSXW_FeE96Jq8D0vS80ym9BpgxdDvdrQyzmyAGEGH7XS2sxWuK9b9nrPZJ3MnCLc5FanIlvhvM49F1HH3XrHBnFOoh_LKofjK5C0MBRJZ7ePwpEhrNuH2quafAac2zDvGLB3ye-RZb-101b7Zvc6bOLddjKG3RsvfDo-bHfICSZeKW0ZFN9Qrk1vYJT-rIWs0surS-CE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
👤
ماجرای بسیار جالب و شنیدنی سرمربیگری دلافوئینته در تیم ملی اسپانیا؛ این ویدیو رو ببینید برگاتون میریزه که ایشون چطوری سرمربی اسپانیا شده و هم قهرمانی یورو رو گرفت هم جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30542" target="_blank">📅 13:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30541">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H5d8oqfWu-ixP-vhsNRSSR0jJo1xG3ZGDST7EJ7s4wLDqPTZPZe0EdaE9xkMFXhFDs3b7wk3Jdo7oq1Aft20oKo46b_65Iq_r4pa_oShMtR-D7LTfxu6mbohEYGSB1nIDwFdYi2MTqtuVCelzNq-ehi8PRKraSBfWL6I8yaUzEPNzo-7Nn2VASVV-v8O1EuvcR9SKD8VbecxsqhgO0dGx-WEJgrInOAxkffQyJqb61dX_AqktiefvzaFImDMBif2sif2O_MZOknIsso6NBABmQkgUTsAjgF3ixiWYn_gt0ZeJRBZz23FfOyDnfi5Ri3pbCUBaJ9rOo3E94cPpqrCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30541" target="_blank">📅 13:26 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30540">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZR0gPiP027PM5-3tmKaE54fw20t2WbIKLvIJPNXyfARfKJb8tf0peyqUipve2CW2wOn4EJeW264TuxvGvd6LeYXaOQVxb_c7hwujPbr456BbgqnQcf-A39dL1yCsIW7fRh-qXPhXRFyYCEp4T2nagH8WOSPwGSjczfNWOlLKL0hhX-r9K5aVhYckEL8Xx57rvF-hkOqwq8zFQOXmqkirk9ZFBVfF8kOoDbmrIPhc_R_68D8PwtNXj_MQ-xfBMO5njhs0uyo6vTR5bDWSLqdUDyZpFo8BEIeo0VqvltKxqx-iGB7hqavdFothG0-6jC0elykQtQ8DNzFf650-7nTBZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛علی‌رغم‌اینکه‌فدراسیون و سازمان لیگ گفته‌اند بخاطر فشردگی مسابقات لیگ، فیفادی و لیگ نخبگان آسیا احتمال برگزاری رقابت‌های جام حذفی بسیار کم هست اما باشگاه پرسپولیس اعلام کرده حتی حاضر است بدون ملی پوشان بازی کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/persiana_Soccer/30540" target="_blank">📅 13:09 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30539">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=FyUjuMq3NPnGfcY_UQxjRhn2yjgI5dixmjLA1AvKRUWQjLG1sSByw67Bd7-4_xBW-kvRDOsFfGvpor-iY_zut10e9kmGSYj0bq2zeuf0rWwPp6pjQfiDxLcGasUpaQukp3RuZAJ3MrxfYUKeaHoC9umghfyS9wZIVgaQ9vqy4A_26GMUUzxtzPIV7QN76yToUGW8pbAzthgkG9NpyCwkUCkey5nZvV7Rb2nULioA_quBDBmj4SGjKzfzqVVzZp9Hm-H-scts1uzS_StLnYiqKNqSkfnjQ0242mCGGIpR30dxGzxAXYSAhyDO2Jb94C63uaMle8PDdDCi_MTH2qvcLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e9a7ecd973.mp4?token=FyUjuMq3NPnGfcY_UQxjRhn2yjgI5dixmjLA1AvKRUWQjLG1sSByw67Bd7-4_xBW-kvRDOsFfGvpor-iY_zut10e9kmGSYj0bq2zeuf0rWwPp6pjQfiDxLcGasUpaQukp3RuZAJ3MrxfYUKeaHoC9umghfyS9wZIVgaQ9vqy4A_26GMUUzxtzPIV7QN76yToUGW8pbAzthgkG9NpyCwkUCkey5nZvV7Rb2nULioA_quBDBmj4SGjKzfzqVVzZp9Hm-H-scts1uzS_StLnYiqKNqSkfnjQ0242mCGGIpR30dxGzxAXYSAhyDO2Jb94C63uaMle8PDdDCi_MTH2qvcLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دعوای بین دومجری زن‌ومرد تلویزیون روی آنتن زنده: دفعه آخرت باشه که اینجوری صحبت میکنی!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30539" target="_blank">📅 12:46 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30538">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rVazisuvIMTxe2NabOO3EIsduPyF23Kx1jMrhFl0Cyz7FripQ1T_NAL_mwXLLutKCkQng-LROC8V7uvDAf1gcKdBZ2BlcEwKXytqxnkXg-GE5oBQ-Q1WMEfwChq2MnzJNCJA_MPv-8WO_FOO3eH_xgUg4aSJ7z64PURz7jYYhGSyNfQKbvbchGkbmlsGyHVhxIH5uldEcF9CcTk_H9-bJYzf14nl2wyY_jamluVPz81ViOI83RTJrs5Pmtyfl9jrWyFi6ZOxlaXQ-5eHcWv8UqiK0NFEF8OF7VfU6_G-lrJ-sFwn56mnNmWlGGr7ZpOTDwe08-Z7ru_BzTn8KZ7gjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#تکمیلی؛ فکر کنم تنها کانالی بودیم که بارها گفتیم که رئیس فدراسیون فوتبال به باشگاه استقلال وعده اهدای جام قهرمانی فصل گذشته لییگ برتر رو داده. حالا هم طبق شنیده‌های رسانه پرشیانا تا اوایل هفته اینده فدراسیون رسما در بیانیه‌ای استقلال رو قهرمان فصل قبل لیگ…</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30538" target="_blank">📅 12:28 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30537">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qU6J7Sm612wVK7mqa9sfcDGDGZhYhfvZg0X2lCOgpicozCfKA_Xvbpt8YDSlohefM4HpVG9wlH6twX62VlZil1hmMenZ5PfO85QWCo2qsTpST6X9JodphYe02XiFoIKu2W48I4tvsPUtbAmCKgPkszuhM2A8DE4Gl7jd2mGHT6QndJRG1IOkOrM70KSBBL7cB1g6pmowk3YetrGikIhHgMLMDhPPMyQT36uaIW6_Bne4LhzsrDBnjYQWhoT8i5zlPKHspqpdsecd0QiEHXnf0bZ9zKvxBp6wfkKFCnQYxBuGdnYKT6nCuGJ2vI4dt3tHVxOOeZnsPrTggzVCopkerQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
در حاشیه دیدار دوستانه امروز؛ کنعانی زادگان و ابوالفضل جلالی دو بازیکن اصلی پرسپولیس دچار مصدومیت‌شدند و اززمین مسابقه تعویض شد. هنوز میزان مصدومیت و دوری این دو از میادین مشخص نیست. فردا بعد از MRI مشخص خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30537" target="_blank">📅 12:12 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30536">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">📹
👤
شیدا مقصودلو همسر29ساله خوزه مورایس سرمربی 60 ساله سابق سپاهان و الوحده امارات.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/persiana_Soccer/30536" target="_blank">📅 12:00 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30535">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/epDPA3Lvio8UV78o7Vch-jdE5djclQIV8YUID5EhnVL4115oKaZl6wcAcEsajzT7Jg_YNpbI_EQlNJPXJzDTggK7c9Oah7uAc-Is-nev7e9mDOgkGHqQzhkQCdo9Wda0wlRV3XJRyLaNPlr6LsSDgVNMpPt8aMlK1qjrq4GjcwwL_7tuZ9jLhfAWu_BiY1o5jIRlJoF24tPWvVX0R-f8jAjy4MuZnv8bafnBE1Q55-87rPIyJYppIqwvJAo2WkizlbITbETnQbvqMf9HL_fGEyKaz3th182TJSStoX10FLfvkB65SW7zmXH32YB44QuvRWJnWsx2BUOOeAceN7s5-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
درصورتیکه سهراب بختیاری زاده تاییدیه رو به‌مدیریت باشگاه استقلال بدهد؛ سید مجید حسینی مدافع میانی 29 ساله تیم ملی با عقد قرار دادی سه ساله به جمع آبی پوشان پایتخت باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/persiana_Soccer/30535" target="_blank">📅 11:39 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30534">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tCfnk-prZT-ph-m-evmsB6svUvDYKn2SQ902QuR3L0QKrdLGAIVwL8d7uC49TsHKP3RX0AHWubSiOwdvLb_QlSHeD7MnQRis1oyTc1qfYaT9N1ijeXebJQtL-LHtY6INjF5QLnJvMtIOimas99-BOTiIOsPWoY-FH8P0fcp-sLSWJmrm8V7QGssdzl86M_iaGXN41qVNtwXcZKVAAgiqIa3XSatVeCjuqH7sPQqoK4qvJgeU1TGsCSY1_mzPGw_y1Hdiq5ac12IwUtXq40Jld38q7_xg_0EpDut_92mN1BkWGtan9bACHpfyZjto3_qvECFfJnWnovBt97xA8vFCpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دو بازیکن تیم فوتبال پلی استیشن ایران که مدال طلای بازی‌های آسیایی روکسب کردند به‌ عنوان سرباز قهرمان از رفتن به خدمت سربازی کامل معاف شدند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.9K · <a href="https://t.me/persiana_Soccer/30534" target="_blank">📅 11:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30533">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJD7C-BfAJ6Rz0mKQdWEJqQewD_dWscbeomIV0qmw-lcG0R-7aeMI3KgopjQw4V3Su6CbRwV4xJgXhzey_A0Su4BkiL6O6PjGeMKNKuliioOQvFWKtGbQz33nJl84s9Kpuf0ou2XYQDlDhKnfKvLap-TL_sDAj-Vdjl9R0-ZBj238vVCS_vHkoKOB6nSNAwYVtCgJkRQn21MDxph6sBRAb4d8cO4gc0f9k4omUWuonpcT38cuT4kKRLtRDUjtfsTHrQodQYejPHDPWPaIMz0-xapww9F5-T74FtcOapnCuz7zgiwhClZv3iCt6FO-_tXaG6TD2Lf5BeG_cKDJGHTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30533" target="_blank">📅 10:56 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30532">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hzw4bHilAazW_xgdECaepV9LIDqOZyt8KYRdUerwVO-7FJHx1xcqSxquDn44FM8ONqZt7rsI9GY9YRW73u1IXEbxQ7VY07n2py0dmEcczic4c9CaVnm5lJiW6Dl0knYKWLOMm8SL3TsEr_PLhBun3d94O2c-kIsTjq0Ya5GLMuDeXKQ9Sx9lAQUJtikwOFNL8Wh5vyyJTwg1YYlG5TQ4anTxyzIPfU7nS2I22zJoKfeyKxYL20h3sxLXkvy-eEjd7Lyv1LkOnK-BkukPvZt7Mqg0A_dshC6ETkGFDSBwoaIwhfOQHqU7vl6XcGmcoMHLGwK7sVsCkYnWcDXQcXS8mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌جدیدترین‌اخبار دریافتی رسانه پرشیانا؛ اواخر هفته‌آینده احتمالا "چهار شنبه" باشگاه استقلال قرارداد یاسر آسانی رو سه ساله تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/30532" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30531">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_vXuC7X9-xyvdzg7UPrfu-gL7mCZUXCrwdExyWwoqrqP0uRZ06cQ_OamuaWX0lbHj-s2zZkUqeU2MRFFIMQnX3TmuI7UO7G5AEUjGlh7QBDI5Jj6Epup2Yrb0rj3iZ5HkFtBTxPFP2w2F0EjEdJgDPQlKWOf_vgkTOc9QhQGXdbki02gHQ0B5nO42z5YE_1KjYIkU4J6q5jzKRhLXIDLD8455sLV1aqB8M2GvhVI1FM69zjpUeBFdW4VRqjc9N321MZ7084D1m5QmHk9c_AEE61ROQjKhjKktx0oCcecab26iBIzxfOpaDwL-A5yhvfQA1cTvy9FiLflUn3ENtXmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🇦🇷
🤩
#تکمیلی؛ تمام85هزار بلیت مسابقه خدا حافظی لیونل مسی تو چهار دقیقه به فروش رفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/30531" target="_blank">📅 10:47 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30528">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJxWjkM28JujcQZIgMvKNeXitP5WeDuCiRbTNsyo3UVODzydPau78RWMfU1WNwkrQwz0XdF6OOVekdcmbhZmjBdjH2Hu9yq4DpZQa-D-pBT6efCTeCIK3iQnrQRBSQ8gPoNXfZO7kCJw8Rw-fagdruck97Nk_d9cpb_Vh6BCvunW4mTvNbLaXxU1ifvKep51jMqPggacUADNy8114tF5b1QbbGdHOYlrgp7GOmf0zYdNFgJQiP74vQoX5EsLjHMnCRKpaTXwvkwNVWVM8hq7Zuo6eFWA1_mMJ2WvnhxnC0nM1IJoKkJ7IuVms-OGU6nDtKNGfHX46DzmyLuULmLN2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیرعامل باشگاه چادرملو اردکان:
بایک مدافع چپ خارجی که سابقه چندین فصل حضور در اینتر میلان رو در ‌کارنامه خود داره در حال مذاکره‌ایم و درصورت توافق نهایی اسم او رو منتشر میکنیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/30528" target="_blank">📅 10:29 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30527">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v6_sHmi_Dx0MLiWkxH01VX62H2G2DjymHoF0XZkROmUUF5pKvZE2AHcMg2pTXMU6wn4Drs_YI6a2zJM2FJ93J6h6BSC2SWCQnvhLhkLiSkE_S7nv8uS4ZcizPZzDUqxMJ5lpet4qHofbhL9_0pPL-jCsAXexKFxe38WaGNh8oLlc3h1k6T8elBfinO9ck7V-M4zd6JoNvzZNDDXArN6Cy-9a9roK2BPtoe_O4ALONLRMATvzzlC-vgrwl9I57yW5Wo8bAxrfkOdLJvRtVkzZ8azU5ZRFfQIetg2iLNJBAyoKv_QdEaj5pgUqnPsmjlKYg4IJ1_MYIIWXpsY62J_pEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ اسپانیاباپیروزی 3 بر 2 مقابل انگلیس در ومبلی، هشتمین برد متوالی خود را ثبت کرد و در این 8 بازی 17 گل زد و تنها 3 گل دریافت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/30527" target="_blank">📅 10:23 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30525">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTBqRCQ_ZSdXVTKUpwFM5oymkS9aK0ub6rcHLpiRhSYruGN9qNGk2KKf0-MGCRyqyAgE8Nq1-bbExWT5jOIGf86cV4vgofQ8lWT5pMOW-rgHxSthJAmnyOIZEGTWUiBwin8cT3jmwyqFjQNSVOS_caTL4hDyAJnDrl-jTB9fcjXDvRpi5seONoaL7uIOIKPBfNlguZaetbfiLXUA3uBuhcPxdDdMGV7FE17aDH_XLcuyxINbwV-brTtjYA8CTLYMHU4mUtdmMZjX3PFDLgUbyrp3qgtWqLEiJ8m98xRtH-dHUWYGVIrD3QNGGz4_YdT5DGAf8wyhfEIadSC-cA2dGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
گل‌های دو دیدار امشب اسپانیا
🆚
انگلیس و کرواسی
🆚
چک درهفته‌اول لیگ ملت‌های اروپا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30525" target="_blank">📅 10:02 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30524">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0IMVlqQdt7PwLHv9VxmuYUf2vyEb6cduabrEjvW1hVSbhpBiRNQb7KjOZrePbB96iU_DxVgXCK2KQM_iDa9ZID-dDx0iZcnv8mk4z1d9_vHim_5iJc8QEJ9fJAaTPpK2pTND6Eipx9pEPzxK9ru5VzKQJ6yyuvB8IVUMOz46vET8xgNlUn5FwJrrRBIpLfIWOomOzeepvb1N6Z5k_LNUSQs7s2iMr2ikT4sg3dSGa6_Z_nsQawGS_8YXVeTQq8iuoTFOYbKk1zIzcFUuma77UT9vTXEyN392OIJE5KdNlET4BN4XiAzoiMAx9YBwTIoFAgkfB02afI5mXQzEj3TUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🏆
درخواست کتبی پیمان حدادی از تاج برای برگزاری جام‌حذفی!مدیرعامل‌تیم پرسپولیس در نامه‌ ای به مهدی‌تاج رئیس فدراسیون فوتبال برضرورت به برگزاری مسابقات جام حذفی فوتبال کشور تأکید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30524" target="_blank">📅 09:27 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30523">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/826b26c676.mp4?token=jgwhn7cCpcZW2NemmAhNw7XWfdYrDlyBiATZYoGgfmROI2qD4qORU-HIC0HpACTCvik6094dyHa96icY-yrgEA_lUZZyKwToq_wqrqZIMvhXE-mocBCu6JDP3wz4yI-TqSupwb7ciobciS2qwdWvNi1SnUhwjNh1y6f_F_XQABX_5pSq8bXRg6xu50OX0RQbEsy-P0DvSaMnPdePZmXwGt5wXfSoppn4IVMh0tpiYquf6KLOZG3HpxKiN4f8y0UzEfG1MpOFSlN19_a2XsK791V9qj6WpqOvOI3F5pCPslfLIn84pEsaNz4DNYnt0vRFYjlycAhs62r4uVWOx3pG0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/826b26c676.mp4?token=jgwhn7cCpcZW2NemmAhNw7XWfdYrDlyBiATZYoGgfmROI2qD4qORU-HIC0HpACTCvik6094dyHa96icY-yrgEA_lUZZyKwToq_wqrqZIMvhXE-mocBCu6JDP3wz4yI-TqSupwb7ciobciS2qwdWvNi1SnUhwjNh1y6f_F_XQABX_5pSq8bXRg6xu50OX0RQbEsy-P0DvSaMnPdePZmXwGt5wXfSoppn4IVMh0tpiYquf6KLOZG3HpxKiN4f8y0UzEfG1MpOFSlN19_a2XsK791V9qj6WpqOvOI3F5pCPslfLIn84pEsaNz4DNYnt0vRFYjlycAhs62r4uVWOx3pG0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇦🇷
آنخل دی‌ماریا: اولین چیزی که من با حقوقم خریدم 206 بود، اون‌آرزوی اونموقع من بود و بخاطر همین باتلاشی که کردم بهش رسیدم، شاید میتونستم ماشین بهتر هم بخرم ولی قبلش میخواستم اون رو تجربه کنم و بعدش برم سراغ ماشین‌های بهتر.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/persiana_Soccer/30523" target="_blank">📅 09:14 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30522">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXQ2SQh5AaV0MRAR276TpiaTkrKqchlfvuRjsV3QJWGRWZ9xmxFTnbvXolsXvnRBr5hGQziUHVehwn3lbuwMdUS5kfZzuwxOQ-V-4n52GxXCdmHaOTOjKw0597m8QfhCACkkXgnojwkapHXCDo9qdTUVIBeDBu3OoH02cpyNfwQt8_5LJc7NAPSsCliyUF6Ed-cckVwagcyWiQuZYAT76E8qJRz8grr8Me5UBqyGQ4dy0AH3kqrFzWMlFeFNFrRwpBumuP7URSNGnNwGXwEiXKXkyfRV_dvR9BGTxeToX-QJNKh1yg7xhg0yRTfujdWv1x6WMab_dEbg583dI1ik0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علی رضا دبیر رئیس فدراسیون کشتی: از تمام قدرتم استفاده‌میکنم تابیرانوند ازخدمت معاف شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/30522" target="_blank">📅 08:45 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30521">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lEUJI2C1-8CMqPnw31JHRyeAHBsmDaEaKgeXFu1um9S06DD4XWMQ4CDoIaoUwoEZkGX_CMHujSouJe8hkq1jhi80IV5qUwGLhKpedWW8sblfDPqsG9-yNhtY_ds_wi97CxrCJsgU9fXWcSh-pLHZUQu-ofqvpqFHVqKwmD3GflW_uoGNg-Kqo_VrWt1hL_wrArtgJDuxPRoVwH61WcKWsKH1SqlEHnnVg1W3rwwii-RM-wDJhHd9BO4hUtYvbqAJKTUQOB9x5fnAu0FHZz8lqbV1pqyUgV9mq40q6QGj6n65IX58bjlWVI2opFgxLuVtagG9F_Bl9cSuU2AFH5vOow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
گوگل رسما ایرانی‌ها روتحریم‌کرد و از این به بعد مردم ایران دیگه نمیتونن‌حساب‌جدید جیمیل بسازن!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/30521" target="_blank">📅 00:43 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30519">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/009c394c65.mp4?token=AjodJMRB35__ua7yZ1PC3TRpvc1bgVtqoareP6PB2YY7zsNHOfyzA3s67pBKruCWb2pVOCvlsvyrNnFpWZYvl8asCn2cv9dvBJYMKlSp7o9bwZHy75zbNlT8RBZAt7kuURs0tolF2Oz3lmUjdgABAca045_4e9WGu0IRulT2Z5wA1fhIUeJy99ZY7-Ad11wNcgxfFbNVYGtRBl-zqSV_O2EJvycRvyNOkxk-2BQ44xWR7jim5oUPphnK2UxyDTbE9vPM1tyHWBNpKrQMT1YvR4TRydxe9XajccW8r8iCEyZYRuMRkqESkntghaw7bc_tUUAehqhlAJiDlI3YlKvyOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/009c394c65.mp4?token=AjodJMRB35__ua7yZ1PC3TRpvc1bgVtqoareP6PB2YY7zsNHOfyzA3s67pBKruCWb2pVOCvlsvyrNnFpWZYvl8asCn2cv9dvBJYMKlSp7o9bwZHy75zbNlT8RBZAt7kuURs0tolF2Oz3lmUjdgABAca045_4e9WGu0IRulT2Z5wA1fhIUeJy99ZY7-Ad11wNcgxfFbNVYGtRBl-zqSV_O2EJvycRvyNOkxk-2BQ44xWR7jim5oUPphnK2UxyDTbE9vPM1tyHWBNpKrQMT1YvR4TRydxe9XajccW8r8iCEyZYRuMRkqESkntghaw7bc_tUUAehqhlAJiDlI3YlKvyOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
هفته‌اول‌لیگ‌ملت‌های‌اروپا؛پیروزی‌ارزشمند یاران لوکا مودریچ و کامبک‌تماشایی لاروخا مقابل شاگردان توماس توخل؛ سه شیرها نتونستن انتقام بگیرند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/persiana_Soccer/30519" target="_blank">📅 00:35 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30517">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCBlTHHF4M2HcPkdYVYvj6Bvt3rD-9GSs7Z0m7cfPhUC1_9WiiDF7XAiVSNSOjRIW6vjHqp-jxtxbjTP3kkV8cMw1JEqqQuLdro3iXZRb9m3tIUN7rzx56j5kzaIf0hD8MxFkqafO_1deU58KNDXFkJ1BlfeM2iplCXWbUeuXL2vHDRQm3uLP1nwf6lCI75GHL9mxXdlwOSfKRymPnW6xE6mqjMFbk-h5SDaZChQFtvisUWRj6qpMOnGcH4yxEJPlFtHBYe8fU13bTT3BpEBK93Vtm8CUPzwchXmL0NUpd-5fuuELAZC6cNSiBnEGgdutpFSDqSnwV-e2ong8vBcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌‌‌‌‌دیدارها‌ی‌‌‌‌‌‌‌امروز
؛ اولین رویارویی رونالدو و ارلینگ هالند با دوئل جذاب دو تیم پرتغال
🆚
نروژ!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54K · <a href="https://t.me/persiana_Soccer/30517" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30516">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tU2Kx6ylZg0fUpIzknTODbSOfcIv_OF34ewScRA6qRSCm0Ot2CPPP7VsQHCC8M4szHC1qei9vLUZiLyFg8CjOJ8D1odkDCFDlyEBzgaB35uUjPPueotAjZuwUNzDc2zxHn4-L9ckRTEv47UFr5HcUUkxjclGiUwNlnScf-Vej03m6N2xG2HqxDEBXYhObQDJxr7wul0kSW5k02kVY845IHoEnBtlY_vzCZvUt-aKbDFVh_itEJ0usayyYqmxOUjSuZATmYKUXe3af9kAdUP6l1_UTMqzbatGoQMtoqiWhAZIVSVS6Wq24D2RRJYQaR_BaQGCRcsQk_ASeJOJDE0KpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌ دیروز؛
برد ارزشمند ماتادورها در خانه انگلیسی‌ها بادرخشش‌الکس بائنا و لامین یامال.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/persiana_Soccer/30516" target="_blank">📅 00:32 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30514">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JHlRuJt7Q8tUKjxbp0JkmA6NkqXu5a66-wFU1nQ6qUHAxofc0bQJyVHrKbJMurVOn4_cVLogr4v9WknhECbtoyZ17JBWGWm4Uvras7zhzsbr4Z508YLD4BvL3G7LRWiiz8HQTuLtdtRQMpYRKprDCq9Kfynavcg4qFDg-M_w-fqSORyP-UbeY8odNRjZTHvIDBS51GtQxR0TEAEiyUjgc0gI_3iwTr3DrYcX4sEC0KfIX30h-JYZbAG4BrwRINvduODKozqwVzoDJFUVnm-3HCXJULIlCwRIT68ZlS8LIRwmnZtDTnjgMzeocauNi099q94QxZFj4Z7mI63A2ZOwsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛ شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30514" target="_blank">📅 00:17 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30513">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N6QafkaRIXwEciS1XdtVUnqZW-eHskcdiqvGlODDqSj0yEgD4BFTHQJOWPD1skeOclPaNhhoP3V2RJblS14WnvbzJoboBNqAn2qJXo72qbG9Y0B-NJlQbOefr3h6kTnGPWFxCXvo1v_pCsKJzJRynHs1tmwGBO5HM85gUSCir-qP93128rILZJdFj7J3MjrGuCXBa6na4AWVS4octwDvMefqQaTFapbDS-nyOkj1H-lmoBzIfWrT5MUBEEOTxXguzzh0abLTcl143miJauf1x96Yeofh_guGWJEyQZIUlBRpjxILpf-_c-qPsrm5-RrpPoSIOpvn0LT_HCF5TAPjLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛جام‌‌ملت‌های‌‌آسیا آخرین‌‌تورنمنت‌ حضور قلعه‌نویی درتیم‌ملی‌خواهدبود و بلافاصله بعداز اتمام این رقابت‌هااز تیم‌ملی ایران کنارگذاشته خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.6K · <a href="https://t.me/persiana_Soccer/30513" target="_blank">📅 00:05 · 05 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30512">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fgV07O1VUfMIpX_2MNCyRlmftezo2MVYEfVekBByFJHyi6iBl_6j3g-5zRNDMm6aPQQ7IJr7UTeu-fJmYBe4hv-L0MxECBoI2Tx9ZGY98S4EWelxibL2lpOPAL3W6-sr_J3L7knod-QW0d0Oud_BgVfjH4nESFIRRateuOEExE4qgBDawTJD6I56mroHyTlMPn9NbB7En5lk30qAxMh-z3pB8mrKfIMWYBB2n2z9oPvqBHN4AB2rvQprUB5TUWpcXjSUFyRK3Zp0uBHYWtbUXRp36mBi3b2tBfp68fvd7dtWkZ3KQ2V7aLXD0jizO0BGg2tBQ-WyIx1tGRV1FSzWdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ تاجرنیا پیرو خبر اختصاصی پرشیانا: فدراسیون فوتبال صراحتا به ما قول داده اند که جام قهرمانی فصل گذشته لیگ برتر رو به استقلال بدهند و ما منتظریم که فدراسیون به وعده‌اش عمل کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/persiana_Soccer/30512" target="_blank">📅 23:51 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30511">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rSkzw2Q1Od4nUkkgGlPZlU3LlIih7VsBSfojVjHJcg1FOTA0w1JgjoaSjzOJgFPFfD0MPKcTFAl4ryZhB5qmcK_fLnaFcIyQOBfzoPox3WzZ_f8nUBaXiRauWttmDiKjgshUxYtX-64JyHzZuqH3yLDo5XdRubOKJNpPCXOHnGQi3Qlz-qDYs4UtxnHPwgukKa2AVGvkaIG8rr7w9Fp3D106XyUmPC45wquuiKzKTBSFu7EejjHZOg-Goo4uzclybkUuf3ca8OHsqtE_Qd7rpsULtmo7A-8Kqzb9io2bcj0NH9VeYDCXNXETmAt97QjZYLG1GSh5YyCaNals7wfyXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇫🇷
#تکمیلی؛نشریه‌کوپه: بعد از آزمایشات گرفته شده روی‌زانوی‌مصدوم کیلیان امباپه مشخص‌شده که مصدومیت این‌‌ فوق ستاره حاد نیست و امباپه بعد از دو هفته استراحت به تمرینات رئال باز خواهد گشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/persiana_Soccer/30511" target="_blank">📅 23:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30510">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fatzD4l4efJD51ijEAa8jO3Af0MqX6uXHdlJHzZ3gj_iVrfluVScvs4gMxbV652c7wJmUhsCN8qqXLgEiVKVhMu_6_wSBAe0Fn2fI4EE-5Ig8ohSeRb9p6K5VAraKMCpOrTY2XWwNA-saHg6lbVuxX0VLKirSM-zAbTYFRSoWL3Q0PcL4srAaNrN4pzeXcUEnMDXuqhF3kqByt0Wxc4NPR2a6AsAD1Nt3HKMNnypbuX7KUAtPCkymu0cMoM2exWbv8uNzyRyvhQS3Jvhk2jFHVm35pEABi73wQRMNPOwaqUMXcg-UMecqfLWebJNUU667YISU2Lo5dQFPKPnWv490A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
#تکمیلی؛ ادعای بن جیکوبز: خطر این سناریوی فاجعه‌‌بار وجود داره که باشگاه بزرگ منچسترسیتی به‌طور کامل از دنیای فوتبال کنار گذاشته بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/persiana_Soccer/30510" target="_blank">📅 23:17 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30509">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VXX_PYZYWwXkei-L1Oq1jMLZtgtnz25qQqxRWznnGf5myMqlMuz_Nq-ZVh43W5hn2gFNWxEIWoRVWc-jclCo4DGsEg3YJp7S25zvdvi4YC0P2QN7a3cZlc6s15EsdjXG3wOl1dN3s_b2GOjtoFm91dBulKTEdxEwqGGkiPqaHNf_j9QO0YRGqsG3X0A7RoiV0BEx_Ndbj2BKS9t0mftZjnSoEH5_UeP8wM0E6NxT6fZs-XpAg_evt6nG340P5DBJtSa-ssGm4ajIKoggZX2KyiOPO8aw-ARU8DwUMIXq1kcqiiwUw1eOQl8JTQyKrHq-lcPbXXtcOd6LnTxNLvxJBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اگه تمام هشت قهرمانی لیگ برتر منچسترسیتی از فصل ۲۰۱۱/۱۲ به بعد پس گرفته بشه و به تیم‌های نایب‌قهرمان‌داده‌بشه این شکلی میشه. تو سایت‌های شرط‌بندی احتمال‌محکوم‌شدن منچسترسیتی بسیار بالاست و ممکن این تیم به چمپیونشیب سقوط کنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/persiana_Soccer/30509" target="_blank">📅 22:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30508">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NH2TmN8XBTC7Y97G5HZLj-c0QDT-c_cwVD9M68cELi82VJFgZYyvkBtYD7N2T5YxRyOtBw09v4wDbt6IAupsfuAazSWqo3Qrp3_3hsE7VqT9WkX-JIX-cXZ5IrjMvcSnluiOCqv21vsCwdDGCSLEmGDf-zEQqr426nPwIIm19GQnXzuH_51pM_eriz6Dl16wZ3ENe6dPPfquApqBTRqqEyhEnrWcJXmuPKoF_Qam9pLg4pL6xLZalBj4G40R7fvaKTIP1Y2blPiTw_cvSk4IDMXFdIklE6e9jG1Syuyt63ljnC-AA4AeEkjVZ6rYyBWa_s3plSbpWkmsh79yhk2Ghg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#فوری #تکمیلی #اختصاصی‌پرشیانا؛ مهدی تاج رئیس فدراسیون‌ فوتبال عصر امروز به مدیرعامل هلدینگ‌خلیج‌فارس قول‌ داده که روزچهارشنبه باشگاه استقلال روقهرمان فصل گذشته لیگ‌برتر معرفی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/persiana_Soccer/30508" target="_blank">📅 22:26 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30507">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjD1U3CC9_hA_ucGNBf18wcVCf6Ej3oyBKNAiiy2vevCFbskUQ8MPGtTPUjOxbYz8_wqM5Syi1bwMrcVbnMRwa0bgGYMqznqFfCV-O3rrXSAkVcviHdwIe0QjpuCkX_Zm1imaBRCnZlqo2HXXuSl7F5I46RqzkITLTSqZ6Uu9wwfrVTGhZXH1T5emkmdA00xCng-_XwEjPy9_911aV-vlBudgpRhc6u6IZBVnnACKQJrXD5Um75xhF7paWkreqMnRhl_ChQELj_iBOD6f0Wx4bkbZNwCEcW8VCd-WLOQcgNkztiW5l7mxEqu84DFp-A52e7fI01CfB0ihANyy3Zg3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا دبیر: مهدوی‌ کیا یه گل به آمریکا زد و از سربازی معاف شد. حالا به علیرضابیرانوند که ۳ دوره جام‌جهانی‌بوده و پنالتی‌رونالدو رو هم گرفته و مقابل بلژیک آبروداری کرده نمیرسه از سربازی معاف بشه؟
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/30507" target="_blank">📅 21:57 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30505">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uk_u5UqzOcd4zJ95eSVuKOEg4MPucYbcxAyKTZUJVMqFCL1Fbg4I_m7CabK80mx4AAT1XdcvFCwcft4SMQR8Ua6buV4GD2jtt_pvUgWe2zxa3PZivIUgkYbNZEk2jT-z4d29zQWBGDwicF3sD03cdI7XkamrkVovLMgNWtA6ppRbPe0g32SjUNDkSUuIzP1cggUqRdFvsWEq--yjQB2Dpcua0nEyPmPf1Tj1Xjz6GGUCz-n3l03MHkBd2GPUUj0GmEt5nFvH3KwW2molRXqlOZ1c3uWROlNIAktjcUq7Kc53urIJGcQRoeHVkIkJctP2SfsXoVj4xpcY67virctViA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JdpsnTILhfi4tv05RDd2lF4wd6NXJeG6W3SlzU9Yr2KojAeIwdIFie-YeoMNQihUDuxksi9hN5SMJlM9owaSYTJKmB6tdE81_zUcYETpaZHXvI9EIpfmVLV9mFbCAD7yh46divz5t2NOZvkKlCpsf79zTskKyv5N8q4xv6esxSy1IHS7qGjwHHw0mNpruiIoJAfg3ENPXBPkqXEVIa2-_9FV-EfV312CbKnLBF1oNjXn1MxFA-NxvkvD_vWjaGyzUmySfIlE23fFgMO5E0sWaUBbMzS8oqyMBtrdrW_9xIGbRn_-Cgk98BU9-eysgQMLfhdez5ie69uNSwn2F8TuMg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
هفته‌اول لیگ‌ملت‌های‌اروپا؛
شماتیک ترکیب دو تیم ملی انگلیس
🆚
اسپانیا؛ ساعت 22:15
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55K · <a href="https://t.me/persiana_Soccer/30505" target="_blank">📅 21:50 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30504">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EZI1jfFrW0CzzSHhBeyuBuBulJgWcw8lgz4gsfPoRyJG9-Y16RiSu638wmJ_-Q2Zliqy-dBlf8vxTNmxVPQvSU2Hban2PX9Ts9imvqHhw3ssmtrLC9Yp0Bhw0-fmFd5Km1SCv90V0Dt5niRVF4FT5U5i1FL_X0-RLtxMrjQ3XlunZRS4oGXnHtA58cBX21NEKDz4tQbdpgBQvQ69iK1EPJMZMTjQkbSgQBESV13lBN8ssVDhxm8BvzC02AKad1hCRlCay73Gu4o8StCDdihzXmJYkvVK73zss0bahCJylhExHD74vzDK2AmJ8keeq8f0EWrWZZ9LHWTF6e4Iwx6q2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#اختصاصی‌پرشیانا #فوری؛درجلسه دیروز هئیت رئیسه فدراسیون فوتبال سه نفر موافق اهدای جام قهرمانی به استقلال بودند و دو نفر نیز مخالف. مهدی تاج تا پایان هفته تصمیم نهایی خود را در این باره خواهد گرفت. احتمال‌قهرمان اعلام‌کردن باشگاه استقلال توسط فدراسیون فوتبال…</div>
<div class="tg-footer">👁️ 53.4K · <a href="https://t.me/persiana_Soccer/30504" target="_blank">📅 21:29 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30503">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BM5sy1A3vRIAT4vGPIo7TNu_ftJ00uVE0yIc6RJs7Bg3xty1SpmXtO6FBG38FNuGCBCwiga78Rw9gb0REpKcjd4dF3nrFRpekW0YNlfhjflTzD8EUPwpjIf_x6wXDEiP9fiza-7dguzrWSEV0J3WcQkQZIRg4HicDcL7hCza5wMtj2a0TVswJ_JlWZ1wkGkZei7k8YNR5Wrdymb_NrpNE8YmUgJh-ZLNOpJvmpNNIH7mg_V8hGzG_bYHYEgqAu_F3dG-6bStDNITc_wXLEF256KKVReRZnKy843yQdclPx3QH2xQR1wFs1O_d1cxxwUQuOMlymfqhwvNVPQ3UGfuOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ علیرضا بیرانوند گلر33ساله تراکتور به دوستان نزدیک خود در تیم تراکتور گفته دیگر برنامه ای برای‌تمدیدقراردادم با تراکتور ندارم و بعد از اتمام خدمت سربازی ام به باشگاه استقلال خواهم رفت. با توجه به این‌که محمد خلیفه نیم فصل به استقلال باز خواهد گشت…</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30503" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30502">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=THmHKfUyZK4ifDReK1qTaH3m3J6adue4Wyw9f8A5ZPBZSSVVpsf44z9tGoA3AB9T0cHIJMe8rZB8aqJhX3lJl44lziA673WJyVH2ej-FTpD4jWMx3NoF-YAZiGrOgXqO2Qx2EoVhvUsJLVO_N0yulApebctXkeD83N8iKHYX6xjVa2shInbyzn4rXa9zl096NjsKFer_6BvA-SYOJjjO0NDrdWF624wLOf3RVoM77lcRBTFv4FOdr8DOrRiQKCIL9C7hcqjO1UZpVHHNqZTHzgi3nzsSlWgb-P00rfW3Erg1cSzUQU5MhS8EqspnpLaI6f5bZ7AxcPjvpJnQPPAb_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/30ee53107b.mp4?token=THmHKfUyZK4ifDReK1qTaH3m3J6adue4Wyw9f8A5ZPBZSSVVpsf44z9tGoA3AB9T0cHIJMe8rZB8aqJhX3lJl44lziA673WJyVH2ej-FTpD4jWMx3NoF-YAZiGrOgXqO2Qx2EoVhvUsJLVO_N0yulApebctXkeD83N8iKHYX6xjVa2shInbyzn4rXa9zl096NjsKFer_6BvA-SYOJjjO0NDrdWF624wLOf3RVoM77lcRBTFv4FOdr8DOrRiQKCIL9C7hcqjO1UZpVHHNqZTHzgi3nzsSlWgb-P00rfW3Erg1cSzUQU5MhS8EqspnpLaI6f5bZ7AxcPjvpJnQPPAb_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جالبه بدونید که نستوری ایرانکوندا و خانوادش وقتی سه ماهه‌بود از جنگ‌داخلی در در تانزانیا فرار کردند و به استرالیا پناهنده شدند. برای آدلاید بازی می‌کرد و در 18 سالگی به تیم اسپورتینگ پیوست. تو20 سالگی به تیم ملی استرالیا دعوت شد و مقابل تیم ملی برزیل یک گل فوق العاده به ثمر رسوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/30502" target="_blank">📅 21:23 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30500">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqLu1m31EA7TnxsWUYwWG89hKt90jbV3Vs2Rv8QGvb3qUA3g7BvNb_NgnPbMtxAev6Mv1O6nGKlQr8rRKi8SjUlx17Me4DivE6hulcqjAgIGG6SvHfCZZM1Imh6w4Rg-1npCtqOfKnyNssxK9eahTmR541BPiPfNxjl9KJa6Vjm0dkwV7cdEdnkpQOalQ0u4ngAbyZNLOVOZQ5EQJRFQEfuRVA2iCpvZQiFDTNGqzPo7aZxGbC81mw16-lMyr39mpWI9h84MyFnC8g38M2qMp0yjxF0wVFsZvkHC2mdsMWKDZseT6pAhqrwgA3GRI2fKRxRW3SUZ_yBaLMpsA1sRPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇫🇷
#تکمیلی؛ بااعلام‌فدراسیون فوتبال فرانسه؛ مصدومیت کیلیان امباپه از ناحیه زانو هست و بدلیل جدی بودن مصدومیت امباپه، او بزودی به مادرید باز خواهد گشت تا روند درمانش آغاز شود. گفته میشود امباپه حدود 3 ماه دور از میادین فوتبال خواهد بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/persiana_Soccer/30500" target="_blank">📅 21:02 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30499">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lRtIvMcLal6FXXI_2dd38OSp0XFOQH53tEa8uLs91Vj_rnQgqat05I67hrveHhygRktVJkq9m5u8pTkDJBPDm9RwAD2B8KPxPSpGws8J796qP8dgf4alC9d7L42d1ughuPplhIdLkfn-a-v5cRnuHVnepNcdwc7tG_domxnQ4ebBzQrElsneD2HWb4yUvC2lM_KfhlG6N4ZkPEOFxomI-mZ-zaDZ-ri9wkozv6cWAdHlHaOWT9iWUXZH4rysKTSfw6oYuzYAJTcGZTVii7T9svPKlnFEnyV8wUoriyOuxf7G5ZLppJUgROq2V3rAHm1pmnS4ay-YbfwlZbn-bTc2SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
صحبت‌های تند و جنجالی اللهیارصیادمنش فوق ستاره ایرانی لخ پوزنان: میدونستم قلعه نویی هیچ اعتقادی به سبک بازی من نداره. تا روزی او سرمربی تیم ملیه هیچوقت برای این تیم بازی نمیکنم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30499" target="_blank">📅 20:36 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30498">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m2srQymfZWOp08mOtufEh1YK9uPMhMso9thaFac89y3po0kHwEMLI3U30S1Uan8L18yZ6wvXXZoQI8mj2uv8I8ws_oZBv9dRUTWXyoe3rvsx-dkYoYYDvCPxyYpUb2MZNjT4s5eKGeL6jrXtIe4XZZ1czZUO8jNbvyN33IMyx1fD73p3p5criej8WQ7Gh6iepZxUnFyFhJYO1993FY0tWTIThekvCaGxlfnWiMaM5veD9EriWOqLMoGwIxo8SI4wcp8cR-pQS80eVAnfU3fkTrFoY2r_1aN2q3CrelxGiAm--tJzML-dTOKTziWWVhR3gzL9CwkpScH6SgmCHliVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
81 سال‌پیش درچنین‌روزی؛ باشگاه استقلال تهران تاسیس شد. آبی‌ها باداشتن دوقهرمانی درآسیا پر افتخارترین باشگاه ایرانی در قاره کهن است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30498" target="_blank">📅 20:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30497">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUk-CAbsk_5Uc3wYi5PDM4gUiHUX26H5KHt35yjuK6bwEbDnHVjyhAQ07CylMXRW-v5YNsCWe7BMDT3XDjEp8uvdnDvLME9BqMMtwqsB0dOpqAa3sXFRUlHpFJycR8Y7KIxcVmHAsj9xC6ko3J7moAcCB1BhYcipucvKTF4IHwvzlnlMlk2KF5nfnBqgMfh_yApphWGnIUeDmlr1U_SUbrKFlWkNL6Xkirhqh33quBOdz2HQ14AoChFCA_iziFb2jLAnbCynw3JlFXG5hKq6w0Fnes0rPRWvqmeDXjwpttHdtlZ-F5bEp6rddFzz30ky2hGyD81tgWuXgAKklBToSOSo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1d9a03df6.mp4?token=crmurWFevo65Hn3JmTiwQ2uz5VljG92u-NcAOUTquf1sB_pLr98kNKrQEQ61yx4sNNvDuy-JzARWWvnk_t95Vr0zy3t_9dEr0klTXSJ2PWFfX3RqCQHo0fIHJGPqLBw1zpPpY4c63WU9kHfGq_Y0r1E--Kuw18MLAXnHM8gQNFEDz5axAQhF_9EoWa4v4LjCgSN6zS1tDWPHIN6Rww8gxE7d2xEUIhrMDdLBAbXc4oujmO-g2ir86o1nrXg5LIxntkzlkC01CMNhEZKB1OPDW4SplIjMr71Feb-N-cV5_OZh3s33g0fHQnIAypkKSo85WHZHJBvFMrMpNuRnPPqYUk-CAbsk_5Uc3wYi5PDM4gUiHUX26H5KHt35yjuK6bwEbDnHVjyhAQ07CylMXRW-v5YNsCWe7BMDT3XDjEp8uvdnDvLME9BqMMtwqsB0dOpqAa3sXFRUlHpFJycR8Y7KIxcVmHAsj9xC6ko3J7moAcCB1BhYcipucvKTF4IHwvzlnlMlk2KF5nfnBqgMfh_yApphWGnIUeDmlr1U_SUbrKFlWkNL6Xkirhqh33quBOdz2HQ14AoChFCA_iziFb2jLAnbCynw3JlFXG5hKq6w0Fnes0rPRWvqmeDXjwpttHdtlZ-F5bEp6rddFzz30ky2hGyD81tgWuXgAKklBToSOSo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
👤
ویدیویی‌فوق‌العاده از آنالیز مسابقه شاگردان امیر قلعه نویی در بازی هفته اخیر مقابل ازبکستان.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.3K · <a href="https://t.me/persiana_Soccer/30497" target="_blank">📅 19:44 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30496">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=RhNWqmNaVSTWuaTM7o5FF-N5Zzs3Bsb02q0YxnTrmPhNN-A7LNPbYe1I6ueCgKlHA9KOmRAaybCEf7Rs8JtRnm_3xKy_M0QC8xbIZZdWf55xrMtWbsya69HBEBQmPDY0U-d4ArIGlyYUX9FhILDODHFfZ2Wq8uI0_V4Hg9ba7oOzZdiyhjAPk7xlXzFXvDjtaB834zCxd0opjL1Yutysk_IHkISTXbu5Gbyv8xFejND2Asls98T4tGcpVsP1RkoVOy_wEbWC5TRA-75Hwm7_cD7ZmwGSU1zEld_l6u3rjN7ImBKjsa37AKCuFrQ8jiiThIBFm1HuXhNMvJL2eBc6jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/777a222aa8.mp4?token=RhNWqmNaVSTWuaTM7o5FF-N5Zzs3Bsb02q0YxnTrmPhNN-A7LNPbYe1I6ueCgKlHA9KOmRAaybCEf7Rs8JtRnm_3xKy_M0QC8xbIZZdWf55xrMtWbsya69HBEBQmPDY0U-d4ArIGlyYUX9FhILDODHFfZ2Wq8uI0_V4Hg9ba7oOzZdiyhjAPk7xlXzFXvDjtaB834zCxd0opjL1Yutysk_IHkISTXbu5Gbyv8xFejND2Asls98T4tGcpVsP1RkoVOy_wEbWC5TRA-75Hwm7_cD7ZmwGSU1zEld_l6u3rjN7ImBKjsa37AKCuFrQ8jiiThIBFm1HuXhNMvJL2eBc6jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🇧🇪
#تقویم
؛ هشت‌سال پیش درچنین روزی؛
ادن هازارد فوق‌ ستاره‌ بلژیکی چلسی این سوپرگل دیدنی رو در ورزشگاه آنفیلد وارد دروازه لیورپول کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/persiana_Soccer/30496" target="_blank">📅 19:21 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30495">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NaBlUs3_anPHjlIYXt3zhZ-UO-2SB4xPT8RXXWBxS658YQZOLAQ5iFTDa617s5yQ9BYwVwvd1-GaZaSizb6csrsnHh2ThC_S6QZmumeXXIGEvVPGXbnNzApYekzJDG3gssnXuQ54B-nqAo9Zw0DxgzQ5A5-LZKxkiMkrCEPWqzdwrln9gdonOr8QEUMi_AOsAIe6KSKOcLSSP655NvHsDaUkxuaFHoMtzH6FakcK6fecvq-Ee-QQrKcT7zOUsU8C4CiAP8NmQKvt1AqZZZgNfD-ylTVDArV68-HCLVd5vyc_eUwqKR6Zj-zXGW5YQ940MmgLtNjO38a4QxQfG30Xlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🤩
لیونل مسی فوق‌ستاره تاریخ فوتبال روز 14 مهر آخرین بازی خود را برای تیم‌ملی آرژانتین انجام خواهد داد و در پایان اون مسابقه از دنیای بازی‌های ملی برای همیشه خدافظی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.7K · <a href="https://t.me/persiana_Soccer/30495" target="_blank">📅 19:00 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30494">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇪🇸
🇦🇷
تعدادی از کاشته های استثنایی لیونل مسی فوق ستاره آرژانتینی در دوران حضورش در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.4K · <a href="https://t.me/persiana_Soccer/30494" target="_blank">📅 18:52 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30493">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n-wivAG_t9gxQDcW0UhLHchPZE4towSkhSxIOXpTndFhEmBq5pHj5uJ1LxQQDgP-zwGhU5GulzA_mMzyALptOFpxSlhIcFbkUid8hQy5b6t3q0IbY4D5xypKeqj5KUXZcJFF2vakcG40-BW_S41xrdYFD9KD_zzS3Muz0N7Sh1bjL3Rb0Srht87OI1jkEoq0TI-VPR2_MHt3OedsFkaacQCkQQ6Knj2xgd-Ruu533BNs02gW4L0ZS2ozZaHoAuDWrVY3T3X-YsFXMUVT4FAPah3SQjvHzuQLTvfLkULjgntVHqP11MYoFo77hyZN3TwLFrCXoVegAHKWR_4c_ov0eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇳🇴
رسانه‌تلگراف: قرارداد هالند با منچسترسیتی بندفسخ نداره حتی اگه این تیم بره دسته پایین تر باز هم بند فسخ ندارد مگر اینکه سران منچستر سیتی با فروش این بازیکن موافقت کنند. بین رئال و بارسا هر کدوم 200 میلیون‌یورو به سیتی پرداخت‌کنه تمومه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/30493" target="_blank">📅 18:08 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30491">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rE-CDaQCuGjEAauvhl2A3ak_fM7rWK2sgrXEMWSa8zDf_0112Fn5imGS_kafNdX5SCwu93qKmwQubNnrkAeHZP8uH_etRsSs53AechFnwHeJ6oTSpGlKmMSWOCAd2gHhgIAkZkXP8GrfrzaXVK87EchjbJRvsZbCd3i-FYQEQRoFJNlzN9WbbD3ocmzBAuwcnJJdUAyYn-uxZry2bgp2dVs34mPSGc5LBC-Wr0cnJ46-sgndyxnMp6RXT7FYC-fkL2fSOFzNWF4Abtjaz5z8Sn1ztphfmHOtPp2tmwgsMhdOGloJfYhsKrJxQFcUT_RSeWc7vsKG44nlI8ogLdYNug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/r37UJ6U5btyCWrmxvmwVboi7b0ESoPKlo3wdd3_JW9Z9041kOVMMOs4KKhvLiEYgXoVEHLTPOf3NtAQXsgj4zxU0h9o1EihJpniDRZ5rsti5tVsI35gKJxLKjsTLjZEcVd6c8OQ1Y8eEpc4s2Z9q9D9UCAhqFPhGckhyOVKo7yTi4AghwgXFZ9anIRNbIQvM18ti26cm1bhOYUDVSjCrZKBY4TKgxdYMPrVN4LxVGINATzru_ZdIGhZxwaEfsfh7k8AVUZCvq-b2pnaogQim2Cd3dnj8wE-AqJcrZ4CDW8bsJ39wGqiCqGDupLLvWFJUVjB53rT1AtPJWJXkCe9ZvA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
رونمایی باشگاه استقلال از آیتک سلامت ستاره جدید خودبرای‌تیم‌والیبال این باشگاه درفصل جدید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/30491" target="_blank">📅 17:56 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30490">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G0fuPt0hgYLINIB64uy5irSd0peoSE3ySlxAVT1gOVuqHVHMhxRzMxriGIQ4oFerEm4YXk2oG4rwG0uvtpOpAE2Eq91UBd0K273WI8MhGr2e7SOyS68nc-oU23r6nFls0_F2ufZcm6O6zpfzwjdUhxibvRuDb-NK7N_jfmw9X00QJ55WO2DInhVhB_t5mLewWTI2SG-t2WJy8QkBYO67VOPP_g_t3sFjVxfM1dVwRGEqPkYkNVyFOVbsfogUkg_8J015LKxfddQKzEvFUSMM8HUc6aQKhZe-Y3fFVtHGUawER_7sdSMQ5h5lG8BjGjNAyThiNXERpVQlMj5rCLXxbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مقایسه عملکرد لامین یامال
🆚
هری کین دو کاندید اصلی دریافت توپ طلا در فصل 2025/26
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 52.4K · <a href="https://t.me/persiana_Soccer/30490" target="_blank">📅 17:55 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30488">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GRzxmpxqRoRPcymWd8Y_2hIv3yhFUvT10ABapBBrPedZy7ya_o2wkP5Kxds6fRGCtMVpHg3MSz_PfamSd8oQvgjBmMLG9t2j0m0ftYsVE6sDbyDCEbW7AplZ8MoW5qYdFrNG6NNCksgj-KPH3zMcr7zV2SON20ZqzL26awY7cnWnIpfb6p9JVRlQd7c_NOk2Kd1kVWemj9v6gtPzPYz8o0DJu2_UIEBsLbb5SNPMzNdASRuJQS0ZWQTntysuaBu9G5e9L3WSA7Lapqk-n-X4PdF3DU8beN6nBGP3KY3eQrXPXuVvGfaIGpNZhukSYTSYTQi3Yt2U0g2-890QAwznlw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مصاحبه جدید دونالد ترامپ: پیشنهاد ۷ شرطی جدید ایران را رد کردم. مقادیر زیادی نفت هر روز از تنگه هرمز عبور می‌کند و شب قبل ۲۹ کشتی از تنگه عبورکردند. ایران می‌خواهد تنگه فورا باز شود چون خسارات زیادی از بزرگترین محاصره متحمل شده.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/30488" target="_blank">📅 17:41 · 04 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-30487">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GbhVIyQ_xJ6RWJHkz4dMYsNjVnLF5vFgmtiaxkt1a2FnuFnoxbRlmVSLRSaHmMU0V8MKbKQ_Y60CjjJOSsfksKpz5Ws7BxeIynwR2sE1Eg3kjL4chLPvWrnUw9tAhtCOX8Cx6jGyT4HIszbhiPuiopI9_z9KnhIANrCA0_oJSiGuux1weSG9SwSf4bZsVIFKlY2OBDJ6gCdILbvticDBMnYrcJhzTPyEqJd6jS315Pgc22-fQdU5qqO3Jjsyj5RRmPy1YkyLoY4RRtr9_qBx0TtJqtqxg09ZJPpxfnxgJ_M3pb8TP9XW2GkN79Lp2LPmNMntwuu6qUogvzGY8gWPZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
یامال که قهرمانی‌یورو و جام‌جهانی داره: من دوست ندارم برای بهترین بازیکن تاریخ با پله و مسی رقابتی کنم، همین که سال ها بعد بگن یامال بازیکن فوق العاده ای بوده برایم کافیه! ۸ قهرمانی لالیگا، ۳ قهرمانی‌پیاپی درچمپیونزلیگ و ۶ توپ‌طلا برای پایان دادن به فوتبالم…</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/30487" target="_blank">📅 17:20 · 04 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
