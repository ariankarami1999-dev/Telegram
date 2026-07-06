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
<img src="https://cdn4.telesco.pe/file/rq5-3qkLmssnMxnIjmiWenjn87Rl2adi__Iu0zSPD_xXUcvtZcOSYoYHcn-Y5SUOOQeA021UW_J1Be2ORqNxf-Fr2UMY5DqHv0XPTQWSXijLan_8uZTFbHL-l05ecNsu2vYMZbs7beatcotFxAI9W0juTsMLYYtlwvr3gdhmDaNyWS65dkMWbXh5evNUtv4uXFyrayGj2cBUmOPQ_5EJ0C76mmoDEhotwh2rQrNh8VdrFRzFeYE_xeonqkN63H7tXORWN1G9a4ZtxXVGiKRKUtZArdnzkJ9rA2h9wsRJ1w9T9rAAV4gyDPZ-0wq_mBPdozy8Ne5gkkbFS3YpZD59VQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 183K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 15:51:24</div>
<hr>

<div class="tg-post" id="msg-79468">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZCoNdpH5W2rs2dCrVHPASvCCBtHd-cwiAJ5AV97flKwWQBVxFpdyN1qjDRjxRAWi1LvCFncF1ognpeFlGv8VQgoAJOlnZ0IWeiKM_L3zqudwkHKx7xiefUaFuy_Jq_8O19AUtlDFs_-BfMPi28DVOFKtp4ZAbVUyxZtZfyXfO8gsl594sFBAhhinY69STK4HZo578LaygLcBhwVKJdlSLYqUuoTifVUsv5NR5BBNkHntGt8P4Paz3SvRfqKpdBuCU1PElPnWFz6rEBlo0uL-uFED9T23qjObOHYZnpB-WztMFacwVlkDUH-aJ9Ch3OSdcgIZeBNDcBmfHOBN0QCYMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">گنگ گنگ
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 2.94K · <a href="https://t.me/funhiphop/79468" target="_blank">📅 15:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79467">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OqSPjUkkJliyClbobFEtwbPxbs5we8a9QxVk64CSRgBV00W2u3G8orW3XsW6kFjZLp4xWYd1wbHGDCVXnXgfW1Htm0acP7Xn46eNHW80nRUwrufQ4yWG0jbdnlYTPJatne9f5Cak4sFB-qyaH_lZ3JgT9AG1eg3UxD_UkZw-NHCEPqRbzWMzRTBFuJNhZdqLSWTCF-j6ootDPFg1gYX27u4uDn4nfMn-t6TKaRNbEhFD2YemPI4Yk2U5st-xGtSA3tEidJRnKeW7s_woWSDG41YGS8CYgAE9bVqZaLpNXyBA6RhaTnGQgoF1KyS1tnansxiNWw8PU583jAlRFgPDHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمام مجتبی بالاخره رویت شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 8.73K · <a href="https://t.me/funhiphop/79467" target="_blank">📅 13:56 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79465">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">جام جهانی امسال یکی از Pay to win ترین جام جهانی های تاریخه، خودتونم بعدا میفهمید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.79K · <a href="https://t.me/funhiphop/79465" target="_blank">📅 13:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79464">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">صبح امروز اسرائیل در طی یک بازی تدارکاتی دوستانه با دولت لبنان، حملاتی به مواضع حزب الله در جنوب لبنان انجام داد، این بازی با نتیجه یک بر صفر به نفع اسرائیل به پایان رسید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/79464" target="_blank">📅 13:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79463">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">لاپورتا کصخل کینو بیار برا دو سه سال پولدار که شدی برو سراغ هالند</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79463" target="_blank">📅 13:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79462">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79462" target="_blank">📅 12:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79461">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XGR0lOkS3jnTJFcAow4BroXvsDtT_fl8qC0ToqpZOTKiCw9erQK5juo69SE2RdGkjReUe-rLMOItznkvk2cifV8mcP88BmcIiGNf1iwZErc0z6mAYpA30llLugPDV6P64oEPML7FSuacUTDNy2mP3qoHKqi63xbGHdclp1ECfhZRbntssMV70qepqhYj6IwRyPQO_YLAEtGmenXOkp3MTXo4RZ8pgdeI7-dC7xretnPeTG0S4sVxkqH5zIIcfcFZe9-SPZf2Ovb8C9fagrzaKcF3v1nxlKjEHMs77mE_r46Y86oUGNPWuuMH7ymKNW-sH9CdTJeXN3-zDsHafUUdwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برترین های جام جهانی در یک قاب
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/79461" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79460">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">میدونستید وایکینگا تورک بودن</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79460" target="_blank">📅 12:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79459">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">حس میکنم نروژ انگلیس هم میبره</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/79459" target="_blank">📅 12:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79457">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/a_eN76qsLU6BuUOVIg3_IszJcmj5c6UjU_bUgbRoV0_bTtfxdzQE3tVPcmqrdUeNmc0nHvTDM19LK8WDP3zhCSL4rx95YbHhR7XJ2bVQY28a76LQ0C6jYbRNtXdPdzM5Tx80K2HJOEk_dgHs6UDhtSoe5tCb268HzICYJL1JsiO4fH2dhg-5YbURoF99VRa2Ynt4zOHeLE8ExLotU5lnKFAKRAy5g_T0PRbDjBIpoQ6IgrzTbdlQ02oCv_cYjMsoTb4l0okg9u9rrzPLPXOVJ2viF0UXAqKTgEMSexclylxNLwcSNNk4K2Atn7t0DvIIjOvEL_Via4omKrnRvJw8CQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3g8_tl8Jz6x6wmVApG1qg3UHn3qmATg7mjvXasoLWurF2YWyfg-xkQUy8JG7sc-MjkRbx_sKNH3Zk3Q4YC1aUj5JFajy90FeA27vy7usFZ5-l_G2mV52XykpuwTQ3kQj-KXJa2W6iBIcyoeShY8_j_0Scdh_r3XPf-sfs870cXoczDMyVZReWxUUIQ5n6kT-bOMcBFGp7QpUgqbFCvdQOAUhXK1bamRqdpsEL61UCCZUg_R9w6EViEn-1Au7t5ZDtijINYjsoabmKIPx9RhpGR35PLtn65kpKeahKWEWgaYi_JK7MDjpMIb7zLDKL6mnrh0etZhl9-Iv3Zx5dg9Vw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">آقا این حساب نیست نروژ دیشب 12 نفره بود
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/79457" target="_blank">📅 11:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79456">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2cV7gV56b15PkRhl5uWi1EcU4zmcNTVm2jptVv3V9k6rYZ2ZcSbLzEEN5EmKyp2lQvIXcDhJYPPr9838SFLrh1K0UVl8iGZcCzv8zTS0KumIkhkgNKAYoxqGr7Tl7jV7oP8fOHoeqd8r2no8xSGtnI_gRJ7AyVtLrvg6Ab8wizrqM_RlMdvREpm9PdUMRn_CPOd14vy-nNF3hYkTIwrWnmBUsM11O6CD6CD27MSOJROMA4CNyKs20JAbrCt7enBX7aCZrzjmbAtDMf1oaiNOzTM0I02aLjoryBJGXlqk4_M2OteYSnEgMupwnljxUZfXmA1S6TaSPD-lVHgNwEVMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ ورد :
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/79456" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79455">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lDRmHiq1iMP5ezD48PY49L6FFQrsPtZAjWMdNUSlX8y9vO8TU3BBn7f7typIMmSA1W-VjotTEno4vBqgogpyk7LgruhDj5D61T9uQT6WwmHbvB6D2D4GYTnhgrhdo_E0KV5kXfZ3otUNUBvjITxAxhRSjrZkAElUs82OGaebGcKH8hbjZK_FVRTQu8Ot2-4sdnxTFbpiJcSk9V9M0mvCgSn3rq330u__n9ivcfGavg8qKVQwAjohwfuucDKL4eXe627Qi5lTsJoQGxz2mB8RDBo72VsA-tVk2rIAN0cHlD_nVhVb4B2n7DcwvyEF6asQwtLdpSNY-MW1iCzQl7uOAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
پرتغال
🇵🇹
-
🇪🇸
اسپانیا
🏆
یک‌هشتم‌نهایی جام جهانی ۲۰۲۶
🏆
🕔
دوشنبه ساعت ۲۲:۳۰
📍
ورزشگاه دالاس (ای تی اند تی)
🎲
با بیش از ۸۵۰ نوع آپشن پیش‌بینی
⚡
با بالاترین ضرایب پیش‌بینی
✍️
اطلاعات و شرایط بازی:
- پرتغال در مرحله قبل در یک دیدار پرهیجان موفق شد دو بر یک کرواسی را شکست دهد.
- اسپانیا در دور قبل در یک دیدار راحت اتریش را با نتیجه سه بر صفر شکست داد.
- برنده این دیدار باید در مرحله یک‌چهارم‌نهایی به مصاف برنده بازی آمریکا و بلژیک برود.
- با توجه شکست‌ناپذیری مداوم دو تیم و تساوی آن‌ها در فینال سال گذشته لیگ ملت‌ها، تساوی یا برد خفیف اسپانیا گزینه‌های مناسبی هستند.
🧠
تحلیل بدون داده، خیال است.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
R15
🅰
💻
@BetForward</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/79455" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79454">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">چه بازی بشه بازی رده‌بندی فرانسه نروژ</div>
<div class="tg-footer">👁️ 9.66K · <a href="https://t.me/funhiphop/79454" target="_blank">📅 10:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79453">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عجب بازی شده انگلیس و مکزیک
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/79453" target="_blank">📅 05:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79451">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jJINrmK_G5aV2U_C9JabRoKnQs4e73VwcKk6W-92YXbqwCVdrCtg8LuY8lnILeWC6fA-R2dAwp4Ou5xRDHuSMIpT2yZdGl-uHCLaTbYj2q5Q5T3szxWTSyx2G8WLQ7ATeYy0JBZ06BO-lXjyaqplNTzPTAN-1df9RW3ABWYrVGMKqSwsVG1On5mFbxU1VmQKINcpfkdEjN8n86tOFNGUl3w65oM6Gp2-OYQSOZ5r6QVNYwTyjamPc55A7-gFoBbRlnRC6gG1cOwwQfIQkef7WHnfBcBwGrehRVGBoGPwrRGk-G4jqQViYoFeFUucPPa9Ztb548KHsFSryv6Y_NhK0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دادا تو امشب نباختی، ۸ سال پیش باختی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79451" target="_blank">📅 03:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79450">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">استوری جدید علی آقا دایی خطاب به کارلتو.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/79450" target="_blank">📅 03:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79449">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CUuNGwTWWqvvpuEWKde040pm_gChVtU-Wv2mfRgcy6dCpnXHSnIFIRZA_WXdNgVU4UR90H2NdbwaQMAykSwNuL3jU3_heDqq_I7RJNGyYtq3CzRG6Vxl8Sph-Ym0ssmv6MPLllp6jgYjMdrp0qiA2_6xT_G2rmbjKNPdBo8anNYMJqwEsZWVxZgM2NpMP8KHbgWRF4Xv1-AkNDA4EcvVXlrS3Yk7kEhY278IFIJjzDb27EAIDT8WNpBpH86tKpUSXPm4fGXwun3D5e7HmAlgrsB6bIVnE3wJvj2ct7kW9Rq3ylNNnC7boHDFHlInyPjw5DIcz4Kp1_AkiN8VmezTng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هعی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79449" target="_blank">📅 02:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79448">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">هالند وقتی تو سیتی بازی میکنه، بین بهتریناس و جلو هر تیمی که بازی کنن دست بالاتر رو دارن تقریبا، ولی تو نروژ این شرایط رو نداشته هیچوقت و همیشه بار تیم به دوش خودش بوده، دلیل این که قدر موقعیتش هاش رو میدونه هم سر همینه حس میکنم چون میدونه که جز خودش کسی نیست که جور اشتباهاتشو بکشه و ببرن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79448" target="_blank">📅 02:03 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79447">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">خدایا با حذف انگلیس یک بار دیگه فوتبال رو نجات بده   @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79447" target="_blank">📅 01:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79446">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oTZj14P5m5CEbYmjkA53m_HBq8-DyLAJ4Jbgog2q5KEvPPxjWCkmZFtK5Dqh4LSJzTd3oou2-iQ3tHarPq7i698ktj4YproeiYU6eNs6GfXSBqNyJdR6Gm6P2txw0UAub-YoWDUQ24nsoiTfihwol5moqhiTAR1PgLQDtP4E7Otu33bhSbaHfkesZ2O16MfGG1IdxgcjCITkScs6wraQxd0-IUIiBiVuaMUZWXL6p3uwsmqESuuf6Q-TfhsKH1Dxrl81lK1Zcb9WvzxDTR3X60clo9e5hMdGtfsrf_5xgdFKgl5NmPW1z1POI-fVRzeyIbsAadj3Ly2tZJ2BZayl-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سیس اندریک وقتی یک تنه رید به امید مردم یک کشور
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79446" target="_blank">📅 01:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79445">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">بازم چیزی از ارزش های نداشته‌ی نیمار کم نشد</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79445" target="_blank">📅 01:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79444">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیمار کصخل تیمت وقت نداره وایمیستی اونجا میخندی و کری میخونی؟
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79444" target="_blank">📅 01:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79441">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C3nxo9q_12kiwU0pFk46xl2T9lmKtiZZTllv63N-M_L_dMvJ2NyyoAgF-0qvr_mkWYkpwrhMN0j1uSNZePDgvMihz9z_N3oKlIZH7xWST665fG9c-Rqd4chld19wWE3KT_rNamesx4eMT9f8PpaD5_Zi2fbYBY1eSSsGrP_F5j8D20ymk_OBWXl7Yd93Yaro6eILseyoHH0EOG7BXK2suMhlNRfdwrITc0E2XZygQrBRfhxA8f7jt1Vwd8aO2PUctnK97JfmH6lBxRaZ4_BqalVSd6okOjZcrhj6IjTwpCY03dq0RD5Irv9YI0UVhiIb4QexdXEEOkZC-ROpwhs8qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسم هالند هم رفت تو لیست برترین گلزن های این تورنمت کنار امباپه و پروردگار بی بدیل فوتبال جهان
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/79441" target="_blank">📅 01:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79439">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ریدم هالند دبل</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/79439" target="_blank">📅 01:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79438">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">وینیسیوس
😂
😂
😂
😂
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/79438" target="_blank">📅 01:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79437">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مهاجم خوب اینطوری کار رو در میاره
هالند تک موقعیت رو گل کرد اونور بازیکن های برزیل انواع و اقسام موقعیت های عالی رو به باد دادن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/79437" target="_blank">📅 01:14 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79434">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نیمار، شاهزاده فوتبال جهان که متاسفانه پادشاه نشد به بازی اومد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79434" target="_blank">📅 01:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79429">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">کارلتو این سبک کصشرشو تو تیم ملی برزیل هم اورده</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/79429" target="_blank">📅 23:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79428">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">انگلیس به این فکر کرده که بعد بردن مکزیک چطوری قراره از مکزیک خارج بشه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79428" target="_blank">📅 23:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79427">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">رضا پهلوی یا مجتبی خامنه
❌
رضا پهلوی و مجتبی خامنه ای
✅
بیایید از آخرا فوتبالشون لذت ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/79427" target="_blank">📅 22:23 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79426">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SLeZKbohpOtTvBYCo5L71XoDl49pVVPKt8nvEvHKlZ2cZAelT49m_bboV9pABfbbcE-LZSfl5Y9Oaesv3FGUKLrvnfxCj-QDdt1As5iKc8xt-Zdaea77PNNVwxMwh5NvZ5mFpc0qlfFLQlhTBxQSmpUYD7oGkPruk7WUOcHxw-FNElQUFE5DaUxOnsMhbSjEO3vhnpP0TqaP0mq7hW5ZvgrmvBIYfQWyUg4FPcCvlF6AQKK313_XslPeGvtTdqUJi0qBQkg4zLYgyk4IsvLr1K4emFMOQ04PuQqk1Txh-9AwrTGgvxgyCCDu2lsKBGOMPupnkV7mBbmD_eKYq--K7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دراماها توی ایکس از فان هیپ هاپ هم خنده دار ترن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/79426" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79425">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HH3pIOOaFZzCuazTGTXVhQaiv2oZX4hA8MoXTJrvepLd4IepRBWcqEOamjVLbxPQcGlY1Qf1CpteitYGPbd83yCrtjVjWk2YJ79zwgX2syecDDRsjOyyRJfCkgwA14wz5bCvrWrkVQ7F7VfGsMIDMyQByBs6Rhquzd5WGkTEJvFxV93ddW5ylUWcCZbYCaq5sj24uGrTys-a1XB59YkUI9H8FCBqJb8y72H58OW0GQMj29x52GP9ZBl__lYqfZ0sTlWiYw9FVrRl3MoHQGjCf9HqMSYyZtT-68gA4g2heUESJlJV9CnMhFMKYjvX1lYy3xBmqRwmZhH6x-KC3LagFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ در تروث : از فیفا به خاطر انجام کار درست و لغو یک بی‌عدالتی بزرگ متشکرم!
فیفا به درخواست ترامپ، کارت قرمزی که مهاجم آمریکا،تو بازی قبل گرفته بود رو بخشید تا محرومیت بازیکن تو بازی بعد جام جهانی رفع بشه
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79425" target="_blank">📅 21:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79424">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بدنسازا شروع کردن به خوردن کِرم، چون تو هر ۱۰۰ گرمش ۵۰ گرم پروتئین داره.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/79424" target="_blank">📅 20:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79423">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Pi1z2w3LZPNTCff1iKA-A0wn_OcL-yUNS2wF6lSNjon445a0orxCHHhm3afJDWf_UP8guvnHUp47yE_2WoiJLx3K6AEtb2qIpaDLnffqBIeeMLbf8Nbo3hdIkFtswZCOx2tuQjkBZQBlfkFIt9hUugfgDo5PuoD3xt95lb4ziA2d2cKedUod65ouIG9LV2ldnEI3RNPqqrMWrAVSWoBwIBbQYlc_n6xyT3mAoJu3uMPrIErOQo6-AeYqH-ekmZ8G5Ksp62uRilJHa_CzJcHsNdNsx8TgOPqfjqZJY3_ncDcyVcGv5XJU0jiLyzCd7me8-u0Gt5ysjDrdhCQRMe-Ahw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو بعضی مراحل GTA6 باید برا لوسیا مانیکور و پدیکور انجام بدید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79423" target="_blank">📅 19:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79422">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6a3401b971.mp4?token=RlrV6HSCy9dnsNhqpjhxXUant15XvtpAkU__ZQ6LQCHE6fN4U2v3-8ORhCaaxdZhedKUGiK8aZLxeUbQIynGejHpLNgHbY0O2I_HpbRrq78rXAVumqPwdQwEobHJSiOCVyymLZHLcLLHLKANT9DsRS6ODuw7MBiiJjdL-Xkmo5afVFE5SbPDJ5uIDB0mvFmfWS1diFhay4qs37uFyvH3C2BIDRXzEw0JATF0bIXM_xXcyxEhbv1c7H2TaVOrnQUPdAaCq_Y05hg2NtV1h9b4b20OyoEF03Gm8Bxek-nQIjL_YSIREtD2ZgW2xCRNsa1yIUmgivXIZSnTi-kzTUdsp0gM0mn86Ubnl3wW-ReF8clwM9H-rzkAquvuAxiqSZ-yn68IT6DiG40kJvXiMqEovht7hEno9AnPhyXPc_im5y1LNwJg5jLV5376TmL0Dkk27mlYcm7Q16lW2ifGxLqDasJ0mC-v3xsh6ztZuc0aVK2L3NDe2M-fUEspS4EiHu89QBonutuZX8xw8zBpEuagmdPf-X2lt4Z_VVI8Fdbzvd5sR9mW0WhkidzcYMIWWS1gjxAg_bDMB_o-n_oUme9GJpckARUbLNhIsHglYBrBrhBCWjqqE5YTmv-qbq649DbjpJgSYwIvY6LQKn0CzwLJQNRy0-1iH3E7HbZMjvlew0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اجرای جدید پوری.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/79422" target="_blank">📅 19:49 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79421">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">اگه یامال جای اسپانیا مراکش رو انتخاب میکرد واقعا تیم سوپری میشدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79421" target="_blank">📅 19:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79420">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">Du biat guta guuung
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79420" target="_blank">📅 19:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79419">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DIULMnv-vlr3g6rbYF_lPFbTKR2yQJr4b6ST6VfgwcZ6pZd3552mFkl8t8X97X5Jo7NpIDkzI13ZaHApxjqBRtejJZF3V_mOx3-CgY9-P4lCZMTB6RpIxz9hqSfaNdDqJFwXZEc5eDtd0Gv_neyp7VyymMMvD92lr5qBQV2Buj48_YBCwY6EHELbmjZ0r72IDirZKlp8ChqmvPvCHVWkYCArjJw_WXV_iZdH6K_H70N2wNIffUUR0X9jIvtjNHytzzmZ67Zn-2xtU5_sugj8EeMpylmiuE9xVo7zznmYebuBESwsWwBeX7d1h8ONjMwmu8yr9gZcfllgjGObbwaLhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوف
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79419" target="_blank">📅 18:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79418">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LalXGVZOw9nnN_EmDH5C7vhmFEHmYzZ1W8Q3fL5kwZ8paUqfXnglOsiE1tlESycnT_N-oN1TGkx440XDAAFPN3U6rUWOgjcxtJ32ZfbkiFt1G_zslpfwBooWWlAkEpOTI0y2entCquPIOY2jkavQoF7R934O3FgxltuhL_2Zi5ZghV_NFrPuYqsZtxruInTHRIaUjrJhcPM6MPTFmfrEtmbUBJ8y7VMLVT3VuhpVGBwuKbxONceQs92lL8ie3-x3XrOXzdxE4bZtHyPLZua_Aba6-kKzzZhLRv5J75x8E12Wn46FS1hmTSpcPH2wHXDXYh09i8bChwJ88O4-TUL0Cw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حصین تهی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/79418" target="_blank">📅 17:13 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79416">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bmRQFTSsktgLtsGIlMkjkscwRRJVoNto4EwR1mhBc0KR1JFYsILJf0kMg7ealEzQnjrPRm4Qok-ajrhq-EOvn4Lq9gYjSdMDSNbqLtNVeRSRdzmrXKFI2CbzeQyL_3Po3EaEKzJsGLBDa2OsaiLm5xUOzujGBksrWN26v1G1Wpiqb4yNLfcKg1InxFMzS3V0l2N83DFZMQxVJJ1TPe3OM-lLP2NOXOhTW6nvPYxgrHEYM84tyD7w_OTIvC17K_kE-hTRvc_eZdWLkhTY5TVWupkUBfwLUnU4doOmudEBmgbTXo-cmDl2Tx1DIq4s8HAPFP3HNUZiV5m4ZFnPR6ufew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kYHrRfT1Akihhs2Bg2j8mLQZoRxzbzm7iniLUitRovDb2QjGJF3_1RgmN8ZEEZDiTuxJ_3Wxo2LKQchQ2GSAdvYekwPiBCmYoU_nDYZ-ABcbVyIffT6LQFB5dLLSvmEM8nBUns-fm2DNhpoBCI_KlWBQrqw5-v3u3mavf977BugWhwvUyWST-Q5YWxHjPOC_iGpcNt8j1jH7O57DAV-XD6f6O1sns3mwzvbX6vr9mXD24kG3TqqN_D-TaVPOlhNPoADhOrW_awnUKIXd_KrBeKF21HogjlBywY2zVNbdNA31_Vc4zmjYjgnsHd0RNUXoxwmA45rTMBSE-xKHmBzJmA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توییت جدید ووزینا :
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79416" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79415">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyZgaY2qUNDNrDpAtAb0tGjhPZ9iAHVruYp-TLbUuP0eM84fdc6puuSsLEfJmyiunrtK8-PUIAOnAlQdmn1dwWZUKfnS1z98CYBH64qRQ9h_G0pXl2Y4ONtifqHDUEOTnK6TtLXKf5XgtiAxyKQTmuZZJlbh-5Wy-1hLH_lPyqXWsOeVWGJgskrVVM9GBvjy1PnBWS9IndHviVUuhcMID-fcvVjNT0U-rpHFMFencKai9_LYOIdiLpRR3S8YW-st_FZ5Y-4fabLDCX6UiwqHWalhRBsAI_OM14CT4m7FF5i1RgQuojxQfsZh-Yd9sR4pofTSyV2nCo15NrQ7FOdATg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79415" target="_blank">📅 17:00 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79414">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P7XXW02ryHTCKMbCIAfszBX3GcSVowlNG8O8Y2H1uJZGKW-p9rHqRNWLEKG5t4XRkGpwZSzYIn9mlLgu93sufgOr0czJk0JrATurjgZlO--DMh0cQzCg4KRHPDtnXeIZhmx25kO9XKvRYOWbCb5kltONIVfQfMe_Q7CGLA8yuQMM2ZJMF09qCSAEN3VfTIiQszvWAD32PJgbrjLfQMwBz472rJnbHh2GJ5idwWkya1mTMeVzW7cOl4SBGk-9H4bk_FGdGdTnLBcsPu8YT_giSxTYTOJEp_MOAKulMTIIVl3rnQwKK1xtZGNogmhgwclLySVMs5mro_IA2RpJxb1oxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همینو طارمی گفت مسخرش کردید
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79414" target="_blank">📅 15:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79413">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZFyzizIPImm9lJzcUWdJgzU9GKpXL0Sn2l1MlAm7FMVVsQHpTrRLM95ZRa7Io5LvgNgzKobYcyjkgGoyKgQts6TKB0_u-hicjd_ZI1ugsewSRTWxYVha6ZvxJui5gA2XrtC4aCEr2iwQuIGWqkrSQ7CRsA2hA2sSlE5hy_iZ2QWnlMy7RA0Y7_9BCSw0U2Fn06D-snzR80yaiOpX31V_C21NzqX3MvrkaIih38022uLdspGPsFphgKBtrDoPCh2I0IPc9pTfvlkZEXYZxIBBNfFBW2_THtWjm6uEXFp-5_RwZXLHRoFTYdd8GuU6h4EO05_7r7zPOIRBIHDC0-ZHrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا این کصکش تو بارسا از اسپاس ۴۰ سال هم جا میموند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79413" target="_blank">📅 15:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79412">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=P5-MOoRrlqOqa6SUEyzFl1hv4jihrwcQ9DBFWfBloWk49LR-eTxDCmIPkQ4aUfNkLuTZ_ByY2oknsgk3Q7limqmhQZJziHwARAeYKdhS_fEQooqmWp0vpsVQGJzNwTQGFUlP3RaEnsYttx8S7Yxw0iny-3QsyFJlrpt-VSwxSTQ3un3XpmM5Z9AE4WSAqVcCeHa5Du_RMoyDa9G8yeGEL3evaL0dYWx-D45q2n28MbGImI6MJu42W-5YDqAE4aCqpV9-10pCEaeM4fRdU7OxP5AFTTL5JuoQLpaCARfnAH-g8A6c47Q9OWD09EHyHAudMi_k3MfcIrDGihKO0QJHdQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e956f60f57.mp4?token=P5-MOoRrlqOqa6SUEyzFl1hv4jihrwcQ9DBFWfBloWk49LR-eTxDCmIPkQ4aUfNkLuTZ_ByY2oknsgk3Q7limqmhQZJziHwARAeYKdhS_fEQooqmWp0vpsVQGJzNwTQGFUlP3RaEnsYttx8S7Yxw0iny-3QsyFJlrpt-VSwxSTQ3un3XpmM5Z9AE4WSAqVcCeHa5Du_RMoyDa9G8yeGEL3evaL0dYWx-D45q2n28MbGImI6MJu42W-5YDqAE4aCqpV9-10pCEaeM4fRdU7OxP5AFTTL5JuoQLpaCARfnAH-g8A6c47Q9OWD09EHyHAudMi_k3MfcIrDGihKO0QJHdQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وای خاک به سرم این چه کار زشتیه
مراسم ایرانیای کانادا برا رهبر شهیدمون.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79412" target="_blank">📅 14:56 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79411">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">اومدم بگم بسه دیگه گاییدین از نسل یک مووآن کنید، نسل جدید گوش بدید، چشمم خورد به این پشیمون شدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/79411" target="_blank">📅 14:45 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79410">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">پیشرو و اوج یه داداش دیگه داشتن اسمش امید قدر بود، اون زودتر فهمید تهش چه آبروریزیه از رپ کشید بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/79410" target="_blank">📅 14:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79409">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علی اوج چقد پیر شده پسر</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79409" target="_blank">📅 14:27 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79408">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">تداوم و وفاداری رو از پیشرو یاد بگیرید، ۲۵ سال گذشته از وقتی شروع کرده به موزیک خوندن، هیچوقت از کس دیگه ای جز امینم اسکی نرفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/79408" target="_blank">📅 14:24 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79406">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gpJ5uGsMg0YdfsHz605ZrGaZP7l7m92hHF3IoB2mOYeuMDQsFA73wNIhJV1GEgmMjxFnFNqvx-tdLMrgliUeuWQCDnSMgQjaICfbvcl-FYIayHkqBDEc_aaapfqbq8-SwEm7MPBlHlOQJ1Kw0nmQ9O-T1dA3ROmqUqDcfxxzM7LyhfbbUUyQkZ9-ukqX-5pEeohBk4koUjS8GSZkX4_pAlRjuiONCZuEzGeJ-qb-y94MTSYWmGyZXKS-bFZgXib9-l7jGuMI3Tzcq7NTWRN4VPBdunT9SF0kmREdp1lfax1hVhe0HnCS7_ShPypZKzdysnjuQ6R_TUv6QD2xIuVlVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7jaKKdD6hdtlI20AsEy5MT0VHu-Cdqpa7RnsyCTyImVq07yKfWOJ4JEa5X-39_S1L7oZIOz5PT6iiBOZ-nmc9UW6f3MzAeeuc_f-K8st6m9onP7fNYk58sDVFNl3FdcnT2c9wvMqZD06QP7J2SeBuGR055-r--tIyoqZHs_dVn5i-e6OELRcGhPFFYPmLG9mJVlAARMZLXfVLO5Ul8H6oQ9ffL0PUD2wOC6m1eBpHvavbEngF_f9tJ3Ka4uVXKb46eBalS7oLucFji0DwZCeBdd60aiUELGH9Ug7rXIRg1n5TEXK59FRnQfOIB-8EzUhPpsaAesEdtljzGH223voQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79406" target="_blank">📅 14:20 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79402">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">یه لحظه حس کردم با ماشین زمان برگشتم سال ۸۵
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79402" target="_blank">📅 14:11 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79401">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.  YouTube  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/79401" target="_blank">📅 14:09 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79400">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BPH2FTwIKA4_qWmiqh89tEWtIFD4YU4X83MhGDpDlvND0RD58_SL9AfGpLBDRdAadMsAqByA1oHpJCndVwn6FCvp9vcN_I7zGUFBf9vGXvzmbkO5kmZc04aD8EIArRfpRHp8_BOXL8Y4H8cs45YaMjMkFgJoiIislxpAwxIIMisq1GTQUfYsI8BbcUh3s5YjgH2x2xDq8XBNlPJPf6zeUOP8IigM_uE-zwRYRl9X2cN66jrNlXTF0CGv9f79b4-LJbvcQn_-BssoN6X-j733-lpwunP3PlEHTnUU2gscouN-RlM4LZmvwtl7AjLctMYbXQtgotyt4fNF4_gqcbiRgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید تهی، پیشرو و اوج به نام سی دی منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79400" target="_blank">📅 14:08 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79399">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FJHZgdUwm-R0IKxTYm8umJKlu2JYzVGzim8tdf8s-mz4SvoP_rMBpgsodavj9ydi1meXfaJWavBVTCh9pKosotvxGA8MF2r_NCcMNJYpKHRnGabpqzNSG-8L_WzvWeauMLV708AA8EEUr_Wfh-HIuL0NVH9r4YP22I8jzzhgR9LnTwrUBpYrAExvP3sYLxDFSdbuMkAAwNjoqqctFJQfvFTLam25CDKhDk11uz_yqmNrgmE86lZwp_IbPlk5Z6ukAgduOs62JViadVTjoZW50y_vGBZd4vnP3b-umrdgte827I0mZrVAfP5x7yy-fedN8zkHatYfvP5F8IJX1nxwRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاربرد این اون وسط چیه؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/79399" target="_blank">📅 13:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79398">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W_6x3nQRLJIHFO8wevbWCkSPzn5DycEKOeoNgWaOws2NekV39XIphVz3aflwTVEYXzIOP_0MYQQnvqNZTSJjSrdBEKKQS937DAS2Y9jt26YQKKgWA0x7Mj-709h3EterCRNHqjSPuCibJ7T6sTg8tBVur9QyQm87Bg4TJTqQ_qNBYVvALOOkuigRQLjYbCgAkswuq0s7cq32Ti7bMPzNOQjRxm13fJ1tmmvwn70ppNbjz012SPoNPDMdgiXrHITH3Kt9JL4726LmbPsYD0YC-jERaI9aSL4Cii8rBctGk6S5xGrzJtvGQMr9X5BmT_N-jFNF_ke-8WlCyEoDSZm3Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلمان تصمیم گرفت یه مربی خوب دیگرم بگا بده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79398" target="_blank">📅 13:34 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79397">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تارتار سرمربی پرسپولیس شد</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/79397" target="_blank">📅 13:12 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79396">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AAP3F4TG7Dd5vRqeyBdYcrkLqhRhjDhtcpLG-_Mt6_m8dum-G_im_LuhB2XoWB2ZUPAoE3xElzBaCY2T8aZh9H-J-F9DMyQb6KXlLVWmjDUwQBtNNYi4JhZLgAkBEnfiXA6YVV3a36JkMLJqCtBqHtG6j1ETemDhV1A8sHQoW6mg0kKOcmVW0rA9fM0dYGQuv8dLNJPoPwBTGnPgWBldRPkvsCy1iZj0m6H5yFbhIk_diCj8mzMZn1Rks0oRNx5zy3FA3yJ0QaRWpelVB97nRGgrd5VwH7F52opkPjk4s9ia7cJKGDKoyVhjf5nzpSqwHn22iOb9Sy2XaiaMVXN26A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">MEGA BANGER
😊
😄
😜
💋
🙏
🔥
💥
🌈
☀️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/79396" target="_blank">📅 13:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79395">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gLCcu-teeXusuGfVC92LohXRHuCS91aTchh-UnQrfHXyhqLq7f6C98SDT8ZxO8S8eMKJwwYQMbPwxrlOymRBQnYZ6S14wmPpsvkOQebQbrecPujR2FhBgSq5NwZitmvzxXTRy9L1G0s-jyLLBlHN88E5fZw9g-OmcyGMs1MX7OCkric0z9tDMlzIrZ1ARgx9j0n1RbUlY624LF2ZOSea1ksLVOqXRS7Yr3fN3rk4OTAD3XaQDbkl0kHFSEDWKYv-DN900dqpfeaJKXynxQ0U6N1bc4wwHL2TqdcwFF7w4ftvgU1UQNiN4fbAdYjQFTuXmBuaYiTTuaRI5k11QgMo4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/79395" target="_blank">📅 11:43 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79394">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انگار بکام میخواد دروازه‌بان کیپ وردو بیاره اینترمیامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79394" target="_blank">📅 11:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79393">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DHX-8Kf_9hrAdsd66cLjEHOvqrgEoYEVV15vj7JZAdWv6dA1QPVF8O0S3E2ge4UeHJGc174srA5xfX-m8e2vciDTGXb2VNz4qrqQQ9XnnY6_hXIxZn7Ubwi5fxoif7g4zF1exdsZqRmDjEtdiXgZgEwj3xJgbkbi0xqZNkc1taQfMPTuZN7ZVxqpwmtbS5GzQwGNKsgopKGyeu78lZg-6zpHSQuQjR5Q7ATsFQM15W_xePH9X8_XPfQKGC2qi8hdu7MtUd5G46O2WWfsXnkA9p6HSdXyvqEe1e09xxEgQ2tX8rv6E-5xYAUtef-tgqNW9RXEnHzWv7jlUVghtfCXAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرانسه کصخل اگه ایوب بوعدی رو نگه میداشت حاضر بودم سر زندگیم ببندم که سه دوره پیاپی قهرمان جهان میشدن، تنها نقطه ضعفشون همین هافبک بود که ریدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79393" target="_blank">📅 11:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79392">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MiHgokchNOl4bajc7pY4PyvMmubshYpi8BFy8cTDGNhGeHTBf57YRiATBB3LxZZvIiHHfPiaarfLTDUSqYLZjknl4Lkh6dEkWZ-qNhhw0x1vG1AknnaN-w5cYJM0TrpnnPdJeLkhcwMA9SFmxBFP0TmQwrLClgwPoeIl8LaAHNMlhXiLrPrqwYtTl8Wn5BgfSSWxlqlnVihMgsoY6oFR4-pXmd44zXhmUT_QNoeigSKfFPJ5xKxakC_mUTWyIPAhwwY1OfZXWxFfu29FoPbq1mPrJhW2CPW9QnpImqjcL88qaacGXR6rPhxnCXfSakCEwr7w6wAwRrkct9oHxwLYLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خداحافظی هادی چوپان با علی خامنه‌ای.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/79392" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79391">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qShewzo3Eh91LHmMGt-Q23qTcZw2M8ms0IAE0ofkJ95sS8t3H7Imi_6JcPKberlzc9m_wLEIem415_cZmx_X72Ju4jJehU7F94v1ol-D8qut8Sp35zULBlpZ_SqVTBs5eFWWz7qEoUXNkLVV6S25lmc2tWdShFiDtdguSUfo9b4blc0kmssA4mwfydN3eoJ5ng9QHHT5cc0XZYllD6Cq3r20forKzsGBQKBB-BNj-t3C7ulPs62uHFhMGwC6sUrslhh7qzxUKODQg-aQzmanxjtx-ZceVTAVG-UotJwEaHqw7Pre5dWL8kauIF1GtwiD4gKoGwHQtKSCVL0JM43ePg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
گل یا پوچ، حالا به‌صورت زنده در بت‌فوروارد
💥
⏩
یکی از محبوب‌ترین بازی‌های سنتی، اکنون در کازینوی زنده بت‌فوروارد در دسترس شماست. اگر به هیجان این بازی علاقه‌مند هستید، حالا می‌توانید آن را به‌صورت آنلاین و در بت‌فوروارد تجربه کنید.
• با حضور اوستاهای فارسی‌زبان
• محیط کاملا آنلاین و تعاملی
• تجربه‌ای شفاف و هیجان‌انگیز
📲
برای ورود به بازی، از بخش «کازینوی زنده» در بت‌فوروارد، گل یا پوچ را انتخاب کنید.
🎯
همین حالا وارد بت‌فوروارد شوید و هیجان واقعی گل یا پوچ را در یک رقابت آنلاین تجربه کنید.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r14
💻
@BetForward</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/79391" target="_blank">📅 11:03 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79390">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h8lz8nWSV8NALxphJT-0zCw4GxumKqaFpj3_aCB8R818-VbS9lXUtHS8EIjjSCerj7lXgjCVYf8SiNgO-sfuxfaAzrKcuS8p08lrE3a_kFmJFR4d5bKbSi-qVBoI9-6lf2MkkMWjQOs51dK_1jCnJjbt4voQGB79eBEYNMseYfd0J-KX2uqemeLX8dKIQ9KBIsyqHwfk_lGsB0GlssPxxlfMaZ-hMkrzAa6vo92_5Y2tzMary-2Ik3q-ClQuJkU0cV5LELi0aeVRtjswVN11lyP_SR5qi9ndSuCcTDI0jGDzw_qK2mR8ojaFqrAFzD52ZqkXcaVFnu5UyCdxql92lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینستا هم داره بامزه میشه ها
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79390" target="_blank">📅 10:30 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79389">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">چی میگههههههه این
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79389" target="_blank">📅 10:01 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79388">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">به جون خودم داور رو صفر کارت پاراگوئه بت زده بود</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79388" target="_blank">📅 02:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79384">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uXqXQk-0u7NyvFa-x3rKkgaYjznjKwCpUrYWZfzNc8PXZrejYRmsvUIcCE1RjPs7520e5envbcvdemR4-N9jx5iv7RIjnTKT59KyOGM4yGTF3GKwU3GZRb8nvqeqy0T3k8WuYylM0vIhisGXX2UrnBthIiCXEo6PL58GUItOrHzrnNfiQ-iBFQ7BKNtA0WPacMw45CAx2voHZsKw5CjHNtHRe_BF6puke34U3So6EqEdOmjSRg7H5aYkO9o2C9aeMCG7FS3Txo_NmTPNF2Wvh3bNGp3GUGsS9SE4OS2hTS0bcaSN4qapODSlx265L-vg6sgnfPwvj3sVRF02-dR06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببخشید دوستان یاد مانی هیست افتادم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79384" target="_blank">📅 00:48 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79383">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LI2C0goTWso7TAkbg-5I3dsybU75VXbdOTggzL90Qhp32UFm-Z-PY4KgV6b_2OXcdx8P3JtMZyboduLMEWUQpm0TmkijyNu-flRk2ng9yvl0TQ2scHRfGvSaXjb3qVbpiteKtsqsHcq6y8_C8G5pDyu1sGzQUyke9Pw3Y5JOxjRSlt0Oy4x5oEgSfvhJ2EFQfupBSINykA1ChykpiWpn_386-VcTJfYkk3QhMXBPdT22M63jiRsdwYTdX1W192_CrC1gXH1fe1RHm3nPEF5OMGHD-u9ncs2p9iM0s1agQsgZLGmMROoW0_Op3xFQK8eWqyfrabdPCr1-rN9peBrzAg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رپر ایرانی قبل از یه آهنگی که قراره نهایت دو ماه تو ماشین ملت پلی شه و بعدش به خاطرات بپیونده:
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/79383" target="_blank">📅 23:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79382">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T8mXC0Z-3omFoFhjaTq5hiCB8Cwt60gmU58-nkj4VghK5GJJhOCYL4LQo17GbqMqFZstsGzJu7Scz1qnEy4gdcqbhNDEnpZEtC-W7Ph7q_wY2f1bKtK5BlkQA3sEwLn6dC-_RnfrEIjGlBAcnG8IOzkJUlLiBsC9Ws2bS5mwV-OMkds5oWW7wHZMpshoyBleXat4Lu-TW7s1g4p_VIN1kmQwX9JTdSw1RVI8iuPhQBoQKp5RPBqqF7Y1NXGdI8Nt8mCV_yAUF7hticrnR-O7BX_m3ZHQFv48KjwBKYkd4YmmOAB2p2phRBaHU5P_BnlyeIn4yySIXImZayBj-aU7jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جور و بیداد کند عمر جوانان کوتاه
ای بزرگان وطن بهر خدا داد کنید
گر شد از جور شما خانهٔ موری ویران
خانهٔ خویش محال‌است که آباد کنید</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/79382" target="_blank">📅 23:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79381">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=OdsvR0npO37-ccoPZ03zGprmRfozc6L6Bo7XyawrfTAwyA0mdyDZQtvY6rDV47GsyyfetVZkCcaoHrVBI6x5uAcAZ78fKdePWoRJ4nleJE7gwc_0OSqiVPkOBgJi6DtT3sgYE02RBjfcfq1GiP3wcZ-H5SaOHAOg4KrXz-7X0LQW-Tq93Y6UWThVeHakZON9t8FYaue6OIxt5OcpzbSafsE33uYt2JxJSs2ZhgBYcr4mXpfj8geMfIrMsqliGjN2Bf412vZ-vnQWVdsNAWq82mne-tARcCue8jcZCwrcZdyliU-8eJzwEWobKROyOSXiYuZf6CxBZTSJj9djlR6zlw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0fc835849.mp4?token=OdsvR0npO37-ccoPZ03zGprmRfozc6L6Bo7XyawrfTAwyA0mdyDZQtvY6rDV47GsyyfetVZkCcaoHrVBI6x5uAcAZ78fKdePWoRJ4nleJE7gwc_0OSqiVPkOBgJi6DtT3sgYE02RBjfcfq1GiP3wcZ-H5SaOHAOg4KrXz-7X0LQW-Tq93Y6UWThVeHakZON9t8FYaue6OIxt5OcpzbSafsE33uYt2JxJSs2ZhgBYcr4mXpfj8geMfIrMsqliGjN2Bf412vZ-vnQWVdsNAWq82mne-tARcCue8jcZCwrcZdyliU-8eJzwEWobKROyOSXiYuZf6CxBZTSJj9djlR6zlw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینو
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/79381" target="_blank">📅 22:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79380">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">کانادا پاره شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79380" target="_blank">📅 22:32 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79379">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">مراکش با امید گل ۰.۰۹ جلوعه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/79379" target="_blank">📅 22:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79378">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">یه گل فوق العاده زد مراکش
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/79378" target="_blank">📅 21:44 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79377">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lCDef-CC8uIQV8ZPRgzATdyE2HcMqGfKQYn2i0qd0CjHCgzLokWxKknh1-RYjZAu7G8ux8tdw-Vxw406lpyYmAqKBcEFrbMvR9mIEMqPgOHL64D55nfp1523ycIpitZaTeNJOmXuiLYJ5qticwJi-OYm_YALPCPISEqULA_iMu5WRrWVVy-ob7uoC4nSh3B48Gg9mBr4KbvWnFSx1QofnXG5Y2k1x6SUch0779EwFuym6-vqxBnoT_LaowDQUl-98pfwAiBpjAApFZ6eBZLaJA4IgiJHMQZr18hZ8F6lR5bott4UIlAYuWjIyhQ8O_QjiClNuZNciFFgBC9G5jGxKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">امثال توماج عادت دارند دستی که برای کمک به سمتشون دراز شده رو گاز بگیرند
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/79377" target="_blank">📅 20:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79376">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rEY71Q8XBj6qWZmiT-JMYCpQJercyu5l6RsLKHXg6lEOBQJNPyx_vJxEoOpLM0stYggNUG1JmcLWs2q4ft9qoKQ-JAY4SqhVKSPfrb_dRIRfqrrKHsSg9Cg9HZ7czbKazt05k0bHndvPVHvV7Fq4VM3OnEbcPulWA4Mn-1W3zoeik1L12AdYRv6MqHl7bgcmGm7NjeiU0tu1I95-Km9tfa5IXNC_btSi3jzRRF7D29i51VUvNSyHY4d2viGrKcx8divQLS9Bn35oHu6eFP7e-8ze23uTeH4F3wqMALpJwpUkxyyl_N0PB6-Pl-ySRd-7mCP3Y1HgP_j0v4pO-upvbg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خودشه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79376" target="_blank">📅 20:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79373">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X0Druruygm2WOcxM3qyhF5CjKsL9QqlP-6bxc5sJrF3UKa2iRfIiVNZZHkpR4_RR-3tVUB4m0FfvCmWVcqiDN-MCb_bJmX8m-fJnKwVIZQdjsQuds53jfUOmjfsVmuH81oIKUbUGnFQgH62QPSgdSGwe2uIHAMXtERwKeCmbiNbnd-dcHE5O-rPI9IQPj_RnavmfERZMWjT1T-TLm8hcbECD3I4GjrIuKggi7N1rLqmCRdz0VSEz_2hhY1Dv2y5zsPjHfe2s3lz-8pptF4N4bA4C9AYc-bvK3M-JFcTaZD4vzKoA7AVpnhIHVq7Vam36m0P3g7CiR66s11RNVFgLRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">متین بامرام.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/79373" target="_blank">📅 19:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79372">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrqFDBs2LmdUqgm9R2wXohNf6ZXveT65_yeWFMZPgSj5_azyT5TVgwpkyS784ZfXv--ZfiutzwQmE2_1OFdk7qFxRTxYSE4RTzAOEJOM78-y0Lv6y34mJzz5aOByWgnC4IY3oHCQexWw_plFqy5iTbAlp2KoLX2p6UFlaYjSe-SBag1mUsjXcRa39dabxNUzUBz3x6d1_JO6HIKxMKMG86PfmPhhk_Bhch5Pa1y5DwmUvK9obbTzDXlvD6ljlJIq8Wv51VgcFdf9-7dobNtQl6WjJh-N1puwODS2UeYNbrajcUh9T0VMZfCN_0SO8y8yUH8qEXSiPd2TE3X2cScN4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید رضا پهلوی:
به نمایندگان خارجی حاضر در تهران که برای سوگواری بر سر دیکتاتور درگذشته ایران، علی خامنه‌ای، گرد هم آمده‌اید: ایران در حال سوگواری برای او نیست.
ایران برای بیش از ۴۰ هزار پسر و دختر که در تاریخ‌های ۸ و ۹ ژانویه توسط خامنه‌ای، قالیباف و ماشین سرکوب آن‌ها به قتل رسیدند، در سوگ است.
این رژیم، مقادیر هنگفتی از ثروت مردم ایران را صرف برگزاری این نمایش تبلیغاتی می‌کند، در حالی که هیچ یک از رهبران دموکرات در آن حضور نداشتند.
آنچه امروز می‌بینید، ملتی نیست که برای حاکم خود در غم و اندوه است. این ملتی است که پر از خشم عادلانه‌ای است، و این خشم و شجاعت قهرمانانه، بقایای این رژیم جنایتکار را سرنگون خواهد کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/79372" target="_blank">📅 18:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79369">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rCdMsCvNoi6I8eBoprVmBzeX_saQzgxpnvD3LLjz74D4VAZL90R4hQdBodO0mVx383ov4ENnBHQB3LOJSvqmXqHDc-Hisf4-VDv_wZ9Rz2tBqsnT-1L02va2kHOfJ-iMBZFwEPZec0EqmpaP022WRiv5Gf1BRQFlvuJ9YA9MXzVFawu8Qt7f-yalsERUWJH3ImS_JmaOVlKP3Ne4tkhJfIEBVg6F27737rEEzEDnZkXZpyeOzMYEDgSiCzyCv5DX6GVNEcUQoM8nAu65CjtEJivs7frni4NxEx1adKHhhtC8s8nQSRv-pIOwXLexJ7QI23T2r4VX1efGJLcea5UiJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوش مصنوعی اونقدرا که جَو می‌دن باهوش و فهمیده نیست واقعا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/79369" target="_blank">📅 18:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79368">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الان تو مراسم یهو یه پرده بزرگ و ضخیم اومد جلوی تابوت حضرت آقا، ما شروع به اعتراض کردیم که این چه وضعشه چرا تابوت رو از ما پنهان می‌کنید؟
💔
💔
💔
که مجری برامون توضیح داد به دلیل تابش آفتاب و وضعیت خیلی خاص پیکر حضرت آقا، مجبوریم فقط چند دقیقه تابوت رو به نمایش بذاریم و دوباره شب ساعت ۸ پرده‌ها کنار می‌رن تا دوباره بتونید جلوه‌ی نورانی این تابوت‌ها رو ببینید.
ما هم نگرانیمون برطرف شد و آروم شدیم:)))
🫠
🫠
🫠
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/79368" target="_blank">📅 17:47 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79367">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">العربیه الحدث:
دور جدید مذاکرات ایران و آمریکا ۲۰ تیر (یک روز بعد از تدفین رهبر شهیدمان
💔
) بین ویتکاف و کوشنر و باقرشاه و پروفسور عراقچی برگزار خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/79367" target="_blank">📅 17:27 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79366">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم  می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/79366" target="_blank">📅 17:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79365">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=fmRiwKAKYc-T29QrFyCXgJ4w70k0g3E9gszhvZbA15JEepq5Beo4gFY39jUBf4RSqT8Za5UpGS1tKPTyXpXGrgCvDmRqEawn4Wo_8g4wg4C77HBYvsUfep3XIQ43wW-gw_Tc8I5XTdpf5pURKhI85LvVSMC_rpy37plPx5_uFbxIumz53l5UDPqG8Rzr2jnDdymiRIT1ZNXyQh7I4fLh4RZ543bA0EHGRZUG1WmMTxj63pjOKfGHBWB6PJUk_wGH4KtS4VcGhtRBxwKzrB2fWdT7ERN-xodIwSmRX46jPU_vDsH3fpIdYHYgMVSgw9kXSwel0CsTHHVNjagiu6kXPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c8f58be43.mp4?token=fmRiwKAKYc-T29QrFyCXgJ4w70k0g3E9gszhvZbA15JEepq5Beo4gFY39jUBf4RSqT8Za5UpGS1tKPTyXpXGrgCvDmRqEawn4Wo_8g4wg4C77HBYvsUfep3XIQ43wW-gw_Tc8I5XTdpf5pURKhI85LvVSMC_rpy37plPx5_uFbxIumz53l5UDPqG8Rzr2jnDdymiRIT1ZNXyQh7I4fLh4RZ543bA0EHGRZUG1WmMTxj63pjOKfGHBWB6PJUk_wGH4KtS4VcGhtRBxwKzrB2fWdT7ERN-xodIwSmRX46jPU_vDsH3fpIdYHYgMVSgw9kXSwel0CsTHHVNjagiu6kXPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام ببخشید من تازه آنلاین شدم
می‌خواستم بدونم خدایی نکرده اتفاقی افتاده این عزیزان اینجوری ناراحت شدن؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/79365" target="_blank">📅 16:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79364">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">خبر اختصاصی ایران اینترنشنال: مسعود پزشکیان استعفا داد  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79364" target="_blank">📅 15:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79363">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBIEnzEgna71H9s4TMd_MaQCf7Ate-MDYgZItE3TSGh3Xj66L3bX2uUYb8xtdWGYS7yZkKzVVMK_yLfWaOBJ51a3UIuOE1UxLmf0yHNhMsOaAxd3lzsXwlQO6_NS2DZqug0ncKkUam0SCso-9HgAXZ5M-fP_TnjxF2VzF7P028TBDhDD05osTipjm0zX2LmOLAVSycNT_JbT1tO6cz1MqWiziQrMmXyEwY8qzhQgSRyNmgTZ4OGJO0kTnZMs95ypGShuXro0NQ1u9D91YmX93kZDzSz7PBWmnILYh8hBHRtZVNdVOR2J8tPT8R4rn8taZsdSelUslwdHJ-DmWPkk7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو جنگ ۴۰ روزه سپاه در ازای هر یدونه موشکی که به اسرائیل می‌زد رندوم ۱۲ تا موشک و پهپاد می‌زد تو کردستان عراق.
بعد الان رئیس اقلیم کردستان برا تشییع اومده ایران و چنین شاهکاری رو خلق کرده.
من هر چی بخوام بگم فحش می‌خورم برا همین صرفا به این بسنده می‌کنم که ببینید ترامپ عجب نابغه‌ی درجه یکیه که به اینا کاملا اعتماد کرد اون همه تجهیزات رو راحت داد دستشون.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79363" target="_blank">📅 15:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79362">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/stCqDXE-WncLz4Dwb-GlRDL5hBcl8gmQ0ebsqfVg5mnKceBW9Fw4i2LNQC7Ii4PSvJiSsxQ8ZlqtwZyQMhUxbs_blo7GF7Upugr4CzKSt1HtuAgTLmk0LULGLbRwD0nraY3EES2t3-Kmq50uxnpMg6a6yakE4AH-0xbLXHwpr5aYa-c7NL7f-8L5T6LpB3SfjOqo54DC2qgeEbKxiMs_caPr5bBIms96W1DDzplUsu-s6BdfTBRywTVcNGsEHV6sRqpF_o4MHC7fDI-W4RjJBzQynIwAoYpfRmJZaLoH_dJnL7KLZQDWE1-tKuxvFXzXP9ZLNeKU76Ln-YKxC-KPYQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
تسلیت به پدیده به کون ها
دریک رو صعود مراکش بت زده، کپشن زده که میخواد از نحس بودنش به نفع کانادا استفاده کنه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79362" target="_blank">📅 15:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79361">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">۱۴۱۱ هم دکی پول ویناکو پس میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/79361" target="_blank">📅 14:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79360">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YBHly77HcjXNOdolC4Xxq_sm9xQYXHF6BfzYgTLjfTsvIQ_wKmL-YQEsHNaMJ1VqDhEZKBW-66aIOSM03sLMoK7pMfiZCpbKAZJShUW8EgqMFhdB8WqRNdEJg-y7BUSPiwZw6OGRcjKPsjuEAgr9bd8oNuUHqdDXvbtwIAwKhJ8WaMZQ2g58IMVvmlrp6oQQJeXNr_WHaEsrljCGy6fAo0myT16fgLYyovVbHJqQoKVqU4m2vk1tsC7vYSvn_tQytaXmNfr9ObbI1CBEoaEcw1UsGAmQuZCU9uFIim8aqQKPWTOC5QGuJac1w24oKxlkr8OG7Q-d2KsuLKhPzpkfmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره، سال ۱۴۱۰ هم امام زمان ظهور میکنه رضا پهلوی حکومتو تحویل امام زمان میده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/79360" target="_blank">📅 14:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79359">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pJ5dz5BhwsN6cn3mUqNCQyQm44kqplY4b-H57hKnRjVs6SwhRve-IrHX19XQ8Uy1wollzX4zT3KGPbxtwoz3grAf0YKt65mztcSRJSHSyhE9-XJTkUn-zTasjwZCtR5H53VS5Y6pAmz4qcjnzsFd8a-OOPJdinpEb0KyA6zbLcjIQgeOWSnf7vrsnTUHoVJ7D0ELB4QLyTBtqrYHke1xC3xePuiU8YX0G0OMD8OwXzGSq6Ul66yMMMkrSQHdLR86oCQENmBQuIteRItus0xMEggkWD3Y5n-jJnRvmMYJUUMF4lf2hRnCG5m--PUbydzbxWH-7o4yfIwnyqcRqgETBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فلش نمی‌زد فکرم هزار جا میرفت
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/79359" target="_blank">📅 14:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79357">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">توماج صالحی از امثال شهبازی هم بیناموس تره
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/79357" target="_blank">📅 13:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79355">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SXTnJldW39Sqb_69Tlmo_8CWfSnDK2FvER5NTxkslOd2KRIrXB7fP94vA_kavnthX7vg8EWaBLRK9ay_iTC8WM-tJ6px_w8KWYeDNycrKl5jcOBlXeiyNkXc3fNF_KOi4e29_2-uTx6Cy4BtnAoISxeV_FgYSOGDRhtkzkE5I4b4bhgOX6i99QQwG_5xNriRiXbi4Jg5TxQuD0Flzg20yah9xwj17Em0CvOSkh8nlrrKTOPoC6kUOM0gLPzg4VFimjzeHT1_70Uh3SeCwLwhYwBu6QQUqvPmpnETa2ivVGsBCqWx5PGfub4ulk305waNasKhbBICi4r2vxJwddmIEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AeVG8uUQ0HKRo_nUBtMb7w7otXq4T6DGOqZHLxM6ua3HKaW4qqFioRQ0KkVccIv0yLLqOk3zHQgnqUVzZn0xkIgUkqyi3NhKoRVU1HYb8TH0uh_zfCbbSmMcaYKk7oyn_ZTj72_KSXe1c2cpn0IzP39rd7iVdjGcgE0jMInveTqAac2VKyfVP3GRqjw5Lc3PbNOSQ6pYg2rDguY3tjPGz5FdTFLmKKs4HHrToNWc7BEZ6NN-JBm1vi2iwaPKBMR4G-W8yYh4q9hxOVRQuNGxJsquVuLsEIx83k-8qZSgNtu6_zntwCF1SIfTXa5ZKL67M9ct833Mbfk2fwUh6nXrtA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تو ژاپن کاملا قانونیه که خودخواسته کاملا ناپدید بشید و یه سری کمپانی وجود داره که بهتون کمک می‌کنه که هر نشونه‌ای که از خودتون و زندگی قبلیتون رو‌ پاک کنید و با هویت جدید زندگی کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/79355" target="_blank">📅 12:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79354">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:  https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/79354" target="_blank">📅 12:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79353">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">کصشعر نگید پاشید بیایید چنل آنالیزم میخوام پولاتونو بگا بدم:
https://t.me/TemSahbet</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79353" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79350">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مسی چندسال جوون تر بود چه رقابتی میشد رقابت امباپه و مسی</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/79350" target="_blank">📅 12:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79349">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">ما نخواییم کشورمون ۴ فصل باشه کیو باید ببینیم
پختیم بابا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/79349" target="_blank">📅 12:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79348">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">کی قراره قبول کنید از وقتی تیما ایتالیایی افت کردن کیر رفت تو فوتبال
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/79348" target="_blank">📅 11:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79347">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uZyxIRO8yoJA37STGy-IibkHYIx0tRQg1I-g3ZDuCIZDmvw1JHgl3CBT-7p2zVXMMLSjtqT4xUpugoclrB7wyUiNBTjsyd_EfY-cJSOLwb0DgUOx38WvphcVxI4O4ljvwGm91qFD_QuYLKdAaHQUfMorNyGoE2OZoAorhwnuRvY2fedLWXIx9wVzDLgBpI8WeXQTA41UF-Lgzi9WYIzF2d84qGH9TfZf2byb57f6c5F_Emc_BQoxRZtc3TtIbBMFS3y1bABiUrk0_Fuzc8nchm5ndjlKRyjnLtx1qlPXwdr_VpPIY7cxmrReMkgd0XwIcx5wAx70ce99sER_yGe5MA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب بازی مصر و استرالیا خیلی عجیب بود، یهو استرالیا برا پنالتی گلرشو تعویض کرد، گفتم دیگه هیچی سوپرایزم نمیکنه که چشمم خورد به بازیکنا مصر که داشتن قبل پنالتی هایلایت بازیا رئالو میدیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/79347" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79344">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OOgyrtmcrUUpFrrjXEBD8z10jGJCd1926BVuWiK5mhgzErr9gdfTk7MUtl1nUWWcSnsysOw2rhLihg2U4di0hwtPLv66faTwMKR2ep1Cv1tDz89LzL15B3Og09hzbgHiLWmwWHy8rmYp5UynMZ9sfPW5Z2BRIarYBF8sQdrzsEOl2S9P7xIKsdCKOQRwMaQBIjIyBPNC-OUjQ6hlKeU7zYmoJsFl2WvzP-YxVBT-z4A6cocvcruisyiHsneR5ni6e3R3D5Q0Jq_vVKRAKvxGXxIsePLm3adu0y2owWjaxpYUxurRr59PQIpuNfqnvuGCaUeliExuEVh9a23vErm3uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ببین حرامز
هم آرژانتین برد و صعود کرد، هم مسی گل زد و هم تیم کشورت یعنی غنا باخت و حذف شد و این یعنی به فاصله چند ساعت سه تا کیر خیلی گنده خوردی.
به نظرم الان وقتشه بری صورتت رو بشوری و یه عنوان آخرین جادوت سعی کنی یه وردی چیزی بخونی که مردم جایی تو خیابون دیدنت فقط یه دور به قیافه‌ت بخندن و دیگه دلقک بازیات و کیر شدنات یادشون نباشه که یه دور دیگه به اونا هم بخندن.
موفق باشی
❤️
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/79344" target="_blank">📅 08:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79343">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/af167dceef.mp4?token=fbwoO-AKSLYDsFy3y15D41hXqBaeqGO-gkox5aqXxoB0m9plsJ0RlfgHazaI0LI3d5gzZZXGirp_ZGXQ0iEonRWf7rtc8OVmrzvvqzZdf-S6az8sDpJukOK1QA57GgwbF8G9Yx6Fd811JmSkFOQtt6ULbCvLPbCDPgemjE9zr97Eh64e7R5OZvstnWIn1Wv_uKMF6dPzh6vaFio4KrykZ1ZzGGPbl8phAymYZ5HmFLZFrErh-CTxc5aASYWCui7GOIhD6lfJhpGMi2GY4Za3VLb5mn61mNL_BoV92nswarWRmxWtdwAs6NPZptNrowwm3PWxf-LIKsMMkoWR72TVEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/af167dceef.mp4?token=fbwoO-AKSLYDsFy3y15D41hXqBaeqGO-gkox5aqXxoB0m9plsJ0RlfgHazaI0LI3d5gzZZXGirp_ZGXQ0iEonRWf7rtc8OVmrzvvqzZdf-S6az8sDpJukOK1QA57GgwbF8G9Yx6Fd811JmSkFOQtt6ULbCvLPbCDPgemjE9zr97Eh64e7R5OZvstnWIn1Wv_uKMF6dPzh6vaFio4KrykZ1ZzGGPbl8phAymYZ5HmFLZFrErh-CTxc5aASYWCui7GOIhD6lfJhpGMi2GY4Za3VLb5mn61mNL_BoV92nswarWRmxWtdwAs6NPZptNrowwm3PWxf-LIKsMMkoWR72TVEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سلام صبح زیباتون بخیر. 2
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/79343" target="_blank">📅 07:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79342">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">پروردگار بی همتای فوتبال، حضرت لیونل مسی بهترین بازیکن زمین شد
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/79342" target="_blank">📅 04:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79341">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/171cc02113.mp4?token=BHc6FXKh8vEm0eGZU1W2-cqDx2e5ZxMnpHIPkVZy-cBKLeUXnwvv1XdtAgkRJ2Ophr3xA6h2ElHUebYjOQqUdYp4z4nxVkT2av-eEgpbfutCYLz2LiCzZWWXLllPbeRTEx96OTvv23GN2cpxgoD5ZmfQmetlWNMlcplfaGxeiiShrEdopBCccx6Z8wWLYpif9GeOOUI-ipGzeoq8PBzz2A6P-1QRj6jdMUDBtpCFMDCiHPtBJEwWDX_oK4yRxAiv_tq0xwsGs63uCurfipFLq5BrIYlWO7PImKz5Q_cXEIw1SKmMEWDWI2k56odWArZBp8o5gbETVVkV-yncM63Z5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/171cc02113.mp4?token=BHc6FXKh8vEm0eGZU1W2-cqDx2e5ZxMnpHIPkVZy-cBKLeUXnwvv1XdtAgkRJ2Ophr3xA6h2ElHUebYjOQqUdYp4z4nxVkT2av-eEgpbfutCYLz2LiCzZWWXLllPbeRTEx96OTvv23GN2cpxgoD5ZmfQmetlWNMlcplfaGxeiiShrEdopBCccx6Z8wWLYpif9GeOOUI-ipGzeoq8PBzz2A6P-1QRj6jdMUDBtpCFMDCiHPtBJEwWDX_oK4yRxAiv_tq0xwsGs63uCurfipFLq5BrIYlWO7PImKz5Q_cXEIw1SKmMEWDWI2k56odWArZBp8o5gbETVVkV-yncM63Z5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جادگر کصکش من الان اینو چیکار کنم؟
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/79341" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79340">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">تمام ارژانتین صعود کرد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79340" target="_blank">📅 04:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-79330">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">جادوگر بیناموس چیشد پس</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/79330" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
