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
<img src="https://cdn4.telesco.pe/file/NaYTvHoa1w6nI-dbIMTPVjIzvNm5vDMpCuDMz_WRBW68T39iSlpjl2a3ayDPAHH5ORIKwvxBitZFEDa75kZkItA6fNfZmN0PFptp5s0FC36l-nlwbUf8TaWbUuazLq3k2zLeqrqQlEY4aBAV4hlq8qYwA_GTB27vcisPR4nzPTJtVPiKuZq80Mzv3q-8gLj4gCVRr6yI1UDRDRBnIs5ODs5RdKm44GKAtUgYepsCbhi1yQh_e1q6iY3MEyHlEL9oblcYApEWamZH19YQVYqP6cdtxKirnYQLNwlc63dSa_dgMjDu8lKot96VoI0tjae610L-HybiZiz_yfmpS7ZLRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 939K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 13:45:33</div>
<hr>

<div class="tg-post" id="msg-130311">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/td5w0i6mXR3I3XlY6IQZnpswh_3mH5aWdgjCtqNzsj_4lpWM684iCnek6dkcSBBALssbyaZBthWDyLsEaRHRUAMP-aR9FkwrELYE3bm5G2dCYIAlQ9bVsSu8pVZwOLoq3aL-DfFgOYH_EcBN5u3C0usOxvm999i5GQli_KvPw9PN-lYYH4qqG6mcPzFbP-6uLjtFTXgkyp93ftEwaaUVSLHcuA_nw5hFklhsImbSDwWfUZKEjh8Mm2aIcRL0kdxpt7VM3DilxwYyXBUW3sYb7z9govViCUVTIG8w00fEv2Vn8kLB64u0OsHhh2TA_uOhFwTvG7UbMjM1l4cfxOyhWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ :
ما یه بازار جدید داریم که داره شکل می گیره و اسمش کشور دوست داشتنی ایرانه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 4 · <a href="https://t.me/alonews/130311" target="_blank">📅 13:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130310">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dO7wpqCLsEte4KfuMUExYgHP62Hl1UbZagm5nfCTUVG5jopjTYmbMq36RQnz2-GUOczeFiRF30ziduo9w3DaDSypfnJPwZ4F60kqcTzYe3FUN70vSGuRs7AQAYQ5Plv-MtiP5fxUFMtETP51b-9N3ny6GUMOy_C6F7W-DbysZsW5vTa89aW6qRk-kSsa7_l4GveKFOBVPQJCW54PfFTdd4yh_DsxuGxgDV6X-mFzNNs1eQ2r7bcySQqjCqBNgeTzVZxhFQLF9CuxsVTRkB0MQKDT07k5Uf5rON6nR_rcBQWIV1d3Z18nNjXI5mzgglSgIOmdoChxe4GXHMjhCcrbUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
روحانی: امام حسین هم روز عاشورا رفت با عمر سعد مذاکره کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/alonews/130310" target="_blank">📅 13:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130309">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/bfb3904efc.mp4?token=Kg35v6ywghDE_kwNMEul_s8Y7-vubLcR6a_EHEeVB5MrwdCU44-6soYkeQX5-XEHQaycFFFXyV3g75pAZI7HJ07dP98wSx48JfI-yJ6_TIqFDulJBIRVOETGRnACSUF77p-vWiMI-9OlA0Wu2mf1D0A3MsRb1BMv7VZK-NVqVTu_hgMnJCg-WQRTKq0hMTXwptcafNaXIMlgHKOvFdqMkaqaDGsI-rsqxMkX2raG7TmWNHkPF2uXeSGPfkJWOeJL5JmYVC6XI0IdlXzykH0TjTr-_uL8gZzWs9TaIIjbrUpAOwesv_tQfVwoc03prW3ysR-tCRTTimTjgfFgWLTh8Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو یکی از مراسم محرم، شیر تعزیه افتاده بود دنبال یکی از لشکریان یزید، که یه لحظه جلوش رو ندید
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/alonews/130309" target="_blank">📅 13:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130308">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
حزب‌الله: با تفاهم ایران و آمریکا، ما به یک پیروزی بزرگ رسیدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/alonews/130308" target="_blank">📅 13:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130307">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uh8c7Q2Js99enYX5dd93_2L235xob4WFZeovi1UVGHkpXcy_xkeZYqWhnTBCI6pfsi8dkLAk5tXXxHnBr2_czsZ_Iu3Ifgxz9j2ucGV3Y47enPkSipzxY3IgCT-enQez8mm4240dUEQ9Uwmvage5Ak_8sL42bhrDFF0Wq1AV5NK5fwXVX48maXNqu2BqwNKeg53jLbkudO068WPUhyZHDeSeY8kI2trhipkTNgg7TDXuK2ssmpLhoUWYsDDKOk664acsMVcQs-j6O03o33stBI35znWEyVSs3x7_3NXgbqnFs43zKD-HFPYICH3g2wGsALnwOqlRT1RSrQpdgKPdQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
شبکه ۱۳ عبری به نقل از یک افسر ارشد اسرائیل: فروش جنگنده‌های اف-۳۵ توسط واشنگتن به ترکیه، آزادی عمل نیروی هوایی اسرائیل در خاورمیانه را تهدید خواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/alonews/130307" target="_blank">📅 13:12 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130306">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/alonews/130306" target="_blank">📅 13:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130305">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/99cd497f75.mp4?token=Bi6Q6dhfCvKx-c05tJIxAZBbSzcjRPSah88e0SOg-fdC80kJtLInzMONL720yr1DU1xOfhu9baZJo7kSNlgVMFi4Noj-cZ1aXQlcqu3v0qGOYcXL7e6AtVtkxYAEqvIUIKfbRnXwJwusSvvZJW1gsXUGF9wL9WXxuIzBh2RkKwIDlOvSOrlGvtya2JlO-hjUIoV_U94wWwIpqhCwA98X7jaOhZ3oUivnBlz6fog-hcgof1zp8V95__lsA9ZrOWm9l6c8seLwvLuiz5aX-sYiv4noArQBh_uHWT9g7ZUTK49XAYQJoxOfAkJXoJERo3N-NQMYD71yOC8BCI3j5Krv-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قاسمیان: به تعبیر قرآن باید اینقدر با آمریکا بجنگیم تا صلح پایدار برقرار شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/alonews/130305" target="_blank">📅 13:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130300">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MIFTUzq6LDictYI2iae1OyxlDffoJ79MtEyOkfwhL7aKIggo5PIMSfVANkSEnCZdhAaqNquXYUhmXA9MZ3s6Yx_7-dZulbCEEuzqZacLmCbdvconkw-oq400yH-FAg7bkpFIeviknEi5Ptkc-MDBGSNVsT6FlI7kVbkS4_7s24RxL7pRd4XwvRvzhl1muNu7ScGYRx8f9orgFa-obIZMbwYK0RP6A3pRxyuyjzvcNtLE_TqfVGJbeaUt-5-NArYZIQsm1D94I5Y18jj06WP78sHqIQ6Y9tk6XBK0UnRlNA1maD8z4UefqU9fi1T-XApezY5aFOFHCsjolAIX28IEfQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JAYidsAlDF6XIv8vbtUj37NKpwoY8nmKE7dw20SPCllxw0mulWt71CkPLJBeh4WW3Ova8p9o0U7y-ou9es6WMJ8z-ds-9ShP7EzFC8OpfhbhJMCiXZmhysdLPKvf8ThrX3Mm63iIenA1wwnhGX8_IRCp6pHc-Csg_db_t87sOUBmNvwHzfE_SAVLRZrnDsHJSUsYLEWmicTMX1B-a4lT0mbTJmqnsO8rKUdLWWD9ywUEQadxHtwEu8WmUUTEcVWkVOVNzCKzzL6INHVHWD2ib6cqFPEeK5D2lSncAuVEODZLVsD3AT_4MWzkbsxP4wrD5dk1gbDT2v984yKmtDZweA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oIPOgr-bjG1Tmwmi9QDtHkfcFIhSzK5RqfUtYa2fcwNhPFL50fKjevydCUM5hsPPNFEC6kmqFRxxCTqZw0UPff5jkNs2IkkmgMj9qWSnOJwX7bDp0YV__32DLftfzRMF9ruTY-tl4PVp216Rt0xU1K_i_UEQiq1Ohg4_E2-iuzk8AUW_grzoDgiyvEhGQ1wkJu77KkuQ53pni4d7uzrtoFcZP-UvitdfdPU96astSUcUWxEtJ8wc0Xj8N66KWzTWQK9WS60fyObyaCMAmh3iiNLyiUrF01Hwod36dndoaWGU2fOekVIxxlFDaGonM8ukbsfhQ-blWPU62c4zjAcMFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a25pcOGrmew_Prsd01rHY5MD61n24LsATmrTM2k4G3Rf-hfJcoHvPHLOWhXqWnwRHGIMxM3hHvxdDWM72CsxLwtYOvoaoNmlL_fyoRIrJSzm0jRVRSflFunbIhmaxLhf-mcp_rl2RV-9ezQipfJHuQF01pjK46iYYeCV03obsY2b2An7yA0on5Yk06lCsgqyrx5L7B2gYAqTtlOMAq6jw67t5JrchKrT0ahbgksN-sHPnkw6GmBrYeSChcolMP7kVmZdvAiIREE_7fcEuLVAOcLmFhq1rr2l5aQa8h1q838s2XMW129zLZpoF2aDdi2FaX_vAY_VUjBz3YrwPBwnRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vqGRiRmdLNIfpwcQFUtf12GMcGyqOBvUsxjXrb9uLDmNvp1CnGyybnCHJKLxey2JG4kc3C_H19pY3ZhnQFxAJ6rNWsHbasQbJDep-PEdbShbhdnohxMc7SVP_Ap9-BHbKrW1qddf4l3BgDDjzaoUo03uKzjl1ZzlS10k7kSLLKmleRXm1DoNYZNH133BTBIWLGysD_ojug9uNaBR1RuKiF7FYlPMfCPSIeowdyGHN_S_gNsFFtsxRbKiOY0JpMncqDIEPEeZ4VgXNp_bdROJdKAgDBs1dvPktDLwqhco5-hPDHqDrzFwKb1orCa26Zzgldf2BDe7uIzCcKXLpXaE4w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
تصاویر جدید ماهواره‌ای از خسارت های سنگین حملات ایران به پایگاه پشتیبانی دریایی آمریکا در بحرین
🔴
در این حملات، ساختمان فرماندهی پایگاه، دست‌کم ۱۲ ساختمان دیگر و همچنین دو پایانه ارتباطات ماهواره‌ای به‌شدت آسیب دیدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/alonews/130300" target="_blank">📅 12:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130299">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/alonews/130299" target="_blank">📅 12:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130298">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
طبس گرم‌ترین نقطهٔ جهان شد
🔴
براساس داده‌های منتشرشده از سامانه Relay Weather، ایستگاه هواشناسی طبس با ثبت دمای ۴۶.۸ درجه سانتی‌گراد در ۲۴ ساعت اخیر، در صدر فهرست گرم‌ترین نقاط جهان قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/alonews/130298" target="_blank">📅 12:32 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130297">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v7xEaNQ8iF6-Iky0unY_ZJ1sk8EMv9k6aSFSCtGN6hH4wp3m3ioOd4hqbIMO-dCMRKDqiqP1h9jm4e9_LuwmXSXWYe4kzmWnRWbiKJeLs_08gFPCpoubewFWlEjYehlKufDF20WpZLieLCoh4scaV0vsKDS0nqG18jRns1bPdwaovYgOwYmoXZhp1akB9Jab9BmyNmm3S3qhfRK7_g0taGted0LXi-rpRQ0J3sY1KenT_RaTofdYnM5C7uzP_ino5fwVLrGMQCg2snzmtWdc09EGxPG-A04m27FRYxCnDoA6W9SuSAqpwdK0Z_CnWOzxapG1UiTGnOd97kqMF_lbKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
آزاده مختاری، خبرنگار: سال گذشته بانک مرکزی رکورد ۱۵ ساله چاپ پول را شکست
🔴
پ.ن: چاپ پول، یکی از اصلی‌ترین دلایل تورم در حالی به اوج خود رسیده که کشور ما در ماه‌های ابتدایی سال گرفتار جنگ و محاصره دریایی هم بوده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 32.6K · <a href="https://t.me/alonews/130297" target="_blank">📅 12:21 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130296">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
عراق شایعه خروج احتمالی از اوپک را تکذیب کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/alonews/130296" target="_blank">📅 12:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130295">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=cfYWZJkD8FbkhhYy059n54vL9tTBXer_HDygguUf2i2PmYcb7CAt9cJ9kMNr-2hNq6tzisjw7RPbVhpZtqOACYSM_2k72tgPintTpsNMIkjSBfjE1sQy7vuUSPZIqkIzlmJpIjEwCnTbGfC14E4CXB452uX3FKu6Bgq1x6gUJBXFvziw3Z2NopCDqHz9ac8CJ4jej_IAEzOjp2LbxY8SOkb4oJnWdrBgoVHbaJexqfWCAHoMVXu0-iygEXE-xkK90euR0fPx9H34bxwGLKltD46zyzHz1e-Esiv9MWWXy8SoFQKo6ovdMaqw2shdz5ZM6G8ggHezo5HzlQ5VIknnbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb2e1ef960.mp4?token=cfYWZJkD8FbkhhYy059n54vL9tTBXer_HDygguUf2i2PmYcb7CAt9cJ9kMNr-2hNq6tzisjw7RPbVhpZtqOACYSM_2k72tgPintTpsNMIkjSBfjE1sQy7vuUSPZIqkIzlmJpIjEwCnTbGfC14E4CXB452uX3FKu6Bgq1x6gUJBXFvziw3Z2NopCDqHz9ac8CJ4jej_IAEzOjp2LbxY8SOkb4oJnWdrBgoVHbaJexqfWCAHoMVXu0-iygEXE-xkK90euR0fPx9H34bxwGLKltD46zyzHz1e-Esiv9MWWXy8SoFQKo6ovdMaqw2shdz5ZM6G8ggHezo5HzlQ5VIknnbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یاسر ، جبرائیلی: اگه قراره با آمریکا ببندیم؛ ظریف رو ببریم
🔴
یه بچه و بساز بفروش و پاساژدار رو به مذاکرات فرستاده‌ایم!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/130295" target="_blank">📅 11:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130294">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kwBzEEoureiuH-6_mopzjrab1fLofRc9tTOIbPMR4Ssi6oogIRa14xbLWnhRkJCrJ9I0BlzE9juM1_LBPbg8pWKtGWRKXTafTkK4D9yeGiMdYPVctdLGCw6A0zqO5fTT7bstMajPlGN4ZWFHm0lSNKg7EtOLhVKRJjx5l75bW-UaL33Z88-qvLQfU1neIJunkLd5Exdl0BmqAnkbkAMk5jtr05iZMfrag_3ho93nbGhH9Kjkw4OUpj9H70_cAFRkuEjBaSKU-oSq4EBPZIYt9QIwFsA8MrImin8BSFQQQWpP-T0uerH2izt0d_4P__YlL0XgrP0pGFqu3jJKz2K5iA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عراقچی: امام حسین سیدالشهدا شیعیان بود و امام خامنه‌ای سید و سالار کشته‌شدگان انقلاب اسلامی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38K · <a href="https://t.me/alonews/130294" target="_blank">📅 11:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130293">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s2ZuU0Xt_AvUxVv-9WP-0_fG4V5e76jjhFdB7rT-6FIWFXBurY-2yQjfNBAa-GuCzSFb8-dD2fp4alzxIvnJq-1wTX-i8ac7j3l7_bGHKGJDdJU-WmQqGWtn7S0cnOm7k8Kl0kJ_aIODWS-kj4hJh3Dbb8qNnXiE2P02ASvZpsS49ofov4psDVe42uw0PqIVG2Vb2kBIq0M1lXxX-Wk3RuCYV9o2SOh9zQn0WYMiiG2iGZCq1Ug2T-RxAPeASAB4jbn6NIWRQXfo-QUhPUIHncawM9yLGCRltmN9F7J4jM06jUx7w4gjrAtLX5i_mJF_ZXokMFTvY0toq4lPDAqDaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
۵ زلزله بزرگ در نقاط مختلف جهان طی ۳۶ ساعت گذشته
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39K · <a href="https://t.me/alonews/130293" target="_blank">📅 11:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130292">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">👈
وزارت امور خارجه آمریکا اعلام کرد مذاکرات غیرمستقیم میان لبنان و اسرائیل که قرار بود روز گذشته در دور پنجم خود پایان یابد، برای چهارمین روز طی روز جمعه تمدید شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40K · <a href="https://t.me/alonews/130292" target="_blank">📅 11:25 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130291">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
استارلینک به زلزله‌زدگان ونزوئلا یک ماه اینترنت ماهواره‌ای رایگان ارائه می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41K · <a href="https://t.me/alonews/130291" target="_blank">📅 11:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130290">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
بلومبرگ، با استناد به داده‌های ردیابی کشتی‌ها: ترافیک کشتیرانی در تنگه هرمز روز جمعه در هر ۲ جهت ادامه یافت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/alonews/130290" target="_blank">📅 11:08 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130289">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
مذاکرات لبنان و اسرائیل در واشنگتن باز هم تمدید شد
🔴
این مذاکرات که پنجمین دور گفت‌وگوهای مستقیم لبنان و اسرائیل در آمریکا است، قرار بود روز پنج‌شنبه در سومین روز خود به پایان برسد، اما اختلافات همچنان باقی است؛ به خصوص در خصوص نحوه عقب‌نشینی ارتش اشغالگر از جنوب لبنان که تل‌آویو همچنان بر ادامه اشغال این منطقه اصرار دارد.
🔴
هیئت‌های مذاکره‌کننده لبنان و اسرائیل امروز (جمعه) نیز نشست‌های خود را از سر خواهند گرفت تا به ادعای این مقام آمریکایی به توافق دست یابند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/130289" target="_blank">📅 10:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130288">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
قرارگاه مرکزی خاتم‌: تحرکات و حضور هواپیماهای نظامی ارتش تروریستی رژیم صهیونیستی در آسمان برخی کشورهای همسایه به سمت ایران، اقدامی خطرناک و تهدید علیه جمهوری اسلامی ایران می‌دانیم.
🔴
اعلام می‌داریم چنانچه آمریکا قادر به مهار و کنترل رژیم صهیونیستی نباشد، جمهوری اسلامی ایران هرگونه تهدیدی را علیه خود تحمل نخواهد کرد و پاسخ به این اقدامات خطرناک را حق خود می‌داند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.8K · <a href="https://t.me/alonews/130288" target="_blank">📅 10:41 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130287">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fCnUy9mBc9JSMj6kWLHzxhQO8oatGBjOlz9qeEABchDE1qyKNOvKFgF84sdgi_1B5nU0HIIB1g9Guptfk0jc4nZdOPcKZnRg6-ZLeG5RwF_bSXqFpyy0fs9XjEmkGkzl4ApCSW-ptbiC1aIKWyKtzcrgST7-uoK-YurK2ghnN4fhyIdVLAd4SIUgBXEss3w0cL5l8p51fP4-o6wo4m_S520ljr9Fpbggh5yuynlt7LVxxs6Vi2l6_dwkYCp0R2YfpXdp5lteaGUA9Sik4l1Pe8nt-WIqr7e_WckJaI7OkQPRDThpOqnInhuNlM4M8JdmIl5lWrxrGO74-CrwxEXV7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نبویان پیداش شد: مذاکره‌کنندگان برای هفته بعد قرار مذاکره گذاشتند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130287" target="_blank">📅 10:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130283">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k_WvBToNU_JDRzQKtpcnnLj9SZS3VH8qyxRk9m9s5CrTel8z5Ze9L6EU9ZBl3tMRUaDb4UW1DYqZmEy1j3XawsXs_Ysp3rGH5QoGFTd4kCSsiGP-Ry-2CLX7sWlNHwarDh0IS3b6NiW5Jc-7taGJHxq0IjTIkdV418pXcxQao-NpxjuKKwWPmfglpRAfFGC2Ev0G0Du_sEBMfbtht8f9p2c89BEAW-OZsop7a2-W26Kp9T4mII46RC4Gqy6_3Qiy0JlRQXoj0IvCIExV22ZAcDeCxX-pAtJ_QI8jJKBT2Zu2PpqGVUJBpInEmGzIdKZDHv3skcr5Gzja1kvs1I96EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BAGzTg_QFJGzmHVr8qdpzDlG0c6vDItGL-4UnJDxInbenwldQ5nBKPANlOOs3VTD4N_WK_uNouVjEmurrXvd6ScA2-jrwHBh0IAryk4d4Fg30n7yrlrSMnHeq5ViXI0EeldYLtoq8CjnzQmRFi1W6t8sQ-2PJ5YyhKfDEjFHYBV9RmTkIZsmetYO2qzJUHwY8aVWt58pNw82_DeG4NlBypLg1NlQQBA-dRPXET31X09sIo-PQxH7m3-d3X-RKNSiaJjKAyhpw7XqzAOuDCEObmh5HgV1m07p4LclI9RBZS1iQSxffHd5lEqx_fr8XG24oLzt5xyr-JsmDFDrANgfeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VIH7q7aJ6vDFz62r6AszHhWa8aQNUAlNcV-hi5ojCgDVGG1hpiOFwOlLd2qvziu6RxuhMSwmeBcCivAhlShLGLZzeE-ujNFTzKPByTrfvsho7yDY8lYYBkR9Cs-IzafXk7FjbQJVPpagrugk7L07cwvLYNjgCIhE0Y0gNR8HErsnV5hYZsQXHRBdELP3OMt2z5IIwGu2jP3XPYrPUPxDN-XVfcL3VeH-IzAby9Pw1gCKmrREFPZP3glj3bLshXz79kTToleRdoDcb_AS2D2wmtFYKoWNAnA_34i4wiLk-ln81VwhjSx3wPQzhZjCUh_FiMBFsMIbA-RnsuF5IV8JuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nTd8J1TbHTgcdSBdeYR8W2i577nF2tTW572eozLM1YIQGyGX8h_Gn-t_-Ugi07I-t7lKWpqlR7uQ2n-6C9xBOU1Q7-F0oGs0oH-2XSYmlLsQE0HFVILgCPG3RmaQQ2m_87LwlEnhNbHhFHYqUxDcgXe3kSwGa2AYqIa8ihBiPUJMKt1pkCnqsqc4ouVqzoRqsZ40IzymsyyMnclCnW_orLIBVTRHdcaOtvSAxLTsk_KBrRJis_MG9ylkoGNOTCuzRFFYTrul61AxRCv5LeSJPmCMwzYUnre24EBXjwZ5sp-vUmZFIeTgiuajuMY6visKlZBORzlwyJ3YbR7jVrP3Ug.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
کیم جونگ اون، رهبر کره شمالی، بر آزمایش‌های جدید پرتابگرهای چندگانه موشک، کلاهک‌های موشک بالستیک تاکتیکی و سامانه‌های توپخانه‌ای با برد افزایش‌یافته نظارت کرد و بر لزوم تقویت قابلیت‌های تهاجمی «مرگبار و مخرب» کره شمالی علیه دشمنانش تأکید کرد.
این آزمایش‌ها شامل یک پرتابگر چندگانه ۲۴ لوله‌ای ۲۴۰ میلی‌متری ارتقا یافته با سیستم هدایت دقیق خودکار و برد تا ۹۰ کیلومتر، کلاهک‌های ویژه ماموریت برای موشک‌های بالستیک تاکتیکی طراحی شده برای وارد کردن «خسارت مهلک» به فرودگاه‌ها، بنادر و زیرساخت‌های برق و گلوله‌های با برد افزایش‌یافته ۶۵ کیلومتری برای یک هویتزر خودکششی ۱۵۵ میلی‌متری بود.
کیم گفت که این آزمایش‌ها پیشرفت در چارچوب طرح نوسازی نظامی پنج ساله کره شمالی را نشان می‌دهد و «تغییری در وضعیت آتش در مرز جنوبی» ایجاد خواهد کرد.
او افزود که سیاست دفاع از خود پیونگ یانگ نه تنها با هدف تقویت توان دفاعی، بلکه با هدف ارتقای «وضعیت تهاجمی مرگبار و مخرب» آن نیز هست، به طوری که «هیچ دشمنی جرات رویارویی» با این کشور را نداشته باشد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130283" target="_blank">📅 10:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130282">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
رادیوی ارتش اسرائیل به نقل از سفیرش در سازمان ملل گزارش داد که طرف لبنانی اظهاراتی قاطعانه مطرح کرده
🔴
وی افزود: «هنوز به مرحله صدور بیانیه نرسیده‌ایم، اما درباره مسائل اساسی گفت‌وگوهایی در جریان است.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/130282" target="_blank">📅 10:15 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130279">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhkjUoeThrDVSfNNDyYV8aQExNq309PmHPTRpWaQUexS1Y0GAdEV9nxjJSko73_ck1JQenXW4Fzi-drEZistqrYXcSEBo9xkqVhnZT4tOEfYE9yCDm4W4bV-y-QOibpPvukcxFkINdg9mxQUCI5m6iSap76tkDd9iUy9TiIkcqibchJAdty9hw9xQyyZlPwFMGkUdS1nGSpLKhxiY0wIAKlDHFLm2pmfo1aWxjt4XaVVIvuYA227eQLDeLrd4gTEq0CI3uM3pODfdB4l_w1u4jzvkzZdgDyXiCeB3DJ0LSALfF7LMzWVEaklbxiv3VGMNXWP5t7i_SMZm2MKH6pp2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/joSLo7p7cDQs-nCD2r5qiDUiRM0CnPXGLXtwJf04bICLjct0R1wwq8vzRe2JgizjOxeCR9AmU1DMfShVw0evytY2y6o7MKV-SqeZ9zYE8F5MWg3tfPIzcZJrwapxTbkKQ9-NFTSV3FZvrl9EJcRNxymo43n9f2ubxo0Uy9zcE5rDEgliQjh_X6q1gFbZvjeLtadvhG7NBFCvX45HP3oIJXraW3vNorB0A4Cd6ZUL0Iio1wB-EbmKIdG4QLZTbUxMO01HGB0HesDY8MCa6rb5QICI5_QJjDXzlZ_We_mHDAiFT41L09pOUxEgn6kXY0m3kIjH5oKDgQpACnt0P6Xv1w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=HRgt9Dpe2AgI22r8NzMC4GIQYxfTwdXwVArspbVM_uC5RYvK4lHghUjZLtpxi3J__bmYORV_bKxZw5F06nRtg9tVXMtfzoaVTayDavC65h3x6ziaONpBWdhV3oQIYKnTAdSTJ62D7BLY2aMKFFWyHp7TPBSnAmopYLaG52D_D4kT8Eapblv7JNwJfejV9JiDQ-v8tkVK-JWLrzdJmz4RkONCcI3QzYdbZ1uZO3ISgRtTomaHc4OX4mYbUQm-7peIwfl556S5dDi6TU-KoNo2tmkVb3e4Kl55Co9DiOtQDW9NPHuH2qoeSRhWxBZZ8WXFV_kzlaG-W84gAY90Sx-A2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52bc2eaf0b.mp4?token=HRgt9Dpe2AgI22r8NzMC4GIQYxfTwdXwVArspbVM_uC5RYvK4lHghUjZLtpxi3J__bmYORV_bKxZw5F06nRtg9tVXMtfzoaVTayDavC65h3x6ziaONpBWdhV3oQIYKnTAdSTJ62D7BLY2aMKFFWyHp7TPBSnAmopYLaG52D_D4kT8Eapblv7JNwJfejV9JiDQ-v8tkVK-JWLrzdJmz4RkONCcI3QzYdbZ1uZO3ISgRtTomaHc4OX4mYbUQm-7peIwfl556S5dDi6TU-KoNo2tmkVb3e4Kl55Co9DiOtQDW9NPHuH2qoeSRhWxBZZ8WXFV_kzlaG-W84gAY90Sx-A2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
یک حمله هوایی اسرائیلی صبح زود امروز به ناحیه النبطیه الفوقا در جنوب لبنان هدف قرار گرفت.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130279" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130278">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
وال استریت ژورنال مدعی شد:
حمله ایران به کشتی باری در سواحل عمان، آزمایش توافق ترامپ برای بازگشایی تنگه هرمز بوده است.
🔴
به گفته دو مقام ارشد آمریکایی، سپاه پاسداران انقلاب اسلامی ایران روز پنجشنبه در تنگه هرمز به یک کشتی باری با پرچم سنگاپور حمله کرد و توافق امضا شده هفته گذشته بین ایالات متحده و ایران برای پایان دادن به درگیری و بازگشایی این خط حیاتی کشتیرانی را آزمایش کرد.
🔴
این حمله تنها ساعتی پس از هشدار ایران به کشتی‌ها مبنی بر عدم استفاده از مسیرهای تأییدنشده از سوی این کشور انجام شد.پس از حمله به کشتی سنگاپوری که از مسیر تعیین شده از سوی عمان عبور می کرد، چهار نفتکش دیگر که در این مسیر حرکت می کردند، بازگشتند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130278" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130277">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-h04qqz9ZlVEQuKCkmgeStwj_P8ro4MzBLIZItMoSVZ2qzN5p3Kb2vlx0NZ0gGi3xxdi6gEWI32URmPQL47I8N-_FJ0yOOvVdG0JvOt6yVPTNtP9xqGlQbekc6EaeCND21GsG-8k4HcxgTqycO7VtXb2M0V1AknEATZo7dzVFjoK5g0dEQ_EqWeWw-Tzrv4-dggR2LXwm8oigXK5CsCM8b-K1shBQ85BUrsfG0c97ocF7y5qw-R5L4hznvjmnw1lUyGWlsAr1CfBfIbaCqSmrq9e0Q-M1tBaMFmRtZUxMsAzTbEBFrG3j4GEKCrkz3EZNrrykEq4SanzVCqHvQvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز ۴ زمین لرزه مرز بین عراق و ایران رو لرزوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130277" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130276">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
بهای نفت برنت با کاهش ۱.۷۴ درصدی به ۷۴.۱۹ دلار و نفت خام وست‌تگزاس اینترمدیت (WTI) با افت ۱.۹۶ درصدی به ۷۰.۵۱ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130276" target="_blank">📅 09:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130275">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6Q_ygCcQRUGPtPxxqrPo8bNctj7kPeewdj3nqDlGcb63ajarhMBW_7nE0iG73ABXt8ziRLnzYQ1cyomfNr24ITWpy1uoVQbelGkAJPtJynSSxuDDZM_4iwAV4ppAdyK59qe6U9c1I5zb2AAE8APbq10EE164zA7tHb1P0d327BpXh7owJIVj6WdE5OYBe3CRVVt5C-RkJSG468UF6IZS-5CEQazWivDaLt3wbnjLc_eTPcB5DFnoy-VGwizD_kJyLVJrUtqke4AWTkazS2fRHARPHSS_G1lfiUWGZ4HWpd3zz0XfCffH-jRJ4HeGRyEE_OtM_Z7B5mqPNjB1xAHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.1K · <a href="https://t.me/alonews/130275" target="_blank">📅 09:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130274">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
نخستین پرواز دیروز پنج‌شنبه ۵ تیر از مبدأ تهران در ساعت ۸:۰۵ صبح در فرودگاه بین‌المللی کیش به زمین نشست و ورود گردشگران به جزیره به‌صورت رسمی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.9K · <a href="https://t.me/alonews/130274" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130273">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ola-frWl6P6tXT6TunJ-XCpS5MHEBDfVnHALSZYkEYNdHi2jW3gIXdfMxVCFIES4QaVK8Ehin7bq2vv6k7eavKBb-Oi6R1vws6lybfhx8JSNbyfPs037vTrvGKE-N5wSCuz-7GwJzXTV6i3mq7xg1vDGin4hPXNuphyHHPG8oH9fRHys3cncH-gaVBMKIyTOTXESUt2D-SWpcqz8IfpX5thJbs5rMr-1tlQzS5KgfYCnZa8XS3nQt18IEwMRtPO6O5AKmjWKW4o8eViklGst0Mf1YbXgIHofEmeIiILC21jRM5Mbw9qZcaXMpzznrWgGwvgBof-FSdpCYoT4tpPLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید اسرائیل به نبطیه/ در ساعات اخیر چندین حمله به جنوب لبنان ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/alonews/130273" target="_blank">📅 09:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130272">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: به هیچ وجه قصد خروج از لبنان را نداریم، حتی اگر ترامپ درخواست کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 39.5K · <a href="https://t.me/alonews/130272" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130271">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
افزایش کشته‌های زلزله ونزوئلا به ۲۳۵ نفر
🔴
سازمان زمین‌شناسی ایالات متحده:
فاجعه احتمالا گسترده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.4K · <a href="https://t.me/alonews/130271" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130270">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=ESQFGLHm1P9oe6fTHc1dT7Ctz8IHb2H9Q9YH5Z0O-LA2To_n-c256zQrRS3qXUbmVDnnBhe04KoaewWzq2fnvP16Gd158S2Pqth6wcXQotA-2xMkYGoXfk3-T_wee8V7GXw3Wpr-aOa9H9p1IuSiRBdhFMmqgDHMBfmfTIYi7QCelgRhP3QkgTIBR5N1MWWWK4kdQZoiche8LnlAnkv1CRaYas6Q7fmwbstS5tzN-ADibLsk_6ZjzH4LoxZF6NqwUdkfYie1JQ9efOL7yqTUDMUTIVTNJR1NrcdQBi79grENN_jAsYAOxAUMLwgHq_-BmCHDukGdcDehqVK-BHqV3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bf6157f55c.mp4?token=ESQFGLHm1P9oe6fTHc1dT7Ctz8IHb2H9Q9YH5Z0O-LA2To_n-c256zQrRS3qXUbmVDnnBhe04KoaewWzq2fnvP16Gd158S2Pqth6wcXQotA-2xMkYGoXfk3-T_wee8V7GXw3Wpr-aOa9H9p1IuSiRBdhFMmqgDHMBfmfTIYi7QCelgRhP3QkgTIBR5N1MWWWK4kdQZoiche8LnlAnkv1CRaYas6Q7fmwbstS5tzN-ADibLsk_6ZjzH4LoxZF6NqwUdkfYie1JQ9efOL7yqTUDMUTIVTNJR1NrcdQBi79grENN_jAsYAOxAUMLwgHq_-BmCHDukGdcDehqVK-BHqV3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از زلزله ۷ ریشتری ژاپن، امروز صبح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/130270" target="_blank">📅 09:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130269">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
استیون میلر، معاون رئیس کارکنان کاخ سفید: ایالات متحده در مسیر بستن کامل پرونده پناهندگی قرار دارد و پذیرش تمامی اتباع خارجی را که به دنبال یافتن پناهگاهی در آمریکا هستند، به‌طور کامل متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 41.6K · <a href="https://t.me/alonews/130269" target="_blank">📅 09:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130268">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=kL7IXN2vVTbL0rnZyJ68YAt09-5mZ8FIJNdEAjlll03mowEWhZjdyDnNxbIfLqPfnlCR_8h_AnegKRJuL3lfcMaQMjY5sWuWet6MzKjDgpsgCSS6E_3kBsApwudsqyt5tjRvWMSw_vryDhX4_iu07x8GluyvhR0BoBOsR8rHbmKoLOAHQZuNyUi8ClI4MJOy6D7gXhu2l2RT0OMwMqKPHlEU8YSjA0L93r_gcBy1Dwr4WfPqaXjy6jLoTIn12MWnLXTIxnEdEkh4UZee1urh9WV4ZinCNj8wjlg1-w4guKDU4DZdHRnZR09xd1f9nWoPsIy1b6vAiGpnka0EEwbX1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4bc8bdc23.mp4?token=kL7IXN2vVTbL0rnZyJ68YAt09-5mZ8FIJNdEAjlll03mowEWhZjdyDnNxbIfLqPfnlCR_8h_AnegKRJuL3lfcMaQMjY5sWuWet6MzKjDgpsgCSS6E_3kBsApwudsqyt5tjRvWMSw_vryDhX4_iu07x8GluyvhR0BoBOsR8rHbmKoLOAHQZuNyUi8ClI4MJOy6D7gXhu2l2RT0OMwMqKPHlEU8YSjA0L93r_gcBy1Dwr4WfPqaXjy6jLoTIn12MWnLXTIxnEdEkh4UZee1urh9WV4ZinCNj8wjlg1-w4guKDU4DZdHRnZR09xd1f9nWoPsIy1b6vAiGpnka0EEwbX1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رئیس‌جمهور ترامپ درباره ونزوئلا: ما ونزوئلا را در کمتر از یک روز تصرف کردیم و نفت در حال جریان است و ما با آن‌ها بسیار خوب کنار می‌آییم.
🔴
ما می‌خواهیم به آن‌ها کمک کنیم — آن‌ها دیشب زلزله‌ای عظیم داشتند که در مورد آن خواندید، مانند یک زلزله عظیم در کاراکاس. ما می‌خواهیم به آن‌ها کمک کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.6K · <a href="https://t.me/alonews/130268" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130267">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گروسی: معتقدیم که مواد هسته‌ای از زمان آخرین بازرسی که در سال ۲۰۲۵ انجام دادیم، منتقل نشده‌اند، اما لازم است این موضوع را به‌طور قطعی راستی‌آزمایی کنیم
🔴
جزئیات فعالیت‌های ما در ایران و ترکیب کمیته هماهنگی ویژه مربوط به روند بازرسی، در جریان مذاکرات مشخص خواهد شد
🔴
آماده‌ایم تا فعالیت‌های فنی خود را در ایران پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/130267" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130266">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
ترامپ: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.8K · <a href="https://t.me/alonews/130266" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130265">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F3yj-3AEZVXgu00c376vMOIaK5zsX161TXn_6509XGswILF8cu0wGjL83STm7tJ0cISG8d1TfNyf-CY6q1mC398U5SnheXZTwdPi1vXb2DO_NteVN0Sh_VHRNlF6R_BBDGUYC4OK-yZvENujyur1Sr5A0R4YeaPqkiT67YWULC8MJHnVUGMliD9fFlxOHTm3d6Z3uanxQnrjBPfemjDaEf4IDI2Ehxb8Gh7nXYbvG-dNT9jbgLkh29jWf-xISytj6cadmKVL2UxcE_PXrr0xbVMWnX-R9jVHiabtcywkFmYtATEgAl8Fp_TIWxbL6s2OO_5Pyq1PWMlsy-fyaPQVkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
فیفا اعلام کرد
تماشاگران می‌توانند در دیدار تیم‌های ملی ایران و مصر در مرحله گروهی جام جهانی ۲۰۲۶ که روز جمعه پنجم تیرماه در سیاتل برگزار می‌شود، پرچم‌های رنگین‌کمان را به ورزشگاه وارد کنند.
به گزارش رویترز، این مسابقه هم‌زمان با «هفته افتخار» (Pride Week) برگزار می‌شود و کمیته محلی برگزاری جام جهانی در سیاتل آن را «بازی افتخار» (Pride Match) نام‌گذاری کرده است. ایران و مصر پس از قرعه‌کشی مسابقات با این عنوان مخالفت کرده بودند همجنس‌گرایی در هر دو کشور جرم‌انگاری شده و قوانین کیفری برای آن وجود دارد.
فیفا در بیانیه‌ای تاکید کرد جام جهانی رویدادی فراگیر است و پرچم‌های رنگین‌کمان و دیگر نمادهای مرتبط با گرایش جنسی و هویت جنسیتی، به‌عنوان نمادهای حقوق بشر، اجازه ورود به ورزشگاه را دارند.
پیش‌تر، فدراسیون فوتبال ایران از فیفا خواسته بود در دیدار ایران و مصر که از سوی کمیته محلی جام جهانی در سیاتل با عنوان «بازی افتخار» (Pride Match) معرفی شده است، از برگزاری هرگونه مراسم یا فعالیت تبلیغاتی مرتبط با گرایش جنسی و هویت جنسیتی جلوگیری کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/alonews/130265" target="_blank">📅 08:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130264">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e24211a974.mp4?token=qXfU5Bg_EitKAGLQB9OVVOLqPXe9mZVpwH7H-7qKFT2hw0IivTXTIZA_RyWOSIRlZkE9vpACpII1T1hAIdccYWH15iV32ydCWTwpHsZ1zxFVVKvCRXjoLlFawrpQp8nZbDqRQ0SgxHilVPT3KESs0JOF13Xkje0K_jYymXW9oC-sd-sQqDRWAd9m_OMtFRP2SQeVeXTQJxy46gOlQdbcIJZVlI0cet-7szlyIrRSunC6EQdY5vQI-FsCXyiHyUA2iLa7BKQOFu-mdDDq0phvAwBxMjMzSey54NJ81IQe6pkx8Z4HVraW-yrTm4Dg6bhYeQlGCzMtxJb_NX8TEzxH1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e24211a974.mp4?token=qXfU5Bg_EitKAGLQB9OVVOLqPXe9mZVpwH7H-7qKFT2hw0IivTXTIZA_RyWOSIRlZkE9vpACpII1T1hAIdccYWH15iV32ydCWTwpHsZ1zxFVVKvCRXjoLlFawrpQp8nZbDqRQ0SgxHilVPT3KESs0JOF13Xkje0K_jYymXW9oC-sd-sQqDRWAd9m_OMtFRP2SQeVeXTQJxy46gOlQdbcIJZVlI0cet-7szlyIrRSunC6EQdY5vQI-FsCXyiHyUA2iLa7BKQOFu-mdDDq0phvAwBxMjMzSey54NJ81IQe6pkx8Z4HVraW-yrTm4Dg6bhYeQlGCzMtxJb_NX8TEzxH1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
رجزخوانی وحید جلیلی برای ترامپ
#گنده_گوز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/alonews/130264" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130263">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">👈
ترامپ: باید علیه ایران اقدام میکردیم چون داشتن سلاح هستهای به معنای نابودی اسرائیل و خاورمیانه و به خطر انداختن جهان است‌‌
🔴
اگر ایران سلاح هستهای داشت ، ظرف یک ساعت اول از آن استفاده میکرد و ما هرگز اجازه نخواهیم داد که این اتفاق بیفتد‌‌
🔴
ایران سلاح هسته ای نخواهد داشت و به آن موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/130263" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130262">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
ترامپ: ایران خیلی می خواهد با ما توافق کند و فکر می کنم احتمالا با آنها توافق خواهیم کرد‌‌
🔴
ضربه بسیار سنگینی به ایران زدیم و اکنون از موضع قدرت مطلق با آنها مذاکره میکنیم‌‌
🔴
قیمت نفت به شدت و به طور قابل توجهی در حال کاهش است و کاهش قیمت نفت با کاهش قیمت تمام محصولات دیگر همراه است‌‌
🔴
تنگه هرمز باز است و دیروز شاهد خروج 19 میلیون بشکه نفت بود که بالاترین رقم در تاریخ آن است‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.5K · <a href="https://t.me/alonews/130262" target="_blank">📅 02:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130261">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: 159 کشتی ایرانی را کاملا غرق کردیم و همه در قعر دریا هستند‌‌
🔴
تنها در یک هفته و نیم ارتش ، فرماندهی ، هواپیما و نیروی دریایی ایران را 100 درصد نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130261" target="_blank">📅 02:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130260">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ترامپ: روند خرید محصولات کشاورزی برای ایران خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
🔴
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130260" target="_blank">📅 02:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130259">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=I2BFPr0NjgIzXdFpUiJWzPAWtALtlA5jTEFVgYALW4UmkKQsaeUKSQFds8ocTbs-sg1MrZrQyeJG5lPn5N1h_DIO64t6vU09pISCQ9CszYsJejsDUX0aenkEcij14aUCbNLbMtgAc_D0bR5pxMzxYvw-umwkdBpRtMu3PxcHDBHfR5a3Ti-tbzK0uTLBKgGXHhULKdJqy26i1s3nfCbat8EspSSkX6BlnSW_qf7Y0qKxpgzhPTl_o9xFKSn3FcaBeMsCWW-hu_QGkxxNnMQjtEbBg3MPoll5L9LJZs9yY2pevoyxjI-3J7rFraRVhiYHANUiMyzlAIysQPfUY-YuDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/566bfa2ebb.mp4?token=I2BFPr0NjgIzXdFpUiJWzPAWtALtlA5jTEFVgYALW4UmkKQsaeUKSQFds8ocTbs-sg1MrZrQyeJG5lPn5N1h_DIO64t6vU09pISCQ9CszYsJejsDUX0aenkEcij14aUCbNLbMtgAc_D0bR5pxMzxYvw-umwkdBpRtMu3PxcHDBHfR5a3Ti-tbzK0uTLBKgGXHhULKdJqy26i1s3nfCbat8EspSSkX6BlnSW_qf7Y0qKxpgzhPTl_o9xFKSn3FcaBeMsCWW-hu_QGkxxNnMQjtEbBg3MPoll5L9LJZs9yY2pevoyxjI-3J7rFraRVhiYHANUiMyzlAIysQPfUY-YuDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
قالیباف امشب با روسری در هیئت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130259" target="_blank">📅 02:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130258">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
جی‌دی ونس در مورد جمهوری اسلامی ایران:
آن‌ها دائماً سعی دارند مأموریتی که دونالد ترامپ برای ما تعیین کرده است را تغییر دهند.
او در ابتدا چه گفت؟ «من می‌خواهم ارتش متعارف آن‌ها را نابود کنم. من می‌خواهم توانایی آن‌ها برای اعمال قدرت را از بین ببرم. و من می‌خواهم تضمین کنم که هرگز سلاح هسته‌ای نداشته باشند.»
آنچه دیده‌ام این است که برخی افراد سعی می‌کنند بگویند: «خب، این عالی است، اما شما باید هدف متفاوتی داشته باشید.»
به نظر من دلیل موفقیت رئیس‌جمهور این است که او از تسلیم شدن در برابر آن تمایل خودداری می‌کند.
او می‌گوید: «ما کاری را که قصد انجامش را داشتیم انجام دادیم. ما اهرم‌های دیپلماتیک، اقتصادی و نظامی باورنکردنی ایجاد کردیم. بیایید از این اهرم‌ها برای کسب پیروزی بزرگ‌تری برای مردم آمریکا استفاده کنیم.»
این همان چیزی است که او از ما خواسته است انجام دهیم. هنوز تمام نشده، اما تا اینجا همه چیز خوب پیش رفته است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.2K · <a href="https://t.me/alonews/130258" target="_blank">📅 01:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130255">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Cwg6itHuqv7GZd-MQSCSx7Z_RMemwONukAaOP_r0X6i2Mtg8ejpog57Ma6EvOjoik08ntWBJzDStvP06e3ucai6hXImQV7pdPvIUpE3PoGhxye6Br_xm1RdAAokYhdRjujdSKNudW6bEMBzYzFQ2Z8-afLX6CyaKm37vuKm0gqndw0U3Cp5p9fnd2EgJ71N0hFCtB0_UsIxlQKSEOxfZWlbzwcnr1eBrqYUCAxwJ0ceYnqNyM23YLsZkpcSeQPKavjlEuDXAZdSpMsA1cCTK-tR-M4Pu8-Q_6Yzwe8MvOEkCQwhbrlhYFrVwEUb0zLEPa3994zZBNyaOCmb6tAG_rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vCeuFOkqbRSSf5C25so8HwVOMnQCop9JPiYcgo8tmFnP0TGJINXCa5bRnzQ0zzg2XkfpUi4LZjt0yeHhYuP_BcGc6yVqjsCvjMGd6L3rpMHQpcWta85UbbPyjUEg1TAqdam3QSQMU9kLYtsWqWA6Lq6XrFao1Bid7msje3YjE0GvV_wS_Cp9ECm-imlOtYyKN6pIHWU8vdAtmyG8cX6gbmStIzp5OIoj_GMaqTBjqUh8O8BLIEAn_3VrYon8smLerkUo_nIStaK7wkeNdZrknLRlk4KgaTnacOQkQTg5-xuOvtsTnDrE92Gdb0A5_LBNoBkJL7WdMT985wXfSYsNhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oHN-oN3NBekaXMJX6blvFXR1IDsAZggfTeeMV_X5ay9l2B7ELC1a_BMK_RJysSyrNFEn2aYRozQsQ34hOy8WzlgRqSs77HLdcVGik_XvRSslr_IDjjJo1GzUpx_jw-bIlhSg5HejZJBwheDh3E5nbPmMQfNz3auD5FwolwtJ4VJ_6pAwK4ZZwXOKhRyvyaGhXd2-SOHdzLWeLiEtsS2uf_wImSdb5fz--TvccFyhxPRiTzgfmBC0SrkZjwUvylqI3vLzlObFZcZ0xqdLef5eh-kLnd5n39zSbBwvfRYHTyf6okyN8_raGl380IX7DKhX7dIYuBBXzvilfkRPvcy-Ag.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
شهباز شریف هم نتونست مانع بیل زدن پایان ناپذیر پزشکیان برای کاشتن درخت تو اسلام آباد بشه
🔴
شهباز هی میگه نمادین هست ولش کن اما مسعود ول نمیکنه
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/130255" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130254">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=aqqBZN85UXBxAAknzNWfGrQrL0MfDBaVheNBKH2jXwvVcT8CJVsJAZbppDJGnU6kFrSd2yFkdA2t45OahRi9EN2c8blS_QVAhBxu--6IzKtLzVP__aBBM9uKS-Gp2Rnp0KLWCuEI17k-Z-huBzooDJ6YU-9ODajWXokcrfraEh71HZ5K0N_1hRKo9l4ttZuyEylJ2RqQ6SLImGsSXqqWcpt0QIicxhVE2_hc_lm75kn_xt4z_ev8vixcEWXPwcXsKTmGu6DljWF74rTZo4IUANtWowO9rf69poAQal9j5W0JZHfYIMiYNnjdOtsZbV3t-YQq17ZBE8Xm8HkwmKPSiQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6e31799d4.mp4?token=aqqBZN85UXBxAAknzNWfGrQrL0MfDBaVheNBKH2jXwvVcT8CJVsJAZbppDJGnU6kFrSd2yFkdA2t45OahRi9EN2c8blS_QVAhBxu--6IzKtLzVP__aBBM9uKS-Gp2Rnp0KLWCuEI17k-Z-huBzooDJ6YU-9ODajWXokcrfraEh71HZ5K0N_1hRKo9l4ttZuyEylJ2RqQ6SLImGsSXqqWcpt0QIicxhVE2_hc_lm75kn_xt4z_ev8vixcEWXPwcXsKTmGu6DljWF74rTZo4IUANtWowO9rf69poAQal9j5W0JZHfYIMiYNnjdOtsZbV3t-YQq17ZBE8Xm8HkwmKPSiQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
حمله یک مداح دوزاری دیگر به پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.1K · <a href="https://t.me/alonews/130254" target="_blank">📅 00:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130253">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRHYJ7no6L0SZy8NWQnr2uzQawAN083gnxSTyVeS9YNh9IgX8_jJlec7J1f6nvdbRegu0EN307tYHaKicmM2a9oAZHrxJSvVOShpPmygdAookOiPENrU8w6i1En_tpbj-l2U5ANL6Q0B2rQsPwCtn11xvbu0Jx8y8GFOcy3cArlfXCSRaid2Wfg_ZaiYaRljFpeMappDNkUaFK6RNnC2vGpYlJVF8c6kjvH7iG9HGbUnsZFGLhE1Zl-2xG6zL_nd6xdT-OLLhXKuTXqK79NBSQ0QGav9hhYt4N4lrxlho0pO1ea3J3Qntt-zGyXPA0CQnXSbl8ZdSEWJYea5K-rrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما برداشته یه آخوند که تنها رزرومه‌اش افتتاح شلتر(خونه صیغه یابی) هست رو هر شب میاره راجع به مذاکرات نظر کارشناسی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.2K · <a href="https://t.me/alonews/130253" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130252">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=HjzqgqUXCDDmsZ2yw0L67JUghwc6T6C-rqK4gkjW56PDVvGU8xEqK_R4oIWjqoXGj3uCqKRcWFJtdJTMUyHhJxGdRiTN7kQhfIw-GUzHE1ARETJgrXleYN8dIrjI1eJNuWYohpP-7VIj6mp7KmnPmyzLx5M1Rh4f24pIU1K95bAlgo_cB4hMmo3JF5PGAcFu-O3v6hRGo29g8t-DRsv71x6Wp9fI4g70MddEiQiRkddIa1Te5cE2XQ3w8MSZc0Djveshj-S5r8zWnOqF2SeUkhI0EIQuyRycOhg1zXKPozfAu6RFE_H1qGHUWNEss5AJpUT2YwegPfwJu0LmcZBU_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0b6026c629.mp4?token=HjzqgqUXCDDmsZ2yw0L67JUghwc6T6C-rqK4gkjW56PDVvGU8xEqK_R4oIWjqoXGj3uCqKRcWFJtdJTMUyHhJxGdRiTN7kQhfIw-GUzHE1ARETJgrXleYN8dIrjI1eJNuWYohpP-7VIj6mp7KmnPmyzLx5M1Rh4f24pIU1K95bAlgo_cB4hMmo3JF5PGAcFu-O3v6hRGo29g8t-DRsv71x6Wp9fI4g70MddEiQiRkddIa1Te5cE2XQ3w8MSZc0Djveshj-S5r8zWnOqF2SeUkhI0EIQuyRycOhg1zXKPozfAu6RFE_H1qGHUWNEss5AJpUT2YwegPfwJu0LmcZBU_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
فیلمی از رهگیری موشک‌های بالستیک اسکندر روسی بر فراز کیف توسط موشک‌های پاتریوت در جریان حمله دیروز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 66K · <a href="https://t.me/alonews/130252" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130251">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=LkwDvJTqfbRguACz68S6j5YSBpndwYFuagm_Km_ILQwdVrvKn61r0WwRWFMXbHWLHHhInYb0Ru_2mmuyeCOY_RDZWWtfIbvtojfMRYuuwC3zhhJuyyrtsXOWQNvnYMeuaXpARizCx6zW8Fmfx1iFrpaPo-naRP3oHOZ9zUiUhjF9cBGTNNUO21IXkyWhUoRB5M0r0Y8fbwrFxrX6fqunxW-YyJyhze4CIqUFfnOYJPso8iS8c8lUgVqmtom9bBLjlfMSCyxIBMyhVTtCNYml79VMVEdGMwvvOY1456XPc7yA-E7-vJOinSqsYTUd3cMJamP1wVJrdFjKVFMTIst_NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1c21bf1806.mp4?token=LkwDvJTqfbRguACz68S6j5YSBpndwYFuagm_Km_ILQwdVrvKn61r0WwRWFMXbHWLHHhInYb0Ru_2mmuyeCOY_RDZWWtfIbvtojfMRYuuwC3zhhJuyyrtsXOWQNvnYMeuaXpARizCx6zW8Fmfx1iFrpaPo-naRP3oHOZ9zUiUhjF9cBGTNNUO21IXkyWhUoRB5M0r0Y8fbwrFxrX6fqunxW-YyJyhze4CIqUFfnOYJPso8iS8c8lUgVqmtom9bBLjlfMSCyxIBMyhVTtCNYml79VMVEdGMwvvOY1456XPc7yA-E7-vJOinSqsYTUd3cMJamP1wVJrdFjKVFMTIst_NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وحید اشتری: واقعیت اینه شکست خوردیم و تسلیم شدیم و توان انتقام نداریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 68.2K · <a href="https://t.me/alonews/130251" target="_blank">📅 00:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130249">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZG7uyNlbxcuAiiUjBPfoUhIxJBWkuiuaFQIbmUpE11_gsdN-yWNgGMVMhuyOw1SX9BGsbe179N7X15T9h3uS9d9TzlSLvYWnadbuSKXFuiz0PkXFGb4zh7EiJmIe4nC1bsJfw6JzcQ2rorsKEwCKrNig85Bf0TlETkCrCPgtPq9k_-yBaVztYorfWIRG00KQlpUBsgI4j2rDpBwTFuxKBnA4Z7wjMPo2lKdpX2VMchsR3OgultPT9k-Aabw1XNeHpNHEiQau-7IGH5-e0WN4ZQEIcXdkvyrO6ROu2XnF0OD8lgwq-9BZOOSN3ulrJh0nXq3tWGkSjmDabfa89LYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxdwGHd4ed-fUJs8v7v-vJWb1eMnv2k-e6WWJ9QgVRa1N9_Jl5CpuJCTHabvKHhBrU-KqPMDyzO0-orZM-nwKz_ErvJg5e8bNYe55pakTvwYDF-0KLGMVM9nUCYVRLDtmnIrfxS9IpbRC0Jv6EDd4asG3sLR-U6sMHMxdwY3bbAhROH4ON6BRZHSs32uE-nKw7OZibIvc_TUm2Keu8ZYMQ2YoWYTAtIFMaikCP6brQ4XtAj7PmSCytq2icvq94hhwY1BGYLyFBSqqGJ3-PilY3p3lvS-2Dz7wJWZzxMVjcJT1NaXevNr90xLo4m2uEPA89ycOM86Su341cxt274wJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محاکمه شیخ "احمد بدرالدین حسون" روحانی و مفتی سوریه در زمان دولت بشار اسد در دمشق شروع شد. او متهم به حمایت و توجیه سرکوب مخالفان بشار اسد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 65.6K · <a href="https://t.me/alonews/130249" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130248">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
شبکه المنار گزارش داد که توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.7K · <a href="https://t.me/alonews/130248" target="_blank">📅 23:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130246">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDdMI6j1If8GksSbhkYA_QKX6pU3SlZpkTbCfZ0ohLPSBWYZY1X0eYMQWL6LP-A04S7wiraSMBL5U9SlTcCq0JycLMZjoUp-cLlSsPlzAPbPRY4djRNdXOXSwnyAO6tWxsa7bwCp8PC5NgQs5P-IS4P3gdyyMzIaSW19LZnQCpTtr9RXkGcWRA8HEx7dplEtTLHXnLalZqeqxuvTfQsmG3WyJ0E3m1kPyaw9M_2MSX29YdXqNKhY26Zcv-UM4tzdyrh4zk78W3fWuYIhbiAhHzXrw86y7jLRX8Hq5LyAdKQkzfjlDjhtjPgwnyXQLN-meteuObhwnDdYmo1ZWJreTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید گفت برید مذاکره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/alonews/130246" target="_blank">📅 23:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130245">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله رو در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/130245" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130244">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=nx1chjl-p0He4tbapu-JolouaNdnVuQyNArDNvqZ4cW3ORk74fNsAXnMKRPVImGQcXUO4_BDPUxlwY9gUa617MtADiAqtzxL8JpDm1SKnlt6JomCsr3W9oqL6gpbJEMLvhsPXZW2lTTFM5WE7hE5KJPLakmlcV2lAu15dQhKxpPo4Z0-iBKFKUvrgt5Sd-nDcN9YgqyhAznEgYajqWqUaoiFPxamYNw8W0iQH4eFbLScY4XVrsA84W_NXAnRfsPAC-XFo_qWbbwZ4jWFrqcJl43hC4G6olUR0VIoMARCavuuKxZWdWWICvUeGMeHvyJGvP3IP5swQz8vhF-i3wHKQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9e0081f0c6.mp4?token=nx1chjl-p0He4tbapu-JolouaNdnVuQyNArDNvqZ4cW3ORk74fNsAXnMKRPVImGQcXUO4_BDPUxlwY9gUa617MtADiAqtzxL8JpDm1SKnlt6JomCsr3W9oqL6gpbJEMLvhsPXZW2lTTFM5WE7hE5KJPLakmlcV2lAu15dQhKxpPo4Z0-iBKFKUvrgt5Sd-nDcN9YgqyhAznEgYajqWqUaoiFPxamYNw8W0iQH4eFbLScY4XVrsA84W_NXAnRfsPAC-XFo_qWbbwZ4jWFrqcJl43hC4G6olUR0VIoMARCavuuKxZWdWWICvUeGMeHvyJGvP3IP5swQz8vhF-i3wHKQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
روته از ناتو: این بهار، با مهندسان جوان و بااستعداد در شرکت ASELSAN، بزرگ‌ترین شرکت الکترونیک دفاعی ترکیه صحبت کردم.
🔴
آن‌ها انقلاب صنعتی دفاعی ترکیه را هدایت می‌کنند که به نفع هر عضو اتحاد ما خواهد بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130244" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130243">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=BbiarLBOWcpDLDVwlNCvNJNupmrb0RbO5s_fv-BdgPmc3gAud7AKpKir8ZGPBJJxKZ-GNrHNmpAmML1VL9dBvjoQdcEtJBIj9wm9L5ZSnVTfLrRrHIiNSvqiTtC2Jgv6c9BzrQoSaTalvSyQF8Mdd-kcpXhomTRHvm_kZoIC2pXHUQIgedrwYl9KY-TD4cVZjcQ7i20rnM9m4v9I_SKupgujX2Y0KdpvSF_7wlQH8n_MF4QFEFZg2v4hTbNlVMLEh8i8fSz5GCPFnXrCqlCbz1LI8ofgPO5180PBwhu85MdWQn54yjz1cSub6xHAq87VjN2LvasbAMnpi4rrI1s5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49014d9e0b.mp4?token=BbiarLBOWcpDLDVwlNCvNJNupmrb0RbO5s_fv-BdgPmc3gAud7AKpKir8ZGPBJJxKZ-GNrHNmpAmML1VL9dBvjoQdcEtJBIj9wm9L5ZSnVTfLrRrHIiNSvqiTtC2Jgv6c9BzrQoSaTalvSyQF8Mdd-kcpXhomTRHvm_kZoIC2pXHUQIgedrwYl9KY-TD4cVZjcQ7i20rnM9m4v9I_SKupgujX2Y0KdpvSF_7wlQH8n_MF4QFEFZg2v4hTbNlVMLEh8i8fSz5GCPFnXrCqlCbz1LI8ofgPO5180PBwhu85MdWQn54yjz1cSub6xHAq87VjN2LvasbAMnpi4rrI1s5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هزینه تجربه کردن GTA VI در ایران، در اقتصادی ترین حالت ممکن: پلی استیشن 5 اسلیم 1 ترا - 112.000 میلیون تومان
🔴
تلویزیون سام 32 اینچ - 26.300 میلیون تومان
🔴
اکانت آلتیمیت GTAVI ظرفیت سوم - 5.500 میلیون تومان
🔴
جمعا 143.800 میلیون تومان
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130243" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130242">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi6HKd96qkDpVvQD0qAEc_vasXu4R45UCx68j4qG1wGDAKAeIuwDUFG1lW9Vla_pMYVmusfah4F-kpF3Qe5fvQk9lB3pjJw2RqcCukePg6bFiOoJIRCIEooWqO865cHmBYXBiBGddygyeX4KeMgWQ5pL9Zc8MAY4DKSYsSlnW3WADzfIuXN-BVtU-tSGY-GhqLNwBR4LpWHhAbUIYDnVksq4k4VxA0P5ZtcR8SECiKbcdSQSwIEAJP5frXNnBPTfbHgGpslZOoMV6HkGasVyvt_5_EoGyyCLxUmVNeWvserooacSOTlGKedLKm-qyqQUb4_zbWtiQnmfaIR3OTtaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130242" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130241">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FWnJvDkpDgA97j-p-chBRAxZuCnkA5YeOGqiZtngO3Y-YXT9evlZxVaeOHjuWqvLcA992hZhJyCy9EL5TrYzvX7SOIbKWVjVDleqwyxCdy5HHNELQT3cZ2e-TMRhDOxyldFuQLiid9tsWB3bWtz8UyJZg4hnSRoh2DFSkHlREdh4UY0cjzzujGdimv-xP0r8Ze4PRHqGq89kirSlapFJfjN0ZN7b-wDI3esVL1hKjZnd3pZWt7KHwTzuZ8Ras_jh5cJLrO9S12BaZJKUIV3mzQ6QkLgsEjVOGRCArx3VTwbuXjNTMERXoT2yjmr9tmDwkjcjJWI3UqAHMLAfRKC8eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو سالی که برای پزشکیان یک عمر گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.8K · <a href="https://t.me/alonews/130241" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130240">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092b312727.mp4?token=J_aL24Mw1SrzR0yNzegkMHAspz-vtRUVatPJPIcXGFqLx8zpwOwxZ4wM81rxNZdbtX16i_8oBM41WMcoekn0ZM5pXBk0M_anCx60Mc70x0C_WGa1HAl0ILLCxmn9fyEx9NOu2hDJAYnI8IjCJ-eLjpvpBBktszPeJ83rxIwcu3i1d-i4MyYUot4zArP18HgFC1UfRsFddk6WQ_k71wp5FBje7mZV7L_tMO8iSckRXvBZhZYL8qU2fQRVaDCkKDBVIcbYiQL-awO7tkoWCeXPM-ZqJueOUmGNkjtixZ24Nj7al1zAVZBhD0lQrOESVFShZUQKS1Z2DQWlC-oBN8U0LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092b312727.mp4?token=J_aL24Mw1SrzR0yNzegkMHAspz-vtRUVatPJPIcXGFqLx8zpwOwxZ4wM81rxNZdbtX16i_8oBM41WMcoekn0ZM5pXBk0M_anCx60Mc70x0C_WGa1HAl0ILLCxmn9fyEx9NOu2hDJAYnI8IjCJ-eLjpvpBBktszPeJ83rxIwcu3i1d-i4MyYUot4zArP18HgFC1UfRsFddk6WQ_k71wp5FBje7mZV7L_tMO8iSckRXvBZhZYL8qU2fQRVaDCkKDBVIcbYiQL-awO7tkoWCeXPM-ZqJueOUmGNkjtixZ24Nj7al1zAVZBhD0lQrOESVFShZUQKS1Z2DQWlC-oBN8U0LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف در سفر خارجی با هیئت مذاکره‌کننده بدون نقاب حاضر شد اما شب عاشورا در هیئت «ریحانه نبی» با نقاب حضور یافت.
🤔
کجا احساس امنیت دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/130240" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130239">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
چین رسما اینترنت 10G رو راه‌اندازی کرده؛ فناوری جدیدی که سرعت دانلود و آپلود رو چندین برابر می‌کنه و می‌تونه یه فیلم کامل با کیفیت بالا رو تو چند ثانیه دانلود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130239" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130238">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
عراق پس از بحران مالی شدید مرتبط با اختلالات صادرات در تنگه هرمز، هشدار داده که اگر گروه صادرکنندگان نفت سهمیه تولید خود را به طور قابل توجهی افزایش ندهند، ممکن است اوپک را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/130238" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130237">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.8K · <a href="https://t.me/alonews/130237" target="_blank">📅 22:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130236">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cVbi_1z350bVTOJ3gcDdfTkZCqzIsRduTE-EveR1qtt3ChmpM6vzROmyu9CaT7DNxRssqI_aq34PHME47S5uLOkKGCCVAf0JJtOR18Owg8L5yC2MY6EnOCvs5D-n6HRzPRZvLSq-kcKlla1vFXQ8JEtBTB2GjpU_lfeykwye1hvoGISxde8boM38NTfe-Sy-vm1g4IfX89q95VQhWshF3DHUnG-tRyvpBKlHN87aD_FT-9ILk53IwQw4nDCecCweKyahPlD8pSmE2zFjNyVMBPO2j78RDtwH3AZVTMvrtgcTkFZ-AgsOYpnnQUmkgjo09xU7XGqJBNyaRUu4x7Z7lQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.9K · <a href="https://t.me/alonews/130236" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130235">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7v1Pe4HQ3ov-QqyQLNdauqQvJixsFH2AxmPbsBXJRNFaaFIouQ1bHEiu9VbWontUicF_xPWuRILJYi3GvVcwk0mJTrF6d2ukjrxyULXGah--wnt63b8HQRcBjdldcO__4QIswhsnlB9MXu4lgMvc0JCb955UPvOZGJuYs7BVCWOWjDizBKkz2gJJ8_EkYLptohFKRDuAERKqR_pTuoj76ghDrzlO6bggwGX_GZ5TI4Kfy2YoPELTiWA7llD96103R8-JwrKNBBdlEiey6QT82EpnNSPGi69PFen-CJ9o1gQEl1-Sko8uvUsLzLFkMOKb2a2STzOew_F6dGRv5QErQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60K · <a href="https://t.me/alonews/130235" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130234">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">👈
ملونی در مورد ایران: ایتالیا در درگیری با ایران شرکت نکرد.
🔴
در واقع، اگر در درگیری با ایران شرکت کرده بودیم، توضیح دادن ناامیدی مکرر ابراز شده توسط رئیس‌جمهور آمریکا دشوار بود.
🔴
ما با در اختیار گذاشتن پایگاه‌های خود تنها برای فعالیت‌های لجستیکی و فنی و نه برای عملیات‌های رزمی، به تعهدات خود احترام گذاشتیم.
🔴
و زمانی که درخواست‌هایی مطرح شد که فراتر از آن چارچوب بود—و شما این را می‌دانید زیرا به طور گسترده‌ای گزارش شده است—ما مجوز استفاده از تأسیسات خود را صادر نکردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/130234" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130233">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130233" target="_blank">📅 22:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130232">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروی هوایی یک عامل حزب‌الله را که تهدیدی برای نیروهای ما در ارتفاعات علی طاهر در جنوب لبنان بود، از بین برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/130232" target="_blank">📅 22:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130231">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/alonews/130231" target="_blank">📅 22:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130230">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
هم اکنون حمله موشکی گسترده روسیه به پایتخت اوکراین، کیف با استفاده از موشک های سنگین و بارشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130230" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130229">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
نرخ اینترنت مخابرات دو برابر شد !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.2K · <a href="https://t.me/alonews/130229" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130228">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/130228" target="_blank">📅 21:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130227">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: اکنون ایرانی‌ها می‌توانند نفت بفروشند و پول آن را به دلار مستقیما دریافت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.9K · <a href="https://t.me/alonews/130227" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130226">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
احتمال بسته شدن مجدد تنگه هرمز!
🔴
سازمان بین‌المللی دریانوردی از تعلیق طرح عبور از تنگه هرمز تا دریافت اطلاعات بیشتر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.7K · <a href="https://t.me/alonews/130226" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130225">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.7K · <a href="https://t.me/alonews/130225" target="_blank">📅 21:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130224">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=uKJdy4ggJTivh34aUyi7vhllmjrDC98-Hr86pm69d7GO1euCwYiMcuXgYydP44HFy9ck_N2L3kEGZaD4RDgtyYNCzY1iNtB5VGsT8xNKZ8mu0j-1WGOZeS2C0CHn_aLaVUFEDkjv1CGL79FXKwd2r6ptdfUG-rPuclnPdin7KPWdJwAzkIS0FrIAhfCDOdM50d5lhDVLgB1sSyQ-EnGQU0Jev8ij9nmeYPW5Ak7BdeUmDA8YwB25MDzz0qM7wcHn0L1PgCvCJBZsrh42KE-8WkjQXCH5f1A-JzaYo59wVtcXeIw8o8wDtpQZcO_ZQttwDZWYHmYWN1zNDxvihJU-4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=uKJdy4ggJTivh34aUyi7vhllmjrDC98-Hr86pm69d7GO1euCwYiMcuXgYydP44HFy9ck_N2L3kEGZaD4RDgtyYNCzY1iNtB5VGsT8xNKZ8mu0j-1WGOZeS2C0CHn_aLaVUFEDkjv1CGL79FXKwd2r6ptdfUG-rPuclnPdin7KPWdJwAzkIS0FrIAhfCDOdM50d5lhDVLgB1sSyQ-EnGQU0Jev8ij9nmeYPW5Ak7BdeUmDA8YwB25MDzz0qM7wcHn0L1PgCvCJBZsrh42KE-8WkjQXCH5f1A-JzaYo59wVtcXeIw8o8wDtpQZcO_ZQttwDZWYHmYWN1zNDxvihJU-4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130224" target="_blank">📅 21:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130223">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
وزیر دفاع اسراییل: هر دلاری که وارد خزانه ایران می‌شود به موشک یا پهپاد تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/130223" target="_blank">📅 21:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130222">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، ولودیمیر زلنسکی اعلام کرد که عملیات ۴۰ روزه سرویس امنیتی را با هدف اثرگذاری بر کشور متجاوز تأیید کرده است؛ عملیاتی که به گفته او برای وادار کردن طرف مقابل به پایان دادن به جنگ طراحی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/alonews/130222" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130221">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔴
فوری / برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.6K · <a href="https://t.me/alonews/130221" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130220">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
وال استریت ژورنال: تهران در مذاکرات با چین و مصر، پیشنهاد خود برای وضع عوارض خدمات بر عبور از تنگه هرمز را مورد بحث قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.2K · <a href="https://t.me/alonews/130220" target="_blank">📅 20:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130219">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/130219" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130218">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
به گزارش نشریه NRC، هلند در قراردادی به ارزش ۲۵۰ میلیون یورو، هزینه خرید ۷۰۰ موشک کروز روتا بلاک ۲ را برای اوکراین تأمین خواهد کرد.
🔴
این موشک‌ها که توسط شرکت هلندی Destinus ساخته شده‌اند، بردی حدود ۵۰۰ کیلومتر دارند، کلاهکی به وزن ۲۵۰ کیلوگرم حمل می‌کنند و از هوش مصنوعی برای تشخیص هدف استفاده می‌کنند.
🔴
مقامات اوکراینی اظهار داشتند که این موشک‌ها از حملات به اهداف نظامی با اولویت بالا در عمق خاک روسیه پشتیبانی خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/alonews/130218" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130217">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
بازی جی‌تی‌ای۶ در کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه، تاجیکستان و تایوان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/130217" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130216">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nrav-IPCG6hAe6tOC0TuzSswofOlWg6gUSQk0riirq3cPNpXHsVirYiVYHUfMdFZm9rglgsuH5v50MAnA6jm74xoH2hD-23CAeiSoc_rgxBYpppsWt5VWUnxFuREd9-d9GH0qmPq6bO4AwKOQBX3CKXUdLBLrUOyvf5-OD7Wdoqar1Zl-Ay5rmbjnOUeNH66RDN61Iq9gFidOyVpxIhH_JXgG991GXE48P_HZiBuT1KU1n1YCebF5TGxj1bWDAR3GEW8dxF5O5h8Dq9UbB72NRXCfrlcf6SLxerodutUE0mfDJjY8r3y2sgug_HZAOroVr9oSEZGV3w5tkTheaKx7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نظر سنجی فاکس نیوز رسانه طرفدار ترامپ و جمهوری خواهان؛
🔴
موفقیت ترامپ در اقتصاد :
🔴
۳۱ درصد موافق
🔴
۶۸ درصد مخالف
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.5K · <a href="https://t.me/alonews/130216" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130215">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/130215" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130214">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130214" target="_blank">📅 20:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130213">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
دبیر کل حزب الله ، نعیم قاسم: صبر ما معادلات را تغییر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/130213" target="_blank">📅 20:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130212">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
نتانیاهو: کارهای بیشتری باید علیه ایران و حماس انجام میشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/130212" target="_blank">📅 20:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130211">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=iRZyIS3mjAc7fFlAIO7DZYsjbhuiRHV-JANvEw9DoybsMwgpVHi_W6CAfUBO7qcZ7ooSZJYSROMUxd8imncRNDKrG2aRhDqxeAFJuBnMbtA42CXG00Kvj3OV0js0aFbUoB2tRc_-nGwN9ujPdATANx60Z6sBrNjJ1vBVeSQk_bXsn2RAcuKrqVU_yAoiswToubcvJuBazfk-OuzQKT-4MG1z2e4jDFgs5Y6lSUOQ5Ci_Q1VLXfS_7HNn7r3HSliDc3rJ6VpSJKv_VPzOORb-EcmLlHC34IxbWoV-bCPe587tEH9PE039amodR-HoQCnSPWQdwxCVc-Oc26KsbD3SuQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=iRZyIS3mjAc7fFlAIO7DZYsjbhuiRHV-JANvEw9DoybsMwgpVHi_W6CAfUBO7qcZ7ooSZJYSROMUxd8imncRNDKrG2aRhDqxeAFJuBnMbtA42CXG00Kvj3OV0js0aFbUoB2tRc_-nGwN9ujPdATANx60Z6sBrNjJ1vBVeSQk_bXsn2RAcuKrqVU_yAoiswToubcvJuBazfk-OuzQKT-4MG1z2e4jDFgs5Y6lSUOQ5Ci_Q1VLXfS_7HNn7r3HSliDc3rJ6VpSJKv_VPzOORb-EcmLlHC34IxbWoV-bCPe587tEH9PE039amodR-HoQCnSPWQdwxCVc-Oc26KsbD3SuQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
به هیچ وجه اجازه نخواهیم داد ایران
بمب‌های هسته‌ای توسعه دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.8K · <a href="https://t.me/alonews/130211" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130210">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=MsUTirRbuvlj4QOHbgtjTwiD7yO6UUAde4KZGkKF_PXJv0jfxPsfqpwZKaYPf8vupk4rzbvGkuGU0gtYqoHZYo1O7rh_bUZZlyHJwBvht2sg_UpApIKSG_hQA7NEM3Hv91SrONP1eDnsN8ubBGcM3w5uO-GLBdRT0LKsdYU3r-Ju5Pd7SD37zKPEDsO1fdAepI-NZVHRV__LqHuRFYK1f3nDGg1ipo-eu5CYfRz1sa85ALPNRFH4o0R6mBNay8y16sPP7kTCwc4F0ctW1CvluWItomV0paHq7Ut1rewPQFsj4bc_ECsnP-6kzOWzmkC1DAqNjW-rk8c_1nwoP5fP0QMvBhkj5KrOkEonghNYSUZ2se2XbmfkIpF-MkqSx-0UztifA2WsFPEeJ92NmRlkFedpqjd6ZCEKvCm3yFpkNjwkXeukDH1viZVusB1Tt1WeGYjSBPE8XX7a6z_zzdfrVkNyACQxbfZWzhyb8HqVP0KOBNNBQCT8WXtG2ehIUIi6WNhCMqe1x0VKaqDjHwJCc-1MrNIiXN4_BbhtXNci5hlINGo_j92-IRNOiQ6wgRFfVrwszUgvNUOT1jhoGEg6xWsvGPXA__F6sjhWBJz-ajWH7EbRzFOI77sQ5p3cXpPuIZD9e40LsL77T81NFTNFqbnjSvyYKRFXjopyc82fCC4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=MsUTirRbuvlj4QOHbgtjTwiD7yO6UUAde4KZGkKF_PXJv0jfxPsfqpwZKaYPf8vupk4rzbvGkuGU0gtYqoHZYo1O7rh_bUZZlyHJwBvht2sg_UpApIKSG_hQA7NEM3Hv91SrONP1eDnsN8ubBGcM3w5uO-GLBdRT0LKsdYU3r-Ju5Pd7SD37zKPEDsO1fdAepI-NZVHRV__LqHuRFYK1f3nDGg1ipo-eu5CYfRz1sa85ALPNRFH4o0R6mBNay8y16sPP7kTCwc4F0ctW1CvluWItomV0paHq7Ut1rewPQFsj4bc_ECsnP-6kzOWzmkC1DAqNjW-rk8c_1nwoP5fP0QMvBhkj5KrOkEonghNYSUZ2se2XbmfkIpF-MkqSx-0UztifA2WsFPEeJ92NmRlkFedpqjd6ZCEKvCm3yFpkNjwkXeukDH1viZVusB1Tt1WeGYjSBPE8XX7a6z_zzdfrVkNyACQxbfZWzhyb8HqVP0KOBNNBQCT8WXtG2ehIUIi6WNhCMqe1x0VKaqDjHwJCc-1MrNIiXN4_BbhtXNci5hlINGo_j92-IRNOiQ6wgRFfVrwszUgvNUOT1jhoGEg6xWsvGPXA__F6sjhWBJz-ajWH7EbRzFOI77sQ5p3cXpPuIZD9e40LsL77T81NFTNFqbnjSvyYKRFXjopyc82fCC4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من ادعای نبوت ندارم. اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقه ما و به طور فزاینده‌ای در سراسر جهان تعیین می‌کند:
🔴
قوی‌ها زنده می‌مانند. برای ضعیفان جایی نیست. آن‌ها شکار می‌شوند. آن‌ها ناپدید می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130210" target="_blank">📅 19:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130209">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
بنیامین نتانیاهو: ما در خاورمیانه‌ای پرآشوب، طوفانی و وحشی زندگی می‌کنیم.
🔴
دولت اسرائیل همیشه قوی و همیشه مصمم است.
🔴
بیش از ۶۰ درصد از سرزمین نوار غزه تحت کنترل ماست
🔴
ما از قلهٔ بوفورت بر جنوب لبنان مسلط هستیم.
🔴
و تا زمانی که لازم باشد در منطقه امنیتی جنوب لبنان باقی خواهیم ماند. ما قصد عقب‌نشینی از آن را نداریم.
🔴
وزیر دفاع و من به ارتش اسرائیل کاملاً شفاف کرده‌ایم: «شما آزادی عمل کامل برای حذف هرگونه تهدیدی برای سربازان ما یا ساکنان شمال دارید.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/alonews/130209" target="_blank">📅 19:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130208">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=F6ISAqUV6QgV_7RzdSyvU4_48ValFaw-P7AsZX6B7h7notd5cSD8J1CDKcXPHnBiMtijYI9rlqeAZ4wK5-cUnf7QbpfvugKuEuAADKERWUrWGqWMSspo1DtgIGz9pKblB8265ITdTa3-8ZOwmp4lxikwVPWkzIZGbvqBybPzK4UWlNxct899u_JwQiTNIaEQWXNPok1Kl2KuRyT5IEOWRMhx1MXUx72phgBMeq9rYgzQmps3_HfeiDO8HynZyl-yVP1jicB_rbHof3Js50IjE-cNcQQ8-dtu_2pmwAN3-o1-8Qur0pmNAd4YyhdXtEdqHTeLEIVzTSUTDEMUa3-emw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=F6ISAqUV6QgV_7RzdSyvU4_48ValFaw-P7AsZX6B7h7notd5cSD8J1CDKcXPHnBiMtijYI9rlqeAZ4wK5-cUnf7QbpfvugKuEuAADKERWUrWGqWMSspo1DtgIGz9pKblB8265ITdTa3-8ZOwmp4lxikwVPWkzIZGbvqBybPzK4UWlNxct899u_JwQiTNIaEQWXNPok1Kl2KuRyT5IEOWRMhx1MXUx72phgBMeq9rYgzQmps3_HfeiDO8HynZyl-yVP1jicB_rbHof3Js50IjE-cNcQQ8-dtu_2pmwAN3-o1-8Qur0pmNAd4YyhdXtEdqHTeLEIVzTSUTDEMUa3-emw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: فقط یک فرد نابینا می‌تواند بگوید که دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
🔴
من همه آن‌ها را فهرست نکرده‌ام چون می‌خواهم شما را بی‌جهت خسته نکنم. شما اینجا زیر آفتاب سوزان ایستاده‌اید—فهرست کردن همه آن‌ها زمان زیادی می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/130208" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130207">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو: ما تهدید وجودی فوری را از سر خود برداشتیم زیرا اگر امروز علیه ایران اقدام نمی‌کردیم، بمب اتمی‌ای به وجود می‌آمد که اسرائیل را نابود می‌کرد، و ما این تهدید را برداشتیم تا ابدیت اسرائیل را تضمین کنیم.
🔴
وظایف بیشتری برای انجام دادن وجود دارد.
🔴
بله، کارهای بیشتری علیه ایران باید انجام شود؛ کارهای بیشتری علیه حماس باید انجام شود. در همین حال، آنها توانایی زیادی برای مقابله با ما ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130207" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130206">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت:
نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/130206" target="_blank">📅 19:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130205">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
نتانیاهو: همچنان ماموریت‌هایی وجود دارد که باید در مقابله با ایران و حزب‌الله شود،از لبنان عقب‌نشینی نخواهیم کرد و تا هر زمان لازم شود در لبنان خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130205" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130204">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kDsXtgv0PS4uCmRQBpgS5Wp9VhewldFDDLJ25Zz3aJeASRPaqQZucB1zu2ebWBRnuN7AyXapV7AKw0BtkG9vGgtfmduVOurRcSIYGzNU6gVfOSvD07XwhVldYN969M7vqqTlEX5wD8JvSiRcGS2SdJgv_nFqGj-XClA6PvXqd5anhaJw6X84jO0acyEbyHh5ECZyfjLaKlaIeIFyjrHtRWMR8UpWA6xSks-rZDUZx5k1c69Y8gcNMbZMIA3ul97VpTeKtLd-HhuDJdq_HEDL1QwShQzI2LO4fk9aa5aJyOHiekHnT6NxPj9mjtUL4BCsacdZHEGjLR2Tm9d2bW1-kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، یک شاخص مهم در صنعت هواپیمایی آمریکا پس از شش سال، سرانجام از زیان‌های دوران همه‌گیری کرونا عبور کرده است.
🔴
پیشرفت در مسیر توافق میان ایران و آمریکا باعث کاهش قیمت نفت شده و فشار هزینه‌های سوخت بر سودآوری شرکت‌های هواپیمایی را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52K · <a href="https://t.me/alonews/130204" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130203">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=AWdYkN6ELwBSlBWAydR2I2fNzWi1b5NX2GWpofikypPcXMHbZZQWwxPQjsSrvSQQtUzlvn6W-c3OoMZZz4c7luAQT3f1A74anoFxwWEcJn2xtlMrSU92N6HAO191J_j6S-laLjD-EP6WlxBAZynpTJYrmcKBSc83sVKq7bQduQJtWB2_jKstuvan_Wkzu9TDUKYFz5tCSSW0jOga-sUYEwBPwOnIyrYcZHUm2U2ugDju27-iKtWXab3WKg4rMY89W9vDsj4VTsbDUeG2HTll1aoaNEkMpTSox7BOVBNUFbPR6s9I5vLxlpC5-X2MnR4CSye2BZuD7U3iyP7BFUwkLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=AWdYkN6ELwBSlBWAydR2I2fNzWi1b5NX2GWpofikypPcXMHbZZQWwxPQjsSrvSQQtUzlvn6W-c3OoMZZz4c7luAQT3f1A74anoFxwWEcJn2xtlMrSU92N6HAO191J_j6S-laLjD-EP6WlxBAZynpTJYrmcKBSc83sVKq7bQduQJtWB2_jKstuvan_Wkzu9TDUKYFz5tCSSW0jOga-sUYEwBPwOnIyrYcZHUm2U2ugDju27-iKtWXab3WKg4rMY89W9vDsj4VTsbDUeG2HTll1aoaNEkMpTSox7BOVBNUFbPR6s9I5vLxlpC5-X2MnR4CSye2BZuD7U3iyP7BFUwkLjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعزیه عجیب در فلاح تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/130203" target="_blank">📅 19:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130202">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش تا زمانی که لازم باشد، در «مناطق امنیتی» در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
ما علی‌رغم فشارها برای خروج از «منطقه‌ی امنیتی» در لبنان، مخالف عقب‌نشینی هستیم؛ عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/alonews/130202" target="_blank">📅 19:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130201">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
مرکز عملیات دریایی بریتانیا (UKMTO): مرکز عملیات دریایی بریتانیا گزارش یک حادثه را در فاصله ۷/۵ مایل دریایی جنوب‌شرقی دهیث، عمان دریافت کرده است.
🔴
یک کشتی باری در سمت راست خود توسط یک پرتابه‌ی ناشناس مورد اصابت قرار گرفته که به پل فرماندهی خسارت وارد کرده است. ناخدا گزارش داده است که تلفات جانی و اثرات زیست‌محیطی نداشته است.
🔴
مقامات در حال بررسی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/alonews/130201" target="_blank">📅 19:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130200">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pplqjw7Eduh5vw-sXA3LI-v_lEbEyfnzTIiKFbIOR_gCVJ0aiMnZCe2hOWfWZtUvOsqDFZqjXLMg831ZCYBkxWXuRTJFv4WaUJZ2g7om53xmAdQLtZ9si8Xfal1cb7-wR6h7ZKomCvhbhRwiVBMTwGFYRq4KFj_Wpkn7tC_rvNGbUFZYLF0YOxBDWgBlo2aTPhF8BR5ne2IEFcccKDpFEoAkVIuj-haBJiX0Tj2ZbIU6MwkqbqW1IXZnAebd-Zpt5uqi051DqE7bSOhwGrr5lkShfl_Jf8_svZ28JDPE3mo6pJ-8CL9jwApkrx597yzcEn1YYxHvGw-dSf56-hnPzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130200" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130199">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/alonews/130199" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
