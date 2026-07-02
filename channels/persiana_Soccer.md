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
<img src="https://cdn4.telesco.pe/file/F1dfKESAjAemtbSeg455lqDthi_uu8Sv7zOHVzes2MYBco25llZ6V52_JhjEBXRbxIH-ExbRFAYpNg_RzzYorGzVPPW5fqdXNgz_WrIcUKUEKDqfKF1Jx2PTGnsmt7cmis3qD71IFCaqI3JTjKgatYhu3rrWsjXFV0QFpUwNnnlqOfTS3OpeukYbaHpRgGJ4qx6M8gC5BDbu74k7i1FfNVc97SyiaXn8xz6K1llL3eiNbGZ08yVa3V2v7IvvRrc5UQgaWATUjlfWadVydeXIvhnVn4T5P28iNlUS0c0oOtS9VFyIszuDKdbTzE8YOthZa-I1AjQ9OY0a99_fzlEUbQ.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Persiana Soccer</h1>
<p>@persiana_Soccer • 👥 359K عضو</p>
<a href="https://t.me/persiana_Soccer" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 پرشیانا ساکر دریچه‌ای تازه از اخبار محرمانه و داغ فوتبال ایران و پوشش اخبار اختصاصی نقل و انتقالاتهماهنگی و رزرو تبلیغات:@ads_Persianaaپیج اینستاگرام:Instagram.com/Persiana_Soccer</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-11 21:52:34</div>
<hr>

<div class="tg-post" id="msg-24817">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nyyxxXJL7HyHqd0CFUMqC8u_IFAR1nvSWzV1GEXWJfOpWrNFAHZ7TNmP7EbwNBm8Y88KFxHsfrtpF8x8oi7cJh6pSw2Xft8GRT5LQK4nU50roqcVGIYeYjAC2AfsghhDVeO21NYtPn35Mqe6Ftv8GDfGmFIl1i5n11PpnstZ9SPCc3OgPtugHcpFvLCy9f5xzWpaXnsI_5w1E3LF2aKiA-xMCrvT1oIuy91-RzPm2NO9gSay2Divf7IV7DoGNXawNTyIGTS14hBzPTfqWNlc6-aWfBW2nXxTywLqbB2dQltBEOBWf3k8AYSwkyctp2LsehQhnzwjbZZxx7FtzRvcYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
امشب یکی از این دو نفر آخرین بازیش تو ادوار جام جهانی و احتمالا آخرین مسابقه ملیش رو انجام میده. شب سخت‌برای‌هواداران باشگاه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 7.87K · <a href="https://t.me/persiana_Soccer/24817" target="_blank">📅 21:31 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24816">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xe21vmr-q31DsHyv1vehiOlwZbQEa4FgGaQToYW-ahqXrfP7lvUnz6zaUMTCm309Atq4tSnTEHqZKy-EPpK2UVIDqoF9IzpGvsh-VWQy4Nu5ika8vb7_OtaDnTehQfmNuTnoGVOcJ19Y6ev6BXAznvh1hYJABlFO1dEbyzx6ZLoYkuWIvMj4zxO9q1neQ-qBJxboGJTvJMzSymc2JkIr6CubSbiP5f0Gm231JgZDMQO_OAw43eVJWokMEkadsK8HA7gPTZlGbpk1RcPSeyIzBOMtZgkxZihsqcCRLtFLxZqQn01ymDkD_a-2U9wEyEOL9iSKUmhCZojBFLtO786qlg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇺
یوفاقانون‌کارت‌قرمز برای بازیکنانی که دهانشون رو میپوشونن رو وارد UCL و لیگ اروپا نمیکنه!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/persiana_Soccer/24816" target="_blank">📅 21:13 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24815">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mvQj232-WEVJV-xHqf-arVtTaJ-Sl0YQBfyr2_I5I48nROqyGqvfXLfMBtVPwlnV_d42y_KxJWmh7b1_CjzAB8y82EcxPq11XvsvxfNnisDmcnl4dortBNE2c04Ny7SsZCY4mINpaUuoAEszS6wBrRcWJSTN9Vm5bSGBSAC6nP3Dr1iTvk4EjZyF7iFF05cUclRc28DFNEJT17fX89jLnipi24q1XDlvzhoz8aVAvI4_3gGLBJo-vgpXEIlkeqklSOMNpGXURy24Cv3buGFQ2Ir3XSYDa7rTrgMIaefq4ESQUlvN-b_JjIwebB9PHBYizd2IA20aAi4IAr57h5O-ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇵🇹
🇵🇹
کریس‌رونالدو به‌تازگی و در اقدامی زیبا برای یه خانوم‌بنده‌خدایی‌خیلی‌یهویی یه رستوران خریده! حالا داستان چیه؟ عمو وقتی ۱۰ سالش بوده و وقتی از گشنگی ضعف میکرده این خانوم بهش رایگان غذا میداده واسه‌همین این‌حرکت‌خفنو براش اجرا کرده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/persiana_Soccer/24815" target="_blank">📅 20:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24814">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzV3KgsJpliiDQg_9zQfHapo3l9OICgHhzeDIx_UebXN-J_GXoPVOENCHmrgfUyB4w8Moije1u77OnvKeAXI4O3ARH5fFVZ_JJdGWCDPTeN5iaqSNAq0ja1jmb-D1Q454lrEgrprdmkx10KYRKz5nMWEg0rKh_pXoZnJU3DOsoEug0O18jxTdQAo3j696_yAuZovODE3PP1aiqVsUU8wwe0bYnwRoPv61RBMQ1gEQzmcra3NXBKIIwEG3VN4xyP9evt8aJcA1v7oySxbTKf_ULNMlgutqgexdNbW52cQJpJXMeFFLSQfFyqucgUsC-jKarhr_1pKZ8vGH1o5Ok5voA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم نهایی جام‌جهانی
؛ شماتیک ترکیب اسپانیا برای دیدار امشب با اتریش؛ ساعت 22:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/persiana_Soccer/24814" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24813">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ixYhyzY1v-06ImtxFBg1B36MXDN15TWCgku8QmkMSlfSF7GEeiUTUTE0ZgLO0XdgZRlsKvUQg7-NNhDSV0HSgJdnYB1Ujk_4dfClLMMx9OcEnCN7QAeg83Sn0ugtBTDhMq_KHJr8HCxE3Jay3t4MOeRS4SlDOwHOkOUdkQNBW9bxSKBcV1AQeTJr3hHAbKRAlk5glyq2RV889FDJ8DyPOUpdaLi-HsYGsDYjqetjiNSF4hJhGjxtWhy7DP8IFqFgMMRL91ZX0wgibMEHUWXtppRnNE2xNU8N75wmV1btKk8PeaiS9-PNqwEVzJKTuHxBOq-4KgaqKa5Hg38KWpO0IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/persiana_Soccer/24813" target="_blank">📅 20:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24812">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rTEiAlGioQIygdXPVYaXgTeo4uyy6JZuE6bkrrS8rZ_t8XT_30sBKYIrZVfmmVYECJxASz9DWdD8pcBLU-6VADV1NaJAa7O3EeGatN4CpRTmqpyIqKFPt5CxX7xbYN3sZapRgzkp_gHKpcP2I6ZxEXTNUtDF9WStmgH5ewg5IdaU9tmYOyMl-D0jJKS_2dgzbCD057YhUYBw57Umj3XBBfrCprElHCuLJVs_PZVmaf8LoyElxF3INARipBjkzbjqhkaiT0MHiIxOSQbBuVzJ8XM0MblyIeQqCk_Cm6wq52Tpx7nfMUewd1MNdtn1-EmCkWWCTSIRxenjlgu92KX9rg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نتایح مسابقات‌جام‌جهانی 2026 تا اینجای کار تا قبل از شروع رقابت‌های امشب مرحله یک شانزدهم
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/persiana_Soccer/24812" target="_blank">📅 20:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24811">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYJapWBhNYeDSkQ2AFYhPHUcyAKr9Rr6bTpURQd4SgrEdxOLtUTx3TPBgu1XYrnHX0xhOxiwvj_6e9U9rzVMDLQL5QEp60B8w2dHpCmm2bTTa5ZYg8cer7pNv_HiomJEK1Vobu3y-sBKb73gL6namCxQJlxteIb5G31AgnK-zOG5TDr5Tb9I-nUvLx0-CStaeDgODrO2QDirtIaC6tCnu6d34YuP1V15ps4UVzrcALSbLpd1CQ9n-5415fQbQb_veMwav7Ec_CUvIkeeNQ30AzBQeFr_L4R-VHy_vVgFV1dSado32gTSAJd97WRDK_HJmuf2UFcgfITIj-Idel-2uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش: تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی…</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/persiana_Soccer/24811" target="_blank">📅 19:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24810">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FE7QS4O6i0_a8gP8hMpBS6rBb_QH3pS-LpRm61WAa6T7LRarxvCAnvR4kWY6rFTqPMvNGMGT5phR9Odd65F_jdLJzWeVOSQDJHxffxycsJY7C_qKBvLUozLwPiP5u4P4HW_oQCM_-uzG_kMoN8MIpTQJO9M26b67qbWyxjC9j15KSWYPvFHKR-Llh5l2TZbjbw9b8Mx898E8eOgmL1LwWuJlzF8vk750W_IFWAmYY2SJ6MkJLLNWGemOiZDPrqQAbCipo4NkpmnNw6wuN0P39CUCPbZtyBwzAP9tlYzFYhCInh2egvCklFbJHGsafk0WWShkGn2QzllEC8Tc9vbfow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/persiana_Soccer/24810" target="_blank">📅 19:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24809">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oa_eezBZMs9eSDKr47gjaSXyxpsgc3dEWt-eW57WtYuBLNcQm6-XgNNU_QZknwBj48tpIxItqFqpt3G8N3SLyN1dqCFR1JJtYba5bVyuAVWpUNvRM48j3Tqf-P4tTiVe0JZAGiBb7Hj5M9dE2RYhCRqP8wv7QgzNYuqPN2wLf4GsECft1Bxv9a7Voz5O2mj-5McEfzLAEi3KFH20QnxdNf5N_ks6vDGXP6nHyA6dTw2PK1fbJ2I3tB-0OXZzlIkHCFoccK_2wqn5dTGZDMV99wqAQcbqTiVLdFWxkVhXBejC80y4gXZaSlR73JliFZ0qcrdWXiF6daq_WokIg8gU6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛ نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 33.8K · <a href="https://t.me/persiana_Soccer/24809" target="_blank">📅 17:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24807">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BxGjkm19LTVLDhuxs7ri8Jmz-gZwWKTdwGIJqz9ec2v2qxmdbDlZSk7GmQNDs5Qn-9WO7EgL66aQKoxP4PAvKDxAFy1SgQJOew1yRn3SZDOiGvlTFRJBvO3IRAmjfHaOsbtrbK61N1OfIYaRD7ns80dKsd3xoq_cIAO2onX7p9CT6It3MBDmqxAveQ6DHCyi0jlVcgmsh8fIgU3dEqLR59YQ7LGOD9tbY3P4JucnaAJvyEgP3rDPQz8vmzuQYxSHOGXBoXcuZdBQJRtbrjgKpokfhd81UTKub6hb8E9JvSPd4qEL_5ZZeFVyRzTCzv6h7_cRav8KFSdWKrcADd3EGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KawBcu8T16tx274cXDLHPgKAWOyNWrBZlc6J_efq3KDx4ef4BqJ2wZKao6aAkRbP5jVvN0qY7BeF0symkw65usSF1BWe3xD749IAC2kCHHpw0h5LyUIqYkd3U6gTiRqmDfo4CvfG6JyKVDk2n8Gy9eK_3A763p8BS6jDVY7UoKRUNVkE0Xk04FVO-_JX5I8TW3jfaySxz2bu5edxOs9BhMEhzFR2lNRxiwHnz1DsQNUQXmRNHkYdTXug_Gvs-SJqYAnjXF7lf5iH_JqXCMqZ_nVEnU4p60z42JbDSUMzthBXNGtnKVSMvjpPwxAB80Avc4KhyDKqZTOIi0UXbk6Iaw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🟠
امید حامدی‌فر هافبک سابق استقلال با عقد قراردادی دو ساله به تیم فولاد پیوست و قرار داد حامد لک با فولادی‌ها نیز تمدید شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 36.8K · <a href="https://t.me/persiana_Soccer/24807" target="_blank">📅 16:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24806">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c080f226.mp4?token=egvHbA8jf-Is_m_Q5GkvcqDhkKtOfy6wJgPdQlddHiAdoV1wqjngo02yn9E0Dix8ZF-lnIwkmuLik_d6AHwx9G_gdQCDGhycP8ecxE1vkFqCd_F9r2b52ELfnkcpOkeqdmNWCTbNtzliv5Npq32Yh_p5FIlnM7LEGAqKlbUltUm5fhxOgMaPbiEBGhnRhQVi6QGF7z_vB3HOAna-b0mXIf2aLZ_BPTwt_fmk_t1ivwS8y5t7g1WKp7yzezli86Q1KEQ0EgpOB4vlzPQURjNrXxGzlFdc2-_w7m6AasmY8tRt-znuOskTF4KjQpoWN3ZPlhPs8xdwtNnrRwBgmGW3qA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
لوکاس برگوال ستاره تاتنهام به سرعت داره به یکی از مطرح‌ترین ستاره‌های فوتبال تبدیل میشه. این هافبک سوئدی‌که ۲۰ سال سن داره نه تنها بخاطر ورزش حرفه‌ای تو جام جهانی ۲۰۲۶ آمریکا معروف شده بلکه به خاطر صورت زیباش هم وایرال شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 41.5K · <a href="https://t.me/persiana_Soccer/24806" target="_blank">📅 14:21 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24805">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L6n0uLxmmVZ74ca0Wp4Au7_R6Am_fgl9GJv98NLKZL8tR2A8auH7k6_tB9dfv7G8d38WvIU99OikuR_PC-_s8Tk2aYTQWGUzXJT7za27T_5zeFeVtkIHyEJ1k6OTheiukvWvtIdf_NApb1u9OUJokqXgCMe7xE7MZlpew7Fyajnp4O58AOGk77cNVh2ou4roh6GuyzducRGXBXZuWQEUEZdNP8kNoFxPTGCR_QC_XKHcuKvIcIwJf4tCrGGvgRSAI8O0Q7FsbMrTM9eoGItlw5KeHIHzimvwLo5i_oi_-FHvMHEYTODhOSyCYiDucsqkwsVbS7lgeSdtabqj_DKcDg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بیشترین گل در یک فصل در تاریخ فوتبال:
🇦🇷
لیونل مسی فصل 2011/12: 82 گل
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هری کین فصل 2025/26: 72 گل
🇵🇹
کریستیانو رونالدو فصل 2011/12: 69 گل
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 42K · <a href="https://t.me/persiana_Soccer/24805" target="_blank">📅 14:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24804">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f01ae4b17d.mp4?token=otiOJRiz9Sswf40YAiP8eJJLk1-BVE2oSADagtMXJ_n4VPV4kDvjhP3Uj9BYhfK2xsAqfDLKadgAaJ0fztxVcQrMZv1779u2nW5yBCnIGPZYCZ1QLaDtjroshAmqBRqSu_9bg9xPxaDOWASODuuA8AEWT14QfA8KKpceWmcHBs2t909ag1tpHuoz-KJDdHGcEE_7KU9dkeGv1KRPx29lZriFhaLyBRxzdN2g-hVoAhWZvm9HLjaT4OxxX1ysMlgUkXXXcq8x8QEgBr6qthzg2Fvll9QiwRL0R7J1h0JI6B_C0kQaSj-HjYAo2eLLoyMSz4eAoDkk2OrXz6ypnYL0gw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
👤
بااعلام‌سازمان‌نظام‌وظیفه؛ علیرضا بیرانوند گلر تیم‌تراکتور از اواخر شهریور ماه مشمول خدمت سربازیه و باید تکلیف سربازی خود را مشخص کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24804" target="_blank">📅 11:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24803">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyrSigv_HDdjmkwuaLRJVFhZ5nThInxClJe1K1IZm9STjtV0ICfsT6dheX-cSVcBGuirIVJZ6GVDhlE7sNzifCtOeEJjgihueFXShiBKSoFy0Fy7vPQlY26TkxVeiI8w9I-Dfs7FLtWA-Ea8POxDx0PVyr6lzyMWG_Xd7FdSSYspdXzIEJSArEeKJt3o441ZWI9DWph2g8EXLaCtXrI6HCwr8VEm1Vh0k1PReBU8ZnzWa0lmXMXIAlOQBSpFLJBjN5dN8wYXBDZxWvBJfOILqNAgcnKvvaJSUhkZtKuSLtkMKbyrcsVgpnoI5UW399otOzZoyOlR0eHiAkMHLHOKaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
👤
ظرف‌چهار پنج روزگذشته بارها اعلام کار انتقال دراگان‌اسکوچیچ به‌باشگاه پرسپولیس نهایی و تمام شده و فقط‌پوستر رونمایی و اعلام‌خبررسمی آن توسط باشگاه باقی مونده اما یه عده تکذیب میکنند اماامروز خبرمیزنن‌که اسکوچیچ سرمربی پرسپولیس شد. زمستون هم بعنوان اولین…</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24803" target="_blank">📅 09:46 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24802">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/291e94c0ab.mp4?token=vjq8zW-Nozhl1HL4pDUMCkVko4oHoLRUo7IiDK_G9AN599Hv5GEX2WjdyYSnorcAI6hHeBGZKzx9uw-M55xdVipGRj8bIBXOGOoz2wCAJSIck6GJ4Byx7WGeRCel7laXtNcSnguiFfVqaqY50OD5RcQn-973rurESKBo3y6UFxoq-Cz3BfKJ4bpA-QJuNS1H-QDB2zSqR_97uYQkWVLgt7hJYy6Q6LptPZV-Jytii7ELoKGjcS650xrCdIkGePo7IY2xkwtGnQYF6GyzfpVxFfm8S-FtGbuzQMkqpBxi6UuaSdKNkKTyOY470BeIbec-qISgxC_RSGGDQAspCIOBTw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇩🇪
آقای تونی‌کروس عزیز؛ مگه تو چند نفر بودی که بعداز رفتنت نه آلمان روز خوش دید نه رئال مادرید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24802" target="_blank">📅 08:47 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24801">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o8EgLi-0D4KBTNr5nWn3i-qkuCwLCkCcOa_5PHDqe0r3IBu9YKr9Kk5kSglZphEvYgB3bkAfqlGMrQtxpP8ERgSYxtvBbUY8JxZQ1Kufw5r-Ek18FynpI4poH-T4rdLbk3tKYvOU__AnZTgAb6Cyet6PuZ2NhcOcAtwJ5zHoaMw9N5xkb-QVknndpq85yRshitYkru7RjGFg8T7TQZhJuaHOhobxejCfqUB66D4HI-xwnDtrWBdJUFZFRkTUbU4gpMnwzcIA_n010V1KfmJ5Seq03M0qFZv0IOMZ6iz1b0XJ1W4WPP85TS9N8kW0akH_0nN3qAZssloF8AINcEzY2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نمودار درختی مرحله حذفی جام جهانی ۲۰۲۶ در پایان چهارمین روز مرحله یک‌شانزدهم نهایی؛ آمریکا هم با شکست دوگله بوسنی صعود کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24801" target="_blank">📅 08:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24800">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gVx4mGPuQ6VLm0fXVPxMijLd_LwjXpEJyYT_do0MqmMrJiXguyrs8fuZjH7I61zm-rS1juiqxN702lSguJxRvzPovimALRSgj3V4MOxmjxx2QCxTxslm59wuOBhieD19Sr9P9cfe-ydscVtY8_WMEm6YcL66R4KBGWj2zXn9m6v6hH35ofi3MxQuCy2FjhluLQZg_Eec1iBzcEjXmBm8_NcFsu7KrKiz6DUARjmkQHLOzUe82owl8sprFL75S4NZAmQ0SN5nS9Mf2Ak1taHrXGcSum1l0fQqlFfoDzfia8U0QMcKl69T8AaywnMwiVQSGOqfYYrRDgFbIioHNkSvKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله ⅛ نهایی جام جهانی که در حال تکمیله؛ بازی‌ها داره مرحله‌به‌مرحله جذاب‌تر میشه.
🔘
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.1K · <a href="https://t.me/persiana_Soccer/24800" target="_blank">📅 08:00 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24799">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k-_YS1f924PRXZJMro_kvNM9NpVdoJpgux0C5Z7PzxR0Ri9jKM2KFTjEsj-Ga-gPVlIzqCW3DB2lpT1e_AoBuOjui2xz6cfPJNxMsFBGZcqwo608DDkpXYgJcoEO7R3zljoqoW_LlOohw6imzm6TNKJGxLYNlWgmLvKQyoWSdwTjmQdh41MYbWEEof2BX79PLfrzZ21kAIJiA2cvXJiJDSWgQL1ZcXqXcKlN2VqNZl4wTT1eOLxfrzZtEB-gh4bzccnSCbwmBB8XJnuEUdGGRdyFzd2qz_7jCp5Vn6JOrZVsdLc2gQFztjDMxITEwH2dW8EldywsOgNtqZyNUzsx0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
قرارداد عارف آیمن ستاره24ساله‌مالزیایی جوهر دارالتعظیم به‌پایان‌رسید و باتوجه به اینکه اون هفت ماه پیش دچار مصدومیت شدید شد مدیران این تیم هنوز برای تمدید قرارداد این بازیکن اقدام نکرده‌اند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.4K · <a href="https://t.me/persiana_Soccer/24799" target="_blank">📅 02:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24797">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80ab6c75cd.mp4?token=TmkWmg97gcR9lvLMj8nOZrffaIoqXC1YzWQJR8e5uBnyDCtgqcp3oV9c12nJI61z71pzEgkszKhC03DTbYV-wjIbz4HH3MPY2lL9R0SAhpPXtTEPgBLnaLTpfjnA5XdpTX0DB8MaRhIsM7NfKqyotQMH7Ux8rGGZDhhr6aB0eFrIpIT8ET70nT_Qcbf2ZFEmkWvyXzWNg0Jv1k06qYx-gseIJGMa0WK12GjK8XapEROslpYVmxqnYp6Aa7XmNHpx_pSyBJuWnQUAepbKEw0PrGNn0oh7vwmW_jPQrCbNfQ7Fehu8b9QzMfiNbR2fZ1X6nPhBZLalBhYVxqY7W5_3LQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24797" target="_blank">📅 02:44 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24796">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QIokwPS7kSuo16nvDGQjCT8HwY7-vuHGJPnnMe5awpEqLrQjZKZ1pR4gU3AlCQmXJ6e8qH4J1wi4m0Fd2mz4iMdmXr5AIRxoBY_hrGNozCr8JZZRmkMOS5Qs-HscDJ18BuoZO5biNT9Qs0CAFwqhZkyQr101qX6m9945blee6xSzHXkzw1YQmLBT5n1Q3TDg5q6Z499NJAr1b1GX-_HBQMZemFCHEoh05YMUa21cdcXKqTBFvBuHw-QVR2ikkw7-8NqmCVkOPH2NOEJ2ZgYgtMIuSfmSbJQcpltrJni96YD4_AlUGfhBij0UaZUWhqYHCYsv8xPnDRPNL_fkBTeQNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک‌شانزدهم نهایی جام جهانی؛ صعود سخت و دراماتیک شیاطین‌سرخ‌اروپا مقابل یاران سادیو مانه در سنگال؛ بلژیک به معنای واقعی کلمه مرد تا برد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24796" target="_blank">📅 02:40 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24794">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9G5DZyrdAlP_F7Qt4sNiZqHS0O0V4PfN-Rnb6mF9vfvfaiZMmeVew4CETXb2k8_fNP_x58RBNse5-01RqiuYAnM8hiHIXLjr45wcqXWRDfJf051ff8cIkfTy614Vyf4eoMpHTSM_HB6CjHghz5VTbfeQb6m8R9aM-6NbqPD32L-ajiC8rI199_nHKcLxZOb0_EbvC4q3ZXVXc1zwaJ4za_nZqbbjS-xxCatRRwRmv-vXE_riDngg5abjhlxebzPXqXKpYh8HBS4RQwsbt9WJXv3wohiP0cehVMtugRZ5BraWzfH3gZT37Y_jGXzSPmr0MVlWalof2oHPjKGfgIrrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌ دیدارها‌ی‌‌ امروز؛
نبرد آمریکا مقابل یاران ادین ژکو و جدال لاروخا مقابل شاگردان رانگنیک.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/persiana_Soccer/24794" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24793">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZDAupG5wP883gbffodbhRc-GQ0FH0mSn3xPxNLDvPWdPsg9K1R8cZq88dgcDPtowwUQeNy69j5d00RPW6XQZivELgOpl-2-tzPdkAP1RRj8W6BBYOBpyKnoPVWZHcMyjjSxQgr7hOyWiU1p-bOwuwWF2y32jO5iak375EDogaDCzbwFNiJ7LTQMQPYPBAPtG5tN8s1QNn7XOkTA7J_oOmnvwBJF3kTXKIGiK3EBlLspxGoOkrbteIc5rXchGIIfjjrUuidAtPbIkBzu4DFQMJ322a9q321I4cIlPyZfpFTadCLaEuIRR7IGanz58sogTkcdTRkeyibUC2NSzKLVyGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج‌دیدارهای‌دیروز؛
از درخشش‌ادامه‌دار امباپه درفرانسه تاصعود دشوار انگلیس و بلژیک به دور بعد
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.2K · <a href="https://t.me/persiana_Soccer/24793" target="_blank">📅 02:35 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24791">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iXSkz-gnkM58152Tlktpvn7zoW-3TrZ7OB2kZWcn96u-d6HzlqJePfr1-ff5-TrEg9SYl5B2XXVKa9pgMSx2q1voOVV1ozr0SRQedDiLVM1SdTMscPz-ApO_B4hRmiKMAE5nie8SL2fEERR87xIiXrcOkF-uReamwBcZDoEkLh0K5rFcRn1_yUAAcrc66NgqS2slFCMw4XGvgwdacBT4os9a015aq2Mb-g4sp7z1hUA-mhJ0jXxctihmlP5nBSLpda7w4ashNHZrf28UlYsiLHXagc-780togtcL7dY2x0ZkGNClj7gylHnGOEdIjNrMn3zCPIAVdDpWX2-Z5nOA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عامل‌اصلی‌کامبک‌زدن‌بلژیک و مساوی کردن بازی برابرسنگال رو میتونید در تصویر مشاهده کنید. باید ببینیم در وقت‌های اضافه بازم به بلژبک کمک میکنه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24791" target="_blank">📅 02:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24790">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O1gLnPp5ubZrDDf9CDvLlwdMmIB7K1HDBws9JEB-88zJ5OpUnnaxDXoKtEvYmuboCgC7zEYj79LnT4sz52_gVGyTEmUfEUZZInbf25G8nCUrw3daAzoYJFj43aeEPTX3V5A184pol8T7GZSuZ-BgtH1Y45d0QyXrPWAw_9Xh0cOJPONB0_rVoqAZNaQ70Jd--XFxkVuoS6Nz6MwC5fE7PNwpXPnmQq4FSH9YbnWWB_N8Td6VwxcUDTard3OnxurPCJmsjjtUNr0Mg87YXa86AqoCV7uJv2cdRBBxZZItn1oHtMSJc45ZaKMj0X_qIrXHOEaUs1ifaVvivqgkj_p72w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
میزبانی بی‌نقص و خیره‌کننده مکزیک دررقابت های جام‌جهانی 2026؛ سال بعد همین موقع‌ها خبر میاد که جمعیت مکزیک دریک‌سال گذشته چند صد هزار نفر افزایش یافته است. اوضاع خیلی خیطه.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 45.7K · <a href="https://t.me/persiana_Soccer/24790" target="_blank">📅 01:59 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24789">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/if1jmzBdw8gWsPOktM89dElrIn6IS8zcBkXo1JrF6xt1cQLLvuQ40Tgm9cLbtGY8NasUEKuFze7s-KjEjQniYCei-OcvhwzpuI6VDAJTgqdbgMg2faaFpljVG-82rkW4Wy4GdzziK3luWgUEFhpzh2F4LQR-H2j-IkzAC_4D5oIlBqZ-XfEhpqaijtiLF4FdNghPDKXlTAj2qSVGq5lDtlIFn_XUt1jdLbJAdZAN1yzOQc3guOQG8YhJF4ivUOoqLB-6-MHSE_hguo22_AXLG1isrhdCEUHq2pT3yQYsEdrmaXJnesmq6LCDiLrEsmO1pGJ00K0HEsgpSLKCDaizAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بعداز این‌پستی که زدیم گویا بلافاصله به غیرت بازیکنان بلژیک برخورده و در فاصله تنها سه دقیقه کامبک زدند و حالا بازی دو بر دو در جریان است.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24789" target="_blank">📅 01:37 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24788">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l96hcElqLAg1z50djgda-uCKO7uF84o3YwUPPSAcolQPddFYdl59_P4Nwjg9_eacBdmn2tlDFfyQqVNfNpHaGilWxVYUYawXikbdCQYTn7pAtPJuGtuIV-zxDZUyfxhonBY2kaYWmZEDXHZFtcH1LJKzIDUbduB09YCkcMoi96kdBwPQy2Jgjz-KZXzF0Mk73wteVGV9vb1fBiJpW5fGdKQTVlyTAMkr4_NQSdh8hRZ-KxCPznP5P9_I4yJZGGKDur-5yklC5y7i4KwNKn0mKqkm_c9Gv8zlZ8ObrTj3TW6Sgaqo69-JX03WHNUkq3qj2RihmEPZNHdSi81YffLi4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
وضع تیم‌ملی‌بلژیک رو می‌بینید؟ قلعه‌نویی داره از چی افتخار میسازه؟ از حذف‌شدن در «آسون‌ترین گروه‌ممکن». ‏سرگروهش‌هم‌درحد سید سه گروه‌های دیگه هم‌نبود.نیوزیلندیکی‌از ضعیف‌ترین تیم‌های کل جام. ‏جای مواخذه داره تقدیر می‌شه ازش!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.4K · <a href="https://t.me/persiana_Soccer/24788" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24787">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cD2Yyv_XZpnuvoDurqOma5SdqZyZ5Wh9Rwabe-Nk_O96mpuD3ppT-r_WXfTNWIjuWzYTJXZzNsPvgl_V9QiQB-qghn3IjP76b3qnnXcpsh1eg7sk8l5rwTVV7PQY85l1Zf_hBTMS8WK2sxbH-fZ0BtR_jl8aWrE5ffi3t7Vc1qfCcHjHQdDZR64EYOaTgkZIhtOG145MQPBoSjy94Rvbbmmw_KeSGm-nLhD-9XbHh69m6q-rrqlWxDQekTbeDMLRWWzCUjmQCJkpiEq5szIw812BbMVeBdXOrgcHqK4GMLEQ1VEGO_8cy7hlpnVPq2ZlpksuRTRqTCna8Cr7hhCDog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی: همش فیک بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24787" target="_blank">📅 01:10 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24786">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXrOdKy1EQzYc7XHncqC7nf3gtbKbRvvGc1C4CSqdZjDFjFJcfd0QeKsfHzhbpRqmjwsg8ercHzoCM6Z4WSQxWhhEnZqTIF2iK9Y7CodeBQLehzNixieHnEDhO9wiSdl_kqbaXJzqtC2Qzhv_F2cMrxG02AtqCyN5Jwe491afB8qADkgAIFLdyevpk0Yb9P0sadrEaIrykyyl-EvaFYqOp0pw9oW2gM1IcwgTYl2diYNoXWazaaeQGACn3YPAE7pAHubLVIu6RHbIku4KCCl1HbUNQ6ou1_A_2KKbaZePRCuG8y5jpQjH1dga10PDzwSYop-MilzcH-W5niQvdXTbWo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3cccb9e5c.mp4?token=bVGQLBcOJsypTz3lkLpcZDg-xedZ8haS4TI78BPMxgZrP7SQANLCK_cWjl2HrPme5bCHV9ng_uTtr8gpn1A4rEfCRXMBPsLiaenRXIKlvuOFLpv6exjgy3rHwKpjYyMoOgLMnTPW448JQS5XUcKmONPgqDaWpbnX1urHKvSkIhltk2us7twM1Jdvb7_TqJvBzvpAeYYiW1fL4cCn8E_UzW6b7t3U4kjeljip4zmBAiC2u_1e_1ickIJQO6iHeridK8dUpH--oY5-QMAj3qqu_R3pvcTWZxF2Xp8X2jvUVf53XJATJ4q4bpfQtZhzTvHaBLtgpOSMkQv8aANxhfJKwXrOdKy1EQzYc7XHncqC7nf3gtbKbRvvGc1C4CSqdZjDFjFJcfd0QeKsfHzhbpRqmjwsg8ercHzoCM6Z4WSQxWhhEnZqTIF2iK9Y7CodeBQLehzNixieHnEDhO9wiSdl_kqbaXJzqtC2Qzhv_F2cMrxG02AtqCyN5Jwe491afB8qADkgAIFLdyevpk0Yb9P0sadrEaIrykyyl-EvaFYqOp0pw9oW2gM1IcwgTYl2diYNoXWazaaeQGACn3YPAE7pAHubLVIu6RHbIku4KCCl1HbUNQ6ou1_A_2KKbaZePRCuG8y5jpQjH1dga10PDzwSYop-MilzcH-W5niQvdXTbWo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
افشاگری‌جالب عادل از مصاحبه های ساختگی از اسطوره‌های‌فوتبال جهان از عملکرد تیم ایران در جام جهانی در رسانه های حکومتی:
همش فیک بود
.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24786" target="_blank">📅 01:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24785">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I0KP4vswKS6xEo_u66iomIKVz0A5OSDE81ldeydDKBxEKsl19GlXYL0b-wWRc3OOlE1X40rfgEqW1K-zewb5c6qFqgXWqn3wkp6111-Yr1grMT8cJu7LCLQYXFa7IKEEqayM-azQY6delzW3q6UPWaXs4eqLUGQ-v6yX_Igy_1QtPSPAOZq63DxZGJ9fOWEpqfiEW-P_PwDVYRf291InRGKojBUNYzG9EcecoI-gfsgEzVCuvQerFs-NNNnT2-F47GxBQmhmFvnGTIwt8Z_JGE1KYKY8MTT5TPEHJ89i_3c-3-C0R0s1glCUqozHPvlBREs1-Wkpj9mmUCqJ3CJPHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
#فوری؛ نشریه مارکا: الساندرو باستونی مدافع میانی اینتر میلان درآستانه عقدقراردادی چهار ساله با رئال مادرید قرار گرفته. توافقات شخصی صورت گرفته و باپرداخت50الی60 میلیون یورو بند فسخ باستونی 27 ساله توسط افعی‌ها فعال خواهد شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24785" target="_blank">📅 00:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24784">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lTxMrX4RJWPsBNLiqp7F7kKWDaGOPE5SN9Cdket9jhkXhcRSjObbXneddJ7WmvV31bROxSiFT35zkYrcXyA_HIhLa1VEIcutbzBf8RhxKlZcYPzkCCTzCK_KJ13UHge04u5pv2aBCu6raJxN-xJw997wZFRcp7Ns0RSbWwWOmtH0ns0t48sVr92HXiXQiShJ89vLlUraan2ke4EMMCj95L7h0sxUMcmaxVsGGM-7kVbPwEByaYPH5g_XMDsC3ddFndn8ZLE8o0pZMUDzIpAeWQFJOOCB81E8x8dBI_ToxEwSBUQDWtZI1P_BY0Aeny-8EHt0LjPNvc2kzgHq1dIJUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚪️
🇫🇷
#تکمیلی؛ ژوزه مورینیو سرمربی رئال به پرز گفته نیازی به حضور ادواردو کاماوینگا نداره و این بازیکن بزودی از جمع کهکشانی‌ها جدا خواهد شد.  @Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.3K · <a href="https://t.me/persiana_Soccer/24784" target="_blank">📅 00:12 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24783">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=PKIAwxdqty02ZAtKqQt8mXLVa9Lbk89VyYq7WJ33swb5CDeR4nfynWy6czjc2ggi-KZbRJ3v444CHAhMXJgCtwT8MElRzWxqlgsBFpOeruCTSrpTpPcCPZD5wExqKI29oIJI-306h9gaE-UBAMI1Bj8LtBhITjzaQG7bkaqUbHAsUxEIZpS6o8P3qc5FyU4ZZIax1lmQxJF1N20DInKPylFGb36OrpDHXnglIlAYWgl3D60CkBeYyCFQjqGp7UjLyOwHTqBeoViDN-oICz3Jd-fKZ85Wjn9Oq3zYqRLYmLM0hsQVBXbQhbuTHv58X6q11AsRzpFhpBOw2fxLhh7r-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/37e51a27aa.mp4?token=PKIAwxdqty02ZAtKqQt8mXLVa9Lbk89VyYq7WJ33swb5CDeR4nfynWy6czjc2ggi-KZbRJ3v444CHAhMXJgCtwT8MElRzWxqlgsBFpOeruCTSrpTpPcCPZD5wExqKI29oIJI-306h9gaE-UBAMI1Bj8LtBhITjzaQG7bkaqUbHAsUxEIZpS6o8P3qc5FyU4ZZIax1lmQxJF1N20DInKPylFGb36OrpDHXnglIlAYWgl3D60CkBeYyCFQjqGp7UjLyOwHTqBeoViDN-oICz3Jd-fKZ85Wjn9Oq3zYqRLYmLM0hsQVBXbQhbuTHv58X6q11AsRzpFhpBOw2fxLhh7r-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24783" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24782">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ulEmoFdkYqxm7vAS0kK6A2JcTZy5TEssbDiHCuvivbRGf70rrB5QoT3zitU7Vq5rtLW7t8k0qStLhSrIX4HTORIeCsiJy_LJ80J86jNSEG2N33ImoBicGYbK2laT7BsITUuKqmGkgnl9-fhSNjlrNROe1bBPphskPKwKIwU5vITDKXaH0LtvM097ZXe3e9SPO6gxgTYAax0WfArb6d_5gHAXOUIm_5yaKKpNE2Zq05yAx6uCi4Z2SIU_hUVVgs_BpXLoq4qlt5xVScj-vOkunG3d_BIbb5X_jqCje3UAErpTbUMphFpNBt3vlEnFreqfnC2g8gqp52ZYERAXPDDZyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/persiana_Soccer/24782" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24781">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DVBx6BeSi8t49ffh5dklMOihJ8aQvCSoL_UMUVWAJVAjzPacTuNJ_jMW6N3zj-QZRDAyuM3xDZNizYh0Ia_3RIav5ZprJjPGnaz_sub2R5SYgrLQZ9s8Ij1pw_hdV_MN-nDpBfo4_QmzjInGUXb2dxGXhjVMYWxdfZ-AkvAZxCkiA7IFMuGSWQZsGMLdHGA7TZAhn9PTf7Y90-73g1lEhbtod_Nr_xgss1oFWsHj2nCF3HbEA3_McDyomrIo3ziPfrpsfyepHPahy5qw7z7-MOvMUW47BJ3KRpWGHG7QOVuHan3hZG91pNtu7Dmx7BGpRsn0KWaLlgfyXYPUYC6HnA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛ مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/persiana_Soccer/24781" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24780">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oyyl3zD2t311o3A7AlhWAdU3c_Do0hOCmixYI9tjC7uTUIn28LExt7y6dNs8JnR8LrwVkKDkL1VujkSD0OGg75lTZJTrX-DfH-9GEMR9BibISrKIbc2D7HAXylCAPJ5etnvJFcxlxTbNpBCkeJGW6b6wv7aMl8vf2_n8JEJc_5uEGeQ8Bl5kQwycDt-3Xd_s9uXO-PYdHrP5nv8aeuR7XJQ9_zA4Kc5hVOcl5Uvu-rAWPv3wrX8nCvZUKNiKbm098p2i8Wfha1R9ERZ8tx0KGup0ADmpvexaKrZliRfrvNo-ZDNfVH0BnQZNztyRNufYxhU-tuAbRwUnb8zGtholcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بزرگ‌ترین تورنمنت فوتبال جهان آغاز شده…
📺
پخش آنلاین و بدون سانسور مسابقات منتخب جام جهانی
در کانال تلگرام Betegram
🎁
شرط رایگان ورزشی
🚀
100% بونوس
🪪
داراي لايسنس بين المللي
🌐
فعال در بيش از ٤٩ كشور
پيش بيني رايگان ورزشي در لينك زير
🌍
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 44K · <a href="https://t.me/persiana_Soccer/24780" target="_blank">📅 23:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24779">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32137f795e.mp4?token=dCrVSrz2OzOdvf5oz2H2g_EbhE5_QMpCKCZ88PWj9JZ3hPKabXVdHGo-yBOVucleS2lpo0bAkUhXto78lcJqnbK42mKiJy2BYG3uhNqKbvzd6FNPmaVaDBdSJKuSUv5CQ6sgKS9JRxPOHj5Hgj5ftRLxkrRCSNY8bavRTaVm6tuC5VtWo8fiYnNdAbUo1SAQ0xHzOnO7HDPSwMCSzzp2zNzM32gcuJHb3-s8VPGx3s0CuVoyLQFcmVasMO58ja1643QsX1Qm2TjGmVLYPSURrqPz_VLt13zpY9R782lxY8Rq6APYHfNHHkF4u4EtlattuKfP0AdQAvd-LaHisGq14g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32137f795e.mp4?token=dCrVSrz2OzOdvf5oz2H2g_EbhE5_QMpCKCZ88PWj9JZ3hPKabXVdHGo-yBOVucleS2lpo0bAkUhXto78lcJqnbK42mKiJy2BYG3uhNqKbvzd6FNPmaVaDBdSJKuSUv5CQ6sgKS9JRxPOHj5Hgj5ftRLxkrRCSNY8bavRTaVm6tuC5VtWo8fiYnNdAbUo1SAQ0xHzOnO7HDPSwMCSzzp2zNzM32gcuJHb3-s8VPGx3s0CuVoyLQFcmVasMO58ja1643QsX1Qm2TjGmVLYPSURrqPz_VLt13zpY9R782lxY8Rq6APYHfNHHkF4u4EtlattuKfP0AdQAvd-LaHisGq14g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
شوخی جالب هوادار تیم ملی با امیر قلعه نویی و شجاع خلیل زاده سرمربی و مدافع تیم ایران
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.5K · <a href="https://t.me/persiana_Soccer/24779" target="_blank">📅 23:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24777">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fpTAaCo6FqABJL2XpnvbjuANKbgp0VJ9qtQlVP_DXnkBQypqS6vxXiQlNJkQ--6CNlsteB-zK-54ZBRYSKUJecc0tFYKda2ow1Zk7xOcB4KgcXg9T_F0A8RN5amFclIwGXUjSixnzBr60V68hePO5RU5XWOZ10cSAchIwUlDtkDR4VWcilSpB7HyxCgRsmIjv-NG6lbdFhn54VXbFzwn1O27J0vz5FFfgjc4jT84JILGMwL9YO4Kwaug-cVxyxscEN24gAfk-glmD5zj01CthpJlTDEQFsSP1ILZmUaFg4TfrVBt8uUimx9l6FeNsoUGPRfnjgWgSgpV-PIBHJEL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون: نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.2K · <a href="https://t.me/persiana_Soccer/24777" target="_blank">📅 23:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24776">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👤
تیکه‌های سنگین‌وداغ‌ عادل به فدراسیون:
نکنه جدی‌جدی پس‌فرداصبح با سوییس بازی داریم که ما خبر نداریم اینا خبردارن که مراسم استقبال گذاشتن.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/persiana_Soccer/24776" target="_blank">📅 23:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24774">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/310289702f.mp4?token=PnQyCi3amLl3MhIn1DerglHPbIDm_6nOnWpbjacxXkpXhdJl5xR2eljSCVrw3APzBmaDOo8At5Po7fbs9Pg07zPMHOVRMLbeJNeCZIggga8-i69xAc23yVr6V7hZTzGZku36CVGnprj8I_nNSx54N3Pp67XLCJGdlg5eFUR40a5PTyi8gLXSHm1EFCz1szFUWq3gytEwn_YfrFspnEWMpaV3CjaZEvnjyd6F-hy9PQwcIHAtUkikWc09llQl24V1OgS1BPX3bvpkQJgOObOyeFCtK_V_lTKv4j5PXADwHvB0AS6Z4OExK2dgCeA36hDOR5NKdk8-IYOgKzXmFCnmTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/310289702f.mp4?token=PnQyCi3amLl3MhIn1DerglHPbIDm_6nOnWpbjacxXkpXhdJl5xR2eljSCVrw3APzBmaDOo8At5Po7fbs9Pg07zPMHOVRMLbeJNeCZIggga8-i69xAc23yVr6V7hZTzGZku36CVGnprj8I_nNSx54N3Pp67XLCJGdlg5eFUR40a5PTyi8gLXSHm1EFCz1szFUWq3gytEwn_YfrFspnEWMpaV3CjaZEvnjyd6F-hy9PQwcIHAtUkikWc09llQl24V1OgS1BPX3bvpkQJgOObOyeFCtK_V_lTKv4j5PXADwHvB0AS6Z4OExK2dgCeA36hDOR5NKdk8-IYOgKzXmFCnmTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
حمایت تمام قد امباپه و فرانسه از دشان؛
مادر سرمربی تیم ملی فرانسه درگذشت و او برای حضور در مراسم خاکسپاری، اردوی تیم را ترک کرد. دشان پس از مراسم، دوباره به اردوی فرانسه بازگشت تا هدایت تیمش را ادامه دهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.5K · <a href="https://t.me/persiana_Soccer/24774" target="_blank">📅 22:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24773">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoePZA5nMzvv5HwO_fEh3KohCxOlt1KU5zauwo0vbMmTh04IABJ9Dy7rPv02UBgfxk-pOI-3or7Jop_qiVg_DE8RZ5NlzAml3HqjdrvgRBLA6Bzzy788xpDTt_D6IfhdpV1uquN6AFZR4XBRIdu_SXkTEKvCPqm5T3osXLRYC1FLGbuTP5dittlgDdKIpjqHcJXAaMGNefKCKHOZzMMitdgBh6gzBVX7x0u8S9BiHikiPEGVSZfTfXl4TDDKX0DgrXYupgKoHoC66iC2D7WmnKHF4poT4RLV4n6Re1Jpze-A080-oL3n6pgK1JJVmOckhB7lPiaDExNAFma9RtbiCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🇧🇷
این داداشمون کل بیخیال تماشای بازی برزیل مقابل ایسلند شده و کلاهدفش‌از اومدن به استادیوم یه چیز دیگه بوده که تو عکس مشخصه دیگه:)
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24773" target="_blank">📅 22:12 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24772">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/teWN2ftVke0aVSAxkn0aJ-cSblO94efHI28po9RTuz7-Wy520-tN9vYmLZf2BRXqejEgvYLsY9BMCykitBrLzqc0M2wC2BdaD0MAVL_bjg30FbyISQ6lNswet06DHSzmYKMASD_R64pxia9Ap_zg8aMsBtdP__fZnX0C1nk1hzuNpOry30_KWys26D8QI7T2GlQ-hn1Hh7G_BzPvKnT9agqJM-TfHVb4dq8F0kPLgoTVhRx4V041S3nkPAg0OxdYug2gsOAM2MRCWOX15cxrpK6Ggc6qfLXYLf46H9RRclS3_AJSmBaaoJ15940u7cmgdKki_jTiaTeq_LsdB3-gLw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
تایید خبراختصاصی دوهفته‌پیش پرشیانا؛ یاسر آسانی ستاره البانیایی استقلال ساعاتی قبل به تهران رسید و در تمرین امروز عصر ابی‌ها شرکت کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.6K · <a href="https://t.me/persiana_Soccer/24772" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24771">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=STebYyx64_wyceN4nrS7YXyMxOfPL5HeTaiNzdQl26dFpucHnsr5lygkVWrXi3Um3SUTJPmKGUq-gsunQQbxc5uYoFwG2x-20z8uzW0DitV7326Z1xIRoXYCEwsMp86D3C5jz6OADp5mwAl96UxnLl4lEUjOJcZOJ80Ol6JmDYpIvsqadU_CMXR2vfAWbo6Wzux5YUo6M1SnXhtk41efBqjAUM80iyj3KdM-Q_o_AkIjrlgdpRB4v1k2QaQgKOJyz-EtOpGdTLglcnL6xIWJ1Cb3mEUphWHwLpDwVJ0Yazw4hjGQppaMILkeOzIyHL9Vs3QnRzr7_0L0Kp7P1udJwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80508f67e6.mp4?token=STebYyx64_wyceN4nrS7YXyMxOfPL5HeTaiNzdQl26dFpucHnsr5lygkVWrXi3Um3SUTJPmKGUq-gsunQQbxc5uYoFwG2x-20z8uzW0DitV7326Z1xIRoXYCEwsMp86D3C5jz6OADp5mwAl96UxnLl4lEUjOJcZOJ80Ol6JmDYpIvsqadU_CMXR2vfAWbo6Wzux5YUo6M1SnXhtk41efBqjAUM80iyj3KdM-Q_o_AkIjrlgdpRB4v1k2QaQgKOJyz-EtOpGdTLglcnL6xIWJ1Cb3mEUphWHwLpDwVJ0Yazw4hjGQppaMILkeOzIyHL9Vs3QnRzr7_0L0Kp7P1udJwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جدال‌جذاب جواد خیابانی
🆚
خداداد عزیزی در ویژه برنامه رقابت‌های جام جهانی 2026؛ سرپرست تراکتور میگه آقا جواد واقعا دیوانم کردی دیگه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24771" target="_blank">📅 22:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24769">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=N88QaofRE3d8JXD5nGvxp2Aevok4QJ1Rppe4UNzlzqCsx4TATMlpPMgQ1oOdJ63UsvGQdcUlL0qU9042qDb4gMymjYBrKPTFVtW1M1P1ktIFu_eg7stp-dPSqO3x90a6wLDy9V6bJiFSuFwYm972EK8TlXrvq_R55Z72Yhk3WKSwXD2D_rYKxkeIo2BG1Wgf4r9nNRi-5K2yNQIO6FjC2oi8YZ6HiNmpgsQOO-zspxmc-Jq_B6-uRle1FnWWha71xsHEjRjBP_N0oUHGcGtx5N22bmMHdIO0NPqwXEPk8pyyUhpLzmAU1WNhp8GHOryPG1pIdNG3NL60oF_4N1t1aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/515246fe2d.mp4?token=N88QaofRE3d8JXD5nGvxp2Aevok4QJ1Rppe4UNzlzqCsx4TATMlpPMgQ1oOdJ63UsvGQdcUlL0qU9042qDb4gMymjYBrKPTFVtW1M1P1ktIFu_eg7stp-dPSqO3x90a6wLDy9V6bJiFSuFwYm972EK8TlXrvq_R55Z72Yhk3WKSwXD2D_rYKxkeIo2BG1Wgf4r9nNRi-5K2yNQIO6FjC2oi8YZ6HiNmpgsQOO-zspxmc-Jq_B6-uRle1FnWWha71xsHEjRjBP_N0oUHGcGtx5N22bmMHdIO0NPqwXEPk8pyyUhpLzmAU1WNhp8GHOryPG1pIdNG3NL60oF_4N1t1aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
هواداران تیم‌ملی‌آرژانتین میگن: آلمان داره تقاص این فینالو پس میده؛ جاییکه این دو صحنه به راحتی میتونستن سرنوشت قهرمان جهان در سال 2014 رو تعیین کنند اماسرنوشت جور دیگه ای پیش رفت ولی حالا آلمان بدترین روزهای تاریخش رو در جام جهانی تجربه میکنه. تیم ملی المان بعد از قهرمانی در سال 2014 در سه جام‌جهانی متوالی به ⅛ نرسیده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24769" target="_blank">📅 21:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24768">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SvUZreU0V7K2Jow4a-vGTmsvlaKodzDh8FZkymvx57wpM35yCiDQ5g7AVys212ujGzaB3xQVMdIHMFIFOfl5aVszBx9DbUV_CWELQl0Ob4RJjpHUsvCQWC66UrgmJ-Q7J2n9_jj3Rtw6cgvT1tp417OB7gvsWmrMJK4iLK8_2DcnVpk-u1UlVcuJtemn4-Ojm01ta8Su6PC9GxW7SD5nhWpMPSHazFSVNVFt6OGLle-NW0cCG4xzv1KI3D9alB9_LSQ0jxEljx0wSIKa_CwB5er-ijG4paxtzwjAa9TUQmqV2HVonvBazMLxlxAYDntlA4rdgzhWfj2dbdTUZm6m0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نجات‌توماس‌توخل در10دقیقه توسط ستاره سه شیرها؛ هری‌کین باگلزنی در دقایق 75 و 88 مانع شکست فاجعه بار انگلیس مقابل تیم ملی کنگو شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46K · <a href="https://t.me/persiana_Soccer/24768" target="_blank">📅 21:49 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24767">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BH_2hHXVd7RDq335e3gCEX9OR_OaoHWGBGBHv_cP43XO9FmP0sp6rwx5OBeckfBUrbNqaBRgNlMkMlf6MXYrQ1xW5d3IoF18meS04M3jRoaJajVxD4EdWatMSB4Sxu6SHI8iLVq2JNC8MNoLcYMh49Q7J_8yq8uabjpNCiO1gelT4Kh6v23QBntCITHQrET4Or9HZHrb7p7THYPtPW7EgG2PLMHpRB80SrqEAwAt5_3YMvUO1Hc7oPyZPIoBk4KF79DN_0e7CbZV03_OP4zpQn0bWhHTwCFBrJn_-qf4ZiLqqk8vdzipujGN3gms67u8NZ45hb5yy0tI8C-KdoFktw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
دروازه‌بان31ساله کنگو درنیمه اول دیدار امشب باانگلیس سه‌سوپرسیودیدنی و نمره فوق العاده 8.3 دریافت کرد... باید ببینیم نیمه دوم هم میتونه مقابل فوق ستاره‌های انگلیس مقاومت کنه یا نه. بازی نیمه اول با برتری یک بر صفر کنگو به پایان رسید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24767" target="_blank">📅 21:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24766">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V15gLs413-VEHlLLXfD9j3vLC6BiJdXTP-CBlYjMnkmMNorJrtmyEC3zOUZxkdwFdRAWXm3F0RYMpq3A6N-APXTM3BV9zN5uHIIgu5jMfKk660QNJNmWecKk716jIvUkE2Icv5Up8OGbn3ff-mlRL4eO93yr0hKtK9SEJmRuQZ7FM-PeMTQCxCbja6FGRo8uXZlI9uAP_YGLKtsGK0T9bQ7cXdOYUrnyPdpWe25T1Zy-WJrbdNAvSmA0nVYKHQ2nXPyW6TxPV_E4ktfzXO9JmvuAsW5liiOMnY5LMyxAWEPGwWUAmA7TlXJAu7cD6B9sAs8Imu4vXMhnJ5krwuChxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.6K · <a href="https://t.me/persiana_Soccer/24766" target="_blank">📅 20:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24765">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=WGfbZgUVlHdEACkKndLRXx4-FF6cD8TdlGmSFbE5B2R88tiOdUAMbG_NGzGB1ZxLvk6oTG3392c2h38gkcWMPf5lSSE4AY9XKhEZItVNJaCb99OhHYyq0p1ZdpgABIJ_O82iwg3TxMHnEWUwoWhHPRyxn7BBOJ6bX2H5vyj8pRGif-ChruliVgfpOefSh74Qjp-Iw78xX-TccwOnwGUT9vVUb2V_go8hr0wqpHjoKIHG8oepita0BneokCRdMFQH-btti1C962cyAUjlUPpIRtJ6iy9FwjIkTw_ybReVfnSSTpEIoeoFlTNh-dNKkFyaUmkGUBKgmzxhjYpNpUjnzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47867a7c2d.mp4?token=WGfbZgUVlHdEACkKndLRXx4-FF6cD8TdlGmSFbE5B2R88tiOdUAMbG_NGzGB1ZxLvk6oTG3392c2h38gkcWMPf5lSSE4AY9XKhEZItVNJaCb99OhHYyq0p1ZdpgABIJ_O82iwg3TxMHnEWUwoWhHPRyxn7BBOJ6bX2H5vyj8pRGif-ChruliVgfpOefSh74Qjp-Iw78xX-TccwOnwGUT9vVUb2V_go8hr0wqpHjoKIHG8oepita0BneokCRdMFQH-btti1C962cyAUjlUPpIRtJ6iy9FwjIkTw_ybReVfnSSTpEIoeoFlTNh-dNKkFyaUmkGUBKgmzxhjYpNpUjnzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
فیروز کریمی تو پخش زنده شبکه ورزش:
تمام بچه‌ها زحمت کشیدن. آقای قلعه‌نویی گفت خدا سر سازگاری با ما نداشت و ما ۱، ۵ و ۱۰ سانت رو تحمل کردیم. حالا اگه به قول شما لپی بوده، مال ما لپی‌تر میشه؛ ۱ سانت، ۵ سانت،۱۰ سانت رو تحمل کرد، ولی ۳۰سانت رو دیگه قلعه‌نویی می‌خواد کجاش بزاره؟!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24765" target="_blank">📅 20:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24764">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bl3zmtTYxQd_1-r-rB_ivCBrElliB8cP6j9yRYAgzzZ4UdFOb7nDaXIgOXmD_wQA5HdMZr5H0slVFQaLQU_OOKmxoNjl2MB9306soFI6XqUxRcuGMXwbk7ObCAwkzoQbozJRkk0B_5lMW86ZRHWW-83UMP7Tn7e0HzO-m7SgzqHLvhnoIQCGAa3_GYbS2cVGqy9ZsC4r0N_Gv7JCVxhggLKukKkTiOdkUQ2ySHBYy_zMqKayuT8lPfO96A9ieLseLFYqqxg2Bmne5FfwgIZlF6eZjBb4coko9k7vQzhV_NBOA8BNUyCe8mHa2WJxUC_BaL6vimXPipzi3AAe_8e6rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره تیم‌ملی‌مراکش در اوج روزهای سختش دوست‌دخترش او رو رها کرد چون گفته بود که اسماعیل نمیتونه یه زندگی لاکچری در اختیارم‌بزاره. بعدیمدت میگذره و سایبری‌باقراردادی نجومی به بایرن مونیخ میپونده که دوست دخترش بهش پیام میده و میگه من روببخش…</div>
<div class="tg-footer">👁️ 47K · <a href="https://t.me/persiana_Soccer/24764" target="_blank">📅 20:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24763">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=qnlCUe7MWgRz5j6XkdGFOibV1qT0qs_GlwjIxlBExF17lEIT3AlG1NDoDJduwt2U913UzOJp7Dxu4e5d3MJUAXO8IEXnBysoc2q4dgFAgx0TrRlYsuWEbC5OSMQLmH6Ozi8BPz1mt01qEnLsmYF5oBQ3drMzX2aSxFfFbUqbktTMu8TpIoXgbRH1ZBjbL0MQJt8jsF21VABGyX0-dgLGgrsDjfda-Z87jwdMci5LDW4hQjzLuKeK_Mljyjf2A0W_dGy2uWe1xrgUFW4uyFbcQ7lriBm4q868ASN7yKGox_rrGFtY3occnimJ9nsVOk3Vxfcg98RRl-yvy8mjh6LrJA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f5a4f2228f.mp4?token=qnlCUe7MWgRz5j6XkdGFOibV1qT0qs_GlwjIxlBExF17lEIT3AlG1NDoDJduwt2U913UzOJp7Dxu4e5d3MJUAXO8IEXnBysoc2q4dgFAgx0TrRlYsuWEbC5OSMQLmH6Ozi8BPz1mt01qEnLsmYF5oBQ3drMzX2aSxFfFbUqbktTMu8TpIoXgbRH1ZBjbL0MQJt8jsF21VABGyX0-dgLGgrsDjfda-Z87jwdMci5LDW4hQjzLuKeK_Mljyjf2A0W_dGy2uWe1xrgUFW4uyFbcQ7lriBm4q868ASN7yKGox_rrGFtY3occnimJ9nsVOk3Vxfcg98RRl-yvy8mjh6LrJA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔵
👤
طبق اخبار دریافتی رسانه پرشیانا؛ رامین رضاییان ستاره آبی‌ها به کادرفنی تیم استقلال خبر داده بعد از بازگشت به تهران 72 ساعت استراحت خواهد کرد و سپس به تمرینات استقلال برای فصل جدید مسابقات اضافه‌میشود. این درحالیه به تموم‌ بازیکنان ملی پوش 14 روز استراحت…</div>
<div class="tg-footer">👁️ 46.1K · <a href="https://t.me/persiana_Soccer/24763" target="_blank">📅 19:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24762">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CqC1nQrGv8HhnAmXCPaHgN8fKMhA-FPAhgxOqvcqgAIfYsD1wCn-jMomJ_wsNEyuo1K17a2KiT9KesydGgItNoM4ld17w-AmIWEV7qx1nvWeRTRIAzAyYLdySuoaSDE-LTkg0I7dQuglkvyd_zZK0QwluMx0_jjW6wtFAOtY2Bw6zgVtOu21iWIlv5i_xonQ52cVRPgnXpJaFT4Abmuy6IEvUCVPZqXzy5jEcHH7BJgy8ORPPS_53TNk0zGvgxjMKoFnf-MYf2S8qd83WjCx9t81UOazwr5S3FaYUI52pI9IocquPC8EMRbgVrF8TQqZqsrnbrjAlAG23a48-vaipw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
🔴
پوستر باشگاه پرسپولیس برای اوسمار ویرا به‌مناسبت‌جدایی‌او از جمع سرخپوشان؛ همانطور که وعده داده بودیم پوستر دراگان اسکوچیچ هم آماده منتشره و بزودی توسط باشگاه منتشر خواهد شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 45.6K · <a href="https://t.me/persiana_Soccer/24762" target="_blank">📅 19:26 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24761">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=q91SY4FQPspIxQLPo4VcknijvOzkj3IWcOJQa5Rw_CkUrArwbyc6pbriiyTIw8HV60r3sIjdHEw6s4_x_WorMlzm3dtorhI0Ab86vliyY4SV1XWdles3dDVARNfC88fDoGlqCFDvFXDSuuw6IPZqW7BURu7CeMalIq31BnYwJRPu1NL9YXTFu3wv9kP_SP_YHNjPmMocYNGDfMReVUHEMlhIcVf33V9ZveHpdktU4uZ69mJjKEJzB4fy2weuqO6kg93Q8s5oJPHZ2G_9YZKAoFvkT1v5waSL9pFyc0Lq_HceF7pcjpkuuVN2QBdI4gEVQfGoHGttp9UMpnOYRvUfxQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e8851fdf93.mp4?token=q91SY4FQPspIxQLPo4VcknijvOzkj3IWcOJQa5Rw_CkUrArwbyc6pbriiyTIw8HV60r3sIjdHEw6s4_x_WorMlzm3dtorhI0Ab86vliyY4SV1XWdles3dDVARNfC88fDoGlqCFDvFXDSuuw6IPZqW7BURu7CeMalIq31BnYwJRPu1NL9YXTFu3wv9kP_SP_YHNjPmMocYNGDfMReVUHEMlhIcVf33V9ZveHpdktU4uZ69mJjKEJzB4fy2weuqO6kg93Q8s5oJPHZ2G_9YZKAoFvkT1v5waSL9pFyc0Lq_HceF7pcjpkuuVN2QBdI4gEVQfGoHGttp9UMpnOYRvUfxQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇪🇸
لامین یامال ستاره تیم ملی اسپانیا:
«من اصلاً دلم نمیخواهد که‌همه ورزشگاه‌ها تشویقم کنند! هیچ نیازی ندارم که در همه استادیوم‌ها تشویق شوم‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.8K · <a href="https://t.me/persiana_Soccer/24761" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24760">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cBtKWV5vvQQhs0J-7M7Fw90v2BxukxEbGex7g4w4hFCy3LXUx0F9dswmPnBzb06oYlCPWTulTSZevLUVXsGPz3ERZswEZlv2b_IckcJr3kGbwBMY9ATHH5QY7Jx6XtAPfXeLHjb0uIM-foJFyN-UNVxmwSISn8ywZNtyxAXLnXrrxJDu5bJFOly3KGWePg8WPXVtvGR4Hc8nczIPRKM21ndqurUoUq23YWCzfrMG96d5YnKpKiLTORK0koTLLuJK1H1SktrN4PjNekq4CePUpdqz2Ic2Vd3NdQQd-_SxiLqa4koW1fW4a6k205GaYwWgDzCaB3ZODFLhwIa2hD0k_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 44.6K · <a href="https://t.me/persiana_Soccer/24760" target="_blank">📅 19:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24758">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ic2FYcxy0P7zzVE5AXxDGvMlc1V2ieoywjfZzQC_cxB2c3WJSsGOocnNDnaPP4hDayWtvN6Ehb7E5_g6iJGUJ9yYWBsCtbtkROPP8Q0bIbh_t3tYKGp78gRTnoAVRhW0q_FBRVNzz5QC58Mf_3kkjT9dPPsrsifurHXKT5OSzuoPwW_l2tAu-cwm8W2vB_XJitIA958tUGOJ0JTixbHJwnJHFQNTRi-utTfb7CwsYUqTfXJvhHqVUAd3CrvmyfXMhUxn3wIQyNVQHWW5TVVoRemu2NYY1s8ZaHSjaYCpfyVtCzTObZwy5kSUJoiA7rG50Wj3MxU-eM3EeInfZHZTHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/persiana_Soccer/24758" target="_blank">📅 18:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24757">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L8CbX2kYxflrFzzgzmUMOVIyA5ORaT0T60-iht1iUIdSJN0Fn4vH4jQrhZf7OWLspUwhD-cjB5nNqMPjhhDDLQRsZ8O2qt2liua1Ae0dUTAWLDTK1wHRWvxFZXuK5LYY9UKu9_JXKEDA9LhxaHQmq5IK0MsSKugcglGpEXaDEpgwypSrPLLOyLmeOZdB25jebd9no507N0Mh4-37FC33XWGoLYHGQQ6C_V2nSeCFU5_0gj7o_EoJcQjhonGbppC0H3XjjuK-lYE2LoHvYwB3F36UQONXrRPHPIOGST8YqFTrKxy4JVkh5GegV_iFhCiFwiMRzJeGr68mhfi_UFWnpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
یک‌شانزدهم‌نهایی جام جهانی
؛ شماتیک ترکیب انگلیس برای دیدار مقابل کنگو؛ ساعت 19:30
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/persiana_Soccer/24757" target="_blank">📅 18:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24756">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YzKaAl67v5JOTs_li3pmExXo9nlrbxXsoX1ThO2ua7mjXcQ0mWYWbl4WcLhNLImSiZl52z542dQY9ihgs_oddskEiACKmkNpwOm5cEg7sQzwJGj-6CsyiOI6FF2iCeqx5WblR9H_b9CQkSbAc_z4owbTgpDWIPaBefQAns2yhgTmll-C5T7O-l1d-IimYjAqnrxjKq-ApJPeIPzABolJbidnelSZUK4QFTpfA9PdW1BILT3hgwEk_4ue-EziLT515egwaofV6q28eLdypDCZLXfUShyjIKJCR5R9uhYmqfi5EIEyvong6Y0nxU3r0D-dx2slDZXYVaS2RxKq3_l06w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق شنیده‌های رسانه پرشیانا؛ درصورتیکه اتفاق غیرمنتظره‌ای‌رخ‌ندهد و اوضاع‌کشور آروم باشه منیر الحدادی و یاسر آسانی هفته‌اول تیرماه به تهران خواهند آمد و به تمرینات آبی پوشان اضافه میشوند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/persiana_Soccer/24756" target="_blank">📅 18:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24755">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qWvMTpKfjuhknEV1gSeZCIJXeKhyZUtpT5Po8Sk9no1ev4Ocplg0wZ8mhSl-e4hp50KqNiMvgHgZH0Xes-4D1ezg7ko91cbCPKXQ__2jzpfdzE5bIsnPhEsUL9EWQvG6yDWkUqByumjhugPMPBjaGKQ_ds1KDcf-KgLK9RHgWuphyIqK1KsTPwtDYCKdBaYOnsoITsOB4zywLp8_XMIEIxRoU3ezT0qgKCeye3M8JG6GR4Ms2d-LpyaulG_gkz1e365qlMyM2MhHSstMcqdH5Vu9cFoGAiDUMENSsw_xUB5h5p5iGzc6_vzdfbYduR2U2qQLMxhOZZz2KyzuEmdAKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#اختصاصی_پرشیانا #فوری؛ طبق آخرین اخباردریافتی‌رسانه‌پرشیانا؛ اوسمار ویرا دقایقی قبل رسما قراردادش رو با باشگاه پرسپولیس فسخ کرد و از جمع سرخپوشان پایتخت جدا شد‌. بزودی بخش رسانه ای باشگاه پوستر او رو منتشر خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.2K · <a href="https://t.me/persiana_Soccer/24755" target="_blank">📅 17:17 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24754">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=HeXx_fyt81WavLWYNLqH37lbcSG-ShU9ng9cQQhSoFeRXmDB9sl32u3R3qJKRfRiOioidFJLRbTV8ww0xlXFQSBa8dcw25ouUprQv3M1qAbl2U82Li0fhVYR7Z9e_pdgmA-d9_-wmoHhVyfkYRR6BWAW-_P778Ty8drjzIsPqsWj3uIWnlRNsNRngZVKzEec6b-qDYGfMRr40qvmLAFV4E5Szre_I0ERJH0IRF_hovev2yEPtBRQu8LdXWl040pP8JAgFjByQuZ--BT48s_wlmO3ESWEok6d40nNTiZJr11eAQlWQcFLzvlaMExJkwlvMg6ked5sEfXm8qzapnnNkD_HMztoCDCImiBwYdUl81dcH2GmiW72f_xAXr9x1QX42UpV4d_Z_oXZE1TgJcVjSdByezb9a7hy897IIN4ut-f1yqxZXAnREpkdmxOZemUndrfNKE9VptiRmV1t-RYmh24qvCNjqb9zL9EAhawAJWpx9R7zJOdo0MyqCZrVb48WGzSYxMo7PHIeDdZI0pbEzF4PPf0MNpfA1pE16Y3no_SGo5YFc3G04leoK9G43BuUCVrdGcD_X1UVFNLocIXAZ6mPO-biwunqVWIJ3MgoCAGQsHZpBr5H7cLyH0aLXVeHsMBCcW_JoQ5C9GK_Bn_XdSlXUx2fPQ0v12uNFphmU0M" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6dba2ae9cd.mp4?token=HeXx_fyt81WavLWYNLqH37lbcSG-ShU9ng9cQQhSoFeRXmDB9sl32u3R3qJKRfRiOioidFJLRbTV8ww0xlXFQSBa8dcw25ouUprQv3M1qAbl2U82Li0fhVYR7Z9e_pdgmA-d9_-wmoHhVyfkYRR6BWAW-_P778Ty8drjzIsPqsWj3uIWnlRNsNRngZVKzEec6b-qDYGfMRr40qvmLAFV4E5Szre_I0ERJH0IRF_hovev2yEPtBRQu8LdXWl040pP8JAgFjByQuZ--BT48s_wlmO3ESWEok6d40nNTiZJr11eAQlWQcFLzvlaMExJkwlvMg6ked5sEfXm8qzapnnNkD_HMztoCDCImiBwYdUl81dcH2GmiW72f_xAXr9x1QX42UpV4d_Z_oXZE1TgJcVjSdByezb9a7hy897IIN4ut-f1yqxZXAnREpkdmxOZemUndrfNKE9VptiRmV1t-RYmh24qvCNjqb9zL9EAhawAJWpx9R7zJOdo0MyqCZrVb48WGzSYxMo7PHIeDdZI0pbEzF4PPf0MNpfA1pE16Y3no_SGo5YFc3G04leoK9G43BuUCVrdGcD_X1UVFNLocIXAZ6mPO-biwunqVWIJ3MgoCAGQsHZpBr5H7cLyH0aLXVeHsMBCcW_JoQ5C9GK_Bn_XdSlXUx2fPQ0v12uNFphmU0M" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
برسی‌کامل‌ودقیق‌شدیدترین‌مصدومیتهای مرحله گروهی جام جهانی 2026؛ عالی بود حتما ببینید.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24754" target="_blank">📅 16:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24753">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=ANj3FLv45AyzvhmLOW4BWIJZ_AdIUg_bRrKl6L9Cg0IbZuYDyDanyPFMc6E5IBP2midRChthZ3byZeQcyRZNfgHLbLgbn2pmwf2EJ9bmraA9biCrna6akr-Nt9qU7HdI3qdca5vcHpV1wr-FmYVRYgZpQP_2cXQ6flQp-jY3jAjkc8ArEU8GTzwF0RhUPQ20Dv4JHsVSPTSXwxZ8Csm4dtO2AEFm2QCwuyodXTKv-TgfddhKR-2IZ49pG5oCbIXrXDSJkPq2pB0ZwkTfySzRWAeOXgtv5lMNhJPnV2ZwtJGykFoOFO7dW5wM8jbFsEUsEEy45hqp9g1BQdnddAoDxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6bce6bf7fb.mp4?token=ANj3FLv45AyzvhmLOW4BWIJZ_AdIUg_bRrKl6L9Cg0IbZuYDyDanyPFMc6E5IBP2midRChthZ3byZeQcyRZNfgHLbLgbn2pmwf2EJ9bmraA9biCrna6akr-Nt9qU7HdI3qdca5vcHpV1wr-FmYVRYgZpQP_2cXQ6flQp-jY3jAjkc8ArEU8GTzwF0RhUPQ20Dv4JHsVSPTSXwxZ8Csm4dtO2AEFm2QCwuyodXTKv-TgfddhKR-2IZ49pG5oCbIXrXDSJkPq2pB0ZwkTfySzRWAeOXgtv5lMNhJPnV2ZwtJGykFoOFO7dW5wM8jbFsEUsEEy45hqp9g1BQdnddAoDxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
صحبت‌های‌فیروزکریمی‌درباره‌مراسم فدراسیون برای استقبال از شاگردان‌قلعه‌نویی: اس چه تقبالی؟ خودِ فدراسیون از این کارش خجالت نمیشکه؟
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24753" target="_blank">📅 16:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24752">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iJrvynN73RxZ90whfEcqnCvbdFkF-4PH5Ga1vaZiyNmOPIexob07UiobgTub6biqNzqNmbBCAnjYi0FanXv3wJHYw8zgin4krgpBqz0ImL4f4M6TZ_KhOtVS7tV_srDHiKekLl5DfMWQ1GPflOIAmLNi-HF38FJ4IBgwh33_nWreTFPENzi0fwtB5lELvUZd-NyfJ0_QgLx9E25Zit9kBodLqsqmdV72ZN9jIqD1dr6dWRljuX4f971f3SyiD2Z3POoU1swO-RsrMhjDnZRpf9TYYeSGdW8CHBNPz2Ce12lHZBYV0E7ALTPwT_em3wZaSJzpfm0JeNdsgDDakTFZ9g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#تکمیلی؛ به احتمال بسیار زیاد بخش رسانه ای باشگاه پرسپولیس فردا پوستر رونمایی از دراگان اسکوچیچ سرمربی‌جدید خود رو منتشر خواهد کرد‌.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24752" target="_blank">📅 16:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24751">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=eBSNV88OE9OqM-oXWSG9nmMrC5HwjI-hLWB6cDKSpaHrNXAoYgef6sBGGisbt7IctlqV_BRZSeALAzt2e0zJ7ietOQgJWa-DbC2aBbf-kEMdYFKp7YTrcqcrwKLF5VK9iBNfmXcsFK962Ojr6z8U0zsDIYrLtxPjsLRRVIZ6jMry_ouCkzdY_1V91gSJ_KcDGn3picwxVfYVL_vxgjXtkWlUtuyIbIyaWc4ESvSg7DYohvMT8sgbaIZ2Ur3YxDdUup-KMiAj_KHI2pvhYVUf2HJ68x6sx5ZCA_i593Ly2riN2N6VdplqNn6KPPXeJJg3ElsKkQHmR86-M5EGCp8wLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdee128ed3.mp4?token=eBSNV88OE9OqM-oXWSG9nmMrC5HwjI-hLWB6cDKSpaHrNXAoYgef6sBGGisbt7IctlqV_BRZSeALAzt2e0zJ7ietOQgJWa-DbC2aBbf-kEMdYFKp7YTrcqcrwKLF5VK9iBNfmXcsFK962Ojr6z8U0zsDIYrLtxPjsLRRVIZ6jMry_ouCkzdY_1V91gSJ_KcDGn3picwxVfYVL_vxgjXtkWlUtuyIbIyaWc4ESvSg7DYohvMT8sgbaIZ2Ur3YxDdUup-KMiAj_KHI2pvhYVUf2HJ68x6sx5ZCA_i593Ly2riN2N6VdplqNn6KPPXeJJg3ElsKkQHmR86-M5EGCp8wLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#نقل‌انتقالات
|شهاب زاهدی مهاجم سابق آویسپا فوکوکا به تیم‌جوهوردارلتعظیم قهرمان فصل گذشته مالزی پیوست تافصل آینده در لیگ نخبگان بازی کند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24751" target="_blank">📅 15:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24750">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
دیگه وقتی سرمربیت اینجوری بهت تعظیم میکنه فقط یه بازیکن ساده نیستی؛ کیلیان دیکتاتور
😂
❤️
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24750" target="_blank">📅 15:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24749">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=LotdGkmv7UJ2soZFctYJv_rBrmVYynGKZergUv0_IhmEKje8wWpbWVhKymXWb3TT0ph6mE92acNYY22a7RvZq_NGrv9Exh5Iv6akTlG2cco8ed3qLbr0AucoXdMGzI1L50pESwpcHSzLa9u1ZA9Z1TGHKSOH6McFzA-7u4xmaEdGO11L0UaL0lLRCtMeoV_WrPluKTIJhJNQqhet2qO5LQ7O_SkjiapjPw1bHl5bpi1nz5dnRRiy992IeuYfpl6ROIMsGNUy8LJdZ5638uXEuXzH1BZ0sbGXpZdA8mF3YQKWYi3upfunTHHzDbccQ1-YFh-zEqSwTPEQCjzKmae5vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b031fa7a0.mp4?token=LotdGkmv7UJ2soZFctYJv_rBrmVYynGKZergUv0_IhmEKje8wWpbWVhKymXWb3TT0ph6mE92acNYY22a7RvZq_NGrv9Exh5Iv6akTlG2cco8ed3qLbr0AucoXdMGzI1L50pESwpcHSzLa9u1ZA9Z1TGHKSOH6McFzA-7u4xmaEdGO11L0UaL0lLRCtMeoV_WrPluKTIJhJNQqhet2qO5LQ7O_SkjiapjPw1bHl5bpi1nz5dnRRiy992IeuYfpl6ROIMsGNUy8LJdZ5638uXEuXzH1BZ0sbGXpZdA8mF3YQKWYi3upfunTHHzDbccQ1-YFh-zEqSwTPEQCjzKmae5vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
یه‌فلش‌بک بزنیم به این صحبت‌های مهدی طارمی بعد از دیدار ایران - ازبکستان در کاپ کافا: اگه تو جام جهانی پنالتی برای‌مابگیرند من نباشم کی میتونه توپ رو گل کنه. جز من هیشکی نمیتونه پنالتی بزنه‌.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24749" target="_blank">📅 14:38 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24748">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ch0vHVPvgqgTSvSe2w1t5yExP2sZvMTd7AMhSzKifXZZd13X8WCCIK1Jz0Ew29LSWEyukrWEHRSVlonk8M2QPV_OqjfZBZ7qPKcoPWk08N2OXGKCMHzjc22NSjC72zFD2uJAEUu90VbW76439dN2gU_7gM9T1xh3wFcjE9Wx-wgog5VG5E4mIM5puiH0R7nK3ZM3A6DtrMVqO6c8cMjrlySo-5K_vcS3bUm3E4j3ainkOgddj2x_Nc4mQdUtzZ7leqprkatyUtc0M_pDPlpN4Cuo9ACkovMWzeSrJaZoQre51cx-WcNJgOWIvXaYiLG-J-9ia9bwzj03y-yNNdb4jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
سرمربی اکوادور که خیلی عکسش از لب گرفتن از همسرش بعد برد جلوی آلمان وایرال شده بود، بعد باخت جلو مکزیک استعفا داد. اونوقت فدراسیون ما برای‌حذف‌از آسون‌ترین گروه مراسم استقبال میزاره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24748" target="_blank">📅 14:13 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24747">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dhxDz0TWYEinoKcmi97nO4j6GZPc36GU1uvXwzZezB5tPAT6e-Ln23bKLtkB5-BoqeXgy4PpbzzYCjRPCNZfiBHcUTM3po0SIirGpv9d4o5-GPWgbPx2IbhX5XOg1PEvumhzAIzzKJ-UplsJWcZJjQ8xWKa7Fw_Nu0NT_SoCflxgu_5s9tubIsDswtq1mQWkjS6YV9q11o9tMbQCOiVkIDU5w8X8anevCjG-EQGi3LDcM_IJG6fnQZ7qCon9J2tTsrbJzG1Y_55QscKuLJqiN0Vz3H1SQzZmIuMwuf1EWGAp7t0sM78qfMfxzdaMJUINKvLfFVgMMmr5SFNJXDgt6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان…</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24747" target="_blank">📅 14:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24746">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mtk7EnYNJSunV1JOC7hkDKAo1wIzOFpoW4DRdYn3aYp9LO4VW5ZabISnYkausBTzkajd-43gmCJNGJ0SL6BLRcTyjt4bmU9xoZeSsW9EcrrFCU4u56mflyDgZEJk83PS0D-V_627qasgMTSju6uO36jkMhn5xrW9dEZG7Fn4UrdOaIKIex5-BlExlT9QY2jSly6Ja-I3TdASM8GNfW9rMsuFwWmzF3GOMzKBfYAN70jGNyw1BO-9_8Mw9JaF53U4joBBh21VQC-S7LVf-QOn-ItYU1-zGxSYHyw4GMxPUG1me04HGM2xPMS0r-7FtT8Zy7Dwwj9MP-MT_MorFu9rbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
به بهانه تمدید قرارداد هنریک میخاریان با اینتر میلان به‌مدت.یک فصل دیگر؛ یادی کنیم از روزی که او به ایران اومد و در تیم صمد خان مرفاوی شرکت کرد اما این سرمربی او رو به دلیل جثه ضعیفش رد کرد. خدا دوسش داشت‌که مرفاوی ردکرد. جالبه بعد از اون اتفاق میختاریان با باشگاه دورتموند بست.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24746" target="_blank">📅 13:53 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24745">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmxd4xAavwwbE-4ub9bSqUT-GjYMdkd4WdpplqMoIsKoR0iflMHmAXAGqlJlKljcrOj_SgaX2T4EbnNGAaflmgq1T_igCnlL4xGLwzN02mlq2jquGxRGXSub9OicYGaGJN2hzgH1q5Dh8kSvHJtI3WHqaC_lpV7D01SNQMdJwlFbs0FjnIry0mF-QJXepr2CUYmoRxP7EXxaQSRLzVASYuEpMshQC-M9Q7g-xcf6g5orf3HbYC1BPnYstX5IHFh98JDpJ-6wpJ_dyikF56A2i0M2CddMroZWJ3N45-e-eh1rZZlSqk4-x3OxZ_eJWfizMiGBAijoCf2P44UD1kFM7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
علیرضا بیرانوند دروازه‌بان تیم تراکتور از شهریور ماه سربازه و احتمالا راهی سربازی خواهد شد.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24745" target="_blank">📅 13:44 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24744">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=fN0tmMouODSCu6gI16LEircLItoDUVv5Pn-agAEk5meWyQ2h-ovYu5rMKmPfohnL3APwrQvjDDS-Bh_ElQn-bW5yptLzgtOFXsN4Kkn9uqBrxs2ZqHjqUN6g9MOZ5GsEg0sPSjykYR0HuR6Hvz4rlRv0iu5x_UOUYzQyvE1nwZfNpm8UvFN9soxSwfmdsLDPeS4PYDOaBbHKwm7MNMVD9jcI3r6Xx8Z_96hnpA9b2mrbFlGz3xSkH4ZgHLKgkYW8zWWOaEvO66V_duVh_CoM7oQor7bH_6XqLmutYPKxyyYr7PLDhZot5U1JniKEXmA7gUI7u6ejHtU9AB3aDm-zcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16504ba5c1.mp4?token=fN0tmMouODSCu6gI16LEircLItoDUVv5Pn-agAEk5meWyQ2h-ovYu5rMKmPfohnL3APwrQvjDDS-Bh_ElQn-bW5yptLzgtOFXsN4Kkn9uqBrxs2ZqHjqUN6g9MOZ5GsEg0sPSjykYR0HuR6Hvz4rlRv0iu5x_UOUYzQyvE1nwZfNpm8UvFN9soxSwfmdsLDPeS4PYDOaBbHKwm7MNMVD9jcI3r6Xx8Z_96hnpA9b2mrbFlGz3xSkH4ZgHLKgkYW8zWWOaEvO66V_duVh_CoM7oQor7bH_6XqLmutYPKxyyYr7PLDhZot5U1JniKEXmA7gUI7u6ejHtU9AB3aDm-zcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
خاویر ارناندس ملقب‌به‌چیچاریتو که در تیمایی چون منچستریونایتد، رئال مادرید، بایرن لورکوزن و وستهام بود، از افتخارات میشه به دو قهرمانی لیگ جزیره، یک قهرمانی سوپر جام انگلیس، قهرمانی در جام باشگاه های جهان و قهرمانی در جام کونکاکاف اشاره کرد، وی به دلیل طلاق از همسرش به شدت از اوج خود دور ماند و دچار افسردگی بسیار شدید شد و در نهایت سن 36 سالگی از فوتبال خدافظی کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.3K · <a href="https://t.me/persiana_Soccer/24744" target="_blank">📅 13:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24743">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tv_suZ8YuS9gnag9QoCvt4h8jfDz-e1ffKf-mn66TPlpXZKni6d404XQezGQsZqgxmo13qSG59VsT_3kQT4eQhkJGcW991zVt4lvfp1KTCxifcOEL-g-c0yG36ZqYIiV6yjzT-Xli94-G0BstM1rNmojjYqBZrgnB2anaegN7AnuF6PVeej0Ykf5Aktq4HqWEESBo-ssmZLL7DJ7LDxFeVFfSMYSzJNA_wwPN9h7S9G6A6CT4jO42cGHu76H9JjBuvR9V3qByyCM8JuYcvKPVj_h5qGK0JjW71TfNgGifpaiCi85USMh9hF_32Ge0cmHkKq_NDXX4hrgqeGDXduJkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
👤
#اختصاصی_پرشیانا #فوری؛باشگاه تراکتور به‌ سید حسین حسینی اعلام کرده مدیر برنامه هایش روتغییر بدهد با او قراردادی 3 ساله امضا خواهد کرد. پرشورها قصد دارند در صورتیکه علیرضا بیرانوند در این تیم نماند با گلر سابق استقلال قرارداد امضا کنند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24743" target="_blank">📅 13:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24742">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IS7jS3uGrFS0bcxFj_U8A3OqQKCYPG0aVZXAARHpdTtVtCCjCiN2IGRl_Y4IEerlvoewneghCsbaLNUpWxxi8SVqMn0Pqpj9_spgJsMHH1haY_F3N_mi8D5d6ixxLf5nSJG8OrCewsV85kI8ngM3T7JyBKomnUSv8u3FQYQY8Gu1lalO_70G9G7dkiTTto1zD0UGgf2Kxq2-NjeNNv9Hmwevz-qdTJCL0fJdyK-FT33ajFwTicRGP37onyLtMLrnZ8tB1-g_URHwYgAbbky2kYLUuEb9PrR-LSe9wvTqKukNW-jszrXuCWmdrZlFv9CqUJD3CYmVF0Q5VGVAp1UqFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
اسماعیل‌ سایبری ستاره مراکش در جام جهانی ۲۰۲۶ و بازیکن‌باشگاه‌پی‌اس‌وی آیندهوون که اکنون در آستانه انتقالی بزرگ به بایرن مونیخ قرار دارد، مسیر همواری را برای رسیدن به این جایگاه پشت سر نگذاشته است؛ او در ۱۴ سالگی به دلیل اضافه وزن و عدم آمادگی فیزیکی با…</div>
<div class="tg-footer">👁️ 50.2K · <a href="https://t.me/persiana_Soccer/24742" target="_blank">📅 12:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24741">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=gPIRBxfQYuJmF3-bM81_YFUVhO3JEzICI_-sYNt78vDSmozruq4REe8ccg1Kspy4NzycQ_bMGgUqWeAvkhkLpsFLN_Eq5FgYZupoQJGZTiDgn8nlbeBEI5V6gYc44pn4_QjMNrp8043dIfpb1cBqaEkcTWmMBlS_cMxdCmDIr_3sO6gWFolhOsui3gLFwIsbFyNOMLRyVD0LCLlagS3UCgcoIodGlyEJo-9zGIBkwKJjFt3WtSRq7EdrDRytzPcG2N6ryII32J8dkfjDvf9fJyCQ1vh7Aa0xWkJ_XUYOoruc8R_zN7G25bcJdswVhNpJcd1pESwXwrL4eDAZ9mr7Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/290b5bc8ca.mp4?token=gPIRBxfQYuJmF3-bM81_YFUVhO3JEzICI_-sYNt78vDSmozruq4REe8ccg1Kspy4NzycQ_bMGgUqWeAvkhkLpsFLN_Eq5FgYZupoQJGZTiDgn8nlbeBEI5V6gYc44pn4_QjMNrp8043dIfpb1cBqaEkcTWmMBlS_cMxdCmDIr_3sO6gWFolhOsui3gLFwIsbFyNOMLRyVD0LCLlagS3UCgcoIodGlyEJo-9zGIBkwKJjFt3WtSRq7EdrDRytzPcG2N6ryII32J8dkfjDvf9fJyCQ1vh7Aa0xWkJ_XUYOoruc8R_zN7G25bcJdswVhNpJcd1pESwXwrL4eDAZ9mr7Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
ته این داستان شد عزت یا آزمایش ژنرال؟
امیر قلعه نویی سرمربی تیم ملی در جمع مردم تیخوانا در زمان خداحافظی: خیلی دستاورد بدست آوردیم، این عزتی بود که خدا بهمون داد؛ وی پس از بازی با مصر گفته بود گویا خدا دارد من را آزمایش میکند.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.9K · <a href="https://t.me/persiana_Soccer/24741" target="_blank">📅 12:50 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24740">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JMzjyypXoseSAlTgHjVlI69mk8M5rVuZHUk-K7taOS4SPpyiNgs_nMY0UzT3JvG_X-tk_ba6TzDflYmRWg0r2HzYoRIaFbCB8e7lrwzmrGNNoJOSVuSeNTUK6zTm-3D8HXvYsSgxK1pgIwDPo43X-LGcShWT_eVYhSy7CVQC5OHQt_eQ6bBLpAmd1Dmu5__5WX4j_7vAObt5A9N60Hr_0zx1jARVq6IONqeVoj8h1Vfsf5CqU_0DwX23AX9VHEsbpfSVrYj-bYvBFV90oVfclT76B6o3pV9tCxANgEl2L1bT4iw0M-lHq2-ohQx0vvE0WrEnHrwXFvW7DvyDY53WXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
🏴󠁧󠁢󠁥󠁮󠁧󠁿
فابریزیو رومانو: ماتئدس فرناندز که علاقه زیادی به پیوستن‌به‌منچستریونایتد داشت در نهایت با عقد قراردادی‌چهارساله به تاتنهام پیوست‌‌ فرناندز بخاطریونایتد پیشنهاد رئال مادرید رو رد کرد اما به یک باره با رقم فوق نجومی سر از تاتنهام دراورد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/persiana_Soccer/24740" target="_blank">📅 12:40 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24739">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dluUhXP7RX1h1k2yKgW46aUPN7ZfkaICVBKalwRRa3cn3YlBsQlxpGEQXAf5macvY_W6BwI7RAm8Qi8wed-9_9hB-zD14JT4MkECD5sfjtpzNDu2mNMECoLSMguBakZdFozzaKbDjjI5WS3S6sN0CDhkGSZB-aF_bjg6T9lMkErU6-c5Q46ixF2Ud8kIyE7Qfkcg-0B6WtcOnQM0I_28qPeRSPB2VgfZzjtlPk4GJgc_WFLLnSyKjENVmehwSvG504jafQJ0V8GLEonPSBnst5r-q636-icf3on027IpCEUfDyPcbQO_pnXDEgClQK1DEDh2QY5uFFGjJnGfB7MG9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
#تقویم
؛ سال 2016 دقیقا در چنین روزی؛
باشگاه منچستر یونایتد با عقد قراردادی آزاد زلاتان ابراهیموویچ رو به‌خدمت‌ گرفت. زلاتان در مصاحبه بعد از عقدقرارداد گفت به‌جرات میتونم بگم که من بهترین‌خرید باشگاه منچستریونایتد خواهم بود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/persiana_Soccer/24739" target="_blank">📅 12:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24738">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U6laiItM6697N9zYEmYroI47EU_QB1nEGhQu4pxWoVbn0D8mJFjMk4nTy_5u0h8nb2if3cKVF5GfEUlQWO9izbk0fWe7bBvAaLrOSabnr_CaDvXCrwhkJRYmuG1jo7-y_oMWR09Hk9OJcBOKjuxvePKP5Lm9I3tEqEvRHFsGQ7p7VHWoyZIgh81BrZt11CuyW1F0yLNwn-Q-YJknwJMkxy2tNS5fYSCvMiUQjzBX4l0mkm2WS5TnFuz1xy5TunjEAjUJZyp3NFkeBI8kWFfV0bwvwWCs4wbtaUp0ZwgG3sGontPOxY_-hBz2CgwbhgJ30LGwWLHv-A4JUFdwSwTaLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🇩🇪
اسکای‌اسپورت:
کلوپ‌ سرمربی‌سابق لیورپول درآستانه عقدقراردادی چهار ساله با فدراسیون فوتبال المان برای پذیرفتن سکان هدایت‌تیم‌ملی‌این کشوره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24738" target="_blank">📅 11:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24737">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NHvl52j0XJpHN988tFWHI4UtPhbpOPkf9C_71MB5Tu4bi1sM0yV0ENsSDf4TgayO-y5WI0xWL91BvJaOSf5a0XChhzm2ltEUqYy_ifUmMyUIjCl0C9keTb-GjjSsJJHZ4yqZnJVaFK-sQ60vfVYiNy5RpvPimTlmSJXnvml1bXlqUMTX-ExzFWyphtb3DSww4hr9G9kvTY1R_C8J9ykzOa7rnDSoeRHVY75PBsww3PXP7htGl9KYFLaxyItEwXFjmciQWfZ3NQRZ9zmJ6FqKBvzyqsVmPeWp_LrZm8fklZbuIcx_RANHjXUze2fEqC03Kw6zADteR-Kd_1pqV7M4gw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
📊
جدول رده بندی بهترین گلزنان تاریخ جام‌ های‌جهانی+جدول بهترین‌گلزنان جام جهانی  2026؛ کیلیان امباپه تنها یک‌گل برای رسیدن به رکورد مسی درجدول بهترین گلزن تاریخ جام جهانی فاصله داره.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/persiana_Soccer/24737" target="_blank">📅 11:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24736">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=RBmQZfGkAOb_0UoyrxsGQ8kHWI7pDy5sHghIL84CyBIXXYu67i3C6_U8DeDwv1LuC1Ekh6bwbOcJQHJ-GptyH3HVw69SGmr6JYQKGwTEpEppmIEmLM5SLtyeHP1ZFpoKJKBfNfWx8ULmtQlQGC0BRRfYH384mjpHg5-RX-Q-XmOHIVjHxvUK9eHSV3NUpqvViP6lru-MADF5cmtum-fauKkEKmlQETB9pxCT9JtBB_WxWMCYbYzmhQ6d7iyUr7UBDBI9n6WR0Yppz8XNosZOlwuUoCAMnzvlQBps3OqeEVlQt_M9X_QLsDxzKFF6osjc0IWWis-Mq-wAbuWalFrFrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc031d7910.mp4?token=RBmQZfGkAOb_0UoyrxsGQ8kHWI7pDy5sHghIL84CyBIXXYu67i3C6_U8DeDwv1LuC1Ekh6bwbOcJQHJ-GptyH3HVw69SGmr6JYQKGwTEpEppmIEmLM5SLtyeHP1ZFpoKJKBfNfWx8ULmtQlQGC0BRRfYH384mjpHg5-RX-Q-XmOHIVjHxvUK9eHSV3NUpqvViP6lru-MADF5cmtum-fauKkEKmlQETB9pxCT9JtBB_WxWMCYbYzmhQ6d7iyUr7UBDBI9n6WR0Yppz8XNosZOlwuUoCAMnzvlQBps3OqeEVlQt_M9X_QLsDxzKFF6osjc0IWWis-Mq-wAbuWalFrFrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه‌جدید آقای‌امیرقلعه‌نویی، سلطان اعتماد به سقف بعد از حذف از جام‌جهانی با یه ادیت عالی.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.3K · <a href="https://t.me/persiana_Soccer/24736" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24735">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=WQFUYI_5L-AyyATME0dRR_oADe2y4XqOBwQrqo6Tagzte6RA0nPUY5lB5ZOMHdje5RfzSGhYWO0KXsM2Ups-cjaF266ICZ5COjh2z_jtcB0VqBf6yda1XjNSN2xWrRrbOc-G7NXgMgwyrS9Ak8IKO3f1FnvLvhvvgF8a7txO3mVuBhaeHNzyXGbD0ONuCs5bca6v7ZMquBaKgWTXDuunT7WA0k5bAMqVO43QK_Nvq_pxr_DbWsaE6W2zSdwKqq9GpdzylxM0VgqcrWVs9AfvkXlPv9Vdi6qYfQTa28p8DaYvgIVpNI_-WOFfxfheFr8FYBFLjXF22xAtG47zpmSz_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fbe8695009.mp4?token=WQFUYI_5L-AyyATME0dRR_oADe2y4XqOBwQrqo6Tagzte6RA0nPUY5lB5ZOMHdje5RfzSGhYWO0KXsM2Ups-cjaF266ICZ5COjh2z_jtcB0VqBf6yda1XjNSN2xWrRrbOc-G7NXgMgwyrS9Ak8IKO3f1FnvLvhvvgF8a7txO3mVuBhaeHNzyXGbD0ONuCs5bca6v7ZMquBaKgWTXDuunT7WA0k5bAMqVO43QK_Nvq_pxr_DbWsaE6W2zSdwKqq9GpdzylxM0VgqcrWVs9AfvkXlPv9Vdi6qYfQTa28p8DaYvgIVpNI_-WOFfxfheFr8FYBFLjXF22xAtG47zpmSz_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👤
منصف مثل سید مهدی رحمتی
؛ ارزیابی حضور هشت ساله کارلوس کی‌روش روی نیمکت تیم ملی.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.4K · <a href="https://t.me/persiana_Soccer/24735" target="_blank">📅 11:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24733">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tOqARjuEkGRqFcf4URYsNUjjre7qAV1Uahmabr05Cs_AsTJJ8bcZaezXZYrSJVEaMAhrXuTySeUp1T8qiUdeqkeTlh8dNKUhrhLcsg61e9ENFDKeQDsmKKbp5Bph_Yu1xyIPgUAx5rqrjmFV1KP0_cErZ7VOVzrV_98EnzF0-38z_t58LLs_2BTUp1Lsfy5QOH5-lYPbuTo1mRGIpEcMC0CuG57FO0EkrxXSnzZ-eGcxjQTTsLXlMkWCkLhR6iNBL7okoky234N9GimSQ3IxYHXGQ2fwhWP1lwzckGTXbtM18j2nhhsNHXAg13w_2V444X9ENThmzeroKm0NiwbeTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
هلدینگ خلیج فارس و باشگاه استقلال برای پرونده بازشدن پنجره نقل و انتقالاتی آبی‌ها روی هم 850 هزار دلار هزینه کرده اند. وکیل ایتالیایی آبی‌ها هم‌امروز ظهر ایمیل جدید به باشگاه فرستاده و گفته شما تموم کارهای‌نقل‌وانتقالاتی‌خودتون روانجام بدید فیفا پنجره نقل‌وانتقالاتی…</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24733" target="_blank">📅 10:29 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24732">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=U_QW6pCGRUw73BZJK23Nx9B4-8aHMpuLtX9QnfbpEei0CWN14T5BKQ0920F9QyfS26tLLL02IRHSDG1wjbiBJ5Ic1K1qOkYteAlk6J7wxnzv3CNNS4je5rxpHP2cFWtgh2T4iSKFf3pivcLlk_21S6ZelV9_Ecn4Lcw63wMbaWNJN2jtrpdwlChD6f6D4yOsvdfKnkvLw7ewZBMS7RmrJGXEujMU04EI0sUcLhvEPvTAlOahmHhKGtmqGbDN0LIRVEYuTHgguiBJIZeVMD-WARvFIq50fvSJz5zxywJ6AbwkZmIgwQt82ZeoJETJ-Gd7qc8pySVutmNDG_nnntR62g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118e0a09b6.mp4?token=U_QW6pCGRUw73BZJK23Nx9B4-8aHMpuLtX9QnfbpEei0CWN14T5BKQ0920F9QyfS26tLLL02IRHSDG1wjbiBJ5Ic1K1qOkYteAlk6J7wxnzv3CNNS4je5rxpHP2cFWtgh2T4iSKFf3pivcLlk_21S6ZelV9_Ecn4Lcw63wMbaWNJN2jtrpdwlChD6f6D4yOsvdfKnkvLw7ewZBMS7RmrJGXEujMU04EI0sUcLhvEPvTAlOahmHhKGtmqGbDN0LIRVEYuTHgguiBJIZeVMD-WARvFIq50fvSJz5zxywJ6AbwkZmIgwQt82ZeoJETJ-Gd7qc8pySVutmNDG_nnntR62g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/persiana_Soccer/24732" target="_blank">📅 10:14 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24731">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=RLqh3e7VxMnHCD_E0ucY6DFhprxhIfIhF1mXVdsRA3o5k4z9MwPjT1P3oEg9T3GCX81JPIdvxhAy4inE8VLNkjVS8vvFZVn4v16xTnMv229iFUdQMZnzUDfCmavqfrMszKpUOelFQsNAflBys3Sy8mB7zrvaHeEaMqhLyNcEZEU5NKojjPaCLVhtxCjHVCW6t_S9q1Ne1YcLHalJVG-Cl711XOZqFjVZmHKV0DUlxdh8U8UJTeDSkgmKew7Ws2akkhNmcIQ1zMZKjDJg3F9JmtsaipdtY7XP0ROv-CzTyN-r4biZ_PD3CcZxSDIHIuraDCrY4R4jK3F7TsY2QV-SNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9a62c2d12.mp4?token=RLqh3e7VxMnHCD_E0ucY6DFhprxhIfIhF1mXVdsRA3o5k4z9MwPjT1P3oEg9T3GCX81JPIdvxhAy4inE8VLNkjVS8vvFZVn4v16xTnMv229iFUdQMZnzUDfCmavqfrMszKpUOelFQsNAflBys3Sy8mB7zrvaHeEaMqhLyNcEZEU5NKojjPaCLVhtxCjHVCW6t_S9q1Ne1YcLHalJVG-Cl711XOZqFjVZmHKV0DUlxdh8U8UJTeDSkgmKew7Ws2akkhNmcIQ1zMZKjDJg3F9JmtsaipdtY7XP0ROv-CzTyN-r4biZ_PD3CcZxSDIHIuraDCrY4R4jK3F7TsY2QV-SNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
#فوری
؛بااعلام‌دولت؛
سه‌شنبه ۱۶ تیر ماه استان تهران تعطیله. همون چیزی که قلعه نویی گفت اتفاق افتاد و یک هفته تعطیل شد. شنبه و یکشنبه و‌ سه شنبه تهران. دوشنبه کل کشور. پنجشنبه مشهد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/persiana_Soccer/24731" target="_blank">📅 09:54 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24730">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TTObRGeYs_JceQOP_H_3vFZVKV3hd_SwOI8-Pnp4aOhMSoke1H2sdqZRy4iXxBwzQ4ZNlXxCXvYQLnLhpQFCRJduwAaUYU9BgMfBJpFfZiSGEoY6up65vLXpdz_LV59GGSuQrLPtOee31sJmyOlXS8rh9XqPpyF4qt4PzQe2i3DWmvcPc4kNHc45x4IUeHt28DiKr-RZPKYU4wVhOegs8xmZdskSwHDv7lSh8OJq4SJ1xrARVzj1lM_-Dr8aMIX6bUkfDyr-FFEqRyu2euLVxR4eaXD8AzReQWEiayrkTR6i3ggHqfg2hYzcKBXMzutuxgYAoy0EP0lJsST9PiEvXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
نمودار مرحله حذفی جام جهانی 2026؛ فرانسهِ دشان حریف پاراگوئه در یک هشتم نهایی جام شد.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.8K · <a href="https://t.me/persiana_Soccer/24730" target="_blank">📅 09:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24729">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gu_yr0DdEPpZBib4GgGJDg-DwGEV_3KifquECIKujgtx9PFU_PXCqTMoayRnkDaxIIO95q_v5s-CjuKO1gGBHCS734NRaBbq6vMNe24iQIXHSGPW-HMpS5homh_j5TaXPeIz_91WZcAXZBTPU5ANTRLmIAUZlKXDysSXuP-EJza7ZLLXti1CSOdt5gXfjZjeAlzVXpwpGkUCpAJ06sLtQsmBuZwES6z4jJGT9r6FMZCglU_0fP0OYC8_WEujJePrghFM75IRKDEI9vqa_vh31rN28D1U6strF7fWUsozHuTJ2aPei5EisUQ4nFxx8NMD_AE4VIZRTQRchcQSkrDCGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی #اختصاصی_پرشیانا؛ اوسمار ویرا برای عقد قرارداد سه ساله با باشگاه تراکتور خواستار مبلغ 5.5 میلیون‌دلار برای‌ خودش و اعضای کادر فنی اش شده. درصورتیکه مدیریت باشگاه تراکتور با این درخواست موافقت کنند اوسمار راهی تبریز میشود.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/persiana_Soccer/24729" target="_blank">📅 09:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24728">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OBJ2F1rQn3bZFzHBBjs02SGIfmdZ4SqJ4tFXy1jCk-VkTbSLDZhOv9CyBP6ujHl3bBEfvoaCxCBCpvWVpJO3KLaPaaik0wdmJ_gf114LutX-zVjdwWo8zM3uqPVzaj5ORcsIDaoPFD0l0GeBReVXnRu0MICMv6BLUQH7RHSNosptaoZLGTzqp3MXQ6AFex4CilgqUuYUuqNWCBWquPcaKpWIAiPzwpM9P6YnmqDn1Rrlr9iXcbvKxmgiIWQNyrYeRo6GaGy7rJ2yV5CoWN1YlK-lQZzyxVYj77SPdwog-qOCaeWluikZqirA5Wv7D0dqjzewf6tiARLssMTA-l898w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
یک شانردهم نهایی جام جهانی؛ خروس ها با درخشش کیلیان امباپه قاطعانه راهی مرحله بعدی شدند. گل‌های این دیدار دیدنی رو مشاهده کنید.
🇸🇪
سوئد
0️⃣
-
3️⃣
فرانسه
🇫🇷
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/persiana_Soccer/24728" target="_blank">📅 02:34 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24727">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vvbsBGu9ZtF1Mm1x9BLVKlBD1oFB27d7HRQ-QAVLnhg647gWndpg0BYQ_lyEBkm3mvvxQb5W6ro-HXecDhu28BDBl_lhjC7w1X6bFBlH5ixP6Kz40oqjsESwgB1lQUKJz-BntESClAA7TUU4K0CjHClUo0NC12uXV4AI_LdXTF8KvWyxMi9koTAvxs7tcWFmkAORlEqqvFIBGSus5ZZvpVSQtUDEJ7imiSfT_pRE1n3T1SPj_Au77-nZYLqP6LSeclmUvjD8Dmdsmsh79lPWgX69Cz2RlVPAae3b0b4v7N6lqeRsuVsVhD_SXhaRXQWxNLkXAkU4cBj56BGXPNVFRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇫🇷
کیلیان امباپه به این شکل به مایکل اولیور داور بازی امشب با نروژ بازوبند کاپیتانیو میده که بره به شوامنی بده؛‌ الحق‌ که لقب دیکتاتورباپه برازنده‌شه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.3K · <a href="https://t.me/persiana_Soccer/24727" target="_blank">📅 02:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24726">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛ از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/persiana_Soccer/24726" target="_blank">📅 02:23 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24723">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=st-lf8NV5izenKyUg4nZwcqngW_GigWoQpYRkK7Q122Jcl8a1R84q759GLZKn_ZUmaA2NX8uOeBBvFt2RaCKNLzFNEeGjIkJVFgSlaquF9TTfsIEocTkcFfdzS2SfZaEgQwrDWU--4779vIA3O6Dj03NxKrZ9EJhHJoSnoTNL0abmow0oyEdMhdlxEYnE6syAskvjLzd6zl6SjhQaDVotCVZa41_vusRcVxGv9GKJ2NGoJZAQDCLKrMWwm3uRCo0o0XXgAu0vwMBqIht-nWDsnyOrPktoXDjoUrIzjlmGIlB3Z7k1-NNY3PecMMwR3OdAnuo1tnjoUqmUO896N3Wew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e80e84f3dd.mp4?token=st-lf8NV5izenKyUg4nZwcqngW_GigWoQpYRkK7Q122Jcl8a1R84q759GLZKn_ZUmaA2NX8uOeBBvFt2RaCKNLzFNEeGjIkJVFgSlaquF9TTfsIEocTkcFfdzS2SfZaEgQwrDWU--4779vIA3O6Dj03NxKrZ9EJhHJoSnoTNL0abmow0oyEdMhdlxEYnE6syAskvjLzd6zl6SjhQaDVotCVZa41_vusRcVxGv9GKJ2NGoJZAQDCLKrMWwm3uRCo0o0XXgAu0vwMBqIht-nWDsnyOrPktoXDjoUrIzjlmGIlB3Z7k1-NNY3PecMMwR3OdAnuo1tnjoUqmUO896N3Wew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇯🇵
اشتباه مرگ‌بار و فاجعه‌بازیکنان‌تیم ژاپن در بازی شب‌گذشته‌مقابل برزیل که باعث حذف این تیم شایسته از جام جهانی شد؛ با گزارش عادل ببینید.
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24723" target="_blank">📅 02:02 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24722">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiMV5C3fno5fsKIzAPOgj6lrkHC1ki9zaopIudgzPPThz0o1uAutRGjBEgQDDIHZM1ZweT2GxwFgjWcJWISRUmOGvKfVmwKEp7UD7TXnJfk-x4yPZ3SEkTZnrjRVX9FyriEsQke3ZDmZkv97e9XwJy6RcrVvNo1gHBesifwMjLKaGs1008NMEDHqH9Gilgmax0SqWngbjpsYJm6b5nnbd2JcL-l8TuYiINc3A2jxzkLLltSboprP6F_rZfg449jJWFsZ7zdCYyXfH86sCDrKDR8ndYYFNyvpaH7HFD2WDFnR9OQIxSSM7xVF7hsLryKkosXTJ-jfchh-Aj2n74jYEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔵
👤
بعداز آسانی؛ منیر الحدادی نیز چراغ سبز نشون داد: تاابتدای هفته‌آینده با خانواده‌ام به تهران برمیگردیم. بااستقلال قرارداد دارم و به آن متعهدم.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 48.1K · <a href="https://t.me/persiana_Soccer/24722" target="_blank">📅 01:52 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24721">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=iUof8gL_QnsZi45G5JAw_uCoh4g5SvRl_RI8kj4xWU3_SDewmEEXUQg9OYiWBoq465nXWVHVi0cF0lm8BR_9lJCRuy_WAgourLxXGwtxM1wiBhFaQtPb1_varQueszVk9BP_32XZn-qs5AYxjM4EgKQUeZ8EET-TyfiACTFPenLjtFbIefSma2eUOStKoxN67_wSGpO0f0yemZ00y1xEz9cr8Yzz_Y9pE0A9LbJ9LvYBYp1jJjHHqZ7Arly3pbnuip4xxgCTH3mma9AEUIYTcavWrrgUhXY6TMdJvfFMZzs1C0mlGWUz9qP-qF3QzaCN0tlje-a8zh0-9msBWnPhXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de066ea2ae.mp4?token=iUof8gL_QnsZi45G5JAw_uCoh4g5SvRl_RI8kj4xWU3_SDewmEEXUQg9OYiWBoq465nXWVHVi0cF0lm8BR_9lJCRuy_WAgourLxXGwtxM1wiBhFaQtPb1_varQueszVk9BP_32XZn-qs5AYxjM4EgKQUeZ8EET-TyfiACTFPenLjtFbIefSma2eUOStKoxN67_wSGpO0f0yemZ00y1xEz9cr8Yzz_Y9pE0A9LbJ9LvYBYp1jJjHHqZ7Arly3pbnuip4xxgCTH3mma9AEUIYTcavWrrgUhXY6TMdJvfFMZzs1C0mlGWUz9qP-qF3QzaCN0tlje-a8zh0-9msBWnPhXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
داستان عجیب ازدواج و جدایی محسن مسلمان ستاره سال‌های نچندان‌دور باشگاه پرسپولیس: دو تا خونه و ۱۱۴سکه‌به‌نیت ۱۱۴ معصوم توهمون سال ۹۶ دادم رفت! دیگه هیجوقت سمت زن گرفتن نمیرم.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/persiana_Soccer/24721" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24720">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LeW9n7ItOpx8Dp4iRT5I5MNhS829lJVKg8TUWwG8r-Bz9KFlwzXYrc3H1RRgoUV380VMBNm88Sx7jT-Zngr7cXL2xktBxwS-ja7k2yICAI2KuKbSWFp462u97z0vEknggB7LtB5r0-bYu5kVYgNuTKg1O7U13r_1OhzpOH3FytmH8nEZmZHFRnO5sA932Eh_lceC_i8aPT7Guc4SQOCISuxvxPdlavxlUZcsuQVqvoJbJhJ0D7uTzmeNGIiy3IpXbKajIaxV024tqeUJxGh3P5upXOJ9Aw83mdeGaYLdIGSbltBlQAIxeOMATTe8qrcaNOdH7ojKQjqVxhz-mb2kyw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇩🇪
🏴󠁧󠁢󠁥󠁮󠁧󠁿
نشریه بیلد: هری کین اگه با بایرن مونیخ قراردادش رو تمدید نکنه مقصد بعدی او قطعا بارسا خواهد بود اما الان هدف اصلی بارسا جذب آلوارز و هدف کین تمدید قراردادش با باواریایی‌هاست.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24720" target="_blank">📅 01:42 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24718">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JO26k1Mbrta_YLUWUL-q5g54A9pUjt8DrwfmdktzB3KUX_tQUi_6_OWejfAqAWJ2PQ18xotKAMoXFFLHO7co_xY1mAwwuFdG8gOeF9PumRqL6obEcU7hYCg_0MQtO0weorU6adZiPZGO1MUpLNoIVfkoKVTHgrnt-RWCElt52Xdgpk9vzkLuoT7WIWcPIcbCs_pA-x3YJvp4MTEfVvR1KMO7FUGCW1EAk1kh5mQ3yf0o3thSfzAU6GtFRAzwZegwdg2MajUUQhcDIWthYAvn1biJbhC5dCO9G2nuYI6GP-tJFmqziYq2Y-pb0YkNkrGOioqxh7DLds16iy4H6jrgpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
👤
نشریهESPN
: علیرضا فغانی باعملکرد فوق العاده خود در رقابت های جام جهانی به اصلی ترین گزینه فیفا برای‌‌قضاوت بازی فینال جام تبدیل شده.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.9K · <a href="https://t.me/persiana_Soccer/24718" target="_blank">📅 01:24 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24717">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nnMjiejQtOE_37x9GC6ufQC73tJE9G_7Z7zTddtyyd4PGqv2QxHldPfIV3QeP8oO_K9v8AFfkj5hGKj4E0Np-1u4WKfxQSpzmrMHt5ulhVnD3Ne5eV7mEqA-l50N7cPL8vFTH0IxxJY4r5K5eTFnYyO4FBZefsUMwyeOCYLgH4LPxkDcu7swKG6r_X8MNYK6e9-Ir_oir32alNSVwkX-US8vGz4eDfmmXMddL2VGS8v09pj-nEGa2BSYGrdDxEFcGzkEO7G7KQU8fbTgG697Ph6KB2Lfub8Oa7pLPR5M2WwMiTzGPdNuICVaXsqaGNMWa_YDr8EUQ5lxxYLeTr4jTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.8K · <a href="https://t.me/persiana_Soccer/24717" target="_blank">📅 01:08 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24715">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/luFvioQp-IOcSYeBOoRJGYmvqvO0ErfHTzR9FZJmlAe-y-sExlGlvecBl04fhNEGvqemC3iS1lOkYDp9ow5TEqpFlyV9AflzbL1HHTm_KRY1Td3Whu3_kBWzF1p8EEnwxrqS0mF1eaV5XdH1eAH2ONt5VFbuvfq-swhWFCFA8RjoO5IzHY-Gl5uNxe9cC55ZSCTsNgf0kLsS4uJea09oZpouhx4NIlLZ8KmcekRZIPa-YqbxvekiP-IcW4Wn6lYXXtUZhfDanbVuQjm2HvNMHpKAz8gZVNWonVoG-QAtc68LL2U6MZKanv7HH6w3rCKWYr_bvJ_KY8R5HH0aKNeggA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
جیانی‌اینفانتینو رئیس‌فیفا تو دوهفته گذشته 24 مسابقه رو تو جام‌‌جهانی از نزدیک نگاه کرد و بیش از 50 هزار کیلومتر رو در یک جت خصوصی گذروند.
‼️
براساس‌برآوردهای بی بی سی، تاثیر آب و هوایی سفر جت اینفانتینو در این دو هفته با انتشار سالانه گازهای گلخانه ای حدود…</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24715" target="_blank">📅 01:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24714">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lGuYaqsDuLvdDxVvPoBP_tYJCkWPc7UlKRepd0TMvpj4u3G4Wbiq2GmnBJP8d6KAY0Bii2m0MSTR1djJFM9ovvA1x5zTgAKgdWXea4IyVNSCAkv2f8j9VpPUf6BCgBfz1G2Uu73Y5j94bZ_IO6lVMkhD-VzN_eWI1j-dnUpJrDfl6oAZBHvtTFVgHhNa9ZT6v0RMmf8NNe3kYtRQGImAd6rN1LVgVAYFX4BUYQIQJ3Q6ZMx1hr7cBfhcVQtSl1oHh2JC_-qqebKgkA8KXu3h2O0taadTvaOqXaiRNHjbiacfKc423a07APo01zI3Vqeh55Z5GKYqXL9SY2IcsoxS4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
‏این‌چجوری‌هرروزکل‌بازیارومیبینه‌اصلا میخوابه چیزی میخوره؟ چجوری به‌این‌سرعت جابجا میشه؟ منی‌که‌میدونم از اینفانتینو دو تا هست ولی نمیتونم ثابت کنم‌. مگه‌میشه‌به‌این سرعت استادیوما رو بره.
🔘
@Persiana_Pluss</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24714" target="_blank">📅 00:43 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24713">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I6wX22yxnlDxkBR3Mu8xvTVmdFsHMKmWh5bTKLff-0oGladRKIrjDEq7jtc6xFqklhbbABtPGXHojV7IyIe-wc7bkP593Yu-BOn9gY525W4dR-lz8SvSaJo1ayGe5ruvxcJyjDe_HeKMFE8jVMSjgmoEIVsmWnFCKkxosBDn9glEWZNR2CQBlcsmwtGOJktfSUh2bNzpF472btKC0cjTgwN7N0FU6KlE_Hf1cpqu2NEYxQhX0ZsqTQHuOMUxZrDacsftvnfy-btwoklrKNhluCySCcD4VC_F3ruk2hSMAnnaErC1GozVaCxcEQNeSetANQHwIydrky-vmhN-Ud-6_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔵
طبق آخرین اخبار دریافتی رسانه پرشیانا؛ اگراتفاق خاصی رخ‌ندهد گابریل پین مربی ایتالیایی سابق تیم ملی ایتالیا با عقد قرار دادی 1+1 ساله به جمع آبی پوشان پایتخت باز خواهد گشت. توافقات نهایی بین طرفین در ساعات گذشته انجام شده و با دریافت پیش پرداختی قرارداد…</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/persiana_Soccer/24713" target="_blank">📅 00:16 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24712">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lc5BLqPPct0hTXoXV5KLQIQdQbzzS-HhgFuTgU0IR-XohyPMZTMDgu5PdPwaql3GE38QrpPh6ZnQB3CRLe5LDxWISnvnx2w2b9Ww9DJ_Z2vlD_zrgETliy3X8Z0UZP7x4VIt_YnUEWhvSsHxeGF4HtrJuzt5FxzSC8Mrr458IUGVRSegTcxUshqDbXVYF26m6f-avzPj2GUsGByAj4Nr9mBX5nFjN9-9vB-8FxpxYtSw8hHs-FA3wxbeCcnTnhHxwLQv0zW-KMzX2ug0qL7pls9c1PyWO6sVi1fPxbKG3cd1EQ3sRm1Cv2OQKxBPSyrw2FCRQuKR7iUfEZgjtHtXgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔴
#تکمیلی؛ باشگاه پرسپولیس در قراردادش با خداداد عزیزی بند پاداش آسیایی 12 میلیارد تومانی گنجانده بود که بعد از اینکه سرخپوشان از صعود به مرحله گروهی سطح دو آسیا جاموندند عزیزی نیز به باتوجه به پیشنهاد بهتر زنوزی در تراکتور موند.
🔵
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/persiana_Soccer/24712" target="_blank">📅 00:03 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24710">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wy5LVA4A_BaBiSYZQebJ1s9n2-Wg_-M3fkVzWMlnLSbu6aNNmrIKe44e7v6IKKiS80kAGJPz_ip-iqOPyqWOuoC6IjabeEbHKWtkbKJUnrTKMrXsy3VA_7matpWXi7zgVGXYSZ0htFTHB1o6vuG4VYSgVGzxnzu1d4wnoBRma4Ef_NcJMbgAMCGsbMCI1nafLwM0XxqbNsJEPpXtl_wZEdpusviv2JhMAzrqNOt2K-wlw_4TYmDWD5a7oXurJZ0cwLQ7l6c4ebTXcQlsJiWUQa2dYVgC9_wbAwD-Jmej3eDMdOF-CJUwKCA9qu03j76DHpBHY8ZwF0gTaDTHasyovw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
برنامه‌‌‌دیدارها‌ی‌‌امروز؛
از مصاف سه‌شیرها مقابل کنگو تا دوئل جذاب یاران امباپه
🆚
گیوکرش
🔥
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/persiana_Soccer/24710" target="_blank">📅 23:43 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24709">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d0XUZTQXpPcsImLvKVS7yMhEdegJO_49xH_JFFoEEtLUv6qERcNSmaXIBWiJey4g_cPJVIVf2noWvTXgCqFSaTMf7aMRxcujbxDhmmOn6r6VtJWzjVaSvCF08Rvj5qBG-RcqvW6rmE2ddqPXsNWNKv8svrj5spaRq4WjsoABR628yPyff_akNrYDwzMzRqMbT8NlfqLBc5TMO9TADngyA57Vij1B9SH6Fslcgiy9ptcaForcXXxyexu2TanStOKYWofiWJpJjtqEtP3xdsq0MbyPXU5jiC_obwt59E_9VY6hQaxQ8D2xAKWq_0EL1pE2e71ygBS1gLaa783WVtsX4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
نتایج دیدارهای دیروز؛
از وداع زودهنگام هلند و آلمان با جام‌جهانی تا برتری بزرگ نروژ با گلزنی هالند
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.7K · <a href="https://t.me/persiana_Soccer/24709" target="_blank">📅 23:42 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24708">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ociXAj1iYoOGNkxR1lyLNNOZN4hqa6bXy0298qZinbxTv-lBjf_LBfHcecccsSP-tN4EhUNLH8wV3Yqf0BAMGTYq5IkEQqwgFU3ivGhdiHMyeKdU_mwZD7hKjTYeLosV0CjZvL6Y4KcZCGPX7lOPAJh2GzUZGT0W24xrExrduRyqj6VgzpBTmQ0kLx-cxPtvy4Kf6SdmmSPtoln8phzkepoCqub_QHafKewWgZURD-qk8NsaZ4HiwvPh3STNSuMIgyev9qjByYUcuGdceSNGmdzvutlSO91iO2iDGfj1pLURZGPBTFNyZIaooLpUsnPanKfl8l8YDjOsvfnPitvfBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🇪🇸
مقایسه جذاب عملکرد بردلی بارکولا و لامین یامال دوستاره‌پاریسن‌ژرمن
🆚
بارسلونا در کل دوران حرفه‌ایشون؛ بارکولا بسیار علاقمنده که بعد از رقابت های جام جهانی از PSG جدا و راهی بارسا بشه.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 48.4K · <a href="https://t.me/persiana_Soccer/24708" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24707">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BEgF0LBQRZTf0YSiBn_i0YCeOHH6GMlIwxp7Y9NJTNWEral4BGhrvEdEdTGRjU97yZ1t28BQZD-bziYCt9mK6Zjh_rUp1SzMuZVCZXMDqYuETQs4x6Hc498GOtXSqEB3UTycVrwGWY3BUg9QiTWEoi-57Q9YEzRz7jwIbcoiWUhl5kp93pJKr_5OISW5JMvfTX7oslirttFLQ_bQs1BA-KTJPeWOjHqeyoGmy5zBKk4P_s0f3OEZucR7YzzprOf-5n-awRX56b2dsfMojk5VNuKapMpS-Mx0ZzT-2imiJ5iGT-qn8-7auciSrAKnYli4NilzQowwOMvrJRMJWb_6uA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
نروژ باگل دقیقه 86 هالند ساحل‌عاج‌رو شکست داد و حریف برزیل در یک هشتم جام جهانی شد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 47.2K · <a href="https://t.me/persiana_Soccer/24707" target="_blank">📅 23:37 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24703">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rOmL3Vs9DTaJItkWgyimr3wVn4pmXF1TVDQ0hNwC2pAgmjQkitZCPO355qeEcvepTRMVINQn47KRqg9gtgi3P81R47x9XI5BsZWSTAOv4b33aTmI6l2I8KCph1cbpZwQ-pJaHZdVSSiDBj1aq0MEs6bBUJ6gZ9DDpHGyVrNVjcWE443o7zsQiAq-SxLDcW6ZKuoiK7Zv8hBPM6NcWyi9voZRcjvjPjvqxUwjfLr5-snt5IXAQNJuqZo_reFrOYNB9AV3T1rOS3N4kDYu4lAg6kqEk5O5JIwxKYalM7SnqvQxBXV-t7O_x9pLLZYq68lA-OYsZpDLbzmDjuEwb7Nn5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aB4kujcMJl_9h8fGkBFRHmyt0R730t0gBfj1yLKBFpYWdCCkfXE5MnG4-FRUZkEFMsfrhbxr4TYb7eloYZI-nNrQBT0UjL57WGv6olPAZ_hk3oEJZyGndPQdNoI7v01KNexOtf_TGpvuRv6BVg4UAr-PQM9k86y9qP3yBzp9Jf4oLepKQoRCO4PwrG2pnbXAgtmdRlGwEWrwgvTYB7y_e-Tao9loC-VP8Nr6T1xIGHiWV47ettn0f1U7hCJBoqLonrWG3AkFjZQMQUasp46BkF2_hvWw-V7WYIgoZhzitEE9bOZvPdnJWeOgDj6kbQRfyVPPJDz6xQzTc2sU4h0gdw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">✅
برنامه‌هفته‌اول لالیگا و الکلاسیکوهای رفت و برگشت پس از انجام قرعه‌کشی فصل جدی
د
‼️
دیدار رفت ال‌کلاسیکو:‌ یکشنبه 3 آبان 1405 در نوکمپ؛ دیدار برگشت ال‌کلاسیکو:‌ یکشنبه 19 اردیبهشت ماه 1406 در ورزشگاه برنابئو
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/persiana_Soccer/24703" target="_blank">📅 23:13 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24702">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GU1W2h_NVHpTNCj72F76-VAHRyEAWug_YnuLcUYPNc66Cmnd7Wk7kOt6ce-8dSJjrpaSlZ8N2ytAyWcOh1UTjG5JkhtMLGSk0w0MI4u9jBesefdKMylSX5hnSuzHXdsJtd5OjxmRrWUV3xIvFTl43Cq34q-IS6AX3GPWIAyf6MUQC6_DTFXUywdln2g8_rz2adzlBUf5GwlBixoRbJJhVlNLE0rm0SxgfJ8zooOVZf0FTmrzOhqnPoFHlWwxZgh0Emiovni7LcVYq8SYoVoEe21kUuLNz1X84pTk-v8IBNGK_9_7xO2L5PSSyLMMy_9GhlvahaVFtGRf4Csd5l_u9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✅
طبق‌اخباردریافتی پرشیانا؛ باشگاه پرسپولیس تا پایان‌هفته‌از دراگان اسکوچیچ، مهدی تیکدری و کسری طاهری سه خرید جدید خود رونمایی خواهد کرد.
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 50.6K · <a href="https://t.me/persiana_Soccer/24702" target="_blank">📅 22:59 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-24701">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UZ_6s4AsAg6E6LHrZydKf85nW9vWKvabXLddUqHmEmFUaMenF3eHiNw1JBIu2iZ5D3ENva4Dhw5z59IfXJVxpnIqsG480bvrwyr9rdb9Jk6Yfem2mxEE4YdKGfiCBIJJ6QwVbsNgpc2kP7b7RTwFUa2Q49zpyo3rvfBmzvuevIWhMR7J3kjqJofludCFn6rkxERh6iaO0zxJDITDCF7zlofHf1m7i3V40nzIRU_iIRy7ub_4ysY042DiGnOib806qClAMpnYOVCxSuVx7sNjUUWtDW6kXIqfazNk1oaYYFghdSozWRgLV4-WnCxxA2MIDLGrT27qU3qqJbM7DbcEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تااینجای‌جام‌جهانی 2026؛ خطرناک‌ترین چیز نه پنالتی بوده، نه وار فقط و فقط یه عکس یادگاری!
⚪️
@Persiana_Soccer</div>
<div class="tg-footer">👁️ 53.6K · <a href="https://t.me/persiana_Soccer/24701" target="_blank">📅 22:44 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
