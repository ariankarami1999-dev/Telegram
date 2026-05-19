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
<img src="https://cdn4.telesco.pe/file/n5CoADku3CG6jc1JoSV0wO5a0FhdBxzU2IT_rVyQ8t-AQQpPhqNES8cR8jgzuDyQ6X5o5hLOsuklDcEyHt5CI1tO_cY4x8tIXIFebyV_C_WfKOyjkmnJBcqRipsJEkDZ3QDZq4QA9xAwId9EvAS_S_f_U-HDv-_NhvWSICI8eMwVZlqwm5pKhZwSsp7m1O0h5XC4Kk0sqsynXas7NmA_QFA5iCvJ49-rJSFDxKTri_OyhSFZlTphvie4ikpOedIDMrbEWKBhoPaetF8Ztvvm2Jps7ZYsQ7jJQ42-lhyRnreOCYqIdcXTclwX_K9LqPj81L2qZhms1U_TAN4B3KS80A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فوتبال 180</h1>
<p>@Futball180TV • 👥 132K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-29 14:16:55</div>
<hr>

<div class="tg-post" id="msg-90073">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/URQchoGR45V3FxTI6e2zxqLWs_C6oQJB3i69ippLgwhJnYROcX4ASLmovpoMSIXqrGS57L9depZBu-XE0Hc0pmN2gbJ4GvSY2GYgxn5Ct0Oll9Ed0ofEiCukhB6y2HiP3pZmSETQq6T6WQHc8r1x2UheXI5pW9o3BztQlf3uXvpE11-uCq5wxGxZmTNmMuzjC0MgbxVcyTYwRncO2lfS61tBSYkkXGToB-EaHQ6ukRJjlwZsucqE9nly7jf-2GpoboOD84njnpdRR2g_nFP-wI3b4Up_Bc4ZWVA7c2xvVH3_dQ3GTB5njnRWmiho4jMFrzVwVQ19XbCk96r1fd0uyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رئال‌مادرید با ارائه پیشنهادی خواستار تمدید قرارداد یکساله با آنتونیو رودیگر شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 932 · <a href="https://t.me/Futball180TV/90073" target="_blank">📅 13:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90072">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/btZ3V1FwL8wffuKx7IkrZhl0V1LmUPiARMrAwIpOf_4NN17fpzkfQykAoqXDAQSDszDTJBylp0TCIq1LneWJk25Mjj0yhDR_tk1xL0HV_BEtfMlS-XwKOJJW-3KlZbwptngrW2sUctAfuGsAK3bff7k8V_RBrkfx_gI4COj1Wgvoqt_NNPlImGQVUJHfP64TY5j8Nue0zP3Nn7Pz0AUQtWBemASJsKCSw7zcD99MwOwSKNGp8iFGcLlthUPK2ivqZXJY1aES-ltCZTfWBlw9i_YjYXjAfQ3rUvVwvm9PxoP1YuJLkUOLJpPGEokWattbihSSHY2P9GRs6a-uK5WH7A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
منچستریونایتد قصد دارد با ارائه پیشنهاد هنگفت با لوئیز انریکه سرمربی فعلی پاری‌سن‌ژرمن قرارداد امضا کند اما در عین حال این مربی پس از پایان‌فصل قراردادش را تمدید می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.46K · <a href="https://t.me/Futball180TV/90072" target="_blank">📅 13:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90071">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c098031df0.mp4?token=POEbVB890fbrn5kblo4kSVrdiCZ4skScGXF__h2HjPxkjpSdd-PxvECQZ0GwFtNCfUvWbnuJEQ1PcWruXO9K4rRdZ--Cm5skkxlhd8E4Nr1ThaYENcUb_N6h_E9sY5rBLPE8uQgHApw2WxA28J6U9AHItJ8asmqkgNEO5_GWzXnHrNwyrJXj2bof8hoDZQDq3SmG68pQBIxRRMPMSubZeSiFfhRJ24N3__fItZC1r2UTJMym-CNdaPKoNSMCnbbgANWf-7SkcayFfrQks6lRBTwEENEO7zPft9CgKEAesUp5G4BtProb3Lf0xZMx5e6FRAhxjMJPcQHFn5viHxxP1w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c098031df0.mp4?token=POEbVB890fbrn5kblo4kSVrdiCZ4skScGXF__h2HjPxkjpSdd-PxvECQZ0GwFtNCfUvWbnuJEQ1PcWruXO9K4rRdZ--Cm5skkxlhd8E4Nr1ThaYENcUb_N6h_E9sY5rBLPE8uQgHApw2WxA28J6U9AHItJ8asmqkgNEO5_GWzXnHrNwyrJXj2bof8hoDZQDq3SmG68pQBIxRRMPMSubZeSiFfhRJ24N3__fItZC1r2UTJMym-CNdaPKoNSMCnbbgANWf-7SkcayFfrQks6lRBTwEENEO7zPft9CgKEAesUp5G4BtProb3Lf0xZMx5e6FRAhxjMJPcQHFn5viHxxP1w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
پاکتا هافبک تیم‌ملی برزیل و دوس‌دخترش
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 1.58K · <a href="https://t.me/Futball180TV/90071" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90070">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90070" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 1.54K · <a href="https://t.me/Futball180TV/90070" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90069">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twMg1l0_WqB-2I_ngBrD8PohgZGHPXnX3BxHzLr6_DGOjHESjbkm0C3_spl24lBW6l7g2QVGvqLHWZ3l8ogo4NUVS7JZ_NVFgFV_NWo5WDw_zZo_E2aiB8Vx1Ev2P5D4iBd67eAWIloeYbVRF5WAqLGPwkwyGK2BDBLIo6zVP0IEqJvoqmrJLlwcGXzt6gGrPXE8R68hUsNTeHeLUEcDz8IeK7Jry_k45feYyt9yQr2ykPDz4AiQH_EV0fnwYUMT6C4ureCF4UVwXS91qXmHLJf_LuKX9KP5Ll1A8gPympts0UhvDHJmrSIrrjpxmFdaNpDU88T9PCBghHby-C6JaA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇪🇸
Ole, La Liga:
بر روی رویدادهای مسابقات فوتبال لالیگا پیش بینی کنید
!
💰
در ابتدای هر هفته، یک پیش بینی رایگان دریافت می‌کنید.
✅
هرچه شرط‌ها بیشتر، پاداش بزرگ‌تر!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 1.53K · <a href="https://t.me/Futball180TV/90069" target="_blank">📅 12:58 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90068">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qwZaRFrtFl0svGmtTL5uei7CA-2XoW0JaM6Mow9LG3vdMS7ND2cRGQbIfp-jIEhZvEhmnSRI8d14bicsPjBc5qHCjv2QinNAZmmb3ob6khnxGQROHG8mULbrS7lypO5z8Fuw4Wi7gEYmIkz57szQSE85EfNaJr_uVhdL3AyAW575jK4yA2-6lms4uYHuX4bbCjRvQvOJPHZlRasIiEBvtJrfmshIXjrxJ42jHL3eoqQnbkYzQOB0jf4cK9bWXkpH4pJKngG0Lxua64enrJq93p0nluLv0xKdq0zMVRK0teAEM0TD7LB-rd6lfc7XHN6h02YLSB03dbEknT7YIcJ27A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
کیت‌اول باشگاه اینتر در فصل‌آینده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.06K · <a href="https://t.me/Futball180TV/90068" target="_blank">📅 11:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90067">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BSQpo2IkoqPxEfY18eSkTcRbawofi2GTTNbv7LK9BmUq3F_s3p3bwyBtr_6DdPB8t1Ju4_6jwq___ODXoN488oX_tw-q31pcPzLINaQer45dcXymmMoF_aDTPpQewxz-gtWtqSGns02pQy4bt9ST66R4AJvDOnj3mYdciLBM30Q2xmXWjf048VggTFVA_qTRFTVpWhie2v-2Nf3C21xNPPQAujo6IZIIp08cv75CXhq0LE2O-fngvFzaA52it1aB6cehGjKXsVEz14ljr2n7RsECKH7AGK283slxwJuJyE64I-yUwehrMX-bbDnTvAbramOquwXVyEjSNHTtTDo2Pw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
کیت‌اول فصل‌آینده لیورپول
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.28K · <a href="https://t.me/Futball180TV/90067" target="_blank">📅 11:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90066">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=TaL4PljUxNudilpKFsrTtVqJb4bvb25-i5HAFCZlsTFfMPPuHCoO5xtV_11NbNSIy6GxWImCnK5bVaYKJ3aL-VzIShtv7BTAB-sgmdreQPVwMtJwoQ0aTdZFCiNpxf9b_oD27ocGTtwBweFm2NB8DncU3QpdKW-F6Jfb2NZrL1PJTyFhunoCPVipoO1lBrrF4up1KNvhSIxtX8AhjcV-57zRKt5sI_ZynkNMHYDS6WZIZSBUmCq0oTEWFbdd1duxogctB2G4ZdoAgV25dJFQ-SA9ehqFM7BVyhCpc9sVlPwoROKvfVc3x7eXxC0nCgmHJugKGxXMg_WcAtoD8v3nMA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f1fd62d6ae.mp4?token=TaL4PljUxNudilpKFsrTtVqJb4bvb25-i5HAFCZlsTFfMPPuHCoO5xtV_11NbNSIy6GxWImCnK5bVaYKJ3aL-VzIShtv7BTAB-sgmdreQPVwMtJwoQ0aTdZFCiNpxf9b_oD27ocGTtwBweFm2NB8DncU3QpdKW-F6Jfb2NZrL1PJTyFhunoCPVipoO1lBrrF4up1KNvhSIxtX8AhjcV-57zRKt5sI_ZynkNMHYDS6WZIZSBUmCq0oTEWFbdd1duxogctB2G4ZdoAgV25dJFQ-SA9ehqFM7BVyhCpc9sVlPwoROKvfVc3x7eXxC0nCgmHJugKGxXMg_WcAtoD8v3nMA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سوپر صحنه بازی دیشب آرسنال
😂
😂
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.23K · <a href="https://t.me/Futball180TV/90066" target="_blank">📅 11:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90065">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
قرارداد آرتتا با آرسنال در پایان فصل به مدت دو فصل دیگر تمدید خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.34K · <a href="https://t.me/Futball180TV/90065" target="_blank">📅 11:06 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90064">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VgBe99WVi8PDmUv6QdEgseKJfK_hAFuJi-GxZhbWV8lggGYU90RAZR9a5zGSAPcQfnRkF-Z1wdOjeR_TqWg6Uf9gW9tKlQs8Q_9tffFBlXvL9ZWOnrL-4K_7_sDEP30_mB2BsoCPwE5_n9KUPCxgrX0S2cbW-YRTFXeNTAQ-A0oqmZR6J-E2tT3D2BuhO3bietvpWp98oDiKyGxvf0869XAebHZ-qt5lxdh5ZIp2XMmjWUwXY6vLDIEMxpuyWUeR2OacoPszQwmbDpKeEUGVtlKue0VnAgFF-P5yZ5nLutn9aWTWE9SszeB1Sbb12QSBfUH_AiHu8vCZfLpUk7-Nqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🚨
با اعلام‌فابریزیو رومانو، انزو مارسکا با عقد قراردادی سرمربی منچسترسیتی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.6K · <a href="https://t.me/Futball180TV/90064" target="_blank">📅 10:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90063">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=BenyKiRAv2oCFaJdQyyGp-EsKbRw1qmSRM5EY3lPLamzZKVU_X-hfDwbFKvSpKzGiBHQP9G_YCGcHQhwRipwDIeac6MJyNIM5EwDyHRennWQw1Dsy4JD17FYufHuXsZ_uwSEHahDVCZhIaq2UrLWNJlK4uHT-1-fTRvGFgT75NGZ50weFgEBH5G0pJJRNB6CilQSJwx_UwDbdeGZtxQG-BACtXKn_on5DXWhqbHDFl9cYMrX_bhlAsYBNA9D4EsUqilsf5zte14qkVdBjkiv-yL4dXA7S9CFknFe8QpBnERkLFz_cIQw3BMzuf1dMdW5bXS9f2zCZ2JRkmdD-aYHhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7a4a423232.mp4?token=BenyKiRAv2oCFaJdQyyGp-EsKbRw1qmSRM5EY3lPLamzZKVU_X-hfDwbFKvSpKzGiBHQP9G_YCGcHQhwRipwDIeac6MJyNIM5EwDyHRennWQw1Dsy4JD17FYufHuXsZ_uwSEHahDVCZhIaq2UrLWNJlK4uHT-1-fTRvGFgT75NGZ50weFgEBH5G0pJJRNB6CilQSJwx_UwDbdeGZtxQG-BACtXKn_on5DXWhqbHDFl9cYMrX_bhlAsYBNA9D4EsUqilsf5zte14qkVdBjkiv-yL4dXA7S9CFknFe8QpBnERkLFz_cIQw3BMzuf1dMdW5bXS9f2zCZ2JRkmdD-aYHhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🤯
شادی فوق‌العاده برزیلی‌ها از دعوت نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/Futball180TV/90063" target="_blank">📅 10:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90062">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=WZux7ZBxqZlr-PZd_64iyzPYfHtrRRWB49eBZWA5Iu9VkjqLdGnii-bmTWCeGmoduUnqmC2Ln-0MHGP_9rcBrhFomV0kEV61Uja9HMKEBjs_sx3uiemlGkcjd-htK26ckXPbAmdfj0dBpQN_c4uI7IPg2UfEhE36g8uu9STH-emhI39ypBQHl273_rFhBjjjQ6a3ONfndC0AS1CHCm7PJxd-O-tPed2rgDvwhk_c7-wb02CCoSx2NW_KxbUlifWIauvSsEbRXzb6tzMd_E2k510r48tQXkC0uRwnAdVWbjiABGb-tU7tHgUvVUYWp194kjFYouSq7Z04SQm_unTv5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2da1d08628.mp4?token=WZux7ZBxqZlr-PZd_64iyzPYfHtrRRWB49eBZWA5Iu9VkjqLdGnii-bmTWCeGmoduUnqmC2Ln-0MHGP_9rcBrhFomV0kEV61Uja9HMKEBjs_sx3uiemlGkcjd-htK26ckXPbAmdfj0dBpQN_c4uI7IPg2UfEhE36g8uu9STH-emhI39ypBQHl273_rFhBjjjQ6a3ONfndC0AS1CHCm7PJxd-O-tPed2rgDvwhk_c7-wb02CCoSx2NW_KxbUlifWIauvSsEbRXzb6tzMd_E2k510r48tQXkC0uRwnAdVWbjiABGb-tU7tHgUvVUYWp194kjFYouSq7Z04SQm_unTv5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
خوشحالی اندریک در کنار زیدش پس از حضور در فهرست برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.97K · <a href="https://t.me/Futball180TV/90062" target="_blank">📅 09:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90061">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=bBtzqO2hpx-2LijFXz6wBkH-8wUeL8-mWDpY1cJilDYjGsHTU7bP_jDvLP89R2EclXFzGs-TCID3I1CmdH1zsBnZknxh5_eFy2uo492eTiNqXpuhQabRPkRzQQDA4mw5eCuy0jSyIMh6QsBFWUs6bypR6cc3xbOfm0BccRCvfugg5M6gA2G-rMAbtt4-L8LbFLxDkfpbR3eq_m4SfZEBHHgOUPfNg1MJISTdz47qiS4Hesoyxv98jl3GfMPF8XTsLKFacGHjayl7meWYC1s5MfWxumHfusW9DJ7Rqmn88nLnT881RyynsSNhrsCFL0EundWETAYx8ma4DeH2kFUYVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1bf11ae109.mp4?token=bBtzqO2hpx-2LijFXz6wBkH-8wUeL8-mWDpY1cJilDYjGsHTU7bP_jDvLP89R2EclXFzGs-TCID3I1CmdH1zsBnZknxh5_eFy2uo492eTiNqXpuhQabRPkRzQQDA4mw5eCuy0jSyIMh6QsBFWUs6bypR6cc3xbOfm0BccRCvfugg5M6gA2G-rMAbtt4-L8LbFLxDkfpbR3eq_m4SfZEBHHgOUPfNg1MJISTdz47qiS4Hesoyxv98jl3GfMPF8XTsLKFacGHjayl7meWYC1s5MfWxumHfusW9DJ7Rqmn88nLnT881RyynsSNhrsCFL0EundWETAYx8ma4DeH2kFUYVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🥲
پایان عصر لواندوفسکی در بارسلونا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.08K · <a href="https://t.me/Futball180TV/90061" target="_blank">📅 08:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90060">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 3.54K · <a href="https://t.me/Futball180TV/90060" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90059">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/AEb19xAMEueVsMXICRTQhuleuJkzEClEIqGBrCYNV790KPZTvKXfDwJOQuR6jKr96JzMO62DgPbRaHLKY5T4DOrWOBGAfJEjrFg8qh6sIojDY1clZxdxXgHxIYljG_3oGOvcp90rmxGYFU2Pqe4aRhr0GpaPD9ozZlk5zqUcSKlsVtfh1959HsrB8K6cNNTZpkoYoZQTQz_q6eBOeVLPterk_w0OcCOyoa1ve74-l8oCLjGwZr3f37ciWV3q4EfV5jk9_Qqp000KmyIlZHvW7p09sPsQALrzfL3u6qW3G6zRjFj5oXv-ES2J2lfgjt7niFnGk2OKEUpU5g-O-mqc1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تو چنل بتمون هرشب داریم به سایتا تجاوز میکنیم
😄
ما هیچ فروش فرمی نداریم و نخواهیم داشت و کاملا رایگان فعالیت میکنیم که کنار هم به سود برسیم
🤑
🤑
🤑
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 3.55K · <a href="https://t.me/Futball180TV/90059" target="_blank">📅 02:08 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90058">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=ZGDl7daw3kowTGyQMnyx7BKg1rLPt4df287pi9ipduIoFf46oqtWQrdPoXREQLSXGDxMuE651x6nglsywHtSa6T7SiVW_5G2uQRcgzLzZqUjFMLBBxpHLuk9598nv5-PptzpSs_DqguH6-81MJYgHWesBdxw7d9NPAcuZ7L1YtBDXtc6q7yjSg5pcGSr198QunuMtJyD9WQPPp7gcJg0OKmbtu8VFVlIBiLMBF_2cNkBLn94BXLn1lrUi-z37Q-z8SRaKrBpBRzOAN11MJJsGmSLKwGrUq6uRKnI2OKGatD9Ef8LbhkkKsXUUxeVXv_c44OL07R8RyK7-Rzi3t0ZVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de7e2f01eb.mp4?token=ZGDl7daw3kowTGyQMnyx7BKg1rLPt4df287pi9ipduIoFf46oqtWQrdPoXREQLSXGDxMuE651x6nglsywHtSa6T7SiVW_5G2uQRcgzLzZqUjFMLBBxpHLuk9598nv5-PptzpSs_DqguH6-81MJYgHWesBdxw7d9NPAcuZ7L1YtBDXtc6q7yjSg5pcGSr198QunuMtJyD9WQPPp7gcJg0OKmbtu8VFVlIBiLMBF_2cNkBLn94BXLn1lrUi-z37Q-z8SRaKrBpBRzOAN11MJJsGmSLKwGrUq6uRKnI2OKGatD9Ef8LbhkkKsXUUxeVXv_c44OL07R8RyK7-Rzi3t0ZVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😍
خوشحالی مارسلو برای نیمار
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.73K · <a href="https://t.me/Futball180TV/90058" target="_blank">📅 00:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90057">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Wco2AxFqA-v38KFFTyR4-gPXUx53vvYrxLh8x4qC4xPCDbQcN9BU8SikmBjKReQckoPusw-1WvcEHQg0ZisTGtGcUO_aVekNNxx7_fY9pVQF1s4FEm_oqBUdmvpL_qXw_0CfIRC7c-xX4eFoc_ib9XvORSo2sDibIasOQWOhyPNfNdBLDvIsNU7ybszPFcPI4SoDsQPZP-dr0WMYhwnel9gialQxvz7pFiWhwtgwxjlFUp9Nge5okqiU_XKyan7IdldpzfWIIqsYwHeygYjEnpBB7rBIM6oIi1BbgDfGUpu1jXCTvqRvnlPvn-8vQVHc0F9PvKjGwbtI-2XmY1PfpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
جدول لیگ‌برتر انگلیس پس از برد امشب آرسنال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/90057" target="_blank">📅 00:40 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90056">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EteriKruBiH7ric3fJcPNAwytiQzf--zPlf1_wZHry04i2Fm00DeV9lGGXdC9n1S0JYjykob0M4IUlwMwrCPr3KT5tH9eyEzaiHim3hmtdkta0TXROI-s5vWzi6yCeATur9wxDiKAB-t2zmbHXckR4uTrvaZwDjZBGGzEx5VTBrPVYRKVqXmixoIiPboTjLDlddJV1za0nrZSA57s9Lm491cMbgsZPCEZ7Q_qS-CZMr6QeC5Bub3d6MKr49vRbacwUGoOwmYySHyVm0WoVkY9gtFGYe6Azp7I1_wt-kPvY8ujKX5lNixuddloHGodyElqufOxXMAPaLWlc60YPnB5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
لیست‌نهایی تیم‌ملی برزیل برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90056" target="_blank">📅 00:37 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90055">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/D5A3TwBXIsOtkQuVSMbuIgPyn1Kz9qch2lwWJohg0MrSqobjBO1NVFwbnsHFraJ_ZkX-4a_1Hr01hzC5aCnLCIpQjMQczzjBC7COs1A2FGNlYvgsdgeHqmFWN31e_Pn9OpN9xJ8vD7jINVxeUQl4Yp-kvtA2KnE7QtMln40xz5c85Mh-fNjbhXg_RvHVKkcM61tU4FVDcyAEjGVEuZx9UEAL7emJxSGmeY36pJ_jd5Jx1ZNhHJ69LxzESyUqHem_srAcPynCF15Ov4qo1lKDpVPG79N4OJJarmCBdb3Y2nE6lkwO9wSaaw2_w4B2LGSPmRSaEwXk4eW-t7Aujf5ASw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.62K · <a href="https://t.me/Futball180TV/90055" target="_blank">📅 00:35 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90054">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=WnPu3gQIyxWz9YrCXULkxG2c9OEiL4QjuB-8wSm9p2iYe13ts0ePM6DzXEVuR6Lp2YHzBF8W2w82Cjkjx0FGKG0E8SoambH8tt94POPpfW4nzGm6UlvmYxshl_FYjZU4did5XQhxuPKrsgwOfS8fNbJzKi8YxPpCKxdrrWo4444xSi_QrQRwR9VNvNgdO1i3x2ST_tIMIqNr32VXR-Ktkk90Ff1H5yKChBoK7iqC_z6D6ho5RQOIY37bULd-vobWweupMUiN0NII-X3E3flm7cLKGAaSccdKZ8h96NRKYfZUBgImkkcc8pBeaZdfNu5CK2YbsB5z5CwEBlathEi0yA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6072fc8645.mp4?token=WnPu3gQIyxWz9YrCXULkxG2c9OEiL4QjuB-8wSm9p2iYe13ts0ePM6DzXEVuR6Lp2YHzBF8W2w82Cjkjx0FGKG0E8SoambH8tt94POPpfW4nzGm6UlvmYxshl_FYjZU4did5XQhxuPKrsgwOfS8fNbJzKi8YxPpCKxdrrWo4444xSi_QrQRwR9VNvNgdO1i3x2ST_tIMIqNr32VXR-Ktkk90Ff1H5yKChBoK7iqC_z6D6ho5RQOIY37bULd-vobWweupMUiN0NII-X3E3flm7cLKGAaSccdKZ8h96NRKYfZUBgImkkcc8pBeaZdfNu5CK2YbsB5z5CwEBlathEi0yA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
🙂
شکار لحظه‌ای صداوسیما از بازی امشب آرسنال که با برتری یک‌گله این تیم همراه شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.86K · <a href="https://t.me/Futball180TV/90054" target="_blank">📅 00:28 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90053">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/E_S8wsfzAKBxX7X0XcEWZ--ODnvrDWGeobah9fEsJHL49-hiUt1JIRAKrolrpfeYzYAQKqjg9GBFoZk9V2gRHoh3m-0pKfyTIyfEVh6I7bn1emZhlqjHezEaLThPydcTSiDYzcA3tl9Mlciy8xgf3CVAW3ZvQGaLiJ9IrxQyugR-8nYJBYN5ON3RcnKBvostOVcshq5HDmvPZWb8JOZSK-R0aO0X8d--CptFjtyFrHFv19gKjxNKWd52x39u3aSkAGMAhC_G-ziDTxijFBZVHbWZ_FtBUmQ_R8wAVlBJQ3ir1YLfBMwNoQUzN2k43Sxd70pn4IaTJmqk9EB4p4hlng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
نیمار بیو خودش رو به پرچم برزیل تغییر داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.81K · <a href="https://t.me/Futball180TV/90053" target="_blank">📅 00:19 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90052">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🔵
🟡
🔴
با اعلام سخنگوی فدراسیون فوتبال، سه نماینده قطعی ایران در آسیا در صورت کسب مجوز حرفه‌ای، استقلال، تراکتور و سپاهان خواهند بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.2K · <a href="https://t.me/Futball180TV/90052" target="_blank">📅 23:40 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90051">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
لیست‌نهایی تیم‌ملی برزیل تا دقایقی دیگه توسط آنجلوتی در نشست خبری اعلام میشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.13K · <a href="https://t.me/Futball180TV/90051" target="_blank">📅 23:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90048">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/90048" target="_blank">📅 23:32 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90047">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fqkninX3ZT5_t0jr0ob_S3eoEydF1TPU6RuHfmSdIpN0ZId19qY9N9fY5kvCzbIdlSwarGcIy-M-cJ0w4SiUSKcvUKA0V6SP1opBvZrg1KKlMIPOdoxAEmbBuGAsSj4U93sTYQehouCxRvPlPw6ukrOB4rlRBWJTiezW2HKLMnwl_5GxzT6hOtBOzm5JM0nIziNhI4eR15CeNiuH_a2RsmuxdZS70QI9U5d7Rb-ztK28fEs4cOHMpKYHaD_fAGr7SbkDishsnjjw4tXbhTOv5cPZeK_XMPyO2XZnHRHuQl_UVcFd6VQ7ReHncN08Loaai8JeJXWuoSuYksMp2nev4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
❌
پپ‌گواردیولا سرمربی اسپانیایی و پرافتخار تاریخ فوتبال از منچسترسیتی جدا شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.32K · <a href="https://t.me/Futball180TV/90047" target="_blank">📅 23:25 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90046">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🚨
🇺🇸
‼️
فوری از ترامپ: امیر قطر، ولیعهد عربستان و رئیس جمهور امارات از من خواستند که حمله نظامی برنامه‌ریزی‌شده ما به جمهوری اسلامی را که قرار بود فردا انجام شود متوقف کنیم، زیرا اکنون مذاکرات جدی در جریان است و بنظر آنها، بعنوان رهبران بزرگ و متحدان، یک توافق حاصل خواهد شد که برای آمریکا و تمام کشورهای خاورمیانه قابل قبول خواهد بود.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.33K · <a href="https://t.me/Futball180TV/90046" target="_blank">📅 22:38 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90045">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=oAsUbCfWadZwW-l9A7iCibDyBLJFH1CbkTJWaY6NnBivsskVgjxpxweUEMdgCmuRjCYH7p7jGiGyH1HJE1ejWbWxAudAwRnncWN3k4N201SWhiSdQoCw2OFVA387iu8YHY9gpYN8lTKGhyeisChJhsNg1gLONxj07nv7PJX2ippRVFzgWVa4bk1WzHAprWb33Z1sh5_zGEIw_DGNEkFoHjIpwVl8aSAUsvHKSPV3qZba9sf3Ym3BNTLvH5f1cpN43XoCn6dRFS1MMQKzfUvczNfz5sFulVY2MunVaY4vTkVeCtgPlOtKt_fS5-ymAtxF4FYa83k-4rlMEZ7PF3v60g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c28244d9b4.mp4?token=oAsUbCfWadZwW-l9A7iCibDyBLJFH1CbkTJWaY6NnBivsskVgjxpxweUEMdgCmuRjCYH7p7jGiGyH1HJE1ejWbWxAudAwRnncWN3k4N201SWhiSdQoCw2OFVA387iu8YHY9gpYN8lTKGhyeisChJhsNg1gLONxj07nv7PJX2ippRVFzgWVa4bk1WzHAprWb33Z1sh5_zGEIw_DGNEkFoHjIpwVl8aSAUsvHKSPV3qZba9sf3Ym3BNTLvH5f1cpN43XoCn6dRFS1MMQKzfUvczNfz5sFulVY2MunVaY4vTkVeCtgPlOtKt_fS5-ymAtxF4FYa83k-4rlMEZ7PF3v60g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
لحظات احساسی لواندوفسکی در رختکن بارسا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/Futball180TV/90045" target="_blank">📅 20:12 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90044">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j0VdbEFWm05zo9luwtcu7neptdsXcvXUw7DGxTQdtXs10ymVNRzQlhy-vTClpZ-jX9l5YT-_4TjmyRt93KlNlaXi8WdA5E8FkLSXsI5X1dhn0GYHEyhVmQUUUFfI6Aj75YIoBpd9xoLZM3uR9oZm_5NBbsJSQPIT0kKNJGYJBFlB1cjisksDx5DoQAwMuMoovN84fX6fUH2VZ5fsBhcCkLbvYi31TX154OYQ6GKA69ammCm2nGk0M5H1TYA0FEkgQpDTtb2cATVwT1cbFnu0dT5SofhMeY6GHzmPQDFU-KDbh3Y703Z8qPK9riVF2f7RcCn8wKyfrz4SG5fA2Mp2Dg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
🔥
عملکرد ژوزه مورینیو در رئال‌مادرید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/90044" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90043">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90043" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.66K · <a href="https://t.me/Futball180TV/90043" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90042">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f4KgiqTCVidTCBAmWNK8h2xWj0nv_dNMDpr5f2pfpM2KMsOL7caW4nlUMSDKV30M-BklLiFRa3fbWOp0CEB1-7X5VWOmI1jur3SJX2SbSYvmGKRJNsnX31ixKqxNjoum9k0jNXh-SFP9us8V0hk-OBfh1Ck9PNHm3p7ccm4it190td9RiOBrt8b_thyPzDCwr3yh044nNHea3T4KhqEIS_4lAhDuzBO5NVtUXt5oTsrGpB5ZAcA7SCSBsmJ3JjRy03BmONIf4SKLEifRw-A6-XijpzYiLLNXxL7Kbv-cy0ezl4OW5es8N4gy5JLib5OH2ak-JQzqVGtS9gHsgrASyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤑
پروموی Crypto Freebet
🤑
💠
حداقل 5$ با ارز دیجیتال واریز کن (حداقل 5 بار در هفته، در 3 روز متفاوت)
💠
هر دوشنبه
💎
یه پروموکد می‌گیری برای 30% بازگشت وجه از میانگین واریزت
💠
سقف بازگشت:
💸
تا 300$ در هفته!
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90042" target="_blank">📅 19:57 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90041">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fo_BXyBo2bJ3LByr1r-OZc6pTQ3iyYG_3_VTgf-K7BWQgO9phDK_trW1BtovJd912rvZLNO1P6fVxAUVFS5Y55K_OWOcDfhjBiM6NkA1sKuvd7iiXuBXulwehXBJmK8inIVHmt7TWx_r9tBsrlpyMQYB0oy5gwh4grlyebRVvTq1mefndymQnqeD5iY7m_w2bJY6pLDlVRVFBEvuf7tmtPTc_IkTPkB9OoWnL0FGOu0H3d2DaXEXxVGlwLdACJ-tVx6LhxlQN0La6AqjXhbmn3UWjMTEdcIyJnHDVM8kLYiLEILSfgel3HqqQ4spbYKykFe43v2OrBMHYxLJOEX3yw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم‌هایی که تا الان سهمیه حضور در فاز لیگی لیگ قهرمانان اروپا 27-2026 را کسب کرده‌اند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.61K · <a href="https://t.me/Futball180TV/90041" target="_blank">📅 19:46 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90040">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn5.telesco.pe/file/HuzcXzdnmqGrOZ78bWf6bDRMY00fxfLCc1EbWu78rzFtW2bywvo8FSLAEiRV13iC7eR6Wjlngm4sfAUozPnOnfVIkj2KWGfHECVcyYNxt-lQLwc5pLwrbpz0N8Rz5nwJcxShuQ3D5oNX8-JyiQI7t-deQJXQdXgRhCvw9RH-jLFam2N2LslZDP1Ang0pzF8YtfJmAqG8e3pPeBMawr3VTydH8N0HkQmsVanqrEs-2t_HzP88bJ7SNRHW-6_3uDgOiI8sgPQyjhP6XHJ41Vug8ye28ygdN7u7shmi0WylQ3WBcoutOpTGV4NCYgkUU75G3wcGMJHWKPA-lE69eUR_PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تخفیف فوق‌العاده - ظرفیت محدود
سرویس اقتصادی با کیفیت موجود شد
💥
10 گیگ فقط =>> 1,700,000 ت
20 گیگ  فقط =>> 3,100,000 ت
40 گیگ فقط =>> 5,600,000 ت
سرور ها  v2ray هستن کاملا با کیفیت بدون قعطی
خرید
@amoadmins_bot
@amoadmins_bot</div>
<div class="tg-footer">👁️ 3.5K · <a href="https://t.me/Futball180TV/90040" target="_blank">📅 19:36 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90039">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y8MoObGq9MKvi3fQlaBt8vRQjjojVJ1auP2a-6Z_8zg3W2GqrBDAKWuohXqA28-Z3bFPn1kunU2ocGBWLsHkJRdQo2VDkshiNfW7V26Ezf-SfLuKHPX11fQvYbOvtKdS210eQ6Ue8lKzAxYUKIKvY8QT8Ub886cU5nLk1uBVHVT7fm8GrPAjKFsPXmdpe8oTZLQ8dFtTLMmslEcvpsyTlKRzqkpgqU4U86VefttEZ7ArcmARBDB-t4uWWfCjQhBNIq26PW3eX4P4f0JKHVzNrdS_y2wu6iNS87ame0gdL0GE1X9t-T7nqZFyNoU46-bsgZaRWpgrmmd3mKN7qZ2jXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇭🇷
لیست تیم ملی کرواسی برای جام جهانی 2026 و پنجمین حضور متوالی لوکا مودریچ در جام های جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.7K · <a href="https://t.me/Futball180TV/90039" target="_blank">📅 16:21 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90038">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZUo-HomXzjbnxHWjPHIqlEDUC-TumDdaKIOj2Ku2W1-b7SxEOhLKoxyIunFMHGW9kgBxC2NIc7-XgLcvfK56qkfSWngkGTApmJl-YID3D80oUw_mCuGsN6qT9UBNB4ocLyUwea-BfyCb_UB5bBqtQS5jgixnF6p7Uplw-qBgulzWyhQ6ZyWO5VMIAoju1ZVRhvVd0E7kZR6RCHXmR6-duOFFvWnGyHZwu01bxAPlX6TJ0vT9eg39gAJW_9Wsh9YtnV_-pNWjN-a9nDeZKuw5I70wjIcx_mIYPyCYL8S1xm4xZJ9LQ0nQ3aKZSyZVcBjJiDHy1yYpPgyhn9TNgxY63g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
رسمی: هانسی فلیک تا ۲۰۲۸ تمدید کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.45K · <a href="https://t.me/Futball180TV/90038" target="_blank">📅 16:20 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90037">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/b5E64H_YE_QolnQINmNyqlCEImP5zN46qPC2IMCayerN-XtyOPTfIM-0X_RbPLSPLJgR7pk4nooVym3scgyMX2cbKyAJhOiTJmSmqdPx5A9vlHarPJhkCQ_3d3kQX-yjDhwOZ9A0yja5_q100z2gPZHpYVUyKsTJGcZK8E1bOIw5_QfuqYe0tjCM2n9zWxlZj5voDhZdxAh-JDcEx4L9qDl6B_A-iiEKQPvXCVwOEMMPPTLC_ifDxF_YaUBzOQfm6_QoQUWptNPO8ye2tSqLV38UEjPVAr-qOJoQEqOkaf74th9mlFOB0w-aQHi-klvkEaAV5GwG3j7abrsKny812Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسمی: کارواخال از رئال مادرید خداحافظی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.41K · <a href="https://t.me/Futball180TV/90037" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90036">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryPaqB1dj8KtuqUko16nj2IkcwBH98cHe8W1uBFLDwDHWG9ZzprqcgeSLvJXHxG3KMjMzz9enBuq87EPjEXLkNRgzfHDaB1p5CkGOYDc978pO_E4E8MCy38MrTYalrFYe4d23h16d6WKXaG_D9EhN2MELqCoGzJwMX_91tZmwyPVfeSMjeOq_B3ox-3Jk83sVlnkHrwruhKiOH4owYmVn3OIM4zqZMc7GL0n_FA-KvIViQVuYWefDqdAioBP1vS9foqlAv2HHfbPUo1Fexgw7smvRoc6YWmfHN9_bgX6VT41iZN-vYKcUNM4RD8y-Oz0RC2ETmRYnb8oOKbqNkQxXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدایای ویژه و شگفت انگیز چیتابت
🎁
۵ درصد شارژ اضافه قطعی
⚽️
بونوس خوش آمد گویی ورزشی تا ۳۰۰ درصد
💹
صدرصد پاداش خوش آمد گویی انفجار و کراش
✅
ورود به سایت و دریافت هدایای ویژه
📱
@cheetabet</div>
<div class="tg-footer">👁️ 3.44K · <a href="https://t.me/Futball180TV/90036" target="_blank">📅 16:18 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90035">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m7mHH13BQYJoEvez3JFYCqmUDxx7lZKm3eSRuwNahyfyyjupLegwDDWRdFx5qzmldnmEQDtcQ-Z0IK-7I1eVei9oMJDKcvHO4W3t_5c3fthBzNhIKjNnRp7vgV9EH5qQgyuOJLaSQaY9SWR3FEFMHloYtkmvXxUAy6mkEkZuJ2QsjVyw5wcjWJIeQ8v5Sz6AXmnrRxU5rwGDWUtGcLQLn-biKOqPpHYACSew-PaweJn-uGhktqdb9ApIUD77PJTlYe7iPt1hAKvWriz6KxQOX1qLAyOtgQy1XikarMXxu6VcYe7ZPgb7DuQw-ToL7PB4yjwnxMxucNuX0Cg1cw61ZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
رکوردداران بیشترین بازی در تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.57K · <a href="https://t.me/Futball180TV/90035" target="_blank">📅 14:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90034">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=Rzl3SptMlExTVxoHrWStsE9w9Wic0o2JhBrwsXn16DFHy0vCG-4_w5QR1S755fV1xx3yTrhDOtHNTwV53nhC9LJt1yNulK761BL5JtzAFiMOm5djThpeNuSmUPQE9ZZ96P25bbyujasGP67N_usREJLxm7p5y5wVC0uNaYijy_yFS4rGi9Y1kKrZYBBa4Uhw75bszgpLy4qFJbu-5Uj0LCRsbp0MBSFihdGjSVtdWTO13X7JHDGfernWHO0C-f6khGdfcXn5gKx-09LrqEGI2c0rlWiFrLULQ3Oc6UmISgbJf_jzsBBqhVmC0jTXvW3fbWimIARHBVaKhB2VyX4lTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8afcf96866.mp4?token=Rzl3SptMlExTVxoHrWStsE9w9Wic0o2JhBrwsXn16DFHy0vCG-4_w5QR1S755fV1xx3yTrhDOtHNTwV53nhC9LJt1yNulK761BL5JtzAFiMOm5djThpeNuSmUPQE9ZZ96P25bbyujasGP67N_usREJLxm7p5y5wVC0uNaYijy_yFS4rGi9Y1kKrZYBBa4Uhw75bszgpLy4qFJbu-5Uj0LCRsbp0MBSFihdGjSVtdWTO13X7JHDGfernWHO0C-f6khGdfcXn5gKx-09LrqEGI2c0rlWiFrLULQ3Oc6UmISgbJf_jzsBBqhVmC0jTXvW3fbWimIARHBVaKhB2VyX4lTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
📍
Tehran
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.52K · <a href="https://t.me/Futball180TV/90034" target="_blank">📅 13:30 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90033">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DCzblIfLBw9kvrsd9I2J8eiIZg2iwd2DSsZ4bQkGxKnkIG_-PCsZobpodWKp9BF51Bskdwpw_8bnm_5qI2zmGr7CES3KCppeeiadyk1zkRJfIbnB9rWb-U6HvxVefNd8y-I5wiNXYlPf_nHs995XLZJ5_q2H0t-XmLIffBhswkKiFYOw6bOVVICYXoV4OHOrjRLeNNPe8Ct8Xq1_CRhs0gRxyG21IVdO1TJSTEewJcS-gv9wPnJkbOdbSEg894N_m46aYvHoEz_aeO4SMkMznRV3F31t7boDOJ4NQLmF_n_wyXUonixA7kJEADEEFrkkYye8vwsOHLAIXjgFPB_mlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
روبرت لواندوفسکی بعد از آخرین مسابقه‌ خود در ورزشگاه نیوکمپ، عکس نمادین اینیستا را بازسازی کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.36K · <a href="https://t.me/Futball180TV/90033" target="_blank">📅 13:14 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90032">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">51.9 MB</div>
</div>
<a href="https://t.me/Futball180TV/90032" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 3.35K · <a href="https://t.me/Futball180TV/90032" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90031">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uiQcjT1f5Xxo8w-X58gT7Acwwyl1qjKd87UD9Vfi2165DjWiKN_EsggI-608AeFSqGEp49wTNopQg5ZtOihhMTboQ55Z9_C59u2BQftnioTaCiv3wA03vsSKnexWDspn1vZBqoQX7jDW3YzJMDjb5BbdUwOADQJPAApICZUqeIgMaM1UvzweeiDFeOTepednfc3bZ8KPSFx19dtBRgBxl7lddOx5_-U7GcdB4aezu-ydk6_rF6X7Fdx5pAUjSubUq0sViz8ZQfncZZCrceRL4itGekRzsRCCL8eJ5oUZunbXJMk56uDrb1lMJEJNkGBs0Uf1tTXj3geEXy0RoSNPFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازی جذاب
🔵
بارسلونا - رئال بتیس
🔴
🔴
🔵
به Barça 1xFamily ملحق شو و با هر پیش بینی درآمد داشته باش!
🏆
فقط این جوایز رو ببین:
📱
آیفون 17 پرو مکس
🎮
پلی‌استیشن 5 پرو
💵
4,000€ نقد
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 3.75K · <a href="https://t.me/Futball180TV/90031" target="_blank">📅 13:13 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90030">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=ESotvFWV7VprpywTsIZZz1SLEUQTNUHrsLHejVO4UGpVC6JqcTmjS_jx9wPHJtGKv5a4CP2qFduCgDd5UdOddt2X5M0IPsmtAgwRsKkg1UWluqoJpwv_Hngz25XiacJlzY461qyNTy1HSIfe-lA4NdWReRSdN1ThNw23LaeyGTraLCTMdwBlPm3JaqUYqiE1PHiCpTSU92SDnPXKqnF00P0NpSwtD4jJFS2U3ABCFc1fxVjXv7-Fvxif03R-W6190tGLhaYNmXb8OkEjXHnkJdk-J6m4VKwU3Juez3i_qHkdvrjejpXwvVlZQncm76NzRbRSX8xqqSHsmPREaCV0wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2c9bd4b703.mp4?token=ESotvFWV7VprpywTsIZZz1SLEUQTNUHrsLHejVO4UGpVC6JqcTmjS_jx9wPHJtGKv5a4CP2qFduCgDd5UdOddt2X5M0IPsmtAgwRsKkg1UWluqoJpwv_Hngz25XiacJlzY461qyNTy1HSIfe-lA4NdWReRSdN1ThNw23LaeyGTraLCTMdwBlPm3JaqUYqiE1PHiCpTSU92SDnPXKqnF00P0NpSwtD4jJFS2U3ABCFc1fxVjXv7-Fvxif03R-W6190tGLhaYNmXb8OkEjXHnkJdk-J6m4VKwU3Juez3i_qHkdvrjejpXwvVlZQncm76NzRbRSX8xqqSHsmPREaCV0wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استایل متفاوت جورجینا، همسر کریستیانو رونالدو، با موهای بلوند شده، در مهمانی جشنواره فیلم کن
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/Futball180TV/90030" target="_blank">📅 11:47 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90029">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CoMf-hSomyMRIxsQN1ckiZ2BlAAoXQFW8aQxSQGURBx3m1-NeCbdwhd8zZCS7KFvsvADb1gaBM4io2eAHx8nMdGA_UPR3UaxHo71drROGkjfd9lzu5ezvj1hcadNCe9Wc9cRtTQgalo7VGkRctmSzaUbVMCzf9HufcSwKjCaDv4nSiVFkQKDxEif9cMbhH-2CgvxJbQwhro4VrzIIz9kaxgHj8-IceE4jCactJHr6AoDGTXMfoh30Tbwpq40vkjL2IithgqLuF_hx4EDQrSjy8DwP2uui6X9Rxa-3EkKS_s3twRKh0Fl9JUT6gU1sA6mrVLaKy7cHXdw3rJvLX8Qpw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
سرنوشت تورنمنت‌های رونالدو با النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.24K · <a href="https://t.me/Futball180TV/90029" target="_blank">📅 09:35 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90028">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/441c980280.mp4?token=Naxj6oXh80lmPp-ozFiv3C79z_h5Nf7X5wqU6QHgPOJXXjFg1cCxeAQl0duQbNHqNi4x6lgaEmtN-yP4alhuwgN4iwyfyFB6OupgrAqGIFufJaTgfDBfWgSgZKEeW15wTEq13b1oxwgumu9LvT81nhHbyaxe7FNH9OMxzb9ZTr26Bja2OoM_8vwoQz9HXpBKFh3AcRKgqcJQv8R_MGgHtVhfEr9937UBldRmjtIZavJhwVdOQEj_W1HrVSFqP1vRMoU49aElvcp-L4lSgNkAkFtbQjXWZTrNflvSOnmQulQQHbaiwSLoAoIDFn6pjPFQxW_JufBPTYhi0739bfmDFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/441c980280.mp4?token=Naxj6oXh80lmPp-ozFiv3C79z_h5Nf7X5wqU6QHgPOJXXjFg1cCxeAQl0duQbNHqNi4x6lgaEmtN-yP4alhuwgN4iwyfyFB6OupgrAqGIFufJaTgfDBfWgSgZKEeW15wTEq13b1oxwgumu9LvT81nhHbyaxe7FNH9OMxzb9ZTr26Bja2OoM_8vwoQz9HXpBKFh3AcRKgqcJQv8R_MGgHtVhfEr9937UBldRmjtIZavJhwVdOQEj_W1HrVSFqP1vRMoU49aElvcp-L4lSgNkAkFtbQjXWZTrNflvSOnmQulQQHbaiwSLoAoIDFn6pjPFQxW_JufBPTYhi0739bfmDFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🤯
جادوگری بامداد امروز لیونل‌مسی در آمریکا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.38K · <a href="https://t.me/Futball180TV/90028" target="_blank">📅 07:41 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90025">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QrYf4SaQlgTWpu9gwcUgv2_uOJRZY0KpAntdnNNYI3YsUsMEcdMEd3g3CWTchzGkdeUtrTPbIx3c0vMwURN0QsRvydxhOrfOmYlq1wIQnqyE-2x-FiDJw4U3xvswhtQM8y9S5VaqWrhA_y1_uYhzLIfpnDUWDTLPPytFTgHafVvII2BtDkvXJcgTGGpjx5awqU_BItXMQSQrmGy1WGV6pJxMc55b_igHRDEEJRF0631RaEgrKK9Ex1UQcb2VlSj0XKegXoXFtUZFMyHdSktHU2rdl0jz-gLEXXC-p2YwIhNbGF_C-Zd1gnL4hQJ1KzJjaPu8Wsq2xuSN_VU7GmEr-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🫪🫪🫪
🤯
برای فهم‌اینکه لیونل‌مسی چه اعجوبه‌ای هست کافیه بدونید که این بازیکن سال ۲۰۱۲ موفق به زدن ۹۱ گل شد و تیم وحشی هانسی‌فلیک پس از ۳۶ بازی لالیگا این فصل موفق به ثبت ۹۱ گل شده
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/90025" target="_blank">📅 19:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90024">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=sgcAXEbqz0Dux4OcnrCndmIThPshZ4cJRypOLCtjIkdMK297SCp0XqoDqyUpwaWYXpcsSLyJCz67jnx9EOG4oZt9QJYau7JWHAlIKoX9md8hrPGknOcINEGCgBj7PB-bPzsE22Q0iOxq_ElxaD52W8i1aCJgEEjZyY3qhDdwBZ76fGL4tnH2Xzx54Bvl2cs6h_dUbkiWEQoKy2OezbW4RHCTI8GyzMygKERDR__eoFKfM3-2X6qHdH18NR3oHmr1FRTAt4kfhJU9jrpSaNGgnYTYLzax5tfugtaWK9TOFJRfxNCzC3eMWYBX5MpIDIAoLmq6e_FSMpwZOXV1AvWZTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1af6bf0b38.mp4?token=sgcAXEbqz0Dux4OcnrCndmIThPshZ4cJRypOLCtjIkdMK297SCp0XqoDqyUpwaWYXpcsSLyJCz67jnx9EOG4oZt9QJYau7JWHAlIKoX9md8hrPGknOcINEGCgBj7PB-bPzsE22Q0iOxq_ElxaD52W8i1aCJgEEjZyY3qhDdwBZ76fGL4tnH2Xzx54Bvl2cs6h_dUbkiWEQoKy2OezbW4RHCTI8GyzMygKERDR__eoFKfM3-2X6qHdH18NR3oHmr1FRTAt4kfhJU9jrpSaNGgnYTYLzax5tfugtaWK9TOFJRfxNCzC3eMWYBX5MpIDIAoLmq6e_FSMpwZOXV1AvWZTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👋🏻
پایان عصر کاسمیرو در منچستریونایتد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.94K · <a href="https://t.me/Futball180TV/90024" target="_blank">📅 17:35 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90023">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/109fc9f803.mp4?token=GHWF-am99wfArkI1ejlskA4w4vmG0g_FqM-50oP-vAUcYxgBZcpAYyQJDg1rb9cKgWM3_SB1amjF_vJqI4Y-Du8I66a14OlWM6FuaxIOUI1RNnEwcxsM31nujUm5huicyA3ct3ACJmKgUl6YtxIe2uf7pAE9pNUxngmUJsTC1ZKOBVzLWzWN3e4sl2XnEhOyPN63XE8MaSaS2XSq9HH1_T0lRYYPLtZ2tXxRz1K_JyjcJWfkgT-P5fxQ9skdn1Xo5esn07VEMCYZHTyHx8kIXUIdquBalk6h8vwNGSGqfgb9ofMPvbFNbHksFGTr-awy85aQHMrsT2T6X66mjclPzg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">◀️
لحظه شکسته شدن رکورد دوضرب دسته ۱۱۰+ کیلوگرم دنیا توسط علیرضا یوسفی با مهار وزنه ۲۶۱ کیلوگرمی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/90023" target="_blank">📅 16:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90022">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🚨
جزئیاتی از درخواست‌های آمریکا از
جمهوری اسلامی
عدم پرداخت هرگونه غرامت و خسارت از سوی آمریکا
خروج و تحویل ۴۰۰ کیلوگرم اورانیوم از ایران به آمریکا
فعال ماندن تنها یک مجموعه از تأسیسات هسته‌ای ایران
عدم پرداخت حتی ۲۵ درصد از دارایی‌های بلوکه‌شدهٔ ایران
منوط‌شدن توقف جنگ در همه ساحتها به انجام مذاکره
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.19K · <a href="https://t.me/Futball180TV/90022" target="_blank">📅 12:54 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90021">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M2UNFBll93kZzQfUcFyGASeMZTwgqxInAkAmgSM6prV7SIgc7-YXoy5i7UjhpEj2dYLJHJfpP6aiRO7BkfnnwwMaUMymgcqZS_3pMngm031vnlmsmPO3wtyI_5na7Z_A6SBCm-x026HG2CTidyGwMVdMzSzP-4gPP2r7U2Q2nvNtb4P6IIzEzSsF8JRl6LYskiA1XMx63YTfuo6eZcrY1zoRfW0uvTsYzzZ9-TMAiI45xBzeL4j4JV88JbfdeCCrenL4Zr20LchiZZvyev5NGFD-bPuOXoLF1QLh3n_R0SRJJVov27eBYWAHq3LV7fvDg_Cz-UvjLT-r10Fmtje7zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👤
لیونل‌مسی از سال ۲۰۲۱ کسب ۱۱ جام
👤
کریس‌رونالدو از سال ۲۰۲۱ کسب ۲ جام
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.93K · <a href="https://t.me/Futball180TV/90021" target="_blank">📅 12:52 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90018">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.45K · <a href="https://t.me/Futball180TV/90018" target="_blank">📅 11:50 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90017">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XXdl7BfTiKXNaiEzOl-qu5GMAXAGf5tI1f-5hViXGYB5MUFGZc-9y9PS5zPMt2GAXiO-yTlAUYfY1jtzNM4k2bqoVPqX7jQ6GYLVqsk_SJUt3d8GcbSD5D9MVzJC2s5KPZlUw_HD1_ZKAkpqr7Orc4KNHF61SwQxDPAuL9PEC7e8pyA7uTAs1su6LRwoV2klelCw5V8EQhDF6nsnQ37Kn-Hrs0rIqSzaWe2KF0Ax2Xvmd9C0RBWBLBQsMOZ3IBjGIRp-UT5G1UfViwJRCkX8HbR1EA1ov7C_NGeEDjjGfs8wxeLZDqG2zYQ9izVEG6vZdLBOx2ndFOVRgWCGyekfdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژابی‌آلونسو: ما می‌خواهیم تیمی بسازیم که قادر باشد به طور مداوم در بالاترین سطح رقابت کند و برای کسب عناوین بجنگد. چلسی یکی از بزرگ‌ترین باشگاه‌های فوتبال جهان است و من بسیار مفتخرم که سرمربی این باشگاه بزرگ شوم.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/Futball180TV/90017" target="_blank">📅 11:46 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90016">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Bj9j5AEUxPBQTdnjCUOdU_uOADjAM_AN9LAqWr8llCgnKmPskXqm82gZhBOCQRj6nwA_cKQ4Kf4k-8lzhH7yoXaqtAssehGhKYtrDU_vh4GWK1Duc-EOGUETpyBkyj4wfEXMPOljQhx0vpCXUQgAccAjvkjg5244Y4DLjWXESGX6acLmObTxWSfvv9C4SvCayGr75StwsUSU2a1VCZX26Kxt-bt_f9L_wsirdFEVTFK5R6OnFmeSMYBhQpiffr3UOtHt_i7V1wFJUHlwE4q0gq8ZuvoMSAxEqBe-6y5A270D_dseijU5KgI9hw3fktcx9QnXZsMZ8Ow47NVpowRmRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🚨
#رسمی
؛ ژابی‌آلونسو با قراردادی چهارساله سرمربی تیم‌فوتبال چلسی شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90016" target="_blank">📅 11:45 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90015">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">❌
⚽️
تیم‌فوتبال البطائح به سرمربیگری فرهاد مجیدی در لیگ‌‌برتر امارات به لیگ‌دسته‌یک سقوط کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.3K · <a href="https://t.me/Futball180TV/90015" target="_blank">📅 11:30 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90014">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=ITD46eRlBpFIQQ49j7WFiejH89Tb_nMMV9bjv0zLm9YQ0nJpcwW9Beaf83ULO-V2Sgsa1im9fCWcXBUeyf7cQSySUI63zkYDzKHCWZJka-e1QDpA7Cb8ySd5u5mAaZLP_aPplvec86xZSkSdRfVX0ckfQV45IwprLZTWBv02VIj3xqxJzkDOKaVANUTDKLNiedqryDm4OUL8t3tgvmWCqjK5__iv7US_9NRdckTksSjebJAipQxOSG6_RY_KW6BCxP2WF6LPNYgCNw-1Zi2ACW3_ISelMKk2DHc9a0O16y0hbDLirrMu0-ENZApY2lnQi5AZCMF7K54d2npipcKRew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/553b8556ba.mp4?token=ITD46eRlBpFIQQ49j7WFiejH89Tb_nMMV9bjv0zLm9YQ0nJpcwW9Beaf83ULO-V2Sgsa1im9fCWcXBUeyf7cQSySUI63zkYDzKHCWZJka-e1QDpA7Cb8ySd5u5mAaZLP_aPplvec86xZSkSdRfVX0ckfQV45IwprLZTWBv02VIj3xqxJzkDOKaVANUTDKLNiedqryDm4OUL8t3tgvmWCqjK5__iv7US_9NRdckTksSjebJAipQxOSG6_RY_KW6BCxP2WF6LPNYgCNw-1Zi2ACW3_ISelMKk2DHc9a0O16y0hbDLirrMu0-ENZApY2lnQi5AZCMF7K54d2npipcKRew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❗️
علیرضا بیرانوند: سرود جمهوری اسلامی رو با صدای بلند میخونم و مخالفا هم هیچ کاری نمیتونن بکنن.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90014" target="_blank">📅 10:27 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90013">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TFqjiluR1HskxjY7zc7q4LhUgDx0yjSGbI94tM3urH-9ZN9MkOMsf0Sa1QAaY6bjAESakj4FhtNs27W5BhyY1xnFERglbzHWMWCgIXfarmyQRYnJrvg_-Cda5k6Jc8D7ff6mR67r6xdlLyM242MhdDAj4dttgWWTkTd_KFY4S9yxRB6r4iYU-ZhvW5wKQKQGf2EKacAayE6dB0-PEc2NtnhNiGGCpbze6QF0GnpG0If0xvuuK2H8u1A6T_6Grpg3roC5yXCNletoVtYitRPPlXsqhXm4w140Acz0HorSLteYb4U0nmYldfbIpgH2t3CSvqXwbv13n4mj0UrTWSBb5ms" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c75de85542.mp4?token=bb1SscTNuZ1hflp9QyeyJ7Hx9BK3YmefQ-OlEFYhBkRMxJLoi_Js92A45JPMSvg8jPL-6BhmR37B7pmzzj5XxrnvqZo76zcYEA0i5pmHPNSSUKAmIoHJ8VD3O0NEFIGVA0siM-S9BXqLSQX3bMKZPmaXAQ4g7lwnKHlO0YyqbQThLvI-xuNhTvkYIb2Pcka6U0t1-RdaOgzX8ybrEp9enl9e03M9V3ieye9ijLX8YIBG-9iVAxzJyj5mrbGajYDC5l94hM983e5VP0K0BQ43Sn40ITUlHm8w_YKprwfYHctxCeRleVPpHxXof4B3LP9Y70cIr8Won47__dcL4qB2TFqjiluR1HskxjY7zc7q4LhUgDx0yjSGbI94tM3urH-9ZN9MkOMsf0Sa1QAaY6bjAESakj4FhtNs27W5BhyY1xnFERglbzHWMWCgIXfarmyQRYnJrvg_-Cda5k6Jc8D7ff6mR67r6xdlLyM242MhdDAj4dttgWWTkTd_KFY4S9yxRB6r4iYU-ZhvW5wKQKQGf2EKacAayE6dB0-PEc2NtnhNiGGCpbze6QF0GnpG0If0xvuuK2H8u1A6T_6Grpg3roC5yXCNletoVtYitRPPlXsqhXm4w140Acz0HorSLteYb4U0nmYldfbIpgH2t3CSvqXwbv13n4mj0UrTWSBb5ms" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
عملکرد رونالدو در بازی دیشب النصر
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.83K · <a href="https://t.me/Futball180TV/90013" target="_blank">📅 09:34 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90012">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hw-Ban-C036LnUi_MakeMDdIn5Jw8jm6IjMVdVG4yqNmGiC9vpzR5ozo1DCcYLUB4FPPAHLC-EVEQUJLXJ74QHkT09YFfCxwmHCfyYk3UohnvKEktJz0AxPVTr7ilqg3R0kzxUG2rojYA3LXCEVht9K9_qQARCw8CeB-3Y8auXo9NECuC8Ev3O7cQ61h98M3FyqqAsCAoS6bSNF93q64I6qQrsMWmGYS3mFHiq_jxK1DkqH57Dyf_WmHjCNOz-q44Kfu9koPCRNotXFKSw85rPv9tBsGPiPf314yjBtzan0Ahv5rPOfA2QI4dMIw4A9OAWEwYIO-vxKahXe169hxPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">واکنش رضا غندی‌پور به عدم دعوتش به اردو تیم ملی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/90012" target="_blank">📅 09:12 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90009">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=EQY3494CjcQBo-l97M5d32XuButPB4t1GZINL7jMLVW8wwWI1NW78eX6XgB5_0L_15FuiBR4InKgjjC2C-p_Qx6zVhslTgNSDsiNUupRYmZbT4UTnVuhaQ0bS4huRAIOIYQTVOFvP522gjH8_0LbFfy_b9-GzsXwi921oX6ZGyXNBUwa0Jnd4G7vKU70pFT7fJjaidNEB80raD8MBaW2LmZl81hvIPvuTtHiepe32Hx__QmXOisOjUNo01AJ70UcN4qM2RWqhfVfy6ADwsNqTBlVaxmBSM4Lbn68vrFvpghc4IF-GQJjZor5MY_2_88RRBctuIMZQXV5EtyrOrRP2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d4fe02d07.mp4?token=EQY3494CjcQBo-l97M5d32XuButPB4t1GZINL7jMLVW8wwWI1NW78eX6XgB5_0L_15FuiBR4InKgjjC2C-p_Qx6zVhslTgNSDsiNUupRYmZbT4UTnVuhaQ0bS4huRAIOIYQTVOFvP522gjH8_0LbFfy_b9-GzsXwi921oX6ZGyXNBUwa0Jnd4G7vKU70pFT7fJjaidNEB80raD8MBaW2LmZl81hvIPvuTtHiepe32Hx__QmXOisOjUNo01AJ70UcN4qM2RWqhfVfy6ADwsNqTBlVaxmBSM4Lbn68vrFvpghc4IF-GQJjZor5MY_2_88RRBctuIMZQXV5EtyrOrRP2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اوضاع اصلا به نفع رونالدو پیش نمیره.
🙁
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.72K · <a href="https://t.me/Futball180TV/90009" target="_blank">📅 00:44 · 27 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90008">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GaWM5qhz5rEztHdqK699MQzr0s-A_KFOHteNOpeCGLoC4CKVoY83ymqNIARM5tg6ZlnNMTm6iiyhT0W7SONf6znbT_OmhLqCOn5w3o38p48KLOC5K5Gsd4wGlOXFo9w6vHXODe7gu9ai2BVFXIHjCbDHDIlg9Vw0p7uIm5D8_f6hCQzezok4fSdkE4jo4HF2AYDnsCUzhIGW0xauUJOxnn2lJUtwYuj6XO6xLBjd8gv45SDE0IsKgMDpEUGk1bc43rWH4_hpsynD5jP-AOfO8_2HdEvEASiDUMeItBo2CVe3h6puGyGIObA60dsi77FETyXVmFv6lLwtkJjADTbjag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇺🇸
توییت‌جدید ترامپ: آرامش قبل از توفان
!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.01K · <a href="https://t.me/Futball180TV/90008" target="_blank">📅 23:40 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90007">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mbxzmO-zajAquu-qRR2knPh5vRaK9MSjywjehLh53PPbzR-91iEccsAAtQxRpT7lxyE5t75NnIN4m-iFJOkvHTQja_pqFXuXGA1q_CWFprH8olXhorMhZs_VQnaLGvNMTFf_f-P88is_FH4WslRf1BDugBYI0xdHkVDVBnVR5fSSn-phIR8hyJce9-aIlsC4Kx6-QF1muB30mMBvhXB1J9G7Q2FG7rrMIfs_3udXjvMJJn-fwYCQqFY_N4Q75dE693m4XjydT1iivflfxaGmygmfUBBlBYky7Z-b9uHYnTCNCzOHvSqJe_0JzS2_4stlDsTWG0s8bT3XXv142lUpNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🔵
النصر در فینال لیگ‌قهرمانان سطح دو آسیا مقابل گامبا‌اوزاکا شکست خورد و رونالدو بازهم نتونست با این تیم قهرمان بشه
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.92K · <a href="https://t.me/Futball180TV/90007" target="_blank">📅 23:22 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90006">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/IfYXESSHrg5_C793-2E32FYyPzE18aMkZQUkZPJxnj99S7_MlXMxDOabgJhW7nD4goSrU8i03k2w7duGUCcVVfKNRARUnLvdOfdiMlLzqWSpB0NT841wc-Re_h1eVTlE9vj2Wie1roo1Y6p_mZ4SEqKPlqJC_Xsmk1Thx412zMGsZzfnHYUNnMfKuhFW5vaZLGIOmlfL6QhWHVdVKizmKKhG9QZJdX6rZtMWaZqZTsVGuuchl2ogOBJspwfOeVi88PPDcVJhIALE-Px1NO1wxqwd1QtFmeK5TmI_LVOw0T6phxgAG1PcWHD19qfMPJiIggecqY7AZU3nxey_WqjdNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/90006" target="_blank">📅 21:05 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90005">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">💥
اسامی ٣٠ بازیکن دعوت‌شده به اردوی نهایی تیم ملی در ترکیه
علیرضا بیرانوند، حسین حسینی، پیام نیازمند، محمد خلیفه
احسان حاج صفی، میلاد محمدی، امید نورافکن، شجاع خلیل زاده، علی نعمتی، حسین کنعانی، دانیال ایری، رامین رضاییان، صالح حردانی
سامان قدوس، روزبه چشمی، امیرمحمد رزاق نیا، سعید عزت‌اللهی، محمد قربانی، علیرضا جهانبخش، آریا یوسفی، محمد محبی، مهدی قائدی، مهدی ترابی
مهدی طارمی، هادی حبیبی‌نژاد، امیرحسین حسین‌زاده، امیرحسین محمودی، دنیس درگاهی، کسری طاهری و علی علیپور
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.65K · <a href="https://t.me/Futball180TV/90005" target="_blank">📅 21:01 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90004">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HO-8kowslL2K4UMj7GslEdXuUS2v0YJ0QDv28vkiGNkEW3dMNP6eEajFF_yBhc2l23Ff6z_GyD1cvfwOkEn0Yjw5sRPG8fk2UuYwPylKuo1Lwn8WtgGo16Vd91RJcYDUZbLXD5ybeLZqUaQTr32ApqKskCElHHKh5GdyQKCFtZlD702potb5sZLOrnDAoQuwTbjvcSAeiansdToGDJeEBt5xsUDJg4yh2Cp_Jy8HiUABQiJmdB9fr9-mnmhQZjVOT5w2BFf6tYTS8KBzyQHgqYOJoVZ-9kfS5H9cA5mFTxHEOhxIuW8m-Pa4Kp5f1SqFbgMRZOi7yHq1ofqktljFFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
به نقل از منابع انگلیسی، توافق‌اولیه چلسی و ژابی‌آلونسو حاصل شده است. قرارداد این سرمربی دوساله است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/90004" target="_blank">📅 20:11 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90003">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C2zgFFFdrzi3cDy2BlF9HeYFVL9yzIz1D1_EcQGileOjhwkjC_P06XGSHDsWHnp1G9BxC0cRgBw6v9ZWBF76g8arZIB5zSYzqZfvIliihdw6uiqjPAXmsTEQvMgVWMEqjFSDHVIl_uM6zXCrrTFUlKMN5B1hTR1Fkqu_2dYoSkFzqugaazaaWnCHhBy2fY7Jsow9kMuP97xQkrl1MuEe75eA-vGwpAxiRu3Ynd5fvnW3RUBNY_Lsj4saCr7KQF0Yg-_1vszh1lnBnlyPKnyWQOsWE6X4SP_eCY3ge9ZKs8I-xySCY1HTHepHxNWsMmJqO5fa8pWSqENFPfqgJcswiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
پپ‌گواردیولا طی ۱۹ سال ۴۱ جام کسب کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.31K · <a href="https://t.me/Futball180TV/90003" target="_blank">📅 19:56 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-90002">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cjashk6UthLnf-Umn3WrQfDTugPM5O0EytnZGYYuDTkyP21BJDcwly_B2DNNpUvu7nhQ5HoWTjRnp5pFZygcm96sCKq5q7XCXCnRoyJiOeR9VvsIAkeVDqURwqGlGoislQ_vp7BC8cK2QMihuZAT-K2tRapDCR7I6AvLysweC4lvMfNwqMkh9esH08ZdDtkyaEaTvaHuvSzJcL6I5ThLkT2HHbTGDr7d9FW6zWB7tbAw9U6Fn3YDrmXCdD4FxMrj-FFWa1MNISjPj__0xG5SurpytgGvAK_dmUXudPpo9NBcIKnVbTD2y93IPNsPBWFjUu2Cr_tOa1-hzZFINx_ffQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
منچسترسیتی با برتری مقابل چلسی قهرمان شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/90002" target="_blank">📅 19:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89999">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Waqumvmqy4u2SVMFKrU1rWhSKNJclXFALs9HdqhtZ9xSIgTJedkyeCMOhg7kziFfAs_SDH7fSjx-DmrCCbwWDE4C3-J7eXqUWWr1KyBtjquvJMavPgyRkTlIt_25Et9fkWBZ5FHHfC4r-08CopssR5GFy6gnSEVgmRzy89jAUBsJtbDdoEWzORx9_8JTIjS3aSlJterKDSkvbj-vlexB_OGoCUuKxiBinwJceOVVLNBFa1ARJL1-DHfpDs7NYCc5T9gW9L4K-snCCJQIp454Cmu2leupZ6SaxIbnR45vaMMZZJZqHVrsSezXL2UsSeyH9rojGmIJDs1jEzdDVmPphQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فینال جام‌حذفی انگلیس؛ ترکیب سیتی و چلسی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89999" target="_blank">📅 16:34 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89998">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Py2SVrxdDPhT6_eSUHHM4MK7AM7m1UvHWKMUlQBCeLtVjKkWqpoRv8gzd2qeAn7mkeYA445eUsGQJF4hwVs6iNdeHunKBI4WGu9ia-p9ZvpTmG9X3apbPxHHQMeXkMu06dsvlUa-vMYZW2J8r7Rdc2dEjvhQAoqbjdHZ8AJE35oOX3DomO-RmIrRcL6hvCtW7-muo69cHjkFivJVTOEQXBiluWV99oh9bXfLd15XpqZoExUHX3EKNn-SEEvUTiKaLyd4Nw2PCg70pqNMVSrc2AeGDUneqXqC8HJR85V9xlaLoZVX6AmJzolsd6k_qi0010jM1byg3HJieMj7gYzMsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇨🇩
فهرست نهایی تیم‌ملی کنگو برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.08K · <a href="https://t.me/Futball180TV/89998" target="_blank">📅 16:25 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89997">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWRl88-W88MYuDJaXI6DZ2SQeTYbu4BLb_g5CH1Yni2-i_ptitvOZElrAQYKkaz2wBJBc9GySWXOwKmZ_yiftm6YeKJeIss-pW33NJjHD_XM1-JtVZK9t_tPHEXSeJqiYXvUmk53zrw5kv-Jtq-yBIFi73seBh1BN0wtcJjArI0UU7bp5LsaEDu6vTKiD3qJVrIsSoFzU0lb8o_XQz55j-tqQtqJk-pJwrM7wt5Lt9l8dh65wwQFSo-Ki1zkEy-ZugMlSmq2UBnf9k059g2Skqqymv3Hw0Q_lnLiOpA4UzBpJ-pAl2iIVryG-0AdkJtjEhJJXs4GVTqbmJq4rM33mQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پپ‌گواردیولا: فصل بعد نیز سرمربی سیتی هستم
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/89997" target="_blank">📅 15:37 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89996">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e01b819c41.mp4?token=Gix2jZCngEVkSo9-VQAZCR5D234SnP6hzgMBDc04fVTK5SGWS3goIlbhIEaIvsvrqd5EoON43Evd8HA_Ii3PbVfTBbIT31ZD-rbUIRXL6PGKDdS1swswXRdrveOxhDp3H_clqVvJJN4f8QByrpajOaC1yf-fMP32ETD4uf4232tQ8Eae4FAY1Vag00UOFRzbQYS0YLpGOX35ApSddg-oDqdPjEPM_M0eYh6DRj-gS9nqTs15pIJkc2QAQs9bvu-4Eg6xMkvfYccJpWnokr0l7pa9aBxa7sqpgl-TvwMjc9XL5ZHH0gDcZgrNS9onuwFsaFqIL6cmvzQ0eTt9CJpOHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
📲
پست جدید لواندوفسکی:
بعد از چهار سال چالش‌برانگیز و سخت، وقت رفتنه. من با این احساس اینجا را ترک می‌کنم که ماموریتم کامل شده. چهار فصل و سه عنوان قهرمانی!
هرگز عشقی را که از همان روزهای اول از هواداران دریافت کردم فراموش نخواهم کرد. کاتالونیا خانه من است.
از همه کسانی که در این چهار سال فوق‌العاده ملاقات کردم متشکرم. یک تشکر ویژه از رئیس لاپورتا برای اینکه به من فرصت تجربه باورنکردنی‌ترین فصل دوران حرفه‌ای‌ام را داد.
بارسلونا به جایی که به آن تعلق دارد، برگشته است. ویسکا بارسا. ویسکا کاتالونیا
💙
❤️
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.28K · <a href="https://t.me/Futball180TV/89996" target="_blank">📅 15:32 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89995">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CKwHkka9AgeyjrWgQE10MvqbKXqPhjv6v0ShJfBb6O_I66WX17tDY_wH05gpKenfO4oyld4NYVp2gNzU-wccSN8WkOK49l0FCcvzaO6wHS6pM4QZya8ivUHaCK5DO-GSNUP3B-M6aavTcSF4_X2iOGdO7poNMkeF6gzPl1kWTPouhdWAKiv7-o-Or8kDJxZw702XJuMZd4MfPk7V39xGWE3FsVyAaoPKcyX4TQsJmLunMD55DVUN26H2eiw1MzLspYdEDgHDGP7WBCmcILsrHCo_sIc3YMy0feFSiw6VAitrYTqjZ7ad9mwcFdbnubEA1Y_jjioeCzX7UcMVcBzrRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌐
نت‌بلاکس اعلام کرد خاموشی دیجیتال در ایران وارد دوازدهمین هفته خود شده و اکنون به هفتاد و هشتمین روز رسیده است که در سطح جهانی بی‌سابقه به حساب می‌آید
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.11K · <a href="https://t.me/Futball180TV/89995" target="_blank">📅 13:07 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89992">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u1aBVLfmAcyyyQBhjNEfE6uIobhkzpCNwqacpBSTzf0jRLtPeGBtmb_XHKhHMnz1T3_aDDaloA9cnW99P76EcB8Pg91a0LCwnv3Pu4urRsDdE9gVWd0wd5epkB6jMqYJO1Ybc8uFz-SQLnuNYL4Ih4Dmi8KeBL0kq6X1axxL7XyaDCHG28hLxIQO4tujI6Y5fJenbhjNA3v1L58uBE92J-kTozC1yJGuUU8MyWGaGP8GBrttBPmmdptJ7lN8RUOYcUaQ-hINj4EywL7Vfy0jMGEc_2n24MM4MfoPNAAbih1oWySAkwfS6OADWT7lhc3BUCUNu16bfmP_U_bt9Jn5mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
⚽️
تا اواسط هفته‌جاری انتقال ژوزه مورینیو به رئال‌مادرید رسمی خواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.93K · <a href="https://t.me/Futball180TV/89992" target="_blank">📅 12:57 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89991">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=q2xjQ-loI5wLVFYPfkReqRdHMM4mYtbTlgfYDYJb-iUyeX4Dbx3mJIzTkYYkrTTExmfWiGtFmBuEN_WJMEYd45gx_CqjL3FyrZF-MwRp-ili9Akj2G1fv7aHq_Pjc1uU0ai__RuW9T2Gcm6nR1ziJXjLyPr8vIGWgYE0uQkqScOYiRMb_42QzhF9wbqoaCkanuxla6zOfrQxnFKv5nDe32XXFGaiWxNWYOBFZpIlSam3oSRNTRdE_u-7N793wDTfKRmSJrQbLzVD91PhvOwYpRkq8ujiydC_ngbFZYJCBVY4CrJfyFxRYNT8_CTFKpj9mOTHNghvAc2y1vTmG6aFZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcdd85ad92.mp4?token=q2xjQ-loI5wLVFYPfkReqRdHMM4mYtbTlgfYDYJb-iUyeX4Dbx3mJIzTkYYkrTTExmfWiGtFmBuEN_WJMEYd45gx_CqjL3FyrZF-MwRp-ili9Akj2G1fv7aHq_Pjc1uU0ai__RuW9T2Gcm6nR1ziJXjLyPr8vIGWgYE0uQkqScOYiRMb_42QzhF9wbqoaCkanuxla6zOfrQxnFKv5nDe32XXFGaiWxNWYOBFZpIlSam3oSRNTRdE_u-7N793wDTfKRmSJrQbLzVD91PhvOwYpRkq8ujiydC_ngbFZYJCBVY4CrJfyFxRYNT8_CTFKpj9mOTHNghvAc2y1vTmG6aFZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
آموزش‌مسلح کردن اسلحه و شلیک در آنتن‌زنده!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.68K · <a href="https://t.me/Futball180TV/89991" target="_blank">📅 12:53 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89990">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXTr94oGN-s-2dXCl5tN_rMz6ao7zOa47CWuF2qy9BTrxl1qPq0_NXsBoJS6VoDdWqSjvspo6UrvpifvaceCLekDvcLBUu8PpoGNf78Kws831wOnRY8iyfJJb3tro0lOe1PZ_IEDrJ5Pw3B7ueQllhFK9SxB4US593elSSSCK7UX4m3fXrLN7sRbb7upzkvKIDns4ENcfyZyOZaK07fSTyIfzEIUi-ZHgfW9OJhtZRE_iTMB9UE6Fp_VNndWhD6uRNNOnIiPOwFntmOLBW04H-KvyqUg1DC8bMzyXrA_PVWTzlR9WxsMWVxhb9yabUInbPOnFZ7nEaItkPBA6hzhvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
هانسی‌فلیک با ماندن رشفورد موافقت کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.96K · <a href="https://t.me/Futball180TV/89990" target="_blank">📅 12:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89989">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VWuYSfMgoMeHV9GPXLsqfhp8JOdw6lKQbOlZr6WaCGmMAHcdwcQmza3p2y7DB_PCnh--bbbGcrtwkwVZ6V5LPdSdhOtlJ2AziV2LPRj_vlq-Tt_ZmBsWBqDN0k_7mrpkpuVBkByZPt5RAVmtp9jKyKB9jjRCpsdbb8LoDiQ_R3jHDzKz1UdrDpdUuDlV0grcodXt8FMJUbXgp3Rg-iDX_LVrGQZ6OnfRPyzXTbSpcHzxSwJbvnuX8YCyMDJ8dsa6MNnd8103C1xbeFUrBYSz9tyEWP7F1HqM9pWG_iykWw8de0vJ8GwPIgS5GHkheDbAlbzCTJ2-RT2yHdxli-W18g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇰🇷
لیست کره‌جنوبی برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4K · <a href="https://t.me/Futball180TV/89989" target="_blank">📅 11:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89988">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fvliiDf5ms242bM4JV1NXkk-W-ADuTqz-u6Ow8yiYtjwCzdJX-S-OyXgDzHvDKndwAszKu9ZgPaHGbPPMO6VoR21o5AnLKS_N62qj-V0Nw-ggYlgEgaY5vOpFD-kvOhi_Otwnsrq0ze6DPuYbMgK4wYKLIitSa53wvrERu3HXzie5i4GKJ2AYkxO6uXlJIPC4w3hgqCZS7CfzP9dBsYywJ-waMklWJIkhabKalDz8LCGv8lC7eMMAl0FCs9EglwNjfj-PfogSZF-a4em7CwtVraez3PQbsPG1XLCNq5iIi_UzoT7cnw9iOqTnPp47RRrajRnpxl1WYPBGoBA-5kTTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔴
وزارت خارجه آمریکا: ونزوئلا 7340 کیلوگرم اورانیوم غنی‌شدهش رو به آمریکا منتقل کرد!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/89988" target="_blank">📅 10:14 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89987">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">فوت پدرم باعث شد از آلمان برگردم/ کخ سخت‌ترین دوره فوتبالم را رقم زد
مهدی پاشازاده، پیشکسوت باشگاه استقلال: در اوج بودم اما به دلیل مصدومیت‌های پیاپی‌ای که داشتم، وقتی خواستم به استقلال برگردم، آقای کُخ گفت که باید تست بدهی و این برایم خیلی سخت بود.
به ترکیب استقلال برگشتم اما دوباره با دو بار پارگی رباط صلیبی لژیونر شدم.
کخ مربی بادانشی بود اما اطرافیانش خوب چیده نشده بودند.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.69K · <a href="https://t.me/Futball180TV/89987" target="_blank">📅 10:12 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89985">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jzK8OrY0CkKnkoXqZxbfcsh2jUWbsBLU3KENf_NEQ4KAeBK2bsmu-JxenUWtgaZwRnHsoExlQi2MowRjOiopJVwO_v0fadjCZsNR2TYwmnMZWIsL-5YMTTXKohkxXrXV4v5KlSI19TBwZLU9kNv1AIQ7kGq9LIm-vX8q4btMBPA3QVdBDlna5J-CTPRrp_iLCsGaxSYGvYgplNJDR6q74XJWcB10C3hqu8sQsboPDr2GEMY5B653D9bwWnm1wmbCpLasRNVwhXDH1YUCOBTrHqzIc5O093r8TEwMT1EZFboaqxtzIT4UnTRLCnHfXtTgDFKxKugRVu24rPNQ8TXRtg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
ژوزه‌مورینیو اعلام کرده که پس از پایان دوران حضور در رئال از سرمربیگری خداحافظی می‌کند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.72K · <a href="https://t.me/Futball180TV/89985" target="_blank">📅 09:47 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89984">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">💥
🇹🇷
جشن‌ویژه باشگاه گالاتاسرای برای ایکاردی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.18K · <a href="https://t.me/Futball180TV/89984" target="_blank">📅 09:19 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89983">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Kqpmdbu8MERoxP18UvoLDCvwkxaw2MLWcc9DOl_6lzw2jm782oFe2yqdhNz9S3XJF7ycVarStumaySP0iHOpUmO9tE2IBUENUPisg2q7WEgksYalowkNpeh_8X5UalYIoEvSbx_vOgztFsV2QeqFTUNYLYQkmfhcP5TEdTNv00CKuEBCLIeSx-UweISRlX-IWASW3lLJCut_jdgLUdmZW_CYPQPK_E5zA-AyIz72PaufaDUrAYMW68I5g5k0koSjf2nP5b2f4LBId2yzNpoauedW6YSPcG5HTz2sTq4nMPsSzDdYk-s_o6tTaFYp963Ol3b6t-mN3_2Lr_3fiYIWwA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏴󠁧󠁢󠁥󠁮󠁧󠁿
مایکل‌کریک سرمربی فصل‌آینده تیم فوتبال منچستریونایتد خواهد بود
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.02K · <a href="https://t.me/Futball180TV/89983" target="_blank">📅 09:03 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89980">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rzFpqgAExztETh7cAMjVYCnqg2OcNaxny8u7NPVElLUN2lKUXYiOb7iu3NhCfo9_M8EQqKV0gcmp_bW7nk0Pg8LQM_bzrh3PWIW6eUccqp5hfQom7y2CtWE-GwAJeROOowQEW2TyugejUo5z-yjUu8hs5ixHFdZ4KUFY4exhaxpCeTKyHDaGGP1llu7zTedrvDvRydOsZHMUC5-UkAuSXpsI-bfL3R8zSul4GQJ2ftp_hOOdsNd4NEc1jI2kW0izNcnEJe06KsfGcrCR4bKbrkZH6yS8n-EZGxnvo250lYuJk881UVkv4NwTmJrMhCP4Ogc44NzT1ZJdMMYfNqjA8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
استون‌ویلا با برتری قاطع مقابل لیورپول سهمیه لیگ‌قهرمانان اروپا را کسب کرد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.23K · <a href="https://t.me/Futball180TV/89980" target="_blank">📅 00:28 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89979">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I_baZozZtemseUF1Wz9pPX2Zel9wFbu4YA7yAMTs1eJrufUz8YB2GOVxVwWU5MYGUeLEh3zAXDFcEjoAtJDazfGXMccoO3IwQggayDRiYVHpEp16SHFj41QeyfpCLZo6VIwrHGIJyIDBRvLyNeGGMprDsAw4srsJrsCjn_1qMYe1LMYSTqiCpvao3eVxCy-x7nKsxbYQlRHs7ELH4QTFq4LV6e8AFY94sOmXN0BUInJJDmRHsi6Aokjx5XjDd9Lx0uukiy7ZDNpC6wSoPJ0HDsEwoE7lsGGl_720Sdy2Moy6nD2jYnZ1gEFTxKibVnYH6aKcsXgZiVnyJkFnk-PI1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
#فوری؛ رسانه‌کوپه‌نزدیک به پرز: ژوزه مورینیو با قراردادی سه‌ساله سرمربی رئال‌مادرید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.54K · <a href="https://t.me/Futball180TV/89979" target="_blank">📅 00:17 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89978">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🚨
‼️
سازمان برنامه‌بودجه به دولت جمهوری اسلامی اعلام کرده که با وجود تورم شدید اخیر، منابع لازم برای افزایش رقم کالابرگ را ندارد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.47K · <a href="https://t.me/Futball180TV/89978" target="_blank">📅 00:15 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89977">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aPdbb9xOoFTGJTv9VVluAcq0z8daslN1-pwlOPgT-dWQlqyv6BGWibpd_HM-9LMYFou9-2aQnLKMGIUHLpAVS0WRphIyH5WOqXRlHxd8YM9qogn10SAJGs163pxzQz8aohtBQlvnoB-kdqAiZcgdmmtIlf91n3iGbsGklc1_Z7NNTUxWaGd0zFP3jLHVFvDIG7hr2q1ZR7ugRmHnEt-LZVZTst3_pmpkoNDqfscJPFNHcpIwVXJhTZnOjg8hukB64cv4eRrX7SElAtu1n__HLljNXNlZJ4mchwlo32JQgry0NHH1oGB4ZYMCcFNO7Z5VbHT65N_wSwHdl_OhDKZw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇵🇱
تیم‌ملی لهستان از برگزاری دیدار تدارکاتی با تیم فوتبال جمهوری اسلامی انصراف داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89977" target="_blank">📅 00:02 · 26 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89976">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rG1jIVHa39CkmNBx45dD0D0XWFCVkLHf65sY4RCQa7zggLDkDvc1xrHQlukHf6jZHKchDjO4L_qaZXCUiymzgDlZCTMbOxlxPHFGO2Uy6GIzxNIJy4gUZ-iqwXISn8H479yRHwMKtDOUJmy3OdPlEZDVIWoOrfkhLyt50nVRJuq37DMJWX-9W9dunItUqJXg8bf8InUC2iqkMf-_u-C-S7xYmXmXqEhUobOPj_1DJyorzzj6-FIgCVOL08Z1z1m_2KQKOi-Ir6C78jg5zPc6W0wUZHi2aiDbd5B5TghT7wg1ailUf0Q03qXY_prP60VbnorQGHqmWh3kHeYl4yub-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇭🇹
لیست‌تیم‌ملی هائیتی برای جام‌جهانی با حضور داکنز نازون مهاجم تیم‌فوتبال استقلال
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89976" target="_blank">📅 19:46 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89975">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DYC8ohVdN2V7DlMwrn_NhHW3zFI7Uj8FuQHarAKr0F1AIsr_tIZ_eUvmzCp4_hadQ4C1DyoDxCTzGxhJPgRBMeLsUhDxzIAGjmadJshdOJg-zZYxkmG911zUCnO6tiJZeSnRfozsP94Kr9Z5Qgv_V6tZWoxZCn_-ddMpCRjWQ4BUrNq3U3chqKimZatTTjx6fgjiTsV6WiFO6HMYyx86Q79Why0JjLH6ODkUgixSRVef0md-KlCKVqOi5RAhbTPi_csE-E5QFYn0Kvei-oqdxfvWx7_Y-ZCZ1BRBIOMZ9drBmDgEeRgJ_BRy5ltzT-TFaaO3oSE-wMJQywcnyvzLIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
بهترین گلزنان تاریخ جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.34K · <a href="https://t.me/Futball180TV/89975" target="_blank">📅 19:45 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89972">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/myFvDEve9L0qmt3IvwHcR2Dkai8ZbWHmpj2Al1azgS7dFqlVXJSxWDSdY5oVDOx1ArABsocHxoJd5RCNhSTK7Y8WF7y-OeLOdQlr3R13Ya4Pr81zHInOunhivi08LYq_gZkMynFJaSYhu9Kj7dViHankp4mpqU1X_Mr1ckgKB3AC2kBVS_dUmiS9q9Y-XQQH3IbaEqvc3rfWD7PtHnc2G8SdBTsc4vrDKHok50ctQFU5P0RTVTZAJCVV6XrHxK3ZqJpjP6wYF-ASN5Itmwh_70pFnoofLJKXLwLetWwIBvwCc5aI4z2ZyjcxKhiBLfWh4iAY2vSyRayGdKxuLvLCCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇮
لیست‌تیم‌ملی ساحل‌عاج برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.62K · <a href="https://t.me/Futball180TV/89972" target="_blank">📅 17:01 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89971">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JKy6oZCAP4QfNMaPYmo3doiZMjJeMgojj-b4Qxbwb0aHYffm_j5A2lLgBQE40GBZuS5KzObq1UWVuDSw61leEVzduw4utDNZMICZoOO9jOyY_Uak0TKsW-xqEJmLsz9aKMkumZSb_fVKMhV9KOlmF9lNmL1lZoHRlJLxXG5yD_5GgULVVAVr4F6Cz5JZPfSmbipOfZCfmGDLul_UU5WZAiWMHMUHF5VFbzs-_5QZDY6OJj65NjrXC69Bqu1KAkDc7f7IvOsImY5NcAUYYNwen67zetWG_kaDhHiZwRnvAwCNUDzZmVcL8iexVdZCgXwodcU2k4nMAMedpzPbPsll2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇪
اعلام‌ لیست نهایی بلژیک در جام‌جهانی2026
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.56K · <a href="https://t.me/Futball180TV/89971" target="_blank">📅 16:51 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89970">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🚨
🇺🇸
فوری/ترامپ: من با تعلیق برنامه هسته‌ای ایران به مدت ۲۰ سال مشکلی ندارم اما باید یک تعهد «واقعی» باشد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.79K · <a href="https://t.me/Futball180TV/89970" target="_blank">📅 14:31 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89969">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8OGfzHPOApn_Rj3WQvhOKHl4y1tYu6NxyyAECtJSLDmwDhmfnWdGJoEuCvrtgxs1NyhZVIYKZbqUX7fZjpEAB4AV8R6jr6zStdQNn8qQszBPpmVTAvH0VW_5NXxrOsOPsGlUIstrYQN2fe3i7NtswVWmxDyDZx7SkW8AUY9U-fDY9qs2eNqP7ComkMArlD3UvcVWuNuZzrW1kRS9o77V0eStnp7TIgpSyCYf6IygXntP-u-D4BTMrrlY8Zk35miDvNMgETDNgp6qw_9oBhd-YecvpGS2Rcuypmc21mSXp1TGAve67HabQglqT7VpKyGhgdgFX_buyeaEoTUPafj2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
نامزدهای بهترین سرمربی فصل پرمیر لیگ
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5K · <a href="https://t.me/Futball180TV/89969" target="_blank">📅 14:13 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89966">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mOj8bPV8hf1OAPT_Z2S_beIeY3Oe93ZWcH8oNybLpXXnOcWeyGS7C9mfp_sWtf2ATVFogKJ9vrSROVAFDaKZB6waA7cXJKu9msDGuWDMrq-8aRkkDxUOG7wBAStfttgqDIHTv-UBFKd20y6YpShiMhWkPca2WkHiGIcSBEpjVRsCjNGIQDhESZ2vwqXQ-N4FYLAcsCK4oR6zMQj1Q-t9SY35j3luMcO5hlY4JVPSTBZZ1hBvGeibsTJAMjBxxUWBfUhrmem3OAY7VVYb16w3K1YOW5CLK7qTTVGpKWe0XKjIzu-yI3-0NUxJLxfpC_WFOWtWCpM3WzRfEe-WjtUaLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇺
کوبا اعلام کرد رئیس سازمان سیا به این کشور سفر کرده است
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.98K · <a href="https://t.me/Futball180TV/89966" target="_blank">📅 12:09 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89965">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BE-HH4sdFG-fF2jq659hrobUvn43UZzX_qKAVJY4746AOkf8UAiBa-gnvQtxt-k7HGi3hLzNQTU_x4-frxvvLPKrfWq9zMevuQvlk-HeiSTB5AWJY7XUOuvv6rykkY7R2mdHH-11aXFWFFrk20YnBTMg1H34xQFiPmlRAXvXhpsWpcXUH0vOPCO7GbEQ1tbdiU5gCCXvuRZ0vHDohiYJz33N2GOaiTYxajOQDoiA5DomkkaIZUhrFzcFg6_zYl-OjsKvo_DojHES9W2bt6MKrMqvHW7FzPu9jBk0MZ94IriSDQGtTOEy2_dmWGA7AJIMhJBOQJPL6CBTj4j9uTYVRg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇯🇵
فهرست تیم‌ملی ژاپن برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.9K · <a href="https://t.me/Futball180TV/89965" target="_blank">📅 11:27 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89964">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jVTUU4zKqOirHuHCzynQQ9-jbCNu79dGCbty6KDvPKRLwccGPEnaSgXKJxmyOPVktGaelbZ-HM-zvlnRAob8gmzwcYDpDYzDO7rtgVbqjCbEuW2SFmL5474zvk6trask9_xza8NGxVeyaW_IQmfOYnnxxPXAdvUkOMN4t_ex54HcF-A2pB6PbodWhbxyM_OElYc8GgeKK1RBiwj4tJ7VRoHKtPo9LNNwB6ZqtIPn84Dej3u0L4JfB6KZkRVeTzwacmY5qfpRb8oaUd_1jvG45OwV-oNmdTuUaD1FS1Hunw9cTdbOjpwhMHRvlmr0dpBE-Ij6kyVdmpzLmpPOf_kR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
‼️
امباپه: سوت‌های اعتراضی علیه بازیکن مشهوری مثل‌من عادیه. آربلوآ بهم گفته که مهاجم چهارم تیمم هستی درحالی که همیشه آماده بازی کردن بودم!
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89964" target="_blank">📅 09:32 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89963">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🚨
وزارت آموزش‌وپرورش: امتحانات پایه‌های هفتم تا دهم با نظر استانداران با توجه به شرایط هر استان به صورت حضوری یا مجازی برگزار خواهد شد
امتحانات پایه‌یازدهم و دوازدهم تا تیرماه برگزار نخواهد شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.78K · <a href="https://t.me/Futball180TV/89963" target="_blank">📅 09:28 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89962">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dVy8noIz0rw9LFW8NwqLpPeMxVEn56ol3ztKnQe5uIHEFDsPEr_WERQwkZv-vbnc-lRW4g0w4Jsve_yJED9BAdd_GPDo4vYb-AYEP77_cz14mU4njIebDR8Gtwzueme_-6VmzzOGLQQRgHuNuQZ7U0fI8pgYrozMKXmahz-YPX2RS8LcE7pUW59zkMqj5aI3iHI3kpD4Bjj-uCfhff0kf-FADOEaNIcdHrnpkINBXWY9mXCY6TSZpKyDtKKvolrCxZ9SwwoILdZ_58brzkL9AGIQakrk2B8Q4zEYYAdH6HdFGjQmo85mPi9JSgCHoSEK3u3EU8b4QkBnjum1UPhOoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که بیشترین قهرمانی در رقابت‌های لیگ در ۵ لیگ برتر اروپایی را بدست آورده‌اند
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.89K · <a href="https://t.me/Futball180TV/89962" target="_blank">📅 09:12 · 25 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89958">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🚨
🇨🇺
دولت‌کوبا با هشدار تمام شدن مخازن سوختی خود اعلام کرد که برق در سراسر این کشور تا مدتی نامشخص قطع خواهد بود و مردم این کشور در آستانه شورش قرار دارند
+کوبا کشوری‌ست که اخیرا ترامپ اعلام کرده بود سقوط سیستم حاکمیت‌ش بزودی رخ خواهد داد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.95K · <a href="https://t.me/Futball180TV/89958" target="_blank">📅 23:55 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89957">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=XzLK-why-wDJb8bulZN9DwknnK5gaRVu4jUGLqQalQXdUToWzVNiWCRxNA98dnmUs8qAxqGd4PhemzZpmb6C2DAtQYQ3vf30P-E3EuF_2j5-FSwfa5ywxN2068X71FIjCTfsr5kucA447j_E3oYIGym2-YH5u5wPO9_yhFcjgYmnkRaN2ply8hXrsl3pk0w347zYzqToXw4Zt7Dn_hgIoo4frd80qc5wUtU-JkqpyG9rt3eHqOmomAvQNXT9gEN2JwPaO9QDv1RVWOXkt06VPAvUCMb2ia9kNHrhQ20VwWVZw0dzevvsWw0ZpDLPWeuIltmWW0m369NCJ03cQpcjh0mNmIBnhZr3vc4OIFQkI1xI4joUDpkb5w5FI_-mYMZe1oyfP2-y_DrKAsAbUgHN8yjzRrhnGk0CyyhXdr34zZG171xkBh6iUiXEIXkWwkVBluQMBoWa70qaBIfphzzFgxYeCesiNWt1GfbL_SlIuzVPTL-wfQiiDzLYFKfnheEmEa-BWUIKHGsX5e1QMzqZVay6HcHE9yf7JeVefm4Fy2N2Bv2n2rWP29se72UuhN67231WI7xSX4ENvV_47XlCy-FFg8gSdLShkuBpL1sYv1l3Zpj_xau2ousQTUWNxUfLux9OeEzCH5ta5f3esc79pruwFW4cRFvTkEMhjd6zovM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6579d2e780.mp4?token=XzLK-why-wDJb8bulZN9DwknnK5gaRVu4jUGLqQalQXdUToWzVNiWCRxNA98dnmUs8qAxqGd4PhemzZpmb6C2DAtQYQ3vf30P-E3EuF_2j5-FSwfa5ywxN2068X71FIjCTfsr5kucA447j_E3oYIGym2-YH5u5wPO9_yhFcjgYmnkRaN2ply8hXrsl3pk0w347zYzqToXw4Zt7Dn_hgIoo4frd80qc5wUtU-JkqpyG9rt3eHqOmomAvQNXT9gEN2JwPaO9QDv1RVWOXkt06VPAvUCMb2ia9kNHrhQ20VwWVZw0dzevvsWw0ZpDLPWeuIltmWW0m369NCJ03cQpcjh0mNmIBnhZr3vc4OIFQkI1xI4joUDpkb5w5FI_-mYMZe1oyfP2-y_DrKAsAbUgHN8yjzRrhnGk0CyyhXdr34zZG171xkBh6iUiXEIXkWwkVBluQMBoWa70qaBIfphzzFgxYeCesiNWt1GfbL_SlIuzVPTL-wfQiiDzLYFKfnheEmEa-BWUIKHGsX5e1QMzqZVay6HcHE9yf7JeVefm4Fy2N2Bv2n2rWP29se72UuhN67231WI7xSX4ENvV_47XlCy-FFg8gSdLShkuBpL1sYv1l3Zpj_xau2ousQTUWNxUfLux9OeEzCH5ta5f3esc79pruwFW4cRFvTkEMhjd6zovM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
روایت تلخ یک تولیدکننده در نشست ستاد تسهیل منطقه کاشان
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 5.06K · <a href="https://t.me/Futball180TV/89957" target="_blank">📅 23:36 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89956">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qkFZ04aycaVLwjFfA30-sRGZNqwVbazxjFPDoXqdE5tlIQJBnnSSjpaLTuRHgqMoRZUaJc2NVZIXWbIj0qSZnJ9mCzfPWJu2nb4RjCKVJgqrJSUo5rJf3vAJLd0nt8BHyD6a-MTcouRq8W_3jgpP4_71a4GdZZF0sQHqw1w9dcX0jH-fiEA6kzYcWFpUcG0UPZ8E3L3M94rNoVuZE5GU_76OZva0XDk2UarLFXzM6ugOwsLW9Kc8ufkcOENxX-rrgJnT7EQ4UchH4uhr9MO4dzjc7N6j71-CUXcdYp6HU0L2dlypu-d2z02ViADNL_zV3JXDP_Eket0Ic_AtiP2yRw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇸🇪
فهرست تیم‌ملی سوئد برای جام‌جهانی ۲۰۲۶
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.71K · <a href="https://t.me/Futball180TV/89956" target="_blank">📅 23:13 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89955">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CMATXIOem9BBuAL85fE3aNXA0da21Ip5Yb2R8mNaxre-MGxfEXoskfQ9I32aloIywNBtt_f6weLktisiEfxKXem6VKQd0ar1793p4rbYG6_xxGeELlBfNXZOeX7HMbjh-lZ4F7O1ul6Cwa5qshn1AxcLdwtA3DnfDsw8voGY32ihVvBWx32mzLSzFoRNxtNbkMm9JTBnZ2ysKzvfi71wlf04OHEmIYlqo-VcH1wRc6SdrzXHEVmGaFyufrF0kvSPHHFbMCQc2XnHWt4VdWoPYhX_ybQzTHJ4qOEPulwEELuMUzEgIIUx7PUaHOC4KoEQrGgyujTP3HAD3NmTzJ9lOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
لیست فرانسه برای جام جهانی بدون حضور کاماوینگا
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.82K · <a href="https://t.me/Futball180TV/89955" target="_blank">📅 23:08 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89954">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=MSQ1YXK4h5Mcvl-2YKJSzAiQLrceOY4CKr_44zHJ16pDTo5v8vfWlFkOG1exNJOCZxBJZzgEKE7tedrQ6t3ynRikt0gThbkc2IHrWZi2eLjffyf6Z9Uf1b2I192_Llsr1zqYe9yHHKFh7U5rEeB_oETQVJSSkaCY2__XKH1OUdEHVRYd4YsY3Bkk-uXYokYt6L9VbMyJ8c4Im2aCgarBpL25kmrFtynZDHbQDuOhk1vcOZRuZiLLxL-j6HhIn5JNetVAleYqhSWjgEbdDZN-BaY4b12rR_eJ0vJc7Sv5rFVQ9N99T2OG6lPs-ADF8ObZ5Z9wp9uGJOsRGxLkCb0zpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b7cda28878.mp4?token=MSQ1YXK4h5Mcvl-2YKJSzAiQLrceOY4CKr_44zHJ16pDTo5v8vfWlFkOG1exNJOCZxBJZzgEKE7tedrQ6t3ynRikt0gThbkc2IHrWZi2eLjffyf6Z9Uf1b2I192_Llsr1zqYe9yHHKFh7U5rEeB_oETQVJSSkaCY2__XKH1OUdEHVRYd4YsY3Bkk-uXYokYt6L9VbMyJ8c4Im2aCgarBpL25kmrFtynZDHbQDuOhk1vcOZRuZiLLxL-j6HhIn5JNetVAleYqhSWjgEbdDZN-BaY4b12rR_eJ0vJc7Sv5rFVQ9N99T2OG6lPs-ADF8ObZ5Z9wp9uGJOsRGxLkCb0zpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
کاتس وزیر دفاع اسرائیل  :
ماموریت ما کامل نشده است.
ما برای احتمال اینکه ممکن است مجبور به اقدام دوباره شویم - شاید حتی به زودی - آماده‌ایم.
اگر اهداف تأمین نشوند، دوباره اقدام خواهیم کرد.
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/Futball180TV/89954" target="_blank">📅 22:43 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89951">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nf9HKpp7T1Xei3MbhuvEz8CJN1SjbYI9KlyFSSar0NueOwNm4ezoozM08l5xbtDyV3nkxgF4L2uiKn9CjNGTWPd-pz9CzwPSZN6tcWd17g1SF0A_gLUI_XCQS4Tw60z_RdddkKfxNbnggwmv_LfQwHU3EZ6wznidIMVJMIA9vP_qbr2MW9nDb7Mb9JwWKnhHXyHVTTTJ_5lzBruC_5B1I79qkSyVlM30aCFJQcQ9lB8UjLM3wjNlaE6CqF5FlVK8E_p1FUfNJ7g9cYyIkhv2nFgfBM7wUsEL4fyyB-VBD-6Uk1NYGj-PA7aOB_ftP30xjk-D7YtnqC9yz6Cnlr-LXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇧🇷
قرارداد آنجلوتی با برزیل تا 2030 تمدید شد
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.7K · <a href="https://t.me/Futball180TV/89951" target="_blank">📅 20:01 · 24 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-89950">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lxiDbXuyB7js38TrqAxMVnQqV1eh2px4xF79nee9ySfXDJEzOZveroAfsZGplI0g8po7Gqx26pbkOYLS2a40CWW9gbwyQitlqIfM4eY22QDu0fxdcUuYPS3jEpPPO2KYoYaaUkb19lsiIX2uTKNkiw77N_rlBxNxlI_iGmTarsCt6bRr4iWrS3TVlRyebiNK0bThV5Z97oRdOMp3_3In_At-K1tdahdDXuNHB3vz6qd7CC_Zin7Nh823VkH0rew6fP9kiEIDuw4hRNqKENPMFQxiADGiA82S2xSQo1_mgoYJoNhuDBn07OEU2GfsXnsQlK59MT7YRJ3yK3LP3C2eIw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇨🇴
فهرست‌ابتدایی کلمبیا برای جام‌جهانی
⚽️
Channel:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.86K · <a href="https://t.me/Futball180TV/89950" target="_blank">📅 19:57 · 24 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
