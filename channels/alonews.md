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
<img src="https://cdn4.telesco.pe/file/dwZbFyAdL54vlTBLUUxV0mghyeE0dOLbv4XHH1_Xn9lDEwb1L5yhzv_wRnHqPIUeyhwzm6zpPthsNI7CFw6_XDqJRb8wux9jU7TVh3DxkptjTWRGIWr0Td_fFn_F1_QCIHNoz8fF3KDaGSVH2aL0hfJAdZH-rLqyrnrnN2bEk1yYRmNSnGNmd-xdEcrruSd5d-I0ARstqwRkSI-R33_jmQb-neA9CxYGiFuSy5d2_sgXA8hPXa1-Ko7f0fjTCvgh2evvfTTlzlsjt0gewOaM4uCabowKDnxwpMVgOSWmqeMmQIXdwfgmIzYDuvGcorpwJqHrjEBZSHUGASY9YDiFvQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 943K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-24 22:26:50</div>
<hr>

<div class="tg-post" id="msg-134525">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f3U3l1aoGDqoMN7SipQy7SjlGOdy5qF58tK6z3uZRyC8kOJI0B3NsUUfmB6ie2Rvle4vRbOU6-fxwv8SUpPR-iqABfEcmeMDYamr8kSQMmlAEY55gH0jD2yfeLMHe7UWI3PzGCTW-Saixxd5GaqUQuznLPEawP8-2l6EzGq9g0rHHR5YqemfTIuc04u3f7s1NxNUo-4A76gk8PCGi2W3Ni6SaD5tUxREBsqGjYzqd8xQjqk--_dGF_GpF5b-RC_RjMBJriedqvlqSmJahyyuvcToHIYnXOqKraFoTJjSR8oBZSWbKMIMj9WrTif6B4okgztDb1lfMlErzZnv7XOKCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پشمااااااااااااام
😐
هوادار معروف آرژانتینی بازم تو استادیوم لباسش درآورد تا به بازیکنا روحیه بده
😐
◀️
◀️
◀️
مشاهده فوری فیلم</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/alonews/134525" target="_blank">📅 22:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134523">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/o1x8BLk6pmIVGNaJ10c3a7yxYJlXghgQOY_MUv-6PxlATlSHfiA8Iq8l3a4qxKX9bHJgDBWBL5-wIp0PNuNadZLbYqSBhXATPj4aUduwTDSLnG7Z47xx3ommeYEMxAtEDcnPl2uDdKYX7LOF7SN_04oe1LYsymw-2VZNHtpNqMm4K__YxoiPATrZUR9eUw-wiCy_xCRvMjgpQOTeq7eO_A9PQOnTtN6dMuptK--bts8EHQXjXVU6EpoAfw3qUfwvel1UIrXq1bLxPlXKnmpPCXwwRTOPUp-1Tx-Wwgyrg7pZ0kxuNu7MeZcW_C602zXmw2ByTLS6GPUIE3eNT_dzhw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l3NssZ8YHiMHBgMQHmit0Sh_IJghHm9FUXbmQ6PIBkCf-f3QmXbd0RVIh32GxVZCvfAR4gCe2J6P6qEpTaW5sskfeYYYZrMyAAI8BqFqT0eUNsCH_uGzzMLVuQOJMHT_MKaCJu6bkVc7zOHWtjauqd6WKZRjcZn8vQZco1YvgmTQncdHL3O2jNGl8T93hD4TEyxTrIsIiwe4rZs15pC28_NY35Z_zWbjCIF7Y_1SBP8T5WAh1vZUwBU-MebnFXYqEHg6v00NUnXGJOFKo8vQ2VjMxJnB2nplW-5sGtz702V8f5CLxalkwuFWxEm8J5o9EK1ojknq7WRBt7YcA5wEhA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🏆
🏟
ترکیب‌
🇦🇷
آرژانتین
🆚
انگلیس
🇬🇧
@AloSport</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/alonews/134523" target="_blank">📅 22:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134522">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">👈
آژیرهای هشدار در کنسولگری آمریکا در اربیل همچنان فعال است
✅
@AloNews</div>
<div class="tg-footer">👁️ 7.14K · <a href="https://t.me/alonews/134522" target="_blank">📅 22:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134521">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
شرکت برق: مردم نگران نباشن، اول میگیم بعد قطع میکنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/alonews/134521" target="_blank">📅 22:19 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134520">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tQLf3O_ZaIKnga9_ryEob_Me5Qspj0VYrpDg2V8rzpSlbuVayABL9vZjRqrdd9pZvzBKWd4DcdRi07ZUTcE9YeNwlepHmxbgzHnQEQcEktDSp-HwCsYulhPd5N6xQjch_00adGA8uubiTIuwAGTstzo5yAFC8sabBSiLKoezD-b7eqpliY828nsJJR2SWRVKjeYzCbsG_BQ52XpuX2LH9yF2ZGThaZ-P5OlFfU3B7jnnMC-ge4tsPdBbdl56aUP4bIKHBXlzhuGx2cBVZskJc_IsFBCRL4we7-jDAjmNo93xWuIn1-PFQKkQ49qfzIU4Cd-79YVFA7DaMCiurpdr4g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کریم باقری :
اگه بیرانوند گفته باید برای بازیکنای تیم ملی مجسمه بسازن ، خودش بگه یه مجسمه براش بسازن ببره خونه.
🔴
علی دایی:
نگو بیرانوند بگو آقای دکتر بیرانوند
😂
✅
@AloNews</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/alonews/134520" target="_blank">📅 22:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134519">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-text">🎙
علی دایی :
دوست دارم مسی به فینال برسه ، ولی اونجا به اسپانیا ببازه.
🔻
علی دایی :
ما جام جهانی رو اونجایی از دست دادیم که سردار آزمون رو به تیم ملی دعوت نکردیم.
@AloSport</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/alonews/134519" target="_blank">📅 22:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134518">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67e4434e0e.mp4?token=BQx0udBeXxGcRudeCAjGGsWC6u1taume3ueTSzGUFOhhbrF1bCWyI1VwPXeTTmuHgaiu-zyd3sSusMuqLi0IYhZlN4k5OVzXvba2yoJpcP8dV_dC-1PX8SxxGDuzS9Q1Jnps1WSLI2UhgFxuxGX-quSIcUIASoqnzOh0tV6BwhoKZRTrZGX1hRuMSUbNMAl-2Hq9cU9whgJBJs9KiRuCpm5lMeT_R75bwAftE2u0FYFCNIJNynLTncHGDjx-4gE9iRBLFRAQsusPOuFMsESqO8MP8xNzP7zLSKMYbKRH8wpH7SsuZTrZ8lmu2Rb0P17YT3QvD20bmCjr7RR8Yj5MEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67e4434e0e.mp4?token=BQx0udBeXxGcRudeCAjGGsWC6u1taume3ueTSzGUFOhhbrF1bCWyI1VwPXeTTmuHgaiu-zyd3sSusMuqLi0IYhZlN4k5OVzXvba2yoJpcP8dV_dC-1PX8SxxGDuzS9Q1Jnps1WSLI2UhgFxuxGX-quSIcUIASoqnzOh0tV6BwhoKZRTrZGX1hRuMSUbNMAl-2Hq9cU9whgJBJs9KiRuCpm5lMeT_R75bwAftE2u0FYFCNIJNynLTncHGDjx-4gE9iRBLFRAQsusPOuFMsESqO8MP8xNzP7zLSKMYbKRH8wpH7SsuZTrZ8lmu2Rb0P17YT3QvD20bmCjr7RR8Yj5MEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
صداوسیما تو پخش شبکه افق داره آموزش کار با اسلحه رو به مردم یاد میده
✅
@AloNews</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/alonews/134518" target="_blank">📅 22:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134517">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
ترامپ: بهتر است ایرانی‌ها رفتار خود را اصلاح کنند؛ من تعیین ضرب‌الاجل را دوست ندارم
✅
@AloNews</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/134517" target="_blank">📅 22:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134514">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bd59a07cb6.mp4?token=ZY9wykKy-73RIbVMSQxegvzTss12MfSqoKIR-CJC0Qwyqchi09mOrY0Y7ONAawc1gERfddSSxlmiyXh-aY6MjF54VAws-C-Oinj9eVa-VjoJL86Rqqq_IMroCovpHHgixBR8bvx8YVjPiJA2NYJWUmhqDUkJTOuP27TbM4VRxnSsMDtvJH17L1F6we2dsA330JvfMSoj4v8tN52mxZ59Fs3oniJMgSaZKHG7Fz1SLo7K_LgN2MQtF5lpCb2S8p804vhBIfJX5_xb5i97jx5dM0kYyv-lo_4D1FCfM2eE7yScDKw21s6U5g5wS1o2XBevQBlUWf1uKX8GnaADUetGLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bd59a07cb6.mp4?token=ZY9wykKy-73RIbVMSQxegvzTss12MfSqoKIR-CJC0Qwyqchi09mOrY0Y7ONAawc1gERfddSSxlmiyXh-aY6MjF54VAws-C-Oinj9eVa-VjoJL86Rqqq_IMroCovpHHgixBR8bvx8YVjPiJA2NYJWUmhqDUkJTOuP27TbM4VRxnSsMDtvJH17L1F6we2dsA330JvfMSoj4v8tN52mxZ59Fs3oniJMgSaZKHG7Fz1SLo7K_LgN2MQtF5lpCb2S8p804vhBIfJX5_xb5i97jx5dM0kYyv-lo_4D1FCfM2eE7yScDKw21s6U5g5wS1o2XBevQBlUWf1uKX8GnaADUetGLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پدافند کنسولگری آمریکا در اربیل عراق در حال فعالیت برای رهگیری پهباد های شلیک شده از ایران
✅
@AloNews</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/alonews/134514" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134513">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">👈
جی دی ونس: برخی از وزیران اسرائیلی خواستار ادامهٔ جنگ به‌صورت نامحدود هستند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/alonews/134513" target="_blank">📅 22:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134512">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e103349621.mp4?token=eunJQEPTUJ79GCsmxHB9tN9QabuPBXPYfiwAebridzunUC1me2FJkFntW5g1ZsmDAdATX1zspjcxH_0ZNZOBSDpTklSuJxB0ZlKtVkvVH2WZDcYhybar45CfV15sqIebVCn5_PQBrQlPc_n3r1DqyWiZbpIVxrJDPf-XPiBT30C4YjdUg-ukYBJvlFkct0iMJzN2h2i9ovzeFYX9-a691Rl-W8iMJcm8ttV0NNhvQ7OF9tsVYWSa7qsTA_QZUtZG0vnKvd6nXTRkmPpPff9YBOQgU1f5g9_Mka9TxuPvEFS3OwQp4XVOa3kN0TywrAwC7H32NMeENfuth_ya8UA1MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e103349621.mp4?token=eunJQEPTUJ79GCsmxHB9tN9QabuPBXPYfiwAebridzunUC1me2FJkFntW5g1ZsmDAdATX1zspjcxH_0ZNZOBSDpTklSuJxB0ZlKtVkvVH2WZDcYhybar45CfV15sqIebVCn5_PQBrQlPc_n3r1DqyWiZbpIVxrJDPf-XPiBT30C4YjdUg-ukYBJvlFkct0iMJzN2h2i9ovzeFYX9-a691Rl-W8iMJcm8ttV0NNhvQ7OF9tsVYWSa7qsTA_QZUtZG0vnKvd6nXTRkmPpPff9YBOQgU1f5g9_Mka9TxuPvEFS3OwQp4XVOa3kN0TywrAwC7H32NMeENfuth_ya8UA1MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
دقیقاً همین عن‌مغزها ایران رو به این روز انداختن؛ حرام‌زاده‌هایی که فکر می‌کنن اگه چهار تا کلمه عربی بلغور کنن، سؤال اصلی رو جواب ندن و پشت شعار و توجیه قایم بشن، یعنی عرضه اداره کشور دارن.
🔴
یه مشت آدم با سواد صفر و ادعای صد، که هر فاجعه‌ای می‌شه فوری می‌گن کار دشمن و تروریست‌ها بوده. خب حرام زاده، پس نقش تو وسط این همه بدبختی چیه؟ تو که همه‌چیز دستته، بودجه دستته، اسلحه دستته، رسانه دستته، زندان دستته، تصمیم دستته، پس چرا هر خرابی و نکبتی که پیش میاد، یهو هیچ‌کاره می‌شی؟
🔴
کشور رو به خاک سیاه نشوندین، مردم رو فقیر کردین، جوون‌ها رو فراری دادین، زندگی رو از خانواده‌ها گرفتین، بعد هنوز با وقاحت طلبکار هم هستین. نه جواب درست دارین، نه عرضه مدیریت دارین، نه ذره‌ای شرف سیاسی که مسئولیت خرابکاری‌هاتون رو قبول کنین.
🔴
اگه نمی‌تونین کشور رو بچرخونین، اگه هر بحران رو با دروغ، تهدید، سرکوب و مظلوم‌نمایی جمع می‌کنین، پس این خاک مال شما نیست. تحویل مردم بدین و گورتون رو از این کشور گم کنین.
🤔
ایران ملک شخصی شما نیست که با جهل، توهم، شعار و بی‌عرضگی نابودش کنین. این مردم صاحب این خاکن؛ نه شماهایی که پشت دین و امنیت قایم شدین و هر روز یک زخم تازه به این کشور می‌زنین.
✅
@AloNews</div>
<div class="tg-footer">👁️ 33.7K · <a href="https://t.me/alonews/134512" target="_blank">📅 21:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134511">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">👈
گزارش الجزيرة: پدافند هوایی، سه پهپاد را در اطراف کنسولگری آمریکا در اربیل مورد هدف قرار داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 31.6K · <a href="https://t.me/alonews/134511" target="_blank">📅 21:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134509">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58f33a9d4e.mp4?token=OwWUnu-6NUGv2GRf9e7zU5eQpG8Pos7YibCpoDNPGs5ab7aZyDlFuIEJ8QHnjA_-oas0QvNC8eopeIBtDrqL3HozNHSnUbj_cuKN5ON5ahMG16eZ0LH9xv9uhQ6QX4TldZLXKZcYrWwo6hWKNLg6pCVgoJF1sbaOP77QceBzlkjzAqI9O3ndFGlHLy0k-nD269NqQuW3wYqQ_AE7NX7EWEZc-nAPUXctKKM2jetFqwFGr1LQSSRGDJNcenWAHluWA0rPqWf7Ux7D5lRh3F9cHqTZTf4ZavHfbsLR23Ev9DeiNKyU0_VS8iMMTphtJlqCj5niEfsqOSiYPisLSFerqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58f33a9d4e.mp4?token=OwWUnu-6NUGv2GRf9e7zU5eQpG8Pos7YibCpoDNPGs5ab7aZyDlFuIEJ8QHnjA_-oas0QvNC8eopeIBtDrqL3HozNHSnUbj_cuKN5ON5ahMG16eZ0LH9xv9uhQ6QX4TldZLXKZcYrWwo6hWKNLg6pCVgoJF1sbaOP77QceBzlkjzAqI9O3ndFGlHLy0k-nD269NqQuW3wYqQ_AE7NX7EWEZc-nAPUXctKKM2jetFqwFGr1LQSSRGDJNcenWAHluWA0rPqWf7Ux7D5lRh3F9cHqTZTf4ZavHfbsLR23Ev9DeiNKyU0_VS8iMMTphtJlqCj5niEfsqOSiYPisLSFerqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
آسمان اربیل لحظاتی قبل
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134509" target="_blank">📅 21:47 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134508">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
گزارش انفجار بندر عباس
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/134508" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134507">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1486415d12.mp4?token=BNLtWzx4Ixh0G0MY2p_Yax9blePwJORwsN2uabRFkoU7F3GBcnOq_dhlrUTtVKjuevwLpuupwtlQeCZpfnFkbHHwZEM0VCOq-nUlJymtVWNPSMTM4uYatX9LNsDTjB4ulkxz8jlJ2qeQthft7KBmTRqH2mR6S_xb8uOwoxrLLdMaVpvuvBXRopRJgbtH5N5p6cnHA21eguM83XDt3ZwCFeUE3G0GWFDL8tHmEkchg_MIym3BSdQWXOWlEQyUS7mVrdjy5D9IfW_6Az7SZOxlEBaKq9z2K3o6jfMJL4RRuahJeXnwxyFp2L4EkNX3h5ooNGLuNYjFO_wttOZQ9QZNZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1486415d12.mp4?token=BNLtWzx4Ixh0G0MY2p_Yax9blePwJORwsN2uabRFkoU7F3GBcnOq_dhlrUTtVKjuevwLpuupwtlQeCZpfnFkbHHwZEM0VCOq-nUlJymtVWNPSMTM4uYatX9LNsDTjB4ulkxz8jlJ2qeQthft7KBmTRqH2mR6S_xb8uOwoxrLLdMaVpvuvBXRopRJgbtH5N5p6cnHA21eguM83XDt3ZwCFeUE3G0GWFDL8tHmEkchg_MIym3BSdQWXOWlEQyUS7mVrdjy5D9IfW_6Az7SZOxlEBaKq9z2K3o6jfMJL4RRuahJeXnwxyFp2L4EkNX3h5ooNGLuNYjFO_wttOZQ9QZNZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
هم اکنون حمله پهبادهای ایرانی به اربیل به مراکز کردهای مخالف
✅
@AloNews</div>
<div class="tg-footer">👁️ 37.7K · <a href="https://t.me/alonews/134507" target="_blank">📅 21:46 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134506">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=fDVxiCw9xwwbDDyELuyXWPuy5TCRfD8l3_43df0MGoR6Z_zvLqWf7bGP_WwyJpy7T9eK1ZZfC0r8XiarOsT56A5PZAoaVOwpCHUjD3bJlLmKZtpf2-9zcftl7U7nqFdnZoDyAFvnlHQR_zlFS2bgJ9X7y9jyC8q1nWJpI6MjJzJJ_laWIw3-lH8iPoZmy2fo6di9yMHhhYtIft2Y88NsVJUWJwj0Glzwu4WMI2SGfgpiJvpN_D5lSe3IftL1e_NoGocbp3G_CI68ybQE6C3JW9HdkQ6J9EijDsFTiOS8hbn86z-9SWyJ38_qEGFGTFDaWz9UJSfsaqSXpdzKn2s0ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c22bbbdae.mp4?token=fDVxiCw9xwwbDDyELuyXWPuy5TCRfD8l3_43df0MGoR6Z_zvLqWf7bGP_WwyJpy7T9eK1ZZfC0r8XiarOsT56A5PZAoaVOwpCHUjD3bJlLmKZtpf2-9zcftl7U7nqFdnZoDyAFvnlHQR_zlFS2bgJ9X7y9jyC8q1nWJpI6MjJzJJ_laWIw3-lH8iPoZmy2fo6di9yMHhhYtIft2Y88NsVJUWJwj0Glzwu4WMI2SGfgpiJvpN_D5lSe3IftL1e_NoGocbp3G_CI68ybQE6C3JW9HdkQ6J9EijDsFTiOS8hbn86z-9SWyJ38_qEGFGTFDaWz9UJSfsaqSXpdzKn2s0ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
وزیر نیرو: با مشترکان پرمصرف برق برخورد می‌کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 41.8K · <a href="https://t.me/alonews/134506" target="_blank">📅 21:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134505">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
منابع عربی: چندین صدای انفجار مجددا در اربیل عراق شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 42.9K · <a href="https://t.me/alonews/134505" target="_blank">📅 21:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134504">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/slhuXkaIJhd21Zcv5M0vtsxnjRatmFEzFUjbJaDB4QxqPfBcejmfuFD_DMjtBL2j9bX7NFna6SznJJRwOdBA_9gijvEY62-2qUwgkSWDEgkKq9aOhcRyEFWXiXmGONl-WWj9KTPOFf_e3Jqo9OnXJnYqVC_3QNEsAYwvqtC9-ZQTVqF8H2ENuZQVXiRpljInlI70YHt3AJgKvxuB35aYG_hZ2f9oB_R3O9h856qWdKegc1vzawTZ4BdYYYhDAMPQJZAcJ7IkMocxP7vgMmEDC4SQTWbansA9NNVsog4eGSR_JkhAGi7Q_XggiLAbdQAxvfkcN-VEsYSi--f0_7Qwow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یکی از مقام‌های طالبان که خودش 63 ساله بوده، یه دختر 14 ساله به اسم نازگل رو میخره و باهاش ازدواج می‌کنه.
و اما بعد از چند روز، این دختر معصوم رو خفه می‌کنه و به قتل میرسونه!
✅
@AloNews</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/134504" target="_blank">📅 21:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134503">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🔴
فوری / فاکس نیوز به نقل از ترامپ : هفته آینده حملات به ایران گسترش پیدا می‌کنه
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134503" target="_blank">📅 21:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134502">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
اینترنتتون ضعیف شده ؟
👍
👎
✅
@AloNews</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/134502" target="_blank">📅 21:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134501">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">👈
قالیباف: به مردم جنوب کشورم که این روزها در خط مقدم جبهه قرار دارند، می‌گویم که از ابتدای جوانی دوشادوش شما خواهران و برادران عزیزم اسلحه به دوش گرفتم و جنگیدم، شما عزیز جان ایران هستید، جان ما هزار بار فدای شما، در مهم‌ترین سال‌های جوانی من و خانواده‌ام پای سفره‌های مهمان‌نوازی شما در مناطق عملیاتی جنوب نمک گیر شده‌ایم، گرمای عشق و محبت شما به هموطنان خود و به ایران را هرگز فراموش نمی‌کنم.
🔴
بدانید که ما سرمان برود، پای قولمان هستیم، شاهرگمان را برای دفاع از این مملکت گرو گذاشته ایم. به فضل و منت خدا بدانید که پیروزی ایران عزیز نزدیک است و مقاومت تاریخی شما ماندگار خواهد شد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134501" target="_blank">📅 21:23 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134500">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/obxLfUvoUiHWqJ3x7lTPuzwhWtl-a5Znqp82wAs7ehuX59wehIaKHlYg4ouWadtC3UyyslER7VyJfmEvk8VJHZhnAysEdthazYI0fVDGl-D3-spW62PlSxFUFIU0GGgtM6e0mrJ7T4jkQ1AiOn45DQ4CclQCJGh_zaFClLbxTZ3OohjwvMwbz86wNOn9IKNvzN7bSTO7jNzuRZNpL82P1WM5yK3ocqUCZvB5mfE58BlpJtvzVqK4IotXMWW8IpcdSDc6wKRpim7Z-xtGfoj1-ng4GZ47KeY3iLwoDxvaGTavdwUzyquoApUM3R_SdWaYjoe1Zy0s9EbclvyalnOiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی وزارت خارجه: ایران را نه با خط‌کش جغرافیا می‌توان برید و نه با واژه‌ها می‌توان تکه‌تکه کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/alonews/134500" target="_blank">📅 21:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134499">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
معاون رئیس‌جمهور آمریکا، ونس: ما قصد نداریم نیروهای زمینی را برای تغییر رژیم به منطقه اعزام کنیم.
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134499" target="_blank">📅 21:14 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134498">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
قالیباف: مذاکره در این مقطع همان‌گونه که بارها اعلام کرده‌ام معادل سازش نیست، بلکه در کنار جنگ،  بخشی از راهبرد مقاومت و صیانت از منافع ملی است.
🔴
این هماهنگی و استفاده همه‌جانبه از ابزارهای دیپلماسی و دفاعی، برای حفظ ایران عزیز نه تنها یک وظیفه بلکه یک ضرورت اجتناب‌ناپذیر است.
🔴
جداسازی و انتخاب یکی از این دو روش  به‌عنوان تنها راه حل، خطای راهبردی است.
🔴
ما در جنگی پیچیده با بزرگ‌ترین قدرت مادی جهان مواجه هستیم و در این جنگ افتخارات بزرگی کسب کردیم؛ پس باید فکر و عمل ما همان‌قدر بزرگ، پیچیده و مقاوم باشد.
🔴
این مثال را می‌توان در مورد  لبنان، رفع تحریم‌ها، آینده پایگاه‌های آمریکا در منطقه و انتقام وخونخواهی رهبر و سایر شهدای این دو جنگ تحمیلی هم تسری داد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/134498" target="_blank">📅 21:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134497">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cY5E2sGLxExHPvU5Eap6B8I5TSjjVWVHCBfWU4E3GNtu-y8mXJEwfX88FKTyx9tqzrwpptSCQJ4h5XINYjBazFeigUu8lcBiNVw2q8pY6gTFu4eDvZN6FH5HWuu7Pd9eg7VTS4kgh06FoMRMKu-cgKptSqQarWifBPp5jgZSBG_pEbapGvJ9tiG6ForyzD7Esbw9UMkE2vcbL2T_ahX92HVq6dbolyhM7ckpgI86hEUbGJikQ8DoyD3UtvA08tr_sslA1_W7V71bU6TQgy2-tB_S12a0M6ti8y49xGM4U5d99iekULGFb-QOPP8FEM4rRtm1UeIXdGP41-f01aVW8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
زیرنویس شبکه خبر :‌ وزارت آموزش و پرورش از برنامه ریزی کامل برای امنیت حوزه های امتحانی خبر داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134497" target="_blank">📅 21:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134496">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
قالیباف: ما باید بتوانیم بین دو روش نظامی و دیپلماسی، هماهنگی ایجاد کنیم و نباید از جنگ یا مذاکره هراسی داشته باشیم؛ جنگ و مذاکره دو  روش حفظ منافع ملی است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134496" target="_blank">📅 21:09 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134495">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">👈
قالیبلف: با شروع جنگ تحمیلی سوم در اسفند ماه، نیروهای مسلح ما کنترل خود را بر تنگه اعمال کردند.
🔴
در طول مذاکرات نیز ایستادگی و ترتیبات ایرانی تنگه هرمز را در بند ۵ تفاهم‌نامه تثبیت کردیم و آن را اهرمی برای اجرای ۴ بند دیگر ستانده‌های خود، از تفاهم‌نامه قرار دادیم.
🔴
حالا هم که به مرحله اجرای تفاهم‌نامه رسیدیم،
آمریکا که به لحاظ حقوقی و دیپلماسی دستش خالی است، می‌خواهد با زور ترتیبات ایرانی را کم ‌اثر کند، ولی ما بر پایه دستاوردی که در تفاهم‌نامه به دست آوردیم، باید بایستیم تا حقوق ملت محقق شود.
🔴
دشمن برای جبران شکست خود فشار وارد می کند ولی ایران با اتکا بر قدرت خود اجازه تحمیل اراده دشمن را نخواهد داد.
🔴
ما بر خلاف جنگ ۱۲ روزه، به درستی در جنگ ۴۰ روزه تنگه هرمز را بستیم چرا که باعث ناامنی و به خطر افتادن امنیت ملی ما شده بود. امروز هم امنیت ملی ما در حفظ «ترتیبات ایرانی» بر تنگه هرمز و عبور و مرور حداکثری ایمن و بی‌ضرر کشتی‌های تجاری از این آبراهه است تا برای ایران امنیت‌ساز شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/134495" target="_blank">📅 21:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134494">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4HqCVsGvJZVdnNrSCScSsuwa89b_jPAXLrlskNoXPlcOqXvAH6BCSO41XhRVPaHPqO7zHrM7VQpNj_w-_QezFnLaaOkXj-eb4Fs179boROCc0L-jRuhDGOYPMaS6_XHpnRxMFQPIz6Tf8jNcrswbrQ5iwdJDyGEMrU9QLKuZJYG__q6zvgimh9CLz_2jmOJWYvD6YykiKNELrg0KXSaIrxAWWnfEjBk_QeOUTMSTT-wctJSghjGjMnhgvuFe1jCY_XpW6wDFbeOEi1994mh9NAVvEgqToRVNTK4vIbiahMtc5hUqO29Pj_a4NwN-LsmvSSpUaliDWifHd5YdbyndA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت یوسف پزشکیان درباره موضوع انتقام
✅
@AloNews</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/alonews/134494" target="_blank">📅 21:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134493">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
قالیباف: تفاهم‌نامه زمانی معنا دارد که بندهای آن معتبر و درحال اجرا باشد
🔴
اگر قرار باشد ایران از تفاهم‌نمامه انتفاع نبرد، دلیلی برای پایبندی به چنین تفاهمی نداریم
🔴
باید همواره آماده نبرد باشیم و در کنار این باید از ابزار دیپلماسی و مذاکره هم استفاده کنیم تا منافع ملی را محقق و تثبیت کنیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/134493" target="_blank">📅 21:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134492">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
قالیباف: نگاه ما هم در جنگ یا مذاکره باید براساس منافع و امنیت ملی، واقع‌بینانه و بلندمدت باشد. لذا راهی جز تکیه بر توان خود و قوی شدن نداریم
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134492" target="_blank">📅 21:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134491">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
قالیباف: آمریکا در هر زمان که بتواند به‌دنبال ضربه زدن به ایران و پیش‌برد منافع خود است و این محدود به جنگ،  مذاکره یا فقط این رئیس جمهور فعلی آمریکا نیست
✅
@AloNews</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/134491" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134490">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
قاليباف: ما در یک جنگ جوهری و وجودی با آمریکا قرار گرفته‌ایم که هدف آن علاوه بر ساقط کردن نظام مقدس جمهوری اسلامی ایران به‌عنوان نهاد اصلی جبهه حق و چندپاره کردن کشور عزیزمان ایران است. این راهبرد دشمن تغییر نکرده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134490" target="_blank">📅 21:00 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134488">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mLt-DhRabEGngxiz2pcjxGgXvUx68WpPEMrMEtMp1yELs6aYqB5hfITVzDRPpVGcw5Eq98nb-P7oBRhQjAn4kbXImH5DVNkADu2AjErWn-FQo0cU2MIzIymTG_tOLJNo353qFUrWcLw7sqQx8BYislK4QwXMtSt66tWTGP7PRGfYipwvA7qaeRS3S10yCUtc-IARuEKWDSf7aw-6qpckJgYM2SkSuC7Xo2HCNh-1JcAiUB1-AAin3_fJyGC5TEjGU94HAo4ukq4zxVbVUDzHJQAiDzHsHE8Ay8Q7acL3-u9zgcg90opWKnuRoFnQ_UQE_lJJ7a2vL4EtbYpQ02mG6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/IFL39BXQ0b6BRrwmfvtqC9O5plI49P1lIlBeQXny7AreEJz6wv_zs9n_QfaLdz3-2wRM4_6R97VC-EEXII7tNDyBF5-op-L3bVxqVa549uz44GkX3HzoGLQcNYoHf39fCkqOIDoN_v8fH8rpXYRArsJQhNDUDDBfRqN1PnbDE_97SWyIMq4SBerHn5DFBwIOOqab6zMQU9v-SBciEbXX2s1R09iHJ-Auhhxsw0OCzi5Ef2hcTzX_6ImElWlgZ4hA6DcJ1w1m7lWhHhybicq2J0fKT8wDtjYyKg3Yd26thzmHpbgpqOqGvDX37uX0wHRVhCPoUjplZ_k0A5T51G8ZOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
سیلو ای هویزه در بخش مرکزی که هدف قرار گرفت
✅
@AloNews</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/134488" target="_blank">📅 20:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134487">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">👈
یک مقام ایرانی به المیادین: تهران پیامی خصوصی برای جی دی ونس، معاون رئیس جمهور ایالات متحده، ارسال کرده و در آن جارد کوشنر و استیو ویتکاف، فرستادگان ویژه، را به سوءاستفاده از اطلاعات محرمانه مذاکرات ایالات متحده و ایران برای منافع مالی و افشای اطلاعات حساس متهم کرده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/134487" target="_blank">📅 20:53 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134486">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
صدای انفجار مهیب در هرتزلیا در شمال تل‌آویو
✅
@AloNews</div>
<div class="tg-footer">👁️ 53K · <a href="https://t.me/alonews/134486" target="_blank">📅 20:48 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134485">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
گویا سامانه‌های پدافند هوایی یک پهپاد انتحاری یک‌طرفه به مدل FLM-136 LUCAS را در آسمان بندرعباس، سرنگون کردند
✅
@AloNews</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/134485" target="_blank">📅 20:44 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134482">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/VU9HWlpOrXW0M_Xzr2LB5G6-y5jHMS0YmaAD9VvaVw9cc_v-_9A-PR2Bk1V-uaJzAWlscHVYM0rm_3uWzwv8qzoTfpyPtWp9SlJj41jgEIPNqyPdztU3WBi6pC2Ih5JyGN_5gOG3mkJ8zVlpfmrwh6fvd38kLuXKX5wXjh7i3g9RuQbbCVlGGpZAr2oVIrWCoCt7tKQ3cZLLLAMTHC0cGj6hde_tftcLCre-Qp6JM5wrbi6XPeugX4MGq4V8oDl9iNJPgj1gK3TFT72yag-VcfUpH48RuKGY1SxXRDLjXQp2Z9UvMitZ5BvNZ1zxhNCc83NZL3_Y5XToWdFkJ4tYhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Qu8DefpiBhBcdsDbi97H5ilRnhvV3IJYqlyk2jt8zESF6Acgmh4Lj54yu_oG5sXjL1QUjSO6ZyOwCyOCyDeqWn7u5JcctG8oUwx6W37gjKTV4oJBbao0UCD-Xm6nyoHKk4XHUtTY3YXe4pdmU5hOEa6n4G_jH_SSuud2fwovLqq8jjGxs6C19MV9Ppdwhsbzlo8JvcICRRywysLKU3nEI4unaxQlPY4y_WSDl1lsQYppxONSqZS86txPCeZT-K0FjCii71Y8KS14JFnZCnV6HRMTU7KsPsFjGs5LIQhIG8dJh_IdjTf7vhUYgOayJanY19PNK17o_BsoWuf4BooqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hOCLPNwAYasCo3AoXfjVjU3y1sCuk0pwbCpnItHQMVmQ50nsfPIWUBAeF7rlV7OI64kBAMc8hua-5Xj-E76zKpEPRYKuoivn4AHHUimXTI_kNfHTeC3tNvVZsKi4aVn0TI531gzxq2l851bp0cXB4IGRk5472pwUlF6Uj-yHpNZX88jw0jSv2DsEEGrurczzrRpR9k1eNOVtEcx83Klz-AbXPPgRKwlsSD3WIfD52VjONxIP4j4TgXUgNaFuYv8vvJkNo1SzrWrSBXHqj7UXPHzN_1ja5nuAJQCEcUEocJ8vcL-oUCUSjNnGdHDJglmsVUelF_qL_q4xR0IxnSaqxg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
خبرگزاری فارس با انتشار تصاویر بالا مدعی شد:
انهدام پهپاد آمریکایی لوکاس در بندرعباس توسط رزمندگان سپاه
این پهپاد متجاوز ساعتی قبل با رهگیری و شلیک موفق سامانۀ پدافندی رزمندگان سپاه در بندرعباس منهدم شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134482" target="_blank">📅 20:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134481">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">اخبار جنگ الونیوز AloNews
pinned a photo</div>
<div class="tg-footer"><a href="https://t.me/alonews/134481" target="_blank">📅 20:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134480">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9n6wMr8FeN40rUfYN-L_-Ja0mtAiQRxxMeu5cKj3jvxg-76MzYqJkzwoIH2xdF8F8wBL53iMvP1MOx-KoGLjJ56GqIGCk3BZq5dswmm46P9-Gv_AUHwszx53aq95r3Z_3-pJGZKk6yMvGBgddz6z7jGcZNOEo7jBQqm5LERTt5KMW3WL3HxDQGF6Q9K4Tf9spwn11ckZKO_6mHGv0xpylK2FTbnYX6gj7iPVoAm-mNm6hM6WK6BEdiLncE5g7NyqH-FCXzgBLxQSwIxdUNNXDOBLHds121G27oUsnTvazXtETE9kMzlOtHppgVR9Dc3-G7o1D0VWjjSqYAXOuyVOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚘
✨
رضائی موتورز
✨
🚘
خرید و فروش خودرو | ترخیص سریع و مطمئن
🔹
خودرو: ملی | گذر موقت | مناطق آزاد
🛳
ژنراتور: ارسال و ترخیص
🌍
صادرات و واردات قطعات و تجهیزات
⛴
ترخیص کالا از ایران و امارات
📌
بهترین قیمت، سریع‌ترین خدمات
📲
موجودی و قیمت روز وارد کانال شوید
👇
👇
https://t.me/rezaei_motors
https://t.me/rezaei_motors
https://t.me/rezaei_motors</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/134480" target="_blank">📅 20:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134479">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">🔴
فوری / صفحه امور کنسولی وزارت خارجه آمریکا در شبکه ایکس با صدور هشدار سطح چهار و بحرانی از تمام شهروندانش خواست، فوراً ایران، عراق، لبنان و یمن را ترک کنند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134479" target="_blank">📅 20:32 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134478">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">👈
پروازهای شیراز – دبی پس از پنج ماه از سر گرفته شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/134478" target="_blank">📅 20:31 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134477">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">👈
ترامپ: یکی از بزرگترین نیروهای محرک آینده برای مشاغل، مراکز داده هستند. آن‌ها بزرگ، قوی، جسور و ماشین‌های پول‌سازی برای ایالتی هستند که در آن ساخته می‌شوند. کاتی هوکل، فرماندار، به دلایل سیاسی، تمام مراکز داده‌ای که در حال ساخت هستند یا قرار است در ایالت نیویورک ساخته شوند را لغو کرده است. این شرکت‌ها اکنون در آلاباما، فلوریدا، تگزاس، آریزونا و بسیاری از ایالت‌های دیگر جستجو می‌شوند. هم مالیات‌ها و هم میزان مشاغل به طلای مایع می‌رسند! ایالت نیویورک تصمیمی فاجعه‌بار گرفته است.
🔴
تمام این درآمد و سایر مزایا به ایالت‌های قرمز و برخی ایالت‌های آبی خواهند رفت، جایی که مراکز داده به عنوان گاوهای شیرده پول با مالیات‌های پایین‌تر و مشاغل بی‌سابقه جستجو می‌شوند. آن‌ها باید هزینه آب و برق خود را بپردازند و هر مازادی به ایالت و جامعه محلی بازمی‌گردد. مراکز داده پیروزی‌های عظیمی برای ایالت‌ها و جوامعی هستند که خوش‌شانس هستند و آن‌ها را به دست می‌آورند. نیویورک باید سیاست خود را فوراً تغییر دهد. نباید به دموکرات‌های رادیکال اجازه داد که باعث از دست دادن مراکز داده، هوش مصنوعی و تمام این فناوری‌های جدید باورنکردنی برای چین و سایر کشورها شوند! پرزیدنت دونالد جی. ترامپ
﻿
✅
@AloNews</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/134477" target="_blank">📅 20:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134476">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/RrF1MNsX38pbB7TyopusK8MrXBfWTuVkLjdhyriK6mf-OLoAsG5iv2cdnUddS62cy925L64qlVFfwe8r7CyOWPmbaFFaklXpViskZoCmCDGlN7c8fnehbCFhbvbkJ8LY6y_VNyGth8J5_O_KSioQl7Jo0eDQEOgdJeIN0-HMKF_DsgGl2VST5v2p0Z4vM0t92Te5h7l4ttPUAFKEzYRIC37KeMPhXf9YvzH7D1iphNZVPxbf7eSs8sFEJt4muaxLO8vtTt9B-RnD8Ktkpgi7tVhwN_yP7vrcmFBWiFbUfywo9Q3PpeWyS4ncoRLoNni5ELs7xb5tMa7s14cvRx0wIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کاخ سفید در حال بررسی تمدید مجدد معافیت‌هایی است که به کشتی‌های خارجی اجازه می‌دهد کالاها را میان بنادر ایالات متحده جابه‌جا کنند.
🔴
این تصمیم در شرایطی مطرح می‌شود که تنش‌های تازه با جمهوری اسلامی ایران، نگرانی‌هایی را در مورد قیمت انرژی و اختلال در زنجیره تامین ایجاد کرده است.
🔴
خبرگزاری رویتر به نقل از منابع آگاه اعلام کرد دولت ترامپ در حال بررسی اعمال محدودیت‌های جغرافیایی برای کشتی‌های با پرچم خارجی است تا ضمن حفظ ابزاری که به کاهش فشارهای زنجیره تامین کمک کرده، به انتقادات گروه‌های صنعت دریایی و متحدان جمهوری‌خواه نیز پاسخ دهد. مقامات کاخ سفید به همراه وزارتخانه‌های انرژی، حمل‌ونقل و کشور اوایل هفته جاری برای بررسی این گزینه‌ها پیش از تصمیم‌گیری نهایی در پایان ماه ژوئیه تشکیل جلسه دادند.
🔴
یک مقام کاخ سفید در گفتگو با رویترز، با اشاره به اینکه معافیت فعلی تا ۱۶ اوت اعتبار دارد، تاکید کرد که هنوز تصمیمی درباره صدور سومین تمدید اتخاذ نشده است. او افزود که اقدام قاطع رئیس‌جمهور ترامپ در لغو موقت «قانون جونز» به جلوگیری از کمبود در زنجیره تامین سراسر کشور کمک کرده و دولت به طور منظم نحوه استفاده از این معافیت را رصد می‌کند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.2K · <a href="https://t.me/alonews/134476" target="_blank">📅 20:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134475">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/134475" target="_blank">📅 20:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134474">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">👈
بلومبرگ: نفتکش‌های فوق‌بزرگ به‌طور فزاینده‌ای هدف حملات در تنگه هرمز قرار می‌گیرند
🔴
در ماه ژوئن، پنج مورد از نه حمله به کشتی‌های تجاری، علیه نفتکش‌های موسوم به «بسیار بزرگ» انجام شده
🔴
این نوع کشتی‌ها، ستون اصلی حمل نفت خاورمیانه به نقاط مختلف جهان به‌شمار می‌روند
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134474" target="_blank">📅 20:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134473">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
نیروی زمینی ارتش: پاسخ حمله آمریکا به ایرانشهر را خواهیم داد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134473" target="_blank">📅 19:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134472">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
انفجارهایی در اربیل عراق
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134472" target="_blank">📅 19:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134471">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134471" target="_blank">📅 19:49 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134470">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
کرملین: اوضاع خلیج‌فارس رو به وخامت است/ جهان نمی‌تواند نگران نباشد
🔴
پسکوف، سخنگوی کرملین: متاسفانه اوضاع در خلیج فارس به هیچ وجه پایدار نیست و بار دیگر وارد مرحله‌ای رو به وخامت شده است و این وضعیت نمی‌تواند نگرانی جهان را در پی نداشته باشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134470" target="_blank">📅 19:45 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134469">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
سی‌بی‌اس: ذخایر موشک‌های تاماهاوک پاتریوت و تاد آمریکا به شدت کاهش یافته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134469" target="_blank">📅 19:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134468">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134468" target="_blank">📅 19:37 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134467">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/moSn9qGzXxp4W2YmC4k7NfHVhfd5hYrfMGZyHEx6Fap9QfNpeQfgVatLnRVY8tLM3nvImHNMtCPuJQBO2xnEiVuPQlxWe00_hL4kQI-ArKHsr3iqUewOgHcplYTF_Jj_S30hh-NAvU-Nr0LNpSnnr44x9KYU3qKFML74-UqKjphfSbbqba_sb07wOWgqnOmbfe-8oWCb-VoLndqWL2yhIyiyd22spNfIGngowd0GkA9yR3UIeSnvMTO2XntpQ2VogjaPcfjp7gxBlg5eD_4q_z16s0hBlhw-3yZ1ZseX7-UsQg6UfROC7SpyC7T2tV002heivdRjlm2J_N0Bpnmkrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سنتکام: ما به یک انبار ذخیره گندم در هویزه خوزستان حمله نکرده‌ایم ولی در عوض ایران به کشتی های حامل گندم در تنگه هرمز حمله می‌کند
🔴
ایران در مقابل، غیرنظامیان و کشتی‌های تجاری در حال عبور از تنگه هرمز و همچنین کشورهای همسایه حاشیه خلیج فارس را هدف قرار داده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134467" target="_blank">📅 19:33 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134466">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
بقائی:  فعلا برنامه ای برای مذاکره با آمریکا نداریم ، روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/134466" target="_blank">📅 19:30 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134465">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔴
فوری / صدای انفجار در کویت شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134465" target="_blank">📅 19:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134464">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">👈
بقائی: فعلا برنامه ای برای مذاکره با آمریکا نداریم و روی دفاع متمرکز هستیم!
✅
@AloNews</div>
<div class="tg-footer">👁️ 64.4K · <a href="https://t.me/alonews/134464" target="_blank">📅 19:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134463">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
موافقت شورای نگهبان با جلسات مجازی مجلس، در صورتی که جلسات به شکل حضوری در ساختمان مجلس از نظر هیئت رئیسه ممکن نباشد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.3K · <a href="https://t.me/alonews/134463" target="_blank">📅 19:22 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134462">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oJjKYLfOsj6R2XfpYS4UwvbO21TrM9tx7vTnKKdqfCHBfukfRfGMFxGnpJ5Me5GBuFtKHIVBkMN9hRYU2lL4GoTivV-OfeJnNgMhx-j47F4EYC8FHprQE9P6RAJnxgZxN_161zyliIeCp9iz1Dq5ymkBTS3buHjqPdf75KjlqndKDuzujNqh747OpJ8Hi3zp_xYoCgogL8DGweIl2yufi580M1ZoNieRYSEoiOTt-DYcNkMcpBJKD4ctECQmArj9nFaEgWHCEUVrgQ6dHFIwyVk9f43ZxKSnOwYqC4sabrIDTjekYGFBQIZM7fDEwj55fNLw1B4lkYbbdY1lZvM6bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📷
استوری حامد‌لک:
@AloSport</div>
<div class="tg-footer">👁️ 63.3K · <a href="https://t.me/alonews/134462" target="_blank">📅 19:18 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134461">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
خبری که تحت عنوان اعتصاب در چارسو دقایقی قبل منتشر شده مربوط به گذشته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/alonews/134461" target="_blank">📅 19:13 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134457">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
وزارت خزانه‌داری آمریکا از اعمال تحریم‌های جدید علیه ایران و روسیه خبر داد
🔴
وزارت خزانه‌داری آمریکا روز چهارشنبه چندین شخص و نهاد ایرانی و روسی به را به دلیل فعالیت‌های مرتبط با اشاعه تسلیحاتی به لیست تحریم‌های خود اضافه کرد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134457" target="_blank">📅 19:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134456">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
رئیس ستاد ارتش عربستان با معاون فرمانده سنتکام دیدار کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134456" target="_blank">📅 19:05 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134455">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
فرودگاه بین‌المللی صنعاء به چرخه عمل بازگشت
🔴
وزیر حمل‌ونقل و امور عمومی یمن: فرودگاه بین‌المللی صنعاء پس از تکمیل تعمیرات ناشی از حملات هوایی ائتلاف سعودی، به‌طور کامل به چرخه پروازها بازگشته است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134455" target="_blank">📅 18:55 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134454">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بقایی: تفاهمنامه مجموعه ای از تعهدات متقابل است و در صورت نقض از سوی طرف مقابل، ما نیز از اجرای تعهدات خود خودداری میکنیم؛ این یک اصل است و در ادامه نیز همین مسیر دنبال خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134454" target="_blank">📅 18:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134453">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دو انفجار شدید در جزیره هنگام شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134453" target="_blank">📅 18:41 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134452">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
فایننشال تایمز: ذخایر بازار نفت در حال اتمام است
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134452" target="_blank">📅 18:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134451">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / ترامپ: جولانی می خواهد وارد عمل شود و حزب‌الله را از بین ببرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134451" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134450">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
منابع خبری از حمله توپخانه‌ای ارتش اسرائیل به شهرک عیتا الجبل در جنوب لبنان خبر می‌دهند
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134450" target="_blank">📅 18:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134449">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
تعداد موارد ابتلا به ویروس ابولا که در جمهوری دموکراتیک کنگو شناسایی شده است، به ۲,۰۱۱ مورد رسیده است که شامل ۷۵۴ مورد فوت نیز می‌شود.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134449" target="_blank">📅 18:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134448">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
دقایقی پیش زمین‌لرزه‌ای به بزرگی  ۳.۹ ریشتر با مرکزیت انبارالوم آق‌قلا، گرگان را لرزاند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134448" target="_blank">📅 18:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134447">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
دو انفجار شدید در جزیره هنگام شنیده شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134447" target="_blank">📅 18:16 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134446">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
طبق گزارشات، تا ساعتی دیگر قالیباف درباره جنگ و تحولات کشور یک بیانیه مهم می‌دهد
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134446" target="_blank">📅 18:12 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134445">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
اکسیوس به نقل از یک مقام آمریکایی:
مذاکرات اسرائیل و لبنان در رم مثمر و مثبت بوده
🔴
بر سر ساختار و دستورالعمل‌های مناطق آزمایشی توافق شده
🔴
اجرای مناطق آزمایشی طی چند روز آینده آغاز خواهد شد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134445" target="_blank">📅 18:11 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134444">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HouZT4tgB7Cf3fD1W_rfXtN3emmY89Y_Yt7f3rH0h9bTeFaDnyD3In5oIBJOzZLm89bDlxEtC8yWis3tHKR_ZZJ8un2z1rHk3jot40HKlPtf1dZYYMpggI1JUfHneHuM2XFEmizGn0XuMQaFirCE9_cJZAHZ1hGPXSPX6nIqNX_PRN-hPM8z8Bm2vogkh9Ry6zo3eV72HaRaOPjIqj-zKNtwJzBGcUy2jVPggUGL6rRnPGpymvr72y31Y3fdASXb62Aj1Q4sw8ahsYPkUg-bp60LBtVp0s_TaQ5VqdNXikoWEvCXMx1ymS2LVvJE1-q9jfQmwU43Tz2GZ5gVd5J5wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
علم الهدی، امام جمعه مشهد:
موضوع خونخواهی آیت الله خامنه‌ای فقط بحث حکومتی نیست، بحث اسلام و دین و قرآن است. ما الان ولی‌دم هستیم و باید انتقام خون رهبر شهید را بگیریم. این تکلیف شرعی و دینی برای امت اسلامی ماست.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134444" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134443">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yt4LgrDrdP3Hg0JW0t3eNQzjJQmB9brtzYhRLzDKZIgHLwxXMcjK3uF1i9FZn2h74UKEYXXKu0RIAcgP8jgjdeIVFO0rZ1d1x2EkZ-9jUoBLCAQV5XNPj75e4AIypZcActV_Br257oE4CeTujVCUrZye3pv21-LaAeWYXDaO-lb3hMi1dk3TmmNFKwnjSVOoldk2TNOWCOxPViXmaccDh5DYVEkZOy6twuq43sHAgdnLoYRfo106x4qZd2N2D386RoYXzdxBTmWta0nUTtpQ4_jlpZVdGztxSw46g224JB932yRTvEKwl59zQNbm-_PYCF0C_rBaKT9ql6jksXYF1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش: به وزیر آموزش و پرورش مهلت ۲۴ ساعته می‌دهم تا آزمون نهایی را برای همه استان‌ها به تعویق بیندازد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134443" target="_blank">📅 18:07 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134442">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-text">غزه که نرفتید
لبنام نرفتید
سوریه هم که گفتید آسمون بسته هست
حداقل جنوب ایران برید یا دیگه گنده گوزی نکنید، زندگی مردم بگا رفته
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 64.3K · <a href="https://t.me/alonews/134442" target="_blank">📅 18:04 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134441">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BMfv13-tvulJjtw48XhY5dcGDyTp6zJzr1lX86cv15fLT5dC8LCD9dmVljd19N0cV0WJEmBsfKu3aFO9auPD6Ia6rxMjf2Gr-zPtQvBMdW7g5XamXsQ9qp-9cOF9rF-3P3hrIE3EESXk_chJQASRtsVIOS2YgwNPPD3HKdqLwR5-BcuGsfRCqkblgxa1iovZ59390IVjQaGPK2S17z4itq5OWjYhqUic2_v2TIgE3tPbTM_KioXmWM0hn8hW4GveQ4r0ZUawZrt6ZBi4hFyeW3-RScueF3o6Wz_KkGdiy1gEc8bB0a5vz5UDMOWfAZLhoJQOuv3E3-EmJHeXc84SVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سخنگوی کمیسیون آموزش:
به وزیر آموزش و پرورش مهلت ۲۴ ساعته می‌دهم تا آزمون نهایی را برای همه استان‌ها به تعویق بیندازد
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134441" target="_blank">📅 17:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134440">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ترامپ: ما نیز خواهان توافقیم
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134440" target="_blank">📅 17:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134439">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/54a47ba115.mp4?token=MNIifgMEEz9kC5_a1kX_No_56PjB3PWpfNLPb5bKEFZ7eIbHdO_FG7L2t-PNgrM_aJYH6teobFfrI1r-wzLLhKVwORBY9P79rYdhFtYI4fnXqg9JwtJEOzO-DIhbpUb0lQ_0ssTNxlDprv5QC2_E-N41YJe6GQtt4FumF6FaHwJK6rwg0LYQn0Hical9u83bzxlP7oUnE-zJmI-f9HjTuAbVKjChwfnfDnLDhfaIiAfkUYXJ9HlIFQGI6A1w-CRpmLCoNQb2MbZcZFS--6P8fmbr9jpFZWHK81nEEbRUEFUs3j8hLfabPyhuKnIhaj-hB7n1coatXU4Nzrp_N8zeoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/54a47ba115.mp4?token=MNIifgMEEz9kC5_a1kX_No_56PjB3PWpfNLPb5bKEFZ7eIbHdO_FG7L2t-PNgrM_aJYH6teobFfrI1r-wzLLhKVwORBY9P79rYdhFtYI4fnXqg9JwtJEOzO-DIhbpUb0lQ_0ssTNxlDprv5QC2_E-N41YJe6GQtt4FumF6FaHwJK6rwg0LYQn0Hical9u83bzxlP7oUnE-zJmI-f9HjTuAbVKjChwfnfDnLDhfaIiAfkUYXJ9HlIFQGI6A1w-CRpmLCoNQb2MbZcZFS--6P8fmbr9jpFZWHK81nEEbRUEFUs3j8hLfabPyhuKnIhaj-hB7n1coatXU4Nzrp_N8zeoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ریک اسکات، سناتور جمهوری‌خواه:
ترامپ نمی‌خواد وارد جنگ با ایران بشه.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134439" target="_blank">📅 17:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134438">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
ترامپ:
ایران مدتی پیش با من تماس گرفت. آن‌ها می‌خواهند یک توافق انجام دهند.
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134438" target="_blank">📅 17:38 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134437">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fE4aLldYfNaJfWdv52g5Ds6DkqeEXE3b86Au2h9KN0vVHKPs2mGFS-60yThE7s4sR0U-wtJDaQv7BP7T_CsT21XGvCVx0DSO2j2KTrmGhgZduG3GGrSi7Z8Y8P7ejiEvs5lM39l051Z3O82Qb7Dtb-n_yEPJ_UHR6c0nvmQJcXTyW86rAtLbHaJZOVib6Ux1MqrU1tHqiupfgNIbK5OF33BvWmAgBhslwsHWvy4jBlaQlw0iYsoDE7n7asTm0QX5tGY3wBdGpqBICaxR-VByhH5tykJIiKONiU4Qibk2yZJecl04umfkehjltIkLUdxyg5Io31CvB3YL7q_PVFFGMg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یادی کنیم از روزی که رسایی و دوستان کفن پوش رفتن فرودگاه مهرآباد و گفتن مارو به جنگ اعزام کنید
🔴
الان که جنگ خودش اومده نشستن تهران زیر کولر دارن آلاسکا لیس میزنن
🔴
همینقدر بی....(ایمان)
✅
@AloNews</div>
<div class="tg-footer">👁️ 74.5K · <a href="https://t.me/alonews/134437" target="_blank">📅 17:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134436">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ogaSt9fgr6mwPN1YeuVTCwHfuypS6bD-O0IV9kCX6AsEOjWSmx4yvoT4rZbsHwbQSz6mTILguy9_JspN8gcVp6k9igFh3TT_mOThBbvk9vSQmB_Q4fNp5u_tHQtn5Vlevzs_3G0ZedkqcH5ZWlduO8kwMxgt8YFv1Q1J-NF0dSabRnEe-590SyvpZh-OlJWYGXgbYTXeLWpg5WVBzwm0NeVrnAc46ZXpt8WFBNTcAR9dCCZWQ4lU4_e7eVS3TMsufKNNyztqXKyrlwfImEGSRlIwOjdYhMrWOZzfODAgNIBlkOq1zT-GPsPQ43rznMdfO_i8uPPKBT84PXlM0UNATA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دلیل حمله اتمی آمریکا به ژاپن این بود که امپراطور و رده‌ بالاهای ژاپنی در توهم این بودند که درحال پیروزی هستند اما یک روز صبح صدها هزار ژاپنی تنها بخاطر توهم و غرور عده‌ای محدود کشته شدند
🔴
دلیل جنگ هم کاملا مضحک بود
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134436" target="_blank">📅 17:26 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134435">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PKHEyfiJ8zK1otky3scOCMRga64MzmnY-SSyNHON0_hTJYxv06PgK1fMwpRAl9hnn39HoUgBHEIzUhrUg8U1fjvtvNxARN8vKISyyUOHGMNufWkz-faodqnJ1K8VCoi0g4WjwkBeForuzxBR5kEg2OdaBbDh_3YyyX0LBzAjRoZs6U-EL-sEKVECYAzLety5iVxK-O8faC-b1NU3dUHg2gsN8jer73PjMDnt0irtw61BY1pEmdbZxjP65_mAb1hX_wK8LVXzaG0iRPAJhoFkkr6oLfNvt3y_mank-DnCVIQJ8S6arRiV0vn47dqof7zhJOd3gbYbcU3dbdWLy2fcrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مهدی مطهرنیا:
احتمال حمله اتمی به ایران وجود داره
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.5K · <a href="https://t.me/alonews/134435" target="_blank">📅 17:20 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134434">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
قیمت بنزین در ایالات متحده با افزایش ۳ سنتی به ۳.۸۹ دلار برای هر گالن رسید. این رقم مربوط به میانگین قیمت در سراسر کشور است. به گزارش شبکه «سی‌ان‌ان» و به نقل از انجمن خودروی آمریکا، این افزایش ثبت شده است.
✅
@AloNews</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134434" target="_blank">📅 17:15 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134433">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2816fc5cf7.mp4?token=fLj2rceuCb5VH_a5wdoQF7aaVvtB9z19UZv-kE7hm70NMi7lOGnde21yD-say9RsjNCa_8kguf5nDebHocgWhhgnjUm32izhwSq9w6dYlQSbifwyIViM69kJJkCIPAJSiAO7BX18M2KLcrjkwL81VFleOBMgOIAGvmgX-4uP3bXxQmCPB-4v8by5r10W7SI94jXjz9XtoYdI_zB9tSBtn8wqvSTtlUPWDFQtN_NtuRJBpgijAugWnhABZxaZJ_Mg634-5Aqmg3TXk7wVLNu8P4GqEbL8Ds3hFszViGrdqUB-GFCXvrnwfTCQhd9PLKmbukaoOfZVGXsekp-Duy0W-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2816fc5cf7.mp4?token=fLj2rceuCb5VH_a5wdoQF7aaVvtB9z19UZv-kE7hm70NMi7lOGnde21yD-say9RsjNCa_8kguf5nDebHocgWhhgnjUm32izhwSq9w6dYlQSbifwyIViM69kJJkCIPAJSiAO7BX18M2KLcrjkwL81VFleOBMgOIAGvmgX-4uP3bXxQmCPB-4v8by5r10W7SI94jXjz9XtoYdI_zB9tSBtn8wqvSTtlUPWDFQtN_NtuRJBpgijAugWnhABZxaZJ_Mg634-5Aqmg3TXk7wVLNu8P4GqEbL8Ds3hFszViGrdqUB-GFCXvrnwfTCQhd9PLKmbukaoOfZVGXsekp-Duy0W-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدئوی حمله سنتکام به یک لانچر موشک ضدکشتی در جزیره تنب بزرگ در خلیج فارس صبح امروز
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134433" target="_blank">📅 17:10 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134432">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c482140313.mp4?token=F-L2GOLbmAC2n-u-w72uRlWsAb8JFlRTnhDrFeG1j_lXrHW4zlgvcCLNUvoFADSYnj52UHBLZqRa1t0Ton8gOWWunMJq1Hten_t4E_GlldGnlx0CvKIC4EzlidcIzEg19BYQTeFA8Sq0YjFoPJ7zG81NC729TkuQ_8Z9TOn8tQikne_r_Ilm30QaRHGMmeef1ayklYhYnfife4zNVZq-_Y4x7ljdXRkNm4KHpwDDxGkLZyaLjWiSPIJSNiO0Zx5i22Pk7uBLsP3-ByCttw0_H48UgWQbEwtpM-lY1uok3u45TU8vh5Qx-bKPJ5Pl-iYTNydWpydfTrLvsfWwtK1QFEskQXZQRjz0JJJmGu4FtTnPf6dio6RvRgzqUiwJd7Hay2bSVTWwKi3ZYSGz0baHx7i_qA1HVSieHn3px0lbgSz-nGI2F6KN-rISHclZX1akxNBRnVGNGdhUcn6m7k8LsQmvn77OFoOP8a98dH2v1EyNk61kDxXQxlorGGkuatGZxYEOg50WHl4FOeh1KvmjLFtDhi64Jqw_XIeQ-3H7AXBSvhlvtg-mlnUhyjzZ2j1IcAfMuWbBHEXMFvyHAJXee_G2B09_hi9lrYCVuek1pDlgoJFr12zkmgEFUG4PZTFy1s6uIhyWJzk8qCdFDAbsJnSfflDdVa_sgw0MZsDNDpM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c482140313.mp4?token=F-L2GOLbmAC2n-u-w72uRlWsAb8JFlRTnhDrFeG1j_lXrHW4zlgvcCLNUvoFADSYnj52UHBLZqRa1t0Ton8gOWWunMJq1Hten_t4E_GlldGnlx0CvKIC4EzlidcIzEg19BYQTeFA8Sq0YjFoPJ7zG81NC729TkuQ_8Z9TOn8tQikne_r_Ilm30QaRHGMmeef1ayklYhYnfife4zNVZq-_Y4x7ljdXRkNm4KHpwDDxGkLZyaLjWiSPIJSNiO0Zx5i22Pk7uBLsP3-ByCttw0_H48UgWQbEwtpM-lY1uok3u45TU8vh5Qx-bKPJ5Pl-iYTNydWpydfTrLvsfWwtK1QFEskQXZQRjz0JJJmGu4FtTnPf6dio6RvRgzqUiwJd7Hay2bSVTWwKi3ZYSGz0baHx7i_qA1HVSieHn3px0lbgSz-nGI2F6KN-rISHclZX1akxNBRnVGNGdhUcn6m7k8LsQmvn77OFoOP8a98dH2v1EyNk61kDxXQxlorGGkuatGZxYEOg50WHl4FOeh1KvmjLFtDhi64Jqw_XIeQ-3H7AXBSvhlvtg-mlnUhyjzZ2j1IcAfMuWbBHEXMFvyHAJXee_G2B09_hi9lrYCVuek1pDlgoJFr12zkmgEFUG4PZTFy1s6uIhyWJzk8qCdFDAbsJnSfflDdVa_sgw0MZsDNDpM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تجمع و اعتراض متقاضیان خودرو سایپا به دلیل تحویل نگرفتن خودرو
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134432" target="_blank">📅 17:08 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134431">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
کامران یوسف خبرنگار پاکستانی: پاکستان به نظر می‌رسد یک گام به عقب برداشته و پس از آغاز دوباره درگیری‌ها میان ایران و آمریکا، رویکردی «صبر و نظاره» را در پیش گرفته است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134431" target="_blank">📅 17:06 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134430">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن…</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134430" target="_blank">📅 17:01 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134428">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن…</div>
<div class="tg-footer">👁️ 71.5K · <a href="https://t.me/alonews/134428" target="_blank">📅 16:59 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134427">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/hOqNEGYpx8SXyW-RUH5asCmRnK2wm-UvRtFqew4COAOQFJH0O4dFV9S1BchrviawaxHOT-HU4Vey2AemBiQLCyo0sydmZxcELvdg3mUGXXVSkRuqFCxc0lDH8uABMUZYMdBvauWgDsa60hcVW0xtYgk-S5zE-6hj5_dYk7GAU5ja8ZXdvM2FHCyMSn3IbsDfc3CCHb-Vt_XL5rUMB3ezCPOUnnosaUqSXc7QuK0PLh0BWBR8Gc8HFO0YoEf42_XqbsNTpXvszQ3xTevhD8hPYGqAkvoiTZPPLC4QTlXUxmOUc8Tfx8quKa_FoXaU-0JZfEx5WjzljGE-nPvJN6T6vw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
یه کارزار راه افتاده که میگه کسایی که موافق جنگن(بیشتر جبهه پایداری(خوارج) و وزیر اموزش پرورش و نماینده های تندرو مجلس) به جنوب کشور فرستاده بشن و اونجا اقامت داشته باشن و کارا رو جلو ببرن تا از درد و رنج مردم جنوب که هرشب حمله بهشون صورت میگیره اگاه بشن
😁
به شدت داره وایرال میشه و همه دارن امضا می‌کنن!!
اینم لینکش
⬇️
https://www.karzar.net/333344</div>
<div class="tg-footer">👁️ 77.6K · <a href="https://t.me/alonews/134427" target="_blank">📅 16:57 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134425">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/63af64b487.mp4?token=YwRWHs0wlU6MDJvc8UUJAtqY7ifDe1CKCzQR7l_Ib34YVj5mLka2IYGb9xUR_h_RktIys9oPGl_s-sEw1Mj-E7zsJ6VOXgjXd7Lu_Rm05HhWsbs-ntSufLx4OyPlj_QlN6xmHIdUxOSO0rSj3_EiaO2rXHHfsr9Dq_YB3S_6UmwBPYz8YnDUHML8gfu_h9_K5IJqXnmcVPogC8Bjqecno2o6CajOxugKurkJ9ySQYMeLlZmPWSWY8WCPP2X1w3acb6f2auVGHyJg6XkJfD3u51RrItbrnsKm3_3m1gXBSofXRyK3TqeTC_AT6XqShrrkoCCPzCf0x4b0JKwINtzPTyfju36WQQwvdOZw23A_D0d4p1IXYDTngca1Hkj2nfiMPAypsjQ_VPIMHbtL_hqhpdHDtV5sNBp2M0q8Bf-mTypmsLaPbIyb5G7S1N7K3Z_HxjUBdKiRZAgC6Kb1_x2NMaskNpnNzFinYz-ZZqKiTzSqvpQ0fZwcz2JIfW0H9SWE-2JUX1dDCRWhrzz2IN1roYkwILNYAtZCMcsN8e44NDm25SeOjVsFXg21ZC7RsZb_muBFsk24pcdZXHODx5jLy1zNmkDza4Cb8J9f4qJybSzHbOdQhu5FV1ht3Q71ChBUOu97DnglnDuvGykwiZ4BoFq0csx1GLb5blzrBPD1IFY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/63af64b487.mp4?token=YwRWHs0wlU6MDJvc8UUJAtqY7ifDe1CKCzQR7l_Ib34YVj5mLka2IYGb9xUR_h_RktIys9oPGl_s-sEw1Mj-E7zsJ6VOXgjXd7Lu_Rm05HhWsbs-ntSufLx4OyPlj_QlN6xmHIdUxOSO0rSj3_EiaO2rXHHfsr9Dq_YB3S_6UmwBPYz8YnDUHML8gfu_h9_K5IJqXnmcVPogC8Bjqecno2o6CajOxugKurkJ9ySQYMeLlZmPWSWY8WCPP2X1w3acb6f2auVGHyJg6XkJfD3u51RrItbrnsKm3_3m1gXBSofXRyK3TqeTC_AT6XqShrrkoCCPzCf0x4b0JKwINtzPTyfju36WQQwvdOZw23A_D0d4p1IXYDTngca1Hkj2nfiMPAypsjQ_VPIMHbtL_hqhpdHDtV5sNBp2M0q8Bf-mTypmsLaPbIyb5G7S1N7K3Z_HxjUBdKiRZAgC6Kb1_x2NMaskNpnNzFinYz-ZZqKiTzSqvpQ0fZwcz2JIfW0H9SWE-2JUX1dDCRWhrzz2IN1roYkwILNYAtZCMcsN8e44NDm25SeOjVsFXg21ZC7RsZb_muBFsk24pcdZXHODx5jLy1zNmkDza4Cb8J9f4qJybSzHbOdQhu5FV1ht3Q71ChBUOu97DnglnDuvGykwiZ4BoFq0csx1GLb5blzrBPD1IFY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویر ماهواره‌ای نشان می‌دهند که در پی حملات موشکی اخیر ایران، به یک سیستم نظارتی ضد پهپاد و یک انبار هلیکوپتر در پایگاه هوایی شاهزاده حسن در اردن، خسارت وارد شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134425" target="_blank">📅 16:56 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134424">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">🔴
فوری / زمین‌لرزه‌ به بزرگی ۳.۲ ریشتر خرمشهر رو لرزوند
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134424" target="_blank">📅 16:52 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134423">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CZ44KHzCT1ez5VIHhvZKZa6DqLdHGfNkJPQZW39P1oM2LEMCVKP0BEo3GXjcauND0Ri42jW-dmY4J_tegvJ9RfReqmysSKcfNuu2Q7Oca-4eNKM-quLs0lZ1PdZBnf0Dpyxgn6iCu-8P991PxDVLKV2i1N0ZVVMw7lqO4Krtp5H-pJZpfIx10p4_oHworwLWKazHqIgOy1Wy3OTxuTcPcYXl_tqBZSVIGXP_C4_Ufo_u52qCZXjVXSumE6r5LwpnWVNFkDVcEKFxZYAC72A0h_Lo5qOKmzIcYANY2Zs-kzONPdgHI24Zlv68iRDUx86d_fvrjFCoLkRH-NWu7uX97Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کارزار مردم برای حضور اعضای جبهه‌ پایداری در مناطق جنگی به ویژه جنوب کشور به ۴۵ هزار امضا رسید
✅
@AloNews</div>
<div class="tg-footer">👁️ 69.4K · <a href="https://t.me/alonews/134423" target="_blank">📅 16:50 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134422">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/979e817815.mp4?token=YqBk_iIWfCCL_U6jwniarTwGNmTCRQ6h2NRI_AUE_xf5ypnHlDqPLFif8XxDDXsjlqvaY_cLG_QndPtai7m-omcJP0D7elJCDtmzojKp1fMSrPOKo00iwIcS9C4QHK6mGU99Jb7rfgZmTsATd0iQG5qc---Sa_6CPa7pu3HUayCT2Kh9XA_kR-riNyD7iThU-ghYsGTMqhv20Q8s-gfmw5WxJk3lza1HBXT8PrLS-sAkmpEbH2OiJRJEHmW7JUazNMwToioYivko3nBLGG1d4QSUGQ-6LNPJ_0lYN1_Aedd0OSSwQeHoSTzQGbt3p-eGUhqSPfWAjE5KTKugbnaxqQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/979e817815.mp4?token=YqBk_iIWfCCL_U6jwniarTwGNmTCRQ6h2NRI_AUE_xf5ypnHlDqPLFif8XxDDXsjlqvaY_cLG_QndPtai7m-omcJP0D7elJCDtmzojKp1fMSrPOKo00iwIcS9C4QHK6mGU99Jb7rfgZmTsATd0iQG5qc---Sa_6CPa7pu3HUayCT2Kh9XA_kR-riNyD7iThU-ghYsGTMqhv20Q8s-gfmw5WxJk3lza1HBXT8PrLS-sAkmpEbH2OiJRJEHmW7JUazNMwToioYivko3nBLGG1d4QSUGQ-6LNPJ_0lYN1_Aedd0OSSwQeHoSTzQGbt3p-eGUhqSPfWAjE5KTKugbnaxqQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
عمو پورنگ در مراسم ختم مادرش
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.4K · <a href="https://t.me/alonews/134422" target="_blank">📅 16:43 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134421">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">👈
رسانه‌های عبری: برآوردها حاکی از دیدار نتانیاهو و جوزف عون، رئیس‌جمهور لبنان در سه‌شنبه است!
✅
@AloNews</div>
<div class="tg-footer">👁️ 66.3K · <a href="https://t.me/alonews/134421" target="_blank">📅 16:40 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134420">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
کپلر: بر اساس تازه‌ترین داده‌های ماهواره‌ای، روز گذشته هیچ کشتی از مسیر جنوبی تنگه هرمز (کریدور عمانی) عبور نکرده و شمار حوادث دریای عمان به ۵۶ مورد و جان‌باختگان دریانورد به ۱۷ نفر رسیده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.3K · <a href="https://t.me/alonews/134420" target="_blank">📅 16:39 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134419">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/vMbuK168SQ3GeacvFYVEBobFJ_6gMpqXekC7jXDGoq9s1nRErhokff-aBT5FRmSkozkBNKmLm76NuGnqGL5RS-xDYUNBXW-D_-45F0zNlfWGr0x_BSWOGqF-FpLtH39o5GtgV0k94pCubRyvq6I6nv8H9iLqyADzp6mkAOaTSVC1sQkYpmoattzOfxPvnCF7gc4FdH0g84H9f38dhzcpFJYpglRv_Ll_qRs5ju0GMaGweYQHzBaovC46JdD8VQEcqG0gqXS1HmatDnLkxVI69QA_YjK3IqgOGhtF-D4Z0seN7PyDIw-rFdL5L5pk_zAF-xUW_T_SHdK1R6ukiEPY7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
فوری / وزارت امور خارجه عراق در پی درخواست وزارت خزانه‌داری ایالات متحده، بخشنامه‌ای صادر کرده که حزب‌الله لبنان را در فهرست سازمان‌های تروریستی قرار می‌دهد.
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.5K · <a href="https://t.me/alonews/134419" target="_blank">📅 16:35 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134418">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/R4bPY-3fkHU-HTlZtWMHb-ElvYBsanUmJ5GYgKjPw9ygAiOrTU1BhFfFrt0cvwmhGUa8R8WmA6KQirUUvW7rTjLSzE3Hvud9192xnt5zp1NTpyTeUUUN3ccLMKIdOF1NMZFgzbC-VxuZA4Mx6GSRvDY1LRSwvEobH-BkwdtfyIbg5j6uwBS6_TFqnvAF38nZYu53ElOw-4uT93H_FXdTYEWXV_bzwwwRo3pWcxqLtT9NJxm4etKGYbVkLrnV7_MsNZh5ddOfQajToZZwRNc8s58sFRDSR6GSZD_FxeOnX1vpyTHzoSpv9asBsfThUvFncirTc5Oo3TkeW31d-Jbzpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نیویورک تایمز گزارش داد حملات سایبری ایران از ضعف‌های امنیتی شبکه‌های ارتباطی قدیمی SS7 برای ردیابی موقعیت پرسنل نظامی و پیمانکاران آمریکایی در خاورمیانه در طول جنگ استفاده کرده است.
🔴
در آغاز جنگ با ایران، موجی از درخواست‌های مکانیابی از طریق شبکه‌های تلفن منطقه، از جمله بحرین، مشاهده شد و گمان می‌رود از این روش برای ردیابی دستگاه‌های متصل به شبکه‌های محلی استفاده شده است
✅
@AloNews</div>
<div class="tg-footer">👁️ 67.4K · <a href="https://t.me/alonews/134418" target="_blank">📅 16:34 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134417">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
صداوسیما : تنگه هرمز همچنان بسته است و در ۲۴ ساعت گذشته دستکم ۲ کشتی با شلیک اخطار نیروی دریایی سپاه متوقف شدند
✅
@AloNews</div>
<div class="tg-footer">👁️ 68.4K · <a href="https://t.me/alonews/134417" target="_blank">📅 16:29 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134416">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
فاکس نیوز: ایالات متحده صبح امروز به جزیره تنب بزرگ در خارج از تنگه هرمز حمله کرد
✅
@AloNews</div>
<div class="tg-footer">👁️ 70.4K · <a href="https://t.me/alonews/134416" target="_blank">📅 16:25 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134415">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GATbc6x2BaHUdP25n34OAPKNNbKViFYsU1VyH-eBEMAtbkLm_bCJOevKiyUn2WoGbxcThny9H2OanNGbkM7vt26JNM5HLJoVCpm6AEAzVxArFM9yS1ekS4msinarvhzRA4FdIFwiTdWp8VluhtBWEoBWBLCQh8m0p023_K-nloAZa1GjxbZ4-A_HTcXLmoFAY0taC3E7Cr0M3UDiCz9eCB7YIZSHmPF38Iliv4yxzXNvNgZ2lsYSgGvjgiHpltWj8Bf7C-NVDR3jax9N3x0JRMkk3oYqKHoYjU9XzbXcd-FRT6yR5A7pWAjVFOulQucYaahIauQRKiaJz-woB6tStQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
عباس عراقچی برای ابراز تسلیت به مناسبت درگذشت امیر سابق قطر وارد دوحه شد
‌
✅
@AloNews</div>
<div class="tg-footer">👁️ 72.5K · <a href="https://t.me/alonews/134415" target="_blank">📅 16:21 · 24 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-134414">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">🔴
فوری/رمضان رحیمی عضو کمیسیون آموزش: کنکور سراسری در صورت ادامه‌دار شدن تنش‌ها، به تعویق خواهد افتاد
✅
@AloNews</div>
<div class="tg-footer">👁️ 73.6K · <a href="https://t.me/alonews/134414" target="_blank">📅 16:07 · 24 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
