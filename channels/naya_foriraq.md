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
<img src="https://cdn4.telesco.pe/file/AncggfiCU95rumxzJa7ML3cTDnN1NjH_nk7JcelTkrhZjO7enmJUsOKAqv_vNfmJtVRP-VzzBYfXKO__qSmzR7Nd02wBlpzM8Wflc95ZDWtdEwQ5ZcPC7gg-uN7MJQQH_q3cLY2c4NWAHgMwTQqWJURgCyGlDrWw4Q-aMAHQdCLNTmyTKPrWg50eEzQMWnN4WI_iVbT_nV3ZxedVv3hHBdf3nBXcn9sFTCtdMAPPikzAp2tenASRdpbhztlL9d3w5Rn5ZrK4KIiorvnv1II4EI0n4Rp4Z3N3CLlcK8iO-IWpBl5Epue2MQ58CebKjzRBlqVT9MvYVEbTMgoV7FoZGg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 272K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-05-07 05:18:31</div>
<hr>

<div class="tg-post" id="msg-86037">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">قصف مجدد على محافظة ديالى بمنطقة سعدية الجبل</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/86037" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86036">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">الحرس الثوري:
قبل ساعات، تعرضت ثلاث سفن نفطية متورطة في مخالفات، والتي تجاهلت تحذيراتنا واستمرت في التحرك في مسار غير آمن وغير قانوني، للهجوم وتم إيقافها.
القوة البحرية لحرس الثورة تحذر مرة أخرى، أن التدخلات والأوامر والنواهي غير القانونية للجيش الأمريكي الذي يقتل الأطفال لن تمر دون رد في المنطقة.</div>
<div class="tg-footer">👁️ 2.73K · <a href="https://t.me/naya_foriraq/86036" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86035">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">من العدوان السعودي الأمريكي الغاشم على معسكر أشرف في محافظة ديالى شرقي العراق</div>
<div class="tg-footer">👁️ 2.77K · <a href="https://t.me/naya_foriraq/86035" target="_blank">📅 05:16 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86034">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZqDHAziMf9yxTIm7A_SNfPV5ucy0yEZwStgqjxcdn4IA7wOkcsePDRIhFP0gsLrQWOzSmDYUPETkK70R3NFpU1serDCGyce-7GUd7kzXApE52slkHVJLqDTKixElVLYQb81SWUSNjvD_KFqBj9AHYZ59U5-9n0-2iilzm09NHf5NgBGpMkwAnJJ2WL_Ha5qrFmSjqErqUZgHrL8KeJDwltwHD7KbTJ6a148V5NHqEPOYRzoLglGPvMwUyyzpsZY0WIDznUnjhPELmWuIVZm1Hpp8bQrkZPXP4LFWudTedvLHhr_vZ7S7ZN9yyZPiCDWBXrRrPVcnSb7fzwaUBIxf_g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اشتعال النيران وتصاعد اعمدة الدخان في معسكر أشرف الواقع بمحافظة ديالى شرفي العراق</div>
<div class="tg-footer">👁️ 4.44K · <a href="https://t.me/naya_foriraq/86034" target="_blank">📅 05:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86033">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تذكروا شعبنا الكريم
العراقيون شجعان وهم ابناء علي والحسين وهذه آخر رفسات ال سعود سوف تدفعون الثمن غاليا وغدا لناظره لقريب</div>
<div class="tg-footer">👁️ 6.1K · <a href="https://t.me/naya_foriraq/86033" target="_blank">📅 05:09 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86032">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/86032" target="_blank">📅 05:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86031">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">أربع مسيرات مسلحة فوق المنطقة الخضراء وسط بغداد</div>
<div class="tg-footer">👁️ 7.48K · <a href="https://t.me/naya_foriraq/86031" target="_blank">📅 05:04 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86030">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1167650f56.mp4?token=WdlRtdQok5BsGoDrplXJgCBe4VLmDoqU034QCePrRyGz-l7I_NpkxwfmTa3FwXeQJcdneeuOGnVMiX86Sfz-FfaaiVPZN0-WD4WPKizp6LloqEDlaEG3qdyfg0ndzBIiDmF32q93I_om4bLxaHpHaU3_2W8qf_KDRxvnwGs1kAalZrJ1tBVuGPW_zHq6YkapkGRPU6WAkDVpjzJ_4qx1FB6tZf7RWq7mRAVJGydAMHcRJtND7aFQC7rcWfTmOwigqNJOiJnLQh89nWpahzywjBZ9I7O7mpsyMDkUjGdAliwoN7EI6ynk3GzmIgOuj_K-3ZsdMQnsIHSCY8GqYy3J4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1167650f56.mp4?token=WdlRtdQok5BsGoDrplXJgCBe4VLmDoqU034QCePrRyGz-l7I_NpkxwfmTa3FwXeQJcdneeuOGnVMiX86Sfz-FfaaiVPZN0-WD4WPKizp6LloqEDlaEG3qdyfg0ndzBIiDmF32q93I_om4bLxaHpHaU3_2W8qf_KDRxvnwGs1kAalZrJ1tBVuGPW_zHq6YkapkGRPU6WAkDVpjzJ_4qx1FB6tZf7RWq7mRAVJGydAMHcRJtND7aFQC7rcWfTmOwigqNJOiJnLQh89nWpahzywjBZ9I7O7mpsyMDkUjGdAliwoN7EI6ynk3GzmIgOuj_K-3ZsdMQnsIHSCY8GqYy3J4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 7.47K · <a href="https://t.me/naya_foriraq/86030" target="_blank">📅 05:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86028">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8d92650316.mp4?token=BG4WUVuTNvj8Grv9TONZLzEh7a6F1b-0lKk39lX-2ku3xBmyI04OtcdA3UhITRwd8KZfz3hPeuf3dZqaaEdNYcvgOPpVHCjO_yGahCizlSEfRO570Eqwg4pcm3Oz6gNhHgKNQGXcFN2zdm33-gVkfYBz4t2GjRB_fdqKltny4p8sI7XbH478qKTJu_DdYqxY2aZn4MmtwbLS9994o9V7VDLG2V7mzbRfJgv6R3O3dNLNSx00S-rluP7uRpmEnnmz9u66tErzlbx7Ojt_N6Yf_qnilsbXz1l7jUQVKVpJe0IB2Xl-bhP_jTKcqWmtHsR2ZJdvp2ccKRmQZFYVT4c69Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8d92650316.mp4?token=BG4WUVuTNvj8Grv9TONZLzEh7a6F1b-0lKk39lX-2ku3xBmyI04OtcdA3UhITRwd8KZfz3hPeuf3dZqaaEdNYcvgOPpVHCjO_yGahCizlSEfRO570Eqwg4pcm3Oz6gNhHgKNQGXcFN2zdm33-gVkfYBz4t2GjRB_fdqKltny4p8sI7XbH478qKTJu_DdYqxY2aZn4MmtwbLS9994o9V7VDLG2V7mzbRfJgv6R3O3dNLNSx00S-rluP7uRpmEnnmz9u66tErzlbx7Ojt_N6Yf_qnilsbXz1l7jUQVKVpJe0IB2Xl-bhP_jTKcqWmtHsR2ZJdvp2ccKRmQZFYVT4c69Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 7.43K · <a href="https://t.me/naya_foriraq/86028" target="_blank">📅 05:03 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86027">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0c2eb5cfa4.mp4?token=P59smr9Cs7U0WliK3MAhTWaPBY9myZcdQmMcSN2slXqAzQdl9wLmlJketoFX6UdyYPA3qiCCtCR3C6B2l3zh-qZDVFd3heK1z-kCdo80Xa-pqYq9Wr0BqXpyR0LXIIcij6dRG2dFHpS2OAlO2dEyLUcQ0XCHd0Hi1ICheQJdBEmi8Fdjc-a4Ek5k6dAiu37J3tuSk7tUr0Swa4_F3-ImeicvwK_t5fVyfYjwKadXtRcFlWprcdjVwAubxcID9hirUzTGPc_WbUaheabnyYVgACZRVio7dLwbitaUUfLin_za0CW5RhJpIH8jgBFlG9yVOQhkynKAywvR0lmc5z-ASWYBwDsuFziJvnvJM_pu0bMdXjSOk77N9hSr8Z0Htn2ArPo0fsQmgrDtB3kXgLsyaga64fAYIEr5zqU931jl_z8tUCOiUI7zC7B6JmJ98cvgzJlgwYapiWEJI_lsxfjUsgUCMan-tYSEsFKpQwmdIpVMQUiazDPDc8DRpSS_29dcUpHUjHBzPkYzkVfDSXfhQgJCJYvY9U2IGOdM6Xx3eBFnKSJFxynZoZPTm1VBcHTxJUCgMKBHKgzBSE6XLrC112fJOqYX8EKAYTNKvYP0pn9S0m8-mRCa_CZvAUuuS-kGS4RlDh1FOUnVVA55nILkQ-x9IEmTjqnVtqad3ahYSOA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0c2eb5cfa4.mp4?token=P59smr9Cs7U0WliK3MAhTWaPBY9myZcdQmMcSN2slXqAzQdl9wLmlJketoFX6UdyYPA3qiCCtCR3C6B2l3zh-qZDVFd3heK1z-kCdo80Xa-pqYq9Wr0BqXpyR0LXIIcij6dRG2dFHpS2OAlO2dEyLUcQ0XCHd0Hi1ICheQJdBEmi8Fdjc-a4Ek5k6dAiu37J3tuSk7tUr0Swa4_F3-ImeicvwK_t5fVyfYjwKadXtRcFlWprcdjVwAubxcID9hirUzTGPc_WbUaheabnyYVgACZRVio7dLwbitaUUfLin_za0CW5RhJpIH8jgBFlG9yVOQhkynKAywvR0lmc5z-ASWYBwDsuFziJvnvJM_pu0bMdXjSOk77N9hSr8Z0Htn2ArPo0fsQmgrDtB3kXgLsyaga64fAYIEr5zqU931jl_z8tUCOiUI7zC7B6JmJ98cvgzJlgwYapiWEJI_lsxfjUsgUCMan-tYSEsFKpQwmdIpVMQUiazDPDc8DRpSS_29dcUpHUjHBzPkYzkVfDSXfhQgJCJYvY9U2IGOdM6Xx3eBFnKSJFxynZoZPTm1VBcHTxJUCgMKBHKgzBSE6XLrC112fJOqYX8EKAYTNKvYP0pn9S0m8-mRCa_CZvAUuuS-kGS4RlDh1FOUnVVA55nILkQ-x9IEmTjqnVtqad3ahYSOA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ارتفاع عدد الشهداء إلى ٧ من لواء ٣٠</div>
<div class="tg-footer">👁️ 7.44K · <a href="https://t.me/naya_foriraq/86027" target="_blank">📅 05:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86026">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">ضربة جوية على محافظة ديالى معسكر اشرف</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/86026" target="_blank">📅 04:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86025">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">الحرس الثوري:
ردًا على الأعمال العدوانية للجيش الأمريكي الذي يقتل الأطفال، استهدف مقاتلو قوات الجوفضاء التابعة لحرس الثورة الإسلامية، قبل ساعات، قاعدة جوية ومركز قيادة مركزي للجيش الأمريكي في الأردن بعدة صواريخ باليستية.
طالما استمرت التهديدات ضد الجمهورية الإسلامية الإيرانية، واستمرت الأعمال غير القانونية والشريرة التي تقوم بها القوات الأمريكية ضد مصالحنا، فإن المقاومة ستستمر. يجب أن تتوقف التهديدات التي يطلقها المسؤولون الأمريكيون والتدخلات غير القانونية ضد مصالحنا.</div>
<div class="tg-footer">👁️ 7.77K · <a href="https://t.me/naya_foriraq/86025" target="_blank">📅 04:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86024">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">دوي انفجار مجهول جنوب بغداد</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/86024" target="_blank">📅 04:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86023">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">خمسة شهداء من لواء ٣٠ حشد شعبي في سهل نينوى كحصيلة اولية</div>
<div class="tg-footer">👁️ 9.11K · <a href="https://t.me/naya_foriraq/86023" target="_blank">📅 04:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86021">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انفجارات تهز محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 9.45K · <a href="https://t.me/naya_foriraq/86021" target="_blank">📅 04:50 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86020">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c8dbf9f9a3.mp4?token=CyNU6K9wknJWkJD8sdp7CAoWBbQT1WJds3TJabrSl1kHy9QEQT_dxcFYcWsqwUZ1s8MnpIYWcCBGk-mm-9uBT82_tDI84-94RV-C1EmH0wOLBPBt8dH0DIdqqgbE1-KLDL_xZ6E1TGdjIxjNYr0EHRYquNng-5ocx2_csxSwXq3t0OOqAf5GWXchhDTNcE2lNx7FbR6T4-Czzpb_fQLNj8ud4mwerNBP5S4i2nyWnbNMinTkG-uFMED5Sz4TaIJjaTg6ExJS22uhvwr-K_-5eWXV2T8yi8avR7tTaghE2EGJgU1QE3L3NSnP2EVDlEiA2y3RvzOHmcAZ_q4ioX7REA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c8dbf9f9a3.mp4?token=CyNU6K9wknJWkJD8sdp7CAoWBbQT1WJds3TJabrSl1kHy9QEQT_dxcFYcWsqwUZ1s8MnpIYWcCBGk-mm-9uBT82_tDI84-94RV-C1EmH0wOLBPBt8dH0DIdqqgbE1-KLDL_xZ6E1TGdjIxjNYr0EHRYquNng-5ocx2_csxSwXq3t0OOqAf5GWXchhDTNcE2lNx7FbR6T4-Czzpb_fQLNj8ud4mwerNBP5S4i2nyWnbNMinTkG-uFMED5Sz4TaIJjaTg6ExJS22uhvwr-K_-5eWXV2T8yi8avR7tTaghE2EGJgU1QE3L3NSnP2EVDlEiA2y3RvzOHmcAZ_q4ioX7REA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">لازالت النيران واعمدة الدخان ترتفع من مقر اللواء 30 جراء عدوان أمريكي سعودي.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/86020" target="_blank">📅 04:46 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86019">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">قصف على مدينة امرلي</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/86019" target="_blank">📅 04:45 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86018">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">قصف على مدينة امرلي</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/naya_foriraq/86018" target="_blank">📅 04:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86017">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nAcdIr4ykqorA9u6rul0cSC3sX8EX2b0JGl32LE6FjXemZI999if_JWdvx0tMGlpP9hxviR0tYta4CDrvdwIQC72Lu0PdKjDY9rrMDVM01HxlK8Jc7pXpiKkjDxxijqC4O1gzmo3KG5FISRZFBE-uyTsDEw_lmg83TTCUj0ziK0aI6WaB9xkILSZNSgeRQyId-_f7CZmsgTsffBb8yBwgFdxktIAerGMvEMtftMxOPXge256BeTS1rB9CIyRU-6zn0T3k1dxb3nCYfor5O6riokAsQ9YWUzB0Ad5SSIGp-Q8zBizROcp38j6AGEXvFKr4YH8zaL3bCfoH1a-PHBhcA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">من العدوان الغاشم الغادر الأمريكي السعودي على مقر اللواء 30 في محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86017" target="_blank">📅 04:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86016">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86016" target="_blank">📅 04:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86015">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86015" target="_blank">📅 04:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86014">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">هجوم على محافظة كركوك قضاء الدبس</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/86014" target="_blank">📅 04:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86013">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8ae5f7a62f.mp4?token=oqQc4HHhGklndf9OGHY1f2kgzSZn2oZM80iyJgzGcxBoTYWpQo9NeU9ndSekfce7QCRpdiW0VRBqBoooWLuRL8BKAmlXOctIoMKPYdFFObTe9KJUzhCKOUyHwI8Vz2l4msEDhZ54kCtRdPHLU_3YrQcylm5TI0LyilbnJgD6YAHwCBmbJfxB-7BI0WdiyGo4rxXrIg96jjxEV6wMc_QmZyGtVkAcZahoEz8vZBcUYCTOn8Xz86ge2EY1UAYqclx5jzYExTHHakY9Si_lMprlHlHxgbcvnvNcknjikiq5iIkJtiG4sgYL8NNoZ4sTMRlX0X5-blcHyZii7LrCtOEhAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8ae5f7a62f.mp4?token=oqQc4HHhGklndf9OGHY1f2kgzSZn2oZM80iyJgzGcxBoTYWpQo9NeU9ndSekfce7QCRpdiW0VRBqBoooWLuRL8BKAmlXOctIoMKPYdFFObTe9KJUzhCKOUyHwI8Vz2l4msEDhZ54kCtRdPHLU_3YrQcylm5TI0LyilbnJgD6YAHwCBmbJfxB-7BI0WdiyGo4rxXrIg96jjxEV6wMc_QmZyGtVkAcZahoEz8vZBcUYCTOn8Xz86ge2EY1UAYqclx5jzYExTHHakY9Si_lMprlHlHxgbcvnvNcknjikiq5iIkJtiG4sgYL8NNoZ4sTMRlX0X5-blcHyZii7LrCtOEhAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ستة ضربات طالت مقر لواء ٣٠ حشد الشبك تحديدا الفوج الرابع فوج شيخ حسن</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86013" target="_blank">📅 04:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86012">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">من العدوان الأمريكي السعودي الغاشم على مقر اللواء 30 بمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86012" target="_blank">📅 04:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86011">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">قصف أمريكي على أطراف محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86011" target="_blank">📅 04:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86010">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/511223b4c5.mp4?token=i98LAQxckM6CRdg6jypItUibGduqyu5FHPzHpkT6XfkHWncZvT9tkvq292ZQcJlT6WXJdFdlcf4QcDYFAm361Yw6P31PyxzytAaoQbIE2dtpxUQxzAQltW7B_V1viB8-o7yE_Fy8b6Vr0cSvywlB5stOu9cMjuDFk-Lpdeyynd004bq-i5TxYiIC0THHEtt8HcLBXW2JfJV5u_JQjUhQ_sXVTP3KSciBvepfZW7h7cfK8Xu9zhyEohbBkM8jkHQTUzYL6EeEFdHwdw6zH-zYF-gsTdqbCy1RrSU-VhXWISvXDI902ufFwi0v8HVFQ_NopWRFCDJpaCqNw7ZpnK9fwg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/511223b4c5.mp4?token=i98LAQxckM6CRdg6jypItUibGduqyu5FHPzHpkT6XfkHWncZvT9tkvq292ZQcJlT6WXJdFdlcf4QcDYFAm361Yw6P31PyxzytAaoQbIE2dtpxUQxzAQltW7B_V1viB8-o7yE_Fy8b6Vr0cSvywlB5stOu9cMjuDFk-Lpdeyynd004bq-i5TxYiIC0THHEtt8HcLBXW2JfJV5u_JQjUhQ_sXVTP3KSciBvepfZW7h7cfK8Xu9zhyEohbBkM8jkHQTUzYL6EeEFdHwdw6zH-zYF-gsTdqbCy1RrSU-VhXWISvXDI902ufFwi0v8HVFQ_NopWRFCDJpaCqNw7ZpnK9fwg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من العدوان الأمريكي السعودي الغاشم على مقر اللواء 30 بمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/86010" target="_blank">📅 04:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86009">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">نشاط لطيران سعودي في سماء مدينة أمرلي</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86009" target="_blank">📅 04:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86008">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">ضربة جوية على منطقة الزاب شمالي العراق</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86008" target="_blank">📅 04:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86007">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">Audio</div>
  <div class="tg-doc-extra"></div>
</div>
<a href="https://t.me/naya_foriraq/86007" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">.
♦️
اين ما حلِتْ امريكا حل الخراب
🎙
وَدَّ الَّذِينَ كَفَرُوا لَوْ تَغْفُلُونَ عَنْ أَسْلِحَتِكُمْ وَأَمْتِعَتِكُمْ فَيَمِيلُونَ عَلَيْكُم مَّيْلَةً وَاحِدَةً</div>
<div class="tg-footer">👁️ 12.4K · <a href="https://t.me/naya_foriraq/86007" target="_blank">📅 04:23 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86005">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">وزارة الدفاع السعودية:  وانطلاقاً من حق الدفاع عن النفس الذي يكفله القانون الدولي وفق المادة (٥١) من ميثاق الأمم المتحدة، قامت القوات المسلحة السعودية بالتنسيق مع القيادة المركزية الوسطى الأمريكية هذا اليوم الأربعاء (١٥ صفر ١٤٤٨هـ) الموافق (٢٩ يوليو ٢٠٢٦م)…</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86005" target="_blank">📅 04:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86004">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1516c51ba1.mp4?token=p55_lz-OfSopVYnooHU9_jBxucjJ5joz9uTzIgtrRjDzQyPmDCDWxKpL8n-bX60XDV27q-tS9vrwPKIbqCvbuKs_EJ7pZH6oEA3177wJIOgqehCVm3PJx-vpPcSMd2szbeJYLj5TX2I8dPKz1zGgMtTYAKHa8THrc-d46uVNUBO3A-0uLkA_ll1Y3rAQjoph7vq2hgUsQ82ClL7Wz-CBl05PZV8qz-CAGPHO5oEEkZ1DoVMPAceE6VoMPBk4PBJnsqde9yxCJwm-0dm7QErplStK6K7qdBtmvBF_f1ipwmiCzbx-bn24cAN9YBSkySr8yv0oGPhtbBauHehL8O3J4g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1516c51ba1.mp4?token=p55_lz-OfSopVYnooHU9_jBxucjJ5joz9uTzIgtrRjDzQyPmDCDWxKpL8n-bX60XDV27q-tS9vrwPKIbqCvbuKs_EJ7pZH6oEA3177wJIOgqehCVm3PJx-vpPcSMd2szbeJYLj5TX2I8dPKz1zGgMtTYAKHa8THrc-d46uVNUBO3A-0uLkA_ll1Y3rAQjoph7vq2hgUsQ82ClL7Wz-CBl05PZV8qz-CAGPHO5oEEkZ1DoVMPAceE6VoMPBk4PBJnsqde9yxCJwm-0dm7QErplStK6K7qdBtmvBF_f1ipwmiCzbx-bn24cAN9YBSkySr8yv0oGPhtbBauHehL8O3J4g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ضربة ثانية الان على واسط</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/86004" target="_blank">📅 04:22 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86003">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ad81b28f84.mp4?token=BTiLfJzjSkSxpUWL_PStg6XRj05-mKgDwhSkMrHRnnr_7e0PGLlRUrvn9QGuXlBrtOf7UGOKxSIqbgHyD8DnChh37H3OGsHjPItvAZF99TUGQHVD23PvDoEtTAHVFlkfC1nqID2_sajmLURaqCpk8UPDPMkp5br3hnqR8TqHP8vGptCu_kV99vQfDGo-fuD4edxf0h89wRmUQCb1NWeZ6DEbd6D-Rt6Lzl7x4DEfKEaCVD4ORlY-9FIzvAMWOwwLpV7IsAU6wT97ey2ciXy1O6ihSQop4H9_rP8PNOpwc7ofmSTv8sFhf7oCQEl3WGPlupWcLyLpe1XUrLlCC85Giw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ad81b28f84.mp4?token=BTiLfJzjSkSxpUWL_PStg6XRj05-mKgDwhSkMrHRnnr_7e0PGLlRUrvn9QGuXlBrtOf7UGOKxSIqbgHyD8DnChh37H3OGsHjPItvAZF99TUGQHVD23PvDoEtTAHVFlkfC1nqID2_sajmLURaqCpk8UPDPMkp5br3hnqR8TqHP8vGptCu_kV99vQfDGo-fuD4edxf0h89wRmUQCb1NWeZ6DEbd6D-Rt6Lzl7x4DEfKEaCVD4ORlY-9FIzvAMWOwwLpV7IsAU6wT97ey2ciXy1O6ihSQop4H9_rP8PNOpwc7ofmSTv8sFhf7oCQEl3WGPlupWcLyLpe1XUrLlCC85Giw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اشتعال النيران في الأماكن التي طالها العدوان السعودي الأمريكي بمحافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/86003" target="_blank">📅 04:18 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86002">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/93ac537cf7.mp4?token=rpYK_IeP00z-6kxxzf1CD2sCFgHfyS5_q9gjz9lwdZHVg12I3QkFZGVRzTu19q48EJ0Y_9AQt4y7CqriN2L1cS-WkayYvCuMAHmuiPXYaNIgAKJlYJSQls3ldLMHrwCGkaZoua-oKH3E9lCZCLIfrWG-5lgN-lvVHbxrn7vDf1u87Br-1Mjbp8mubYKkrqFXp78cg6qjaJIMf42_9IOL7q_r_Glo5wXnOBsVg1DsimefC922qy3bonqa0XD1CCVyNeDcYtzwlUoF0bJxpWaK6rdvItTW_f1WeX5OhOt7_aTxnYrNTpvIn05Dl3ioratCZwej8GrP7pWLWlXFGy8RIw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/93ac537cf7.mp4?token=rpYK_IeP00z-6kxxzf1CD2sCFgHfyS5_q9gjz9lwdZHVg12I3QkFZGVRzTu19q48EJ0Y_9AQt4y7CqriN2L1cS-WkayYvCuMAHmuiPXYaNIgAKJlYJSQls3ldLMHrwCGkaZoua-oKH3E9lCZCLIfrWG-5lgN-lvVHbxrn7vDf1u87Br-1Mjbp8mubYKkrqFXp78cg6qjaJIMf42_9IOL7q_r_Glo5wXnOBsVg1DsimefC922qy3bonqa0XD1CCVyNeDcYtzwlUoF0bJxpWaK6rdvItTW_f1WeX5OhOt7_aTxnYrNTpvIn05Dl3ioratCZwej8GrP7pWLWlXFGy8RIw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">عدوان أمريكي سعودي غاشم على محافظة نينوى شمالي العراق واعمدة الدخان تتصاعد</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/naya_foriraq/86002" target="_blank">📅 04:17 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86001">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d2fa717bab.mp4?token=tmeAaA5VTRF9avBmUn6oEyrfJTwJN4MJqYQadH_xgkW19hRA9fvh_IcvROHEKL4a5_ndicEh6i3RfunD5_BnYBa-Sm2oO-7VZ7YHcp5oNUHwV9i63c9OKC92lFB1S1GKhV2To1w8Ci-rtt5vNBzCT9znFvsxsxb1Dp8nL-m_lvUDGLvdHKj6REfD0nkGaCMD7OLJqR5Pl7ZLXaJeo_S9l4FfdRVE03YuEf1K3UoAi4bZ7s6W2TI3-aeMj76bsZizQJ90fettAf5QVIStt5P0MkhCebLNrrxjOMi5lHEeQoXKPGqAbwUNnXmR4VQOuSUpbbZ3bEz-S8B7ICHf7svbBg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d2fa717bab.mp4?token=tmeAaA5VTRF9avBmUn6oEyrfJTwJN4MJqYQadH_xgkW19hRA9fvh_IcvROHEKL4a5_ndicEh6i3RfunD5_BnYBa-Sm2oO-7VZ7YHcp5oNUHwV9i63c9OKC92lFB1S1GKhV2To1w8Ci-rtt5vNBzCT9znFvsxsxb1Dp8nL-m_lvUDGLvdHKj6REfD0nkGaCMD7OLJqR5Pl7ZLXaJeo_S9l4FfdRVE03YuEf1K3UoAi4bZ7s6W2TI3-aeMj76bsZizQJ90fettAf5QVIStt5P0MkhCebLNrrxjOMi5lHEeQoXKPGqAbwUNnXmR4VQOuSUpbbZ3bEz-S8B7ICHf7svbBg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان في محافظة نينوى</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/86001" target="_blank">📅 04:11 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-86000">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">انفجارات تهز محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/86000" target="_blank">📅 04:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85999">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">قصف أمريكي على أطراف محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/85999" target="_blank">📅 04:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85998">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">قصف أمريكي على أطراف محافظة كربلاء المقدسة</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85998" target="_blank">📅 04:07 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85997">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lcNKz6oSN-KaUgwLKIhD8Qtbs4dOoSK_EtocCFwVKY-XA3bQ6N6ktrLCCjlEaiaFL8Nn_ljO4rYm7UWCXKzzT9fWPx7Z05v4oj770rs-pn4cZapAgDsn9sPv7FL9RApcv69XHUQ6JDuuhhtHgBscF6e1Wos2Kq2Yc3A5wgbaLUvd542d10y22QSZ4r9RptcnrUW3VUvMy24RRq4KwLVAuBUD-2szNX0uABQxI8vaqvkn6R96niFS53ZfdwC1kLDg7AdEAVCX1y7joSiCB6OifAUmZJoRekNmIu8Hsaw33m-nWsDYblvKdD60f4W4CF1ZLoYmCmKj54Zo_xZuicNG_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجارات تهز محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85997" target="_blank">📅 04:06 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85996">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">انفجارات تهز محافظة نينوى شمالي العراق</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85996" target="_blank">📅 03:58 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85995">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">وزارة الدفاع السعودية:
وانطلاقاً من حق الدفاع عن النفس الذي يكفله القانون الدولي وفق المادة (٥١) من ميثاق الأمم المتحدة، قامت القوات المسلحة السعودية بالتنسيق مع القيادة المركزية الوسطى الأمريكية هذا اليوم الأربعاء (١٥ صفر ١٤٤٨هـ) الموافق (٢٩ يوليو ٢٠٢٦م) بشن ضربات نوعية محددة ضد أهداف تابعة لتلك الميليشيات المتواجدة على أراضي جمهورية العراق والمرتبطة بالاستهدافات على المنشآت البترولية في المملكة.
‏وتؤكد المملكة على أنها لا تسعى إلى التصعيد إلا أنها سترد على أي عدوان تتعرض له.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85995" target="_blank">📅 03:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85994">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85994" target="_blank">📅 03:55 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85993">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/105f3b9a10.mp4?token=dhUAS3n8cIlZvEOSLN8RZ7j8Oz_fpEouLJSC4lESyMGyGhL_ahJvY7G4JdEOoxhAtoarSXYUqmeQkIIhKzuVTPczION0p1VgedsyU74OMYNPNjtiK4cL5DjEtEgyB8LtO2XlUqnR-FUc5ED0AyxBAdm_RC1sCuZyJFQVPHOjy5cSSbVo_8kTHt8HMygtpKk4ARVw5D0v8XYmE1OQMPxNWvBNt0jgwUZVpcv94cQiPUM1SthW3iHx4-EBG8nt1iOuJN2GnMoWnFGQjUCG_YWRU5tSjoVK3Cke1Ukfx3KH8KsYZkKL_uwmlYOMkrDWi-I2ERjzRn0BoSKIl1ydMazs2g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/105f3b9a10.mp4?token=dhUAS3n8cIlZvEOSLN8RZ7j8Oz_fpEouLJSC4lESyMGyGhL_ahJvY7G4JdEOoxhAtoarSXYUqmeQkIIhKzuVTPczION0p1VgedsyU74OMYNPNjtiK4cL5DjEtEgyB8LtO2XlUqnR-FUc5ED0AyxBAdm_RC1sCuZyJFQVPHOjy5cSSbVo_8kTHt8HMygtpKk4ARVw5D0v8XYmE1OQMPxNWvBNt0jgwUZVpcv94cQiPUM1SthW3iHx4-EBG8nt1iOuJN2GnMoWnFGQjUCG_YWRU5tSjoVK3Cke1Ukfx3KH8KsYZkKL_uwmlYOMkrDWi-I2ERjzRn0BoSKIl1ydMazs2g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الجيش الامريكي:  نفّذت القيادة المركزية الأمريكية والقوات المسلحة السعودية ضربات دقيقة في العراق، في 28 يوليو/تموز، ضدّ إرهابيين موالين لإيران، كان الحرس الثوري الإسلامي قد وجّههم لمهاجمة القوات الأمريكية والبنية التحتية للطاقة السعودية.  وقالت طائرات مقاتلة…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/85993" target="_blank">📅 03:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85992">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">العراق يتعرض لعدوان عسكري من السعودية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/85992" target="_blank">📅 03:54 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85991">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">الجيش الامريكي:  نفّذت القيادة المركزية الأمريكية والقوات المسلحة السعودية ضربات دقيقة في العراق، في 28 يوليو/تموز، ضدّ إرهابيين موالين لإيران، كان الحرس الثوري الإسلامي قد وجّههم لمهاجمة القوات الأمريكية والبنية التحتية للطاقة السعودية.  وقالت طائرات مقاتلة…</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85991" target="_blank">📅 03:53 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85990">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">الجيش الامريكي:  نفّذت القيادة المركزية الأمريكية والقوات المسلحة السعودية ضربات دقيقة في العراق، في 28 يوليو/تموز، ضدّ إرهابيين موالين لإيران، كان الحرس الثوري الإسلامي قد وجّههم لمهاجمة القوات الأمريكية والبنية التحتية للطاقة السعودية.  وقالت طائرات مقاتلة…</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85990" target="_blank">📅 03:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85989">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">الجيش الامريكي:
نفّذت القيادة المركزية الأمريكية والقوات المسلحة السعودية ضربات دقيقة في العراق، في 28 يوليو/تموز، ضدّ إرهابيين موالين لإيران، كان الحرس الثوري الإسلامي قد وجّههم لمهاجمة القوات الأمريكية والبنية التحتية للطاقة السعودية.
وقالت طائرات مقاتلة أمريكية وسعودية على مواقع لوجستية وأسلحة إرهابية متعددة في شرق العراق، ردًّا قويًا على أكثر من 30 هجومًا جويًا بطائرات مسيّرة، نفّذها الحرس الثوري الإسلامي خلال الـ 72 ساعة الماضية.
ولم تُكلل هذه الهجمات غير المبررة ضدّ القوات الأمريكية بالنجاح.
ومن فبراير/شباط إلى أبريل/نيسان 2026، نُفّذ أكثر من 600 محاولة هجوم على مواطنين ومنشآت أمريكية من قِبل ميليشيات إرهابية موالية لإيران في العراق.
ويجب على الحرس الثوري الإسلامي ووكلائه الإرهابيين وقف هذه الهجمات لتجنّب المزيد من الرد العسكري الأمريكي.</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85989" target="_blank">📅 03:51 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85988">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85988" target="_blank">📅 03:41 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85987">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b308800350.mp4?token=cmNj7EePDTmrX1Suj2kyD6eJWNNtJtdrBZFT8qhMyxnORnjK0dr8H7V9Foyko2vF2WhTbOVLK3DM2pBJmxuLSm4NkPDeem6rymClYEy4w9rELf-zLcBD9sDMXtQkCfaOszQuEEkZ5I8wiQldIUzAMKckbC9Y56CVoKVvAoCIVDTGENsp_VFvfag91OxmnkS_B1pthZn7FxOnP5PwtxU7lDNKiVc3gzq33pPdT2MMZMdBWBVZZNYe-dF4DBBFQ1NGs-BVYMzYdfSuyVPfCzDUhGtpRKvtkVHzvuIUf1-0WqrJhSIYfVkIatfISg9cbUT8lpjmwD9tZde_ggB-C-Y_fQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b308800350.mp4?token=cmNj7EePDTmrX1Suj2kyD6eJWNNtJtdrBZFT8qhMyxnORnjK0dr8H7V9Foyko2vF2WhTbOVLK3DM2pBJmxuLSm4NkPDeem6rymClYEy4w9rELf-zLcBD9sDMXtQkCfaOszQuEEkZ5I8wiQldIUzAMKckbC9Y56CVoKVvAoCIVDTGENsp_VFvfag91OxmnkS_B1pthZn7FxOnP5PwtxU7lDNKiVc3gzq33pPdT2MMZMdBWBVZZNYe-dF4DBBFQ1NGs-BVYMzYdfSuyVPfCzDUhGtpRKvtkVHzvuIUf1-0WqrJhSIYfVkIatfISg9cbUT8lpjmwD9tZde_ggB-C-Y_fQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85987" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85986">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85986" target="_blank">📅 03:39 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85985">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85985" target="_blank">📅 03:38 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85984">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 11.6K · <a href="https://t.me/naya_foriraq/85984" target="_blank">📅 03:37 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85983">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fa7283cb13.mp4?token=NRjlL8ZrSZPB_pYxC50f6rDnq5uMwyy05S4qxYRyE-zd_WKmn5swI-jHZ-_Ykte5BYgy9heJ8Mr9goITnk1qZitr4Ixdc7syEiXMjz_72bzTAa6JwDuAKsw69aab6Y-v8nO4nq_Z11ALrM7kBlxVdEEPwsXjB2FpTZ9pVi3FXAmaaI-gUAZwoIXYviGIIKap-sbWgPR6eXZQBueUf31QRZbMNkzE06RxQ-vDcibvYJLGRn6ndnITngW8pcY4NK9IsNjTJy9VObNw8sPbNmcPKwj9iQAoYn4LdDjnToAV-tJKSpxq1OyqvvxOdWnA84oiHc6obvAoU9sSlBnozVxaZg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fa7283cb13.mp4?token=NRjlL8ZrSZPB_pYxC50f6rDnq5uMwyy05S4qxYRyE-zd_WKmn5swI-jHZ-_Ykte5BYgy9heJ8Mr9goITnk1qZitr4Ixdc7syEiXMjz_72bzTAa6JwDuAKsw69aab6Y-v8nO4nq_Z11ALrM7kBlxVdEEPwsXjB2FpTZ9pVi3FXAmaaI-gUAZwoIXYviGIIKap-sbWgPR6eXZQBueUf31QRZbMNkzE06RxQ-vDcibvYJLGRn6ndnITngW8pcY4NK9IsNjTJy9VObNw8sPbNmcPKwj9iQAoYn4LdDjnToAV-tJKSpxq1OyqvvxOdWnA84oiHc6obvAoU9sSlBnozVxaZg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الإنفجارات جراء انفجار كدس عتاد في منطقة الهارثة بمحافظة البصرة جنوبي العراق</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85983" target="_blank">📅 03:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85982">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85982" target="_blank">📅 03:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85981">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85981" target="_blank">📅 03:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85980">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">طيران حربي في سماء محافظة بابل العراقية.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85980" target="_blank">📅 03:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85979">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b0c88170f8.mp4?token=Sng-i9cA1cQrcdBvT9kljjwGXHda8tYYn7Dat0bDjPDykW1qpEJVOzMWzxVXckroqW3h4MUFSBS4xVezmnjhpWUxWEYYs5if8qqiAV9qrHU_kALMp-TeYnHRH0Yu9_vA1sbrbSihTPUSzNQAYIIo40TmlOoPmB2jQXr80JQzFM343nLEcntkVRqEe9emmr64AtByplABwKK5X8rVmdHIflIYgHph2ubTz0PsMFvZVYSw-ZP-_D-4NZoLSs-UaGkEJUtaYqHoDEIr4K2qvKjeSV1OE9uqsGg2C7920yWBfQyWI5wlaP07NZ8AVjED3oI3oUvYWVPXlmlRjgi6EBUJoA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b0c88170f8.mp4?token=Sng-i9cA1cQrcdBvT9kljjwGXHda8tYYn7Dat0bDjPDykW1qpEJVOzMWzxVXckroqW3h4MUFSBS4xVezmnjhpWUxWEYYs5if8qqiAV9qrHU_kALMp-TeYnHRH0Yu9_vA1sbrbSihTPUSzNQAYIIo40TmlOoPmB2jQXr80JQzFM343nLEcntkVRqEe9emmr64AtByplABwKK5X8rVmdHIflIYgHph2ubTz0PsMFvZVYSw-ZP-_D-4NZoLSs-UaGkEJUtaYqHoDEIr4K2qvKjeSV1OE9uqsGg2C7920yWBfQyWI5wlaP07NZ8AVjED3oI3oUvYWVPXlmlRjgi6EBUJoA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تصاعد أعمدة الدخان في قضاء الهارثة بمحافظة البصرة جنوبي العراق جراء انفجار كدس عتاد بالقرب من مقر عسكري.</div>
<div class="tg-footer">👁️ 11.3K · <a href="https://t.me/naya_foriraq/85979" target="_blank">📅 03:30 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85978">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85978" target="_blank">📅 03:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85977">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">دوي انفجارات في منطقة الصويرة بمحافظة واسط العراقية</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/85977" target="_blank">📅 03:27 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85976">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/43f9b4b140.mp4?token=jlgvG_ql_KPgjeafdic8xBCFyU8AOaPW3pzyQ_B4ErydzOb8GVU_dJuVAWyfPS15d4K4TTExw1XYxoN7sZxOoj_Q9M-FcIKIWOyOVIMSbDszP0Kipmt2yU6mR-Qxu-kr_RkN_R-2qRd3ktdjx7ei7fmhBqInul0EVV6hX--z6dZuwl70rjUc43G1RICwrO81CziA3SsgxosHwHNP4hJYaVT7nS5tT8G5EtB0et1Fw3PW5uNqCC3Y8RL5ATp7YFvYfm6SRE6z0DD6hfsSnzMm1G1MZDbAGfmXWR_1Qrwdzt2WZUTmVGUCXYH1Wqr4W-uKFD6HBxVtfdZ-V3jZD3LO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/43f9b4b140.mp4?token=jlgvG_ql_KPgjeafdic8xBCFyU8AOaPW3pzyQ_B4ErydzOb8GVU_dJuVAWyfPS15d4K4TTExw1XYxoN7sZxOoj_Q9M-FcIKIWOyOVIMSbDszP0Kipmt2yU6mR-Qxu-kr_RkN_R-2qRd3ktdjx7ei7fmhBqInul0EVV6hX--z6dZuwl70rjUc43G1RICwrO81CziA3SsgxosHwHNP4hJYaVT7nS5tT8G5EtB0et1Fw3PW5uNqCC3Y8RL5ATp7YFvYfm6SRE6z0DD6hfsSnzMm1G1MZDbAGfmXWR_1Qrwdzt2WZUTmVGUCXYH1Wqr4W-uKFD6HBxVtfdZ-V3jZD3LO7IWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">استمرار دوي الانفجارات نتيجة انفجار كدس عتاد قرب مقر عسكري جنوبي العراق</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85976" target="_blank">📅 03:15 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85975">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a3af92751.mp4?token=GBW9yIjNTQpXIs3DRWp91JDdKwMAQ5GlrDjjDzZ21hRPsY8j1yytkyogDeGEDseI0Xnv18QLvNufGAMAnAzmsbErnlVFXFMmF-dlpoA7lVhzYS9gDRNtk0a0MVz8wsiod1WDYTR-25H4KnF5Jj14lgSbwtF9M_YWVa508SnAYe8zku2yVzHBdcM75E7uiutNUl9WRGEr8HJrewOaQR0skpO817mceOi5ZlAUV28iO_MQBRdeqpDp6qVZCK5lKMYTMDLjGaN_8gW3ueCqLQeaLZw8Yajr2MOqIcGE6BthNImJjcW6vhdSQWUo6YRrIjjRWf_K6PbPrSzY_BR6x82tQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a3af92751.mp4?token=GBW9yIjNTQpXIs3DRWp91JDdKwMAQ5GlrDjjDzZ21hRPsY8j1yytkyogDeGEDseI0Xnv18QLvNufGAMAnAzmsbErnlVFXFMmF-dlpoA7lVhzYS9gDRNtk0a0MVz8wsiod1WDYTR-25H4KnF5Jj14lgSbwtF9M_YWVa508SnAYe8zku2yVzHBdcM75E7uiutNUl9WRGEr8HJrewOaQR0skpO817mceOi5ZlAUV28iO_MQBRdeqpDp6qVZCK5lKMYTMDLjGaN_8gW3ueCqLQeaLZw8Yajr2MOqIcGE6BthNImJjcW6vhdSQWUo6YRrIjjRWf_K6PbPrSzY_BR6x82tQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85975" target="_blank">📅 02:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85974">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85974" target="_blank">📅 02:52 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85973">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/557a609003.mp4?token=SVAvhVlT5ULLD4aeDO05SjNt_eMfI6NvtwvQjxOYmvSkDmbsfJYamAzW4XstHBFwplWeIHQpB-lMfHIHkd2S57GGUpEwu8sEVExxcl1WAldcHSZtvkf9VRAYExLI25W-ljCISbdtQqCZ3UItOxXjGTq9nTMdrCMrVQbXVK1fCbd8LInGfSIdy5bmU8kX6nDLhv02GCXMWo2OUbQ-Cc4KCjiVYUtMArTyPqy4oQacsGLZ0cizrpAFV9cItNpkckV-ZQhlqsFzn3PrEQ15zPCJqlDEZ8OlFfVJd8kccVZBkMA9O4V1fWoW6ap6xiwzlz6Mh5MGCHZfAAvZI1Dl7djZTA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/557a609003.mp4?token=SVAvhVlT5ULLD4aeDO05SjNt_eMfI6NvtwvQjxOYmvSkDmbsfJYamAzW4XstHBFwplWeIHQpB-lMfHIHkd2S57GGUpEwu8sEVExxcl1WAldcHSZtvkf9VRAYExLI25W-ljCISbdtQqCZ3UItOxXjGTq9nTMdrCMrVQbXVK1fCbd8LInGfSIdy5bmU8kX6nDLhv02GCXMWo2OUbQ-Cc4KCjiVYUtMArTyPqy4oQacsGLZ0cizrpAFV9cItNpkckV-ZQhlqsFzn3PrEQ15zPCJqlDEZ8OlFfVJd8kccVZBkMA9O4V1fWoW6ap6xiwzlz6Mh5MGCHZfAAvZI1Dl7djZTA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مصدر امني لنايا : انفجار كدس عتاد قرب احد المقرات العسكرية في محافظة البصرة جنوبي العراق.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85973" target="_blank">📅 02:49 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85972">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🇺🇸
‏
إدارة الطيران الفيدرالية الأمريكية:
تعليق رحلات الخطوط الجوية في جميع أنحاء الولايات المتحدة بسبب عطل في أنظمة تكنولوجيا المعلومات.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/85972" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85970">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FsUR-c24-pziFuJWCSrJAiFHMCci2TWIY1ltnfmlo0gNXvPFQNSB7VwsuOcn5M0tx-f_Xi4d7zj-6u8q-uvHW_VnEBXFHsKXcH3d45RtsDjVFw1tGgQ_2D2eVA6AfiLeHVzt1M6f4TqN0v7UmnHvtYTQzwgdy5bTqpgZ-bi4gz_pE25bazstFV18fQ55WF9rdBDK0qGEVbojvQyC2JRJ3_pxD4KRJKgZ8DbXv4hlRLMrrv4JMDAH_yxV5RA_nUgFt92pGXtIfmCKuJspSZNSJ6bzDbk6lnF6pVWQEvYJTWVDXV4_oW3sleRomb8ByfbUdPmafPi6CO1GD7-0BfhYxg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/X1ArSOlEM8n9HXhjg5nlEOCbo1K9wRTuiZtGJ8hn7D8De_ysXLnP1YDhyAsn1GrOdb_U15vKe-65FV92vPsw0arvVd1ca2o3XoPoZpbQ6fu2nvQtsXoZZdCw_D9HkDvpwxj4uW434vCBTn4XsJgCBhG4fjlJQHwFjjjL3J7XMnX7qJpDoh1FR_z6LnMANaVyO8Y0ISyQ9i8QYFgK4Jf9piOesUqrboYexpvL4rhtlYdymg3rNn0UF2xV_4B9WqaV2bkP8v76NcL4kuoSH7vWTrezGRusHvmkMFFKvqHidHZsbl3R-fNrsWx2-GAGO3xVmjN0PShdP3OEEJmhFqOjCg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات الجوية الأميركية طيران الإرضاع الجوي و طائرات النقل الثقيل تحاول قدر الإمكان تجنب المرور بالعراق وتسلك مسارات السعودية الأردن خوفا من استهدافها في سماء العراق التي شهدت البارحة سقوط مسيرتين أمريكية</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85970" target="_blank">📅 02:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85969">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RDAuPOVTgkBHfC-HkHPVpPy5IT7Yu9t-nfanZm5QlZT8upBkZsiwaCeChL1b4KnAQkaD8Ic7wBuB2KBeueRSyKPQlI52EU-2utGCJcx35vhd6bns6mkDPycCrghE_2fztvhWo4lNs6OlbZbc56UH6JtsRM30Y3haYTxLohVdmpmnUEgbkAxrVCrXOZsvRGVseJF5W0BLhym3R2g_DjCjNHFzHeEybtSSNN8C3ofrUEiXCTiPnKlXE-cEe-NvQx9w86J9p3AlxsxIl9d99uoJA4tinrLuUEytEjI4tnaZS_Pva860L891fU8a-k-vzYrHw2eYeGS7EV5Lc0oNLfbR4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">القوات الجوية الأميركية طيران الإرضاع الجوي و طائرات النقل الثقيل تحاول قدر الإمكان تجنب المرور بالعراق وتسلك مسارات السعودية الأردن خوفا من استهدافها في سماء العراق التي شهدت البارحة سقوط مسيرتين أمريكية</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85969" target="_blank">📅 02:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85968">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">انفجار عنيف في أربيل</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85968" target="_blank">📅 02:08 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85967">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">انفجار عنيف في أربيل</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/85967" target="_blank">📅 02:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85966">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">طيران حربي في سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/85966" target="_blank">📅 02:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85965">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">فقط للتنويه   وقف إطلاق النار كان من جانب امريكا وليس من جانب ايران ؛ بمعنى ايران لا تكسر الهدنة ؛ امريكا هي لوحدها قررت وقف إطلاق النار بعد ١٣ جولة ، و بسبب العوز الصاروخي والوضع الماساوي للقواعد في الكويت والبحرين والأردن وغلق باب المندب من قبل أنصار الله…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/85965" target="_blank">📅 02:02 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85964">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">طيران حربي في سماء محافظة أربيل شمالي العراق</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/85964" target="_blank">📅 01:59 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85962">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇺🇸
الجيش الامريكي:
في تمام الساعة 5:45 مساءً بتوقيت شرق الولايات المتحدة اليوم، أطلقت قوات الحرس الثوري الإسلامي عدة صواريخ باليستية من إيران في محاولة لشن هجوم مفاجئ على القوات الأمريكية المتمركزة في الشرق الأوسط. وقد تم اعتراض جميع الصواريخ الإيرانية بنجاح. ولا تزال القوات الأمريكية في حالة تأهب قصوى.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/85962" target="_blank">📅 01:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85961">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4dcd2f9593.mp4?token=ZMmhB5bNBzLMIAG-mN_TMrlP5o5rVrbYEzHlMX0IL66UuymbkxyZpoOCfxbamTo6kAvff0WGGqRmZm56_otKf0v6Hhb9YTmDOKK5uOOf7Q1OhEirtPH7VNtRQvkbv2KSPbJr0lWZ0S_cy9N98uBUWF_JzmUTuz6hX9bvJHzpPo8ucD08dobFJ_hS9OPBrRprcQbxB28uF6fZjYPN0WyZ7WaRzkvy_OyaCG0iW0ZumU5YMvCoS5D04xEaZ9uZEj1F_dlWc09zknxa_4YUT9_VcGhFMuDHaT3LvvLHmJiQMs-2HAoCzYnZfVtsYTsGj4nibJQ-kYom8tdlCHpTfPZbjA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4dcd2f9593.mp4?token=ZMmhB5bNBzLMIAG-mN_TMrlP5o5rVrbYEzHlMX0IL66UuymbkxyZpoOCfxbamTo6kAvff0WGGqRmZm56_otKf0v6Hhb9YTmDOKK5uOOf7Q1OhEirtPH7VNtRQvkbv2KSPbJr0lWZ0S_cy9N98uBUWF_JzmUTuz6hX9bvJHzpPo8ucD08dobFJ_hS9OPBrRprcQbxB28uF6fZjYPN0WyZ7WaRzkvy_OyaCG0iW0ZumU5YMvCoS5D04xEaZ9uZEj1F_dlWc09zknxa_4YUT9_VcGhFMuDHaT3LvvLHmJiQMs-2HAoCzYnZfVtsYTsGj4nibJQ-kYom8tdlCHpTfPZbjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد متداولة من سماء عَمان عقب إطلاق الصواريخ الإيرانية ومحاولات منظومة الباتريوت التصدي والاعتراض.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/85961" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85960">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZdWNh3YV0KIC37vVYjiLr_85bGQGrxHd8lRwqrcAhtmGmRLb9iKv3IGY9-gbH_SMwOd67rtxt5cs_n3RxX_dPbHIMum5NAfeSCNoPQI4KskVJeabDnF3cA_JLR6KhKPHn8RDGnBgvpge1bbdPRc9a_ITwtLehgGnm3Rky7ndf1zC2SVkQjzYZntDu7JtIf2w0KqJ2Ap9UKiI-sBYe-HY7GEVfIt79gPxvYDOI3EUygHElSbVPwtrOSQ-66QkBtlKJSYyPmai_8Jw56dig4566_cOiFBXRHB85-J1VqtbL6S3sdJYP-fZJs1Iug0hhsAuzuYoI8rt1nP2XzdP9vGqXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شركة إيلون ماسك تطلق خدمة ستارلنك في العراق ..</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85960" target="_blank">📅 01:56 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85959">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">أعلام العدو: اصابة مباشرة في قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/naya_foriraq/85959" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85958">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">أعلام العدو: اصابة مباشرة في قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85958" target="_blank">📅 01:48 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85957">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n4wkRHnjgagCloTaza642auISd17KXMG5G8C6hHGl_ocZp0yhBpJGlU0V7gV4vh9WharkEXN7OYyypkx5AkSvInigz421YVtLUMo1TpzDknQnovVwmsFsVYnL4xcfP2e2YAdwJNTJAcFPXZ04-4evQw5gJVeudJ5vZLQZqJfv4OMTZiKPLJxf4hXg1pxPHUwEAAble3qiLYsxt4hNTwAQsqdru0aeG0fKzvx9lXcP4hMIdx1FpQXz0SHkZDHJHUyA7JDEXCt1jM57KJxVK9fJtZbxbT3mzstTPpVxugJTsUZ7zsGIq9ytpf1iMdnkB2aKruEA1XLHZ3JfakQU-tOmw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/85957" target="_blank">📅 01:44 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85954">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/079a967bc2.mp4?token=RPrxvlns0Vc37M34OgmfMjmmRPEubxD8TF640CdtmJblx99uQiWc7G2TwYQ9hlI4n9aee0iXQj9ZGGGilThwOjCJPrrAKnsyE0d1Q8LR-Mk2aXDFoubKdA2796HNKfcVnVvnUsAJD9jur_LaoEBlk6HaZrrRUByk4gumnirRGOCK4nmREpfRLQ1fxUaVzzMiA5g9i4IXtiScVlcsfnnouxLG-xZUr783qjmQlGACKytMxtI-YB5nshynt7SMf-OImEpiMvsz8TmBWztw8OEN78Fq4vWygyNCT270mp3ld0POH_ENb3nEh3UeLcacr_A84TNI3_IHBmbeK4iqQ0qyeKChpW9D7EaPWuN_9xmZNv2gx6T6FSpU0YA3bO4kfNtFXxAYGwYbH-RGDuFEr4PCjtQr32bmgT3NKXezRCyOT6wkjIK3_az1mMvWDcCDCpRdqUsILe3zpBeZl21MZlXE3sTAYHZAiLweL3Ehk7BRYub6riHAH3EfvBK8Im5wJdoASOCvFYleuOe57nxJawfJpz1KhynY4_ODML9c83jxaitahom_4S9C1cxUWK0JD0-mK0mwc3fuXs1UfDsIuqdWShfrpr16aq00II1kgmcy7aF4TnU12xqO8i9cykuTab-kd1bZmLOh_LJDpg-oF4SyU_Sou-C42ul9bQ5g2NnGTDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/079a967bc2.mp4?token=RPrxvlns0Vc37M34OgmfMjmmRPEubxD8TF640CdtmJblx99uQiWc7G2TwYQ9hlI4n9aee0iXQj9ZGGGilThwOjCJPrrAKnsyE0d1Q8LR-Mk2aXDFoubKdA2796HNKfcVnVvnUsAJD9jur_LaoEBlk6HaZrrRUByk4gumnirRGOCK4nmREpfRLQ1fxUaVzzMiA5g9i4IXtiScVlcsfnnouxLG-xZUr783qjmQlGACKytMxtI-YB5nshynt7SMf-OImEpiMvsz8TmBWztw8OEN78Fq4vWygyNCT270mp3ld0POH_ENb3nEh3UeLcacr_A84TNI3_IHBmbeK4iqQ0qyeKChpW9D7EaPWuN_9xmZNv2gx6T6FSpU0YA3bO4kfNtFXxAYGwYbH-RGDuFEr4PCjtQr32bmgT3NKXezRCyOT6wkjIK3_az1mMvWDcCDCpRdqUsILe3zpBeZl21MZlXE3sTAYHZAiLweL3Ehk7BRYub6riHAH3EfvBK8Im5wJdoASOCvFYleuOe57nxJawfJpz1KhynY4_ODML9c83jxaitahom_4S9C1cxUWK0JD0-mK0mwc3fuXs1UfDsIuqdWShfrpr16aq00II1kgmcy7aF4TnU12xqO8i9cykuTab-kd1bZmLOh_LJDpg-oF4SyU_Sou-C42ul9bQ5g2NnGTDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الصواريخ الإيرانية تشعل سماء عَمان وقاعدة موفق السلطي الأمريكية تحت غضب نيران الجمهورية الإسلامية الإيرانية</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/85954" target="_blank">📅 01:43 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85953">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/85953" target="_blank">📅 01:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85952">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">فقط للتنويه
وقف إطلاق النار كان من جانب امريكا وليس من جانب ايران ؛ بمعنى ايران لا تكسر الهدنة ؛ امريكا هي لوحدها قررت وقف إطلاق النار بعد ١٣ جولة ، و بسبب العوز الصاروخي والوضع الماساوي للقواعد في الكويت والبحرين والأردن وغلق باب المندب من قبل أنصار الله في اليمن وارتفاع اسعار الوقود
سنرّكع العدو</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85952" target="_blank">📅 01:40 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85950">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/76ecc7e77f.mp4?token=ZTPsrWiZVeFPlwM1Ok4ERTxnMm3m5QqxL7i83iiPDLqt5mtdpjnx6iuG3Yvr9ZugfFRnUU80nfeAE8tD_Liq1WDDrArztEhK7R1sWiDvFtmuwpgTvN_XynRPcbpz-GYYxIezDFT9irhBiPfzJxrVt1CxSrBj3KXgTPkjKAhvkY_mz7dpNYXu6sluhvfHO9iwbffYffu0Jg2_7E9iI-Rmb_soJ9BSwOdKPkN_bDrf4A6hmBtTHPkblEHQDswa0mxkJsfUhgyDoi-IK-ic7XNM11eC1DVOZi5a5ODOr8_QUEOna1N9P3Ulyp8DSoK2hnyvQ7OrzAC0wPyrIunq2l1Hyw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/76ecc7e77f.mp4?token=ZTPsrWiZVeFPlwM1Ok4ERTxnMm3m5QqxL7i83iiPDLqt5mtdpjnx6iuG3Yvr9ZugfFRnUU80nfeAE8tD_Liq1WDDrArztEhK7R1sWiDvFtmuwpgTvN_XynRPcbpz-GYYxIezDFT9irhBiPfzJxrVt1CxSrBj3KXgTPkjKAhvkY_mz7dpNYXu6sluhvfHO9iwbffYffu0Jg2_7E9iI-Rmb_soJ9BSwOdKPkN_bDrf4A6hmBtTHPkblEHQDswa0mxkJsfUhgyDoi-IK-ic7XNM11eC1DVOZi5a5ODOr8_QUEOna1N9P3Ulyp8DSoK2hnyvQ7OrzAC0wPyrIunq2l1Hyw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">معارك صاروخية في أجواء قاعدة موفق السلطي الأمريكية بالأردن</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85950" target="_blank">📅 01:36 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85949">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/624386482d.mp4?token=MGDEB7o8OSe0Q_aa1xUEcte5IqQc7JVCKao_5GVCtzTPQHGgmWTn9hg-jNqBVivIIdKUYcq_XknLG954m-dPrFgx44Oos0wDT8kCehjxHXw6yJLo989HV1h6X3BcjJMYOuOQwAULLpNXBEh5_fzJnMP0gqw5led9RKzOWgxFxK1NQ2Seh4ZEqxOyh1E7kQBbug6aBEasxCEWUkaGkfbuPcMZMiCuIDO2-gt0Rmi0XSh_oifPZyew2qOGbs2ALTlCK-YN3cyCo4INm8B-j0HZrb68PwbeMvXG1IevNwIk3CesQpcL6gfvc5nQm5NFh6n6fO3tjMd1t3zDWMyHkwuxiw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/624386482d.mp4?token=MGDEB7o8OSe0Q_aa1xUEcte5IqQc7JVCKao_5GVCtzTPQHGgmWTn9hg-jNqBVivIIdKUYcq_XknLG954m-dPrFgx44Oos0wDT8kCehjxHXw6yJLo989HV1h6X3BcjJMYOuOQwAULLpNXBEh5_fzJnMP0gqw5led9RKzOWgxFxK1NQ2Seh4ZEqxOyh1E7kQBbug6aBEasxCEWUkaGkfbuPcMZMiCuIDO2-gt0Rmi0XSh_oifPZyew2qOGbs2ALTlCK-YN3cyCo4INm8B-j0HZrb68PwbeMvXG1IevNwIk3CesQpcL6gfvc5nQm5NFh6n6fO3tjMd1t3zDWMyHkwuxiw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">من الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/85949" target="_blank">📅 01:34 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85948">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/naya_foriraq/85948" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85947">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">من الهجوم الصاروخي الإيراني الذي طال قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 11.5K · <a href="https://t.me/naya_foriraq/85947" target="_blank">📅 01:33 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85946">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f4be504ac0.mp4?token=owCfO-HVH8T6da4Mx28GJ7f8AVqb4kOJO3RCmLwSJq06Q04sCgm963Hu9aVQP4C5dSVx2dfQmtP7J10kSworpmAg-KAcXYMs78wQwxxj4sO9VITOrvwrhjCZxwuSIrg6o-YV56TfljvqPkruNES71YF9vZHZ52Ru-s2zPKEYmhKZ6ga2GzcZVRw-CCmBRVTJ6lfvBc_PLAGNX1-igEGH24grP8Hb7AO2I2X9-tgrwfpBhFXNpsaPJ4YQ3xcU3u_ccNfkP1EPytPvmuTN1Ial8BRuS1WMlh9fmvYnGhLFsCAuZOZplPcG4ahcvSOpLHTP9vTUu34ZpX83wh2sImUJBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f4be504ac0.mp4?token=owCfO-HVH8T6da4Mx28GJ7f8AVqb4kOJO3RCmLwSJq06Q04sCgm963Hu9aVQP4C5dSVx2dfQmtP7J10kSworpmAg-KAcXYMs78wQwxxj4sO9VITOrvwrhjCZxwuSIrg6o-YV56TfljvqPkruNES71YF9vZHZ52Ru-s2zPKEYmhKZ6ga2GzcZVRw-CCmBRVTJ6lfvBc_PLAGNX1-igEGH24grP8Hb7AO2I2X9-tgrwfpBhFXNpsaPJ4YQ3xcU3u_ccNfkP1EPytPvmuTN1Ial8BRuS1WMlh9fmvYnGhLFsCAuZOZplPcG4ahcvSOpLHTP9vTUu34ZpX83wh2sImUJBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/naya_foriraq/85946" target="_blank">📅 01:32 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85945">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ed59912d11.mp4?token=Po9RDDefv5nw5HUV58wguyZ7RkssdXDxl2alLRhxFjmbi5rpGaZeO70i6QVJl9Ib5xjYJckp-nKTTlX0SV4RMI57fXxED6_9OKmSp07yXs4jiq4rSbDi53-dXkch90GbcldeyMfPzxgg4bIOk6ol5UYYQFKk5B9Q3AkAQU3W7JCoeMDHzWec001BHbRNkfbTPwrUndJ9FMxTerbMQB6_oWD4kf9iDQFwepAHLU0ve8fCY235Iue-1l5-0M-SyIvzRpu34AGsZ3vu5I0Zi9Ta4TBBGZUopSpf5JWYxtbmlkmNY3jkJUvOeI60Xq3ObwidQTiL-Azqxj9eF1fQ1U6C9g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ed59912d11.mp4?token=Po9RDDefv5nw5HUV58wguyZ7RkssdXDxl2alLRhxFjmbi5rpGaZeO70i6QVJl9Ib5xjYJckp-nKTTlX0SV4RMI57fXxED6_9OKmSp07yXs4jiq4rSbDi53-dXkch90GbcldeyMfPzxgg4bIOk6ol5UYYQFKk5B9Q3AkAQU3W7JCoeMDHzWec001BHbRNkfbTPwrUndJ9FMxTerbMQB6_oWD4kf9iDQFwepAHLU0ve8fCY235Iue-1l5-0M-SyIvzRpu34AGsZ3vu5I0Zi9Ta4TBBGZUopSpf5JWYxtbmlkmNY3jkJUvOeI60Xq3ObwidQTiL-Azqxj9eF1fQ1U6C9g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الرشقة الصاروخية التي أطلقت من إيران نحو قاعدة موفق السلطي الأمريكية في الأردن</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85945" target="_blank">📅 01:31 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85944">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/71d615425b.mp4?token=wCaKJyFmiyn2CJ_eCg-9IPKspE8LOF1uSSW06K5SSyAcN0epCkRe-yKQxyLxQINCBxk1vi1sU0rUFB30mGPKe2r9GxOJjaSI59OhEwp-y-4F_mVTNxHbWCpHDX_UAM-ywh6vXq_tFKtd5yxW2S1KtHgDt6W9Zs3WqcrDwM0Gw3ZX0wjeq3rudI70RvTarnMdiFdzOaoWWbz1YitC7O4fzvd_bCOpez3lXcidW2uKIvH1iUjOb_r27agBcHty5mMSVOO-s3anrPpZQsksGmaAmAPc0m61rxqDhvTMWTqRljJtxV-A5Nb8XowKZQhVtkTUte38eSrpHN0PZGDtNFsnpw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/71d615425b.mp4?token=wCaKJyFmiyn2CJ_eCg-9IPKspE8LOF1uSSW06K5SSyAcN0epCkRe-yKQxyLxQINCBxk1vi1sU0rUFB30mGPKe2r9GxOJjaSI59OhEwp-y-4F_mVTNxHbWCpHDX_UAM-ywh6vXq_tFKtd5yxW2S1KtHgDt6W9Zs3WqcrDwM0Gw3ZX0wjeq3rudI70RvTarnMdiFdzOaoWWbz1YitC7O4fzvd_bCOpez3lXcidW2uKIvH1iUjOb_r27agBcHty5mMSVOO-s3anrPpZQsksGmaAmAPc0m61rxqDhvTMWTqRljJtxV-A5Nb8XowKZQhVtkTUte38eSrpHN0PZGDtNFsnpw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة وسط تفعيل منظومة الباتريوت بسماء الأردن</div>
<div class="tg-footer">👁️ 11.4K · <a href="https://t.me/naya_foriraq/85944" target="_blank">📅 01:29 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85943">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/123326eeb8.mp4?token=RGPOUnep_jIqpTJlCR_eeii9m92sFe81U61Gzz-WyMrMJMPmz-1D_VsDsawhrUqkhmYrLCICyalqZ0bfMX21o-aaOEEu-Z5KiCtYkJYIt9sh4yv_2HUDDZeKYDP7UGSQgEriVZvsgIbssSmv3Ga8HvbuDBaMH6vSuHYSqJBVbxhKhO5Z3gxtWnjxmN23FiZVovIb1P9mUkSmVeuVI1FTgFDJPAD9Znad7iuf7B_7m3ftLwRwsnXnLpFUksHO970rZGqg4ad4bnDldYskCZJJr2K8H42ZkLd6LEAIpQHnLYuEtAnhZ2Tr9XneOCLGzHsjQ3ezW4I6nnsAJM0yo1ma7g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/123326eeb8.mp4?token=RGPOUnep_jIqpTJlCR_eeii9m92sFe81U61Gzz-WyMrMJMPmz-1D_VsDsawhrUqkhmYrLCICyalqZ0bfMX21o-aaOEEu-Z5KiCtYkJYIt9sh4yv_2HUDDZeKYDP7UGSQgEriVZvsgIbssSmv3Ga8HvbuDBaMH6vSuHYSqJBVbxhKhO5Z3gxtWnjxmN23FiZVovIb1P9mUkSmVeuVI1FTgFDJPAD9Znad7iuf7B_7m3ftLwRwsnXnLpFUksHO970rZGqg4ad4bnDldYskCZJJr2K8H42ZkLd6LEAIpQHnLYuEtAnhZ2Tr9XneOCLGzHsjQ3ezW4I6nnsAJM0yo1ma7g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات الدفاع الجوي الأمريكي بصد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 10.5K · <a href="https://t.me/naya_foriraq/85943" target="_blank">📅 01:28 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85942">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d59bfa47d.mp4?token=t_-MjLAuRQc9o0oNmD8p4bdrQyJ8jWB7tIFj8zTBtUrwwRlMn44ednY_Fv69HSG0lgJcNjbXJd1B7rVSptNkhQx0haTqEvT5kuW6qwuGM9guvQrApJZTQkXCPXI_quWkAtc6F1oDmnVuHFOHE-LaAQyZ-h9CHW6azBUJr-0Dmw13KvxTwXCi7IebEdju4QXorvVRIuGKUfbB6DtaUQdAa9XjTtDYIlOcDna7A87zaRXZBckNg9yOMQKUAg_hd1pBc4HRDTFJJzmG7r9v8X4Z6zQ_1P_pEepdlzURg08SiVWv7lnzAn_J8-hSrhCOcUZng-PZeEdJWnvy7y4iMUD0CA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d59bfa47d.mp4?token=t_-MjLAuRQc9o0oNmD8p4bdrQyJ8jWB7tIFj8zTBtUrwwRlMn44ednY_Fv69HSG0lgJcNjbXJd1B7rVSptNkhQx0haTqEvT5kuW6qwuGM9guvQrApJZTQkXCPXI_quWkAtc6F1oDmnVuHFOHE-LaAQyZ-h9CHW6azBUJr-0Dmw13KvxTwXCi7IebEdju4QXorvVRIuGKUfbB6DtaUQdAa9XjTtDYIlOcDna7A87zaRXZBckNg9yOMQKUAg_hd1pBc4HRDTFJJzmG7r9v8X4Z6zQ_1P_pEepdlzURg08SiVWv7lnzAn_J8-hSrhCOcUZng-PZeEdJWnvy7y4iMUD0CA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">محاولات الدفاع الجوي الأمريكي بصد الهجوم الإيراني</div>
<div class="tg-footer">👁️ 11K · <a href="https://t.me/naya_foriraq/85942" target="_blank">📅 01:26 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85939">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/k7au9_HWHEjakldjvbnRxsWzv2CaIhH9SoRjeGzhKd8vlUrzfICCq_Wv3fAT0jIdJXQSb9eX3EYNrZZfaN1q7e0LrLC6pquTflWJSB2CHJRSuKfVZFrpJ_L1rBE9TsJ2mijucGAIf65zQ6ymcyaZ7U01_PhCoFJ_AdEWw5jBchD2ogMCIP3L1gaNYME6FXnqWlVzY6g6PDJL_MG-D9Rq6hS5vFvfG-vjXbGDp5ZvsfO9WsgUqilNtO0mzekPjkHJTNZtekpmE4Jm2Va8VYIWCOKSygG9dTiYZryENYHAtIPZP2reXwDjY5265xV1YuWMw6mFa1WkwASGvEZF_lBF3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oRCfjBFKgVyGM9FrTXt0Hu10k951zQjjNKpitm2cSYSz6vGw5lwS6kIZqWQRU9a40welUyc5K4fCaW4NfQzLolyJ-qenM8P0ukc4wnV_Eo9JC5OugY9hIpUbhO-ISEI47S1vRnXO-Ur4bqVhMRKSGeLca39YNQhfqMOVZx5qZOxellZKYQYMTArGUS7CAz20ZaetKD7kHbPF-OHZ0AfdVbAj3ud0a6QNRmCo4pmObsXdrcKu9KMQRHURyBUlneNcFBStTku0g-7QeZenyC8RIwbKB1HMdPxmVPxutzEG_72Xk2M-51HO0_qYONcpqcHLv_XWMTf9UhNVOO60NEOR1A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=PJD6-GY-wsE0RBfTy1z07XqmXvid0603IpdD4bwzCvMNxr-bhfM9w7QoF1a7d9PBMa93WTYER-5USrUenh3HzuAGaScaYGcPGaT3ziPhlD8knjdotxf-b1-w8rF_b42zrhB6LLORxMDbx44p_OCmQ5FDQtgYhaYN0zVD4U8J9gKuhFaz9qbLCBTxTdeGdUToV7v6Jvqiv5nLZbh9SumvzlyUAji54ipzQprMlm4tUnxFt3cVGmP6svh6FDUEJ0Uthe4q27tPH0MdUAP6Ld7Cx8Sat1akrc9zDDLCnB_NEJSwUDLtCRw0Xr1bSn_9jlA7N4OFLrjBd3-6ZhNvf4IygA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ddc19f9a3d.mp4?token=PJD6-GY-wsE0RBfTy1z07XqmXvid0603IpdD4bwzCvMNxr-bhfM9w7QoF1a7d9PBMa93WTYER-5USrUenh3HzuAGaScaYGcPGaT3ziPhlD8knjdotxf-b1-w8rF_b42zrhB6LLORxMDbx44p_OCmQ5FDQtgYhaYN0zVD4U8J9gKuhFaz9qbLCBTxTdeGdUToV7v6Jvqiv5nLZbh9SumvzlyUAji54ipzQprMlm4tUnxFt3cVGmP6svh6FDUEJ0Uthe4q27tPH0MdUAP6Ld7Cx8Sat1akrc9zDDLCnB_NEJSwUDLtCRw0Xr1bSn_9jlA7N4OFLrjBd3-6ZhNvf4IygA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات في سماء الأردن</div>
<div class="tg-footer">👁️ 10.9K · <a href="https://t.me/naya_foriraq/85939" target="_blank">📅 01:24 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85938">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=jpvPIopzRr91kvQoj9ky46XJ8_ITfWN33s68BlA2YSW8KGZPJUEwiueY9Ywj0gbOFZmnbZdbHA0p1NCiY-OaOZDSOSWfIdHdaBOldEK97687wELz6MsmDOt_zIRwTsMcYQbtqIVSYK59eEFKDDd8BBSiQk00gUGQgWI1adtE066ci6uiqlbgvf8ZAEC1kjobSWbg-VFineJefn-f_UbGKW7K53fyJQxSxpLSndqnRlOweIYerK-_AnX_Py5yEUwpqnB905IBXgXEKsYymBTVegr2vtG_orveAsAS5VeCJBBoJ5VN35mCdPFB4zUGsmSiFEKfB6hRsNRXrlHha_Bx5w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/95f6f50330.mp4?token=jpvPIopzRr91kvQoj9ky46XJ8_ITfWN33s68BlA2YSW8KGZPJUEwiueY9Ywj0gbOFZmnbZdbHA0p1NCiY-OaOZDSOSWfIdHdaBOldEK97687wELz6MsmDOt_zIRwTsMcYQbtqIVSYK59eEFKDDd8BBSiQk00gUGQgWI1adtE066ci6uiqlbgvf8ZAEC1kjobSWbg-VFineJefn-f_UbGKW7K53fyJQxSxpLSndqnRlOweIYerK-_AnX_Py5yEUwpqnB905IBXgXEKsYymBTVegr2vtG_orveAsAS5VeCJBBoJ5VN35mCdPFB4zUGsmSiFEKfB6hRsNRXrlHha_Bx5w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجارات عنيفة تهز الأردن</div>
<div class="tg-footer">👁️ 11.8K · <a href="https://t.me/naya_foriraq/85938" target="_blank">📅 01:21 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85937">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">تفعيل منظومة الباتريوت في سماء الأردن</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85937" target="_blank">📅 01:20 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85936">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6ebfe400c9.mp4?token=USu4HXXGLQ8pfJ9qaxiuS476qYhePpcQ1N9-VW4QdU8JSQDnTPiQQTmBY2UDUKLvAS2sLJpG1ia3ELYTeTPwBG0ayOqxd8XL4AAUz1grFZAIY6ayLpcCWqitc8jryZNQ_spWwPDff3uSGthzosoBncL5yUgxgB6HGWmWrfsovvHEJqunLWQAih79hxdKYlKJCgY_ebAy6aSAUxf73KrTvVWmoqxPfhqnZkiMFZEcGyaMkgUiKO7h6Yef-SEgYaHA5dZof09pDMXhc7mAeoZj7fCK94iGzXJVK87lcSB8DLIZFDEJwi2QlgNUG7s9Ob3cd5HJzh3prsL25zhlxMM_RA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6ebfe400c9.mp4?token=USu4HXXGLQ8pfJ9qaxiuS476qYhePpcQ1N9-VW4QdU8JSQDnTPiQQTmBY2UDUKLvAS2sLJpG1ia3ELYTeTPwBG0ayOqxd8XL4AAUz1grFZAIY6ayLpcCWqitc8jryZNQ_spWwPDff3uSGthzosoBncL5yUgxgB6HGWmWrfsovvHEJqunLWQAih79hxdKYlKJCgY_ebAy6aSAUxf73KrTvVWmoqxPfhqnZkiMFZEcGyaMkgUiKO7h6Yef-SEgYaHA5dZof09pDMXhc7mAeoZj7fCK94iGzXJVK87lcSB8DLIZFDEJwi2QlgNUG7s9Ob3cd5HJzh3prsL25zhlxMM_RA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من إطلاق صواريخ في سماء إيران الإسلامية.</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/naya_foriraq/85936" target="_blank">📅 01:19 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85935">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Cd4HLHL4OHzNgovJEZN1SukCo_RhVo50OpngvqCcnwRKQuh-77k2Q68CY_comTK0TbN0b-Ye8A4mRrhzbUHyxcnjjO0Mf7yJuUpIPzvF4mopyZlGPbQ-RqcOp-WKbEXed1V4j0V4dNAfep4MOuJB1CLAhrCKG3GbKIVGtu0mkbc9HQmokNzrxq0mRXlYeZSrqTyxKK0chUon6Hi5wfONFh7aqt_PwODNkdbT3m3yYMBSDytFmRqF89OrAFyu9-5T5jaYdwOHWEsibpks-BIk1gs2ILgfccg-5wBM8LYdZ5vbq32B3GI8QCB60RFLYIbKcvetFu2aD9plfgeWw1puLg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85935" target="_blank">📅 01:13 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85934">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">الصواريخ الايرانية تكشف الزوجة الثانية...  سيدة أردنية تكشف خيانة زوجها أثناء قصف قاعدة موفق السلطي بعدما فضحت تنبيهات هاتف ثان كان يخفيه في الخزانة ويستخدمه للتواصل مع زوجته الثانية.  والعباس القصة حقيقية</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/naya_foriraq/85934" target="_blank">📅 01:12 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85933">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">انباء عن اطلاق صواريخ من إيران.</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/naya_foriraq/85933" target="_blank">📅 01:10 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85932">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">بوليتيكو: ترفض الدول الأوروبية المتحالفة دعم دورية بحرية تقودها الولايات المتحدة في مضيق هرمز، حتى يتم التأكد من أن الهدنة مع إيران ستستمر.</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/85932" target="_blank">📅 01:05 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85930">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/YllfjPNk_ETTw2N0RIAoszXIDDyrORowbebp6d30vkTBwsXp4fG7lqGnJnih1iHVjJGb6-3oza-eBa_77EBg9ikjyQ8EuCRSi2hrMo6U3ngS9lDIq5w1I_aODEgjrN5f5jXzYvi8-INAfw-Xj1T-OLuoaUTYkpJ3o2Va0bLYgbD08HeOFCTY-dI7bgI7_xcpTAXST1WrRUOPSj98uZYZC64JMZtD7c-59jOdyxn7vzZ1P6IfTJ5Tw-c8RVOCGKixEUzLIPVIrbTrwX9y1-L6OVe6P_Qf8cs558xtO4U5lVGRlhKSlKOW-6k2nNAv098w0F1kfr3ozeBRJ-aMQ0Vnug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/u7LWcPAIEBon6f2un2w4oClyAtFj03OF0Us1rvc1YJhVs0swHFF1V--sVbzXXwBKtFssZRQpN47xVBOSgF1VjLJUoyFL7WlswBWISoaKnS1GN37SgL6B33heigN6XuJNbQJH-DTun7HEXEaBP1S8YtO1vviSQBe5LE1nAVehmZmuzdhTtKwNiuTHL6un1N0cuPtYaXTn_hcsyhX15nd9ZO4HQLYrY9OKWC4iWmXVyzZAmDqSHMIxGBvsKvL6X2rhu2XmXx6YFv2c_zkO5sqWNBlBcdFyBguSLCGpW_E8OKCaAiC_jPjKtObQYsLh5XgeLSvwgiSjdqbk12eirCOiNw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇾🇪
🇸🇦
مشاهد حصرية لنايا... مراسلتنا الميدانية من المملكة العربية السعودية توثق تصاعد أعمدة الدخان من محافظة البقيق، عقب استهدافها بصواريخ أنصار الله في اليمن.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/85930" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85928">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NHRmaOTUif9yZezAy0mfEx38Suxz1KSsshvH0fT6kU1CuTY4OvdOorlZ_vX9bthJKMOmdiIJ_AIt_7mAVxFq8LmIiZDfVRZXhgP5hHABabE8MR1wa51--uzxekyictxee29mEKquFz3Jz3wzqoHX4Zk7PK4aQSd3Y45qC_fFCZ3zyJIW0HwDrtHoEWV1JXsxGEo5aHckrHkvoWUIxGpPlzOBB9CgwQUrkD8BR0EQNE1m3sBZEjj6UPoqVDDLX3WCHKje8jcylHCRyVDsOFue0GxYVdYKe2Me7Rf6DrWzNqXW3aOSQwFZgYZsqQDQhzClSfKfrmY9KKZMmbF-Ec0b_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rhSIB9UsvaNytjkidcLh6efqdj5WddTUqmhg6Sh1pjIeawTcYLxJZuy7xMgXoTNUhqJd6XmsuEch52v_YoFk5RzhQmcX1uachvRjbe95OQWH1VRuIcBbJN8cGZlvT4vXB_xXOM0Z2IZAe7efUIcwONOzbUAlnfBP8TcID7iot1pnxZCxyGXSPf353jEpLHe3pzgzm0gqR6q_ifb0gFbUP22MRC3_2ssxdzvU-HqGR_wfUmZVEBD6hZecbAEqdCPMPV7uG4f10y6M5GChoAPxVVtGeaztcivi6XoYj1CGTavFpJeKa5e38sje-OhVVdTyJsVNXvQoEbgs1cSj8H0q3A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🇶🇦
حدث مجهول في منشآت لتسييل وتصدير الغاز بمنطقة رأس لفان الصناعية شمالي دولة قطر يوم أمس أدى إلى توقفها عن العمل بشكل تام.</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/naya_foriraq/85928" target="_blank">📅 00:57 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85927">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/04839e658d.mp4?token=TtVaBbpOl4cOsu8aqk420nlrMCMcQPYmqZiX44E1He33ieAzKlvUQy3jXFLCvTaxFSwh8PbiTySb5lvO9whrfOM6aj4AEQoiKgO04tmZhJ2f803JIwwAZkAK-ilVxWBQnsyYD0dXyTl8-VPkEJU6WJ6xFk1-w8_3wXj7t8e1qbCqLWkPhrZm53fOz6F2_QRCn3KyKw-aCvkyIuqJSG9rIGNDiue24Fc1RWcYqdc_Uh9TXAurIc_XXVhek0Fh0JcGwyBWNQFWUOlOHm-xLU-Tj9Uf9SUBx1cmN3fEzsr87B3fXqE_K6zJEGh00c0tSG6XCm0Hd_dJb6f25tojA5N7VQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/04839e658d.mp4?token=TtVaBbpOl4cOsu8aqk420nlrMCMcQPYmqZiX44E1He33ieAzKlvUQy3jXFLCvTaxFSwh8PbiTySb5lvO9whrfOM6aj4AEQoiKgO04tmZhJ2f803JIwwAZkAK-ilVxWBQnsyYD0dXyTl8-VPkEJU6WJ6xFk1-w8_3wXj7t8e1qbCqLWkPhrZm53fOz6F2_QRCn3KyKw-aCvkyIuqJSG9rIGNDiue24Fc1RWcYqdc_Uh9TXAurIc_XXVhek0Fh0JcGwyBWNQFWUOlOHm-xLU-Tj9Uf9SUBx1cmN3fEzsr87B3fXqE_K6zJEGh00c0tSG6XCm0Hd_dJb6f25tojA5N7VQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇱
🇺🇸
🇮🇷
وزير الطاقة الإسرائيلي، إيلي كوهين:
أعتقد أن العامل الوحيد الذي دفع الرئيس ترامب إلى توقيع الاتفاق مع إيران هو مسألة أسعار النفط، وتأثيرها على سوق الأسهم، وتأثيرها على الاقتصاد.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/85927" target="_blank">📅 00:42 · 07 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-85926">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">الصواريخ الايرانية تكشف الزوجة الثانية...
سيدة أردنية تكشف خيانة زوجها أثناء قصف قاعدة موفق السلطي بعدما فضحت تنبيهات هاتف ثان كان يخفيه في الخزانة ويستخدمه للتواصل مع زوجته الثانية.
والعباس القصة حقيقية</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/85926" target="_blank">📅 23:44 · 06 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
