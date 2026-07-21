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
<img src="https://cdn4.telesco.pe/file/vIAMeLrxnEoQr4blOGj5skNGhODp_FqsqZrBssMCiSTmO4HfE7mkTN-reJ8GiXFUMCzNwywCxYLBneCXdr-xuCMz-gI7zzSK1oGig4eQS6TlJUQDBdz6KfJH3f4_dAU8PbKWZ1AeNb9AB82r5zOzdBF-8xnRBThxgv45DuSwnf-rQlG4FXnyO2IHwpNT_94KUh6vgvnbEHKkiuSOx7GCR0VDqINKED4FsTfLbjO_2YiQQ5p8SZRhoqe_p67ECvXaPno4Gn-ORoQwonV_WFzXtwHyivTzdjb1uZWuFreGkv-XB_5mt1kLpXqrmqKSnkS3GJZHVjcJSw0O4BbwuQgb3A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-30 22:35:21</div>
<hr>

<div class="tg-post" id="msg-84696">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557ac7f23a.mp4?token=HFZ_pwDAfPLg3xA_5f2kF_Dj_N8C6Wed_j7QEL_gXqJgD6aCvRGMTBYMq28-yQbq-8369FVl2AvSbeSbbe0MDHOgxMo7tqX8j0kBVMUesQcAgZyJBvdKsY8aFrgbys9PGRdFwnUiqjST0AWltSvMATTP-ZBzEk7BXZFT6a9mIWMZFKnl7gDK9FQgUvdrhUY-CAev6bFVDOpWj9ITASNQ2fjaZZvt-JpuFLNcPt7hMwyMQSwDyET9agguW4LrR78-rT0P6WQZ-q6SZJC0syVG7YqZI1rrf5VEVb27DeUe5Pu3ZOc25i8KHJh-mhrtoODoPPNoJ_ZN774B5TLeXFof5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557ac7f23a.mp4?token=HFZ_pwDAfPLg3xA_5f2kF_Dj_N8C6Wed_j7QEL_gXqJgD6aCvRGMTBYMq28-yQbq-8369FVl2AvSbeSbbe0MDHOgxMo7tqX8j0kBVMUesQcAgZyJBvdKsY8aFrgbys9PGRdFwnUiqjST0AWltSvMATTP-ZBzEk7BXZFT6a9mIWMZFKnl7gDK9FQgUvdrhUY-CAev6bFVDOpWj9ITASNQ2fjaZZvt-JpuFLNcPt7hMwyMQSwDyET9agguW4LrR78-rT0P6WQZ-q6SZJC0syVG7YqZI1rrf5VEVb27DeUe5Pu3ZOc25i8KHJh-mhrtoODoPPNoJ_ZN774B5TLeXFof5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇺🇸
مشاهد من الأقمار الصناعية ترصد تدمير محطة الدعم الأرضي وصيانة المنطاد في قاعدة الاحتلال الأمريكي بمحافظة أربيل شمالي العراق، إثر استهدافها بالصواريخ الإيرانية.</div>
<div class="tg-footer">👁️ 3.17K · <a href="https://t.me/naya_foriraq/84696" target="_blank">📅 22:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84695">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">تعليق العمل بمطار أربيل</div>
<div class="tg-footer">👁️ 6.35K · <a href="https://t.me/naya_foriraq/84695" target="_blank">📅 22:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84694">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/69a1201641.mp4?token=vTm-uV38_Zk3S2nznDeLWRaBzarudMFRIKx_sWXgB4M8RPkdOg56HzdA1YNn-G7x9diKHWy6rL7ggpmKtoaaOuQBR5Y02k81shBjbaJhZQnpx8AdoST2HN4vRnApJ04YEE-7kNKYAXY6R7MPKnyphlW9s6QWtFI44NDoLmUAEHlGbh-c31DTE_ZgF3KShJA2j5JFEG8A5DD2VdY1XfCYKho0UXBsC8Wop7VJppZy68YXMyfnHVbySGD9yF1zhwckXQN7TJOopHMMRdFd65xgXYX0aWuwg-ZjCTD7z_7UMLStHqFN39D_q0vMqjiheDnqSYnBebJHHFVirdctMlUBGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/69a1201641.mp4?token=vTm-uV38_Zk3S2nznDeLWRaBzarudMFRIKx_sWXgB4M8RPkdOg56HzdA1YNn-G7x9diKHWy6rL7ggpmKtoaaOuQBR5Y02k81shBjbaJhZQnpx8AdoST2HN4vRnApJ04YEE-7kNKYAXY6R7MPKnyphlW9s6QWtFI44NDoLmUAEHlGbh-c31DTE_ZgF3KShJA2j5JFEG8A5DD2VdY1XfCYKho0UXBsC8Wop7VJppZy68YXMyfnHVbySGD9yF1zhwckXQN7TJOopHMMRdFd65xgXYX0aWuwg-ZjCTD7z_7UMLStHqFN39D_q0vMqjiheDnqSYnBebJHHFVirdctMlUBGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر... اصابات مؤكدة في صفوف جيش الاحتلال الاميركي بمحافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/naya_foriraq/84694" target="_blank">📅 22:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84693">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">تعليق العمل بمطار أربيل</div>
<div class="tg-footer">👁️ 9.8K · <a href="https://t.me/naya_foriraq/84693" target="_blank">📅 21:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84692">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">اصابة بناية السفارة الصهيونية في البحرين بمسيرة</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/naya_foriraq/84692" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84691">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/84691" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84690">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 9.49K · <a href="https://t.me/naya_foriraq/84690" target="_blank">📅 21:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84689">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/765c241b7a.mp4?token=rsebvF48QEVX28gpBNU8bXrZMBuAsunxY_4KzETUrK4IF_JgTrYbGr7wMVCX858BaaMHbNjpTuKehhlH4hEMyiUHkhjstL_4f5vhSUlV40jy7tLiNu5_eB8lGFcifRElGsjIHJm2wc557WvGzShk73Mi-CbuBYtP0Mo4ji1-Ct6K3d7cx1z0XWjLdIyeUQU-dQ_uOVO7ym6nJrKYoRUzwWd99D7L79pKtXUixwI0t5oC8jQer0sXpsifm6YQEWXhT8nw_R3YCr2GI-1zK4lC5yfWa96t8p4FLwewRw1yZdh3JGV3-br-9E9UhoLqHL4Bki5HOewDz2WxW0OUi6WVyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/765c241b7a.mp4?token=rsebvF48QEVX28gpBNU8bXrZMBuAsunxY_4KzETUrK4IF_JgTrYbGr7wMVCX858BaaMHbNjpTuKehhlH4hEMyiUHkhjstL_4f5vhSUlV40jy7tLiNu5_eB8lGFcifRElGsjIHJm2wc557WvGzShk73Mi-CbuBYtP0Mo4ji1-Ct6K3d7cx1z0XWjLdIyeUQU-dQ_uOVO7ym6nJrKYoRUzwWd99D7L79pKtXUixwI0t5oC8jQer0sXpsifm6YQEWXhT8nw_R3YCr2GI-1zK4lC5yfWa96t8p4FLwewRw1yZdh3JGV3-br-9E9UhoLqHL4Bki5HOewDz2WxW0OUi6WVyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
استمرار ارتفاع اللسنة اللهب من مقرات الاحزاب المعارضة في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.5K · <a href="https://t.me/naya_foriraq/84689" target="_blank">📅 21:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84688">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/80d4c16950.mp4?token=L2__-alkM92FQ54upUbpa6drMFZCSClZ8ctG0xyeKLs6FKLIItri_3nwLNdcngTQSVauhgzcJBy0fEl3CpiYVGMDL6VHi8RRk2JK_ZztN6SSrt0RvwzNx87enLT4mMgTzw5L_VRAiHWJr8nBav_yvHmLpwgMZf2rE398SdCVvnGWj8wEOi_FtZ4KSoesIkt5_57wZn2y7oycrDggCIPX7Chc5bD7lUD5FoWLrfoSPaCtkndmI9I1RWSU1ritzJBvxSUFCL-tiJZV2JBWWTyvOj6Pzo393v5g1V6HnKxHIqIOVmwub10DKvQyIw7B44P-o9gTJYHA3jX_JbAsP8EfYw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/80d4c16950.mp4?token=L2__-alkM92FQ54upUbpa6drMFZCSClZ8ctG0xyeKLs6FKLIItri_3nwLNdcngTQSVauhgzcJBy0fEl3CpiYVGMDL6VHi8RRk2JK_ZztN6SSrt0RvwzNx87enLT4mMgTzw5L_VRAiHWJr8nBav_yvHmLpwgMZf2rE398SdCVvnGWj8wEOi_FtZ4KSoesIkt5_57wZn2y7oycrDggCIPX7Chc5bD7lUD5FoWLrfoSPaCtkndmI9I1RWSU1ritzJBvxSUFCL-tiJZV2JBWWTyvOj6Pzo393v5g1V6HnKxHIqIOVmwub10DKvQyIw7B44P-o9gTJYHA3jX_JbAsP8EfYw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
النيران على مرمى البصر اثر سقوط المسيرات الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.51K · <a href="https://t.me/naya_foriraq/84688" target="_blank">📅 21:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84687">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">🇮🇶
🇮🇷
اصابة مباشرة في موقع القاعدة الاميركية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 9.83K · <a href="https://t.me/naya_foriraq/84687" target="_blank">📅 21:51 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84685">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇶
النيران على مرمى البصر اثر سقوط المسيرات الايرانية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84685" target="_blank">📅 21:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84684">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=F_1hjMMFg2dLcxLvWw_lSsSAy1AaXapkQg2DxvSHoi844p2qsETW4FkKuE7rjduE9GKsRK_BU2ZWlNDKj7qbgT6PRYuS-YNzDsivNRKW_BWr5fZ6iye-AeYL1Opp0uv0nLRfITlCY_WSGdPfbj2NO-hd4l_Axg_FyRqNIm1POqIWOTcaA8muJYCijMviG1g6-Fl-dmcIUUlKbmQ8j5Au5bnTy5tJAAWFrLTh7msfJmgklavcyh5fUcOnjAEm80cu6AkpruJYKcX4cQLY8eMa7IKYKMGQLrm9cdQV_lhoedDRZViZgt2Uu_m1TUWmYXqWYLRs6vXqJIEipifhVuSz3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dad9abeee3.mp4?token=F_1hjMMFg2dLcxLvWw_lSsSAy1AaXapkQg2DxvSHoi844p2qsETW4FkKuE7rjduE9GKsRK_BU2ZWlNDKj7qbgT6PRYuS-YNzDsivNRKW_BWr5fZ6iye-AeYL1Opp0uv0nLRfITlCY_WSGdPfbj2NO-hd4l_Axg_FyRqNIm1POqIWOTcaA8muJYCijMviG1g6-Fl-dmcIUUlKbmQ8j5Au5bnTy5tJAAWFrLTh7msfJmgklavcyh5fUcOnjAEm80cu6AkpruJYKcX4cQLY8eMa7IKYKMGQLrm9cdQV_lhoedDRZViZgt2Uu_m1TUWmYXqWYLRs6vXqJIEipifhVuSz3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
اصابة مباشرة في موقع القاعدة الاميركية في محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84684" target="_blank">📅 21:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84683">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ee3de71745.mp4?token=owFzbvYBaYJRa3VGDHy9IH-Ceb3BotKiTwKhwUFwDzkE-IjBncO8G7nT4Z6nIiEZFfeu2L2Yg0vALDRE6lD6_TLh0i-C_vGScDTZS69u6PCjsYAFVAYQLRHM35F9fGL4QRe1Vv9SzlivpzH4DwMHUJfY9-kY0TapA76j2ZTvTq5hEh47mn6YYnVBSraR_hgG8lYF3Cjag1ZiXUazBmh7wAdunFvxqNmsckufb0vijwSb-0gR4XqFDImRMN-MaVYhFDqkAQrGhCSnHAEy_pjProWAlhQ1SI_uBLqt4Gm7T-DBT4lKH0GkXl1EZkPdla8L8qMsamuH4dIIU2-sJ-wZWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ee3de71745.mp4?token=owFzbvYBaYJRa3VGDHy9IH-Ceb3BotKiTwKhwUFwDzkE-IjBncO8G7nT4Z6nIiEZFfeu2L2Yg0vALDRE6lD6_TLh0i-C_vGScDTZS69u6PCjsYAFVAYQLRHM35F9fGL4QRe1Vv9SzlivpzH4DwMHUJfY9-kY0TapA76j2ZTvTq5hEh47mn6YYnVBSraR_hgG8lYF3Cjag1ZiXUazBmh7wAdunFvxqNmsckufb0vijwSb-0gR4XqFDImRMN-MaVYhFDqkAQrGhCSnHAEy_pjProWAlhQ1SI_uBLqt4Gm7T-DBT4lKH0GkXl1EZkPdla8L8qMsamuH4dIIU2-sJ-wZWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/84683" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84682">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/84682" target="_blank">📅 21:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84681">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84bcd374c4.mp4?token=pCTV98pZT1_5rsXkaaf0x_18n8aR0aF2ohlB2nSx0441UrBS25JvY0hyARSqfQosahAYlltYI5WBSzYr9_qT1HO1DjTixE5GJfOkE6uFj1YHoWvaLI8E5sJXhJw63fwwtV4O7jx3833JE6PE_VJjGipWTCsiofg31TT2iyPPZ91dYYagVtThlHeurmBJmjiQ5s14zriUWS56C6Zxxw4RFHtaAlzyXd7xBIi24dxoQGp8U9s8L6WMz3R3HwhBgZk92BmoOuehx44eDsn3u1Di36_PBVKB-2zV5rKIz_UpQfg7UO0oykBubxzur5NGarNptjzUJopQ9dbJDoEvOVJKvA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84bcd374c4.mp4?token=pCTV98pZT1_5rsXkaaf0x_18n8aR0aF2ohlB2nSx0441UrBS25JvY0hyARSqfQosahAYlltYI5WBSzYr9_qT1HO1DjTixE5GJfOkE6uFj1YHoWvaLI8E5sJXhJw63fwwtV4O7jx3833JE6PE_VJjGipWTCsiofg31TT2iyPPZ91dYYagVtThlHeurmBJmjiQ5s14zriUWS56C6Zxxw4RFHtaAlzyXd7xBIi24dxoQGp8U9s8L6WMz3R3HwhBgZk92BmoOuehx44eDsn3u1Di36_PBVKB-2zV5rKIz_UpQfg7UO0oykBubxzur5NGarNptjzUJopQ9dbJDoEvOVJKvA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
الدفاعات الجوية الاميركية في محافظة اربيل لا تتوقف بالانطلاق في محاولة منها للتصدي للمسيرات الايرانية.</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/84681" target="_blank">📅 21:31 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84680">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6435203c20.mp4?token=Z4rrwvRVQKhcHOWkrLcS9ak4Atub09A7nN8Z2boJPPd42TY0SxRgfhpxGhdD8st8f4RFHhHIqyrhHfn-YW02eULXLajdhBKlWrcY5h2_AEIKxUZc_OUHHNLDsRxIjrNBddBLujZdT-p82LM5JunzryfvoyEK-CFiau3dwUgiWcTBNmk9IAYK602AjjSHlYZbg-xNV00pPa5xcD-jcH1wWhH2GsMa_UWog-auOtIt2YOSWg5lQpUbg6s99wWVGzjoCZXvQkFoVznTOojpik-4bHuZAsQ73KjPsCm2waJBedUYn9frqo0wmlTXSOwcWNe9WztupB2XJfCxN6t-HCIgdA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6435203c20.mp4?token=Z4rrwvRVQKhcHOWkrLcS9ak4Atub09A7nN8Z2boJPPd42TY0SxRgfhpxGhdD8st8f4RFHhHIqyrhHfn-YW02eULXLajdhBKlWrcY5h2_AEIKxUZc_OUHHNLDsRxIjrNBddBLujZdT-p82LM5JunzryfvoyEK-CFiau3dwUgiWcTBNmk9IAYK602AjjSHlYZbg-xNV00pPa5xcD-jcH1wWhH2GsMa_UWog-auOtIt2YOSWg5lQpUbg6s99wWVGzjoCZXvQkFoVznTOojpik-4bHuZAsQ73KjPsCm2waJBedUYn9frqo0wmlTXSOwcWNe9WztupB2XJfCxN6t-HCIgdA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار محاولات التصدي للمسيرات الايرانية من قاعدة الاحتلال الاميركي في محافظة اربيل</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/84680" target="_blank">📅 21:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84679">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1ff0cf3d8b.mp4?token=Yyy_uWSG6Q-LQw5sZ2fsg376xzPuxmnqn7N6fVpt48odcnT6zO3LDxg28jpFBcnpqda8JErCNxqNpK6aFGAooADKaZYbthJyGFEJN-mnqOd-2L-_dGyPRNJrOiNfI2bCd0Lw4duxMmId_2sCyeFIaoom6U_ep08_MqZXRqA9TjnNGI53YhJOHaU6pXzJpHVL236v-fEXCA9gqvHtIBA6bTj-PlhB7FUTAD0uL4wIJq5uft_De8UlzRc7hOjG_lT99TZTa9tnNDFA6R2KGMkupgs0JCP8cvEPLu1kxd1BDK9XKn7L6hSSLVMrz_25Zcg-6gug-8w00I11RKf1vuVCUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1ff0cf3d8b.mp4?token=Yyy_uWSG6Q-LQw5sZ2fsg376xzPuxmnqn7N6fVpt48odcnT6zO3LDxg28jpFBcnpqda8JErCNxqNpK6aFGAooADKaZYbthJyGFEJN-mnqOd-2L-_dGyPRNJrOiNfI2bCd0Lw4duxMmId_2sCyeFIaoom6U_ep08_MqZXRqA9TjnNGI53YhJOHaU6pXzJpHVL236v-fEXCA9gqvHtIBA6bTj-PlhB7FUTAD0uL4wIJq5uft_De8UlzRc7hOjG_lT99TZTa9tnNDFA6R2KGMkupgs0JCP8cvEPLu1kxd1BDK9XKn7L6hSSLVMrz_25Zcg-6gug-8w00I11RKf1vuVCUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">طائرات مسيرة في سماء محافظة اربيل</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84679" target="_blank">📅 21:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84678">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🇮🇶
اطلاق العشرات من الصواريخ الباتريوت من قاعدة مطار اربيل شمال العراق في محاولة لاعتراض الصواريخ الايرانية</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84678" target="_blank">📅 21:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84677">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🇮🇷
🇺🇸
ارتفاع اعمدة الدخان من وسط قاعدة الاحتلال الاميركي في محافظة اربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84677" target="_blank">📅 21:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84676">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🇮🇶
اطلاق العشرات من الصواريخ الباتريوت من قاعدة مطار اربيل شمال العراق في محاولة لاعتراض الصواريخ الايرانية</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/84676" target="_blank">📅 21:10 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84675">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/feb398ac09.mp4?token=dn3vXnYjurI7atUj36wOTphP9t0SzXanawJfhGLK0aXIvvAWJ1kTAjoUIdj6hAE50qRDsb7Xf5chXokm2uLxc22WkfK0tI9pGdXcfl-lhPM2ij8QEIHByJbIzsrIKX39hEOKhode9p5bZdkbASs0O5tSkr6RgxWG87UCDfuXkFUJW0N-66_75AFLeZ1pIYGgwpaoNgU7cVSl0LNCON1t8oQns-ATs-frXg2g5PLeGX5k4iIXHT7oV7M9H8mrTm2HThdrMr6B8RM1qaZYwqnR2PTK3X_DcYshYHd01NJhAjmFMC9BArmP90Ij6A-mb40V3RNHYI2u0GLbEWQF6Jifzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/feb398ac09.mp4?token=dn3vXnYjurI7atUj36wOTphP9t0SzXanawJfhGLK0aXIvvAWJ1kTAjoUIdj6hAE50qRDsb7Xf5chXokm2uLxc22WkfK0tI9pGdXcfl-lhPM2ij8QEIHByJbIzsrIKX39hEOKhode9p5bZdkbASs0O5tSkr6RgxWG87UCDfuXkFUJW0N-66_75AFLeZ1pIYGgwpaoNgU7cVSl0LNCON1t8oQns-ATs-frXg2g5PLeGX5k4iIXHT7oV7M9H8mrTm2HThdrMr6B8RM1qaZYwqnR2PTK3X_DcYshYHd01NJhAjmFMC9BArmP90Ij6A-mb40V3RNHYI2u0GLbEWQF6Jifzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
اربيل</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/84675" target="_blank">📅 21:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84674">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9f63ee9925.mp4?token=uWGEgRjOUrdXjPsEZjnxL3DPQWxYbFkBegMeQC3XZlam2POtQQsxJ-DbOUndVnZ-GejG9R8Q_T7tKkNVNTyoyr-O54DzLygHbBxJgVH7xYL9dyy8d0WMDyJMCtuGsqyTsxTjK9NDqePNFRxl59mLL_De6oRBVqQDlJ80lnTOnDfL2ggT5W6ZmppKVPBTH4GE9KUaVrbw3lXa9TJsT1mpgVGCN6bJEKvjD-NWg365j-tXfFwC10_ds48gB4YwviJ9td0VZRTY1YSGDhoA9s-bAe3lg2810qMuSof8G_ntq0eznYkK7u-hVgB4o2GKw8xgf-Tht1jVjSLz2i9wGFJppw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9f63ee9925.mp4?token=uWGEgRjOUrdXjPsEZjnxL3DPQWxYbFkBegMeQC3XZlam2POtQQsxJ-DbOUndVnZ-GejG9R8Q_T7tKkNVNTyoyr-O54DzLygHbBxJgVH7xYL9dyy8d0WMDyJMCtuGsqyTsxTjK9NDqePNFRxl59mLL_De6oRBVqQDlJ80lnTOnDfL2ggT5W6ZmppKVPBTH4GE9KUaVrbw3lXa9TJsT1mpgVGCN6bJEKvjD-NWg365j-tXfFwC10_ds48gB4YwviJ9td0VZRTY1YSGDhoA9s-bAe3lg2810qMuSof8G_ntq0eznYkK7u-hVgB4o2GKw8xgf-Tht1jVjSLz2i9wGFJppw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇧🇭
انفجارات في البحرين</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/84674" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84672">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5545797f5e.mp4?token=IECDshNpLoHf0TL7opuzgFO7Xd64G7w6w2KNHQmFH91vA51Xiv1n8wHLtE5Yuy_pAF4svwhKkOF30zWzQ5VhhtqLuHjsu5gXgLUA1B_j9t6DSpSI3djIkddBbEO3g3PYSqE9F7qe-6AyXkR386wyvq-XRfHxqsWiZ02ygDcrcXNCqn4z-7QCkNWwbP5KtxZkGFkWJ6mmGbyt_DNTYQSW6PJ2Z6FbMgkhjiNn4nvsT31ilptzzfYydcokSfLzMMKb-MXaUduK6TTz74_hUfjebPBjvxa3SB2DIvhKZGqUYuAFLUgYL6xzxbpiXWXMCTKfbYd0K5Fiuwbfi0mn_sTIWw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5545797f5e.mp4?token=IECDshNpLoHf0TL7opuzgFO7Xd64G7w6w2KNHQmFH91vA51Xiv1n8wHLtE5Yuy_pAF4svwhKkOF30zWzQ5VhhtqLuHjsu5gXgLUA1B_j9t6DSpSI3djIkddBbEO3g3PYSqE9F7qe-6AyXkR386wyvq-XRfHxqsWiZ02ygDcrcXNCqn4z-7QCkNWwbP5KtxZkGFkWJ6mmGbyt_DNTYQSW6PJ2Z6FbMgkhjiNn4nvsT31ilptzzfYydcokSfLzMMKb-MXaUduK6TTz74_hUfjebPBjvxa3SB2DIvhKZGqUYuAFLUgYL6xzxbpiXWXMCTKfbYd0K5Fiuwbfi0mn_sTIWw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انفجارات متتالية تستهدف قاعدة مطار اربيل</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84672" target="_blank">📅 21:05 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84671">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">هجوم بسرب من المسيرات يدك قاعدة مطار أربيل الأمريكية</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/84671" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84670">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/84670" target="_blank">📅 21:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84669">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vucb6qovbW108lkKuLyS4FUjzLQocz-9Iw_-3CZbG0T_SVAbMeM48eBTvb4z6bzffkP9B-ku-B4AC4HCbc69mtxVmC_DdRkJ8fzSbkKE7fF4ZUPYd_1WN5GkP2sIaCV1U2zHqr1mspxs-g6_dqDz5PtSWFOuBj_7ZGrhw7dA6X2Or-nyH-c4bKam-BotBxLJmGZeZME83tWV8qZn7g9fkFEOSWc6YR9zFbBGA4PXBaphcKPvEhqgP9lRQZAIPdSPuGsoguKfSdmD_i2S1KpNu0I3RwX2i_I9bLscyJ0oq2P77g9S00KhAySerR9wM61nlMgb6t0Uy5Q5JmfgAkt05w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/84669" target="_blank">📅 21:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84668">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇧🇭
انفجارات في البحرين</div>
<div class="tg-footer">👁️ 11.7K · <a href="https://t.me/naya_foriraq/84668" target="_blank">📅 21:00 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84667">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
انفجارات في محافظة اربيل</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/84667" target="_blank">📅 20:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84659">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/iYyQxzyJChCLoyUmZqdHHx8r-SwrydKLZ6Nx51Tz_KSvyQu_ynunHGvE7bTFY5Co5-OQMqWgJEVbrwxAum1pbhXMW314wajOWIdt6-lQSyPEQPuVFpdJ_aFtqUrkCRhCjqCgQ77FW8y3DhFoq7oYdqQnLq-jTNYVlOggG4f2aq8T5kmU73X9KQkif2Ai-YqLxBSQliJdewb5-_-xPLoj2TIKEBUSKt2ZLzGRBudYrqyP9D6XEXSeJM7MW1WKp-3bErKbLck9WbtpB48NBkY_RMuclVbcQT4l46SceM00_xYNM7-QaamNZJ3unkRO6BDiBOTDJu3tmXxkuC4ZiH9h6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NNj0cUILMsfdMJyU6HPKZLBBrFNQmw1cknaFV3HpRuFCEloG4sseQRZBdWo_ExfThiBV-9F0gmCOXl25_O_DUq4g5qjwa_hWLT6HrbLY4zob7qgmvpjqLEqVEjRGra5wEGCQf-SaB3QSXEYmr8uN_LEbsap26gJQF3osx12Lae8awrk-sQzPMaRA_XSCMXnQ5mSmyk59x8TkwmIAGbNXnPvi_A0WBpQwD0g_HmRhMHQLCSScAsrdQItBjHQHugcHqMU3gSJhxtgFGp2LMfPEzZBYWfqBGJQFROZuFn_WVpDYUPhiQYLzsPXg3PttYIRYh6NqAlZMs6MLABlNIPjL_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/gDvfB-DxfCCXLH5XqXcSnWYUjdP-ulLA0YNvltYrdfelFVSfmFWWIImBdbWAFkGcEdz4X8xw-TXbFfOHCEJ-zXCd8eDIFt88tV6fRawy7mpy9Po9dCZ-pW2Lc74i5v0ahIKIMBtt7Noji_rsJpyX48HkzaKuQhnVefZn1Dm51CGS829ySlX6n6qmsvFk_YP3YDFp8qnDMyvAct7gAAGggVmBE4oBNiyKw64th9GjVP0Z23onE9KEiMnObexiSzvYvZQ1MM5g_rLDLibKYfBkZSMYL_fASY7AdPDFaHQzaPbk_JMvbtnl2-EyGs0DR1NanAyqQu42o3Vp3-rm8ni_Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AELsKl8tVCO6ECwVria5WRo_HoUEe_lLHofrRya4qvJxYbkt_hpVlLsJbrc-5RRrtFRWvDlEUaFLIHgB4n43ly7vfGv1Da9cC-Wa7yT8a-9vd0qhiyw5UnvhqcdAFN_1zbmXDjKDXzmsUbNkzcsTQvZLWhmRIWRM76WGd2tpXnYj2yq5jb70U3_Q2X5_xslm1OWiFRWiV09jk_tMwbUzOS_levNe7kiQfw7w1K7fPvOYq-W-lSyyu0bHhwh_Vvdfm_exEV6M3chPopP8IqsH21KhlxXrFCaDG6TyiblBg8zKdyR7ulw9shaXYdq3saBg7A87HJPJcbZJ4-U_tkmOkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eZHgKzlxSjxt9HiSUIV2Blnl9Y73qbTraTI6bpq2nui7M6O4x-KxuTSOzoIjPtt6SyyNsK3xH0_3f7KVFY_MdO6i8hP0ta3bbLCRIG04QSENWAT0Ij6n2QrJz21MFEHOJVhueaZpQOGHhRmB4k3aacKuliD-9wZgYEqDbU6sR9-GFd1C_-HnbyWEOvG49IL4YDUS9axwaj0z-V_iwlzUs0WeLTZJtaFpm3iEXzt0DwP8uznJ2dvxX0vhDkTB9Ob-IXLobIO879NXUouPAu36Agu84x2cRBykkvQfT3VNm22K4CIJBvvysn4VGxfXO79SVeajQbMLwvYwP8i2Xd1OTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/nw1ESgq_h6rM0qpe2FwzaUDB3uu6NZ7Yx2UTX1PZI08Ajl1ZOdIE4mfaagLAvkipgSYzVHno8rD-ARHZ1-g9lnkguOVduIo_7WYlgBAmIfyW41IWP3VqrXlLjfDwli9WMNTCDPLFnIK88rhXeUf4J0JWHXa4KSFDhm-rYm9M-l-LaL8sIqWKzyXRlB_ggd0RSxJI-wUP7UsjVyxAvdrcx9SMDGkw47-g3R1XFGoKUXWRcKhaqJ85kbIGCvlQUU2tNetsPM4SXPJvArgrFmT6lSXML_8QdagQl28N31zSzK8Vt9CVYPnrSMY5OS1nfkkH8sy55NtX_KjD-9mnJDMSdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Dgn40x-zTCzIejFt3RfBorBezz0IV7dWpDtfhJjYF4b7zp3sxUvgtJYqv8qrd9laWwl_bXcz5pifCurcD342sdVRDwp-YVV7aeylvvKJN_cN5rl7LWc6FCN62D9dtAbC88nAdNEXt_sLD12tGAq1ICd95Q8CVYH3LKCoeCb-6bAUkYNKDyfol_BoUbtZPaFeMIAI7DlD32y4rmsSBrI1jFk98Py1bzXxa4WRy6PUGYInKoztz7wCQTrD02ppaSjUTrCPKjLzzqhVUnwNN-YVf46zinBLEOMlAYW275ypfSe0aDI19nqcRWPmChhj_cEGPF5QHL8hdLEScz3I3DgfWg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/n5NxWGjqNqL-gnn2lmxmh4lCBRIoTrxDoloHA6GAt0KrDkrQp7s0p4GRgTTn_s4132NSMLG3c7NqZN_7AexSwKBf_6qg-A-Z-cslL7wfTGhfN4nrDvn4KBZds7TCj_Lz87juUVPIJMYvE-uMtD6gAFBgvAiAYy3qidiLZY4uXMxPlu8lsGE-hEU8GWU4YCp1dMOrmxdqaRqa93LyjwrNkuA4KIhY2m4b8lRUjrkLNFQfR5tCz4XL5QplUChYduWOGGevV-EVH9fEiFn4xqgRnrkeo4naRwEXrGiSMR3TizysJqMyRCTpRi35WMLsPpejLXBZHNJ_BxrSmdle-5EDFw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇮🇷
تُظهر صور الأقمار الصناعية أضرارًا في قواعد عسكرية أمريكية في عدة دول عربية اثر استهدافها بالصواريخ الايرانية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/84659" target="_blank">📅 20:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84658">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇮🇷
زلزال بقوة 3.3 درجة يضرب منطقة تازه‌آباد في محافظة كرمانشاه.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/84658" target="_blank">📅 20:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84657">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">اكسيوس : ترامب يتعهد بأن الولايات المتحدة ستقصف قريباً جبل الفأس الإيراني</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/84657" target="_blank">📅 20:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84656">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln3xdjt39EegrGv-B9wSZfsExEprmVB_ofDVPurkogkZ0128ANoFjg9IIIs0xGF2i2bDPowc2mOhu_ZsqZl2mXBQ6LD4NejWuo54AfsruBRshC09u2etaNhgDm2uXP-r5f4BtwJBCYE36kIngxWgW7fG81fatg_7oDQjqBJOWxJcE3o4qi3XyIr1o3VAF2i8H3G7Fa49o6WUoxAYiMRLnhVOhK0O78ZYRLVFeGZHXdedikqm7aHvcaAUSF6pg0uxAsOB-6vXxEShyJqLkmo_g0owEz8o46VBgrYziHTXW3ehaxoQCHi7ZGbkskvCDLuNnnLyVIkCcmjJVhRK4Kx0uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
تدمير طائرة انتحارية بالدفاعات الجوية الايرانية في محافظة أذربيجان الشرقية.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/84656" target="_blank">📅 20:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84655">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1841ae0343.mp4?token=uncRLKzbQioqnbWlRDneNYmQrlzutQjWP0X-pTU_MDpwr8Kb2ur3tJ5CcJShzfVVXqAiRsvIfIzABjjqzjGEewn7HYD_wyXwhiFLpJsFX76WSJAb43Uf5RrVtUdsR0MneH2sEorBM_Rzh8dXfbGcAETEKRXIUnBwCA63gc1ScNE1xpmOfmtLM-WOVev6nKvPXhlTt4W-Hrm33otVoYe9-9CwdgrX-igfI7zHgVMK0qNMV9038ZBgkcsxkdMUrmxTuvuaocU6GKNEYlNSjZmx4hIvfagn20rbasbAawILH2-Bnun6LlCoEKtzPTRXkDsz3Oj8u1TBwhcwnyT-ucNGORSvV1rIZhGfa1aFK0GnLwJlefIzo5qhLX0ag9YJ7-Mq6jRHb2gl2wMajNrFAZ8RdLt_EF_CWqkhJ74QNJhirzbyAgcKnYNN5pyGSQP5pmDlVFXpmGIBACZ8vdVsSsmyToDUfmddBVeE_0478ESXa-FMLMp-BfPFxsBZdc3ShvoA9MO_sDQRSXHcrFo0PQnSvJXnPHuOde9wQx-19tCUUIqnBsUag20zMoJm6aQiFiKZRSdYJPTIHHvGgsQSOolL65CScHQWlKeGfi5iuhIZl0TnZlBCjlZ6epDv27wfA1arm4wR0l2071e1jb0W5NOCzuHEkJQlpfJYNBvyo_0zXKA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1841ae0343.mp4?token=uncRLKzbQioqnbWlRDneNYmQrlzutQjWP0X-pTU_MDpwr8Kb2ur3tJ5CcJShzfVVXqAiRsvIfIzABjjqzjGEewn7HYD_wyXwhiFLpJsFX76WSJAb43Uf5RrVtUdsR0MneH2sEorBM_Rzh8dXfbGcAETEKRXIUnBwCA63gc1ScNE1xpmOfmtLM-WOVev6nKvPXhlTt4W-Hrm33otVoYe9-9CwdgrX-igfI7zHgVMK0qNMV9038ZBgkcsxkdMUrmxTuvuaocU6GKNEYlNSjZmx4hIvfagn20rbasbAawILH2-Bnun6LlCoEKtzPTRXkDsz3Oj8u1TBwhcwnyT-ucNGORSvV1rIZhGfa1aFK0GnLwJlefIzo5qhLX0ag9YJ7-Mq6jRHb2gl2wMajNrFAZ8RdLt_EF_CWqkhJ74QNJhirzbyAgcKnYNN5pyGSQP5pmDlVFXpmGIBACZ8vdVsSsmyToDUfmddBVeE_0478ESXa-FMLMp-BfPFxsBZdc3ShvoA9MO_sDQRSXHcrFo0PQnSvJXnPHuOde9wQx-19tCUUIqnBsUag20zMoJm6aQiFiKZRSdYJPTIHHvGgsQSOolL65CScHQWlKeGfi5iuhIZl0TnZlBCjlZ6epDv27wfA1arm4wR0l2071e1jb0W5NOCzuHEkJQlpfJYNBvyo_0zXKA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">المراسلة
: علمت قناة "فوكس نيوز" المزيد عن الخطط المحتملة للرئيس ترامب لتصعيد الحرب ضد العراق.
بعد لحظات
...
المراسلة
: آسف على الخطأ ايران اقصد
😏
.</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/naya_foriraq/84655" target="_blank">📅 20:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84654">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/aac7be9311.mp4?token=lGOo6VrwuOZM7Lb3DsRM-kcyv_W4sND75rhaAvs6ZDTfWcBE-izSdAdoX19Rtz3oK_0zA47O21xifJHAZf9auOsB2IC7zrodnA4UnssjJKHskS_k27tYrt_Ou24cMI2HXmHAIDzNp7cvM2LUgsYPBT2Z15l11NjTGFAvoXqF4JDIX0SviLxxKd3F0wpR4JYocZIMA8Ey-93p9yikwJUZ9bfE5ZZUeh4naYhJapt9aXYwZcMGia1U9uWiNnRCo0ucclyhxDHcdOBQmrgEzMxJWmBWbDoVT2khKNMDjMHu4y1iVitH70zTqJp27iQHulHS1QEkn_DQIOH8RnRQZ5Ryyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/aac7be9311.mp4?token=lGOo6VrwuOZM7Lb3DsRM-kcyv_W4sND75rhaAvs6ZDTfWcBE-izSdAdoX19Rtz3oK_0zA47O21xifJHAZf9auOsB2IC7zrodnA4UnssjJKHskS_k27tYrt_Ou24cMI2HXmHAIDzNp7cvM2LUgsYPBT2Z15l11NjTGFAvoXqF4JDIX0SviLxxKd3F0wpR4JYocZIMA8Ey-93p9yikwJUZ9bfE5ZZUeh4naYhJapt9aXYwZcMGia1U9uWiNnRCo0ucclyhxDHcdOBQmrgEzMxJWmBWbDoVT2khKNMDjMHu4y1iVitH70zTqJp27iQHulHS1QEkn_DQIOH8RnRQZ5Ryyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
غادرت عدة قاذفات ثقيلة من طراز لانسر تابعة لسلاح الجو الأمريكي B-1 المملكة المتحدة.‏</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/naya_foriraq/84654" target="_blank">📅 20:01 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84653">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">🇺🇸
"Afghanistan, Pak, Yemen, Iraq, I don't care if I ever come back.  From poor families how far we roam, So the rich kids can just stay at home.  When I come home with PTSD, The VA hospital won't care for me"  It's a big club, and we ain't in it.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84653" target="_blank">📅 19:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84652">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">🔻
مصدر امني لنايا   عملية انزال أمريكية في صحراء البادية غربي العراق استمرّت لمدة ساعة.</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/naya_foriraq/84652" target="_blank">📅 19:28 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84651">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🔻
مصدر امني لنايا
عملية انزال أمريكية في صحراء البادية غربي العراق استمرّت لمدة ساعة.</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/naya_foriraq/84651" target="_blank">📅 19:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84650">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🇺🇸
‏ترمب: الرئيس اللبناني يقاتل حزب الله منذ فترة طويلة</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/84650" target="_blank">📅 19:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84649">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dafd60b575.mp4?token=Su712TUvsJNIh1WU0TDJLshUZs3NC9apwxRYJQQ8XQ3W8tUB-5p6YPLzWZtBKzuCEmT1Feyh1VasPBIkplVXoovZOEQgAzqkxjht6qUXxjT5aOCcOJbnpkWBbCmKLJ7MErQOPET2xMzr7QMMx5ciloeZTvTRwmETmNtFaD7C6FoNrt2_WQ3hX0LVjUixdrY-4jJtJQIQ6prSrNKzkEIChzBYp689EzkugonFYf1AKjGIMkDeyuJxg5MqJJxvMJZbc6FYQ09di390M3_BFwwtwBroNSQcnZitkkxQMcuTAzajzFGzqYg-h962EmdCjqEOUnVWZBUzezFlRgtVgZFAKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dafd60b575.mp4?token=Su712TUvsJNIh1WU0TDJLshUZs3NC9apwxRYJQQ8XQ3W8tUB-5p6YPLzWZtBKzuCEmT1Feyh1VasPBIkplVXoovZOEQgAzqkxjht6qUXxjT5aOCcOJbnpkWBbCmKLJ7MErQOPET2xMzr7QMMx5ciloeZTvTRwmETmNtFaD7C6FoNrt2_WQ3hX0LVjUixdrY-4jJtJQIQ6prSrNKzkEIChzBYp689EzkugonFYf1AKjGIMkDeyuJxg5MqJJxvMJZbc6FYQ09di390M3_BFwwtwBroNSQcnZitkkxQMcuTAzajzFGzqYg-h962EmdCjqEOUnVWZBUzezFlRgtVgZFAKoWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصحفي: هل تشعر بالأمان؟  ترامب: أشعر بالأمان. لماذا لا أشعر بالأمان؟</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84649" target="_blank">📅 19:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84648">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">الصحفي: هل تشعر بالأمان؟  ترامب: أشعر بالأمان. لماذا لا أشعر بالأمان؟</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84648" target="_blank">📅 19:06 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84647">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7e5d6cb79d.mp4?token=D61XzkM31mJOMtJIP9nEse0X3oP4BvimEQfCFAK0MspgAG3VaLW5a4cpwfHSLxisCuR-bn4Cmb4pL0c0Ov5xKP3UZ2FSGNkhzxxIjDrqj2hC9CA9G_WrNtXq23uHoni6UCtEIa3g8I5Vv6hHcS1jF9bS4wV8ZGhnaCl_vS0W4dgBcfEB6uYjDvMfz8oPqcD2xelXRQgvZSS2BaQaf-jcXWYYkEkkwWlEstgaQbrqD0zw2_S-hqZrAcyxESA9VsfM580X49DKBIbqBSNhkk2lOlJ0228qRWr8uXJ-1MBiLnCLVRNBjGQUX_aojTH8KTZ002Ly8K2OT4grrOZ66lBVYQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7e5d6cb79d.mp4?token=D61XzkM31mJOMtJIP9nEse0X3oP4BvimEQfCFAK0MspgAG3VaLW5a4cpwfHSLxisCuR-bn4Cmb4pL0c0Ov5xKP3UZ2FSGNkhzxxIjDrqj2hC9CA9G_WrNtXq23uHoni6UCtEIa3g8I5Vv6hHcS1jF9bS4wV8ZGhnaCl_vS0W4dgBcfEB6uYjDvMfz8oPqcD2xelXRQgvZSS2BaQaf-jcXWYYkEkkwWlEstgaQbrqD0zw2_S-hqZrAcyxESA9VsfM580X49DKBIbqBSNhkk2lOlJ0228qRWr8uXJ-1MBiLnCLVRNBjGQUX_aojTH8KTZ002Ly8K2OT4grrOZ66lBVYQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇺🇸
ترامب: لبنان ربما مكان خطير في نواحٍ كثيرة.  شباب الحزب
😏</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/84647" target="_blank">📅 19:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84646">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🇱🇧
🇺🇸
ترامب: لبنان ربما مكان خطير في نواحٍ كثيرة.  شباب الحزب
😏</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84646" target="_blank">📅 18:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84645">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/568f296f2a.mp4?token=ddCtKF9nKeJDF5zrJTxlLzNKMxCBUTLzkfkpn892ZdtBW2o233sYjLmf1fmwsSJ5yLnL4FPXECK6DTP3DlmOxhM5xBNADd22fDX20V2eIF_PEpb84573snSIDmNEtwx5B03N_DFiXFRRnD-5vupOrrRz8hrjcjI5i3Icdu4gpV7ho62x0atzYBr_A5BBNjsFRpyzIdnsSlGgHSk1_k47SOohAlSGUQCgpHSyuXVZuzAfG-w4F7WVcKMrWVn-vSPUBd5rrJM99LbWMCatAvrf3hSxZ987b6FDjOyR8hu902Fx_dOJQdgGfV1sQdv73QNjph2oLtWYNjbpIexfZYbJaA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/568f296f2a.mp4?token=ddCtKF9nKeJDF5zrJTxlLzNKMxCBUTLzkfkpn892ZdtBW2o233sYjLmf1fmwsSJ5yLnL4FPXECK6DTP3DlmOxhM5xBNADd22fDX20V2eIF_PEpb84573snSIDmNEtwx5B03N_DFiXFRRnD-5vupOrrRz8hrjcjI5i3Icdu4gpV7ho62x0atzYBr_A5BBNjsFRpyzIdnsSlGgHSk1_k47SOohAlSGUQCgpHSyuXVZuzAfG-w4F7WVcKMrWVn-vSPUBd5rrJM99LbWMCatAvrf3hSxZ987b6FDjOyR8hu902Fx_dOJQdgGfV1sQdv73QNjph2oLtWYNjbpIexfZYbJaA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇱🇧
🇺🇸
ترامب
: لبنان ربما مكان خطير في نواحٍ كثيرة.
شباب الحزب
😏</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84645" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84644">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇺🇸
‏
ترمب
: لم يتم إغلاق مضيق باب المندب، سنتخذ الإجراءات اللازمة إذا أقدم الحوثيون على إغلاق البحر الأحمر.
يم حسين جنتي بوحدة صرتي بثنين
😆</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84644" target="_blank">📅 18:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84643">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a5f3a97f9a.mp4?token=O8gawRVyvS9t4ZdEQjHQWQUUNhnI3rUINYqyE2aUBNcy2aRpMlvKZIs-UVxuy0h8UAjKHdM5lX3uBu1Xt0YS2Srp_beOKhxxc-N4WXQ6S1DF1cKlJCfo_h2VwBO2bw3qJy-w_x81A_6mxDvELfYemPp6iOlN-Q5gS0DVk2pHsY49Ou6RLjRwEdm3oMLYxRVBHZLK-AZlYHiYsaR2NdoW1xkelqCwzRZqVNtaZnh0KT9HOHEidkepW_yextvHDyMZtfoEmY0Q-sZS1nI6046jhdIc-oFjps6hLWOYWAOGg1YYpjJwsGEQO3bbsevKNwyI66qq7U5SGDad10akl_3YGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a5f3a97f9a.mp4?token=O8gawRVyvS9t4ZdEQjHQWQUUNhnI3rUINYqyE2aUBNcy2aRpMlvKZIs-UVxuy0h8UAjKHdM5lX3uBu1Xt0YS2Srp_beOKhxxc-N4WXQ6S1DF1cKlJCfo_h2VwBO2bw3qJy-w_x81A_6mxDvELfYemPp6iOlN-Q5gS0DVk2pHsY49Ou6RLjRwEdm3oMLYxRVBHZLK-AZlYHiYsaR2NdoW1xkelqCwzRZqVNtaZnh0KT9HOHEidkepW_yextvHDyMZtfoEmY0Q-sZS1nI6046jhdIc-oFjps6hLWOYWAOGg1YYpjJwsGEQO3bbsevKNwyI66qq7U5SGDad10akl_3YGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد اعمدة الدخان من الكويت</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84643" target="_blank">📅 18:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84642">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">تصاعد اعمدة الدخان من الكويت</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84642" target="_blank">📅 18:12 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84641">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">في خبر غير مهم
وزارة الخارجية الكويتية:
استدعاء سفير إيران وتسليمه مذكرة احتجاج لاستهداف بلاده ناقلة كويتية أمس في مضيق هرمز</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/84641" target="_blank">📅 18:11 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84640">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا - NAYA</strong></div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">سليت سيفي في سبيل الله #سالم_المسعودي#100K</div>
  <div class="tg-doc-extra">العباد Abou Al Fadl</div>
</div>
<a href="https://t.me/naya_foriraq/84640" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">سليت سيفي
#شاركها</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/84640" target="_blank">📅 18:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84639">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84639" target="_blank">📅 17:49 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84638">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/naya_foriraq/84638" target="_blank">📅 17:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84637">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/evRS7mrIXALjShV1EvOZTm7l55yE3ouwXSTPwhBahh5Jl5-MXXpuhHJVsBHuzTzVd5fBvKr0Wno08JQYL_sNk5mFNwki62KSMP_zVN_CMX_HsuQur4BFEcImMfGCJJOcRfWP_ifWtKio6oKyeQ0oMIzuARp235CrG4X2nbWXJ33j51_GuPGH4x3Z2x4j7yicQqhUG2HFOOwUNDe05E_BxGxc3zzlNGKzTLk-22x6cAmeiQstLWGEhLse_vQS_f0X8tel8GYHtRMrjtoLXonfD1l4LYLOwMEIDaXzA6XtYkcXigg0myRPhJwekSSB0iCIahREhp8FTZg04Mn8JG-Hkw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارتفاع سعر النفط إلى 91 دولارًا بسبب الحصار الذي فرضه انصار الله على الموانئ السعودية</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84637" target="_blank">📅 17:40 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84636">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اصابة مباشرة في البحرين</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/84636" target="_blank">📅 17:27 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84635">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/84635" target="_blank">📅 17:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84634">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vKn_hy9G--_hmXsF2Absh1FGIer49zH6pi0QHjFKC8YSDxNi60SMIB148B6bml4VwAyr_teL4c6W2fdo5M5umktU0D_iujggw152Pj8Ml-kefr-LZZ2PFc0mkcYaEk3f3QIbpkvn_-EJm80A0SKezdKE19ITyRgdTdP4Z0nAKVYeoPj4Vz8CWdrWMPlYWgQ9MvVLEpxkkA8Ksrnkz13dxc1rt4Oug6zvFijgb_4truEFUkfzl1bLV8PsStJdMTklOoBWgVMMQ7kWCXQ46YXKchklfPMj41n6iF7RvzwvGpN_NPp5PQ3O3Suo0WJ8KZiQBxC2N-UFfmtWzxrmEaG2hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صافرات الانذار تدوي في عاصمة الكويت بعد هجوم ايراني مركب.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84634" target="_blank">📅 17:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84633">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U7r1aI8rLhva4tDgsZqmXQ1Suzwfh31Yg04lOlQcSXHa3qS1-rbZaF6M4tloCQzfTLMBhABrsP_T6Egoiz-rE_hXQV8Y_jDw-5q8Wp9mRxv5qw9U6TmiPkE4LCrHuHIE8in35F_IcfjNsH6wi5XsKn3jYGCcCcBbYqctKBOeW7XhgvW5CsMvlRm0U-PbaGlFvhZWoCtD4RnGBXdcN01TBDTpa2JljI7z4VGHVMiYIEjRZR23ThGRpx0YLhk5HtjK65GysTRuveu9xb6gtSoZ7ltoJEfsmgWAEXe21g6wITuHB8YZGS5pGCkJhgEpHFMuHq4LLpBJ9KnXTGGnDdbfzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/84633" target="_blank">📅 17:03 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84632">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ac0adb9946.mp4?token=hxULpytNB9c7tP08hHKn8uwvM7n6-FyuXnnKX1pK6zBMCDN-27BGt29c8N6cTVeWjvrzeNsG-cdqnvYZx9JXq-L05LzBRjGl0iwlb_YiTsTvdTUELmVzWVgs9llb_Pi74Dd1QcmEVpiUISG30f-_PtXsrDd4oiTo7jwBW4yFfCjjpuH46cHA2RyZl9A7Oi6oCfBTUXoc7zaAN5bAUkraBkx_3r9uisK7jJ-GR_RwSaHhKhJjA4SzZZOeCQmtAbEALX2ZBm9qw32SSAt_yeB3gCR6HIVLIu6KV-YTI7sJT2x2f4WCqPZQvTZHtXoT6zXJ_a-wFgXP-C1SPdHT-Y-u9Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ac0adb9946.mp4?token=hxULpytNB9c7tP08hHKn8uwvM7n6-FyuXnnKX1pK6zBMCDN-27BGt29c8N6cTVeWjvrzeNsG-cdqnvYZx9JXq-L05LzBRjGl0iwlb_YiTsTvdTUELmVzWVgs9llb_Pi74Dd1QcmEVpiUISG30f-_PtXsrDd4oiTo7jwBW4yFfCjjpuH46cHA2RyZl9A7Oi6oCfBTUXoc7zaAN5bAUkraBkx_3r9uisK7jJ-GR_RwSaHhKhJjA4SzZZOeCQmtAbEALX2ZBm9qw32SSAt_yeB3gCR6HIVLIu6KV-YTI7sJT2x2f4WCqPZQvTZHtXoT6zXJ_a-wFgXP-C1SPdHT-Y-u9Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صافرات الانذار تدوي في عاصمة الكويت بعد هجوم ايراني مركب.</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/naya_foriraq/84632" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84631">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84631" target="_blank">📅 16:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84630">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84630" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84629">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BKI0XcfuT_RdD5qrgKXn0iyw7_tn1Hd6dJ0ZEnN1SPJSgtSCFyZLsOI1291SXwmdiORUdWtzhgR5uv7cjuKHgk3LH5ojQHkt8vQ4yEmq6SVRohRODDoCSAOzxroLizLpFB_jiICG33c0TaMC-KFpj-JkALXcUWgUBGpI3tyaVyGk14Rgg-HyRwu4C3ASZfCVVHw1LcqVmSkm7ltVHUq9CRbpqcIBuhHkEEP0SIyLSsYLuhzwV8Pa_O0yKbMwUQo9kqC50-F12SLpnZ1gnL5v0OcOKggogCvrVsfVu67A3Bd5YOyjBTip5fZHiH8kZSmleNMwpls9tk9eo2QntQl6Mg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/naya_foriraq/84629" target="_blank">📅 16:57 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84628">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">انفجارات تهز الكويت</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84628" target="_blank">📅 16:56 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84627">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇫🇷
🇮🇷
‏استدعاء القائم بالأعمال الإيراني إلى وزارة الخارجية الفرنسية بحجة احتجاز موظفي السفارة الفرنسية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84627" target="_blank">📅 16:23 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84626">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/naya_foriraq/84626" target="_blank">📅 16:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84625">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/84625" target="_blank">📅 16:14 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84624">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأمريكي:
جمدنا محفظة عملات مشفرة بقيمة 130 مليون دولار مرتبطة بالحرس الثوري.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/84624" target="_blank">📅 15:37 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84623">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🇮🇶
شركة شاماران بتروليوم الكندية:
تعليق إنتاج النفط في حقول دهوك بإقليم كردستان العراق على خلفية التوترات الأمنية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/84623" target="_blank">📅 14:48 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84622">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n1yieHXdn7DAEslOLzbcKOgmDKJEYy5QviiM2ZuKQCYITdf7yk7SrcOguavLZCxdEdaorHu_uH2HkocseDjWOZwhZ0FPGOKjmXGSJMAP4wu0314sMVv7i0pyAY4dTqasdLHTH8fnmyVnzl63AXG8NIYW2BbLlZ9Iz0g_xk3136SYuU2cLXThO007ZO53KDQ2h8nfTk9mPaWCYrtIx2oNqC15awl3F8ndJo1vSOc2YzP8gQXLU6thZSN1X4ZoskMAjaCTJ6hc2r5qFi2UGOVCKyvffihp8k7q9vTfJOv0xZnt3LoXNSFcJ_NP-uYtFv5gt3hwuUsnLpP3_s27YGxCIQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
صور الأقمار الصناعية تظهر تدمير خيمة معدات منطاد استطلاع تابع للجيش الأمريكي في محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 24.5K · <a href="https://t.me/naya_foriraq/84622" target="_blank">📅 14:41 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84621">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🔻
شعبنا المسلم في الكويت
قلنا لكم ان العائلة الحاكمة في الكويت غير مهتمة مطلقا بأمركم و ان جعل أراضيكم منصة اعتداء باتجاه الجمهورية الإسلامية في ايران سوف يعرض مؤسساتكم للخطر ؛ نوكد لكم ان المياه الصافية والكهرباء قد تقطع في الكويت كلياً بالساعات القادمة وأنتم تعلمون ماذا حصل في محطة الزور ؛ ننصحكم بتخزين المياه والمواد الغذائية الجافة والتوجه لأقرب منفذ حدودي باتجاه السعودية .. دمتم سالمين</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/naya_foriraq/84621" target="_blank">📅 14:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84620">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">استهداف محطة الزور في الكويت لهجوم بطائرة مسيرة</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/84620" target="_blank">📅 14:29 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84619">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">الكهرباء الكويتية: تعرضت مساء أمس عدة محطات للقوى الكهربائية وتقطير المياه لهجمات لليوم الرابع على التوالي أسفرت عن اندلاع حرائق في عدد من مرافقها.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84619" target="_blank">📅 14:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84618">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">تدمير محطات كهربائية وتحلية جديدة في الكويت</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/84618" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84617">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">تدمير محطات كهربائية وتحلية جديدة في الكويت</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/84617" target="_blank">📅 14:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84616">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇾🇪
بيانات الشحن:
تحذيرات صدرت من اليمن عبر البريد الالكتروني لشركات الشحن لتجنب ‏التحميل أو التفريغ في الموانئ السعودية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/84616" target="_blank">📅 14:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84613">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/UG_24wEc19UdMm4vBqPC7SbLgSio31aB3K7i8ZZrQodxZ5Yl8HoTqzqwpQXfsDjoTi4t4ULmZNXMVuiYL2BUEOFvBPLChs5z31QvoAvZV9Z5xHqHorkPSVpZjWmUTUlU0jk34gaFvfkVxecoSnGPJgyvQOfxMOQUAGxMwOk17qG0OFJMZHLtWYi2mrHv88iD7-ct4C5LXFg9S3dR55gFd5L_c4wSRe_XK7zPB9q5DlS9S8QBmoiAvVeRTuVDog2Gv-Z7cw3STLzdMnZ5ZYg5De_ttRi7LduL8pKhDFZLfipp0JdMm40_dZ8P8NahZ72H-vwCba8wArroRbfOPL1Yxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mzJCBFKg6oxcBDPti2TRM_pORom9UdjNo4nesq1E24jA63ro-_qVx9QlpS-_qLZtlc_uC7biOWkN_6Ft8yJhneDshRVyhwdtjMD_CiMrH7mBwK7i58umylGvdvdHrny3g89I6BloXvds3MQEo4vYgKIATeUYWXdETVgQOXT_upXgPoO0z4NHV99Wa8s2bVacGrC7oG7NorahJAoQ0V87HMzfXRrj1Ovxcsu8hyaaWq1xDqaTfxRS3ARG2T0ADuzxS56KdfSbcZIRquzafK0A5PdcU9L-CnDnBU9tcQcc1oVbLQK2iCDyu1Kin83IARcovezYXa6znHpzdGZ1YpLh5Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45bbd67ccf.mp4?token=Sr9M3Pt6_8IoZZHqCEOnNYh0ghcI2iWj99TmSOWs98ir2wey8jrNQzOM4w5bCdk-qmdGs83AyVlplhqW2S_QTdWI639cjLEvG0_VSAZHP7psqQoddmzZ3Se0ZIfXzDsrOGk-lLexdhDaa6zIG9dkbKzxaHgrW2OwDsb9auPFiLkSKfTsHEIZJoMVOEM4wiMnp11-5MikRs4M_Ft8PEhxcpALcrm2l490NoJHLBEXpPpmKm5S-_m3eRk6wOFESuev1GGTki0hR-VUJYx5z0Vg_gOcLR6sOD6SHBpuX19ASmF9ZH68AB6eaPXI3oMb7RitWlZMt-O8-5oPCEF3n3H-ew" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45bbd67ccf.mp4?token=Sr9M3Pt6_8IoZZHqCEOnNYh0ghcI2iWj99TmSOWs98ir2wey8jrNQzOM4w5bCdk-qmdGs83AyVlplhqW2S_QTdWI639cjLEvG0_VSAZHP7psqQoddmzZ3Se0ZIfXzDsrOGk-lLexdhDaa6zIG9dkbKzxaHgrW2OwDsb9auPFiLkSKfTsHEIZJoMVOEM4wiMnp11-5MikRs4M_Ft8PEhxcpALcrm2l490NoJHLBEXpPpmKm5S-_m3eRk6wOFESuev1GGTki0hR-VUJYx5z0Vg_gOcLR6sOD6SHBpuX19ASmF9ZH68AB6eaPXI3oMb7RitWlZMt-O8-5oPCEF3n3H-ew" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
🇺🇸
توثيق يظهر الدمار الكبير داخل إحدى القواعد الأمريكية في المنطقة جراء استهدافها بالصواريخ والمسيرات الإنتحارية الإيرانية.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/84613" target="_blank">📅 14:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84612">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اطلاقات جديدة من ايران</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84612" target="_blank">📅 13:44 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84611">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">استهداف سفن  أمريكية قبالة سواحل قطر</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/84611" target="_blank">📅 13:32 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84610">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">محافظة النجف الأشرف تقرر تعطيل الدوام الرسمي يوم الخميس بذكرى شهادة الإمام الحسن المجتبى (ع)</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84610" target="_blank">📅 13:26 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84609">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bX1o1IlPsjnn5JBsNoz_cKNVp3VoOni6VCQTz2CYaCvRwqb-bXE0yj3OglcCJ6cx8UKSNR7rCf5FonrBsBJwGIpmEu5H7iNJP5aaziIKOa-HwvX21nuGViJvsfnxUOqqDuJpEpzbHDTC2Lx25TLnkJYl65AK3mpt5BNUInQlJDrBsghDQv9oDP2zC0k4srSrJbDIRa4uvuMSL5kptKXwtSFVPd1vwsLtAShOocmi3stbtgZct0Xyx3k06CvhGXkVN-Pg5xCkntwQJRcXjEskzFwMmduPMoJ0P-lzw9SwvFBWOGb2OC-i92oqH-pRfqsXrTXMqdS5zNd5Dg50PVZKTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">كما تم ملاحظة وجود مسيرة أمريكية ثابتة لأغراض المراقبة والتجسس انطلقت من السعودية باتجاه قطر ..</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/84609" target="_blank">📅 13:25 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84608">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G5FPzUC-u5Dm9ybjU0b_lQWKpM-Cv0nFMVbYjA4KYeq4vPBzpG85_B4cpe3p4JLJkwjzI0F7jnlJmhZxZe2M80Z-rkyjYxKS9XtOsgE8TjetAKXfG7DwKWxvH5THCnA2H18GMa3F7j8joedLNAr-ouYOWrFmaTNrtEaaW7Jm2Qgx4jAkgVYALIkQiq-K7tIl8xoizLPA1NtcZxOTrXEDAAVU8W9SX9dxOxmroRrQ0GCRme6Q5yMeZc89ej1Y0R9LgJdwMcqhO6OCdj2FcynPiNZhprtvBDnO7qs2v5TLEqpehgSAmfLzP6pSHQwWuczDo4OP16ITTUuI8XrRPgAE1g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">على ما يبدو تم استهداف منطاد تجسسي أمريكي في سماء قطر امام سواحل ايران</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84608" target="_blank">📅 13:24 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84607">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجارات عنيفة تهز شمال الكويت</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/84607" target="_blank">📅 13:20 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84606">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d1125fa749.mp4?token=b9siBfR9uDmKAkS9VzqOJJd_BTd5PAqt6rzkarvJL8SW63LlgGZuQdKhEf94jg7R7R8tajst6K3FRPrTSgg6ixTqtejjG3_8iB1PaSZMT0P9lZV_OIBeyYK5NyHAVLos99S-PD7PuEZzEuipzqJvcPSH7WE53wmPu0HPmt0bUtLw7QNNJ8RV0gW7tigbaZzu97aFohjZ9FBBSaPpjWDAoaw8b8lxeaq6X_57OSp3V1DgCX5JGSQKhun4TP8t11uT1HFG2aaLbZykv9m0mbSOAPnuAM0hS5RDMvgRcR62MzCzPSOD-vbIWTdoJMP1TtbIJ_rjcELgLPuAUvAbfL_3Dw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d1125fa749.mp4?token=b9siBfR9uDmKAkS9VzqOJJd_BTd5PAqt6rzkarvJL8SW63LlgGZuQdKhEf94jg7R7R8tajst6K3FRPrTSgg6ixTqtejjG3_8iB1PaSZMT0P9lZV_OIBeyYK5NyHAVLos99S-PD7PuEZzEuipzqJvcPSH7WE53wmPu0HPmt0bUtLw7QNNJ8RV0gW7tigbaZzu97aFohjZ9FBBSaPpjWDAoaw8b8lxeaq6X_57OSp3V1DgCX5JGSQKhun4TP8t11uT1HFG2aaLbZykv9m0mbSOAPnuAM0hS5RDMvgRcR62MzCzPSOD-vbIWTdoJMP1TtbIJ_rjcELgLPuAUvAbfL_3Dw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇰🇼
صور الأقمار الصناعية التي التقطت أمس تظهر أضراراً جسيمة لحقت بمحطة تصدير النفط الخام التابعة لشركة البترول الوطنية الكويتية في ميناء الأحمدي.</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/84606" target="_blank">📅 13:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84605">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">تفعيل صافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84605" target="_blank">📅 13:19 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84604">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">استهداف سفن  أمريكية قبالة سواحل قطر</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/84604" target="_blank">📅 13:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84603">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">تفعيل صافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84603" target="_blank">📅 13:17 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84602">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">تفعيل صافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84602" target="_blank">📅 13:16 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84601">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">تفعيل صافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84601" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84600">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">تفعيل صافرات الانذار في قطر</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84600" target="_blank">📅 13:15 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84599">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🔻
مصدر لنايا:
حل والغاء قيادة العمليات المشتركة في العراق.</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/84599" target="_blank">📅 13:08 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84598">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/84598" target="_blank">📅 13:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84597">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/84597" target="_blank">📅 13:02 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84596">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84596" target="_blank">📅 12:59 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84595">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">انفجارات تهز البحرين</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/84595" target="_blank">📅 12:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84594">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اشتباكات واصوات انفجارات تسمع في مضيق هرمز</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/84594" target="_blank">📅 12:58 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84593">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">انفجارات تهز الاردن</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/84593" target="_blank">📅 12:55 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84592">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">صافرات الانذار تدوي في الاردن</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/naya_foriraq/84592" target="_blank">📅 12:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84591">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">اطلاق صاروخي جديد من ايران</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/84591" target="_blank">📅 12:54 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84590">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/91fd9dc5cc.mp4?token=XmI9LCq3kZhVFr0QCw4hBvHcv8ZrhcAJ0vZr_kNtbGvrFECUy9fKzTZw2jY0P35rq1KJWQnGqy8UUFvNk7qoOdKRDEaFbeoEh-m7sCM_ZTFHBDncgRpNxugVXCZqAJZNfGf8SDeJX7vW1w3nH8TEHXy_NF7ShMfMd1MwJoYVzXPmUpvIGFX4dacZKFBREl34aWi9faNIfga1iq9PxI1nwEwWDSUtqrk5Uf-DaGdH-mI_TbeFT23F9ZTwATvDMhzEPV_5noE8e_0v7C3nRv91r_yf3VjDRB3_2sEsEJiu08kdJU2hu_E5sWWTWSfCSqlj0783K1maxhw6nv2h9jHXHQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/91fd9dc5cc.mp4?token=XmI9LCq3kZhVFr0QCw4hBvHcv8ZrhcAJ0vZr_kNtbGvrFECUy9fKzTZw2jY0P35rq1KJWQnGqy8UUFvNk7qoOdKRDEaFbeoEh-m7sCM_ZTFHBDncgRpNxugVXCZqAJZNfGf8SDeJX7vW1w3nH8TEHXy_NF7ShMfMd1MwJoYVzXPmUpvIGFX4dacZKFBREl34aWi9faNIfga1iq9PxI1nwEwWDSUtqrk5Uf-DaGdH-mI_TbeFT23F9ZTwATvDMhzEPV_5noE8e_0v7C3nRv91r_yf3VjDRB3_2sEsEJiu08kdJU2hu_E5sWWTWSfCSqlj0783K1maxhw6nv2h9jHXHQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الايرانية في سماء الاردن قبيل انقضاضها على المصالح الامريكية</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/84590" target="_blank">📅 12:50 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84589">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/geetNphxMZZ0hv84tbDOQRG_G4oKJzFRD3nXe8yiMQT2cp12xDqR1MxMV40tSiPYa6qsy-UoT74BymJZdmsVSzQdskEA_Ge8KNf0IyA2D82OkGKcuRXHJmIcq4AAb6uMKs21rmCgxrSm3ZbzOKVx2v-OZ9N_URy5p2yXwRb3tH8r1rt5SsQUIsAzlbN-Rf_sxRBzDR9kCkfG0wu_HUl_o9iHnbqyZ9cR22M_5hr300OGzCLZF9_nbF074x6V5lKPl5njkcqTiCI5HYXoCX3nAaV-J4oL3I6x1DafrGr82it23IbZsCEk8GM3VZW4SrTIYkh3FOGaAAHKS6VyO02z6w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اطلاق صاروخي جديد من ايران</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/84589" target="_blank">📅 12:46 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84588">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">سقوط مباشر للصواريخ الإيرانية في الزرقاء</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/84588" target="_blank">📅 12:45 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84587">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">وقف حركة الملاحة في جميع المطارات الأردنية نتيجة القصف الإيراني على المصالح الامريكية.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/84587" target="_blank">📅 12:34 · 30 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-84586">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YF9tNXfWnaROZXspZUMhPiJsvhFTGP6QoUnpVdiH7bqGAh8XdKX3iOjZBTZ-Qd13EtIQMvUde3oIM4UN4QIUGSddPaUozMg_oBOB9-6xOVOxHLQwXz4fgwEiLBROeYqyI7tId5p21fJaRHayNRjtEVhcnym4cEC8IT47AxszaeYQnBdKt2Ol0_FiSki56URgUX6tRuxRlv2bpIJao_1OvtjpU3qBo86R31vZcLYFEP1RI8tEjnNO9cIopImcqwFIrR5fwViYl7WbR0uGGUQ5O4zpUsfbaP9n7GVk9kzufYNd7pHofSTcU6fiPMR7g8ExVtMqAh_L4paH6q5Fk5xRUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله أكبر</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/84586" target="_blank">📅 12:28 · 30 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
