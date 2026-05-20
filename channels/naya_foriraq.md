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
<img src="https://cdn4.telesco.pe/file/gKmQdUj6gXJnq02NxBNx0GUGkkOVC6Mtof2ecxXSjv7XZ9fLRQoKKMbziou0g5499tXBhLY1jos78Vyal1dZyStECim_5GzGdtqpGDHM8lazeV3vXIA-L0i3oHIQQMFWEkQvbYqyPHaNY1abb7oaz6DRQlWfkX5zHS2tAweiLxTbi_mSPtTZf2iYJnlbiwB6si9E-LMt0Pbr4Nb5TbCUVRKiwxg9jPkRqmaf2cQFObAJqw6BmaLw4D8i0C5qluh7I4NnCLIxvuw3iKvImJwG-XPNdfbTPtit2P8CeznP2aHHEnyZsfnKCBr44N1LVsbhsoMngqACNczChFnXDT3B7g.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 نايا - NAYA</h1>
<p>@naya_foriraq • 👥 253K عضو</p>
<a href="https://t.me/naya_foriraq" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 اخبار ؛ امن ؛ دراسات ، خرائط ، OSINT ، تسريباتلا تظن الإدارة الأمريكية انها قادرة على إسكات شعوب المنطقة والله لن نسكت .. يوما ما سوف نعيد أيام عماد مغنية وسوف تبث العملية على هذة القناة ..🪪للمراسلة وارسال الاخبار@Nayaforiraq_bot</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-02-30 17:31:58</div>
<hr>

<div class="tg-post" id="msg-75749">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🤺
🏴‍☠️
اعلام العدو:
حدث أمني في جنوب لبنان.. التفاصيل لاحقًا.</div>
<div class="tg-footer">👁️ 356 · <a href="https://t.me/naya_foriraq/75749" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75748">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/352ed3da2b.mp4?token=sGpYxHMErIDWhGIajMHBDqruRiyL_dCejwEsC-SNR3qEg3xZTdgwVJ13eMAtiSJXBXX0gTN4vbKGmKOOtgefjNU3VNBYl49HR0wm7-ugYVOI2LvWYZHozr1cqadV0TTFKsdCj_ezApFsOJHXVh7wgSMVpDmfwVdCx5DJ7fMA5ed2DPGFKNVVDmwb4t59eY2xjljIYbx1ecDJkKqnE33IZ3krIB6axNB8rJLtK91iob817PvvgsMc9uHghAHMVl76c-JgT5vgoZkgRLLYqxUUbZaz2yAbj4Fob2IZH_PmcGd807msGG2-CKFHRGZ_R4Wm4mSxO0gNh8PdY3C_CRympw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: أوباما انسحب من أفغانستان.  علما ان بايدن من انسحب</div>
<div class="tg-footer">👁️ 359 · <a href="https://t.me/naya_foriraq/75748" target="_blank">📅 17:30 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75747">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f240d29220.mp4?token=f7apRT7z71Ghwx-naj7qz9a2iXjqZJZKKLMw6Sau30BlzQJu5y-iOVZdPbZOrO89Hlm3x3EalRGKhTWVxe1XALk8WyEzJm27qM2WMCYqQ23wIzrP_jKDtkdNwG4i-soVFu8_dPFT8DpEPpgd4FsNFNx0zs95TaYjzirCI6CypiuZxyWjNETEKM4npn39Bj659GmyaLTlg_ofeBn1wmanDCLFA8UMIgSOtp6Tq4jXaL1ARZdD4yLbJwJPBw3yPzOTv86ZinPMHvSNDghVR4O-ivwPi0hpa4e20hAJY2egtAbfzyA1QMez-3np_XrKxfYzPYzCQeMT5jKR4VS7dQqmgw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏ترامب: لو أن يسوع المسيح نزل وأحصى الأصوات، لكنت فزت في كاليفورنيا. لكنها انتخابات مزورة.</div>
<div class="tg-footer">👁️ 1.81K · <a href="https://t.me/naya_foriraq/75747" target="_blank">📅 17:22 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75746">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Lqxc8EmeKy8rHxW1hc-ijySJrxu-9vmtSoIoDBRRm2FsbXNqP2dAYOJUqvkeNoC3VF8DOLLVlV1rj-FjBZvTpcPYeuubpLjNgE621Zx2NzZo26cY5CPgYlgdhJHSLbRVgNf_b1iSVixuPa1-R4OmeCBprPP7RjpV3AbkvWpTtSOyQVLJVVeOGe2X-SAkw8bUs89wVgk13hcwS0jp0J_ZLVXUDAf1LpkTW-4CobfJyx5Ozewd0S-kBoSKkiCTxzNalcZYqcY_HF9qxCZwtN3IQsdDifQSNfHL8kEePX9gDqVfqGls9qqk9BilwD28dSpKEjdmwGKu8XzbgFhaqa3eug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
وزير الخارجية السعودي:
نقدّر تجاوب ترامب بمنح المفاوضات فرصة للتوصل لاتفاق ونتطلع لأن تغتنم إيران الفرصة لتجنب التداعيات الخطيرة للتصعيد.</div>
<div class="tg-footer">👁️ 2.26K · <a href="https://t.me/naya_foriraq/75746" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75745">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">ترامب: لسنا على عجلة من امرنا لفتح مضيق هرمز.</div>
<div class="tg-footer">👁️ 2.35K · <a href="https://t.me/naya_foriraq/75745" target="_blank">📅 17:18 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75744">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">ترامب: سنمنح ايران فرصة واحدة، أنا لست في عجلة من أمري.</div>
<div class="tg-footer">👁️ 2.93K · <a href="https://t.me/naya_foriraq/75744" target="_blank">📅 17:13 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75743">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">‏ترامب: رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه  متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 2.99K · <a href="https://t.me/naya_foriraq/75743" target="_blank">📅 17:12 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75742">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5677620f9.mp4?token=bW8npgvoEjPDLwGwWPdZYcbZ6bxLx-YIFwlSt-IXkZznKD4BWBKAeK1hxAuMS0U0X8bijW569dScHLCaNTV5NdeOG6BeYH0TnsZ2YnEdyASFnNJz0TEjTYTZ3wB-jIkgupvkGZiJZz0DWjNfFDXeA7Th_FBwYrr1u8-rgMe1Zl0yoKuu6RgClKvNetMW7FuYOjUpdnn7ZP6lNmK3bxAgQdCHEwAGAJVhRJDdXebR5Zcs6HGln7LaVo8ZXjA8rWOpfThueIS6iuCMoN_io_PtbUdj5TmBlAaHQd11-vgrBtzB3FPLASnXFnGfAx4pD8Esg_uFhLltYtpWG5Yu0613jQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‏
ترامب:
رئيس الوزراء الإسرائيلي نتنياهو سيفعل كل ما أريده منه
متأكد؟ جا وفيديوات ابستين؟
😄</div>
<div class="tg-footer">👁️ 3.31K · <a href="https://t.me/naya_foriraq/75742" target="_blank">📅 17:09 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75741">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">رئيس المعارضة في الكيان يائير لابيد: الهجوم الذي حدث اليوم قام به بن غفير لكن المسؤول عن هذا الهجوم الخطير هو رئيس الوزراء نتن ياهو الذي أدخل مجرماً مداناً إلى الحكومة، وكل من وافق على أن يكون شريكاً لشخص غير مسؤول بهذا الشكل</div>
<div class="tg-footer">👁️ 3.91K · <a href="https://t.me/naya_foriraq/75741" target="_blank">📅 17:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75740">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">محمد باقر قاليباف: لا يزال العدو يأمل في استسلام الشعب الإيراني، ويعتقد خطأً أنه يستطيع إقناع إيران بالاستجابة بشكل إيجابي لجشع أمريكا من خلال مواصلة الحصار واستئناف الحرب. إن الضغوط الاقتصادية المتزايدة والحصار لن يجبرا إيران على الاستسلام</div>
<div class="tg-footer">👁️ 3.84K · <a href="https://t.me/naya_foriraq/75740" target="_blank">📅 17:02 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75739">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">🇮🇷
‏رئيس البرلمان الإيراني محمد باقر قاليباف: التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 3.88K · <a href="https://t.me/naya_foriraq/75739" target="_blank">📅 17:01 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75738">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">🇮🇷
‏
رئيس البرلمان الإيراني محمد باقر قاليباف:
التحركات الواضحة والخفية لـ"العدو" تُظهر أنهم يسعون إلى جولة جديدة من الحرب</div>
<div class="tg-footer">👁️ 4.14K · <a href="https://t.me/naya_foriraq/75738" target="_blank">📅 16:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75737">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pFkgOnDCTAQlTnClq4POSBFXg5CBkoFqo0WdIbxsVusStAa32z6c9qFMDnde_AKuNAP6_ONOsy4hYidP0f468G6tnzwTla4pk05kz5tKQ-c2S6-AlLPghu2r-pJEZRXBrk-q1HFUzfP3vSGwULfbV99FNF7xnVm-_DzYJmjnXr3A5p6VIhCVMHYvuPvLdlSFSBgqnDHkBM2R-DruYzWPkCDLPO9oiJAr4UqIwO0Th2vdL0TE1RHe0CkxJTuuLeu-75nGY_fgszyEPzsunm0_2-99bS9vB9vs-0lISf6G0pjY6qtUJLCl2MTgZftRyi8fPsFpZQe1JgU5PUJeoSHXsw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يهاجم وزير الخارجية الصهيوني: هناك من في الحكومة لم يستوعبوا بعد كيفية التعامل مع مؤيدي الإرهاب. من المتوقع أن يدرك وزير الخارجية الإسرائيلي أن إسرائيل لم تعد دولةً تُعتمد عليها. أي شخص يأتي إلى أراضينا لدعم الإرهاب والتضامن مع حماس سيُختطف، ولن نتسامح…</div>
<div class="tg-footer">👁️ 4.6K · <a href="https://t.me/naya_foriraq/75737" target="_blank">📅 16:51 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75736">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/H9PNHKUegQv9IkEWX4UyT5tZkgi6Uoy77T-D8Pyvo9oxE-q64PZ08YS0pmpFBreBK3mzJ0RwkIE3vF3VWBUrryhNU5elsJMi4vtkDj1F50go0aKyDIKm9Rwfnn7Wma34t3oMu6OQWVcwjVjIZJwKy7fInWvXVD2nqRPY7EvsVETrkR234anvslW9X6LZGUS2oVBW9-76Fm2W0A1yqWpKMzzY064UZ2lz5A74CotDyw0AMRJ_QPsVRwLAeXq9EV2KBtMINN1dbbX62Qmdm1snvDjFnbJO95aNuhqNllJOgVaW8anPQDot0-AbIwjzn5CbvkoFYa8dfIqjGTsiJjpKHA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇶
الاعلان عن تشكيل تحالف سياسي في العراق تحت عنوان (تحالف البيان الوطني) يضم تحالف العقد وحركة سومريون ونواب اخرين.</div>
<div class="tg-footer">👁️ 5.86K · <a href="https://t.me/naya_foriraq/75736" target="_blank">📅 16:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75735">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iQOSfA6HDHZqlLmwukJsNjQWHz-Qe-nox2GsxDJdK_Z3oqMglYCIjbGvKHMp4trlfCyd1BHRiOQdRoQaIUYbFwv8clblBBeYEleB9RnzYhOXEk3d9fUOVmLtjpKWFrQ07eyZWAXh7KgZLoJcsMu5V71mFUdMA_LxMqBBoTqrpieevr2wB9ogCoqVDHs0K7d682evtfrW96khtgND6dqOVYNso4E_wq6dVFRCBMGMhhkltRjzb6_ktqMkg9g0V8CCvlgFqb4YJ9u8p8v7737_2p1f7Lqru1pvp2ouzCItSE2EVE79cT9csj-86tqF_xyFH5VwHYHHqyErxLa2Gv_P-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
وزير الخارجية الصهيوني يهاجم بن غفير بعد ان كشف الوجه الحقيقي للكيان: لقد تسببتم عن علم في إلحاق الأذى بدولتنا في هذا العرض المشين - وليس للمرة الأولى. لقد أزلتم جهودا هائلة ومهنية وناجحة بذلها الكثير من الناس من جنود الجيش الإسرائيلي إلى موظفي وزارة الخارجية…</div>
<div class="tg-footer">👁️ 6.01K · <a href="https://t.me/naya_foriraq/75735" target="_blank">📅 16:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75734">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TJiRU6BtXoXzl9coe9s_jRT63ojy4wrITMAJ0MSt3GWy0wUglqAXF8_QIlmjZ2wi7B8fwNR8ECcyJI-URC4xSRRinrVFWmhKzLahrL5MfJbkKWxm-bTWijSy4ZyKm5XZQANXTPd-McsoZfAQhn2bTyBYw2FzlQXEQStg__eFF0r_zw-z15qZ6qpTCa88lfIasQdWNaZ0xZ0T5CFe5hGd6ZhKEDgIJxpS7-8jqcssRCfJwZPdgT5fvmrH-jq7cXsDOpKiH8Z9PQKvL5XozqCSQYwqYil4Gfm-W_L76WM8sD7GpXfGGC4X-43LrJn_ehZxna923vZq5-lJ0Q--uxRqjw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 6.48K · <a href="https://t.me/naya_foriraq/75734" target="_blank">📅 16:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75733">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/naya_foriraq/75733" target="_blank">📅 15:29 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75732">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">رئيسة وزراء إيطاليا ووزير خارجيتها: معاملة إسرائيل لنشطاء قافلة كسر الحصار غير مقبولة. نتوقع اعتذارا من إسرائيل بشأن معاملة نشطاء الأسطول</div>
<div class="tg-footer">👁️ 8.29K · <a href="https://t.me/naya_foriraq/75732" target="_blank">📅 15:25 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75731">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">🤺
حزب الله:
شاهد من عملية استهداف المقاومة الإسلامية بتاريخ 19-05-2026 منصّة قبّة حديديّة تابعة لجيش العدو الإسرائيلي في موقع جل العلام على الحدود اللبنانيّة الجنوبيّة بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 8.77K · <a href="https://t.me/naya_foriraq/75731" target="_blank">📅 15:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75730">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">سوالف الگهوة
من منزل العامري ، طرح مبادرة اليوم تتضمن صلح وبناء الجدار المتصدع داخل الإطار التنسيقي في العراق..</div>
<div class="tg-footer">👁️ 9.24K · <a href="https://t.me/naya_foriraq/75730" target="_blank">📅 15:06 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75729">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c7c36a9108.mp4?token=EIw77dctHTr2syk4wmQDudVa-cfnr5OLV5jq4EcNGZ4QKQllIO6m_HPXFSr3IpfqApb0rmFEa_bWKDWQQ9ZRO66kJuyY5VkqXoW2zvzQ8ngW5fUzC5enQyieIm6NToGNqz-FlH3gIiovT7Wt-lv9JLJ7n8zfRmlVLvvk2s8hXWqof7c0i1gdcJ1nq9fukEJQBMS3n1DHlt7UcA1TZWTRi-g3f63vOP8-ZTmDH6q4rEodWgBqD_NxTDH4jpTvxMUp76jqUm8ivM9CfMJmfUk_7zhxMipK_jt9Mw9O4N_QUVhk7Ti7Ago9RYxPnvtwzCO2XLKWyX1EYXsYVW_2oDldjg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
جيش الكيان:
رصدت قواتنا أجهزة مراقبة تابعة لحزب الله في جنوب لبنان داخل مبنى كان حزب الله يستخدمها لمراقبة قواتنا وتوجيه العمليات.</div>
<div class="tg-footer">👁️ 8.89K · <a href="https://t.me/naya_foriraq/75729" target="_blank">📅 15:03 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75727">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">وزارة خارجية دويلة الامارات:
نشدد على ضرورة التزام حكومة جمهورية العراق بمنع كافة الأعمال العدائية الصادرة من أراضيها بشكل عاجل دون قيد أو شرط وضرورة التعامل مع تلك التهديدات بشكل عاجل وفوري ومسؤول بما ينسجم مع القوانين والمواثيق الدولية والإقليمية ذات الصلة. كما نؤكد على أهمية اضطلاع العراق بدوره في ترسيخ الأمن والاستقرار في المنطقة، بما يحفظ سيادته ويعزز مكانته كشريك فاعل ومسؤول في محيطة الإقليمي.</div>
<div class="tg-footer">👁️ 9.65K · <a href="https://t.me/naya_foriraq/75727" target="_blank">📅 14:41 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75726">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6b6bfe77ce.mp4?token=lpKNUYFZksAyi85CYvJl-K8pIsqLNzkQnDilaAGnv4CXFLZrVkiL2uOPIdUL3sPJ_AQhZRRuYCxVjTTgKxnun4vSH7grHs4AkNkvBkEtHyyPH5ie8TnAoJJhRpoio5hQ42XoBQbjpxJFQRzApMNMGe5S06_RxYu0qd5ZfAN0aSR7pv0PRmEn7-Iwc5_Zd6A0ZNJvHptfQGIFRYqU-NWavSQZcbCvptIIDmaZiXOFCcvNBZAZymsjmctX9BADaW6a523wph6eknIbG768hCuAXCOD6ngFSZpuecyzm6Q3Y9XnNa58FFPJOr-daWmFKMDyFRw1_r1TRnDom3tx6yCkSw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">بن غفير يقوم بجولة في ميناء أسدود ويشرف على اعتقال نشطاء أسطول الصمود ويقول: "أدعو نتنياهو أن يعطيني إياهم لفترة داخل السجون".</div>
<div class="tg-footer">👁️ 10.3K · <a href="https://t.me/naya_foriraq/75726" target="_blank">📅 14:32 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75725">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">🇮🇷
رسالة قائد الثورة الإسلامية السيد مجتبى الخامنئي بمناسبة الذكرى الثانية لاستشهاد الشهيد رئیسي وتكريم شهداء الخدمة
بسم الله الرحمن الرحيم،
إنّ إحياء ذكرى شهداء «رحلة أيّار» (حادثة تحطّم المروحيّة) وفي مقدّمتهم رئيس الجمهورية الشهيد حجّة الإسلام والمسلمين رئيسي، يُعيد إلى الذاكرة استشهاد قوافل خدّام الشعب في جمهورية إيران الإسلامية، من مطهري وبهشتي ورجائي وباهنر، إلى رئيسي وآل هاشم وأمير عبداللهيان ولاريجاني؛ مئات الشخصيات البارزة من الذين تربّوا في مدرسة الخميني الكبير والخامنئي العزيز (أعلى الله مقامهما الشريف)،  وزيّنوا سجلّ الخدمة المخلصة والجهادية لمسؤولي الجمهورية الإسلامية بتوقيعهم المضمخ بالدماء.
ويمكن للمرء أن يعدّ  من الميزات البارزة للشهيد رئيسي: تحمّل المسؤولية، وإفساح المجال للشباب، والاهتمام بالعدالة، والدبلوماسية الفاعلة والنافعة، ولا سيما الطابع الشعبي الذي اتّسم به؛ وقد كانت هذه الخصائص تبعث الطمأنينة في نفوس أصدقاء إيران، ومنهم مجاهدو جبهة المقاومة القوية وكثير من الحريصين على النظام. وكلّ ذلك كان ممتزجًا، بالطبع، بنفحة روحانية متجذّرة في أعماق نفسه.
وأما بشأن العلاقة بين المسؤولين والشعب، فإنّ الخصائص الإيجابية المؤثّرة كانت تؤدي إلى تقدير متبادل. وهكذا جرت مراسم تشييعه إلى جوار مولاه ومخدومه الإمام أبي الحسن الرضا صلوات الله وسلامه عليه، بمشهد مهيب قلّ نظيره. وقد شكّلت الفترة غير المكتملة من رئاسته للجمهورية معيارًا لقياس حجم الجهد والحرص على الشعب والبلاد، مع الحفاظ على استقلالها.
واليوم نقف أمام الملاحم التي سطّرها الشعب الإيراني في مقاومته التاريخية الفريدة بوجه جيشين إرهابيين عالميين. وهذا الأمر يزيد من أعباء التكليف الملقى على عاتق مسؤولي الجمهورية الإسلامية - من القيادة ورؤساء السلطات إلى جميع مستويات الإدارية ـ أكثر من أيّ وقت مضى. واليوم، فإنّ شكر نعمة الانسجام بين الشعب والحكومة وسائر أجهزة الجمهورية الإسلامية، يكمن في تعزيز دوافع المسؤولين ومضاعفة خدمتهم وجهادهم، والعمل على حلّ مشكلات البلاد ، ولا سيّما في المجالين الاقتصادي والمعيشي، والحضور الميداني والمباشر، وتعريف دور جادّ للشعب الناهض بمسار تقدّم البلاد والتحرك بأمل نحو المستقبل المشرق.
رحمة الله ورضوانه على شهداء طريق الخدمة، ولتكن النصرة الإلهية ودعاء سيّدنا عجل الله تعالى فرجه الشريف سندًا لخدّام الشعب الإيراني المسلم.
السيد مجتبى الحسيني الخامنئي
20 أيار/مايو 2026</div>
<div class="tg-footer">👁️ 10.6K · <a href="https://t.me/naya_foriraq/75725" target="_blank">📅 14:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75724">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">دوي انفجارات في محافظة السويداء جنوب سوريا</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/naya_foriraq/75724" target="_blank">📅 13:11 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75723">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">إعلام إيراني عن مصدر بإسلام آباد: وزير الداخلية الباكستاني توجه إلى طهران للقاء مسؤولين هناك</div>
<div class="tg-footer">👁️ 12.5K · <a href="https://t.me/naya_foriraq/75723" target="_blank">📅 12:57 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75722">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">‏الجيش الأردني يدعي إسقاط مسيرة في جرش دخلت الأجواء الأردنية</div>
<div class="tg-footer">👁️ 12.6K · <a href="https://t.me/naya_foriraq/75722" target="_blank">📅 12:56 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75721">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">إعلام خليجي عن ‏مصدر دبلوماسي: تضارب المواقف بين إيران وباكستان حول قنوات التفاوض ومكان المحادثات</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/naya_foriraq/75721" target="_blank">📅 12:44 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75720">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🇮🇹
إيطاليا الدولة الـ19 التي تشغل طائرة التزود بالوقود A330.
وقعت إيطاليا صفقة بقيمة 1.4 مليار يورو مع شركة "إيرباص" لشراء ست طائرات تزود بالوقود من طراز A330 MRTT - مما يؤدي إلى إلغاء طلبية شركة "بوينج" لطائرة KC-46 Pegasus، التي اختارتها روما في الأصل في عام 2022 قبل إلغائها فجأة في عام 2024.</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/naya_foriraq/75720" target="_blank">📅 12:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75719">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromنايا احتياط</strong></div>
<div class="tg-text">🇮🇶
إلغاء القرار المتعلق بفرض مبالغ تحت مسمى "أجور خدمة" على شركات الهاتف النقال</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75719" target="_blank">📅 11:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75718">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">🇱🇹
أ ف ب: إغلاق مطار فيلنيوس في ليتوانيا بعد الاشتباه بطائرة مسيرة</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75718" target="_blank">📅 11:07 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75717">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=n4o39UIQdML4xUx7FCS7n--BHjzrX12jtyN9X8PuVFlm0F2hqCSch4R_JJoGwS03ITmfZJboPEEZsTFV2Yn4h0pzPjXqUVFqIuTm1YKRANzzPNc3HVFGv-9WOpTEn2K1UGu_145Ov00Xk-OjEpTaiVx8Xh09R2BmCTBdTKDK_xQaMTlfzHp0HSh1DB45xnz9LTVjcrUkD8fhfjaQFPt2286Aa8LH39mFx7NoUg51xSJOLpaDKPY6lHhdyQaPWuhuQv9-QjRwgR7SwJV1emWBpztVP5Knre3xYGbwvxhf0VLyOGh_TR6VClcE4hqhMKCIrVT_eVb9V7UvxaZUDc1uwA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/db7a1d74fb.mp4?token=n4o39UIQdML4xUx7FCS7n--BHjzrX12jtyN9X8PuVFlm0F2hqCSch4R_JJoGwS03ITmfZJboPEEZsTFV2Yn4h0pzPjXqUVFqIuTm1YKRANzzPNc3HVFGv-9WOpTEn2K1UGu_145Ov00Xk-OjEpTaiVx8Xh09R2BmCTBdTKDK_xQaMTlfzHp0HSh1DB45xnz9LTVjcrUkD8fhfjaQFPt2286Aa8LH39mFx7NoUg51xSJOLpaDKPY6lHhdyQaPWuhuQv9-QjRwgR7SwJV1emWBpztVP5Knre3xYGbwvxhf0VLyOGh_TR6VClcE4hqhMKCIrVT_eVb9V7UvxaZUDc1uwA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏴‍☠️
هبوط مروحية عسكرية في مستشفى رمبام على متنها عدد من الإصابات في صفوف جيش الاحتلال جراء إصابتهم جنوب لبنان</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/naya_foriraq/75717" target="_blank">📅 10:19 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75716">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vP84Skl6i928H4vDc3DfLLDMjPzDMOYtKTxH4ex4hhVuEtiBPvQ0CyD-_DXfliTqsPnECgwbQCDihRje8ow-SlCq6kzPQJMC-lExf1KlsPgwUMD0KW0kJpgIWRbrU_Ntr4NzU7naKnUlfWpmA4leelvmgIbnU8POc24u-TfgBP69eWuXcOIlVGT1J8_S8XXNgn8i7agtheDIQZxMEezDFXwguTE6jym1UVIalAlv3a55z9ErJ0ls3khU0ODJ-yd9sE1ToRgwCbkDn2wjpEMk4Mh3vzgo2BcO_LdHpS-ST0F1bMTPv-22hoJkuTWbFG8nS9vhKKKLqLh9OmWqP8QN-w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
🇸🇾
الدفاعات الإسرائيلية تعترض مسيرات في سماء محافظة درعا جنوب سوريا.</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75716" target="_blank">📅 09:39 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75715">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">زلزال بقوة 5.6 يضرب شمال سوريا وتركيا.</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/naya_foriraq/75715" target="_blank">📅 09:33 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75714">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aKoy1UntyaBdw2d8vgl0OIpipZY5bSzC-D6XcmCAu1d7cONUyQtnbloNETX3kLSTM5G6JL9NbndAixX0iYeWpUTmqmsu5F0Ck6-gjYe47WN8zsp1gUp7H36Uiz8v4zPkbJYnCvNqdCcYyDvyxdibd8TD4iWo4zOJbpkUfTgJzF7X4oeUWrzL5frdta8c6Lr1EFrybEL2MluyvPmYG2E6qEouDKO7sP13Tyty6kxlWSAlD56V9EPoXkaHvl8JGyBdxNQ8s6Nd3z5Ewtrx4EVHqrLGR8K_sRT8uN7lY2Ffcq--ZJ3HPtx6FdlXWa3iO5bFnXbORm-XwSL7EOgzzSqOqg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نيوورك تايمز: يخطط الاتحاد الدولي لكرة القدم (FIFA) لحظر المشجعين مرة أخرى من إحضار علم "الأسد والشمس" قبل الثورة الإيرانية والملابس ذات الصلة إلى ملاعب كأس العالم خلال بطولة 2026.  تم أيضًا تقييد العلم في كأس العالم قطر 2022.</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/naya_foriraq/75714" target="_blank">📅 01:15 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75713">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qLahdOJ-mNArpLLsce7g98tALbqNoD2LVY0Jron_qgQuUgI98S56aw-QxXAwy2ble05zyfrafRXriVMPn7_3t-DrS1g6tB8tStQgPi8-Prd80xBLFTMt1-5wZBuG9eoO1tcwDuw0lToXhedbTb3wr944iiIixPzUOYEo-FFTxjbNaXzbv2f70kMSnfG5gpH7MeY0HAA46b4OHrK7uZDXWMjnWV0hiZ4ADeXNzoI6IsJGXEQh3ju_lCQD0pq3nsmyMbaQoUcGcvLIYTvMR-FsR3B6w6qBqCYsj_qb13FqVx3Fu1cKE4hbN8YqJ1ETdcs6cORSjWJt9UDw6sYuKmHXJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الجولاني يشكر دونالد ترامب على “كرمه الزايد حيل” بعد إهدائه شيشتين عطر، ويعتبرهن “الأساس المتين” للعلاقات السورية الأميركية، وسط ترقب شعبي لمعرفة إذا المرحلة الجاية تشمل بخاخ جسم لو مزيل عرق دبلوماسي.
القدس تنتظرنا يا اخوة
😄</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/naya_foriraq/75713" target="_blank">📅 00:46 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75712">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jFTZ0krJ6fwyJ3FWftT414Gev9VrodS0TWLcBhpdN3Bj8SrNcfG-AnRaYeqwcCSC9Fpnkyom0wKnTPWLPo45tF_4k-hAJ73Mu7HU__cuK0Odh5_J-8qOXvkCrRljC3EsMqANNT3gp2_r_i4frrgJlkWMcMxLvj8B3KpEH0zFR99O5CkaEx-ErDanVoMNeh9YNzCBGoUY7VpJwFRVot9fzVWRWArvBlWPdicA8Y1j9jZmqFJK25IYN1-iyALvcFJ4M4woin3jWITBDcJW27H2qsHByCGXveSTlio416DqJgVO-XWMmgtUNJCIyu7fO0ckg4Vz3ufzBZxpc8i3JOYyUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">عراقجي:
بعد أشهر من بدء الحرب على إيران، يعترف الكونغرس الأمريكي بفقدان عشرات الطائرات التي تبلغ قيمتها مليارات الدولارات.
تم تأكيد قواتنا المسلحة القوية كأول من يضرب طائرة F-35 التي توصف.
مع الدروس المستفادة والمعرفة التي اكتسبناها، ستضم العودة إلى الحرب العديد من المفاجآت.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75712" target="_blank">📅 00:38 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75711">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75711" target="_blank">📅 00:21 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75710">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">🌟
🏴‍☠️
قوات حزب الله البطلة تشتبك مع عناصر جيش العدو في بلدة حداثا بجنوب لبنان وتتمكن من إستهداف وإحراق دبابة ميركافا وإصابة عدد من الصهاينة والمعارك مستمرة حتى اللحظة.</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/naya_foriraq/75710" target="_blank">📅 00:10 · 30 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75709">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4cbad0422a.mp4?token=FN8CLgsKuAMRwDllRhCm-MfogZ2IvjxATLEGwB8g52epIV_ndx881EhAZ2_7CweT7vHukzaLzrJcKSs7e8Usf9Eu6mE5UrahOHQZKfBHsZGO5XT86y3Z_a_Zh_U7osmg_adIFcCHLcTO-1SkJNqkIMpgeB-P_qbOCXnh41BLQcPdV8rLeiA0caToR2UZAF4QP-ylRKNT6gJb--FPJNdNs6z9TjsFW8iwyquy-um3nrTUwOuWFrNHB3yCGYWWhd_TDN6qt9SLuaeiFFoazgu51aR5-P8CQGM42EJaTsygfO8cGaoe--8L4xTXd1TABE6c-zZlgaZca2gAXCqjDXO-nJV7NP5Yr3Wq6M5PdGbEkgCqqc5sgR2rwbDxAR4GTUB_BVgcO7G8x2sa0qI6HyjhuLo1GCR1URRapyaANdvj8RKvzEt0DYgq48VEerag_8yiyrZtt31cxRYVHFp5WqOZzaMxkEhBPFY-fZAm0FIehsFO5kVgmpbVGe9gNrBgLF-DTv9DqrpICL9T1je1yl82nvM4utrwm6tICtqUGWVuISDHv5zVVsHp6BScqKQLZ9082gB7w_HnjLr9oKfDXdBCHuikrLxwPMN-mvI8a7v9WTgr03pZZoLeUD5vU1qxUmHZxCbP9gi0f5cyGjnf3V3NbKZnC1MQTtrBEeqOMtxC19o" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انيميشن بأسلوب الليغو يوثّق المسار الذي خاضه رئيسٌ شعبيّ للجمهورية الإسلامية الإيرانية
نُشر بمناسبة ذكرى استشهاد الشهيد رئيسي ورفاقه الشهداء</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75709" target="_blank">📅 23:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75708">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">🇺🇸
حاكم كاليفورنيا:
إنهم يحاولون تزوير الانتخابات. دونالد ترامب يعلم أنه سيُهزم بشدة في شهر تشرين الثاني.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75708" target="_blank">📅 22:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75707">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
انتحار جندي من الجيش الإسرائيلي داخل دورة مياه في "الكرياه" بتل أبيب.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/naya_foriraq/75707" target="_blank">📅 22:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75706">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🌟
🏴‍☠️
مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 التابع لجيش العدو في بلدة البياضة جنوبيّ لبنان بتاريخ 17-05-2026</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75706" target="_blank">📅 22:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75705">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">⭐️
وول ستريت جورنال:
‏احتجزت الولايات المتحدة ناقلة نفط مرتبطة بإيران في المحيط الهندي ليلاً، في الوقت الذي يهدد فيه ترامب باستئناف الضربات العسكرية على إيران.</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/naya_foriraq/75705" target="_blank">📅 21:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75704">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">🇺🇸
‏
جي دي فانس:
خياران أمام إيران إما الاتفاق أو استئناف الحرب.
نعتقد أن الإيرانيين يريدون إبرام اتفاق لكن نؤكد أنه لدينا دائما خطة بديلة.
‏لا أحد يريد عودة الحرب والفرصة متاحة أمام إيران.
إيران بلد معقد للغاية ونرى مواقف متشددة من جانب فريقها المفاوض.
أوضحنا للإيرانيين خطوطنا الحمراء.
لا أعتقد أن الإيرانيين سيكونون متحمسين لنقل ما لديهم من يورانيوم مخصب لأمريكا أو روسيا.
مخططنا ليس نقل اليورانيوم الإيراني المخصب إلى روسيا ولم يكن ذلك أبدا ما نخطط له.
لا نريد فقط التزاما من الإيرانيين بعدم امتلاك سلاح نووي بل بألا يعيدوا بناء قدراتهم النووية مستقبلا.
هذه ليست حربًا أبدية. سنتولى الأمور ونعود إلى ديارنا. هذا ما تعهد به ترامب، وهذا ما سيحققه.</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/naya_foriraq/75704" target="_blank">📅 21:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75703">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🏴‍☠️
‏
هيئة البث الإسرائيلية:
الاستعدادات الأميركية – الإسرائيلية لاستئناف الحرب ضد إيران اكتملت.</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/naya_foriraq/75703" target="_blank">📅 20:56 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75702">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DjCf8MfaTrAKuSlYVMyYXsAzD336XJa0HK4ALfZmtm3K8U_84EN0O8GdWbmViYe3ghDnH-4KXtpmucs-Q4FOZSYkItLxmWXglUtHhLXBZ0eJ9RSUDHYIVgQwq7icDMk-Pf7aIGF44rgTD5cNUBgHts6u0WvQ19Qa2r6u-7f8sN5zoxBxGMzznJyjgcRMApGEvDQyfwVS7_R-sc7RN1MMTHakXDld95LZizjePIUZT0kjyu3kf9uybxgmkDhdVtOFnhl9Z3a0vssoOZi0ZbWm4qHiyCnATKFDlSqOU3W9Cixf4hWUoW3rll0ran05Ti9i-3uX7ukHUzrFdWmcLkvKOw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⭐️
وزير السيد مقتدى الصدر ينشر عبر حسابه الشخصي.</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75702" target="_blank">📅 20:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75701">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">‏ اعتقال موظفة في السفارة الأمريكية في بغداد تدعى قند محمد فرج ذياب الجنابي بتهمة الرشوة والفساد !!!!
‏</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/naya_foriraq/75701" target="_blank">📅 20:24 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75700">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">حدث امني خطير في بغداد</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75700" target="_blank">📅 20:23 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75699">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m6woGBmaX00JZhO9vkjsAxe8Beyv78a-piOZkqMmrV932S6PGisMXtjXRQEz8-1g1c1ttwCMw5kLOTLAOC2vH2P7kP48Ojdnwq2cFyOEKxcdEOCuHkm4hPgC9_aqnllmBpTDMQzsEcGSJbCmnjMt6eS2rZ9wc0WUaM2CzB36hCJ-VvvADP2ATWFCzWbiqUqW7ioELgYspRtKz8S2JaQBZEow90q-Ext2o1SQ33xnQeOdN024UoGadYxkSDPvI2mHfThjHzZwhviFvc-oEbEsJ3Wq1ZsM0pjRke3s7mVAe_dLv6FTXfzA2msa7lY-66qwetTr9g8dvxbkx9bx2SIR5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏴‍☠️
إعلام العدو:
مقتل جندي إسرائيلي في جنوب لبنان.</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/naya_foriraq/75699" target="_blank">📅 20:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75698">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🌟
حزب الله ينشر:
ترقبوا... مراسم تنكيس علم العدو الإسرائيلي الغاصب في مقر اللواء 226 في البياضة.</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/naya_foriraq/75698" target="_blank">📅 19:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75697">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">⭐️
ذا أتلانتيك:
اصطدمت طائرتان لإعادة التزود بالوقود من طراز KC-135 Stratotanker فوق غرب العراق في 12 آذار خلال الحرب الأمريكية-الإسرائيلية ضد إيران، مما أدى إلى مقتل ستة من أفراد الخدمة الأمريكية بعد تحطم إحدى الطائرتين بينما تمكنت الأخرى من الهبوط مع أضرار شديدة في الذيل.
صرحت قيادة مركز القيادة المشتركة (CENTCOM) علنًا أن التصادم وقع في "مجال جوي صديق" ولم يكن بسبب نيران معادية. ومع ذلك، تظهر تقارير المخابرات الأولية أن نشاطًا مضادًا للطائرات تم اكتشافه من ميليشيات مدعومة من إيران في المنطقة في وقت تحطم الطائرة، مما يثير احتمال أن يكون الطيارون قد اتخذوا إجراءات تفادية قبل التصادم.
رفضت قيادة مركز القيادة المشتركة (CENTCOM) لاحقًا هذه التقارير، مستنتجة أن الإطلاقات المكتشفة كانت على الأرجح صواريخ موجهة إلى أهداف أرضية وليس طائرات.
من المتوقع أن يحدد تحقيق مستمر لسلاح الجو الأمريكي ما إذا كان الحادث كان خطأً يمكن تجنبه من قبل الطيارين بسبب ازدحام المجال الجوي بدلاً من عمل العدو.
شمل الأفراد الستة الذين قُتلوا ثلاثة طيارين في الخدمة الفعلية من السرب السادس لإعادة التزود بالوقود في فلوريدا وثلاثة من أفراد الحرس الوطني للطيران في أوهايو من السرب 121 لإعادة التزود بالوقود.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75697" target="_blank">📅 19:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75696">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=V_UzbAd9t9qoJrBrGsa__94-Og2uNmfhNf3MF-b5c-bZmnMDXxWRnVJ0cXrNfjAEqy_g0tgVPSztFJBQUyTU5b84aBR6EixplLAyaiOCs8etrkSXZPw3AGESdR67RPXDC8R3DWOwXd1C9abNZGiurEDNoG9FhsQNuQWhIfO-WBULPEfo89qeSAw86E-czqygxUryRMJuZ_FF2d8gNsBzH4B04uEsjvBDaysZcWQEFN4NXqkHKcx4YxF5PiHzIdgM2Mor2LepB-5P1OS3yOjMp3mEa5Ly0pOiU92UGsP0SBK_CXbMjt2kHSrBbtSH8eBOU1bSFVofKcpnU5CkHRSjskMImPgbw2A2jAe8Qvh4HBWRTxrHO6gcL9XUY-ZZehdWMrdRlACpWRYgXQU7xq4fJs_iYtkyusqb88IeNUSeeDtuvrgMUuQd7CW8JmUhLnu0K6TgKcWkEk36V0xPIRth2GbQII2oy9hxJca8xYpotuee3QorypI-Qn0GC8RarC8Sc99MDYBoXm9roUFjNSIXkN4z0cX94vghjQDPUk_ZAUz2xfgmo5jcKyR2418S6B6kk5eeibamGlKsgFKB_0B2m1wSGU0AF0jOHG0AmCVWnCMUWao1JEsEOd7rDhrWfVZHxTozy-bTbDQox6jFO3kAMwnQwTJWHdRxmhotyrtSt0Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8c6863208b.mp4?token=V_UzbAd9t9qoJrBrGsa__94-Og2uNmfhNf3MF-b5c-bZmnMDXxWRnVJ0cXrNfjAEqy_g0tgVPSztFJBQUyTU5b84aBR6EixplLAyaiOCs8etrkSXZPw3AGESdR67RPXDC8R3DWOwXd1C9abNZGiurEDNoG9FhsQNuQWhIfO-WBULPEfo89qeSAw86E-czqygxUryRMJuZ_FF2d8gNsBzH4B04uEsjvBDaysZcWQEFN4NXqkHKcx4YxF5PiHzIdgM2Mor2LepB-5P1OS3yOjMp3mEa5Ly0pOiU92UGsP0SBK_CXbMjt2kHSrBbtSH8eBOU1bSFVofKcpnU5CkHRSjskMImPgbw2A2jAe8Qvh4HBWRTxrHO6gcL9XUY-ZZehdWMrdRlACpWRYgXQU7xq4fJs_iYtkyusqb88IeNUSeeDtuvrgMUuQd7CW8JmUhLnu0K6TgKcWkEk36V0xPIRth2GbQII2oy9hxJca8xYpotuee3QorypI-Qn0GC8RarC8Sc99MDYBoXm9roUFjNSIXkN4z0cX94vghjQDPUk_ZAUz2xfgmo5jcKyR2418S6B6kk5eeibamGlKsgFKB_0B2m1wSGU0AF0jOHG0AmCVWnCMUWao1JEsEOd7rDhrWfVZHxTozy-bTbDQox6jFO3kAMwnQwTJWHdRxmhotyrtSt0Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇷🇺
🇨🇳
لحظة وصول الرئيس الروسي فلاديمير بوتين إلى بكين، واستقباله من قبل وزير الخارجية الصيني وانغ يي.</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/naya_foriraq/75696" target="_blank">📅 19:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75695">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YQKMr3ww9nSvfdBJmi3R6lEJD2X4kmA3hBJS23Fgy9HnE62iBbxkD5mOu__HFqKoKthS9uDf__CfpEXYHLEykrb9j9DcDFxpulm0H-evwnz1A0vfDBaPCqwfyUiDg4NriWihOJXLUiBd_kLU3r4Pv0dG6-zJ1nG2StbnePRwi-lyx5x26IOOBXQcp8jLyGBiS_vs7a72g84vynwBNeUCve1B8cG_4TSoI0gBSp6iDvgcQSs07uRAU9eI56wdivPOtieiaYoCJWjkoDrn2UYRKGciaI_Fqo0LLfjGAHr7vxBF-9D21mYbu2eTGQxvq1RSR5PhKOURYlKGrWKl195q5A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
رد قائد الثورة الإسلامية على رسالة جمعٍ من الناشطين الشعبيين في مجال السكّان:
أشار قائد الثورة الإسلامية، آية الله السيد مجتبى الخامنئي،  في معرض رده على رسالة الإعراب عن المحبة والتعزية المرفوعة من قِبل جمعٍ من الناشطين الشعبيين في مجال السكان بمناسبة استشهاد قائد الثورة (قدّس الله نفسه الزكية)، إلى مسألة زيادة السكان وارتباطها بقوة إيران الإسلامية وحضارتها، مؤكدًا على تكثيف الجهود المتزايدة للناشطين الشعبيين في هذا الحقل وضرورة ترويج ثقافة الإنجاب.
🔻
وجاء نص رد قائد الثورة الإسلاميّة، الذي نُشِر بمناسبة اليوم الوطني للسكان، على النحو الآتي:
📖
بسم الله الرحمن الرحيم
بعد توجيه التحيّة والشّكر على إعرابكم عن المحبة والشعور بالمسؤولية، أيها الناشطون المُخلصون في مجال السكان؛ فإنّ من بين الإنجازات القيّمة للدفاع المقدس الثالث، والنعمة العظيمة لبعثة الشعب الفريدة التي تجلّت للجميع، صعود إيران إلى مستوى قوة كُبرى ومؤثرة. ولا شكّ في أن استمرار هذا الوضع وبلوغ مستوى أفضل منه، يرتبط ارتباطًا مباشرًا بقضيّة السكان.
▪️
إنّ قضية وجوب زيادة عدد السكان يُنظر إليها من منظار تعويض النقص الناجم عن بعض سياسات الماضي؛ ولكن إضافة إلى ذلك، فإنه من خلال المتابعة الجادة للسياسة الصحيحة والحتمية لزيادة عدد السكان، سيكون الشعب الإيراني العظيم قادرًا في المستقبل على خوض غمار أدوار كبرى وطفرات استراتيجية، وقطع خطوات واسعة في اتجاه إرساء الحضارة الحديثة في إيران الإسلامية. ومن هذا المنطلق، فإن الجهود المتزايدة للناشطين الشعبيين في مجال السكان وترويج ثقافة الإنجاب، يمكن أن يكون لها أثر بالغ الأهمية في سبيل تأمين هذا المستقبل المشرق.
⏺️
ومن جهة أخرى، فقد كان هذا الأمر أحد أهم هواجس قائدنا العظيم الشهيد (أعلى الله مقامه الشريف)، الذي طالما أكد عليه في الكثير من اللقاءات، والمداولات، والاجتماعات العامة والخاصة، ولا يزال يُعدّ من أهم القضايا الاستراتيجية للنظام. يُؤمل أن تؤدي جهودكم المخلصة، أيها الأعزاء، في ظل الدعاء المستجاب لسيدنا (عجل الله تعالى فرجه الشريف) إلى نتائج مثمرة، إن شاء الله.
✍
السيد مجتبى الحسيني الخامنئي
🗓
19 أيار/ مايو 2026</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/naya_foriraq/75695" target="_blank">📅 19:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75694">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=eWirmBzS21VVkY5pm9VyLIwzC0mMMtJwJX-5gfA0GALKwfAtHhT8DWaRshymp_D9XHIDk9Dvx10nx1mY3zVK-D_qwm9xxNQpTY2jY7RDwg7qwK_KPNo_jR0GOlbwTYdbyjmGbWsknivcyeLMkx80gDy5kAD7RUwyBRab7I_2cVVRr6c4sl_3nucZkvGoEM5U2iMzSfd3iN5DWinJOGpPY2Ft-yRXYBHVAigVYXXcVixPPjtD75brdGWiWTRaJx8f7vbYzyGGN8kELx-xKRavVU2nrKC0huPQJnx4fiPO8VgFO3bxU3ZyCAKC0uN3NpP0nkJvYOhVH9UcGoIgT2e9MoPapuAKO1dDMlyKfAFaOgTYwsMlg2zJH51YxMriFLZmHdMO-ObXYmILRrFJAd7uTjHrbBZ0YGP3dyNoDKa59C9P2bkqIdxD9gMeGvVMAKQDsBtvW6zA5oQS3VZGGuV8DLYp-munFf0Loj9UDH2DMCCL34SM_D33TMw1JyHbNgvvhSShj2kq5u0-GmNMtVxOix99gAqUvPzmSNL9g5hj0xby1nFzNZ9bfZUFYhaR2HuMFM9y7PFAV9Dg5aZ5rAhYkYDc5Qx7MxAuz68DxYvRAmtVmony3V0Tll4r3wBKpajslTNJQGQys4J4zSwYVLcR463M5cXaPm6iP61gEkjNKME" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/60e2efce8f.mp4?token=eWirmBzS21VVkY5pm9VyLIwzC0mMMtJwJX-5gfA0GALKwfAtHhT8DWaRshymp_D9XHIDk9Dvx10nx1mY3zVK-D_qwm9xxNQpTY2jY7RDwg7qwK_KPNo_jR0GOlbwTYdbyjmGbWsknivcyeLMkx80gDy5kAD7RUwyBRab7I_2cVVRr6c4sl_3nucZkvGoEM5U2iMzSfd3iN5DWinJOGpPY2Ft-yRXYBHVAigVYXXcVixPPjtD75brdGWiWTRaJx8f7vbYzyGGN8kELx-xKRavVU2nrKC0huPQJnx4fiPO8VgFO3bxU3ZyCAKC0uN3NpP0nkJvYOhVH9UcGoIgT2e9MoPapuAKO1dDMlyKfAFaOgTYwsMlg2zJH51YxMriFLZmHdMO-ObXYmILRrFJAd7uTjHrbBZ0YGP3dyNoDKa59C9P2bkqIdxD9gMeGvVMAKQDsBtvW6zA5oQS3VZGGuV8DLYp-munFf0Loj9UDH2DMCCL34SM_D33TMw1JyHbNgvvhSShj2kq5u0-GmNMtVxOix99gAqUvPzmSNL9g5hj0xby1nFzNZ9bfZUFYhaR2HuMFM9y7PFAV9Dg5aZ5rAhYkYDc5Qx7MxAuz68DxYvRAmtVmony3V0Tll4r3wBKpajslTNJQGQys4J4zSwYVLcR463M5cXaPm6iP61gEkjNKME" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🌟
🏴‍☠️
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ
12-05-2026
دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بصاروخٍ موجّه.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75694" target="_blank">📅 19:00 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75693">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🇺🇸
🇮🇷
قائد القيادة المركزية الأمريكية:
القوات الأمريكية تعرضت في 7 إبريل لإطلاق نار من إيران وقمنا بالرد.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75693" target="_blank">📅 18:46 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75692">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🇺🇸
ترامب: ‏الجميع يقول لي ان الحرب على ايران غير شعبية، لكنني أعتقد أنها تحظى بشعبية كبيرة. عندما يسمعون أنها تتعلق بأسلحة نووية قادرة على تدمير لوس أنجلوس، عندما نشرح الأمر للناس - ليس لديّ الوقت الكافي لشرحه لهم.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75692" target="_blank">📅 18:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75691">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSJz_EwFqEPqjDNVaOviocYOwidUtXskMsa4DYQndL71cwFNKZym6ZX-xqlUBwXIH_nzY6DAz0DtEwTbKxklrn6CKtWERIXLKWf_R_ydr4t--dH3hV4S9XA0fSKfdBqv1TrWOasyxPc5l0fX16MPvf3ESJvRzlYlxraga3P4RW69zITqysFVwtxH1Ni9LQvV48MSsIQSizRh80LfroMCtDub_tGdhkEmmg2IQsg6hXgn8ChR7fOS9b0Tl_uv_oUr-U_JKAMzDw2DLXtcji84cJxgR13dYLIeENVoP-CMJpsY2GO9-NtyTtPgUnUE5Nq81cwjOIJDEcNb2fBwbueeTon0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7bc14bff42.mp4?token=J71TU5xmyN672tMq7ieFnaOWG64bshpOe7brPZKw-97qqbGQl1M6vTTx1Za5lSdNEMKUmSENUavTKhX6zLLAKyL_9YydgC6-allyi5y136oVvFEVVUG-CzTToo1r1o8G14kruuyAwphsKh3X2ipp_yVxxXkTA16Jl156scQEJssGe37aVg1jASu_wQUi_xqQjs_zbDf26oDNi42GyhEXFmrkqHnp9Zq8_6UGnA9RJht-D1peXZbBP4QmRxSCglj36CHsUdPnhQU089NtdFc0z-SZJ4882Q6cLNZrcJQnoYa_MNynR7FWlf8cktIeSGywsxZgBVG8eeTZjLY8aCQrSJz_EwFqEPqjDNVaOviocYOwidUtXskMsa4DYQndL71cwFNKZym6ZX-xqlUBwXIH_nzY6DAz0DtEwTbKxklrn6CKtWERIXLKWf_R_ydr4t--dH3hV4S9XA0fSKfdBqv1TrWOasyxPc5l0fX16MPvf3ESJvRzlYlxraga3P4RW69zITqysFVwtxH1Ni9LQvV48MSsIQSizRh80LfroMCtDub_tGdhkEmmg2IQsg6hXgn8ChR7fOS9b0Tl_uv_oUr-U_JKAMzDw2DLXtcji84cJxgR13dYLIeENVoP-CMJpsY2GO9-NtyTtPgUnUE5Nq81cwjOIJDEcNb2fBwbueeTon0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
ترامب: تلقيت مكالمة يوم امس وقالوا لي "سيدي هل يمكنك الانتظار؟ نحن قريبين من صفقة"  سأمنح إيران مهلة يومين أو ثلاثة ربما حتى الجمعة أو السبت. فترة زمنية محدودة.</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/naya_foriraq/75691" target="_blank">📅 18:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75690">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=sGoNQ0q4ev1bAdRXT3zX_7Hjwqd1hfuLZ3DC5Smdj-TSNxo1h1vuvdIh57gbJlsXBKGQI1_Zpegz5QoQ35Qq6cB-EPtgh3Tfjf2jn3VqHYfJR76uuzt0TTcVvyjA_I67nOosrrqtPFfeOjCS4bmNnWXNJ3rlF2APjnlNimlpWSnQLkQJuR5hiu8YMD70GYqRdlvY3lO5yTeU3CNvIyKERDG_ww6aMvh919ruDv1i66rVWX5-zT9JEU3XGilo5vu4q_bmsdgpULz3uhkPyJ0-80JjBMj9eXTj07I0pDNb0i4FBQiunoKJH_ufu7cIYXZeyTV45Lp0Mg_xKogDxvS-WI7SnE8zJCRSh4IqrY8rjYULmdhassvdtGM2Q_v0rhipB-OVY9ehUp0N1gRdwmhWMQHy860tYvHCsCJ9YnxkH64F1AnBKG1cYOZgdVPXDxq_UgXiauFv1zmpcYslE7ML1alecQXv8tHE_qMMhaDGF_gN-YYPtW_TuN-LuZXy0gzWawR2eSVu-k0vWRM9XgRAWpy15Rtf1QXIEu65X2RDfk5Z3UM3M26-Srp_7hoPPC-3f8cBB4lYSid3HJTzgKO6pW37O3XhQrc6IYSc5J_a6KpIHd1OdhIyBnzp-0cTL4rED-R8oQJmADJLEEw3j4TCEvECsHQIBuUmtkuLFCw9UW0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c3bf75e59c.mp4?token=sGoNQ0q4ev1bAdRXT3zX_7Hjwqd1hfuLZ3DC5Smdj-TSNxo1h1vuvdIh57gbJlsXBKGQI1_Zpegz5QoQ35Qq6cB-EPtgh3Tfjf2jn3VqHYfJR76uuzt0TTcVvyjA_I67nOosrrqtPFfeOjCS4bmNnWXNJ3rlF2APjnlNimlpWSnQLkQJuR5hiu8YMD70GYqRdlvY3lO5yTeU3CNvIyKERDG_ww6aMvh919ruDv1i66rVWX5-zT9JEU3XGilo5vu4q_bmsdgpULz3uhkPyJ0-80JjBMj9eXTj07I0pDNb0i4FBQiunoKJH_ufu7cIYXZeyTV45Lp0Mg_xKogDxvS-WI7SnE8zJCRSh4IqrY8rjYULmdhassvdtGM2Q_v0rhipB-OVY9ehUp0N1gRdwmhWMQHy860tYvHCsCJ9YnxkH64F1AnBKG1cYOZgdVPXDxq_UgXiauFv1zmpcYslE7ML1alecQXv8tHE_qMMhaDGF_gN-YYPtW_TuN-LuZXy0gzWawR2eSVu-k0vWRM9XgRAWpy15Rtf1QXIEu65X2RDfk5Z3UM3M26-Srp_7hoPPC-3f8cBB4lYSid3HJTzgKO6pW37O3XhQrc6IYSc5J_a6KpIHd1OdhIyBnzp-0cTL4rED-R8oQJmADJLEEw3j4TCEvECsHQIBuUmtkuLFCw9UW0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇺🇸
‏ترامب: دول الخليج تتفاوض وإسرائيل أيضاً.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75690" target="_blank">📅 18:15 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75689">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">🇺🇸
‏ترامب: كنت على بُعد ساعة من توجيه ضربة لإيران، وكان ذلك سيحدث الآن. القوارب والسفن مُحمّلة ونحن على أهبة الاستعداد للبدء.</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/naya_foriraq/75689" target="_blank">📅 18:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75688">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=M0_qvQIedcIOX35hBrFthBFcwMkjODTF87Jk9J4aWBhtupEfVoADgROYBSmmq90o6IkANhvsLwEz4Jdg00n9LUJzXI5qVV2j0fGtdZIM7W2Q5k8-oEmladWspNudJTjleMtg24qCPxo08VktQixhpvZ3SUXytxEDUCXD-NJAE9zzpT3J19X0j_RCP5bXeyLe3zliEbltLn1OIzDcUho4g-mLuJzERwfu11x_xhvji2fJNGtCiR64rZG53FFR3kMKC1BQBABELbSRVB4mxkRqRfiaDTEmgmia75AoiBYtcP0Q-sYBtF07VMBtgNUdvLk3C_-O9Lc_FhkiXr6rpMBB-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/27acce6b15.mp4?token=M0_qvQIedcIOX35hBrFthBFcwMkjODTF87Jk9J4aWBhtupEfVoADgROYBSmmq90o6IkANhvsLwEz4Jdg00n9LUJzXI5qVV2j0fGtdZIM7W2Q5k8-oEmladWspNudJTjleMtg24qCPxo08VktQixhpvZ3SUXytxEDUCXD-NJAE9zzpT3J19X0j_RCP5bXeyLe3zliEbltLn1OIzDcUho4g-mLuJzERwfu11x_xhvji2fJNGtCiR64rZG53FFR3kMKC1BQBABELbSRVB4mxkRqRfiaDTEmgmia75AoiBYtcP0Q-sYBtF07VMBtgNUdvLk3C_-O9Lc_FhkiXr6rpMBB-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامب: ستعرفون قريبًا جدًا ما إذا كنا بحاجة لضربة كبيرة أخرى.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75688" target="_blank">📅 18:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75687">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/naya_foriraq/75687" target="_blank">📅 18:10 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75686">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">‏ترامب: قد نضطر إلى توجيه ضربة أخرى لإيران، لست متأكداً.</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/naya_foriraq/75686" target="_blank">📅 18:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75685">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-text">🌟
‏
مجلس الوزراء العراقي يقرر ما يأتي:
‏
تعطيل الدوام الرسمي في الوزارات ومؤسسات الدولة كافة، ابتداءً من يوم الثلاثاء الموافق 26 أيار ولغاية يوم السبت الموافق 30 أيار بمناسبة عيد الأضحى، على أن يُستأنف الدوام الرسمي يوم الأحد الموافق 31 أيار.
‏تعطيل الدوام الرسمي يوم الخميس الموافق 4 حزيران في الوزارات والمؤسسات الحكومية كافة، بمناسبة عيد الغدير.</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75685" target="_blank">📅 18:05 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75684">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">ترامب من موقع بناء قاعة الرقص في البيت الابيض: "إنها مقاومة للطائرات المسيّرة".
يبدو ان المسيرات مصدر قلق لترامب
😄</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/naya_foriraq/75684" target="_blank">📅 18:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75683">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">🇺🇸
وزارة الخزانة الأمريكية تفرض عقوبات على أربعة أشخاص في أسطول الصمود الانساني الذي يحاول كسر الحصار عن قطاع غزة.</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/naya_foriraq/75683" target="_blank">📅 18:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75682">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🇮🇷
نائب وزير الخارجية الايراني:
- تقول الولايات المتحدة إنها أوقفت الهجوم على إيران "مؤقتًا" لإتاحة الوقت للمفاوضات؛ لكنها في الوقت نفسه تتحدث عن استعدادها لشن هجوم واسع النطاق في أي لحظة. هذا يعني اعتبار التهديد فرصة للسلام!
- إيران موحدة ومستعدة بحزم لمواجهة أي عدوان عسكري.
- بالنسبة لنا، الاستسلام لا يعني شيئًا؛ إما أن ننتصر أو نصبح شهداء. وكما قال الشهيد رجب بيجي: نحن أمة عظيمة، فلنسجل اسمنا في التاريخ؛ من بين كل الألوان، اخترنا الأحمر، ومن بين كل أنواع الموت، اخترنا الشهادة.</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/naya_foriraq/75682" target="_blank">📅 17:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75681">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">‏
قائد حلف الناتو:
سيتم سحب 5000 جندي أمريكي من أوروبا.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75681" target="_blank">📅 17:44 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75680">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">دويلة الامارات تزعم ان الهجمات التي طالتها قادمة من الاراضي العراقية.</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/naya_foriraq/75680" target="_blank">📅 17:43 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75679">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">‏الولايات المتحدة تفرض عقوبات جديدة على إيران</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/naya_foriraq/75679" target="_blank">📅 17:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75678">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">📰
مجلة
فورين بوليسي الامريكية:
إيران تتفوق في معركة الرأي العام. قبل مئة يوم كانت إيران "دولة منبوذة" أما اليوم فهي الشخصية الرئيسية على الإنترنت</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/naya_foriraq/75678" target="_blank">📅 17:22 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75677">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=Oti4A-ZcUy5b3hPKD9w_f925qpNhOwshGo24WrTu26yytLFtaHIbXEC9CeDcI-iJ0ZXWwBvqeIQyaTPvGzxdT23WEBwiGDVgaP2iHda-tGMdNGq6tm6QJQEJDACZ38b-73wmXMxTHFHL6Jd4iO5uX_K0hQl2M4mT5vLZHoKqLfCNYJ_6MDnJHK7OtXzK3S-OjkFILAuOr8G6A6tQ_pCBysrSSS9dFqTjrDxsjOtENPpkZH48whFCj1OmS6njIcRFbf3FiUbIJZlcsfpvEDVtc0iqfSCwDVV7UaT5E911YAaNku8auoq12jXSaq9jf7mfCwlqaJYAgQ_lGaqE4dzesw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/bcdfd32e5e.mp4?token=Oti4A-ZcUy5b3hPKD9w_f925qpNhOwshGo24WrTu26yytLFtaHIbXEC9CeDcI-iJ0ZXWwBvqeIQyaTPvGzxdT23WEBwiGDVgaP2iHda-tGMdNGq6tm6QJQEJDACZ38b-73wmXMxTHFHL6Jd4iO5uX_K0hQl2M4mT5vLZHoKqLfCNYJ_6MDnJHK7OtXzK3S-OjkFILAuOr8G6A6tQ_pCBysrSSS9dFqTjrDxsjOtENPpkZH48whFCj1OmS6njIcRFbf3FiUbIJZlcsfpvEDVtc0iqfSCwDVV7UaT5E911YAaNku8auoq12jXSaq9jf7mfCwlqaJYAgQ_lGaqE4dzesw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">#متداول
نفاذ الوقود يتسبب في توقف سيارة إسعاف تنقل مريضاً وسط احد شوارع محافظة ميسان</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/naya_foriraq/75677" target="_blank">📅 17:21 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75675">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ERMNQCozKTmmLDD0NgTIPdInUNigPRWSRA8qtJ5orWPskyWCjg9Ni1lBHjj7eN3UCjMqHSU9nazr8BrsLO0UmE-7N8T_edvmEX4mO26m1gE_Ia8p-Sjo1PqKXxjKc4YCUy17ZuMPUjE1OJwnI3uoZTBnLWxoPBfUlS-PRxtaxhi1tplZkGG0MvDt2V_EabJN7pwMAtZ2nzmG7YkpA-tnMkvIIk5Zs6NDBed3V4qMonX0unvKyFZcgB8UPWVdUUBWGOT9DiM-e5ajfUy9ms4s8C7GibY4AWbB1rC71Aq_c5EHM5GBbIhIcm6bSMVcvi-LDnyrdiDFoKMbY0zaq4kOPw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/P0LvifbrcPeIgwtVqLmFop55NDDq5zekOBkAHvVeFNGapRKh2P7UU1EH1zddOCo1VyDomIgGg6l4y7UCycoTWaDT304kE8CZNQzeydaMz58UTxRtxgIYLZVX8Q1ea_YJhRfW_VPk1oXVzcImLDnyc5Rqqd1P5-1hbEytPacrxOuwVq3WuqtlWqic3gSfgWz8k92LPmIO71LokbHEXvHq_HCGHiX7_uUqCCEww6001wgIOMVz65orgb840616kakNoip2PKRK398Nb54Wq32DhaPLr0wEMIEtJWxWW-W-amnulbhkjNFA99n1GGZty21IEJvJ6n0g3UD_RrWPfBotAQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">النائب سعود الساعدي يكشف عن هدر مالي بقيمة (4) ترليون دينار في هيئة الإعلام والاتصالات كمبالغ ضريبية بذمة شركة كورك لم يتم استيفاؤها للخزينة العامة مطالبا بتحديد المسؤول عن توقيع عقد التسوية مع الشركة دون استكمال إجراءات التحقق الضريبي، ملوّحاً باتخاذ إجراءات قانونية وقضائية بحق المقصرين في حال عدم الإجابة خلال المدة القانونية المحددة.</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/naya_foriraq/75675" target="_blank">📅 17:12 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75673">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">🇺🇸
‏
وزير الخزانة الأمريكي متوسلا:
من المتوقع أن يدعم الشركاء الأوروبيون العقوبات المفروضة على إيران من خلال منع مموليها، وإغلاق فروعها المصرفية، وكشف شركاتها الوهمية.</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/naya_foriraq/75673" target="_blank">📅 16:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75672">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">#رياضة
⚽️
قرعة كأس الخليج
مجموعة A:
السعودية
العراق
الكويت
عمان
مجموعة B :
الامارات
اليمن
البحرين
قطر</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75672" target="_blank">📅 16:49 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75671">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🤺
حزب الله:
مشاهد من عملية استهداف المقاومة الإسلامية بتاريخ 16-05-2026 دبّابة ميركافا تابعة لجيش العدو الإسرائيلي في بلدة البيّاضة جنوبيّ لبنان بمحلّقة انقضاضيّة.</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75671" target="_blank">📅 16:32 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75670">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">‏وزارة دفاع الجولاني تزعم تفكيك عبوة كانت مزروعة بسيارة ثانية في "باب شرقي" بدمشق وتعلن مقتل احد عناصرها واصابة اخرين</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/naya_foriraq/75670" target="_blank">📅 16:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75669">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9JbCdKlvAoJGKjZ4oHA8eEuMh04_YA0fd6SAPp8LkqDxoFC5ovnvjgHJnJFmUn8ctdU1EQyXQBklFdHDuB5G60RdvX6iIBYF-Ce_-HqOIrzR6Btrs2QSegzgtCtizJSvaHYfLvjHJOU3EaIPQr1Iv7ksV44Rg0fbeTg0Zekon8ASOrbjAMSzHdbxwb_2W_YPAV8t9eWnojLuHG1V9vrbd82YFEL3GkJKBqauLjEOLGppFcKAeQ3SJSiAttspPTbVi_FhZlXsMC_6EvZEDwp7nO9TGyLfxzfh4w6cFmWMOAOEY4W4LfvABBV1L66gQRiYVrpSG6yQHArArjoA7j6Hw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لحظة الانفجار في دمشق واطلاق النار العشوائي من قبل عصابات الجولاني بعد الانفجار</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/naya_foriraq/75669" target="_blank">📅 15:55 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75668">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QXiZRfKE2qt4ribZcVCf1TVMdMA7M_tgiqaRN-hSEAakV-K7EwWdcILQJE5RxHj96BanY1Cihqm87piuoaL4ARAlDIa1LODLBrFJvvE4NuFoNTMugCdzupWaBOVBSry07-j3kiSVIIkUAmXYyWbJhlQDH8vYdRkcord6tuxOOpLk1ONY9_8YgdX-ktnwNdqGsvyQJzZhd_qlJw79u_NK964qr2olUd-1k4RClpAW4VOJwNYBEaGOnhe2AyWSnNs0bTLAYXdLB4px0dCLJKbnN_vLydnJZWTAP4mXhvcVtySejoNAW9c4ItbMZaH44n_N2fCSqGxFFwIqNqO3HkXR_w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">السيد مقتدى الصدر:
لن أغفر لمن يتهمني بالعمالة للثالوث المشؤوم او اني عدو لآل البيت عليهم السلام لا في الدنيا ولا في الآخرة وسأقاضيهم وإن لم يأخذ القضاء مجراه فسأتعامل معهم وفق الشرع ولن أسكت عنهم</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75668" target="_blank">📅 15:48 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75667">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🇬🇧
‏
بريطانيا:
العالم يسير بسرعة نحو أزمة غذاء عالمية بسبب إغلاق إيران لمضيق هرمز وعشرات الملايين مهددون بالمجاعة.</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/naya_foriraq/75667" target="_blank">📅 15:39 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75666">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">🛡
قائد عمليات الفرات الأوسط في الحشد الشعبي اللواء علي الحمداني:
نحمل القائد العام للقوات المسلحة، أي رئيس الوزراء، مسؤولية نشر قوات في الصحراء الغربية لمحافظتَي النجف وكربلاء لمنع حدوث خرق مستقبلاً، أن إفراغ هذه المناطق من القطعات العسكرية في السابق كان مخطّطاً هدفه التمهيد لمحاولة إنشاء قاعدة للكيان فيها</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75666" target="_blank">📅 15:34 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75665">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3002a10155.mp4?token=B4_UtHVnNRrh70f5oK2_b1T_k6uU33mCdPL2QCeA7QjjASzBqqYquZl2HkmuUdyd6dP8WuPCc6RfY65FtN1YVIoBddkV6Gm2TYK8UYJLncVXIZhD9mUT9u-zlF3bQIcLU6-HB9IokQdufyoDrZpYwsfmdG_tfwqtHDUdFcyreACZyi0CCWbfRK85p3KNzQVw8QEqMcsQnyyteGhFmcFZKlwZIS5k5PHfkWkqFWelF3tibg-7l4DI_WYuNxFl_zm0a8UH5Q0KgCC3WhFuea-v9xqeOloJfjh5M41rcY1pJJPlpxHIVqnREVOgfBSiICdpW1IEkdJiC0b22-K4Ne6NsA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3002a10155.mp4?token=B4_UtHVnNRrh70f5oK2_b1T_k6uU33mCdPL2QCeA7QjjASzBqqYquZl2HkmuUdyd6dP8WuPCc6RfY65FtN1YVIoBddkV6Gm2TYK8UYJLncVXIZhD9mUT9u-zlF3bQIcLU6-HB9IokQdufyoDrZpYwsfmdG_tfwqtHDUdFcyreACZyi0CCWbfRK85p3KNzQVw8QEqMcsQnyyteGhFmcFZKlwZIS5k5PHfkWkqFWelF3tibg-7l4DI_WYuNxFl_zm0a8UH5Q0KgCC3WhFuea-v9xqeOloJfjh5M41rcY1pJJPlpxHIVqnREVOgfBSiICdpW1IEkdJiC0b22-K4Ne6NsA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مشاهد من الانفجار في دمشق</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/naya_foriraq/75665" target="_blank">📅 15:25 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75664">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84c91c7a93.mp4?token=OFxTxdIqGMgulH0O3vTp0LqLoxPrtrRdVHavzroutXdI8ApS_U1ybLQTKLDA0O26G867x8hRFsigz7NSfIumGV5TdzVjepw7EVOsdpWE5UgXueyOCd6KZwWir6tksbHns_APZjdpCnMP7aGX2RFBd27tVg8d9PokMWxcSDGvFY0bAi9sVJWNbkJtWnNSSsBfmnmU5PaN03tX5LiTpbG2Xi-1CsfanNh4dazYKQKbZZJr73Q9z-6V6OjyLuXYkb6JRm17Ayp3SB-TJkYFGrUuiiHuUxgpTBKKiC8rqpkGYQ-VGQ-V48m1-IB5uUhcZLx84mBmXRykPes0CnyjGGO8bw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84c91c7a93.mp4?token=OFxTxdIqGMgulH0O3vTp0LqLoxPrtrRdVHavzroutXdI8ApS_U1ybLQTKLDA0O26G867x8hRFsigz7NSfIumGV5TdzVjepw7EVOsdpWE5UgXueyOCd6KZwWir6tksbHns_APZjdpCnMP7aGX2RFBd27tVg8d9PokMWxcSDGvFY0bAi9sVJWNbkJtWnNSSsBfmnmU5PaN03tX5LiTpbG2Xi-1CsfanNh4dazYKQKbZZJr73Q9z-6V6OjyLuXYkb6JRm17Ayp3SB-TJkYFGrUuiiHuUxgpTBKKiC8rqpkGYQ-VGQ-V48m1-IB5uUhcZLx84mBmXRykPes0CnyjGGO8bw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعلام عصابات الجولاني: عبوة ناسفة في سيارة تستهدف مركز إدارة الأسلحة في دمشق.</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75664" target="_blank">📅 15:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75663">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gUnc8sBwy3u_mV_aviBgtcwrHvBM9iG-s2Bgr72wp93rNowwrU3DLcc62MmQvHOOrw6lmvyYTVA8XrkdwQLqgUgT7JLp8VXOYp-0bpYIancu9Q82QPfzIX53wEbgx0K18JrA6FhVrawjmrIx6FQqcPFzEQfYXsc-cSqdPsEJgAWBJ-LhJRnI7clm_PZd1V3_m4KhXTWzbTR8w0zTzS0l70sssWIbfHhQx6FIZ3ymS06q25IdrowVvk11-sXjegZxyRN5OEtc3ZvYaO7N4GhiyRVOa4wAJ8GhrzOo9tZdRqh_DrXcowE2TLf5ZDBmNzy2PfSaKp8Z9ukbhNbndSpaNg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انفجار سيارة مفخخة في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/naya_foriraq/75663" target="_blank">📅 15:16 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75662">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7388a4652.mp4?token=KUlAZWdMwYEq19ZsyTWHvAk51Us-JfkH_qpwQPfGXKl_wkk0XVpizHMOKPtz-x17oVhNm0rOX8ZLvxX3CUHTlKIaqQNcethJPE6_OrU-Hs0h_pDTAl_LFwYZUiRh2vPiQrNbZ22odClrPdDnKkX34VWVGbGQPFfYrf7bPZuM_MU3_l5r4NtlfV8L52sK_75Bn_3IZTn9067tMFJkbAqI80mAP_cz-orXO5MnFUaifiqmzo3HjCZpro-8-hqOCCCnP40X_oC9KkOWYFF9s8VA-CtyWpiLbAqQmx8HInh0bHluukzmzVyS1f20jV0BUHW8Jqi9yp102F6ZfPiVxJHS-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7388a4652.mp4?token=KUlAZWdMwYEq19ZsyTWHvAk51Us-JfkH_qpwQPfGXKl_wkk0XVpizHMOKPtz-x17oVhNm0rOX8ZLvxX3CUHTlKIaqQNcethJPE6_OrU-Hs0h_pDTAl_LFwYZUiRh2vPiQrNbZ22odClrPdDnKkX34VWVGbGQPFfYrf7bPZuM_MU3_l5r4NtlfV8L52sK_75Bn_3IZTn9067tMFJkbAqI80mAP_cz-orXO5MnFUaifiqmzo3HjCZpro-8-hqOCCCnP40X_oC9KkOWYFF9s8VA-CtyWpiLbAqQmx8HInh0bHluukzmzVyS1f20jV0BUHW8Jqi9yp102F6ZfPiVxJHS-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">انفجار سيارة مفخخة في العاصمة السورية دمشق</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/naya_foriraq/75662" target="_blank">📅 15:13 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75661">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">وكالة مهر: سماع دوي انفجارات مجهولة في جزيرة قشم.</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/naya_foriraq/75661" target="_blank">📅 14:33 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75660">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">وكالة مهر:
سماع دوي انفجارات مجهولة في جزيرة قشم.</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/naya_foriraq/75660" target="_blank">📅 14:09 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75659">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">🏴‍☠️
اعلام العدو:
تقارير أولية عن محلّقة مفخخة استهدفت سيارة على طريق مسكافعام في إصبع الجليل ويوجد إصابات في المكان.</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/naya_foriraq/75659" target="_blank">📅 14:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75658">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">"نيويورك تايمز": إسقاط طائرة إف-15إي وإصابة طائرة إف-35 كشفا أن تكتيكات الطيران الأميركية أصبحت قابلة للتنبؤ بشكل كبير</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/naya_foriraq/75658" target="_blank">📅 13:02 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75657">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">بلومبرغ: الروبل يتصدر أفضل العملات العالمية حيث ارتفع مقابل الدولار بنحو 12% منذ بداية أبريل.</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/naya_foriraq/75657" target="_blank">📅 12:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75656">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5330bf0831.mp4?token=bDrHf5KLmj_dXeBU2tKEQU1ZncTpn9dmTIF-RW3AtxnhBabBrKRrOEJ2tTgqxpw1bhWvmzYvcLgEmaJD8EXhPj1skD0ox1vZj7SushDsbp2mN95MjZiOLj2RhYLC8CG1kdV5rtgLeVCJyCZJ21tzW1SfggiH8BtnEWUxrh5dD29FOiO0ipyyEzAtFp0RDP9jSdO-Topoj2A7ovnQjXRabUMCUvlF8vXLD91wXunZqqZvSLmWwjIs_sgLsiKb2WmfWbd0--2H3sgfSrJ6899IKnl87O5dtvg2IYlIpDaOfzF6T8pPyDzDmkGqGyZNqLPMuiUCvBDPNor0hRJoEaDo_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5330bf0831.mp4?token=bDrHf5KLmj_dXeBU2tKEQU1ZncTpn9dmTIF-RW3AtxnhBabBrKRrOEJ2tTgqxpw1bhWvmzYvcLgEmaJD8EXhPj1skD0ox1vZj7SushDsbp2mN95MjZiOLj2RhYLC8CG1kdV5rtgLeVCJyCZJ21tzW1SfggiH8BtnEWUxrh5dD29FOiO0ipyyEzAtFp0RDP9jSdO-Topoj2A7ovnQjXRabUMCUvlF8vXLD91wXunZqqZvSLmWwjIs_sgLsiKb2WmfWbd0--2H3sgfSrJ6899IKnl87O5dtvg2IYlIpDaOfzF6T8pPyDzDmkGqGyZNqLPMuiUCvBDPNor0hRJoEaDo_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تحليق طيران حربي فوق سماء محافظة واسط العراقية.</div>
<div class="tg-footer">👁️ 21.3K · <a href="https://t.me/naya_foriraq/75656" target="_blank">📅 12:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75655">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">‏الصحة العالمية: قلق بالغ جراء سرعة انتشار فيروس إيبولا</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75655" target="_blank">📅 11:01 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75654">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">خفر السواحل الأمريكي: رصد تسرب نفطي قرب عاصمة ولاية هاواي الأمريكية</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/75654" target="_blank">📅 09:27 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75653">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">دوي انفجارات في حيفا بعد هجوم من حزب الله</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/naya_foriraq/75653" target="_blank">📅 09:26 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75652">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🇮🇷
المتحدث باسم لجنة الأمن القومي في البرلمان الإيراني: نعمل على إطار قانوني سيقره مجلس الشورى لإدارة مضيق هرمز</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/naya_foriraq/75652" target="_blank">📅 08:50 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75651">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">🇮🇷
قائد مقر خاتم الأنبياء التابع للحرس الثوري الإيراني:
نُعلن لأمريكا وحلفائها عدم تكرار الأخطاء الاستراتيجية وسوء التقدير.  عليهم أن يعلموا أن إيران الإسلامية وقواتها المسلحة أكثر استعدادًا وقوة من ذي قبل، وأنها على أهبة الاستعداد، وسترد بسرعة وحسم وقوة وشمولية على أي عدوان متجدد من أعداء الوطن والأمة الشجاعة. لقد اختبر الأعداء الصهاينة الأمريكيون مرارًا وتكرارًا شجاعة الشعب الإيراني وقواته المسلحة الجبارة.لقد أثبتنا بعظمتنا وإرادة الله أننا سنُظهر سلطتنا وقدرتنا للأعداء في ساحة المعركة، وإذا ارتكب أعداؤنا خطأً آخر، فسنتعامل معه بقوة وقدرة تفوق بكثير حرب رمضان المفروضة، وسندافع عن حقوق الشعب الإيراني بكل ما أوتينا من قوة، وسنقطع يد أي معتدٍ.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/naya_foriraq/75651" target="_blank">📅 00:18 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75650">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vPf0lIPNRzBiRCSEQKSOGyMro87sgmQeXN6HIJ4He5a3GvUbjLi87tFcU6vfaAQ5ZP4gJz8md3-R1Jtudfm95elrr7xD0k9QqDCz4v0IpaUTW4Y9ITj9g-5JWAn0f6762xSTw0ghM3sFW1rokADQfjU9AO_mnmeRyxz4arxbqliqbfGnjX7pGht-wpATdOO-4e0jI314UKVn8fboJ1hpi9nQKB6p6MEnd_rkTaTYLocQnQABeozSL1QEcnMnAO3QGVBUR8iQtdv2yh5a3w1hR8Hc2vRLi4v696ZdhhVo1MdQ0ceLK9fPgASB3PCP4-7T9iVU3rfrwGsAbxPoksfE1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇸🇾
عصابات الجولاني الإرهابية تختطف مواطن لبناني من الطائفة الشيعية من قرية كوكران الحدودية بين لبنان وسوريا وتطالب بفدية قدرها 500 ألف دولار.</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/naya_foriraq/75650" target="_blank">📅 00:14 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75649">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kjAHziouQciZtf3Jmm_BI5wgCE4Nr4TznGStwk0RWvN6NNywdpqUjwn6ZET3zlugBViHLjs1h91gKOahY-E2Gq9vlmS6gKLh6XrWzkSdMJJ_Vzc7bC4cKg5OVyLrHNrb1njhYGbQwzRXf1hMBtxfMlNlyLGbMcjLyW0WZ9tedugkoT140o9qOkZcasJESDGRkpMFlWF3DXgcTefJ0vL8bH4O721Ti3MBT6Qd38_3CFMQW_4gp1vbqqrjqkEqIpVXUKuGV6CPvTZc01YXPL3nJopad3cYcJcr0tLN07o9RlHbeSO9iFMOHOywXsw7z9jsEJhhdd97y6BtcAH748ej3Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇮🇷
المتحدث بإسم الخارجية الإيرانية إسماعيل بقائي:
السيد فريدريش ميرز، ‏النفاق صارخ. فالهجمات العلنية التي تشنها الولايات المتحدة والنظام الإسرائيلي على المنشآت النووية الإيرانية المحصنة لا تُقابل بالإدانة، بل بالأعذار والتبريرات. ومع ذلك، عندما تقع عملية يُزعم أنها عملية مُفبركة - والتي رفضت حتى الإمارات العربية المتحدة نسبها رسمياً إلى إيران - تلجأ هذه الأصوات نفسها فجأة إلى لغة "القانون الدولي" و"الأمن الإقليمي" الرنانة.
‏إذا كانت الهجمات على المنشآت النووية تهدد شعوب المنطقة، فيجب أن ينطبق هذا المبدأ بالتساوي على جميع الدول - وليس فقط عندما يخدم المصلحة السياسية للغرب.
‏هذا الإحساس الانتقائي بالعدالة يذكرنا بالقاضي آدم في قصة هاينريش فون كلايست "الإبريق المكسور": رجل يستدعي سوء سلوكه الذي لا يغتفر عملياً إصدار حكم، ولكنه، في غطرسة وتبرير ذاتي، يتجرأ على أخذ مكانه على منصة القضاء.</div>
<div class="tg-footer">👁️ 21.5K · <a href="https://t.me/naya_foriraq/75649" target="_blank">📅 00:11 · 29 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75648">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">⭐️
تفعيل الدفاعات الجوية الإيرانية في مدينة أصفهان.</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/naya_foriraq/75648" target="_blank">📅 23:59 · 28 Ordibehesht 1405</a></div>
</div>

<div class="tg-post" id="msg-75647">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=PJm14dhfpldHufk4nBWAE03S-5hANrmeSKSXzitdnx87XKDFdOFOCPdRvSQdNFqKeIbubP6U1mBoBLhfdco2qTPHFLnrvN3517clGJaxC-pMNbMjHxcBZne90eeO84a8hPMa0YyPCY3d89RFuupOKJUHbgUO4CgEIBChLMyFBFHf61AIYZN77TsC5m_XyG9Bn1akd2cDS6yhaTTk7hRrYQsK9h01rvdETN79Hzdi976R-BIKt34gv-YRuQ49rmQcMeAcoos_mDvS9mxGqJFiuJJGCqPKm0LWP6y--yfnjDMA-M3iFx2iQ0GdU5n8W6mQZ6V4dfM3WcbwwoaffxD-dA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3da62d1b00.mp4?token=PJm14dhfpldHufk4nBWAE03S-5hANrmeSKSXzitdnx87XKDFdOFOCPdRvSQdNFqKeIbubP6U1mBoBLhfdco2qTPHFLnrvN3517clGJaxC-pMNbMjHxcBZne90eeO84a8hPMa0YyPCY3d89RFuupOKJUHbgUO4CgEIBChLMyFBFHf61AIYZN77TsC5m_XyG9Bn1akd2cDS6yhaTTk7hRrYQsK9h01rvdETN79Hzdi976R-BIKt34gv-YRuQ49rmQcMeAcoos_mDvS9mxGqJFiuJJGCqPKm0LWP6y--yfnjDMA-M3iFx2iQ0GdU5n8W6mQZ6V4dfM3WcbwwoaffxD-dA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⭐️
اندلاع اشتباكات بين قوات جيش الإحتلال الصهيوني ومسلحين في منطقة حوض اليرموك بريف محافظة درعا السورية.</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/naya_foriraq/75647" target="_blank">📅 23:49 · 28 Ordibehesht 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
