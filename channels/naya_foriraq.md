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
<img src="https://cdn4.telesco.pe/file/uj3oj40kWhW9OP3fKi7TzvQqREeVC10_UiJKzSzUDOH3Rtj1i60XZ6RSpNeNo4ezQQJSOI6r0wfEC4dBC9_rCI95Q_cdCWNH8BC2VWasfGgB-JBzd4VtrxdGDML-J29Dy5S2LV9UFrLVG7HulKEM6ZfABw8IzIvBcvYn6joamEuzPoxzBF97Jf0VzvmwMptw8jy_asIvK-IQuTa2tBH9Y_tJc2kCU6UvTV6axICsJmPfa3HxVQqjeSdd3i7xLnYCF5MVtzlCZqYAYUQUtNHK5Dl6hE3frUmuc_bDZcy0MM1Y3VDBFKG32xEfZqnUZWKs-5HKU0HtHQbNOsRXMwE0eA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 255K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-15 19:28:02</div>
<hr>

<div class="tg-post" id="msg-81231">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5df5b7d88.mp4?token=DMGlAzXL7vFtTG_txTnC5OjilhYAtVBU2svCZTIa-4c8UZ4P8bJD98EXPGbgnl5L_q814zX-W0QV7MwK4WMhNPs2Urpv-ikrVwHEFQ9M9sB5ZfVePnysfAp0SMDWbJhhB3kbtDcEUwlEoXsE0Qj8wN1Hx8s2_LeNQ0tzg8Lq5LLZlDmnhgp95OUV61Rd6pdDyt4QTzBVJV-iTkyVTG40KReMY7V4jhMxhUp90cAxw2S8LlCxt1ZQvHruyCW_deS1TXJjYvVy822O-vacRoPOwNvhYMO7ct-S6Aan3uYLZMBNQJh32tNvBxRiSR7WHsFXi9HNG0a9WFCbk3CJ13QlFSL1Lgcz7L_OPjTIMU_yvAOodEvoeDnAPu2jJA6bZAQocqE7f9gWHhWy-nfTrpcD_crRewCdrkHTq7aXqa7pCuRVbO0Y4594cjf_TEjIltXQRNeOcugsbVAMjMAuXVpQyoJdbVP4ZZg7dAOGET_oZsDO5pujcL-JX8xVgEqv0fm9RJObXD9H9tpix9MLbj0-9mLgyN-d16qkUyoZe7xF9OBXcKHx0gGilMx9ymiNPZ1UMGhsGLPkg2rNBwMeWCSZbccOSpsx_940C3mOI-elwMeUeTVVAGcYSFSz475Gzmo_GqtAERV_FvR8prg8bnfSq5jbnQjpX7ewpZYV1FOgCKE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
تطور جديد غير مسبوق تشهده سوريا في ظل حكم نظام الجولاني الإرهابي.. انتشار مرض الإيدز في بنوك الدم السورية بعد تبرع عدد من المواطنين النازحين إلى دمشق من إدلب ودير الزور وغيرها.</div>
<div class="tg-footer">👁️ 801 · <a href="https://t.me/naya_foriraq/81231" target="_blank">📅 19:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81230">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">🇮🇷
محافظة سمنان الإيرانية تعطل الدوام الرسمي يومي الثلاثاء والأربعاء تزامناً مع مراسم توديع واستقبال الشهيد القائد الثوري.
▫️
تعطيل محافظة مازندران يوم الثلاثاء</div>
<div class="tg-footer">👁️ 2.65K · <a href="https://t.me/naya_foriraq/81230" target="_blank">📅 19:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81229">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8928abb69f.mp4?token=PbI3u1n4bPOIj_S0y9Y8kQtu266Lp6Hg3zZ8ZWHQZAAKmfaDUgsK0EV_TSmsp29HKiKz1A60Mm4A7EaKRT58RcWleDLr9ingrgW4lH10WDfPtkMSuSWBlpv1Rr4ZEvsMnhMjn8cf9L8f6bAt2fNv17M_WaM3Xs6ZiHeXXjN2nafnULUSLqBT2k-xszTdsKTACKE9RKlZgrUEAb5zVGYIne1szTbSSypkmCwXoh9nwC91mcuJh-oNca_ROIZNkTGrqV6IKc2nIFYcsf72__y7rBdb0dq2lg9q6CrK5vGCMI4ICAriBpjIWIomM4PGyrW44rXkrGoqaSUd_xEVNcdPVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
ناقلات جند صهيونية تتوغل في منطقة حوض اليرموك بريف درعا جنوب سوريا بعد سيطرتها على معظم مناطق ريف درعا.</div>
<div class="tg-footer">👁️ 4.68K · <a href="https://t.me/naya_foriraq/81229" target="_blank">📅 18:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81228">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1b83f2717.mp4?token=ixcd8jSoKB3rbfkKJ-frzOaHqFd82lH2wCuKH8zh3mQxeE2MT2hlLGb5h37MBt7kK0KzTWh8I6v2RLflza7PJl-XgOcRR8beKX_wUY4rNY77_TmrRbcp4PHtHeLu0ZQM0Rv66nKUb3HwZu4RN8bfUl2bvDqM7bFyqGztXpYneBlTsMlPPH_mXfTSSO74ikn1ENnZQDLJwMck_htZW2TD4uqxxzE7bB8n-Wc7tWDnamLJ-v3Zxr18vhzs0lU7bD3Q_zGg_iK694hrEYduRpxSi1Zbr4Y_IHzOwB2Gk_NpYy8Tdtd0r2HKNIqmQ4mnObm3QJwWJF7Qg2I_i3-4cAr0Wg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
مشادة كلامية داخل البرلمان العراقي ونائب يطالب رئيس البرلمان بالاعتذار بعد وصفه البرلمان بـ"الروضة".</div>
<div class="tg-footer">👁️ 5.23K · <a href="https://t.me/naya_foriraq/81228" target="_blank">📅 18:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81227">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة:  - سيشارك أكثر من (3000) إعلامي عراقي وعربي وأجنبي في تغطية مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره).  - ستتولى (2500) كاميرا و(23) مركز بث مباشر تغطية مراسم تشييع السيد الشهيد آية الله العظمى…</div>
<div class="tg-footer">👁️ 6.21K · <a href="https://t.me/naya_foriraq/81227" target="_blank">📅 17:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81226">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: سيشارك (751) موكباً في مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في النجف الأشرف وكربلاء المقدسة، والعدد مرشح للزيادة.</div>
<div class="tg-footer">👁️ 6.44K · <a href="https://t.me/naya_foriraq/81226" target="_blank">📅 17:54 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81225">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0e74d73728.mp4?token=ofY9WKWbvvrUuzB6tZ3y4zhdv9zARIq6ar4MBuZdkMxADr0851PnyhPiwO2U2JRy7ww32rZBasYL21js78H-s-qQfoyV9fMyijrp-DJiR6NualbSuF6q3yM3OnqsvzM9pS1X1gdDait-6NP8xGXredR9GAegtIcTgsDdPGiZJCyrmgbfrh1JwESvYLG9CtwGhNcbe33i_BanZQtk80Bjh-bS9MncO33tLtv4o4NILVguH-Et4RV773frvjwuCr-YFCb4Hpn_W51vLA2n3VaVeWrV0gNXGz3fwpPyshPKE6gXL0hOhPa66Zf-E4xyjUPFw7dJUJM1KS2QW1vf_0Mghw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: تحدثت مع إنفانتينو، رئيس الفيفا، بشأن البطاقة الحمراء، من غير العدل أن يقوم الاتحاد الدولي لكرة القدم باستبعاد أحد أفضل لاعبي الولايات المتحدة.</div>
<div class="tg-footer">👁️ 6.64K · <a href="https://t.me/naya_foriraq/81225" target="_blank">📅 17:51 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81224">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">ترامب بعد هزيمته: أفضل الوصول إلى اتفاق لأنني لا أريد الإضرار بـ91 مليون إنسان  مو جنت تهدد بـ"محو ايران وحضارتها"
😄</div>
<div class="tg-footer">👁️ 6.24K · <a href="https://t.me/naya_foriraq/81224" target="_blank">📅 17:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81223">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يمتد خط سير مراسم تشييع السيد الشهيد آية الله العظمى علي الخامنئي (قدس سره) في كربلاء المقدسة لمسافة (5.8) كيلومتر.</div>
<div class="tg-footer">👁️ 6.14K · <a href="https://t.me/naya_foriraq/81223" target="_blank">📅 17:48 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81222">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: يبلغ طول خط سير تشييع السيد الشهيد الخامنئي في النجف الأشرف 6 كيلومترات</div>
<div class="tg-footer">👁️ 6.03K · <a href="https://t.me/naya_foriraq/81222" target="_blank">📅 17:47 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81221">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: اكثر من 600 اعلامي عربي واجنبي سيشارك تغطية مراسم التشييع</div>
<div class="tg-footer">👁️ 5.97K · <a href="https://t.me/naya_foriraq/81221" target="_blank">📅 17:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81220">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 6.02K · <a href="https://t.me/naya_foriraq/81220" target="_blank">📅 17:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81219">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">اللجنة العراقية المنظمة لتشييع قائد الثورة الشهيد: الدرونات ممنوعة وسيتم التشويش عليها</div>
<div class="tg-footer">👁️ 5.98K · <a href="https://t.me/naya_foriraq/81219" target="_blank">📅 17:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81218">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 6.13K · <a href="https://t.me/naya_foriraq/81218" target="_blank">📅 17:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81217">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">ترامب: أنا لست مهتمًا بتغيير النظام في ايران</div>
<div class="tg-footer">👁️ 6.07K · <a href="https://t.me/naya_foriraq/81217" target="_blank">📅 17:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81216">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e64db71377.mp4?token=F7U7taMNzpNQ7p26fnhOqVfBhOzWvxm_pJhUPG_oQsYA80S_pDOTO29qJ32IQjSy3xliZk75XTHwITUnv_dvodrEgLOHeSfr1NvvZcdULsHsgPo6KJ0pW1hlR7aVxV6YCZm6MCbO68YZhI_P2vJG1UyKE8Xs3t_IFBi6CjCRnm0aTVJV-joAEYGf0I8KIjlIZOCFAxbSpBUmY6Rq1tpigJfHqm1m_o2OZIjEwunux78dNZ8EFo5DY1SWQHYVMUih2BAV9EKCWz5QiuMk8b7u4TZoozk7FrtekDwXyViV51xnmKrQ0ZqFfaZ59VkOIZrvEPDu_-_eq7caID-9IJ79Pw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
الرئيس بوتين يريد إنهاء الحرب الآن، نقترب من النهاية أكثر مما يدرك الناس</div>
<div class="tg-footer">👁️ 6.4K · <a href="https://t.me/naya_foriraq/81216" target="_blank">📅 17:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81215">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🏴‍☠️
نتن ياهو:
إضعاف إيران يفتح الباب أمام اتفاقيات سلام جديدة على غرار اتفاقيات أبراهام.</div>
<div class="tg-footer">👁️ 6.95K · <a href="https://t.me/naya_foriraq/81215" target="_blank">📅 17:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81214">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">#ترفيهي
🌟
‏ترامب يقول الامريكيين "اخرجوا واشتروا اجهزة ديل" بسبب تبرع شركة ديل بمبالغ لحسابه الخاص.
ابو جنة فرع واشنطن</div>
<div class="tg-footer">👁️ 7.49K · <a href="https://t.me/naya_foriraq/81214" target="_blank">📅 17:08 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81213">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=IWd3juHynuIdk6GPTGTT-aTuMmq4XFa9d0R50xwkpz4AiRfVDjPHzafQbhTC2bR4OhVCTl8OMwsCjnfflBCprvrnY6WfAMZxovTsOLuqakb8pX6HL7ZuHt0wduoS2VUIQJQO3zcz6RN-vx-SiyXdWu_Erj2grVtlseL3DmzPKDJ2qtYfHCXU2tfsBpWvrdLtdeorkS8Cipvqlby1m1Cw69GiTMLD5aZgoftESkz9iSpwKkrpHPsH7ZYaxacZPWmScpFIWnQLTeP2d2Q-e-zVlnr0STD3LTkRFrZtQSsmui3zC4KCpOqwsquifO7KSE8mH2n0JsFdLcWHRTmlijdYNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18f395cb56.mp4?token=IWd3juHynuIdk6GPTGTT-aTuMmq4XFa9d0R50xwkpz4AiRfVDjPHzafQbhTC2bR4OhVCTl8OMwsCjnfflBCprvrnY6WfAMZxovTsOLuqakb8pX6HL7ZuHt0wduoS2VUIQJQO3zcz6RN-vx-SiyXdWu_Erj2grVtlseL3DmzPKDJ2qtYfHCXU2tfsBpWvrdLtdeorkS8Cipvqlby1m1Cw69GiTMLD5aZgoftESkz9iSpwKkrpHPsH7ZYaxacZPWmScpFIWnQLTeP2d2Q-e-zVlnr0STD3LTkRFrZtQSsmui3zC4KCpOqwsquifO7KSE8mH2n0JsFdLcWHRTmlijdYNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
عصابات الجولاني تقوم بقتل شاب عبر بث مباشر بحجة "الغيرة على العرض" ويلاحظ في نهاية الفيديو سبهم للذات الالهية بعد تنفيذهم عملية القتل.</div>
<div class="tg-footer">👁️ 8.02K · <a href="https://t.me/naya_foriraq/81213" target="_blank">📅 17:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81212">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fZzKTE3_aTZz4KT9kis9sRwAbH4KIqz37G2dd4ya4vSWeJCRiRG0i7P0dlKZytcUqJnfxHOxHkMTxJAgvLKj3OTjwVIzw-sExYzX2SeiNPNvBlPwZeERkb-h27eHQv3ZOHvgGNaw1ilfrNpFLb1cRdutPk2zauf2LX2x3eh-m8X86ye1ANzbye1JzUrmQZYengfNqZOWKat59cndILauV4xqWaPlOET0SkeS000ZgZk1oI4f3RsBzhXkfy-eX7ot5_9-QFVLIUUdQJQgVrZyjGm_QrDuAKdwUFFXescVfdg6zj0Lj9ua1SF9wS03DSZqsO_1Z0vEN1hepia7BEAn8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">البيت الابيض يقر ان الغاء البطاقة الحمراء من اللاعب الامريكي جاءت بسبب ضغوط من ترامب على الفيفا !
لا يابة السياسة مالها علاقة بالرياضة</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/naya_foriraq/81212" target="_blank">📅 16:43 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81211">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">محافظة ديالى توجه بتعطيل الدوام الرسمي ليومي الأربعاء والخميس المقبلين للمشاركة في تشييع جثمان قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 8.44K · <a href="https://t.me/naya_foriraq/81211" target="_blank">📅 16:34 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81210">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">سماع دوي انفجارات في أمستردام</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/naya_foriraq/81210" target="_blank">📅 16:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81208">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dfqs1UCGZ6VvVhuGUx7ga8TfzxXUQy5dlgzE8rGZKI3rwH6j4lPoOFzZbUsfnp-VNOyWn7b9md6dykuMoRmhGqg_a54mgp-vghGKy-YUJgNd3NEv0RjOxzvMIPYadeCdwug1k1llAaTNO2rB_QTQ9rmrNIIIbnXvtASgcy0mj8Fsg2OvEqXzoORDo7XK6e-NFgkIDpju1guLYcdlKiKdKolJwvTcsdClHZDmza2bbu8C3JeDtcJbjrLB3Ki7Dy9TjxUmefgvTCnt5skMBZ90mnh5yEHuptRkMC1fCpKJ42xoXUFOjNufuPi-nPC17RSNIg0nDW86Rri7w7Y5Vp9YAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تعرضت مجموعة الضربات الحاملة البريطانية مرارًا وتكرارًا لتحليقات طائرة الدورية على البحر الروسية Tu-142M3 أثناء عملياتها في بحر النرويج كجزء من عملية FIRECREST
✈️
.
تم إطلاق طائرتي مقاتلتين من طراز F-35B من حاملة الطائرات R09 Prince of Wales لاعتراض الطائرة الروسية ومرافقتها حتى مغادرتها للمنطقة . ووفقًا لوزارة الدفاع البريطانية، كانت الطائرة تحلق على مسافة قريبة جدًا من الحاملة، وألقت عددًا من العوامات الصوتية في المنطقة ولم تستجب للإشارات الأمنية الدولية
📡
⚠️
.</div>
<div class="tg-footer">👁️ 9.92K · <a href="https://t.me/naya_foriraq/81208" target="_blank">📅 15:50 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81207">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">اجتماع أمني وخدمي رفيع المستوى في النجف الاشرف لوضع اللمسات الأخيرة على ترتيبات تشييع جثمان الشهيد الخامنئي
بتوجيه من السيد نائب قائد العمليات المشتركة الفريق أول الركن الدكتور قيس المحمداوي عقد في محافظة النجف الأشرف اجتماع مشترك ضم رئيس خلية الإعلام الأمني الفريق الدكتور سعد معن وقائد شرطة محافظة النجف الأشرف ومدير عام الإعلام في هيئة الحشد الشعبي ومدير قسم شؤون عشائر النجف ومدير قسم الشعائر والزيارات المليونية في ديوان محافظة النجف لبحث آخر الاستعدادات والترتيبات الخاصة بمراسم تشييع السيد المرشد الأعلى السابق في الجمهورية الإسلامية الإيرانية اية الله العظمى الشهيد علي الحسيني الخامنئي ( قدس الله نفسه)
وناقش المجتمعون الجوانب الأمنية والإعلامية والتنظيمية وآليات التنسيق بين الجهات المعنية بما يضمن انسيابية مراسم التشييع وإظهارها بصورة تليق بمكانة الحدث وبما يعكس الصورة الحضارية للعراق وأهله
وأكد المجتمعون ضرورة الالتزام بالتوجيهات الصادرة والتي شددت على أن تكون جميع المظاهر والسلوكيات معبرة عن القيم الإنسانية والوطنية وأن يتم التعبير عن مشاعر الحزن والوفاء بأساليب حضارية وسلمية تليق بالعراق وفقيد الأمة الإسلامية
كما جرى التأكيد على منع حمل السلاح بمختلف أنواعه خلال مراسم التشييع وعدم استغلال المناسبة لأي أغراض والابتعاد عن الشعارات أو المظاهر التي قد تخرج المناسبة عن أهدافها الإنسانية والدينية مع الالتزام الكامل بالقوانين والتعليمات النافذة.
وشدد الاجتماع على أهمية تكامل الأدوار بين الأجهزة الأمنية والدوائر الخدمية والإعلامية والعشائرية بما يسهم في توفير الأجواء المناسبة لإنجاح مراسم التشييع والحفاظ على الأمن والنظام العام وإظهار الصورة المشرقة للعراق في إدارة المناسبات الكبرى بروح المسؤولية والانضباط.</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/81207" target="_blank">📅 15:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81206">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TI5z4QxSYstvDV0zFPOlC6kmCsdysLiTJKbqh56ZDe4JhzyEUqkUs0NK9d_2cka4oGTgyUBfiuc6U8j3pM35QpK5H3y7Xt4F4jti1BBJt92hxzOpqWtRlp5KipmrCiJfv-xAzHa9TghtHKhZwg1PqWRrhY0pxWAnmj9FHbOVHh2k_UKUzz-uyh7OCZnmoaqXkfI1QlwRmuWOIuV7_EjzDEkvVKDx3ZW7g6RYcdhpR4keIEAwtj3muFkKNZZyff0aG23NJTN3Py_m4qND48I09fCXm_VhvlPUpK5BOTJnmeJWqs9Sk8sovJGqwVv7bCERvHqSDvBYix9lIkY-NVK0Mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
وزارة الداخلية العراقية:
وكالة الاستخبارات والتحقيقات الاتحادية في محافظة صلاح الدين تطيح بأحد المتهمين بشبكة الفساد التابعة للمتهم (عدنان الجميلي) كما تضبط أكثر من ثلاثة ملايين دولار امريكي وأكثر من سبعمائة وخمسون مليون دينار عراقي، كما ضبطت مجموعة من الأسلحة الخفيفة والعجلات الحديثة وعقود حكومية داخل داره</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/81206" target="_blank">📅 15:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81205">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🌟
‏
الرئيس اللبناني:
بقاء الاحتلال الإسرائيلي يقوّض شرعية الدولة اللبنانية، على الإدارة الأميركية الضغط من أجل تحقيق الانسحاب الإسرائيلي.</div>
<div class="tg-footer">👁️ 8.95K · <a href="https://t.me/naya_foriraq/81205" target="_blank">📅 15:16 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81204">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇷🇺
مصادر روسية:
اغلب الهجمات التي تعرضت لها روسيا مؤخرا بتخطيط وتنفيذ وتسليح مباشر من بريطانيا بالتعاون مع النظام في كييف</div>
<div class="tg-footer">👁️ 8.93K · <a href="https://t.me/naya_foriraq/81204" target="_blank">📅 15:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81200">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/E8mqQCS5zirD1tm3RS613WVs5uc3ktrIEd1ZLfr0mD4D7ssChWhpgg8NCzo57N0uN_q86fpI30JPbSTE_IZeshDM5aA7F1-N7tqLhMGxZDoj98_sB67NLnb9LSsq4AeeM3buAH5R5SJ9MVuBj-4EFMZgIv6DhmvCGH9sGoNPIwSLpmcVdCduNyBQqFe3UloL4x7d1Y1_MJp-ppxmdalckmF6IqHR932RRd2Rgkzu5s1MU0EnHkcBZh0jhADY0VqawoQ6o7Pv2uLCWrdfTflD0lJcsXIJL9uCXzpGm7vR_ofnCL7hwM2tE0BOHMk8XhmpzqyjdDWEx7EXCqTfAQXuKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/j5yYKerlN9b6zvA6Cc26w4oabBnrg7yjSAVDmPEQR5YlznWNj1yZdfl40ivM0Ll8J6gdUdppeDZx_qrHg1GT3NZUgQbNAmG6Bkg1SufsXtkznIOwLf373k341DoZtNNsYjawVra1tRtfzLP26wyuN5nY1PfxVlhfE-ktBktDKzmNLPRn6AbEh0qiQ3ZCmJQm4T9XSrHOWcjgEjRCftbEN8SFe2xAXG3T6LMw91OEy_4fxqP7zML1ZJQ11efwzj_WRk9os8yTSUBON6HFXDnLBGCC71AbVTStt2iPCSalpuifvuOayXx0XFMr-kt608qdiHzhfH_wjmXtF63lslAlSA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BzLHiRoHxNQeQS6_mmOa9vkiRS5Q4lWd_a8-O9h3uEWMiaVoPg_mnD8ISAlvvtQMd1_RpE_ddrMAvDBcHUQunwndyyeHkbesI1yohYqEK_PJz29iJUakXAcsjN__gfOQAaGPJ6amrP7a89qeSr5pPv9MFZ7tYetS55AJe37FIxqPqXMaPRoP4TJOc_PAs2J0m4wUYv0X1VmjnRxuv2oGaB-m8Bjf-S9rkzEitjY-9O_TNBmtew-16Cujk9PrNpVpbB5HFKnV8OKYm9ALaj2dkuuLCrHfk8SsBGZZCkBJ6hbU3WSmAI4Zlaisr1CunTS-FhWm1Gfk2g_aIF37gknV8A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/poHGn_VqFulyQnmzdP22I8RtW_Jitk-7Bun9DxQmvuTSSiCv1dOZwxtluKLpzMyUTwVVZ1pzchxK9QeTEWNlYQb1uIHWxtXcSrkNAR61DePXAccnMl_lB8ry0ZtiIfhmytXRd8ljXSV2Yd97-6W5KewMqeHyS1WIoaK10AltG9udhD_P1uej77UxCBVrh2mF7Zi_OTPowt3U4WmqHdNAiqNFta7yaHzRz00YKeJ7vjnZ259AZswE8FWvKkVMG5O1eIXbN3sKfERBjwHzYnU2GFl5Fc7fL133ItihzVcVYYbr0DW7FxswhuNLRugEHHuBdx8gcef8oRcLwdhm1Sa60A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">جثمان قائد الثورة الشهيد يواصل طوافه في شوارع العاصمة طهران وسط الحشود المليونية</div>
<div class="tg-footer">👁️ 9.19K · <a href="https://t.me/naya_foriraq/81200" target="_blank">📅 15:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81199">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني: سيشارك الرئيس الإيراني بزشکیان، ورئيس البرلمان قالیباف، وأحد أبناء قائد الثورة الشهيد في مراسم تشييع جثمان الإمام الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 8.98K · <a href="https://t.me/naya_foriraq/81199" target="_blank">📅 15:01 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81198">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d673daa6.mp4?token=LzCjzFMd2tK7Kfx79_ixzN8VsoA6pHYmbYrQ-QlEkvR2u1AS75BaNiMBwVjSkTJ3dYbCn-Fz3AOguGZoHNHDkLZ2s-YXeV9JecKMrjR1wu2Zc2MSk6EJgGHZtfeBb2qlD4l6McvRVvM8Sgmi47_7F1FenckOsSzfbQZau4OjZEVFIwPUmzEpmUnwIIbsDII-Iog8Hf6KbNZe6hzh-s2Bu4UyPvhY_idX7gERtlyGd4D1KGGx0isfrf9LLN8Iact6rIAUfQKLwhqo6a6mR-HNr_WB1ksxwbxFzplIUboQiwNFdJfeinksBB6gMjOTG1uZrHl1W86AGEAcBjuSGc6Y41ToAU3rYW4pjoY-3cfwqIVxyAYKpSGQcAn1Da4T6c0FBltvs1bnFCmRGVHsUKP9XWg4fGY5ACutzshKv1LjjfXMsOjfUtoJTucavgSSmW4oADceucSefSmrNSzpv7in4AF3ufhxzDchOy-YazvogfmcgX4y6pwIvnFXE3VYTtTV4q4Fi6QiNBWkZ6dDToeIlhCizKMM9R1loj3wDpaMRX7yE9t2a3LVQjjbxhzAS6dZuCRY-x6y1zURVJjiyeQ6N4Vy8rRPIunUMTJu_RIcoeiDKJUmDaU1nQfPs1H67uo0WUxMknXGc7aKQb6mgZQRkpzd6uzM_iPU1_YDNlStVCA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d673daa6.mp4?token=LzCjzFMd2tK7Kfx79_ixzN8VsoA6pHYmbYrQ-QlEkvR2u1AS75BaNiMBwVjSkTJ3dYbCn-Fz3AOguGZoHNHDkLZ2s-YXeV9JecKMrjR1wu2Zc2MSk6EJgGHZtfeBb2qlD4l6McvRVvM8Sgmi47_7F1FenckOsSzfbQZau4OjZEVFIwPUmzEpmUnwIIbsDII-Iog8Hf6KbNZe6hzh-s2Bu4UyPvhY_idX7gERtlyGd4D1KGGx0isfrf9LLN8Iact6rIAUfQKLwhqo6a6mR-HNr_WB1ksxwbxFzplIUboQiwNFdJfeinksBB6gMjOTG1uZrHl1W86AGEAcBjuSGc6Y41ToAU3rYW4pjoY-3cfwqIVxyAYKpSGQcAn1Da4T6c0FBltvs1bnFCmRGVHsUKP9XWg4fGY5ACutzshKv1LjjfXMsOjfUtoJTucavgSSmW4oADceucSefSmrNSzpv7in4AF3ufhxzDchOy-YazvogfmcgX4y6pwIvnFXE3VYTtTV4q4Fi6QiNBWkZ6dDToeIlhCizKMM9R1loj3wDpaMRX7yE9t2a3LVQjjbxhzAS6dZuCRY-x6y1zURVJjiyeQ6N4Vy8rRPIunUMTJu_RIcoeiDKJUmDaU1nQfPs1H67uo0WUxMknXGc7aKQb6mgZQRkpzd6uzM_iPU1_YDNlStVCA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">والقلوب تستحضر ما تركه من أثر
#قوموا_لله
🏴
#باید_برخاست</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/81198" target="_blank">📅 14:45 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81197">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/snVdbYDCtl1DgI7c90dS2Y-Xj8n0mDl24oVD_Exu1j8vf_3uT0k7HR6MLmDdQ-an1Hz0SfhVMaBF89A5-jyPeRvHo6nzJUqpBweKPb4zftnBTDSZi9v3B_tvshhG8u7dppBp0XOTcoiJyokQYaCLSH0_VXPXTellX9r57Z1BiSPqU5q0NEaQMja4VftM8zv6vOUIxH9V0dqwrmEVJNqAJ2HwVzwoUlykS4ZTb6TFw1pPNz7m2E8EItX5WhdU78OwV-qqGZkeOn6TvfBX58A0UZj5dW_BTt9Tn9-E9yhoavXjCjeHTkk02guhk-CJRWj1kIx9zgmwOVpjkBszhxIRIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المديرية العامة لتربية محافظة النجف الاشرف توجه ادارات المدارس في المحافظة كافة للمشاركة في تشييع قائد الثورة الشهيد</div>
<div class="tg-footer">👁️ 9.03K · <a href="https://t.me/naya_foriraq/81197" target="_blank">📅 14:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81196">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇧🇬
عشرات المؤسسات الحكومية في بلغاريا تتلقى بلاغات عن تهديدات بوجود قنابل</div>
<div class="tg-footer">👁️ 8.82K · <a href="https://t.me/naya_foriraq/81196" target="_blank">📅 14:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81195">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">الاتحاد الاوروبي يهاجم ترامب:
القرارات بشأن ‏القواعد الرياضية والشؤون الرياضية هي ملك ‏للهيئات الرياضية وليس السياسيون!</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81195" target="_blank">📅 14:05 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81193">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/s41k40y3Uxk8qSPrGX3UehJICq6ASIe-ukxd-BWRq9AeP41wO6Ocgs5gsya-KDmubpK4HDT6jDjNwtJZLx9N6Pg4Qdvb1eKi8VTuHb8JHK27ZT89bDHIZymqmh_t-fG492utYq5RDo5UeQEER_4O-NOG-YNteEFv5x4WHI-ScDD-cbdFDlu3hpmqnHZnLyzHMm4w4Sc3s8XmMFEVYHYHiV69HIDb2Zwq1uwrIj_57SMT2ATAps_CW4C9ltP9bmmS3UHePTqpTHMqv0DO7JePCVkyQ9_DfcwiUZCaFbt2Utngt1ok1b_lBDmwGr3_sxi3v-yxJbkfstXUvv_Ejy4Htw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/MCgHYJsFI_-IR9pwWx0xcE8ocdQE3BxPgwr-zz2NS5zFC7QrLwsXB-tKspAVy4YfTFb_eDBy5BjvruR-PqXjHiXTFNNLHFzePiRfHGMYXhe-zgvDRm08ZPMYYq7FfPEykRGZC3lc0q4a-kNhbCHW98lBBPNpViOgHe3Cjw5TKGPU17vg-WrvZ2rLdfCypSk95tm3AY4tJvZE-Zr6p2j_3GUpkoRBUC-kfbYCGseEpLj6PPueUBV_fW-2K5HC8smPqOAXq7d7cfaSdIBgwVm89t0ICRegFTaanAr4QcAfaFbrsKic1nrS5tj3fk7x-H3vi0Fh5YEsr8UaZUDfGICJTg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">عباس عراقجي يشارك في مراسم التشييع</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81193" target="_blank">📅 13:38 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81192">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6fabc1873.mp4?token=MlZUPsziGhQJj2XxuqWMhuNBlNxsEeMWTI_XPG6VYHFNK5dg1JPdy574Nh14pIPQL3vvgJ3ANogjLsxyFqDV_MOO1BRa6mJdFlA2oARixCauUSTl_vvMfZ5ClaoUv34bsEp4-sgRarGOGZnYkHC08oy05XeEHTefCv0-WHjmID8aUdCIuEF11xIG-Eu7FP26m5TWGLkNqoNdnhg2fc-fdTiPViO26SuVyjGkvm2U2-yjrCUNunjKYXCqF3NaPW2Z-ckkLqX-IHfvLbpU0kG8RX9gX1pLlLVK70d_RUk3RbVbSPoWr7u1jTM6qnMZWWdlO45aQdOJTO--QwtN5QT0AQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6fabc1873.mp4?token=MlZUPsziGhQJj2XxuqWMhuNBlNxsEeMWTI_XPG6VYHFNK5dg1JPdy574Nh14pIPQL3vvgJ3ANogjLsxyFqDV_MOO1BRa6mJdFlA2oARixCauUSTl_vvMfZ5ClaoUv34bsEp4-sgRarGOGZnYkHC08oy05XeEHTefCv0-WHjmID8aUdCIuEF11xIG-Eu7FP26m5TWGLkNqoNdnhg2fc-fdTiPViO26SuVyjGkvm2U2-yjrCUNunjKYXCqF3NaPW2Z-ckkLqX-IHfvLbpU0kG8RX9gX1pLlLVK70d_RUk3RbVbSPoWr7u1jTM6qnMZWWdlO45aQdOJTO--QwtN5QT0AQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
المشيعون في طهران يرفعون صور مجموعة من مجرمي جزيرة أبستين ويتوعدونهم بالثأر القريب.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81192" target="_blank">📅 13:17 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81188">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PasUp6M3RFXJHo9BWdZIeWRShQqF16uMHQ2eia_5-UPAZ3NSWou9Hg5vSFcf9UJXFEnGtWnnpxuwscKEwoi2bxnR4A5bsHbAom2_DeRYZhhU-Lt6HOJoHlWVkJwItTfZQ1xgZ1ewDkh0IHC6DQosFqHNXM7ndDSnUQF94D9oUwBJqZUQ_U9WTLzWW_rvJKbGXpS0MP27GKbOY3El-fKYAOkziQsN1I3Z0Td3ITp4H_DGaaqoLefv4Bxi-gYPg8gzwG0680ICn7dAoEKAyzi_zAiacvl7jvsddd1qGPH5JDrf8rqwqbwnvyaa6NhPGMIAmSB4CJDJ0sG9AFPTrQ7dhA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/hmW2KTofHY46mHgC3p2nOPxI95sFC_MsV1zWibJtNyuJst7L-9kIG7BILSj5M6VtmNfdCRRKn-DzuWefWcSm9XEOekFytuAENoacPMtOAs-3nTERwjaAZaNzlwMDfss7FJQBmnBwgY1WMlV6kpl848JiimwJeMg3nW_-sqEe7pd39SzU395qYmYYUx0FfoFXfdEgQKC5CLB7TfQezYxbfsnRpxHlVCM92q0aabEpaMHl9W6wI-5djp8hpNAafCu8mBIXlotKI8hcUoQmr8UdXUgcnvLmSAYazW9Ne8yuE3FXHTQnGCKB7h5YLCkIvHRMAWMI6QM_NjX5MwjWd3ntkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/l07wFb2eFHho00ssaISCpZk3zETDsf1gO56LphlVC7yJhuWKi6ddCDiwZhGZCuUcyPOy5YNX30rcIa7t1G9DGhcwnwS-e7BAv96MO7PlSntA-KJAwv4rOWXveiHNbGfZzR0yr_UGWcPCgHoEOexNQiz533xpcw2U6JPor29hyIt6XQQkHVOEQq5DZyUKV_U-Xtpejyd1CaVJx1sy4RHcxUS597suniXohtCbS_M1b6YfbqM_yxDdIJy1RA3gY7QzZRJmlSbsNtlOG_R10oBimpGKV-R6enOYC5tkaJOmNQjdYES8Rh9sAZntfzbd226GIHmKjGauuePjrCpWFyI2Ag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/BSHE0sHesieBkaXp6FlNgjjoNYdOD-N2KinPJHqbCE4nwg4HTVWK_uQJBxA50F1BuRpuEhXvTpn2Octk9NImFtwGPvy1GRZURg4nW687lxUlvtycTzyRG3luXtOhK9S7etuwtAXTmPqJbBTHWuuHjiiHANSmlZK_4tJEtBw_OtbdXztHI8iFoMMRfZ8EfeXpBVpaa6W1F9BLdh4zrEwQ_h9UUcLV9UDQ7_T99ejd6Z16cZ6FVnMMs9Tyw13vLA0FAnM3xWM2Jstw12MGHKLc3O3vFWaCO3faMdki407AciGRKolA14nxogpeS2JHWp8rmcK9LmGQ4unvABPSkQEAYA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
🇹🇷
مشيعون من تركيا يشاركون في مراسيم تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.85K · <a href="https://t.me/naya_foriraq/81188" target="_blank">📅 13:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81187">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🇮🇷
🇹🇷
مشيعون من تركيا يشاركون في مراسيم تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/naya_foriraq/81187" target="_blank">📅 12:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81186">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YfHpGTtW8WCgu6Enkvvqnz51Kzx0N8KTWDBMnrj6QBJkBlQVtogAk7iXb9FBHbBCXhrRefMj8flroozTkc1MuEjl08es2VtNpwNM1MtnTS-HAmxEgKCN5cmQ1T5wbJxumQXHuNXlvIwSzIj4-nNAm2Oa-M9VJbTI5aFxp0PIEOe6tPHWVMkO6kyD91R70WTLz7JVdvpyUOOuFT0EEXI8xrit3hSduaTsI-g3cFSobYMgEDO6QfWRMGlS-9IhqR4j6Jt2_z_7vOYmoFAHAxLMbhP3lJyRQiYwo6YvgaqeZKA-eOwBl3psrJ-DyZ3WQHMdac4Rs_4hnx-Rq_0Aa5RxgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
🌟
غارات صهيونية على النبطية الفوقا بجنوب لبنان؛ ارتقاء 3 شهداء كحصيلة أولية.</div>
<div class="tg-footer">👁️ 9.46K · <a href="https://t.me/naya_foriraq/81186" target="_blank">📅 12:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81185">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
🇮🇶
مصدر إيراني:
سيشارك الرئيس الإيراني بزشکیان، ورئيس البرلمان قالیباف، وأحد أبناء قائد الثورة الشهيد في مراسم تشييع جثمان الإمام الخامنئي في العراق.</div>
<div class="tg-footer">👁️ 9.97K · <a href="https://t.me/naya_foriraq/81185" target="_blank">📅 12:42 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81184">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U5zce1ZeMKKiE5qHBKWCGRMP3aVs6PpMQDckk6da_gk6H0nztoiVVmlOCpmQxaDC6jbZVIHbvKuV3PeviUEQBDQ5PKgMigTBI7RKcZC7V3gx4NKIPl1nEgN1GmpTNtZeRvJQOHpVR3TiW7JC-xseSjtO_6ZY6v2CuQhCcZzsLXL40CScOlYW0s6ZrE_E7Qmcb-kSLKifHjvcarBl5fEUFP1e38m8pmaKuUcPOi7000mtufdkhM4wgGk4BnRh14oIRFnJRZaj3e0-ysaGterM-lgk8irQUqyiAXZfkKdCpDR8o8ASgeaf_5fU3MPOw6IIu91Rv4e_b1Mr9E2XRmJSWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
المشيعون في طهران يرفعون صور مجموعة من مجرمي جزيرة أبستين ويتوعدونهم بالثأر القريب.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81184" target="_blank">📅 12:40 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81180">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/S1PWv0iUBqtY7zfpFk_H4pwwSQo8ZWRjfJ9yg128EFZ2hL3gItgb8yn99xYdXE08-EQW1JXDC54fRHvMGQQhQprTI66VAh1bQc6q2vljFh_mN2QM6n1pnqEChL1ugNWfX86GzBQ-NqXJSXXB3E9HDVjrX2RJMTE-8Qdh10z_5X47V1W9dp19nMG1gEGsq86OdTxMbke4ggo3ErI8WoftDVx7k5A8mGM9ifqHCwjNUiJO2gr-K0WR0E9D_DqVSiuh2IRLvv1X7BszRI1wnfu2HPHVHIouTycmrad_t3MFizXA3F8ogvfeDh8ZBL-Ss9sHoAbUVYxGd4vEmVTd2M6ZZw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/HldkRaODC8BbQkdsHLsthoKQ7OGSCRnxXlbHVxjVlmf_kKlDQzL5XpacthOuOtVSL8aeu-cnWmro1T4DOtP3LjVGtf6S5u0w1NyyS1_GaGVJwu0OgSv_i8GO16vGc9pI-dIFfDN2s8vAw9_-8uXxIbODEMiluukgkrASBu4NJoQkQY72Y--LikJ_hzakCWZHRiS3S1shj2kYFMU2XzQqGXUKfPe9aKdvOVYJzTmHsn8hXOWz5ksk-AuFG03pwsoEGfywo3szpceBMPiZ-09ex33XJobBQqNfLMpM67Y-fvA80CQ-2ucEpad67yC9gNUOUM-DLme0xiEdfvhasy8d_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Ggja7puZwN3R0_8AIO-rzJmYBOwVoA1dMfEwBLDJvalQAegAXAZzZX6OFJUnCuxB9qQ9sGHhitkKQ7VehXuLVv19SkqKmRWNWvfd-ik8CfiZ3jCWmGi4HNep_x0qRimmB3NL5fH8gMPWX3XAjPQHyPI27sQvvuwC8wghTigGuu0a8xZLJ3meYtbDkkB9irddTMneX5RR8__aeruBBJevP7BjsaQkkMisqrMhQxr1Hlw7uHaoPHr1Ceh4ae4dpY934TfZ7_C-TDey4kyRSxdCJfEf_fDtWUKEItyqtt2z9cxmrEoVzlsSiElFqmk-6V-Bk2qWPnSA58nuT5gV18q_jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LnLDDv8omAu5Mp_WpfPnkM-Ugx4MlRk7rPqqgR-TR7VYu-50QrO_A94soJYxiqmtLlHzb2zLW3nb06my44i8p3qlmsRwdxfVEFio_p6hZZ_ccrM-YtvRp8Mi6-n7H7gdwm4FPfPSuyOy_Cz3QBqmCRaYDZ1zh7zjzuodxX692WDnoK3VVq2ZBIiyzOskSXRtAUizWmQIv7Tw_rVPbJ9BPAwywYUpS4xuOfE4O_qORRmz4HaDRn-ijfSytNOIknGbSYOtDfl6Sx9aa2GU9hNqAvYVQiViku1pBeGoUVkYbQ_kDcXKd4aStaMVIS1nrd76VlZ4vdoph61PT_AP8TRI_g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
بلند شو عملدار.. علم رو بلند کن بازم پرچم این حرم رو بلند کن.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81180" target="_blank">📅 12:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81179">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e19d2d9f50.mp4?token=aOxDhwp4O7YWJJ-ZhgJ8q6RWrcpxMqxD8y3YBNhDSBUDTQ87RumT1XwkVjPEXCSZOId_dsxMDnBTh51l7DwKeORizduYpi5Mf0f2XoGxOZG04StgU8IzgxHzZIBVFAZ3azbtaqKlAAaOxAmFH9B80DWtLoLqEIiqAwHGMqMi7EPhjJzP6AqP1ugfw3VXOv5E7cBuUc6tFqWyNn_8AmX67He1c9mjZr9E2_9AdfaJSk_QyHqvuqmBq-fknfCw7KM2fXFw8JKfrtygF4jJPnVSSAS8LAxFHAQ6wYJsHg4P6paIApsgUlzFzFvl0hTPOsbS0UepZfAaTbPs9mrvW16hNyGqAI7egeavvm0Q3fg3psQhR7xnFl7pI-H4J5Yj85KXcIOF_U0FR5iwOHr_xNHXV3tyG6Y8zdmfPkt6JmHCjc0hvlvpm-IbgSDuj210bK48qjffwK4c59SFxOB8CjDFYahu49jLhujEEayJrXBCOuleESa-jAr4Tj_EalKhapFWuG6lkoH2FtUHVTkfrHAeL1suI8HkcLl1osykUwM59JXY_nKEyJumFEfNUmC7PJey8HWK2JaQ44cW55RALXw4rvQjIqCbfz5tBhVmLFZFr3BawIyb-3-vCeNlbCLsqRAjQ2CqMvKZ_zsidFBznCi5Ea9FqdXz5n3psY1YGgooaaE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e19d2d9f50.mp4?token=aOxDhwp4O7YWJJ-ZhgJ8q6RWrcpxMqxD8y3YBNhDSBUDTQ87RumT1XwkVjPEXCSZOId_dsxMDnBTh51l7DwKeORizduYpi5Mf0f2XoGxOZG04StgU8IzgxHzZIBVFAZ3azbtaqKlAAaOxAmFH9B80DWtLoLqEIiqAwHGMqMi7EPhjJzP6AqP1ugfw3VXOv5E7cBuUc6tFqWyNn_8AmX67He1c9mjZr9E2_9AdfaJSk_QyHqvuqmBq-fknfCw7KM2fXFw8JKfrtygF4jJPnVSSAS8LAxFHAQ6wYJsHg4P6paIApsgUlzFzFvl0hTPOsbS0UepZfAaTbPs9mrvW16hNyGqAI7egeavvm0Q3fg3psQhR7xnFl7pI-H4J5Yj85KXcIOF_U0FR5iwOHr_xNHXV3tyG6Y8zdmfPkt6JmHCjc0hvlvpm-IbgSDuj210bK48qjffwK4c59SFxOB8CjDFYahu49jLhujEEayJrXBCOuleESa-jAr4Tj_EalKhapFWuG6lkoH2FtUHVTkfrHAeL1suI8HkcLl1osykUwM59JXY_nKEyJumFEfNUmC7PJey8HWK2JaQ44cW55RALXw4rvQjIqCbfz5tBhVmLFZFr3BawIyb-3-vCeNlbCLsqRAjQ2CqMvKZ_zsidFBznCi5Ea9FqdXz5n3psY1YGgooaaE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بلند شو عملدار..
علم رو بلند کن بازم پرچم این حرم رو بلند کن.</div>
<div class="tg-footer">👁️ 9.6K · <a href="https://t.me/naya_foriraq/81179" target="_blank">📅 12:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81178">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/56ba224243.mp4?token=BGTMwH2Ago9wa6QZ605WDiBJTx-NAQLPd0vHmgvPp6_c3OGmk-QyIrBp6GgFqtbTaFZVZ-jydG3j_nJ1DmJnQWiP6K0SUlzkpk8T41jNC7uEnpW2AIsi74BW6nJOWSKQsIWqPATGf4SJ1knELYDtzMQ4UggJ_ibMmziLY5Ib8LbS3-ZMza1vKyOCAcp8anguwQfCr-oFrPm4_m0uM-cnbDjnC5lehzsEjyG9iU1RV1f2lODnKGZCM3_hRjfgv74zKLiCuME0hZykCCOLuEUbBSXfyw3_TtxE-n9_yMzVrSWFuKHgyZNp3wt8h81J47wzkLwJHzJCZjixeXRkSYSxdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/56ba224243.mp4?token=BGTMwH2Ago9wa6QZ605WDiBJTx-NAQLPd0vHmgvPp6_c3OGmk-QyIrBp6GgFqtbTaFZVZ-jydG3j_nJ1DmJnQWiP6K0SUlzkpk8T41jNC7uEnpW2AIsi74BW6nJOWSKQsIWqPATGf4SJ1knELYDtzMQ4UggJ_ibMmziLY5Ib8LbS3-ZMza1vKyOCAcp8anguwQfCr-oFrPm4_m0uM-cnbDjnC5lehzsEjyG9iU1RV1f2lODnKGZCM3_hRjfgv74zKLiCuME0hZykCCOLuEUbBSXfyw3_TtxE-n9_yMzVrSWFuKHgyZNp3wt8h81J47wzkLwJHzJCZjixeXRkSYSxdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
شعب عشق قائده وإمامه..
سيدة إيرانية كبيرة بالسن تسير زحفاً لتشارك في تشييع الإمام الشهيد.</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/naya_foriraq/81178" target="_blank">📅 12:09 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81177">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5c3013d59c.mp4?token=qCeqkP4ooeepkfb67BAQ8JBBaAF2fRIV7EfdWPWzUaM1rlPK9IfkSx9llWHxdhlceY660rhRmm7dhnVsNNexXvuiFiu3iHUC_jXUCrjjNQkxIjuoEzsEHEQXjn0CJTy-FMhOsuBLpY8bRT_-BSZpLhsOLGrJUU6R9ivq2GbYritKrpRIehKAaY7HBnxJwyZ6ZIUyN8zJrY6fehwhg47q0jhctvokzywy2NT4WCyoUi-uaa_RlofRY04nz36BqSawyDCX-ucubAvoMoiRobxK1OdpGbjDOyLB-HY1jdOIdTJZl98gPHVD7JMNLZc2WfelKFDhTLHSiOlaPjMt1P152A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5c3013d59c.mp4?token=qCeqkP4ooeepkfb67BAQ8JBBaAF2fRIV7EfdWPWzUaM1rlPK9IfkSx9llWHxdhlceY660rhRmm7dhnVsNNexXvuiFiu3iHUC_jXUCrjjNQkxIjuoEzsEHEQXjn0CJTy-FMhOsuBLpY8bRT_-BSZpLhsOLGrJUU6R9ivq2GbYritKrpRIehKAaY7HBnxJwyZ6ZIUyN8zJrY6fehwhg47q0jhctvokzywy2NT4WCyoUi-uaa_RlofRY04nz36BqSawyDCX-ucubAvoMoiRobxK1OdpGbjDOyLB-HY1jdOIdTJZl98gPHVD7JMNLZc2WfelKFDhTLHSiOlaPjMt1P152A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية تظهر كثافة الحشود المشاركة في تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 8.94K · <a href="https://t.me/naya_foriraq/81177" target="_blank">📅 12:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81176">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3ff45c8712.mp4?token=Sx943RnIn-PPHa4pnafMCDQuO39TxpACEQ9tVHLPxXIkGNM-msAnf_tspRd_4FelAP4YlF8FXvnYlFK5a3r9rBPhC0l4iAxms46MYbShbZ9ppYXYz9x3v4G18fg-P6d1rsoU4TKJJ9iBiiPliMug58WJ4PJ7jXzvGpV9MXUQ17Sxn40L1fs1rtwm6Ns0oigkcLh34DcRTmfTFJMYxrIRpUHZfGkq9Rypz3eSR0uZExKINp2Mg1Kew8ytQaLs8ZLz2eHHRczUCA-1DujQtccLHFJiB-_peLrItAByxPbbfXmpoSB9LKUSZXrfMmWxmvC5A3L5IudLXeLZw3AJCPoSeyYNhjP2W9PCqtyMbKN5VceqH_rY8DmC1Tw7G08fGXAqbTZx4btSHBjQyLd-kySHem1gEsQFkqJ3gwGAqTYw5MAuTtWRITl_3TxTdPub-BfP_ugxmHXcOWtaGQx-pjIuQW8W0f_IpGx8wA4vrt7g9NwQKrrWvaT_ryYA9WSICrqrDC1BsW4H3ESd4B9VTzYyW1bU8X9DIbNpAev859-AiU7-l0C_FL_SQlWsQJDcamyMczEBQT1_smFzqWq1o2fuuQqzuA5FrZccFo9bMz4z3vrha-IpiIhI23CrKmF3AuWDyW0Ffet9nqsk4CZRIUAR65Pdl1maIpltMstRGQto7t4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3ff45c8712.mp4?token=Sx943RnIn-PPHa4pnafMCDQuO39TxpACEQ9tVHLPxXIkGNM-msAnf_tspRd_4FelAP4YlF8FXvnYlFK5a3r9rBPhC0l4iAxms46MYbShbZ9ppYXYz9x3v4G18fg-P6d1rsoU4TKJJ9iBiiPliMug58WJ4PJ7jXzvGpV9MXUQ17Sxn40L1fs1rtwm6Ns0oigkcLh34DcRTmfTFJMYxrIRpUHZfGkq9Rypz3eSR0uZExKINp2Mg1Kew8ytQaLs8ZLz2eHHRczUCA-1DujQtccLHFJiB-_peLrItAByxPbbfXmpoSB9LKUSZXrfMmWxmvC5A3L5IudLXeLZw3AJCPoSeyYNhjP2W9PCqtyMbKN5VceqH_rY8DmC1Tw7G08fGXAqbTZx4btSHBjQyLd-kySHem1gEsQFkqJ3gwGAqTYw5MAuTtWRITl_3TxTdPub-BfP_ugxmHXcOWtaGQx-pjIuQW8W0f_IpGx8wA4vrt7g9NwQKrrWvaT_ryYA9WSICrqrDC1BsW4H3ESd4B9VTzYyW1bU8X9DIbNpAev859-AiU7-l0C_FL_SQlWsQJDcamyMczEBQT1_smFzqWq1o2fuuQqzuA5FrZccFo9bMz4z3vrha-IpiIhI23CrKmF3AuWDyW0Ffet9nqsk4CZRIUAR65Pdl1maIpltMstRGQto7t4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بعد يومين قمر الشيعة سيكون بيننا.. ويجب أن نوفيه حقه بغضاً بقتلته الصهاينة
#قوموا_لله
#باید_برخاست</div>
<div class="tg-footer">👁️ 9.53K · <a href="https://t.me/naya_foriraq/81176" target="_blank">📅 11:58 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81175">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e69322afe.mp4?token=fsEXYGfqkWwRc8mylG_Z6j-hNo65kCPtdKsXP22rVSEvZK5fpiTcsQNE8edmoLQTIy5dOpS87_kVVBOtUMisUfW5-tPYYYpIV0fH-Bnppn4yCOALBvgM4K6CeCk4ASgbp2Q-5RMH9I-UMuEK1B2P0PG09U4ICzYeSNpfMEWvpw8gEn2bFyVPBSylvpOXT-7KAuyghz3V6A0rgVjn6S7VSTIzZ-yZ7VrvnDZxgsNSLKZy1XPkP-wyGu130pJSia0aW7UmY6-AN7mjUPqc6OUWS4W2Ae-aB_JDo3bvU6oTwLZZQW-FQXo14LJ6iCT0PbukQv2dO9WI9R9ZyXiYq6EoGTCx81ElDhWPGb4oJ4K-hPtG83LjfOm6uO0QVcLI7Edwr6DLCjYOdWqaMakhHLEJnFr3D2FM9uo2Alt3RC7YHaaXEM8mcP905fpjBv3xDvKMg0gShDTfqMHDJk-WaU3dJU6OWPw6lst9woxLcekbthOqTLpx_E3KVql_0FKkgFuaxhpr7Aes3o_p8O6kSYaY2TrsMj2d3OvFQQkR5lhnf1gymsfL_RMaW2FD1sc7dazSINkOpYC98ZOsvvXOfi3zJtU-Hs7iuJDJP6RojC7Fzdg3Jkzt5qzKbj2jfljeb44rg00K13L_mCjppQ0GfmtW1Rw16TvsITreSkp1CjhbodQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e69322afe.mp4?token=fsEXYGfqkWwRc8mylG_Z6j-hNo65kCPtdKsXP22rVSEvZK5fpiTcsQNE8edmoLQTIy5dOpS87_kVVBOtUMisUfW5-tPYYYpIV0fH-Bnppn4yCOALBvgM4K6CeCk4ASgbp2Q-5RMH9I-UMuEK1B2P0PG09U4ICzYeSNpfMEWvpw8gEn2bFyVPBSylvpOXT-7KAuyghz3V6A0rgVjn6S7VSTIzZ-yZ7VrvnDZxgsNSLKZy1XPkP-wyGu130pJSia0aW7UmY6-AN7mjUPqc6OUWS4W2Ae-aB_JDo3bvU6oTwLZZQW-FQXo14LJ6iCT0PbukQv2dO9WI9R9ZyXiYq6EoGTCx81ElDhWPGb4oJ4K-hPtG83LjfOm6uO0QVcLI7Edwr6DLCjYOdWqaMakhHLEJnFr3D2FM9uo2Alt3RC7YHaaXEM8mcP905fpjBv3xDvKMg0gShDTfqMHDJk-WaU3dJU6OWPw6lst9woxLcekbthOqTLpx_E3KVql_0FKkgFuaxhpr7Aes3o_p8O6kSYaY2TrsMj2d3OvFQQkR5lhnf1gymsfL_RMaW2FD1sc7dazSINkOpYC98ZOsvvXOfi3zJtU-Hs7iuJDJP6RojC7Fzdg3Jkzt5qzKbj2jfljeb44rg00K13L_mCjppQ0GfmtW1Rw16TvsITreSkp1CjhbodQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد جوية تظهر كثافة الحشود المشاركة في تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/81175" target="_blank">📅 11:44 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81173">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=DO7gSDSqxld4RBhKd7ZgTZpFsQ7dPFurjKDX97jsqvB3krp2ZOolOMZ4s-GSB3zafXO0XIlB6pLPU5e8l62xtjD8XPlCth2NjYZ104BnHFOY3ivmFi614GQo-kiiy-5z6LVuLHTq_lMNVpo5hZSv_xmX_EuNPoDzVFGv98BbEnGWaH3dmpuJPvRM7E60GvVwSH8LNC3oR7zmw3PzpG6pG4Q0oQIoF17dvFO_elRRjY3dKSUGIb5fE5rOO9VnH_rTEKGIQ6v5hsWGqbjNqDBNrFwYRWhBVdCOzK332hp8N0tn9SWxzSaHnR3RVKiMkfXVQ5H2x53pJ41_RqR7VvoKoTl-vyy8pSV9OSZA4T-B8UNoggZ83mIwEsx8IkW71pUJX0hT-zOqG8DYHfhYXQ6gBwwmCHOAIh24VI7mn7AnQFA8Mg4h9oG-xYBGzevNQkKvlOxQAM1H7wr4TIW-86Pk__4xOFqmd_-83Z02sw4Ri2EBWkzGD7f5SBJ5mbHd1wniwBDcBCcMqoPIYBIy_FtpdDV6s-IxQ-oRD67CusV1uOqOZ3I4B0BCJJDqnCVZNOBZt0PymJVKeWB-slp6XZOvJfKFf3cpCDBikyVpjPfsJkWv6Xrm5HpCZh2Op7Sea_QXblyMm0MQf75bvlQXkUJeAzqQw6NolA7TVFFpOkdIB0w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b422331f5.mp4?token=DO7gSDSqxld4RBhKd7ZgTZpFsQ7dPFurjKDX97jsqvB3krp2ZOolOMZ4s-GSB3zafXO0XIlB6pLPU5e8l62xtjD8XPlCth2NjYZ104BnHFOY3ivmFi614GQo-kiiy-5z6LVuLHTq_lMNVpo5hZSv_xmX_EuNPoDzVFGv98BbEnGWaH3dmpuJPvRM7E60GvVwSH8LNC3oR7zmw3PzpG6pG4Q0oQIoF17dvFO_elRRjY3dKSUGIb5fE5rOO9VnH_rTEKGIQ6v5hsWGqbjNqDBNrFwYRWhBVdCOzK332hp8N0tn9SWxzSaHnR3RVKiMkfXVQ5H2x53pJ41_RqR7VvoKoTl-vyy8pSV9OSZA4T-B8UNoggZ83mIwEsx8IkW71pUJX0hT-zOqG8DYHfhYXQ6gBwwmCHOAIh24VI7mn7AnQFA8Mg4h9oG-xYBGzevNQkKvlOxQAM1H7wr4TIW-86Pk__4xOFqmd_-83Z02sw4Ri2EBWkzGD7f5SBJ5mbHd1wniwBDcBCcMqoPIYBIy_FtpdDV6s-IxQ-oRD67CusV1uOqOZ3I4B0BCJJDqnCVZNOBZt0PymJVKeWB-slp6XZOvJfKFf3cpCDBikyVpjPfsJkWv6Xrm5HpCZh2Op7Sea_QXblyMm0MQf75bvlQXkUJeAzqQw6NolA7TVFFpOkdIB0w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
تعجز العبارات عن وصف هذا المشهد المهيب، حيث يجري تشييع قائد الأمة وإمهاما الشهيد آية الله العظمى السيد علي الخامنئي (رضوان الله عليه) في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.88K · <a href="https://t.me/naya_foriraq/81173" target="_blank">📅 11:23 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81172">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇷
الدفاع المدني الإيراني:
لم يتم تسجيل أي حادثة حتى الآن في مراسم تشييع جثمان القائد الشهيد.</div>
<div class="tg-footer">👁️ 9.54K · <a href="https://t.me/naya_foriraq/81172" target="_blank">📅 11:10 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81171">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5eWGfwRqq_DJGKO3DCGWPwMHL8Rf3DHb84N5RRTknjDnxjt_z1hvbPpDBsioU3w8-9lT7tW1-xxaIGYPJgYmLgpDAeGC8_ViVVsLuiPaAhy_5qFPuEos8Ql3hAStx-kx2uTFMb_XXhxKp1fR4NDLOncNB_r5GnEGh7xM62Y1tdaFVvY5-F72f4w7Oq2Ifgch6aTFDJ-uw462XxncijwUZn634vk5GY--NK-4nmc4HvVQGd4RIqVsHBWn3ZwcuTNgUjySkrQajcow6DH2e9sV6Q6FVWMO_eE4SNL2EmZw8EtM6YK4CDeLtjLo5FAy0-erFaBm3PiPLut-6dWrAtrQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
السيد مقتدى الصدر:
أهلاً وسهلاً بالوافدين الكرام إلى تشييع وتوديع الولي الشهيد شهيد الجهاد والإباء تغمده الله بواسع رحمته.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81171" target="_blank">📅 11:07 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81170">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/42524754b1.mp4?token=tiFFjTpmH9BHXM3jDKcvMpMpTQX9NSln0g0Qf_tG_RQ4CrWoOQDu_jePRRQqiNXh9ziphx9Y3prLWDKsbskI8MskckCAPNBaPG9SP9BkaHXB_hfQ6WUd9dc55gyH3liRC7FjgJkuux2k-whgKyt1fQJABU7SFUVqlWlSseiX3vei-rJ5Dnyqm-BNwUCNt_gcS4gRkxh3clqTH1xZPJOMR_JDouKtAerqs1ECZhucSqRBC6lQUUfytEQE0CIfqemuZzWzW02vJjs3R_fjLDScdoI38v-7DCW708k-D2wMEkAoawurwvhs15QBBTjkeTTWMR2hiblFvoAaXrJy1lpIMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/42524754b1.mp4?token=tiFFjTpmH9BHXM3jDKcvMpMpTQX9NSln0g0Qf_tG_RQ4CrWoOQDu_jePRRQqiNXh9ziphx9Y3prLWDKsbskI8MskckCAPNBaPG9SP9BkaHXB_hfQ6WUd9dc55gyH3liRC7FjgJkuux2k-whgKyt1fQJABU7SFUVqlWlSseiX3vei-rJ5Dnyqm-BNwUCNt_gcS4gRkxh3clqTH1xZPJOMR_JDouKtAerqs1ECZhucSqRBC6lQUUfytEQE0CIfqemuZzWzW02vJjs3R_fjLDScdoI38v-7DCW708k-D2wMEkAoawurwvhs15QBBTjkeTTWMR2hiblFvoAaXrJy1lpIMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره.. سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 9.31K · <a href="https://t.me/naya_foriraq/81170" target="_blank">📅 11:00 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81169">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QvwAQfTsQdc_JdXcCvDKyoj115mfY-BrWp4pINLiAD6uk76zGj0iNeT0uCyxdBOHWXqq-9QfDQVM421gz-jUkLUzi9_yvXNWrZaRSnplglU0fvh7FpbD5ARfpNlYtODn9e_WF2i1Y_AqsmmK4wwHKg5LGJ7CyLrdAUoozIa7A4MiFhgKHSbQMC3DSaWnuGdjnS2Ss6nyphlM3zF7pihmo-Hxa0V5JpeR_JzTudnrZ86dZxO1gGk-ArMCmxAxq83hnTi1QZ09AWsLHU8OlaznqcyQzMu6o4gedzpzoENFsR-_7QMafGqS3KRMj38iTPcaPtHVzAs0s-UA1Vzis5VmdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌟
شعبٌ لايَترك ثأره..
سيدة إيرانية تعلن عن جائزة 20 مليون دولار لمن يقتل المجرم ترامب.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/81169" target="_blank">📅 10:37 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81168">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vup6y6ghFYOcPsM6nYeuP4qC0YrzmSETbzdN4gbFbPu6NHXqPtcDhryRqnc5njRPMGuF2aT1089Ine6kKQIfEATk-GEqMMFVzZOGpsFIvUPopIJoevLxL4ss0FYFqAPibOypb5HztuBoOy3zLdijp7I1ICypbHtLLy6uaE4jHiiQ62zST8ZuXmxO3Uh22B7eqRlfa8oP1XQXNfZ1ps6O5UvGM0EC_Ah6yCLDdzShwBI3uq_4VGnZvGmzuf28vM4mGZMyXlOMujXW0T8uJpTOOW4UZxib0pePzaDC9HbWENbed70f0ZU5uOMH6du42mTs-oVZOAe05CkxubB7_ozWiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
🇮🇷
جينه نواسيها اليوم السادة.. أبناء العراق العظيم يشاركون في تشييع إمام الأمة الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 9.3K · <a href="https://t.me/naya_foriraq/81168" target="_blank">📅 10:35 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81167">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">⭐️
إحراق أعلام أمريكا وبريطانيا والكيان الصهيوني من قبل المشيعين الغاضبين بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 8.53K · <a href="https://t.me/naya_foriraq/81167" target="_blank">📅 10:32 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81166">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 8.52K · <a href="https://t.me/naya_foriraq/81166" target="_blank">📅 10:28 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81165">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=QBEuWQtWUu6RFgssaSvwnj_WgSUyzeh30nqNBfh0yS1z2i9AthoQom1iOPw5mb7VEk4S5brbxoak6K3g7dhGIOFNOULp1N0R2okAhamRLO4MQ_LokE_-bxjMM4nXhccl1MkYOpIY0QNREHJLD4fH9AGBRWnnlLtP06VHpthPhj95zZZbu-Ij-oW5N7aFEpUEh-vY8PIPBVlIz72-IqAHcSv8EIwsg3hezPSy2ceP1ryAukJxiw1C-WAvHzD9OOYEMZ3CzU3KakTQqHw97f0pQTtPNy3ffBY3QhczT5dhLJX8x-KWvY-zvGCnMk35EhL8Rd7xo2asMsMoqyHr5qavekJZzCnH4yFW5SWvYjBfVE2dkgBmTKNUa6y3uwEj1xZ4qNx7F1iwxfFHmfvXjSS_mTvoyg5NaSNgplJONflEIVzEv749iAOsuh79p_jD-rUsKh10jRG226Yh3TsH4bbyK4olUl15WHdbPoqkszTOJfj4EwCblV-iaAjgbKIYsz9Z-OVdXayM5jC6zm1Nn1Hey-Y2ylmsuXNti86Z_LG0YZwU0WOq9M-eMV9SbxWmZtnlqqcQNslXKQLEJSwG58GIZBb2BgxbU7W_7YhjaK6iWGIflCuyx5SlYLVvdaGy-xi1QTAYIfNgX7R9462vvuSvKcKfaCWs-HDXYbThJYmWuIo" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1d247494ec.mp4?token=QBEuWQtWUu6RFgssaSvwnj_WgSUyzeh30nqNBfh0yS1z2i9AthoQom1iOPw5mb7VEk4S5brbxoak6K3g7dhGIOFNOULp1N0R2okAhamRLO4MQ_LokE_-bxjMM4nXhccl1MkYOpIY0QNREHJLD4fH9AGBRWnnlLtP06VHpthPhj95zZZbu-Ij-oW5N7aFEpUEh-vY8PIPBVlIz72-IqAHcSv8EIwsg3hezPSy2ceP1ryAukJxiw1C-WAvHzD9OOYEMZ3CzU3KakTQqHw97f0pQTtPNy3ffBY3QhczT5dhLJX8x-KWvY-zvGCnMk35EhL8Rd7xo2asMsMoqyHr5qavekJZzCnH4yFW5SWvYjBfVE2dkgBmTKNUa6y3uwEj1xZ4qNx7F1iwxfFHmfvXjSS_mTvoyg5NaSNgplJONflEIVzEv749iAOsuh79p_jD-rUsKh10jRG226Yh3TsH4bbyK4olUl15WHdbPoqkszTOJfj4EwCblV-iaAjgbKIYsz9Z-OVdXayM5jC6zm1Nn1Hey-Y2ylmsuXNti86Z_LG0YZwU0WOq9M-eMV9SbxWmZtnlqqcQNslXKQLEJSwG58GIZBb2BgxbU7W_7YhjaK6iWGIflCuyx5SlYLVvdaGy-xi1QTAYIfNgX7R9462vvuSvKcKfaCWs-HDXYbThJYmWuIo" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
اليمنيين يشاركون في مراسيم تشييع إمام الأمة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 8.79K · <a href="https://t.me/naya_foriraq/81165" target="_blank">📅 10:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81164">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=rY5K1T-Og-44WKIpVZtWvpvmI881BdY_YireCj47nstWt8oonoNgvUw1MEcCMAMRyiRDO6dN3Y5M8JowQ0UDXbEbCdojTBWJxQFLzsEs4V7hm83_0m2sprpObX1BCrXcVByDd_ylOHVFmGlwuS10kWeKdTwxoehEyvjSG3pQwotp0A75N_2LHYcoJz9fxG88N52zEQ5zf18GjyQRjMJIkqQyW50TaEq8mOTm9BwxsvtstPZ0N7GVrNP5TIlNjFIpwcerTP7Sr-wGAlnWP76aVB5r4knqldG5dDsC-sIb4GFZkr6TLURJq5TyqCRj44CGb17gT1s-Ho7A-nSPt01C2w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/180cd7b6ea.mp4?token=rY5K1T-Og-44WKIpVZtWvpvmI881BdY_YireCj47nstWt8oonoNgvUw1MEcCMAMRyiRDO6dN3Y5M8JowQ0UDXbEbCdojTBWJxQFLzsEs4V7hm83_0m2sprpObX1BCrXcVByDd_ylOHVFmGlwuS10kWeKdTwxoehEyvjSG3pQwotp0A75N_2LHYcoJz9fxG88N52zEQ5zf18GjyQRjMJIkqQyW50TaEq8mOTm9BwxsvtstPZ0N7GVrNP5TIlNjFIpwcerTP7Sr-wGAlnWP76aVB5r4knqldG5dDsC-sIb4GFZkr6TLURJq5TyqCRj44CGb17gT1s-Ho7A-nSPt01C2w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
إزالة صورة المجرم ترامب.. غضب عارم في شوارع العاصمة الإيرانية طهران أثناء تشييع القائد الشهيد، مطالبين بالثأر والإنتقام من ترامب والمشاركين بجريمة إستشهاد الإمام الخامنئي.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/81164" target="_blank">📅 10:19 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81163">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=mz9lxYhVNozkA_V3vJuORwRD47FqfnOahOgxcT2SCPzyq_u5FHxpda8YjkWc0_OQ4m6KEY9EP3EJrOnFtaL66lzmNJYaTHvW6PdlT3g_MIrrJkqdehMMZZtZL8AlPG5L8Thzw4yUjEUU36SUrMJdkjH7apjdpA-UFgw9xJsL3erhJvKEdgwd9BTjUH0waMTqB-ua-PW_J-yIL873CZSSowrHujC2QveLu2Gscm4K3OZr-AnNEm9yTLxt9CXI-eXmIqsveZnfHDekgD2YH3elI4vj9EZ5OVZii99wuaiviUogul_81gHOo6qlqrCwZ1-yNjlhIb5Sjm_hPHHxI1c36A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f0db34ce8d.mp4?token=mz9lxYhVNozkA_V3vJuORwRD47FqfnOahOgxcT2SCPzyq_u5FHxpda8YjkWc0_OQ4m6KEY9EP3EJrOnFtaL66lzmNJYaTHvW6PdlT3g_MIrrJkqdehMMZZtZL8AlPG5L8Thzw4yUjEUU36SUrMJdkjH7apjdpA-UFgw9xJsL3erhJvKEdgwd9BTjUH0waMTqB-ua-PW_J-yIL873CZSSowrHujC2QveLu2Gscm4K3OZr-AnNEm9yTLxt9CXI-eXmIqsveZnfHDekgD2YH3elI4vj9EZ5OVZii99wuaiviUogul_81gHOo6qlqrCwZ1-yNjlhIb5Sjm_hPHHxI1c36A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
مهاجمة صورة ترامب في العاصمة طهران من قبل المشيعين خلال تشييع القائد الشهيد.</div>
<div class="tg-footer">👁️ 9.34K · <a href="https://t.me/naya_foriraq/81163" target="_blank">📅 10:13 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81162">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=cGB6nv8aRQU6qJlx3BAmnCTqshhQmbQWxXA6HZr5jmns2QzKYHtmxuqZC_PVg_HQ8AjmOfNlAwfnA4xOH4b3wRSzJts660jruz0Yf61msOkt2D8kAD2fOBXyVPjgiSTtqQspqR5LSEe3BVRihVoOxqjzDc8V9S477Bm6RESyN_4ionqhewTy-WCAeSQ4FDvdkEKH-hIM2Tu6KStIpAQbnoZY-R_UFiSH-IlTPNIzIRENuCEiQpVGnZWkG8BeAa3-d3NCkwtj2yGEFk0mjL5VtFVxT7V4j-PrzNSX7Dn7ACw9BQsPet8MopEr9KDX9V8qwlMTJ_dNWfYdNegmjnHKjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4b95403b3.mp4?token=cGB6nv8aRQU6qJlx3BAmnCTqshhQmbQWxXA6HZr5jmns2QzKYHtmxuqZC_PVg_HQ8AjmOfNlAwfnA4xOH4b3wRSzJts660jruz0Yf61msOkt2D8kAD2fOBXyVPjgiSTtqQspqR5LSEe3BVRihVoOxqjzDc8V9S477Bm6RESyN_4ionqhewTy-WCAeSQ4FDvdkEKH-hIM2Tu6KStIpAQbnoZY-R_UFiSH-IlTPNIzIRENuCEiQpVGnZWkG8BeAa3-d3NCkwtj2yGEFk0mjL5VtFVxT7V4j-PrzNSX7Dn7ACw9BQsPet8MopEr9KDX9V8qwlMTJ_dNWfYdNegmjnHKjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
يالثارات الحسين.. بحر من المشيعين في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/naya_foriraq/81162" target="_blank">📅 10:12 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81161">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8abd840738.mp4?token=TMWnvIBjYgZds02rZGJqMmevXdVWPGbSeGGMv5j1I63CS5mo58-vidsEu3KBx6vcqm1OhshP5cf5DTKEXQsHi3ayCeOBWJ__SHOg8BAXdLpiEeTasneOw3XC_bLpoUH3TsocaYmmYClloW_-mm2yqhnCU1loTRoxxrI1X5iIvgv_JtS-6Z2Hv6XVxe23ymqJRabOpwrZu0seNU7R51QOnp2w9qSO76BmmarJEU6KN3BVeYQk8N24g-5P7Z5FS1lH5Qx8QU9FBjqcDbAimI8biAo_1UgURk2Lyt51a_KeSJoagSmwff7PvLKCil-tYU8ifoJVHlzqqDy83BA4WoKN4Zmh-a9lV69hgawt8KJOvbhKRpBoBl70Jr0xQEbpdQD43vRP3TR_krguDyifCZqEKpErumhHgCfxW55qH_4t_2fdicxLbL3WVAt-M_aVjVZSd-vNpYDrhBgLTQyaYywJVYrOwMQCMiGqozMU39Cb6r_n3axa7cyEE519KOBiVG9IOBuf9TPzcJPuPD2Fl7ep0AJIv379WSIyvU7TUGpBPysR2yDIL16KdxgBoXclur4Chlpc6Sb46vh6C55ZxC73jKz-q5KN0rrwtp5Aodk3vNw--M4Ya4rxTda8_OR6sKF4ymY28HFn1n1UjLR_McSzlzi9fnNTlnscYtRx2gpKEcs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8abd840738.mp4?token=TMWnvIBjYgZds02rZGJqMmevXdVWPGbSeGGMv5j1I63CS5mo58-vidsEu3KBx6vcqm1OhshP5cf5DTKEXQsHi3ayCeOBWJ__SHOg8BAXdLpiEeTasneOw3XC_bLpoUH3TsocaYmmYClloW_-mm2yqhnCU1loTRoxxrI1X5iIvgv_JtS-6Z2Hv6XVxe23ymqJRabOpwrZu0seNU7R51QOnp2w9qSO76BmmarJEU6KN3BVeYQk8N24g-5P7Z5FS1lH5Qx8QU9FBjqcDbAimI8biAo_1UgURk2Lyt51a_KeSJoagSmwff7PvLKCil-tYU8ifoJVHlzqqDy83BA4WoKN4Zmh-a9lV69hgawt8KJOvbhKRpBoBl70Jr0xQEbpdQD43vRP3TR_krguDyifCZqEKpErumhHgCfxW55qH_4t_2fdicxLbL3WVAt-M_aVjVZSd-vNpYDrhBgLTQyaYywJVYrOwMQCMiGqozMU39Cb6r_n3axa7cyEE519KOBiVG9IOBuf9TPzcJPuPD2Fl7ep0AJIv379WSIyvU7TUGpBPysR2yDIL16KdxgBoXclur4Chlpc6Sb46vh6C55ZxC73jKz-q5KN0rrwtp5Aodk3vNw--M4Ya4rxTda8_OR6sKF4ymY28HFn1n1UjLR_McSzlzi9fnNTlnscYtRx2gpKEcs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🌟
لافتة كبيرة تحمل عبارة "سنقتل ترامب" باللغتين الفارسية والإنجليزية خلال تشييع القائد الشهيد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 9.74K · <a href="https://t.me/naya_foriraq/81161" target="_blank">📅 09:46 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81160">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=isuuiuHFQFBz9afBD2ug_BLMxse8O5FHuCu92b5TE6UX7bKcN-Fdu6ZDoHaz4StxZjAE00Bd8UoOjbz3kCTF8wxN9g4DB1aoCq6IPh5-AmqotslsW1DRZP4_rPz3y7j2mO359GyMxj525gzYWjeBUfkR9JRG7Dn7RCyZ7UvLsOKWzcQuqYv4OoAXMz9tEwQfQ-lX8eAF8tblr4ypzPNjsjEBTRm7WRwe4VxXCaMS5Prk58E7FXSegaLJcpcS7DLkO3WEmQGydw8v8QSNI7QbamxHktmA7bcSOO1KUmxmRLfWy0xCU-1uUZ3Thxk5HBc8Tp3hXaiHnmrOoQf0n_Q03pL_eEs8VNYw-lRoK53Aw8Yx_lbwHGxOBq93dR_udrFqaTQBFsn-EjwudjJrqvrtzG4wgSDpVKl7TflWHx6XvS9ePHSP3qAwrs6Tc6Zq_LyQjojSgi3mEtA_GlSwKiRzrtvM9-pS8uIoRMRbATFniJSupvA_izPQYgfS2OIYPBT2TYJUXHKwgh8Mp0Diulb00c1Rtqbp_YKS_GvExUZsCcwIDqsjiUsIViMYrWRGmQ5xWokXx0tgL5YwsAN4l1LlBbVg8HPdNdkG5wWihxp8-HscVxAKEc7hBdZW3Ub0RWTCwi3MRgQNBI93YZ0z7Ud8u15RWAIudwj1mkPcxjX1hnE" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd3ecf504.mp4?token=isuuiuHFQFBz9afBD2ug_BLMxse8O5FHuCu92b5TE6UX7bKcN-Fdu6ZDoHaz4StxZjAE00Bd8UoOjbz3kCTF8wxN9g4DB1aoCq6IPh5-AmqotslsW1DRZP4_rPz3y7j2mO359GyMxj525gzYWjeBUfkR9JRG7Dn7RCyZ7UvLsOKWzcQuqYv4OoAXMz9tEwQfQ-lX8eAF8tblr4ypzPNjsjEBTRm7WRwe4VxXCaMS5Prk58E7FXSegaLJcpcS7DLkO3WEmQGydw8v8QSNI7QbamxHktmA7bcSOO1KUmxmRLfWy0xCU-1uUZ3Thxk5HBc8Tp3hXaiHnmrOoQf0n_Q03pL_eEs8VNYw-lRoK53Aw8Yx_lbwHGxOBq93dR_udrFqaTQBFsn-EjwudjJrqvrtzG4wgSDpVKl7TflWHx6XvS9ePHSP3qAwrs6Tc6Zq_LyQjojSgi3mEtA_GlSwKiRzrtvM9-pS8uIoRMRbATFniJSupvA_izPQYgfS2OIYPBT2TYJUXHKwgh8Mp0Diulb00c1Rtqbp_YKS_GvExUZsCcwIDqsjiUsIViMYrWRGmQ5xWokXx0tgL5YwsAN4l1LlBbVg8HPdNdkG5wWihxp8-HscVxAKEc7hBdZW3Ub0RWTCwi3MRgQNBI93YZ0z7Ud8u15RWAIudwj1mkPcxjX1hnE" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
جموع المشيعين يحيطون بالمركبة التي تحمل الجثامين الطاهرة المتجهة نحو ساحة الحرية في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 9.59K · <a href="https://t.me/naya_foriraq/81160" target="_blank">📅 09:30 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81159">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=ngxY_Q6hbtLvGtRKvpMWus63AoZ0aE9tyQQ5WWVo8VJxKvBTrt9gxqOTYm6WZDIpTXjz3gCMt1uUlGgNdNUQpqTfIohYufjAyrXmsqn6-CUJ6KwsmqWPwlqfUuHHURcGiRXF8TuLDXt_24Wuw_ChmIJIXTkSpszOp4D57x8EXquaMWQnH4Cguy-vWFmZ9Vpi2frXvuos5twrS3vrscroqXfUpnw_ueXpsC2sEgxAUJHU_qglAL-5sIGQ3HwYhLag4rne-zxX5oTEisAJZzOLnOmGFsJ4Voe73gUB6i9WoBXO9A0zotmHj0vNtHm7yPHBDS73VTG-0p_ji_UvirL6_2pWPLzgXroZXGoQrc25A2xrxR-b7b23S3RjIWYEU2KZwA4RNt8JbHdiE7O7YQQMi4KkD-jq-oDwVsMilzMF5-JEdW0tkju6F6wC5XUWaOZxM58lglgqyXKyaoT6tec9kDJ6Gvl3zFMRD5KQULxooQyhqJ0Q2RpL9BfkHu33UX-kzMbcPqoo6U1pK8Wt6_d3J1gI8AV3KZjHEECpR4Di0d7vIxXwroO3Kp2t3tu9LoWJdECB08va8m4FEdVw-Q0CYLyhVvzxOgpNw5dVJd6-TN4lY84YUta2_q86SyAQylA7Ncv5Z_Nl74Q5-YgcaOlQDNRpxITzUVbC4tzB6qAnnnw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c809f5d37b.mp4?token=ngxY_Q6hbtLvGtRKvpMWus63AoZ0aE9tyQQ5WWVo8VJxKvBTrt9gxqOTYm6WZDIpTXjz3gCMt1uUlGgNdNUQpqTfIohYufjAyrXmsqn6-CUJ6KwsmqWPwlqfUuHHURcGiRXF8TuLDXt_24Wuw_ChmIJIXTkSpszOp4D57x8EXquaMWQnH4Cguy-vWFmZ9Vpi2frXvuos5twrS3vrscroqXfUpnw_ueXpsC2sEgxAUJHU_qglAL-5sIGQ3HwYhLag4rne-zxX5oTEisAJZzOLnOmGFsJ4Voe73gUB6i9WoBXO9A0zotmHj0vNtHm7yPHBDS73VTG-0p_ji_UvirL6_2pWPLzgXroZXGoQrc25A2xrxR-b7b23S3RjIWYEU2KZwA4RNt8JbHdiE7O7YQQMi4KkD-jq-oDwVsMilzMF5-JEdW0tkju6F6wC5XUWaOZxM58lglgqyXKyaoT6tec9kDJ6Gvl3zFMRD5KQULxooQyhqJ0Q2RpL9BfkHu33UX-kzMbcPqoo6U1pK8Wt6_d3J1gI8AV3KZjHEECpR4Di0d7vIxXwroO3Kp2t3tu9LoWJdECB08va8m4FEdVw-Q0CYLyhVvzxOgpNw5dVJd6-TN4lY84YUta2_q86SyAQylA7Ncv5Z_Nl74Q5-YgcaOlQDNRpxITzUVbC4tzB6qAnnnw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 9.58K · <a href="https://t.me/naya_foriraq/81159" target="_blank">📅 09:27 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81158">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=W-6CQwK3RDZsbDeH7Hg1JR_lw5JoMlnxLbo5alY83yftDxSuL-zU2AI0IcURInatkZHVTz3nwFdWebYe9O7ONBUYskExG1ZTvrMOFA4yezYtIkZ-g47RoPOsN3cn_k1VMsVUEf6P_fgw4KfH8JnKR8iGG5-m0EGJDtkPQ8AH1Aff1trmOLNx1rScWyCH3ay0IVak2-j4SGYoZ9c0Ci0kjSpQuCDDT6OTJRAApKC5bxbIgqLpSddxm2GasJmQyGD-NeG36GD0Nou2lPurc0ycidhAd4J4lxrwaSr1M21VTZiuU0a8BIVCgqEIww8avlWs9mbzVTuqOGlh9wCWxv47dhqQ3HdNweaTiQR0arQIQBQVVaRKT5BlkiViDPT4vNBh9A_V0ts4qXYIP4WRHIaLmbxjGbhpXw_GiDnwwz0AzpWk8zXEtgR2Dg4Yxb29kRddAWjYx0wN3_az8E5Xv6FZ6tMcAoh44rnf0cxLGpnuj90aWiRcskTOD4ShG_c1DBmFaA2UMDnGo8AEDAhkppvQgx_syTK8JJ7ujPv4Xdsg_ziXEMOV62KB6h-37hAWxMUJ6MEeMojZzuz5d1yXMAYfvYSyAdTO7HD46xV2m-mD1WG6MYiNCLlyopa__wyYbtZ71O1djCpu5RyWziQ2Q3a3PfNWpawE6x3KulVzqUAj7hA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e02d27f89c.mp4?token=W-6CQwK3RDZsbDeH7Hg1JR_lw5JoMlnxLbo5alY83yftDxSuL-zU2AI0IcURInatkZHVTz3nwFdWebYe9O7ONBUYskExG1ZTvrMOFA4yezYtIkZ-g47RoPOsN3cn_k1VMsVUEf6P_fgw4KfH8JnKR8iGG5-m0EGJDtkPQ8AH1Aff1trmOLNx1rScWyCH3ay0IVak2-j4SGYoZ9c0Ci0kjSpQuCDDT6OTJRAApKC5bxbIgqLpSddxm2GasJmQyGD-NeG36GD0Nou2lPurc0ycidhAd4J4lxrwaSr1M21VTZiuU0a8BIVCgqEIww8avlWs9mbzVTuqOGlh9wCWxv47dhqQ3HdNweaTiQR0arQIQBQVVaRKT5BlkiViDPT4vNBh9A_V0ts4qXYIP4WRHIaLmbxjGbhpXw_GiDnwwz0AzpWk8zXEtgR2Dg4Yxb29kRddAWjYx0wN3_az8E5Xv6FZ6tMcAoh44rnf0cxLGpnuj90aWiRcskTOD4ShG_c1DBmFaA2UMDnGo8AEDAhkppvQgx_syTK8JJ7ujPv4Xdsg_ziXEMOV62KB6h-37hAWxMUJ6MEeMojZzuz5d1yXMAYfvYSyAdTO7HD46xV2m-mD1WG6MYiNCLlyopa__wyYbtZ71O1djCpu5RyWziQ2Q3a3PfNWpawE6x3KulVzqUAj7hA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
مشاهد أخرى من الحشود المليونية التي خرجت للمشاركة في تشييع الإمام الشهيد السيد علي الخامنئي (رضوان الله عليه).</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/81158" target="_blank">📅 09:15 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81155">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=HOYOR23pe8J-0MyISooT29GIAx8ZuHOvwHUw6JWSc7x8CnmAifqcn3BbYOrVRgpo--coCX5Su8qyL2EnSBaYav2Hhf4lTPxfwZxKY5_lStAr0LxK9161eZerJNrNFi8pYSI96r3dHWu5SnUjrF615EzdAQYtgMHnqOCv36N_AvD6WKgQH7XklwgeTXWu57JCvblpjRFFcGq9nv_N1IZsGTm5-G0FwrOp1u5dS55bnM6RnrY1Y0VH2Hkwn9ThTfWCuEtyWP8YK0RJXTsLisN_TN5Bt_NYGzLlVuS2zfC7eS6a4CEx-k7tTV2NeAgMxIVStNMUnYAjixPQhHYxoUNwKKVfCA-94Fl3jbllJM0ZdkKKvTfFuvj9Yzj4b-ye-UJrXGJ8sokDm9HBuRMEC8lQbfxoP_A6RSn5uqoBsMG4TQ5jf1TglWiMWBoWCvxnJegvYF1S75F-9ShgG9P5z4GJyELhEolBHguuHJ3EY0AwYv0wSlNJmhvWA49QudJEi7kYGy2k4JOV88D4HmfAVAIp7EUJ35JTnSFHZoQdbAEg5cycHBabZ6rtuV1k2Gseed9TPiffV9dpk-fysET1pQ4JGVbkJd3aWKl7JvxPmT5icvr21N8TlPJ1DYSma-kLB_okw-5Biwx10gUNa1Lkiuj8xFz5bUQRaUOE21MBxrI7jzs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ed80a1b5c.mp4?token=HOYOR23pe8J-0MyISooT29GIAx8ZuHOvwHUw6JWSc7x8CnmAifqcn3BbYOrVRgpo--coCX5Su8qyL2EnSBaYav2Hhf4lTPxfwZxKY5_lStAr0LxK9161eZerJNrNFi8pYSI96r3dHWu5SnUjrF615EzdAQYtgMHnqOCv36N_AvD6WKgQH7XklwgeTXWu57JCvblpjRFFcGq9nv_N1IZsGTm5-G0FwrOp1u5dS55bnM6RnrY1Y0VH2Hkwn9ThTfWCuEtyWP8YK0RJXTsLisN_TN5Bt_NYGzLlVuS2zfC7eS6a4CEx-k7tTV2NeAgMxIVStNMUnYAjixPQhHYxoUNwKKVfCA-94Fl3jbllJM0ZdkKKvTfFuvj9Yzj4b-ye-UJrXGJ8sokDm9HBuRMEC8lQbfxoP_A6RSn5uqoBsMG4TQ5jf1TglWiMWBoWCvxnJegvYF1S75F-9ShgG9P5z4GJyELhEolBHguuHJ3EY0AwYv0wSlNJmhvWA49QudJEi7kYGy2k4JOV88D4HmfAVAIp7EUJ35JTnSFHZoQdbAEg5cycHBabZ6rtuV1k2Gseed9TPiffV9dpk-fysET1pQ4JGVbkJd3aWKl7JvxPmT5icvr21N8TlPJ1DYSma-kLB_okw-5Biwx10gUNa1Lkiuj8xFz5bUQRaUOE21MBxrI7jzs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
وسط أجواء حزينة.. تسير العجلة التي تحمل الجثامين الطاهرة، نحو ساحة الثورة بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81155" target="_blank">📅 08:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81154">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b13427680a.mp4?token=Apv-_a0Ds6YHkUEUrRkFpWXESuC4Q9A9wSkrbcQQ2wh3icWgzAVCF4KSwRS5V48IruTFZ2bjL_XQ88N9hnBJy8TByHVRGHSi6KeN9f-DGrTyrzgLlRgWSD-FCgt8D81JoN61Yffc97sNT96tlA1jfwkpyjj5f9AJFsPIhx38_PfbwJ58AJdVbnqf-zM6i4bGYDJXBf-fb5QJ5GAjy4Ocsqwt8s6HL-YAM4APavj5PEL6bk83-1kAzaSdPmBHCYzopTDNskSQY4_ORUoVVT-jNnV0br8XStIWUAIIliz9HhczP7zxX_O2PIqo7n2VCLpZP5_faa6g60q3kHkic60lkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b13427680a.mp4?token=Apv-_a0Ds6YHkUEUrRkFpWXESuC4Q9A9wSkrbcQQ2wh3icWgzAVCF4KSwRS5V48IruTFZ2bjL_XQ88N9hnBJy8TByHVRGHSi6KeN9f-DGrTyrzgLlRgWSD-FCgt8D81JoN61Yffc97sNT96tlA1jfwkpyjj5f9AJFsPIhx38_PfbwJ58AJdVbnqf-zM6i4bGYDJXBf-fb5QJ5GAjy4Ocsqwt8s6HL-YAM4APavj5PEL6bk83-1kAzaSdPmBHCYzopTDNskSQY4_ORUoVVT-jNnV0br8XStIWUAIIliz9HhczP7zxX_O2PIqo7n2VCLpZP5_faa6g60q3kHkic60lkzzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 9.9K · <a href="https://t.me/naya_foriraq/81154" target="_blank">📅 08:26 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81153">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mncWfJ7nP_Y2zzwt_GUXBFJpeY4QZMtS-Y7tgV0wYL3aYWf9KnAz6Ceyr9y9PKL7f4jKL5fBEESWyH2y47uocNvJaBG07FlTM1N_ADN_0zJrxANGbsNzsLWENAPejt1OCBGhUQZIPOLdIKARLqRCswpATp3fCebVDez6qu5UtaLuNFQBQfilb3FJ4gsyPGxS0ydeZryu0Nxw2Ff_9_vohr_-kMpNPf-icBr69lbHR_o3pMxnWWrEwapG-pNxbyT0EJEHeSXEwz5RejTTMJC59PWlKF_dUDj6JoUMoe3Av5CHEXnlpVd4hbl9krO5I6FYqhaRrE1Iv8IkjPutkfzSaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/81153" target="_blank">📅 08:24 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81152">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=E1NIXFaF1fnK7AXy5Gpl-t8tm9kB2Qu5Cnu6npQUyGORGydJ93kGt__fOvYSxTG9SrV5HJBwjXQqJu9OmZlXdLPEmc62GkI-AmIZ9XB3vSIk3EURaMSGNxBVBU5zFNWa2CwNsPSZthA8tdDZileMuSFOszqZjsFjvoSnwrzQGhs5pZoJ-2ZHAzs9lE_l95j8M3UMbgpwc4pt6h5eyrwicXqUFA6xVRZMHfnMOIwNsK_h_Eb6Ldtv-JM_jkiJ3GHqTppZHW8UQkQNW_zucXzJpSroidAm8kfgCPbnyps-pJ2rjNeiPGKTTuwlq1vZOqwAtB6D96BF7tnobEiwSTmX_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6616f0efeb.mp4?token=E1NIXFaF1fnK7AXy5Gpl-t8tm9kB2Qu5Cnu6npQUyGORGydJ93kGt__fOvYSxTG9SrV5HJBwjXQqJu9OmZlXdLPEmc62GkI-AmIZ9XB3vSIk3EURaMSGNxBVBU5zFNWa2CwNsPSZthA8tdDZileMuSFOszqZjsFjvoSnwrzQGhs5pZoJ-2ZHAzs9lE_l95j8M3UMbgpwc4pt6h5eyrwicXqUFA6xVRZMHfnMOIwNsK_h_Eb6Ldtv-JM_jkiJ3GHqTppZHW8UQkQNW_zucXzJpSroidAm8kfgCPbnyps-pJ2rjNeiPGKTTuwlq1vZOqwAtB6D96BF7tnobEiwSTmX_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">العجلة التي تحمل جثمان الإمام الشهيد، تنطلق نحو مسار التشييع.</div>
<div class="tg-footer">👁️ 9.96K · <a href="https://t.me/naya_foriraq/81152" target="_blank">📅 08:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81151">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=W0Z030ytKmUxw4UGsi58kIOmLWJknR6cpULrvhN_VKOTmpwu4OOzAeT6wUM1Y6ch6gwjuUZkuVDfmKGiAQUoGep9PqdB-nAx2bBBfrBuaBmRbMAX4MbZWPB3Ei_HTtXZCtJiQLV8QIVnUHaYqJtE7vamQr83BVPPns5UUBVwm2UYOEwsIM61QbCBsXSa_p_0EAQeOw6q3X_P6OwQ7R-NQWi7mFA6T9F6CWeXMeIs-T8Ecb_QyUj82z4rU6_Q_JN280kz_qKHBnB2OwIzLj6j4I-kjpz39Srnp0IqZJAF9XAsCDD_6zcxn4WmMW_S634KWLSQpOYEYUrsnWKxEGSxsw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/48c7081ef9.mp4?token=W0Z030ytKmUxw4UGsi58kIOmLWJknR6cpULrvhN_VKOTmpwu4OOzAeT6wUM1Y6ch6gwjuUZkuVDfmKGiAQUoGep9PqdB-nAx2bBBfrBuaBmRbMAX4MbZWPB3Ei_HTtXZCtJiQLV8QIVnUHaYqJtE7vamQr83BVPPns5UUBVwm2UYOEwsIM61QbCBsXSa_p_0EAQeOw6q3X_P6OwQ7R-NQWi7mFA6T9F6CWeXMeIs-T8Ecb_QyUj82z4rU6_Q_JN280kz_qKHBnB2OwIzLj6j4I-kjpz39Srnp0IqZJAF9XAsCDD_6zcxn4WmMW_S634KWLSQpOYEYUrsnWKxEGSxsw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همه آمده‌اند، با پرچم سرخ انتقام.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81151" target="_blank">📅 07:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81150">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=WgZFkfIKPgyyASedgPWxzISQqsELxxuEuncf2j76Gr4U2LVO2FI9CGmDZ3_-MaHBSR74ln7hkZ31aSws-H9a2pyC8LLUSlPFH1Nuzg1R8EYVYRLR4IV6dI98YqCWV2cITKu1YX_qQ8gRszjAid3ManAIYebANKC1UC92s6myS3_APp-ot-c6NREtdx7LGkqewejzbG3z0Hq1-78dpHr91in0GQeUkGDME8cpvfqntB3rFj3aATmclsPVGNg6QDS5DyTWbj1EJKS99jehoBAuSpJeNTLbz6waCWeMUgKoD9VS6oLKhmqAgdM1d8ecxTO0ddejzSGk5vuWAGlWzQJ2Dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a22423dd0b.mp4?token=WgZFkfIKPgyyASedgPWxzISQqsELxxuEuncf2j76Gr4U2LVO2FI9CGmDZ3_-MaHBSR74ln7hkZ31aSws-H9a2pyC8LLUSlPFH1Nuzg1R8EYVYRLR4IV6dI98YqCWV2cITKu1YX_qQ8gRszjAid3ManAIYebANKC1UC92s6myS3_APp-ot-c6NREtdx7LGkqewejzbG3z0Hq1-78dpHr91in0GQeUkGDME8cpvfqntB3rFj3aATmclsPVGNg6QDS5DyTWbj1EJKS99jehoBAuSpJeNTLbz6waCWeMUgKoD9VS6oLKhmqAgdM1d8ecxTO0ddejzSGk5vuWAGlWzQJ2Dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/81150" target="_blank">📅 06:53 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81149">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c8AdxShclk_U1UX2PbWGiIJWxNwVi5qQ0v_W27lIzUXf3KuemtX_J6wFyQsPLQzc2mRi2n7-R2RIf3ALOYabOy7OtptL5x1RMtztU0viGsZ9y4d0E7pbluqdJHBxF7brABAPjs8wRRCfdQRX3ACI0pKbT6dvrivl-83Au63X84OdmblgfcHDXiGWQVYOatsGdqbjmlGjW5pfj-pKwnIiYTsb2YkCXVqZBBdBO_t_oqbGDMygvlMAzahbFXDdq8hLm9FyOg3nGDV48O00NOB636WR7wSOHXan8mZ2oWjJs8aqp6IIbB30k33HLNMhV6hieU1WNi6KYJi5x9QPgMObEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🌟
سنقتل ترامب..
الشعب الإيراني ثأراً للإمام الشهيد، يتعهد بالقصاص والإنتقام من المجرم ترامب.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81149" target="_blank">📅 06:41 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81148">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eYloCn6IgQy54DItlZdfDjAMk1N5JLm4Tj2hsjxVBAwuBlc0iXgBRy6OOeLWCotAuIH_A5XhkcTlks7SNbwrZSWYNjcPCMQ9ynmNRmt-MwN4PnoLnkB10R7dRpDQTNb1LBpkcFHRVGjsBjothT2K87J94K6qxR_t_Sc2lRYOIq28wZU8hhojJsOD_8FghPZ5t2HE8BwiIHOqF6N_I2SyIrin2k7m4UR3g94aRmnaaAp4mmsM7Adhg_-Z-cbmIGQM2CMnTiQj1otZFJ_vEeiYFGe0phLhhjMMHRBQr7Fnd2U3UozHdQcvFngLVnRPDMQ7xLpAWdBi0f7G1KuoLPrWGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
الحشود المليونية تنتظر وصول الجثمان الطاهر للشهيد القائد السيد علي الخامنئي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/81148" target="_blank">📅 06:33 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81146">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=sbiBNHCXP6k946SgWMkbOJLzRIqzV8RC5sqm3jOEnsAiv_W-Dz_wIE6Ahxo3MOzb3GUwtxI82se_4h7-WDI-GPMyKuhoqRCq3aqSbWDYgFgmz41P8gCT2iyz9Xb56dArX6UJ-LCuCkMbioNGBN8ZN1Pr3peek4objPlik5jBt4l0s10o2CaqwcUSglZLMlImgH_BQ4cZIxnjoPUAT6zmw6R9Vg9f4LWcVAYFBxj2v1xMrkkLtvaX7X8MG2PlYTCTJzt_brOiuD9wqWXfys_lsf5SvaukZTuuClYGsvpMtetsFLOA8TF3Hc-yl8w7RTXJgD4ymuk8CfMrKC_j4-t8lg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9d52e5f01.mp4?token=sbiBNHCXP6k946SgWMkbOJLzRIqzV8RC5sqm3jOEnsAiv_W-Dz_wIE6Ahxo3MOzb3GUwtxI82se_4h7-WDI-GPMyKuhoqRCq3aqSbWDYgFgmz41P8gCT2iyz9Xb56dArX6UJ-LCuCkMbioNGBN8ZN1Pr3peek4objPlik5jBt4l0s10o2CaqwcUSglZLMlImgH_BQ4cZIxnjoPUAT6zmw6R9Vg9f4LWcVAYFBxj2v1xMrkkLtvaX7X8MG2PlYTCTJzt_brOiuD9wqWXfys_lsf5SvaukZTuuClYGsvpMtetsFLOA8TF3Hc-yl8w7RTXJgD4ymuk8CfMrKC_j4-t8lg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
أبناء العراق يشاركون في مراسيم تشييع قائد الثورة الإسلامية الشهيد بالعاصمة طهران.</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/81146" target="_blank">📅 06:25 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81145">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1119c62728.mp4?token=Xm4Fs5wP-RRCrujjSXEhSlmmEI5k6RMtDbw6_fUzIOOM9JsFfYNB3AGc771ffUlE6FMIppD09Tp52zJHAApII0wtTNlHeQ43xE4_-Ywk81P66sbMMj-stgLfsber9odVe79tBZumP1Fb5ei-6ohfgUil6m05M42c3depTa4k5anmhzc-_rWUYrx8Qhes-Yr2QbFF306kJvssLAXvYdQFxLlijEXiUrdWF0Pn9g_pll8eeu-f0qyBF-1JZetylehWjW9UB-dUjPrJ3fvN8am0v73u6RvAon0Rp4f7vJlTTQHXs9fiQT3isWPiYU7zkzYQzxYdaIUeXqQ9aGGN6NLMfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1119c62728.mp4?token=Xm4Fs5wP-RRCrujjSXEhSlmmEI5k6RMtDbw6_fUzIOOM9JsFfYNB3AGc771ffUlE6FMIppD09Tp52zJHAApII0wtTNlHeQ43xE4_-Ywk81P66sbMMj-stgLfsber9odVe79tBZumP1Fb5ei-6ohfgUil6m05M42c3depTa4k5anmhzc-_rWUYrx8Qhes-Yr2QbFF306kJvssLAXvYdQFxLlijEXiUrdWF0Pn9g_pll8eeu-f0qyBF-1JZetylehWjW9UB-dUjPrJ3fvN8am0v73u6RvAon0Rp4f7vJlTTQHXs9fiQT3isWPiYU7zkzYQzxYdaIUeXqQ9aGGN6NLMfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بدء مراسم تشييع جثمان الإمام الشهيد بشكل رسمي في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/81145" target="_blank">📅 06:18 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81144">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🇮🇷
بدء مراسم تشييع جثمان الإمام الشهيد بشكل رسمي في العاصمة الإيرانية طهران.</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/81144" target="_blank">📅 06:04 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81142">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae73531a85.mp4?token=XdLkCc5ER7hpsXrFL8OvXNAbJ_QaIgFFeK0IcKDdkfaLvph5-uXw4bEAhKtK6WqtFtIl0tB-zVOqXFpU9B4ymPFfX8_XMPVD48OFTcozoSIlwne6W6KEKzXIOeK4gV7d_1WTsbm1lk7F87PxkfqBiJgiebrRlxg1MuLZMPpAqu7r62VbR0f0fmGBjkjf8KmlQOABNQegRBJl39hYZXBuGQ4T5OuKkCBGk8wXcdh9pWUgLtgQ-0sxpQsNFb3bWTAgF9ZTq5K3N2w27cSnNdF9UjeqZa4Lne1UCpbIYdYipTfkAqIWP2SwaNj5KFmnudkY6PWh9sGRA9OKYFjD28OrUmzQwwNvdmsV13N4NGVdfBcKYQpbAjEOQo3MCFy-46oWptuR2kNo4cwbtsDypY_6tPdyV8lcdBfsNGV55RvnlFzct4VvcH4ix_vtGZsx4pnWa0D83XYCXsOoDDU4_JMTko-23hMjS0JQAOiUV1gn7Rae7RLdPsABd9BqKDRMCaiGZ6Theuix9QA0A0lFQCsicOlj6kh7rWljwrhdqUl8y8dhy00hUTy55CfKyGjvHG7jVKUk7VcSEfYtgHTnJrbiw3FeSDWK4oDjhqjY8Jabul2Fjkgpj0SoJZy5yEbKL0go94o9UMrBMKvVne-7o9AjLQUBddV_3KRjKK40JrbR4A8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae73531a85.mp4?token=XdLkCc5ER7hpsXrFL8OvXNAbJ_QaIgFFeK0IcKDdkfaLvph5-uXw4bEAhKtK6WqtFtIl0tB-zVOqXFpU9B4ymPFfX8_XMPVD48OFTcozoSIlwne6W6KEKzXIOeK4gV7d_1WTsbm1lk7F87PxkfqBiJgiebrRlxg1MuLZMPpAqu7r62VbR0f0fmGBjkjf8KmlQOABNQegRBJl39hYZXBuGQ4T5OuKkCBGk8wXcdh9pWUgLtgQ-0sxpQsNFb3bWTAgF9ZTq5K3N2w27cSnNdF9UjeqZa4Lne1UCpbIYdYipTfkAqIWP2SwaNj5KFmnudkY6PWh9sGRA9OKYFjD28OrUmzQwwNvdmsV13N4NGVdfBcKYQpbAjEOQo3MCFy-46oWptuR2kNo4cwbtsDypY_6tPdyV8lcdBfsNGV55RvnlFzct4VvcH4ix_vtGZsx4pnWa0D83XYCXsOoDDU4_JMTko-23hMjS0JQAOiUV1gn7Rae7RLdPsABd9BqKDRMCaiGZ6Theuix9QA0A0lFQCsicOlj6kh7rWljwrhdqUl8y8dhy00hUTy55CfKyGjvHG7jVKUk7VcSEfYtgHTnJrbiw3FeSDWK4oDjhqjY8Jabul2Fjkgpj0SoJZy5yEbKL0go94o9UMrBMKvVne-7o9AjLQUBddV_3KRjKK40JrbR4A8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
بدء الزحف المليوني في العاصمة الإيرانية طهران للمشاركة في مراسيم تشييع الإمام الشهيد السيد علي الخامنئي رضوان الله عليه.</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/81142" target="_blank">📅 05:55 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81141">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcb1cf7016.mp4?token=JodKAG6rdMkz4N3j4N5lw-wnVUMQWma_GWwIg4Drc3LbTqVBkzP_KkTPWaR7nkZ1J8iCelYOcapoAfvylFKw1KgQqogyDLYev0nLtXSyFW1OOvE6_pE0iQu3u8XdnTerRRVk2vo5pbfn4_QtJDtEls356HQfht2VTn8L6lyBREUUvV138Sv-4iqzsszYxno74aVSYNyHA5P03q9fKGs_G58jJLisb6aO2mJXxI3s9xzauswOp1ki0q1D2hKJxgEDF9ITPzxhH9keWHGZMf8sYupfO8Eb_FSzTjuePIEURt-33rRaOoVlBePVhcjDE24Ui4VMnizR0OQ-TlJFWP68KzE_6OR732GLTG2VvoOtzU9j7Eyg6zrcnj9nPhsr97mzGnVpZEqRA621f_lolqCccgtEsxskjhl8IF3yP8G_kRvX7WzX0PIftOzAb3BKogH9XfO48NSgcGCRf6ChO-onEjKo0p6_ITaLGZQ7Qtr_ljtepv1fJwh7OLnCyB7jYs_UCn7DfEhajS6KnoazSM9T4CEB372ndXYOitfOnt4JHaMxi9WPHciNetL7k2uV4eVCUrQ6D2o2_3L8vFYkOlGk436nJFwjv0i3WJBjwcDrGNR3NidqaWYgIimAC2sJMIutp39xY3XwrxkLWYSWLcxfAQCfOJATlesqDlKJklgEiws" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcb1cf7016.mp4?token=JodKAG6rdMkz4N3j4N5lw-wnVUMQWma_GWwIg4Drc3LbTqVBkzP_KkTPWaR7nkZ1J8iCelYOcapoAfvylFKw1KgQqogyDLYev0nLtXSyFW1OOvE6_pE0iQu3u8XdnTerRRVk2vo5pbfn4_QtJDtEls356HQfht2VTn8L6lyBREUUvV138Sv-4iqzsszYxno74aVSYNyHA5P03q9fKGs_G58jJLisb6aO2mJXxI3s9xzauswOp1ki0q1D2hKJxgEDF9ITPzxhH9keWHGZMf8sYupfO8Eb_FSzTjuePIEURt-33rRaOoVlBePVhcjDE24Ui4VMnizR0OQ-TlJFWP68KzE_6OR732GLTG2VvoOtzU9j7Eyg6zrcnj9nPhsr97mzGnVpZEqRA621f_lolqCccgtEsxskjhl8IF3yP8G_kRvX7WzX0PIftOzAb3BKogH9XfO48NSgcGCRf6ChO-onEjKo0p6_ITaLGZQ7Qtr_ljtepv1fJwh7OLnCyB7jYs_UCn7DfEhajS6KnoazSM9T4CEB372ndXYOitfOnt4JHaMxi9WPHciNetL7k2uV4eVCUrQ6D2o2_3L8vFYkOlGk436nJFwjv0i3WJBjwcDrGNR3NidqaWYgIimAC2sJMIutp39xY3XwrxkLWYSWLcxfAQCfOJATlesqDlKJklgEiws" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
أبناء البحرين المظلومين الغيارى الشجعان، يقيمون تشييع رمزي لقائد الثورة الإسلامية الشهيد السيد علي الخامنئي (رضوان الله عليه) رغم التهديد والتضييق من قبل عصابات آل خليفة المتصهينة.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81141" target="_blank">📅 05:31 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81140">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🔻
‏دوي انفجارات عنيفة في كييف وتفعيل الإنذار.</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/81140" target="_blank">📅 02:22 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81139">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">🔻
تنويه صادر عن اللجنة الإعلامية الخاصة بمراسم تشييع آية الله العظمى السيد الشهيد علي الحسيني الخامنئي (قدس سره)
تودّ اللجنة الإعلامية إعلام السادة الإعلاميين بأن توزيع الهويات الخاصة بالتغطية الإعلامية للمراسم سيتم من خلال مركزين معتمدين:
* المركز الأول: العتبة العلوية المقدسة – النجف الأشرف.
* المركز الثاني: العتبة العباسية المقدسة – كربلاء المقدسة.
وسيبدأ توزيع الهويات اعتبارًا من يوم غد، ابتداءً من الساعة 12:00 ظهرًا، لذا نرجو من الجميع أخذ ذلك بعين الاعتبار.
شاكرين تعاونكم.
#المديرية_العامة_للإعلام</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/81139" target="_blank">📅 00:57 · 15 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81137">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0193183dd9.mp4?token=Xgz-v4ZTsAdShIC8NsntWI0QP0XZXpUE2Nfj0tfZoS2-AGTacYupZdf4w_8VMjNpADHNkxPINZ_gnxyfRT4wL1uElT_5lK-JKqq5X3FIeLKtG3k5ywMrqBsZmBX8ehvahJFYn9ztK6_FAqxezSkYgXzQX8IRPXtfvSwm187xqjENfshYsuZzimxdTUzU85BRqw3Y57-rqY4_kZxMTdsXWL1iA-iOpoZG6JvqPJE8St16s4OqNkLE0D75I08V1dlg6vyJ-5V2M5DGC04su8oCS4IapdRspHtTLHDSi8cJJjMPrdeNjgIsleQ2LlMnIAKH_iMALtboDTh_3J03JyYjYA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0193183dd9.mp4?token=Xgz-v4ZTsAdShIC8NsntWI0QP0XZXpUE2Nfj0tfZoS2-AGTacYupZdf4w_8VMjNpADHNkxPINZ_gnxyfRT4wL1uElT_5lK-JKqq5X3FIeLKtG3k5ywMrqBsZmBX8ehvahJFYn9ztK6_FAqxezSkYgXzQX8IRPXtfvSwm187xqjENfshYsuZzimxdTUzU85BRqw3Y57-rqY4_kZxMTdsXWL1iA-iOpoZG6JvqPJE8St16s4OqNkLE0D75I08V1dlg6vyJ-5V2M5DGC04su8oCS4IapdRspHtTLHDSi8cJJjMPrdeNjgIsleQ2LlMnIAKH_iMALtboDTh_3J03JyYjYA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إرسال مدرعات عديدة برفقة الطيران المروحي إلى قرية غاردا راش في محافظة أربيل شمال العراق استعداداً لبدء المواجهة في تمام الساعة 8 مساءً.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/81137" target="_blank">📅 23:29 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81136">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3defccdf92.mp4?token=txA3tztBHAhcY5IU42UH_z1gUfDmNXCr6vhtsrL3qywMbbalIDw8Xh43Yjmcq-XclGUkKDf0KLWkUbimsmWA_wQ0uoEt1qPXi6aFsdagWXgyHRoj6m7u7LF4n-L4KOOXhlvtaYk54PXpR12YFmReP7F0VTdVerILtphDYpepOxOm6mNIQaqHHGBcPWQI9jOnGBg0zAZJzwcXPopaqvoWPuSkvDTjwTwFPGNKY1fePISmSFkWWzckil7A6wLEDEzsW0kWAed6odqbeNFp4PJhDLNkO2MyBBcC9w2EDid8xl7p0mPz4lsGzGmMuAERSRz-08Aw_h0rJwh5Wt5Z9k8QkQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3defccdf92.mp4?token=txA3tztBHAhcY5IU42UH_z1gUfDmNXCr6vhtsrL3qywMbbalIDw8Xh43Yjmcq-XclGUkKDf0KLWkUbimsmWA_wQ0uoEt1qPXi6aFsdagWXgyHRoj6m7u7LF4n-L4KOOXhlvtaYk54PXpR12YFmReP7F0VTdVerILtphDYpepOxOm6mNIQaqHHGBcPWQI9jOnGBg0zAZJzwcXPopaqvoWPuSkvDTjwTwFPGNKY1fePISmSFkWWzckil7A6wLEDEzsW0kWAed6odqbeNFp4PJhDLNkO2MyBBcC9w2EDid8xl7p0mPz4lsGzGmMuAERSRz-08Aw_h0rJwh5Wt5Z9k8QkQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
في ظل انشغال الجولاني بإثارة الجدل حول تدخله لقتال حزب الله في لبنان دفاعاً عن إسرائيل ؛ جيش الاحتلال الإسرائيلي ينشر مشاهد لعبور مستوطنين صهاينة إلى محافظة درعا التي تعتبر واقعة تحت سيطرة حكومة الجولاني.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/81136" target="_blank">📅 23:04 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81135">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔻
انتهاء مراسم التوديع للشهيد الأممي السيد علي خامنئي وأفرادٌ من عائلته في طهران</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/naya_foriraq/81135" target="_blank">📅 22:55 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81134">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">📰
‏بلومبيرغ عن تقييمات عسكرية غربية: التهديد في مضيق هرمز لا يزال كبيرا</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/81134" target="_blank">📅 22:53 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81133">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🇸🇾
دوي انفجارات في مدينة أريحا بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/81133" target="_blank">📅 22:41 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81132">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🇸🇾
دوي انفجارات في مدينة أريحا بريف محافظة إدلب السورية.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/81132" target="_blank">📅 22:38 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81131">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3f8442434.mp4?token=YXNFZfZLUg_MTx6FSVG94E8e-aZFImhMdWilSYiPtb5NIeDtCtQvVogZbP5t07FH3rH2n3nkQD-Tdaz2hNEHmY2G6TnL7uVjLrigLT6qfltAiiucpGxpch_H_BrvfwSJQ3NsMVIUKaeer3OVrduEZkqjfyXaUozFQ__wCvrvovT8K1_epyti6jfySNOD7dD9gy5PwZuyMtOoEg-c1YPgHxPfYCqCF2C38DUfiUrlKY2xr6eRYuEqxejN7I5WDpHm8ARwFHj_XC1vgbIkRXIfkhtvF81xMMFWRBn0sj7tVHlm_eyq23DWmDWpHY4HbT8h-frRlVJyANBUUz6RsLadmADP0AZMEaPkN0A2Lxb4osrxhdqml71DFczqJNdR8eSgdM18zagtRAbVul06WY3wGjWdA40qHAxti1Co5sd0Y7iPlW8c6m79UnLT-1moPPxONnBQQbaxPgQEjVC9stZR1IgqtmQKZUXSd33taAWtelDGPMpx7TOUc1MxVZJfVm2sr3D_KThs7itEiToVuZw5_Xp8usQDhPu6mObI1rcuz_ZrjndZ0f8HJcnOgAEB_479HVvPnNIjNX4A-bjTO4n0cdDPrADM-B_XdYaSW5gUxMrYHsFMceBQCQh-wioRSdHgB6CYpC5oUp3TdFwV_WXZBagoSVASNwSaw6W9tMB2q-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3f8442434.mp4?token=YXNFZfZLUg_MTx6FSVG94E8e-aZFImhMdWilSYiPtb5NIeDtCtQvVogZbP5t07FH3rH2n3nkQD-Tdaz2hNEHmY2G6TnL7uVjLrigLT6qfltAiiucpGxpch_H_BrvfwSJQ3NsMVIUKaeer3OVrduEZkqjfyXaUozFQ__wCvrvovT8K1_epyti6jfySNOD7dD9gy5PwZuyMtOoEg-c1YPgHxPfYCqCF2C38DUfiUrlKY2xr6eRYuEqxejN7I5WDpHm8ARwFHj_XC1vgbIkRXIfkhtvF81xMMFWRBn0sj7tVHlm_eyq23DWmDWpHY4HbT8h-frRlVJyANBUUz6RsLadmADP0AZMEaPkN0A2Lxb4osrxhdqml71DFczqJNdR8eSgdM18zagtRAbVul06WY3wGjWdA40qHAxti1Co5sd0Y7iPlW8c6m79UnLT-1moPPxONnBQQbaxPgQEjVC9stZR1IgqtmQKZUXSd33taAWtelDGPMpx7TOUc1MxVZJfVm2sr3D_KThs7itEiToVuZw5_Xp8usQDhPu6mObI1rcuz_ZrjndZ0f8HJcnOgAEB_479HVvPnNIjNX4A-bjTO4n0cdDPrADM-B_XdYaSW5gUxMrYHsFMceBQCQh-wioRSdHgB6CYpC5oUp3TdFwV_WXZBagoSVASNwSaw6W9tMB2q-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إجلاء 11 عاملاً كانوا محاصرين داخل المجمع التجاري الذي التهمته النيران في شارع الظلال وسط العاصمة بغداد ولا تزال النيران مشتعلة وممتدة إلى الأبنية المجاورة.</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/81131" target="_blank">📅 22:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81130">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔻
قائد عمليات الفرات الأوسط في الحشد الشعبي اللواء علي الحمداني يعلن استكمال الاستعدادات الأمنية والخدمية الخاصة بمراسم تشييع شهيد الامة السيد علي الخامنئي (قدس سره)</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/81130" target="_blank">📅 22:26 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81129">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5fd87060b8.mp4?token=cer60eI3fie07wnX3hHO_p9za5E0AmL03FEHAOYaBIEFLgtt2HG8pzD5Eo4t7aeB-qxG0bZZVXCaMTmn-rjsIjcpXgBiiDxeBrE8Enjx9GPT1NpC5mMrNCBD3mc5PSrRD96oB4rYqW_UBZr-XXCaU3ktaSJ43jZhX_D4NcDRffcEKK_D0MIUU2T4GcnU07ON3Vom6y0Zf10fN-Oxbi5vtybC_AeF-gCKiSSo0UJ3NERPyXXmR5wbPYM0rZ1xWDw2W57GdYua9JiK-JaCoZ1daqgNtysSL0rjqeEmllNJeS5t786biStFKNnReA8g7CDMJhsi76BZY473pfjnB2cTf2E-r6C2XWWbcp7vVI-ByCYo8EgQLKZb_t5x7-RkowHRNDaesho4NL0HO2C53Vny7TxgetWGwSinxv19bMMJ1G388zvtzIYXL-SP9M-ihggC3Sj3wH0L_7dW7IP_afQsEIhr9XCa6K0fsWZ05dcxx6YNWtwvTESkbdUsaU8SA84zR_EE57oDTY8xMsktrLLX1oXQIYtGrHErfO1yx3w6GycB7HnZr3IXnRywY51OGt7rCSpVX9lGOCBu4-G9vl7w3bNp02SZF6OpIAKZCUNCrfgpNp4Py-YHnJ_VH5c5tCdHhloKGOXPaz5l60-PkVu0bHo2JKTjSoe2CV9xqr3-0wc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5fd87060b8.mp4?token=cer60eI3fie07wnX3hHO_p9za5E0AmL03FEHAOYaBIEFLgtt2HG8pzD5Eo4t7aeB-qxG0bZZVXCaMTmn-rjsIjcpXgBiiDxeBrE8Enjx9GPT1NpC5mMrNCBD3mc5PSrRD96oB4rYqW_UBZr-XXCaU3ktaSJ43jZhX_D4NcDRffcEKK_D0MIUU2T4GcnU07ON3Vom6y0Zf10fN-Oxbi5vtybC_AeF-gCKiSSo0UJ3NERPyXXmR5wbPYM0rZ1xWDw2W57GdYua9JiK-JaCoZ1daqgNtysSL0rjqeEmllNJeS5t786biStFKNnReA8g7CDMJhsi76BZY473pfjnB2cTf2E-r6C2XWWbcp7vVI-ByCYo8EgQLKZb_t5x7-RkowHRNDaesho4NL0HO2C53Vny7TxgetWGwSinxv19bMMJ1G388zvtzIYXL-SP9M-ihggC3Sj3wH0L_7dW7IP_afQsEIhr9XCa6K0fsWZ05dcxx6YNWtwvTESkbdUsaU8SA84zR_EE57oDTY8xMsktrLLX1oXQIYtGrHErfO1yx3w6GycB7HnZr3IXnRywY51OGt7rCSpVX9lGOCBu4-G9vl7w3bNp02SZF6OpIAKZCUNCrfgpNp4Py-YHnJ_VH5c5tCdHhloKGOXPaz5l60-PkVu0bHo2JKTjSoe2CV9xqr3-0wc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أهالي درعا جنوب سوريا يعلنون تشكيل حركة ردع الاحتلال بسبب الاعتداءات المتكررة عليهم من قبل جيش الاحتلال وصمت الجولاني المتكرر وتجاهله لما يحدث من احتلال للأراضي السورية.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/81129" target="_blank">📅 22:18 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81128">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
هيئة الحشد الشعبي تنشر قوموا لله يا أبناء العراق المشهود.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/81128" target="_blank">📅 22:06 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81126">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8f3dd24b03.mp4?token=qxVXJk94FPoUbltYaaDaQ_kCZwp0r0R_RdJcDCD8UTRiS2MqIymvH9ZT1ofpBFCGLnROVc6sHobH1nBvtQ1TMy5ysRvpRTDZhc3e1eWnm8CUvK6PQad4vGrGcrq90zXyeM6tdyOMc_3HvMXG1gXsC8QMgLjMzTFGGr2zdRMKBPmC0NHbPJOYRaevTwc1kW8l8LkcRxiGmmcpPkRhdL4t1OFdEgIOOf-ID-R7WwawDB3aZnqOwlVFf_HBLJ5tUap7JSLyo3BYWp8m4X98Dmjhq8LR0JY6a7JIoOE1e0G7c4wX_zTjFXQ85622RGGUoCQdPx7CRg3qRd7dbXF8fwodQ649tJQHkvsRHRdOtHvNHYix5DAms68WpPqHktaeMrHN_sp0N7xS3MREJNSUn6vTVMOMsv7TL74XBpqgj7NM-hyAb8y1cleA0TBdI7s0pHkPUZHOw9K5mW5Pwn1PRattTafZ5FWbXbEMSPMPB2XzUwyj27iBIRPrPkRi7bjVRgBKMfKTFiUJDNk_NMcvdTzfSd_TmcLB6w-Qw3ZavEsC2nwr5spaP0AQJrngL2bLnat_6IHiWSiNF383II46AL45kEa_vF7GkVpTO4zec9dFJjGBDqQWDCz4bGKORe-VDoEbGCfdiyyxsFGHctljr-UCOGFKdJ13R1Aahc9NXQ_iApY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8f3dd24b03.mp4?token=qxVXJk94FPoUbltYaaDaQ_kCZwp0r0R_RdJcDCD8UTRiS2MqIymvH9ZT1ofpBFCGLnROVc6sHobH1nBvtQ1TMy5ysRvpRTDZhc3e1eWnm8CUvK6PQad4vGrGcrq90zXyeM6tdyOMc_3HvMXG1gXsC8QMgLjMzTFGGr2zdRMKBPmC0NHbPJOYRaevTwc1kW8l8LkcRxiGmmcpPkRhdL4t1OFdEgIOOf-ID-R7WwawDB3aZnqOwlVFf_HBLJ5tUap7JSLyo3BYWp8m4X98Dmjhq8LR0JY6a7JIoOE1e0G7c4wX_zTjFXQ85622RGGUoCQdPx7CRg3qRd7dbXF8fwodQ649tJQHkvsRHRdOtHvNHYix5DAms68WpPqHktaeMrHN_sp0N7xS3MREJNSUn6vTVMOMsv7TL74XBpqgj7NM-hyAb8y1cleA0TBdI7s0pHkPUZHOw9K5mW5Pwn1PRattTafZ5FWbXbEMSPMPB2XzUwyj27iBIRPrPkRi7bjVRgBKMfKTFiUJDNk_NMcvdTzfSd_TmcLB6w-Qw3ZavEsC2nwr5spaP0AQJrngL2bLnat_6IHiWSiNF383II46AL45kEa_vF7GkVpTO4zec9dFJjGBDqQWDCz4bGKORe-VDoEbGCfdiyyxsFGHctljr-UCOGFKdJ13R1Aahc9NXQ_iApY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇵
أجرت جمهورية كوريا الديمقراطية الشعبية العظمى اختبارًا لإطلاق 12 صاروخًا كروز طويل المدى قادرًا على حمل رؤوس نووية بشكل متتابع من إحدى مدمراتها الجديدة من فئة Choe Hyon - وهي أول مدمرات حديثة موجهة بالصواريخ في البحرية الكورية ؛</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/81126" target="_blank">📅 21:40 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81125">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/49d8b18868.mp4?token=u7qqXvpaLokyese1t6hVjOd0BT9lxgPn7-BmKPVRQk-J3catvMI4696P_dCCGDQNqedwDzHvPZGsGVqAVfdtXe4ZFVw3uW_SWbBXifGDRcKHt8mrzWufHL4NDBG-F3Lu9G6ZjUWB7KEi9kG1CoJ91rC_8ybLfm0Kc0SEGSHGykyXo3dVdqtIkSZM1s8LXOz4L8D0MmTWD84gma8TIWbF9w8iJuuT0P9AQVqu7jcoHV85icgX2Ui2Uax6NDI4WYdV_V-Py5nN9gwojpBZqTfWPfyGeyVhs2pRwLqZFvK2BoEvZ9_WQPaP4jPOKls1vhMWl4i5whrjM02ZBFYrPlZjBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/49d8b18868.mp4?token=u7qqXvpaLokyese1t6hVjOd0BT9lxgPn7-BmKPVRQk-J3catvMI4696P_dCCGDQNqedwDzHvPZGsGVqAVfdtXe4ZFVw3uW_SWbBXifGDRcKHt8mrzWufHL4NDBG-F3Lu9G6ZjUWB7KEi9kG1CoJ91rC_8ybLfm0Kc0SEGSHGykyXo3dVdqtIkSZM1s8LXOz4L8D0MmTWD84gma8TIWbF9w8iJuuT0P9AQVqu7jcoHV85icgX2Ui2Uax6NDI4WYdV_V-Py5nN9gwojpBZqTfWPfyGeyVhs2pRwLqZFvK2BoEvZ9_WQPaP4jPOKls1vhMWl4i5whrjM02ZBFYrPlZjBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
اندلاع اشتباك عنيفة بين حراس أحد أعضاء مجلس محافظة كركوك عن فصيل الجبهة التركمانية وحراس مستشفى وطن بمحافظة كركوك ؛ ما أسفر عن إصابة اثنين من حراس المستشفى بجروح خطيرة.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/81125" target="_blank">📅 21:35 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81124">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60d7f0de29.mp4?token=s7TAKl9_UvWOTMMK3GWwcXHqNHZUouDXWnffn_O-8CnOsj_Ljv50nefjnVM_Fce3PnwdtwIwgWlTOZOIrOT3XVXcypcZTd9SP3HMUPuwQ-islrvYrP4Y9AzzqvXWC1NcMeoNy_tjwmRjKlG_xX6LfMurhKT4yfYhUmvL5t4TRre0Wl7GhBmGm4o9y-9DK0fwe2CyHmPge5Hu3vweN8n-eDDVpCjrhb5e7SUr3x80M1UknpfZKd2y-Ag490vJp8L8_nys1OCoh8EfD3Af9URgk7UmKpVCyINCsAD21-ECDhHj4NnUnalRWU5lb06TsjZxAxAHUj5gbVy77O6DnHfYqg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60d7f0de29.mp4?token=s7TAKl9_UvWOTMMK3GWwcXHqNHZUouDXWnffn_O-8CnOsj_Ljv50nefjnVM_Fce3PnwdtwIwgWlTOZOIrOT3XVXcypcZTd9SP3HMUPuwQ-islrvYrP4Y9AzzqvXWC1NcMeoNy_tjwmRjKlG_xX6LfMurhKT4yfYhUmvL5t4TRre0Wl7GhBmGm4o9y-9DK0fwe2CyHmPge5Hu3vweN8n-eDDVpCjrhb5e7SUr3x80M1UknpfZKd2y-Ag490vJp8L8_nys1OCoh8EfD3Af9URgk7UmKpVCyINCsAD21-ECDhHj4NnUnalRWU5lb06TsjZxAxAHUj5gbVy77O6DnHfYqg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇾
أقدم عاصمة في التاريخ تتحول لساحة معركة بعد سيطرة نظام الجولاني الذي كانت أبرز صفاته الإرهاب والفوضى حيث شهدت ساحة المرجة في دمشق اشتباكات بين مسلحي إدلب وقرباط دير الزور إثر خلافات داخلية بين عصابات الجولاني.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/81124" target="_blank">📅 21:31 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81123">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=IXbsyI7nUy2hnJccBROD3tVra7XBMxiEvf_IukamPmrznuIBdT3kJTWY33aAlzVQtHMxNXb1Jykrl6shGEXJpL2OoooBfAU2t71gXvMhGsTXkjYBGqz-T5ilV44jeZLXkVcp2SbHP_tYAk2iuErOt2LcyKo5OuzjXHELyS_PTHuPcBQ3odkOTPJqn2C0jM41nlHVeTNYE9LE3XdQLpxn1lGukqZyTlvwOfXdeuv6x6O69DusyL398y_SO2p_0741fNmoIQjzo4A7BxkOAw92pxEqWOBSEMKHUVC4Sl1qQRFu1OaX6OBS8BqWmwY8Iy2LV_q7UU99nPc2wH0CSxdUjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4285da2f6b.mp4?token=IXbsyI7nUy2hnJccBROD3tVra7XBMxiEvf_IukamPmrznuIBdT3kJTWY33aAlzVQtHMxNXb1Jykrl6shGEXJpL2OoooBfAU2t71gXvMhGsTXkjYBGqz-T5ilV44jeZLXkVcp2SbHP_tYAk2iuErOt2LcyKo5OuzjXHELyS_PTHuPcBQ3odkOTPJqn2C0jM41nlHVeTNYE9LE3XdQLpxn1lGukqZyTlvwOfXdeuv6x6O69DusyL398y_SO2p_0741fNmoIQjzo4A7BxkOAw92pxEqWOBSEMKHUVC4Sl1qQRFu1OaX6OBS8BqWmwY8Iy2LV_q7UU99nPc2wH0CSxdUjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هنا طهران حيث رايات كتائب حزب الله تشارك في الوداع الاخير
مشاركة واهتمام واسع من قبل الحكومة الإيرانية بوفد التشكيل العراقي الأكثر ايلاما على الاحتلال الأمريكي في حرب رمضان</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/81123" target="_blank">📅 21:05 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81122">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=tghbBrvgtAYtP3SX1kvE2y-0YkCoBsUwZ1QCqM2NWwpt5tYZvGtSVQwXLSwC8QEILysfcji-_G13JlLn0Q_-2KxnTix0-nNfY4g50YorEXflowPzzomwQmsogqhthYYOsFcgxuz_MY2nbBGsOEaJvOGZKdZob4Aexsntp102ydaweW96sPAJ24gV6mHFKHLuRJkqO3rqO9kK6Awcg1vzBWpHW8krbbWeY_NoywKrESAIFe9KEzuRJY8cuj5oAp6JJw7Kx1E9srz3NBsXjWLsuR342tJvEbNqYEyr4KctJWD8s0BqVVov65C0YDttxhuIEzRnNbe1hC78_hcrc709Jg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f731e28c.mp4?token=tghbBrvgtAYtP3SX1kvE2y-0YkCoBsUwZ1QCqM2NWwpt5tYZvGtSVQwXLSwC8QEILysfcji-_G13JlLn0Q_-2KxnTix0-nNfY4g50YorEXflowPzzomwQmsogqhthYYOsFcgxuz_MY2nbBGsOEaJvOGZKdZob4Aexsntp102ydaweW96sPAJ24gV6mHFKHLuRJkqO3rqO9kK6Awcg1vzBWpHW8krbbWeY_NoywKrESAIFe9KEzuRJY8cuj5oAp6JJw7Kx1E9srz3NBsXjWLsuR342tJvEbNqYEyr4KctJWD8s0BqVVov65C0YDttxhuIEzRnNbe1hC78_hcrc709Jg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
إجلاء 11 عاملاً كانوا محاصرين داخل المجمع التجاري الذي التهمته النيران في شارع الظلال وسط العاصمة بغداد ولا تزال النيران مشتعلة وممتدة إلى الأبنية المجاورة.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81122" target="_blank">📅 20:59 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81121">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=W3Fznb7QdaBfAmkn1tL0SY7nYcdMElvxxQRoD8nBfOhwTNoK78m_1L1lJ1LGqRQTIbjFEVVcblKkamI3brcwOGP6BeVypXCy9-z-4js7-zGaZyS6Qz77HF4jidQxP11PLGcyMinPjPOEEQkBNyCpNAzrvrvmu95nGd9wSjRHyjgruwibPbA2IiAk7z7Rb7kdHyUhb3fiRxMlEmYy8Oj0p85HoVj_iYnHkJcfduO_9_DPSZyIdKm52G8WwstM0NdGSiqp_9EovPcELE7oMQM4LfWlvHjVArS7mRd6voY1rQV1ueXgJWTcgViHL4ZgtYnvd-rmI02KuCKbe3NwTVzoCQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/700c45fc9e.mp4?token=W3Fznb7QdaBfAmkn1tL0SY7nYcdMElvxxQRoD8nBfOhwTNoK78m_1L1lJ1LGqRQTIbjFEVVcblKkamI3brcwOGP6BeVypXCy9-z-4js7-zGaZyS6Qz77HF4jidQxP11PLGcyMinPjPOEEQkBNyCpNAzrvrvmu95nGd9wSjRHyjgruwibPbA2IiAk7z7Rb7kdHyUhb3fiRxMlEmYy8Oj0p85HoVj_iYnHkJcfduO_9_DPSZyIdKm52G8WwstM0NdGSiqp_9EovPcELE7oMQM4LfWlvHjVArS7mRd6voY1rQV1ueXgJWTcgViHL4ZgtYnvd-rmI02KuCKbe3NwTVzoCQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زلم ابو حسين
الرايات الصفراء الراية الأقرب لقلب الحاج سليماني والسيد الولي تشارك بالتشيع الرسمي في الوداع الاخير</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/81121" target="_blank">📅 20:57 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81120">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromابو الاء الولائي- القناة الرسمية</strong></div>
<div class="tg-text">كلمة الامين العام لكتائب سيد الشهداء الحاج ابو الاء الولائي (دام عزه) في رسالة الى الشعب العراقي العظيم.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/81120" target="_blank">📅 20:54 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81119">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WEjDfQhW-_-XrBai1QRiJkP5lHMOSP3G6n8dnzENwzJhYLbBDdFU9U8A-bGEa8AV2yA9LQM8X6L2M4z8uiQNGOd-yFP7tG6keTxJfXPHfefIPnqPJ0zxfhyozYXiacsyJ96KQQQMGI69G0CcBpwvtnZSHfjYdLKXvNM2rvzTiyZcQykA2t3Cl8BCZyLkQA7ec71vx_aWpo4WxKwxz2PpDYOy90BtS_lsVoUAZoInspCixXX3qjkX23kUZN1zhcj3m5xxjieccshXT1j9wHefPlA-KfVDiceSK-MSlvLchsh5VSUqx1uMBLCA_5ZXg2z1hDFA9-5BTzyKiefN6bZTyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب: شكرًا لك FIFA على فعل ما هو صحيح، وإلغاء ظلم كبير!
علماً أن الـ FIFA قد ألغت البطاقة الحمراء لمهاجم المنتخب الأمريكي ورفعت الإيقاف عنه قبل مباراته المقبلة في المونديال!</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81119" target="_blank">📅 20:52 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81118">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruIUJoWaJjcsZtVWUCQVpZWA3rzi9zW8ulumj2AjxqcHQp2E7Vb71oBEK413aEMfaxODfRjRFQmJBowpLFx__EsTy2knum361-dlcyd65RtUHiq6Qw1Jq1kz3clwkugohld17kwI7nChos20ZOSvBruRaLyFLYvXQr7foXf2qGaD7Vi3ehp_7lSqVB9JlDmttdWHWh5P5HQdRSeVlESuncOxY-bt3j8f74EsZC5wn8lgTZHWV5w2qIyClzpPe5N_O5yCWn021PEUUiEi0K9BvwnMziHVsprZ8p6glllULSECKZtIhYzYFtDQWKoC_S1LgcsqYC5vUI_Htf58UkiAWEIY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/77100992bb.mp4?token=JU1Q_Ktuahk2r0NFlgo8GmOspRXxjisIBRA_RGA5OoaAxUpGAW-chsle1r83fhA0zwwofv7ordBDq7Etp8wvhOQNhgNe-G30WzoTzV6HKB58JCsloFcgCq7KdxPqvJhKrRSVnj3iiyXiMTQyoisJ5UCQhEiXGjnznT9Xr7L_eLdZFKpY56omibYXaDI54CtgSSkWlY9kiHuOaPMNwoI5TID9SWDhzbAPBec69vCrxFJXQYhqkUUtEFTfkJE7Fg0tBFEh7DB1EXfpqIWADs4Yn5PrttjQ_FY5GChghSutkY8-BZ7ZahneetBCOOXQaI9NcpVeb1JRxS1fuuKshUSruIUJoWaJjcsZtVWUCQVpZWA3rzi9zW8ulumj2AjxqcHQp2E7Vb71oBEK413aEMfaxODfRjRFQmJBowpLFx__EsTy2knum361-dlcyd65RtUHiq6Qw1Jq1kz3clwkugohld17kwI7nChos20ZOSvBruRaLyFLYvXQr7foXf2qGaD7Vi3ehp_7lSqVB9JlDmttdWHWh5P5HQdRSeVlESuncOxY-bt3j8f74EsZC5wn8lgTZHWV5w2qIyClzpPe5N_O5yCWn021PEUUiEi0K9BvwnMziHVsprZ8p6glllULSECKZtIhYzYFtDQWKoC_S1LgcsqYC5vUI_Htf58UkiAWEIY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
أنباء عن محاصرة عدد من العمال داخل المبنى المحترق وسط محاولات كبيرة للدفاع المدني لإخراجهم.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/81118" target="_blank">📅 20:51 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81117">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">‏البيت الأبيض: ترمب سيلتقي الجولاني على هامش قمة الناتو</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/81117" target="_blank">📅 20:39 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81116">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=IWrjwVmVivvvzS73oT7e0CMw7nMfDCVG4rlwPpWJ4kg50LsZYAimsytE6HlD6ltqX8dgOgtqzx83DIbFD23nq-I1LvcHTYpA_Fw9pZwPVxs7BLbE_PoFvXvOF9O-Z_uR0fbDNw7Q9JBu38rnCIcCf-NF3r_J0azIko_6NtM397i6f13T-0HoJKsRjvtm1QbvdWvgTxzZ2ElIMA0Zr0-TKOBV-vlGjhx6C7CTYSl6d_tHCsoBYLniOQ5u8TkyQyPRq7mJTR4lD-22BxJcqu_i5DJTgd6YhXAIq40HfKFYKotzJAxwfoDlnCRB1qn9VY4AN1hRVFQhb941CIEE1tRq3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6de9f8037.mp4?token=IWrjwVmVivvvzS73oT7e0CMw7nMfDCVG4rlwPpWJ4kg50LsZYAimsytE6HlD6ltqX8dgOgtqzx83DIbFD23nq-I1LvcHTYpA_Fw9pZwPVxs7BLbE_PoFvXvOF9O-Z_uR0fbDNw7Q9JBu38rnCIcCf-NF3r_J0azIko_6NtM397i6f13T-0HoJKsRjvtm1QbvdWvgTxzZ2ElIMA0Zr0-TKOBV-vlGjhx6C7CTYSl6d_tHCsoBYLniOQ5u8TkyQyPRq7mJTR4lD-22BxJcqu_i5DJTgd6YhXAIq40HfKFYKotzJAxwfoDlnCRB1qn9VY4AN1hRVFQhb941CIEE1tRq3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
الحريق يمتد ليشمل الأبنية المجاورة للمجمع التجاري في العاصمة بغداد والبدء بإجلاء السكان من منازلهم.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/81116" target="_blank">📅 20:28 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81115">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=VrYkJFt17OrSA16W-TR8Q8J9trKlh9KwOnUY9Yt4QHncXBoC5QgFHsPzd7-FeOk2PeMoAxYX_6Vv3hWoLe7iXul6T6UHtuPlky9Shkn53_we-F-TmFyiEX4QQImMWvTof4TO0CHLWO7wZnTjkqUqM6gbz2OhNVwlKMdAcv3XsbaCGraAF6nHCxN_tNaXBon1TWom_n383FcmgvezGGzJsDh8K6zOnPW_Ga81mp2pPzugmhwNy9ZCtbFGmAjZ3vSASlpj8lyMmE1kh_GMq-i9X2yXPKdaTfvM-yUF6gXwqsdgabl4UtM8_cKWakMMLML9UR6daqv5GKVpkhy2winBGQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6af75ae984.mp4?token=VrYkJFt17OrSA16W-TR8Q8J9trKlh9KwOnUY9Yt4QHncXBoC5QgFHsPzd7-FeOk2PeMoAxYX_6Vv3hWoLe7iXul6T6UHtuPlky9Shkn53_we-F-TmFyiEX4QQImMWvTof4TO0CHLWO7wZnTjkqUqM6gbz2OhNVwlKMdAcv3XsbaCGraAF6nHCxN_tNaXBon1TWom_n383FcmgvezGGzJsDh8K6zOnPW_Ga81mp2pPzugmhwNy9ZCtbFGmAjZ3vSASlpj8lyMmE1kh_GMq-i9X2yXPKdaTfvM-yUF6gXwqsdgabl4UtM8_cKWakMMLML9UR6daqv5GKVpkhy2winBGQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
حريق شارع الظلال في العاصمة بغداد يخرج عن سيطرة الدفاع المدني ومخاوف كبيرة من انتشار الحريق إلى المنازل المجاورة.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/81115" target="_blank">📅 20:25 · 14 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-81113">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95438bf709.mp4?token=s8vjyLRpg6CZs8tqJ1WsHar58c157A5s1YrwHP53lPyY_Kb1R13TC-4qmjaQF8tqxqavrttaZeZ8TnuAP_OwF2CM_fNjt-sYixIjhrmFZxxV80BwgwuVD1k6hcJ-50OIK34iR4sbOrp226LPYFjx0tWG-z7l3bg3Wz-zz93aXdW9Hletq2opfra_JBGARz3GRJXHyeLCa6b40pc7BuMmsR2Zx507f7IdzgMcXbDfXXyXtCDr6up681jAbPtgr67jvoPTdzuIl5qviTBrScwh_F6fehABz7s0CDpLjHLF_BJuVQBpiGLn-WTowuMcS3SKjpGgVY5nriGnThe7lGqORw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95438bf709.mp4?token=s8vjyLRpg6CZs8tqJ1WsHar58c157A5s1YrwHP53lPyY_Kb1R13TC-4qmjaQF8tqxqavrttaZeZ8TnuAP_OwF2CM_fNjt-sYixIjhrmFZxxV80BwgwuVD1k6hcJ-50OIK34iR4sbOrp226LPYFjx0tWG-z7l3bg3Wz-zz93aXdW9Hletq2opfra_JBGARz3GRJXHyeLCa6b40pc7BuMmsR2Zx507f7IdzgMcXbDfXXyXtCDr6up681jAbPtgr67jvoPTdzuIl5qviTBrScwh_F6fehABz7s0CDpLjHLF_BJuVQBpiGLn-WTowuMcS3SKjpGgVY5nriGnThe7lGqORw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
استمرار محاولات إخماد الحريق الضخم الذي التهم المجمع التجاري في شارع الظلال بالعاصمة بغداد.</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/81113" target="_blank">📅 20:16 · 14 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
