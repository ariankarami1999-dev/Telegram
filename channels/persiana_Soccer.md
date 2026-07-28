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
<img src="https://cdn4.telesco.pe/file/jCc3YSp78ZdyqfgEwgwUqx3oysH0qgR4aqjTXuxjv9rC_VvuMzlbkvWOG964vD6lBWkWZ_fEoADPwcj9ke883BDTfjYYHVT9VQWGWUyF6wYfRJ9M9BIHkwVyEkkUCH3O-_4UWsfmgB8_N8132nxEw0llXMc-8fBmvt_NMYcSLUL8rA_1x1UnZC2NLZETScQJ_gC4G9bdLdwW7nB4BR4za8uWd9TSYGCvDGBeTcrW7iCGvdaA4pkdJYQRnPjaY4n66_acKQO69OWRaT5M-MlMJRGL7nbOgoSYU4feJ9lK_3mrMDpIS2EAWCGKOy0Pj1QooCk-aYb5WKHtRnH_FdMMDQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 609K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaکانال دوم رسانه مردمی پرشیانا:@Persiana_Plussپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-06 05:27:46</div>
<hr>

<div class="tg-post" id="msg-26657">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rER--NWGUX0NRonOBiXegtSYZeJYmZcfrY4hZzlXpspeNyvrC30oNAH7hcBe_jpakmEugofcWAciWV46A5BH1Y5U1gZL_7afT2ciVfYKEl-IdRmxz8PArUt_viT7LnpLVgjo8BpQNLES_HcB7M19m9P_Wk6rm3jcWC9jjnAyvsFZJXYvBocZUVqkX5pRYpGX9VooAgCKrNZQ7E94Al-cXHnRkeKOxTvwfkG6Yw8V4Kb1eSgQsTxz9_cuoT790ipnV6wsT4nFjlexZOu_5y-mvlppXjrpkuDdwXwE5-rwfJSClpTrg_CKj_wesZZBIrWILFbe2ham5tRNMyq7_28WjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ مهم‌ ترین دیدار ها‌ی‌‌ امروز؛
بازی دوستانه شاگردان ژوزه مورینیو مقابل لگانس در مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/persiana_Soccer/26657" target="_blank">📅 02:28 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26656">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gPN5tJ_UuyR2BN5AW5sRrR53-JEGDk0hmA82kn585ETeI-acSFR5Ll_PN-wCEyFahdno2CHPEQwlaHvvHrkx7jIvU5Pttu-NAeUrTpTsyDEjgpJoVXOHHKPNubPNbqTpICE31kXePEGSukl-x3VmSyDhtODsDhrBJ65X3qWb5kOCSmOiq9ioAS2-XbUW0PPyVnZhTaQ60M1DaC1kV6unwEOef_rgpMuA6O3Qo5tttVJUTSxXNnf0GhoVAulPDw48lwTwISNrUDa4Wm7FdMnU4f0_iVLaIvF4iVBiotvoLiXjIHwPCj0KUlg7qvNSh1eyA1nuAk-N-Ktx39MQby49jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
#تکمیلی؛ میکل آرتتا سرمربی آرسنال تماس های خود رابا وینیسیوس جونیور آغازکرده و در تلاشه که اوپیشنهاد تمدید قرار داد رئال مادرید رو رد کنه و به جمع توپچی‌ها بپیونده. نیمار هم به وینیسیوس گفته جدایی از رئال مادرید یعنی نابود کل دوران کریرت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/persiana_Soccer/26656" target="_blank">📅 01:44 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26655">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47adf0f058.mp4?token=vtLYzh0ZpADdg5EAfxzb0G6662ABs66BqLoEHAzUr5xdZx6bWvBz7PuOWo-_O5iIKHKRXwg7PRbHwTo7SOQp19giL8TkVYVEr-UiNbDuIOqI6aKaQAsmiYU8M_5FjLDuVRgH2w3OB7kihy3TsmqhpLoD08EmCD1Hi9eFBawPbvBtzQPx-HdWheUyjLE1pOA416xG1yckD5YXZqMZpvjOj0XQA_YVesz0nul-ykC0uJipGkpptfv1nLzyvcbjZZ4uvx-EFSysjAUuf5BviYIwkd0WIldPETAfNXWLLEnN_CSu2QSCtBS4_q7UbLYPDtQEGRCjG-GRTYdu8YtnHrsI4wyjKLF7Nh55Z_TSc3bsXRKTJd7M9l_0N2Bi2JmBCU04-aq15zlplz-ZM7vplBtSU-ofQjS6tT7XSgO85vV3CN5kb5igPqOyhSeqZ6PbsXRZhFAhdzlum-2m51UvnIAHbjaAcMlojUygM5gDojUUO_pEG3wmANhCPrQC1CDDV95F_M64EHQbbZ-V7yDNZWhk6-V076WzpVH5UchrJeVVk_Vw3-KAEgVUgxrfk7s1OAaQuh0-uOeWooEXQvwiYBRFcV5cZpEQZ042nKqZUO6NKCS3d3O9nc0nJw7vu_rdmOoL9TmAfXnisA-JL_bX45DLqfnmWL8PF_PRfaiAyVr6OZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اوایل‌لیگ‌برتر
؛ یه‌باشگاه‌‌ایرانی‌یه‌بازیکن خارجی اورده بود "روزی صد تومن بهش میدادن میگفتن برو سر کوچه فلافل بخور… نوشابه هم نخور!"‌با نوشابه میشد ۱۵۰ صبح‌هم بهش یه بربری میدادن با چای! تو یه بازی گل زد یا تعویض شد، یهو فاک نشون داد بعد اوردنش نود که ماجرا چیه، اینارو تعریف کرد:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/persiana_Soccer/26655" target="_blank">📅 01:33 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26654">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAbiX5d0oPsJ4e3feuIFIW9otfx3im_aXH6WAi4KF2JxMPL05f2o3pb_zowbGjemDTvdHaZroWmSYvcx7Y505oQ2uk403QPx-D1Vkr1EJTAk6KGmYbicZdF4fy91IzVxfK2vOaVcTcLckjyH_3HTHfIDqaCaq88WjsvKBgvnrohPrPmHZhJ1hSRWsHNmh8_7Z1poTtbdy0B9c23wGFCS24NkXXgM4NH5290zSzjW0l-BwkKEugRLWUvRAPFxSR913ehEvyvFGpLtC4lulbjgZ5DJM6HWtnSBH87gybBR7M2PvW78pKayR0ojs3wmbO9jVIHhK6XWAggeph1Zyiv4lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فلورین‌پلتنبرگ: رئال‌مادرید رسما آفرخود را برای تمدیدقرارداد به وینیسیوس جونیور داده. آرسنال هم بلافاصله اولین‌پیشنهادخود رابرای وینیسیوس و رئال مادرید فرستاده. حالا تصمیم نهایی به وینیسیوسه که کدوم باشگاه رو برای ادامه فوتبالش انتخاب میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/persiana_Soccer/26654" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26653">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z4PXTMTVNOJwQ6qqHtbqic6_hQYMmwJv9A6R911Ir8Dsy6diuHzn-kt36DXdBQSrgn-u4h-oPrkzsJwyaV9ObMT9L5PMW9YIqWNVNX93GbPIKyIt4G-iK_i8W__SL22H3XSOAvlvSoCo58v_hEfr7H5arUjGi2lex3dKMK73rSaXxBAmqi7DvVeoYRvtf-CvHWR_lRB9dUu-VWGp802RhcQUzHloXntTcR0N4A51vd4kGLgcIO9gsEwm8A57a7_2yez8mRj9crOjR-0BcEM7xfff9yqPni79aS4IwdrDUtZdZT8LMYkC2D3i9si3rLKDTmcaqPkdWVqnIGnlhfJvMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
👤
حضور کوین یامگا درتمرینات تیم مغرب الفارسی مراکش بدون استفاده از عینک؛ معجزه خدا تکمیل شد. بینایی او صدرصد برگشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/persiana_Soccer/26653" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26652">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F51-CvvEswJRQDLAPfIvZwru75m01zUqA4cx_Jtfy_PfRYwim_ZgMKQ_kvNttDe-7Ep8SdTS9GFJS87PKBmUe8uDCXc2lD6SHmv52T3_YbhcACMa7p4Q0sKI6s5l9koxOT6AjOswC2rR1tuI72Gjbw_GAGEPRNTxRmc3Db6zsED9cATrO-Xzr2V1Aga7pIv_-jQh6gHqo13R2BGx46_slVWfr7fKX9iuFlA-ovAnj0Mb4VEdsnP3B9YkVciqAQ_anpn4XSFI8VaArQ5YZoOrZREV_81sI-or5ekNzuKxTzPC9TB74MycqTkUw6akYzopRGbcZe2c8uW8dMNdMokeyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/persiana_Soccer/26652" target="_blank">📅 01:25 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26651">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uCIVAxoeTRRCl6ybBc5SDr_Pwoz5qK58keffpq6KvmW6xyc7oD71sru-gpDLIIS-qodNFpdNZ5M444F6e11bA7oOTfIa8Sl8xnQSYEPksr51lCA22nlA97O8htYvpc3PkRUKjkb12e1lgjZXcTZuTwSKdA0tK_W1QI6DGKsnChrFR7LE8yLCs8orTwoq5quwbHA1t9zzk7DtbUU5fzwxgGo821KRa1yyy6TY1njuQ4VZwSoODuNx01T658pmtCHcQxvckjjIjIkTdEQoMVqITgyQXwrwWMBOm4Z8iDYnlK5YPC_CD2lbVUrvFwBO_vxhaei5evVaZpjJVyFnC0bVQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/persiana_Soccer/26651" target="_blank">📅 00:57 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26650">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/185f669e03.mp4?token=GSEDUwNeI66DZeLDgTcAMJ6oLCDvROQcMmvO9beRcLPwInOypR7Oo-ahtKuUMyYvvtCJ1c-heyD45iDwokKMXvkzDgWplNOUpa8rCeyvzKq-q8_65u2FW9wZCo6hh17m1BUW__q7evUHwkAjifiHlUNyxhbhBNKLLgZ2PTK6nzLQWZSa9RVkty0xqWRTUNBld95UMoo6WO9nSjpqhi4iLby2geyUFNt2fqsUoOZjbZgIZGe3iC2CepwnlMnmuOiZ-q0rghbJyvKcRI79HP4emS9iyhiJEy9xKvrwYGvQSZmotU5zQZv0dwxFq3xeVGap0NE2Mlg96P_7hSo5ipACGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
صحبت‌های‌جالب بلینگهام از زمان‌ بعداز پیوستن به رئال مادرید: کارلو آنجلوتی گفت فکر کنم بلینگامِ اشتباهی رو خریدیم. باید برادرش رو می‌آوردیم!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/persiana_Soccer/26650" target="_blank">📅 00:50 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26649">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vRmbnMUF8DPMWoTkrf76s3vLRImJehQp4l9pRQIpDkpwxIsv_VWLBs_yL5uY9Bb76JtstDslRq25BX5s-Z6lq4WLQrCWne9mN56XQo5jehRxW4xsPeZqis3cxVOt30T1cRUuku0edBGhT3bu4TKvvb4y8DV2uxym5kn8x0W2RE68c7YYfe8djDZ_XTQ5x91Qsidgqoun6eZg9vQAqXaAcJVAMyAEXGQ4GSFB3nB4IcIuQS-tTRkePy8ltT2kNiK2cCIOYbpSxDU2mLm05bxwr4qOExOAaw4PSzzeLzlJGypnUbvj0We1Y_3uPnfr0yZl74dWbBMq3ZZvUXGXlSwqyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇪🇸
#تکمیلی؛ تمام خبرنگاران معتبر خبر از عقد قرارداد رودری با رئال در آینده بسیار نزدیک میدهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/persiana_Soccer/26649" target="_blank">📅 00:40 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26648">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sJtij5Os5MmJHbgg7X0rElfPZGpLhEkRREFKrCbE5mG0wzMdB0NjWfNM7uUF0DtY-x1TWiZKbuImpHfHyT_eqE13LPQVd78FgsSMxaXariL7_J37ftNEKX5sOdzvEb0M4z-nWkhsGo8PRKuSKN3EWgW2KVNDPPWUvWJR75z8AowP7nFCwPPH566fXLmfob1CrDqNloEu0RTm3CiTIZSZzDcyQZShoMwD7-0uCaJVWZBBWE991BkmZVmfeyFyYrW61KgEXqLwM6f5tdna8a3AiR0cLqC6rbxtQDRWLDikjV5wG3MM18oBGhe7vksLlE9mN2vEfKd3YJ1OcqIdrGMV1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🏴󠁧󠁢󠁥󠁮󠁧󠁿
جان استونز مدافع میانی تیم منچستر سیتی برای عقدقراردادسه‌ساله با اینترمیلان به توافق نهایی رسید. استونز به‌احتمال‌زیادجانشین باستونی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 35.2K · <a href="https://t.me/persiana_Soccer/26648" target="_blank">📅 00:13 · 06 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26647">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eAp9dgw9ADY1kPODgp_SS8PHLUYQbdqlNjEnMI0-a8DaLQJg2nUcHOYLadtrEKaTfGTcRgLMoQG_yA5UX0pBx9flLgLqelRGI5qqb7TboyqwCdV-PVeSnG97NIZ-DssPu3w0ByfCvOG219UFAEol4hPKg-8WsoiGNXipLfNSzT2XmDZMAicJiDH6nkZsXxbT2G60U_LYxiEvYqQigyYarVDHp29hCthJCdBG3WIdKkxbaraAxDwZ-yE_uI8WUGiNNsH0bnfq6pFqo6YPadyRS4XGqZCuF6n-JQMmiJdGtMgUBLu6ThcOo2uUREHf5O_FIB7YEcOUN07k_kAnKbzyKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
امشب‌محمودرضابابایی ملقب به "بچه" به رفقای نزدیک جواد نکونام گفته "بی ناموس عالم هستم اگه اجازه‌بدم‌باشگاهی با جواد نکونام قرار داد امضا کند.
‼️
سرمربی‌سابق استقلال ظهرامروز با مدیران ایران خودرو برای قبول هدایت‌تیم‌پیکان به توافق رسیده و قرار شده فردا به…</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/persiana_Soccer/26647" target="_blank">📅 23:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26645">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e09976f50c.mp4?token=SHfSWz2DXuC1JwXZXBB8U271-sj4Zt1_6QXNcaQWqJZ0WNMS9xEwjDLwcC-FnzgoWGWAjrexrJcj9tsDSOvrnh8t7D5qwT6QFSjyY7J6ZoYBUIRp6BDY_HzlK0KbI0_fh6igHTc8GsFkyZBOMrm-lGI6Ms4dnXpFGhiMFr6FP8itF3XzN8iYxzWkyrTX-EiDDkNmPGBFajEGRRH7mUBrL4egopZXcPsfz9O4VKLxYL8DdvzqpEKV8PQwjuPHaW7_uvwWtrueHhFS4hFM0gwHMMW5V1yyJn-cYNH6Rfpu85GYEtF3Nzy58EazCGUlza6Lk-AdYDSby-dzdSlJ6Obs8w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/persiana_Soccer/26645" target="_blank">📅 23:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26644">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D_KyClrn_Wej310DtgBg7bZAjOQKpLAk_DK2ySA_EbA3E0HRUPQHT1YPwNAefK7AHAW6kSMnonMP0Wiz9xod3-MJldtn6LLTuJs3N30CHxABKVczBaeLKWgfpWhlOz63TkubaddItHB1IoF5OWGo-mdgnTiEXAqqqfKa4lIxNbT4mMK56tfbgkOxTK2qKJc20-pcD8ZNgb0wYt-Mlzks5z2yp4Cc4rcx0_MCNLZa2n4n5gtf8TiCWpGYNoZS4pEj1qjQaCWlPsJgMvkHFOxJ3WFFI1O6teGk2wFG6RMCF4Mqq-ohe4GLDYKR1a09C9X_C1WapO7Gt1iGDOmZpc1UPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔹
فرداشش‌مردادحوالی ساعت 16:00 قرعه کشی فصل جدید رقابت‌های لیگ برتر خلیج فارس انجام خواهد شد. مراسم از شبکه ورزش پخش میشه.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.6K · <a href="https://t.me/persiana_Soccer/26644" target="_blank">📅 23:28 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26643">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QgJMqdMbuaW-x9ui-rKKWuBBk593yX71wXNn9MtDX34g6SNBrmDAzOI021smqjFGbnjjvWID3TSQ-CnmNoplj-F4FmE_ubYMI3J95LGgMj3loRjB1l0enuvjGYPfDAqbsWAdF8_-nM8ylfZiF4hVczHwKJMQddLWbgoQvGeslmy0dvK3zNxLyG80U-ilPO4V6lp-7EWLoVvHMnKTIaJ0AOMmWwttLBDQcpi6i9f5nfBRkpvHkV-4piLpGfNynDboEC2sPPgjTSI0Mv6dGpnjHO-DPs2ASiquS7ZTjMIQTwdnQMAIOjGEncGva-jY2tW3642rmY0ixeR3vt1A72RBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
یکی از مدیران باشگاه استقلال درباره آسانی:
🔵
با توجه به اینکه فسخ قرارداد آسانی در سازمان لیگ و فدراسیون‌فوتبال به‌ثبت نرسیده و باشگاه هم اسم آسانی را ازلیست‌تیم‌خارج نکرده‌ونیازی به ثبت دوباره (new registration) ندارد بالغو فسخش و توافق نهایی، طرفین به قرارداد…</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/persiana_Soccer/26643" target="_blank">📅 23:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26642">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRxZYymahxCnNUXSNaPcZNGVYdmutff1R_xkaO2fmUBVVTTuJX4wX-04wSYk2slJD0q12Cr6Lu545g0MMDGcouaJQdtLytIjl9vB33ZycY4g8jT2gSjVLgoAAnjX05Fm4SfXrQfYYxMsxdYpYH4rBIrq65bFDouBB62fF7WSkRNrGw0uRa2L5okWNdpHR9dYVBHr7kXVsYeD-ehR6oxOSfk5bJUFuhT43HBWxE2SSC8FV3hl6qSgkA-v_CIySIltG6KlmtyqBFdCMsxn-PIb7Y6rmhlA11Ka53P_PyRX0Z8nzMfgjwiOIW01QIqJDnYpzu004cxOJNWTjk4wgzgVmg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پرنسس لئونور شاهزاده اسپانیا امروز درحال شنا کردند که ناگهان با شش تا پسر شکار شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/persiana_Soccer/26642" target="_blank">📅 23:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26641">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dpM4_oONkl7285N16_CwukXXTawHwUu9XpOVrht_2JgOKhnEX2mH7mt9iytTZXocaF0NmxsCCkOvse3Mp3NlavHT2cxp-2_zEeR6rv1Jej7XL_rjxLzngGLFXK5nbhljIBkvEwY3WbNrk_qzkLC6Y1CEpPz0eEMtJvYzy7oEUBcon2Dw6UGeTMTkJDcL4ZTtLxQ0KNDxVTxifWfnfqnOneQ9k1jARMv5et47cpBZNoCzpXfMCHd5S2aH1i5q7UQZfpnyWTHVwi0QwRfqskXhboAbozXvqxSFF05iJfeKxhyfUD16WD86_65OWabLpzbolrMQu1Jy_uJRIbejTi4ULA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/26641" target="_blank">📅 22:48 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26640">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bh8ZrS03wW_OGY21Q6A_i_wfQlY-XMPwYyx4vJhAblzAg1QpnYJWErPrgfMjnfQfB3nwCxnAYqRtMHHT_uX9fvoJiMf1aDzz6CFQ8ARNupuM_xM_Dhy6MkWpJt5c6kUNwYlsaCHcpUTshz6tm-9Hhc9vVq2qEgubOxYcSKUVClNm7jlZXRzeqNRWTjQ0kPiu7MeZxUSIWlxNb-hv0KF2K3SdTcHqKzv0XIPvdjaOOvxDxfcpgh8UOPxNjKpiiFQxEqhtSNSPpSRIivNIDtBgbCVol5vVy_czqBwR1dvv3IOUCUeNlLg3NinRpyEWtwBrZhezlhzMutzDvqH8ZUrUuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
#نقل‌وانتقالات|جیمز ترافورد دروازه‌بان 22 ساله انگلیسی برنلی باقراردادی‌بلندمدت به منچستر سیتی پیوست. احتمال جدایی ادرسون بالا گرفت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/26640" target="_blank">📅 22:29 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26639">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tWG7zQne2TXr6K8oPo3GgxVmQWTgIPKaO5hP1Xf2utPRL7FT6PMz8er-iroLvgQeQWS0dkt4XvBCHXCBarDrEGfWyijJFxvupS4RlRQOvJQxHKX6BZMdci7uKPkQFzb8nxRGCq8-nA-FxGMZRlbX8DUUsDydIYoKFLQg4vIGPbbo3shDqUpMDtjOE53BwOcwcmIfx-MUf_To4WuiwWk8_nA_dCnVEItgtx87iBdsls-xTgXebvqdSh0uGqtjuZ8SL8NdyPCW7H-jn9e_Kddfd56veyRwbmtaUsHJUUCxJRoBJ4qj0IhJoTQZqxF29LFbc-6GFlHfUZefiudmVABrYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
🇮🇷
#تکمیلی #اختصاصی_پرشیانا؛ منصور عظیمی تا ساعات آینده راهی امارات خواهد شد تا رضایت نامه این بازیکن رو به الوحده پرداخت کنه. انتقال محمد قربانی به تراکتور نهایی شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/26639" target="_blank">📅 22:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26638">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KWTjKH0ews5z3dQj7QMfhvoQP9Vf9BCoO3785wgvWzG0i2ggTGDBQ1GgGAps4kun1l_8uiEcDyQWKdZIMEEdoLzIJS1JMwLajEorKUaPG38L_-JNIa8Vc_4ArIQfOc5KBD0Be3XTo5_HdUwWuTB5KAGFL0zP1Q9NbuAOaGX03TvUeytXr5ua7ObKKWycU7gvtG-vgSRbR58X-QdyMn3RQZhimTjQUQ8exqjJtwM5u9DwUU-KUeaqGLa33m-t6J8gGXwYZinwsxmwepsI_H5FHGecWJRdUocAAgLkQkhzVDk3Rg06isjep_eMV67HOFh07JKvONFDyHh1XdrDvKopmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🇪🇸
خبرنگارشبکه‌باشگاه رئال‌مادرید: به احتمال فراوان فلورنتینو پرز بعد از جذب رودری برای جذب الساندرو باستونی مدافع اینترمیلان اقدام میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/persiana_Soccer/26638" target="_blank">📅 21:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26637">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PMIFOfH4Ummqqud_YBRfq0AiFDlGbA7RzWqA2MxFlK-5jDie6gokfT3VgxxLWFGyo-Hu3NZym_co3yKzoSEJa0ETLeAuEVThhCh25NpkYR85No9-v_-ycjQsmfP253qcJEtx4ytcgX9Yt-k9bfO1yM-Q09OyOH5bi7QZg2H8g0YEvMQm9Jh5dyOPO26990RzT9IGXfhokbC7rEiyZwLzkamh5HiMUr3pfcDvZxpuC6t29yJtfMbwTVLEHz9g3WZxUP9GcTeIEMWpavkOYTXUscTBmFJ8tahWrWHiYFyTyntQ0eqmIqfza2f-rMv-UE9aArM4TrCfIf_7V1tu_dQVVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
رسانه‌های عربستانی: باشگاه الهلال عربستان در جدید ترین اقدام خود با پیشنهاد سه ساله سالانه به ارزش 65 میلیون یورو به دنبال جذب لوئیز دیازه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/persiana_Soccer/26637" target="_blank">📅 21:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26636">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OhrSL4OT7akFezOOV20GpJWTOFYBa3Lsrd1PrtOOYNqTmqvksoxcreEoUPLp81lFkesoQnZiLxIpKyhv01unkIldYtRFIYi_CreErjDVgetEARo94OVb5QD2geOxAkBumhYxA7Gl-53_9xFNoDlYocnk0EJPznETJn-PtnKqXBZqxCxPJExXzNJ9XdN2E3BaWK_uQkzHWlwd-4MMGT44WLVVe2fMwdy6mUyP4UfONuNEPeX3uKrwCeiAq_oUVdaTBAaefzfzBtSOiKyMMkpCmxEg20Nym4QgH2QASvpvcMltuedn4p2mkee0WTjN2X9tRn1ngCWtC4yrEjRr6BIdyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ: ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/persiana_Soccer/26636" target="_blank">📅 21:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26635">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n_ku-_dxBuhLq5DvlllfNNeARH_2Ar_-CLfZnL97Cg5GZlRiL_fE7-m-yuVe_q6c6_5lT_9N2yx8x8WfYJCfRI4MF18scL3qu67wLKoRQ_W0cNvbfwsS7cJel7NjdeGKQb9ihTEQCIZxuXByTsaup5gjqfoDyW32DzAaPv1vFiqNlm0HhwFp7FHzrBI_ZCwWFKeozFXAcCSCeJeShGgODFA7jmXUNSILioBD3pCMr6JBPls63JBseMMzSVnI6F4pzm_jf14_EJpjne_7-l3X-CFMwX_S85VgSwXqk9yZZPaJIXdX0oa_MfgpcleydbNh4NHmP2L1oSIaP_QJTYY-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آتزوری‌درحال‌شخصیت‌گرفتن؛بعدِانتخاب روبرتو مانچینی‌بعنوان‌سرمربی؛حالا پائولو مالدینی اسطوره میلانی‌ها بعنوان‌مدیرفنی تیم‌ملی‌ایتالیا انتخاب سد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 55.6K · <a href="https://t.me/persiana_Soccer/26635" target="_blank">📅 20:45 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26634">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KUvVEWFuLH8InWb6Nk7Dg2xLyqqBDz--E3jYsLff1HfDtilUdne6QfG6u2eNe0MvIYnVN0AsCOPDUQuPH_U31Tov8EZCbRRBA4nZ_jwI5d6B1y7y5AV4vST_HDNPatzTR_iya-cOlOEe1Y4tORUZKTLuZ1wDff8ck7cQu7QVY4A3jehfCVw0BjmUsQZaMCWImyXaLEQK_vCLdQqX9cQ0M9Va-jjKxENYws5day0rtGEAFzrtXsckq2FxaocMJG6ln52_qoEFiL-CIHTPxpjxItmVi8fiLjgh1WE9KyHlfeYWK6KQ3-Va7VBtU3w0hGS9FGopSPI9rlltqzmyrZUGOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه اتلتیکو دالاس که درسطح 2 آمریکاس و سال 2024 تاسیس‌شدامروز به عنوان نخستین قرار داد تاریخ‌باشگاهشون با چیچاریتوی مهاجم ۳۸ ساله سابق منچستر یونایتد و رئال مادرید امضا کردند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/persiana_Soccer/26634" target="_blank">📅 20:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26633">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ae0WFtqXEQH8ATlgGVZTyYg8kRXyVg5paG46yY98OBTM_EHUq8RILux8Ax5YlEqKzAREJjMeOYeUgjt4JL0A8FaTL462X3DxGSksW9TZvvJQlwdbkLyV1gvld7TLVqM699tSWDhXqcVXqty95LN4id0wfbaNknecUBqutuC92IvCpWq5IeGENJjR5-fG9vSijPhkrqA9bAe7KDyDvrJ4ECwfHYFD7mqp6zS7vK49eBav7jJ28AH54WK0fgGEsS5zIuTZqeCIgIVUnh2oXg2DT9Nl8cGXCgBFq8VT-YW_a137x5FxQDCk4bluc3SxLw1SvpTy61QN_PArXO_TsGXiBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
میلاد کرمی دهن سرویس بلاگر محبوب ایلامی تواین‌وضعیت‌که‌میبینید داره شیر آلات تبلیغ میکنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/persiana_Soccer/26633" target="_blank">📅 20:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26632">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EPyRZufGAQ44--VbUdq4OPOpAfxOpU6pdClqMFvGTcaotLH3zZSiPOs6BmCKwMdffoBHItbsFASvoB0k9Z9BbkxPbkrX5TUYl_uU_K8tMLW0bbPVICEmZZIcyvIrpPOu8h9YOayJI9wy-yJdQkB21mNdWZonY30xWynBq7qfCqkHy8JQaHr0CYHOpJYBCmjDAbQWQXNPYXKv9jsDjC7Dyt8eGOJHgzWHfoAlQdsb0keWPj6zh5xTeeKwCGHEK2W3xLBcuYsF5JnQHhG6gDevC109gJ-LLvd4_zKkoYKAbf-OyQFlIYRN6izlA3ELIXQAHWH_jXJhTdIys2Dkcf57iQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ روزبه چشمی کاپیتان33ساله استقلال ظرف فردا یا نهایتا پس فردا با حضور در ساختمان باشگاه استقلال قراردادش رو تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26632" target="_blank">📅 19:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26631">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Iky7foMoe47H3Jt4qGj7WPZmGP4fQZUnyFk0FYxAfqqXt561xkC1bQXm7mHnOwTQVexaT0bxoBWTAAcsVMXHltn7cn1-Qn-FKbFJfp55bMoyE_p-1WYOLjgCcWhrNBQQjgIID3HRvO83FZo8rPSCX5eXHxrVHg9FKJm7Ucgu8mCVIHMhVuWgdl2T_UddkASBMPUoUM_a_gg9qnWwy6e0s-X9bf7VsxMeE9BcGsfVlyN5q2d_j7Icvou2XFg74T2ZlCkZG_6Hep8Zk6Eji6IWcHXjmZ8G9lp22igzWJyH3dBeUwJgSoZ5VC4Lo1U7-IgQlHKdDzNUoBxVrynU2VA8dA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
فلورین‌پلتنبرگ:
ژابی‌آلونسو برای تقویت خط حمله باشگاه چلسی خواستار جذب دنی ولبک مهاجم انگلیسی 35 ساله سابق باشگاه آرسنال شده است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/persiana_Soccer/26631" target="_blank">📅 19:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26630">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDlXIfJ9gTGYPMWtironeBJwKWP3kCkybBaO359uOPT0VJ8uIWVTR1alrzlZz2HJ2a4Bsli778K5YfizIk6-ziQbX30JKpcoRiT2nJqQ6A74i2s9zctSg_zT6LD3gCyh5hv2xBEahoZZWL9duE7SMokBXCmmN9J0PLh_LQjnXMlD9hdN56FQIiezRR4S1cvqhjY4MhVSzuiVvXH24-NarzoaD_2HeosWhJqkE3_h9JGEGwJM7WSKcqxOUFf_hVx8qnjrBeGXcblOrsAaCacpEAWijEpQaRFkWr2pRtdh-mmWVJvQ-GEAmSd_0w0Oe-9R9Q67sy9cwmuren2lHKKMbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
باشگاه چوروم اسپور برای جذب مامه تیام 150 هزار دلار به به باشگاه‌ایوپ‌اسپور پرداخت کرده بود و 750 هزاردلارهم به تیام برای 1.5 فصل؛ روی هم جذب این ستاره زیر یک میلیون دلار هزینه داشته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/persiana_Soccer/26630" target="_blank">📅 19:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26629">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hAIdXMpUjL6n7tNmo4v8P0gGeNQDDOcLWzB1U_OSQHfvBlMTznQEdEQwAJU4VZdsJdid3fCYHbSyaFPh6j79f7jgomYmD8IooibckuT5QAbbIO323LpPI5KfzBzR1aFCoLJ9LfBp2dMKptcasQIGoPSTnC0ZtiIoPIC5sqJyCFPkq2Hs82nmuZQ6GSMZJWQAiYO4Txyi-LcZkuKyqCsbYQ_zIyqzK-nxO5rewECz72y2XOcaTKFvspoWB3b4USHYtVOlD0IQGAySYlYk9dETMrZEIDDslS1kOo70NMevm6g3emt_fcVM8Y6s0c1upIJg3MaK6X5VU1SWlg2BHm0gUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/persiana_Soccer/26629" target="_blank">📅 18:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26628">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KLM9S5hfFn4kwgZX8q-HqfunCNipfJTmcJfglabm6GD1fBMqXxTrOUXJDrIZajM-EosJ9rMYWN84VTHQIOJbSTZIqI7zwsVdx8v2i5bsZ90_E1r5wl6p9JdhFHMyArVaPeEmO3dHBUaCVzu4rl_IewxKYxFn6jNpyZ6lvBk3E4jDaGLmJ5hdG-_Np5V1_rgQjp7OB2mzBoGcyB5j9k913I1xBGJ9J4-krXUd1SuHb3m8MuSDdcxWa4VDbmlvrmIbZiPl4Y-ugDfztie2vM4rkjPCde9t3L7_qEhP1kdsAMHElbvjD47D4CG1B9YhJv0Mx5WawdX0kvFewq9dLkAtjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26628" target="_blank">📅 18:30 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26627">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=JBA5LDoC4fiwEtf5IF1L-bn7clhC7Kja7Xev2Ayz_9kZ7F5PsqIsTvcH4tRfI39864Oe_q3XTSjZVVSVvCBhqrJzPJw9GBYtaOoCS2vGK8nWwkBlQa1ij68MT-UDo3LYmYlw-P4xfNpvqE3-Pox5sZO2EUy9cQthjBldNavqZBFkknO3Xkm3sfO6Ywt8IOtLGRGSyvaYyBnclZ_7z1uXYLdMGTa_G8k1dFpaiEeBt4ukey5hMgZwcCtY4FgZJMI5S3Z9ObfmpMT0dz6LBlahGHMMQitqvZVxA4W5evtTvprEWYybMWonPENobAE5KgGSB6iHZUkDBsopnlOyZHMkbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b902abcc5.mp4?token=JBA5LDoC4fiwEtf5IF1L-bn7clhC7Kja7Xev2Ayz_9kZ7F5PsqIsTvcH4tRfI39864Oe_q3XTSjZVVSVvCBhqrJzPJw9GBYtaOoCS2vGK8nWwkBlQa1ij68MT-UDo3LYmYlw-P4xfNpvqE3-Pox5sZO2EUy9cQthjBldNavqZBFkknO3Xkm3sfO6Ywt8IOtLGRGSyvaYyBnclZ_7z1uXYLdMGTa_G8k1dFpaiEeBt4ukey5hMgZwcCtY4FgZJMI5S3Z9ObfmpMT0dz6LBlahGHMMQitqvZVxA4W5evtTvprEWYybMWonPENobAE5KgGSB6iHZUkDBsopnlOyZHMkbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
8 سیو دیدنی وزینیا گلر کیپ ورد در بازی مقابل آرژانتین؛ پبجش از 18 میلیون به 20 میلیون رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/persiana_Soccer/26627" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26626">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jHiZE577-1Q5elnLOoj7bhVj5MZ0FVc39UE8ysgTIsdeTXARepj-8R0G5Q6Srgxv2MFnBNq3kqC2NapDVXylJwhU2KzWTqvUshvB9Wxph1xWMB-AcLXYUOlX_NrHieK4qFRImM2WBbDLdwwBYVGSpk8VJiRMR7x1IexOr4_4jORE4MzJ9-oXke0lzrkykZLxuuZXBaJB-9VvtXu3qjwn2KW-zCV41qHveL35Nt9TXFPZrIm5bIq6KOLCxFQGBwFez0BjMc5tSjkLfYDdNuoEk9SbIBbCE7-2Tor4BQJIE0TPqg_TZY3nOFOkHt0rfDPeTQ0awtwwmZ_mBHLQXvhTPCxGbFIopvWfGJVfOZjT2WTfQA5fCb6YkGa_i3YSf1sLJXz-3tvOjOtJF5DztiWZ6cCOuiaWlSaYJL46AY6vqp3oXHK7Nz_5kLTu6TXQnS1dkHDaABM6mYB1OACiCa0fwWlsL90Hu5dFYhqYhvi4LMFaccmwOkVy6KxJDFBdqxWpY8HkXphMcrjidHXk2PVUIlpGzvh78571I-9BnoGTxg0f-bC7NaG6hhcg7TnFKYfGRRYFFJWdjWDVmRyCWYtoomChW28Me7OOnwgICl52FbBEpByloPmJy-wcGPc5IhD4eKv6CXDdYMruspohN7j2ocp5KTtkCFynn5LbK-zdLHM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3df251c94b.mp4?token=jHiZE577-1Q5elnLOoj7bhVj5MZ0FVc39UE8ysgTIsdeTXARepj-8R0G5Q6Srgxv2MFnBNq3kqC2NapDVXylJwhU2KzWTqvUshvB9Wxph1xWMB-AcLXYUOlX_NrHieK4qFRImM2WBbDLdwwBYVGSpk8VJiRMR7x1IexOr4_4jORE4MzJ9-oXke0lzrkykZLxuuZXBaJB-9VvtXu3qjwn2KW-zCV41qHveL35Nt9TXFPZrIm5bIq6KOLCxFQGBwFez0BjMc5tSjkLfYDdNuoEk9SbIBbCE7-2Tor4BQJIE0TPqg_TZY3nOFOkHt0rfDPeTQ0awtwwmZ_mBHLQXvhTPCxGbFIopvWfGJVfOZjT2WTfQA5fCb6YkGa_i3YSf1sLJXz-3tvOjOtJF5DztiWZ6cCOuiaWlSaYJL46AY6vqp3oXHK7Nz_5kLTu6TXQnS1dkHDaABM6mYB1OACiCa0fwWlsL90Hu5dFYhqYhvi4LMFaccmwOkVy6KxJDFBdqxWpY8HkXphMcrjidHXk2PVUIlpGzvh78571I-9BnoGTxg0f-bC7NaG6hhcg7TnFKYfGRRYFFJWdjWDVmRyCWYtoomChW28Me7OOnwgICl52FbBEpByloPmJy-wcGPc5IhD4eKv6CXDdYMruspohN7j2ocp5KTtkCFynn5LbK-zdLHM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
تیم ملی والیبال زنان ترکیه با برتری سه بر یک مقابل تیم ملی برزیل قهرمان لیگ ملت های والیبال زنان شدند. زهراگونیش‌بهترین‌بازیکن تورنمنت شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/persiana_Soccer/26626" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26625">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzotovBjT34t-aIk_r6gnOhePPAC8jeh0PvjHQBDMatCcZoi9gzJI99kgW53K044UOOTBA2AtZw4vatwB12HyhwdJhXJl-LVvmnhd1KU6uJoHk4cThLy4NmJgdD4Ov-b0VPwOV-xarKH-3OEyiailM_mQJ7mnqJ2A8TvOlgpAtK_iJZtSl_OHqNBowxCCL188xKGY8-rnsP6tmNJBXd_Y0SdVZhgfEUE3CMifzs48U_PHGGB__5F9a4c1ACkyBWRX2ErIQ9oBx7szxgzLa2fEKAZqoAgd8CDH3S4v2AR6rb8z5SRANU5X09s0y6XVJQS8KpRxqvqKogTuNo79zuk5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🐉
میخوای به راحتی از فوتبال و باقی ورزش ها کسب درامد کنی؟!
⚠️
پس همین الان وارد کانال
Evil Bet
شو
چون بهت اموزش میده چطور دلاری پول دربیاری
❗️
💵
اینجا میتونی روزانه درامد داشته باشی و سرمایت چندبرابر کنی
👍
آدرس عضویت کانال vip:
https://t.me/+TmGWkUYH_8c0OWZk
https://t.me/+TmGWkUYH_8c0OWZk</div>
<div class="tg-footer">👁️ 57.7K · <a href="https://t.me/persiana_Soccer/26625" target="_blank">📅 18:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26624">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QWy_O59b_3K9xV7109V9nRTheDXV9d5KeH02TKceh_B4BnCpom5TUtHxPxAqy0YnSqD2wnmwOXTGIOLf9KDFAnU71MMk06yJcBsa4IiH1_RRi8RNlbtWmIGBWNUAW_nK5VQfsL9QbMOF2iqBgc-08_vayzme-k_sMWAkAOiCXb7AcV-0qVVf5C_HjGKElDTOMU9V_Gb0kE7COLB3bltpfR6vnc8ud0KdhjJ7G1x-befsfiTbJfB5pQTvjFzAI9UI4OZEoPVRLMR4rttMFg9srShB_OCOrPMf9HE4zwNzBcas1kWwQABV3390fU-7c2EDT7e3quUzqaAkiQcCev5Jow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🔵
#مهم؛ اینکه‌بعضی‌کانال‌ها میگن زندی مدیر عامل باشگاه نساجی‌پول‌پاشی کرده که با قیمت بالا تری دانیال‌ایری‌وکسری‌طاهری‌رو به پرسپولیس بده واقعاصحت‌نداره. زندی‌بارها تو جلسات با مدیرعامل پرسپولیس حاضر شد و گفت حتی حاضره با همون رقمی‌که طاهری رو از روس‌ها گرفت…</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/persiana_Soccer/26624" target="_blank">📅 18:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26623">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mYRktDD5v9578o5e4KqpvG1zqb0WESRzLEkRO1z7gjaFrjiYMftqDONLhKwSLYvJepNTqNRSDP2x0iVYwB86_-P90lt3Ksj_p3qUABkAC0qOoFrVK8gtFY9LBN1LbdHgffPFcs4udCpDIWtm7e5XUEQ0K7f4Hum3VF1jH2BoBAkmDIUFrMgG7JCiYBFRbUA-2iHPMgx6Goe8qWxllL5SLxufSlf7NDLizaZfUxxwO50uO2Gep8KJ49QjnfGd7WbHH8JZLd0K3jLLLroAqG1IE14zKlpgQEYX9zwJSVqoWVtpVtbzXGnon-Jqj60RyrE5-T9rR3lPROp3wF0Sk3u5aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/persiana_Soccer/26623" target="_blank">📅 17:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26622">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NLfFnr1ZcEE7avFwro0yA0AD2XwpEHz0Wq7qkxfAg3YUwPSzRJTkeImR9PZylTgfvvqTLikVljaJ5Pybe5gNnQjpGeXUuOztxyxBDvrqjvqLDg7nFtIC2jQGKV-oTBAlgwKhwHGCNsYUxZcyv_t0XFwb3YySJsbiiGFAe8ULof4R4G59c2xWIKIbhH9YwDi3cvZMOtIhnStLxIS9c3i-KN_69WfnawX5v4W3nSGg4g3OtVo9HCg3eN9uMZQpu63KLy9p8eKCx2QyGBcXNJWUqOZKnMaAqTdl9anoUif89Xzk0WLGc8eTdPQYqS0LV8HqsyZgWHtC9rm6Ieg5MsfQNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بااعلام فابریزیو رومانو و علی رغم شدید مایکل اولیسه به پیوستن به‌رئال‌مادرید؛ این ستاره فرانسوی این فصل هم دربایرن‌مونیخ موندنی شد اما تابستون سال بعد به احتمال زیاد این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/persiana_Soccer/26622" target="_blank">📅 17:25 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26621">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BiZ9z9nPPhq2cZKImRFZQxeN0GwT_F3i1xg0rWEa1XpPO64XlUdBBbPcllcs82lcuteCy4IvlA8omTiPiL-XKHHinM9aabRMXcNuwQ9MzCmRp03xlJ5f6DMWp9T-0jk2zaEUOLbzkLqEgVKZNI7eTaK98QOuvzU8tmD12TdpRMpjlGQlL1MxHZAdFbajmDxkPObnahDZT_D_yCc6mkdgMVdfssS0qWQbzLopOoE-AUW8gC50HE-YYdsAzStx3wPJPfbckg1jnm5gFV31Fp1Aanutv7jzDza-J4VaAGnArRPtAWf3DaVeRCO-_Q7T28kaEpBi1vbk62IIMYdxwSZCcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇵🇹
🇵🇹
فرناندو سانتوس‌سرمربی‌سابق تیم ملی پرتغال:
حقیقتا من هنوز از این‌که رونالدو رو در جام جهانی 2022نیمکت‌نشین‌کردم پشیمونم. ازاون زمان تاالان‌باکریس صحبت نکردم و رابطه‌خوبی نداشتیم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/persiana_Soccer/26621" target="_blank">📅 17:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26619">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1a0b40618.mp4?token=U1CtHB2rzlvbXv6haPVyjetWFOKZcAt9EmyOXiYeRWrgFgFodxvdKchnRlS7QjAAoQvDhEQoOV3F7oK-QRTxGj2t-qwKy62UhS000whKVTiETSK8Y9FF7duu-joA3pszUPSYpLg7WU-cQ4_xUm9ByIG0KljrBSvAZTFCIj5Lf4XyBBHOKnOuipFypKYX_og4o1k_FeLjG0mgOlZk0FqbEpcMnBj5uVD_NH23qgS1QGHixhSUHfwKUqBHgHm8P0Bc1LFM0a1cJyPLqF-JGE2sDwHzbc6tySGgEdqspdC6dG0PmfXMVi6v9kX-k1YhWVs17D3fj7CS4ZCmjCjeeuSt9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
تاتیانا دوس‌ دختر هکتور فورت ستاره جوان بارسلونا و حامی تیم ملی اسپانیا در جام‌ جهانی 2026؛ گفته چه آرژانتین چه انگلیس بیان فینال قطعا اسپانیایی‌ها توان‌شکست دادنش رو دارند.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26619" target="_blank">📅 16:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26618">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bT1o0hkAGDlKcjGAjm4TJQcHCS9hR92cbuCECoJOJf1t7vhO8DnCh2Jm1CJap7ZLihllT3Jqdz_8kKtD-jcOo4my1pCjeUASuV7KpFALFnOE0h3f3n5BvecH6haxmv21yZtiI0qpaz8NIW2S0PXWgn6GEwkvepLobI2K-Su--upDXZalSn8OWSO2c4NlMLh2WKWRpwULNT7aZtZcnrhg1gjYG0wGq7DZZX86hKxDTDLEbfImZB5JfTOx9KIHnwaoXGy5eVu4hkF0lknYl8-2I5AQdYDqMx5BDSCMVcLOhdJP167qM35MJFS6liSET2PMrU0feRDBMXhk-ld_dvS6bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26618" target="_blank">📅 16:38 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26617">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7JkPWEQNBbaSqlBUPHD17VnaczY4XWzoP2YbWqc_MXzDp1J5pWY07yfzId7CEdbbCUilqIktXNY2DIZJbbrpP74qA47VJKOR3ohLukKs4UC0OSCGYbtpAhjkFDQOL0Q406djUOjkQBM8WgyMq9fWXi6zRDbxfpc3IQ3uzPf5uvMgWSqyUmdv3ewmdIKUDaZiVVBcONkhg6Xv9_hPR3R7bHXdtckLDZ4pxwIj1hkkFaDyqqLsfJb9OQZWEBu62FQNoYMF6-UynMa5Mn5YmmkRlsb14vKbNjCKLrg10SZuvkYCyfxYqPBg1jhm3QRnML6KtvvgxbMXSwGJM2aohII4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🇮🇷
#اختصاصی‌پرشیانا #فوری؛ محمد قربانی ستاره الوحده‌امارات‌امروزظهرجلسه‌ای یک ساعته با منصور عظیمی مشاورمحمدرضازنوزی و مسئول نقل و انتقالات تراکتور درهتل‌المپیک تهران داشته و برای عقدقرار داد به مدت سه‌فصل با تیم‌تراکتور به توافق کامل رسید. عظیمی به قربانی…</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/persiana_Soccer/26617" target="_blank">📅 16:27 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26616">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l7YbzQJa88ZpYM_8N-msfDwKqHpT9wsaa-kW__vLCJytTYsEHHF97cN0ka-ZyT7TYpfqO7X-yqdoV9rtT2C3w4SAo8XsCcgIfOJmbwBZJy9FnM_yM0dxi-pIU0BsLon5jZZEWqbso-tY3VVB0Fp7eVNzgp3CgDWsFemr2N1ZahJ3mu2MAg-VfloalZZHmzP-ZtknzOWOQ8NUWkPEAedWc-dCk9Y1ZaNTuSlcnN0_5ReeLOneal3lFjb1bp_5tOkXBhqXDN1Xuj_KixAHVXgbEfpJpCYZcGHWqlihTs1FymTe37QEUZAEH5D9Mn--JCYV44wMSOoYlfgVozlQe_f-3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف…</div>
<div class="tg-footer">👁️ 60.6K · <a href="https://t.me/persiana_Soccer/26616" target="_blank">📅 16:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26615">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kId3KWKG8AHgFyB-C10UruTGGYwFxIEBuBAXmKUXJ_VqjEr2r0oB00Czs5uoZawZ2oLTGOGPGgnr25wyEVU7NQHVebanRsPqLKd-sqnR2htq5lZgqqYIOLCc5nKAykZVV5duauPuxCIJs1G_G7QsDkxQc4XVKK0aqC4BcKhWGM9or0zzjk9W7PMz2tea2pD-FE35Mn7T5_Wtl847eU73nFTR96Ew1MJeYRsb2EYv3C544Ph_qrEzOL_5nMIzTmJQZcp1_dWvCgv4-OaaGk8CjSNbnzzmyxDpIIYPw509F1i9LWEkgU6bXeEDDTqXpJ3m6ACjXGc1GP1vOR1hPtqJ5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
🔵
طبق اخبار دریافتی رسانه پرشیانا
؛ باشگاه پاختاکور ساعاتی‌قبل با مدیریت تراکتور برای جذب خامروبکوف‌به‌ارزش 800 هزار دلار به توافق رسید.
‼️
درحالیکه مدیریت تیم تراکتور با پرداخت رقم 2 میلیون دلار برای رضایت نامه محمد قربانی مخالفت کرده‌بودحالا بافروش خامروبکوف بزودی برای جذب ستاره 23 ساله باشگاه الوحده اقدام خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/persiana_Soccer/26615" target="_blank">📅 16:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26614">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OmlPUtD6opl8dioWO-jewefokaxpost_TFb1dGZZ-Bx8ZXUHqtiHt4JqF9LeD5dFYFIOFf-F9ORdvi8s4PMP5MdX34Dw6G7g9iLAKsgE3v3U70qthS_vv0HcrXdk9iG8tte5oZJ9jE5y1CjalnnifhmX5kxiPhksoabnxwNOG2XBoX36HZ8CZ9PrKC1Tf9wFCyitcBHHLDjPw1U8j1-saBzw-bjgm7quY2WZJaE2LWaGG6pYizVxem25dVo-TXAD8xzoV8doJ5XX0b_QtBEOgX-f0kLpfwfdGn5I1ok9xihM7kj5HzIYO7k3Nnl0g4RLozMo3w1EusuoPLdwxslX1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26614" target="_blank">📅 16:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26613">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HtPeD925KG1CzpVHHshnVxp7dWaaI_chw2tcQbP9cRB68mORzyELVwhPRSzeB-Eb9JVylsHEG0oF1kPNcqpCf0rQXT27x_5fFKS0y3jhICcfMvGl_mjzYBk-5r4IWMd9OemTvt1MqjDKgq0Upe5147XNC9QfB0t_QfY0VM9tL-4LUkr6oAAOAfOuG-ZZDY6baYYwMSnf8rcx1q36Lvv40jzYTAu1wWJOauF7cT79H0y1X__yAwIHvVUaYveiWpu7K_QHa_xPFCjlX8fKyObrBao3RLxhSh4EdezMRaIRMycz3TZzeKdCdnxyPfNfAmb_tqS1l45dZPu5RaaWgg9EQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
👤
طبق اخبار دریافتی رسانه پرشیانا
؛ پس از کش‌وقوس های فراوان و مذاکرات با باشگاه های لیگ برتر؛ دقایقی قبل جواد نکونام با مدیران ایران خودرو برای عقد قرارداد یکساله با پیکان به توافق رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/persiana_Soccer/26613" target="_blank">📅 15:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26612">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QY67wZ0KA33pBTv_Vkc0jBBkQHEaZf6xS2GWD-4YeSDxOSivjIhmdXfBg7nd6FzfT5glWNKng480hNqDQWSOr_EC3GGETqJQSN0-K2Bahj0Zk5Iz1PcJvjKhSLqUyDctAxRw8X47r2GmiaAXfyKp7NZXWWNwzZm8_MeTHjrxdqLPWBor-2TanmcHfK8kPsdvHCCQuJ91iN7JPd5vaKxgBsJGternCVqqL873KHia3SzWAPv-Wuu3TPsO8MhMsjyKrdEDK2cfRJJ8apXhsBRj_Zo-jN2xYeEU7GJsJNgham9MnrwHkt5QnPn71s5DTFTZq2RopJ1ywv2awDAbeNp0dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
یان دیومانده ستاره جدید رئال مادرید بعد از پیوستن به این تیم این تصاویر رو منتشر کرد تا نشون بده از بچگی فن رئال و رونالدو بوده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/persiana_Soccer/26612" target="_blank">📅 15:04 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26611">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sGhM6RyhMrP_Gm8BUv4b0mxtWaxAb-UrzlEsJSr-G7lT0FF8LE5lpXwC0ronCifpys-JqY_LmbWfT3IIGFCyat6owxASFwhaFOkA0tL1gGyUOrmRc17DGEQGAIL-YB3igeBVkjIHU3vnbCSpKQUh0d3c3kn_C6LErj3Rt_0OS1F2jO9ukLMo7_0BbEtQmwYD718JWizDPawlNe73GrHEsrsPMVvepWnIzs314S31uQkSe6zXQcDgULvhVtLz49zN9rvpltPMS0C8bexKKPhFcODLavj7opFJuuxiXDQbXvFsYOhrdNg4zFKKdYpLRlnxxhSrahYH2GJEHyckWugJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبر اختصاصی 14 روز پیش پرشیانا؛ با اعلام‌باشگاه‌پرسپولیس قرارداد محمد امین کاظمیان توافقی‌ فسخ‌شد. امین کاظمیان پارسال در شرایطی به پرسپولیس اومد که لقب فوق ستاره به او دادند.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/persiana_Soccer/26611" target="_blank">📅 14:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26610">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mU1d26vz4PIvI2j28BTm6qT1ZcM5RaGu4WqnfeymiCVjDraSJYgEmCP4AEA6QaERSqY0gtZUV9-trxjwNcWMCGr9gP7n37FdXG6zZgfYf8Zg4QoG82svmHbAaT2OmPBJ0uq2OBaDekDY2VIrUjeGB2l6hBe6EYAa4dn35CuaBoOZ6O_a4sAcp-plCdMTgXPevVC_T7wEXIne5OyszmNFezCPL5rh5vMXLzHxS-GUnprWq1-suVaVR8lLjrYl182ThanxNDX-bXeMMK-8FBo2LaSH9HE1piLB7Hdwybuss8dT3aEMv6y9pEocBQGaR9rHFS2GCemoAsntqXffFtMEew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
فرصت 24 ساعته نساجی به پرسپولیس! اگرپول ندهید دو بازیکن راهی استقلال میشوند!
‼️
علی تاجرنیا رئیس هیات مدیره باشگاه استقلال امروز ساعت 11:00 باشهاب زندی مدیرعامل باشگاه نساجی تماس میگیره و به او اعلام میکنه که حاضره رقم رضایت نامه کسری طاهری و دانیال ایری…</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/persiana_Soccer/26610" target="_blank">📅 14:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26609">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=iKJw47fdu6cuehD80d-hovOLruPU5GNZp9ODoZPI0BwkKFSW2BAVWsEk-65Er3bK8QG5WsnL6LpKqQwcslngyrqrJcnCxcik_hYARNtX8HuDCEoJjTN9O9l4afGd74qR5VXmODUZW3w4Sa17EsbLMxJSBQaMegXmozrn4HUFXwzokSIbDAMzaYYk1XkpotNyVTwsF_uKDSX8ITwZzWybzaIMqOKWmqNAFLsIfJN_TpGlAjJXGGmNk_5RmZCM5k9iHf_5rbU5Chiphwr-uwV4nixT_l0N8BB2z-4n8cIh-Pj4m4dSqVtZbFdDrqy7UmmG8WVCD-ym49w7vrtvGRnYzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b74811f44.mp4?token=iKJw47fdu6cuehD80d-hovOLruPU5GNZp9ODoZPI0BwkKFSW2BAVWsEk-65Er3bK8QG5WsnL6LpKqQwcslngyrqrJcnCxcik_hYARNtX8HuDCEoJjTN9O9l4afGd74qR5VXmODUZW3w4Sa17EsbLMxJSBQaMegXmozrn4HUFXwzokSIbDAMzaYYk1XkpotNyVTwsF_uKDSX8ITwZzWybzaIMqOKWmqNAFLsIfJN_TpGlAjJXGGmNk_5RmZCM5k9iHf_5rbU5Chiphwr-uwV4nixT_l0N8BB2z-4n8cIh-Pj4m4dSqVtZbFdDrqy7UmmG8WVCD-ym49w7vrtvGRnYzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✅
پوستر باشگاه آث میلان برای روبن آموریم سر مربی جدید روسونری؛ قرارداد سه ساله امضا شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26609" target="_blank">📅 14:26 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26608">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZLQrEjAVzM9R8LBugfv_YAJiv-bE8LgpWKZX1QCBz8yAM2VQxtxGUtXqGXkrsq907VVxLxZZ_obToDWYwSNzDuiLDRJLabYYODCxXBfnd5uj9qSQUAmwDKdtJf7t6ku7Z1Q4uQut8r840nkuAQtp3MWESfXX4GWisUqMPadpE9agxXQs6R9d5fQkc4-fWK5sItcqE1RoHBo9lDq5BbVc8MGSAiKwbNWN10kMrglI17EOlX49SnUwxCm6Q4_u9rpnpcdaAfoFXeLNh83_UzLfXGM8dVbyUPktb3gAptDL_1PNZolY0Ft0stalybiDn06KxdJNZupIZVhI8wiDyl8eiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26608" target="_blank">📅 14:11 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26607">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MQJxyI-uzPk2EwofNxMewrIn02CGtHL47QijAHDR-KzI24vDSZEWWS1xhTONNxJBxmenCcBCgkDv5T4SbS_w73BiQAvU36tl9ZUfVhMLigq19eQ_4bNYdgv68TJYdM9naRZXzxNBvSshTfJf-tBBzkLS1lCkzx5FhbhFY6k6fYN1w4xZXZmLDeMJxIKrif-RMJtZ71AkX2I45avAUMfwP2C0HaF8AXp8rlU0t1k_zrSpRRhmV4IUq8k_xu3u03EKFuWeRMuC5ngb_KqVp15Eb_OHwDAtoxG42za74USyOud_ABCvXFCA6QNOyxrEdaxRjGBU645Oz47t94a14QvoRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جایگاه لیگ‌ های آسیایی از نگاه Opta Power Rankings؛لیگ‌برتر جام خلیج فارس ایران در رتبه پنجم قاره آسیا و 61 ام جهان قرار گرفت.
⚪️
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/persiana_Soccer/26607" target="_blank">📅 14:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26606">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UUe_Ote0El_B__dWY3TUqsVEDt0sqU3gPKikyFdAxO8tUsIwCaAC2ni6hXKUYoH-7Pp_Ce5cG8wlqvFL_hgReqNu77748n0F0KUBRg04LrHBhagDXPGO3Yb6dLbtm4XUMgJqIkW-X1dVlrhBSIY954bdicnElX35iJ7XAGsqejezEFf4JVDhgQwFyeGscKe_uPAhE0wmjwzNMLxH7zNNNgGcMg9Ck33P-uCIALmC1HUdz6lvI87TNeakdcxNR0I6Z0LYFwPRkQiMvfhowsjsNZvF8xP8OjBg8ClUzccq1sI-n8ZwE6CDsF2XZ-_KL6j6EzoaVzoV9QYwe4eIHBgw2w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌شنیده‌های‌پرشیانا؛ باشگاه نساجی مازندران با هومن ربیع زاده مدافع‌میانی 27 ساله‌تیم شمس‌آذر به توافق رسیده و این بازیکن‌جانشین دانیال ایری در این‌تیم خواهد شد. جالبه‌بدونید که ربیع زاده با اینکه مدافع آخره پارسال در لیگ برتر شش گل زده بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/persiana_Soccer/26606" target="_blank">📅 13:42 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26605">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/crTTtWV442KiCb46rjFncZgK_Emi-GueMV6FYVT-jUEMHpOl6zr-yfrsG8Pg3Rbh7zwVxWeom6fSTWyoFgULrUfnY7bTAkODGeAcyDkVD0LiWEZYHQvpNyhzCpHW6hoYY7OtJbPi4pqF86E7NjeP-keDMmcC4Kp2EHz_tnhL1Ge7oDQF2nc5TroCLWeT12vf-RMDNpogMwtVaVnqk29YJ1DnF96RPAe6n4E_i07pzCafKDug8i3f4nQMQjFP4M5Ddfvo8QozPzqS2NnoevflK-EIXwd35HamWuC6x9xmtIl8zTx35hSK44EpGiqifNfN4hYStWw4ChuD616jE78ACw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
🟠
فوتبال ایران فوق العاده‌ست
؛ داوود نوشی صوفیانی پری روز رفت باشگاه مس شهر بانک پیش پرداختی گرفت و رونمایی شد. دیشب پول رو پس داد و امروز با ذوب آهن اصفهان تمدید کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26605" target="_blank">📅 13:36 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26604">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZzReZMA70PWsuVaFpbSayvOuR6ZYetq2muUwPsKkSYUNZ9sROzWR7Iub-d2_6xjXH8vi8d-dnWRePEAz26C03eLW99l9sXJofit2vsgKpp1sulLq_-kKM9wX5gDBxsCwRppmCpgTtsXtEDtWGOsWSX8L84sgCz29PEG2fYta4m5Thgr1ZOoF7usRjEgLVmv12qckYKSP2IAGEm4ajr98MfLTOKcHeb8hO8Df2WP0h-EuKVhUPwnepEHQx-gdv_XzYNeIaicsJTrc_gSbWcXhP-zOvBqFmNXD_fr38g4zTUDfSL8vzaNYjeZWul_l4Dd346H0GD_sMCkRps9XWY-y8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌گفته وکیل‌ایتالیایی‌باشگاه استقلال؛ ظرف امروز و فردا دادگاه‌عالی‌ورزش CAS رای نهایی خود رادرباره پنجره‌آبی‌پوشان‌خواهدداد. یا پنجره رو بازی میکنه یا بسته میمونه تا نقل‌وانتقالات زمستون.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26604" target="_blank">📅 13:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26603">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=Mdna8qr9QqKKjCgQ-RsY2Iq9S4-fVnEnTY1VyB4ICdLkmAvOD8RuhqVTnKNjcVE191oI6vSIJM4BWTTIL1TIE5dnWm3WfkWoCqEtf3aivkzBzUzn0roQo7dK0UKeaA93sbNfd4MKwPkc_wVo_dtDnvVD9i95A4ySqzF9UFn8QjQfRV_pKKyNCDKqfhdcyfNpN-qNKpAFLuv1KPQs0Rrh4W3nkyJLfDTG2oM0g6yC0_YHVmxxC3nse_mC1k7PxO-fMjLs3gcdWUGGbM7GVy5mUBR6x5Ir_-1xOIude16Zl76Gk6EhfepUX4susKlZX86ximjLr90sOp0BDABiEF6dcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0cb160c99.mp4?token=Mdna8qr9QqKKjCgQ-RsY2Iq9S4-fVnEnTY1VyB4ICdLkmAvOD8RuhqVTnKNjcVE191oI6vSIJM4BWTTIL1TIE5dnWm3WfkWoCqEtf3aivkzBzUzn0roQo7dK0UKeaA93sbNfd4MKwPkc_wVo_dtDnvVD9i95A4ySqzF9UFn8QjQfRV_pKKyNCDKqfhdcyfNpN-qNKpAFLuv1KPQs0Rrh4W3nkyJLfDTG2oM0g6yC0_YHVmxxC3nse_mC1k7PxO-fMjLs3gcdWUGGbM7GVy5mUBR6x5Ir_-1xOIude16Zl76Gk6EhfepUX4susKlZX86ximjLr90sOp0BDABiEF6dcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
علاقه بسیار شدید غزاله اکرمی بازیگر سینما و تلویزیون به مهاجم سابق استقلال: غلامرضا عنایتی ستاره سابق استقلال کراش دوران نوجوانی‌ام بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26603" target="_blank">📅 12:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26602">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u4kKr4_XhI3F4vAr-g2ndjkY6iQVAT9uz8ltkcaxRQTRS85_I_t1BN95MgLYQfzDHiqN2rYv7yEPqO-U1kRK_S-RsfT6T6P5SmWa4lW2eXDGvjD8pEFmsH61QW1EwRi44fgOOamxkGOWH5a4dxmuSofyyeQ0lkh2F0AWxVNc10M4zS_KLvp-QA-n6XEEmZdNsOZ1yGfChAPUhuyD67Tg29pBOCJuvlEtjH0z_NBxX7_mLia00AYDsIDjhNYEKsfe46DurbFoMjSd2nve5Hl5iDMNQb0AaEfVKRu6RfrtO2QuiUBWK_f-HJX0QtISa9fSjd0UsAVXArOfHrMYu-lWbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
ویدیویی‌خاطره‌ای‌انگیز ازسوپرگل‌های لئو مسی از روی ضربات ایستگاهی در دوران حضور در بارسا.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/persiana_Soccer/26602" target="_blank">📅 12:52 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26601">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQacSXssNOrVfPydnAF1djyKbanhEB4Ac-mjGNVK57tW1C7eTPNbUTI5skP2ojpw8nS6lGMa3Msw2q-emo7xAvgNgRQM4YSntxHZgzKXV5MI8EsX5I-L2oXyhyMY_eTeCXLAK3V4XdsLpIq0ugCrq7SE-PM8eZdfcCYpX_P3oIlsOkmzFVi8GSQ-SIGk5srMTa8TTbZGdMiYx6SYIaViRQi-Ew8i9ly49a3KKdrzefRdqZNwNGkuOhPm9d4Xm6W4rlCOyhUFFgMgk7ZZAyuqbd-hnxOm7KO3ph7WGokJ1hvGtO_rUMpDw6gUaTPaXC7wO72TIm7e0S9XHDsUP0DNzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #فوری؛باشگاه استقلال باردیگر به منیر الحدادی فوق‌ستاره سابق خود تماس گرفته و به او اطمینان خاطر داده که بهترین شرایط برای او و خانواده‌اش در تهران فراهم خواهند کرد و هیچ مشکلی برای او خانواده اش پیش نخواهد آمد‌. بایستی صبر کرد و دید منیر…</div>
<div class="tg-footer">👁️ 60.7K · <a href="https://t.me/persiana_Soccer/26601" target="_blank">📅 12:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26600">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fm7PBMv-Dm18NXq1VH7YkJnOxjgvdpcpijj8m6PVi2p6hegEQxvxhIGZelU1uTePXRbu915mJ3sVXmdM03OWNC74jKR19_3ICWJ_4OQIqMzXKlyR8oj32vLahvxa7hoaaZhQDSxmMtDjtf29i66v3YDvNej-uNYhcn9bGKvUPA5CuIa5aS_DUIhIr_Vo7zzdZWLL-D63ZZWNxrIk9InRGWmpy42XRrmcDYgFE3a_V-XkWBWN2TspQ7Au5A_kztP7B-7a9qsgMm5EA6rZ-gK_waye7ta1t9PbUcZjnyeyJjaf789ccMZ1nHk-D8iVxBdY8WyeWEKTKwqG5eLy2XQLKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رئیس جمهور چک در اقدامی جالب و در حمایت ازتمام عکاسان به عکاسی مسابقات فرمول یک رفته.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26600" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26599">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i1nzKOyU6Aqnn4_mjsQot-R1KfH034Nu50cytUAIZ8M9TZmBQLSblyr_CcZW7u0he1CdD-8QGnpNG54ult8qsx70eZtIYtAN9yATcnApIAgtUYGqvPeo4Yn8fJLkZLcqTB7hJ6BsuStzA-hsv7b-c_UYSXWNhUIax5v_Q6HcU4P3t9WMDt6ZDybEa3B15yjNA03W_ZrfyBZ2lniQR9PFfbcQuOC7y-dFuZ7w9DX1BBgAX_SAmhjRlYOfdZAg4822BtDPmWfT7vs_pi_O9L_anjMZGDBkVwCCFfvcuBuy3xs9cvGIXPN-2BqNIJ1G32OisrE2ZkWvpM_Mus4ig6Afng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/persiana_Soccer/26599" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26598">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKvaG8H1jBZ1DywNkflRAUPxHY3seejWcN53CxQcqgP6-EcRjfNrdsGMsv9Wleb2F9-Yno4ZUBxergeCogkXDkAlVixZ3EdxoDtJQvuvQl9RIgmr_0x02Z1Kx6yDa4ohedSC12TnyU4hKtr1dayO6DftLMZ_V9ONo_MF76dnJHvON1SVFplPHKoYNoFgaUmHDqGMaYDNHeCwJzry3gEbVRFd6z40Q5T4NkmjbmFaKjrP8f2HC2JCS1IaedBdtTbAfjerNfwoKLsl0CssHnrBnwUHqAENHEpeYAUioA2hXVo66gPwGzmNNNbSgDiob2r5IdaAU9g7ix1hmGD7cTjg_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
پیشبینی در سایت بین المللی ریتزوبت
1️⃣
2️⃣
3️⃣
4️⃣
1️⃣
2️⃣
3️⃣
1️⃣
2️⃣
3️⃣
4️⃣
⚡️
فرآیند ثبت نام ساده و آسان
⚡️
آپشن های متنوع با ضریب بالا
⚡️
امکان شارژ حساب با کارت بانکی
⚡️
شرطبندی بدون لیمیت روزانه
♠️
کازینو آنلاین شبانه روزی
⚡️
پشتیبانی از 61 زبان
🎰
بونوس 100% اولین واریز
⚽️
بونوس 100% ورزشی یکشنبه ها
📲
اپلیکیشن موبایل برای اندروید
🌐
http://ejh7qy8d.lol/L?tag=d_4828009m_69797c_&site=4828009&ad=69797
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی ورزشی
⚡️
@Ritzobets_official</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/persiana_Soccer/26598" target="_blank">📅 12:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26597">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i2ejXdfnlsext5Xi9whC8Ydd7aTCLdvIH4iehIclJdNWV3BNpWgOoMA7K0yBy9vSsqezMj5YqRFPiPlUaNqY-O6FOq5MCFTGpe__SG4fCNuN_snR7aR_y9kEVp1kXUcpqgz6ZywAbLq81shFykaX4B6qXG80OZf5GuZH5mgCZ_DoWk7bMFMfMdfscPkn6vZQX7r2sjHMJzXoUgRh-fNHwGWwoIypP5YkS6XPg12fj7V948LEhwwFZ62uZ2LqsSvm7TJIz9yfwi9IjoXZSxvelpq1LuJczl4Gj9FjJvJ9AEJEz0nKVnFeuGbOcyqaKQbHCznog8tbVFg5g1tbBjMvtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نشریه‌گاتزتامدعی‌شده که آندره‌آ پیرلو درگیر یک پرونده شرط‌بندی درروسیه‌شده و به احتمال فراوان فدراسیون فوتبال ایتالیا قید توافق با او رو میزنه و روبرتو مانچینی پرافتخار سرمربی آتزوزی میشود.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/persiana_Soccer/26597" target="_blank">📅 12:06 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26596">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=q9ORuyjWhUCFKnEw-e23pZHb20WlLZyZU8oyFtxRsxISsxVoUs4dAVXBJdihIZR0f0wyISzxJc0tqPeBBFrlGYaKoRULYWnt0mNpSySD111gGDBOi3DH6-6CJZnInEq_5D11LGs8DyDJzrIrv2iBM6sZnqduOn-R9LxopdMa7D9dy0agt3xBwL37JgSusRBLd8jWropePVrnnocMRM_xNkmjDZ30uYJb84CGdE2iVLrSDcSBVS8wHCOR0EKgrR0gU8FLLyycw6UxJA6Na1Rqg1HL2jz6hNIrIyf7QEuI-NPP9Z4mQRzBYHoRwJV-r-Ij1_6wRsJOHGcGhua_I75kJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a36a095cf.mp4?token=q9ORuyjWhUCFKnEw-e23pZHb20WlLZyZU8oyFtxRsxISsxVoUs4dAVXBJdihIZR0f0wyISzxJc0tqPeBBFrlGYaKoRULYWnt0mNpSySD111gGDBOi3DH6-6CJZnInEq_5D11LGs8DyDJzrIrv2iBM6sZnqduOn-R9LxopdMa7D9dy0agt3xBwL37JgSusRBLd8jWropePVrnnocMRM_xNkmjDZ30uYJb84CGdE2iVLrSDcSBVS8wHCOR0EKgrR0gU8FLLyycw6UxJA6Na1Rqg1HL2jz6hNIrIyf7QEuI-NPP9Z4mQRzBYHoRwJV-r-Ij1_6wRsJOHGcGhua_I75kJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
ویدیویی از تمام‌کنندگی محشر لوئیز سوارز فوق ستاره سابق بارسا؛ یکی از بهترین مهاجم‌های تاریخ‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/persiana_Soccer/26596" target="_blank">📅 11:44 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26595">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nn8rKBL0ZxdGpR0nZb0jG08MHgvB7I_yfj7jjV2KOVINnfMDyVNwdfmDlL23lYYxHFGcGYrIQAyhQ0VT0TFIYNAqENt473As71L8A2wmhfYUk2gRAMtxLIuuSPYmKfdoetxu5KAh7Cg1wv9smgh0SO5bBFPZL-SfeL8mEUA3AxjnU3vP_FQHm5CNBYMZEPss1u6CiTEmdCM515MDB3TMLP17RPHUF8xR62facBDqyPvT7NVcY_05TyJom07Fbhvlqem-v2dxpy2TjmPa1JM7oAePuXVTSjTX8Dwpx-OIwDJ5RVeXtU4_1QLs3V7PjPKfCxoOnDwBk8CuBoYUft27fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
رودری اگه به رئال‌مادریدبپیونده؛ احوال‌پرسش با وینیسیوس جونیور در اولین جلسه تمرینی این تیم:
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/persiana_Soccer/26595" target="_blank">📅 11:20 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26594">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NR4p6vBDAbSmyyfaLwKLdLy84pFjiP3JNXNERC6qDTmRUNCc650JUis8mFxzznTVo8sSRAey-VCOuOrXdD9Fu2ycqMF0faQqpDIQTApNzeT_l3Z0I-ZsGVlw1DWHpqebzkHL-jaI-wSamZyTyWq6vocH2L-HH7Q-1R1R0IZa_4KbECgZZTV1uR_p8lLCyRolQJ4bTcuYILD09v-4p79IY4QDDaxx2nepuoh7WZmIaY3sdFxrGTqlvMVMgwGXvmf_K8OChQ7Uz-sriRiPPqfCRJyaPUvE65GjphKUtQmnH3ix7QN6UpC6Qh6D8n5Oj16jc4sblJ4-S263GI4KHZMxjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
باشگاه پرسپولیس صبح امروز به درخواست مهدی تارتار؛ باارسال‌نامه‌ای رسمی به باشگاه تراکتور خواستار جذب صادق محرمی مدافع پرشورها شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/persiana_Soccer/26594" target="_blank">📅 10:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26593">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DFIr-_G1HKjyHabJnlc4DKmVb06eTyXGsb6RTH0roASYCxH_SI1fbwWAyMyDd5qKg4iMtu0_urEKcDTt8TCqewOuD1_3KfOsv-KmoP_kOXiNMwCAs7XIfoS3f3qJ3Pgz4ZOl_jTS-lmA12b523qHYcYNHSnoaMgeijF3hVKGVaBzO6MwjpbjEybn2F-ttwP99PivuRF7-ype91qU35lEDux7UjC6cvYXu684Wa3_rlfpq42LYPDHselWA8Sod-ydjfBYAKVyt_bMMGvrjaHnLkWXOPm_SroBmKKApo8CIgWCGSa075CiQlG-ihiK3rZXYqbO1i9-CoDDjMT0CICx3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/persiana_Soccer/26593" target="_blank">📅 10:40 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26592">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsSR3EdRD3U6U2TMfgS_DVaLbmAdVXPwrNEV5lBC0rWIRYqKiNylL9KL7C3XpD8fDjFbp5rM_hVqfHJTI9DXU-HEJQjWuOxNBl4eDMbaQOOla_iNm_CfML5xXkf4MP3mkAfoxNFlYt5S1vrh4w_CM0HYCKdA-y-W-dJOPZtvEqd2lb60vGbtorcvhDK7xsCUb9sa31LV9w5PjvbSiE3a8fNr29cpUANFxHR5IyU6JwRj4_ieQnN-umvcVwvKU4z2AuLx8PpjR-EZ9QBVhF8sE5tc3aRQ-7uJNyMaGXi21Hsavcj7qnzNroben8YxSWVKdeBViXp63Mrs-ieQbrhNBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
چیواله وکیل ایتالیایی‌باشگاه استقلال: روز دوشنبه یا سه‌شنبه هفته‌آینده دادگاه عالی ورزش رای نهایی‌خود را درباره پرونده‌باشگاه‌استقلال میدهد. ما مستندات رو کامل‌به‌فیفا و CAS ارائه‌کردیم و بسیار امیدوار هستیم که پنجره باشگاه استقلال باز شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/persiana_Soccer/26592" target="_blank">📅 10:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26591">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lXnxtxFs_LfOE0azswuVp0hGue5a9-RFY2byfuHU1miwaZ3QMBDroOqI4VtA161TiyzZWI1xpe0qQhnK8ybdoGXyrC-T2rLWIc_01V6AlKjFRXOHRSRsHbwqTCufHGexZqQX-j1lqlq6CGP3uuiey3CTq8kU8uADJ1KLfUoQRFMcU26362F1n9w6lR_MHIti-mjxuXPZPIWEG2Ir26KHTSrdY9MJ0hCEKY30J-LJSdvt8L9rLFOX2nrZq5gwphtb1GVAOs4Ctyo7rmbURutv4LcM8Z-FBaVYi3FzuwMRh5hl_kbVeJmLj9WvRktc2RCOblUITJARLKm0VYmphbs55w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇹
#نقل‌وانتقالات|باشگاه آث‌میلان با پرداخت 50 میلیون‌یورو به‌PSGگونزالو راموس مهاجم 25 ساله این تیم رو به خدمت گرفت. قرارداد ستاره پرتغالی باروسونری تا سال 2031 اعتبار خواهد داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/persiana_Soccer/26591" target="_blank">📅 10:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26590">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MCZIECo2_YIONVvTl7xyDscb3jD_9CMaHzaz7TUGIiJh72WbgD_WvxeVg_Pbpi-oBT_d0M4C5oOaf0AFh19LisM5rqK1uRfXLXyOflXL585Eo7LqLHLYUbqaVLmNKlOGD5fGQPts0jemtEqy6sDEQ8Yu8hk8MXFZSHIeoeQ5648qtSVXadPrBusdQDj7MuNZ-HFJ3CXBpmDDpXsm5tiLT4Ftm6y_lg8CMeUBR2LU44HTxMev2kPWUAKjSMtVGJkB6j3gPmkyAjsrMGv21vgH0MzbfsU6ZcdlHuBtETzRX4AOEgSpwqtce-Bl8WeQxImpLEXyzppuM9aANQjgzkmlPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
طبق‌پیگیری‌های‌پرشیاناازنزدیکان رضاییان؛ رامین رضاییان طی روزهای گذشته با پرداخت پنجاه هزار دلار به باشگاه استقلال بند فسخ قرار دادش رو فعال کرده و در حال حاضر بازیکن آزاد بشمار می‌آید و درصورتی که باشگاه استقلال او رو بخواهند باید قرار دادی جدید با این…</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/persiana_Soccer/26590" target="_blank">📅 09:58 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26589">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LsKIn8YzaqmZ-4MvKs_UN7ijRzV10Wa4sYC16uOWtpjZr7pTMoPn6jXHQ8Vt4wQI0UIg_uHQ5WpI9n8hNtOyJLxflr6NemRsq7Dx9AdfhGFDaQ42ul9awyvygDK3CaeSRhzx4rHdbk7Z6_UL-Xak--Aww1S9Y3fBn_s5JNk0vIFSy1tGqUkiycmYtJj0jFfShElXp3tEnnCOmRLhiBVtwqN7qDoikKshd4XZZHlzmVenATkQganSx31C5X5sq3RwMaEDZJG1JOz_MiGV4l3_jR4jAvqwObzAoQJDP6AOjKJfOEH3j5No9KyO4ugpk3Ph-5IqjcA3IVf6TKvWCmiCFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
آرام جوینده در ادامه‌ مصاحبه‌اش گفته که سپهر حیدری تو روابط‌جنسی کم‌کاری کرده و اونجوری که من میخواستم هیچوقت نتونسته من رو ارضا کنه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/persiana_Soccer/26589" target="_blank">📅 09:49 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26588">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=preEFm8We1cg1H6ygRF8BJUqJsVdDkMCRM6r2cX84TPFTEDRf1HJZ4oM18HmUaCmdg7naJKlDq_znvJqY3XvsOZs4vCiI-37rRlBEaK1AnYnE0e2Zfs90AUuCp2yJR6EcU3Xg1Med4fYdttjY2rI09enyFQN1NA96HwZe6jVUx9W9rB2X8GVkEG4fskAhacVn4LBScj8zK12OkwThcujJ8h3YkP7MssduEFpgh9Np0KBwnwETzOLMlKvc2exmOwpoQ1aZ-ps1CCKGjqZ45yCwvNluJ5zfn_d_VseDwyWZ0mvfeHg_nNyDe42Ufue_OaMhD9mwvDxTlLvkpJE-ORw9A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c7b549a0c.mp4?token=preEFm8We1cg1H6ygRF8BJUqJsVdDkMCRM6r2cX84TPFTEDRf1HJZ4oM18HmUaCmdg7naJKlDq_znvJqY3XvsOZs4vCiI-37rRlBEaK1AnYnE0e2Zfs90AUuCp2yJR6EcU3Xg1Med4fYdttjY2rI09enyFQN1NA96HwZe6jVUx9W9rB2X8GVkEG4fskAhacVn4LBScj8zK12OkwThcujJ8h3YkP7MssduEFpgh9Np0KBwnwETzOLMlKvc2exmOwpoQ1aZ-ps1CCKGjqZ45yCwvNluJ5zfn_d_VseDwyWZ0mvfeHg_nNyDe42Ufue_OaMhD9mwvDxTlLvkpJE-ORw9A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
🇪🇸
🇧🇷
خوزه فلیکس دیاز: باشگاه رئال مادرید برای فروش وینیسیوس جونیور ستاره برزیلی خود رقمی بین 160 الی 200 میلیون یورو میخواهد.
‼️
آرسنال آمادس تاحقوق‌هفتگی بیش از 450 هزار پوند به وینی بده که در تاریخ این تیم بی‌سابقه‌ست!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 61.6K · <a href="https://t.me/persiana_Soccer/26588" target="_blank">📅 09:33 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26587">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OUGGLwr4O9sR0OEC7CYnbqJdzRhKveRy5UGgyYuUt1TSR-PXBHFKOWo7nJbZpxiln2Yml5-BYwRoBxYoC2qkyggVC6sKnqxfO_OdnUQC6pTk_H7z_Q7RgDdvr_zTu_FcGc-JvRSW6RghT1H0GGmnC9Tt4jgZL8nC_mul4gZNTjX2WxiPaTroIv-wCCxZZ5gE6Agd9aZD4CTX_QCUyMheGMZ-tu5v4cvSfPqnJxc-gHGiFukjNgTaciucuQLiIld24kifzREk_Bc4FtFdY-WsFFWfFCCdmWodAE8wnlWCe_etfJ9b70t9r3-T4b2L9K_9Nk2mlRpxWWCFA2zbOAmgcw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
مقایسه جالب عملکرد رامین رضاییان و یکی از مدعیان توپ طلا درکنار کین و دمبله در جام جهانی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26587" target="_blank">📅 09:08 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26585">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iwV7Fu44_wFvRRJBI1lSEj2SWc2hgk7v_kssDcBWceSTh92Ny2z-4G7qnCXbCLptSB6Ve56VbNO3gGTratZM2ndaa9dT6BKio3YQy6Oamblf8q7L_V30dtbxGDo6nz0PcDKPDntHOLdlcOX4KsRsnZwxjf6logTFADsMfsRsu-7je8QgrAvzXlU6CaWxNDrkPt7k0YG5rng1eIOd6JFocA31gqgiARCq4vcy_zKXNyTSKnTMW0O2KmLz3efaiOsfQC3eQHYcMVMrwQVhVqd2z7c3UfqnleaprNy5zx2YyBfJ-__kHv0b6JA-Bly1rrOG21-JbSEjtqIpCo6o3LGp2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/boFfltbX_MMQCaQ43ma8LA1Wp1GoJLrBaU8wxTHlLvRwLxAuor9nvxDwUAdUT831at00Ti3Kw9eFcojia6wmzSs02fzFiLNTQl3oVNpqncSzUtcRmhuVLwkzMMqjftdDV22XJicL2lGh5YT4L4LZ8glDe4Ye3UW1RmUBvsk4CYzyOmzeYKrHpCVkEygfhPgkra3USKhbUZYk_OZ6xkjQOS3J--kakq_2fgmqLSluuv_P2MiKmZ98dt70acNXk72I8jJMA59w9uXUaQENyA4isTjnV65ElcES-1cpPalZdULbZSAMdlMAED2Zn-9y5gzWJcr9w57v_ieymLGtO59mGg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
آقای دیومانده بازیکن جدید رئال‌ مادرید هم مثل عثمان دمبله قبلا یه مصاحبه اسیدی کرده: الگوی من رونالدو عه؛ خبرنگار: مسی یا رونالدو؟ قطعا مسی!
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/persiana_Soccer/26585" target="_blank">📅 08:55 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26584">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Odf7p-goUSbDlFl3GTAqKMMwaRF1lsxYjurcqoa8MA2rFZXLg_n0mpI2mVgMBfReAOUVGRAf5Po_NWQY-ANMykNHwjRA0LRcteZalPi4yEoAqqvKLY4mVPxscbvBauXwYjIeXoZj_bh4BnlMzCkY2Qnzwgnh7KVSI9mkHd8owt5ktrzPdPB9FcHmvUhqDHCqFjSOBr69h3gZ2-AW0-W6f73_-VcX3SgQRVQVohX_nazAK3YxUKUKVeGbda9p348nYh5VQyyIwIJLQ7AFNd6aTAdYlK_qjMqVsIum9DDX66vNq3zdDm8zWWnLmSD0BBTPZNJnrjiUwiIuu90QGXvOfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/persiana_Soccer/26584" target="_blank">📅 00:51 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26583">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lhMsnIqJsU5ULbqrkAAiFUS0F8nr8ragI-56h1t95waATOdH-tAe7GqPlRd4EE61r9ZfiVfkcsWsl8HABQT-doHahOzcGxUPWp_QH6MRMXFKHlKk8gFraTaKrf7KTLo8_8V1jFPD22zrfKs9v_vJIOD7a_Rl2GO1HE7ynKIBuRy__Ca_uPRqy-zkpz2btrH4hw7YOTE96WTnvKsHqh49yNPRotusTUPV3tYmkbpKSBfIJk3kZ9rei-X6Ty19ZgoYKk8xcvzBNB1Xh87vF_Q9XZ5aYNCAlp3RacGP4T9ay9dFBHJ9FY_jAQJ87lyCyr_Su3whaZOlnEY4bYI8KxunPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26583" target="_blank">📅 00:43 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26582">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KpO_hVNPUv4au7RiT2_dZWKuuCGbRrH-Wjwy8WIhVh0aCQaa07Cf0IuQ97mSy5pcmrN_FdYyBLpcz6-Er5RC9s5qBorm9vbiO_4Ya2a5jUlkO-4IHkdQ0BNxdSsvJQGE8Urt8JpCji-10wqlBnRO1hI4shZWNcNGudKiraU1FI7bNf75nTT7BkmgQb73ZlKw8Q6k-XQHWqUnBKNDCuJHmJ62ffa_Y2dpf_KuIDcJCATDGh_1hcceGFFaA9nJJ60MYJBbymEUkZYnvzmDeFip5NoXUX0sC_dUQF8HfZQNUydtYbyPJQE8IYihXJ56Kjg09N_YThmR1i0j7SrBiHnMxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🇮🇹
اقدام ایرانی طور فدراسیون ایتالیا؛ از پپ گواردیولا، کارلو آنجلوتی و روبرتو مانچینی رسید به آندره‌آ پیرلو! پیرلو با عقدقراردادی‌تاپایان جام جهانی 2030 به‌عنوان سرمربی تیم ملی ایتالیا انتخاب شد. البته در صورت ناکامی در یورو برکنار خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/persiana_Soccer/26582" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26581">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j2w1GsbooOpSPEmWJHpGPZe0JJWEUDi6kheoRJNiGc_0p6Pj6VJk9R63ViGx39gdi6G6GZYUbh7KXVWxoLOYZBe-giMoL3fgptTm1a0-N1mQwNiHklKIagH4b4N7KPHhBJFskyMZD_p8eHHwtUN12lCtSvp6ADedxRDPZh2tOOu-JALuWtlNWNI0qB4upjHXkjbv5Ww_8S6q1WNd1XCnbj1FhHes7Bmi2cd_2t3A7417-47P78NAhf5xFHJ0ew4wrqVD3a0Hht5eq86ld_wEVXSZvLYWkp7JU_tsdK2gYL72AsXQ0i4PHvfrMWmK257Ua6_HQCR87Ko4pXX3fVCZeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌‌دیروز؛
برتری لک‌لک‌ها با درخشش سوبوسلای و برداقتصادی‌اینترمیامی با تک‌گل سوارز
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/persiana_Soccer/26581" target="_blank">📅 00:39 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26579">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bm8dqF82zpPf5KHbDyfY98AcPgOPNzW947bDFVjd8hCdSNq12vd-_R87u716KJD9vKTDJeywKS00gINP3hDAMEzHlXAL6Ye6e3obUJVKt0AmyO5FqpAoi9CUjeqXrLGhJs2FhQlECqEYyA-P65Ugffe4CYcU2HffYApcnvYj018zD-ynzZ1io8fU8mVbIiIMrgKTF9cwe2nbf8y0m4zL5R8f6_t8_o76FbEyLFnj2IYVXdvBhAdM5CJ5gh1ZJUCamXW_jMRiOVvd4NsDvYdqBC6njWtzIIeHmZ8pBnKslH0cN-OcD1rbysscsrFqyTTAexEaELjhSFfj6qhkirmyZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
با اعلام رومانو: یان دیومانده با عقد قرار دادی تا سال 2031 رسما به رئال مادرید پیوست و مدیریت این باشگاه بزودی از او رونمایی میکنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/persiana_Soccer/26579" target="_blank">📅 00:17 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26578">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FiOn58jQvomqejjvVhW8TqS9zFWBlSOevuVTB6D7nJ_bCPQ9pQTD1lqSrewElH-xhKx1SDHLo63cJj3mLjQU5oKI4P6UiztQZOTWTiWpZy03QL14Tupd-8Me-W6VPAbMnuLKB9h907y4OkrSTki6KRsXuEXfm8o4QZBR5d2r_s9_a7UP8lOUtqt268Ao9_CDQE7D7qzKZz6TuVav9laz-kvHF3SVhg-zJIXbAKs_m10yU6Pqj6cvBaTmnWgvPAQWbvtGFFWA2VXUhRSF5aVdqwHU-x-hSGCX37P6bauGF7QOzl3yORujza1cVZFfyHjhMaU-1z_OrQlZ4MOVdH9QQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ پیروخبر ریپلای‌شده؛ رفقامون تو کانال میگن عثمان دمبله، کاکا، پائولو روسی‌ و بابی‌‌ چارلتون از قلم افتاده و این چهار نفر هم خلاصه موفق‌ به‌کسب‌ سه گانه‌ارزشمند گرفتن توپ طلا، قهرمانی رقابت های جام جهانی و لیگ قهرمانان اروپا نیز شده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26578" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26576">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=tT0apIoDYMY6Ui9z9-Jf1Uc4fc9ANG2eFPB-CFYgx4KE-_f0Az-hhVrm1OdHj2ob_cg4s4CdIDGiVn3LyidEoBfZPTHo4Nw83V4U3HAwIYQlYmIvSRj7DsfbZ45mMT5ZN2JKhkOx7E8f84mm1Hx7nMOqpnMxmJjqRjIM71Zmcg2L9DOciJIKTmA5aRqSVNNLZvLoCwokskOWwyruBCxWItk8Ue_mvDMkZw8DGiRlMa1tyIVjeXuQGkEcJynGNmXv48g1PznHiTN2Wqav0JTaE8VkXmJwnlb9vfKG8RYjUHSRG67JlltlDHokDABNs6oqvkemkWBSgHUzE1P1ys5Xzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d08e79ca3.mp4?token=tT0apIoDYMY6Ui9z9-Jf1Uc4fc9ANG2eFPB-CFYgx4KE-_f0Az-hhVrm1OdHj2ob_cg4s4CdIDGiVn3LyidEoBfZPTHo4Nw83V4U3HAwIYQlYmIvSRj7DsfbZ45mMT5ZN2JKhkOx7E8f84mm1Hx7nMOqpnMxmJjqRjIM71Zmcg2L9DOciJIKTmA5aRqSVNNLZvLoCwokskOWwyruBCxWItk8Ue_mvDMkZw8DGiRlMa1tyIVjeXuQGkEcJynGNmXv48g1PznHiTN2Wqav0JTaE8VkXmJwnlb9vfKG8RYjUHSRG67JlltlDHokDABNs6oqvkemkWBSgHUzE1P1ys5Xzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه نزنی ما احمد گوهری رو میاریم به جات!</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/persiana_Soccer/26576" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26575">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NC_01oCbVC4rYnlr-7EPJ7LH7Rs39rkQVbC90zHeTgCMgiIUM-V-2LJ6A1lHiSPAXepYCnW8yLCMCrc5WiVqG8NU5c1tAdmoUo1PeEnAC-g57t9clA9BVMxQ6g6fUMJwEBbaMANJozvl52ZsdYJOxmYbgD-HTX6mvVcn3ULdt--C-WoxHfzTAty_F500eIupFKy9Yk2oa-rp_Zaghvjq787qdaAlEqrsO3rSC8hVPOjbw9iKzUXPtawW4BNhZvhNnr-6ukQZ8K7MrWrXP5csaE7GNX-PD9H00HJimpChBTnjPMqZ21NZUoKHuIwhAFjPWAIXvzxJeoR7yBVhlbHSrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
#تکمیلی؛ حالا که تموم رسانه‌ها خبر از پیوستن اخباری به گلگهرمیدن لازمه بدونید قضیه چی بوده. مدیر عامل تیم پرسپولیس ساعت یک ظهر با اخباری تماس‌میگیره و میگه قرارداد رومیفرستیم امضا بزن اگه نزنی ما احمد گوهری رو میاریم به جات! اخباری هم میگه اوکیه امضا میزنم.…</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26575" target="_blank">📅 23:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26573">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O3E_6EKaj942P410kf-Lmy3gCLA7gCerHgKT7l648oxpXY_L7i7LXrdZGm9UbBGvcmv1qQv2kT-i6ClbuGnJE23lXET5aTneQTvUhovt0D--0pT6YhR1rAjbOROqM7OfBxJ4mXMb6RE4FQcC0NkOOc6afQ8CDbIv7GW2Y7yA03t4Gx-o8SFNsCuqJv4sXcpo6jFqfTLNtgpRFwSVxqAMziT_Hqz7A-jO8c5VkXzIL6UKIQQ7gXgBJxy1OWDx4jrrKvFPI6RQHQU6qYZsO30mwviX15x_1cD5VOKwGv0gsahYNyS6Xd8_Z_N8SzO8MJ_xYLGjwslGC9oWR14wi1yOQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی_پرشیانا #فوری؛ دقایقی قبل سیدمهدی رحمتی شخصا با محمدرضا اخباری دروازه بان فصل‌قبل سپاهان تماس گرفته و از او خواسته به گل گهر برود و قید حضور در تیم پرسپولیس رو بزند. قرار بود امشب محمدرضا اخباری پرسپولیسی شود ولی به احتمال زیاد راهی گل گهر سیرجان…</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26573" target="_blank">📅 22:47 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26572">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1p6XzfFvWYtB0hA-IpVOAzOWKatAHMfjy5J1wxa_RDN_WHFDU2tO5zeySL1C8H8YBidxiIcu00dye0yaeGmw9cz1i7uMHaCSbvirqY_8Ar8F9r2K42TU4DvOUkJasxskFv3AYKaJarWcdHPjyk4Y4JKOtKwKP169-_WRQyAeFv1sT8PQj-2sTz8tF5Mx_1UFJvlZPVAo30tWv3-nQ1MOKzCCc3atHEsbKPD0ngVtz12SnKE_OgRjNz-VVRJLlu800PRVTNMRfcFuJdCmr9IUmVjittGgxhV2Qu_5RG5LSVDu7yZxH3WYffKVR244bwq-FBxLFW5AGNTLxrfUHCcQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇨🇮
#تکمیلی؛ خب دیگه تمومه رومانو هم تایید کرد؛ یان دیومانده 19 ساله با قراردادی شش ساله به رئال‌مادرید پیوست. پرز قراره بزودی پول رو بزنه به حساب باشگاه لایپزیگ و این انتقال رسمی بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/persiana_Soccer/26572" target="_blank">📅 22:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26571">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PTOzyaOp0xMcNm9fQkzuONKYOg12rpnc2TJB-o3Pjr20FFg0dU9dbMLkrnH-6ykwR4-qgRsSUw1aW03oyFev_B7jXIk60t40e6bM3Kvas2Kpy2qPKCWvHxttNNnYByxRQZ-LOS9h8C_Jb1Wt5BjytzH1PlL2ZJwqtxQ_eDKevmBavqys4Zs90nXH5FbdpxD64rjlhm6nsc-Ik7Dyz8NGt2pgH0ZaniuYsIoychragqg6lXUX3AsR2Dn9UPNBSbqCXL8XWmmSl0BpmOY8lbyFvtFZsOLP_U5N6J-M4xZ7ta1JcrmNuH-uwJgtNjpQ8btKHW3rBCeDIi0_pUADeKUnCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟢
مهدی عبدی مهاجم سابق تیم پرسپولیس که در فینال‌لیگ‌قهرمانان‌آسیا هم برای این تیم گل زده بود باعقد قراردادی یک ساله به خیبر خرم‌آباد پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.9K · <a href="https://t.me/persiana_Soccer/26571" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26570">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I3yuIi3tVnrcwfkQdnr1U_s4nbc9u9VBnYv3TiAHkXUYw0xy8thAIakMJMGhWOqe94yQwrvdxdJyCeSEGA7yGHuRm78iFxgBIN3x-dD41j0OZHM78lniyd57PRi5rKLI43bI1p7VdUpjtNm3KETwnYzINFnADAY3nXCEvQ9UnVyhTfeFOds-h6HQvoq-0ZHMfv9Ax-V25kNCxNSP4n6W7HlTBJdrcFDSBgtrhJzvHrH8U3dTribcwmIDCFugqrEpfiBU5jG8CJfIRaV3uqcF3nUPQoPFVwS3-eixUSljmp0AmyD-buaAEozZhlIjvADLlHiYs48YzCWxNwIK3EAxGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
هروقت فکر کردید بدشانسید یاد آرائوخو مدافع میانی بارسلونا بیفتید که بعداز گلی که به تیم بنفیکا زد اینجوری خوشحالی‌کرد و به خاطر خوشحالی‌اش مصدوم شد، گلش مردود شد و تیمش هم حذف شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26570" target="_blank">📅 21:37 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26569">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fy9staWGPvH4kvFw6wluSDb4PsedZrEj2g5yFrAJKpl2Es7MbeAedegaeAgPr7wWA997PE5_Y5oRYyks1xfO5h0i9-ifXwcqMTLwcgwgS5Ld_0XVYHMHab9hS9X_Ba7W118KhzCBlz_eRl7NLGIJCkKLMytDwQ-oCK7PVoxdxHS22Wrgp9q_E-rhN_6CrWaLdKf14h9H3zmTsutAKXcycaR_jFyp6olcJT_8RvrkxG9KKt3qRKd-JSK3taVIpONb_hKFc9HpfFLLG0ojIu2XbKJm9OeuV_WHqhdbzUKoAXd3e5mE5GDuKnrbmbSkUuxhNzD_20msqULCbNYRV29DFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
باشگاه‌استقلال به‌وعده‌اش‌عمل‌کرد و امروز پیش پرداختی توافق‌شده رو به یاسرآسانی پرداخت کرد و آسانی نیزتمایل خود را برای تمدیدقراردادش به مدت سه فصل دیگر اعلام کرد. بزودی بعد از انتخاب مدیر عامل کارهای تمدید قرارداد آسانی انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/persiana_Soccer/26569" target="_blank">📅 21:28 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26568">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xlrgvk0pKapBczvk6GD86gLoCKzVsoFzoyXKs0sNYSSxy_8jHKQWAJhCxZ_hlPJL9v0It1ZEmeDVTaQ4qu9TO6Ky875O4-uz60M-ARnh7QmPDXMeg_isDas589NAbtvLbSZewRMe2Uty9irMQaMnj5ifqQ3dMYs2sF21ksrnDCQtKCcPWxUpuiHDCP8ROhM-tiwrrjnN_v22AS3CbOJ3Sm-hKSANi8O4g8_MOmvWzRzURx3Qh7ObNFCzeDa-AWV3njwM172Zm_Nla9MHdyiaprkEB64_6FitmWGiAST4Tf5ZfSRktM4Zd2cQKcUYHQaFqSjxFdfHa31KEPcyTFL15Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
🇧🇷
#تکمیلی؛ تلگراف: خبر مذاکره آرسنالی‌ها با وینیسیوس جونیور کذب محضه. این بازیکن بزودی قراردادش رو با رئال مادرید تمدید خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26568" target="_blank">📅 21:12 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26567">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QGxW9ptLrRbBZdvSy4Kq4mbP3BWTEm854UoHHwnBGi7G0K_nZcMdgyiMI4VDsopWBhykueyJByY9gzwqBYaXi1GyZbJwd6iUfqD8Ia5BhQx3iC5oSU1yp_M6Pp-8Dp6-89At17fLwfW5nvHBg-qGhsL5AKvn9QIDFlIwEqu3isRquGm6jTSo1CCR7Om1_bhz8kv_2GkxTkfyaxXrx3pkx57CRJW0d-oLnPJcdseIc2OwOpj3XEPuwDS58QPMp31_nyArvqcmoz31evwZBG8dj3c3vkZoQWOeWhUcH3nogq0i38wo6Wr1nuo68VjNbESMWIraoW5RcuDFKnRb1AK8kQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
با اعلام رومانو؛
بایرن مونیخ بارا ساپوکو اندیه پدیده 18 ساله فوتبال سنگال رو با قراردادی 6 ساله به‌خدمت گرفت. پست این بازیکن هافبک میانیه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26567" target="_blank">📅 21:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26566">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMH7-NyWkzTb8xnrtYuGfHOs5LuF8mX3bNixrO3OSg9wFjbcPRnTvjMAwWczmruHrqFzcEtDV8t5gRZoc25PG0XOn4O7118fcjCz84ZvUmL8KJfw91wzqs3VGND9fg0vU5Q8UxkaPMmgUUpARUIgakzqtEGUGUcsa-JPfJ0kIJDLl2Bi3LX9xnkb6SZYFGXSyvJL5BQyD3G_SnRFp6xFnk_MlapZ14N6zzvJ4gk3hnCunwj9naB8uiS3gACDGvcnngBSld22Zf-dmNvtoAkVS8JbC0WDYGHjuWN7Mbj-9Dt1STZesf95nAIRD8mNWMT7r5HAdGxHD3ausiqi-mjVbw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه میخواین بدونین کیفیت زندگی، اضطراب، فشار، چقدر روی زندگی‌تاثیرداره، باید بگم تام کروز و اکبر عبدی همسن‌بودن. تام‌کروزهمچنین بهترین تفریحات، بهترین بدن رو داره ولی متاسفانه‌اکبرعبدی‌فوت کرد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 65.9K · <a href="https://t.me/persiana_Soccer/26566" target="_blank">📅 20:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26564">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iiEzgBIkBmMGrP6Tz_FJaguvImPdS9hMpDMnJOuwXAeLHRYTD0zq5VDQuZNK8DFn6a5FH9Noe3odXRb8U3nrbBwwec_kQoe8NKOhVl5V0R4FbMB9u36mgcbdIO_CPEeFOheJyw_GJE66O8QdMTeMgMgQdyfR-dm9O_4FMYxCk7coqRSyzVHxpBwQK7NsmCF0lyffPicnp5HGigck9PqkNkYPhyx4AZZwJtND7hiajILnv2qC6DJnCt72RhsPynWQ9gjBLUHYtfHdNG7maejOtDmRxfDU-AE9EwVlt_O4EMvkyFc-KIqnztyNEGDIpBk40FVvnzhPn0TemtbUjjRnQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تاییدخبر اختصاصی20روزپیش رسانه پرشیانا
🔵
محمد خلیفه دروازه‌‌بان ملی‌پوش تیم آلومینیوم باعقدقراردادی به‌مدت پنج سال به استقلال پیوست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.7K · <a href="https://t.me/persiana_Soccer/26564" target="_blank">📅 20:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26563">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=FIsW_eCS3f3_b21YvkdpXOogKfvpI0G298T_zL0pXtD_aXDCB9_iGoRHMy288RRNkDv26JbFNc-mQYQWxY4FGyQLwGkeblrxEn41FDquR1KwB0XcWsVh3AObnCetm863GG0o591dFVqxMe799jxdGrDFso_jE1OlwFs1KP1ubtHJIXIOTRre0pS5Xmaacdg6R9LaNI5ftUIeUvJD_bcLENY9QjbC28UDUnXeDUhb2Xa9iJhNOINzg7ifAjsmD5FSSFAlt7p-1-FTMx1QiyTpeo8ixaiS5lBdPakC6eurzqzTJwxfKGNpmI5pXjOAaSXDnRdF7l-Ah3YkJ1221GWnIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e2409944d0.mp4?token=FIsW_eCS3f3_b21YvkdpXOogKfvpI0G298T_zL0pXtD_aXDCB9_iGoRHMy288RRNkDv26JbFNc-mQYQWxY4FGyQLwGkeblrxEn41FDquR1KwB0XcWsVh3AObnCetm863GG0o591dFVqxMe799jxdGrDFso_jE1OlwFs1KP1ubtHJIXIOTRre0pS5Xmaacdg6R9LaNI5ftUIeUvJD_bcLENY9QjbC28UDUnXeDUhb2Xa9iJhNOINzg7ifAjsmD5FSSFAlt7p-1-FTMx1QiyTpeo8ixaiS5lBdPakC6eurzqzTJwxfKGNpmI5pXjOAaSXDnRdF7l-Ah3YkJ1221GWnIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
🔴
#اختصاصی‌پرشیانا #فوری؛ باشگاه نساجی دقایقی قبل رسما بر سررقم رضایت نامه دانیال ایری با باشگاه پرسپولیس به توافق نهایی رسید و به‌زودی رضایت‌نامه این‌بازیکن رو صادر خواهد کرد و باشگاه پرسپولیس پوستر ایری رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.2K · <a href="https://t.me/persiana_Soccer/26563" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26562">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwJWaAurBdKqVpiJLgrsSNXCjBvl6DGxCAUpl8nv0bIFRSkI5lEzUUOaWOiVQfVkdm9iHMA2qsNsJQynfrDClGOWvM7eR-D_G4CFsfqpHOZBLoWQrVv_b4WTUaWo__MMoacA3cHMwP_xeKun3l5YsmlGTATiwTel3FS1u0f2PQKHddlomMSLaX5i0C-b72YFFddxEiK4ccYVKs29MMT7GA1rX6RH_zUlS2LBoZDSv8k_ZNBNyoOnXYtFsP0WzgJFzvodOnCsBj6sztIQy-H2IcwG25kByrhDYq5wNdXVfUrEcA8KAQjwbDHRJWO9D6PWTy5t7eIUpetGQdLZJ_x1cg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
👤
#تکمیلی #اختصاصی_پرشیانا؛ طبق پیگیری‌ های رسانه پرشیانا؛ باشگاه استقلال پیش از شروع‌فصل‌جدیدقرارداد یاسر آسانی رورسما تا سال 2029 تمدید خواهدکرد. امروز توافقات حاصل شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.2K · <a href="https://t.me/persiana_Soccer/26562" target="_blank">📅 19:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26561">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/66921272ff.mp4?token=fQAOW4FmxgWtSYsHPg7LUK488bbZjV0Gp8JTwvt3Kml76DTI4ElqkxfWt9PhbwF4OrRqPdviwbuvPLG4WAC67hnsLUYpEA4HwxgmqSK4HNg3wPdQkZZvkpF6TxXGo2lmjggCGo5IVlDA_NhPxy34-lHfF0qj_v7tDG23SesEFrzgYp5B-g-ReDCc3JAB_QHtSXQZabvgDfIxwCIklzikPBN3acknza-5q-wmxZwCQEAQuoo5o8jJQnYLkDqmB5lPdI9hbDveXxrP4hVYNEi3ZQ-7WU4t7uXUBu9Kib9TuPranRoVRYvtjc2R2ltw66DoG4yuYusIj5KlTNwugIuXDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/66921272ff.mp4?token=fQAOW4FmxgWtSYsHPg7LUK488bbZjV0Gp8JTwvt3Kml76DTI4ElqkxfWt9PhbwF4OrRqPdviwbuvPLG4WAC67hnsLUYpEA4HwxgmqSK4HNg3wPdQkZZvkpF6TxXGo2lmjggCGo5IVlDA_NhPxy34-lHfF0qj_v7tDG23SesEFrzgYp5B-g-ReDCc3JAB_QHtSXQZabvgDfIxwCIklzikPBN3acknza-5q-wmxZwCQEAQuoo5o8jJQnYLkDqmB5lPdI9hbDveXxrP4hVYNEi3ZQ-7WU4t7uXUBu9Kib9TuPranRoVRYvtjc2R2ltw66DoG4yuYusIj5KlTNwugIuXDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">📹
حضور جمعی‌ از بازیگران سینما و تلویزیون در مراسم خاکسپاری خدا بیامرز اکبر عبدی عزیز.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/persiana_Soccer/26561" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26560">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I9QezSCQsn-CIfYnTEl6pkaGWYZzVxeG5GnW_5BdRlYtCuaJyJYq7pI7XAfJHq3AxWRmbZGJ4IALz64vW04g4dfs1eragv7lvqpSZRwAmsOAhNKW_gYwrSCS7V7w2rstJl8ZK6ZGgTkP6-lqRdXYqca6cL56heKrbbLH0jiYVTOwX7MJJYtvxNN9qhw6w_V2hW-EYfqEB4P5m3T4CcqhQii5fJnrwzfezCtZROsBV31Ngw-9rDqECSxoaEIVj2BkbL0KppYmokS_m4qXYiduFpgmmcN1NXU-2tepFfk9jfZ7j39tFUyCb1IRb3KoqC6Q8EWRqZffmlxdhN3_4vrjyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
از دوس‌دختر لامین یامال پرسیدن‌چرا نامزدت رو بعد از پنج سال ترک کردی گفته فهمیدم لیاقتم بهتر از اونه و منم حق انتخاب دارم و انتخابم هم یاماله:)
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26560" target="_blank">📅 18:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26559">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/saL89nhaxsmtNo6u1D4aqBMQID5pqRTmm5si4dxLnFvi7t-FcWL4glI8A5lLaiNDJWKafJqh25q5DL9rnSZd2ST5GsWt8cy8MLzOLQV8CQDHX6PNS_W7KIIbGlOU6YTXRBy1YTL4CY-L_aZCdENW0yKazq9PlVI6CKsCj0b0GKeRbJH244KjxQO0XoGbqvMnSwFv5nJdiYg2mciuCpUgQfpDajcF04mZjx5hVnF2EfawRunwpaNpniDRgyODBKTmwY_UWQeNTQAwO2H8Pmf_NTvyXIW9a2EQ03gCqbNJtTi8VtNDkmTgrbMamtZqJ_ata40T7p0I-jJqb8a_yAlaFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مدیر ورزشی تیم لایپزیگ: در ازای فروش یان دیومانده به رئال‌مادرید 115 میلیون یورو از باشگاه اسپانیایی دریافت‌خواهیم کرد. توافقات بین طرفین انجام شده و به زودی این انتقال انجام میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/persiana_Soccer/26559" target="_blank">📅 18:15 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26558">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g68ro4gkH3gDKYXnYXJMeIlSJgA14VBHLriPDAxclne08FXdZV9-diWS3viYooe53xwtzw1CGywvZ11qChFUeMd4Mbq_MIhfPqCud9bLOVl_IDa_DoouX9clwZPsiwv_SHfr4Modq7aEr56r96fAz4kohG-wA1TxxRgkX77X6vz0uokbgCmB8t__jYVy6REC-d16rOnUi8lPW5TQrX621wAQIJ9rnVwi1SH3VlwI0Q8vxGIjUR-FL9bm2Y3ryVPh2UqvKUc9iProq6WNRsIloYfgQNFanfxHnkBhRNm7XB4UFVvTgTUWwCYi0n6vnIwTPTxI1FRtpy7Gb0BEStODFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#اختصاصی‌پرشیانا #فوری؛طبق آخرین پیگیری‌ های رسانه پرشیانا؛ محمدرضا اخباری گلر 33 ساله سابق تراکتور و سپاهان تا ساعات آینده قرار داد ارسالی‌ باشگاه‌پرسپولیس روالکترونیکی‌ امضا خواهد کرد و رسما به جمع شاگردان تارتار اضافه میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/persiana_Soccer/26558" target="_blank">📅 17:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26557">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XT0YS0Qr8dQINt_tuHrxwIgzmk_P2Wtglrz6vumQcKUiDxdyZZp1qgn3phJ8lXLHntBdBQhBC60uMJ7x2tb6xZ_81rqP3-E1kuOhu8ELOhPH8bCPb8LyVYW0NSmU2aJmOxU7FY2PSCNpCvGZUsY-idftLs-HXwdpFB_v3-eishaLETnRK9YEVNDi3D3N58x0ZsfI95DKQGxcKjR5I3caJqY2hwN1fT2fEUoWWgR1RHnr8m_UasWtzkKhUQ8ZEozhhqVsbdL_cC8qAxRZyzQpYiXYOpDNjLwrq266XytkUJ98TswNWkpcEA1BqiWE2OFb3TloMJU3aVe3A_gT1McXTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#اختصاصی‌پرشیانا #تکمیلی؛باشگاه گلگهر به‌‌درخواست‌ مهدی رحمتی خواستار جذب امیر رضا رفیعی دروازه‌بان جوان پرسپولیس شد. این احتمال وجود دارد که درصورت موافقت خودِ رفیعی، این بازیکن با پوریا لطیفی فر معاوضه شود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/persiana_Soccer/26557" target="_blank">📅 17:55 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26556">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">📹
ویدیویی‌خاطره‌انگیز و دیدنی از عملکرد ریکاردو کاکا اسطوره‌فوتبال‌برزیل‌دردوران حضورش در میلان
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 63.8K · <a href="https://t.me/persiana_Soccer/26556" target="_blank">📅 17:46 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26555">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S7_hHLJkVAI07boYgkZEiLY2U388bkL3Ab1qGDULhrZCMdDFCyf_TYT7FpeJUxAAW42r43kI8YEaxXqCyegrWQRFAzZ-Sikp38bMh_e0WUP6xMAuHKr-kRELMgzV__KYjj_QX_DEjTikudjNBSo9XctQb1GsbRSp4GSDCeI52E5zd9NkshY4xcagRvUp4gwzMdtkDQ-8PaQF16u9gRM1-NjkyhwEz_8rUDs7h5tnclAJj7IZylU3PYxOLKoIZl19EbQygxXhJCFcDfAxJq-nVSOQiUk6_p8Del68Hvk_wlDVCEsPWHJax1FU1rV1flH1Ah4kKD8QQUKi1k2tM_2xlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
#تکمیلی؛ یاسر آسانی برای تمدید قراردادش به‌مدت سه فصل دیگر با مدیریت استقلال به توافق کامل رسید و بزودی رسما قراردادش تمدید میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 64.6K · <a href="https://t.me/persiana_Soccer/26555" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26554">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rT5jNOy-Y_e7zlFawo4Sq-suXvERuM_Jscox5sZwG9amtQOVN0fByCcQ1fNOUab-W0XMVLvFx-FZtBfVPtzDC4gFKhDC-zGK_1jktuwyGEY5h2KWHcJCBdzm9FROxYusqdYioGUQNyRHMndb2rPhTGEBP5dFMHEgETXQ7fzZLXeHQjjDlmD3PqbNQd7n8ZztcPxrNVqDNpZkg8tNS9jK0p78jkXFruGcipKe7XCsMH-5Xp7SsKPgEueTOxQUAJjzz30J4ixR3v6n2NMFne36puUNV5Ay0NepkVKoST-456dOmC50_i50D7LcFyr5keutdPQ1EstKXN4oe6FwurnJtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
طبق‌اخباردریافتی‌پرشیانا؛ باشگاه استقلال برای تمدیدقرارداد روزبه‌ چشمی کاپیتان 32 ساله آبی‌ها به مدت دوفصل باایجنت او به توافق کامل رسید و بعد از بازگشت به ایران قراردادش رو تمدید خواهد کرد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/persiana_Soccer/26554" target="_blank">📅 17:43 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26552">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738d729f53.mp4?token=VNMhpg3KA6pIwxfSkwpbsS3IgI_kxddGhxkZL4NDNUGgvl8bMGW0_EQm5M5wTRguoFx7ciy3C5gWm8uzd70jPsb-gOOP68MxVdiFtBBr2oFC7W2cBH_uxDrLJnVvBYxz2UlqQ0YDuNem3XWEfBoB7D3ecw86oI8cD9ho2Ze4C1jvu9YHqoTK6xivCB6Wy94KDB8ir3uOAS_7xEVG-HgN_neFzXenGJX5DZNXBoDNx_KJs4ncrhOqlsZzy2TuPl9ws97r2yUMtgnIH-9A0fqcQHWji402g4utnQ68Q042Zqz2RCwCV7ySEQT9rZNuAg4FAZ33p5oVQ2rdtWm2qPIX9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738d729f53.mp4?token=VNMhpg3KA6pIwxfSkwpbsS3IgI_kxddGhxkZL4NDNUGgvl8bMGW0_EQm5M5wTRguoFx7ciy3C5gWm8uzd70jPsb-gOOP68MxVdiFtBBr2oFC7W2cBH_uxDrLJnVvBYxz2UlqQ0YDuNem3XWEfBoB7D3ecw86oI8cD9ho2Ze4C1jvu9YHqoTK6xivCB6Wy94KDB8ir3uOAS_7xEVG-HgN_neFzXenGJX5DZNXBoDNx_KJs4ncrhOqlsZzy2TuPl9ws97r2yUMtgnIH-9A0fqcQHWji402g4utnQ68Q042Zqz2RCwCV7ySEQT9rZNuAg4FAZ33p5oVQ2rdtWm2qPIX9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
👤
یادی‌کنیم‌از این‌صحبت‌های ارزشمند علی آقا دایی در گفتگو سال‌های اخیر با عادل فردوسی پور.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/persiana_Soccer/26552" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26551">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=F_-ulYuyLOv06gfwv9yAVv6lvYDRig4yuhEmLMQnwGpfAjdOl8BgdeS4dUL3UbJKoux6wHD_40oyD2Rb_9ef1xloT0PQJXLA5y4XrXAqDD_McVXnvOf5TCKaZR2awdOrBoIMT2I3kyp316J68Re46NTKT8pEat4mfVZSt27Yr_WvUiAPxfuso0C7GvsSpqtmJe_EQvp2Xi9lzgXnjjIO8aFf6jT9X4ryYdU4U_z3rB1urwDExTDMRHIUJcDxutz9FWJJeqhdW69TgAOqY3Ah4GxMkfBUBape_Rb_osZ8Co_Lg0_iinors_MG2xtFM7OqV8Fb5Wn9tL_n0_01odUeSg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7014b2e92e.mp4?token=F_-ulYuyLOv06gfwv9yAVv6lvYDRig4yuhEmLMQnwGpfAjdOl8BgdeS4dUL3UbJKoux6wHD_40oyD2Rb_9ef1xloT0PQJXLA5y4XrXAqDD_McVXnvOf5TCKaZR2awdOrBoIMT2I3kyp316J68Re46NTKT8pEat4mfVZSt27Yr_WvUiAPxfuso0C7GvsSpqtmJe_EQvp2Xi9lzgXnjjIO8aFf6jT9X4ryYdU4U_z3rB1urwDExTDMRHIUJcDxutz9FWJJeqhdW69TgAOqY3Ah4GxMkfBUBape_Rb_osZ8Co_Lg0_iinors_MG2xtFM7OqV8Fb5Wn9tL_n0_01odUeSg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عربستان‌میخوادبرای‌جام‌جهانی۲۰۳۴ ورزشگاهی حیرت انگیز درارتفاع ۳۵۰ متری بسازد. این ورزشگاه باظرفیت۴۶ هزارنفر برفراز یک آسمان‌خراش ساخته میشود. تماشاگران هنگام برگزاری بازیا می توانند در میان ابرها فوتبال‌تماشامیکنند و همزمان چشم‌اندازی وسیع و دیدنی‌از شهر را زیرپای خود خواهند داشت.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 67.1K · <a href="https://t.me/persiana_Soccer/26551" target="_blank">📅 17:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-26549">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u2ha8FVtu2gts_l7CFWRzfGHtzc2xLKZMFYT8SWEPE8oiuuxWBgV6CyxMP0RCz7uH33wByTtNOsWvHtOb5Vf6G3wgHYOgiuoPz1qR5QgCVMoyqJwPykAWNtXqfcxDw1_uHcLR6uzuV7-KmVoxRcoANmTwMKVFGG1uVw3nMm5p0T9W81Kkokbzo6iiHFcY5rUk8g8alBKg3iOae9XNUzh6tO_P7fxvYKwAez3tkuJMc4_X_b60lThANaMryvj5gUpAysmOYehKIvbYj7M2smjwB0vLWBkQiSMuKM7dtG4f8O3KWpIZBqyJ6pKTvQnBvPE2zetlCPsITauUjgoUlHhsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
#تکمیلی #اختصاصی_پرشیانا #فوری؛ محمدرضا اخباری گلرسابق‌سپاهان‌بعد از تماس مهدی تارتار دقایقی‌قبل موافقت خود را برای عقد قراردادی دو ساله با باشگاه پرسپولیس اعلام کرده و اگر اتفاق خاصی رخ ندهد اخباری بزودی پرسپولیسی میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/persiana_Soccer/26549" target="_blank">📅 16:35 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
