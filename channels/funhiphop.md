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
<img src="https://cdn4.telesco.pe/file/AJ2XhDDThWmJuBJd-frbLfzyTFzGQY7w06R3rlkrgt5o1HFceCdeHzk_t1WEqU7VDYhMvDg2dk6iaq5McxQd0_fnWm-XpnLFLznzm6Ctlo9t3-FGUxNlFvdxHBaQ-IV_GZHvK27W0W7OLQ7bnyp3lY0W7HF5aRbNcbOD5YQNAv1gwq5jY5yjg1v5hjvf5HbmVRHiiJrGXh9E7T3Zp5KfINkFnez_J1zAz5CqaSQamhJ-dqFaOro5U9Q7vjwavNJAzF2isDttZemMgjaUJxndVByGkVVmyAS3Gvp5kKbd-3RbvaG27KXTJj69AllDNcnhigZGDf5Fip1021vRq7CSIg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 269K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-07-22 21:34:27</div>
<hr>

<div class="tg-post" id="msg-84843">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">فردا بهترین شو کمدی تاریخ ایران میاد
مهمون قسمت جدید برنامه قیاسی پیمان قاسم‌خانیه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 3.6K · <a href="https://t.me/funhiphop/84843" target="_blank">📅 21:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84842">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/86350e52fe.mp4?token=sP15uNYRc0x0Dy_ROJFTVY20JZGLlRCDxZw-j-0Hpz46Gckm09vEj6_H8idCep-a6a_nIzHedbNcNja0HDShCDvn8fs5-pD-ubLxmESfa9pM5kCtN3oi3-SGomN_FiT7hozIGJKg__EE2R4kkTHpB-xGGqfiOJEKOb1nTO-B70NK7_sVUVSP_lVFSBYeYtAAo9ExqYwng_hPr0iU60DqNjwnVAxS717jH1NK4qpHXMVjRuhVAAmbqiRCVpcGHspAGAgiZg4lBFWoP5U4Ccm-eF1jdBamtAkFhOadFp7d7ZcpNGuSDLmRzr6H7CIrQDo2a_jQ1djXUB00jknO-_wxBwqqasFowoGTEpAa5DnU5R3mqsURa-AhfCW0d7eaZhoxq4ExP7WdvpeU7uU4RXmA9qKZxRIsOXVqdxdlb0ve_xOPr77QSGufoCjvMUMdzl3PHXYwr_YAt5HByjIHhhNGJAF_GIKDersm70b7AI3VIbu6CgyS6svvSTVfT7rrKLhiR0FNwMH3PnKegJz3tn0-doSi2nwfBaaa2zVjbF39aiZOPA0CUCT48GlqbJoFV9pXIVSfTE_y2Wa55b1shOX9TZxP_mqNPMzL0iMiIZqIygpsJHH0fA1V_c-VVNNWml09BavqbGRd5bBZk7UHl4E0fiPAggVvkhzkgvy0Rnz3Hz4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/86350e52fe.mp4?token=sP15uNYRc0x0Dy_ROJFTVY20JZGLlRCDxZw-j-0Hpz46Gckm09vEj6_H8idCep-a6a_nIzHedbNcNja0HDShCDvn8fs5-pD-ubLxmESfa9pM5kCtN3oi3-SGomN_FiT7hozIGJKg__EE2R4kkTHpB-xGGqfiOJEKOb1nTO-B70NK7_sVUVSP_lVFSBYeYtAAo9ExqYwng_hPr0iU60DqNjwnVAxS717jH1NK4qpHXMVjRuhVAAmbqiRCVpcGHspAGAgiZg4lBFWoP5U4Ccm-eF1jdBamtAkFhOadFp7d7ZcpNGuSDLmRzr6H7CIrQDo2a_jQ1djXUB00jknO-_wxBwqqasFowoGTEpAa5DnU5R3mqsURa-AhfCW0d7eaZhoxq4ExP7WdvpeU7uU4RXmA9qKZxRIsOXVqdxdlb0ve_xOPr77QSGufoCjvMUMdzl3PHXYwr_YAt5HByjIHhhNGJAF_GIKDersm70b7AI3VIbu6CgyS6svvSTVfT7rrKLhiR0FNwMH3PnKegJz3tn0-doSi2nwfBaaa2zVjbF39aiZOPA0CUCT48GlqbJoFV9pXIVSfTE_y2Wa55b1shOX9TZxP_mqNPMzL0iMiIZqIygpsJHH0fA1V_c-VVNNWml09BavqbGRd5bBZk7UHl4E0fiPAggVvkhzkgvy0Rnz3Hz4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">داستان های بیرانوند به زبان ژوله.
پ‌ن: به شدت چندش بی مزه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 5.5K · <a href="https://t.me/funhiphop/84842" target="_blank">📅 20:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84841">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/325e9a098a.mp4?token=kz6jJd7iAv5sWihPmEnX4lLHXIKLBN0zNInK1FRhOSdMcV6J7rRv04eWBxGEDItDxKKQXG2y--nfHmfY9yGNBEHF6OT9ZPmRcuoHV1wFfpIDi2HFkMZBAPcj_ov4GN55hD-wFOsXslXWv_B8x39DXhmVgr24TWF-IuLe9BoK6UCII9C7m5Pii0dYaAV-sXM-NvssXX_8RNjIl5FTF2FR3xsbb190IV3Y7EKe_jmFOOkkFaVhIQkN0Mk0n6O4dDLROaPPpXFlvAsiHBaNxKWBCgmN11huKh9tqvI3NJ_EvFJKFOG5ZhhP79_ZaVZFys-uvg9RkF-LUS7Vjmu4DQPUMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/325e9a098a.mp4?token=kz6jJd7iAv5sWihPmEnX4lLHXIKLBN0zNInK1FRhOSdMcV6J7rRv04eWBxGEDItDxKKQXG2y--nfHmfY9yGNBEHF6OT9ZPmRcuoHV1wFfpIDi2HFkMZBAPcj_ov4GN55hD-wFOsXslXWv_B8x39DXhmVgr24TWF-IuLe9BoK6UCII9C7m5Pii0dYaAV-sXM-NvssXX_8RNjIl5FTF2FR3xsbb190IV3Y7EKe_jmFOOkkFaVhIQkN0Mk0n6O4dDLROaPPpXFlvAsiHBaNxKWBCgmN11huKh9tqvI3NJ_EvFJKFOG5ZhhP79_ZaVZFys-uvg9RkF-LUS7Vjmu4DQPUMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">میا خانوم انگار تو کنسرتش خراب کاری کرده و خوب نخونده، ولی خب به کسی مربوط نیست ایشون هرکاری کنه درسته.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 7.45K · <a href="https://t.me/funhiphop/84841" target="_blank">📅 20:03 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84840">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b8f9205840.mp4?token=MsPiEuCvuI5VlElrsEpbVNCMI6JquDt6_STLHga8iOhuKpa1zmN4mG3DKOyVMXQGKuKNR6TAPeD5JpRfkPcfY-OrlIdcSZlHQ4DIjUVFThgvGlhi65djwIx3asN43PO-hNRDs4j5Waz2oe-HM-NZhm3fJrvp2fjrB_1-ZQYYjAWF_jfsTxcXXaAOJtOcrc_gyAPhe8lZah9msP-5R-cj8xO3xKdggX6NBC_0sICEO40-M1PRHiZcO68CAO-nA2gwIugmaOMCpkx2YuQ4B6BcHtICc2t7AYmrJcJkTbA27xUeCtxh86t1Vz_Cx4twDSa5N0fif9ZOJQzFQdutE5nGyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b8f9205840.mp4?token=MsPiEuCvuI5VlElrsEpbVNCMI6JquDt6_STLHga8iOhuKpa1zmN4mG3DKOyVMXQGKuKNR6TAPeD5JpRfkPcfY-OrlIdcSZlHQ4DIjUVFThgvGlhi65djwIx3asN43PO-hNRDs4j5Waz2oe-HM-NZhm3fJrvp2fjrB_1-ZQYYjAWF_jfsTxcXXaAOJtOcrc_gyAPhe8lZah9msP-5R-cj8xO3xKdggX6NBC_0sICEO40-M1PRHiZcO68CAO-nA2gwIugmaOMCpkx2YuQ4B6BcHtICc2t7AYmrJcJkTbA27xUeCtxh86t1Vz_Cx4twDSa5N0fif9ZOJQzFQdutE5nGyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ایرانی انگلیس هم باشه کصخله پسر.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/funhiphop/84840" target="_blank">📅 19:35 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84837">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WYEzmzp9OcP7hqFFPB8hnEZVKbsu9SoqlOzgt9QvQgAFADOxs1AgBUfrFHXOnraD4ZaZ7wPUOti-2ReOvaEoLMBxE-prUuDu4ptcr53SZJuXWf-6YX86WZhjKkKMH13j6vTE-xXuBKfFzS2osqw9GMmBYIeeUgafZjBXdsJVNr7IfVrzQK1sjSl0jAIc2QovytmynXiVZEwv5aLLUYcqD2AzqgFjRfSrnzBYxMHBW_iO5VLe8-eXV806_sOaG_6TVN7pbGarErxiAh1XboHQkU2K6PhByiBjGi9Wm1HHgQkFDb7krOxig5J7B7oq1NHuEuOA3aPuI83rjJpos1YxYw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/m4lEVkSJG8-_O7y5eJt7EpQLUv_NxvT-ue4vVqHUSC9nTcSmXCeK9dtlgMwNI1sDdJRWviIRqfu6xYMln3he2sUo13QsNOGeJcjnfodXTIrttWXF-ZjfL6Syk7LOeREudnQpDoYLuwkt14OgXK9Uv57V-UIpxfn4cKOWXDNeEHDdDzvuEDsM9kpVpyFiRLiXkTgfPTPRxn4QHnOWlfTH9-tnwo7xfIjHzh-sYiFxP4yfVAMxP1dt1u0sCQKeEH8LWPxNHnX8SYmfSGhvonmfo6Aoaqn5h6bV-0ZdwyPZ9JYWMEUidAbQ6gMrVgN0iEH_8g-rZA-2EeXfLlIRgOPHNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/R_XUoypWGwrLPWKTS8pJUhB1XTGeKhmzulhnfZzmOwHAB9OSM-UBxdL9nXXckjojW4KBGtyLCeA6WyZxSpkooDNq0NIuSfJfDv4kXwEg60okNCphQDxJoSu5px5ODUaLtFmJDMFBRVimWicm1MQaPNoLiZ7Z0jqDtrEgcT1dJRJ8-QjtluP3jajMu2RXh_oAwOUD0O1PNG48L78XKNivX2KOVfQc_PK_OTp-yn4Rmna4AzZZULDCAr0cCh0WYfVNQSVA1FDLkHkAUu2uSuSbIlxIdZY-QYPnRD7-yrd_pVrTB2v5CihufD_oYwcCCVT9DfgBjfwUQax1omMQEft9fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">شاتای جدید کایلی جنرو ببینید تا ببینم چه خاکی تو سرم میکنم.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 8.63K · <a href="https://t.me/funhiphop/84837" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84836">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oiq5NQRGgoq6ENYn5oO2xk_uV4tX9wJgQMZoFzTJAJWt65m8nB7CCfWKZliYMBIC_VhLJNpvhwQyUzy1feB-R9k2RTKjrWlUFKuHbkjndjR6I8i5elMOEw8yqt8Ccey_GUy3oTixIw1nMAl5c5dPyuJkjqYhgkI-3MbpDmdbVSFsbxBe3Zta1BTGLqxzQ44aIVCZBfk3VN_6tStkrj3QpyApxkY6CJPJcPu1IXvBH0h2n3va1RgdyYPhHZe8Dpn82kdupyK9dkjc1Wc7DkgMUbKXYuWIYZh6SOWW14mnhydr0pdfyOn4UyEbrM1uSwJTRmWeQ83jc1RHPswyQoxWkA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
10٪ شارژ اضافه بر روی واریزی‌های ارز دیجیتال برای کاربران بری بت
⭐️
🌟
📢
در سایت بری بت وارد حساب کاربری خود شوید.
💸
از روش ارز دیجیتال اقدام به شارژ نمایید.
🔋
🪩
بر روی واریزی‌های ارز دیجیتال تا
0️⃣
1️⃣
🔣
شارژ اضافه دریافت نمایید.
💰
✅
ورود به سایت:
👇
🅰
g22
⭐
https://leworkcihsa.shop/fa/affiliates/?btag=914641_l303106
🌟
کانال رسمی ما در تلگرام:
👇
🔗
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 7.96K · <a href="https://t.me/funhiphop/84836" target="_blank">📅 19:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84833">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=E16lpTLfyG3BKwcL0YJ_NxEhtojrtJuTC2U4hrM7322tplZ1Uvq1WlMtcDZKHMMeOZPt_cxmeqFKAb1fNgVCyANxqfQyKv-dk4hnyG1509vm-Hr0D6Bz383P3X3Ivq59IMxRCMitGYQasrGlrYU7DaYqSNArzYBZNzDI8XuX_-78zFynALHw4PdSwgpZQZbcI6M6Pl57u9D7lXHHflx1upPrHLnBv_ABLqAZKdKBgxUumBUstdh6I6b6BOHnq8ITbynoloFeRP6sibhz8eIjwoy2pSBBq5mdgQqpivU3B7xxrMX-RjNneGUz1WejdzTqlDMPZzY3BERXyrPBbLYPDQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c264e282e3.mp4?token=E16lpTLfyG3BKwcL0YJ_NxEhtojrtJuTC2U4hrM7322tplZ1Uvq1WlMtcDZKHMMeOZPt_cxmeqFKAb1fNgVCyANxqfQyKv-dk4hnyG1509vm-Hr0D6Bz383P3X3Ivq59IMxRCMitGYQasrGlrYU7DaYqSNArzYBZNzDI8XuX_-78zFynALHw4PdSwgpZQZbcI6M6Pl57u9D7lXHHflx1upPrHLnBv_ABLqAZKdKBgxUumBUstdh6I6b6BOHnq8ITbynoloFeRP6sibhz8eIjwoy2pSBBq5mdgQqpivU3B7xxrMX-RjNneGUz1WejdzTqlDMPZzY3BERXyrPBbLYPDQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تو انگلیس، یه مرد جوون وارد محوطه ببرهاتو پارک حیات وحش میشه و اونجا یکی از ببر ها بهش حمله می‌کنه و نهایتا میکشتش!
مسئولین حیات وحش اعلام کردن که خوشبختانه ببر سالمه و داریم بررسی می‌کنیم بفهمیم اون کسخل چرا رفته داخل...
یه ویدئو از قبل ورود این مرحوم اومده که داره به یه زوج بریتانیایی میگه "من میرم بین ببرها، ازم یه عکس بگیرید"
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/84833" target="_blank">📅 18:37 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84832">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">این رپر جدیده سمی‌لون، بالای ۲۰ تا ترک داده تو این چندماه، هیچکدوم هیچ فرقی با قبلیا ندارن، اونور قدیمی مارکت شایان یو ده ساله داره رو یه فلو ترک میده و همش ترند میشه.
بعد میگن چرا مارکت پیشرفت نمیکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/84832" target="_blank">📅 18:10 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84831">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4bfb34762f.mp4?token=oQs6uBXi1oEJAoZF4ln2Z4_74KlPa-L4pvDjJ0grJ5CFiQ1Z-zgHDlP43_BmZPBcyMTSVWZZ9A4BKGXhAklrdkF-TGCbTIV9MJbeDBaB9TSM4_2bwy7fIcatYd8alLl3n9tRNfRypSx0xB2EdsNLAD4xiiLjhBtOJnFB0HyDk5sPZVq43-QaKzi5sJgWEKZwPNHeeqGHkF_ZZUjK08rT6jNKu6bgMvnSs041kDLyBxuOz3nghS9KIzzzAw6rQkfRBh_Awmo-Xc_lWE_DIEdX0OV_7uY8Z_F2pyNVfqNUhrJ6O_CC0W9vCBwhQeNEay4GXAWEvJyhuemnL4QlpShZ4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4bfb34762f.mp4?token=oQs6uBXi1oEJAoZF4ln2Z4_74KlPa-L4pvDjJ0grJ5CFiQ1Z-zgHDlP43_BmZPBcyMTSVWZZ9A4BKGXhAklrdkF-TGCbTIV9MJbeDBaB9TSM4_2bwy7fIcatYd8alLl3n9tRNfRypSx0xB2EdsNLAD4xiiLjhBtOJnFB0HyDk5sPZVq43-QaKzi5sJgWEKZwPNHeeqGHkF_ZZUjK08rT6jNKu6bgMvnSs041kDLyBxuOz3nghS9KIzzzAw6rQkfRBh_Awmo-Xc_lWE_DIEdX0OV_7uY8Z_F2pyNVfqNUhrJ6O_CC0W9vCBwhQeNEay4GXAWEvJyhuemnL4QlpShZ4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تتلو قبل کسخل شدن
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/funhiphop/84831" target="_blank">📅 17:36 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84829">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">اینترنت پر سرعت اپراتور های مملکت قراره افزایش ۴۰ درصدی بخورن
تعرفه های اینترنت فیبر مخابرات هم کم کم دارن افزایش میخورن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/84829" target="_blank">📅 16:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84828">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c83uYHETy_ssVXkDj0IqxnoRA660ZfvwXRZ7aqfNxBmzOhvk2WWWWKmQWUfaxIl-IaSDx5CbKgaaySNngJ1oMnpm9f2TUbqTCjUpDDrqeGiYIf41_ScVWfKW2tW9pBT5EScmKkfGgMuOIDQIP1VhZPu7nwlx-SiFvdzEEl09qG3C95EIdQ9FPNMqv2XDu7B51j7_FY2Qcb0Bt4o-91ncZicRsKXh9pwNR8oZmEncrwzvFLfz2k9-KOJAeUFkTm6299pJPPqC-R7qnfpPa5DXlwhwwqwVTg7tTNX7CT11FCaXtysoiIJe8RLToyL2qz-5GWscpF-KQ_Q1YIVIi3qNyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟  رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84828" target="_blank">📅 16:21 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84827">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ujFGuAFn80bzjMLB-HnNNG9Tsn-V7j-Zzfjhsi6k1Ch4ZxsObv9IKxGrjmG3-jQGyJ7zt4eHYRdAfprDw7FjP0MMyYa0zospWAPy2hYTN5NQrF4Te-kAsQxhLSof9u2iFNQaWm7-t7B1JimFIdjuCl6Rt4aNzXk_2DwE9LiiA45iiam_xfhrBwhY-Zmp_RTcUiMWToAH2WHgY7k0o4xJ7UALo5gleQtIC8dDOI7ghkePSBXmuR1YaAUHB18wNVQ8RNvhfswEr_A26GW9MW2wGc2-gCcenD5jPDOnJ9hO6NeIJWIxMrU_LbI-T1R5Deu28bbIBq_QY5729xffaV3w5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یامال یه پست گذاشته خطاب به لمینا بازیکن گالاتاسرای و گفته، یعنی الان دیگه منو می‌شناسه؟
رافینیا و فرمین کامنت گذاشتن فکر کنم دیگه شناخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/funhiphop/84827" target="_blank">📅 16:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84826">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">کیم جونگ اون رهبر کره شمالی خودکشی کردن رو ممنوع کرده و گفته هرکی تلاش کنه خودشو بکشه و زنده بمونه، اعدام می‌شه.
ممنون
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/84826" target="_blank">📅 15:54 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84825">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">عمان:
مذاکرات با ایران درباره تنگه هرمز به پایان رسیده است
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/84825" target="_blank">📅 15:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84824">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cPPKaiD94wlR3flCm0EaUwPuOl9H-m75z3c00CIu0DKfiRcqJ_gw93zL0zOSvYjUzgsnENWOtTfbyi2TLqSe02Z-MjkPBjqjrD5lkwRmiDIISP4WF2I3PthLCQMQbfy68GxIA-B8kaArjyuSUcNzoC4EnrpIjZk7Te80aHqtlTjWmB8lp2HT7BKhkm4Iyxc8yMz2fbNB0KwrUsnZd10yY8ExrVYCQQYYJKIuIvXSJywGg0tUEV5ghSVq8XLRrUcU_pyqmIvXurzYXMJQlV31n0gt9LKXiVDe9OgThsPRu4RJyyBjyL7VH0Jn3zvpfbfSba5gCEoxxKzpX8OYJSvlqw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بسه دیگه اشباع شدی
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/84824" target="_blank">📅 13:07 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84823">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سلام فریب جان خوبی چخبرا  ذخیره کردی؟
سیریک صدای انفجار اومد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/84823" target="_blank">📅 11:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84822">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromGangstShip(ChamanDarKhak)</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pK0lXfi2QyPnaVztObC8dXzAd7C-9FLkfpOHGj8296cGvUSZqx0ETwH3iO8cmaTuAoOYQy4yvGxxw-lQQhUq44p9oogZ4Jm1fWWSpEkgrFjdUInhyjEwvC4CVekisH5KkSELF1BQBq2QOP6VxkvK-Ujajbtp0tjZslaOIW10NrquVEF3mx6EgCsDUpyobDPtkduN6FO_judKZ9StIN2NqUf0lLspSaeedCEjXxIDR97GxgJE4proiNbDCBDU6h6lJ15CWBLnfPPckFfCl0CYycgE6ygz3R3bkrceru4ii5A0cMEvf78syGCl_fSjIdmUvTeoe__D1elKcVl7Jk9M7w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">#NEWS
🗞
🔴
فیفتی سنت
به یک خبرنگار گفته که
Eminem
به دلیل اینکه داره رو آلبوم جدیدش کار میکنه نتونسته در ساندترک فیلم جدیدش حضور پیدا کنه، حضور خود
50Cent
در آلبوم
Eminem
هم قطعیه
@GangStship
🇺🇸</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84822" target="_blank">📅 10:57 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84821">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lVCot7eDrTF5b1dh8ce3gLI1VMTvto5YZfyfe7vBsdRRdZMdkn-WFvs2p6_eo557JAEeK8xqChe8XH55QrEQdyajBSbS9Bti7VBnE5UpQvB4SL9v1aXreEJxiEVxWw5wodzhWgkQKdk2OC9Vhl7ikyH01KhEGsmsh82RA3432MKiCi7UYWwfi1gG_5eP-6mV3RJzeB66qTO---4-WfzFBK5IrDwlHz9JHmsumz1C_2TpI6cElTY2_rNZMjBmD6nzPrHHYyfmYlaE_Vtz6Gr4y3JwbX59TY7mo916KJNrclckr1NLNw8dForhGmt-u9E02nH3ABMDSopNsRmfL9bSHg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پرونده قتل توپاک بعد از ۳۰ سال بالاخره حل شد و قاتلش به ۴۰سال حبس محکوم شد.
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/84821" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84820">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dWiqAbicY-GCFxc2mK0MsObFo7sRJKS2kx7-Y0Br4C8xgqr9bp_G6VGJqKtzvxXTgGRtmmT0ByoaCZ3hzFpYj4z01uS30VP_lYxcebpYXdsWdqHXhGVD1WVk1B8iXVg4T0cE3J3sgG9kmVS9N-bYOI7Y9kRxffkcFXAnOlsVKLhRjNqRoy0mQ9KzM-jhVtfjvi4D4o27yRaDyCecSt4L1YmDAFcqnfj_iTZ0xsrkCpDquLBhbh_r2BQzTO86l7jqtfdnETToj-67S0sMN2uhR9gr22hyAedfbUs-JxL3-TYM0oeOW_egSL3WjevmV6orjdLCKrmIW-DpKoUP0h2_Tg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
منچستر سیتی  - پاری سن ژرمن
🌎
ساعت ۲۲:۳۰
⚽️
آ اس رم  - رئال مادرید
🌎
ساعت ۲۲:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r22
🔗
https://leworkcihsa.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/84820" target="_blank">📅 10:38 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84819">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j17dW6qklu-W5Ih7ed6BZn8w_y6Yni4qBhSkGDLX2cs_vbB_9MDCtgF5cDGoCp5YK_t6keUUuC6sFB2d5OReRxBrJf2bTN1gYojyqiv2zAasozmUpF83v5AwmeI54lKxaFQVjw0Xx8k10vHQSDfS3SlivUXKW5s_pB_rC9M6NgMO7VIQg7Qh9n2-buBIRahiKRcnijfm-jDRujQwc9-OCTUfSiS_copZHAgI6bkwZg4jJnNdbpqPW7zgIihJxJilnkFdWVuaAPKYC3HNJwTwcnJce4hEebFPaJZ9ln9Sn3nUHtg_Y20HjlJuQ5jEKpo8A7Qhyz_3d8evxOLTgB2SvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیشب تو استرالیا یه دختر مسلمون برای ترویج دین اسلام رفته بوده توی خیابون نماز میخونده که یه راننده ندیدتش و از روش رد شد و دخترو کشت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/84819" target="_blank">📅 09:51 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84818">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=bRPgtHNRna5Mfrd-VXpg-KS9_K_owzyyz4OUR1VKzPQsvG2Sgxx8nAnC3JEmAJalXgbUZhfqqmgQZsbMFBzbiEaJSqV0JCtqaCx_UHlUZWKpPrd63MwBmPIMf89cUWv-cUZ4NMrYp_Vy3FIq3r4Yzopp5H-DfWjBaumVXsUVqNLtZYcW5ZCBMjHv879W8TCjYgfCEMB1Z6oQa28LxSIVo89kgYqIgcbz82m3eulbA9Q42cHJm8u3Rhbedopwx1h87bWNtcJ2PEX3wA8QPu2IFQni95_mgWWnDfGjpkXAXV98S9Ui1vF-tmS-I2wUx1VvPoD9qoKTiVKh4u1xSPmS_wFzp0SsBBrMVKL3RsFpqsBiZS4vaUfS-A8z4rL4ZjnJUQg3ks_VfC7FHlYBieAVPZACSjjFN9GFJkyZ8cszTsugsShSxTp-VFzJH9eDl-1yIkr2m36_g98uBFiQ9cs9gWOpxY5pPrUJPl4nnCnC_-WVY2l3x6wVW0Ace5HA7WXbXl_ZWrIubyusthTMQLraUlEpyroQ9JPZa2bVOukk2V52vUgTwTY5282bZ80GHS5nb0PnSnM7qGWTyKzxwiOvmsahIKAz-0kwmFeeVRaF0yZ_8xO3qpqpaG9-qr99Fz95J-GiN5lvxvOWzl9jr9B2Tj_MwevCnuNJf_0fhAk3Q9I" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc5f754c70.mp4?token=bRPgtHNRna5Mfrd-VXpg-KS9_K_owzyyz4OUR1VKzPQsvG2Sgxx8nAnC3JEmAJalXgbUZhfqqmgQZsbMFBzbiEaJSqV0JCtqaCx_UHlUZWKpPrd63MwBmPIMf89cUWv-cUZ4NMrYp_Vy3FIq3r4Yzopp5H-DfWjBaumVXsUVqNLtZYcW5ZCBMjHv879W8TCjYgfCEMB1Z6oQa28LxSIVo89kgYqIgcbz82m3eulbA9Q42cHJm8u3Rhbedopwx1h87bWNtcJ2PEX3wA8QPu2IFQni95_mgWWnDfGjpkXAXV98S9Ui1vF-tmS-I2wUx1VvPoD9qoKTiVKh4u1xSPmS_wFzp0SsBBrMVKL3RsFpqsBiZS4vaUfS-A8z4rL4ZjnJUQg3ks_VfC7FHlYBieAVPZACSjjFN9GFJkyZ8cszTsugsShSxTp-VFzJH9eDl-1yIkr2m36_g98uBFiQ9cs9gWOpxY5pPrUJPl4nnCnC_-WVY2l3x6wVW0Ace5HA7WXbXl_ZWrIubyusthTMQLraUlEpyroQ9JPZa2bVOukk2V52vUgTwTY5282bZ80GHS5nb0PnSnM7qGWTyKzxwiOvmsahIKAz-0kwmFeeVRaF0yZ_8xO3qpqpaG9-qr99Fz95J-GiN5lvxvOWzl9jr9B2Tj_MwevCnuNJf_0fhAk3Q9I" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">به روح پاک پسر طبیعت قسم این دیگه صددر‌صد یعنی تعویق
ترامپ:
صبر کنید تا ببینید ما با ایران چه خواهیم کرد. ما کارهای بزرگی انجام خواهیم داد. صبر کنید تا ببینید. آنها فقط منتظر هستند.
صبر کنید تا ببینید ما با ایران چه خواهیم کرد، زیرا ما تا حدودی از این موضوع خسته شده‌ایم. می‌دانید، ما خسته شده‌ایم.
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84818" target="_blank">📅 05:14 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84817">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube  @Funhiphop | Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84817" target="_blank">📅 05:05 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84815">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UXQDCxEVXz2xgLrJHWYG8qO7-FDJp3Km1EOW9VePp4FHLNQlQ33Lytq2TB4KdNJAwZu9Ak-KMXKKB3zXb8sd5tNDul-jFhKMEn61ZUas2fNPYmcAilp-Avqj7ddmIO4zNARa6Nc-fq8kG7pwlJZlkrZ7u7tXsKjB1DLESp1Lany9WH55cGC9HcyBJ_EnAU4B89Vbq38PpvZpOU_1tC5gMHw0FFrI3-W5OtpTdvi9OU9ZXfYgbhuRawpeSZVGEehEE0tVxcv3CLDz0Aax1pwnpMsSHozDzhTnS0-FEOXgjyqL__r8d4zT5UZzGOBUCxsTP_O7h6zHZnRlQW3XXYpsxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید سلطان بالاخره ریلیز شد و سلطان بالاخره رکورد گینس تعداد ترک ضبط شده با تلفن ثابت رو زد
🔥
🔥
🔥
🔥
YouTube
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84815" target="_blank">📅 05:04 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84814">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=CdRKu-8XVp6Uv4Is0CwtxpaIkizMx7quBxmskn8WZPJzFdtMyHKDjWNS6I3sjmmEgvK1a2ipra4s0G8kKCpp191993GiE2_R_X6FAYF8EVMvAANpiyGHqatuBfBuDg9DMU_0TiVZGyTSnrFSELQAVbsWFoUjYmXcOB3486_WnoEfwJbdha_6UgPsNVdTrkSGeLwVLO6KI5onAG9Z8ip4X2D-MpqFrxTiBHniJd_7ZhveDCSoSr4s86ZKPSGI2CmCfAHweYox4LQxmFAJvK5d_oXsQDIY4agztcABROdU3dqXtp3z-c7D6qi0tDlR3E4dYR3QQUFYCAojnumeIvSerA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/08b06e11a2.mp4?token=CdRKu-8XVp6Uv4Is0CwtxpaIkizMx7quBxmskn8WZPJzFdtMyHKDjWNS6I3sjmmEgvK1a2ipra4s0G8kKCpp191993GiE2_R_X6FAYF8EVMvAANpiyGHqatuBfBuDg9DMU_0TiVZGyTSnrFSELQAVbsWFoUjYmXcOB3486_WnoEfwJbdha_6UgPsNVdTrkSGeLwVLO6KI5onAG9Z8ip4X2D-MpqFrxTiBHniJd_7ZhveDCSoSr4s86ZKPSGI2CmCfAHweYox4LQxmFAJvK5d_oXsQDIY4agztcABROdU3dqXtp3z-c7D6qi0tDlR3E4dYR3QQUFYCAojnumeIvSerA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قهرمان فیزیک بن‌بست دسته‌ی مثبت 35 کیلوگرم، بعد از یه بحث بسیار پرتنش بین سه تا نورون باقی مونده‌ی مغزش، یه همچین تصمیمی گرفت.
🔥
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84814" target="_blank">📅 03:31 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84812">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">شمام خوان گارسیا رو میبینید یاد نویر میفتید؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84812" target="_blank">📅 01:25 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84811">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ryxEGN2mLvY-RLPEpn904gd-gCGvW472aTvHBfxPfJQPKbXT4l0fhYRvpdjZHX_uPVCrEzW2TRGsJuNWhZAbYnilzK6zdolY3X3v1fnf-N2UieZXXiXApfqoeVwGi5yvksTCIjT0dscsHTUO3FWDHF4-SXsAInm832lkI6kQqJRtCBfk-856B0cz8hH7kcyFFjFmm58naoYBi6m4qPEUhB-bqDkM_IOkw7hnYlQAV4pluLsJjtd-Q1lL0FwOz3mlDHfEUUAYzpNxGV3sHJdIzYBrqCC47nTdYUavDgTxYELcZnAjBAbrFbvXbP1HdsCWx1T_xrsqGOXoT5g1DFzjvw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حالا هی بگید منچستر قرمز نیست و آبیه.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84811" target="_blank">📅 01:18 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84810">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">آمریکا اسرائیل و ایران، هر سه تاشون براوردشون اینه که میخوان غافلگیر شن و هر سه تاشون منتظرن اون یکی اول بزنه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/84810" target="_blank">📅 01:00 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84809">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d65b19bec2.mp4?token=JhSWfSyMfIVmGrxvq_ZtQ7AIQo2ipUNPTYo1ZFc0nexfPaKrLI3AdLTVRn2rsSjJQ9UIsC6J5AjmtNFnWxssk9YCQ4ZWCA2sNxrYE2Feg0XpdGIVXxLtCcK-ZnkVMGT7jSNlkIT4KqpyzzjepJDu3k0rDC8araIezojQQPHi1yw2LA_eUJGsJPJ-UZ77Dz_PFu25r-3NzImkqJpjb9jd3QspH5h9NSEKL2wGMeBWS1swsrJeDdVzpM7WNjax23ih6ytrdENZQIX7PgtjwBNpGozKPwko0qakg0DT_s9mG3m_FjsEASNhjkqjNXe1qMuxGtMxqDuo9EZ3pv5828ba4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چرا پر تناقضه این ویدیو، شاهی و بیگ شگی و محسن ای‌وی‌ایکس انگار از سه تا دنیای متفاوت ان.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/funhiphop/84809" target="_blank">📅 00:44 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84808">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بارسای هانسی فلیک واقعا بهترین تیم تاریخه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84808" target="_blank">📅 00:20 · 22 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84807">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">یامال یه سانتر کرد توپ رفت جایی که غم نباشه</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84807" target="_blank">📅 23:42 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84806">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MTyzDeExR96PIS3saNAMaRTuC4T8hDo6RV4BaW2A6j6yUC9ncno-1Y-u1ZpWv-ISw8xMo-bLvZZ3XOLI4lhkYMX174OZKtOHs-UMaw_P190VPJj_z-F8um14D9AQIHhvPxoCtJ52gNVQzTVTwiQM5wfzMn7IDTikvUN90i06BvX6fgy2CM5mSxt6yfQgetMqdESbg0Eq_JXt3QiwSCP03jVZxSlK4RMIv08c5j37INnpnIAu4SRpiG3XITWSuql92m6cH-q9fQ6Ipijr6m9AOGvIWn6QT5O5iFr08uwNzIoRJefysB2nw4wnc3_goY-6fKBY-7PKhQSwRmdNfYVX2A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اسپویل نکن
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84806" target="_blank">📅 23:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84798">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B8tJ-pLBy4Oapjxl8J_2_l6opcfbfl_zGRZyp2lbpXfl372QYbZSYlzcAkVRJ8NaoNF7HY-IV3_hwNa_DZ8jxBGJW-r3yaScGM7ZisRdBdj_-c0tzugY7rh5U0oiOguCr-7GzJvvfJAA9zxZGVd5aT6jzqlqJqnF-eXwWsW7awaQpkTSDO85CMNGJWjuonmGZ2fLx0laZGegNPaT3XAR74L6oFo-J5Jc2GubHGWFNy5BWMvX4_ncbJ7soW2C7PBhENIRuNFUMe7wPNKoxnhI-UWgmqxMf843ARq_7ijHsOovzBtaI6KUTuyy77BNWYULgyB4sKvt9qdf20DSl1pLTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Tvr-RtfLc7MgkK3ss36oKhPze_EvP9YpRGzD4CNb6pCxIlV2vL9VckNuxuHoJJMPP_vAqNtAoUtjHxK7XmCIIG1Y0PoJyaO02LUgZ_tTTWVEjCJlNRz_rXZiyE2KF7OWkO8XqzgQjhp76F9ND_7pFzyoOvp0UhXHTeV8yWCo4DlUaGmrgERTxKKPYkrAry3486cCkcVX3ayuldV1XPMFNxJfLYS9yDuezROBr6av8r95Jy8XvaW504CHyXvlB38n3rL1P22Fsi3cs3KGXWPu-lS_EsYG56uXGmwEQ1A0XlN-WA2o22P-GIvNTypk1u_mSsprWlHS2zfkcfBV3Nb1Fw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">توی ترب دارن دم و دستگاه لوازمات جنسی مثل دیلدو و واژن مصنوعی و بات پلاگ رو میفروشن.
حتی صندلی و ابزار شکنجه ام موجوده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84798" target="_blank">📅 22:43 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84797">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/941b0ce75a.mp4?token=Ra60EUfz-4QwfW0pPSxMZEOUtmQ0lhYEe7amij4P2-HFJf9OvOZAO-n1qHjCuBmpooXHo1UL2qwi-gqqBIkGDBoQ6Iz2vNe3y7YSF_DcfzxIekA10Q_b4r3VIWDyPOfyTX2MEszpIkXgpLcGFQnrxwWNSoB3__-t8Uy2g1phsDjaj8Tuq3C23uziR_ZpJeXn1yhz3LSPM8O3daDO53_QB9jG_dptVTP5wyJzJsGCAOm0okIGixwpfdI4K5qP5ZiT5czcQnRY8lVcros6-v-ELCu-xpo_CW_IoYclPdHyUOa2JahPh6pPJbg1xa815rS3ptn2VFCvbgml5v5y4CAIVA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حسین تی ام واسه خودش و دوست دخترش ۱۸ پرومکس خریده
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/funhiphop/84797" target="_blank">📅 22:19 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84796">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/ZzKLw04_jzXusWdm4LJn4u3V4kUyAgPOwpdZRixJydYMZc6dAU6dCcKvDcAU6hKPUYcrU5M8iJrnTAJ-YsPBhXJDCShJqCLoJs_iMVFzmLeE-MmIU20-lEL7eLnMz-Rxqnb5H41QjXk9xWq5zvrLAr0Nsti1iu3kHqzmVQYilsYFRecOOzRNA9h24aK6ZBfPSy_MxH20VeYGIUxz3zXnzff0XZxkTq-rJNG9jBAOACoZ_bByhR0yyTOhuUNfDbLPOlw0Z7dTNOtIs4XuRRbDTicUJnIba2slmSBsRF7IBO_KU0zuwlxLzKDko1fCctyco8No8-eRk3wjQdJD3uYiaw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شهردار همجنسگرای شهر مونشن‌گلادباخ المان با یک مرد ایرانی به اسم سیروس دبیر
ازدواج کرد
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84796" target="_blank">📅 21:21 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84795">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">The Memory</div>
  <div class="tg-doc-extra">Creator (ft Alidanesh & Sahar)</div>
</div>
<a href="https://t.me/funhiphop/84795" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84795" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84794">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from“Creator”</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MVJToajeo74AmOyoFEkBrb4L0Vlb73UOJTL9XUgQBDITKllE4Px0N_LQ6WCfmM3mBjZSCI-ne6zuCvDxM8AHP0mXs_AgVU6EX6_tx6aFw08_rfvVNszK-MyW6kIesNcKmUotu8w1uNFSnjgqB3NCdOrdOr_raBMTdyzBS89lMuXiQSMscjkBFdYmQLUJUTqUppcEFiLvST0uWrYqJZ6ggbdXoNqPpQo1td4eBl9GEqVRZqh8qvhOpx9aTodh6d5RydymSxCl7on77rwMTOclVBHRiVpX0-irOjhyWv-u96b9NwHrLnmZ2p24wDGqpr7_jqDql9wojBNmxUC4sg_kPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترک جدید Creator ( Alidanesh و sahar ) بنام The Memory منتشر شد
🆔️
@Amircreatorrr
📥
Download</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/84794" target="_blank">📅 21:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84793">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=MmJJZskQifKIRoJ8fY6HZTQjRD4SVF3Jl-767cSjtGI1n3Vn2Cvaanc10LfZhytVxtijJZbQKZI9WIyj9SLyWOtVLL5QhNaqR21YE33z9lr-O8Qkx5iNFWk0_FMkQUGwTC0GtxZRcef3cvRll4YpejGSPUNtgTA8q0b0L-h2SS-pPLX0qxCE1YALxJk0KwVe2n77EOfKRuZl-Sq0f-BB997OnZD0S9b3tEhr5IK0z9vWTmrC7ph3nCMnrSQpHwlRLFuIv3DWkfjh7jha-KFyH1xex4WKDP0u5_bwKDcQawDLBNPygB_vPQS3_gGwi2MDzKMZxJi3ilNmwEhGGkhTpA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83f013a68a.mp4?token=MmJJZskQifKIRoJ8fY6HZTQjRD4SVF3Jl-767cSjtGI1n3Vn2Cvaanc10LfZhytVxtijJZbQKZI9WIyj9SLyWOtVLL5QhNaqR21YE33z9lr-O8Qkx5iNFWk0_FMkQUGwTC0GtxZRcef3cvRll4YpejGSPUNtgTA8q0b0L-h2SS-pPLX0qxCE1YALxJk0KwVe2n77EOfKRuZl-Sq0f-BB997OnZD0S9b3tEhr5IK0z9vWTmrC7ph3nCMnrSQpHwlRLFuIv3DWkfjh7jha-KFyH1xex4WKDP0u5_bwKDcQawDLBNPygB_vPQS3_gGwi2MDzKMZxJi3ilNmwEhGGkhTpA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دادستان کرمانشاه: در بازرسی از یک تریلی در مرز پرویزخان، ۹۹ سلاح کمری، ۱۰ کلاشینکف، ۱۷۰۰ فشنگ و ۱۹۸ خشاب کمری کشف شد که در بخش‌های مختلف خودرو جاسازی شده بودند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84793" target="_blank">📅 20:28 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84791">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/h_PDx1Kv_yXRk2_N4eE21_Nhmm5Dn98rPIssZTB3ARCHc-5Ete46LACUVEH2CtQxtlDI4Mhl3Oftm31OJ-jMlnIstzvvXX5tYt9UAE-0sCdIxssdaY7FJ1CsSN82rGfDYusJ4gy7RYxZwHj_Ab8v6RKTbeVQlJ8979vx-AhgSE8jJSCXWr6fYaM5F59uwZJjs2UyAOWArBvUclFEixrvSBm5RsnRuKXknqLdvYeBQLJD_7Y-0X9lkBCRGdeLOgSuEWGARQja5w6rJOjxMlgEv7LvzJPTy_Qa0r4TaGB5Ji01w4bx513Vdq74WXTC5jRD9m_4kWZa8JlOld3alli-fw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn1.telesco.pe/file/WBLcUIfA0EDZxr7SckFdxtC5ezg68DpzJ5DMQwf3qPcRBtjsvBd25fhT_JjjYNWXce5R_3XajZd973qezS7FsRSCIP0Y24A4bENmSfApHede-M_2jsgRKBKq7WuEGMa8xOShkPe9ez_5SDc3-SQl8nhfL4DJH0eu-_0imwHjb5wG-HOi3cwsCy4p9dPZcvaT_IzzOZQI2UzcmZLu3zW6F_7v_WWk8OP7m4_cgRp4Z8zCs2zxApSe_Tf-MfOCC9776Kmw7aogh89pUflGCK11ix87Brh-Bp6Roy1JaYN6vRm_-JF_Xjd52iPDZAdrR3La8lQSoZHOn2DRsP-uMpiBrA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">بررسی تخصصی و کامل معنی “سیکتیر”
@FunHipHop
| TemSah</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/84791" target="_blank">📅 20:02 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84789">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GEHnKfYsOu946xVkpSuYaVv3WnGRc5D9LT7QSzpWeiW9NlmhRR9xB-M3G95KH_T6bDmKdoPis10QaAi5i6T0WTZvzZXGFs_rV2sZjWUpmQy7NtyW0IuGPdtuRjMTFL8uZ-U3ebBlVpj3d9eLG8GKV40KSCmGgnpg7Hbt3vW5oRh9vE1OKgWMRnR69jC482vERlO41qSGUklR1jAPrz_ej0hAvD9lH8RF5sxu9AO_HCB9mcnupEMy5AYVT3_fxpH03GidlJbufXGPDfU7d9dcoRP1EgcgdidkH-Y_qNTom_vIqUuBKtLcs_mmAFxXHrkDYsjLWQLy2Kx00Lxyt0Stsg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=TBovDusxJiNQLXG-HURRwVH0qF-qX5H6uR3ea4SWrLfgJ0eaMN9gp-qcg5dR9M-k6CiTbBTw7DVj7ZNj0CzQiD08cFlUPpewgGWbmnRR5YcTyh0y3JItfXfUXjp2ex-214XgYrDOfVtUgsfzq-V1vUBBI6x48YlnrRydZV8pIJnT-MO_dw_1RGgqAytxYVuuQAdf1YfLkjYod1-vumPsUWxF7FPHjmtOFIynIbpMqB_hm8xOD4qP33K1Ky5bZmWZfIQ60lSUpxIwof7NWKhW5tL2aveTyFvIOXu8_GwENqWSRsS_7cM98vtJuw27Ed-fbqzbfeK8-cSmZoL0APmINQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d11bb640d1.mp4?token=TBovDusxJiNQLXG-HURRwVH0qF-qX5H6uR3ea4SWrLfgJ0eaMN9gp-qcg5dR9M-k6CiTbBTw7DVj7ZNj0CzQiD08cFlUPpewgGWbmnRR5YcTyh0y3JItfXfUXjp2ex-214XgYrDOfVtUgsfzq-V1vUBBI6x48YlnrRydZV8pIJnT-MO_dw_1RGgqAytxYVuuQAdf1YfLkjYod1-vumPsUWxF7FPHjmtOFIynIbpMqB_hm8xOD4qP33K1Ky5bZmWZfIQ60lSUpxIwof7NWKhW5tL2aveTyFvIOXu8_GwENqWSRsS_7cM98vtJuw27Ed-fbqzbfeK8-cSmZoL0APmINQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
بعد از اینکه «محمدرضا گلزار» به «رضا عطاران» تیکه انداخت که به خودش نمیرسه تا مردمی جلوه کنه؛ دیشب عطاران با این تیپ توی‌ جشنواره فیلم بوسان کره جنوبی ظاهر شد.
@FunHipHop
| Temsah</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/84789" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84788">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-text">شانس
0️⃣
0️⃣
1️⃣
میلیون تومانی خود را در بری بت از دست ندهید
🔥
😎</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/84788" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84787">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gmmr5by0pgpaby4-G9AxZ9K_mn2NVb3dTZokL-ysJ5Zrz_oTgCaBpnDSZgXRBOwvb9ezCi_twNkuxGLYfBd7tWckNpKOa1JCYLIvfKHu34O4pTOebmoOfCB0HYP2Sph-hTYCw-5opdbaGc-oBVWXBVuaRgtbm09l_McIQLs9M554kKL90t6vSpt0-cU59f2Kws_wamxp9PJmO0G0GvX4sdM4vf6PDAVr0VJod4q8-UvWaiTciTbs-1tL5ZmNH0yjAcIDm-yYdrp5dprQQrEOnTONQEZyTI4CoIe_JTUZSUVrlRF_im6C2QB50BgTNOq01kU88LWVEWL4YMZwT-8LSw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G21
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/84787" target="_blank">📅 19:58 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84786">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ترامپ:
بزودی درباره ایران تصمیم بزرگی‌ خواهم گرفت.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/funhiphop/84786" target="_blank">📅 19:50 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84785">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=CHZFbt1jVxt-2a5LGM38-2DXaAUPon5RE2VysQJCEOYQlSlcM0fm6H6G-Z-UVwbWwzULFuLCsq4oYhorhL7egw5UJWe6jkDF1BZnOLVpwJ1TseBi_9WQlfGE_B0H-dFCpRzCQuXbBZXme5vKR5NTne36pTPpmMb8GB7_ReBQzWV2dHHm2fWjagKgCziiWGrWu1W_sZpx0A_VhVvyO8BLCiNiCJGUAsNXrjxvBLWPEwt89wjEkVYRJLdhpc-avlZQyuae_I6ka3lSPahK1th24gkTQwZ40GSQ8D65EZ-EfTU5su_q6OBEWXvzGKhWHfUN5Yakwu9L7ZSMg85PBNzikQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d183db41bd.mp4?token=CHZFbt1jVxt-2a5LGM38-2DXaAUPon5RE2VysQJCEOYQlSlcM0fm6H6G-Z-UVwbWwzULFuLCsq4oYhorhL7egw5UJWe6jkDF1BZnOLVpwJ1TseBi_9WQlfGE_B0H-dFCpRzCQuXbBZXme5vKR5NTne36pTPpmMb8GB7_ReBQzWV2dHHm2fWjagKgCziiWGrWu1W_sZpx0A_VhVvyO8BLCiNiCJGUAsNXrjxvBLWPEwt89wjEkVYRJLdhpc-avlZQyuae_I6ka3lSPahK1th24gkTQwZ40GSQ8D65EZ-EfTU5su_q6OBEWXvzGKhWHfUN5Yakwu9L7ZSMg85PBNzikQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شهردار کرج:
همه ایرانی‌ها، کرجی هستن ولی خودشون خبر ندارن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84785" target="_blank">📅 18:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84784">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=Zb2cK8JRlpnbwckPMJzNb3ZHaHw-8P-WyCJIVk37rRJPF3nJqCuLILrceCr7ernyLtEP3j1Y1RHbNZ6RHS1HJXXaEDH-h4URh9shhAUWwcj_NprQtMxPYcCTJykXfvLGlxZXPYc7TZvHzL_53KEvA1tmYO-j3XWF9mQ25Vi1y_4kaBE1afO3gutVhw1s9I0J3BXxXivXnNU3MMRusxtg19__GHkpluU89xPDKPWh7cLDEwEtCM3JveDtwL4HEcR3Ml7F0nSaj30CC1UpYcu6CbNwEnVtoeZxfbNklBURoRctYFUSPVbw38BSv1wrQrny2JVivYxjRPUsCiAmFDRblw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5d0c459f41.mp4?token=Zb2cK8JRlpnbwckPMJzNb3ZHaHw-8P-WyCJIVk37rRJPF3nJqCuLILrceCr7ernyLtEP3j1Y1RHbNZ6RHS1HJXXaEDH-h4URh9shhAUWwcj_NprQtMxPYcCTJykXfvLGlxZXPYc7TZvHzL_53KEvA1tmYO-j3XWF9mQ25Vi1y_4kaBE1afO3gutVhw1s9I0J3BXxXivXnNU3MMRusxtg19__GHkpluU89xPDKPWh7cLDEwEtCM3JveDtwL4HEcR3Ml7F0nSaj30CC1UpYcu6CbNwEnVtoeZxfbNklBURoRctYFUSPVbw38BSv1wrQrny2JVivYxjRPUsCiAmFDRblw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حمید سحری برا استقلال و یاسر آسانی کار زده.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84784" target="_blank">📅 17:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84780">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/SQ0l1sXk5WEQ2zrL1rbJFAqY-YWpEyL_y1srGuIL9mngdt1D5DTyCrjNr_J-F2kpRcqrY6TFIXw2sDho2H6uQ_RyxgU_ZQHizf9msThr17QQ24uAIJ8H_U7ooG7DaOC1IxDwtlHYVgHvtg9C5xPXoMv0x_DWbaAhGlWfKOPxTtOR9bB6fvf6S1MwGDi5ZE5NdxHDBHs6zjF_a7p0UqUc336MIMi6XJChRNRaIE1zO9DHL3f4jzcOlQp1YY6g5cW2QeCegaDzN0a7g2hIxsBZ_cPudkDqgCIb9Zd8u8R_SYfzjVks1Ro-ws9OWCvUaoVZTAs8V7tg_m9X6bSwX-TPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f_bSJJEkyrwpabX_rtKx-FfqrDLvuNquyTU8R_YH6CWIpW6aNuQ_wXkmKPiixgAVzWGcoCwtfY_DgbndHmmt2B-CYXdUWNXSH2ZTUl7673Y9ZbqDEynpfXxiu07krhsU8V-IShxWfA1yyRIzxuKPspaZHg79SImks8EGLs9EosrpYHEAEBRfRVmMm5blC1a6HlxbbdUBJ_DTkINlIDy97jQFtM4chfxbFm3Wo8_NfDWW8T1cd5ysUeOGfkaOzgAPpJD_tmRzOoCo-sTQpNSTgHLPo43ZG26WHA3jWBmbrQlBURvUOuhPwKuqOyWj0JwvqxzdF1LGUHb_iNtNFP7W0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PjR72eRBb2oSKGTCez8SS8JwS2z3S46OphzXst-ifCMBlxoP2dQy9yccLC28135uEVLCfuI3SO25jnhrEQIGXVlL6Z718Si-Wep6G_AAYge0l0H06HJwagFKZKu8J-OgR6IzFELQuW2TVQd86uzNrUkV20-AEt-pmTZ5ZWDWytpdWDZiLvyr1PLK1P1Qul7txMB2P0RaXIJ8sRRzXx_tJENPTckfhK0QtFLuTOTbllIi_emW44P3WIRfR_ypAPnvNnaVx258Ye_XaBUDjimxtBKjZ2vC8IY1zcV1VUfhHCf7gHL83k4288gmtNQka6tqRWE5UIKNvyWxzcL-NpMJXA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/p_m0dYIIDFtS8ZHCFkPm1JbjpDn4TV3APA1hx7zbv7J1YJTn3-6iMv1p3_A4L06pTMXzwYQFrquLfGENJ_uAICghDjy6ddYrEjhm-aaITMbYLtDboHnHpXCqsqBrBZYMtGVgLThRQZ_jqLu-SiHMxrkPPu_PC4U7iGQNBkVHMDp3RcsS9_3qz5gd-BHkPkpWt_qBx2K3wpNNfW8oe-g5H4eHM6GnOITmEqbg0v90VsLmxXkokNDs0qjNrRDD44N7LPmfLZlCD97vtTtqWNV3UiXvoC3RgIRB9fXPcMaeVzqYykgiNq3oJYM27BWGpr2Whzh355W9cxldhSeJfnpoZQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">دیروز یه عکاس فرانسوی تونست از پدیده‌ی زیبای red sprite | رِد اسپرایت ، عکاسی کنه؛
رد اسپریت‌ها نورهای قرمز کوتاه‌مدتی هستن که گاهی بالای ابرهای تندری، تو آسمون دیده میشن.
اونا فقط چند لحظه (هزارم ثانیه) می‌درخشن و معمولاً بعد از رعدوبرق‌های خیلی قوی ظاهر میشن.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84780" target="_blank">📅 16:29 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84779">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=dqKoZ3u8xfs91bCO2wId03JqAaFnSQxllJaEU6dUkHClOvaaLcGPtSKTTcBzXqgZ_HoACuGFOARTjUVH1xez9K-jAesIl-UCtCkXSLE8AUPnXzCe52oMr629kqKSl3oTaaDfBknGLIOfXIRzGnG2_9lYYKTx1vlLDT49m9QLfgSHn2DbBLRarSFLnCfIAuBloq-KpwT7D5ozcnGogoc34aP2okbLFc6UvOXtyPWvQIAH4wUue5e7YYdHRGYydmwRplMp84AOLt2rXZLstBRyYi8r_g4zVwRZrkdre5aVIjmcxej4sN19mrSFCbYxI1X7tII5i73Vnu5pc5GyzE9cbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fdd7b86e14.mp4?token=dqKoZ3u8xfs91bCO2wId03JqAaFnSQxllJaEU6dUkHClOvaaLcGPtSKTTcBzXqgZ_HoACuGFOARTjUVH1xez9K-jAesIl-UCtCkXSLE8AUPnXzCe52oMr629kqKSl3oTaaDfBknGLIOfXIRzGnG2_9lYYKTx1vlLDT49m9QLfgSHn2DbBLRarSFLnCfIAuBloq-KpwT7D5ozcnGogoc34aP2okbLFc6UvOXtyPWvQIAH4wUue5e7YYdHRGYydmwRplMp84AOLt2rXZLstBRyYi8r_g4zVwRZrkdre5aVIjmcxej4sN19mrSFCbYxI1X7tII5i73Vnu5pc5GyzE9cbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">پست یه خانوم از اثار کتک خوردنش و 10 هزار کامنت این شکلی...
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84779" target="_blank">📅 15:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84778">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMehdi</strong></div>
<div class="tg-text">بنظرت لیگ دانش آموزان بلاروس پخش زنده داره؟</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84778" target="_blank">📅 15:18 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84777">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">مرگ دختر جوان در ژاپن بر اثر سقوط یک زن از طبقه یازدهم
زنی ۲۹ ساله که قصد خودکشی داشت، از طبقه یازدهم یک ساختمان به پایین پرید و روی دختری رهگذر سقوط کرد دختر جوان جان باخت، اما این زن زنده ماند؛ گفته می‌شود این زن به اعدام محکوم خواهد شد.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/funhiphop/84777" target="_blank">📅 14:48 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84776">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">کل مصاحبه گلزار فقط اونجاش که گفت اینایی که پولدارن ولی مثلا برا مردمی بودن به خودشون نمیرسن و درویشی زندگی میکنن کسخلن
تا خود صبح باهاش موافقم، کصکش پول زندگی خوب داری چته مثل کیرخر زندگی میکنی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84776" target="_blank">📅 12:31 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84775">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=XmTO3y8RFR0YrCqb7QbgfGaEfv3Peas45rw0D-X80NnQIjsb9AYK7kTN8JzPZTGTQLbBgpIqRAlXjzSWNgVQW_PVnpUYlsRpeNjeLM_8rRUv1QdsxWNdXxJ96NzVqHXe6nVKpWOgndQnr-6ShCmvD_4T0UvYMujHV7QiAPkSyhIZzO78_n-zkXlVcovIPIwtMFfFng5AMssy2PJZc1jaRSBBOz3sEuvYuTtCqCGV04Hw8gxhhGjKM129lPdfajb2-h6haYjU1Bq2fKXkL2sYKfeiJUPmDGmzH_WAHWJX9Nr2bXt1RYJhWrpoNkyMNR4XxDuAk7M7KL5AuRWA2eORuCUpB_CJB4SWsTVvb-TTHsZrAbbxICIkNluIyvdYB8t6IB384k3AVp3hfgG9C5hpQoaxDbN-PniPqJVMPLyOM_9XmYKWU5ip2zv8uv_8zHBstSVHGePci6J45eb0z8FbRYO9qcNRGVxz6EsfyujJjVpwqAfgVYTi9MdLr4Ws-MioEOZwfpF_FS5QyvC6DdxuynFWGIIe-tmyV_a_3OIDnSGHlQ1LoZ0xDS9XLZ0pTXs5RatvJMZmbj08cvS8nAsqUnAktUeXjk_znjAWJ3LESfn8tCpv91FJ5sMDyQ_zpapKggSKw9aLwzDPOJg8ECaO_tzDR3FakiniLE6B0Sbeyso" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a93f041f2c.mp4?token=XmTO3y8RFR0YrCqb7QbgfGaEfv3Peas45rw0D-X80NnQIjsb9AYK7kTN8JzPZTGTQLbBgpIqRAlXjzSWNgVQW_PVnpUYlsRpeNjeLM_8rRUv1QdsxWNdXxJ96NzVqHXe6nVKpWOgndQnr-6ShCmvD_4T0UvYMujHV7QiAPkSyhIZzO78_n-zkXlVcovIPIwtMFfFng5AMssy2PJZc1jaRSBBOz3sEuvYuTtCqCGV04Hw8gxhhGjKM129lPdfajb2-h6haYjU1Bq2fKXkL2sYKfeiJUPmDGmzH_WAHWJX9Nr2bXt1RYJhWrpoNkyMNR4XxDuAk7M7KL5AuRWA2eORuCUpB_CJB4SWsTVvb-TTHsZrAbbxICIkNluIyvdYB8t6IB384k3AVp3hfgG9C5hpQoaxDbN-PniPqJVMPLyOM_9XmYKWU5ip2zv8uv_8zHBstSVHGePci6J45eb0z8FbRYO9qcNRGVxz6EsfyujJjVpwqAfgVYTi9MdLr4Ws-MioEOZwfpF_FS5QyvC6DdxuynFWGIIe-tmyV_a_3OIDnSGHlQ1LoZ0xDS9XLZ0pTXs5RatvJMZmbj08cvS8nAsqUnAktUeXjk_znjAWJ3LESfn8tCpv91FJ5sMDyQ_zpapKggSKw9aLwzDPOJg8ECaO_tzDR3FakiniLE6B0Sbeyso" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فنای گالاتاسرای دیشب جلو هتل بارسا:
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/funhiphop/84775" target="_blank">📅 11:57 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84774">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">یعنی هنوز ایرانی ای وجود داره که فیسبوک استفاده کنه؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/funhiphop/84774" target="_blank">📅 11:52 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84773">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from𝗔𝗺𝗶𝗻</strong></div>
<div class="tg-text">ما سیاه پوستیم((((؛
همونایی که…
بغض نمیذاره حرف بزنم
حرف دلته؟
خب حمایت کن سیاه پوستا به حمایت نیاز دارن((((؛</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/funhiphop/84773" target="_blank">📅 11:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84772">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">من دقت کردم از وقتی فوتبالیست های خوب دنیا سیاه پوستا شدن برکت از این ورزش رفته، چرا انقدر عمر حرفه ای ورزشتون تو فوتبال کوتاهه شما سیه چرده ها، ملت هنوز با مسی و رونالدویی که تو لیگای پرت دنیا بازی میکنن کری میخونن واسه هم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84772" target="_blank">📅 11:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84771">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=cI6GNoqdT06n6MCg2dy8M1Pr74zaVkrfk8sTcySxNHJfDrOov8l42jniZ3lTnd763EFMwJ6n0m-LVLWrWPWt9gNDwPmOKNGm5sL6ISNRxYkDxYAAh5cyhTkWwiiTQN1QS88CXv-psc32iPjFW258YgXzvzqiajglT9b4heN0FKxPySYPwCRyFs0Bba3iFYLSCBYwHlkhxmx6eDoVqrN0f3M-gag0cGKYmkGrNPQRg4gam3_eyryPDLiZGCHJh6qd-OsXWHOJ0XXnGS1WuKPp7KS-zdo0kxGM1fDHocwEGKeJy91_YLnu9kd2x94lgEVyDD3Zyj_B3JXxcN97SoeW2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5f888102f5.mp4?token=cI6GNoqdT06n6MCg2dy8M1Pr74zaVkrfk8sTcySxNHJfDrOov8l42jniZ3lTnd763EFMwJ6n0m-LVLWrWPWt9gNDwPmOKNGm5sL6ISNRxYkDxYAAh5cyhTkWwiiTQN1QS88CXv-psc32iPjFW258YgXzvzqiajglT9b4heN0FKxPySYPwCRyFs0Bba3iFYLSCBYwHlkhxmx6eDoVqrN0f3M-gag0cGKYmkGrNPQRg4gam3_eyryPDLiZGCHJh6qd-OsXWHOJ0XXnGS1WuKPp7KS-zdo0kxGM1fDHocwEGKeJy91_YLnu9kd2x94lgEVyDD3Zyj_B3JXxcN97SoeW2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: شعار موردعلاقه‌ ام «گی‌ها حامی فلسطین هستند!» می‌دانید اگر گی باشید، تو فلسطین چه بلایی سرتان می‌آورند؟ شما را از بالای ساختمان به پایین پرت می‌کنند. شما را به بالای بلندترین ساختمانی که دارند می‌برند . البته ساختمان چندان بلندی هم ندارند ولی از آنجا به پایین پرتتان می‌کنند. با این‌ حال، مدام می‌بینم گی‌ها از فلسطین حمایت می‌کنند!»
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/funhiphop/84771" target="_blank">📅 11:23 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84770">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LiCwNebYthqGrDxcNfnT8n1VrQ4h3R5iI9mUQ4t7_d-hqmDKyI1nX-FDSddy1bYKyjR2yToVJ2WdfnIC6aAHMF3WQ_SC3a-fS8Z7QScprEq0jzkHc_iYlJQzZCBNXdoWaNImUswYP6n0iZ2nEj4WYrCJgQFFuhQk6uUlIgMV-ngSp7zqNxnQWaWDg9xRtgtY-q9FmALDS7N41zyY-w064MHFj8SHt4W11k5cgvnFyBMTVmpyQfgKLL36Rw54wkY1a4p4EXk_wAZX0njB2rStcL0U8jHT3uIPFNTJe2Fz71dkJZtlCXs4Hw2Ceh_C0PFqcGFSWhHkhrzHXj9qGaNeaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">سایت دیوار پر شده از آگهی فروش سبدهای گل دخترهایی که به مناسبت روز دختر، جعبه گل هدیه گرفته‌اند.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/84770" target="_blank">📅 10:45 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84769">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/84769" target="_blank">📅 10:35 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84768">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=T2RMKcSfU1k5d8gPOTlG9vsL-ZphDUi5PSso2vEbvfkFSqngtXrx_C8pZZYlI3Q1485kYtS8nzE7o-7_8CPLxR59rtZ2By-CNutoyjH3Ea1A0Qoqb9RUhOZy_TJTFujxkI21ucwsuPoGnQqOHpxoTjXuty20R6BeX7CQAbjzBI6HA5KqcmI4YhEzTr2ZwRMAGRAlK10DWm2h5wvN5E3LxLWQdMspwTeyWxACEvALXcM4Ah4_JHImgQZ86xLWqBISUz_UriigS2jb3vFO0atjIwwS0w9ps5zVeGoHFVKhay8b6npSKZpin3NDl8_U5NwqCn2Nn1u8hK9UaYUq9ZRiAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9441c5ec98.mp4?token=T2RMKcSfU1k5d8gPOTlG9vsL-ZphDUi5PSso2vEbvfkFSqngtXrx_C8pZZYlI3Q1485kYtS8nzE7o-7_8CPLxR59rtZ2By-CNutoyjH3Ea1A0Qoqb9RUhOZy_TJTFujxkI21ucwsuPoGnQqOHpxoTjXuty20R6BeX7CQAbjzBI6HA5KqcmI4YhEzTr2ZwRMAGRAlK10DWm2h5wvN5E3LxLWQdMspwTeyWxACEvALXcM4Ah4_JHImgQZ86xLWqBISUz_UriigS2jb3vFO0atjIwwS0w9ps5zVeGoHFVKhay8b6npSKZpin3NDl8_U5NwqCn2Nn1u8hK9UaYUq9ZRiAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثل مسی اسرائیلی نباشیم
☝️
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/84768" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84767">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BgkTi1s7U_EWOAQVcnPWlJNJWfru_HJKhkYmzdA7LsltfwH46oP1ilgjddvHSrYR0W_x32Vfgf_vBBLujOMTSInCjLBry-hganp0xDMjtNS00QQ6K7PW7NTA6lZvvn9JlPJQ8E84_Gql-7Cp6UHBjDGt_q4XijERtsJ1kE--XuJRz4M8TVwAhekDg8IB3l0Uztbm7vTP8EN4va9w_r53P_xwXEnUMaO1aGdjlMloCggWYbCpfSN2gPRRsCH4cY4Qe6MmHl0s5XTc6B1-WMrJMWdJzoNzUUEGXwEFJS5chy68tKyULZoYtK1aGOETvUMoR2w-IV_msjF0HVqRfZ6uNA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r21
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/84767" target="_blank">📅 10:24 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84766">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=HrCdqzrcZPDxytVnozHqaR1jp7XGPQcg5O-dr6f8SyKrbWK-WANdIHei67aCLKQ8rqiNFC177g1tlISJbYYsK14FpuzZQcbv5VotLz11CBZe6-Uacu4jtzypDI0OHf9gYzMGk2E16JyZvPHOHrSGBWqcj3RnUDQ-1JzBC2MWGMZxFOgvpCeF3U8KrtTtq5OJ8MOouVeBP6WEaY6aHiLOT-5mM6PmxoYqHyxPG_G7Ab9NKHB1s2ldP7nKZ6g_rjuE7BmvQrJaKoAseKdOomWk9R9aL0dcdq3RNkQoeYQuRhrSMuqXtYAEtNktfaF7TmI40gZ5eDNFwQly1eil10o0uExhTnI_f6yBb5prcju4BUgBz-6g7poU04_G6vIsDb_z9RjSew4pQufD7WIOHzsebDTIY4SQuvDCAx12ugwbzWwKnEvdm3flOh04vXOhL1CtnZR0-AdYmcaENlbUQMvcXG6DsgqTkDMRhgkeAUbcJoY6lOYKENcMZRE0HO_gwHpaGHK2L0iGMdVu9OHGIRimVsH-ruBLalZYt1Ewi8Od3gLqgcDoYfNaXvkHXp-Rs_CXFP21nfPYLKZo_Phm0-9fytAYPhLjr4iFS4OvncFJRCnlp-_LpLN8Sx8Uo8EbJai5s3I0VZptGXmwKC3jai9b6AqNN-QRLDD-fBkyAV0hLwI" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7babb9a577.mp4?token=HrCdqzrcZPDxytVnozHqaR1jp7XGPQcg5O-dr6f8SyKrbWK-WANdIHei67aCLKQ8rqiNFC177g1tlISJbYYsK14FpuzZQcbv5VotLz11CBZe6-Uacu4jtzypDI0OHf9gYzMGk2E16JyZvPHOHrSGBWqcj3RnUDQ-1JzBC2MWGMZxFOgvpCeF3U8KrtTtq5OJ8MOouVeBP6WEaY6aHiLOT-5mM6PmxoYqHyxPG_G7Ab9NKHB1s2ldP7nKZ6g_rjuE7BmvQrJaKoAseKdOomWk9R9aL0dcdq3RNkQoeYQuRhrSMuqXtYAEtNktfaF7TmI40gZ5eDNFwQly1eil10o0uExhTnI_f6yBb5prcju4BUgBz-6g7poU04_G6vIsDb_z9RjSew4pQufD7WIOHzsebDTIY4SQuvDCAx12ugwbzWwKnEvdm3flOh04vXOhL1CtnZR0-AdYmcaENlbUQMvcXG6DsgqTkDMRhgkeAUbcJoY6lOYKENcMZRE0HO_gwHpaGHK2L0iGMdVu9OHGIRimVsH-ruBLalZYt1Ewi8Od3gLqgcDoYfNaXvkHXp-Rs_CXFP21nfPYLKZo_Phm0-9fytAYPhLjr4iFS4OvncFJRCnlp-_LpLN8Sx8Uo8EbJai5s3I0VZptGXmwKC3jai9b6AqNN-QRLDD-fBkyAV0hLwI" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اگه بادیگاردا این یارو رپره میگفتن خلوت کنید آقای بولینه و نمیذاشتن طرف نزدیک بشه، دو هفته مغزمون گاییده نمیشد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/84766" target="_blank">📅 08:33 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84764">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=mW3bGIf1ZNsz1annWiUo5oVfRa37YtXpMAgx4QLLWe6n2qzFwETBbqPosdQviuc08ZPqqPvWXN4vDryozNmnJyyQL-5iKYdiNyexXlBopCAmFafLP3xJl91zhbc7HHg2IB__iqUp2s_M6j_Zusg5Z-ZaUrLcr49qY7Zb_91Byu0NlZa33HyR-yQAIkjFugB15QkEKjokSU0UEXBhCH4J4-_VmY5vWd_31qpVF2P4cpc4VfQ_nFTJDJXWgfpGApVZo5uAi_6lzBEYp1IwY_AX5KVvdOmAPraqiPT5o7r0SyCtyVY50qytVMgfGZ_70jITpP4LTA-W1cPr9r5kVtOpyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f656ec5109.mp4?token=mW3bGIf1ZNsz1annWiUo5oVfRa37YtXpMAgx4QLLWe6n2qzFwETBbqPosdQviuc08ZPqqPvWXN4vDryozNmnJyyQL-5iKYdiNyexXlBopCAmFafLP3xJl91zhbc7HHg2IB__iqUp2s_M6j_Zusg5Z-ZaUrLcr49qY7Zb_91Byu0NlZa33HyR-yQAIkjFugB15QkEKjokSU0UEXBhCH4J4-_VmY5vWd_31qpVF2P4cpc4VfQ_nFTJDJXWgfpGApVZo5uAi_6lzBEYp1IwY_AX5KVvdOmAPraqiPT5o7r0SyCtyVY50qytVMgfGZ_70jITpP4LTA-W1cPr9r5kVtOpyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تورکا حسابی خایه کردن از بارسلونا.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/funhiphop/84764" target="_blank">📅 07:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84763">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=ahLg9j1EC0l7G5i-Bolaf_zodk1CsAa7YNF4rOJBJZLtSJwKrzkn0shd3_C9WgjHsiW_4WWeDqSI52aTemht8V_TGecbv99MrtV_iNvM3Z6ckDVCndpisp2IWnKaAaJWP6CbjmlZVllCJp2uQ7i2NtJSy51ibx1mBdZEQqDijjem3FWRP5_fQTWVaFmPiY83SlE3n-dkoTcR353Z61wPMH_WjjqIYFPA3r4sHn06D1FmvBvbYFjh7vuHK8lSfb9elc1onz1dAjuiXgumI0amTW0fZRNd6UrCQHce-A1oB2I1oiIJwefmqiLz7wM9033Z7QTv92B9r4CPRgGEgw8IWQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aae0b77801.mp4?token=ahLg9j1EC0l7G5i-Bolaf_zodk1CsAa7YNF4rOJBJZLtSJwKrzkn0shd3_C9WgjHsiW_4WWeDqSI52aTemht8V_TGecbv99MrtV_iNvM3Z6ckDVCndpisp2IWnKaAaJWP6CbjmlZVllCJp2uQ7i2NtJSy51ibx1mBdZEQqDijjem3FWRP5_fQTWVaFmPiY83SlE3n-dkoTcR353Z61wPMH_WjjqIYFPA3r4sHn06D1FmvBvbYFjh7vuHK8lSfb9elc1onz1dAjuiXgumI0amTW0fZRNd6UrCQHce-A1oB2I1oiIJwefmqiLz7wM9033Z7QTv92B9r4CPRgGEgw8IWQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مثال عملی سخت کار نکن هوشمندانه کار کن.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84763" target="_blank">📅 01:38 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84762">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uyFIDsoLMSP-w3JfAjLwFD_HkS9Dthlq5uLW1fAk-3UAVw7rMfGQxkhsxnCw4WczK9ouZC7sk0gcL6aAr_K_Ju2ydau-RRqn5YXUa_2eWnZ3I2jLev_wiKbIpTzIIE-6mTrqYiHdq_w6COn0Ddn3udsvwAV0thThyrR8DgigOEbmwpnCq4si5UCw2lf0F5i5XM-BWGN9AVF7LDM6sFO3tbohLR4VoLBIFUKhSJM799GcbAAx3fDbVQqrg98CpGW7cHqxGlxBQqIZPXl4JtE1K5bjVt_3m1-qFYOxEsSvq3PCydPpmiMvp-DGcySCXmY0oeAPW85C8NE-DV8oz6S2zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😂
😂
😂
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84762" target="_blank">📅 00:20 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84761">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">خدابیامرز نقشش تو سریال اینطوری بود که اگه اون لحظه جلو آدم سبز میشد تیکه تیکه اش میکردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/funhiphop/84761" target="_blank">📅 00:13 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84760">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ahFAulmIVR_8HKXo9dRRqRfk6oSDDM_1kjr9Skae2T2TOVOHIf1Zy28lOG1H0xSzFxem7e5E7iwfxpxm-SrIPXvB_XwqbyV2hdmdzDXIsDoN4oPrjzr5ZUKe4lv-RoFPkb1QMpdiNOx_QHueFhGQhG0QQDdW048XD2a3IW3KZkKsuixmerh-ymanA0D4l-X9ik_Tpp3Hl0KSuovz3G02vnZKcKj9HWuYrwodWk1TafVx313xJbxViEjkp2hEqNbNq_60a6kWnT8_0fg8S0pWMHuhMiupvaGkikqlWTDAsU7ACrEfaUpcjPsfdbBzExZQvwSOi8EsMRrQ3JDvnPbwqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بازیگر نقش پسر والتر وایت در سریال بریکینگ بد، بر اثر خودکشی در ۳۴ سالگی درگذشت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/funhiphop/84760" target="_blank">📅 00:11 · 21 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84757">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RUf8me9QdfHC8IDuOSyi2yupsvfHjImon30n9lP31PUIdBLUfrW5vVo1yv2cZnR4ATXWUQslLtEl9m_WI_dz0bg_9A356u2BLYTG-qgeBXzE88F4Yqz7ZSJWtG9mOrsCU6I2GXz62Gd0SXax7B2rchUGSqI37UhKgsaCzpkbi3gpqtxQ4Gl3cFOLp4hT3M3gc2j0RDNe76IXDobNxSrt7KfJ_WgahGFVKWhiND3WSRRFPZVOQqvXJvi7rKa_p85UwwoYuR3t3oh9Yy7_w-EysmPV5SRrEmuajxMYfojMKghdrC-C6m18TRWM6D95QfHdUzeeT_7ZlVoJHpoj3y668g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">داشتم زیر استرس جون میدادم حاجی</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84757" target="_blank">📅 23:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84756">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pHqTPonvDrufhxLL6CUIxeD9GbVl0AR6P6t3XRqZ_o5snbP9yMfqdAl_TfXlpYgL1fMOAXt1ttViypzBaPcS0S0FEFcKUa3dI4tOQutreIeZ2FyGmRzOAtVaMwGNbtgTY_nGESXWCi6xYAsQhWV6BMn06MWs_E1DT_3pp85ztW4ippeuRamrroxhmV9XkGJ_Y5eFCz7hNWVPHAFBPclXIoeK8aKPRRm6ZT3l8P3PHoYmpVBP6pwiqWgggZCTpFWQZT7kNJEZhH3GajzeN01yJjVhXkVa87oQhRpNcnprpuqX3SqYviq1PZvO8Y49donl_hsJorkl5qJstQFCbivR3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شات جدید فدایی و شاپور و رفیقشون ارین بختیاری
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84756" target="_blank">📅 23:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84755">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">حبیب کیرتو بخورم</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84755" target="_blank">📅 23:35 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84754">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/VN93yvN3tMYGx4rGnRGIlUlZSaYtEhb6ROp4rP2h5lJbQVnYk_tPK1jnqVLxFVEKBiaf98QBLGJCnFMxYjRZexPBGg0InCAayaheUgwhYHlAK1LHpxkE63JAhmF23s4geDdW-H06yd1qKTIyYiPVXiFTCiddY4kiqQ8p70qmeOfgki27vTtYl9nKczATonz3D6mXtOVd8c7SU015beklgh9TCDr9_kIPRquPDGGatbN1iGVLguiKv-TguP3XBbB-dLV4JRL1FAvG-Eq0dATmhQEeJCb1N18cRepZWKAxA8bsOopFlFsG8HD_WXLFn5ssKIemL4HQhDkyyTf4Fwv1PQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قیافه رو
😂
😂</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/funhiphop/84754" target="_blank">📅 23:27 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84751">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">هنوزم نمیتونم درک کنم چرا هلدینگ دو میلیون دلار داد این سعید دالگخیزان رو بخره
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84751" target="_blank">📅 23:05 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84750">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SgJnunFp4VJ3XqFZrwnMoxPFRhYFeOU3rYJibS2Vzr_EL2n9NeGZGZg2-vlVYJd5sJ-ixT10qmtK5Q_ieYEr-SEuv-dry47zSmrqrkw6RLv9kFePLzLudEFdnrS3aa0RW_N0R0vXrzoOH--eYLhv4CHqEkeH-bBt4odSCA1IKu_3TF8mDd44wm3-r6j5Aajg0cO2GBDT15ILQ_4SQsQgeq8QELTd4fDXJEwewqsEWPO-UeenA6tJL-HBpt_BLR3Y9d4biLEReskSKGMM9GCGmEWCPjaSmlBJjDISioRqFvnPGohbWmohnhb_uU9NSUK5U4bNvW7GitVTy8KtLi9TVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/funhiphop/84750" target="_blank">📅 22:57 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84749">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">همین روزاس اسرائیل فک کنه یاسر آسانی لانچره بزنتش.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/funhiphop/84749" target="_blank">📅 22:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84746">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/940390f975.mp4?token=uOcaLD7qYhJ_8BtMOpEftg4mySLMKplQHa4vWw3MjnB2Gv0nSvwG4tBGYYFu6GPHs9IHmbLIl5jm97IK_yV9URYZ0HLSmaUHEa-l1YgcHkykRxcuY08Iw28CI0FTfanJoZo0YTtbqcmN5p_Ix_OYFI4eGJGaV3rPQIPYOTgDkKwTuPtxJAorAVd0v0_uyOxMdG8kEGTThSVkh9felg_Tf9tQFx6YSjNU9tpijIiCm5DGkJpajhjyiXvswOEIgCdFzoIwJAUlhk2rvXOjyHX_eh3S-lDGvGD9XvjwaZFPgDaTDBn-0a6BgvWJ0_82b-9s2PsBauFrwgzEtKu2xL0DOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/940390f975.mp4?token=uOcaLD7qYhJ_8BtMOpEftg4mySLMKplQHa4vWw3MjnB2Gv0nSvwG4tBGYYFu6GPHs9IHmbLIl5jm97IK_yV9URYZ0HLSmaUHEa-l1YgcHkykRxcuY08Iw28CI0FTfanJoZo0YTtbqcmN5p_Ix_OYFI4eGJGaV3rPQIPYOTgDkKwTuPtxJAorAVd0v0_uyOxMdG8kEGTThSVkh9felg_Tf9tQFx6YSjNU9tpijIiCm5DGkJpajhjyiXvswOEIgCdFzoIwJAUlhk2rvXOjyHX_eh3S-lDGvGD9XvjwaZFPgDaTDBn-0a6BgvWJ0_82b-9s2PsBauFrwgzEtKu2xL0DOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/funhiphop/84746" target="_blank">📅 22:32 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84745">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=pkainJa1a-SkDRI4k1m6OL7O7hRetr5CpAHhvUcx3CoE8uWQ9fswcBko8qIWibr9n0w1xqrzJyktCJxVja03g01-xLe13R0bXr-_4fKoXoQebAKwxyX4yv_5jZv7sQQgnZWm4IYq2eUG51yjkhwz4Bf9Ly2ngou8BeBCzdNlHni7UX_l6Zc2MeDQPQ9UwBIiYXoA2TV-tIQeQM7bM6yf-7y_reFFOOU95e5x3HDQlZfSA4ritbKS4Vq_viLYJm8pLLoITiSpvZk11v_tTbLYv1_MusxH4HaYeQUcwG30C947ejYEWXgS1_fDyrdsMh_k21EWN-4kOh8iz6q2qtkD3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c170193b1b.mp4?token=pkainJa1a-SkDRI4k1m6OL7O7hRetr5CpAHhvUcx3CoE8uWQ9fswcBko8qIWibr9n0w1xqrzJyktCJxVja03g01-xLe13R0bXr-_4fKoXoQebAKwxyX4yv_5jZv7sQQgnZWm4IYq2eUG51yjkhwz4Bf9Ly2ngou8BeBCzdNlHni7UX_l6Zc2MeDQPQ9UwBIiYXoA2TV-tIQeQM7bM6yf-7y_reFFOOU95e5x3HDQlZfSA4ritbKS4Vq_viLYJm8pLLoITiSpvZk11v_tTbLYv1_MusxH4HaYeQUcwG30C947ejYEWXgS1_fDyrdsMh_k21EWN-4kOh8iz6q2qtkD3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بازی النصر بخاطر آژیر خط امنیتی (احتمال حمله حوثی ها به ریاض) به تعویق افتاد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84745" target="_blank">📅 22:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84744">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">بازی پرسپولیس الهلال بخاطر حملات موشکی حوثی های یمن به عربستان لغو شد.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84744" target="_blank">📅 22:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84743">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">ناموسا آسانی حقش لیگ ایران نیست</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84743" target="_blank">📅 22:24 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84740">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">استقلال یه بازیکن داره اسمش احمدی عه، یه بازی قبل دربی رفت سال پیش مصدوم شد، ساپینتو میگفت به دربی میرسه، یسال گذشته هنوز مصدومه</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/funhiphop/84740" target="_blank">📅 22:19 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84737">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">آسانی نیست استقلال در سطح تیم سالن بچه محلای ما بازی میکنه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/funhiphop/84737" target="_blank">📅 22:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84735">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازی استقلال تو آسیا شروع شد...
گزارش لایو با چاقال اسپورت
🤣
🤣
👇
@Chaghalsport</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/funhiphop/84735" target="_blank">📅 21:45 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84734">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sMhNb83VjST97XDgOtxgl0uCba5mW2D1RZ5wdrEYPPZp73HwHi-EezipTHXzRHN9KGV6IY0aWC1-dsXlUxXNLqEE0BmjTV2eQTtK3gCVB3h1mRJMe2UxqfmvOXDbn2K3v3H6UGxYEIYpyLaWEaBV-xmGTnqVsXdaAj1XciG_KokyVinUH_ha0aSPjf7zNaka9pL-pHVDNCG9yUHn0xE5la1Tayf5IxRL5Tm3a55Oe9nTH8qDm-2oji_eAQOHqEiwwqpVu7k_OKAdeaI_bxNlNINGOKLQDG2BaTktHWnhM-6zMRK0VDKhYuh1PM0oa7JPnF5g14HpkCRnex9sQN1E5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب پرسپولیس برای بازی امشبش جلو النصر
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/funhiphop/84734" target="_blank">📅 21:22 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84733">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=Du1Z4CWN2jSNxdVkzHl-ScRuZLwgwzW-4Wjh1r_eo0FsS4DnMnW1e6d7QJxcBf36AeQ1cI0Xiw3VfbtrN-_1QrqfX2RGJvycgdQj57XS2iRcrTzTseypU3smWwSexZmE0ui0Q8eJ3tRnVJvr85g_hwThX053v2CJZEuaQJEUh0NPmO8pFvRoRZqhyC977WH3jT7crhWc1d4JXdfUs_idzWcYK0YFeject6PqLIN2wN59phjxFSIuUUNfLjuqEWfT1TDZ26ymFZKX2YdnBoqa4mqHqt2ddo9TUVn9xSTJSgrNWpbmejCuiXwF_EgKI6NrrXnXpZMUjM2krooljpY5Cg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2bff24e8c4.mp4?token=Du1Z4CWN2jSNxdVkzHl-ScRuZLwgwzW-4Wjh1r_eo0FsS4DnMnW1e6d7QJxcBf36AeQ1cI0Xiw3VfbtrN-_1QrqfX2RGJvycgdQj57XS2iRcrTzTseypU3smWwSexZmE0ui0Q8eJ3tRnVJvr85g_hwThX053v2CJZEuaQJEUh0NPmO8pFvRoRZqhyC977WH3jT7crhWc1d4JXdfUs_idzWcYK0YFeject6PqLIN2wN59phjxFSIuUUNfLjuqEWfT1TDZ26ymFZKX2YdnBoqa4mqHqt2ddo9TUVn9xSTJSgrNWpbmejCuiXwF_EgKI6NrrXnXpZMUjM2krooljpY5Cg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">آقا چیکارش دارید خودش دیگه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/funhiphop/84733" target="_blank">📅 21:01 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84732">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">هالند راجب شایعات سقوط منچسترسیتی و جدا شدنش از سیتی: خب اگه سیتی سقوط کنه مسی باید نگران بشه، چون من برم چمپیونشیپ رکورد ۹۲ گل تو یسالش تو خطر میفته.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/funhiphop/84732" target="_blank">📅 20:11 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84731">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hUw4M_Fwpgcp2BwJRxtKTOXwR9uyhrdeCk_G5Kk0RA0tfVCPFiopD4zhB7AzHRmfP-I18AKCoDwdrzaaw1H6wozbqjflfVoiW2cKG-57n8VxFqxRTAgG8Mg7Z7vjHFKS_ARdZyAsYkhoXIVYQ68bTusCeXq81Dig9cd47zwIXoQyrXW7nWxeyp0-vXpNRuFF4JL381zaEyYeNwj9fl5mwJeG63SszIMAUvBe9D8A_IuiJHpehxQ8A2ZC8r0hVgYay0BZQXfcalcd6JnKmhihQ-FbauhpVnOeh1evOOQvGG5Se4LdppHBa6eHbE6rz6LWXmodjw-tByOO3_rLH7pzwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تهران رتبه ۴۵۹ بهترین شهرای جهان رو با کمال شایستگی کسب کرد‌
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/funhiphop/84731" target="_blank">📅 20:02 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84730">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=QCex_qXQCtgPKf5jRMac02K23wgTNdqZsRg7ul3KQJxTQJX4-R0xjA0h8w1j4deSjVaGOvuEF5r97TlkSUxg96c_dTAOlc3u5rS8WZHUzLrQQxeS7y2Q6f4owbE3MQ8Zaon6NuNJPHpw__1Dq1nEsc0mYVfrZrxlDXf9vKE-u215xEW-Z6TZ15D0uZB6mgTb-1K4c_3FTnnvJLje-Pf5Ka6k4TJoX2QKEW3Wr4Xf7VNgjxQMJ0fZtZZroy9T2Aodgs5CBzsDMOjUdaPDK3oAFMhdFKdJXp3QCOri4aRvZFbgbPnTFT-PNCiD7aN8LNgIglnBb8SD68dTT6wwe_6pHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eecaea14fc.mp4?token=QCex_qXQCtgPKf5jRMac02K23wgTNdqZsRg7ul3KQJxTQJX4-R0xjA0h8w1j4deSjVaGOvuEF5r97TlkSUxg96c_dTAOlc3u5rS8WZHUzLrQQxeS7y2Q6f4owbE3MQ8Zaon6NuNJPHpw__1Dq1nEsc0mYVfrZrxlDXf9vKE-u215xEW-Z6TZ15D0uZB6mgTb-1K4c_3FTnnvJLje-Pf5Ka6k4TJoX2QKEW3Wr4Xf7VNgjxQMJ0fZtZZroy9T2Aodgs5CBzsDMOjUdaPDK3oAFMhdFKdJXp3QCOri4aRvZFbgbPnTFT-PNCiD7aN8LNgIglnBb8SD68dTT6wwe_6pHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">فک کن برا ۲۵ تومن حقوق مجبور باشی بری تو باغ وحش درس بدی، معلما واقعا بدبختن حاجی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/funhiphop/84730" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84729">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from.</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g4eU3qGnVeKnCgh9QOFOsNYBMllpl9TuX9wEaMuu84TyYZlIkwpUusZbVQxn7Vqsx_T2LOfvRs2ttu2AYtrEePL55J1B3d9oTH-bxE6H-LpC8U8k3tuofh8Ec6Fn20-FlaNSYJibJZJtO0xEJrzkZF1zUXoIFvnQlPs6zr0kAy3e_nx9HyaNXnLZ-VH5M6q8Gen-NAUR8qEIEP0IUW1dMxfEw2pNnB31gGouWhrVE9xLW7oo3XDueJaAYeqxfVWXiH3lgbZXsdnLJUuaUsU7lxivXGPCyKnF2LcFjcGUxEpuVx_oxtvGNZ56kHUUsbaIiTxU6EYrzrxT-zzKRkicVg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😎
۱۰۰,۰۰۰,۰۰۰ تومان!
🎁
🫰
💰
فقط با یک ثبت‌نام ساده در
BerryBet
می‌تونی وارد این آفر بشی!
💰
✅
شرط رایگان دریافت کن
💯
کد طرح تشویقی:
888
💸
شانس برد تا
🔢
🔢
🔢
میلیون تومان
💸
🕔
همین حالا ثبت‌نام کن
G20
🅰
🛒
ورود به سایت
👇
✅
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106
⚡️
کانال رسمی ما در تلگرام
👇
✅
https://t.me/BerryBetOfficial</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/84729" target="_blank">📅 19:53 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84728">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">شاهین نجفی میخواد بیاد استانبول، دسترسی بهش راحت تره لطفا با راکت بزنیدش</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/84728" target="_blank">📅 19:10 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84727">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">نخست‌وزیر بریتانیا: حمله به پایگاه RAF فیرفورد تقریبا به‌طور قطع به دستور سپاه پاسداران انجام شده است.
اندی برنهام اعلام کرد:
«می‌توانم تایید کنم که ارزیابی ما نشان می‌دهد این اقدام به احتمال بسیار زیاد در ایران هماهنگ شده و تقریبا به‌طور قطع به دستور سپاه پاسداران انقلاب اسلامی انجام شده است.
ما چنین تهدیدهایی در خاک خود را تحمل نخواهیم کرد. با استفاده جمهوری اسلامی از شبکه‌های مجرمانه مقابله خواهیم کرد و از تمام اختیارات خود برای هدف قرار دادن این شبکه‌ها و منابع مالی آنها استفاده می‌کنیم.
تحریم‌های بیشتری اعمال خواهیم کرد تا توانایی جمهوری اسلامی و سپاه پاسداران برای آسیب رساندن به ما را محدود کنیم.»
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/funhiphop/84727" target="_blank">📅 18:37 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84726">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">شین: پرتاب دو موشک بالستیک از یزد
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/funhiphop/84726" target="_blank">📅 17:13 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84724">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eLFcNfh-pjrMhyhbI_HuOlBBPSzKbn31WXCrTlXr7MeU3TtQpUoBojTb9qLvmXd95jA8BSM1j97Ki5509qC5NWNHZX57BfYTWFakqcjRKEKWHsfKxeKIqUIdIipz-szaI_FEGxuhwVWUXWVJhVE7PquXV2aGPKGzdqZJoKJYC2aX0wvN4Hev3mkAII-ClOP9tdP9ARbwcGF-5XN3i2_mnghuFv9tPARD_HXhrRu0LZXo9yffOGu18FCMRsp6q4xCKBSwxynNr_wZcedfvCc_z6TNT7f7V-NVj_t0i-i1OrumYwlxjlWmMqtpgcfzbaZH16WXNFahMheTjoSRTmweSQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eWk6tc-AAkRsQrI0hxgf3L3Ja4Yw8fdu07os521fBbz1kx1E2UjI6kcPehGQpbhFaypWfmxiTmidQNLwR0FwH8r41L-An6Wd_961ld_4lLUXmKDwMgG6BcED1Hn9yf1m1uopTF3vlipAfcXXof32WTHtmq4YugGu8Rm8mYnk08Ef5WIWy34j4eW6CsTMJUw2dFFM_r8PmOm-lphkcN5_9owxNlIVPvBsHbsnDWDG8MW3w7iirKkJQ9gz8zhXba-sovzJzX6aB6_87kceNIclQ_jVivcB1kWgAeWp0RZMf0P4Df3zDdNnb5dDs7MRKiQVyOAT_ZlEAUIQ1isSdGRmIQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/funhiphop/84724" target="_blank">📅 16:55 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84723">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=MPiQ-cnzdxrTcreI7rPZX9FKPcqEohlISUJxkXFkwf67lULtq3jDWFJXM3w0dKlqJv4XmwWNVtTOrWIsQFTBIFX9l7wnRnMhlWH1YiERQ89fEKN-BZGDMUJPfwAJVZTxh7PFH-ymWhsoucFoYLunj9r9sKzH9GDFwRp18MCfRWfp1L0Vl1roqW6A2_ubLIB5u_FQzA188D8Z_5ukS5Ue-wg6cmWzIo5uf0-4kGVAyJwShMSnqFaacEh4tSs9S1nR8Zk5aqLZ-B69Wt0PsAm61Z1kikCMvfFeUOAUmkINCnNZ_XrND1xfIj6CvVQmqmyk5NhyKGq9LgDCxC_yNWH63Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/40ca73243e.mp4?token=MPiQ-cnzdxrTcreI7rPZX9FKPcqEohlISUJxkXFkwf67lULtq3jDWFJXM3w0dKlqJv4XmwWNVtTOrWIsQFTBIFX9l7wnRnMhlWH1YiERQ89fEKN-BZGDMUJPfwAJVZTxh7PFH-ymWhsoucFoYLunj9r9sKzH9GDFwRp18MCfRWfp1L0Vl1roqW6A2_ubLIB5u_FQzA188D8Z_5ukS5Ue-wg6cmWzIo5uf0-4kGVAyJwShMSnqFaacEh4tSs9S1nR8Zk5aqLZ-B69Wt0PsAm61Z1kikCMvfFeUOAUmkINCnNZ_XrND1xfIj6CvVQmqmyk5NhyKGq9LgDCxC_yNWH63Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ی نفر تو ارومیه اومده واسه ی مسیر نزدیک اسنپ بگیره بعد اسنپ رفته بخاطر ۱۰۰ هزارتومن یه راننده از ساری فرستاده، راننده و مسافر هر دو پشماشون ریخته:
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/funhiphop/84723" target="_blank">📅 16:39 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84722">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sBca3sAn-SLNW_6tBWeXzxo3UG9QnnONZwK6w-7MILZ96a6XihLGoeL-iP3gA2N7aqDH4EbsHRvEX8IrQGfVcdSPHmK20Fo4P19tBPAD4A-zq0Ijap_JZ67xT7aygz0Bf9P3dh_W_hHt--_onveD5y059zm1Do6Nwy5ekQZZCXDj2_KBPl8jjyrDBMoP4dPWfR63WvJEj-Wdc7L52grRJxfOBnnr6DqaQpW9w1a-iRS42IFcZ20wifbfw6BKjHf1iR25mFoWWjnh9Z6S9bWsEhWqoZmbpFrJ8FowId6FWBcLZbZsrj28Tq1r1MhugEF_bxjkSFZqlk623OQUgEK5ww.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نتانیاهو لایو گذاشته داره راجب انتخابات حرف میزنه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84722" target="_blank">📅 15:33 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84721">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=Lqa0lf1w2Sxy5f36e0q5B0x2jtM4d1GLJjpxP-OfXzoF2ZvtncMHxbTFJgXBBclMf9UVps4_CgMOcVwyCpOeTi7YH2KUXYr4iLpQDWeJIPgQz1Dreyx7jL1crnNkVHag1Tm38ouSM8kUm-wU08W9bxOby8nB4sfvoiy_ARvHw_2eCRgUEJNrpth2VAGMbo50PTfsCMCmBpmN8lWMTw8qorrzhSE1mC5KEr1D6t_gKcvcaNuySAxzaATolt3CPZq67WUv4MNztxwfJ6hnwd_quVCzRR2yr7aqobA5qY08y2Nqy78LsWur6t-zu-ZMySsGzbeegyZDIRaLKWGppnK-SA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/479ab143f8.mp4?token=Lqa0lf1w2Sxy5f36e0q5B0x2jtM4d1GLJjpxP-OfXzoF2ZvtncMHxbTFJgXBBclMf9UVps4_CgMOcVwyCpOeTi7YH2KUXYr4iLpQDWeJIPgQz1Dreyx7jL1crnNkVHag1Tm38ouSM8kUm-wU08W9bxOby8nB4sfvoiy_ARvHw_2eCRgUEJNrpth2VAGMbo50PTfsCMCmBpmN8lWMTw8qorrzhSE1mC5KEr1D6t_gKcvcaNuySAxzaATolt3CPZq67WUv4MNztxwfJ6hnwd_quVCzRR2yr7aqobA5qY08y2Nqy78LsWur6t-zu-ZMySsGzbeegyZDIRaLKWGppnK-SA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تمرین حرفه ای کماندو ها و نوپو تو سنندج
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/funhiphop/84721" target="_blank">📅 13:44 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84720">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">نظام‌وظیفه با درخواست کمیسیون پزشکی علیرضا بیرانوند مخالفت کرد و این بازیکن از اول آبان‌ماه باید به سربازی اعزام‌شود
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/funhiphop/84720" target="_blank">📅 12:26 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84719">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">پزشکیان : داریم در تهران آب زیرزمینی را استفاده می‌کنیم و اگر تهران هم با همین روند رشد کند از کجا باید آب بیاوریم؟ باید برای حل این موضوعات چاره‌ اندیشی کنیم
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84719" target="_blank">📅 11:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84718">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OB5veVQMhKot6dqvBXpjrhJFcYlSMX3NKgle4sF1e_nsc6gNiUd183MS5WRGaq9yjhRKhkWulBwLe4FYsClW3OFLisAHefp-xaf6DSVcBHsGbDLWslVa7lyp08sELqKOiAYMmuYfG1GYHvfG2vONY3JEsgH8lEMmFedgDks5cDbgtQxgwyGhAihpxYCcpXrHtHny7EDscqCFbiX_pP7MMXQYpWVHtecyZYU8m5onjv-6IAeLF5HBF_2yviZDT0cURYQWtaOWDA9bmDiMJh4lAHmvf7Q4sbTlgoEJw3DMcuWnlDiD_a3xll7ln297Kj3Sh9bqv2Re15pyCqPvKtwbow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">😭
😭
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/funhiphop/84718" target="_blank">📅 11:00 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84717">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=WIR3UDvw9i-RMAqjO5gwYuisytoU-XHhSy-MP56y2Wcyv_QWiMGa8Loylx7dezhMlPlUGZ5aaJ_j9ycm8Np-hA6fUM_hHTogD5FyQ3K_Pt_FEzo1bT-WneP8Awcastnqsb6lUSxVdZE3qQgCbAiNSsxhN-b6NwTuWM3ybkTRRup_aSTXbdFdpYDbpk65gXcfjXCMt4vSQloA7Wem3_YMKiaTtLye2d_W80pwDUAE4uTj3VhNnv0dvUIPdYFbd9YK-jREHQe_LZo_dao6Ybxrb7OdRhIXTCuDnHy35HvPS21hltr1uzi_ZQUOE_dgUG0KjrfMn6IMYqtqCFLitwqzmg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/abc4e72c98.mp4?token=WIR3UDvw9i-RMAqjO5gwYuisytoU-XHhSy-MP56y2Wcyv_QWiMGa8Loylx7dezhMlPlUGZ5aaJ_j9ycm8Np-hA6fUM_hHTogD5FyQ3K_Pt_FEzo1bT-WneP8Awcastnqsb6lUSxVdZE3qQgCbAiNSsxhN-b6NwTuWM3ybkTRRup_aSTXbdFdpYDbpk65gXcfjXCMt4vSQloA7Wem3_YMKiaTtLye2d_W80pwDUAE4uTj3VhNnv0dvUIPdYFbd9YK-jREHQe_LZo_dao6Ybxrb7OdRhIXTCuDnHy35HvPS21hltr1uzi_ZQUOE_dgUG0KjrfMn6IMYqtqCFLitwqzmg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بالاخره دختر اومد تو اکسپلورم باورم نمیشه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/funhiphop/84717" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84715">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NP6ESQuX1Y4VJ3DUMG62tTJBYfw-FfJoKTeAsGviwYlnGNTQzK2VrHgmN04BXzbpBBg2Sv2_tuEo9nqrrWFSI8790Yd1ztfQDC4i9G35LQ59Ek9L-We0BiUPX_XSkA8dIriGiIHEkTWZr1JL04GBrj9yBFn0YFg0RvdlRagTsq-cZ7kr70Qh_UVLrnrHqfdmOAXbzd8v7N7GmgMgU5EaIPuLSJbX9M_gVSLN6rA2y-JMzey126125usL0CDlRXAqzbjr1YPRVXsN7vZxx3dRpE6fRhr2CfQ84NphAtPbjujCMAMc6NKbZ7fsMVQr6_xZtD-fg_hXyxNf7uWCbjMl6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚡
بری بت | BerryBet
🔥
مسابقات امروز
👍
⚽️
الغرافه  - استقلال
🌎
ساعت ۲۱:۴۵
⚽️
تراکتور  - الشمال
🌎
ساعت ۱۹:۳۰
﻿
💸
ضرایب ویژه و رقابتی
⚡
پیش‌بینی سریع، تسویه آسان و پخش زنده مسابقات
🎯
همین حالا شانس خودت رو امتحان کن و هیجان فوتبال رو چند برابر کن!
✅
۱۰٪ شارژ بیشتر برای روش‌های رمزارز
🤙
ورود سریع | شارژ آنی | پشتیبانی ۲۴ ساعت
کانال سایت:
✅
https://t.me/BerryBetOfficial
آدرس سایت:
🅰
r20
🔗
https://ikruyxysd.shop/fa/affiliates/?btag=914641_l303106</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/funhiphop/84715" target="_blank">📅 10:47 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84714">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=LdOfNtzBmvGBnAzuYPoNn43c4yDEL8TUz6xiq1_Shg6NIlZYkGZtPEd3jDMIHKEygq7Ej-Y6Wj27tbwGURhk09R6v7ayert1DKnAWAKVtbYdIJl2M1ryRtdDz6ejtzMqmaHFto24Hkxo2djcpKJW8FD0_c250-B6XqJ5BkQWWbir93SPCVXkAUU1B-5BldRrEpObeBKPxgoHatO4uJuOpT3FuUXnjZpp8qgqCXHxrPTrMaevYATMTbQxzrnGBkilQzdK1FnszB1-gkTVA-9SaaEt-9YbCvZOEJ-P_Z6OGzYWF3IZKeztV99GdmygdyZ8ZMmVpXVTj-LdLhju9S0CJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/408b52a61f.mp4?token=LdOfNtzBmvGBnAzuYPoNn43c4yDEL8TUz6xiq1_Shg6NIlZYkGZtPEd3jDMIHKEygq7Ej-Y6Wj27tbwGURhk09R6v7ayert1DKnAWAKVtbYdIJl2M1ryRtdDz6ejtzMqmaHFto24Hkxo2djcpKJW8FD0_c250-B6XqJ5BkQWWbir93SPCVXkAUU1B-5BldRrEpObeBKPxgoHatO4uJuOpT3FuUXnjZpp8qgqCXHxrPTrMaevYATMTbQxzrnGBkilQzdK1FnszB1-gkTVA-9SaaEt-9YbCvZOEJ-P_Z6OGzYWF3IZKeztV99GdmygdyZ8ZMmVpXVTj-LdLhju9S0CJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قرار دعوای دخترای دهه نودی بخاطر یه پسر
انگار یه دختری به دوست پسر یه دختر خانوم دیگه تو اینستاگرام ریکوئست داده و همین باعث ناراحتیش شده.
@FunHipHop
| Mehrdad</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/funhiphop/84714" target="_blank">📅 10:25 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84713">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">روسیه حرف ترامپو به چپشم نگرفت و به نیروگاه برق خارکیف اوکراین حمله کرد
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/funhiphop/84713" target="_blank">📅 01:31 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84712">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">به رضا پیشرو ميگن: از مسافرت برامون چی آوردی؟ ميگه: تشريف.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/funhiphop/84712" target="_blank">📅 01:08 · 20 Mehr 1405</a></div>
</div>

<div class="tg-post" id="msg-84711">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">بچه‌ رضا پیشرو یک ماه دیر به دنیا میاد، ازش اجاره میگیره.  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/funhiphop/84711" target="_blank">📅 00:45 · 20 Mehr 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
