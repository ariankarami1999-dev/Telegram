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
<img src="https://cdn4.telesco.pe/file/U7qvtq72NWbF3y0_-ZK86TGkaJa0r0jGvHfUpRDvlKwJ_7PCf6nBuwVaOkyDPOl77B7Xdvror99B8W0BummUJVxpgwKMoMzZt5g7Y3zHf_MspIdZXxnM7iqXbCyZ01D8jRHjOVpdj29mSQHn5h9UNYEXzWuKd485g5F4ZQCOXtCTVjBrznmJ0ciJcCiT36aSpE3QYEFTGZsBnnkvPaPr6_JtCDptZZGZBJzHzIVihMAluzuIuPd6XDhI5gYC6y23C5t1bU077zL1CYstXH_T0eBiEKNjxw695y6CC4IDBSs9dp0vPkzIVzPLf3WoiO4soPEFN057piWRWF4gQZftmA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 اخبار جنگ الونیوز AloNews</h1>
<p>@alonews • 👥 956K عضو</p>
<a href="https://t.me/alonews" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 با الونیوز از اخبار جنگ و وقایع در چند ثانیه مطلع باش!اخبار جنگ بدون سانسور در الونیوز👌جهت رزرو تبلیغات👇https://t.me/ads_alonewsپشتیبانی کانال🕵️https://t.me/AloNews?directادمین کانال🎩@AloNewsBotX:https://x.com/AloNewsBot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-03-31 01:30:28</div>
<hr>

<div class="tg-post" id="msg-129474">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=q6hB-jnR5aiJrF5ZPHl_2keYsWEASDXXBKb6aEBVAv-RUFvER0iXR2NRIxrvp_7fWxjUGbpvJDR8Gp2MVT629mSSUTJ9kpuphTFJ18nc4WLbIQuGyhkH3KMiR4KbF19kd0GRmjkk8HqU_7bve-zWoD19y2cwgIacDiJyyaVYZiWXaXSV5DuwTzIRnCI8lNFjAAfZo38YTcwee2ehG69TZXH1_NU5ywIKSbPXu9aZWq-jbqvu2N5YkChqMhcVhVC7WLxciGLoteoLGpgglmIDaHnvyDjYNKdjpRbm6kmFmqIHrb_acdJbPm5xQpOgLwVcObaLIrDIKkcNCC9jCyiZBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e23c2d0b89.mp4?token=q6hB-jnR5aiJrF5ZPHl_2keYsWEASDXXBKb6aEBVAv-RUFvER0iXR2NRIxrvp_7fWxjUGbpvJDR8Gp2MVT629mSSUTJ9kpuphTFJ18nc4WLbIQuGyhkH3KMiR4KbF19kd0GRmjkk8HqU_7bve-zWoD19y2cwgIacDiJyyaVYZiWXaXSV5DuwTzIRnCI8lNFjAAfZo38YTcwee2ehG69TZXH1_NU5ywIKSbPXu9aZWq-jbqvu2N5YkChqMhcVhVC7WLxciGLoteoLGpgglmIDaHnvyDjYNKdjpRbm6kmFmqIHrb_acdJbPm5xQpOgLwVcObaLIrDIKkcNCC9jCyiZBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
مجری تیلیوزیون: باید فرودگاه مهرآباد رو ببندیم تا هی نرن مذاکره کنن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/alonews/129474" target="_blank">📅 01:29 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129473">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">👈
مراد ویسی: نباید به ترامپ دل میبستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/alonews/129473" target="_blank">📅 01:19 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129471">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/avEnkuKAXFLr278EaBtJbjbQylujxFeSnFsk_3i-a_CSQfeRdSoCitRgZuKYbXyK_wxulXsLemtiRnqyFEQPJZYospTxxmr8twVsYux1NChyJSaDMZe-Plvkrp24wsWBjb5cNsA7vdZKftDBBnBMsRnzxrTZMkPxSp44gW6cTWicSp5ol1MRdhIOlAVioqR0lTLler7pBhwviZseONRCq70-iMfCDhtq3jMEEpTX-Z-QtPAHTVglsX-nDXxKF8NSwQao6hXNdaGXIBQG0Vai_sMJ3k90lh3oxsQzvpBV73fVIbO7grAhJcdCOWw92x9NgfCpC_MSPkJ8sFwmJ_4JWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lPaig20EHcGRCI9oMh_qucYtwnKZTXl6dTPTNflQbo_2ZxpZZUaN0Y2aW0DBJfssg_ZVH1UaXxHDpLYw_n7RI0rcF9VcS5BMoJpFzRKqGq-fHMKVirvL9qXfDmP7_PUS_NIWjjgEWaMC913XUoj4gCckQfjzzWtwu-dZY936aB0qluI1MebHgDgQ7_7VrW38qzIWCH3wSdGTzoLB6YKukhZiMfg-5Em_65yYz7mlw3papD50rDOF7oTwbdWbCZrw-Tt2k_vJ9_k1gc-TExsEqIx6H2O1sjTt5nvv4WjpZ2Te25ZlKeXN6LczYsrioQzqSuSAJxoLpV8xqUmaB9f1ig.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">یکی با پرچم استقلال تو استادیوم داره بازی آلمان - ساحل عاج رو نگاه میکنه!
@AloSport</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/alonews/129471" target="_blank">📅 01:17 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129470">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=q9fKgTxPh6gSlnD3NEUA6kNE4KyeF4ybOKKHo9U-8s0Pof940PDkHF7H-gVEJttx0hJ4_5iTm3MtlosDyKrb8PGWUJ7n_wkBU_c6Y03FklDYMJmyMHgz9qhYTNj0UB52vJMWFc6PZtZWYbXeIGob3DCRNMHD1K9TT9OFh-AlWU7HAB7tyZagpS7hVxigHpDjoYvUC7IKjHyhp01gwCXFJ25KImJ7HjJ9fCQTirFH2LAd23TQ7w5oxnbbwXH4W6HxFoo0y1F_N1fF2VbsyySv06yZElz09DUmA56wOBBrPZoVm6Qdqa1EQ8081_UANXmhH6vo0bRYky1qN_zyEKcWwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8f4b679b.mp4?token=q9fKgTxPh6gSlnD3NEUA6kNE4KyeF4ybOKKHo9U-8s0Pof940PDkHF7H-gVEJttx0hJ4_5iTm3MtlosDyKrb8PGWUJ7n_wkBU_c6Y03FklDYMJmyMHgz9qhYTNj0UB52vJMWFc6PZtZWYbXeIGob3DCRNMHD1K9TT9OFh-AlWU7HAB7tyZagpS7hVxigHpDjoYvUC7IKjHyhp01gwCXFJ25KImJ7HjJ9fCQTirFH2LAd23TQ7w5oxnbbwXH4W6HxFoo0y1F_N1fF2VbsyySv06yZElz09DUmA56wOBBrPZoVm6Qdqa1EQ8081_UANXmhH6vo0bRYky1qN_zyEKcWwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لاشخوری عجیب ایرانخودرو
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/alonews/129470" target="_blank">📅 01:02 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129469">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/W0SknVvH3uCDbhCVu-wYJOuu1JRGAtEXRBsExkyqAFgR-gdE2rHoTZZPXbZJgwJGu5GFqOCKtH1KB1pdo2oHgDbVKfivDBXClAsudS7Ddjk2VukAZmnZCdezs7tj9CPnB_lnBXngzEj7ySas2dQfwr3h4FazNw_k614RZ7R_cqhr8ZNbd8JXMfacoSOa6P0lTVHGG-OLm0cS_HBO5TF_xvkMzOD0VfejMgeJMo0Xm5oO7ergKPQwL6aD6-kTtc20OWO4EvWPLto7FZLTUxILw3cWjHDDsw-cDNNeAEjRpBYB6bOMb8bBLLPsbquBMVcp32pW_-C1vu97rZgWZQboOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
رسایی : آقای نبویان اشتباهی نکرده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/alonews/129469" target="_blank">📅 00:55 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129468">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">👈
علی زینی‌وند ، سخنگوی وزارت کشور :
به همه کسایی که توی مراسم تشییع و تدفین علی خامنه‌ای شرکت کنن بیمه رایگان تعلق میگیره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/alonews/129468" target="_blank">📅 00:50 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129467">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gCtxSvUtXBMCU3Evgpq6cd0b3c1OXpV1vEc4ygeKvllTCHw8Jkdgfg_nCzIh5RXNKxIXEZmmj-O7z0zCr5DEgvfEbJ3J1g1cIqrTOUmXykHeUhU8PsMGSKuDNIRz463KZqmIqAu6Y9GTqaaKp8R4GFlT48GK3ruUchdRvx2Z9Jde9z0M2JzAB2RwK_ga31MP6XekPh0RP9e14Dj1TjM9UnOU5kUuB8bnprV5-jhYV3pAB_vtpOyuD3veswPMAVKGAZ88qpM8c8cG8Hi2dQ-L7DTj9JccBVOsbUhvZrRKY9ZvZfmXjwWkWbsPkNg3xVWJ1nZRIGyYb4v_uaL5RPc7kA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
قالیباف بعد ورود به سوئیس:
کودکان مظلوم میناب و تمام شهدای ایران عزیز را هر لحظه ناظر اعمال و رفتار خود می‌دانم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/alonews/129467" target="_blank">📅 00:45 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129466">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H0vX5cNWGx9QmpvvmFH9d2pyfKhcoCqPi3yll_M5H3irnk60-DrFxqqPbmLmMJ_f_ccAxqkF2TCU0N8iHhtypcmLLm1a7xB6YHjYkklD7-XTsGloTDe1FyoNZoBnM995YEB5Y8D6l6xT627LecjtKaDnihN0GKJ1XjbQojSGe1TkK-qy8Lz_Y4AvZIUQRV_OWhoosOwhL4XJ3DmPeEijWtMU8azyx2Zs-IuP-9nc9WOowUkAF0DpjOaT9puuUktn9zIshu3YXqtEhy0HRydu53pDqzGR9MXGcrkj49Y3as93FK_CB70YByKOkAaA5Sjn9dOKiWfQ_gelhccp-4WcmA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
این وسط ساعت رولکس امیر نیوکاسل در مکزیک دزدیده شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 33K · <a href="https://t.me/alonews/129466" target="_blank">📅 00:30 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129465">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=OfZ2CuiRhjBGODNDb6nHFc66XtdJp-D5xUiiLiP9Jl-oCa1ia_sxpabLU01tjds9enHJCEf9FIxaVkeXj7tuxIdeMzqZ8yF-2RWRFkn9WU6N5geDN8SR1VjcrBR_GIUv7zTQBQ5ZEtBF8qWfxw8JzVBe0P2KchQyadCsrLTZ2sN_wMy683evHX1_kSMKrjor6gNppyBBD7r5dusdjtkvqKCmwtAaqKOWlNXBY0OjXF0xCc1lorHRswiEeT_z5XAiN1caoX1yLelyJq2wbDFtyiw3AqNROgEreLU86ZReHfeojEoV79cTx5BU_gJobHE87HGmqyADaPE8EL5UfGFwVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/68aa7787ac.mp4?token=OfZ2CuiRhjBGODNDb6nHFc66XtdJp-D5xUiiLiP9Jl-oCa1ia_sxpabLU01tjds9enHJCEf9FIxaVkeXj7tuxIdeMzqZ8yF-2RWRFkn9WU6N5geDN8SR1VjcrBR_GIUv7zTQBQ5ZEtBF8qWfxw8JzVBe0P2KchQyadCsrLTZ2sN_wMy683evHX1_kSMKrjor6gNppyBBD7r5dusdjtkvqKCmwtAaqKOWlNXBY0OjXF0xCc1lorHRswiEeT_z5XAiN1caoX1yLelyJq2wbDFtyiw3AqNROgEreLU86ZReHfeojEoV79cTx5BU_gJobHE87HGmqyADaPE8EL5UfGFwVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
جی‌دی ونس :
«من مشتاقانه منتظر شروع مذاکرات فنی با ایرانی‌ها، پاکستانی‌ها و قطری‌ها هستم...»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/129465" target="_blank">📅 00:25 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129464">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=cbH4X3V4ymIRoMVlBGP4n-dOU5cRxBzxdwTaeSBVH4bSd368EPbI_55YR0uDw2b1zdSNXEtOTKoBpqR8ar7vV2lKw79TTIOanh47-QX0FK0A9ojeKid6NEhKgmFEmS7Sa4_OTGUxZsVqSPa9ez50mJQLFByqZOJ319xEF4whPHqCBSJhTKTSEqyHSFjuI5Xgfda4-BJmjChSNehYAgOTwnCTU7S6MegBcOp995KR_YDT6suGoGNSXDcjW_wMf7XQ0BCkacJXRlf3KDkQQ4ikZykDHHzn1wTzeEcD-o5XPElENHUtAfDRUcA7SmDBW4J4mbB0wZ50AWQHr70Xhp6qvQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f204fb86d.mp4?token=cbH4X3V4ymIRoMVlBGP4n-dOU5cRxBzxdwTaeSBVH4bSd368EPbI_55YR0uDw2b1zdSNXEtOTKoBpqR8ar7vV2lKw79TTIOanh47-QX0FK0A9ojeKid6NEhKgmFEmS7Sa4_OTGUxZsVqSPa9ez50mJQLFByqZOJ319xEF4whPHqCBSJhTKTSEqyHSFjuI5Xgfda4-BJmjChSNehYAgOTwnCTU7S6MegBcOp995KR_YDT6suGoGNSXDcjW_wMf7XQ0BCkacJXRlf3KDkQQ4ikZykDHHzn1wTzeEcD-o5XPElENHUtAfDRUcA7SmDBW4J4mbB0wZ50AWQHr70Xhp6qvQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ویدیویی از راهی شدن جی‌دی ونس به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/129464" target="_blank">📅 00:23 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129463">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">👈
همه رفتن سوئیس فقط آقامجتبی مونده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 34K · <a href="https://t.me/alonews/129463" target="_blank">📅 00:22 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129462">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CdKXpvCiMjm5EHHT78Oq359l7B3Xo9xphPciqscKyEec615uHq8REjVGrBFwMYwC4MJtoW_ubbfVz2P0s2CGICgPnf3GY6eE-vPnaZGUyqiR0vA5s-m1jy1rBo8dXKiyPVYMmaVi8v70lPsKJT1RxlaQ42llmvq-A76AMPkj9Uyo6jEXdITuZLYqXlt_2K65Rx87H9HZHznbl4W9pY0YGUwve7GG7edZORbsRxerEFmYkp_GP5Q3ivA8ow8jCPOM1qRNIsrY5OOD7kTlqB9o45GuGi48761IEoyX7eCGDFVkdhRqevUS0vS0YnFx32y5JO2zQ_j8poMk9qSd2C65GQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
گویا بعد از اظهارات ضد امنیت ملی توسط نبویان، تنگه وی هم اکنون درحال باز شدن است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36K · <a href="https://t.me/alonews/129462" target="_blank">📅 00:16 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129461">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=voVbdE9FJJtD1_zJ7tn8ZFgU-bXwhbvLsvROiGlcS7Fze53ZBRENR35ZRXVPkkhtrGu-6BIacAXRhTaPy9vORTsMb5aZo8Q8N4Q2ZEUeCpr3-iuYkCjTvNtIlIG1_XgkKhWlr8gtiQg3xsdPNlpRQkXGwZgzHFH2KhgGtUfwp9xGNKsO2aqMZCKoUVUMuk2QgeWaK3pOgQCoPDVUDdbfQuRE6IHJs7P2rBF1G4BEW0wec9CsYywYyq8vsPbnKljPBg4SdvRtaSsNct-fcsIY4k4VLmHeztQk4EiKHwGHwdrt_qbAhyRmB-xMM5jVhvUp3xIB_EBGWjbE-XBBUbdrqw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ae9096e084.mp4?token=voVbdE9FJJtD1_zJ7tn8ZFgU-bXwhbvLsvROiGlcS7Fze53ZBRENR35ZRXVPkkhtrGu-6BIacAXRhTaPy9vORTsMb5aZo8Q8N4Q2ZEUeCpr3-iuYkCjTvNtIlIG1_XgkKhWlr8gtiQg3xsdPNlpRQkXGwZgzHFH2KhgGtUfwp9xGNKsO2aqMZCKoUVUMuk2QgeWaK3pOgQCoPDVUDdbfQuRE6IHJs7P2rBF1G4BEW0wec9CsYywYyq8vsPbnKljPBg4SdvRtaSsNct-fcsIY4k4VLmHeztQk4EiKHwGHwdrt_qbAhyRmB-xMM5jVhvUp3xIB_EBGWjbE-XBBUbdrqw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
تصاویری از ورود تیم مذاکره کننده ایرانی به سوئیس
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 38.8K · <a href="https://t.me/alonews/129461" target="_blank">📅 00:11 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129460">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">👈
ونس هنگام عزیمت به سوئیس: امیدواریم در مسئلهٔ آتش‌بس در لبنان پیشرفت حاصل کنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/alonews/129460" target="_blank">📅 00:10 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129459">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">👈
هیئت مذاکره کننده ایران وارد زوریخ سوئیس شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 37.8K · <a href="https://t.me/alonews/129459" target="_blank">📅 00:08 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129458">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🔴
فوری / جی‌دی ونس، معاون رئیس جمهور آمریکا برای پیوستن به مذاکرات بل ایران ، واشنگتن را به مقصد سوئیس ترک کرد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 40.8K · <a href="https://t.me/alonews/129458" target="_blank">📅 00:03 · 31 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129457">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🔴
فوری/ بی‌بی‌سی‌: کیر استارمز نخست وزیر بریتانیا دوشنبه استعفا میده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 43.9K · <a href="https://t.me/alonews/129457" target="_blank">📅 23:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129456">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">👈
حسین پاک، خبرنگار مستقر در لبنان: ساعاتی قبل عملیات نظامی از سوی اسرائیل متوقف شده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129456" target="_blank">📅 23:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129455">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">👈
خبرنگار العربیه: کارشناسانی در سفر ونس به سوئیس او را همراهی می‌کنند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 44.9K · <a href="https://t.me/alonews/129455" target="_blank">📅 23:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129454">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">👈
محمد مرندی: ایران آماده است تا برای لبنان از توافق چشم‌پوشی کند، زیرا از متحدان خود دست نمی‌کشد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129454" target="_blank">📅 23:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129453">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hB-kHVE5_Eon0Mdlf3Cez3LuM22yY8Am5GYa-cjU8zJvU5YNdWIIJvjqWmFqVmL9t1LVxGVP8EYber2EFGdf8evXtYCQM_nJnVVpumwFM_tieL3RsJTfDhg7XB0GSdrb-tny15fFKk4OYGLULMYcDTP9L9yQKyY3C7jZNLRue9QcJsHNUDIq-82iht2Dz5ANvUedd1q0f1TfRdQb3TmLgwU0O_juiwMM3AmHBn9btybdpRym5P1gcWbSvfO66rfsiyH9j_EeeojY1OsUvYLYibcZ0dPsRENNnffVgEIJ8M2av7KOCfpjec5IFtHhKbnwFAtK79Tjn_0kPalTHNsZ6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مرندی، عضو تیم مذاکره، خطاب به پست ترامپ : هزنیه‌ای وجود داره، این قطعیه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129453" target="_blank">📅 23:24 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129452">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">👈
ونس: ما به مذاکرات ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 46.9K · <a href="https://t.me/alonews/129452" target="_blank">📅 23:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129450">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">👈
هواپیمایی حامل هیئت ایرانی به سوئیس رسید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 45.9K · <a href="https://t.me/alonews/129450" target="_blank">📅 23:17 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129449">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">👈
کانال ۱۲ اسرائیل: تصمیم به آتش‌بس در لبنان بعد از فشار شدید آمریکا بر اسرائیل گرفته شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 48K · <a href="https://t.me/alonews/129449" target="_blank">📅 23:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129448">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129448" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129447">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">👈
رسانه اسرائیلی آی ۲۴: پشت در‌های بسته در اورشلیم، انتقادات تندی متوجه ترامپ و تیم مذاکره‌کنندهٔ او بر سر رویکردشان به ایران و حزب‌الله شده
🔴
نگرانی در اورشلیم این است که ایران قصد دارد از هر توافقی برای بازسازی اقتصاد و توانایی‌های نظامی خود استفاده کند، در حالی که امتیازی اساسی در برنامهٔ هسته‌ای‌اش ارائه نمی‌دهد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 50K · <a href="https://t.me/alonews/129447" target="_blank">📅 23:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129446">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FKF90eZzE8HiAwSnBp5u0lTjektcdsgrRTkuPkTcgJ4fY_zBml9mKDkJzSlNQo-LB-1Pbl8V5Fs_dynqHd3Xs_Qa8Vq-WZH_r3iZVIlBmUYi_jB8OJVM9VofqiAIpPF9tAwl7FFMPwMtzcojIhEgWSQX533IAgoJaDWVUs8PUZZ3cMHr6TMJifx-DlIniheo0DcczKTAZnpzVNuuejdu8CUaYwGEopay0aAUu-TBnVIuFSS5dQ5xcM-C4fJmC3IqnGoB1iExMaDmTwPs7vU5L3E24WzmlXReXeZKn3qQBrqU2GpNFIDsGC3ynyHFTX66CKmdRestUV2T-NCPOLm-6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: در تنگه هرمز در طول ۶۰ روز دوره آتش‌بس، عوارض گمرکی وجود نخواهد داشت و پس از پایان دوره ۶۰ روزه نیز عوارض گمرکی اعمال نخواهد شد، مگر اینکه توسط ایالات متحده آمریکا و برای آنها، در صورتی که معامله به پایان نرسد، به عنوان خدماتی به عنوان فرشته نگهبان برای کشورهای خاورمیانه به منظور جبران هزینه‌های گذشته، حال و آینده اعمال شود.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129446" target="_blank">📅 22:49 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129445">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">👈
کانال ۱۲ عبری: آمریکا در مذاکرات فردا به دنبال دستیابی به توافقی برای بازگشت بازرسان آژانس به ایران است
🔴
در صورت موافقت تهران با بازرسی آژانس از سایت‌های هسته‌ای، آمریکا چند میلیارد دلار از اموال بلوکه‌شده ایران در قطر را آزاد می‌کند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129445" target="_blank">📅 22:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129444">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">👈
الجزیره: شکاف فزاینده بین ایالات متحده و اسرائیل این هفته به اوج خود رسید.
🔴
مقالاتی در نشریات مهم اسرائیلی منتشر شد که ترامپ را متهم می‌کرد که پس از امضای تفاهم‌نامه با ایران، اسرائیل را به ایران واگذار کرده است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.1K · <a href="https://t.me/alonews/129444" target="_blank">📅 22:37 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129443">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">👈
ترامپ‌، درباره نتانیاهو : من کارت‌های ضعیفی درباره نتانیاهو دارم
🔴
من تصمیم می‌گیرم که اون تو انتخابات برنده شه یا نه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129443" target="_blank">📅 22:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129442">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QALGGI9ces_-GVPvby1ghVEmfVo3O7RgBzfZimwqFOWELW0YX1jxz38TOwNv-wyNcgebTgoND-dcgMHjmibI7MaQGorleOipcHQcAooUdRbM3swKh9-b6GdLOWftISid2iRWrUwfOT3ypOhrkoRaJ85hpuwf2_YYFZEWScjWK1IBg_ez8K3RV72uUW-EKg6ycLpxL2ylemjf5GQX7Q029xddozi710laTrCDVO6-Iy33k7bSZOtu9CD7-LzlFaJyEr5dabMafgVSP2NHapEod5ZFfJxfRcT5hHCb6OZ511kQHaxuLHulllkgzq9IJ0GLiDeIQEad7rGOa8MCQlcc9A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
توییت جدید نبویان بعد از مصاحبه ناقصش توی صداوسیما
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.2K · <a href="https://t.me/alonews/129442" target="_blank">📅 22:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129441">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">👈
کانال ۱۳ اسرائیل به نقل از یک منبع دیپلماتیک: پیام آمریکایی‌ها به ما می‌گوید که در لبنان دست به تشدید نزاع نزنیم تا زمینه برای گفت‌وگوهای سوئیس فراهم شود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129441" target="_blank">📅 22:19 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129440">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">👈
بیش از ۱۰۰ نماینده خواستار استعفای کیر استارمر شدند
🔴
روزنامه تلگراف از افزایش فشارها بر استارمر، نخست‌وزیر بریتانیا، خبر داده و نوشته است که بیش از ۱۰۰ نماینده حزب کارگر خواستار کناره‌گیری او هستند.
🔴
ستارمر اما هنوز نشانه‌ای از عقب‌نشینی نشان نداده است. او روز جمعه و بلافاصله پس از اعلام نتایج انتخابات میان‌دوره‌ای، در واکنش به سوالات خبرنگاران درباره آینده رهبری خود، با لحنی قاطع اعلام کرد که در صورت بروز رقابت داخلی برای رهبری حزب، «وارد نبرد خواهد شد و از سمت خود کناره‌گیری نخواهد کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.1K · <a href="https://t.me/alonews/129440" target="_blank">📅 22:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129439">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromAlo Sport الو اسپورت</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee12760742.mp4?token=dNaSW3K7eAVce5ARZPLOCXYLCGxIwsXRLEgObzRYP0l6_5MNrMX6gvxOE76PaznIGkKbCd7RV34-nuePa3aqSwymqniox9ILscKoEUdUMZPfcWD0Kk-qO31_fXa-eZF0-iPPj0UFNJ9QuzPTi240i_XoEbyCSZJbrysyV14nauWTV9kf54LuUvQ5bj2Y7U9mgR5sNCuf0Pz3S_SDXVPSTgAQRa9Rs1krIGX_a6eqTt30ZmUNdE4jG-Mxq2Ob_05uQ1T7tNHAiyIY6Qt55J7P94dcdpLwlfpcbLY2Wl4p8ckbLINAzUclJPkNaeKmjCReg-udVdm0ksxSihFnOfQ86g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee12760742.mp4?token=dNaSW3K7eAVce5ARZPLOCXYLCGxIwsXRLEgObzRYP0l6_5MNrMX6gvxOE76PaznIGkKbCd7RV34-nuePa3aqSwymqniox9ILscKoEUdUMZPfcWD0Kk-qO31_fXa-eZF0-iPPj0UFNJ9QuzPTi240i_XoEbyCSZJbrysyV14nauWTV9kf54LuUvQ5bj2Y7U9mgR5sNCuf0Pz3S_SDXVPSTgAQRa9Rs1krIGX_a6eqTt30ZmUNdE4jG-Mxq2Ob_05uQ1T7tNHAiyIY6Qt55J7P94dcdpLwlfpcbLY2Wl4p8ckbLINAzUclJPkNaeKmjCReg-udVdm0ksxSihFnOfQ86g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زمانی که تیم ملی، تیم‌ِ ملی بود
@AloSport</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129439" target="_blank">📅 22:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129438">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">👈
المیادین: هیئت آمریکایی پیش از اعلام رسمی ایران وارد سوئیس شده بود/ کوشنر دو روز است در زوریخ منتظر تصمیم تهران است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.1K · <a href="https://t.me/alonews/129438" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129437">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">👈
علی الاصول، هواپیمای حامل هیئت ایرانی تا ۱ساعت دیگه به سوئیس میرسه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.1K · <a href="https://t.me/alonews/129437" target="_blank">📅 22:08 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129436">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uL5lIlinbZPfS-igWgmGyMAo4DmGrW9puWQaEVNNOxtWm3MNKrsV4cLCXGkbJMc2XphJ8-zTSRrFFtKUp6UpyatDSC7PE8AimfmbNa7us3qcWtm-LgQ1V3XjuDuCeeIdEdzF6MwwLveRtUC9Fb3ww4YX3r6kWUurBHix7rtDjVEDxr9y5G2LNKE2bM96RnimBG-aDxAb4bIDy4wtzBSslicBR38xKT0XtVQoRbnBcbR6tYuJA14rXayEjdy9K35mVvhUxcpqsX5OYJuMXFyhuNmH8GOaMYfd5knbAu0hVVuwLLuHX-CO5k4g1HxnNP7kAhlza3M4SXo3cWsn01EzbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ماشین های تک سرنشین وارداتی جدید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129436" target="_blank">📅 21:58 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129435">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G8MFYOsoxesbAcVwnupGMKCpqTD0bdgYTXUwc9hu1Vcs92-8NZzMsmXxUEk6qP4VdC604IvhSQWTPG-Mnr5T7OrBWCrYWv1gVgAoirBxZh4hOaukd6W1ZKRGaSjOXLQXhKsEaFTSjPColBq-NqUZkwmDSIICoJO7el2w5Yt6LJsh5vgwlYG1fzh8mF6_PgttdmYjxS55yFf0EWb53mdrkrva8eQI2oZTUQLqsUESEADwd6OuCyWAo2Tc7hkShz3kpKqBoyb_JinRW4T8MFrNkkO3JNQQ7tR7IFT4Qg1vTlgo5hzBjjMu0G0xQDNNaIYEfi9cdGwX63Wcg59IRtJtRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خانعلی:
رهبری میگفت باید جنگ رو ادامه بدیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129435" target="_blank">📅 21:48 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129434">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">👈
یک مقام آمریکایی به الجزیره گفت که ارتش اسرائیل به سنتکام اطلاع داده است که به واحدهای خود دستور داده است که به آتش‌بس در لبنان پایبند باشند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129434" target="_blank">📅 21:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129433">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RYJ8KajfEehaBbHBmxyG9kNHf6NEMzflyWkj_tk3GjmkLdUSUBiLIdIKRbSHlsAHY7RuIoYb2GQaoQBRDhDeLNLf_1zld-v8a4Ki0hl1e1tiSTXeTNZwa3-C4EEDgS83-m62w1G-evPLSEHXgWZooPJYwPyetFULveLNH_LVydUBckkKc836CWU7zcZlngY7sHbMZsosq2JKxCVUjf0PNzHLuZJxOW1DpIaT9zv-jhYTenbOL1zHJn1CN6HGbm7IoKSJzWzXk9Y_sz1XquRSgfvb0sUBNIzKZqudVQjoMVP-kItZ5QW8J-JP5XScMJKHo70sF_IlkTM21oGgKCUbig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
چندین هواپیمای سوخت‌رسان KC-135 نیروی هوایی آمریکا وارد منطقه شدن و یک هواپیمای هشدار زودهنگام E-3 هم در مسیر خلیج فارس قرار داره
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129433" target="_blank">📅 21:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129432">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O43QOn7CIjDyzMwVpI_TJv5AoAC0v0Y9WqwUfHPjVB1TdM0FVjhf-HITpGNU9g7fC5StH0Fcq5A1hTjBLb53vYnbxFH8uK3XqwdnQARBteJ9kYEQb0f2whC12C3gUqRmyKjafgpCi8XqPDSB9MPRQcuQBJ1OaPJybCirLKEbTrC61dx60Hj_cihoyPYxJ1r-LuXeJZvGxCnfXsaWvvH6U8kGUvYQ6bwW2ML4KXz2kChmyg07vvHggsomBCp4MASQsfkN6lYfq_2LJ6RwxqT6e5nf5Q6nB4ixG8yoiP3dXiZyYmFksye8jgiSAc3owL2eDxT0DX2pSZuZIGsehOhxKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت ایرانی از آسمان ترکیه عبور کرد و تا ۲ ساعت دیگر در زوریخ فرود می‌آید
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.3K · <a href="https://t.me/alonews/129432" target="_blank">📅 21:28 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129431">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qqw3Ps_hs6wQnUQDcROamzf2Q0Ifn8A4ynD78a2EtaUukKytMOZHQ_TN-2jJ2dE3OZ7EZXyUBxumCVo_TfbdOkxvKABj27PeF3Ymt7_fhUL6euroAy1Joj_V1M0qlNSEsf_rA_UbW3-Aq4MXy1bCIunMoiYddUNaqSoBi9HlBp6dSxjFkxP7QXTYYu4qDUcC3fw-VRgRj_05IDvRkvK1S7ea9w6FQQM7jPO9jim5NtZHMwlVB6erK7CC8E3FEL98o92yGnGvsSR897vcvXtDhavnAYb6sd-7ctb7lUJe71n-wfhi0WxqvExRf-IWQ_eKQc3QlFDDNoDZYMRD08gkGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نخست وزیر پاکستان و فرمانده ارتش پاکستان هم به سوئیس میرن
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.2K · <a href="https://t.me/alonews/129431" target="_blank">📅 21:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129430">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.3K · <a href="https://t.me/alonews/129430" target="_blank">📅 21:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129429">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=IPNVlHe2MJsNW_pkWQr3PuuExy1RmcKyLXhBy-UU0_nUEsiYSvUrObHEoCGKsHpx3jjsMg-KhBfuN_HPX0ung92MjxzVzygko9HIMEEfelR_foHCQgiQbd2ymS5UQ6p2690Zo5MuzwQWlBddF2j18OVgFBhE3G2e5X16c0fxrRi6s9xTdz8G2XRM_wyHoQQiViM6qz2xm4iWnrey1ZbDP4nM65q-nKdd58BfOE6Xe1WJ1g9Ab71yn2xxvmZKkGRiojj-p8fapB5P6UEu-vKToaR1Q6TWFXD8jVOM7eg5haotlzZQ9VFnW7l6zkDppuC2QzpQS2Q6oTWqjcgFjIlEyA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7dac5f9d1b.mp4?token=IPNVlHe2MJsNW_pkWQr3PuuExy1RmcKyLXhBy-UU0_nUEsiYSvUrObHEoCGKsHpx3jjsMg-KhBfuN_HPX0ung92MjxzVzygko9HIMEEfelR_foHCQgiQbd2ymS5UQ6p2690Zo5MuzwQWlBddF2j18OVgFBhE3G2e5X16c0fxrRi6s9xTdz8G2XRM_wyHoQQiViM6qz2xm4iWnrey1ZbDP4nM65q-nKdd58BfOE6Xe1WJ1g9Ab71yn2xxvmZKkGRiojj-p8fapB5P6UEu-vKToaR1Q6TWFXD8jVOM7eg5haotlzZQ9VFnW7l6zkDppuC2QzpQS2Q6oTWqjcgFjIlEyA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
لحظه‌ای که آنتن از نبویان گرفته شد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.3K · <a href="https://t.me/alonews/129429" target="_blank">📅 21:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129428">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=ZBDgS6y7hKGTVza8-N1VrzLLoXGcGroRt9UKBcF-Szh0AZmFFick_bgORPDFCEz7J3QZs_7DZ__eFZU4vf73o-UD1A_gxD6lGq0XBse7oqcWx2MZTCAO6O05vAoIFgjzXJtp_ewl-OvTKo11SEwnmZ3M7iID4gwKPhiLfANeAl7Xhh7mdVO5LX3MCoZqV46KehSVyg-PlAqvpWeARAT0l6Y0VLm_5uYLRgK_LWXvfT4w_WOpoUGHWfIGTqKU4esJfPRd65v4E7Zt3xCkxx-CIszt6i0le522NvadDE2qADAhywM6fTtKx8W8DNxIovitK8zE9Om3nYVr-Ztbp7cQJQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/428436ebd0.mp4?token=ZBDgS6y7hKGTVza8-N1VrzLLoXGcGroRt9UKBcF-Szh0AZmFFick_bgORPDFCEz7J3QZs_7DZ__eFZU4vf73o-UD1A_gxD6lGq0XBse7oqcWx2MZTCAO6O05vAoIFgjzXJtp_ewl-OvTKo11SEwnmZ3M7iID4gwKPhiLfANeAl7Xhh7mdVO5LX3MCoZqV46KehSVyg-PlAqvpWeARAT0l6Y0VLm_5uYLRgK_LWXvfT4w_WOpoUGHWfIGTqKU4esJfPRd65v4E7Zt3xCkxx-CIszt6i0le522NvadDE2qADAhywM6fTtKx8W8DNxIovitK8zE9Om3nYVr-Ztbp7cQJQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
ترامپ: می‌گویند من به اندازه کافی سخت‌گیر نبودم؛ من بزرگ‌ترین پلشان را ظرف ۳ دقیقه نابود کردم فقط به‌خاطر اینکه دیر در یک جلسه حاضر شدند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/129428" target="_blank">📅 21:05 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129427">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/prU5Z3BoztWj7lxtIgDzUCWYUYq_C1rqU-PMwpXg1mRORi-ZyhDynoiWQh0tCMNy_ZrmysEE6tytcLe3_Ks0DLgUv05rnA9yTux_xN12NKxDq8QQVsCotqeR4n3TGnR0AYXO2oJjVYE5QCGTkGwiYq3m4Pl2GXKqPUD3y5I5HgE6gGzR5zQCLg4Fr7g2quXBXYIuJYtTXC6gMy6Ii40wQDHGdnzkSjTl9TQenJMMBp0BdRV1Y0mSw6d9ZZmgS5DRhXIA7er8qYaMnHFJ3O0DEiPk6Kpu3I2E3e6YuypF-Fj2xwVGCwZlYzvNpxYCH8m2Dkmae-G4HkxwoxOyI4UeUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دونالد ترامپ: سازمان مهاجرت و گمرک (ICE) توسط رسانه‌های جعلی در حدی بی‌سابقه مورد حمله قرار گرفته است. مأموران آن میهن‌پرستان بزرگی هستند که سخت کار می‌کنند و در محیطی بسیار خصمانه وظیفه‌شان را انجام می‌دهند. بخش زیادی از این دشمنی را دموکرات‌ها و رسانه‌های جعلی ایجاد کرده‌اند.
🔴
مدتی است به این فکر می‌کنم که نام ICE را به NICE تغییر دهیم. این کار خبرنگاران و روزنامه‌نگاران فاسد و غیرمیهن‌پرست را کاملاً گیج خواهد کرد!
🔴
تصور کنید مجبور شوند بگویند: "امروز از یک مرکز NICE بازدید کردیم" یا "مأموران NICE یک قاچاقچی خشن مواد مخدر را اخراج کردند." آن‌ها نمی‌توانند تحملش کنند و کاملاً دیوانه می‌شوند!
🔴
فقط کافی است یک حرف N (مخفف National) به ICE (اداره مهاجرت و گمرک) اضافه شود. به نظر من اسم معتبرتری است.
🔴
همه این ایده را دوست دارند، اما تام هومن به من گفته که خود مأموران به اندازه بقیه مردم از آن خوششان نمی‌آید.
🔴
چه کسی موافق است که یک N اضافه کنیم و ICE را به NICE تبدیل کنیم؟
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.3K · <a href="https://t.me/alonews/129427" target="_blank">📅 20:50 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129426">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 58.3K · <a href="https://t.me/alonews/129426" target="_blank">📅 20:47 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129425">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hin5opBQExFIrkYBHWfHxRD7Q5EuT3pSjdv4rYey4ZrzZvfsVSwVQw5WldTdLqWC7eTy1YrYYVmYrlk58CqbYKWukivir79KOO8-1MJBOQQcR-6L8D22cub8Q-3JH6xWgyMMwKcDV0ExDV-ZhzNFbrLj839ZV8QNe857QSS8Y59U4KPuWOGdGk-DEjJb2Lmpb27VmYHj8ZnqAWg_oo20NZG4mu2Da4bhngzTfATh6gFNufxv1KgtkhQE-CS6FSnISk15HA8BC5k0A0PyTys8eV7toCZylyrOHxfwUgYKgGV9RJUaVg1zNCZA261e_W5077JBKgHP5vALFA-ibKyRZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع…</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129425" target="_blank">📅 20:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129424">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">👈
ساعاتی پیش، نبویان نماینده‌ی تندرو‌ مجلس، با حضور در صداوسیما مشغول قرائت بخشی از نامه‌های «به کلی سری» مربوط به آیت الله خامنه شد.
🔴
نبویان با انتخاب بخش‌هایی از نامه و حذف عامدانه‌ی بخش‌های دیگر که شامل چندین نامه و مکاتبه بود، نقل‌قول‌هایی ناقص و تقطیع شده منسوب به آیت الله خامنه ای را در تلویزیون منعکس کرد.
🔴
اگرچه این برنامه‌ی سازماندهی شده در صدا و سیما یک‌باره از آنتن زنده خارج و «قطع» شد اما رسانه‌های پرتعداد منسوب به این جریان، با ضریب دادن به این اظهارات تقطیع‌شده، به تحریکات علیه تیم مذاکره‌کننده که هم‌اینک عازم ژنو شده‌اند، دامن زدند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.2K · <a href="https://t.me/alonews/129424" target="_blank">📅 20:44 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129423">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">👈
کانال ۱۵ اسراییل: اسرائیل تلاش کرد مسیر لبنان را از مسیر ایران جدا کند اما شکست خورد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129423" target="_blank">📅 20:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129422">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">👈
الحدث به نقل از یک منبع آگاه: نخست‌وزیر پاکستان و مارشال عاصم منیر فردا در مذاکرات سوئیس شرکت خواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129422" target="_blank">📅 20:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129421">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">👈
یدیعوت آحارانوت به نقل از منابع نظامی:
ارتش اسرائیل دستورالعمل آتش بس دریافت کرده است و نیروهایش از منطقه علی الطاهر عقب نشینی نخواهند کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.2K · <a href="https://t.me/alonews/129421" target="_blank">📅 20:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129420">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">👈
ترکیب هیئت اعزامی ایران به سوئیس به ریاست قالیباف
🔴
محمدباقر قالیباف، رئیس مجلس شورای اسلامی و رئیس هیئت مذاکره کننده ایران
🔴
سید عباس عراقچی، وزیر خارجه
🔴
علی باقری کنی، معاون بین‌الملل دبیرخانه شورای‌عالی امنیت ملی
🔴
عبدالناصر همتی، رئیس کل بانک مرکزی
🔴
حمید بورد، معاون وزیر نفت و رئیس شرکت ملی نفت ایران
🔴
کاظم غریب‌آبادی، معاون حقوقی و بین‌الملل وزیر خارجه
🔴
اسماعیل بقائی، سخنگوی وزارت خارجه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129420" target="_blank">📅 20:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129417">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bkl6de0c21ht7U7jTfLkf4cDFOf-14M_vRXfDnPF8ut6pSOFKAjSTWBM8nab-4nP4czHquLkYWYS-Mlj2K_rRDdYGpwIXARrvuxP8EYek_vCIEWIsmxBCUPsLXmnx47Ou0niL_P7bQoy-swpZSPC33yLQXyvZhPk0cd7TF1pstlucPxndTNjA8G1bASTNxG2L2sZU7lgUthut-kzuhPyM1aAwN_w5IdpkUXihQUSkTGI4MBlYmjs_F8hkTKgGeIjX_Ac6z7Oq7FXp7queWtvi9CpRvBPNT-fHmhFCiTZXCVMkuRWhpW8pxrW6ZdiKKhWKrAWGrKxxAS0FyHHUvGROA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vjfh5DkEfcOE6E_PNNXbGhoet5qOIpjxo20J4Wa128WZ8h5yVVT3kTDknddOmScxtDuHIuLohSZEGSfWotaroMLjsERhDymgU8hlRNuAO6NSo-Py1HMrU8Zt0jGZ1L2t7nxpJIo64LgFlwGq_ThRFEEXZhIgAjR-CWDCAfMmtPISHgt5NuC5Vbz212S4DqnxJwetxDiTGWrXOjeaw7ZtJD78gKw-IXGaoXRpVHF1OgkBaoIXojTzsPRBn2Z0iIFmsafZK9p0-EnS0B2M9maLaWPmACUCd_c__-wqI_D80z6gtyd3m7KJ7OOkw8mSe3ybx7zKsj7EUcKjM87kMTPq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ni_HOY7gGBJnBd9aKZXg-f9IT5DrDAf6bRenm-BqKj9EBCWvLxzqc9cHWWx9IfnTfE5YtRhwEZJ25IYtORQUQfD0C2Mvc1c4H45S3zXiCyjlc5B9RxHhHEXyH_7SBTP-I_5P3m8nyJd_XX9ZS4njWwj6-C8yvUgo07DViC1m_p3z3KY8pd9qocvCEwI3DfUG2im3jD9GAPVfSuExf_IDT0iFxDdORAKk-9JzoRWc8SET1F3FjSA8gijmwKtVGGN875QXBrHO610nbjCaTiS9T1Uq1JYiK_Bbd6LN7BewlrvGm00QxkF85GcIQPeb22jgdadapVVKLlkQEs5NRkPMng.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👈
عجیب اما واقعی
‼️
🔴
فرود پراید در اراک روی پشت بام یک خانه!
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129417" target="_blank">📅 20:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129416">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/S9YtPTNY8wZNcEMMHlUdTDg0XnZUyAsHvGpPe3JrSjAehJyTkP0bjg0ImaDsC3jw9j_dcT1qk7cXSj6TlNds4gj67Z6Kv9bzZVt-zULkq7tSVcYQ_iUv3CLRJYD-v5suCPJxUKkcITy5oEBirGmVR13CU7g4IIewrBr03OkFmAHizTdQGLV9tP64UQwLJQe90rJVJeDbH7SwUNc67lwkYpMJ0L2MBvT--ryLuLfKnCln-yKd3Xv0KAChLbXYSrU03dnuxm32YLpORRH0zHpgrxWqTwDGwNUlRWcjpR0F4wrs8vugA26Y1nInGL3TICCxHqWk41iHo2SXsau9uj1JEw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
نوشته پشت موتور یک خانم: لطفا نزدیک نشید میترسم، تازه یاد گرفتم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129416" target="_blank">📅 20:18 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129415">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B9e-fkv5xkKLnm5rU6NDAhzNw4fgxqK6A_zxcNdg-5D3ogt_sAJaZmNLl9Rmm25zgf4saUHetbnzchH0R6x9S1W9DMCWg7jnqY8EiH8QdGsNFhRnT4QAuv71khowrQR7bTPxS_SAWGL74LLu8fO8Ew0CqqNDb6rszgHYnWyk_AoNgplYjgKh-4j3CV06NOKZl0s5jMX9DxMSXFnAXLvuo_eQqKAgAbl8TZ5TlKdXZkF2fxCV34mPaSPM9NqvHEIXEW4qNgSqqsw1NdMcZ0B4Ysm7s2e0QIr7ON-VFKrOzQ2guL5uteElJXYcXUzK7Qwvs4o7gyT9ckmuioSG0ymUyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
دیدار وزیر کشور پاکستان با مسعود پزشکیان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 51.2K · <a href="https://t.me/alonews/129415" target="_blank">📅 20:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129414">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">👈
بلومبرگ: عراق به میادین نفتی بزرگ دستور داده است که تولید خود را به بیش از ۳ میلیون بشکه در روز افزایش دهند، زیرا صادرات از طریق تنگه هرمز به تدریج پس از توافق آمریکا و ایران بهبود می‌یابد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129414" target="_blank">📅 20:10 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129413">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/92808565ea.mp4?token=cn440o0ZZKl2VqOZv0sSA36KXzoFL8EUszoALgMNcHAFPR1RNHJOgNGRLc_du66MzHcC7U7Ni2-gz-QUrUcQe5Jpkx7Of3xZBydpozHmrXti1Lh7xEtpB8qvELuyd0oXTlZHUHPzEMCsgSfMBAcxkrz1_tpFunfWy2dEUDc-KqW5z-SLTSkdH9kqrI-8DhyPIKS7XmRAdzmxxXZSeUqnVtMTpQQpjGfedMvomAF41SJF6LUezHy6ymNi3zzDJzlREng2NEJIT79G83cm0b0F5iPx1B3_aGPGgJL4cZ0zUnncIW9SEht-LLWFkCt1Fpn1QkedRcsDrJR5dzG9do4nNQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/92808565ea.mp4?token=cn440o0ZZKl2VqOZv0sSA36KXzoFL8EUszoALgMNcHAFPR1RNHJOgNGRLc_du66MzHcC7U7Ni2-gz-QUrUcQe5Jpkx7Of3xZBydpozHmrXti1Lh7xEtpB8qvELuyd0oXTlZHUHPzEMCsgSfMBAcxkrz1_tpFunfWy2dEUDc-KqW5z-SLTSkdH9kqrI-8DhyPIKS7XmRAdzmxxXZSeUqnVtMTpQQpjGfedMvomAF41SJF6LUezHy6ymNi3zzDJzlREng2NEJIT79G83cm0b0F5iPx1B3_aGPGgJL4cZ0zUnncIW9SEht-LLWFkCt1Fpn1QkedRcsDrJR5dzG9do4nNQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">👈
طالبان یه معلم زن رو به جرم آموزش  آنلاین به دختران در ملاعام شلاق زد!
🔴
طبق باور طالبان، دختران و زنان حق تحصیل ندارند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129413" target="_blank">📅 20:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129412">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">👈
مقام اسرائیلی: ارتش اسرائیل طی دو روز گذشته به 300 هدف حزب‌الله حمله کرد و 100 نفر از نیروهای این گروه را کشت
🔴
نتانیاهو به ارتش اسرائیل دستور داده است تا به هرگونه حمله از سوی حزب‌الله با قدرت و قاطعیت پاسخ دهد.
🔴
ارتش تا هر زمانی که ضرورت داشته باشد، در منطقه امنیتی جنوب لبنان باقی خواهد ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 52.2K · <a href="https://t.me/alonews/129412" target="_blank">📅 20:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129411">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">👈
وزیر کشور ایران: محسن نقوی، وزیر کشور پاکستان حامل پیامی به ایران بود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129411" target="_blank">📅 19:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129410">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OfXfjokzo-7Gl1HsvrVcylIV6MvQdfsPmUGNmlXMdOc7-qVk4ovwzSQtil0UX1YrAP1hb0Xshmrzwa6N_f2ufcMXHVjaLqY5gNqfJXGP3bEs4FfuMICQXxBKu_oTIU0uBKUotRoIN0j-7qKDGL7fK5rEKZhIgTQDoPiFnZdUBN2eIUv4uHLcavr6mrVYGkH5vvDGN6fuu5tri-LA9Kqo8oKUYxwsRSPKqB1yzrNpC-u8JFQIgWHelC_OU66MbAh-LaL4DsmxPCtfoOvTNZJl3mpwr65Sf1KxBn08weU7xGUzD-HwZBEgBrBmtlYEXXMr3N3UznZ8TB5hM5gWrazkxQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
مخبر: وقتی توافق روی کاغذ بماند، جریان انرژی خاورمیانه هم متوقف می‌ماند.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129410" target="_blank">📅 19:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129409">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cgSmY2a62QOKV86WeKqUVSN1GodKOc4AryZmEQvujOlHs7Fc7gQNZkKsK7hsu7WBJPMqW7Lbt3iRhc1z8lcY70ULqx5bYvzgMNnRSGpkWq7JIT8AMa_gt8i7EuYlxct7jL3cs5d-VkNI1_3wJFJ3nqHtH_dav_R4ZoVBYbu4R2iu3cPgVw-5gA3CRU0oj_00CiejubZG_h6_zgwozaDCo2YQoq9uNPqn3MAaVwC0dcVo_iZd_KEQNGevFIRi-E5Qmc66SWiDIge2Y7k1gPPktQGKphcHYhV1-W_0bcbEeHfsTL5W-t-ZamJ6AnXHGKVmLfi0ZKzeBZDxdcJNECBp7Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
خبرنگار الجزیره در تهران: تاکنون، خط اعتباری که به تهران اجازه دسترسی به دارایی‌های مسدود شده‌اش را می‌دهد، فعال نشده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129409" target="_blank">📅 19:33 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129408">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromالو توئیت | AloTweet</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ecd9f0207c.mp4?token=dqF-Ok3YjXYXd6nwZPTMe8i_ZokxqGoxmIXZyP_-Szeo-3RXFG6UogWvadJPJUIjcMSAHWdl41NXdLLqvtSb3HndmZ8fOa5mpxcYa7Xy3WpCQiZofuuT1ifgERSEMMqjEAcSG53FCzi9tTm0dkDL6pKN7OyuLufRBe5XVaxzgphaRflyyDCS9Trubal1Zhu8On_BxFvrMPwot6Eqr38JI73DBMPW_1KqPaQOfMfzEFUQEtCu0aCwCn16UH3XKt4QZWIVEdfQeDtAXP7BqjhjLdqvF-wDTJ3VUXwQNr6A35zWQ3lJ0fCmEPVgr7BQR_fN6tVIF-NI9V2FpfA9aBk1cA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرف دل ملت ایران
[
@AloTweet
]</div>
<div class="tg-footer">👁️ 55.3K · <a href="https://t.me/alonews/129408" target="_blank">📅 19:29 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129407">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">👈
محمد جواد ظریف: از مذاکرات استقبال میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129407" target="_blank">📅 19:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129406">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🔴
فوری / مقامات ارشد ارتش اسرائیل به کانال 12 اسرائیل اعلام کردند: عملیات نظامی در سراسر جنوب لبنان ادامه دارد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.6K · <a href="https://t.me/alonews/129406" target="_blank">📅 19:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129405">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">👈
گزارش ها از اختلال در اکثر همراه بانکها
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129405" target="_blank">📅 19:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129404">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">👈
سنتکام بسته شدن تنگه هرمز را تکذیب کرد و اعلام کرد این تنگه همچنان به روی تمام کشتی‌ها باز است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129404" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129403">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">👈
معاون ترامپ: احتمالا طی ۴۸ ساعت آینده به سوئیس خواهم رفت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129403" target="_blank">📅 19:03 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129402">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">👈
شبکه ۱۲ اسرائیل: تصمیم نتانیاهو و کاتس برای آتش‌بس در لبنان با هماهنگی ایالات متحده اتخاذ شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129402" target="_blank">📅 18:57 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129401">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">👈
حمله اسرائیل به غرب خان یونس در غزه
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129401" target="_blank">📅 18:56 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129400">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/C4wZ35UjsuqOjVYobGzT-G8PhjBV2D_I2tHR7m7SNPajuwz-WDNGsCPA1d3wFse6NyXxsfhKy-oW08WWtfAyhxfqkB6Kasntat1M8VkwiMEsSaTdFGf59iJbMA2IIVqJRKLFbTAI7bbBZGdWwzlvm8aPCOw9JrhDYLUoop9r59WglU-lXHQCRHbSgA2XcDeC6KSX-GcRfpcT25zd8RRn_ssI7PX3nrU0pYBtYX3zLScUMcUIzS1hVnPb6EZmjBE-Ema5jvbATC2czIvbtFHG1cDIs9FSv4G2ZIo3MIovIRXY1aVd9Hg6L92j5i71EBnpAIMVoMhiyhVKb6Td_vKCcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ایران‌خودرو: دوباره گران می‌کنیم!
‌
🔴
شرکت ایران‌خودرو اعلام کرد که اصلاحیهٔ قیمت محصولات شرکت که در ۲۸ خرداد منتشر شد تنها تا پایان عرضه دورهٔ سیزدهم اولویت بندی محصولات این شرکت معتبر است.
🔴
‌لذا پس از پایان این دورهٔ ثبت‌نام، قیمت‌های اعلام شده در ۲۷ خرداد ملاک قرار میگیرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 62.5K · <a href="https://t.me/alonews/129400" target="_blank">📅 18:42 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129399">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Itdgths6BSy1bTXzyims7f7FLsOkNBtobIlBDzO3TBxg_XD6xQd0GDo0GGLGSmsjurKtz24iqT6_OifLVA7qtMSZVmb847jDNoI4jraFLbxx2puXobuI0ufzzChnYh1wYekdgZVtEHIJCVd_D__dJxgzobg2kLZzdvG2PVN_hrPqNgmnfVclwcc99Aa7Dq9T9it2oZDIrxkQspeXAVXeZ2nrP6VHZ4ljAvp2Q3U-NrJhNJXgAoUvyz-JFvSATKZ_OWQnV4TPDELVt51x303VLbjU-iecqXEWksW4ygEhzsu1_fLSxkwLfotHc5KNKlvIvM-ovP_t31iaGtiKVDK9Vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هواپیمای هیئت مذاکره کننده ایرانی در راه زوریخ
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129399" target="_blank">📅 18:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129398">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">👈
سی‌ان‌ان: ونس امروز به سوئیس می‌رود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.3K · <a href="https://t.me/alonews/129398" target="_blank">📅 18:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129397">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">👈
جی‌دی ونس درباره ایران: من بسیار مطمئنم که می‌توانیم این آتش‌بس را حفظ کنیم.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129397" target="_blank">📅 18:32 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129396">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🔴
فوری / کانال ۱۲ عبری : نتانیاهو دستور توقف حملهِ‌ها به لُبنان رو صادر کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129396" target="_blank">📅 18:22 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129395">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">👈
ارتش اسرائیل (IDF) انجام دهها حمله هوایی در جنوب لبنان را در طول شب و صبح امروز تایید کرد، اما هرگونه اظهارنظر درباره تهاجم به تپه «علی الطاهر» در نزدیکی «نبطیه» را به طور کامل رد کرده و به جای آن، حملات را به «نقض آتش‌بس» توسط حزب‌الله نسبت می‌دهد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129395" target="_blank">📅 18:21 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129394">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Hq4UJf7ToEJ79xj7PA0_xwafpQlK3k1WrMH4HZQ_EZxyc0s2UTtIPQiyAaYrp2X5byAM1PISy5quG0_QiCyLGsNHBO7FTkWpW9HG7OQu9GdDSaJ94eg-Ow6Ce9RbtppUQh8t238_VxlStw8UcFrZHf4i2Mn196-khzsa2aVGpdvQFQ01tBKcm0lEMqbUJA7Efra0Xg2d9l3t33V4YaJU-pbRBiE8_e3z5CzyLblKMSu8xiW1TdC5kGu5dCd0MrJa2OVJzhTBV48xEdmSYuOOZgExxZKn24vSE9Z-9z1V3oDwhKonnRNEx4RPqMYJlYgkv6NCi3x4c_Mi0nnKoxV2mw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
بدون شرح
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129394" target="_blank">📅 18:02 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129393">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TrwWnmk-hWyVaEDryKmx_QniIoZY_ch5EyAXOQfB5fNaY53EX8D56rEN1-qoXBjSMJu-IBsXT3aItRITBlrJYjZkF5iudri_Droa8SVzxj_LHAt6h0b1aiilRvAaTEbopyUc1ELsPPz7-SXrUwCvDpmXLD2MWgDqH7n7jFlQhdHTd8FozwXqKyuLzAMXsMaqaWrbkz7tBVndEQHoxZ8DSOsIa_Eegtdp5e5kwA6RMLAhuyUb5Exki1R38G6PIXChHZJhYIl6ZCnTgB8jAfpGGySQhuHDxt844ZUGwTYsTL9YIFu0BfcKSRONs2xW2ABijOBm64w1TCFTHx5oBi3ITA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ملونی به ترامپ پاسخ داد: رئیس‌جمهور ترامپ، این حملات مداوم و بی‌دلیل بی‌معنی است. در مورد محبوبیتم، دوستی با شما قطعاً کمکی نکرده است و همچنین به رابطه من با شما بستگی ندارد.
🔴
محبوبیتم به توانایی من در دفاع از منافع ملی ایتالیا بستگی دارد، و این دقیقاً همان کاری است که همیشه انجام داده‌ام. این همچنین کاری است که در مورد پایگاه‌های نظامی آمریکا در ایتالیا انجام دادم. استفاده از آن‌ها توسط توافقاتی که همیشه به آن‌ها احترام گذاشته‌ایم، تنظیم می‌شود و تا زمانی که من نخست‌وزیر هستم، نمی‌توان آن‌ها را نقض کرد.
🔴
ایتالیا همچنان یک کشور مستقل است. به هر حال، محبوبیتم به شما مربوط نیست. پیشنهاد می‌کنم روی محبوبیت خودتان تمرکز کنید.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129393" target="_blank">📅 18:00 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129392">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fd8Og7alVTDWzzMUMaUvvSklt9DsqKEj1CudSSZ_tJubLAFCwMrB2gpZJkC-leOisjtWwsPT9WEwIXl3OLEOh4RV-8t3bgQiwZWa3maN4dXi21aQ9YP9e5AiyFjFsdbeqGAzsVYjXKR894V2jzIP4DTsnIeyoCXnOJywyL59RF-alYdHJkslVrkS_OuXSSVq0nvPaKx7TW6udLKb1JbRQVGbQl1yFlgWYl2_dRD-ZgRG7Joq9JJ7cpbZY5HxpkLRy07zYMSa7Ho3fE6GvgPwIib-FxHpVooBBEuWk0gf7KxdqTof37LkHybaQKAXZxouqbVPLceMUIoRoDPyF452_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
هم اکنون تردد بدون مشکل کشتی آمریکایی در تنگه هرمز
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129392" target="_blank">📅 17:46 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129391">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">👈
فکت:
هروقت عراقچی تنها رفته مذاکره، جنگ شده
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129391" target="_blank">📅 17:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129390">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">👈
العربیه: قالیباف به ژنو نمی رود؛ عراقچی ریاست هیئت مذاکره‌کننده ایران با آمریکا را بر عهده خواهد داشت
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129390" target="_blank">📅 17:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129389">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">👈
نیروی دریایی سپاه: شناورها به تنگۀ هرمز نزدیک نشوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129389" target="_blank">📅 17:34 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129388">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">👈
سخنگوی تیم مذاکره‌کننده: آغاز مذاکرات توافق نهایی، مشروط به اجرای بندهای پنج‌گانه تفاهم‌نامه است
🔴
طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129388" target="_blank">📅 17:26 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129387">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">👈
سخنگوی تیم مذاکره‌کننده: طبق بند ۱۳ یادداشت تفاهم، آغاز مذاکرات برای توافق نهایی
مشروط به شروع و تداوم اجرای تعهدات طرف مقابل بر اساس بندهای ۱، ۴، ۵، ۱۰ و ۱۱ است.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129387" target="_blank">📅 17:15 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129386">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
فوری / ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 60.4K · <a href="https://t.me/alonews/129386" target="_blank">📅 17:13 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129385">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🔴
فوری / ایسنا: هیات مذاکره کننده ایران تا دقایقی دیگر عازم سوئیس می‌شوند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129385" target="_blank">📅 17:11 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129384">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔴
فوری / الحدث: عراقچی امشب همراه وزیر کشور پاکستان به سوئیس سفر می‌کند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/129384" target="_blank">📅 17:04 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129383">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🔴
فوری / فایننشال‌تایمز: پایان عملیات نظامی اسرائیل در لبنان بعید است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.4K · <a href="https://t.me/alonews/129383" target="_blank">📅 17:01 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129382">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">👈
فاکس نیوز به نقل از جی دی ونس معاون رئیس جمهور آمریکا: مذاکرات با ایران فردا امکان‌پذیر است و وایومینگ و کوشنر برای انجام این مذاکرات آنجا هستند.
🔴
اوضاع در مذاکرات ایران خوب پیش می‌رود و انتظار دارم به سوئیس بروم.
🔴
به توانایی خود برای حفظ آتش بس اطمینان داریم.
🔴
به مذاکره با ایران فرصتی خواهیم داد
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129382" target="_blank">📅 16:53 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129381">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">👈
الاناست که عاصم منیر بیاد تهران
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129381" target="_blank">📅 16:52 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129379">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">👈
قرارگاه خاتم: تنگه رو بستیم
✅
@AloNews خبر جنگ</div>
<div class="tg-footer">👁️ 61.5K · <a href="https://t.me/alonews/129379" target="_blank">📅 16:45 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129378">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">👈
قرارگاه خاتم: تنگه رو بستیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 59.4K · <a href="https://t.me/alonews/129378" target="_blank">📅 16:41 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129377">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pVUymKUWVFcbq9Wuh48DQU5DQRTQ6zlV_vNB01nPU1CHzLVOm6Izn9jpeKxiaYfnosw_b_wt-JMLQZ1Vvo3HX9QAFh5b_LhszGDL49KyGPtaHeD3RaS0kBiDOrK7s5TqvSl7ufJYCI8qXN6Pe3F6rWB0NvWDBBkOKP0uZTqf-bq7NyHgR9Mk7Kgj5fxLsN7vfTbSe9maIlTBEuEZ5JkapcWFnLd1PikQTzAVUkzwiq_hFoCm-nBpyCnJj1IJPQDiPVJYCj5XJ39owSu0bb6BJjARsphNHAMCXzVBTskEojlfwjR3bGOQPsrKLTfQv8xr1rEXC80OugS_kXthQ_3MOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ظریف: از مذاکرات استقبال میکنیم
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 58.4K · <a href="https://t.me/alonews/129377" target="_blank">📅 16:40 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129376">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">👈
سوئیس اعلام کرده است که به ارائه «محیطی محرمانه و قابل اعتماد» در بورگن‌اشتاک برای بحث‌ها درباره اجرای تفاهم‌نامه آمریکا و ایران ادامه می‌دهد و اضافه کرده است که به دلیل محرمانه بودن، هیچ جزئیاتی درباره شرکت‌کنندگان یا محتوای مذاکرات منتشر نخواهد شد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 57.4K · <a href="https://t.me/alonews/129376" target="_blank">📅 16:35 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129375">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">👈
سیدمحسن نقوی، وزیر کشور پاکستان که امروز وارد تهران شده، با عراقچی دیدار کرد.
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129375" target="_blank">📅 16:30 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129374">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">👈
خبرگزاری ایرنا : کشتی‌هایی که می‌خوان از تنگه هرمز رد بشن باید با سپاه هماهنگ کنند
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.4K · <a href="https://t.me/alonews/129374" target="_blank">📅 16:25 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129373">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">👈
ترامپ: نخست‌وزیر ایتالیا در جنگ با ایران همراه ما نبود؛ اکنون می‌خواهد با من عکس بگیرد تا محبوبیتش بالا برود
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 56.3K · <a href="https://t.me/alonews/129373" target="_blank">📅 16:20 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129372">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">👈
رسانه‌های سوئیسی: هیئت‌های مقدماتی ایران، ایالات متحده، پاکستان و قطر از دیروز در اقامتگاه «برگنشتوک» در حال فعالیت برای آماده‌سازی مذاکرات هستند و تاکنون هیچ نشانه‌ای از حضور رؤسای هیئت‌های تهران و واشنگتن دیده نشده است
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 55.4K · <a href="https://t.me/alonews/129372" target="_blank">📅 16:16 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129371">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dScbv7WDaVqM98mTQ61sJAQ6z1jluo-830TYBwcJ6ByHw-Q3A8PV7v3fdzzFYUhvcAFi-KXH8wiVRxOuO8aw8wMzh_qfOaVtQUAH9dHD001JW9yKGgVTKnWHhSEH5v4TSetT27vmMamFkomF2HC39wEg1c3QSjvuZPeEDEsxH6PQPFaTY8PDBvBqlh1ILuubjiHOj5IHrvDNMaMMyDRZH2mSUGkXHv-J0WBLF0yvcXhYQn3J89ylRxqBWR6vCuMuzvrplrQplgXgT8xnpA0uHvFvv3KLvCWuBl_VRgmDwjeQkn2Vfd1zYb86MMNlOcoaxb7Hi1sVgYUl0885S-bLWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👈
ترامپ: «ترامپ برگ‌های برنده را در سرنوشت انتخاباتی متزلزل نتانیاهو در اختیار دارد.»
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 54.3K · <a href="https://t.me/alonews/129371" target="_blank">📅 16:14 · 30 Khordad 1405</a></div>
</div>

<div class="tg-post" id="msg-129370">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">👈
هم اکنون حملات سنگین به لبنان
✅
@AloNews
خبر جنگ</div>
<div class="tg-footer">👁️ 53.3K · <a href="https://t.me/alonews/129370" target="_blank">📅 16:09 · 30 Khordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
