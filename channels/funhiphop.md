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
<img src="https://cdn4.telesco.pe/file/hWWkRlb3XDRzqKMtS02afyW8KJDzosxWCbyIN5EshGkkU6dIrmGwStyv_vXucwY6Hxcz6nB7-cPooDvbmHPhnK8aoGq7UHqByjXbwRyUCd_s_TmKFz5oRAhMTjEFe2N8ksepKMdsGW5ilFdizN7Z9U3s7dDVKwPQeMxgJKTLMZ9MtN2Y-wqVIe-FtzUi1b6v5A02OPERhXjwn5kQtiKk-WkcFsUg7ZQR070SvhAlmPxfa1GCud17dmEek2gpoiblW0tO7M4J06a7DM43GnpNwRGsLfnqzQ-XoEmNFDO4Fv3Ei9X5rdKAjxjrKYGd0ZwFBS2ZAs32mZ34IjlSnAvztw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 237K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-25 02:03:36</div>
<hr>

<div class="tg-post" id="msg-83515">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YmiZ8YKeYdE8wbddu3joQltm_B2JezAyFrt5zYxvSauH74d4j5MOwIXKJTNAVeGfsU4r8yLI2-cn8BIdfFEVlh_kNdPzIikmsrkpRzzXsUhrgbBi1Z4c-AzJ39Z37Cmy9poe9QA7w0KrkjiQktFa7b1HBV8drej7Zx2Ag3jJw_gcoMAr_6wlN2RS1P-_-rOHdNPzSMJMvVTY1jCfgdMUMS3uD-a44M0sL60UbE1YxLRJo5I2vCL9lJ23XJuHcu4jR53x2Pdn8Mc__RDFm1e2bo0oh55rvzWjt-Dwrj_7xLfWpOpoof2mXFHNQTzgMQgQJk7tDiMajnqRwycrWKYaIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعداد رپرایی که تو این کنسرت حسین تی ام، بیگ شگی، تی ام بکس و... حضور داشتن بیشتر از شنونده هاس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/funhiphop/83515" target="_blank">📅 02:05 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83514">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08141ed2a0.mp4?token=u99zdOHqUVFQUvX1cLDyrKxVyCHcwZu6QMnYAzjE9BdiaHtSNjBwn4VJWmnMfyob8FAn2K96GagguyT_AjgCOeePdCcKZdltOwopsm1UpOR5kyRvuiKbAa3fGao6U2yiPh06on6jcB-kVkarjq0L6ZbZouQnQD2Dy4c24VGPnbNa35z8vq8WLab-YJ7Vr7HJYDahSL1le6dGbFFo5tfP-UDPUSZu2H96YJUFFVhTEiDn9xhcMTxa-rKXGSmbNRd0Ijxe4nCUN315LOF54bYfK0INx6XudjZyuSZbZ4NJU8yulwoNJ2c_A1i9dNF_1lYYjcoeq7A8CQBPfqm2oOK6rA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رسام سهرابی بلاگر شده و ۸۱۹۲۹۹۱ بار از جاهایی که کونش گذاشتن ریلز طنز دراورده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.28K · <a href="https://t.me/funhiphop/83514" target="_blank">📅 01:50 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83513">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">این فلیکو اخراج کنید ناموسا، ۷ گل زده اش تو بازی هم حتی ضریب خوبی نمیده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/funhiphop/83513" target="_blank">📅 01:36 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83512">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi)</strong></div>
<div class="tg-text">آمار امروز:
🔴
1.49
🟢
1.78
🔴
2
🟢
2
🟢
1.8
🟢
1.34
🟢
3.89
🟢
1.67
🟢
1.44
🟢
1.35
🟢
1.4
🟢
1.6
🔴
1.9
🔴
1.46
🟢
1.24
🟢
1.8
🟢
1.2
🟢
1.3
🟢
1.3
🟢
1.3
🔴
1.3
🟢
1.41
🟢
1.85
🟢
1.5
🟢
1.3
🟢
1.5
22وین
5لوز
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/funhiphop/83512" target="_blank">📅 01:15 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83511">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">بخواب بارسایی رئال برد</div>
<div class="tg-footer">👁️ 7.4K · <a href="https://t.me/funhiphop/83511" target="_blank">📅 00:53 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83510">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/huefKTYYK54k-9kvWaZQuHKB0s7APoBT3Cip_nsVwAoHUVCvTMdFpCotjaEkajq0gENeVDw52xiuDd_LETHoz75IyEzCpC_H1fXDorNNCm55XNYO-WGZ_M3AvCNPl0wZK76AIf1FnHAaKQYd1BnypeYKMP5Hn1COGmo3FBxzGHDXDG-JUILcPuy-rnsoBPcsZpJYwqFAIPcUnXqDuhZC3TBFVAzuF7nOQi9cybLBN8h0yOzWc3cgVdqf1c0Dr0u6CGGvbh3sfbuz-E1D6AzApAcUbB7UvCWTNF7p3gaqc-itpUmfwv5ep2ztkb6kf3iVC6RaUKZTvM_7ucIcE0UbJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقت خداحافظی با بارساس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.99K · <a href="https://t.me/funhiphop/83510" target="_blank">📅 00:11 · 25 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83509">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PgoDmkLJfKRUGHjQWmxoKjQp9SqTfF4DmYVXm-qwx4ys9IPv463mCLHcnRIfPZ_-oTDsd4k4-uTAXAS_pYw2lLoubV54Zib7CHeZbKgQbYTL1ELFLMY0obsXy6fJdFfePmxc9E328g9-S3pyVhKEH3xSZBJCdwUMfm3BjQoh-BGEn46JMrMecoIvDR_WHboHuIN_trtkq0GP6oRdoXWszUKaGTXvYHuW3-FEBifRnjUa1t3ZEQtenCh3Tbfi-HgdVy1n0lx6oTka2Rd0pCEF8HXJVlr4419FXiohgr3d4yCWxpWoN7pbEQV2Z5VIuolQ71bGn6bgP2wHA9vdSeAbhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83509" target="_blank">📅 23:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83508">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83508" target="_blank">📅 22:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83506">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپشتیبانی تندر وی پی ان</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tzRNcBcsAlU0SqVzAeez8vGIiptvYdxnmQXLyY18vN5REysrWIeDvotsKNsrMEbijq-dEoPHxvtr626HsvNQUvqkcJoZzY6YNuBSDaD6S1drqMWCAlOv0eTlVI9ZutlXePdmLvSckn_qS0yinyPN14kGV5JXNjXY0YaKi7LLAP-93M461PHe1Xd-lFoFYcizqgvcsgLABgzvC99NuuMB1j9QCyCy-q9PHxsqeEMDa5BR8AUlz9NQ2HkfMJVZ7-nPuRdNSEWmtCb3dp9dfY4swwyuV_s7EyB0eya-YizZirCF5cWvQusyINV36kqkhlro8_UpSPIzmgBNSnGva3XIxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارزون ترین توی تلگرام و ایران
🔥
هرگیگ فقط 4900 تومان
🥰
تست رایگان و پشتیبانی 24/7
✍️
بدون کوچیک ترین قطعی و اختلال
💰
⭐
خرید از طریق ربات بدون واسطه:
🛍
@Fastundarvpn_Bot</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/83506" target="_blank">📅 22:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83505">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a69179260d.mp4?token=a-E1a4aFONCp9-DAEdu6tErJtDrV7f6AehEDiI5oBP_b3E3lKTzhjLob44DRH1j6oicdHyGuIqqMxKb4INM9O7lJS3zhXgL6woOLMOfqKtTQYS0jrPPsN80-0cThyTcnvcl1mX6HqGSCxMmMi2PEl8aXtpHcRn0QB4lq3p4FUmZdRPJg_Ij1155AMB34WZn8KiJFepgDePspYA0cql74oLb57Zj3YAIlZnKLx6Ijk-DQgWJDP1vfDJNp_llbDrAv5q_SgCMgO5PTnP6P4Elt7wOgThun5NAgKRESc6rjHkpMzEox7BtSIOby1nSHPsTyqxHNTUQjHlsOq0Tg1WCMAA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a69179260d.mp4?token=a-E1a4aFONCp9-DAEdu6tErJtDrV7f6AehEDiI5oBP_b3E3lKTzhjLob44DRH1j6oicdHyGuIqqMxKb4INM9O7lJS3zhXgL6woOLMOfqKtTQYS0jrPPsN80-0cThyTcnvcl1mX6HqGSCxMmMi2PEl8aXtpHcRn0QB4lq3p4FUmZdRPJg_Ij1155AMB34WZn8KiJFepgDePspYA0cql74oLb57Zj3YAIlZnKLx6Ijk-DQgWJDP1vfDJNp_llbDrAv5q_SgCMgO5PTnP6P4Elt7wOgThun5NAgKRESc6rjHkpMzEox7BtSIOby1nSHPsTyqxHNTUQjHlsOq0Tg1WCMAA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی ایران حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/83505" target="_blank">📅 22:25 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83504">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">بیف اصلی شروع شد باز
تو تنگه هرمز صدای انفجار گزارش شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/83504" target="_blank">📅 21:18 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83503">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">خدایا گوه خوردیم درگیری بین پوتکو آرتا رو پوشش دادیم بس کنید توروخدا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83503" target="_blank">📅 21:08 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83502">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">انقد نگید چرا بازی پرسپولیس شروع نمیشه کصنمکا
با تایم تیمای شرق آسیا بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83502" target="_blank">📅 20:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83501">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تیمای عربستانی تو لیگ قهرمانان آسیا جنده شدن</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/83501" target="_blank">📅 20:20 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83500">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p64STA5gFJha8VwOiaEfQbTWK_hVsYpcpt18o6ZQaCf6Az-1VbEWcNyCO5PrBf8eoV0Fqu7tWoPueKtbNniEXqnDDvwe2ITr_UWFJpYuv4R-0YISFJ6IydKH_U8-3qYbCdvtdZtxB-SXzLhrRsmZrE1tqcJJZidwGand5DZ0ik1yluQsiXauhonTf4WGthaVePQjUKI1py8QYf5ciaTEpFv2Ryg913kxkkq9vJcF5Wnmyb-rFdB7uPwQD0T1r4wJ-bXFtTqG4TRZBmCGcaqtHHQ2z3KVIhtlqAopu6MX4uBbRGGyvfzl74o4ilMgdUZ4OyH9lPOc1cgtu_mt9FTC7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منم همینطور واقعا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83500" target="_blank">📅 20:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83499">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">فیلترشکن JumpJump که دوران قطعی اینترنت خیلی فراگیر شد اطلاعات کاربرانش در دارک وب، به فروش گذاشت، این اپلیکیشن اطلاعات حساس مثل کارت بانکی و ولت و پسورد و… رو از گوشی کاربران جمع آوری کرد و برای فروش گذاشت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83499" target="_blank">📅 19:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83498">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ij5UJQBp989nvMHvl-rH76a7MNL5gORDl0uH1ghZI2436_JbiGQ3b3ibbvDI0xohFn6rI-hddt8YavRNqSyPcdysKjAyz6dzZVPjgi4AAqHPHhHLfkkCUezzHXQ8VPSdDjcEuTrOatliWf4fDPvnUYDyH_eSX4sHiQGPmHFl78W-56RjZ78lTvZGiln0_3InyHYb3kX-hpN7ih0BCYx7VLWvQxQo2uekDC5x3J8csIla9qTilYUIhY6Y1sZwK1sW5qKjvjUcXm1tR25l-gzRb-x14w2ev7nM72Yi7gjNKiqJmJq49PGlS5k42yF1KnW_0huM9yHkaO3c9o8rJTtfjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تا حالا هیچ کصخلی از دید به قیمت دلار نگاه نکرده بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83498" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83497">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83497" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83496">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLZS0mp-xDBhZRLzcL2vVZ1C8B8GGDkWkYJKqC7-1YXC647ORpoZ7K3fL_ROxduBHFS9VzXaRe582kdaAcVGhZJlUXC474UXwkw7QLR6CuPq1CfIgExAChL7IOWL4vXEDXz2LONhz6Q2nTtxKiXGJR0z8rTqbdnoY0qnmK-hkbarAEmIn7lGyjjy4vriDYvCLOaUarKhVEs3RQqUSmBSzbcEUWGfkI42HUMqQWzaWySNTLborqaulJzLrC8Yj03kioTnsKomRdzi2vJ40SOH9RlMAPXCd72osRRTbjBjrskehOAaFLG0OUbRq0PAVxOZ8mAWlgf7azBmiZ7JZ2mQ0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
24g
🅰
🛒
ورود به سایت
👇
✅
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83496" target="_blank">📅 18:49 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83495">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CsDU9SpVeSfLausIARnag0hG2iwh_bTeITPKhbj5z9Z5WiyFnXli-jZXVEuKm5hZ2em6zjXABKGWa9bvpzofHrD91dc6xOLas-biTQZ3B3X8hepWw0JVh9aGCjvSl09sU1Ox7R4ZdZbKnMoQjgN4Az5KtQAYNr5QRp5AfsiTKBzUFOcgAHI_cefWAUqawljLYSYX3OZK8UQeqxlq7eDVi4uxvG5Zk_s6sL-sYEeV7q8hLAR9qW1Tq5yZ8S9fxCnFq9uKhq5ozB_6elpSSnCVAMWo9kwPFAWNL6mB-gdA0ORXZfLl8UwBVUS3ZhgZlGiIG9FaGULqD0H7uvAZaxHqLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خلبان آمریکایی که از ایران نجات پیدا کرد پرسیدن چی بهت انگیزه داد که با دست و کمر شکسته؛ ۲ کیلومتر راه بری و خودتو به بالای کوه برسونی تا نجات پیدا کنی؟! گفته تنها انگیزم بود که نمیخواستم سر از صداوسیمای ایران در بیارم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83495" target="_blank">📅 17:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83494">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/959d87b013.mp4?token=gwFUlPdDii5zGjx_acSkiNfEdL7OR52STiz0gSaxPNObPgRRig4eKV5fS7p0ROJf-xtG3SdDm6A2K5No-SLBc1bupgXk5jdhDhJu4BBH2WHCpSWIyoCU0YhLkg5zPEBHqZf_uyL5ayiAYWsPinqyR4i3VeZjw40RkLDLfPsXjRc2omGLZnI8XhgIIm_tnhCqu3hQvb2UXJDiNzvGxTMxIwe_-eB8-YnXRVEw8-nBOhmXg0t2AwI5dGoY_fkHUdghDNGiMgnNZ4zJdqJqF6TcVgUMBFpgV1ogUsxNL7V0-kd-1NTd9_fPnVwET0I9CRg8hSSU8ZlYOnIj91-lIHWgHA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/959d87b013.mp4?token=gwFUlPdDii5zGjx_acSkiNfEdL7OR52STiz0gSaxPNObPgRRig4eKV5fS7p0ROJf-xtG3SdDm6A2K5No-SLBc1bupgXk5jdhDhJu4BBH2WHCpSWIyoCU0YhLkg5zPEBHqZf_uyL5ayiAYWsPinqyR4i3VeZjw40RkLDLfPsXjRc2omGLZnI8XhgIIm_tnhCqu3hQvb2UXJDiNzvGxTMxIwe_-eB8-YnXRVEw8-nBOhmXg0t2AwI5dGoY_fkHUdghDNGiMgnNZ4zJdqJqF6TcVgUMBFpgV1ogUsxNL7V0-kd-1NTd9_fPnVwET0I9CRg8hSSU8ZlYOnIj91-lIHWgHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هیپ‌هاپولوژیست بالاخره ترک کرده.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83494" target="_blank">📅 17:16 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83493">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j241kGQJeGl4N1Qz-qJbWfwxooxjn-pwayeuPyM8tVxIk592GJfvt5wi5z06MWVBl4lcF5ED75fpO7YJHyrTScWCsNyIE9JJ0Nkc6-YJrqHaTLqKfWOLvClu6GRDZSinXZQy4mrs1lN-kqyf1QKw0nfbxYnWvsmeSV2saVsGVj0puWeXFHA7-ZQ-7U8NaqdMiL3g388ybLyvt_-xd9netvH_2zT8d_WVQ_g1W6VMqrgej-LrRFj8wMpM8-Wk_GWJkK2nBR7I_P0gYUpCgUultWxUOA6LFzdUDxj56AbJTFIBwW-hILg9P66CmpvNN-OCybPK_jQM_SJi6_WCrupFOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83493" target="_blank">📅 15:37 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83492">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فینال سی ال ۲۰۲۹ قراره تو نیوکمپ برگزار بشه و بلاخره بعد چندین سال بارسایی ها قراره جام رو ببینن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83492" target="_blank">📅 14:51 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83491">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">خداروشکر حداقل وسط این همه بدبختی طرفدار دنیای کشتی‌کج نیستم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83491" target="_blank">📅 14:21 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83489">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K1XFIt1IZ_Ro69YHoqoamTsJlZmRxBPZJMau-T9zmlPq65cShJ-7mynr9EzdJoFO8FcL4Vdbb6bE9dD9v4oxiDHlvC0w3RtBEuzix_PerFn2ediPpQZQYLZojx0ikwvb67awCh7Jpe4mfjkGpWxwup0VE6lLEcK0s9G1R4fmvLiErc1tf4b3NGmDZedgFadNpWvJZhAsBZkz_2hUH0q1TkNSqJgY9kffbqFZqufJ6DthHj7iPzuCoBYQtDwPrCfxoBWATSpR1K56dHeHOfYg8lkZ6sdumYt3AXQtzdPZKxU9XtN6c0stW_gU71lZnMhA3ImuUlS7_1VAUEzyKF5mng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یادش بخیر دهه هشتاد حاجی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83489" target="_blank">📅 13:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83488">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">هشدار شلیک موشک تو مکه به صدا درومده، فکر کنم حوثی ها یادشون رفته خودشونم مسلمونن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83488" target="_blank">📅 13:01 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83487">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">قشنگ دارن زمینه سازی میکنن بزنن بعد بندازن گردن هوش مصنوعی
ایلان ماسک درباره هوش مصنوعی: «اگر هوش مصنوعی بتواند کنترل سامانه‌های نظامی را در دست بگیرد و مثلاً یک سلاح هسته‌ای پرتاب کند… این اتفاق بدی خواهد بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83487" target="_blank">📅 12:45 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83486">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SGax10vS7XHvUU9oItJ7jtc6u7BBm_EazFoYsa2V7tLLGJXHzkOLR5UQmPVbSi1oL-9x7csyTxTBdnGgYFd4mZQdudFXWkPsi0E1_PzY9lZplVJtVdqOqMoC-yY-9tnEpiQ595_iNnNq316Pfh1iUdw5svmnE-tyrDKD54mGci7q532gywU9MA1QhLNiPw9VczvPORvhcuE62B8IBg9Augt2Cb0F98HHiIRW_sJPczMiP3WMN0EtmvH5cJ0ACFL6EDl9B6zXImYrMVVGdgVNY11gZwQsnki1HsHNIICv6epoz14FjxFUl0yKmTKEePFmiCdfUgNBf-BLTocEsWWhAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بلو بانک اگه ۱ میلیارد پول داشته باشید تو حسابتون بهتون کارت سفید میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83486" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83485">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/83485" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83484">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKD7kUaq8Vd21FvqtbI0X2-8Wt6ChPk7_2U2r_yCA0vgjsmw1jtydgiIHDTCESbRtevg8H-c8VL6XigpimB-ffADVhs6pmkO3fc8Cz-09ghCpYFc755DoH_SovcMzQgCJXn6mxeriA5J2hhCEqxZhwC6PKmSmpXdHtA3ZD1YkSvxyjuwWX92pnQQtcNcdnWaM83x24MBBnCY3cbAAYiXapSIeBwP7lv8xxhIhovKx8DgLhUf-dNeHIOWjUdx1i_UQu1SHaR1kKatKWShxueiMAZAA-UI6OpxwflsHP-d-3REfdj7bSjLqf7-yE3DDQ9QD4EHYFSBAPe0w69_N35SkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
آژاکس آمستردام - ویلم دوم
⏰
ساعت ۲۱:۳۰
🌎
📲
الچه - رئال مادرید
😀
ساعت ۲۳:۰۰
🌎
📺
بونوس خوش آمدگویی ورزشی
🎁
🎁
بالاترین حد مبلغ شرط
🎁
🏆
واریز جوایز در کمتر از 24 ساعت
⭐️
👩‍💻
پشتیبانی از طریق چت زنده
⌨️
✈️
https://t.me/BerryBetOfficial
R23
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83484" target="_blank">📅 12:27 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83483">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">لیست برندگان امی 2026
بهترین سریال درام
The Pitt
بهترین سریال کمدی
Widow's Bay
بهترین مینی‌سریال یا سریال آنتولوژی
DTF St. Louis
بهترین برنامه تاک‌شو / ترکیبی (Variety Series)
The Late Show With Stephen Colbert
بهترین مسابقه ریلیتی
The Traitors
بهترین فیلم تلویزیونی
Remarkably Bright Creatures
بهترین بازیگر مرد نقش اول در یک سریال درام
Noah Wyle – The Pitt
بهترین بازیگر زن نقش اول در یک سریال درام
Rhea Seehorn – Pluribus
بهترین بازیگر مرد نقش اول در یک سریال کمدی
Matthew Rhys – Widow's Bay
بهترین بازیگر زن نقش اول در یک سریال کمدی
Jean Smart – Hacks
بهترین بازیگر مرد نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Matthew Rhys – The Beast in Me
بهترین بازیگر زن نقش اول در یک مینی‌سریال یا فیلم تلویزیونی
Sally Field – Remarkably Bright Creatures
بهترین بازیگر زن نقش مکمل در یک سریال درام
Allison Janney – The Diplomat
بهترین بازیگر مرد نقش مکمل در یک سریال درام
Tom Pelphrey – Task
بهترین بازیگر زن نقش مکمل در یک سریال کمدی
Kate O'Flynn – Widow's Bay
بهترین بازیگر مرد نقش مکمل در یک سریال کمدی
Stephen Root – Widow's Bay
بهترین بازیگر زن نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
Linda Cardellini – DTF St. Louis
بهترین بازیگر مرد نقش مکمل در یک مینی‌سریال یا فیلم تلویزیونی
David Harbour – DTF St. Louis
بهترین بازیگر مرد مهمان در یک سریال کمدی
Rob Reiner – The Bear
بهترین بازیگر زن مهمان در یک سریال کمدی
Betty Gilpin – Widow's Bay
بهترین بازیگر مرد مهمان در یک سریال درام
Ernest Harden, Jr. – The Pitt
بهترین بازیگر زن مهمان در یک سریال درام
Shailene Woodley – Paradise
بهترین کارگردانی یک سریال درام
Saul Metzstein – Slow Horses
بهترین کارگردانی یک سریال کمدی
Hiro Murai – Widow's Bay
بهترین کارگردانی یک مینی‌سریال یا فیلم تلویزیونی
Steve Conrad – DTF St. Louis
بهترین نویسندگی یک سریال درام
Vince Gilligan – Pluribus
بهترین نویسندگی یک سریال کمدی
Katie Dippold – Widow's Bay
بهترین نویسندگی یک مینی‌سریال یا فیلم تلویزیونی
DTF St. Louis
بهترین نویسندگی یک ویژه برنامه / سریال ترکیبی
The Late Show with Stephen Colbert
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83483" target="_blank">📅 09:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83482">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">روابط عمومی سپاه پاسداران انقلاب اسلامی:
بامداد امروز، یک فروند پهپاد پیشرفته از نوع MQ-1 توسط سامانه پدافند هوایی پیشرفته نیروی هوافضای سپاه، تحت کنترل شبکه یکپارچه پدافند هوایی کشور، شناسایی، رهگیری و در آسمان غرب تنگه هرمز منهدم شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83482" target="_blank">📅 09:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83481">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=E9TPYDEQ_ssv5LF7dyB20zX9o8InBhCfQZTeD_4CE9-hJE-a2k-GqP3PRE7-NeiJycFIMlREYsFUbyvkx0qovGcb4SfBAmf_tu9-qlTXmcuLrp_4tFhvtZKNhhP9mxpjITW2s66GdqrTEl1Ry3vzb5gYK44L7UqdYE5aoUM-mK97o-dy7qAV4E2l9gR-z3M_ruHJbm6-VXnxwK5gVAHA2odd0GtGdgnzKT1DiVNbc0jnOBtIEsbQp4u3xmNH3JTOMskq5cGKAFjDcIjG1w_DDd2KQQx7v8smOjm-FDpQNhJyP8--Xp17GjesBPekt-Zn35g58wYAgAZy5zHjgoDrvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e0468951e.mp4?token=E9TPYDEQ_ssv5LF7dyB20zX9o8InBhCfQZTeD_4CE9-hJE-a2k-GqP3PRE7-NeiJycFIMlREYsFUbyvkx0qovGcb4SfBAmf_tu9-qlTXmcuLrp_4tFhvtZKNhhP9mxpjITW2s66GdqrTEl1Ry3vzb5gYK44L7UqdYE5aoUM-mK97o-dy7qAV4E2l9gR-z3M_ruHJbm6-VXnxwK5gVAHA2odd0GtGdgnzKT1DiVNbc0jnOBtIEsbQp4u3xmNH3JTOMskq5cGKAFjDcIjG1w_DDd2KQQx7v8smOjm-FDpQNhJyP8--Xp17GjesBPekt-Zn35g58wYAgAZy5zHjgoDrvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83481" target="_blank">📅 09:09 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83480">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ساعت ۲ تا ۶ صب فوق‌العاده اس واقعا، ملت میخوابن سرعت اینترنت رو آسموناس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83480" target="_blank">📅 06:10 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83476">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QgAaM-QcbqmryAWosokX-UtSchra7scTbgJP3392sB2l1GqFlAmbc6EchfQDX5G0QzRRvqz8upODVEhCIoq890xaIQjrh0ajVrjDtdV_hiBbi5Vkh1yvSuinyUmigXoTTRmZnlpeK-Zwbo-PvqL35UsVRzXWQim3_HUOGHdYFLMcjAvfkK-U1hU7020pHjqA7o7zN-gJVAoF8-UG-PHsYIp85fqflAdv9v2zbxURugugJqOkhMUdl0fUTWuJ5oPvUD8X3oujKn7r2lTwnrLbbytrCTEaeXFr3RwKKYN9wzxiTIPDbLcBupaqWR-7aKmiadysD1tMA87RyL0-oxQ-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iQ56iqhv0YmTUMC8IA5j5BXFGgu97b70Lbx-xaEI4ajA3VKg6VDWM4JAgTgX3i85zTgDGq5lCp1OzwznZck5qIdLirWyWK3R1AXp6yyZk4VcssBOo9j6PuOFXNOeXED5sZhCNo4C8-JqrzAnTgL9iul36Z-GRV5qiKeJnoY596t_q-41SJc_zD4EExdDq8ZPcLbLi_uamMbKibAUWx-GiFBe73TiasIMbWSqVtnZfCbAgZbG1LUooTBPjd6k0INhR4sdbuH26imKFrPu8Xt0Iibl0_UGL5Lv7mK6sCpQ25WHcJN5_te_G6uYbJZUKjfwsze00_YVqmsPkLlym2EG-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AR4s2QAdwBHBT0Ntpko8SJ1clXXWwpm5VTNUmgcfdNjY8YIck_Rh7yWSKiaK6vd-d2xonLP6XCwasNuRN39eSkNxSbYl0ZgyGUjYywDfE6i3PEMs0Y4Tbyqb7fJqNNvxQk8rdq6rEp0LqoYz8KUSsdfwEtw2BAxymGGaQrIPqJq5GKdw0Jqji_JD1VIfRAX9o5W_xwzH-K_5FlxiQa2eFulwgttJqPY_YuqWzOVUZy3SnHxYvYkTbOWubn87IOYeUvTqPYPQhZQYQ5JhiPbfFCnFzDC-XjkLN6brF9-TrUKjTvRNpcHeWFrvXL3sWfeRJ5FWj5G7U3r2J2UN24uONw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تام هالند از زندایا خوشگل تره</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83476" target="_blank">📅 04:42 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83475">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TfgAHE3rlCxN9DyHzfZWu99wZPePA10Jzo-jaKmXGq7JJU_XcJvx05QDftXzwOAFp6F3bJwqMN62ZmjgKo7vVvVpyIcc39RfaaLlb5SE8rgHKAyCv2675WOzLXw85ByuOHfyWeopj0uFPgLzobAtPk9du6j39Cjy9D8-hyctkxwX5liTOYnNWRcSPruLLTswc61ONYLarxBzy5Tws6J3uDD8GxzEOgJDAMCVDhumxurOZP963kOBcS4cjfKQu5wt0gukvms2ycpqyIPlmX0ix_u4kg07pyEoo66F5o9tX3dsjJMeMmC6QwPrj0c-80HkpZ313IDAn-jImPGEHhG1-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوآ وای‌لی برای سریال "The Pitt" برنده جایزه بهترین بازیگر نقش اول مرد در یک سریال درام در مراسم امی 2026 شد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83475" target="_blank">📅 04:28 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83473">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cNJ4SHWKrKlfvjQokahaSfY2szxILud4llpgUlhTq334y3IY1c9pTPb1oqdV-7N7iqJ_eq0w06-EKfWMMn1gDu3fH1V0IJ6sqBvSGz9IYa7aJFu37Y61eg2s0zcSbZXXNfu-FKWlvvnTE1IIwMx_UGC2uocjWcfsOh_alpVDb3ArEN9PeR9suhIrPtSHLEwRYGlOFQame_8KMtG1bBanjCEFdNHB0IuohKbGzhuMwTEo_pEamJFDytZWvMF-fIuzTlA5IOl_GrgJMVirGMJI2npdTyP0ur0u5rWF8ZB3n5UOnjEluV9XK6Tp_NEQgw38MLzCg14UIElqmvkdM6siVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DjJc3ss-9Tx1fUpErkSW42UyMOVDYxSCW9Af7ohpecQmdoAQzo7Y3rOtGwxgrLfILORBNFkHTMYJ61cOIbFj8fv7nuCPj48WriZqmKVB4qr48L45lKLI2lC_Bwo0G3UEOv9kz6vGMTSgL2h1naq3hf9RSG0Qky7A0Je-MdcRitC6ykQKYLpQUMT0hkRPLDMajy1Qtxbf7HdxSvq2iK7Ktjqy7BLfRFTMYo0Smhn5k1ZT9-oTVwS0cNCJInjCA-frc_KzTyR7O7lEebyily8AT4fqG0xv5IKAVhtNlcDKtmmByy37C8GraVyMphbmeAGtv80Uc_4ce8P5uXIuTIRM2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سارا پیجون</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83473" target="_blank">📅 04:22 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83470">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ov8MuPAHlu5AMZHH2-q9sZwURGFU__nlocSSeI59bo19ZrxANa6wZIIqAit46nC-u8l5ucLmAPXVaGbszUCtE-phU0F2ReytMvxAA2_vmGSJZqOUJ-XQPVKVTzNR1Mot8nGW7JLAE4GV6BzitFu1nGk3VXBhvWxTHZM8a7DMWVEmhSSO3_B4KcBbZ2t06t5M9nym9V8V7AIKIKrgXT-h6cFeO1QY1P46ZbYwodQTIZQPgxf59zPsWXRL7PGNGNAd0qwGf4PIKdHDrfPgJqXbpXCe4fudN6amwwYScnDKgW3QTjRfhTOTikhPA51MOt3tpHUK2J6IzEknqUBJdb4jcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OB2CV-iZICBrTylZWDmxP0cIe1o_iARnjuYw8OGcb4nK0cjnpgMZCTR7dELSERut7MvmADh7JkiqaArK4Bdi_n4Vzu4ogGZMQ5iim65sG7x0pXoGvhNcoqhg0EY0FWTMdDLPOBYJh3fc6qN38vw5UmD6cuMaVZd94adoPmAqoSk9Wqy9ok9yRp6dBKtmTW0L619eY5NeVHQ7uOOQgQQ_By_Qdno_Da11BJIDBjt8ySE5u3lE-O3llp392Bt_HNSMWmZSnAi8WwAiwuhh2Glw5cC29IzVsolPuNSUeAS9fL151lNCci19o3k5ZB-j1hl9n1V0Ox4tenrqQ2WhDk0-eQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تا اینجا کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)  جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)  متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)  آلیسون…</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83470" target="_blank">📅 04:06 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83468">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vT9-xtqn2yoptyHopvaklqkLtUhMfk4RzUX26zzeHEhjLkC4ae197GocX1KOpXC3FZGPwBw0MNHAyrsyQ3646HLKywktN3sqUIbd3Uhp8dIm2jGiHm838STFFON4pkBheBXaB5TDSfd3EBGxnF4GVWijUrsM1JMiI27ZRtrivjf9NN0u3YKsc2Kc0qFuFUEJB7ZGYML2RvVG_NzSfCCgH7yb7Pz0Z7r6S3ev5z6AE-85K8lsoxKQTSMnf6IFzMtSDK5m6acs6NLPRBItanUXS21OfYFAfAPye621sh9XppVp6vIvoRyrdMr2gPUiU39HpTvrC7ODlGzuu4LuJaZFDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Kq1KAQmVpSGZUy5PpEUlgD4tR9eps4ui6XJKsOoFrlwCgqA3qYIgD8VAdZ0RqhgRYgVA9jib6chnqf-MfS1DaANpVF6ILvsc08T_Ieacq8YbNqV2v1ez_0dU6kZ8s98nm6bLFu2rr9BjPJt6ed0MgxHdABauR5zaXiGVuBCwmGPLcwASpNnwVd5r6DoY5h2K9cf55jnvCnefvHcy9FBFqIRaIAJmgtPJb-h35C7d3WoqX9HHqFvKNaoVdtFQ3Nh0wTf3rnJ1DNf9Zg5LyqSUuWp0g1kclzb0DeSZQo5_LuvICWQvV00MarnSTbKWJTCXFOVaE890ImRGC2tsbj57NA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ما درخواست پستون داریم</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/83468" target="_blank">📅 04:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83467">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">تا اینجا
کیت افلین برنده جایزه بهترین بازیگر نقش مکمل زن در یک سریال کمدی (Widow’s Bay)
جین اسمارت بهترین بازیگر نقش اول زن در یک سریال کمدی(Hacks)
متیو ریس بهترین بازیگر نقش اول مرد در یک مینی‌سریال، سریال آنتولوژی یا فیلم تلویزیونی(The Beast in me)
آلیسون جنی بهترین بازیگر نقش مکمل زن در یک سریال درام (The Diplomat)</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/83467" target="_blank">📅 04:02 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83465">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JSJBf6E_KjO_37xQENH7MSMizIWmNX-0jw96GkVpQFgS6et0mZzdwkwJKsvU_F5q-bZqq1-ZVGcBbCiRRyJk1QQpr9LgYwLT6N-ETb6YflNF3OqWa5yjUIgcTIYGX6B_BLE_LarbgJVmQfGENS3HkY8AeGNrcczFRGQCTNlV3Mj3ztZnAvzckor6G5mQl7iNlBBAIK5FYRM4VsBLiRuT6taKKFNRTS3HmLxw-zHGz2LqgGXvPGngDoAG_oPoZ8Xg7EZ5uabvJlw63v4S3EmGhUVCVUPV9eiuqsNFdS1bkJOqG3sIDu1DThUfLfxx4gDd5i48_v-5-UvpNejl9QzESQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HHUY4s0DWV9vU7nGplxsTE-GtgIRl9p8AL-V-LIf3jEjeH4oMTCDhX9LA7ox4jj2yDqtCWuj6X_swzI0vrXrHYdhvv03KycvDXD8JT6RtPXinuHTRdKmh3NR3SoQFE87fdNW_aUhHcgZmqdivu9yAJaRkcjw5Vgd2vyD-oLlr0tGTZSuKhK-FwfwHIBQ0erugidYeXx-N1Q9Q_QjLA5EGsTjgxyVmG0t7EwwR8a5kOmFiZSv1VUgC3pyFGpdfGB06jyiVw4mCHq12lO6ukJ-K0MUCPbUHmu27oUh-qjR2mSRcNmpx_ehgvlsRK4lFLB4OM1vlDwRUAjQHzpBxfsf1g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">اما دارسی هم با استایل تام بوی های دبیرستانی ایران حضور داره</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83465" target="_blank">📅 03:58 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83460">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FKzWm7r8zguMax6-KygqC9n9oE576uYJKKNtjlcn7hR0aksg9GPbGpP7FXKAj2mOyMmDU29u7Xn8WDbohICrjK0rymOi5R8x8xzkv7VMKG_f6MiMjR44xmsuSzGJ9fOTiT7RjK_vtPiBRCRNgVtwvVLp0oXT4yhtH-tZvG3YHk4KIXSPN55bkod23zn7yJHRbkXlI2deu27g4sdEFnc2myoUNO7vjgYrOXUcLWg4WopqTGfnKLrNFivWiDd2LOlbDWkmhi-iQZWtjc2ubvc3KjxPQWh__7ESIonAgll68Qq5cDaBZUcxUvTivMA_084NRyOEWOjDcXbuz6ymLHU0Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAjWF0BNe9WRkIbEkbFvziIb2KY44OA1gAFnqTXvil0p8hobdMoHAIeFCr-334lcW1w8OtXAntJCj4ORN3k99FGKIrcAVEwP4GyKDWCDhcbR8bHsyVpbY-sPfCu-tQsgXCuGUPLKLXkBkXQSJGyV6dT5DW3_Bufnd9SCt9DkBTYogwKoMzvVGzCpb5_4z1mZOBUFt3bMDit9LMwZLbVhnexk2WuoIQA2JTGNQXtFFOeh6-ngDjDqwNhX6BNR4Yj_ChTcjgYhL2cLNOgpS5opedwLDFfkakaLt6s_IWsMaBx6f5DRzqHQKMspqY2pIMLZkfBXMVI2HQP38v-a8MRgYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AQlTzZTyvPERjRbH9MJ6tXawBeml2epfU_tJ9y6f2NfdGMt4WQjkr7OFIigK43NKmKinAgTg8JIg-WzBLU6A5xxsoF-wpkRsjUCwnF7J2aSzVeWXJFuqAsfGGUvNn-SRvP-wzvfDCfDpQmns9f3nKvhTEvRI6ZiBil_Xbsyynfqxhx19kfGoD4IljAHX-gEiqx8dqq7O0KhYD28g7OCIVOjvIl1p1H0wIdt1BbXlB4Xy7N7sIvUmeJPQztDdY5OPiWwagNqBZMsOo5xP4mIs9-ir7vAx9KNFgsDNu-0WI8RHrTMYL8l-vlhAu_kDzTOiTcxCKLjojg716ADwgLm1LQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">سپیده خانوم معافی هم هستن</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83460" target="_blank">📅 03:47 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83459">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f5zJsKY-2JlfrAcyUNuilRF5FVoP2qTv4GlCGKz5bj-rZ_eHw5yTga2rRfgD3WUDtoJrfHi5g1eGOUX71VtJO_Kyv5ItC_OvW9pWvD3XnnQxCD3dRexP4h_e4JsZA6PtNaB7XHxsGfoox1b25nDoqPI9mXI9RhgnzqyS99U5Fs08Iim4x3mNmcq7nDD1BaC16KX2Dn_v-ppMP24EtzMP4ny_3Q9Dv929l-baXgXf-lk_O5ASyuqAHjrksZ3Jj7MrpiL9v5IiPDzZDKKkMODDV3E17QnphqwJhCe4xF_6r933e8D6a-FxsHNTq-0maUolHi9WHJ6vempsRc0Y3QGfRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جولیا گارنر هم برا خاص پسندا</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/83459" target="_blank">📅 03:44 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83458">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyVe_2piLHYmoXmvMb1jzAHom9uFg2IBltpdFdlTxvtCNU-sC57B8e4DDqXr7w8NDvFmQFXwEzoZghv0i4IEHrZxbmMVp5Wy5pk7KHtEtKJgmFI6xc1sIyoHPsDYaFN49k0jTltiPZ--mKzAriEKud6kk-IvXL0oJyGQZ1uNnKtEGdWGCm72xLKe7FQMGzlh4wXynWHwrepq8fn_Y89v2TCjlY5gCHmz7PFWL2Hb3Zbq68md_7AVVx5_f8lhjvDzHlbt3YxV-8ufxlE7V9Rcpq91Hh5d7TDYfcG01sqdoQBzyjxjoZVKYixs8wU90JYAC884wfMCBoEwQLZkYxWZnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلورتس پیو رو پیدا کنی و نزاری ناراحت میشم</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83458" target="_blank">📅 03:41 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83457">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sD9th79dCc6vC18vONR9kCC9zyklcb4-vYFQnni-pu4wOr6r2IfdNRL05SkAauEmMKWAWXLaOBHSmEiHg8Q-YfpiExqlmMK1ZHp7TUShckkvNSL2qZoKRmprg0WWi-YC6-qyGgYRrfiiSNfFJz3vSfvGajDFa2qKMhkSUOcEM6aETJEnE8aO8HXL-EtPsyTqH3CZ5Axf6rzirepTC6L2b3MDNKOB3Om4R4HFi4Ga37wNVn86wpp9ELVaEpQCK564WGjrE3ygSRaZvRUtmT9RxxWwWpyBiB12ncPopgGNV_ut5pXKSqo0HqePRhrsaHGzEO44Cd7FYByGz7VM1gzEoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عمو بهرنگ خبرنگار اعزامی فان هیپ هاپ تو مراسم امی حضور داره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83457" target="_blank">📅 03:39 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83456">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H_KrIHzi1qc-O4mmb1FiTqSPegy5ViKHciOIGu6K1TV0h74pih0kF0p9HTLx2ipC4sY1xRcdXkIBHU3ns51UvkZ_VlriVNyP4Q3UOiF2I_g6VrOhNLeLBAZ9xuKmtfZbNutscZX0lxqalsVHXTvvaGb3OL1bHU-39n9e-j3X4Dad1795SvsotLj2E9ArFg2T4r6C4BKvukCLqOuRfxT16SwMgVzLwYt5G10kmfOlwEfNg-mlwp4d9onAheM3H_9pkrRI65_QGEwcKx8LQpGi6yj8GQtECNgpVNXtmbBSxHtMEIThG4kvuCAOiMbvd_JjRjT6XmSWMuJyGu9cn__Esw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندایا رو خودم نیستم ولی شما ببینید</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/83456" target="_blank">📅 03:38 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83455">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PALpa6K6SbM5-vIx89oFbpvwJkoWVYkxzOHWnN4WYfpqVN2oyRPkfdQ-j3zV8gKoY6o5Lrd88tlCAqxC710qVg0oaIkRPY3OG1BXYfXdlz4fMjznQw7AZrpWu11yqDY9C9Mv5jSzGCDU8t8Ldzau5TAua0nxuYemX4Qd6KCiXPHatxcMH6wEdZkGNYT-1b7ue8O5warbzaQJ8Snp4vJ8FJ2b4nZ0XakfUbtOVW6BeVgccQPGZTmaHhUnqGr-agN_wyzzjFwEfJEOHDbv6g5bOTQfappjpD9Dad7I40VvfrF1nemRHiNcTa4B067JWUh56VVEKNsZd7tkGS6A3rwXNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عکسای ال فنینگو بزار زود</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/83455" target="_blank">📅 03:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83454">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">ببخشید مردا رو تو چنلای دیگه دنبال کنید از مردا بدم میاد</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/83454" target="_blank">📅 03:33 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83453">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DxO_dta7zFS3qwe54qj0bPLReDtPyKT-iWs_FWDoORYzSL16QuG4zy16Bmsm-rRvNDdMmlY2bIbS_3pYI0IdxOflFUEhlPYEZUShoIGXJuYEV0WweRzBr1xFLhhhX-MDH4CS2pnl4s3c1u0d3bU8jqs15j_sdCAagIr4VmQegVDKbfKYQNQE1sgeXGRHpFbykP2WfTLSonGNBM7gQdqcZ8VCivZgXZJ_XZByky97lkUOoHEWhp_0m6vN1q6S9HfdEi6nqsP2p_kUUhO7r7Z4gmYMf8I_Lzp1TN-5uR0kgAzeGDzCZGblzGowmp6JuS_0CRng5nkUcCWUTxJS3mVpIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سگتم بانو</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83453" target="_blank">📅 03:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83452">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83452" target="_blank">📅 03:30 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83451">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hvkwc69gnHbnLR5CixRZvRUa8kzc32wcN5ZHjDY-H6afGzZtDBCcy4xtEj3ltR6tqnQdHBoNWZHY_N0JeY_nd3cqPFUiGXKcLK7tQSqgIaHtloksvniRxWe4Drf0_zBFGIhu4A0FkUvxriFbpU5k4s8VfTkVMzh7uoFqiWB7otsweSXRQt1mANGkgAaO_c72bpAxH7eNIeqjUs3L84eQG3O4x4uA5eZIrJGbq8THA1pcdLwB5MxMa2K1EJP3opFkf6p0Qsiq_tMrQRyjE806Qdho7lrSaRpDwy_TEHuMuqnXxtfKJsa36WNtB5X8fwgKqLU5yYX-h-Y4A17cC4gM6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دنریس تارگریان هم خیلی باهامون احساس راحتی کرده لباس خواب پوشیده اومده</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/83451" target="_blank">📅 03:29 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83449">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmf5t4yTPD4fX0kPwkZB4cme1nvTqelkl6K2xkiskKOG7d0rGeAnhCI4F8gCTQShrmaiV1PChRSkVY-YUfcSDNOtQH5lj0Ni1kPD14xCzODbpNoRO0kw96daOVcsBdPem4oC414-PR8DC523UimwBfgjIWOSe5dugOxM_t2SmxWOqToVu91DMPfyAg7GTa9ZavCOauNOM6yBQbqo0yiit-rVVCeJSHguqQfimLBRiZH1Gt3U2_DnuHCwB9s4yoAH35jfGbF5jeDO8x7_yExLoEIgLbR39-M0Ai8AvoWEl1N6pSDflgLwul3J3y8b0QIPDc75fU31SiR1DVksmkrHbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GC-v-ujHNhNmf5p4XB_QgsmHX5qQpe_1MtB6-SVPwpWydOAmKCowZMLovnevKFtN6dSgg8QPgWoZv2GprTBBk8yhqfuojLc2heoYmUQYDVQgc75ewfXSEIwd4xVAmcDdGH8OM9ytBx3IPEZnUWBje8EGxI7hd47kYZpK9gG9-hmvBdKalMIKAA2dbJTS9Ne-90T-pgRqwF3Y0pZ6RqQKgIe5O3OlQAERfcgyei9yxEFxdWQe_uRCWr3verH3FzvIHT7T05Ab-ZpMIQF0vb6nqqjqysDRrrMF3SxEZ5TbnLdNL6HEVlaUDo47li2Iv2ZH0v1HttLhQO32E_ckaAO4tg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بانو کیدمن و داداشم چارلی هونامم هستن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/83449" target="_blank">📅 03:26 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83448">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JyyHScEoMayPg_alAROfiWVEiQ6gal4dpC4hO0hYRFNKzsGcxWkrmFkeRayBPgf_Xaxrun-KJttVPHzTiqCabBpdbE5KNc6q8v58JA8ed4ToT-l3FaO1qJktv-EM4eic2s-j3hzJJxjACUaclqwa33nSW1qV9Hg72sOKXA2fOxlHKg3_fTEvF587BFEfhcmrv8tVMYfsNyqqjYYNNXjU3UrQzLmMhv46veY7zqH1Be7iKSqGbeYLUjoAuhwbdpDwsHcyzx7YQCMgbwX8Dwi3IN7ctMkgcp7mYsVHhH043ffQFyUeTIf2vCXoiU_NzLJIOpRhdi_fVCEHiBwK-5GqzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/83448" target="_blank">📅 03:24 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83447">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">مراسم امی اهمیتی براتون داره کصشراشو پوشش بدم؟</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/83447" target="_blank">📅 03:23 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83446">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OcA3XInvl4OeEJ9YTC_r40YgbUpU9Ts_vN-NPs1tjdhfrcfD6sUrficiWCYqQZFo8EAJ63bOk8L3sXJAO4i_wzSC2xjoC4bnO8WKgNguk0cyQE4VorN0tw2EHhIP_XJZo3sG4peb1wwtSz4V_6A1MWp0Kz_Ob0MxsgferS5Bb_yH0qgryDhcrCrWTXYa5fx4bu1R2lsW5H3pGEaM7wwfqbuAVOCQXp-OI4LzxiAMR95XYzG2_FUKRaSCoJlrdCUza4vRtIhth_OVMEFFQrrRZVn97nNlReV9WYvuuz-1NEJBkaX0hN1f9mHoBN3LRELxXoQWr6RYUYfAonc3IlQbZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی زشت شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83446" target="_blank">📅 02:34 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83445">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=n9z7e-HBHqJngt8icQ05l9gW4In1prBALH_09o36PWDXsBdxuAGLV1jwPOUx94MpdyXwKJ6_5YwR7P1DywlBbUkg99uwYL4GvousErVBnLmiJTnivo0wev0UOQVQhJl51K1LO52QZj1e92BxdlEUeNR1uOC1KXIT4IzchTloifxINCChtBKzXuP71AzFtZxVvJ6anvuOsbonuPuRFYcSYaGCwqBK_onjX-5zNCfweTZ_XCbuNMOzCcJlYZoy9pYmc-DNHpETGk8GBKsmFVyuUlywP0DtlZlwIeNAU261IsKPuo6MH00-AwdfgGfDIa5jfDXnhVDevqIBYc4fRevG0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/adc8cbb03e.mp4?token=n9z7e-HBHqJngt8icQ05l9gW4In1prBALH_09o36PWDXsBdxuAGLV1jwPOUx94MpdyXwKJ6_5YwR7P1DywlBbUkg99uwYL4GvousErVBnLmiJTnivo0wev0UOQVQhJl51K1LO52QZj1e92BxdlEUeNR1uOC1KXIT4IzchTloifxINCChtBKzXuP71AzFtZxVvJ6anvuOsbonuPuRFYcSYaGCwqBK_onjX-5zNCfweTZ_XCbuNMOzCcJlYZoy9pYmc-DNHpETGk8GBKsmFVyuUlywP0DtlZlwIeNAU261IsKPuo6MH00-AwdfgGfDIa5jfDXnhVDevqIBYc4fRevG0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داداش یعنی جدی تو یه رفیق نداری ببره درمانت کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83445" target="_blank">📅 02:14 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83444">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">این چه مسخره بازی ایه ۷ نفر شانس توپ طلا دارن، قدیما قبل مراسم همه میدونستن میرسه به مسی فکرمون راحت بود.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83444" target="_blank">📅 02:04 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83443">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=KWfkGVTFBCkJSfl7pq3aIUM7p767_Upz2grWhy8phpW4ENU-WVytg5DSY2UG2WNL8jfg9xZBy4v_75-MbyHwIdA2oziyKDO10OmnafkyaWMKpFcW-ipFE1584xfsi-cUHpLG4-3yOvyIok5jBtO2fTvXJ-pa59OWsiRZME_Npxe2dLt0UyAsd2M1BcCHtD6fM--n9GX1DUOplGk41-B0H3-2gDt3m8JGxbmeBAA13vaVxLHTfZRzc3S_ERF4tOb1kaIMBLjA1-hm-P_B5ar1xbvmdq-5ojoxPx0lGd0QPgKPcQNt-zwsK7bBxjyYZZDbevP-8G7ge1Xa2t0fq1s_zQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/634b7d2dc9.mp4?token=KWfkGVTFBCkJSfl7pq3aIUM7p767_Upz2grWhy8phpW4ENU-WVytg5DSY2UG2WNL8jfg9xZBy4v_75-MbyHwIdA2oziyKDO10OmnafkyaWMKpFcW-ipFE1584xfsi-cUHpLG4-3yOvyIok5jBtO2fTvXJ-pa59OWsiRZME_Npxe2dLt0UyAsd2M1BcCHtD6fM--n9GX1DUOplGk41-B0H3-2gDt3m8JGxbmeBAA13vaVxLHTfZRzc3S_ERF4tOb1kaIMBLjA1-hm-P_B5ar1xbvmdq-5ojoxPx0lGd0QPgKPcQNt-zwsK7bBxjyYZZDbevP-8G7ge1Xa2t0fq1s_zQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83443" target="_blank">📅 01:48 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83442">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZvTO_RTm8yvtlx1awjw0B2HthJ1JHNkctYvII_jChmKxN5jAYn9mvipGG-UL1vmH-nLTzr3r-gkhdzLofbTtnFBvd1cuwYhIaNKm68ATmrMRElF2ap1DJyHHfsm1Wfgf51qMSDTVOEUuMNXm45BN161y58XtdCU7zCUHWk3QTqL3TjhdM4adkZMzWLCbQGJpDWm2LEiqhxSmgJd7GLZx0KWGa7e1IPL3talVU6aa7EnkOcSnvN_ycnKvReTP8JkA_LjrLP3TuRigAUJU7Hb6d8-G-nSE0MYIUyrjQ_-sxoJbxG9r9QdwhWiVA3za7WWs1FGM8LTmwCQvntKXtAHXtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد میگن ایرانی فراموش کاره
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/83442" target="_blank">📅 01:32 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83441">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">واقعا بامزه ان پوتک و آرتا
پوتک یچی میندازه دو دقیقه بعد پاک می‌کنه، آرتا راجب همون ۲۰ تا ویس میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/83441" target="_blank">📅 00:35 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83440">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixO_F2yYgZX44IRwcYpl0E-WPaBoKLo8jbzXu_K3EVrwgXrjz2ClScFg2Se-JG-smVVazcl_Kh24EtTNdNT9Kfj0jBUADOYPexSvtL0RUKflF1JB3t_WguslDE2razhSKbvTuaVm5g4lNW3fBfBfpOKSBb5_qyJJaz2cNr1mTkp0wkgNh_neiSuYwoyBIsczC6IBplEFq6txqFwAO4tuPSK-5JUTmQNQDFLwX_JvAr3v5ZUtsnVBT_58xaBqRuDNvtFoZo-c6BOlEHRK7Vj9LDJA88h8wYCGQxpPsxfRVa4l4BQeise_KMXOlUaaYRFaqhSL1Pcn1r1n24XiCuv0TQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پوتک بعد از کلی ویس و فحش کشی با آرتا اینو پست کرد
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83440" target="_blank">📅 00:31 · 24 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83439">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hOi7v8dVyKmk5iFN51uQuBsaFITiuxnU2ENc3JkES6Qfuns_PH30xfcz695VhyUMBCgFf6Cc_92b5Xbrd-AlXaTIOS3VmRk346so8tJmFtqETPThELrVBUl6_BnZ5TMSactqVgg5b5hDG0skdil1dZHzULoaS0rpo2eCUtPdG6xCeWlNB75RTec1mWFyntn2GqkWCVQWWHP7ybPQDGnBDpAtNc51t5pXQSbqXVieRYkrNGEiP67fBfwhjFjz60VFHmSPvQnjQGAflaXk23ga-3U5DvxRfKhT3IPz4JyUROhYS9aGirj7__KY9MrvRPuOzY8mUEdTt_QZFdh7BGds_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تیم سهرابورینیو با 137تا پاس صحیح 3 تا گل به السد زد و برنده شد
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83439" target="_blank">📅 23:43 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83438">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">حقیقتا هرچی پول بگا دادم فدا سر استقلال با این بازی
مساوی میشد فشار میخوردم</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83438" target="_blank">📅 23:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83437">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">برید بگید ال نمیدونم هرچی که دوس دارید بیاد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83437" target="_blank">📅 23:38 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83436">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/McjQ1nThASdiHURft26KJ8-tG2rXuy76KnaHROQVIG-Xi07h2_CoSr4SI2z5zn_WRQKQhg8VUKnW7FFSAJiHHTargh-Kc9jabhDgOCkRdR_pjFV2XSh3TXlKdvUql-TUmnVAhS-liOyPmMdJ_4GAv5iKNNLz2NEaOtMMz1QlqundVJQo_AeGr2geUrMk03wEBp6-xVJQ6QQ7HzYv9x3P2WtR1SA_-s12G9ZPPlFyWXdQ0Zmrdu1g8t_j_Te_GDERq57MM4HkBqqMcwysMAxpG0fXqDgTj5c7NyaFfKMCEPR591V07cRTQs9Y3vtm16qT1U0tcnz2AG4JNoDaKvxlYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداد عادل، برادر همسر مجتبی خامنه‌ای:
آقای مجتبی خامنه‌ای عاشق سریال فرار از زندان و فیلم‌های کریستوفر نولان هستند و به من گفتن چجوری تو کریستوفر نولان و موسیقی شاهکار فیلماش رو نمی‌شناسی؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83436" target="_blank">📅 23:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83435">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">ویس‌های آرتا در جواب به
پوریا پوتک
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83435" target="_blank">📅 23:10 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83434">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رد شد گل السد</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83434" target="_blank">📅 23:02 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83431">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">چه سعادتی بالاتر از گل خوردن از فرمینو</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83431" target="_blank">📅 23:01 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83430">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">یچیزی بگم نخندید، السد از جام های داخلی انصراف داد که تمرکزشو بزاره رو آسیا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83430" target="_blank">📅 22:54 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83429">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">استقلالو</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83429" target="_blank">📅 22:52 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83428">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">از بازی استقلال کاملا معلومه بهشون اطلاع دادن من رو السد زدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/83428" target="_blank">📅 22:28 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83427">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">سحر خیزان
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83427" target="_blank">📅 22:26 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83423">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">استقلال یکی زد</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83423" target="_blank">📅 21:56 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83422">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">این یعنی تعویق
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83422" target="_blank">📅 21:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83420">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">اوه اوه دختر بچه ها دارن فایت میکنن
ویس پوتک خطاب به آرتا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83420" target="_blank">📅 21:13 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83419">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N85PasrumB6cYoYcj1Km8uFTXbpk4Ty-Dfb6US0MjUAQyCXDJR_0Pj0CbwMFFAx4N8iRYDGB2MnnUNL6VLgL8vLy_MyFOZiAcQgs8H3Bz0vypC7M6A63cSZ37ueW7rClOCxQnkr1izrAYmQ_StcmV0wZonWilZMJNdCD-VLWOXLeD9oJVPPf7xXSjsQRu9oiUnSofQCPbGJc7ELwpAWYdU-AaXeMzhF9YAbg_xp77Rbx0xS08KnKV5UChCK72mhaTUqkvhmrLS1qh353hDElrTfHtROClXwB2EVC0DRABo1Fd-www78JS_QR68VTw1Ci7GhQTykVV4h5E_z1kYPfCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بچه‌ها این پیامک چیه برا من اومده؟
ممکنه منظورش این باشه که یعنی تعویق؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83419" target="_blank">📅 20:59 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83418">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=Zmsm1Xy74PPFvxFQrqKfD-39HfL3J44C60ACHgN7k7Jb3ah6OpnnkuJFIVgMuA8fB6TByI-z-XXJvKNNp3WOYT3Z8RhfdToYpdgJMzWP05-coKbTWYgTjUXunx9xZZGTIBoybNcTBiHwTl_4qtEJWoFHp78td_0KExI-toDzzPtxE92J7-eF6QENJZep-noT5qFy95dVPzC7AdLdr2nzTlxdP5HeUEQMiFZ70odGZ6efXyqEbALvqoiyylm8SWGZ5DTERFSGD3tukIaA34j8DvXyt2m6ZSw0PLseW2Uq_LC8xUULQsPPW24JZcJ3W7hg6WJ1XJyOJ3gdNWgVAVLEuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1140a336ae.mp4?token=Zmsm1Xy74PPFvxFQrqKfD-39HfL3J44C60ACHgN7k7Jb3ah6OpnnkuJFIVgMuA8fB6TByI-z-XXJvKNNp3WOYT3Z8RhfdToYpdgJMzWP05-coKbTWYgTjUXunx9xZZGTIBoybNcTBiHwTl_4qtEJWoFHp78td_0KExI-toDzzPtxE92J7-eF6QENJZep-noT5qFy95dVPzC7AdLdr2nzTlxdP5HeUEQMiFZ70odGZ6efXyqEbALvqoiyylm8SWGZ5DTERFSGD3tukIaA34j8DvXyt2m6ZSw0PLseW2Uq_LC8xUULQsPPW24JZcJ3W7hg6WJ1XJyOJ3gdNWgVAVLEuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به هیچ عنوان قصد جسارت ندارم اما حقیقتا بنده احساس می‌کنم این رفتار و محتوا در شأن همسر آینده بنده نیست؛
امیدوارم محتواهای بهتری رو برای ساخت تیک‌تاک‌های آیندتون انتخاب کنید لنا خانوم، وَ مِنٔ اَللّهِ تُوفیقْ
🙏
🌹
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/83418" target="_blank">📅 20:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83417">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">آخرین باری که پرسپولیس رفت آسیا دلار 70 تومن بود</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83417" target="_blank">📅 19:53 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83416">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">زندگیتونو بزنید رو برد پرسپولیس و اور ۷.۵ گل بازی</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83416" target="_blank">📅 19:42 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83415">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سردار آزمون دقیقه ۷ به تراکتور گل زد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83415" target="_blank">📅 19:41 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83414">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سردار آزمون دقیقه ۷ به تراکتور گل زد</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83414" target="_blank">📅 19:40 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83413">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SHT3nnZMLB7GZfgnNuiT8uB-tkZEXlXgp656YPLN5WvPu-5W6WWEZcX9n78LNz18csqt2SEcUFv25LL-iK0HGzT2gyGLPixWeoe6utT2bl9QtC9NhT1vmOhv4owST-hplgYWQAdk_RKg77ewMomQUAUVUdbrxLKirzp47NfJ7OrAcUVY3F8Wk63r0baDjsXOtIxd0B1gCPxEBFNFQCGoOdzHE8tRyx1seQcfbPfJkHXZCsHlyqsBX_DF3vBnbzOR6z4MZQ9_30H7-BpC3vhVP5KJK3a8AJ1WOVuuAoqZeno7xb_iiOqtJLWf1JHAs9JaNZyLwnNvz4vbULZZV7qFMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کایلی خانوم ریخته بیرون براتون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83413" target="_blank">📅 19:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83412">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=mVQ4YXiYTkuw9bQxFqqnS7aMCaFlOIHZsgoq4pE25LWx_DTUstNDMsVT5czrrH5xILhRWZIyb3OPDTleceCDxWNADpHred4WJ64fWEYhxXuUc7J_it9DW5ZIAHtCbLOTFa-65yDDgmODeY8KeALWMVJPlLy1_wlUWRLNqP0UMZuxjb7_GPFOlbk5KxiO6aJql-h8Hby7OJlj5IxUQ_tAP1OGBCC-B8_kp9oUALRzLnQ__fug28HKRajxOqW3nx8rlT1h7ySH7AO4HyApPSp-lDu62T4hRot8WwqICH4ks7ygvlfXqL5g-bzwcAO7Jjh6V_KabqVNJSdvuBkPVmqEkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23eb3a1ec4.mp4?token=mVQ4YXiYTkuw9bQxFqqnS7aMCaFlOIHZsgoq4pE25LWx_DTUstNDMsVT5czrrH5xILhRWZIyb3OPDTleceCDxWNADpHred4WJ64fWEYhxXuUc7J_it9DW5ZIAHtCbLOTFa-65yDDgmODeY8KeALWMVJPlLy1_wlUWRLNqP0UMZuxjb7_GPFOlbk5KxiO6aJql-h8Hby7OJlj5IxUQ_tAP1OGBCC-B8_kp9oUALRzLnQ__fug28HKRajxOqW3nx8rlT1h7ySH7AO4HyApPSp-lDu62T4hRot8WwqICH4ks7ygvlfXqL5g-bzwcAO7Jjh6V_KabqVNJSdvuBkPVmqEkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
روزهای
بلک جک فارسی
در  Berrybet
💸
بازگشت نقدی:
معادل
0️⃣
1️⃣
🔣
از خالص باخت
💎
حداکثر بازگشت نقدی:
۱۰,۰۰۰,۰۰۰ تومان
❤️
🤌
حداقل شرط واجد شرایط:
۷۵۰,۰۰۰ تومان
🩷
بازی‌های واجد شرایط:
فقط میزهای
بلک جک فارسی
از ارائه‌دهنده
Creedroomz
⏰
روزهای واجد شرایط:
دوشنبه، پنج‌شنبه و جمعه
🌐
ورود به سایت:
➡️
https://teyurixjknfa.shop/fa/affiliates/?btag=914641_l303106
🌐
تلگرام ما:g23
🅰
➡️
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83412" target="_blank">📅 19:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83411">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V73pO2ju3mxKGI69qFblNEWlyfN-fZMkqF-zKSPVr7-y6xOmqIH6xZnR-A4ZPVfT06b1yRgPsGowYzNEh6fARklWaLjFuDOnf4D5VtOHEUnMQ0uku_GGatVxH6Nl4y8LWG9dC8YajlCQ3xCdorPVwPp_VP0u8qcAC_2lBH_3Jl7Z5LlvhQ7hQvizRb6Y48IX_bqKWxAqMx3WlmgAvPOeXcnaEvNjdp8hBcVd3taWQPLNSN2ob4k7p42uY551Xm-jTV1oLZ9KUbNN7fhulnoegzmuJOm3enyFcQa2g-kolzB6-bxKvi-C2Bh46E6RysCE6lIXdcysasrN7mL68f95pA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ته خند
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/83411" target="_blank">📅 19:12 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83410">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BQ0Ia2o5k8k7lZCQeuKUqFlAu9vVSwty1cI0us6J2hoVF_u-KWB7B7sfBmNFuu1UkrOlnhrvEKhyzz7jdLzy623WEv7-JlLKAEaP4ClvWiA95hIqO6vgrFPK4spovB_KaCoYojWuntw4ZixF-kj6mP_5CDEjuCM-oaNsXESU5_Jh36No5gyDDU9DDYj4AWBXJl9q_1DCoKo-_FuoWJhSENWUObjZedvbAQMm6If42vdHxsvrvV3xRP2VRsyAps2ki03XDfKtw6I6GSA_crl1Lc0K5NJqS1_HFpFvef9kbHZ_3NcWPuzi7duZBwCN9AtXluazzi6eUrhlPHeLofXHIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لیست موثق‌ترین و مطمئن‌ترین اخبار ۲۴ ساعت گذشته برای عزیزانی که وقت نداشتن خبر بخونن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/83410" target="_blank">📅 19:05 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83409">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eblKIMaR3Q2_GgZqN9giHskQTdng_A00E07wQUwLHd9cJAC5R0-c86i-ntrNJ5mNjOr2Xoknh5ZdX5RfRVg6XFj3t4m0wyqEFxs1zQkdzyvErnPQP5MQ8STZp6pWkp-W-WxNVhGq23lKAilbdSF1olUpPTqkdNXPvdEWnU1jA4wmCX8tcO9ErTf3v5JILxct4rKJn9Kflau8CFJMXHcLi6tXyIdCZeqfliXBqGGjz4wdvgNtcjL0qQrm02tjOfA5TBIR6N9lzOtMnCUeyj-oyjBVsdn0qoXvQYRQd7Os1HOBsdKv-_a5UL_Jf3llmTy6XffeTjh-bz0vYRlWA890lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تایید میکنم   شین: چندین انفجار در چابهار استان سیستان و بلوچستان  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/83409" target="_blank">📅 18:45 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83408">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">البته مطمئن نیستم ممبرا تو کامنتا گفتن</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83408" target="_blank">📅 18:39 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83407">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">البته مطمئن نیستم ممبرا تو کامنتا گفتن</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/83407" target="_blank">📅 18:35 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83406">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">زدنننن</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/83406" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83404">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83404" target="_blank">📅 18:34 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83403">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMatin</strong></div>
<div class="tg-text">بچها میدونستین خخخخ مخفف خدا خیرت بده خیلی خندیدیمه؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/83403" target="_blank">📅 18:33 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83402">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">حالا بازیگر لر و پژو پارس از کجا قراره پیدا کنن</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/83402" target="_blank">📅 18:25 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83401">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwHfAl6ZE7iAO4DiDC7EzbprJ-eDk1csyRI2sbz1lf_pxvMJQSIw8ImA9PoVgYvyKaLBpkKC3xivk6T4ie3yB5VQjuzgCdfxnUQDODI5GU1G0g4xmszrnLXIMNTK9G25XPpEzj2kpn8UB3JSdW9teal8Mx2fgscmnhZVaOKa37C-N6GxKIBhyD9UZvQOtVaiRb3q3biUcLU6MGGHiBFuonNUhMoNCJRvlfp8iwaUdImspkiWVc3Zu-XFZpYPr36cERna-W89GAu1rE-54lgWNCyQG4UnlFAB6Cx8pVD8urdNQyXkMJ9tUZS8cPEBbdikEuW81u-vhaf8ctZGGsubHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال seal team فصل ۳ قسمت ۸ یچی تو این مایه ها ساخته بودن که خلبان امریکایی تو ایران گیر میوفته و میرن واس نجاتش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83401" target="_blank">📅 18:21 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83400">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">بازیگرش تام کروز باشه کاش، اسمشم بزارن تاپ گان ۳</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83400" target="_blank">📅 18:20 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83399">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">البته یکی دوسال دیگه فیلمشو میسازن میفهمیم</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/83399" target="_blank">📅 18:16 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83398">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع…</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83398" target="_blank">📅 18:15 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83397">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اینام ادامش که میان و میبرنش
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/83397" target="_blank">📅 18:11 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83396">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">پس از ایجکت از جنگنده‌ای که بر فراز ایران سرنگون شد، «براوو»، افسر نیروی هوایی آمریکا، هنگام برخورد با زمین دچار شکستگی کمر، دست و شانه شد. او که به شدت آسیب دیده و در دره‌ای محصور در میان صخره‌ها به دام افتاده بود، می‌گوید تمام توان خود را جمع کرد تا از ارتفاع ۲۱۰۰ متری بالا برود تا از اسارت بگریزد.
او در گفتگو با برنامه «60 Minutes» گفت: «هرگز اجازه ندهید کمبود انگیزه باعث شود پایتان به تلویزیون ایران باز شود.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/83396" target="_blank">📅 18:00 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83395">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">مصاحبه خلبان امریکایی که تو ایران گیر افتاده بود
«براوو»، افسر نیروی هوایی آمریکا که اوایل امسال بر فراز ایران سرنگون شد، می‌گوید: «وقتی به بالا نگاه کردم و هیچ چتر نجاتی ندیدم، آن لحظه ترسانک‌ترین چیزی بود که تا به حال دیده‌ام.»
چتر نجات او در جریان حمله به جنگنده‌اش آسیب دیده بود. براوو می‌گوید در واقع در حال سقوط آزاد بود و متخصصان نظامی بعداً برآورد کردند که او با سرعتی بین ۷۰ تا ۱۰۰ مایل بر ساعت (حدود ۱۱۲ تا ۱۶۰ کیلومتر بر ساعت) به زمین برخورد کرده است.
ما هرگز نخواهیم فهمید براوو دقیقاً با چه سرعتی در حال سقوط بود، اما این برخورد باعث شکستگی کمر او شد. او همچنین دچار شکستگی دست، شکستگی شانه و پیچ‌خوردگی مچ پا شد و از ناحیه بریدگی‌ها و خراشیدگی‌های سر و صورت دچار خونریزی شده بود.
براوو زنده ماندن خود را یک «معجزه امروزی» می‌نامد.
او می‌گوید: «من باور دارم این گواهی بر لطف و مراقبت خدا در زندگی من است که مرا از آن لحظه به گونه‌ای عبور داد که جلوی مصدومیت را نگرفت، اما مانع از آسیب‌های مهلکی شد که می‌توانست توانایی زنده ماندنم را از من بگیرد.»
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/83395" target="_blank">📅 17:49 · 23 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83394">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sI81ljKOXOmsE34LNs72CX_0XYwdUA_aaIi-CH-4vyFjfz7HnKHUuqqNHcSLsRd1Z1naBeqG8V-6un9w0ycY_d9R6dArD2ACgVsNyp0HDv_l6O-e079OlbH8cviU7vNJ6KogeJ0wLSShpQgl5H1xg_2LoYggnTtTo-Bz045yP8u6S864AxQLudx5HX5ZgyeT-5fyA-xn6XIuiLTb2iU7_WVcqfPGFBmMN2AK6oJ7NQuijZ1BXIK9o4r7ccUzTRABV_KAHyCYfle4J_n8Jczk2KemOKw1xAvx2MUzAhrEcxIYB45JmkPnwz9uRnpcJkphkVoP048B1TUgBP1XUF0W8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هادی چوپان چی پیش خودش فکر کرد گفت من هانی رامبدو معروف کردم پسر</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/83394" target="_blank">📅 17:25 · 23 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
