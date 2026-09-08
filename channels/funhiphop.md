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
<img src="https://cdn4.telesco.pe/file/i2qhfDKW4RG0osGT29x44ScVM4G0MjQzeb5nNPpjluSYTF_KVmB5I4m9Zgwn7oLNUyb40cqMSaxfQg6XMMZ7RtvxOBQVvvsZU9uofZqvlO-wI8rFOZRtO2RB-Rzx5D7plgTdArzbZcf81kV72uZ9YhPBm8dGE7RMvmov3j9YxIngDjGLEii63yoprL_-Ewg6fnSURZXcjb0JhoB96JoR18WhoVe6tZT5ViHv9KZOX79DDJemQ2st1jfGWf4Fq_Xgxu55AxoQVNbEZrJWj76lGknKx1Qg0zZuQb4VJ_OUdy1MFyfzkS3CifbvxyWPJgPphQ78PDwaspVYGRzxQK8TKg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 226K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-17 21:28:15</div>
<hr>

<div class="tg-post" id="msg-83164">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IX4sZ_jeO44GZILHrq-mXSRR16rCvZSYJG-I1SNcTG7FcC69-xCgewEAm6JqxMXX0trDCs7gjenfukNcmClu44tpjR6qQO9Kgr5IKCz53_kig_XlcD6aUSJJUSGqVTUhwuZnlG9gn3NjWCD6VdOvO82yywWOGl0U7hfJBb5uCslaJyj2_-KAlzEibp8DSjNzWzbP3bEloSzMlVlpegQgCTL0OrXJLsS0p8Nn72HG9971lTMi7BAnI9nyAqX02AlcXEL8FJa4MxGg0OTh-olmF_5LGhEj80i-TfggOQI4D8Mympghdr6_XHtzhmRNrdww-NSXVT3NrHlvbLct-WvcKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من فکر کردم بخاطر بارونه داشتم به خدا فحش میدادم، نگو باید به ارمنستان فحش میدادم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 1.55K · <a href="https://t.me/funhiphop/83164" target="_blank">📅 21:21 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83162">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">به گفته بسنت ایران رسما از فردا ساعت ۳:۳۰ صبح محاصره هوایی میشه و دیگه هیچ کشوری حق نداره با شرکت های هواپیماییش کار کنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/funhiphop/83162" target="_blank">📅 21:05 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83161">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">کم کم داریم به فصل شاهکار هودی نزدیک میشیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.51K · <a href="https://t.me/funhiphop/83161" target="_blank">📅 20:53 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">کم کم از ارتشی که قاسم سلیمانی تو خاورمیانه ساخته بود داره یه خاطره میمونه، همرو زدن</div>
<div class="tg-footer">👁️ 6.74K · <a href="https://t.me/funhiphop/83159" target="_blank">📅 20:39 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRTXKDXt-yU_3J4DPynJGQL43QSaICR81oUPOcymwrB2zONQy0nvV7E_OXD2Sur9wcu0PThCy2oRYi6HjaJr2xUjpGuDuYfTOZk6k7M2zLuPalIf4Z96rJirkTBU454CkIEQ7ZkPasxDh5YRXHJV7aSesgb8_l0uAMjgaSE5E-I5WfN3rJ0jlJ6W_nVkn4UFBM0otiLKhMC_ZwbnSs6s5WF7u2Ea9iip8RKRunviabjv7JKVgZgzvVoC3tt4xb5KGl8ydctfXBPaRWghWaqq_Axg4mQLfW-0YBnjRmOnUmVPSgbVvXQSXI_J4-beepuwXcjy-bdW_m7zgUbKmyOQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من بین نتانیاهو نزدیک انتخابات اسرائیل و محسن رضایی نزدیک انتخابات ایران تفاوت خاصی نمی‌بینم حقیقتا.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 7.26K · <a href="https://t.me/funhiphop/83158" target="_blank">📅 20:30 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83157">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCgYhI95hQAgOccw9zRG3hkLz8XMB4XHRQJeYRZFnscuO_nFU3O-5jSEafnHZzDcepNi8-xMwGRl7kOye9w24F5m4xqW-BJogpo9mRylUarkJZrJOcsiHUNIXU3mI3bnPfOpsRoHf3_jesRA3_US8EJr4SOI_iEv2WAK-LTlyN6DhWqFANnHFxoEOArQkCXOi0dqkRVV-wxPGsXAeOSePavJEXQthgcE7LH6qQFDoCK3RPywseA8UCpzEOAq3kV45OhFu-3jksh8l6I4oqIbehslon5Li03kS9IXSSYnVmEa9f-aibOoH31bS55wM-ss344CkOL7Z12KyR-JHoo9TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 7.72K · <a href="https://t.me/funhiphop/83157" target="_blank">📅 20:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83156">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">شنیدم رافینیا و فرمین و پدری کاندید توپ طلا نشدن، دارم میرم اونجا امیدوارم اشتباه شده باشه</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/83156" target="_blank">📅 20:08 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SsTmopRTqmLC-HX2_Gyzk2jjaFzgUsIcIwt2GxwAvXtaC0PHq1OlQ9kM52qH2QNO_eQBXaBlY5HkJNV1SF_yfS-__NLzvArY4mjPkbGL1z6S6Ca4kvwYABUsvmk6QfuExkegaCTbZrPS9-6_bLTA9IW1Iklg4V1_NxY-GSI-VTDf5mwdyDG2ERss4N5ICPDalZZJejgHgbCNt5hAUoxT_ape14yQyGNEuLONmlDFgWQ3ln1FfPJVbr5qJ1w9LxhxDuIbgUbWACnfV5DCaZ7JYAuP9IbL_TNSWsYbTdPM4TItQfGHSscgeX5avfpc_5j3yz0b36dLd_kiNxdUCHtXHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهین جان خیلی عذر می‌خوام ولی اسم این فن چیه؟
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/funhiphop/83155" target="_blank">📅 20:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حصین بنده خدا دلش خوش بود که یه دونه حوثی‌های یمن از محور مقاومت موندن که پانچ خفن ترک بعدیش رو با اونا بزنه؛
ولی متاسفانه خبر اومده احتمال داره عموهای یمنی هم تا چند روز آینده توسط دولت یمن و آمریکای جنایتکار با نوار مشکی به صورت جدول مندلیف برن رو بنر
💔
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/83154" target="_blank">📅 19:50 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه   @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/83153" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CzNT1iVHq3cuGjLhro-pgFwort7rkS2iJ22TLbe06QMpPMEM_w57B3hQHt1PfWhUg69zmxLRYuuoPZjxoPzlBQ_P7HgBQshdb0xmoTt_a3GOqjICyD8ZN2hVPmT44EtRUK0a2bOhmZZ-iNpuHTgPI0bxqk4Rdun8gRttJcP08MBSwErRFtzBHDqNSCwQ18tK-wpmTZVb2_n58QWk6FoR6EIJsCQ_uX6apeNnmyUhyWGyO6H3hRUanvZbvosrFLspU7lEz5WgFZYfLIB7Y2SKSzXX2Elfhq_C6p8s_ca2TUZ1h7lznlTO_d4jlD1l_LrO6WWyvE0g6zvglAYuVckf5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بونوس ورزشی ویژه برای لیگ قهرمانان اروپا در بتگو
🤩
🙄
🤗
🎁
۲۰۰٪ بونوس خوش آمدگویی
🤑
-
✔️
تا ۸۰۰ میلیون تومان پاداش وفاداری
✔️
-تا ۳۰٪
بونوس
شارژ اضافی برای هر بار شارژ با روش حساب به حساب بانکی
✔️
-اپلیکیشن اندروئید
-
✔️
شارژ حساب بانکی و درگاه اتوماتیک بتگو پی و اتوپی
👽
بات راهنمای بتگو و آدرس بدون فیلتر:
@betgoir1_bot
📌
لینک دائمی سایت بتگو
🔝
:
g17
🅰
🪩
betgoir.com
@betgoir
Let's Go To Betgo
🚶‍♂️
🚶‍♂️
🚶‍♂️</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/83152" target="_blank">📅 19:35 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83150">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الله اکبر سپاه پاسداران انقلاب اسلامی: با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم…</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/83150" target="_blank">📅 18:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83149">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EC4arPXn6I_22zqRl_oRtqZcEuOKw5l-VkBgMXP-T3-FwR-1VpspD8QnTIbT7BfaVUM__MOVgYBkfbf6YNIGdNz2OLX7hiwj0Rb91cqWrzd3hI-OxSPI9oT6i_M0ttHylWS7MTDawu5ZQg3UJHPGkZvigTl1SDbcwa0xzW34tdOYRtGUjsx0EbhEKQM7L-J54Hi3ndOrKjY68-9PrGEwpI1rB628j-XSvSgXDc1uJ8gYPVie5QHlzkaZHvxjCD77MEBtBiI8N9NPSeumNg8teIWIshPfG29-6Zmi6I3QOJGj1nc60fn7GQR77JPnPvgtCSfy9U4oXC9rJl4K86BTJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اکبر
سپاه پاسداران انقلاب اسلامی:
با تلاش‌های بی‌نظیر و شبانه‌روزی نیروی دریایی سپاه پاسداران انقلاب اسلامی، یک عدد زیر دریایی رباتیک و بدون سرنشین کودک‌کشان آمریکایی به دست سربازان غیور سپاه پاسداران انقلاب اسلامی اسیر شد، چند ساعت دیگه عکسشم می‌دیم بیرون.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/83149" target="_blank">📅 18:29 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83148">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ta_YxuyIoxxRt0FnUSw_RTyDJlHmaDFmWGPlwCrVZJxwEwsz6oCJWjGokN6MHcu19b-h7UHEzzcPaIdgsMvmNhczR86We1_3veILd_eazSrJFwm8QSyrg6_r-wURRJ_mMOdwDQzqbX-sh5FOGVwvddxFeCaiYiu3li9Ly_xt7egw_hdRn7WO3phFsvb6yZEyn6UjXxt5VxzFnVy0jAi1AC5rxBWxIshbq5KIRHe-Vhsbj4wkv_JozNE232PaQ7oR7NxS_Ri6Og3lkR0xzj5V1t0R2mVY_gsN9waflu_oXy_yzZ2JiFxiiGPEzJLs1CtFLMndwku4cpdJiPg_1V40uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اگه می‌خواید کامل اثر بالا رفتن قیمت دلار رو درک کنید باید بهتون بگم که با این قیمت دلار الان یه Gulfstream G650 ساده اگه تر و تمیز باشه حداقل 10,350,000,000,000 تومنه
💔
🥀
(آهنگ ای غم بگو با جوانیم چه کردی اثر استاد شجریان)
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/83148" target="_blank">📅 18:23 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DPMO0gK95DVGrsXj9lcAJTrjdUkf6VeIATR-zmCEWMJD4TgYM_6zhehJytuBKJCv3J2tteaIEvwPoXp2uGUqP34uRluVuEPhL9bszNw8R-O0ZehwF1a5669WgvjTNnBPR4XN5xKPDRZflBT9hkZG94SqOwW2ui3WD7_GPSw6s4POCiEPfiWsU86Hngk__pdrwqIyBVmHnxoeKyq0l4rcfejhabNEG6zrwE2NicWqR2LjTn9_HAeQGW2XMEbJlCKvhI2du911eleTN8MzC_5nPEv7aStCI_p7nDbgd434zhcuiTCl5jqKrQyBtJP8MFR4S1HYzdZHwyTXGXveoPZR9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داکتر بیرانوند حقتو خوردن ولی تو فوتوشاپ جبران کردیم واسط
❤️
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83147" target="_blank">📅 16:34 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83146">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سرنگونی پهپاد MQ-1 آمریکا توسط سپاه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/83146" target="_blank">📅 16:13 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83145">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">پزشکیان بخدا ما خواهان انحلال توییتریم نه رفع فیلترش</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/83145" target="_blank">📅 15:52 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83144">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j3z5AD_22hct0SJwEO_XD4gTyIS08Ax3rjj4MNOMF-Q5-Jel6cJdGDiKDntR7A-i3jG-xd0-2aVgB3ODf3iIW9eGmhtRfRo0t0sY8T5vCMbNJ4s3CFOqE4tcnKwm0xuaOrw9hfaPYfjggSl-5bEWZBazGQOFo3CAZ6SeUye5HHLcQTCXokiLMy0YuQlu-TLnD2JvyhqcuFVKJcVOAoJOA3rNSBawozR10LAx6bW7rQ1SV-z8XTzFWSZWKbY8bZlS6vtlpYKG-Kryp68nAhL8PF3IaIH7HIZbKRxQQbWwKdVN2SRDGU36DX77fuOonncUwpk9TmUbVUWnK21e-H1Mvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیج این تو کون نروعه رو هم بستن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/83144" target="_blank">📅 14:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83143">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rzm-eMDMcpQBsaLAY4kEu9p-NZnBQPnIC87lWGvJFtfYtMpVmG1_EYfDHB9mGWGgXVOfO6LtXyl8RUt28xhOYNSNmA75BseSWJi1PTUhi0drmi9HjOW1Xj99J-vPHxOfwIXuGuw1LGlLRMM5NxEniovfesbt3r9gHNKJEIWMD6KxmqYEEOfVxwgnsbKcMCOGF-Sk7Y8etbGbkGzzO2fLv-vvCZ2v_vSntaA2NL5Q3FD93h7xcLwAYJtaCRlAeCiPaNvmSGOVO6cmq8wOiKFEX1t_tetve8Rlj9nQDMMYYtCNUf1HyN1S1yMyZIcLfu_ikFXpoqQ1lDBi9PtKK6i7jQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگانو بزارید بالای یخچال دست گوشیش بهش نرسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83143" target="_blank">📅 14:26 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83141">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سامان ویلسون درمورد معترضان به وضع موجود و حمایت از دلال‌ها:
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83141" target="_blank">📅 14:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83140">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فلافل قسطی ام اومد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/83140" target="_blank">📅 12:54 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83139">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=rmXbL7XDXN1EoNG8ftHmumuLYPoeu0YZA0sgKibtJynyP4x0jwiHopKdCTuMcfNyaXgdPPiLiDAO3vXqu8b3jZmYOU_EOzruroxAfqOOMJZQ3BC5fARptolqSuGZgIbXdkCiTkP9azEOkoq-sy3W-gw5cMR7WfjCCG6Iv7RIjiRPRuUcBGX1HX1cwfQyMh24lf2arTOmwBNVDxoE1fotd35LMq1ORacvX0vf71ot23SpzQBP6OXFhDvtnu7VjjSOMIn0hH_wYFNLGOfQvO_8T9p2dCeXMFEvwDh4Iot_VSH70YhBHRFhHot5bfVsVoi6pdyjVwwQuaKYc_eagGlgXg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f0d6cae38.mp4?token=rmXbL7XDXN1EoNG8ftHmumuLYPoeu0YZA0sgKibtJynyP4x0jwiHopKdCTuMcfNyaXgdPPiLiDAO3vXqu8b3jZmYOU_EOzruroxAfqOOMJZQ3BC5fARptolqSuGZgIbXdkCiTkP9azEOkoq-sy3W-gw5cMR7WfjCCG6Iv7RIjiRPRuUcBGX1HX1cwfQyMh24lf2arTOmwBNVDxoE1fotd35LMq1ORacvX0vf71ot23SpzQBP6OXFhDvtnu7VjjSOMIn0hH_wYFNLGOfQvO_8T9p2dCeXMFEvwDh4Iot_VSH70YhBHRFhHot5bfVsVoi6pdyjVwwQuaKYc_eagGlgXg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف پدر بزرگش چند سال پیش فوت کرده الان ی چمدون پر از پول از پدربزرگش پیدا کرده که واسه ارث گذاشته بود و پدربزرگش تو چندین سال جمعشون کرده بود همشون صد ریالی و دویست ریالی ان و جمعا ۲۰۰ هزار تومنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83139" target="_blank">📅 12:09 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83138">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">عارف، معاون اول رئیس‌جمهور: فیلترشکن‌ها اشراف امنیتی ما را از بین برده‌اند. در جنگ‌های اخیر از این مسئله ضربه خورده‌ایم. تحریم فناوری و فیلترینگ در فضای مجازی نتیجه‌بخش نیست.باید با فرهنگ غنی اسلامی و ایرانی در اینترنت فعالیت کنیم.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83138" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83137">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83137" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/83137" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83136">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PVpaYcEnLhZ7TkKPcx72ShFoOIsZxqXYJL5aj9vdWyzIUphFMqIjUlQ0voLPlAOchB8uVybf5UKTGP2lWggJmtoZpuJJtsgTDMH4Z33GOSGqxJR-_EsaI1oXjRikPgbioc8qnbkXPKqRlTd3ax23Ry8peUA_lVge5cpwhjOyCHnJoZ74QC9Tay9MO8g9Hqt7MeSTElg7130jSu3VLg8OMtnvIxtKf64h0O51qWMJqfW3np8eI6JUtJ6MuIO6pHjA8rSESMQQtIJMiF1l5olm8lT5PZVM2hW5bth95QxsUu5DX1wEbsBPnkI1HBF_vfTTHcsAy8U6qBucnmalYXWVsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r17
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/83136" target="_blank">📅 11:44 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83135">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40085684e0.mp4?token=plGjL_2do0YLqSWvqemRsYurycBpkb1Dofvtjlee884pwBNzr9N_XCmb45lEwp8c65hUk-PvNue-sVK_DBuILL_RX3QVZ019GOotyQWfMkqS6x1i1cHBuczT9bnIkfPQ3CEMA6zpY61GV51M31u9yPfttn3XHVVC5cozg8S3khDAL19DYF-MK7_ZSjNNhJs6iRPuawXrc1w_aVZk6Q_8K8SfUvJH7i5z10cmmRczIR456NoagIPFA634DhxJ1N7snX5hu2NFg4F8f7_OehE7plqZbZcAV6yqqjGxNQ9BRj0x_jkVGnmdL1ZmVYG8rfaamu9pKLpe2WNpPBMMhO5s6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40085684e0.mp4?token=plGjL_2do0YLqSWvqemRsYurycBpkb1Dofvtjlee884pwBNzr9N_XCmb45lEwp8c65hUk-PvNue-sVK_DBuILL_RX3QVZ019GOotyQWfMkqS6x1i1cHBuczT9bnIkfPQ3CEMA6zpY61GV51M31u9yPfttn3XHVVC5cozg8S3khDAL19DYF-MK7_ZSjNNhJs6iRPuawXrc1w_aVZk6Q_8K8SfUvJH7i5z10cmmRczIR456NoagIPFA634DhxJ1N7snX5hu2NFg4F8f7_OehE7plqZbZcAV6yqqjGxNQ9BRj0x_jkVGnmdL1ZmVYG8rfaamu9pKLpe2WNpPBMMhO5s6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی بخدا این چیزا تو اکسپلور من میاد ناخوداگاه یاد رضا پیشرو میوفتم وگرنه دلیل دیگه ای نداره که اینجا پستشون میکنم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/83135" target="_blank">📅 09:40 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83134">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X86GWIi_cUndR3IZ101mPLpj_y60yvmEOm4v5HhLyx3JvkA6EURKel5AgYho6QNFNV5Y0-TOXfbgm9ChfyP4dQG988kqO3p191vnQ4HAkeCPywB0XASp344yBNFAU17vlfqW7pH0NGOptvZyxOK9VBDApMNmBgfO8W1nw6uxfvdci_kuy11DKrUp5syzOB7FvG2C6ntpM-CMj_sPHfB3ccRKK4sd7TEB-UFQcDIq0fi7_c5S0P4fVhK0Wyl21GkVYV7ozi2EhkuV5w20SddEuU995SR5ofo1D8TUa1Jp9YW23ghcEpsI22PVLJxVMqhjncYIBO6D8nPS7v7tKt_1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون بخیر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/83134" target="_blank">📅 09:17 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83131">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">بنظرم که خلوت کنید آقای خمسه اس</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83131" target="_blank">📅 05:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83130">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=jIY79HDI4O3et4mcSiGP_GheULuIvndl8uEa4EIKre35LmzmErtHn79dOMTUDd3b_5yOemcZlZIkhQZ2_pMhjnOamiGUMjBBepjtIITOpQEpl_m_HmNqUvu3hpoz6o-SIuH8Skbpgli5ZLQaSegjjKHP3fHV9VWTFYSk5yeTtgbK7xbBZ3e6uBI8L4r9GCyu28QykAMaIC2d4yBY6U8A3PVukmNbFTsRUvKwYYbUEWozpvjX227C5Ype_y58QpS1HdmMsG0AN_4JbqB7Zq26NFv85jrnav7mP1s_qQ-Xm98hFF75crBxCwz1r8651aWGaz3s_QybmuiNQmiU1TWW5Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9fb941baa2.mp4?token=jIY79HDI4O3et4mcSiGP_GheULuIvndl8uEa4EIKre35LmzmErtHn79dOMTUDd3b_5yOemcZlZIkhQZ2_pMhjnOamiGUMjBBepjtIITOpQEpl_m_HmNqUvu3hpoz6o-SIuH8Skbpgli5ZLQaSegjjKHP3fHV9VWTFYSk5yeTtgbK7xbBZ3e6uBI8L4r9GCyu28QykAMaIC2d4yBY6U8A3PVukmNbFTsRUvKwYYbUEWozpvjX227C5Ype_y58QpS1HdmMsG0AN_4JbqB7Zq26NFv85jrnav7mP1s_qQ-Xm98hFF75crBxCwz1r8651aWGaz3s_QybmuiNQmiU1TWW5Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83130" target="_blank">📅 04:41 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83129">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">شمالو سیل برد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83129" target="_blank">📅 04:36 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83128">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=kRuregGYE9LrBEaXHXyhalivbYyyNm8hvVF1Ke0j05CuYcITUwWOciVHivQyoyrVjOi4pOTy7KNXwW2Pw0v-tRJYlZEW_bywUpYRW9_XUIYtjheiAtBbyIUY5k2QilyU457JdTvQC-csbxKyfYz_HpJTjzKWoSaDX_Cy5E4GQWhWG4OsXux_HOVG0cd0Y6SAiUgPRwfRBejj2FaYYk9CVrMhlJaSLkK2dUzpfUICVoHsE7V736XgpTyowR64Gac8tV2N2Z-KfaDF98rf4Ok1bZjGvc-VG5GTzhNG_hSiMNGxbRQ9ZINdw5_l9W1UdltJDpU6pHtw3snHVDuHAyDyGA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc6988641d.mp4?token=kRuregGYE9LrBEaXHXyhalivbYyyNm8hvVF1Ke0j05CuYcITUwWOciVHivQyoyrVjOi4pOTy7KNXwW2Pw0v-tRJYlZEW_bywUpYRW9_XUIYtjheiAtBbyIUY5k2QilyU457JdTvQC-csbxKyfYz_HpJTjzKWoSaDX_Cy5E4GQWhWG4OsXux_HOVG0cd0Y6SAiUgPRwfRBejj2FaYYk9CVrMhlJaSLkK2dUzpfUICVoHsE7V736XgpTyowR64Gac8tV2N2Z-KfaDF98rf4Ok1bZjGvc-VG5GTzhNG_hSiMNGxbRQ9ZINdw5_l9W1UdltJDpU6pHtw3snHVDuHAyDyGA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کسی که این ویدیو رو درست کردی دهنتو گاییدم
😂
😂
😂
😂
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83128" target="_blank">📅 01:45 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83127">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83127" target="_blank">📅 01:33 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83125">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این ساعت خواب در شان و منزلت اشرف مخلوقات نیست
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83125" target="_blank">📅 01:28 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83124">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d524cae959.mp4?token=d38Weq4iPwiHzXsd_nIlQj3kMOiLXS79SJVyTbw9kefxw4hd4rkYbQ_6cB7obLFfgxkS2c_3SdwHiwmuyUT-SDlhG82Oob-DG1rcN_IU6ogBCfr4j7MzbiZoNs10RO7GprO9aN4dltKJD5SbkIh9VE5aMtUgtu1dms_BB2QBIODBa3HdXMVU7gO9lVvwFSCXuG96CZtxhBuXZi1VxNvplrEbHQqCDWVYCILxKhpWo95cpdmwmmKfc7x_JoMyGfILZdh3isF-x-uUfzw-HDa2R75Dgk12naK3RmQqb-0mhmidXZ9TlXgmcg83DlclX-hKAJP47_GEbSkkFW4woWsbTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d524cae959.mp4?token=d38Weq4iPwiHzXsd_nIlQj3kMOiLXS79SJVyTbw9kefxw4hd4rkYbQ_6cB7obLFfgxkS2c_3SdwHiwmuyUT-SDlhG82Oob-DG1rcN_IU6ogBCfr4j7MzbiZoNs10RO7GprO9aN4dltKJD5SbkIh9VE5aMtUgtu1dms_BB2QBIODBa3HdXMVU7gO9lVvwFSCXuG96CZtxhBuXZi1VxNvplrEbHQqCDWVYCILxKhpWo95cpdmwmmKfc7x_JoMyGfILZdh3isF-x-uUfzw-HDa2R75Dgk12naK3RmQqb-0mhmidXZ9TlXgmcg83DlclX-hKAJP47_GEbSkkFW4woWsbTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینهمه هزینه کن زن بگیر، تهشم یارو بیاد برا اکسش دابسمش درست کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/83124" target="_blank">📅 01:06 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83123">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">۱۰ سال پیش با ۸ تومن میشد ماشین خرید، الان تعویض روغن ماشین شده ۸ تومن  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83123" target="_blank">📅 00:04 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83122">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نرخ سوم بنزین رسما شد ۱۰ هزار تومن</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/83122" target="_blank">📅 00:01 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83121">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.  SoundCloud YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83121" target="_blank">📅 00:00 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83120">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_vLQk6ctYL1EirCXTYu42_5dkW1WcM31HsHSv8vN16vBSAK7YVT9jKwz0sLEI_7yI3KxygybzAdJHtEut341Y3T-Cgcm6pRjkojhnDRsvbYfA5NFflbIwb7vGM4kMyIpXdpPM2GL0qp3DkVU89vRbwSI7DhGjXDKUAHKCBsxq7DnWEnepdhM8HHW2WNsxjLovs-PF1iI0r35dSz_Q_OgefBhygxk1FW3__IdqP66zSeTpSN2DDxwF5ue_5DkcG5i4m4vu5n13Kg_4P9Tdru-fEXxj4lIUgUZOv-H8yEIhlhHHXfvxZkT8hBmyCb6C8URbRNuBm_zxxrRjz-lnOq5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید هودادکا به نام "دلی بستم" ریلیز شد.
SoundCloud
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83120" target="_blank">📅 23:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83119">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=H3kjeu_VcvMfOE8Rxn10eJxW1um_I3y-zs3nHcQ4I4k-tIvnR8osjVLhP8OY8hzkPHxPLTrLA4NunT4WJBv96TQJl5633k-ldx9KBK8yOqx56u3wHXC3qTJW83Z2IqzUH3Sm2tFUJ6gu3auQR5ECT6KEeavgd0VvC4cz1G163ZgJU5f7oJlMMqq5Tv8Cuzy3uqcJiiNjtPVB6KsPhMcAGv3YZHGE1KVHEONJJSRMdwAOoyW3ct5X7lsMBe61ur66AAa-dItu5pW87yW_OKhgIcyNcqsGqd61wvutAuui-z6D-u8NugwtxPRiQM0k9r4lpltO2OanL-YJuR3CHM60Uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7248d185ff.mp4?token=H3kjeu_VcvMfOE8Rxn10eJxW1um_I3y-zs3nHcQ4I4k-tIvnR8osjVLhP8OY8hzkPHxPLTrLA4NunT4WJBv96TQJl5633k-ldx9KBK8yOqx56u3wHXC3qTJW83Z2IqzUH3Sm2tFUJ6gu3auQR5ECT6KEeavgd0VvC4cz1G163ZgJU5f7oJlMMqq5Tv8Cuzy3uqcJiiNjtPVB6KsPhMcAGv3YZHGE1KVHEONJJSRMdwAOoyW3ct5X7lsMBe61ur66AAa-dItu5pW87yW_OKhgIcyNcqsGqd61wvutAuui-z6D-u8NugwtxPRiQM0k9r4lpltO2OanL-YJuR3CHM60Uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این پسر کصلیسه رو یادتونه؟
بزرگ شده ریش در اورده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/83119" target="_blank">📅 23:38 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83118">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/buogPUGuepx_YlHA9JOqc1aw_CrpmHsGlVIVTiaH_PifQA9Cf0jJ9yy_MNzW7fkqVQ_94BU6uOTvmk4P9ngvkKWKKkuxm3BGeMYaOC8zXwJXrc17-L1VIKb_rJMwov-EjvfTyaowlMbpB8wReAM-X01jPIK1JnybJLYN-Ev-SDe4i-NnJECL7pAwIfdusoW-NGTNZDHHRwEkrWlmgS6jHQcprSPWuroeyjuT3wLuzTtNT9rOjWVxhq35Jnu2XJ8AGV1MZvQOtr8QH6EhchjeKsuwx_q602-zxJJJRLfUhrSvgGK5xbq6f9MtuZklH27hTCoIXT5kYfOWAMdTIT62Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری ناراحت کننده امیر پارسا نشاط
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83118" target="_blank">📅 23:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83117">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ur587IBhARWu1kORWGSpiuTjNzNFpIdgLW5eLPXGo1nxGAHf59h-EXqaLGFyX68-6nRX-d_mMApSts-kI30dEh-uDk6x7iVBb556EjZrDdyxSaB7aNdG6do006YhjOiJdqBWIKuHsFdvOZSht-dbPasfLiB-PiqSO-I88HKLzzaU4ghdhoebNO3AkDt39fTeRvuyF48qgAJa1ctlbMJDhxY0P20wFdHQG56TnJgpJdm9a09NEn-fNYuiYIrO2KtbIDd-tAHCBZV5Zwk1XTsrS-nbSpQ-iYj8_pC0RzDMf39HyUZ_5lyJQHnvjSGYLLLI7sWJmqwbZ60dnPsdCF6fEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایبرلیک هکر معروف بازی GTA VI اعلام کرد نسخه کنسول و PC  از بازی را استخراج کرد و بزودی منتشر خواهد کرد.
اف‌بی‌آی همچنان دنبال این فرد است.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83117" target="_blank">📅 23:07 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83116">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">مارتنیلی تو لیگ عربستانم کیریه</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83116" target="_blank">📅 22:58 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83115">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAbtin🇺🇸</strong></div>
<div class="tg-text">کیری کیری کیری
واتساپ برگرد تلگرام گاییدمون</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83115" target="_blank">📅 22:52 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83114">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">تلگرام جدیدا خیلی پر باگ شده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/83114" target="_blank">📅 22:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83113">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aWh-jvd-WAr5exDw-8_n7D0XX7mIkab6i4af-go5M29RhEVrWsJi7VnK0jZyrBLL1Cx1ZLWyLPf1jEuRXN6NL3Da3wLBP-XsP3wNN68HgIDPUIbgi5uXjC9PNjskLZ_IDDnn7WK7ifapVhRgTx9-hShy4Z10H9WgEU_6fHqYAHa6MixGcrq28tVFavN1_SzQ9o4Q3H-5Epwh1y5DgoXvF0TkJGGsnSqfCinB4I-8nf2pffm9NmloPNqHtWpv2Opx1EmUIA1SXrv-i8vv10EmM-YP9-lZOwICu9Pwv6u2ZorP0HnjSe4FIr_erS_h59vEDyXh5cHR467R2uEX7TovrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدایا از ایران نجاتم بده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/83113" target="_blank">📅 22:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83112">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=i_VMk2xB-oMckTyYSKhW5gp3PKlFdxrksLVUqU8WU2jZBrs643ZzuPdPz_UYxIxR7-UZApm4E7cmimjLYrP2nP65ASBngUBdjrlW8Kgtpd-A50EPtwjValKjBMZcvvXWIkHlgdm29I7O4rtFZYYeUFOHmyawRX_0LfgyFTshlGieFgI5YPmvibRcmKodjQtZis3GRAi7fg9UXkdOLs7CweJA0BIcpeQwlz8tI-3z7swgxzI2CW1ttNMGKBNU-gZs_iD6Ee_To53_b95qzKZzD0GrpVLhw2psgqgqnm1-77W6aV3CCsk3vr4KeiDjpRy-fe2K1LEiMwZmPBtY7FTWEg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e5ffc27d84.mp4?token=i_VMk2xB-oMckTyYSKhW5gp3PKlFdxrksLVUqU8WU2jZBrs643ZzuPdPz_UYxIxR7-UZApm4E7cmimjLYrP2nP65ASBngUBdjrlW8Kgtpd-A50EPtwjValKjBMZcvvXWIkHlgdm29I7O4rtFZYYeUFOHmyawRX_0LfgyFTshlGieFgI5YPmvibRcmKodjQtZis3GRAi7fg9UXkdOLs7CweJA0BIcpeQwlz8tI-3z7swgxzI2CW1ttNMGKBNU-gZs_iD6Ee_To53_b95qzKZzD0GrpVLhw2psgqgqnm1-77W6aV3CCsk3vr4KeiDjpRy-fe2K1LEiMwZmPBtY7FTWEg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.  کصکش پا پرانتزی
😂
😂
😂
@Funhiphop | Menot – ویس فحاشی خداداد</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83112" target="_blank">📅 20:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83111">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vB-KGaz7riqxidxJRIGkBaZhycekzdq299BfaO8jLV3ssWMYM_PrcHqoB0wA-uskVJnutyJnT4hCG9EWb6J2TFDWWMIhZP_IxjfAL-9JZ8A_-5tDksnHIugsoFbgAMs3aR8ufWpLL_lbCjDeMfV8X5JO3Wk8Eqietf12rp7VZkg0g9K2246yTCzW8hkAfzqpLz1Pod6msP4qrsGcaMTEAbawnKicwOUYAQIfL8ZR2XcSE5r3qG61RiP-s0nk5IJTfjpWPQNL4rtJOAA6K1ItJorvfZKpGlN7O0nEimrmS4K4a0yDqtvAbcGzei0yTZKMrh996660LGuePu5iH7R-_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مشتی تو با این قد و هیکل باید خیابون ببندی، نشستی با بلاگرا و رپرا تاک شو ضبط میکنی؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83111" target="_blank">📅 20:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83110">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">چرا از کلش آف کلنز حرفی نمیزنی</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83110" target="_blank">📅 19:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83107">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حالا کاری ندارم ولی آدمی که نفس میکشه قطعا عقب موندس</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83107" target="_blank">📅 19:31 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83106">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMpMV9AS367TIaJ1q_nUKgWTruvzigTU5OnRTnV05HwR4ROv1PxhIT_WaaKDlUQHzMRpFlX6B0EE-akGbg8TSBhOLKEhtKIphlxp_tGX2EldWBDt1yeknU8fdtSwoh4muenlNdevaX8DO9taWcJQlPrH81E_ZTqlg67LPuOa4T8jsaJ4sKfKVFaBIeKbH-UaTIiEWCr2EMNHiKq3USb7_11INmDfxSzkFDKNdrs3zMA-a_b8MjD0_fg8UGQKJGUkf0RGw5DiycmzAMyQPOwny48By4EMiK0sBWDSRlN8HzjGQOe9eHF3R__fWptvxc97cA4S36DZPaCz8iJRp7BsZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقب مونده واقعی این پیجایین که از هوش مصنوعی کپشن میگیرن میزارن زیر ریلزاشون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83106" target="_blank">📅 19:16 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83105">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vZl67GCYcoe6A908dhP3jApd14WQPgUDKZK_U7hIemPyXO0P4HItOTXz244SRMKX6-Js8QbQJlJ7AzTzAxETlbmkkaT-loLTuOOA82xNnsW0eUk2pk1UEi5kyGkgpIHn_GbU-0moIox48y-xTNgIV3nYo9gzvJCbO3dZfmmBZMLLaqJTclmrzvNFZNdHivRjFHTJ4Kd-sx-yW8kL06-o98waDSAA1kMcpu9KenjBXqwyOawANgFQOJEWBDS3d4TiMvgL6-uCPh5SzbWJVxxl_qIXIA5YSk8uqKq3Ib2fSERNJGiYzcP1G-1QTLglEx8svSMNIFNpc_sa-UE826dgJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فکت: پسری که اکانت توییتر داره و خیلی جدی توش فعالیت میکنه عقب موندس.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83105" target="_blank">📅 18:59 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83104">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=hcXB6IB19KpcZXV8bIal5ljfHWr-iCMig6V7afKCrk1ZdMGMb8ba5_g2hWe_8Hqf7paTQc80DY2FABaNT8oQp2c6Gtf9h9cVYGxNNLGcoSWJrtODgM1FcV9FQbxm1co5CiqAFcXcaxzKjZTTQaVyhKrmErguLzv7FjO0opvI0jjaYOO3NvgZ1mtUVk8JUMx_fkP8troWd5uASfAUJZSlF0YPTrfOY9dPuWNlhsw5L3rowbWLUu3gF_FM2KpGj-ofAAdDoW9RFhpJdMEcD_qYHB7MVtphoZJA4astIiVofTcngR5hKYUuLPdRa-C4cjmdKCfPYHOevkHdAeDTqYTy4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d117c4a49.mp4?token=hcXB6IB19KpcZXV8bIal5ljfHWr-iCMig6V7afKCrk1ZdMGMb8ba5_g2hWe_8Hqf7paTQc80DY2FABaNT8oQp2c6Gtf9h9cVYGxNNLGcoSWJrtODgM1FcV9FQbxm1co5CiqAFcXcaxzKjZTTQaVyhKrmErguLzv7FjO0opvI0jjaYOO3NvgZ1mtUVk8JUMx_fkP8troWd5uASfAUJZSlF0YPTrfOY9dPuWNlhsw5L3rowbWLUu3gF_FM2KpGj-ofAAdDoW9RFhpJdMEcD_qYHB7MVtphoZJA4astIiVofTcngR5hKYUuLPdRa-C4cjmdKCfPYHOevkHdAeDTqYTy4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مگه ما اینهمه شهید ندادیم عراقیا نریزن تو ایران و به ناموسمون تجاوز نکنن؟
هرجور حساب میکنم تو ضرریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83104" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83103">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sk5orfuexcnWs6wLk5YwKSfvqT6icQY1WIW6Fn3_zzLkjeeTCnIwb_TCpCtKnrxWbEVTnM-yq3G0h5taQrbzvv2rk61Omyz98ErgyVsIXePqBQpthAXWjJRu1wb_ezt9RAmo2sZg0FLKI0JHyBFx9oKvgHXlMi8rh8UpD_W6-MAXKInPi62IziB1zji_8J--Gy8SsL0tmwfkK0F_tVNv6Are4OJ0UIKOAU1G4kJ2CsX1vnKQSpcliYm1YrIAHzlGmzPTNtoqa-qwsU6HJZgZtCR8blJEiXXx5Mvz7c2FC0cJOeN0Lt0zA8sdnTep1bPV1INCHe6pObtqD2Pkpir-fQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥇
دنبال سایت معتبر و بین المللی برای شرط بندی می گردی
⁉️
🔥
کمپانی بین المللی
We pari
همون انتخاب
🔥
👑
سایتی برای حرفه ای ها
👑
🎁
اولین واریز توی وی پاری 2 برابر شارژ میشی
💖
🔔
چرا این روزا همه وی پاری انتخاب میکنند
⚠️
💖
شارژ امن از طریق کارت بانکی،ارزدیجیتال،ووچر
💖
تسویه حساب سریع و بدون احراز
💖
دارای مجوز رسمی Anjuan و curacao
😃
😃
😃
😃
👑
کد هدیه ثبت نام:GG007
👑
ادرس سایت:
http://til.ac/z5jcpGT
😢
سرور فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا،کشورهای اسیایی
👑
دانلود اپلیکیشن اندروید
➡️
🔥
کانال اطلاع رسانی ایران:
👇
g16
🅰
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/83103" target="_blank">📅 18:47 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83102">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">امیر پارسا بگیرمت کردمت</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/83102" target="_blank">📅 17:48 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83101">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">شین:
پرتاب موشک بالستیک در هرمز.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/83101" target="_blank">📅 16:56 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83100">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZOGQxPR5tGu_nx1YlgEdloeA7WWRcenVFDTa-IxRAKGm0uAsawxxJahBRr5vaxgStILlaQewEuxBVAUKx580h1T2CYSFNMbqkY8MUTi-cK4-9MGcybWWNMkOgsl_ds-TC9uvSnqowsEw-3n_CvMMxMOvv0KgvwJ8o_kaJH7lfMzcqV50_m4gGGM2Nd8nGY48oXITsy8DNl8lvc5oPuCnHUksaXPXoEq4oU-W-q4dEbTh1hsgafetH1mupf3zjtoWmx56lndYN8EjLRZ62oMHhvRty4z5P6M8o8ifeNmCGaOH2l3UvSiiHOxDc-OJrO1hoWe3SlOJRP0E1Cp-ZhIz7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان بد رو فرمه پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/83100" target="_blank">📅 16:37 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83099">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mcm494njI7GGhuvNoLqs3aSmRj930GkdNRWB9StKLOYYgIOuYqgUuBUtmTLFsFLBMtvuTMe7Kdc4PZkEZGAh_U6lOar7DoSjcb0JEyIfxehoSlNFzh_tZfcZOh7cdG8KTTnzszRO2Lwx77J06mhVfWLuTYI7ooHaDA4mfkMiL8epc0p0Y_yB8PqZhaTs90cttVAhlFXONKR9htMd9CfPG8IHrT1dnpTQtBGxJB0yBFvyXObGxZ13CFOvcMCRTclc2ztwlc3KuI1Ke2jEG4FzsDfAX-ZHTVjcZBZdKLQpdRxkVwakb87FX9xi0bSypxfLB807zddEwHIZr5yx3YCcqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عرفان میرزایی، هنرمند و معترض جوان که در دی ماه بازداشت شده بود، دیروز مخفیانه در زندان دستگرد اصفهان اعدام شد.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/83099" target="_blank">📅 15:21 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83098">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">ناشکری نکنید، درسته دلار نسبت به دو ماه پیش سی چهل تومن بالا رفته ولی نسبت به هفته بعد مفته.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83098" target="_blank">📅 15:03 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83097">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویس جدید علی دایی و کیره خر
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83097" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83096">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ویس علی دایی و کیرخر.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83096" target="_blank">📅 13:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83095">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=uhgHhR7W2-dsokbWN2g9rI1SCEugO5epT9zDkPR-EbYtrAAxfv2SFi3zK_3iUzaxANT2f5VIF8q3pQHuPkBpOy_ZOqOCns74psYTI1owtaUrq016LvRcPFA8p94W6FHMzxeSrDA_Ko8jd-qXKDE5jmc7pScU6FEQo2-5PLqmb4s0LQVeKWrXZ-vtiZf5qp1Utd7rI-iGia32jzPXmuhLBVn5JvPpNesZvOtuLM92SRXhhDA7s2WLpLOKfZo23_Uyeszhl17RN7_bQoD1SN_5RP7-Be1iThxpTbm6tmscH7RRiBhkaWiNKyv1QU7d31H073TLokytAUKkGEMi9afm7A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af2b3362cd.mp4?token=uhgHhR7W2-dsokbWN2g9rI1SCEugO5epT9zDkPR-EbYtrAAxfv2SFi3zK_3iUzaxANT2f5VIF8q3pQHuPkBpOy_ZOqOCns74psYTI1owtaUrq016LvRcPFA8p94W6FHMzxeSrDA_Ko8jd-qXKDE5jmc7pScU6FEQo2-5PLqmb4s0LQVeKWrXZ-vtiZf5qp1Utd7rI-iGia32jzPXmuhLBVn5JvPpNesZvOtuLM92SRXhhDA7s2WLpLOKfZo23_Uyeszhl17RN7_bQoD1SN_5RP7-Be1iThxpTbm6tmscH7RRiBhkaWiNKyv1QU7d31H073TLokytAUKkGEMi9afm7A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/83095" target="_blank">📅 13:04 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83094">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">رپر عزیزی که دندوناتو طلا میکنی و میای تو خایه های دوربین باهاش فلکس میکنی و به دشمن فرضیت فحش میدی
بخدا نه تو ترویس اسکاتی نه اینجا آمریکاس، بزار درتو</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/83094" target="_blank">📅 11:51 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83093">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oiCaErGpjFq93E23PoQ4qlGk9Amro_Uugv2X4lGolu3F9hOOT3ar-aZ_nMdgYhPkS8GGbA1MZTgSGZlTIQlMnls3vCZA5Mrd-xhQKw2RWSNc7R-jJqsmd4ci6YzkhcAAW9HCC6PL5bzZvGGDfLxgIvQ8qgpIxlJ_TtPk-Z-Y788P2NsOFbTiuaFNh9MdYytE1EdyobBWV6iHfUtVcTAWHpOsxmSfZd-0uXZmUwAph9mr2ejjd5G-5AdSGKiazkIbShyt9tBmnq3QXTfnuISXRIHCF38kwAl2nia_c0Vngn3X4YzKuLNGierdgRCJDiIyrpgeqbFtjNUoj1tRyM4WOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استاد عوارض تنگه ما چیشد استاد ما رو پولش حساب کرده بودیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83093" target="_blank">📅 11:42 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83092">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی  شاه کهکشان راه شیری فتوا صادر کرد.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/83092" target="_blank">📅 11:25 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83091">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_5xkpkkSFOG8x8xsMxUUmf5Lfn1RZRnpKyFQQs8H9K9iPF4s1VRPZOYa-mxYil6nK-UAdjYLsh4Rg1juT8K6CGundskIwWFW2sw-ijGfFeoRvseQSrWce0ukZXsEKDDZx2CRtLrPKI1uWehSnp9FN--4yzKeEtEZkKBftp3BnUgBUk3IMXGGT7rsBgNuoFgR3pUBuosL9nGUqYjlfLl5EcVIbpt4NbfOFBHHZyL15gmvL3Q1AYx41sa3qR0w7PzKoZwyHkQ9wvmhlWDqKbvhltSsvFZjyy49j3f4rcqScHp8pAgj83EkeCIn_IVx0Xl73JKf1SVrxerRpO--rmdHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید پوتک به نام TiKToK منتشر شد
YouTube
SoundCloud
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83091" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83090">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">wepari.apk</div>
  <div class="tg-doc-extra">46 MB</div>
</div>
<a href="https://t.me/funhiphop/83090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
اپلیکیشن حرفه ای اندروید کمپانی بین المللی وی پاری
🔥
💖
امکان شارژ از طریق کارت بانکی
💖
تسویه حساب سریع بدون احراز
💖
دارای مجوز رسمی Anjuan وcuracao
🫣
ای پی فیلترشکن روی کشور مناسب قرار دهید مانند:المان،کانادا، ترکیه و...
✅
کانال تلگرام:
👇
💖
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/83090" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83089">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fiK52ZfHbC9r6-4wegufmfrQ8BnPJcdgTGa7a3v_xkZpVtmq_awzGBi8GBhoh6xUVfg5urCa6W-StBBzH7L_vAzf17lkiquK_zQ6LmddRuYr87YmRO5frHC44G-uYKaZz2YQSwSZgoWhkdUXYf5ktrsCnZZi5a1fG1g3k5moPLY7lCOEBrud_Hk7smnPj_avplCh2PN5j4qRVZeuXtwG2fmhm1HDGrZJjOvpeLkc-2dsgO0r3M5DfWU-Qa4-J7RE_RF7p-AGgouAkrg0fyNNgYeS56LTvmBX3Eq-z8TLwpwm4XGqk5pLgzocjP1yLMPAbR3-BAcjHFb4q9_9GxAA8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
شرط بندی با سایت بین المللی تجربه کنید
🔥
🥇
سایت شماره یک اروپا حالا در ایران
🥇
😀
😃
😄
😁
🎁
واریز اول
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز دوم
💖
100% بونوس هدیه(2برابر شارژ می شوید)
🎁
واریز سوم
💖
75% بونوس هدیه
🎁
واریز چهارم
💖
50% بونوس هدیه
💌
کد هدیه ثبت نام: GG007
ادرس سایت:
🤔
http://til.ac/z5jcpGT
💎
کانال اطلاع رسانی ایران:r16
🅰
✉️
https://t.me/+VKiCVNmMnFM2ZTU0</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/83089" target="_blank">📅 11:19 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83088">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GqHifiDXSPcbEMiQr0C_aivdchYmZzpl-YN4_D9X9bBrnvrILykl_CEzboRNzLn2PnfzpW851iKByXo76wm12gY881IMjFhyfWitBeyeHYroNFipV9VKWhk_kZ-ped-m7XLfgLKz-tAryJFOoQsjh9iPIZBdzO0Svw5q3Y4SnjqWyR_fZXjgyQGLaSRF4jWP6Ui8mzuLOCBUfZ5Mkgm9Pa1QqRazzvEf3qO7WXTgdkGxKQpCsq8hKtbJT8HZwNYUo2uKUydR4PBncEVvlUnjryEUX3Gs5S5B5lp6z04aA07T57XSNMG-fb7uRAQGJbUfFcMBeq3TAHbSUPV_kPI1rA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#پست_دارای_محتوای_نیمه_رپی
شاه کهکشان راه شیری فتوا صادر کرد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/83088" target="_blank">📅 11:15 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83087">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lJnvq6E2xca9XLQb2FxUP9PuKcd16iJqfNn-h8BhD6P5_R0QrJjxM5FlXW7L_hz2nmBfn1HEt1qFWRIG1JJAsF1Yx423c2oKLdh_eRJHE8KFSmZO-MsD-9Sdj6Nkte7nBzTlr7W0O-_5zxz1alj-OQBXUn1WaztMCrwjz5gJGrjsfAy-qA6RV9dqfG0pIBTFgY2DDSkUgqvTRv2aGNlvOfi2x0IHMn2br74RRIF2SmCduZ4gBCouY9gj2Hhnj90LRau9mcjMrtcv17aYWTEcuSIOs44sGBhnQhziiJ1LKLo4S5Gn8thEmVRuUVwWrQ85dhn7mTNh-X-2WDyuNFZ8EA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صبحتون به زیبایی و درخشندگی این تصویر
❤️
😍
😘
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83087" target="_blank">📅 08:35 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83086">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مثل همیشه درست وقتی بهترین املت زندگیمو زدم فهمیدم نون نداریم</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83086" target="_blank">📅 03:23 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید  یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/83085" target="_blank">📅 00:44 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83084">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56316020cf.mp4?token=Tiu9d2hbG9GXwVc3i6bRWvWCtkSjqXccxu3h6B1vh-qy7kU3vtN8Z7vi8KnepE85ojkjDq1cRW9ggu-WRWx-7Op8KfSAvZg4bVHyL_ZzgJ1FnyR3DHGhLhRbKcB3-jWP5z-xZnG7BA1xwDqENZ41iai3IZ83cvqV8AvLBy8Qdve9G-T7FHGNYbJ2nktpsNn3gCF2tg3Kw2sJQkwBUtHMFPZTGWWVOHJUfM6td3DdQgNYPFSpKKdJU8AI9QxOyZeH1alg9u6b9vAHHOThzJw5fNsx_8b-TRnHJLNJK-TpUZhP--KISsLTUFha3SlCfk7aFP0RLnwxbmDkP5Ii3goGxw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56316020cf.mp4?token=Tiu9d2hbG9GXwVc3i6bRWvWCtkSjqXccxu3h6B1vh-qy7kU3vtN8Z7vi8KnepE85ojkjDq1cRW9ggu-WRWx-7Op8KfSAvZg4bVHyL_ZzgJ1FnyR3DHGhLhRbKcB3-jWP5z-xZnG7BA1xwDqENZ41iai3IZ83cvqV8AvLBy8Qdve9G-T7FHGNYbJ2nktpsNn3gCF2tg3Kw2sJQkwBUtHMFPZTGWWVOHJUfM6td3DdQgNYPFSpKKdJU8AI9QxOyZeH1alg9u6b9vAHHOThzJw5fNsx_8b-TRnHJLNJK-TpUZhP--KISsLTUFha3SlCfk7aFP0RLnwxbmDkP5Ii3goGxw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه ناراحتی قلبی دارید یا با دیدن صحنه های حساس حالتون خراب میشه ویدیو رو باز نکنید
یک جوون تو همدان به دلیل مشکلات معیشتی خودشو آتش زد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83084" target="_blank">📅 00:39 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83083">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4lLOL3h1hWfM__F-H_SyTRGM7rD5V6I8jGOverlED_MLeVSi6ba6TGHVIidOlCT2veG-wOJzoGAXFFlHMzy2wjkNYLLsDSYxCXGObSNXyEnojGOkVdPbvbjKItlKQLyh05hxVAP7W5morvLrO3fyr_AP_9c-jlz-a-uVlR4IvQfoJbervrBoQ0EsmE9jgueYLUMsEa_5ivlUZJJ7MpNnva5Ao2DXyegJTpPOp7LiC67FC6H-usVbvCg_1kscdxjbOOWWsYZ-C5B0uB_yTCxTqPoNqlki0wv6k8mG3D1MViPDRsHBy9GObA0gnWFd4qnr3yiZJApJ9X4o64Qk39hPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">به ک
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83083" target="_blank">📅 23:31 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83079">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/c_Dn-TIoAMpiT4Pu0xcWwMign9NHXT1zm0_qs65bCwlHAEHwsjCSBoWiL1BlwCA-kuETsBLPdEdzrbG3pSKMoJbdFUygWCe25hIeBUYqiQxUqxIK2fpXnhTA4kBgJtFLo_gTDOrrT1RFNGyuKJ_Eb5mORVj3zIMPoIMKYufuZqw6Oc-kY0imd26pcofzrK-J36Bt_sVC4Uu4An5GewFlDxAboMnCEUCBHzsY4XqlXwXkuTBLnblDwitbuy_VnpnNZ2RnVsRRnSFPo3ugY17eAMpmCRHsHgeQgqu-f27-xfu7nZyyp-d4fOXWqRx38c_LBuj8YzqXupZOCOCRJXGXzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkJ-deCVEEkUE-KsqSd6fDdQUWteosiWl4hdE4mU-tlkehnQZp8lY3_-32AhZA1-UrlsS2nYYOrj9UqrsMqlg29iv4_4RdF7hIev5RlA0qmg_WiRcUoAj0UL_3_FIhPksTBXi31AjQznj-j_XknJJ3UaYLEHL5ykKAuJTHSizcF6Dz9AQvqsEZEZHuX2ywyOUjcX2HJzEyaCWRPdAXI1EFgszxje-Pk9btHXH6wR_DBbmmyEDCufGWb3XvH1e5ho-7zhTMKjtZTNjZnudaSU4F0Lt9CMtTnDXA4rglJkEwGCbUSRYKEHfBjwE0DktOMtFzPjx8l3vfd62VNVg5QE9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TXLlXkt-Czzm7gpJcIhejHr7WDeiIWJ2ua_NQLCgu2YveURyluzIIFmBMXXbtbW-TFOEQo5QhiLda3pp4BYs4hxdxPw7lZjLlS_m7YiM7X0fMvIe8_w4ffiMCkR-hoQWwcUgQrs3THsPqpbeTnuMAZWnK1azKLniblm6SOrEmhSsdMiIEdybNb5hbWbaVa49qBSVkZRHGDnpylJvd4r0PB5PTmUZiUiiSztnVFZtdm4z52de83Y4P5j7n_FBBu3_ASLElUm-NbPKWOhOGhlikzKZxtwrZbmWvv1PujIVwmw4mSaaqZ8VdKXdGLzItKQP6gxNPOsiIRxNNkt2XDT8Gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qj-5cZJYd8o2Tk93EguAHI1JBodEl6v8xanEw-lWFXkx8LC66CQDASwLQYRAYizdtmhTVbzRTp67_7S2uWz7LUewgjN1wsUh6szgIKC6rl3Eln1b7OMqqJZGh7Y-aDtoUwCRv-beLHLJt6Q-0dHq5cb5QK60gMAwEMvSlx6bxBtfHjrfWu04vShzqfmkDBstNdVwNN8K8FitRMmslikIstSRxboZgpptDNELvVQFg6z4-CpDWbilJG4nhH4xN5MI_uFsiNblEs873qTu5veToU7rCGdKXh5eQvT-l5djcPfTSenFvJGiQLZKbn6pnN51a959K-ITzfeBINIQF72XOA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صد رحمت به سلامت‌روان دوست‌دختر تلخون.  ترجمه:
ماه مال ما است
🇺🇸
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/83079" target="_blank">📅 22:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83078">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ia5UZKOx8yiyKWRe8oGAMRQZNSrSBQWjyVcIVAQKg-GEK0TsVIhodYu2xDdzKrZ8kopZYjwIiZfTivbKmNaBQCRT5uEPM55Zog5fVBOBu-9kKoRzd8ICyWGlZz0CahRzNRcjcYrUYi5DLE9ibbadaFEYT13YyB7YEgr0MKY6QF9HcZbrek2NU1rtipbZ1ILUVl_gH4A1J3ozFh_P6KqX3DAg_j8tJc58MxpPqt3Mqu69RXf4OYKYh4eLJ7WwNvaC76h_J05ZscNEjXPtfPPPO2Mk6Wfaaj7kPtt1_6XzS7IuljiF6N_4TlcuJxRax_cO9Tci1G0QEieKFDnQoV2H_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛ این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83078" target="_blank">📅 22:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83077">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FYMCfX1ryzebe5E1s7TjI7OoupncLFOzTcKwlKYky_OexLY9f3cLj1Djv2HvjppecsRmYUAHtzshTeeeOFWVsJLjykluR5q4JTXGNnsRxiexMpeMJiMSP0WartNbF2TAsze6ABhLBncx8-T7pd4dDn9bIfWC2IxfQGaseVQykWk7i6KSoRc8V8o_yxPlwOkomHwnOpCe17yrwzS1XChNflhVoY2ns6L--mqi-JC7mkuZADagP15BA6A9DJjqiwuWZ4kHoTvK-7L-qrylToMrKZdMT_hfdf5J--lJSEtoirQxWHogxEGoDVQWMzSk0-BWPPvmc03NWm_dKt8KOTR1ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من حتی خایه ندارم با اکانت فیکم چنین کصشعری رو پست کنم؛
این چجوری می‌تونه به عنوان رئیس‌جمهور آمریکا چنین کصشعری رو پست کنه؟
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/83077" target="_blank">📅 22:06 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83076">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">از امشب نرخ سوم بنزین ۱۰ هزار تومان میشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/83076" target="_blank">📅 20:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83075">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JWDjvXiqVIpoSM8sXLCLB0xHnE3WGPuykCz_WPvVm1t22VmazszPBTyGILUUCthVgkpJoSQ5PhNEUbtEMFThsEfsEd5sz9w_EuAIRATsP4t7QIWei3X8rndgET82hjm1omtDRUM6njvS9vjh985_XszzvgFtOmJeMk5NEhzH1tOzXfQaDapWk1hVdC1kqxv5t6B4izMFCmYiVQ1_j31MTjUmh47WxJtiqRcqhJJehY4NGSEv9zoigUqhWygzlyE7ytszNAMPTaNO36CJNmYi0guIYD90S2W9-fhnwFCdgykY-WoL8hQUaXanpJwaVxH1pLq-RjASAysTII87gqYK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرمین صبا میره براتون نونم میگیره</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83075" target="_blank">📅 19:47 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83074">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bAnKl8AOufFiIloPMkT4dtVYvv36dt-INAjGYfIJHSsSQKr6DbsZWazr9qVDsvJI7kqXZ3RN3tTLqC4cgqIKl5K_Z2_UNEEk5RdGvwVGjHtPjkrZHoJgtiGN-eNa1MeYhQ_4tJf4xC78XBUXQ5ys676Y8Dwfb_j_z4amDa2TUvC8IrqpeOXL_3Xe1RVVwDF8Wd91ldZv39y4T_UAc7KKrt2vzsTmnfZmMRRrzE6jijYmo3bcv2xb-SGIRm9PevtIH7PzkIelNNEHpGnAvxkeuM9fbFphzjg1f4C6k9qU4VdVDWQrO8sKnaKjFlLzyJq7XlEJQkHg5d38nVa1QP_cuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداش به خدا یک هفته از درگیریت با بسنت گذشته،تمومش کن، به خودت بیا
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/83074" target="_blank">📅 19:20 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83073">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">کصکش پا پرانتزی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/83073" target="_blank">📅 19:04 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83072">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">منچستر کصمادرت</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/83072" target="_blank">📅 18:27 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83071">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y9sNKzzb8rKa2Qhq03Acrz4JFKMg-MYNx-qZj2JVHTdNAGHaDtoI65UFsIkWEJaQ6wvtvNCKwYH5QB5mJXvPWmSPtvUlkcIpOOc1XNolmh-1393TSi6Iyn5oaSl_CTpo9ddzzL3D8mX52kmqWurXcgOW5h7hHTpRHQ_AiZMalZkQhfkPJwJmhqGbXKbGDOkiqAaARxSfkI8evnp-Hh8pD5wXbFFaexG0VxfXKTqMOqt8vkphWzz13kKF0bbINE8X_LO6ToDLpavwyNoOAf9rwdr5aaDQcuUApE95oy5D3nFjuvMWh_m_Q3o3qo9uHnbi5lFN0z2WB3s9rxhz37Qk7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">باز خداروشکر گفت روحشون شاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83071" target="_blank">📅 18:22 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83069">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">فرمین لوپز شاهکار بشریته</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/83069" target="_blank">📅 18:11 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83068">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gle1S6fDTZtyctYWw0d9IIq_VoAjtiFWO28zbLKJpFg7gTu30vBQGLDv-oRxgrEwaXZrLkSIHuLQcyJuv1txcKh3F3c62BLEVqPLzrX1lca-hgwiCGulu1aWitTxJgSxDEKskkWaJpee3bJtD2kGW3k4z-d3LBrcWpTwFUHvDq4r6DzOI0LU1fWf6VKAv9Btsi0Ex64_A9v_JkN4WUMaqgVpnxs3xfSG4ZSEqB69dW17VPKABEIrEFDmv0PRllIx13YCzskexX5SYjZ_nomyAlbSbNBw4r4ji2YhblMNu-AZn1UVYzt5jIp52TiA4va1G_8dIjQ1ibjBsIoccjNweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داداشم آلوارز نفوذی درجه یک.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/83068" target="_blank">📅 18:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83066">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EDgzQI22qYyxEfz668Rn8ZNkrh3lWH1GD8H18tmT7-_d2MEFRdDhPZ1Bd3_liaOVPGnmNDS_AbRbpqff66S94gD-L1zmCJ7ArwFt3kmLhMTnZM5TVw6q6Qbl60lZbTnqCggHQrRvuwF0wJWT7XoDgRINKc6KAtbGvCu-8Vcwjpj6hcIf_1P2C_C_kIzLBm7HUgjiC6DeKCQgy0ZO00bLJoVyizQ34YbEFxnat1dlLvl4DdmqRO5AaOVddplBjFH07OYJy-GQXXVY_4M_Wl3oEyhny4N_-DRdfJQz7E1wpWP8Q9d8-5TtJUPriqk8LBe5S36W1COIKSE_DoVz_u5Z8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بریم واس شش گانه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/83066" target="_blank">📅 17:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83065">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NlMxMGt_cYHsMu6ONnHOsMeZk0z1EopNGNOj3bjVdLdiZsAORL08IT6EEumUvcazqpFQIzPkcIIz-G2cgx_9Vh2u_Qb2qbCXEc-W3ezADNENczX67r2Syl_9LmuUr16mGXM17v4rgaujR4QDPVjf3C3_zH5qbVIc9k7L3dpDDYzhyBoZg3KRZIrYrwXtAwkLnUrSDB0MVe3mGnc9U2FvWnY4BGiCOsyLlhwtGlgOtZuQf17ubBDCPobKrpfzk1DEAkO3CoDjRutCEksa-ccFWpMoO-tRvib90zQvbqxa2Y62XUc7-cBeqhzzUdn120Nc4n-m3NVvDWGCII-g_y4xPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به هیچ عنوان برا تازه کارا ساخته نشده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83065" target="_blank">📅 17:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83063">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iFWAjXnQvs3fw2_WUxz4ZA0Zut2yvSEWR0wA3RgKUpiAkiG3ZbC2I68VjQ4tdjeRYGeYrUVo8Lm3MtoWZncsw8cFz8Ttgh2r30VPPiPA_X-z-ayQ2nwr35oQjn_CHwRPPJclUkSqEsW6xP-U2YSdH7k1h3mPCs-w5yaQ7Icxf1R2YjZRAqH6_b_TUuoIXtviCZBtC23VYYqkJFUIteCTFLJ7TdXXmGe68dZ7BId4whiQVXuLqIN13VS1BuJa0VPItkEtGCVBKc4MkbRvEvDl0ptB5HEHbGbWp6X6CVZinXo7e_3vz_mCzCECh4TiQDUMXhyXe4kAFU8kZgWaNDmFyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=eOwA-TdS4sBMOlDgY1KY38hLAScZACMHdgtvlQpPvE8ixPdasqTjprWeI6lF60uEjsd-xsSDBgu4FuGPujRkkN1w74ICJl_wKRLiW8Ef5UPTH5lWOj_DixUAZyUX-aIGFC2XaEtQvE3QosItO0crrfEq1pAuE25pyV2Zl-Sc73hmQMs96EDHlHBWgrryyAYEPK95_nuyersscSSJpoLkMlO0h3YV4x40STfoo1I95PUvj287z5G7teMuSJ7bfcRhaDNQmPvdqHRP-O2CD3T8aOkiX6XfozlpBw6PLVNDmfLODEysE5xt2X-6RPacAPP2MVs8Y-xS9TKWXDNuxM7fWA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff0e768cc.mp4?token=eOwA-TdS4sBMOlDgY1KY38hLAScZACMHdgtvlQpPvE8ixPdasqTjprWeI6lF60uEjsd-xsSDBgu4FuGPujRkkN1w74ICJl_wKRLiW8Ef5UPTH5lWOj_DixUAZyUX-aIGFC2XaEtQvE3QosItO0crrfEq1pAuE25pyV2Zl-Sc73hmQMs96EDHlHBWgrryyAYEPK95_nuyersscSSJpoLkMlO0h3YV4x40STfoo1I95PUvj287z5G7teMuSJ7bfcRhaDNQmPvdqHRP-O2CD3T8aOkiX6XfozlpBw6PLVNDmfLODEysE5xt2X-6RPacAPP2MVs8Y-xS9TKWXDNuxM7fWA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">علی عشق ابدی براتون رپ خونده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/83063" target="_blank">📅 17:03 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83062">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ساندی‌تایمز: دو تا آپارتمان پنت‌هاوس لوکس تو پلاک 3a Palace Green لندن (منطقه کنزینگتون) که برای مجتبی خامنه‌ای هستن به فروش گذاشته شدن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/83062" target="_blank">📅 16:52 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83061">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">با گوشیاتون تو شارژ کار نکنید که وضعیت بگاییه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/83061" target="_blank">📅 16:30 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83060">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=NgiE8A-xsmeWNOG68jiEyfzxTV5Dcfn6QD1Kluj0FXDKd7cqBvaaOc9_eWxZrQWtrP_wfp2fA2v7xkMizm5FKFYfzAiiemuW8_TlAEaiYgqpMgkFK0fzk2Id4CfROlycUDNpNQmywk0kgnKIUYELDxFF17mqcH3oJYZpEsroe3icOxic9IzZHlRGp-3X4eUaY8yhSViOK1ED9ms0kBFzb11TTG0dE5Y9PuvWEYFRFtu_cxwl7kSQNOa-tzjlA0_C5ZrrumB8Q0s9eShbkiZWzPSF7VIerT5rtp_-34RVY4nbKB4s8WzQ8wJhROtjI8f4sgYNcwQQ4dhDe168-SBQAQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b309c1c56.mp4?token=NgiE8A-xsmeWNOG68jiEyfzxTV5Dcfn6QD1Kluj0FXDKd7cqBvaaOc9_eWxZrQWtrP_wfp2fA2v7xkMizm5FKFYfzAiiemuW8_TlAEaiYgqpMgkFK0fzk2Id4CfROlycUDNpNQmywk0kgnKIUYELDxFF17mqcH3oJYZpEsroe3icOxic9IzZHlRGp-3X4eUaY8yhSViOK1ED9ms0kBFzb11TTG0dE5Y9PuvWEYFRFtu_cxwl7kSQNOa-tzjlA0_C5ZrrumB8Q0s9eShbkiZWzPSF7VIerT5rtp_-34RVY4nbKB4s8WzQ8wJhROtjI8f4sgYNcwQQ4dhDe168-SBQAQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایلان ماسک به قصد پاره کردن کون اوبر، تاکسی های خودران تسلا رو به بازار عرضه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/83060" target="_blank">📅 14:56 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83059">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DBPXaVqO3g0CbyNhb3cJtvGGR94054v20QUOwriCc7B0jpyuOck6MGBMDmDTCCmPwuugmAwP2nFf0tY_ANcsfiqSXBBq7tTQmcTW4O_B52ZUPhAKNbWkXXgP_G1TXT0jJ5wEXTVpp5Ag5RfYJFDtRCHqRUYfuYyCmcD7OvgQC_ACHx1seJBIgq5MzFrIq4gBVznt6R2XH8Bv_b4y3mSuPZo3fQXfGmrbhF_mpbe4quIrhSTYSZMksTPfJf5WZqYhsCuopI-7t4UJe_d3CCCNqii80vbykjuH25gBUu8tCsdd_2saLhxKzSa1i2FhdDyVSVgEl_G4n1_f6aRRYJ8DuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ادمینای خبرگزاری فارس واقعا سطح طنز بالایی دارن.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/83059" target="_blank">📅 13:33 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83058">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">دلار شد ۲۳۰
ایرانخودرو هم اعلام کرده میخواد کصشراشو گرون کنه
عالیه وضعیت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83058" target="_blank">📅 11:00 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83057">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BNeIkZiN9zJqNnpnGOXN1kQD8Bzkd7DudXGi0JgaDE4AUXS89lhcKwto4wDdZV7B4AV1x0TlsOgsAZgxnR7fKnrHPtIkWtmhH_EpU0QbWiM9vykK3V1EsrNKxNlwo8L76JUjs8AtD1ndxC3ZCxO5POpu0xx4M4b4z4zFyDZOlp75GCe1nc3FOrJ8zp25r068KhqADxyrohMDYnkXbPNZzdr9ZYLP6ACCvsuKBcxCYAvyQlzDoJ5J-XRa3JwMfkCLpauudlkGrJH9T1l14sj_FhNi_fy6mO-xu-WLz0xuS3bciid_TGu4WhISC-w5ZWCPwTvN9xhy4I0nQFrFTwJ6zA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گردن نگرفتن همیشه از صفات بارز کیم جونگ اون بوده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/83057" target="_blank">📅 10:51 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83055">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=tSTYQGzeUv3-3AIEMurqOZJ8Yyq6nlxSJEL1cmRAUrQkwdI7o-LkuNSFOJ49eowiWII6FWwARiPwfhYVUz2PefDiF3fDj--CCOW4PFhP20YykYD0o9aNwbSiUQCmI3wLHMTkn9B51i-edom-PzMSpg3uPiLlSXo1Lc6bwixJ1G40B_FX41p3sAKBj8dZ_bPFaJ0mGo2PBABhct2PZkHH6vU9OmFwY67kNedhQ-Nm_KABmz8NnhHl6fDDPgMdL8ftFor-LVDzx2OfSqS1JtCA-c3udpnBKe-LEqMbx6k2wpZO8cPSoY2-6QnrRw-x4h5Y7NwFQCCZ68HD8baFXScalQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dba858a3ad.mp4?token=tSTYQGzeUv3-3AIEMurqOZJ8Yyq6nlxSJEL1cmRAUrQkwdI7o-LkuNSFOJ49eowiWII6FWwARiPwfhYVUz2PefDiF3fDj--CCOW4PFhP20YykYD0o9aNwbSiUQCmI3wLHMTkn9B51i-edom-PzMSpg3uPiLlSXo1Lc6bwixJ1G40B_FX41p3sAKBj8dZ_bPFaJ0mGo2PBABhct2PZkHH6vU9OmFwY67kNedhQ-Nm_KABmz8NnhHl6fDDPgMdL8ftFor-LVDzx2OfSqS1JtCA-c3udpnBKe-LEqMbx6k2wpZO8cPSoY2-6QnrRw-x4h5Y7NwFQCCZ68HD8baFXScalQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بابک زنجانی یه ربات هوش مصنوعی ساخته بعد تو یه حالت مثلا ما خریم یکیو گذاشته با کنترل کنترلش میکنه، یعنی در اصل اصلا ربات نیست و اسباب بازیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/83055" target="_blank">📅 10:15 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83054">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">ویس فحاشی خداداد</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/funhiphop/83054" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">فحشای خداداد عزیزی به امید عالیشاه.
کصکش پا پرانتزی
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/funhiphop/83054" target="_blank">📅 00:58 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83053">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">قالیباف: بستن تنگه هرمز به ضرر ایران شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/83053" target="_blank">📅 00:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83052">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">اگه میخواید عمق فاجعه رو بفهمید باید بهتون بگم که قیمت دلار داره دو برابر قد کاگان میشه در حالی که پارسال همین موقع کاگان ازش بلند تر بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/83052" target="_blank">📅 23:40 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83050">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RrrFAIHfxfMtten9pUrZkY3yUKI4Ya0jnxi3qSfTgh2IrkdKTYFNwcWQ5pEFWHzmeMroloZKWEPVjY4knulkndE1AyCHW1En900lrp8Wl1toLzkTgIt2ACoOEfB78fAl_xaYsuhSLxVwtQTM1BGYDut4brVeKWLoaAPC4-hwReZTSu5pp3984Hffl1CNGIQByNtftR8E2U_I_qV-8tulUONP2FkzFpKDPv05p30Hbw2BLb0TOkovlKaOPEdkFVbtz3e8LC8yN1i4RjQWJ0qZOrFV_xKcMQ-QreSCwPEEnMj_Ai3qAj4w4PmQbkhEQUncAggNrsfAwlyLgU-qjr7y1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lnSXV0KDSN3UJrPUXlaaL5Yh6sH2llD9BGfCX2wNbN3MIiTebQcDkLBngalcb_DGkEiIDBTICupcKNZZUdf3wCEwK7vSwMUO5Hmueb6aZzoDsCAvJgHV5jDRbNb3G8p6oHfNVl1ZvyBfqtPFZf8as1OORW_RG3PN9SWPEMse_tWJO5VvnzsuoeDrB0EI5lBpCnI36BAneJW6KL8MyBWfKsrseR0jCkFi3MY8RSNEL4EEM-xb_MgVWTkmEPoEJci-zKMySyCRxTVs9czWjCl2VbKe46mi_VH93V6b3tIN-eME-y8WTGcjeqqbGHxl6Rucc6YKXmdmxO9SjAf1RcnCGA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">حسین تی‌ام و سجاد شاهی دقیقا تو کدوم زمینه یکن که دارن سر اون یک بودنه باهم دعوا میکنن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/funhiphop/83050" target="_blank">📅 23:19 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83049">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">درگیری بین نیرو های انصارلله و نیرو های دولت یمن رخ داده از اون طرفم شبه نظامیای تحت حمایت امارات ریختن دارن حوثی هارو قیچی میکنن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/83049" target="_blank">📅 23:11 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-83047">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">رم عجب تیم سکسی ایه</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/83047" target="_blank">📅 22:56 · 14 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
