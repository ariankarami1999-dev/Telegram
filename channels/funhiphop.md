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
<img src="https://cdn4.telesco.pe/file/CVfHauWoQhGIG59yfF_Ewkg5rOjCIVrgysl8a15iRQbT3HJFMQ_sBVuIq-RqTXeeVw9pDEEUn2IkvuWpZK6ROyOnuNb0tYIYQeuLz4WMdS8JZ7_8w-bHaoPm1keTnIzEVu2FRz9v2IvO2Jm2IB6PrRxGqlkmj-x-6c7ecF-MM6s1de6zcKbxWTjsyQ0GJahyzHTXmEwX7eaPlMhiGEM6ru8Z_u-2WuzRWLQcaAeJYF9OsHepOulaDxQmcc_upITG9smf3njahKyJU3XCdWiThXL5XVXQ12oIg1q7Yp1RTCzXCp9CS5MJi5u3oddEhpzw3_KuGXRwByjNhGI21EHvEw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 186K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 11:31:22</div>
<hr>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 3.51K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0E4vxo5VKDFpdxY5psI-t2FA_WdT_Uxd93uHeaEOFIJfpx6_q_YE1JjahHsU2sJnTc1MhYkvzZ230VrISdL_d5zdENfxzHLEXMXthYZc_ItjUY9Iy4nahXakN_r9-n0me5MD2jn2-RSpFZj9nZSYmC4si5ygk3TEUqFA1DuYtk_tbtzVQS8BoGOdNfiWDUNPFkhWlV1ObjDnttcwQpAFW37EObo7z7T3SJ1NF7DjJwrUuvNcUPmshaHL1p7CH30gd1dh4GCDMPjz_B1XIf3xFiabAEekrd29lgIROJTaatnbYnU1_IlKFjWLC2SrwKlPVRcGku0---eHraF-gb4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 5.17K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 5.39K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIm1-MXeQb72AiJ32hqgL3GhCPYIuLvwFyRGqdVZQ72_OkyknqpfS4VizHvWTUlxiAci6MbM7uIgAYaA22JvSJpPTUBGYGm0tzOKp40yzhOfh0dsCERELz9p5oVzVY4Xwo8Tz48UXxHUyHJkNSAz__v1f4LX2Rl4GZ9uIC4jmuSGUbf-7Wesf9-knkOWQV0bVowJi96EB8tdgoSJ_GfG2q5b9cT-pxOc2LijIbUQSHHcb772qJXCXw6eA5G0EUbCswq8EqO_TwHCWClw3QNnXVQC5BjB26AR60_Nv5JmMjdhD2ugyzWyn3qDXqZjE5hK_9NUB5FOG6bvyquTgAHlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78971" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 5.28K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jaSCDQngI2iQpzfEJe8KeuJZ18BeDzQCfOTun1B191eG-MMlmJBBQr2KmcGpod7LjBfkEC74rC7159OJVSbCI52GTN3beLFzn1fgBTxIUB7anXh5Qd_nBIIggTGTc3GMHeq_X7GP-z9HcTf5M59D_CmsCtHaaKYHQR1529qgTiSXGrcI6RgE4OrF9WnM4qUb7ORAJ0uCKSZlduX8iXExSLIjdSPUMjw045O2mVVS_ztx_rNpMuqEOh5Y8hOmW_781iDTLweqJw3EMV-c_QCGIY6CSLmooF67Vm_nlmPXi8FGdos-Ao0KioJQYqtTG4TDibSJ3ikEAIE2aqkkTBpwhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
R7
🅰
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 7.15K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNUxuxFEtydx6GFqCFFsBj2-fmntYZxJlu2usJX45MJN3cl1QVaXzaJGq2rWVYF8zQWKxU90iw0HWK8B7rbw6N2YF7vVtmxF8wCET1C6RjzVpULPJ3Avc4ARWb6UAZr09ceThM6MRn78kQGN-VCe3ab07D6_UQPCoW1LnfsM0NEu_aGvSAAt9HT-ja41HLN-d4_n4T4ZyNiavQrriqTOxQLPd9FKicuzwoFVBnBj98c8n1mCllzWKv_ClfAU74GN7Dj6kvge0UxXkibEjXTX1onnlNFFiZkY7Nzk9R2D1kXN260mreE2Vn2hR3x4TGXek-j3Gnou-WA1lz3fi-7SxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpiImuadXDh55NpofBORYeQrtqx4neNeI9F97SAW4cO44Kwzyi2Ut4wA8WpaHnolrrW_GUL33DYKTEN_GofFYRjUHpH6Z9cVLYkKjJoOGPCnKoF72S0fT-VffXiAe5BmE79iAWq_xkgZ6RR16eCI97j84geeOJs9xjjZMfM16-OtmrlWYSZBwDevFs0N4KngRITsDHTrco_V_e7Y8srx9xqMPP4AlHStxdEFpMxK2XG-qJDYBntnotkucv-gMNIPZrKa0PAjt6QYAxGRCEZ4ys4bIiYDhYn6jahEnGCivY9DGqoLpwIUDkdJY2r9Uw7E1fln9lERR_-Na2qLUG8r9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 7.8K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCQM0o5J2-F4BFbZelcpCinXeQWiAho41Mw9Rug_ZZnS1yKjX7WDMEy1D9bcjlq446YeXa_b34qLpdR5YLnZWEZOG8BMuBr_RGikbi8NvrOpfh6fpGtLVNh1NfAS3c55GdaI4NbpVBkhFRdlMoHMgQOCJmxsrM_eqrwTs69twK_zretjsmC5q3gir-jC9oIot2HZzym9F9Iu73sQ_AFhTIoCMVIv_k0RqyI5-ZOPUviBxNOWnbHDt_FIWV12T6nAwSeOZ870-F1gNu-Zx1itQ9cdYyzeOBSttSMGhvt13PA_cgd3kVnj1PAPdLGyZTIimUNFrYGZf2nDyQvTZayL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 8.24K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 9.05K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5aDLT9pXpA8zy148zTpqWXoK6ZVFD2g4Hg3qx8kLkXKUOJIUf95LVKNJNzns4NA7AkEfQaEMqnCQJ7xfBFQ53WE0FczefNUaBNr5hWRQZhKoHVu9T8gVUXMIuE8huDAnK6SGQrxwK_rhrMCGNePn8QreCALi6SHyHWs_nFdmgSeaBj9IhJmKRYusKuFraJ0n5dqbnT0VSelJ8zcKgLA9Jwr9z0f4HSds_Fw9Z_op7QuW4u9dT0ImehiUX7xrsmZa83m6frkvuN3VXU5HEyHxVYqfaedwSo3JDDmZ9SrnwVYRvg2KxUR5LV7N7AWvPAQ1nHTwxSfBpt8gjokgDTJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 9.7K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 8.92K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 9.25K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 9.28K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 8.71K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 8.75K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 8.99K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 8.84K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 8.22K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6d_Wu91TtlFprSeuhfkEiy8o6lM2jIXQZp49TTYXA6ZT4s1Il6CpqZHcCANbiZ1x-2LeBP9pQF5gYKKrntxYwY2bjYI8lU-Uk9MCWmzMjQ6quAT55x5Q9bZ2XfKgwVGG9Z3t9eEC47kLuhwVDPw_UrgM1ffbFelw7qZcLXegtR63VYjzy-2piQ2BjIPvmG9EjCanpRX57wP42sxi4klvPWv6KsTNUqSuO_RknPRtNddpwtpA7cagrpVfhHYMy0P9tdPubgJHmvUTF6kPh4KfV4iQ1rOo1T7BU8ryTioeWHa2NhTXZ_iwl7kJosp1kqVHHMK-nQZRgYbw1HWAo6oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 9.67K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LC4IjHjQ3KjgEuCU6H7M5W2LLORZvvWOonHd0f6_u2FmDg7fSvi0BE7dS_QceY0t_p20ZTSdxdOz0q--XZEyTF0BMHkFMHvYCKEU3pESzI-4MjA1DFqbXKKbc1qZ7SfWnnEcpDzEexizRp6dYuiYBM5FGVl-BuAM7YhADouiMZJHre84530jEEJ7jLizqAfmlESDmlwQyKEEeew_KiZEkme7DwAKKHvIVAsa1lz7vMfqq6usHcs1RVf6l6ie9HTjWM9EW3p3Jj5FFP-9qVCo_2p8aS6Itb9Y7nvNA5rob3Jklcnw0ZpsZZom3yO5EXeWB5FHDaJ4c5yiyAZ8_vU7RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c43122e124.mp4?token=HwLhVa2ECPCUQJfUqKtBkLdvBA5TQ2d8jWP2YjXdFtWkG0fuk5GCdXZYFdgviIE2ZU8hBuT5QHP7TfVlLKktHDeUxK5N8edtGiqEorkFFgpWFIqzv51TrLPtv-xFsLkhBFgbWJfFbR7hnN0gFh2w6ouu-QnWTj8i5B6J-sygxZ076VsAbLVLvWiUufvcHeinj70tIO4an-j3HSPnLvL5MjDiCMqtQx5wQWxow5Jhl1jhjjkm53QwT9YOHfztWzMmlpFb4P6zzQebXznumKUbD76DWTQUNFwZcR18eNzUWEQFv16mNHMa7zeAjJ6trhprb_sAzQ4o7EDIa_7B9qgLsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اینم مصاحبه شجاع خلیلزاده قبل جام جهانی:
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ac246bd5b.mp4?token=h1wrcdxCpzGITv7K_dRacvfhEBCH_iyYzZCBEvmF-p7ywyQrCozOUYE6mfLkwCHTUGqUE3p6uYkWjtKD0IpxYdM-PPewuH2RbxmBpkdP45b1bEnPLXYkwFrGiRtMYXvoADH1IeXrUhD7o8pMaLiE5B1mamhoAVTSkW21SNdq-RlXHuvdR6W2iYbuyAqpu2mFMHINkRkSfHDHCf92Mzpw0HU8GIHaXeZc6hNHXADKHN_YWTiV_u6v5ozGlmifKMRRcUBtBZX5HgNegg7Ji-T09WdL2NAwurD5_vAT4HGooi1zK95A0u_RY2LyO1_UkTmwpFsn3bfYquaBejYmzBd7KQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">نظر رامین رضاییان در مورد هو شدن سرود ملی جمهوری اسلامی
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4dTesjd9u_6XkTvF2NWwSh57ZbbArBftLSVv3HcYykjGHP_j9QcBxpdp2jfdgnAEPIG46lDn55-Svsoi0JpAVrDOJ3umPZFs1CjGfMJ3vFA76_HjKG9icq_Gil5GMjfy8bo17lblzvhjmxb036635FSJFzbv92NbUv2VEPRe-okONuYthqQF-ElQ5JjZ5bFG_itPq4qRIRZ8MZWavN5_3rFvl-mVPrzQ-yw4bADLc5YUYsI-Eb4npnF0Nk25hsO1dKT9Xk1Tf4A1OYySBVz9r6TENwq2WBmHDk7V_UJx0KRWgVLkHJZjeBREiFf-H2Wf1RaeaTQSg0jAAoM7lVcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A22slGqUfUI2VZ_L6-U-GfkBjmaz2pKYtPXQCVQVK220n35wNgn55YbBOlgT_o36xPb-VhIRjPpTLTP5y0C41labmBQEiKbAeEHWcwH2Pm29BmaQSlgML7RGcAyrgrEh4iaghhmgjeWddaHIAXgXmn-u7XSU0W7zRgDrG3ZR_mGnAYy9MrGts7efw2XHDdtLTyk4EMyTriHW12G62iAvvOP9YcBENo23faBg-unMVg-HUlwh7lDPFjHEPixrL1V4TEOR9Vv9cF-trsWPG5xc1aM1fzwAsxtsi_W1yJpYpeJWFrhwWjJTo21L7F7SP7D8ypaGxkgI-HAfwKtDwkujTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oc_RYka8ZS9S7KV1FsIeTHsEAObsUXLQ0rrTcySIg7bXNJdn9Y65PadzNcg-1bXkfYQn7_TBNGc0Gsl3OQy22r79ttk92An2PCzZzYRJRiwVrTDUjxCBLlSgfgEtjBWLiAcHDGugNPTajSqA4QN97JiKEMeZP_m7p7dNi9KnuPQl_Y8cd0vmKCXxF8rRd0ldk9QIHkAcwdwzgMcSv_HbcDp_M12Ub477HYBLbTJDng5ZGh5Kj-IIzcfTh4prQiHJtGlEwvBPS_FsIaZWovgDEHQErGAzJtCmH5aVbt8YFqaQ_B_ZdbYl0fAFhJ8UFQEjTXQajZVoclA65u7qD_5jmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JNPhZZu2XygZr_1wJcJ4FiAggCS2BvE1iuQmsRJ5N7q7I29fp6w6BJ7iJo-MAwLAkVBcH62LgUBM-HIU26FPLPEi8r1SIep0fJiD6VXvC7enYIvSSO7SQD-5taBnHzD5FNRraqrRAyju_A118ibsrvZQF_Nvr8xqM7JisxJlZOltplUynV01AoVjPl-VWCciaioxjsK8SpSIvdWGvz82ILSrwOhRxdWA713ej_gca4LWb3w4RTY597JcbxEFHwZ4_OJ2ryTNHga1wiCi31oL7MtPqMxGzWAXwubrhXRNtt_z5NbIfcoL2Z7EAfCD3h3DFyc99PIM_ITPeJ9voUFfeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">RitzoBet.apk</div>
  <div class="tg-doc-extra">53 MB</div>
</div>
<a href="https://t.me/funhiphop/78911" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">📲
اپلیکیشن اندروید سایت ریتزوبت
🔥
🚀
وقتی شرط ‌هاتون رو توی ریتزوبت ثبت کنین ، علاوه بر ضرایب بالا ، هفتگی با کد های هدیه کسب درآمد میکنید
🤑
#شرطبندی
♦️
آموزش شارژ حساب با کریپتو
♦️
آموزش شارژ حساب  ریالی در ریتزوبت</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b96vJHkyQ0rUSd2LDIuKFZLqPLYjKdW5HcVsP2QWR79NX7QboNvtDGcmdiFE2LYAn5VUFh0OUveL1k0yXgLlxgMYjbCtNWP5okv1AZ8qqmlo3XcRchWZLDgA9pSK3I_9G-8QIIDJU61gNMhHdGl-z448Sggw3HGtqePqiw1sZ2hJjS56LwCkRtG3m6xTBik0A1Xg7hBAOrW-9qfoCHv7CrcnNmnfG-moOQ5KJWU7pYKAACDa0mmqhkkuh4MBl4y1s8bkh0acaEklMbvZT4NNGSAvTBJSicLuJhpu-al712W81UxguVCw-CLjLUtoasrVDVc7ZF2LZS1CCBcGIBxo6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
شبی پرهیجان از جام جهانی ۲۰۲۶ در ریتزوبت
🔥
⚽️
کرواسی
🇭🇷
- غنا
🇬🇭
⚽️
انگلیس
🏴󠁧󠁢󠁥󠁮󠁧󠁿
- پاناما
🇵🇦
⚽️
پرتغال
🇵🇹
- کلمبیا
🇨🇴
⚽️
آرژانتین
🇦🇷
- اردن
🇯🇴
🌍
امشب ستاره‌های فوتبال جهان برای صعود به میدان می‌روند؛ شما هم شانس خودتان را با بهترین ضرایب امتحان کنید.
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
G6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aFhJdK1YXo5q-bMIgjCSDII7RtGC0SB7xA1RNWPidIHyQOVQwUiAePD1SaZ1dk4kh8TQki0srqg9X5s4WHwfTEFSrgbZ7PQNNnQ4EDKHPmPA-_iceaKyJumewNjgylOrN2HnZU5Hv3Z38R0pYCp1xra3P-ALF27IRFCbWbVBWSdRiMGRxauNagpFLmHsTsoKg4-MBmtxQXzrA75FHdfLNoj8tfOw0gItzCXxHvKc5LToMtEB0ErNdZet7AqyVxN_dOgBPZ79qoaI0aCoBI_gAfVg5D-j4JvGH4c9KyJe0W4Z41fmcjmkY3wHemyHQ-z0hZWklrUyIJQzf82dDJZVCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید
حسام تی‌ام
و
حسین تی‌ام
به اسم "
West Side
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKAr4Q1e4Uvd5SYU9n10upotucqYdXyzbfMVGR4GN29Z0g-yfPnnrnkN4XdKs_7xE4iBG_BpyjI8K2csRul06OGg67y7oJtACD-oH9JVGqmYvmf98swjYCPPi4S3ysLRUAWRHgteAGeavGvhUsSnSxkeOl4MvoHARkCcIyqVbtOAHvNwVGPhE61mMRZ4-DJ8jRm6oEqGDWbiXPkjpCXpFdcbDWgS2Vhhx_-GcL27kAyxa9xeR7c_Gfc5dWfPtL8sB-y8bbuqAJnRpAXpmU3uutN4N_V53l-Wy3aL12h6n518k9fTpwP4wLZAdHDFUApbefQ4Mc26y44dIhgE59WjEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید
مهیاد
و
دینا
به اسم "
ATISHSOOZI
" منتشر شد.
SoundCloud
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🏳
سرور مولتی لوکیشن موجود شد
💎
🟣
لیست قیمت سرور ها
⬇️
🟡
سرور 10g - کاربر و زمان نامحدود - 60000 تومان
🟡
سرور 20g - کاربر و زمان نامحدود - 120000 تومان
🟡
سرور 30g - کاربر و زمان نامحدود - 180000 تومان
🟡
سرور 50g - کاربر و زمان نامحدود - 300000 تومان
🟡
سرور 80g…</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tjXPNkaKS7_wUpBLoccd8SdsqETmyIZ9wIKe7dmG_X4jpd7xslCFK0HGnC2nDX5tVMe_GU6jcJ5coAozOdZMYnopoGQKWqjb4RGkzL6CA470Ezd-HBx-ZFaMSRR-PTeWc_sK30bejhtG7cH0vzrlJTiyhQBmlPEah5H1I7-1NbwTDddNXvmsWh6fGrnwodUxIS5MSNnKquXnHaaLb3p3fmXol4pwNI9tEFX5Gxj3E39BVYd5BT7xDRBecDadrTKyGTXr14YdBl3nvqLOwxQ7rRN42kJdAWR3Cp9V3HrH6vT2gya2O9Jk9uthhuKhPkJNPD3t2ow8vuapGEVSVc1W-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bkfh0vQKZjpUccgfmZOBeqMgFYRL5cCgkv6zviRVIUTbPIUzvupSP0lZTHytV-xCSHqMu3hdL6wIeBquOjK84cxjtH_BybB4Jeccrn7VEl4muuKtMUze0rP5jMhI8s6uL1OTYxcYIGat0-rogIDP1rtWoW7omy4v6lAOXU_2wWgHWcmB3vH39kAIWPBk02eVhFrQHra60UR582HnTIDtOyLFDlcFIaWPGE0FxFR9ihFpv_YFWR_I4e_qD7p0hVnEAAbA3QiAXOBfR9U7opG15XphNgnGQFwhqQBRZYR2ZjZv-7wwjYw4nPOpWqYqu4Fy2xSnZ6qpEzwyh9N1SPfY4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=DdiWIjx5rqjJuZpBM6ongNN0lvhuLB4I0tbhgs_5xcT_w_vW2Ycezwj0DHiKkhuc4OfuB7M3jwBSPPb6yN9LDy-JClHJHsEfALYzIpaMv1nmDPXnw_gHtIw5WsLw7oMfTH_FI-fPW-k_Oj-dGlLDV6X0dbyf68QiHxJ5p6R1GdyS1sWjgPe35nlmnifLYGj8C8REJ_eydTLYmhaIl5k0Ay5Bsb6RIE-NSBANFyBRflFCHLL2CF-BWWCnUYvSKE0ipFGi8aQsD-Y5PuBT-iWMJk60n08yHZsWrDfo72F8RC9i4RwkYpunRCUl1otyEbvbrGM03FiFKZ8NCjawqnPNKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=DdiWIjx5rqjJuZpBM6ongNN0lvhuLB4I0tbhgs_5xcT_w_vW2Ycezwj0DHiKkhuc4OfuB7M3jwBSPPb6yN9LDy-JClHJHsEfALYzIpaMv1nmDPXnw_gHtIw5WsLw7oMfTH_FI-fPW-k_Oj-dGlLDV6X0dbyf68QiHxJ5p6R1GdyS1sWjgPe35nlmnifLYGj8C8REJ_eydTLYmhaIl5k0Ay5Bsb6RIE-NSBANFyBRflFCHLL2CF-BWWCnUYvSKE0ipFGi8aQsD-Y5PuBT-iWMJk60n08yHZsWrDfo72F8RC9i4RwkYpunRCUl1otyEbvbrGM03FiFKZ8NCjawqnPNKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pqxhjm42ukzGNOhss0rWDmRZLHMwbI2VWwGkKU9JDELRqpq5ScWZMfjpmDwbbXpoIOyAUKQUM5SAMjvLZt9z9EOvCwGfzgEXsWFH8hhzTwZco26B9ledjmzBLQp2fDqS80OmycoSm4FHiQFuKiHElPUxUbK-j9EgWmGeeTizdYuU6uRxpTz226oJgYnsxu6yTIWlOKFa9AkcEUK9odQUttrKBXvbVqSAmQlpHyq2GFUXP0uQtIKM0zEUqSerxS6c5zxxeVBxg_uo0wmjZiYYUEh3WyARrYKvGO_RTBuU6k7lRjCvtUxMN3E-3CxC9ibIySEXyENJ35sV99at-p1-7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXoM9IqSlc-5GVgF_Wd0Xa67jO9awrfa4LbwdRtn7BQVm5jFUpPuATY_aXazmGAsP9QHMs5rYAMzmHiz1xY8TlgqAtkcTjkH7diLH1DMVs21jLEzx7ApR4eentdEOqoL03O3Vk1vmMuqwGb4LM7bDAmXWMh_hXYtJBCCZJf1VA2S-JW-DDOi6herkU1jLITfawBm8ND2EWqtZKRX2tcfqRGcf8ysHUmWIjWNo6SfgVMfKr7YXADD6VmLTLtj82S8HCom4_zzc5uuA9EVMCx10ejPGYwz5EzpEG7_GW7B2Oba4D0GtRRMAr-h1lWWel8AnWvIMo0Q0kCOhYE0h9-2bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UrjNhmkoeSVcIyIlnfECHg3lEAGq3kIWt41pSZXMlYMYvE1vuki9tRxH8SQCVnrcBcw84kF3Q-M_SEXhDZYMm_1jrd-mROSitiYe7lOSbeuxIxVUCP3qqHlbQuZoQsCwnHCavtADBYeul6XCrC0PfWh4NVGh-cir0aeW5Mx3pXFZxLCZm2K5SvCmLe9cU_k3mWvhmloO7MNmNQCNUufdQ-jLyf8dZc6wyZ7PGNXObcIMGjgLHC4ZkNF1BkeMzBYjWBaJWYQP7ixj1DQRvy7Sg0nVnEKyZeJUdnLQmEuH-YvDDtMbt6rTFcLC0iEVzrHcAYUF0Oi4IrVBPuM1N0tK6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
می‌دونستین توی
ریتزوبت
هرکی شرط‌بندی کنه، هر هفته بین
500.000 تومن تا 100.000.000 تومان
پروموکد می‌گیره
‼️
💰
باحالیش اینجاست که فرقی نداره شرطت ببره یا ببازه، تو هر صورت پروموکد بهت میدن
🔥
🎯
دانلود اپلیکیشن بدون فیلتر اندروید
🎯
لینک ورود به ریتزوبت
💎
امکان شارژ حساب با کریپتو ، انواع ووچر و کارت بانکی.
✅
🌍
ریتزوبت؛ همراه شب‌های فراموش‌نشدنی جام جهانی 2026
R6
🅰
🆔
@RitzoBet_ir</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78893" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJDAQMYF_xeb5fL-hQid3kPzGlycoHQmr54TSxuRXQPog4JdM1u87gLslnjBvQ0nUmwPeFyhm5Vyy6dya3NAUNyxQb4e69N4T7K3t5J22ySJSFR9Sbc1nNxtLNi8U0TrYrYxavHGjCZTE4sPrWGNKDqcUh000t13DzyhaVKO_x26IlCR0UwvMK2Uq0TDEY0Hv-asNq2IWoqu2zMhseAGQGIqD6r7jvAssi1evDtYMQrEmTf-5ff7ohPNvwvZxdA_J2wv-q0YrVBYM2RnIZ6tAeHL2YVNx1j-KZoHB8gDMl9xox8pM2KIbSfsKG2xZO917IW5oOjd6sNETmZTPSU61A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اوووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78887" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=rG4PXrjKLIOFQ9JyhJt-VQY9uYu-KyDNtcrXHJwm_tQtyFpayuYnYs5qjrJlqI9tyevoR_GnlZZeI1HiEKt0LcrHW9NDzKRgQVThfkDKwChiSQjQ81HhSIDbBaMUO2vtKW9Us5kZ7sm1ojBj7StyU0ZRe2df5vvq1_sqbsYl65aGXMSqnDm_DgoDnne0RbwfW5kyLGfP_bdzOW-cfARmg9mbenO7ka3PCp09TIw0gBLeihJQwOSfIk1VrR663Hp4__sFfMfBHku8S-EIUJdMHRqYWud4yhsiZIgiBcfmEZxo4Y9pHY5aMj9S-qgXtLfNsCK2lr1VWmgU6oTwZ5O20A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=rG4PXrjKLIOFQ9JyhJt-VQY9uYu-KyDNtcrXHJwm_tQtyFpayuYnYs5qjrJlqI9tyevoR_GnlZZeI1HiEKt0LcrHW9NDzKRgQVThfkDKwChiSQjQ81HhSIDbBaMUO2vtKW9Us5kZ7sm1ojBj7StyU0ZRe2df5vvq1_sqbsYl65aGXMSqnDm_DgoDnne0RbwfW5kyLGfP_bdzOW-cfARmg9mbenO7ka3PCp09TIw0gBLeihJQwOSfIk1VrR663Hp4__sFfMfBHku8S-EIUJdMHRqYWud4yhsiZIgiBcfmEZxo4Y9pHY5aMj9S-qgXtLfNsCK2lr1VWmgU6oTwZ5O20A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتون باشه این ما نبودیم که فوتبال رو سیاسی کردیم
و خطاب به وطن پرست های فوتبالی بگم که کاش یکبار هم که شده حافظه بلند مدت خوبی داشته باشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/78883" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">چین به اینترنت 10G رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78882" target="_blank">📅 09:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">می‌ثاقی:
اگه بازی تو لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات درست و درمون var نداریم الان گلمون آفساید نبود و برده بودیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78881" target="_blank">📅 09:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UcKdu0Il_jVc3PYvwB5qZgPBGS6Zrp7e2tJQW2FObItjAD9UIGeg6QZ3xaE0s-BtZJ8grxD9_vICosoWfutafxJOZ1MpijqR94Tn8bYthv0ewb6nhSmYHlDf7CRrs000NNhHmHc5ni3w9wxeIo8rrYYTPO146OIkoq52BKvEyINvxZhf3tvO4TrqEqbNOh-6g0uqDfib1_UQo8d5Hl-8zwTasqkrwKcfFxINO9Fv-OTiM2EXVl1sZ8pVkJy8kt0QTHJaGcJ2765EZnL9Wwp1ohAB4OIm-vjEmchbHGw6DzGTD4_TkR4vXveabtX9IjsZ0rdM-yJOMaJT-bLo-Vd8jw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوست دارم بدونم این شیر ایرانی در چه حالیه الان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/78880" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78879" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GcZfqb--PRkXzcTGQ5hNGuYXc-TrIorWtCoRirMy6SISFfbyJB_Wyr1c1Czfx41B9RDaZ1ALWH6cOV5SkDN6fwNSbDwkIh54U1s03RVyX47Y6Xt1DFNCdSCpzDI4mTl8SGIQYbT4DQoM4Epb3qW1LNbgEmKUXCNuQz0emK2gDPaCdNqXGS53vg6L6uC2kHyMiUX52aUBbSuMDW4olG2fmteL7CjLXguFhEm1BYo-teEyejXSwwV7ynvzhDlNI3jrDcTEMRxKe8zb3Nmc_LKvedgXum3IfdP-Tp82R4qwf_sU3rVYqN335gZg4n42iIiFKcumkpsAzW9OoJWtakWfkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی عکسه رو سریع بگیر تا نفهمیدن کیری فازشو دارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78878" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">رو دیوارای تهران نوشته خدایا همه مارو ببخش بجز طارمی، مردی که ایستاده رید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78877" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=cEo7WUYcDnjM6yeGPWrTewJG5P1Oz5QZWVAEp9yPk0WVWU89v7wDUhKmgR_hcm5QqFwV3ZKGnrrp1GlZ6ebJ0beE6_zCfLM3LsXD0oGFgGjV4c8UtlKxgHwVY2ImzMnIdqczXo0C-WrpUV2uRfoQgYnsEeY-2P0H60hCg_h3P9UqdtClarqoqBnsdMe31Bgvwc-qWHb1mbGasFp5nez49b4YQh2mB-F2-7Y3jBclGnXY7jT0ghftJNXMhHklAwAxIYrZgp8VfiZ8ARI-3SHWVFiaIEbcXADIZbVWQSZXRXA7KGjL7U6YCWEEsOW-Cb70bqezj-_DZaRWyo5i_s2k9w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=cEo7WUYcDnjM6yeGPWrTewJG5P1Oz5QZWVAEp9yPk0WVWU89v7wDUhKmgR_hcm5QqFwV3ZKGnrrp1GlZ6ebJ0beE6_zCfLM3LsXD0oGFgGjV4c8UtlKxgHwVY2ImzMnIdqczXo0C-WrpUV2uRfoQgYnsEeY-2P0H60hCg_h3P9UqdtClarqoqBnsdMe31Bgvwc-qWHb1mbGasFp5nez49b4YQh2mB-F2-7Y3jBclGnXY7jT0ghftJNXMhHklAwAxIYrZgp8VfiZ8ARI-3SHWVFiaIEbcXADIZbVWQSZXRXA7KGjL7U6YCWEEsOW-Cb70bqezj-_DZaRWyo5i_s2k9w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت سرمربی مصر تو کنفرانس خبری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78876" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">ولی امروز دیگه بهم ثابت شد هر پیشبینی کنم برعکس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/78875" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMz_vFH5EPoN3H1kq-bDmyvCIOpsiGwChovuc7TkinMa1wuBmV7WKx8yFFySCI8XT_Wpu67q6i6YDBWWAHdr2waA6D2AaGe_7XPyOA-NSdrsy4kWkLwxlfa6e-a-8vxop4Bwyqn3CSpOpSU_VNtXAAaa2izc_6gOXNjlb_ZSI84i1IAtetEsJW2uduIu586ThfYdS4QcHFNUkQddjDJn8aN-YR9ECN7-LXHale7rFFUKkE6HEdXeZaNhX9yyYxAv82146SO1KGUtKnC1PKXQMJwf7KxOo41RzktY29IuWih3eh3eUYA3wUaYZ76AjCE0pfrn9AU2ddOFCJ5w7U8P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر عشق است
گریه نکن رامین جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/78874" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">احتمال زیاد تیم قلعه نویی صعود میکنه و به سوئیس میخوره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78873" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78872">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،
2: یا کنگو نتواند ازبکستان را ببرد،
3: یا بازی اتریش و الجزایر برنده داشته باشد
هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/78872" target="_blank">📅 08:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78871">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YY8q_pB2viI0Cr6zYelGnXuQrIdyJyiFt1hxsNB7VqQ4q0ra8IIXIWsyDAmZdNmBhh2boGtFHPPL-2qvO8o9BVoaRxiX9fxywRtgDGk0X5iND428_H78JintYVzsro-ytDTtl9xC5F-mN4Vd7qUIL1X1gsyN9kRYYa9iyg36_AlLdcLyKV0a5Zclq7B2Hf8dYMCitq4cKjouswcBWbde5RZHAs_n2AOn-7YyQPt_17s5XlyKh77i1hXiCH3MtDHJlrcl4_znanRv6CoGCS7WWk9jfWQcqCUGcWPPW-guNg-H224CdLeZ-6y-zpO2dnDfC1BH3TqjImSvftn-rPaDDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بزرگ ترین کیر شدن تاریخ فوتبال
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/78871" target="_blank">📅 08:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78869">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شانس آوردید، ژنرال فکر میکرد اول گروهیم، دقیقه نود بهش خبر دادن که برای صعود به برد نیاز داریم وگرنه هفت یک برده بود بازیو.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/78869" target="_blank">📅 08:34 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78868">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">رد شد
😂
😂
😂
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78868" target="_blank">📅 08:30 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78866">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">حرومزاده اعظم گل زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78866" target="_blank">📅 08:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78864">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">حسم میگه که مصر میزنه
بماند به یادگار
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78864" target="_blank">📅 08:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78862">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">البته یک صحنه کاملا عادی بود
هیچ جای نگرانی نیست
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78862" target="_blank">📅 08:24 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
