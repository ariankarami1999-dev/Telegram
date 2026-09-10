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
<img src="https://cdn4.telesco.pe/file/FOJyG5gHHVfU2sXXLbn-Z8PiZmU5QdtWndfd36p40dN8FOcvmuj4w36Hh9Gh8sUit43oWsah-HGNY6i_bjZ6Qca_sHy09VtlKZ-zZ5hIRs4vSdLeHCaQhHEKiBSGlnkdavZhYwGB9q5XQU4FYHZvdB5Mvgi_3Mc_7r5wlfwjsTFVi_xQvgQm2gQ7PD5lp7_Oo6OvWV_UkEksVVdpSJEjju1DIqWW2IqbmDGEsyHhlblFZKBePPdx9emDiqWkZPVPFwwSgp0j_G85SykHS3iY0dI0jXMG7eg3AtHmOizoZVuF1gYLVWhNNeXUWWz7fNtGlfwRph934fRWJYL9IFMcUA.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 فرهمند عليپور Farahmand Alipour</h1>
<p>@farahmand_alipour • 👥 63.4K عضو</p>
<a href="https://t.me/farahmand_alipour" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-20 02:47:11</div>
<hr>

<div class="tg-post" id="msg-6723">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‏آغاز جلسه شورای امنیت سازمان ملل برای بررسی موضوع ایران</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/farahmand_alipour/6723" target="_blank">📅 17:48 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tYr9DQzzVhF9xThvGTCxcPuovewN8pWhd2YAiiTXGfEOLYA82-UgvI9VvPos7J5Wg38pj_RcSimE3qnfyN7_Qxeb9TR3D9-49QWk_8T1M2UacXnDMMGKuCvk4W-hDQtbHc1S1x4ry6ABPgtiszxpMrxXUGdDegXYCa5ETD-Wx2vp9-IDNPFe37L5Tkdjyq4dXZTCv6IQ5EVkOAK5RKm0oJSYdBrNUc6EamFjRQ797DKGtjIj8vOae3IBfu_grDiuByzN1vtfgld364M_MZTgb1PO_2i_BLULKKgfmDL1Ro1Sm77nm4VcRNqNe4dgULL_ow3pmSHSTxfQuZJpgsobMg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/942e1020d0.mp4?token=tYr9DQzzVhF9xThvGTCxcPuovewN8pWhd2YAiiTXGfEOLYA82-UgvI9VvPos7J5Wg38pj_RcSimE3qnfyN7_Qxeb9TR3D9-49QWk_8T1M2UacXnDMMGKuCvk4W-hDQtbHc1S1x4ry6ABPgtiszxpMrxXUGdDegXYCa5ETD-Wx2vp9-IDNPFe37L5Tkdjyq4dXZTCv6IQ5EVkOAK5RKm0oJSYdBrNUc6EamFjRQ797DKGtjIj8vOae3IBfu_grDiuByzN1vtfgld364M_MZTgb1PO_2i_BLULKKgfmDL1Ro1Sm77nm4VcRNqNe4dgULL_ow3pmSHSTxfQuZJpgsobMg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کارشناس صدا و سیما میگه :
مردم ایران در خانه‌هایشان
«۵۰۰ میلیون تن طلا دارند»
یعنی «هر ایرانی» حدود
۵ هزار و ۸۰۰ کیلو طلا داره :)
روایات اسلامی و معجزاتشون رو هم
همین مدلی ساختن!
اون مجری شوت هم میگه : الحمدالله!</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GSqYEwDnDhV5v_z_Xi6L6GWzVouqjr6JOUYDCA8WP39VMYULvMtW90ggmBPWFpk02RwVRHxUU0yxxssFKkO5sKKE0QUwaOVURd9bxAI88bb9xdfv54Ku252LKEEM0tNiwkEvRGy05WreP3CK_tFSdJj75FTmVT1xqJvRa5t9APlGf_NvLQU7P8zdrk0KhAc234Ge72Gb1dLsqXpbp5pFjnDcY7TUA7LlEl30hMLRxvRkz192TlnNkFgWR9DIG_ylz1I_FPVW-tYBrEitIGwZ4TFNZdS2DOBliAt7lmr-h3TdNyRm1TE7lIp2zunD59nZbJ9INPifS6sSuxEhPMpMIQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/eaef64a82c.mp4?token=GSqYEwDnDhV5v_z_Xi6L6GWzVouqjr6JOUYDCA8WP39VMYULvMtW90ggmBPWFpk02RwVRHxUU0yxxssFKkO5sKKE0QUwaOVURd9bxAI88bb9xdfv54Ku252LKEEM0tNiwkEvRGy05WreP3CK_tFSdJj75FTmVT1xqJvRa5t9APlGf_NvLQU7P8zdrk0KhAc234Ge72Gb1dLsqXpbp5pFjnDcY7TUA7LlEl30hMLRxvRkz192TlnNkFgWR9DIG_ylz1I_FPVW-tYBrEitIGwZ4TFNZdS2DOBliAt7lmr-h3TdNyRm1TE7lIp2zunD59nZbJ9INPifS6sSuxEhPMpMIQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">قابل توجه کسانی که دنبال بهانه‌ای هستن
برای پناه گرفتن در آغوش امن و گرم آخوند و توجیه حفظ قدرت در دست این‌ها.
این مفنگی، پدر زن مجتبی خامنه‌ای،
میگه «فعلا به خاطر شرایط جنگ
با حجاب کاری نداریم»!</div>
<div class="tg-footer">👁️ 19.2K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0966fba487.mp4?token=WF7LcbinBGMWFTE2OpauLPOMEB7TjHx-uYM9l-q3dOlJKf4a4Ratm-XaXMvinpI0dz0xCR2GkPBh0GAYOeA6ebOzAQVHuU5QEF3p6iDJ--WKiVpi32aAWxuMc1ieEdPknkXnji3Nk3JMsVxL9Ht9zbtLfkHq6T-jqVQa7foo-MGna0uK-i1AqE7buRYh7pIHX-3N4zy0rI2TtoxZt_h90su7LD3msX7t5_suB-W_Y00zv-jr_9Dy_0ztm-kdsW9M_qMd41rJKnKYOO-4bo4rTW0AWdUnmqyzrPWrHl9JyDoiZD1MRryvUWLvS4fAAEDKHy9pn9XA8HyyUpcX-Wrp_w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حامیان حکومت دیشب این شکلی موافقت خودشون رو با قطعی برق و افزایش قیمت بنزین،
دلار، طلا و گوشت نشون دادن:
تو تاریکی می‌نشینیم، دلاری گوشت میگیریم،مهریه کم میگیریم!
موجودیتتون ذلته!
دیگه ذلت چیه!</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0oBrXt_6lCiYrIvM3CWsUTWuxfDUW4J0z6G59N9tqNRK_UYGp16m51FZtVb85CngRTdtkQkv96HPbGJp6-VFaTw36QjDU6vmgfPF7bwS9DaqT7wHmUl54PPGEexsoVKdKAEhE8XOzIqtmUvEehuu6a1haCoq6FFa238Qh8CLYAZBNk19aqUHcXgexFt5nHNplyYrGzAaqJ45lF64dU2zJOOiBkjYcSU77aIpMWm8vZYhSRbu0JlrtBzJYOETnfLUcw-n_4meOttVoNvluKnnc8P6smjncsBDM1hCbB3PTuqkHsMiKKpHVN69nqwEpcgPC9gMTsyZ-Qn2eRoXEJ6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7cd7686141.mp4?token=fQkG6mrm29iUQt9ZKrofCJrg5BmIzT7qJH_LgVeN0FsjxZvvQRFrgti-VvYDnvajoPRaKnouPwyaDTR53rQUktdLIikRZXgBo6V2tQjorEs2KR1VMYy4i-bzzRnv97RYojm9gMMYeVrYhGZ4Ve1zJn1r9FJG9JZct7qCzgmrm45bfijljIrV2YlJXv9pxC0hJj8Y2j4dMBEGjnse_joCLXDytJPYJdC3nSAydJsNPZDDOBsRmmVLsPEMTZe7SiYv747_liPHcWt72WVtyonZWo0n8H_KvgJEczEf1ni0Ms5w3bRggWQPHfmR_6jab3jBMbIAH9-juEmVAM2AenU1ZQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم
همون ۱۶-۱۷ فروردین، کارشناس
صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه
رو رها نکنیم تا قیمت نفت بره بالا!
و فشار رو بر آمریکا اعمال کنیم!
چون خواست مجتبی خامنه‌ای اینه!
نتایجش رو هم همین روزها داریم می‌بینیم!</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grT1IV8p2uZrOz1ma8v9ymcZ8N_fcVPClbus-hnp6_KVfyNPG20yVE5d9eO_JvK7Zl-lV2uz8RBDiRLV8q8vyDT9epBVr8gaberG1Im3FgK2f3QgHYhlo3o-WSTmj8dN0rFt4TXrB8JRiRMOYE2fnhODQCuAfh2PO9ru33VqNJe9qnSaHNVfmkYm6VgTDVnYOwBj5X78A-19xlJrZEoQkk3CLWpCcrj1U3SvOhrb6k3wMwhRd6s2OaZDQOV5E89dM4YwGU2S1p6zMVTNt5xP6o3Z9NiheDLaGg6VkYupWHBbow0JsbF1ZTwFbyVTX34KVyI0JxCURQWwnuQZxhojyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 24.9K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=Lp2owU9-4FFKlWjcGiFB40L6gfVxD-paBMQ9NHWBgrp2UYWorNHkV5NeHTqKButK8_DSXhwxKij_f6ZMuBG_9s4EtAT40l_w2u7H0nihQZvo5uONV29OpZ27QTPaqbFDKMDs0hHYbVWC4Ffh2l43kbYYJLSw0ByGVDkoj3r-TkL8E0viPYNUvIb-tO_hHg0ArDo9qU1wxG_JWn20EZwLpQ2AWMhchnQ1X4uxzpJ7F_YTpF8DXua8D47A25cHDFjR9XYaYKQ7m5wd9NfSxhisFe-j4CDoat75igJquR0fylZfEIP7qU4WV4thj7qA5oEKf19lCxlyrya78zDKwJiPTYWOpGPPJgrUDPjvR3m_yJOfwRxPGsEpzEljmzYPM_ib305LxFaLPd8quvZ40nG9StDJNw4Nax8aoRuL-b8n-6oBPvwGr8dv3EhiyaKqNfG_gV9yGSa5ZYGah72x-eD3NdPOT5KFLz0rHzzCgVpF21iBWL2Mh-pu7emhKtuQ6RrzYc-exPxNBiFoTJJ4PSz4BcA7I0RbPUvvLPVvJS478EhQjqh_St8RHpk-3Wpaz8lMgpmY2V0l6NDEKTgkiX0IrwOxzwQ6jsb7EQRO3f6H6YGX2g2aDZYSErWvG97giqxzjDm64dEXG5M0_9VmmbDUMpm4EEasNpxSft6FvnJPxA8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 28.7K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=SFny1EV0pLB7td35-R4uvuwk0qgez3cPcXiPXNMSMIHjLHSgui_TB-Qg5VDb-Rvze0NSPThdssKA06h9iEBvsm1pK6PZAxKBVhGCBugCJq4zFhlSinoXVW2cvEWuDnPkegaNAqmOcq1MAm_1NRYKlmkMz2zjbPl8v5iRdt8HM6XcuVyOUAuyqOPGPQJAT2v0BEXDS6ZS8ybtDbUgm0HIS4b2UBgRPKnDIM5Y3l-Sp_M9pxmXdC2LcLpQFFIpkFl_9pqi_xNb07sO12kpRJ_0xegyVzIgCVX-t_9F14DyZjAVXzSFtz8Pfksztr8RFqNfMRnrXknkLeZWOCUsRrMd5g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 31.3K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 33.1K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/EueTBuooCvwrY2vJWGheBKARvS4U0e4RjQ5XUI3XFJ51_rTa1W6mDVUaZDz_aCvZIf3X7E5GRiSzXDBP1HR3OnoQMJmgSt6Ms3D8tj3cyYBHqBTU8Xs9k9Lv9_nfiIFFPERk9WlkzWzYJGrWR_7ga14EPIbhPaUFLXRh1hIGrz8_Jqk1MI6_0X7HkeZq91rNLJAgiVuH0oY6VahS10My3z7nxxY25S9mRWhxHZ6pOTjH6yWA-68SIIHCSRsVJ6guAUN1WB9q6-NZ7CBCftW8uFd6MNtbPAEVZ47dkaxWhBg28x1JAfSESfOIeyiTcJCHZO0FQJbfJdsveJlk95UJuA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/W-Ar6sCX37U0o1Jnx7--I5kqmQhmoKVALNiwRQdCxsnBbIWAOMNoY7VbEAY-50fgDBq3lRdxg4gHrJnf8_cwE2JzH83JCFk-4NG7qibfNFHubQnEpR-YuAEhFLTSIbDSQNh9f6999H8qxJWIRbOFFRYLB3Xbk-cwZ8xk63cByWi2rPDBQU8dpqXUArPs9ki-o1f-Em1t1E3sQckWN45UV7ExRXvSmGIjovngHv42jV8Mpa-WDolmwN41jqqU_MBoNDk5iXiJwtOpOWouJ1rHmhOaN9a2U7-kZpHI7o1Hy5hE5OYamJyJcROXeiWJz22JHqJOfMF3oTUERXNc39qGQg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 36.2K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ufEQYeO0S9if3aJcIVB1qyNWz1MuCGs56eQj6rUnt-9_-g6L6V-aVyrxmKUofxfeNPE_CaLNpyG_JCLXc1ngsK0L6Htbk8HgbE7bIkaRlg3O-gjgX15aVLJGQWE2n1IwSZgMQZcm6dV6_CxcBoUihvor7ZTSiwG5ABfRcFMS0hHDUma48PTJTAvpS-m_5HF1xj-lIb4VzWXkWXiXZg44LVuLQ9BDdPv8ianUw6wJTwG8pnO5uD96ftbyd4iUsPXOlxuIqrfm_gZ12JwdCpw2mf__m-l9rCYxqp7bjTTxNUtKV3BbzBoVmjF3iVKl5Ane35FM5XHT6S2bOc46o_Z2pg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ufEQYeO0S9if3aJcIVB1qyNWz1MuCGs56eQj6rUnt-9_-g6L6V-aVyrxmKUofxfeNPE_CaLNpyG_JCLXc1ngsK0L6Htbk8HgbE7bIkaRlg3O-gjgX15aVLJGQWE2n1IwSZgMQZcm6dV6_CxcBoUihvor7ZTSiwG5ABfRcFMS0hHDUma48PTJTAvpS-m_5HF1xj-lIb4VzWXkWXiXZg44LVuLQ9BDdPv8ianUw6wJTwG8pnO5uD96ftbyd4iUsPXOlxuIqrfm_gZ12JwdCpw2mf__m-l9rCYxqp7bjTTxNUtKV3BbzBoVmjF3iVKl5Ane35FM5XHT6S2bOc46o_Z2pg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dmwYwSxLQD1g7BM8MkzCM_QATzx2xcdNZQVFkBwiQ4LsKuGHCfuHV_B7h1SRwcbt6YuF3u5-dtBzf5Yw4vrSJZwGrE-9wycf1gFNOt99gvievyT8jVZsC8Xc0sMozi5Q-rRm3Rj_4jHu7aKQg5CA8bS3qi9l-L1WK6zjyHvEjPvnbx5agOaUaQVzw6Qvt_QcKlXZELC39ivrzrIB973x-E37CkFDib7cq2qM5Z5GmS1h9FwVxZQN2oXyNuM85sZkUhsoZHLgyl1QGjKd46DfyNBG4ffCaRChUAQfxPLtih_aVQzYS_eqrQV2eoxfyxJ-TOOG_0dIvlC5djlzmiNVBA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 30.1K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ksbhiu9ABNbem22xPgBXxK-vNPCX2qBofXi_wTOle062TyXvkUfAALebsjFUtOdojiM29hSnM10uAgPzqVnov9a61JAI1n5vHtHmnOBKHSFGw6GyfC87VGe1EgYV_WVhn9nbkn73qSAIlas8n_DfC8B01l4sJy6-a7zJRM_cxi7cN2FXd9EPGhII6cr5kB36Qnar--UaT02PsvRxXzJnltUO1RMtcnM1d-j_bkuKW3Q6cdAo1be9h4fj9PfjDfNsVKWdbfJeYjW1_s2wbBPQYNAYVKUW6a1S6jh7HJLoFK7pR5jhkqMXw5NfNpPZ77EofJmvgZRTveB5Yp1gsYKrQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/h65l6tQ5c4rYxUu2a_iXHVm5XSvsOIhhkkqwmHfdphiNHDJf_4YzoGkAm6a9ME3Wh88I7GqZhM9zv2FY0UGawxjkP-OYS28wyftciB9I2vKOB8XG_KjIzh_FGsIgimM3b0s1poy9_urBVrnzq_4oDdh5zIvUa-YtLXXk5njXaSshZOL2ofc1FTZdJwpZ9hTZoJN_BLkKIVlAUoz9ak1TIzoMSNkiF7_NkVpLedA_kdJ7073lL6tOBzy5odCNNuWZmMsg_Rz8VbQUFVABAW_da1L8OxGJ7LnNKntp_tnCdC3-_dByvwRCQ4BcB7Vu_nmfYJ46NVa_X-jE_kDYrk4f8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=rETAhiMVA2hh7zN8Gs1_2vw1taZN_M6zD9d-SNdw--h2G-HLKYH91TMgiCJ79JnlJn5KoPquGBbmRuU5H1vxwPo-k3MNAcsLzlqEFVpyLiHwufB-aqmSmOhQAXLHrhjq8PXiQkIhukayCirEthOKNOGFi1xrMUiNcK0cvs5kUyDT6jaKEaD-_RxylzEa77UGgWRueF-OiQXh-yS4f8UZyVb-C1AAzgSM_qVUY9lUzDwmAt-fGfqXZDXddjk5uzFGvYYFjRarjDFy-U2USOaSoD4PkSBqfjNb3XEv9cCnsousTflXf_AJxRJPG8Y0cNrwxgsv_aL-Nm1FydYpii4fPA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 30.4K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=JC-oOCrD50DNiNzmvgbTNzkSmBcEkTt5821TOtl0cJtaLWTxSNhOZ4st0iOJ2amJSVAmMlRtbcmX-24-kZegTYixmq_hYtqJjy2oPjmmbVsNQ8sgJNVIlk3uc0Z9OQUPQo8EEt7yOJj1hB-HbglmGxFIB4FjQuo4CSfRNbj8Nci9Eo1tm1nRuz-emyEmrmA-7HiwiwObSUt3CjmssMfjevMooaTi5n2oCcjtHqRhShbkTQvjazPiSD9IdWVfIcHdTruPkKkXvb7Ll62dmXTp3uJmIrI1RWUC1S_Ul7-HekSuUyUf5qeqA__zaYLNVhwnGpd9v-TAD5oVnB_68dwRGw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=reT9JhEyoEYV8Qzv3zIBRUU06HA3CJen6e_klRKxcu-bOKaWwX12uaOlZ1l_UtZz11ZdqXYI7ChS_MuR06o3uzPRkmjzMxvlJN0SBsszVfhHd1Z1QJxMlA9uruddIHkp4z4basD9RRdQjvv9kDoQPsxl-lpLDRcs5MbThN5fZbtBNKDAy5rAPlfKsHmYFecqVKNF24gnIx9l2YHA7NXEHtw5yhJpGUlpFHrfs2wHrK6qSw-_1kbxKi6ecx12KCTHJVfZlpSKB3SFwe8HHTPq2ejrZYTQGgyk-Qy25VlRHZcbOAByzJhhmTJcXIXRFmRMabemb3mV3ZKljjtVU6rxcRXXtDwlOoomKbJfFf5MI1mirO1jRbebRNcaXNiPGW3JyV1A_OCRnAxqHcWZdMFe8TTep-HAVcxz-P6QCom4uDs83IVK3WiQ9iAwYQcj_5iNwAzBYPdjpHviLpdWNIKlHDo2YOw-A-uyxOxarbQhH3aetNMzWSkHvSphAta0TTX2z7Nku48_-bMTIR_5JgicfPV2rJZCa5BQJmIn0WvCiTtkrmfc2gLZQdzGy4x80DWd_bKeCGX3sE-i9nUewjB-MPGa20KmQIp4ls1QetrTSiYPmLHQH399Xdxienldp0L6Pph4-e0-4Xx80D63mY__WSBxCjzHbsHi2OMEVuediss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=reT9JhEyoEYV8Qzv3zIBRUU06HA3CJen6e_klRKxcu-bOKaWwX12uaOlZ1l_UtZz11ZdqXYI7ChS_MuR06o3uzPRkmjzMxvlJN0SBsszVfhHd1Z1QJxMlA9uruddIHkp4z4basD9RRdQjvv9kDoQPsxl-lpLDRcs5MbThN5fZbtBNKDAy5rAPlfKsHmYFecqVKNF24gnIx9l2YHA7NXEHtw5yhJpGUlpFHrfs2wHrK6qSw-_1kbxKi6ecx12KCTHJVfZlpSKB3SFwe8HHTPq2ejrZYTQGgyk-Qy25VlRHZcbOAByzJhhmTJcXIXRFmRMabemb3mV3ZKljjtVU6rxcRXXtDwlOoomKbJfFf5MI1mirO1jRbebRNcaXNiPGW3JyV1A_OCRnAxqHcWZdMFe8TTep-HAVcxz-P6QCom4uDs83IVK3WiQ9iAwYQcj_5iNwAzBYPdjpHviLpdWNIKlHDo2YOw-A-uyxOxarbQhH3aetNMzWSkHvSphAta0TTX2z7Nku48_-bMTIR_5JgicfPV2rJZCa5BQJmIn0WvCiTtkrmfc2gLZQdzGy4x80DWd_bKeCGX3sE-i9nUewjB-MPGa20KmQIp4ls1QetrTSiYPmLHQH399Xdxienldp0L6Pph4-e0-4Xx80D63mY__WSBxCjzHbsHi2OMEVuediss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=j5y1cNjFIhXEnWxqW1V_LpZfwCM0ObyB_0HrlGps3ggNkeIeSnGKhoxRLFYzo3TpBiEq4rfGSpqIvlkx5yoMdu6g8bmYaWDYz-QHT2b25ki-8K3tzjDcnwgenjwUrrxpOXepv7eRRQwCv-3nPkTnE4jQAoV8gA34_7N3FMpmUrSJ7qvxCcZLmezWCMH7lBBsyob2RQy5GjxHaHXpCf9nxw7ukyjvJ3iOHU9OGK6kqf-ODH12EYBZwzWXi6o4LNPQChTa_OBHnZOWv3Lffn6fW3B1Hk9FyC24g-XXO1HmUXVb14JBpunlc7NWyGFGtGYwKQYIezNc6aaDaVQmKBB5sa2R_2q4tGqXjYYkRCZJjycj-_uNIdoltnKkBLVqWdCnZs0BwVmth_EgTq5ewkzbFK9nn0R-RjLNoe3uOlkPODm5TN1gV_lWofJ5btDPhRxCzIT6wF0HoD8GPOScwH8lZ3NoAMGVwp8z_kx80yT0ByYy9EEqz45XCuXubJYu_lQsiPMxktkMl3Kjmi6fx2O0C2fEb8kHHZg32ZqnP-xDgZxqJCjsb2hNyRdDwJaty4YFekFJv1IDK_4QdgAZ206TiodzE1i_QHnRlg8OHvuoWB_giMHF56mG5Y9JB32CFL4u-u6FowbSUBZP0eiJ8vfkDPeQRUZ8AeSQwAsewboitoU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=j5y1cNjFIhXEnWxqW1V_LpZfwCM0ObyB_0HrlGps3ggNkeIeSnGKhoxRLFYzo3TpBiEq4rfGSpqIvlkx5yoMdu6g8bmYaWDYz-QHT2b25ki-8K3tzjDcnwgenjwUrrxpOXepv7eRRQwCv-3nPkTnE4jQAoV8gA34_7N3FMpmUrSJ7qvxCcZLmezWCMH7lBBsyob2RQy5GjxHaHXpCf9nxw7ukyjvJ3iOHU9OGK6kqf-ODH12EYBZwzWXi6o4LNPQChTa_OBHnZOWv3Lffn6fW3B1Hk9FyC24g-XXO1HmUXVb14JBpunlc7NWyGFGtGYwKQYIezNc6aaDaVQmKBB5sa2R_2q4tGqXjYYkRCZJjycj-_uNIdoltnKkBLVqWdCnZs0BwVmth_EgTq5ewkzbFK9nn0R-RjLNoe3uOlkPODm5TN1gV_lWofJ5btDPhRxCzIT6wF0HoD8GPOScwH8lZ3NoAMGVwp8z_kx80yT0ByYy9EEqz45XCuXubJYu_lQsiPMxktkMl3Kjmi6fx2O0C2fEb8kHHZg32ZqnP-xDgZxqJCjsb2hNyRdDwJaty4YFekFJv1IDK_4QdgAZ206TiodzE1i_QHnRlg8OHvuoWB_giMHF56mG5Y9JB32CFL4u-u6FowbSUBZP0eiJ8vfkDPeQRUZ8AeSQwAsewboitoU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=uvvs568QtPkWKWOcpUuIij08NXksRj1hbpmlZhaccWBLFM6nlfaTMJVsN07AceYj_grTc92y0jR8SxDs3BJ5UChPRuiCmnAHbSy_dylx9hQe6qxn7YUNHBJp7WExfVoKs0Swdl8pwlh0-sgpli2lWfPAqV1m1_sBbbIK57QBuVN3DsE37CYLy8T2DHENuEsJHkvrDkaFQftGrOOmvsuuj4BI1AM9kYpfPb4tYuclp_cwC3WitYUT1kIOPRakKBYxBvic6GvByhuolRPiwPxKi1ZfNsOzd2h-fjM1Gf9XUqbdauzIX5HdQN4A7YjhaZaMPvnJQxkcavEMl2hyQjccmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kTF3R5zQTkP99Sp9BXl4jNlBES3C_yqYJBm_qNrv2pIP3sOJMmJa8LUriT9BaiT5BaYR1c4LIwLBq71_IHX4B3k0JJid-itdhPlzvjLWyZ1-5ueWXsFlV7KGrYECnB4ohWnmXYGH6qfrrUxytCd0QKgMSKBroBGNp3Q2ZKyMMwJeqxXroELNtegpjASFMwKIoidw9luPQCh6sp8V4K0McCi3yhibblpDZ9DVBkX_E7aUJ3DMH8UcChoPGUZ0vv-FL7-Ly06Go--jXydk4BB5AxuPQ8F4SNkPdWUFE3NwYDlJ4z-ivAmgyTSEkRUrZ2_SA9ZiQuVTNPJ4s7ExEzm5uw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OueIOHjNRF2QGqUxmFhpg6EWRKLVbNE59zMSf6VusSFVU4seHC0xh3AsrKwirzKgR3qK7r_G8fVc1KGsRJcxVUpQNbreMx7gpLBg7MA8QnxkzLJC_kuRfT6j55yEXhOlNV3MvCZZSa-Tq80GN3aTMbJenLhYyg0QDe4yBxNy3WWzrvWw5xzAX4vUNcFPW5kbLzsqkYeDQUjHWuMuyJGHzzReD-bqH0NwEJQx3-7-sCmoVTfOugXkqK2zYis_MOXlnDWJdhBgqvnalA6UGUee2bj-Y2Al-F4kWGpLREbWwsaXUuNNaMvqUim6PuqhXxgdUAm4CRjWkiBPEJECKzmY6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=OueIOHjNRF2QGqUxmFhpg6EWRKLVbNE59zMSf6VusSFVU4seHC0xh3AsrKwirzKgR3qK7r_G8fVc1KGsRJcxVUpQNbreMx7gpLBg7MA8QnxkzLJC_kuRfT6j55yEXhOlNV3MvCZZSa-Tq80GN3aTMbJenLhYyg0QDe4yBxNy3WWzrvWw5xzAX4vUNcFPW5kbLzsqkYeDQUjHWuMuyJGHzzReD-bqH0NwEJQx3-7-sCmoVTfOugXkqK2zYis_MOXlnDWJdhBgqvnalA6UGUee2bj-Y2Al-F4kWGpLREbWwsaXUuNNaMvqUim6PuqhXxgdUAm4CRjWkiBPEJECKzmY6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.8K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24.1K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=FKiGol33oCTQ3ePr8P39KydWAc6f5gWii2UzdBwVoIRom1wHM5AJTGg9Tjzi5aszJCd8_ZAnUMrymTMGBFU8jUOt8_fVQ8uHOMNCXxuJoPylpXaGDbpSLK1TcpC3IOGX8LCwMCJQQrRyRIR8r7lRhICApdnl9gsbHTpq5D06jy1WkWAwpPSceOpuiFkKKPGm8swmuNBE8l56gzwkpZTFttdh-KWvR4rJW3zKOVv6pxrE1bJzfuRjuCumEDt1br8Af8vmh4PiGbHOEVUXHE6TNfcsHb3jXvDVdNNUU2opdhzOkc4SLh9eUckRwVLOPB7IPG1btTJqEeYs32_cbuu2Xw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WJ4INwb_9eVIfVgpveGVNKmztQ5k0TUYMmYnb00bJ92-aWHfaxZ1isvhYRnSYnUthxCYkKQeoVC7r_ZfLrZTEArfznmaJPgbKtwH8sTQyG9-dU-O1B5rSwDn2aoAvLypHSqpXhqFTaB21I3hPpfUvQ14_TI3qTDZEcPDua9Lx5oYW8ZtwjLMkiecTfHY4FFUS_Uv_Pc5fXoSgmtdrKuVN49gjEKqNFFobG99NtzMG6nlUFJZFMbrEjAuL6P8txgsmevLy1H0i5z73jv89aswJ0aLlsl_eO2xK-xrv6y4wyU1CIfIg3_DUHcsenpwqP-sttCwir45z6TrVzbTfr9W6g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PJqeDIts_h5ToP1_adc8S_2Waj4ITR_7MUTIGXF30YfOyU3UKKtBYr0vYWbopO44tf0SW2KOR7g2PaeCuHZzWEu0W0nu29Rimt2TEl0AptjXf7DKPtG1HerMw6iOtRy3TJw_nw3ktk-KyXLVEwJmwYRELGIQIzrQiO05gU42HeP0TlKnpA_CpPsckuFDtFiPOM7YURXD3FSBlHqO93B4z-YgXVtMsuUpvNNVLsukGHXKalQRqDUgrx7IdFWOLGhAHFoK_L0THxXpQ2s5u7jwbU0H_LT6I7WifRfGUlNIgK_MUe5Z53cd7wonpyEssld6wQC6x_6dh3btnVKioVIlTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.2K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/DbaRWFc8sLeAuO4JjzSrzSWdjD1XNY5uURpYUUw2aBM_xTNMgUYPHeW65KcsdAuLi3UTu6IYJ_y-1YVxqYsG8yuT1NQrZczNcihBDgX7TzHmc0170naIViRxRl2ri3ikQlQy778neGWkUdSKFh2HHOoyd9WUfJxK5IvIh7yUMMv_7zWJv4hBvthhX486RPAUZPqjcB--Y_rpkS9QP10BlhAJqZLXodpNI1RJabirHRXZpBIpFjjrR2hXaVu6PIS-iA2VIAQopkxBT2FSAuVTrRnFC2kQIAdD7TeM3GVBHADcJS3pAzhYz5F4pZhIykXZEohlTDL2EVlOj_bA_Odr4Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/LVFohCK3ci7H8Y5QnQf-nrBxgoujUgBvuqXVchXxZ1CWD_glx3thqnVTQdUrpj2JjqQzRVJkT5EVXH2pPapKQ5rewXi1V-oF1_DmFwz6qYgwk7SoNl9JvRlmrKOgmQbsVBBECMnXiHxlCYarD8Cfxi9K_5VOZMFE5itxmHHO9233q1ELrGClw72y_JtPU60Hf_DooN0DfF5nB-WAj_HHnVaQ1iFVCHm9e82x459EbGRXS43vvdenZxatYDI1GgfPNMn-ohkGy3wrQaWQ2aOZbYzQ6kx8ANbD2Tsrxx-WM-YNMHUgM6LFFMh7D40VefTSo7uXghuM-gYXqrnlSlws4A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/U8L4XiyL8s9z33d0j3PpBoSlJ4KJSZH4gy9CmGFKxb42i3-OLbTy336sdt-EOeuCZOoQu9ApotjDyS20fZM3BENZqwhlpYpcj4igRyTW4c4rdOqvlcRR_K0N3ZiZ4O5yp2XRVkcBtlH6tP5HxF9I1A98vLL3EQjm4HCV-MZgdLXXOFtHum1_je56oPs4cTJX_5oinxF_GncsSLtvWkHq1XTmFZ2eXF7xcMCsaRBLiOh5n3ocH0csGXHHHQP8_mQjVtpPmH29xQrRtAJlhQQCBkWNpVnsYu07Ewv9LFaEOMwfiZQtTnMib30B0cc7nxNdf7SqB4qy9OXWWDPXgTkwng.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uYahaMcSxRhmDPpdACyqSAqVMBRoBl4r8kw_oyhFGqT54vWwSr_zTm60PoWggvr7CJujHX0YDvW943gU0CXkGyw2QjS2Vq3WqXSFKieQ7C3bS2ip7q1Ry96B5kKXj5b-Shu3BwCwj4GKURC22b55n5teBiSwAX_4XatINvOTLe2OxrjnUmcYcq3PPwmjhxK_QmzXF3-jmqthqrqK4cSSHNrIMfOslULTrQLwtnZ0v4DH-UNvFCH_vm-8uL4q0Px9igiycuqRmhmKtbQxRT7-_E6WgwF8fO1F-svX4QA88hlVzNU5Fc5l6Kleng9smUMLVYn2hhM978zgGZHwFDtq4w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.9K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XFCncvsnlIFY_ZZWxjSvKcCXCaQD1Cs9TZnW_DyKNKxVHq3gT58Vkt5jaLTNyEsB0QuZep9BqlGCnrbBk_z5UlNE6xvaneCukVsuZFG_yl-IVrb4dOgiSbXWgAfsMWum9ouQfoi9ySffQCOpT9CMj11Qv7zfynHOUU50exB3cCOXsNkQSuXDgbtOnfFw_gXY3WsISNs0gl9FkS-KfJoJrQzIr2XQi7jo7nte4jQN0r9qmv8aolBWBPhZNOQ9R-kYsnLWo18OSr4T_VVnj-jpx6KShIEyVtCGYKF8VLO0AWAbgCvWtgIQ6HPgsRr6qwnz7yEHNBy3oedAe7esN9aqfA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.7K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/npebOxhcWMJdm2oT9kTj0YbN3ZdD39QQVoF7DYDkPCFeI5gK-6CAyAInjeU_kWbZXHymylQbyJbW_AncqPze-9Pa2zudnJewSIGxmrnuKZf7ASoSYXefA-FztvjHrHVfAIhrelQUSHyWhhC_bBBsjf4Sv8DIVBUjvMyoQ_0zy99YdnbjqgKOfhs4Q_WqwHqqukV7xcMT5uWBDXIDVTMz7Vso-4VY3APT0tTGMLWA6jI3JhGs0v28QEAfClKLL6qklD5Iyx7U6ZcoSvUUavcQzzNexO5uUa7mfdIgOJPMyDJmP2i0SF4xRMdaGZuuIi_eoS7gJ_mbVvMNH_KVF7332A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/dwH076-AYyvX6YJ8cDFUHfk23Op5FPxuHpave_csuzENad_cRMw3ea3N3VVygGF6j-RTGzss_3AQiflYaL4h5_cB5i_5ZcyxlohvdQasO_utchzw5mTElZB4i8_vVSZCr0lbEZIdEDonMBw-ZnEIvOo5Ae909qA93666D6GVJ4nkVlEjhGkfyiDdBtSfA_bmg65M8sSW-zX2qNngHC3PBZ-SEXuU0z03jHl_AtYlQ2Io3_r0tHvaNva6epYs5ukfiuSQIv1c3_35DVJQCoUnEbboas9g9mwFoEsPjgBucI-6pSoJeKTQF6zCww7LLzZ_JNyw_sWViXq0qICgC_MUiA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rTf93Adi-MiL5RQK68mBjts9xcxijRY4twUzxSCxZbCMZZVXcNYmRDe0A_A17qnMLjd2qdnFRaY1cJ-KkaUOjV53QKL-V_ckSHFeWK9SACRQ7N3c9ujUX-oEc0dnC8gj0fez5Vat5c4nGK89LNmJtq76a5tNEZcSGJaS-Vx-S7aXpmlKk9-Gn22ZfA6L9Iyj-P5kaZJOQ67LFJQa7ItiXxZvJnHBNHA8-7MRTYLVy2qb6vMUrZ3svX09Gz-SHHZFrWKtN8-YRGQFajzDJCDo6YiogVlfy1iF2nMsOggE6VYyssPeaouWI9Ho-EWlGu5uduSUqT8_H4IFvkiV4pqirA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.4K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">🔴
حسین مرعشی دبیر حزب کارگزاران سازندگی:
«چینی ها رسما به ما گفته اند؛
۱- تنگه را باز می کنید.
۲- عوارض نمی گیرید.
۳- مسئله تان با عربستان را حل میکنید.
۴- مسئله تان با امارات را حل می کنید.
بعد از این آقای قالیباف می تواند برای دیدار به چین بیاید.»
نکته : چین در ۲۰ سال گذشته کمتر از ۵ میلیارد دلار در ایران سرمایه گذاری کرده، اما  حدود ۲۷۰ میلیارد دلار در کشورهای عربی سرمایه گذاری کرده.</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6669" target="_blank">📅 08:19 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6668">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
۷ کشته و ۸ مجروح در پی حملات آمریکا به خوزستان
استانداری خوزستان:
در پی حملات موشکی شب گذشتۀ دشمن آمریکایی به ۳ نقطه در استان خوزستان، ۷ نفر شهید و ۸ نفر مجروح شدند.
🚨
دولت پرو روابط دیپلماتیک خود با جمهوری اسلامی را قطع کرد.
🚨
در جریان حمله آمریکا به کوهستک هرمزگان ۴ تن کشته و ۵۰ تن زخمی شدند.</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/farahmand_alipour/6668" target="_blank">📅 08:18 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6667">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=ALreyFGZf_hNxQUdHafqGuNg6OPSJkCIFly2Vjtvq5m5xhzlAhxuGriL504wM-PiG2tC57Lcvdf3WOsGE6pl4zXhmtZy5Ki15in6yYhFuZEmCC8jXB8R-8elK3LpAZ7OdQ2NDRCv2qSgU3Pt7gKh1vicpAntcp1Lk7gnU7THyNio1soBdwoh60z5AgeDUGwiO598kyxf_dmI-5WHHG4ploqrPIS1j1o4IpcVJChheM1KOG88o48YfwNUdxhlku5YVR-gm7zGq0l_zOG1gCU3JOxIqmo8MftxKcP5rUjmf7Dosg-IjRqiT56w4zbUmR_HuvaCDJ3Q92ph5pRy6dqVcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AR2D42YACD1KXbtTaoNFV9j4v94XAAgXnG1ybs51KfYOotYKSFh1zOyLaGIKp80cVPtJAj6XjJtLyNK5rip9vCFjaiuTPhWbhpzR3ggYgkA4BimUslWn5QCgKOQfVar2KG-w_01kEqkk9XZZQOS-1eayAVEjG0QI5BVgfi7xEcAqfO2xNVr_qgqdeb9PbraBarp8XqW8-A8JmFE9qZk16BryitYN93ip24GgJ_cLzpKEBA7hriEgY_vUayNKun7gYSFYygr17bRXJkXdwfw5yq1OdYY2C0uUR-ixrmvNaDtAwPGDzK-26vsg9Ia4Khozq9MV0DkjkgeTBGo6NQy_9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hHXdDJzcgf80jwfN88Bp12tHYKPCWy66_25bRYdCRZ9HVpgV0L-7ZTsPZTzACQq9sQF32bKCpau1I4ozSdDa1u5VGda1AzwrMMAtMjxiyN6jr6EkYQiCp56e2T0E7xmcTd9ce--7TWFlY7I1bhyQOPlAe3_6VUlZ8-0hbEXJIoXNtS0PYD2nZSSdtN80n4hatWXxQSshADfImNT5gPaxg_tOLoui7UEstBrpJ_7zARAzVRyukXsYre7l3tlTZnmNdleGRbZIrEPuvFjMu4_bUS8BgB98UDSTVyenlzwGCd6nwMH5BPaTINEIgCk-5_THNL7JUsEZyiQXmxtRco-Gtw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=qqM_qvSfKH0mh4KiwsvtUsOuI-U2SP-SiFqY_tKidYUiOzILh5ZJuG6eACF-gXRsWpqCjN623wZODxIdbqX7h_4VRxCTwViz-Ask-qD7mXVWm4p8F206e0N5psTCzEv1SuSU8U3Q3APnXaBg1O7pNcPtk3j2wExKIRuDqK4cLRm03LfxaNkl4odi-gX9YHKatE_dAE-3p7kPXkK3ssfJJRNblgEH1z5kvPoni9k2NV4X9LfDrngFAh4LfqOtYRl1K3sXBdeL6Urv1w-qC-7gsakHm5zPUYx0K4DoH3dS-n5qIsIchqsqvHlm-xL4ZsH9_Fn8HTaNUwKGlhEu_gqI5A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=qqM_qvSfKH0mh4KiwsvtUsOuI-U2SP-SiFqY_tKidYUiOzILh5ZJuG6eACF-gXRsWpqCjN623wZODxIdbqX7h_4VRxCTwViz-Ask-qD7mXVWm4p8F206e0N5psTCzEv1SuSU8U3Q3APnXaBg1O7pNcPtk3j2wExKIRuDqK4cLRm03LfxaNkl4odi-gX9YHKatE_dAE-3p7kPXkK3ssfJJRNblgEH1z5kvPoni9k2NV4X9LfDrngFAh4LfqOtYRl1K3sXBdeL6Urv1w-qC-7gsakHm5zPUYx0K4DoH3dS-n5qIsIchqsqvHlm-xL4ZsH9_Fn8HTaNUwKGlhEu_gqI5A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.9K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=s8Ix0HBQTPe5DjKDpnE7PYtao58Vs1kisEpvAi19J-ER3x8NvavIiFdgMtWnlTNxytE_guUBBv85g2sZ7-gCF-awpryq55dpGI0bvnLbDMOXIpwbD2vahx6Xua3QqZ2SYQyXU5OOapihaOUaULoLMVqPPU4vCHR8gUoxjnJrEqTsb6QJ2kgqQ3F0xOJLa2UuS8xTlU_QCz8qHjcyeZYQkOgIK8trz60wg0PWK692Ve9uq37bC5u5FDEgGjr4DQ769VRymFmVk_T58J4-kHY9Vsxtyj0W5QjrNwkldQjt0iJgfIP75hUv4H4vKf72MU6KxOEW8H6_Hz-nX9Y2UVuCAw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=s8Ix0HBQTPe5DjKDpnE7PYtao58Vs1kisEpvAi19J-ER3x8NvavIiFdgMtWnlTNxytE_guUBBv85g2sZ7-gCF-awpryq55dpGI0bvnLbDMOXIpwbD2vahx6Xua3QqZ2SYQyXU5OOapihaOUaULoLMVqPPU4vCHR8gUoxjnJrEqTsb6QJ2kgqQ3F0xOJLa2UuS8xTlU_QCz8qHjcyeZYQkOgIK8trz60wg0PWK692Ve9uq37bC5u5FDEgGjr4DQ769VRymFmVk_T58J4-kHY9Vsxtyj0W5QjrNwkldQjt0iJgfIP75hUv4H4vKf72MU6KxOEW8H6_Hz-nX9Y2UVuCAw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fMWUt7e51DaVaqcYiq9Z_eG1-LtyTh-xDlSaaAphLEIBPX0I63vSmRmOCfbyyR0uih547ZqRfhW9cilaNzmCw43-AJPVibD7BvQratbqYmjzEAy_h9HBbpNqdk77eRsSfxozOQMsdsY4a9WHcNdouTAyUjhzpqD6Oz-f07bjThBn0ed1AEZVI8HM3f8r-QTNP1QC87u3BYxoRDVmkOGBjk-4BGBT881YvTGetS65RmzHrDZr6qHBhu0sR0uqN-KG1maSOTyqkC6SksucxNHJEZOh_07BbKjyHFE7bnjZx_Iw2q6kuU-Rl_3nrAEpB36oxcNQdBrJcGWMuke7ozltpQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جنگ رو به بهانه خونخواهی خامنه‌ای راه انداختن
۴ هزار لبنانی کشته شدن
از جمله بیش از ۷۰۰ کودک لبنانی را به کشتن دادن!
قالیباف رسما و علنا گفت
«برای جمهوری اسلامی» بود.
بعد دست به دامن دنیا شدن،
با التماس و با تهدید به جنگ با اسرائیل
و با قراردادن «پیش شرط  شماره یک»
برای تفاهم با آمریکا
در پایان دادن جنگ لبنان،
اینها رو از زیر چک و لگد اسرائیل کشیدن بیرون
حالا اومده میگه ما فلان کردیم!!!</div>
<div class="tg-footer">👁️ 32.9K · <a href="https://t.me/farahmand_alipour/6656" target="_blank">📅 14:47 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6655">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbmZgR4PYMdugebZJMx6lN3fBqNi_ydlmA6GvLYr_y1SdcRMmcLVqj8UnkyOiZx1xK-ujU458xAiwtBO3ibs6m3sYhcHDusiC5tkwy5Eg28ryPjvmxxAYSIN1wGjjDRGil6SJhOKTrgVB-ctK9QAxgk1falojao6_saAW_VEj5Co-XvvenOX-kzeauJvzxsWPZAkbz7uRCn0f7m5QBBe2-fIzfQ1cO7nE284GLtRcduNv05SRkyzCHwZ9V1-mi0VQDmX4whrmc_gSU_wL0PP_eImXM3Dpp33BJesCvwO9LnIyChEXHVJIMz5tOuI19vv3w9bny0-mRsbseSbFew1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">داریوش، در لس‌آنجلس روی سن زنجیر میزنه
محسن نامجو در ونکوور کانادا، سینه میزنه
دختر بی‌حجاب ایرانی در کانادا روی
ماشین قیمه عاشورا نذری میده.
ای آخوند فرورفته در مغز استخوان ایرانی!
روزانه چند جوون رو اعدام کنی، ایرانی‌ها بیدار میشن؟ چند تا جنگ و مصیبت و کشتار دیگه باید
سرشون آوار کنی، تا بیدار بشن؟</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6654" target="_blank">📅 19:13 · 06 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6653">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V90pIsz6lwdFbvBSxbrnFV-fmEw6HakXbjiZTmQ1mx3SVJOzRvLeSXaLZpodcdqgfS1xP9jBAaFPJhGJTLcKNA2gGes5nSWhQWNMYDch8d_b6Nbo3ui8NAHqUyk9NNyQwPFznQhe6W_m394T9EN-QvAeqQgYkiaYBzo9ZQZp6UnkhLKQPkwfpD0gSF8jBjJHrrkWvTJIB0gQXf4a9GSonInosgmdSDPWXGNrhgchCZ_AgkYNYI_1JeikKnsK4b6m0to7Qy4G48hov8tAjxyeVRiaz4Py-UY_DYiZGIiTHrtDAWKOWNrXJ0JZdvPMjI8FSlnbvn-LAvOrOdtLPhDw_Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از آتش گرفتن یک فروشگاه فیلم گرفته،
دادگاه گفته این اقدام «مشارکت در آتش‌سوزی»ست و حکم محاربه و اعدام داده!
همون حکومتی که با جنایت سینما رکس آبادان و ترور نخست وزیران و بمب‌گذاری‌ها شروع به کار کرد و قدرت گرفت!
بعد بگید چرا مردم در صبح ۹ اسفند
و شخم زدن بیت رهبری خوشحالی می‌کنید!
هزار بار دیگه هم شادی می‌کنیم
از مرگ و نابودی و تحقیر شماها!
هر جا که تحقیر بشید و نابود بشید؛
از غزه و لبنان و یمن و عراق تا تهران!</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6653" target="_blank">📅 18:40 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6652">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gWPFmZ7_LaY5tivL9olIR0eTbE0cLOFYREU8ak_ijD-vt7jyxA7QKioUQTQzPfvx5fi65P8eEYI69_npKwY6IFG_XLidONhEcY1iTI0-DMhMpl47c6YG1t-OQ2G1KVLvFUlN6T4OjVBEok35BA4xZLTaGqa3rrUTtpuNsirAbVrnk0xmiV0-qZlHvEHzhVjT21ik7OMckItjdPMDfxCp9UhhLkbllR6ybEWCLfGu-Wg0qpHHEdEt0Ktu9s6QFxXZW2aWwzoMP6t4cmGUMtIs2tiwi1JZAyAopO9Bjp1D7XcVLxd-eDEKtRhxTvVY11tHa0kzeYXqRE8rRIbZhJL6Dw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HwSvHKHMOvbzaqmfb1ukZHmSpcwN90mC5YrZqzcvRfFW1XBjNan2oKbBNwESgJ0qX69hdX5Qle02JzwFED-heza0Qc97vR7VLYFPJGrVsHlJ4Db8DX9MxmmxJhzsv5eJzJVgZkeN-EBetB3sllEe61dIEmm-OrjyywXoz8wehGjr3BMJjHbq7VjocUmp0feNuYmPVCbe1qnUtWkWJYMx0DNPiyw3xKf1x9AW4UOAefPo-RRWtCIFM0SRSK9nPnUIsQVKos1GeWsC2ge3EiDZaEoTLT7txFcdi7hiOyNcOjrSFUHVuFXxDveyWmHH94d-_C-enYRx_xqnGgPE2w8xkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UTsOmUu8SR9y27nzgtVgjJZFs7pcz5MjPgK0uGf3PlvAkx46oLLwzs67hTXznSn35wsxKvgFn4-0oOuyZLhoZMwxsg7AfDOZqLjz-3YFIWFO1Zu5CWfRHfyAc2QF5qgbA88D9qFxW1oCNIUS45ma5Ioc57lqKcbwUIstqgCPKqFs9NH-iYf7fDe4gmDe2G5lUpVg2dHc5jtVO4Np8U7HnizAShDOlKLIF--NxfozoxOPqFWPV1aglyS9US7GXlXl9F7CaUYpgoPj44AMzsyQZzKz2Vna-2TZXZ-SJ2CelERPwuZfbBTYCYy9tfLSwWDper25YszoN_zCHt6on6Z7sQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/oGjnCHVXbka6BXO3nASfOcuA2Rh9l1-OswyuPfZD9DuWt9kggViEMh6F-dbbyXSULnvA_5qBMGZcUfXy7-f5AbcSSQVkr8il6Jy4sV-jZ28EhcZnlhT777cZ5i8Uts65Q2Q8F7dGJvejUYMADzTwZYsnbShQHyAZDQvxwfsLkTCd2wXlyM2fSayNcbMj9jz6e3fAcn-xg7yqqHoo1POUO0lbwU7Q1HdAjiuk5ffLLJcxyW3EuY6ftxcbXxoRT31Pk5mg__bmZ-HTNPrFT0wfkraBXGKpnnkkw7JUPc9tFlW8OGUDXJhQiPjvJByBpEJSiItqTl6qEA0Fp09xCV37AA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jWFdSllK721o5NOLSOhTcf--wastqXA3284MKIdqPFaLHoEhtDuutzF9leKOL-shHdaW2eVX-O0SidRBKYVS-xMin9NIwGOA5Yel_phU4ElP_3kTEbnWSkU_7QaUCjk-CnpOyZkiab15FgQ3ux_gv7IncD5NGC01f0qAqHBVwZ8Rjok5lCqpvNhBz6FfREJs9hquww-udBC_zCyZE8IczK_ZooVx96zz80zKKoZLyNO8K10WEK3y8q1Z6c_EtXPqgH0-4CIfkeU3laS_OG7MYMVhDQ5VMvE1UdgPjgW39LPl_K8jYW07nb6D3niebuvkPtWE5TOqdVsf5c_ZF9uDuQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی،
دیروز به عنوان رئیس هیئت مدیره
دیجی‌کالا منصوب شده!
نام او با واکسن کرونا گره خورده،
او سخنگوی گروهی بود که مخالف واردات واکسن بودند.
رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و برای ماه‌ها
مانع از واردات واکسن شدند.
تحت هدایت رهبرشون خامنه‌ای.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6648" target="_blank">📅 09:14 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6647">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nYAnoP4fU5Nn8994Vpl5q_qJAlu--ttk_4j2eCzibaApPENFjrgy_W79A2DcpaZr_YAMwvx0lwv9d3A7Xa8MSOpGog39t0_gtNc1Z22GcdCYgTZgdiTTMw3mM4W0Bkq2CbbrsbKG4MhKaZ1LZ7qEjyLltlPoThWw6oX92ksIb2G5ugKZudO7h0w24N7zrKRwjjTjYh2uRk1VPjyuaaTqsdyfQ6J0MN3XCQSssulu0GBp9NUfkUScscrNAErX13pS_duYvI5AY72tTGzUKSpyjqJTcGYaPAseXXL6batCUVCZ33mO90LYf4TdAD0DOjFNgEbB-1sZgb48ZXtTxdMXrQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=nYAnoP4fU5Nn8994Vpl5q_qJAlu--ttk_4j2eCzibaApPENFjrgy_W79A2DcpaZr_YAMwvx0lwv9d3A7Xa8MSOpGog39t0_gtNc1Z22GcdCYgTZgdiTTMw3mM4W0Bkq2CbbrsbKG4MhKaZ1LZ7qEjyLltlPoThWw6oX92ksIb2G5ugKZudO7h0w24N7zrKRwjjTjYh2uRk1VPjyuaaTqsdyfQ6J0MN3XCQSssulu0GBp9NUfkUScscrNAErX13pS_duYvI5AY72tTGzUKSpyjqJTcGYaPAseXXL6batCUVCZ33mO90LYf4TdAD0DOjFNgEbB-1sZgb48ZXtTxdMXrQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/T7lHuaZmFDfCDZwdDHvrolF34zyR1qF7_NCzaxrP6q6u_BCfquJnlrQeKt5XIXbm8pgIc9QG-rGzxbiNCi-MGtiDZv2gk8A-bz74ERw0tvfhXvRS4y7coLnGlT7TG7XLSe8OsWEROYuebPxEnTbEeo5fXlAtOpbW6VCNUrcxE11M_10unZxdV-u_jvLDuqy3j-n5S6T4EvHYc-IyJwebt0HwRrwRMtFeH-rjKK9VJ_Nhrr1NtAqHaYDTImDhRWMEUQL3NiiEIyHmjEb3RQAGnE1zZW-eSwbtZwxumQ1EDMBy8UR2SH2j4fvCX-S5FcF7BUFYa16vgaSd0PjZ4_8o6A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=oaY6IcG_Qm3nWIuvdaoVgli208PkJfYhUYLmKWA-oH_MLhnbUyGOtNUqZ0wJQHdB2UMlSfJBa1INGYImbGQEfwfx6EZjMFsyTwoFMGtGOIQcoeG4a7ZFKYAqvnupjAnBwDX3t9ofIlv_STZOTQ0bVhTEIowk75eFP_Pk0-szemBVt8wYtTuhcXCqe5dleelcbJD4gjgN3Y9U_Zy2eklY26x0rnzP90SyR_yp3gbk_nlhMtawYapP37eBvJWUx51PYTzPso7xIu7InGF2zfKGmb0pY2g7roNSiUBYVZi7X7mbNTymsIJB7_ebq2o2Cy7SGXN9a3LtWeoFCEgzWDUTAg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=oaY6IcG_Qm3nWIuvdaoVgli208PkJfYhUYLmKWA-oH_MLhnbUyGOtNUqZ0wJQHdB2UMlSfJBa1INGYImbGQEfwfx6EZjMFsyTwoFMGtGOIQcoeG4a7ZFKYAqvnupjAnBwDX3t9ofIlv_STZOTQ0bVhTEIowk75eFP_Pk0-szemBVt8wYtTuhcXCqe5dleelcbJD4gjgN3Y9U_Zy2eklY26x0rnzP90SyR_yp3gbk_nlhMtawYapP37eBvJWUx51PYTzPso7xIu7InGF2zfKGmb0pY2g7roNSiUBYVZi7X7mbNTymsIJB7_ebq2o2Cy7SGXN9a3LtWeoFCEgzWDUTAg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=jG9nKVI0QPKyXVd05HqAB-9mFj2tSj3dXDOxeZuJ3eUGi6aH0YBSj3HEjZIVDirR5TyRYXNpI8Hc4_-Y1ABC63ggyvODmrX3mdkfqmWG3xBSBBbqtd4JFYBhGwToWIalojdn8-hEY3WB1MFb5QBLHJhbpnAydRXxrVOreJKUAOcMlyAro8KLEWp34nnRDOX8BarwsjlqFPfTZ_ukpLvaiGNqrdCRkWSKTqaMCQFvlBe5P9x5h7gGFxH1eyH_f_9b2cSQfakg6wCpaDUzm_710DyZXfh1pdu4ebjmaKML5V_TvcHbdV8c3Wg3E2SdxhltxMtypfbZNBrN-eXTIaak3w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=jG9nKVI0QPKyXVd05HqAB-9mFj2tSj3dXDOxeZuJ3eUGi6aH0YBSj3HEjZIVDirR5TyRYXNpI8Hc4_-Y1ABC63ggyvODmrX3mdkfqmWG3xBSBBbqtd4JFYBhGwToWIalojdn8-hEY3WB1MFb5QBLHJhbpnAydRXxrVOreJKUAOcMlyAro8KLEWp34nnRDOX8BarwsjlqFPfTZ_ukpLvaiGNqrdCRkWSKTqaMCQFvlBe5P9x5h7gGFxH1eyH_f_9b2cSQfakg6wCpaDUzm_710DyZXfh1pdu4ebjmaKML5V_TvcHbdV8c3Wg3E2SdxhltxMtypfbZNBrN-eXTIaak3w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e3hx3j0GQh4ICENRmjcuylzhkqfoxGy506gaHQVRVG48vxHON5nfr4z_frn08xpWdBYU1dGTlnt_NFzvmfRQFBsLvWAm5LeLpQd9jC9uzTbRoE1B3pWXdFZVJ7ItV8TMq0z9KIjMeE1HcTyLdikYg7-nf8WcuSkc4Ayhp10CHBBBd1E-9NMFk-qNO2hRBGU9wtxXyoC-ipOsusZLH_7mv1hVBUcw3Sa9DUMtKV9k3DAgkj3I3xjXnqIPaRba3JlQR4WvJ0siKXsfGgsSf_9Sgo-RRRWaDRTXWqa0oBo-aS2YpPJiFmGcBDhAc2DVXOg6KKNTxqc2ZXL09qSIIZHUOA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A_Ht4Sk6NMAYdh0IVCvw76jXQKybSu51Is0RQK_XSfKme_JXPv1d5ZVub4ZHNZ5KUdDv9xxqvrNIBJAeM_znsnVGRNSj-5i8VLdwRaoVt6iDm4IvLIlSkTuRNc4dtjcVu0a_2fnxhtDNDKIZQMRawA1E6eEiN8zvJmbTWZ8IR4bxLRILYOBWI1rPq12tRN-OMApRH8c2oD29Mb4dPD9p-rJErUzBPLAQkEhlJaYRQXywd7GIzpeTKa5vDdTi60cXeSbL4dXxHun9kNjSCOpLwUy9xL98X972nPWdMfnXd4EV9ZrpDOjL_ia9SB8ESYroYhxsDO5E1bkjNXG4sr0rjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای با افتخار می‌گفت ما مشت
و سنگ فلسطینی‌ها رو به موشک تبدیل کردیم!
همون موشک‌ها و ۷ اکتبر،
قدس رو که آزاد نکرد هیچ!
غزه رو که نابود کرد هیچ!
مخفیگاه حسن نصرالا رو که تبدیل به یک چاه
با عمق ۱۰۰ متری کرد هیچ!
بیت رهبری رو که شخم زد هیچ!
رهبر فعلی ج‌ا رو که از ترس جان
به غیبت کبری فرستاد هیچ!
حالا بادبادک هم نمی‌تونن دستشون بگیرن!
اینها همه پیروزی‌‌ان!</div>
<div class="tg-footer">👁️ 32.5K · <a href="https://t.me/farahmand_alipour/6641" target="_blank">📅 14:22 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6640">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🚨
اسکات بسنت، وزیر خزانه‌داری آمریکا :
‏
🔺
امروز «عملیات طرد اقتصادی» علیه جمهوری اسلامی ایران را آغاز می‌کنیم؛ هدف ما قطع تمام شریان‌های مالی و اقتصادی این حکومت و منزوی کردن کامل تهران است.
کشورهایی که به ایران متصل بمانند، باید انتظار انزوای مشترک با این حکومت رو به زوال را داشته باشند.
‏
🔺
خطاب به رهبران جهان می‌گویم؛ امروز زمان انتخاب است، یا آمریکا و یا جمهوری اسلامی.
‏
🔺
هر کشوری که با ایران تجارت کند، خود نیز منزوی خواهد شد. هر کسی که تصمیم بگیرد با ما همکاری کند، سود خواهد برد.
‏
🔺
به عنوان مثال تمام شعب بانک «ملی» باید تعطیل شوند.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6640" target="_blank">📅 21:11 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6639">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=p90m90yRkXPFnpt4KkFklKvgg_wpZOhJ60-FhZa25YjapY_QCxZsGM-csg-7cyuxI0xNOAGR7i-q71aIImOFnSst2Hm12ZN0Zsc0nn8YHv1ORxlEODQha7VWr2C6jdHD-7L8ZyfQnhtOJeAmpq4MZ00PscV_ub5qGw-BuDpCvd6eknZ98TmQyx70GR5ob1Dh2vLAYiG1IlYPskEGw371uVZ_E6CVsDDvv2Z7LW7HpFuGTjcauOGPT1EeC3a6oZlHXeb5YierqU4PwlRMk-1hKmVLjCsgo2gVE6LgAcdnUNWtotnQyGftscTG_Gc773bVHiV7iT505DHJ_h4TUw270ptl3XUKb2sYBnc0qWyNZ7QkpsyYXBfvJ99obYN__EsdqSuGsALAO510f9IEC96hQJmjx9YIZH3m6mrIG_zFFjffFeZcsO7I6jmemYzdZhpX4MiPSiANjyMe2yVLLEOQUMBQYB7Wmnum0675RtYD-eUXQXz1ro9twJvuF_BGOAld8YaQr8UY2PcsNCwto0_u7pvRsKkjcK2aIt-7cD92RdeXkHhVB-AYYXKSfJP9dbMkRxk6fZ7tYFh9zwKr-ZNfnQbZA0kGZGlur4vVF4LeFicj6wS_VL-s8W-EuM9CCxmw0wvmuwQ4C-KPi9spa_E9-8seAx8emXS5XVAdw3a4WiU" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=p90m90yRkXPFnpt4KkFklKvgg_wpZOhJ60-FhZa25YjapY_QCxZsGM-csg-7cyuxI0xNOAGR7i-q71aIImOFnSst2Hm12ZN0Zsc0nn8YHv1ORxlEODQha7VWr2C6jdHD-7L8ZyfQnhtOJeAmpq4MZ00PscV_ub5qGw-BuDpCvd6eknZ98TmQyx70GR5ob1Dh2vLAYiG1IlYPskEGw371uVZ_E6CVsDDvv2Z7LW7HpFuGTjcauOGPT1EeC3a6oZlHXeb5YierqU4PwlRMk-1hKmVLjCsgo2gVE6LgAcdnUNWtotnQyGftscTG_Gc773bVHiV7iT505DHJ_h4TUw270ptl3XUKb2sYBnc0qWyNZ7QkpsyYXBfvJ99obYN__EsdqSuGsALAO510f9IEC96hQJmjx9YIZH3m6mrIG_zFFjffFeZcsO7I6jmemYzdZhpX4MiPSiANjyMe2yVLLEOQUMBQYB7Wmnum0675RtYD-eUXQXz1ro9twJvuF_BGOAld8YaQr8UY2PcsNCwto0_u7pvRsKkjcK2aIt-7cD92RdeXkHhVB-AYYXKSfJP9dbMkRxk6fZ7tYFh9zwKr-ZNfnQbZA0kGZGlur4vVF4LeFicj6wS_VL-s8W-EuM9CCxmw0wvmuwQ4C-KPi9spa_E9-8seAx8emXS5XVAdw3a4WiU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت دست دارند و اگر بخواهم دکان آنها را تعطیل کنم، شیشه‌های دفترم را خرد می‌کنند.»
🔸
در سال‌های گذشته آمارهای متفاوتی از قاچاق روزانه میلیون‌ها لیتر سوخت از ایران در رسانه‌ها منتشر شده است و برخی کارشناسان بیشتر قاچاق سوخت در کشور را سازمان‌یافته می‌دانند و برخی منابع رسمی انگشت اتهام را به سوی بخش‌ها و نهادهای دولتی و «خصولتی» گرفته‌اند.
@RadioFarda</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6638" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6637">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/isyVzRgyUpNYJoOTDF2ItZpV8TZzhjCiT5ZdiBQOck7Xuqsi8wQBG5xKXhatl-41RXRN-d7y4tkbYBGh-OxK5uGs8r_CRhxqJuy4ceNK_Y7OFgJ3Pyln8dKv9zHaf7rPFHwal9L9PdwwbbeyIIS1iJo83gl_f96GpAlZJsD-yPZqV7Xaz1hNSq9wRCtJZc71c0n4kG-820kOjhpAj7S51Ya-vAtssr-8owgi1PLOOwJBrbGkHpZdDFGRLqs9QYbLugLGAuwpt_3u8Ve7Ji1_VAx0tZN_1kCVFerXP6NQS8RBCXVg6hoJjOXVyrOJFjhHwHBpSdqbuLuB6lvYHdIfvA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">💢
جایزه ۱۰ میلیون دلاری برای کشتن پسر ترامپ؛ بارون ترامپ هدف تازه تهدیدهای تلویزیون دولتی ایران شد
رسانه‌های حکومتی ایران در ماه‌های اخیر تهدیدهای خود علیه دونالد ترامپ و اعضای خانواده او را تشدید کرده‌اند. این تهدیدها از انتشار محتوایی درباره بارون ترامپ و ادعای دسترسی به اطلاعات رفت‌وآمد او تا طرح انتقام از رئیس‌جمهوری آمریکا را دربرمی‌گیرد.
تلویزیون دولتی ایران در تازه‌ترین تهدیدهای خود در خصوص گرفتن «قصاص خون علی خامنه‌ای و برخی از اعضای خانواه او» از دونالد ترامپ، ویدئویی پخش کرده است که ظاهرا مسیر رفت‌وآمد و فعالیت‌های بارون ترامپ، پسر ۲۰ ساله دونالد ترامپ، را ردیابی می‌کند.
در این ویديو ادعا شده است که جایزه‌ای ۱۰ میلیون دلاری برای سر کوچک‌ترین فرزند رئیس جمهور آمریکا تعیین شده است.
این ویدئو تحت عنوان «بارون ترامپ را کجا و چطور بکشیم؟» در رسانه‌های وابسته به سپاه و همچنین شبکه ۳ تلویزیون دولتی ایران منتشر شد.
جزئیات بیشتر:
https://l.euronews.com/UtiQ</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/farahmand_alipour/6637" target="_blank">📅 09:56 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6636">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=e0rkYwcOhKPTPKXcBHg2OPlba_bMa0-gKy5aqJHg1_3qhz5m06pGJv7Eb1aaGzXhJ4IZL0fEIsyGV8Fg-YTnoyZZGlU516PlTZ6aPRG5YP4ar2dgNAzTwahH77OrzGGk0waOHehRMENrP5O5xCwTaGy5q6Xp4qY2L6N383XXeZTQC9fl-qqGfSmOGX6SKvWJmLifC-RFJjFpbja_NSzkad3204vT5n8ZSXbcyyXz9BwwYJZE43jNABy8gqPh-PMYd2GXO12EJHN313Kr2Ey2qsiSeRrHurlHIYkV3Pj7RVs6SCJi65DqVEoTho0aSY6a4IxX79uo9JLkWa0sDYDGB42hMKdzzfE7bW8iJ5rA6WpldKRhvIxFM-iWbMmPRcGhe_2G9-WLBPzSyM2NOEhqcfRN_ahsDFla6QBS0hNUrXOUl-KBrPPFplFX82co6vYylk77Dciqf5kmbdPzRfhhfi3XPlKTF0ftJqRZ1Kx63brMxaC35rjezHtDM68XeuvDIeEu_lr4DYXscuYhHLzlU9RzH0rLHbIPhRJEjYmDXJpceYw6AoVMqvmeVdrFgIHLDzbAMQNbHKvSiKtloK62Yqs-sNbyxRiNiQpDROFmhClcj5AtjWWxY7UenfP-dIrFp7gkDTsaNB0_p9ZfZZ-TZaZDWNZPGgo6qBU-t6vPHxs" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=e0rkYwcOhKPTPKXcBHg2OPlba_bMa0-gKy5aqJHg1_3qhz5m06pGJv7Eb1aaGzXhJ4IZL0fEIsyGV8Fg-YTnoyZZGlU516PlTZ6aPRG5YP4ar2dgNAzTwahH77OrzGGk0waOHehRMENrP5O5xCwTaGy5q6Xp4qY2L6N383XXeZTQC9fl-qqGfSmOGX6SKvWJmLifC-RFJjFpbja_NSzkad3204vT5n8ZSXbcyyXz9BwwYJZE43jNABy8gqPh-PMYd2GXO12EJHN313Kr2Ey2qsiSeRrHurlHIYkV3Pj7RVs6SCJi65DqVEoTho0aSY6a4IxX79uo9JLkWa0sDYDGB42hMKdzzfE7bW8iJ5rA6WpldKRhvIxFM-iWbMmPRcGhe_2G9-WLBPzSyM2NOEhqcfRN_ahsDFla6QBS0hNUrXOUl-KBrPPFplFX82co6vYylk77Dciqf5kmbdPzRfhhfi3XPlKTF0ftJqRZ1Kx63brMxaC35rjezHtDM68XeuvDIeEu_lr4DYXscuYhHLzlU9RzH0rLHbIPhRJEjYmDXJpceYw6AoVMqvmeVdrFgIHLDzbAMQNbHKvSiKtloK62Yqs-sNbyxRiNiQpDROFmhClcj5AtjWWxY7UenfP-dIrFp7gkDTsaNB0_p9ZfZZ-TZaZDWNZPGgo6qBU-t6vPHxs" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/g1UNCd3bD-AkHf7GnpVrhaEulfNMKWue_fZ4dgtbHhSiPwLzvgrRlDzBsEOHFXrJ2M14ew7c5vGsAtwMR3zu0wrf_QJ0Ug1YwmGl7pAOrPY9H_VJaZ3JjhX_M24rCeXDeXGr-rqvgCtnWvXTx3Xjx1ljNYU8_e7u4_G8HJWw75nRUAwrr_n8ZKHkWim-YE6qDs3eQbaWiJj6dwvXsSRYfAthgwMHwcI6wNsY9PBrFNT4PkdrEAIzov_wumQc4it_1GCf6YBkg4Hfcf1E8LtJVQ4y5n2xuPtgKSiyZayKdWIRacewmdVErUhZ9TDwSsf1_ppzcIhpeneic1zcUpAkkQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dvRNl7l-N2WUOlpK9U8eiRaZJELxwndha9qfpHgYH21UmK5OL56io6svHDzdtiUhKSzj1PzWuI9YNwcpicP1G-NOJjagZlzrxP1FWy5Fp5CBxZzNlt9CzWR2P3dPa3f0jly0vofQWS513riUhar4H-9G7FNKWH2xdFFBaDXehf6o89sINNmqCEQUpyPS-2FdoxB2orxtDTkrPP16u8s-HxoRbmMtzt_jPiJila0CQNVKOAHbcZtg0b65tpW6qh3xeYGVUoWzaZjnnFvx37mfwTS1lG0a1EZm6prHcfc_zTNYzY0YNw3pRc5ZfU-XHXHi8G_vF-lElj_0d52ZVpA70Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TyXJhhnAVajpyQ2m9Ete8ve8JH01dKQ7Cd68McT8-CKQaZcYMR5ZCutHBkJPNc1hwfLTPEuoLNocGYYSJzlnRUhUavYWEEyAThFP-SPkGei63QGym7-tIckpIkNFhoAyS0JqAVKFNLGwCwJbgFPs-Va66vLkMzL9l7M0l67cOiLwhXzVnGQuclaFeWSmLlpnQp-DqE6grwugwRyIb8leYwCjRXUhk_BV9ZNxN5OvWmTdh4CFshKvtz2gIRPlUYkAyseBGrR8AgaejpWGho2KCGWXytc13R3lbZrz8wxPUhTDRVzokqCGjhwJtEn-k6x-fa2cmeeugBPL24sQgOtzzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fHwlTM-aa00J8ZBxpMvhJw5ZShvSInWzDPXnioraUCKEsMpH9U993o_11ioBsfQzNbfj8ybjbRLX-IzA0WQx9kOci00DBWHwN-dZ_P79GM6gmrcPMMkZElcFkBuY_p4ISY6halZAbYvrMa1Yiq3EOW_x3t-onb4p4Is-_dbdxJvIFr5AX3y0QckacEGa10Qpq87o01cATI4w5mb2tHEkZjCYi9FESbGIxqpsAIbs7pC1ULdmSInVa_CfNKPBE0NDpKMRwPZP4Ko2_3HRl6s3RL48MY9JrB87TWRmiB_b-lwN_42STFhW2d6QMZCf6QlnNyvZ_5HOZlnKEQQTK1p8Kg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YJXoilxZGxZQPjBhtBQujqEmrsI41R5Wk7g_HEaNMus6I7ENVpeUE9V71OcBfGmUF2zWgtEH3snbP6I2aCNIEGrTOS8X1_kRdb4nFOzDcsneZoyTzsAs6vVeOQUpZtt_JDQUaC6Ifg6SqNcIKLyHbXyk3UcI5n6KmHGdy5cuSWXUqnJ6EFAqL3hiF8_olmn5GII43uaagxnDeruQKwCy0_CoNqH0iYtjhDnfDTaeObfSJbPRESUhOsFnsfSZ2UC60nfqp9L36gVmFMG_5qjwcri05J9jTcYDctYoKx7ZCbMKxougwNbOxcEszSdwIHzAjMusT4hDhox1ipRLOzW-Eg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/k_SaiIgn0aw0ZFAJLvf5l0OkT2w5lm9IHyyBtKufCt0FxjyoLrLi1QzKQvOYU3w8wHDaqocHjsGV4YVOQxKPsy2eTIHqv6NetA7dut1pVVF7nL_8u-q1-VmqbiFKDAGFUeC4wnQbxQzPv38BAuQzUvQACrfnU3dz1qQxIIqJj4RWOL3GA6RnQuNMB_wc1R82BvvYWMtViIUo-7n_bzf-bWNIxZo2nICf2WsNchT_MJaLzjvRSb8CxiGO805AXxeU5cxWKhruhUYq1OwQK2tE3_n5YM7WbH1jZ2PZyvUap2uu7-YW5HZ7dy3Jl9EX8yYsJDkKt8DHd7IeFK--poszjg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Nbwk27NGSH9bY2N3dZ2XtKb-oLVh-GGnA8UaHXvKegJTlrGiW4Oi1IW3hTqd9nbVQByek1UlUxULkF2rx5mlc-LC0wdKcON2tyTkWRHWw4mAEfoUupKqZw97byGVVL_79Rh9L2pb6sMoZmfS82SJfBd1YjkXMhtS95-ub1fH1SzdeClCJkW_4q80L7dp-MOgoW2lh62xSJHAb_NT1n0oQ_Nn0DeP4OiusRW3Fn6XgJv0WsGaZcTt3TblKRyJe2LJw_kdyz1ESd-P9qizccboo7hphtdrsUwkD6faAqWKoXLpHlOROxwLX__5nacHgcsUQX4RrBkjDI48mnf8gxVPNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZQG_OJVIQxM6c2_a0yHCZ_FvLv21jXvqPZNQMVUTrSudKVYQHuru8Nx58Q6QtMC9GqA4Z11xIu5Cg3r_JGoy2OnBKJxOiV0Xlbz0INHnAVAIS9HxupI8Zhfcr2xV2zvooF8vpTIn6SrHrJ4OrrTAE6YevGeKe6yBMtZPMRbvmW7eDJfA-mdL-9_a7klCYUrdwHUGa2O-2lneOl8VkSm5cEz1u0RMiCwX2PKw-04vVUwAonG4QdlrNMpJdCZTCNWXz2VL7zj3khU-cA6tqoyZAVbd0Qa_paugdNeQBdi42OsD47nQNHzm0OxgWYU0v6BfDmGO0Sxiv4Z07upIi7nLeA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MKGRklSe29Ypmb-X-34p3gyyWrUAemNeU-o_vhe8iXnKh59NJ7c4QoqwZbG-rV_w7nyYaAmytP6gp-ESDLSP7LbmkIeQaNmW73Y7C8afqchvCnLDkYQLs8p4pMAsxDc0epD17IRKgWhxDTSRjrmz4oFIEtd-mA2MBoJgMhvDY5GiJppKYMyADCSCZvMTXYeOw10yTeO1cU4y4jHrPYx5TXGjDBEPRN4BCGa2ZnknQXVJeNRIt4ARzcI96-l3KkmXgK1E_UZE3JUZkTJFzMFtqKCdCflBA4srB89w4Dl2GERnBNzRP_Cjq-sVeFseXWTK_0IeDcYxxawQIXwic0oBNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/faa1motSusXMnecZ9Ex5GgQeFyGIW0hnlIE9OyXQFi2Sfjj0BLlPplA8BOHd4-FKLdGhOOVKPdWMt1800Jff1PwO6MHS1bPWghfngyZpn-LE_6PLrntiXZlz_WDc0EW-DftSAznf2DSs6De1Je8fLE-sZgrit4cXMsoQ62sttZ7ZsSXzTPIWP1FN8DwQMJgt8Ifl45D5vSBDAv3W0n06PYBPpqr61uUVHuRMq1xbwZaD8p1LYP90PoOJh6lhz036ctQbe_VflPIZioaaw9SgBhVCWvguAltGqhCxdvZysD0VemCJhbG0eGaaD6ipAeEnkviLrQP1IE5X4n4UJzr9Fg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jlmfSTojTmyA_UULpDu6AO0k746INaZCUBRyDuPes3lrKo-SvGrjI1QcJ3qAl38DG8b-gTrY2IiVEZJ5aV9fHSowaSqRlz8-uBvlQTrjcvvhUV4eYndBg3PLrziwbkaJ_79fLdc3rPNfNbEuJL1tzrut3mo66gCIsZrptIYcdPnM5Y0poe05eE_yQkeq9UP-0SvKdSOWWLMGYjD5l62CBxwQBL9IRC8CCZdl_p1310S6BkHy6GqRJCHjy0K8G_VpjOUEzZAub19r8pndnqbzEqEkbf8AJ3d5MwBML5BvMnZ5DdSZxXKr_xXoFRQOsdUTvHLL89DZnWb__FHsX2AMWw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
