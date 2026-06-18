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
<img src="https://cdn4.telesco.pe/file/kBp2hlhP7nNusbHDRj09YtrK1v52AwtOaWJ2sh5w6V9w_OTxWRgFE-yI4f_zrqqY43ZoEsnTEoPReXrJhlPPOdZk7VDmflUtzfCsLPrmyNHDqpfPYag2qapdajrZN5lbMnE99lPN5Vw9DcOQEQg0CyGyIHBZ8pK4-heW7qB0u6v6xXB6TynoDnDgODIeMxmAVCX3Prb-vHmAsIjXJyiUi9Y96Qo7i2TJXYcBgGxZN5VXLrDio9m8-sSbC5ADmtR-sDUOpxrAsTBxA6ytXlyKTTg6qQgtFnY4N8o0uGT9UO1dYX8xRFZ8W6LV0T3bgOwA369cFzpESx8KjGpd7lFtVg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 170K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-28 17:57:40</div>
<hr>

<div class="tg-post" id="msg-78205">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromLk</strong></div>
<div class="tg-text">بچه بودم دوست داشتم مثل رونالدو بازی کنم،
الان رونالدو مثل من بازی می‌کنه</div>
<div class="tg-footer">👁️ 2.15K · <a href="https://t.me/funhiphop/78205" target="_blank">📅 17:34 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78204">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sLfAR7p287HmiiGGT_nZ5mMBX3AcEIweRufz8vD7rMOYfajn4NjBXyWq1jIZodcE909PCINcHf_vvXJO0n2-21FKJsncOkGnfOHvaQ6TLbPpxM0z7JMJ3zOBzLgYmuJ1_1CY9qu7bDLkXE5DqmfH21iY-ZdZ6K9LVINbcJ3Q1ZPln9cp2-reZc9kZhzUQl1C9zr0zLU4P07NbIADHemGsRcwxNoyT_F2pYVh6PvS_WZqx-4Wmoo6qlmKBbme6h4FRnrHwJkSGa9uF9rq-axVTU0fqXenaUrBYMVcq0dKUWtPt0cOGBdhZ2jAe0pFW9CQFQMpdJiXYq_S2nN-GGGsrw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیکنای تاپ دنیا توی اولین بازیشون درخشیدن
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/funhiphop/78204" target="_blank">📅 17:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78203">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/funhiphop/78203" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78202">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FUBkEKmuup2RSOaeLyJb0203MmQ_rTB7xbTFNM2orHSfmOc0niOm8dmdTYs9kIGh9x3nA3uHAHyj29C1ID4h1Y4trGdMwKwFmkDRj68mruULvZb3TN_4OZeDMgU7vK01oGF_C1Ngs_FIUf2qsR3CPRUna6nJBQYWzUv-YFB-OBvAsvtZ1ZpVOVTrQ1gImHogP8tSOqr2fTT-bhPGcV_jideR8CXm7YbUnr8Pj7_Gzelpy73jopglXyOumI1yzofNJemPpy8fRtGViH8NpDUkCHkroHMPvU-eerhGhKvQtFRNzyhSNvWb66VtK9Wml0OaZ6D6Q9pqi8X8EVy0wrjrtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g28
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 2.46K · <a href="https://t.me/funhiphop/78202" target="_blank">📅 17:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78201">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">گویا پوری و تیمش این مدت توسط موساد تحت تعقیب بودن
🙏
@Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 2.69K · <a href="https://t.me/funhiphop/78201" target="_blank">📅 17:27 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78200">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WcWHF6U2d33jU7hx6_so7SX0xaOsS_vVe0KNJgrmQdVWf3xV08K8KmSx381ZTmljzQ4CcIh0VAyZ6Gzj93nwg0WoJhRqLE9IqMQObdtXq7hJA6qla5UmaXR32A8nShdcwr2BgharRPIGXnsMeiHQxb0Y3Y290JwAIkzk2DAjQwh6FrG91dsaeo1OJuupwBdMWKnWiXgtTifIHhiddlcqI6iPVG_SlSb7XJ0GDoPE0YnDQ2rH4WKLtWTcShHPjZ6mqy8Cmc4jzI563stsRSTMxLo89K7-BdlwHMH-4dN16UW9EHBImdKBPw_q36WOZs6kU8peCd95AdJeYTAmKsWHVA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم سرپا ریلیز شد   YouTube  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/funhiphop/78200" target="_blank">📅 17:22 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78199">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/q9sP33XgGu-mO2KPuwJT3gu_b0_tGiOzr9EfXS1-8jhtk_2THc8ovhfXTfeezDi8zLUsYPt2fCwXT-hHwgktwWFzouuLDtt9leEg-1pD-d2Ik2hjkx7eUoPxx9upb7B7ssWma6MGNNMyhN22WbkbOD-_XiABM2Z9y5aHf71I1sTimqSaaTLKpeFKM65pEbU76FS-op3-c2BjUeo7eRK8FCOSl7qY3S4R_1FnXNVGSpVu7SZHjeV4Uixb_PqobjlYeAu6fnoh0pPmTJlAIzithSwCJpz6BwCJTwbx8zNT4bq7g7xU2wNguaGJBSRM41X3bNSKXsyDBvdzO1U1iM31wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک جدید پوری به اسم
سرپا
ریلیز شد
YouTube
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/funhiphop/78199" target="_blank">📅 17:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78198">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">وقتی مردم ایران صدای بمب‌ها را نمی‌شنوند، ناراحت می‌شوند؛ آن‌ها می‌خواهند همچنان صدای بمب‌ها را بشنوند. چون آن‌ها می‌خواهند آزاد شوند.</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/funhiphop/78198" target="_blank">📅 17:01 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78197">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">ترامپ: فقط مردمان دیوانه میگویند کشورم را بمباران کنید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.29K · <a href="https://t.me/funhiphop/78197" target="_blank">📅 16:47 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78196">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MkL1vzH7L2uoN3Stf9u4dr8SKvRDJ5ys0jo6SkFhqD2_HXGc41sd7VfPemHYBbSpcji9cnSc3HGf3v9RBT_y1XQiEFJ0I6JyEOn1rPNlCmkitizQtT4H4uKfxXnLLug71B-t3H3AIlbcyW-GdkOpNtcdtit1Xlz6s2eHa9BjLuaEQMqRBqFd40a4rIzvt7LV4TTtn4fnwoFPQkXo127DkIXTSFSSsdA_erCI6tDv5nMZtgvSonTuJvNotIcTsbC5tEFtPw4PcT2IHPhHs1fHTgTKi9U7pQxN73YArv567T0ynP3l-BU3ifuByoUIWW8P_O1HhdGO0lg8w5_wK0gAOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 6.47K · <a href="https://t.me/funhiphop/78196" target="_blank">📅 16:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78195">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BoouhXvwCpLgT_QXJLwXBDEUoZLXwqTtlGAk9RHwW3Q-Z7oJ9S5Rj-Sp1YIAtTwu9nQ3whPgKxzhoeWQ-csK486M8To6FswHjDT6PZV5DsBI_fPBd2CTW1ORpNbNRBTpLkufEwc2Wx9NXK5NT60Y1EgdPXHlYRLniLXKqLbeNiYHWjKbpeT_kjZbBUdZT4kTWLTf0FV9wG_TMe7_lycVtC5fvBgleyQkCxaHgKz7LubogtiPa7WMo-X-L46Z5zfItnrLwyqC5i-bjZt2f7rdsIofW1qxbZdFbOV4LLEbTTgFe6RVdlb8399Wzt1Fg5v0DlQIlENehGevm7jIIreQaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از سنت خجالت بکش کصکش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/78195" target="_blank">📅 16:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78194">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پوری میخوام برم بیرون، سریع تر ترکو ریلیز کن یکم بخندم برم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 7.52K · <a href="https://t.me/funhiphop/78194" target="_blank">📅 15:59 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78193">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromuıǝssoɥ pɐɯɯɐɥoW</strong></div>
<div class="tg-text">مهدی واقعا افغانیه؟ آگه آره که کیرم دهن صاحب کانال که یه سگ افغان و ادمین کرده</div>
<div class="tg-footer">👁️ 8.34K · <a href="https://t.me/funhiphop/78193" target="_blank">📅 15:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78192">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/06ef661660.mp4?token=sZ0c5b9rMuGesKy5p8IxUcl7SKr8NFgfsM11Q3WZMywTVZddsWiBSC4MirNAKueTzbhqW2CbFqJhnUrY-2rfIzEEOyGpt8---o69DisJPPb_gHMssAsynpCa5-jDvPLB0iCrH2xkHjSKV_ZA8RyjuZwuY47hrlFUIHPcKK0ThMgxnRMFYqQZKLn-ppYTbEL1N62vTMtT3HN9OQCVLUI8RnkeeHjMEttQnCI9hxl1u_-5afka2NsmBC8iYrb9ZHzN6SvY0hKLCCgTk-0BC12QBoNROeXXAO3yMAVsFzi906YAvFAd-E2loz6Fhd3dmgmPJqCMuSn5Q5qOn_NfPhWe0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/06ef661660.mp4?token=sZ0c5b9rMuGesKy5p8IxUcl7SKr8NFgfsM11Q3WZMywTVZddsWiBSC4MirNAKueTzbhqW2CbFqJhnUrY-2rfIzEEOyGpt8---o69DisJPPb_gHMssAsynpCa5-jDvPLB0iCrH2xkHjSKV_ZA8RyjuZwuY47hrlFUIHPcKK0ThMgxnRMFYqQZKLn-ppYTbEL1N62vTMtT3HN9OQCVLUI8RnkeeHjMEttQnCI9hxl1u_-5afka2NsmBC8iYrb9ZHzN6SvY0hKLCCgTk-0BC12QBoNROeXXAO3yMAVsFzi906YAvFAd-E2loz6Fhd3dmgmPJqCMuSn5Q5qOn_NfPhWe0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریچ یک کانادا و حومه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/78192" target="_blank">📅 15:25 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78191">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">راستی محرمه، پرچم عوض شد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78191" target="_blank">📅 15:16 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78190">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">انقد همه پرچم گذاشتن جلو اسمشون منم تصمیم گرفتم بزارم
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78190" target="_blank">📅 14:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78189">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fo92tKMpWXV4pcVrW8kYGrVBjsE53jcqfa_cnluVUGrF1VY8Aat-fJg2VmKHGtnHk2lsZY5sq5IpxxLBcX3Fmy2aSMQOCoxpttEztLBKiLuERV1k6LIowdr1KGq3Tm5cURiihrSGauEsnJDZZtqc7ZWWE0XT9YAGL8ivRLh1OCPqL3S23WuzBRcl45HlHSGYMw51A_hms6poPf1KI4nkxkU46L00BrIdmSjrJRMfCSpcYukvGSjToFGlFiM97V8wqzWX54f9gSWyM4iIyho4Qo-nyR8FM5h9SXFs1dDlO5FCg0tcFlSpFzkaowvyb34swFs59wgx9LAT_z5L8ZZyyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرامپت اوردم براتون که توش میتونید خودتونو درحالت امضای توافق با آمریکا قرار بدید
پرامپتش:
A tight close-up mirror selfie, black and white, grainy backstage aesthetic.
Subject 1 (Foreground): A young man with messy, sweaty wavy hair. He is wearing a tight superhero suit with a web texture. His face has realistic battle-damage makeup (cuts, dirt, bruises) and he looks exhausted but calm.
Subject 2 (Right): A girl leaning her chin heavily on the man's shoulder, snuggling in very close. She is holding a small retro silver camera directly to her eye, covering half her face, smiling.
The lighting is harsh and direct (flash photography style), creating strong shadows. The background is cluttered with a hanging white t-shirt and messy towels. High noise, raw, candid snapshot.
‌
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78189" target="_blank">📅 14:06 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78186">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/78186" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78185">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">کصخلا فریب و فرید دو تا انسان متفاوتن
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78185" target="_blank">📅 13:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78184">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BRrrLIu_t9V0ipYxgZWzOgYKqknhNdBrFBDC3cXiprx7L8iVpS8uoXCPHS9IXAEy2_8ZFrqJKmjvWItdcq2NaMEMyDZ9oF0HIBuCZEmFIaxkARx8u4T-r23BmhqT8vH7u8XJ90W0znaKRFljYqi3vSfFslNuy-uaCtpkme_--IhOjubyYPc-Al6L074xVYrtj1hkbQVKMI2WvwNfxhr2ZwjO6e_p4zsHsH7PN7xqoBRx6s83C5n3VIjDtflh5vePvDyfl7edKgfPiILon0iz1dSOlIk6KxjHBNw6YbDlegujJwdxYNMMC5QKjVpJuxcTcM1C7k-DLUztMoNqUKpHQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78184" target="_blank">📅 13:09 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78182">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">خب دیگه توافق هم امضا شد و مانعی برای سخنرانی مقام معظم رهبری در ملا عام وجود ندارد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78182" target="_blank">📅 13:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78181">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترک جدید هودادکا به نام Best In The Game ریلیز شد.
🎵
SoundCloud  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78181" target="_blank">📅 12:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78180">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KTP-r8sCFQOWFLlrvGy987yHhuIO4Yty8gMIlLQJLQ8JLAJl9sZSrIntvH1fSJUm8O4PXjcV2p_u19r9FoQIvscrpTd2MK1nt6orlv9Lm2aCWgOOVOzeXMKik7m5tkquN-mdpM3bPFYQxYSgYgg7OOwmppwYkAdUmIQ_OGLTrrcnQ5uhJ5RDrMSQA-SGt7JLITOKl6zVfFbSnm6n65BvQ8AGmtfMwars_R5FocTL08sjmotWCUUfrG9H-YCTpeM4pfN7wTqKTPY4CoPVo_88yEPyveONIk8-Y1CiVacycvFwjH4Z1zj52Ohvhi3OHTSD0xOd1P8lduDtZzyASoC_bg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78180" target="_blank">📅 12:43 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78179">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">عرفان چطوری میتونی انقد کصشر باشی داداش</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78179" target="_blank">📅 12:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78178">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">آرتا:‌ کصه بشینه نمیره عین جمهوری اسلامی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78178" target="_blank">📅 12:31 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78177">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78177" target="_blank">📅 12:30 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78176">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.  Download Spotify  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78176" target="_blank">📅 12:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78174">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a1Zn4L-ynMzwYeXNF906DNMPNOQCDe3i1n-vIOB0c_KTUQFQ9dnu-og1kA8gIghCenW4TEws9n7pUc1izypt-izxYIl82KhqAxZv0ePqvtao1MlJZ8PnXPgRccNq030D8QsuIPQQ8eBJK9SCtNf5G5e-r0iMVd_IWdy6F-AFEVLpjo7BOQSvGjrremhtqfxpJqX4-8UNude0uRwL5RocedAtjv193MCauP-6SwxApqR8EQWhfzr9gyzCyP289OZ7qMQqZsg8NRjW4_dgGB02gW3kPl00RWZKAVyN48RBLV5z_c6spG6pKq8rENEqcB1Qo5r8DX1-0xGk2FY-Yoxf1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید آرتا، کوروش، ویناک، عرفان و کچی به نام میتونی مگه؟ منتشر شد.
Download
Spotify
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78174" target="_blank">📅 12:24 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78173">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">آرتا، ویناک، عرفان پایدار، کوروش و کچی فیت دادن</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/funhiphop/78173" target="_blank">📅 12:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78172">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OgjX8gG6KJSkH5A1Xsb0CAbiH6eqpIRgp2maxUyHKs23u03HB39W32GeCuRpNKGZUtg3vU8oVu2QxpGHsduKwbd_JaCQir7wVRfJ3b-S1OK-c55B4nW8_-LrK56WVCWzqSLhcVUvSYm99yo3Pon93ImWMGAX3MNfLEms74e3h24L3slGmom7ywpA72lxdPvLnayzlWxRRfG5mvIcCT_hILuB-YcDQq0uKZmiMji299Spopbl8Aj13FMSaYaNfdlFGTmtlBerNmWcfIYPGG8I0o5B-ua_ld9Ikd539yOEg8GiMY9AK10Z9RX4UayYgW2uDclDP9l24AD8_spOYHPl5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایرانی بدون خایه نمیمونه، بالاخره یه جفت خایه پیدا میکنه برا مالیدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78172" target="_blank">📅 12:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78171">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">آیت الله سید دونالد الدین ترامپ(دالگخیز): عادلانه نیست تمام کشورها موشک داشته باشند اما ایران نداشته باشد
آنها باید بتوانند دفاع کنند
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/78171" target="_blank">📅 12:05 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78170">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78170" target="_blank">📅 11:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78169">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">رائفی پور: اگر میخواستین توافق کنید قبل از ۹ اسفند میکردین حداقل رهبرمون زنده بمونه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78169" target="_blank">📅 11:54 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78168">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">شاهین نجفی نوستراداموس   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78168" target="_blank">📅 11:45 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78167">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=J3Ok-aQjFhZskhZVOu2YPG_mWz_VZDJC-dmwttczp6PusVurUCXO52WFZgqRUrlAm_C47j2FXu-40m9jVHOGO-rgRvv-wFtqfvYnDq22j1kpyqk1BMArOtaLuXp9fcB_4Z-xbJCT2j6-DUVDBCjPJqDkpuDFEEJbp1KMA8sDn9pCDzm_6DaWh9-478xVqZKk_d4kBLBb8S-d5R_WmrmoRuGqgan9i3GZ9hkF1MaQMp00nRNuasVkSOTGux48VA3iP5xWkyUvsKzFiBKOuru5pQAe6DSK45y6qnNY9o1Gp8OjKZ6F5I328km62Z9guqfAOYqpaD2cxK2P3KdgpSY1Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c40ff98049.mp4?token=J3Ok-aQjFhZskhZVOu2YPG_mWz_VZDJC-dmwttczp6PusVurUCXO52WFZgqRUrlAm_C47j2FXu-40m9jVHOGO-rgRvv-wFtqfvYnDq22j1kpyqk1BMArOtaLuXp9fcB_4Z-xbJCT2j6-DUVDBCjPJqDkpuDFEEJbp1KMA8sDn9pCDzm_6DaWh9-478xVqZKk_d4kBLBb8S-d5R_WmrmoRuGqgan9i3GZ9hkF1MaQMp00nRNuasVkSOTGux48VA3iP5xWkyUvsKzFiBKOuru5pQAe6DSK45y6qnNY9o1Gp8OjKZ6F5I328km62Z9guqfAOYqpaD2cxK2P3KdgpSY1Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شاهین نجفی نوستراداموس
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78167" target="_blank">📅 11:37 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78166">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/knYwzQ1AtPW4XJCmpnpO_t95kk-LTiywzum1fj4GWEvx3OqFSjXiXusJpUusQ7Kblnw1wAFXUMnUstwfGlQz0M5LU-yJFgXkIJ1iaB_GWRV_InEQQpff5L86mlMLGyjMYkesGOreyJqYiNS0PHT3io7DbKWqdqLq2y1wLu38OdYNWKe_71rO-n_1kGuPEPAKI1ibvN24j9mY_SeUpugqCvM0xAVHesws6-8Jq5JkKOPLSrwc9VVjD3LSQjh-mZyHctref4I2vrrUKdoEQkcOIckvkuIbJi8BdpOhu9JnsLJNz6iVRR4gNuf8abyCifbTKrPDrC2x33tXmrV8sJg_ZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بهترین ها درحال درخشیدن....
@FuunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78166" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78165">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78165" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/78165" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78164">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VEMAmK8Z6d4UgMRBY9VhNMLyRQAgPsJhEe225jW2hVBBAIgU2Uqh7H9Fkxo4G-YQ71XNkdOpTjmtOIxIBxtScmzv6lwyVUDR0nx8MNI5TGUigFKi-BNWlDTfyQI6Q4noNNpKGdoepQ1N5iQFGzBmzBlBLGNx26QxcYbyzLsGyTooIogtj6uFJgi6TXVAnoTMX2IY8mVW48Hqg6BDq86lY-jWcFqTRMJoDEiO3T2nCb7Pp7Wanda5-u9wo4lVgDfPmU8eJKMbvEKFfiC4vKiyIR5xtZtTjHRitojdgzdh91AI-TwRncUOnmqujfUI_BjFa9PM9xhunipf-hUAQUhVIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r28
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/78164" target="_blank">📅 11:28 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78163">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=rfA7w77TnUT-yx7B9yd7Z6mpcyjgNCClnJPa1x_Sogju_4NC2C0F-PM8wRkaoRP-WLhpUrX7jlfHvRfKBJBpbedCgLCWaRf0eRgYT3BORRjVbPU0Djnu5ZZOYljM78XnIAmGnfAXqBr8MxNSkPYkOFNBmx8dkiXQ6-wMdPlNfLtrtvdR44y3wSm6RaWyBlFosuTklr7QyQ1N0GGqf4BhQNEy8BM28jolDqia64RwpxOW-sr9Y9QNtq52FvNNwOgSkq0avY08UDifH2rc03kjjlKz6Q3_Ay5X83Ss-tZHoTjU_rRZ8LQd3oHAlGnRNI27cgdVGjDUU850efF0gls1Pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be730c80f1.mp4?token=rfA7w77TnUT-yx7B9yd7Z6mpcyjgNCClnJPa1x_Sogju_4NC2C0F-PM8wRkaoRP-WLhpUrX7jlfHvRfKBJBpbedCgLCWaRf0eRgYT3BORRjVbPU0Djnu5ZZOYljM78XnIAmGnfAXqBr8MxNSkPYkOFNBmx8dkiXQ6-wMdPlNfLtrtvdR44y3wSm6RaWyBlFosuTklr7QyQ1N0GGqf4BhQNEy8BM28jolDqia64RwpxOW-sr9Y9QNtq52FvNNwOgSkq0avY08UDifH2rc03kjjlKz6Q3_Ay5X83Ss-tZHoTjU_rRZ8LQd3oHAlGnRNI27cgdVGjDUU850efF0gls1Pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار:
یک انسان خردمند در ژانویه ۲۰۲۰ گفت: «ایران هرگز در هیچ جنگی پیروز نشده، اما هرگز در هیچ مذاکره‌ای هم شکست نخورده است».
ترامپ:
این را چه کسی گفته است؟
خبرنگار:
دونالد ترامپ
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78163" target="_blank">📅 08:58 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78162">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Jii6vq68au8_WuVX46VygZ0vmfBEmZRpX8sfi0EKDz2U7c60_K2QKbr_mtAHnkFUSN-0zwnGj4fZyeYCKiWcdaEK8G_nABvgD4KPES4Sd86OI8Gh_o6U-ifaID0kaSghxkfFP8D3Os6IqUxgpHGTs71ltnGvHrd7Kc-ldfc4ryGW_wDwbLzZhvukqrkiIxRMMvQK2d4G0acYWaLhiUPBm8PXv9Bx2yYpFLdly9DU6JdGp50faZM7FEu05VENFtc7mw8yRT7mmt578BGHh3Xpif3-O2FLp9FRVZXk_65uyT9KnYlSAMsNdzFYwSnWdEOO0RujfZ-7k659KNC8dCnICA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78162" target="_blank">📅 06:51 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78160">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/pCilUhF3cBtO0ekb8zBulK6g84e4D1s8EOaDOdFUwFY4qsJL-N82-z8PM1TKZb5nVy4BmtyULs0uHll0ohu5VdFzZdsUmx3IjPEQdlgg-o6IEnhNqLQxMjocq_3zhEZCzswXYUZ2D-WX3_2zfrs0mN9tNdYpNPoqOGG1sx6mf2hsVjB45nJ1lJxEuWKbuLmlNfqA_7-E4OuUkmxFhH-FdgDeeVx7amKIqKVkYOVHrRwBG3OCaMu_Ugdx9W2YHrfUIChXhW8h7NORiWohN-D8PCFh9Nn5U1zYo1bsHs7sfgcMMBZ6bGFMtYowZ3usdnv0ZVbo5zPMJ2njhXBNlKNcUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XjNrs_Z3y2FaRAq3waf93dHMzBVFRaZSkW4vuakmSYLh0YxeNxtoOzcD2_rK7s1_aklIWlYXJVIwijcQgzpSC-q_AnXOeo6bRzbxZPJza02AxomUg12Go8H34FiOiIgXWHryBEnoPYQar2F_6Ghnrx_-QIHJCTSPwEXuEtEqPsNy2wU0VTECyLBhTA-2KRS-ctCBCXIg2_63-1fGObPVY9ev_UKXh0JEYqPCypexBtqHmE1xVieLmGD1_YeimX9pxmauBepKfQ8Lhk3eXFFvU91oll-H-2-NkOUhSH2IeKrqOu1pBiDNHTW9-vb5IeDD6oNVsMuDYm2E0MEVAiQ85w.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عزیزان ببخشید من یه لحظه حواسم پرت شد این قسمت از بازی شطرنج مرگ و زندگی رو از دست دادم، لطفاً راهنمایی کنید این چندمین تاس ترامپ می‌شد؟
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78160" target="_blank">📅 06:14 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78159">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">جی‌دی ونس دو سه روز پیش اومد گفت تمام بندهایی که از توافق تو رسانه‌های مختلف پخش میشه پروپاگاندای سپاه پاسدارانه.
امشب خودش از رو تک تک همون بندها خوند و تاییدشون کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78159" target="_blank">📅 02:55 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78158">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">سخنگوی وزارت خارجه:
ایران دو قدرت هسته‌ای را که توسط برخی کشورهای دیگر نیز حمایت می‌شدند را شکست داد.
ما شعار نمی‌دهیم؛ ما واقعاً یک ابرقدرت هستیم.
روند تعلیق تحریم‌های نفتی از امشب آغاز می‌شود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78158" target="_blank">📅 02:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78156">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">کاخ سفید جدی جدی حسینیه شد؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/78156" target="_blank">📅 01:33 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78154">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">رشفورد چهارمی رو زد و تمام
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78154" target="_blank">📅 01:20 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78153">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">خب طبق بررسی های میدانی و حضوری تیم من در ژنو، تفاهم نامه به صورت دیجیتالی توسط پزشکیان و ترامپ امضا شده؛ ارزش قرارداد سیصد میلیارد دلار با بند فسخی که بعد شصت روز فعال میشه.
Here We Go.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78153" target="_blank">📅 01:17 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78152">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">میگن که تفاهم نامه رو امضا کردن ولی فعلا بچسبید به بازی انگلیس کرواسی این مهم تره.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78152" target="_blank">📅 01:02 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78150">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">عجب سیو پشم ریزونی کرد گلر کرواسی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78150" target="_blank">📅 00:50 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78149">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">بلینگهام گل سوم رو زد برای انگلیس
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78149" target="_blank">📅 00:42 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78148">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc2oQDv6Hmhc05dC0W1DgUYFIYqaSD6umYcY5V9ivGDJoVeDtizXmrNIqURyDBKVPYgsIpKqQ1UXcDkQ3v4gCCTTl2vdujOYq0j8gSwMH7rAZqZbeJnRoRs0wRE4spZGjsPeCVVwmj5vmlPpNPoC4_fSCwE-j_gYx6rjNI5KAIABLFLNSSCrTwSLzrvNy8GBw6BiJ0gFfb6xtn7uLJCUCzQM8eT41BGIeKSdzUxOwWKTKk5KwGxbu0XYUSuAUIwUeL_1CdylSYH-w_j-Eo9tDPf68JcURtYPYCPYhxAa0hOrxRvadIhQOoqB_w15mGe3yQ4Y5h4s7ULLPKR9OMdgcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمتر از یک هفته تا منتشر شدن فصل سوم سریال خاندان اژدها مونده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/78148" target="_blank">📅 00:39 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78146">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a8FfPO44DgJ6cmI3hnalxU6qhLGDY7MLnJq3q3DEGhphqXNdGyCeeTZS8IWuwKytnX7hPfg7MUuwUXFSitXl_O1dAyOSh5hhlJMuHvBAOLDwYUdk_xdW4Tox133A-rVTcygPgoXzW7yaGlCzZSxjzWkz6zlrSaW4DkJpZkPxm3t731PYHvm4Q5qYsn-hxymH9ZktBotT8V3BZQAtSzivSK90zNtuLGV3s_-906JP9BKl_O3hXIrBLJKkjtg_RQ9G2JtCZpzBN5_AQg8A1HVNE1TlahCDGZPRYD3oGPLDUR1jyD-cpbaI80ZPxYSAtIA8jMU-n1owO-9uW21CAUcIug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری مامان پوری از مهدی طارمی.
@FunHipHop
| Sogand</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78146" target="_blank">📅 00:26 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78145">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کرواسی زد
۲ ۲ شد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78145" target="_blank">📅 00:21 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78144">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">مثکه متن تفاهم نامه منتشر شده ترامپ قمبل سیاسی کرده برا جمهوری اسلامی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78144" target="_blank">📅 00:18 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78142">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">این بازی داره قشنگ افتضاح بازی قبل رو میشوره میبره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78142" target="_blank">📅 00:15 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78141">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=vMH_-WvM6wiyA6vlp9YmoVUKvagbT9m37PYRJ4_RVbhKHqrzLJA58e7bqB1JsJVkALY7By7Ky1G0BG8Ir8EBhwRzHJXEkdpR49W_jMm8issU_1xNT3B693epnXdV-eiQt5Tz3Rw-LQydDykVxxFSdx-IZlOycqPncJBL4pFmafuqEcevtGS5maQhAeAUEkb7kPqP2C0GmhMlyw6L_qP_eXC9LCVVT1Y5v3tqQeBoh2PP8umfxoIzRbXiXa3BN8wgLpY7s2YHSs8lmqOX2y1Ib8_dbMn6GyYGHi96s8nwVcGZcPhYy0X7kvdPfjeRS7_KTdt0s13CMbCDy3a35L2gUg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/7dd58a539d.mp4?token=vMH_-WvM6wiyA6vlp9YmoVUKvagbT9m37PYRJ4_RVbhKHqrzLJA58e7bqB1JsJVkALY7By7Ky1G0BG8Ir8EBhwRzHJXEkdpR49W_jMm8issU_1xNT3B693epnXdV-eiQt5Tz3Rw-LQydDykVxxFSdx-IZlOycqPncJBL4pFmafuqEcevtGS5maQhAeAUEkb7kPqP2C0GmhMlyw6L_qP_eXC9LCVVT1Y5v3tqQeBoh2PP8umfxoIzRbXiXa3BN8wgLpY7s2YHSs8lmqOX2y1Ib8_dbMn6GyYGHi96s8nwVcGZcPhYy0X7kvdPfjeRS7_KTdt0s13CMbCDy3a35L2gUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خخخ:
وقتی همه‌ی کشورهای همسایه ایران غنی‌سازی دارند، منطقی نیست که به ایران بگوییم به طور کامل غنی‌سازی خود را برچیند به گونه‌ای که برای تولید برق اتمی هم غنی سازی نداشته باشد؛
درمورد موشک‌ها هم همین است، وقتی همه‌ی کشورهای خاورمیانه موشک دارند، خب عقلانی نیست فقط به سپاه پاسداران بگوییم موشک نداشته باشد.
بیایید کمی عاقلانه‌تر با آتها مذاکره کنیم.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78141" target="_blank">📅 00:11 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78140">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">شما یادتون نیست ولی دالیچ یزمان کنار شفر گزینه سرمربی استقلال بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78140" target="_blank">📅 00:08 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78139">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کرواسی لاشی همیشه جام جهانی غول میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78139" target="_blank">📅 00:07 · 28 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78137">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انگلیس چه خوشگل بازی میکنه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78137" target="_blank">📅 23:53 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78135">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ترامپ: ما حتی ۱۰ سنت هم در ایران سرمایه‌گذاری نمی‌کنیم /از یادداشت تفاهم، بد برداشت شده است
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78135" target="_blank">📅 23:32 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78134">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qGzghM8x37d4bCAxOSwMeECpitmFiKolavcy6ftjXmpd0p1NlIcx-Ko9YN0xSqef9D77gYCMh-uV-NwIXptMfewhQ8OHVXKjAceSOsq0FSmLZkREBg4rPXdhDZYw8_RvNYPLuELkr4D9Ci8Wb9FPLXKS-ryOftkA7z0yr6HnEZX2AbXGum6l-TrCdRdc0kdHy5C3SUsZZnLVm9aw1CcngSviNJ0ZRHvrewWoJCVY75YxgUKvtbmo6NUtB-L33TQF2ghkGD7hNl1qoPbneBEdYGHZ-r_Lf5IQ2ZV6xIT3hH1zI37wQe0N9rHRfsmo2IaPLGuH94TiQb9guTaQihXMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکوادو
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78134" target="_blank">📅 22:47 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78133">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار  +
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا  +
🛜
تمامی سرویس‌ها آیپی ثابت هستند.  +
🎛️
پنل کاربری اختصاصی و حرفه‌ای…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/78133" target="_blank">📅 22:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78132">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">☁️
✨
HappyCloud
✨
☁️
🔥
تخفیف‌های فوق خفن
🔥
⚠️
فقط برای مدت محدود
⚠️
+
⚡
قوی • سریع • پایدار
+
🌍
مولتی لوکیشن واقعی در ۶ کشور:
🇩🇪
آلمان
🇳🇱
هلند
🇦🇹
اتریش
🇫🇷
فرانسه
🇫🇮
فنلاند
🇺🇸
آمریکا
+
🛜
تمامی سرویس‌ها آیپی ثابت هستند.
+
🎛️
پنل کاربری اختصاصی و حرفه‌ای
📦
20 گیگ --->
❗
فقط ۴۹ تومن
📦
30 گیگ --->
❗
فقط ۷۲ تومن
📦
50 گیگ --->
❗
فقط ۹۹ تومن
💎
100 گیگ --->
❗
فقط ۱۶۹ تومن
💎
150 گیگ --->
❗
فقط ۲۳۹ تومن
💎
200 گیگ  --->
❗
فقط ۲۹۹ تومن
💢
تمامی سرویس ها
۳۰ روزه
و
بدون محدودیت کاربر
هستند.
✅
خرید فوری از طریق بات
👇🏻
🤖
@HappySmileVPNBot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78132" target="_blank">📅 22:35 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78131">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">یه صحنه گلر پرتغال هم اومد پاس به عقب بده به خودش اومد دید خودش آخرین نفره
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78131" target="_blank">📅 22:31 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78130">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">تخمی ترین بازی جام با اختلاف
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/78130" target="_blank">📅 22:28 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78129">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">همون بهتر ک توپ نرسه به رونالدو
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78129" target="_blank">📅 22:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78128">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">فقط یه رونالدو فن میتونه بگه ترکیب منتخب بهترین هافبکای جهان نمیتونن تغذیه اش کنن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78128" target="_blank">📅 22:02 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78124">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">بعد دیشب گفتم شانس ایتالیا از پرتغال بیشتره یسریا به کونشون برخورده بود
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78124" target="_blank">📅 21:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78123">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">تقصیر رونالدو نیست
گذاشتنش نوک بعد یه پاس نمیتونن بهش بدن</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78123" target="_blank">📅 21:25 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78122">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">رونالدو مادرتو گاییدم پول منو کی میده</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78122" target="_blank">📅 21:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78118">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">نوس با قد اندازه کاگان چطوری با سر گل میزنه هی
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78118" target="_blank">📅 20:39 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78117">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryjh2uiQcIBzdqyp_7DxXEcquPdro95xHhRDEId5xEsCz00Hf4FBm3TsAWw2aLGOV4Yu_tKXK6tbo65LF85qPIdPOnpC5qwTRUUQQHDdh0Ye3dVT01tMbJdO8sbX37MQRf-c5wGCx-61gGp0VN0-GSw1FSaUuHml2nIkXego46-JRLkm-mfcp3WjcwckfVUBGI1bO0J-kL6qfbE5K5OnKMwNAZgQwCVLxuEMYrzYhKkxtNpalbECmqwYDO2TAYQzjmjpFxq3zqEhAaLjYz7w8Pq0If8qm70tbMLYqTIGekzjUG2LT7o-Wc9SqC0zNSEk6IM21uuk_z-SKbSShYlajA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آقا عارف
تولدت مبارک مرد بزرگ
❤️
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78117" target="_blank">📅 20:03 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78116">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">ایت الله جی دی ونس میگه چهارشنبه متن تفاهم نامه منتشر میشه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78116" target="_blank">📅 19:42 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78115">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">نه داداش پوری خایمال نیست اینطوری میکنه فدایی باهاش بیف کنه و کیرخر
@FunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78115" target="_blank">📅 19:11 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78114">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">مسئولین جمهوری اسلامی حاضرن هر کاری بکنن ولی نرن حضوری قرارداد رو امضا کنن چون اینطوری مجبور میشن با قاتلین آقاشون دست بدن و روبوسی کنن
فک کنید همچین عکسی پخش شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78114" target="_blank">📅 19:07 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78113">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=IlSDIgrqF_niLzAsAUtCJMIoOaN0mBcejvm6z2ksvOVVNKWPhwGRknMIR5Jxck28QppG9RwIPIffDaaV_ncz19pLfY_wlPu9E6rMgPief7QvyIH9PAzLndYx6ejXlW5sjO709OvTQv4YQ13rpc6OtrUjHuGT-8p8gNAr5vtJPoMw270afwKlnuGBqvtxrlJuEDARMI6oTYNmX3c6wQ1pxMk9U3yD_kXk8L7PbJ88dqqDplthzHoO3ddXaBDmYTieMYsCVjV6UJeXZV6mp3yylBzw25zVcwPOIZkbZRE_FDCGgMRyeXGhKP_VZpJXD3Hyw0YDaP6baFcCD8C8UtSFPQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63df8bb0.mp4?token=IlSDIgrqF_niLzAsAUtCJMIoOaN0mBcejvm6z2ksvOVVNKWPhwGRknMIR5Jxck28QppG9RwIPIffDaaV_ncz19pLfY_wlPu9E6rMgPief7QvyIH9PAzLndYx6ejXlW5sjO709OvTQv4YQ13rpc6OtrUjHuGT-8p8gNAr5vtJPoMw270afwKlnuGBqvtxrlJuEDARMI6oTYNmX3c6wQ1pxMk9U3yD_kXk8L7PbJ88dqqDplthzHoO3ddXaBDmYTieMYsCVjV6UJeXZV6mp3yylBzw25zVcwPOIZkbZRE_FDCGgMRyeXGhKP_VZpJXD3Hyw0YDaP6baFcCD8C8UtSFPQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/78113" target="_blank">📅 18:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78112">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد  @Funhiphop | Jenayi</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78112" target="_blank">📅 18:30 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78110">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Zo3D0-cUHTusrNffoA7TVnDBgyMGYUV3nho9vKy9o5yOusiY1tcYh8pa9ZSPrR8n8O6upttzPCcK5eK4d_GGpnDFjTl5-MIX6BxLUBSqC60FJhDjvhxNaen5NTE2PcX1cimrg3TdY3_ck4y0J8EaI6Pjq7vDFuOwbwiY1woi1lo8paeLovTCUh_h2QfazgIMdQNkzYuBMxqaiFUckVdQ5Dutm3OAqKh68UiazMJ8UbXz1TTlr--4YOpb1o2H1KyDG3KHnkeAbLrrSzTzrOcidVt7M8b3SWEKZl6pulsxBCHr4-QhBoz0AHBen6w5MEPaX5D_feLfS2cHrNmqnlev3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rvsrWoKSJU7vuSgGbwHImsXkw-UtEJZZFAQCLj1JRPLl9LypHQssrYilRzFcLFH37wrM9kMyqXAUK7VeMAZ8X9669wvmo7x6wvkn_7b5W0uP4reIZB6eTSt07SAa9iiKS8d_1GMY5QX6YjnTaGSWJTmparQS385nq-Peeu4mjaaXPXBGDO6VUPbDiiKHcFZotxzbKi7mj6pSuqnG9KfiOo5RDXMO4MuY4z73_hIuGHX7XeaCkhG4QKjLpHCHmCav3SX0ZHMThybQYBaPAJG66EcRf215uHLfBxf2VFS7y9JcVlgvSjhRsZ9cD7syuMPsWM-w7zvW5oty0k21Z-c73Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">از دیشب هرچی بازیکن و باشگاهه افتادن به مالیدن تخمای مسی بابت هتریکی که کرد
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78110" target="_blank">📅 18:27 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78109">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78109" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78108">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hf2-jfReBhFw8KOYRJ-KCS0_8oRHaN-T7QQx58yodMRBljMj3UvNdZxMFPExeDH-0BKm3FkxU3igJ_kVxoCacBLbYH6vF0vjK0oPnqnpBT2Pv1iPmCR5wzGTnOOcW9hJBw5130-jcKKW538g66k7S6DdxJRNZaW2Mf7MDCZQtPJJOS_SklLAA1Aiwb9nfWg0BLO0xvUYI7aKZUnpmpnbfuOC0a51PijgVlOiGuENIo8cmTrdq8h-mBJp7pqTLV4DqqlTrjErkbBIQ7HLgJhgWEfwHHn_V1V72BEXypQMiaF_iC0-lVhsF1T29_12Ep0ZMjzHVzdsQcHWBMO4w-0mkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
چرا سایت بین المللی ماف بت بهترین انتخاب برای پیش بینی جام جهانی
❓
1️⃣
شارژ و برداشت اسان و سریع
2️⃣
پر اپشن ترین سایت فعال در ایران
3️⃣
دارای مجوز رسمی curacao
4️⃣
کارت به کارت همیشه فعال
➖
هدایا بی نظیر ماف بت:
👇
🎁
100% بونوس خوشامدگویی
🎁
برگشت باخت هفتگی
🎁
هر روز 100% فری بت هدیه
🎁
هر روز 20% شارژ اضافی
🎁
گردونه شانس با جوایز بی نظیر
👍
با فعالیت در ماف بت طعم واقعی امکانات در سایت جهانی حس میکنید
👍
🎯
ادرس بدون فیلتر سایت:
✅
https://mafclub.online/fa/?btag=260368
✔️
کانال تلگرام سایت: g27
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78108" target="_blank">📅 18:26 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78105">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78105" target="_blank">📅 18:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78104">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ai8xAz0toPsoXLXtKyw9dlR1PXbbgSoO1ucD0zQa6iZvFQahXKxfafzyM88wqRQ4HFXy_gap20f9S509IMOGZ3RIrNZF64NQ_qal-cdA5kdSPFHrw05bjGxonrEi5SPt4KHeCPkQoJRk8Zdw04vjo1K3PX3de3naPrDCR2sA10L4SyALVdLYOcLopBgNKvhoRXOK1mtO_7Lra_hOWcXInnW7wCyDZHy-mGrMNnTfRfLErNbW9aHro2CKrcR9zdkL7NcY442HXKNUb860VQpafM8PM4H2eOFCUI4PdpxVsTKeHpA8K3mgvvpvL_4tGoC7B1LwUoGMxr5ltYMeVPKMQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جدی برا این لگن هایی که تولید میکنید خجالت نمیکشید بالای ۱.۵ میلیارد پول میگیرید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78104" target="_blank">📅 18:08 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78103">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=XQBWFdJMstcGPsNhOJxqRve5WBc-cTlhaSVEbUN-blS7QgrxCzyZYPgix1mOIAgTd9jrdS_x7tJhXmvyzF0SbDoSZ7w6-2IeOgvpSCGgvzNrzWLUWeSRxzCzntjmlvrzArGI5dm4olkc5DohYOE9URFRH-CBItNRXaItG5JODwySXLyC-20pIz-BBES40dVrRB8HQDyWKK3J6kPsLEU-OhR4lWv5TNcD136Nh-i2dUXLRCV_5GppQviyM-b96aIcgEMq1A9LiVwsZLr2Yed_rmEy3orb-jf04zexOvdpXZbaHlpOaEfKURB6u7xQnNuvejlIle0_QtAxcJWuANZcRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/912473cfa2.mp4?token=XQBWFdJMstcGPsNhOJxqRve5WBc-cTlhaSVEbUN-blS7QgrxCzyZYPgix1mOIAgTd9jrdS_x7tJhXmvyzF0SbDoSZ7w6-2IeOgvpSCGgvzNrzWLUWeSRxzCzntjmlvrzArGI5dm4olkc5DohYOE9URFRH-CBItNRXaItG5JODwySXLyC-20pIz-BBES40dVrRB8HQDyWKK3J6kPsLEU-OhR4lWv5TNcD136Nh-i2dUXLRCV_5GppQviyM-b96aIcgEMq1A9LiVwsZLr2Yed_rmEy3orb-jf04zexOvdpXZbaHlpOaEfKURB6u7xQnNuvejlIle0_QtAxcJWuANZcRjzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دسخوش
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78103" target="_blank">📅 16:59 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78102">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">مثل برج میلاد بعد ترور سران نظام هنوز سرپام
😂</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78102" target="_blank">📅 16:58 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78101">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">ابوطالبو بخاطر این که گفته بود تیم ملیو دوس نداره چوب تو آستینش کردن و مجبور شد بیاد معذرت خواهی بکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78101" target="_blank">📅 15:05 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78100">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">ترام: توافق قطعی نشده اگه هم قطعی نشه دوباره بمباران میکنیم ایرانو
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78100" target="_blank">📅 14:37 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78099">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ترامپ: بخشی از تنگه هرمز باز شده.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78099" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78098">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">ترامپ: گزارش صندوق سیصد میلیارد دلاری کذبه و آمریکا چنین کاری نمیکنه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78098" target="_blank">📅 14:33 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78097">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ: ایرانی ها به ریش اوباما خندیدن گفتن اون یه حرومزاده احمقه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78097" target="_blank">📅 14:29 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78096">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اندروتیت ۱۰۷ بار تو یه صرافی لیکویید شده.
الان دوباره رفته صرافی و شارژ کرده رو بیتکوین لانگ گرفته.
اگه لیکویید بشه و پول از دست بده، میشه ۱۰۸ امین باری که اثبات میکنه تریدر خوبیه.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/78096" target="_blank">📅 14:23 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78095">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/827713cec2.mp4?token=ENd5Sp4TdlrH3AqM1vM1oqT8byC-BJrhECcBr_QVShRDLj8bxAbGYx9ZDrF4tpQBWEe628qljRVuqMwVFZv-Ur9RCXK1crkLmEUO5YzpXlA1N66BPaiWx95Y0ceSDmgRlmhaXOVmom8bbO8Kz8NszhVSwfcGk6nfFyKB8mvTwdvfOQKV4VusOYsr33vYgvcU7psfvG7yNID3l8k-Su204La0gsHLGrxuyZuTHUlc2aUJCGgJau15FzeYiK_J5GxN2sG_cy2wW59LQmcm3vq-OBo_K2uGSpRM0SwhSZnuKB1yc3dgriUDyeXPGjgSZsX6LccgjAo3kbZQx_OoW2telw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/827713cec2.mp4?token=ENd5Sp4TdlrH3AqM1vM1oqT8byC-BJrhECcBr_QVShRDLj8bxAbGYx9ZDrF4tpQBWEe628qljRVuqMwVFZv-Ur9RCXK1crkLmEUO5YzpXlA1N66BPaiWx95Y0ceSDmgRlmhaXOVmom8bbO8Kz8NszhVSwfcGk6nfFyKB8mvTwdvfOQKV4VusOYsr33vYgvcU7psfvG7yNID3l8k-Su204La0gsHLGrxuyZuTHUlc2aUJCGgJau15FzeYiK_J5GxN2sG_cy2wW59LQmcm3vq-OBo_K2uGSpRM0SwhSZnuKB1yc3dgriUDyeXPGjgSZsX6LccgjAo3kbZQx_OoW2telw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عاااارهههه تو موهات بلنده زیباس
کلی شیک و پیرییییی تو شب کلنگی نیم‌ساز
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78095" target="_blank">📅 12:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78093">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/sCAd-bIquz0AOJmmvuF4UZ_gBBXlGnvtztn5jNXreLo4sO7BRojF6FdCh1WkpMK57ZF20yjzg2aOsMhRa1cp2Een4ZiUDy8bY4eKIq9jfMWqDcs5YW7xe2H_yxwyWekzu2F8abXkzcflmhsBtRgxI1QCbXfk8nVFcSypspRHpVdnm6fdWmok5a8B5J_DCNgy7q4jS96SK-c4hYUmx14LW9my8vWRU76s4L5oiWRSg5uHAnSDBrzIJa27YoWY3_9odTAHQSRBwfc3FwernEGT2oOryGpfE2Lxotxe0rDMWIP8z8V4o1Bm8pXqHmz0WW5294sqzHuKjQhPKA-O3Ivj4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/OenOxgWR0NYUjkActXZVqKTpc-UlNHAcHIvko0XZCPeYTZV9xfVuR5gpIDBwuB2kUawS5fZwPNrN_JpCn6x-QMQhr0cazZM6eEQnv4ViniDag4hdb-BYgoG78Ew9F_AERsBqzxQGiVK13DqF29QTLJDOS0KdgSKwZDupf9AH6Vs9bsMu7rBoR1WQdy91gc1oSyqLhml_Opfca0ssIpsGUn4BzAnV7SaeGaqUdu0cmlmaYXfbms4glH2LyZUSLWk9GwsWJeu9ED-M70ACHC1RA7y5WQfM6oFHoRgm9hQxzpBPjxiSddBk1-rqP6izxpc_hG52jK9vkNDypx6FOklJvg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این داداشمون هم به دخترایی که فالوش میکنن بک میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78093" target="_blank">📅 12:01 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78092">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e5GwM4uoq3DXahCnXRy1pD3BQuks22EFYYSmVcs55tmkC3djRjC1emXppzSp4FTTvEfipdislP4mpkHy7u0SvFVdYTZWzZ4_8AkUAjrxTJzlyzeEEkhJ7dxQcPD40p7sdplpKbIdAW6aPxMukvpXCj9BXayAFIJYpAWRj0HWFpqBz7EzLdQTBExJIFY2ibwyvlB0hInSphiuwcfRGnjdy1M3vUGTig8YXoDW32_JOCqWQkf-FXSHmqoHKMLdH7j8urv7MhuF4Z37YpJBIRqozTyycpryH7BbbbBO8dksFcLF6nsasOiPHYx9jaLwOUjQQBVQMXSK3U8Wgkze0HtGXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مسی چند روزه زنشو نکرده اعصابش تخمیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78092" target="_blank">📅 11:48 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78091">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oLQQYCspFiLCOSUFfDT_HTeDXM3q_S0ZaYXiS-zu2KHlZsBJ-OG7znZKDqwsIfgyWERd6m6oxeqqIit7-U18KWNNA8phXKJQC5kU3W5ikDnlSMZbdn6s3FPze4VMsgn56m8Q5dwgYS_waloC2dCpgnw2ZyljkcKuclI7zaCSf6o1PxnQs8xXN1CnmUdyotewvOb1ISc21ChPyyFx6uV6VKo1xTqlF8j0AsQik6ZDcJR_lwWcIHP_-tyDlnSmlpN3uDlk1LvtQvbVR5XRDFqTBe6x031Cls2zoxgMJEIHkjQnHkbntyagu0vTNiKcawV0hdrUStReu9VTCc1LYmwPRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ملت نگران مصدومیت نیمارن
واکنش خود نیمار:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/78091" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78090">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">derbybet.apk</div>
  <div class="tg-doc-extra">52 MB</div>
</div>
<a href="https://t.me/funhiphop/78090" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکشن رسمی سایت دربی بت
🌐
DerbyBet.com
💰
امکان شارژ ریالی ، ووچر ، کریپتو در کمترین زمان ممکن
🔥
🆔
@DerbyBet</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78090" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78089">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zfg7vfqqbmxghEDLVOx38kZepWFIXaYQC5fjQndfalIH0gCn-sUQYY1dC6Y-jspXOR4yspM8GfXwfgU3VFJr6ZH-vasetuQxMxW8pLAIvTVuefJowt9BotRc_RsD-FtB7a9Ozrl5qQfeahx8Tmsh6rrOZkBLS-jQcFBfeQNIshssc2vdGKoCAkf3juEhmnLSM1Rxi6Dqwuqyuce9C4u8R2NXOosvpJlrJ23qMBtrq69KGd6yQ08YnxznUNCoA6lIXgsVut0Nb3OIWfXfLrwqlGp6cndafQUq88UkfEvdGcAET9wV_iPK5A_mWQabMI9yk46mP_fvwSrylcwwax1JaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
دربی‌بت؛ جایی که پیش‌بینی فقط حدس نیست، شروعِ بردهای واقعیه!
✅
با لایسنس بین‌المللی معتبر، وارد زمینی شو که حرفه‌ای‌ها بازی می‌کنن!
✅
آفرهای خفن ثبت‌نام در دربی‌بت؛ فرصت‌هایی که تکرار نمی‌شن:
⬅️
۱۰۰٪ بونوس اولین واریز؛ شروع انفجاری
⬅️
پشتیبانی کامل از همه ارزهای دیجیتال
⬅️
درگاه ریالی و تومنی امن، سریع
⬅️
برداشت‌های آنی و بدون معطلی
⬅️
پشتیبانی حرفه‌ای ۲۴ ساعته
_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _
✅
دربی‌بت؛ بازی کن، ببر، لذت ببر!r27
🅰
✅
https://DerbyBet.com
📩
@Derbybet</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78089" target="_blank">📅 11:40 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78088">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aVDKnINLtvMf9jxQbDq_aCor--MymU7NRUT4ut7E9HM7MygqPxXmeqeETjd65TdqDMEjUKyukKnBsNGfNX2gW_WN1KseNRs0H8DWcoT-RB0sw1w4UuqFWlWeIxyAT8Xwu1Jo-0isU75eWPIlucAcQfPMvjq0u3Ujh_SzC-7ntMqHkdltSM6DVWvUXpeA4jnUqSbdMeSSyj362As_FthxTkWbXphUAU2QAoZ6um9YJKEsG5C3b2ZCj-Gj9gftyElvhXjFMRHHKAdYKmci-e8A5V2PG2M0U5jUoLsinau4e7ZEEaGgbN3vNGtlWf2adfap9iQHkf0a7lvldP7Ix3mT7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حمایت پدر از پسر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78088" target="_blank">📅 10:14 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78087">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oS7UWbIgQ2MDId9r9m4kmRjTHnZIcPPhGUdXG_ZOqpk6Mb4d9fqSeO74Lo1D6R50nGb2G9Afmp7GsS4cw5JbXO44BtTu5vNafBu0q2vfuegxusMmwwY69o4HAZQn6pdVO4OGxeyYkDp1-m6UKhRI73WitM1XxrlBP0LNloI__MuqtEaqX5oYQgZpccAbX-4Yy2HDQKMINVG3xg_kQIcs0MzDWPU4gTd5aW0QwZHRYOUfLvIzz9TkoCCxd20rb1AJR5LX_tEVaGxUv7KZT8Gbe0JDJ1HarWEWnwix3b5zP9fgVI2ifo6IL_QTQdig5CFy9gj224p1TukY1LHFeEnVnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو دریاب پسر، یاخدا</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78087" target="_blank">📅 06:24 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78086">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حالا رونالدو مصاحبه میکنه میگه نه ببین گروه ما از آرژانتین سخت تره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78086" target="_blank">📅 06:16 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78085">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">پادشاه فوتبال تعویض شد تا استراحت کنه و برای گاییدن بقیه تیم ها آماده شه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78085" target="_blank">📅 06:13 · 27 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-78084">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">نویسنده کتاب فوتبال هتریک میکنه
🔥
🔥
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78084" target="_blank">📅 06:10 · 27 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
