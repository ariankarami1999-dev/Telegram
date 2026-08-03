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
<img src="https://cdn4.telesco.pe/file/sywsf1y2pw3sni9f5rezvOZVFA3oqMY9tsb0N0OSXMn9S1d2wHvmh60aTZrZWPkFGyr-lNezLnB1XxpSgZmLfRMrjMPLQMw7agLdtIkCOx_5ZgdKBkx9R2D1ofiHrKPlG-cIZorlUeC1baFRpQg2g2pijeY6Ai9Zw501DJRK9DK4xvfrfKHy0mf9yP5mdK3SgYae25Qp79cB09bNeWU_FvAFhGf-3aLgdUs7cPf5K3R1aMJUG-G7hp5Lsfd-jaGOQomTxrtiWgHo-tnLzRQpq7rJY4CDtJ0dM1W9roTisykRuIX1faCjG54hVSWEg8G2xuifR1FFC6-ifbzt_PDJxw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 225K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-12 08:27:22</div>
<hr>

<div class="tg-post" id="msg-81710">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فوررررررررری
آکسیوس: منابع نزدیک به کاخ سفید تایید کردند که تا دقایقی دیگر ترامپ دو نقطه را خواهد زد؛ پشم‌های زیربغل و خایه‌ش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/funhiphop/81710" target="_blank">📅 02:27 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81709">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/funhiphop/81709" target="_blank">📅 02:06 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81708">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">عباس مگه صبح نگفتی تنگه بازه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/81708" target="_blank">📅 01:58 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81707">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سلام انفجار نفتکش شوخوش
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/81707" target="_blank">📅 01:55 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81706">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsApK5Gp6I_1r7F41YOvWZqQsFxAbNM-c24QB57h8kV73LQqwShDVaQkQCKuWwiuG_PHNWQ2ON_DDD8CBXUwT_0bd0w1O7VFHDG1BDaZkdPHuo6uWzB_yPeslag9cOndIP4FIctSNwWXOEYZyq1bbPU4g0OQlF4VYX77CC0FGvDmAP5zrqa7Iz052jZLQRVQEuZaCanNfoku7uv6jFpVO5vxj_0eegJ-HVGqlJxoyeGa4sW_SOL9D1we6odlCr58cPAYuxctq6rnWthquGnA_30HXPCYHW2IFbODnvveXwbvuAJuNY99Sm5S5pAb8NoppKQifygB2w1OIXSaCM8ZUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وینی کصکشکششش
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81706" target="_blank">📅 01:11 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81705">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/adGKT64zDj-QF-FtoEeskPI6vgLEUprMBfl5o8kVAAAB9XvJPJsMyxCGpXjjlZbpU4e6Ox7K7TZJjdOFbuEd_zxDopffXGuMnQza8gtuF7u94PzAVZRFHnx9RHzYdiWB-weyUpMBTjvJOatUb0BZt6gk3eBAGViWfTiJOMcNIa0viNrYPmi2PoG_7LW9i2cDnX3M15uOh6Ecfg6nG1aKnP1FevQ-8TC0IpBy1hz1zRrBy4PMF5WE6lQS5vXpJdH6Ei2CRs5_Q0XVIMsJnwBBXs2lN-LEmms7n5jPk54Zgdwc808aa_MyGBttn9tQLjCSsfPL7QF1-nJaYz5L6o8Nqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استوری یانگ کید راجب اتفاقای دیروز
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81705" target="_blank">📅 00:44 · 12 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81704">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GY3d6KV8UIquTATiRJE2H6h36tRXrDkhzY4TBhGsCrksJ5Byb2XzxpJb1BJOb-AJzQY9fcNcu5I47bcmGvl3Cxv2rWryEXULz1ii7bIM0Vazy6uXTP_0Bb6e77oPW7-_r4OPTLM6N2r8Sa6wZiyc50Lb-llbaa6X8ih3r4-Jhk89yT7f_CMtze0R-cnbUThAdk5Ebm_RpAf4By2epU2eZFtm_2seBMSqYVHMtI8-d6oTM0VPS_YpYtDDI3aQsqDDm0fWljrznTUmvN7lIONgVkmi15IUfqFDMYcI8y2rkjm2BxhvHfu9c5iGUtDy-k9YxuDjD6mNA7Hr8dA9SlmwTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">توییت پزشکیان
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81704" target="_blank">📅 23:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81703">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">حماس خودش خلع سلاح رو قبول کرده امضا کرده، ایران بیانیه داده که نه توطئه در کار است ما نمیزاریم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/81703" target="_blank">📅 23:03 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81702">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TcYpssdcbWYnMB9zJOAL_pMbZMQ8ja1vtNMBhM28E6aVgcUg4NPv9QjIqPM3j7CbaXKy9_4qkL4w6W11NRn6refk5eRN_dGp5v-Pi0ii2nXGLeZi6-tS6gO9yfco2wpB1QbgC4sDyNiS4Kr9hhsX5wZyPyxud3oJumnnyElO-1qIzsrraw8RXfIS1Uy1C8pyPts-XKYY4DYB6_aIyK7Nv4FG2DRbvAih5jLzDACJ2B3ulJkfUxGfDyxZy1Sh7MALIC_Ht7HWrXDs3m9j7VtMWX8zKK4je3-ThZWWTOeuOTnNYsR9ZiMC55W8iI90bgRaU-aBs4ij8uy1PfOZR5n8eQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دکی ناموسا ببین کاراتو
نيروي انتظامي تهران بزرگ امروز یه دختر پسره رو توی پارک با گزارشات همسایه دستگیر کردن! حالا میپرسید به چه علت ، چیکار این بدبختا داشتید؟ به این علت که هر روز این دختر پسر میومدن اینجا دختره به پاهاش کیک میمالیده و پسره پاهاشو می‌خورده و فیلم فوت فیتیش ضبط میکردن
همسایه ها هم دیدن و گزارش دادن به ماموران انتظامی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81702" target="_blank">📅 21:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81701">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NmbBqx_DBJEy-agq756QLO6cfCfrp-Qtt1kd4ClwZ9JxB7br4YaDhhTYdD_COWPJlvuFCT6UPDU4F-KQlHZsU6eLknVMirqG_QfBt1MbAi0U_BPBl5clBtNyclLPcrXehA1WFQE67Eg-BDfjycRamOaqjf5phwsFq8qVzim8jzj-JMXZ6DdmDtxp7-rMmq9tBegMQGXsjHC5RQEu5Ssm2WgoHaz6rVmIT5aM77PHe-Kcu1JsJK3kF39Xw-v9iFcz1GObcDkjf8_qwpUp8zddoMQ4_JCEvGu9Xv_NZp0AtSVGKD-aRwk_VJdeTJ1b7f30Z4XHdRaSBQuFnf3f17Q1Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">- زنان با قاعدگی بارداری زایمان و یائسگی دست و پنجه نرم میکنند  مردان با چه چیزی؟
+ رونالد ارائوخو
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81701" target="_blank">📅 20:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81699">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل: علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81699" target="_blank">📅 19:04 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81698">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">وول استریت جرنال و I24NEWS اسرائیل:
علاوه بر اسرائیل حتی کشورهای عربی و میانجیگرها هم از تصمیمات لحظه‌ای ترامپ کلافه شدن و حتی یه سریشون مستقیم به ترامپ گفتن داداش خودمونیم ها ولی کصماد
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81698" target="_blank">📅 18:56 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81697">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KaOI2gBQbwdMnByBlD1zypJ99s0e6Y4p11O4oDvTBmUjhd8sIa_hu4CBvoOQ3OBlVBF5PgT46wRi54TEM4KLO5jbtEUsbrg55tg8gHGkbTDoEtN5C1hDh2naa_1vq--G24rFpDKc_AAK_a35X_XPCjjQvMsaobENQfVua0-hxyxK0MhNaWGAsBLaxCsOwPKaMABKxTtAJ1oMnSPc3eZO6OCsLEk0SzUPZ89_zMQKrh8W6ePL22cHtgBo_RyTrzwlpj-VmpRlNgJ089Gkv4jABSvQsQzPTaNZ1Sykh81gKyIZcy_EbZrtIEfoZp073CPdXSPv8AEizeugI_4PR3kRsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لاس زدناشون
😅
😅
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81697" target="_blank">📅 18:38 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81696">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/81696" target="_blank">📅 18:27 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81695">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">فوووووریییی</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/81695" target="_blank">📅 18:26 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81691">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">قاآنی رئیس ستاد مشترک ارتش اسرائیل و عراقچی رفتن عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81691" target="_blank">📅 17:15 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81690">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.  @FunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81690" target="_blank">📅 16:20 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81689">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dJru1ZMk2IStzFh_Jltk-OQweNyYABEcOKggKZo6Olr5TsM_zxDgNsToI87Ip5VK2V0f7W2EQaRcVoBO0poLqGHdB9-Y3Rv-jMz5l-yHxFBAxjqhtgzEU13mpv8DG7bNxhULy4-n3uBDIpJDXx3jKIi_TV5jyyzmbz9fRgqT7FkspJlTYrcfLVzo2EU8c6eoQZJlI2v1oFRkfR3viPJgLf-m264WRS83HzAZ8Kjs-qYY-T4fzlYgL35qjftr-T0wsdbO69N2FUMm1REngV3L9oDmikWu9gi8AtURb84cZ3Kx12ccK7zgDUUwam0dbDFgQQYnc8FEthKtHt1VuzawSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فصل سوم مرد هزار چهره قراره چندوقت دیگه پخش بشه.
@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81689" target="_blank">📅 16:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81688">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKU5V2ipCFWfhRc6-FnUnzwstSnu49mf-tVu3Z-KhKLJcv8sey890iCH6lQpa4spq6A7QlqYFSTQxL-50bHpaUdnpQHJTmcLGS0Y65tIxuIfxmTW5rCWx92xAfcniiSpoFz13nNUfzhWJS9-q5RJ6kYMMAMG1TEk8bpyjmArByFkaMQT0G6kZ0M4o9G2kSzcWYq8yqPIyISYze4YLZZHALm5M3a8lLR5H_zMkaQLLbB6u9dtGljX8Kr8kWbNtXhEynNmcmbATqSdITiSGr-7XAo4gr3sQxCXHR3N3sHBGfclX5M3N91hhCnZMUOLxN6Zwgt0FRRiayBKzsJHValxmQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Jenayi</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81688" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81687">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/N1DAIACPAtHGXvkgD_hiCwP4Hd8Nn5yedxEFGhNMGPPdU4H-MGiAcyLPds9hTatYt1Y3BNrmAgbXOTLe8fvgWp4nFAQTec3wsSTvcDaAANV79pzuiTomsQfNknv2I70gtDZalSSMQFBHyueYLcY67WZ4bJlrXRbC7W7nT_2EOZIKSvOF74oUnvz9-GB1SXscIDXSGdEuk_plAKZ0IzPPayHwSKuB0fBVwFt6PFy01mxEmNw0Goq9pZPSqjzDP_vNc_DsXCOvSgv1XMZl42MgYn4955muOFuveYq7nzYdt2-RKh92R2XTOsZnuPHvPnO9xkFx-Tb6adSoYx6BHBaiRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/81687" target="_blank">📅 16:06 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81686">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🔴
چین میاد بهترشو میسازه
چین به عنوان بزرگترین خریدار نفت آرامکو، قراره سرمایه گذاری های بیشتری در این شرکت انجام بده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/81686" target="_blank">📅 15:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81685">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lWNEK8z5Ceif6hEd3I_Hm4jdYTqJPADoDit10vJ9XGZwpMqWnZZTp-Y-8DeuMfJqpZWgxTw4cVvwZ4WnqId-XVbqpo8JpUHsu19Dgg_3l6hKAtwbYTV6PihnzJ-8gEMiBgU_IhAIBCxqqDpFyKSUQF0ymtxb2KAC8NYHLvV4tDrusCN1AJOB5W52-oui8RFulSuigBYWdUQJEl_0r9cS0TOnKPgPvN4CUzTJwmjCPiVWCaH3FQNqf9l0TitVC3H5LnKknMGY_MP3eP0Sn30SFgJQ_V67KNl97kAGa5kYdYBTwHteJqP4E2xGMeh0ln8l4sk6h1dXnFu4yNboo17rEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آگا یکی ترجمه بکنه چی نوشته
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81685" target="_blank">📅 15:28 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81684">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">نبویان، نماینده مجلس: عده‌ای در ایران با انگیزه‌های گوناگون از جمله نجات دشمن مجددا به فکر مذاکره افتاده‌اند!
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/81684" target="_blank">📅 15:17 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81683">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🔴
ببین ما داریم چی میکشیم
کان نیوز: نتانیاهو و کابینه اش از تصمیمات لحظه ای ترامپ کلافه شده اند
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/81683" target="_blank">📅 14:32 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81682">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T5edvptycMr5h3F4Tw_DNxW90l_35uWs8OqPCd0mbYxd4ERJysgxUvqE1QdiPldQuZJBDLRYF0awQhtqm9W63vCFRDNf-G4yBdJlONALinKJEAxlWesdds0m1p7owv_WQnVIrIjTOfS9aPLdJBTf5hi4WgHT10E-drQD-Y-5XbDwfDSbVeAVUOpq_ujbGWT5ygfs7QFVE5VZ2kajsAkKYBLWlxGw6EY5-622Bm-8fXFlfdcMXi3tv26n4EVUxvy3tnurMOaYlvfnhm_3jSj4HHWubMUJDvbPo_RbnCp_0dCpnLMAz1XHnJEG18UADAXgtcMPIJaUkJ9357tUF9mTYA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاضرم قسم بخورم کسی پیام بده دارم میگه خب تو پولداری ۵۰۰ بزن کارتم رفیق شیم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81682" target="_blank">📅 14:12 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81681">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">فارس خبر بازگشایی تنگه هرمز رو تکذیب کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/81681" target="_blank">📅 13:41 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81680">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">خاک فرعی مگه داریم</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81680" target="_blank">📅 13:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81678">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jT2lZOFviMiGZgTvAjcGHrSvTP8KM9O1em40ssGPi_vDszfO7E2iY6iI-cu_twRTrTAoNwf_vwoh51DPRbYIqFIh8ANUJfXw9mLwBW2Br3x-vwW0T5VqoFsaCOUNPtFzGkGk0KoOfViECWbO17PDkThMDbYHZYtAyz9D8h5-XRZ48m38j1h8CFT7LiIyEYfL4ZAVwiSSFFGO5X1-PQUql1BMaZPUVdV3Au0jFkdE4pT0zTsGmGEqo7UrZuZ7PvDMUSCVnVGVod_mFJF4jE8jHkWXF7TNYW7YLm00u1HHSBX0g65LknskHtjoQaI_R0sBPUFy_vifJRI80qSKvrDnOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F3LogtXL9aeOsRDAWlTxC8QM4qAkhJMJ3Dp0DMG2kYPKIfjWvNP2M8FhBc7xPr1BCuuGy_Xfb6tKucLihOIYa4LCuYcYg04CzHl2yWqT5s1FvOI3utL1n6z29mSPQphQodPYRoAxOToMRmMbZjjUGuyeQ-0JVkZFsfM30QVszXotFtpS0UimBEftZVYe3vhA1Ipdia9QcMm2dDJang7i0NPxTxbZRKI37uEnHUqRQrkuoRsSahErBmRcVCRz5O6B_0CnnGzvXUzaGjVJK9A9CES2-yLUOxS68wDENi8Bj7hqb-2eTBVuj2tBN8XReT9H1p2vCr8x9OKcXL_YVqSXyA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یسریا کسخل شدن فک میکنن مراکشیا به خاک اصلی اسپانیا حمله کردن
شهری که بهش حمله کردن:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81678" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81677">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sIqLrjrAqjewujPZl1wFBUuvENBwKEB5O7JYjbyyVHFGl6GO1RsHGEp_HW-A0NWO3fRLRxuYzrKik2d2XN_VCgIZE71cV6Ut1M0qfv6ACJ0gUuw4IfSFxq5l8l6x5lwaOLoX8hbfy3wx_Th6EFZd8YfS9b17u47k3iy6UOdt2AO9lFZfaB-xfx2NFoTc1h8GzG-Q5D-YQmR1t5kHJ1LJmkBWPctzHOqKD8K6v2mWvoLJ0YmhxEw6TYlb6-4NcvkcbzagPR1PSNksygjMD9ZNnpaTwijtZKAUwJxdxvK9cQIuI9R2j9H0gSq6Q0AQAUf5U5BXqeT_2GM9YiGP9CN_lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽
لیورپول
🏴
-
🏴
لیدز یونایتد
🏆
رقابت‌های دوستانه باشگاهی‌
🌍
🕔
یکشنبه ساعت ۲۳:۳۰
🏟
ورزشگاه سلجر فیلد
🎲
با بیش از ۲۵۰ نوع آپشن پیش‌بینی
👆
ضرایب شگفت‌انگیز
📊
نگاهی به آمار دو تیم:
✅
لیورپول در ۳ بازی اخیر خود شکست نخورده است.
✅
لیدز در ۳ بازی اخیر خود مساوی نکرده است.
📈
میانگین گل در ۱۰ دیدار اخیر لیورپول ۳.۳ گل در هر بازی بوده است.
🧠
بازی زمانی لذت‌بخش است که کنترل در دستان شما باشد.
👍
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🟢
دریافت سرورفیلترشکن رایگان
🅰
r11
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81677" target="_blank">📅 13:19 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81676">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZyyOcJRNfoYypgil-u7QcjSuodrK80qLQHdkUQeDvT8ISVymhwSg42dBsinY6yyPItoc_86NJtbYkKoP2v2GKGvjzelzZuCn1lwYWr3eVjN5zAGlW9bCPvwagLHl0GUuHhfEywI26fmexzTW_IKiTA6XywzgiPnHnMiKQlDVYe5W-OQu2yDoFfz9Yd-HIreig3gFyb_xLNFTCja6tcFlj9BQ-_OiG5kEajUIYFaT_ica8YdGBZ_mXYNHst5pvNbVsVgVdeMg0UdciHqGWTS5Bj__Gnq1Ptx3RkyH8Bi_8IT4mBYRIIb26tiLw_geo0tXCVJBroz8F0XoDxuDpRjQGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صحبت های یامال درباره فان هیپ هاپ:
اگه چنلی بامزه تر از اون پیدا کردید، من ابرو هامو میزنم.
#Arash
@FunHipHop</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/81676" target="_blank">📅 13:11 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81675">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cybPwaKTrI1tWu7q-hf2gER83fMohN_3a92wUbi_3nPvjScPdlEJiiyFTD5GvIqnQNyJMi4rA7PdXC724L2zAX6A98Itny5EmIftqkvMoaAEfdZbur0RK-1NUlbP92kW2-jrpPP-5WJDRfM6bh__bp_sOlmucFRSV4KI2R585btTldO3yQ-ZmCw7ciMaSmL21CPFaIMB8tUgqsOrITLMQ8PTb4GiZCFMyrWEcYtccJk3hVa0jUJvdKflhgfe3h7Wl1RIr3lVvBA7iiMr2B-Jh3oTKO7iwzL0KOq7Iv-qYIYrE9Ckrbh8RAvsnv9K3RsNvNM0ckQpKfg2nZqFHuCFXg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">۱۳ اسفند، چند روز بعد از شروع جنگ، رسانه‌های حکومتی گفتن پدافند ایران یه جنگنده اسرائیلی رو بالای لواسان زده. حتی یه ویدیو هم پخش شد که چند نفر داشتن با خوشحالی «الله‌اکبر» می‌گفتن.
ولی خبرگزاری‌هلی اسرائیلی گفتن ماجرا برعکسه و یه اف-۳۵ اومده یه یاک-۱۳۰ ایرانی رو بالای تهران زده و بعدش هم رسانه‌های داخلی کلاً ساکت شدن و واکنشی نداشتن.
حالا بعداً معلوم شده خلبان یاک-۱۳۰ ایجکت کرده بوده و زنده مونده، یه طبیعت‌گرد به اسم جواد قارایی پیداش کرده و به خاطر همین کارش هم از فرمانده نیروی هوایی لوح تقدیر گرفته.
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81675" target="_blank">📅 12:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81674">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dxa3cP_g-NT3-7gS4XjdaohO0UW2s945yUgzVXFOas7P9PJEvAWrFhXv83uEmSFnb04PpejmVAtSlG_G2KFBEsC9-blG2TwmGBdDXqqOT9hFjUYSXbP6JVKP1pzFHwwucBapHPIDAeuuDW7CxwvwcUD3ooLzwgkQleiHoJYdo3eTXTUM5h2RmgRPp86RzmYLwVnIfK410U4PY9x3gCwt0iJ5Xn7LpDJ3V_20v1-hI-JoG0aGQm0GK9QV8I5626SNnAgchkyGgUc6EcVGoBIOU_phLlmUjJxbWfKoFbq0CJnUEmighZpIQtLoJzw-PJwbVL-gVltlsp1sG53HjnLU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آسمون ایران کیر شده.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/81674" target="_blank">📅 12:36 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81673">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">بیشتر از همه دلم برا اونایی که دیشب رفتن بنزین زدن میسوزه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/81673" target="_blank">📅 12:14 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81672">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYiDfspamMquTAvyofuTs-zSrlFxqxzgKfOVOBu-IM7smvtDbuCSjz2_OXb_pmcx1rEpJvm0PH2UL-XI_DwqpnsvyreK-XXpcocoipMsuQzlI11CXhlPUP89DcNSlnnp_3LoGOvZcGgzbYAd3iT8hFq8hVjizwUMcO3MKFK3If8gHX14mGkBoqELHBNDbuDqXdrKUHNdFKkIdQJ65YnirimH389XrTdqLT-Avt99ac_LydagAx9HgAO3J_CXkrI2_Lf3eR_YSKKwTKARBl8Hi7qQXcTgNg0A8py4zlsNa3CG6HXYzr71eWHSkLhh_jlYA0cAdXfwBt9IoICymGJZGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عقبی اردلان این میما واسه سال ۹۷ بود
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81672" target="_blank">📅 11:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81671">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=cXlWJE3S_FGkkzrTEJXTZu5ouUo1UB4uA1pQrjaQBN0ARmJugiscbqsyP0zfAz_VBe6roKlIfa9O7GUNRLTbvMHCBq5OSsd17BqwnV6orvddSURB6m5H2JtPLDKqgk2I8lv8Ze-r5dCq3Y2OID6g2y3yiSh3ntEj4s4MUp1Y169dAmev4UEzriZqi8bKVw1Ces1eTg5oNBCdOnE4Q0n4Ru-gXlNGzY2RuPz6_aP5RMzsYnptVCKh55l4IovEIyFkc3RCjVnCg1BJMFYrNPJj77divwSc7aLcM1MTPxfRdbk8-6Q5ZcseJC4X_nmA5ItGESqh5wNrxaHnVTjTniw9uw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f01cb7d9.mp4?token=cXlWJE3S_FGkkzrTEJXTZu5ouUo1UB4uA1pQrjaQBN0ARmJugiscbqsyP0zfAz_VBe6roKlIfa9O7GUNRLTbvMHCBq5OSsd17BqwnV6orvddSURB6m5H2JtPLDKqgk2I8lv8Ze-r5dCq3Y2OID6g2y3yiSh3ntEj4s4MUp1Y169dAmev4UEzriZqi8bKVw1Ces1eTg5oNBCdOnE4Q0n4Ru-gXlNGzY2RuPz6_aP5RMzsYnptVCKh55l4IovEIyFkc3RCjVnCg1BJMFYrNPJj77divwSc7aLcM1MTPxfRdbk8-6Q5ZcseJC4X_nmA5ItGESqh5wNrxaHnVTjTniw9uw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صرفا جهت یادآوری
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81671" target="_blank">📅 11:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81670">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">المیادین: تعلیق حمله آمریکا به ایران پس از تلاش‌های جی‌دی ونس، معاون رئیس‌جمهور، و رئیس ستاد ارتش آمریکا برای منصرف کردن ترامپ از این کار صورت گرفت.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/funhiphop/81670" target="_blank">📅 10:55 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81669">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ewZZ1oWg5uZvVCfH7Dedbow0-UP_cUAMBE4XRJ-M5TmBhbFMkfvg1oPqqyTDm-YV4DjtJdmCdCuiUCn87OkollVsRUZlM-csdeYzIz0FtkqXJrbru7OQZZtxJBnJR5b77cTGfvpiE5QTLh49CfYon8aMzlJsHbScMd0nJqmR1rYY6Qm1ZNP7aJ2ssVtD3EX6OWhNezFPP-kh3Rc5wiQPAsf9-Z-GGZX8sr-Co5yVZ7cfgfC6YOM_oXRqBJQf9FMydWCQDQTS__bxwFGDDkJWG9cjzgh6xij9a3Kwh5Z4OrqXXwVF0MOls_128zoUk9ArYL0sKPshqbrtn5VvFi45Og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کوروش یه سینگل میخوای بدی اندازه تریپل آلبوم دریک داری براش مارکتینگ میکنی، بده دیگه گاییدی
پ.ن: کوروش این عکسو با یه تیکه از بیت آهنگ Fiancée پست کرده اینستاش
#اخبار_جنگ_شرمنده_بابت_پست_رپی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81669" target="_blank">📅 10:33 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81668">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">بخدا اگه این مارکو روبیو رئیس جمهور آمریکا بود الان یه جنگ جهانی رو شاخ دنیا بود</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81668" target="_blank">📅 09:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81667">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/81667" target="_blank">📅 09:47 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81666">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FD2yfEYHNxhwwDY6Uo5eLGe04nZIhEUPJTt5Y5_8PRpjYmTxC_YOBFINrkHWLdOIGI84wzwq4xZ8crj_oDTMvmXb8TQ6pSf4U8pE1YU0VOT9NlJiQmeytF0CvU47AMZaVlbXwwco66TliLI1Ubu3ZPSiDzFfE2INHeWiroWw7Dh3FZab1caM3d9STS1H7R0PH1jfznZKvZ-6td9NuTJuZBZgys8OYp9hTVRebbhLH7dDdZqbMdrjgp1LFjEQ6etqpKEYMwedrL9rxKp0gk52k5RU56ivTB39etc6rfJ7MwGSq8hoiaSgivBYzMPq4uEr3xiTrOs10fYUt4IaenMVFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#معذرت_بابت_پست_رپی
رک بگو میخوای باهاش فیت بدی دیگه این کارا چیه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/81666" target="_blank">📅 09:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81665">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">یهو یادم افتاد چند وقتیه براتون طهلیل و پیشبینی میلیون دلاری نکردم پس قطعا مشتاق و منتظرید: این هفته رو کامل قراره از ترامپ و باراک راوید و نظافت‌چی رویترز و میانجگر پاکستانی-بنگلادشی و راننده شخصی جی‌دی ونس اخبار پیشرفت مذاکرات و آتش‌بس بشنوید، این یه هفته…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81665" target="_blank">📅 07:25 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81664">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ftXIpts3im3ogPFfjlAJqAzTu1jBiUG8W-i2fKQ9N_xXl0RHrDoLfa3wv1jmf8a5PktaR1quiAzVRFX4T44AIRGJmVMOEeZAzJkbfHhOIlOcEWnR6GFVa1dUrM6X7aZoEIXr_j4L497D9qRBCKnBYF_vWrTO-jYfVPkUAsk7ukHHRSWhSzJZj4dpsx77bHi53R906RTwFZVaDHAImsjm7VsZHBHjvkL5AiSueeYME62UFqzd5OMfyxYrUivwOFr3ayT7t59-sv80zhqLtoWx2PBrJPb5ma2hfdSOd9kWDisfh_cZH46dBUReX-sDWgXD_1eO2FgAuie594zUL8HC8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
🤣
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/81664" target="_blank">📅 06:08 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81663">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">چتایی که از ملتفت پخش شده همشون فیکه و تو ویس و ویدیو هاشونم که چیز خاصی نبوده جز ی سری حرفای جمع های خودمونی و شخصی.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/funhiphop/81663" target="_blank">📅 02:51 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81662">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">امشب بنزین بزنیم یا زوده؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81662" target="_blank">📅 01:58 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81660">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=fGMGcG0wPAxfHNZtJajjFjyszrabaaeM7CD_qJu1hgRUo4IXauiAjQ_OswvNF1FPTw62YG6EuY2MlHw9CPOz-ByWXf0OhgW32SjhdzaLp0b-pWJo6PGfC5CiCazNCEFGFEmmAwQFnUL1D-xljFwaWrftGGxfrAZczxgHwoGSgXTlaInDG1HrV8MhhEVHDoBFlu5dRWAla5xFZ2TZ8WQz_GRNVGlOMekEuIkmeaG1AVgMC2TltLfnXMJFm9eX6yIlDClmXA-BmmlBeXV_ha_E_gkiTa5wYU5cZUAIfCeayu-NFmq6cIXYo1Cmk4g8TKgB-4zzVa0mBRvQLP8FIZGIbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce55f6098a.mp4?token=fGMGcG0wPAxfHNZtJajjFjyszrabaaeM7CD_qJu1hgRUo4IXauiAjQ_OswvNF1FPTw62YG6EuY2MlHw9CPOz-ByWXf0OhgW32SjhdzaLp0b-pWJo6PGfC5CiCazNCEFGFEmmAwQFnUL1D-xljFwaWrftGGxfrAZczxgHwoGSgXTlaInDG1HrV8MhhEVHDoBFlu5dRWAla5xFZ2TZ8WQz_GRNVGlOMekEuIkmeaG1AVgMC2TltLfnXMJFm9eX6yIlDClmXA-BmmlBeXV_ha_E_gkiTa5wYU5cZUAIfCeayu-NFmq6cIXYo1Cmk4g8TKgB-4zzVa0mBRvQLP8FIZGIbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فدایی حتی به لوله آبم رحم نکرد، وصلش کرد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/funhiphop/81660" target="_blank">📅 01:10 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81658">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dgl8Llc1YI22cuQEjEBACRssfCFcP4q-fpApZxeEPG7GhnRLAIRPASDoo8ucE9NjLOdgmmjtylGpJIQio9JJppOOn-DU4Da0IsZgkgHqZ6Z_YfHWmD8E78GbK8auYaDtFXP_jDXrGnPD4aE_psDgnI-Frr_T-CaeW8VPtLLaeZEJtVOx_eJPJRE7NMWsWiJmwhAu85XI6bl_gs5X2C5qnjcgjQIwHPWyo9WuHqYUwIXV19UbQakRF6viCkAldJM58SCEymLeBScpfTw64Wj5dek7k37INWpV2ruq1xG2ggTcanKIc_zn_DJA7rppukAJYwvGP9QgdG6Ye2XVwJ4ziw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b27da425db.mov?token=Dgl8Llc1YI22cuQEjEBACRssfCFcP4q-fpApZxeEPG7GhnRLAIRPASDoo8ucE9NjLOdgmmjtylGpJIQio9JJppOOn-DU4Da0IsZgkgHqZ6Z_YfHWmD8E78GbK8auYaDtFXP_jDXrGnPD4aE_psDgnI-Frr_T-CaeW8VPtLLaeZEJtVOx_eJPJRE7NMWsWiJmwhAu85XI6bl_gs5X2C5qnjcgjQIwHPWyo9WuHqYUwIXV19UbQakRF6viCkAldJM58SCEymLeBScpfTw64Wj5dek7k37INWpV2ruq1xG2ggTcanKIc_zn_DJA7rppukAJYwvGP9QgdG6Ye2XVwJ4ziw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویسای منتسب به اعضای ملتفت(تایید و تکذیب نمیشه)
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81658" target="_blank">📅 01:01 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81657">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/81657" target="_blank">📅 00:52 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81656">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">یه بیکاری اومده چند تا شات و ویدیو از چت اعضای ملتفت پخش کرده که نمیدونم واقعیه یا نه چند تاشو میزارم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81656" target="_blank">📅 00:49 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81654">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/wBFeTWYPWdN85lchDT3lqKB_QvPyUqnrDPGz6PA9S6ItaV0o7_JUGS0aj20eT5doGeBLbvsUPpvt_6-JVQpIfJMP6z61FEF2F0htZwkCEZa9GN4TVE8oRsdqqqKMsfak9gG3yXMBp5rGqX-xJ2KT4O2CWoySWDb4m9Gc7YGVR70ZTYY7jnlUeMpSUencyMfEG-346uUicFXj-JS_gNu856gv8NRdZVhDArhCcjOqDKhYs2focTzOTTf-HSMXnNiU8g_RdaS--vsMYRbEGrHUpRaumDh3ZVdt_frPZVv3r0eF873tAxSaSsm6ryCmKcHo9TQP6NF9EUliZnSWsJyZGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ox5YOeZkDMuvKOcvtZuQTvxXStxuX-q5Mk18qqLtFEYlPkCquQpzg4cNzYJi6VldA1lhxN_V3gdrvy8n-AntLWpiOv4z6eaa2o3Yn6F4pRHEPOur1Flx5sYQwxBwC4zM_BMClNnMy9s3xRaUCYVc4yWQK71tcoIdq-opMYCzBsrsWGlpG0IEeFpfFSgoeMkHBOFX0TjSsv6Pne39LL1_Keup8qrWyOXVw2LIk16nyQVLOhPJoiTb0yyXaJR3EVvre_43092GFqNc-U8vM9OoNkOJ4D4dCbrdP3yeAvroagTv5X7lmpZYXAZDsmE4_OXhnsD-I0Th3RsGCFMBAO3mqw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید مهدیار و شاپور
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81654" target="_blank">📅 00:45 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81653">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/funhiphop/81653" target="_blank">📅 00:31 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81652">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">ساعات پیش عراقچی با وزیر خارجه ترکیه، و عاصم منیر تلفنی صحبت کردن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81652" target="_blank">📅 00:29 · 11 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81651">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">زدن زیرساخت های نفتی و برقی برای امریکا و اسرائیل کار خاصی نداره
پس چرا عملیات رو شروع نمیکنن؟
چون منتظرن مقاماتی که هدف هستند در دسترس قرار بگیرند
اون موقع عملیات بزرگ شروع میشه
دقیقا عین ۹ اسفند‌ ۱۴۰۴
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/funhiphop/81651" target="_blank">📅 23:20 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81650">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C9Uzvzs-9OB1Ie2LzX-wMOLQuKK9gj5MIAdcubEDFiXxm1iIvyhvzTtxGE1NHbcoN6N5xl6dpG23hf5IVtX0aqlT556QCmkd0AHF8yxgCTxFJD5MvQmr8Q9x90WNrHz2GKMEsy5vzYtIbFRa5PpV56-iSEARM7tZKyaqK26oUmpziqx7kIlhfJmDTAG3Jagcsg3ZlzuRCnOywl8VX9XqAgRgbRsLJSi4EhFJVK395MObPEZZZenNWdugzPzbL9BBByH1XIiMnTBwDFJ5VL6og-Lbpi2RRsTdLkjpo2zc3ptVVvVls5f2ufofkSVcKXdfbIRsctm5Ej9rkl5e9gWU-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پست جدید اکانت رسمی مرتبط با وزارت دفاع آمریکا
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/81650" target="_blank">📅 23:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81649">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">چرا کسی از من درخواست نمیکنه خاورمیانه رو ترک کنم.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81649" target="_blank">📅 23:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81643">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RQ_1fMik1XiSQ-AKeIBcmyHeR3qJRj98ltooMIYWVpGZI5fJ89xS9ovrtJK6qvJ13d_qYpOcwRdm1ZrqcscDhnHE4vLI_eNhn66tB_6g-LJCfshaYMuCo9ug1ovpWi9whGMNxa_-Q7jGsMeHZAFzzsR79_-yx55dsEa8DZK5a8-aJebCnZPvIoRLJxTLfAEO-rTAVvwH-fAvZRoVJblXG1IJsuXiQD46IwpQm3R5omBQFoUEmQxSsdG-yC7Gy-UAydxyBKzbj0NbGA9mGmJWXUJ_VVxajuFDfHmHlIRA4XOEwd3FFt8XwAaUNntuD3XjC1vmjRYqN7jKJtjMIAOKaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MpYj40UzT22ZFHYXyqrQVKEk4hTYsUUY0LtcA5L0ORYIFzeBL7WqQTDF_Rs-6FDW1bUcDQtvNkqzkscwDsQ4kGl8m-2ZLzoHAG_9Is5u4gPTrkN8ORKEXd0ujkD5B91Kxc4gdnJcVK27SrV7lcjpbcSSUgN4gLI3dC516y5amjjfLRrS6LyZN0SesNjK7FZJLZmlw_i7vkSnEF1TJrSq1806C8O-ATDus1iYSbypwCXj3VnBsk8xFab_LbpAN2OLmhBo-PhVi_hHp_YNNsPdSaz6jcq7MVuZBqNbvoX-amhWHIZgPmd7iifc-dgFIeZwn4XJk0Aidpn9GDRmR90ERw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iq5q0EI72e6M0tmp-X6HWOEzsgluDo5hC8LVTseKk72K-vYV5mHiWqIZEX3retZH7URHtiFciAimVC6axmNukX7XBQ0wmSclDb9KRY9FasBuCact8SaoyBAC-HqvLk2a2-i4RIA5OKd7WwFCZnkuQa4LLK1xs0HD2t-yPXK4zxUjQayjzWAyS9-wLZl9qoQL5DYwGvTWu4V75eT1BwyfalMugqYu9_mD0nygRBmh-cyEqc2CDJSYiYoRsKkQ65TTDge1ylym7muAJefTabNKnInIUCwMWuGuYXWJGaiCzryEIksDVj5Wbkez-EyHkxxsZk5_k1jNsU_D_eI2UppUAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uSsinGnIxTa3mIXEinqLdFrE3rNV7MUVTQo9pIsdiZzQePH0Joy-vcDX8mDlvGv7AGQBJ7rOgagMwJsQ_vM7PeVboxotFWYKKbElQ7kMZRfXXco5kRAOLbEiAjJBRBUYJWNCmbtxA23a_yh1gU8FBdcgMN1jpm-hGFfnB8TVvhco2eu0Knwc_0DyLNIdApFGDHwCCVipzWjNEeT6qeBAtS8g-_g4vL6xdnkJXTalREcDzGfFoRvFwVv1Og66839MzN8PkNkQhgToVCO8Tlen2GqbfiOAyNTuSizxBmlDa8D7HEfWWVQyK9TxhCX0dqTULGBI6dP0820yyooeVE4xCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C-B2YzMwmWNXV1mfqXWDVlxRAKx74M7qWjINDMhadcGJUcYK3qtw99YqlmY4FSGANbcXefdb5j2EODsALEA9HAf8y5Jwh5n9kPCP4W15pokcEKMuYFhfZHSx6zk2g5BVeKRBxfNggRCnSWbxtdJ9DNlzZU_lQvEeZMFlu15P5UZ4r73EAE5Uh3uu0z_IuumC6VWeaUQ7THirFiHYQEQQJi0rz_MoqDYXxpGRYK_A_1VjKJBZFKNOt6i5777s5aykZc2m_Bik6tbfmcaVPsz_xqPqgS7IEmoG8gQVuJqcM--tzsUVc7guiahvPnNLPcAZ3FH-xL1hDhq9p5gbTyA7Iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">تنها فرق شوهر عموی من با ترامپ اینه که شوهر عموم، بزرگترین اقتصاد دنیا و جهت حرکت تقریبا کل اتفاقات جهان زیر دستش نیست و بلد هم نیست تو نیم ساعت 37 تا کصشعر ai پست کنه.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/81643" target="_blank">📅 22:45 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81642">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">#پست_دارای_محتوای_رپی
سپهر خلسه:
نیلو یعنی عشق؛ شایعه طلاق و خیانت درست نکنید.
✋🏿
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/funhiphop/81642" target="_blank">📅 22:33 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81641">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81641" target="_blank">📅 22:16 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81640">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">خلسه چه خفن شده</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81640" target="_blank">📅 22:15 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81639">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">این سری، این سری دیگه قطعا میزنن
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81639" target="_blank">📅 21:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81638">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">کانال ۱۲ اسرائیل:
تخمین‌ها حاکی است که آمریکا یک حمله قوی علیه ایران انجام خواهد داد، بدون مشارکت اسرائیل.
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81638" target="_blank">📅 21:12 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81637">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">لیست اخباری که رسانه‌های رژیم غاصب صهیونیستی تو یکی دو ساعت اخیر روش مانوور دادن:
کانال 13 اسرائیل:
به گفته مقامات ارشد، انتظار می‌رود ترامپ دستوری برای از سرگیری درگیری‌ها صادر کند، و این، ساعات آینده را "بسیار حساس" می‌کند.
کانال ۱۲ اسرائیل:
یک مسئول اسرائیلی اعلام کرد که ایالات متحده از هر زمان دیگری به آغاز مجدد جنگ با ایران نزدیک‌تر است.
نیروی هوایی، سازمان‌های اطلاعاتی و بخش‌های مربوطه در ارتش اسرائیل در حالت آماده‌باش بسیار بالایی قرار دارند.
انتظار می‌رود که هرگونه حمله جدی به ایران، اسرائیل را وارد این درگیری کند.
مقامات اسرائیلی معتقدند که ایران ممکن است در واکنش به این حملات، موشک‌های بالستیک را به سمت اسرائیل شلیک کند.
یدیعوت آحرونوت:
نیروی هوایی، آمادگی سامانه‌های پدافند هوایی را افزایش می‌دهد؛ سطح آمادگی در نیروی هوایی، بخش اطلاعات نظامی و سایر بخش‌های مرتبط در ارتش اسرائیل به شدت افزایش یافته است.
خبرگزاری والا اسرائیل:
در ساعات اخیر، تمریناتی شبیه‌سازی کننده شرایط اضطراری با حضور یگان‌هایی از آمان (سازمان اطلاعات نظامی اسرائیل) و نیروی هوایی برگزار شد.
کانال 15 اسرائیل:
برآورد فعلی این است که اگر ایالات متحده به ایران حمله کند، "اسرائیل" مورد حمله ایران قرار خواهد گرفت و مجبور خواهد شد وارد جنگ شود.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81637" target="_blank">📅 21:06 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81636">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eK3BCq09E8CJsUEJk5fHrLSa7HY7jd0Fsqm2ioG1byhxQgAbvCDrtPKPslFTuncNA7xLe1XWFOSwk15NT2ZwCnNhikXBKlvKnZ1BfDeDwh8grwsGDxjkNPiVD9937gFEnA4liGh61xTtOdiIcvKsv0t_8PJXdyH2zWYzZ1Fd3-jxtXL1RvYHCXYUktnH0AkYElif6u2Lv8p4nzvlHTZINwkk5cZ6C3GyAqoRUi9E9WwvXXg1tt5BefbV9X3idVqRjuFTGfGhaCHvHbCdA5XOvPZG63aFkcGsTFZkbC8larDaCKb2lsIzWr633tA4gJAutuBRg4I3QToIZsvHuCMDow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چنلای ایرانی یه جوری این توییت رو با دوازده تا ایموجی آژیر و پنج بار فوری گفتن پوشش می‌دن که انگار انتظار داشتن کاخ سفید بیاد این ویدیو از دیدار امروز سربازای آمریکا با ترامپ رو بذاره بهشون ناموسی بده.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81636" target="_blank">📅 20:38 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81635">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BDxa9eJYiHjt42LOCRhelH-zV4zWglt83wfD5tZYx_M7CjNnK9akaBuW1uDfuet-4ev1TRTqV-mF2Fsw-pfGwTHTPKe9-IhVVvN3Qe38pNKxbvCVEnPEU55J24u3feOcCEKf3oQssdCyh2lKzpjO5jrzwkzXGYJj2YMZiAPCyxqiq9BcGXggtmbHsyKXXdGuSawpAM8WWRY8ZvNj9_T8Lzy6a2GgO_wdnU2Cml3s_8WhVAhLoalMnFrXrXozEjAB0WDPOF0b5HNM5kQFjy3J7CXMNXa3RIMVO5-a9R61TWQlL7emtdPLGYhpjM4odBEYw7xSSv9iT-4hQmUgMltK4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تنها کسی که باور کرده ایران ابرقدرته نویسنده های این سریالن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/81635" target="_blank">📅 20:26 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81633">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗽𝗲𝘅 𝗦𝘁𝗼𝗿𝗲</strong></div>
<div class="tg-text">🍃
به فروشگاه ما خوش اومدی
🍃
اینجا هر محصول مجازی‌ای که بخوای پیدا میشه
💰
〰️
محصولات فروشگاه
〰️
⏺
انواع آیتم و ارز بازی‌ها
Ⓜ️
😶
🎮
⏺
هاست, دامنه, سرور
💻
🐧
⏺
استارز و پریمیوم تلگرام
⭐️
✉️
⏺
اشتراک سرویس‌های پریمیوم
📹
🤖
🎵
⏺
فیلترشکن‌های پرسرعت و پایدار
🏳
📱
🏳️
🌳
قیمت مناسب و تخفیف‌های دوره‌ای
🥢
اعتماد شما ارزشمندترین سرمایه ماست و رضایت شما، مهم‌ترین هدف ما.
از همراهی شما سپاسگزاریم.
🌹
Channel
▫️
Apex Store
📣
Bot
▫️
Apex Store Bot
🤖</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81633" target="_blank">📅 20:04 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81632">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QUbzGxtUiq9dnPWep0Q596OoQSJn7okzkQQq8rjhO2U8iY9itbCK-KZRlozR8ZKZWFxwbJ7saLg5TpZ20C0Fwa-Hyuf1fVYRZgVZGlzG-gMddm_0kQ7HsO5L-Lp4xx7QC-0t4oBKvLnjF17wzcGUMQb2GdyNdJI0eNou9RyVI7rhANpG6swUn7g5BwrZrzlrJGh-0pfSv9ZhGvwnUGkXxxWEP-QeZJqt4WxqliV8aNEzCm2ZuGiWS8VrpN6pidet7gLmFsMz2rUNePkpHW1x9Fo0Lw8-S3DxlLvLivBN1bDzzKCAOtplxXnnQZFpVPXbFU3zHJFjJoqju0HwVY-Vpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زمانی که این بویان کصکش اومد بالا مسی خودش ۲۲.۳ سالش بود، بعد میگفتن جانشین مسیه، درحالی که کلا ۳.۴ سال فاصله سنی داشتن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81632" target="_blank">📅 19:29 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81631">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/F2GvPgE7tgk71ZKCbGtHddecK5OrGGLXKF1KI8MQGIEtFaWAuLJOS8XvokxMcpKsSO3JlPThYsXEj3dNFsD6M_2lUgbx9baumab-l880uBHxVAnv_kBpraxE6UOca9jIGBkW3nqrMbb-CmlbH39iGXOBdyDrItvm7tCgQtFSlEkm2NFRXog7MIJjdhzT191LB0rzrkkc2on_ZXp4Kh5Y7zB204Ki_h8tdk0GesGSkzmi4kXXBa9VB4XPiRdRXjOFJqjYlsL0YXJYIVJVNfH8Kg304bgxRgZmlGnPEqXOxX8bzta5e0mv5pwB_QW6weHGufHEZs2KlTe0bOdRIE8K-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این مرده که توی سریال کلید اسرار که قبلا از شبکه سه پخش میشد میومد پند میداد و همه میگفتن چه انسان شریفیه رو یادتونه؟ الان رفته پورن استار شده و بعدشم عضو یه گروه تروریستی به اسم FETO شده و تحت تعقیب پلیس ترکیه هم هست و برای بازداشتش ۵۰۰ هزار دلار جایزه گذاشتن‌.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/81631" target="_blank">📅 19:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81630">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">رسانه های نزدیک به سپاه: اگه زیرساخت های ما رو بزنن؛ کابل های فیبر نوری در تنگه هرمز رو قطع میکنیم تا اینترنت کل جهان قطع شه.
پ‌ن: مشکلشون با اینترنت فقط داخلی نیست انگار، جهانیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/81630" target="_blank">📅 17:59 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81628">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Og1s7-F0PTuQ8GmvCFg3lrFXTXj92qr2k2D8yLgAjjZB2ErJ4aycYJ3MK0yWcrH0ViQ-1b3XDUMzjG8Y4W5l_tOexSpmPAQtiehXPgVHpth4SuBIlfWolS02u6eTlCuMYcNBwQt5Cy1H9g50TzsG1CoNVIRcl4CsoYp48h1LUoTS4qNo1h1a2v3RBGNohwqkOHdnyQvzAfOltFfnGw0hiyxF-m-6WvN6SFO4IWS6dPFLSlYu4NApFKcPrT7B8R92zH8d62WoMdqoqnUbPaVDRghIC0ziH7_C645EaqOqyxewhPfnZJh11xmz-vMQ85yt-cjFwvm_pgbCCqM_JET83w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=bHN7P0wjsfeetitNndTnMdO-uBNYtnIcgQwFvHkEb5UyVJp2aVm64xmmNR4ZwWC62-_oum2C7jIT3Ay8pdjMNOP-p6HecHh26fdW8cjbOu07CreM11J8k9Qfpr1AIgTfE3xwLcsLxtR7AFZtiJ4enrUxcjMLL8_p4zEsv2QtiLPoEtmzGJvaZ0tZVCjrYef0d4b1c226_8t43Y-5GiAXR_OnFiGAgifnDyqzwGwhqj3398mEagcfcll3s2adk19SIxadRU_77d8UUU85WupeIeIRV0LkAYK8Rw5jgTFB0BSZ6ajYUpa2Ob_UBiNs7dS446GsxLSFa469SZWtBgIb5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0bf99c7d1.mp4?token=bHN7P0wjsfeetitNndTnMdO-uBNYtnIcgQwFvHkEb5UyVJp2aVm64xmmNR4ZwWC62-_oum2C7jIT3Ay8pdjMNOP-p6HecHh26fdW8cjbOu07CreM11J8k9Qfpr1AIgTfE3xwLcsLxtR7AFZtiJ4enrUxcjMLL8_p4zEsv2QtiLPoEtmzGJvaZ0tZVCjrYef0d4b1c226_8t43Y-5GiAXR_OnFiGAgifnDyqzwGwhqj3398mEagcfcll3s2adk19SIxadRU_77d8UUU85WupeIeIRV0LkAYK8Rw5jgTFB0BSZ6ajYUpa2Ob_UBiNs7dS446GsxLSFa469SZWtBgIb5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو جدید سیدنی سوئینی برای برند لباس زیر خودش
.
پ‌ن: برا آخرین بار ببینید که نت قطع شه دیگه تا چندماه خبری ازش نیست.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/funhiphop/81628" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81627">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aifxFtx5-1r6kvm0g_KxVxxzrGUANhrcmvPCSILN-Ttba2OmWuoJsb8lHWrJywRWW0TBnNzVOoRujB2ASK2B4QJMnOmJny3IZ8SH0fx-MJcFpapjhqHbdZIMQl9u0iiCftkRx2ttno4dvCL37HCoeT9NcPU62I3swgLy1R9-DKX-jN6Gn9h2NXS-BKoRyM-HdpTPGSKyTwT8mYrHMgG_D4jINJcNtNwqLXcoDGqwuPad9r-rTUzYiGN80C-AfEKQzIpioH8cic_RmXVks2RglklK069tZxPR2n5eWHxrvQUikTbyUZGSouhBDAwePRQOMukBMIM2Hpp_QB25NmY7bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
g10
💻
@BetForward</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/81627" target="_blank">📅 17:48 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81626">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">انتقال لجستیکی آمریکا به خاورمیانه تقریبا تکمیل شده، الان دیگه همچیز به ترامپ بستگی داره که دستور حمله رو بده یا نه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/81626" target="_blank">📅 17:42 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81625">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MpnlU24FpEm7neNgOGxpfkk_fOt2TSkjZvxVGUpkPUgqX10XQAtlWjgMpf5T-aLO9namCQ1IpDQfJTL1W1YgNXMtT_SF7eCxf13jfsE-T3ZRz5ECFyt9vRANspHEqLbVG6pVfpaCWWZ7R3DkmPCv98rsGLPJsG20JT7SQNRFyR1uJgcT87ZKqwefQNJ1bHsT8vJ3VVzh6EmzuSlxrJKitnrA_VHSuBlsLLIwDo3p_F_WXJOHp86yN4jieW5uDkCr4FfUbqywWh-W2288ol8gE3c240aGXqZI3wS_S2WUH7V6npPRYq-QJAumDmtcODWYdPpTNweDG2nGfASTz1CFdg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصویری از تانک‌های T-72 لشکر زرهی ۹۲ ارتش جمهوری اسلامی در حال حرکت به سمت آبادان و مرز خوزستان با عراق
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81625" target="_blank">📅 17:25 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81624">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">امروز صبح آروین خیرخواه یک زندانی دیگر اعدام شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/81624" target="_blank">📅 17:14 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81623">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">اول جنگ ارتش یه سوخو 24 فرستاد العدید قطر رو بزنه که منهدمش کردن و تازگیا جسد یکی از خلبانا پیدا شد و برگردوندن کشور.
ارتش گفته این ماموریت 4 نفره بوده و همچنان اون 3 خلبان دیگه مفقودن و دنبالشونیم
منبعشم نمیدونم کپی پیست کردم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/81623" target="_blank">📅 17:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81622">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XpyaCsAjF_8ePhhWK0gsNh_ilk8OSxo2DB_wGthP5wKrQj-rtChn9JHOqBqplwMJiEdzWl8RKgE7uMqg6OeJsOPtxgNBT_CTFpId7nFMouM5b_Kiaqrj_x_GsgG-254zvCldpYE3_Z99FaCkRIcjdsW1rOIe8bW9RWScP0GAFPjHXuYcONj2bh8hoqA3OikI_mCirv9oh0wloVcPfUXnPAryoVXMssaQjIn0cAsb9eINywk-n6sQj0V8p9hTuWbxbo2qhsvE-QLtGk2S9Kgdwm2FQk6Bxe5AU40vc4IKm8yzsLr25tvAfBpFsMNU3eMZ3WhzTj1PFg9Wm_wJiiTzIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بابا کمتر پورن نگاه کنید، مغزتون گاییده شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/funhiphop/81622" target="_blank">📅 16:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81621">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">سی‌بی‌اس :
ایالات متحده در حال برنامه‌ریزی برای قطع کامل برق در سراسر تهران است
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/81621" target="_blank">📅 16:32 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81620">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ep1xMBQRDOvkX67r__n2-0qS15y3JyRUxC1lU_4pBvKO0SY4qu32wEfkEj1w-sqo72RFZzy5WcswJWtMNjMs8jHIdGaYukegtx5DFJSkJU3rmbEViR_fsYEwkGB-NFAjHvg-MH30U8eJxoU3MMep0vG4zELYKi9iDOC3pt1CKtWVjEIin6V0epW0DNO3kwdFFtuUYIvtXJpWBB5ASCiL8xl4kEKTbacSkMkaSG2fESEEVPiBbOAJzgFYAk6xvgY0xm4VCZcRvAwCi5ic4rsrg25uptHCOGd9bmRhVOT0SIzvCbOeJP743Qoy2oIPMzRMQjgQ1b3bGIts34QMfakMOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داش چارتا چیز که ندیدیم پیشنهاد بده
اینو بابابزرگ خدابیامرز منم تمومش کرده</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81620" target="_blank">📅 16:23 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81619">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wyko0TYfeVOl5ABN8Cwn4fH4y40rRyc0PNArWVIvt4H4LhbPEh1potTATy178TPqouoX0cDc89anJSKQDN28SZYWBEkp18vDertDMQJLQdYrnEnNfit-MidjDgKTcrlmHpawheyvV9eW8tUl8OPbhlA4RCFEkbAQe7ANpEFWC6zTgErvtG1S5Wa46uw9lHmo33l5WlM16KMCVlWRNHmGCw3z3ZGkJb5E21IAZnkPR79y1D-v0Enz5bdZBH7MMXNU96q6KFGrYdF4NKlQSdP6FLaRd3UaToAZq80C1qRgPx_UGtYEY80dlloCuThSs7MthhURLaw7OyZ-Jxf_FKWa7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آب دستتونه بزارید زمین برید این سریالو ببینید.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/81619" target="_blank">📅 16:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81618">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mN4WChilZDYJa8h9SuyB5OVwq94IIPpaZj7OTQZomxAwRvsZIPX2ALAD8CbgWQ6PrRgMfVPUn7Iy8pZSrKhzh4F7oogM_AFzuDH6OJuJwAcYGFqIIeh2srQkKs0xF3d1XhFDLi7fGCwF1085pNuFMGWsJo_Y5pIyBK735QV9ejOG_4EnpadlrchxNerr3GiMMQdhlh6_h0CjYE-mA0YPBTIQgNOk-Sw9SWyZ7Hb3JGpcsGVuS8vsW6Q8v8pLssJMI2jXA-GZGlt0pqi_H3DXOyqcV4rQ4Cvyx7DKt_KYHLtUnjOlFj28CEn9YKMoywCtRXps_rryXLn0t4jo3txd4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نگار جواهریان جدی معتاد شد فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81618" target="_blank">📅 15:43 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81617">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/07811532ee.mp4?token=pT2VkeJaMKBOo4AtOQedq2aZqgGsURQkXoj9KJK2QmfK-0MbwNMk06UjeCv3rQVxBqBTcnNmxb4vlUI2Qh-rAKGr7tFaTy_nkjRZdgpVjEmcIrW4znc0OA-bylYQL7TvhCj78ZgIM-QeZv-vjmDPnk9JFY3aBVWOQMYshVlltiz_vhCri9ZiID8rSGyghrWzUNm6ZpuS0EIqr2hLishpmtG7Zqclq8ywOXja2TV_HRjMJMs2Q0S3hXoypYz3yPZRCWRKdKTuKrMwuV5JZ4FLNK8eReE6y8RZ59p-V0mnGUThI2zz4bd_NQCq1ZeA17T3iRpP2klhHea5a8wKuvKfZw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/07811532ee.mp4?token=pT2VkeJaMKBOo4AtOQedq2aZqgGsURQkXoj9KJK2QmfK-0MbwNMk06UjeCv3rQVxBqBTcnNmxb4vlUI2Qh-rAKGr7tFaTy_nkjRZdgpVjEmcIrW4znc0OA-bylYQL7TvhCj78ZgIM-QeZv-vjmDPnk9JFY3aBVWOQMYshVlltiz_vhCri9ZiID8rSGyghrWzUNm6ZpuS0EIqr2hLishpmtG7Zqclq8ywOXja2TV_HRjMJMs2Q0S3hXoypYz3yPZRCWRKdKTuKrMwuV5JZ4FLNK8eReE6y8RZ59p-V0mnGUThI2zz4bd_NQCq1ZeA17T3iRpP2klhHea5a8wKuvKfZw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اسپید به مناسبت ۶۰ میلیونی‌شدن یوتوبش داشت با بادکنک پرواز می‌کرد تا انیمیشن محبوبش یعنی Up 2009 رو بازسازی کنه ولی یهو بادکنکا ترکیدن و با کون سقوط کرد
.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81617" target="_blank">📅 14:27 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81616">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده  @FunHipHop | چمن در خاک</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81616" target="_blank">📅 14:18 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81615">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">غرب کرمانشاه یجارو زدن انگار صدای انفجار شنیده شده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81615" target="_blank">📅 13:51 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81614">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=iSTpwaMyIfcJgZPjNkNlNhdsSfU-k3HKgGzL64rYA_B1dejabebdiEEJSLS740w6dml1AvE528lBEPdSFMbsQOwHRX-ZoCaxP6-F-e5hOWNDeR57fus9cfpAAchrcgs6hSHKMLEWdsRIvKiT3T9h6pyrC5gCfFO4VWsa7vo1Fv7wpnBmyS9Cdvvgoqvi1d5e-dwHIHnm_ulfkmwTgLE3gb0k8bfpRVvVO0AZPZw9MJ5SqmnuiyXQlq5ee9Ckf_gqRB2eq580oc3xFsHck5sGpr-5dRG9dwTA1gw_vobAYdGJCl6NcKddDzkRXsILE9JYBVdDKtfYn-pDSdPuzLHpTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e859712cf3.mp4?token=iSTpwaMyIfcJgZPjNkNlNhdsSfU-k3HKgGzL64rYA_B1dejabebdiEEJSLS740w6dml1AvE528lBEPdSFMbsQOwHRX-ZoCaxP6-F-e5hOWNDeR57fus9cfpAAchrcgs6hSHKMLEWdsRIvKiT3T9h6pyrC5gCfFO4VWsa7vo1Fv7wpnBmyS9Cdvvgoqvi1d5e-dwHIHnm_ulfkmwTgLE3gb0k8bfpRVvVO0AZPZw9MJ5SqmnuiyXQlq5ee9Ckf_gqRB2eq580oc3xFsHck5sGpr-5dRG9dwTA1gw_vobAYdGJCl6NcKddDzkRXsILE9JYBVdDKtfYn-pDSdPuzLHpTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا همه با ورس شاهین نجفی دابسمش میرن، پس عرفان بدبخت چی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/funhiphop/81614" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81613">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kQ9nqr2XZtny7OyqWdlsdOG_vYAG_whO8O-jbBpfnu7DLTes84PQTEC4u7s5Ry4yU46jKVH97aFgT2K8XeI5wvxKrMFeIGyZO77HI_Y960hAVBPBBVv5nGq1iiRxrejW_0NvvkSkIdE-HGGltoYGxRHhe5FXkAV_20KBcafWiZD2WfD-i9D4fESnHi4HtC0UhbWpAnQE7eDMfsmNDsS0gW4BfghRzlCuiyBLDOJfR4iuVRsPK8Wtq-4OcBFiYanZb9ilb6ghXn4WkJkK-IS-Vz_oNAUag2voR0jMf9V0Wr3Sevk8EBTw0kR08wg5txUzvy7rW_KX19kIY0p5iK1_zw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎮
آموزش حرفه‌ای بازی‌های کازینویی در یوتیوب بت‌فوروارد
🎲
⏩
اگر به یادگیری بازی‌های کازینویی علاقه‌مند هستید، آموزش‌های اختصاصی و حرفه‌ای بت‌فوروارد را از دست ندهید. در کانال رسمی یوتیوب بت‌فوروارد، نحوه انجام بازی‌های محبوبی مانند انفجار، پوکر تگزاس هولدم، سیک‌بو، دراگون تایگر، پاسور و چندین بازی جذاب دیگر را به‌صورت ساده و کاربردی یاد می‌گیرید.
👍
در این آموزش‌ها با قوانین، روند بازی، نکات مهم و روش‌های مدیریت سرمایه بهتر بازی آشنا خواهید شد تا با شناخت بیشتری وارد هر رقابت شوید.
📲
همین حالا به یوتیوب بت‌فوروارد سر بزنید و آموزش بازی موردعلاقه‌تان را تماشا کنید.
👍
ورود به یوتیوب بت‌فوروارد
کلیک کنید
BetForward_Official
کلیک کنید
BetForward_Official
🅰
r10
💻
@BetForward</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/81613" target="_blank">📅 13:47 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81612">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">پدرو سانچز، نخست وزیر اسپانیا رسما به گوه خوردن افتاده و خواستار یک جلسه اضطراری با کشور های اتحادیه اروپا در خصوص بحران به وجود اومده توسط مسلمون های غیر قانونی شده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/funhiphop/81612" target="_blank">📅 12:00 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81611">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VLYz_rAX-DPxqwdHhYpHTjkAKY-Iv31tVXeXdNRvcb-8W6KR0ZLL4XdF4lRU4YDlYWXVMe2CZatSp-NCJaWs3gk0tfx0FYBavC5w7O7MgDMAObhxc9KzKzE84cIgJ5NszsiUuQsN3lLAvyaWXQnSsiyhwgHTAIJGMiM-BHEvWV9dEvoaw0wNy-0B2v-tm-FSSoLnbCCvJXwcT9UmY_iVBgGqj-7VIKCpW3tAxQUOF78ibblNRQL47Dcl2zE9rEMM8beFTLmvUQd1B7bquVJ3E8cwGXY1GDCn7Y0y7LGS8JnWs3zo-MP0V1H411vqTyW_6stBPna4sRGd08s-LRdNLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تورو خدا به این بی ظرفیت چیزی نگید از این به بعد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/81611" target="_blank">📅 11:52 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81610">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">امتحاناتون بالاخره تموم شد، چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/funhiphop/81610" target="_blank">📅 11:35 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81609">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مثکه به دیتاسنترا اماده باش دادن وقتی جنگ شروع شد سریع نتو ببندن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/funhiphop/81609" target="_blank">📅 01:54 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81608">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">راستی وارد شنبه که شدیم بازار های جهانی هم بسته شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/81608" target="_blank">📅 01:50 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81607">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=K2hq-0EJeWZolad-RDvvtgTEJ5gf45uAyGkL9fZ0u-_cmv1SEHB1Aqx6APVWiaipewW-atoSmRfa2nWehxQDEkRN0cSUxHOQ2zzy_kRIl0l14U-Uc3GB6aV2Bq8uZYfiSV_RbAFIh4a9qJvZrOxc3GEe8-qKw1DEa5RlfnCYXOqaVN9XIIdJBGGwgE4mKfJYrF95gaRV29tkP27ELQsj6_q4mP5Z-PmrQ05JehmVLmJSFrRcsvVeXcbbhuR8hatttU3O4aQnFBU28xuhLDqGHzsExuz22beAc8z6CApw4XXRZokyDVJzCnJuxDwOeqGOpaLI8379Fhna4VmCSWK8zw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4ac286f3dd.mp4?token=K2hq-0EJeWZolad-RDvvtgTEJ5gf45uAyGkL9fZ0u-_cmv1SEHB1Aqx6APVWiaipewW-atoSmRfa2nWehxQDEkRN0cSUxHOQ2zzy_kRIl0l14U-Uc3GB6aV2Bq8uZYfiSV_RbAFIh4a9qJvZrOxc3GEe8-qKw1DEa5RlfnCYXOqaVN9XIIdJBGGwgE4mKfJYrF95gaRV29tkP27ELQsj6_q4mP5Z-PmrQ05JehmVLmJSFrRcsvVeXcbbhuR8hatttU3O4aQnFBU28xuhLDqGHzsExuz22beAc8z6CApw4XXRZokyDVJzCnJuxDwOeqGOpaLI8379Fhna4VmCSWK8zw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جنگنده های اسرائیلی و امریکایی دارن کسچرخ میزنن
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/funhiphop/81607" target="_blank">📅 01:46 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81606">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aJdfpideVgBpKefGhEb2vmbtrXYd-joDhssMzrGwejsaCEV8QnVHcHVdFkfvccmrd1K0swQcNb1R99DuGTthnrlzGvoZubOMugHMcJmrb3VpO5GMYBod3W8g1LZcrBohUmjwah5rfUkouYmGVjvzVAuZNrHbRfLuQsdJeZs930fTn28lVwid5VGR3NNXrhcpyl0papT0TNptZnjrfxp9FajcDbMbUxwTzRSEFr2w6Fu0F_AY5eWTZXfUyjcDpsg4-o4eM3WjBXe0_e8bhQHYTRYkVfTOd9pJVvsYP1RaylaEjFLH9OTO3U7LSby5w_7RWpFzHNoMnJ-6oO8P6zpg1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شیما کاتوزیان جزو ۱۰۰ فرد تأثیرگذار دنیا در فهرست TIME100 سال ۲۰۲۶ قرار گرفت.
@FunHipHop
| artin</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/funhiphop/81606" target="_blank">📅 00:41 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81605">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromɪᴍᴀɴ</strong></div>
<div class="tg-text">گویا دلار تا ۲۰۰ قراره بره بالا
سال دیگه که قراره بره بالای ۲۶۰ اصلا
همین امسال فرار کنیم</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/81605" target="_blank">📅 00:05 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81604">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ITsNuVqK2Acl5TjEmvxiIWtvb4H2dLfoetZ4hewt9SQSK_ZZFSQoF-H2w709NEAA6fVJtjB6vjS2KIeRFUd9CaQKFomSc9sNENIV3v3L5hrTNcYHmhmjLOQBy16-QA807Y7oawJRyV56dxYWL4LkCeD81e5Wz2xMUQxgwbjO_h9wLlK4hEfFialSFcqwt-WIf99j0DAcwxvXFSd0IxawhviZug_KLhxY3l9a1K47wiImWDbMIBATly6Gcf6Iai-oNIensr7rbbuc2BbdMD6Y2bMQ_O4ST2SkQGfVILA409lcfHzQR-sljtkIsd77BUlg4c2wKRKAB9RBRR4fKG5cVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/funhiphop/81604" target="_blank">📅 00:02 · 10 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81603">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c227c270.mp4?token=pwl33GZkP4M2RpHXh4knqUnLwAKH5Ame49ke6DXw_3-7SY53KDahPJ8RwuSfusAmDLBjHpS3Dm8QlaY7a8sF5-l01VxIdVPnisYhQkaY9D-bJCAFeDj-noBkIltqeC3Oavor0fCofaevjCN_20TUgCmClTf3iidnwNwo6I3LzE6GuYTDLCRs145nXGuoZFaGhd_FbdXmRIyHXwmbLqz1N7dhMjC-EhtXk-r0_ld4krRfTPWjOrzWyT6SEW7KbLyycviBHkTGo72ZlY4peXGsKbSFjUhSu0vMa5iBolLlGcICD2QS2jcwscwrKFzqcXFZnBhRJLQtVEVICSIyR9oYXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c227c270.mp4?token=pwl33GZkP4M2RpHXh4knqUnLwAKH5Ame49ke6DXw_3-7SY53KDahPJ8RwuSfusAmDLBjHpS3Dm8QlaY7a8sF5-l01VxIdVPnisYhQkaY9D-bJCAFeDj-noBkIltqeC3Oavor0fCofaevjCN_20TUgCmClTf3iidnwNwo6I3LzE6GuYTDLCRs145nXGuoZFaGhd_FbdXmRIyHXwmbLqz1N7dhMjC-EhtXk-r0_ld4krRfTPWjOrzWyT6SEW7KbLyycviBHkTGo72ZlY4peXGsKbSFjUhSu0vMa5iBolLlGcICD2QS2jcwscwrKFzqcXFZnBhRJLQtVEVICSIyR9oYXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترام:
من قبل از شروع جنگ ایران یه نقشه و ایده میلیون دلاری داشتم که خب ما میریم توانایی نظامی و هسته‌ای‌شون رو نابود می‌کنیم بعد سریع خارج میشیم همون‌جوری که به شما گفته بودم؛
ولی اون وسطای جنگ چیزهایی در من جرقه زد که خب عقب مونده، تو هر چی خراب کنی اونا دوباره می‌تونن بسازن که، برا همین الان دارم یه ایده میلیارد دلاری رو می‌برم جلو که بتونم کنترل و نظارت هم داشته باشم رو همه چی، خواهیم دید چه خواهد شد.
@FunHipHop
| Nima</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/81603" target="_blank">📅 23:57 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81602">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">نیویورک پست:
برد کوپر، فرمانده سنتکام طرحی رو برای یک عملیات بمباران گسترده و طولانی‌مدت (به مدت دو هفته) علیه ایران تدوین کرده که این حملات به صورت نامحدود هستن.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/81602" target="_blank">📅 23:42 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81598">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/narENkRU-fdUACBO82Aqzqj2dtkGmg8LD-1Owjq9Z4B6dy_HRfH1DMcZEFGcRQTxNv16JDVsJc9uZPjuyLYfu1-0qtQ7MKmfQLkgv7snfkQdya57QNGn6Lliz1nCvAgsxb7fn5pJN64AjuZCtmELte98ZKfPYjshif6K7_Z8CZL8ntcfAUbkGqjBwQc1md4hWNDu4HDq8Brqlx4e25rwp29lJvZd_BUeK6jrbCA6tv0MHTV2QvmOMPe1QzQTeuUAHOLPJxXQFSZhMuYzFpXzy7U67QaftzR86GEWG15ZfognG35B8xAN9OPeS18HecTT_SxBaionW6h_8HtTBSTBFg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Iuc7nnHoI_VVHfqfk-Jj55lHPWDVnXorrCWHFS9-ZOsb24TvbeXaFf3S-m2vTH5a5Zvw-QrSNV12WBElHas80pe2vaPpT6jnRSR6F24fuHFxVK9SuBSq9d1gF7Q4jehW8F65MME6KbwkeL_wfAd9iA42Se231jur6p5FfOJDQRNCofyzrN7vmXjAHVDvnpZBoW1P_MWdVWAbMsHb98xAdvsVuxsNb4N4B2FoVx7QIneTH5GSuEAjH_JG0cApSXMAOO60ZP9xtWmxxeRtl6tLlzWDEwO35ZTWtBoVQzxh4_39piPFaHFS42lyJSfoWdrtJolXF6CrTYW885qqhH8ZHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aMCsPQvlXjw3_EP5ct1LxXmwE4dE7AqPEWq1hnijB19HML8DFVotes8BAToDnnIXjsj4-WCROovnTxIHs2sYp1q53V3mV_Q_tEa_3Pr4zzTVgkqcHwYDWoRCKg5ZzTVze1prNkM2IO6ocPlpomTZH63coOPBqvv8ovG0dx1ooQp0CxIFRNFIdFLV-tUwh7y-kE0Ou75nCoRU8IBZY_9JC2PytwWJpuTa3jvmK9sYH3ZJg1czd_F9HVOVcwQMphJ7BeN-iuXCNaS2nW_zMvjrFmOKqP9Qf0CSQEuJY4YsGf0LOHpn2Cav7fdZRSMjKkmwhiW_HUdGI4-gUZ4i4JMzEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lmxFcbVJH15tLsNKtHgDeX1rIqXLwmLt-1C8XyfGHcN8oi4nkQekUls7snteJGL8vzwnVLcfy6Vf4myICjyqysjMg7ZLdN3vb0Vbwylw0KhJnVG5leEEds9hKVn2zLve6iV7CXpAli0U7wkC9PVAteWzNBWBZivUWDBxhAuBJcAX7Bh8noZKasiqJSU4J_TlkzdG-0Tn8OPJa8r_prT6-8Aq1F8jrTTNKbRjWzIXoffxdXhfZZ1M1Mrr0-7gptnW3adaOuJrhB-6JchdhASgCrvq1jp22SSf2l1KarTCc6-7VoSQRMbirWqowAiQQNrEWGEGeevfCrN7W-DxpWtCww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/10712ee047.mp4?token=lmxFcbVJH15tLsNKtHgDeX1rIqXLwmLt-1C8XyfGHcN8oi4nkQekUls7snteJGL8vzwnVLcfy6Vf4myICjyqysjMg7ZLdN3vb0Vbwylw0KhJnVG5leEEds9hKVn2zLve6iV7CXpAli0U7wkC9PVAteWzNBWBZivUWDBxhAuBJcAX7Bh8noZKasiqJSU4J_TlkzdG-0Tn8OPJa8r_prT6-8Aq1F8jrTTNKbRjWzIXoffxdXhfZZ1M1Mrr0-7gptnW3adaOuJrhB-6JchdhASgCrvq1jp22SSf2l1KarTCc6-7VoSQRMbirWqowAiQQNrEWGEGeevfCrN7W-DxpWtCww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و آرتا دارن موزیک میبندن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/81598" target="_blank">📅 23:25 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81597">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🔞
فیلم های بیتربیتی با  زیرنویس فارسی
🇮🇷
تاحالا دیدی؟ با ربات زیر میتونی کلی فیلم آموزشی با زیرنویس فارسی دانلود کنی
💀
⚫️
@EzzyPhBot
⚫️
@EzzyPhBot
تازه میتونی از
💎
Porn هم هرچی خواستی دانلود کنی ببینی و برای دوستات بفرستی :)))</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/81597" target="_blank">📅 23:00 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81596">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NMwz63TjmIRPTT1pUsHokT9_AtasKuWDUrXOFzt8cEKrL5gXMlKyjG8TKNuKPAd1k1PTva1RKxqn5oIFtu5EzIa677sxpORVLbjTywUka_5OOYt8-gEeQg5m2ICq3O86N8oZ1irD45UCiXfDd7Pt7DIbYZvYZK59NEhW_k7sNRQW5afWJt5-jhZY3473ttOJihwaN4sdJKNstQudDZiAR_hu1PFP2ynFC4ZilpQ-7suz1Tr2nBaHLgiR45T5Bq9ZfPGiEOPoomB_SKeyEPUb7A1GdBRyuPhTa_zZHtZqS1PWZm-D4bciHvcT-HLWWj6eC5QfZxezrN1u20d7whztag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FuunHipHop | Jenayi</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/81596" target="_blank">📅 22:38 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81595">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kc8R8vKES6edb14cWEFpdaVfxP-wVrGn8L1ra-qPiJWn_AFHMIj6OmViov_8WV1ueagUUiRX69CWGleJxsD8Znih8r21MBUG_1hxlm5EemO2FMM--9rMnAwNJTZbMjjOorctt6tRU3ryiUuVJnYJMlXw03g4BBJ16eGNMhxeLLh2uWQO0ElFp25yrwIC2Tk1LQCNWjXXW1tq2b_uiRYwnYTZwOBH9n7WrJPE8eU1ruhn8bQIoSgmQ04ZockdFi5gOYUcncTpVqkdlse9iq9rF75gSv_InrcWccJqb5jggHSebyqpbvNTm7SKPYGLFOMsmKMkvnUHljXtynYcq1nTQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">برای عمو هایی که میگفتن ما عزت و احتراممون رو با برنج و ذرت عوض نمیکنیم او عه او رو بخونید
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/81595" target="_blank">📅 22:30 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81594">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1LSpfh9MCk6wL6uLJHpO5S3_9QnWqqQfsnJmF6OaPLhvkDY6wsvFMciHgjHkF87xQY_XJ-52-n3n6QJxuTrmITrYN3296_eMkle_sBf6NaF7PLW4CKGq3ikF6FTmq7cKq47tFy8zrQLEPL6p0tmCiJLzQ1Wx0yELfEjlveMwZ-fGlL8a6MEfa_ncKIWhJyqoBRHsIskMuhVPew5I-tfrO9uOZF33f4WX_GZLW0TlZ7_iy2szBiIMuaepP_yNQ6f7iR9ubSAltDW7L3pdEPC4kriOx4EC2iNat1dcRRnxaqF8lJ4gcWrQtn8z8_Dy5GpFBlka0EEUvN7c9bOtBl5IQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وول استریت جرنال:
ترامپ از دیپلماسی ناراضی است و وعده داده که ایران را با قدرت مورد حمله قرار خواهد داد.
ترامپ روز جمعه گفت که قصد دارد حملات نظامی سنگین علیه ایران را از سر بگیرد تا رژیم را مجبور به آمدن به پای میز مذاکره کند و قول داد که به این کشور «بسیار سخت» ضربه بزند و پیش‌بینی کرد که رژیم تندرو در نهایت «از صحنه خارج خواهد شد».
@FuunHipHop
| Nima</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/81594" target="_blank">📅 22:06 · 09 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-81593">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">#شرمنده_بابت_پست_رپی ترک جدید سوگند و سجیل به نام وقتی رفت ریلیز شد.
🎵
SoandClaud
🎵
Spatifay  @FuunHipHop | Nima</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/81593" target="_blank">📅 21:05 · 09 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
