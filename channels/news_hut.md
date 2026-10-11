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
<img src="https://cdn4.telesco.pe/file/EY32lHtHo9evz-VhKCNVpx4of5a8pChU7-iYD-H43OtSTCzEgBA6rPByazFJWgIqaoL--UU7ShNFou437HzBIJlTMH1ys13-hm19zDjy8L4K3bGSSJaK_9Iqgl7UIvoO_t32qtvogRKsOBMkIuvu_0aLpgYcsI9CclQbBNvYRTwmHGhCqDONoBTiV6CPbRqD5y8FBan79NaTqjjpWkBSvWEysbSnunbTlTd5d9CjtoI6ut8eLaCk2WJtOQY5Rz8_rWK9pqwASa-mESFvh_oAtLKNZZYVopXh3QFR9POFuDVOpLfmK-PRM9BSKEYC85iJ6Y_wUipPRVbl3eK0bL-Prw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 104K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-19 16:40:45</div>
<hr>

<div class="tg-post" id="msg-73112">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1394e2d860.mp4?token=BtjzbG6vqbOgpoOj5xEeWXJLKqZOKsvm28uLHSvO0Pl_lK_KmXj5lKz3xTi1oGh8Rbl11NYpbV8KBrY8YKIYLKLZ_1aQJB0Xt2jYARTpF5wm_WgdfrbkhJZ5Vcp_6CLkEMci-VG5Ansl4xSkLCq6JvhM5yr1HfJfUXoASod_C8yPcKaVntkoNOwsDCjlRN3g00wtttPckosZOQQO0zDdJhodbaJWBCyvgxc8L7mPNXsaKnjtD3Sp-p6Hy_mq8nLeZ4xZGB1o4WJjTrl5LuiHAe4ArLsOMOjy0fRJ-TQX4xf_4CSd8UQPGDv7yJGT80YEV59ggzXMoVw6v3DY3zz51Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آتش‌سوزی یک کشتی در مسیر جنوبی تنگهٔ هرمز بر اثر اصابت یک پرتابه:
@News_Hut</div>
<div class="tg-footer">👁️ 952 · <a href="https://t.me/news_hut/73112" target="_blank">📅 16:34 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73111">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">صدای دو انفجار از طرف تنگه هرمز شنیده شد.
@News_Hut</div>
<div class="tg-footer">👁️ 3.82K · <a href="https://t.me/news_hut/73111" target="_blank">📅 16:08 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73110">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/de2a7fa633.mp4?token=P4jTGY5SDRsiq4ZZ85OY-HDocgGnl2xn6IxcnBgQhLCTF4soLaZSlhtYFQRXGJw3hs5xf9MIzkMppFCmxnu0axaQIt3JJ4wPpcDKWseBamV8JqXw_VxSFWGaPYBNyRfWGdoXhRkefA_ELUK5fWDVAu7ZQXzvqIXjDW3EqiKOIN8S8IZFECCmT2zqMzEx5TzN9jzAQNJXK18CwRFeqt26r4JZWijTSu8_Ls8MeBJETGFQD-fS4xDETwYoTwWsC51Xcio-aJFKDJwCyw_06G7TEx6RstsAGiEDsSyyKpDv3oUXK2KZxqBMBsTB-UaaBAqZ6bkg4innyzvdVGR-ECxB6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رئیس سازمان مدیریت بحران کشور: احتمالاً در ۴ ماه پایانی سال کسری انرژی خواهیم داشت.
@News_Hut</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/news_hut/73110" target="_blank">📅 16:01 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73109">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4f3b1e9af.mp4?token=bEWblb9hdbsrJocGiSLkIDGUDf4Brps2c-_XDlqOKQ5SZHDGCUN2MMMgaPmrgoBX9sIKyBO_SJJYHPjXZlyh-YceT1O94i4bHht5zYVMDFkECNeVaK7MCkorsbB7ir9T5mOadrQmCihzlwDd8W8_Q5oPXZiA83_vs-5c3oUUu1Fx6sd-mOfZDWdaMVS3aVyIKwCZOawe9EJqNWqxPWdCQGO5T2YvzC6Y93WTHovThU5WWANh4WaOGzqFzV6BVikZgwGbaeg1IcrS6p2HkzxxZ7bPBuRZcwDlB_btVy1UIBToaiSMdjOY0RtOxeO2aa7wEYVxxCTgLExCGnLb8BH1ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یا بچه مچه با خودتون نبرید طلافروشی، یا اگه میبرید با طناب ببندینش به خودتون که همچین منظره‌ای خلق نکنه :
@News_Hut</div>
<div class="tg-footer">👁️ 6.84K · <a href="https://t.me/news_hut/73109" target="_blank">📅 15:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73106">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d18ce038cc.mp4?token=NA37AlFpnwBgdY0fr-S8wq7-qOWDSqpx5QvAmLIqiXW3R33bCXPfb1QNcHN_kG05iNPlobCSI8Sm_1SOC97c2riiHj4wNW-X_NJfuNCey7d5rwKig94kzDaQyLxT9y0pIRIe-1lM6Q0u3fH0_IrRgyt4hFbeFgUirlCCiv5cGgzlnRGTc88-Hqa7jo0hWXqIEnYPUoXS1lP5jv90y_enfx1TBCWvjPHV_9OL5ybPHbntgAUS86p46YXXM3erVW5s3yDQgwUBGD-cwQ90aca4dmHURs7iaD_BIPcGFwjJbnMt0_hWZ5obe3HcO-24CqTouMmh81a01Ax-Bs_yWjjSKw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت گرگان بعد از سیلاب ساعاتی پیش.
@News_Hut</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/news_hut/73106" target="_blank">📅 15:03 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73105">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=iuMjLKHUGGcWu43CgT0wDE_Ab5yYfZmZUGLsIru0-B6xE687kbVxF1HjBloQfQHYiPN_4yqGUru1N_V4L0Y8MQUCej8ila_ZaW_XqkAE_xL8Rf7TWhBflqjnc-RsiYQTmFGnJ9MqLgf_3ws61hxXsjXOD-_OIxtKPjlDqBldsY-IMjHGpk1Ac3fy5uAN1IB3RLA-CI6vg9cJx_SrteO7NWCArGx_eiHF43KYXhDkAgpEEiKaORJKkMzWHnxkqstKQOahWXoA-d7qRHL4iQoBbtDcnGgfX41wuljw-3_yT6Jp64VdcVoR_46fMbdN1ZyTcTJDbXmqNmBTGsr9we3YLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/35cfb05bea.mp4?token=iuMjLKHUGGcWu43CgT0wDE_Ab5yYfZmZUGLsIru0-B6xE687kbVxF1HjBloQfQHYiPN_4yqGUru1N_V4L0Y8MQUCej8ila_ZaW_XqkAE_xL8Rf7TWhBflqjnc-RsiYQTmFGnJ9MqLgf_3ws61hxXsjXOD-_OIxtKPjlDqBldsY-IMjHGpk1Ac3fy5uAN1IB3RLA-CI6vg9cJx_SrteO7NWCArGx_eiHF43KYXhDkAgpEEiKaORJKkMzWHnxkqstKQOahWXoA-d7qRHL4iQoBbtDcnGgfX41wuljw-3_yT6Jp64VdcVoR_46fMbdN1ZyTcTJDbXmqNmBTGsr9we3YLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جواد ظریف:
من به مسئولین گفتم، با برجامی که کونتون رو پاک میکنین، فردا باید دماغ‌تون پاک کنین!
ما کشورهای منطقه رو تهدید می‌بینیم، برای همین سفرای ما در منطقه جا بازرگان و دیپلمات، نماینده سپاه قدس هستن.
ما همه چیزو تهدید می بینیم، زن رو تهدید دیدیم، اینترنت رو تهدید دیدیم، کشورای منطقه رو تهدید دیدیم، ما حتی حجاب هم خاکریز می‌بینیم!
@News_Hut</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/news_hut/73105" target="_blank">📅 14:28 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73104">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=fd0LJ4mCY9UVBhdFMvEngdQyRHQQhwA_hxlexp7DbZEGBtvWJ4d7m2Lt2Ty7Cnz0QHv1ygGoZO1kw484bMkp4iajXA6cNvStatOtybMDEy7qEn7QSgReDaPoa_cLMswhIRmZQUVCX3Xc0M-m4X5E4qPxODJp4fMpVVgcsFgEpvOzQywlv3veGhIiYlJ6Mjz-PUt4zQaKCxK1bzlx_BxyNVmhSz_9UR0ze4PJWE7iiT4D6huBj3py7jKrIbVBhbX6-rK13PYD0IgrkffoaUGB7bWJGWDpBoE5ZvgYDstkhe2hf2hnuTbpsjYF9HhNHyY_UeJHFJVWifZklSq55ak5sg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7ac45cb0ca.mp4?token=fd0LJ4mCY9UVBhdFMvEngdQyRHQQhwA_hxlexp7DbZEGBtvWJ4d7m2Lt2Ty7Cnz0QHv1ygGoZO1kw484bMkp4iajXA6cNvStatOtybMDEy7qEn7QSgReDaPoa_cLMswhIRmZQUVCX3Xc0M-m4X5E4qPxODJp4fMpVVgcsFgEpvOzQywlv3veGhIiYlJ6Mjz-PUt4zQaKCxK1bzlx_BxyNVmhSz_9UR0ze4PJWE7iiT4D6huBj3py7jKrIbVBhbX6-rK13PYD0IgrkffoaUGB7bWJGWDpBoE5ZvgYDstkhe2hf2hnuTbpsjYF9HhNHyY_UeJHFJVWifZklSq55ak5sg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری منتشر شده است که لحظه حمله حوثی‌ها به فرودگاه بین‌المللی ملک خالد در ریاض را نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/news_hut/73104" target="_blank">📅 13:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73103">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QPJeJ7RI7MXreV_eU2Q_EaEFFsHg8DgBKJsYsUQFVr8QlADFFcYkHiWcLgANJEy738Q0RuIsUH3-o0w5JleOk7z4duRNtcapjRmlRvKnxNSkHhQfSybrfQ8CyRPMQbP6XQeqP6kkqNPCgDLWpUmRTQRTz4bJ2vcmI3Qk6qP9jMfFQVsQtsHnE9mkj85nnofAlO8sn9rsYHvHhEieJg3I0nm_kcc86hfwxiLKYSR9naGeBhkU_2_PLabF1UjP8Eo8iAQS9ctcQQbsXN5NeazXY8DD3V9_CoFKM2t-oNj0VGdW1fPGlM1dTNhZoJT-Dm0FXqD7-e-7dCNFGK8ck6CG0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">روز جهانی دختر، بر دختران سربلند و آزاده‌ی ایران‌زمین فرخنده باد.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/73103" target="_blank">📅 12:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73102">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z389a-R88AwrEo6VprFVP_PwwjWHG0RN_A-1JnytG3iiKNSH6iAhpaCc7IUoU_Zkx-3QrhHLNXtjxp_M2vVcQ0xhFI1QBB-DkB5cI8_TZ0etJgJLs-EzDuAk1jDRqcohQXTQZFX70c6b4knd5mxMLWsxCthCOOEWTzc8UCu32VH5DwX2LGHyaqaRthxQOAJ4keTqzSIobkj54A-2EiuaEFMEYhDoBSzwSb2TtGOn9zfFsVCepk3KrtM9lvllaNHSPZ45hWCGO7F5up5PNBMaZIvuVxA8ONTbdKaQ-16RE7b1OP9IUa22zNkiG3z-zszoOa6Z2Cufpt7kAUNw3YzuxA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تست موشکی از جنوب تهران
@News_Hut</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/news_hut/73102" target="_blank">📅 12:52 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73101">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/47fbc83428.mp4?token=s2HJYle5Gj1rMuuckE4cCzf12Lz5vXhiTvYailyUMvKDaBLDFT-g0M43pEnlJ0QMgFDbiwx8MloMthyxJC6CF56SzTvU3VJ9e07QC4qRVJp62bQ5tDLzdVz2eSH0cVOE-NDIeknXaQ1cme4uURUoHXexIHALXcSGj1uMcMipy90-7jJGRUaZ429bCfAtu7ItpkT7nJM7_1xSJzjqO4L5EIWEMnMwXsMqhydpLPO2YSeMcSdc2GiNAoHw1h3jJ7H-aM2ZWqVinHvHrbwfRhE9OK0olU_1zha8K3a1EnQo7Sk9zraciPx-C53nzPby1EPPIwBv2YwRw_JaRmX4qT-4Ng" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: یک کشتی باری در دریای عمان هدف حمله آمریکا قرار گرفت
فرماندهی مرکزی آمریکا (سنتکام) اعلام کرد در ۱۰ اکتبر، یک کشتی باری با پرچم پاناما به نام Ocean Molica که پیش‌تر از یکی از بنادر ایران حرکت کرده بود، پس از بی‌توجهی به هشدارهای مکرر و تلاش برای عبور از محاصره دریایی، هدف مهمات دقیق یک جنگنده آمریکایی قرار گرفت.
به گفته سنتکام، این حمله پیشرانه کشتی را از کار انداخت و خدمه آسیبی ندیدند. همچنین، طی سه ماه اجرای محاصره دریایی، ۴ کشتی از کار انداخته و ۱۳۵ کشتی دیگر وادار به تغییر مسیر شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73101" target="_blank">📅 12:29 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73099">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=XaEJHgdEk5S-wQxi5GO7Ri0ng51z2GaY3bmC-G4FlZNj3ytLTSKMooERbP-yENZFWjFGQc67uXUkrl0bMkvFQAvqtFuKcI482rXE2xewgCxFiF2Gbr34qIBrC7Zlcvg9UEi6BvFMzGjM_DtUglPaUJ9Cj5w8NI-GhwmcpHXTEjQzSWWEYFWFntN0aGvuL5_OmKOkMrnNwyVlobTp8lK0rdPMddAHlwn_t7DswP98Xi9zwOcGURt9_AUmsMEo-j9bC6195KRQ8UPLhkBQ5LTwgyTePHbac6ayqIcPDnlI2E66wOoppNB928JmPAR4wf0yTWrEVThr-oqRr4rx_gNtYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6da19cc3d2.mp4?token=XaEJHgdEk5S-wQxi5GO7Ri0ng51z2GaY3bmC-G4FlZNj3ytLTSKMooERbP-yENZFWjFGQc67uXUkrl0bMkvFQAvqtFuKcI482rXE2xewgCxFiF2Gbr34qIBrC7Zlcvg9UEi6BvFMzGjM_DtUglPaUJ9Cj5w8NI-GhwmcpHXTEjQzSWWEYFWFntN0aGvuL5_OmKOkMrnNwyVlobTp8lK0rdPMddAHlwn_t7DswP98Xi9zwOcGURt9_AUmsMEo-j9bC6195KRQ8UPLhkBQ5LTwgyTePHbac6ayqIcPDnlI2E66wOoppNB928JmPAR4wf0yTWrEVThr-oqRr4rx_gNtYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">جدی رفتن ویدیوی رپ هوش‌مصنوعیِ بی‌بی رو نشون خودش دادن، اونم به شوخی میگه از کجا میدونید شاید واقعی باشه:)
@News_Hut</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73099" target="_blank">📅 11:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73098">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">مقام‌های سعودی اعلام کردند در حمله روز شنبه به فرودگاه ملک خالد ریاض، ۱۲ نفر کشته و ۳۰۹ نفر زخمی شدند.
ملیت کشته‌شدگان:
عربستان سعودی: ۴ نفر
بنگلادش: ۲ نفر
آمریکا: ۱ نفر
مصر: ۱ نفر
اردن: ۱ نفر
سوریه: ۱ نفر
فلسطین: ۱ نفر
سودان: ۱ نفر
برخی مجروحان در وضعیت وخیم قرار دارند و حمله خساراتی به تأسیسات فرودگاه وارد کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/73098" target="_blank">📅 11:14 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73097">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f2ae9fdb8.mp4?token=bgSQXKir0xGI2uv6f8C5eD7vaSgl5EvlMls6jByzyuyV9S7noy1u2UnqMI9cHaVljRXvLbfjze9966bmHzAh8z25yjPS2rtaMyIHOUwA45Na4Lo1NgMZFZiqww7XRASNEw7pPX5AVt-S1zBev7MEcBQQmVL3l1jvrkn3fBvO9C4vWVLoKvS1uwmXdOEiRuQAY2lklQIzIgj3dEqxYtzLO7ZxLVJA0EVzx6LYfiDlRVjIBtxvc9YMN5oYFZx8v61B6yjUW-3iqxBYyTR3hN6VcJGRj0-_BX8db6FvFPaMlFB0OcYwY_LU8XygWI5Otv6P2-_IWbg8mkleFx5f-ouJdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: نظرتون درباره حمله حوثی‌ها به فرودگاه ریاض چیه؟
ترامپ: «به نظرم اتفاق وحشتناکیه.»
خبرنگار: آیا آمریکا هم وارد ماجرا می‌شه؟
ترامپ: «خب، خودتون متوجه خواهید شد. اما به نظرم اتفاق وحشتناکیه.»
@News_Hut</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/news_hut/73097" target="_blank">📅 10:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73096">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامپ درباره یمن:
«ما با حوثی‌ها در ارتباط هستیم و باید ببینیم چه اتفاقی می‌افته.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/73096" target="_blank">📅 10:46 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73095">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=pCJISJ28_OAhz3KWkbgDojBZQofEalD1W-21AvMLLq-RNqrvFpdIZdEI_B4jnmUFniptDTa5XMXGG9mD_or36pgHAuINpPntYWwAqWJ_j-FR7uiMAeK3ltzNSu_4HkXZAlJduaww9QZhtezUGCpm7xQUVdBQ5T11VQn18XBhxSobZuvJSPpH5e0NrbkXAlTUFqNxRATFyjXaeTeVCPRqLxi-HLxW1M4aklPXhZTQlVW-n-bffJwdJx-xILTde5vlUJqouUGhyUf4Q5tJgBeDhUSx3dgBHfjMPMgxvk76jTRCAHqI6W7gsipAA5iNkTNa_ljwd46xYjak4Dz6IRHzmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/174ee9d3ac.mp4?token=pCJISJ28_OAhz3KWkbgDojBZQofEalD1W-21AvMLLq-RNqrvFpdIZdEI_B4jnmUFniptDTa5XMXGG9mD_or36pgHAuINpPntYWwAqWJ_j-FR7uiMAeK3ltzNSu_4HkXZAlJduaww9QZhtezUGCpm7xQUVdBQ5T11VQn18XBhxSobZuvJSPpH5e0NrbkXAlTUFqNxRATFyjXaeTeVCPRqLxi-HLxW1M4aklPXhZTQlVW-n-bffJwdJx-xILTde5vlUJqouUGhyUf4Q5tJgBeDhUSx3dgBHfjMPMgxvk76jTRCAHqI6W7gsipAA5iNkTNa_ljwd46xYjak4Dz6IRHzmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: آیا سعودی‌ها بدون حضور نیروهای آمریکایی هم می‌تونن از خودشون دفاع کنن؟
ترامپ: «بله، توانایی دفاع از خودشون رو دارن. سعودی‌ها جنگجوهای خوبی هستن، اما به نظرم اون حمله اتفاق وحشتناکی بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/73095" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73094">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73094" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/news_hut/73094" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73093">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ElvFrXraSVC9BUdDias5ZQVsdAoipYsj3t06i0789cLBKB1fkj94SXnQLcp1HIDNyB35qgBAPKZJbKI4cxJXLMhKC_KrLd4uw2KvbvxwJXTk7e9XEecxBKI3B7lbeDIU7ZgpA4RS1Jki7wX58YDuB8TroacnkEOtBPU4vT93Ay_SDiilro-HAGP9D8PY6vPWwigcEKC7Xe29TI8AS8WCxtrtCpRHelDmxhQHM21UwF0h5H3soKcDTXY9plgNGzsIuiBDN8IlnhX1cAuAgRrcc02Xl7LC-MCwp9Hp49ufPjwuFeP0j-kJtivgqRaN4upT3mlMP788e2AjZtqpPa2A6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
ناتینگهام‌فارست
🆚
کریستال‌پالاس
اورتون
🆚
هال
منچسترسیتی
🆚
لیورپول
اوساسونا
🆚
راسینگ سانتاندر
رم
🆚
کومو
مونزا
🆚
لاتزیو
میلان
🆚
ساسولو
فروزینونه
🆚
ناپولی
یوونتوس
🆚
کالیاری
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/news_hut/73093" target="_blank">📅 10:45 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73092">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71e6800693.mp4?token=qJo8UCABh1oyGt7EZiEvoffYQmIinKFLsD-hm0Kcs-xWJ39D--yCj8ow5UmUrAUkdFBSpfpsmIroCNGPFJGp_v7_gv7njw7QfFzIQQoBqbiUidZenxrgOOCt2kNHH-MfNFYNsExQbm9NS5EA0Qm6ZFJjTwDWNYvS7IDGrMNq-O8m9EDxI238OobjH91Lt8fyqlRA2C48ziNGO4ObEmtiDZPHQr_4qo2s7srh_9KBkqGedLfRklqslu4xB_lZ9hgW-eXZRIbsnhhDFgPCYV9ODU50SZRMCuUIox49mxEdHIHLw-5cBX-LORWkWaaXIQQuaB1rYPib9WQ9BiBqcT9o-A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71e6800693.mp4?token=qJo8UCABh1oyGt7EZiEvoffYQmIinKFLsD-hm0Kcs-xWJ39D--yCj8ow5UmUrAUkdFBSpfpsmIroCNGPFJGp_v7_gv7njw7QfFzIQQoBqbiUidZenxrgOOCt2kNHH-MfNFYNsExQbm9NS5EA0Qm6ZFJjTwDWNYvS7IDGrMNq-O8m9EDxI238OobjH91Lt8fyqlRA2C48ziNGO4ObEmtiDZPHQr_4qo2s7srh_9KBkqGedLfRklqslu4xB_lZ9hgW-eXZRIbsnhhDFgPCYV9ODU50SZRMCuUIox49mxEdHIHLw-5cBX-LORWkWaaXIQQuaB1rYPib9WQ9BiBqcT9o-A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">امام جمعه تهران:
توقع مردم، تجدید نظر در دکترین هسته‌ای ایران است
از ان پی تی خارج شویم به غرب می‌گویم هسته‌ای ما به شما ربطی ندارد؛
غلط کردین؛ برید گم شید!
@News_Hut</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/73092" target="_blank">📅 10:04 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73091">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=Z9h2lJAwnkbhVRnC4yEH9DpHi6FwwU6Hn3x8dCWknF1WA9o0EpicFqO1CGWppMV9977n5KeKIK90Kmjf4UUsp_q_NbLX7xgDeCw-_swN8nwvo8syNgXGJK3kVtWSdn_TYflSQdjsDqu2-gds9Kbpj91bbSoeEQ6fEZigUXhJiUtCc7MJipbKedSyuSCEsYWYPOhSRQrWt44DBJh5W_-mW0zAEEAgrddu52Y_ppA1r_a1LFKoPEwuidlf48ZNkza6fADI11OZG1vlJwOyiL0P1rvZ0k3TNuxPWmpkZ_P-ddcGg-V1AuGGt5-FU11UERbT-zEH0clpRYblLQXN8Qb3Gm8hHbwFcD27mLtJavz0CKZ_OBQhT1qX76Hxan3yC2cg3X2x1PMZ2kSVNKbrdfWbX8Ou2hxA2ifGhZD2fmkBwofYNrkzErEv6wy5MzRP7DkjkiCflz9T9Zqfl1sdX4nghkLKJ5fmGXmUWZs1q7NCaGCxRpn4wFHq9e-TGa5-qrfgqkXlvjDZJ2mZ02U4KIdHFqBxkIWogF01fefXfdanD8rf_XkI9ElWMfo_8sysJLvJC-ZjT65IWTELeiL4vk2mwRxTsNzRcfjRgX5yL4hSwl0dvTuFbBOMi59Ae2HSAdnnpntEUqpSFOPD3lOe5A-bJT6aPmh6lxL4tqIyYwqax14" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce6a5528a8.mp4?token=Z9h2lJAwnkbhVRnC4yEH9DpHi6FwwU6Hn3x8dCWknF1WA9o0EpicFqO1CGWppMV9977n5KeKIK90Kmjf4UUsp_q_NbLX7xgDeCw-_swN8nwvo8syNgXGJK3kVtWSdn_TYflSQdjsDqu2-gds9Kbpj91bbSoeEQ6fEZigUXhJiUtCc7MJipbKedSyuSCEsYWYPOhSRQrWt44DBJh5W_-mW0zAEEAgrddu52Y_ppA1r_a1LFKoPEwuidlf48ZNkza6fADI11OZG1vlJwOyiL0P1rvZ0k3TNuxPWmpkZ_P-ddcGg-V1AuGGt5-FU11UERbT-zEH0clpRYblLQXN8Qb3Gm8hHbwFcD27mLtJavz0CKZ_OBQhT1qX76Hxan3yC2cg3X2x1PMZ2kSVNKbrdfWbX8Ou2hxA2ifGhZD2fmkBwofYNrkzErEv6wy5MzRP7DkjkiCflz9T9Zqfl1sdX4nghkLKJ5fmGXmUWZs1q7NCaGCxRpn4wFHq9e-TGa5-qrfgqkXlvjDZJ2mZ02U4KIdHFqBxkIWogF01fefXfdanD8rf_XkI9ElWMfo_8sysJLvJC-ZjT65IWTELeiL4vk2mwRxTsNzRcfjRgX5yL4hSwl0dvTuFbBOMi59Ae2HSAdnnpntEUqpSFOPD3lOe5A-bJT6aPmh6lxL4tqIyYwqax14" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شبکه بریتانیایی ITN حدود ۴ ساعت از تصاویر وقایع سال ۱۹۸۹ میدان تیان‌آن‌من را منتشر کرده است؛ تصاویری که پیش‌تر محرمانه نگه داشته شده بودند و توسط تیمی ضبط شدند که موفق شد این نوارها را مخفیانه از چین خارج کند.
این مجموعه که حدود ۳۵ سال در آرشیو نگهداری می‌شد، شامل یک ویدئوی تدوین‌شده‌ی ۲ ساعته از سرکوب‌ها و همچنین ۹۰ دقیقه تصاویر خام و مخفیانه‌ای است که در روزهای پس از آن واقعه ضبط شده‌اند؛
تصاویری که کامیون‌های نظامی در خیابان‌های پکن، جمعیت مردم و پیامدهای آن رویداد را به نمایش می‌گذارند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/news_hut/73091" target="_blank">📅 09:30 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73090">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=ushH8Uz8acDvjzn4mJFCdw7uWeu-SwvIPHQi3OuCbTFUNs0VYLse4a2DOw-EboZmEe3ObbNQDWNPdfsDilQycTIvgQ3QsG9FT2yjn8TbowzO-YyBUWvQaObLdX_mYdWDAJ0GGmy1vX7iOjwK9J17opadsweY7G2xhkuGPhnWBexQvLfg-hCzqqV54rQ5F_nr2vknx3DZBfKCJfWzga3tPX_A9_QwzW65Qddh6q-AhSLqi3yUk9PintQXw1suFd6XUcAE55c1c2_pt5BdDzsu0GNwtsVuT1klpdYVdl_uEDsMLhCAOH29kbyVf0nDODrDsCVW1f8aHtu5udO5uFBvBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e31f09431.mp4?token=ushH8Uz8acDvjzn4mJFCdw7uWeu-SwvIPHQi3OuCbTFUNs0VYLse4a2DOw-EboZmEe3ObbNQDWNPdfsDilQycTIvgQ3QsG9FT2yjn8TbowzO-YyBUWvQaObLdX_mYdWDAJ0GGmy1vX7iOjwK9J17opadsweY7G2xhkuGPhnWBexQvLfg-hCzqqV54rQ5F_nr2vknx3DZBfKCJfWzga3tPX_A9_QwzW65Qddh6q-AhSLqi3yUk9PintQXw1suFd6XUcAE55c1c2_pt5BdDzsu0GNwtsVuT1klpdYVdl_uEDsMLhCAOH29kbyVf0nDODrDsCVW1f8aHtu5udO5uFBvBTzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
فلسفه بازنشستگی در یک کشور اسلامی هیچ مفهومی ندارد و مسلمان واقعی باید تا آنجا که می‌تواند خدمت کند
حیف است که افراد ۸۰ و ۹۰ ساله را از خدمت کنار بگذاریم.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/73090" target="_blank">📅 09:00 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73089">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73089" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73088">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromTrexBet IR</strong></div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/news_hut/73088" target="_blank">📅 01:57 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73087">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=cSaG1mt7D2LkJMECEGuVR8okIFE48UOgvmfP4vCDyq_1niU6r5eLCeWgDgp3DKa6HymZ4TZ7lFc9GtM8W6Li8Xkux_fpkkMH_OnyRnqlAjrlEq8xi77tsKO9EK4cn679NgzajXWXo-0AZnChUErV_ls1c0ww3zm4skL0xNNdHzUZ2m8N1DJ4ZUVY5EpxslUPC9s69lt3wpwrjYQxJXo2HZ2xyayR6cgXhNjqIImM2vEs77WPR0-ezw-q1-qzYrrdduVYMH1mJ3pMZY4d51f25xxFo6OnNqmRyeRTxJXWibTxmVuO4imp96MDHwggNXgxCss3jTuX9bWfvL9tKMyVwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1848b3d2ec.mp4?token=cSaG1mt7D2LkJMECEGuVR8okIFE48UOgvmfP4vCDyq_1niU6r5eLCeWgDgp3DKa6HymZ4TZ7lFc9GtM8W6Li8Xkux_fpkkMH_OnyRnqlAjrlEq8xi77tsKO9EK4cn679NgzajXWXo-0AZnChUErV_ls1c0ww3zm4skL0xNNdHzUZ2m8N1DJ4ZUVY5EpxslUPC9s69lt3wpwrjYQxJXo2HZ2xyayR6cgXhNjqIImM2vEs77WPR0-ezw-q1-qzYrrdduVYMH1mJ3pMZY4d51f25xxFo6OnNqmRyeRTxJXWibTxmVuO4imp96MDHwggNXgxCss3jTuX9bWfvL9tKMyVwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«ایران کشور بسیار شروریه؛ بزرگ‌ترین حامی تروریسم در جهانه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/news_hut/73087" target="_blank">📅 01:54 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73086">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=ONwV-epK66QB21HmLmyUBJPFstAks77z2wC5ecU4uRPDs_6ow1iCq2h_95NWFx-VNki39Fou293a3m1YgyQGD5aFQrvZ0iqD0DmZ2vEvOLY_I1i96tPZZKIWZncpSHYBqU07S5dxAX6nJzDU5NivhIQVw34sMr1JJBlufLTmpJDejbxE-JFyX3WvvkTMy2NnqP0gUsW6CiibU-rKoKTdBcY-nBxUGPP9gXJSDnrEstCt335eFqbNkGl2EMLYvCIRhD0vvXFATeuoFbsati-w0U86DtmzJifg3KcJiWw7drrQdFmoSEJ1ktumiIrqHoCy073GM5kz6tDhOgDdfeO9sIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e6a4893ab6.mp4?token=ONwV-epK66QB21HmLmyUBJPFstAks77z2wC5ecU4uRPDs_6ow1iCq2h_95NWFx-VNki39Fou293a3m1YgyQGD5aFQrvZ0iqD0DmZ2vEvOLY_I1i96tPZZKIWZncpSHYBqU07S5dxAX6nJzDU5NivhIQVw34sMr1JJBlufLTmpJDejbxE-JFyX3WvvkTMy2NnqP0gUsW6CiibU-rKoKTdBcY-nBxUGPP9gXJSDnrEstCt335eFqbNkGl2EMLYvCIRhD0vvXFATeuoFbsati-w0U86DtmzJifg3KcJiWw7drrQdFmoSEJ1ktumiIrqHoCy073GM5kz6tDhOgDdfeO9sIWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«اون جوان‌هایی که در جنگ علیه ایران از دست دادیم، بیهوده جونشون رو از دست ندادن.
نمی‌شه اجازه داد یه آدم کاملاً دیوونه به سلاح هسته‌ای دست پیدا کنه.»
@News_Hut</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/news_hut/73086" target="_blank">📅 01:50 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73084">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=W4dujg4Gs9ixB4HoXTudrgUbr37nWAFkOL2nHWpR6XWxffmNdzJt6T8hdReIzMVIRKKNsCoYevIVC3XIaWP_wns0G4RcvfMEN6Ka1loHuzXDpkBuP9alGfGA1_tD_N0u0xNXXdKCJktE0jw2OSEShkOPNr0H_m-kUDAl1JxV_HCgBzItGOUH9xwa3Y8TMwsk5g4PdG06VIyN8_BCuKmXKBqWEAHRe4ZRRz4QBk5ZiLSxQSHUG6y7NnyDvnj7WhYQ56i8axd8p2D1xZMDkAFUKeDBGmrUCKgEfoW7B3gJ37VvjOyxVSbxRyy_F4zUigO6D4oMQIAPgyAJsZ1LIgb8NQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/595730e6c3.mp4?token=W4dujg4Gs9ixB4HoXTudrgUbr37nWAFkOL2nHWpR6XWxffmNdzJt6T8hdReIzMVIRKKNsCoYevIVC3XIaWP_wns0G4RcvfMEN6Ka1loHuzXDpkBuP9alGfGA1_tD_N0u0xNXXdKCJktE0jw2OSEShkOPNr0H_m-kUDAl1JxV_HCgBzItGOUH9xwa3Y8TMwsk5g4PdG06VIyN8_BCuKmXKBqWEAHRe4ZRRz4QBk5ZiLSxQSHUG6y7NnyDvnj7WhYQ56i8axd8p2D1xZMDkAFUKeDBGmrUCKgEfoW7B3gJ37VvjOyxVSbxRyy_F4zUigO6D4oMQIAPgyAJsZ1LIgb8NQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دلقک بازی املاکی
😐
@News_Hut</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/news_hut/73084" target="_blank">📅 00:59 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73083">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=W021I6k4cbrhzRz2nwYWWTtzfnoFQGwAbOjJWmQ9cPHIGi2UJTcOQ9eAMmCnEGX8grJBWhlb0wOazLmnNtzJ38iVkPUGgvnfFUJdXR4l76-FLHkxhZhsu643fLsvdzwweGTXvGhz02oBBny-ArXWyCiDLIxl63Voy2_B8QqexzrIK43r3MBogS9KNukEfzlktSDiz-h5mv9u7Z6LwTe9Vg2J37gOPLb5T_M7NG-A3QN4Ua-NOT7gUM7LR8tEXap4oXljps9pCc00viJPJBtDkx0jd6veztzJAvuhbmVLCNFOvkUOKs9MeroXpwnnHfDMISyc049ZERhX57xGejMmTQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8b6424edb4.mp4?token=W021I6k4cbrhzRz2nwYWWTtzfnoFQGwAbOjJWmQ9cPHIGi2UJTcOQ9eAMmCnEGX8grJBWhlb0wOazLmnNtzJ38iVkPUGgvnfFUJdXR4l76-FLHkxhZhsu643fLsvdzwweGTXvGhz02oBBny-ArXWyCiDLIxl63Voy2_B8QqexzrIK43r3MBogS9KNukEfzlktSDiz-h5mv9u7Z6LwTe9Vg2J37gOPLb5T_M7NG-A3QN4Ua-NOT7gUM7LR8tEXap4oXljps9pCc00viJPJBtDkx0jd6veztzJAvuhbmVLCNFOvkUOKs9MeroXpwnnHfDMISyc049ZERhX57xGejMmTQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارسالی یکی از اعضا از گرگان:
بارندگی شدید امشب در گرگان باعث وقوع سیل و وارد شدن خسارت به اموال مردم شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/news_hut/73083" target="_blank">📅 00:48 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73082">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=L5FeRVDMhXyeQ6n75pU-uqgIDtoRtzo7dIpRpGDZVP0NxdX2crGEsyd41IxvN6pkXcaRhiGjpE5_CjsIrtsvUVLAALAWdhvqRvGf7s3qawBZEjQfyVbRzuoifBp8MNWs0VOntYM_VzQ8juGnUOtSNfYdKmiseQrowufnVdXH25Qhyu4aGZPLY75V4RkqkLlpNSptvT2UNrQz8OVBOcdeFsFAfGNaZE52pgFK3Ae97AApf81gdO9BaNy7FnrSpEl2oAxH-uncVo4NbPeK55r4SU0FG1V5qp_DboPTc-6m4KfgGtcLyW_8DoafqtQivtzXccJMM8MZP5Xy1JsBHP00Mw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c88cca8dd.mp4?token=L5FeRVDMhXyeQ6n75pU-uqgIDtoRtzo7dIpRpGDZVP0NxdX2crGEsyd41IxvN6pkXcaRhiGjpE5_CjsIrtsvUVLAALAWdhvqRvGf7s3qawBZEjQfyVbRzuoifBp8MNWs0VOntYM_VzQ8juGnUOtSNfYdKmiseQrowufnVdXH25Qhyu4aGZPLY75V4RkqkLlpNSptvT2UNrQz8OVBOcdeFsFAfGNaZE52pgFK3Ae97AApf81gdO9BaNy7FnrSpEl2oAxH-uncVo4NbPeK55r4SU0FG1V5qp_DboPTc-6m4KfgGtcLyW_8DoafqtQivtzXccJMM8MZP5Xy1JsBHP00Mw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">املاکی درباره تنگه هرمز:
«داریم به این فکر می‌کنیم که اسم تنگه هرمز رو به تنگه ترامپ تغییر بدیم!»
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/73082" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73081">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=TivT_dQCmiulhePxXzctatJJsa9nUBp6TFbOpM2m0RkhGTCYsaLGaXX4R9a8ztbbjJeE9V4S9jR-sy4AW0Cxmjp_xaqMW89d9RKhF0Qph-ejEoVAex75jQ9SVZD8kToTcOsdGiFFwLWdItndiabRFSEvXlQfi9x_xojS3tTpFYdG6Hs-WgTuYnS2UQgZWvPJcwr9kA-ZQPqe3ziY4BIy99Jl0koXwy0UMeRCESiqhDI8Xl7haa1sk-fPcBwg3diJekTcAf5fbUHUx7Q-fGhZ-ahDKbw29KU843huibUt51brvYY20ZaJaszGMUsnSz-rDcYVwK2arWyMLAijMUfd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e93cc318ec.mp4?token=TivT_dQCmiulhePxXzctatJJsa9nUBp6TFbOpM2m0RkhGTCYsaLGaXX4R9a8ztbbjJeE9V4S9jR-sy4AW0Cxmjp_xaqMW89d9RKhF0Qph-ejEoVAex75jQ9SVZD8kToTcOsdGiFFwLWdItndiabRFSEvXlQfi9x_xojS3tTpFYdG6Hs-WgTuYnS2UQgZWvPJcwr9kA-ZQPqe3ziY4BIy99Jl0koXwy0UMeRCESiqhDI8Xl7haa1sk-fPcBwg3diJekTcAf5fbUHUx7Q-fGhZ-ahDKbw29KU843huibUt51brvYY20ZaJaszGMUsnSz-rDcYVwK2arWyMLAijMUfd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«می‌تونیم خیلی سریع به این ماجرا پایان بدیم. ایرانی‌ها نمی‌دونن که من تا حالا چقدر باهاشون مدارا کردم و چقدر باهاشون راه اومدم.»
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73081" target="_blank">📅 00:25 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73080">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_3RX-vb_pIFiPjTfvwFAB6gGrPnpoSa-n0KHFP45O9HRMM-OkDLD7sLKzbm7f0tl0cLx2BlMINGyHKG1aPIiMzY5RkG9NJrmYp67n2-mp4t-tQ27WHcwwmL4YJUq62kpl9kLZb4J4jCmPUXcoADrUtTX9MwAvK0FSe5V319-ULy6PBliaCrcd28PFm-tmQPS3GyDTSCSV1ltXBAMEZNbbXXc9nUhEnFEknx0nYeH7CLCILKCf7KhZY7fFvuiDBEUBR1eG8SQyGTEkzJ3JiuVv1WTMKwgO6gECQII_3NiN1TxN8jneCyl_U2zrEda8sFrxtvkOPaOYfqov5GMMqhIhgE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/988c9468b6.mp4?token=ZmXCEjBHNzzV22fHM1VTzIG-uBWOFbibD1jSipIzB3v2C51Uo1SshqlJun8ECyi9WvvDOJtsk5kKm36ObUuudCWPaFjYAlnyLvZhkz9sLXB_9ebijTo1HXMOkrvSNvDLBHg3X8dBe8PdLdC6rJBH-sn7PkHTmV93_HjgtesaOik13H-7xJWQa_eiCbddCP4o2MaJfAhGhtK73PjJtfnxztTOIFD3CmeG4pqGTn3QtL-scwQyc50EMWB2whbNq0-bnqpf1vJhX012HUnCyl35wtRaZScU_kAiLONS-PpKwfZqCM7NmUz8nhFt1BHJX28Qe6mVCvz9xur9B768m6mu_3RX-vb_pIFiPjTfvwFAB6gGrPnpoSa-n0KHFP45O9HRMM-OkDLD7sLKzbm7f0tl0cLx2BlMINGyHKG1aPIiMzY5RkG9NJrmYp67n2-mp4t-tQ27WHcwwmL4YJUq62kpl9kLZb4J4jCmPUXcoADrUtTX9MwAvK0FSe5V319-ULy6PBliaCrcd28PFm-tmQPS3GyDTSCSV1ltXBAMEZNbbXXc9nUhEnFEknx0nYeH7CLCILKCf7KhZY7fFvuiDBEUBR1eG8SQyGTEkzJ3JiuVv1WTMKwgO6gECQII_3NiN1TxN8jneCyl_U2zrEda8sFrxtvkOPaOYfqov5GMMqhIhgE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ درباره ایران:
«ایرانی‌ها می‌گن: همه رو می‌کشیمممم! همه روووو!
همچنین می‌گن: الحمدلله! الحمدلله! الحمدلله!
منم بهشون می‌گم: بابا، شماها واقعاً دیوونه‌اید!»
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73080" target="_blank">📅 00:24 · 19 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73079">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=tt2kD4uZdzjEJDl2n-xhr8uWKxnyoKivFnvHqHR34FizWm4iB2XcpVExRNsqMnYGhniAyOd1NFM7BceWYhazdzYhwwcCLOKmA5EX-0lcErquf16fYlpCkWhmw2Wt8ockfDVdQyOPI_sv8pUVwUR5-9Yx0nqzgo1veVVu4YgMYOee8xJBaRjXtCQl-6INIv03ff6DcUrSXeBOL9afH_cNceaLupMuFeccox5HnFLAobemx67Xo4zwGdaaEHYddzDllzaBRUhVuErKBRGaHlvuA49wpgbMiCjiKoDTpD1x0Lm3h0uj6jKOAwg5xU5dVAhPqKMLkKe9O2C2CGDMAR2g8A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8279d9c497.mp4?token=tt2kD4uZdzjEJDl2n-xhr8uWKxnyoKivFnvHqHR34FizWm4iB2XcpVExRNsqMnYGhniAyOd1NFM7BceWYhazdzYhwwcCLOKmA5EX-0lcErquf16fYlpCkWhmw2Wt8ockfDVdQyOPI_sv8pUVwUR5-9Yx0nqzgo1veVVu4YgMYOee8xJBaRjXtCQl-6INIv03ff6DcUrSXeBOL9afH_cNceaLupMuFeccox5HnFLAobemx67Xo4zwGdaaEHYddzDllzaBRUhVuErKBRGaHlvuA49wpgbMiCjiKoDTpD1x0Lm3h0uj6jKOAwg5xU5dVAhPqKMLkKe9O2C2CGDMAR2g8A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حضور گلشیفته فراهانی در فیلم Matchbox: The Movie 2026 و صحنه لب گرفتن او با جان‌سینا!
+ نکته جالب اینکه همسر جان‌سینا هم ایرانیه!
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73079" target="_blank">📅 23:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73078">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=PSbDfHij2y8fEJ5I8XKQtt6pSmm3SQ7MgWb-65IL3Pdp_D7x-66nv5Duo_f4ogGbUOKe-SfqM-m-kqCcZkImGNOa1bhxJdrypjs8DBytc-NlJDzw6OShJu1FdUjsE9jhkc9c-ZmBQLe9HwDc3FUpavdt3THrvtizFiE2wPbl_K1jwtifw-vn2lNxSFKD0as86zuEO0O6VBMJ8QFT-F8ex0p5JCWQxhR85TI7i62jcWfMAz4fx0tTGcd0feJbf246tNjLpaAnZ2sxhy2leMdu3Tdod_FrGZOlKP7uzp5s1cIMTlkF4vbLsI5UqKBtMY7BP2z8OuZKCuKtzra0jV_cdw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be8b607f1d.mp4?token=PSbDfHij2y8fEJ5I8XKQtt6pSmm3SQ7MgWb-65IL3Pdp_D7x-66nv5Duo_f4ogGbUOKe-SfqM-m-kqCcZkImGNOa1bhxJdrypjs8DBytc-NlJDzw6OShJu1FdUjsE9jhkc9c-ZmBQLe9HwDc3FUpavdt3THrvtizFiE2wPbl_K1jwtifw-vn2lNxSFKD0as86zuEO0O6VBMJ8QFT-F8ex0p5JCWQxhR85TI7i62jcWfMAz4fx0tTGcd0feJbf246tNjLpaAnZ2sxhy2leMdu3Tdod_FrGZOlKP7uzp5s1cIMTlkF4vbLsI5UqKBtMY7BP2z8OuZKCuKtzra0jV_cdw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یک پلنگ حکومتی :هر روز صبح و شب اینجام که بگم ما فقط جنگ میخوایم  و مذاکره نمی کنیم.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73078" target="_blank">📅 23:15 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73074">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=K6zCWTpsMCjHlq7pSfc3YnG5Ge4TzKgo8DSNgyMgmSWsZYHkMIaRzipXZ7MWOaQqLUlC_XJMxzrZ2O1kc5pSmjDncvsObLOFahKL9LUTTdSbKQK5867y9EQvtdT_Aow8TdxH4OraGASPb7oIur_XiGrT_l7RdDVywswnvF55ilFMwv3aDmjvPi06tv2DQohK1kKCJCAf6JLodTOD-RLJ4Nbym9MdQIs9HDp0w1ug1E3m4XTNGOPl9bezZ69eowUd4MSCqDew0oLCIUXGSp-JkvTc552CMMjmT2_KfXDyuVdWJ3SEAS3oBOmeHTe_yk64ibxYxMcQTulYNFyZFOKbKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/52a72e1a5c.mp4?token=K6zCWTpsMCjHlq7pSfc3YnG5Ge4TzKgo8DSNgyMgmSWsZYHkMIaRzipXZ7MWOaQqLUlC_XJMxzrZ2O1kc5pSmjDncvsObLOFahKL9LUTTdSbKQK5867y9EQvtdT_Aow8TdxH4OraGASPb7oIur_XiGrT_l7RdDVywswnvF55ilFMwv3aDmjvPi06tv2DQohK1kKCJCAf6JLodTOD-RLJ4Nbym9MdQIs9HDp0w1ug1E3m4XTNGOPl9bezZ69eowUd4MSCqDew0oLCIUXGSp-JkvTc552CMMjmT2_KfXDyuVdWJ3SEAS3oBOmeHTe_yk64ibxYxMcQTulYNFyZFOKbKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله هوایی اسرائیل به ساختمانی چندطبقه در غزه
دقایقی پیش، جنگنده‌های اسرائیلی یک ساختمان چندطبقه در شهر غزه رو هدف قرار دادن. پیش از حمله، دستور تخلیه ساختمان صادر شده بود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73074" target="_blank">📅 22:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73073">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=ZlgVXMOef2zHXX0fT28FN-DfTeDTbqjjcrAdbIQXrfWJVe7jmW6QBJ3E7z2EFvzTIc4GLPLaKckZhq1ImEiiPMlQuFE_FR0uEgWcX9Q-DwuEpMA2UKDRmPF2lpaGoLJ8o8mWlNT1tIQcAKYiu--zdCnvzxSI8m82kJ0iMiNx2QzbvDjUNWHmgZked0RgTnU7fRmcxm890E7fnbMXtXRQtYcuM5wLC3CAErpUEmF5igTN9QdUOytrxKq4x8EJN84RgUV-mF8rYkJ_Dp0OkrzVK4P0Ay12pI4BNvd-hI492I-v37IelpNplCCEdNmQIy6xa4hw890JdGOe10WMTQ7zIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d6e7ebfe2.mp4?token=ZlgVXMOef2zHXX0fT28FN-DfTeDTbqjjcrAdbIQXrfWJVe7jmW6QBJ3E7z2EFvzTIc4GLPLaKckZhq1ImEiiPMlQuFE_FR0uEgWcX9Q-DwuEpMA2UKDRmPF2lpaGoLJ8o8mWlNT1tIQcAKYiu--zdCnvzxSI8m82kJ0iMiNx2QzbvDjUNWHmgZked0RgTnU7fRmcxm890E7fnbMXtXRQtYcuM5wLC3CAErpUEmF5igTN9QdUOytrxKq4x8EJN84RgUV-mF8rYkJ_Dp0OkrzVK4P0Ay12pI4BNvd-hI492I-v37IelpNplCCEdNmQIy6xa4hw890JdGOe10WMTQ7zIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضرغامی: پخش خطبه‌های نماز جمعه از اشتباهات من بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73073" target="_blank">📅 22:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73072">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/be565181a8.mp4?token=t8tz4ayw-sDXiXMui4oHPHsBLxOT5tL6_JBDDVPc8wvlYMJfrs63KzoTKc3zyn5CljBTaB-9B3X-QVobhsdveZRDMLjHw4kVV8QmzJVaToYVHI4zuo77WMBpSOczVxRz-gN9a9V5PlS6h0HUPiii_ZhgAQ0wF6aD2t4E19EUZC7SZEurzxoG_9-HJ-_AsDT9upzZggtJ78DtJUbxhuJoBIvHqnTY6bqmFUnAY64_7yfeHmwtIGY8ckIwa8swTxyf6GOmLb-rj3u1cqG6ncsv2czXPwY95tPrh7Y9y9mIjqWhr6DC9pX1J7oCt9i6hJRUHmnoaVKPn596c02DiAn4rw" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/be565181a8.mp4?token=t8tz4ayw-sDXiXMui4oHPHsBLxOT5tL6_JBDDVPc8wvlYMJfrs63KzoTKc3zyn5CljBTaB-9B3X-QVobhsdveZRDMLjHw4kVV8QmzJVaToYVHI4zuo77WMBpSOczVxRz-gN9a9V5PlS6h0HUPiii_ZhgAQ0wF6aD2t4E19EUZC7SZEurzxoG_9-HJ-_AsDT9upzZggtJ78DtJUbxhuJoBIvHqnTY6bqmFUnAY64_7yfeHmwtIGY8ckIwa8swTxyf6GOmLb-rj3u1cqG6ncsv2czXPwY95tPrh7Y9y9mIjqWhr6DC9pX1J7oCt9i6hJRUHmnoaVKPn596c02DiAn4rw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چند وقت پیش مصاحبه یه دختر 25 ساله منتشر شد که ماشین 50-60 میلیاردی سوار بود!
بهش گفتن چطوری این ماشین رو خریدی؟ گفت تلاش و استمرار!
رفتن امارش رو درآوردن، دیدن باباش حسابرس شهرداری تهرانه و دختره آقازاده‌اس!
@News_Hut</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/news_hut/73072" target="_blank">📅 21:59 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73071">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=r0cn0CEiA8Bxf4LT_j1CihIodQ-y2RnMHLzV-9V64pBC4o_ms_wlAy5Pdqql8bhxfFP9xMUpxa5vF652i0JZwdW4sCCnReZlLsJJr1jAWK2nCXJPpucT3nQdJbSGnkUE8J42NpkNSl-Db5-hOHF4FdG99oqBuRxlPOTZpypcWlmofPlmlu7I7uIjd8cbIF6Bslx6iQvvYaARjIIsXrNuv9t25Sl-ZfxSGodydL-ysaDWcPxgE3bspNckogbJKqjbLv7ehQpFIt5gWXShARAI6uNnulQDbIQFhoTTStKxr72WFo0yrLb690E1Iw-YC2MeHThrFob7rgkba8hdgdTDOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/118178a3fa.mp4?token=r0cn0CEiA8Bxf4LT_j1CihIodQ-y2RnMHLzV-9V64pBC4o_ms_wlAy5Pdqql8bhxfFP9xMUpxa5vF652i0JZwdW4sCCnReZlLsJJr1jAWK2nCXJPpucT3nQdJbSGnkUE8J42NpkNSl-Db5-hOHF4FdG99oqBuRxlPOTZpypcWlmofPlmlu7I7uIjd8cbIF6Bslx6iQvvYaARjIIsXrNuv9t25Sl-ZfxSGodydL-ysaDWcPxgE3bspNckogbJKqjbLv7ehQpFIt5gWXShARAI6uNnulQDbIQFhoTTStKxr72WFo0yrLb690E1Iw-YC2MeHThrFob7rgkba8hdgdTDOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.   ترامپ: کی اینو گفته؟  خبرنگار: زلنسکی.  ترامپ: باشه!  @News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73071" target="_blank">📅 21:06 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73070">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=AnmX3YUdoMnNOq2jH2bZXQzduE_vPLpRaiLDx0I_pOcWZK-8GbbplJa4kQiiycROozgxvGoIB-DkKyr2hgDCXu7eFaFckN0ALGcALpMt-K_WRYbbJgZlQKrOe7TyrPkKqiKDcJg4bcORIBpc3e4n7Tip5I0DJr4EVs3SkmGxQMcshr5fZsTGkvYbmDZ-W3UEdSiFkrDg994c5tfjSYV7ZkqpApgKpZoHLPfD5N2aA7u66GZ2t-rBBSTwcetGP8cn-Hkem-qA_0aiKveRK_tk2wsWv_4ZyE4YtenU4kd_23fwhNyCK1zsWqeRVwIC2uQVjayl-lA2nMA0OoYoKITZqg" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/2bf843dd2a.mp4?token=AnmX3YUdoMnNOq2jH2bZXQzduE_vPLpRaiLDx0I_pOcWZK-8GbbplJa4kQiiycROozgxvGoIB-DkKyr2hgDCXu7eFaFckN0ALGcALpMt-K_WRYbbJgZlQKrOe7TyrPkKqiKDcJg4bcORIBpc3e4n7Tip5I0DJr4EVs3SkmGxQMcshr5fZsTGkvYbmDZ-W3UEdSiFkrDg994c5tfjSYV7ZkqpApgKpZoHLPfD5N2aA7u66GZ2t-rBBSTwcetGP8cn-Hkem-qA_0aiKveRK_tk2wsWv_4ZyE4YtenU4kd_23fwhNyCK1zsWqeRVwIC2uQVjayl-lA2nMA0OoYoKITZqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سپاه تصاویری از آتش‌سوزی گسترده و نشت نفت از یک نفتکش منتشر کرده که به گفته این نیرو، بر اثر برخورد با مین دریایی در تنگه هرمز آسیب دیده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73070" target="_blank">📅 21:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73069">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3875ef3f4f.mp4?token=fJhMP5n7bk9K_RAXPgEe62UrpqSTRb6hLFObDvAtpQVjroFv2GSO0bOdbSGjILiF-hCpdUffdIzZOB7PB5Kjjf98dIygDpJhWgNmlw33THmu6ti8DE67HVQLVBd3O4H813Y15L6znFNVhbUmdZGplZDqbNSygZrBCDK3hp5ZR11wPcNvdlV_KvxpKcpxvkUMVRoGYAtMWxQniEIlc3oWGKD11tn3j6kGHisy4I5kcKh1nXrpv_o0wuPqCeZhIzoAfL-YzajDplCpdvkUEYfi-kvsDKU-pEjgsaacW2jzVTuFYMIiP7hm2KZl0u0h6c4ETPwmzedu74EfnOZhRztQGg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: شما گفته بودید تا بعد از انتخابات میان‌دوره‌ای به ایران حمله نمی‌کنید. حمله اخیر در عربستان باعث شده نظرتون عوض بشه؟
ترامپ: «بررسیش می‌کنیم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73069" target="_blank">📅 20:58 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73068">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=c3Sl-wFAFqX4ncA-To6RE9vKz20hJdK07ELgO9b5FFa9w516bULOuueuwdqUzkGqtiEhvKcrbqzgHhef2koCM196wGdF9e7kC_Shya98-X4txevNjv_L8es1xd6y0QKFMmgNc3PnqZrkn-T-kIlb-yf5CzQnDRcA4JbTZIJ9WgMFoV617p_nadhBdugaYs5--D3Bxu6psNCabLnbCAgJNw34O2DAtivdZewuI_qVS1MD3zaRx3y0hI9OTMgQTgjrH5tW3N8G27BSCOKFwpzBZwJNd-nsgOr4Ghs3Ku7PSZBF5lroO5xRVA1qg1dQ2u_ylqUSZWbnYrIn6jAhtbDNyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2ba9c18ae3.mp4?token=c3Sl-wFAFqX4ncA-To6RE9vKz20hJdK07ELgO9b5FFa9w516bULOuueuwdqUzkGqtiEhvKcrbqzgHhef2koCM196wGdF9e7kC_Shya98-X4txevNjv_L8es1xd6y0QKFMmgNc3PnqZrkn-T-kIlb-yf5CzQnDRcA4JbTZIJ9WgMFoV617p_nadhBdugaYs5--D3Bxu6psNCabLnbCAgJNw34O2DAtivdZewuI_qVS1MD3zaRx3y0hI9OTMgQTgjrH5tW3N8G27BSCOKFwpzBZwJNd-nsgOr4Ghs3Ku7PSZBF5lroO5xRVA1qg1dQ2u_ylqUSZWbnYrIn6jAhtbDNyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بنیامین نتانیاهو، نخست‌وزیر اسرائیل، در ویدیویی جدید که در تیک‌تاک منتشر کرده، در حال ورزش کردن در باشگاه دیده می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/73068" target="_blank">📅 20:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73067">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f89266c981.mp4?token=el9jueNPyJ-tZ_poz676FwZ_gv4Vx1gijjbe5bYXsfPZVDeXyjbmZMIen6q8BU4AnmiPqPe83yxNFqa6WLYLco4GgzF8ZvjQdwUYC4uTAIpcZryI21e21LJMFAbylH9r-zv95Oj0FZoFIt1xKNEux_arHMJWiOF3Wr6b1duqFkdjBLfeV6BrUhmTfUf057ZHrBWiUEqv-VQz1ko3iCAzaIiVg6TVeNcz7ZTdpxZQ95bBDhK3DiCf9XZPRWvarQC8DRRUdT9qLOTV9222Db4Qs9lCCT5fT5etVym6d8x0pJE0xbE_KvRgGWbmLHR3wVMTlrqW0BHyp9cJ37rSApeCz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f89266c981.mp4?token=el9jueNPyJ-tZ_poz676FwZ_gv4Vx1gijjbe5bYXsfPZVDeXyjbmZMIen6q8BU4AnmiPqPe83yxNFqa6WLYLco4GgzF8ZvjQdwUYC4uTAIpcZryI21e21LJMFAbylH9r-zv95Oj0FZoFIt1xKNEux_arHMJWiOF3Wr6b1duqFkdjBLfeV6BrUhmTfUf057ZHrBWiUEqv-VQz1ko3iCAzaIiVg6TVeNcz7ZTdpxZQ95bBDhK3DiCf9XZPRWvarQC8DRRUdT9qLOTV9222Db4Qs9lCCT5fT5etVym6d8x0pJE0xbE_KvRgGWbmLHR3wVMTlrqW0BHyp9cJ37rSApeCz4i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رائفی‌پور: آمریکا را پایین کشیدن کاری ندارد.روسیه باید پالایشگاه‌های آمریکا را هدف بگیرد تا حملات اوکراین متوقف شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73067" target="_blank">📅 20:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73066">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ke0Mwh9MpbjcnIhL047au0f4k2_ylTNRS4-Kdua276PC3EpIwUeiWVFI3ftMOYauhYKNBdfsdA5XQ4SLt4F_HsE3a9dotbcHbmbLeaT0fOlziKpmSzn2ctzUtz9gbDhTAmiKfiDIim5S22VpkiVJ0UgQtLx69ZxDdhhWhdzn6cxv8gse-S3-hr6OrBO746vE0FZUl1wrh9UAfr0MDuHYLv6yJQ9WV4OhIbANAyB6t7jOJdSabYux-UcmvxhKANkoPWcckgU_5nYaqN6GEEP-3Pu7pPHjhdl3hL9mNEWO4URln4wXTV2TNrPQZFIo7DWoVzUXrfDTV6yeVLcw07we3g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اولین محموله گازوئیل روسیه به مقصد آمریکا حرکت کرد؛ قبل از اعلام توافق ترامپ!
اولین محموله گازوئیل روسیه که راهی آمریکاست، ۲۲ سپتامبر از بندر سن‌پترزبورگ حرکت کرده؛ یعنی دو هفته قبل از اینکه ترامپ توافق رو اعلام کنه.
این نفتکش یونانی با نام MINERVA ZEN حدود ۲۷۵ هزار بشکه گازوئیل حمل می‌کنه و پیش‌بینی می‌شه ۱۱ یا ۱۲ اکتبر به سواحل شرقی آمریکا برسه.
تحلیلگران می‌گن حجم این محموله‌ها در مقایسه با مصرف گازوئیل و سایر سوخت‌های تقطیری آمریکا، فقط برای چند روز کافیه. از طرفی، حملات اوکراین به پالایشگاه‌های روسیه هم باعث کاهش تولید گازوئیل این کشور شده.
@News_Hut
| Clash Report</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73066" target="_blank">📅 19:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73065">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=eSkyDUn1K4AZ19jCx6h9ZDNl4kTo6VxzicJfw8hv2wp6nl-oUUxaU9OPaf3bmTFxMIa7LSU7ISl8GOYpsiVKP2OQovn7uL_XvnlCo2Y6gr5kxfRscAPy-SXdCiNsuS6OmmN9Zluxj-OWkga4-4QUXqeIZ7NnJi_pRviPMfqU5YN28MmYJqVnkFPO9OCXB3gjurf37kOXKGT589d4vPFkVoQ0THx5vJt306takcPSdyDHPPSZ7w5du2hyU3zbkphQjdbcFjaSq26fqFQbOC1bmS8C1mppF_LCIP572pnxrfDCUKsTe2H7i7P9xO-T8H5Pk58_nClvbhhKOcLekbfbsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e3e4a880ec.mp4?token=eSkyDUn1K4AZ19jCx6h9ZDNl4kTo6VxzicJfw8hv2wp6nl-oUUxaU9OPaf3bmTFxMIa7LSU7ISl8GOYpsiVKP2OQovn7uL_XvnlCo2Y6gr5kxfRscAPy-SXdCiNsuS6OmmN9Zluxj-OWkga4-4QUXqeIZ7NnJi_pRviPMfqU5YN28MmYJqVnkFPO9OCXB3gjurf37kOXKGT589d4vPFkVoQ0THx5vJt306takcPSdyDHPPSZ7w5du2hyU3zbkphQjdbcFjaSq26fqFQbOC1bmS8C1mppF_LCIP572pnxrfDCUKsTe2H7i7P9xO-T8H5Pk58_nClvbhhKOcLekbfbsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در جریان اجرای ارکسترال «آرش» در سالن اسپیناس تهران، در شامگاه جمعه ۱۷ مهر، تماشاگران در واکنش به صحبت‌های اسماعیل بقایی، سخنگوی وزارت امور خارجه جمهوری اسلامی، او را هو کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73065" target="_blank">📅 19:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73064">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">برآوردهای اولیه از تلفات حمله به فرودگاه ریاض:
بر اساس برآوردهای فعلی، در پی اصابت یک تا دو موشک بالستیک انصارالله به ترمینال ۳ فرودگاه بین‌المللی ملک خالد در ریاض:
مجروحان: حدود ۴۰ تا ۷۰ نفر
کشته‌شدگان: حدود ۳ تا ۵ نفر
این آمار در حد برآورد اولیه است و هنوز تأیید رسمی آن مشخص نیست.
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73064" target="_blank">📅 18:26 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73062">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=KZBUqYaEpBua4D9I_ILLzvBRjuDfErg9XBtGQTlQPp7odtUjlZT2tg_WNuCRHybBT9LU1SOKDaXmdqa5N9yf9xPa8y4X0hM2zTOnALv3eqA0s5LDmXgkJK7vdT87IBqiPkBReFLdT4N5ftFlK7iRIdz3PEsn6ISX-6p6_wZR-qmnJZhqWB3sRzGcTLq_PLmKrwgY1381gITY4afa6T7rPFZb6Uc8F0BrMImS1orlb46qEaR07aGBLph6bEYs2NzhQKju_ZXFV8P8u--vyhG4nbs40MrXLzEJzGUyQ23zMxT0WuPZ7nBmvxhVrKPJLQDMo63yNoyBzv8xZxhlX8vmIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/23f8abc61b.mp4?token=KZBUqYaEpBua4D9I_ILLzvBRjuDfErg9XBtGQTlQPp7odtUjlZT2tg_WNuCRHybBT9LU1SOKDaXmdqa5N9yf9xPa8y4X0hM2zTOnALv3eqA0s5LDmXgkJK7vdT87IBqiPkBReFLdT4N5ftFlK7iRIdz3PEsn6ISX-6p6_wZR-qmnJZhqWB3sRzGcTLq_PLmKrwgY1381gITY4afa6T7rPFZb6Uc8F0BrMImS1orlb46qEaR07aGBLph6bEYs2NzhQKju_ZXFV8P8u--vyhG4nbs40MrXLzEJzGUyQ23zMxT0WuPZ7nBmvxhVrKPJLQDMo63yNoyBzv8xZxhlX8vmIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از فرودگاه بین‌المللی ملک خالد در ریاض پس از حمله منتسب به حوثی‌ها (انصارالله)
در این تصاویر، آثار خون روی زمین دیده می‌شه و نیروهای امدادی گسترده‌ای در محل حضور دارن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73062" target="_blank">📅 18:21 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73061">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">گزارش‌ها از وقوع حادثه‌ای بزرگ در فرودگاه ریاض؛
گزارش‌ها حاکی از وقوع حادثه‌ای جدی در فرودگاه بین‌المللی ملک خالد در ریاضه. احتمال داده می‌شه یک موشک بالستیک حوثی‌ها (انصارالله) به این فرودگاه اصابت کرده باشه.
تعداد زیادی از نیروهای امدادی و اورژانسی به محل حادثه اعزام شدن.
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/73061" target="_blank">📅 18:18 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73060">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">#فوری
؛ خبرگزاری فرانسه (AFP):
خبرگزاری فرانسه به نقل از سه شاهد عینی گزارش داده که در حال تخلیه افراد از فرودگاه بین‌المللی ملک خالد در ریاض، پایتخت عربستان سعودی، هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73060" target="_blank">📅 18:16 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73059">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSlyOOlAFMXkgoG7SkEyG0Ydvi1qBUtlg5CzAAhdb05oL8jFvT8XgGRRicHTmfbJHMwZKFzZ3z_gxD8BTBtqAV9PoGOg0eo8eW4nd0ah7mAwccoQc_XTzR3EuwDNcg02wwZ5urrAbIJqdfBB4bDp5V_apQlAOKw17b4PVvOiT_n0MtoE6Fz4vkKdDRPqDXAlxFHcWkJCTvlvfkbVWZEcZMkxpGkas-HMD-pJJo_TcXP3hlUzltve5qUbQodantXzMkgkYDwT5P1apmefm7qUsE5QuAR2Og3Ft7PJJqG3L_npZ9cAo8MzfCgEXseV0nkJDZaxTphr8AMMYR2-4jFwx_p0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dc0bb8954.mp4?token=Ef_vdZM32WLV3F0anItSsSyYndkoki0LpdsjJVLDxG9qFpsdNJjiOQ_y_jXcNBYTBihW3m3fCD315UXcbIp2_s672C8zZTUSHFzNOCKVa4A-3Vc78HQwjlV-OiMj1dz3mqXZwBrzMf7iZtB9KEd6qUVkFx6FEpTiOdiD6B98bP_94KXqckuBvHe3hrFA5ulUmbBlNt5BpyMQkgWFrgg3SPcHFaDmTV-HLADQ5cJDpd4LFX-xMRWB6RTkBtZTZ7wPbU7gomQkzcMY3wtmxs8Wij5INfD1IgFzPlFO16chT7jBZxl0upMt2spQJgU3ZX2xM4tY6AwgHCKAwqH3U8TJSlyOOlAFMXkgoG7SkEyG0Ydvi1qBUtlg5CzAAhdb05oL8jFvT8XgGRRicHTmfbJHMwZKFzZ3z_gxD8BTBtqAV9PoGOg0eo8eW4nd0ah7mAwccoQc_XTzR3EuwDNcg02wwZ5urrAbIJqdfBB4bDp5V_apQlAOKw17b4PVvOiT_n0MtoE6Fz4vkKdDRPqDXAlxFHcWkJCTvlvfkbVWZEcZMkxpGkas-HMD-pJJo_TcXP3hlUzltve5qUbQodantXzMkgkYDwT5P1apmefm7qUsE5QuAR2Og3Ft7PJJqG3L_npZ9cAo8MzfCgEXseV0nkJDZaxTphr8AMMYR2-4jFwx_p0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ملکه تایلند برای نخستین بار به تنهایی هدایت یک جنگنده گریپن سوئدی رو بر عهده گرفت و پس از فرود موفق، از پادشاه مدال دریافت کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/73059" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73058">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73058" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73058" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73057">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EQP2TO6OKQrnQ-Ac1k_hOXwPCFMlhMVdEJMMtBg6_PkG0pkKtqiC0i6D9kC86XfwOzgAAAadG5U-ZntCBWr-Aw2ROn6cCJnfaCflRQwjigfFd2r_gKYwLvUW9Ly0aMEMxCPUri5B18isd_NtGq4J4RSEo252o0uKjQ5JtfFmCEQ-Ux7R8E3n_eAY0Ppqyz9crHoQp-2glLeR-0nykaSsuIizv9iunpFAJHaNmkDUCJ7XN8ZrvdeKKGU0xjKooq7_y46CKysNOh_Hjgfloh4fpeDRa9UMIh98axFyLzgHjqbuq2Lzyx29QyWDWSch_60uV3Z0wkE6IJPpNPYILZAvgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
نبرد هیجان انگیز ویارئال
🆚
رئال مادرید رو در
TrexBet
از دست نده!
📉
نگاهی به آمار ۲ تیم در ۵ رویارویی اخیر:
ویارئال: ۲ برد، ۳ شکست و ۱۱ گل زده
رئال مادرید: ۳ برد، ۲ شکست و ۱۰ گل زده
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73057" target="_blank">📅 18:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73056">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=UdxlbNo9b7nf3DCNVDLTy_VkVAK_q7Vz-OlXsaJVmtwnI5AHVHcdouUcTU712cE1fcprHsqFw5b5zYSQdahbTkplILA5zRmvKHMDF_X9ewJBBPjoFc570SM4XZSb-rO-3CsxBymyq-4mNqYgPMf8wHp9OQu2XfrnTsRZQT9QNVEtmtmMOSxU-Qt68wFT5iksbmrxjFpTS4uDO7nTQhKH4gdkeX0EtFrW6WM0MEXzjEOywkvRaleU81d_kN8DFSSrRUmm85oui9_tcJIOflpEkylcZcExtcL9iyaB9uHHsG9xSHLuxSJlESLwSBY5xIJMgmYYNG_tQEfaqijles82doeSdyDZFzLw34acuCbJBBdWJEQEmudxhB7Aq9n9Si0z7SJDKRfj7w-Syypz4t1HWM99Ih6d4CpIrqKCiWXV5xMIDs4Rdwm9CYOJNV_ZKmk5hrauORrolq6jdXTAkKunlrj38H5GIU4KoRmyUubVUVZ5CMRfAXpaCj65rmDxvKCGrBrRrANljmOcxGXn0MzWC9-DxsSawCApZJ8h02F58EMiAgogapLjFkJGg4nlzzWKJOkfy5A4Ibmdb-tmJvzw9O71F8x-1B23Lu2xKmxMa9MmnTqXsxEc75c1ogQ0DLACor6qljN5YTZgkagv0GMIsRvzet1h6GhxCRW0Ippo3bQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c52e5fb32c.mp4?token=UdxlbNo9b7nf3DCNVDLTy_VkVAK_q7Vz-OlXsaJVmtwnI5AHVHcdouUcTU712cE1fcprHsqFw5b5zYSQdahbTkplILA5zRmvKHMDF_X9ewJBBPjoFc570SM4XZSb-rO-3CsxBymyq-4mNqYgPMf8wHp9OQu2XfrnTsRZQT9QNVEtmtmMOSxU-Qt68wFT5iksbmrxjFpTS4uDO7nTQhKH4gdkeX0EtFrW6WM0MEXzjEOywkvRaleU81d_kN8DFSSrRUmm85oui9_tcJIOflpEkylcZcExtcL9iyaB9uHHsG9xSHLuxSJlESLwSBY5xIJMgmYYNG_tQEfaqijles82doeSdyDZFzLw34acuCbJBBdWJEQEmudxhB7Aq9n9Si0z7SJDKRfj7w-Syypz4t1HWM99Ih6d4CpIrqKCiWXV5xMIDs4Rdwm9CYOJNV_ZKmk5hrauORrolq6jdXTAkKunlrj38H5GIU4KoRmyUubVUVZ5CMRfAXpaCj65rmDxvKCGrBrRrANljmOcxGXn0MzWC9-DxsSawCApZJ8h02F58EMiAgogapLjFkJGg4nlzzWKJOkfy5A4Ibmdb-tmJvzw9O71F8x-1B23Lu2xKmxMa9MmnTqXsxEc75c1ogQ0DLACor6qljN5YTZgkagv0GMIsRvzet1h6GhxCRW0Ippo3bQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این دختر خانوم با این پسره تو رابطه اس و که علاوه بره پسره، سگ دوست پسرش هم عاشق دوست دختر پسره شده.
@News_Hut</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/news_hut/73056" target="_blank">📅 17:34 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73055">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/502e54151d.mp4?token=cm2cBCfSibvRQMDV38sL2ErEs-VhUTeSh4_vn3SpAnFFB-Q2QI2qdffaxRsiExI2sEs4cEcAT_sS6peNHmiatD5Jd6v1ecw68d51TdfaPUYTlw2UFYe5UxLjaRYlru8xU65nb1jKHxf7wrRVMFWdthZv4Om_AfEiNTHn9GIWCzDhud-42hcY0DWZdhsgzgfHqEyilAIqWOZ6sKnGISHknIKZ1UpMIqDZYDStgdluwk7Nq5H4pQk-GjjU933WBT1Rboszswr2xLcALwAon5qXD0bZRuSiS8RMcL-yuEAPpts7MemBYc0wzACiWotTm_i4-iUpcYWTSDOEXvw4G1Wqkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/502e54151d.mp4?token=cm2cBCfSibvRQMDV38sL2ErEs-VhUTeSh4_vn3SpAnFFB-Q2QI2qdffaxRsiExI2sEs4cEcAT_sS6peNHmiatD5Jd6v1ecw68d51TdfaPUYTlw2UFYe5UxLjaRYlru8xU65nb1jKHxf7wrRVMFWdthZv4Om_AfEiNTHn9GIWCzDhud-42hcY0DWZdhsgzgfHqEyilAIqWOZ6sKnGISHknIKZ1UpMIqDZYDStgdluwk7Nq5H4pQk-GjjU933WBT1Rboszswr2xLcALwAon5qXD0bZRuSiS8RMcL-yuEAPpts7MemBYc0wzACiWotTm_i4-iUpcYWTSDOEXvw4G1Wqkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاویری از بمباران پادگان سپاه در خرم‌آباد، استان لرستان، در جریان جنگ ۴۰روزه:
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73055" target="_blank">📅 17:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73054">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aLlsqwIwUKenNrqxCBEni7WqxJXFo19TAwJxszV5qeL1Gtlodv2KcJu90pc3ZF4v6pR66kmUEs-DwtYPxLi0BKTPBvB6BIR0fyUmwWr-Emr63bQc5g6qQ_j4W_zXNNtymvef5N4flTKVbFZ_JrfmRqnL6G_nNPKzISystKk6E-PmpipIuu3jDcs_QEybFdvp5WjjiVv3IqCboqiAEXvvjwJVOB6Ukzv6n22hpMwJd3HHLcj3cs3-pX33RqYaHXfoWWcQ9nT_yUuxl6GYw91MOqK_EYGpJCcbh5XuF6iKgrrRXw3Lifw_11gNS0FsLozXKPElrEc3AXJKn28j2DAWeQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
معاریو: آمریکا از اسرائیل خواسته به‌تنهایی به ایران حمله کنه!
طبق این گزارش، واشنگتن توی مذاکرات دو هفته اخیر از اسرائیل خواسته بود بدون مشارکت مستقیم آمریکا، حمله نظامی به ایران رو انجام بده.
هدف آمریکا این بوده که پیش از انتخابات میان‌دوره‌ای نوامبر، هزینه سیاسی حمله به ایران متوجه ترامپ نشه؛ درحالی‌که چنین حمله‌ای می‌تونست از نظر سیاسی به نفع نتانیاهو، پیش از انتخابات اسرائیل در ۲۷ اکتبر، تموم بشه.
ایال زامیر، رئیس ستاد ارتش اسرائیل، هشدار داده بود که ازسرگیری جنگ می‌تونه باعث تعویق انتخابات اسرائیل بشه.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73054" target="_blank">📅 16:33 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73053">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=f7neHfhh40nq6_WDuJ1CI5XoXwg7cUw7kM2H0wJefi_T5bU_cZcngVKoQbd23auqukSEq-cfGq7nwZM6C6wNYzUgQmJ1WnNPRGTNtX5vnS9ikWe15GgKbdymKQwslkpZaSRW0A383YSIPaxcMqFf9JP2pdsyHFTYGLe6iBWi8pC4MXJhu4jbZvj_bC_lWVWkkBX0xmlPUUzVjkDFRb9cD2-NkUry-11pGC7pHZOeaOD0DsgkW9jYCJ_2LLlTaRpwSJTYH9sIKQ8Bdn1dDzYitba8-vohyFqQeeERof8svw63xj0P8wtdMG71XAAXRt5yfPbEKA42Ddjtm6ANi5aNIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1fca26fcca.mp4?token=f7neHfhh40nq6_WDuJ1CI5XoXwg7cUw7kM2H0wJefi_T5bU_cZcngVKoQbd23auqukSEq-cfGq7nwZM6C6wNYzUgQmJ1WnNPRGTNtX5vnS9ikWe15GgKbdymKQwslkpZaSRW0A383YSIPaxcMqFf9JP2pdsyHFTYGLe6iBWi8pC4MXJhu4jbZvj_bC_lWVWkkBX0xmlPUUzVjkDFRb9cD2-NkUry-11pGC7pHZOeaOD0DsgkW9jYCJ_2LLlTaRpwSJTYH9sIKQ8Bdn1dDzYitba8-vohyFqQeeERof8svw63xj0P8wtdMG71XAAXRt5yfPbEKA42Ddjtm6ANi5aNIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظاتی ترسناک و باورنکردنی که امواج عظیم زیر رعد و برق یک کشتی باری غول‌پیکر را ناچیز نشان می‌دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/news_hut/73053" target="_blank">📅 16:20 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73052">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/swy16kgKHKcR3jqlZK_keQO4gkda1YeGwWC8HAjbOSHc67w7su5446qHOl2vL9_Gp9GxIGmRPNE0wK9B-1pUcWdDpyj5GqTbcUuyBsa3a88aB3i_GQXG0yOZRrw6TpH8ALCmhQ2vQP1B5F135Yg7vj6FMDOIL5aBohXKDQ0oAX57q6qO2S3AwP3JAUmKAuXWbVI-ZVgo4jQ8MOzwLTAAjWCRjf-9GH2_Y0B9ADyX_TbQrGQpk3jeoZO7mvL2WDsLOZtTMYxH3Boe6PxEYsyNfzeljn9w2nM_bIbWe0wNNa8EPMDCFYMo3J4q2pN56e6ajs8CJXtWZpuB9RWxKtkEDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:«من به ۸ جنگ پایان دادم و به پایان دادن یا حل‌وفصل ۲ جنگ دیگه هم نزدیکم.
همه گروگان‌های اسرائیلی، از جمله ۲۸ نفر آخر رو، چه زنده و چه کشته‌شده، برگردوندم.
صدها گروگان از کشورهای مختلف جهان رو آزاد کردم و به خونه‌هاشون برگردوندم.
در ونزوئلا در جنگ پیروز شدم و دیکتاتور خشنی رو که با بی‌رحمی اون کشور رو اداره می‌کرد، دستگیر کردم.
همچنین جلوی جمهوری اسلامی ایران، بزرگ‌ترین حامی دولتی تروریسم در جهان، رو گرفتم تا به سلاح هسته‌ای دست پیدا نکنه؛ و خیلی کارهای دیگه!
با وجود همه این کارها، نه من و نه ایالات متحده آمریکا جایزه صلح نوبل رو نگرفتیم. عجب!»
@News_Hut</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/73052" target="_blank">📅 15:43 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73051">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=FyIlJzOEgBwmkVE_31s2GA2jPGb2N04eEk_Fp-02WvAupDnWQSjcYG5gTskltWMYATasq9hAs3X3jwGUfl0vJGZjB6o4BczhGCWuxSuPD_3xmMAl7lxNgHef_VeJ6cMmfP1fQDhJ3ixbBwDd-cSUNkXb9ezEpAp8s6u-3LYgB7TS-SyCorXmehbchDcB3eFAdQGqO4IQrPHAkSIkgp4dCArOp1jy2JuXP6G22Y1X4FECBBo_DHndyIl9ZBZN9QzMMWmlUYAbmfKuSl5thU5MdZUKf_iHcqo8Balwp-92z1XUOoetsiKyOVoeLqN_hp_WFZUKv1bdLOtD8NRmRcLL2A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f583eac4a.mp4?token=FyIlJzOEgBwmkVE_31s2GA2jPGb2N04eEk_Fp-02WvAupDnWQSjcYG5gTskltWMYATasq9hAs3X3jwGUfl0vJGZjB6o4BczhGCWuxSuPD_3xmMAl7lxNgHef_VeJ6cMmfP1fQDhJ3ixbBwDd-cSUNkXb9ezEpAp8s6u-3LYgB7TS-SyCorXmehbchDcB3eFAdQGqO4IQrPHAkSIkgp4dCArOp1jy2JuXP6G22Y1X4FECBBo_DHndyIl9ZBZN9QzMMWmlUYAbmfKuSl5thU5MdZUKf_iHcqo8Balwp-92z1XUOoetsiKyOVoeLqN_hp_WFZUKv1bdLOtD8NRmRcLL2A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهرداری خرمشهر دیده یه سرسره تو پارک شکسته، با خودشون گفتن چکارکنیم چکارنکنیم؟؟
که این نیمه شاهکار رو پیاده کردن :
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/73051" target="_blank">📅 15:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73050">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=Jzrq7bLpzlinotph5b3__Pncucux7cgNCvDeZ3opnjZroaFVpUaMJTCwQFYilaK3Z7Rg-n-ThpNZUgW0_3JslcPtnyhTkqGycwMTkr57Rd8j9mseVE5-hZQiRpLzXtoEnYpxgwsEnT3LfF4kjXv5oo4qipPHjvRnZzQB21jgXOb_hhB6wIqTXxsrbXalZdVYHn-pXHPQbECMmLigQGOktkxFiwFMwTN83CqHI19XGyDlvmaHbHac2Y3M4e0W_CZlZqEZhWAwsak6uUHul__kPDx1jI8E9xLp1Jy6Fg0XE9IWEI6xVCtJG_UKblkYA6Tk-wgaCN33CVrgPkOS4KYjwQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ef585e24.mp4?token=Jzrq7bLpzlinotph5b3__Pncucux7cgNCvDeZ3opnjZroaFVpUaMJTCwQFYilaK3Z7Rg-n-ThpNZUgW0_3JslcPtnyhTkqGycwMTkr57Rd8j9mseVE5-hZQiRpLzXtoEnYpxgwsEnT3LfF4kjXv5oo4qipPHjvRnZzQB21jgXOb_hhB6wIqTXxsrbXalZdVYHn-pXHPQbECMmLigQGOktkxFiwFMwTN83CqHI19XGyDlvmaHbHac2Y3M4e0W_CZlZqEZhWAwsak6uUHul__kPDx1jI8E9xLp1Jy6Fg0XE9IWEI6xVCtJG_UKblkYA6Tk-wgaCN33CVrgPkOS4KYjwQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
نفت ایران مال مردم نیست و متعلق به خدا و پیامبره
مردم  حکومتو انتخاب میکنن فقط و اون حکومته که تصمیم میگیره چطوری نفت استفاده بشه
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73050" target="_blank">📅 15:01 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73049">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/520264f117.mp4?token=oQHzq5pWEIFvLCReTRjAOSb2PPblKOBvnjttlY89AIzCiuYZuSi8oeoD2dLuDSfBoHovUFZojXTlChWqN64d_TGfnR6KuN0SQUo67jDMKPq8m2i67rO5s_J7sjTKRyAAcH_Sfbv55ogciIw9ZHejPHQ-BWNqNPnW9fDyAVA2mXYBRahEnN2BnUTQQCa4f5VbOuVVH0ZV9a-J2VwS_InsshGTKtdSBsa-xe5puEWf7risOjX86mkmC9YQEu0rLZX4Gg8JH-GBb__9kPXbeEs1TxiqVLhrqoBRAXZBRuttcokwmxvDFku6EQzN-AdThkiiuV-JVevUFgzcixGIs0tb7w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/520264f117.mp4?token=oQHzq5pWEIFvLCReTRjAOSb2PPblKOBvnjttlY89AIzCiuYZuSi8oeoD2dLuDSfBoHovUFZojXTlChWqN64d_TGfnR6KuN0SQUo67jDMKPq8m2i67rO5s_J7sjTKRyAAcH_Sfbv55ogciIw9ZHejPHQ-BWNqNPnW9fDyAVA2mXYBRahEnN2BnUTQQCa4f5VbOuVVH0ZV9a-J2VwS_InsshGTKtdSBsa-xe5puEWf7risOjX86mkmC9YQEu0rLZX4Gg8JH-GBb__9kPXbeEs1TxiqVLhrqoBRAXZBRuttcokwmxvDFku6EQzN-AdThkiiuV-JVevUFgzcixGIs0tb7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیوی وایرال شده از اجرای امیرمحمد، نوجوون ارومیه‌ای داخل برنامه Kaos Show ترکیه:
+ این برنامه، عقب‌افتاده‌هایی که تو فضای مجازی معروف شدن رو دعوت میکنه تا مردم بهشون بخندن.
@News_Hut</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/news_hut/73049" target="_blank">📅 14:32 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73048">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=Zc4cuLZdF-vMACrTA27GuFtJ9Wn2wVeZ3u51ajF3jj-p-B918preco8f0U8Y_zVx8rwtIyNHhzlZYY8nMFjAi7hA84uwx6HoANPAJ2xVH8cfqGdO97KN8Acc2vB8eRvTqt-swDPZ7i8bM1OQ_KLLTCOk-9YS6_YhvzxcxNoSntesbS4-Cj4882ix89MIO3euX4R8fwm-RGgjnbWvsME_lP0YLV67KmdXX_SVv_58Cmf6mGaCsVJp0Jl1yiU_VvLN5jdrRCQfkbm8aKNc-tQzAXDbBuqICncspvRWJAu0p6Kc1XUQi_IaORZ5hAxNZNwNt_uxz2DCenUl_YRX2AkYtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/983154ebcc.mp4?token=Zc4cuLZdF-vMACrTA27GuFtJ9Wn2wVeZ3u51ajF3jj-p-B918preco8f0U8Y_zVx8rwtIyNHhzlZYY8nMFjAi7hA84uwx6HoANPAJ2xVH8cfqGdO97KN8Acc2vB8eRvTqt-swDPZ7i8bM1OQ_KLLTCOk-9YS6_YhvzxcxNoSntesbS4-Cj4882ix89MIO3euX4R8fwm-RGgjnbWvsME_lP0YLV67KmdXX_SVv_58Cmf6mGaCsVJp0Jl1yiU_VvLN5jdrRCQfkbm8aKNc-tQzAXDbBuqICncspvRWJAu0p6Kc1XUQi_IaORZ5hAxNZNwNt_uxz2DCenUl_YRX2AkYtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسن نصرالله، رهبر کتلت شده حزب‌الله لبنان، ۲۷ خرداد ۱۳۸۸:
امروز در ایران چیزی به اسم تمدن پارسی وجود ندارد.
آن‌چه در ایران وجود دارد، دین محمدِ عرب است.
موسس جمهوری اسلامی هم عرب بود و عرب‌زاده. امام خامنه‌ای هم عرب است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73048" target="_blank">📅 13:45 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73046">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=Ep2wj9tRDvBDVisg4lPFxtl_ypZluyvX7l2NP8YCW-KG5ejT_UM-FRQ6Y04hq1DhGcNSPEkeRpoSNootvomwph82jrsM5S_EEIY7PwRDsSn6LNsOpQYpqdunnciLVj117MM3cAFnN5V2PKyu9D0oMRBeJXKK9p19Z5gehRa2l1hrvzP9GjCTM3z_ptPwWe1WRX2ksQqVRsPYmNM9C8FW4CZ7qjtfxYzqi8p4oBgkQiTg5R1VWuX1ZeVUJ_Zrt2fBtaHviKTtSXZq8oAKa9KxzE2U_AWshTKBUuPRADYjBQboeH-Jf6TTnyUsAe00kNE9A6cJxfRW7nZqy1WzJmCq2g" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/97e3d7ab08.mov?token=Ep2wj9tRDvBDVisg4lPFxtl_ypZluyvX7l2NP8YCW-KG5ejT_UM-FRQ6Y04hq1DhGcNSPEkeRpoSNootvomwph82jrsM5S_EEIY7PwRDsSn6LNsOpQYpqdunnciLVj117MM3cAFnN5V2PKyu9D0oMRBeJXKK9p19Z5gehRa2l1hrvzP9GjCTM3z_ptPwWe1WRX2ksQqVRsPYmNM9C8FW4CZ7qjtfxYzqi8p4oBgkQiTg5R1VWuX1ZeVUJ_Zrt2fBtaHviKTtSXZq8oAKa9KxzE2U_AWshTKBUuPRADYjBQboeH-Jf6TTnyUsAe00kNE9A6cJxfRW7nZqy1WzJmCq2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیشب صدای این انفجارها توی شرق تهران شنیده شد که گویا تست پدافند بوده!
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73046" target="_blank">📅 12:51 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73043">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/351194ef56.mp4?token=eTHJJZK7OouUc-_dEfVS0yhQp8zoE31Uj45Tt9wphD_AHhoD0HxkRPp7b5KEHEJentKJ7cYlk_b5MG6v8yrjPeYgPPxhRoM0HWNQSc_862oXKYKohavE-UJHgXo1V993MSBN0izsB5kwaSttksxM1Gw9c8rc377c-i52BGDC76-ODKX8kl5eu3sNKpd5cR91oAJkw3WbHoeplYnnbUW66Vp1-dy-BvVRDK5IQSm9rDSFKN01vavCb_k57LDOm26YFDs5i_Qfk0Es28d_wCYUrSwsAKqVxFUHln5iD6S2VBKTDNH7P3XMXR0_5lbO2OXo5odfgqdj52eMb_LInTf_7w" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/351194ef56.mp4?token=eTHJJZK7OouUc-_dEfVS0yhQp8zoE31Uj45Tt9wphD_AHhoD0HxkRPp7b5KEHEJentKJ7cYlk_b5MG6v8yrjPeYgPPxhRoM0HWNQSc_862oXKYKohavE-UJHgXo1V993MSBN0izsB5kwaSttksxM1Gw9c8rc377c-i52BGDC76-ODKX8kl5eu3sNKpd5cR91oAJkw3WbHoeplYnnbUW66Vp1-dy-BvVRDK5IQSm9rDSFKN01vavCb_k57LDOm26YFDs5i_Qfk0Es28d_wCYUrSwsAKqVxFUHln5iD6S2VBKTDNH7P3XMXR0_5lbO2OXo5odfgqdj52eMb_LInTf_7w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پیشرو و هیچکس بعد از ۱۰ سال قهر و دعوا، دوباره باهم داداشی شدن و دیشب کنار هم روی استیج رفتن!
نکته جالب ماجرا این بود که سروش هیچکس فریاد «جاوید شاه» سر می‌داد و سالن رو به لرزه درآورده بود!
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73043" target="_blank">📅 12:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73042">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73042" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73042" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73041">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hcus4LTWo_8zEnmbU_35_F0AgLGz3OHEoVLN0VAi3cEo5pSFvDV0QJBQBrNZSma4uQ_R4SAbC92cqP1vDUI8SpcURFIhI0zmQen_rYHn6eAfIHIX5mn8Hmat6mlqsRI0pDXGRTVGVQoxOSgrrUxDZS1mgRGcXuG-hujGKziU-4iZ9TkoiwdVRaz2oYZL1MIKESh6XXidpTaCO0-xOLWpg8G0BW9KiDP77nFWckHRvfWLzzZNyVqSQGGsgdg5sAA1rMPR53u2Nd-btLnElyZDE0QiymGeSVeB_hx-_vT0P5dR43JaTgVu1d2VazW8pc7KHXN9HuQAu1pkq5augrB9-g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
مچ‌های مهم امروز در سایت بین‌المللی
TrexBet
لیدز
🆚
آرسنال
بورنموث
🆚
چلسی
تاتنهام
🆚
منچستر یونایتد
ختافه
🆚
بارسلونا
ویارئال
🆚
رئال مادرید
بایرن مونیخ
🆚
آگزبورگ
پارما
🆚
اینتر
فروزینونه
🆚
ناپولی
لومان
🆚
پاریسن‌ژرمن
🦖
🦖
🦖
🦖
🦖
بونوس اولین واریز تا سقف ۱۰۰ یورو
🦖
بهترین ضرایب بین تمام سایت‌ها
🦖
واریز آسان و امن از طریق کارت به کارت
انتخابت رو انجام بده و آماده‌ی هیجان باش!
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/73041" target="_blank">📅 12:13 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73040">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=I-pMxFIZXNZZzmw2NRL3UCcRfC_02blPNNfkbvkrDTrUraOmRxdsVrUB4nelRCaTSdg-yjV5t1l4CJ922Uq0OfWggAquqjKpM3LFEv9nVwI6gV-D09Ae_RTJgwyEO7_6votP6FmgAvcrnNuc7bIDALL3m4BXp7gY28UgcLA7c250KsDV0GIXMOtF3AJo8b_JYtFDZR3rNrKlAVPejdI7NuipljSMTvQR30HWWP145lENhPVEroWJhRqAsvMkK85Be5PeSevrDB7p0M2gY9Rkgx1v1JZm4FxtgQSVXMlXsjVqjjErXHqS54i2sggxa_HkI1O8GjXMP-F_tgBl5yQOWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1e742ff38d.mp4?token=I-pMxFIZXNZZzmw2NRL3UCcRfC_02blPNNfkbvkrDTrUraOmRxdsVrUB4nelRCaTSdg-yjV5t1l4CJ922Uq0OfWggAquqjKpM3LFEv9nVwI6gV-D09Ae_RTJgwyEO7_6votP6FmgAvcrnNuc7bIDALL3m4BXp7gY28UgcLA7c250KsDV0GIXMOtF3AJo8b_JYtFDZR3rNrKlAVPejdI7NuipljSMTvQR30HWWP145lENhPVEroWJhRqAsvMkK85Be5PeSevrDB7p0M2gY9Rkgx1v1JZm4FxtgQSVXMlXsjVqjjErXHqS54i2sggxa_HkI1O8GjXMP-F_tgBl5yQOWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میرسلیم:
مرگ مردم در تصادفات رانندگی به علت رانندگی بد آن‌ها است و ارتباطی به کیفیت خودروهای داخلی ندارد.
واردات خودرو خارجی باعث می‌شود کشور پیشرفت نکند.
@News_Hut</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/news_hut/73040" target="_blank">📅 11:27 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73039">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=Ksbn__5ZiULLghTlmFFukEOa54NYdd3rGrZxHr8oxbo5SpWbO0JQAt2arNatgmYyONMsmsFEquEdZ98W0zqImd5Fsv42PpHs29C4aXBckw-WMBbmpUnfl29_fZZHGr65Wj3u6aEH0hbbfCZmbtnnPUdSB_0Veui0JQ0vRS_OMwq89yA2oJRR2jXWVSiyoRATjbSxq-5BrGJn_zykW2BCt1Ai1An-X688LOe0J512H3RHJB7RvYWmU_FANtUeBdCImnCe11DG08MnUS2MfcDnm046iE_8knpdBOGnVeQZVUxLVFPFUQ3t-U4Opdn8gnChg6QBpDavI_YYBQZCoADePQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e55bfab16d.mp4?token=Ksbn__5ZiULLghTlmFFukEOa54NYdd3rGrZxHr8oxbo5SpWbO0JQAt2arNatgmYyONMsmsFEquEdZ98W0zqImd5Fsv42PpHs29C4aXBckw-WMBbmpUnfl29_fZZHGr65Wj3u6aEH0hbbfCZmbtnnPUdSB_0Veui0JQ0vRS_OMwq89yA2oJRR2jXWVSiyoRATjbSxq-5BrGJn_zykW2BCt1Ai1An-X688LOe0J512H3RHJB7RvYWmU_FANtUeBdCImnCe11DG08MnUS2MfcDnm046iE_8knpdBOGnVeQZVUxLVFPFUQ3t-U4Opdn8gnChg6QBpDavI_YYBQZCoADePQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مایک تایسون، بوکسور افسانه‌ای:
«اگر رئیس‌جمهوری مثل دونالد ترامپ وجود نداشت، به‌هیچ‌وجه امکان نداشت امروز اینجا باشم. متشکرم.»
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/73039" target="_blank">📅 10:40 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73038">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d334669b16.mp4?token=C6PabBLjPxRTlktS1D_u7FBrpXndZSmNMU2Z-GIK7WF9rhx2RjJVMUk2GOL5h6LNuUqtTEquv7TkLh_VMxGLLPZepiRynZY9Z615xImqDC7qSBRzEaIttLPGsE_gXWnzm8melMua-iVSNa_oqtW2b9KLQjqllwWUR88v4BDeqif7lwZYWoZvy0XpdO3CTiATxcf1UyVU5U1g8LGPV7XpFSoKjoSVPbLZa4sJIR0QPp3j8Q51gDWrWxaJsn_m7P0LNYXICjOrlLO_urQOEWo-ItYTIQFPdv1JhtuWL7Ixn9Ei1bfAeXqYFH-_bCwuVI3Q0EkeNiEjX4mZ2Cvl-3y-Nw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d334669b16.mp4?token=C6PabBLjPxRTlktS1D_u7FBrpXndZSmNMU2Z-GIK7WF9rhx2RjJVMUk2GOL5h6LNuUqtTEquv7TkLh_VMxGLLPZepiRynZY9Z615xImqDC7qSBRzEaIttLPGsE_gXWnzm8melMua-iVSNa_oqtW2b9KLQjqllwWUR88v4BDeqif7lwZYWoZvy0XpdO3CTiATxcf1UyVU5U1g8LGPV7XpFSoKjoSVPbLZa4sJIR0QPp3j8Q51gDWrWxaJsn_m7P0LNYXICjOrlLO_urQOEWo-ItYTIQFPdv1JhtuWL7Ixn9Ei1bfAeXqYFH-_bCwuVI3Q0EkeNiEjX4mZ2Cvl-3y-Nw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوووری
؛ پرزیدنت ترامپ:
«ایران یا همه‌چیز رو به ما می‌ده، یا دیگه وجود نخواهد داشت. خودشون اینو می‌دونن.»
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/73038" target="_blank">📅 10:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73037">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">میرسلیم:
تیبا با خودروهای خارجی ظرفیت رقابت داره
واردات خودرو باید یک در هزار بشه هموناییم که وارد میشن برای این باشه که ببینیم چطوری ساخته شدن
مجری:
الان چرا کشورای حوزه خلیج فارس همه بنز و ماشینای خارجی سوار میشن ولی ما سمند و تیبا و دنا با این قیمتای بالا سوار بشیم...؟
میرسلیم:
میل و انتخاب خودتونه دیگه
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/73037" target="_blank">📅 10:03 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73036">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">سپاه  تصاویری از حملات پهپادهای «شاهد» و موشک‌های کروز به شناورها در تنگه هرمز منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73036" target="_blank">📅 09:31 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73034">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">ویدئو های وایرال شده از دعوای پشت پارک یه مدرسه دخترونه در تهرانپارس که دو تا اکیپ با دوس پسراشون رفتن داخل پارک بخاطر اینکه یکی از دخترا همزمان با 4 تا دوس پسرِ دوستاش داشته خیانت میکرده به رفیقاش و گرفتن چند نفری زدنش و دوستای دختره هم برای دفاع ازش اومدن!
نکته جالبم اینجاس که چرا دوس پسراشون ایستادن کنار نگاه میکننو نمیرن جلو جداشون کنن و گاهی تشویق هم میکنن که بیشتر بزن هم دیگه رو!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73034" target="_blank">📅 09:02 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73033">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet @FutballFuckBet @FutballFuckBet @FutballFuckBet</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/73033" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73032">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/twp9ZMePXtPZW8_dzQoo0Tt9aOnPTmhZCqJIAtHdRamWKxCBc3l09hWZbqA0lCRFDEfi-vwQyKkVRLOw_OIMipfvT5yWHg_sUkQcNeSxow90T5yXh7JoeGjjS83pIZ2NuY_Bf9Lm6pw7J3tP5QxCvAZtPkBZ55dK4huFOguwkJ1vDGHT9a-U7TtwEh0grYNKgzcfwROMoG4b9MoTxEOu0hLVQhkXO8uQbLGPrfXbVVMKq6NwrpZzeftSqCQpzoIXr7LFWMWDLzGESKIB6sbQ5ag7IPM4Q3jCkkiPmzDjktngVdPJ4_H2N5FKsKgm0XfF-sZjfiCrY6UFYMyqlphQcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet
@FutballFuckBet</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73032" target="_blank">📅 01:55 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73031">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=VGhS-CZQj_OuCxeOHCO6-i7zeEDeli4d35Pw5pJEoin9HjMTN4epec7Owtl49_ZqKjG5toX7eGA4wgTaADLjvAWn4HfU17agh7jfqopZCewK4V-AlrASNOom0Posl2CV-S0WB7YIQbLsqYMQjFJVxMuYYRWOYWtbxauUUnUJCXzFuFfaleuvE7LgxK_xMGDarVPcAjm-V27LIpZaklC5H3h6sTm_uKXp8rFJuGqQTtHxY_vLjxciTCIu7oA7bHaeLOLoXOQObVKFs8tYwRCnhyUh6F-iPr2ek-6NaHRibyt4npfSvFPoe1vWgvoyWLDCYogsIn8OKGCr8SoESdZTPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d4fabef22.mp4?token=VGhS-CZQj_OuCxeOHCO6-i7zeEDeli4d35Pw5pJEoin9HjMTN4epec7Owtl49_ZqKjG5toX7eGA4wgTaADLjvAWn4HfU17agh7jfqopZCewK4V-AlrASNOom0Posl2CV-S0WB7YIQbLsqYMQjFJVxMuYYRWOYWtbxauUUnUJCXzFuFfaleuvE7LgxK_xMGDarVPcAjm-V27LIpZaklC5H3h6sTm_uKXp8rFJuGqQTtHxY_vLjxciTCIu7oA7bHaeLOLoXOQObVKFs8tYwRCnhyUh6F-iPr2ek-6NaHRibyt4npfSvFPoe1vWgvoyWLDCYogsIn8OKGCr8SoESdZTPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ما در هیچ زمانی پیش از انتخابات میان‌دوره‌ای آمریکا در ۳ نوامبر به ایران حمله نخواهیم کرد.</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/73031" target="_blank">📅 01:47 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73030">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JS0fZCymJaUvteCMyT74ncfKHPSyrVJwvW1S1i7bFfM4o6NEx16eb-TJMngYRpGj9kWozWeTF_6Db35v7lowBZICx67BsKkk6V9g2FTOodNZePSLtWrqJCXqhHiA7tRRNLhe5um4D8ytn_IK_QiPCMEbq7rKN8840KTtYsBNs6iF0X3hrjB6D39cKWIOsY7tltRHMTG9I7LRe23YI7xX1yHlnR3yqR-oOUu44z0_ODn_jCxSASzNstk2YAglIKYtvLnhBF3ZVtPVnZ1AYw4_6ch4DEde1GZTxYqcJ2QcF3mbAZ9CUJbYCJ0mHFxAgrlS7V-wXS7zb7ZzswJ6Dk7XsA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛
هشدار امنیتیِ وزارت امور خارجه آمریکا:
به شهروندان آمریکایی هشدار می‌دیم که فورا ایران رو ترک کنن و به هیچ عنوان به این کشور سفر نکنن!
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/73030" target="_blank">📅 01:14 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73029">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از سیریک چندین پهباد/موشک به سمت شناورها در تنگه هرمز شلیک شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/73029" target="_blank">📅 01:05 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73028">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0925073180.mp4?token=GPv7aTiGkF9lo_kf8cJsS2jvVDxwTOJvLSXEFD53klyRrLaFYYXgDY41fLRZVe3_hXXn2AVv2AkpTt6_3H3a9QfFsCXGfhkGxTaLBsRx7eqecpRvCwjGBVZCpfyavqROqwRXmSNIPnNtjNiAAldXeIYbmfsWfZlvBGVVpI_K8g4GLpTRLt1fUcVW9-hT7EtNi9kGIOvQdaX1k-fGfhoulI_lVcyJlKU9p2gjgT8BzYqs1k05SGu5-LpFOzPnvWYqYn-XZFbTP591B1xZJBAUafVUiYTm8S0KNskpfpVyMi3FBMS49FFa2zbhjeCbBL-_cVxCLWOOuJAirH9Be8_F-Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0925073180.mp4?token=GPv7aTiGkF9lo_kf8cJsS2jvVDxwTOJvLSXEFD53klyRrLaFYYXgDY41fLRZVe3_hXXn2AVv2AkpTt6_3H3a9QfFsCXGfhkGxTaLBsRx7eqecpRvCwjGBVZCpfyavqROqwRXmSNIPnNtjNiAAldXeIYbmfsWfZlvBGVVpI_K8g4GLpTRLt1fUcVW9-hT7EtNi9kGIOvQdaX1k-fGfhoulI_lVcyJlKU9p2gjgT8BzYqs1k05SGu5-LpFOzPnvWYqYn-XZFbTP591B1xZJBAUafVUiYTm8S0KNskpfpVyMi3FBMS49FFa2zbhjeCbBL-_cVxCLWOOuJAirH9Be8_F-Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خبرنگار: زلنسکی گفته توافق نفتی شما با پوتین نشونه ضعف شماست.
ترامپ: کی اینو گفته؟
خبرنگار: زلنسکی.
ترامپ: باشه!
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/73028" target="_blank">📅 00:52 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73027">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=UfPHDeTU3M3PyArlVtx7u4yhaxDZ5HLEX2u3MVdUwWwKWKlOj-gsedJ61SXxs767NUDmybeEbTdAnOdeJPsUEwM_5FPbmsarq3cwtGXMHSinKlC8gTrMjO17xooWwfZ1mrMEGEA2NwzNlkPPpEfmhkuRqSY255oPhL1QfmDB-7fN_2ih0pzMegbjik2nW5GvoYnf8w9ToW8zs9LE-_-6ov8eFpxxDhaVdY5kset8xpN_MCqnU-mXfFi42bI598FpZGApcqh45LKDpj_67kDJRm_W3nfg17krqxhB-cQLgiuu7emb31jq9VuaFBgykFujCytP6QjKowfH1aKqB38ZuBxPQmLz7Zki_P7gQb0KAS8sbUQ9JJG_rgarObG_g8ksQxyFFAo9o7lzfeFUNfQUzBzHnALDmdcazwVcYHb_hTdpUz9TZ1yRFd2zp1tgAmmgPR37zoyT8LBuUJBlcf4Ai3enBqFnIlkMgXX8jTTBYW70BQYJnH1Ub6GIWRv7ylkjYUsbvkte83n9rO2FFJejfu2dRY_DyeKZUFa0n3ykw7J96uAGhs3rqtr-mkMMvndgf20pELmDVrXuvZ3vxIFvDv3OF_RMVfcmVuYk7-De5qwjG2VR8l0-ARR7zCLh7AYiQyPlP-qso3Ol_hpfcS3UEVTa8zX3kcySpI9du-i5BkE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9bebfa1213.mp4?token=UfPHDeTU3M3PyArlVtx7u4yhaxDZ5HLEX2u3MVdUwWwKWKlOj-gsedJ61SXxs767NUDmybeEbTdAnOdeJPsUEwM_5FPbmsarq3cwtGXMHSinKlC8gTrMjO17xooWwfZ1mrMEGEA2NwzNlkPPpEfmhkuRqSY255oPhL1QfmDB-7fN_2ih0pzMegbjik2nW5GvoYnf8w9ToW8zs9LE-_-6ov8eFpxxDhaVdY5kset8xpN_MCqnU-mXfFi42bI598FpZGApcqh45LKDpj_67kDJRm_W3nfg17krqxhB-cQLgiuu7emb31jq9VuaFBgykFujCytP6QjKowfH1aKqB38ZuBxPQmLz7Zki_P7gQb0KAS8sbUQ9JJG_rgarObG_g8ksQxyFFAo9o7lzfeFUNfQUzBzHnALDmdcazwVcYHb_hTdpUz9TZ1yRFd2zp1tgAmmgPR37zoyT8LBuUJBlcf4Ai3enBqFnIlkMgXX8jTTBYW70BQYJnH1Ub6GIWRv7ylkjYUsbvkte83n9rO2FFJejfu2dRY_DyeKZUFa0n3ykw7J96uAGhs3rqtr-mkMMvndgf20pELmDVrXuvZ3vxIFvDv3OF_RMVfcmVuYk7-De5qwjG2VR8l0-ARR7zCLh7AYiQyPlP-qso3Ol_hpfcS3UEVTa8zX3kcySpI9du-i5BkE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ:
«توافق نفتی با روسیه خیلی مهمه؛ حجم عظیمی نفت وارد کشورمون می‌شه.
راستش رو بخواید، می‌خوام از رئیس‌جمهور پوتین تشکر کنم.
این نفت هم گازوئیله؛ همون چیزی که ما می‌خوایم. پس ازش تشکر می‌کنم.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/73027" target="_blank">📅 00:50 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73026">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=nIxmkgD0aB-Wo9hYogcvjziewpF6GS2TWYsFaCWQiRoxbcqwu3GZ9XHzHrDDDf5zK09CH0l5Ss1XeqNNGyxPn2vlAAQb2aD-j-v6Nw2ANfWBMz_qa1YeyIf2SEd4vPONNRrUkZPc3aCXXBGzof6MSvR_z7Hm3GftnnMA87fOwWm9JSdaKB0bED8PGJ2vTj3MhXftZ-TBfmJbfwWT69ljWntIu9U1uli9qNr-3N7_UP5sNJuuyYFMBjC5x_2L5M-rJFWnAA_-4I3TK5DXYUiXc3IfrkHzaiVfqdtYSEvcZkCjdiOOdsJSTb-d7kgq3ikCDyibwSh-t8PlmVBjOe0Lr4Z1EiEUtqs8HpagnkDajfIFuu25uxrGRwq3qiASM9ZHI396VX6l443eROxn0s5MhlKcQUKBA7v_UWJly3jHPtAV_D8PUY1YIOxy93oXyviss5iMosiJv5pPGW9T044SH9ytduTFGHlB0D2jzXSbMhl5a8_Bni9KcsKPinFR9YpDub8N_p8y0AApiB5g4i-0uEWC0eo8CXEC_J7-CHYBAYmeYCldAiAk_hiT4JrofGsKNxyS5AeoghujhLlR3hwrI9GYP65h1lGoWIIaT_5FbahL0Eop_-32d8TzBrbfz7-JeSsaxI635iYaiUPjKi42DOM3cIhgg_b6BqVVQZkMies" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffadaf48ae.mp4?token=nIxmkgD0aB-Wo9hYogcvjziewpF6GS2TWYsFaCWQiRoxbcqwu3GZ9XHzHrDDDf5zK09CH0l5Ss1XeqNNGyxPn2vlAAQb2aD-j-v6Nw2ANfWBMz_qa1YeyIf2SEd4vPONNRrUkZPc3aCXXBGzof6MSvR_z7Hm3GftnnMA87fOwWm9JSdaKB0bED8PGJ2vTj3MhXftZ-TBfmJbfwWT69ljWntIu9U1uli9qNr-3N7_UP5sNJuuyYFMBjC5x_2L5M-rJFWnAA_-4I3TK5DXYUiXc3IfrkHzaiVfqdtYSEvcZkCjdiOOdsJSTb-d7kgq3ikCDyibwSh-t8PlmVBjOe0Lr4Z1EiEUtqs8HpagnkDajfIFuu25uxrGRwq3qiASM9ZHI396VX6l443eROxn0s5MhlKcQUKBA7v_UWJly3jHPtAV_D8PUY1YIOxy93oXyviss5iMosiJv5pPGW9T044SH9ytduTFGHlB0D2jzXSbMhl5a8_Bni9KcsKPinFR9YpDub8N_p8y0AApiB5g4i-0uEWC0eo8CXEC_J7-CHYBAYmeYCldAiAk_hiT4JrofGsKNxyS5AeoghujhLlR3hwrI9GYP65h1lGoWIIaT_5FbahL0Eop_-32d8TzBrbfz7-JeSsaxI635iYaiUPjKi42DOM3cIhgg_b6BqVVQZkMies" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ در کنار مایک تایسون در کاخ سفید:
«امروز قرار نیست باهاش مبارزه کنم، اما مدت‌هاست که طرفدارشم. مدت‌هاست با هم دوستیم. هیچ‌کس مثل اون نیست.»
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73026" target="_blank">📅 00:46 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73025">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z2CE5nIOtYwcCRVqvaipI4ZkW1-iqOH17_s0Yu-gHfX9ovAz44R-04Cbd25ghUPrbFNNHxApCHzZSKx_pAljzYMTf7s_wtduD2TP08uYP1wuqaFwEw7LM05mu8xIHHVLOpLCpujha-4gWYJD0fUoR0zy9GgvnycEAVzwLZPAAgwONCFBQOclq5UdoEnoqjyA6uI3VITReVhFuPd2QITHfS6RC8HKAwLF5mqMb4qkk5eYP-fuhRxFsqIvpB6J4BpOo7EeHswSrGqDjTI-zLF61J39vDpIRBD-5l5UOxKda1cs7hYn4VcQEDJoRZvfS8fejbbC_dwq3hBZ--YvVYhPpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#فوری
؛وزارت خزانه‌داری ایالات متحده انجام تراکنش‌های مربوط به فروش، تحویل، تخلیه و واردات سوخت دیزل با منشأ روسیه — از جمله واردات به ایالات متحده — را تا ۷ آوریل ۲۰۲۷ به‌طور موقت مجاز اعلام کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73025" target="_blank">📅 00:25 · 18 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73024">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=tyFqMK5E6XvbvXBFFx293-_3vLZXi8fMto2xHCnNRt-RHtpsQScT8TuKjMUcwlrZCtpNykDjfHi-b03_Nb8dJvHxr1qz0ELeKHeGBp6qWp2nNJiNeQizu_t6zW5UF8ZLOk4JoU-vbBeDkXq-Ld0wvWXvPhJAY63htS6uWS2WR376thNcKp3aZJe42hn_JqPDLk5kOTgfmq5jQzWjbLDiLi-jj2ww64INUJugCJ64cpQizXkiWjk0TvcK34Xen2kD5b48D3KCRfVBTIZX6JTzhQGQ1qsJvaYX27JKMrxEDVDKK9UV2wmTF4AppoX2YrrubE0od4gKxdL05jNVwm1ZRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e6f11119a.mp4?token=tyFqMK5E6XvbvXBFFx293-_3vLZXi8fMto2xHCnNRt-RHtpsQScT8TuKjMUcwlrZCtpNykDjfHi-b03_Nb8dJvHxr1qz0ELeKHeGBp6qWp2nNJiNeQizu_t6zW5UF8ZLOk4JoU-vbBeDkXq-Ld0wvWXvPhJAY63htS6uWS2WR376thNcKp3aZJe42hn_JqPDLk5kOTgfmq5jQzWjbLDiLi-jj2ww64INUJugCJ64cpQizXkiWjk0TvcK34Xen2kD5b48D3KCRfVBTIZX6JTzhQGQ1qsJvaYX27JKMrxEDVDKK9UV2wmTF4AppoX2YrrubE0od4gKxdL05jNVwm1ZRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سال ۱۹۵۴ بمب‌افکن B-57B Canberra نیروی هوایی آمریکا از آزمایش هسته‌ای Castle Bravo فیلم‌برداری کرد
این انفجار در آب‌سنگ مرجانی بیکینی در اقیانوس آرام با قدرت ۱۵ مگاتن انجام شد، حدود هزار برابر قوی‌تر از بمب اتمی هیروشیما.
قدرت انفجار موجب آلودگی رادیواکتیو گسترده در منطقه شد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/73024" target="_blank">📅 23:58 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73023">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vLds-7F__f3hv16u3tEHDhP3mQx4yeWHiu08_y2NEqo8qDS6LxNDjkq8vlmKkmt7YxyTEgZiw_9i0sr8akBs6-5JVKustdt4ktFfgGymUQ_Ft_lHRT5QJCs5TlBWpkF_F8Lc5ggD45h5FbOBygwHQjS1U5udkQRDrESQTCdrLy8kZ8sTjekpJitNzkxu8zi-mT96qGU_Ok3fLL-XvH1MftsGmTPU18geA_dm72UMP7BFiVFWz6OI86frsXRdS9mE2l1nXa3ulq01Rhnysa3RlP2mDv2SvzJjzJDfQUC5mcD6tdvu-IC72bMs-xeFgcoD1ITrGlwBzWZKGqzAjHIMIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ:
من به‌تازگی گفتگویی بسیار موفقیت‌آمیز با ولادیمیر پوتین، رئیس‌جمهور روسیه، داشتم که طی آن توافق شد روسیه بلافاصله بیش از ۳۰۰ هزار تن سوخت دیزل برای بازار آمریکا و جهان تأمین کند؛ همچنین ۵۰۰ هزار تن دیگر در ماه نوامبر و یک میلیون تن بلافاصله پس از آن تحویل داده شود.
علاوه بر این، با توجه به وضعیت پالایشگاه‌های دیزل روسیه، این کشور در مدت‌زمانی کوتاه، ۳ میلیون تن دیگر سوخت دیزل تحویل خواهد داد. با در نظر گرفتن «کنترل کامل» ما بر تنگه هرمز و این خبر عالی درباره انرژی روسیه، قیمت دیزل برای آمریکایی‌ها و در واقع برای تمام جهان، با سرعتی بالا و به شکلی بی‌سابقه کاهش خواهد یافت!
کاهش قیمت‌ها برای آمریکایی‌ها، به‌ویژه کشاورزان، دامداران و رانندگان کامیونِ فوق‌العاده ما، بزرگ‌ترین اولویت من است. این خبری بسیار بزرگ و مهم است. همچنین باید دانست که ایران هرگز به سلاح هسته‌ای دست نخواهد یافت! از توجه شما به این موضوع سپاسگزارم.
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/73023" target="_blank">📅 23:06 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73022">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=JItPmJGgQi7hsfoCCtwwWzR_s69naSoMQ9YQFxCZcmy3iT3pWSqmZEIlDlgOrv0TtER6spCru48FuarplyPkI4J4pzOHNU7XkXxKjlFRebDUkVIIWUn8aZ2vMDrLygKvDPdTJ6czWssdaP04FNsKF_37vWg6ai7RNB1ti4Ql6WeYFKFWQljD9ldOiV-z6Tt_6ntqc2zKrF9K1oti66i_h8FnVyru1Rz1NtcbcOJ75NqU9W1z1VxqPwJ8C4rhzTH9niZvYGIdWaUzUbRYgGcNg7CKxwhAYczGhC74Uza_WMSTFWTW9Pz7z1jXjAsxTRv_j8PMbb1F3rRbX9MMDY7Zfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5846d15ad4.mp4?token=JItPmJGgQi7hsfoCCtwwWzR_s69naSoMQ9YQFxCZcmy3iT3pWSqmZEIlDlgOrv0TtER6spCru48FuarplyPkI4J4pzOHNU7XkXxKjlFRebDUkVIIWUn8aZ2vMDrLygKvDPdTJ6czWssdaP04FNsKF_37vWg6ai7RNB1ti4Ql6WeYFKFWQljD9ldOiV-z6Tt_6ntqc2zKrF9K1oti66i_h8FnVyru1Rz1NtcbcOJ75NqU9W1z1VxqPwJ8C4rhzTH9niZvYGIdWaUzUbRYgGcNg7CKxwhAYczGhC74Uza_WMSTFWTW9Pz7z1jXjAsxTRv_j8PMbb1F3rRbX9MMDY7Zfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دیده شدن پلنگ ایرانی در جاده عسلویه:
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/73022" target="_blank">📅 22:47 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73021">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=Bh1cpk0YFDlqPATAmnyC1nV0U8BUIaEea6ncjvO4jszB9QeaZp72UbPaUIq77dow6yO_w-T33rs5p4LVmPz4BHkekzGwVND1PF7drAHiBOr8Bm2dxbceOiGwK4suH7f_LtpPgS9_YCKrmZTKj8nD-U-JVanSWvO5Ajp37fT_0thRJPOivJra5XSjBeF0XJmh1Uj7uWGDzkJ20PgiD0wCijtsRaaPBMCfc-Cj8lMrLSKmQWVdZ8hXXrwOziPEapVgczj0gAgnHOqrXzT-GgNgxDeGPp2uPxMP7WWdN_Sl168O-8aHraLxOwh_xB1OgpzcDDSQZf7x17yVHKEFPtufgg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9ec656b26d.mp4?token=Bh1cpk0YFDlqPATAmnyC1nV0U8BUIaEea6ncjvO4jszB9QeaZp72UbPaUIq77dow6yO_w-T33rs5p4LVmPz4BHkekzGwVND1PF7drAHiBOr8Bm2dxbceOiGwK4suH7f_LtpPgS9_YCKrmZTKj8nD-U-JVanSWvO5Ajp37fT_0thRJPOivJra5XSjBeF0XJmh1Uj7uWGDzkJ20PgiD0wCijtsRaaPBMCfc-Cj8lMrLSKmQWVdZ8hXXrwOziPEapVgczj0gAgnHOqrXzT-GgNgxDeGPp2uPxMP7WWdN_Sl168O-8aHraLxOwh_xB1OgpzcDDSQZf7x17yVHKEFPtufgg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گروه حامی حمید رسایی، سران نظام رو تهدید کرده و این‌بار گفته‌ «کاری نکنید مهرآباد را برایتان ناامن کنیم»
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/73021" target="_blank">📅 22:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73020">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=focXKGTj4HwfWEF_I-cj9IHw0a2Dews1bph_EsgaMC0gQvIuA0dxeZh0sw5dvHC3CvlCpKsPPH23p5kaek4IT2dmeNqVJk1ybGpqIZ1qeK9L3D-zE4HYnhKo1dUywRWI1s0Hw1JOKzg0w3onkA8M-gviAQbFtUUx8hGpBRnQb-GdOTAS-pf4HjH0_h0AIIIDZkDL4V_dViR5wViYdNoedUIZJBGzAjUIrBmPTdgTzfWaXyKESOXJ1r3_nG4SaUwFA2V4aENQtNs12BVh8jQzbFAQ-bAC90Eq3Pe_dkI3_21gceb6SJNYkLv2yuUqHKG3QeQXDOWYwnYDNHFZ_xh0Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/852188e7d7.mp4?token=focXKGTj4HwfWEF_I-cj9IHw0a2Dews1bph_EsgaMC0gQvIuA0dxeZh0sw5dvHC3CvlCpKsPPH23p5kaek4IT2dmeNqVJk1ybGpqIZ1qeK9L3D-zE4HYnhKo1dUywRWI1s0Hw1JOKzg0w3onkA8M-gviAQbFtUUx8hGpBRnQb-GdOTAS-pf4HjH0_h0AIIIDZkDL4V_dViR5wViYdNoedUIZJBGzAjUIrBmPTdgTzfWaXyKESOXJ1r3_nG4SaUwFA2V4aENQtNs12BVh8jQzbFAQ-bAC90Eq3Pe_dkI3_21gceb6SJNYkLv2yuUqHKG3QeQXDOWYwnYDNHFZ_xh0Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ناوگروه آماده آبی‌خاکی «مکین آیلند | Makin Island» نیروی دریایی آمریکا وارد پرل‌هاربر تو هاوایی شده؛
این ناوگروه بعد از یه توقف کوتاه تو هاوایی، مسیرش رو به سمت غرب ادامه میده و راهی خاورمیانه و منطقه تحت فرماندهی سنتکام میشه.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/73020" target="_blank">📅 21:14 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73019">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">فشار اقتصادی آمریکا علیه ایران؛ واشینگتن به‌دنبال قطع مسیرهای تجاری تهران؛
اسکات بسنت، وزیر خزانه‌داری آمریکا، در گفت‌وگو با شبکه نیوزمکس اعلام کرده که دولت ترامپ قصد دارد فشار اقتصادی بر ایران را به سطحی بی‌سابقه برساند. او از تشدید انزوای اقتصادی ایران و ادامه محاصره بنادر این کشور سخن گفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/73019" target="_blank">📅 21:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73018">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=DjVa-0xpmyNTw9iolqijPzMgKfQ3mJXG_PZ_wsxKw4sNsowKuFFDhkj6v2koyBtgXFm8fH4gDbj7x3bTJjyPXHX6WqPmuQuE4Ofcp3UyjR4R9nNkCH3k6hPkTQWrWdWRIlDVRvBAjC6BLuqcTra1g8cC1SwX5uHfDZC8_8SMbt-c-TcGXuqCXn4y0aP-Fs1DDuDBDq33jEDZiqkz0hvbnHHApA-BeJA4VuQyEbQXs6qEocwUqGiXsqyqX87JOV81PJqZrD7mnG9glxdaCvgSZuH0oVjDegBZNiIkZ8KuAIABVdGJVp7QWmboYxjXD1NweeuzdjVmiiTp2R36_2268T_rNLrFSe4G8TbfYtQgDZJhBTjCDLSjvuCXcn0YB5TJM9p2Eta6GpHSPt5060aOGraOU0gwUpncrAbYe_YOUl9FOVmdLSLCeZbIcwVfWhIj_nTKphp9ftTnNE0O034Dzy9QWG0Y0jnNLBEAHRda9LBLXaXHY6kgvtz08cZ70d_eMILSIfKCe2Jx0bkrCVKgG9ysl9lupneQJS0CWU954e_Jb3DYdr6NlvjWA1P65WyUygBjvwukFgXRN6Cf7q2kYsK0n9rAPpzMJcbWDftm1PaR73odFiJe6lqBPBe6OrkI7qeMCHBODEXakZJKDn7LKex3I4_OU-dDynnk1Rt6PV4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ac3d9705.mp4?token=DjVa-0xpmyNTw9iolqijPzMgKfQ3mJXG_PZ_wsxKw4sNsowKuFFDhkj6v2koyBtgXFm8fH4gDbj7x3bTJjyPXHX6WqPmuQuE4Ofcp3UyjR4R9nNkCH3k6hPkTQWrWdWRIlDVRvBAjC6BLuqcTra1g8cC1SwX5uHfDZC8_8SMbt-c-TcGXuqCXn4y0aP-Fs1DDuDBDq33jEDZiqkz0hvbnHHApA-BeJA4VuQyEbQXs6qEocwUqGiXsqyqX87JOV81PJqZrD7mnG9glxdaCvgSZuH0oVjDegBZNiIkZ8KuAIABVdGJVp7QWmboYxjXD1NweeuzdjVmiiTp2R36_2268T_rNLrFSe4G8TbfYtQgDZJhBTjCDLSjvuCXcn0YB5TJM9p2Eta6GpHSPt5060aOGraOU0gwUpncrAbYe_YOUl9FOVmdLSLCeZbIcwVfWhIj_nTKphp9ftTnNE0O034Dzy9QWG0Y0jnNLBEAHRda9LBLXaXHY6kgvtz08cZ70d_eMILSIfKCe2Jx0bkrCVKgG9ysl9lupneQJS0CWU954e_Jb3DYdr6NlvjWA1P65WyUygBjvwukFgXRN6Cf7q2kYsK0n9rAPpzMJcbWDftm1PaR73odFiJe6lqBPBe6OrkI7qeMCHBODEXakZJKDn7LKex3I4_OU-dDynnk1Rt6PV4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">افزایش چشمگیر پروازهای ترابری آمریکا در ارتباط با خاورمیانه
طی ۲۴ ساعت گذشته تا همین لحظات، تحرکات گسترده هواپیماهای ترابری آمریکا در ارتباط با خاورمیانه ادامه داشته است.
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/73018" target="_blank">📅 20:26 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73017">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">وزیر آموزش‌وپرورش: تعطیلی احتمالی مدارس بر اساس شرایط هر منطقه تعیین می‌شود
.
کاظمی:
در الگوی جدید بازگشایی مدارس، شرایط هر منطقه به‌صورت جداگانه بررسی می‌شود و در مناطقی که خطری دانش‌آموزان و کادر آموزشی را تهدید نمی‌کند، آموزش حضوری در اولویت خواهد بود!
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/73017" target="_blank">📅 20:10 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73016">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">#فوری
؛نحوه فعالیت مدارس هرمزگان از یکشنبه ۱۹ مهرماه ۱۴۰۵
بر اساس تصمیم جدید:
- شنبه ۱۸ مهر:
همه مقاطع در هرمزگان غیرحضوری.
از یکشنبه ۱۹ مهر به بعد:
قشم، سیریک و جاسک:
- شهرها: ترکیبی از حضوری و غیرحضوری (تعیین‌شده توسط مدیر مدرسه).
- روستاها:
حضوری اقتضایی.
بندرعباس:
- سه روز حضوری و دو روز غیرحضوری در هفته (برنامه توسط مدیر مدرسه اعلام می‌شود).
سایر شهرستان‌ها:
- حضوری.
@News_Hut</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/news_hut/73016" target="_blank">📅 19:41 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73015">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=ZVUzxAIqhehAmHOljSNRmFk6nSW-SKr4xQ88LxgT92_DSR8mZJWKvAYgWyXsEIgsB63DDxc7m5ydObXAqmFyfW54WiEo2beNHt3PE6dEUDKjf4Ndt0ebb6QrZwMcop9_oTK7qZYtY_RWeUJ1TyKgWsetzRTwXJPhbJLe14yR_anWUAk6EGU8TXa-1txmr0ajqTDGd_SqQ9SmfkzdOA6H-qwSkkfdvo0653cfFnfs5mSIdonoIrSgt6VmAO39eRsel26g0eQoUyQPD0KC9B5tWnXNSjUcGhWYZd4hHKzCNr_cSll96YewOmQo8V99VkfGyPs9pDSbgDKgtFwBSLoP64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8de0455f4c.mp4?token=ZVUzxAIqhehAmHOljSNRmFk6nSW-SKr4xQ88LxgT92_DSR8mZJWKvAYgWyXsEIgsB63DDxc7m5ydObXAqmFyfW54WiEo2beNHt3PE6dEUDKjf4Ndt0ebb6QrZwMcop9_oTK7qZYtY_RWeUJ1TyKgWsetzRTwXJPhbJLe14yR_anWUAk6EGU8TXa-1txmr0ajqTDGd_SqQ9SmfkzdOA6H-qwSkkfdvo0653cfFnfs5mSIdonoIrSgt6VmAO39eRsel26g0eQoUyQPD0KC9B5tWnXNSjUcGhWYZd4hHKzCNr_cSll96YewOmQo8V99VkfGyPs9pDSbgDKgtFwBSLoP64i-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استاد دانشگاه امام صادق:
دیگه هیچی برای دفاع و حمله نداریم هرچی داشتیمو زدن؛جمهوری اسلامی هیچی نداره دیگه برای حاکمیت.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/73015" target="_blank">📅 19:04 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73012">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cFlgHJDorQ8mDZtihfcTByf3VpqFgKxtprLfTFRSs6m3jdm_JITlfNQORYfQnSlxAboE5Il_BP-lSlOK39dkP_GQfWsoVArfXaAi3SV2cfQaPBGp_ZVMF_7OY6JKxxr5pQQU_Bc8haJn_DL7UTJm_vaQZoDnzb6rCoWftuqay9XzapwzaFh0l_EHGQSCTX-aPsMVxNZ7xtAMjb4I2LSpz_O3olLBEKm3LbHajo_cX1-UqYI4v4eIgHviXYomC2ZhhCVucKT5gKQVj_jH4PTts0ON0nymKKTESxktLkluVIDHw8jrGYUx8zwmY6gq5Ohl7qUBtGHTB__GVMIh5FMfPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WBrnIjrrvRV8S9aC3E-88pLMUkzcvnxR5ioD2VfDGX4kRGKDj74MJwjc6rojj8blQdLyrzcNzzQM7gLYOhAFUC5D8sEiWA6D6AT_Jw22nUSdRdh8gJ6lw3m701vTAnZfTqPDseItLpYC2SIbvptIIMlYMXGBeI5d40xFQ6o7UlKY_C_TMKz_UVCWKaCYq-x1zsMdVPLKoHR0Q3tYmzAM0PNfzAbZfiHr0ccezxLraCwCB3cvAK94Xx-8GWla6Ep1vQvpWN2jaJQUlqu1hvE3iXNc12qquFvEeqKwt6rhEkcmexPgxxIbiqqvCyXEnuAHBycBRODhofp4ugX0f71krQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/305d802103.mp4?token=LepoQwZq2KXhyXlqyhhY-pxGzM0aFtr5wbgSqKOy-nO_un-7TFlHTdnGm7P4dJmjXcgNMwqJPiusrcPwUf7h1Dhjdwa7NExp5MB0r2JIlOn1DOWm-J9gK0WlrGbo59bxl2tXActjo22r27t4GWJpEs543wEe8e6Ky3GkilBX3eQ0twrdXbpNVRIi38n4jKZQqNEADegw6y2tAAxai1-6oJTD-Rxj16EU2noWtpLeWRzI7lLVepfK_N5HGBXerhNPgHTiuBCBjZa3QjF3NGBC-cnQ2Nw1zjfO3JyY9IXEDiRfn54mhhj11Pphv2AIzBHeNNn6vbLOlQVP6I0bODppeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/305d802103.mp4?token=LepoQwZq2KXhyXlqyhhY-pxGzM0aFtr5wbgSqKOy-nO_un-7TFlHTdnGm7P4dJmjXcgNMwqJPiusrcPwUf7h1Dhjdwa7NExp5MB0r2JIlOn1DOWm-J9gK0WlrGbo59bxl2tXActjo22r27t4GWJpEs543wEe8e6Ky3GkilBX3eQ0twrdXbpNVRIi38n4jKZQqNEADegw6y2tAAxai1-6oJTD-Rxj16EU2noWtpLeWRzI7lLVepfK_N5HGBXerhNPgHTiuBCBjZa3QjF3NGBC-cnQ2Nw1zjfO3JyY9IXEDiRfn54mhhj11Pphv2AIzBHeNNn6vbLOlQVP6I0bODppeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو و تصاویر وایرال شده از آخوندفدا‌ها تو شهرستان بابل:
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/73012" target="_blank">📅 18:23 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73009">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/jVv-nICTIUKfsX4NR5KocerZBuFU1lI7dbnVYJpUwmgu_xfR8kl4ngpM093f3wL_Ri_IzLUrgR0GTkT7N0w7kvQwjxJMfY2axzj0jtuKWZAWBRcSrwfKMl8a_YO7I_e9tiXdk8RSdfbQd9fXp-ZS43g8_DVogZWjCE-HRl9LDKD8nM-apNMdtpr3bhJs7winxbpGFh0zqNzZ7Q9-NvkCW8e591POHl_1LsXCXb2jJtKAvf7PxiYR7814NRR7ildWceV4ki8w3BpkF3EHiDvMXtVpY9EKvFLQTBwlfdQuo7SNRtmYG1FHsSKDUtTf0WToInYlbZq_gSo9As40DGZ8CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aJ6zRbG7eWfM4bNCP2UXRrtx5Yd76hrvRKEdfRF5adI371Hw19lHlDDtBm-1-Jr3hSdJaPtncLOm8SFiWFqHPHoqfbnWPzA2XM_vytooYZ5h_wYdRFH48JfP_7SfeIQIRRYyda4RxFGAhck4X4l1Gubp7BxGHldL8NP0c5XHzcvr31TeIeW80BLM-Cwz3MqfR__NscPR6fh_bu7ISXERn9pR6U-Lv7yKnUzowTBzRYtwKBFeLMBep1UYUOJuW3dLBYOx-45U0z_d1hJ9gsWyy--A8Zi0hAug4sRlAMdCeN9565KPgZQZ8tFMgJc9_RaJXVOQH2BlMHIrSkZsmnnf9A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=PqfcP9n5Np3A2aYZad8BUg4a5DJmxrfjlsKQfdzEp4lY-BlRF1hvUJyo8ihBXJJ81fpNzNjhXXch2VIexnnfnovCzerAnG3qw6WAZWVVWl34RecumH20FiRg-s8t3VE0XMfC4SF6PUucZ6vWuuqt0Whb49lGFy1lcizzuVfLKZGJ1188wEQAGylHz4YbKrLkshJxTFi6W40Zi8jllSaFyrz3TvvOlISnoDbP0j3MpQXG6jbVifG_ngdVlaW_u5jLwh-3V8msdi5Sst10qSNQx-vmCpk9uYjKldk8MXRZ4HFk11UrGTmALFbgtXoNpYTn5ke8Ue4-lChgKuE0HZbJGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c93bb666a.mp4?token=PqfcP9n5Np3A2aYZad8BUg4a5DJmxrfjlsKQfdzEp4lY-BlRF1hvUJyo8ihBXJJ81fpNzNjhXXch2VIexnnfnovCzerAnG3qw6WAZWVVWl34RecumH20FiRg-s8t3VE0XMfC4SF6PUucZ6vWuuqt0Whb49lGFy1lcizzuVfLKZGJ1188wEQAGylHz4YbKrLkshJxTFi6W40Zi8jllSaFyrz3TvvOlISnoDbP0j3MpQXG6jbVifG_ngdVlaW_u5jLwh-3V8msdi5Sst10qSNQx-vmCpk9uYjKldk8MXRZ4HFk11UrGTmALFbgtXoNpYTn5ke8Ue4-lChgKuE0HZbJGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حملات هوایی عربستان به صنعا پایتخت یمن:
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/73009" target="_blank">📅 17:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73008">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Qv6pfbxyl8-hFK1jHPt3OZqb1Rh2UGvxlzryBbEW60a2Ht6B2uNG2vX3m047TLw6E5QeY-4-0PItCRP0VCrQP9L_2wtp_hzGHP7TqO4H2pHEkIBS5hy_6WGvEQNG7WptoQ-IbNSnh_hcjKzILS118Z-sy0d7Wx8HEXnicQGp4O3Cq-_faJEpU9SlI2tUrMmU74noASIotd95fgK5RhPiLi_HW3pqwevi1qnzrnHaPbRlxojpXq2rbJjsk53bmgxgDLz-IPxhO2tfMIAWCJVhTzMHcYqxf2rkkAj7JVIr_xs14p3tK2ea6cksj03FOtOGbNBg9qzhlZPZ12kVD7HGxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نیروی دریایی سپاه پاسداران:
از الان به بعد برخورد با شناورهای متخلف محدود به تنگه هرمز نخواهد بود و هر شناوری که از مسیر غیرمجاز تنگه هرمز عبور کنه در سراسر منطقه تحت تعقیب قرار‌می‌گیره و حتما تنبیه می‌شه.
@News_Hut</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/73008" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73007">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">trexbet.apk</div>
  <div class="tg-doc-extra">45.4 MB</div>
</div>
<a href="https://t.me/news_hut/73007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🦖
اپلیکیشن رسمی و بدون فیلترینگ
TrexBet
📝
ورود و ثبت‌نام سریع
⚡
سریع، حرفه‌ای و همیشه در دسترس!</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/73007" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73006">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jqxbSPVb0uqsL57WqCfAKNp3mzn4LNS9HsoIL7ko550EnCEUmyPoos2J8qsBe73q2RNYu2NwNTRouB8Dj-g3muvEiDyDUzHFKtCUpQzt7a-J0Q67CSoqFG-EznAJoVfPns0399G6ed3sr4PGvPbdYHCYmseW6sHEC0ykHq6xn-DqvJ3m01Bb-SiquL-zxNu4P93FXUWEb4kTsIQpF3qMmNNse48HCFNjpiZW9ZlK_SytgkQIIujG0Con-6WrVANY0Qc9xgYUDoyop8CF3ahv_o-fYPaYUg6omqYv0m8ZLGee5yVEu0LPMRFAZtcKv8MXeLLzJMOTbyqC-h1nFJXb0w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🦖
فقط یک بازی از میکس‌ت لوز شده؟
پولت برمی‌گرده!
میکس می‌بندی، هیجان بالا میره، اما یکی از انتخاب‌هات خراب می‌شه؟
با پیشنهاد ویژه
TrexBet
، در صورت رعایت شرایط، می‌تونی
۱۰۰٪ مبلغ شرطت رو پس بگیری
.
🦖
قوانین رو در سایت مطالعه کنید
🦖
🦖
🦖
🦖
🦖
بونوس صدرصدی اولین واریز
🦖
واریز آسان، برداشت سریع
🦖
سرعت بالا، طراحی حرفه ای و تجربه ای متفاوت
TREXBET — PLAY. PREDICT. WIN.
https://TrexBet.com
T.me/TrexBet_Ir</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/73006" target="_blank">📅 17:46 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73005">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=lvv5OxqNXvQNNzJlWac3kpEBZGmEZ5-rMTNx0qVi-k8GWipelE30Sene_vssuI4SWB4i0B0fe3qMqCX-NTeMn-BVXt7gYhfA_AyRgJe2fC7A9uDIvs32GA3VHa9YxU2v4Qa2s3lguJbnrTQGSDOfK5dAGFnBq78v7tGANq-h534z_1JhUq1MHe4HXmvkdurFtA--I1j2VJMjO58iUTqwqkaANaYLeYebn2rAPJ2YJhzAqI7RB2EZ0p93tA02Ae-6w0ab7h1u43BEVirVmOlIhJPAimtGrn5zMgsuk1ctJ4zavywO-vY4scEpiv0FKzyNP38OkAVNqMD2cTcTkCaF5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c0f7d86e64.mp4?token=lvv5OxqNXvQNNzJlWac3kpEBZGmEZ5-rMTNx0qVi-k8GWipelE30Sene_vssuI4SWB4i0B0fe3qMqCX-NTeMn-BVXt7gYhfA_AyRgJe2fC7A9uDIvs32GA3VHa9YxU2v4Qa2s3lguJbnrTQGSDOfK5dAGFnBq78v7tGANq-h534z_1JhUq1MHe4HXmvkdurFtA--I1j2VJMjO58iUTqwqkaANaYLeYebn2rAPJ2YJhzAqI7RB2EZ0p93tA02Ae-6w0ab7h1u43BEVirVmOlIhJPAimtGrn5zMgsuk1ctJ4zavywO-vY4scEpiv0FKzyNP38OkAVNqMD2cTcTkCaF5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یکی از هواداران حکومت : رفتم تو گونی!
رفتیم جلوی مجلس تجمع کردیم پرایوت نامبر بهمون زنگ زدن
با یه شماره به من زنگ زدن از اطلاعات سپاه بهم گفتن بیا اطلاعات باید توضیح بدی
هیچکس با کسایی که هنجار شکنی میکنن و پست های زشت میزارن و کاریکاتور های زشت و زننده میزارن کاری نداره
بعد من که براساس قران عمل کردم ، منو خواستن احضار بشم
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/73005" target="_blank">📅 17:43 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73003">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86531200e8.mp4?token=tWohgXsaU-roDW65ZG40vMEHKu0YT8kbC8OvT-PYRE_DTI78ei-gkzlNJ6Udbhr_gNxUhdvMwb-fEp2XHCBLB_hMHKt7EelDFrGPU3AzkTualeiZTPMc7bIu0EAU_I_bIMJSg1y9kiRu1PThosw-3qYSGyxwMRbCvFxosWUe-nk_H46PpWNbx8ETXh6doxwHGYsBSmH87hTplJfo4B8RbMnydsARLWHR2TE1LoATtI8vZE-xpDP6zCg4BHSa0QpKQACI2Dauo6XqMpZtSmyU-qlveJHAAMA6zMK9g2L6mnj1-qPaK5FAZTEoiZkYmNL-hnCNs7y_xBe29I8oy1GkUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86531200e8.mp4?token=tWohgXsaU-roDW65ZG40vMEHKu0YT8kbC8OvT-PYRE_DTI78ei-gkzlNJ6Udbhr_gNxUhdvMwb-fEp2XHCBLB_hMHKt7EelDFrGPU3AzkTualeiZTPMc7bIu0EAU_I_bIMJSg1y9kiRu1PThosw-3qYSGyxwMRbCvFxosWUe-nk_H46PpWNbx8ETXh6doxwHGYsBSmH87hTplJfo4B8RbMnydsARLWHR2TE1LoATtI8vZE-xpDP6zCg4BHSa0QpKQACI2Dauo6XqMpZtSmyU-qlveJHAAMA6zMK9g2L6mnj1-qPaK5FAZTEoiZkYmNL-hnCNs7y_xBe29I8oy1GkUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#فوری
؛درگیری مسلحانه در چشم‌زیارت زاهدان؛ اعزام گسترده نیروهای نظامی؛
به گزارش حال‌وش، در پی حمله مسلحانه به یک خودروی حامل نیروهای نظامی در منطقه چشم‌زیارت زاهدان، ده‌ها خودروی نظامی و امنیتی به منطقه اعزام شده‌اند و پرواز یک بالگرد نظامی نیز گزارش شده است.
هم‌زمان، رسانه‌های حکومتی از انفجار بمب کنار جاده‌ای در مسیر یکی از خودروهای انتظامی استان خبر داده‌اند. برخی منابع محلی نیز از کشته‌شدن معاون اجتماعی انتظامی استان در این حادثه خبر داده‌اند؛ با این حال، جزئیات و آمار تلفات هنوز به‌طور مستقل تأیید نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/news_hut/73003" target="_blank">📅 17:05 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73002">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ptY5PmyJfG1-vnc8z9q2Z0cWKbMHtZ_oqt9mwjyLo4VqSYt3upGbC77C9B3pUonxu7sRJ0k77a4iMY0GRZ26y4RfFyY-kW6K9Zm7RYND0cqLVL0hD3AozfMs2Qpu0GCqeBsyZd4y_IpKpPhQuH6BkDHCE6jSgJ79mwahqZG7LpDpmd_NaNdMW8EIOGQQdFFP6--BVsPvQHSr0UMfruz_gRgcJyw4_ReojbKsU4nTq-o9oM_FUI6p3LZkAm1oX2kB4e3HoSrlNXznqbmke73VMfLLEI5fe40OiZcxh6RCLcDCGWwu66IoN_MbY7DrpISXBcK5r9FwOZlLa1BkhNt9qw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حال‌وش: کشته‌شدن ۱۲ نیروی نظامی در حملات ۴۸ ساعت گذشته
به گزارش حال‌وش، در حملات مسلحانه اخیر در سیستان‌وبلوچستان، ۱۲ نیروی نظامی کشته شده‌اند. در حمله به دو خودروی نظامی در منطقه کرین‌دوک نیکشهر، محمدرضا اوکاتی کشته و پنج نفر مجروح شدند. همچنین سرگرد مهدی جمشیدی در فاریاب و ستوان‌سوم وحید عنایت و عباس آقایی در محور لخشک زاهدان کشته شدند.
هویت سایر کشته‌شدگان هنوز احراز نشده است.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/73002" target="_blank">📅 16:56 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73001">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=BwTrDe52E310jG9yBYmjAXRgeHi7zVAC2LAsl3W1OXd-RudOJ2PlyntczIikoBBGqwmo5pxC9nnFX0UaXB2mQHs4s1b9CVZAGfttlHRZ4Cs6A3JbAJ7yawf9dmlMa-KFlQ2jwI9UGGs0BJ26EMVH1ccgXIbOjC3Z4H3hYK9Jx0iIyjHVFxO_iK9yxp7IWK8WEU3xyrtUWPxvGuSrK0qZqceOXYALcCmQG1KNPuht_vAVoLAPw5FTFg33xGs58eo1JbxCHd78y_Zl5jhkalxyyDTfmiDdzboKx6iOjonT7SuuojreAwc5o4f3MYBeJySGHotU44S9tKKJbgipwr8B7Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/487ed2a10b.mp4?token=BwTrDe52E310jG9yBYmjAXRgeHi7zVAC2LAsl3W1OXd-RudOJ2PlyntczIikoBBGqwmo5pxC9nnFX0UaXB2mQHs4s1b9CVZAGfttlHRZ4Cs6A3JbAJ7yawf9dmlMa-KFlQ2jwI9UGGs0BJ26EMVH1ccgXIbOjC3Z4H3hYK9Jx0iIyjHVFxO_iK9yxp7IWK8WEU3xyrtUWPxvGuSrK0qZqceOXYALcCmQG1KNPuht_vAVoLAPw5FTFg33xGs58eo1JbxCHd78y_Zl5jhkalxyyDTfmiDdzboKx6iOjonT7SuuojreAwc5o4f3MYBeJySGHotU44S9tKKJbgipwr8B7Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طرف برای نامزدش یه شب رویایی رمانتیک ساخته واسش گل خریده کنارش یه ایفون 18 پرومکس ۲۵۶ گیگ هم بهش هدیه داده، دختره همون لحظه میگه ۲۵۶ گیگ چیه اخه ۱ ترابایت میخواستم!
@News_Hut</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/news_hut/73001" target="_blank">📅 16:31 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-73000">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=RkFBHtIVCXBqOGDlv4wcj2fpsF5iwrI_XHVJNKZTzNSf8bWDBLMAhHX3TAAzq5s9lbkLgzUqRksFyhoG3wADNCsbMOY3HBa6WLkO5U7W0aqtGfNzKVZymEG_gYxJPKsRCKGCwcZ_IBpOi7A2cwySAJDamiJMg02TvleLiXzyWo_3AQQx6g-Ve2JPG-ebGBjfIB-2qs8RSgNqfKkwfvSyr6YpTAZ8i11g0oCFMo2UPEJuJEPgWV2ltBTSCzzax_FXN43YlgFkKqIKg49_RDJf7mRXgTgQoiwpLjBSqbj155S55GN3ahTxq7lmWlM6Yi6XCPuk3S32fSaDOXNfWhqCnyP-y9LQBa_Ao4RiDYD2hSIGgREsIEdNUrW1d04SdydbsqW33lQJA47LE8mQVFhm95C3FoNE1COUpTh0N9q4ULnsm78JnMsiDhukgZCLqF3M3EHG7v8tIEirkfUJOYYKa47bM3tvNjA77fHhCRFx0wm0GWKcUv25IBePS4YW-6ZNcYkK_QlsqHTAYUx1QfceKX6DjzK1tjijsnvScBn-S2MB83Qiswsh7mubLWgPRAgd7HtNq04-QYRxTJXcaKQXB7_HQX8h06-m1VMCJ8nhdWCEuTCic9n8__MJdiJUfHgbL7qL6yCXIW2aueVXqKnKrGm5zonm6p5OLhzAYZUBESI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9eb6da5f21.mp4?token=RkFBHtIVCXBqOGDlv4wcj2fpsF5iwrI_XHVJNKZTzNSf8bWDBLMAhHX3TAAzq5s9lbkLgzUqRksFyhoG3wADNCsbMOY3HBa6WLkO5U7W0aqtGfNzKVZymEG_gYxJPKsRCKGCwcZ_IBpOi7A2cwySAJDamiJMg02TvleLiXzyWo_3AQQx6g-Ve2JPG-ebGBjfIB-2qs8RSgNqfKkwfvSyr6YpTAZ8i11g0oCFMo2UPEJuJEPgWV2ltBTSCzzax_FXN43YlgFkKqIKg49_RDJf7mRXgTgQoiwpLjBSqbj155S55GN3ahTxq7lmWlM6Yi6XCPuk3S32fSaDOXNfWhqCnyP-y9LQBa_Ao4RiDYD2hSIGgREsIEdNUrW1d04SdydbsqW33lQJA47LE8mQVFhm95C3FoNE1COUpTh0N9q4ULnsm78JnMsiDhukgZCLqF3M3EHG7v8tIEirkfUJOYYKa47bM3tvNjA77fHhCRFx0wm0GWKcUv25IBePS4YW-6ZNcYkK_QlsqHTAYUx1QfceKX6DjzK1tjijsnvScBn-S2MB83Qiswsh7mubLWgPRAgd7HtNq04-QYRxTJXcaKQXB7_HQX8h06-m1VMCJ8nhdWCEuTCic9n8__MJdiJUfHgbL7qL6yCXIW2aueVXqKnKrGm5zonm6p5OLhzAYZUBESI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صحبت‌های یه جراح و متخصص زنان :
این خانم 16 ساله بعد اولین رابطه‌اش تو شب اول ازدواج (شب زفاف) دچار خونریزی شدید شده ولی چون فکر می‌کرده بخاطر پارگی پرده‌‌شه، نیومده پیش دکتر و الان هموگلوبینش چندین واحد افت کرده!
در واقع شوهرش فکر می‌کرده داره کابینت نصب می‌کنه و بی‌دین زده همزمان پرده، پرینه و فورشت رو باهم پاره کرده.
اصلا پارگی پرده خونریزی زیادی نداره، هرگونه خون‌ریزی بعد رابطه رو لطفا جدی بگیرید...
@News_Hut</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/news_hut/73000" target="_blank">📅 16:02 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72999">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=dzHuqZIJPLxNmtQJX6uiyKFHnej0v0f2AsC1cHxSPqvAKE0rYuBHGJUT8v-2m5HUboIlfBTCwOHIxu7bfxVkBnBvM0Ikw24Pa6dk3lP19zP9ODseR_v-6GCOBiP7w9ESG1klIo8A8vBlNOj5SsO929FkG3Ri4LGwY59RMA33H6JsGtUbD-wT2QAd42_HMzspjx1_jMO7Xz8OXW3-HEw7XM59B0j9ahEzf58TU7_3KXYfUxqA89IxyOwyLG0UE-9uekCPgws4ytT0EkKSpO9hPTcjMbewXePMYh_WrUlO0LpnW9ufAQGA2p6xREnjCPnV01Jxk4mDXmSnpRYy0BcoNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bae6808a3e.mp4?token=dzHuqZIJPLxNmtQJX6uiyKFHnej0v0f2AsC1cHxSPqvAKE0rYuBHGJUT8v-2m5HUboIlfBTCwOHIxu7bfxVkBnBvM0Ikw24Pa6dk3lP19zP9ODseR_v-6GCOBiP7w9ESG1klIo8A8vBlNOj5SsO929FkG3Ri4LGwY59RMA33H6JsGtUbD-wT2QAd42_HMzspjx1_jMO7Xz8OXW3-HEw7XM59B0j9ahEzf58TU7_3KXYfUxqA89IxyOwyLG0UE-9uekCPgws4ytT0EkKSpO9hPTcjMbewXePMYh_WrUlO0LpnW9ufAQGA2p6xREnjCPnV01Jxk4mDXmSnpRYy0BcoNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حزب‌الله حدود ۲۰۰ میلیون دلار از ایران گرفته تا بین لبنانی‌هایی که در جنگ امسال با اسرائیل آواره شدن، کمک مالی توزیع کنه!!!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/news_hut/72999" target="_blank">📅 15:32 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72998">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=HicXam3NTg6G3IXxJKiLXnXRl_48f_RL-bmdYrbvW8aHbuLnriElsNSkmBF1YGvZJ6NOZAOdXkTwqV3pQmAMDEEI8rZI2AbflrEun4zYR-3xbhsQZILlGN-gaxIIvnINsJRHLiVsH7F0JjCvq9u0zuRBj11ksuzqLpuQeBNzxVBdjfLJwk8iwHlVdH5ynDQil_6tIbyQaVwNmIYPl5_H4OeWsnwsVTp3Yff4tky4iznLlF9BMsBo1dGjvj8BM_Zb7KkxcxX3-qI8c4VBnZgD-Za5AHc6oSt_NQKI5oXVG2-VuCCjPP1CJiTI8_9BSkR-Ber-j0MJEuCdJxC1byiKEA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed5ddc3810.mp4?token=HicXam3NTg6G3IXxJKiLXnXRl_48f_RL-bmdYrbvW8aHbuLnriElsNSkmBF1YGvZJ6NOZAOdXkTwqV3pQmAMDEEI8rZI2AbflrEun4zYR-3xbhsQZILlGN-gaxIIvnINsJRHLiVsH7F0JjCvq9u0zuRBj11ksuzqLpuQeBNzxVBdjfLJwk8iwHlVdH5ynDQil_6tIbyQaVwNmIYPl5_H4OeWsnwsVTp3Yff4tky4iznLlF9BMsBo1dGjvj8BM_Zb7KkxcxX3-qI8c4VBnZgD-Za5AHc6oSt_NQKI5oXVG2-VuCCjPP1CJiTI8_9BSkR-Ber-j0MJEuCdJxC1byiKEA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لحظه حمله پهپاد هرمس هرون تی پی اسرائیل به نیروهای گردان پدافند لشکر3 حمزه سیدالشهدا سپاه در آذربایجان غربی در جنگ ۴۰ روزه
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/72998" target="_blank">📅 15:00 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72997">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Sndy1urYHPLILPiNc78L-ypBbLnbeuEFF6MTVZHGYRB5_j2snaYoJUMaahvRsAYUWzfXkwmDRlKig73K793yu-lb7jl6UHcCdCQ7xEe_Prdzd8qosn3q0V1S5SHf-EPnlELcxC3jKBuJE92xgxEWALvf8FApx1Vcbl4MpKEm3T94OIx1Np6LVZlN_vn9WUuOkWZfsjgmTjSqzxatKyqiDV6g3QeWECuYC_fp5J-n3TSPVUs3oBmY5qqAIjmCq6lxoYD5mYf9A2BNZh18rdXnsWOnE_AfYPRj6IxYEOEGHD5NpiJsd1BwVKIdPwIeoow8R7rZyGXVHZRBMo4suUsINQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هشدار امنیتی جدید سفارت آمریکا در اردن درباره احتمال اختلال در پروازهای منطقه
؛
سفارت آمریکا در اَمان بار دیگر به شهروندان آمریکایی در خاورمیانه هشدار داد و با اشاره به احتمال تشدید تنش‌های منطقه‌ای، درباره لغو پروازها، بسته‌شدن حریم هوایی و اختلال در سفرهای هوایی هشدار داد.
@News_Hut</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/news_hut/72997" target="_blank">📅 14:16 · 17 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-72996">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANX27WqwQ4VeM9d0bAQZXlrRf17M2CnF7p321Ltnggy4vhXsplVcJ9esaNfNikxl75Z9_WT1YoYxvBlrs48iYBNiXDUfeq7Q_EihpF_e7JPVpqz6o5_IqBx716Dysam8AU3ADQABZgk7LheJ4uSJPcDT7UEK42SVBzraAbUQbYOcTHUfPu_H5P__Y-h6PL9CuJQVbYdtSpIyAFhvnoz2RD1p50IR7A7EXyrGyX-XLUmn4XhlSFAP154OncoGVcDv1bIOc6w8QK3XuAn5WWrmM5OjRqlys0FEk7LPUahCMz8A87j033fr65yNZYQ1Dc2hmOr3XV6wUfU6bYMpuG6c9sE8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a562a527a7.mp4?token=C5CVhRLau28CPex5vYqcRelVpvBQUp1vEbYuOvZqxrlLx0DlpFIbjSa0gBuClfKVRGPI8LaywLR5q5bjohb08rbzFUeot7BG9KpeRdDDONj5xttr3jltcNhMRvGes8q_NDxG0tujtFMt3PK27UZTkn3L8jITslYWtVJiQwQ3c0v6hWcSIVgWCDRJKhCBRx2OCcjsGHklAe_kCQ15OZ20LrW2mkBc-inugiIwaoXOCTy86dGo20M3OZIXa8ZdJ7ResYQF4_z2CEKMmYZfJ8_EKwA7PyZ1rASfW0Nqc2ekh0--VPDnRsPT0c5QvQjhAu2voeqOXG8FCGFHD__SAPyANX27WqwQ4VeM9d0bAQZXlrRf17M2CnF7p321Ltnggy4vhXsplVcJ9esaNfNikxl75Z9_WT1YoYxvBlrs48iYBNiXDUfeq7Q_EihpF_e7JPVpqz6o5_IqBx716Dysam8AU3ADQABZgk7LheJ4uSJPcDT7UEK42SVBzraAbUQbYOcTHUfPu_H5P__Y-h6PL9CuJQVbYdtSpIyAFhvnoz2RD1p50IR7A7EXyrGyX-XLUmn4XhlSFAP154OncoGVcDv1bIOc6w8QK3XuAn5WWrmM5OjRqlys0FEk7LPUahCMz8A87j033fr65yNZYQ1Dc2hmOr3XV6wUfU6bYMpuG6c9sE8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار شده ۱۱۰ هکتار از چابهار رو بدیم به مردم افغانستان تا بتونن یه سرزمین متعلق به خودشون داشته باشن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/72996" target="_blank">📅 13:32 · 17 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
