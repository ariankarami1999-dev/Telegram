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
<img src="https://cdn4.telesco.pe/file/IWHAaj3IEyrc_g0vDCpWsXrLzZQhh0k3minhXvet2PvviYRgx54vskBF2_K2Xq8i875v2MU3TqiD8Y-aWL_AP2j3oGvgCJqCOUvzvTzhZ_aMCrtxHeZoJl2fcTEqzhyONskm5GMv6lA76aVpUGCoQ3zt774O6VInSs_pVduSX9suArLQ3UYHmjGoXD9OggQTx6HPeC92Oglt5AqVZWm9EUipo5alxnnLITmtlOdn8BlecLNWf7-NnlPHd9H5cwPvJV0XHbjKzaV-ozTJZmZnLYZkiToRtz3odqB3wekLc7b1OI_8SnE9HKaKkPSvHl1S1iiBUXfVCBFR3HH6YsWhRg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 64.1K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-30 08:31:18</div>
<hr>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/moWg_UMfYn_-p3qEgdHOKFb1FpzLlZXnLKG9GV-qNGUeAAlctAjKtPzrZnJexLjb9IZXF43Spj21oMD82vRhIuG8npvZkuFeMruMdtYZJjcUihc304b-WmcGUb4PEjzhhKu5StX9HRcbdsoGsJpeTk3ON0O4neh5I3HNNsAxd3wg7jxOkKGI6rAhbs-ZTLVZXbCHxqahKCGEd8SMUuKp2XQCPhTPprkgNm79LofgisCFMB2xjZ1KtUz3lfkO2dmeqDiAk4Srb8kLE_zXHiI84T_9vtGyLmVyMRQIf44lOrkqeaD-2-ndMMA50QQOBNrir8D_C2RKGP4V0z0qPChrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Uo1tNOZB6c-MoQ3XQMu7mUtgF-BQk8BMsZvsHZp8EYCDv_zpKIBZeahvjQdEf4RgZ7zIoEWNj6nP_D0RHGtp-tLA8u8D9Gf_tAf-LuisnUl33KjquBkubl4EAybwzC7_v1V7ZDU3sp2DkwBmL7BWsm6XZzbeGe5Uy_cRNia0ZJjQspMSAE-y9Ed5NMYNYgxoWd4sVy2HvYEOLEfidb2RzHubd1Ck58F7e7MZWMXLx5Vo7qkqzwYwcuH7OAz66P371ddS8pQihuvL2xWKQTXIG7eOpEPEvPM3TWGQLxLLxc4R9w6GsON6xoFqJ5H-Gz0dtblGYamEKuPrYk1X_EoLQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rZRyw0iU2VFhAMFp2m_a_3-SSRdkA5AV6S9loQG-kbaiVi-QUqeNWTNoKr-73zhFnVkbPziBP0BhMVM2vKCDW3mQCrQXqTfmpsLgGbwe6SasjzfbJnHeTs-Js-HabNbNdtPkgmCTWxVUnheyTDAwU1bCKHsYKQRN4sOmc4-zk1gb7-CtNb6emhLO56nMPzyzTFR8K_Hwz0gqed5RLJq6-x1-WHzgk_f6aIZtAJgHTWqIkeUZdzFGywjdZnx_LiPulKoWNujHM_5uk1BiS_UbA_D_4_8mxtipg82w8KcpIN3Y0ywAF7IML_SX3GItVibRpNLxwyUimP2udxbgv4xtng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KlPhwJlLNIWfIgbpbp24avJ4W7ZhTarLQC4zObmgYTGAYDF5NZQ1Qs9TgedJnl9RPvf1JfQYv4qgn7U5RbQhixB1XDzX3DMHodY0sfqdfPxyRLNSrEcuHt8sQwZNOmRtTKJwKR6LnINP89kkBKmAEalUOutd3LNi6SAFjoKwvPCZnOQzUypE5FcXGy1oSkEwErALx1jDkxIk9CyMvMg8aFy2f5dvHYqrpQlTE8DiNcNbCLdmnwkxTTL5yLvEuafpUaw1JyF32K8QzvV_Tnbzch2-1xNlFUhE4AP3IvOEi69R4u7oDekmr6NqV_fxIKYWY-12J2Yq0kULKYIoCAX-eA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 9.56K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/wA3w1V-njwjgAovl4pImqJ_jNE--G398_rO0o4aFBJ92wQDI-5SYfpCgm5nGqQpxVRYzR7dede-LL5gk-RyI2bXmAgkDvyENKoyon2UesjVKmSSFio8rw9svH0RlkLbjOwStCGdcV9AJXEqZdyYqWXSGq3UsmTH7u_7u0dES4ALmy9dRCV6W0F6xbU3KABXM-wfPBaR4U-4IDMFxdItGWpQqf5U0ueFNTO9KTD0i2fqHfP1tdfDcC8QiWBalZ7TVWREQw9_TJpEw6xF0ro0FlY8TSIOi523ik7-_aWMmPr3piUl-ZEGBtS2EGTu4n4jeTAihluI6hhIERp5P5E0zBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BnJ149wgYQqbxpY6yLqlPLzmFx_lyekTaUzSvXxIzaY4QWZp_f3jUkto_vaNAF1uz4Y-WeJF44iu8sebMCubQBrTOC01rfKpvdmCl10GOozHRxSNyl9eISyz-qSeiXlzzCUjtt6euhUOFZ2k3Attae8RlAM7dPt7qwBHnkqKdTzmhskFtChOouRWiH0yifuSgwXmPGuNa02qPazrSE6YwSJ5Xh5aTVe8z8Frb5D2LJLVmjKVam0vGr3PbF7P10A2o74hrf1eegu1t5lFM7Pmws_skJTGlrhQI_FSCLwi1OCAH0Wfjv2KLKyhbPL4fgTZRZF4mPkGq4TA6em2FRDg4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qoxNTgkjnPbTeKICysX0LPJfGwCHOW2iD3f_ebigOk8hrDOCOe_pgoUKN5Z7ymmMG4T-n6LlsmZxzd3Dxjemem9kbkM5FVHuwlaqWnZrrOZPOgoIBNk1lHAFKtR6zOarxvOTKcW3mmqPCr847T0Gt43n5Gp3z63uMR-8PMt0H1b8nM_Jx7qgbcqBta5XPLk4J1uRmrtwTVqKdYKmjqGJOFiKH7l3Mb-uKu7nPyZooKu2l5-d6oDJvkOmsLrYdQ9TNwwpBPbffH_WB_gEv7FoWvrRcFpnTIbRnCOPe-XAch6zjiMS2bDz28yWAsP-k1WQ8CAVivVdPM6MvHyCpdYhew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XLpCuZuxFKWSCjEzu71wUyxUkFO7HGadK715-NzgRYYcuWLAUHMyf949g0khScg08-wPcf7Y4FH2pJWDygdd_iEIhWIlTlJL0jNfTfEqbP_ZN8xNfKY2Gv45BLZm7iHOmlAbjissBmNo6h2CMZLUb0FMOrYdB1Mlh0qPuqmY_s2njlHgAsEZ_wH2DSHkoW7KSAdr3IPBuPZInCIoP8b9e8UqzBCka02TstPMlDgwwd7FxRi-nBWfYwFwFAZjTMKOx7vI9NVWCGOfVXFtmMTLhswa9i2PBMOH5nKWwFOTzAWqiZFuDb2_twIOQ9VhGNrs1DIThDbZhCPUiGn8J6qa9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lqJXr9vcL76eKAEuLaYQRTPhAqKSlS7_l2zUrAXZSd_-Wh9rsx_Lx8aCaPm8du5yUYZCzMXTt-iyeM2ROnc2_1XpT-iX5kX9w3qdAOy4RPMXhG5hzOlDjJl3Z3Y3mTCGfy1lF-f6JQjpqzTLHqm6tT0rN2nd7rX5HLFqWgRprLS-00tcFwPUkZ_AGM6s0SFdXfPEUbHIlWJUWxJTIdnfuXXDfrAXBmfZ1ht22SCFWcrFwYUGBzSa1qx0DhhzzaW4K2DlbScR_spN0hk7cpR9Kiw7VMDh43FdiALWVWhP-cal8VX1Sf_ooQuNwZ-E1Yw9sROfSz8guJV40JT88v2uJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O2BI1w-_mSf3bgQku3PuIT_AXybxbQ7r3qjNUxlZe2yMsQnPZAM7o7Fmvh1S1lXcXhXt711b-8dKwWfHNTsiNA-ES-SBaKpHwAMxXFl0PkYrIZdTCWAAQrNsTxWuFk7q2dXcOn3EppJ01KFoRbahXBzUJTjt7tyc2jaX9fYn2PoZG1NNa5PA_9Q2ZqAmqy_EU_2UKgB98p7PWPBkvg2_iBX90WQgQGT4sBjxzG7SUbdz9aYlzUn6QAFIzbZid5zKCDbE8jDHt5EgSapRlkTGT--mmL46vUlkzms-DGtvvC8ViWH1H5v3ZU665OD4RQVJPkALOMkSYWEu3qZHOTWs_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XHkLlf_-sPzrgDlYGDmykfRpNfDXG7sX3FbvzRQ6ZCDImIxERkNISvtXWHT7ZQOD2lk0TmBSTjCU6xA67lSCUxElZlwRywWsruQwBzaH8TQaTE-Wb2CZo9HaWhDuXA05u-bZlmotLAApfdwtmvNchowhWhuDjlRN8QiVLnFdOE-9Eui2MH0i4MdZT6-Blb6qXK9mdubCuLW-NS8cbQmZBMuXJPXQoPv82Os-358FrwjO1jMgdwxWr3Yj4od-8OIXhfJT1LB9pejA5wfWRocHNL_V5ASqrH3Cjrj7pW5D0bMqRvA6uty6rE87UC5zsSv-8hpWiqkf3sIbai1iykBe1w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 9.71K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FPAo7c7545wDSYEEG-CSEohlqWOlog21qPHBA0faen9s6xcM6AHrLE8m9TedT4mnBHx2j4HmJYQ7C6jMddtbiQQukWK3KIXrPC00B-cVFaUtBfEM7_oCYPuKS6ruvZFTLky0rVk000i71cfFhUT879pb9FIjZFfJQ6HUjDhUr68hoPawPjPQ1Tp0Oo026Ej7ZTCxiElw_M9LHVl6rUklvvM8oBUF4H5pStCOEe2JTvshrzU8SzdzETKBx-sYf7AdfkzxxJi2EquYYlIv5VF6LZgtVbCq05VUHMDyNnQYMbwucDlE_5-PCVsHKX5WcL5nCu_IHj0NYS85l6UJAcsR5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6617">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Up26RLvC1n2_8ROhyPYNkkV5AvgPo3n7fzGtW2x-zX5hwuHKxXnTpup3oHLseEQIPRxco-ij9hmmrgFq9UB7lZMel7kOtQZB-ld4Q3SYLBT9lWiuHz8HJhi0-T_EQYQALOQ1-wVxPag-H-W97r3jFjSYiKU9cW61ijmOoih1rgpw8xvN36lh-S7LU2tufIoXcxFb0Q20rB_CYq0iMNVg2DLHSqhdJXKkZhw6RN6ef61AO87gYbvDLshFvjGtdfj859hEY24pdSlx439doL_3czm0bsxHVSKLWw9_30mzYA9YT8sZoakOKhr9CA7saiIlPzL1kmDqjSp8r-_x1b12kw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند  «مصدق علیه دیکتاتوری شاه بود و شاه علیه او کودتا کرد.»  ولی یه سوال! قبل از اینکه شاه حکم عزل مصدق رو صادر کنه،  چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟  بله! یکی…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/farahmand_alipour/6617" target="_blank">📅 15:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6616">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXACtl6XZUnZfrfau7IoXcMUSPoTYjnQnrUXHXG0Z31rzqo9n6Sqp1hZYydTCDjHdzJqzVdGMc6Omy3mZs-g3PJLOAx0evGxFw2qhd3QAlTtFdtrzZDLAF3vFnibC-MV1VGtikCmSHL-K0VG2--8Xv0EgLSNBffZA3b_0BsSykbvdHERuSzFv5QlYZCwmycjx2GhYCF5YRgqkdd-5CXrpOm-CfpdAuhC9ldJbk4_2_0kT4qbpkNR0qpxjEf4GDoRLOq0IJtUryhfHrToJWA7WhylGQjl2dhD_2p6MU353qTfJub1obGkOFzPkPzDjTpUMK691w_otXlGQQaYMvqA3w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای ده‌ها سال به ما گفتند
«مصدق علیه دیکتاتوری شاه بود
و شاه علیه او کودتا کرد.»
ولی یه سوال! قبل از اینکه شاه حکم
عزل مصدق رو صادر کنه،
چه کسانی نسبت به «خطر بازگشت دیکتاتوری در ایران » هشدار می‌دادند
و می‌گفتند «مصدق به دنبال دیکتاتوری است»؟
بله! یکی از آنها «حسین مکی» بود!
او نماینده ویژه مصدق در خلع ید انگلیس
در صنعت نفت ایران بود! به او «مرد پولادین» دولت مصدق می‌گفتند
به او «سردار ملی» می‌گفتند!
او دست راست مصدق بود! او مسئول اجرایی  ملی کردن صنعت نفت بود!
اما علیه مصدق شد! چرا؟؟ چه شد؟؟</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6616" target="_blank">📅 15:37 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6615">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UW6my_cp7Rxy9PDQMmz2LMl_FJEt1iAEvv5jyok3YFmSohY8zfCrgxdHRuZqN-OYu35hONRD4fUy3bDXE7tiIpbeLWVwhNiR-yIaOFqaaCuVdScGna0vv0SaEAJA0vryeB3-aPiYl17wyp61x25-Ua56j4QhfcXC8dBUyjki1ZebdHqfzb0H17sp0al36kzpTbtf5aQZhXx5rVzv3VXZ1C6QjznXhtejN4I4Gl9ttVR8cpIVW66i-FV_QMYwnannMMcnkeNdsZtmM18Y-ag5g9u5w18T6TZJ2T8sEylNeLrOfkACgjBAr5sOpKrg458WIWIQVslPwnxLo7AxWl_-Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پس از حمله موشکی ساعتی پیش
جمهوری اسلامی به امارات :
وزیر امور خارجه امارات با صدور بیانیه‌ای اعلام کرد که تمام معاملات تجاری
و مالی امارات با جمهوری اسلامی
متوقف شده است.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6615" target="_blank">📅 00:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6614">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q5-SdCeCDaPg0kroiH7J1iGfOVuLC5DlLoOv1qVsSXZb9wvaHDInozYQpEc29gmixf7QGA3L3nmhxsIs6cxF2DRnmQs3OCtiN3Jyy-IPIdBpzs7szXK3ZZTUdjfkf1GUoZdXGfL-mDC1eqqMGaZiNlflSLuQBz7W2VWr0osSacQp0LgBJgPXRCUgmM7sffi1zd-dwWweM7gh-8BPgVoePTmFN28IX3C6y51pF28g33I9mUtYH1_w0dMARq4kXky5wXnHsJWlBliBWLe4_qyqpM0V4-vKC3Vd5CUGow75o49dWJ-DyTRQ-_ONtNUXTDS_1BS6XQiU2l5VaO7qSLBuPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخشی از درگیری‌های خرداد ۱۳۶۰  بین حامیان خمینی و ملی‌گراها، در واقع ادامه درگیری بین مصدق و نواب صفوی بود.  هر دو گروهی که ضد شاه بودند هم در سال ۳۲ به جان هم افتادند هم در سال ۱۳۶۰</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/farahmand_alipour/6614" target="_blank">📅 19:34 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6612">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/K5dB9AkoScs3TBBlGrPQ_2DDHXBVwnqCPW0-YyQSzqGLWVTTq783sxmVq-_DpJENqVfoce7tlquwiTyStQcaWlGvFqPx0HgO2OPm8LTRJW9vjtgS0-rQ7lklOAR78SypVDaYz7wlSoLHdGK8MjxE6tZdeKFAxtEILCdmJYB8v_nSWiYy9BDfDyTb-0dv7Gi6_hS9ZnvW6Z0V5RXmx74NSLZnHbYjp1mpfiRZf_Immgu3xjaT78s4ZvEEaRDz_dTfWTfGOo0GdYLforZMx8clNUur_cjI-cU9jGUno2n8vw3Pd6qG7JEZdnKTaDsfPvRcw-r8eLTS8qql3FkkIKKycQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n4uxwxDn6usD6tP-7vc0kGOV-4lklFuIjxauLqPOTWPPN27ibSvJJjYrZ5WGJa9V1VzPi_buiTwtylVtGO9CgDj3jgDiW36cKOUW7R7KdWuQE0E9NQctj0Op8SCC8CHetO7pJ0OFZP45Bp4jHjVeCpnyZquXJXBcjKQgp3hbC2g2lWGamvwTtyDzBvuscHJiKaRj42C5fP_89LIZOMv0ZoTUwAeV4zwaFU_n74WyP02aPDOW8nyvJaaU76of1LDMNOuiIbiUHftWD5cjjitbyTsmEvOs1evxenSYMw6ApuG4ZVI1FCJ2gQ9nTtT9gJxnH51wNPTpVF_5yfmLTrSDcA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">این نفتی که اینها این مدلی  ملی کرده بودن رو گذاشته بودن توی کوزه  و آبش رو میخوردن ! حقیقتا!  مثل همین هزینه ۱۰۰۰ میلیاردی برای انرژی هسته‌ای  در ایرانه و خاموشی برقه!  هیچ درآمدی که نمی‌تونستن داشته باشن هیچ مردم هم چنان فقیر شدن که ظرف چند ماه از شعار «انرژی…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6612" target="_blank">📅 18:54 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6611">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV9BzkjaH2x4CbOwKVVJWmkAa8sQzSC1tfSHTtk9kXjmKaESlThfkgwCOwcXRa2P2ckR3gV3HZCk5a-w4GX8iVRqsQGBNJKuGIkfhlXyy4UqWAWD9JXgUnOwKt9yGxwuu6a0UdazncsebAIMxP1l7KFN2kdfo4_pc_Uow5kar5D1Brcw2cyLSEn40Dv6DIzbM0azmbuaucwpg8jqX4-aYXr5enjAPphEtb26IbE2o24RXR6ONhLpwfpDdNuhbl-ECP_o1FsH1PnZD100ooqBR5L7ege2PDr8irI2Qnw58VMdj-ZL9IVx9odiObo1OJ0dpAnWbQDfy_tucR1jIfsuUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران به اندازه مصرف خودش مواد غذایی تولید می‌کرد، ولی مشکل این بود که تقریبا ماشینی برای حمل و نقل وجود نداشت!  چون پروژه‌های عمرانی در سراسر کشور تعطیل شده بود، بیشتر مردم بیکار شده بودن،  دولت حقوق کارمندانش رو نداشت! پول نبود!  دولت توان خرید گندم و…..…</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/farahmand_alipour/6611" target="_blank">📅 18:45 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6610">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/enzQtcWdjhl4rMaiRajVMUB2lL8D2xsgExiRzs0z8KiFEMUK4VvNgs-KoWzoNKZLRrAVWSWGXOtseOBJjXKc-OCZ6UO4xxrMH0JiV8adQHU9JCYWSFvTO1x4gV7inBD9FJbP2EY65thNwsTzlC3UAG5KMkH_GtScJtlA9FdRyfqE6oblZMkbhvOjA5rLFPtT_Xl1q8oHcML5HLiQlisn2J6tfnXiVPfy_i5lsIBxAuttC2QI1AnQNVQKh5sNMCUqPkavXHk_dynOXtBsXCeF2b2DFB-GdVLzL9mM4YWcgHMKJ5fb_vmHX2zuZwOFPpJYD3r9Tt30MBDieVIw0Ol-UQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران در اون سالها، کارخونه و صنعتی نداشت!  وارد کننده «همه چیز» بود! دارو، لباس، آهن،  ماشین، سیمان و همه چیز!  ولی هیچ‌ پولی (هیچ ارزی) برای خرید کالا نداشت!  کار کشور به جایی رسید  که دولت مصدق اومد گفت اصلا فروش نفت رو بگذاریم کنار! (اقتصاد منهای نفت!)…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/farahmand_alipour/6610" target="_blank">📅 18:35 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6609">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GoibvlWiKCoeXs7QniEppGn9LlY-P7uejoOus3ImB4PTLIhW6XdYjrPApptnXFuNd7kWatA0hG9zPRKEP4mPhMroRkn8gaP4Ls8lLClrp-p5Og1MuwxAwrI0XsV9pD5mbWDUTNIe_iLHVAQbxm-v2MNwh9XTcKDAk7kd21FcDD4yetJnMZmG7XfyNWV1LjeV3sslnnkH8C_qx7n75Z-V0SNPyabhIQjXJpylnrE0kOkJCegNULXe1Xm8AV4U2g4pRJQ44iSmNMz9MaBxB5yK2Zuytp59fIT-Njii2KC8vs7FWe3FOPe9kTXZPoPnILxAmyOo2GlhVi467aRj-h7DOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صنعت نفت ملی شد، مردم‌ هم عموما بسیار خوشحال پشت سر مصدق بودند!  کمونیست‌ها، مذهبی‌ها، ملی‌گرایی از جنس خود مصدق و…..  میگفتن مهندسان توانای ایرانی می‌تونن نفت رو استخراج کنن، دروغ هم نمیگفتن! ایران‌تونست نفت استخراج کنه ولی کشور برای فروش نفت  و صادرات نفت…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/farahmand_alipour/6609" target="_blank">📅 18:27 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6608">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WMyjRJvEH6XlOas_cRRwGpxaPa6LtqDBBiazwBoKdIZQ3MhDkTop3VcZe_RDS0WAEVQ4tbWlxn7nagPSRFWTNl53EpXKWtLiZ2NbPtTBISByB3O1gxXAuyTrIj0PUp80RRaMPojQf1GrjrsriEAYfHgGeYoR53ULbPePDPnUihzKtpo7zkbAEoxQVTEeOBk1KBJSpLXWkT7miafOm6tagQkcbvtlnFObW8BZeFnDYwjJDPEQHoysZPLvQWg9lrIawUH17beQ3KAqIZuh6_ml4-_I5f56_anTX-P_pRsjKATz32aDh4PrTgVe1sguqHH3jUkTh02gHg24ggZ318lnSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رزم‌آرا، ملی کردن صنعت نفت رو رد نمی‌کرد ولی می‌گفت کشور آمادگی‌اش رو نداره!  و وقتی نخست وزیر شد، جلوی این طرح رو گرفت! تا اینکه یکی از اعضای «فدائیان اسلام» و شاگردان و نزدیکان نواب صفوی، او را به قتل رساند، زمانی که نخست وزیر بود.  مصدق که بر سر کار آمد…</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/farahmand_alipour/6608" target="_blank">📅 18:16 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6607">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F0JgdENI6elMjow-YcdSwoILFGV1Gb_BjmH8DVkJ910QMsxQB9kSZS-LU-zysg1uEGf45znvEqaOSd6YZm3961935rFK8VyRMRNbug7oAnEmMAHGC2er3kbaT4CJ-tftbaWodiZrUfBk1y8pVdzl7lsTreCL33T7RmkWk7PFv_PAOd3s3GCIxEAxGMt40ASL3luXKD9es1WHoHHgbbr_VXUBGsDmeS5XGblPM3mu8oLPNns8h5PSwYjqEe5Bfw1vrJ9jIFWp0xHaN4gbPqCXVfH3fwiYQBGbSutaSe7jUDeNQqS1ZxZWzNjDvwMw4YKcfHJjdUQYtyX3DAf_PSk5Rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حزب جمهوری اسلامی در یک کودتا و با طرح اتهامات کاملا مضحک و واهی  که بنی‌صدر در جنگ خائن است،  او را از ریاست جمهوری خلع کردند. سالها بعد شمخانی گفت نه!  او خائن نبود و اتفاقا دنبال پیروزی در جنگ بود و‌ گفت که سران‌ حزب جمهوری اسلامی  (بهشتی، رفسنجانی، خامنه‌ای)…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6607" target="_blank">📅 18:10 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6606">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YD8xGVWTH-EPLCKFrdIBQyDv9N69-2uTEdR57zhEQmZhGCJRlBmDIzSGt8HIZwtq7z-QMFv4VUt58e6PJjtdP15XZIx2V_rQ6ZBxHOxJ-BfcGVL3K3CsXP7ah5_ZG3AcN9WfBHRZLWMin1h2pDtE0x_SqeJjq2TJuu7RAcWjttcjGybRscgkHkRyztfcj00VCdh0QoCONfpC0-C1GvfByjDr83pKJckbltEHik03B7Kmzwle9SmqX7B4yDxTg7I38NbtPhHtTcOww74ZWQseu6VPRNMrfFF2kEZl2d1Jc4hs6xXTefBmZZIU_trIfiDGl7SkQ7q4SW-IWE6M5xNf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آیت‌الله کاشانی، نواب صفوی و مصدق،  همگی علیه «رزم آرا» بودند. مذهبی ها از مصدق خواسته بودند تا پس از پیروزی و ملی کردن صنعت نفت «احکام اسلامی» در کشور اجرا شود.  فدائیان اسلام و رهبر آن نواب صفوی،  اولین جرقه‌های چیزی را زدند که بعدها «جمهوری اسلامی» شد.…</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/farahmand_alipour/6606" target="_blank">📅 18:02 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6605">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hDmkewnzy5iw1sSTFPpPAekogAjmTjfdzNMcllqhEqy45X40jTNJFBlWWf1a33fsUb0Fdg9GgU558GhGY49qDlM7pitu9ut18HxYLJaa6nZQd9k3J0dh934bo1FB-nBHsapKTfsRr-agyfhpTHqs7OsdsJTBoUjhP6MSoBtyFGcJJAsTGZgD2GI2H-beQr5SmjjG11M_3Cxj2qGCsR1btKrEFUuSFSsiVD5OZ8A5LIsQsjpSeljU3PrJ6vfrwinh8V-F_qzhyk4ecfT9gNyuVsgqTjG7EhpdATnSSuFNQkxrIGnbRj9Gf2mx-ovzc0KGjGSh2eIegL1U17m9Jx66Xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر آشفتگی وضع کشور  پس از اشغال ایران توسط شوروی در شمال کشور دو کشور خودمختار ایجاد شده بود،  و کشور تحت فشار شوروی  توان بازپسگیری این سرزمین‌ها را نداشت،  مصدق ایده «فدرال شدن سراسر کشور»  را می‌داد! و به شدت با «رزم‌آرا» مخالف بود که می‌گفت…</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/farahmand_alipour/6605" target="_blank">📅 17:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6604">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0N-YZtabmfyaodx3f9I0wk2_CX44fYiwH5TZ1e5mQVRaq3PlnPIhf8BFILJz_4S8j2X_kPNk8TWp9HaK4VDgDtAf8TgxQcz1UGb3x_XAdBHnldfikA9NfPlsrZHtGukI5nX5ZWGkPSaBB2Q4h_gMhFwOF3SJzOqtl37dAvbwIeWLMQBngaPvfFYQBbTVNePFN2BvOusjVbZG7StltNDZaVl9JVZp_3MXibuBYTAIehjlxIil2TiqK325jz5A10YneSaNS7UP2TX6_JOmyrWx7a3rPGPP-dilHcTUxwmn1tOfxIGMsdEOdr6uXkteyA7IVD1ZiTaRejMKvzKuKw7mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنايت هايى كه جمهورى اسلامى عليه مردم ايران روا داشته، هرگز وهرگز اسرائيل عليه مردم فلسطين روا نداشته! قوه قضائيه جمهورى اسلامى عامل ٪٨٠ از مجموع اعدام‌هاى جهانه!! سيستم قضايى اسرائيل حتى يك فلسطينى رو اعدام نكرده! نه فلسطينى ونه يهودى و اسرائيلى! اسرائيل…</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/farahmand_alipour/6604" target="_blank">📅 17:39 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6603">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uKfqEwVGSmZ7MHNG3JPOjVZ-tPt5loAzlQsbLbJIN_F_bSxY9hTpQxHi57XWVUWXwQmmK4l_JA4OBtglJb3fY6K5penV7dkwsxNR7xrq4oHEc_y-AxS0iIQCHJwZlQAq2VKNu1XjkU4_B2v89oKhsDOT6DwoBc00n4_FYYhDDkC7vHCMQlGGrcSH_3QIMySb1Qvyr_X-c0ZPyCr_N24X3DACCSdpVWxtWKdvYekqZx16Opr9nV1eiyBEU8tkLEIAt_o01G6fzsO1LZT4_VJuIh644HnGyYOjN4g1CdkIeibqbl_VFFmdUQJ8DTRAclnY8pYL74zeSca8-X1HiyYf9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتفاضه «قیام» اول فلسطینیان ۶ سال و انتفاضه دوم ۵ سال و ۹ ماه طول کشید هر روز جوانان فلسطینی به سمت اسرائیلی‌ها و نیروهای نظامی اسرائیلی سنگ پرتاب می‌کردند.   حتی «یک فلسطینی» دستگیر شده توسط  قوه قضائیه اسرائیل اعدام نشد!  حتی یک نفر!  اسرايیل ۱۰ سال در…</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/farahmand_alipour/6603" target="_blank">📅 12:53 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6602">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vtRc7-LDhTAPdLCXkkysbeSGHaNOeXMl_9fUz6QJlv-Fd1somsy13PgTCVqD30CS84fLeX7zvOr9F6dLpw_wKIsAe6AuVBBseuJcXEKSbLlz4ipsLgGqeJRQFbUHpVx3GG4gWEsXXyTgQBvTY76KmwM_XOelYtQgrFgB72lOFgvXgAInTdezFP92fylZU03hU_k0u7KT472lSradjaRmHP5mCNY8GVkgNTqnB40SOzf716dplhDhya2byoQFIvtIcfEJn8f6ertOtQvUmLqtzvYfGx2toCUstrc88oNo2Vx0jCMmHyr0ouLRPISmmzsRlozlsxPLfS-6bGl8KlFo6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی «رزم‌آرا» نخست وزیر شد، مصدق که قدرت اصلی در پارلمان بود مانع از این شد که بودجه دولت را یکساله  تخصیص بدهند!  و بودجه دولت ماه به ماه! تصویب میشد!  دولت رزم آرا تقاضای چاپ پول کرد،  مصدق مانع اصلی شد!  همین مصدق بعدا نخست وزیر شد و مجلس را تعطیل کرد!…</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/farahmand_alipour/6602" target="_blank">📅 12:48 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6601">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BjC5rL8F5u_GVr-vLmfKVXxhXmV4QtkWX8odWhGmabexVEM4dU2Ze9h2hLUBRonS3WuX0IQ7kgcSqArqVtP70NfgbusaKlSkvAXWrGu8o5KVLOlfA5M34948kSiT8bYhbRb8LmF-ZXP97EiUYzlR-MzysxOrs1g7QFLCCS2J13S3hhjKys8A6fxSBjg5EdqRPcvqjDJ6vlPhvXLbVvDol9RM7YjDDpruCAuCELJfrz7m7MjkH6nzlbfveVyCxC1voog_CPhQZeSF_VDxoQDM7dDoWR0KEL2_plrpnLVYKNgBmXDgVCnzyMywW1TMgMc0ZWvKeQWgBMOZuY1lr-7G-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سپهبد «رزم‌آرا»، کسی بود که مهم‌ترین نقش  رو در سرکوب حکومت خودمختار کمونیستی  در آذربایجان و مهاباد انجام داد.  و چند سال بعد نخست وزیر ایران شد. مصدق از دشمنان جدی رزم‌آرا بود،  مخالف جدی برخورد نظامی با فرقه دمکرات در آذربایجان و مهاباد بود.  البته که مصدق…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6601" target="_blank">📅 12:38 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6600">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kRHY0aEaX1R81rP7QOtchCDitQJzZBRevIu5LkO1IR7eTuDzI9qXhgFFosi2i5aF-DqnmHX7VLvkp0fWGdok0c6gKL2bjhyn_Pb_JiVhsF6YhusjJQc9qHyR7tn6C3w67dkA6jF5zHcIp8M4knNxt4vAJ85NRIH8_rJsp7MTgfAK4NMiUuMmHiu84mu7voykd92tQ6qvzIY8W6ZDR6vzSQLLDeC9cObGZJiMYXRTT_DMeOXnBGndGn3Lb2YrgTZ67SsHvUdbpVr9OqDKB8ZF7NWBMxAT6-dZJnIA6nSTkCb4CtjIbUVehvNu7NcJfNE6qa9IgX4YchP3zwdH84zQRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی میگیم بر اساس مالیات بر چای و شکر و قند، راه آهن سراسری ایران ساخته شد،  یعنی چی دقیقا؟   دولت در سال ۱۳۰۴ قانونی تصویب کرد  که بر روی هر ۳ کیلو قند، یا شکر و چای  (۳ کیلو رو اون زمان میگفتن : یک من تبریزی)  ۲ ریال مالیات گرفته بشه.  یک من تبریزی ۱۰ ریال…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6600" target="_blank">📅 12:32 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6599">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RzeXf5sfSQTZYA-Wm-de3r-qgcCv0QkosbgUCGg3sjln_D3iEMWIjwGXIwFHblwFjVDLGRsfPbmdjU1lRt6oKdwrJdj0PniGakU1AghvuP4jy1FYubS5II8XaW7lFKXkT7jE67L6csaddWqM1mjxIxtKz5TSCEAvCbKN5EVGxhydXd9apy_codvUHJzOlJoo-TmY99CmMqBP7Q9DaQhoaNwZsClBQ0toqEYlf9CMLxIr0w3EBnr4PYxTXa4NfboO6rj66Uq5Z5yThaCu3_YFPdUOl1DmXXMp4xJLOmDAszJjx6K3Qctub1Ja6tF6CPKHuIwGzGS-2nQcrPGGp1YbmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">راه‌آهن سراسری ایران، زمانی ساخته شد که ایران راه شوسه  درست درمان هم نداشت!  زمانی که حتی قافله‌ها و کاروان‌‌های شتر از دست راهزنانی مثل «نایب حسین کاشی»  و خوانین عشایر در گوشه و کنار کشور ، امنیت تردد نداشتن!  هم قافله لخت میشد و هم افراد رو به گروگان میگرفتن…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6599" target="_blank">📅 12:14 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6598">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">مصدق پیشرفت را در آبادانی شهرها نمی‌دید! ساخت عمارت و هتل و آسفالت و آزادی حجاب و…..!  خامنه‌ای وقتی از امارات عربی متحده، و پیشرفت‌هایش صحبت می‌کرد هم  دقیقا از همین زاویه انتقاد می‌کرد!  میگفت : این‌ها که پیشرفت نیست!  حاکمانشان «بی‌عرضه»‌ترین هستند!  و…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6598" target="_blank">📅 12:04 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6597">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqXX1ycW0v__ZylkE3hRTOY9UWQrWJOio3XJLvfRY76o6rQ7dP5ql_fN8eoLpVEcVV7ueYzNcQnpCshcQJZ0G7eYq7is-xCIXmn6TVFbiQTI7FwQ_ZwHLREH1YgedaYf1OR4W62LGLZmu7eunD8GpHXHW7pQKfN2bGKjiFzdEwKDTLd0v9vO8jcNx2ULVcsm4741wBXCU_VKSY8eREf-TNWnFQFLrh0KIGZjuyHos6Tez4UbRvRTQ43y--1w3xuFi8nXo5vOuEMluiqS_phQpmdaqn_sa6-xpNqnujAeVHYBeuGBHnB4Ovh8TojqypD2s9YX3s2nX5owjBIsWtFcSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت. ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى، چه كسى میگفت؟  این حرف‌ها را مصدق میزد. مصدق حتی اقدام رضاشاه در آسفالت خیابان‌های…</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/farahmand_alipour/6597" target="_blank">📅 11:52 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6596">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hnbuUqylfF7ujRkp8GbhB1DcehHx8q4vRLAql2II3dxqSOnpk_EfHiWnkQ4SiCDuABHm3RUMdwkgQGnoo2FF1Cg7GzjzwZUcOnuE7EuLyGo6thYsmgPNaDsoOCwkNZpVhBRDEM8Ps7ChPzi_mo-qCX_cpX7HV3PZE3plyHLH-ZnlEB6sXM2nW6erX8TxhyB5DDvyG85wIrGKrgwF7jyzdooPYHJFuHQYJHl6Pbcis4zw7HfbIiskTnVxHQu8Yqr7F6hZRhMgAIDVqCxFxmIRjOUi8so0Cr1KAOkZ4QPusOGUuEW5Ks91mranhCrAzl3XbOzl_RKvPyYMfX7qJO7SlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل زمانى كه ما در مدرسه درس ميخونديم بهمون می‌گفتن که رضاشاه به خواست و دستور انگلیسی‌ها ، براى ايران راه آهن ساخت.
ولى مى‌دونيد اين حرفها رو خيلى سال قبل از جمهورى اسلامى،
چه كسى میگفت؟
این حرف‌ها را مصدق میزد.
مصدق حتی اقدام رضاشاه در آسفالت
خیابان‌های تهران را به درخواست
انگلیسی‌ها می‌دانست!
او ۱۰ سال پیش از آنکه با محمدرضاشاه در بیفتد، یعنی در سال ۱۳۲۲ ، نطقی در مجلس داشت از آزادی حجاب در زمان رضاشاه و تغییر چهره شهرهای ایران و آبادی آنها انتقاد کرد  و از جمله گفت :« رفع حجاب از زنان پیر
و بی‌تدبیر چه نفعی برای ما داشت؟
اگر خیابان‌ها آسفالت نمی‌بود چه می‌شد؟  و اگر عمارت‌ها و مهمان‌خانه‌ها [هتل] ساخته نشده بود به کجا ضرر می‌رسید؟»</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/farahmand_alipour/6596" target="_blank">📅 11:49 · 27 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6595">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VDgTO9JLepja-vYozDrZqiEEWvfnrKvk1mIBndSuJMPzbCn3C5Q0mImtsFu0xPvzybON8gmF_PDfRu7E20IP7TQ0wo8EJr5mod_5mpYUAJ7MZc2-SCmRS2B_PfRCbQVl7KGxpNATE38UyGSFb8gTtaGchXyqhfhejYyfYAsFb88vpYnkzrjSUrNcVU-x0HdSHaqq73MKB7-FYhiNVl6slXpKQ-7Xz9V_LCXc6RSorQ2TQzHJzNkkZO6jglBV6f7wMPznGSkuaVbrVlUbJEOwKKZlNu64Ag4C4hrPMwcVCCDwIFf4fVOHZ-9uuWVd9DS8bV_uwiitcARxBB0oqkss5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیروز نچیروان بارزانی
رئیس اقلیم کردستان عراق رسما درخواست داده بود که بین ج‌ا و آمریکا میانجی‌گری کنه.
خوشبختانه جمهوری اسلامی
همون دیشب با پهپاد به دفتر نخست وزیر
اقلیم حمله کرد، تا یادآوری بشه چه موجوداتی
در ایران حاکم هستند!
کار خوبی کردید، قطر و پاکستان رو هم بزنید!
قطر رو ولی حتی بیشتر!
که اون شبکه الجزیره‌اش
کپی صدا و سیمای خودتونه!</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6595" target="_blank">📅 17:29 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6594">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپایگاه خبری انتخاب</strong></div>
<div class="tg-text">🎥
تماشا کنید: «۹۰ میلیون ایرانی متهمند، مگر اینکه خلافش ثابت شود»
🔹
این هم نتیجه باز‌شدن مجلس پایداری!
🔹
عقلای مجلس از تصویب جزئیات خطرناک طرح جلوگیری می‌کنند؟
🆔
@Entekhab_ir</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6594" target="_blank">📅 00:17 · 26 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6593">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PyieLqyQlvyKatpbhpdM4tPC2qSbxunOo9FxTg-89Sflp971D5BCBWWBTktOZs5G217olZASNUPYZrC-Ni3BrZO3FyyeJIYSHArk3phxzGbuseaM4IDhXfXS9xyZO3FjUr71cZzB5GotN6tG2KMQgvQxHl_3EknuY7eb3kUtUCXfVtceRADEBe961EBFNihRS4qVPfg4w9YZ6eEdt20NyHBUC3UJfK5rn-VMSElbhFiOlAIynMgqtNoCy-dz6UzoHtu-rSAdn7wLy42lRAA_VGIoWwN1ly2XE_hKLRmBowsIcqCJus0FDA2IQmBbDAs7o9xHqJLbOYgXNxB_boC4yw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1874b5ce80.mp4?token=PyieLqyQlvyKatpbhpdM4tPC2qSbxunOo9FxTg-89Sflp971D5BCBWWBTktOZs5G217olZASNUPYZrC-Ni3BrZO3FyyeJIYSHArk3phxzGbuseaM4IDhXfXS9xyZO3FjUr71cZzB5GotN6tG2KMQgvQxHl_3EknuY7eb3kUtUCXfVtceRADEBe961EBFNihRS4qVPfg4w9YZ6eEdt20NyHBUC3UJfK5rn-VMSElbhFiOlAIynMgqtNoCy-dz6UzoHtu-rSAdn7wLy42lRAA_VGIoWwN1ly2XE_hKLRmBowsIcqCJus0FDA2IQmBbDAs7o9xHqJLbOYgXNxB_boC4yw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنبش شعوبیه یه چیزی توی این مایه‌ها بود
اعراب فاتح، ایرانیان رو تحقیر میکردن،
زنان و دخترهاشون رو توی بازارها می‌فروختن.
می‌زدن توی سرشون و ازشون جزیه می‌گرفتن.
ولی ایرانی‌ها گفتن اصلا ما خودمون از شما مسلمون‌تریم!  و در اسلامگرایی از عربها جلوتریم!
انقلاب اسلامی در هیچ کشوری عربی رخ نداد، در ایران رخ داد!
جمهوری اسلامی توی قانونش نوشته بی‌حجابی ۷۰ ضربه شلاق داره، نه فقط نوشته که اجرا هم میکنه.
هر روز پلمب کافه‌ها و... رو داریم.
هر صبح اعدام داریم، هنوز چند ماه از یک قتل عام نگذشته. اینها اما برای موشک‌های جمهوری اسلامی قر میدن و میرقصن.
البته که مردم ایران آگاه‌ترین مردم جهان نسبت به تاریخ و هویتشون هستن! خیلی!</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/farahmand_alipour/6593" target="_blank">📅 18:44 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6592">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QdkDl0A5Ned6cnMkZ4KLJEYOzRoGB-I3FRAwgjaNrAFP2y1fhUXoOj_5ajOUQp1jWlSCNmgxTO4lqcvb2MW7Qel2pBc2SNqywXdGufbhuVIixUaQXAkDDV7GJa6uwkpYwmlWu7SA-66G-lSPJrvbHpc1aL5YFR2KVEtexy_l-weRdVMp-gKlM_MRsZs9vpHC43RQpVtKjI-Jzf_HSsf04PRWwkE1ZQTE6w6qb5lPPZFPEz2hL5gJSvhkKtidrfxpXK4DKHXYsnP7DHUyqCtE87YHZKOX0Dvy7CFztw8-6CKa2VWSCuLrgSGcNcVWYaSvOudu4c9sLgBO9oRKsqIgag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هزینه بقای شما نابودی ایرانه!
اگر اینگونه است که تسلیت به ایران
و چند نسل آینده ایرانی!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6592" target="_blank">📅 17:11 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6591">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">اگه این موضوع به این صراحت در تاریخ اسلام و سنت اسلام وجود داره  و قرآن هم صریحا مجوز داده،  چرا در ایران این نمایش‌ها برای گروه تروریستی داعش برگزار میشه؟  پاسخ ساده است!  ‌اونهایی که این برنامه‌ها رو میریزن می‌دونن عموم ایرانی‌ها از تاریخ اسلام بیخبرن! اطلاعی…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6591" target="_blank">📅 15:46 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6590">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این هیئت رفتند پیش پیامبر اسلام  و گفتند : « یا محمد!  در میان این اسیران، خاله و دایی‌ها  و زنانِ دایهٔ تو (کسانی که تو را در کودکی شیر داده بودند، مانند حلیمه سعدیه و قومش) حضور دارند.  ما را دریاب.» پیامبر اسلام هم گفت من سهم خودم  و بنی‌هاشم رو میبخشم!…</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6590" target="_blank">📅 15:04 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6589">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">در جنگ با هوازن (جنگ حنین)  [که خامنه‌ای قیام حاشیه نشینان فقیر مشهد- کوی طلاب در سال ۱۳۷۱ رو به بازماندگان جنگ حنین نسبت داد!!!]  تعداد زیادی زن و کودک نصیب مسلمان شد!  مسلمانان مکه رو فتح کرده بودند  میخواستن برن طائف رو هم بگیرن که وسط راه جنگ با قبیله…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6589" target="_blank">📅 15:00 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6588">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">آیا این تنها جنگ و مورد بود که در زمان پیامبر اسلام رخ داد، و زنان و کودکان به عنوان غنیمت جنگی برداشته شدند؟  پاسخ قطعی : خیر!  در جریان حمله به گروه دیگری از یهودیان،  در جنگ خیبر، زنان و کودکان آنها هم به عنوان غنیمت برداشته شدند،  از جمله زنی به نام «صفیه…</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/farahmand_alipour/6588" target="_blank">📅 14:56 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6587">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">آیا علی هم سهمی برد؟  قطعا!  از اونجایی که ارتش اسلام حدود ۳ هزار نفر بود، و سهم سواره‌ها ۳ برابر پیاده‌ها بود،  همه املاک، زمین‌ها، پول و برده‌ها، ارزش گذاری شد، ابتدا «خمس» (یک پنجم) که سهم پیامبر بود جدا شد و سپس ۸۰٪ بقیه بین افراد تقسیم شد. از اونجا که…</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6587" target="_blank">📅 14:50 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6586">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">وقتی ثابت بن قیس (مسلمان) نزد زبیر بن باطا (یهودی - اسیر) رفت و به او مژده داد که از پیامبر برای او، همسرش، فرزندانش و اموالش امان گرفته است، مکالمه‌ای بین آن‌ها شکل گرفت: زبیر پس از شنیدن این خبر، از ثابت درباره سرنوشت رهبران و بزرگان قبیله‌اش پرسید و تک‌تک…</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/farahmand_alipour/6586" target="_blank">📅 14:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6585">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">پیامبر اسلام سهم خودش رو  (حدود ۲۵۰ زن و کودک) رو ،  که خب سهم «خمس» بودند، رو فرستاد که  در «نجد» بفروشند، و با پولش اسب  و اسلحه خریداری بشه برای ارتش اسلام.  البته این وسط یکی دو اتفاق هم افتاد،  مثلا یک مرد مسلمان به نام «ثابت بن قیس»  از پیامبر خواهش…</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/farahmand_alipour/6585" target="_blank">📅 14:30 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6584">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">آیا به بردگی گرفتن زنان و فروش اونها و یا ازدواج سریع با اونها اگه شوهر داشتن مشکلی داشت؟  نه! چون خود آیه ۲۴ سوره نسا صریحا اینو میگه!  وقتی هم قرآن بگه  هیچ آخوندی چه شیعه چه سنی نمی‌تونه مخالفت کنه!</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/farahmand_alipour/6584" target="_blank">📅 14:26 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6583">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=YTYKn3K7jxGGV5_-4iG73rUVchNCHbOyttvRg7o-538mcAzVdpJaZMXiPggaNcGp6kZ3MgGIn8K5dLSo_4KcrY3oHurz0SSr5nUq1EmC0VuolXVwLf-9OUn9NhChk3NtayB7vN67O5T6GhsqwWQoH6FUqp64ykoeIONt7GWTAJhyOf-PN6coIQm6V6CGcpDr0DTs0JX40YzqRnwKnfe7rR4SHOR5KU_HD94N-AGMV9VnGTsjsrfmZ4tXq9hpJhE7ODF3XLvuVxycaKY4OGICN1rfXyKurFl30Wz-1FNs9idW6z25UFeoWu9p2yEPyLE7vgxR4ZSQgaK-MvDta2mNDg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a982a9f63b.mp4?token=YTYKn3K7jxGGV5_-4iG73rUVchNCHbOyttvRg7o-538mcAzVdpJaZMXiPggaNcGp6kZ3MgGIn8K5dLSo_4KcrY3oHurz0SSr5nUq1EmC0VuolXVwLf-9OUn9NhChk3NtayB7vN67O5T6GhsqwWQoH6FUqp64ykoeIONt7GWTAJhyOf-PN6coIQm6V6CGcpDr0DTs0JX40YzqRnwKnfe7rR4SHOR5KU_HD94N-AGMV9VnGTsjsrfmZ4tXq9hpJhE7ODF3XLvuVxycaKY4OGICN1rfXyKurFl30Wz-1FNs9idW6z25UFeoWu9p2yEPyLE7vgxR4ZSQgaK-MvDta2mNDg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در روایات این دو کتاب، اومده که حدود  هزار زن و دختر و کودک یهودی از این جنگ موند!  که اینها رو به عنوان «غنیمت جنگی» برداشتند. یک پنجم کل این تعداد، تحت قانون «خمس»  سهم حکومت اسلامی و پیامبر شد.  چهار پنجم هم بین سربازان و فرماندهان ارتش اسلام تقسیم شد!…</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/farahmand_alipour/6583" target="_blank">📅 14:16 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6582">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PxZ-gfcCgXSBddgVm8S156FoccjHQ0zrBi3R0p35Ntl_qSq1L13TepFfOOGPOWh0WkwKJkRjdII7XezJpcawvIsVxfDxdn2G2P5kEqegGzvQqbrbALQKT6Vm6aCq0-ZX53iZlAXT18Gvmxqb-EjPbPT4FgnGgiViMU6_pU3ijXHPXyvYQrw72oja3QAegIr1OGhPlVSTBZP2oZWylGFy3a8de8vLk-cu9XRN96F0YDm5QrUBO9LQeqn60mqSzWW5Ereq05m_QhUAPKxZurSQusmjtbCzgqsj7NVX2sKLOvoq8qWETkXahT2U36VykkQ3ssfi__O5TVDUpF0L49FNBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نقاشی مینیاتور از جنگ بنی‌قریظه و صدور حکم کشتن تمام مردان و پسران یهودی.  مردان رو یک به یک کنترل کردند،  که آیا کودکه و به عنوان برده بردارند، یا به قتل برسانند.  مردان بالغ که از چهره‌‌شون مشخص بود که بالغن. نوجوان‌ها کمی دشوارتر بود.  لباس زیر اونها رو…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6582" target="_blank">📅 14:06 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6581">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaGD7vQcrQUOtJccWzxcqM0ssqeT5w1pL9yMTb3D3omzNSb3PSL15lEdfYQIvUDX8FZz9g-UYzQVD72tJc6a2u6tz59sImaRjUT32BxN8myyoTrKkIdjiKiPayqjnMgngnh3cSBvg-x0-KGMTQNu-CTeVV_RF28RnfpGUWjci0Qb4OoMEYrsK7l4V2FbvnE2LhvxLCAsxy5P5sYL3PNZTUDIbmkMZLpRbPtA5g3mm1YdAo7yoNrXTYox3Ns3vP0DYZnpRC2-XevOHoEdj1mD2E-ZSPUnkWJv6mvQh4BLcF3nu8DJ7dG3JlPfuEZrLr0EQElDxkw2t7DWWXsL05l2CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در جریان جنگ علیه قبیله یهودی بنی‌قریظه،  به فرماندهی پیامبر اسلام،  تمام مردان و پسران بالغ کشته شدند.  همه اینها تسلیم شده بودند و اسیر بودند!  یعنی در جریان نبرد و جنگ کشته نشدند!  همه تسلیم بودند!  کتاب‌های اصلی تاریخ صدر اسلام  مثل سیره ابن‌هاشم و تاریخ…</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/farahmand_alipour/6581" target="_blank">📅 13:52 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6580">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/201818ce22.mp4?token=K7wgjitNdnrOc6cUUioKisWUZoAMwLE2RmnStU_yOmPfVACkxBPRjuV-9pCFM7DXNtS8QDdjoPxzoqN54VWGb8S1knRzM9C8FUALFjp6ZRo9uwR7sDlx2J4rkvtAB6QIBtIYnuUrdwfBIVOL4JjT2S3QhCP8aVBDTQPxXb4guPpq7ONARWz3PLVHEP_LkuuuKaZCLiJYZ3eLh6SMYqGVQAJOJCQmKwtBRXIdx53t1Tv0_hBr6gMlTf_P3G1cFbU6H1humRbD7s-uCNz-YTQhc1UASaveZWb_tYJR2tfCECX0HuJXzgwGdpR2w6vAaEAKOIJHqSG79G8vgXvbmiH4PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/201818ce22.mp4?token=K7wgjitNdnrOc6cUUioKisWUZoAMwLE2RmnStU_yOmPfVACkxBPRjuV-9pCFM7DXNtS8QDdjoPxzoqN54VWGb8S1knRzM9C8FUALFjp6ZRo9uwR7sDlx2J4rkvtAB6QIBtIYnuUrdwfBIVOL4JjT2S3QhCP8aVBDTQPxXb4guPpq7ONARWz3PLVHEP_LkuuuKaZCLiJYZ3eLh6SMYqGVQAJOJCQmKwtBRXIdx53t1Tv0_hBr6gMlTf_P3G1cFbU6H1humRbD7s-uCNz-YTQhc1UASaveZWb_tYJR2tfCECX0HuJXzgwGdpR2w6vAaEAKOIJHqSG79G8vgXvbmiH4PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد. اما اين الگوی به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى…</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/farahmand_alipour/6580" target="_blank">📅 13:41 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6579">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPqY7afCokRQtgCxJiVJmSrWnLqANNkLES8HtqEXd-Ege7Q-r9Nw2Sd4uDn7TYu16PnNndHkz5XYGQh9nVv_1l8nfMiwUQxmG1djvS89LqTj8di0Iw2qwx1GXEeBU_MIQVUZVDlWfsIX9k_I8SrAn1GDyjWOi2gZjlDKGwapfq6JeORXsfswxhRSdEBdrhuTPpAD5gRzFuqxapNo3rx096OFKQhK77XM0OYFDioAveAesGbnjOMaJXxwUscXyvk22CdOfhlYd_Fpv___MNQV_JxwZPXXiF1LCXez_Ige4EAIOWUMTMY3vPiGZaanY1NpgtwR72EvgX9PWndQ8vVUzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در تاريخ ٢٩ بهمن ۱۴۰۲ در متروى تهران نمايشى اجرا شدكه
اگه گروه تروريستى داعش بياد ايران، زنان رو به اسارت و بردگی میگیره و اينكه قدردان جمهورى اسلامى باشيد.
اما اين الگوی
به بردگی  گرفتن زنان وفروختن اونها در بازارها، از كجا الگو گرفته شده؟ آيا گروه تروريستى داعش اقدامى
ضد اسلامى انجام داده؟ پاسخ صريح : نه!
آيا مذهب شيعه، مخالف اين كارهاست؟
پاسخ صريح : نه! به هيج وجه!</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/farahmand_alipour/6579" target="_blank">📅 13:40 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6578">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZkghfB3cQPrS_PK46QqAugBKPeI61j0xAXnzcpAC5hNEU7g1bDfu4FlhxoczlTn6aMIqE5KysOtdz8JmruQopI9poNUqUL406mUSkGwMmIlyXbFYydZD4sAzmj2QVejmUvOe2NDmis6mn0rARTSLvinFGZsaOu1_83XEQXB3CY7oAyv6RcxNooMa0FU68XPPbt7mYucopFZeEJUuhoF-mq3ji8_jNVQv8E6vOcL9bqRWsjhqIQrOvvil23o3DEvmWnUsoUsy9xdDrFLSAS_b4T0yCXuUL26GD6WB6MzYGi_PJ6rQAIK-2xwssId89vagF-eYk1mQOQygyRUEknz35A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
میزان، خبرگزاری قوه قضاییه از اعدام شهرام صادقی، از معترضان انقلاب ملی ایرانیان در دی‌ماه ۱۴۰۴ در کرج، خبر داد، اعدامی که بر اساس روایت رسمی دستگاه قضایی جمهوری اسلامی، در پی پرونده‌ای با اتهام‌های امنیتی انجام شده است.
میزان نوشت که صادقی به اتهام «اقدام عملیاتی» به نفع اسرائیل و آمریکا و گروه‌های «متخاصم» و همچنین اقدام «علیه امنیت و منافع ملی» به اعدام محکوم شده بود. این خبرگزاری مدعی شده است که او در جریان اعتراضات، در ۱۸ دی‌ماه، به دلیل «زیر گرفتن ماموران با خودرو» بازداشت شده بود.
قوه قضاییه جزئیات بیشتری درباره روند رسیدگی قضایی، مستندات اتهام «اقدام عملیاتی» یا چگونگی صدور و تایید حکم اعدام منتشر نکرده است. همچنین در گزارش رسمی، جزئیات مستقلی درباره ادعای زیر گرفتن ماموران و اینکه این اتهام دقیقا بر چه شواهدی استوار بوده، ارائه نشده است.
@indypersian</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/farahmand_alipour/6578" target="_blank">📅 08:33 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6576">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bUvNQkR0HrporZbNL44xyGv0PrHn7LU9oeYkm3c_JVm4uP3gpsLdkKSux1fJgCjWm4Haxe-6KvvXpCkuTNrpgn3NjBM7ZFO3dmt_WJ5duhQT6n8YRmb8OZgm-wi4WuLCemgC6snm446VN1DA4rEjCyOqgP151CwIufD00h8AKPIH6vl4IRolvX7-OzCK3wVJJYN2om8vrG-H0I3MieuMpToANzX1xYXQp6Adabhc3dnMhwPMP1W8YXkX4aDezRPuR9RH08mBeNcNkoTslw73gIngOohirRzyFnVlBzyDHgUY-NwgiaPsWzs5FvjKmwM1HcAUHVeZa5pwdZNqIw7dWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=U8jelYqLxMXUinI8CVMS61VxHx1iBRiibVoI-71KkJiQwegZb6Xs7aMmQz3o76G-D_BLAt3SZK4Z1JRTTkbYcIPimd1fGlxR-G4L75DIvWl0ZvuPO-KJsS-yxZThS5CVvEcx6CQXipsc5n4NF66JVkQsRpW5xfbRDJ0OK6nNLf3UlBdxMu_FOOVH6UJ4fc4kpEiSKkSFz7MoEKQr6Jy3QSbm-yQ6R-a-PEF0EKH3UTM1kbyV-QI_cIOUzMGhT7CZmHVCYsQkmRR556lA07WlfgYAo56vqigJ1_Mu_DAJ_3XqjwiSG96NieWntcGEsEZpuldPyoiYJiAlBUG3wumOmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eb4f8f85b8.mp4?token=U8jelYqLxMXUinI8CVMS61VxHx1iBRiibVoI-71KkJiQwegZb6Xs7aMmQz3o76G-D_BLAt3SZK4Z1JRTTkbYcIPimd1fGlxR-G4L75DIvWl0ZvuPO-KJsS-yxZThS5CVvEcx6CQXipsc5n4NF66JVkQsRpW5xfbRDJ0OK6nNLf3UlBdxMu_FOOVH6UJ4fc4kpEiSKkSFz7MoEKQr6Jy3QSbm-yQ6R-a-PEF0EKH3UTM1kbyV-QI_cIOUzMGhT7CZmHVCYsQkmRR556lA07WlfgYAo56vqigJ1_Mu_DAJ_3XqjwiSG96NieWntcGEsEZpuldPyoiYJiAlBUG3wumOmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در پاكستان ۲۶۰ ميليون مسلمان زندگی ميكنن (از جمله ۴۰ ميليون شيعه)
اما يك آمريكايى رفت و اين خانواده رو بعد از چند نسل از بردگی نجات داد.
در اين کپشن نوشته نشده، اما ايشون حدود ١٠ خانواده رو نجات داد!!
اين مورد از برده دارى تا همين چند سال پيش در پاكستان «قانونى» بود. الان غير قانونيه اما هنوز رايجه.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/farahmand_alipour/6576" target="_blank">📅 00:07 · 25 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6575">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=MkWgamTRSlebnTkYrzeIeB8qy5HgcT1Vc-sr8ZAG7xaUtNBtRwyHSwqzrbNcidyhMbLt4Md8ctaNb6u1k7kWa6jYpS4y9ZjXRhsayeNoNzChY7qtN-NvYZPBcZAjnCrpl3lRXMFNWtGWdiQ4eLBuce46pDxDeZxv0xQq1EVmvbx8gEAfZmowSNu8XsjH6w4qKd2IjpLo-2hqgNEKvXk0vMsC9EyW8ONZ2al8sKCmTMEy02FLZ79Fbg2VuY4y3DNlVJHnfr5bNnojVfrjz-YAHh4_-UgYTGBi_27P3WIfPTQfs-4z83cQ95sUE5HsOECL7dPGTiyivvjXmo8wzpa66A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b59ed2e4aa.mp4?token=MkWgamTRSlebnTkYrzeIeB8qy5HgcT1Vc-sr8ZAG7xaUtNBtRwyHSwqzrbNcidyhMbLt4Md8ctaNb6u1k7kWa6jYpS4y9ZjXRhsayeNoNzChY7qtN-NvYZPBcZAjnCrpl3lRXMFNWtGWdiQ4eLBuce46pDxDeZxv0xQq1EVmvbx8gEAfZmowSNu8XsjH6w4qKd2IjpLo-2hqgNEKvXk0vMsC9EyW8ONZ2al8sKCmTMEy02FLZ79Fbg2VuY4y3DNlVJHnfr5bNnojVfrjz-YAHh4_-UgYTGBi_27P3WIfPTQfs-4z83cQ95sUE5HsOECL7dPGTiyivvjXmo8wzpa66A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نماينده ملاير با چفیه حمايت از غزه و فلسطين!
«مهسا امينى به درك واصل شد.»
مگه مهسا به شما چه ظلمى كرده بود كه اينقدر طلبكار هم هستيد؟
غير از اينه كه به خاطر يه روسرى و به خاطر افكار عقب افتاده‌تون، جونش رو گرفتید؟
حالا ناراحت و طلبكار هم هستيد؟؟
توى خودتون و دين‌تون و نظام تون
و چفیه‌تون و فلسطين تون!</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6575" target="_blank">📅 21:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6574">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wc_MApcnSDBOYkeVfOGPPF2ElFdw776dCubWKaaaWjh9pHYYAF26UL2On75_dr02F4mm5771NH44FVKrtzbpt1XrktNFuOfNsuzirNoUQTKDi_VnYS-OuD1ne2IR-kfTCQ7YktQrtiK5hLwNKvoABsdwDS4HRpFiqN0HJt_Yk4knGkinV_8z60uSTYSewcCunbzVVEsUoD06G5AWw5l8UJ1kqvFwmGjj2vAojJ2chfOVzl8v8yyHOGWbT_-Yqu81XweqMwj8rMPLaFwTbOfaJz3FHqvexvWnp_cu0QpnRGWd6SyX_Rn33uvvlojbxAApME_zE8Y9HOEX5RkD5HHUBQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خدا اون روز رو نیاره!
همین ایران و غزه و جنوب لبنان
که حاکم شدید کافیه!
همین افغانستان بسه!
میخوام ۷۰۰ سال سیاه گروه تروریستی حماس نتونه حکومت اسلامی در غزه ایجاد کنه!
میخوام ۸۰۰ سال سیاه گروه تروریستی
حزب‌الله در «دکترین ضاحیه» بمونه!
و رهبر شما هم از زیر گودال و چاهِ حقارت،
«علی الاصول» بنویسه براتون!</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6574" target="_blank">📅 11:14 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6573">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AT0v5kIJl4f6P6ZgVDdtXe3qK5I057m4V4UVn6w1qQcUcD8mjeZfObq4Hg87dosWniIBF6wQoxH52LFqGfRa81wm1bVKgRCmEN0Ihoccjnz74zBD8t55hctvMyKww4e86NKVxbQXlQbRhbrzACSp8C7tgryBq8V82gd9RekAaGL-TkyNyiw-HBOQ0KUEywZyXFsomO8VyF8k0Y1cmcamtVHF9CESUL4yFMZi2yxf3_hK1hvw7zzUl0R1IxzUYFsll9fRy6Xx5tjMMYgIa4leunXfs_7IfkcFC6noLNIfCXT3-ug1yqXEl0e6gFQ2H_Glwufm2qH52BC3FCw1e22GPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی از پسران معصومه ابتکار (سید طه هاشمی) به خاطر اینکه پول یک موسسه رو بالا کشیده بود (به ارزش امروزی حدود ۱۷۰ هزار دلار  یا حدود ۳۳ میلیارد تومن)  حکم جلب صادر شد.  سید طه هاشمی همچنین متهمه که سرمایه‌گذارن رو پیدا می‌کرد، یه پولی ازشون میگرفت و با توجه…</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6573" target="_blank">📅 10:29 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6572">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jg5mdgl_hOVIWg9CDEFq7wOx_Yi9a8wTy2QveG36eMw5dn7vDR7Jey7KhWRhlMBQ67Mm6RMUPljQAHHiq2exsi9BORaRjI9CrRCW0citC27o5nhQIVUZ3cCwyS507jIk1I5JviMqNxuXjM4ZETC4d2u5IHjWlZy_bd2i6twMFtSCGAztCw-ocJVGPQG4qWXV4mIkDLXzripuO5KV-V4ip5Oqp2UOJDhG3Dh9bIrN-aA6C-et0pvvVF7pkf6Ncr7ZowDWkSSurA598aCEX99e-lZr_6R3WX_fDLKk96SkHA2PhZsMPHT4pPq91EA7OHEKtezmNKH5ljcmb6vZpJpP8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در پرونده «املاک نجومی» که شورای شهر تهران به ریاست چمران، زمین‌های مرغوب دولتی رو با نرخ ۵۰٪ زیر قیمت، به مسئولان حکومتی فروخت تا اونها بتونن چند برابر بفروشن  (بعضا با گرفتن مجوز تجاری و…..)  و از سفره انقلاب بهره‌ای ببرن،  نام معصومه ابتکار هم دیده میشه.…</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6572" target="_blank">📅 10:24 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6571">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTkyk6xStodQDgpobgf0Ub3JhnPAatBDMF8MMjrHMq4NHfDpGodQco0ce6E6PcE0ojd80UYJ2apZ8h2xgNtJ66ipvjZ-mW1CizXif9B1KDCrt3-iqT2IgD27FdMKuOB8BiiTBX1aVL0ulwedDqdihvt_rXLgn3ubwIXHFN_CCZToFbvlamactqbzn28t2Czfw68ycQet7L1S99Gz9DEumNpQGB_GTApwUx9iwptVSXagOpGUemTJrhsS65OVCXfYZFVomt9FYcGpcqK9a52SFHAW9eOTct39wvqFHCAD2jG_QMESMYNnCH7zLIIP0Ckklgz2IDDmJei-oWoXZOJ8JA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">معصومه ابتکار، از زمین‌های ارزشمندی  که جمهوری اسلامی پس از وقوع انقلاب مصادره کرده بود نیز سهم برد!  او به همراه مادرش (فاطمه برزگر)، خاله‌اش، پسرش و البته «مهدی چمران»  این زمین‌ها و املاک را به اسم «موسسه زینب کبری» ثبت کردن! موسسه‌ای با زمین‌های مرغوب،…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6571" target="_blank">📅 10:17 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6570">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bNd6Gf2D6d8bFf-0US-mlPl-X576xH-WXMPKoHwDWAynPZqBsPAOKQt7KiD0hxVVCX4pt7f8kpHpMhq9NV0SJPO7gajkvFmy8PahX2t9CUnQzvYn3PPmz4N8mSPrnR8O6NlBfY7_WS6p1i2nhm7r7dafC6gE_9f9TAf0WLaMZpA4K8aqUfDPXHLgnt81HAUMVs_d5S7mYwQOumlclvY9RflJqYWEbY-l4jz43R4DH-t3Vc724nr6VDt8vMtfkCEL8NrTdFpiKyp_3rbJr2uKcGDp8aAe2Huz3HqLASceiPHYj33eRDgCxtA9Fo6mEX54PTJxSRBCevz-JnX4iXMjPQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این تصویری از پرونده «چوبهای روسی»!  معصومه ابتکار همچنین در دورانی  که رئیس سازمان محیط زیست بود،  به «زنگنه» وزیر نفت گفته بود که اعلام کند که دولت «بنزین کم گوگرد» از اروپا وارد کرده!  در حالی که این فقط دروغ گفتن به مردم بود!  زنگنه بعدها خودش این موضوع…</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/farahmand_alipour/6570" target="_blank">📅 10:13 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6569">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBTutqPCkjkMir_JmOpbVxaAJRN3I2ej-Pp2qCOLl3RUgcuOkUzDlH6L_sR-XAylfgwfyyX_d0KnPcqEQYn4LlIB2X4mdIwrthQY7zZ2S3RI4yHgjFuRHcYBQMVvHUg2WyZo0o68NgfqK07ymFEgsOnD19tf51UWmllNX52tPKZ1qKBW9_7nVrLFMMppZTeNEmSFTXAKfIIEsXhWAPwhs6Z0OVL3_xlzjUN1nPT55SK6Glj95ViO_GWLp3LIRME7hMCAeyOMYYbL6KN6OjnOpNb2A44_UieqfSamrEC_nUUcdsLJv6UNeQ4aMNLnp0wS7jA_Nz0K3OXsyxtIMAjzBw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">در حالی که به خاطر سیاست‌های این افراد،  از جمله این زن و شوهر،  کل کشور و جامعه ایران درگیر یک بحران  عظیم شد، آنها از رانت‌های بزرگ حکومتی  برخوردار شدند!  سید محمد هاشمی، وارد کار و کسب شد!  از واردات قطعات سلاح برای وزارت دفاع تا واردات چوب ! از جمله پول…</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/farahmand_alipour/6569" target="_blank">📅 10:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6568">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">معصومه ابتکار و همسرش «سید محمد هاشمی»  که او هم در تیم گروگانگیرها بود،  در همین ایام گروگانگیری، با هم آشنا  میشن و باهم ازدواج میکنن.  سید محمد هاشمی خودش فرزند یک آیت‌الله است!  گروگانگیری ۴۴۴ روزه موجب آغاز خصومت شدید آمریکا علیه ایران و آغاز تحریم‌ها…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6568" target="_blank">📅 09:40 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6567">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pvtSvbPMd72GtWimCrjJArh1rk1xmE8zkwYy8yBOAyw_ZtTBjs0ToQWrgiz_iBv6lDZHIRY2l7LNfJ2Zvq9EWN4iVTHu99ZGjpoB2QyK_U7eoVKMaNlPJAJi80PdCQqr2cC1DwxHIjZ68HwelO6tc5G-VYlwGODd4yR3m12lvVAlf7_Qm6LteECGiT4Tw6z8f-xmkT558Ll2aKDJsNYKj_0W0KWXVv4VF4Jeyh16Xe3DOE3aUnuBwtJ-1M1HXNjTLOa6aG5lWbXP0miMrg2a8WNuLQUPBfm2H6uAVqX3MzacqMmZpuad1s8Dny3u56Ivax3RJ_fRZTDByZxvYlyIRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مریم در این نامه به مقامات آمریکایی نوشته  کارهای «معصومه ابتکار» ربطی به ما نداره!  ۴۷ سال پیش بوده و…..!  توی این ویدئو که خود مریم گرفته ولی، خودش دست به یک مقایسه میزنه، میگه بقیه پرچم آمریکا رو زدن ولی ما پرچم امام‌حسین رو!  در واقع عروس خانم خواسته انتخاب…</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6567" target="_blank">📅 09:36 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6566">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/farahmand_alipour/6566" target="_blank">📅 09:25 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6565">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=SgYoaHZV8kyNiZlofi6jxiEvyvJemHBnMJbHcFKuUZbW_AHqXjkN65IHbIyTEdV3sk9xj2ZlXspHAqOEayTrK5ZQOiCV-92DXB_Jn6nLx3LhBEgUPwH51drRqBIyhhkfx7KoB4pmf3YR1dQyiCnnZJY3yvZ974ISykyUxHnOdiw15IPIfrzBsNyD6uySwbY2wT8Kc7VWrsEAkcSVY1yvK7SjrEBpLEhZfTlWVZr8_aUMQdcHrkCE4fXTWkGmJYNiyU52iYWDlHdfbHcrVl6GVQ-4MkPcW-pxvbBnsRRrf8BvIW9OzDPC-fmeN3-2L0u7Bk73q_1-QAQTdNkSJxtmrA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4aff068a.mp4?token=SgYoaHZV8kyNiZlofi6jxiEvyvJemHBnMJbHcFKuUZbW_AHqXjkN65IHbIyTEdV3sk9xj2ZlXspHAqOEayTrK5ZQOiCV-92DXB_Jn6nLx3LhBEgUPwH51drRqBIyhhkfx7KoB4pmf3YR1dQyiCnnZJY3yvZ974ISykyUxHnOdiw15IPIfrzBsNyD6uySwbY2wT8Kc7VWrsEAkcSVY1yvK7SjrEBpLEhZfTlWVZr8_aUMQdcHrkCE4fXTWkGmJYNiyU52iYWDlHdfbHcrVl6GVQ-4MkPcW-pxvbBnsRRrf8BvIW9OzDPC-fmeN3-2L0u7Bk73q_1-QAQTdNkSJxtmrA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مریم، عروس «معصومه ابتکار» در نامه‌اش
به مقامات آمریکایی نوشته که مادرشوهرم
[معصومه ابتکار] فقط مترجم بود!!
در حالی که چنین چیزی واقعیت نداره!
او «سخنگوی گروگانگیران» بود! که برای ۴۴۴ روز دیپلمات‌های آمریکایی رو به گروگان گرفتند
و واضحا تهدیدشون می‌کرد.
میگفت شخصا می‌تونه اسلحه رو بگذره
روی سر یکی از گروگان‌ها و اونو  بکشه.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6565" target="_blank">📅 09:16 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6564">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=VnmBeFMfWQXHXdQEWMaB7p9FQd6SSR6egSiYVIXXvEBde32O44_qTRKp1RA9_EcKbWLLllD2nBSSxsyhT41tk1JbX7MFT2KeC12kz4VcZnXqkyW7_mtBVPThIha7yXfK8F6D1k_A8QB1TbZJ2MOaSAmSxzFaf49xawx2PxsVDMoBnuoL0Yl8QlCkOoJ-6RnyCVjnWEuBW5uCkEQ5XujkTjY8wVSs1FF9_acbab34teDCvprXZfSbf8swSOPq9rtOTJ4BwdXl-a_HDOgOg6_ObShbLSdWw2JqWvhx6loMgEn1dnFbmjk1O4byESq1kZQvSJJPZ6ENlOiixGGUNn2TJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f7a1d6d2.mp4?token=VnmBeFMfWQXHXdQEWMaB7p9FQd6SSR6egSiYVIXXvEBde32O44_qTRKp1RA9_EcKbWLLllD2nBSSxsyhT41tk1JbX7MFT2KeC12kz4VcZnXqkyW7_mtBVPThIha7yXfK8F6D1k_A8QB1TbZJ2MOaSAmSxzFaf49xawx2PxsVDMoBnuoL0Yl8QlCkOoJ-6RnyCVjnWEuBW5uCkEQ5XujkTjY8wVSs1FF9_acbab34teDCvprXZfSbf8swSOPq9rtOTJ4BwdXl-a_HDOgOg6_ObShbLSdWw2JqWvhx6loMgEn1dnFbmjk1O4byESq1kZQvSJJPZ6ENlOiixGGUNn2TJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است! و این خونه عروس معصومه ابتکار است.  که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،  حالا نامه نوشته به مقامات آمریکایی که من عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6564" target="_blank">📅 09:06 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6563">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">این صدای عروس «معصومه ابتکار» است!
و این خونه عروس معصومه ابتکار است.
که با لحن تمسخر میگه اون پرچم آمریکا زده به خونه‌اش، من پرچم امام حسین،
حالا نامه نوشته به مقامات آمریکایی که من
عاشق آمریکا هستم و بچه‌هام حتی فارسی نمی‌دونن</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6563" target="_blank">📅 09:03 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6562">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74c1b28b15.mp4?token=ov_nNOUpJDpNbBRX-Uoh3BMJ0GavyB852puTzBn0AwKMcFkNRiyvCs-h-fR1cIl-o5FCQwUUR8wHBn141X19NkMrUHDa_SH4d9YoWmQ_rZJbYovE2f6dlx_PE6Qyo0wMtIn0djvHghx30AZP0cveox-qCsQYSisew5WzfWIKVnMsIm0MDisdyV1iXAFdNIT2GrKQknXGDVJpJcKnaRVaE7T6gJf7TciZmsebAMbCsFovJBcLi_yi26WBJ06mse2OYB6CoKB-z8rAbC6uiMEo9eEj7N_hAc-KWt7AdEG0tGWYWQhkmioFdwlGGDoKOa09ZRCDTSXcA7Twz-WeDAjEzQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نفت نمی‌تونیم بفروشیم،
راه دریا بسته شده.
چرا زدید زیر تفاهم‌نامه و حمله کردید به کشتی‌ها؟ که قیمت نفت بره بالا
و به ترامپ فشار بیاد؟</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6562" target="_blank">📅 08:43 · 24 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6561">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/farahmand_alipour/6561" target="_blank">📅 17:00 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6560">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2226555990.mp4?token=Uq7Codqnn94IKIUfzDovJzi0lbTSUJnkPtG0EWZ0KPQhuevcYfpXX5t4l-PBFgNnvg7T-cFBdya1aRWJqlwX23tPr2wgwoxt0ONBn-C1Zoc-nOvd7rsC63oKWV8lBch_-CKEMUfzW04pkc76sCH8zX0XhvbBpEpeSDCqgEYg_lcHGNd9GUebAOqelCLoZEolrYMOYm18vUt1x3G1e3k0lYVBooA1YA1gYlbbJkF65qg7eLLFAnZzGT25vRvyGIYTcNcDB6hsH_Re9iV1o1oWwfOSy-GurcanhsPfTB3vMSJeg7pLZrh-OrzArZYZX8HdGRZZ0lxtA7vvLDOQRkiMBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2226555990.mp4?token=Uq7Codqnn94IKIUfzDovJzi0lbTSUJnkPtG0EWZ0KPQhuevcYfpXX5t4l-PBFgNnvg7T-cFBdya1aRWJqlwX23tPr2wgwoxt0ONBn-C1Zoc-nOvd7rsC63oKWV8lBch_-CKEMUfzW04pkc76sCH8zX0XhvbBpEpeSDCqgEYg_lcHGNd9GUebAOqelCLoZEolrYMOYm18vUt1x3G1e3k0lYVBooA1YA1gYlbbJkF65qg7eLLFAnZzGT25vRvyGIYTcNcDB6hsH_Re9iV1o1oWwfOSy-GurcanhsPfTB3vMSJeg7pLZrh-OrzArZYZX8HdGRZZ0lxtA7vvLDOQRkiMBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">و تاریخ ثابت کرد حق با آرش و آرش‌ها بود!
فهم آرش از «شریعتی» و «آل احمد» و «هما ناطق» و «شاملو» و «غلامحسین ساعدی» و…. بسیار بالاتر بود.</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6560" target="_blank">📅 11:22 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6558">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea4168e97.mp4?token=lHbfrtiHPF2QIe2B99T7urWjjfZzBJeVjXjbmsLUktnf8sTXS4hVAUbI6VL-Muu4QGIoJxyD8cAS1B-Q17QjULJtBgZ9ilQjaR7yLnCNjJhIKRo99Kj-CS79qhT4S4qzNSRavvjhzXx76Y4tGQDJFz3tUJ7VpDyRO-0_NsnQ5Yrs8HHJNQYiNXHN4mOQD8vjfsOoRaj5faRILQcCBuDzx3cu6MuA1RHnMHDjKtx4xJtQDbFAyns5BBmOcWVJR5TFLTBCW5JASqsGYm2rUJVIx3VL58MFeOmZXHEDgRCYrT-uuCqEZAvw0JN7JpDHY_ntZe2eHVtWNJ1VCKUZ84bqGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب هیئت‌های عزادار چوبدار تبریزی و یزدی در مشهد، پس از مقداری عزداری برای امام رضا، همدیگه رو چوبکاری و سنگ کاری کردند.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6558" target="_blank">📅 08:42 · 23 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6557">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Hnfwcwnh95nDeVpDbp40pSKNq8PvWZ2s84Jt2P8tAI7wi1h3Zgm3vxTMkb7srlVz1pXJBkJQSrwDAQFBr-yP_KvDvNx7iw8GvqtpDMDjciRccVXmdYnPwHwne4VxHW_YXf8Dh7Rc57mF3Zm2WaGKfy7Rl8H6HBceLbLY6lNhjLOsG2PKZKUn9Gzq4R4PMVkm-zsJGOSWNoUbx7IZd8KgSHfZY86sUG1FNIHosDYM9Vy-MoTIMtE25jkYV6TlHwpv7ov_cqWjmDpZ2LAY5QkpfAcJ-Yy53lHM6LsQGryQmLWFLXP_DxNXYV-B1MQqaxaBi8leey_BmcvykGI4g42o1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08352cf997.mp4?token=Hnfwcwnh95nDeVpDbp40pSKNq8PvWZ2s84Jt2P8tAI7wi1h3Zgm3vxTMkb7srlVz1pXJBkJQSrwDAQFBr-yP_KvDvNx7iw8GvqtpDMDjciRccVXmdYnPwHwne4VxHW_YXf8Dh7Rc57mF3Zm2WaGKfy7Rl8H6HBceLbLY6lNhjLOsG2PKZKUn9Gzq4R4PMVkm-zsJGOSWNoUbx7IZd8KgSHfZY86sUG1FNIHosDYM9Vy-MoTIMtE25jkYV6TlHwpv7ov_cqWjmDpZ2LAY5QkpfAcJ-Yy53lHM6LsQGryQmLWFLXP_DxNXYV-B1MQqaxaBi8leey_BmcvykGI4g42o1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از نتایج حملات موشکی جمهوری اسلامی در تنگه هرمز،</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6557" target="_blank">📅 23:18 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6555">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=EPyNd5EQUJ9kISIvVAVgE7kTzElTkWRcaqvdevlTV-hiT3EPZ9gTiszFa1LW6nXCAjOnrxw8pr6eZS7DWIRfg0Fk_4JvtHQ3kWaYwL6ZoKOVsrezra0x5tbAhfY-ns5H33qAPbuStDd5P5q1glKUrrql3UbMWR3yYJXa1esbiFpIX-KuShGtLo1b0klX6ymrOE8_AT93oVbKvcXthPSkEZl0F5lOaIPbRF66yLkN7MZK3TOknQUHTKKO0B8yrRa_LN9uTWB_EZyx5nhgQ3Q_g9iuj_QyEZ5ObcaoyDp83Rw1Le-aNHGqSUW8Q1F643b0EZ42PYftw4YreXmN1N5lXA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c212d95b13.mp4?token=EPyNd5EQUJ9kISIvVAVgE7kTzElTkWRcaqvdevlTV-hiT3EPZ9gTiszFa1LW6nXCAjOnrxw8pr6eZS7DWIRfg0Fk_4JvtHQ3kWaYwL6ZoKOVsrezra0x5tbAhfY-ns5H33qAPbuStDd5P5q1glKUrrql3UbMWR3yYJXa1esbiFpIX-KuShGtLo1b0klX6ymrOE8_AT93oVbKvcXthPSkEZl0F5lOaIPbRF66yLkN7MZK3TOknQUHTKKO0B8yrRa_LN9uTWB_EZyx5nhgQ3Q_g9iuj_QyEZ5ObcaoyDp83Rw1Le-aNHGqSUW8Q1F643b0EZ42PYftw4YreXmN1N5lXA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک نسل دیگر ،  با بیماری و سوتغذیه در ایران بزرگ خواهد شد.</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/farahmand_alipour/6555" target="_blank">📅 23:17 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6553">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgvtS-tz4sDaIK0ZwDcZQwogYn3hL1ImyNykjJWtf37ty4I5tEc_36egJbPu1mS_GiHH8vVlv_zxKrxU-gaQR_6Ozj9kfdwfMxWsjDEguJ2F-80VUoRCGAl7wZEVmn2gWJIY2DCK0DoEnVbAunuh_B0192eGYvCzUN6F1NKUXnYN5XlJZdun4HUf-iHWVIsCTqlTzzBEL0oOIeQ0bvrjp4-QwRTsr7af-OycnTINKy_E67YKO8klSyhuEEYjw9BpAIXx8L-dW-kTbBcHefOmryf0PP_umTj4TVkcuQQVBjpJ_FMp68d1lWxySFwKPqTtO7zTK7o9ycJrL2cEw7sYcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6253088b91.mp4?token=SbEb_n3TlsZMIXutEXE7CAG_g-0nW8VozgPtUIqMaiyZXpuEnXPP1jrKXrFcI7Sxcvcev2HMVfCS-4L3TZKIDw_YEzOlWg6_9BDbZt3ThFEWC4OVqDAIQCbhZZoSuwTsg9-olCXlHs958HX8nmCTtE-T4r7ApyyQqadPKr5nGOkrLEywn0r4eYn97dtrw0f1lfwnbB_QACrLujUH1TtciQYogThn94qwAkI4yVV8IEUDPxuQKqNOzhkEi_rZtRVJ42PZ2RlSpTj6FL_h0GEoC8207ecK9Gq8cmzK_42uPbobF-DYdVx0HpAgmxSXfjYGjltGs5LVyWnMkiXqWu-5WQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6253088b91.mp4?token=SbEb_n3TlsZMIXutEXE7CAG_g-0nW8VozgPtUIqMaiyZXpuEnXPP1jrKXrFcI7Sxcvcev2HMVfCS-4L3TZKIDw_YEzOlWg6_9BDbZt3ThFEWC4OVqDAIQCbhZZoSuwTsg9-olCXlHs958HX8nmCTtE-T4r7ApyyQqadPKr5nGOkrLEywn0r4eYn97dtrw0f1lfwnbB_QACrLujUH1TtciQYogThn94qwAkI4yVV8IEUDPxuQKqNOzhkEi_rZtRVJ42PZ2RlSpTj6FL_h0GEoC8207ecK9Gq8cmzK_42uPbobF-DYdVx0HpAgmxSXfjYGjltGs5LVyWnMkiXqWu-5WQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتش اسرائیل در حال خلع سلاح
(محو سلاح) گروه تروریستی حزب الله لبنان
اون چیزهایی که دود می‌شوند و به هوا میرنپولهای ملت ایرانه که صرف خرید سلاح و تسلیح این گروه تروریستی شده.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6553" target="_blank">📅 20:01 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6552">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QBgTQPPsUTuSWKCgzomYwQeYjpWeICqx8UBYMkAvyiDECHxYceQKjSEsl38zn1xtzvQqT3pnyWBFIUQmGmdR4A3xdnDjuT4s9vIZB2oc39d6zpApx7ekmiF31oFp5Pp_SsNfVJZQOTD8KJljGYJwUEDN1fHOgI84vcrU3QV3u9iwOvyszFuuavxRFcKgz9fMGIvYnOHmOCzk5JiKCsyxAfzZ_MqT9BlJfsgIy5Z-svKl7m6TBC5lbx_5vfL1pE5Cd1Ozbx4aAj1an0xHktDdDAzt_9xbvIN3mKz36DziuksLWSIjT3jQ_p4RUZvmGiLtx-biuh8nP5uZycFW0iAK8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ظاهرا اون موشکی که زاکانی گفته بود دقیقا به خونه‌ مجتبی خورده بود و خودش از اهداف حمله بود، باعث ناخوش‌احوالی مجتبی شده و گفتن پول واریز کنید  زخمش خوب شه.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6552" target="_blank">📅 10:33 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6551">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🔺
آمریکا در آخرین هفته‌های سال ۲۰۲۵ (قبل از شروع جنگ ۴۰ روزه) حدود ۳.۹ میلیون بشکه نفت در روز صادر می‌کرد.
این میزان در ماه می، به رکورد ۵.۷ میلیون بشکه در روز رسید، یعنی افزایش ۴۳ درصدی صادرات نفت.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6551" target="_blank">📅 10:29 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6550">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.  جلوی دوربین‌ها وارد هواپیما شد،  اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!  نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6550" target="_blank">📅 10:28 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6549">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqJexvFXfZzJRu-pM6a9fZLCFdKuGL2-rxG_5RwxDFHjsWtsER8zldfQjPi0KAqGEsj88D59_XEU7-R9Mlq2UZgYubJIBrGrCeM7ketL1T-O1zdxs7mFIR1fb4yXFxJ1G7pOCrpc3XykLqXg6rjlyCctAs-NE4rVwLjuJ_RPnzZEuxSFMVzvnXG6K8kZ6-tTDEzXKTcYmQbhfCsH6jS7R0ovNmtQMw7bQ2Or5kIUDiCLCiYQmCmGpJcbInsFBvq7DZae2b_Z3b63l3T2HO_JH0FdCKJW7B9sEO6YnlogXgM3iScIRmajshqXRXydqbVUe4-y4KErnMSpZoQJjdQF-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لکه نفتی به جنگل حرا رسیده
و حیات درختان این جنگل به خطر افتاده.
اما این لکه نفتی که تهدیدی برای سواحل قشم شده از کجا اومده؟
جمهوری اسلامی ۱۲ مرداد (۳ آگوست)
به یک کشتی باربر (و نه نفتکش) حمله موشکی یا پهپادی انجام داد. کشتی داشت از آب‌های ساحلی عمان عبور می‌کرد.
پرتابه به موتورخانه کشتی «مینوان پایونیر» اصابت کرد و نشت نفت رخ داد. این لکه نفتی رو موج‌ها آوردند به ساحل ایران.
سخنگوی وزارت خارجه ج‌ا (بقایی) هم تایید کرد
که این لکه نفتی ناشی از یک کشتی‌فله‌بر است،
گرچه نگفت هنر دست خودشونه که برای بستن تنگه هرکز به کشتی‌هایی که در سواحل عمان حرکت میکنن، حمله می‌کنن.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6549" target="_blank">📅 10:15 · 22 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6548">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fFKgw27XiEw3yHcvBrnGXNZVGh4Z8Ge0zWCVUKwL45Y-MGL9fV6fgQj1KCWFx7IsX_GUDPUwQa9e1hV5EIPrsmXnRprwTMfixytIOPItr-B3f49qg3aGVMCyBE6szW3MecAu2LyHVt8FMy18efXkphAANStj2qM_e9PQUnEXWPiuSpxKzmLSZ-X7TyCH4JHcgzYwYttIpulhjTHJqJp_5LmudoLRWRqkdYKzXBKNCRK8fWw2kE_DiPjII0don_SxsNTg1kmSJeJJ0Xx0hQI-jaLPXB3vwj60j5G8GzUh_Ofq9ZAI_D_ElqBtJB9hpY0zMH814iBmWgT0QMxTXZ2-0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
بنزین در کرمان ۸۷ هزار و ۲۰۰ تومان!
میخوان آروم آروم و استان به استان
قیمت بنزین رو گرون کنن که بتونن
با تفرقه انداختن بین مردم جلوی اعتراضات رو بگیرن و قیمت بنزین
رو
۱۵۴۰٪
افزایش بدن!!!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6548" target="_blank">📅 21:54 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6547">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PdRpwbluNCc261dnlxUFGBQDhMiyvUd7s1m4gskDHIAvqMvWEQlqS-hrMMQNK6Vderl-BnXY97AK5bCwV51npM-hxOHOMVqHfO69PW1eRd-CuVj3GzKrEJCXKCqt1BvKZbdVPO20TYzescreNgXCvvxTwHEEJGiMbB9ObA9C32w-rLC5Gebe7DgErCKjQpWe_bLrbzhrETrqoT09l99Gmb0s0mkIC-5atSbx4_I9X_C3bJF7pyfK3GxUi7YKJsxTMGNzWpzUBKz5BAA0TFCAy7XFqpZZCgBW8Bj1hqwyJyl66kVVXIaHsWCY9HkspUfXNgRwWV2eauu1u4L_wd1zsQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زاکانی میگه : ۱- موشک مستقیم خورد به خونه مجتبی ۲- مجتبی خودش هدف بوده  ۳- زنش کشته شده!   اگه مجتبی هدف بوده و موشک خورده به خونه، قطعا همون لحظه مجتبی کشته شده!  اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید  که…</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6547" target="_blank">📅 15:30 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6546">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=YpZaoYdIUjZ3Yw29AmQauGVr7OA0r6nt4p92v0pr8-G_71bBk2KwsbhJbnOP8qlqR9Kuz1Q9fIf--UZdcLqdwZ9VDmVx4s-MLH_lBBQJP7A8ctHjFgehTz58tGR1l-BIHg86faVl1eill252qVE7msCxWJDSR0D7EkXnTxHpH5c8Oiz5-KPkcySRDnstGSKISy8xPeT0keegOKN8a0CrWZHKeSDJ7Kwwoi67UXul5jejQG6EOWcEjrfq8z0FD-QBx8eTmAiE-KDqK8t3g_ROI6HHfvAZ_v3oUQRSUIldXDqxdhZeq1aZwL8E9vx4rR79iFEsVTqEK9E7TPUUOW3J5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7024d4011f.mp4?token=YpZaoYdIUjZ3Yw29AmQauGVr7OA0r6nt4p92v0pr8-G_71bBk2KwsbhJbnOP8qlqR9Kuz1Q9fIf--UZdcLqdwZ9VDmVx4s-MLH_lBBQJP7A8ctHjFgehTz58tGR1l-BIHg86faVl1eill252qVE7msCxWJDSR0D7EkXnTxHpH5c8Oiz5-KPkcySRDnstGSKISy8xPeT0keegOKN8a0CrWZHKeSDJ7Kwwoi67UXul5jejQG6EOWcEjrfq8z0FD-QBx8eTmAiE-KDqK8t3g_ROI6HHfvAZ_v3oUQRSUIldXDqxdhZeq1aZwL8E9vx4rR79iFEsVTqEK9E7TPUUOW3J5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی میگه :
۱- موشک مستقیم خورد به خونه مجتبی
۲- مجتبی خودش هدف بوده
۳- زنش کشته شده!
اگه مجتبی هدف بوده و موشک خورده
به خونه، قطعا همون لحظه مجتبی کشته شده!
اینها فقط برای اینکه حامیانشون رو نگه دارن، یک اسمی انداختن وسط و گفتن بیایید شعار بدید
که دست اسرائیل (دست خدا) عیان شد
و خامنه‌ای جوان شد، ولی از قرار معلوم میخوان آروم آروم بگن که دست خدا، هر دو رو از زمین برداشت.
موشک خورده به خونه و زخمی شده  باشه :))</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6546" target="_blank">📅 15:11 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6545">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BVEL7rAGEuRjpqfqxhJY1-xwsbq-aPfxUbZ_Z0iHMzuF0NgIs6hJUs40rkH_EsOv41CH7HAlltOuZ2hrK28K723Ey3SrQZ9hzgJgtrjWZoFMJY6WrstkjBOyxC4VGSryVhgx_3pc9xaKgghdQELoAlNhFV_O7kTUNB2CoOuuAayaQz3vTKVfUYdcAwK55Ywy64HHWOTWCWStdKK-rJk3WkD1o8q6lQ7wl540VlpoNcP2rY2xIKXqS8RhhbUnkhnOQtYTAH4xgv9ULWXwjQczUY1egqgFuNkvSJi2-Axmv_Yg1wjZA1mJoVnE0VPxm67TjPW_780qNJNOFY1PMx7JCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شارلی ابدو
ایران - اینجا تمام سال
خورشید گرفتگی است.
(عمامه سیاه آخوند که مانع خورشیده
و کشت و کشتاری که پشت این عمامه سیاهه و روزگار خورشید گرفته ایران)</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6545" target="_blank">📅 02:18 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6544">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">‏محسن رضایی دبیر شورای عالی امنیت ملی:
‏آمریکا باید جنگ را پایان دهد، پول‌های مسدود شده ایران را پرداخت کند و جنگ در سراسر منطقه، از جمله لبنان و غزه پایان یابد
‏-شروطی دیگر از طریق واسطه‌ها به آمریکایی‌ها منتقل شده
‏-تا زمانی که همه شرایط ایران برآورده نشود، تنگه هرمز بسته خواهد ماند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6544" target="_blank">📅 00:05 · 21 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6543">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=o9TDZFijkESyronpLmt_bhpGfqShEIGg4iEYUzGB6AzlM4WsnHffnKbLnnLDrJ1P1WKemKGcixLlNPT3A4z5Y3UBUqkW8or7SSu52GsQg8gzNzIimNWvcBzCOYpaT3_js_nmyemw9MH6mghFLxbhzg05c7pqmWn2h9vPE1zFL7FSrcIInZyYh3i7VC_4k8PxCAoNsmT2sAAsrt7leur1ucR1arw8MgKS_U0YXDsGkpRz1iVVzRYPrGJSIWRBDUbD1H1yD_P4c4RTSJtkej8UEm8ainXVuEFUUteF3QPuZFmeRMZznIS8ImDHXmKN4PJZiu-7QR-CnEb7kqCkmLCV0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0b8763e605.mp4?token=o9TDZFijkESyronpLmt_bhpGfqShEIGg4iEYUzGB6AzlM4WsnHffnKbLnnLDrJ1P1WKemKGcixLlNPT3A4z5Y3UBUqkW8or7SSu52GsQg8gzNzIimNWvcBzCOYpaT3_js_nmyemw9MH6mghFLxbhzg05c7pqmWn2h9vPE1zFL7FSrcIInZyYh3i7VC_4k8PxCAoNsmT2sAAsrt7leur1ucR1arw8MgKS_U0YXDsGkpRz1iVVzRYPrGJSIWRBDUbD1H1yD_P4c4RTSJtkej8UEm8ainXVuEFUUteF3QPuZFmeRMZznIS8ImDHXmKN4PJZiu-7QR-CnEb7kqCkmLCV0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وقتی ترامپ در ترکیه بود اعلام کرد که با «ایرفورس وان» ترکیه را ترک خواهد کرد.
جلوی دوربین‌ها وارد هواپیما شد،
اما بعد از درپشتی خارج شد و با یک هواپیمای نظامی ترکیه رو ترک کرد!
نگران از تهدیدهای جمهوری اسلامی.</div>
<div class="tg-footer">👁️ 29.1K · <a href="https://t.me/farahmand_alipour/6543" target="_blank">📅 10:33 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6542">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b31726f423.mp4?token=cLao71FgWzdg4MG1mwuLaamkDSrlqqVULdaUq1hM4iGE9Ygq3BmGh4zzY4MsVuf57xkJMk21ZLvtOXfPjeqJAjcn1oG9awy-HUp7O1TZO0PJZFoUN_Yht71NE07zhXX3vXuKefoLvnCFo3RkeDlf-wK58LQNXXLz6AqrhtSsmmIMX1vbZ-FpTe0zTWsvQ0Vb83syHfmIopuQbn7R8kwvVF1Usl97atqiCxFQvPAYYz-K1udXcj2YN3PClyPq0Hxkp_5hBSt9L5ayYTACPL5ctPwU7W14o8nOETtcN8HEbcDFu_hNE9csZ7LxsTMa945VVMVcn-IuxmtD-iGCJSsi9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b31726f423.mp4?token=cLao71FgWzdg4MG1mwuLaamkDSrlqqVULdaUq1hM4iGE9Ygq3BmGh4zzY4MsVuf57xkJMk21ZLvtOXfPjeqJAjcn1oG9awy-HUp7O1TZO0PJZFoUN_Yht71NE07zhXX3vXuKefoLvnCFo3RkeDlf-wK58LQNXXLz6AqrhtSsmmIMX1vbZ-FpTe0zTWsvQ0Vb83syHfmIopuQbn7R8kwvVF1Usl97atqiCxFQvPAYYz-K1udXcj2YN3PClyPq0Hxkp_5hBSt9L5ayYTACPL5ctPwU7W14o8nOETtcN8HEbcDFu_hNE9csZ7LxsTMa945VVMVcn-IuxmtD-iGCJSsi9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عضو فاطمیون (نیروی شبه نظامی تحت کنترل سپاه ) در تجمع افغانستانی‌ها در ایران ؛
هر کسی گفت تو افغانی هستی به تو ربطی نداره بزن توی دهنش.</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6542" target="_blank">📅 10:05 · 20 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6541">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت: ‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.  ‏</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6541" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6540">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzg11khL7Uxo1t7rkfI1pFC5UhHhitTr0TtLFAdLUNm_HYgRZF4R5GX6O7jtX7wxyeGy3bQQHnNyzoK5VTqn6IPz75NSj655LltKxB32NIafygy3IXeNF4V8DqjcVV8kSczmCnAQR_IaKYOYWR3FjIzkrACf5LgdX6mXbsq6CWJhgcWPjmj2jwDv-93YE9B1M8armJVzZq_n9zIuOs5feaTCMBKTCvEVZ5PF7RbdF73mJC86xA_gNuOrxSUC2vLO-quefbjcJykZPhTXYM5D4N7x3_VRh6lmfFXztaqqBoKptDXSTv9RLd5T6ywfpSDeqzsEwGF5vOy9X6Sx0rbmpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ درثروت سوشال و در واکنش به درخواست جمهوری اسلامی برای پرداخت غرامت نوشت:
‏باید به خانواده‌های صدها هزار معترض بی‌گناهی که ایران در طول ۵۰ سال گذشته کشته است غرامت پرداخت شود، چه برسد به ۵۲ هزار نفری که در همین پنج ماه اخیر کشته شده‌اند.
‏</div>
<div class="tg-footer">👁️ 25.8K · <a href="https://t.me/farahmand_alipour/6540" target="_blank">📅 21:08 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6539">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIndyPersian</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMGpi75LVSDoguELbF02YLVQ6LVzsB1dGLoJpXWbWS3a4BIdpIDzEy-KXbAvzouThUud5r1IPhqaFvRJRCRx1tFP8wz43KjwrooJZxa3exygNAlLRGYmZ0A9cRExDu9Sxlv3oVGPhElmNGjsfRikL5Ihn43QzJ5PqfaZA05NQNxDg05VdKdhJvGqMOmn87W42CQYma9KDVMMtW2Orc1jj3i9yF-qy6CchNQP4JwZjChnpJkrOPw3DkynPjyt803lwA_lkCuIjL_3elTT1WlsldoeR2hPr2My0O2c_pswZ-m3GLLEOiKcdTxFh2JDEo0n1iL1d3sFw7Ju6XfbffzLmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">♦️
مجتبی خامنه‌ای با صدور احکامی جداگانه، شش تن از فرماندهان و مدیران عالی‌رتبه ستاد کل نیروهای مسلح، سپاه پاسداران و سازمان بسیج را منصوب کرد.
بر اساس این احکام، سرلشکر علی عبداللهی پس از کشته شدن سپهبد عبدالرحیم موسوی به ریاست ستاد کل نیروهای مسلح منصوب شد و سرتیپ کیومرث حیدری جانشینی او را بر عهده گرفت. در حکم انتصاب عبداللهی، بر ارتقای آمادگی‌های دفاعی و ادغام ستاد کل با قرارگاه مرکزی خاتم‌الانبیاء تاکید شده است.
همچنین احمد وحیدی با ارتقا به درجه سرلشکری به‌عنوان فرمانده کل سپاه پاسداران و سرلشکر مصطفی ایزدی به سمت جانشین فرمانده کل سپاه منصوب شدند. در بخش دیگری از این احکام، دریادار علی عظمایی به فرماندهی نیروی دریایی سپاه رسید.
در نهایت، حسین طائب نیز پس از کشته شدن غلامرضا سلیمانی، به ریاست سازمان بسیج مستضعفین منصوب شد. «گسترش فرهنگ بسیج، تقویت شبکه اطلاعات مردمی و مقابله با تهدیدات نوین» از مهم‌ترین ماموریت‌های محوله به طائب اعلام شده است.
@indypersian</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6539" target="_blank">📅 20:05 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6538">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RjPpW8K0Vs1Lh1Pc_o46AwqDzTHknKC12fX27_1S1VXLeFZkL_A_KQxKqoQ8CEWmic1eSC_t5hS04R5kwqzzVfAZwNuAyBWve9uROFCTUw4cUtLIrWm2qBYUbg86Ec8NClohiiBlY_lPXPGN53izaCEamTCKRQBznNdiS6I9KXspvZvgGOBE3KylbI3b2kFfniLbwYCE-RZpe0uXhCMwJyGvCetogq1AMAmQK9nU5P9tdLORpgaFZxfSbYNB8yID0YPCYtYy4WndxWUqavgSo6yhx9lmQlaJr1LsWElrSPttagLH5ULq-yGe0YL8O6mHRxRa4m_6TbH9QHitCCqH2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسکله بندر عباس
اصلی‌ترین دروازه وارداتی کشور</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6538" target="_blank">📅 12:06 · 19 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6535">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
شرکت ملی نفت ابوظبی از حمله موشکی به یکی از شناورهایش در تنگه هرمز خبر داد.</div>
<div class="tg-footer">👁️ 37K · <a href="https://t.me/farahmand_alipour/6535" target="_blank">📅 15:47 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6534">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=LWCJLOjyT91RKqRoLlsxfW9n7ltOqmKafYymBHsXzFPIFrjwyaj5XjeFZP3pZ-Lwwdz6PcZWOXiEfw_0clb9kreH2ifKNJmjJhQ9dv2d7bo1iJRilVDtyTtdcQvtQ6qOnDaF_9jEQI9_uYVj0hnVqVe8FbX4nEj7PcSi5k9VhcoNb1JUVGgS7rP_jUc280srn996sxoOSfhjMgNw7L3ALn5y8AfN2VPnvwjtru_ARx37olWRZMfreAe_DnAfW-ZslU9hjS5H2ywz8tGdygG-H4j_ZjZx6JszmMQQA6EKnnmLrZaShWpIjQxIpjXCkTKCWVt5dShZNS3arR51jonmyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6e0455e32a.mp4?token=LWCJLOjyT91RKqRoLlsxfW9n7ltOqmKafYymBHsXzFPIFrjwyaj5XjeFZP3pZ-Lwwdz6PcZWOXiEfw_0clb9kreH2ifKNJmjJhQ9dv2d7bo1iJRilVDtyTtdcQvtQ6qOnDaF_9jEQI9_uYVj0hnVqVe8FbX4nEj7PcSi5k9VhcoNb1JUVGgS7rP_jUc280srn996sxoOSfhjMgNw7L3ALn5y8AfN2VPnvwjtru_ARx37olWRZMfreAe_DnAfW-ZslU9hjS5H2ywz8tGdygG-H4j_ZjZx6JszmMQQA6EKnnmLrZaShWpIjQxIpjXCkTKCWVt5dShZNS3arR51jonmyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسماعیل کوثری :
‏سردار کوثری: شمخانی برای جلسه فرماندهان در بیت بسیار اصرار کرد
‏سردار رادان جلسه را نیامد و سردار پاکپور هم نمی‌خواست جلسه را بیاید اما دستور شمخانی برای حضور بود؛
‏وزیر دفاع با معاونینش در جلسه حاضر شد؛</div>
<div class="tg-footer">👁️ 40.1K · <a href="https://t.me/farahmand_alipour/6534" target="_blank">📅 10:23 · 17 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6533">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=sXOKxrp3XkkK-vKPlCyEB3gP5003WJfS7rBzfXEtPrPQt4_NK2SNca-v-0rZlVhM-wonCb1PPC_vIU_w6DORJPRUakuyfi2lUaa08yB0-gC6wkT_SEsP410Gk_fipkGeFPjowFcONbspojWXi47p4FLAUfHszjyZuOIRm_ipHvf3DmGW33t6arvrVDkPQob0Pzx-I8Mk-QXqAv4vV0Rz1HHHdCTax25fkK6uvMUCPR4gdv8dw1Ux1b7qSr8Ca4isi8cawPZr04VrBbUsmqHJyXk8okxWDndYVytRFM66OkAN7j18zwZMQXF1glCoX9GzsDckNumaNgbuP17B4iUFLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9163fd2da9.mp4?token=sXOKxrp3XkkK-vKPlCyEB3gP5003WJfS7rBzfXEtPrPQt4_NK2SNca-v-0rZlVhM-wonCb1PPC_vIU_w6DORJPRUakuyfi2lUaa08yB0-gC6wkT_SEsP410Gk_fipkGeFPjowFcONbspojWXi47p4FLAUfHszjyZuOIRm_ipHvf3DmGW33t6arvrVDkPQob0Pzx-I8Mk-QXqAv4vV0Rz1HHHdCTax25fkK6uvMUCPR4gdv8dw1Ux1b7qSr8Ca4isi8cawPZr04VrBbUsmqHJyXk8okxWDndYVytRFM66OkAN7j18zwZMQXF1glCoX9GzsDckNumaNgbuP17B4iUFLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حاجی‌دلیگانی؛ نماینده مجلس:
ما الان جز ۴ ابرقدرت جهانیم. نمیگم چهارمیم؛ شاید حتی دوم‌ باشیم ولی دیگه جز ۴ تاییم و باید توی شورای امنیت حق وتو داشته باشیم!</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/farahmand_alipour/6533" target="_blank">📅 18:01 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6532">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PNTQ1z8bLHSd2ckhSMtIpGrW4UIfkY2218p4lZbEpjpfCixchXV-eBUdkawpm0ZxWfTnAneEGhQvDGkWZxJdMynaPVG8-dLWIDvgB9ku-3M9zMIBB9kwl1qlM_uPHLvjvBTPyuDbKPfZwIq-F9o3KqUF3q1JSB5jWutjGJjC3Jwqy4UPdPzRJci6a2LgjhxX2feO89j1owL0VT_VWM-PEUmnaHLLVja5533toEUsC9bINg6Qdebuwzs3n1bXunPpaopVHZ6aU-Hqeog_yl8Kj72zwxoF44-dTKJt6_jAD0YUKiUMvp3Qw-PHr7wrAUdryNUQJDhYNU9bCmTCHlFvpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یکی دیگه از ریشه‌ها هم به این جریان برمیگرده  که پیامبر اسلام از نسل اسماعیله  و یهودیان جملگی از نسل اسحاق!  تمام پیامبران خدا،  یعقوب، یوسف، موسی، هارون، داوود،  سلیمان، عیسی، ایوب، یونس، دانیال،  ذکریا، یحیی و …… همه و همگی از نسل اسحاق هستند! پسر برگزیده…</div>
<div class="tg-footer">👁️ 34.7K · <a href="https://t.me/farahmand_alipour/6532" target="_blank">📅 15:14 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6531">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EkIo-QOnYScKP45m3XG0I7qvgVbMGe1NU6WBRdO9JV5PxadJPKB6xgj39GQQ9Wi05zuowheL2nXDciHCeOZlEw1PO923evHoJBSCGp-3p4ZQJ-HQ1_JKkYVDVnd-W8Gh1havbqIdiqvs-nDZ0f-e-TBb6OshSdrQeZCSEarUMDnwtavpWjw_ySqUMhx6dJFMx3xG9020CxD1WIMY3xHMitIay4Gt0-Wj1T6-TZRNvs-cCMwRjmA-nMFgP5YBibXd1w89Y8oN83j4pDsQcm3DE0gPaPj0jwrsK6KNKLvdD60oduROscCG4y1AVfuqO3dlUhiInjwHqaPCpcCggM8Z3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم در این آیه ۵ سوره قصص، هم در آیه ۱۳۷ سوره اعراف، هر دوبار  قرآن میگه که ما یهودیان و بنی‌اسرائیل رو تسلط دادیم و حاکم کردیم!  . «و آن قومی را که پیوسته به ضعف کشانده می‌شدند، [بنی‌اسرائیل] را وارث مشرق‌ها و مغرب‌های آن سرزمینی کردیم که در آن برکت نهاده…</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6531" target="_blank">📅 15:11 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6530">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">و شاید خیلی براتون جالب باشه که این آیه قرآن  (آیه ۵ سوره قصاص)  که خامنه‌ای برای  خودش  تفسیرش کرد،  در واقع قرآن داره درباره قوم یهود صحبت میکنه!  درباره بنی‌اسرائیل صحبت میکنه!  اینکه اونها رو از ضعف و بردگی در مصر به قدرت رسوند ! و اونها رو تبدیل  به حاکمان…</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6530" target="_blank">📅 14:58 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6529">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kueKy6-lsPHAMGQKHVRvlJFqt_oNt-8iAFc9JFVRBoXfMBKlBLKA2hopfH16dSkr2aVsA4ON_qIm1Myx1zAcRw-iXDSxsocuz3QtFlgn9Q-S27nP2D-OJRBZ8gsO6qxtmEGFyX_f597MVQtA7-ixReIH3ebHT1vEdwjLlXVJVCFClnOlstQ-pDbl-uY8e8R1KVVWbTLcKtX7eUp4Jht9JOLklRHxm0G7s10ilUHeFXAuySOcXvD4ByM91dFu9CIWSNpuQWAGc8CgCI0HBX-1uA6kQJvMSRLpOsq3oI-mRh__BB1RYeUhXq-9R9v8DmELebR5keRHdEhnADW9vct_EQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای در سال ۹۸  معنای «مستضعفین» رو هم تغییر داد و مفهومش رو از مردم مستضعف و مورد ظلم واقع شده رو تبدیل به معنای «پشوا و رهبر کشور» تبدیل کرد!  به نوعی گفت «مستضعف» من هستم و اگه میخواید خدمتی به مستضعفین کنید  به من و پسرهام خدمت کنید!  کفت قرآن اینطور…</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/farahmand_alipour/6529" target="_blank">📅 14:51 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6528">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yuq_CzhB81Caua8lsOgCwpRvutAGdgeM85w728StHX7ppVkAg1WXwACKpUhHWUU5dHNF7vZdGSTW01ZJVC1ruwFDxdEx9c5uCip2VlR8Kg_EY3csWZKxZT9M59k8xFfqRKWjHGaHu1G97NcNjhND23wZcKQAvSxP5OROYoejR89jjRTT0KPFYsRuREQx38VDjQL5LAM7mnuHUK6j7_nWzjzOckZI7mtH6DufHFcu3klJQWfEvbwiz7uSE3_V4K_plcHG2uW-r4PyYAyzhg1FX8ete2OCSKusZNFS8HQYW1YRVXBo-tindn5bCjzDaMQGC30AOkwFIIQc_6o5Qml1Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حامیان وقیح جمهوری اسلامی هم به مردم عاصی ایران از فقر و فلاکت کشور  دائم میگن :  شماها بیایید زیر پر و بال فقرای کشور  رو بگیرید، مدرسه و درمانگاه و….. بسازید،  به کودکان یتیم و سالمندان و….. برسید،  تا ما هم بخشی از ثروت‌های ایران رو یا خرج لبنان و فلسطین…</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6528" target="_blank">📅 14:43 · 16 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6527">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WjEQgLVIvk6aaEhAeIK1HzRba_iGI-f3NKNQcLUVTf7eQU0WoclIff7BVi-4Iqlb6QB21EKz6IKEn3JwBgGxT6r-v9ruPViW9XD7MyfD5UfSmQ1tr2lbT-NVZI1bM5AjN09qQNPx7Uk0UT__I8ffTqkSK4p7ee5NgrgJqnxuBbWX100QUlCaHGUgN65P7mNVsNASccB1mwYvr7fkh5uH1v6xmlLs72kPscOm9-2wmbEIaxCGVukcwpvKV5y-4iFdpZwyzCj1SQ22rNplMVaLDdOs7RQ5WpTdcUaolhfhYQFXepORTU_lsFraY-0Af8Tk_VXtpZnhmEdR-jzuGnTjKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اختلاس‌های ۳-۴ میلیارد دلاری!  خودشون  که هر سال یکی از اونها افشا میشه  به کنار!  بیش از ۳۰ میلیارد دلار هم در سرزمین سوریه ریختند و شکستی مفتضحانه هم خوردند و اومدن بیرون!</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/farahmand_alipour/6527" target="_blank">📅 14:34 · 16 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
