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
<img src="https://cdn4.telesco.pe/file/fa_wDvOylGmB3rDkk1WpTJkxvA_vDux-MPCDPZfOkfKQJIlUYPOcRuXJmCieyHGh3oWXNfr4jGIVMVLuppsvlK7iCdqkcD4kjEDH4Q1mWao91Y-HaVCfFD6GiKcKn7mFW8W8KgObvyxPQuTZ00timZnhW9naMoP7RjvImgPqSsWgKZW4NMXO2GeDkvvMyfWusanh5xvfPtt38FD0t4bgdwTOh7q3AxGm7DS8ssyPWbZazTO3xMHevjiNJlo2KNo4qcF9IM9d0zlV1SmW2NZKClsDI33EpApdRCVhXj4Mi0Q9cJAtzZEBZOV18gnpOqj4t84RjLd-Xk22vOO8b3U31g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 270K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-01 00:42:45</div>
<hr>

<div class="tg-post" id="msg-88335">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LQj_yMZ_ACR9_-cAWQXZHIXXXeowZu0usQou18p_Cz5D9mRC3KyhrlLElX1w1JX3G0SpZVwXEbpfT0KNLyR45Wc47KozqST9HijVH7rvsYoI6ZecJuNmb1GNWitfTfpMv124-X0wKHAAloFieRGTOxm1O5wN-sLiTKWnm0t7kxTu8inIBzmmly1fzni-mOVQGlY2rvEIVqOad8UknCqfNdIxwMx4EE4xobelxeq3RAO5eGhffq3JYtcQRYa5w3T8F8-Sgo5XQecd-LpC9M3jgJmq66jHkIcVpHcDg1PbyzLjCRpqpyip186txXLLNCS5VBbtqwFK3OHx8fgMK3n1PA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاعلام الغربي: ‏
هناك أمر غريب يحدث مع ناقلة النفط "نيو فويج". لم تتحرك بالقرب من مضيق هرمز خلال الساعتين الماضيتين. ويشير موقعها عبر نظام التعرف الآلي (AIS) إلى أنها راسية. كانت متجهة من الإمارات العربية المتحدة، والآن عادت أدراجها دون أن تتحرك.</div>
<div class="tg-footer">👁️ 990 · <a href="https://t.me/naya_foriraq/88335" target="_blank">📅 00:39 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88334">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a2zXXQ8HgMCqEkUpFpozzEQliTEgvXLJHRzrbSbgPw8eLf3cM2rDgLUMqtjjJyJwnCQA0nOf21REojr889GZb9c9f-QBzhM5-7B9G0INpYsQ0_vIjvfAkgvtvRqIQTtZFbfBkV7A8Q1DaJhIDwF8M6zSgZgLGFk20uco93h7tFTMplTZkxrMVzSbQcz44o6GWYOVqzbKBgPTR7Tp38Jo9RV0lShuTpEsAcORVb7nVRvwlDYfu2U7MRoAkvEkMjRf18366JKK7yDeRlwcmBk9BAStvfNm03KGpfXKbNii9iATs8LiXZqnhlTks8OAjXcz1OWO1iLbNdnSByeTotLtgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترمب يعيد نشر تغريدة بخصوص مضيق هرمز اراضي امريكية
😫</div>
<div class="tg-footer">👁️ 1.96K · <a href="https://t.me/naya_foriraq/88334" target="_blank">📅 00:34 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-88332">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=nsNy8JRLjlbUW6HcC_gU6BmhRZrS0YUOFCb8D1UGRgovP6NjBZa87uDFayM0RmowjI0AB475pYvt1drzmKeFz3r5biSkfSZYNt1IAvxVgm9dr_I2zN6JT0_b8mvW8hXAgxC4WCUXisyqZ40bVVNYbSqFEiiyeq8vUyp1jGoguhaDtW_2jEUVYr_Bo6g8Wbydkf-tmSGN6coyX50FJvrPQSD0CcS1M1kpXqh7AdqOlTqIvQDKy3mHs6O4sAqabAcdUSHdfEDFZ1SMbK9QsyTjAyulSUPvLiledDfq4Ne7ysSHknvfhUcd-VKmyUGlVTfKJ8B-ipZ8W4R8QQazFSeFTg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c07055ecbb.mp4?token=nsNy8JRLjlbUW6HcC_gU6BmhRZrS0YUOFCb8D1UGRgovP6NjBZa87uDFayM0RmowjI0AB475pYvt1drzmKeFz3r5biSkfSZYNt1IAvxVgm9dr_I2zN6JT0_b8mvW8hXAgxC4WCUXisyqZ40bVVNYbSqFEiiyeq8vUyp1jGoguhaDtW_2jEUVYr_Bo6g8Wbydkf-tmSGN6coyX50FJvrPQSD0CcS1M1kpXqh7AdqOlTqIvQDKy3mHs6O4sAqabAcdUSHdfEDFZ1SMbK9QsyTjAyulSUPvLiledDfq4Ne7ysSHknvfhUcd-VKmyUGlVTfKJ8B-ipZ8W4R8QQazFSeFTg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇷
الأمين العام للمجلس الأعلى للأمن القومي الإيراني "محسن رضايي":
إذا ما أراد ترامب القيام بأعمال ما، فسوف نردّ عليه بقوة وعزم.
بالتأكيد، سنقوم بإجراء تغييرات في مسألة إدارة أساليب الحرب، وستحدث تحولات في السلوك الدبلوماسي لإيران.
نقول لجميع الدول المجاورة: لا تشاركوا في الحرب الاقتصادية الأمريكة ضدنا، وإلا سنعتبركم أعداء.
نحن لا نسعى لتوسيع نطاق الحرب، ولكن إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية، فسوف نضرّ بمصالحهم.
إذا انضمت الدول المجاورة لإيران إلى الحرب الاقتصادية الأمريكية ضدنا ، فلن تخرج قطرة نفط واحدة من الخليج الفارسي ومضيق هرمز، وسنستهدف أيضًا الطرق الأخرى التي يتم من خلالها تصدير النفط من الخليج الفارسي.
مضيق هرمز مغلق ولن يفتح إلا إذا التزمت الولايات المتحدة بجميع التزاماتها.
أنصح الأمريكيين بعدم إرسال أي قوات إضافية، لأننا سنرد عليهم.
أي حركة تقوم بها الولايات المتحدة في الاتجاه الجنوبي لمضيق هرمز، ستكون هدفًا.
أي اجتماع يعقدونه مع جماعات معارضة للثورة في المنطقة، سنستهدف ذلك المكان أيضًا.
لم نقم حتى الآن بمهاجمة أي من المصالح الاقتصادية الأمريكية.
حتى الآن، استهدفنا فقط القواعد العسكرية، ولكن إذا ما تم تصعيد الحرب الاقتصادية، فنحن مستعدون لاستهداف جميع الشركات النفطية والاقتصادية الأمريكية في المنطقة.
سندافع عن إيران بكل قوة ولن نسمح بعودة الأمريكيين إلى إيران.
نبيع النفط يومياً بكميات تعادل إنتاجنا، خلف السفن البحرية الأمريكية.</div>
<div class="tg-footer">👁️ 8.78K · <a href="https://t.me/naya_foriraq/88332" target="_blank">📅 22:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88331">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">🇮🇶
رئيس المجلس الأعلى الإسلامي الشيخ همام حمودي:
لن يفلح أي رهان على حرب شيعية- شيعية بوجود المرجعية العليا والالتزام الديني ووعي أبناء شعبنا بحقيقة المؤامرة الخبيثة.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/88331" target="_blank">📅 21:54 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88330">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NkDO_biuSiNTZDo60z2rsfYvk8ZGWgTLwF-ZafaNI7Nt1L1CuEHmM6cpXeDGR0TqgYQ5JiP5fklwcbEAxrnP1qhrQZZ9tO7s-H9Mhg8Lrk_fHTLG9yRr9z-r_DJsq3r5LSwBSMRshkppj9r1ZQe5wwWSg3ZnFFsWcGiT4o3X5koF0LBNqRrGEKFCzVvKlP7utzzyVC4p8OJQfR-duDXEuUgit-u6ONh-ngE3iYoDfVKQ_xie50FXun9JnvRA1UTBEXVBcSLtnh22WZaIQlx-9QcWbd1AeCtx-RpvlxozhgQ-MtA8vtUB2vzGQm_dW-kOBff5HuHii6mzUe5r4Z4Yzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/74d826f753.mp4?token=NkDO_biuSiNTZDo60z2rsfYvk8ZGWgTLwF-ZafaNI7Nt1L1CuEHmM6cpXeDGR0TqgYQ5JiP5fklwcbEAxrnP1qhrQZZ9tO7s-H9Mhg8Lrk_fHTLG9yRr9z-r_DJsq3r5LSwBSMRshkppj9r1ZQe5wwWSg3ZnFFsWcGiT4o3X5koF0LBNqRrGEKFCzVvKlP7utzzyVC4p8OJQfR-duDXEuUgit-u6ONh-ngE3iYoDfVKQ_xie50FXun9JnvRA1UTBEXVBcSLtnh22WZaIQlx-9QcWbd1AeCtx-RpvlxozhgQ-MtA8vtUB2vzGQm_dW-kOBff5HuHii6mzUe5r4Z4Yzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 10.8K · <a href="https://t.me/naya_foriraq/88330" target="_blank">📅 21:46 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88329">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YWogY4dxc_grHN9zi-98PbV2vzrA4nIyWHjLnV1VfNJgdT87-XoiaNNWP_wd8EtsWjLKSQ3H-V-Iv1S9p_iGVaS4PziEmefOj6zZJaFEua9y0i9jb6a7t4QrUiskm3vBK6_q_AZ6Ij4ap-LqjR3h0okfWr93vKPJBV9oFHBKgjih-hpX65HVdg_SN81SsJwMJm9Ky191_Rkqf7-GJ4uuGnrQB1JoGr2pwjU70vfsTKd9kTGIZYoyT3MRAge3xdIpGjsT0mAxEx9i_2EGlo1_DfFCLB-jO-0kA40Mvq2WIrhs7ARnVi67gc4omeSysJKq1KFrY8Ivw-hzU0UXamcVEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
غارات اسرائيلية على الجنوب اللبناني.</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/88329" target="_blank">📅 21:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88328">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">🇮🇱
‏
نتنياهو
: لن تقوم دولة فلسطينية تسيطر عليها إيران لا في غزة ولا في الضفة.</div>
<div class="tg-footer">👁️ 12K · <a href="https://t.me/naya_foriraq/88328" target="_blank">📅 20:53 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88327">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=FqzGCHKB0UvCj5QKJ0I_r3Qb_S2oa9l6H5pHapzK3HoJrpYRz5N84AdQ-p1Oo5-pgqdOd9EmaGMv0200sfaFVMcUPBEa0tO0Yad_ZMr2Lm51PYZxNHVkKeVEHfDzoUrNQBo5Kbuz42p5slGXuYZJVmI0G7_6rjRakuXVNZdaT55b9xZRnCvtQWlL-KE16Hh7X-VztKwxZEu0yHLjAEzIYA553wkSaSdTwnM4d4ObE-PY0ZyuDLpgCaOqJX5a3HoJkaMGVNSio2x-FM61rQBy8g9xzlfwyHrzuUQeVRw3vsoh7Uo2BtOKy49pnYgMv8EYGdi3vAJ-swgU3bjxZyU48A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0551d70e8.mp4?token=FqzGCHKB0UvCj5QKJ0I_r3Qb_S2oa9l6H5pHapzK3HoJrpYRz5N84AdQ-p1Oo5-pgqdOd9EmaGMv0200sfaFVMcUPBEa0tO0Yad_ZMr2Lm51PYZxNHVkKeVEHfDzoUrNQBo5Kbuz42p5slGXuYZJVmI0G7_6rjRakuXVNZdaT55b9xZRnCvtQWlL-KE16Hh7X-VztKwxZEu0yHLjAEzIYA553wkSaSdTwnM4d4ObE-PY0ZyuDLpgCaOqJX5a3HoJkaMGVNSio2x-FM61rQBy8g9xzlfwyHrzuUQeVRw3vsoh7Uo2BtOKy49pnYgMv8EYGdi3vAJ-swgU3bjxZyU48A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">رصد نايا
منصات مقربة من فصائل المقاومة تنشر  مقطع فديو لم يتسنى التأكد من صحته مع عبارة " ستعرفنا ستعرفنا قريبا " المقطع اظهر مسيرات من طراز حديد 110 التي تعمل بنظام المحرك النفاث .. فيما لم يعرف دقة او وقت الفديو او مدى جديته ٌ ..</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/88327" target="_blank">📅 20:42 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88326">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Dm3i8PYGHjnbyFSw-zupcNK7uA8ARgNeG81p1vCDUZZkLwrs0Nm5M4LGRx4f3n9PJJBAfbU4i6_Yt9UwGIZuP_0Kajhi30XHGbQ9HSYdqA4clqgwuV1Kr19Wl_5dpSmjeD_hVQHk3QVNUhwMHnSuPgXAj0ZFtJpORfDj_ra1cd02UJ_Ps3kNxOQlMxi9EfgqfruEoYxgPm1FAkYIoTTxO23A-tUifP6Ljsb8gq9zFURuE4a6xTIglNEvX_x0X7r8DwFXzeDJOJNoeOPkq8O9Dour2uBIVR4bJDFRW-4_oL5FQ5LukA9CwunTRhJl9fNkI-7VGno91jchJBWo-dlkZQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">العبوة انفجرت بباص تابع لعصابات الجولاني على طريق معرونة – صيدنايا بريف دمشق</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88326" target="_blank">📅 19:36 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88325">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/88325" target="_blank">📅 19:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88324">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">انفجار عبوة ناسفة في ريف دمشق</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/88324" target="_blank">📅 19:34 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88323">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">‏
🇮🇶
وزير الاتصالات العراقي:
ملف حصر السلاح بيد الدولة يحتاج إلى واقعية ونقاش عميق ولا يمكن حسم ملف حصر السلاح بيد الدولة بمهل زمنية محددة أو تواريخ ضيقة</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/88323" target="_blank">📅 19:16 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88322">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">🇨🇦
رئيس الوزراء الكندي:
لا يمكننا قبول عرض الولايات المتحدة، ولن نقبل مطالبها.</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/naya_foriraq/88322" target="_blank">📅 18:41 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88321">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=usKqpDRgzEjL9i-Anv4Jl1Itm0OjylszSIP9smGtcI2Tjy-9xgFsU4LWOdHiGWmPIYojUCsv_fCv8ykGMjVgt4Na5_4KwAWYtu9af8JAPr0nmZG92jhy-pEReLcKYiLrCSfZ7q_6A3RRf7oHL3xkxPT-MZ7OZj3LsNbFlJQKKVxPBY46RhHpp38iOa-qUAtPlSINV3tZdmAHri1Ma6yCh3QmiOghutHmu2CFBDljP8jjRgHeVZ9zV2HjAxxs6p3usI25C63WQ5BYext6goSB0sbWl-GjV6jfz7Vvcemfe70cpbdvtjIo_O8Duo8d4bGMtthCcyvXg10ZfM41YqzTkW1i9X5P5CTFxcxwXrWYCTCPm4JGWDCBzp09awVhn5UsZ5owltGRvAiqZdh4jHqPiU9Hn7sYRMDTMyvZTabXfF01rvnp1iihlJ-UCZcmCmWZuNJv_rTSGHStoq5ASQJZvMzvUDrGhcFL3J21l8geyJK1fjwZxXrn1bbmAGmbSMaYK6rY2Rzdf8zEg0HSFfau7oGOIYvaXzUk88gfl5rJptMAjouvPbnYjEgfWR6SDwce1boao69mDaAGIwqwkM9qsQ7-Af9NkOb95D1IeO_fHEiMA8JzDsLqir1U61DcGScgysXhAo9-WB7oZ3ctBXqGGc9opKNO3LL5o98RUPepl4k" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cc26914f9.mp4?token=usKqpDRgzEjL9i-Anv4Jl1Itm0OjylszSIP9smGtcI2Tjy-9xgFsU4LWOdHiGWmPIYojUCsv_fCv8ykGMjVgt4Na5_4KwAWYtu9af8JAPr0nmZG92jhy-pEReLcKYiLrCSfZ7q_6A3RRf7oHL3xkxPT-MZ7OZj3LsNbFlJQKKVxPBY46RhHpp38iOa-qUAtPlSINV3tZdmAHri1Ma6yCh3QmiOghutHmu2CFBDljP8jjRgHeVZ9zV2HjAxxs6p3usI25C63WQ5BYext6goSB0sbWl-GjV6jfz7Vvcemfe70cpbdvtjIo_O8Duo8d4bGMtthCcyvXg10ZfM41YqzTkW1i9X5P5CTFxcxwXrWYCTCPm4JGWDCBzp09awVhn5UsZ5owltGRvAiqZdh4jHqPiU9Hn7sYRMDTMyvZTabXfF01rvnp1iihlJ-UCZcmCmWZuNJv_rTSGHStoq5ASQJZvMzvUDrGhcFL3J21l8geyJK1fjwZxXrn1bbmAGmbSMaYK6rY2Rzdf8zEg0HSFfau7oGOIYvaXzUk88gfl5rJptMAjouvPbnYjEgfWR6SDwce1boao69mDaAGIwqwkM9qsQ7-Af9NkOb95D1IeO_fHEiMA8JzDsLqir1U61DcGScgysXhAo9-WB7oZ3ctBXqGGc9opKNO3LL5o98RUPepl4k" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇹🇷
🇮🇶
مركبة تابعة لجيش الاحتلال التركي تمنع شاحنة لمواطن عراقي كردي من المرور في قضاء شيلادزي ضمن محافظة دهوك باقليم كردستان العراق.</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88321" target="_blank">📅 17:40 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88320">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">انباء اولية عن اختطاف أكثر من 60 مصلياً من مسجد في نيجيريا</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/naya_foriraq/88320" target="_blank">📅 17:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88319">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=nEwFiVp0TGslK_PI7cWNH9eBtUNofdWLxJP6TCJ4ZesAscNgbutrfNwxBEg0jPbBWRtVNdy1zscudkOmwBEGslXxgf2ApdtP4kSdKrAtJLGthSq7MiP99Dx0F59J4fQDxWTfpAvuZnVO48l39_hwRobuD3HEOtVXAcqnjzsLrH8uPUbFo7Mv6og6NcZDuu3NJb6eLh3UnyrzF-zSN49_IiW1dK-OTGdNVkERCM3axvKzdbIXANMVNK60m-i_MbxPG9kltZg0Bz64LmB6Cd3Nowg8FCvluOB832g9kKfFbJhla1vunfXjO_3iVssL_USNGjkH5c_4sDSZz30GnyFMLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a2655fd592.mp4?token=nEwFiVp0TGslK_PI7cWNH9eBtUNofdWLxJP6TCJ4ZesAscNgbutrfNwxBEg0jPbBWRtVNdy1zscudkOmwBEGslXxgf2ApdtP4kSdKrAtJLGthSq7MiP99Dx0F59J4fQDxWTfpAvuZnVO48l39_hwRobuD3HEOtVXAcqnjzsLrH8uPUbFo7Mv6og6NcZDuu3NJb6eLh3UnyrzF-zSN49_IiW1dK-OTGdNVkERCM3axvKzdbIXANMVNK60m-i_MbxPG9kltZg0Bz64LmB6Cd3Nowg8FCvluOB832g9kKfFbJhla1vunfXjO_3iVssL_USNGjkH5c_4sDSZz30GnyFMLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صدور مذكرة إلقاء قبض بحق مواطن سوري يقيم في العراق على خلفية امتلاكه عصابة وقيامه بتهديد مواطنين عراقيين بعصابات الجولاني في حال توجههم إلى سوريا</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88319" target="_blank">📅 17:07 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88318">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🇮🇱
🇸🇾
‏
وزير الحرب الصهيوني:
وجهنا إنذارًا مباشرًا إلى دمشق قبل تنفيذ الغارة على "مطار أبو الظهور" وتم إبلاغ السلطات الأميركية بالمعلومات الاستخباراتية.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/88318" target="_blank">📅 16:25 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88317">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/a9WCUnz7irEvTCfb-pjFLIbB1JWMwKY6TloczfeqLMz-hqv-eSKmrUh30bhw6FXFlY95c_S9t2Y4zvAlH7tteHquGjYfyZGavpPGkWRkj-34-uSxTkqKgX2eOXNlso_9HQs2NLuyV7KeKhMPoh2Tmk-7UR-1rf4Vz8TnQW0r4yn-2eHQRNz3zcvqM5QUbGMSULFQ-mh5ToICewiCJuYJClGxOafgw0JpNMp-jL0cEM7NgunTyBGEGNhZL8fELOlxYc5PjpcUlhEF7NChKQVLM4uzO1n3SKrjrAEXlBUWUBrJb5sYUo0WTYdxOLTcCKzKY1O3k8UGYKEN3hdoFEeI6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇾🇪
بيانات التتبع:
‏
تستمر صادرات السعودية من ينبع في الانخفاض. شحنة واحدة فقط من ناقلات النفط العملاقة (VLCC) قيد التحميل. ترسو عدة ناقلات من فئة أفراماكس أو أصغر حجماً في رصيف أرامكو. من المرجح أن يكون إجمالي صادرات المنتجات المكررة والنفط الخام أقل من 4 ملايين برميل يومياً. ربما يلجأ السعوديون إلى تحويل مسار النفط للاستهلاك المحلي بعد هجمات الحوثيين المتكررة.</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/88317" target="_blank">📅 16:23 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88316">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">لحظة الانفجار داخل احدى المصافي في منطقة دارمان ضمن محافظة كركوك شمالي العراق</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/88316" target="_blank">📅 16:19 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88315">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXKVaYqdwUeZpVSgc0I86-BiP5BPuh0JeaMfs3tfMztyY7s2ca2qFbx9bCCkYMtf6Oosqm_Xv_jKnp8o-0WoQYgkyQzQid1QKEO1vfg9lzrGh-9jomD8C-ZwPWQ1lpEYSfEYgD6LMUITTnM4ElnCrrDLs-dXE_iI5C_D7u7VL6Tcv4VuETwMhDZUGmcB_PjRoeYkeLLHBtcg0Tk0D_57utEj87bEVuuWrz5KjW_m0m07oS1CWM2Rpma31SXy1fKaF9Mg5T_hUUiUP7pEu0sd2w_Prbmf7OowBIgzOYpBlOPLCfgg1FplJY46xkhY--snUovfqg1C9SttxUNykbeSZg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔺
ارتفاع اسعار الحديد في دولة نيكاراغوا
#دنيا_وصفت_ياناس</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/88315" target="_blank">📅 15:49 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88312">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/O4z2HUI1oiE1R727pVAjzEkvJaF_FUJ33PDT4N2Z8mno-jHMupUFgneQlP8h_QjHX8OwOE9QH7a167yYkOOlf2VRJmR46kfSeGrYc1zC94LwTUWG4zoYkMiDdYiQ1ySdB8AnbeJiDxxxs_ZONg0bZvdbk4EU0poJsk4dfd-kEobddUsdGY3_9p0JTtE8bdDe12KjKJ9yy6mKJggBDP2RaXSsxif5vqaKwN9BJkXqjwchDV_pAnj00oRqaQusbjSZ4tK4tkwaK8hgGO8Aa1FJSe5dddtG7v2yqfYs-DKqeN09_3hkcZ26heCumXuv_Q3Xw5XP0xkYsJdqWWxurlIfKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QeQ9md7OBwfci2ECmbRwjrm9D7534rKWMVq8ZHg1PdKiCkkyj-9FovzzCWerhlsS0gvUrtljKeYsKuohW_GiGD6UnBUGxbMFqUklcqv4JxWST0Dl-4byp8lyYQCzC4fN4Y16CH_2Ers0rPx6IvP6pvvS4XykGWHOBMJCbybNbkcyoOZGJgE0D8tXbFMNQBbXjOMLDSSIoUq1334BCRhChbhP4gys6HINu-N7AEjBDdaVS3elEhCmaOd28WERMi4mfytVDZ6vpgoeiR0LgPV-zmsIDpNJdzmFTjE9_NDVWEFjIyLcdNr8gUlCfgxPYlK2DhbVSmWxKNfwu9QIHuTnZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZvEHnFhRb6tAoxktzN22YMBrrLD9X16-SpMZ2uMJusiSBdMsSKJxZe6NNJkuv3EgijXIYWURO0YEx1Q3QGrqli-HdZ9K0vbKoRJvhGzeeSn3lL3Y7wKvrlnr7C7dtKLH5Bik8psLtPTCY1FkoJ__dsY03BFQLxHYJqWICd5s-m48gFBrol4WzdaWlBH4g0yIPdnaJnjDpNpUXYE1a6iZSRokgwaTjRLZi1z8DWqV7zj9s7D85njROOD3y9fE18Jwyd0BXNJnOX4AmcYTnMv6fB7RI4B8iMfLAMNbgTafbKPNj4cgibie7x17Tc-TNA-LzxEgkelrk5_J0q6dc0OCHw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">⭐️
تمهيداً لمعركة كبيرة في حال لم يسلم لاهور نفسه.. نقل دبابات الى محيط فندق لالازار بمحافظة السليمانية مكان تواجد لاهور شيخ جنكي.  انتقال تانک به اطراف هتل لاله‌زار در السلیمانیه که "لاهور شیخ جنکی" در آن حضور دارد.</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/88312" target="_blank">📅 15:13 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88311">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=BtyUfwClRGpHbYUnH2NT3WID5a7A_3yz-ZBtxxfI2rJyKELYdWyC8BypFN9Tauau2C201GqYen7FV6ooy3hdc2seBqrepPY_iHN8dW0XyprvZptyVo-C-Z7Pu_wH67aEAm3ZuiJSLWq_dKMQNdOedRLRtIG2cbCtF7wacafV75C30mlO3JgsIhIJtGCD-ls9xQ679GTIOs7dODaPickQ6iFg-g-t-IOwFW61M3fySPkoSoyYuaPpsBc3YyZYBH9siVYLtrp7vFpWfBCGwa_LaEWm1tq-JdqzaU7D1BD_4lzz8WQkww0gwz8Asa051dx_ir0Q9x71_nk8iLobh_qVLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b84232b8c8.mp4?token=BtyUfwClRGpHbYUnH2NT3WID5a7A_3yz-ZBtxxfI2rJyKELYdWyC8BypFN9Tauau2C201GqYen7FV6ooy3hdc2seBqrepPY_iHN8dW0XyprvZptyVo-C-Z7Pu_wH67aEAm3ZuiJSLWq_dKMQNdOedRLRtIG2cbCtF7wacafV75C30mlO3JgsIhIJtGCD-ls9xQ679GTIOs7dODaPickQ6iFg-g-t-IOwFW61M3fySPkoSoyYuaPpsBc3YyZYBH9siVYLtrp7vFpWfBCGwa_LaEWm1tq-JdqzaU7D1BD_4lzz8WQkww0gwz8Asa051dx_ir0Q9x71_nk8iLobh_qVLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الإمارات تكمل بناء أقفاص معدنية ضخمة حول خزانات تخزين الوقود في أبو ظبي للحماية من هجمات الطائرات الإيرانية بدون طيار، وذلك بعد نحو أربعة أشهر من العمل.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88311" target="_blank">📅 14:04 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88310">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ClLx_snp8P82wrz6qpRGEPzBztveUfmF0TMCzG4jaDHTOdnU1DkLR4eqQbxgN3H7psfGnf_sjkemcXH0F0JA7IRmHtjh9VN0ZR7A4zKhN3j9GQe6EJwTZEi_VfGpiH8YcQ9VPrergyLmrHklrP5CmNnEoOAKr8Onbb_yvQOYh6Mqw-2zpgnCpE7wR0jXcOA7pq6k-N8buVzUjh50W_52AhS-nFE-f9oNcaWaYzTRMEC0sQjvCnP6vxDSQ-n7JvE9YhApAnJTdaG8dGA1c4U6fnpKQKIdUt5XxurB2MLw5evZLmu36114iOQ1xkGkwAdP1vWGap8DAP9SgBKuBpEkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
محمد باقر قاليباف:
لقد تلقينا العديد من الرسائل من الدول المجاورة بشأن صياغة ترتيبات أمنية جديدة وتعاون اقتصادي في المنطقة.
‏لقد عرّضت الولايات المتحدة أمن كل حليف من حلفائها للخطر الشديد من خلال التنمر والتجاهل التام لمصالحهم من أجل إسرائيل لدرجة أنهم رأوا لفترة وجيزة وجودهم كله على المحك.
إن النظام المحلي المستقل هو ما سيحقق السلام والأمن فعلياً.</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/naya_foriraq/88310" target="_blank">📅 13:55 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88309">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hrztJM9DKN8fTL40DDsARHsBYgPiYV7ol5wBG5k0dG2Y1SnzwIn8eahXiJSBBN8cjqlwTl2yMavc6R_Tbrn5pWhvTMePBZ_mVBiJrfrQZ5Lm5zCtJfSHHvm8aNmw8eBg8y0BLRHE_48XgmNMDJhDqgbWfP_Oe-R8hcOUTwR5VtOb86AG2IwQ8tq8OlGv4UufsS8ifA2tKtJzl8SHdCGhGnoC-lwDxW8e5Xh0PohRqPW9l7jX_oQslYqdnlbKGGKJ3DiN-BMPmDP8Ht2DfmUrNA1D6OcwPgV6uggL-gpgS2L7P6IwExOD7qhgQdYCLNbmbv2d2TW9eakKVPX5TiwGUQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇸🇾
جيش الاحتلال الإسرائيلي يستهدف عجلة بمسيرة في ريف العاصمة السورية دمشق؛ إصابة شخص كحصيلة أولية.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/88309" target="_blank">📅 12:58 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88308">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🇾🇪
🇸🇦
مرتزقة السعودية:
الهجمات الحوثية أثرت على ميناء المخا وحركة الملاحة.</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/88308" target="_blank">📅 12:45 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88307">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">🇮🇷
قائد لجنة البحث عن المفقودين الإيرانية:
الوضع الصحي للطيارين الإيرانيين في قطر ليس جيدًا.
مكان احتجاز الطيارين الإيرانيين في البحر لا يوفر الظروف المناسبة للحفاظ على صحتهم.
يجب على الحكومة القطرية نقل الأسرى الإيرانيين إلى اليابسة وإلى مستشفى مجهز في أقرب وقت ممكن.‏
ندعو الكويت إلى إجراء اتصال أولي بين الطيارين الإيرانيين وعائلاتهم.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/88307" target="_blank">📅 11:51 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88305">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">🇮🇶
رئيس الجمهورية: هنالك تسهيل لبعض البواخر التي تحمل النفط العراقي في مضيق هرمز.</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88305" target="_blank">📅 11:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88304">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية: إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/88304" target="_blank">📅 11:29 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88303">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇶
سوالف الگهوة
مراقبون يگولون تغريدة " لخ " أخرى إذا صح التعبير من ابو مجاهد العساف والجماعة حتى باميا للمواطنين بفرحة الزهره يوزعون .
النجباء مسوين شده يا ورد وزيارات وكذا على قادة الإطار التنسيقي مرتاحين لشوفة العامري حتى واحد منهم گال جنه يم هادي الكعبي مو العامري .
خبر " فصيل مسلم أشياء للقوات المسلحة العراقية و الأمريكان كانوا حاضرين للمشاهدة خبر حقيقي  " .</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88303" target="_blank">📅 11:20 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88302">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇺🇸
مسؤول أميركي:
لا توافق بالآراء حول حرب إيران وحل أزمتها داخل البيت الأبيض.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/88302" target="_blank">📅 11:06 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88301">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇮🇶
🇮🇷
مصادر إيرانية:
إيران تسمح بعبور عدد من ناقلات النفط العراقية من مضيق هرمز بناء على طلب بغداد.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88301" target="_blank">📅 10:09 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88300">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">🇺🇸
"توم باراك" بخصوص الشرق الأوسط:
أُرسل جميع الأنبياء إلى هذه المنطقة. ليس إلى منطقة البحر الكاريبي، ولا إلى أمريكا الجنوبية، ولا إلى أمريكا الشمالية. ‏"إذا لم يستطع الله نفسه حلها، وإذا لم يستطع الأنبياء حلها، فإن فكرة قدرتنا على حلها في العام ونصف العام القادمين تبدو ضئيلة للغاية."
توم باراك صار يكفر بعد فشله بحصر السلاح في لبنان والعراق واليمن وفتح مضيق هرمز
😆</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/naya_foriraq/88300" target="_blank">📅 01:56 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88299">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">🇷🇺
🇺🇦
هجوم صاروخي روسي وإنفجارات كبيرة تهز العاصمة الأوكرانية كييف.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88299" target="_blank">📅 01:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88298">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Xz0EaWzQFUYWzeEQP2QhB2V-dJPLyvSvUi6cDgWEZOGYvG7UbxUGg4h3B21jblU_kQxFxfQrrdIy9AJos72U6YF0RmaSm8AOMWFny9mBc6OTzKYn1d-WGShrFroPm4oDDE3ekVFi3IIebI6wJuy8afRxmaMkHH-1HpH1zn308pji6mW1JI4ziE5kP1i98j47GNrUTDzUKxA5j0B7CvqnkwFAmZ5RMSHDmsVIOq7iNxqmZsQ56bWwpNihEsG3CWUVQ8oaAl8F7hC6KgrY2el9NOpEORBGUuQV0GldLyNdPOuJ2Coet_mP3CqIZxWWGOruXLoHNYMKi6Ybgnco3bSFNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
طائرة مقاتلة من طراز إف-35 إيه لايتنينغ 2 تابعة لسلاح الجو الأمريكي تطلق نداء طوارئ على الرقم 7700 فوق الإمارات العربية المتحدة.</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88298" target="_blank">📅 00:35 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88297">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=AEvp27JDMrMJxl1STy-946yHblskrlmnds_i7RYNV2Q-gkTxmTWsC3fWQMxDkDR020y1hv_Njt_WBHjsvP20tfMHj_urlRyN_iLdLsxmefT-wj02y23TbNyMxogiMOlNT2i7MEZnO2-_Xy8zEKctlsOSIllK5ZH9xbo_6t2wDJrlIDBeQSTjRVI-lCO1AKp_oaAqwFmQKe1LjM5-0XDTebxGJj0eZuCZ3k4iR3IbrqEPax_epWF6UDLrQuTrK_mmtrhzfhFaHYKu1tUbCwiBSQJ16M8OxmULJ2KeX0euEwFTtRBbKNk4lvVjwxjWD1q8MiYqSoPjumlWnIaKOKbOCg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e124a7b79c.mp4?token=AEvp27JDMrMJxl1STy-946yHblskrlmnds_i7RYNV2Q-gkTxmTWsC3fWQMxDkDR020y1hv_Njt_WBHjsvP20tfMHj_urlRyN_iLdLsxmefT-wj02y23TbNyMxogiMOlNT2i7MEZnO2-_Xy8zEKctlsOSIllK5ZH9xbo_6t2wDJrlIDBeQSTjRVI-lCO1AKp_oaAqwFmQKe1LjM5-0XDTebxGJj0eZuCZ3k4iR3IbrqEPax_epWF6UDLrQuTrK_mmtrhzfhFaHYKu1tUbCwiBSQJ16M8OxmULJ2KeX0euEwFTtRBbKNk4lvVjwxjWD1q8MiYqSoPjumlWnIaKOKbOCg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب:  إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.  لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.  وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/88297" target="_blank">📅 00:30 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88296">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=DmvVFLxdVqvfOFfy0DhAGmbGJz4ekGxRnyHpl5PAjh7867FxHnCZ3Ph2W6mUpfODfycbWaPNcK0GzKXrjz9IwQddZwsxCjMXf63VC-k_NCG-M212j8-qKL_OuTFDQu63ZjCX6f3hvxLZtIqKgTZMKySbYwYzGJIgIsp7G29DCCEz2q0PQ6-ZCUIT8lcxrh5ckNfcGG8ZsiYIicknCSTkG9jyMfjcGMu3Q2wzWtyjTiCYZ1fb2fqv1wOfZ4XCZOmOvgFVvd-M6w4TLndCprnKUFAMGnestOI_k3YxbmKCsJX7lyTsurQpSLbclE9700tM13ZBiZcKfCxyA_8WRwpB1g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/97f648adb9.mp4?token=DmvVFLxdVqvfOFfy0DhAGmbGJz4ekGxRnyHpl5PAjh7867FxHnCZ3Ph2W6mUpfODfycbWaPNcK0GzKXrjz9IwQddZwsxCjMXf63VC-k_NCG-M212j8-qKL_OuTFDQu63ZjCX6f3hvxLZtIqKgTZMKySbYwYzGJIgIsp7G29DCCEz2q0PQ6-ZCUIT8lcxrh5ckNfcGG8ZsiYIicknCSTkG9jyMfjcGMu3Q2wzWtyjTiCYZ1fb2fqv1wOfZ4XCZOmOvgFVvd-M6w4TLndCprnKUFAMGnestOI_k3YxbmKCsJX7lyTsurQpSLbclE9700tM13ZBiZcKfCxyA_8WRwpB1g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏
ترامب:
إيران ترغب بشدة في إبرام صفقة لكنهم ليسوا مستعدين لإبرام الصفقة المناسبة.
لدينا سيطرة كاملة على تلك المنطقة بأكملها، وبالأخص فيما يتعلق بمضيق هرمز.
وهذا يعني سيطرتنا تمتد إلى عمق المنطقة، بما في ذلك المناطق البرية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88296" target="_blank">📅 00:28 · 31 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88295">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cED6ayK3CmDD8uJq-Bb9c94cg0q_FCM0h06RVgSe91OhcIsIazy_slkVUt6SofuJmDUiPeF2P8pRsdqepC3Y96Rjgb1ApoTe4Vx_IeeXyIuQZAn0jIp4HWT9UyziWEusPSQ6wtogTESn4QHZMXNBPFg0ndaVAENx8-vQhyRjyG2L59NkroDhQWn16cVR0YD-oInDBQ0niz6nB9uGDGMKkuebvgY5Ejxs8ml2YiX8V7gELC-f_wkX77he9KYbft6oHFznSYc_2y3CbmA9PrPrUsLcF0dGksSKvWN6u_R3jkC8HvM_tQSs2oXnfe6RMTSsa0EatYEB8__fE8rcAM3PQQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇺🇸
ترامب
:
نحن ممتنون لقرار المحكمة العليا الأمريكية.
المجمع العسكري/قاعة الاحتفالات الذي يتم بناؤه على الأراضي المقدسة للبيت الأبيض، وهو أمر بالغ الأهمية للأمن القومي، سيكون الأفضل على الإطلاق!
إنه شيء طالما رغب فيه الرؤساء على مدار 150 عامًا، وهو ما سعى إليه الجيش خلال المئة عام الماضية. قريبًا سيتحقق هذا المطلب!
الأعمال الإنشائية تتم ضمن الميزانية المحددة وبوتيرة أسرع من المخطط. شكرًا لكم على اهتمامكم بهذا الأمر.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88295" target="_blank">📅 23:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88294">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bvHaRZBhOqsVa88P_lh8YknocC2wNm5v9-tPsFheNz2WylBAD6T5q-LnpyT10BIPrWwkIQkjJwumM2-SmlS4DCq2c9nuRbqaNJ1behX7RzU5jwumJLnGGK0DVV1WZc58nikgWprJXvEd4zdder175a9tzD8Nd1tD5LJo2CJ9qWs7PrkqT1ue8GU9SIdCWCDZkrFDE4Jpz8Z739SZZKCU7C2TGABIByc_AhzjRDSUlC6wAl9xWiM6exdwQ6DfOaaVK9DCboWaLcX242XPacrOYxjNe4tL2zF1U8awsDQuTYnTIp7Y-Qjqez5hLpPQVLNVAEKaasBjNIqQ0jg3WYq4TA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇱
🇱🇧
الطيران الحربي الإسرائيلي يشن غارات على مرتفعات علي الطاهر في جنوب لبنان.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88294" target="_blank">📅 23:09 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88293">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🇮🇷
الجنرال وحيدي:
لن يتوقف الأعداء أبداً عن إضمار الكراهية والتآمر ضد هذه الأمة العظيمة.
سيستمر تعزيز إنتاج منتجات الصناعات الدفاعية والعسكرية، بقيادة وزارة الدفاع وجهود القوات المسلحة، بذكاء وسرعة ودهاء أكبر مما كان عليه في الماضي.
هنأ القائد العام للحرس الثوري الإسلامي وزير الدفاع بالوكالة بمناسبة يوم الصناعات الدفاعية في البلاد، مؤكداً أن الحاجة إلى الاستمرار السريع في استراتيجية زيادة القوة الدفاعية والهجومية باعتبارها الحل الذكي والفعال الوحيد لعبور المراحل التاريخية الصعبة وتحييد مخططات العدو الحالية والمستقبلية أصبحت أكثر وضوحاً من أي وقت مضى.</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/naya_foriraq/88293" target="_blank">📅 22:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88292">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MSMEmcWFVROSqcouSKZyLGvFRbdp9d3ExOg6fUWWE2c5u7hA_FHgwBNCzFZ-Ld3opJ1kg3ITDpV3wDlxdVmEoFI80mw2eKGp_boP4jGpxVD7bUpnS-pLOVABsC-YbYDfUe_e0-IQPhOEeaqVTX_QvApVA59ng7UHeahQbasbubhROZ_2L27CFOb-q-KKGio4LgAvoxC4eaLElnG0HqlvHX8tjG4jrqDcMKrR0QTD8gmuhfYTttq3XkWBA7-5WOP3KF_8dD5NLkGwHu4gh8Txkgwa3brzfBl9mdij2reJ6Ct7QHvIrVDHqJb4lxcaL5LcZnDGZJZZbanB1Oo4BFDwOg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
تفرض بدر نفسها مجددا في العراق كعرابة لمحور المقاومة على مستوى المنطقة
العامري يلتقي حركة حماس في بغداد تحديدا القيادي أسامة حمدان .</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88292" target="_blank">📅 22:27 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88291">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G1nutQaYI3GatG6G1swa7PqbX46JJZoHAvcRMH9YYmZ6KNxOTIm2FqCH-uWUITRi9hVk84OB69rPSmwwLbncR6dSN1Ml3X68euVEfBVsDTHD_PTdSAg2so9pALesvKKIM8ibAfQQlCIpN3e4OTrvYz3PzmnCTD3YYr0psbdG79zy-MWdEG14dAxB1HXTu_n5dLRhXkwIyNr139JYf0M0kuC-eUVuEScHwDgSITW-yGlO1jeTvEH8SveJ_xNYsbqCpDjUgJjC-hYl9enRk8xAhZnvTgvWabc36X3EGt645jiRMsGru1Lfzua8cI1v5PXiQAMlw7NGjujtgupw_f9ksQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">أسعار خام برنت ترتفع إلى 94.39 دولاراً للبرميل</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88291" target="_blank">📅 22:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88290">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JXYim0fvPJxP6qZw16kYrw4CUe5miTiXZJqHqVHiaMl9svaYtALBN3cYHsNplsywYaeC2mokC0Nn1s00HSWaCcE0D3w3k7TnMe00zGLsDMb2zYJ3L1BxIZfrTVWss_yJndeneEVuEgA2w8gyVyIAcu6Eebh19OynRBKLFISfS3rfo9IwxOuaRWkkeFnSwtCfo_3-9YvMpD-ab9k7YVUsw3NO-16wpVQ1MtftWHUhQC66Jfevnlpvl0biaywsdENpFYIH3ircPXZRhjckDpcPN8hULtqKnzyx3QYKq1r5lDba9XHfwSjIicnH-giixIedc6faDz-q0abJVpXUmRTOrQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
السلاح عزة وكرامة ..</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88290" target="_blank">📅 21:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88289">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🇮🇶
يودّ فرع توزيع كهرباء شمال البصرة إعلام مواطنينا الكرام في مناطق المعامل، جنوب قضاء الزبير وغرب البصرة، أن سبب انطفاء محطة المعامل يعود إلى خروج خط 33 ك.ف عن الخدمة نتيجة عارض فني.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88289" target="_blank">📅 21:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88288">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🇮🇶
طيران مسير يجوب سماء محافظة اربيل شمالي العراق.</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88288" target="_blank">📅 20:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88287">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس مجلس النواب العراقي:
رئيس الشورى الإيراني ابلغنا بأنه سيبحث استثناء العراق من مضيق هرمز مع القيادات الإيرانية.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88287" target="_blank">📅 20:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88286">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🇮🇶
نفت وزارة النفط العراقية ما تردد من اخبار في وكالات الأنباء الأجنبية والمحلية ، عن تصدير شحنات نفطية عبر السكك الحديد لايران ثم لتركيا.
واكدت الوزارة ان عمليات التصدير للنفط العراقية تتم وفق السياقات التي تعتمدها الوزارة وشركة تسويق النفط "سومو" ، ومن منافذ يتم الإعلان عنها مسبقاً .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88286" target="_blank">📅 19:06 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88285">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/c1_pC2dse2444Ae5_TFFPyt9mDoB1AtMg-cBV4fgRQXUM25xQUusogJBMmDWwdrXBXscgofx3iRC7Fjeeb55L0VU7Jyqxy-zdE-Ou0jDqHVCEBzuiRI9tayWgzefUd9ZS0gmozolCdopCyEpwjYHE-7vaeva2WGsOD2e8WVQzWSPg9rmy464IRqnfBcCErab5V5IkW12pOet_peLg-_gQM6Rhh5IOfd5vrA3YgYYFHNxOD3CbZqjxsbRW1HJV0TlmBhSVB1g9Kh7_9mqeroCO518mEfpDAIJ-zVu7pWb7wIocA2zhkBZMQ68U3TIV2gmGr2JNMQCn_gt9fUbK8BqzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🇮🇷
عراقجي:
قبل 14 عامًا: "أكثر العقوبات قسوة في التاريخ". فشلت.
‏قبل 8 سنوات: "أقصى ضغط". فشل.
‏قبل 5 أشهر: "استسلام غير مشروط". فشل.
‏اليوم: "أكثر عملية اقتصادية كارثية على الإطلاق". محكوم عليها بالفشل.
‏لقد شاهدنا هذا الفيلم من قبل. نفس المشكلة. لكن المتنمرين مختلفون.</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/naya_foriraq/88285" target="_blank">📅 18:56 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88284">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">🇮🇶
تنويه:
تفجير مسيطر عليه في منطقة البو حداري قرب جسر الإمام علي (عليه السلام) في قضاء الكوفة في محافظة النجف الاشرف وذلك في تمام الساعة السادسة مساءً.</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/naya_foriraq/88284" target="_blank">📅 18:21 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88280">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/V1YnLX1RAGm8FYxsBkuEs8uuGrfc-0Kw1aYvCWY4xQRJ0UVTu41KXMC005mogkZdUe-k0uDdIJeeoL4iehcX91wj1ukxFB2lMTrdYLvOt8sx8Xa0gTz5TLiNzGnAIJBaw6p6iCnc_fXu31QRYA2v4K-8gKrypft7TOqixGEErJPtNc3f2TFvhpuA0WdEq6WMgzLQuO0OtrcRID1CnD2E6c3zEveZu2PNbHW5U3k1PxfmU1xrESFqmN7dBrPpbVFenNmOKnsjl5hWE3LAqaBWWJ1OL3BT-WVXOGoaMFdmCIKdIU3ksWiWUjIlpGfk8n_SsAZ2E8GAGjZCVyf5G-Pikw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/aKxH1QObtUd_jffI3X9V4YihfSSLVidsHvUZOlinnzaIBvdJ5QMROqBUZUtMUTVCXbGBsYVaD_jHtjzPD0KNEF3QpkiZX10LhhOtVp4U_4f5GUZ8Mzr5XWnxyIsUmJDKahqV7adc2qg-en2WS7Xscwcyim8Vp9f5FNe4Ik5OyAUalNg1mHXHJi0Spho1HvvPuHXV5ptXzBu21HXzcqkhByyqu4x0SzjqCc1DVFh2zGvAZOdxFK1bld0ULZileZWyLUTiLeurjjTeHJAwdDquPfkHsGc5Uz3BziajktCgV3bZd1n4DaaZ3jIsCU-fvJhYTgt12aMUfPGI9P5zf8fMkg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WQCXQrVNnREyxry9HkIef0MkeCrJcddwrQTL9knQ9_5iVwOeTm1CKMDPkwpNf0yQmfCnU27PBt337Be7AQGqyFQtgt-9HHZUi-vGlW8n29NCRRKu3IlGwlyJF_k3P7iDWx2zeb3KCasMvHlyJ0JZ2nk3Q6mf5A-hXiF0nXrj1O0v3bk_3zwlaaIQ_ZsHkO9vHerJ9DcAcELdD1qThXmzykzNIWXavPDqWhVCYph-eJLmu5hY57NlHAdWKy2reAWps3-aYAIozpCERiX7MmfAIYwWGK05GZumOYTXiMAsX2jYfhCW3wsSMgL25uJbQkOZfRAunmy1xvoI4hBeBw0z9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rWgxsDZZdE8cxEyamf6tAiOY1CshVmGVF8j4NuL7m46f5Q_k6KIalv8K4SgY25ltCVx0EplQ9kLlZ274gq1fvbJvmwKFKl1cq9Rd2UHQ1lU9jByE77BNkeTNM1ZgX24LQQN_S4egLOrd2RFovktuaOaAFmyqDd_dtVwUSmQji0ar_uKmCSEVC-6ZXh6mqd4V5K57MH90_vfift-ksfy0t4gtTYYGGTGwj4p1NRpyU1YBWlSB3cnPcKhx5rXahlHfnztHk-UjCrPjmqsDPTsttfjDJtlTnV_xdjkFTvDhAj6p_2DDM4IYnXXcLC1AHsqjZZ-dRgNSUmOHdxAiv4zIOw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">مشاهد من الحريق في قسم الخدج وسط حالة من الذعر بين الكادر الطبي وأهالي الأطفال</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/naya_foriraq/88280" target="_blank">📅 17:48 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88279">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">انقطاع الكهرباء ‏عن ضاحية عبدالله السالم في الكويت بالكامل لاسباب غير معروفة</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/88279" target="_blank">📅 17:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88278">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88278" target="_blank">📅 17:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88277">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">اندلاع حريق في قسم الخدج في مستشفى النعمان ضمن العاصمة العراقية بغداد</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/naya_foriraq/88277" target="_blank">📅 17:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88276">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oUTm3QwH0DyLx-ohnT9QtHeYGmMNP_hffIPBfwA229TN6XVtp7aIZJXzyVk5HUUJwuvv8VJg9hUt3Q9bhH3ozyxfucV2bPe4kI9ESaReEAv4VJArt9qMBcjbaVWJezBZWSvclgCMnvgJdtAOvLTXwkZaWCQfG5ywZFBsEH02F-7tY2P4l6WrNPefGUdCbUKdusw7p09eKT66_j4-ncoFLLelJfsLTt__Mxe2Igf0VBpK92Wy-bDgikcdfTKMwPcI98VIfsR1dX-F3f3qaImMLL65EmIRCa1NkwHRtQF9iIvMSd2b5MA9GOltuZ1mGlXcIzJFY_JoIcCpM5ehPBh-CA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الاقمار الصناعية:
لا تزال حوالي 3-4 طائرات تزويد بالوقود جواً تابعة لسلاح الجو الأمريكي مرئية في قاعدة العديد الجوية في قطر في صور الأقمار الصناعية التي تم التقاطها اليوم. كما عادت خمس طائرات نقل جوي من طراز C-17 غلوب ماستر تابعة للقوات الجوية الأميرية القطرية إلى القاعدة لأول مرة منذ 12 يوليو.</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88276" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88275">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/naya_foriraq/88275" target="_blank">📅 17:08 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88274">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=u-9Z6hRiMO3ZXJcXsXG5wXf-_WkTAm_5HgM2LDXSBSDvH6vyhxScCYUvjHvu3-zwRVWSk13_0DltFxW1anyawKS6p0kpi9wBe8gczj0IrFNkg6bstram2Sq_DqGlRWkQTM_afvDhFfSSqcWJTVxkd4TIwUCMavsyEcwrphAjBg-WvoZ0rjBLsIO_PihgRawsae8laFce3XH_VWPeUi4tVSc6v-lhI4EZdtH-uOyK_4cCMMrFHf67gwNf7vm_wANGLf2AEBdaNctSaNVwM6uipnVXDegVIYzYXHwxmzCPItYm29oUF1GyeyAHlAEYsZBBMTslv1yAB4yW8Lfsf5GXDA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b4c39f9d48.mp4?token=u-9Z6hRiMO3ZXJcXsXG5wXf-_WkTAm_5HgM2LDXSBSDvH6vyhxScCYUvjHvu3-zwRVWSk13_0DltFxW1anyawKS6p0kpi9wBe8gczj0IrFNkg6bstram2Sq_DqGlRWkQTM_afvDhFfSSqcWJTVxkd4TIwUCMavsyEcwrphAjBg-WvoZ0rjBLsIO_PihgRawsae8laFce3XH_VWPeUi4tVSc6v-lhI4EZdtH-uOyK_4cCMMrFHf67gwNf7vm_wANGLf2AEBdaNctSaNVwM6uipnVXDegVIYzYXHwxmzCPItYm29oUF1GyeyAHlAEYsZBBMTslv1yAB4yW8Lfsf5GXDA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تزحفلي تزحفلي وفاتح ايدك</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/naya_foriraq/88274" target="_blank">📅 16:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88273">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=P8_ZoE5yKI36gNdhc6qEDV1e9Lmb6pjrivQJbNpikKTq_-kUMruYuRZqGPgKrbTu0-zPfw7LYPklRGdCpEk6eQEXQnQpP9vBcAbVaT3mxxCLri-fIJqKL2LAEwiVC-0MUTi6ZPCxikzYLFN88-kjskBdQ9KTcPzkiqBZLi8mwOOJgJLwtoGFrzIxEaU5HummIp1pba9b8tYZ_8hSbShYm10EFSR0istX1vpvpjq70ZGC1fFtpsdb3ChNEOUgNFkJ-vi5pl-duv1C3C27XNKNtRlYKScwsVRDSI7HLZzfYHp0gkY73_x8ww2IYyVaEOTVzkxksKt_6E7Lge3byLgGnA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e99c8dd0e3.mp4?token=P8_ZoE5yKI36gNdhc6qEDV1e9Lmb6pjrivQJbNpikKTq_-kUMruYuRZqGPgKrbTu0-zPfw7LYPklRGdCpEk6eQEXQnQpP9vBcAbVaT3mxxCLri-fIJqKL2LAEwiVC-0MUTi6ZPCxikzYLFN88-kjskBdQ9KTcPzkiqBZLi8mwOOJgJLwtoGFrzIxEaU5HummIp1pba9b8tYZ_8hSbShYm10EFSR0istX1vpvpjq70ZGC1fFtpsdb3ChNEOUgNFkJ-vi5pl-duv1C3C27XNKNtRlYKScwsVRDSI7HLZzfYHp0gkY73_x8ww2IYyVaEOTVzkxksKt_6E7Lge3byLgGnA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية: مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/naya_foriraq/88273" target="_blank">📅 16:42 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88272">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇾🇪
🇾🇪
القوات المسلحة اليمنية:
مشاهد نوعية لاستهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/naya_foriraq/88272" target="_blank">📅 16:33 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88262">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/af5GnDbhdatxx2D2eieQGwPZjgharEOQ5EqMmydIS_Fyr7wkEArIZA4gR-OFV620zghH2Pf3F2G5UpMpFUePuJqC85zIiRlNb3Ed1X-hV7RoZTTj4wxLvyEfVaqNF96nP3VAue6DYNiLAfVhszH6wmDQyUY2j_Yyr9TCAMWdCHaGyKDZtCnR5X0Qt8gJaOuRh3cPnz_kE-brwIpcziRmvg_bKc2xD0iF1GQKi5wHqAcDHeIpfQIwVIAsuYVq6cZ95uSpcjArP3E7MMNh2vmnFHKtx7yLk4sv_kGaRAe2EJH81X5eK2y3Z4nsUoqI6zYqcoldZmklYeouZsdPXfwhEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B5nYqd-2zARQOaLBOxyzF5mZtObP1dfp2sDDI7htjL4OSCCZn9mZzm9gEhNoFMd7mS8-vwxD8h7v8Wi9SPczemvL8xlZBf6Tr865ZTDIzhFsXAl4CHLvqyKw6lpbOQSjQXcQgwyBgrSl8-LVyZwwfqHyslBIh71aJL7ki8Y-kXnOtTzz78TtCXRF-AE1ss1-86WiED1fqkd5uOz-l-07fh_monJNx_kmQicaBNHfniHE6habr1Tx9_XA3_luOWYFaD6AMbHovwVlXCRMbHRn7ebQneELeKSNlKfUXaAv3_Bbb-w-byOAzrL9DllNA5lrhQwMdp3TObrvbHrWt-T1lg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/PuuR7SR1-Nhgk1Q3V7lV0pm8gFFxRCb1ttFu_IUNxM5xbSPlSt-nc1WxhF2GxtIIfrlCWjBUP-fvgPjDmMhVIpVRZUeoaSQXn_DWUpJcyd1sOnlbjTRMmae36yD74O0Vgfahhxzznlv1IvW_cgGY1jxG7Wphmt52YIt9J7j6bVm6I4snR9XAdbhPRSfYTv9CZa3qeFwM9Y9mOVunFeV-pb3ss11gd1k1ZXMjZq4aco20mICDsTGVll1NF3Z1YqtwgSuyvxlT4CNXA-Cf_ndE0CvCWfXws70e0WQHm-iOGygCPIPWMYxawt0RID88Vz5W55ieY6Oy3nIF5UmKV4_eRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eDdnNU4hYaAuZBt4gPEuH5PV2a-bfMoP_iDu8zu4xuz49gRoms8tpdW0EdmPX5NVBF4EdKnGm2-4-3fa38ZUhczmsEd0u5_WA3yrjuxITC2pcntzuAS389sW73DGi7RU0VGjmUo-APjFNaq1m9_PV5jjRD5R32JPnpyUMVagGeLiQl5iwYPdPkd0YkQst617iur1LYkCXjn12GsJ3mHeiPuIeKVlz7Vdpoq6AZtR7LLJz03Vkwro_xdtioDRwFZ_5KkXYr5RNVi0HNL3iVHanrol4Z7MPUfRnqhY0GYmMD2VcKY-065ass1lJtdWhmURX5trPa9jbAo5CYPQdKNZwQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/JIAyr0c2H-lZkB9_OEKTWMG4FhKtnKpZoE_1qtahJ93pGlmRl1_qKP6f9ZeAeFYWgLCbr5W3VOtlTrzSs0dZZKUiUwBSkmJ7g0ooagKKOH4WuDD8tIWWyx_fIJ-wghsA8cNvKOjUfYfvf2THH3zXCIZ1uuSBF7eBWZ8M7eJH_j_6Eb2U1K49QxLn7MmHfHImPSg_zuGa_SHNoj62yEiUz5yoQ12G_ssIKo0uQfr5ncosFBxWDpP7n2eLhTthyQbdQpvkRndMBM4yU5hGp4P4NkzvcmQDOHwrTVwHt1TjyOvJSTCCwOLAJLzT1eqUWe0JZU6dc7CIbXK1PLKgj7lkLA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/B0X3e9rZaPWZhApFOaNmV_qFnRyujUUUdMKS6J421_WnyjjALSzncWTfGpqoIFDca_Uz-x3FmxVJRKqrA0rXL5ELIXSL1xCgZqxlLWZMFG8IiCVqlTfPSwxiKzIXkLVHMQy0r1Z5NFKKVAnch9ij-wntFH6ni10dTPP-yytjwBhuoBwMG5Gsuug8g4HNCn2J9xogWADIhie7Bgw8qP3euUoRaX3FO2RkafFUXJUv1Fjg0HVJN9XWfRjIvQEx8sdD1XQUMdUOEVv4XCi8Yg9h66FjgUXjGWkcK1clRtAAVbfZkV11tmhxIKd6-HYj_slWemm7GwKRVHCmu-8UfmYCDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/L43SROVvgEYnFvRQMjZti1B57bwu631ciRfSyLLcRiJxspjECogg741NJV5uo_TSxdgzgrxeB2EOiK0XAkdUyjs5o4FmLuqM2_tzf00G9K0Rdq2hu9eaUXbMcvIQfDX2rJnDx-KRO_kZm5qU0ScwF8h3LzsjnY3sEQqH6Fw2zHpLbKBRwUkcLnCck1XUCodAu67_sMc4IdFiCdbsAERd8cZVZBCnp7Lr9m0uh7J3pJ8Nj3fy3gQX2jadOSNhuBboNR6XczVzTlQoTx5pdS05WRS9aY2aqMy5td7tRUrr92ch1pqe9K-Mqz869jIt-BfhpWfm485EgZuBP9DYWBYnbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/efe0V1zmzNB-dBGMMsdGbziupKlTFUNy6Q4zFz0RPlQVdSgLDENa1wktBwz5D3u4c3463QUBexrrGTBfjwfTkinAkYZf-KFiSe9NfjVvVdU6M3pUYG-fw4gmBi-3txV_HrEO1Y57gCr-HQaW8cEotHr85OxBy1G9Ez8YxeI10dm3qpwcJkw0gSpLYC4NbNldXdL0HSr8MqXd2LGQeSJemjQjOu3z4sczZxDlJLwHrrcYm1-pGBRcYeW-OZTSGs-8OjuRq17DOauR77HV9C4YBIzX8iIWETIYdMlJ0bdtR-cb8DLpqf4pZ6dH5M-cU7REfA8lDMv8Re3xjBZFWaAbug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lGfEo5Z_-lHzZVKP5goZICIvI8vsfw423R9ujLRtZJOJl2PxNqJtS4Y8F5Zz-H5WPm606C4JIQrioKMeZ0g9zoulkKJqnU6MkLXCzAqeGTG4XJdpEA22PqH7gzsBuJLI1FCYkAQzRmO2kxgDTyGXEoipSOMHZ7PkTS2_EP6J137AwFccrOybNk3NkaDqIEvpSfxWkQ3_tP4dhi1XPKGIuBQubmS6073HkOUrxflEKUOZwG8_iK0MHqFsDInCt_ki74sWLMgFJzP3HlaE1AmllIqPFbcwokvuA_t15l1lZIX7TeUj6oKDBQgk3wxwrau3rSH4Ti1LmAfAoWwa4BykBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/TGwvUNNjaEv_D5bB0g6ibPXUxTn_m-uOEaV6hzfeKMVqG_-5FW92yrsZikRwsoIQv8pC0yfeXOLn5iSdyJMUjLiyClXp9vbTM7pUVClw7wy0LsRM853ZS_8mkRM9TZI6TpwkaiFA2ZS2JmNTvdZiS73EMX2-RrJ7AGJuSBme_6xx2tBj2VVCBHoGTu3szGLZrK-UY8qzw55gbLTJKf_3-A1dT9LeClU03pxTU7H1l65o6wsnu9g_IYPUa7OXHoB0m2wPonmkC9Pe63kOA6k3gAbOl_Q25KFNjcIpNSegBJhuF7suuI1gbf9W9UvZQlJS2hiGC93XzVrxeXrOnpsYaQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">القوات المسلحة اليمنية:
صور من استهداف تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيرة في مأرب والساحل الغربي</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/naya_foriraq/88262" target="_blank">📅 16:30 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88261">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/sN6bysPFGQlHz8QmZmLvoqWx1uONeI8b-TvH02icYYo17y_2T-g5e0jtEM77MjwoEXpIZG3oeHN-9iz15KbRwqpX5QXPVaKO8AKe2aCAfzeu_rRMt1pfIDOBKBSMgzZK4n7mCOvniRBguzatsJSG4VbGsudUePv0S-gGBKv25FVO0xyjD8UBJDrEVqY2wSFbvAXSwOf1u_w3myWjI3LXEwqG-v_IM7sEwSG8qFXKfvBPyzsIfRDDIdWNOuUTyNdzHHawPBJ6j3GKn646s5tZQi1iGABulMYAK-VVE40wI-fFmI-Kb6krE-SxKUKL1QmLBxl1mGNS970J1j7blmGaiQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏اندلاع حريق هائل في مستودع بالمملكة العربية السعودية قرب الرياض منذ أيام، ويبدو أنه يتسع نطاقه باستمرار، حيث تجاوزت قوته 200 ميغاواط. ويحرق الحريق بشكل رئيسي الأخشاب ومواد أخرى.</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/88261" target="_blank">📅 16:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88260">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/98553c859a.mp4?token=G5MZnvsBJnFtmwZ5wg0ks4HfeXseB1rB-Y6-cSqiiECtmmIljKHB8R-m_feR7hLlycsh5p6Sb7NcOtMRqpTSFZOQ5YyK6k4m0uSKcsepE43jFVsV6lCJeJoFd6OXn_5ztdOyaKbnX0Rlq9LlMYi8XqEGVNkXZLzdepEkUSLYitB309rCxnSfFJ1JlTedDEbf3F-8fl2RjEityR2AU38ttIOezu4Mu6eBVsCpCRQzEqC4DhUiPPRoz21UCLkss_yWc2hK4ieNtvwCtUuPsmetc1e54FqoAFqpHhfQDBQReiOyxFXzcU09lPyhUsdp6ZVrgcxOSWOqQpA66IhGK1FLQw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/98553c859a.mp4?token=G5MZnvsBJnFtmwZ5wg0ks4HfeXseB1rB-Y6-cSqiiECtmmIljKHB8R-m_feR7hLlycsh5p6Sb7NcOtMRqpTSFZOQ5YyK6k4m0uSKcsepE43jFVsV6lCJeJoFd6OXn_5ztdOyaKbnX0Rlq9LlMYi8XqEGVNkXZLzdepEkUSLYitB309rCxnSfFJ1JlTedDEbf3F-8fl2RjEityR2AU38ttIOezu4Mu6eBVsCpCRQzEqC4DhUiPPRoz21UCLkss_yWc2hK4ieNtvwCtUuPsmetc1e54FqoAFqpHhfQDBQReiOyxFXzcU09lPyhUsdp6ZVrgcxOSWOqQpA66IhGK1FLQw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">الاقمار الصناعية تظهر أضرار جديدة في مصفاة جازان النفطية جنوب السعودية، وذلك عقب غارة جوية شنّها انصار الله بطائرة مسيّرة في أغسطس/آب. وتؤكد صور الأقمار الصناعية الجديدة أن خزاناً نفطياً ضخماً يقع عند خط عرض قد استُهدف، ما أدى إلى اشتعال النيران فيه.</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/naya_foriraq/88260" target="_blank">📅 16:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88259">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
تعرض موكب ابن السيد خضير المطروحي، قائد عملــيات نينوى في هيئة الحــشــد الشـــعبــي، إلى حـادث سير على طريق بغداد</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/naya_foriraq/88259" target="_blank">📅 15:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88258">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">في اول رد تركي على القصف قرب الحدود التركية.. ‏تركيا تصدر مذكرة توقيف دولية ضد نتنياهو بشأن أسطول غزة.
رد مزلزل</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88258" target="_blank">📅 15:36 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88257">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🔻
بيان صادر عن حزب الله
:
خرجت علينا الإدارة الأميركية يوم أمس، عبر وزارة الخزانة ووزارة الخارجية الأميركية، بادعاء أن حزب الله خاضع لسيطرة فيلق القدس، لتبرر من خلاله سبب إعادة إدراجه على لائحة العقوبات، في قرار ليس في حقيقته سوى حلقة ضمن سياسات الإدارات الأميركية المستمرة لاستهداف المقاومة ومجتمعها وبيئتها ومناصريها ومحاصرتهم والضغط عليهم سياسيًا وماليًا وأمنيًا، بهدف حماية أمن العدو الإسرائيلي وترسيخ احتلاله لجنوب لبنان وفتح الطريق أمامه لتنفيذ مشاريعه وأطماعه التوسعية في المنطقة.
إن هذا القرار القديم الجديد الصادر عن الخزانة الأميركية، يؤكد أن الإدارة الأميركية التي اعتادت استخدام العقوبات وسيلة لفرض سطوتها وإرادتها  على الدول والشعوب، ما زالت تتعامل مع لبنان من موقع الوصاية، وهي بدل أن تذهب إلى إلزام العدو الإسرائيلي بالانسحاب من جنوب لبنان ووقف اعتداءاته وتفجيره للمنازل وجرفه للحقول وقتل اللبنانيين، تذهب إلى حصار اللبنانيين وتعمل على تجريد لبنان من كل مرتكزات القوة، وهي بذلك تسعى إلى إحداث اضطرابات داخل لبنان وتحويل مسار المواجهة مع العدو الإسرائيلي إلى اتجاه آخر.
إن حزب الله لا ينتظر شهادةً على لبنانيته ووطنيته من أحد، فتضحيات آلاف الشهداء الذين قدموا أرواحهم من أجل لبنان وشعبه، والتاريخ الطويل من المقاومة ومواجهة الاحتلال والدفاع عن الأرض والسيادة، هي الشهادة الحقيقية على لبنانيته. وإن علاقتنا الوثيقة والأخوية بالجمهورية الإسلامية الإيرانية هي علاقة نعتز ونفتخر بها، لأنها وقفت مع لبنان ودعمته وآزرته لتحرير أرضه واستعادت سيادته وحقوقه، وبقيت إلى جانبه في كل المحطات والأزمات، وكانت من أولى الدول التي ساهمت في إعادة إعمار ما دمره العدوان الصهيوني إبان حرب تموز ٢٠٠٦.
إن الإدارة الأميركية لا تملك أي أهلية أخلاقية أو قانونية لتصنيف الآخرين ولتوزيع شهادات الوطنية عليهم، فسجلها الدموي الاجرامي من فيتنام إلى أفغانسان والعراق، ودعمها اللامتناهي للإبادة الجماعية في غزة، وتغطية جرائم العدو الإسرائيلي وما يرتكبه من قتل وتدمير في لبنان واليمن وسوريا، وعدوانها على الجمهورية الإسلامية الإيرانية، ودوسها كل القوانين والمواثيق الدولية، وضربها بعرض الحائط كل القيم الإنسانية والأخلاقية، وتحويلها العالم إلى شريعة غابة ينهش فيها القوي الضعيف، يجعلها في موقع أم الإرهاب في العالم، وينزع عنها أي حق في أن تنصب نفسها حكمًا على العالم وشعوبه.
إن كل تلك العقوبات والتصنيفات الظالمة لن تثنينا عن التمسك بخيار المقاومة وبحق لبنان واللبنانيين في الدفاع عن أرضهم وسيادتهم وثرواتهم، ولن تغيّر من حقيقة أن المقاومة كانت وما زالت وستبقى جزءًا أصيلًا من تاريخ لبنان وحاضره ومستقبله.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/88257" target="_blank">📅 15:24 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88256">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🇾🇪
🇾🇪
الإعلام الحربي اليمني:
ترقبوا الساعة الرابعة عصرا مشاهد نوعية لاستهداف القوات المسلحة تجمعات وآليات تابعة للعدو السعودي بطائرة رجوم المسيّرة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88256" target="_blank">📅 14:58 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88255">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">استهداف منزل ضابط في وزارة الداخلية العراقية رفيع المستوى في منطقه الزعفرانية جنوب العاصمة بغداد</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/naya_foriraq/88255" target="_blank">📅 14:17 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88253">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:  إغلاق مضيق هرمز يمثل تحدياً كبيراً.  العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.  جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/88253" target="_blank">📅 11:50 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88252">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇶
رئيس الوزراء العراقي:
إغلاق مضيق هرمز يمثل تحدياً كبيراً.
العراق يمر بفترة عصيبة ولدينا أكثر من حل للمشكلات الاقتصادية.
جميع القوى السياسية متفقة تماما على المضي في حصر السلاح بيد الدولة وجار العمل على آليات تسليم السلاح وإنهاء هذه الحالة تماماً.</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/naya_foriraq/88252" target="_blank">📅 11:43 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88251">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">🔻
مؤسسة "سي آي إس":
أن الولايات المتحدة قد استهلكت حوالي نصف مخزونها من أنظمة الدفاع الصاروخي قبل الحرب، وأنها تمتلك الآن ما يقرب من 800 نظام "باتريوت"، بينما تنتج روسيا وحدها أكثر من 100 صاروخ باليستي في الشهر.
يتزايد تساؤل الحلفاء في أوروبا وآسيا والخليج عما إذا كانت واشنطن تمتلك القدرة والإرادة السياسية للدفاع عنهم في وقت واحد، وخاصة تايوان وحلف شمال الأطلسي.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/88251" target="_blank">📅 10:57 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88250">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">🇮🇷
قائد هيئة الأركان العامة للقوات المسلحة الإيرانية "اللواء عبداللهي":
القوات المسلحة في الجمهورية الإسلامية الإيرانية، بفضل استعدادها الشامل والحديث في جميع المجالات البرية والبحرية والجوية والدفاع الجوي والفضاء والسيبرانية، ستواجه أي أخطاء حسابية وتهديدات تقليدية وجديدة من الأعداء بردود ثورية ومؤلمة ومدمرة.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/88250" target="_blank">📅 10:54 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88249">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=Jnx6bNNY6-PKgwbtoySjhP0jGXDoLs6iGH9HXvqZ64gfMYnxvUWHdVscfc5Znj4979oByBE-Yjvclf3JZuxot7mldS8uwFgsU7SC4L-rjVjaBdvD44G-VsdsSM-SuNAie6uPFI_5UJfI-8BKvYLFy4-I9jpUreR2OTxAVzoC6JAkGtbmrr-dcMcKxhCfKgK5DiU8RM-JyPhNwuPD4jtWKdPgJdhLx0RH1_TEVAYkDhU4dqBzdhs6QiJfvvqZp1ybF6okUFbYLJuDr_UhVPwjtjolAp51jLa-iyuizbsal8j6BPj6u4L_ixRlTmObbTfoYxSyEKf_oihH3oSrd7U0Eg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a23d5a7c74.mp4?token=Jnx6bNNY6-PKgwbtoySjhP0jGXDoLs6iGH9HXvqZ64gfMYnxvUWHdVscfc5Znj4979oByBE-Yjvclf3JZuxot7mldS8uwFgsU7SC4L-rjVjaBdvD44G-VsdsSM-SuNAie6uPFI_5UJfI-8BKvYLFy4-I9jpUreR2OTxAVzoC6JAkGtbmrr-dcMcKxhCfKgK5DiU8RM-JyPhNwuPD4jtWKdPgJdhLx0RH1_TEVAYkDhU4dqBzdhs6QiJfvvqZp1ybF6okUFbYLJuDr_UhVPwjtjolAp51jLa-iyuizbsal8j6BPj6u4L_ixRlTmObbTfoYxSyEKf_oihH3oSrd7U0Eg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🇮🇷
رئيس البرلمان الإيراني خلال زيارته لمرقد الشهيد القائد أبومهدي المهندس، يكرّم عوائل الشهداء الذين ارتقوا نتيجة العدوان السعودي الأميركي الغاشم على مقرات الحشدالشعبي.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/naya_foriraq/88249" target="_blank">📅 10:31 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88248">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.  #أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88248" target="_blank">📅 10:16 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88247">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🇮🇶
🇮🇷
حضور رئيس البرلمان الإيراني محمد باقر قالیباف عند مرقد الشهيد أبو مهدي المهندس في النجف الأشرف.
#أخوتنا_قوتنا</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88247" target="_blank">📅 10:07 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88246">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=R-t9whcue2BZx2o2kqVdBC89YmktYn6pTAPuBiSKEPrvlEfSkiqpbFScB-c04DEeKOB6Nop6Evish3O32y1vi4RfLdgKc8vfcVc9umiL_6YbeKaGB5fnGSo_d1jx5SgR0nfNnJoUOkSsUAWyn0mmFp8yJ5BD6mswvIfDr7w0useEBo-04W6s0jDjOWY_V23IIgeWwaRi-3JlASEw3yzlVafpDQUMOhzlRTReLnpEX2NxesirygOmRsqnqwjNq6RrSVJwTjqEgdhL8TEZOC1v_zweMX14jtI1VpW4t_SNrZasbUnKL62aojRRGmCQhx665YxVlYYBsCBfpeTWyC-UPiCUXIHQ_-6Bct18ooX03b7fX-9ZEoIrBesLwYOsVexp9d2kmzlKD_G9gASSeym25j2wr88K9Oqr5rJM_5IthysW1d6ZRaDASoX6m5_36shwJpkUCwME-OrppIVov0jXSr1o8DYWwyZAPj2BVz4jHnoi_VKhvWhvbNYSqjvYFhZRUIGtWCBbwscmNLQnGRyP0XbS61nryD5H1WrjR5ffCc_DPw5RK8vTqu6XDkaBIwbEIFbHAaKvE-IAX6j5SWroqw6ZwTe22LsXpb5Q7NGpsf1jl_krqI2odWQunVZvYSEXOlKD3sRX9XWwHAsuDKg8v0p1BenCbLCbauCY-4788Dc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2a0ca47031.mp4?token=R-t9whcue2BZx2o2kqVdBC89YmktYn6pTAPuBiSKEPrvlEfSkiqpbFScB-c04DEeKOB6Nop6Evish3O32y1vi4RfLdgKc8vfcVc9umiL_6YbeKaGB5fnGSo_d1jx5SgR0nfNnJoUOkSsUAWyn0mmFp8yJ5BD6mswvIfDr7w0useEBo-04W6s0jDjOWY_V23IIgeWwaRi-3JlASEw3yzlVafpDQUMOhzlRTReLnpEX2NxesirygOmRsqnqwjNq6RrSVJwTjqEgdhL8TEZOC1v_zweMX14jtI1VpW4t_SNrZasbUnKL62aojRRGmCQhx665YxVlYYBsCBfpeTWyC-UPiCUXIHQ_-6Bct18ooX03b7fX-9ZEoIrBesLwYOsVexp9d2kmzlKD_G9gASSeym25j2wr88K9Oqr5rJM_5IthysW1d6ZRaDASoX6m5_36shwJpkUCwME-OrppIVov0jXSr1o8DYWwyZAPj2BVz4jHnoi_VKhvWhvbNYSqjvYFhZRUIGtWCBbwscmNLQnGRyP0XbS61nryD5H1WrjR5ffCc_DPw5RK8vTqu6XDkaBIwbEIFbHAaKvE-IAX6j5SWroqw6ZwTe22LsXpb5Q7NGpsf1jl_krqI2odWQunVZvYSEXOlKD3sRX9XWwHAsuDKg8v0p1BenCbLCbauCY-4788Dc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
🔻
جرف النصر للموت ما ننطيها
لقطات قليلة التداول تنشر لاول مرة تظهر جانب من استبسال كتائب حزب الله وسرايا الدفاع الشعبي في العراق بعمليات تحرير الناحية ومنطقة عزيز ويس والفاضلية بعد فتح ساتر ياحسين باتجاه قلب المنطقة .. اللقطات تظهر استخدام الصواريخ الارتجالية الأشتر وصواريخ ال 107 ما تعرف بالكاتيوشا و ضربات ايضا بصواريخ ال SPG 9 و ال 106 إلى جانب اشتباكات من مسافة صفر بالبنادق الخفيفة والمتوسطة .</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/naya_foriraq/88246" target="_blank">📅 09:10 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88244">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
ترمب
: لو كانت إيران قد امتلكت سلاحا نوويا لكانت استعملته ولقضت على إسرائيل وكل الشرق الأوسط ، لدى إيران بعض الصواريخ والمسيرات لكن قدرتهم على تصنيعها منخفضة للغاية مقارنة بما كانت عليه قبل 5 أشهر، إيران تحولت إلى قوة متسلطة في الشرق الأوسط تتنمر على الجميع.</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/naya_foriraq/88244" target="_blank">📅 02:04 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88243">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=Yns2DyKPZ5IGfIarSZRBzRc1BI1_5nxulv33n8Vj0i1C6F_foMw6GKAx1ZAndeeZU7zwV34OiX9G7DPjYGeKAJMy-alpRsW_xz7hrvG3IVqZiJvynIex-URPO14XIN5uRb8Shzl1y0_uEPuYIdaNB5Ag-E55Ah2-oUFwdxymuwu1OX6j8uISAxQtAdxKCBt1ThEFqYOXaPbzKq4E__zPFmekZdyfp1yD3NnO9ZAdJSkkJ_XW4hMywYBFUVBAMbTf68AayQg6e3_SexojSeGhmyyDwbyEeWwDKWmUqOD1wO056BRRSuiAQq5LX7Tz1R_E6fmxgZH4BqDGefyXO7Hd4Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9042a34cec.mp4?token=Yns2DyKPZ5IGfIarSZRBzRc1BI1_5nxulv33n8Vj0i1C6F_foMw6GKAx1ZAndeeZU7zwV34OiX9G7DPjYGeKAJMy-alpRsW_xz7hrvG3IVqZiJvynIex-URPO14XIN5uRb8Shzl1y0_uEPuYIdaNB5Ag-E55Ah2-oUFwdxymuwu1OX6j8uISAxQtAdxKCBt1ThEFqYOXaPbzKq4E__zPFmekZdyfp1yD3NnO9ZAdJSkkJ_XW4hMywYBFUVBAMbTf68AayQg6e3_SexojSeGhmyyDwbyEeWwDKWmUqOD1wO056BRRSuiAQq5LX7Tz1R_E6fmxgZH4BqDGefyXO7Hd4Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
سفير بريطانيا  لدى العراق عرفان صديق
▫️
‏نوجه رسالة الى الفصائل سلموا سلاحكم وستكونون أصدقائنا مثل احمد الشرع.</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/88243" target="_blank">📅 00:52 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88242">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/naya_foriraq/88242" target="_blank">📅 00:22 · 30 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88241">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FAY0KgyB6PNy4OU1cgp5VMPtkefIKAi6wzW3jDRGnE9TMtd-XGLkMqFzQUbB2LMy4Pc41RkLrl9O9doXkjsF9dEom8gCTdGnMULHL1SPXjW-wlm9TmNUIG1YyGaKI3IpLWF3EeiquziP3mStGwSCUUUnyrmHZysSatCwTM8GYkZ7B_uwNhzQJoUMVEz1-HyGiX9TOitrSVZMeK1ebvcg2R6WBx5faz89WOapi9SvcDjqYEtMDJZ9wMonka67FO0WvZ1vY9dDWMZk2L35V0INlMPUNYk1XsmQb09645hz8xQ3RbI8Jy9wbtS5mLiJxdwy22XCQfA7gs0Tn0VI3jW-ew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇦🇪
صور اقمار صناعية تظهر تضرر بشكل كبير في مصنع مواد بترو كيميائية في دبي بفعل احد ضربات الصاروخية الايرانية.</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/naya_foriraq/88241" target="_blank">📅 23:52 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88240">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lSPPRrJ3M7EfeCDDD0GrdVtP3yrF7wFEfly4XMIp-x2Cl3XI1-3jWgATbmAmtp34ISEAbTfvsYThoodPO_Jfpr6-wcFyd2Nz02G9HgAocJ4UFG3vEBCG4zTNU0pO0Kp8dAiAPyoqNjwnIH9nFgKtN2QbvPYlwDzCbgSXkLipLD7P_qX2evtvuCnAlyyBuv99edipw7cbiNHbbfCybE55uRc5Ru9Qh1f1MvZw1IcnOWQZyDlqkLLWu-9r4dAHNoeqDdc3JFOyOWm2a0kGdx7SXxxJLTZ3_laGcBHgdn9eVpmn6zHi8-ozO4qVd5ZM8ZjonDfoFuP5qq9uPhYRCERz1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
🇮🇶
مشکل، به‌طور خلاصه، تفاوت در سطح فرهنگی و علمی بود
پس از آن‌که آمریکا دموکراسی را برای عراق به ارمغان آورد، عراق بر مبنای قومیت و مذهب تقسیم شد؛ نتیجه‌ای طبیعی از سیاست استعماریِ «تفرقه بینداز و حکومت کن» و نوعی الگوبرداری از وضعیت لبنان. با این تفاوت که در عراق، رئیس‌جمهور کُرد است، نخست‌وزیر شیعه و رئیس پارلمان عربِ سنی.
مصیبت بزرگ‌تر این است که طبق آنچه گفته و نقل می‌شود، رئیس پارلمان رانندهٔ کامیون تریلی در مسیر الانبار–اردن بوده است. یعنی در همان زمانی که قالیباف هواپیماهای مسافربری را هدایت می‌کرد، این شخص مشغول رانندگی، تعویض روغن خودرو و تخلیهٔ بار بوده است.</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/naya_foriraq/88240" target="_blank">📅 23:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88239">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nV5yZIjHkg-Z6YDKG6i4oldyH4kVJCn_oFzFuBN630nXGLeMBhAJHSLSseY3iQF1ydvrXVfjwChD6uw_RTEVbcsqbs_vDnIKfPAJwCm-MadPR1XX8PZ_t3QpOhpyPNtJmX-SRhG2d6qQR06uHmQfxkD_IIvipDRXfqdeKJMS6wrBgoHso9jS1vYHT02wYm8xvrt2TXok2j14V6hKDKjxLySO6MDkv0gqfH3fvGuADm_PvV1881D6OSK5sjWsGSHhkyAJO96VhEg01Y7FOVz56YOHYG2eAerTgfDsviKhux5rbvhe3J-wd1FN-KkO-oXe78rAspC3li4pEop6RZCtTw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ربما يسمح بالنشر ..
🇮🇶
🇸🇾
🇸🇾</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/88239" target="_blank">📅 23:40 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88238">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=JABA4aZ-unv9qriIfD9AFqKIqJwfgYpDQZoFglLHUKUGR6HQ3i5roFOPfGvzP3GVcE_2eU2dCOu6sjbsNjrX8VpV5R-jO--6lKy4FU2shuWeUqwfvN1pm6t0WY8_7Y8uI_DFviIhV1evtcwjh_4QV9fOB3Ik8_HSwxANCXlToencgoiKzasm-sZy5jVbE-J99ynMUOJrMEkCuwf6Q2AxuPln6s8PzrzDPdSCm3nifQyrila6gdDm9_FvagZosQD-tWHjZXUO_ar7QwhjaBXP6hW_1zq-oTpx2ty6bUhqmry_bqE5k1SNhxctQ86xWATp0BmC_qzdJsWhm3G46IDXUg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ba39abc2c2.mp4?token=JABA4aZ-unv9qriIfD9AFqKIqJwfgYpDQZoFglLHUKUGR6HQ3i5roFOPfGvzP3GVcE_2eU2dCOu6sjbsNjrX8VpV5R-jO--6lKy4FU2shuWeUqwfvN1pm6t0WY8_7Y8uI_DFviIhV1evtcwjh_4QV9fOB3Ik8_HSwxANCXlToencgoiKzasm-sZy5jVbE-J99ynMUOJrMEkCuwf6Q2AxuPln6s8PzrzDPdSCm3nifQyrila6gdDm9_FvagZosQD-tWHjZXUO_ar7QwhjaBXP6hW_1zq-oTpx2ty6bUhqmry_bqE5k1SNhxctQ86xWATp0BmC_qzdJsWhm3G46IDXUg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ملانيا زوجة ترامب تظهر:
سمعت أنكم اشتقتم إليّ. ها أنا ذا.</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/naya_foriraq/88238" target="_blank">📅 23:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88237">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/660318801d.mp4?token=RLsqolOM2CSqufu0zzEU60QTCG7gYwsZFn8DrOuSXOJzNhj7iMJGFgOmvz48T5smx3QKnt4Rwv1hVa6-jWLHQ_bRpLQ0q7eKuJBkAwHDCSK7aF1RZv2bb9ybQvNHm-q8PbkL0o0D8S6xw6vRP-xLpkC5sjTCvzlu5CS36zfRg6YARSrGMU3aC4qfzowDgVLMsnDhrq8zUp0xuTC1EJBbHvPMsJ21-l9m-3iAvtpkNQ0M5YnOEAhedPmoaPhsRCRibEVIK2nbL-HE5JbOY7m09mxWbTu1c6zHdWLGo3G-TFYjxKJA_fAJgJxlPhz5KEbbfsTYUQvQUIY2y_Ml4fffNg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/660318801d.mp4?token=RLsqolOM2CSqufu0zzEU60QTCG7gYwsZFn8DrOuSXOJzNhj7iMJGFgOmvz48T5smx3QKnt4Rwv1hVa6-jWLHQ_bRpLQ0q7eKuJBkAwHDCSK7aF1RZv2bb9ybQvNHm-q8PbkL0o0D8S6xw6vRP-xLpkC5sjTCvzlu5CS36zfRg6YARSrGMU3aC4qfzowDgVLMsnDhrq8zUp0xuTC1EJBbHvPMsJ21-l9m-3iAvtpkNQ0M5YnOEAhedPmoaPhsRCRibEVIK2nbL-HE5JbOY7m09mxWbTu1c6zHdWLGo3G-TFYjxKJA_fAJgJxlPhz5KEbbfsTYUQvQUIY2y_Ml4fffNg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا   اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/naya_foriraq/88237" target="_blank">📅 23:11 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88236">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">🫡
أنا تحت راية أبا الفضل العباس
We will never forget Ya Abu Fathel</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/naya_foriraq/88236" target="_blank">📅 22:47 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88235">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">رويترز : قال مسؤولون كبار إن القوى الإقليمية لكرة القدم في العالم تناقش إمكانية طرح اقتراح بحجب الثقة عن رئيس الفيفا جياني إنفانتينو بعد أن أغضبهم بخططه لبيع حصة في كأس العالم لمستثمرين من القطاع الخاص</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/naya_foriraq/88235" target="_blank">📅 22:20 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88234">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🇮🇶
مصدر امني لنايا
اشتباكات عنيفة شرق العاصمة بغداد في محاولة اعتقال احد قيادات جيش المهدي " ابو درع اللامي " .</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/naya_foriraq/88234" target="_blank">📅 22:07 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88233">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">زلزال قوي يضرب بيرو بدرجة ٦٫٨.</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/naya_foriraq/88233" target="_blank">📅 21:37 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88232">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">🇺🇸
حدث امني خطير في امريكا
اعتقال امرأة للاشتباه في تخطيطها لتفجير قنبلة في مبنى الكابيتول بولاية نيويورك .</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/naya_foriraq/88232" target="_blank">📅 21:28 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88231">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">🇮🇱
🇹🇷
الاعلام العبري:
المستوى الأمني أوصى بالتهدئة مع تركيا وعدم فتح جبهة إضافية.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88231" target="_blank">📅 21:10 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88229">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=DNvm6uzOgLRaoS6ea6Kh7XzT2CdPzw-kOIxNVchGQjTXwMnmyjXWgOHEZ54zGAyQrYvensatRK_0upk6Of6ulMZg6S5S5m0v_HiJq-7FKxM5MCL2Dt8SO3nMMX7kYoW0AGNemjz5CiRRLX4LqBhcOCh6xn3i7IONzBHDNSpUVNmdVwU03OeHaVf_oKpKQ1P-mTofAatl1KNQz05JtMLndcey0W4cWmTU807yQntJQIQN40cH_cJ7LBOHDcLA7avQJYLwDmW7OL3caLGhO9hbge5yQIxbqfB1MK4vX6OtffSKlWjXwHeu6_z4o-ZyvXDL0UmN2stzl-n70JfLqSgUHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3f8d4d95c8.mp4?token=DNvm6uzOgLRaoS6ea6Kh7XzT2CdPzw-kOIxNVchGQjTXwMnmyjXWgOHEZ54zGAyQrYvensatRK_0upk6Of6ulMZg6S5S5m0v_HiJq-7FKxM5MCL2Dt8SO3nMMX7kYoW0AGNemjz5CiRRLX4LqBhcOCh6xn3i7IONzBHDNSpUVNmdVwU03OeHaVf_oKpKQ1P-mTofAatl1KNQz05JtMLndcey0W4cWmTU807yQntJQIQN40cH_cJ7LBOHDcLA7avQJYLwDmW7OL3caLGhO9hbge5yQIxbqfB1MK4vX6OtffSKlWjXwHeu6_z4o-ZyvXDL0UmN2stzl-n70JfLqSgUHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇮🇶
انتشار كثيف للقوات العسكرية على سريع القناة بالعاصمة العراقية بغداد.</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88229" target="_blank">📅 21:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88228">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=B3Z2Q-vaEWilvZd9Xj5UEfuaFUQcCdCl9i4Hs-7Vh8Ku_8gN_xUPnMWhMMHCDHfvnDeIEDhWqww7ffravuBMV9x8X-s2oJ1uLa7gDbBFjPMz2CD12svBuF41A6oY4lGVbLBTPPXOWvhmiEdQ0TyYjGqeRv430B409_s9fqWBr40fsmzPUdYgjnTETYt4K6HNvS-Lq8hCPBym7f9IPU3iA7AJH5sABx9jBZJVYjZXl-xeqdzhBUVnXwCgSnuCOWL4ey3GZZYFbczR761gsA3FNK8HcthbtEgZMnsEn2T8ao26eFqi7tiRjY7kT9Lnv3j5EMXkBK5XrJ09UwdI02B0jXKbpyOhc8tFE6fNNJgyxOS2IViAQ8PePb2hFb8SyFGm4SKND5jN_En4K2lvRLVN-ewC38l8K3ZIgdn1CmrhEcWXj-hYSPPDoy-imzGUye4Zsu3lK8Lv1EIFY9WZaepFbn67-yrrjFp4VDCbVlVnDpp04YB63AH6COm4Hv5Dv1mobMaoXjtG8hk8xWbJliX4eycXnXf7J3fRwSmOWnaPBwsSgBYz9V1TKHbSoBY-NhXUJn8wb2N-g9bOfRFNmfTCae-DzPgrtuN_7L-10H1XKkQBXinVwmi6mLZ9MGXdEXtwSMUSa2EKxhKq8fIXc6e7eGmSysl66oA--z_GzhKL9Xc" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9276455e9f.mp4?token=B3Z2Q-vaEWilvZd9Xj5UEfuaFUQcCdCl9i4Hs-7Vh8Ku_8gN_xUPnMWhMMHCDHfvnDeIEDhWqww7ffravuBMV9x8X-s2oJ1uLa7gDbBFjPMz2CD12svBuF41A6oY4lGVbLBTPPXOWvhmiEdQ0TyYjGqeRv430B409_s9fqWBr40fsmzPUdYgjnTETYt4K6HNvS-Lq8hCPBym7f9IPU3iA7AJH5sABx9jBZJVYjZXl-xeqdzhBUVnXwCgSnuCOWL4ey3GZZYFbczR761gsA3FNK8HcthbtEgZMnsEn2T8ao26eFqi7tiRjY7kT9Lnv3j5EMXkBK5XrJ09UwdI02B0jXKbpyOhc8tFE6fNNJgyxOS2IViAQ8PePb2hFb8SyFGm4SKND5jN_En4K2lvRLVN-ewC38l8K3ZIgdn1CmrhEcWXj-hYSPPDoy-imzGUye4Zsu3lK8Lv1EIFY9WZaepFbn67-yrrjFp4VDCbVlVnDpp04YB63AH6COm4Hv5Dv1mobMaoXjtG8hk8xWbJliX4eycXnXf7J3fRwSmOWnaPBwsSgBYz9V1TKHbSoBY-NhXUJn8wb2N-g9bOfRFNmfTCae-DzPgrtuN_7L-10H1XKkQBXinVwmi6mLZ9MGXdEXtwSMUSa2EKxhKq8fIXc6e7eGmSysl66oA--z_GzhKL9Xc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔻
نتائج الحرب على إيران.. النفط يصل إلى 94 دولار للبرميل الواحد.</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/88228" target="_blank">📅 20:57 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88227">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SbQsGgRM9-OP79jEnxX4eZkvtibymza8FHE9I9mQj8XKHMGZhSFCxdTA924DH5yamFPe_ASm1F6Yk6Lw6yJxlJGUTd-hiS6k-44F2kLyQzA9le23MevBTi5rV7tTqTx5FDjk_OVofyhLf3bbqTJgZgFo_P9nTCjJD7eiG6JdG8eXsDgUD-Bim5XioZFZp6lcZbieiPTDSKdXiL5zfW3nP36jZKrQGlgdFFr79EkTzTfOsAevAaW_bWfbS_GRAw0zpmjZOrJF1S8M8V6BkRWAxuPZtDsilC6ytUKfhT5ZKMME6MGldDTKw_7NE46rPzGnRCbxOSLtwUfBvobURWpprQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">المحور الإماراتي في العراق يرد على زيارة قاليباف بصورة فوتوشوب  من تجيب قاليباف من كبيسة</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/naya_foriraq/88227" target="_blank">📅 20:01 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88226">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">🇺🇸
🇮🇷
وزير الخزانة الأمريكي بيسنت بشأن إيران
: سنفرض أشد العقوبات في التاريخ، وسنسقط هذا النظام.</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/naya_foriraq/88226" target="_blank">📅 18:43 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88225">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">🇮🇶
🇮🇷
محمد باقر
قاليباف:
- كنا مع العراقيين أخوة وأصدقاء في أصعب الظروف.
- عمق الروابط بين العراق وإيران متجذرة في التاريخ</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88225" target="_blank">📅 18:29 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88223">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KKh-U_MAgmuhNAPDVaiqe5zGBDMNSkf37MO6No5GI1S-SrWGJCFVXhpX5r_sTijvue0ij2JeyETyYD3CHr55uS7wtVx_BRmIiQ13HNKM4gPaJEssGBrFMb7qByuj3eewRHVbxsat2Gl58XP-HSrwJWHCpIPmnBVHdvD4alB_Y466b8uqotxyTg-8969guBRBa3R8njC8fk3mRVWYOQs9xOXbYoRkksfCO9PgouAATPaKZUK67k0ZWRczwsEBXSF-7XJe8lUDTJ6dAoumDcXIKeBFEd0s6m6JzgEB6e9kwdzX7uiXTrFzxd4ekrO_3ncRiYxL9I0lNrvi3atmb1xm6Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
وزارة الخارجية الايرانية:
تزامناً مع ذكرى انقلاب 28 مرداد 1332، أقدمت الحكومة الأمريكية على فرض عقوبات اقتصادية وتجارية واسعة النطاق على الشعب الإيراني. ويُعد هذا الإجراء دليلاً آخر على استمرار العداء والخصومة التي ينتهجها صانعو السياسات الأمريكيون تجاه الشعب الإيراني منذ 73 عاماً، كما يثبت الطبيعة المعادية للإنسانية والمخالفة للقانون والاستكبارية للحكومة الأمريكية.
ولا شك أن العقوبات الاقتصادية الأمريكية على إيران، والتي استهدفت الحقوق الإنسانية الأساسية للمواطنين الإيرانيين، تمثل مصداقاً لـ«الإرهاب الاقتصادي» و«الجريمة ضد الإنسانية»، وإن مرتكبي هذه العقوبات والآمرين بها يستحقون المحاكمة والعقاب بسبب ارتكابهم مثل هذه الجرائم الشنيعة.
إن هذه العقوبات، التي تأتي عقب الحروب المفروضة التي استمرت عاماً ونصف العام، وكذلك الحرب التي استمرت 12 يوماً مؤخراً بين الولايات المتحدة والكيان الصهيوني ضد إيران، وبعد فشلهم في تحقيق أهدافهم المتمثلة بإجبار الشعب الإيراني على الاستسلام أمام مطامعهم غير القانونية واللاإنسانية، تستهدف الجمهورية الإسلامية الإيرانية، لكنها لن تُحدث أدنى تأثير في عزم الإيرانيين على حماية استقلال إيران وعزتها وسيادتها الوطنية.
إن فرض العقوبات والضغط الاقتصادي هو الوجه الآخر للحرب والعدوان العسكري، وإدمان الولايات المتحدة المرضي على هذين الأسلوبين لم يعرّض السلام والأمن العالميين للتهديد فحسب، بل تسبب أيضاً في انحطاط أخلاقي غير مسبوق للحضارة الإنسانية. وبناءً على ذلك، فإن أي دولة تؤمن بمبادئ وأهداف ميثاق الأمم المتحدة، ومن بينها مبدأ احترام السيادة الوطنية للدول، لا يمكنها أن تبقى غير مبالية إزاء استمرار خرق الولايات المتحدة للقانون وممارستها العدوانية العلنية تجاه القواعد الأساسية للنظام الدولي.
إن إقدام الولايات المتحدة على الإعلان المثير عن العقوبات الجديدة، رغم أنه يُعد اعترافاً صريحاً بارتكاب جريمة ضد الإنسانية، يمثل استمراراً لسياسة سبق اختبارها وفشلت، وإن إعادة اختبارها مجدداً لن تؤدي بالتأكيد إلا إلى تكرار إخفاقات الماضي وفضيحة مصممي هذه السياسة ومنفذيها. وبطبيعة الحال، ستقع مسؤولية نتائج هذه السياسة وتبعاتها على عاتق الحكومة الأمريكية ومصمميها ومنفذيها.
وتؤكد وزارة الخارجية، مع إدانتها الشديدة لإقدام الولايات المتحدة على تشديد العقوبات غير القانونية والمعادية للإنسانية ضد الشعب الإيراني، أن الجمهورية الإسلامية الإيرانية ثابتة ومصممة على الدفاع عن أمنها ومصالحها الوطنية ومواجهة الهجمات والضغوط العسكرية والاقتصادية والسياسية والنفسية الأمريكية.
وستواصل الجمهورية الإسلامية الإيرانية، بالاعتماد على قدراتها المحلية، وبالنظر إلى تجارب سبعة عقود من المقاومة الشاملة في مواجهة سياسة الضغط الأقصى والعدوان العسكري والإرهاب الحكومي الأمريكي ضد إيران، استخدام جميع الأدوات والقدرات المتاحة لردع شرور العدو الأمريكي-الصهيوني وحماية المصالح الوطنية الإيرانية.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88223" target="_blank">📅 18:21 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88222">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">نايا-NAYA</div>
  <div class="tg-doc-extra"><unknown></div>
</div>
<a href="https://t.me/naya_foriraq/88222" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔻
مناشدة عبر بوت نايا:  نحن مجموعة من صناع المحتوى نناشد الهنود والباكستانيين بالانتقال من الرياض الى نجران. نحن من بعد الله نعتمد عليكم في توثيق الانفجارات والدك اليمني على رؤوس ال سعود ومصالحهم الاقتصادية. نرجو منكم النزوح الى نجران والجنوب خلال الفترة المقبلة…</div>
<div class="tg-footer">👁️ 19.5K · <a href="https://t.me/naya_foriraq/88222" target="_blank">📅 18:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88221">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇱
اعلام العدو:
يراقب المسؤولون الأمنيون الإسرائيليون الأتراك ليس فقط على البر، بل في المجال البحري أيضاً. ووفقاً للمصادر، تُرسل تركيا سفناً حربية إلى مناطق في الشرق الأوسط لم تتواجد فيها من قبل، وذلك لإظهار وجودها، وفي بعض الحالات على مقربة من السفن الحربية الإسرائيلية.</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/88221" target="_blank">📅 18:02 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88220">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">القوات المسلحة اليمنية تنفذ عمليتين عسكريتين بطائرتين مسيرتين الأولى استهدفت هدفاً حساساً للعدو السعودي في مطار نجران والأخرى استهدفت أرامكو نجران وقد حققت العمليتان هدفيهما بنجاح ردا على انتهاك العدو السعودي لأجواء محافظة صعدة بطيرانه المسير</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/naya_foriraq/88220" target="_blank">📅 17:42 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88219">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/88219" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88218">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">الله اكبر</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/naya_foriraq/88218" target="_blank">📅 17:32 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88217">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ACX4aMN4JFj2ZHAgImcGEYGl9w8nnxCK1FoqStG6gNsuWiil7FeaU2Jqf3TIARKstPnjpnWG-uX-lQ4JdWOUMiJafnqGhc8g0Lpf0Oynbhpgal4oDnUsEfhc2Amz9DJEkYsJ4k4yDRbfVm2S2kbWn4nZaIY8xdVVodhsVb2lISiocifTgYJbC8Llfh-msw1U19TO2YtcpzPlvmHGfcEVOdD6SiWj4qzt-gUUFyHGkNMCCYb7VGvCdnSbHIMPT_NbvEhNVTAXoPa1Srn29T6mNK7zMpjB0AWkk61n8hlN3Bz7nC6Q-j-R-T_JUQR0_LEumUfScKB2F_2q1z8AvQjQgg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
هيئة الإعلام والاتصالات العراقية تغلق الموقع الرئيس لشركة كورك في العاصمة بغداد وثلاثة مراكز مبيعات أخرى.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/88217" target="_blank">📅 17:06 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-88216">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">وصول رئيس مجلس الشورى في الجمهورية الإسلامية الإيرانية السيد محمد باقر قاليباف والوفد المرافق له الى محافظة كربلاء المقدسة
🇮🇶
اخوتنا قدوتنا
🇮🇷</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/naya_foriraq/88216" target="_blank">📅 16:50 · 29 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
