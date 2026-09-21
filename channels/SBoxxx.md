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
<img src="https://cdn4.telesco.pe/file/vwjiC215YbqQkyJUV1mMPSEWQV976Tmp5QPArP4xUnM0iFjEaEbsWGDUvsd2A4fmRIudEFhkAcHgxozmqWoNn_SJ9PU4oInEwxACsbPx8co0Yf7qtzOOxKTa9L3scnhbQ8D_F7s1z70IJ-RnwUaRznsjhOpoglfpcRAbg8MbInpDeTlcmIu589_UnNyr1xPvuzZsM7bMEkwjghi8BErWPsWZTngJNmhbG_He_LCc17WsVnwl6zGSqyVEi9cEW_KDYMFjQxbXHwyePVdm_OLW8mm86RMwqDmFpTqIkYFvF7iPUnc3YCg7hzjJL2z_XkwMmbja3V0H1BNWqAxg9imUUw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 Secret Box</h1>
<p>@SBoxxx • 👥 10.9K عضو</p>
<a href="https://t.me/SBoxxx" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 ■  تاریخ | ژئوپلتیک | بازارهای مالی ■https://secretboxxx.com/</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-30 20:59:37</div>
<hr>

<div class="tg-post" id="msg-21075">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/POUhsy3uJCgJV6hOshH1ojLyTCN5a3tAIKmgZeyrQLtLbV2hXVonE5xyqowI6nqT_3VdymvAxb72Nr0f3RXUpPSxROguxbD8o95rDmPhYJBq3ywM85PeyMi_Du_AyOIxq4poP8UN56Y_GEdb9QvqlEKyGWdA7FSty9lWJHVY65fGndg3rVFiRb1ryu3zvSeWC6vlCGWtqPXRA90MLl14RoZZ5SqcPlrnPu8ep4tDugVSCLYsVFXjV1Z7z5A8IEoOeTgqy8P2qJoA0TAkerS1gcEHWAelXvteUjDg-mzqrxxdxCCGGAl2gQCg1onYfPyZCeGN-2GbII1_q_80jz-0wA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !  فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!  اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 1.7K · <a href="https://t.me/SBoxxx/21075" target="_blank">📅 20:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21074">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 2.03K · <a href="https://t.me/SBoxxx/21074" target="_blank">📅 19:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21073">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZgSgmbJpRFGNNqXj2Qyi7MuYKpDNlcg_FpwhINYdN8BEz00Yh-i84lUbQ8c_HyMbCYGrR-cZRVGGaeP-p1Gq3dcxPXIk_ui_L9RTja4iXhdzBkkIH7EHrikIQac76iqixvMQuwiAAagkuwD8MmBFXBmuBEykkKXht45MooM4DPbzHkGtPOAtdRZsIwosKkKH17SHRyUimpM9kPX_g8W9bwRlmm5ZXIgYFaowkFGzEaXA9jrr8LemHPYQLntSEZG0xdNmBaW_ENb1YCVZ_k7Iri5JhREQZUUAkDG6PnaFd2POodQr2cFa-snyba2bV4ftjDYwjZelaF_dEbTRbSmIHQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اعلام وضعیت !
فکر کنید پزشکیان بتواند آن ماموت ۱۵۰ کیلویی را با دستانش خفه کند!
اینها شده اند نخبگان ما!</div>
<div class="tg-footer">👁️ 2.67K · <a href="https://t.me/SBoxxx/21073" target="_blank">📅 19:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21072">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">اظهارات جِی. دی. ونس درباره قیمت بالای بنزین:
به نظر من، همه ما باید این واقعیت را بپذیریم که تا زمانی که ایران در تلاش برای ایجاد وحشت در حمل و نقل بین‌المللی است، ما طبیعتاً تلاش خواهیم کرد تا در برابر این اقدام مقاومت کنیم. اما به همین دلیل است که قیمت بنزین اینقدر بالاست.</div>
<div class="tg-footer">👁️ 3.12K · <a href="https://t.me/SBoxxx/21072" target="_blank">📅 18:26 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21071">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RG5WZ6NL3idTOViiJEXeUOjW4kIVmHg-pNGH4Qil9Yo4E1NE7Byq5T3PFjwL2ZE2uxdgW_Fhp8PV9oir8vbywpstkyjtxlQ2NDnpjM9lrgsZirLQAS8dVcBCvW5T9UtB9Y-9iELkS9Sw-eo3R5NNUAD23Qh2DePUzP1Wq4et3Ef3Ryvsix1hWrem8QJcfmEOm4BuoayQjZCoYM0t75XfWw4M94NdySdv0s_S2kAgKMjczFBI0_PCrmqN0y7teZA-1VJi581EoKXqLwMOC5VA31s0vOmrjE7HUPdzmfRNNJxUJxUw2Vm6xZwIjIhDewP0eqx0uWjYj3vntbRGuzeBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 3.33K · <a href="https://t.me/SBoxxx/21071" target="_blank">📅 17:51 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21070">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">درگیری های سنگین میان نیروی انتظامی با جیش العدل در سراوان</div>
<div class="tg-footer">👁️ 3.63K · <a href="https://t.me/SBoxxx/21070" target="_blank">📅 17:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21069">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">رئیس خزانه‌داری ایالات متحده می‌گوید تمام خطوط هوایی ایران در ۲۳ سپتامبر «بسته» خواهند شد</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/SBoxxx/21069" target="_blank">📅 17:08 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21068">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">جان کیریاکو، تحلیلگر سابق سیا:
اسرائیل هزاران افغان را در ایران با ۱۰۰ دلار برای جاسوسی به خدمت گرفت.
کار اسراییلی ها اینطوری بود:
«در این گوشه بایستید و هر بار که این ژنرال را در حال رانندگی دیدید، یادداشت کنید و برای ما بفرستید.» بفرمایید صد دلار.
اسرائیل هزاران نفر از این افراد را استخدام کرد.</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/SBoxxx/21068" target="_blank">📅 13:20 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21067">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XiqBHizN7znU1pEOfK0GJgI2GEaD0XWcIi_lpVaUJJgHQsEker774sScC50u_05HOd_P2_ItwBLQ2g_BsNDO_Zb7HjlyGQFek2XDh7ZGeMTCE4E5hyXPVCItn2k5NWtG28KyaHcuDBQmBw5iWuFRbNIT1wVc1SnaUEbx1GEnelSS6fBTm8MV5BIKINOVxeJz3E7mGp78ZcIXVdLDeU4WMt8wC0PORjfLb0Gqdu3FRhONDZIQ4yrAQwJ8z6ANkXZ1iN8419kgsACMJcKhzaku2E7EkgfTsBmzrzX3hKwh0RrhEH1XUQoC7GqwOhzr6NTbHhnkIy8LdMbFOhFJ_7ielQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve
نمایه FVC در محدوده زیر قیمت منصفانه قرار دارد و لذا فضا برای یک رشد در طلا هموار است.</div>
<div class="tg-footer">👁️ 4.41K · <a href="https://t.me/SBoxxx/21067" target="_blank">📅 11:52 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21066">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EJgrsfgNohLPSNmEl-svHoXgv3UQemYXkaq2toixgTzd3yFYKmaP-KZyqoMQGj995HXdEKWC-nbLkMi_-5c6kXue4CiwC-mqCp0cbQQpVQjM3IuyUotnNU6sBDJYzm1xZAq8GE18MGsYFzU55sNDjIpw7-LPvDpJpJ28MHGPYOFja9_vppy8ix3xCiJ5A5kTmy5fJsPaoHERYN5bJUpreIo_xXDx15GZaYegjf8adnhmdre7n4i2_CwbIAmUHZa83rrPB4j43UophUjXpxdUlH6yxtAjQ0ToqGKsUGeA49doPxlImvlh1xLhmHAKVJQ7l-UNkbp0YIALPD2NMpuy2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#GRI
شاخص ریسک ژئوپولیتیک + تقویم اقتصادی برای امروز در سطح میانه ای قرار دارد و با توجه به افت بهای طلا، به احتمال زیاد دوباره حمله به سقف جمعه و حتی فراتر رفتن از آن را خواهیم داشت (یعنی بالای 4400)</div>
<div class="tg-footer">👁️ 4.37K · <a href="https://t.me/SBoxxx/21066" target="_blank">📅 11:50 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21065">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">قیمت متوسط گازوییل در آمریکا برای اولین بار از
۶.۵۰ دلار به ازای هر گالن
گذشت. از ژانویه ۲۰۲۶، سطح عمومی قیمت‌ها (موزون با شاخص بهای مصرف‌کننده)
۴.۸ درصد
افزایش یافته، در حالی که قیمت سوخت خودروها
۱۷ درصد
رشد کرده است؛ این امر احساس بحران توان مالی را تقویت می‌کند. دونالد ترامپ، رئیس‌جمهور آمریکا، تمایل خود را برای دیدار با سید پیش‌وا (پزشکیان)، رئیس‌جمهور ایران، اعلام کرد. با این حال، گفتمان طرفین همچنان منفی است. توافق آمریکا با دانمارک درباره گرینلند می‌تواند گامی مثبت باشد (بازبینی یک توافق موجود می‌تواند یک سابقة مفید باشد)، اما عدم اعتماد بین آمریکا و ایران اوضاع را پیچیده‌تر می‌کند.
مِرتس، صدراعظم آلمان، پس از باخت در انتخابات منطقه‌ای هفته گذشته به چپ رادیکال و راست افراطی، سوگند یاد کرد که در سمت خود بماند. به صورت ساده‌انگارانه، نگرانی‌های اقتصادی به نفع چپ رادیکال و نگرانی‌های اجتماعی به نفع راست افراطی است، و روند جهانی به سوی قطب‌بندی سیاسی پیش می‌رود.</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/SBoxxx/21065" target="_blank">📅 11:48 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21064">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UgAqa2JMgk8gtw2UzjjNokhmbBT_k8BPjQI3v7DF4Ox_XRBV0g2L3bwBFd4l0-zrkvxzmc3VBmUxPHrhVcPSbI15k2qB1EqLvVQ9M1wYBkvFTFMb3miv9aITbIxACFpE_fhBLWUwSN9Vh1ykQ9b-wD6jsJbfdj9N_LMxnmLDCHLL1TeePzj9bvTV3TIVSOFQsoAelPzaCXI6TozzTge9f8FaEZDbthmCE1Fo2TyBB7DBAexMMHN44eLl78KJzvxd7W3dX1gN7X2M-vZjEZGqwfPr48YI-4VKgDlgB4o_Y5BwoY7EdS1ZL9NaC3JZjD2ld0g7udPwosbhfUIE591Umg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چین میزان اوراق خزانه‌داری آمریکا را به پایین‌ترین سطح در 18 سال اخیر کاهش داد.
چین بیش از یک دهه است که میزان دارایی‌های خود را کاهش می‌دهد. این میزان از حدود 1.3 تریلیون دلار در اوایل دهه 2010 به 618 میلیارد دلار در حال حاضر کاهش یافته است.
این کاهش پس از سال 2022 تسریع شد، زیرا چین نگران وابستگی بیش از حد به دارایی‌های آمریکایی شد.
دولت‌های خارجی، خرید اوراق خزانه‌داری آمریکا را کاهش داده‌اند، در حالی که صندوق‌های تامینی و سایر سرمایه‌گذاران، خرید این اوراق را افزایش داده‌اند.
کاهش تقاضای خارجی، به افزایش نرخ بهره اوراق خزانه‌داری کمک می‌کند. نرخ بهره اوراق 30 ساله اخیراً به بالاترین سطح در حدود 20 سال گذشته رسیده است. افزایش نرخ بهره به این معناست که دولت ایالات متحده برای استقراض پول، باید مبلغ بیشتری پرداخت کند.</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/21064" target="_blank">📅 10:37 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21063">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">ملونی ممنوعیت پوشیدن بورقا و نقاب را در مدارس ایتالیا اعلام کرد
«هیچ‌کس در ایتالیا نمی‌تواند تصمیم بگیرد که یک زن جوان باید خود را پنهان کند. برابری بین مردان و زنان نه در خیابان‌های ما و نه در مدارس ما قابل مذاکره نیست»</div>
<div class="tg-footer">👁️ 4.5K · <a href="https://t.me/SBoxxx/21063" target="_blank">📅 10:06 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21062">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">اقدام بی‌سابقه دولت الزیدی:
یک “عراقیِ ارمنی‌تبار” سفیر عراق در آمریکا شد.</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/SBoxxx/21062" target="_blank">📅 10:01 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21061">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hqgcr5PWQPPXA0zKvwrpLIZDCrMYRPbir-rXHyvp_RrKE041istFZqZWTm0fzjILh0oYwnyxeBGCO1RsvgtGd6X7LPWAcv2kAYc710dfdio8rtjAikSXZMguqpyhCianznb3tOiLUa627qP-F5_WEf9vzwnG3nDuJFslJy8kF3D2tAqUMvQXNpRb06Toieb0__x6mYfCZrVQe5OI54yZ4IgMC_NwYWKTG9O9WPXgM8yO9X6sp1LYY7fXOWHUC5cZHb1-FXt8YhDseVmpC7X_JLlKzX2AKLEstQ_eiaENW9y2_NXyuLKvKresrgKPR32j2Hodgudfl4ffTyhjpP7lVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21061" target="_blank">📅 01:42 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21060">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">یعنی همه چیز دیدیم جز قهرمانی....
هعیییی</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/SBoxxx/21060" target="_blank">📅 01:35 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21059">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21059" target="_blank">📅 01:34 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21058">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=m-NaQ61a9y2MLpTrElDB6XgydWnpOnxp2In9qMJG7RDuigYgROOQK_iTnDKSGMIUZAAkByUu87r8o2OZKi-YkxjS6A_LBxfvTAbhaa6deo7dvaJmZtqovlWfSzA5P1kZbderXjDIyFl6iGhKsnt4mWoDBLKnLyVUMMawf9KDq1vz0hP5Bv1sy5bt_oj9GX2rT84Gvj_4mHvFTP3VlYH4o2E8jvd_q955JCP_xtlumnAhgtpBosZFSfeB8q_k0OrUQJQSZNZVWR_ZmOD1BzVe1TDtki5n098FcuHsY4albuHDoeQiJh32qlXQawKmUn8nIVvbU5SI1Yvdcg3Wii-g_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b9e029fb89.mp4?token=m-NaQ61a9y2MLpTrElDB6XgydWnpOnxp2In9qMJG7RDuigYgROOQK_iTnDKSGMIUZAAkByUu87r8o2OZKi-YkxjS6A_LBxfvTAbhaa6deo7dvaJmZtqovlWfSzA5P1kZbderXjDIyFl6iGhKsnt4mWoDBLKnLyVUMMawf9KDq1vz0hP5Bv1sy5bt_oj9GX2rT84Gvj_4mHvFTP3VlYH4o2E8jvd_q955JCP_xtlumnAhgtpBosZFSfeB8q_k0OrUQJQSZNZVWR_ZmOD1BzVe1TDtki5n098FcuHsY4albuHDoeQiJh32qlXQawKmUn8nIVvbU5SI1Yvdcg3Wii-g_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن یک هواگرد ناشناش در آسمان تهران امشب</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/SBoxxx/21058" target="_blank">📅 01:32 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21057">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=cNRl1AUCDPk3ynUPi4TuY6DZqc3KUEYSksCaSZfcFF1O6NM3dLevw_Dh-4sbmur_S6AQ5Q8bPW5OYgmZyjMm3Wkwfc9ruGAY17h3GHBnzeqwvJZ4zJwlG-qBO0XoJbZm_K678kXjyViYWoDhntFNzHJqx6fsaJhEo36ij2NlXSCWUJ2Z2xVdqfv6Fb1j-yEXYsASebq1LLyTeWBsvj8BomakApbJVkL4MwWDVjcT1IIZmeEg0aw8Q_kUAqCCDq9dRS-3tYxRKJ8I92TiYVfGqmwDGfpyEqFS-qZa_8rCX9IsORma2BGSLztWwCVdcO3Fh_Kctvs0aUJlwBg--1W0vA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/304c99ed1e.mp4?token=cNRl1AUCDPk3ynUPi4TuY6DZqc3KUEYSksCaSZfcFF1O6NM3dLevw_Dh-4sbmur_S6AQ5Q8bPW5OYgmZyjMm3Wkwfc9ruGAY17h3GHBnzeqwvJZ4zJwlG-qBO0XoJbZm_K678kXjyViYWoDhntFNzHJqx6fsaJhEo36ij2NlXSCWUJ2Z2xVdqfv6Fb1j-yEXYsASebq1LLyTeWBsvj8BomakApbJVkL4MwWDVjcT1IIZmeEg0aw8Q_kUAqCCDq9dRS-3tYxRKJ8I92TiYVfGqmwDGfpyEqFS-qZa_8rCX9IsORma2BGSLztWwCVdcO3Fh_Kctvs0aUJlwBg--1W0vA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مستندی جالب از روند ساخت و امکانات شهر موشکی یزد!
بخش عمده اش به نظرم با واقعیت همخوانی دارد اما در بخش هایی از تخیل استفاده شده مثلاً بخش مربوط به نمایش طبعیت و روز و شب برای کارکنانی که 500 متر زیر زمین حضور دارند.</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21057" target="_blank">📅 01:25 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21056">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d9AII-bhifzApD9vBTUbwMPwz1503nWYWZeIw6XoKL3_yVq8WCZkCfF0a--7uk_QD6lDnoTJnBTU88ErA4P93gZBXnwvlEDxzwDSMi2jA7UWAVzFECQS-o3zg-U4MriXh6HMxjI04tTqScNeGemSSeck4QtOiRPF66BarDOG3cANwcdoNqHgw-o4qG3twiMoCYEp2VfIk38aFtodEuYcTx8aGrq_NS6s5zpEqiCkXFFpvXGYBBxLrLfZogutJIaDpWRLEChNJh-wkX_2M_mNRSsz7tiQJcTP_edMKVC2Pwbiw-mBUqYI27pjyrXIOjD8VRNUhk4ueUquwwK-bFInZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21056" target="_blank">📅 01:16 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21055">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم  که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21055" target="_blank">📅 00:15 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21054">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7235f04196.mp4?token=KDKrpIJNCc7opdWc4UiA0FISha9q2OcVpu4C5b8jEgATv9J3FBfHO0n4x2Z_UCRCupRmptQEHHOzF_hcsXu4M7YbsFi_97gFymThmmxUS6D5j7SN8Gw3ghjyQNFTGhTvNjjS2ChKVWwvb8FnQSZeWP3i5sNhz6kmFrWwgxJIOogGZVfPP-kI3108QGwVtUHGjTZnfkhx3yJYu8bPx1CRa7t-mmVoivH7ZTUwquLdEjz-66IV2KGh_oDLzwgHgy2Iw7sYAIYrPMtlsDj8aXGqzZwURFeYYvLdC7utFa0meyGi6gOPPvXf4_F8RdVELEuSzVgB_xGaac4mShgYmCc6WA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7235f04196.mp4?token=KDKrpIJNCc7opdWc4UiA0FISha9q2OcVpu4C5b8jEgATv9J3FBfHO0n4x2Z_UCRCupRmptQEHHOzF_hcsXu4M7YbsFi_97gFymThmmxUS6D5j7SN8Gw3ghjyQNFTGhTvNjjS2ChKVWwvb8FnQSZeWP3i5sNhz6kmFrWwgxJIOogGZVfPP-kI3108QGwVtUHGjTZnfkhx3yJYu8bPx1CRa7t-mmVoivH7ZTUwquLdEjz-66IV2KGh_oDLzwgHgy2Iw7sYAIYrPMtlsDj8aXGqzZwURFeYYvLdC7utFa0meyGi6gOPPvXf4_F8RdVELEuSzVgB_xGaac4mShgYmCc6WA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واقعا تا حالا کسی رو ندیدم
که با این جدیت کصشر بگه
😂
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/SBoxxx/21054" target="_blank">📅 00:14 · 30 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21053">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gaRn730FVlq7BOC8iJj_QF6Vs6tAEZlBt4UJ4btxrq6MiV1GfUKobjtVJ402EFJycSGcwi1TdED7xM0r4xQQ7qnJx8fJphBuFji-1viyGbSWc0WmRiDx0x-033GcQYRA6EPVlg-0r5RdPeiK4cVl4kSlyWbevnZUe5FtgXKR52A0r0A0qosVqGxT5NDcJJVfmvQt8V_cIFzzJ7efdG_Mq28bwTeQwcVJgxSnzuVlXuxn8RNhBtoK9Hl0bqfpNDYMcwTiDnsER3NI4lwI92BrX1grxp4h1eB2YAyQj31q6i_1Mq3yixEl872vHf0zeAyoP22CQA6pT2f1658K6n1EtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21053" target="_blank">📅 23:49 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21052">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.4K · <a href="https://t.me/SBoxxx/21052" target="_blank">📅 23:34 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21051">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MYUfxZ4JLxe4lMDiD9zcfLiFVn2cQN6gJ5L0HMz1HOKGSvgkjz55AWPt6j7ZP0vHpWE5mywf1gAzAlCykirCdWYkBsfCeBR5FZVRcih_a_rSdHZ1h70de41iSfHlV1rin8tB0VrqTtrlnS1gBgYs53VTGZm86uVVZDyelrS98XLb7eQZPu-mjlRJO_fM_zWv2mA4st1KvbW_4voOHBXsSqDsmPhGbJgkALG1cIlVFM_q2SlYup6fL_Gpprn9q9RLD4-85wTX6F6e_AQ-y8-rdo1jpz9sc1CHGU0ZHtC9pf3xtL_WMh9p40BOH-r6rDS1uYscPqCJ2vZG4glMA6uSMA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چارت نفت جوری است که به نظر یک کاهش تنش داشته باشیم و دیدار شی-ترامپ مثبت باشد.</div>
<div class="tg-footer">👁️ 5.22K · <a href="https://t.me/SBoxxx/21051" target="_blank">📅 23:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21050">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حریم هوایی اسراییل هم بسته شد.</div>
<div class="tg-footer">👁️ 5.77K · <a href="https://t.me/SBoxxx/21050" target="_blank">📅 21:24 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21049">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dn0GpDSwPAhYWYfHnyThJtPLYheC9rfV6JOYIW6FqdkD8EjPByyd65OsJvEKgwBQjOzmziyaNmJPtqViSByJexH7LrHZiEwBFPpbMFsNioxXh4FDhRwlENsg-0xhTsxHi_F2J-_o_n-Md2pb1pGhHR_psxDCCvpo3a2QCgyg8PIIsP7VHcAqSPaPuukvkJu5XfEb807qB3nmQcjTzvzMkEGk6-NpiGp5vf8v_dyE-8DGDMkenYhDcRRLZsTPau_N5amiDjqKT8VrayzRcEVF31Y3cPBqQXV1gxATHOhDKZiWkb54AG_rzHtIUTkPHixvsfYriFZF_rV8rnceCXX2dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پزشکیان:   صلحی که دشمن تو را به آن دعوت می‌کند، نباید دفع کرد</div>
<div class="tg-footer">👁️ 6.27K · <a href="https://t.me/SBoxxx/21049" target="_blank">📅 19:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21048">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">قالیباف:   هم میجنگیم هم مذاکره میکنیم</div>
<div class="tg-footer">👁️ 5.95K · <a href="https://t.me/SBoxxx/21048" target="_blank">📅 19:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21047">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین  شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.  در بلندمدت، اختلال پایدار…</div>
<div class="tg-footer">👁️ 5.44K · <a href="https://t.me/SBoxxx/21047" target="_blank">📅 18:52 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21046">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M8Ufp4HGDu3YiR3UlpS8syhaF2PIafmeCnqtKjV7A-2QAD9sWklodykjDSyq5Vdpe_HTAq6-AAF4jVSC4wKmVdAOG6wbxXRhO2Ygs0GHA8bnESvv87_uGKLwQPqDLqPw9hYyhnpVQe8sWbg9MRFZjXka9wpIxLpSp2uh_YZcn_5z4-J75QtFCPdi0uIPjOmYd685OPqYh77ClFQ6ChQNemFHC7ufPHP-EaE1ruRgJXlRjXa1m-kPDodPNDGReIMoiXfLNexKzZv3y8b51L5XdwghZ39PE7BSMw5HG2TQsQRrLQrn_Js7jlWInwJ7eb4Al9gtN6cCPgpj2rpy0rppcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
تخریب تقاضا در بازار نفت و انرژی های جایگزین
شوک عرضه نفت در کوتاه‌مدت قیمت‌ها را بالا می‌برد، اما تداوم قیمت‌های بالا با کاهش مصرف، افت فعالیت اقتصادی و تغییر رفتار مصرف‌کنندگان باعث «تخریب تقاضا» و کاهش فشار بر بازار می‌شود.
در بلندمدت، اختلال پایدار در عرضه می‌تواند سرمایه‌گذاری در خودروهای برقی و انرژی‌های جایگزین را سرعت دهد و وابستگی به نفت و اهمیت استراتژیک آن را کاهش دهد.
🔗
ادامه یادداشت را از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/SBoxxx/21046" target="_blank">📅 18:50 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21045">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">ترامپ به فاکس نیوز:  برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21045" target="_blank">📅 17:38 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21044">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ترامپ به فاکس نیوز:
برخی از مقامات ایرانی مانند موش‌ پنهان شده‌اند.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21044" target="_blank">📅 17:35 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21043">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.18K · <a href="https://t.me/SBoxxx/21043" target="_blank">📅 17:20 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21042">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.09K · <a href="https://t.me/SBoxxx/21042" target="_blank">📅 17:14 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21041">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:   گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی #إيران، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21041" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21040">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ترامپ به فاکس نیوز گفت:
گزینه‌های فعلی که در حال بررسی هستند، عبارتند از: نابودی
#إيران
، یا اجازه دادن به فروپاشی اقتصادی آن، یا رسیدن به یک توافق.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21040" target="_blank">📅 17:12 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21039">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">رویترز:  در این ماه، ایران فرماندهان سپاه پاسداران انقلاب اسلامی، مشاوران نظامی و تجهیزات مربوط به موشک‌ها و پهپادها را به یمن تحت کنترل حوثی‌ها منتقل کرد.  یک پرواز شرکت ماهان ایر در تاریخ ۱۳ جولای از تهران به سمت یمن پرواز کرد و بین ۱۰ تا ۲۱ نفر از پرسنل…</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/SBoxxx/21039" target="_blank">📅 17:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21038">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">پوتین:   رهبران اروپایی در روز های گذشته به صورت آشکار اعلام کردند در حال آماده‌سازی برای جنگ قریب‌الوقوع با روسیه هستند.</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21038" target="_blank">📅 17:00 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21037">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">قرارگاه مرکزی حضرت خاتم‌الانبیا:
براساس اطلاعات دریافتی، آمریکای جنایتکار .... بار دیگر تصمیم گرفته است با چراغ سبز برخی کشورهای منطقه، در نشست مشترکی در یکی از کشورهای اروپایی، اقداماتی علیه ایران اسلامی را از سر بگیرد.
هشدار می‌دهیم چنانچه آمریکا علیه ایران اسلامی خطایی مرتکب شود، تمامی مراکز استقراری و منافع آن کشور در منطقه، بدون هیچ‌گونه محدودیت و ملاحظه‌ای، هدف حملات مستمر، موثر و دردناک قرار خواهد گرفت.
اخطار می‌دهیم چنانچه کشورهای منطقه با تداوم سیاست دوگانه در قبال جمهوری اسلامی ایران، با تجاوز شیطان بزرگ به ایرانِ اسلامی و مقتدر همسو شوند، همگی در این شرارت شریک تلقی شده و دیگر نمی‌توانند از نیروهای مسلح قدرتمند ایران انتظار خویشتنداری یا نجابت را داشته باشند.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21037" target="_blank">📅 14:58 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21036">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فایننشال تایمز:   عربستان از برنامه تحت رهبری چین که بخشی از تلاش‌های پکن برای ایجاد یک نظام پرداخت فرامرزی جایگزین دلار است، خارج شد</div>
<div class="tg-footer">👁️ 4.97K · <a href="https://t.me/SBoxxx/21036" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21035">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">این هم پاسخ ترامپ به چموشی سعودی های مفلوک در نپیوستن به پیمان ابراهیم و در عوض دست نیاز پیش فاکستان ورشکسته و عثمانی مقروض دراز کردن!</div>
<div class="tg-footer">👁️ 5.2K · <a href="https://t.me/SBoxxx/21035" target="_blank">📅 14:55 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21034">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">قالیباف:  جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/SBoxxx/21034" target="_blank">📅 13:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21033">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">این تناقض را نمی‌فهمم:   از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،   و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.   آمریکا دشمن خونی…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21033" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21032">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRaefipourFans</strong></div>
<div class="tg-text">این تناقض را نمی‌فهمم:
از یک‌سو ناامنی در کشور تا حدی است که رهبر حتی نمی‌تواند یک پیام ویدیویی منتشر کند،
و از سوی دیگر امنیت در نیویورک آنقدر تأمین است که رئیس‌جمهور و مقامات وزارت امور خارجه بی‌دغدغه در خیابان‌های منهتن قدم بزنند.
آمریکا دشمن خونی است، اما با بعضی‌ها‌ کم‌تر؟
✍️
پسر سوم‌ خانواده تیبو
@raefipourfans</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/21032" target="_blank">📅 12:56 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21031">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">قالیباف
:
جنگ بعدی ناوهای آمریکایی را در هر نقطه اقیانوس هند باشند هدف قرار می‌دهیم!</div>
<div class="tg-footer">👁️ 5.16K · <a href="https://t.me/SBoxxx/21031" target="_blank">📅 12:47 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21030">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KvtGHWsydjjyVyiEx_6gotU-MP17ZCwCRTLvuR9H3krR_VX-oZl9iN4Z8Uj6sSRFv8Rmnact_8O5lDkBe92WMj75m-8-CKCoPWOGrwMvYxesolTWwUh7poS5bOhnkIBjh2HcaPEbOC2qKlh_Ig_ZPjmzamReJjO1Rz1N2_OwKxQC7dl1NyEQelrJAJ2qaI_N5vKXbu8h_doEvWBQk4iuDUudRF7cuX1uU22Q3aWtl-teLbe6XEu_kVlq1jRMEB8_2Y-NcOsblc240crCHErmtiPxn2G1D91YppBvobUiquQlGWYrkUrPnpNKlnsfYXfjOZxaYAiV-NPhrsmEo-BQJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.13K · <a href="https://t.me/SBoxxx/21030" target="_blank">📅 11:07 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21029">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">کانال 14 اسرائیل:
آمریکا گزینه‌های حمله احتمالی به یمن را بررسی می‌کند</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21029" target="_blank">📅 11:03 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21028">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lzoVrl37AquKupvUDqCnUTbMtVRcqj5qyBs7SlDHZP5ZEvDC2dBOjtbJCkqyYWx_swGaRR9sBi0DLzlL-8ieAIc7GGrQYikeHSYi1cGVbefVw6hkSYTsCE_M--KuLcgFcaUZ8d0WYXstsX6tXRS06jHojZ2OL3EKQViecFm7nI1HCq_17HdOxQbv9K49NyXkZtWb84tHyN1IOHlIxzb5ZbrR5tZp6GHSscnx5ci7KDo965qKJER_kWP5m6RAgPxdRqB0ooaS8wSOyhHKmURBJ1TFkbgv_kg0mwFxKPwr5qtOijMEnj5diaVniTE84rIgtUok4UdFl-IWr0e4pY1gjA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.  یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.  ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون…</div>
<div class="tg-footer">👁️ 4.91K · <a href="https://t.me/SBoxxx/21028" target="_blank">📅 10:26 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21027">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">یک حمله پهپادی گسترده در طول شب به مسکو و منطقه مسکو، در روز پایانی انتخابات پارلمانی روسیه، انجام شد.
یکی از برجسته‌ترین اهداف، پالایشگاه نفت مسکو در کاپوتنیا بود که صبح امروز آتش سوزی بزرگی در آن مشاهده می‌شود.
ظرفیت پردازش این پالایشگاه حدود ۱۲ میلیون تن نفت در سال است.
آخرین بار در ۱۶ و ۱۸ ژوئن به شدت مورد حمله قرار گرفت، زمانی که هر دو واحد اصلی پردازش نفت خام آن آسیب دیدند و پالایشگاه مجبور به تعطیلی شد.
تا ماه اوت، گزارش شده بود که توانسته بود تنها با حدود یک‌سوم ظرفیت خود مجدداً راه‌اندازی شود.
اکنون دوباره مورد حمله قرار گرفته است.</div>
<div class="tg-footer">👁️ 4.88K · <a href="https://t.me/SBoxxx/21027" target="_blank">📅 09:11 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21026">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromپیکنیک تحلیل</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=dj82iOU0Hw-3878L-qlcpiNTnWgXsDY8Ci1U6N1IlvzE63zQEiHYOTgTanVfpG3OCeEE6KzCU2-PbF6zthoKuR7xASvLHUqIDB_gZioOgo1r7thdojgYTupbpI8WMfHCOIQHCOfvsbsPjGcbL0szU5P6GmGD06qEol9tiUgg-so8pdpLyTVXEALul0BGND33Y5oiVV2-yvG8v-mXUvd5352QJPR-IJoEGZ8GMkreI6hqphK5l2TIq629bcpCJdWRywyURUxQ-PrnSHbPB3YJIwZ6S4ZwmB2SnxjRXrvgKYcrB5eM77AFcLXHBjZzQZllpdF-Wce3IhKGROeKZbe_9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4607a666c6.mp4?token=dj82iOU0Hw-3878L-qlcpiNTnWgXsDY8Ci1U6N1IlvzE63zQEiHYOTgTanVfpG3OCeEE6KzCU2-PbF6zthoKuR7xASvLHUqIDB_gZioOgo1r7thdojgYTupbpI8WMfHCOIQHCOfvsbsPjGcbL0szU5P6GmGD06qEol9tiUgg-so8pdpLyTVXEALul0BGND33Y5oiVV2-yvG8v-mXUvd5352QJPR-IJoEGZ8GMkreI6hqphK5l2TIq629bcpCJdWRywyURUxQ-PrnSHbPB3YJIwZ6S4ZwmB2SnxjRXrvgKYcrB5eM77AFcLXHBjZzQZllpdF-Wce3IhKGROeKZbe_9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت امروز من در بازارهای مالی
@PiknikAnalyst</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/SBoxxx/21026" target="_blank">📅 09:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21025">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=f1wND1rCpubsIUO-4rBzGySw_nQT0xFmEeebSO94AZ_KcMRzzm5LPkhqd_VvbuNZN9_x9KBWoiW-X-Z0k9pjXIftC8goGYQ615AZFjXPhZnqmmgMHz4748ep5hVQDXo8t0knT0vLg2E0UZvu3YvtBNwHsVgtsR-71yOxX85_u4MFrFdqdawfPEoISOt_CCBXc930_2_ONeeGF4C2jxQgjfKw51ZMLtmfTHLKoNtKrv53greplmmZTep6aMetQjR2tYPpKDVZ2l2C93dzOF3_-pgA-p5T_xMuIPEbJ6Y36ir1_G-zrZK9GH82HGr-Fq7Q-1SVQVnMMciSnCeohkVxMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9d8265c9ad.mp4?token=f1wND1rCpubsIUO-4rBzGySw_nQT0xFmEeebSO94AZ_KcMRzzm5LPkhqd_VvbuNZN9_x9KBWoiW-X-Z0k9pjXIftC8goGYQ615AZFjXPhZnqmmgMHz4748ep5hVQDXo8t0knT0vLg2E0UZvu3YvtBNwHsVgtsR-71yOxX85_u4MFrFdqdawfPEoISOt_CCBXc930_2_ONeeGF4C2jxQgjfKw51ZMLtmfTHLKoNtKrv53greplmmZTep6aMetQjR2tYPpKDVZ2l2C93dzOF3_-pgA-p5T_xMuIPEbJ6Y36ir1_G-zrZK9GH82HGr-Fq7Q-1SVQVnMMciSnCeohkVxMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی از حمله موشکی دیروز حوثی ها به فرودگاه ریاض</div>
<div class="tg-footer">👁️ 5.15K · <a href="https://t.me/SBoxxx/21025" target="_blank">📅 09:05 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21024">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=ABT_pTlbhm2yu2zYJNS0eyTQ7eiyQMj73MXKXa_H0vPoiMJLQsOm-UF72Z33Nk8n0E_MZa8PX3sWFXiJ1Wa1vwu3rlnWxowvnzjt9FXE7-OJAt6pTcXpj_mEqXyCVHbyjbXKrS0VUJ4wiBOKGHF3I5Tm0ceubva5O-pUh_va3auroXgQaKTnreLW8_w9wHMrSNmO6tMxHejl5xXiVxosRBGXOyHmgtW0k7xWw9kyCsIRTtXGyaC2rCTicU0IfOSF8dtYEy03Vr7E3wohUFVciwyda485TSwQMjOx0qOV4ZntXnXv8nYKB-VQv7uTFRzy41qpuQN1zG9g_Sh3VL_GmQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ecd762d60c.mp4?token=ABT_pTlbhm2yu2zYJNS0eyTQ7eiyQMj73MXKXa_H0vPoiMJLQsOm-UF72Z33Nk8n0E_MZa8PX3sWFXiJ1Wa1vwu3rlnWxowvnzjt9FXE7-OJAt6pTcXpj_mEqXyCVHbyjbXKrS0VUJ4wiBOKGHF3I5Tm0ceubva5O-pUh_va3auroXgQaKTnreLW8_w9wHMrSNmO6tMxHejl5xXiVxosRBGXOyHmgtW0k7xWw9kyCsIRTtXGyaC2rCTicU0IfOSF8dtYEy03Vr7E3wohUFVciwyda485TSwQMjOx0qOV4ZntXnXv8nYKB-VQv7uTFRzy41qpuQN1zG9g_Sh3VL_GmQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 4.87K · <a href="https://t.me/SBoxxx/21024" target="_blank">📅 08:33 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21022">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">ترامپ می‌گوید باسن ملانیا باعث «نجات» هر دوی آن‌ها در پله‌برقی مقر سازمان ملل شد.</div>
<div class="tg-footer">👁️ 5.03K · <a href="https://t.me/SBoxxx/21022" target="_blank">📅 08:32 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21020">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">وزارت خارجه آمریکا به تمام شهروندان آمریکایی اعلام کرد که سفر هایشان به خاورمیانه را فوراً لغو کنند.</div>
<div class="tg-footer">👁️ 5.27K · <a href="https://t.me/SBoxxx/21020" target="_blank">📅 02:01 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21019">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">محسن رضایی:   محل تپه علی طاهر پیش از حمله تخلیه شده بود و عملیات دشمن شکست خورد</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/SBoxxx/21019" target="_blank">📅 00:59 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21018">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.   به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/21018" target="_blank">📅 00:57 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21017">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">محسن رضایی، دبیر شورای عالی امنیت ملی ایران، از آزمایش یک موشک ضدکشتی که به 80 گلوله تقسیم می‌شود، خبر داد.
به گفته ایشان، این آزمایش بر روی یک ناو هواپیمابر آمریکایی انجام شد و با توفیق الهی به نتیجه رسید.</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/SBoxxx/21017" target="_blank">📅 00:54 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21016">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">موسسه مطالعات جنگ:
طبق اظهارات مقام‌های آمریکایی به Axios در ۱۵ سپتامبر، تعداد عبور روزانه کشتی‌ها از مسیر جنوبی، با انجام موفقیت‌آمیز عملیات نظارت و مین‌روبی آمریکا، به حدود
۴۰ درصد سطح پیش از جنگ
بازگشته است و عبور کشتی‌ها هم در طول روز و هم شب انجام می‌شود.
عربستان سعودی نیز بنا بر گزارش‌ها صادرات نفت خود را بار دیگر از مسیر تنگه هرمز منتقل کرده است. بر اساس اطلاعات منابع تجاری که رویترز در ۱۸ سپتامبر به آنها استناد کرده، عربستان برای بارگیری‌های ماه‌های سپتامبر و اکتبر حدود
۶۰ میلیون بشکه نفت
را در بندر رأس تنوره در شرق عربستان بارگیری کرده که انتقال کشتی به کشتی آن از طریق تنگه هرمز انجام شده است.</div>
<div class="tg-footer">👁️ 5.21K · <a href="https://t.me/SBoxxx/21016" target="_blank">📅 00:43 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21015">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=JVgbifpKkhEqCsIo_7g8ozhYsQ3VuEKywpJ5KafBj6_ublWZdgWGgsfQoZ2l610dbqszyGuXXPQ2QoGbv3qMA6Y-aAFSV6PGc78huw2m4neB-TJTDQ_7Dqz89pT1WIFRbeoSps1BQJ0ieJbr4FkiDWw8Uc1vg1K4eQOaIHAxG86fv8Q_K71HD0feEGZxT-_5Nk_gWBr6-eiB9TwX--po4v8RIamvNH1dAKEdEarxEN7tJeKOtATbtaC1JQxyaKyuYPQaa-63hOZhCdr3MRIzGhVjVtVJIo35ATgu455DBnUyXU62WHyB95GZCIp7WxXaff2HuhzZlRzqKf2nqyz1uA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86c95cb0fd.mp4?token=JVgbifpKkhEqCsIo_7g8ozhYsQ3VuEKywpJ5KafBj6_ublWZdgWGgsfQoZ2l610dbqszyGuXXPQ2QoGbv3qMA6Y-aAFSV6PGc78huw2m4neB-TJTDQ_7Dqz89pT1WIFRbeoSps1BQJ0ieJbr4FkiDWw8Uc1vg1K4eQOaIHAxG86fv8Q_K71HD0feEGZxT-_5Nk_gWBr6-eiB9TwX--po4v8RIamvNH1dAKEdEarxEN7tJeKOtATbtaC1JQxyaKyuYPQaa-63hOZhCdr3MRIzGhVjVtVJIo35ATgu455DBnUyXU62WHyB95GZCIp7WxXaff2HuhzZlRzqKf2nqyz1uA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وزیر خارجه ترکیه گفته که ترکیه می تواند نیازهای نظامی سعودی را برطرف کند!  یعنی در این شرایط که عربستان بشدت به نیروی نظامی نیاز دارد هم ترکیه دست از بازاریابی برای سلاح های ساخت خودش دست برنمیدارد!</div>
<div class="tg-footer">👁️ 4.99K · <a href="https://t.me/SBoxxx/21015" target="_blank">📅 00:39 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21014">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aYP5e4BUzaPn0QbogtXVchtYdrdKDyYpl7kgMBe3R_3JxH4Dpx6pG6rKUpwt0jxPjK8hl8CAhJeq_oKuasaFDWscyCCE7guOcS7MluqilzPIc81HzpzrH5wXPeSmfi1Dyrly1gpYOTPhVuuBjDGAiAziP1fuevYqWPFYR0MwjS_YQIrEQsgXa51POzzx9mU1xryCoG3bh6UYDwFt3gbqVBqxGJC87NPLvJLp1bJHWs-0yYVHZPzrdQbJsyyuoRThBJ_dWVCIq8nqEfytn-U3Q9B1_jIDKwSghlsX7O_zWhN5tvOsXFzkeZlfPez8Hh0bTrtWPuYEEVVlxo7UHV7CzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:   این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21014" target="_blank">📅 00:23 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21013">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/K8Wvf5OErF8tdc7CE0OsSDuDKR4RfaudB5tcf7V2f-2KjQKLgmWCHy3Q9o4DceX0LlO82_l7B4sfScNW3cWnZn_zJyC9qKfXH8CaLS3GcT-ipJUtacwb1iT3h8r3eiB53P7NbL2myTR-sB9IEv4m25yBWktKOWZVJnDkryfLmfX1d0DPxEUgZh6n64IOIbpSwFygAXpRcfhEKHioPAFAvbKPpuPvJqFw00QYxM2cOhRHoL5pD0FGdLNj7T6GbtBKyfhVyWbLVwpw_fRf0JqFsaAVu6sgF0tMFb_bo7rF_73-QGf7HOB9sjM-Er4L8VYL5W9JJr79RkF8BVOJ3C1drQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 5.1K · <a href="https://t.me/SBoxxx/21013" target="_blank">📅 00:17 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21012">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">عضو دفتر سیاسی انصارالله:
این پیام به ترکیه و پاکستان ارسال شد که به خودتان احترام بگذارید؛ اگر از عربستان سعودی حمایت کنید، ما به شما حمله خواهیم کرد و شما را تنبیه خواهیم کرد، و دست‌های ما از فولاد خواهد بود</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21012" target="_blank">📅 00:09 · 29 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21011">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صداى انفجار در تنگه هرمز شنيده شد
گزارش‌ها حاکی از شلیک موشک‌های کروز ضد کشتی به سمت شناورهای متخلف در تنگه هرمز هستند.</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21011" target="_blank">📅 22:08 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21010">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">درباره دیدار مهم رهبران چین و آمریکا
دیدار دونالد ترامپ و شی جین‌پینگ در ۲۴ سپتامبر در واشنگتن، در ظاهر یک نشست دوجانبه میان دو اقتصاد بزرگ جهان است، اما دامنه پیامدهای آن بسیار فراتر از روابط تجاری آمریکا و چین خواهد بود. در شرایطی که جنگ ایران، بازار انرژی و رقابت فناوری بر اقتصاد جهانی سایه انداخته، این دیدار می‌تواند یکی از مهم‌ترین رویدادهای ژئوپلیتیکی پاییز باشد.
مهم‌ترین موضوع برای بازارها، احتمال تمدید آتش‌بس تجاری آمریکا و چین است؛ توافقی که در ۱۰ نوامبر منقضی می‌شود. مذاکرات مقدماتی اسکات بسنت و هی لیفنگ در نیویورک نیز نشان می‌دهد که دو طرف پیش از دیدار رهبران در حال تلاش برای حل اختلافات مربوط به تعرفه‌ها، مواد معدنی حیاتی و دسترسی به فناوری هستند.
اگر ترامپ و شی بتوانند حداقل یک چارچوب برای ادامه این آتش‌بس ارائه کنند، نخستین واکنش بازار می‌تواند کاهش ریسک تجاری باشد: سهام و دارایی‌های پرریسک حمایت می‌شوند، فشار بر زنجیره تأمین کاهش می‌یابد و بخشی از تقاضا برای دلار به‌عنوان دارایی امن می‌تواند تخلیه شود. در مقابل، شکست مذاکرات یا تهدید به بازگشت تعرفه‌ها می‌تواند مجدداً سناریوی جنگ تجاری، تورم وارداتی و اختلال در تجارت جهانی را فعال کند.
اما مواد معدنی کمیاب شاید از تعرفه‌ها نیز مهم‌تر باشند. چین همچنان اهرم بزرگی در زنجیره تأمین عناصر کمیاب و مواد حیاتی مورد استفاده در خودرو، نیمه‌رساناها، هوافضا و صنایع دفاعی دارد. آمریکا نیز در مقابل، محدودیت دسترسی چین به فناوری پیشرفته را در اختیار دارد. بنابراین این دیدار در واقع مذاکره‌ای بر سر «اهرم‌های استراتژیک» است، نه صرفاً تراز تجاری.
برای بازار طلا، نتیجه اهمیت ویژه‌ای دارد. کاهش تنش تجاری می‌تواند بخشی از صرفه ریسک ژئوپلیتیکی را کاهش دهد؛ اما اگر نشست به بن‌بست برسد، هم ریسک تجاری و هم تقاضای پناهگاه امن می‌تواند افزایش یابد. هم‌زمان باید نرخ‌های آمریکا را در نظر گرفت: اگر توافق تجاری باعث تقویت چشم‌انداز رشد آمریکا شود و بازدهی اوراق بالا بماند، اثر آن بر طلا الزاماً مثبت نخواهد بود.
ایران؛ مهم‌ترین بخش پنهان نشست
ایران احتمالاً یکی از موضوعات حساس مذاکرات خواهد بود. واشنگتن از چین انتظار دارد در فشار اقتصادی علیه تهران همکاری بیشتری داشته باشد، در حالی که چین همچنان بزرگ‌ترین خریدار نفت ایران است و روابط اقتصادی نزدیکی با تهران دارد. گزارش‌ها همچنین از تلاش آمریکا برای اعمال فشار بر شبکه‌های مالی مرتبط با تجارت ایران حکایت دارد، هرچند واشنگتن تاکنون بانک‌های چینی را در موج اخیر فشارهای خود به شکل گسترده هدف قرار نداده است.
برای ایران، اهمیت نشست در این است که چین می‌تواند بخشی از اثربخشی تحریم‌های آمریکا را خنثی یا تشدید کند. اگر پکن حاضر شود در زمینه نفت، شبکه‌های مالی یا دور زدن تحریم‌ها همکاری بیشتری با واشنگتن داشته باشد، فشار اقتصادی بر تهران افزایش خواهد یافت. اگر چین در مقابل، بر ادامه تجارت انرژی با ایران تأکید کند، یکی از مهم‌ترین کانال‌های فشار آمریکا محدودتر می‌شود. همچنین شایعاتی درباره کمک اطلاعاتی چین به ایران در راستای دقیق تر کردن هدفگیری موشکهای ایرانی منتشر شده که احتمال بحث طرفین در خصوص آن می رود.
از منظر بازار انرژی نیز موضوع حساس است. هرگونه توافق آمریکا و چین که به کاهش تنش‌های ژئوپلیتیکی منجر شود، می‌تواند از صرفه ریسک نفت بکاهد. اما اگر ایران در مرکز اختلافات آمریکا و چین قرار گیرد و هم‌زمان اختلال در جریان انرژی منطقه ادامه پیدا کند، نفت می‌تواند دوباره تحت تأثیر ریسک ژئوپلیتیکی قرار گیرد.
در نهایت، اهمیت واقعی دیدار ترامپ و شی شاید در یک «توافق بزرگ» نباشد؛ بلکه در این باشد که آیا دو طرف می‌توانند رقابت استراتژیک خود را مدیریت کنند بدون آنکه وارد مرحله جدیدی از جنگ تجاری و فناوری شوند. برای بازارها، همین تفاوت میان «مدیریت تنش» و «تشدید تنش» می‌تواند مسیر دلار، طلا، نفت، سهام و ارزهای آسیایی را در هفته‌های بعد تغییر دهد. برای ایران نیز سؤال اصلی این است که آیا تهران از رقابت آمریکا و چین فضای بیشتری برای مانور پیدا می‌کند، یا اینکه واشنگتن و پکن در نهایت بر سر اعمال فشار هماهنگ‌تر بر اقتصاد ایران به تفاهم می‌رسند.</div>
<div class="tg-footer">👁️ 5.26K · <a href="https://t.me/SBoxxx/21010" target="_blank">📅 21:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21009">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ممکن است برویم یک نایت کلاب اما آنجا شربت بیدمشک سفارش بدهیم !</div>
<div class="tg-footer">👁️ 4.96K · <a href="https://t.me/SBoxxx/21009" target="_blank">📅 21:48 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21008">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">محسن رضایی :
دکترین هسته‌ای ایران تغییر نکرده، اما خروج از NPT ممکن است</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/SBoxxx/21008" target="_blank">📅 21:45 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21007">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IGPK5sq4rRNyG1NEOv3bHXaw-HF0VtR_yKvZvVC241dJDHbMDFJuQLUkRz5X1oqkOf6uMZIafoIV12kUbAONMx8p_CbrNZnWW3SHcUgNKngpLySsONSDEZTaoI5sjkEFeLPg5Kw7MbbKAP-AIhCNhFgaZtE-G6AnhQ7rJmh1rmNNiG8TnJeEZ0qPYcG5AQvsLTAa6G_vCHNSJzb3OTLuVv_gdoY9vg2Gn93jHWVsJALs0GNflObrdfc3lblqSNehcctX7d1euJNKwk0QnshP8puFu7d-DuXH8fRa9ZJS4USweMYYI3F-sO92Ww9NEWtLgKMIOjMrKxpZvTFdeVm35g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خب امروز و بعد از ۹ ماه تارگت ۲۴۰ هزار تومانی دلار محقق شد.  بعید نیست مدتی رنج بشود.</div>
<div class="tg-footer">👁️ 5.43K · <a href="https://t.me/SBoxxx/21007" target="_blank">📅 20:29 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21006">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترامپ می‌گوید توافق با دانمارک، «کنترل دائمی» ایالات متحده را بر امنیت گرینلند تضمین می‌کند  ترامپ می‌گوید توافق گرینلند، رقیبان ایالات متحده را از ایجاد پایگاه‌های نظامی در آنجا منع می‌کند</div>
<div class="tg-footer">👁️ 5.04K · <a href="https://t.me/SBoxxx/21006" target="_blank">📅 20:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21005">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">محسن رضایی:   خواهان پایان جنگ میان عربستان سعودی و یمن هستیم و معتقدم یمنی‌ها نیز خواهان دستیابی به توافقی با عربستان هستند</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/SBoxxx/21005" target="_blank">📅 19:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21004">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو  با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.  این نابرابری،…</div>
<div class="tg-footer">👁️ 4.85K · <a href="https://t.me/SBoxxx/21004" target="_blank">📅 19:16 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21003">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromCyclical Waves</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QOedRIARjMFKB0qXqWVZmPKgqc3ZCnBMqCwwndoUhG-qHShtW4tHqOvsAxv1u0uVtttAF73fmOc8lG46ez4uljJiQbOgc_Qu5Px636c2RzxjET97OqbjzrWZGV8iqUHaeA01_vlq0g5u6_Q736tbzD60oLFey_cPBSzvGQSjWMa8gj0hWUb_t5xA87SfyoP0u1MGWDT7_O9SSo5CJvO_BNBeA11aVDAA0OT-vJWQirsUQA0hFMkGrFULopTFnHtCEzwF8d1N4h1MySOuyvNm6qsSCrPIqep1R5WOt6gi2BTWRQ9e7QDwFIQv16RyD_pRnJw0T8E3I8ugKQWjhAw1mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📌
جنگ ایران؛ رشد و توزیع ثروت و درآمد مصرف‌کننده آمریکایی و چالش فدرال رزرو
با وجود فشار تورمی ناشی از انرژی، درآمد واقعی و ثروت خانوارهای آمریکایی نسبت به سال گذشته افزایش یافته، اما بخش بزرگی از رشد ثروت از افزایش ارزش سهام و املاک ناشی شده است.
این نابرابری، چالش مهمی برای فدرال رزرو ایجاد می‌کند؛ زیرا رشد دارایی‌ها می‌تواند مصرف را تقویت کند، در حالی که افت بازار سهام می‌تواند همین اثر را معکوس کرده و به کاهش تقاضا منجر شود.
🔗
ادامه یادداشت از اینجا بخوانید
💬
ارتباط با پشتیبانی :
@CyclicalWavesSupport
📌
کانال ما :
@cyclicalwaves</div>
<div class="tg-footer">👁️ 5.02K · <a href="https://t.me/SBoxxx/21003" target="_blank">📅 19:15 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21002">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">محسن
رضایی
:
خواهان
پایان
جنگ
میان
عربستان
سعودی
و
یمن
هستیم
و
معتقدم
یمنی‌ها
نیز
خواهان
دستیابی
به
توافقی
با
عربستان
هستند</div>
<div class="tg-footer">👁️ 5.74K · <a href="https://t.me/SBoxxx/21002" target="_blank">📅 19:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21001">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NIcNFGCrlqfJy14yz7QJ0bwVnZpDNS3k7h4-3yEvrB9dJy83UWoiMbguxL7fntf_NZcJzRjLf8-QVVYiiQrQ6L2iLujkSDD28tdF8DRBqTWdNXWbfWCQTNOy3x4yqOUmMvtKPq38YZkn0PCzKODRyzylfmakn6DJKb5XZxRQ0Ee6Qxgk44lZz4htJyBbi_FbrBm-cOzgA3IPfSgXNU1_XPyGMa4dyOkaEg6drFWlKxAoaNjCvaqL117_dszN2DModro4URncwhAkvh3NBuNrWUHbPYkkKhcHUTHHoHwg6L1LDlbcKlZGnsW1y2vvxyhosX0EaJaUzQahS4TEsFqC_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آخرین وضعیت نتایج احتمالی انتخابات میان دوره ای پیش رو در آمریکا</div>
<div class="tg-footer">👁️ 5.31K · <a href="https://t.me/SBoxxx/21001" target="_blank">📅 16:22 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-21000">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">WW3 is loading....</div>
<div class="tg-footer">👁️ 5.32K · <a href="https://t.me/SBoxxx/21000" target="_blank">📅 16:06 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20999">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">خطر جنگ هسته ای؟!  ساعت نمادین روز رستاخیز بار دیگر به یک یادآور قدرتمند از خطرات رو به رشد برای جامعه بین‌المللی تبدیل شده است. در ارزیابی ابتدای سال ۲۰۲۶، مجله «بولتن دانشمندان اتمی» عقربه‌های این ساعت را به ۸۵ ثانیه قبل از نیمه‌شب (ساعت فاجعه) رساند که…</div>
<div class="tg-footer">👁️ 5.45K · <a href="https://t.me/SBoxxx/20999" target="_blank">📅 16:04 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20998">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:   دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.36K · <a href="https://t.me/SBoxxx/20998" target="_blank">📅 15:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20997">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس کمیسیون امنیت ملی:
دخل و خرج زندگی مردم آمریکا با هم نمی‌خواند</div>
<div class="tg-footer">👁️ 5.89K · <a href="https://t.me/SBoxxx/20997" target="_blank">📅 14:38 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20996">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tBqiXYM00Bxp933MJUGCwrUqC-TnV90A_-A5CoSYhU6hR0Q6-XoAGzw30CqFzyU5Jc6aPDjwmTyKsaEvcshuDGJCrtA91B3OGxZO2YouWgnXIenFNpaQq_o2tkCtZhEZRgFCI800T7lVSzYpSY-YYS4aCqxwipe181TVEMibjTOUn5ZoqqlO4jyk-vvzWqwY5VpIoKW7q37aqzX6WSHOtJq9v1KEleQPPwFEw4aiqRXZne6_4JZC48ZP8Mptaij7GLC33a2fMZOB_iZjrzQdBo6YaJhD0If7eqvv0q5TbF3ybI-moMDMU8EK-Sn63ckvmP175reJLbPlSV2bTnDlNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گزارش های موثق، ترکیه چندین پهپاد رزمی و شناسایی برای کمک به سعودی ها در جنگ یمن ارسال کرده که دستکم یک پهپاد کارایل توسط حوثی ها سرنگون شده است.</div>
<div class="tg-footer">👁️ 5.47K · <a href="https://t.me/SBoxxx/20996" target="_blank">📅 12:41 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20995">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">ترکیه مجوز فعالیت بانک ملت ایران را لغو کرد</div>
<div class="tg-footer">👁️ 6.54K · <a href="https://t.me/SBoxxx/20995" target="_blank">📅 10:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20994">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">آمریکا بسته دفاع هوایی ۲.۶۸ میلیارد دلاری برای اوکراین را تأیید کرد
وزارت خارجه آمریکا
فروش تجهیزات و پشتیبانی دفاع هوایی به ارزش
۲.۶۸ میلیارد دلار
به اوکراین را تأیید کرده است.
این بسته شامل
سیستم‌های دفاع هوایی برد بلند، پرتابگرهای متحرک، رادارهای ضد پهپاد، قطعات یدکی، نرم‌افزار و پشتیبانی فنی
است.
اوکراین هزینه خرید را از طریق
کمک‌های مالی اروپا
و
کمک‌های نظامی خارجی آمریکا (FMF) که قبلاً تخصیص یافته بود، تأمین خواهد کرد.</div>
<div class="tg-footer">👁️ 5.62K · <a href="https://t.me/SBoxxx/20994" target="_blank">📅 08:20 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20993">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">حمله موشکی حوثی ها به ریاض پایتخت عربستان</div>
<div class="tg-footer">👁️ 5.6K · <a href="https://t.me/SBoxxx/20993" target="_blank">📅 06:13 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20992">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.73K · <a href="https://t.me/SBoxxx/20992" target="_blank">📅 01:12 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20991">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">منابع خبر می‌دهند آمریکا و دانمارک به توافقی درباره گرینلند نزدیک می‌شوند.</div>
<div class="tg-footer">👁️ 5.76K · <a href="https://t.me/SBoxxx/20991" target="_blank">📅 00:50 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20990">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aBZqurR3kazWTjajay_GWb9awz-PXjPuYmOYS_Mh7fS5R-Z5xUzpWhgtoNI-6rYc99QCv3Aor1XDimbMxf24q6MCWDd8u1BsLR4uM1n-un6Riuiay8jZ6NJAbt4-zcN7m4XnQS1eobq7sK2wlHjMssdw2s1Vg7i2J71aKqK4M4Bzlx0Ze26_3Nn-uSjEB2LQ9veMpID51PvWn_17kygBOoaJKritmXweYIrYanMaLCRtQ7fsUt31hVsyLfCEAf_xGH6RuXrLxW_j86srDBZCZqfUEsDOTCjFYKeLGdOGNS_-34MnkY6MpqlMs1Gas1AoA30WEQJHlG3D8NqEmpMmrA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سلامتی همه پورن استارهای وطن پرست!</div>
<div class="tg-footer">👁️ 6.11K · <a href="https://t.me/SBoxxx/20990" target="_blank">📅 00:11 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20989">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Fc8pe1qASngHF4omAE6SHlyHlhf-iki5PlYK59Xx0eAcZHVzKlpbmSWDS-fujNjReSaRO-nwU09dTiyC3lwhNT0fY3XVR_pnlc9gyEMhnAYqCO1DBfpZyZEj4x2QW2OYorlDjnCO_8F_lrb-TK7AhiV488ydo6WsAvavdMiqxK_5pWD_cZgDkMdLd5AQSczWhKPx4ucFQqgNlYsp4LLlVJsP5Qh4IMjElX_Sd-FOU5Es1ZKg7fb-8_RB1QNjAdZ4LFVqqKm3b7PkTNCH_bOv1RpYj6VtxRr9LlN1P5H5XsHBx3wUFXgI4i7WzIkuSPceO4poZootHS7khxVsgUb2Nw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!  فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!  همه شان را زدند.  یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20989" target="_blank">📅 00:07 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20988">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHEucwr7hdDPXonnMuUJAxwMwajJ6zpwo9RIB8fDj7tc8ZkqUkCoFmcxOdUzgOxQRV-67AKqdkA29nBgWweYEbP5-aJdu868mOuSaENiI0E0SA5wLlXyhbLuNKvjS52E_hqj26SXb3wqPecmrUTSk4cUbjQMaB4LsI0BEZl3Er5-pCAO1ny-VAxDNB11BQengwQt-Sg6Q7x5vQjGDhUHc3YkXNHczrFHSy1UVyjXYCEong1ki6mM-xV952vAAlAN10R2w_2VXEb7NGltS16Yu62SmkILYpsVAHisQqTjUi8tWLxU6lj3UcQUdWYviuCNzEHPzj_kUfpRKqox47L57g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">طبق گفته‌ی شش مقام آمریکایی که با اطلاعات داخلی وزارت دفاع در مورد آمار تلفات آشنایی دارند، تعداد سربازان آمریکایی که در خاورمیانه و در جریان جنگ جاری با ایران جان خود را از دست داده‌اند، بیشتر از آن است که پنتاگون به طور علنی اعلام کرده است.</div>
<div class="tg-footer">👁️ 5.29K · <a href="https://t.me/SBoxxx/20988" target="_blank">📅 00:05 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20987">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">حوثی ها قشنگ دارند خاطرات کتاب های دینی راهنمایی و دبیرستان را برایمان زنده می کنند!
فکر کنید اگر این دوستان ما نبودند چطور یاد طائف، مکه، مدینه میفتادیم؟!
همه شان را زدند.
یا ذی الجلال و الاکرام</div>
<div class="tg-footer">👁️ 5.3K · <a href="https://t.me/SBoxxx/20987" target="_blank">📅 00:02 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20986">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">انفجار در طائف عربستان!</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/SBoxxx/20986" target="_blank">📅 00:01 · 28 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20985">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">📌
جنگ هرمز و باب‌المندب؛ آیا ایران در حال فرسایش مالی دولت‌های غربی است؟  اختلال در تنگه هرمز و افزایش فشار بر باب‌المندب می‌تواند با بالا نگه داشتن قیمت انرژی، تورم و نرخ بهره را تشدید کرده و هزینه تأمین مالی دولت‌های غربی را افزایش دهد؛ در نتیجه، جنگ از…</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20985" target="_blank">📅 23:33 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20984">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">#FairValueCurve  نمایه FVC نشانگر نزدیک شدن طلا به محدوده قیمت منصفانه است و لذا از حالت حباب منفی ارزشگذاری فاصله گرفته است (به دلیل رشد سنگین از پریشب) هر چند هنوز تا تشکیل حباب مثبت و بیش خرید بودن فاصله زیادی دارد.  پس بهترین استراتژی برای امروز:  خرید…</div>
<div class="tg-footer">👁️ 5.41K · <a href="https://t.me/SBoxxx/20984" target="_blank">📅 20:04 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20983">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">العربیه:
وزیر کشور پاکستان طی ساعات آینده به تهران سفر خواهد کرد.</div>
<div class="tg-footer">👁️ 5.57K · <a href="https://t.me/SBoxxx/20983" target="_blank">📅 18:19 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20982">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نیروی دریایی سپاه پاسداران
انقلاب اسلامی ۴ موشک کروز ضدکشتی به سمت تنگه هرمز شلیک کرد</div>
<div class="tg-footer">👁️ 5.56K · <a href="https://t.me/SBoxxx/20982" target="_blank">📅 18:02 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20981">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Yg20e_sAM1MXYffDXM2IdLsmlwvUEQi_fdYlR4QtF9FhMkT7T67pnDBe1Ud1EeTzksTGLn6hg4gSilG70BXZ01B89OuaKJznhfR80CBrFLHLH1saJxn8QNbt1naKRndrDQwVn8vy3TB2cQA-UNexpVihFv6KnSIdsUXdWwwBxLNZRuKkfzRnSXMapJFU6S8a40Is_WEkif9WbTRmvQNkRt7OJ9AMRi7u-yL60b33KoTqQDsofIeQe8TdE2LN9yfhtGL8g-Ck3hZhysEYdOPdpQkME_NLViNEaAx4IJMlRByp7f19Y2IsJz_s4wsAuO-ndP1ET4i5ohwZ72yjFkVSQw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توصیه دکتر پزشکیان به جانفدایان:  کمتر مصرف کنید!  (پسر پزشکیان هم دیروز همین را گفته بود)</div>
<div class="tg-footer">👁️ 5.8K · <a href="https://t.me/SBoxxx/20981" target="_blank">📅 15:07 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20980">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=ZFIsniaD8zHuLXi-SgUM4IZifTLY60rCEFd7uGi1Qa4mi9YEjjFeiwk97tCfZyP4fNydkFcZMPoAIluipSc0eYFh-K0UWj_XvfWEEwDszEGFsnRXanBjp_A4Z18pmHw_KfA0ogDLwxEwDuEIFZymKBCaWP7-DwXyuqXcVB3ZFxB9UKlVgE2zCLtzKZlqP69rtuZX-2FaDGkgNo-Ka05Xxg3dfrbNLkqIF6kan5mYE_-PQdZ1TGObHlajp6HFmtttGIev1gIABCv4bVC5HI759pX36QnTPoBAebxF68UWUbQaz5tF4kyyNtvzERg5V9A6E2cNZOSseTvCsiB-UTfdCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/573e6b119d.mp4?token=ZFIsniaD8zHuLXi-SgUM4IZifTLY60rCEFd7uGi1Qa4mi9YEjjFeiwk97tCfZyP4fNydkFcZMPoAIluipSc0eYFh-K0UWj_XvfWEEwDszEGFsnRXanBjp_A4Z18pmHw_KfA0ogDLwxEwDuEIFZymKBCaWP7-DwXyuqXcVB3ZFxB9UKlVgE2zCLtzKZlqP69rtuZX-2FaDGkgNo-Ka05Xxg3dfrbNLkqIF6kan5mYE_-PQdZ1TGObHlajp6HFmtttGIev1gIABCv4bVC5HI759pX36QnTPoBAebxF68UWUbQaz5tF4kyyNtvzERg5V9A6E2cNZOSseTvCsiB-UTfdCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">از اروپایی بودن همین را فهمیده که یک لامپ را خاموش کند!  در حاکمیت قانون و مدیریت عقلانی و کرامت انسان هم اروپایی بشویم یا نه؟!</div>
<div class="tg-footer">👁️ 5.58K · <a href="https://t.me/SBoxxx/20980" target="_blank">📅 15:06 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20979">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:  امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏   ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.53K · <a href="https://t.me/SBoxxx/20979" target="_blank">📅 14:25 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20977">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">ضرغامی در سالگرد ⁧مهسا امینی:
امروز همه تصمیم‌گیران و تصمیم‌سازان، بر اشتباه بودن ‏روش  گشت ارشاد  اتفاق نظر دارند‏
ظاهرا همیشه باید مصیبت‌ها و مقاومت‌ها ما را به راه و روش درست هدایت کند</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/SBoxxx/20977" target="_blank">📅 14:13 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20976">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">یادداشت بسیار مهمی است و نکته اصلی اش این است:
جهش بهای نفت و افت قیمت اوراق قرضه به تنهایی موجب تسلیم شدن ترامپ برای پایان جنگ نشده و احتمالا هم نخواهدشد.</div>
<div class="tg-footer">👁️ 5.37K · <a href="https://t.me/SBoxxx/20976" target="_blank">📅 14:03 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20975">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">جی‌پی مورگان از تلاش برای پیش‌بینی پایان جنگ ایران و ترامپ دست کشید
جی‌پی مورگان اعلام کرده است که دیگر برای جنگ ایران یک
سناریوی پایه (Baseline Forecast)
ندارد؛ چراکه قیمت نفت، بازده اوراق خزانه‌داری آمریکا و قیمت سوخت از سطوحی عبور کرده‌اند که این بانک پیش‌تر انتظار داشت عبور از آنها واشنگتن را به سمت دستیابی به یک توافق پایدار سوق دهد.
عبور از خطوط قرمز اقتصادی، به خروج از جنگ منجر نشد
در آغاز جنگ، جی‌پی مورگان بر این فرض بود که افزایش فشار اقتصادی در نهایت دونالد ترامپ را به سمت توافقی برای بازگشایی تنگه هرمز سوق خواهد داد.
مهم‌ترین آستانه‌هایی که این بانک در نظر گرفته بود عبارت بودند از:
• نفت بالای
۱۰۰ دلار در هر بشکه
• بنزین در محدوده
۵ دلار در هر گالن
• بازده اوراق خزانه‌داری ۱۰ساله آمریکا بالای
۵ درصد
شش ماه بعد، چند مورد از این سطوح شکسته شده‌اند.
ناتاشا کانوا، رئیس استراتژی جهانی کالاهای جی‌پی مورگان، در یادداشتی در روز پنجشنبه گفت:
«شش ماه بعد، بسیاری از این خطوط عبور کرده‌اند، اما استراتژی خروج نه‌تنها روشن‌تر نشده، بلکه مبهم‌تر شده است.»
او افزود:
«برای نخستین بار از زمان آغاز درگیری ایران، ما دیگر دیدگاه پایه‌ای نداریم. واقعاً نمی‌دانیم پایان این جنگ را چگونه مدل‌سازی کنیم.»
هیچ نشانه روشنی از کاهش تنش وجود ندارد
جی‌پی مورگان معتقد است شواهد چندانی وجود ندارد که نشان دهد واشنگتن یا تهران در حال آماده شدن برای عقب‌نشینی هستند.
به گفته کانوا، هرچه درگیری به جای کوچک‌تر شدن، گسترده‌تر می‌شود، دفاع از این دیدگاه که اختلال در عرضه انرژی کوتاه‌مدت خواهد بود، دشوارتر شده است.
در همین حال، عربستان سعودی پس از آسیب دیدن خط لوله در پی یک حمله پهپادی که از عراق انجام شد، خط لوله
شرق–غرب
خود را متوقف کرده است.
همچنین شبه‌نظامیان حوثی همسو با ایران پیشروی‌هایی داشته‌اند که می‌تواند موقعیت آنها را در زمینه کنترل یا ایجاد اختلال در تردد نفتکش‌ها در بخش جنوبی دریای سرخ تقویت کند.
ترامپ نیز روز پنجشنبه به Axios گفت که در آستانه تصمیم دیگری درباره این موضوع قرار دارد که آیا عملیات نظامی گسترده علیه ایران را از سر بگیرد یا به سمت پایان دادن به جنگ حرکت کند.
ترامپ گفت:
«یک تصمیم بزرگ پیش رو دارم. آیا می‌خواهم وارد عمل شوم و آنها [رژیم ایران] را نابود کنم یا نه؟ این یک تصمیم بزرگ است. هر اتفاقی ممکن است از سوی من رخ دهد.»
بازار نفت، کاهش بیشتر عرضه را قیمت‌گذاری می‌کند
جی‌پی مورگان ارزش منصفانه نفت برنت را حدود
۹۰ دلار در هر بشکه
برآورد می‌کند، اما شاخص بین‌المللی نفت اکنون نزدیک
۱۰۵ دلار
معامله می‌شود؛ در حالی که در اوایل این هفته به محدوده
۱۱۰ دلار
نزدیک شده بود.
این بانک محاسبه می‌کند که به ازای هر
یک میلیون بشکه در روز
کاهش عرضه نفت، حدود
۴ دلار
به قیمت قراردادهای آتی نفت اضافه می‌شود.
بر همین اساس، کانوا می‌گوید بازار در حال قیمت‌گذاری ریسک از دست رفتن حدود
۴ میلیون بشکه در روز عرضه اضافی
است؛ آن هم علاوه بر حدود
۱۰ میلیون بشکه در روز
عرضه‌ای که هم‌اکنون دچار اختلال شده است.
تصویر کلی بازار انرژی با حملات اوکراین به پالایشگاه‌های روسیه نیز پیچیده‌تر شده است؛ این در حالی است که ترامپ روز دوشنبه گفته بود کی‌یف و مسکو توافق کرده‌اند حملات به تأسیسات انرژی را متوقف کنند.
ذخایر نفت همچنان یک حائل ایجاد می‌کنند
مهم‌ترین عامل محدودکننده برای افزایش بیشتر قیمت نفت، حجم نفتی است که همچنان در ذخایر نگهداری می‌شود.
ذخایر تاکنون
۵۵۵ میلیون بشکه
کاهش یافته‌اند؛ رقمی که به‌مراتب کمتر از کاهش
۱.۶ میلیارد بشکه‌ای
است که تیم کالاهای جی‌پی مورگان در ابتدا پیش‌بینی کرده بود.
بنابراین بازار در برابر یک شوک طولانی‌مدت عرضه، نسبت به برآورد قبلی بانک، همچنان از
حاشیه امنیت بیشتری در ذخایر
برخوردار است.
کانوا در جمع‌بندی گفت:
«خلاصه اینکه، فعلاً هنوز به اندازه کافی ظرفیت ذخیره و عرضه پشتیبان وجود دارد که قیمت‌ها را مهار کند.»</div>
<div class="tg-footer">👁️ 5.42K · <a href="https://t.me/SBoxxx/20975" target="_blank">📅 13:12 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20974">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛    «ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با…</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/SBoxxx/20974" target="_blank">📅 11:40 · 27 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-20973">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">خلیل شیر غلامی، سفیر ایران در ارمنستان؛
«ایران رویکرد ویژه‌ای نسبت به مسئله تمامیت ارضی و حاکمیت ارمنستان دارد و این را یکی از مسائل حساس خود می‌داند. با توجه به اهمیت منطقه سیونیک به عنوان یک مرکز استراتژیک برای ارمنستان، به ویژه در زمینه حفظ ارتباط با ایران، هر پروژه‌ای، از جمله پروژه TRIPP یا هر طرح دیگری که تهدیدی برای ارمنستان یا روابط ایران و ارمنستان محسوب نشود، از نظر دیپلماتیک، مشکلی ایجاد نخواهد کرد. در اجرای هر پروژه‌ای، تمامیت ارضی و حاکمیت ارمنستان نباید به خطر بیفتد.
علاوه بر این، حضور آمریکایی‌ها در مرز ارمنستان و ایران نباید تهدیدی برای ایران باشد.
اگر این دو شرط محقق شوند و همچنین منافع ارمنستان در نظر گرفته شود، ایران مخالف اجرای پروژه TRIPP نخواهد بود.»</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/SBoxxx/20973" target="_blank">📅 11:38 · 27 Shahrivar 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
