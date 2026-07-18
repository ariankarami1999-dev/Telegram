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
<img src="https://cdn4.telesco.pe/file/QxZbwXXNeCBFvbuyWenAKyN9JyRxVk26L8PFhBRc-8LpVMUA57E9mORtsWLNoEvF9MRMVKH827V63AGFDexNKslURKAKGvLJoWYErF1NOIiq7-dKzPR6nwFbwzIVJMe1otcqwDPQr7gbUpml3R-g6wi2n4hkjvY1cO6lmdexow2hCeZI_de641Fq-hGck-5wByAA_MHenfzi_XqVyOHHIPTuMOxFZELLAIYu5Fn4kdus7MQ5xLKDWsmkfJFcVd3eEiuuvFi4HX8K0uSJVSuY1Us3NDqfjciUUpzsyG3b6KXIWN4yOu7Lley3PW_M2vPuxAujPIk2kANE53N-Jv_Q_Q.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 267K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-27 15:41:26</div>
<hr>

<div class="tg-post" id="msg-83935">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/58ecdbf49a.mp4?token=EbmTEriNJoNHxSYcKwVkj5cUYkRXianLTuvvB2kR_7FytqXuahh6XSRbx5TFFUaq_ChVksZgOmc9BtjaH8Wx2S-8o9F6NkCq4w6CSIJ0Vyj7WRmOvuvqkm1mxcE4orwJMEzbB_4bbtmMHrCKHdEeMWrNm7JemBfzMFp63f-cj811FTRXQZyjHL7SAA4po5h13OM_eEQlyx25EnQ74sjXsBUKfoEDUsHxw2VVjn1PxFVtUrAVeL-5kcJDssXF2d9TECxPMi-L-kRSqAH5CCAsO0h3nkNx4HaAzBbKFBECMjqo-qOHnrH_Bil9-OfXA2Skvj4_fj4-P7-bZZ11owca9x6tMM4HNHCikB2d8tmfuJX6GD2EfCz8wKptqytW-otYMiNmb0QyDahAYLTtb4SFAQfi7Ru_d2LEuAyBhvVyJ1E42bM3HAJdVvaAYycQONAs1cXwmfRCB2AokVwhz_cBClBlV6gMRSGijd4edR5dzYXmhS4reADHXmCPS93UYNUc9ic0iPYPIItgu0pUmNhXkIm4qy1mpmNeiuzYyQw4jQiVfzSx2utEhHOxWy4eAHzmiDQXeMydK3-1OdSDMPTp6CBuddQMH1UxkrKXjl-85rxFfrojSAmR1FDMmh2Pq2pgqs176cJOTouQZdQAn3A1dJHi3tuJo2T_V_CvEzO7XhM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">القاعدة الامريكية في الاردن تحترق</div>
<div class="tg-footer">👁️ 331 · <a href="https://t.me/naya_foriraq/83935" target="_blank">📅 15:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83934">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fad9043e8d.mp4?token=IE79oq-jFUdn5RgmzoqvYdcO451-QQyAuBSYLGj9ONMccUJE2NUrKn8mNFPeZ8s64jpljEMagJEXdqRCxC9aG-_G3es8tbN8csvujH9xFxY-_UGMAIgzNHJvSCMP3-epTgltrH37S_IBZ05WMG7avv3a8GhnJ020k7Qj3Y-jjnna6XUmDl3d_YopQHzevMF-AxdeaAbAgfJtLG5LQpWFwyw0aUqEVQc0jH4R1Kuh1YSJe7R7aBBIVxTqdgn1hJi4BWr9uo9YQur9R97d9Yy1V1POvHoqAARMehH26SgBLEW1hxBhvKwDFoJHr6J2M9lDfBYB53jBrvNdwWY5SOKGMQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هكذا تبدو المشاهد صباحا من الكويت حيث صوت الغارات والقصف الإيراني لا يتوقف ..</div>
<div class="tg-footer">👁️ 3.15K · <a href="https://t.me/naya_foriraq/83934" target="_blank">📅 15:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83933">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">دوي انفجارات بمنطقة الميناء بالكويت</div>
<div class="tg-footer">👁️ 4.43K · <a href="https://t.me/naya_foriraq/83933" target="_blank">📅 15:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83932">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🏴‍☠️
انفجارات عنيفة تهز مدينة أوديسا الاوكرانية ، أوديسا هي قدس روسيا وتتواجد بها اكبر قاعدة لحلف الناتو ..</div>
<div class="tg-footer">👁️ 5.05K · <a href="https://t.me/naya_foriraq/83932" target="_blank">📅 15:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83931">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/83931" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83930">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">انفجارات تهز قاعدة الجفير في البحرين مقر الأسطول الخامس الأمريكي</div>
<div class="tg-footer">👁️ 5.69K · <a href="https://t.me/naya_foriraq/83930" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83929">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 6.3K · <a href="https://t.me/naya_foriraq/83929" target="_blank">📅 15:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83928">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ebbb2b7015.mp4?token=lEAiq4rq_GoPf1ghg1cVCNwj3xvy7lp7n7aflbFUBL7K3arwImpdQG9DeurHk9Bi0p2L6R6u7jYbLQvyR2bH9qbl5kbvBbtyH85Z1GDcLNTweOWlrp4TZjFd5RJ0l1jivQQ0Vig3_SWWl4LOIwn3Mm9UDPX05GpyLuE3exKyFzyIYKGDuv1DlbIwOi55Jb2go-Aa4SonOUsaxm_8U0iF3-GNV6UbuDb6MN85HiNd9SA_MteMnup2H8qWk7fF1XO537GEA-u2LavK_xWk2tsqMn9scHED_u3RnnQbs4RtXC_Gzzj5W2E_SEEQTMgFJqXaXOCQJdKTBIlG_HAMnhMsrg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
🇦🇪
وزير الدفاع الكويتي يزور جرحى مستشفيات الكويت التي تعج بالمصابين العسكريين الذين يعملون داخل القواعد الأمريكي ، وزير الدفاع الكويتي يؤكد ان لو لا جنود منظومات الباترويت هم غير موجودين بالكويت</div>
<div class="tg-footer">👁️ 7.89K · <a href="https://t.me/naya_foriraq/83928" target="_blank">📅 15:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83927">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a628a424fb.mp4?token=bXl2vmbWxgRVSoijZU1HNkUyPPQdO4hFC02yk36J_CSVi7EvVoTBmKmsXcdnnAsH548J26FA8Zmk9_cVrYMUq8fysNd_GOFGV8-4oFjaY6Zbu4BIePOQ_6ZnJchsFdPY_R8yDXtX3CO5gQpOtIIr_S93TRXd9XCHlK5Cl_S2nphui1jQ2Bmlj2HYiF4cCtiC-LBFi981HGVoZhtpTtJGCeTBjM5xjeKwyotLlBIEJE_NklfqG5RFkIwuZWhpQr7Im6nmTrPf5ChHtkYL-kD63o_vq9hs2lKKVri7V1KuUrI3iNzbKdyrXYKZtKBSa0MZ1b84H4TQXdH2Qgrr6nIYtQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استهداف عجلة واوكار للتنظيم الارهابي</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83927" target="_blank">📅 14:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83926">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cxBATl-bYcXZ7vSoLCERc0PRQdfzgQ8wlSq2f4TxEkI7C2lSzJ5xS57fmVir1T9Uo2PwMVV3mUWVF0HvUrtw1Q0QUaDE0rD9xNJWlMzfmNx4p7PvhCEa7uc2H-rB5tNHl7zrL_bNk4_X7jwHd0Pm3BvuvnLb-24OhXgIAh_YXEbrcaR3tY2v9FZdG3Yv_LkMqSODDR-S5fVkzBvUV16J9_jfLEbXZIxBj580G5jiFt8AYXEUUbMgheee1FUmKPged7xVmOeRl8WuJB5v_kCLC0vItn48cncdSHfP6_stOMGoi15BracjGOQHi8iTJoCAi6Al0rweOX2ygHEwsPgFwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اصابة مباشرة للقاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/83926" target="_blank">📅 14:53 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83925">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83925" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83924">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/008b089ae2.mp4?token=PoUfroZ0hh8If36k2UmN32e-hxokndTAHQg5ITxpiAXH26vKq2pVoiFSnFoTER9k7srY1d7oc_ZWVqzU740w3RNodBnYwYxEZCh5V4Ij7cck4oBYeE4VntyPhkRLOuo-J6O_zJoaBXWrA2X9AqDpwAeT05OGHIsY7SlxgORw0H54xw1QVfAkMP6jP0JB3HgbHm9BidfsoqiDeIfghmJap961UWgCgORqlavH7HLtJRC-NFHlcHr0DK_ziB1YZwybaku0D-NaVcr7t3JQKw9_SxAr42SWL1tFDa_hoqQIJqR8Z6rHjRHEim0lhq7gukTD2WNQ6FIsIbN-ko9nany69w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعمدة الدخان تتصاعد من القاعدة الامريكية في الاردن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/83924" target="_blank">📅 14:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83923">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">موجة صاروخية إيرانية باتجاه القواعد الأميركية باتجاه غرب اسيا الان</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/83923" target="_blank">📅 14:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83922">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/83922" target="_blank">📅 14:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83921">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5b2110ca7e.mp4?token=p8uAADQYtTzUd56rQaKWzbzqfy51HNUy9W0Pxj_Mo8RsBpwDIGiMNyQOgiSDRLE60yoLbeC7MrPB3dn_49JCRQQFd1n-_duGwM8dn1Q4tyck9-E8nGZ0zr0OArx9Z4E9QcUYWlw8YnmPdzQwPM9Ln6Zp-tysnlCyU6Q3mSy5SAV-1BS8-JniKaFtN-EGvVXMOwFDUiSZusp34B1a19vf2A4hYZ8NcRC2hQ9GOCwxXsXbf-i_fCKRLTJSxj84AwBMgA-9IaPvyG-t4q3bQbdyebHWgTGmwhRyS79jYWIO1z0e5eF-asyAd8lNDPGqsNPwTTuwz_AGmEs2i45IkwJ8_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماء الاردن تتزين بصواريخ الجمهورية الاسلامية</div>
<div class="tg-footer">👁️ 10.4K · <a href="https://t.me/naya_foriraq/83921" target="_blank">📅 14:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83920">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">اصابة مباشرة لقاعدة أمريكية في الأردن وارتفاع أعمدة الدخان</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/83920" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83919">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.76K · <a href="https://t.me/naya_foriraq/83919" target="_blank">📅 14:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83918">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUuRsAEUhUcFaOlXt8a1kw_0Q91DeM0WbDrv4KKqE1VjH17QGF3x8ezYgLF_hSSkG9mMLrCFJPt3JbQLhiC4jdJaJikmUY70FgK_BxnWB47zSchCcGhewCd0yZ_wTV6kiWSfYrvHBMK1bhSuXcZAuVae1gKktrfujO4SefrwkmtLbBL3PdEXK_5nLuPGc0gK-6YuT8t9Y-sJ5othqf1wbL8hSsGu2aBOEbt9hm1tAZRoyC4cf8RGdi2ObhETEzsr2HrQg2qJypk6XvzGhhXJ4BQM920SCBiwIVCzfIK917a5cYiopWtFUGm3706oj_mEhezr0Bire-kqhFdNDHandw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83918" target="_blank">📅 14:36 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83917">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇶
الطائرات العراقية تشن غارات جوية على اوكار تنظيم داعش في قضاء راوة ضمن محافظة الانبار غربي العراق</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/83917" target="_blank">📅 14:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83915">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">الكويت: تعرضنا لهجمات إيرانية اليوم بلا توقف</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83915" target="_blank">📅 14:31 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83914">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">ايران تطلق دفعات صاروخية جديدة باتجاه القواعد الامريكية في المنطقة</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/83914" target="_blank">📅 14:30 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83913">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">مشاهد من مدينة الزرقاء الاردنية قبل قليل خلال الهجوم الايراني الصاروخي والمسير</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/83913" target="_blank">📅 14:29 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83912">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SNIOUlrpffwDaWuOa6PnzLZneqgoKt1P6rTZTaK3zjeO50dp0hvXQE1sD80pIt9kfd1V6oIQ2xPzgUL4kuo0LElnSJFHr1xwq8wxAAWXUlyGKzzA7d3V7dxfCC_OPIN_4qsVX1TAIV2iLTPLSEt9V8VH8H4url6ry9soLqFFbXPvR8Zu_WIwbNWfZ38YpqDq2pnO4zdku54JJ5avN9QZL5NQx-A-OW09k7otjXXyzfw7LTqFwUn6pOsSZ-DxJbqPuNc_OMF0wAqpNgALv17jhFXAqbTAjAY2Ciu52V5h99neIwW1GnVbU7QxRMF-D9qRJfbDPmi5HhPa2S9dt3JbiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
النائب سعود الساعدي يوجه سؤالاً نيابياً إلى وزير الكهرباء العراقي:
ما جدوى توقيع اتفاقية جديدة مع شركة جنرال إلكتريك (GE)، في وقت ما تزال فيه نتائج الاتفاقيات السابقة مع الشركة وغيرها من شركات الطاقة محل تساؤل، ما مصير العقود السابقة وما أسباب تكرار التعاقد مع الشركة؟!</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/83912" target="_blank">📅 14:21 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83911">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f50fe64417.mp4?token=PXjNv0TW3oq8Bkyy_nOD8KVB9hr-CRJDEvlzrLzzCK3YRUJnnzdefMQI_SU0Kzp1qaWqFe_srRPscGFP-zLutcBUEx7z2ZCIfYAuU79WK1UdBv9DDZj6mFKyzHe6LRTyGmFkIU6yJKvT4JKqoykpKAwDwdl1DVqzMrBxUpF9SUqgSJCvpJBVj4teQ8uwLL_gBfRsXkegYU7datk9Zn3MjXuC7QKnBB5btChpD8_rAxKqNhtQwOq0qEs0jnb-3c9pRaoSK6ojrM7LGN3VrCh9qVZIJRZAgkli8pZlY5l5dgN3muwF1xO1VzG976bLL5sMNc-fDHAkUa5ohf6VhxZKhXQu7xsXgTopsEK31O52LOmQpXPs1_ciUE8v6gWiLOZqmm-kSiAeVtccBJryKJN6CT6pqnrnouh4f50zW7jkLDLquEllFJfOlxNYTM9-sBSHe6VvaPyN1EXcdvwlGyxTDoIKiPatR7fx0BH3Ns4z55F1MYfk1E31K_9543Cgwd-w6CcwxT_6v_efR42tF4wI4ImIuXmegWNyuAfqdRBSSbrIh5LE_W3rkuPFfe944lnjbQWOB1MTcdaqXMEf20tAOT5nd-2jm3e_xQLzzo4HpJVdaPyVOBUQnyfFG_weZgAkTfDf3cypqn1dBNet-LHXzUDhCE6g_Y93z6dVWqFs884" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/83911" target="_blank">📅 14:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83910">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/96d41849e7.mp4?token=JwFBYJuleYmb0yyqqHPJJWoI-mjRSha2mGBzoljFQ9XR2PVw-C4P7v9AqsdfMbvuo0ACFTdqqOTmgTUFUVGv2akI37rVrV3F1bu22Rj1o9R8qTsHFYNWqh5hbCbrse2UPe9v5OUSMfq3ii8oEQWiH5HT3Ox2cQRewUfklbgslWpjW8UfU9u_hDo8j1rN5wR17mbHqBYf3Igr1Y4xW-VtIx3huLApktGZx7tHXx5h3ewkEMBUvB7WJpc4t81TtbKgPN_9bNw1pRomsWbdfsp7FjZoNRUNW-lYcR2ZlkY1Z-MgU5siT_JDSNPiuH27PwJFc5361GfMh26m1cJwLISYTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">سماع دوي انفجارات في قاعدة موفق السلطي في الاردن</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/83910" target="_blank">📅 14:12 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83909">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
حرس الثورة الاسلامية يبث مشاهد للحظة إطلاق صواريخ "خيبرشكن"، "ذوالفقار"، "فاتح 110"، "حاج قاسم"، والطائرات المسيرة "شاهد" في الموجات من 17 إلى 20 من عملية "نصر 2".</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/83909" target="_blank">📅 14:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83908">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">الجيش الاردني يزعم التصدي لعدد من المسيرات</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/83908" target="_blank">📅 13:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83907">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83907" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83906">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏البترول الكويتية: موقع نفطي حيوي تعرض لاعتداء إيراني صباح اليوم</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/83906" target="_blank">📅 13:35 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83905">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">هجوم بالمسيرات يستهدف القاعدة الامريكية</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83905" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83904">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83904" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83903">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">انباء اولية عن سماع دوي انفجارات في الكويت والاردن</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/naya_foriraq/83903" target="_blank">📅 13:27 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83902">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">دفعات صاروخية اخرى تنطلق من الجمهورية الاسلامية الايرانية</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83902" target="_blank">📅 13:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83901">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">🇵🇸
🇺🇸
🇮🇷
🔻
رويترز :
عاشت ⁧ الكويت⁩ واحدة من أسوأ لياليها من الهجمات الإيرانية الانتقامية منذ بدء الصراع في الشرق الأوسط، حيث تم استهداف محطة توليد كهرباء ثانية في غضون يومين وتعليق الرحلات الجوية</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83901" target="_blank">📅 13:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83900">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O5xiK16F4WQ9lkDleAl1oSiQM4hNqFPL5Am0tlngBlRpdFTU8BMgbmIeBNAQRpZbfOXzfGXbqBEx3tULH05c145FttX53I1dRkfkymkZmWsGTwxBnlqyU53y971DcAzxx6E6H-3ix7HNdq5cHl1kW71gzuzo2UP_mvD_hW0th9dgETHs7mdYLbYXK9WYJLAKOYKQEfOsTWrt4ASCyTxC0tzXHzvLIWsySSvtQB8yeR7Pf_26H9_iqhyi35w-32wUCx9HPqE4QXBeJVN-FDqHrNteehRXBwzPZPlAy2h0EJjdXCs91W3wYkM63pcxtQXYk1RDKy8ntK9MffYZ6ewftA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
الْأَعْرَابُ أَشَدُّ كُفْرًا وَنِفَاقًا
⚠
عرب های بادیه نشین کافرتر و منافق تر از دیگران هستند. / ۹۷ توبه</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83900" target="_blank">📅 13:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83899">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">تحليق كثيف للمسيرات في المحافظات العراقية</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/83899" target="_blank">📅 13:10 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83898">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">اسراب من المسيرات تخرج من ايران</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83898" target="_blank">📅 13:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83896">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنایا به فارسی</strong></div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UQoHVvRgowpfUsQeRDlGyxq5WgAwpdITGCZgc05IXH6zAP5Ur8cT-4xherU-nVXaEV_xfI2rmNFEkDwoyq2C1r3CisK1X6F0SmdAj7fbdeSs1sd5TfmakQ7PYKOOA7IAao07UAhTU9UzNt2U8oq06U0zhbbagbLu9SNEriZxLxyynZG7GTLbJbAi52mCIVpUCwNqwJ_5DDgDm2k4HGG_AaYvGEc3hZldtTpfmq3NiOwN9TYhrvcX9SFkcWWlNL_PX1bTQiK1sI0P9EC9FhHClQrB8nd-1eWsSNoZRh6kJJCJvtHWyQrQidS_W2E8EZIoNMFeyH8Y9ARHSxF9SpOdVw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Q6VUVzTXgOVlqTml02Grzy6buVRbixdF3BHkTqu-q4yecn4PvxaPRqetztM9DpPPeropx6gSMcdVERpupdKI2mluyM0t3nOfmCw3sRyZ2YuzI-E_8csxCXxgb97pbsXV3eaOgRNFYCHpj9pR5BrocgwytowvbvbkRKRY06XCiskZ_4d97rcjuEGOaEV7_sxjROJ0KfeHHRhBZSi3WBEBHmdN68kN5sLOCwPacpegf__MvBWQFzAwNSH-YRXv2wasPSs94BgqpSQmsU62jHrEPUtT6jDcH6Hw73BmwMd0Rwkz4Y3blVpRy50VcLQPxaBmGq1XLh0v0-l68-zItlmgDA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🔻
فوری |
موشک های ایرانی به سمت پایگاه های آمریکایی شلیک شدند
@Naya_Press</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/83896" target="_blank">📅 13:04 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83895">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عدة رشقات صاروخية ايرانية تنطلق من الجمهورية الاسلامية باتجاه القواعد الامريكية</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/83895" target="_blank">📅 13:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83894">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">ايران تبدأ بدك القواعد الامريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83894" target="_blank">📅 13:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83893">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/naya_foriraq/83893" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83892">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">ايران تبدأ بدك القواعد الامريكية في غرب اسيا</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/83892" target="_blank">📅 13:00 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83891">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">حريقين اندلعا في موقعين مختلفين إثر هجمات إيرانية في الكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83891" target="_blank">📅 12:25 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83890">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">حريقين اندلعا في موقعين مختلفين إثر هجمات إيرانية في الكويت</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83890" target="_blank">📅 12:24 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83889">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83889" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83888">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">انفجارات تهز محافظة أربيل شمال العراق</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83888" target="_blank">📅 12:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83887">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b01d4738a0.mp4?token=MfCPPOHd2eWHDDbtUMRgd3ZeKUcldkX96sTwuxXcXtwKWXBBIU2X_whekT4Lm6UuO3YuW4jWDVT3uFRfce4ZoixzU8r98sqdmRjHaoNOcKLc1N-2ffUsrnv8b7c1BoCUuE8mR00BZLhq9n27GrOob6FCJ6jXrxeeBC4pkECCNBFo2xuo2RkG3umTtxcmmIesh9ptlOOVXHiJRd94qJktTrI5_va6emnKhcd3K8bz1UMsmxO1OUqdj_QaH-_RmX70Kvzgf-iLQrAsKTD711OnfMaQHM4kcGfyRqnkm-y1hZ-8IHvCPQUnDAa5LC4qz5RB5nDlQ-w0MO1jkj1LFZQUcA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
🇵🇸
🇮🇷
شظايا صواريخ الباترويت الأمريكية تساقطت البارحة بشكل عشوائي مما جعلها تتحول إلى مصادر دمار لمنازل المواطنين الكويتين</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83887" target="_blank">📅 12:07 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83886">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇺🇸
الخارجية الأمريكية : وننصح الأمريكيين بإعادة النظر في السفر إلى الشرق الأوسط .</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/83886" target="_blank">📅 11:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83885">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">🔻
🇮🇷
مراسل نايا: دوي الانفجارات في مدينة مهران ناتج عن تفجير ذخائر حربية</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/83885" target="_blank">📅 11:38 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83884">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🔻
الحرس الثوري الإيراني موجهاً رسالة للشعب الأردني والجنود.
أيها الشعب الأردني الكريم والجنود الأشاوس؛
كما أدهشت استمرار تواجد الشعب الإيراني في الشوارع لمدة 140 يومًا لدعم الثورة الإسلامية العالم، فإن استمرار ردود أفعال مقاتلي الإسلام، التي تواكبها معونات إلهية وتحقق نجاحًا حاسمًا، قد أذهل العدو وأدخله في حالة من الارتباك والهزيمة، ودفعته إلى الانسحاب من ساحة المعركة واللجوء إلى جرائم حرب وعمليات غير إنسانية ضد المراكز والمؤسسات المدنية.
الجيش الأمريكي القاتل للأطفال يحاول إخفاء هزيمته في الحرب المباشرة مع قواتنا المسلحة من خلال مهاجمة المستشفيات والجسور والسكك الحديدية والموانئ والمطارات وقتل المدنيين.
في فجر اليوم، ردًا على أعمال الشر التي ارتكبها العدو الأمريكي الليلة الماضية، أطلق مقاتلو القوة الجوية التابعة لحرس الثورة الإسلامية عملية "نصر 2" تحت شعار "يا أبو الفضل العباس (ع)"، حيث شنوا هجومًا صاروخيًا وطائرات مسيرة مكثفًا ومتزامنًا على مواقع طائرات مقاتلة ومنصة إطلاق كبيرة في قاعدة أمريكية في الأزرق بالأردن، مما أدى إلى تدمير كامل على الأقل طائرتين وثلاث طائرات أمريكية، وإلحاق أضرار جسيمة بعدد آخر منها.
الآن، حان دوركم أيها الشعب الأردني الكريم والجنود الأشاوس. وفقًا لفتاوى جميع علماء الإسلام من جميع المذاهب والطوائف، فإن الجنود الكافرين المهاجمين للأراضي الإسلامية دمهم مباح.
الآن، الجيش الأمريكي الذي دم القتلة، والذي قتل مئات الآلاف من المسلمين في أفغانستان، ومئات الآلاف من المسلمين في العراق، والآلاف من المسلمين في إيران، واليمن، ولبنان، وليبيا، والسودان، والفلبين، وفلسطين، هم في متناول أيديكم، وتقتضي واجباتكم الدينية والإنسانية أن تقضوا عليهم بأي وسيلة، وأن تطهروا الأرض المقدسة الأردن من قتلة المسلمين الأبرياء.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83884" target="_blank">📅 11:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83883">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8edc485f93.mp4?token=s4p5j0Hg7fDTJViotbcAgdDQ5lMucyR2CG0uBXsSE2IKW4ZIEHBKbUeboeUd3RmDmJS96o_4av5yIB1fykIkXH0TbNDnngu3NPnCRUEpH9pSIc6AfNndPkXCxO7CDR1xyLNtm13gMxHeue1P1uFl3B0G58cZousOvxFm7LjlaeYnjECs5_KZH6ZoX57TUZxKaRnGZINgq9724eiGqdySO6eNwu1tqCW9b6ezinYnNCculZ9XaDkJD8T5d0_udcWRHKha28apSbJYxgwBMkyxqnb5Lbe6tpQvYdt25Vp59V2RaEq1XniAbnggPV48X4jJwDjH-1nmuqCiQI0E7XHrUA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🙃
تعرضت مخازن عملاق التسوق الروسي شركة وايلد بيري الروسية لهجوم بمسيرة أوكرانية في العاصمة الروسية موسكو ، تشتد الهجمات الاوكرانية مدعومة من بريطانيا وألمانيا وفرنسا على موسكو بسبب تجنب موسكو المواجهة بين تلك الدول او الضربات الخجولة على تيار البندريين في كييف</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83883" target="_blank">📅 11:19 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83882">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WaNib9A_9y9DNyuFRAHIO6vCLvVm6Ki4skcanEfNMVYsTVV3xYSEhtr9vO18W1VEPlAOxTie44n5oyj9sh-hytlX1DckyY73qyOrplq_FHU71tVbkDMlEiu-6dgx539HlwVpNuMxzYsNI45gneTmjUGZAOlu41ZR0dntMmZY7LIc-szLED9bF7umKqnJzhCHWDG0nhWgRIzUIY1v-AoScfeArN-fXfg7V_knKEtr_n76ii__7o-n7YLyQ6IQkUzk-OUzYhPxMb98xXAH_0-6G2ZyAoNzVmIQYUjdc1zX4NB2ocOIZBPpGFFd6DaM4TpEOU6Np_GHxqP99I29CHR_DQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لليوم الثاني على التوالي
الكويت تطلق حملة ترشيد الطاقة بسبب الهجمات الإيرانية</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/83882" target="_blank">📅 11:16 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83881">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/83881" target="_blank">📅 11:08 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83880">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">تصاعد أعمدة الدخان من الموقع الأمريكي المستهدف في الكويت.</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/83880" target="_blank">📅 11:05 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83879">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🇮🇱
🇺🇸
السفارة الأميركية في الكيان المحتل تصدر تحذيراً من السفر إلى إسرائيل والمنطقة بسبب "التوترات الشديدة" في الشرق الأوسط.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83879" target="_blank">📅 11:02 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83878">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">انقطاع الماء عن اجزاء من الكويت</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/83878" target="_blank">📅 11:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83877">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/83c6693056.mp4?token=ie5qwieRuWpYm2uPKk-ltPlelIFIiLby5RxtFDN52pvB7cx3H_k6tnr2ZAzHiFGq-fFkwe8MeXyLWdNM7cMa9Lo_94sFzCSvjQeNkBDKjH9tOODatQnvIOaI80djAUVptyYiNq4bhZq_fQXEOy1aQIhXN87EhyIgQNfI8lXJRCOQ2Nb0mPCd6-wMlNR0V5X8aRhyxPaTh_lAuw4n3ygteCqh6BJbLM75Zrp5cyx7P_EKFOAm-EgaeOhkdrfVSg94t84hatFQz4-aA8siBb2RY192l45na4j3BP4v-LihBHkUKmn0fwnFOoC6GsQ7XDgPYl9wlueyqUXDVIsBCbNyJw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات تهز سماء كريات شمونة شمال الكيان المحتل جراء إطلاق صواريخ من الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/83877" target="_blank">📅 10:59 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83876">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83876" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83875">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/83875" target="_blank">📅 10:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83873">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vngtqY7bZ6tRuhgwdzgcrjc1YvS_-_i1UPg8qRcBtCUpRApNOvUjbI3UC7rtLAIs3oVdvrccE5bcNjG1XfrFEMlzo3HnwYnfWtP5rszG-GT1VIcfBBnADqKcO-1mevL9qiYRpTHB4YI3OY5Nocpc1anw703VPZU8x8SYzKz3SownSieMAgA9jY7wgThH2wQQRdbkfEmMuJ0toWPKjWdg0bWHjU5kAaArOVQ60LENm785JfH6o4PN4CaXM365lFVD2pvtUUWgMuBrzrgBoyCzS0ZAPQECvarCsUte8qwav4j9DoQ0SuPuE01HI_zhANZpqMrma8SKtNClc1-nVdvV0Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eQIIM3lnLsB8d5VdHBEZnjz5qF2dwgCOD2WIcse7Wy9hURhsnqGPdVwgo8KDCTABYALWbH4o14DPoB_tCcY1R0RI07pxwi6C5j6Np-etNawTj70M9Z8_IlOr8fFLUYpqu7IBQX12igFlAi_LDODla-mkEUGXK6CbCQH28BUV3UlGwV2qgXV7PO2bT-8_F7qAzw93gGHAYoCdaGn5sw3wPlLLmMa1OBBW7ULwI_2DrpeFmoTxewkVhwCCvhlrd6SSsXoJ27K_zHW9Ud58MHpMGlEAJAH8jrlawpoVA7UBAIe8TiEo9QcqkERCqZNOMnEA5f-oa0_p1tyX_c8jGrS0aw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">هناك احتمال كبير أن تكون طائرة أمريكية أخرى من طراز MQ-9 Reaper قد دُمرت في الهجوم الصاروخي الباليستي الإيراني الأخير على قاعدة موفق السلطي الجوية في الأردن.</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83873" target="_blank">📅 10:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83872">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83872" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83871">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83871" target="_blank">📅 09:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83870">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏الكهرباء الكويتية: هجوم جديد استهدف محطة أخرى للكهرباء وتحلية المياه صباح اليوم</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83870" target="_blank">📅 09:40 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83869">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=BrxqwSr69uJsJK4p30oH8to7PK80Xltn2RTvDS8vq2qT2-I2lc5Umh33rzgulQh8kUIHfPT6-9t_dB9vO--zR_0Q3XDs8jno0bP_qEwVmFrcG6c2s-JiGZYkPGDm7puD5HYgKb3RVQPQunF5y9VQz_OsfHmMocwJu2ajfgKFaCj2r0GBocVeAotwRKlvuqHNlg_kHChK5HYIxRrTIWc90N3GAjwsKPE2qITnLaZ1bl-q0un3iDsQqhl8f_XvY-AbEAirPyYTMdKFOB55AtM7KFy4gpTSGeZYoGNcY3LqqRzUpEfWDAzYdNLZY-HBm4Vlks2q_YyW213ZDf3-KkmqgA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/13b66fe6ee.mp4?token=BrxqwSr69uJsJK4p30oH8to7PK80Xltn2RTvDS8vq2qT2-I2lc5Umh33rzgulQh8kUIHfPT6-9t_dB9vO--zR_0Q3XDs8jno0bP_qEwVmFrcG6c2s-JiGZYkPGDm7puD5HYgKb3RVQPQunF5y9VQz_OsfHmMocwJu2ajfgKFaCj2r0GBocVeAotwRKlvuqHNlg_kHChK5HYIxRrTIWc90N3GAjwsKPE2qITnLaZ1bl-q0un3iDsQqhl8f_XvY-AbEAirPyYTMdKFOB55AtM7KFy4gpTSGeZYoGNcY3LqqRzUpEfWDAzYdNLZY-HBm4Vlks2q_YyW213ZDf3-KkmqgA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي صافرات الإنذار في الكويت دون توقف</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/83869" target="_blank">📅 09:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83868">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TzCnbLGm25B3hyKvC1PHfsD26iujS0kIe1nGcXn7-jcJ9h_Mdv3M3XBG7ngistF4-UJORWhbzA8shIN7YKtEs3wJRvFVmEXpsS3ILbyEFGTQcppdvLHoX6fQUJqShGjVKYJRpTTOU8BrmJOs-dtK9YIe14q4HBKIcizz65ITvk-GI7PQLEd7YbcdHmbVfTeUOsfpuNxYIx-IaYlmZNbZ_g7rv3d5jfqDxVjn-g8Egc_I1hfU9J4fR8It118cyzQyb1rJ0ocTe-syiv6XuXqvpUjiGm15rphsJP6JdjVymb7JVTOWV1VLKNwdn4vWevW7KMS2S1u-5qAY4cIWS0653Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الكويت الان تشتعل بفضل الصواريخ الإيرانية</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/83868" target="_blank">📅 09:11 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83867">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">إطلاق صاروخي جديد من إيران</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83867" target="_blank">📅 09:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83866">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجارات تهز الكويت مجدداً</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83866" target="_blank">📅 09:01 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83865">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/738e610a18.mp4?token=r3GOQFPO6gKX_1eC8OnJnAvXeqL_HOk5l5Bo4I-a7N98G18XIlpI5cOg61hvcU0lOeB2S9_rbNAecZYtD2wsdd-KQLocuMKeMaPAXCLPznQGsVATsAIrLceGN7YA-4kuVBSWZfNSFw-Mih_fdxSfmTczsigoLNqRiufMNrK8rLj79FBw9eEROBBzNM_xIQ-YWd6ueOVpqcVCYJT4GQBWKa36e9W7ThiqsL7S3QhXoHuAfIaM11Azfa3QTiU1aeizHYFHB2QZXTGoFMJDkynU-5jo4y0FrObuIQhkHxjtsPuJbascDkAngStVAetl0-Z3oY8P7IeborEtU4Ho3VrM6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/738e610a18.mp4?token=r3GOQFPO6gKX_1eC8OnJnAvXeqL_HOk5l5Bo4I-a7N98G18XIlpI5cOg61hvcU0lOeB2S9_rbNAecZYtD2wsdd-KQLocuMKeMaPAXCLPznQGsVATsAIrLceGN7YA-4kuVBSWZfNSFw-Mih_fdxSfmTczsigoLNqRiufMNrK8rLj79FBw9eEROBBzNM_xIQ-YWd6ueOVpqcVCYJT4GQBWKa36e9W7ThiqsL7S3QhXoHuAfIaM11Azfa3QTiU1aeizHYFHB2QZXTGoFMJDkynU-5jo4y0FrObuIQhkHxjtsPuJbascDkAngStVAetl0-Z3oY8P7IeborEtU4Ho3VrM6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حرائق كبيرة جراء سقوط صواريخ إيرانية داخل المواقع الأميركية</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/83865" target="_blank">📅 08:49 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83864">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/83864" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83863">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83863" target="_blank">📅 08:48 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83862">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/83862" target="_blank">📅 08:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83861">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/83861" target="_blank">📅 08:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83860">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">الخطوط الجوية الكويتية تعلن إعادة جدولة معظم رحلات الطيران بسبب إغلاق المجال الجوي الكويتي اليوم جراء القصف الإيراني</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/83860" target="_blank">📅 08:37 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83859">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83859" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83858">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/83858" target="_blank">📅 08:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83857">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">انفجارات جديدة تهز دويلة الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/83857" target="_blank">📅 08:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83856">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">الحرس الثوري الإيراني: في الموجة الأولى من عملية "نصر 2"، برمز مبارك "يا أبا الفضل العباس عليه السلام"، استهدفنا موقع تمركز وتجمع القوات المتجاوزة في مركز دعم القوات البرية التابع لهم في عريفجان، مما أدى إلى هلاك عدد منهم، وفي الوقت نفسه، قامت بإطلاق هجوم بطائرة مسيرة على رادار قاعدة علي السالم الأمريكية في الكويت، مما أدى إلى تدميره.</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/83856" target="_blank">📅 07:55 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83855">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">محمد القحوم | زامل تنورة | 2023 Mohammed Al-Qahoum</div>
  <div class="tg-doc-extra">محمد القحوم | Mohammed Al-Qahoum</div>
</div>
<a href="https://t.me/naya_foriraq/83855" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">دكوا عروش الأسرة المغرورة</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83855" target="_blank">📅 07:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83854">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات تهز مدينة خرج السعودية</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/83854" target="_blank">📅 07:50 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83853">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6d059d386b.mp4?token=IUeNOv0YIwN120zJVtH5Yap6nUIZ0mTvxiaZF3xzLAqrYpm7wFNuXjC2pXVeFGirEzINC4vRwajxz-7X44TNiVbCumht5F77QVctjoMdkqirlv-gJNZAvrz-iGFCqCnYIY3NclEHaXjsyPW3XMZZjvR-y-M2T212VgGTaN1EakYbemKlWPrWis-7ND-5V1o0NXGBoQMhbvC9Ds6wjv0PgbKEfnAcNhiQXoDInU2w3MF29OWGhA3AvEVMTd8TSUCHmDsS5GmWbUbNoxe8ApJtJFXbvbNdfI6Xs3PCBa6j-fLRit99dQ_M7ivSglpA49_VGnR43SlcuvFkkuA5ceECOg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/83853" target="_blank">📅 07:46 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83852">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83852" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83851">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">الفرار الفرار حيدر آمد شكار _ شور مزلزل _ الفرار الفرار جاء حيدر…</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/83851" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
الفرار الفرار..</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/83851" target="_blank">📅 07:45 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83850">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">صفارات الإنذار تدوي باستمرار اثر الهجوم الجوي على الكويت</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/83850" target="_blank">📅 07:43 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83849">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/83849" target="_blank">📅 07:41 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83848">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">انفجارات تهز الأردن من جديد</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83848" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83847">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83847" target="_blank">📅 07:39 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83846">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇹🇷
زلزال بقوة 5 درجات يهز مدينة ملاطية التركية</div>
<div class="tg-footer">👁️ 17.7K · <a href="https://t.me/naya_foriraq/83846" target="_blank">📅 07:34 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83845">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gQZHc9R9g3poRW0HNeyWNcE1Uwk-a4y85jzYyPRD38uCsZtc5F115Z7ADBSmuAEV1rhBzkfZgU6yAzzMPt3l47z0k2op26Xjq7ukrYrDbab3EipB79G4VU7v9hwGY0eZEeafu85j-pf8uKI7Oqr__J37r4EkSnT1IvRdf-3X3rZCDbIMOCvfmGQSko2MCdOlXyJsnrqrcsAz8dYolHHSnnSdTQsHsv_oX0b9dfa5-PK6KWCFWyz66A87_LMvYFV3rcN_I6yPRFa-iflsk8e8koxS5tLGe8rth_bgCHnC9VwGXBQql26G7Mu-CWpgHJQuuddy3Y5kG_MTCchEVMdCpg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة الإنذار المبكر أمريكية تعود إلى قاعدة الأمير سلطان الجوية قبل قليل بعد مشاركتها في العدوان على إيران منذ 28 فبراير.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/83845" target="_blank">📅 07:23 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83844">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">هجوم صاروخي للمرة الرابعة منذ دقائق يستهدف البحرين</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/83844" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83843">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/83843" target="_blank">📅 07:20 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83842">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز البحرين من جديد</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83842" target="_blank">📅 07:17 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83841">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/83841" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83840">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/83840" target="_blank">📅 07:15 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83839">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">🇮🇷
هزة أرضية بقوة 3.5 درجة على مقياس ريختر تضرب مدينة بندر خمیر في محافظة هرمزگان.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/83839" target="_blank">📅 07:13 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83838">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v9s_W1TxxiFI9N7uDsVb_mz-fNUH6jQtR40qE3c-WfBIcym33JJK-tPUI9OpHHknsBSIk-MZ7uSbCM_Zkb7P52necGJ5LkdmfzTnzMYVc28oBcMLc5NtGJ-H1NonmjuzLzGXzeMaATYta4revdjdo2jk1uXNEcMYPzSoktP-cpSC2ebsT43jXzvPyOVhM2RtlTPZqKl-px-Kg43TfLe5fA2PCWXMzg1MWMPiLLohzLwlWJqwgRwbtvsxOVIk3YpT-ukS4NX_HRF-2SOtkVIFkfy-RGdV2A_YmIjeaWdhNKGMt1d9mXOXKc_SmWiFtYJsNTcapAJ_BzggZK_RSXEKUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">استمرار تصاعد أعمدة الدخان في الكويت جراء الضربات الإيرانية الأخيرة</div>
<div class="tg-footer">👁️ 17.6K · <a href="https://t.me/naya_foriraq/83838" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83837">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aca3d60dc1.mp4?token=smUDdXtFgGHpsAAavqS1V1CpKydEvYDuIP3ch5vN-EsVeS660D0a5BcJa4XHVO1Kp0gigfly3f3-aL-_TBeyNn7CivGVwGl3sUz2x7YQNAEIiEHT9jEpIpgDD46SNWS4277tQzEq7X8QV-hDcDC1hGr1s7XJz0UsuJQ7sqAEwnKWYf4pxumPJPH_JWTLZLb79C5nojBzsRyQ-Ewphm0cycUUu0HOMNdSB7b8RRm1VYKp5nlyC_MrfJ6Xvh5P9ECG_xKR0X6bPpFm6mUDTeffeViWi08wVrDSf8N0aIujGWxc1tv8Xtt1LAFqn9QfarRwPuJWjfJ7Q1TJZWo3n15ZDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/83837" target="_blank">📅 07:03 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83836">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">إطلاق صواريخ من دويلة الكويت المطبعة باتجاه الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/83836" target="_blank">📅 06:57 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83835">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سقوط مباشر للصواريخ الإيرانية داخل المصالح الأمريكية وانفجارات مستمرة فيها</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83835" target="_blank">📅 06:52 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83834">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">انفجارات مستمرة في سماء البحرين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83834" target="_blank">📅 06:51 · 27 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-83833">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/072ab78971.mp4?token=cxjp59hzS16G7rrrcVkaC60-EFofvahNszDZ6RVN57PShvq64BMYL9UK6bBmIC6F7gd00OEmoYWxAl4-s8FysNSsb4GHke5xlyJE-py6QMj3NsjLraYzeqc9bS5XOiiQDieuatU5ToEk6NN61T8migAdlntsOfFgb-bxCYUmh0UDiRqXF0kUvAFoUxa_zGb1blNBqjMFVWpMxPPwo780aXYM0xm7m3tiu5f_K0RCyv3rSVFjEm5m3scGDAQwOPs9oZJv4JKY7cx6B0xO4snS3nh0rXyh2ZpLd4fC8ws3UEgmmr4ZMUnKwTunKuHL8hJCnG26D7GIHlaKHSDms1q7Qw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طائرات مروحية من نوع اباتشي في سماء البحرين</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/83833" target="_blank">📅 06:48 · 27 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
