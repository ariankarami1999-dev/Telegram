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
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-06-19 15:05:25</div>
<hr>

<div class="tg-post" id="msg-6722">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0dc8790870.mp4?token=ezFYgq1VMDjVhMjTBLatgSuaowqRgDoBB99DpJiNRKkSPioKCf5Jppep4z5Qy6HsrclIiCMZxbXMIXqrZAahgfzHyYMxgGXmYX03PM5I_3-NTemDtIl_HZRGVwV0M-sg4sHzhQpmWT6InrFAvkmISWgSLUP3M2whRwEmjiu9QKs7cqFjkQh8siFbOF69VQzNZu7YMr758RIseHylzzi0uRgJbfAIqm3rlhVFQMQ2F3sktdIVGXuLSqRQOlFxB8KSxPliMjBk8WQyPLG3yr0tVB-H5wYqZ4ck2D3FZqeohZj-YgKdzCrLzp-VxqQ51J047QwjmdvZszzzjVV_bdNUmA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">حالا که  اسد فرار  کرد و سوریه تصرف شد میگن قبر حضرت زینب در مدینه است.
به اینها باشه پسفردا میگن جنوب لبنانه!</div>
<div class="tg-footer">👁️ 8.21K · <a href="https://t.me/farahmand_alipour/6722" target="_blank">📅 13:11 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6721">
<div class="tg-post-header">📌 پیام #99</div>
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
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/farahmand_alipour/6721" target="_blank">📅 09:14 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6720">
<div class="tg-post-header">📌 پیام #98</div>
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
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/farahmand_alipour/6720" target="_blank">📅 08:59 · 19 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6719">
<div class="tg-post-header">📌 پیام #97</div>
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
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6719" target="_blank">📅 14:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6718">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">دلار ۲۳۲ تومن!
💸</div>
<div class="tg-footer">👁️ 19.1K · <a href="https://t.me/farahmand_alipour/6718" target="_blank">📅 13:33 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6717">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/t0oBrXt_6lCiYrIvM3CWsUTWuxfDUW4J0z6G59N9tqNRK_UYGp16m51FZtVb85CngRTdtkQkv96HPbGJp6-VFaTw36QjDU6vmgfPF7bwS9DaqT7wHmUl54PPGEexsoVKdKAEhE8XOzIqtmUvEehuu6a1haCoq6FFa238Qh8CLYAZBNk19aqUHcXgexFt5nHNplyYrGzAaqJ45lF64dU2zJOOiBkjYcSU77aIpMWm8vZYhSRbu0JlrtBzJYOETnfLUcw-n_4meOttVoNvluKnnc8P6smjncsBDM1hCbB3PTuqkHsMiKKpHVN69nqwEpcgPC9gMTsyZ-Qn2eRoXEJ6QA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شکر نعمت کنید،
بلکه این نعمت‌ها افزوده بشه،
اصلا گیریم یمن نیفته دست عربستان!
بگو اصلا بیفته دست کفتارهای
بیابان‌های سومالی !
همینکه این‌ قوم ظالم در ایران شکست بخورن  و به غصه‌هاشون افزوده بشه، جای شکر داره!</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/farahmand_alipour/6717" target="_blank">📅 13:17 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6716">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b5c656aa3a.mp4?token=ZuSArq9OoO3n6G7QD_08Xw4fg2Oz0U5B6X94PKD_dvNW3v3gAYr33TJD5JPhEkfwzCm6-SzbRwnQ3qJ3iE5YjdEdqHX7VLxnO1UGefWKr5Lx-ASFSzVuawwy2Y4LcpjH5BbCpiqQu2_i_hGaCpSQnt-3-5U-8S33vTp6aMB_3BmmrwKHZKDzXGO1t1UXdujV4uypM_KSqcCzB7jCJsP2oF7zGc95H930qrrB3wF_ms6BbTGcdwFATPQhMHM21N5fqrdA1mde89Hi-3z8Bu351gboHfSzcNFje43G0SkmUO2CDK03-A5WPDoj0op2hKPH5STbLrgcagTGnZT7X50IHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">چون رفتم توی آرشیو این رو هم دیدم همون ۱۶-۱۷ فروردین، کارشناس  صدا و سیما میگه جنگ رو باید به قیمت ویرانی زیرساخت‌ها ادامه بدیم و تنگه  رو رها نکنیم تا قیمت نفت بره بالا!  و فشار رو بر آمریکا اعمال کنیم!  چون خواست مجتبی خامنه‌ای اینه!  نتایجش رو هم همین روزها…</div>
<div class="tg-footer">👁️ 18.9K · <a href="https://t.me/farahmand_alipour/6716" target="_blank">📅 11:44 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6715">
<div class="tg-post-header">📌 پیام #93</div>
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
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/farahmand_alipour/6715" target="_blank">📅 11:41 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6714">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dea6786566.mp4?token=pTcoW9i2QHip8fIBXF0dqclcHgCGHO_9pwrL_60RTxkjKz5ecVrysXvtzaCQbNb7bTgbY506rYgay_ZV2siDa7aaunMlZWPoWzYOa66b76XUAA_f-NE35rQHBvyx6Jv7MQsownB0kw8h3xoviclT3PkDECu8w_A9Y09NuHF7eoIRflUwIwy6NZf6dWaZSFj5KcNsreMWqNi4MFeHe2q4k8bt1AuP8wpm0IMw6bOm79k6kXSBJcNCYZj2_WMs8HV48Puq5dMzg5DqY-TMzdqgk9lFHFJHkVRK56zUtrk4eGYGI1FTFHg-3iM7cU8sEOUvnpCDEVVRlFvbA0LT8q_-3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خودشون هم که با افتخار این  تصاویر رو منتشر میکردن!  بگذریم کل سپاه و ارتش و بسیج و مردم و عشایرشون نتونستن وسط خاک ایران،  این خلبان رو پیدا کنن!  فقط هی نوشابه پشت نوشابه باز میکردن و تعریف و تمجید از خودشون! زارت!</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/farahmand_alipour/6714" target="_blank">📅 11:10 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6713">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">هالیوود از این داستان فیلم خواهد ساخت خلبانی که وسط جنگ ۴۰ ساعت در عمق خاک ایران بود.</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6713" target="_blank">📅 11:06 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6712">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">آزیتا در کالیفرنیا داشت محله نیاوران و فرمانیه  رو به دوست آمریکاییش نشون میداد،  که ایران چقدر پیشرفته است،  یهو به خاطر اینکه خلبان در یک منطقه نه چندان نامناسب اجکت کرد، سی‌ان‌‌ان و فاکس‌نیوز پر شد از این تصاویر از ایران!  تازه هالیوود فیلم سینمایی «نجات…</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/farahmand_alipour/6712" target="_blank">📅 11:05 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6711">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/75c148c255.mp4?token=O3qzpMSIHoJMHIbsQdZC3CyJOMG_QfrDSh3kx7XzP4nDnl5fzGlQWz-ILLhw6wtYLwX20nB7xGPstNOYhWa_LGWo2rMt_0l6Dokpunws_M1UXzkELvwcaySJzSLzgltJyH-d22VFBZPKfpjt5SKF1C70FX7zZADKEizL_5c4bXR-tF9f0q9bISY9VG-lmVcYoQRkVehiZsIXkEBG_OnnXN04o77nKFkxjEfVGQmTwpAUT5yhtfJVx5udSj8myuT6kLs0X4SJfEJTa1VSxoxc1LGbk1mLwsZyMwoCDnlaVR80vOhnVKf2pWFvy3j45PjTlRGi-iKkpiUWU6uQbWnJVw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">:)</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/farahmand_alipour/6711" target="_blank">📅 09:28 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6709">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/grT1IV8p2uZrOz1ma8v9ymcZ8N_fcVPClbus-hnp6_KVfyNPG20yVE5d9eO_JvK7Zl-lV2uz8RBDiRLV8q8vyDT9epBVr8gaberG1Im3FgK2f3QgHYhlo3o-WSTmj8dN0rFt4TXrB8JRiRMOYE2fnhODQCuAfh2PO9ru33VqNJe9qnSaHNVfmkYm6VgTDVnYOwBj5X78A-19xlJrZEoQkk3CLWpCcrj1U3SvOhrb6k3wMwhRd6s2OaZDQOV5E89dM4YwGU2S1p6zMVTNt5xP6o3Z9NiheDLaGg6VkYupWHBbow0JsbF1ZTwFbyVTX34KVyI0JxCURQWwnuQZxhojyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
شب گذشته و در جریان حملات آمریکا ۵ نفتکش ایرانی منهدم شدند.
سنتکام اعلام کرده که حمله به این نفتکش‌ها در پاسخ به حملات موشکی جمهوری اسلامی به  یک ناو نیروی دریایی آمریکا صورت گرفت، گرچه ناو آمریکایی آسیبی ندیده بود و موشک‌های شلیک شده ج‌ا دفع شده بودند.
سنتکام ویدئوی انهدام این نفتکش‌ها به نام‌های « ام‌تی کاویز، ام‌تی چارمینار، ام‌تی هورایزن ۱ ، ام‌تی ریسکو و ام‌تی دریا» را منتشر کرد.</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/farahmand_alipour/6709" target="_blank">📅 08:38 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6708">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">🚨
ج‌ا با ۱۳ موشک به اردن حمله کرد</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/farahmand_alipour/6708" target="_blank">📅 01:13 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6707">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">🚨
طبق گزارشات، سپاه از اصفهان، یزد، تبریر، لرستان و... بیش از ۳۰ موشک شلیک کرد و حملات سنگینی رو آغاز کرده!</div>
<div class="tg-footer">👁️ 24.4K · <a href="https://t.me/farahmand_alipour/6707" target="_blank">📅 01:09 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6706">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">🚨
حملات موشکی جمهوری اسلامی از مناطق مرکزی ایران</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6706" target="_blank">📅 00:54 · 18 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6705">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها، ارتش آمریکا امشب دو نفتکش ایرانی را  در نزدیکی جزیره خارک غرق کرد و به یک نفتکش دیگر در نزدیکی جاسک حمله کرد.</div>
<div class="tg-footer">👁️ 25.7K · <a href="https://t.me/farahmand_alipour/6705" target="_blank">📅 23:02 · 17 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6704">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZsV-x8dtFdl0tZUL99bZo_WSS3dCbcxxuNCIsLJgewXQihuwzsYUh2klvLiHLG6r9Aqkmmb7mIL4p2PNWRHO23OxcPj8oZAa5Wk1PuSpPlI-04ZYmaUzI6FwzTVXWHAuSa42DtoI5LfXNUUSFypFsFwMeqxQYW-QnFH5sl_A4thFF9QWnoszsculWAj_I0FiYblKaoSh2DW7oEsGmw-SRySVjaiKWz8x5sCPQxya4UWA4BdRvnAbJ5wdW6msiZN9tO2-TYkcKkqlWFCQULYAPuj-kx5ddqCatuRm17pE-tspvtaRWMtooTBvhcX3C5FCncsrtkPc3qukPJ3sAgPC1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1701dd8ef5.mp4?token=ZsV-x8dtFdl0tZUL99bZo_WSS3dCbcxxuNCIsLJgewXQihuwzsYUh2klvLiHLG6r9Aqkmmb7mIL4p2PNWRHO23OxcPj8oZAa5Wk1PuSpPlI-04ZYmaUzI6FwzTVXWHAuSa42DtoI5LfXNUUSFypFsFwMeqxQYW-QnFH5sl_A4thFF9QWnoszsculWAj_I0FiYblKaoSh2DW7oEsGmw-SRySVjaiKWz8x5sCPQxya4UWA4BdRvnAbJ5wdW6msiZN9tO2-TYkcKkqlWFCQULYAPuj-kx5ddqCatuRm17pE-tspvtaRWMtooTBvhcX3C5FCncsrtkPc3qukPJ3sAgPC1Yi-rc8JTn60jg3WQw8tSra5FJxajnlRbgTcvWPed9A7hoA88mFEYCu96vjiXAEZIAWkQueE-1qfgrnZIiKZoOLSGAUdxqESUh_wv6CWr27chfsCsgVoKSxYSAmHOwd9qM7iqlPdgl1WkxUyV4FV1b61Q8iTvryYmw13wykAZmAL84M8Ol7JirvcyAAKeOKp5D_ZEhqwoY_cuXrmIQkPFgzhCGz6UMwuTUnj_s4PDZe4dZ6NOvNp-dJRftmQqnzb8PDbBsTnn49KDphInnbCV3xZTrl6vLoFMz2QYxq3AZWfks8FtguR1kxPhFOt7Z_JSDXnBAlnUdZaDVx7DBCB7MQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">زاکانی موز خوران میگه
که از خامنه‌ای «وصیت نامه» نمونده
و دنبالش نباشید!
(خیلی‌ها حدس میزنن که در وصیتامه‌اش اومده
که از پسرانش کسی جانشینش نشه، برای
همین منتشر نمیکنن)
صدای کار و چنگال و بشقاب و
صحبت از وصیت نامه رهبرشون :)</div>
<div class="tg-footer">👁️ 28.1K · <a href="https://t.me/farahmand_alipour/6704" target="_blank">📅 18:41 · 16 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6703">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">بنزین ۱۰ هزار تومان!</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/farahmand_alipour/6703" target="_blank">📅 22:10 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6702">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Jy5U_zM3e6dsvbEm3pRtepajwfZhHQkQFgDSD8PXLRaRfVBcrDSLlmylBLBq0VlTF39hSRij_mSm8Fr_8lEhm8pvIdCpvJVoziyysA1lVEzTybptzHVdZzBWblZeiU-R1cknbX_ipDDj5Ty-wBc3pgIZgtjasYXohoRschp9CPJZu9S6amatZU4dV8RtiG4XX0WV7p1XuNJxQXX-i-S-Q8l_Ahrbv0tJQk7e7HrJiU1-ncyyucCX-jboNrUBk_hqqBN1CmJN2fX1xVAI_5wdRWkwhHFnPiH6drUjC6BDUTvh5DXpWoJCRUfEiF0Fo6TtR-bRij5YKqCnyubgWWYPSQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d87f7a2533.mp4?token=Jy5U_zM3e6dsvbEm3pRtepajwfZhHQkQFgDSD8PXLRaRfVBcrDSLlmylBLBq0VlTF39hSRij_mSm8Fr_8lEhm8pvIdCpvJVoziyysA1lVEzTybptzHVdZzBWblZeiU-R1cknbX_ipDDj5Ty-wBc3pgIZgtjasYXohoRschp9CPJZu9S6amatZU4dV8RtiG4XX0WV7p1XuNJxQXX-i-S-Q8l_Ahrbv0tJQk7e7HrJiU1-ncyyucCX-jboNrUBk_hqqBN1CmJN2fX1xVAI_5wdRWkwhHFnPiH6drUjC6BDUTvh5DXpWoJCRUfEiF0Fo6TtR-bRij5YKqCnyubgWWYPSQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
صحبت های سردار محمودی :
ترامپ باید موشک رستاخیر و موشک آتش افروز ایرانو بیینه،ی موشکی داریم سوخت جامد وقتی وارد جو هر شهری میشه خودش جنگ الکترونیک راه میندازه، کلا تمام وسایل الکترونیکی و برق ی شهرو قطع میکنه، وقتی به هدف میرسه قبل از اصابت تمام اکسیژن هدفو میخوره و وقتی سر جنگی این موشک به زمین خورد، ۸۰ کیلومتر مربع رو کلا نابود میکنه، اینارو هنوز رو نکردیم.
﻿
+++ قدرتمند ترین بمب اتم جهان یعنی بمب هیدروژنی تزار متعلق به شوری ۱۵ کیلومترو کاملا نابود کرد.</div>
<div class="tg-footer">👁️ 30.7K · <a href="https://t.me/farahmand_alipour/6702" target="_blank">📅 16:39 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6701">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">🚨
🚨
🚨
فرماندهی مرکزی ایالات متحده (سنتکام) اعلام کرده است که موشک‌های بالستیک ایران، ناو هواپیمابر «یواس‌اس جورج واشنگتن» و یک ناو جنگی دیگر آمریکا را هدف قرار داده‌اند و این دو شناور برای گریز از حمله ناچار به انجام مانور شده‌اند. در این حمله هیچ‌یک از نیروهای آمریکایی آسیب ندیده‌اند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6701" target="_blank">📅 00:16 · 15 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6699">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/KSX6sHMmsNQ2jSbgobDTGaPNeDXf23W63o6VEuVmlWOghL5HuN4rp57O1aDgWTbb06Kb_aM0whgHEjbKpQBg5TK4pVFYrW4qLLUmSgU8shWlp2cIG379sB_uYarFciL1bk7pwmFzvmg9sX-t9RIZuQxbcnknW0-AWVLrnvK1vh4k0XrBvy-vsIQmGqk9pe9tjSo71j6WjWBzGpwP8C28RojsT9El68k6oRN_ZxPtwtlBmddSwQzERb1VV9NzVYhDkHxQlGQgPIICD16xSYt7n99UWnz8DMpVl4DP3Tpout4FFdAKTpI7g6E1S58uVDqapyJ9OIE9oScKqh7u0hLkfg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/J6PSYkKFL4p8SWHfHrsrp2N65kyMDHHRU-xSQgF57mBe15elnUGC0a5_SthnGAE3D8D0AOG8EXASzNe8U0Pwu0RV0mNkCJFHX3Q26k3-JGBr3dh7tR-qc78RyZnbV2IQkGIjVA3AnAk0FR2ex8FcIr-nxYbRswqgZPvAOO8BcB59e3umgxKSKuiLUk65A5O7SN5BbsSGJeL0inbvx9T1PA5I6Jqo7K-Lym-mCQcmKXvlHfnkz65qWG8LsXELvYw44W8klqOvuLDJMdvvrR_9nkBhtpXarfkkg1a3cePAiZV5HeQ4oSg5FhHLR5Dh0Zg1d0dj87PzeXPUymFc7FtgPA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">برده‌ها در مزارع پنبه اربابان سفید پوست
در ایالت‌های جنوبی آمریکا،
سالانه در بدترین حالت ۴۳ کیلوگرم گوشت میخوردند. در حالت معمولی حدود ۷۰ کیلو گوشت در سال.
ولی در برخی ایالت‌ها وضعشون بهتر بود و برده‌ها تا ۹۰ کیلو گوشت در سال مصرف می‌کردند.
وضعیت برده‌ها در آمریکا، بهتر از وضعیت زندگی در کشور امام زمانه.</div>
<div class="tg-footer">👁️ 35.9K · <a href="https://t.me/farahmand_alipour/6699" target="_blank">📅 21:48 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6698">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIran International ایران اینترنشنال</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ku13awIRNLpkHF_1vmBiOnafFYy-Br9FiJ7wuV9sS6mZDCOR-StUVe7GbFnFRjFvWunRASTqLmQuU2ZTKRvcHFkEKwsDpq4qttGWJLPwEnVfDiZV9XO69zkVEV93dCn3T4x5YkY-YRdgPrkbnIYqjnj8I15r6ck2PmECjdaLlXtcX6oCMV75iG31vEbEQIUMcBauxZJtdfZM6GdjtDlgM3okgf96Mr4f3QEwVmUFN8mO6Lauxh7UkNoAjg53gUSwC4cJKk9SPNVHPEzj_s7_m0E1xMNt-DisteS-b3uzmwJkHaT8ThTZxtBNiEy73YUzdyDyROpOOpBOL1tnGccoXQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffc46cde83.mp4?token=ku13awIRNLpkHF_1vmBiOnafFYy-Br9FiJ7wuV9sS6mZDCOR-StUVe7GbFnFRjFvWunRASTqLmQuU2ZTKRvcHFkEKwsDpq4qttGWJLPwEnVfDiZV9XO69zkVEV93dCn3T4x5YkY-YRdgPrkbnIYqjnj8I15r6ck2PmECjdaLlXtcX6oCMV75iG31vEbEQIUMcBauxZJtdfZM6GdjtDlgM3okgf96Mr4f3QEwVmUFN8mO6Lauxh7UkNoAjg53gUSwC4cJKk9SPNVHPEzj_s7_m0E1xMNt-DisteS-b3uzmwJkHaT8ThTZxtBNiEy73YUzdyDyROpOOpBOL1tnGccoXQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدیویی که ستاد فرماندهی مرکزی ایالات متحده (سنتکام) منتشر کرده، حملات به سه نفتکش حامل نفت خام جمهوری اسلامی را پس از شلیک موشک‌های بالستیک از سوی سپاه پاسداران به سمت دو ناو جنگی نیروی دریایی آمریکا نشان می‌دهد. سنتکام اعلام کرد دو نفتکش از کار افتاده‌اند و یک نفتکش دیگر در خلیج عمان منهدم شده است.
@iranintltv</div>
<div class="tg-footer">👁️ 28.2K · <a href="https://t.me/farahmand_alipour/6698" target="_blank">📅 21:23 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6697">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lZQH1KY3a2prCdvo_6cIIvqh9UwLCNZvDDE2DF0PIpuKjyo2ppuvDUX764i0DtzS2GrXUhMRhHCrpAfpHVjYnhgb05Rf4ItT0ZJnqzs3V-6BHeuJcIjkL6cDhjjzReXnvNLZZNJGw17X8HAiMlQvJjqPOHAyOkKHFmztvKlfqFdTysEIMcbQFiWJPZIpqwYN8hiMEtindzhKqq5vhu2m6G6oncH8UQICldD_f_DG4Fzxp6H8AQRrv3HoX9s9ltyimM8CaQOEjipSnEhY_fNvckaca2Pi4TjMoEOnKvKCzso8EEqU9vFbTbY1QmXoPCu3wZSp3prrIxWxjeOXnuoRTg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6697" target="_blank">📅 15:12 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6696">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،  کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 31.7K · <a href="https://t.me/farahmand_alipour/6696" target="_blank">📅 15:08 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6695">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dQVXfzL3ENxSY6cNy6MqF39oZ7wFPjNQOp2E_0rom4B6o8eCnYeUtL6dnOX8C9EhS4r-YPwdnYchFkJsvre1L5xH9PiqdFU7hlmxk4kiOdnOB0f2XCbu7hqmGx5zxL9dHHePHSQFfcfPbWEuCjhwoT1HE22G_JwRMofqLwzlOna0Hhh-Qaun5ShOkZSm3M9eUm3XqOJNcs4F00RqO63ljnQkk4kjM2U9zHQgDVUJPxx3kUcIvmrC7YAR7erynbrqgrEs_xIkWRlXFRmjbeSPkoINk7ZSbSFmlYBZtZszEAkq1PZynGg3-ck51DB4UpKZos6QX8fz5vgrzbi70KajoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">می‌گفتن : دریا هم بسته بشه،
کلی مرز زمینی داریم!</div>
<div class="tg-footer">👁️ 27.1K · <a href="https://t.me/farahmand_alipour/6695" target="_blank">📅 15:06 · 14 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6694">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Rh72qnYT7_sjApHG0Mu7IiRkEFS8bAz2IXwZ_eBGMx77caeD_mk-8sytCQEprCsFJyqLxjQdI0P7f7nBMtshy-2StYI4Brplsh6cP4HAqqedkKY3yRche_PiiHZoB9rkkFVRrUa88X1rPa6Eaeq0J537T9PjZ8VwLYm3hmhZGXQrfyVImdQBuit2nSAfWOHmqzlFIV5HEqNvW303mg0c2MEI6pxPzwmFPUIUFg2qISGzEUnrSql6oW0vwdwb8lAheYib0QYPbk5mXn_06_adFnSJ3EUhmZln2z-R3Jcixk4lM4ZKm7bThMmWd7wK6GZNvTeA5TuN98RNMD5_dQB10w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بارها به تکرار نوشتم،
تنگه هرمز، تنگه احد اینها میشه،
به وسوسه غنیمت گرفتن و پول‌ درآورن از تنگه و اعمال فشار بر بازار نفت،
دست به کاری زدن که جز زیان و خسران برای خودشان هیچ نداشت.</div>
<div class="tg-footer">👁️ 29.4K · <a href="https://t.me/farahmand_alipour/6694" target="_blank">📅 23:59 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6693">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">‏یک مقام سپاه پاسداران به نیویورک‌تایمز گفته از ماه ژوئن تاکنون، بین ۷۰ تا ۱۰۰ عضو حزب‌الله، از جمله مشاوران ایرانی نیروی قدس سپاه پاسداران، در تونل‌های اطراف ارتفاعات علی‌الطاهر گیر افتاده اند و مقاومت میکنند.
‏این مقام گفت حزب‌الله بارها تلاش کرده است با استفاده از پهپاد، غذا و آب برای نیروهای گرفتار ارسال کند، اما نیروهای اسرائیلی، رزمندگانی را که برای جمع‌آوری این تجهیزات از تونل‌ها خارج می‌شدند، مجروح و تا سر حد مرگ زخمی کرده اند.
‏او اضافه کرد ایران و حزب‌الله، تخلیه تسلیحات و نجات این افراد را در اولویت قرار داده بودند، اما اکنون به نظر می‌رسد احتمال موفقیت در این کار روزبه‌روز کمتر می‌شود.</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6693" target="_blank">📅 23:52 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6692">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4tEPOePaZRMfYJKp_hz3xHPSXey2GVi0PxwyD3fr3jJPzYPJTZsT-pN0UA2LS1ivVgkdhsaBSXcJXF8r3WLTseFrRBFtTjM0whHQhnAIdh9wQBIOV7_ikzmnsxG9AWEzkF4pVKZrbfg0pyGdnDvsodKUEvYLVrRz-f6jftP7ErsfDjcGKKJXk5hK_DRrcbpJN_yAGGb7iPDn8F3ssnujx673KQ5PLgyp16H8aYWZ3XzH3-InmxSfKuqWWq1uAQKKkaI360ltCS1okGm1lIpLFZUEM8b_-xrdwadirIz2BzlU3o8EZ1MFUgClnZXS3uwlBLbeLKTaMp0ruzQ1uzGzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f75a2dec2b.mp4?token=g4tEPOePaZRMfYJKp_hz3xHPSXey2GVi0PxwyD3fr3jJPzYPJTZsT-pN0UA2LS1ivVgkdhsaBSXcJXF8r3WLTseFrRBFtTjM0whHQhnAIdh9wQBIOV7_ikzmnsxG9AWEzkF4pVKZrbfg0pyGdnDvsodKUEvYLVrRz-f6jftP7ErsfDjcGKKJXk5hK_DRrcbpJN_yAGGb7iPDn8F3ssnujx673KQ5PLgyp16H8aYWZ3XzH3-InmxSfKuqWWq1uAQKKkaI360ltCS1okGm1lIpLFZUEM8b_-xrdwadirIz2BzlU3o8EZ1MFUgClnZXS3uwlBLbeLKTaMp0ruzQ1uzGzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اون ناو آبراهام لینکلن بود که ۶ ماه پیش
با ۴ تا موشک بالستیک غرق کردن؟
خبر موثقش رو هم  صدا و سیما پخش کرده بود،
خلاصه دیروز رفت پاتایا  !
و یثبت اقدامکم فی تایلند!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6692" target="_blank">📅 23:02 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6691">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VTSgiX_nK9mzSOl9p-qPdTUqiWnvgS8x0JxmgIO4AO66WRAx251xH55rFXFSgbE1KjwKqZ76F2XPUbcUAjJO8m0UrkyHkrJlOoYW0G7L_IP0_lCtOtZOnV_8NdsnI-G1n9J96v99ZxYcscQMjzNR3JMqlZsKrZDt6tdoBg_zzzfhrGULNbWNCvAt0Wvt9-nFJ1vzPp6d_6IJHDWi4gJA7E2ok26E1XF9KGuudqCgQt6Ve1gj3rVs3PEZe-T14_qClwEfM52eMRSu3stHB-LmNNpvppBnMMKo5kR3-HJXmECwAF95vUVmf25ZVNClfRUfIpKYO6h2hMcG1y1BhazCKg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d5f5cc74c1.mp4?token=VTSgiX_nK9mzSOl9p-qPdTUqiWnvgS8x0JxmgIO4AO66WRAx251xH55rFXFSgbE1KjwKqZ76F2XPUbcUAjJO8m0UrkyHkrJlOoYW0G7L_IP0_lCtOtZOnV_8NdsnI-G1n9J96v99ZxYcscQMjzNR3JMqlZsKrZDt6tdoBg_zzzfhrGULNbWNCvAt0Wvt9-nFJ1vzPp6d_6IJHDWi4gJA7E2ok26E1XF9KGuudqCgQt6Ve1gj3rVs3PEZe-T14_qClwEfM52eMRSu3stHB-LmNNpvppBnMMKo5kR3-HJXmECwAF95vUVmf25ZVNClfRUfIpKYO6h2hMcG1y1BhazCKg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یادتونه قالیباف برای لبنان
از اینها
⏳
میگذاشت؟</div>
<div class="tg-footer">👁️ 27.5K · <a href="https://t.me/farahmand_alipour/6691" target="_blank">📅 21:51 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6690">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp60Vok1p8lcWn-2EUvoY4QAzCtwCFWTnsf6C-4hTRRC-7mIK-PHhWq4YHBs2OOnX81RBjcQAqgknOETsKJC5A1BcKn1KS2bdNHh9GSNnVTtMwtuB2fLbTkndDYKGfKIS7bQZNyUSaR52dCbAm-3Agq3IHHgQ4faAAUnzcrq6E8_noAkG6t3M9-H-cTA7nacQUIlQQy3UwHNFP-N-3YgshjwOgqV-ADp7hM7ijYnwfLtIDusd8vm_CtxXUw48DP1eydjyeEA7_qJjFVPT16kLKHOvfH5ODBwla-E1deLaZff0X6zp62dC-4ZYtLF_r_1BEoIZ-W6LdPIzquPZsvrY4hPLlhSp5ol1ZHiNSZzzUwFYDM0A84mhmorXTyqhZy6QqGqYHenBktDcFR2Hre1cjf5M9w3zKRdMUcdNkQS-EndSJ9AzlelZpQ9F9BqcS36fV9i_tsRlQWe_qfMyaCP67hLTXk-tuR3zBri3S0UfedTBqOUTjkwPZSDujBz8vsOGVExyU7PsIJwqD1FLvw43GsWrEhrz5OwAtoQDvUJVLd2jPH7JwTf3HLBjRaildUgFB-MSr2YUgvY7TEpb6kG5JLBSzORK_-JJwo9G2GCmOa1c5FuH-x8hpq_wO5frLCSVn3oJnRUugvoPbIKvBAvS0eSur3VWEiL4qSGLF7ZpL8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/0a42d9ffe6.mp4?token=Tp60Vok1p8lcWn-2EUvoY4QAzCtwCFWTnsf6C-4hTRRC-7mIK-PHhWq4YHBs2OOnX81RBjcQAqgknOETsKJC5A1BcKn1KS2bdNHh9GSNnVTtMwtuB2fLbTkndDYKGfKIS7bQZNyUSaR52dCbAm-3Agq3IHHgQ4faAAUnzcrq6E8_noAkG6t3M9-H-cTA7nacQUIlQQy3UwHNFP-N-3YgshjwOgqV-ADp7hM7ijYnwfLtIDusd8vm_CtxXUw48DP1eydjyeEA7_qJjFVPT16kLKHOvfH5ODBwla-E1deLaZff0X6zp62dC-4ZYtLF_r_1BEoIZ-W6LdPIzquPZsvrY4hPLlhSp5ol1ZHiNSZzzUwFYDM0A84mhmorXTyqhZy6QqGqYHenBktDcFR2Hre1cjf5M9w3zKRdMUcdNkQS-EndSJ9AzlelZpQ9F9BqcS36fV9i_tsRlQWe_qfMyaCP67hLTXk-tuR3zBri3S0UfedTBqOUTjkwPZSDujBz8vsOGVExyU7PsIJwqD1FLvw43GsWrEhrz5OwAtoQDvUJVLd2jPH7JwTf3HLBjRaildUgFB-MSr2YUgvY7TEpb6kG5JLBSzORK_-JJwo9G2GCmOa1c5FuH-x8hpq_wO5frLCSVn3oJnRUugvoPbIKvBAvS0eSur3VWEiL4qSGLF7ZpL8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهم‌ترین مرکز فرماندهی در جنوب لبنان
و مهترین سایت موشکی در جنوب لبنان
که از دست دادنش یک فاجعه است.»</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6690" target="_blank">📅 21:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6689">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LOqC5cG8cm_e11bffExiJaK6Q6ri27MobiKNNWE_WzRSeGKBg-v8tQWA9tCEKx1nD8LN2VvXRu2O0b3c-fcjwnT6ClT5IWD8HNnnCeQVNjIL5q4a1ZLZWbpmxbrwCeWU-3QJeSC8M9DwLaQ5T1O8sPhinspMfiMpzuBuMa-ezSr3IkRTAHPEBJa93_QX11gSh5tPV6e0MLvmoYEjzz0Lc8ylOdBZomvgDQE1DplPbHfxQJ8Efi5TqJuKm6Eh3ucg224rglB7EenBDNYMemgGZuQFvTnSXGDaeND59nBbeTA-u0irvf1yiu9QfB1d5L9gEZXWeF_HlBfEoHAx28Md-zFFFjeott7glwBij5rMwtOUTD3Gv7Mwr1nwrLmNzsOBjfPuE0IXdj3-wYqJDKUEpKcj4cg4LPL_9RngsCJWvzDGTkX-GKIZzSqycjB_0PER1hJFpVH-xy7AULwQQBE70HHJmrBR0stlGSiUab57jDOVVzpJFEr420o-FkQMuvXlz71HZGNbL-306WKKOPK47qNVjkifzaTjRM40YQ1iaLMG9-hEaEmMHsXr67u3VW2u4xz644UN3IB8_L0rr459k0Kn3zN_sIQ28BhA-LT1u4WOxrg4kRFch7Uv1r579ZgPgkjxK-TgNgEwFNKpEil1lE04VyrPtUxGi3FqaoZNvD8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec9ad5c57b.mp4?token=LOqC5cG8cm_e11bffExiJaK6Q6ri27MobiKNNWE_WzRSeGKBg-v8tQWA9tCEKx1nD8LN2VvXRu2O0b3c-fcjwnT6ClT5IWD8HNnnCeQVNjIL5q4a1ZLZWbpmxbrwCeWU-3QJeSC8M9DwLaQ5T1O8sPhinspMfiMpzuBuMa-ezSr3IkRTAHPEBJa93_QX11gSh5tPV6e0MLvmoYEjzz0Lc8ylOdBZomvgDQE1DplPbHfxQJ8Efi5TqJuKm6Eh3ucg224rglB7EenBDNYMemgGZuQFvTnSXGDaeND59nBbeTA-u0irvf1yiu9QfB1d5L9gEZXWeF_HlBfEoHAx28Md-zFFFjeott7glwBij5rMwtOUTD3Gv7Mwr1nwrLmNzsOBjfPuE0IXdj3-wYqJDKUEpKcj4cg4LPL_9RngsCJWvzDGTkX-GKIZzSqycjB_0PER1hJFpVH-xy7AULwQQBE70HHJmrBR0stlGSiUab57jDOVVzpJFEr420o-FkQMuvXlz71HZGNbL-306WKKOPK47qNVjkifzaTjRM40YQ1iaLMG9-hEaEmMHsXr67u3VW2u4xz644UN3IB8_L0rr459k0Kn3zN_sIQ28BhA-LT1u4WOxrg4kRFch7Uv1r579ZgPgkjxK-TgNgEwFNKpEil1lE04VyrPtUxGi3FqaoZNvD8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز  منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6689" target="_blank">📅 20:42 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6688">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HvDFj5tTb8AafdqXs-UmuMPxTslmarXTr_7W-aUvlK7XIUW1xQAmOmfy7xj53nelhG7_nIyK7R9Ze57VOWRjDXN1OTLdeg4qxvaajybRDUE9geLxrpg2VwSN2GaUttyqZBWykJhuv3TwLCbuiPlEtR_P7XHpaXW2kicMp0jKuLgy5yxYjoyP1Pk-sNCkAcAIc11ivlPasz2MC57_smuBxaB8clxgmhz82DlZq3aTkVuGR_ufqXk2zj9R6We-hHFP0j4n20vejaTGq3eMBKa8kXdlQVJy9aKy6-3TNMs8lPOcnUdHkMpPLgPmOhplnDnUy2k-KZHSms_7fY3bxzyhOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9b658d3f18.mp4?token=HvDFj5tTb8AafdqXs-UmuMPxTslmarXTr_7W-aUvlK7XIUW1xQAmOmfy7xj53nelhG7_nIyK7R9Ze57VOWRjDXN1OTLdeg4qxvaajybRDUE9geLxrpg2VwSN2GaUttyqZBWykJhuv3TwLCbuiPlEtR_P7XHpaXW2kicMp0jKuLgy5yxYjoyP1Pk-sNCkAcAIc11ivlPasz2MC57_smuBxaB8clxgmhz82DlZq3aTkVuGR_ufqXk2zj9R6We-hHFP0j4n20vejaTGq3eMBKa8kXdlQVJy9aKy6-3TNMs8lPOcnUdHkMpPLgPmOhplnDnUy2k-KZHSms_7fY3bxzyhOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ویدئوی امروز
منطقه استراتژیک «علی الطاهر» هم سقوط کرد و به دست اسرائیل افتاد.</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/farahmand_alipour/6688" target="_blank">📅 20:33 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6687">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ENBOB-sE9aKbvMnS8--DgNHV3CqeOLlpcGBNL-SCThmrbZrJejCsIHVl0BWKPPef6e_m2KhZxqGENg3K4MUgE5uI6ukcUg2fUaERszwe1pv3lvoPm7ntuORvkRgM7Nx-g2Pl4wN2oJwx4crueOi1381gqCdWlvjz1c9qmMMbT-dGFI2WelnyTQa65ZXKER01NIbgtGcDnt6OkiAH1dXW1oqFozCTDapPsHAcdAFnLLp9c1DUCxgK7x122_B8SNgdwYBFchHPUxtobJXUFwm6Qs3Nq0JqEmBaZ3TGSzId0OaxXQy5cczOZRX-InJzZde-qbz2ve9mGqyvCPd2xPCKPA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.  ‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 26.5K · <a href="https://t.me/farahmand_alipour/6687" target="_blank">📅 10:09 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6686">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Z4alFYW6pG_gujF6mNER1GAeLgu3bEqcUqOfi9mmdXK0yGDHaHqOhxrs-2Bs8sjbLMqWseB5xlbBWbez_ZSHQMaP-tld7HS5NKBJx7IcTYbGgQ1f2wcDUPpsTxR3YLU345Md-QeJtGx7hffUfMuaqv6g4QwV0QIdN04VcZknn7zK6EIgsHXmfk_fgjVFQ2GllFqT5Arc988QBvxac3rhSOA_0v-czaFLTavq1eIaTvzK0QGfUHJvBUbuvlz-dt0iawxeZXDYMLpolkT0r_sqlCLQj-li_LPvCIODvlm-jx8lxKNfGi7X-IL2VQC5uSCHz1g-KewefEZm5kC0V9BLJg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cd8bd60696.mp4?token=Z4alFYW6pG_gujF6mNER1GAeLgu3bEqcUqOfi9mmdXK0yGDHaHqOhxrs-2Bs8sjbLMqWseB5xlbBWbez_ZSHQMaP-tld7HS5NKBJx7IcTYbGgQ1f2wcDUPpsTxR3YLU345Md-QeJtGx7hffUfMuaqv6g4QwV0QIdN04VcZknn7zK6EIgsHXmfk_fgjVFQ2GllFqT5Arc988QBvxac3rhSOA_0v-czaFLTavq1eIaTvzK0QGfUHJvBUbuvlz-dt0iawxeZXDYMLpolkT0r_sqlCLQj-li_LPvCIODvlm-jx8lxKNfGi7X-IL2VQC5uSCHz1g-KewefEZm5kC0V9BLJg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شش سال پیش حسن ‏روحانی: اگر تنگه هرمز را می‌بستیم تنها کشوری که صادرات نفتش به صورت کامل متوقف می‌شد ما بودیم.
‏کشورهای منطقه برای صادات نفت راه دومی برای خودشان ایجاد کرده بودند و در صورت بسته شدن تنگه هرمز به مشکل نمی‌خوردند.</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6686" target="_blank">📅 10:03 · 13 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6685">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">ارتش اسرائیل تپه علی الطاهر را تصرف کرده است. گفته می‌شود در تونل‌هایی که در این تپه ایجاد شده نیروهایی از سپاه و حزب الله به سر می‌برند.</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/farahmand_alipour/6685" target="_blank">📅 23:38 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6684">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">جی‌دی ونس در خصوص ایران:
ما با ایرانی‌ها مذاکره نمی‌کنیم و تا زمانی که آنها شلیک به کشتی‌های تجاری را متوقف نکنند، با آنها وارد گفت‌وگو نخواهیم شد.</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/farahmand_alipour/6684" target="_blank">📅 23:34 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6683">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oDQtk2bXVdrN3qE1Uc0wJpeS8yMNrYUAWFsd4r2Kg6q8BUzP7jt6fU2f_1YONcCkkyYTfqFJGv76MLz9n-rLSk6P33iUpdgvPT7TaLNpQpl-H-M0DkwdieyM156xTmSKz8trkpzjkFbdCkao_fwKwr11HWMIQZ01ZeQwzvz2euOscgZTjS7bxaFyoT_upKLxJ7xhnu7njDzRIagNdkR0CjGy-UHgzy59ldZbj2wA8aVJB4fyShlhfn0KUk46xcQEjAhdM20bCCA2preMX5601jM80x-hSsGQ9AHDfvVFg4dp7gROfGyaXR1gEyvkgpT-ZnZ4Lr8bLmGC5tZumNVXtg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f632dcbecd.mp4?token=oDQtk2bXVdrN3qE1Uc0wJpeS8yMNrYUAWFsd4r2Kg6q8BUzP7jt6fU2f_1YONcCkkyYTfqFJGv76MLz9n-rLSk6P33iUpdgvPT7TaLNpQpl-H-M0DkwdieyM156xTmSKz8trkpzjkFbdCkao_fwKwr11HWMIQZ01ZeQwzvz2euOscgZTjS7bxaFyoT_upKLxJ7xhnu7njDzRIagNdkR0CjGy-UHgzy59ldZbj2wA8aVJB4fyShlhfn0KUk46xcQEjAhdM20bCCA2preMX5601jM80x-hSsGQ9AHDfvVFg4dp7gROfGyaXR1gEyvkgpT-ZnZ4Lr8bLmGC5tZumNVXtg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">خمینی فتوا داده بود که دروغ گفتن
جهت حفظ نظام واجب شرعی است.</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6683" target="_blank">📅 17:32 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6682">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BYKHlcLJXB9C97XzOVm21KQ4W11B9fn6QvA09uPejtRhkcXiU1ch8Rf4q7ZJQuDsosXNHlnuyBKW9VszpAl5VaOnsomnRUccCdccPXPgmelRteTElJ0wos-ccrEuk9tn0TpDKLxRe66mgfYsoaIWcKbZrNzBV93PNURg082aa9IPx0zysXe0P2NrlWg6crmIlg3rbFaQhlz3kHZ-JYCd7OwlD-9VCwe_VOdeploB3GjYHDq0F0LUQVV96L3kLd3WazK96WTjZf2X_WT1Hrce55Vr0tVzqrQIciWpl1PXJ4Xb8DT8e8zi11MpdV9XRTZuS-lthwnGZEkmjSQ09Wo9QQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6682" target="_blank">📅 16:11 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6681">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eyviLsr8x-ClFCJZssncujanAAeY12MZZ9Xf1pXW0ULI48A5pK2xi4uoVLyVBIIgF8-ND3rAll8_WEyLdbySWlUVjn0uJ-TO0MTU863femC89JX6sJwnG0ltS9IIZb6hJItDgh55TbreKr6tGT7bkol07hlMGMNuYDlA9VgeosleyIb9teM6DsiV5YMk-ZUQA6Wk407FmmgLJYSmccW3YuhkjFla7_JoFP84lhvXHXcMQgSJ1Fv75FW83J14O-H8S9kiRdqAL7oO-nbmlk0Yobh5VSgZXRjHvmeY3vPTZynPV5Ewxo5t2pvr_hmp9A7PTC-bY2z1Q669TZnic8Y_RA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کشته شدن ۶ تن از اعضای نیروی دریایی در حملات اخیر آمریکا</div>
<div class="tg-footer">👁️ 25.1K · <a href="https://t.me/farahmand_alipour/6681" target="_blank">📅 16:10 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6680">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B5RLgiWse_Ik46SqUb_CclDCmUtxU4AVedevFkickcmSRfEWcxPIUqAfmNtUVZRaq2SLa1jJibkP5i9GMQaMnsZtzSQBJzYv9S4G7GJRNzCD85C9ZdQpE4FGe2WcZif-TgWuv1lT7vWvculiOFN6J2I3o7LJLkDNbFfb_-lW-vwBWFyCBT8eV4v7RSCdbmm5Mzri5EeCZcvgpsx2QgLH8uKHurLbzbNwsaC-rvunfm1b1cNpJOxcduuSv5xxA_41M9s7eph7Zzj_8Azj2OM_G76_CyzJbUncT2wbIWiRTqp-7EJLSN7i2JN8xcxkzAFDT1SEjT81LiK4SlixO5r6Gg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا بزرگ‌ترین تولید کننده نفت جهانه!
آمریکا چهارمین صادر کننده نفت جهانه!
آمریکا بزرگ‌ترین تولید کننده بنزین در جهانه!
آمریکا بزرگ‌ترین صادر کننده بنزین در جهانه!</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6680" target="_blank">📅 15:57 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6679">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">🚨
مرکز رسانه قوه قضاییه: حکم ساعدی‌نیا در دیوان عالی کشور تایید شد؛ ۱۲ سال و ۶ ماه و یک روز حبس تعزیری و مصادره کلیه اموال و دارایی‌های منقول و غیر منقول.
اعدام، مصادره اموال، کشتارهای دسته جمعی و در کنارش روضه‌خوانی و قیمه است که اسلام را زنده نگه داشته.</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/farahmand_alipour/6679" target="_blank">📅 10:02 · 12 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6678">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">نتانیاهو: ما جمهوری اسلامی را سرنگون خواهیم کرد. این نظام سقوط خواهد کرد. تمام نهادهای ما در حال تلاش برای سرنگون کردن این نظام هستند.</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6678" target="_blank">📅 23:20 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6677">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gIpOWbQse8idpDiWivSaMV7NGkdTX4mwwQYQnfiDk8CxIgMJumhC8cGWpc25gguIyz9ctm1JexdtdBc19HQz4qEWCEmhYEun-mUjyvnRIkqJUbEZxPRzqAHzjAiCXwp4goGIA-u-_dmdxk3Xhp_p-9fYjuWTIkWkTb3YOj8EH5QMuhaP-7pYljj9Wjs0JDJufnaV9h0IZj5b9-GCfcBc8UXSr3syhhEELMPSDYmdiiz8ALNpDzPmnEWZ7eyPeYCNpn2Elvf4yKPfIXL2SgFxyKRWcqzGl7rTvuxi7yOTmFRSnaqHsEzXgjRyU37y_w3AFj9RNLSYQSP4DYBKJG-nLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از پزشکیان
حالا قالیباف هم از آمریکا خواسته
تا به تفاهم نامه برگرده!
تفاهم نامه کی شکسته شد؟
وقتی حمله کردن به کشتی‌ها!
و گفتن امتیازهای بیشتری بگیریم و غرامت و پول از تنگه هرمز!</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6677" target="_blank">📅 19:54 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6676">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GyHqZF7jWO8CXkZ01QxA6GnuQWGGINiXqevGLd7XKHP3kAuafjLXOAof95dy5AZwV4S9DHsIiyfxWxfhvVfzkJAoT4ObkJxhwUeVNxJTlDlvv5VZsTmdNEpMdNb-f9HhPas4xERrG3MjWJuYYzLnf-G8vqGZpKIH6nrcD95Rt7p3bPUHZCq3rXlibS81XYOprirRtjIGoXcxaRPDeR-GlTEjMmrVuFDSUyuLGskZsrhsaYZZKBEdpQflA--L66Y5OeOTHIo91Mg1CALUBVimjD5tPXxk3e_-lQGeO12Jn1zJToCs1Z7-NPPzEroWasImplvs6dSw52LO-8ibYxqQhQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6676" target="_blank">📅 14:24 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6675">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">🚨
یورو ۲۵۰ هزار تومان را رد کرد!
دلار از ۲۲۰ هزار تومان گذشت.</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6675" target="_blank">📅 12:28 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6674">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CJROU5Z3iGM5hb_5Ap-cpX4Gza3blEZIKICihJNsUz-PLoaIc2KkWD0tZcxM2O3l70dAjBtDIuTJK-4y9vghoxHMha920TtdvsNjAoVLfs1LWHhS-21uSIZSS-MELZRFCwI8mEK5aML9hO-4u4Ee8bXjiETEfbSQEzQRezXfMZLZrSH-ZMcpeVbDEbWNhiwbnMgtPtDN2gYXRXdZiSPnmQ_n9rIQ4jGMQFEbD6EGTTnrPGIVJx0ooUeFKEncjlD5xdRrzc6dlD8mJZa2t30kUdE8VPB8H_iJ-tQS0M5j7vcQH3hWYIGUjsQ_iV1Ctp0dUvSbrgtgPZJrM-dzEjtYzw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خبرگزاری فارس از کشته شدن ۴ نفر از اعضای هوا و فضا (موشکی) سپاه در کرمانشاه خبر داده.</div>
<div class="tg-footer">👁️ 28.8K · <a href="https://t.me/farahmand_alipour/6674" target="_blank">📅 11:23 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6673">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/FL1NBo-hAIrTo95oDwr113dcWgwujlrY6vl8u4rMGUeSPciEkRjIEAm0Ld-Y8b6IEKp_--cyqswNUxAII6FppcCaUrfAJrqwflMT55qJkF5TnytGRbIxr8WS1ZMoOMdN0e6VNZbc80QRrxqwp-JvPMzTUc2qRhmR3mbxjhY9GR-iLkSH68Q8MXQNEW5_9Jm8IW0PYkUdxW4tF_51aARL1aARoeHsMKh9FNgMuUJinR1f4PVfClKLOeto_n7b1swZiUTCbVdG1VRL6KlFymvSL5jkVZq7Mpepv2TtlouhESPXm30RtUnpLnkyXc65YcftqFQHjId7E1KCGod56GXrJQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آمریکا به موتور خانه این دو نفتکش ایرانی
که در سواحل ایران متوقف بودند
با موشک حمله کرد و سیاستی
تازه را شروع کرده که هر بار ج‌ا به یک نفتکش حمله کند، آنها نیز با حمله به یک نفتکش ایرانی پاسخ دهند.</div>
<div class="tg-footer">👁️ 27.6K · <a href="https://t.me/farahmand_alipour/6673" target="_blank">📅 08:53 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6670">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/mb1QxGGAGD7hkqYDNpvUWEwm8IMmbrT1Dh4HFg6pFh6O8_A1X2E1r19P8TLA92DMlxoTIvfET_q6il5xBN6m4NSFceoIAJwKndXDlb9w5mpeGGtZLUKocVPd-Vs8liyE58iXBE1Gk25uZ9tukLG5wSjxl35yfOQUrbmwAse3LHYPk-wFkQiy7nxqybjhCQ9l0rdi2vBJIJQhRrwzpyQJUDDmbP4l5VIftdkcEZh-a-FdO02gKw17WpjqiC2jEKtvRx3xQrKNOUQXOSIswh5VsOYVPTmIDhyuaqNP-_o1v4HLgnI-Lq3BzxSSGv5KtxDnUlYpOT99He_11qJEmxqjEg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/F9FeWKonuy5X4RqHGbdDKzNmNAMvymPrZMTB8J5QZBm42ACwsKF7TggL2ubAIhulY-SLoJ8DiKE40CSwMKy3flbB4BatYDHfGiDRIdX9PGQI1HSEjqdYGlFxZxzzOTOCi0S65aAAZc23zQ6eBOikyJOqSVdGlOfwc1IQiDmC5Oaqec5mSrG9YRxCZ9yP-TAgmeDMkrmWuo_rw6U8h0GxHwk31bDqvg3yUTb518P7qQdsYDreqQzCvbKXd_AyEpNO9UDJIvAK_QJS6mah8l3S83RrKXGEw7sTN0QYVlOff0WtLI_v1kyDUuwsvrrx8NVfPpzi0K9kqyuyc_IMjsaEAA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/phKOHWbRjcSSK-gCzIT_JR3j4Z-1SW1uWYomoKyVqCUzYbohihQS3SVeKUSJHPLBQvs6XwlGksEfjMYlR4JzOX3bHq-97yjZrJDi4RiUItyD_sB7UZFJbl0R1n4i1TPXAufk9kWDogUpoGSi3D9BBsgqIKu6-umv-nOV33a2Ra25qNTppIHaWZk5u2sCBbCQFfvShUXzMcq5VNyWd9Qy87PCgqZj3Z4y8gipZrSiLYI9I0lphFab-NADKtUhjQCmKF6b5asUoKq20ij4Oh5U8sH198U-JO4kGIbL5XW8t32j2ijXJWYWVNF5yckEtL4XzZ7cGZxGaBpxnvSndKjx-Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">رئیس جمهورچین  حاضر به نشست
و دیدار رسمی با پزشکیان نشد،
به طور معمول در حاشیه اجلاس‌های مهم
بین‌المللی، روسای دو کشور در یک اتاق و در حل اقامت خود با یکدیگر دیدار می‌کنند.
(مثل دیدار دیروز پزشکیان
و نخست وزیر هند و یا دیدار دیروز پزشکیان با پوتین)
اما رئیس جمهور چین، فقط سرپایی
حاضر شد با پزشکیان سلام و علیکی داشته باشه اما نشست و استقبال و…. نه!</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/farahmand_alipour/6670" target="_blank">📅 08:39 · 11 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6669">
<div class="tg-post-header">📌 پیام #51</div>
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
<div class="tg-post-header">📌 پیام #50</div>
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
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">نیروهای امنیتی اسراییل (موساد و شاباک)
با ورود به نوار غزه، رئیس دستگاه اطلاعاتی و امنیتی حماس را ربودند و با خود بردند.</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6667" target="_blank">📅 23:55 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6666">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fea5666110.mp4?token=d94yLSC6ODmfmPhwARPoxQI0le16gg_4wBGML4YjIRk7ympE-BW0AaTh5L6tETmmuYTEjJfwoLGkalHd4LrduPRPWXrfkTHaY1GZ5DLrhW-f9APPea43hQmqBYXw9P4SOQtqakKlmfjsPxQ0qwpyQoP6HSwx_J8emKXTpQffvpLNsG0HE37ZnQJDtjxRVRjR_6MxEALzJgilkVNFk78WDmGQ_4m_5xTtP0oFWazwnpx1b7aSyTJ0HSzo-6tIGWp-X6reWERzrjibFWKpLsilY-iVYyfvhfbtVdwl5rivv5leRpXZFUzIXSmQ03MXfBGqh-1sdGp0NW-pobKggEm9tQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fea5666110.mp4?token=d94yLSC6ODmfmPhwARPoxQI0le16gg_4wBGML4YjIRk7ympE-BW0AaTh5L6tETmmuYTEjJfwoLGkalHd4LrduPRPWXrfkTHaY1GZ5DLrhW-f9APPea43hQmqBYXw9P4SOQtqakKlmfjsPxQ0qwpyQoP6HSwx_J8emKXTpQffvpLNsG0HE37ZnQJDtjxRVRjR_6MxEALzJgilkVNFk78WDmGQ_4m_5xTtP0oFWazwnpx1b7aSyTJ0HSzo-6tIGWp-X6reWERzrjibFWKpLsilY-iVYyfvhfbtVdwl5rivv5leRpXZFUzIXSmQ03MXfBGqh-1sdGp0NW-pobKggEm9tQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
بر اساس برخی گزارش‌ها یک خودرو وارد جمعیت حامیان حکومت در مشهد شد.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6666" target="_blank">📅 23:52 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6665">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🚨
🚨
🚨
انفجار در بندرعباس، کنارک، چابهار
سنتکام : «امروز ساعت 12 ظهر به وقت شرق آمریکا، [حوالی ۱۹:۳۰ به وقت ایران] نیروهای آمریکایی حمله به اهداف سپاه پاسداران در ایران را آغاز کردند.
این حملات پس از حملات اخیر سپاه پاسداران علیه کشتی‌های تجاری در تنگه هرمز و علیه نیروهای نظامی آمریکایی مستقر در منطقه انجام شد.»</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6665" target="_blank">📅 20:23 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6664">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/f90UkVZJ7p-TP5rFttQQjtrar2_f6ALL3hg1P86UY_YaJWJmZwIpjejpO4EII55oYii5EhncYCoIYojApDmYWBuWqoZUKtJFWZzEaZFenR2tCLgZCEype7CxuxE58nBBAbSLMFPdQsMtGOJuHilnfrX9Z7cOxXUQAzedbfa4u_ju91JsUVZ6LCBEFzVO60UaY7iZ21oIfIMhE43iV1Sy73BEV072gf2hcwoX46smVJ0tw3bhrPZ_CdS4romYDFDTRW_PTZ0bhfaRKxaaiFwrEFhNH85TDWnGhMxa9rpTZ2lmTVS7AuzsEKVImChMiAyhwmVQfloXFYRwtvFtUr1MRA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رسانه شورای عالی امنیت ملی!
دستاورد تازه : حوصله آمریکایی‌ها سر رفته،  یکی از معاونان و زیر دست‌های وزیر دفاع (هگست)استعفا داده.
حالا این سمت : از رهبر گرفته تا ۵۰-۶۰ تن از فرماندهان ارشد و وزیر دفاع و وزیر اطلاعت و … کلا کشته شدن!!
تنگه رو بستن قیمت نفت بره بالا به آمریکا فشار بیاد، الان کشورهای عربی نقت صادر میکنن خودشون هم‌ نفت نمی‌تونن صادر کنن، هم مجبور شدن بنزین رو گرون کنن و وعده خاموشی‌های بیشتر  و… میدن!</div>
<div class="tg-footer">👁️ 29.5K · <a href="https://t.me/farahmand_alipour/6664" target="_blank">📅 18:08 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6663">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">‏ پزشکیان:  اینجانب به صراحت می‌گویم چنانچه آمریکا به تعهدات خود در یادداشت تفاهم بازگردد، ایران نیز بلافاصله عمل متقابل خواهد کرد.
خودشون با حمله موشکی به کشتی‌ها از تفاهم نامه زدن بیرون، گفتن تنگه رو بگیریم و بهای نفت رو در دنیا ببریم بالا و فشار بیاریم به آمریکا و ترامپ و امتیازهای بیشتر بگیریم،
الان افتادن به التماس که برگردیم به همون وضع!</div>
<div class="tg-footer">👁️ 29.3K · <a href="https://t.me/farahmand_alipour/6663" target="_blank">📅 09:16 · 10 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6662">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">🚨
ترامپ به فاکس نیوز : به حمله شب گذشته جمهوری اسلامی به پایگاه آمریکایی در اردن، به سختی پاسخ خواهیم داد.</div>
<div class="tg-footer">👁️ 29.6K · <a href="https://t.me/farahmand_alipour/6662" target="_blank">📅 17:35 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6661">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CPO4pCst5QClsvy8edCImjZhOIOSsams0sIAUxrmzit7RyocNStjF2sp3k_HKBkrMXca7oKWqLiyyfeTdZAhkWQkQS8GKo3zrse55k8YfPTL2nCjZrVPIjJu8BjKPzye4kQCpcITljaoATWpw5-yRodRzTggZXRbwuzabP_3q-as14SfU8qfqlzvCWh8O07SNJJsk0jQwF8u42sY0S0XIcMXaAYz6gNq2Jo2sgpvjsnoIKK-MFJpo3pc8XfL_B19RaIit0qbvYyQLjGrfQ8ZQsQJAe6vohMwjJZoki4hMT13Y9R4CEI84MZewso7nH6pn-XFkAPv_JK0g_R3BwBJ5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پیراهن فلسطین پوشید و مردم هم
تحریمش کردند.</div>
<div class="tg-footer">👁️ 31.8K · <a href="https://t.me/farahmand_alipour/6661" target="_blank">📅 16:01 · 09 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6659">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fda626d442.mp4?token=LOrlhHCTWeFe4x6P_77NBudJnLE9lkp-OD5DEEzhneGVaDNh9kL-k8x4_0trTeCWsrouzKYG9054s65XjAL09Zun4yKR5PZuj5W7VitUjsPyv1Az51qWBHfDfQx2cdGAjvd8E0JKWcyQZyMAe-VK_IlIRukErYDldqIdeHQD5TsHXpAKt_56JASTCvjJnLTgMrUmYnIZ3hQsFOzDUt-3pdmUcBcF6ifIJCDiBHMAqY74ReimnnwI_gu_wZnKwXZ0MODfWSum3rqN4-zegJCJ1YkEOizsADWJ2Z5Bm-gDtzaQRNL0HPf_effp5Mg3jkWScdlXUR4VgpHDJ2Pvtbe5ug" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fda626d442.mp4?token=LOrlhHCTWeFe4x6P_77NBudJnLE9lkp-OD5DEEzhneGVaDNh9kL-k8x4_0trTeCWsrouzKYG9054s65XjAL09Zun4yKR5PZuj5W7VitUjsPyv1Az51qWBHfDfQx2cdGAjvd8E0JKWcyQZyMAe-VK_IlIRukErYDldqIdeHQD5TsHXpAKt_56JASTCvjJnLTgMrUmYnIZ3hQsFOzDUt-3pdmUcBcF6ifIJCDiBHMAqY74ReimnnwI_gu_wZnKwXZ0MODfWSum3rqN4-zegJCJ1YkEOizsADWJ2Z5Bm-gDtzaQRNL0HPf_effp5Mg3jkWScdlXUR4VgpHDJ2Pvtbe5ug" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">وضعیت بازار تهران و اسکله متروکه شده بندرعباس</div>
<div class="tg-footer">👁️ 29.8K · <a href="https://t.me/farahmand_alipour/6659" target="_blank">📅 14:25 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6658">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">ظاهرا مشاور قالیباف،  «قیمت پوشک»
و «خون خامنه‌ای» رو توی یک جمله گذاشته
اینها هم ناراحت شدند.</div>
<div class="tg-footer">👁️ 32.8K · <a href="https://t.me/farahmand_alipour/6658" target="_blank">📅 08:08 · 08 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6657">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=cFxTAP7JqfbV_GcHespUN59BsKwCZ_4qiaH7FlET8RCW2yS-qrySeO66xr7SD_NIsGcz4MDysaNWsM-dk8WEwFwpeR6eCqpChfDkyc1lkkA0zcKY0ZZcvy0zZ6Gy9ckD2yQOw2Zn6yj6Aq1uuDbU1KLYUHD9F56iBTWbWVc8R4Wo7oXkeMoXOqoFyON8K_jpWPAT42TZFaTn3Lqj9OCc7DAmE_UKXTq69PZlFpn3kKzJS1wej4tBeJC5Jzk4l0IwSjye7QzUrx7JDYjYDfXAkQoIF7O4uXZwkWn4jyD4HrWXJ3BlDE77aWEY67N0ctd-CE3VXaIUMAJw2XpBDgPxHg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f2da8f260.mp4?token=cFxTAP7JqfbV_GcHespUN59BsKwCZ_4qiaH7FlET8RCW2yS-qrySeO66xr7SD_NIsGcz4MDysaNWsM-dk8WEwFwpeR6eCqpChfDkyc1lkkA0zcKY0ZZcvy0zZ6Gy9ckD2yQOw2Zn6yj6Aq1uuDbU1KLYUHD9F56iBTWbWVc8R4Wo7oXkeMoXOqoFyON8K_jpWPAT42TZFaTn3Lqj9OCc7DAmE_UKXTq69PZlFpn3kKzJS1wej4tBeJC5Jzk4l0IwSjye7QzUrx7JDYjYDfXAkQoIF7O4uXZwkWn4jyD4HrWXJ3BlDE77aWEY67N0ctd-CE3VXaIUMAJw2XpBDgPxHg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">همین که به چنین وضعی افتادید
همین خودش اعتراف به شکسته</div>
<div class="tg-footer">👁️ 31.9K · <a href="https://t.me/farahmand_alipour/6657" target="_blank">📅 15:26 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6656">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SkytHy32CAGGtHh91nxQJax7k_999E1-sepE1doZLsMe_qjGhESXzB7FUX-tOTwCGO1CVrbbSuWLQd7AVDiwBSEWdLxODqKOGSp7WEb0tdkOjLuNfSeiy4GcRYeVDEmB7BywusycstTBVSIeyKfC4kfSgbXbQFA3-izAngUoEc1q5a71wp05d1oUpY2kS3Rp3yUVUVetqmgP8stJNfsQYNzoqMg2UQlBGmb6Cr55UYLqd3RbY1jnMlNAxkcY4g7iuGLbUw_fCA5bDqkULXjxqpoMwTVKehPVCkE2aY87EY0_3wpCT6S-jr5trwxJHJvo4ayqbDiHlCUEwUX3R7NNZg.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CbmZgR4PYMdugebZJMx6lN3fBqNi_ydlmA6GvLYr_y1SdcRMmcLVqj8UnkyOiZx1xK-ujU458xAiwtBO3ibs6m3sYhcHDusiC5tkwy5Eg28ryPjvmxxAYSIN1wGjjDRGil6SJhOKTrgVB-ctK9QAxgk1falojao6_saAW_VEj5Co-XvvenOX-kzeauJvzxsWPZAkbz7uRCn0f7m5QBBe2-fIzfQ1cO7nE284GLtRcduNv05SRkyzCHwZ9V1-mi0VQDmX4whrmc_gSU_wL0PP_eImXM3Dpp33BJesCvwO9LnIyChEXHVJIMz5tOuI19vv3w9bny0-mRsbseSbFew1lA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صادرات نفت کشورهای عربی
خلیج فارس در ظرف یک ماه، دو برابر شد.
جمهوری اسلامی تنگه رو بست و فروش
نفت خودش متوقف شد.</div>
<div class="tg-footer">👁️ 29.2K · <a href="https://t.me/farahmand_alipour/6655" target="_blank">📅 07:43 · 07 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6654">
<div class="tg-post-header">📌 پیام #37</div>
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
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eOh3wpCLnMnW-dPqtSDAF0P1CGZ_4ONs-rF8Rk8pNv7ZBB2sl7o0rrqxDV-RR2CjzTwqDoBP8Vk3RRxEodRmirdgcfUAWfUkuWhp62AFxmjSv_3jE3NSh5ZXcA6GNdXHVXor2kC11H1uNQCfltKfxcmM6grDlM2vrKWM2xs07_vacKKNvzseozhSAxFjQ0Ihdrv0Se-40pOc2ZxeKQ6w3eRUj_HyB_4FtiI1YXWigfyBNqJMHkQ3hmkDRpLHLnVmDNNwHCvAgDdwTRm_or4KbWz3Bv5q2e04SdQnmReXh7i26h65mU_2lhG2GVi_ts5OAqhLByLtBAKNpNtDYnYblQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XWUZu3thKBQAa4MMLmtTELxDJ1KiohDPvhxMJpwQ6e9W52wl32Ma9x64TGVabhKIerUWVgDR7g15cQJaFjBm8LeUlTsspWuw17aNmL55ACbHa301HJESzcaZr_QDmNLLhPJSyOVBUa7T2995fL8cd2aJ8zzwBXG2zqbSE2ssh_1pNTxHDupMzwbuoJ9j-vf7Y8KNveAcYwHeTDhdnchvWFO9Q9kKg8YA9_IKhrwW4WnFR-7VLhCJb6jX7S_ez5zNfee7q3gfYiPpkz_4pQvEQ2U4GIvw6-293Tl5hsdaAwoCo6Nkl0TE629WWJVMif2gzevwbzqzbdisCrX-eyrZgA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی بعد از این سابقه درخشان در بنیاد برکت و ستاد اجرایی فرمان امام و….. عضو هیئت مدیره همراه اول شد!  که بخش عمده همراه اول هم متعلق به همین ستاد اجرایی است،  و مخابرات هم که مال سپاهه!</div>
<div class="tg-footer">👁️ 32.1K · <a href="https://t.me/farahmand_alipour/6652" target="_blank">📅 09:29 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6651">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kW7ogMPBc9vRj1KtRLE2__yO0apLdpdN_om2hHacQ3xaXFRCBXiho4rbW3RANr9mPDytJYCJ9BQMjXBgl8sXSWQtoJt--N7c1mzn2rvMiEDU_bM7tz9W-9nqw0B_tq8XTlbG1UL885CrUCQO28Y9xsH2v9H0vft5m14wQIlTcb_JFoWvBywGfsB4VSDprOzt6YcIyDvldco4BWxwqyFxWrnHV-OndVo7UtgxNoujcw1DZCbExm_3VdFdxBi1KnGvft2V14loLb-aYlr-ZzAbc0k13a0-v4v4LtKXowAP4lti2Fww18ndeg4RUnQ3qxi8Fv_1N9GcJbFxBZsCb9sq3A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خامنه‌ای واردات واکسن را ممنوع کرد.  خامنه‌ای به مردم ایران گفت  بروید و دعای هفتم صحیفه سجادیه بخوانید!  زیر دستانش در بنیاد برکت و ستاد اجرایی فرمان امام و….. اما دست به کار شدند، صدها میلیون دلار از دارایی ملت ایران را با قلدری از دولت گرفتند و گفتند  «خودمان»…</div>
<div class="tg-footer">👁️ 30.5K · <a href="https://t.me/farahmand_alipour/6651" target="_blank">📅 09:27 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6650">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mW9pfZW2qPkBCw9r_FyzJkDVhfTVO_rThu8U_y-upRjaY-ckXDvWZn0gV9-N-hYKgHyRE7U4LW6aeTdnLieapWLHwju5sl3LBNBNlP9XZVoL42EqJZBazIlhZPQvqK40s05Ew3THcZDTbmqHIDScmDAyNG5E1gwFYZb_7-0pZAwfq-6PKoq-DxyZPyO5Z46GENMF5dVhCKCBiE9Ag8igk_8fjyr2gMiKgSVgYfLjsana9bPrZXtm2tgIR4C2f_-VLZFZrT5VNys-O7OYTMiGArwV7oLyjHfchzHX6YEXcmUMfVm2EL26HE1Ns-emxO446JAM1ZmarmJcPRmpyCC_wg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وقتی اعتراضات به عدم واردات واکسن اوج گرفت (فقط و فقط در دوره مقاومت حکومت در واردات مسکن بیش از ۵۰ هزار ایرانی جان خود  را از دست دادند)  او در واکنش به آمار و مرگ و میر روزانه  تا بیش از ۷۰۰ ایرانی گفت :  ارزشش را دارد!  برای «اقتدارمان!»</div>
<div class="tg-footer">👁️ 26.2K · <a href="https://t.me/farahmand_alipour/6650" target="_blank">📅 09:23 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6649">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eJ2xNfBBOmG1YL44-FmhCug0U75teWFdHB093cC7HfPAXiqxuQRHBmV4F5hFg4XL3ns_zkhNMA9tLmn0jd1mFjpq6ZoJFW9FZ8VAkHTIo9GLF3VQMLpoLfUB9N2IqqruzRfKfDT-Xpze_wJIq3nh3QzgYxjcA0Hno4hMUx0ehZXk8Glp5EmoeCMH3QAymBaBkuZV4TbSCNfGgC_oc0aldAo4WPbX5yqMTiPlpLjQK_j85pZdo1qjuTh8ucLJb0wNy5uzoNbGTleOGLVePdg5IPVO5bPhco1OqLpioe3KESCwvsdTAwqGWnbbQz0dWj8QKjNUEQsZRsQHLfDmeXXkwg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حجت‌الله نیکی ملکی، دیروز به عنوان رئیس هیئت مدیره دیجی‌کالا منصوب شده!  نام او با واکسن کرونا گره خورده،  او سخنگوی گروهی بود که مخالف واردات واکسن بودند.  رئیس مرکز اطلاع رسانی ستاد اجرایی فرمان امام بود، ستادی که پولی کلان از دولت گرفت تا واکسن بسازد و…</div>
<div class="tg-footer">👁️ 28.5K · <a href="https://t.me/farahmand_alipour/6649" target="_blank">📅 09:16 · 05 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6648">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SUEG46qeyaU8_J25ci_07agu4RbnAHy7TDBlhfF_zCXQfqug_lFWpSMR_fwQm2ITI3Jm6aclJ8vg3ukbs9Nb0lAdxpxuG-urugm0Oin7mLNZsNip2ascVOlLE490Zj8RCrjum-cI44zu4G9fz0X1eefQPrT2V824mehJZfnu0WKaAcFvIFI8rrvGe_3jBn7x1dnIZ7KUr2RI6w2upiTtlgeuEpu7CFFFewP0ogANuG_BhbdvHf3KbRjnwxzELiluxJXeoS6boxHWJix3GtU1yqjYJ0JrVDtU-cObP8c69hKDWkl9k48VLQdWLioz5oAJQXD3HAXenXqJS-OFL3FsoQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=iRVDQ2De5YCpCaFeW_HxdU0eWnoMb7A3mO7Nht8GJSLVAPmlZu6VsFxUxIBGhEK60yZPhv1XPN8oBW4Zk-Ysk7GekvFl-6SHavo4FF_6YJoBvSwXEw3seOP5xFXtCXqWYjcY2ENdK-OWSmjTqOLjbtROEx_J2VrYCZQG3C80N91OTWjkTJ6fTvQPoexqxuvyH00d7d3UQo-y8Xm89PefAR-dtY2kvEU4m_xeRw9_4LPk3dREEeLoDLyyX0U2sM07hOne2ypMm0cfoutFnr4yE8R6DaRv1S8OxCiSYBxi0zgLrTeBcnb9bmQtetjUtJtAuEe77w3Upl6C18w7iytb8g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ec877d4c5b.mp4?token=iRVDQ2De5YCpCaFeW_HxdU0eWnoMb7A3mO7Nht8GJSLVAPmlZu6VsFxUxIBGhEK60yZPhv1XPN8oBW4Zk-Ysk7GekvFl-6SHavo4FF_6YJoBvSwXEw3seOP5xFXtCXqWYjcY2ENdK-OWSmjTqOLjbtROEx_J2VrYCZQG3C80N91OTWjkTJ6fTvQPoexqxuvyH00d7d3UQo-y8Xm89PefAR-dtY2kvEU4m_xeRw9_4LPk3dREEeLoDLyyX0U2sM07hOne2ypMm0cfoutFnr4yE8R6DaRv1S8OxCiSYBxi0zgLrTeBcnb9bmQtetjUtJtAuEe77w3Upl6C18w7iytb8g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">تفریحات شاد جوانان غیور مسلمان</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6647" target="_blank">📅 17:45 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6646">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/uK8tB4LQeSxay84hCDiJIvryBlQg2XEB7KhZ0fbKwgaSFA5mt3ODjMd0ey_p2QS6WweAzyxMD9IL-iFxXuL8_xmDHTxbQXwMdRYN1LS4CdNHNdPQpR_qtJsGCj_6DSVqBHdwzA8RX5Q6L6ulOH_RKunI_zurFA6AMrny3EUrc8DUAxpnKxwRmKl-6gIjtSZTf1Ddjpsz9o9frge6yRWvB_9y8bK7n4C38aoxWHdM6oNPRECrclCkXksCciqX2a1YXY2ri4HHohGJoJoX2cQ2jz3Qwb1uj0Lnzg-UmmPWuuVs3697fXEMaGzImRgASUSc4es4pB4Rk3hUOkO5i2_N2Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الشرع : حذف رسمی نام سوریه از فهرست "کشورهای حامی تروریسم" را به ملت سوریه تبریک می‌گویم و از جناب رئیس‌جمهور دونالد ترامپ به خاطر این تصمیم تاریخی و همچنین از تمامی برادران و دوستان عزیزی که در کنار سوریه و مردم آن ایستادند، سپاسگزارم.</div>
<div class="tg-footer">👁️ 27.2K · <a href="https://t.me/farahmand_alipour/6646" target="_blank">📅 17:33 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6645">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Y_20ExIsAFaIkhVojQwcQLijFTO4zjY-qExf97rFPD-gZ6DFa3NzG_zJ4jcOnLkZ8J51W3GLYWFCLmQlOJaIBx0N9jes-e88eAjc8kFJniWzaCsEto01YgTm7ybUz8nVmePQXbUtUq7RTTm57A1-z44UG5PIzoTHRpvw1lKR9oWbpFA4H6NYt0e89N8qf1yovRPnu61gX_YArC24WUNKJ6OCN-4IgdDt7URnFV3LG06GVIJfDIIIoQvtP_cjiEa8zs0uaOdEQ9gfzIRGkwehRSfCphu_EIS-ZPO0jw_Z8r1gj678uFxLMtdsHKi5X_iNzfL6WQdMDupLrWmBzoFwfw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c6f972068b.mp4?token=Y_20ExIsAFaIkhVojQwcQLijFTO4zjY-qExf97rFPD-gZ6DFa3NzG_zJ4jcOnLkZ8J51W3GLYWFCLmQlOJaIBx0N9jes-e88eAjc8kFJniWzaCsEto01YgTm7ybUz8nVmePQXbUtUq7RTTm57A1-z44UG5PIzoTHRpvw1lKR9oWbpFA4H6NYt0e89N8qf1yovRPnu61gX_YArC24WUNKJ6OCN-4IgdDt7URnFV3LG06GVIJfDIIIoQvtP_cjiEa8zs0uaOdEQ9gfzIRGkwehRSfCphu_EIS-ZPO0jw_Z8r1gj678uFxLMtdsHKi5X_iNzfL6WQdMDupLrWmBzoFwfw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ترامپ: محتبی خامنه ای رهبر ایران  به‌شدت مجروح شده است، سمت چپ بدنش، دست و پا و در واقع تمام آن قسمت از بدنش به‌شدت آسیب دیده است، فکر میکنم او زنده است.</div>
<div class="tg-footer">👁️ 26.7K · <a href="https://t.me/farahmand_alipour/6645" target="_blank">📅 17:21 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6644">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/374629de87.mp4?token=hvFbnrnUoNiOf99huw3Np2MMkrxBzMY4P777JLCYXhzAYVXafWAV46AdVH9fDwEoYjNpRdan_iBog-VmQp1RF9UrwPeB0vYyuCvgtdBsIJGCKgjflPp6iTv2BkzrTWaOiippZHlyaD9txQIFuZ-DZT0ZLGLhzxrOgIyU88vRUYBZd9vzTCF-mPvH1Ogg20EPZqGVh9Qyt9uynW7aqtX7uQBm3KoLtVSlaZRExnViL4UvSsrQnEE4gwF8NYl6zaLiBHKCPvf52KpuDDliS8F10IGZMoOeEz6l-nGbcP3mMyQKU9xUmnHUlHLnCeI0yhd2X2VfJpLeROlbwanPPVa6Ig" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/374629de87.mp4?token=hvFbnrnUoNiOf99huw3Np2MMkrxBzMY4P777JLCYXhzAYVXafWAV46AdVH9fDwEoYjNpRdan_iBog-VmQp1RF9UrwPeB0vYyuCvgtdBsIJGCKgjflPp6iTv2BkzrTWaOiippZHlyaD9txQIFuZ-DZT0ZLGLhzxrOgIyU88vRUYBZd9vzTCF-mPvH1Ogg20EPZqGVh9Qyt9uynW7aqtX7uQBm3KoLtVSlaZRExnViL4UvSsrQnEE4gwF8NYl6zaLiBHKCPvf52KpuDDliS8F10IGZMoOeEz6l-nGbcP3mMyQKU9xUmnHUlHLnCeI0yhd2X2VfJpLeROlbwanPPVa6Ig" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">در رژیم گذشته‌ همه همت‌ها و توجهات این بود که آدم خونه و ماشین خوب داشته باشه</div>
<div class="tg-footer">👁️ 29.7K · <a href="https://t.me/farahmand_alipour/6644" target="_blank">📅 11:46 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6643">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMmxkiAiVTzNCJYTStYoHrXX0CLGSED7zHHxS3n4Cwl0NsuHhz4PQT4qYCXZUPeICGay54eXTeNhbtxgyBXhXP6_G5tLfDiPRjul542nZKzuRa5gR_hm9yUNJyGRE0H9wq1CK2_A37lvo_s45JPn_5rb_ymGy-eT7QL8mP2FCvHQQ2Ld_HcX0BfnWAWG8BK4waZ6wNtE1rRtUVYAHu71T2Ju0AfgQWz73z6NrFvgr_GjLU0zltVq57APbiMUFGk9WG8ozVz-gyVS7EMhxwNQ9139dlQP09Mh7rTwaFiuGnCe84DQ9Uj8uxbajfGkSFvYlo0wgFKSWjHA_eKHBkH8cQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ارائه دومین هواپیمای غول پیکر سوخت‌رسان‌ به ارتش اسرائیل.
دولت بایدن با تحویل سوخت رسان به اسرائیلمخالفت کرده بود و مانع ارائه سوخت رسان به اسرائیل شده بود.
دولت ترامپ اما مجوز ارائه هر ۶ فروند
را امضا کرد و سوخت رسان‌ها یک به یک راهی اسرائیل می شوند.
نیروی هوایی اسرائیل، قدرتمندترین نیروی هوایی منطقه است [برای یک دوره کوتاه، در زمان محمد رضا شاه پهلوی، نیروی هوایی ایران قدرتمندترین شده بود که امام با آفتابه از راه رسید]
اما تحویل این سوخت‌رسان‌ها تحولی بسیار مهم در شصت سال اخیر نیروی هوایی اسراییل است و دست اسرائیل را تا فرای دورترین و شرقی‌ترین مرزهای ایران باز می‌کند.</div>
<div class="tg-footer">👁️ 25.9K · <a href="https://t.me/farahmand_alipour/6643" target="_blank">📅 11:22 · 04 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6642">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">رئیس سازمان اطلاعات آمریکا (سیا) برای یک سفر عازم مسکو شد.</div>
<div class="tg-footer">👁️ 27K · <a href="https://t.me/farahmand_alipour/6642" target="_blank">📅 19:32 · 03 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6641">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ydts4MVv2KYCIWwLMcH8jpoKa50ERE3YTRwjFb251hIxIFjwyomHcCXsOQPcI-6VIeqri_NdIgxMwo0_B_9YewpoESpSezo5Ytq1ceMMukf6735U-KjJ1GuTs7WCLxOf0SbaUhm7jQu7ElPA9kp-ovi94JzqCtLthOAvnTeZD8pfqWJw3_SlvZhjA6qeHf9QQ-v6t4_CVepsyo7j4xKywLd2mbCfs9lKJ-ECrIPOALsuOnccZUGeB9e0E-4SiQd15QXYLEwZss813hceDff4sN18p188-tQZp-rpRirRl2or2vdvvmvWzXf4oqIlWntj2aK8fHPgPcbRE4CYyAvyXA.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #23</div>
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
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">🔸
اسماعیل سقاب اصفهانی، رئیس سازمان بهینه‌سازی مصرف سوخت و مدیریت انرژی، در یک گزارش تصویری به فساد ساختاری در قاچاق سوخت اشاره کرد
🔸
او در یک گزارش تصویری که به مناسبت «هفته دولت» در روز دوشنبه دوم شهریور منتشر شد گفت: «هر دو جناح سیاسی کشور در قاچاق سوخت…</div>
<div class="tg-footer">👁️ 26.9K · <a href="https://t.me/farahmand_alipour/6639" target="_blank">📅 13:23 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6638">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromRadioFarda</strong></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=feRJPZe51s397b7W_VBbApnLS1s7sfnMdFmiIafUN0xwemltTf0hZLWT5WYSe7tItUYez5ixcWDkKe-az5eb3q4J4iBrkUhXUnilMlNS0g69PQOrgD0Mx7EunRptNe0YSWIHy4CLVVkFVG_VRMOSuPh5o8NbtbfGM1A9L4wy6EGS1z62CTNork8D9_5QJSDvwjv0kmgbAWPd3BDXy99Rb6g8gYFpMNDFZfwWfQwSKT839_NmzJBGmhi2Wrx7amyyc6_cIXBpYEa71HrFLyw8RZvflLPuU_CnNX3goKioemcqnBYsblX1DoGLo8jQIuSk6itrla2wuhDJ2RG9N20hAaokHVLBnsITrMi0tsjlFcHIQ0dmnU-ZB-tZKDQAdBKoJr9eACf_SaeHc5hBWSCKt6YBp6FBj1D3dmvHgHnE-4mq7fV150qSRFQeoaiOTAKx2sVS9m7Fz0855agLdUR8UqeDt3WehKAAMzLfbuUma_9J0iKmPexOqImRtDfjr-DvjqIzHky_hbCqpwKXVy346MhYTf8i8uotLw03a1kzborS1yC7WSfGhAayRyf6WlLYkuNWJmHweIZIZPNTQuLQV4iJ73_b3yO7ARXVz-Rst-g5AWO2N2Qo7ZhQJoCA1rRo__Yw9g4q4gDx0LpQPfK7sUva3-xLYl-pDTsi-bo1fp0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0e9949129.mp4?token=feRJPZe51s397b7W_VBbApnLS1s7sfnMdFmiIafUN0xwemltTf0hZLWT5WYSe7tItUYez5ixcWDkKe-az5eb3q4J4iBrkUhXUnilMlNS0g69PQOrgD0Mx7EunRptNe0YSWIHy4CLVVkFVG_VRMOSuPh5o8NbtbfGM1A9L4wy6EGS1z62CTNork8D9_5QJSDvwjv0kmgbAWPd3BDXy99Rb6g8gYFpMNDFZfwWfQwSKT839_NmzJBGmhi2Wrx7amyyc6_cIXBpYEa71HrFLyw8RZvflLPuU_CnNX3goKioemcqnBYsblX1DoGLo8jQIuSk6itrla2wuhDJ2RG9N20hAaokHVLBnsITrMi0tsjlFcHIQ0dmnU-ZB-tZKDQAdBKoJr9eACf_SaeHc5hBWSCKt6YBp6FBj1D3dmvHgHnE-4mq7fV150qSRFQeoaiOTAKx2sVS9m7Fz0855agLdUR8UqeDt3WehKAAMzLfbuUma_9J0iKmPexOqImRtDfjr-DvjqIzHky_hbCqpwKXVy346MhYTf8i8uotLw03a1kzborS1yC7WSfGhAayRyf6WlLYkuNWJmHweIZIZPNTQuLQV4iJ73_b3yO7ARXVz-Rst-g5AWO2N2Qo7ZhQJoCA1rRo__Yw9g4q4gDx0LpQPfK7sUva3-xLYl-pDTsi-bo1fp0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
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
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromeuronews یورونیوز</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/v5GNGWGCoHpNtiYTF-GeBDXoUUCzcrjML3LCeL4eEiKBON5PQ6NEBT28N4ebmk7SHsl2idZVX0r4a5VK5JX7aHLGJ5dKpSnlGYeNjh-k8ZAnOlj3f5QnsIEuqTMJ4ncgLIoYIRZnu6cA96U_Z8d42l3_i6C24FUaXxor_z28HIyNzBVB267A92bRQoqbMzTyagtwEIaJGenTVvLh34_kfuPqJCI3lx5E5wDu4K-vPRcVqq2EYmZkAUJhI6GPplahGdIjV8JbTfABQe5D6lp6Q4xELDIW-fDEvtJVWhYUmTmJuxipQKKXZUXtvis9zpSavrvEPYqseG7V_Nc5JK8WtQ.jpg" alt="photo" loading="lazy"/></div>
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
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5eslNlFtRS_I4Sm02OlwJ8mTmmO3uUewYUDmYC3jvNEfxEwEjLoDjmt-e-TcrbpNJaMQCdjIhIAYUEuTFSthjS8uTV51Z7-EZWaORapCnu3-naFdyFXrXVVssmTm2zX6HGUzGcwlmbOsF5BOuwJJXmxESC6dyiMl0CM4ifvrWDvdcrwmZVeMAL06iXYEeXvwS2G7oYF6Q7mz2qRaMuUKcz9l68lI8b0Hv6K6SD8di21e6jeIx92Tg6MmF7evXmE15Dvdo6L35EpQJn03g6GoPGpZcid2u9Sj00RXnLlqvhw0rvEhDwb2wEmO5UI5imF9MTxO0syfrIv6LzgfExQIg4A2QIkzVRI_wt7iVajDAVNJ2feLnNiclgctON7C-cyuCfIX0toa9lXGL1NZSazobhGy9sN9Y9adHMMRP1FCHqW0ypvISNOlCjUDyWPokaLMbpRvrYc8x1JBn12YC22h9avlOFDj0YPuHl7I_m77QH3THY_Gx8ZqsucEMBa4iS_7lfebvxeOhnSfgkQa-X5skSfMouIt3a8dkAg3SiKFNpb9bNncAOQgIWooEuD7yQSTMOdbHMF3D2xYZubgVhi9GsyzlcV0H3i3I9wv1IjQzYDqfEqvtNmh51zcfbM7qO8t1KJ6U2RHMvmPtXooNnmIBW0foCyulDWyy5k1kQf7a8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8930b829ed.mp4?token=N5eslNlFtRS_I4Sm02OlwJ8mTmmO3uUewYUDmYC3jvNEfxEwEjLoDjmt-e-TcrbpNJaMQCdjIhIAYUEuTFSthjS8uTV51Z7-EZWaORapCnu3-naFdyFXrXVVssmTm2zX6HGUzGcwlmbOsF5BOuwJJXmxESC6dyiMl0CM4ifvrWDvdcrwmZVeMAL06iXYEeXvwS2G7oYF6Q7mz2qRaMuUKcz9l68lI8b0Hv6K6SD8di21e6jeIx92Tg6MmF7evXmE15Dvdo6L35EpQJn03g6GoPGpZcid2u9Sj00RXnLlqvhw0rvEhDwb2wEmO5UI5imF9MTxO0syfrIv6LzgfExQIg4A2QIkzVRI_wt7iVajDAVNJ2feLnNiclgctON7C-cyuCfIX0toa9lXGL1NZSazobhGy9sN9Y9adHMMRP1FCHqW0ypvISNOlCjUDyWPokaLMbpRvrYc8x1JBn12YC22h9avlOFDj0YPuHl7I_m77QH3THY_Gx8ZqsucEMBa4iS_7lfebvxeOhnSfgkQa-X5skSfMouIt3a8dkAg3SiKFNpb9bNncAOQgIWooEuD7yQSTMOdbHMF3D2xYZubgVhi9GsyzlcV0H3i3I9wv1IjQzYDqfEqvtNmh51zcfbM7qO8t1KJ6U2RHMvmPtXooNnmIBW0foCyulDWyy5k1kQf7a8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">اعتراف به جنایت در سوریه</div>
<div class="tg-footer">👁️ 28K · <a href="https://t.me/farahmand_alipour/6636" target="_blank">📅 09:20 · 02 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6635">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/farahmand_alipour/6635" target="_blank">📅 18:06 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6634">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">🔴
دلار : ۲۰۰ هزار و ۸۰۰ تومن!</div>
<div class="tg-footer">👁️ 26.6K · <a href="https://t.me/farahmand_alipour/6634" target="_blank">📅 17:42 · 01 Shahrivar 1405</a></div>
</div>

<div class="tg-post" id="msg-6633">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vxP7MY5-S2K8LNYGQkz7ey2ntP2HzvtIM0JP6lJvN-knYB_VLmj_x7DtvmVXUA8TFpIG2ZjqlbSxGGg1QxAQHJ9UwNdb7qf5UKiN_NFKJ-636kkgpce9GH1ETDTZ7ipOTGQ9BDfXhA4TR852z-OEvsfhfqxrWadQuppi_I_LW90pF7KOS8zi_fI5WGhb2WZutnlh1Tz7iei68BKOkq10CquNxMClM2FYLvn9_kshw3lhhkn6NbxrbfImrJ2djlMP_XbWkiLva1jaUkPXf91egu7xFPhtC63ri6qcaTAwsHTLgnzKv9BW6HqG_6xmof8vJX1yT_zQ44NGQgEhOcVObg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">الحبوسی - رئیس پارلمان عراق!</div>
<div class="tg-footer">👁️ 37.9K · <a href="https://t.me/farahmand_alipour/6633" target="_blank">📅 19:03 · 29 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6632">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Eyym0v1myTpt_VS7dWPhg8NCHnd6QVjuuAH3LCxagKmwriSSaIrMQdpuJ6zDQYSnTU277HuoWqYE04RWJqJ1ptFpFWbwpvviUh8ANyjgrKYRz45cwnv42LYQRxgshlMQPf3opbX8llytSsZomauH5wxaTHvvEKjD9bBgismoVDh9tbgzd114NjKGQnMvz5Gho20tnCshK0GZpocUgn6U_A5Nl-QABxBYJyPHBNif3stPPK0i8zW9-BzRqWGI9VdqvUn6sJ9H72Pvkp-vmqpzV8WeqlUreWMgExOzJNKHo1oNJrTLtN7Ev8g7cP36Vi4RB0L6ge38O8FiczOnEJibhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد از انقلاب ۵۷ و از آنجایی که مبارزات ملی شدن صنعت نفت، اساس و پایه «ضد استکباری» داشت، روز ۲۹ اسفند رو به عنوان روز ملی شدن صنعت نفت ایران  وارد تقویم کردند!  ( از قضا ۱۳ آبان و تسخیر سفارت آمریکا  هم رسما روز مبارزه با استکبار جهانی است!)   ولی آیا صنعت…</div>
<div class="tg-footer">👁️ 36.1K · <a href="https://t.me/farahmand_alipour/6632" target="_blank">📅 20:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6631">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">مصدق برکنار شد،  چون مجلس رو منحل کرده بود!  اقدامی که باعث شد یاران خودش علیه او بشن!  مجلس علیه او بشه!   مصدق برکنار نشد به خاطر اینکه نفت  رو ملی کرده بود! ۲۹ ماه قبل از عزل  او‌ نفت ملی شده بود!  این دعواهای ماه‌های آخرش تماما  با مجلس بود! مجلسی که خودش…</div>
<div class="tg-footer">👁️ 34.6K · <a href="https://t.me/farahmand_alipour/6631" target="_blank">📅 17:19 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6630">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">سرهنگ نصیری  وقتی مصدق به طور کاملا غیرقانونی  مجلس رو منحل اعلام کرد،  که فقط در اختیارات شاه بود،  شاه نامه عزل مصدق را داد دست  سرهنگ نصیری فرمانده گاردشاهنشاهی که ببره و تحویل مصدق بده.  آیا شاه حق عزل نخست وزیر رو داشت؟  بله! طبق ماده ۴۴ و ۵۸ متمم قانون…</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/farahmand_alipour/6630" target="_blank">📅 17:06 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6629">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cqhFTZsL-ilPSXWsE9cq5eEE77Bz5nYobzhImNhbUpQ8X-Ufs1rVLEBCEhZw63A_932wDaX2SjcNl33TOO3gtxV2hk6RIBNBcFu3gkhZRO0o3OvIYci14heQbjtpwyp8j9zhf129edTGQk4PM_XSFCu_rVdEq5GeHvK3vNU1YXCNKe3diqzh-_8vBmjSP8_LcxjLuKC9-a5aueWYcDvMRCcLF6A6ennMvXyhJu3p09OrIqftR5wEitZkMJwiVFsCfy0meHhxDU1uBtff6ygSQEzy8YEhI6V-pa7DAGumLaF7f4cTI6lP9zenrUO_knN8TtEyRilKVx_X-HaXewyvZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بعد هم یک انتخابات نصفه و نیمه برگزار کرد و طوری انتخابات رو جمع کرد که تعداد حامیان شاه در مجلس زیاد نشن!  و مجلس رو با ۸۰ نماینده بست!  شاه در عمل مانع این کارش شد؟  نه!  رفت رفراندوم غیر قانونی و مضحکی در کشور راه انداخت و مجلس رو  به طور کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/farahmand_alipour/6629" target="_blank">📅 16:42 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6628">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">مصدق با عنوان ملی کردن صنعت نفت  (که در عمل هم رخ نداد! و سال ۵۲ رخ داد)  کشور رو وارد یک بحران عظیم مالی کرد!  شب و روز هم سخنرانی می‌کرد که رضاشاه راه‌آهن ساخت به خواست انگلیسی‌ها،  مدارس زیادی رو در کشور راه انداخت!  (باور می‌کنید این یکی از انتقادهاش همین…</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/farahmand_alipour/6628" target="_blank">📅 16:35 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6627">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اینجا بود که نمایندگان شاخص مجلس،  افراد ملی‌گرا،  چهره‌های اصلی در ملی کردن صنعت نفت کسانی که تریبون میدادن به مصدق و  مردم رو جمع می‌کردند  در خیابان‌ها در حمایت از مصدق،  فردی که خودش مسئول خلع ید انگلیس از صنعت نفت بود،  شروع کردند به انتقادهای تند که…</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/farahmand_alipour/6627" target="_blank">📅 16:32 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6626">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/V27WQ51TlatPvYE4CuDd2zTJMj-yMIEifM7cZXoiWdxncAVtyiI8PGDt_j4O7etyFyO8rN_GFSjQeWZH3VUrFJfZrzvnTTOjJlxvON4n5AL3sAFj5JN3CUvJDSI4Kv7UNIr1dH5lmcMuhagLjiU3e0DzWZwMRn6cpBVWuzwzCXIKc4flb2dCO4R4idFMfgYkCwbukgGrhYOs9g7qoTB9u3RsXPlKx6yEnxU1ap6CoeAeGAf1L09-_dndD-2PDr9aw-cC2i1BH-UKUWKq7JtNykLtSP_gmoudFW6dQFs710UuAt-gw3N2SNeMWXu7zb31_75R9QUfUZtGD6BkLd3W9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینکه مصدق با بیان یک جمله پوپولیستی که «مجلس همان جایی است که ملت است»!  در یک جمع چند هزار نفره،  رفت به سمت بستن مجلس!  اقدامی که اساسا نخست وزیر حق این  کار رو نداشت! و فقط شاه در مواقع اضطراری حق چنین کاری رو داشت!  ولی مصدق چی کار کرد؟  مثلا قانون رو…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6626" target="_blank">📅 16:26 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6625">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/G3jz-eqgwmuihZcYdNvSij6XENNIsotI1dGc94F1R85WLcMmA8PPatie9_qtStV0S-SFdaohftOoGEW6E2oGmPzgE6GOF1QLtBdWih0SKeEE5aWwH-ItAl_f4RlVR01hK1vQfLJ0_Q4jOaCe0HfPdcGCTYVz6HLUdNxFb32YYtqnK1ovMBTNN8WUJBa3bjK3EDiAJJc14fByiY8RguiffzodSSvyNzq8Pn7CG6_nfL1EQ-oi42tGfLpWIQ8cnwjAtd9ROhFbgFvxF0yGXg8rly5l1hujWMyg7sBNKZ8fwZF9UenRwFolu_psCvz_QoZF34vSUEaHGQHPgswlPYWfdQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چون پولی در بساط کشور نمونده بود،  مصدق از مجلس خواست که مالیات سنگینی   بر ثروتمندان ببندن و زمین‌های خوانین  و فئودال‌ها رو ازشون بگیرن!  نماینده‌ها مخالف کردن! گفتن کشور خودش در بدبختی و بی پولیه ما این مالیات رو هم ببندیم و با خوانین در هر گوشه کشور هم…</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/farahmand_alipour/6625" target="_blank">📅 16:23 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6624">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gOAMJSSykNhakoxjLtEt662SHaYjmPwm8djxrKYF8tY4mlTTogOWFI-YFvqajtF5QR3AtPWXfpHsc-0_qo2Hw8SAtY6cFZnWVjGgBVP0dyYyntST-COwhJvQ-gRplqyQB_9vVfgPE7HKZbrliSSGim5ylao-GtJXGhqd9e8d9qbAtKq8ItCHRBLwUacNQYzlKg5n1p1yHSJtyQlEaqbngrCiE6ndgRnUkI9F9nfbckbTStN6RL30F6j35PqLvn3uQP-flvY6SY4mFzwNZ8llsrm1SFybpkX7vxARIyvji03pItXdHpZp9pjRpHossqsrHto64blvzy2BlykQrT87jA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اینها رفتند نفت رو ملی اعلام کردند  ولی فهمیدن نمی‌تونن نفت بفروشن!  چون نفت نمی‌تونستن بفروشن، پولی براشون نمونده بود! وارداتی انجام نمیشد!  کشور دچار قحطی شده  و گرانی و تورم شدید!  حالا مصدق رفته بود و از مجلس درخواست‌هایی میداد از جمله اینکه  وزارت جنگ…</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/farahmand_alipour/6624" target="_blank">📅 16:18 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6623">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TOrecV7Tpuq9892llCz4YQ5yN6TyvBq6IEUYwxG5inY8Zw39Vhka9T-QAQkeUhfVffsH7SHA161CLkffBPkrXRA3mZkwgWrW8xHAMmA8e4uSKidybPYEAIIYaFmIMlJf90_eYyZMiJod3g2daY_OqFImNwErzlmB2RquwZO8DkkxkTgAcs2yR3jhTRekDXbTwwQvV31YiAGBL1Yd3QI5ImN8Jq8q2E43q9h72P4ZpYycXbXfZUTNsaFUg6Qe5fYcb94W5d4vRqCG0PmZL5LtbICV1kk9qGTD1nll2MotKhSZZ0qFacMs2B4nnQYugcgHAW8hdyB44m6X28plnFMDGQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مصدق به عنوان نخست وزیر اساسا  حق نداشت مجلس رو منحل اعلام کنه!  بر اساس قانون مشروطه،  این حق فقط و فقط برای مواقع اضطراری بر عهده شاه بود!  اما مصدق چون درخواست‌هایی از مجلس داشت و همین یاران خودش علیه این درخواست‌ها ایستادگی کردند،  در یک اقدام کاملا غیرقانونی…</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/farahmand_alipour/6623" target="_blank">📅 16:15 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6622">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KNFYsgonfGXDlY1bnZU-JONhSEqabBpJcwIcTbg4mQpFexr1yhtioOagnDDCkOl2GrkLa5xCf78YHuSn2j5AZWn3jIo8rMukU-jrBoZO_LI5MRMZjmHOFW02os0hqmSG4Yj_HEzmwFTti89eJ9WBmp1B6t48ducdO0iAT0L5wJ4iJmWlKj32gvgZfzn2JMGBYY2yMaJd3dFewfzzRVcz3nxKEfoZl76DcLNq7waeXj2pAbblk1iDDXcsQjBfIcYBqmqiyYX7awRXQk9zPkBYavX67nqUH-3MioYXbBqSG5IYPD14nbNQ7Di3GPfiLzAiJQ7iLf-lmuiZpowJ1y7IUw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این سه فرد که نام بردم  و چهره‌های اصلی حامی مصدق بودند  و نمایندگان بسیار شاخص مجالس مختلف،  نسبت به این نحو از برگزاری انتخابات اعتراض چندانی نکردند!  مثلا مصلحت بود برای حمایت از دولت مصدق!  مصدق به روشنی برای اینکه نمایندگان  حامی شاه وارد مجلس نشن،  انتخابات…</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/farahmand_alipour/6622" target="_blank">📅 16:09 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6621">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/TeyjZcNmGU0_8U0JO1Ns_PQg34TQOdo32ZnZnZccXT5cKrIv5j35RdfLMWU_zpISqLFyffbIJjKuHM2WnuVT6PZciS7mrQViWoljGDYXsxML3mU7KATr_FNH6az87a-xax0gVqpebEyGu9dk2bOoekybwjWgINgH3z9Ej8NFjyV2RGbi-Fcl7vCZsAxh-5smbs3p-xIYHnENWLNrOXDVm5v4eTX6nmBO1flafQKp5VPeSxL_Kgc3LkrDPP1EA7nl3G0ZXANTSHPuZQG4tUsYjGYl7RErOe_lnw2t_EC00iHJBEiOn-ve4qfz5ios14XvrIQF8eq0I06pRn_HhYsPYg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">انتخابات مجلس ١٧ ام رو چه دولتى برگزار كرد؟ دولت مصدق! ولى همينكه اسم ٨٠ نماينده مشخص شد، مصدق دستور داد انتخابات متوقف بشه!  گفت براى حد نصاب جلسات وراى گیری ٨٠ نماينده كافى است! قاعدتا بايد ١٣٨ نماينده به مجلس میرفتند! خيلى از شهرهاى ايران، در اين مجلس نماينده…</div>
<div class="tg-footer">👁️ 14.4K · <a href="https://t.me/farahmand_alipour/6621" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6620">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/twg_8XGmdkSWEwk5ME3JvsOOmMicJJ349_h5L9oPK-8PZFoLRPbFzWyuB6P_UiIn4QXkZZQODYvENSPmkOl558isaGGs1-8lN0ORh-24Bb8wnkI6liKS0WPmxtHYRJPETz8iwtlGMYAAnkIRyn4TCR5GzH24bfrP3vbMGq1gqSmAfGxpGNpQ_ERnQ-pI9fiPStC41UYbxl3kSlC4fUBNF3n26AwpBuR1OgaSEWuZb4mb85ne-nKtYiZ7pyfyP7cGYqXodqqECSg1WShFfQuSWkF71NHjgCWqhvxxp6vylP3y-GW6iyfJcvnDO7JBHTVjKdqYdRWo8KkitSJ1gJQz0g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">چرا ملی‌گراها، چرا نزدیکترین حامیان مصدق و شاخص‌ترین چهره‌ها در ملی شدن  صنعت نقد، علیه او شدند و از «استبداد»  و «دیکتاتوری» گفتند؟  خیلی کوتاه خدمتتون توضیح میدم!  با این یادآوری که این‌ نوشته کوتاه  در مورد بقیه حامیان مصدق که تبدیل  به مخالفین مصدق شدند…</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/farahmand_alipour/6620" target="_blank">📅 16:04 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6619">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/toRJR3lJroFUVHVyj_gIzHziUoy6oRTRinObdCr5nqCYUqTdUAqyqYuPO6RvumuXkg_S6jtGepmrMo4IotUg8ZJk1VISYfyWQyUp6Gbd1-Tfk1uSrhGP1kR1mgyg9yiODtxgzKhFAN1XtLmTj58t64Tf_VQovfNnxJ3EkgAiNny4zW0Gq5VOIIdA7Rvnde1LJrvDe5vKW91OdbjN0oOdUa4Jwp1gHp__86HI61gIaB1emCzVzBFS8cvqgSZNjsvm_z82xvUsb8_K7nj3-90SnaCOgbAy8ecSZ1c3G2fKIJh9lsdgi3jOFavRGeTIJxoa-VK_jkghbC7jhtCoYoLh8g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حائری زاده در سمت چپ مصدق  حسین مکی، مظفر بقایی دو چهره ملی و شاخص در ملی کردن [ناکام] صنعت نفت، تنها افراد شاخصی نبودند که علیه مصدق شدند بسیاری‌ها بودند! از جمله «حائری زاده»  نماینده شاخص مجلس،  از حامیان معروف مصدق که علیه او‌ شد و مصدق را رسما متهم کرد…</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/farahmand_alipour/6619" target="_blank">📅 15:51 · 28 Mordad 1405</a></div>
</div>

<div class="tg-post" id="msg-6618">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Oxm2nmjAZYFORrv-0N7Wbf71Lg7aSd560w9MzsugFu6caixxsLwEZduxgfydvtNQoAD2fQ6YXlX9Dzu3VWdOTaqhbqQlLDYcQMFbGJO4Lm8AjB2QYXQOrfaCbc1NVv323v0i-U4drnKbjlaCq9M4kIS2LDNhoj370eFXXCyY2QETMcmzXNcklSCMcBuDdvByuBMsKWhSn0lxKq8E1JohkGg07Md7S0p8UVlIPn0Y5CtVfVLbjROeT7T8YjjScxdZOTD6QIlZOluqmZggqIJQ_c9XOqeNYuxkGMPTdFcXQfzpeCmHbXXMLGa8FAxita4sE1kbo4t5vMZaP3_XNTEMvQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">نه فقط «حسین مکی» که «مظفر بقایی» دیگر چهره ملی شاخص آن زمان،  همان فردی که تظاهرات‌های مردمی به سود  مصدق را در خیابان‌ها صورت میداد،  همان کسی که روزنامه‌اش (شاهد) مهم‌ترین  تریبون  مصدق و مصدقی‌ها بود،  همان نفردی که نیروی فشار و چانه‌ زنی در خیابان‌های…</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/farahmand_alipour/6618" target="_blank">📅 15:48 · 28 Mordad 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
