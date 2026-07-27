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
<img src="https://cdn4.telesco.pe/file/cQ79wbpHrLoLNW_V08LYYBqZCW7DauVVwShr6iOeZvfqQdj8SSg-QuMkso11oqHTqQ3kA_-RV7rQwWNWbd_IHFnkC2rzvJC5f8KRCUf0ft9FSZ31PPiYFuhXweAr9el7ZlYmsJylD68F1Dl5R0cRVmosC6OFYK5hOxDaagLqNpKLO9rxMsZuq8DPo_xr7XYAxWPVsxPuJ7OwgwsZstWrHJK6vlTukEQzy2amHc6oDbSQS9GRmOTgu4F_oLGQUQawHmhKYo-eiA7WFop5JXz3r1yk_kYn83BgNruI1Eu6Yc0aQsGDmR_pLnuvFR-SvnmcAa6e2pHwqNVtgz6_ndJnBg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 958K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directمالک کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-05 04:37:42</div>
<hr>

<div class="tg-post" id="msg-137805">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dj1GHz-KOUkGw-1P01qEmAntaRj-8dqa6MCINZphBl3YL9I4X0TYmUs0ylVr-_FZokCm7bqOKl0jsBfcAWGR8az3F4jxj3b7VTkxGAu5cpd6r-fVLRqTiL3Xh1SsQojq5U8PnJCwrcNMVunb-Xs6_OryiSJkWLt-HgKVmQ6L-l8z8m1SruB6mCYWsi_1q2iGm_yVqUwWZOYg57xRiZvMoZnC4_HfFULjQp5QX6nWSpD3lY9M9zAAvqgqoAZKbts62ZPp5jnO9a0YvxMGdG_YImLfBu05MLKo8k9-zVBS9ry7SRPQUNNc-2GdzFL7rtjq55_PVSwT9Azsia8Sfd3tMQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎓
دریافت مدرک رسمی «دیپلم تا دکتری» فقط در ۱۰ روز!
✅
قانونی، قابل استعلام، کاملاً غیرحضوری
✅
مناسب مهاجرت، استخدام، ارتقاء شغلی و ادامه تحصیل
✅
ترجمه رسمی و تأیید توسط تمامی نهادها
☎️
مشاوره تخصصی و رایگان
:
https://t.me/irantahsilat_chat
📺
عضویت در کانال
:
https://t.me/+1I9Ex4YFtcZkOTY0
https://t.me/+1I9Ex4YFtcZkOTY0</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/alonews/137805" target="_blank">📅 01:46 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137804">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sklPqnC3DI_EiV77R-T5v5eCUiHH7EbNZ07D8DeT5DFKnNNulishe2CnfP6wIPDVyh6xhu7kdUTzoXWpMJRrTpgXVN-M1PaGuuSMFQF0pU_IX-eAUDAMjyIfJVTH2_dDIpwhfAS5g1z-9RrNXPqbjSQUCfT8znra_e45DO_ouRYA3XURcOftLeuyFEXMeX6KI-7WS7IPCvkYlk8b-ZYLaCx5uVDjKsZCuucqcjZeKPTx-Sli60cXccB2mRMxNNkOibquVHHLdWCbuWYjO8AXdcCU7q5lntdmSiFGYO5rLB1VOnfF-Y2P4qdi87Yp6Gw1jLGE37HfcweTiZ94WPLGHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امروز ۵ ام مرداد، سالروز درگذشت محمدرضا شاه پهلوی هست.
حستون رو با ری اکشن نشون بدید
✅
@AloNews</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/137804" target="_blank">📅 01:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137803">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X_e44PjddYWHkPSsNrWYCXBhdiQqRmtDEkxGE26kVezKnVZbmMcsY_cHhvj7syXidYo6Nu2SqL4MIP7ycVU370OxszHqsTjYPb9i6OYr8Z1TrYuy3SlF242FnWzH2dyG2P7_48ad1XhuT-hozWMhiVRn7yWSfDY9sofTfN8o0jlGgdvyt-xr_fTkf7vWUyx1KRDVtL6yJiO7b5fN5J29_2bXlbM_byMLQ8myofQH_6MRXiB77aXrgYA6RVImBpEBlcxc_-yRM7w16Pis4N_-QEIVk1wtPkaGT0YRLuUloorsu8fejy8OrMy7dxgYJnhCzT69Fx6Rs88LM2nIAjaN0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یک منبع نظامی خارجی: به نظر می‌رسد نیروی هوافضای سپاه پاسداران در حال آماده شدن برای تلافی حمله سرویس امنیتی اوکراین (SBU) به یک کشتی باری ایرانی در دریای خزر با استفاده از پهپادهای تهاجمی یک طرفه است که منجر به کشته شدن یک ملوان غیرنظامی در آن شد.
🔴
کی یف تقریباً 1850 کیلومتر از تبریز فاصله دارد و این شهر را در برد موشک‌های بالستیک سجیل-2 و خرمشهر-3/4 نیروی هوافضای سپاه قرار می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.1K · <a href="https://t.me/alonews/137803" target="_blank">📅 01:21 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137802">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ufBo3to-97oAbl4NRk6IKfJeTvC6xZ7ZMqOuR6HYDSGInxDfKbVpN_etntPXtBc2L-v9LQ6u9iADsBDbPiDFyuhyp9W69gbIKLJao7hzwSjiq4e9Asp7J08UHZYr_qPIO_jJpGQU8EcijvNoB4QQkggcT_RgChbSss6nN-igJWtO3czewHsVpaRlrZPEEvs17u9bFGGP331QnX2YqhvK77Vw10aWxBu-DQDlqvsUeW425P0yiDXmme49Ro3G73MpTqCu_t1H_WydtMKmitexDGYl1DOcn5w9AI1dKASnmL5v1EevH62rcbPo7BaEDHz9UQjFyAT8WObs73ERkiLquw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
در ادامه خودشو تبدیل به دکتر کرد و نوشت:
این ستون مهره رو میبینی؟ این دقیقا چیزیه که می خوام به جمهوری خواهان برگردونمش.
✅
@AloNews</div>
<div class="tg-footer">👁️ 38.9K · <a href="https://t.me/alonews/137802" target="_blank">📅 01:13 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137801">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D-C6HVHJcJ5hQVwQ7lp7PmI24ORdiL3UuJuXsYbiUE8Zboy9f8sSFyPfp_jDT7MWFQp-uSMqaCo2mV1KKsma0F5zbAs93AKvazGPxJAybLPEqeNS4lK80VeqvJi2tD2l9zrkZpFiiRBDW8I4H9vFOPoPKwb5rAH0wv-u5zLWYnHNUJBCwdqoGC5x9xnrHyZwrGYl-W7nOvKPouZY5UOYOhkIfgAXE2WIDBoA4MC2sX-Gs6jA6E7muOVEyN7oYYHTJaqjTwuDpDb_TNdTb4Wv4dKSX55GLMICok-1kqQjVfFjwDb1xG8VvxS57VYEGKlQNffAxWnuDL03QwhwpxJ1CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ: این نفتکش حالا متعلق به ماست
✅
@AloNews</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/137801" target="_blank">📅 01:03 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137800">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">گویا آرام بعد طلاق از سپهر وارد اونلی فنز
😐
شده و داره تصاویر... رو به طرفداراش میفروشه
😐
چندتاش رو خریدیم و گذاشتیم
◀️
مشاهده فوری</div>
<div class="tg-footer">👁️ 43.3K · <a href="https://t.me/alonews/137800" target="_blank">📅 01:00 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137799">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DcS6HCvrCD2k1gXwN1SvEHGzEgR3aFq9kUYng6qXngcHjCVmLnz5atGytez5E4svjpknuzSjvP23MtMVggsju7xBixj7YjjnNAkvDjUupkBlT08WzzZSWOOst1Sfqhh-VRNqN4ucYswGEE-33Y1VKB9YATYHI2wYT85xZrxl61BAuBaOUQMwlUsFIxkwAdiNPFqOpE46AvWbCGOaZ_QLIe01xd-wXY_0L5LF0WCUMX6M2dlNkhaUgdQkUVG-xoqs9diMoMHthfHWI-pPrGQVtGaVmoF4V9R7a4l2OxZIOMOfRMWaIeurHSypReh28iNTyna3TJHFT80-6-gxNrs-YA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هفت فروند هواپیمای سوخت‌رسان و یک فروند هواپیمای هشدار زودهنگام E-3B آمریکا در نزدیکی سواحل ایران در حال پرواز هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.1K · <a href="https://t.me/alonews/137799" target="_blank">📅 00:59 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137798">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lLaanB3gKh0-cjGDedoQm4lA_02epWIyvqI9O3AJtjpyU1t7dlnDhVmJbOvPGdkazhkDxj0XRQaR4hg_70YE5JxO-lQASm4Y6ADNPj-VoIOp9RvdcORRyV1H_mX1qQmln5XJscel8hdfJhylkRuo_tYlr9LQxTUFVnneUij0NdEuFVl0uxQT3yh40oPERKn2wMO3mtZnFg8n7qsV5DsKS24wO59utI6zgv4yW-BWp2N8Mn4bLsVd_fUpxfLOAPGw4_cIoro51krGegZhCJAkk6z6XM_0IvaGqkHV-k-CITv4X1lormrTZkTZd9OP1hjNg0nW5I3srx36uOJk6NPANw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید دونالد ترامپ:
✅
@AloNews</div>
<div class="tg-footer">👁️ 45K · <a href="https://t.me/alonews/137798" target="_blank">📅 00:54 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137797">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ca4847374.mp4?token=uluX-FnO8ntJD4EYXaEHH9cb8dhektlnuuXcvwIaxauVJy_gdGVUYxJKxxebdlbHnuWzxNoG1mSagi_7nkx69R_7yZWTCcPBPwSRihQYNmw9DwbuvbKL69wGxvIZzQIPnIB_hYiOB96B3ADodWu2uf0IB_jODzwcbaItLpxO-dK7hApEaS5Y98OBJD7E0Z9r80fKwYKdkDIWlb4HBe8m7gPsDhXtJK4P7QFlJqC69L0nJR9MssGT2-HPdiyxaTWgVUWbGCub6q4jq47onp5L0JGdNy8FdvhupD-0ZzbpwkqpLpohDytEhv97W-alKiLSHvnDypvyhTNtmWzCLz-doYi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حرف‌های حق شهریاری به جوانک مینی کمونیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/137797" target="_blank">📅 00:37 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137796">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
فاکس نیوز:حمله گسترده به ایران هر لحظه ممکن است رخ دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/137796" target="_blank">📅 00:34 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137795">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QKBVVKWGsNwe9DDxkHIY95IWc7IuTg1n3atKJQVCr95aa3LBjG_hPIWbEjiIBr4m-BhmEieUDWkJR0dB_cMnaAkUnpVRhsn891-1t6ByH2nZYPbzFo6DvYtnneFW5cwi-TNxgVSQ8rjfAdZ_sfPoQYdHo0dCVq5T6l0vCcRUhjpSKa5xFiYHjzz2aBBB8LA3ygwdIkCTVYVuwuQz61DjUM6zVFpJ_8XvSIKoAhZEhku0frjAK6JgoO2MxC2oe5yrPKo0NUYAqRftW1_wCPYIGra3zrRJSpwtUMBdNYjYTi-c6i_28nipcD1_oKuJHbhfpMhwyq0aIuG8DoeRK40k4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🆕
کانال میلیتاری خبریه
@Breakingpersian
@Breakingpersian
📌
رو داشته باشید  لایو 24 ساعت اخبار فوری جنگ</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/alonews/137795" target="_blank">📅 00:31 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137794">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
وال استریت ژورنال: نیروهای نظامی آمریکا، حملاتی را تدارک دیده بودند که می‌توانست تا دو هفته به طول بینجامد، اما این عملیات به تعویق افتاد.
🔴
فرماندهان نظامی در مورد اینکه آیا کاهش موجودی موشک‌های پاتریوت خطر قابل توجهی ایجاد می‌کند یا نه، اختلاف نظر دارند، در حالی که ترامپ اصرار دارد که مهمات آمریکا همچنان بیش از اندازه کافی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/137794" target="_blank">📅 00:19 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137793">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
انصارالله یمن: تنگه باب المندب به طور کامل به روی عربستان بسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.4K · <a href="https://t.me/alonews/137793" target="_blank">📅 00:15 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137792">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cCkNigcevKyD4AejtWCUmUjKNv8qaq9V4p6YRp3SBPQSXX8QkyL4jDmj-EdTlPKWeREYXTWmzRNrumTMqwdzfgCya3kQ2oeBwhPscEtOheCtXknOXCXEsmG2A5xs0aGmT3kXX428oh8cG6dHES-0T_kRJbpj3WqYR5qvWb53sZ_kSNeWkh72fC8MLOKt9zgV-2GXnLEfRqxRUvVgEepE860Ong0k6gSmMX0kzMQUhVHf_AhhHxwFS7vJNzipkdZUZ8Pe9P_avWXlDn5E-QUJcicoROqyMBzfOfcEPlFoIpUb7cPonNG-3JVp60A0k9JxR4gxROjzuy-G1EELZrnSfw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social
✅
@AloNews</div>
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/137792" target="_blank">📅 00:12 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137791">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
وارد تاریخ رند ۱۴۰۵/۰۵/۰۵ شدیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/137791" target="_blank">📅 00:09 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137790">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
کانال ۱۵ اسرائیل به نقل از چند مقام: این ادعا که کمبود موشک‌های رهگیر مانع اجرای حمله [علیه ایران] شده، بیشتر به یک بهانه برای خودداری از انجام حمله در شرایط فعلی شباهت دارد
🔴
در اسرائیل این باور وجود دارد که ترامپ فعلاً از ایده اجرای یک حمله گسترده علیه ایران یک گام به عقب برداشته
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/137790" target="_blank">📅 00:07 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137789">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93a7d60290.mp4?token=ZICe6aFrL1eWmtUjI1cAngRohG-QWu0Nr5JOfTBogwvW2FYqNg8gSbOaA2Bb6KwCTxSqhMEtm0GJAvfcsCHpIH98652DGsrg4YRw1x7tWZVGUuzBnwfuY950CxLGe-6N-RgyxW8YZv7UBn7jbrdKkhZzvUmxX5FnAg50bCH4p-1971soAi4afDTE3a4MpUtuMrPm2H52zjqOnxi3P3Ao6t2_gEzNc_62FG6i-L2hkibDOaOxKS-wfxB5jqjo_5I0ES_hLD-gTHUa-f7-tRVPHmvwNeBVEIQFUWDI0HSqlN7c-6BqsqorDZb8ZW6ldiKLqFihcBtmIQHEuB8mslA9zA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93a7d60290.mp4?token=ZICe6aFrL1eWmtUjI1cAngRohG-QWu0Nr5JOfTBogwvW2FYqNg8gSbOaA2Bb6KwCTxSqhMEtm0GJAvfcsCHpIH98652DGsrg4YRw1x7tWZVGUuzBnwfuY950CxLGe-6N-RgyxW8YZv7UBn7jbrdKkhZzvUmxX5FnAg50bCH4p-1971soAi4afDTE3a4MpUtuMrPm2H52zjqOnxi3P3Ao6t2_gEzNc_62FG6i-L2hkibDOaOxKS-wfxB5jqjo_5I0ES_hLD-gTHUa-f7-tRVPHmvwNeBVEIQFUWDI0HSqlN7c-6BqsqorDZb8ZW6ldiKLqFihcBtmIQHEuB8mslA9zA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
احمد الشعار، رئیس‌جمهور سوریه:
نباید همیشه مجبور باشیم بین اهداف اسرائیل و اهداف ایران در منطقه، یکی را انتخاب کنیم.
🔴
خود این منطقه باید سیاست مستقل و هویت مستقلی داشته باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137789" target="_blank">📅 00:02 · 05 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137788">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
وال استریت ژورنال : ارتش آمریکا یک طرح نظامی تمام عیار برای مدت 2 هفته جنگ همه جانبه با ایران آماده کرده است که هر لحظه با دستور دستور ترامپ آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/137788" target="_blank">📅 23:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137787">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
سی‌ان‌ان: لیندسی گراهام در فیلمی تازه منتشر شده، تلاش چندین ساله برای جنگ علیه ایران را «بهترین کاری که تا به حال انجام داده‌ام» خواند
🔴
او می‌گوید «ترامپ و نتانیاهو مانند روزولت و چرچیل هستند
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/137787" target="_blank">📅 23:53 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137786">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
پوتین : شرق اوکراین برای ماست و غرب آن برای لهستان، مجارستان و رومانی است و به زودی به آن ها برگردانده خواهد شد!
✅
@AloNews</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/137786" target="_blank">📅 23:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137785">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UGFkJUqdjzPGYHHlqqX63JTY_cQstDmICrnli44oUXjrYi2_vEXAMDBiJUbwWE67EIGxvcSZZcoSesXLUuzN8ZF61vUs5twaw-OV9Hky2_MW_5J6S25QP4fmwIzZch6kMlIFNp5aiAfAWmo1ZgM8DCNjUppiP3CmEs7a_HC5WDPIwGZskrbgexgnW2lsQge8d3znZAmG_b38Obrqel5gnV49VranEdd5PV60wZN9Ji89J6dpAN7aRe7TomhjHbDI20vo93cvrX7PmdZQCQYx9kL4Ob7IfKp2t-tNaOaRKY8g9lf3vJNtdQ6CsxAsb5qj6-Lg7VoUBn48Wt9SHWWZxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ اینبار رفت سراغ بایدن
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/137785" target="_blank">📅 23:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137784">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c34aa341c.mp4?token=jESQZOVMTzx0lV-AAh-ThjemzrCZH7PKLYEPw0NZkhVsN_wORIuTuwX60xux0JrToroFZdU5le11oTZsWf3dyibPG78Aig4I-ZndEoX_gwxr5t1z6Tljh1elLPgKni5WXGbWLU0c_tnHpMRFmQtJhCsDWZ048MWh30Vi0sEGqqINNVngQlOUuAbaRgj6_CkCoyqn6x6lBV15VomFFz-Vs_4xqKl5baaNkPhbdxJyMD8xJaie067-9hoYhXWJ4gUH0RsTdOVUENybe1MFlIsRDWzSpD6Em0y-_ovPwAn3jbNEZs6MUrZB-3xcY631xknI_oLzR2lawlRhWC6rS9Pb1A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c34aa341c.mp4?token=jESQZOVMTzx0lV-AAh-ThjemzrCZH7PKLYEPw0NZkhVsN_wORIuTuwX60xux0JrToroFZdU5le11oTZsWf3dyibPG78Aig4I-ZndEoX_gwxr5t1z6Tljh1elLPgKni5WXGbWLU0c_tnHpMRFmQtJhCsDWZ048MWh30Vi0sEGqqINNVngQlOUuAbaRgj6_CkCoyqn6x6lBV15VomFFz-Vs_4xqKl5baaNkPhbdxJyMD8xJaie067-9hoYhXWJ4gUH0RsTdOVUENybe1MFlIsRDWzSpD6Em0y-_ovPwAn3jbNEZs6MUrZB-3xcY631xknI_oLzR2lawlRhWC6rS9Pb1A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مداح اهل بیت، عباس زینل پور خطاب به ترامپ؛ اینو تو گوشت فرو کن،
خارکسه
جزیره مال ایرانه
😈
در تنهایی گوش بدید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 56.1K · <a href="https://t.me/alonews/137784" target="_blank">📅 23:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137783">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Vc-IdOrbMaCevcOMgnwsAkBNEolO8z0Z2grMe1kA4mx270MET5JPtmnwVNH6XgAuyhJzVhvJNGMnGbHc1NyIMjv-8s_U5KuV9w3bnEktN-ybOfuWDsuAu5hBfp7QJLBmeTsUr5u2xNEmbLMgdx3cZ_DByZgqC-SUznKVmHcTX-XXOfa7Xb2aZwyW5YvVHXP-Sa6fqEOEkJwUXCQPHBJ6RlrS_wXyhwBP-gvbRIe3jgcyj530exHSOwbgQJKO2rwUrdDFSyXLcEEl8Dbip455FORuQJ9l0KSzRPmG7QEKBP2LqEu7zZSpR8p9v3gjaXas6kuYnqTitScnmy3YlYFkcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای E-3G Sentry متعلق به نیروی هوایی ایالات متحده، که یک هواپیمای پیشرفته شناسایی و کنترل هوایی است، در حال پرواز از پایگاه هوایی پرنس سلطان در عربستان سعودی
✅
@AloNews</div>
<div class="tg-footer">👁️ 57K · <a href="https://t.me/alonews/137783" target="_blank">📅 23:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137782">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
سفیر آمریکا در سازمان ملل: فرصت مذاکرات با ایران نامحدود نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/137782" target="_blank">📅 23:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137781">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال استریت ژورنال: دونالد ترامپ ادعا کرد:آمریکا مهمات بسیار بیشتری از آنچه نیاز است در اختیار دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/137781" target="_blank">📅 23:32 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137780">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kxgmjwaeVSdznxWyYj26eQuawqfUzBQmNlX2AqESOsIR21_x7IS9AS74AlcjCPmJBsKajibLOUGXnurm8qiBm8d4cjD91KyMe1u__HMrasxCBO4TPhVFmcxdC3XrXu8ZTDP2ATwn6BkI-HHSCHfYj0Qf6RMpffUDM8Orxhq5qHI-hsztaw748QjIEuts3k3wpan4zOpFIRlVYz7p0fbTASYthDnqFFKY5bk_elj4NHbvHFTGaxQVmScUiCwsKk4TevxuZ6pUT2N0qtW8z7SMh6XGkrIyFWHUQweVFxRFV7tvutJg_lppoXD21Il74gzreAtpGxjtiI0GjMFC6pLMmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ از طریق شبکه اجتماعی Truth Social: دیگر هیچ موتور [حرکتی] وجود نخواهد داشت.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/137780" target="_blank">📅 23:25 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137779">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OiAz-Q1ehBhCW-gbs7gGqITyDftUC87ItQjh8WpK9Djm95WwxJCBbPbGxS1hqw9siS-xBPg2GjqwqvhDYsgT1zY5TxCqYQctJUwyQCJ-qf9Xg_JRz4sNnIhdsv28a7xgrCzDvImxQFj50mhbfCX38ErDRg-JG0jlg4eKUbZC-oGBlMOF8d1W46EQnJYYZW3d0IqdZGAhu_nfE7CgYkGaBpJ2W9Kn9qbys5kAhGoHeHQrMT3Cqmt5YHZyIOc1K48EqS2mxCJywyl7JQqV2KykgGXVMeCSSeWhYPl7VcuhvZu0o2Y8PONEOu81nI8St4I1eBZDqSLi54Hq9PIbyDnHjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ،  از طریق شبکه اجتماعی Truth Social: به دشمنان کابوس تعبیر کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.9K · <a href="https://t.me/alonews/137779" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137778">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4F-eP6klZh-PGjMJ-8UfulGuj97ZRZcuXdjOUXT4KmYAbdNCzKeg3XlrYp7y6Ms-m8uicC_uJcmGS0BI8eYci4FXX9N0-OtFl9IO0fgu37Drfg23JGVl7-kAGghBrHvyCsQiqSo2HmBZJ3Kh_YLJLGZ-Nh6XKeV4G5n4JsHWmLDWANvJKwf-LSCiqMBKBWqr0RITkDPGAhW7oS8_IEg94AvyduKZA4VV1YBA0felLdmyb99FSi1ViqeyyNTWsUf9iOtG4VsQ9tPE1v7SS4jbHzwu5YjEYgtrsHHNaFS5lugFpTIq-g-DZ0ApstlRLrM0KTFtIC0jIkI4Izp12S5ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ : تصویری از پوستر یک فیلم را در شبکه‌های اجتماعی منتشر کرد که با استفاده از هوش مصنوعی ساخته شده بود. این پوستر، او را به عنوان بازیگر اصلی یک فیلم با نام "فرمانده کیهانی" نشان می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 56K · <a href="https://t.me/alonews/137778" target="_blank">📅 23:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137775">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Rz2FV9myR2j_Ly8IEfw-eMAGpuajhi90P6Rwk0UaewEiHIEy5DIrwVt5yBkT2UZBVgVMMIwDAC8rrtY_bRdkVHwPxL_rOhWTcWfXZTz5ReEbXLp75uv6OjW5kPqXHByVUNuKQK1DO12Jhh6Gq6MwHDmTVwJgnw26sm315e-T2io_rA9MRFDD1dv8ylF64AXesWSuSDcODNpim1ISDxgtg-_M1WiMeHYgGNMtfW40frpXikcRmO-tzQORF8JfXXKJXWLNN4Bjc4OhPql8Zb5xUyHRb4qCnfDJ5F0NCqeCeoTrotN1oFvknyQpF1nF_OvjDwO7bW-pGhuvdc6ovz8c7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ePUUMakvRwt3aZVWOzJI9YVtjaP2UJGIIcjgYnxH63shQd1crHioPvzskU17yfskvvKnbCssvM6nzAw-ujVh8w7goi4Y5S1KyLOI5XRcwH_YstCsiPqVvg3Bot0Kjjxs76Oj0zZNNFpNjgoRY0exstE1Dr73ZIRzsppRYdaRGjtlVBgMxPaxWLp4n7yJxgZxwfEBvKWicR4H8oQ31eNLHZme3BNO3f5WSUOhWCATeOv6jxeBavWmkspxs_pw_4fJw_1vNTgXwbQNiXAYmW4_dFB3U_L1Uh2JYlkWpPL_xEQP9f7EmjupFL4bDx6yBhcqjERhg6HDiRH7aPgJB7elDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cL5MxPzHD7RVjDwHT34fTtnWckBSOrWLlYx4x1GucG4dRa5o_6Mjk4-IAqajAeFGi-2KFI_D2gIWas1RT4BPTtsJy4TV-a-L7u71NkaDYBNTv7DXvztVBg_NJZn0SpngcsQzN4rwWWpnTJG4l0ACqVQB45mNyJV6Ld5DJclApmUbMUvPaETTikNfNsqieX8Q5H7MedCzcsX7lGKiYXERCcK-djZ6oAUuBZXSorFlwQY-u32trniwrxci7pEN9qL375JVuSDFP4ES4xnI2MSkS1btkEiyOMVYTm2CQYioh_h2FnRtf8nBLoFRo4j6Xu_9CbKZMwvEMi-Xx12cU8qk4Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
ترامپ تصاویری که توسط هوش مصنوعی تولید شده‌اند را در شبکه‌های اجتماعی منتشر کرد. در این تصاویر، او در حال تصرف یک تانکر نفتی ایرانی دیده می‌شود و در زیر این تصاویر نوشته شده است: «حالا این تانکر نفتی متعلق به ماست.»
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/137775" target="_blank">📅 23:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137774">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aEnDAelcAydzq8bGpVBnzTkGY3gYwrIDMK8f5A14UOQxwgU79CrvXVwwcqRo6SnweG4-ktryLz6J1yGa6mqv3RwLVhD8JmfOi6zJiVqV57KmSn4h0quHZN0nZ6abadmL2lAd-kPSb8CPjXc1rzyzr62rVrVwVEfFMFVcmBStRYiEKbAjwHlfK4QpE0Eokuct6gngwIc2MLmJq9kbJ0Q0NenBWSF8JmYEABnmcNoFSXOYUM7OiBnU7ynD94-vrCw7Fhu_wda8W0se2Hcpxvi0rka6s2lojIliK_DbbxtBgfrxesStXEyAG1eJlkIgIwMymgmLvn7F4BqTw0PpIon4Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری/ترامپ: حمله به جزیره خارک!
🔴
تصویر شامل یک حمله هوایی و آتش‌گرفتن تاسیسات نفتی جزیره خارک است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/137774" target="_blank">📅 23:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137773">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WfIx1uyzIOm96ZqLbGSLUlu1mCMeDjU6Q6zGTwfR9PM9X1jkYYdKrsXtK6wz3YjvWstQB86ps7GIlYOdfHCVdQ_qdvuXQ4fq84puT0vMR8tl-wpjzNWKqdEsy0YcqutKoFC1dRn9eFMwUCUdb3k7YQDjkcZnyf3yJgrouL6VxRinl9B_C1tBihXRg33pVt2OqRk6AYAjmxUCAnsmTpI4KBwmx6T3qyITjMdcN4R59TCKx-dgA_NHIeKUSiH-2RQr-snVL-BItXB-rMCwwv27Nk0FTVzjibaQgwOBzIjQ3AgktDgaN3CxDtLM24pMpgItrFnxPMEH30MKqtY68bXNaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بقائی: آمریکایی‌ها در حال تبادل پیام هستند اما اولویت ما دفاع از ایران است
✅
@AloNews</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/137773" target="_blank">📅 23:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137772">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
علی نصیری، رئیس سارمان پیشگیری و مدیریت بحران شهر تهران: بلندگو ها و
تجهیزات نصب شده در شهر تهران، برای پخش اذان است نه برای آژیر هشدار جنگ
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/137772" target="_blank">📅 23:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137771">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
العربیه: تماس‌های چین شامل بررسی اقدامات متقابل برای اعتمادسازی میان آمریکا و ایران است.
🔴
پکن در تلاش است زمینه را برای مذاکرات میان آمریکا و ایران درباره امنیت منطقه‌ای فراهم کند.
🔴
هدف تماس‌های چین، مشارکت دادن کشورهای حاشیه خلیج فارس و دیگر قدرت‌های منطقه‌ای در حمایت از ثبات بلندمدت در منطقه است
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/137771" target="_blank">📅 23:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137770">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
الحدث به نقل از وزارت خارجه آمریکا:
تبادل پیام‌ها بین واشنگتن و تهران همچنان ادامه دارد.
🔴
العربیه به نقل از یک منبع بلندپایه:
رایزنی‌های چین در هماهنگی با پاکستان برای کاهش تنش میان آمریکا و ایران انجام شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.8K · <a href="https://t.me/alonews/137770" target="_blank">📅 23:01 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137769">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
معاون شرکت مخابرات: سرقت کابل‌های مخابرات به بحران تبدیل شده.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/137769" target="_blank">📅 22:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137768">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">فردا 5/5/5، هر تصمیمی دارین فردا اقدام کنید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/137768" target="_blank">📅 22:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137767">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا :
تبادل پیام‌ها بین واشنگتن و تهران همچنان ادامه داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.1K · <a href="https://t.me/alonews/137767" target="_blank">📅 22:36 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137766">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
نماینده‌های مجلس امروز طرحی رو تصویب کردن که بر اساس اون، تمام نیروهای سنتکام و تمام شهروندان ساکن اسرائیل، چه سلاح حمل کنن چه نکنن، نظامی محسوب میشن.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/137766" target="_blank">📅 22:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137765">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DdYUWOLrx8BIx1xs88-ucMwOF8pulGGp86V9eMrD0iCxzItVDnnYxyvSwrIqrrwTEVBuOb2TrrH7D3qriQnyJwqpowRxGtiZu4zGuFwvjc8vGjY3-Db7zUVSLbnLlaQL-tzKc-J8FQAljuQEjD3VZaMTZWop2EjxE2jaRKGMztUZPyZCfWE8KCh0rJB3wm-MOBHWwGcOzMsayQBdrZr9Per90TiemKPwOK7JnbaY14sZHeQV6oBUP7N4Q2pTNjQ4Db2KQCcezM-hSY_OUnDSKlTxmbf7f2jSsaDItXMIlFb3ouHSrqiZd5-AFOz3I5HqVnxnFbMQumheRS3S2ml79w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ثابتی:
مردم فقط دنبال انتقامن نه چیز دیگه
🔴
پ.ن: با این نخبه موافقید؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.9K · <a href="https://t.me/alonews/137765" target="_blank">📅 22:23 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137764">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XmkZQL0coNMw4fkMkkzix6TPKsgmmSFbgmRuPY5v6ftUEFXhfglA2NXDjjetk3d9BQH-TaRZr5ae0ZRiLyeoYvF6F1S4OfnPJQPGokfjN04M3rtdvfbLJmxxUJnZxHtG3RXWRsgmfIEw5LKUAZ6ObRhVFeRExIRkrxnkcu8ZiKEp00zU-8jc_2RCr9LSjdMbL5SpbS6q-F2TmgQjXRQV0UsnPM5n-0aoS9vu5HVhcmzT6jLfjtvtSdMMBku8GG4qDUTQtzDZJb4H_xR1Ercjd3JD4gQOnCcG-A9aetMTffjwwq26OIFYGPk5rxHQfwcN4JZyvFLg1Hga8x_v-Lz26g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون فعالیت گسترده تیم مذاکره کننده آمریکایی در منطقه
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137764" target="_blank">📅 22:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137763">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
المیادین: نیروهای مسلح یمن طی ۴۸ ساعت گذشته ۳ نفتکش سعودی را هدف قرار داده‌اند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/137763" target="_blank">📅 22:16 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137762">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ViLOBKTwE4-tJaLXtbbdIYRAtP_E4KFaZNt_L-rKVONUlOT-_empjdrKp6Q1hIvQ2PdASftoiWLP8IMS5g3HHnnHK1F_UytGo8WIFBlaJ5H4kVvOwIN3tD63uWvq6Zt4uJZzxJHCviEQehtultw5qsjkvZF6v8c_sqrYEQm3b8e3pWEy5e2GObhIKE5TWZZqRuwan_sAs_MFSd1yJwUxt_9cf7AZ5GF8FD0ucKBe24YdWscHLnabbvit4-Kzm8_URowae5Of9fTK5L3nEsrCxABJ90-LomrinQGrLGbJ5YX4Q6I2gNgk_cfzl_1XkboJpmaVKRsCIljArfjmV5BWtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.6K · <a href="https://t.me/alonews/137762" target="_blank">📅 22:10 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137761">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=PFE9rHl_K6JePeHyDqIK5Tj5uFm8VNDETYiA6-1aMpjOR5BRpltqRhlHetG-zftvTrJA67JgO-I8ub2uH9N9k_iBbaKw3Ez_9BLf3Dak-GmCQPAQHIsOQuNGrJXhKH1epypouIc17OjcjI7nqD_Mb6W810ueCHNrV_Upvfcj1o84_WCJ2pGIHI2mN5vENFJCGTG-a4L8X0l9_wtO4Jy5BZXUPLqMAOGg_iXyz7mgBoW6wczDuyond3-ij7U5x_qEVUMc3UP96JvmPAWn6h5iQcYyOiV93nOXd7TQy242FJoiqZI7LfReEq_bSX9P11kec9F7K7Tk1qqAel35YIdHTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c2b00254.mp4?token=PFE9rHl_K6JePeHyDqIK5Tj5uFm8VNDETYiA6-1aMpjOR5BRpltqRhlHetG-zftvTrJA67JgO-I8ub2uH9N9k_iBbaKw3Ez_9BLf3Dak-GmCQPAQHIsOQuNGrJXhKH1epypouIc17OjcjI7nqD_Mb6W810ueCHNrV_Upvfcj1o84_WCJ2pGIHI2mN5vENFJCGTG-a4L8X0l9_wtO4Jy5BZXUPLqMAOGg_iXyz7mgBoW6wczDuyond3-ij7U5x_qEVUMc3UP96JvmPAWn6h5iQcYyOiV93nOXd7TQy242FJoiqZI7LfReEq_bSX9P11kec9F7K7Tk1qqAel35YIdHTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
توی موزه ملی کره‌شمالی دو تا پنکه گذاشتن رو به روی عکس رهبرکره شمالی که یه وقت تو عکس گرمش نشه
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.6K · <a href="https://t.me/alonews/137761" target="_blank">📅 22:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137760">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭕️
چند نکته بسیار مهم برای حفظ امنیت شما در تلگرام
🔴
برای تنظیم بیشتر موارد، وارد مسیر Settings > Privacy and Security شوید.  ۱. مخفی‌کردن شماره تلفن وارد Phone Number شوید و این گزینه‌ها را تنظیم کنید: Who can see my phone number: روی Nobody Who can find me…</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/137760" target="_blank">📅 22:05 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137759">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RTA68JVP53UT48SJtEeaEqdaX5SeA3xIh_OHT_Xp1j1UlehmtHFQbNQ7X81Q2MsFHE4G-ykg3_JnxHqLTp2E0WCmNbDEyif2F0F1eHXD9sCUlPsVSg4SeMP4z9KU3Q7BSxJjSVv-IgLFToLgE5qjUFnECzbCl_EaNdCdtZi2C0oC8TVUi_KTO_yDy8f1NTtBFya_XsSTsJ3BChzA2RudGPzQsGMq8X13BVjjDkITvtRvOOqBrVEsXvPggj72Yqt5KYsAvzP8kv-qiKK7Alr7hkIF3D7_pWxTnqrJgjqT8jr1BGVjbmWpTrDCGBlk5lkx8DckrAlocuXm694FeYap8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آرام جوینده همسر سپهر حیدری اسطوره پرسپولیس: برای پیشرفت نیاز داشتم پارتنر بهتری پیدا کنم برای همین از سپهر طلاق گرفتم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.5K · <a href="https://t.me/alonews/137759" target="_blank">📅 22:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137758">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
باد شدید در هنگ‌کنگ داربست بزرگ یک آسمان‌خراش را فرو ریخت.
🔴
رسانه‌ها گزارش داده‌اند این حادثه در پی وزش بادهای شدید ناشی از نزدیک شدن طوفان «نول» به وقوع پیوسته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.9K · <a href="https://t.me/alonews/137758" target="_blank">📅 21:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137757">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
مدیرکل راهداری هرمزگان: کنارگذر هر ۹ پلی که در حملات آمریکا به هرمزگان آسیب دیده بودند، آسفالت و فعال شده است و عملیات بازسازی پل‌ها نیز در تمامی نقاط آغاز شده و در کوتاه‌ترین زمان انجام خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/137757" target="_blank">📅 21:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137756">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
ادعای العربیه درباره رد کامل پیشنهادهای عمان توسط ایران و خروج هیئت عمانی از تهران، تاکنون از سوی منابع رسمی تأیید نشده است.
🔴
گزارش‌ها فقط از ادامه رایزنی‌ها و اختلاف‌نظر درباره سازوکار تردد در تنگه هرمز حکایت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/137756" target="_blank">📅 21:49 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137755">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=spJhQ6SQ5jgITvR9ERfzRoKwK5prAyoVhDSgcFFPlbN4MkwurEAtgfhoAYtEiw4GeMqhnAM0_W1GwetcRq7cpIt7za3JlOzBpqXBw6o9WlQI8sP1XHEf9O0-oHFcue3cHToTdLc1e6Bnk3mwTZlgr6U9oIOXMJjcrV6mY4Y3DqAE5RarxN3mngZkTjAoGMkBew50rsigNF4kd7Uc-aOr88WNGZes5cZjlRVnsR7ynIDRAW2KJmdpZlNjehcs2h5w3EN6txuvMmWgJ7MVKNxb7FJLPnTqdBN8nyk6LTkbnIDo1WHsPzJCIWkW04PZPcpx3pJ7o5hUM4gQ1iFGX8JjcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/567a79a6d9.mp4?token=spJhQ6SQ5jgITvR9ERfzRoKwK5prAyoVhDSgcFFPlbN4MkwurEAtgfhoAYtEiw4GeMqhnAM0_W1GwetcRq7cpIt7za3JlOzBpqXBw6o9WlQI8sP1XHEf9O0-oHFcue3cHToTdLc1e6Bnk3mwTZlgr6U9oIOXMJjcrV6mY4Y3DqAE5RarxN3mngZkTjAoGMkBew50rsigNF4kd7Uc-aOr88WNGZes5cZjlRVnsR7ynIDRAW2KJmdpZlNjehcs2h5w3EN6txuvMmWgJ7MVKNxb7FJLPnTqdBN8nyk6LTkbnIDo1WHsPzJCIWkW04PZPcpx3pJ7o5hUM4gQ1iFGX8JjcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی عجیب از جنوب اوکراین که یک قطار روسی را پس از حمله پهپاد اوکراینی در حال آتش سوزی و البته نشت سوخت در طول مسیر نشان می دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.6K · <a href="https://t.me/alonews/137755" target="_blank">📅 21:40 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137754">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
حوثی‌ها (انصارالله) فیلمی از پهپاد شناسایی و مسلح بایراکتار آکینجی ساخت ترکیه که توسط ائتلاف تحت رهبری عربستان سعودی عملیات می‌کرد و بر فراز استان الجوف سرنگون شد، منتشر کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/137754" target="_blank">📅 21:33 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137753">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KVNZ2cklUXkgUXl15GcJ6COuOoQcN05VOa4gKRPK7Pj-eeqdoyHb-x2LQbs4j22Wja-qP4tV_rxxn3sQYEksTu0DLkXjF3rZ7c9Zj-llttxKJshDwdmWcnoaxcRrgc71MSgpeLep-IookjV-DOdEKElHkng6kzGDJ8wtDajB56xodXasU_d8pfGJCz0eLNZ1TjnT2VIGi0c2UF2c-7AZimN-4yBZ_WG0X-MAXA1Bb_RCgMN5a2kiq2CNq3vFPyoEttdjok-oCU6CVJV-Y3NUK3UjXfCtUWSTRYEl6AdlBq7Oe-5F_eim_33H5qOhmJ767DXYWSUiqZ13VHj4VpIaOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عجیب اما واقعی ، لیستی از عجیب‌ترین و پشم ریزون ترین دلایل طلاق :
دومی عالیه ، طلاق مرد از زن چون زنش مهمون که میاد خونشون میگوزه
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/137753" target="_blank">📅 21:29 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137752">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">۱۰ دقیقه تحلیل مولتی بازار | سیگنال های طلاجهانی،نقره جهانی، نفت و بیت‌کوین!  عزیزانی که تو وبینار «سبد ضدبحران» بودن این اپدیت تحلیلی است که اونجا بهتون دادم و با هم سبد بستیم.   راستی امروز کانال سیگنال کریپتو(ارزدیجیتال) ۲۰۰ نفر ظرفیت باز میکنیم دیگه میره…</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/137752" target="_blank">📅 21:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137751">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/npgFwUlG-yAaqim0D6x6ksvZ1yQ2QNXyB_8sM2eUea_wssLx4GCyP3FJG-QvsR1lWxGvjw1aSBdEZ6u12y-tUNWj4aLKZlymS4F22KJoQuBLpJF0NRzDjIJcHdkarZdYUm3ttdz5WkLNkXo_BjV4_MQYfiHEQnZad1ulM9_gdxFF32Gu0s6aG4rPn3hsUSmNzm53OiBen_UDAGmSS8OWkrx8KRNTeE3nsrmqlWCLZyInYDmlJXaWzXd9nQfaTYBa5avozyktDNaL7UYhaBiuckmoHxgJUvaf6vTmmv9ekcKWlFqZcUVbHghScvV_DXcSFAt4W0XsvZhQ7dVusUMOnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: تو عراق به من میگن عباس قهرمان
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/137751" target="_blank">📅 21:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137750">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
کان : نتانیاهو به وزیرهای کابینه گفته؛
آمریکا ازمون خواسته به‌طور گسترده از غزه، سوریه و لبنان عقب‌نشینی کنیم
🔴
اما نتانیاهو با این خواسته‌ها مخالفت کرده و جوابش به آمریکا اینه : «نه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/137750" target="_blank">📅 21:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137747">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/VX_iQ7cRo56Nb4yWebzSwyaFSSXEXK6qjpaf3FPx4PC-ZJLKynpMzg5uZq4PHGOeAqhFcPBvsmIpUtWdPmUN53vF5aGvGhMQB-6YlTnQtRPLlGl_oXO_39lSYLfQ3YrZmqW9mE3gpZkVBWjZnsPzWDQ2KxyCGGBBXryewH9uqX9MM6jO_u2vQVtZtoeyW-h_U6hK1aDbZ9ESfcVwA07T4W0ICIW5NfoQuLNhEK4bxk6vKCl0PrkSnQGjyQLLa-vXDQXxYXrYiSNE51XH6W0Uz6ocTcZHtu-DKQbIO2PuJbQcwmiIamR8kRHyG42Jg8fy0IjOWB_VuMMUkJF_IuiCjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/EbC4a5l262FtQwHK0vnzyXoKedtbUMlcxvEpZWrKcDvuo8Sdpdzih6zq-fuN_oxgjT8uy_uP28LI18qi9Rxz6MYOogZZED46RN7Nprc9EUcwJdrSULGIHCPuQxn9kZUkAhDUgvtB1XBnrYs3-w7jeJa6sWWzgRyaj70ip82qO0vWGOchBE2cH0sTiQPyO68S7OfOeLASqsr_HteWWal_KWnrQIfBJzcorhXl_Yexf2KWeJkgBBdD3VOUQDYWXNmr9tgk7Jd-pilMPGJ5Bp09dbwBkob_K7PjpElwYeIX0odmUQeSyRlIFpZQ65foZODt3NxKK2zpFIji5I9aqfp7aA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/qgZWfArUz3LvUJFpN9pwS327KHwjLDvjI9uE8ic4LnJrtfVBNepp55j8nuYhHmOsrSnNdeKCqaC79V3dQzeHGunTmjawcLrl4LwnNmL4C1G_sh8tICY_4tXShuWKPi2gNQ69Q_JbPmkm_TNmeURRipEV81IdFDszPPFrXzTaNbL3tv6MTdN1latf0TCBO-D8i0GURliOHenvZ0FlnJ0i4HWbJttY1N1Khuhu2ad4u5ABmzOB_vTitR8Rvpt0EwFEpZebsG-rW361UTe8lrbYQ1aWx9cU3LTNz8sR7A3GQNopiHUd2svzRj52EAam1zJWrOXCbcMkFrnU5tfyGLrkjg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویری از سرنگونی پهپاد «بیرقدار» ترکیه متعلق به نیروهای سعودی در یمن
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.5K · <a href="https://t.me/alonews/137747" target="_blank">📅 21:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137746">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
آکسیوس مدعی شد: آمریکا و بریتانیا هنوز در حال بحث دربارهٔ کنفرانس بین‌المللی هستند که می‌خواهند اواخر این هفته برای تشکیل ائتلافی به منظور حفاظت و پاکسازی مین‌های تنگه هرمز برگزار کنند.
‏
🔴
تاریخ نهایی این نشست هنوز تعیین نشده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137746" target="_blank">📅 21:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137745">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
سی‌ان‌ان: عمان پیشنهادی شامل پرداخت داوطلبانه برای خدمات ارائه شده در هرمز داد اما گویا ایران آن را رد کرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/137745" target="_blank">📅 21:02 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137744">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
بیانیه مجتبی خامنه‌ای  :
🔴
نامه شما، رزمنده‌های مؤمن و شجاع حزب‌الله، باعث افتخار و قدردانیه
🔴
امروز که مردم دنیا از ظلم آمریکا و رژیم صهیونیستی به ستوه اومدن
🔴
راهی جز جهاد و مقاومت باقی نمونده. هر کسی هم تو این مسیر پایداری کنه، وعده نصرت الهی شامل حالش می‌شه
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.7K · <a href="https://t.me/alonews/137744" target="_blank">📅 20:56 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137743">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h6KaC_H2y_4KsumjaXPacOcB38Df9HfAn1t1PsT2LEwv6PzH9bzIGKeI1LCTHRL6SWaEIy2x187KLLho4NlQmo_S0aQXs1DAYXy9SzMWSEsaWniDUq5SGcCbD70YRwP5mR2rx7G7CVXUXHGEqC01GG6m-xvvw-haaxV64pOyssagvTiKbt8ugb1b5XdDtRRLaR1N_jDUfXwXidiOANR1NCrLCmq1yKdPxUOnwtorU_tVAcqJPvgf_Kw-jNx6v4XwTnzRUGgNsqtgPK1g5T3TTYh_3k4klVR1pWMuoK8NgfGl5nKsp3EPhUbMfBj21bCQdMbJPunKCwEKgIipMAwQ6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
غلامعلی حداد عادل : سید مجتبی خامنه‌ای همراه با همسر و سه فرزندش تو ی آپارتمان ۱۰۰ متری زندگی میکرد
.
✅
@AloNews</div>
<div class="tg-footer">👁️ 69K · <a href="https://t.me/alonews/137743" target="_blank">📅 20:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137742">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
العربیه: ایران با تمام پیشنهادات عمان برای ایجاد گذرگاه جدید در تنگه هرمز مخالفت کرده است، هیئت دیپلماتیک عمانی پس از مخالفت های ایران، تهران را ترک کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.7K · <a href="https://t.me/alonews/137742" target="_blank">📅 20:42 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137741">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/fMUdUVmdZdOBGFv-vEwCmU707YcgcnMx6hbp04c9ASZHE0kbjZWx3kMkAyJyFVZHgimovCwJiJDM7h_lO7j2mTOqBbJgSd6JtCI_NuFybrleb597vY5ON0k6No-lM2hYWM8r1GCtHSz9MFvjEbQbd2Do_POqSVmDDvrF5FpDXtspG7iQOJBRoOOSjWFICyp-g3hnTr7f0RWemQTE2QX82wV1aPcrn0pKSsQokunXe2Td-9gYfLBmGrSZxTEFFvVGCiylIUX4wRCWVzXbuWQBYj276y2vw9g563DHMyQTSYD-s9NsX_gs9oNYf0GXQYZqAVgywaEKCo3GV5roZM0QXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
اکسیوس : ژنرال برد کوپر فرمانده سنتکام، پیشنهاد داد که عملیات بمباران در اطراف تنگه هرمز متوقف شود، با این استدلال که این عملیات به حداکثر کارایی خود رسیده و بیشتر اهداف تکراری شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137741" target="_blank">📅 20:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137740">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=mwk7RHZ_4DXxyiLiU-aoLGB5nTCildx1PDhA-4BDUaCl_4zx4iPCvO4LZGRgYw3wTdhAaym7SoyqZkTimljEsFhTLfTVRcMlPf3fk4eTpkEs7df003Sc1YziZtROQHmcLka6D_94LsxAB3aKzGPCSawhpfwsbnrPF8vdGiWlCCmO6rYaelhEkVyOcZidYc7gI2Z5U9quV7b8K_uCD7EwXiNtOAOoTmjRoClLcfQP2vickMUntcU93BB3kYIM7GwbWjLv3T5ZJ0YLg4pE9at0xHXq0Srtsr-j-gBiGhL6AlcRsURfwPHmOlaK1K42mmqA5BiduxO1U5ipb3GtIM5cRA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f700083cc1.mp4?token=mwk7RHZ_4DXxyiLiU-aoLGB5nTCildx1PDhA-4BDUaCl_4zx4iPCvO4LZGRgYw3wTdhAaym7SoyqZkTimljEsFhTLfTVRcMlPf3fk4eTpkEs7df003Sc1YziZtROQHmcLka6D_94LsxAB3aKzGPCSawhpfwsbnrPF8vdGiWlCCmO6rYaelhEkVyOcZidYc7gI2Z5U9quV7b8K_uCD7EwXiNtOAOoTmjRoClLcfQP2vickMUntcU93BB3kYIM7GwbWjLv3T5ZJ0YLg4pE9at0xHXq0Srtsr-j-gBiGhL6AlcRsURfwPHmOlaK1K42mmqA5BiduxO1U5ipb3GtIM5cRA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو، نخست‌وزیر اسرائیل:
ممدانی خود را با این قاتلان همسو کرده است مراقب کارهایش باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.9K · <a href="https://t.me/alonews/137740" target="_blank">📅 20:24 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137739">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
نتانیاهو : الله‌اکبر، الله‌اکبر»... شما خودتون می‌دونید این عبارت یعنی چی!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.1K · <a href="https://t.me/alonews/137739" target="_blank">📅 20:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137738">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو : من برای شرکت توی مجمع عمومی سازمان ملل به نیویورک میام
🔴
از هیچ چیزی هم نگرانی ندارم
🔴
بیشتر اسرائیلی‌ها می‌دونن که باید با حزب‌الله بجنگیم
🔴
ما هم این کار رو با عملکردی فوق‌العاده انجام می‌دیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/137738" target="_blank">📅 20:20 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137737">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/psz4k2wUv-HQdLI_HrHAadbnfd93EU2we5PU39P8HV79SgzrsB7Z2P4EvEZ4mPmvQsAfe15hvccwidkp6-omkDlk3rh6jndNq4yJQKcdTJuZPnyz5uU89npKH-4P_PbqgGXHWcOCiEPne_oijAmSuqATTJmaODdd7o_Vmp05RximudW4ORtAPFqzlkmRcOwhd7dOI0_6bhHBKFAw-FduRa-ZXOp7hfIbCvGyalO5PWUdcwjpXtDGPqCP6vvr0S15s4gJJscrGufrJXRmclu98h22MaBOZJXA_AUN_9wYgWrrWzOrn3RPSbRVUT-eYLTYBSYz8wcVOk-fofkVIMQ5Jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
برنی سندرز، سناتور ورمونت، در گفت و گو با سی بی اس، عنوان کرد که به ترامپ گفته باید با حکومت ایران سر میز مذاکره بنشیند تا کشتار و خسارت به اقتصاد آمریکا متوقف شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/137737" target="_blank">📅 20:19 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137736">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6c20258523.mp4?token=OQqmFa-ygj0ojnOEKDVbgzGVKng7zzm1b66KL5T2zCfA1jWDsGDu5VT2ukqxnkyc9BtLY5p52MoQK5J_otIdifdk1vdaSvh2bdnmw97jp4VdMzzlug_cilqAGeaxFdum6Q0vJ9XW3TOp0hWSBRZkyKM8IY-8B40zFUxPA91nhkNgtKbow9lMl9-UQPUVuYXYRsgG_wakWLHmuu8nheIrWOFHy55kWR7EKO78T696YG-z6Vxwk2m-Y-II25-agIcfoiW_uYACH984mDGJISCQGM1nLkyQeshB1jBuUCSmQy4q9HBnz6KZtyK_04Oq0mqMpHijmvt40zD0VN7CqaT1gQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ایلان ماسک: تا سال 2036 پول دیگه اون اهمیتی که امروز داره رو نخواهد داشت. وقتی هوش مصنوعی و ربات‌ها بتونن بیشتر از نیاز همه انسان‌ها کالا و خدمات تولید کنن، دیگه پول قراره چه کاربردی داشته باشه؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/137736" target="_blank">📅 20:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137735">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
وزارت نفت ایران: در طول جنگ، ۱۱.۵ میلیارد دلار و در دوره آتش‌بس، ۶.۵ میلیارد دلار نفت فروخته شده و با این میزان فروش، بیش از ۶۰ درصد درآمد سالانه پیش‌بینی‌شده نفت در بودجه تحقق یافته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.5K · <a href="https://t.me/alonews/137735" target="_blank">📅 19:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137734">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/137734" target="_blank">📅 19:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137733">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DLZ4n-JRk1UWmTeorcPErt51x6EJkEUyIFOiepMuLzhmrWk_VYwhDT5jByLA6iTvIPmO-foCvqHv7c1I3wSaHlrZtjYUu-z6X5bWwVSOoVSHkgwvqb3akGbTQd1soJQ8D1WoHmaNjvCx9kO5k3p6DKesoVSaVjzNIh8aDUjQGAp_-ZSpiJwg2-q7ounKPLmzcxKFOQylIRIT6U9PonV5XAp1KEos-fwn4JcV6-MPINXSVHQY1eWRYAR3yZ5YAeV7ZF36VyseORAVz2qWrim5--fwExRPsX2D0LFI851CIwGqFbRZEpyaVD3Zt0QgwPTykudVSS2LV3T-m--YEQpYXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: اقدام اوکراین بی پاسخ نخواهند ماند
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/137733" target="_blank">📅 19:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137732">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
وکیل پژمان جمشیدی: موکلم در رأی نهایی پرونده، به‌طور کامل از اتهام تجاوز به عنف تبرئه شد و تنها به ۹۰ ضربه شلاق تعزیری محکوم شده که در نوبت اجراست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/137732" target="_blank">📅 19:38 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137731">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: پس از تصمیم دولت آمریکا برای توقف گسترش خصومت ها، یک منبع سعودی نزدیک به دولت ریاض به N12 گفت: "ایرانی ها با ترامپ بازی می کنند، آنها به او اعتماد ندارند. درک نحوه رفتار او بسیار ناامید کننده است. هیچ کس روش کار او را نمی فهمد، او گیج کننده است و هیچ کس به او اعتماد نمی کند. همه از رفتار او ناامید شده اند."
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.8K · <a href="https://t.me/alonews/137731" target="_blank">📅 19:27 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137730">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hmReNP6jA2Hf5iY36An0-H19IXmFoQdQG7deRJNY85Xbbi77UQO0_Tdnz0k9VKsIxWC3TW6Smlp2qgJbzXwQsCfPKFOeq3Bb86f5rD-MBK26dAtXghxQHOq6Y7dR5gSoIxtSvIKdGQllg-BeKctqDUE8e71JklRLVPtX0Wtweq7n1UUFiltmLikOzVHOb09pXPBha4BfMkh9CHSQCvNFdrhu-AdVieGA6lVAAk3FgjIoK41h7LjBPKVLAlwjInOEAJ-6pqWKLmITYsvRVVbiPaNO8QaoSXo3ebrw-gPpbXBB5pKzCdL1RCmb9_hGjqaOA4IMoOsBOlVL4ey1ZRVR9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توئیت عجیب عضو کمیسیون انرژی مجلس:  فقط نفت!
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137730" target="_blank">📅 19:22 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137729">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
احتمال شنیده‌شدن صدای انفجار در بندرعباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/137729" target="_blank">📅 19:21 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137728">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24096cdef.mp4?token=ehyW3yu-PAIXoXDRbw2Luhe0fX18OHODJjTOMC7oK2TWAjEMFtUCWHZIKGHCDt2b36ljrJsUzX1G6JxeGXpvckkEJiiF2p4I6LCBXO9Ln4boIk3fUVvdi0b_FwpM-uhc_gM9gANzsVcYEJk3LTW5wlQGJWBnfxzj3Kk4bvDYpLSb4ovp3xQOvtV3Ik2IcGw1kKk7rkmdOyDgDlvi1-Q_FgUHG96nEDCm80jrQ4HwofVlU2tG5k4OtrIFqnUPgt4vFK99mn_lGiWljO2GFWOePr13VjWUOZL_xcimROI4c87snCXpmPxOuPqAKHQ5nOzpV3TAYxVdABsN1Iys372gIIi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ولادیمیر پوتین، رئیس‌جمهور روسیه:
تلاش‌ها برای منزوی کردن روسیه، حتی در چنین حوزه حساسی مانند دفاع و امنیت، شکست کاملی است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/137728" target="_blank">📅 19:14 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137727">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
نتانیاهو: عربستان سعودی در ازای عادی‌سازی روابط با اسرائیل، یک برنامه هسته‌ای غیرنظامی دریافت خواهد کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.8K · <a href="https://t.me/alonews/137727" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137726">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
نتانیاهو، نخست وزیر اسرائیل: اگر ایران به اسرائیل حمله کند، چه مستقیم و چه از طریق نیروهای نیابتی، چه با موشک‌های بالستیک یا پهپادها یا هواپیماهای بدون سرنشین، اشتباه وحشتناکی مرتکب خواهد شد.
🔴
زیرا پاسخ اسرائیل بسیار بسیار قاطع خواهد بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/137726" target="_blank">📅 19:09 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137725">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CwLyiAlFjjEhW78VD6DTJSjQ5GRYm4Hjz2BCcZe1L-DlTsxdOZOIcxjTpmHFlWTRbF_iyioSxM0KCj42D-EYgAmyWvNKU7iuQGNsTucHNA35p9Kv3q0Cww3M7HUvyAtW4wMMzhMVHR-MT-bHZa17UcwTWMOB8HCYb4RZuCmaks6tJoK7Qdt0EVMesU7b69xj2fzdkbrFx46rG797-C6dYT_oG-BKZyJVbDJJ7KdnKjF0edl3XJO1O2bcMwlpVQVP1u1VS27uXryUjptDyHw8M7wH0_NldvyV7tkvSE2hqRW0YOiqRjhadWtJXgnTZZR0X4vAWqWb-t6LepTEYj3PSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
پست جدید ترامپ
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/137725" target="_blank">📅 19:06 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137724">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
پادشاه بحرین حمد آل خلیفه با رئیس‌جمهور اسرائیل ایساک هرتسوغ تماس تلفنی برقرار کرد که توسط پادشاه بحرین آغاز شد، طبق گزارش روزنامه تایمز اسرائیل.
🔴
دو رهبر درباره تحولات منطقه‌ای و بین‌المللی، همچنین تقویت روابط دوجانبه در چارچوب توافق‌نامه‌های ابراهیم برای ترویج امنیت، ثبات و رفاه در منطقه گفتگو کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.1K · <a href="https://t.me/alonews/137724" target="_blank">📅 19:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137723">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/59abab6717.mp4?token=EsQlYn12S9VeerXtvOpNYy_LUcD_QLz81rFVVH107pbl3dECRrD3XumTu3SDDkVzWNvakJuDgpLYXtg632dBX_8NMAWnFJKAuGr6jjdYz_27aYdJQ_6mQ8XMcYk52yw2o15GxgLZBwD5eT0ivWDD6LK43SzsQQxzRc2fXqLs6LGhyBBulxQm3rjBYto5gonNKljzdEZs94BZ8C8Bz0gjktZWt3oLjLGhC87w24ot72FZeKiQXEZqAQWTkSTUtV0TAfPnn7kDf165IsagYrT1jQaZH5dpwdlLjVkT2T7GakPn9Zw_mexvhYIG923MhCV7w8HCzs0KJGX-SO-wq0jHmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بارتیرمو از فاکس نیوز: انتظار دارید کدام کشورها به توافق‌نامه‌های ابراهیم بپیوندند؟
🔴
نخست وزیر کشور اسرائیل بنیامین نتانیاهو: آن‌هایی که می‌خواهم بپیوندند، با افشای نام آن‌ها در اینجا احتمال پیوستنشان را کاهش نخواهم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/137723" target="_blank">📅 18:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137722">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:  آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:  اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده…</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/alonews/137722" target="_blank">📅 18:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137721">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XNJP7GQ-oASFsBaOvGLsz-2x2SCSmMwVP7Cmh-vcVyRH1LGdC5YaybkAlIAyJUh8mkGj2ynL9_rKgeY_1LHdKbdhB3tJPibyBZpmp9W0jVolCEzY5CwiuYZSM1zsS0F-VPD8I_jTqeFoiwcnwmjTNvTcKZBLOVWQ-5VUBpmwm8JUq3mdPNCtxIDm33Z2c-6KExRKIzHY3HI4T1E2yD6Z-0RqdXqoOjs2UHwhVj1dt68X47gKwY-D-nRujB0-j-mWUld0QYI6d5-gqBffOJmbDuw8uKq-ZbMpRBCWJBhEsYFGeeqmUNZ32p4cOlPlGha7b7C15sOt8BTKj5NNUWVxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
تو عراق یه دختر بچه مظلوم ۱۰ ساله توسط پدرش کشته شد
حالا دلیلش چی بود؟ بدون حجاب تو تیک‌تاک از خودش ویدئو گذاشت
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/137721" target="_blank">📅 18:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137720">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PLZ4Si3gEJbu5m2aAfcJ4OaFAuY1ocRUj_3kfmqdY_21N-0WQvboh5R34She3vWmH4Iv-LA0hHAtKIyIWp2IAwCcUlCFzH8xRrRK-IQ2vkJNouupxKkR4Lq-sj25r6TvK7ZqOEZ_bloiAGRPxmXBb8n6IcQN-34d4Y-_YDJm1RJe2cmlorqr520E4TLWf9enwoGURERM0XVmjY361zMs8DD1Kzl7HivBfaaqlwZBahU7UuW-FColoXFqVRsvsNwMSPhOB0ZkkvxU4Cpi9aRCmwxpRPK1RMsgxYoLETkwGK9i1FX1GaD-opBdW65_h7FKTAf72kuKZqrDS4QCth7ytw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رضا پهلوی با گروهی از اعضای جامعه‌ کوییر ایرانی (کونی‌ها
🏳️‍🌈
، دوجنس‌گراها و تراجنسیتی‌ها
🏳️‍⚧️
) تو پاریس دیدار کرد؛
🔴
شش خواسته این جامعه که تو دیدار با رضا پهلوی مطرح کردن:
حق تشكيل خانواده
حق زندگی تحصیل و کار تو محیط امن
جرم انگاری کوییر ستیزی
صدور مدارک شناسایی متناسب برای افراد ترنس
دسترسی به خدمات درمانی متناسب
آموزش و افزایش آگاهی عمومی درباره مسائل جنسیتی
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.5K · <a href="https://t.me/alonews/137720" target="_blank">📅 18:44 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137719">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/87da6000db.mp4?token=uIivkVqAguicdd__YufadaAX_PTmoFLah69mEky9XJ4sp_HforoYHalcXCnlLjgIKgShHNrMM4_ZjRw_YRfdAhiBwnwOVzv4Lft3Gn0gOMlPGoDUTM02IiYGG1XyyDePMdW_LxDr5BHdB38hQ5y-RUmAzW_LBXKSvKkfyQgpfFOYRmP3awfaqpQUhLgEQ5_6Hud-_h5_4JbyrIiH4Qech12N58qS1wzq9OCNgISuz_pK_-ZnVmMfVaQvpw2qiwGVAPegwva6-rkquMBaIHfEOglcAz-9OVTfM8K9zcrqdP53QmEZjdaeWX3xp9Bm19H3vaThA_zGUYV5p7WZaJMPbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/87da6000db.mp4?token=uIivkVqAguicdd__YufadaAX_PTmoFLah69mEky9XJ4sp_HforoYHalcXCnlLjgIKgShHNrMM4_ZjRw_YRfdAhiBwnwOVzv4Lft3Gn0gOMlPGoDUTM02IiYGG1XyyDePMdW_LxDr5BHdB38hQ5y-RUmAzW_LBXKSvKkfyQgpfFOYRmP3awfaqpQUhLgEQ5_6Hud-_h5_4JbyrIiH4Qech12N58qS1wzq9OCNgISuz_pK_-ZnVmMfVaQvpw2qiwGVAPegwva6-rkquMBaIHfEOglcAz-9OVTfM8K9zcrqdP53QmEZjdaeWX3xp9Bm19H3vaThA_zGUYV5p7WZaJMPbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
محمدرضا باهنر درمورد رادیکال ها:
اینها در کشور، ۱۰ درصد هستند، پس باید به اندازه ۱۰ درصد توقع داشته‌ باشند، نه اندازه ۹۰ درصد جامعه
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.1K · <a href="https://t.me/alonews/137719" target="_blank">📅 18:39 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137718">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز: اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.1K · <a href="https://t.me/alonews/137718" target="_blank">📅 18:17 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137717">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=HzlS0wTRvW8zrMwyQ1baHSKKStXrmgnlXeF_ltmVLCfH4jVBD8AOr7U7yQ7s5ZF6mfSNfAOxFJtvc8OoeZI4Jlh9WgAGYt0VVEps1WGmW4uNpd2ea29t_EfGu3DrFn7LHoW3BN7CBSF53e8m4EsxFY_-XN5SP9EgXVRJK35jnKb4oPDTQjPQOqk7QYClW-8B_PQBV3yAgOFrLVFv63guWlkzJlSrr9K4MTCO6-SQ00hvFrRRRn3J_RpjAYXWtZO4bR8O1YT4QAr763llrkbPOaCoicbfxd4b3QHRv8ZdT22yyn8qdI00Jxsseu_ClcBJtu0_CQHx4PtHDNLIERoK2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3da6c5df1.mp4?token=HzlS0wTRvW8zrMwyQ1baHSKKStXrmgnlXeF_ltmVLCfH4jVBD8AOr7U7yQ7s5ZF6mfSNfAOxFJtvc8OoeZI4Jlh9WgAGYt0VVEps1WGmW4uNpd2ea29t_EfGu3DrFn7LHoW3BN7CBSF53e8m4EsxFY_-XN5SP9EgXVRJK35jnKb4oPDTQjPQOqk7QYClW-8B_PQBV3yAgOFrLVFv63guWlkzJlSrr9K4MTCO6-SQ00hvFrRRRn3J_RpjAYXWtZO4bR8O1YT4QAr763llrkbPOaCoicbfxd4b3QHRv8ZdT22yyn8qdI00Jxsseu_ClcBJtu0_CQHx4PtHDNLIERoK2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
نتانیاهو به فاکس نیوز:
اگر ایران چه مستقیم چه غیر مستقیم، چه با موشک چه پهباد به اسرائیل حمله کنه، جواب اسرائیل بسیار سنگین خواهد بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/137717" target="_blank">📅 18:13 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137716">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=H65IfRQMBym_yBgAs_XtKkZ9iVIQm1bryUCt5qaoGy086oqJEuqqePhaHhPZrqSRTcpWO4PsDmJMNPV8QUX4-jxGhVO2OKen5wAjEM0V3HIKoatmDUtKdMkQ9iezwQvGRdqsukCQYIazIkPC-1eOwCY7ANuG_bXqemfZaNY8C4dJkdnvMptap213mppJpvCMm9gTleDOm1srygIGfvfwwmJ6mYBXhTQknXnQA29mdYCGhFnJyjpVsIIACEw_F4tKYMfsHg2aL0-KR2pb0XSHJx7Uws23Kc11-nOYo1bf1iHk5CiK8LW1T74euBWhRA_zpGExLVGyBdUmfBRRvFmffoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/851a7f43dd.mp4?token=H65IfRQMBym_yBgAs_XtKkZ9iVIQm1bryUCt5qaoGy086oqJEuqqePhaHhPZrqSRTcpWO4PsDmJMNPV8QUX4-jxGhVO2OKen5wAjEM0V3HIKoatmDUtKdMkQ9iezwQvGRdqsukCQYIazIkPC-1eOwCY7ANuG_bXqemfZaNY8C4dJkdnvMptap213mppJpvCMm9gTleDOm1srygIGfvfwwmJ6mYBXhTQknXnQA29mdYCGhFnJyjpVsIIACEw_F4tKYMfsHg2aL0-KR2pb0XSHJx7Uws23Kc11-nOYo1bf1iHk5CiK8LW1T74euBWhRA_zpGExLVGyBdUmfBRRvFmffoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
کریستن ولکر از شبکه ان‌بی‌سی:
آیا حملات برای چند روز آینده به طور موثر متوقف شده‌اند، یا می‌توانیم انتظار داشته باشیم که امشب، فردا و در روزهای آینده حملاتی را ببینیم؟
🔴
مایک والتز:
اگر من رژیم ایران بودم، رئیس‌جمهور را بسیار جدی می‌گرفتم. ارتش ایالات متحده آماده و مسلح است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.7K · <a href="https://t.me/alonews/137716" target="_blank">📅 18:04 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137715">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
سفیر آمریکا تو سازمان ملل گفته ترامپ حملات به ایران رو موقتا لغو کرده تا یه فرصت دیگه به دیپلماسی بده
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.7K · <a href="https://t.me/alonews/137715" target="_blank">📅 17:54 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137713">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=mzStY51LetdIP-OqXdxgdyBHPkTgGoBgTbJxdJQVSdHokQxriONjPdKZoqY8CMA0Olbt36va5Dg0gcp4PdKn24iYXaxLcbQD7Qxne32yPiN80_tE9ekoWv6Ijib0fdCuqU-EHmhra00fp3DZgNR17_XIcCzl2IjyY1NzTptsyGbduEbtIMUuz4iZMBbUIO66AoWd2C6HBpjTurmt-6mFitbz3Z5ez15Go8b-hPn-p4GI-VD1unKTufq854kQWQmha-3UWJiLxzuj4OdGARjc_rRpwicgM_WL9numFJQRlybQlzowwRotrytnHyspfg9yYX782dES69LOQ30tM92Qmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19b1e9d73.mp4?token=mzStY51LetdIP-OqXdxgdyBHPkTgGoBgTbJxdJQVSdHokQxriONjPdKZoqY8CMA0Olbt36va5Dg0gcp4PdKn24iYXaxLcbQD7Qxne32yPiN80_tE9ekoWv6Ijib0fdCuqU-EHmhra00fp3DZgNR17_XIcCzl2IjyY1NzTptsyGbduEbtIMUuz4iZMBbUIO66AoWd2C6HBpjTurmt-6mFitbz3Z5ez15Go8b-hPn-p4GI-VD1unKTufq854kQWQmha-3UWJiLxzuj4OdGARjc_rRpwicgM_WL9numFJQRlybQlzowwRotrytnHyspfg9yYX782dES69LOQ30tM92Qmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هجوم عجیب مردم به سمت بازیگران در مراسم اکبر عبدی برای سلفی گرفتن
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.8K · <a href="https://t.me/alonews/137713" target="_blank">📅 17:51 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137712">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=E3GdkfSS9iImEU_JG597VH7mfmpDtDIwbsU3N0IgtxSp_1dlLh1WZYa36S5kFv1UO7bYsyPalV7Oh0LU9n04l_oa9uh_PbwybdkoZbIHJOoVsQxlYKabZb4CAludTq0KfZuVSJEap5h_Z37STrVvekJowvc-WvGa_X96127DHm3vWXHishk8uQmIaZKgoG-jJ7Pq4wVTq6oN1iDY8OcgmGSzX49m1vEfjZtZqaHMRMBgsL5oencNFg-mzsxkiEZtWAO8TgE_VPHxWPC7LShu3-skJ5skP8ovgyOusgIjrrSDR6WnHneU5ZrI7Yf0_R3fMVfADWLZtz-tMMMLikK90A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ed262802b.mp4?token=E3GdkfSS9iImEU_JG597VH7mfmpDtDIwbsU3N0IgtxSp_1dlLh1WZYa36S5kFv1UO7bYsyPalV7Oh0LU9n04l_oa9uh_PbwybdkoZbIHJOoVsQxlYKabZb4CAludTq0KfZuVSJEap5h_Z37STrVvekJowvc-WvGa_X96127DHm3vWXHishk8uQmIaZKgoG-jJ7Pq4wVTq6oN1iDY8OcgmGSzX49m1vEfjZtZqaHMRMBgsL5oencNFg-mzsxkiEZtWAO8TgE_VPHxWPC7LShu3-skJ5skP8ovgyOusgIjrrSDR6WnHneU5ZrI7Yf0_R3fMVfADWLZtz-tMMMLikK90A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بهروز تابانی قهرمان سنگین وزنِ چین شد و مجددا جواز مسترالمپیا رو گرفت
🔥
بهروز تنها نماینده مردم ایران در در المپیا است
@AloSport</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/alonews/137712" target="_blank">📅 17:41 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137711">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
روسیه ناوشکن اقیانوس‌پیمای ۹۵۰۰ تنی جدید برای نیروی دریایی می‌سازد
🔴
فرمانده نیروی دریایی روسیه گفت: این شناورها از نظر جابه‌جایی به‌مراتب بزرگ‌تر خواهند بود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/alonews/137711" target="_blank">📅 17:35 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137710">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
مقام‌های فرانسوی اعلام کردند آتش‌سوزی مهیب در منطقه ژیروند، محل استقرار شهر بوردو، همچنان از کنترل خارج است و تنها در شب گذشته ۵۵ هزار نفر دیگر از ساکنان پنج منطقه در جنوب‌غرب این شهر تخلیه شدند. با این تخلیه‌ها، شمار افراد جابه‌جا شده در منطقه ژیروند به حدود ۲۲۰ هزار نفر رسیده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/137710" target="_blank">📅 17:30 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137709">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
فعالیت‌های دریایی در خزر ممنوع شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.6K · <a href="https://t.me/alonews/137709" target="_blank">📅 17:26 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137708">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رویترز به نقل از یک منبع بلندپایه ایرانی: اگر واشنگتن به توقف حملات خود ادامه دهد، ما نیز حملات خود را متوقف خواهیم کرد.
‏
🔴
پس از توقف حملات ترامپ علیه ایران، تردیدها بیش از خوش‌بینی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.8K · <a href="https://t.me/alonews/137708" target="_blank">📅 17:18 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137707">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
اولیانوف: درگیری ایران و آمریکا راه‌حل نظامی ندارد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/137707" target="_blank">📅 17:11 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137706">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QQoXyWLymmgCBCEykqsc8dK-FSo6Vy5hhmbrpdjM5s4fDBTeo71ChwCKDODe3jFsT9tsXAGrbCHJztuepeLJWn18cL7fTL9y_YQXmklom71RDsqVAjqbWPRB6nj8ZBTNhsHbHvXcVOpm-UKq6imKvhynDs5CE67q-0O65sqg3Pl9TwetS1LYiOvtKukAswS0THipaEI7lWL-r2Yw_0ngArK1hRZWUUvfgQvjvGNeBgsIB1BzGzJKci1MEMeFJcnWZrnH4AlVvOvgnArteK2IHLms_f2icx47p6Ba6AcPBIf786C58N6r-qNkADd_7Da-Gg9lAyyVLlG5s6d14ZUmOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
العربیه:  ایران آمادگی خود را به پاکستان برای ادامه مذاکرات در ژنو یا دوحه یا اسلام آباد اعلام کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.7K · <a href="https://t.me/alonews/137706" target="_blank">📅 17:00 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137705">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
مقام ایرانی به المیادین: ما آتش‌بس را آغاز می‌کنیم به شرط آنکه طرف امریکایی نیز به آن پایبند باشد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.7K · <a href="https://t.me/alonews/137705" target="_blank">📅 16:59 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137704">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔴
فوری/ الحدث: واشنگتن و تهران، پیشنهاد پاکستان و قطر مبنی بر از سرگیری مذاکرات را رد کردند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.5K · <a href="https://t.me/alonews/137704" target="_blank">📅 16:52 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
منابع سعودی:‌ ایران به پاکستان اطلاع داده است که با ایجاد یک کریدور جدید در تنگه هرمز مخالف است.
🔴
ایران خواستار از سرگیری مذاکرات در مورد تنگه هرمز، سپس دارایی‌های مسدود شده و در نهایت موضوع هسته‌ای است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.8K · <a href="https://t.me/alonews/137703" target="_blank">📅 16:50 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع بلندپایه:
ایران به مسئولان پاکستانی اعلام کرده است که از مذاکرات خارج نشده، بلکه «آن را به تعلیق درآورده است»
🔴
ایران به پاکستان تأکید کرده است که ادامهٔ مذاکرات بر اساس یادداشت تفاهم ضرورت دارد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/137702" target="_blank">📅 16:48 · 04 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-137701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DmhRFyMi43e9T0unIH6GY_uk5LnMSAWiP5PNFNr_BIry9goNQTCP8mZsF806PwIle0taYJ6qvmFmo0PaqnGRM_BzDm32AtG_E3Aw44ac8o6tn7zH4zTc4OGlZD4rVlONnuQC_JkcGD3ahapiMfMCHZB9nbXOeHl9wt1OZTWSP2OmLxegfmCD2yVDnNuxjnRYJogIbl4bB_ObfFwQt2szCiEcUgHNaBcJBoCq0AoV-PueI2HdFJS1ysKMnrVIsc87vwPG_dSFhN33RGpT28PKXjlbF48nRptNeBSy5kl6QemK_32HR5oNQgdiM0e9lDSqR-L07mW--GzpEWS1FMXV3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
امجد طاها تحلیلگر مشهور عرب:
ترامپ حملات علیه ایران رو به تعویق انداخت؛ نه بخاطر مذاکرات، بلکه برای اینکه منتظر جلسه رهبران اسرائیل و گزارش بعدی اونا بمونه.
🔴
این وقفه بیشتر شبیه زمان خریدنه تا تغییر مسیر. تعویق به معنی توقف نیست؛ آخر هفته آینده میتونه تعیین‌کننده باشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/137701" target="_blank">📅 16:47 · 04 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
