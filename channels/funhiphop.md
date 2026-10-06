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
<img src="https://cdn4.telesco.pe/file/NCpguSLUrZnZg9KR1pqg7bTN9QTlBwtXtrr7ymrnvDI7NyxcPiyqorqxCxH1CGoLDTBZI_5pTV9_28DZOLD6IhSNVJiWpgqc9xdSqRmSBaI-UrwXyO60d0scnLXeS7uIAAFnk9aho3TJeYXdgFxB2zFORXP4NS-eRFuUi6KXs0JMtFiwEz5fD9QuO6nn3dynE-qWiZjP3V7NT2h0nIm5PEozOIJxEVUdkaTU8qc44PJbkpUrgIgQo9vE040FmD-4FYPBTajAvCoZKA3XWif_tuuAbNylQJZEpID6bwEPCLoHKFnfjKi8mVmWwBCeUSF4jof9_6-jL55Lq_APclE3cA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 260K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-14 10:14:23</div>
<hr>

<div class="tg-post" id="msg-84484">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">رئیس پلیس تهران بزرگ: از این پس قلیان و موسیقی زنده در کافه‌های تهران ممنوع است و با ارائه دهندگان برخورد میشود
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 2.3K · <a href="https://t.me/funhiphop/84484" target="_blank">📅 09:55 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84483">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/84483" target="_blank">📅 06:54 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84482">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">سلام، پاشید برید مدرسه+دانشگاه بدبختا</div>
<div class="tg-footer">👁️ 8.8K · <a href="https://t.me/funhiphop/84482" target="_blank">📅 06:52 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84481">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NeJw-n-VPzEQ6F7TNvX6lVsphhDYBGjEeZRzlkQfkz6Fs87ObCsWv-H8i7vUfeikY02Zhu0UHR_w2PnDQxD0G-B1uehaKzfKkBkn_Ng159MqFb-3pd045iu2I18SLNGUBmwaRqRFNUS2a8Qtp3yixizPe-H3rGoi2u4aVWqkzadUncOA_f7eINlovlsixqGeUio3ieliTGbBSAPz2ClH4qKpJve2iERyeEXJgSNND7tGWczap0gGS_g7qZrva1YeGL_Z_99dMT-N5s9uYBywX0iAiroIQYzr3uZUFJ6MVEVMxLzP1sahOPg2UBggYFjqU2cRcFZu_kXJbDoDRnaNnQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثیا که نیروهوایی ندارن بالگرد آمریکایی چطور در نزدیکی های دریای سرخ بعد از کد اضطراری ۷۷۰۰ سقوط کرده؟
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84481" target="_blank">📅 01:27 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84479">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/T4SbkL9FmyOdb2Z1Ftz9jPZEafyxmgvGE_0jZFaW9G2unaa8wyOS7y8VIRbXSH89W6HZSIIBcM8y9yejl_fzmbi4fLh6kt9zzpTr6-lCQEAnrLJ3IVTOh7rO16QCkFwamlyqIRGLKeJ4IIoKQnUG7MdIZ2rfgynP_3JVPwxwTUdUUCUpUib_xscpv64e36bZhdQIaYJue7Tbd21glZyXry0hmGb4GPE5oIqy8rY4G1YR0bvhldU-zTIvsAKqZZo19Ub09NqIKvWfV3yInsoivpetxIlXXnU4_06k6nccv3f2fsdb8uJWoPp-YQRXgomt6GBf9yCXzkupJ4YnnJEc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/DPlaZwQKplvkAnr4oXnOkh1JU2oojidhQXonwyqqr61vIj88F2DcfQq_Or2rXiUBOX_SCJidvQV_Fu2iWFo5jr3rgucMo-b4D7fdI86vJKOmtBI_-DI__7Un4gnBy-L4RgWowZEoHwzuaSYFZ-eBnxe_YoFCCHPsi5zH3JDFACvhndz9vsFk4eH3fLL2fqcXl6Z4tUkd5rlsOz68iTrl5ePkxTNnhZpYowajPK3RiUgsoSSufJsMN_uEgh9gHMBXi3dN0DTrUHuvsBKconwCu8g8DcWbG-a26TwiUGBxc2F1cEOub3HaV--cvH79327p4j6ouynKq67TF-lMseOX_A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بهترین وینگرای جهان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84479" target="_blank">📅 00:38 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84478">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/84478" target="_blank">📅 00:20 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84475">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اولیسه واقعا خداست، دلیل این که فنای بارسا ازش بدشون میادو نمیفهمم، بازیکن رئالم نیست بگی از رو تعصبه</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84475" target="_blank">📅 00:03 · 14 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84474">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n6pYsFLrHwBq6Xu7bpdSPdHMJMS5PfJLmBeh5dpH0NoC6UO3pQLM5o9z0WaGwpwrpWs3aEo8asryeyFujMmsW0w5KISHQmJWafQV1rYTuxbyqbEHIGL2_tHWlqS9Huwrx5VleoWeLBWQxPpTUpRM1kTOEWF9zddynhGaWFDHizTxUCMSFJbfW8FX-luJ6Xpe78yZKYjeUeHA9a4pMTtbhhwd11zaTbFWsfM6mke2WClPzYSEPOWg_uvhFj-CQ_ZW_L_kyBrI5wQ3O1Fu-Qztlh2PVPTom5rVzy2At2mllSBwxYlmjz5_orwQXggbH7_cbvgOPi1XT2_nXgF5k3r12g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پسر تنها کسی که شبیه آدمیزاده بنیامینه که اونم فعال رپفارسی نیست
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84474" target="_blank">📅 23:15 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84473">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ:
معتقدم ایران در تلاش برای ربودن هواپیمای «فلای‌دبی» که عازم دبی بود، نقش دارد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84473" target="_blank">📅 23:12 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84472">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">ویدیوی وایرال شده از شهر شلخوفِ روسیه مبتلا به طاعون تو سیبری که نشون میده چندین نفر با لباس‌های محافظ و مخصوص، تو شهر درحال رفت‌و‌آمد هستن؛ اینطور که میگن در حال حاضر بیمارستان قرنطینه شده و داروخانه‌ها هم آنتی بیوتیک‌هاشون تمام شده. @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84472" target="_blank">📅 23:07 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84471">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b249c59827.mp4?token=MfXMPfv-dEOrmDIWTL1iOspRuUj9EXO-gtP7_Uyk_ajJyQLFxF_WcKPorFr_nFVXGW9e6n7KSQGXVuVAswooD6X12Ov9Rr91k0pKx8aC0lr6bxmE5aMvUJpuINTkIXnDy3ibN7vYen8dbCZZoWm-DJZxVvnnXt4QbWERGeRHLNf2U_InUt6V9qfmBGwd4Y7xJR9F37VpisrFThPRTU8JR4YVenJeeW0UfAx639sjhgbzCbkQfR82QAXNbxYx24s2ZOzLLmR935nA_m43ak-7CpDyyW3dBXVZlcRLyfuLCEmwNmNJJGurgbmgAYGaC2wTxBD9ajehe_vCTPmZWiPU5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b249c59827.mp4?token=MfXMPfv-dEOrmDIWTL1iOspRuUj9EXO-gtP7_Uyk_ajJyQLFxF_WcKPorFr_nFVXGW9e6n7KSQGXVuVAswooD6X12Ov9Rr91k0pKx8aC0lr6bxmE5aMvUJpuINTkIXnDy3ibN7vYen8dbCZZoWm-DJZxVvnnXt4QbWERGeRHLNf2U_InUt6V9qfmBGwd4Y7xJR9F37VpisrFThPRTU8JR4YVenJeeW0UfAx639sjhgbzCbkQfR82QAXNbxYx24s2ZOzLLmR935nA_m43ak-7CpDyyW3dBXVZlcRLyfuLCEmwNmNJJGurgbmgAYGaC2wTxBD9ajehe_vCTPmZWiPU5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84471" target="_blank">📅 22:40 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84470">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">این لوکاکو چرا نمیمیره</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/84470" target="_blank">📅 22:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84469">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=sQbeQyTKRPNIbco0CcHNb9FonD29JuFiY0Wa92FgMR0WPQpleWxA199al7qyDVaENLiWIJ26i9U65kwLlzV11fl-DzGo_FTKKAYlKI_2Td3JESFjmwdoDrBdBM19QmUXA0r9iZ3V_0cHwT0YLfg98_m84QBXM43kIh8QXxbQWrfkqKZLSPbo5WEqgeAbcJ8xb608XOk9LJRtkGonoJMUOU2L7NrQRhleNuOYSmaq5UeXsgVNYQMm8soX7MBgTwh-t2kwXiXWhW-A3du-MyZqw014vmQ0QUIv_xFNxiJRDcd7ZLO4h8rTllExW9zo9czIRvIC7BSP5O0P6K5USgHfag" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbed26b887.mp4?token=sQbeQyTKRPNIbco0CcHNb9FonD29JuFiY0Wa92FgMR0WPQpleWxA199al7qyDVaENLiWIJ26i9U65kwLlzV11fl-DzGo_FTKKAYlKI_2Td3JESFjmwdoDrBdBM19QmUXA0r9iZ3V_0cHwT0YLfg98_m84QBXM43kIh8QXxbQWrfkqKZLSPbo5WEqgeAbcJ8xb608XOk9LJRtkGonoJMUOU2L7NrQRhleNuOYSmaq5UeXsgVNYQMm8soX7MBgTwh-t2kwXiXWhW-A3du-MyZqw014vmQ0QUIv_xFNxiJRDcd7ZLO4h8rTllExW9zo9czIRvIC7BSP5O0P6K5USgHfag" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">با یه پست رپی ناب روزمون رو شروع کنیم  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84469" target="_blank">📅 21:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84468">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خیلی دوس دارم بدونم اینایی که از رپ دنبال محتوا ان تو باشگاه چی گوش میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84468" target="_blank">📅 21:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84467">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">منو برگردونین به اونزمان که تنها دغدغمون این بود که حصین زد یا فدایی
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84467" target="_blank">📅 21:19 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84466">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">LCPV</div>
  <div class="tg-doc-extra">Creator (ft sahar)</div>
</div>
<a href="https://t.me/funhiphop/84466" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84466" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84465">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g8eiY__tb4KfHpmDP6Vm8L36Lu4Pbvs5B-gIxjnTBDDA7C8Fw4TC37H4sdavTSAd6ktNUjA91Y8iBzsqKsTo05-xq1Gy9NetD6JndR977dRjQ854-y4Gc8K1sZiFyr1ER-xiPzFVg5TbGlMZ_N7gWAnEfZdQcnuIueWxciju-aKWXd1VJQ4bydO1-ew_7rOfbtwtZjui3CGw37RxRq5iyq3Z_9lvx0c_KHSTVa9iGuPmAzFXDyXU1OqEZTfzAh8jMkyo9fwnOUCbPT945FbP40pyYA1yF61s28VTKQRypAyzFLUQpJ9OV9jYcA0-e5mhoBtvOE24gC_H_cDuHO9syA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator بنام "ال سی پیوی" منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84465" target="_blank">📅 21:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84461">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ruZ1sHJlf8k8SyRHqLE0LM_vD7HynpcRUApKvOFqPhU6HAAcblB0AldHSu_bbq-biox3mFo6YfVOCZStkVXDCDHb3OKvcarWRVNKOgYLr29IiMO5TVxqTfxqZkZJM-7IqxQdTH_BlpyDQPQeoNxeh_IFlUbqTBz_mLRaOM21fmY-emC6BuKdmsa3ZDu31Lm-tBj304V5cxLYSiDK-v2zhl3njMzuyP6xHGyLhJWOX77rKUn9IBYyzjQ37oRtNLLjdwmiyzxIJKQq6nr6oTUJVtd5o-kgK3qiNSdUhqw6VRnjRWvV99Gahh6D8Ak2mJxYYJLwtISV94HgizcluQ_ZtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rkMjlFvO4iXpWGvF9zV8SpJZd5fgzo88GlZV5McSerQVOjrcT1_AXkPkesPp6aoqOj_V-PSDtwrFnlYnFd1hjWgnOtq-A2jHey6LkT3E58LSZpTyX5YqKn785Uzc5kmACJZR-EjhRFptrsxCA-3CInE4FPavsVcabjL9SWVGZvDPYUBSl-P5FEGX_pvLC9WndZanY1ZFQijxINpLVvhBoA6HfKRMRjujb3rszTm1sJBXoDOsNs_WUgZJfRTmNzljuEDfqAhnOCalhLpfthHHxI3PQKX1ztiRCnR9JhMtzL3cWjcnYthg8TSbey5EmegQ1mKgyhVMOGP7PhQHwkrmLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uLyrbk0AS2VD4yqiaWA4dPzyQZapKyl0rV35ZbKTGqzbHf280qS1nD7JOBPMM7sNAlIXo5uDq9YMRRUKrGUDNHTL5AC_hPUiV59srFPzAzdavfIfK3aoyeiCyMAUxNPi0bMm0Gtl_F5leENSef0p8QegWW4M1VF1uoQtEROPrgGDYAD1cx8lqfqzDoovMc83wyNqUAoAIT21OYNnDne3sSxoyZKVji_ss2OP4V4Cfwz23zt93jLhHtifAATODI0CnLAaHW8HWq2y--HOx8M5oFa7Ft6ya_dcgJTvsJzvpD_zKR_tZyWTLZ_7_BVkcpg0JFcX4uQBvZAZvZ8rxVwLNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YKT14pcp1x7gCSjtMkr7y8dnuoX7B2YcpVPLlkJ85QNCI_g3IQpwMDdOWZ7IlDsi9TFQPZLoy1yYFVStFLp-UDMv0RHoX90pOAcNedJh4MffQxoDn17pwTheL62A1pLp4npDjOT6dM437UvXejlll6kLAw7PXa-IvIxFkORAHNqdESVl3nymQ_j27QVoeZBuAr7Fk9-U4egJ8e88lxql_-R_bZAxnRkXf3s6btyC8U6pWwhy55CkSVOJnILsKWudtFyk9REc_K9SnpyDXxFUZI0Lg56oLnKYEXkGGCS2Osw6vJ8xE0NXUO90K1HBpNynReW7LOT3A-4opGTwO42wyw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">کلیشه برعکس و اینجور پستا تو اینستا زیاد شده و دخترا با این ترند حال میکنن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/84461" target="_blank">📅 20:58 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84460">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">دکتر مسعود پزشکیان:
تاکنون، آمریکایی‌ها سه بار پس از مذاکرات به ما حمله کرده‌اند و این نشان می‌دهد که آنها به دنبال گفتگو نیستند؛ بلکه هدفشان سرنگونی نظام جمهوری اسلامی ایران است.
حمله آمریکا به ایران، که با هدف سرنگونی نظام صورت گرفته، فقط باعث اتحاد بیشتر در میان مردم شده است و ان‌شاءالله، این ماییم که از این دوره سر بلند بیرون خواهیم آمد.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84460" target="_blank">📅 20:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84458">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromFarz!N</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OkaIaxw9nAdh1Jkdwx8Cx8w-LB2zyK4X3AUjzVKtm1Fp6rk86gnJ_thJyoQAvnEOkLCtJExKEYlYVqdIHXYlCkzMg6_s8jchDnu4c3cIuCp-aqR3IskA1jjT73e17EbXtfpgtdit4Af9msKaJ5jxgP1mtT4ImbN9Dri0TGl0q-l0TE8VZUmhFYaVfMndaoK4G2EFFIcHwvDL9-N5zKVlBRIChIHZlnJQyeMqiQDW7yPnqC3bP5ho3X9cBs5CV4yxdk9cGHz4ia34AIaajV__mCkj1H-9vmsVXtZgUdp-DlfPo4Ji74KC3r6OMOTNh7tGKarL6vQWvfgbQ-Gt22jhuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بنازم بدهکار شدم</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/84458" target="_blank">📅 20:25 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84457">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/84457" target="_blank">📅 20:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84453">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=eZTC7blSe-2yv0xFv3bfB0GpUgcQ-u9LpnLUkwF5AjMqtyo6GLYZd_iwSAkFI6DGdwQDk43udnEVv-2QYWAKcSy_RUVVEuR08ChCXzpE0igwmCq6bFPv8LeQoCMdCWRTjbV-APn82QmLWR-5gUAMzpNv4pI_s9JkotMU3k4lDKl6UQsm6XuvCDBdTiluxCS87FHqNGu2X9ehNcXSJMd5RGTHEMKd7jTpMuoEuQ7W3bIfJbM8DNmMA2ThwjLpPP2cXwldTvTCCVCc2-saTS5Eu2jLmtxkDDSsGz4IGVOWLrWoSVFhJJcPyWj4dN5SNz1SchEQGHfnecq9nyzGkZNLiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e122cdcfbe.mp4?token=eZTC7blSe-2yv0xFv3bfB0GpUgcQ-u9LpnLUkwF5AjMqtyo6GLYZd_iwSAkFI6DGdwQDk43udnEVv-2QYWAKcSy_RUVVEuR08ChCXzpE0igwmCq6bFPv8LeQoCMdCWRTjbV-APn82QmLWR-5gUAMzpNv4pI_s9JkotMU3k4lDKl6UQsm6XuvCDBdTiluxCS87FHqNGu2X9ehNcXSJMd5RGTHEMKd7jTpMuoEuQ7W3bIfJbM8DNmMA2ThwjLpPP2cXwldTvTCCVCc2-saTS5Eu2jLmtxkDDSsGz4IGVOWLrWoSVFhJJcPyWj4dN5SNz1SchEQGHfnecq9nyzGkZNLiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش یمن داره حوثی هارو با ماشین زیر میکنه و میندازه تو دریا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84453" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84452">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/84452" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84451">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/esQfisaHq2SHkeJPl8T-tO3WqotA9Ui2LpApJkyhE6-Uwg_xLUAhNa5JOCgnAWXhXZ60Vo-y0tWmOvwp41ikLUUCCtLs-qim2j1Jfd5OnjOKGe6HfA1CrCgsDB2_ZuXyu1P0Y536EfXV6NfsIeHf0PH19l-6A_syKhRd-tC9QFzx3L_Az3O74SEaENFVvHDW0jeQpaMoWCxkPn7T13BjCkO29WOqAI4ZsHF4S_lV4HrRh1UZmqUGyaNszrXgcqxQRbK6fZ2TKhoi2ymLJyzsNihNnxkJh-f8y-ttnxrThUFR88aDn_gL5JUMAwpAG73Jtl0H-P7dq4s891bA3KlMiA.jpg" alt="photo" loading="lazy"/></div>
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
G13
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/84451" target="_blank">📅 19:46 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84450">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">پسر خاورمیانه به روزی افتاده که تو نسخه بدون جنگش روزی ۸۰تا نقطه مورد اصابت موشک و پهپاد قرار میگیرن، وای به روزی که جنگ دوباره شروع شه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/84450" target="_blank">📅 18:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84449">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVkOREXULZjcHU2pl7DYyLEJWHzd7IgTjBdup3yyJjfpPJold7cuZHNCgVbD81trz8dDr6kMXSd-4QVVqH5uV_0J3ViwC5VUOR381wp1foRcSPLrLaYT7gSt77ZCMYbLik-mfgEaynLI5BJnOtQHpHQE8ALFLtz9vWpPO63pY9OhDMJX2lscnAeEF68nmMt1pHnccAVFKtk05Nngo-ZH7bKs5t8_TP-RqY28CrcuIFboXYDRl_nPvJJyC8p-bmpyWHf1BGs1BddnltJlKPsfaNFQZxIKxtVZHSjAd6w2ObBCPTGR-YO7U87ustRQswvGLteaQ81vhhjMk2sZt5vCXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">منوچهر عاقل ترین فردیه که تو توییتر دیدم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84449" target="_blank">📅 18:14 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84448">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUryIaHRddJoWFCCmz-8OxKGvnSZhiOJ2mNutZJr-LS_mDgPO5DX3slkvg3cygZdUxcJeV5M90svvPFbjtyaCCMIZxdImv5nVvz7UIU6i9mcWr3KNU_K4tl90UEWCnUPC4fNuc7_t7i_3SpzD5Mp2JESGo6wecpwfUuV5Zc1cBopW71Zxaexk5oRYO7i5MifUqSHvK3W09nDMcyRLle-_bQfe6MroxlMhGmsuamv-sHJckyPLRkoaZ4Co5qRIB8aUiq_tCe5Ru1PdsIWUtHOCjCbnZJ6CZTJAju46DWhJusydU7wVOPTao31fOEMuGUUppILZ4FJZR88Qw2qO4Rb5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این شاهکاره ولی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84448" target="_blank">📅 18:05 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84447">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84447" target="_blank">📅 17:52 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84446">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">مغازه دارا واقعا بدبختن، با یه کیر دومتری تو کونشون دارن کار میکنن درحالی که ملت فک میکنن اون دومتر کیر برا خودشونه و میکنن تو مشتری
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84446" target="_blank">📅 17:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjBR_bK92qboo5YqG0jkW58i2_po8lNwoN6U1AekCOgZW2npRMwc7yWLqev_UFJ9kMT-L5bR_I6-4Qg9jd5s4ycs15ZeZzJwGi2mMgl3-OLN6U6p2vXzaIYbgGbC3_mu-eTQ185nHtxEe9i5US4ZO9uXhKDLQmM-sch_taKcGmEZfWY7Y1gAK8Owt3eX5pSh5jfM_3nPYoPm4B5g10-OBHO4yYpUQdYBDuDei3OL6ZcMWHLxuDDgP5L_cTnK6mzR-j13iAXz0j5Mzh5Kzlu0EBPGM3Vq7Dc3W-jghT83aftXIr87STbaMgg06CvR5V1ILNVxS7CZqM6eH7D6ILMavw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/84445" target="_blank">📅 17:27 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZRmeadKN8KfOFvUQxbtuingxvF_F4xCMCSWYoHSFVdt-baKIyu0y_ZjOAEpzDvfg01RsxqrXJPpUWoVcmlPReTDBJWQE66VQ2WGkX_7ur0IgQ-uVsJjJLPIE_dvwavQjJ2GW5upC76t5UIQz26ynx3vVJ3xmiqfML_hUV9vrqGgWt_rA5zbpujl33S8pgaI1w5xk73NtA232-bRv3o9XhShVzPoJz6B50tIQ8y6B0Kr279fnQbMqDXSMmemy1jRj4NBuB36UjqtR3C3Bv40fi0C0N2MFGHli4DW6fijrUOLBriCYFmEYa635NQFMH7MBR-mVYFALeEJW_2PzoUlaJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت؟ کدوم چارت؟ چارت یوتیوب با آیپی زیمباوه یا تاپ۱۰ ساندکلاد با آیپی هلند؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84444" target="_blank">📅 17:20 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=e8JDc6G5Jdq255GWNc4eDLxJfqeo-Nt_mqMEP_RRgmtAf_-8MkTRKbGxauHqzeeODFdUWCmPntqN5iVENRd9XN4zTrG2UjOi_BD01LHqboFJgFgJoTz1RO3pPB3R0hE0mHOJnD9iYkckILrYMOC_aVwmbrkhRk41IzrWGjCDXzCBdosPqqaMxvx0LikEp0wGzWSZwgSO_kVrVnOqj692rD8YcF41QVvEU96oosJyDWwVuodqzaYHj2OKoWndyVRjYvm3i4dvnWS9z0jZCKSYyy-LsADtYpf-cWzY1JFw7cZi2w1uyvkwXRgxUcOBmfG5iznlfTBkCZ_xiMg1-nQqDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/269eed4b24.mp4?token=e8JDc6G5Jdq255GWNc4eDLxJfqeo-Nt_mqMEP_RRgmtAf_-8MkTRKbGxauHqzeeODFdUWCmPntqN5iVENRd9XN4zTrG2UjOi_BD01LHqboFJgFgJoTz1RO3pPB3R0hE0mHOJnD9iYkckILrYMOC_aVwmbrkhRk41IzrWGjCDXzCBdosPqqaMxvx0LikEp0wGzWSZwgSO_kVrVnOqj692rD8YcF41QVvEU96oosJyDWwVuodqzaYHj2OKoWndyVRjYvm3i4dvnWS9z0jZCKSYyy-LsADtYpf-cWzY1JFw7cZi2w1uyvkwXRgxUcOBmfG5iznlfTBkCZ_xiMg1-nQqDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورو خدا بسه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/84443" target="_blank">📅 17:08 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">کیفیت اصلی فیلم اسپایدرمن اومد</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/84442" target="_blank">📅 16:35 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YE47h45e_UdfNtxBZ6YNKdGOCDy8S8hvf2nubuxnZbwqTsfl6MaQwcZQMcOdUm4_9LdGY6jIpPKAMMRY_TK497TVIql6W2Y_DdB4cb9rChGZBXDN6TQCUlROgsq8w5-FhjxRUGVJL7xmbqTw4Pyc0bOGnuq4qYLSmyFsR7OZHsv6Kco1EAu39LPYTq10B3bLbZ5preeiAgivR2UIG6r0NVGh9C6IhE9pfqtioHBgP2UZGvQjB1e1SJoA1hu45vClBm4GP3mUwPWS0IosjLbR6BQbD6_NciuXnJs8APe2sIczeWK97hLqerzWrjuuI7d6tUAXmEG7gchnhQ6zM2Rb3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کاگان همچنان درگیر مهدیار.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84441" target="_blank">📅 16:26 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gYumoKiBRz5BoB3W1K3uJhnJJvM1qaXCjaP8U1UIR0iKzsr5cVFLOFYdlhWkEQLDa86JNr8YqhzGjZbM_YcDZzw9CrWaaQnOfbL0FG8CchNoPXZRTaF1YD6hxA7nICa_Uf0Uiljq-L_lyfSLz2jaUWFa7WZk6PviE9W3U1rm5ATZf0XMZT64K2M42vOB0_GoChXSxTezZQ1gKc_9_tKYsPlkijUOmF9sSM9er5yobGOOadSt8V8uuOT61HE4s8GgnlyeIz2fSNHtVLo7XESbcAiJAYfCO9lnpF6ht8I6tMiEY2SbLYTRwHpQpGpFp99gDc4r4Jxt18fsh1ShLE2U5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زود قضاوت کردیم
میلی پول ملتو تسویه کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84440" target="_blank">📅 15:43 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84438">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تیجی داداش هرچی نسخه کنسل شده دادی بیرون از نسخه اصلیش بهتره که
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84438" target="_blank">📅 15:04 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">وکیل تتلو گفته که تتلو شاید امروز آزاد بشه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84437" target="_blank">📅 15:00 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ok0-UbYf8LgiP0lI2w7PpSJ2X0g8ekSFLvBW8FOLhZ3TaJWO19PLIMlXYUZ80pOFl_18nmLdqjNzzKDhUMfsu88wPZrrczf8doLwXIjz30eJNgpunz_AbtlfZr9GCiQdjmxTadHO4A3_s_ElGAoex9hXUUxGLwFjbAzpB1MAP9G-0sFBj018mjjixP1u8frxZnI3p8vzsr4WEyTKT4frYaaVHnfPBQml1yZvZ-W29xwVes0DD1wRuw3CN4tHGGbh_RJUcNH1_y6_c7iJv_UxxH29dV5qWkX4JzVd5f3w585caCwQpmIDzt6-lNtviqTPA5zLlxJ7Uqm5dOlX4IIlHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
ورشم؛ خبرنگار نزدیک به ترامپ :
آمریکا در حال آماده سازی حمله هسته ای به ایرانه.
@Funhiphop
| TemSah</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84436" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84435" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84434">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VdufEzVnwDONE0h0GIUtuZtc_V_X6g25sv7-aFSavJPk5-1QWfAtZLyDQdPz2q1gtI378Yt8XKfnmPLEilMExB0Kox3qn3zIXiOjLV00mHQwevDqIRdC125oAn20Q7YMnU1SMSFdZmfNlC7WTqcogCet7oYQw_lNnNB4v3OHRA9LV1TEiYIgbDJFC79MVIWqgKvhAW0lcaiZBle2qclR6y9hOzcJnhV4tMAJzOni3JjoaIFoHIQArAXNJvWa_JVU433XzpzlXkoNzjM9owZ-Wayr-NPzwcXmlYFDrpnHxjgJtxxiJf7WPYU9CnLqPHqtPNcGpONwgSbTsw_hHq1zcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
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
R13
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84434" target="_blank">📅 14:56 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84433">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/84433" target="_blank">📅 14:51 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84432">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=TZqvQcjxlkxUvPVU4KBZU8eauampM7AY-vL3pTMy87tmyrWjCtvzNgNhLKIig1dwwMnnqG2OwfkSeu_A_2kESN98V5V5UXI18MsxyN5FSG3P8sRNLX6mTOuOKBTf2TfUPND9FKqYo1eq48eicsZcD5kRtUSZd27XyKQCTD_mK0ZrFZUIVqbL7ww2iA3xuoQ3Ic80w-f0-M4ajTQBPh4t2cvGvb-XUt4oj__SXALtSZE3sq6CCEEhmbaf2Cm2OH2SCZCbjt4dJRPwxGKvjo5LJSx7O78G5SLz8E4LvM8WFtdYsYSMRs1MSDpPIjGF5TnDFHEMZ-t6aKK_jMteSyYCHA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3008a810e4.mp4?token=TZqvQcjxlkxUvPVU4KBZU8eauampM7AY-vL3pTMy87tmyrWjCtvzNgNhLKIig1dwwMnnqG2OwfkSeu_A_2kESN98V5V5UXI18MsxyN5FSG3P8sRNLX6mTOuOKBTf2TfUPND9FKqYo1eq48eicsZcD5kRtUSZd27XyKQCTD_mK0ZrFZUIVqbL7ww2iA3xuoQ3Ic80w-f0-M4ajTQBPh4t2cvGvb-XUt4oj__SXALtSZE3sq6CCEEhmbaf2Cm2OH2SCZCbjt4dJRPwxGKvjo5LJSx7O78G5SLz8E4LvM8WFtdYsYSMRs1MSDpPIjGF5TnDFHEMZ-t6aKK_jMteSyYCHA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس  @FuunHipHop | Mmd</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84432" target="_blank">📅 14:28 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84431">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این‌سری دیگه ماسک نمیزنم
یه ویروس ناشناخته از آزمایشگاه طاعونِ روسیه پخش شده، چند صد نفر قرنطینه شدن و چند بیمارستان هم بسته شده
هاگوپیان: طاعونی که تو روسیه پخش شده، حدود ۱۰۰ برابر کشنده‌تر از کروناس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84431" target="_blank">📅 14:03 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84430">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد. Spotify  @FunHipHop | Mehrdad</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/84430" target="_blank">📅 14:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84429">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s55rVnJRAB2PbH3wTwAvMjpxq6PZIiy6TAsxyAkoguqRTgG_QD2use9QY7-M-BbDkro3IhkaX8zzicQafM-whEp9PQni3jGN2Kv43PSDOXMRRlqI0aujzBBG0ngywIhPmBzm_ZPnMSsR2AKvqsNVje4IBy_PkyyiIBcbHTrWhpEiHjZjxg1-6rk3JcbgrACICO90SGfMileiuJJ4WNcs2Vlx7FrowEhYE_h7CPwsIYBJ2M53-Z1eAeHWy9sCkt1ELKepQL9_R4ffDac_3ckIJcvjDxT2ppUElHi2FAXnkPiKoMdHM7liaVKP-fDS_SqZpNaKfj_DXIJBeHvQzbbqNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آلبوم جدید امین تیجی به اسم «پله اضطراری» منتشر شد.
Spotify
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84429" target="_blank">📅 13:32 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/ve1KBUC564SpUBqaWRGq7cV61_0OT2FO8HKuhnewUOLLbC8-iggepPpNpJkspTiXctEzb93IbaA1JbT1U9t3BFaAhOh5LCgsO4GFfOmZelILdaGpHwgLYJ4quLzvNIQ5-djXCOk0kSP7WIz3d8VgwqART7DC4xO2Qouifb3y1gZghWupVYxeafWHVM6Mn0a0ZGmi3Ridru_D1m6q-FbgSG76bsxxMPO1aEhgqK1SnjhY6DR_cFIN1ENlkGWrUP5Osaw_9ORjtvv51iByol3AxnapJ19Yf2qEUf9SCXSgywuFV325yUdPQdP7RdFcein52iYmz0m3xJLfvOTUcTvm8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/vRlbcHfk9ppagbx6SMPvnUrMV51v-jHDziNOs6DIH1CWCtekO6RNtWJiuMrMtp5pwDrkf0VcRif6ss8QlJAwuBSM5tdqaBkWeLDnqSgRVKkGjO2rXooAtYLxo7nOxIIIuuYo9JMprLkOXlg1HrDlm9xst5kJD_Fd3mfwowj-lR8TOgCt9Cl88VNV39ZDvRRCeAO-iX8tgLozLoPuIZyE1RzzvbcnHjkD777zx5G83o3GyEoHy0vTzwy3f0ej7SmqPqWyGaKeDqYjLQTK8YJemSz3IZ5PlsIgzz-5GwrejTXaQBv07XN5i7LvLssO73SyrqO6C5vySiQw-fUkiQ-1cQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">صرافی ایرانی omp finix که امتیاز رسمی و تایید شده ای داره، پول مردم رو بالا کشیده و ۳ ماهه درخواست تسویه حساب مردم رو پرداخت نکرده و مردم رفتن جلو قوه قضائیه دست به اعتراض زدن
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84427" target="_blank">📅 12:06 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">علیرضا رئیسی ۲۱ ساله و علیرضا سپاهی، امروز همزمان با اذان صبح اعدام شدند.
قبلا علیرضا سپاهی بخاطر از حال رفتن موقع اجرای حکم اعدامش راهی بیمارستان شد که متاسفانه خوب میشه و حکمش مجدد اجرا میشه.
علیرضا سپاهی با دختری که دوسش داشته شب قبل اجرای حکم باهاش ازدواج میکنه.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84426" target="_blank">📅 11:17 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g9NKS_ony_Zi5daB4bjkGMqrdphR5lBCGfbPboS3OZO9hufU_bM0VARrtNKEx3VU_uV4kxk_1SGBJYA6ZeXHTb4peTofBphoUR5tpGFqLXb1U5adJVsEvsKj5JD3uSxa9xZOfShx1Tan6VsG-hAL7AMd0YweKh5WbNizvSVPPo0wT3yrt7cmr-iqWeu8KTaXOIx7vrLbxj49H7Yp4WXAthgHeN5gzhI6-SZdBXZaAT5zt3iHl2cPJ5BLhtC9dU0yCpPd127JCzYCqRoy_MfVd_dLsVzZOt09as45xShpdDbTV1IqmPOpnML-RkgnkF-SqHEgXJUdoYg8hLl4OjyR5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84425" target="_blank">📅 03:49 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">فدوی: قیمت گازوئیل تو اروپا 2 یورو شده که یعنی 700هزار تومن
ما اینجا 10 هزار تومن پول بنزین میدیم که حتی یک دلار هم نمیشه و اصلا متوجه نمیشیم گازوئیل لیتری 2 یورویی یعنی چی
حتی با اینکه قیمت ما سه نرخی هست بازم کمتره به یه دلار هم نمیرسه
این شرایط قیمت ها بخاطر ابهت نیرو های نظامی جمهوری اسلامیه که بوجود اومده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84424" target="_blank">📅 00:38 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">تو رسانه های اسرائیلی قراره بزنن
تو رسانه های آمریکایی قرار نیست بزنن
تو رسانه های ایرانی "زدن" که میگن چی هست؟
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/funhiphop/84423" target="_blank">📅 00:13 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بمب افکن های B1 آمریکای که برای انجام عملیات تو بریتانیا مستقر شده بودن برگشتن آمریکا
ناو جورج بوش هم رفت تایلند استراحت
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84422" target="_blank">📅 00:01 · 13 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DBqkKBKtUZiy9Yxw7qC7CWRGZYiMJi2H3LkoJBr31QvXT7Pt7HsiCI7t-NgAyAOqK5HGe7_yqKKUsn3_3qGBqYegULHTCsLm-9nJisbkHafmfYNEqr5kfcgPJv2ictFlGxzt6pIa74TuvpoDsKyJ_2YwqWoc8A3fwjJu4RtmsX1G8hVeQ1LBHnXdjfbE0RmlAJaYEBMsNOIXyHQ--ISnt20i2XfaLvIXrhth9jwuTLjz_ZddNjDsLmqKJ0gIxLXEzUPWkQcPP-GkwWfZTlGLiRkfK6aXwRl0OanypGMy7ceqAkOx44WO7msp_rFXfdIRQBWInp8RSnZzK7Tutqs5Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/90aedaaa0c.mp4?token=DBqkKBKtUZiy9Yxw7qC7CWRGZYiMJi2H3LkoJBr31QvXT7Pt7HsiCI7t-NgAyAOqK5HGe7_yqKKUsn3_3qGBqYegULHTCsLm-9nJisbkHafmfYNEqr5kfcgPJv2ictFlGxzt6pIa74TuvpoDsKyJ_2YwqWoc8A3fwjJu4RtmsX1G8hVeQ1LBHnXdjfbE0RmlAJaYEBMsNOIXyHQ--ISnt20i2XfaLvIXrhth9jwuTLjz_ZddNjDsLmqKJ0gIxLXEzUPWkQcPP-GkwWfZTlGLiRkfK6aXwRl0OanypGMy7ceqAkOx44WO7msp_rFXfdIRQBWInp8RSnZzK7Tutqs5Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رژه همجنسگرایان
🏳️‍🌈
طرفدار فلسطین
🇵🇸
تو فرانسه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/84421" target="_blank">📅 23:21 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84419">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=ayxRncHvllYnOT3_sXHatRGY5DYI8IV6AfaP4qVkJbUeIvCutqdDRyHDop1jV8N4xhK6shSb96lH4F7ftA_Us4_2XNi_0oCPzz5zRNwk2ROXGILrY0Vue0YCrF6KGKhCQR61u7Er80yMxDeoaZhIdxFvmH6jy2ih9u5qY2vdAUqrnyN4F4Zi3hgjCXkvo1MQEpPkMm6cEKrpI5sOBNq5sVfC7_mCrxSLUt7gijeAkiA87imj4IBgKQeN1xhR1PTQ_OQIZoSWRORjpgkIrkBH_Zh7D7sGIZPFHydwRUCh3mSydu1DN-cc1VjfDv_r4MXDfkjXrPIBDd5BRXPrWKuumA1gB1ihWDoqZGm56oLS8_G8YmW-7T29E_lE1Qn_dR6lcV2RgzCjx1PjCnI9NOMJW5rDOCC4kev0wraugTHEQfoI8q6QzDrqnNAQigr7kYx3kszFjpgqRVRjHjGdvlCUi6NaI7QPZ0713hb3yA_OKE7RPp1GmWcQRryCvLbaM0IPp1BIgfxhVpeZUAqx2yzVhPTJcKzwFBHc4tx0xzd3B4vRlxaxlO6Vr0uGuUM4ABi2zSEcp34m8Jo9fbHcktuxJNfn33LNA1leq_WG3JyQf5TmAHILWEvzV0ftrQ-z3V3kW684i3bC6vI8BJNMlZQY1lH0dJb7o5diBuVJJJU0xSU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fa13ecbc2.mp4?token=ayxRncHvllYnOT3_sXHatRGY5DYI8IV6AfaP4qVkJbUeIvCutqdDRyHDop1jV8N4xhK6shSb96lH4F7ftA_Us4_2XNi_0oCPzz5zRNwk2ROXGILrY0Vue0YCrF6KGKhCQR61u7Er80yMxDeoaZhIdxFvmH6jy2ih9u5qY2vdAUqrnyN4F4Zi3hgjCXkvo1MQEpPkMm6cEKrpI5sOBNq5sVfC7_mCrxSLUt7gijeAkiA87imj4IBgKQeN1xhR1PTQ_OQIZoSWRORjpgkIrkBH_Zh7D7sGIZPFHydwRUCh3mSydu1DN-cc1VjfDv_r4MXDfkjXrPIBDd5BRXPrWKuumA1gB1ihWDoqZGm56oLS8_G8YmW-7T29E_lE1Qn_dR6lcV2RgzCjx1PjCnI9NOMJW5rDOCC4kev0wraugTHEQfoI8q6QzDrqnNAQigr7kYx3kszFjpgqRVRjHjGdvlCUi6NaI7QPZ0713hb3yA_OKE7RPp1GmWcQRryCvLbaM0IPp1BIgfxhVpeZUAqx2yzVhPTJcKzwFBHc4tx0xzd3B4vRlxaxlO6Vr0uGuUM4ABi2zSEcp34m8Jo9fbHcktuxJNfn33LNA1leq_WG3JyQf5TmAHILWEvzV0ftrQ-z3V3kW684i3bC6vI8BJNMlZQY1lH0dJb7o5diBuVJJJU0xSU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدیدا این بابا بولد شده حرفاش شبیه شیما کاتوزیان نیست؟
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84419" target="_blank">📅 21:24 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84418">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Chera?</div>
  <div class="tg-doc-extra">The Creator</div>
</div>
<a href="https://t.me/funhiphop/84418" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84418" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84417">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgtyEtiPg5fEM9tp1LIXTILJa8AxP3qCLCkKq7dYGWbulKhanYIgk7OMNdN_Ro_oANITiQm2IWWAGOe1TDMAtnfLvYcj1Eky5rSY9xOs9BuCI10Lw-v04J7TEV1Gyx_S41Unm6xA7nwnEQNqA9yP7KnGpbh0k7twNtPlZ7HXUkv0PQo1BxAzHRMeTCYcqEbWvljghjWO-iPYRCSURmJprlYI4WWvUsukI-QpqpfGVQTdiFoPEHq-g0vNA8-g5qNKzEuIhVTtLeCViNCavlj-iKppYn2Zm1s0b3Sk-U_KaQERqAsW1nLaCK3jbbvYTnCvqskceVH895W2FewBuew6GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید The Creator بنام "چرا؟" منتشر شد
🆔️
@Amircreatorrr
📥
Download
نظر شما درباره این ترک ؟
عالی
👍
خوب
🔥
متوسط
❤️
ضعیف
👎</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84417" target="_blank">📅 21:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84416">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">وزیر نفت جمهوری اسلامی استعفا داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84416" target="_blank">📅 20:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84415">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/riam6-VAwHAf8-Iz2X_cNbKkdVgQvoW55KSeLZ_Rr74H0R0W8Yk02tyi5-CbqpIf72GQ7xHQ4jrIF62EvwQPGyJwy-DG0lIL7uevOL_fdWnIVekG5EU4VK-Ecwp3UbZH_2PZiRw7i55CDHr6NuWFgvLTw7Wmylo0ea_vItbIEG8NUBaykV9YSEsEUvbQD-Z0oko_9nPLZCgeqoWdGV5JikffN5Q7S2FyodAqWAgmG_LHJ_rYk_nCHJJ0JDhFv7uyBOnvPWtLVw-yb8z2qB9ZY39HNePj-U1QC-GaZSTjMTFdQZ7aQqhHJHuNd-Ymf0qzhBwrWHlE8572Ymj8G3B0PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید گوچی فلیم و کاگان به اسم «هالیوودی» منتشر شد.
YouTube
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84415" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84414">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNkZXg7FwDZOrqqIObI24b8p9qV5HYwP8MaUxZYD_yIlk1i_aGvckNSGAMf53TgNrlaP0DzO_wzATjWg-APyyLxBioEyZwhDCg_IBl-ErOmlE0DwDfyyEVOG-iAO8ni_c5YULwjAdxBZlijI6pKFhXae3g1vt5U0r6mc9vLSJWOeEHrFDVw3jgXg6Lonk5m-vs02CLpKa4YTt5Uve_UysKsEq66TAfMYRNwY4peT00_govEpE4KjLJ-643nSfkuFsn43Cp5D97AJbIxgdEvgZqDZS9ag6-gvQJmRxmUZWjOggmxx0CzaKj_kQo0TddtsjUL61FmVqqpu-VG9s-QcRw.jpg" alt="photo" loading="lazy"/></div>
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
G12
🅰
🛒
ورود به سایت
👇
✅
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84414" target="_blank">📅 20:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84411">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nkr6av0D-gnqWtaw6a1ysfGx9XXNv7gbt23hVYvoocZ7mkaO76AgsjdBCb1k1Dusxs0YPUg3WKpOJE5984ZKA4a-RkrrU1H8QpYjqL-wHA-Lm46A25jmAc6zrnF8I2rpZ-j1N43LnBNrAXSuYcVgohP9VEF7b-t59FlXavwYE11CRVYx_2hH5-aRt3909Hb6Tt0_D5Vnhqxuc2x2g0rAJvwb0tB0JoQQK9vxZ3fhzvaXwfr7zn1pJ6DC80ZkRtox3jKEarh7HAsgf21XF0Zp6Pne1OCRaIhSmTpFzP9RPZ0yCxKJDR-0k0950Ai3Ge5tI74TPKVit3jdOPFqd_Po9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یاد کلیپ های دوران بچگی میوفتم توش میگفتن من از اینده اومدم و ماشین ها پرواز میکنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84411" target="_blank">📅 19:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84410">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">تهشم داداشم جوکویچ پیر سگ مچ زورف رو‌ خوابوند</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84410" target="_blank">📅 17:54 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84409">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84409" target="_blank">📅 17:33 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84408">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">دلو از دیس به دکی پرایم رسیده به دیس ریری</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/84408" target="_blank">📅 17:28 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84407">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yf2EqecnAOQE07wuFoRgrNVKU0Khx0HbFLbir48N8DMoc0CGRNrY06XyqhqE5SSOxC9XKkeDRL4SxbWgtR0qT_g-DR4PBbdes_44shP0Q3qwn0bAslg1dFL2_HXZUEHavvGkFBLn8wpv3hz--AozLZf0BNnJgGyr9XahOEvrzL0nNPpO6EGwoYAY1JuUAMVO-7Vo_aP_jov0hI0xqaXSNhJMiQWCpm1rauZiV5uUxU09A6PUXXId9xhtrBJlUa7_V4GEW9pQ_NQYqulPQdHFslGu_Wpnxu3-tDejxraRhCBvYuzopBLIC2oE_9RX-eqY5pfFhPWOQYHZw7isc-cf2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید دلو به نام "هاها" ریلیز شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84407" target="_blank">📅 17:20 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84406">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=c3wVWdttOaq3UgJF02mVQYxUKine93Jyx4AK3g7Gp4Dla2PDjuFJ0zBPrxJagVAnAvzNkexlj1GsGXDbf5_cxNt34Si7Nqx4i2fX28bObt4MiCbVSh21g6t4NYqwCRpoyaSC3z7vC7RStb047xTcciVf7dr9F0UcYO9WPOyx7g1kZ31PA5SuQT5KpxAdowcyLDTnNQ4_3qMGrclqxvHSyS6xNM2g7iAA83WaxmI39VzXeJezBVP0PenBcPxoZW04C6NjunXFXgRc-MCz6Q6OZHt2SOCiCYky0X2ayIXy-RMf9oCRCE3d0tJkSc3lFsTydu9b5EhJdoAjFmzB1dFiew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7d2c0ed177.mp4?token=c3wVWdttOaq3UgJF02mVQYxUKine93Jyx4AK3g7Gp4Dla2PDjuFJ0zBPrxJagVAnAvzNkexlj1GsGXDbf5_cxNt34Si7Nqx4i2fX28bObt4MiCbVSh21g6t4NYqwCRpoyaSC3z7vC7RStb047xTcciVf7dr9F0UcYO9WPOyx7g1kZ31PA5SuQT5KpxAdowcyLDTnNQ4_3qMGrclqxvHSyS6xNM2g7iAA83WaxmI39VzXeJezBVP0PenBcPxoZW04C6NjunXFXgRc-MCz6Q6OZHt2SOCiCYky0X2ayIXy-RMf9oCRCE3d0tJkSc3lFsTydu9b5EhJdoAjFmzB1dFiew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عالی بودی حاج اقا
یه آخوند یه ایده به سرش رسیده که رزمندگان رو به موشک ببندیم و در اسرائیل هلی‌ برن کنیم.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84406" target="_blank">📅 17:14 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84405">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mu0nkRNPOIazs_KKcSvrLTmd9IBmMGlB48QW8qcjDLvMPZ7VuxVZWJTXgGy0Yy5q50IBbvFXu89kCOcJHZjZ82Vhwyw01pHCIaKtWZfa1wlZDYwQylIiXiQoIcfZUsiofii821g53PujyDQef651NaXMZyQ_fwlkm7ViEUkiNAlnLM_Kt4HhNgo9LJEmNIyIGoRFTkgiGQmbY0WP6PgQIkIEwRN3MwymDgnCaFc66gFx9CtoVbsgAkMPjf44uNmGSJ5RF_kkclBgv_Xjo2QVwlJitCTjFQtyHvjiQo7R2FfhXcm93E2ScdUex_FYVkrYMM8ZlKpVZ89IpPk0Th5Fuw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کل زحمتامون بگا رفت، تازه تو ویدیو هم میگه امیرمحمد افتخار ایران
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84405" target="_blank">📅 16:34 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84404">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=Njxw8oR1-FObXhn1czQqSfZAYWB0rTlHLXCDCg-YFVQ-iIcZfDguau6fTBFYhdtd5b2i4nRaw8qBSJJq5HOjxQjhN6c4PiUEgfpvf0phwPx9EleefclBfb16zCfueLH-0ZcNFw-Emn8hT2NZw5TgkICokUhi79ppAkbHZ5l7HEYj3axp7J2eqX1B-OvR8CZUOsGgejtDbCBN1gteIGudnleeBHiHprEBHUY98xfuNHNpRCZfUsa7EEOZy1EGUELorbMGZX7gG6_01wAdBKcb7LgKcnmZ6y7p8lKXrIQxh4SA4NZ-x27aUqSnJOAkeRQlaGgbX2XoTcdw7fslB0Cn5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3ab332668.mp4?token=Njxw8oR1-FObXhn1czQqSfZAYWB0rTlHLXCDCg-YFVQ-iIcZfDguau6fTBFYhdtd5b2i4nRaw8qBSJJq5HOjxQjhN6c4PiUEgfpvf0phwPx9EleefclBfb16zCfueLH-0ZcNFw-Emn8hT2NZw5TgkICokUhi79ppAkbHZ5l7HEYj3axp7J2eqX1B-OvR8CZUOsGgejtDbCBN1gteIGudnleeBHiHprEBHUY98xfuNHNpRCZfUsa7EEOZy1EGUELorbMGZX7gG6_01wAdBKcb7LgKcnmZ6y7p8lKXrIQxh4SA4NZ-x27aUqSnJOAkeRQlaGgbX2XoTcdw7fslB0Cn5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بچه ها شاهکار
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84404" target="_blank">📅 16:27 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84403">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=arVxlv7ji4Vxbd0mwFmCd0Nr42xE_xeEe6T9C1ECauJAjmt3HQ84T4adrF7320yE4-E-RiGx6FsctKEGrOit4sANBVDgntFk2XwrvSNOJfX_s3MPu1NK8B_SCu1hUr-tL8RBmmu_chUeLA0wib76Il_4D7IC96obnZDi9GkpUdm8cFS13JcZPIki_HHmhkGVCWL0BrD9SRoRzXr1775PwA9RSfdH7rCJ15TBW8wS9gquQDJ2yEwDHyJmnaX4tzBPQ8LiEFpLauUJP6mz0C3-n4JHYq9TmnuOa6Gjr5vCYIX9L1EECIhCkTZQuB1ZPGBPVcujYGnNgY7z_brYAVoQsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42b7e86ab7.mp4?token=arVxlv7ji4Vxbd0mwFmCd0Nr42xE_xeEe6T9C1ECauJAjmt3HQ84T4adrF7320yE4-E-RiGx6FsctKEGrOit4sANBVDgntFk2XwrvSNOJfX_s3MPu1NK8B_SCu1hUr-tL8RBmmu_chUeLA0wib76Il_4D7IC96obnZDi9GkpUdm8cFS13JcZPIki_HHmhkGVCWL0BrD9SRoRzXr1775PwA9RSfdH7rCJ15TBW8wS9gquQDJ2yEwDHyJmnaX4tzBPQ8LiEFpLauUJP6mz0C3-n4JHYq9TmnuOa6Gjr5vCYIX9L1EECIhCkTZQuB1ZPGBPVcujYGnNgY7z_brYAVoQsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هواشناسی یه بالن فرستاده هوا یه سری نگهبان معدن فکر کردن پهپاد آمریکاییه با برنو زدنش.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84403" target="_blank">📅 14:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84402">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/X4ERdmM8nm8AaqfSv-YdQYmXV5L845uf2mUIA1MUE_OQ6RrY9jZj7Y33MXY3JrcvhBZhX5kz76Y6CBtsfMSo8WLNR5_i6I2zQairVOywSphm-n1vdeoD9WYroh56KU6T3XsaaIlRdhhPr2s0Zpy2jDg8DlxwEUmlh6Do56y8MYKnE9OK-Za8Yj8Mu3oeeUieNvXoB0VSz47vKcXiyE5JEneEVC9pcc34xbcBSxUMM5IZPsiNcIIfrcWXi_1D9h34RwlkDUwgGIGimvbQ2BasEIUXkPaD6K9sSYlyVg0RwG6rhbHlYejEzVA2p1Mw20NzUezKJgzX1gv7ounl6Cfk-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زندگی تو ایران هروز شوکه ات میکنه...
دو خواهرزاده، نسل دایی ‌شون رو منقرض کردن!
چند روز پیش تو خیابون آتشکده اصفهان، یه مرد میره به طبقه بالایی‌شون که خواهرش اونجا بود، میگه صدای سگ‌ تون ما رو اذیت می‌کنه.
ولی اونجا اوضاع بد پیش می‌ره و دو خواهرزاده (متین 29 ساله و مرتضی 35 ساله)، داییِ خودشون رو با چاقو زخمی میکنن.
دایی چند روز بعد میره ازشون شکایت میکنه و این دونفر هم به بهونه گرفتنِ رضایت، وارد خونه دایی‌شون میشن و اونجا انقدر بهش چاقو میزنن که کارشو تموم میکنن.
تو همون حین، زن‌دایی به همراه دو بچه‌اش (پرسان 6 ساله و پرهام 12 ساله) از راه میرسن، این دو جانی، زن‌دایی رو خفه میکنن و اون دوتا بچه رو هم با چاقو، می‌کُشن!
در ادامه هر چهار جنازه رو به بالا پشت‌بوم‌ می‌برن و سعی میکنن با ریختنِ آهک، این داستان رو مخفی کنن ولی نهایتا پلیس متوجه میشه و دستگیرشون میکنه
.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84402" target="_blank">📅 14:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84401">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">قیاسی سهیل پرنک رو دعوت کرده برنامه اش، سهیلم با همسرش رفته، اونجا گفتن باید یه اسکارفی چیزی بندازه رو سرش بعنوان حجاب، سهیلم قبول نکرده و نذاشته برنامه رو ضبط کنن و زده بیرون
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84401" target="_blank">📅 13:40 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84400">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">Winter Is Coming
بابک زنجانی: زمستان سخت در راهه، اما برای ایران، احتمالا یخ بزنیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84400" target="_blank">📅 13:12 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84398">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GXFXkWLTHzyjppzyTuO9Vix9Yef_cmcWrBqD8xoaMLmFygLMUDTGrPrxmHvqZpFSLLTNWjedkSZtisEGhYpvpstzSJaUQW30CWJLf3hbzoG56H9QSyiI_lEiaa6idYgtQ44XOOwNPC4tpurwwa3BomICrkxpDbDw3judEQzwaBOmYr1a5hrujrwmSZOviRur0erv4Te7qslvli4mhwzMfwVMDCIyC91-Dk-yD0K3yWczZmGNCb5sjtVBKLQmmGdOEz5wUsPcKxBnjt6X8dEiAhw-SfuUE1tP0l-zRw05PbrPxoMX1APYYRKBV9hQLiWn5bsohlwiiF8ott9M-pp-Aw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظهرت بخیر ایرانی
-دلار:۲۷۲
-طلا: ۲۶۶۰۰
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/84398" target="_blank">📅 12:43 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84397">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=L4E5HXLJoWWZ-v8_YSt46aMSG2xfBhIauW8NHUaUKuS3QDmo-FASKZYZBRWHDybar9bKeUK0fKKevIvyPrD-ASkWyENBsI75Xl4w5FtZeocWw1S0lySMs61EEUg5rAROhoiV6x6XkNobiqqJPr6GTOkP3VtyJu12pWdCPZl4RyBum2WIY0uKXlPLs1h0isA0I6fnC_g8174Qhq-bGT5zP-gJsT_J4rqWl8K5FhD_6HM4R3_NDDTFaq6Zhn7ax215hrrmtxl2CQ0mFhB1keAB5bulZRdsZabIs3BuozDKqZ_GtKrEpchVUJLxH4fdcDnnUBumg71pJYpKGmySkyYiFg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ba4e1d6062.mp4?token=L4E5HXLJoWWZ-v8_YSt46aMSG2xfBhIauW8NHUaUKuS3QDmo-FASKZYZBRWHDybar9bKeUK0fKKevIvyPrD-ASkWyENBsI75Xl4w5FtZeocWw1S0lySMs61EEUg5rAROhoiV6x6XkNobiqqJPr6GTOkP3VtyJu12pWdCPZl4RyBum2WIY0uKXlPLs1h0isA0I6fnC_g8174Qhq-bGT5zP-gJsT_J4rqWl8K5FhD_6HM4R3_NDDTFaq6Zhn7ax215hrrmtxl2CQ0mFhB1keAB5bulZRdsZabIs3BuozDKqZ_GtKrEpchVUJLxH4fdcDnnUBumg71pJYpKGmySkyYiFg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/84397" target="_blank">📅 12:10 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84396">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCfykZCtPtxhqF-6suX66C6n-qg0kF4Rz83rCE6wZF9uGRzT_8ggFFuvgzyShhkqKCFNZsAqc5nInJyU9XJZlYkMVjBCSutE1f7ZwczqUhRc2KRPIRWwum9VNr6VZ9uv7l8rPgEFCQSKw0Ja_F1zJyFhAyfh-QL1U6EREwPkVP22ewklVU3-4SqiLH-93JwluoUTPy66-XfC5orEeqmtYAdl23MrNb9_gbh72tEHdIY4gSvloC2XCi8VhrbaDK2nVLhW9tRS_vuDuTutwWcngSQoLiJHxNhMIs6-KfMEf8GCx7kJUPHkUbKK_NhtdvC8Bem3uTRXWzoLDteoPAAefQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سازمان عملیات تجارت دریایی بریتانیا: یک نفتکش در داخل تنگه هرمز هدف یک پرتابه ناشناس قرار گرفته و موتورخانه آن آسیب دیده است.
روزمون دراماتیک شروع شد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84396" target="_blank">📅 12:00 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84395">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WYR3F8PozcTGr7dDFARI8Jqz41DwtynAshlmZRdHChF8ZiuJsnnnQZXIA9_fR4XoBoznqtiibqbtARPlAWoqhKfvh67Zs42zi-t2PFEXlm0nUZidMWYoslLosjdRdIKH5LU-jROUSTxxge1Gg1-vkUTcOvyzhwtz-2jhTVJ3FNrpvDBYcnUJW5dYxBl_uuQ1kZvE_Tylbw2HtyAT0de51ReI9aaAN2i6w-gxgMf_4AIKcaPa9S52BZf2BEiH0VZYlur_6PWl9LWTEBva2UzvMgDwOkWmvbQ7bn8WogInk8WZPjAyqPo8-L4xv4G2SfvN4esB_72vNPPHo0tdG8_HmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ماشین جدید ایرانخودرو به نام 207 elite
قراره از این به بعد اینو فرو کنن به ملت
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84395" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84394">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">⚽️
مسابقات ورزشی را با بری بت پیشبینی کنید
⚽️</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/84394" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84393">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iW8rqQQ24e2QMCfyEjGF2Xdoi6LRQR1Uami6S7bJi5Jx7RyoGTzzWQjcVZK1KeUOQuIDcjq8FHs3ua_axczRbfouMblmDnKow0E-OH8HJakDVVSxcqxFj1utPZyevCwoBXgWVl7_IyCSxGZvcnNfmnRG8zlkP_hHtMTweoAYDHalPPP1qdsE_waItuibPiNIYjPpyj3eh8bYJCV71sEMJQTFlUimV3WFWc3kL0Kv_fuAN3FeW9U75m4-KNze0SN0jQQLCgzJ-JkfTl0lPtDtzqldURzf08fKPa-lWFYfsTBO_H0ujPwWV0TG3Jqac0cVM-oKK4IgtE4ZCmSUz582kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎯
هیجان مسابقات ورزشی امروز  در بری‌بت
😀
📆
فرانسه - بلژیک
⏰
ساعت ۲۲:۱۵
🌎
📲
رومانی - سوئد
😀
ساعت ۲۲:۱۵
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
R12
🔗
ثبت نام و ورود به بخش پیشبینی
💵
https://vsdgyfcdosko.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84393" target="_blank">📅 11:51 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84392">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=GXHX4qgxe-5e1FwUuu-ujdGhv6mzBJh40RU6YmsHfN9iHFsTXsYGGD1f5AN-8Fddb5Gn1-ZBfbTh0AM4tPHVuwiLsZEz4TrrL-D6HXbxL28fq192z1hXrtYu8c6kDvDz1RUegM0iI6tosHvxl5gi6a4w7jhpeJ5-DjvbjhKjpLayDLWIY-t8hteb1R9jdhWEFiCVIMZ_da9oNY1IcP1M3TEBjOCmkIcOturh4dxiwOo7_GrC4BrxwEmM3Lk3pHmIpQwxs6cYd1Tr5inZZAkvCqUIyK3E8Ml1kquBM9xIn8P4ept-0p0M1FXFOqg7UsylXq8LX70TYALHg2B-WR3gKQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0466e7e7a9.mp4?token=GXHX4qgxe-5e1FwUuu-ujdGhv6mzBJh40RU6YmsHfN9iHFsTXsYGGD1f5AN-8Fddb5Gn1-ZBfbTh0AM4tPHVuwiLsZEz4TrrL-D6HXbxL28fq192z1hXrtYu8c6kDvDz1RUegM0iI6tosHvxl5gi6a4w7jhpeJ5-DjvbjhKjpLayDLWIY-t8hteb1R9jdhWEFiCVIMZ_da9oNY1IcP1M3TEBjOCmkIcOturh4dxiwOo7_GrC4BrxwEmM3Lk3pHmIpQwxs6cYd1Tr5inZZAkvCqUIyK3E8Ml1kquBM9xIn8P4ept-0p0M1FXFOqg7UsylXq8LX70TYALHg2B-WR3gKQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتش سوزی در پاساژ خلیج فارس عسلویه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84392" target="_blank">📅 11:42 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84389">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">پاشید برید مدرسه بدبختا</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84389" target="_blank">📅 06:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84388">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rc2q_N66ECWaRwq6f6w8SWMXww5VWm6g2IffvTv6LQ0WxKYP3jrlJaqyzRP_J0OZtUIEfHT7wskLI1ofOGnzXu9eaFqrYXSMbwwpEtt3HNi2NXjJHgsUzH2NjE9Zt6YhA7DV0CbQ77Q73ZRGnKwD72jnA6xXrYct2-MKFhWtnWT1m3i69-hjph2UXwis7O2PJBziMsCCx0JzmWhFIBiDc0Oa4mSW9fW9sdLcda-r9tTia4Wk8fUc7Su87ZbbUL27_8KjLlo1pACxySSQJc7pDJQL6MG4yTHB-QCldXis7DrBAddo2qGb9G9kOihMMmDbsdId9gC9FRHgdv4M_NaqYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۷ دقیقه نگاه کردم اخرشم نبوسید
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84388" target="_blank">📅 02:44 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84387">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OZL0NNtB07LXRK_LobKHo6XNI8csjAL719eQrhHZQzWpEdTfcX1YJmUMJ72xfOLss-JdPWaNqCwpv0WVZX-Gbtgjua3W8rGEAGUVhdp2SJRXQ8Rn38ARjV5ZcqBc95YON9fD0Vahcm2mYX5haeG9X7FRPICQNJs8e7XbFmnowyiCbqXzVed4Qb-j4l6_EfjxPZ1Wkl3U7xAtt3Lvugw32kGKo7KCP-juLjYoYHI46ZAx88t8EkL5JZsOCYfUtwxMGOxZ2OLaEKy4fBJQe2oFPCbZnzA1s9NDx5yKnOvEjhICQg5FNViZ_GaweCbE9XhEPO-qMkExpusuVf6dYW6eGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقای پوریا عرب نامبر وان یوتیوب فارسی
🔥
@Funhiphop | Nima</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/funhiphop/84387" target="_blank">📅 01:19 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84386">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=Gj1CuhvJBUo-964m0QWIZc8iGCMKhp0jotdkveN0QvP1Y3Bwvf-iNctbK5p04vwBX8RjtPxC7zQnBpq5Tc77SBMdsV9-haru8z58Imkusx8hpAKpYGzbVu9__dm3VVenz_m2AvhUmnkjDruoaPOf0tcfC5lwRrtPkwlwfNBDo-Bi7DjZg-ToRAxiJcb60w5sFGczllod0DyY-ph76q9451beyYQ7JdbG691jDbifiz6SFWh1TOzwcHTASpLoTkmEajhYQO4Zd_nyzNxMT79Ohm-vA8uJgqIT9mkwcNbVKvISZmqPYqXZeUgBcjV0u8fsyptt_fx2rQnJpmSadTJACA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/979e96f7d2.mp4?token=Gj1CuhvJBUo-964m0QWIZc8iGCMKhp0jotdkveN0QvP1Y3Bwvf-iNctbK5p04vwBX8RjtPxC7zQnBpq5Tc77SBMdsV9-haru8z58Imkusx8hpAKpYGzbVu9__dm3VVenz_m2AvhUmnkjDruoaPOf0tcfC5lwRrtPkwlwfNBDo-Bi7DjZg-ToRAxiJcb60w5sFGczllod0DyY-ph76q9451beyYQ7JdbG691jDbifiz6SFWh1TOzwcHTASpLoTkmEajhYQO4Zd_nyzNxMT79Ohm-vA8uJgqIT9mkwcNbVKvISZmqPYqXZeUgBcjV0u8fsyptt_fx2rQnJpmSadTJACA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رعد و برق خورد به نوک برج میلاد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/84386" target="_blank">📅 00:48 · 12 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84385">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">پزشکیان: نوک قله ایم و نزاشتیم فشار اقتصادی رو مردم حس بشه
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84385" target="_blank">📅 23:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84384">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=sCwIbhKnSAnlGwJ9mMcq8xdQ0-3VrZFMO1JvGaFTfyqdCyibYoZCLunYDMrtHjH4YlfTRrFHwhtaKMGr16FHr8v2gKDoQoTwsp8dcYTdb6HcTASlrs6slusjbgpVkK7JPVlzQgdQMbRgc3Z3KSMPtb024Cafq4Z8X17GlXmjBksbZqRmcn-728jKuDCn50fxU_QAlDr7WAG2P2EZzh9yRkN1TnGXZ9ZDy3TqffUopPEQv_Qhg6EsCKf35TPd1Z-zjc1ADaLikP1p71zwdU8H88jqIssHaQI2C8Y6KQxX8ExJa2miLlKoytZpwPi-M9Gs3up03Xpiv3zoahR5iEk0jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7fc135904e.mp4?token=sCwIbhKnSAnlGwJ9mMcq8xdQ0-3VrZFMO1JvGaFTfyqdCyibYoZCLunYDMrtHjH4YlfTRrFHwhtaKMGr16FHr8v2gKDoQoTwsp8dcYTdb6HcTASlrs6slusjbgpVkK7JPVlzQgdQMbRgc3Z3KSMPtb024Cafq4Z8X17GlXmjBksbZqRmcn-728jKuDCn50fxU_QAlDr7WAG2P2EZzh9yRkN1TnGXZ9ZDy3TqffUopPEQv_Qhg6EsCKf35TPd1Z-zjc1ADaLikP1p71zwdU8H88jqIssHaQI2C8Y6KQxX8ExJa2miLlKoytZpwPi-M9Gs3up03Xpiv3zoahR5iEk0jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همسر بیژن‌ مرتضوی: به جای نفرت‌پراکنی بیاید کمک کنید ما بتونیم از پس عکس گرفتنای مردم بر بیایم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/funhiphop/84384" target="_blank">📅 23:05 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84383">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">توپ طلارو واس یامال اماده کنید</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/funhiphop/84383" target="_blank">📅 22:23 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84382">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">گورودن با اینا حرف بزن نزنن بعدیو</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/funhiphop/84382" target="_blank">📅 21:17 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84381">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AsQPc86PQ_M2VP1ZDV1J3XNaP6HCP0yxVyUrpfvlkuTQG_DL_MYU1l5f8Ed4WkIeWPTuN129f48qnzK_W9a_m1wuo61FUlz2nwBI3G-wxpGCBKysJpwPU0k71_KXmCMY40KWAHVWpa2XvG3xnjNmL_cihawILWX3Ru6E_MNatqs6XursNWXlb0RJr2gp368HqujfkwZrm-f7zz_Mp42bxtNb415ViKZK5FD7Dp_qWxw4HWA4XsoNSgH5yH4xClTHb4Qum6db79SI5adQBNfMwnLER-DYqoE-1l_KKTNsjWge5mKPt7Gbt06zNOU86Nqo-6-5-VRgU-EhhKXvVsZqsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نوشته های سردر اتاق رتبه ۱۳ کنکور ریاضی ۱۴۰۵: دوست دخترم مادر شد من هنوز کنکوریم.
پ.ن: بیت بالایی شو هم کونم نمیکشه ترجمه کنم تورکای عزیز تو کامنتا خودتون کارشو انحام بدید
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/funhiphop/84381" target="_blank">📅 20:35 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84380">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بلینگهام داداش لوییز انریکه رو میشناسی؟</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84380" target="_blank">📅 20:29 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84379">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HK3H2sFCbg4Uj6t-Xqk4AF-XoCtyBfuuvBos8CMKZ8QPrgPYWPZ-uYAV_yJ8LtFzN758i27V7SNaxocDrQxWLC8C8dxWhDaEXMzPP51xdMHHCYG3SKcgfQcBrO9xpt4hqUB17w_tSGtNP_J546dY-Cr_WEJxHNJpXh3CkROoZNaBGXDs9u_ivirZOraScN5g5mtYOMvyxoaKyW3ZPFqm69J4pT5Y6XYJDL2f6474BdOsdqqx2rZCgcrqUEellwkbWiRMRezSvDesebQCsO_fCJxIKwM9xTGfTjbxeK1FSQYq9sXIt_KPBPCkdYn8GYlWu7PN-x0EXENFVZ3olT9J0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واس بقیه دوستانی که رتبه هاشون رو کنتور بندازه به یه کشور بدهکار میشن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84379" target="_blank">📅 20:13 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84378">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">ترکوندی شیر
به دستور بانک مرکزی، نمایش نمودار قیمت تتر در صرافی‌ها متوقف شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/funhiphop/84378" target="_blank">📅 19:41 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84377">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=PdJUYtfX1YsNaBNlZt24yubD_Ny4di6Oluy5BVOcHK4CdVvj21qzQjAUemOX16dofEVwUj8XdriBn-kSZncGoCbA6sh2TgHGvpjpltSyutDTcS3Xv5hgrkgXsgn0cDeXDtnhZqR1MfLeOjFC2KLbeQahXg1uDBdgVjf9jMX3W5BFJCRkJAAjzmuH0G_Ilc5xb9LHnJUWVY7EcaRAAGwuGjkrhpy54aVfCNRQ-2FKIeBwDYcUJltdjJWoPUh87N-IlF2G3zhtW2pTn0guV3MTy2G-Io3bvQhGLEYrOeSS414OQD5Ge0D2FdcgGknbKziukLvb1Qr81h-MUEovGMte4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6db6ea36f.mp4?token=PdJUYtfX1YsNaBNlZt24yubD_Ny4di6Oluy5BVOcHK4CdVvj21qzQjAUemOX16dofEVwUj8XdriBn-kSZncGoCbA6sh2TgHGvpjpltSyutDTcS3Xv5hgrkgXsgn0cDeXDtnhZqR1MfLeOjFC2KLbeQahXg1uDBdgVjf9jMX3W5BFJCRkJAAjzmuH0G_Ilc5xb9LHnJUWVY7EcaRAAGwuGjkrhpy54aVfCNRQ-2FKIeBwDYcUJltdjJWoPUh87N-IlF2G3zhtW2pTn0guV3MTy2G-Io3bvQhGLEYrOeSS414OQD5Ge0D2FdcgGknbKziukLvb1Qr81h-MUEovGMte4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چرا هرچی خز بازی در میاره بازم جذابه، خسته شو دیگه کصکش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84377" target="_blank">📅 19:15 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84376">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">حالا سریع و خشن هیچی، باز خداروشکر از دوره ای که ملت با سری فیلمای یوری بویکا فاز میگرفتن رد شدیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84376" target="_blank">📅 18:59 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84375">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nIzfK0n7E7p8DzYY9g7hStcKupFk0KNRa_ut4Avfa6nnAjd13YFyENYwgI5cNHTDS5LUqiZqUk_0ku9kbrvH0X8yeVx3iIgxOhp6aMyF2Sovsn8HueDtg5Vi2drZlMFZawk2tXF_X3E7fhO6_7WCQ3ogU0Fqv3V7HjWo9crWjRDVplEIlKE9cE6Cnug13is3YlJOKV8897KnsLeKjpXqfXYll4x0QKsnznYWHe5l5eiJPafUpenFtp7Rd79wcjnhDXAWts8GSgIVXC52zd8J88WMwtY_PIZ6W4w94V8nMakupuOkTk_53u8qtoozvmFqKRWjxp-QT5Xw6Ms7vYybVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خسته شید ناموسا
سریال سریع و خشن در دست ساخته و ۲۰۲۸ منتشر میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84375" target="_blank">📅 18:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84374">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=HDMGHzQ6-A4D2pgV5CcVjbGpn6nrsE6t7EKA7sWixKwiq1v7KU9L4ZVbo0zr-HnIDGy30eE5DG2kPVd-2CRScrcnhEzZpGdsBmNltMQR8QY8SmnCeH0SzuxZMxWKcS4m08HPBJPdyX47vCJ8Bpvlums35-OeBU4QCX86r6-H5KbYu2zZzYfRm-2dlNUZA2tkZ9a0dGvBsrSpCAGCX6_78U34ODQlnTMZ5kocuJU_eCFLZFyYjR_Bukr2ynJvTtw54cys46uL4KK_7kXQD4-lzVj9s9D9aD9xDVNkc-qxm1YTqh6Y-gkLbM9yOm5TTJnAhWVvcEEXstiaqQ5lyGbNIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aaeea73ec1.mp4?token=HDMGHzQ6-A4D2pgV5CcVjbGpn6nrsE6t7EKA7sWixKwiq1v7KU9L4ZVbo0zr-HnIDGy30eE5DG2kPVd-2CRScrcnhEzZpGdsBmNltMQR8QY8SmnCeH0SzuxZMxWKcS4m08HPBJPdyX47vCJ8Bpvlums35-OeBU4QCX86r6-H5KbYu2zZzYfRm-2dlNUZA2tkZ9a0dGvBsrSpCAGCX6_78U34ODQlnTMZ5kocuJU_eCFLZFyYjR_Bukr2ynJvTtw54cys46uL4KK_7kXQD4-lzVj9s9D9aD9xDVNkc-qxm1YTqh6Y-gkLbM9yOm5TTJnAhWVvcEEXstiaqQ5lyGbNIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از دست این پیجای ادیت اینستاگرام
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84374" target="_blank">📅 18:43 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84373">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">روسیه: به زودی میزنیم پایتخت اوکراین رو کص باز میکنیم(
چند ساله میخوان این کارو بکنن
)
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84373" target="_blank">📅 18:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84372">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i3mb3KWLQX2UCnvfL43k-oaq3vMSMjoJHv96SFW3C0mFgP87RmtNGLl-4dvdGzOurzJTyU2WFm21p2D2x6R6OX1V2PV63dT0yEmBlCR6tZS_x6nTHAz8Ha0YzZJGdouwlQGuEC2JI3h_os3uahQxAuIZgMtpAxLsYPwfNDyIYanCixhqmXDhEvN9XykUYLQRjT5Vv0rI8pkmua7EPDLhsSKSscI6StUWVnxER84_AOI_MGJzoPcI7NgpeQDPzI2rz1W5rvqqMiZrxD6YayNbVNDd4MoH10MQKiX-mq_DQ671s5NVdSL-mvpbceUeAqcYpxjlNoZ8xMMwQ-49YaooRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دقیقا منم با این تصویر موافقم، به نظرم قاف باید برگرده به خیابونای تهران یکم جنس اعلا بفروشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84372" target="_blank">📅 18:16 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84369">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">عجب هواییه پسر، امیدوارم عشقتون تو این هوا بهتون زنگ بزنه بگه ما به درد هم نمیخوریم خدافظ</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84369" target="_blank">📅 17:58 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84368">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/favbmyuyhd6cwmsv2YZW3Tc718OscSJnj5PLKBs5OdlDezm_vZhlZLhKXjwAZv1C_XLDzdZZQeHbd96sYxu3iXP-lpPKxqqkJK3VbWq-8-E3kuBuOwf3KQ0LOKzNVnTjahbFsfmUPkuUWGD0BH8F_CV5DtuJEs7M2PmpFAzIlHGB9ggUvX2BDOdmsrrEAzoCMkoQBDYoSA5R2-y1ZTWkjOE-Pd0Hp45sx4f7kPkjJdJsMsSNBtuZ1oP2oYAqF4aEPfLJ0cNeOIWIlrnXYRb8B7Tc2s7GherEqWldiALm_QpzpOCb-zlq7zjvvMTfAdr_GDYsQgN40pSilmOBBxK2Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سریال the gentlemen پیشنهاد میکنم ببینید فصل هم ۲ تازه اومده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84368" target="_blank">📅 17:51 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84367">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اگه مصاحبه فرهنگیان دعوت شدید همین الان بلاکشون کنید، بعدن میفهمید چرا
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84367" target="_blank">📅 17:24 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84366">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">این میمای کنکور چرا آپدیت نمیشه، هرسال موقع اعلام نتایج همین میم ها تکرار میشه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84366" target="_blank">📅 16:45 · 11 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84365">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">دانشگاه سراسری تعویض لاستیک قطار فرار کن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/84365" target="_blank">📅 16:38 · 11 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
