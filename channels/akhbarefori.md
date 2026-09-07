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
<img src="https://cdn4.telesco.pe/file/WhyQmDaD8UBl9Eq-I8gwlRcY7UCaVS_0dLOsIM1pqQG1Nc6Gklab_iG95Y0in9USfSwFFMn7ifOB_11i4U1_HtenDkt4j0fsoH2IQ_bRUjPpqizlqhp8bCEMDghDQy7go0CIc-ojG3C8N9zm7TuuxLUdSh0NS4D_yn92LlCkFDshFpnsANWftkpRPzKVgTANTnvQT0x93Epo8JQAVK3F8cE-q-tOrd08wjpwl5S62Q_XiGrai06kXSFqHhH_Kl8hMJF-m592oyF59biSndldKvWdIUuGxcgi9lDe4CYvIZcJHDHLQIRqmcoJb4TjCfUp5vgWJqhpLs612hdG4hGeaw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 خبرفوری</h1>
<p>@akhbarefori • 👥 4.36M عضو</p>
<a href="https://t.me/akhbarefori" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ﷽تبلیغ درکانال خبرفوری@ads_foriارتباط مستقیم با ادمین تبلیغ@newsadminجهت رزرو تبلیغ تماس بگیرید. 09018373801؛ارتباط با ما@Ertebat_baforiiتبلیغ در ۳۰۰کانال تلگرام@Maino_marketer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-16 19:42:49</div>
<hr>

<div class="tg-post" id="msg-687999">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
فیلترشکن‌ها روزانه ۱۸۹ مگاوات برق مصرف می‌کنند/ توسعه هوش مصنوعی بدون زیرساخت برق شوخی است
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
محدودیت اینترنت و فعال شدن فیلترشکن‌ها روزانه ۱۸۹ مگاوات به مصرف برق ایران اضافه کرد.
🔹
هوش مصنوعی بدون برق و اینترنت امکان‌پذیر نیست و برخی از موبایل‌ها برای استفاده از هوش مصنوعی به فیلترشکن نیز نیاز دارند.
🔹
بدون برق، توسعه فناوری غیرممکن است. اگر مصرف‌کننده‌های جدید مثل هوش مصنوعی را در صنعت برق نبینیم، قطعاً جلوی آن می‌ایستیم.
🔹
در بحران بی‌آبی، پمپ‌ها و تانک‌های آب سر سفره صنعت برق نشستند؛ حالا نوبت فناوری است.
🔹
تا وقتی مشکلات زیرساختی برق حل نشود، صحبت از توسعه هوش مصنوعی و فناوری یک شوخی است. اگر توسعه دانش و فناوری می‌خواهیم، قیمت برق باید واقعی شود.
@Tv_Fori</div>
<div class="tg-footer">👁️ 1K · <a href="https://t.me/akhbarefori/687999" target="_blank">📅 19:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687998">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzGCPLpMyMx-hFhjZNFkMTHmpBPihxiFdEkb1cq5JWPHSomhhP-d2RzWdZhuNFX9M9WZlfvhUOlPpimj9BYU4AqUKIQH3yEJd6kI6rFUjM7wcxojJWqTDi7VP10WbqHXf-6fG8tCx8VUcUCB_dFyOpPXf-Cv4irqwZqCS2fprAXwfc45K-ab1kThSHf7V__8nBOStrlcLjkNOlC5QcJtv7qIZTNyo7OL0RjFp1vM7fHZhbMNrLqX9V7ITFwbTIsEHKxyuWlH-tVglAtlUBwWeaVU_MnUojypWwlhOlil-DDSVXS-XKLBR5onIbnwrBRYPkVCfF8ctEl0dyYWrj1DRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
قیمت خانه در شهرک غرب؛ از ۴۷ میلیارد تا ۱۷۶۰ میلیارد تومان!
#اخبار_تهران
در فضای مجازی
👇
@akhbartehran</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/akhbarefori/687998" target="_blank">📅 19:29 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687992">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HrPcBPmtWYaCSARWM1GL1KUqSPYks7hgAV8ymkCN38A7CatadlzNulSn0mbfURTqPPWGAKySCKW5ISzii7Ej80WnDPaNBW6iuAQ6ZtQ8N5-sit2uWl9Ygoq-mO4Pr-q8-FvxdoShopqcclMWbD3U6VYk92oYCOGFJdBTCKq6_8D7-BeRqeblkBenVeMJ1mmbb-NwbFriNoyWFXj8JToQg78ZDJu-tIM6j_lJayMDS9hvUYoPPUueznrwZzn2Bi8Js50ygkwEogXsV_q46IanRGoK6NxpHfBu65Doo4d3M6Bn1iUrYkUXY_sxj6uuNlY4a84Ks6te_NOt9oKoNO5gyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o-eqlR7JjGNMe5hiSYyu5vzxh4fIiF5jRN2AyH1xYye4Xa-GRYbsNjrrOAF9ngINA7F-zN9kAzSZgkNDvM3Sj6W3eW8cy8RmWDiyc9xqoQQHx14FnfcebEX9OhDRG06l9VmVXM5JKAzmvc7fYZEYU4ZJoMPdmaCeYfPANcOAl-3KrQmmHTgy7pmBbv2vCA8JXRBSzvML6RKGLPark_CbKL5YvFg6wn_yr2QgyFv7L1GI0_k630WZGDH_fJDfGN7Qvwd1YD2UfEV7zoUyrqXF5SFBzL9XD-7ENzteyWBPzKqmiZZvkuHyQvl3tm95S_53tvQZAOFw1rCCOvdNZxVisQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_NQ9FunAaxm7fXiFt-Ku1zc2xDjzfkprsq4-bN9ARQBsPIHGfDpZpD5SptXrRQejw77qtMWk7p1_mwe72tYFfQThQRbv6-v412YmZf3DRgvCuWYWZpXdE8o9DrQeLhZPGavPFY_Ymru4xFEeFLbs2tTAU6nxfqkxPLicBC2KwHtubCIWfj702HNUIdokilywTOkS459-DoNhC4fR9W2b9fKSQwcM1aHEgzAmYL4XtPcbmhswaKKGLxV1s9VQhPR7HIcM-DpcOGETJpqzjECnP1ScC2dyeJ7t7bzIiylvn63Vv5dfV7e0E9vHeBQf64NIRiklxhBL3uL_FUzehkX7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nj7ggD_qkxCy0vugaJXs2YFqPyZ7p8g9eLRnKi0LbXFzfoVYoxOBA-mAZToxUgyyeSZ0q_X54zibh7wu-9fRaJmjYDKtDQn1IIfv0wKepWaukDH10PQvkERttH1M7DA1m4nq0p6-ywppN7YcXZO_fPenUNo1sgI4fQs2pl0ilE9eIQeCtTLSD1JH0K0zTrIsPChoqWKyp-lzTgeOT0DfQK8d0wxfmE6tRdIxV1mI42hPAaEh8BNg0zkaNkNzr0AmckqqAj1HiZOQ3vxdOUg3DGpwMXpMZlToWDETDXjRfeKBwV-Ex3AdHvWtAuLUs506_KxEpGolYyypn-C2pOWQ7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eCUWQrzHwLpaXpW2U-6CIAXbWBhif4nLFpUTzHqLIG_Vruk9WRl4wvgMKR_RIZsU4fCHEkhsv96mUCaR65CljSROGatgXCLKhiCEaOXq7ML1D-AX6xZxrK8zACrlXTn_WsILV3lqViTkfFgIeyK1qW0DT3P4QTUs238Ri2Gr9mS7KfgsuL4hABlW9hwiWmU7y2LTJmsL-Jx-YjwJbJDs7YPjNlrePNxiTP-jk7RdGFTQXbWr1mAxeZ9jWeuyq7LJphhmAfhN39mti-84y4IdBX0L55EF6-IVGAdRUv4jn7qtEgEo_bIOjhYdMcx_B2UAnSwNWme5vJPtRY5wtMFgfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZANusXCLqfWGpDHHe5aPIYsq7oYAwJ4CP6r4l42HdrRkcndeFxWeVnXLN3AVDyU6V06RaVCKvwBphveGbZ4CnL7jN8XkSrnu1_u9ITf8NvlQDou6ZzaB4cggQAGAtpdad9Idzz_6g-yyuPEAJ5ap80afvIHJ5B29LaSzcr9DnVV1FzhQZ6mfJFqQ9bFviCo0FqbPTQZFcSOq96bC3sKnB6jSYaSuO2aMQXmdRUXpb8DMY4yuXg6SXl3n5ZqgsRwfJBIKvbHqYg-YmOg59DgI9svOOAA49KIfKtoOD2rQMx8Gc_TxXvKg-PV4EGpz5HxOa8DGCpKsbYbhmStHd7wZpw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
خیابان‌های توکیو، ژاپن
🇯🇵
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 6.68K · <a href="https://t.me/akhbarefori/687992" target="_blank">📅 19:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687991">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lv3oUWRRWxBZ-grpAQ-UxOJn4myBHdowGckO0IDpmE-XXr6DKm05QMuU72I1hI6wpUUAoBi_IfaZ-SREOAdAVcLufE8CSOxobamhjjK3FflxFAtKEQNneezHwHZy3Pd0Yo70sML2WcuH95doxR0nepSFrGgXhHQRxxiMVOQcp6Z6qWEYm5QsypiUwxAkWJ6TrSAI4x-il4OC_T7DFhVVqeerxduEUrONZ5osXgaaGgfC9ugH6bNji7lT3ev7B-w0j8D5Fy_iMtM9ZQk7P2roARZgSWcyY2hR7lGJKg2HFnp56xGjGULhhjn7wjsg8I1zTbVUaNOP4WKYldgGJuyu4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
الجزیره: سوخت کشتی‌ها در حال کمیاب شدن است و سوخت بانکر مورد استفاده کشتی‌ها در حال کاهش است و این مسئله هزینه حمل‌ونقل دریایی را افزایش میدهد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 7.71K · <a href="https://t.me/akhbarefori/687991" target="_blank">📅 19:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687990">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">♦️
ترامپ: آمریکا را نجات خواهیم داد
دونالد ترامپ که پیش از این مدعی بود نتیجه انتخابات برای او اهمیتی ندارد، ادعا کرد:
🔹
ما در انتخابات میان‌دوره‌ای به پیروزی قاطع دست خواهیم یافت و آمریکا را نجات خواهیم داد.
#Devil
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/akhbarefori/687990" target="_blank">📅 19:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687980">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8LHavKjvEj4jcAfO4NW5hirEO3YdV0PrySbJ6dVBa3c-DJjNYmMr2qJnsORCwgIaVY0Us_6yNPRz3Qm8e3LeY4HJLUVgdKQjI8chzUvtnImZ0eoPu7pyauY_mx6lLxu_ok-J2jqmMFToccvhRP_ntEELsE5bB64V_tnX-2ln1uWsYqgnC9o9bTklfS-yGBKRxqPaQbjlbJ6Gtj-X9XBlZHWR2K7c6tjvm05FXkNos8n-B3EnPjH4wGzKaRps8BBUHlfqPV7eaAqmC3xOj3unrN6mmJ1JVbLj6tqY1QtXk0O9lk3PZhm26AfAQofuIrUOPAU5Mjq7e6juwFrJvDwUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I1ZFQWXBzi9z3LRFeQk4QjGVjn5AGL-m8QqVhJiZx-PkiBrdrMYkad25LssvTcoQ3YWUZ9KdJqlQtIOdtBkqw1XNsrH2npJ6UOtMXKwMiUo-FTEvHVirjtd_TDVINu6fLgHE-9k9XjjztaX1L2QbtxumzA7i8ULPWGVSuSXh1_LA8TN57aRzTHcjvLQ1X4VG4dgN8i3s54lJgXgxZuCFld-kg7iEQTHg-jtxpi1ldjy-ntnEoCD8TPqD8ROJ4HvfydMsfd95ZKf45jhnnsV_e4h4hJYXGvx2PISGlftK32MkkXC0ZCErEQpiOBMI4jGHy1pzPMDNeLpU__Ty6tst7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vFIHLVf7InjKR8WCy4fUCY1fuC3nKR3hthceelP_sx7BxsKYcRCYcHg6XaMeZRg7OI_avwgLsw0vXrs35ddRtqIgWGE5SEutECobrHpxImkbsfntqzUUny33YRC2JzGIqlOHSTxCDlrItyFxjYI-NyW-PYH5IhHYoB7mhVGNfJwrAQauXwh0xUuDRrkMLwcM9UxypXlZCUIqTh08qr4T2pMDc2fOZNoPSpNAlixapThEu6wCZVsgS0RGeLscY89n5w_xpfYs9XsH4fBZ0KUflY2wknamfkjt__QKAWCKVQeCBwWSErcHbVClN7RwHnCthPufy3s0jKUIeMUOGCwz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Xj4uiDwZuEwqLDgSmseyAB7jce9ohw5NzlCoSbuG3TknHewotsMwnXmI3kmwbMmPD9zYN45Xurcs01dWQ4bgcE7pQ2_BkPpOx8B7vIrWG3LgE2GGchFZa-wmLzsTxmsLkcE7Ke59G9SqVJlsuB2nLDLW68egr7eiVC3BAXWAGE_1dAhys8GO4LVnW7S8Srsx1xS8F4TZbh58SWVGp80Zj55YcUWuVuzX7ekDSwhUcbz2ZCpzZSEFh-_Ccm2FZoFaw2_Wnfv6gXZRWIzdmXTT5xbXihzC9DdaxGCg6VOkjVsleV4YVf9Cgi6RvZlH5QFCUNZKfRq_pyGP6_bci9MuaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/d45nqJTCEMguHFqWrhoY23sDiGtwcLoNwEZK1mkjXaV7MnCg0pmZphotf6y7w7cswQ3kdy3dQ4YLQBaXv0u39uDP6_q4JtXOkWLWUwXs-Ga4NzCjBBtV7K2EJrVYqB_YGIYTAnhQNILa5ovF-88hGDWL8jPJ2hsPlOlQYI5LTfE5OJO3bVBmUR3vyqZF-v6VLcjXkUn8klgeI0meOHw35Uh6nnWeNym1Cg7UCyieuPYa8HdcXn_U4BPl7KYQiGcyNlooGlVMFBWEX_AkZebAhd7b6AMSMsQjW8xApkxgFBK3JYghLJWa9WWx0dJY49Ix_-GX3JJz8wI4EZBxKYX-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Gnmkm8ZnbTS1TmEVfZk3T0_i1EuJd3rgVhiFA28HB8tn5tftb9Mp3ZDs8Ert-SmtqESZmWq5lMY4Vj0XZB6Z66YMScz-8ow9v0flT0jACZwg-KO6p8SOvXXUL2cL3wdrU9nZE-56qLL9inCPZzw7HJqr1MUBNd8T_cPOpznQMcDluLlikifu4IrkY3EObt8Ota_mrIEhnNB5pIlyRNU_ZsOgcWE7qBnb-iDSeUcq_S_qvn9g2ySX4_HfAr8oFyFr8AlHfwDisOqnVoZ1XlKgcOEEYm9CjcNCFZlenlYhoGR93E7ofVoPz0E18wK0WolgTN3DelCnCmZgGEOqIU50Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E58zabdNTbg-ROBE_gn2qnHMsOHrtshuYNPakF7MpgBLCMgZjvFODfDLSZhI-kPONKyXR_3gapQnq9-ZnuiSFDgfWn_C99F3lM-ZQFR1coJBe2z-MdBWyDwnlea1piP01lCe0IOQmVPah4al8Q9Y4ZXJjebqT2R9doiZbcxSEIjlsE-qoUXNiduJtje6O7b75ZjkvhVNpeyxzratl9xrB4oKBOAoaHRKIcLcLiaYS7SkmGnxFA4LEVH02oI_783C0GXWdP1cjG_736kdzjLnmELAts-_6VfjlK6MEG0hY2-nsuJqKGu_qVLGw5sxJHOQhWk1qm4YP_uTrejOOhKQkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OyhTORPFOL3m3NbJo2uu8X7uFDwV7kPe06B6-QhLoxOA_5307OHJwkL8cD2eMhZwnsVFxMNuwL6blo7GCz5pAyjyeC1HHsu6uPgSXFnzXKyX-YY7Jq-gtkEZ_MG7Gc370vFej7dUHnCxhldoOqR_5idqc3XEaIhmyTD9xbCH9Pqxk5AgQd7jAB1vkK5udT9CgLNXd1wvWzuXIORRMeA73LHmsLBzjQI_1DRTEi-I34AK0WnI9jGDES6LsSy4Q1WYJ0sTQ0_J1D3EvQqCUj1ha5LDum983c5bbSSddKWyg6dOfgdRcw3jSS_VIq_ULEF00uyvsSj-LtYAH4o-XQqTEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e8jbhoslNgYr_6ySKCjQFEi8IZfRVr6DA4Vgdult0p6suH2QdUsBDEXi8AnClJDCapqXw50nwPz6kNRbNVSb9UJ3jpd735xKRIEYltjwmGu0MJKdb0iU3gOzLYJjhA3_T8bCHrPBIUcqae-bB0F2yehDi0k7Q6e_52s9WdG9cdnV_75uCPQjTPpD3xF5mhrzzKSqV7z1Ffng7nb5ngzOBCGjyc2V7mRajF2ff2waxncAP3crtttZN2FWWYedamOZdtfhf4Ay-MmVkErGW6VmGhOgvE5G4n34lF2qDYzDaSZKjeY59AIROBq_b0wqoluTkUD8vE3ANzEr3sbB5Ma2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZSyueKMa5BaNdbDLvk7NO4lm79gzUQP5zufvuHM0PcWcijDHVuTL5Z0v44mEvc-oz_NwBoKKREcARntKgiPoaS8a_kCtcL8FeOtwoS2G6W6fhUC0pvlYc4r0YBwPsQZxE4g2i6rJCj4EPrthGr1Iffu2xs__qZ3ntQVuePBkQ2tqUV-z53tn3ja2gAEUKMPAb5NnxwHvC8zy-AYhsnrMKQap3ry3233gzmPAlxsuo8CDjRvez8iXFaW13kn4BCiJqGZw5RQCWnPe_kRWR8-Fm51ws4_d8uOQX9nBtFUHIti6hClU0P_763INX4bnBu7kFLTtx9LmiZO05FKmMDDy2A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درد دارو
🔹
موانع و مشکلات  شما مخاطبین گرامی برای  دسترسی پایدار به داروهای ضروری
🔸
ما پیگیر مسائل و بازتاب‌دهنده دغدغه‌های شما مخاطبین عزیز هستیم؛الوفوری را دنبال کنید
👇
#درد_دارو
@Alo_fori</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/687980" target="_blank">📅 19:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687979">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nd9xFD8n3uYI83rZCK5pUwZ8U6zQsPO-m1coXB36p185g7pqN9y43_C2bnlgnrBlyYi_u0-Wj6DnGm7FcYqbCvxf6V8amiJ4WBk3ain_4SgAV2rk4WUiJR79h5QiPXzHgMcfjFPB0n4HeRBTYJsi2MmM9aVR6ydS-nJTjKwfpqpnLXWbiSvuKwdW1uK_njE0S8cYQgabZsYX0QxAqjK9gSGIgItHCbPULn4lf51zB6c06XDXKoeFRGKVZd_TEN9eBZEzQvAskIOdn8LMIynRAQtF9BXtK7XFzqTDY966LDUmx0JtzbBG_hhGXSYrPkNTaN6ECPBt3kj4-yW2oRZ4nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفت برنت ۹۸ دلاری شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/akhbarefori/687979" target="_blank">📅 19:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687978">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsJMj9Vgz03WDlBYfmi2V3k4FTcgJ1L6Mdx5c_8EYGma0uTi6dYkmGDYF8cJi3SO7Y-jxJhPDd0IF4QL7iDiz_02O7d-YwgJEohTGtJZUDwc1X3LJ4K_8g6md3cvOgtayZT_5tUj0ncl2Gv9uVD4XHRriyXipNr7tI02W7gTfEHLGM3C00JLLbAgvRennW_iTk85SAx6TFjE-f2dkoSV4CqicLtiKfEB4r1czvDPypQ26z4DfGSw_yIO5zx3imx_v_-gNDpRDaT-71iKU6F2m68OG34i-YM8sl1HeKZxPaxuRPOCTQez-tuQOL08smFf-zxZWvPyQ2GfUYdCCD97Bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
دونالد ترامپ به مقاله وال استریت ژورنال اشاره کرد که در آن ادعا شده: سران ایران خواستار پایان جنگ شدند
#Devil
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/akhbarefori/687978" target="_blank">📅 18:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687977">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
سیم ۴۵۰ برابر شد اما برق تنها ۳۸ برابر / صنعت برق با طلب ۳۰۰ همتی چگونه رشد کند؟
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
مجلس یازدهم قانون مانع‌زدایی از توسعه صنعت برق را کلید زد که جای تشکر دارد، اما این کار خیلی دیر شده و حالا با اعتراض مردم و صنایع مواجهیم.
🔹
۱۱۰ هزار میلیارد تومان پول برق مصرفی صنایع به صنعت برق پرداخت نشده است. نتیجه‌اش هم این است که پول پیمانکاران بخش خصوصی پرداخت نمی‌شود.
🔹
روی کاغذ، وزارت نیرو متولی صنعت برق است، اما تداخل مدیریتی داریم و مشخص نیست واقعاً متولی کیست.
🔹
دولت دو نرخ تکلیفی و بهای تمام شده را برای برق تعیین کرده است و  قرار بود اختلاف آن را دولت بپردازد، اما هنوز پرداخت نکرده است. بیش از ۲۰۰ هزار میلیارد تومان بدهی دولت به صنعت برق است.
🔹
وقتی صنعت ۳۰۰ هزار میلیارد تومان طلبکار است، چطور انتظار داریم رشد کند؟
🔹
از سال ۱۳۸۴ تا ۱۴۰۴، قیمت مس ۴۵۰ برابر، آلومینیوم ۴۸۰ برابر و حقوق و دستمزد ۸۹ برابر شده؛ اما قیمت برق فقط ۳۸ برابر! مگر می‌شود یک صنعت زیربنایی را این‌طور اداره کرد؟
@Tv_Fori</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/akhbarefori/687977" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687976">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">♦️
کارت امید مادران شارژ شد
معاون وزیر رفاه:
🔹
مرحله پنجم کارت امید مادران شارژ شد و مشمولان می‌توانند اقلام مورد نیاز خود را خریداری کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/akhbarefori/687976" target="_blank">📅 18:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687975">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afd014bb00.mp4?token=RLy4g-MWfCUodM8dH9X4lPhtZXOJAI5s90Wb5OJxs90ZJ7RZJ0riUrD92avZn1zYcPNEveVz7neDVkLQslAaBrcX9GILLA8YASlWjb3D_PM4yOnnV_TBTxc8MtZJX38WkeKFtYDm35fuxOCZe3DWELDIYsnODzzj_2S_s_DN4IeZ-2ww87d2Crhzjfz5-rBdyZkoaS1978IowOqaUFt_14bOJSCtjxaXSC2goOdUL3HT3gtQ19N4lGhMgJDk97Dm-5Co-WM7UCpp9OFAVc7s_eVsmClTAdLFTbo_IJqBVkprDGp9wpFwXJHZSsgixuQA2ZK61GXdhKSVBpx6Y88YqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afd014bb00.mp4?token=RLy4g-MWfCUodM8dH9X4lPhtZXOJAI5s90Wb5OJxs90ZJ7RZJ0riUrD92avZn1zYcPNEveVz7neDVkLQslAaBrcX9GILLA8YASlWjb3D_PM4yOnnV_TBTxc8MtZJX38WkeKFtYDm35fuxOCZe3DWELDIYsnODzzj_2S_s_DN4IeZ-2ww87d2Crhzjfz5-rBdyZkoaS1978IowOqaUFt_14bOJSCtjxaXSC2goOdUL3HT3gtQ19N4lGhMgJDk97Dm-5Co-WM7UCpp9OFAVc7s_eVsmClTAdLFTbo_IJqBVkprDGp9wpFwXJHZSsgixuQA2ZK61GXdhKSVBpx6Y88YqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چطور تفاوت انواع باز کردن رو در زبان‌انگلیسی یاد بگیریم؟ #زبان_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/akhbarefori/687975" target="_blank">📅 18:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687974">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f8a9998442.mp4?token=r0Pfwbza1J9rKRYS7d5MLzsoMCnGbi5jQU7O8Oum1ffsRn8IuybwVw4zrSWreovqrEqBre1JVJbjHn4MpYfI05b9lTsuQFrMVaEl1duL7N84zxrLnOfKrwMBm4QRHMBBKE9g9wZenuGpJGmQPtWZqqPSHgK6HF6LT6jX8ch3B-fS2gzW-KnxHaqs-sa590Ek9JPPHR8qusctMesylriWX6Vve1--pVx4Rg3x45MJ2cAL5Q7QETMmpA5aFrknxgzBmIiGkCgFmq1-1AkXncxrj-CPScWLjSQf-90gnAi9e9vzfdjJkAr18xeI2ouStx1Xa0Oi6H3MwmmlVUssO0f8Lj6Kmw-t-5MQRFxdq5HKWr-63MhKpLX5Oa09E0pOpZTeI51s_jcTYyqqUS8XDNsrbwcgP88bROcV0IEFGEzYV7TWLPQV2teMPAxSTCm0WHqP6C1oYMs-mUGFAOu2Q26AskZZASo3Q94ib_Ra5JJDlTc2XTdt8QG8RY2KvHTpgDUmu0kUpABF8NcIziTyezuNFOEsrci6llyDEAlwf6Qy6LnKnrvDJs2QLpSMLOFAbXc4mTIbbOfaquTP4jjV7H_8nEeJ20AkhAyo_P63CrrrkcIYunGtnIG5zmBAIlR84_rn6WzR94g4VEJfmUWfrVZVJ9k37IEOJ3XkocubUHAtsEo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f8a9998442.mp4?token=r0Pfwbza1J9rKRYS7d5MLzsoMCnGbi5jQU7O8Oum1ffsRn8IuybwVw4zrSWreovqrEqBre1JVJbjHn4MpYfI05b9lTsuQFrMVaEl1duL7N84zxrLnOfKrwMBm4QRHMBBKE9g9wZenuGpJGmQPtWZqqPSHgK6HF6LT6jX8ch3B-fS2gzW-KnxHaqs-sa590Ek9JPPHR8qusctMesylriWX6Vve1--pVx4Rg3x45MJ2cAL5Q7QETMmpA5aFrknxgzBmIiGkCgFmq1-1AkXncxrj-CPScWLjSQf-90gnAi9e9vzfdjJkAr18xeI2ouStx1Xa0Oi6H3MwmmlVUssO0f8Lj6Kmw-t-5MQRFxdq5HKWr-63MhKpLX5Oa09E0pOpZTeI51s_jcTYyqqUS8XDNsrbwcgP88bROcV0IEFGEzYV7TWLPQV2teMPAxSTCm0WHqP6C1oYMs-mUGFAOu2Q26AskZZASo3Q94ib_Ra5JJDlTc2XTdt8QG8RY2KvHTpgDUmu0kUpABF8NcIziTyezuNFOEsrci6llyDEAlwf6Qy6LnKnrvDJs2QLpSMLOFAbXc4mTIbbOfaquTP4jjV7H_8nEeJ20AkhAyo_P63CrrrkcIYunGtnIG5zmBAIlR84_rn6WzR94g4VEJfmUWfrVZVJ9k37IEOJ3XkocubUHAtsEo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
کلیپ جدیدی که سایت حسن روحانی منتشر کرد/ روحانی: دوقطبی‌سازی میان موشک و دیپلماسی بی‌اساس است
حسن روحانی:
🔹
حمایت از نیروهای مسلح و دیپلماسی منافاتی ندارد و «موشک، پهپاد و مذاکره همگی از کشور دفاع می‌کنند.»
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/akhbarefori/687974" target="_blank">📅 18:20 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687973">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">♦️
سخنگوی هیئت‌رئیسه مجلس: خبر مخالفت هیئت‌رئیسه با خرید تجهیزات و تسلیحات نظامی از چین کذب است و مجلس از هر اقدامی برای تقویت بنیه دفاعی کشور حمایت می‌کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/akhbarefori/687973" target="_blank">📅 18:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687972">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95959f5d94.mp4?token=paKGKxy9Ndz54AQb-Bm8OUBqMMbW1_cYC2y51seySrH-qn3e-G5C9KYVb7QZxM2EMrMYBP9T14-Bqq-XU5QEmH23pKREX3jtTOLjMaZNnxciVicRCDbOEajFArSRwtZ1ExJCkPRrt5k99wEEDCRB7vNZi7wHy9LsPQ3UeZ7U3E8ZQZWQvH0oLViwwNHfAaCKOKsSGSUqvvYKBzxi-V1M4vW8PJvkYoRC4iau0WDXyCPJeFzQli6X4-4GM_9IUPfusFDaoFxHfAXN0sRagk8d4kyU6PqoPWWLGPEzHuEIEAjRvpdbM4Oqoj7YRqI6u-W4Kp4mjJNCQ7UVaW_2YRPYyQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95959f5d94.mp4?token=paKGKxy9Ndz54AQb-Bm8OUBqMMbW1_cYC2y51seySrH-qn3e-G5C9KYVb7QZxM2EMrMYBP9T14-Bqq-XU5QEmH23pKREX3jtTOLjMaZNnxciVicRCDbOEajFArSRwtZ1ExJCkPRrt5k99wEEDCRB7vNZi7wHy9LsPQ3UeZ7U3E8ZQZWQvH0oLViwwNHfAaCKOKsSGSUqvvYKBzxi-V1M4vW8PJvkYoRC4iau0WDXyCPJeFzQli6X4-4GM_9IUPfusFDaoFxHfAXN0sRagk8d4kyU6PqoPWWLGPEzHuEIEAjRvpdbM4Oqoj7YRqI6u-W4Kp4mjJNCQ7UVaW_2YRPYyQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علی آقامحمدی، عضو مجمع تشخیص مصلحت نظام: بعد از انتخابات آمریکا، جنگ به حالت قبلی خود بر می‌گردد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/akhbarefori/687972" target="_blank">📅 18:12 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687971">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/M6ROlQUO9sFqpCQWA7IvQRht69ZpHKh2jRElvV3MQUxRTTxg7Mo5KBHL41iU0HVro8kp1kD3srRuTGtKW56B83qT49VPEw3J02XHtHWvvmq9o70eoypCmlhriMKvK9UmkmszczghYDaxaCcoTSYoIyjTcKvprz_CTiAKcZRjWYzO9rr4iNmYv75ID4HY1dGwFka1KPa4T7a4FQjmDkicC3GZ26w3nqI6lJq0UK_gE3E_4aIjDogF5EthOlwix36kNlRARhpX5r_Sgi2ZOq8NDXWB4QctKp9BGHUB4CFmfA7JE6vWj3vCsV_9r12HvhI1f_IzAIUXayKF33SwxLmAIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
درس‌های سیل مرگبار نپال؛ گرمایش زمین چه بلاهای دیگری سرمان می‌آورد؟
🔹
حادثه مرگبار و ویرانگر سیل و رانش زمین که هفته گذشته مناطق مرزی نپال و چین را دچار خسارات فراوان کرد، یک زنگ خطر بسیار جدی است که نشان می دهد بلایای طبیعی ناشی از تغییرات آب و هوایی، چالشی جدی برای تمام جهان ایجاد کرده‌ و آمادگی بیشتر و اقدام جدی تر جامعه جهانی برای مقابله با "گرمایش زمین" را بیش از هر زمان دیگر ضروری ساخته است.
بیشتر بخوانید
👇
khabarfoori.com/fa/tiny/news-3243383</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/akhbarefori/687971" target="_blank">📅 18:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687970">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b8spscSmCAZQsQpDPTSylj1yD3CL0UWQT7nvMWtg_9edSaHLbSNt6qbyo8HXv-L1ovSlJjvMXr_03VKc0ZcjFlut2zJym5b-Un1n_0GB6theT27ls9QXQ0BuAuOnVn6KV2TqKIbFgeST3qmwq7ePwSh_ZfHEIZmu4-VlRS6QPmnLvRHxPwVkdGxwocwLF_GdSxd2TpjVn2kNHtAPTG3wAayNhb0-e5H3gV_dvQtohzbHO3dE3oY24f0-zIeiVFg7DGN9q15gVPNIZhGobvVNU_heMpRPOuZVU38PuWR5jJxcvv4TWhI4VJlK181_L60pzrv6Gy7oUTfVb3vVUB1YQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۳۱
شهریورماه؛ آخرین مهلت شرکت در جشنواره بزرگ قرعه­ کشی حساب‌های قرض‌الحسنه پس‌انداز بانک سپه
🔰
آخرین مهلت شرکت در چهل و ششمین دوره جشنواره بزرگ قرعه کشی حساب‌های قرض‌الحسنه پس‌انداز بانک سپه، تا تاریخ ۳۱ شهریورماه اعلام شد.
🔸
به گزارش پایگاه اطلاع‌رسانی بانک سپه، چهل و ششمین دوره جشنواره حساب‌های قرض‌الحسنه پس‌انداز بانک سپه با استقبال پرشور و اعتماد گسترده هموطنان عزیز، تا پایان شهریورماه ادامه خواهد داشت. هموطنان و سپرده‌گذاران گرامی می‌توانند تا ۳۱ شهریورماه جهت افتتاح، تکمیل و افزایش موجودی حساب‌های قرض‌الحسنه پس‌انداز خود اقدام نمایند.
https://sphbank.ir/news-1301/14050616/5349
@AkhbareFori</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/akhbarefori/687970" target="_blank">📅 18:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687969">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a87e72f58.mp4?token=KB60_5DbsEZEZIuHxsTh_Uehy4jpEaiw0-hmp-UQIYoExKZJQpd4nvyoy2FwEnWFOOTJnpJhEJ_1PwW_tzQIV6cVWMuEYFiPt0To7rk-vI8qL55JOtuc1wUsxyaMmvS5IIQ96ZXG_8ERXcEJwmQmPTB4M--NXl5Cwb2JjeChV-tJifYvHtMhq0lqqKac5DyQAZEQedi0sCvgBZW1CwZUohtFU2_CltqWN6gdoQyJ2uF2F-2lEc7RS1uAPhfqaPp0Zw5FfOAlW1PdkGYCHzpbTUByVDwShZm8IzIpxlnH6oliJZ3ypnusw-L3lLyubHlAExzTIIwtbC1xtgNBwbOGlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a87e72f58.mp4?token=KB60_5DbsEZEZIuHxsTh_Uehy4jpEaiw0-hmp-UQIYoExKZJQpd4nvyoy2FwEnWFOOTJnpJhEJ_1PwW_tzQIV6cVWMuEYFiPt0To7rk-vI8qL55JOtuc1wUsxyaMmvS5IIQ96ZXG_8ERXcEJwmQmPTB4M--NXl5Cwb2JjeChV-tJifYvHtMhq0lqqKac5DyQAZEQedi0sCvgBZW1CwZUohtFU2_CltqWN6gdoQyJ2uF2F-2lEc7RS1uAPhfqaPp0Zw5FfOAlW1PdkGYCHzpbTUByVDwShZm8IzIpxlnH6oliJZ3ypnusw-L3lLyubHlAExzTIIwtbC1xtgNBwbOGlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
می‌دونستی خط زرد‌های پیاده‌رو چطوری اختراع شدند؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/akhbarefori/687969" target="_blank">📅 17:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687968">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlGrFho9QqH45ooGf_Griby1I7PFnq3c1oDPW0iob-KKbQiY3xY4VIvo7_1MceUj6Ze3hFwdDuyQxGWGIPgeofVMWQPF97b6DSispZHT9IMXKMxR3o7oT_HaklENDHGCS--jczA95TnwRtCKKgNJAnHPlWxF8VdC_QvoX47-nuQzfXjdT1TSAMGtFfyPdC315v6AtX7FrVZrRKpH6KCWgGSSHUkkVZH9W0-mc6undWSx_oIsMGcsSmv4Z3a480_HfxFU77CQeUvryVqqvC9qb68hVGuG91rUM1JS9pxFf64MYs1Iu1CXaWoiOa2U8t9lJ43uCw_g8lKN5YjL4rRChA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
حمید رسایی: این کالابرگ نیست کلاه‌برگ است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/akhbarefori/687968" target="_blank">📅 17:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687967">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xu86QpTdFLUegSMN_npIhIBAe_RMp6B0dehnSpfAvO6NohCwrPYXdP5SHLSi3AyTPM6ufnV83QeP5Upg0rIGaG1pl70tv-JVBSnEVJc6QqnXJ-Ld8SXYACdxa2YaIx7hhnfvFoY5pwFnvTFXGM5ayHLwZkmhvrgXQ77UKvShbqWQyHiEZ_-FBjlcWekIdx4-ufJlXoBpVyYIb0tqdtUHz7xuqLf88t0lzlYs_silQTnPt1u22LYTYPoxYP5LCxw57hMhCupldN5wrS6n_jDV_-EPPiS62VIlfi-lsVzP_LnQQ6bBgur6OLcpfNiQoSSDCEn5QdN1X8X8MRCYEbpoBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
احمد امید بخوای طهرانی
🔹
کاندیدای مستقل سومین دوره انتخابات هیئت مدیره کانون وکلای دادگستری استان تهران
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/akhbarefori/687967" target="_blank">📅 17:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687966">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-text">♦️
نهاده‌های دام و طیور تا ۴ ماه آینده تامین است
داوود رنگی، رئیس اتحادیه واردکنندگان نهادهای دامی در
#گفتگو
با خبرفوری:
🔹
در حال حاضر از نظر تأمین نهاده مشکلی نداریم و ذخایر کشور به اندازه مصرف ۳ تا ۴ ماه است.
🔹
در نهاده‌های دام و طیور وفور کالا وجود دارد و رقابت سنگینی میان واردکنندگان برای فروش شکل گرفته است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/akhbarefori/687966" target="_blank">📅 17:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687965">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">♦️
استفاده از مسیر ایرانی در تنگه هرمز همچنان در اولویت است
🔹
طبق داده‌های مارین‌ترافیک، عبور از تنگه هرمز ۲۸٪ کاهش یافته و از ۴۰ عبور ثبت‌شده، ۳۲ مورد از مسیر ایرانی انجام شده است.
🔹
در مقابل، تردد در باب‌المندب ۹.۷٪ افزایش یافته است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/akhbarefori/687965" target="_blank">📅 17:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687964">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/amf-XiCFDPceYDrZwKHH28jq-jkbK0imRKfWh8_birQSLCyVZDrcwcj0LSnpzyUEh57Co09XEiH7kxBJrQfhsnKVgAFrrtJaDClqpOO3JipXDHLvQNN5wi-jCFI8FjTuzzSDNArEEIz-b9rrCbUNiXdXhnttrK6YaWHDnd1ifMNfx8EE_pOOCk-fEmeDst2kpG0XTmsUstPpdXcq90bJL39Y0K8HdZlEyVigkwVHDSCbDvLsV5cxkPJUEgyAt_ud0AyfM1oWh1auIHGJg4K5WX0-WmbMeZsqYnAIr3sPQjK98n2haiFmOeIDH7bdBS_xnK5njdKFxcdYtXeComDImw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهندسان ایرانی خسارت ۲ ساله در ۴۵ روز جبران کردند
🔹
کوره قوس الکتریکی شماره ۸ فولاد مبارکه که پیش‌بینی می‌شد ترمیم خسارت آن ۲ سال زمان ببرد، با ۳۹ هزار ساعت کار مهندسان ایرانی ظرف ۴۵ روز بازسازی شد و به مدار تولید بازگشت.
@amarfact</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/akhbarefori/687964" target="_blank">📅 17:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687963">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAdad │ آداد</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/p1LoUol7kHfJvOYBhCi49x0pl6Ipk3gInSef_wDw4AqDnJJaWCUyuz2NsVpGHND3ImAIt_eJ_oSDIx9ZaIkrkzyR24g_XfIlQdc94jsQsOy-8HaUFnNj9xx8yuDtMk82hH6aQm1-V0TyQ8UFP-I-YMnpdagHiu3NRoEAAE2MnmWe8AGCs4bkGsgsxSbVCIEUOOdXvqCeYd2DCqnTZVLm_0ah-9tgIwYEGzdP3eDX9LQyThfTyUMo-HdZwYX7IZ6-8V1dQqTcn4j798uzoW3zDPTHq8xcJLYog7OZfpzPBu2W48Sc126RPCmlSOJO1oiSkBLJ2vGQIgNcTptY7-sY2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚖️
قبل از هر اقدام حقوقی، از آداد بپرس
آداد، هوش مصنوعی تخصصی حقوق ایران است؛ برای بررسی مسئله‌های حقوقی، اسناد و قراردادها ، تنظیم اوراق قضایی، انجام محاسبات قضایی و آماده‌شدن برای قدم بعدی.
با آداد می‌تونی:
🔹
سؤال حقوقی بپرسی
🔹
قرارداد و اسناد را بررسی کنی
🔹
مسیر مناسب برای مسئله‌ات را پیدا کنی
🔹
پیش‌نویس لایحه، اظهارنامه، دادخواست یا قرارداد بگیری
👇
رایگان با آداد شروع کن
https://go.adadai.ir/PGOFF4V
@adadai_ir</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/akhbarefori/687963" target="_blank">📅 17:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687962">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E8r_LejXW-FU-n_0uoqs9eQdIyMNcpTHURm9KPX02qGPY6mXhD7GtjlQlyb1iIgeL9jG4lc8sYgHhm8g615j_yTSyESeMRVCWrfu3VVb3lu-gBlHW1t2yqp6QIhuGuL3u4vRcvi6xmgFqet3wa_nb-GIppARJweBtHiCLgjrCjBIox8vJlkivobi4Fu99vnbnrm0PrLFWxm8Y1UtNHRdihDKqcvi7Bc3dDfUFJdPFhFSddSOF8gG1vOkK2TqCbR3PI9x130dhfOXQNdT_8BCIf4lOfn5_SXxQGXgRfXHJOBlyFrcAOOrzUV5dADRTsTkefkBhEV3hxzncg2qb8_yFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آیین‌نامه به‌کارگیری ایده‌های نخبگان بر اساس تأکید رهبر انقلاب تدوین شد.
🔹
حسین افشین، معاون علمی رئیس‌جمهور، در نشست با نخبگان و فعالان علمی و فناور خراسان جنوبی از تدوین پیش‌نویس
آیین‌نامه به‌کارگیری فناوری‌ها و نوآوری‌های پیشنهادی نخبگان جوان
خبر داد.
🔹
به گفته افشین، این پیش‌نویس در
۵ ماده
تدوین شده و اکنون در کمیسیون‌های تخصصی دولت در حال بررسی است.
🔹
بر اساس این آیین‌نامه،
معاونت علمی رئیس‌جمهور حلقه وصل نخبگان و دستگاه‌های اجرایی
خواهد بود؛ دستگاه‌ها مسائل و نیازهای خود را مطرح می‌کنند و نخبگان برای حل آنها راهکارهای فناورانه و نوآورانه ارائه خواهند داد.
🔹
افشین تأکید کرد این طرح با توجه به
تأکید رهبر انقلاب بر به‌کارگیری فناوری‌ها و نوآوری‌های پیشنهادی نخبگان جوان
تدوین شده و هدف آن، استفاده سریع‌تر از ظرفیت نخبگان جوان و فاصله گرفتن از روال‌های معمول برای حل مسائل کشور است.
🔹
پیش‌نویس آیین‌نامه مذکور پیش از تصویب نهایی در دولت،  توسط بنیاد ملی نخبگان منتشر می‌شود تا نخبگان نظرات خود را از طریق بنیادهای استانی درباره آن ارائه کنند.
@AkhbareFori</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/akhbarefori/687962" target="_blank">📅 17:11 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687961">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">♦️
سردار آزمون در آستانه بازگشت به تیم ملی
عبدالکریم حسین‌زاده، معاون رئیس‌جمهور:
🔹
پزشکیان شخصاً موضوع بازگشت آزمون را پیگیری کرده و ۹۰ درصد مسائل او حل شده است./ خبرآنلاین
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/akhbarefori/687961" target="_blank">📅 17:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687960">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">♦️
بمباران کاروان نظامی مزدواران سعودی در پایگاه «الودیعه» با موشک‌های بالستیک یمنی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/akhbarefori/687960" target="_blank">📅 17:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687959">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">♦️
گروسی، مدیرکل آژانس اتمی: بازگشت به دیپلماسی درباره وضعیت برنامه هسته‌ای ایران ضروری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 25.5K · <a href="https://t.me/akhbarefori/687959" target="_blank">📅 17:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687958">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">♦️
سهمیه هر دو کارت تمام شود، مردم چگونه بنزین بزنند؟
معاون وزیر نفت:
🔹
سوخت‌گیری افراد پس از احراز هویت و متناسب با سیاست مصرفی تعیین‌شده، امکان‌پذیر خواهد بود.
🔹
در این طرح اطلاعات کارت بانکی ارسال می‌شود و سامانه مانا کد ملی را به سوئیچ سهمیه ارسال می‌کند.
🔹
در آنجا مشخص است که فردی که به جایگاه مراجعه کرده، تا آن زمان چقدر سوخت‌گیری کرده و چقدر می‌خواهد سوخت‌گیری کند و سپس می‌تواند بدون محدودیت سوخت‌گیری خود را انجام دهد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/akhbarefori/687958" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687957">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">♦️
تکذیب شد/ تأمین اجتماعی توقف پرداخت معوقات بازنشستگان را تکذیب کرد
🔹
پرداخت معوقات فروردین‌ماه ۱۴۰۵ بازنشستگان از ۹ شهریور آغاز شده و طبق حروف الفبا، به‌صورت تدریجی و مستمر ادامه دارد؛ سازمان تأمین اجتماعی اعلام کرد این روند بدون وقفه تا تکمیل پرداخت‌ها ادامه خواهد داشت.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/akhbarefori/687957" target="_blank">📅 16:45 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687956">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">♦️
لینک یاب فایل های صوتی گنجینه معنوی کانال
:
🔹
زندگی پس از زندگی
فصل یک | فصل دو
| فصل سوم
|
فصل چهارم
|
فصل پنجم
|
فصل ششم
🔹
چله علم و نور  "یک"
،
چله"دوم"
،
چله"سوم"
🔹
مستند شنود
🔹
آن ۳۱۳ نفر
🔹
تفسیر سوره‌های صف
|
مسد
🔹
سنت‌های الهی خداوند
🔹
شرح به وقت شام ۱
و
شرح به وقت ایران ۲
🔹
پادکست کسب‌وکار رادیو کار نکن
🔹
ادعیه روزهای هفته
🔹
برنامه کتاب‌باز
🔹
شرح و تفسیر کتب:
"سه دقیقه در قیامت"
،
"آن سوی مرگ"
🔹
چگونه با عبادت تفریح کنیم؟
🔹
حال خوش معنوی در زندگی
🔹
چله جوشن کبیر اول
و
چله دوم
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687956" target="_blank">📅 16:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687955">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">♦️
یکه‌تازی «وتجارت» در بازار کارمزدها ادامه دارد
🔹
بانک تجارت در پنج‌ ماهه نخست سال ۱۴۰۵ با عبور هوشمندانه از الگوی سنتی درآمدزایی و ثبت جهش‌های معنادار آماری نسبت به مدت مشابه سال قبل، فصل نوینی از استقرار بانکداری مدرن را رقم زد:
🔹
رشد ۵۷ درصدی درآمدهای عملیاتی
🔹
افزایش ۷۰ درصدی درآمدهای کارمزدی
🔹
رشد ۶۰ درصدی خالص درآمد عملیاتی
🔹
افزایش ۶۴ درصدی منابع
🔹
رشد ۶۱ درصدی تسهیلات
🔹
جهش ۱۹۸ درصدی سپرده‌های ارزی
🔹
افزایش ۱۴۲ درصدی تسهیلات ارزی
رشد درآمدهای کارمزدی، توسعه فعالیت‌های ارزی، افزایش منابع جاری و تنوع‌بخشی به سبد درآمدی، نشان می‌دهد بانک تجارت در حال حرکت از الگوی سنتی درآمدزایی به سمت بانکداری خدمات‌محور و مدرن است.
📌
بانکداری به نفع همه؛ به سبک تجارت
🌐
مشروح خبر
👉
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/akhbarefori/687955" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687954">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12c7771ad5.mp4?token=XWEzghQ7qNMHjWl12eA8Bz2DWQaJxglJAqQHnQHsy6BZfHBYaA5oo4uzW294a-njecdeZxumKZj_cFUFuZUg7b40Xm9vV54rKrYxFVr6fwHt5f_wEmOvlJ4QClPY-AVm8UlnzWKK5yUofmKBgeRNoybeGVlYbJR7SPPJ1cO500yRH7vIogNwkZXmehvslGBmoKcRpVWNg_XWLNJoRLQw0bNEH_Q76QMlrrJtaTASj2XMnG9fdXw81b_UohhPDDpR3AQ_oz5UKm2U1qzWsN0zO1yhPh-V31KSwhQ7QVWIzbFvFQXwbNEDmi7rZSZstFNYfnydC5nKLNbTnON1azLc2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12c7771ad5.mp4?token=XWEzghQ7qNMHjWl12eA8Bz2DWQaJxglJAqQHnQHsy6BZfHBYaA5oo4uzW294a-njecdeZxumKZj_cFUFuZUg7b40Xm9vV54rKrYxFVr6fwHt5f_wEmOvlJ4QClPY-AVm8UlnzWKK5yUofmKBgeRNoybeGVlYbJR7SPPJ1cO500yRH7vIogNwkZXmehvslGBmoKcRpVWNg_XWLNJoRLQw0bNEH_Q76QMlrrJtaTASj2XMnG9fdXw81b_UohhPDDpR3AQ_oz5UKm2U1qzWsN0zO1yhPh-V31KSwhQ7QVWIzbFvFQXwbNEDmi7rZSZstFNYfnydC5nKLNbTnON1azLc2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
لحظۀ مجروح شدن خبرنگار المنار در حملۀ هوایی اسرائیل
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/akhbarefori/687954" target="_blank">📅 16:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687953">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5bd99461d6.mp4?token=XpeqroL04yfKzglqiLaTOVlprUg4ZrjBVXKCtczNul29cTBUiY-M1scAPE0TRXiYuEtBST1JcMhoGEDdFkiEoGMHMvtqCHKw_WBqAnjbOzM_NrtyjMnBCNANQh5oezrtnMJRCjFH4FSvlNJQ0vK0au_3jwX7HW01mb2Z5XZI3GDvZJM5M6KeGnsdwENtDX8MzaYAnXzUdoHMHS61bHf-gqEVgaPD2bGs_Ly39eEgQQJjg7_DuJ2v3_PVfYKPaQyatCWpiyTqoI1kILBbPdaSGkjKBgZxE3utLb3_IloKhvb-eox5-n05KpsDeMUK4fGZj7orCUgxQ_HU-XCljOWwDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5bd99461d6.mp4?token=XpeqroL04yfKzglqiLaTOVlprUg4ZrjBVXKCtczNul29cTBUiY-M1scAPE0TRXiYuEtBST1JcMhoGEDdFkiEoGMHMvtqCHKw_WBqAnjbOzM_NrtyjMnBCNANQh5oezrtnMJRCjFH4FSvlNJQ0vK0au_3jwX7HW01mb2Z5XZI3GDvZJM5M6KeGnsdwENtDX8MzaYAnXzUdoHMHS61bHf-gqEVgaPD2bGs_Ly39eEgQQJjg7_DuJ2v3_PVfYKPaQyatCWpiyTqoI1kILBbPdaSGkjKBgZxE3utLb3_IloKhvb-eox5-n05KpsDeMUK4fGZj7orCUgxQ_HU-XCljOWwDDzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
علت وجود ماینرها به اقتصاد مریض بازمی‌گردد/ راه بهتر این است که تولیدی ماینر راه بیاندازیم و دولت هم عوارض آن را بگیرد
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
مردم بخش کوچکی از تقصیر مصرف بالای برق را بر عهده دارند. ما از درآمدهای خود مالیات پرداخت می‌کنیم و در ازای این عوارض، از دولت انتظار داریم یک جاده‌ی سالم برای کسب‌وکارمان فراهم کند.
🔹
درباره ماینرها؛ آن‌ها فقط برق مصرف نمی‌کنند، اینترنت هم مصرف می‌کنند و محال است نشود آن‌ها را از طریق آی‌پی شناسایی کرد.
🔹
علت وجود ماینرها این است که اقتصاد مریض است. تا زمانی که اقتصاد درست نشود، مردم به دنبال راه‌های غیرقانونی می‌روند.
🔹
اصلاً چرا باید جلوی ماینرها را بست؟ هر چیزی را که ببندید، بازار سیاه درست می‌شود. ماینر مگه بیزینس نیست؟ راه بهتر این است که تولیدی ماینر را راه بیندازیم و دولت هم عوارض آن را بگیرد.
@Tv_Fori</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/akhbarefori/687953" target="_blank">📅 16:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687951">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/561ec2a9de.mp4?token=vFJzZTLozApemwEhIAJfxwSlIs9N_DHBI4qK9phj3I46SqywWE3Youn-tx2uAHDd1Cp7XLwdCgmMfPrh6sjcjealrBAtnawv99KrbFS34-hvzwvjN0nE2QHH77aq5KuYNJ9I5eBt9c2F3-gV9XmPqmRNURNLMiqUO3rw60-uY1pmgVx8dzQNdVoZUKcEctN9QZjUwpXjT-l4x_zVnTWbTS2IsG7eZr3kwJXj8n3Rr5xewzIPxm5LUaXi6YSLuc0A7bkoHL4gXq5KOelLoT8vTyWNbV_tk9sSe9w33zYGo1pCt-N4VsJEiiTB3sLF3H2vjiWtUknYLzaob3g2u2FAyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/561ec2a9de.mp4?token=vFJzZTLozApemwEhIAJfxwSlIs9N_DHBI4qK9phj3I46SqywWE3Youn-tx2uAHDd1Cp7XLwdCgmMfPrh6sjcjealrBAtnawv99KrbFS34-hvzwvjN0nE2QHH77aq5KuYNJ9I5eBt9c2F3-gV9XmPqmRNURNLMiqUO3rw60-uY1pmgVx8dzQNdVoZUKcEctN9QZjUwpXjT-l4x_zVnTWbTS2IsG7eZr3kwJXj8n3Rr5xewzIPxm5LUaXi6YSLuc0A7bkoHL4gXq5KOelLoT8vTyWNbV_tk9sSe9w33zYGo1pCt-N4VsJEiiTB3sLF3H2vjiWtUknYLzaob3g2u2FAyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
هرپولی که در حساب‌تونه برای ترید کردن مناسب نیست، قبل ترید حتما این نکات رو در نظر بگیرید
#دارایی_هوشمند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 30K · <a href="https://t.me/akhbarefori/687951" target="_blank">📅 16:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687950">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">♦️
سخنگوی وزارت خارجه قطر: جنگ با ایران نشان داد اتحاد با آمریکا کافی نیست
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/akhbarefori/687950" target="_blank">📅 15:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687949">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec5f662aa3.mp4?token=KMQnFqvPwIN85FVe7ZK3yR8-YqYYHQb9zhBvtcmm699nRvYMlAznCuVwnJ00mbZtLFCfENGDQJ1Us4NiHyjKss4084h_qU3NBv7s0YE3lw3SHNXHoyqItqJrWOLrFj3R4nk1CZA2evwID_ZQ-ypiRj8M3-o7ozNki3kr2Ao_zcPOyAPUgsNYNeazDOZVeQaq0kctBPePEVfXRC_4SikBC-y8Q7XTV8TltP52S-f0x5L5Xo0Y8e40ek4cZ8aJeYJKoQIMyeeZxmUWdJYGpEDivsR-WXt5Y9nsDq4W4uIkWlmNPBMoBw8nxnlxkU1I2rEccVTHIkPp4hvP-Ymz43V-sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec5f662aa3.mp4?token=KMQnFqvPwIN85FVe7ZK3yR8-YqYYHQb9zhBvtcmm699nRvYMlAznCuVwnJ00mbZtLFCfENGDQJ1Us4NiHyjKss4084h_qU3NBv7s0YE3lw3SHNXHoyqItqJrWOLrFj3R4nk1CZA2evwID_ZQ-ypiRj8M3-o7ozNki3kr2Ao_zcPOyAPUgsNYNeazDOZVeQaq0kctBPePEVfXRC_4SikBC-y8Q7XTV8TltP52S-f0x5L5Xo0Y8e40ek4cZ8aJeYJKoQIMyeeZxmUWdJYGpEDivsR-WXt5Y9nsDq4W4uIkWlmNPBMoBw8nxnlxkU1I2rEccVTHIkPp4hvP-Ymz43V-sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گروسی، مدیرکل آژانس اتمی: بازگشت به دیپلماسی درباره وضعیت برنامه هسته‌ای ایران ضروری است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 30.3K · <a href="https://t.me/akhbarefori/687949" target="_blank">📅 15:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687945">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AqLtq5zN7WYWxm299ti8BbCCpb9kTKbcv3hWsbNz0EI1q0F-yEJEnwTx9RMksGj1Vq05CweS_FGUjNANIArM6_AiKMrIFE0li4XFSW9Yt0GHi1SUpxDi_MIAymOI2gG5o9jaK1CQ0Nm8NmvbWaCb6C3w24UxrSXuZkGtE9SjHcZgFblAmste4goa1R3nrBCres0-IcC3bitZrgKviQF-4gppd-86YU6O63NeCe9ua-x-fK7AJMqA1tgOln2kRbZxAM-rVAkwTbqyBwKBOMygZJtqTPqstlegRECH7hlRqUwE65hJq7QF6MIbYFtDokfnL0UZVgwYVwevzt_74JDd7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WOkLbmIua-hgywhsqMYkGly6tjibZjZRgZi8mHEXdC2WZHaRkgbFa6cqn_--7kJvR70uWpU_7_AwDzqGLm5tW36Sw0yM-KwW4T_uEyIbxPrCkzuT2WdNx0BOcI17RdBjg2_tLIE4XVpwFtv6NPNxXDdskZtMWNWnH9KJVsKb8bhcN4pSIb5s_0LHE8y3u54-uczCjQHQP46AmszbxzLoMesRaNYXFZ9BfVFo3GB9ea-j0EKLfhZgNaKogaiBZIVGWM7ZvSuAvUqi8jgp8aK-mu4-NstiES11AzhOmP2LCvhrBxzjrswXY6sB3Nig_mSajlQuChLL29xtjhmvFPTqIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fiMcWNC34FnXDiZylyWJ90jjCD511e0qXH1XekmZOULiT7odTd-skW6u11Hzldq7kQkTXfQ97LajVXd5PSi1zzsnNt_DNmyHBlDFCtJ8VXhuduCM9JO0dhsTIiLNJYqqbcSnUjWqhaRVYlsYs1xUt7VxsErN4EmcMC3SxTQSu75XAHR0M_piIBd9rIBcalc_kwX78bOTypU1wj715FQHl2uj89rxA5Fx4F_Q9CkmWhowWgDjhzEIRFoG1YwHhAcpks-SliJJP0u_yfYDYnuCJpifakOqRr1rnvsUNItlvxERH5zxLClutDX8V4LdETN8AB9oNXMglcSS4AdanZwazw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JPXt_7Dt7-2IcjGdbwqUOqJXgAkNDrL041uu3fz8Mm7TB3T7ZdsEEOEAj-Sr2Olf1LPRTGXdfc1MrhMVLOYuaTPT4IJyLkKFyJYVWVbA1MQI33IIFO4LbB7MxSWIcA5WOKtHkOvqzDTWQeVY0B4O817Jntu5_eK0hsG4K3QFoqilBZXkOjawl5YCaypjFPHEpYysDb6NvlG-H-opuN731YeZvbvhxPsPu4cD6GF2jZ6LgKgrQicmbKnv0bQH7QGAturMsZy80fuSJrZYECpPltJJYRZ2pDD5wPNs-hTeda3_AfHpIaiAzHVykISmn6dxfLRFbuWYFcPh2xtcxhk0VA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
درخت سیب نیوتن هنوز زنده است!
🔹
درخت معروفی که گفته می‌شود نیوتن با دیدن افتادن سیب از آن به ایده گرانش رسید، در محوطه خانه کودکی او در لینکلن‌شایر انگلستان قرار دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.9K · <a href="https://t.me/akhbarefori/687945" target="_blank">📅 15:46 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687943">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce8679746b.mp4?token=fwYGp_3so0rvVKuf8EZ6q93_Xu_xNHd5p_2gggxd-BTfsN2-ct6-tIY6W7mnG05Vm7_z1BdMwy_9KXRr8nLEGUxaGBZdoNvJ0FqPEOuLRotU335LG6dCWzW3DPP_v2KYeR48ozfSZ7uPoNQs7IlDQLwSNiuiv7q4iHDJx8FZ3fUjlvHOk6D_loLNcDrhP1NGQjpxJ-Z-0jcMRUU0NDPmmSBYUIlj6W4GuTmSRgOrmYrfeZExxbLygjO18gL-yJkDrr-8CAJ1RlxjtRh8s2PY6PgDscJtSKYyhJ_-JCB5n1k3kGD_hdZR2GJXByCrBQOmRNlw3IsdMLamEXrnGl6CmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce8679746b.mp4?token=fwYGp_3so0rvVKuf8EZ6q93_Xu_xNHd5p_2gggxd-BTfsN2-ct6-tIY6W7mnG05Vm7_z1BdMwy_9KXRr8nLEGUxaGBZdoNvJ0FqPEOuLRotU335LG6dCWzW3DPP_v2KYeR48ozfSZ7uPoNQs7IlDQLwSNiuiv7q4iHDJx8FZ3fUjlvHOk6D_loLNcDrhP1NGQjpxJ-Z-0jcMRUU0NDPmmSBYUIlj6W4GuTmSRgOrmYrfeZExxbLygjO18gL-yJkDrr-8CAJ1RlxjtRh8s2PY6PgDscJtSKYyhJ_-JCB5n1k3kGD_hdZR2GJXByCrBQOmRNlw3IsdMLamEXrnGl6CmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
تعارف؛ پل عجیبی در بوشهر که سوژه کاربران شد!
#اخبار_بوشهر
در فضای مجازی
👇
@akhbarboushehr</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687943" target="_blank">📅 15:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687942">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">♦️
صداوسیما: برخلاف برخی ادعاهای طرف‌های وابسته به رژیم صهیونیستی، تپه علی‌الطاهر اشغال نشده است
📲
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/687942" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687941">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">♦️
چرخه ضربان قلب‌ما مثل یک کارخونه‌ای که در هرلحظه از شبانه‌روز مشغوله و سخت تلاش می‌کنه #حواست_هست
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687941" target="_blank">📅 15:13 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687940">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FC2w-Y9ZXwDByOdNxlulLrG-I7XJt8Szxb7yhcpC175iOKLgOc0z5a0gUlEcR5xnEf7D8hjB2mRtoh9OPZRIjosEUo_b_jZjYk-cFEiAIW0hgISZE8cmfXbuN86wtqAMdA_S9OeppZUB4-ypSrYJyUtMJOhR52COFioz_qoyr6o8zY8It2uPr9Izk5_w0HR8pKaHwVXILDNiAQpid8Lh_T932jLtUjgijvsQGlc86MI54j-32bwlX1Inar46_AO3ZbVyi4Imr0iJzhO9aNNXhAQotfguDEHbPBfgPy_VFYvdon58FKKAQ7_qXtOox8i6__SFJccIXemffmaVxWTzyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
ماری ترامپ برادرزاده ترامپ: دونالد ترامپ دارد جلوی چشم ما از نظر روانی و رفتاری از کنترل خارج می‌شود؛ فقط کافی است به دیوانگی‌هایی که در شبکه‌های اجتماعی منتشر کرده نگاه کنید
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.4K · <a href="https://t.me/akhbarefori/687940" target="_blank">📅 15:10 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687939">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رسمی الکام‍‍پ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76899b0ddf.mp4?token=RTKSJwdBjcSkAqpJOGBkFmf95V0YYgM9mK8s_htL1rJWGuZ580wxMNe7KFS42bfmvs-0Ci7Phz12lv-7ZJrOlf1dif_dIJc2MeNGDlCskitHlV_RuWpYX2pVnXSjmV63pQJSZ-ANjyj39iXJw2e4vM6mIJVcGnlDjamIlpVWhjywD1w8Txom5fqLthI-WPGiMZI0A2MkRuEq9ICDnJ7TK6Sw7iVObPHtQfd5p-yNz8ePAE5OcpQmU3TRQIFguXMKiMsmXJwqo-dQPpfEg0ZN7ccxy2xID6r0NjI_Rtk50MQii8v94PdB8rFWeTi1KDib5LJ8eDzxMihdEnb_rM3Gpg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76899b0ddf.mp4?token=RTKSJwdBjcSkAqpJOGBkFmf95V0YYgM9mK8s_htL1rJWGuZ580wxMNe7KFS42bfmvs-0Ci7Phz12lv-7ZJrOlf1dif_dIJc2MeNGDlCskitHlV_RuWpYX2pVnXSjmV63pQJSZ-ANjyj39iXJw2e4vM6mIJVcGnlDjamIlpVWhjywD1w8Txom5fqLthI-WPGiMZI0A2MkRuEq9ICDnJ7TK6Sw7iVObPHtQfd5p-yNz8ePAE5OcpQmU3TRQIFguXMKiMsmXJwqo-dQPpfEg0ZN7ccxy2xID6r0NjI_Rtk50MQii8v94PdB8rFWeTi1KDib5LJ8eDzxMihdEnb_rM3Gpg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">برای نخستین بار اتفاق افتاد ، حضور استعدادهای درخشان
#دانش‌آموزی
در
#الکامپ۲۹
،
با همکاری ستاد اجرایی
#الکامپ
و سازمان ملی پرورش استعدادهای درخشان،
#الکام‌سمپاد
متولد شد.</div>
<div class="tg-footer">👁️ 32.7K · <a href="https://t.me/akhbarefori/687939" target="_blank">📅 15:08 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687938">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTV فوری</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/687abf05ce.mp4?token=TZh0dUzJRiNLMhU9P9XXuRQxd-ySNvJlCbzat8IcTjWJ3RLoQ1JoZfQkaQTjMdfby9T_DL6qpq-KadSXhc40kIwDJqV69P1UBysFxU8ovLAT5aqGNyIp0CS7iskDJrGIpFy0bI8DMRv97-xbBjsOXVOZZCO9PyqU2JIoci009IMv00SkWm3MJAuy_IUEn3SflFfdkEzHDvASAsODicvnnS2EgTAFYjquTcOU3eku7xPt8CZu67BXhimUAIEUbEpjTQP3eMHOwL8AStFHBfmeV7ER3DWwXotbra0eAw4I72p6l1u9TLsni9MXJ2kza3VfB_4mOoes13rJ9a-pP0w3ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/687abf05ce.mp4?token=TZh0dUzJRiNLMhU9P9XXuRQxd-ySNvJlCbzat8IcTjWJ3RLoQ1JoZfQkaQTjMdfby9T_DL6qpq-KadSXhc40kIwDJqV69P1UBysFxU8ovLAT5aqGNyIp0CS7iskDJrGIpFy0bI8DMRv97-xbBjsOXVOZZCO9PyqU2JIoci009IMv00SkWm3MJAuy_IUEn3SflFfdkEzHDvASAsODicvnnS2EgTAFYjquTcOU3eku7xPt8CZu67BXhimUAIEUbEpjTQP3eMHOwL8AStFHBfmeV7ER3DWwXotbra0eAw4I72p6l1u9TLsni9MXJ2kza3VfB_4mOoes13rJ9a-pP0w3ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
مجلس به اسم حمایت از مردم تصویب قیمت‌ها را گذاشت / دولت احمدی‌نژاد بار یارانه‌ها را روی شانه صنعت برق گذاشت
مهدی مسائلی، دبیرکل سندیکای برق ایران در
#گفتگو
با خبرفوری:
🔹
مهم‌ترین چالش صنعت برق اقتصاد آن است. دولت هنوز باور ندارد برق یک کالای اساسی، استراتژیک و در سطح امنیت کشور است.
بی‌توجهی به اقتصاد برق در تمام این سال‌ها انباشته شده و امروز خودش را به شکل ناترازی نشان می‌دهد.
🔹
مقصر ماجرا از «ب» بسم‌الله مجلس بود که به اسم حمایت از مردم تصویب قیمت‌ها را گذاشت.
🔹
دولت احمدی‌نژاد فشار آورد و بار یارانه‌ها را روی دوش صنعت برق انداخت تا جایی که این صنعت حتی توان تأمین حداقل‌های خود را هم از دست داد.
🔹
وقتی دخل و خرج صنعت با هم نخواند، توسعه متوقف می‌شود و مردم هم نسبت به ناترازی معترض می‌شوند. امروز سرمایه‌گذاری در صنعت برق هیچ جذابیتی ندارد چون این صنعت از طرف مجلس و دولت حمایت نشده است.
@Tv_Fori</div>
<div class="tg-footer">👁️ 35K · <a href="https://t.me/akhbarefori/687938" target="_blank">📅 14:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687936">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">♦️
معاون بهداشت وزارت بهداشت: ویروس کرونا همانند دوران اوج از سطح هشدار عبور نکرده است
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/akhbarefori/687936" target="_blank">📅 14:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">♦️
وقوع چند انفجار در آرامکو
فایننشال تایمز:
🔹
پالایشگاه جیزان با ظرفیت ۴۰۰ هزار بشکه در روز هفته‌هاست به‌دلیل حملات از مدار خارج شده و حمله جدید، بازگشت آن به فعالیت کامل را دشوارتر کرده است.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687932" target="_blank">📅 14:33 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59ba1bd1af.mp4?token=YE89jdKbvn-qLIa8zYb-bdy224Mx-MzQ48YFihS4SVrUIvgd2e1I_UnN4iAa9UEL8Z1LUTYD0kPK3jYROoGdSSrFu0Vl8QcO5tEAIFSMjka0lIYb9W5jS_erCXp32Wvacw0XLUwcr00AunWjZBwRuqdqNs2WEO97gQrEesGaxVBcB5JU9oZMYf5Id7cs6OgV4sCM8451q5kzqdgYU0eV-WEzOqAh8btoqikTpRKA9pq8AcYWEGJrtXH5JvO6ngz1w70-sQayx04uLAbeG1aO_n_8unicLQJWZCRJ0TVA2PwGD62DAScw5SlidcxwCm8W9WEnvegF6IQ-6lguqEd3oA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59ba1bd1af.mp4?token=YE89jdKbvn-qLIa8zYb-bdy224Mx-MzQ48YFihS4SVrUIvgd2e1I_UnN4iAa9UEL8Z1LUTYD0kPK3jYROoGdSSrFu0Vl8QcO5tEAIFSMjka0lIYb9W5jS_erCXp32Wvacw0XLUwcr00AunWjZBwRuqdqNs2WEO97gQrEesGaxVBcB5JU9oZMYf5Id7cs6OgV4sCM8451q5kzqdgYU0eV-WEzOqAh8btoqikTpRKA9pq8AcYWEGJrtXH5JvO6ngz1w70-sQayx04uLAbeG1aO_n_8unicLQJWZCRJ0TVA2PwGD62DAScw5SlidcxwCm8W9WEnvegF6IQ-6lguqEd3oA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ایلان ماسک: تهِ تهش ۱۰ سال دیگه وقت داریم که با کار کردن پول دربیاریم بعد از اون، هوش مصنوعی بیشتر کارها رو دستش می‌گیره و واقعاً دیگه دلیلی نداره کسی بابت وقتی که می‌ذاری بهت پول بده
🔹
اون فرمول قدیمی که چند ساعت در روز کار می‌کردی تا آخر ماه حقوق بگیری، رسماً داره به آخر خط می‌رسه.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.6K · <a href="https://t.me/akhbarefori/687931" target="_blank">📅 14:26 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">♦️
گروسی، مدیرکل آژانس اتمی: بازگشت به دیپلماسی درباره وضعیت برنامه هسته‌ای ایران ضروری است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687930" target="_blank">📅 14:18 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">♦️
ریزش معدن آلبلاغ اسفراین؛ یک کشته و ۲ مصدوم
🔹
در پی ریزش معدن آلبلاغ در خراسان شمالی، یک نفر جان باخت و ۲ نفر مصدوم شدند. عملیات امدادرسانی با انتقال مصدومان به مراکز درمانی و خارج‌سازی پیکر فرد فوت‌شده پایان یافت.
#اخبار_خراسان_شمالی
در فضای مجازی
👇
@akhbarkhorasanshomali</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687929" target="_blank">📅 14:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رسمی الکام‍‍پ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bbaffec5c4.mp4?token=ZQKtg2wvhqI4-bp_8FJYNJLcrXm45xn3RWBVFzUHBYXv_nNktDmi_kYAHcM97s_M1aE_K1NIIETh4-WfN_mbUh_3AUqwDWJwdz0VejBjeizolCP5AYb2R6Yco_4yjW5r-4C_WIRPQ5KYy6Lg6L0f6G8MhgyQx3oDFVcCyMgAm721EAR5EA_85scI3ZHwbx9Q64IagraW_KEuMCwuZAa-tc614gSzG8XW_L42paBqLtkWwLq1EwHmzi0ZcsuwVTzQfljLoMgEUsdc5xzJizf3D_z5pxGYvDBR3opSK3kdbdr18orRhjnNq1Yf4I-EdOZ8__dZSJm-hRMYhM-OjvHa_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bbaffec5c4.mp4?token=ZQKtg2wvhqI4-bp_8FJYNJLcrXm45xn3RWBVFzUHBYXv_nNktDmi_kYAHcM97s_M1aE_K1NIIETh4-WfN_mbUh_3AUqwDWJwdz0VejBjeizolCP5AYb2R6Yco_4yjW5r-4C_WIRPQ5KYy6Lg6L0f6G8MhgyQx3oDFVcCyMgAm721EAR5EA_85scI3ZHwbx9Q64IagraW_KEuMCwuZAa-tc614gSzG8XW_L42paBqLtkWwLq1EwHmzi0ZcsuwVTzQfljLoMgEUsdc5xzJizf3D_z5pxGYvDBR3opSK3kdbdr18orRhjnNq1Yf4I-EdOZ8__dZSJm-hRMYhM-OjvHa_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور فریلنسرها در
#الکامپ۲۹
، جایی که عرصه جدیدی برای ارائه مهارت ها ، توانایی ها و کارایی
#فریلنسرها
فراهم شد.</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687928" target="_blank">📅 14:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687923">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nOSPov8Jqlmayl82PhICtUkt_7s_VMBpxhWocnS2En9GyAL99-I6O6XosnzceH8VDzCx5zrclJ-gyR4dHjo6_5yUaDYKxVnmr6ey-Arl-dW3PJi0oONlx54Q_vrUeujopB5To-W0PBDNq50BTuqksSAdialInaYla1A8gklQg1tZ3B8UT12xlAY9ubcoMk2IjRilRv62sTyUwhvvJPpTlouRH-1DTS3PyVSK5cTgI_lza4k5YlZKLu65kf1pZqcLbTKNSoviLrJtp11L_ODt5OkRt_XXCY83Nqmrkwr-lbeRAlMVkex1P9oEFNsAYCUdQ8wuF3tzVNUqefTvyGietg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iiO57kTlbLN4hQAvXqwG3PtzmrUv2TN8gMplHf8Kbk_6-4HNmScujGKBM-lvhjIond2s21-ZBWevKGV6W-sidoM44CKvH1iWZ1UMfLWbRWpLe08aE0T_tr-Y58ZQR1K1fwhZFsG8JcYox2eWfmEINV7BQxLcBluQxQr1NwAuslzE2qlXG3DBt7E7O_sOPoxYfKPJ9IfTeOhGIR8ZWCmjwhKqJlufpz9Q6cJnpViwrYvyQddAAbmEbOQ2mkhRYKvxoZ74KwawoPKl_XJUaz1jkkn5iy7xeM701nH44AuBEONwKHE1PyUYSVMBfcMhPpOHqfIwocW40aYIdGLDDuPvlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TA_po7D_S_6tXSlK0q5ckjJzkD5SJK9eSTeBBHZ5WEJ_tLUccd_Ux-Y-4eG66intZmXXyZBjg50nN6ahShgdxMPZDFNnbpk-jkNuo4spYnNHgvA0SzQgj2Gd3uaJyCAgT4l3VYlEI_y1aa2CJwAorz1CwYfkTtkH_c53Qj5l5-saWzVW9WFMVGTUxB2HLq6F-ONYP3t1GmySE_qR8XMBog8ozObGSxRu3VVWtDyiHVsjhOj9C9qbyVQzjTjyWBwkBpEg2eV9OkfFo_f69sHXhofBkDMAb9EQ5CnacIJLikeuv1dmkrP8GqyZrxCvUiTE3eJZi6CjT-chU-0JPfWj7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ai27r3TDevEYrw2EnHgAgL4__-yplwVZmf6QUdccA2kg0nLwfWcxi7CF7NStHVqf6Dq4YeWhsnf7LUMylekkY5WPBFOQlHEyPsVqt6zGnHt-iN9wHsHqBmnLW-Jt9JN7gMpQUp3szYGoYvNCTJtTqHkavKLwClNiSldBp9-5V8yHUVEB-QCaIPBgOoMqHafGmw9nXPJSdQHCzGyLyCIByL9M8lTkmGKQvGbj18zxJSPk-1suDXa7RmjkwoyBQ7bSIWRIJdBJ0UdBG8cztPfj9iUstkkaIO0el3Av0zcdkH0GnPgVUJtI9CkA8ekoqI3p6TDOe6ES3t1yPlFSRFvBlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mfW_EOhdBIV4O4zqsu58w_Xnszz2yn5X-ndIoEvzzn1wL_fyARhsjQpgyyzDOqKpAaQY9WcTjd8mxyXVz1B3yRpf4ShRvVccb1pSh68BziQipaQ6EqbmN_P2ANfY8VhuTBTnMulIdeHIfo_rBtlNY14C4Snm7rzEsTwaFjLgied8fFuyd5Ow6tE08EYYyk3Tfo-bB6ORalcAEJE8S7u9BPMn2wyKSyG99Zta3bFoMh7ZJmKhX2FDlUmYyVkDiUpw7O3M_4SCCrIDlmlwTRKqfzQ6OTOJ2IW-m90caLapf-g85ai7D_48dMRB4XesGssRigQkfc9m56SK-bdtuX1n-w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
وقتشه با سرآستین‌های متفاوت و شیک استایلت رو خاص‌تر کنی #استایل_فوری
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/akhbarefori/687923" target="_blank">📅 14:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687921">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">♦️
ثبت سفارش واردات موبایل آغاز شد
🔹
امکان ثبت سفارش و ویرایش ثبت سفارش واردات تلفن همراه هوشمند از امروز ۱۶ شهریور در سامانه جامع تجارت فراهم شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/687921" target="_blank">📅 13:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687920">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">♦️
هشدار درباره تبلیغات آمپول‌های لاغری
مدیرکل دفتر پایش و نظارت بر مصرف فرآورده‌های سلامت سازمان غذا و دارو:
🔹
داروهای کاهش وزن راهکاری برای لاغری صرفاً با هدف زیبایی نیستند و مصرفشان باید با تشخیص پزشک و متناسب با شرایط فرد انجام شود. مردم نیز نباید تحت تأثیر تبلیغات و توصیه‌های غیرتخصصی این داروها را مصرف کنند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/akhbarefori/687920" target="_blank">📅 13:50 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687918">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0285cead3c.mp4?token=IgpbUuL4lmywaGFWxSh3QXDPWQWuGoldRkKPJ9kb-Otr5p5BgT4VQpq8RHjiwqzMXl914ymHL3f50ctwCaTtyN8VdLBqXXrnvn44o9JW1XF1eS5wnpERQv3x80Z8kOlRvghbUQoGsImDwDEOTkW5ylsUrF0Ek9r6LIIsWdF83267IkBmCmEdkJaevw3jofjJTGjzqkCkdSdAschYOJhQ6of6B-YcTA72V8RaEC3oQArNVdLYIyAil3Hnd5OYKvbk5xD6mTPyYXoVVCOr_Y4hGz-X3JWPSOv_b2Kj1hRjUecQNQQ78QBiwNSHEzktg5qJXpJLXi-Uc5KHYbdaX1bwbpAarUS-mmp-ajyXFu-V46W6p1yK1SASJtyv9OZIJ8D7uFtfEpu8eXliCWGbPUjqGr-RLYEq7D9MttVJr6gb7e-hwNFUKGVtYj8h0m4TMf6j-EGK6h1BpVr65ls4fGxCzeSW9qqO4GFZlsjB8XrEpD4bXW7ug4o3xSMzFzvnZoGdCRICu7jEtwT2jTwEVaWl3qMke13qRIRU_tkJlXH7w1qSQLXEMtchfBKV8WiVic2UxIOhdxDDIHj3WHwQnoh-pGAm1VpWmt4Z6s9pNJu9r5H0qo-LagAAy1lNOYJkUWZVC0mLsSdbfFYyvwOJylb_N2cLuRygYNgB2lYPH_xA7fk" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0285cead3c.mp4?token=IgpbUuL4lmywaGFWxSh3QXDPWQWuGoldRkKPJ9kb-Otr5p5BgT4VQpq8RHjiwqzMXl914ymHL3f50ctwCaTtyN8VdLBqXXrnvn44o9JW1XF1eS5wnpERQv3x80Z8kOlRvghbUQoGsImDwDEOTkW5ylsUrF0Ek9r6LIIsWdF83267IkBmCmEdkJaevw3jofjJTGjzqkCkdSdAschYOJhQ6of6B-YcTA72V8RaEC3oQArNVdLYIyAil3Hnd5OYKvbk5xD6mTPyYXoVVCOr_Y4hGz-X3JWPSOv_b2Kj1hRjUecQNQQ78QBiwNSHEzktg5qJXpJLXi-Uc5KHYbdaX1bwbpAarUS-mmp-ajyXFu-V46W6p1yK1SASJtyv9OZIJ8D7uFtfEpu8eXliCWGbPUjqGr-RLYEq7D9MttVJr6gb7e-hwNFUKGVtYj8h0m4TMf6j-EGK6h1BpVr65ls4fGxCzeSW9qqO4GFZlsjB8XrEpD4bXW7ug4o3xSMzFzvnZoGdCRICu7jEtwT2jTwEVaWl3qMke13qRIRU_tkJlXH7w1qSQLXEMtchfBKV8WiVic2UxIOhdxDDIHj3WHwQnoh-pGAm1VpWmt4Z6s9pNJu9r5H0qo-LagAAy1lNOYJkUWZVC0mLsSdbfFYyvwOJylb_N2cLuRygYNgB2lYPH_xA7fk" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
چرا اسکورت نفتکش‌ها برای آمریکا به بن‌بست رسیده است؟
لوسیانو زاکارا، استاد پیشین مطالعات سیاست خاورمیانه:
🔹
اسکورت هر نفتکش و حضور نظامی آمریکا در منطقه در بلندمدت قابل دوام نیست و ادامه آن برای واشنگتن پرهزینه خواهد بود.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/687918" target="_blank">📅 13:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687917">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو: یک میلیون دز واکسن آنفلوآنزا از چین و روسیه وارد می‌شود
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 39.6K · <a href="https://t.me/akhbarefori/687917" target="_blank">📅 13:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687916">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">♦️
لغو ناگهانی بازگشت صیادان ایرانی؛ امارات بدون ارائه دلیل مانع خروج شد. با وجود صدور بلیت و انجام هماهنگی‌ها، خروج صیادان هرمزگانی در آخرین لحظه متوقف شد
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 40.9K · <a href="https://t.me/akhbarefori/687916" target="_blank">📅 13:14 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687915">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jEmZ3TwBEBT-9cz0-dVE_IGW3k39miV-d5BhJGYyeKb5l3TzbYgJqJe0SaIvua6ZFxASFPSVb2R2-N1e0LJ7J-owRel2g4QTZLguntdbjLmI3p-oTOMdzCY0kEkyLIh4rtlfTsMrvLZU3sZh89gd0p3ksyrx0QOyiZRNJL0pmWu5-BUek2Ls8Cbct0UdGadK6FfGihtDAn1jZQZAINGgMUSlGIgWr1eq5wsVFZftDD51NCnupa2IXnKnXQ2sUA4uHBZFDJER6nc6S3_SczG2zoBw2Rz7ock5aeyk7-xby4CA5IkFk33CeIVj1ZG9rKuKP7rUwGpxI8zpJ0EJa5fyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
چرا آسم در زنان شایع‌تر است؟
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/687915" target="_blank">📅 13:06 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687913">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FkkTcsNOqaDxnpbZT5a1z-jMBwVkhR0UsNaoFYreZ1LsPhr2wV5Z0_PD47pmR9Ykwsqz6ut_qIIFOM-J7mPJxKPR_Ge3BsjOdxbmHEhTV49-CsOQGybjMnr3P6yA7KcWNo8YulJ79i642RShXLJ-vgbqWmMMZYacLSu_yMpGYBNeBirDQ2eMrvMV9Gna41EOWZ7WN7GqBIjVcLOCxiL7ce8e1E3NfzrtHxBrwaW5PJEbiF9Fn8BVTt5bAtbe_xenfmIaVBtUr0iaGBQU74_5g7X8cbmmA1pORjvrLNSjSkFBdox5-3TDB8vORHViN6ukQs8nLUcI-aBf7HcOAgRt5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XDj0__H-XrdcAEfpg8fb9AjcL0e4sNx0XYLcgNU_z4jOwGG7IblbPadKDc33pRffi5iZBNHQtRD_B3BW-ZuZ_AT3otDtBHpuRMqgUKcV630E7E_WDGab0aWCStri_3JX4QLxLQ3MK7snY4OoMTUa4cZYTsfuP3AneMa3T_e0RtM2DbDHJpxOw_jyN5j4-MINAEZLYmEMciYO-Rv2JBfrL9sdBhbzOCitMJ-Jj8E5KGxjt2oR2ezuug2jtXlYOt-RBB3Q5O5ztC6hIMB6he3wc9uQEVjOSy3u0K66HZ02bGZE270nqLrQ1hQhXOQ814dmpIFtx3o-bEeo4ySvd7tsuA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دو روز تا رونمایی آیفون تاشو؛ شیائومی و هواوی از همین‌حالا رقبای قدرتمندی را آماده کرده‌اند
🔹
شیائومی ۱۸ فولد با تراشه‌ی بومی Xring O3 و رم CXMT عرضه می‌شود و ابعادی نزدیک به طراحی منتسب به آیفون تاشدنی دارد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687913" target="_blank">📅 13:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687912">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromاخبار رسمی الکام‍‍پ</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9cb7e2fb20.mp4?token=tI6bF75CPRr0zfIzUOw-2YKqiOxxR3lUa5A42pXgpjLkHOCmojrc1wn8au3_YOo3WEV9SGiAVBcIRg86N8CiMZrmTcp5QNr8q0CeFlPhW5BJu-R9qB5Vfxs0qQ_HZz-rlg1UvYPARjmqFX7E1UfroPTEBmJlKRY6j0vOE27s5g1t-tXDUOyMjZSiX57L8C1lyNlZZTGq18nsKY2W0dODeYwvr8g7KT9FXHTiy7olUkdXvgga8-SVxLHqV2CDk6GK9_jQfwGbQqGIo6e-4snD93g10coZGUYbSzBTqGphd-18ELs-oxlsgOyMrZMk3keF-e6VtpNkEijXLHbuaCfVgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9cb7e2fb20.mp4?token=tI6bF75CPRr0zfIzUOw-2YKqiOxxR3lUa5A42pXgpjLkHOCmojrc1wn8au3_YOo3WEV9SGiAVBcIRg86N8CiMZrmTcp5QNr8q0CeFlPhW5BJu-R9qB5Vfxs0qQ_HZz-rlg1UvYPARjmqFX7E1UfroPTEBmJlKRY6j0vOE27s5g1t-tXDUOyMjZSiX57L8C1lyNlZZTGq18nsKY2W0dODeYwvr8g7KT9FXHTiy7olUkdXvgga8-SVxLHqV2CDk6GK9_jQfwGbQqGIo6e-4snD93g10coZGUYbSzBTqGphd-18ELs-oxlsgOyMrZMk3keF-e6VtpNkEijXLHbuaCfVgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#توان‌تک
از ایده تا عمل برای بهتر کردن زندگی برای معلولان</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/akhbarefori/687912" target="_blank">📅 13:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687909">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">♦️
فریدالدین حداد عادل: زندگی آقا مجتبی بسیار طلبگی و ساده است/ در قم خانه آقا مجتبی ساده بود؛ کف خانه فقط موکت داشت
برادر همسر رهبر انقلاب:
🔹
زندگی آقا مجتبی بسیار طلبگی و ساده است. در قم که بودند، خانۀ ساده و وسایل محدودی داشتند. کف خانه هم تنها با موکت مفروش بود. وقتی هم که برگشتند به تهران، رفتند و در یک خانۀ ۷۰، ۸۰ متری ساکن شدند.
🔹
آقا مجتبی در علوم روز، کشاورزی، آب، روان‌شناسی و علوم شناختی مطالعات گسترده‌ای دارد و به حوزه‌هایی مانند استارتاپ‌ها و کشت‌های نوین مسلط است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/687909" target="_blank">📅 12:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687908">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromتیتر تجارت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HFbG-vP48hY7OeBUR6TMAxcUcInmUTtWKUPuVmr3wk5FynlCXjgXaIu0o6anERpUTukZ-yeHP6xLKW2OyimtE2xKiQd8q7SzvUou_94wLPW9qqF_QYy-Jij9FFgKT3qLmq2UZvI1JG3ifJZosm6OcQldunGFR_yifi0_WE0Dq_Z2IT8b4e48sm0H2g9_NvMf0tJYDT-7oyKCj0HRiuMc5KIvxfGTJOrlyaAM9-FCrEMTrX2H6Y89a_euGyHyt9FVuNVJhLGPKQ1q4f7zPq9SlZR5IROFd8APswoE1BtV0NV9V0ilnB3zv34VttVAN0iRNDEdplbgnUtpkuBO0VDt3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
#نبض_بازار
| قیمت طلا و ارز؛ امروز ۱۶ شهریور ۱۴۰۵؛ ساعت ۱۲:۳۰
🔹
بازارهای مالی امروز یک روند متفاوت و جالب را به ثبت رساندند؛ دلار در حالی که روز های گذشته را در مسیر صعود می‌گذراند، امروز کاهشی شد و به ۲۲۲ هزار‌ و ۸۰۰ تومان رسید./تیترتجارت
@Titretejarat</div>
<div class="tg-footer">👁️ 36.4K · <a href="https://t.me/akhbarefori/687908" target="_blank">📅 12:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687906">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c018ba1b33.mp4?token=oqNtjNWElxPTuHpKTOjkzX44WjWbgpbzbqSIDT66rUzAcsp-o6NkuU0467cgtOucOK5sK0WcqgfXIDA8AwRTR2fW9xl4jstY1YbrYkqH0PFxWRopzGSG_geJlo9ZUMvFAaEnRjP8VUAFJwJlPG_pT949SPHqnKG1GmVwNw0JFbvZ1RHPmCEHwFHkjGjaqpbPs2DPrKn2hdJ5a-dg2AzrXpYYlk3ErXcLWWBPKUL6qfGjAreLjNTOfERTwqtxFbGPrVDHgCazvCca0-qfKV_m7ch09mCg-1B5329jCvSiKDjOnM1qlWw9MmJni6iN_zsGE901ztzT1cIAKr-RbqOXDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c018ba1b33.mp4?token=oqNtjNWElxPTuHpKTOjkzX44WjWbgpbzbqSIDT66rUzAcsp-o6NkuU0467cgtOucOK5sK0WcqgfXIDA8AwRTR2fW9xl4jstY1YbrYkqH0PFxWRopzGSG_geJlo9ZUMvFAaEnRjP8VUAFJwJlPG_pT949SPHqnKG1GmVwNw0JFbvZ1RHPmCEHwFHkjGjaqpbPs2DPrKn2hdJ5a-dg2AzrXpYYlk3ErXcLWWBPKUL6qfGjAreLjNTOfERTwqtxFbGPrVDHgCazvCca0-qfKV_m7ch09mCg-1B5329jCvSiKDjOnM1qlWw9MmJni6iN_zsGE901ztzT1cIAKr-RbqOXDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خسروپناه، دبیر شورای عالی انقلاب فرهنگی: پدافند کوآنتومی نیاز داریم. پدافند متعارف جواب نمی‌دهد. لیزر کوآنتومی باید در دستور کار قرار گیرد/اگر ارتباطات بر اساس الگوریتم‌های پساکوانتومی وارد مخابرات شود، دشمن نمی‌تواند حمله سایبری کند
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/akhbarefori/687906" target="_blank">📅 12:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687896">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو فوری</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/diUrb4S2hvHR9CV1FxocVIXSeG8ax9iFJ9BTlSFMx5aM3ZZSZYccTjhVe1rso1WugpIsTTS9zSqhs_Oz2TpEUV8FUsNB7QX5eJxirS0b7L-T7O1aFUshW1oJfdTjg-qgsXoMHwxee5lTMHeNpd4STfzTKh1UX7dARmOkUa8i1gzPhl2pZRZIFmlz4YjcZ9eYGyEvnUn9XV91_MBp2gWyKnM5JYd6Nca10Y2pkWt8mGZH7ZYhd_s6QKHXPUNFvHB0vw_2BaLMd-i8Gen5fKBJCefQFTPv4gl1Z4RdNyuKtYB0hklG7jhnOsnp4YgfaN7Y0HLFo4_GK3Yh4pc2cjiADw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Hl1nLtGNljZruhR3vjOdlwJs7sNqr5cg6-kfb88pYU1-oahTG0Fb4AqC868SISBsdAUkKHMl1k_hOlPyBJockzLn9FhRRxyorwu9anJ63KfMtD-EB4PAxy0Mn8OliLXcK4dx948Gu6PRhjFGQZVX_bnXIpiFvMczYaIysiZ39ETPKGy43SzyKxY62dc78PHXp01xxqbojcDhrK7zon4uuC2kcNbTh6WlRot6PhzdOj_4xEAWhwvipIkky6eWBhS5AXZODyu66ZWwFKs74q1L2dVKzv6-iV71ksG38UjpIymG2pFHpGp2hMz5p63oqhj7Ceu-cOQJJGVolfvQBaKREw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oviYj2WNp9htUYV07PWsyakxGyIrgmqySD5gwuRFJRQdfOSMaXOkxNU1m6lfilIYRdjmc309NSw_HcM1WvgapwGYkzULqUPKKEIIicZta_uFE65KTJI1HjjxTv5J7m9dBCZuApgmiHMmhSrdSCgtI8zHzCTcTpd3XlFO5e84aPeGNuqKXlM99ihHnyjKzf7JXN0E4DLfw6SpsIN0LXET-g-wOz449pidfQcfI7tD7aG5F-gSBcWHWd8oIjzsueQPwEFuRUdfD243JwLShjjjW4HMN0_XBUESSVzmthnd-Zf58B12vKYAxrVfsWM1f8gXmdSRTCVMS6TNcIUjTGahDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tXjisr6sqLARNIWXWmbGsSDskiUjT3-kw4DQrctN5p7xYxvoYI91hbJhz-yUMAdQkgmTVG9DVUD-tm-PwiJunZHHFD12WpmxIXphK1Crsy-44Cdt6TgRPTVYoDkwuZfdsm0YLBNd_0EymTMmi-9EGGC_LuUEnwQtfNTLg0TzLuX1XFVYOILcmHApa4lXUEYsW8hrCr8O9D5NkpsTll7_-pns-A8q1Rj6oiI90O3i4IRJiY1P2vekPJ6grzZ0KzbeMazHNegQbbV4o1LU83Kf5L_sX3KAQKKfyR8gS_Va9gaQaUbm3gIQfcAO1_-QXRkmx1Xtc3kaMfSGL0DsSUTWCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/v-tLNnoOW6UyeKcwKiU5iPIRLRIwbJF7hPRzafzTwyNL80u9HHORuygBfGDWBYgWMpxNBnxynSrA2SSs2IE1YvXA8RBbddXQGl4U0wTaQJ_AoBtL6NUTU4E_m4hBGI_wB304rsZRBH8G_K34SM7FG4PSWdmg5oTlvg6ckJk7O5IImy7IoN0xIs6vPrmg3Asi8dHN8G9vGmkWuFT0ZvuPmsGMrRu_SECInFft4JDJF6dyHquZKBIv50WqI0uHEFsZ77EGUu70-6jcgamuh1CIc3bID46bWZWrrDRY8cE4EhaNIppRHot_28Yc5ceLVz6f_uNOazBWnAgAZNC2lOQOnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vucoD74p-DXDreKMNGDTYUngqZsYFa1eV4ue_Uq7JoW3_qG13EV6lfBv4YgO3XE_nh9zDKrxmLQUY-U2DFz0rF8YwvZt3Q2g59Q8GR9paaYG-odWrfKOwpZkAj22TvoF1vgSfnFnx66nRkgpHCgS7hEbcmO7V3CZESDl4hdVMgKIdtvqHOogTfy2zFWvS-TICIDAvXFurni6QhODQxmFO5A83yHxgywPkoyT9TnsuvGJorNMlRQCa9uX5YiX0lkuPGQCpW_hz4QlI_bx_3CRtHKOfyNsaNZzOdqEmURinqOidlw2ZbqDAFaqeDuoA_BENeJnfaRspOKfggIZEuwJqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WKqNrdJFBYcYLlePgy2IlKX9nY-pPpVNwaxL4VxdCq-oa4f0gvWSEOEerfJIn8ropy8GFjXDzM47SyDfTTPEtxJB_b9tTiy1BkN5L4rK8QR7tM4cxStVPWW7Ia0vHhKxyW5hM6h6t6wqQzXJFsnjsXqj5qpMb81R1AQ4sBbgzitR8vA1AsA36DqkIPLAa88_UivNjWFSVwUFSw1f2Ku_oiNjjYL4ER8bQFnDu40eIGYFZoucKqC58Pe7mi0Jbf2_P9_BcPKm_JcBon6PqBrVwRFP0xmyOsD8Z5K4VM-tMYtdBVqrxAxnNqsE0PBLmImj84vJCgoe3nqc67S7K1M2fA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jpXndGgMSjsehrg4ukoVQ_R0uVLdkzzLrpXqSCAscSXPTyq3Xw8ofK98SGADPpUOmBN9ov514C5rA9M1w6JQgcxsQbDUJKMNZeGTRpJpujYNO3g4uO_N5mKgVHkHvc2lMtiAhUK9k8hnXGUQeF2_TznMXvD87fBis5QvLUfiqsPSzbqWHa_SD0w2EmNAEr1J52LJjbMFH9KpaKXl_FVU9QClQGvMnMBTyEWpvz6ez5lmWYpMAengefQuSvVD-2hU-1CLLOu_uz0_bo3-i7J-OD9FyM-Dh9umlWxs1FveOrW39DPLOxopjZXjpTKcfdNjCowGmK2nsfMxNHQEE3szgQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o8vuSxtMeagRDTaN3xeAQTPyvwoVCPj_Fab8bZkEwB-tRXwLBzBtjTVirksHIc-WIA2K2cmbEyeFhXi92cg1847E5sn2pMHHfyWlxVkOHYI0in8Vi83qqoa9bFT3axR_2sdOuetUVKtaFZXS5Nakw69023uYSAR1okF2uNveHSH_hlnxuva_rxgkTm4rVfoWHt0b2d_At8WXhG2d3uKEtxhSaOJUEr5_t8VQJ1pwG6l-v_wn-n1s9FCRrANHKAJswAn155iDrEc0bFgKLu62LcFXX6yMupp98Fu7WZJUgbcapobrHGuswmjqedhN7uFsGjOFaRgdd-P2dp_mZ6PdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hUtSiv6dSJP3yfbWjqnJrjvFYeUW1LM5hWO1E7yIHd20aEW0aZuy3nMKcoAQ5DQAoI4hlurK7-_m0iMXETB6J48Z3XXNlEMnmgfNV7Z2-L2rgt-CJADyLD9zHBWYhfTJrWdJRZvvhMLN8dILcF0QbqfxwQY7uwTer26H7PLvgyD1CUdBWg88wQgCr5OahegcfI-n13puLZlyRN3-kS6SuhFZ5m-nj3wR9zn608_k1w5Rlv5S0WRNKdrCi_OsV6oSNib7A_WbV1AeKI0o3HhH7lbviAS5uMqSZCpV20b9xHHTEOkz1t7BXMl0t5RVWN0Iaqk-WtWW5JvOIlKnKhLAwA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
چالش‌های شروع سال تحصیلی
🔹
بازتاب دغدغه‌ها و مشکلات شما مخاطبین عزیز برای شروع سال تحصیلی جدید
🔸
روایت خود را در قالب ویس (حداکثر ۳۰ ثانیه) یا متن کوتاه  ، همراه با نام و شهر به آیدی زیر ارسال کنید
👇
@Ertebat_baforii
@Alo_fori</div>
<div class="tg-footer">👁️ 38.1K · <a href="https://t.me/akhbarefori/687896" target="_blank">📅 12:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687893">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Vix8vp-v_4Qh-_7HX84lk11ynf7JN7fmr51blP5vHY7Ahqgo3ktIKV9TJqLl7OD7jtMT6Izt9cR_6wNg-T5CFahis1hzjW1u6UowX6HG8RA6tahSl0zEpN1WahhFq1UujFNniP-_kZypLL6HLPeQjXuTZFpGNFsRLaaNPeT4VgqyfQzlBQ5mM11K-104b3BruBbbBGm2mi9pjAp0OcW7TvhcrVtoY97J8RdUs-eDgJA7l6rUKtIu-50Wes29H-TeRZidm1qL1eyD2c-TIgcLa1bz9gUG3hRyyGMAaU-R2PAtoNgxjLNerizEdfBcVa-aID2HVNWRHjb1hNrxYEeDzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p-laoC2gHSBi95f0PCLySQeBaS70uiKPtP5itA1pzVGm5Pa1Oo4Q6CeggdskSGibB2-Y6tf21fVHJYpidM0NPRnvvnN4e3xiCRS09lnFghBmUncdzdwsckMiOhLUR1GS-ZvKQ-DMvg7UVbhCYZfYOTSCa2dchVKO-v1Vy_b8toIrVURx5rKWNbvlYHlyEQ1fd1Pt0tXy5mjRyubu2Soz2vAxsZG7ODlCapOm5625ka1KjlUoFGweBn3fQVLQ0ebVWr13tWJ8sS24TmAZnO2D5RkDDijRfOYtkwa2lx4QhJ0DSs_5stIGamK7OyN40mvV0S-Br8K_jVYuxw9zjfrrGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ac8da80b1.mp4?token=ocQqps7ZXYA9En6tE2M0AhVYDaRPBVDzzc_lkfPRGVBHtKsDwfSkOhraYDKXuf5ap6MGo57p2wi2m7ycakhVDIJvT-50hwFtbf78vngCfpN8s7uYohK7BUSYNw7Ifx02ML-6tzp9BNaDK-FvlXHxq1zFQ3GgCvhtFTlUUnEJUUQceXJyVXX7WmvssHkSO-W2INkkzNPl-lTqPEAWHgQDimQ-wlUvy3oOXXCFJLhZIlye3HfsAT-3n7CEVzw7WKHSCM0tHICYqM6WYFm2in_vFToaaa9FXWlkIq8Mqe0-hnXh09vIxhqO4xf9dbcclUtUaX92a7xv4tde9yAeteLhgQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ac8da80b1.mp4?token=ocQqps7ZXYA9En6tE2M0AhVYDaRPBVDzzc_lkfPRGVBHtKsDwfSkOhraYDKXuf5ap6MGo57p2wi2m7ycakhVDIJvT-50hwFtbf78vngCfpN8s7uYohK7BUSYNw7Ifx02ML-6tzp9BNaDK-FvlXHxq1zFQ3GgCvhtFTlUUnEJUUQceXJyVXX7WmvssHkSO-W2INkkzNPl-lTqPEAWHgQDimQ-wlUvy3oOXXCFJLhZIlye3HfsAT-3n7CEVzw7WKHSCM0tHICYqM6WYFm2in_vFToaaa9FXWlkIq8Mqe0-hnXh09vIxhqO4xf9dbcclUtUaX92a7xv4tde9yAeteLhgQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👕
از یک تیشرت ساده تا یک کسب‌وکار خانگی
🔹
کمپین
#چرخ_زندگی
تلاش می‌کنیم کسب‌وکارهایی را معرفی کنیم که با سرمایه کم، امکان شروع دارند و می‌توانند به تقویت اقتصاد خانواده‌ها، به‌خصوص برای بانوان، کمک کنند.
🔹
این بار سراغ چاپ طرح روی تیشرت رفتیم؛ ایده‌ای ساده برای تبدیل تیشرت‌های خام به محصولی جذاب و قابل‌فروش.
🔹
با خرید تیشرت و مواد اولیه به‌صورت عمده و تعداد بالا، می‌توان هزینه تمام‌شده را کاهش داد و در نهایت سود بیشتری به دست آورد.
#چرخ_زندگی
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687893" target="_blank">📅 12:27 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687892">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">♦️
سخنگوی سازمان غذا و دارو: یک میلیون دز واکسن آنفلوآنزا از چین و روسیه وارد می‌شود
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.3K · <a href="https://t.me/akhbarefori/687892" target="_blank">📅 12:22 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687891">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MeP7ycf-TkGf5-cNoywmp2Ce3L2WkfUCKvVKuvrkg6jqm4j6N8n1IZZHhG30jotx7svYhrA7iS-LRPwf44Mmc01SDyUNjD41q5htJmHx_g7FxDkh9x7JKplMA3Go00EBpgwFnh8uwLCQspR-WwosJDjL_76OmgiqM7WQ3dDLJ6m4MSKJXqb_1TB-t-05E2PnxgpilNB_KsVML6O_0x0CE9lnDYppFPnXhE4pyv4I_AUFuDphoKzy1HqtvHtkUA6RlLwAHV3rKBUxQGAaZ1RODJhIQunCkY_ys-BLkssVTFVOnKiPR6g23VkEyZfwP65f0-URlfUS0EoXwWKrd7OtmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
۵۰
درصد مخازن سدهای کشور خالی است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.7K · <a href="https://t.me/akhbarefori/687891" target="_blank">📅 12:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687889">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromدمـاتجهيــــز | Damatajhiz</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=mJuos7AyY2J4oOgWDKEyHHKIjXL08Zf1JpvSOn2F386mfqr-UO-yFwx_1Tn019WD24dDSkbWWkPWyKO7fzmTl-wZlnpMJS7QxJPBZvPkGAiDCcSQe_iODVZ5fR8oyRpkML9E_IaFOGLmP_Ij2RP1hl5a3UwtjJUTp1tXszePUe-x7kPd0Z6WPgWC3nYmHPXNHYlZ_LhSr0D1a3TTV8goM86cHFLFDhDGytUzRs438eyyoPMM2ChAE3uWXK8-t757w8KMbKjkKIncwhDzbix4PhCl7x0Wai4VUltI4d0ux2ro8VKyCukVleSBk_Mjq7mlXuh77Z53gjjzp8yx59t0Tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d57d3af292.mp4?token=mJuos7AyY2J4oOgWDKEyHHKIjXL08Zf1JpvSOn2F386mfqr-UO-yFwx_1Tn019WD24dDSkbWWkPWyKO7fzmTl-wZlnpMJS7QxJPBZvPkGAiDCcSQe_iODVZ5fR8oyRpkML9E_IaFOGLmP_Ij2RP1hl5a3UwtjJUTp1tXszePUe-x7kPd0Z6WPgWC3nYmHPXNHYlZ_LhSr0D1a3TTV8goM86cHFLFDhDGytUzRs438eyyoPMM2ChAE3uWXK8-t757w8KMbKjkKIncwhDzbix4PhCl7x0Wai4VUltI4d0ux2ro8VKyCukVleSBk_Mjq7mlXuh77Z53gjjzp8yx59t0Tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥇
دمـاتجهيــز؛
انتخـاب ،قیمت ،تامین و تولیـد
تجهیـزات تهویـه و تاسیسـات با
اصالت
گارانتی
(از سـال ۱۳۸۳)
داكت اسپليت
+
ارسال رایگان تهران
كولرگـازي واسپليت
+
نصب رایگان
👌
فن كويل و تجهيزات كنترل
🏊‍♀️
استخــر، سونـا و جكـوزي
🔥
دیگ و تجهيزات موتورخانـه
☕️
تخفيف ويژه
دمـاتجهيـز تا
15%
- انــواع ايـرواشـر
- بـرج خنـك كننـده
- چيلـر و ميني چيـلـر
- زنت آپارتماني و صنعتي
- هواسـاز آپارتماني وصنعتي
🌎
www.DamaTajhiz.com
☕️
☕️
🙏
☕️
☕️
021-88822550 خط ويـژه
Join
🆔
@dama_tajhiz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/akhbarefori/687889" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687888">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=Lr8ZXAmcGkUJxZ_Giqz-eyDXsBGNbtYtWAlEYSboE7b3EMW7wooWUrtZoo8IJE8TYkfVUXd0RrysKDfVqHYxblaHfILF4DDeg3PceAQQuWcvNjuFM0Lnn7knHnPvq0qJckRUiE2Hj7qQ2Msf2Wu8a5F8UKvi3KVB_PVKJfGAiaj2_S3jE_GDympRI1lT-oeNT2C_oVGKf6upmHh0a4wnAD1EMfHPGzNbq4lOSlhkMxwAiHvrCDTh58LuR9-Z459FiUOMxs-lfMCFILu4lnAZyR7iKp0BnTdDf9InHRpFVuUrwMl9HcxC7BudwHf5BxUo6ut5TZeiGloSANYiSewbuA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/569f2c20bd.mp4?token=Lr8ZXAmcGkUJxZ_Giqz-eyDXsBGNbtYtWAlEYSboE7b3EMW7wooWUrtZoo8IJE8TYkfVUXd0RrysKDfVqHYxblaHfILF4DDeg3PceAQQuWcvNjuFM0Lnn7knHnPvq0qJckRUiE2Hj7qQ2Msf2Wu8a5F8UKvi3KVB_PVKJfGAiaj2_S3jE_GDympRI1lT-oeNT2C_oVGKf6upmHh0a4wnAD1EMfHPGzNbq4lOSlhkMxwAiHvrCDTh58LuR9-Z459FiUOMxs-lfMCFILu4lnAZyR7iKp0BnTdDf9InHRpFVuUrwMl9HcxC7BudwHf5BxUo6ut5TZeiGloSANYiSewbuA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚗
🧹
جارو شارژی خودرو با مکش ۴۵۰۰Pa
سبک، کم‌حجم و شارژی با ۲۰–۲۵ دقیقه کارکرد!
⚡️
🔥
قیمت ویژه امروز: 1,089,000 تومان
🏠
پرداخت درب منزل
🛒
خرید
👇
memarket24.ir/product/brief/26903/180124/
✨
تخفیف آخر ماه؛ فرصت آخر!
https://l.memarket.me/lp/65/180124</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/akhbarefori/687888" target="_blank">📅 12:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687887">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2e5fc067d.mp4?token=qPRwaqi3qE3MDRYxnLIrfOs2RBSTbqnFhQTfJB7uQ8V4f3Y-BPfmVsWl58DEBSBfxawGnz1Z2LyN6ilQQQKTQA7KaMgGWyyIK-NbTHfIZ3rUajassY3PB735WrPo7AVbBt7rkzDM-2jDbVGbX9Bx8sXeh-f6MPA4Q-WUvHmyObrBambW8l6RnjyhE5H6hI-I5g_6Dye-WlrQReRGcrN4t1_cUqPXjrM5Thv3Ouwiuzo4CHYvtvqv5QHWMD_tPfgguD6ALwtNaSVacTN-NmtUawlJz7ky-gEd7_0vIBO_nv_YYwFf1wYF76MUYdhTQDcKr4F_aLhKwA-Erj-jj-dvRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2e5fc067d.mp4?token=qPRwaqi3qE3MDRYxnLIrfOs2RBSTbqnFhQTfJB7uQ8V4f3Y-BPfmVsWl58DEBSBfxawGnz1Z2LyN6ilQQQKTQA7KaMgGWyyIK-NbTHfIZ3rUajassY3PB735WrPo7AVbBt7rkzDM-2jDbVGbX9Bx8sXeh-f6MPA4Q-WUvHmyObrBambW8l6RnjyhE5H6hI-I5g_6Dye-WlrQReRGcrN4t1_cUqPXjrM5Thv3Ouwiuzo4CHYvtvqv5QHWMD_tPfgguD6ALwtNaSVacTN-NmtUawlJz7ky-gEd7_0vIBO_nv_YYwFf1wYF76MUYdhTQDcKr4F_aLhKwA-Erj-jj-dvRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
حمله غیرمنتظره عقاب به یک مامور پلیس در بازی‌های جهانی عشایری در قرقیزستان
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/687887" target="_blank">📅 12:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687886">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/162214e774.mp4?token=TZzIV4m0-9os1mUdtJU9TOFiQRx5osQbA33QX9RZoR7iP-XdawROYKcWdMsXscqp891yOLj27HlqaOcTwk0r5w3lpPM51JBKCE5K_231EWjoN2vOPPFALLf79gY7-VgJPv8ZGqRGRdKLdt7TUWY-im58n-dzWWE7W0dpUFlAPAUT45gZi0EunvILIhkfAPmZBzd49eVwexdRjsbCeLwpyQZ7hiw3Fq1BmcZGEu9buYYSuqTlESOx3rMsW9VbzVAdlJtNPa5k7tzF-_0cgPeLcaGA8Awp0LouGeMVstonnle1ebyomi2Oi20-tNKSJkr2ADDl-_arle1km0w8k24hxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/162214e774.mp4?token=TZzIV4m0-9os1mUdtJU9TOFiQRx5osQbA33QX9RZoR7iP-XdawROYKcWdMsXscqp891yOLj27HlqaOcTwk0r5w3lpPM51JBKCE5K_231EWjoN2vOPPFALLf79gY7-VgJPv8ZGqRGRdKLdt7TUWY-im58n-dzWWE7W0dpUFlAPAUT45gZi0EunvILIhkfAPmZBzd49eVwexdRjsbCeLwpyQZ7hiw3Fq1BmcZGEu9buYYSuqTlESOx3rMsW9VbzVAdlJtNPa5k7tzF-_0cgPeLcaGA8Awp0LouGeMVstonnle1ebyomi2Oi20-tNKSJkr2ADDl-_arle1km0w8k24hxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
برای سرزمینی که هر گوشه‌اش یک خاطره‌ست…
❤️
🇮🇷
#همه_باهم_برای_ایران
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/akhbarefori/687886" target="_blank">📅 12:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687879">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TiCjh94rnB6iiABzuPigPsXvKZ1WGY6MjduqvrHgCh3RPqKexCnF8hSA6Un7RtnT5XVKLv8_oYcFQejnnZURYow91ulgguLrmaOzwQIns8xAyGGQMJxs7EYO36fq0syp7ELkuE0XJlJXj8Qmr5gZl9hAyrZ4siHKcyZCxiXsyrpLGjaooJG4MGs3S9koqiCqYUIONJseKqP6SYuZmxiThLjBiXLvdAgODq4AVuwahHnoqh4eYh1Jiaorj-lxlqry2BoNXRuR9lycIJCRC3d-_d8p6dbTGxL6L0Lj2A-pc8Ye8PIpqMiCRB87VTcC8PUrN4Yc-OiqWBRjcgB-BpOqSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X8Go6dVwyzXw9TqrtErdyo5mSmLqonDl6U-bRgkKqzxk8Vm8WK-nDbWRbBwZehgFiRpulFEGqBsXibIZYrbl6fOl7GKbk4gs1SfDY_b4MtG4VGsdACZSTZglEpuHDEA-X09UELpulA3ZlZeWAY_YRLuKajMrizfFKp5foDGnKuxG4f9qmhS2PNV1n53ZdVMartZGmd3qZr13aCxjXSKYRUwloHwg0yg1GOOZ6JaSXlZgW5mLdjok58MbvAQ_ToTMDamorA7k4QjHiZMTs4kvfqS-3Zg8b_lBEOiQCELgnIenWb11OkE5rkgBVnKGpaynpjEUqoWbzYlSBywH2Qs10A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/h7o0QOGweqq45kH5lcDVLzjJUq9NWce2lrx2k-7zY5LmDXaHg5GMtoGdATQ3_GWS726OznUkcM6NYwd53MkZlUWELu2JJLrsdMBQZ6uGDIocU1xvTgj2ODMGCiNprqboMRRZkZEm38Bm5naALT9Sta5xDhCmpAVka4NUlTRvyrIfFNoiPsPxT6DFkZ4hmOdSd7ChroEbGrcCESGqakdOH0DwykB6DRy1IF0aJIqHMg8ZGgO8AzNoiQkJW_mJLC4AGUuy0guA4Hts7_4ojSEUW1XcDS5P-d_4cX1aCH2SVJLopyyyQ7rkBAcuyxw_zi4Nl60iSTxXxyKnfD_y1BSACg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/tiZT5yL3fs7h7inzTCHmnBvrEkoLLY1-22vdg9MaM8ebFm_2P0UXbyuzsUwQZEwtKFbfvu3sARuc5oCFjJINRGOihlUvfmGSSjw6VD--JW0oN927aEdDMgSlU8yngePidtiufxcUBTKsY6gWz4oi2jW7T8ZOaGbx-Uwofub2KKm5aExLMJJU_giOwuJP48aztKNzEoOy8gd1zZCBpbJubBwLXyeMZN9Eq6zSiZofPKtHXB4YHt74a9aVePlHS8RToR3IGFS5PS0v6ivqtNMHF9Q8r7ivBiNjC2AzcUkXcnk0vFslFJTba1ZUML1AkKOTgMUbAd0Ajnx5PPwC2YwXeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DXX7o4439w3SZTfU1gCSAeiNDCQOShVXHwWNZJOjamAESTZ-o-CKESj5TdDAD4UEKtZVTPIlhNRrg7-McB7PVXYUZeUqE2_JGiQAul9nHTkc-lq1-ZcDve1PBBreScwPN8jBB7yUDYpS4_SGF1oAI-ZTS8hzKV-fu7PyaZGQ0jousOJs8MCmSowWyNCHbV9VW4VrMXFo43PMJdALSPl5L80faY2E_dtRGj63WfhQ-WzFPh0MLnatxjAmtiCW9o8xFNKbdAzrGifW5kLmpfScyU66cqpdUTeHh9qxCiDCfb-TLMoEYP8L583xef1BbafWfieJ2tOUqWO3gV8M8LzyLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mDPBB1oMz9-6I172H1e7W6rOCus3LZWibSa8hVe9E6CR4FUd0cwOYLozN13KfqfUSKI33t7Hw4fjR0ISk9W_QNbvkaXeFuu6nkuOJykmyJSl8hWI1xSPTYudlDpetZWGScHtH57mxU-HJjV1ECzAjMXTGI6TKoMOxF0ByguAlhnvrRrYR-jVxMsB5zPT7fVoO_dHdrTbMljUGxPRItXA7zYoghAjMa06L4YjVdMpA71QjwgI3mIYbMsJf0sARYasrY817JJ1aqM7jZgQEhwqN2Y4NvR4Njd6bi-t9SYT-Ahq51bnSxJYUtEaImig-SSdUgoAF1vvHZD076Bs-p2Few.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LE8Y6-MI8yS-vrDwlCSd-IKfc4DJmxqY-9umZSGbCxn6LBWYZtKL4vFzFsTxawzwwkF9ddbNELeeIqXflySKTj1r3Tryo6VqPS2w3_XaLYKasTVU_VAvoEC9GrBzKONZyxBvnpScjvHv1NCfa8WpkNV0SIZlLFuEjwu0nCPLSOKzTHg04e7ZkZlx8nbMV-00n-8sByjSNr4-fCdiD-4tPNt_-lewLBozD9eiogrXqJoNlikqdCHsFJqP3IeZFXmIippZGCoBJCLWgFegyeYlWpGjeralp0dLifusgIatSkqA32hO9rcTxzpFZTdrXK26TdRLNPDZx1f0Z5OVdL8Oyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
باورش سخته اما هیچ خواهر‌ و برادری، پدر و‌ مادر یکسان ندارند #سلامت_روان
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 35.1K · <a href="https://t.me/akhbarefori/687879" target="_blank">📅 12:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687878">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">♦️
بقائی: هیئت قطری دیروز در تهران حضور داشت و برای کمک به کاهش تنش‌ها دیدارهای خوبی با آقای عراقچی داشتند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 34.2K · <a href="https://t.me/akhbarefori/687878" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687877">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SJ9_vtd3H_Vp4GqnY83iO5HyfSunz-fEUHUBsrKFkRe_EtkcA8z5aPJ5AEDBDK7ZA7SI89Jtc3qVKv3bthdpUblP1wWBzIWO_L3NtOUj2-MMSwN9zN3lM_hPc5bjxVOZqHvb7prOA80juw0TjbSvR7SqkwbM72rdASLpE2s2BNeP1n9yK_go8ZP-8oJAI2FTktSqimcoKCXxgoGBuIWqqgEkxui-nf_1A4FLJSLbOdcMKkziS4RoHw1U9Hsqniu77CZni5WD3FbOvAVXLHD5UwKWiSy7uH2F4v6ZRfTznNXzHawDcjWYerAzv8RjcrHrK_JIRCQq8LDPOrshQjl8SA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
موافقتنامه ترانزیتی و حمل‌ و نقلی ایران و عراق؛ فرصتی برای توسعه همکاری‌ها و بازارهای هدف تجاری
🔹
مدیرکل دفتر ترانزیت و حمل‌و‌نقل بین‌المللی سازمان راهداری و حمل‌ونقل جاده‌ای از انعقاد موافقتنامه حمل‌ونقل بین‌المللی جاده‌ای کالا بین ایران و عراق با هدف توسعه همکاری‌های تجاری و گسترش بازارهای هدف خبر داد.
🔹
سیدحسین حسینی گفت: تسهیل فرآیند ترانزیت و‌ تجارت، هدایت فعالیت‌های حمل‌ونقلی در جهت رویه‌های بین‌المللی و انتقال کالا از قلمرو دو‌ کشور به سمت کشورهای ثالث از مزایای اجرای این موافقتنامه است.
‌
🔗
لینک خبر:
https://www.rmto.ir/s/mfaonQz
‌
#سازمان_راهداری_و_حمل_و_نقل_جاده‌ای
🌐
rmto.ir
🌐
141.ir
🌐
https://ble.ir/141_bot
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.5K · <a href="https://t.me/akhbarefori/687877" target="_blank">📅 11:57 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687876">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mVSiT44HnYAGaqbU0HxKydU2SV5lVcZw23n8jpDKOI8-pyvTGObxb-r8H_8dxWuVy2pqOW8SD_GdSX7oAwvuoeiRjHv4FYOn-7U_UaH8JkpxLl9hWOLs_-N2OXYTvCGoWBVjJsARBt6AkwvOi5_nC0IROIIZPreZKtLIcMXyL01IGbyUvbSo0Rv2xh0N1WnACn4T5AMtjmAldihKlUt_cjX7fjqPadEIZG8bl72zwVkJAuIQjuAZ5RxzmVjIdYQdcMhb2s1SrCXcht5Px7Hvf5RldOThSgRp4KwakM8UjZwWSTP9oXvQbrla0fXr8bw2_GAiTnYYLVN188A1BfQVIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
هشدار قالیباف به واشنگتن: پاسخ، فراتر از انتظار خواهد بود
رئیس مجلس:
🔹
ساده و قابل‌ فهم است: زنجیرهٔ تولید نفت و گاز در این منطقه گسترده و پراکنده، در دسترس، و آسیب‌پذیر است. شرکت‌های نفتی و گازی آمریکایی که در این آب‌ها و تأسیسات فعالیت می‌کنند نیز همینقدر آسیب‌پذیر هستند.
🔹
اگر به دارایی‌های ما حمله کنید، مورد حمله قرار خواهید گرفت. ما این توانایی را قبلاً ثابت کرده‌ایم. از پایگاه‌های نظامی‌تان که غیرعملیاتی شده‌اند، بپرسید.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 35.6K · <a href="https://t.me/akhbarefori/687876" target="_blank">📅 11:55 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687875">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb01cf1796.mp4?token=awpXvvwM-RRr2lxgXo5VDYlI5NyzuX9QIX0W9XMSKTDYAwJ_q4Ke7YGzAtoxIbwpm9N5f_DOuCmPw9LRknrYxKctTIyIH7esbDGeg8N-q_lXCfWcwYBsVMQSW3NIeIIKPAWYqYvA6uZT-qvlvTmkX1sHmvmpOIZ6DWch0890-qs71waWAnQYqBrmBkPg5DnvONYaQXzxx2TsbNL-JhZi_wqUwwarXIFTZlfAGa4fHt_3igP73ZtsXt765fxwFJF1eq4QofAImCJ_J9JZ1CRcG4w0fb5VTiQMfExXauzkovUkne4lI_BYVykyDq8RNrv5pXo-r2oq_oDd5tyRglouLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb01cf1796.mp4?token=awpXvvwM-RRr2lxgXo5VDYlI5NyzuX9QIX0W9XMSKTDYAwJ_q4Ke7YGzAtoxIbwpm9N5f_DOuCmPw9LRknrYxKctTIyIH7esbDGeg8N-q_lXCfWcwYBsVMQSW3NIeIIKPAWYqYvA6uZT-qvlvTmkX1sHmvmpOIZ6DWch0890-qs71waWAnQYqBrmBkPg5DnvONYaQXzxx2TsbNL-JhZi_wqUwwarXIFTZlfAGa4fHt_3igP73ZtsXt765fxwFJF1eq4QofAImCJ_J9JZ1CRcG4w0fb5VTiQMfExXauzkovUkne4lI_BYVykyDq8RNrv5pXo-r2oq_oDd5tyRglouLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
وزارت اطلاعات؛ انهدام ۳ هسته‌ی عملیاتی گروهک تروریستی-تکفیری با دستگیری ۹ تروریست و به هلاکت رسیدن ۳ تن از آنان در جنوب شرق کشور
#اخبار_سیستان_و_بلوچستان
در فضای مجازی
👇
@Akhbar_sob</div>
<div class="tg-footer">👁️ 35.4K · <a href="https://t.me/akhbarefori/687875" target="_blank">📅 11:53 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687874">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/noHyjEUFmfuF8XahyKl26ltQuCMcS7m4OnaVxcLh20zwR9WXds-lGpZKIFpEY4b-EMB-Y-DG6iYt0uYdgTp01sStkSDA9895yzx76xbYQeS2czBD6B5zj-yOIP9vGwISHEx6mJVh163kUksEbpg0Gwm3dbP69MRh89v8bekJCVzsUuiLkk9dvRR76GfaJGhN9yEJzSWyEgKyhFb4nYi9ieU48cKOq9VqkmWamwRlNRcq6s_XqK6OA3IAd1UYj-KPyBOq0c-kwvQVB-slHUcCwfBHsz15WUzaOGxFQsKH4IqQhw3flLIaumqpCX8-PHVVDzXJxeW88g3Rka8jV9yUlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
نفتکش تحت حمایت آمریکا هم برگشت خورد
🔹
نفتکش TITAN HARMONY صبح امروز هنگام نزدیک‌شدن به کریدور جنوبی تنگهٔ هرمز مسیر خود را تغییر داد و به‌سمت جنوب بازگشت.
🔹
این تغییر مسیر درحالی رخ داده که قبل از آن نیروی دریایی آمریکا درحال پشتیبانی از عبور این نفتکش در مسیر جنوبی تنگهٔ هرمز بود.
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.5K · <a href="https://t.me/akhbarefori/687874" target="_blank">📅 11:40 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687873">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87a8d94677.mp4?token=Esb9PZ8iAPQB1urXCzY8YG1exeWlSJQCL2XRGJnzoPkCsO9EeAvS9BcVKfGAm75hKK_y3idG8Lvxvyz8U3TPaKI3diYxFIZgCnpaz05do9hBI_Xd7YC4XqdnG7qcJR3DPjSu8b0GKMYUhvNINLC68AQNIJJf-lVBlSZOr6otSF9CzgTdey60vb3zv_u-ZztQy1_fly9n5YQrUwzmvm8gsMeU0m0_79yBlxkwiGJ9j3URwDGva3opNi4K809OfLSCihpsVKIGKtXOVnN6VEh3VyatfDKCUkt_Mf9rfZ87c9TgyqQrof-Zueuk30_OFx_yfMtim3IozBJvOtB6ge_2jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87a8d94677.mp4?token=Esb9PZ8iAPQB1urXCzY8YG1exeWlSJQCL2XRGJnzoPkCsO9EeAvS9BcVKfGAm75hKK_y3idG8Lvxvyz8U3TPaKI3diYxFIZgCnpaz05do9hBI_Xd7YC4XqdnG7qcJR3DPjSu8b0GKMYUhvNINLC68AQNIJJf-lVBlSZOr6otSF9CzgTdey60vb3zv_u-ZztQy1_fly9n5YQrUwzmvm8gsMeU0m0_79yBlxkwiGJ9j3URwDGva3opNi4K809OfLSCihpsVKIGKtXOVnN6VEh3VyatfDKCUkt_Mf9rfZ87c9TgyqQrof-Zueuk30_OFx_yfMtim3IozBJvOtB6ge_2jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
گریزمان در حال مبارزه برای زنده ماندن؛ وضعیت ستاره فرانسوی در هنگام کولینگ بریک به سوژه رسانه ها بدل شده است
🔹
در هنگام برگزاری دیدار اورلاندو و سن‌دیگو رطوبت هوا در فلوریدا، بین ۷۰ تا ۷۵ درصد و دمای هوا تا ۳۴ درجه گزارش شده که باعث به وجود آمدن شرایط سخت برای بازیکنان شد.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/akhbarefori/687873" target="_blank">📅 11:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687872">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">♦️
«مرد هزارچهره سینما»، ۴۰ روز از رفتنش می‌گذرد، اما سال‌هاست که در قاب خاطرات ما ماندگار شده و نامش با سینمای ایران گره خورده است
🔹
در شبِ ماندگاری که با میزبانی «محمود خاضعین» برگزار شد، اهالی فرهنگ و هنر دور هم جمع شدند تا یاد و خاطره سلطان کمدی ایران اکبر عبدی، این هنرمند تکرارنشدنی را گرامی بدارند. شبی که با رونمایی از تندیس او و مرورِ هنرمندیِ بی‌نظیرش، دوباره ثابت کرد که هنرمندان بزرگ هرگز نمی‌روند؛ آن‌ها در آثاری که برایمان به جا گذاشته‌اند، همواره زنده‌اند.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687872" target="_blank">📅 11:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687870">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromآمارفکت</strong></div>
<div class="tg-poll">
<h4>📊 به نظر شما مهم‌ترین عامل در ناکارآمدی حمل‌ونقل عمومی در شهرهای بزرگ چیست؟</h4>
<ul>
<li>✓ فرسودگی ناوگان</li>
<li>✓ کمبود ناوگان</li>
<li>✓ عدم پوشش تمام مناطق</li>
<li>✓ ضعف مدیریت و زمان‌بندی</li>
<li>✓ سایر موارد</li>
</ul>
</div>
<div class="tg-footer">👁️ 36.6K · <a href="https://t.me/akhbarefori/687870" target="_blank">📅 11:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687868">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">♦️
لغو ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها  معاون ارتباطات و اطلاع‌رسانی دفتر معاون اول رئیس‌جمهور:
🔹
ممنوعیت استفاده از پیام‌رسان‌های غیربومی برای اطلاع‌رسانی رسمی دستگاه‌ها، با اجماع کامل همه اعضای ستاد ویژه ساماندهی و…</div>
<div class="tg-footer">👁️ 36.5K · <a href="https://t.me/akhbarefori/687868" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687864">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aFoH7nxHbUUkD5kIBUNsfYcsBGnnsZDh9nq5E68DfBSBx_gx0hJZHy85woLr2K-2OYtLBCsWO1niqNnVjr2dQAPh_A8Lb4nycYMAUVTMzlmFKTz8puAyFYdCjPySb0XhjSHFsZVHfFKboeIoxbImvqySVbWvmvDFrz_J_gts73t18mSLrQQYTlQ9fSEqIPGxkXDRpWQs3QAdnqPziKLxVuPyAAadhACAGaLcvSrvLWqECircqhYDhMCJIsPkPLWLlvEW8z21T-oM3t5JhkKx8rJJULQupYd19Bfhlm3HGTGT0rwls5yslHqMypCF1ZxtY-iqcXqcWOvBO5fceNfRBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UtSZUesfaFejk0fzWud9FU4ZUe7hA1mET1mMPG3AbHWFmJMCOXLYoqXND-N1Esm94sHpNCCi_-dz9cReYYmLJ-NUF4zMRmifcGrETYdV8UgKlUYbk24udfhMP4wYJzb2q2Nmh8hss5VveXZFTA24eTCHf4bnXLYWHDR2VONZ6_032D6_QirTVyULPLcn63aOxWX5svAbGm7VvBJAFRFsKqsRok79DCg84kSD9CY7njD6GFjajaacpbba--0rbqtYexP4ZITpTbBMmmR3G6NveykLTOg7z45hb5-7idpPoaQWd1QzoAmYXBo6Bj6iLf6yyHkSf0zYqXzDkh-Dw6bxXA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">♦️
دیوار نویسی‌های عجیب و معنادار انجام شده روی دیوار منزل رضا کیانیان بازیگر سینما
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.4K · <a href="https://t.me/akhbarefori/687864" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687857">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ef6437ad10.mp4?token=GCZ0S1kapnpaDKtLKqzkghM8fKasrcruGrzVLfhYtS6uyOGTwZb8RnOiFkRDqC9FUo00u5nKlYUYdUkFGjJTE5qv_rCnJ1caMVRNmj7YEq3hChyJR8WSldiLQToIJiH_TndFPoApPFAUMh8rnJDgYVHaEEEQ2maqcARKc5DjdSGhfcz2wiyDypRoMrDrnZarvQj3rkElJND84g1r-XtXkTP_8W-sGlzMm5_puK8FRlgF1AkMd7jF8fJiJX6E-UzSDRhxo3Ou79PQF4CcLGU_K990ZLL-lgbw0iqaTlze-kUoCRw1hmMtkx28sE1_38bS5KGpb0oMyLTg8gyCmi8WL039tEYdOPQVMYB0h_3qySirrz6Bc0OVMxey_9wAbsz80dv4qP046O8hOCPCLSaAuPTheyb2loN_pC6qedsIlUPUsfDcz0C9eUEuCvtrXgKvPIvdQB8xspwZ5CioK2xSJ8ptGaCTeCsWfJwgNbFezXHUq5N3KGYYtNZo2h5Rk9PmkiWqkiASWJTg7Wx8QXvuIzccnEctgj8DmGf7Vat9_A-ts5j2-U3jlv6gzLzPPl13dKE6C40XLeKAdv9x1QJezqP9piKXjvq5kELECFQuz9SyNPDWb-d5HehYfakBdAfh6bfdzsQiWm-zJnMt_-J7jhQqoYOWilqx4B0pGeMg3M0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ef6437ad10.mp4?token=GCZ0S1kapnpaDKtLKqzkghM8fKasrcruGrzVLfhYtS6uyOGTwZb8RnOiFkRDqC9FUo00u5nKlYUYdUkFGjJTE5qv_rCnJ1caMVRNmj7YEq3hChyJR8WSldiLQToIJiH_TndFPoApPFAUMh8rnJDgYVHaEEEQ2maqcARKc5DjdSGhfcz2wiyDypRoMrDrnZarvQj3rkElJND84g1r-XtXkTP_8W-sGlzMm5_puK8FRlgF1AkMd7jF8fJiJX6E-UzSDRhxo3Ou79PQF4CcLGU_K990ZLL-lgbw0iqaTlze-kUoCRw1hmMtkx28sE1_38bS5KGpb0oMyLTg8gyCmi8WL039tEYdOPQVMYB0h_3qySirrz6Bc0OVMxey_9wAbsz80dv4qP046O8hOCPCLSaAuPTheyb2loN_pC6qedsIlUPUsfDcz0C9eUEuCvtrXgKvPIvdQB8xspwZ5CioK2xSJ8ptGaCTeCsWfJwgNbFezXHUq5N3KGYYtNZo2h5Rk9PmkiWqkiASWJTg7Wx8QXvuIzccnEctgj8DmGf7Vat9_A-ts5j2-U3jlv6gzLzPPl13dKE6C40XLeKAdv9x1QJezqP9piKXjvq5kELECFQuz9SyNPDWb-d5HehYfakBdAfh6bfdzsQiWm-zJnMt_-J7jhQqoYOWilqx4B0pGeMg3M0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
خاطره عجیب ابطحی از رادیو تلویزیون مشهد در سال ۵۸
🔹
در تلفظ عبارت
«مُدَّ ظِلُّه العالی»
و
«قُدِّسَ سِرُّه»
مشکل داشتند!
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/akhbarefori/687857" target="_blank">📅 11:02 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687854">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cf87d180eb.mp4?token=X0skWcSGd6duIyrw8pw4t5rbaBwX9xryPP9h3rwi_tajC6a_hlRzoNd59zgU1JXhcTyUqKOgd76eOwIv8JanMMuh-l3RZixTvM8mNVZMBKEYnJYtxbOyXNEY7eVMbGmTiaHy2VA6GM7dXZ6Yt20-5BMUJuqyHSpdv7nAvoAQohhEWbx30qb5JxCXgRFKFEY_R6x214rPAsNB0tjgFTy-2pdupNcmr5W9YwHvJk91g1ZTPoekj6puVwYzg2vg3bPRoGv5h4nqKmtbhPmvVVKqGRZJJSWlfBIaNRy3K4DW9mAF1yFUlTKNX5zkeiTjEegULIexu9rlTeThp5waajlCLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cf87d180eb.mp4?token=X0skWcSGd6duIyrw8pw4t5rbaBwX9xryPP9h3rwi_tajC6a_hlRzoNd59zgU1JXhcTyUqKOgd76eOwIv8JanMMuh-l3RZixTvM8mNVZMBKEYnJYtxbOyXNEY7eVMbGmTiaHy2VA6GM7dXZ6Yt20-5BMUJuqyHSpdv7nAvoAQohhEWbx30qb5JxCXgRFKFEY_R6x214rPAsNB0tjgFTy-2pdupNcmr5W9YwHvJk91g1ZTPoekj6puVwYzg2vg3bPRoGv5h4nqKmtbhPmvVVKqGRZJJSWlfBIaNRy3K4DW9mAF1yFUlTKNX5zkeiTjEegULIexu9rlTeThp5waajlCLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
آموزش ساده پارک دوبل برای کسانی که با پارک دوبل مشکل دارند
🚗
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 37.6K · <a href="https://t.me/akhbarefori/687854" target="_blank">📅 10:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687853">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمجله مس چی | پلتفرم خرید و فروش آنلاین مس</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jgjLTZge3-IyetkO9mccbzFs2rIYtK8Rz3hoR7x5Q3pwMPvj7NO0FvuimAhJB3nvpMEY3dj9NOMe8feQvjOW7Y0hb1oi13UGXdvUkbwnYgLO-fhH0jLykCqJpcyewhu_32HznllkLFb216xRF8QTGj5r0cJ4jW2yZeHCJKZcrO81amW75FhCBP3hlqYp1wVqW-qptofYynYkApp1NHXhPYa8N4CH0MxCM9DCzhHsJqeSfkLeS6pbvhJGvKcoIV3Q88lonwrrd6bQvavpC_Wrby-W5D_PTcVpKtU2nUQ6xBeX0ei3siKw0SErVQFASBQMu1s0Nq8eCMg4pGISLpOCnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🟠
فرصت طلایی خرید مس — ۰٪ کارمزد، فقط تا ۲ هفته دیگر!
‏
✅
با توجه به استقبال شما عزیزان، کارمزد خرید مس در مسچی تمدید شد!
فقط تا
۲ هفته دیگر
فرصت داری مس مورد نیازت رو با
۰٪ کارمزد
تهیه کنی.
🔺
بدون کارمزد
— تا ۱۴ روز آینده فقط قیمت خالص را پرداخت می‌کنی.
قیمت در آستانه رکورد
— ‏LME نزدیک ۱۴٬۴۰۰ دلار است.
مسچی؛ پلتفرم خرید و فروش آنلاین مس
🌐
خرید مس با کارمزد صفر درصد</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/akhbarefori/687853" target="_blank">📅 10:49 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687852">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">♦️
مدیرعامل شرکت پخش فرآورده‌های نفتی: اصلاح قیمت بنزین از ساعت ۲۴ امشب
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 37.2K · <a href="https://t.me/akhbarefori/687852" target="_blank">📅 10:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687851">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TMWYltrKsbsv8kLQ-whGbe_49IJkMfWU0KAwQZjFL65Q7zsbz9cCb2T-2UZtewXyesimPVkGZbvClvbHNXRm7kx_ricAPHt3BzRqi9Ec0bh9Y3kCxMJld7QueBz8hyUcILhTy4vMjy5vKjpJg2_PIqvfmLx385ZkOQCa49cCY-Fb6aNaQ1QD2iLNUKUd75wHrQeGcv815Ae9nVKpXsQSq7ZEWJpoHTCEhnJeFyQ5ewPm0gzpuHYKDxQ9ei5LvcBkxcGHN1ywDuTnUEntfREUWF71PWfl1bKndieUPx7NphRMXzyXsvW5GbUnGwwp4S73spcQIkd0iCxahpW6uCoKDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
واکنش سفارت ایران در غنا به توهمات ترامپ: نکته جالبی در حمله به ایران وجود دارد: دیر یا زود، فرهنگ ایرانی شروع به رخنه در وجودتان می‌کند
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687851" target="_blank">📅 10:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687850">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromمن°</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a6fa73d8b.mp4?token=pCgdb3BYdnZsdisbsbT5RcLl_XNLvNjHfrv_pMX62_bejGDAKC_uRHztQf6z7WKhciOY-n9uAvSzW3pKcuWjEnpdiQJD2vmvZL4bYifRw5RAlFx-FvcMi26HEuGi2uYczhGp1jCnvNNu96NldRR8MEMNAixFji3dFWhXpnVYumdgCSww_NV24PoY2CU-KTir7Fh_g57QO7u23L0nGERe2p_Pvk0shy1keMVx6Wz5rWMVAwUPcj2mP037EC-lSU4VntXl6MbBoaXUUNE6OD-n4IGpBA025uyCy6SF2c75a7TH9RAZi4Hr9YdJCDbiFyBUJg5cOTzp4XjpvLmxfJ7lKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a6fa73d8b.mp4?token=pCgdb3BYdnZsdisbsbT5RcLl_XNLvNjHfrv_pMX62_bejGDAKC_uRHztQf6z7WKhciOY-n9uAvSzW3pKcuWjEnpdiQJD2vmvZL4bYifRw5RAlFx-FvcMi26HEuGi2uYczhGp1jCnvNNu96NldRR8MEMNAixFji3dFWhXpnVYumdgCSww_NV24PoY2CU-KTir7Fh_g57QO7u23L0nGERe2p_Pvk0shy1keMVx6Wz5rWMVAwUPcj2mP037EC-lSU4VntXl6MbBoaXUUNE6OD-n4IGpBA025uyCy6SF2c75a7TH9RAZi4Hr9YdJCDbiFyBUJg5cOTzp4XjpvLmxfJ7lKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میلادت مبارک
آقای زِدیده پنهان و در دل عیان</div>
<div class="tg-footer">👁️ 39.1K · <a href="https://t.me/akhbarefori/687850" target="_blank">📅 10:32 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687849">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a016153d30.mp4?token=um4n2iydYEZuhhNfQrw4g9IanLXbIWjOr5-HE6Yd5FgMsKyVTBz_KHWOIe9sS-__vUzjDajzqil7yppQX8OoeTE_UVco7fJCSk8TgJ7PcTlZLS_jPAzKLeDGw5_8EHJDQ4cY_MmECPeA1dBDx2MdDMYbp2bqhV5fiaql7v6R5RZj_hTWas4T4vRxXaqR3JBTHmcO32W964y97LyhWgxKx5-Ogcx2tYN9jTNm-8n1MN52v_jqskHvhcunQNjxW_YPy0yUUoEe4wJwWK_7F2buDRM8X3FPBRZVhbs6S7o1b6H3BNjbxBRxHMoMvp3HJsQZHAuC7vUk6zWTZvqYHHU1mg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a016153d30.mp4?token=um4n2iydYEZuhhNfQrw4g9IanLXbIWjOr5-HE6Yd5FgMsKyVTBz_KHWOIe9sS-__vUzjDajzqil7yppQX8OoeTE_UVco7fJCSk8TgJ7PcTlZLS_jPAzKLeDGw5_8EHJDQ4cY_MmECPeA1dBDx2MdDMYbp2bqhV5fiaql7v6R5RZj_hTWas4T4vRxXaqR3JBTHmcO32W964y97LyhWgxKx5-Ogcx2tYN9jTNm-8n1MN52v_jqskHvhcunQNjxW_YPy0yUUoEe4wJwWK_7F2buDRM8X3FPBRZVhbs6S7o1b6H3BNjbxBRxHMoMvp3HJsQZHAuC7vUk6zWTZvqYHHU1mg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رنگ‌های جدید آیفون ۱۸ پرو در روسیه؛ گیلاسی، نقره‌ای و آبی
📱
📲
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.7K · <a href="https://t.me/akhbarefori/687849" target="_blank">📅 10:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687848">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">♦️
آغاز دومین مرحله پرداخت وام فوری ۱۵۰ میلیونی بازنشستگان کشور
🔹
دومین مرحله پرداخت وام فوری ۱۵۰ میلیون تومانی ویژه بازنشستگان و مستمری‌بگیران تأمین اجتماعی آغاز شد.
🔹
بر اساس دستورالعمل اعلامی، این تسهیلات بدون نیاز به ارائه چک یا ضامن، بازپرداخت یک‌ساله و اعتبار آن در کمتر از یک‌روز کاری پرداخت می‌شود.
🔹
فرآیند ثبت درخواست و ارائه مدارک به‌صورت غیرحضوری انجام شده و متقاضیان برای ثبت درخواست نیازی به مراجعه به بانک ندارند.
🔹
جهت اطلاع از شرایط و ثبت درخواست، با کارشناسان از طریق شماره 02191551808 در ارتباط باشید.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 39.8K · <a href="https://t.me/akhbarefori/687848" target="_blank">📅 10:30 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687847">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u-Om7OonWtji_Sk1U0ALKkICZAwhjMC0y6fI-oe0OnES-Qs_UvWfDJlCzM8vGR-IFivPNzm9E8apcHCF-BKiGFfIadKVwTc4WoV5oaehLQLWRDb6D5SxL7SWZKfCndAW8L7m6gSjlr410Rp2sMunEv0f2lrf5TVzd3E_rBBYqaO3tmlpd1wc9RDXnmDtRtO0u30nImdzjV0q70ISoZARRWXTr48842nIvQmHIY2u2O4snhmGlHBG-UWwnAIWo_1JIcnU_KBbnQvmbc8_3wp-DusiidfDS5AnbLmwAf_eNOAIOzWK_4M-D4gMT4DwjmGAgOiasRIsBZeu7_iscEyOxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
آلون میزراحی، تحلیلگر سیاسی و فعال رسانه‌ای اسرائیلی-آمریکایی: ایران به‌طور سیستماتیک در حال تضعیف و نابود کردن قدرت نظامی آمریکاست. طولی نخواهد کشید که آمریکا عملا بی‌دفاع خواهد شد
🌍
تازه‌ترین خبرهای ایران و جهان را به زبان انگلیسی دنبال کنید
👇
@AkhbareFori_En</div>
<div class="tg-footer">👁️ 39.2K · <a href="https://t.me/akhbarefori/687847" target="_blank">📅 10:28 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687846">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f6ec33636f.mp4?token=OIcws5yS_OWZUmX2XZGQ704DqOFyp0lP9D43fQCcL9o6XzSYob9VMK5vjCyFAITjSpZuXEAN8-TnndRTPEKUb8rfJQmNsGgRbY1ad0HIhSlKbFSGQ4a3vLRl_MYAmpC4zwGqw7UkfDd2LCP6LAQnNajYqcCl0YRU_4o_014rNkar7a6CVYftCB1QSzVNi7uyRxOr7JZrGpxVU95HBavn7jGgsqyBVZImXYKPKKqiQdfirm4_b7fVkDCy2mTlWZRZb6A_jz1GXKEZFmFh81O9Ztn3ll_AgtSBCuquOKAwj1kIVKKj89QE299vT8VM00X4ZPG6xmBSx23Q-VpqjPh7Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f6ec33636f.mp4?token=OIcws5yS_OWZUmX2XZGQ704DqOFyp0lP9D43fQCcL9o6XzSYob9VMK5vjCyFAITjSpZuXEAN8-TnndRTPEKUb8rfJQmNsGgRbY1ad0HIhSlKbFSGQ4a3vLRl_MYAmpC4zwGqw7UkfDd2LCP6LAQnNajYqcCl0YRU_4o_014rNkar7a6CVYftCB1QSzVNi7uyRxOr7JZrGpxVU95HBavn7jGgsqyBVZImXYKPKKqiQdfirm4_b7fVkDCy2mTlWZRZb6A_jz1GXKEZFmFh81O9Ztn3ll_AgtSBCuquOKAwj1kIVKKj89QE299vT8VM00X4ZPG6xmBSx23Q-VpqjPh7Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
باورهای غلط درباره فیزیوتراپی؛ مواردی که شاید شما هم اشتباه فکر می‌کردید
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687846" target="_blank">📅 10:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687845">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">♦️
وزیر نیرو: تلاش می‌کنیم قطعی برق متوقف شود
🔹
این درحالیست که وزیر نیرو روزهای اخیر مدعی شد قطعی برق متوقف شده اما همچنان خاموشی‌ برنامه ریزی شده پابرجاست.
🇮🇷
✊
@AkhbareFori | Link</div>
<div class="tg-footer">👁️ 40.5K · <a href="https://t.me/akhbarefori/687845" target="_blank">📅 10:17 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687844">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac420da3c7.mp4?token=g3ZRPZj3QMpzIkyjaHmLNvixIIkWYuNmWvDDA2Oe461HSOgbdn1UhL5-Lqde5xyXY6jr3WvZIEzhG6b3KWi7oBC-oZuYsSIUgY6VA3-zAwFEiy-Cl1aXMadqnCQys8mTDoMdOB9tRn7vHoEf1A6GIU4RakLxn4AgE8Xj9DMxTKlNMhDBOtzHGCBzzszc4mOok6cINduH94DrQyg5OkNT3-FaFPhGppaf2Rn3kTlVtpbOzdxXCWpWW6tWa7Hq9q3KG10b4bIKFZarISMwGrBXR4QQUl3_mdU-_G7Ixu0spgSnShmtIDgvPqr7PtaLeLHDpDZReOPXA7hjE5BEDvCKYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac420da3c7.mp4?token=g3ZRPZj3QMpzIkyjaHmLNvixIIkWYuNmWvDDA2Oe461HSOgbdn1UhL5-Lqde5xyXY6jr3WvZIEzhG6b3KWi7oBC-oZuYsSIUgY6VA3-zAwFEiy-Cl1aXMadqnCQys8mTDoMdOB9tRn7vHoEf1A6GIU4RakLxn4AgE8Xj9DMxTKlNMhDBOtzHGCBzzszc4mOok6cINduH94DrQyg5OkNT3-FaFPhGppaf2Rn3kTlVtpbOzdxXCWpWW6tWa7Hq9q3KG10b4bIKFZarISMwGrBXR4QQUl3_mdU-_G7Ixu0spgSnShmtIDgvPqr7PtaLeLHDpDZReOPXA7hjE5BEDvCKYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
رئیس جمهور جنایتکار آمریکا در ادامه توهمات خود نام ایالت نیومکزیکو را به "آمریکای جدید" تغییر داد! #Devil
📲
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/akhbarefori/687844" target="_blank">📅 10:09 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687842">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56a35e76b7.mp4?token=amVDE9GOGUMLy2WcXEjQkgwX22CNmcEswPLRK8KAsVhk8C-z_6ovNpkJ1CC3xHkCY-haX4s0imsFE-GSBxziJq6JLhkJeM3UqLgS-aQ2lYrdI1t49MkrdGGDhP48bm365O2wBWJvJ_-oEkEdTK0nRtoyLhqoT5TM_IZCieQkVON-3aOmHtkNRRzs8heygemXOzRyk_705YHPbtuZhWQJCc83HDZR0np4xA6i1-Y2RWQJGbDSV4dR1k833tcfQMDAq1iuuYCH0HYZEdDTBW99ai8A9Wrr3yCfY3uU6XniyQFfEpW--rz65Fy30czZS-n1BRyF-v9_bM9cUiUE4A7_J4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56a35e76b7.mp4?token=amVDE9GOGUMLy2WcXEjQkgwX22CNmcEswPLRK8KAsVhk8C-z_6ovNpkJ1CC3xHkCY-haX4s0imsFE-GSBxziJq6JLhkJeM3UqLgS-aQ2lYrdI1t49MkrdGGDhP48bm365O2wBWJvJ_-oEkEdTK0nRtoyLhqoT5TM_IZCieQkVON-3aOmHtkNRRzs8heygemXOzRyk_705YHPbtuZhWQJCc83HDZR0np4xA6i1-Y2RWQJGbDSV4dR1k833tcfQMDAq1iuuYCH0HYZEdDTBW99ai8A9Wrr3yCfY3uU6XniyQFfEpW--rz65Fy30czZS-n1BRyF-v9_bM9cUiUE4A7_J4WOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
اگر دلت یک پیراشکی خیلی راحت و‌ خوشمزه می‌خواد این رسپی رو از دست نده
😋
مواد لازم:
🔹
آرد ۳ پیمانه
🔹
سوسیس ۲ عدد
🔹
خمیر مایع ۱ قاشق‌ غذاخوری
🔹
آب ولرم به میزان لازم
🔹
فلفل دلمه رنگی ۲ قاشق‌ غذاخوری
🔹
روغن مایع ۲ قاشق‌ غذاخوری
🔹
نمک، فلفل سیاه
🔹
زردچوبه
🔹
پاپریکا
🔹
آویشن…</div>
<div class="tg-footer">👁️ 39.9K · <a href="https://t.me/akhbarefori/687842" target="_blank">📅 10:05 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687841">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromگروه‌خدمات بازار‌سرمایه پاداش</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2WrEhcpfO-KOGyRzl4wl2Uz6gNWYEHFNU_aai7yjP0SHqnuEOHRm_zILOi43Nog_cUFC1gFt4azBitRY3qirt_6xLWAxmovJwrFAiWLRc_pOJAtg7lmN_ETF-ACTdMm5dBFMo-7EJrPNMILJgliWJUwRSovqyMbI1c4p3hK3UXzggFc-zn3Xf2cegh93P9Nb1f8yB2v_xv0Hs58W4F58sMY1JkpVZZEmzyAbWrO4ICo6HUUHodmGsfvmUwif58R4o1J8-t0sQw_nd-FkX0vSaWV3121XVENoVXjgd9eqgOk5ZY-sUlVpQkxoCGQxG5_aKU2G3E8V7ln011HZQuuqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
«سیلوا»؛ یک میلیارد واحد سرمایه‌گذاری
◀️
سقف صندوق نقره پاداش با نماد
«
سیلوا
»
به ۱ میلیارد واحد سرمایه‌گذاری افزایش یافت تا فرصت سرمایه‌گذاری برای تعداد بیشتری از علاقه‌مندان به بازار نقره فراهم شود.
🔺
«
سیلوا
»
از روز دوشنبه ۱۶ شهریورماه بازگشایی می‌شود و امکان خرید واحدهای این صندوق برای سرمایه‌گذاران از تمامی کارگزاری‌ها فراهم خواهد شد.
🔺
مراحل خرید صندوق نقره پاداش «
سیلوا
»:
🔺
وارد سامانه معاملاتی خود شوید. نماد
«
سیلوا
»
را جست‌وجو و سفارش خود را ثبت کنید.
🔺
امکان خرید از طریق تمامی کارگزاری‌ها
🥇
صندوق طلای پاداش «گُلدا»
📈
صندوق نقره پاداش
«سیلوا»
📞
۰۲۱-۵۸۷۱۸</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/akhbarefori/687841" target="_blank">📅 10:01 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687840">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GCBMUndYIjR7PrFGaV0xGWGfHw6QeNU0EGHdo3BkUo6Y5YtD9FckAcTOfHD5PrhFe8XL-v32Cm2e7fKTkNfs6OwlTqE_RcuB9gPiLmqppvXONlEVzgFo9idsfg4gjUEsyPBt2gQL4Jpv5ROs1bCGFCfIVLNvxk45-RXRbqg-84aMbVfGNGfhvZOFbCwodGFTcAbWdYSvzykueKSSS5mwrwOvjcNvKVjcMljrgnJFNcx786tufGHffQdYPBKtd3SrMGDB6PpOHpw-5dVPoMeiBVTfJMiBPjjYMceaWkf4Upvj2rOf9I74rIUdpaY0zCCvASxkw6kUFefGwNoTLhd7Xw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🕌
فروش ویژه فرش سجاده آریا | جشنواره میلاد امام حسن عسکری(ع)
⏳
این شرایط ویژه فقط تا میلاد امام حسن عسکری(ع) برقرار است.
🔥
فرش ۷۰۰ شانه بخرید، به قیمت فرش ۴۴۰ شانه پرداخت کنید.
✅
۲۰ تا ۶۰٪ تخفیف
✅
خرید مستقیم از کارخانه
✅
فروش اقساطی
✅
ضمانت ۱۵ ساله
اگر به دنبال فرش سجاده‌ای با کیفیت واقعی و قیمت اقتصادی هستید، همین الان تماس بگیرید.
📣
درخواست قیمت و کاتالوگ فرش سجاده:
تماس بگیرید یا عدد 1 را ارسال کنید
👇
📞
شماره: 09128044740
📲
آی‌دی:
@farshsajadeharia
https://t.me/aryiacarpet
💫
💫
فرش سجاده آریا
💫
💫</div>
<div class="tg-footer">👁️ 39.4K · <a href="https://t.me/akhbarefori/687840" target="_blank">📅 10:00 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687838">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eb3e1c4d7.mp4?token=FzuYtAN0wW76uys9TkcC-VJkNsUh3maSIavaiB1yCpGwdKxMyrruAS10nAbkBUcBr39mUweFGqKl8bRIR00diI1R8SrAynWKQDfOjcBMTFBn8kAxaylc2OV6QuKLF4o2JcZlXuMKqpZFlIM2eEu00gColTujdjhlZMoyBDGQWnvqj8oUWUlMp9V_m3Cd9mrbQG0L2VKGpzkv41fu7ZkIlu4qbGzlE2OKAcmBu8J00EVoWk5HEIa6rn6H2CgNyI432x7GZvhGiCV0hLvXbyAXkgtxetQ-a87tiyYyhMiGsyIktL99lWFjZLFenSbjRxWHE3Y7VgF6WoKXrzTHlw_w8g5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eb3e1c4d7.mp4?token=FzuYtAN0wW76uys9TkcC-VJkNsUh3maSIavaiB1yCpGwdKxMyrruAS10nAbkBUcBr39mUweFGqKl8bRIR00diI1R8SrAynWKQDfOjcBMTFBn8kAxaylc2OV6QuKLF4o2JcZlXuMKqpZFlIM2eEu00gColTujdjhlZMoyBDGQWnvqj8oUWUlMp9V_m3Cd9mrbQG0L2VKGpzkv41fu7ZkIlu4qbGzlE2OKAcmBu8J00EVoWk5HEIa6rn6H2CgNyI432x7GZvhGiCV0hLvXbyAXkgtxetQ-a87tiyYyhMiGsyIktL99lWFjZLFenSbjRxWHE3Y7VgF6WoKXrzTHlw_w8g5bWCdLwG1qPHzv_F-6uobb1vX3yZpGnV_finxswdWo6XS4WkxwJ5y5P7x4ZMsJK2km9doRvn8lIB1q-cnuvhqTsf0DAViBNs95wZ5WiWVHZqSDinu3pXyqxp7EIEuOT-UK3GNh2uPfFBDedmcFqSyUVJkmTfpAFxDABLHSWk-27_Nq4AyHTakFIHdgi6DfGUBimcuC42ETn47MhjKYiPhC2NjxXcZSlvZ_yt8Ewn9wxfOzd2VqlrihY06zI3Gz2SozcLZGesngSyRm98S7wyNMcCAVrEuTAnJ5NjAaZVccHOnM3yqYqtBiyoam0JczLCZCDU_xYuhqK_JAXRCy3os" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">♦️
ویدیویی جالب با ۱۲.۷ میلیون بازدید؛ که با هوش مصنوعی تولید شده است
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 42.1K · <a href="https://t.me/akhbarefori/687838" target="_blank">📅 09:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687837">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">♦️
چه کسانی واکسن آنفولانزا بزنند؟
⁣
مینو محرز، فوق‌‌تخصص بیماری‌های عفونی:
⁣
🔹
افرادی که بیماری‌های زمینه‌ای دارند، زنان باردار و کودکان از جمله گروه‌هایی هستند که توصیه می‌شود واکسن آنفلوانزا را دریافت کنند و در صورت وجود امکانات و تأمین واکسن، سایر افراد جامعه نیز می‌توانند واکسینه شوند، اما با توجه به محدودیت احتمالی در تأمین واکسن، اولویت باید با گروه‌های پرخطر باشد./ مهر
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/akhbarefori/687837" target="_blank">📅 09:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687836">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">خبرفوری
pinned a video</div>
<div class="tg-footer"><a href="https://t.me/akhbarefori/687836" target="_blank">📅 09:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687835">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">♦️
خرید لباس فرم جدید اجباری نیست
⁣
سخنگوی وزارت آموزشوپرورش:
🔹
خانواده‌ها می‌توانند در صورت مناسب بودن لباس فرم سال گذشته، از همان لباس استفاده کنند.
⁣
🔹
در برخی استان‌ها تقریباً تمام لباس فرم دانش‌آموزان از ظرفیت هنرجویان، به‌ویژه هنرجویان دختر رشته طراحی و دوخت، تأمین می‌شود.
🇮🇷
✊
@AkhbareFori</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/akhbarefori/687835" target="_blank">📅 09:36 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-687833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">♦️
ویدیوی جالب از دامداری پیشرفته در چین؛ آیا در ایران نداریم؟
🔹
مشکل اصلی دامداری مدرن نه پیچیدگی فناوری، بلکه ضعف مدیریت، بهره‌وری و نگاه صنعتی به این حوزه است. ایران هم به این حوزه ورود کرده و حتی نشانه های صنعتی شدن دامداری در یک شرکت ایرانی در فریمان خراسان رضوی شروع شده است.
🇮🇷
✊
@AkhbareFori
|
Link</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/akhbarefori/687833" target="_blank">📅 09:20 · 16 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
