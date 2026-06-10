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
<img src="https://cdn4.telesco.pe/file/Wnddt4d1UHGbXjSYSQL33owErkEaAUxMdSx03aFpSPMjgVIN0J-8sPQTfo_y7Yxw9BmqaaUaVnTIhEyGtaj5qtaKUjQFMu9bnj6Vqtu-bqYhqjeNrNO1aE_OFf5Uo21W4KfavVRiDrgoZsS5vLV3TtXQO7mbjCrvKvlLgqXaHa9aRW3pXLrZnGVsGMrQClxITzoXAc1_kfm1a1cVoOy2-a7Ilj6M6OWoPPD8HlaYnQm3Np4mq_vCqMn6DLv1Gcvx6d0qCUvFT7gxndjr0k4f-1y0gBfLmYeN55wSkF2gzjPRyjNTcJvdSuCUdvLedpp1riLKOigX4dee9dPySGELrw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 173K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-20 18:02:50</div>
<hr>

<div class="tg-post" id="msg-77476">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/126e9f8e6d.mp4?token=uzlO3daLiJLxTdMUC3l5hW6FyuUy85CoTCoXuWTZu6KxSWV6e-m-1qsoBmyqNvzCl4h46JaESISoOgEl-c9jkK5CdUfqlkVxvoJwGLrJc6zhhqT8Gie7IW4F6s_NtPK3PNkuZHEHtHJVSJRAYuGiotzjhGyc85I6K1pLChtiQwLOVp7_9L36QT4ilZKPEnCZeDJuOmiaUV6CW8RVtGyWb6uabEYLh3coVqSajD99oRI27PO6HjTSwlnCFv0AbvhbB100-0A-STCp1TN-Nu4YvU5NUzCJvo6ZybYLJjojYKXhqAUdHGxDWAHUhe-5zQKfj8dbz0jsSCCVr6oWuyqX-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/126e9f8e6d.mp4?token=uzlO3daLiJLxTdMUC3l5hW6FyuUy85CoTCoXuWTZu6KxSWV6e-m-1qsoBmyqNvzCl4h46JaESISoOgEl-c9jkK5CdUfqlkVxvoJwGLrJc6zhhqT8Gie7IW4F6s_NtPK3PNkuZHEHtHJVSJRAYuGiotzjhGyc85I6K1pLChtiQwLOVp7_9L36QT4ilZKPEnCZeDJuOmiaUV6CW8RVtGyWb6uabEYLh3coVqSajD99oRI27PO6HjTSwlnCFv0AbvhbB100-0A-STCp1TN-Nu4YvU5NUzCJvo6ZybYLJjojYKXhqAUdHGxDWAHUhe-5zQKfj8dbz0jsSCCVr6oWuyqX-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناموس چموش: اغلب انقلاب‌هایی که از سر گرسنگی شکل گرفتند ناموفق بودند
تغییر باید با آگاهی شکل بگیرد. قربانی کردن دیگران برای رسیدن به هدف شرافتمندانه نیست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 1.24K · <a href="https://t.me/funhiphop/77476" target="_blank">📅 17:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77475">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">شهربانو منصوریان چه کراشی شده پسر.  @FunHipHop | AmooFirooz</div>
<div class="tg-footer">👁️ 2.47K · <a href="https://t.me/funhiphop/77475" target="_blank">📅 17:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77474">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CpuM2hAxd04QPk0py2IMTC46UofQc25fagZa_05FXW5KkoqbimRHSXp8jb13MB-1yyEPV-Vx2-GlM-7lY8wbPWIVxKW49SV_RPGDIKx9fDt-aBTg-omEK8ExS6JQ7_QTynrZudyPeuIP-uVrlbujwoIkF0teguR4B4Dibp3e6Z8H5wOf6IVq6svEQznB17-xYxyRf8FELwW1Q0Of02_nXHaUTPYhfQO6RkyKIFGLexBnZq1lllzYUmVtwm8ZuKGTmXtM9aHSJ6a4IJrPHcP1mtFX_TjR3KDLygkj5gz3ob8wDSo1haUExZZmTdRtHmEBEy0P2uFwy_Bi47yIkJxm0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهربانو منصوریان چه کراشی شده پسر.
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/funhiphop/77474" target="_blank">📅 17:41 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77473">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TERvtgIS-CP5BYshblsGaAzctDyltzqkIQ8uc299YUaJpSFK2fDg16C0MdguUyV54W74J7kKStIAAc_8wPK_koIeQW-QgccBe2x2vax5o7Z6OUe00-a1jRLOuEzgywf5tL_cQG1CLboz8-u5jHQ3D4jWTUf1tcTXP7wiT_-LsXdhNq6kaW-llrLuaBJ5MDTz5_ncDOL4qYRFfl8EyKle4s-TXzCw0KvuSX6K2eUUf7IZXslUTj7HJ-8xT8yLKIF0I0EJdLwVeVqgDI0GrFRpkqQiyhd2cneFXrey7kRuhB8sSpqRs52tE4XMiWGe249Y7bMuT1ncW7x6s3mLJ4lcAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">«تو کون نرو» اگه آدم میشد :
@FunHipHop
| AmooFirooz</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/funhiphop/77473" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77472">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">با ماف بت از جام جهانی پول در بیار چون کلی هدیه هم خود سایت میده
💵</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/77472" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77471">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vBhTOjG_02Dbwd1lUI1yehwyZK3QRzXmouLHhjQPMpmAIAfvg2cpoPkP_WzyLYPWv1dji2B7edH_Yjtsm3B3COPlbhgtnw4VloJMgSyxk9-G7xnQwPdT5CPIbNl9gKNHEh9-e1IR0U8ZF-SQzkx-ELBFaiFKXaauhOWs2NZbeZ8uPj-Ri7a1wNKppujh_YmJP3ksFa-ERmNCGNBaNvI4JrMV5oFvam-jAHdTtFq9SDceMpOVSz_X_cT7XUtAn2NDiuPHqT1WguboyO7cENykxtzhlsLotyL6gKt2fuiDm60nxt_Ct84EnBOcrAETAmtxh5P6m7Y1QC5uPVg1VX8pew.jpg" alt="photo" loading="lazy"/></div>
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
کانال تلگرام سایت: g20
🅰
🔹
https://t.me/+3Zxs6WU7L_UzY2Fk</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/funhiphop/77471" target="_blank">📅 17:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77470">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/araUVRGaq3QzmdN_2-L6dJyjdeAtFSH4byhI2nWdh9-pTRcOQ_nuyQh2k-7P6h0XYiF9lyE1tJs7642d0JDD5P6ndn6JEH2Rmt4X1E_NG2wZ46kbtpcxksoaCT--9_QWw0xUg_aB01nrq3DICQ8P_n3HdisR0mvVxQNDbhT4y7F8_48lgoVLJRuWiN5NRGF25tRmRrsboi9lsvMhdYq2N1BdkVfrOaZv3vZmyKfUgIZF9Yl-9DcUuD02WWpg5ydlH0c40wIRIjCZuHtduVqAfiFvVq6QLWDyzxXHzFr-_kthe8MnxPMi_xOMk4dmUQKLVh1GAYKKhT4WuoCZlJB_Hg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم
😂
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 5.33K · <a href="https://t.me/funhiphop/77470" target="_blank">📅 17:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77469">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامپ به کانال ۱۳:
به زودی حملات بیشتری علیه ایران پیش‌بینی می‌شود، احتمالاً از آنچه دیشب دیدیم، قابل توجه‌تر خواهند بود! علاوه بر این، یک گزینه واقعی برای حمله به تأسیسات برق در ایران وجود خواهد داشت.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 6.06K · <a href="https://t.me/funhiphop/77469" target="_blank">📅 16:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77467">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این دفعه بخدا عی ماخارنا ماخارنا ماخارنا  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 6.46K · <a href="https://t.me/funhiphop/77467" target="_blank">📅 16:49 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77466">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">۸ ‏فروند جت جنگنده F35 B در راه خاورمیانه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.27K · <a href="https://t.me/funhiphop/77466" target="_blank">📅 16:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77465">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">چندین بمب افکن B52 در انگلستان مستقر شدند.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 7.66K · <a href="https://t.me/funhiphop/77465" target="_blank">📅 16:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77464">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">میگن
ترامپ ۳ میلیارد دلار اسکم شده
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 8.39K · <a href="https://t.me/funhiphop/77464" target="_blank">📅 16:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77463">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">فاکس نیوز:
مذاکرات آمریکا و ایران همچنان در جریان است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/77463" target="_blank">📅 15:58 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77462">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ:  هنوز با ایران کارم تمام نشده است.  ما ۵۵٪ از آنچه ایران در طول آتش‌بس بازسازی کرده بودند را نابود کردیم. این احتمال وجود دارد که من به حمله‌ی دیشب ایران به کشورهای عربی واکنش نشان دهم.  دارم به آن فکر می‌کنم. حملات بیشتر آمریکا به ایران یک گزینه‌ی…</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/77462" target="_blank">📅 15:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77461">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ویویویویوی
I24NEWS:
ترامپ دیشب با نخست‌وزیر نتانیاهو صحبت کرد و او را در جریان حمله مورد انتظار امشب قرار داده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.87K · <a href="https://t.me/funhiphop/77461" target="_blank">📅 15:34 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77460">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">ترامپ:
هنوز با ایران کارم تمام نشده است.
ما ۵۵٪ از آنچه ایران در طول آتش‌بس بازسازی کرده بودند را نابود کردیم.
این احتمال وجود دارد که من به حمله‌ی دیشب ایران به کشورهای عربی واکنش نشان دهم.
دارم به آن فکر می‌کنم.
حملات بیشتر آمریکا به ایران یک گزینه‌ی بسیار واقعی‌ست.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.62K · <a href="https://t.me/funhiphop/77460" target="_blank">📅 15:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77459">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MDXPj0LEBgzSoV5Gv3O02agWGA4N-EtAz7YBAPXcvckoOCRrl6mtjWx4sbtGylWpuszKREZCOOZIchEBOOJEmzxUR4TSXbtSuoiZBUL0UuJNIQw5mgBZtgQ0EvExlV8Qg6oBQKfekXRqcosa5pyx-8Xt-X-1NKwl1K0crIf5rthgKw5p4WtUJbxkgpQKsUwxkOq76KWaQZBk25PmcXsJugkuEtPN8IRGBtvnOTThNplHwubBj4E0mi3e43OQ8G2_U8X-_sUQWaXW2I3dkwz___wteH1B1HAmyexPOLdxVF8x-6EumjGAjIXTrnDLPBvzP_l3ptNVD6HizY26MQtGXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویر بالا رو توصیف کنید (۲ نمره)
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/77459" target="_blank">📅 15:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77458">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aewTbTA2bO_LLl9s51_igFWyPzxEe40W9JU34pfLd2ClYJzNZ_zURouXJCi-2o3wD6N-mWZzWYyFAd2IIcHlKLGzdfnZoXsbFLg3pc7f-aJi1ClJjAGy6z_sG6MqKg_dCq1u-vfnwr_LoL1bScK9BlGtVvt6erEZTnZNhQ6Ek_I3XET_880JKNDSKXtnHW6LlSPfxOWOrhsvwP4TNVrcN0ptziGA0Bp-vRoDdkGBUBs2lTwzX_Ee2RkgHCAY5r64amDP7MDjWdQIyOOBDZgxt30UFN3eSArE9LTPU5pFlApFMqF8JLWHO-pNVgwWz1jdZnFvlNXoZuZVoZQ-MaxeCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ باز از الله تشکر کرد
🙏
:
رسانه‌های خبری جعلی از گزارش دادن دربارهٔ اثربخشی محاصرهٔ دریایی ایالات متحده خودداری می‌کنند، موفق‌ترین محاصره در تاریخ جنگ‌های دریایی.
هیچ چیزی عبور نمی‌کند مگر اینکه ما بخواهیم. این یک دیوار فولادی است!
ایران هیچ کسب‌وکاری انجام نمی‌دهد، حقوق نظامیانش را نمی‌پردازد و هیچ یک از صورتحساب‌هایش را نمی‌پردازد و به سرعت در حال تبدیل شدن به یک کشور شکست‌خورده است! مقدار زیادی نفت در حال هدر رفتن است.
الحمدلله
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.97K · <a href="https://t.me/funhiphop/77458" target="_blank">📅 15:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77457">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">ترامپ باز می‌خواد بترسونه:
ترامپ به فاکس نیوز گفت که نزدیک است دستور حملات بیشتری را بدهد که به زیرساخت‌های انرژی و پل‌ها در ایران هم آسیب می‌رساند زیرا مذاکره کنندگان ایرانی بیش از حد همه چیز را کش داده اند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/77457" target="_blank">📅 15:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77456">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">توماج صالحی به قیام دی ماه تیکه انداخته و گفته انقلاب هایی که بخاطر گرسنگی شکل گرفته همیشه ناموفق بوده
پ.ن: چقد یه نفر میتونه مادرجنده باشه
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77456" target="_blank">📅 14:59 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77455">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">فاکس نیوز:
مذاکره‌کنندگان قطری امروز صبح به تهران سفر کردند، با هماهنگی ایالات متحده، تا با مقامات ایرانی دیدار کنند و تلاش کنند شکاف‌های باقی‌مانده در روند مذاکرات را پر کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.01K · <a href="https://t.me/funhiphop/77455" target="_blank">📅 14:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77454">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GX7z9J-6FQwRIeaCSvJ7xTtxOTc2mS9Y3FI_KZD8P9K_mIHVf-5o9FeOP8byqspU4krYhMBtEyoTS-8zWRkcOt2okTd8mXcIcBxREQX5FhdBRGoMTKOQJqRttlszBnj2EnB9IEl9UC-oHSrB5OuQZX4gJQZonUn3xI0LTWnpaNGZc_uNJ_rwLDTNvlocr7ioSFskb2KpthfVtMazWaV9A7QBk0gecyLmC6bTGlPnpe9w11PPcixVrPWGwxfRuFFhKrheaUMdR6OlRaobrVVGVekTWpqv4DsOHlF554w1Wr_NMCEFK8nuIpS5juMlMZVIOGOQXEHRNju8NWtBUxAzoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت جدید ترامپ:
ارتش ایران یک آشفتگی کامل و کامل است. بسیاری از آنها، مانند نیروی دریایی و نیروی هوایی آنها، دیگر حتی وجود ندارند - آنها کاملاً شکست خورده اند.
ایران همه حرف است و هیچ اقدامی نیست. قلدر خاورمیانه مرده!!!
آنها برای مذاکره در مورد معامله ای که برایشان عالی بود خیلی طول کشیده است، حالا باید بهای آن را بپردازند
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/funhiphop/77454" target="_blank">📅 14:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77453">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">فک کن معروف ترین آرتیست مملکت از پشت تلفن زندان موزیک خونده داده بیرون</div>
<div class="tg-footer">👁️ 9.47K · <a href="https://t.me/funhiphop/77453" target="_blank">📅 14:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77452">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">واقعا این ترک جدید تتلو رو گوش دادم خیلی ناراحت شدم، درسته خارکسه بود ولی اگه قرار بود خارکسه بودن جرم باشه نصف کشور الان میباید زندان میبودن
ول کنید این بدبخت روانیو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/77452" target="_blank">📅 14:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77451">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دستاورد طلایی جنگ های اخیر تو سهمیه کنکور سالهای آینده شکوفا میشه
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77451" target="_blank">📅 12:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77450">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">دیروز روز جهانی سکس بود برا همین تو خاورمیانه همو داشتن میگاییدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/77450" target="_blank">📅 12:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77449">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سلام صبحتون بخیر، متاسفانه دیشب خواب بودم متوجه حملات سپاه به کشورای خلیج فارس نشدم.
#بیکینی_باتم_تسلیت
💔
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77449" target="_blank">📅 11:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77448">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ممرضا بنازمت دیشب بعد از مدت ها خندوندیمون</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77448" target="_blank">📅 10:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77447">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">سوپرپانچ دیشب شایع که جنگ فیدش کرد : کونمو مشتی بخورید.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/77447" target="_blank">📅 09:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77445">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CSvEga9r9WYbTKOSFbnrG9O2YyyIDeiKuCBGXnKTiWfvPTU5p0XZi-Jye3kTyUdlX171mkLxWP_GGGVUWnlJHLx8owdvpzsR03nxICn-Fv4Tgy01owqv6bxTrpX-CFCTxthfHaVyKze5h_j1s2JI6ye09ErMZq9GFV3BCLlTfNmjH255Pib7J3wkcdj7fRNV1M9iNhqrZMb4MEFtxI8fyTTrq3qc5es3NVT4cNkSMC9jxKWEghqCre_Qu6S_4RLC5Pa-JivcVmWqzlP-9VYebuDa-GxNnyZKEC5cEPI25tpRntavCoGWqVvW6KRi3klIuDJu5vsPzjWiIoD5FeL_sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/fGs5yjKmJVHY1jVkN1rTEPLND5ECC4gzAruD-uD2OX-A-HoVihnMLx5aM0aKFTZnZXui_DJfq4a4gwmk_cmnBIMgEL10CQf1oyGKHrNuwJB39W-VauAVRXZtxaR2O9PKx5U9rNVH7n1m1xwHKd9vS4hH_CgNnQxrV-lrMZvPJ2TAnb9DAcFdtWJ-9P-OUyJwdhQeli4MbfGdQx-RwUypWivf19Xhot_Uy_bNhPoZP3x29AFb8gUL6waB4M-RnP0RHcS19WY9BbBuT_bMfZ_I1y0L25CDzwYV-HrmQ9qlYY9NDu4lqBmF4E3-UIZadpHUXyMSRXGwi5cN2uOqQR1wRw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">فقط و فقط یک روز تا شروع جام‌جهانی.
@Funhiphop
| AmooFirooz</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77445" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77444">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/o6KaNWgNCKMr8k4PiUZyg97Jqtu3zrO_C4WSo0iqXpBr_R6c8enXGY1ARiLRohxb2D_M5zMx1DztGc2KElC30oS05Rm9wqkJaZMGxpWaK_UUsdPY6h0ASbQL1mYWN2-EAfuFFR3eimMoajsKfY5pn4CM-17iUVXZ0EFxoKlSkoX7LxOWs9ZWn53ltsNA4wu0a4fpKTXDnRSlwda11OerdbYQCkRN6yApC_vDvxRg3UQjWh0Kzf4negR0haIiebM8V00caY_Pxxg-JXK-jJh329oWrCgrxnQRGmJt1us_YOlFKWPipGF-a0TlY5gd_G3Evj9mb6vSmD0AXyp6SESDKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
پرتغال
🇵🇹
-
🇳🇬
نیجریه
🏆
رقابت‌های دوستانه بین‌المللی
🌍
🕔
چهارشنبه ساعت ۲۳:۱۵
🏟
ورزشگاه دکتر ماگالهیز
🎲
با بیش از ۴۰۰ نوع آپشن پیش‌بینی
⚡
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
پرتغال در
۱۰
دیدار اخیر خود،
شش
برد و
سه
تساوی کسب کرده و در
یک
بازی شکست خورده است.
✅
نیجریه در
۱۰
دیدار اخیر خود،
شش
برد و
چهار
تساوی کسب کرده است.
📈
میانگین گل در
۱۰
دیدار اخیر پرتغال
۳
.
۶
گل در هر بازی بوده است.
📈
میانگین گل در
۱۰
دیدار اخیر نیجریه
۲
.
۶
گل در هر بازی بوده است.
🧠
اگر دنبال جبرانید، یعنی از مسیر تحلیل خارج شده‌اید.
👍
ورود به سایت با فیلترشکن
R20
🅰
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن اختصاصی
💻
@BetForward</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77444" target="_blank">📅 09:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77443">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">وزیر علوم: سهمیه جنگ ۴۰ روزه در کنکور ۱۴۰۵ قطعی شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77443" target="_blank">📅 09:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77442">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">هرچی نخاله تو ترکیه و امارات بود کم کم دارن برمیگردن ایران.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/77442" target="_blank">📅 09:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77441">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">وای نه تروخدا بس
آژیرها دوباره در بحرین فعال شدند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/77441" target="_blank">📅 06:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77440">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">آژیرها در کویت فعال شدند.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/77440" target="_blank">📅 06:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77439">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">آژیرها در کویت فعال شدند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/77439" target="_blank">📅 05:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77437">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی: بسم الله قاصم الجبارین فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/77437" target="_blank">📅 05:36 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77436">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=BdHp5MZ5dSJ6_yNLcNOhR6pzW7VaT47wqeU1nG2sJ7icZHa2ZXizgyMN-hyTTGfbSdHH_-MgUXEUumOsPx1cI0qEEvwKhkH1qWVDYCTDpX2YQy5QU29Q3F95gWoO3E3yt8QPaHwcu2dTM5i7gZnRnqS1N_OVokJKFpitiT0HomyNdyUCcbfXFZXPd6J3uaMORXBSSO3mzBw7jbLISJ0X2nQKr1OgOD5u-hRfRMJnaKeK5ZDiQ4TmQsP_oT1IHfzfBGWNk6kgMs3LDzw6b5z6txnqZ3pqaQJyNdGyZ3klPeEkuAUTqSmh5-MLNvLpFRNXNEZYnpr6aDRcpvR5HmVK1Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a936874c3.mp4?token=BdHp5MZ5dSJ6_yNLcNOhR6pzW7VaT47wqeU1nG2sJ7icZHa2ZXizgyMN-hyTTGfbSdHH_-MgUXEUumOsPx1cI0qEEvwKhkH1qWVDYCTDpX2YQy5QU29Q3F95gWoO3E3yt8QPaHwcu2dTM5i7gZnRnqS1N_OVokJKFpitiT0HomyNdyUCcbfXFZXPd6J3uaMORXBSSO3mzBw7jbLISJ0X2nQKr1OgOD5u-hRfRMJnaKeK5ZDiQ4TmQsP_oT1IHfzfBGWNk6kgMs3LDzw6b5z6txnqZ3pqaQJyNdGyZ3klPeEkuAUTqSmh5-MLNvLpFRNXNEZYnpr6aDRcpvR5HmVK1Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بیانیه‌ی سپاه پاسداران انقلاب اسلامی:
بسم الله قاصم الجبارین
فمَنِ اعْتَدَى عَلَيْكُمْ فَاعْتَدُواْ عَلَيْهِ بِمِثْلِ مَا اعْتَدَى عَلَيْكُمْ
به دنبال عملیات موفق نیروی دریایی سپاه در اصابت قرار دادن ۲۱ هدف در پایگاه‌های هوایی و دریایی آمریکا در منطقه و ساقط کردن یک فروند پهپاد MQ9 در آسمان شهرستان جم، با توجه به تداوم شرارتهای دشمن در تکمیل عملیات مقابله به مثل، قوای اسلام و رزمندگان شجاع هوافضای سپاه توسط موشک های سوخت جامد دور برد خود ۴ هدف مهم از جمله آشیانه های جنگنده های F35 در پایگاه هوایی و مرکز فرمانده کنترل ارتش کودک‌کش آمریکا در الازرق اردن را مورد هدف قرار داده و منهدم کردند.
نیروهای ما آماده پاسخ کوبنده و قاطع به هرگونه تجاوز مجدد دشمن هستند و عواقب هر تجاوز مجدد بر عهده دشمن آمریکایی میباشد.
و ما النصر الا من عندالله العزیز الحکیم
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/77436" target="_blank">📅 05:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77435">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77435" target="_blank">📅 05:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77433">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">یه موشک بالستیک دیگه از اصفهان شلیک شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77433" target="_blank">📅 05:14 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وزارت دفاع بحرین: تمام موشک های ارسال شده رهگیری شدن.  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77432" target="_blank">📅 05:11 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">وزارت دفاع بحرین:
تمام موشک های ارسال شده رهگیری شدن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/77431" target="_blank">📅 05:05 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.95K · <a href="https://t.me/funhiphop/77430" target="_blank">📅 05:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">انفجار تو بحرین گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.26K · <a href="https://t.me/funhiphop/77429" target="_blank">📅 05:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KkHtStg309gNtkBn4UEODJuwC-Xseadl0v2vTV2iIyIgd3JoRu3CETioZ2y2gTdRTJbsxygi77K4cYxfb9vhWpo_HGMPpCmOsSp4t_zFn-3XJ40jRMCyozoz0MojTe9WQxTv4XGLN9uMn-AvzF2xhKsT7R5daXVvS9upLbw3sVZPK6-cdpymCywTV7NEy95hEAoONX1fqpEiR6YXhUfF0mwyobQljsMrj4D9yBa2KbdJLl8Q_pzHePWUXI0jxUIvBY1VI1_aLo_f7SXH7scT-X1VOW3LHfzvdM-xj7IuCbRWXjepz3k62PlZ6a8vpkd0fSmz_P4Rp7-Cveh2xi_nIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بحرین به شهرونداش هشدار داد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77428" target="_blank">📅 05:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">اوه اوه سپاه جدی جواب داد.
گزارش‌های اولیه از حمله‌ی پهپادی سپاه پاسداران انقلاب اسلامی به مقر کردهای منطقه‌ی اربیل عراق.
🔥
🔥
🔥
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.83K · <a href="https://t.me/funhiphop/77427" target="_blank">📅 04:56 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">احتمالش بالاست که موشکا وسط راه فیل شده باشن. چون ما تا الان باید گزارش برخورد می‌داشتیم درحالیکه هیچ کشوری تو خاورمیانه هنوز آژیر هشدار هم نزده.  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/77426" target="_blank">📅 04:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.4K · <a href="https://t.me/funhiphop/77425" target="_blank">📅 04:48 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f03f509353.mp4?token=Hr-ykB7Jp5BQzT1vMiHqikt8xp-DyP6RS2_PtiS_niti2DxCm2TrWLI38eTxTP77FSC9F_q5mKfDFmCmJPq5CWld3QdetVSaeJ0jna2QrvMBsYwVcmcrYIwLDoRmYBftJ3eZOAtR2myXgLkNsQALiyHF0L5O2p3AFaK7j_EBR68U3AtFjcm7JAzrhiGcuR4sTG0i0TBY71rG4aq0rljMSSpXblIO1VNpt5hMs0mU4vUTTv5Z8uVmSNkdF7KKIscQbybnhmFTpDrh6sZ5VKZEyVap4QwtgXdTTeMeIT_H5l0dW7dh8taD1yxoaRnBgKGE-B2tEnwpA8IidUKPXa21fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f03f509353.mp4?token=Hr-ykB7Jp5BQzT1vMiHqikt8xp-DyP6RS2_PtiS_niti2DxCm2TrWLI38eTxTP77FSC9F_q5mKfDFmCmJPq5CWld3QdetVSaeJ0jna2QrvMBsYwVcmcrYIwLDoRmYBftJ3eZOAtR2myXgLkNsQALiyHF0L5O2p3AFaK7j_EBR68U3AtFjcm7JAzrhiGcuR4sTG0i0TBY71rG4aq0rljMSSpXblIO1VNpt5hMs0mU4vUTTv5Z8uVmSNkdF7KKIscQbybnhmFTpDrh6sZ5VKZEyVap4QwtgXdTTeMeIT_H5l0dW7dh8taD1yxoaRnBgKGE-B2tEnwpA8IidUKPXa21fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینا همش برنامه امریکا واس جام جهانی هست ساعت خواب ها با امریکا تنظیم شده دیگ میشه راحت بازی هارو نگاه کرد.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.45K · <a href="https://t.me/funhiphop/77424" target="_blank">📅 04:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نخوابید که سلطان بیدار شده  ۳ موشک بالستیک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/funhiphop/77423" target="_blank">📅 04:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بزارید سید مجید نقطه زن بیدار بشه تلافی میکنه امشبو</div>
<div class="tg-footer">👁️ 8.23K · <a href="https://t.me/funhiphop/77422" target="_blank">📅 04:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.76K · <a href="https://t.me/funhiphop/77421" target="_blank">📅 04:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">حملات هوایی امریکا تکمیل شد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/77420" target="_blank">📅 04:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77419">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید: در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان…</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/77419" target="_blank">📅 04:26 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77418">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قرارگاه مرکزی خاتم‌الانبیا می‌گه ما پاسخمون دادیم تموم شده رفته شما داغ بودید نفهمیدید:
در پاسخ به تجاوز ارتش تروریست آمریکا در مناطقی از جنوب کشور به بهانه واهی سقوط بالگرد خود، برخی از پایگاه های آمریکا که در منطقه که نام نمی‌بریم هدف هجوم قدرتمند ارتش قهرمان جمهوری اسلامی و دلاورمردان سپاه پاسداران انقلاب اسلامی قرار گرفت.
ارتش جنایتکار آمریکا بداند در صورت تکرار تعرض به جمهوری اسلامی ایران، حملات سهمگین و گسترده تر علیه بانک اهداف تعیین شده در منطقه انجام خواهد شد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.55K · <a href="https://t.me/funhiphop/77418" target="_blank">📅 04:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77417">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=HXZHuV3Rz8JiTUUB_9QF006CmKHkLb2bvV59SZQdL-Q9Hue1V72Up7WoXfYbNTb_BJeFNgPCSe4GQpt8x0Nm8yGVJJCxNLCyyNxdJG5GlUdcbOxRfoN3voHS9vHaboeLejweu-X2aIXqeBvYWHjxphREj7OvGJeQokOB9joFZqQjpWc9Zsj4B2kQCcWYconHuSCHqDit9gdQBzu9boL9FQCA-qfeAePahv7E-dvaWgv-g3tpRbfpTOcm25etpMnVKUjyvnbqbTDEf_rXFNMpoes891jn1ftAMkpGvrd2T_KDNW-fvJjlC5EG6QZUYui_xHa6qJNz3CgUAoFwaVd6vak9AnKNCtJ0mqykZ0UgYSZZ1kVzwClN40UP5W4_y5oNXLwb1VfAKyge9TvtCqCChMJZJZbIrNWwHNsnGxjdZfNH6Mne41yQhmtu9UB5f9pD4B_QQ7wyRCKjqhkg-dwNOZiaAswiMpfUFGrsvdarRd6s7xJOY0QhyPl4g3vQHBf5F6JjAyVxQfpHfY3MLXs0pLvLCG2EC0WSONvp33GIQBevy8Sc-15ulj9yZI810ewnSG6kYH0icIIhywuEvClRuPZrpDm67Q4HiEY8q9hRv-i1NpilSKil3zvZHj0NQyUV6jb3BanTrI1ghGrKXvdeXyGWDwNskRqU5eEGlxZo1ZA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f906ee6c6a.mp4?token=HXZHuV3Rz8JiTUUB_9QF006CmKHkLb2bvV59SZQdL-Q9Hue1V72Up7WoXfYbNTb_BJeFNgPCSe4GQpt8x0Nm8yGVJJCxNLCyyNxdJG5GlUdcbOxRfoN3voHS9vHaboeLejweu-X2aIXqeBvYWHjxphREj7OvGJeQokOB9joFZqQjpWc9Zsj4B2kQCcWYconHuSCHqDit9gdQBzu9boL9FQCA-qfeAePahv7E-dvaWgv-g3tpRbfpTOcm25etpMnVKUjyvnbqbTDEf_rXFNMpoes891jn1ftAMkpGvrd2T_KDNW-fvJjlC5EG6QZUYui_xHa6qJNz3CgUAoFwaVd6vak9AnKNCtJ0mqykZ0UgYSZZ1kVzwClN40UP5W4_y5oNXLwb1VfAKyge9TvtCqCChMJZJZbIrNWwHNsnGxjdZfNH6Mne41yQhmtu9UB5f9pD4B_QQ7wyRCKjqhkg-dwNOZiaAswiMpfUFGrsvdarRd6s7xJOY0QhyPl4g3vQHBf5F6JjAyVxQfpHfY3MLXs0pLvLCG2EC0WSONvp33GIQBevy8Sc-15ulj9yZI810ewnSG6kYH0icIIhywuEvClRuPZrpDm67Q4HiEY8q9hRv-i1NpilSKil3zvZHj0NQyUV6jb3BanTrI1ghGrKXvdeXyGWDwNskRqU5eEGlxZo1ZA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لیکرها با استناد به منابع معتبر سیزن آخر ایران رو اسپویل و یه فیلم از شبیه سازی انفجار یه بمب اتم تو شهر وسط اخبار صدا سیما پخش کردن.
🙏
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/77417" target="_blank">📅 04:12 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77416">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">اهواز رو هم زدن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77416" target="_blank">📅 04:09 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77415">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">اهواز رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/77415" target="_blank">📅 03:57 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77414">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">صدای انفجار تو برازجان گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/77414" target="_blank">📅 03:55 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77413">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">گزارش‌های اولیه از پرتاب موشک‌های کروز ضد کشتی ایرانی از بندرعباس به سمت ناوهای آمریکا.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/funhiphop/77413" target="_blank">📅 03:54 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77412">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">شین: سه موشک شلیک شده  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 8.1K · <a href="https://t.me/funhiphop/77412" target="_blank">📅 03:51 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77411">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">سپاه پاسداران انقلاب اسلامی:
آتش پرقدرت پدافند مقتدر و یک پارچه‌ی نیروهای مسلح، یک فروند پهپاد متجاوز و متخاصم دشمنان جنیاتکار را بر فراز آسمان امن جم در استان بوشهر ساقط کرد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.48K · <a href="https://t.me/funhiphop/77411" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77410">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">صدای انفجار تو زاهدان گزارش شده.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.07K · <a href="https://t.me/funhiphop/77410" target="_blank">📅 03:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77409">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">ایران بالستیک شلیک کرد   @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/77409" target="_blank">📅 03:45 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77408">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ایران بالستیک شلیک کرد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.72K · <a href="https://t.me/funhiphop/77408" target="_blank">📅 03:43 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77407">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">بندرعباسو دارن بد میزنن  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/77407" target="_blank">📅 03:42 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77406">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">جم تو استان بوشهر رو زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 8.9K · <a href="https://t.me/funhiphop/77406" target="_blank">📅 03:39 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77405">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">یک مقام ارشد آمریکایی به کانال ۱۲ اسرائیل گفت که موج سوم حملات به ایران اکنون در حال وقوع است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.91K · <a href="https://t.me/funhiphop/77405" target="_blank">📅 03:37 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77404">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">بندرعباسو دارن بد میزنن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/funhiphop/77404" target="_blank">📅 03:29 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77402">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">صدا سیما:
حملات امشب آمریکا تو سیریک به دوتا مخزن آب بوده.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77402" target="_blank">📅 02:10 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77401">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Q9gSOlEz1XO1HYnh0ZrV0ua39LgPWF-YxSTVbESHJ03dhRSWpxkjz0ay7qXMPzgJ-5St5olpsmG1XDJy_my5Z7qGyTJ-giUpmDYkytII6qBLfmsHsaYbZ0cT-_a2U1I--ttnVDdRwAs2IvqBumfLPnmXuGEZkS7l1qNTRzM4vjoU9M7xBHcys_73Am27ctnaP8nxNVbq0Vs7YgMe-WVBbr-Tck7NHzJwt8DmPQbj2i6uz1rOMIlc4AmN6PN4DjTyCjwGfQmKHAxOh2vk64wT6lvA8j9_ZOGkvRNKwv8DP5-9isFm4Kn7O4ItqNI2L7jPfBVZP5G6Ep_olL0G1lRFnw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پروفسور عراقچی می‌گه جواب می‌دیم و تنها راه در امان موندن سربازای آمریکایی اینه که از خاورمیانه فرار کنن:
با وجود شکست‌های آمریکا در میدان نبرد، آمریکا تصمیم گرفت عزم ما را آزمایش کند.
نیروهای مسلح قدرتمند ما هیچ حمله یا تهدیدی را بی‌پاسخ نخواهند گذاشت.
اگر می‌خواهید در امان باشید، منطقه ما را ترک کنید.
تاریخ خلیج فارس فصل‌های زیادی درباره سرنوشت‌های تلخ متجاوزان خارجی دارد.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77401" target="_blank">📅 02:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77400">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">رئیس مجلس نمایندگان آمریکا درباره ایران:
یک حمله دفاعی انجام شده است — این حمله متناسب و محدود است.
این حملات هدفمند به سایت‌های رادار، موشک و فرماندهی و کنترل بود — ماهیت آن دفاعی است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/funhiphop/77400" target="_blank">📅 02:03 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77399">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اسرائیل هیوم:
ارزیابی مقامات اسرائیلی این است که حملات آمریکا آنقدر حجم زیادی نداشته که سپاه برای تلافی به اسرائیل حمله کند.
احتمالا حملات تلافی جویانه ایران محدود به کشورهای عربی خواهد بود.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77399" target="_blank">📅 02:00 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77398">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">یک مقام ارشد کاخ سفید به پولیتیکو:
ترامپ همچنان معتقد است توافق صلح با ایران نزدیک است، حتی در حالی که ایالات متحده امشب حملات تلافی‌جویانه‌ای علیه ایران انجام داد.
این مقام گفت: «هیچ چیز وضعیت کنونی توافق را تغییر نمی‌دهد.»
این مقام تأکید کرد که توافق با تهران «هنوز نزدیک است.»
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77398" target="_blank">📅 01:52 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77396">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ای مو موردوم سپاه هم داره کردا رو میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/77396" target="_blank">📅 01:47 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77395">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">روسیه 6 تا اسکندر زد اوکراین
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77395" target="_blank">📅 01:46 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">عربستان ----» یمن
پاکستان -----» افغانستان
ترکیه ------» کردستان عراق
آمریکا -----» ایران
اسرائیل -----» لبنان
یک شب عادی در خاورمیانه
@FunHipHop
| Menot</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/77394" target="_blank">📅 01:44 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77391">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">هیچگونه انفجار یا حمله‌ی جدیدی در بحرین یا هرمزگان یا لبنان گزارش نشده است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77391" target="_blank">📅 01:35 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77390">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">CNN:
یک مقام آمریکایی گفت که حملات اخیر به عنوان یک هشدار به ایران در نظر گرفته شده‌اند و انتظار نمی‌رود که تلاش‌ها برای مذاکره به منظور پایان دادن به درگیری را مختل کنند.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/77390" target="_blank">📅 01:33 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77389">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">انفجار هرمزگان
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77389" target="_blank">📅 01:32 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77388">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">صدای انفجار در بحرین
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77388" target="_blank">📅 01:31 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77387">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مقام آمریکایی به فاکس:
حملات هوایی علیه ایران «در حال انجام است» و اهداف شامل سامانه‌های پدافند هوایی و تأسیسات راداریه.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77387" target="_blank">📅 01:30 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77386">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/77386" target="_blank">📅 01:28 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77385">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">این تو بمیری دقیقا از همون تو بمیریاس
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77385" target="_blank">📅 01:27 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77384">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">سپاه: بزودی تاسیسات نظامی بیکینی باتم را مورد حمله قرار خواهیم داد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77384" target="_blank">📅 01:25 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77383">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">پاکستان هم افغانستانو زد
🤣
🤣
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77383" target="_blank">📅 01:24 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77382">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">جنگنده ها از فرودگاه مهراباد برخواستند
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77382" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77381">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سد مجید :
و ما النصر الا من عند الله العزیز الحکیم
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/77381" target="_blank">📅 01:23 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77380">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lFoXWldZEH6gsLbmBfyiMcNTIG21HIE2f3F-GNYUKXafDu3gIVPrW2Mh2Tb8yPq2QxamF8WKnxyxPFa88sAz0-BPqu3nV6uZvMCQs2Ya0PzvVW_FsWdh9tw93lkibNVHMvnWd9Kd2VM5kHfQ8Mtdc0ObkF-p5iZZaGA3ORByGPV8EUiqnrUjOiZPG1stCLzvJ8FaIcinhgpqZRE7tznQOFfsxV2M6U3L1JCw_-p0ARatVPJuonct7ZA_VM5fs_RNQ6VWkl1CCnHgMTBbM-NZ-anVIUJNaoGk3CidM0qB1vbW2oiRPAxjCYK9QpuO1_J-Eo_BStmz3sjLD3vb77E4LA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران سوریه و لبنان
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77380" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77379">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تو این هیروویری اسرائیل بیروت رو زد که ایران به جفتشون پاسخ بده تا شاید آتش بس نقض شه
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 9.29K · <a href="https://t.me/funhiphop/77379" target="_blank">📅 01:21 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77378">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">قطر و کویت حریم هوایی خودشون رو بستن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/funhiphop/77378" target="_blank">📅 01:20 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77377">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">لبنان رو هم زدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/77377" target="_blank">📅 01:19 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77376">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">هگست الان زیر بغلش تموم شده داره بارفیکس خلبانی میزنه
@FunHipHop
| Constantine</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77376" target="_blank">📅 01:18 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77374">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">حوثی ها: مالک گپ مگام
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/77374" target="_blank">📅 01:16 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77373">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">تسنیم:
ایران همچنان که ساعاتی پیش نیز هشدار داده، پاسخ قطعی به تجاوز آمریکا که به بهانه سقوط هلیکوپتر آپاچی انجام می‌شود، خواهد داد.
@FuunHipHop
| Nima﻿</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/funhiphop/77373" target="_blank">📅 01:15 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77372">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">صدا و سیما:
پاسخ های ما تا دقایقی دیگر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/77372" target="_blank">📅 01:06 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77371">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">فوری از علیرضا تنگسیری، فرمانده نیروی دریایی سپاه:
سریعا به تجاوز آمریکا پاسخ خواهیم داد!!
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/77371" target="_blank">📅 01:04 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77370">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ترامپ به آ‌ب‌ث نیوز:
فکر می‌کنم پاسخ دادن بسیار مهم است. آن‌ها یک هلیکوپتر را سرنگون کردند و ما همین الان در حال پاسخ دادن هستیم.
این پاسخ به کاری است که آن‌ها دیشب با هلیکوپتر ما انجام دادند، و من معتقدم پاسخ باید بسیار قوی و قدرتمند باشد، و این همان چیزی است که این پاسخ نمایانگر آن است.
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77370" target="_blank">📅 01:02 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77369">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجار تو میناب گزارش شده
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/77369" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-77368">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">هم اکنون جلسه اضطراری شورای دفاع به ریاست علی شمخانی در حال برگزاری است
@FuunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/77368" target="_blank">📅 01:01 · 20 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
