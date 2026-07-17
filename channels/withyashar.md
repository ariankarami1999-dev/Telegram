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
<img src="https://cdn4.telesco.pe/file/dL9sMLxqA4yDGGTsZhOrp9saIv2hCznBtK5sqbXZUHHLYRfW7Sa7-BvTY3nQz_tTNWeN52cYqShsiJjEPTlyXiDt0LLAoeItlT021Q9U5CYHb8E58HbvVcKiCD17jy-XDd0UbXrtTd8StZffNfVq2Y5rivJNvEdPPSEfNACBkhDVF10voTlYota7a-qR3UqpIzfHiTFPaXtxGP8xEckVMDXkhW5A98CqV0cj6_QRHIyovEwHA9VkTgGHjUbARCLMq1BHr4pLaHYgBPFMPP24cOeGnMAQsrOov_pbUxQOlstxQufGyoLGpKQTBxKP1Ovd9XFi3dV-FFrr_2CI0GYDAg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 WarRoom with YASHAR</h1>
<p>@withyashar • 👥 399K عضو</p>
<a href="https://t.me/withyashar" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 چنل رسمی«اتاق جنگ با یاشار»اخبار لحظه ای و فوری از‌ جنگ با تحلیلinstagram.com/yasharhttps://X.com/yasharrapfa</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-26 09:43:41</div>
<hr>

<div class="tg-post" id="msg-18511">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/05fd2e417b.mp4?token=oKmE_dhVWRIZGGMnQes7HLh6xKHeIOTC0H82EA1or2KKLLEmOhwG3GoVndr-Lzjs4dPxNaNjLXmZwz42AdKgwYwBI-eYi89aI7h7Wh4ibLqqZ46OqCzn7sZoF9Xlp3NzEie9p3jnDaYB2u6OhZB95d9Ai5oVoPShWfoRDg1xUbHCgDucAVnh6XbLkjnkaRmmOPtS4eeQPf9Ywt75LjrnJCCbUCuA8YP3kv4zfyoXUrbsQEPsAIUBHDcI-JrZyQctnqzh4PjLY4-7mFcRKkqgb1J8e5pPHW8Qi6pTM_21cAiEK61YNSbWwmpCDwYoe84SDgEykxZiZ4k2yaVxmrKutw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پهپاد MQ-9 در آسمان چابهار.
@WarRoom</div>
<div class="tg-footer">👁️ 58.8K · <a href="https://t.me/withyashar/18511" target="_blank">📅 07:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18510">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-footer">👁️ 60.9K · <a href="https://t.me/withyashar/18510" target="_blank">📅 07:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18509">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/12de77f1cb.mp4?token=oXOd1DVL0dMTWLCm0XdYgzj0MGQ0BgvqpFmlxfsCdZyMIBcgmjjDUo37YIkkYCiqCI5AQpBswZXh5z-cmctjPQiYHG2LvcgcuzFp9H0czvwL3QNHCY1iBtaYoWcxCnZAprOtiIIlYmfPpMXF-wW9okWn6u0Hhpe2HuI539zMr4wAGbBaIDT_SmS-0Y2GBblvb5a5AlNrddaR_Zp5i-ARiLH5nZjixGBm9jC-AF2e5pMsl50O-VSd09RJyC-5Ad-tq_ewAG-IXEJlxqyQhQM89JQtDNP0jnSUlefRTw9-fZKfAJ-MmG0t6r4HCmhrVi3boWcepJd9xlInrcqr5HD9TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پرتاب موشکاز لار ، جنوب شرقی فارس
@WarRoom</div>
<div class="tg-footer">👁️ 61K · <a href="https://t.me/withyashar/18509" target="_blank">📅 07:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18508">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/766440ca91.mp4?token=J5paqaqoCjHJkGljy6Mh1kJNi8g9C8wGrxHnkMpuRcaxYhqcna_sZll1xfGJNsOw81SIgEkkme5Du9yiolUHRKaj_-MmpKyVP1lx1IG6Y7Slm3xt9EmNSQjKe5f2-IBzU9Z0BipDZl2MKjY6MfhwFlnytfb5RXXD1C_7EavF1g-gHYKevp3ZpKpmM-nEImhpL1iqtgg2fZfxAse-tyjFsCY_h8u-Uq6Ggj7bgNntiJGndLk4Y9HwcaD2Lygh1mx8RNphG9zAHxi_e3rPo6K1Jr8c663mTMMGo1lvIKz-7dW1ZUUsjjCqPxHEon0WY8D_QQMk608pEuH3lxsmeMKycA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: ما در ایران پیروزی بزرگی به دست می‌آوریم و شما خیلی زود ثمره این تلاش را خواهید دید.
@WarRoom</div>
<div class="tg-footer">👁️ 62K · <a href="https://t.me/withyashar/18508" target="_blank">📅 07:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18507">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">وزارت کشور قطر اعلام کرد که در پی حمله ایران به این کشور در بامداد جمعه، کودکی بر اثر اصابت ترکش‌های سقوط‌ کرده مجروح شده است.
@WarRoom</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/18507" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18506">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/881e02f1c1.mp4?token=Hhh9bTNdW8d8eq6xT7yFsqClB9LGl_ARgqJyXhnJzfKGhDSK5qV73dep30LUkGDTuE-uOH0Kfr1su_EIylpGCzQ2LoK-z9oU_f-Z-ZN_vRaDwMqbYFUxFsmpKxkWdx27U2mIe7u9ySZNxNsaLgydrJ6_K5ufG0YIbugcHs7HsihHCpx8wKFN8OPjei_cjcySQVXHtrrmR4lVk5ZEbShWOnMDBaKMXoJPP66dlm_WuNLpKllz2dnp5AF-_TtCNiHvyEtyzm6ip0g8Qz4eNEnOAeb06r3iA41VBzgL_PdfBlaxlqPqvFY-o-aOfBk5kmKaiVvockeIaRGQqzhN2WpLSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هم اکنون موج جدید حملات خصمانه سپاه پرتاب موشک از پاوه کرمانشاه
@WarRoom</div>
<div class="tg-footer">👁️ 63K · <a href="https://t.me/withyashar/18506" target="_blank">📅 07:10 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18505">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ma30O2KQBThPbjsjnbwkSnDJ43BjYAr3TFOE3bA5HEAx_lwguGxiPq0-fha_TnoWVAjKq6--_DDMXiYH0Bin84xg_5m5SVFvrIKcXjvGP3sVRHyLsQKv4r1798BDmBGJfzvtBBKNJtcG6p5OFpdxP2wsXNcOwMok795Z9iryu7dc8FaMX99oiNt9tA2R3hymIweAsjjBIUvwWUnj-8yOb0D-djpiymuVxVhWo3FVDPhxKBGTKH45t8UDiB2xt1kuUy5VyV5TwqjXLqhPitlB2-Chtoy-d7Z9ioel1OC6lgo2pNofgEWdgvYTA5SjVTAFwv_5QQXdiJxqof0OdFlWlA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الان چیزی از برج چابهار باقی نمونده
@WarRoom</div>
<div class="tg-footer">👁️ 63.2K · <a href="https://t.me/withyashar/18505" target="_blank">📅 07:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18504">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pR_CEL5cgfkhzxR1pMb9VSaSjidE6Uat2s6e4nxwkTlqM_2lIjOg86FpxBwY9Ko5oilzWH3sTXLy3eZ-PQocKf_RKSukfkLDQri4qqShNF4sUvMAorwuEFBPmUwnu2xfHskdLgM8CN-KuDrz5Lz6GTZ9xqwvF0wa0OGpjcWsShOMU4t8CMEA2i1yOql3i1uasAzTgrX0LIEg0VoHL0Vln2Y-NIz51sv1FZVPUDQU3uLzADRYWztAde72V-6Yr8FoT4sEbF4WBADmZJe3jnbxz4koM6DPbzjPhGXbN15yJ3A_t-5w9C-g5lahjbgvXkXg5mxJYw8H741lD8lhyd3wdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حدود ۵ صبح کل چابهار برج ریخت
@WarRoom</div>
<div class="tg-footer">👁️ 63.6K · <a href="https://t.me/withyashar/18504" target="_blank">📅 07:00 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18503">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Y2QqgH2aheRypn9RXqMPMZDwGSkRYX1LVUw90OQuXoJEwIATU16gnkcdP0zH0EWSixfePhkpPEVx8kabvHxAauHTRrjmQ6ziArKJknDb5kO42G5jMr7Mx0L-2UJ_3WQPRgClZ8SonJB_KDRJCHkvHZgmNE_5d5utE-CEWXbGOl5LC9fgv-tUet7GrphspFW1KI2cTtgDzYvNjsRxTkXkueIPEgH7dQDMzMfrnmYpTESawG25dTMwwouJmiEq2IxmEegTbDcqil2AFxBeNWk80f7Oog5V-KiM6gRNvklzujka4L4AuZWsHAUoKj69mFmVOst8yQ-zXwSJYQPxypuMrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرتاب موشک از استان هرمزگان شهرستان بستک شهر کوهیج همین الان
@WarRoom</div>
<div class="tg-footer">👁️ 62.4K · <a href="https://t.me/withyashar/18503" target="_blank">📅 06:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18502">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fe0dc5a19f.mp4?token=Pmrgh0jSbJa_nsNPM12cPGBHg5iXLxKA_rjMffFdZDksljlmnnD81yzYjowQOI1pdPhYPm1H4WnEU5AdRIvQSycopsQzmBqgT0Iv-07wkGI06cLCHHbLQrs6hcct0gJq2H18ghrtIT5q3E32OLVTY3uabg6aI7O6gIuAJeb7VwMSTy9EjCd76P0at6_wosFYjEQy50SFSeBAXME5YsDr0LEQqjiKQQXTEGW-NgrBVhLmn7GeQCilfMP4oaKhN9_Ego2WzwK1lxnM8vMDn8xWKPafWMzINh43VdIqAhI4lE_9MYEsG3PNigy9wNLW2t4psVQfRSSZHgWdNPOOfH6k7A7xbdXvbnXxBLIG7CpcrBqa9aytaOXfbE41EM87urnV-qXPoLHU8sY_-PfHHwqBo72nGNa5uTAVn5xZJ2RU7PrKJwfBhVDrtuWeSyBpNxV4GbZPXYgGJt9XGL-h05tgO5-9c1bGydVEv0b9ldSLTJHr8C5e9ESsEnvFhi2-gFQD9BJVyhjYujicZMhm6GwAxdKWpaBoevKmx_Pul1hrsyEOM_Ted5AndnjsUGxvMZK6oduhdjkn2qqsnz4ekblnPEIgNPYBnT8BwDtjBZuknh0etiXa20ssrB7Tuyy5sxVYllSnkNuM7EpRf_s76OvvXZA9M8J40LmdbLKihpeRJEQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام: ششمین شب متوالی حملات گسترده آمریکا علیه ایران به پایان رسید
سنتکام اعلام کرد
امروز ساعت ۹:۴۰ شب به وقت شرق آمریکا (ET) (۰۵:۱۰ بامداد روز بعد به وقت تهران)
، تازه‌ترین موج گسترده حملات آمریکا علیه ایران به پایان رسید.
به گفته سنتکام، نیروهای آمریکایی با استفاده از
جنگنده‌ها، پهپادها و ناوهای جنگی
و با به‌کارگیری
مهمات هدایت‌شونده دقیق
، ده‌ها هدف نظامی ایران از جمله
سامانه‌های دیده‌بانی ساحلی و پدافند هوایی، زیرساخت‌های لجستیکی نظامی و توانمندی‌های دریایی
را هدف قرار دادند
@WarRoom</div>
<div class="tg-footer">👁️ 65.4K · <a href="https://t.me/withyashar/18502" target="_blank">📅 06:45 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18501">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">نیوز CBS : اگر ایران نتونه پاسخ قاطع به پل‌های تخریب شده بده٫ حملات بعدی امریکا به زیرساخت حیاتی‌تر ادامه خواهد داشت.
@WarRoom</div>
<div class="tg-footer">👁️ 66.6K · <a href="https://t.me/withyashar/18501" target="_blank">📅 06:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18500">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">بندر یدونه زد ملت نیم متر پریدن
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18500" target="_blank">📅 01:31 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18499">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">از سیریک موشک پرتاب شد
@WarRoom</div>
<div class="tg-footer">👁️ 153K · <a href="https://t.me/withyashar/18499" target="_blank">📅 01:22 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18498">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">حملات موشکی/پهپادی سپاه شروع شد و تمام پرواز ها رو هم کنسل کردند
@WarRoom</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18498" target="_blank">📅 01:20 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18497">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d4661b5383.mp4?token=P_PCRam0oKjtBJsRAWX9PaBp-mh49vMLnpYMbfwMkwiIq654uxVJFoKthMyaNvfMVdC6m-qzkiNDgq2cQjfkQH7ui_AJiYTL7lgyY5jQx-AteavNqrNQCQNClPyOnLYPmpqzvYdIEcJvHgGP9Y669kD5h561BKagggFzsYbntjfy_ZSZarwUMVkiQmk-CaeNFjbq7uzBz9NiRy_st2RHmK1-9FVgTNWWwDlNuTKjITf_Blfh0z3K6_JFTZGRJ5fFo0G3TnG6a8fOKWRrYEJWLXxDcGdTaRhqDtJO2fiFxidy-oqjGKlWwnn2ImsqCra3a2VjMuxbLxsqO3LNJijczg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سنتکام اعلام کرد تفنگداران دریایی آمریکا از یگان اعزامی یازدهم نیروی دریایی (11th MEU) در
۱۶ ژوئیه
عملیات بازرسی و راستی‌آزمایی (هلی برن)را روی نفتکش
M/T Wen Yao
در دریای عمان انجام دادند. به گفته سنتکام، تاکنون نیروهای آمریکایی در چارچوب اجرای محاصره دریایی علیه ایران،
۳ کشتی تجاری
را که قصد عبور از محاصره را داشتند تغییر مسیر داده‌اند،
۱ کشتی
را به دلیل عدم تبعیت از دستورات از کار انداخته‌اند و
۱ کشتی دیگر
را نیز برای اطمینان از اجرای کامل این محاصره بازرسی کرده‌اند. سنتکام همچنین مدعی شد
تنگه هرمز و آب‌های اطراف آن همچنان برای کشتیرانی آزاد و باز است، به‌جز برای شناورهایی که قصد نقض محاصره دریایی آمریکا علیه ایران را داشته باشند
@WarRoom</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18497" target="_blank">📅 01:09 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18496">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">برق مناطقی از کیش قطع شد @WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18496" target="_blank">📅 01:03 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18495">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">۷-۸ انفجار رگباری بوشهر
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 159K · <a href="https://t.me/withyashar/18495" target="_blank">📅 00:57 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18494">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">شاهزاده رضا پهلوی در مصاحبه تصویری با شبکه آی24 فرانسه گفت، امروز پس از ۴۷ سال تجربه جمهوری اسلامی، بیش از هر زمان دیگر آشگار شده که بدون تغییر این رژیم، دستیابی به ثباتی پایدار در منطقه ممکن نخواهد بود.
@WarRoom</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18494" target="_blank">📅 00:56 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18493">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پدافند تهران درگیر شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 163K · <a href="https://t.me/withyashar/18493" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18492">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18492" target="_blank">📅 00:53 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18491">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">سخنگوی سنتکام: ما آماده انجام هر ماموریتی هستیم و در حال حاضر 50 هزار نیرو در خاورمیانه داریم
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 156K · <a href="https://t.me/withyashar/18491" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18490">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">فارس: حمله به پل خمیر ۶ کشته و زخمی داشته
@WarRoom</div>
<div class="tg-footer">👁️ 152K · <a href="https://t.me/withyashar/18490" target="_blank">📅 00:49 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18489">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">ترامپ حدود ۳ ساعت دیگه صحبت میکنه
@WarRoom
⚠️
⚠️
⚠️
⚠️</div>
<div class="tg-footer">👁️ 155K · <a href="https://t.me/withyashar/18489" target="_blank">📅 00:39 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18488">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W831MBi7xOexlH3x5HmprsC1Ng2K3i-BeW-SxfKWwLHQQO6M5d82jJbbNGnwuLMZcJAvRRqRjL66ps0kGW346gUb0LSrvXN7mxU5BEWeWnD4D_ot6Y3mSB91XeIOULBTiQtYvGeU6dD5ssIZZiAhTgF64JcWEGuFlbxLKa7IkxjRMKiX-QvX7wMAwcAvwA4CJM-BYLgLkYPFdb643z3zCKfXJoUF48EmH1nZeogjlrtkrhfgfMXzg9-2FmaqYGlnPozkOAV6FO6VwJnilM0IxMfCPdMH2atf2UWb3BAYjASBplf8bAI1PRkJLoB22yderhWURQj4xowBNeQPwhH3dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تمامی پل هایی که بندر خمیر را به بندرعباس متصل می کرد توسط ارتش آمریکا مورد اصابت قرار گرفت.
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 158K · <a href="https://t.me/withyashar/18488" target="_blank">📅 00:37 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18487">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/049770daef.mp4?token=rCfDH3x3FJeu5C6Tw76B1fWpzz-3pX0fZV_EesNTkVuy4Amc_9O6bYa7-IhvjPV2F_vpUAm2HXIHvkLZLS6-KeMiUfY81os92npM7YlY9FRmx4Hut0Ryge9StS2C8Gv-gss4czxzDQHiSInR9zgNx4NiosNXN7F2f3pcqi-GD6Z8azUSyX-E_r0-DkKgloCp3kjGcl50HGMXpHUewZJpZsGkYNue4xiTOKCLUbL1c26fl2Di7QcbloJmlC-iHoazek8gcCjPZs3jupshejlTg0Bp-Tw63Q8MsrZKSXAg2wv0FxXo-ZXGoPww5io5oPjlT0OTtpGEuenyzvlgepwReg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حجم زیاد از پهباد شناسایی در اندیمشک نزدیک پایگاه چهارم شکاری
@WarRoom
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18487" target="_blank">📅 00:35 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18486">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">حمله آمریکا به یک نقطه در اطراف شهر بستان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18486" target="_blank">📅 00:28 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18485">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">برق مناطقی از کیش قطع شد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18485" target="_blank">📅 00:24 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18484">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">خبرگزاریCBS به نقل از مقام آمریکایی:
دستورالعمل‌های مربوط به حملات آمریکا به‌روزرسانی شده‌اند تا شامل پل‌ها و اهداف ارتباطی و تدارکاتی شود، با هدف افزایش فشار بر ‌رژیم ایران!
@WarRoom</div>
<div class="tg-footer">👁️ 149K · <a href="https://t.me/withyashar/18484" target="_blank">📅 00:23 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18483">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bWPz4NDqOZkyyNYzeyHoVxUy5ymLlUbcRs4XEX3gBD9oXEjYxhbILG71oSEBKMDCxqaE8-26uCgRJ_RjHs4QacjbBo3iPf4D4uR4VwhJdbIdoaZrKekxeS1AlVQYKg7oTVzbehzGZ1xMK_rzAro5FFuPK0PZJw7KTD8e939xoXoGQrGuG1FA9IB1bLQHjYaOkcqiwQ-2mCCJkBLkeDG20m-WDxkXz1Vl6Y-TyEP0dWmgmKDA9W_Kmof4PskCwF5tX3lQrBkkOKkMB192t9cx_x81tYO7HO6bB_1gU6FB7GN0rtQROMea_yrgzbOMkrVHK4UWUpHQd76Kv3o2dERjPg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یه F35 رادارگریز آمریکا داره فرود اضطراری‌ میکنه
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18483" target="_blank">📅 00:21 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18482">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">راه آهن بندر عباس رفت رو هوا
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18482" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18481">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">قشم رو زدن ( گویا فرودگاه)
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 146K · <a href="https://t.me/withyashar/18481" target="_blank">📅 00:18 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18480">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">شکارچی سخنگوی ارشد نیروهای مسلح : مدیریت تنگه هرمز به قبل از ۹ اسفند بازنخواهد گشت
@WarRoom</div>
<div class="tg-footer">👁️ 145K · <a href="https://t.me/withyashar/18480" target="_blank">📅 00:16 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18479">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">صداوسیما:تاکنون دو پل استراتژیک مواصلاتی بندر عباس، شیراز، لار و بندر خمیر بمباران شدند و تخریب شدند.
@WarRoom</div>
<div class="tg-footer">👁️ 148K · <a href="https://t.me/withyashar/18479" target="_blank">📅 00:13 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18478">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">انفجار سیریک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 141K · <a href="https://t.me/withyashar/18478" target="_blank">📅 00:11 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18477">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">یاشار همین الان صدای انفجار بندرعباس کنار پارک جنگلی
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18477" target="_blank">📅 00:05 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18476">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d02804dc2d.mp4?token=fY309ajTybgjpg0N-Zm-zRjldb08n00wxpxClx2JfWHUbfQcnUjP3DVdLyuS9nguD9uV0sHJn4kHZZXReqX9eGtmHg69hku5eA6VrLcSFsWQNeik9o7Dw8TvIcSclTI1XOqKeC8Mnn7fvIS8uB28tckXj-JmMveniD7k0aApuJ1RLTYavhHdmTQTZ3t1L02hWnUIz4UOdNmumLfl6PUzfX18esKGIulrcyd4wgJkyta9X7n7beAISQkuhaoQcqdXufQnxBuqCfBfPCtIftx0KPE8gnRKGkdx31VPgNxXqDHZPhXQGr2my5DXDqzc8iqH7h6nkpiLLthPED6w48C03YWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس
@WarRoom</div>
<div class="tg-footer">👁️ 144K · <a href="https://t.me/withyashar/18476" target="_blank">📅 00:04 · 26 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18475">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18475" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18474">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18474" target="_blank">📅 23:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18473">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=nbtYMNNU9gaVpDss9voWQBzou-pI3BF6QI_bT1Ah_NOAzW9dopiZ6D4iHYqiXHWKKPuyl_92y7AKZdTmdCt0dWWOkM4fkqZ3bud37apaCeTHHoxSI2Mp3g7XQIG4NOAbnxlThlOdq4m7BTR7GN2kGHNpc4Q2r50F5lParIt9GN6JkTw5hhX-V9oCn2Uy1p8olAeg3Il1V4TIR-VPiOeoLjagdF0t3_0oN3EDmwb08qFJ6EBgsF4XlZjmwjVvFDLfs1sVb_D88lzm1t460QJEz3-KK_T9GbMKxgESHAOPssrJV2XhG5qneCh-5t_HmRp9qERHY9we7iK6xmsKlM3fCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e1b7bcf1e5.mp4?token=nbtYMNNU9gaVpDss9voWQBzou-pI3BF6QI_bT1Ah_NOAzW9dopiZ6D4iHYqiXHWKKPuyl_92y7AKZdTmdCt0dWWOkM4fkqZ3bud37apaCeTHHoxSI2Mp3g7XQIG4NOAbnxlThlOdq4m7BTR7GN2kGHNpc4Q2r50F5lParIt9GN6JkTw5hhX-V9oCn2Uy1p8olAeg3Il1V4TIR-VPiOeoLjagdF0t3_0oN3EDmwb08qFJ6EBgsF4XlZjmwjVvFDLfs1sVb_D88lzm1t460QJEz3-KK_T9GbMKxgESHAOPssrJV2XhG5qneCh-5t_HmRp9qERHY9we7iK6xmsKlM3fCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کهورستان بندرعباس ۳ تا پل رو زدن
@WarRoom</div>
<div class="tg-footer">👁️ 142K · <a href="https://t.me/withyashar/18473" target="_blank">📅 23:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18472">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9lc5WTj2so5AdkApBBnInjIQJvR86EJ1iRrnFaqUrsNu2r0xdnzdFkXGwHV0p75dA21PVv1HmyQ0Xe18JSj5VftoLT2yYVxqT4SeR4efnEew3njIohU5xxvylPuO0Ea7hrhR28XPjFe1U6jAor_k8tf5KuGruRYdmuQgIDUDrE3jaQJfNQAFoLFKYimz0P4IBCIfv16ovihL33-HszgfIOY2DE9JY-Mm6VHOW-z6AROCZjXUyESob-58Dh5y_kqh7BQ7UX0LBm7bGdeVSw7otiRxYilMzEclBMgW9trLOmMi_a-BNRheyay10nZ8FE-6KVeSVDEsMz8dsBDqBbKgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فرودگاه ایرانشهر
@WarRoom</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18472" target="_blank">📅 23:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18471">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مهر: دقایقی پیش، صدای حدود ۶ انفجار پیاپی در حوالی شهرستان حمیدیه شنیده شد
@WarRoom</div>
<div class="tg-footer">👁️ 138K · <a href="https://t.me/withyashar/18471" target="_blank">📅 23:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18470">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=Ze3iTmgblj6kC53E6OyA6ekBjG6R3eWlwGJbI-IXs40ZYYoITAf2vGtI8x7jJWOD0WvcbL6vJXgZIkE3kIRaE3-u30PfJWTaXEYbzg-mTa3eUnGw7Jqd4mxYNkX3I4tW5MjT91YYffTeh01JKSyP41Fl7EDMGnPZ3Fb0WF56UYxXRB--7mxKE3O9v_i3TtYKGPXqm6T0ZpnuFqvlIgj6hHO4V18ohk_b2umhHiLV9fn00-F4D3mkZZ0m7ULusLK6zufqldiDN-qykqmM7M7WlpqxJZyEcifsaIdiCAwlkWGDDmrLRR3PxerqOCSxHEfCAY6ZsGKErcJiPrC4XHZEeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1cd2970e89.mp4?token=Ze3iTmgblj6kC53E6OyA6ekBjG6R3eWlwGJbI-IXs40ZYYoITAf2vGtI8x7jJWOD0WvcbL6vJXgZIkE3kIRaE3-u30PfJWTaXEYbzg-mTa3eUnGw7Jqd4mxYNkX3I4tW5MjT91YYffTeh01JKSyP41Fl7EDMGnPZ3Fb0WF56UYxXRB--7mxKE3O9v_i3TtYKGPXqm6T0ZpnuFqvlIgj6hHO4V18ohk_b2umhHiLV9fn00-F4D3mkZZ0m7ULusLK6zufqldiDN-qykqmM7M7WlpqxJZyEcifsaIdiCAwlkWGDDmrLRR3PxerqOCSxHEfCAY6ZsGKErcJiPrC4XHZEeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 147K · <a href="https://t.me/withyashar/18470" target="_blank">📅 23:43 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18469">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-footer"><a href="https://t.me/withyashar/18469" target="_blank">📅 23:39 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18468">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">پل گچین رو زدن
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18468" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18467">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجار اهوازززز بازم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18467" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18466">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b364528971.mp4?token=P992DsRfI0KccSa0GXyBDkF_rFKU8lFXekebEgvcdoIVRhIefDwrNvFy3_RR-wBJRRzbIuqZTiugGlHKrQ3RN8KqcV9wZMd9lLs6__7PXbbLDvLy5GNOVb25Sa0H_ONpd8IuQav88KvlAzNJpCBUy_qwLLdNnheUg65BioenUKCI2H6Gxh4Xw3oA-bXWuQrMTftU9RKQwi35VBPV0tYyqj-FCo-F1zkIAubBAbBrN_UcAELD-SwAF0r69pLlSuhLTQDls9m359tHYU46_TEkkFMT87wpiwrh-3kVpImpmpLf2dACT0-tytQisAT3046azbI7pciPGfDoYtYDHNTgIA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b364528971.mp4?token=P992DsRfI0KccSa0GXyBDkF_rFKU8lFXekebEgvcdoIVRhIefDwrNvFy3_RR-wBJRRzbIuqZTiugGlHKrQ3RN8KqcV9wZMd9lLs6__7PXbbLDvLy5GNOVb25Sa0H_ONpd8IuQav88KvlAzNJpCBUy_qwLLdNnheUg65BioenUKCI2H6Gxh4Xw3oA-bXWuQrMTftU9RKQwi35VBPV0tYyqj-FCo-F1zkIAubBAbBrN_UcAELD-SwAF0r69pLlSuhLTQDls9m359tHYU46_TEkkFMT87wpiwrh-3kVpImpmpLf2dACT0-tytQisAT3046azbI7pciPGfDoYtYDHNTgIA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس جهنم شده
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18466" target="_blank">📅 23:37 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18464">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">بوشهررررر سنگین
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18464" target="_blank">📅 23:30 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18463">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">قشم روستای مسن رو زذن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18463" target="_blank">📅 23:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18462">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">همدان ، احتمالا نوژه رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18462" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18461">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">فرودگاه ایرانشهر رو زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18461" target="_blank">📅 23:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18460">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">روابط عمومی دانشگاه علوم پزشکی هرمزگان:
در پی حمله دقایقی پیش به محله تپه الله‌اکبر شهر بندرعباس، تاکنون ۷ نفر از هموطنان مجروح شده‌اند.
بلافاصله پس از وقوع حادثه، تمامی نیروهای امدادی و درمانی دانشگاه علوم پزشکی هرمزگان در حالت آماده‌باش کامل قرار گرفته‌اند و اقدامات درمانی لازم برای رسیدگی به مصدومان در حال انجام است.
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 139K · <a href="https://t.me/withyashar/18460" target="_blank">📅 23:16 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18459">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">سخنگوی سنتکام: ما در پاکسازی مین‌هایی که سپاه پاسداران در هرمز کار گذاشته است، به پیشرفت‌هایی دست یافته‌ایم و ادامه میدهیم
@WarRoom</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18459" target="_blank">📅 23:12 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18458">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">تسنیم: دقایقی پیش تپه الله اکبر بندرعباس مجددا مورد حمله دشمن قرار گرفت.
حجم این اتفاق به حدی بود که برق این منطقه در بندرعباس در حال حاضر قطع شده است، هدف مورد اصابت در این حمله یک دکل مخابراتی بوده است.
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18458" target="_blank">📅 23:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18457">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">سلام یاشار پایگاه هوایی بندرو رگباری داره میزنه الان
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 136K · <a href="https://t.me/withyashar/18457" target="_blank">📅 23:06 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18456">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">قشممممم بد زددد
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 135K · <a href="https://t.me/withyashar/18456" target="_blank">📅 23:05 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18455">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">دارن گرم میکنین ۱ ساعت دیگه میان شهر های عمیقتر
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 137K · <a href="https://t.me/withyashar/18455" target="_blank">📅 23:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18454">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجار قشم
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18454" target="_blank">📅 23:02 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18453">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">بندر عباس میگن عباس هم رفت فقط خود بندر مونده
@WarRoom</div>
<div class="tg-footer">👁️ 134K · <a href="https://t.me/withyashar/18453" target="_blank">📅 22:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18452">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">اهواز باز زد سه باررررررره
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 133K · <a href="https://t.me/withyashar/18452" target="_blank">📅 22:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18451">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-footer">👁️ 132K · <a href="https://t.me/withyashar/18451" target="_blank">📅 22:55 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18450">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">گزارش انفجار در جم
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18450" target="_blank">📅 22:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18449">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18449" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18448">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">کبودراهنگ همدانو کوبیدن
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 130K · <a href="https://t.me/withyashar/18448" target="_blank">📅 22:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18447">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=ubOKSyFfWR4WUNTVhpERY27FYjFQ7EmpWbQFCghSj3PEDeSdCu2L_SHdZApUA8JG-6Se6FjkZJ4wtEVXppfS9vnSkdoZc4dxloJcXXzceh357RiDhC1eQmlmid_DgvVNUkPPy7BTdLt7vN7RkrMrmWMYFTz_SJKbBqf_U2-hACqN92zUQhc4c0qag_qwbz0msgQm-h3_M2E-roG58lTzlSyaUBm6DmznXfNRHZTxwcbqIIpKHIX9VTjUV8OThzWL_IcbuGLKlTalL1JuAaXDD2xBieTNuJy9NT61V9W7JQaV8tpI7PtLCi9J1uYKfrRVIYqggrbCv-Y2nxYqS1qeVg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9358a92cf5.mp4?token=ubOKSyFfWR4WUNTVhpERY27FYjFQ7EmpWbQFCghSj3PEDeSdCu2L_SHdZApUA8JG-6Se6FjkZJ4wtEVXppfS9vnSkdoZc4dxloJcXXzceh357RiDhC1eQmlmid_DgvVNUkPPy7BTdLt7vN7RkrMrmWMYFTz_SJKbBqf_U2-hACqN92zUQhc4c0qag_qwbz0msgQm-h3_M2E-roG58lTzlSyaUBm6DmznXfNRHZTxwcbqIIpKHIX9VTjUV8OThzWL_IcbuGLKlTalL1JuAaXDD2xBieTNuJy9NT61V9W7JQaV8tpI7PtLCi9J1uYKfrRVIYqggrbCv-Y2nxYqS1qeVg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمله موشکی آمریکا از کویت
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 131K · <a href="https://t.me/withyashar/18447" target="_blank">📅 22:48 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18446">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">انفجار در قشم
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18446" target="_blank">📅 22:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18445">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار دوباره بندر عباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18445" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18444">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار جزیره لارک
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18444" target="_blank">📅 22:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18443">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">اهواز ۷-۸ انفجار در مجموع
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18443" target="_blank">📅 22:41 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18442">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">اهواز رو بازم زدن
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 126K · <a href="https://t.me/withyashar/18442" target="_blank">📅 22:35 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18441">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">بهبهان رو زدن
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18441" target="_blank">📅 22:34 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18440">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجار سنگین اهواز
🚨
🚨
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 128K · <a href="https://t.me/withyashar/18440" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18439">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3e0125430a.mp4?token=TQqLxGIgmVsob4CIV3qLC5iab6hjkTJSixBfxMQ3sOJBfD98tg0Q3JJwXdWZKIG7EIKY8iXVQNCAk6xVI9c_ksEyTv67zGeQwdbMQKLHiZdhihsk5GLT3LaNl4fai0yCVtyyqOfYPoTT8xuwxlJa1gE_84hqbst_aAav5JjFBLjAhDckzSIgNKpHgOMXMJoOwUZMvS5szQ9J2SJvxEYnrTUbMG3I8wgL-OpfIxRfA3Lt8xxO6jjdOyKvbtoMx0w74OOKHWym7IP4td8t5cypCZgM1H2NUKkP1O6Oh3RBFXzruzvAZxgN3Wm49_RcPhjy6ARoUaaMwp7liKnBuOo6PA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیو از بندرعباس؛ مجدد همون دکل رو با 4 تا موشک زد
اینبار واقعا شدید بود
@WarRoom</div>
<div class="tg-footer">👁️ 127K · <a href="https://t.me/withyashar/18439" target="_blank">📅 22:31 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18438">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">رسانه های سعودی : شنیده شدن صداهای انفجارهایی در بندرعباس، بوشهر، چابهار و کنارک
@WarRoom
.
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18438" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18437">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">گزارش انفجار‌ در کیش
@WarRoom
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18437" target="_blank">📅 22:26 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18436">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Dnq4KFGrDEQfLmyK-TG6Ta9xWNIrZkL3SsP7Vh1ENk_YeONhxjnd7qlsQnCRURh7GKZ2_r27pCwRGlebcqotkD2f3_QwiJ-d8zWJHuJk9l7F1ayRiKmP6AGLEF2MLQbUPwlX9lL4rsuHtDX4IgZJqsgti4a1xDxevIW_9ZauXi02Irj6i1dTixmLbj0d52wV7bKzeMZj677SRgEQ5jvZT8n57__ms5DCTRjlvitv2zal6cVH1hpkem1BVMf4NtEZdKs7EiHxO2fxRJ2CsdxHQnbYbt3vhFVvnP7UqIXLAardYn5AB4LtSJM7u191R6q44iVidczqHa2dx8QcwYu5Fg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e346db66bb.mp4?token=Dnq4KFGrDEQfLmyK-TG6Ta9xWNIrZkL3SsP7Vh1ENk_YeONhxjnd7qlsQnCRURh7GKZ2_r27pCwRGlebcqotkD2f3_QwiJ-d8zWJHuJk9l7F1ayRiKmP6AGLEF2MLQbUPwlX9lL4rsuHtDX4IgZJqsgti4a1xDxevIW_9ZauXi02Irj6i1dTixmLbj0d52wV7bKzeMZj677SRgEQ5jvZT8n57__ms5DCTRjlvitv2zal6cVH1hpkem1BVMf4NtEZdKs7EiHxO2fxRJ2CsdxHQnbYbt3vhFVvnP7UqIXLAardYn5AB4LtSJM7u191R6q44iVidczqHa2dx8QcwYu5Fg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس هم اکنون
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18436" target="_blank">📅 22:25 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18435">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس @WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18435" target="_blank">📅 22:24 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18434">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=oYgmqBY9A8liNqnJVhu5hYmRd34W9W2SLLSeDcXBpbSinEfO003dzq8wQIJqhQJD1WncJ-W1tSfQ87Nzxm-gDDNemITD70A9GdEmyfWAlZuP5gE7ceehoULuwpNS96Rc9DXzb_0csLJFX1QigTtMtvcjEjhKxvW6hcvRtPodjsNEbvsVEVQMi83-toBQL898d_zB-1Y31roXkYorxd6m3a55kjy3Ie_PqrCI2Ni9Bt43OxKx_3l2-NodweA1SLahLh05euMc-RQO0ZcjhxooDv0mWZykqG7oQCb9DBcEFeCuO3CqFn85Eavo0ZyhlK_6z7vy-W0IP8BY5J9R6hJw0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/35c067b6c9.mp4?token=oYgmqBY9A8liNqnJVhu5hYmRd34W9W2SLLSeDcXBpbSinEfO003dzq8wQIJqhQJD1WncJ-W1tSfQ87Nzxm-gDDNemITD70A9GdEmyfWAlZuP5gE7ceehoULuwpNS96Rc9DXzb_0csLJFX1QigTtMtvcjEjhKxvW6hcvRtPodjsNEbvsVEVQMi83-toBQL898d_zB-1Y31roXkYorxd6m3a55kjy3Ie_PqrCI2Ni9Bt43OxKx_3l2-NodweA1SLahLh05euMc-RQO0ZcjhxooDv0mWZykqG7oQCb9DBcEFeCuO3CqFn85Eavo0ZyhlK_6z7vy-W0IP8BY5J9R6hJw0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18434" target="_blank">📅 22:21 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18433">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">انفجار چابهار
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 120K · <a href="https://t.me/withyashar/18433" target="_blank">📅 22:15 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18432">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">بندرعباس چپ و راست آمبولانس و آتشینشان میره سمت شرق بندرعباس
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18432" target="_blank">📅 22:14 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18431">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">غروبه هرمز @WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18431" target="_blank">📅 22:11 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18430">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">سنتکام : در ساعت
۲:۰۰ بعدازظهر به وقت شرق آمریکا (ET)
امروز
(۲۱:۳۰ به وقت تهران)
، نیروهای ایالات متحده
موج جدیدی از حملات
علیه ایران را آغاز کردند.
این حملات برای
پنجمین شب متوالی
با هدف
تضعیف بیشتر توانمندی‌های نظامی ایران
در حال انجام است
@WarRoom
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18430" target="_blank">📅 22:07 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18429">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گزارش انفجار بوشهر
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 122K · <a href="https://t.me/withyashar/18429" target="_blank">📅 22:04 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18428">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لطفاً تا فردا صبح هیچگونه سؤال سیاسی اجتماعی و تحلیلی نپرسید. لطفاً در مورد اینترنت خبریی ندهید. لطفاً صدای جنگنده ها را نگید. لطفاً فقط گزارش صدای انفجار رو بدید و تصاویر و عکس. همچنین پیامها را فقط همیشه در یک متن بفرستید، نه ده پیام جداگانه.</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18428" target="_blank">📅 22:03 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18427">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vff7fqWUCnMZ6Uy04y7_PHhN7DwDWqG2n98emQz-jINEel7OdapTCcWqeo8_HQAEYoQwHtIrcl9KxtCx6iqEuWk06OyiTJCZOxX1HHHfmcDRVHvMWiyeCRq0-T5JpzzhKDGdw26I9SP5j_hzIZAf4rVxYZYVWlMmxaHQJrd5M4UNsHP2V0aylhj2Ku98B9_YjIDY2Nu_AzP1bJ6oMecR_s4JnhL3thIdFgZbZa2zXUnuPKctBihALg5U8xpn5BRWfUptzHROHYvloeTTzw7gtau7YK9NNqbVU3cDRgY53IpriqUpJ0kwOXZkr8NHXgHX7wIerL3IxWi65nwa2AyNDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هم اکنون دوباره سمت ایستگاه رادیویی پیامبراعظم بندر عباس
@WarRoom</div>
<div class="tg-footer">👁️ 124K · <a href="https://t.me/withyashar/18427" target="_blank">📅 21:59 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18426">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18426" target="_blank">📅 21:58 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18425">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">ادعای ترامپ مبنی بر آزادی یک زندانی آمریکایی از ایران تکذیب شد
ترامپ در حالی این ادعا را مطرح کرده است که با توجه به بررسی‌های صورت گرفته هیچ زندانی محکوم و یا جاسوس آمریکایی با مشخصاتی که ترامپ اعلام کرده و یا با هر مشخصات دیگری از زندان‌های ایران آزاد و یا تبادل نشده است.
@WarRoom</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18425" target="_blank">📅 21:57 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18424">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">بندر ادامه دارههههه ۵-۶ تا شد</div>
<div class="tg-footer">👁️ 117K · <a href="https://t.me/withyashar/18424" target="_blank">📅 21:54 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18423">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">ولی باید ببینیم امشب به اصفهان میرسه یا نه الان مرکز هدف اصفهانه کوه کلنگ</div>
<div class="tg-footer">👁️ 119K · <a href="https://t.me/withyashar/18423" target="_blank">📅 21:52 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18422">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">انفجار همدان
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 123K · <a href="https://t.me/withyashar/18422" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18421">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">تهران رو شاید بزنند ولی‌ نه به حالت زارتان زورتان به همون پارچین اینا بزنند فککنم</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18421" target="_blank">📅 21:51 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18420">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">۲ بار قشمممممم
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18420" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18419">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">قشم رو زدنننننن
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18419" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18418">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">بندر عباس زارتان زورتانهههههه
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18418" target="_blank">📅 21:50 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18417">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
) @WarRoom</div>
<div class="tg-footer">👁️ 116K · <a href="https://t.me/withyashar/18417" target="_blank">📅 21:49 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18416">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🚨
🚨
🚨
حملات امشب شروع شد
@WarRoom
🚨
🚨
🚨
🚨
🚨
🚨
🚨</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18416" target="_blank">📅 21:46 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18415">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">شروع انفجارات بندر عباس
🚨
🚨
🚨
🚨
@WarRoom</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18415" target="_blank">📅 21:45 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18414">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae627587b9.mp4?token=iLCeomC25M2qcPzyRzJof_XcoeG7oyeMmXO0nGqKNW4vc-2GhiUQhhiiL_54j8YCrcGe7QclVD-L2gQwE7In-msNcj7tRaNm3ApoWGcoHtqjhaLmXRuME6MA0WPuakielaSF5sOZgNCDqq3N5rvyt2CVdrRaH8wuM_BgywCPOOwN9o4NOZb6i1XyrW9NTP9tXH8Gyvua6k3zKZwfO5kFxCYu9nN8jS3SHEf4ahUr4qeClKttf3tFb_gsGWZWIIYDQoghPkFC0ZcSbj9T1ERIHqjo42VyUT0ZIrulIeMCmqJbmDSYFGMabLLBwWHVPDMvSFbdIOXklYromW24d4w_mLQQWyuxSuQP359P3CChZTSotX2_tTUkkBEh5aWs-Xe94yRh2f1k-oEhT8WG_8ddEdCvFAKW7j4g1o__0hLAGQNIiPkrK7OkLyIZSsy_5I7eMR225lRUGGMDiUsP-XqJ2UlHKh99ZlBaXut5o1sw2JWcHCOk3tEUHkwj8gz4WzndHmKe2O53urfNFS9c22qXNhlQpSjr52ceCu_hJENbVySlTMnoNinhIhL61o0UmdUXMHwDmg_ay56Cqbp-1qziM7BpqIUzam99nd5Tl6Ms1Jf-6eQZzL4qPJGBdUNrBRbDwtTSDW7-gsP67LhuFIlmR7Yi_-KncWbpp09Kt0DHNH8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تناقضات میان ادعاهای ونس و ترامپ نشان‌دهنده این است که در یک جبهه هستند
خبرنگار:
درباره ایران: رئیس جمهور ترامپ اخیراً گفته است: «از نظر من، سروکله زدن با آنها فقط اتلاف وقت است. آنها دروغگو هستند. یک جای کارشان می‌لنگد. آنها عوضی هستند. آنها آشغال، بیمار، شرور و خشن هستند.»
سپس ونس، معاون رئیس جمهور، دیشب به جو روگان گفت: «من از آمریکایی‌ها - و صادقانه بگویم از مردم کشورهای دیگر - که می‌گویند نمی‌توانید با ایرانی‌ها مذاکره کنید، بسیار ناامید شده‌ام.»
خب، پاسخ شما به این تناقضات چیست؟ فکر می‌کنم با توجه به پیام‌های متناقض، می‌توانید درک کنید که این موضوع چقدر برای آمریکایی‌ها گیج‌کننده است.
کارولین لیویت:
رئیس جمهور و معاون رئیس جمهور دقیقاً در یک جبهه هستند.
@WarRoom</div>
<div class="tg-footer">👁️ 121K · <a href="https://t.me/withyashar/18414" target="_blank">📅 21:44 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18413">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-footer">👁️ 118K · <a href="https://t.me/withyashar/18413" target="_blank">📅 21:22 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18412">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/427068d887.mp4?token=J2S7HITiRuaMZHvef2USbKjPKlniSUJ8sXSCXgW8N_UYvl_K_FstXCx-iXe8CCrBgz8GyIb0C7dfdRoGD6F87PabNEHOqil80WaDKzR-QWa0sKpCDs46yjQWoUfW1yCUMMNZB4Ux1yp6TsGVhEWAWtVRy50NLLY08Tk-k54RhfyvJPd3-jvga8fGeCXCpLz4yy5odLySyVSxjtp_fYof1J59FiuMymHgKgJ7ZGLL8YfcYthEKhAeWQ4zh9c1dBbanMfiOeHpsjnR0uGeHCL1OqhFTYus3Hxq4vj_aHFxHi-vDxYryPIHz_f25wgi-NS64Dw-5elazxgNkg54eMJim7qcCVGCu7lz09zjj08Y44Dh8b7jKzKCi-E2rOxxStPZEpp8np50XJ9CL0K2m2jslYG6dABmkPvad6PBEc11UF3kjqJjrOj687d-BxPBEQxDCxJFDY1lcqWr8tAxv10NsIS4TCLQuqpyAlr5NiGSe8WrbjJ3Y386YZed_9wHstgLdVki_aOLqqGR5tfpj7LBlcJD4tpO8BEsWJjsdYQXcuvYr-euy7fL37PjzhhIMGs-RxNBpa5zliKZ-GIqLdaEwp5dqdvg4OyA4ETU83WwRmwrwJlG78b4UWgR9tbNc4ZTa_l62xOQ-uC-XqxQCfV9s8enRxNGy4KDV2mCrXIvgvg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اتاق جنگ با یاشار : وضعیت منطقه (۴ سوخترسان جدید بلند شد ، تحرکات زیاد در منطقه
🚨
🚨
🚨
🚨
)
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18412" target="_blank">📅 21:13 · 25 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-18411">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">کانال ۱۵ اسرائیلی: ایالات متحده در حال آماده‌سازی برای گسترش حملات خود علیه ایران از نظر دامنه و تعداد است.
@WarRoom</div>
<div class="tg-footer">👁️ 125K · <a href="https://t.me/withyashar/18411" target="_blank">📅 20:51 · 25 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
