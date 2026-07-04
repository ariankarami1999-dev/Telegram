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
<img src="https://cdn5.telesco.pe/file/DPP5HhYYUGYjyVXrL_7I4Z3Ky7Ov59Ar0OL3a2X0GauUquZ4Kxdq7L7tp3IK-wJfxR0g3ZiHw2OL8Lyb2j646j65fJLOiKpDEFH9bX7BhmWV6lU72bGp03gHg0RZA-oUsv8ZT338Sjj9dhq2tRATaaeG30ym7oVsqvrWiPNdSL5YKq1SHMwkc37Ew7lSVXTgVMYZEOPIDhuhT82pSyHehlsiiTXSxSAYRQlUTg1AVlnn8RJtUJVRcHWrQteDbVuWT4ivknpxD9nnxqDpgWp8BAySCGDojkCsxRzaTrT7WGewZ_xS-Mlise-UGV7HKPQTZvYFQVJyEXoe_rsC6NbsCw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 642K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-13 17:36:18</div>
<hr>

<div class="tg-post" id="msg-98173">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">👀
▶️
🇨🇻
کشور زیبای کیپ‌ورد که علاوه بر فوتبال جذابش، این جاذبه‌های دیدنی رو هم داره
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 307 · <a href="https://t.me/Futball180TV/98173" target="_blank">📅 17:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98172">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a6f3f631a.mp4?token=LgL8TG_B-DM_dIXDVt4g-8JCLxsJ8PGv4iHGAUaHGaazCSHmWu4TAohUR2ilTRXEYyR2FCHkgpzTUQTcjdyGsxuIiEaZD55v3YaOm4eX_buwpAoSujYJPJBiiTJLeod0o7ByqaqUfYaEOp7DF2Qt1V0dXnezRayofl6fOi2Y1wOsjHAaKjsNHlcZJPN469zKfi0MHuonhkbqBvQsLha8BlmqhJKy0gm1HDDlvx9qMD9FG6EMPL77paHbAIUTUWhA3WK7hiPwrjt97yb9SlK6RmTwgL4aIiwDMl2FiAtAJhpf1t_sniV5xQukXtMOgOFFpPQVtL_sD8ahI7i2h6H_Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴󠁧󠁢󠁥󠁮󠁧󠁿
🇲🇽
هوادارای خانم انگلیس در آستانه بازی با مکزیک که پسرای مکزیکی‌رو تو خماری گذاشتن
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.98K · <a href="https://t.me/Futball180TV/98172" target="_blank">📅 17:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98171">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mPZoNPfkkWFkPnksXzK9IwkYDilCZM4Jp5NZwpZ-a1stOeSpp-ugqaqZQjrRqPhrDdOk9Rfi4P0kZW99pmqkuf3zZzx1shzU3kb1_745F912rI5OmgATx9S7UYXM1JB_RURZ8RAHk7VlUdMSyQoq_blzSIP5jI_h610gAXLqFA1goamksSisEUeiRJ9lvJG9XJ1HL3tiVDD63OcUxxcFeWQSI8ZnVTN_k6vuffkf8RaxCaNPRklrBcYv37vXXe0-ZTIWJ58Sc6lCw1qGEA15RQ1CBWqxElZjfMoD632635STuqnzG-Rx4lJ8fDPbY7yIvQQ66WBChb10wzoD5DrQ_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
⚽️
⚪️
فوری از آاس:
باشگاه رئال مادرید در این تابستان با هیچ هافبک دیگری قرارداد نخواهد بست. این باشگاه با جذب برناردو سیلوا به عنوان تنها گزینه در این پست، رضایت خواهد داد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 4.59K · <a href="https://t.me/Futball180TV/98171" target="_blank">📅 17:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98170">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=babGz-6iAIxqukzJHl458u1RSKgxe2tR7ty3Q9fqs12vUyRtsvZl8nV5HPZfhAGXxi2hcoRPzDGfxLks_e-0aVxY2HHEEJDZxpDi3XIVMMNWpGlaV9dq2TSAjPBzrkd8IsM-mKL2TRHaMRPYrKaKQ-LLio4lQKdqml9TJScIXSNEceC_bl8Qk_dBkzyK0GcOCyJm-lBiIAIdsD3ODrXp2O1Eb_aUphN4CFeiaJJ5elhsY_GZfElrcGzvGPrMC3AqV9FwGX-vuXs4NjlpeEaAc3y51X8zypPW9XfoOrsORww8Sw_J43tVVlIe89nB9nkM6D-jFV_71nHhKBpRZQuTcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f0c663da9.mp4?token=babGz-6iAIxqukzJHl458u1RSKgxe2tR7ty3Q9fqs12vUyRtsvZl8nV5HPZfhAGXxi2hcoRPzDGfxLks_e-0aVxY2HHEEJDZxpDi3XIVMMNWpGlaV9dq2TSAjPBzrkd8IsM-mKL2TRHaMRPYrKaKQ-LLio4lQKdqml9TJScIXSNEceC_bl8Qk_dBkzyK0GcOCyJm-lBiIAIdsD3ODrXp2O1Eb_aUphN4CFeiaJJ5elhsY_GZfElrcGzvGPrMC3AqV9FwGX-vuXs4NjlpeEaAc3y51X8zypPW9XfoOrsORww8Sw_J43tVVlIe89nB9nkM6D-jFV_71nHhKBpRZQuTcYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇦🇷
🇨🇻
امکانات سوئیت ۷۵ هزار دلاری ورزشگاه میامی در بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.63K · <a href="https://t.me/Futball180TV/98170" target="_blank">📅 17:00 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98169">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a58ab6c152.mp4?token=CY2oqK7JvW0NSD0LxrK0ySMZO-VDEDNqJ3pILsvJuGprKWGdualW5tn7dHQyYrkC4D-kvOE3jzKfIP7BECL0u_4hPoyesTs1IQhKRHz73LuIHZjO8lb8f2Savn_mhv5yEYDymoC4DujDn0B5X1_DGA0U43iYelAWOvT82ptmbWH-_oxEf6xWoHHgy1x85WzUvHOBg6L0lDA4Nq8SWGovlWCjl32jK4MRDF5GQEyXFxOAL-kn7xPsTg4PXDOSm4kVjEAQVQt47qgXRtqsx5Xz2ujIxMuToMgpsj3ShCm44An4kAEAFmS4LgnfPB5b7LTCtBYb33FKScHZvnX4mAVHQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
گریه های شدید یک خانم تو مراسم تشییع خامنه‌ای :
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 8.25K · <a href="https://t.me/Futball180TV/98169" target="_blank">📅 16:58 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98168">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35a2a62f27.mp4?token=NWgQ3ihfBwIQxQhc0wI_83xGSdTkaF5G20QSASYJ2QbgTKz8PvH2Ghimw0i0q7CmfNHtLc7gqVtFdai48NGRaWJFjQWYRt7PbTo35LrqIDkTaVUvxt8DVIO1HT_V-Np7iBCYekUK4YClOXm29Z_qy4ITt_QGRJv0hqaAhRUt1ZjluLB8KSKSu6aGxw6VJp6h1zRp0vuJKQpX7W55jUzm844cWZSm6hQxNgALvPcComP5IIeoisSTYRlekmYC5OMfhlGNO6GXmCq62RARCYoVHzVH3aDKbP_-s53Dt-FCAyzjYe9Bb9Mro1k73AaDv0OdSjnvWuNBQmNr6bIjlC85hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🇦🇷
برد دیشب آرژانتین احتمالا بخش مهمیش مدیون این سوپر سیو امی‌مارتینز هست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/Futball180TV/98168" target="_blank">📅 16:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98167">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5efd98ee66.mp4?token=SWzTRplsLRgefH5Cwtk6eDNDDpTf7nOC8r1iJbqfj0f_HvuXna37lh7k-TVoOumogq6wk_9zFKmJQ7G31OO_PnPf0EzXAf6PmPlRGuvXZWVRoi-HuyspNqX1qC8TQIwR_-K3MkWHcvp3dpF9zg8DKsE2RuBlel3UMCJlUl00S-j2ELriFYnga94KkgiyMUjM25W9rgHVj4xnEwVwfsXu21i2OQ89lae7pNacvY28fAZ2SkubTkLPpp4enAKWWR_eDWWZJ6v-gh7fAYngtPZcjPcjR1StjklSo7m1I-3I-93NUoqOmjpdocRX1Madc0yXipXKX9jlxn2eYDaVbr3kLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
😆
😆
😆
رفیقای من وقتی دختر میبینن!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/Futball180TV/98167" target="_blank">📅 16:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98166">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/Futball180TV/98166" target="_blank">📅 16:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98165">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی…</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/98165" target="_blank">📅 16:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98164">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🚨
🔴
#فوری‌#اختصاصی_فوتبال‌180
🔴
تا این لحظه و با تصمیم اعضای مدیریتی سرخپوشان، سرمربی آینده باشگاه پرسپولیس به احتمال بسیار زیاد گزینه‌ای داخلی خواهد بود و خبری از سرمربی خارجی برای فصل‌آینده نیست.
🔴
در بین گزینه‌های اصلی همان نفرات همیشگی یعنی یحیی گل‌محمدی و مهدی‌تارتار قرار دارند و چند گزینه عجیب نیز به گوش می‌رسند. از طرفی نیم‌نگاه برخی اعضا به بازگشت وحید هاشمیان نیز می‌باشد هرچند که بنظر با واکنش خوبی از سوی طرفداران پرسپولیس نخواهد بود
❌
در صورتی که با نفرات اصلی ایرانی توافقی صورت نگیرد، گزینه‌خارجی در مراحل بعدی مطرح خواهد شد که به اطلاع شما خواهیم رساند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98164" target="_blank">📅 16:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98163">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b6f4aebb1.mp4?token=ZG5-n2W9tvWNElzQ-9eO_TnubWwH3Ci1aA9gNZ-pjeNRyL4wT29zNyqU0qBzP8kBN-dmdBiYj4NUW4dQJwtr0y__SfVOZ49SPmDYcwgSchT2orRBErLX_2b4ryocWR_LBCy1vaJUAuCSGls4z2s9get4hzMG7moKq17F3YWMXt_jmg5nFi9SgbBL_TqSiqYIhODUkr-wxdVgnz0Eucw67mO83M4YDVCS12GbfZxSDv8EonEqQje_RQxhiRlc4529jwpo06micFXr10FmixZAEYiNFPppUh6iFUNAa5KMuMWYYU5VrN6CJyE8VqZhd7CJx92YuxfhvyEQnCZ6Zji_IUasV5UepTeT294PEpaKVCOXv8awYDX9k7Otr_ZX0fz0Dyl7DGlyUIxnhWbCK82mdrv6V6YCBJVg62n6oKSLtqDBEbxwOYFIP0VtRMDmss42EWZgREOsanuOszBgdgRXpddetrGy16MYXhGKKRJ3_cg_KQqdjCWLLAS8BaEaPk57Waw_6O6cuzvVMZ4PLvHiP9Z6tVNhH8Tb-pE1YjM6_AzA-HRuFVSZpurkv_2CY0TZsrYS8l4mJN0SC_tAaSlqwFtd2Oo4CWLwLPDto4r3xUTgN5S9nwVR6ARFHfyUSz-JRpWYuStskekC06_RUIZgsEt3nu5TSo4yPtl4PEokE3k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
👀
🇦🇷
گل‌سوم آرژانتین به کیپ‌ورد از این زاویه جالب و دیدنی تماشاگران رو ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98163" target="_blank">📅 15:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98162">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/J7fZrcticwdUcoD-5WZJ1wtTzdL2lNowtg5TJqgYibThwdlP1Am4_syUyW_Ub9M02lI7lwBNqMEvjNobW8_fyFHdxkSPHI9SXCQTkDYAGmnK9q0ITyu5E6AIDDi9CImT5xVtLXj1QzY0Z9lFASuncJlVDEeysdHcZ2hlpSeJFO0pgPigPGHmeA6teJ3jCV6RZJTEG6rBOKpFl7nhKbMIneXhZYwel8_DJWcXdlGMtSdtgovkbuaKnz3FnXVpqJ2yU5X-_BtyAgLhdLhZG1i3zaqkyv61VgOdhkPSzF8TZQJd2fFP_Ev7pZPEmMCV5JbjnhZDljT5IGF5a4iKnPR-jg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک فهمیده رو هرکی ببنده میبازه، 1 دلار بسته رو صعود مراکش
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98162" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98161">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/98161" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/98161" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98160">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
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
<div class="tg-footer">👁️ 14K · <a href="https://t.me/Futball180TV/98160" target="_blank">📅 15:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98159">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=og757xYae5irOiAVurlqPsLOzPmUZ7oAMVjQS7sjN3vW1fXh6yKp3OPcDjwlwVfKr8MZaIc_-98TzZsr5qpO1SH5DoBBy3iY2x_T_Qb0KNcfLYLggiNl78TOeElbjeSp_FEAoS1QwhcQvfFFXcHudjS3HWjc7SjmICgQ7QokMC2doHzAF5eK7ECdSUmsu21My9_N5eNIdfsTGFsxDAN5jF2AfxSoX2va41EPDW2YQAuvmYsvMkma3LUER-2UddyNrxXQhGcR4gotfCu7y5ICTeaBagZmSAWTnsZW7Qq6qT6ukEr8nWpruvnn6u4fGNR904vT-9bjessLAK8gBdXeUw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/341bb1b1be.mp4?token=og757xYae5irOiAVurlqPsLOzPmUZ7oAMVjQS7sjN3vW1fXh6yKp3OPcDjwlwVfKr8MZaIc_-98TzZsr5qpO1SH5DoBBy3iY2x_T_Qb0KNcfLYLggiNl78TOeElbjeSp_FEAoS1QwhcQvfFFXcHudjS3HWjc7SjmICgQ7QokMC2doHzAF5eK7ECdSUmsu21My9_N5eNIdfsTGFsxDAN5jF2AfxSoX2va41EPDW2YQAuvmYsvMkma3LUER-2UddyNrxXQhGcR4gotfCu7y5ICTeaBagZmSAWTnsZW7Qq6qT6ukEr8nWpruvnn6u4fGNR904vT-9bjessLAK8gBdXeUw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
عادل فردوسی‌پور: اگه همین روند ادامه داشته باشه، علیرضا فغانی نیمه‌نهایی یا فینال رو سوت میزنه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/Futball180TV/98159" target="_blank">📅 15:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98158">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Zyk8YQn4frQYhnv9unwjDjg6dvb1OLD5JbHFcCR36QF-AF8oBgI3HiVllXouYGom6FX2zDSA4PaHPfhPDxOCodPzJfND-Up1jtvaB02XmRPIU7e8Ut34m0DmrPG0ddHd-lhxtbvyTL4i59ngqTSz8SUSkCglRxoXMQmSStnUmiEi6yFG_XH1OkSAS9rpB5o2ftKbqZix2MznCYEZWmU658Bl2PEuwqkXeZdk-QpA5fbQTjV5wedbM8-qtR2d2ekstHhyiuor3dDmfeo2NzRbpqIEMI27cjoU6Or-p_RLluyjMIgyCSVJuQTC-PsHnqo4ckKAtTJZpeAO3cudEOdO0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🔥
هوادار جذاب تیم‌ملی اسپانیا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/98158" target="_blank">📅 15:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98157">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1aaf3f086.mp4?token=X2MHsm19lqhBLMx5UddXRI8G7fnnr_YAZnFDq-aWY_fXtI64T3ot8BIQCMxGmAh8LDZpjsiF1lcCIPFtz2hYD6BUX0NG8qY2OMCrXbTFYPwFLj3-N_hq7IyhUgxHetkypwHwxJH7N3vEUV70SKWrRlBKn2GO_qwqqkgv7azfGe7VqP77Lel_CU98eCHQpDcavFWEzA_jOnmBEgK93FBg54NAfzgAPAOQJ8I8bgDKhQb4pjYzI6F3075gCvwKtY6HLrnfSV2EgZotIpj5YMdcHEz86Sok78gzpJDdXl8GF8bpCuPPKAZC4Cpy4LGtAD2kgvpOa3T0dup91eWhyx5xyg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فتح‌الله‌زاده اومده برنامه ابوطالب جلوش یه لیوان آب گذاشتن و بقیه ماجرا
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/Futball180TV/98157" target="_blank">📅 15:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98156">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NhVEa3_34w38CZbOCP3o41SYGKIi319cOImbazEy9Opb47J15VXukdA1kSugqJyY6SvgLw4_PdQ8J0S8zUm-xJ3DxVVTngKeLXC8qO1Bl68UorJNCeq57qXRhMv3eG8EXw4eHkvJgVnaXtAZrJzAFUQ9GGr4XpNycFLGBxmqC-wRL3bBLz6KYs3HcYKqWE_x5yldth6-riaxcS6q1QwZF-CtB7--PS8SQy4_sjXE8814olRVPH4xOApR0MO3-Qrn6YRT7nMp63VhTzJ2xdUpfQVA6fg8l9L6qeW41PIRA64DJEGhd5lJaTB4xVtkknyL4bAF5FmT8TPT_5DJO3n9Bw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎙
حمزه عبدالکریم بازیکن مصر در پاسخ به سوالی درباره تحقق رویای دیدار با مسی :
🔹
ما با آرژانتین بازی میکنیم، نه مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/Futball180TV/98156" target="_blank">📅 14:42 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98155">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4a433836c4.mp4?token=nG5YKs9NvQHSYq_7N_wd3ablzTzXTzmzK_W6Bo95m8u6DX9GDzzVraLG4WYjDpECbuJRVfjFoIGmalBoclPUIMgvi8twOO6v_3nRv9ntNlYo9DKnjEkz4tbvqZL1geFcV6yp30RlXEYHwb7YbaP5g33c9UsyfYvHU5qjTnuAHrG-QoHgPYppAtwWfe6kmW-1dXqwOyDI7CwXoLtEQoEKJmTa8NdxtsH9xw5TbSwvC0LJslxvN7yuNF8PlvdEUgSGsOnfqET4IROM60rmmUBvxuh1TED2LIBLefC4-9N9Bzj5WGqRVTr8kQjGkEopv9LiKVx26npRYirUqt1XEIlWOBRBS__npLD6CGS-THrcqbO149PI0wfhe55YaHsr92kAAwrYsBljAbRmHdb_9cYFZqYVw53fAQrnF40J_2KpPHOp0w9wc7ocnX1JAuy0wM8kW69Mie5s6dDgSfZG1qsbfREEtkVljOnqD0WE-rHWE_gPB_kCciyJ6o-W1Mn4Zxs9USBhfcAFSsRk0Oos9dVeK6K72CYwhhiEfV29T5QMShT9r1QCiPBEhrOTFpUJ7lT6Jpc8-E-P1ywlrGbt2399hms8M6ExDIRudNpifMJaEfjOyACtdX7wIV2eMY88CYsCOK1FDriP9qOnMSKAErO5NNnRUfS_KzGi_BziYT2d1A4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👀
💥
دل‌هارو ببریم به سمت بازی Pes2013
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98155" target="_blank">📅 14:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98154">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">💥
▶️
عملکرد لامین‌یامال مقابل اتریش که هرکاری دلش خواست انجام داد بجز گلزنی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/98154" target="_blank">📅 14:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98153">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sYiYtaGz1HTIAe-My3SuJtrxPSTs5D9lIK8hYZ2kAlmoTk74WzoPVY106drqhxiCo-373IotslEVXiLfs7ujzSr40xaaTM0VObAbpgkWR6Qntp25JF3BZ1s1Nz148GJc3HiAfy6jUx-Aqw86UntwWViPgMLBth1oyukCA8JLtID4CyX3zUe5qhrujg-CeZMjGXb64tMVrTRgXYJ_4NzlNULJslU8CY5EJuMsX9b5xyD9V2UeGiS9nD2dO8rjn_AEE6RzP2Ittcybx9WYTkuFbj-F4UhBwLr2eJPJKn1JZmKBGGY9fssCAtsj-VLK0V3cnKjXu-6ZagbnjOaaZonGBg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنانی که تا به امروز بیشترین موقعیت را در جام جهانی خلق کرده اند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/Futball180TV/98153" target="_blank">📅 14:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98152">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XYcYACRMn2AFEA1ByiU_UpaNF1bNz6vADeprpQQTq7dZQkKSKky5TW_N90Q_TfxADL7e-MN_3Mp_NYR0c447UCzwTSFU0uCUIIWVjgG8-S_OsgMrkFJOMA_rYx1b9gguWpp1DOqUek1IYUi7qn8tC7hBGdLku5hRg8DsL7uxV2yLV2wTwGQptQQ9wXMMxe6XM8jTqICHR0gTYFAqIqmthL7JqX9wsO2qzZq-WjTmaTbhDdKufQHKr1IU12OD0Olzd-hfjfivdasS9Nf6xZb3Fi-dZqR-uW9O5McNwX4tK3mPZf3c-PuZUk-rdCiIt3P-O3V5q8K41i_kl9ZZodizOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
تیم منتخب مرحله یک شانزدهم نهایی جام‌جهانی از نگاه سوفا اسکور
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/Futball180TV/98152" target="_blank">📅 14:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98151">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=YYWHEaF9o7U_iBHSXG4NoKNHE8T4-oAnBPWC3hDB4WVg-eu2gHBbGgestzzvf8VnTXxy_AiPaiJPscIdx7HXdj5T4SjxqoIAuRqJmFbIgjvOGhvTsiBs5HHvEY55BibuhBnMZlpD27cXbBtDedS64EcJsSv8GjdT8XOeaxgQb3uj-bNIbnPGgvC4NmlzHLqIrWhFbm-DfVYNhuVi_gca4hVRT7Kf1rvMzyQf16VdFsNDgAhEiC7mCuLdb9HOwpZ3dfa-mBGOq88ROJZ6umMmWdNZadgWVFEaD8KcMXnjAG6Rm1Od2kJIr_3D41ecQoQa7HJU5lObdw0yg_BDyqWkzA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc006f9bf2.mp4?token=YYWHEaF9o7U_iBHSXG4NoKNHE8T4-oAnBPWC3hDB4WVg-eu2gHBbGgestzzvf8VnTXxy_AiPaiJPscIdx7HXdj5T4SjxqoIAuRqJmFbIgjvOGhvTsiBs5HHvEY55BibuhBnMZlpD27cXbBtDedS64EcJsSv8GjdT8XOeaxgQb3uj-bNIbnPGgvC4NmlzHLqIrWhFbm-DfVYNhuVi_gca4hVRT7Kf1rvMzyQf16VdFsNDgAhEiC7mCuLdb9HOwpZ3dfa-mBGOq88ROJZ6umMmWdNZadgWVFEaD8KcMXnjAG6Rm1Od2kJIr_3D41ecQoQa7HJU5lObdw0yg_BDyqWkzA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهرداد صدیقیان از فوتبال دیدن فقط زن و دختر بازیکنارو دنبال میکنه
😂
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98151" target="_blank">📅 14:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98150">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vAnSjvvoUSrd8WrYW0YtnO5iQSSY1EtmPQI29FwpTNIHZYXz118gCw4Vv-qUpN4WZRHF1MYIPf7AjGW_QCrFB5Rlk2LlDrP6OP0gxTCVzRPWwr9aIJy-S1HdsGkGSKUdXKBDYBhDtJLWZn7a3uF91EuS6InnG5hpZrauqy6txzS4o10kU5MxQsrqQJeTYM4EZZcFmAWgzcMaM5Q6eQ5553uHdxaFZ-Xy3EmhsGHlOqpvokY2ZSPok8ejTdphg4tuket1QUIK0l-025IcTfIU3FWwnhS7BNb5bddEMJdkSTVdQ3fu2BUtTldUWxCsIywGRXTUihZ02NI_Q0dB9GV2pQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🎙
جیانی اینفانتینو:
‏"در این جام جهانی، مسی با یک سبک فوق‌العاده و شگفت‌انگیز بازی می‌کند. ما او را به خوبی می‌شناسیم، او یک بازیکن نابغه است و همیشه خوشحال می‌شویم که او و سایر ستارگان را در زمین مسابقه ببینیم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/98150" target="_blank">📅 13:51 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98149">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=Evjjyt3MGVaPCNIwAN3pNSOtJlNVIDk0-pqsgWqZnREOwwnIfO2XwnZtl6FmZTuehKymuQknSEVyW8iqfrPI5PIrrMfT70XL7E1LCq_uMSau6zuzwt9iVsZqbfkql_IRBkPy21HZofHO2VZZdeKILQFrwUzXMbbTZqa70fC-aFssruT9JScuAY4itzcrZ4dMiVFL7Ru9bii6tQnaPrxzUu7_Lnj2b_rV9yBsJhNj6bAJ4FxLcNwqyKQYvYJyLW7tTMWMo_Ry0-qRLWaX2K8Z9vnFvM670apLNAnQPGtd2LDsV5PP-5Qg71fPISspA4kT6ahdbmcyavX5c-VWWQVXbg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/618fa5af23.mp4?token=Evjjyt3MGVaPCNIwAN3pNSOtJlNVIDk0-pqsgWqZnREOwwnIfO2XwnZtl6FmZTuehKymuQknSEVyW8iqfrPI5PIrrMfT70XL7E1LCq_uMSau6zuzwt9iVsZqbfkql_IRBkPy21HZofHO2VZZdeKILQFrwUzXMbbTZqa70fC-aFssruT9JScuAY4itzcrZ4dMiVFL7Ru9bii6tQnaPrxzUu7_Lnj2b_rV9yBsJhNj6bAJ4FxLcNwqyKQYvYJyLW7tTMWMo_Ry0-qRLWaX2K8Z9vnFvM670apLNAnQPGtd2LDsV5PP-5Qg71fPISspA4kT6ahdbmcyavX5c-VWWQVXbg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
🇨🇻
ووزینیا دروازبان کیپ ورد پس از درخشش مجدد برای کشورش مقابل آرژانتین:
"تقابل تک‌به‌تک با هر بازیکنی همیشه سخته، به‌خصوص با بازیکنی مثل مسی که فوق‌العاده خونسرده و قشنگ می‌دونه چطور فضاهای خالی رو پیدا کنه. برای همین مجبور بودم خودم رو آروم نگه دارم و تا آخرین ثانیه ممکن مقاومت کنم؛ خوشبختانه موفق شدم توپش رو مهار کنم.
بازی کردن مقابل مسی یا هر کدوم از بازیکنای آرژانتین همیشه خیلی سخته چون اونا بازیکنای تراز اول جهانی هستن. اما این رو هم دلم می‌خواد بگم که هم‌تیمی‌های من هم لیاقت این رو دارن که توی بزرگ‌ترین و بهترین لیگ‌های دنیا بازی کنن."
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/98149" target="_blank">📅 13:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98148">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=tzNnHWB-GNSJvUWnRlSZJolA1K-1WxZYd3Grj4j9Ty1yjlpqNR_xChv9FPRsyMjH5dYWY2xYM3zQiijGwZKnlf7F8zS89hpN1XaiIRTBpbLRxxxrio-srPBkokP1P2OzB9c8UipjNOEZctbJr4gnflyhupaD0yH1xL-W_04TB7gygx841UyKZqypRmePK9QO3lfudWrA_zNqfPRytbsnezTx4J2qgFHYrhKdMfzzDRnblf-6ZXb1qLPU8sOL5DVlpPft15R1C90J5s9bJkaeobYMnu3jIRhjCm0JN7B9ZR7ADbFQujzpUZ1N-h3sDUbmv43vL42kOijo3sqkFxqqtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0f3e951975.mp4?token=tzNnHWB-GNSJvUWnRlSZJolA1K-1WxZYd3Grj4j9Ty1yjlpqNR_xChv9FPRsyMjH5dYWY2xYM3zQiijGwZKnlf7F8zS89hpN1XaiIRTBpbLRxxxrio-srPBkokP1P2OzB9c8UipjNOEZctbJr4gnflyhupaD0yH1xL-W_04TB7gygx841UyKZqypRmePK9QO3lfudWrA_zNqfPRytbsnezTx4J2qgFHYrhKdMfzzDRnblf-6ZXb1qLPU8sOL5DVlpPft15R1C90J5s9bJkaeobYMnu3jIRhjCm0JN7B9ZR7ADbFQujzpUZ1N-h3sDUbmv43vL42kOijo3sqkFxqqtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
از این نما
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98148" target="_blank">📅 13:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98147">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXDG5dADUC0yJWH2i82zrCBR8-mfSSViSLj-v7I0SnggSHfMXKItoBSgiJYKhjZgVQTC9GdtTN3Y7cdwq0gf6E1VqQ9HuagZYc_6FZTljWY2yfkw7y3st_1NU6YCO5zZcY1iPajdu6hEFgDlNwXkHD7rlJ6in8HvBLEXUv7jbaGcuYiqLGjHjRbODwilgi3z-qkRn89F4qYRzMNxVw5ubrlZIB_PAVYIGkpPgzPpT2yDGQkcROJAEq7wuQGhu0fW4qAWTojRPH7ErRDBjUhjHNA0-gNzkE-ZZbykqli3kPK5IMshLPUava-FQWiX8tXY-Zkjh2MZfpkfa_zFUwyvOQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
متن خبر: خداداد عزیزی دقایقی‌پیش مدعی منتفی شدن حضور اسکوچیچ در پرسپولیس شد
✔️
❗️
🤩
واقعیت در پرسپولیس: جنگ قدرت شدیدا در باشگاه شدت گرفته و چند نفر اصلی بدنبال فرو کردن گزینه‌های خودشون به نیمکت سرخپوشان هستند. صحبت‌های خداداد عزیزی هم با دستور زنوزی رخ…</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98147" target="_blank">📅 13:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98146">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=u3HIHEN9rn9-Os1zkBgwFCSp85YUSmv8yF9dcUClJWSC_WCQxh1yOOPp5SIC6MDiGpj_iQp5NkGoLfK7KisnTB0X-F2UazpFfEqGYU24atf11B-Kpb9cqa9vj5Ik-WvxVM-nxELp-crnol4vMjHqS5DH05NNXwR2XgnQF4Sr77afq_3dBXWrxfa6cHQ1F6mwx2jt3q2F_a2MtBKsaaV_JpipLvomgddp2ltBojZvWcXW5rHmOaRiubG5Ejh3hCQpQQN4LTypjgk_P0ZPrqutKtZ8efeywOlJA68uHlyGHLEglrYXrr1xy_5aEfncalETwpL8sNuSglUTwjU5BfA9YJlidxxilPEO1JhzPnX_Ng0AhMUCXNv4cnsOgBQYhG9x87QqC4gkHOIQ6OM5e6JHqMJFOSqEYzA_-yi3J4KsHITJywM5-LHEy8lp7zzUkon-GV4EG4qqkZijhvvEnqyrQjx_ooYZoLE2aphXbDd58pGjC5X9uwWZY_21l4G7e73fUTl10Bt18UF2b_UXLiqYbPu9V7266z3lGql-od4PJRpnPoSHWoQVhn30MMB65gWSAfXBu2PgK2Z0tPnKhHbadPQYPxhZ0PUuq1fbdCORQP3bD2rewa8I_Z8JA-y-k-9Tik0uxjQNBtEibR3ExgAjV0mFJccapBVgGn_TwXvucKI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f532fa68ef.mp4?token=u3HIHEN9rn9-Os1zkBgwFCSp85YUSmv8yF9dcUClJWSC_WCQxh1yOOPp5SIC6MDiGpj_iQp5NkGoLfK7KisnTB0X-F2UazpFfEqGYU24atf11B-Kpb9cqa9vj5Ik-WvxVM-nxELp-crnol4vMjHqS5DH05NNXwR2XgnQF4Sr77afq_3dBXWrxfa6cHQ1F6mwx2jt3q2F_a2MtBKsaaV_JpipLvomgddp2ltBojZvWcXW5rHmOaRiubG5Ejh3hCQpQQN4LTypjgk_P0ZPrqutKtZ8efeywOlJA68uHlyGHLEglrYXrr1xy_5aEfncalETwpL8sNuSglUTwjU5BfA9YJlidxxilPEO1JhzPnX_Ng0AhMUCXNv4cnsOgBQYhG9x87QqC4gkHOIQ6OM5e6JHqMJFOSqEYzA_-yi3J4KsHITJywM5-LHEy8lp7zzUkon-GV4EG4qqkZijhvvEnqyrQjx_ooYZoLE2aphXbDd58pGjC5X9uwWZY_21l4G7e73fUTl10Bt18UF2b_UXLiqYbPu9V7266z3lGql-od4PJRpnPoSHWoQVhn30MMB65gWSAfXBu2PgK2Z0tPnKhHbadPQYPxhZ0PUuq1fbdCORQP3bD2rewa8I_Z8JA-y-k-9Tik0uxjQNBtEibR3ExgAjV0mFJccapBVgGn_TwXvucKI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇵🇹
فرنوش جعفری گزارشگر دختر ایرانی: رونالدو قبل پنالتی گفت بسم‌الله!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/Futball180TV/98146" target="_blank">📅 13:04 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98145">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pnhAStwVs4OiGZV4maycnsrk31zDhWLhgrt3perzm9t3j-GbxWvCROjdLBhYLSjuliyEuxQETmTN1ObOTcyXiKkNYcnx-rkaI4jpd4wp4NTMQxEJYZdRYodc-aK_Ns7yzoPUdbebnOcnskVEW4r-jf6JSKoBSLmIOycBiL4UXWgC-SXeCUP-ek5GJ_xWnJR_hZdSf-uNHjYjBgHnqi1YtSisJp3pyIUH3IbTnVk_59oklAk4TqWx5gt9kZRJuBzZkrO1vpfFLTtU0xe1mtYpJ-S2QjMtvBUUWZpsmbqwfI71biqbrnzIuLIT2e00GM_4vV6a6RvGNGXbQ_5Cacb4kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
❌
🇫🇷
#
فوووووری
؛ شوامنی بدلیل مشکلات عضلانی در بازی امشب با پاراگوئه غایب خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98145" target="_blank">📅 12:43 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98144">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=cdIerL5jjpJks-1YaI-APNWxxn_EleOgr5c19mo_BEbD-RaN9hG-jjmAMtfuPFXF7AxDRdMjgVQL_J_SJpzIMixw7PALvtbB4rLtC7vXLGMQ1IV7dpIjqnVW_Uz4RfdNibxeTRrSBovbmsmjVl5zf-FAeiyRKwIXVizqduNC_5Wb2NAsBZbCpLD31ZDWEW0sC3-bYUAYAJZ1pRQuThX6PtblTzvRqkHxRxYfDv4tO07czw-K3CXthcIURKZTSSa7zDGt5MyYfVRdk6qZkLQVCbZpPYR7l8xJIdbnYAOp1-z3xo46kr6HVqwKRBP8JmagRfnCSDJx2A_k-eXJxkmsjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1560d3443.mp4?token=cdIerL5jjpJks-1YaI-APNWxxn_EleOgr5c19mo_BEbD-RaN9hG-jjmAMtfuPFXF7AxDRdMjgVQL_J_SJpzIMixw7PALvtbB4rLtC7vXLGMQ1IV7dpIjqnVW_Uz4RfdNibxeTRrSBovbmsmjVl5zf-FAeiyRKwIXVizqduNC_5Wb2NAsBZbCpLD31ZDWEW0sC3-bYUAYAJZ1pRQuThX6PtblTzvRqkHxRxYfDv4tO07czw-K3CXthcIURKZTSSa7zDGt5MyYfVRdk6qZkLQVCbZpPYR7l8xJIdbnYAOp1-z3xo46kr6HVqwKRBP8JmagRfnCSDJx2A_k-eXJxkmsjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
👀
دیس هادی حجازی‌فر به حسین‌میثاقی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98144" target="_blank">📅 12:28 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98143">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pGF4L46dgiWMT7_fQ1DYS_L48yXpIzWnKnuck4QVTVkn7aL3NYyOxJrhcDbAx4TuIPg9uYTvjp-VJULo9wW_fQcfHz82AU5O8jX7rWOCPboB8do4ZT1VnFssFz1DzBprtcOuEGeCsDv4LhxNNgohu8c4TlqGp_AhU7ao2oFCkHXhWm_BwSS2QzCBpG9sfD-qyiAW3xPpewvku4GlIQuLnb1GDc97cGPs17Xa3h6aUqPOWCYPcIOulQczLpAfxUIEpR4mg3HW9dWWRLLiwCx7zL7Tmb0QXtH-LcnDtBGjjn6hdwpyumB1XBQpYk71Vmx2rEQ1FuKz4MQ7_7ypgqbEKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4e644ac1b7.mp4?token=pGF4L46dgiWMT7_fQ1DYS_L48yXpIzWnKnuck4QVTVkn7aL3NYyOxJrhcDbAx4TuIPg9uYTvjp-VJULo9wW_fQcfHz82AU5O8jX7rWOCPboB8do4ZT1VnFssFz1DzBprtcOuEGeCsDv4LhxNNgohu8c4TlqGp_AhU7ao2oFCkHXhWm_BwSS2QzCBpG9sfD-qyiAW3xPpewvku4GlIQuLnb1GDc97cGPs17Xa3h6aUqPOWCYPcIOulQczLpAfxUIEpR4mg3HW9dWWRLLiwCx7zL7Tmb0QXtH-LcnDtBGjjn6hdwpyumB1XBQpYk71Vmx2rEQ1FuKz4MQ7_7ypgqbEKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇲🇽
رییس جمهور مکزیک: از مردم میخوام اگه جلو انگلیس بردیم، زیاد مشروبات الکلی نخورن
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98143" target="_blank">📅 12:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98141">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=LSfJcCvDOsr_Thr31xg4rN-un-uDAwP6pfMuuT1AYELfdZitDc3Nxu_WKAqAYzFDuLh1a6HHRuI856HRi1z36ySPeGjCIrf0qurEWRbAfcU4okhjukAdH2jccVVEzrXfsHe1tg-wQbLzbOn-gFjZklqZsjJbZEKhDWfpgqjU-cCCfMu5k8lZ6bp6Ac2XlN-xPloZ-UVPvo4WagRCRKPnAUMgI7xBcI0GqMEl8ISa9Q_k7T5-hyiWwLY1vyMJe074ntKeEr-C8edcirwB5ten4sthxA5E6njapMOpxppIk6slF0DxjJUiqIAn5Ax-E8vmdhmci3PcQZXu7rxB048KSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/32c0e1238c.mp4?token=LSfJcCvDOsr_Thr31xg4rN-un-uDAwP6pfMuuT1AYELfdZitDc3Nxu_WKAqAYzFDuLh1a6HHRuI856HRi1z36ySPeGjCIrf0qurEWRbAfcU4okhjukAdH2jccVVEzrXfsHe1tg-wQbLzbOn-gFjZklqZsjJbZEKhDWfpgqjU-cCCfMu5k8lZ6bp6Ac2XlN-xPloZ-UVPvo4WagRCRKPnAUMgI7xBcI0GqMEl8ISa9Q_k7T5-hyiWwLY1vyMJe074ntKeEr-C8edcirwB5ten4sthxA5E6njapMOpxppIk6slF0DxjJUiqIAn5Ax-E8vmdhmci3PcQZXu7rxB048KSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
🇵🇹
رونالدو با ارسال ویدیویی به پسر بچه‌ی ونزوئلایی که از زلزله جان سالم بدر برد ولی تمام خانوادش بعلاوه یه پاشو از دست داد، از اون دعوت کرد که یکی از بازیاشو از نزدیک ببینه اون پسر هم توی بیمارستان این کلیپ رو دید.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/98141" target="_blank">📅 12:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98140">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=GuisvYSNGx2CY0_UkhJnI0S95Iv6GKIqxDDlVR6DdwqNaSJwcj0SgQYoGEq5F2V8BQjnUr9M--qZyJWj57QenfCmZ6ExIpYJXPmvUXY901HlRPBdwkJkuDcCt8oRd6BaxtigJUg4GF3CmooLspEWgF5PETQjXFKmWzGzOm1gfi-CHO-tQM9bVMF_rIPbk75MFARHtQzr-o0nH1qVe-1Fd3awu0lXZskwYM1x9CpNq5abOKHEEUTOPFzgkTayYMlP8TvgPy2dSWjBKRFXSAXOlUEVwGUygCyOKaJ9MwLpZoIlxBYf8_bAJQmmQ0zmclRC6ZCM6uG1HBnnmQj6TfEBxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6fe8d2196b.mp4?token=GuisvYSNGx2CY0_UkhJnI0S95Iv6GKIqxDDlVR6DdwqNaSJwcj0SgQYoGEq5F2V8BQjnUr9M--qZyJWj57QenfCmZ6ExIpYJXPmvUXY901HlRPBdwkJkuDcCt8oRd6BaxtigJUg4GF3CmooLspEWgF5PETQjXFKmWzGzOm1gfi-CHO-tQM9bVMF_rIPbk75MFARHtQzr-o0nH1qVe-1Fd3awu0lXZskwYM1x9CpNq5abOKHEEUTOPFzgkTayYMlP8TvgPy2dSWjBKRFXSAXOlUEVwGUygCyOKaJ9MwLpZoIlxBYf8_bAJQmmQ0zmclRC6ZCM6uG1HBnnmQj6TfEBxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
😐
تکرار ادعاهای کسشر فتح الله زاده در گفتگو گو با ابوطالب حسینی: اگر مدیرعامل بودم مسی را می‌آوردم…
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98140" target="_blank">📅 12:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98138">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/keXiKCByxK5qrVKle8ykiVF3HdXxg6lBuSfdjzNAuvq1hlWJZxupXr5mDHQtcTedIWAWNjF8pUcV-q_qst5TWt07ujuyLS9Ylh8Oi0RmOdj1BHCVrnFQytDdA6sY0eFUOKL8W-xcRzXvviZrHTjSXiavn1bDJiigI4AJZ_p5tP4fFccJB7Rx1GYFptLoP74CuUAPHzuZbnHsR2LCkRiee5uS4GGwAQ7jzbT7sOmexZWTPjYsL_AIMkyw1pj_qVzXA5k-YtnMh1-_qoZSpbIrqHtcSB33UPVDmPyIb4Ng1PdX0HPIKKybDWQyCBIeOQmZIf14bJ5oBQzI7P-_rmG-bQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/I_K-FonYuVwyjbUd6jY13-KLz620tRBivw0GxWFxbIXV8eSCiip5Uenm3tlLL2mti9uRbhyWT3rEhu_78nm2R-j-m8-FmLFyaE3ZVV9etsTCfBersgXKRghzUN1A1WwNr18pYhhOr5nGKT_iq1KUmllUIZTVxYfju1PWONAG8nz6YaQkgLBEK3l3iqGv0y843AE8m3_fEb3qzBknDFUr1aQtypqEtBLlr1mx3h1cSnPmbTjv5W0rk2wrX6L4I9XNrX4NtA6wwrBO2VOmOvJ47xaSfrd6kh2BFiIi6-eYghsEnGo3X2eoMqBwhwFq_EJCQWWj4RI7D6_TVRvSRQUDwQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
‼️
🏆
🏴󠁧󠁢󠁥󠁮󠁧󠁿
هتل "انگلیس" در مکزیکو سیتی، به دلیل نگرانی از احتمال ایجاد مزاحمت و اخلال در کار تیم توسط هواداران مکزیکی قبل از بازی، با تدابیر امنیتی شدید و یک "حلقه فولادی" محافظت می‌شود. نیروهای پلیس، واحدهای ضد شورش، موانع ترافیکی و گشت‌های یگان‌های ویژه ارتش در اطراف هتل مستقر شده‌اند.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/Futball180TV/98138" target="_blank">📅 11:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98137">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=WfD0W4oklH5KAOsmJFnl29RDLA6GnZtbXjqQbekadGvUXLrvWNf_bQeURmqibjvHZ84RKPEY2jS1PeJ_c7xE56N_8ZvHH6RNrya4jRO4GM-p8JS5If3KXjP4fJ6EZr1nxgHrETfDW4AifOeZACk6UPnQEKlio1TRhb40MhKlx-0dfAG5RmuQL23Tz8xhA1S7FQlgcpb5YCOn7CO6UImbMn7ZxPfV1r1IMYisoKqFx7HRi2ErACa4MiM08sdYP5bEq_FpH6p85XOg3htZpyRic0C7_1X64N-wxWMrUbIgQmvEmkEbqutYdfl1g8w7CmzGjx0rvxHfxgm7U-g5tbt9tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d7c8cb22e4.mp4?token=WfD0W4oklH5KAOsmJFnl29RDLA6GnZtbXjqQbekadGvUXLrvWNf_bQeURmqibjvHZ84RKPEY2jS1PeJ_c7xE56N_8ZvHH6RNrya4jRO4GM-p8JS5If3KXjP4fJ6EZr1nxgHrETfDW4AifOeZACk6UPnQEKlio1TRhb40MhKlx-0dfAG5RmuQL23Tz8xhA1S7FQlgcpb5YCOn7CO6UImbMn7ZxPfV1r1IMYisoKqFx7HRi2ErACa4MiM08sdYP5bEq_FpH6p85XOg3htZpyRic0C7_1X64N-wxWMrUbIgQmvEmkEbqutYdfl1g8w7CmzGjx0rvxHfxgm7U-g5tbt9tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
😎
بهترین گل‌ فعلی جام‌جهانی از این زاویه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98137" target="_blank">📅 11:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98136">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=B9b5YRHHyBT0YrOC1Dhq0T4BYYRso-72LdDorNseVqxjEvuEhbL48DUxE7qill8EXYCE0X3FEO-h_1Hey9c2oLjNwVNfGpoAMEFtod51lw_W4AkHE-fmNwU2Xylq52Lx33FM9DiDNw5gb6oTtBTCXvcaX8Jf8ks36o5rlTq27LK6aH8ZPfL8sGfs-dee0hZ7Tp6pNJwt6EJyML-DAsoe2_9HOlYGKHlZwp-jWCsfsIcOu4HJXj46mLhzvcbSSxlca64F7ahe0pKsSZiZ6lfqCrH9O95ASlzm4zXw5oy0tx24_53LYsmrMlRMmkvChcW3AvSG_GncqqwQFILRs9W4ww" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/384560aaa9.mp4?token=B9b5YRHHyBT0YrOC1Dhq0T4BYYRso-72LdDorNseVqxjEvuEhbL48DUxE7qill8EXYCE0X3FEO-h_1Hey9c2oLjNwVNfGpoAMEFtod51lw_W4AkHE-fmNwU2Xylq52Lx33FM9DiDNw5gb6oTtBTCXvcaX8Jf8ks36o5rlTq27LK6aH8ZPfL8sGfs-dee0hZ7Tp6pNJwt6EJyML-DAsoe2_9HOlYGKHlZwp-jWCsfsIcOu4HJXj46mLhzvcbSSxlca64F7ahe0pKsSZiZ6lfqCrH9O95ASlzm4zXw5oy0tx24_53LYsmrMlRMmkvChcW3AvSG_GncqqwQFILRs9W4ww" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کیپ ورد سرانجام تسلیم شد.
💔
آرژانتین به یک هشتم نهایی رسید.
🔥
🇦🇷
😎
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/Futball180TV/98136" target="_blank">📅 11:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98135">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=gbJIRXKLWSX6LWq5VngXiiGKe3dhZXSi6RAxMPEK7Fw5MjZJYJdoF5zFkFIL9wty8fg4njVp8jA7nMGjhnG_6D7Ql2ElqfwNh6DQsykyMANqAmi-OPfblq07q-eEEFKLqwQ9axVVrePF5XYclFAUB9K4ObDKA_e7EkQDfX3LmWEF5fKrTq1cqude-I0a_J3eBtihQlMSESWVxWJ9rko0_CyxOwGcKDE7zqysIyU4pjvP4WWKKLcwpnDwgZCSPaVLbiBLwuE0NVFgngLmtjHF3Of4JgpuJc2l-MD1iSFOlOvI990H7JzPyUWltfZfAZ0qMMvo-VsABKEmJ2LIOrL8Hw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/34ed4cf233.mp4?token=gbJIRXKLWSX6LWq5VngXiiGKe3dhZXSi6RAxMPEK7Fw5MjZJYJdoF5zFkFIL9wty8fg4njVp8jA7nMGjhnG_6D7Ql2ElqfwNh6DQsykyMANqAmi-OPfblq07q-eEEFKLqwQ9axVVrePF5XYclFAUB9K4ObDKA_e7EkQDfX3LmWEF5fKrTq1cqude-I0a_J3eBtihQlMSESWVxWJ9rko0_CyxOwGcKDE7zqysIyU4pjvP4WWKKLcwpnDwgZCSPaVLbiBLwuE0NVFgngLmtjHF3Of4JgpuJc2l-MD1iSFOlOvI990H7JzPyUWltfZfAZ0qMMvo-VsABKEmJ2LIOrL8Hw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇦🇷
🇨🇻
خلاصه‌بازی دیشب آرژانتین و کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98135" target="_blank">📅 10:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98134">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=dsyKvDuzSO8rUCEAgx0dWxhmWYVgTHbjnLV4xVbsozg_7mZkUypSeo17dxCb7ak6SRTqNZIWWH3dxAVStY122LZ-igv7bTBZkx5TQ4ELqbQ7u1TDWFQZpxVKNf9NSB7n02gorPAyjtqfRVpLOr3HKnceadg7v5P8CmAMOzR1kz4osbptIDh5lrgWkEbTez4x-lB6GMS6aH6cZSVQEX1df67_IrUnDNOsmapTxJxrukVsfGm-OsX6pxIzmE0KsuRyGqZOe7vAslrY7r-1nZkXuL9fcpbMljvisA2jhnk0N0X_nWty5jmrXu8w8wFniz7rhD09vV8-JAcCaZLzsiYtwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257254cbc6.mp4?token=dsyKvDuzSO8rUCEAgx0dWxhmWYVgTHbjnLV4xVbsozg_7mZkUypSeo17dxCb7ak6SRTqNZIWWH3dxAVStY122LZ-igv7bTBZkx5TQ4ELqbQ7u1TDWFQZpxVKNf9NSB7n02gorPAyjtqfRVpLOr3HKnceadg7v5P8CmAMOzR1kz4osbptIDh5lrgWkEbTez4x-lB6GMS6aH6cZSVQEX1df67_IrUnDNOsmapTxJxrukVsfGm-OsX6pxIzmE0KsuRyGqZOe7vAslrY7r-1nZkXuL9fcpbMljvisA2jhnk0N0X_nWty5jmrXu8w8wFniz7rhD09vV8-JAcCaZLzsiYtwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👍
جدی‌جدی ۲۰ سال از این قاب خاطره‌انگیز گذشت
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/98134" target="_blank">📅 10:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98133">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=GmSJHFJWg9Owgbxul-hD7wyk3O2xibskaNT-Q27ReCRf4rnXcTESsTajtqI5PKw7zmfD90_2X1iCOgPMmiLz1lxjGqcJCsYFC7z0Avv4OHYiyJfmQ4nw04sqnnKiBPZxiOJCqOqkUY8BsKqPe_Ud2gCYfYeuvA9Td3asuUQOIO8_tkX5jgj13pq4eY_20bOXpDo99Bc4cxN8rHJ2mLiylNQtA5jkGO5-DkkbTP8Zkja_CJ99BnuVRDuvnxLd1-H09Wq4O_NH9erOKWrTBiTpzGBxhYtoUGrUOkqAhy2OA-6R-m2fGslEBUIWuKBvptS7M2umZ9kG8grBwFnLdsTnsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/be274a4b56.mp4?token=GmSJHFJWg9Owgbxul-hD7wyk3O2xibskaNT-Q27ReCRf4rnXcTESsTajtqI5PKw7zmfD90_2X1iCOgPMmiLz1lxjGqcJCsYFC7z0Avv4OHYiyJfmQ4nw04sqnnKiBPZxiOJCqOqkUY8BsKqPe_Ud2gCYfYeuvA9Td3asuUQOIO8_tkX5jgj13pq4eY_20bOXpDo99Bc4cxN8rHJ2mLiylNQtA5jkGO5-DkkbTP8Zkja_CJ99BnuVRDuvnxLd1-H09Wq4O_NH9erOKWrTBiTpzGBxhYtoUGrUOkqAhy2OA-6R-m2fGslEBUIWuKBvptS7M2umZ9kG8grBwFnLdsTnsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو مکزیک یه زن و شوهر دعواشون شده بعد بازی که اینجوری مرد بیچاره افتاده خایه‌مالی
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/98133" target="_blank">📅 10:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98132">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=N5YmfxFmv_4O0NSyAaei3q7GFvqoa0tnma0KBPzfxnJ1L9mLBVfWZS6CJyOKFhVMwPaU2-r3KoSz9KFbusX95In1fJOY59wCDVrpDQ2f63azyYohMuEl6y_tW2PXCAXRHJvrhRWWCG2Qh3p5I4hHVIRVB88F9isP1PM1R1dRkLgy_BtGR74cYi6zKKdCw25JivJA8veWEkLJ4N-l8bAeRXJq0i5NuKm2mdZPlkXneg58OGz4HcXlFo91uBmnc1MqTR_edMP6RDW4lZkx5FOgSEpr-7mAIZ4LPHVYyhffPGsphhX0k_PcFunDt_HTBNmXGCFaOKXKIO5idhQ34eUmuw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c85478b9cc.mp4?token=N5YmfxFmv_4O0NSyAaei3q7GFvqoa0tnma0KBPzfxnJ1L9mLBVfWZS6CJyOKFhVMwPaU2-r3KoSz9KFbusX95In1fJOY59wCDVrpDQ2f63azyYohMuEl6y_tW2PXCAXRHJvrhRWWCG2Qh3p5I4hHVIRVB88F9isP1PM1R1dRkLgy_BtGR74cYi6zKKdCw25JivJA8veWEkLJ4N-l8bAeRXJq0i5NuKm2mdZPlkXneg58OGz4HcXlFo91uBmnc1MqTR_edMP6RDW4lZkx5FOgSEpr-7mAIZ4LPHVYyhffPGsphhX0k_PcFunDt_HTBNmXGCFaOKXKIO5idhQ34eUmuw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🏆
ورژن فارسی آهنگ جام‌جهانی
😁
😁
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/Futball180TV/98132" target="_blank">📅 09:40 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98131">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=cKMt_PWiUQZOrqNAVE95-VNa4OHOtXnkNhyHLtItzJBPS4SV0nT5Zmmqf7TJ1c2T3ucaPp5Lt1_VtwakKz0JWx-963cxTbtrpJFO18dsprLClVVGH-QEy5KrrSmyyvwbJEUmDUdD4Uq4RUtvbg6jeLi1gJR2NSi8flbO4FRjpUSou92_allASydbrBjPX63u2rQEB3jB8EXYuBD-eOllggWlF-vYBXFFZ6v2lHKMZVul6qcl0p_HRuSr2Mo_oqG3PP4H3s5Q6H0ltB20-GVmggU8PS81Qot2ZF86lqLCXLwFUSrFLiozGs9Pv04ezIxCmPNvOduyGlQvZHKkFpZpHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cbf09c69ac.mp4?token=cKMt_PWiUQZOrqNAVE95-VNa4OHOtXnkNhyHLtItzJBPS4SV0nT5Zmmqf7TJ1c2T3ucaPp5Lt1_VtwakKz0JWx-963cxTbtrpJFO18dsprLClVVGH-QEy5KrrSmyyvwbJEUmDUdD4Uq4RUtvbg6jeLi1gJR2NSi8flbO4FRjpUSou92_allASydbrBjPX63u2rQEB3jB8EXYuBD-eOllggWlF-vYBXFFZ6v2lHKMZVul6qcl0p_HRuSr2Mo_oqG3PP4H3s5Q6H0ltB20-GVmggU8PS81Qot2ZF86lqLCXLwFUSrFLiozGs9Pv04ezIxCmPNvOduyGlQvZHKkFpZpHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😆
خلاصه بازی بعدی فرانسه و پاراگوئه:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98131" target="_blank">📅 09:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98130">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3536115386.mp4?token=hoLa95NOJRJt57NUSdmRQgNFdj_Xl6GNvp9qW17eTbJlOcdQCp1lTl-AKmPq8Tgtk1vzA6XzjQ9wMJYyZJ6tPhyhXaEaJZ12QTZ-Vhu5kHHBh0X7cifhF-2fxzU78d4SkLUXpxA0g_OltFnQaD8THByfnBt4XfKqQU2GDwtqiI1CG2PEhTsoUxyHIboF-QbbWnkp2PiWUR8wPtEta-LUeQ8xL_hPkNH5sOI09vjsPjA1HvxOr0MEiIg8JBih2r6rt4mCchDzwHJoNE8tv6Rqds78a9fUDCZUBy8g3QUiQhKIoYdSdhGfBS2np7BQE7Z83rbKBUS8YpyQvfSnEtgZCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3536115386.mp4?token=hoLa95NOJRJt57NUSdmRQgNFdj_Xl6GNvp9qW17eTbJlOcdQCp1lTl-AKmPq8Tgtk1vzA6XzjQ9wMJYyZJ6tPhyhXaEaJZ12QTZ-Vhu5kHHBh0X7cifhF-2fxzU78d4SkLUXpxA0g_OltFnQaD8THByfnBt4XfKqQU2GDwtqiI1CG2PEhTsoUxyHIboF-QbbWnkp2PiWUR8wPtEta-LUeQ8xL_hPkNH5sOI09vjsPjA1HvxOr0MEiIg8JBih2r6rt4mCchDzwHJoNE8tv6Rqds78a9fUDCZUBy8g3QUiQhKIoYdSdhGfBS2np7BQE7Z83rbKBUS8YpyQvfSnEtgZCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🙂
اگه کیلیان امباپه در یک کشور دیگه به دنیا بیاد:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/Futball180TV/98130" target="_blank">📅 09:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98129">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WXtwgLKf0bR3uxyj48I9G9ZCdhs02BUKKQLFw8wpinMflQ53xAVsI0viyxvShUaY3XHYHWG5L7oeaSPdaxghNI8ar2lHhV11oBklGZ0BvubsBFcTTiDJ65wfwGwR5BcjoEs_8S_3Ku_Fiav0xHLmUIVK5r9nDumv8SXXCTDMhNQhlcWYtRf4yAKHMFO4nWq2vpoBhd8GOl-1-S-BWGlkDqzs1zDFdA-aS0Spuoj0BnM8wJ2H4rP3ZzSc3niQsAP8lxrv9oqMHSQLZAG_9_-t0Ki5xekD_oC5lbn7iwtnh6DEYPKP7EpeSHYwuextEQTW_C7PpWOL24mJTAdvlBszyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🤣
ولی چه کیری خورد این بشر؛ تو چند ساعت هم تیم ملی کشورش از جام‌جهانی حذف شد هم جادو جنبلاش اشتباه در اومد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98129" target="_blank">📅 08:21 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98127">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qeKjbdKiPdjEKW3BXL9ZNZJZ_acxvSRcfgSaACqog_uc_lAQLAspbf5CrTiLcFvlPePr76I-_yiHNsnzYp7peU04J2lzZUMSIgDyC9CJWU9wK9eeOM2pjh9eC1iE3z05C383iBajYHAAI7NgC2m8g_vUumipO-A16yyHs2jh_he1rX21kXHcDTDBMrQeyEpjiW-_2-MkO1wfY78GUwo2fByEadMF4WL5304M1FV3CcgL6PL7sXnuQ9AsBNaorUAzfixNgUR4vsocLRw7ahe0_H2-oFWrmP0DWR2sbNtUCYMPHQfl0GtZ6c-Mbxu76yykm77yNuhep8ZXz8i5MGQaUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
برنامه مسابقات ⅛نهایی جام‌جهانی
🇨🇦
کانادا
🆚
مراکش
🇲🇦
🗓
شنبه ۱۳ تیر ساعت 20:30
🇫🇷
فرانسه
🆚
پاراگوئه
🇵🇾
🗓
يکشنبه
۱۴ تیر ساعت
00:30
🇳🇴
نروژ
🆚
برزیل
🇧🇷
🗓
يکشنبه
۱۴ تیر ساعت 23
:30
🏴󠁧󠁢󠁥󠁮󠁧󠁿
انگلیس
🆚
مکزیک
🇲🇽
🗓
دوشنبه
۱۵ تیر ساعت
03:30 بامداد
🇵🇹
پرتغال
🆚
اسپانیا
🇪🇸
🗓
دوشنبه 15 تیر ساعت 22
:30
🇧🇪
بلژیک
🆚
آمریکا
🇺🇸
🗓
سه‌شنبه 16 تیر ساعت 03:30
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19
:30
🇨🇴
کلمبیا
🆚
سوئیس
🇨🇭
🗓
سه‌شنبه 16 تیر ساعت 23:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/Futball180TV/98127" target="_blank">📅 07:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98126">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uUpPqx-8FFpRHvfQPN3iZZcssZY81ei_-h7zhk54fj08B_F2fNH-cF7crN8b4sqck2KT9xUWsnzKqStGjMRQCSIN509YmGod8MpeViIAH671aeCEfEO9dvnn5vqfjfxAR2QvIwGFgykeXkmD64NzTqTs-mAkHks7tLYZsRz-bAcV9KveBdgGxjkmCt4idaZNBIlZId6eZp5oyw0zsvb_HiaMfA7FzOn7CGav5f7BI7f98zi9Z08br3Kp-0c1AkWs2hfSTI0-VV2TeMlVrDBI3TwCkZiflLCe9CW7JGiRbGV01VhTEq1TwReME1_AaakM-SmT3HJwrnwGReSXOoLZOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/Futball180TV/98126" target="_blank">📅 06:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98125">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">کیروش کون سفید پشت هم داره از کون میاره</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/Futball180TV/98125" target="_blank">📅 06:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98124">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">آفساید
❌</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/Futball180TV/98124" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98123">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">کلمبیا دومییییییییی</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98123" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98122">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">گلگلگلگلگلگل</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/Futball180TV/98122" target="_blank">📅 06:20 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98121">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDPA0PXkllNvSgdW0fyuYBNb9DCpVohcyNYGHzCV9i4dHxrGcGUVx_II3w_A9hTh8u940fQ6WKyMXbN3WGG74gKknC8ezv2RlU19-whAXpvQcGjSPHQi-arfQkQ6rY6OLI3nMI401YRxz20lFRAXlYXRvQW5PJ63IPdRPPBg2G1DKoHbtQooHXQoEFHxl9rUzhDkUSOJ4Ah37Q7-R9IEGhOtJFh_T49ga9GL2ouW1h7GA9rNyj0N3xwxLDhreAGmgiNuibIzvoTk1sycpRUJuLZX7_D8vdPJ1zvHUVbrCyBJD4MGjZ6c_X5Yd0a_uxY9Y_k0qPFlQr2BN6qJC7QFrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📊
آمار دریبل‌های موفق این بزرگوار: 2 از 2
🔹
نیمار: 0 دریبل موفق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/Futball180TV/98121" target="_blank">📅 06:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98120">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/djfXPEZNV7rC-cGnECHs4rzewtlAzaBbUScfbfqef0SDWRyhJmgtS016fz80jYW1bGu9o-aHHWniLiCD801ruXtVKSwhKtCrn3QAcplkBHx-HAEUjtQUQfY2rZQKoUEmYexJtZWqDUW8dRYFzQHXGXA1evhu86WgEbEhLWSwIFkaItJM3oZdb2IdyYDPJ6Px_jc2_e3EjpBCEJHQxZGhGYpX6fONCQ7XF8sFPcLKqjrG-KCS6i8Z093E-h4di9NMAOgD6i9lnbYVV3mn_57GzCHKYVUobu7y1KZ3EBhjBCcOErgWH33jJPtJtjznpUAxVFkLqII8G7JNenvrv9dVNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
خامس مصدوم شد و بین دو نیمه تعویض شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98120" target="_blank">📅 06:13 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98119">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیمه دوم شروع شد</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/Futball180TV/98119" target="_blank">📅 06:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98118">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/98118" target="_blank">📅 05:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98117">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k8Xp8_eIqU6Ez9TqHDo5lV9pVNYdGixDCaG8-ZnhTfwYYFxDipxUizpuKPD_DlXnBZpxWpC72qpjbb-JV8Tds39yTIcWdA8auvGOn5gfz9VGyoPrw7WpCliwKMESosJTIRf7PyzhOD95rk46A3ji3RTwdYuXQeriS6YREROg0lRN4g42wI0Rtdri5JirhV5j908nTxzl18NK_PwQ2BzbGzreUWV2Mm-aRCYAciIbWXutKLRcmFn5aEGUlywd5i-heS0ZJBEkqqWCBIncLOo5TXBobSbpL4K2mawk0EBFTWvdIISstuOxnSUaK5MmSN5hGNFPTJiCD15w1IF_8johPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدترین بازیکن آرژانتین در جام جهانی خولیان آلوارز هستش که در کنار مرحوم لائوتارو مارتینز رسما آرژانتین رو بدون نوکِ قدر کردن.
این درحالیه که مهاجم نوک اکثر تیم‌های مدعی مثل انگلیس، فرانسه و پرتغال نقطه قوتششون هستش
‼️
‼️
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.6K · <a href="https://t.me/Futball180TV/98117" target="_blank">📅 05:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98116">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/tnfb4KDI_s3jCuGtx2qYwIM452c4VKB0nM3pG5PTU_0AWzo_gGjI2jE8-A5axVz6j_T0QKpE8CrEN8lVJruqC0otDl4up8jqR-uAeyqAuqg7Azjv9JjyAX4DX8jJxdMBlhPo39eTDHeIJ46PLGfakRE6i0b7WCsr_skoP9MEdgodWnLrDR7Kwr5v4BENpbq7ia7Cuu3LHgXd5oP_mpLkIVdwq2PTjs9dvpygzZUor5UTYdrCrBPajiI2llIV-5bjk7MCBV5AnDmX_iQ9dUFuWt1569r7DtWF0CioT1nciGYz91nwXJgPML4Xqsk0NRIQRI15aIi-_v9g2pd_UEqJ0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آنتونلا هم اومده بود ورزشگاه که شوهرشو تشویق کنه
🥰
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/98116" target="_blank">📅 05:46 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98115">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/16e1357ef6.mp4?token=rRAa88fFljloSYpwZSJHfE9BImcWqd6bLVT3aCoE6nnY-buv-OYYW_iwsBCpFeGvDXjgwvRqHEQx1Qe9YVamGWQh-2-WvOmbGIlf0Xf2ISCZ-WfN45JxNNZhPvqZF7J5cV2oqq2QzFEqzwsYU7XjfHT94fbG82Sc2MsLA5Z1hp3_TItyqPoUmYj_0JNzh5zxpeAGx2g0dsIUx_g0d2Zn6_EzjHOqYxGySUKBnYhLzLk0SRVYa_vtbvrTWgz-po7viXLKCZQQl6i6em99fu1KuMv_Nyzyrbq5btzFKmv-SqPEgoZX0RNZRrHTGfiCtIzpwj3PpMzbrBF03tkTbITwUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇨🇴
گلللل اول کلمبیا به غنا
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/Futball180TV/98115" target="_blank">📅 05:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98114">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">کلمبیا اولیو فرو کردددددددد</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/98114" target="_blank">📅 05:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98113">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">شروع بازی کلمبیا - غنا
🔥</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/Futball180TV/98113" target="_blank">📅 05:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98112">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YsdwKZwid9UAKF4THbvKsgbmbmMjb1q3k1j2Lxt58qwWPaQEmtJwm91UrnpNqLKBOQ11G24gKkPjcNjIcHj23NXcNZouV0biFAzvwaHsheM9x25-tvekDaixYSd8NQcY2m-S681JCylp2cSK67ikCAOr0Qqnl3h7WQuGyD2j6uL7Oi4Gvs-FubKmayT41CTupKK3hnQxmmTBMVPaJFX3DUyoCwaCjW37dX08o-kuRRJ52fUCawGNCuFfTfE9oe4FXqY6qpfZ_oS5z416t4C9uHjAJUh2CrFd41TdkopB_fksr_IyqkNNWJI4gFxaypmMiANuD3aYwfrdAhDN6G2HyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🔥
🏆
لیونل مسی، اسطوره فوتبال، اولین بازیکنی است که در تاریخ جام جهانی، مقابل 14 کشور مختلف گلزنی کرده است.
‏ـــــ کیپ ورد
🇨🇻
‏ـــــ اردن
🇯🇴
‏ـــــ اتریش
🇦🇹
‏ـــــ الجزایر
🇩🇿
‏ـــــ فرانسه
🇫🇷
‏ـــــ کرواسی
🇭🇷
‏ـــــ هلند
🇳🇱
‏ـــــ استرالیا
🇦🇺
‏ـــــ مکزیک
🇲🇽
‏ـــــ عربستان سعودی
🇸🇦
‏ـــــ نیجریه
🇳🇬
‏ـــــ ایران
🇮🇷
‏ـــــ بوسنی و هرزگوین
🇧🇦
‏ـــــ صربستان
🇷🇸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/Futball180TV/98112" target="_blank">📅 04:50 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98111">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WOrl_CP3s9DOscrupUbELT1hSaR6f8HP_5su5M2_vxilrm_Evgm1TxjEh8YJIRB3HEWb2oplmdU_Pq3pNiTsuKTzQjsI-v5eOTAMbsMVYIGAfjCS5asNClBNDzQJkwnAUOiFaCxomtvqLbWCYwrbLLHcFpQiALPLqRH0RQxcynSzkn28zWma2YnpUZCwm1T1qdqe1x_p_1Z3i9wmBMQiT7LY9sHdiiO9hKmw48D0_Pdh5-qq_qa8Yn61p3ExM63DNA2pNxspeRV9dUjqUUI-pC107VjBRl3cMZgaD-oeysaBGiwOijU6ybdI8Nrnr3dUNP1LrQqloopcrDiCxTawDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📱
مسی همین الان گل زد. فکر نمی‌کنم تو بتونی کفش طلایی رو ببری، رفیق.
هالند پاسخ داد: "درسته"
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/98111" target="_blank">📅 04:45 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98110">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iBrWkqfz37EFI5FhWvghwb5ovQKWE_jg-M5NJvnGkDctqJ4hu8gFZwY3EQngIX-f4VRHHtQuuoOvHToHzpWN07xYFHDwtl2i1ROxXgt5vzXrt3djKeY_JRnMl-H2_bRGaLZrCedHyZfUn-BwuJNwwJMzLH2r66k6TkZrB1LfC2khWtB-B717t4RGfwRFn-S8_sf2-eMhIwqCfqxa8CgyJqc3tXZ0FXh84MloGRnTfzwpAlAL-3yt3awuOH1bxpSZpXZdif5h1BVAgCnx7GBvCHWVZ1H7Kq0X2kMoWG7acH_1m_AbXi4IY-huh2ee1FywDc8NPgjNGDN0WZYhgIWnqA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
🚨
🚨
🚨
🇦🇷
🇨🇻
🎙
لیونل مسی:  ‏ ما دیدیم که تیم کیپ ورد در برابر اسپانیا و اروگوئه چه عملکردی داشت.  ‏می‌دانستیم که این مسابقه سخت خواهد بود، هیچ حریفی در مراحل حذفی آسان نیست.  ‏گاهی اوقات مردم ارزش بعضی از تیم‌ها را دست‌کم می‌گیرند، اما ما مطمئن بودیم که این مسابقه…</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/98110" target="_blank">📅 04:41 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98109">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KgKQWoeA2lHs5F_5_Au0izl21_V1VELg4iV0mg5NDhCto_hGvrY2g7sp1387KZhBwHGjn4wi8cjWeP8qupG-f4DsP7SmfDgozoKmc7X_rxImBdF8p593NFaVTkXPdmfDjuv5pCRZaufe-ZP89yHjSllJQdoB9KfKEsRh23j5XatYiOy6rUFQVTX061Ej87hudv2Fa9p8emDlwFH5w56uH1v7lkH1bDSnaJgu5K10up8B1VWdLWhCrv2_JoCRAHYRWTCUBLAQNGRhJOaoJiz3dCP_HCWa4LWg3v1ruyUC_1J1BrgzF6bfRUKoJyAW4uzLZ0p9Vvfljkgph_-upicX0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
لیونل‌مسی برای چهاردهمین بار جایزه بهترین بازیکن زمین جام‌جهانی را کسب کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98109" target="_blank">📅 04:39 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98108">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gcFxPm1eEvC3fDDDIujXM-JgGSVQrvcM4zckNfSCoSKpx6IRqUxFA4hPucqnL95y7gSnd5HrQpgovYDxRGKvUn4HG6wrwirdSIf6Pzv8AgyNr657mcdnyAcWNpeyz4t4qvpvuiR_5xtBq0vUjG0_12H7jNRwt3zNX5qPo_7DxB6FvyKf8nwzDwTl7sMTvtyIR-y63bKY5INV_HC-ip7-TYWbtN_Z43Lx2S0S2P1MnF9USOlUwIXQMV_9pyaP_MkRM2-7d025ZAS2BrHxfYzrt5nLgDdUG1iCJ8HmOKabk7CHezExnu9dINhjwQQlkDD9pNkTf1t1FzgS15PYTiEruw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
مرحله‌ ⅛نهایی جام‌جهانی فوتبال:
🇦🇷
آرژانتین
🆚
مصر
🇪🇬
🗓
سه‌شنبه 16 تیر ساعت 19:30
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98108" target="_blank">📅 04:37 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98107">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2lif8eOR1kMYa6KJqf9JxyRo-umu0pU_mb39Xds0g2PsjHXKK2817zglX3mCl-ikIOU6kZiYypJsZpmy5d99Rls36qR2D5BpY1y7NZhRclZTLVRnS-UQvM8pDm1NboN-EkMDU6_AXad8meI2vOuHMk1OjCcr1E8NewH7kTL9kRFTBiZVxJBmHEO9KGTXonzqtmGBSIyBwUZ651_qFjk0OJ9BLTi-yUI22U_CBetwvU1zv0uqTisIpOHO8kYisS2wnWJOOAFUljy-2-YpjfLUDxPvKIfHeaG3lPXC2Z77bneZdxbgdusw2yJZofzkt2X3zRKUMclGugRIEWLAVRT9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاتوووووووووووو
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/98107" target="_blank">📅 04:35 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98106">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i5gHif5jucSywubDgZ_P4APemxroDEmD9_QUYVuiYfx_ftiVUcyBjwOsszFuV8UtiodK8gcttRQcD0a6ME7rxwr2u6qjn8EE2Gk6SIz4Y0EiEsjXOmDZXQDxFA17aIKxNs763Zm4X4nKTpIIr7Gdb2PHB1_vMdm2WJblmaU5smhxh3MV2OdJzrDFFci17m6vFKlhrXnqouFk_f8ghOhenFiEy1l6l0vV9mqscwzrzuW9UGLBdeF6gkthO30DR_od9oX9P0QQWYutN24pz2i6pS44eAS1q4c9q75UgKe9c-t1BqSSk49Ne9L0oSffQVqJQos2p5wEbB97hGfopVIopA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شاهکار خلقت در ۳۹ سالگی
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/98106" target="_blank">📅 04:33 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98105">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🚨
🚨
🚨
🎙
🇦🇷
🇨🇻
لیونل اسکالونی:
«می‌خواهم به حریف خود تبریک بگویم، آن‌ها امروز ثابت کردند که یک تیم بزرگ هستند. وقتی می‌گوییم که در جام جهانی بازی‌های آسانی وجود ندارد، این واقعیت دارد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98105" target="_blank">📅 04:31 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98104">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nlpkVf0iD65BUVUZp_5pgHVjt4eykQtVM60ssSYuL-cHMF2yXSezfdWMFJ_B5zESMwZWwOJFmbmCy6CubR0iWTa-2aeRKO95U0fHBuTypJbRCh89xTf_xf8O1lCxX6JdnC8P08dkQsV85WGM7kDXNQH0FfHJS4uY9Alk5VFjqAqsd8CAe4TqTlpscwpP7-lh9_QhL2YIHj0UMiwMuHF-OqEyp8rrbBbnWBJHCyBnjiPLxWz8BLgObA9M4UyGbkJPy1d74afqlIP3pptZPPHMQz0RKGu1AMpSUMRtB69vIdzmy8hYG-A9wiwN_-Fn5j4wz-gZb9Zphr7KdQcEArcUFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/98104" target="_blank">📅 04:30 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98103">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/L2IlzQj0XOJkf0r8P-QbhjTO37vOr2zI_tMSQ7UNiXlGurA2Kx9QxhZdVhdGE9bH3hVxxax72DblFp74BAi_51TprAKBpD4S1FTtszH0svvwqtvTKLSnRaaN4aDm9U7MClqeQ54Ju1k9YFokM_e9Q1lvrUz9wSbaP_ciLdhOE9qE0yYEpVi_jOkhR2R2arH8QO5g6PD0KKNssGz-EKnEn4gngvhpGHnxBb0vVTTUTWxs5QhlMFhX2j5RG4xep8f00Ar-jkoo_Gxoi4sTbXkySTmjnzIDEwlH9Dlym4SRNsdq5KlxI6Cd7JNFLFrZIHe1zN5HmPlqYLrAPoI3H36tDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
📊
🇦🇷
#فکت
؛ آرژانتین (از جمله در ضربات پنالتی) در ۱۰ از ۱۲ مسابقه‌ای که در جام جهانی به وقت‌های اضافه کشیده شد، پیروز شد (۴ برد مستقیم و ۶ برد در ضربات پنالتی).
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98103" target="_blank">📅 04:29 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98102">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WgyGQr85ybVXgTQq1ddO0F0I2ESKjWbK4lam7RFqWotwcqGkYoNC5XV4l66xK3tGRNk6oBijvJSSsV6dLUtPuWnkADOneo5kYr3JtzAjcn6tfSsmGtJIJQlJ3xpFQhnszQP4-niI-AABUpBTBOqPEAlt3RG1TYv76XQdtrLU1pNDaiRra_Hxwop1Bh3xxyaOHB5npnWz4YwfPc9XeIk-aLmvqPbMGic1EoGJbFQL0_0rn1GASIt3WHH4gUkc0nLeNbIxJtc6lC3inB_47eLwyUv0Nx1YQ2bZtIwMMq716RkajoqjLNYWIqciOaVENffjNpMMVt6vSsKombGnrtmqGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
📊
گلر کیپ‌ورد مقابل آرژانتین
🇦🇷
|
✅
— 8 دفع توپ
✅
— 5 دفع توپ از داخل محوطه جریمه
✅
— 3 دفع توپ خارج از محوطه جریمه
✅
— 1 دریبل موفق
✅
— 8 پاس بلند موفق
✅
— امتیاز 8.4 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/98102" target="_blank">📅 04:26 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98099">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oZyvTBLnrxokMT9OwKNQkqb5QewzCWXfqpNc4JQ8MmU735mAE1hReiKgB5bkDhc-WVHclu0_TzMODA1mBJTFeIRqXujffa6IVn7PQvhOZrJOEGuAw4HV5K3O5J3YswihSweSbjgr49ZQ2-hwSNl-YgbMZFBPRoOLkLrTVLRnUYDgbfGV8BiYpksELkRIRI8fvhXWO3cx6NiJm8EoDrZEyLPu4yVvIUOGy2upd1oEpklWVuSHw0uHsPfz5nOIEg1vXKxWXWUBxXi4mP_k_Z2z1P1uoKw0y-Oqbh9YM6TzDX8Cyl_cm7ZtXrGcamhept_eMkukLqa7xrukHW56hVUwew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🇦🇷
📊
مسی در مقابل تیم کیپ ورد
✅
— 1 گل
✅
— 4 پاس منجر به موقعیت گلزنی
✅
— 1 پاس منجر به گل قطعی
✅
— 6 شوت به سمت دروازه
✅
— 2 دریبل موفق
✅
— 8 نبرد موفق
✅
— 5 بار دریافت خطا
✅
— 33 پاس موفق
✅
— امتیاز 9.5 از
📊
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/98099" target="_blank">📅 04:24 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98098">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">خوب اقای وزینای عزیز الان ما بخوابیم یا سر کار بریم
کیرم
دهنت تموم برنامه هامو بهم زدی</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98098" target="_blank">📅 04:23 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98097">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ivjw8VfJWdZCG00bcv4DkXLI8KzIXon9Y73p9ygHMr0k8tu1CdRVAShVzOl0sFxQda6hd10o5I8yx37iZU4cWvoHwM-okJi0LfjHAKI8j39pUwmhdI8EY8ajI24jRJps0mTdjok-w1Hz-6ncexO-CoHtRR8IibC6Ot5DdtYVVEEfedRlVrVLhsuHejZfJGWljODUh9u7vvVgI3tSwOhLKLMhWYqyiKYy7r6r6CTHlmkM-rolygiLcwATF0hQcj59n80mNFRzaNPzO-QPsPUNohfJX32UeVS3stW8ggJEU77Rz3qnM_vVIJBJYY2vzgSf2TQGtUbxtmxIJM5DlNKEGw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشک‌های لیونل مسی بعد از برد مقابل کیپ‌ورد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/98097" target="_blank">📅 04:22 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98096">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sABrFpvKYlcg04qpq0tbGH1Q4G9O8R8irIWPVa1NkNbc1MMnbFs_oYSkBeMVPNpLcXhaiyqqaTMzbJLs-rEA2idYHgmUX027_N05VsmGCAPIIHs6qZORzvGUAaRIBXk1wUR9YARkLSNn972DPDmsdvbju91neHclHZf-QeHbOo2zwoXEzkGjTntC6hH-j9JHXbme77ZGhlWmqxnCw9kLp5tFoR7gJaHSefgYFzG7T9Q-vGbEpJPUo6V0afFaPGUm2GBRMP6T4phKjQcs5UPMlUXHOYroEVrBdOIh4FxCwtHuEhYnoPzsV5OJqrT067PHadXYHDldvM3HL8mHPfaQew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیپ‌ورد سربلند ترین بازنده جام‌جهانی...
تا لحظه آخر جلوی مدعیای قهرمانی تو 90 دقیقه باخت ندادن و تو اولین دوره حضورشون در جام‌جهانی شگفتی ساز شدن
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/98096" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98095">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98095" target="_blank">📅 04:19 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98094">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a7AI9Jp7M-AnH79hVNw3522jrDxForIqjoV9BoAPcTy3sc1U4a1Oix0lwXb9pcoEQuEYVDloWHjj33__VkzCcapzun-vNK-ZB10w3z8TMagE1ar_7BlvWqt4QfvRqfDKLxw3KKwdiW7kkPblN5kTHiREQkuVERtiKvkbVCY6Lwt3s0u1zHqiwr82MM-b3hIY4erNbO50Og87WevqrpeyEJBWQmUEd2mH6rgJpwtgu7z9x9akSvOkwAr7rvmqk3rFEgbCkb_KCNltTwgkreD3LeOhPhkh3dpovVeCyPaM4KoM8VFwoXb3lb-1SpXVMNZxNTTmsMrStBS2cd0VySl4Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
لیونل‌مسی بهترین بازیکن زمین شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/98094" target="_blank">📅 04:17 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98093">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a0JSThE6bS822_5jTdBKwpTkrRcAH7Bp5fKKJ_lsMOw9aL_WhV2-NelA1A-n9CXV7C_xmZK_2eTE05lhXoLWveCltjAn6j02L3EcNLWWXGuEwt3KRub4OWGgGZmcsmfbW0ppy6oJS3BCSfCpTtb_fOADxzD-iSD7WC8r9OPG9uqZAiqym8RvsrTx09QBVSllwQ6qi3lSx67wHdz2FArTNfV8JNeBVYWmOH92QBgq7TmZ39wW397ZqicJenb0L2bUUgY96BCkpaCoKtWeTQ0LmD1lZBrQC8bF76R8h_sHMiBf499ntv9oVwty6dx20mVS_ErRuJUULCtlSGnAY3HlMw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/Futball180TV/98093" target="_blank">📅 04:16 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98092">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">انگار این بازی خدا میخواست مسی رو بکنه
😂</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/98092" target="_blank">📅 04:15 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98091">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WbxZU17pQ_sACQRX87R5jgrtdkzL72Su31REGPShEv6GB1OUL8QfVtg_-zi91mb336aXa3CgWLsvC8tnmTr9wn_8ICEu8DxD9PEvm-1wBi5lNFbLbf5biYAq196JewS2GavjU_H_ZZs66fuJmfrTzqVG2y1sfPHdZAtBS0BF8ruW7q9gsKMExsE4cLph2H5M937-vMfHxHRnV85fTo2k5LzyqrU3-8jd681EIBNbv3Pvi3a2dL5m2A0NT2NDCXnYGsNrbuMfGH0QEf9jJm6MubO19HHtQ7g7ht3htDAjcqPNrEm4PM1Fo7cnKWLVG8-IIwCy8Z4z1N5gDWEge8HDtA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
پایان‌بازی؛ سکوت برای کسانی که ندیدند؛ خدا با آرژانتین یار بود! کیپ‌ورد تا آستانه بزرگ‌ترین معجزه قرن پیش‌رفت اما در نهایت با جادوی لیونل‌مسی حذف شد
🇦🇷
آرژانتین
😆
-
😀
کیپ‌ورد
🇨🇻
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/98091" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98090">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">با اختلاااااااااف بهترین بازی جام جهانی ۲۰۲۶ رو دیدیم و یک دقیقه سکوت برای اونایکه خوابیدن و گفتن ارژانتین به راحتی صعود میکنه</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/98090" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98089">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🚨
🚨
🚨
🚨
عصام‌شوالی گزارشگر بین‌اسپورت: از مدیر شبکه میخوام هفت روز بهم استراحت بده تا این بازیو هضم کنم</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/98089" target="_blank">📅 04:14 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98084">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=MOgE7mx_ymO7elj1IlcH1socqPmq7DjgXyzaH9IZF2EnwRZNPE8L1V6CDNZNYs_ZOgHYnJ6vN2NMsNggQCQvtd9L23efUC6rCCgkcH85iD05bvAeT-q_0tU6fIsLOltZOpZCpzRgNn4h7wRTgu4s60ZnTuEnlreUWqY8vMUgiXxQrOUK-1TXJNX44PFKrOOhw8BoG4Mr-37IZqw98oj0yTM1XNSdXwdzcKCkmQStDUaRiNDhb2h6wdM7BilxmMzLFYd5xSr4r1TSN0RrHnYc6V8Hw_DJ8Fv3fAmPg3njJ41wIPBRYFzs5L9_KcLFHF-OThQddqbp1ONNRrjaE2gZSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6c46fd63d.mp4?token=MOgE7mx_ymO7elj1IlcH1socqPmq7DjgXyzaH9IZF2EnwRZNPE8L1V6CDNZNYs_ZOgHYnJ6vN2NMsNggQCQvtd9L23efUC6rCCgkcH85iD05bvAeT-q_0tU6fIsLOltZOpZCpzRgNn4h7wRTgu4s60ZnTuEnlreUWqY8vMUgiXxQrOUK-1TXJNX44PFKrOOhw8BoG4Mr-37IZqw98oj0yTM1XNSdXwdzcKCkmQStDUaRiNDhb2h6wdM7BilxmMzLFYd5xSr4r1TSN0RrHnYc6V8Hw_DJ8Fv3fAmPg3njJ41wIPBRYFzs5L9_KcLFHF-OThQddqbp1ONNRrjaE2gZSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
گل رومرو به کیپ‌ورد با پاس گل لیونل مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/98084" target="_blank">📅 04:11 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98082">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">کیپ‌ورد خیمه زدهههههه
😐</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98082" target="_blank">📅 04:10 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98080">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/Futball180TV/98080" target="_blank">📅 04:09 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98079">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Izy7SqzXd6Y_dreQ4SwHWGWTyTrD8dU2aByMIg-NeGxITBLwAk3MI-LClUI_NHw6XVjE4alXS-tw2yn1Ez3_N_Zk4Cpg_UX6I4kXXScRraNwHa_r-afeyEuHJNFIXi0Ae2BQfdP_2t13UUb-BgCVJM9MPT7eKWPNml7RALtpY4EOIQSH1tavD70fVrCaWcZZpLrJ30T0hKcpHSDRXfIrwOrCxmnEe4hcX22SnkzR5zQI2LAzRB9T2atlCT5UR0-rtqhI1n2LlS0yHAILeF6LrcK5w4IaYP5bp6w1CMjrlNhFMt9Fryarlt8M8vDONMBsfARSVY_nN9a6D4DnlIYICg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.  • اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/Futball180TV/98079" target="_blank">📅 04:07 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98078">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">مارتینزززززز چی گرفتتتتتت
😐
😐
😐
😐</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98078" target="_blank">📅 04:06 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98075">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EdicVxJykImMe3xHN2NEC2aPRDWv4ZMdpqDQO4oRs_2mUtvQdJ7iB7ygWUDptUhAdQ5QN_DIfULdfHtuBgMNHPz5_mU3wnDk5_svXJ7tulpoEzXYxhqmz_jzwBizfshPc53fgRS-lIRrlGqN41HqXSjublkRPm0adfIrzq_lMSMb8VwKN9tTT2TpPXGN6HOEPYRnI8mL8XsOEj_Pwm5m3gcQXsRE_7G2ON5SdWrJApUocma_VtYPvtI3LUb6acfwRl8Mvgj8hBkSzsm5FTyXVl09b_N24RaKAtGICKqpk9OlehBd-rqtMwzzXfYJ8CQUiKAiiG2DxWLHrP0GqrIP7g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🏆
• لیونل مسی، اسطوره فوتبال، با ثبت آمار جدید، عنوان "بازیکن با بیشترین پاس گل در تاریخ جام جهانی" را به دست آورد و از مارادونا پیشی گرفت.
• اسطوره فوتبال، 9 پاس گل ثبت کرده است.
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥
👑
👑
👑
👑
👑
👑
👑
👑
👑
👑
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/Futball180TV/98075" target="_blank">📅 04:05 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98074">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">اسکالونی داشت گریه میکرد
😐
😐
😐
😂</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/98074" target="_blank">📅 04:03 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98073">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">پاس‌گل از اسطوووووووره
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98073" target="_blank">📅 04:02 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98071">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سوووووووم آرژانتینننننننننننن</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98071" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98070">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">رومرو زد
🔥
🔥</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98070" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98069">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">گلگگلگلگلگلگلگلگلگلگلگلگللل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98069" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98067">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">رومرروووووووو
🔥
🔥
🔥
🔥
🔥
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷
🇦🇷</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/Futball180TV/98067" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98066">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">جاننننننننننن</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/Futball180TV/98066" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98064">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">گلگلگگلگلگلگلگگلگل</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/98064" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98063">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=UbpdptpSmaIjlvRAasnmYbOt2i9Y_ieObIVGAIlb3rr7xuZCVE-LuhzFV2uzodofX_7BTtbjDYKyWRwnwGto7z9HuxMFEehNKrxvsup-UNBEXkB3nd_V2D9b-Y59nCZprg4QQ0Recg1_hs1O5WPsQD-7l_lF8HId771wlfA_Y7uAlOh-e3PzmXSxHhWUAX0PkC7ALq8Rnqzst0gSsItw7uIGGDSLylI5JB1tWuI5n97aM_ci3tUfp-UkEGAq-6IoAn6_x7g0aLdyoONohZZrHbqS3_rioyEYgvPMnXfhAmIwJ6PEE0V3y0kybq7lQuQ12FT7BXHUKoFtg4IVXDshIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0e6e57be9.mp4?token=UbpdptpSmaIjlvRAasnmYbOt2i9Y_ieObIVGAIlb3rr7xuZCVE-LuhzFV2uzodofX_7BTtbjDYKyWRwnwGto7z9HuxMFEehNKrxvsup-UNBEXkB3nd_V2D9b-Y59nCZprg4QQ0Recg1_hs1O5WPsQD-7l_lF8HId771wlfA_Y7uAlOh-e3PzmXSxHhWUAX0PkC7ALq8Rnqzst0gSsItw7uIGGDSLylI5JB1tWuI5n97aM_ci3tUfp-UkEGAq-6IoAn6_x7g0aLdyoONohZZrHbqS3_rioyEYgvPMnXfhAmIwJ6PEE0V3y0kybq7lQuQ12FT7BXHUKoFtg4IVXDshIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">واکنش اسپید لاشی به سوپر گل کیپ‌ورد خداست
😂
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/Futball180TV/98063" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98062">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ne19lVQnXsrx3Hy0a0RN1Qn2fTAC6z8mpkftGyZyGAlGRvbgD7QvbeG6jK3vCTqpiYEPQVQxMXZzkrfa-gfZZwzB75OnK5OidXyvEQoPxybmB_dUb90OG5udLy1ZD6S7j5V42synZ6CeQokAPJz1-8nnrhqSJlNtT_wdRJ2qMDF49EFv9HZ96IEUSLzPDqABX1LOwSWzhoGxqT7iG-TCAYcfZYhHYxSY9ZjLrzZIkYeC4Ror4U8sd9RdZ0j1ljKIzUCrHdZVwNTlhm2fjkp8KJOxVslOASO_wPjtFoKCuHjycA0fh9vJtEhlUtyw-Sm68L0fx2sAqiHq0K2R7l-lWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بدون شرررررررررررررررح</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/98062" target="_blank">📅 04:01 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98056">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">سرمربی کیپ‌ورد رو بیاریم جای قلعه‌نویی</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98056" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98055">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">اینجوری که بازیکنای کیپ‌ورد جلو آرژانتین پاسکاری میکنن تو خود بازی فیفا هم نمیشه
😐</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/98055" target="_blank">📅 03:55 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98054">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقت اضافه اول تموم</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/Futball180TV/98054" target="_blank">📅 03:53 · 13 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-98048">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/182721537d.mp4?token=WlBSj-3RLmXfJeHUlkvu_RE7B4_JsNuMqGZuiEUE_LEqYoOg4NisXTA1Sr6foD3qkGQ6lCEJjkkHd895t4QZag2yOx4FHK6zKKkEcDmIiofMSSFCXvVARnXxyRyb_2EgZhbWmwNXFcwh5LXpHJj230rk7_ZBLPvdI_caX7hmqNMK_DcwNoAKKP4mqiYniSbzcAZrytZGTVtfVA4s5vvCBw9iu6Ud8shvu6J0jLmfKCHl_RDrq3UlTN4_axhyID0C6PqihyHIGLD1mvOOOXSQkzfFQt2XGhJXa4soJeHAFjdew7h33NW6iZvGgSNHgt_vYykDdkWVf2UtXlgiLlWMgVlI4y9hzbxFsLX88AONtvgleUdBP1AkoMZaG1_bYbFAs7K-JIqKzZ_C3O_vGJXseqIy2VQ89CKo7cXgG8sXYoJOqWic47CotLIMhwE7mvy528gmL4cfsFdDhu-rHv6VvM1B44TMBw_rIoGekd_mzro_NQBoRoshC3_rM9ifyMMj8U_4LdQWVb4cnYezvLTVr0lYnUBNCstHyUVcWgCNC1TTDTf7EEgmJFcZzwtDvmI1DTYYubr4ukfVxkNLZwYRUmdTe9WBKcxNpUljqOjdn4V_HJIHI3vJQPJ_y2Al0gTh0EWYVUR2sJXupOjvgyYCd1xBJtI7lVx_4VqfpEgftK4" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/182721537d.mp4?token=WlBSj-3RLmXfJeHUlkvu_RE7B4_JsNuMqGZuiEUE_LEqYoOg4NisXTA1Sr6foD3qkGQ6lCEJjkkHd895t4QZag2yOx4FHK6zKKkEcDmIiofMSSFCXvVARnXxyRyb_2EgZhbWmwNXFcwh5LXpHJj230rk7_ZBLPvdI_caX7hmqNMK_DcwNoAKKP4mqiYniSbzcAZrytZGTVtfVA4s5vvCBw9iu6Ud8shvu6J0jLmfKCHl_RDrq3UlTN4_axhyID0C6PqihyHIGLD1mvOOOXSQkzfFQt2XGhJXa4soJeHAFjdew7h33NW6iZvGgSNHgt_vYykDdkWVf2UtXlgiLlWMgVlI4y9hzbxFsLX88AONtvgleUdBP1AkoMZaG1_bYbFAs7K-JIqKzZ_C3O_vGJXseqIy2VQ89CKo7cXgG8sXYoJOqWic47CotLIMhwE7mvy528gmL4cfsFdDhu-rHv6VvM1B44TMBw_rIoGekd_mzro_NQBoRoshC3_rM9ifyMMj8U_4LdQWVb4cnYezvLTVr0lYnUBNCstHyUVcWgCNC1TTDTf7EEgmJFcZzwtDvmI1DTYYubr4ukfVxkNLZwYRUmdTe9WBKcxNpUljqOjdn4V_HJIHI3vJQPJ_y2Al0gTh0EWYVUR2sJXupOjvgyYCd1xBJtI7lVx_4VqfpEgftK4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
🔥
🔥
سوپرگل استثنایی کیپ‌ورد به آرژانتین
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/98048" target="_blank">📅 03:50 · 13 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
