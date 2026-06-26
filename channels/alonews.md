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
<p>@alonews • 👥 940K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-05 10:14:50</div>
<hr>

<div class="tg-post" id="msg-130279">
<div class="tg-post-header">📌 پیام #100</div>
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
<div class="tg-footer">👁️ 2.08K · <a href="https://t.me/alonews/130279" target="_blank">📅 10:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130278">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/alonews/130278" target="_blank">📅 09:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130277">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E-h04qqz9ZlVEQuKCkmgeStwj_P8ro4MzBLIZItMoSVZ2qzN5p3Kb2vlx0NZ0gGi3xxdi6gEWI32URmPQL47I8N-_FJ0yOOvVdG0JvOt6yVPTNtP9xqGlQbekc6EaeCND21GsG-8k4HcxgTqycO7VtXb2M0V1AknEATZo7dzVFjoK5g0dEQ_EqWeWw-Tzrv4-dggR2LXwm8oigXK5CsCM8b-K1shBQ85BUrsfG0c97ocF7y5qw-R5L4hznvjmnw1lUyGWlsAr1CfBfIbaCqSmrq9e0Q-M1tBaMFmRtZUxMsAzTbEBFrG3j4GEKCrkz3EZNrrykEq4SanzVCqHvQvrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صبح امروز ۴ زمین لرزه مرز بین عراق و ایران رو لرزوند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/alonews/130277" target="_blank">📅 09:50 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130276">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">👈
بهای نفت برنت با کاهش ۱.۷۴ درصدی به ۷۴.۱۹ دلار و نفت خام وست‌تگزاس اینترمدیت (WTI) با افت ۱.۹۶ درصدی به ۷۰.۵۱ دلار در هر بشکه رسید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/130276" target="_blank">📅 09:48 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130275">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6Q_ygCcQRUGPtPxxqrPo8bNctj7kPeewdj3nqDlGcb63ajarhMBW_7nE0iG73ABXt8ziRLnzYQ1cyomfNr24ITWpy1uoVQbelGkAJPtJynSSxuDDZM_4iwAV4ppAdyK59qe6U9c1I5zb2AAE8APbq10EE164zA7tHb1P0d327BpXh7owJIVj6WdE5OYBe3CRVVt5C-RkJSG468UF6IZS-5CEQazWivDaLt3wbnjLc_eTPcB5DFnoy-VGwizD_kJyLVJrUtqke4AWTkazS2fRHARPHSS_G1lfiUWGZ4HWpd3zz0XfCffH-jRJ4HeGRyEE_OtM_Z7B5mqPNjB1xAHLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
معاون وزیر امور خارجه آمریکا در امور شرق آسیا:واشنگتن، علیرغم اعتراضات چین، مرتبا کشتی‌های جنگی خود را به آب‌های مورد مناقشه در منطقه آسیا-اقیانوسیه می‌فرستد تا «از آزادی ناوبری دفاع کند!»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/alonews/130275" target="_blank">📅 09:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130274">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
نخستین پرواز دیروز پنج‌شنبه ۵ تیر از مبدأ تهران در ساعت ۸:۰۵ صبح در فرودگاه بین‌المللی کیش به زمین نشست و ورود گردشگران به جزیره به‌صورت رسمی آغاز شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/alonews/130274" target="_blank">📅 09:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130273">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ola-frWl6P6tXT6TunJ-XCpS5MHEBDfVnHALSZYkEYNdHi2jW3gIXdfMxVCFIES4QaVK8Ehin7bq2vv6k7eavKBb-Oi6R1vws6lybfhx8JSNbyfPs037vTrvGKE-N5wSCuz-7GwJzXTV6i3mq7xg1vDGin4hPXNuphyHHPG8oH9fRHys3cncH-gaVBMKIyTOTXESUt2D-SWpcqz8IfpX5thJbs5rMr-1tlQzS5KgfYCnZa8XS3nQt18IEwMRtPO6O5AKmjWKW4o8eViklGst0Mf1YbXgIHofEmeIiILC21jRM5Mbw9qZcaXMpzznrWgGwvgBof-FSdpCYoT4tpPLJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
حمله شدید اسرائیل به نبطیه/ در ساعات اخیر چندین حمله به جنوب لبنان ثبت شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/alonews/130273" target="_blank">📅 09:29 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130272">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل: به هیچ وجه قصد خروج از لبنان را نداریم، حتی اگر ترامپ درخواست کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/alonews/130272" target="_blank">📅 09:28 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130271">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">👈
افزایش کشته‌های زلزله ونزوئلا به ۲۳۵ نفر
🔴
سازمان زمین‌شناسی ایالات متحده:
فاجعه احتمالا گسترده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/alonews/130271" target="_blank">📅 09:22 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130270">
<div class="tg-post-header">📌 پیام #91</div>
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
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/alonews/130270" target="_blank">📅 09:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130269">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
استیون میلر، معاون رئیس کارکنان کاخ سفید: ایالات متحده در مسیر بستن کامل پرونده پناهندگی قرار دارد و پذیرش تمامی اتباع خارجی را که به دنبال یافتن پناهگاهی در آمریکا هستند، به‌طور کامل متوقف می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/alonews/130269" target="_blank">📅 09:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130268">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/alonews/130268" target="_blank">📅 09:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130267">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">👈
گروسی: معتقدیم که مواد هسته‌ای از زمان آخرین بازرسی که در سال ۲۰۲۵ انجام دادیم، منتقل نشده‌اند، اما لازم است این موضوع را به‌طور قطعی راستی‌آزمایی کنیم
🔴
جزئیات فعالیت‌های ما در ایران و ترکیب کمیته هماهنگی ویژه مربوط به روند بازرسی، در جریان مذاکرات مشخص خواهد شد
🔴
آماده‌ایم تا فعالیت‌های فنی خود را در ایران پیش ببریم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/130267" target="_blank">📅 08:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130266">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ترامپ: ایران کشور زیبای دوست داشتنی و بازار جدید برای آمریکا است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/alonews/130266" target="_blank">📅 08:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130265">
<div class="tg-post-header">📌 پیام #86</div>
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
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/130265" target="_blank">📅 08:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130264">
<div class="tg-post-header">📌 پیام #85</div>
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
<div class="tg-footer">👁️ 26.1K · <a href="https://t.me/alonews/130264" target="_blank">📅 08:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130263">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">👈
ترامپ: باید علیه ایران اقدام میکردیم چون داشتن سلاح هستهای به معنای نابودی اسرائیل و خاورمیانه و به خطر انداختن جهان است‌‌
🔴
اگر ایران سلاح هستهای داشت ، ظرف یک ساعت اول از آن استفاده میکرد و ما هرگز اجازه نخواهیم داد که این اتفاق بیفتد‌‌
🔴
ایران سلاح هسته ای نخواهد داشت و به آن موافقت کرده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.7K · <a href="https://t.me/alonews/130263" target="_blank">📅 02:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130262">
<div class="tg-post-header">📌 پیام #83</div>
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
<div class="tg-footer">👁️ 45.3K · <a href="https://t.me/alonews/130262" target="_blank">📅 02:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130261">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
ترامپ: 159 کشتی ایرانی را کاملا غرق کردیم و همه در قعر دریا هستند‌‌
🔴
تنها در یک هفته و نیم ارتش ، فرماندهی ، هواپیما و نیروی دریایی ایران را 100 درصد نابود کردیم‌‌
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 42.7K · <a href="https://t.me/alonews/130261" target="_blank">📅 02:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130260">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
ترامپ: روند خرید محصولات کشاورزی برای ایران خیلی زود آغاز خواهد شد و من انتظار دارم که حجم آن بسیار زیاد باشد.
🔴
ما پول ایران رو گرفتیم و بجاش ذرت و سویا خودمان را دادیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.7K · <a href="https://t.me/alonews/130260" target="_blank">📅 02:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130259">
<div class="tg-post-header">📌 پیام #80</div>
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
<div class="tg-footer">👁️ 44.2K · <a href="https://t.me/alonews/130259" target="_blank">📅 02:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130258">
<div class="tg-post-header">📌 پیام #79</div>
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
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130258" target="_blank">📅 01:10 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130255">
<div class="tg-post-header">📌 پیام #78</div>
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
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130255" target="_blank">📅 01:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130254">
<div class="tg-post-header">📌 پیام #77</div>
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
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130254" target="_blank">📅 00:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130253">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pRHYJ7no6L0SZy8NWQnr2uzQawAN083gnxSTyVeS9YNh9IgX8_jJlec7J1f6nvdbRegu0EN307tYHaKicmM2a9oAZHrxJSvVOShpPmygdAookOiPENrU8w6i1En_tpbj-l2U5ANL6Q0B2rQsPwCtn11xvbu0Jx8y8GFOcy3cArlfXCSRaid2Wfg_ZaiYaRljFpeMappDNkUaFK6RNnC2vGpYlJVF8c6kjvH7iG9HGbUnsZFGLhE1Zl-2xG6zL_nd6xdT-OLLhXKuTXqK79NBSQ0QGav9hhYt4N4lrxlho0pO1ea3J3Qntt-zGyXPA0CQnXSbl8ZdSEWJYea5K-rrJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
صدا و سیما برداشته یه آخوند که تنها رزرومه‌اش افتتاح شلتر(خونه صیغه یابی) هست رو هر شب میاره راجع به مذاکرات نظر کارشناسی بده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.1K · <a href="https://t.me/alonews/130253" target="_blank">📅 00:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130252">
<div class="tg-post-header">📌 پیام #75</div>
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
<div class="tg-footer">👁️ 58.9K · <a href="https://t.me/alonews/130252" target="_blank">📅 00:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130251">
<div class="tg-post-header">📌 پیام #74</div>
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
<div class="tg-footer">👁️ 63.1K · <a href="https://t.me/alonews/130251" target="_blank">📅 00:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130249">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KZG7uyNlbxcuAiiUjBPfoUhIxJBWkuiuaFQIbmUpE11_gsdN-yWNgGMVMhuyOw1SX9BGsbe179N7X15T9h3uS9d9TzlSLvYWnadbuSKXFuiz0PkXFGb4zh7EiJmIe4nC1bsJfw6JzcQ2rorsKEwCKrNig85Bf0TlETkCrCPgtPq9k_-yBaVztYorfWIRG00KQlpUBsgI4j2rDpBwTFuxKBnA4Z7wjMPo2lKdpX2VMchsR3OgultPT9k-Aabw1XNeHpNHEiQau-7IGH5-e0WN4ZQEIcXdkvyrO6ROu2XnF0OD8lgwq-9BZOOSN3ulrJh0nXq3tWGkSjmDabfa89LYHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JxdwGHd4ed-fUJs8v7v-vJWb1eMnv2k-e6WWJ9QgVRa1N9_Jl5CpuJCTHabvKHhBrU-KqPMDyzO0-orZM-nwKz_ErvJg5e8bNYe55pakTvwYDF-0KLGMVM9nUCYVRLDtmnIrfxS9IpbRC0Jv6EDd4asG3sLR-U6sMHMxdwY3bbAhROH4ON6BRZHSs32uE-nKw7OZibIvc_TUm2Keu8ZYMQ2YoWYTAtIFMaikCP6brQ4XtAj7PmSCytq2icvq94hhwY1BGYLyFBSqqGJ3-PilY3p3lvS-2Dz7wJWZzxMVjcJT1NaXevNr90xLo4m2uEPA89ycOM86Su341cxt274wJQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
محاکمه شیخ "احمد بدرالدین حسون" روحانی و مفتی سوریه در زمان دولت بشار اسد در دمشق شروع شد. او متهم به حمایت و توجیه سرکوب مخالفان بشار اسد است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130249" target="_blank">📅 23:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130248">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
شبکه المنار گزارش داد که توپخانه ارتش اسرائیل مناطقی بین دو شهرک بیت‌یاحون و برعشیت‌ را مورد حمله قرار داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130248" target="_blank">📅 23:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130246">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aDdMI6j1If8GksSbhkYA_QKX6pU3SlZpkTbCfZ0ohLPSBWYZY1X0eYMQWL6LP-A04S7wiraSMBL5U9SlTcCq0JycLMZjoUp-cLlSsPlzAPbPRY4djRNdXOXSwnyAO6tWxsa7bwCp8PC5NgQs5P-IS4P3gdyyMzIaSW19LZnQCpTtr9RXkGcWRA8HEx7dplEtTLHXnLalZqeqxuvTfQsmG3WyJ0E3m1kPyaw9M_2MSX29YdXqNKhY26Zcv-UM4tzdyrh4zk78W3fWuYIhbiAhHzXrw86y7jLRX8Hq5LyAdKQkzfjlDjhtjPgwnyXQLN-meteuObhwnDdYmo1ZWJreTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❤️
حداد عادل:
آقای جدید گفت برید مذاکره کنید
✅
@AloNews</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/130246" target="_blank">📅 23:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130245">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">👈
ارتش اسرائیل: ۶ عضو حزب‌الله رو در جنوب لبنان ترور کردیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.2K · <a href="https://t.me/alonews/130245" target="_blank">📅 23:37 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130244">
<div class="tg-post-header">📌 پیام #69</div>
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
<div class="tg-footer">👁️ 59.1K · <a href="https://t.me/alonews/130244" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130243">
<div class="tg-post-header">📌 پیام #68</div>
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
<div class="tg-footer">👁️ 57.5K · <a href="https://t.me/alonews/130243" target="_blank">📅 23:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130242">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zi6HKd96qkDpVvQD0qAEc_vasXu4R45UCx68j4qG1wGDAKAeIuwDUFG1lW9Vla_pMYVmusfah4F-kpF3Qe5fvQk9lB3pjJw2RqcCukePg6bFiOoJIRCIEooWqO865cHmBYXBiBGddygyeX4KeMgWQ5pL9Zc8MAY4DKSYsSlnW3WADzfIuXN-BVtU-tSGY-GhqLNwBR4LpWHhAbUIYDnVksq4k4VxA0P5ZtcR8SECiKbcdSQSwIEAJP5frXNnBPTfbHgGpslZOoMV6HkGasVyvt_5_EoGyyCLxUmVNeWvserooacSOTlGKedLKm-qyqQUb4_zbWtiQnmfaIR3OTtaHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.5K · <a href="https://t.me/alonews/130242" target="_blank">📅 23:24 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130241">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j6-vfN-IKYLpt3wCtn2o7yCuMm2YFmmXO56zPA2AOu30TGDs-XZFcI017-wElrn_ZR-yCLVp0TAkLxK-DrXsPgmke5KErC11s9Y_XYXaNO43EvUCdlRrUtQ9e8JSzFWrLfaY0b04-S-4aNwcUJSuA6bd7tuPcv9aj2XLPZqAcHQInm-VdnQabcmQCdEkfEPkPoghaz9ce0gQxB87GFwaM5Iqgkg-KplkEUvjdYQrB_a2tMwJf7Wm2u16x1lOBpEgXHefeYoQT6cQHz6TNVp5gqBsDsLokTHtHbgt1lwnQjAgw6ooFK-7c4V7ltiXXv_No2a-CdB7XzrBjbUKnl42rw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دو سالی که برای پزشکیان یک عمر گذشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130241" target="_blank">📅 23:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130240">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/092b312727.mp4?token=DM6pTxeHeES2qDLlMRwXBDTSy9rYq9mdyZzCW4GBIazSIr31HOUW0-g5vNHldBQksmon--85uDGP8W9oe6yBELGO3a99n8KXlaumZgxBtOz151IYHDczq1dIGF-9Ma791gMoBKmWjghqbaDNNedmYAtiDlgz2quFCnmkaaiMh_Tsis4dKC4FnK8ztdJ4ExFZ8T4W9EeXutsWzaqoQmSQsstsnJ3ie4lphTadzbgJIbzBc3rHPVeEuBi9sIPOl0ZzsO2SskbyAD3qMrejRfg5mie0d2xwuG3gICZmT_nxMzplfjiPMY5S-DOFUvarNB9b1UqrEcEEjwzznTTekIMslg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/092b312727.mp4?token=DM6pTxeHeES2qDLlMRwXBDTSy9rYq9mdyZzCW4GBIazSIr31HOUW0-g5vNHldBQksmon--85uDGP8W9oe6yBELGO3a99n8KXlaumZgxBtOz151IYHDczq1dIGF-9Ma791gMoBKmWjghqbaDNNedmYAtiDlgz2quFCnmkaaiMh_Tsis4dKC4FnK8ztdJ4ExFZ8T4W9EeXutsWzaqoQmSQsstsnJ3ie4lphTadzbgJIbzBc3rHPVeEuBi9sIPOl0ZzsO2SskbyAD3qMrejRfg5mie0d2xwuG3gICZmT_nxMzplfjiPMY5S-DOFUvarNB9b1UqrEcEEjwzznTTekIMslg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
قالیباف در سفر خارجی با هیئت مذاکره‌کننده بدون نقاب حاضر شد اما شب عاشورا در هیئت «ریحانه نبی» با نقاب حضور یافت.
🤔
کجا احساس امنیت دارد؟
✅
@AloNews</div>
<div class="tg-footer">👁️ 57.1K · <a href="https://t.me/alonews/130240" target="_blank">📅 23:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130239">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">👈
چین رسما اینترنت 10G رو راه‌اندازی کرده؛ فناوری جدیدی که سرعت دانلود و آپلود رو چندین برابر می‌کنه و می‌تونه یه فیلم کامل با کیفیت بالا رو تو چند ثانیه دانلود کنه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.9K · <a href="https://t.me/alonews/130239" target="_blank">📅 23:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130238">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">👈
عراق پس از بحران مالی شدید مرتبط با اختلالات صادرات در تنگه هرمز، هشدار داده که اگر گروه صادرکنندگان نفت سهمیه تولید خود را به طور قابل توجهی افزایش ندهند، ممکن است اوپک را ترک کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/130238" target="_blank">📅 23:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130237">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
پرواز مستقیم تهران-دوبی از ۱۰ تیر ماه برقرار می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130237" target="_blank">📅 22:57 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130236">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vrFQmBQeGVjrZ5qbGpgWEKfVWA4sWXYyUGDy5nJccj8gxp88cDHI9l4wdTPZ6S_rfFMpE7MHR-6UCHo5vzQbwS8jiY_qkPNjm6Sz7lb2AjSD4HC8Dz5G_uOsZS1Wq_EJWuFI4mYwwg0hr9gCzDvlz47NBMLSt3VFvaKdyaZdGd6LkZXWzSUUPA8elNC3hnkjmQunDm4gXVdCQKyGS90HdeknGqJ1S11KpJ24KiiuRm5bhOJ1A5brxdSEwL-eP4lYySN2KlKW6oehg3HjFYWZPFHxbH9uzdbsvi8OPGVe3kMwXoG7Er7GyO5IThQAd2fpvbGpahXRyFqS6HeVYMc5wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
افزایش قیمت نفت پس از حمله به یک کشتی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.8K · <a href="https://t.me/alonews/130236" target="_blank">📅 22:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130235">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QeiUN_57Tqs_i66TMDufmkyRgpZnB-PPUSShl5Dz6xBAHL0axcZQ-EaJuzAl_LSzE6LgyfY4SpVg46tRtDtf_6zXHECmX_N2HQh9A0YSOI439zgBjLZO6QrUPV-2_BKt9LKgUve6vntoC7Q0hYko_B-aw0iF6sC_YFS2LYiaCggeMw9wZhxUafVWjPr2cU-t6cJ8blKSpFOrN8FAYZ73vXVDwBc_yo7xGbcGQ_J2eO0Qx0Z8pa6JGpHS-UazRyXCe4GHMzDkdZtsKTACxOVL1bEII-p13ulgG33d9N5WqN5eRbdrrduZCP2Nz1BNNcIBgsMiNRbYkwFZLEB7XOrFDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نهاد مدیریت تنگه هرمز: تبعات عبور از مسیرهای غیرمجاز با خودتان است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.9K · <a href="https://t.me/alonews/130235" target="_blank">📅 22:34 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130234">
<div class="tg-post-header">📌 پیام #59</div>
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
<div class="tg-footer">👁️ 58.6K · <a href="https://t.me/alonews/130234" target="_blank">📅 22:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130233">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
ماریا زاخارووا سخنگوی وزارت خارجه روسیه پنجشنبه گفت، هنگامی که آمریکا و ایران به توافق نهایی برسند، مسکو آمادگی دارد که در توافق بر سر پیش‌نویش قطعنامه شورای امنیت سازمان ملل مشارکت کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/130233" target="_blank">📅 22:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130232">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">👈
ارتش اسرائیل: نیروی هوایی یک عامل حزب‌الله را که تهدیدی برای نیروهای ما در ارتفاعات علی طاهر در جنوب لبنان بود، از بین برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/130232" target="_blank">📅 22:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130231">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 60.1K · <a href="https://t.me/alonews/130231" target="_blank">📅 22:04 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130230">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">👈
هم اکنون حمله موشکی گسترده روسیه به پایتخت اوکراین، کیف با استفاده از موشک های سنگین و بارشی
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.7K · <a href="https://t.me/alonews/130230" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130229">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
نرخ اینترنت مخابرات دو برابر شد !
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.1K · <a href="https://t.me/alonews/130229" target="_blank">📅 22:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130228">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">👈
سازمان بین‌المللی دریانوردی: طرح تخلیهٔ کشتی‌ها و ملوانان از تنگهٔ هرمز به‌طور موقت، پس از حمله به یک کشتی در سواحل عمان، به‌تعلیق درآمد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.8K · <a href="https://t.me/alonews/130228" target="_blank">📅 21:52 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130227">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: اکنون ایرانی‌ها می‌توانند نفت بفروشند و پول آن را به دلار مستقیما دریافت کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.9K · <a href="https://t.me/alonews/130227" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130226">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
احتمال بسته شدن مجدد تنگه هرمز!
🔴
سازمان بین‌المللی دریانوردی از تعلیق طرح عبور از تنگه هرمز تا دریافت اطلاعات بیشتر خبر داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.7K · <a href="https://t.me/alonews/130226" target="_blank">📅 21:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130225">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
فوری / ادعای وال استریت ژورنال، به نقل از مقامات آمریکایی: ایران به کشتی باری در تنگه هرمز حمله کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.7K · <a href="https://t.me/alonews/130225" target="_blank">📅 21:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130224">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd736f47d9.mp4?token=Lt8VFn-WWVnHSLV4e6jYHbWZIz6gopTHLqJA7AjSzRUtEu1IOnPf1LMKfjOKSKe-_men-vZkTotwCC3y1gpOqk0WVbfgmrfGgUT8KHJdDcagGwFcdgVTNJmz7108ZsqIhlTSawFsNlN0DENJM4V7kdIBMlVe-ws06_BPcbx-bkYKnXAmn7rVICLO_PtOwiMVs0e88MW1otZ2QPF6uj0-9971l32n0r5WXd9Ovz7JBji2vRWYsHugtMR0RLQoVpQdEwXrCwiPkWUC-ApynyCW0VKiKirm6xlGi1xWTyTEeigOMSi6OELUMrUxxRTKN4qoxrNhcMuhxxsMOTQAgWJyGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
پزشکیان: نمی‌شود برای امام حسین اشک بریزیم اما در جامعه شاهد ظلم، بی‌عدالتی، فقر باشیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/130224" target="_blank">📅 21:27 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130223">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
وزیر دفاع اسراییل: هر دلاری که وارد خزانه ایران می‌شود به موشک یا پهپاد تبدیل می‌شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/130223" target="_blank">📅 21:17 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130222">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">👈
به گزارش کلش‌ریپورت، ولودیمیر زلنسکی اعلام کرد که عملیات ۴۰ روزه سرویس امنیتی را با هدف اثرگذاری بر کشور متجاوز تأیید کرده است؛ عملیاتی که به گفته او برای وادار کردن طرف مقابل به پایان دادن به جنگ طراحی شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59K · <a href="https://t.me/alonews/130222" target="_blank">📅 21:15 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130221">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🔴
فوری / برخی از منابع محلی در لبنان و سوریه، گزارشاتی از تجمع نیروهای جولانی در مرز جنوب لبنان را داده اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.5K · <a href="https://t.me/alonews/130221" target="_blank">📅 21:09 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130220">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">👈
وال استریت ژورنال: تهران در مذاکرات با چین و مصر، پیشنهاد خود برای وضع عوارض خدمات بر عبور از تنگه هرمز را مورد بحث قرار داده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.2K · <a href="https://t.me/alonews/130220" target="_blank">📅 20:58 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130219">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/130219" target="_blank">📅 20:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130218">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">👈
به گزارش نشریه NRC، هلند در قراردادی به ارزش ۲۵۰ میلیون یورو، هزینه خرید ۷۰۰ موشک کروز روتا بلاک ۲ را برای اوکراین تأمین خواهد کرد.
🔴
این موشک‌ها که توسط شرکت هلندی Destinus ساخته شده‌اند، بردی حدود ۵۰۰ کیلومتر دارند، کلاهکی به وزن ۲۵۰ کیلوگرم حمل می‌کنند و از هوش مصنوعی برای تشخیص هدف استفاده می‌کنند.
🔴
مقامات اوکراینی اظهار داشتند که این موشک‌ها از حملات به اهداف نظامی با اولویت بالا در عمق خاک روسیه پشتیبانی خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.8K · <a href="https://t.me/alonews/130218" target="_blank">📅 20:44 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130217">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
بازی جی‌تی‌ای۶ در کشورهای بحرین، چین، کویت، لبنان، عمان، قطر، روسیه، تاجیکستان و تایوان ممنوع شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.6K · <a href="https://t.me/alonews/130217" target="_blank">📅 20:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130216">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SYysEOb_pbbzczw9oTBPiUq06YuRcdm-pBaWSx2Gn9je9A6osuDcvFj3XDQZD1pPx4IfnUN14K2QvaLhgwlj40O4tIxKBk-VlmkKBEuXyRslUVhvgGEw2T7OWcRD3u0GWcn3HvnO-koRu2zJhd5hVmRbJ4h0qO0e3Vm6BSUzUsO0z7iYRlwz2d-zmpwokzN_Ac94snGTrAOrZe5I4MkTODZNMyvcE-HdD2mvNP6L2Y_pF-i86rn1HMNtc1ZTh88-km7Ib32mewcm5DUJgaL0Ys2yIQlq0v0qm7r9fyAMhhuGRUk99pLD5II6ISXEsTsWIKcMvCkiRTae1WKs0gxLow.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 56.5K · <a href="https://t.me/alonews/130216" target="_blank">📅 20:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130215">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 52.6K · <a href="https://t.me/alonews/130215" target="_blank">📅 20:26 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130214">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">👈
بیانیه ایالات متحده و کشورهای خلیج فارس: ما بر اهمیت حفظ روند مذاکرات برای پایان دادن به خصومت‌ها و جلوگیری از توسعه سلاح هسته‌ای توسط ایران تأکید می‌کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/130214" target="_blank">📅 20:16 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130213">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">👈
دبیر کل حزب الله ، نعیم قاسم: صبر ما معادلات را تغییر می‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130213" target="_blank">📅 20:02 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130212">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
نتانیاهو: کارهای بیشتری باید علیه ایران و حماس انجام میشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/130212" target="_blank">📅 20:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130211">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bb13ca9f59.mp4?token=PYN-eOAu12AOtIVHmxKT2Vihm1_zc_tlF_VXd4HQPL4u8eKJsYyRxkO_wMo6EPo_J6UB-9n7sBULzjjHCsazIwPtDbh7c-cRbL1M8SqF4L8VUE1n3G-SoGOGINT9D70-XwjSFHP2j5kLAvC4zRUrcbeenNFb_PID-rNcMTsdSFjAZ7rsOqwniURitzhy7t9_GxDcvfNwB7wQqd4PE6bMhh-6mBG-7C3m1gGqsQPdfDqX1HPSIAY8X4bNXY1CRdr9gu77PM9fewzu44FTO1ju8iGVnkrUNJPS2yzfTVGtQtjh2AT6G80CWVJr6sBOAk2Hc3KDamM_PBmWos3xpfo8Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: در مورد رژیم ایران، من فقط یک چیز خواهم گفت: با توافق یا بدون توافق، تا زمانی که من نخست‌وزیر اسرائیل هستم، ایران هرگز سلاح هسته‌ای نخواهد داشت.
🔴
به هیچ وجه اجازه نخواهیم داد ایران
بمب‌های هسته‌ای توسعه دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/130211" target="_blank">📅 19:51 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130210">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b51b52633.mp4?token=H4S4Vt0D1Pr4yy_Ur5vBNNigERFHydtHOenMKBaACYYKMETRP0fnK2N8XEotZd7klw056N8T0KRj_g7RTNf72QZy6CmK99S3sl90eS1A-wyCLT3-M6lWpIx8fvHiDabGgIJoTyH9Bp7BjtHa2r3KDHMzf9jUeOATdOL7GoO2rTOTsAd2CR3Hkd4xX_fy4mhornp0U_G1GtYORz5p8GnPv1EQjyttDme37953HT7uTvI5iGjhWLffYrhcwdE6cti9plcZV5XE-r3BzukNAfGbaZXms4vV7nykLea8NEKRIIWKpRJoXHpsmcTz37gdO2_BfBwtKtKk9D73uYj0ZGYNYINlvI3v1eBVb5Ei1I-LGSQ6CqJNa-QsqEHU4O--cPbgt7RZxV7XA3l3u1mB3G3sJ5_KrZB7jjQQFd6R5hMQk2FGCH5mJU9B9ZZ3npX2JFwZVX3iuYHqt9LrlgJE3jemqPoxTLt6N_q6UoRl-amD7ePTXezNZzGJqL07C8Uvsw3Rcr2ZgliH0Kdp5C6q1w5_nh6JU7HKRphwU-UD70Udbdya-qSceoNcnh6yYb-hzGq3FH1-e_St1hyvtlqjq0K6cSKqYNeNh0quVFxbIYeK8gYUJCZtBN9PNZV8AsKQJMU5x6lV9Cw2RF8YeZsRKRKmmJqiXqipb8rQ0T1tHlwqdSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: من ادعای نبوت ندارم. اما فکر می‌کنم می‌دانم چه چیزی بقا را در منطقه ما و به طور فزاینده‌ای در سراسر جهان تعیین می‌کند:
🔴
قوی‌ها زنده می‌مانند. برای ضعیفان جایی نیست. آن‌ها شکار می‌شوند. آن‌ها ناپدید می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/130210" target="_blank">📅 19:50 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130209">
<div class="tg-post-header">📌 پیام #34</div>
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
<div class="tg-footer">👁️ 48.3K · <a href="https://t.me/alonews/130209" target="_blank">📅 19:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130208">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8a762ed4c1.mp4?token=dekUK3jjPp2iQyddy8s4YFZcPSsReTKfD6F4HL3J44phVFrdYt3vTladYmNUIrA8H0Ajg9CoJMyqyH1AuT9DpVEXwaQ1NHynbJz44zNA-iYeCM4k98frbUbku6GbuVzpW105fINw5Q4rkon2JAQFZ31HhLQL7hwkSsCIXl4yP0keWsRX0N3FjMIQE6rRLHd8xi5weYcS3ix5BcZT00Ve60fi9x6Ez-sbDBNx5RdAMdGsT1y6FCuKBiYv2aszv-rPuDk6qkjgKoZwfB_GM3KjjZ8Ds7lC7IHkgfKZarHOXNYeRAl3E6eOapw-joYwPjdeGlGBnjb0Ye1mhK2z-OwQbQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بنیامین نتانیاهو: فقط یک فرد نابینا می‌تواند بگوید که دستاوردی وجود ندارد. دستاوردهای عظیمی وجود دارد.
🔴
من همه آن‌ها را فهرست نکرده‌ام چون می‌خواهم شما را بی‌جهت خسته نکنم. شما اینجا زیر آفتاب سوزان ایستاده‌اید—فهرست کردن همه آن‌ها زمان زیادی می‌برد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/130208" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130207">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
نخست‌وزیر اسرائیل، بنیامین نتانیاهو: ما تهدید وجودی فوری را از سر خود برداشتیم زیرا اگر امروز علیه ایران اقدام نمی‌کردیم، بمب اتمی‌ای به وجود می‌آمد که اسرائیل را نابود می‌کرد، و ما این تهدید را برداشتیم تا ابدیت اسرائیل را تضمین کنیم.
🔴
وظایف بیشتری برای انجام دادن وجود دارد.
🔴
بله، کارهای بیشتری علیه ایران باید انجام شود؛ کارهای بیشتری علیه حماس باید انجام شود. در همین حال، آنها توانایی زیادی برای مقابله با ما ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/130207" target="_blank">📅 19:48 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130206">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🔴
فوری / یدیعوت آحارانوت:
نتانیاهو موفق شد ترامپ را متقاعد کند که اسرائیل را از جنوب لبنان خارج نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.8K · <a href="https://t.me/alonews/130206" target="_blank">📅 19:46 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130205">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">👈
نتانیاهو: همچنان ماموریت‌هایی وجود دارد که باید در مقابله با ایران و حزب‌الله شود،از لبنان عقب‌نشینی نخواهیم کرد و تا هر زمان لازم شود در لبنان خواهیم ماند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/130205" target="_blank">📅 19:45 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130204">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sfhpPa70BvigIwwBvVVgoGpoIEkGWQmQMKJtM2JvIrNKqwGoC3k7Cf9XOQkM7Tb_2qeLETfYtfnhMRfsSbKYGIuup8pBhqIcSiNBdVveRVLjZ5p1DfQLrsO9JjcbZilqkEOAM1w-Y_ri_oMtCHZn0MLjJcCZr4cGqdcJ_zqlDNKD1MIbiwWADWxZRMyI8Ns945NE9C_4bP-1mQ3NMjkPZR0_jE30BWTAsU6vdNaKbrp9F5lUUDtGP3tAclu1a7Ut4RJJIHrZymvU0hSeH4qJbvaan50xLRbH5EnVOpvmjIZaG5hKMKVOPm_HKfU-pkTIby6G6xoKPPoMkQdhW0-bdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
به گزارش بلومبرگ، یک شاخص مهم در صنعت هواپیمایی آمریکا پس از شش سال، سرانجام از زیان‌های دوران همه‌گیری کرونا عبور کرده است.
🔴
پیشرفت در مسیر توافق میان ایران و آمریکا باعث کاهش قیمت نفت شده و فشار هزینه‌های سوخت بر سودآوری شرکت‌های هواپیمایی را کاهش داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51K · <a href="https://t.me/alonews/130204" target="_blank">📅 19:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130203">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=lDiuGj0X5LF5DtoWfqq4spjclDwbYrxVTlBDiOau9z3SgE_c586Hw807AmaKRRV93lzF3E0sq1-MiTMFUChxINyyZ3hafK7LAy9aVW78Gu5_6w0RCe34ZZzUD0k2vfUOC9t3gBAegiK7ozHB0uXFUVlANbP2-j_jLzNC1GAg460j4kDADtpLMjgYH0cp3mqw4DQgDgVUGURo7hyK4KVUz2GbmjTy7up9gk4XqIY5q2n32BWQpiEBJmKbqlfEBl4yoAi0e59JLODkYWsNCyID45NwTXFxcG2Zte_Vz7Ebb3z6Tay0h9ru9AXySdOXbLvoZIdBc1lGXcnOA4Rp0Tno_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed090dd487.mp4?token=lDiuGj0X5LF5DtoWfqq4spjclDwbYrxVTlBDiOau9z3SgE_c586Hw807AmaKRRV93lzF3E0sq1-MiTMFUChxINyyZ3hafK7LAy9aVW78Gu5_6w0RCe34ZZzUD0k2vfUOC9t3gBAegiK7ozHB0uXFUVlANbP2-j_jLzNC1GAg460j4kDADtpLMjgYH0cp3mqw4DQgDgVUGURo7hyK4KVUz2GbmjTy7up9gk4XqIY5q2n32BWQpiEBJmKbqlfEBl4yoAi0e59JLODkYWsNCyID45NwTXFxcG2Zte_Vz7Ebb3z6Tay0h9ru9AXySdOXbLvoZIdBc1lGXcnOA4Rp0Tno_DzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تعزیه عجیب در فلاح تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/130203" target="_blank">📅 19:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130202">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
وزیر دفاع اسرائیل: ارتش تا زمانی که لازم باشد، در «مناطق امنیتی» در لبنان، سوریه و غزه باقی خواهد ماند.
🔴
ما علی‌رغم فشارها برای خروج از «منطقه‌ی امنیتی» در لبنان، مخالف عقب‌نشینی هستیم؛ عقب‌نشینی نخواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.6K · <a href="https://t.me/alonews/130202" target="_blank">📅 19:10 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130201">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">👈
مرکز عملیات دریایی بریتانیا (UKMTO): مرکز عملیات دریایی بریتانیا گزارش یک حادثه را در فاصله ۷/۵ مایل دریایی جنوب‌شرقی دهیث، عمان دریافت کرده است.
🔴
یک کشتی باری در سمت راست خود توسط یک پرتابه‌ی ناشناس مورد اصابت قرار گرفته که به پل فرماندهی خسارت وارد کرده است. ناخدا گزارش داده است که تلفات جانی و اثرات زیست‌محیطی نداشته است.
🔴
مقامات در حال بررسی هستند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.6K · <a href="https://t.me/alonews/130201" target="_blank">📅 19:07 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130200">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RaVkIn6raW18XDYmuvZcdxRQHljl7oVrew_KMeMdcMiFl3sWhlDRyrqmUCnPjAQsaPihTqw4kH_hFI1dQAXJ4wwMVTWKjnjoQ-JL0AIHCOTIUjBpsPsdF2m8dWkD7w6-61rO0qKJhOVbzzjbDkqWZ6Fq9_yU0dfgOJW4c5RvTsnztTIRqluA7OfdLhLsgFHotl7BeD8fPRQjy5iLT2pJlBqVjfS3BZa4bBXAzkTIg9zVwxwAsd2Cw1Ui1lrKf7nAcZsZLeUYQSDD4OA0pDAsv4_zdBthySbKfnpD_ZS7ftX-B2QuNDlDY30VNbfLG85dDI3-shiuDaGQ4WvLjBGxcg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سقوط ۵ درصدی بیت‌کوین در ۳۰ دقیقه؛ پایین‌ترین سطح در ۲۱ ماه اخیر
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.7K · <a href="https://t.me/alonews/130200" target="_blank">📅 18:54 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130199">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">👈
ارتش اسرائیل: اگر به دلیل عملیات ما در لبنان مورد حمله ایران قرار بگیریم، با تمام قوا به آن حمله خواهیم کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.8K · <a href="https://t.me/alonews/130199" target="_blank">📅 18:36 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130198">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">👈
وزیر انرژی آمریکا: ایران روزانه تا ۲ میلیون بشکه نفت صادر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.4K · <a href="https://t.me/alonews/130198" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130197">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">👈
مقام آمریکایی در گفتگو با نیویورک پست: وجوه منجمد هرگز تحت تفاهم‌نامه حمایت شده توسط ترامپ به ایران نخواهد رسید. در عوض، پرداخت‌ها مستقیماً به فروشندگان تأیید شده‌ای که کالاهای بشر دوستانه تأمین می‌کنند، ارسال خواهد شد و نه به خود حکومت ایران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.5K · <a href="https://t.me/alonews/130197" target="_blank">📅 18:32 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130196">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔴
فوری / تلگراف: فیفا درخواست جمهوری اسلامی و مصر برای ممنوعیت پرچم‌های رنگین‌کمان در بازی دو تیم را رد کرد
🔴
طبق اعلام فیفا، هواداران می‌توانند با پرچم‌های رنگین‌کمان وارد ورزشگاه بشوند؛ این مسابقه هم‌زمان با جشن Pride در سیاتل برگزار می‌‌شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.9K · <a href="https://t.me/alonews/130196" target="_blank">📅 18:31 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130195">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
وزیر انرژی اسرائیل:  ما از کمربند امنیتی در لبنان عقب‌نشینی نخواهیم کرد، حتی اگر ترامپ یا هر مقام آمریکایی دیگری از ما چنین بخواهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.1K · <a href="https://t.me/alonews/130195" target="_blank">📅 18:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130194">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
لحظه فرو ریختن ساختمانی در ونزوئلا در جریان زمین‌لرزه‌ای که این کشور را لرزاند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.9K · <a href="https://t.me/alonews/130194" target="_blank">📅 18:13 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130193">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
جی‌دی ونس: یکی از بزرگ‌ترین پیشرفت‌ها در مذاکرات سوئیس، توافق اصولی برای ایجاد یک کانال ارتباطی نظامی مستقیم بین آمریکا و ایران بود تا به جلوگیری از تشدیدهای آینده کمک کند.
🔴
ادعای ونس، آن‌ها گفتند: «باشه، خوب، ما کسی از سپاه پاسداران می‌فرستیم که در دوحه با کسی از سنتکام ملاقات کند، و این‌گونه بسیاری از این اختلافات را حل خواهیم کرد.»»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/130193" target="_blank">📅 18:01 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130192">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
وزیر خارجه آمریکا روبیو می‌گوید «خیلی نزدیک» هستیم به «بیانیه اعلام نیت» برای خروج برخی نیروهای اسرائیلی از جنوب لبنان.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50.7K · <a href="https://t.me/alonews/130192" target="_blank">📅 17:53 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130191">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">👈
رویترز به نقل از مقام ارشد وزارت نفت عراق: به دلیل کاهش شدید صادرات نفت در پی جنگ علیه ایران، با بحران مالی حیاتی دست و پنجه نرم می‌کنیم
🔴
در صورتی که سهمیه ما در اوپک به طور قابل توجهی افزایش نیابد، مجبور می‌شویم که تمام گزینه‌های موجود را بررسی کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.8K · <a href="https://t.me/alonews/130191" target="_blank">📅 17:47 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130190">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=X_OgvJbyhNsZtKEzHV3CUEFoqDyPzETfZjDfWIyvhUpjEawTSKyb2qjA6pvCcO5eBq-8dnngBLUJwb4Hmd-bWH2VC9bw78PKEeFXaBbp_eQvnH27iKwpMiv5nrDOR4hjPx_G7xthrFCFd1tUtdUJ7sFwe5EBavvYWIjKLASgouqDAKb_2OdjDl13HgcPaSL4QGFicP51Ct4vuInkbu3guPozqR5wlbm4p9H8KUH4nyldkb6KJ-ziB6LKadbFmjNabJO6nuW2q4GnYMIE9NiIAGtt_n-PgeIlbRtpJwqJB23g1y9hyOQHz5DQsztZtS0hDq8Vmmum5xJma9bendQiuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed03997a75.mp4?token=X_OgvJbyhNsZtKEzHV3CUEFoqDyPzETfZjDfWIyvhUpjEawTSKyb2qjA6pvCcO5eBq-8dnngBLUJwb4Hmd-bWH2VC9bw78PKEeFXaBbp_eQvnH27iKwpMiv5nrDOR4hjPx_G7xthrFCFd1tUtdUJ7sFwe5EBavvYWIjKLASgouqDAKb_2OdjDl13HgcPaSL4QGFicP51Ct4vuInkbu3guPozqR5wlbm4p9H8KUH4nyldkb6KJ-ziB6LKadbFmjNabJO6nuW2q4GnYMIE9NiIAGtt_n-PgeIlbRtpJwqJB23g1y9hyOQHz5DQsztZtS0hDq8Vmmum5xJma9bendQiuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
بیش از ۲۱٬۰۰۰ نفر پس از زمین‌لرزه‌های ویرانگر که ونزوئلا را لرزاند، مفقود شده‌اند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.7K · <a href="https://t.me/alonews/130190" target="_blank">📅 17:38 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130189">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">👈
رهبر انصارالله یمن: پیروزی ایران در برابر دشمنان، پیروزی کل محور مقاومت است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.2K · <a href="https://t.me/alonews/130189" target="_blank">📅 17:29 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130188">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">👈
جی دی ونس: اماراتی‌ها - که تا حد زیادی جنگ‌ طلب‌ ترین و تا حد زیادی طرفدارترین کشور در شورای همکاری خلیج فارس هستند - در حال گفتگوهایی با ایرانی‌ها هستند که قبلاً هرگز اتفاق نیفتاده است، از جمله با سپاه پاسداران، در مورد انواع مختلف مشوق‌های اقتصادی.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.8K · <a href="https://t.me/alonews/130188" target="_blank">📅 17:20 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130187">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
جی دی ونس معاون ترامپ: دستاوردهای مذاکرات سوئیس، توافق در اصل برای ایجاد یک کانال ارتباطی نظامی مستقیم بین ایالات متحده و ایران برای کمک به جلوگیری از تشدید آینده بود.
🔴
«یکی از چیزهایی که می‌خواستیم به دست آوریم، یک کانال در سمت ایران برای کاهش درگیری بود.»
🔴
«آن‌ها گفتند: "باشه، ما کسی از سپاه پاسداران را می‌فرستیم تا در دوحه با کسی از فرماندهی مرکزی (سنتکام) باشد و این همان راهی است که بسیاری از این اختلافات را حل می‌کنیم."»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.7K · <a href="https://t.me/alonews/130187" target="_blank">📅 17:12 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130186">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
کانال عبری: آمریکا ۲۸ هواپیمای سوخت‌رسان خود را از فرودگاه بن‌گوریون به درخواست اسرائیل خارج می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.9K · <a href="https://t.me/alonews/130186" target="_blank">📅 17:00 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130185">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
عراقچی: دولت ایتالیا باید به‌طور رسمی استفاده از خاکش علیه ایران را تکذیب کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.2K · <a href="https://t.me/alonews/130185" target="_blank">📅 16:49 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130184">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=FvtjLS3miIhvqdL-gCJ2sibDu5YLrsDX7limqFqlCYItQZ5bjYuBAMJ_xKJLO7WV9ep8NkPaiurwd4uTTHhq62yppQvdJB6-vaPAibxEYNxs-OTe3HjfNDsHgWlrja4HkmUIm3_0p0jNg7eGaaCT8_fS16CIR_gyve0A2B-72QyOgN8v8LTHEAVSREZi-nPqZAgHYbCR9tVditvcfP98FQC4G7JPY7SWouoMXZhzEFiCjUGN8OszmWmrNT_w5sErTJLFCY60ToNj4L_WJGcdPxlWs8l3M-QFO8OD0meZVQrdQrZPl2VfJQw6xkM8xUMbWQq4h0C9eevhuBbuFy6gUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f844f77e67.mp4?token=FvtjLS3miIhvqdL-gCJ2sibDu5YLrsDX7limqFqlCYItQZ5bjYuBAMJ_xKJLO7WV9ep8NkPaiurwd4uTTHhq62yppQvdJB6-vaPAibxEYNxs-OTe3HjfNDsHgWlrja4HkmUIm3_0p0jNg7eGaaCT8_fS16CIR_gyve0A2B-72QyOgN8v8LTHEAVSREZi-nPqZAgHYbCR9tVditvcfP98FQC4G7JPY7SWouoMXZhzEFiCjUGN8OszmWmrNT_w5sErTJLFCY60ToNj4L_WJGcdPxlWs8l3M-QFO8OD0meZVQrdQrZPl2VfJQw6xkM8xUMbWQq4h0C9eevhuBbuFy6gUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
افزایش چشمگیر تردد در تنگه هرمز
🔴
بخش عمده این فعالیت‌ها شامل ۵۳ مورد ترافیک تجاری است و شناورهای کم‌ریسک بیشترین سهم تردد در این روز را به خود اختصاص داده‌اند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.8K · <a href="https://t.me/alonews/130184" target="_blank">📅 16:43 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130183">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7inM5YysUNUxWeUR1lZsmod9FOYfiINPeCSfKIDQ5pc4zNOfoKof1NQEHbwn2uyADjEEnCQvloaZM3-zE2NK_O1570K6puhGInaoxRDl3sj4kaajuUyPknirkGObkISEjxpM6muFKQRCwkf68YebvX4UhXhwzK1PN9FSwGBUyxtzsdOqV2NwwVuRNo1wq2b3sgAfaVCn5yw402FVgDBn_il2RuJnucOBQaKauWIpJV36q3C-rpvvgSu6-HKREFH-hv1Wq1m-0FfbGz90MYDVzqAjrrFsPlmJQjgMugN0SnzWBC8rguGOsev1RZ44T_Ov680RgTkl2u_-3jDPWnbsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
موسسه کپلر: تعداد عبور و مرور از تنگه هرمز در تاریخ ۲۴ ژوئن یعنی روز گذشته به ۷۰ مورد رسید که نسبت به روز قبل ۱۰۵ درصد افزایش داشته است
🔴
این افزایش به دلیل پیشرفت تلاش‌های مین‌روبی و استفاده بیشتر اپراتورها از مسیر عمانی رخ داده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.5K · <a href="https://t.me/alonews/130183" target="_blank">📅 16:39 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130182">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YjawQGfOvc9jUm5j43P4cuAsuNM9LJCRrSIIPTx6nu0KVb7KyFfN1YddSEsj7aucYlF3LfwfNLHsSdKWINN_VYezgfSd6mPjWhmFhgoInFX1rtrFeZBzKiHjLAuPBDHMnVGfC_BrhFJEBB3m33ijHzKArr1Bc774dEKfWJ-rX-RIW5w7zbPM5uIoh0pULtFkZeBurI-9jqfGQrk5pzPdjQWVyq5z48XhHNturjnnaVaWM00lSFVtkvd6i3X9sE7_06hYsS0rHWG7UXbe3pQUR4dQVUpwjHcbdmMmatSG21gtkCgDSBUrPZaP5K_c9sf2OtbI1lgP9il6hM3jU7kZ1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
کتلین تایسون، بانکدار و تحلیلگر نظام پولی بین‌الملل بریتانیایی: هیچ بانکی برای ایران، صرفاً به‌خاطر مجوز ۶۰ روزه تجارت نفت، حساب دلاری باز نخواهد کرد تسویه‌حساب محموله‌های نفتی همچنان با ارزهای جایگزین انجام خواهد شد
﻿
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48.5K · <a href="https://t.me/alonews/130182" target="_blank">📅 16:35 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130181">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
وال استریت ژورنال : ایران ۳.۸۴ میلیارد دلار را از طریق صرافی رمزارز CoinEx منتقل کرده تا تحریم‌های آمریکا را دور بزند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.7K · <a href="https://t.me/alonews/130181" target="_blank">📅 16:33 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130180">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
گزارش حملات هوایی اسرائیل به مناطق غربی غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 47.7K · <a href="https://t.me/alonews/130180" target="_blank">📅 16:30 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130179">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
وزیر خارجه آمریکا: عمانی‌ها می‌گویند که طرفدار سیستم دریافت عوارض در تنگه هرمز نیستند
🔴
دریافت عوارض عملی نیست
🔴
اینکه ونس مستقیماً در موضوع ایران دخیل است، نشان از اهمیتی است که دولت ما به این مسئله داده
🔴
در جلسه با اعراب، موضوع صندوق بازسازی ایران مورد بحث قرار نگرفت
🔴
توافقی را میخواهیم که امنیت شرکای ما در منطقه خلیج فارس را تضعیف نکند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49K · <a href="https://t.me/alonews/130179" target="_blank">📅 16:21 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130178">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
هلند تیمی به ونزوئلا خواهد فرستاد و حدود ۲ میلیون یورو برای اعزام نیروهای نجات، سگ‌های جستجو و تجهیزات اختصاص خواهد داد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.5K · <a href="https://t.me/alonews/130178" target="_blank">📅 16:19 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130177">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/Ez8mCjNctSftzhVHCZRIZZDHwJ29XOwuu_cD7_fhLwhYk1rp9ajQg_PzGNN-MIysObrDEnt8p_i0uqRbH7j5K1ONJL8Q_7ZgpHdCaQyt2n-j5hzNY9hdKpwY5kCEVzmHn9O3WtkRER83W6aBcoqUXL-bDSakNpbYnFz7oFlugR1URDTEX3_SsErKGgQW5f1UO326rwut22eqgL69ALvpDT1QZM9f3x5B0oj72wIBN3exWD0Ofaye5P_I-yFasMXZUMS8C7xBEyAMkBvTryLNw1Gid6Z8Nl5_qewKh-8JQZVuA8_P2t1Wv0LgidJTr6plAguhd4z85s_UQbmjRIhlsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
سلطنت عمان بدون مشورت با ایران،  بیانیه‌ای صادر کرد و از ایجاد یک کریدور دریایی موقت در جنوب تنگه هرمز خبر داد(رنگ سبز)
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 49.1K · <a href="https://t.me/alonews/130177" target="_blank">📅 16:14 · 04 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-130175">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihz7Srua1O5gB3ETeppfBdGiEgq8iMJ1wcWzpKdxQVfZNsFoX_eF5VFV44FkGU5UN76hCh_H4MSa8Na-sAORSF50B_K6M_kCOXMRFIZ67NgYHojjJPNMQek-b-Bfn5zW52EZjbSEZI32GpeaH7SDPJTXTH2AZBuFh7ad__QQNfkxIKkY-qDwecwZpiEB_22aZhD3H9R1XJV1QSpabWRAi3HVLiYN_uM3Ujea45XKvdHTh4FA8wEMt30vYb6osa3fNi25FDtgpUposG_uGelch8KoMG0oGK6UwMMwXoceEcMJ5d-4ED0F7E9GtU7VySrf3PFyvyKob4frBa_2o6CMTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FTPwUOhqKZrkBeRYicgK4Iy4JdKExIUETFHHaFQG4IByX9Dc7HyMgwLMwZS3QB7Zrk6l06KUpBCkDpIDYC5zDBuwOXBLK6Oi3_roN5IIy_oC6RMrBAFGeRQeeIPAaDk5igUHJU9EonwBH8aAgBPXbSJXIzhKqms4lPyz5GuP3n5WjKG_yUGkEgsc0_nJlecHeBU4Js767ZeVrfDSi2aPPxLbGAywKGQYUsIogql1SqfvtgGeSP8Hpcf6lBINqa3iilSlfOTQ6D3bPWV0tzEcRB6-kKv74qZwCGTKcxMjS0GVKDPQvvkMuXqcuge2rsoiQPk3REnSJ3FkULfoMj7Wig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
قبل و بعد از زلزله‌: لا گوایرا، ونزوئلا.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/130175" target="_blank">📅 16:07 · 04 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
