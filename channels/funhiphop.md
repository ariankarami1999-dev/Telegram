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
<p>@funhiphop • 👥 187K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-07 14:07:51</div>
<hr>

<div class="tg-post" id="msg-78982">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">جدی چرا چیزی از ارزش هامون کم نمیشه هیچوقت، مگه چقد گرونیم؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/funhiphop/78982" target="_blank">📅 13:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78981">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">قایدی زن جنده تو که قرار بود یه دقیقه هم بازی نکنی همون نمیرفتی نمیریدی به محبوبیتت دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/funhiphop/78981" target="_blank">📅 13:03 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78980">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">اوووووو رامین رضاییان اووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 8.15K · <a href="https://t.me/funhiphop/78980" target="_blank">📅 12:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78979">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N-LeQTdPjU6yfkkjc3cQispa-YzR1RciA6hBKakqnxML2lePocBlVNXeVqAwUvifS8IcyQ_okf9abf5ef5pP4NsGmT265bmzE-SNoYKUe39Meqmq0KfEt8Wkcju7FESzIuXnQkFLUB0Le5UakJ6RrlZ_RChW6d2mv15bLiqq_s8IXnIFRR5UryeRV37MYgwbwWl94OSXjTKCvdXjbgkNhPa-WT08gFiKiSO-iQovnFi0rx5be5EZJhriatvCQdu9fHzrhkO4rvUyfo2f5BQ3NAA9cU3nCXOGwyffOR-ELzoamLRTKmkYXXHPZJtrA0D9dny5vn4tXqs4x9_8tH6KKA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هالند: مسی هیچ‌وقت قرار نیست بذاره من کفش طلای جام جهانی رو لمس کنم
😭
😭
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78979" target="_blank">📅 11:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78978">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">سنگال با دو باخت صعود کرد، ایران بدون باخت سقوط</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/78978" target="_blank">📅 11:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78977">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">همه دارن خط حمله های آرژانتین و فرانسه رو مقایسه میکنن، ولی بنظر من کلید بازی دست انزو فرناندز و مک آلیستره</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78977" target="_blank">📅 11:44 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78976">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVwN_qJRjxzoCDFIDP8DSLtEPQ8WbpfxpRjD-xm09nrqOZ4CKUtf_Kduhsuu-bcQGyqU5Q0xwpTe-U6NoJLaklUyqghuNn_Eq-a6LYzNAGEk_lqeG5ZUVyzx49T8HKv2iJCdTsqAJ3aGlLHmous-7UkDhGCwvmiLeXu-yZGtRKfE893wp-bZZ9w9BBYmzL9BQvElxFXKzye28DVSAOBHC1NFQXam4VjuLnOZQSQQNkBMiWBWwX7R_jpAhlHmWkgzTCRQcP36-oWrxPCDZKyvg0gis1a2AcMTH3bGpu-jCDv85RsNHmakPjeHcmh4YvaZJ1iSIdPlg7r8BMCS70bIpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بخدا خود فیفا هم نمیتونس همچین مسیری تا نیمه نهایی برا یه تیم بچینه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78976" target="_blank">📅 11:33 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78975">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">هفته دیگه قلعه نویی میاد برنامه می‌ثاقی میگه فودباله دیگه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78975" target="_blank">📅 10:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78974">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D0E4vxo5VKDFpdxY5psI-t2FA_WdT_Uxd93uHeaEOFIJfpx6_q_YE1JjahHsU2sJnTc1MhYkvzZ230VrISdL_d5zdENfxzHLEXMXthYZc_ItjUY9Iy4nahXakN_r9-n0me5MD2jn2-RSpFZj9nZSYmC4si5ygk3TEUqFA1DuYtk_tbtzVQS8BoGOdNfiWDUNPFkhWlV1ObjDnttcwQpAFW37EObo7z7T3SJ1NF7DjJwrUuvNcUPmshaHL1p7CH30gd1dh4GCDMPjz_B1XIf3xFiabAEekrd29lgIROJTaatnbYnU1_IlKFjWLC2SrwKlPVRcGku0---eHraF-gb4ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب یک بار دیگه پروردگار و اسطوره بی همتای فوتبال جهان، حضرت لیونل آندرس مسی نشون داد کت تن کیه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/78974" target="_blank">📅 10:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78973">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/funhiphop/78973" target="_blank">📅 10:04 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78972">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SIm1-MXeQb72AiJ32hqgL3GhCPYIuLvwFyRGqdVZQ72_OkyknqpfS4VizHvWTUlxiAci6MbM7uIgAYaA22JvSJpPTUBGYGm0tzOKp40yzhOfh0dsCERELz9p5oVzVY4Xwo8Tz48UXxHUyHJkNSAz__v1f4LX2Rl4GZ9uIC4jmuSGUbf-7Wesf9-knkOWQV0bVowJi96EB8tdgoSJ_GfG2q5b9cT-pxOc2LijIbUQSHHcb772qJXCXw6eA5G0EUbCswq8EqO_TwHCWClw3QNnXVQC5BjB26AR60_Nv5JmMjdhD2ugyzWyn3qDXqZjE5hK_9NUB5FOG6bvyquTgAHlkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ایران توی جام‌جهانی : ۳ بازی انجام داد، با ۳ مساوی ۳ امتیاز گرفت، ۳ گل زد، ۳ گل خورد، ۳ گل آفساید زد، ۳ تیرک زد، رتبه ۳‌ گروه شد، بازی ها از شبکه ۳ پخش شد و برای صعود باید منتظر ۳ بازی آینده بود و در نهایت با تساوی ۳ بر ۳ الجزایر و اتریش حذف شد
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78972" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78971">
<div class="tg-post-header">📌 پیام #89</div>
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
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/funhiphop/78971" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78970">
<div class="tg-post-header">📌 پیام #88</div>
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
<div class="tg-footer">👁️ 9.43K · <a href="https://t.me/funhiphop/78970" target="_blank">📅 09:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78966">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">سلام بچه ها من تازه بیدار شدم، بازی ایران سوییس چه روزیه و ساعت چنده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 9.91K · <a href="https://t.me/funhiphop/78966" target="_blank">📅 09:19 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78965">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">با ریدمان پرتغال جلوی کلمبیا، پرتغال، کرواسی، اسپانیا، مراکش، فرانسه، آلمان، هلند و بلژیک همه رفتن یک سمت جدول حذفی</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/funhiphop/78965" target="_blank">📅 08:56 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78963">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jNUxuxFEtydx6GFqCFFsBj2-fmntYZxJlu2usJX45MJN3cl1QVaXzaJGq2rWVYF8zQWKxU90iw0HWK8B7rbw6N2YF7vVtmxF8wCET1C6RjzVpULPJ3Avc4ARWb6UAZr09ceThM6MRn78kQGN-VCe3ab07D6_UQPCoW1LnfsM0NEu_aGvSAAt9HT-ja41HLN-d4_n4T4ZyNiavQrriqTOxQLPd9FKicuzwoFVBnBj98c8n1mCllzWKv_ClfAU74GN7Dj6kvge0UxXkibEjXTX1onnlNFFiZkY7Nzk9R2D1kXN260mreE2Vn2hR3x4TGXek-j3Gnou-WA1lz3fi-7SxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cpiImuadXDh55NpofBORYeQrtqx4neNeI9F97SAW4cO44Kwzyi2Ut4wA8WpaHnolrrW_GUL33DYKTEN_GofFYRjUHpH6Z9cVLYkKjJoOGPCnKoF72S0fT-VffXiAe5BmE79iAWq_xkgZ6RR16eCI97j84geeOJs9xjjZMfM16-OtmrlWYSZBwDevFs0N4KngRITsDHTrco_V_e7Y8srx9xqMPP4AlHStxdEFpMxK2XG-qJDYBntnotkucv-gMNIPZrKa0PAjt6QYAxGRCEZ4ys4bIiYDhYn6jahEnGCivY9DGqoLpwIUDkdJY2r9Uw7E1fln9lERR_-Na2qLUG8r9Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">من برگشتم !</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78963" target="_blank">📅 08:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78962">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TCQM0o5J2-F4BFbZelcpCinXeQWiAho41Mw9Rug_ZZnS1yKjX7WDMEy1D9bcjlq446YeXa_b34qLpdR5YLnZWEZOG8BMuBr_RGikbi8NvrOpfh6fpGtLVNh1NfAS3c55GdaI4NbpVBkhFRdlMoHMgQOCJmxsrM_eqrwTs69twK_zretjsmC5q3gir-jC9oIot2HZzym9F9Iu73sQ_AFhTIoCMVIv_k0RqyI5-ZOPUviBxNOWnbHDt_FIWV12T6nAwSeOZ870-F1gNu-Zx1itQ9cdYyzeOBSttSMGhvt13PA_cgd3kVnj1PAPdLGyZTIimUNFrYGZf2nDyQvTZayL0A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ریدم</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78962" target="_blank">📅 08:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78961">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">احتمالا نیمه نهایی انگلیس آرژانتین و فرانسه اسپانیا ببینیم</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78961" target="_blank">📅 07:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78960">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2aa8b89a24.mp4?token=NO55uF5rGAqQtTYElBukWwJdXibGMRynXHW668w6qARuUAbRTyv5AXCebah5To57HlQ_brpMpnlCOjwsBU4ny3lDjNJ92nlwph73rkY9EKtfTORJfOHFOXlFUSUIipFXE8ntyqAxL1snqZzsj-XDICq4CJVy4p21Qve-4LsREIDZZM2yvcZ9smnVQjkthznt91DV1w619QXm8MC1KHZXA5t6I-3K8DkpKaM6zqx0k1YdUPUzGVPeZpZkMWhEFjaNfpJ__I1kLuTGkPlYY2XyMFkRqRO6b-7-lOPuQGNygXYqtzpt9KQiEDa9pW1lGe8FLary7BzSb02HYfnxXxCCYTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78960" target="_blank">📅 07:55 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78959">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یچی میگم نخندید،
تیمِ رنک ۲۰ فیفا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78959" target="_blank">📅 07:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78958">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">گزارشگری که میگفتی عزت اللهی رو برای بازی بعدی از دست دادیم، بیشتر از همه به تو خندیدم حال ندارم اموجی خنده بزارم</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/78958" target="_blank">📅 07:39 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78957">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t5aDLT9pXpA8zy148zTpqWXoK6ZVFD2g4Hg3qx8kLkXKUOJIUf95LVKNJNzns4NA7AkEfQaEMqnCQJ7xfBFQ53WE0FczefNUaBNr5hWRQZhKoHVu9T8gVUXMIuE8huDAnK6SGQrxwK_rhrMCGNePn8QreCALi6SHyHWs_nFdmgSeaBj9IhJmKRYusKuFraJ0n5dqbnT0VSelJ8zcKgLA9Jwr9z0f4HSds_Fw9Z_op7QuW4u9dT0ImehiUX7xrsmZa83m6frkvuN3VXU5HEyHxVYqfaedwSo3JDDmZ9SrnwVYRvg2KxUR5LV7N7AWvPAQ1nHTwxSfBpt8gjokgDTJVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مهدی داش چیا رو که از دست ندادی
😂</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/funhiphop/78957" target="_blank">📅 07:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78956">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">صبح بخیر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78956" target="_blank">📅 07:31 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78955">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">ژنرال خارکصه تو چقدر گناه کردی مگه خدا هم نمیخواد تیمت صعود کنه</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/funhiphop/78955" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78954">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">عجب سوپری زد اتریش</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/funhiphop/78954" target="_blank">📅 07:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78953">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">یکی ژنرال رو نجات بدههههههههه</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78953" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78952">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">وااااااایییییی</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/funhiphop/78952" target="_blank">📅 07:28 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78951">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ژنرال صعود کرد</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78951" target="_blank">📅 07:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78950">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">اتریشششششش حذف شددددد</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/funhiphop/78950" target="_blank">📅 07:26 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78949">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">تاااااااسسسسسسس سومممممممم</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/funhiphop/78949" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78948">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">تاااااسسسسسس سوممممممم</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78948" target="_blank">📅 07:25 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78947">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">ونزوئلا زلزله 7.5 ریشتری اومده  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/78947" target="_blank">📅 07:24 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78946">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این وسط یه چند تا آژیر و صدای انفجار هم تو کویت و بحرین شنیده شد که چیز خاصی نیست احتمالا حملات پهپادی سپاه به کارخونه‌های پرچم کرنر سازی بوده.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78946" target="_blank">📅 07:10 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78945">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">حضور ۵ دقیقه‌ای ژنرال در دور حذفی باز هم لغو شد.
💔
گل دوم برای نماینده‌ی رژیم صهیونسیتی در جام جهانی.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78945" target="_blank">📅 06:52 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78944">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">گل دوم برای تیم دوم ژنرال</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78944" target="_blank">📅 06:48 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78943">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78943" target="_blank">📅 06:29 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78941">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">پایان نیمه اول
خلاصه:
ژنرال ۱۵ دقیقه در دور حذفی حضور پیدا کرد ولی در ادامه به واسطه تبانی پرچم کرنر با رژیم صهیونسیتی این حضور لغو شد.
💔
#پرچم_کرنر_۲۵_سال_آینده_را_نخواهد_دید
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/funhiphop/78941" target="_blank">📅 06:27 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78940">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">عجب چیزی زد بازیکن الجزایر</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/funhiphop/78940" target="_blank">📅 06:15 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78939">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">اتریش ناخواسته گل زد</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78939" target="_blank">📅 05:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78938">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">این همه تلاش اتریش و الجزایر برا وقت تلف کردن و زدن توپ به در و دیوار دیگه صرفا از سر تاکتیک برا مساوی کردن نیست؛ انگار با ژنرال مشکل شخصی دارن بی‌وجودا...
💔
@FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/78938" target="_blank">📅 05:54 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78937">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یادش بخیر مانوک خدابخشیان ۱۲ سال پیش خیلی دقیق این روزا رو پیش‌بینی کرد و گفت یه ژنرال با سه تا تاس بازی می‌کنه...  @FunHipHop | Nima</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/funhiphop/78937" target="_blank">📅 05:43 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78936">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">کنگو هم ازبکستان رو برد الان فقط میمونه بازی اتریش و الجزایر  این بازی مساوی شه تیم ملی جمهوری اسلامی صعود نمیکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/funhiphop/78936" target="_blank">📅 05:32 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78935">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/funhiphop/78935" target="_blank">📅 05:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78933">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z6d_Wu91TtlFprSeuhfkEiy8o6lM2jIXQZp49TTYXA6ZT4s1Il6CpqZHcCANbiZ1x-2LeBP9pQF5gYKKrntxYwY2bjYI8lU-Uk9MCWmzMjQ6quAT55x5Q9bZ2XfKgwVGG9Z3t9eEC47kLuhwVDPw_UrgM1ffbFelw7qZcLXegtR63VYjzy-2piQ2BjIPvmG9EjCanpRX57wP42sxi4klvPWv6KsTNUqSuO_RknPRtNddpwtpA7cagrpVfhHYMy0P9tdPubgJHmvUTF6kPh4KfV4iQ1rOo1T7BU8ryTioeWHa2NhTXZ_iwl7kJosp1kqVHHMK-nQZRgYbw1HWAo6oUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامب:
اگر این وضع ادامه پیدا کند، ممکن است زمانی برسد که ما دیگر نتوانیم منطقی باشیم، و مجبور شویم کاری را که بسیار موفقیت‌آمیز شروع کردیم را با روش نظامی به پایان برسانیم.
اگر چنین اتفاقی بیفتد، جمهوری اسلامی ایران دیگر وجود نخواهد داشت!
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78933" target="_blank">📅 05:06 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78932">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">چیشد پس جادوگر مادرجنده</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/78932" target="_blank">📅 02:17 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78931">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">طبق تحلیل من آمریکا دوباره مخفیانه داره کشتی هارو اسکورت میکنه ک از تنگه هرمز رد یشن
جالبه بعد از تهدید های سپاه قیمت نفت هیچ تغییر خاصی نکرده و این نشون میده که همه چیز تحت کنترل ترامپه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/funhiphop/78931" target="_blank">📅 01:42 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78930">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">سلام فرید جان وقتت بخیر
ما بندر لنگه هستیم اینجا چند بار صدای انفجار بلند اومد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78930" target="_blank">📅 01:38 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78929">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78929" target="_blank">📅 01:18 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78928">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CIUb2Yc-zSmD1yxjw3rNHy3wgTFqnsNfVDEY1t2o6xzdXQWGgvX60lyq8IaCCws0j4PjNgyff9Vt8L02paP_bfCq9PtwiFzbXnThojPh7-WuJyzGAOMUbnfQ_WCDFAAIl_A7_NXi64Qjlpu1gR6ta7AjDBn1BYKiKwfw_3kMSW8Pe7uH-fluZ5ivHULnpkbZ10rFI01dHhgW8WJHXd7RcPS6YOpzaDcwDu9aul8xnb8tYj0H3gx1Zn6M39_n5r4KCEYFqll1hDPkXStjI2U9yarqtKTKNIi19MbRTa1CCq8q6Jlvm2gRKaftlQKyecDh6PPJ0Y6LpVNvdFMPBlDSFw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مودریچ چرا این شکلی شده.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78928" target="_blank">📅 01:14 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78927">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">نگران نباشید دوستان، ذراتا دارن تبدیل به پاپ کورن میشن برا همین سیریک صدا انفجار میاد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78927" target="_blank">📅 01:02 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78926">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">مودریچ چرا این شکلی شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78926" target="_blank">📅 00:59 · 07 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78925">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">کیروش گفته امشب میریم کرواسی رو برا ایران ببریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78925" target="_blank">📅 23:56 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78923">
<div class="tg-post-header">📌 پیام #48</div>
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
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78923" target="_blank">📅 22:52 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78922">
<div class="tg-post-header">📌 پیام #47</div>
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
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78922" target="_blank">📅 22:44 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78921">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">اینم یه آزمایشیه خدا داره منو میکنه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78921" target="_blank">📅 22:15 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78920">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">همه ۵ سانت و ۱۰ سانت و ۳۰ سانت
واقعا این عدالت نبود
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78920" target="_blank">📅 22:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78919">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">نمیدونم چرا اینقد بدشانسیم
۱ بار ۲ بار ۳ بار ۴ بار ۵ بار
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/78919" target="_blank">📅 22:04 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78918">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بهترین ترک یکسال اخیر دورچی ریلیز شد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78918" target="_blank">📅 20:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78917">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">همین امروز با رفیقم نشسته بودیم داشتیم میگفتیم بلو کیری خفنه بیارم قطع نشده و کسایی که ملی داشتنو مسخره میکردیم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78917" target="_blank">📅 20:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78916">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">بلو هم قطع شد</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/78916" target="_blank">📅 20:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78915">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J4dTesjd9u_6XkTvF2NWwSh57ZbbArBftLSVv3HcYykjGHP_j9QcBxpdp2jfdgnAEPIG46lDn55-Svsoi0JpAVrDOJ3umPZFs1CjGfMJ3vFA76_HjKG9icq_Gil5GMjfy8bo17lblzvhjmxb036635FSJFzbv92NbUv2VEPRe-okONuYthqQF-ElQ5JjZ5bFG_itPq4qRIRZ8MZWavN5_3rFvl-mVPrzQ-yw4bADLc5YUYsI-Eb4npnF0Nk25hsO1dKT9Xk1Tf4A1OYySBVz9r6TENwq2WBmHDk7V_UJx0KRWgVLkHJZjeBREiFf-H2Wf1RaeaTQSg0jAAoM7lVcEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اتفاق بد برای هلندی ها
فرزند تازه متولد شده خاکپو درگذشت
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/78915" target="_blank">📅 20:05 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78914">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LxyCOcYCbWLeHgvRYahoS_5PNwUBfenlpO0J47HRLKScs30kKN1OJjMv2gn4oI6X7h6Uja33u_6EM9AHWvCNrfilR4zsn87aY-LRMOQlYZ_gZX2nKpL67-KoP4kom_Dw6tHO7vG2s3aYLbjZCGeVFXFF-4oo-5_GNoVLFyB9752KeEFe2HSCb9KbZsosXkwxQKIqgKwzWD_colPnZQKMeflz-HIrjVUEBy_aL3PBglQiZUMHkyy6G5hid3z4noerZ76cAiMf8ta5D5ErQs8ne2tDjctrc92r9d5b3eXQt_jzVOV_4LZH7J-iZCg2sWcZHMP_LNP5n1bqqqFX7qtkBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شجاع رو کل دنیا دارن مسخره میکنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78914" target="_blank">📅 19:58 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78913">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cRtyEU-JQw9r73P22JubZZrr5yCYUrgbMny-cQxn3J2N3Pcow5MPRkDJFz1lmdQmaMHV573mMKAeeKabmOR-sQBSKuYxehfWE-sG04X929luWJWpTfsBCIeqE9t6G_HZezf7oxrSGl_WGoV0ZFzWlw68QkgmFmi2rYDicHA7izXM39Wv275tik-W52UIa-u4jTFR1zFzBtDdRSIns2tCs_GYpmx-7Ju0kTb84cRNLgUn5wB3_DmTm6tjW69v_RWWD6-co5Zo_G2FIB1gYNC4VbRyL_nGWBzUBUdeRAughgclctLD06ft99CGXozPyXDvbfKNJ3UeB5GPfQG1wTzvTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این جام‌جهانی هر بازی داره منو سورپرایز میکنه.
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/78913" target="_blank">📅 19:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78912">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jOiRd7w-WLyITHEn-fd5fBeICDr0yDNTvA8hGzeJV-zhUBoFX2ebkh2dQFzv5_RAbpHiDvNkvY03OS1rOKneq_xnnTMEdmRucwenUlJVjtjtXmE2VmLoMwFI1axb_wPocR7sjax4oOg_uU7SIO4m_kE8PxEL5XoCrOntYZiKqHv0rET32C4c-7vf-SxbZCFkOaivlLZS8WobOd4tSzD22G5f9nsi0uVK-3Ap6_S0ScRg5UXvWC2lRBdL_sMgbJEi8vwgrPHfFkqoMZvzaGhSCAjPzkj0Y9BWNjFl7vecda1di1gJ5lrij7SYNCO8XZmNFh-iSE770ocXATRghBXlKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کی گفته ایتالیا به جام‌جهانی صعود نکرده؟
@Funhiphop
| Jenayi</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/78912" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78911">
<div class="tg-post-header">📌 پیام #36</div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78911" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78910">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QD8Z5lowHMVqk02FoxSmtILr0u__XB5UGDGlyfMT6J_by6KMuvSzCk62sKnF2BhjxUDAbzQiAV4lNbgAC9vATPUdKS7_PTO8EVvT6aFVwFG9AN5Vz9nHikwwHJ5M0h2pOf6nsMnz_X8mIttjKYky7iMa9A-1vHz5aOCvabq9PeQH3PsQak4G8ol2pEVrP7A7hda4R22DlYARKrxzHUZnOCi-bAEWYbDTvWW9J4MD7E7oXPP3ubLR2UyvDK4M2BrKPIBWmJl9ceY9piCSZS9AK90cbWuZwpcAs0Uhz0z05bjDvZsc1B5Dn-Qan8L_616_jPDToyi7GMPgbVCWhDF24g.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78910" target="_blank">📅 19:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78909">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">همه ده سانت تا ۲۰ سانت نمیدونم ۳۰ سانت</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78909" target="_blank">📅 19:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78908">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">ترک جدید حسام تی‌ام و حسین تی‌ام به اسم " West Side " منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78908" target="_blank">📅 18:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78907">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tXeqlxko-UtNSGNcQ2bbzWFVxf3LtsQlpp8hfLxwuShopxKVpAOo90Rtr-j-UaWu5yYv9T0bIpnKmnDAwMJj15RQ_tZ1_B8qW7_AuZHtKZwzBxW2YTzW35HQwcCwEIujCnm-3g1aKwUVdI03BT-fm-WeRCd5VGBSuDwZqY0qIqTA-oMuYOjKyFL1z6F4w1LWMo_dfoJAy8v1BU9JxQ8b1PZzvPJ7uUWr5YqHLNNhVvzLQPhS7i54yt4IT_woCI-kCgSB8HqsLL2KyS3jsTfi1M-ariQ3QKYxcpx0CHMmsB1JezYzMzIksVGsARY1RfXefitTapJUtctEyMJuWYHILA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/78907" target="_blank">📅 18:28 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78906">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">موزیک و موزیک ویدیوی جدید مهیاد و دینا به اسم "ATISHSOOZI" منتشر شد.   SoundCloud  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/funhiphop/78906" target="_blank">📅 18:26 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78905">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qa3UKKt-5nNs6GzsNcBBUkB0m5MkmUl4cCDXKjnp_oKeZuJBueNN9Z_O8LLUQrfVOToVx_B0Q1bLPVY5EImsbcBaG_J66DKExDmH3vG4b1wfDeJph0hyOpcAub2p9Q3CR3v4z47AJsX-9oMzy__pyDFacDdFA3MpGqq3UWtUeSbmIwMvnyub_jJ9Lf3x9Y08ZWp2gcJ6kYvUWKY2jyr951uI2RQQt_JXV-RjCSa0MO9cJdHRV84KnuANXo2UNAeM7vNk3eBGyrEdGvgWrWBBZ-Ilxx30c_bpBDUf5K4yz__tGYMBG3X8HHGbvGNUSB28uRgRMSs-Awlg2KxzbQtIgA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/78905" target="_blank">📅 18:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78904">
<div class="tg-post-header">📌 پیام #29</div>
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
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/funhiphop/78904" target="_blank">📅 17:51 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78903">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kheia00O7LF2IjbfB9oBU6N1ym3_n5nJwTNUZPI63mwNmEw1KJsv2JVDPPkvR-Wp8yKjqyVLLPhPONmBYlJOJEWComrDLVIl6Yd8Bdg7q2SGwc_OLz9iSIFS1bMchPZh145gBzD1wcFreI09rFuBlos--4yxFxeWsxz6jtLf-pvyEBLgezdwQzn2BOaQ6hPzSyZc7dfv90Z-vs6XcrEpTDuPI81fuPqsd8A29_iUlCxhmbsuTc5JhFZ0GU0MgDn5IwZ5nEUL3n3CGV1Dy3PQHSdyfkUr20mzcGS0K39JEtfCBL44EzwM1LzLCTq5GKgHe5mdrZjAxFbYfM7-swXKrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/78903" target="_blank">📅 17:03 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78902">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">سازمان دریایی بریتانیا اعلام کرد که یک نفتکش هنگام نادیده گرفتن هشدار های سپاه پاسداران هدف پرتابه توافق قرار گرفته.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/78902" target="_blank">📅 14:25 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78901">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RB4R-B3B2ISx2YrKdQd_dVPpk7H7W4fkr0GJYPDo0cxOX4EyQ0BJwYGnX21CPy5CyFecsZBjhRF_9pP7PMbJnmzFUeDAl1AQ4Fv5Dm12gmr3FXIsD4Qm-oDzE9ZJeMajyD_yhttT0sAh-ycwgso793pf3ygiv0vcOwDn4XeWVAsy6n7hSrV8Q9N-eEdh7RQLjCCSlM5FwOzhr759TNa808Gi346wbeVkzwxySBj4RfHIYv0EXgcmDxzLOtLnPLlDmhZ1WKPTCYzg9uHWBMP-Wlfk7Nq_Udqd0d1MD0XhyX5E_AjPFP8AASKkgnLFXWWtH96M4e7HfQmAS8IXrDvdfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روی دیوار فلافل فروشی توی بوشهر نوشته بود
خدایا همه مارا ببخش به جز طارمی
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/78901" target="_blank">📅 13:35 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78900">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=ccNsbmT0vk7WIXM_Bz12TWxm9LKo-RAy4OKm1_vrryrCpFK9zDQ-sy48wKTRfLa61jFYvr7Ai1WmZ2ZdxujLJC9P3lcPeyrCoUXJ99VIqijksM8oJprCttGnwQMd8cJpCv-dfu7x2bWDn6CwH-KxIM54ulPpDWhtZRr8d_Ehu1Yqt2ButTQU470pBqC-0b7lhkOtSD5QHC5scdOsEtD-NP7Rs_DscqMR-VyMWQDMpQ0JoJS5LJyjbuPRWYE3EUfXoZOo5R5SqHUjJVzgWMRcQtF0NsK36TIfo7g93LTRDCdmzHd1Lrb3X_3PLeyh8v4PxZZLYBGZreC6y05Rp_W0aw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4960c204ca.mp4?token=ccNsbmT0vk7WIXM_Bz12TWxm9LKo-RAy4OKm1_vrryrCpFK9zDQ-sy48wKTRfLa61jFYvr7Ai1WmZ2ZdxujLJC9P3lcPeyrCoUXJ99VIqijksM8oJprCttGnwQMd8cJpCv-dfu7x2bWDn6CwH-KxIM54ulPpDWhtZRr8d_Ehu1Yqt2ButTQU470pBqC-0b7lhkOtSD5QHC5scdOsEtD-NP7Rs_DscqMR-VyMWQDMpQ0JoJS5LJyjbuPRWYE3EUfXoZOo5R5SqHUjJVzgWMRcQtF0NsK36TIfo7g93LTRDCdmzHd1Lrb3X_3PLeyh8v4PxZZLYBGZreC6y05Rp_W0aw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این کونکش دیگه خیلی رو انگلیسی بلد نبودن مسلمونا حساب باز کرده
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78900" target="_blank">📅 13:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78899">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZkBa1XCr7c9RzXodfXpJTKU9Rd5RNaFQlwtIbGT4LXif5pABtImQxb_MGzHoZHorkhaIoiAaUqdszDoNS8Gn2HckAJmNnaktleHnAsMhpCDTjnjjVN8QLlgIpVAMwwJglNWdhacrPljrUKEMQS1D3AuMHJixodgasxiNmDBrzlprslWVcsSvI9p8fShKfMRW2g0Ht8NIZ0Sh7qYGo9tIEwawT2AY0cMjwJr7GYd-az1hkVfx05I9uUlRm1ZAZOxqjPkh8-wGZCFVFuz1FQU6haVszyrM8Nm1mlNSTKqJLBlDHMvB0YZCGeAY6DpOrut7UWdeACsc2f92vDFaglILg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یعنی به کیروش زنگ بزنم براش آرزو موفقیت کنم فحشم میده؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/78899" target="_blank">📅 13:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78898">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/78898" target="_blank">📅 13:10 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78897">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTemSah Bet(Mehdi🇵🇦)</strong></div>
<div class="tg-text">من کیری خفنم پسر</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78897" target="_blank">📅 12:43 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78896">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">فک کنم تتلو کل درآمد یوتوبشو میده برا قبض تلفن زندان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78896" target="_blank">📅 12:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78895">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تتلو چند روز دیگه موزیک سومشم میده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/78895" target="_blank">📅 12:18 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78894">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYUWNADSphpvAWJ1zoHy5AyrgPVW7glnnP7EoH9SWlMoBIfNuf9QiXTd1cdThqxhbLVo5hqkFaSiq-8dxERy4YIeOhStPu32Os4PMhO8-4tJ5yOS7Ab1PXxnCLUsT2dkiwFniJ2miFqzA3ppy7WUv01gZaKHQ2kncbzbD0_L2QG-FixjRwU-0AQKcikjGDcfOuK5d3qPQ20Yq6iJigBzAo69Ys01_GGFgboQdcBUsFEZ39k3qiq4oI1ZRax6WcgBbrQ-Ma3McIiqbV7iAHVouSn4lqz9rMzV_yAXWxDvg6Rj3azNBvD0hqbG3u9xYA1Yes2wAMsH8CFWDUKB8pLukg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انقد گفت بدویید، دویدن همشون رفتن تو آفساید.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78894" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78893">
<div class="tg-post-header">📌 پیام #18</div>
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
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/78893" target="_blank">📅 12:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78892">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dPmVgBA8VvR1xcGMR9zO3-n1t4LXw3jlhkwnZNlG1mK7VxeKvlQqjUSGFabnQey8mrFd9_oDcqRcHWVFewHiAWtP75Hc9pKnPb58MQRBXbGmamE8nwqcHtDstnzoqFRGqeJJyNPQUjbcKl-PKOA4BiTJbEGnXYQAdn2usrlSGznIpNIoRpnUgYkqrCjNnxdmzuwAzBZpNOQrWeaZabXgHMHB2WrNXpq2eLyn82v8jWnu57LyYsb-vFN_eYFKdHPh-WdzDv_UO7l0pXQAXV6z9Owl5o3AQov000yIGqwi1GgH4aaobbgzF1yuythz4CqJ3dt7LvJp8CjFm40sMDGKvg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/funhiphop/78892" target="_blank">📅 11:48 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78891">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">حتی اگه این تیم رو دوست داشتم و حتی نتایج بهتری هم میگرفت خوشحال نمیشدم.
چون هرچی شده باشه از رو خوشانسیه و هیچ برنامه ای پشتش نیست و نتیجه ای نداره، تیمی که برنامه پشت نتیجه گرفتنشونه مراکش و ژاپنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/78891" target="_blank">📅 11:38 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78890">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">مثکه تیم باز یکم خوب بازی کرده و شانس صعود بالا رفته میبینم یسریا شل کردن خوشحال شدن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/78890" target="_blank">📅 11:31 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78889">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">سلام دوستان من تازه از خواب بیدار شدم مشکلی پیش امده؟
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/78889" target="_blank">📅 11:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78888">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">جدول حذفی جوری شده دیگه کم کم منم دارم به مسی شک میکنم</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78888" target="_blank">📅 10:40 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78887">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">اوووووو رامین رضاییان</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/78887" target="_blank">📅 10:32 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78883">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=NBk_qDs7SDL0YC3i4PRZwoygw90_XvnAwF5qbHMgO2w_fWacAJ8nVCJGEREwNIj5r4calWG6C3E1CB_X0KS6oSPpse7dQiOQKJstiperg4WlajhJW_EHD7HRfR9vBp4VF9AqwFu8Jo_5f3-s_RYHi1N2G-taIequfel69szSxJyuxf8uKTnEXtycJSC4CMNmDZNVlvFrtgX7Tp-dN39HU6tiRSEBKiJlc4mtprFlx-Beu_g8jKRl6QU7gmpjyNjocXbyTrzFXYknR1zRITRu5RgzF4r5ux-5auB8su-lEQ5NV8WFtM3KNEDn3-xSubtNwZ_itIpy3YysFNqrNqkvNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be30b9f5bc.mp4?token=NBk_qDs7SDL0YC3i4PRZwoygw90_XvnAwF5qbHMgO2w_fWacAJ8nVCJGEREwNIj5r4calWG6C3E1CB_X0KS6oSPpse7dQiOQKJstiperg4WlajhJW_EHD7HRfR9vBp4VF9AqwFu8Jo_5f3-s_RYHi1N2G-taIequfel69szSxJyuxf8uKTnEXtycJSC4CMNmDZNVlvFrtgX7Tp-dN39HU6tiRSEBKiJlc4mtprFlx-Beu_g8jKRl6QU7gmpjyNjocXbyTrzFXYknR1zRITRu5RgzF4r5ux-5auB8su-lEQ5NV8WFtM3KNEDn3-xSubtNwZ_itIpy3YysFNqrNqkvNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتون باشه این ما نبودیم که فوتبال رو سیاسی کردیم
و خطاب به وطن پرست های فوتبالی بگم که کاش یکبار هم که شده حافظه بلند مدت خوبی داشته باشید
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/78883" target="_blank">📅 10:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78882">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">چین به اینترنت 10G رسید.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/78882" target="_blank">📅 09:47 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78881">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">می‌ثاقی:
اگه بازی تو لیگ خودمون برگزار میشد، چون هوش مصنوعی و تجهیزات درست و درمون var نداریم الان گلمون آفساید نبود و برده بودیم
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/78881" target="_blank">📅 09:24 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78880">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/go9ONhn_93nljdEnyzAIWVeRaQ0qa5kIRstEAWHWqhNovaL820DP6OFkTVm1NmozEMx9XByJORLMg2mNbrYurS1yVZwZV2Es6vsSi7ZqCjV_qX_xfLeq0_lwIgKEaS4RwUMB2DbTp6kYrv3oDfLhi3huyDVjNAnsM_GWavOvc8WRBYmQ-5VhxBlBrVqI7Trfm9LI4Y0u0zwTxMllyQ46C-FQbrhAT9Y1PbrBdiVw9tsLFnkOCNCpXj2rLFR_xR1jN5vMFLe9IYfrNRiHVxW-L86kBk2rBgyKSLLVn_cyfglUaIHufpKVM8zY7WGcCNg9bVaKbLJ3vETdlbyMkymMIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خیلی دوست دارم بدونم این شیر ایرانی در چه حالیه الان.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/78880" target="_blank">📅 09:17 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78879">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">1: باید یا غنا کروواسی را شکست دهد،  2: یا کنگو نتواند ازبکستان را ببرد،  3: یا بازی اتریش و الجزایر برنده داشته باشد  هرکدوم ازین نتایج رقم بخوره تیم قلعه نویی صعود میکنه  @FunHipHop | Farid</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/funhiphop/78879" target="_blank">📅 09:16 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78878">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LrRjL1lZWF8qiZmXwkwqUxZMxQhkUgoOYM52yqBaVx2bVA2Q_MI5ptvjw_19T5snK4kmZsKU1rRiiRJb7P5WYeIjCnYyAa5sqV4XifBTIjVe-QaOjBVyZVQEGYo0UUNjiCD_8e0sQvX2vyoWJySSqxyg97Yl0BgQdeXgYx3sQ_RiFJ69yTQ8NDFrIEb2fHDLbgJbFmDvfXxYCYmeQ79p46R-lE7l-j6YaaGzXoz6DS71jJMyn1j4lGruQ43OZus3_a6EwlN_43mtnexcE67mnQq3w_ayAB1Q3eqIlu-2LVltfF7uN851424NU2BY-BB-qys9lGTG0RwIEIi4C638lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی عکسه رو سریع بگیر تا نفهمیدن کیری فازشو دارم.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/78878" target="_blank">📅 09:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78877">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">رو دیوارای تهران نوشته خدایا همه مارو ببخش بجز طارمی، مردی که ایستاده رید.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78877" target="_blank">📅 09:06 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78876">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=W3jpSFvrmmsmtuBhuEEKdmmFJ5IsFk3AHTguMrdG23p-9uCJk8GkYpQsnZRGyxgn3HgC4ncfGouwJ-iuNvqZOielprFzXbgdW1_tGFEYrgx8aLF52WwknM_g14qbS1LSKsiH3vyDELmqKkhwWJFJstX-rz-jMaoxVCPRlt7poJimtODYxRU0QQSOln-A97oC3T0AJODrkoXWSTT156rVHH9m7KOUiUiZDsakhv8jSWcLM_5iDvzuPM2RsGacIwCkmbLxlnxMTQngICpth11moV-hC4m2Cyr2ZbvB3Ijy9mSL-9uoQ5nh3trK-Sa-dybSWLQsvJEMDewmwpgptVQLjQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4c5a352edf.mp4?token=W3jpSFvrmmsmtuBhuEEKdmmFJ5IsFk3AHTguMrdG23p-9uCJk8GkYpQsnZRGyxgn3HgC4ncfGouwJ-iuNvqZOielprFzXbgdW1_tGFEYrgx8aLF52WwknM_g14qbS1LSKsiH3vyDELmqKkhwWJFJstX-rz-jMaoxVCPRlt7poJimtODYxRU0QQSOln-A97oC3T0AJODrkoXWSTT156rVHH9m7KOUiUiZDsakhv8jSWcLM_5iDvzuPM2RsGacIwCkmbLxlnxMTQngICpth11moV-hC4m2Cyr2ZbvB3Ijy9mSL-9uoQ5nh3trK-Sa-dybSWLQsvJEMDewmwpgptVQLjQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عصبانیت سرمربی مصر تو کنفرانس خبری.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/78876" target="_blank">📅 09:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78875">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">ولی امروز دیگه بهم ثابت شد هر پیشبینی کنم برعکس میشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/78875" target="_blank">📅 09:01 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78874">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nMz_vFH5EPoN3H1kq-bDmyvCIOpsiGwChovuc7TkinMa1wuBmV7WKx8yFFySCI8XT_Wpu67q6i6YDBWWAHdr2waA6D2AaGe_7XPyOA-NSdrsy4kWkLwxlfa6e-a-8vxop4Bwyqn3CSpOpSU_VNtXAAaa2izc_6gOXNjlb_ZSI84i1IAtetEsJW2uduIu586ThfYdS4QcHFNUkQddjDJn8aN-YR9ECN7-LXHale7rFFUKkE6HEdXeZaNhX9yyYxAv82146SO1KGUtKnC1PKXQMJwf7KxOo41RzktY29IuWih3eh3eUYA3wUaYZ76AjCE0pfrn9AU2ddOFCJ5w7U8P2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدر عشق است
گریه نکن رامین جان
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/78874" target="_blank">📅 08:55 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-78873">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">احتمال زیاد تیم قلعه نویی صعود میکنه و به سوئیس میخوره
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/78873" target="_blank">📅 08:50 · 06 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
