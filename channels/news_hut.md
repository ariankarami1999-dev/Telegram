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
<img src="https://cdn4.telesco.pe/file/Z29MtDzD8kuVCuJ3wbN2RoolRIKGskGCZj8Ozjv9soqkW7eQTKkPEtj3G4r5i_rhUMHNL0Quz-gB5vRP2CG3eHoLIaLgFeLAMOisJzoucDBA2Y_KQKr9vaKKYF4IrXWN9HIEn3EVBhhbKh9QJ5DzhG2fr40VNv3ghKi020_B_2Ysl0SX11ngWVn0_j8dEejfC9u5PeHj_Q2GPXx36J3nY8W5An0KLRUtuTgdtPBh4Z1i4Rs76B0uI0JpSfbKpdgQ-jB2HfX7c4iQruq03uMe3fujVmsBb8R6BOoDZnB-BY7iMyNfPXp_gEPOw58hsB-MyQKCBpRAHqTzmOBqpBQR_A.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 هات نیوز | HotNews</h1>
<p>@news_hut • 👥 213K عضو</p>
<a href="https://t.me/news_hut" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 بدون هیچگونه گرایش و تمایلات سیاسی، همیشه سمت حقیقت و مردم.</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-12 00:38:49</div>
<hr>

<div class="tg-post" id="msg-67214">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">‼️
لحظه ورود تابوت علی خامنه ای به مراسم ، امشب در حسینیه امام خمینی
@News_Hut</div>
<div class="tg-footer">👁️ 2.79K · <a href="https://t.me/news_hut/67214" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67213">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aOuMgUcNhEA2vQq2LfW_K5o9h8H3Nz3Liv7rmjnyDYkSSA6sN6qsT4bKhGyUKHyV5w0du8_I1_Qphs50pfSLDim7jnATibj3nSHD35aNnqZoWRohesqFlgGKwBCRkDXIXHJSa8CsmBwAIaCG2He1CiFhfOylU4IL4uJ4WkYSMET6pTX3F9sFMft50r80ADushpFG86zQs87fQMXFb_Xz21yjsvZusTrV23ZC4mTH6A_y3qGUEeSrXizc-85ErXHU5mRkwt470so76IOxg-bOLD_nwIIlMRo8G2wTcGDbQozsvRJgj6fwk6hD2fmxcFvi3HIdozi7fqyZlF2qo8q8OA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
محمود احمدی‌نژاد بعد از ۴ ماه سکوت امروز درگذشت علی خامنه‌ای رو تسلیت گفت.
@News_Hut</div>
<div class="tg-footer">👁️ 2.78K · <a href="https://t.me/news_hut/67213" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67212">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Vuz0732779nWRs8b2cUuUDWdgS68-oCsUm06cdpwdqBuH2J-k9_sQ248bptz3ss0XZ3qS8ubrSUIU5xQlCV08czd1XAV22JhOH-svqCjDXZ5yEa6PwMj9GPifGIPgCnMy-lPN7ctKHHhirdZ87iaCEl5XnaXvcF6WICObR3uqp_6oBTGzUoVEU8-N66KQ6gjLMyWVneznkxfriPOHHcPvTjPlGNy1klCuA2TdyawvqLjAnXOU_qO4Cgw1XoaHuatHYNpa1b0wwzjPzWBfrslzsqaNYcIleeQD-jSm2XMAI-dBNQmdiMttIkWR3KoZyGXxFxM5XF63yUrZyRGTjXIgw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">📈
رشد همزمان انس جهانی و قیمت طلا در ایران
📊
همزمان با عبور انس جهانی طلا از محدوده
۴۱۰۰ دلار
، قیمت طلا در بازار ایران هم به مرز
۱۷.۵ میلیون تومان
نزدیک شد.
🌐
مشاهده قیمت معاملاتی طلا در میلی</div>
<div class="tg-footer">👁️ 2.48K · <a href="https://t.me/news_hut/67212" target="_blank">📅 00:31 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67211">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bTQzLW12fcu_3tWKsVQa9HXzX4CchRGQgUhEbfiwPqosOD18R-ABbvvfcNGM6qdBnepHXhIOCA-cf2BoFQYckPz74Mf46InfqMX7rheGDqhJ-EI6LGpf-AfEkNhLWxiykNH98GdxdM5o1PygHzLNho2UjvgEt-Y9bqDpAcntAqws4-UdlxUSVmUhGbrTv4PjRdDH2sku22gNBAdWU6ljetXtXEa_kh0hPpCtBgIM8DofPpZlJi1nuzst-tFa1f8PuWGsEgb7VzNRJAC_4_Qyn1aPiPWdS3uh4jpkYMZxdpjNKBWUSc2pufo2qyvVdSQHCe5aZ6FEciqTBL-06Ep4-A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">تصورم از دیدار ترامپ و مجتبی خامنه ای
😂
@News_Hut</div>
<div class="tg-footer">👁️ 6.49K · <a href="https://t.me/news_hut/67211" target="_blank">📅 00:04 · 12 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67210">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1459d85069.mp4?token=Vx7Ox0ATL_ohIBFGL0C7tds3AFQdRLA76HuLybJgEmBDtLwY5u3CrFZNkwTQGUa58Kqv6l5Z9v7OyrG4I1harluDaPXSoEXY5Bdan_zL5Rc5ehUcI_Hr9r2APGHi20Bq-a7U2VCXZU0a25MrA0lcHDU8qlzkXwEjUj8lxTxex1x6WzhQRSQDrpIB1I31C2ufJbmI3ZkJqiL2NrQ2al3_Z-OLC2PGPmyNNrt2xIWqB8qycfRGiYodotQY-O_UtE_FfEUIPF_Mucf2lICGdjZEFjBsVwj1slOqaAo-rib3ckyoV28xvzW5R8lh43hRHepSquUMvjnn6EUryGbKb9dFXw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه شبکه ۱۴ اسرائیل با جاسوسان اسرائیلی شاغل در سپاه :
در برنامه ای که الان تیزرش پخش شده و میبینید شبکه ۱۴ اسرائیل با چند نفر از جاسوس‌های خودش که در سپاه مشغول فروش اسناد و اطلاعات بودند مصاحبه‌ای کرده.
@News_Hut</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/news_hut/67210" target="_blank">📅 23:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67208">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/IMd6PvIQtfL95x9JoCWpAxXEkyBUaPtU1jPdhIMcGj3ZEwSTS7MwwsgYR5slKPC8GImtfwSXedf5Pu9SwP4lSXw_AI-V82fpV5zrSywt9D6V4gTblnqgIyn45ldxQWBk93VMFR9yl1itvIqKL059EHXRnhPvJGi3umD89wYe2oXe5C6TEvEq0x4ajj8deUVB5TEOoL5RQXLSz88g_XSJJXZaT-EdeGJe3jOk7qHcwB4MkPlVnBwsoJNKrvu_cwJpIyfK4udfmRjCTELoAXoiETPGOHR9s7GB9dhQ8s3CNQox7Gkt5SksilDg93B6v93Z8oPyqj94r042MbNKKoH_Ug.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/1f3d132bde.mp4?token=mmxpEd8sqrpOwFLalpUic4M86VXUFzUYxuFzxVgS2cToRDkczRAmpRxOVv-HiIP3cpdgEns8b89FH8zwDur3tR8GVDRQn-IAv8K6JhTgkeS_-ZdUfBCU8XFZRuBkjAN8g_cN-zTBXfiQ-qX86FVlzLPqJJwokjYaJmTGC0uXbD9Fua9M7OoxovJQ5c2Bilo200RNELiRqzaamt-sGV7F2Nr7Bb5mvoX-DyyCXF55YATWpg41W_KvRSHB46W0PP7GbWhXqZPJuvN4ocRHk6CFM28TbQLvzMxh3rXKbeS9DyCJ2LcWS8vc7VEEuO6sjC3WRLKGpULV3rKROYQHwItGVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
امروز ۱۱ تیر ماه، تولد جاویدنام سارینا اسماعیل‌ زاده هست.
سارینا اگه زنده بود امروز ۲۰ ساله میشد.
تولدت تو آسمونا مبارک
🖤
@News_Hut</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/news_hut/67208" target="_blank">📅 23:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67207">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fJk9GvyJW3OQ8I8WfukEvnqBEO6CcLIG4Mn17c7HD79QR50iLZhv7Lu8GHplNWSuHtnXskj93wexuVzIg4Oak8WSuGj8Vxg-DBrYdIMJD0in0VPGEpG1H1pZzHOaajtq8ZtAGMSY3CDirhDujALce6KEGJXeQ7u_2GX214n-Z6B8NhTjFxpcEM1ETlLHTPjzmos11pFWYAK0wDLTE7BJNtf1Vj4QQC1djg8XgYkdpYIAA7XoXyrUr2X9MmPNIcNVajs6YFwP453Cu1Svi54OdmpHhKof36v94YjotzLBoiuIsDEQivJMYbpEW0arxXDm4wX-YHQJ5pJtwF1OSxCcCg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
رسایی:
طرحی جدید و فوری برای قطع اینترنت بین المللی بدلیل حفظ جان رهبر و فرماندهان در جز اولین اولویت های مجلس قرار خواهد گرفت.
@News_Hut</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/news_hut/67207" target="_blank">📅 22:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67206">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fb76f1aa0b.mp4?token=BLnDLM7iYokZ0G-vbEnQJvCIFyFwThRghtwx_ifl8pcCKdhpOS8x5yIMQQtC4taBtwrplzLq40LVOcqlax6w3yPFt2bMDnrc7BDA8OfXJe6osD-pNzxx2kLr6duNvcbEfizctxrr7wUJ3EatcZpd937BIuB2Ns93ZEp6vkFLRb1sZmr6-zZa7r8NThG0mBavGIg9WJqBcLGLbtzzBVvXKjwWLmfeVAciJzUPs2uvSa7Zg-wvHJyjUGNQJ4ug5H0mI4SZ3n89czpbScKTNEbD2ukK6Bvh0Zwro0hRvzGrzEfifFAI-tI9aGBVtZHdEHDJ7cGyHldmh_iNikE2L5b-_A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جایزه یک مداح برای کشتن ترامپ و نتانیاهو
100 کیلو طلا
@News_Hut</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/news_hut/67206" target="_blank">📅 21:41 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67205">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/EVUfbS1-hRgUAA1U09dOnUIDCUQ9rEbCDlM2Z-VbJBDgN5Ilzny4dMlB0fQRKinANxP5kCWSnd3ipts8RtDQoY3JBXXPHLFda-fXdaxysXFcHMQVYg2gWT2Dht6Q_G8nAWVxgnPEsees5ub_v2e1i5Impm2_9rNbapjeDQFyACWHSOMGe_DBNjfyQA_qGaFQUEdpjx18urRITLmng53Mku8WVYuBAGJRAXzTMZTAiHXcAzpV2UUJX8xSEqaOGmRsZho8gz6w6LOfH8VF2gmqwQR2EdZ92V5VgPbdYzZVo5SMUEvJjtS8tqhljfWecRAnVsT8Kfcc9HKln-Z29LKeFQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
بر اساس داده‌های مؤسسه کپلر، روز گذشته در مجموع ۳۸ کشتی از تنگه هرمز عبور کرده‌اند. از این تعداد، دست‌کم ۷ کشتی در مسیر بنادر تحت کنترل رژیم جمهوری اسلامی و ۱۶ کشتی در مسیر عمان ثبت شده‌اند.
@News_Hut</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/news_hut/67205" target="_blank">📅 21:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67204">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PqK9xctnlVvPpnVbj5vOwRXurYw4pbleRflAbvDL0BxJadcqcI8CjQOiN4aA83loOTbsHbjEOCCrqpcE8IzaeOiJNdp-ifhNF86kimZKW-g-kifKaCpWamM-LapfBPY1qPK30y1U4jDl-LFgy2i-QBdMB55_Aq65fEzmB439HtzQAyLk8E8Y2G-JPzSHbWE6qbKjXlOAsBSIAojmFZWxcYxZYiVL5TYakQndZRZsOj5frVjug31kGx4xGNP_SuMPBa2CUgjY-6_JsFuEDaEyJWa_C0M8ll_PN_AFGRubL6a7-UAtzCHg5tVSp1XBoJ4Q8ybeOHZ4IGvP9G-uDutXZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
احمد وحیدی فرمانده کل سپاه پاسداران برای اولین بار بعد از آتش‌بس رویت شد.
@News_Hut</div>
<div class="tg-footer">👁️ 15K · <a href="https://t.me/news_hut/67204" target="_blank">📅 20:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67203">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/KjNho7JFd3r8kzA4IJUMJ62KFadGMiVLl2N2RQUiz9KOFfjeRKuDuAbIeJHCbDH_yup50ptX6xPvu7G7Kkk4P6cOGvKPIzS3WmbsTGFztL1hKcubppU6D2_RYJSFV0p1ozFdQiLr-8mXXFWtQVMMEGRRDhZaUtwlcqyJ9oPOmhZnal1wW-ojPLSyKyR_YKX6ChiKhL3h-VJjK5CvPy5ZsbYQYaESavMrsFD0bSAbCcPKaWp20MAQ3vxOMJzf587721AYNkkRmi3gw5JoWuJG0mLDOqCDHAQJrwA6wFw_a73fHtZA7bbUdCRN879WiXgmbZAekipWktep3sb8m5aSRQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
نبویان بعد از گفتگو دوستانه با ممدباقر:
دوقطبی جنگ‌طلب و صلح‌طلب ممنوع.
کسی در کشور مخالف مذاکره برای پایان جنگ نیست.
اما تحقق اهداف دشمن در مذاکره در حالی که نتوانست به آن اهداف در جنگ برسد، قطعا خسارت محض است.
@News_Hut</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67203" target="_blank">📅 20:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67202">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/vMuVB-8aYZWdmmtfl53F9taUrzrq4PCcWd0lYeAmSOfXVcopGPSo4K2P2p4lYWgWF93k1DLnykC8-SCSGhXqshJRUr8QIx6qBCgESVWoY28VsXAcTiAO9o-jh4szirza1fTPH15WIthedVhONyamvySvMCLIndKMRqfi1f_Fg3Gqlm2mxlF_WwhlkQkCFFOEej1tDWJSQPs1VXNBMAyk1gk1FWJ9iEQ_n6I5FZWMjPgiw3dEIM5fxzROGslmjUApkUFwwhU3G6SfV6L4dzvaMAkfz2-M90aZnroJj1-6grArvuKp4RQJxnJwORxVIM4NCjrdTslklYOO4bc07cXKeg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
باراک راوید:ویتکاف و کوشنر تلاش کردند این پیام را به طرف ایرانی برسانند که اصرار آن‌ها بر دریافت حق عبور در تنگه هرمز می‌تواند توافق احتمالی میان آمریکا و ایران را به شکست بکشاند؛ توافقی که در نهایت برای ایران بسیار سودآورتر خواهد بود.
یک مقام ارشد آمریکایی گفت: «پیام ما به ایران این بود: "بزرگ فکر کنید."»  به گفته این مقام، درآمدی که ایران می‌تواند از طریق توسعه و فروش آزادانه نفت و سایر منابع — در صورت لغو تمامی تحریم‌ها توسط آمریکا به عنوان بخشی از یک توافق — کسب کند، «برای آن‌ها صدها برابر ارزشمندتر از توسل به روش‌های باج‌گیرانه برای دریافت حق عبور خواهد بود.»
@News_Hut</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/news_hut/67202" target="_blank">📅 19:43 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67201">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WwIQveqeG1Hc_7YajuUyMYssWCsnuqcVv5IkF8p39qrQXZrke3cOrWsnfjwcMMie6YGj_L4KxB6BeYKr6HACHokWst4fA8le7Z1CmVTa1Zi-volX84JIwga1rk9oo4QvsMCXAOdAyJJw_dsadGt81TqC3VE-iSnoV2QZVDiuY6QOh9BsIJcVZ7pKs82d_9zgqNFBxe2fUE0gXJdl0X6t5s3k1BaHrWgajfb9VlHHvuUuxa3DmCaiAYCedLGDIEjh4xsLCsgl8KRiQjljOUT8KBe5PFLvJsjC9bvjmrGxzMwySIwNOVbHNh6tqMPZOS6Z5wUh3UuOQjsVDIgki48IXw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
لارا لومر، فعال سیاسی آمریکایی خواستار بمباران تشییع جنازه علی خامنه‌ای توسط ارتش اسرائیل شد
@News_Hut</div>
<div class="tg-footer">👁️ 16K · <a href="https://t.me/news_hut/67201" target="_blank">📅 19:07 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67200">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8af16d4917.mp4?token=nKHqSo7U5wdMvElN0G4O45aPWh93xvoe7zo3HEZzJfrvAJo__opdPXeafZASIrMt_0WgLgGwqWJuFdEc_q-k1hixkbUt-ZDlTrmvf1cKQ_SafV4UKE2tbl3J-_JfyFmhnK7nuiYqqVfDRPhbWvEKZ0Kn1hC3Id2_ynD-F8Cyu1CgWzey5gftAoQUJr9Tx0WN-oPmbAwJW42OspWuDeQwq5d4lxTBjVAS7_5uWwbSchj4DAJTdRkdUzUEztfxuPx_jlWMZ-QmW91UBNxhV8uoMylGKQN0F9uM8VerPqCyo1rLbBthPaoBQKoMOGu4GaILdPJncsmV3ZIwCNWeEbjEpQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
کارشناس شبکه افق، به قالیباف:
این مسیر به جایی نمی‌رسه، حالا دیگه خود دانید.
@News_Hut</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/news_hut/67200" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67198">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/67ae57b0be.mp4?token=rt0NUHGLv8I0re6r7OQMmfw9lTLl7_mkr1JOC7T-vrzuOSpVvHGvh2GOMny0LauQdbaT-IhfSLCHPi5viBgR7defWenSc9du9lm4TWVmqrA76j6sWMLkdpLACs97JBUqQB0S7bxue-JfbG2RWdKAIAhzDw_BHvJJ3DzVmPfXL9fd_F2_Twp0iv4TKvOsUO2t2bJlFr1WCVBdq7vlMzUw7jEsBLPp1PJ6s0mfwS8hDC_uJC3FrMr3H5YBFpAa3R4iFQPbn1IinAKpsnZjyOJ2KFnGcf6PWKsBZDEOdinsG_c0Zn7RtCmQEs49CFAKQegTN80xG-16jdLuAooRBWlOmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک پهپاد روسی اوایل امروز به یک سالن شنا در زاپوریژژیا در جنوب شرقی اوکراین حمله کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/news_hut/67198" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67197">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 با توجه به مذاکرات دولت پزشکیان، قالیباف و عراقچی با کسانی که آنها را قاتلان رهبر و متجاوزان به میهن می‌دانید، آیا به نظر شما این آقایان حق شرکت در مراسم تشییع پیکر مطهر رهبر شهید را دارند؟</h4>
<ul>
<li>✓ بله، باید شرکت کنند</li>
<li>✓ خیر، نباید شرکت کنند</li>
<li>✓ نظری ندارم</li>
</ul>
</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/news_hut/67197" target="_blank">📅 18:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67196">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/f9db45e91a.mp4?token=Gzmt4xOIlxonsa4r9jH5c5bhbN5EqPpnD1_q-kbGT7wFk4wVIUu94LUpjSPJ_jKZ11mpEOcjAcRZYp5SL-znPT1ceE625rkSksYGhl3tBXF9626VJpxyGK6VKIllUhQfqF4fuQXIia58bOWtLsngDQY_qufnue7MAJGVBbl82-nVlBsuqLZBGiZ3k61cqX6asZYHDHeAF-fCWGxH8DoVWD2zEEFCDl3c2AuGi9pv5AafpodvIecztbsF0ycqlyzl8xRwDr571Z-lr6WFTXBflpp-x_niXiI-6hSrod8lrrzGq11LTJnfUt4Vcf7QudSgyfIQNrTlr_TW0uvXHKw11A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
در جریان تجمعات شبانه صیغه یابی راه انداختن و یه نفر یه دخترو به مدت یک ماه صیغه کرد!
@News_Hut</div>
<div class="tg-footer">👁️ 16.9K · <a href="https://t.me/news_hut/67196" target="_blank">📅 17:38 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67192">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AnhCD1ih_b0XXLpvBDIAZnB4fDiC5H8SeARPt5sTfjdSnyjh7c8SvaS22amE14lYKRALdiB1LUyndlGc7EIoSdodyk-Ix0JYYpNSTu2ESI-dyxzrG0qyzYLicA-oCr0CC2xCJ_4kEMn-oZIlH_rHa6SziBupIydZLbCPDGrTxq9e0npmBMyC-7bwNsDitoSKjVyF4qh3rNn4wd5sck8u5MRal18jsX20GRJij1ZXaYSXY4d2R4wqI2Qws0-PoAm6gdomI-mkgiGmVz2gCk-hCZaUiWFNBB9d4JBTsrXSTAVvsugLS0NYl_CdD4VS8tQuUzsNkAIL5fsjpqvLJVSu5g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/QqTkhnTZ41JnmVdIDMm5Y45F1mYe3vtoy7AaKuh7n_JVqeJ7iEUHMEvfLeD__GXNy7ulBHagzDoRqtRbWH_z2cN6XYbGJF-h0Eib26G4Z4lVYKYvMHOb4rdT6weZwNiN82AjruA_anoP9PTaKJAOmBQ5OAAop6liPSFC_hmKca35FpH7fq-m4STugYe7dMhxsOheTV4_tQaXnxiUJmsj9kcQHkVVnq8_o_iwrFXiVf_lbBxwY-6d1ILamDKKChAIBpfMkP6WN--Zeofe6qDsqWVnBaeUnlB1teM_2JP2xevHBpRe-LDIT1QGv_H7Sif_eYUNPMn-Ig_8ZQ8Ot6XNWA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/oUSPj4vuyhkxsW-C7YOxTIkqqMTxNracE_iHXbUY6kd0bM1Ml0qVRD8ekCVyROl6OsrG45gJFCwbRUTGXMUClNgTs2ILMYPjqP4g-Y70JOiZ8sDOJPfGoeUCP76Xa46oFxdEfEyq3rdWWMPX9wA4NgTlYvDMwJtTQh2snM9mwmiB6_TJWX6vf9pjqNIQZzV3CVdL7xarFz4BmX-0huY0lEH7RAHoiK6u3uu8yPkEzitgBUjeeOc7sbwARb60WcV-oYSwHCkKAHzh86SI7cCWmRdKakXOuKGsEmLEasapscfBmUvgnhE_hG19aZ9Fav0VpRKYtFN_F6Y--3aNb7rp8g.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/543c505f1c.mp4?token=Pt9pv8uvn9x4qAHmPdMCt0p5x_h-mVk_zwSNyT16xjXRkCewNzEdJ6D9Ny6IZjczopqmqtFonUiI_KFwqe7IFynHRXBuAAf4D1bd9f-AXji_FuuTF5CX3kRq1q-Z9Dv8LO436JkZ54m-jqA9vOrIb8WBeaBCOWzj00OPlxLEGw0NWk9bw6LcKEpbMeBJAo0Lxzs0CcssO5so-flZ5zLahLHWraqr_0TOdNvQ9fvrA0jBz5A4GWG9UCR9HhVyCVxiTA_FQKJD4Md_yFgjdO-IH5i2dVJYlh8vw_iK5GQ2g86nAIx0x1Zb_weaRCVSMVOQ_SPoKqZziBmUcnNJ0k0SNA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
دیروز این دوتا زوج تو نیویورک رفته بودن بالای یک برج ۴۴۰ متری، که یهو پسره ازش خواستگاری کرد
@News_Hut</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/news_hut/67192" target="_blank">📅 17:04 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67191">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/afce812fcb.mp4?token=oAFdhcQR-W6EoxvYh6HHto7yMn6iaO35qobyu_qUA7onTOvslggprGLIXFdzrUhdZj_irVHIH7irFB3hRLYmV2MIWv5B3nI9S2RTg4Z5asEAX2gXuYw71nw6dxykIX7o9fhYsw-Crt3XbEqtv6mAfSWS0XKfhQT6mKXzQawpt3kuJPdwomIJfXL8dOwAuFUCQDSzvNPoYHfGzKq8lovY69fVXQGCPUpO-0CIEJF2KJp_UIYHDo39H5C02aG8MvDkQ49r916BfFXJ0lMBIPt7leCblmhvPm84IGCAxhAdOTIVe1pT6_kRHh6db9zNlZ201LWystgfVMitglii2PEtIg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پست جدید ترامپ:
ترامپ پزشک می‌شود و بیماران مبتلا به «سندرم اختلال ترامپ» را درمان می‌کند
🚬
@News_Hut</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/news_hut/67191" target="_blank">📅 16:36 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67190">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2cadc1a3fe.mp4?token=Kl9HAPEDGqhINFhq4GTfEtJo7k21SaGHgFWQ6k93-HPNrKpWp_vG4tRaIsrHsAOpRBxN3jzbAei2q9y2C29L-dmb8skIVgQWjP5TnkR8Vi-xznKbem1o5b-7nWRqi5nZ8A5SSxkdB27HfM3gYptLGUTpY8e2M-TBjmb8HqftJmJNy3xC8WC8v47qTX7kM4j7aTyjFtcmRYDC5OCtJj0kBwI-x_MBXRaxhTCP8EDeaAdN2-Aa7xwezvXEOgWoA_yQGyRCeJVvgLbovsXtKTsn28iddpCE-FMurtxm4kRc6Y2lqEmKwzzxe5HT_ZWJ9Vzxld_lJjqrTcbtd_jOsAi6tg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">این چیه دیگه
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67190" target="_blank">📅 16:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67189">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dcf57c8dbd.mp4?token=pIv9bjCEaqNjU2Bv6mAd9tiWNGfh2XbasiwmrfBWBT0og7PkLLLfYy2Exq7I9DOGQFBbSFpX-GFkMArsfad-EA0tKVHAJw1-R5t-4yDeQGICHQH0yaQvihRbIPiwTcvqFxZxLfKJ8A6EDPaOixzuSVa_LB8n8JuTqpRowx0xxRYXz3nWnxms882Ms_625QfNYLuerOeyLzO37orpCwjof6UZZJCI_Yw7bc0Dto9wDx8o59IQIOSsdfP6GiJX9c3_SCyaL0MB_uCdd2kn07Slqim8uNJJY7AUvX1eq8JeKz2UTqvOYnXNTtf1XmRwetkozjX4vUA-iiZgiV1EcMQI7Ba0ePa7KuJwXpwqpjjtNEDt2zkzAeNwkEA62GYpR2PmZsI8Yq4lYgIGBH-OAPFJI9PESkt4PqBzPWLsTiAKR1Ob7M2FOq9TKMMFkJr-tO3tX7j3AIND_svuIF_ay7RwAkpFUu6LyvRu687qwyH3yf0DTGbfda1kY0E3OCZyQjbjKzneWIJZdLulNvTxBFEdlLmu2UUaOBr0MFIglaT4bBViboUiZrb2Nm4EvviPuOR2i3T45eNd83BjaVIHavcAz3bnvrYEDKeovw8X7E_TJzF-uklbtTNf06w7xxZ-RDQUYzag50qGGVdjY1kVvZ1v3bksBR7HIBTMvCfHB1ELcRM" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⏺
صحبت های جنجالی
غضنفری، نماینده مجلس جمهوری اسلامی:
عده‌ای میخوان تجمعات شبانه رو جمع کنن. دارن علیه مجتبی خامنه‌ای کودتا میکنن. دارن هزینه‌های سنگینی میکنن و به مداحان و سخنران ها پول دادن تا دیگه تو تجمعات شبانه نیان.
به بسیج نامه زدن که دیگه تو تجمعات شرکت نکنید. مجلس رو هم ۴ ماهه تعطیل کردن که نتونن اعتراض کنن.
قالیباف و پزشکیان میخوان کم کم مجتبی خامنه‌ای رو کنار بزارن و خودشون اداره کشور رو به دست بگیرن.
رهبر از مسئولین قطع امید کرده و الان فقط امیدش به مردمه.
@News_Hut</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/news_hut/67189" target="_blank">📅 15:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67188">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1148d0ce1d.mp4?token=qmFo3scwc71wqM2txzBLrcRbJlApWbStz4dNsk4Sac_xaWim3A45Z-XDUpKwBqnDGDup3BQFnpLVuw8VPRPc5rUh2WAQPcRTlDp1ntpjwE90bUyzvB3rSKYqKOoejZmhmN0PHVCKs32ZmMlf-ZuJVwxuvE32_-6CRygHRIgGmbl-gx0tKzOMhMzMi7-wCgoS9XQkxfX97SwOgxl6JRAAfVO1z7oA3NvWDzcejfj3z8psvEbu9_XC5JWkTeMeZXrxMYQEcURJbt_bukRITM5855WnBbm7x9cqAyse2f3_ocW_snQYtcwFCPZzAuqFJyNUHUJNgHJfc7NlIn_23NyelQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
درتجمعات شبانه عرزشی‌ها:
مردها: گندم و جو ارزونیتون
زن‌ها: تنگه، نمیدیم بهتون
😂
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 18K · <a href="https://t.me/news_hut/67188" target="_blank">📅 15:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67187">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/57a2c0f9a4.mp4?token=XWi2iawMMrGQer4FcTB3QCtVPgyavb_MKVio1UF3eH0t1GZT_E6HZeZfSXx0iVzqsp7D-sR3m99aMaEXCIJ88xJ4vNpSXptk9EiKf6pGjm0N3fUGh6p7zvNokdzmzkq5Zx7KEvwuCDp1JJ6o5FXifJLVmS6X3jL_hrZunYSGUJ6J5k78kg8ZtfdzHdHpPLcBUk7u2HD7mtwECTedxrd8vqKdhT_3eDXhqCprj3qmVmBlDuQqI7BR60T0d0XVl1J8n2eYx7Scq8BjPwqnlTjAGm_D5D-VDiEJHvHARjEjPntwjTjfq7tY1PffTNtDi7wTlIboRF9wlu3gcUFBYcFGeg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
رسانه‌های اسرائیل: تصاویر ماهواره‌ای تازه از سایت هسته‌ای اصفهان؛
تصاویر ماهواره‌ای با وضوح بالا شرکت وانتور نشان می‌دهد ورودی‌های اصلی تونل‌ها در سایت هسته‌ای اصفهان، جایی که بر اساس برآوردها بخشی از اورانیوم غنی‌شده رژیم جمهوری اسلامی نگهداری می‌شود، همچنان با خاک پوشانده شده است. این وضعیت نزدیک به یک سال پس از آسیب دیدن این مجموعه در حملات هوایی اسرائیل در عملیات «با شیر» و عملیات آمریکایی «چکش نیمه‌شب» در ژوئن ۲۰۲۵ ادامه دارد. بر اساس این گزارش، جمهوری اسلامی در آغاز سال ۲۰۲۶ به طور عمدی دهانه تونل‌ها را با خاک پر کرده تا آن‌ها را در برابر حملات احتمالی بعدی محافظت کند و ذخایر اورانیوم غنی‌شده را در بخش‌های زیرزمینی پنهان نگه دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67187" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67186">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromMoris News</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/s37eul_rWWdfDrZVmqFUsAh1dKNq9i0Uc_p1JU6Lk7eeTu9gZYoNLvX1AueoUDmEjfJpnWaycW9F29th1WUNxfEKeoBDFwpv6nqEfOv1K8XF8vHVNCJjl-oo0gC_Lk18b5K1rq02xPVL38jywoKLDmdIUfMwzxrycGpIPvumW-s3OjpIc4c5vyYv2-NzfazEh3tzcKPXuIsCjOiRiiqJG-s7guVS75UNAVpQM7MEnBGe-dFwLiS16hSR7JlyIXcU5GlAe9KJ8bKeDvTaaUIFF6eYRJRL419GjaWzdviQ8R6iq-E5I3BDGMVPy9PjJRemIYuifUAkXwGwc7D9IGGLXQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">صفحه جدید یک دوست عزیز و هنرمند که احتیاج به حمایت داره
از دوستان خواهش میکنیم با فالو کردن و شر از این دوستمون حمایت کنید.
@egyptinpersian
در اینستگرام</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/news_hut/67186" target="_blank">📅 14:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67185">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rH5MCve6-VJD_NCcpwXir5hyjGZCFnRqq1l2ORZM0pnyiFrZgg-DMW8V9gRPbWQTtbsu-WBD9zFsMd2RndOnd31yse-hyQczrEHDrb-rodx1_kV-1ztOT2dl_tftsT-Lxl0PA0Ht95sJQFv2we-NmP3nUFpS8Yc-1ScD40A-R9C3imAgdTyjPiIWSNmABMU1GGQh-DOxjUTyTHSKf_FNCiLYzsyeZnihTBIyb6WAChMlr9wwazIGziQ6m05UmEH3K3CZ83wCtIEj-z6O1DHNt2Ijy53cngu3zJDni5REY77KX8wGgK44RKTK923xyjebhXxNt300fN55Hpp6I5oD5Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
العربیه:
دور بعدی مذاکرات ایران و آمریکا ۱۸ ژوئیه برگزار خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 18.4K · <a href="https://t.me/news_hut/67185" target="_blank">📅 14:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67184">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/885b0b0686.mp4?token=KKfe7eVcgOla_x6iMCOAV0ujHj9VCa0SELGh6X0YflXIU3YKv4MtK_7PFuLUDitdTTA_kTu3doiXNOWfqGU_ZR1kW5xNV53_u8juvr4bfacUs5P6xIxJo72HIR6XQqPFIe6R_F5LtWPK0bLPv2WsB_uu_79x_u5SQxYxlmG1iSU6APOvI2hLTON74m0CJQyFJVI6whC9SirlKew3ZfUJTPzHK1QilLfbkqQuB-u-9HmvfYrvnOyNdkryaGNq8WNaTm3AmnlG5vbChdjcaOXzxpPjQEVrXuaz19f3PF_41-352eB1W8BSg5DHcgtWtwUGWIVe6WHO9zONrjysFf1k2Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
پرواز جنگنده های رادار گریز F-35 برفراز ورزشگاه Bay Area سانفرانسیسکو در بازی بوسنی و آمریکا
@News_Hut</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/news_hut/67184" target="_blank">📅 13:56 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67183">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1dd137decc.mp4?token=FBba-p1Iy8UbZzOx0-jL50vBatmkc5pkQQYxpncurVimG6zI_Vepbra0kCEi0drDsEXC4AWVZNo_E05bkJvVQhqjgWoT-GAWkPNV-pPWs7V2PI3qW4xa0yeopODFddWvNsipdmuFhpVGrWuVludjDrtDpYys9qWNuxV4ag6dbaU2sTTRPJpGOLo3iFgYsmJZwbHBWpYKN5Cjec9-o0CpU0-L9DExhKD5QdGL2gaTGbUvUd3CV2WZaqtznTNfpbQPdCln_EgL1c1zPyN8-aMtn_t_cdXJV66aH0WCvH-CMGRp_GR4G3wBfLzwUFgI1R6Tdce3LNjSQNQogAQ2TIXkhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
نتانیاهو:
ما دو بار به ایران وارد شدیم تا خودمان را از نابودی نجات دهیم. در صورت لزوم بار سوم هم این کار را خواهیم کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67183" target="_blank">📅 13:20 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67182">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b216695e17.mp4?token=F6MJMNDu-aOdXrFnseqlYIShJm8wglwDEEtJe9zdciZyQJiB_go7d6Svr-N_urxzu8Xue41GSU3tKFhoU7-sQWqEdTQDjDzq8qOkCg2KPNByqNzXAi1LjVijX1xYzxmqHFX7w8Efy2whX_nJGAT_8TxLkyPR3CfDZe5XwKiB5JDJvcdqhjGcImotmxZcOVT0kediKqFulrXhlOOsitvX4GKG9fgwYnG0k7AmjK3v1BgI4eWqkbt0w_kVerIedU9UFO85VsXlMSDFD2n4u9q52OXj9PvdCSCiudDqidL_1GnisHm6PGOTPgWbM7t6n1dk_A6my_wGd5JJDr_9kWGEow" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
ناموسا این چیه ؟
جدیدا تو تهران یه روش درمان افسردگی به نام "هیپنو‌تراپی" مُد شده که مراجعه‌ کننده رو می‌چسبونن به درخت و میگن گریه کن !
درختی هم چند میلیون می‌گیرن...
@News_Hut</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/news_hut/67182" target="_blank">📅 12:45 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67181">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">🚨
🚨
🚨
قرارگاه مرکزی خاتم الانبیا:
استمرار حضور جنگنده‌های آمریکا، با سرنشین و بدون سرنشین بر فراز تنگه هرمز، باعث ناامنی این آبراه می‌شود و امنیت منطقه را به خطر خواهد انداخت.
جمهوری اسلامی در صیانت از حق حاکمیت خود در تنگه هرمز، از هیچ اقدامی برای درهم‌کوبیدن هرگونه تعدی و تجاوز توسط ارتش آمریکا و حامیان آن دریغ نخواهد کرد
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67181" target="_blank">📅 12:17 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67180">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/r_3qAxJfw6frwUUXVsZ-N_jqwSFNel5JK-E5pFTfOMB8nSQnO6AxpRE1JbQOH3kg42VySShNzWHyWU5CZIEA_PGA_oR5BbI59LxLl2BW4MAaELGE_CmWwhG1hFAGe7IoCcA-UcUQOSO8xDJeNQd09aoV9KnB9zE6EhShRa3NozRrXFQ70-8DnTadpKjwdwCbi8RfsEsY3DAqJLAwGWsUn9AqNgekghFhzxGXvCq_ZSQsiPP0sc8T_KFoMHjd8Mkghi-Maj27MHSq3qVr33A6iZl3vWKd3goNwyO40x2F-xMZNBxYet0uhiyc_mnGchEm-uVpZaCVqGTPce3XE_3cyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‏
🚨
‼️
وزارت خارجه پاکستان: مذاکرات غیرمستقیم ایران و آمریکا در دوحه پایان یافت.
ایران و آمریکا در جریان مذاکرات غیرمستقیم دوحه، ضمن دستیابی به پیشرفت‌هایی در موضوعات مرتبط با تفاهم‌نامه اسلام‌آباد، بر سر ادامه گفت‌وگوها توافق کردند.
زمان برگزاری نشست بعدی در اولین فرصت ممکن پس از برگزاری مراسم تشییع رهبر شهید ایران تعیین خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/news_hut/67180" target="_blank">📅 12:05 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67179">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d167641bf.mp4?token=nGSkGBGkcIi2EoscDpTAuCnGMlrBu6tNIVgNwPYuq-uZBcXwCL7066-nPuOzPV8BVj97_5OqOhKvYIa5bawhOfvZeVQX_65rqqB2aGK0ByDWt9O1VRdiHDXPJA5v7umpQY7h1mhB-lle_rt0ja76vywjmC4zOFdxi7PkALOMRcW163TS6v4M7MeqftuH0s9tPiP6C1Yreepm9Y0Cwzm8Fouyy9CMmEN566lsrLZ2DnBagjEDKjywgsBat7euRFZaQXdF3FlkATt3uuxcqkZUJhSqSIxEjhxcQb8uF1GogoOenLpXoAhaX_txBFUGK0dbd0-bwj0vbTTw584A542iFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🇺🇸
جی‌دی‌ونس،خطاب به هوانوردان نیروی دریایی:
«رئیس‌جمهور ایالات متحده از شما خواست اطمینان حاصل کنید که توان نظامی متعارف ایران را نابود کرده‌ایم، و امروز که اینجا نشسته‌ایم، نیروی دریایی آنها در کف اقیانوس است و هیچ توانایی برای نمایش قدرت ندارند...»
@News_Hut</div>
<div class="tg-footer">👁️ 19.7K · <a href="https://t.me/news_hut/67179" target="_blank">📅 11:32 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67178">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/cc4627802a.mp4?token=k3HwIrf5RfQn0bN06M8CzKSFE9LFCUSSF5JTCpaBiUcnUwmHxD-rwENjg1SQtTeqCtOym-6o7SiwfZyuJatZf9Em1eGt_hoKtiKmTCYEONzz7Da8Q9DAwh3V9UsvlwX6zKGqUcsg1dITSg7jbwbVdQLJntEfuyETPOoD-HyUcAuo6mxTBW-emisWSE1831tephjSJ4jFGSZzefNiZdtsByyk76ySESaFRL23v3fETaPT7bsG7rWzX6Xy35gLwStw9ZDvKvKEVokM_r8NCKxsR1D54vK_GYopKWuyvqP3zOwZfXOM6FtU_T9-ae4z9dSmZK59pHWkr7tFKjzioX1rSA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اشک‌های مهدی تاج پس از کسب قهرمانی در جام جهانی فوتبال 2026
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67178" target="_blank">📅 11:03 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67177">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=Zm8eQJY13deQ1zWjUYpx3I0d7B1zzn31tHYC8p2MoKDmFVpdNDbzs4h8ld_cz3LoNJ_5nyHi-nsyozUtTiV4Bb7fqcGmL-42S5mjjMp5HO1tZmdLVedtDQr3KoKTxwvueMWpzjq4Ko2SBCqoNCeu0Giclxna2pT0f_8ahrQ4Z6D7ie1_bOnI__xhRJMJm7Aycot69jMxWj7RO_ClzOdbnUxuhc2WHMVtYwgKvWUnsAyfJl3t14ox1tARqWBXssj0K7EgexmfzwGGZThIl8E2QBMLQszzaNPA6DgjATW9rnkXvS75-LAxW16T9lorUHyFPTrJHh8HJfvTt0qTlXvcsg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7280fbe763.mp4?token=Zm8eQJY13deQ1zWjUYpx3I0d7B1zzn31tHYC8p2MoKDmFVpdNDbzs4h8ld_cz3LoNJ_5nyHi-nsyozUtTiV4Bb7fqcGmL-42S5mjjMp5HO1tZmdLVedtDQr3KoKTxwvueMWpzjq4Ko2SBCqoNCeu0Giclxna2pT0f_8ahrQ4Z6D7ie1_bOnI__xhRJMJm7Aycot69jMxWj7RO_ClzOdbnUxuhc2WHMVtYwgKvWUnsAyfJl3t14ox1tARqWBXssj0K7EgexmfzwGGZThIl8E2QBMLQszzaNPA6DgjATW9rnkXvS75-LAxW16T9lorUHyFPTrJHh8HJfvTt0qTlXvcsg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
‏فرهنگستان زبان و ادبیات فارسی از سال 1369 تأسیس شد
از اون سال کلا 158 کلمه رو تغییر دادن و تو 8 سال اخیر، 2 هزار و 100 میلیارد بودجه گرفته
با ی حساب سرانگشتی کنی، می‌بینی برای تغییر هر کلمه، حدادعادل، 64 میلیارد پول گرفت!
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67177" target="_blank">📅 10:25 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67176">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SJ5fCjt_ZiIXpai5WGyJpvuyIj0xF4A9HquRQMHbPZT-lBe-cBlFxL_QMy5YDK9L0aO-DYukLKqxGAve0xEI9TEkd_Qpfohf8KxkdSdeLwIp8Lx4xKDTobsrhOxe19EON3q32241yw0k-KbbR4NL29e41eEN2AIBVORyVapvQSdjLbHX3X-QGqavBpCgacozNpmcedKDtkO0h2IsGe39LJFdy4UpQ2ux0agnzUWp1y8mo5ZwuNEntUNoFpHhras493fYVnJ-qTLPV_qyvhF0b_NRzsYLwJBubEbdDclvgs3rOWhNFEIVyn1N-lEtNc52AEY2Nin3YaBDlhlUgGBVkA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/514f1dff1b.mp4?token=SJ5fCjt_ZiIXpai5WGyJpvuyIj0xF4A9HquRQMHbPZT-lBe-cBlFxL_QMy5YDK9L0aO-DYukLKqxGAve0xEI9TEkd_Qpfohf8KxkdSdeLwIp8Lx4xKDTobsrhOxe19EON3q32241yw0k-KbbR4NL29e41eEN2AIBVORyVapvQSdjLbHX3X-QGqavBpCgacozNpmcedKDtkO0h2IsGe39LJFdy4UpQ2ux0agnzUWp1y8mo5ZwuNEntUNoFpHhras493fYVnJ-qTLPV_qyvhF0b_NRzsYLwJBubEbdDclvgs3rOWhNFEIVyn1N-lEtNc52AEY2Nin3YaBDlhlUgGBVkA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
حملات سنگین روسیه در طول شب به کیف اوکراین
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67176" target="_blank">📅 10:15 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67175">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromIRAN ANKER</strong></div>
<div class="tg-text">.
☀️
هوا گرمه ؟
🔥
ما قیمت‌هارو
💲
خنک
🧊
کردیم...
🥳
جشنواره‌ی تابستانه‌ی ایران انکر شروع شد
🤩
برای دریافت لینک جشنواره به لینک زیر مراجعه کنید
.
.
🛍️
تمامی محصولات انکر در این جشنواره انقدر تخفیف خوردن که این گرمای تابستون رو خنک کنن برای شما
❄️
.
.
📍
فرصت جشنواره محدودِ ،
دیر نکنید که این قیمت‌ها حالا حالاها تکرار نمیشه...
👇
لینک ورود به جشنواره
🌐
اینستاگرام
🌐
@iran_anker
#anker
#soundcore
#جشنواره‌ی‌تابستانی
#ایران‌انکر</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/news_hut/67175" target="_blank">📅 10:14 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67174">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=nYPns8tqWjYKXK5gXvYRx5nvt-wsE5Drwqxc3xFi8yB43lfUNpQRaLtnIU4AbJ0-9E-XaaUtliTueAoO_Jhw_2piDG7uUtNp4_ZNr5Jb_gZ6uIg5xYcrHme-1nPbhAVF6_M2ziwCXViC64Qq1BHWLFCTZ8gIEJrDgy2WvCC1i0pSlAtby8f05DBNMFlcCVLF4MALuW-vtFi7jf5ixsGyZDF3dTRmFux2AK0dWvVd8Kbnwx-sSkFIP9T3fk8C3qDnbVoF4y2sCT7tTMctCVd8ToUo0LecrM3kJxxVR51sGxgRT9ehFwvXb32OrDA59LEJbWMGjJyMV_IRk8DnywBrxg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b45db1d5ff.mp4?token=nYPns8tqWjYKXK5gXvYRx5nvt-wsE5Drwqxc3xFi8yB43lfUNpQRaLtnIU4AbJ0-9E-XaaUtliTueAoO_Jhw_2piDG7uUtNp4_ZNr5Jb_gZ6uIg5xYcrHme-1nPbhAVF6_M2ziwCXViC64Qq1BHWLFCTZ8gIEJrDgy2WvCC1i0pSlAtby8f05DBNMFlcCVLF4MALuW-vtFi7jf5ixsGyZDF3dTRmFux2AK0dWvVd8Kbnwx-sSkFIP9T3fk8C3qDnbVoF4y2sCT7tTMctCVd8ToUo0LecrM3kJxxVR51sGxgRT9ehFwvXb32OrDA59LEJbWMGjJyMV_IRk8DnywBrxg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
جلیل محبی:
مهدی محمدی(مشاور قالیباف) جی‌دی‌ونس ایران است!
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67174" target="_blank">📅 10:01 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67173">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=TRm2DulIlmWwx637s1lDB3E09uHCZfPUYEevmdIdI2yL9oIMn-ZPsT1Tt-iwXvswzpLjyOUc7YnIepxnm2uDTRsJQIE-ZSvpu17Ob59El7C0TcuKGtLT9EhrE4owP9VBrRP2rVruckcB8NNDIZv6WlywDz1iVGAEN3b4OPrys0FF22as5rRfn_Oqt8hnKWgT7tcMKk4qCF-8qMb4A3KJXQty5u-RJGtTtTw0chPH9gUmy_08y6G4chewpo7DuJf3h8ooZuXDXnayMUvu75AfsAmhEI7Rzxy4I7thSAvUVbZNzspyy46wkmaRpMzcNZiV6h9rbVXnlxj4O1TASdSdZ3_SL4j8zpQu4w-41mFYDOC0uO9IccDVAYmCy3mLScH2YSMY29dKpcPFupgy_X1ZuCQnAX_8YvekJyXxtgskUUxilH9VGrxGp97UEAHbDzg43hctY4Omtg1UyWix_f3pgCgZSC9YMNlS24sWhNZvJsNsVsWxZtLSyIcucnVgDESRHzOM006rg9f7goGixobOO-o7kpXqFVAC-C6YhSErxoNsXYdIOU1mRjhF-sq5Xkb9Uh2wgurgFrnSzeaXnPSTsGTuy82oC4i3Xx8IopHW5Z5QIREiVoOV_ZjETLI3hW5cFKU7TbMrDj4eO1r_iJUMaTpF8jwjAB4uVwPLDWfUjhA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/18665cc14b.mp4?token=TRm2DulIlmWwx637s1lDB3E09uHCZfPUYEevmdIdI2yL9oIMn-ZPsT1Tt-iwXvswzpLjyOUc7YnIepxnm2uDTRsJQIE-ZSvpu17Ob59El7C0TcuKGtLT9EhrE4owP9VBrRP2rVruckcB8NNDIZv6WlywDz1iVGAEN3b4OPrys0FF22as5rRfn_Oqt8hnKWgT7tcMKk4qCF-8qMb4A3KJXQty5u-RJGtTtTw0chPH9gUmy_08y6G4chewpo7DuJf3h8ooZuXDXnayMUvu75AfsAmhEI7Rzxy4I7thSAvUVbZNzspyy46wkmaRpMzcNZiV6h9rbVXnlxj4O1TASdSdZ3_SL4j8zpQu4w-41mFYDOC0uO9IccDVAYmCy3mLScH2YSMY29dKpcPFupgy_X1ZuCQnAX_8YvekJyXxtgskUUxilH9VGrxGp97UEAHbDzg43hctY4Omtg1UyWix_f3pgCgZSC9YMNlS24sWhNZvJsNsVsWxZtLSyIcucnVgDESRHzOM006rg9f7goGixobOO-o7kpXqFVAC-C6YhSErxoNsXYdIOU1mRjhF-sq5Xkb9Uh2wgurgFrnSzeaXnPSTsGTuy82oC4i3Xx8IopHW5Z5QIREiVoOV_ZjETLI3hW5cFKU7TbMrDj4eO1r_iJUMaTpF8jwjAB4uVwPLDWfUjhA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
😂
شادی نروژی ها بعد از صعود تیمشون به مرحله بعد
@News_Hut</div>
<div class="tg-footer">👁️ 18.1K · <a href="https://t.me/news_hut/67173" target="_blank">📅 09:33 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67172">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cLRo69gdUjH0_eh31KZDhefnn6jg22wG2ytliCSWil0vfp9nOkR9xvZuyAW551OQLjdF7TMC7CWRimSYA2noQdg0oM_vTcLe9Vpo8QzPdNe4mBIMPw6P9sCHQEiLnkC6bQdA1NYhFs2vnUyViEIR8YGyu-tFLqmhmCM0q5lThSkUZ21w3S-vwOYANuwb3oHNPXpyU7fUfIB2DLr9EdlKUZyeEhBYZ3690-VpYqSthuneY5TyBsrDFoxjEwpxvIWlOhGUf7HKNKcM2ymUcENjSTO24-rShJpLDPqu5vrO1VmnQ_QYPtR6lga9NT2DvHn9pR3BUUJsmKvNhGfgPGiKxw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⁉️
‏اطلاعیه ناوگان پنجم دریایی آمریکا در بحرین در پی یک سانحه برای یک بالگرد امریکا که طی آن یک تن از پرسنل مفقود شده اند:
🔴
در ساعت ۳:۳۰ بامداد به وقت شرق آمریکا (ET) در اول ژوئیه، خدمه یک بالگرد MH-60S Sea Hawk که به ناو هواپیمابر USS George H.W. Bush (CVN-77) اختصاص دارد، در دریای عرب فرود اضطراری روی آب انجام دادند.
🔴
در حال حاضر هیچ نشانه‌ای وجود ندارد که این وضعیت اضطراری ناشی از اقدام خصمانه یا حمله دشمن بوده باشد.
🔴
سه نفر از چهار خدمه بالگرد نجات یافته‌اند و هم‌اکنون در وضعیت پایدار در ناو جورج اچ. دبلیو. بوش هستند.
🔴
نیروهای دریایی آمریکا در منطقه همچنان در حال جست‌وجوی چهارمین خدمه هستند که هنوز مفقود است.
🔴
علت وقوع این حادثه همچنان در دست بررسی است
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67172" target="_blank">📅 09:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67171">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/news_hut/67171" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67170">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/GjORkcn6qXYp3r-fF8SFfYaBZGj6QVzkBpE_ER1zCvFDo-DTRLkHHP2Pv0XhS_bes971cOE3W9excr_1Boih5nSFMnG6dGJ5m7-f-UeV3Rpqm3l4fHXkiYmwK6-ITJ7qQe1F_wgJSWE56hxxB5lUs1JEqQ-0Qm17_OKCmbz4X2bh6RXj-M3XhzeTXohBgWqotk65XPjnLzhkw0Y75kcHXvwC-IeCX4A8zY-iLbvlgtJhE3ciGS2kCVWd6nT1kUBLq6EOlIZ_ztsNgOMW6brZlKNU8Df_fzQQzR-jMUbEUH8Ea86NQ4rLjIxOeglIvDeqYKj-32xn4z_6JkDfNoPcLQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کنم اگه هرشب با ۱۰۰ هزار تومن میومدین چنل بت ما ، شبی بالای ۲ میلیون سود کرده بودین مثل دیشب:)
😊
😂
میگی ن ؟ بیا تو چنلمون و ببین
🔥
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67170" target="_blank">📅 01:55 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67168">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e2juPabSi6sPOC3vl6RIlb2bC5_wbvBmRvA_TmmJCphgYL-IjD760wotlVSdLphswzYX6wHZsyqeU3rAVcBJTAc17QW3x1w7zsQrBGpbKQYPDpMAiKFgeJ6Jzth8mSHRxG2-YC3OVlT1JCdTFriNwLXtLJnVxXCDP5xZo7YIlR7g1yam4OrzaH37VTl12IO5Gj0Rfv3_j-1dPi8pzznWmBCyi1wjw3GnPQoDSLFADJAvKkPwzKJBgvmnWXpqkN_0ND5Ym6GWWjy5GSJsCY7MA9J_Q0Z7kKjD0dnoxtiMH-KCjCa1o1SXLf2w3AMlpeNjoLVbUZk3jMGO_iDWNtWd2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=saS7XgrOdB_iPZUK76THY4Wiu82oic6d43jInxKs81ApLP2aJo34RZIXNJF-ntffcn9MsvxPD5lOUYvGK1171KG6dv-hYdy0uDbrUGp4z-H7-okXi2dhkigCgmrinumwR2TS1pKEmUsMkrne27xArQcafEESNjlDUb5TqT-Fw1DYKyCrIXx-J-Eu6TIacJQeC7Lq901HpJqoF4vXR1jD8zAqUs6-2tbNzJ4jVi91RJN3zc7box_cG4WGoKsPAEDXPHS8PBd1f0dQL_1VnGQzKYdz_iOFZ4YKBiallJJjYbxIb-9DyKhWnnqjEoS3N02ZQ1eRIXUEdHua_HgE5VPPRw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/53ac383b11.mp4?token=saS7XgrOdB_iPZUK76THY4Wiu82oic6d43jInxKs81ApLP2aJo34RZIXNJF-ntffcn9MsvxPD5lOUYvGK1171KG6dv-hYdy0uDbrUGp4z-H7-okXi2dhkigCgmrinumwR2TS1pKEmUsMkrne27xArQcafEESNjlDUb5TqT-Fw1DYKyCrIXx-J-Eu6TIacJQeC7Lq901HpJqoF4vXR1jD8zAqUs6-2tbNzJ4jVi91RJN3zc7box_cG4WGoKsPAEDXPHS8PBd1f0dQL_1VnGQzKYdz_iOFZ4YKBiallJJjYbxIb-9DyKhWnnqjEoS3N02ZQ1eRIXUEdHua_HgE5VPPRw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
حملات موشکی سپاه به مواضع کردها درمنطقه کویا در استان اربیل عراق
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67168" target="_blank">📅 01:27 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67167">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">‼️
ویدیو‌ ای که گفته میشه مربوط به پارک ملت تهران هست و هلال احمر چادر های زیادی رو برای پشتیبانی از مراسم دفن کردن علی خامنه ای در آنجا قرار داده.
@News_Hut</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/news_hut/67167" target="_blank">📅 00:57 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67166">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=J6GfogV3WJpji2K3P5BgzNHvrRczcyvC8_aFbxC3uCeU_237Cup-OTiAxi0Rbp4Y1lCSapqY2lbkf2WtdnpAdrzCmAej32fR8PkWfAeqZtdLfMxXwYDE7WECTjsdWui1B3kVdNbHRiQrrQNbKMBV37GkKrzUmbs0mxClPJbhQv7fTp8PVuJiERYzOCZhcPHurkCk0PtGy2aAjVOgI2STiKBu4q-zTQ6Sy_qQ0usubmuUg7195jO7hOUPvHBy0682ocGyuwQpBet-aQ2i021rluVYbU_eu5tEp4JB8oPu2tCAZx216VKKV_U1e2yp2CjsHK4UtmTDB3axsjkaoQmRNw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1b0f2d20b2.mp4?token=J6GfogV3WJpji2K3P5BgzNHvrRczcyvC8_aFbxC3uCeU_237Cup-OTiAxi0Rbp4Y1lCSapqY2lbkf2WtdnpAdrzCmAej32fR8PkWfAeqZtdLfMxXwYDE7WECTjsdWui1B3kVdNbHRiQrrQNbKMBV37GkKrzUmbs0mxClPJbhQv7fTp8PVuJiERYzOCZhcPHurkCk0PtGy2aAjVOgI2STiKBu4q-zTQ6Sy_qQ0usubmuUg7195jO7hOUPvHBy0682ocGyuwQpBet-aQ2i021rluVYbU_eu5tEp4JB8oPu2tCAZx216VKKV_U1e2yp2CjsHK4UtmTDB3axsjkaoQmRNw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
در خانه ای که اسامی محمود،احمد و محمد باشه فقر وجود نداره.
@News_Hut</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/news_hut/67166" target="_blank">📅 00:28 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67165">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">🚨
🚨
🚨
🚨
نماز میت بر جنازه علی‌خامنه‌ای توسط یکی از مراجع تقلید خونده میشه و خبری از مجتبی خامنه‌ای نیست
@News_Hut</div>
<div class="tg-footer">👁️ 24K · <a href="https://t.me/news_hut/67165" target="_blank">📅 00:02 · 11 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67164">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pQL-gTzSUv75j6nJoxzeGVFBx5HVYYaELSLUooOJqPow_vzxJSYVc81vOQ5luGbaBG9yZ8Kr9IOXLvOMWkfkKzlIby_U2SVg5OIuUwLrvl0v583ZtJdSEdCxf0hNyDsXHCj5Fgc-H6JYuVFDVMUArSdPBcIpHSFQrwzPtc8w6P6N5EjzYxtMznAfbWVzpQmVz9UAIETt9xAdnWUNNUU833vjufujEOD39qLWlpNdzkrAhYRD4UIJcCy1DGPKpqesKGbmTzsE1Dc2IqUOiA1-OoNn0eYh5yoLeaxQ9hx9z31heX2LmrAYFT8YP0JXuhTLi3sG6W5baC8hUC0PI77C0TzLd2ij_s9R7JlLWQlbr5ziYcx3L19jkaucpAvTqUCAQVj-H27z7JpRjWLNT5bRQZ365vYGmwy5CzgNke5dYIwYhvsKpfRvv7c3aO20uwpcpI2omrZQAoJGdapg5XY730VaShIYgc9kOunagKHDjjjp0CojamM9XfPCGqyPI3gp5GPFVpI4SglG9T-pPCflqw24kd0mSwFhOfF93rviyCcl4h---UFsZeJms50GBRlx_5yaGWWOov2GwbT3oZQqBVfw2_zaxzYSqc1L6XvLRmoGH2LqiCYF0NKZ_9ruwELvACtj8KRsQHpULHnFVZ_iW5nO7DiSP00QIShtNl-HNsY" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/44959f900a.mp4?token=pQL-gTzSUv75j6nJoxzeGVFBx5HVYYaELSLUooOJqPow_vzxJSYVc81vOQ5luGbaBG9yZ8Kr9IOXLvOMWkfkKzlIby_U2SVg5OIuUwLrvl0v583ZtJdSEdCxf0hNyDsXHCj5Fgc-H6JYuVFDVMUArSdPBcIpHSFQrwzPtc8w6P6N5EjzYxtMznAfbWVzpQmVz9UAIETt9xAdnWUNNUU833vjufujEOD39qLWlpNdzkrAhYRD4UIJcCy1DGPKpqesKGbmTzsE1Dc2IqUOiA1-OoNn0eYh5yoLeaxQ9hx9z31heX2LmrAYFT8YP0JXuhTLi3sG6W5baC8hUC0PI77C0TzLd2ij_s9R7JlLWQlbr5ziYcx3L19jkaucpAvTqUCAQVj-H27z7JpRjWLNT5bRQZ365vYGmwy5CzgNke5dYIwYhvsKpfRvv7c3aO20uwpcpI2omrZQAoJGdapg5XY730VaShIYgc9kOunagKHDjjjp0CojamM9XfPCGqyPI3gp5GPFVpI4SglG9T-pPCflqw24kd0mSwFhOfF93rviyCcl4h---UFsZeJms50GBRlx_5yaGWWOov2GwbT3oZQqBVfw2_zaxzYSqc1L6XvLRmoGH2LqiCYF0NKZ_9ruwELvACtj8KRsQHpULHnFVZ_iW5nO7DiSP00QIShtNl-HNsY" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
‼️
قالیباف خطاب به مخالفین مذاکره: بیشتر از این آزار ندهید و حرف‌های ترامپ را هم غرغره نکنید
نه در دیپلماسی کمک می‌کنید؛ نه در جنگ!
@News_Hut</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/news_hut/67164" target="_blank">📅 23:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67163">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z9RV7Jzdw95YfgkW9xUfGDheQh792azxvJBj-KXT9QXgsXuHn8Onb9Zxae5Ljq2V3BfnEKlrIWsHcfj3vVkNrO5LR7QSSkK_x9dlmrjgxHBWJgJDQp_HHV5HICK7uvSwdrTSQqmr3dx8pQt7aYO0cm2JoeVVmLRGoiLByQk63bv7Fr77wfsw2bGGvhIGFEYGfedf-0NJNvTzyDuF0_4g6SnkYiIaZ69C4iAnKJknMiDHbFDap-1mRypE0BI011Eo1syuaqMIh6at4AGrEEAux2eupYKfRA5fjidzXX83p6rCqEN-FDnhsQTPjOZm-1bdUCDKn4cSICyxH7PzNazgGg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
برخی مطرح کردند که چرا اعلام شده ۲۰ میلیون بشکه نفت در اختیار فلان مجموعه قرار گرفته و این موضوع را افشای اطلاعات داخلی دانستند. اگر بار دیگر نیز چنین شرایطی پیش بیاید، نه ۲۰ میلیون بشکه، بلکه ۱۰۰ میلیون بشکه هم در اختیار آنان قرار خواهم داد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.8K · <a href="https://t.me/news_hut/67163" target="_blank">📅 23:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67162">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=JX3XrY8V5JFSqUuYKRU8aRck5BGsX4owAhMXama6syaB8LTwpA-q4FtOf_9TEFL6qKmohtgcjjkjbs--knIknDjpMSAm3h8rCrKuaJK4o_Qi0BfRlriZCsfBfD0D4QGbwgP1AAnnPmJSdUdnV-x9KYXWuoRCIuJJGNSvcPuK49AGCKN6OT_0d1NLxuI5h8nmI-KVWKMfqXQChf7bM7dDcUfqg9gSKHtCadZiAVz5ZG0z5Q7cOJIlU_SdM6cA2WgBXCkONMzhlRmP0uZLFSc5v9y3FwZ9Rjm2DdALQ6FWaOO-5qQGjp5ObuetI0-xaTBavJH3l-GhPxt60iku64ftBA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/076f83ca5a.mp4?token=JX3XrY8V5JFSqUuYKRU8aRck5BGsX4owAhMXama6syaB8LTwpA-q4FtOf_9TEFL6qKmohtgcjjkjbs--knIknDjpMSAm3h8rCrKuaJK4o_Qi0BfRlriZCsfBfD0D4QGbwgP1AAnnPmJSdUdnV-x9KYXWuoRCIuJJGNSvcPuK49AGCKN6OT_0d1NLxuI5h8nmI-KVWKMfqXQChf7bM7dDcUfqg9gSKHtCadZiAVz5ZG0z5Q7cOJIlU_SdM6cA2WgBXCkONMzhlRmP0uZLFSc5v9y3FwZ9Rjm2DdALQ6FWaOO-5qQGjp5ObuetI0-xaTBavJH3l-GhPxt60iku64ftBA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
حمله پسر سردار طاهری به پزشکیان:
مگه نفت بابات بود که می‌گی ۲۰میلیون بشکه نفت دادیم به نیروهای مسلح تا بجنگن؟ اگر نیروهای مسلح نبودن ما نمی‌تونستیم اینجا شعار بدیم
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67162" target="_blank">📅 23:05 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67161">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=G-zX7kPHWSkRBPWEcBBR36RLenr-GMxnEw6dwnrEeAirnxkeKHTFLNmzkjpiMOlsmC7MuMv_UBVam_jInHCns8JNn6jnEu4Jp2kYMhW2SWY2qmBGsizcd_j_k4E7p3l0vdN9M3nxHbYK1gYWtFj0F6oSyafX58fUWi2myAMckY4oVVRxhHbtoGDSq9kX8yc5GGGctWFPdjPYtBe1HnpcKIOiBGM8dauIAvnA5yYSt1wg_GnqL1AHKjx6Dy1v-dTmcHXOOKCS2GytiLt2yqfLp1nuerDKYr7N40t8cd-FXLb35d6lqExFhto0uCyS2E93FaPuvY4sYJ9ct-EEBiM4Kg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a7f1bdcd52.mp4?token=G-zX7kPHWSkRBPWEcBBR36RLenr-GMxnEw6dwnrEeAirnxkeKHTFLNmzkjpiMOlsmC7MuMv_UBVam_jInHCns8JNn6jnEu4Jp2kYMhW2SWY2qmBGsizcd_j_k4E7p3l0vdN9M3nxHbYK1gYWtFj0F6oSyafX58fUWi2myAMckY4oVVRxhHbtoGDSq9kX8yc5GGGctWFPdjPYtBe1HnpcKIOiBGM8dauIAvnA5yYSt1wg_GnqL1AHKjx6Dy1v-dTmcHXOOKCS2GytiLt2yqfLp1nuerDKYr7N40t8cd-FXLb35d6lqExFhto0uCyS2E93FaPuvY4sYJ9ct-EEBiM4Kg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
فیروز کریمی:
قلعه نوعی 5 سانت رو تحمل کرد 10 سانت رو تحمل کرد، 30 سانت رو دیگه کجاش بذاره
🤣
🤣
🤣
@News_Hut</div>
<div class="tg-footer">👁️ 24.7K · <a href="https://t.me/news_hut/67161" target="_blank">📅 22:15 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67160">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=tOjr1VdAQR2Ni0CLPm1_81lNpEZ1yI8LYOiKfORAxwBkXl9Sq0GhH-afKeeRnmPTtES9Xhl2-h2SgMtn40zkRsW56aOhvgDSa64Vbu8t9aDQLmd8Nw2dTchO9DsfP2TbZEUXbw_nKzoD0fBl9MHzaHYcgd1Uft7Isb9nfSCzDdOUWsqPs2j5xfv4C53VUsfQgcdG6UG90VcS3VWCW6Wda9F7YiyGJXcWW0qoPnh_YaBez7a8jm8Euc1i_b3DD_ZAyxiyf-QGw8SiAHBJ3U2CG01igjx4cSxUn2Li1xfkSZN3LJ2LqrOJAw2Pv7n-65Ha6U95qW7jNEPXtLDRmF9_dg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/7be0c9f31d.mp4?token=tOjr1VdAQR2Ni0CLPm1_81lNpEZ1yI8LYOiKfORAxwBkXl9Sq0GhH-afKeeRnmPTtES9Xhl2-h2SgMtn40zkRsW56aOhvgDSa64Vbu8t9aDQLmd8Nw2dTchO9DsfP2TbZEUXbw_nKzoD0fBl9MHzaHYcgd1Uft7Isb9nfSCzDdOUWsqPs2j5xfv4C53VUsfQgcdG6UG90VcS3VWCW6Wda9F7YiyGJXcWW0qoPnh_YaBez7a8jm8Euc1i_b3DD_ZAyxiyf-QGw8SiAHBJ3U2CG01igjx4cSxUn2Li1xfkSZN3LJ2LqrOJAw2Pv7n-65Ha6U95qW7jNEPXtLDRmF9_dg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔴
خبرنگار: آیا می‌توانید قول بدهید که آمریکا قبل از تمام شدن ۶۰ روز تفاهمنامه، دوباره وارد جنگ تمام‌عیار نشود؟
​
🔴
جی‌دی ونس: ترامپ تا وقتی که مجبور نباشد، نیروهای نظامی را دوباره به جنگ نمی‌فرستد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.5K · <a href="https://t.me/news_hut/67160" target="_blank">📅 21:46 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67159">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">🚨
🚨
آکسیوس به نقل‌ از مقام آمریکایی:
در مذاکرات دوحه تفاهمی حاصل شد تا اوضاع هفته آینده آرام بماند تا در اجرای تفاهم‌نامه پیشرفت حاصل شود.
@News_Hut</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/news_hut/67159" target="_blank">📅 21:20 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67158">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iyMcE9-3lf5wPKJpCkYIZOd7LeNM60Nq8fPO98N816FJ5JHMIesUVQ-IdToA4e1IC8PTzXsDqwa4_-Q54tQrJ5ujWqQomAW97wXHdv8oEKFyzKmM9ZuyoeVaL-UBd-JGJGAyLjIhf48KmiVyQZZF1fgDCDBU2ISm2E3mzf4VeZp5NyzUWYju8HMxGnszdZuNjlDqvO267T1XLR8qTAMD_jdoR7zalm9YW5VNQvX98TWSHslWEDNZd1SDmtL6KdapkYhPd8ptnaEp4eHKq9sphrcMUHpE53beK6St5-Yn6cpav8uxTUZcbAv3r772YVGTHqmyy4fJv2xJy-nGNX1nTA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
آکسیوس:همزمان با از سرگیری مذاکرات در دوحه، ایالات متحده تلاش می‌کند تا ایران را از پرداخت عوارض منصرف کند.
مذاکره‌کنندگان آمریکایی و ایرانی در دوحه برای مذاکراتی با تمرکز اصلی بر تنگه هرمز حضور دارند و دولت ترامپ مدعی است که ایران از توافق هسته‌ای سود بسیار بیشتری نسبت به عوارض عبور و مرور در این تنگه خواهد برد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67158" target="_blank">📅 21:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67157">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=l3ZzdkMklg4iuUnN-E2Q2lE046bOHvMO68cjCIjvnerng3R8AZ-kO0Q-hCG900aoSla02IJLgLSJpkA6w4baS-LD0XtyEdeVAwouHd6LpRw9pdwuN1fWfTMUqfqtArOkoTk6o6EYPXdiPHCa2qak1JjHluANyKJ1-lqSBVZPBdjP9Q0Aa1UbeIwXp5zsD_J_34SOkwTwrY41BAjf3Z_zs9XDED2wLPefnRtyvYfHHd6cxjJUD5BGUsbj8piLEU_ROY3g8kRau0DEvy2tdeupghbUstzhuWF8zQDXCbVI5c-BNPHPGRjgseBKjZGIQar8cak3xtSvYnYIKoXwzCoYWg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b973f48d61.mp4?token=l3ZzdkMklg4iuUnN-E2Q2lE046bOHvMO68cjCIjvnerng3R8AZ-kO0Q-hCG900aoSla02IJLgLSJpkA6w4baS-LD0XtyEdeVAwouHd6LpRw9pdwuN1fWfTMUqfqtArOkoTk6o6EYPXdiPHCa2qak1JjHluANyKJ1-lqSBVZPBdjP9Q0Aa1UbeIwXp5zsD_J_34SOkwTwrY41BAjf3Z_zs9XDED2wLPefnRtyvYfHHd6cxjJUD5BGUsbj8piLEU_ROY3g8kRau0DEvy2tdeupghbUstzhuWF8zQDXCbVI5c-BNPHPGRjgseBKjZGIQar8cak3xtSvYnYIKoXwzCoYWg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
پرزیدنت ترامپ:
«روند خلع سلاح هسته‌ای ایران به‌خوبی پیش می‌رود... بازار سهام تقریباً هر روز در حال ثبت رکوردهای جدید است. قیمت نفت به‌شدت کاهش یافته است... و اکنون از زمانی که من حمله به ایران را برای جلوگیری از دستیابی آن به سلاح هسته‌ای آغاز کردم نیز پایین‌تر است.»
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67157" target="_blank">📅 20:27 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67156">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1792b01078.mp4?token=jpfnYjOLCpGOjJe5lJfmr-yvk7ambtqC4GpyisSOFYlNhLe9crreL8fN30otKIa6ryUc3e6MevwI4FWR5iaI4NJ_nfoyTLsuolIGH5AUvavmTVs2SnDndkDuj-dVmEABVy2F-aBxnp63_bidCw82SM8YyAipHEK7VVhd7Jk0TqEaJtoTy_yJAnqfO5qP1DRVJwMAzx090TJOj79gC0W73K6_MyCVN07dcl9BYy2OF5X5Kutv9vG-fHx7NZT97F2Fgv3lLj7Cytqkg4b7Rlg3I0LTAYbqreQ9rNAS2bNyZSTiqV9ixgPt5VHicAvophZG4m_9PBiQbWKHWQYTzjeUHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1792b01078.mp4?token=jpfnYjOLCpGOjJe5lJfmr-yvk7ambtqC4GpyisSOFYlNhLe9crreL8fN30otKIa6ryUc3e6MevwI4FWR5iaI4NJ_nfoyTLsuolIGH5AUvavmTVs2SnDndkDuj-dVmEABVy2F-aBxnp63_bidCw82SM8YyAipHEK7VVhd7Jk0TqEaJtoTy_yJAnqfO5qP1DRVJwMAzx090TJOj79gC0W73K6_MyCVN07dcl9BYy2OF5X5Kutv9vG-fHx7NZT97F2Fgv3lLj7Cytqkg4b7Rlg3I0LTAYbqreQ9rNAS2bNyZSTiqV9ixgPt5VHicAvophZG4m_9PBiQbWKHWQYTzjeUHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🚨
🚨
قائم‌پناه، معاون پزشکیان:
اگر قرار باشد هر آنچه رهبری می‌گوید اجرا کنیم که دیگر نهادی نباید وجود داشته باشد
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67156" target="_blank">📅 20:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67155">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=EnmWU-SwXG55f_AC2nmp5doesIHvWIyYhFOlg8KSM1_jU_t9SfvOwlmV5Ju05a1EdxcZJozHPvPwxueNywXaQ5W4LJeUJdEJ_nYtfcQ6tSCfCEkLKueFTxDHMonObL169ubzh1OJ3w0WieT8293t2lGrTSyr5WW4VRq9y_EAzHVmJoGuJYLMaPL9G9hb_kXjnv82YcOUHxc-erLls4B2Ab1fRdQ4zIObATahC-B2Qgl_J69nvA8R-LD9LOLRpIpGQVse3Q67x5dB7DxV0X-q9YKja7IYfOMOoMbRl0-lLS1P53o8gYPLPz8hNQTCD08gCv_C15L0PUwAfnTGs_E5JWa9AFQp7JO0j2lMY4iTpkmrTF9pKigYzTVpKdpDfqBJxb9NLMu5rsGt89GZd22_kyLA6rJr3Sr2T8rZuDNnQVCa1vivApNKxhn8duYNTNuBFTOVCXF4ruPC-ou5tOX80kbahPFov4kNlpBWONRM5OryGg8K8U0ETZLRRmAWEBfXK5XtKWBYQEVj6IDvG2Ie-ZgTz0MLewaG5A6VRzlfqK7V5j0mGVeq_bxmIrtEgB7LUTzVdPbsYo1uE1TuN20wPf0eLU7HNx_JSa7r4tcyWq_eNnyMvlc98o0E941-mAgYeqpUyf4LmeaGTHWyWaNMVU5JR3fKzzDMOBDgOoPvwT8" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e20aabab5a.mp4?token=EnmWU-SwXG55f_AC2nmp5doesIHvWIyYhFOlg8KSM1_jU_t9SfvOwlmV5Ju05a1EdxcZJozHPvPwxueNywXaQ5W4LJeUJdEJ_nYtfcQ6tSCfCEkLKueFTxDHMonObL169ubzh1OJ3w0WieT8293t2lGrTSyr5WW4VRq9y_EAzHVmJoGuJYLMaPL9G9hb_kXjnv82YcOUHxc-erLls4B2Ab1fRdQ4zIObATahC-B2Qgl_J69nvA8R-LD9LOLRpIpGQVse3Q67x5dB7DxV0X-q9YKja7IYfOMOoMbRl0-lLS1P53o8gYPLPz8hNQTCD08gCv_C15L0PUwAfnTGs_E5JWa9AFQp7JO0j2lMY4iTpkmrTF9pKigYzTVpKdpDfqBJxb9NLMu5rsGt89GZd22_kyLA6rJr3Sr2T8rZuDNnQVCa1vivApNKxhn8duYNTNuBFTOVCXF4ruPC-ou5tOX80kbahPFov4kNlpBWONRM5OryGg8K8U0ETZLRRmAWEBfXK5XtKWBYQEVj6IDvG2Ie-ZgTz0MLewaG5A6VRzlfqK7V5j0mGVeq_bxmIrtEgB7LUTzVdPbsYo1uE1TuN20wPf0eLU7HNx_JSa7r4tcyWq_eNnyMvlc98o0E941-mAgYeqpUyf4LmeaGTHWyWaNMVU5JR3fKzzDMOBDgOoPvwT8" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🚨
🇺🇸
جی‌دی‌ونس:
«من واقعاً فکر می‌کنم ایالات متحده، فارغ از اینکه مذاکرات در نهایت به چه نتیجه‌ای برسد، در موقعیت بسیار خوبی قرار دارد.
اگر مذاکرات موفقیت‌آمیز باشد، که بدیهی است ما می‌خواهیم چنین باشد، با ایرانی روبه‌رو خواهیم بود که به‌طور دائمی دگرگون شده است.
از سوی دیگر، اگر ایرانی‌ها رفتار مناسبی نداشته باشند، برنامه هسته‌ای آنها همچنان نابود شده است، توان نظامی متعارف آنها همچنان از بین رفته است و ایالات متحده نیز در مقایسه با ایران همچنان در موقعیتی بسیار قدرتمندتر قرار دارد.
@News_Hut</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/news_hut/67155" target="_blank">📅 19:47 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67154">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=O-Di4G0anlRO4tpInIvjDqwvUvsCIH9_JqFMkicKFQFDp8se8HTRvRmb8OBMLkgkSbyeunYFYNW7T3kdQ7VvAxzoNufkYQncpbAEXcVpukosckpLQE4zKMCtSa_wRWOW4J4Ot3xBA03hqh6O7InHKmGQw3-DcX9koCebHZcA4jnWxxBWCWQ18BUw57lPCx4iMTUSQEmapuPNTW9rmNKmSF_ZVdXabaYr7YLkAEZyia5at6Wz7RW9VFaKaYwttIyjpiOYNiLpgABgTjMQbCC82bTTYhgeXEmoOzHYGySBME1eaE_AqyvEbvyKojuEl2jzNuBVGS-AjWQci2zRKvzuxA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b1035b1e35.mp4?token=O-Di4G0anlRO4tpInIvjDqwvUvsCIH9_JqFMkicKFQFDp8se8HTRvRmb8OBMLkgkSbyeunYFYNW7T3kdQ7VvAxzoNufkYQncpbAEXcVpukosckpLQE4zKMCtSa_wRWOW4J4Ot3xBA03hqh6O7InHKmGQw3-DcX9koCebHZcA4jnWxxBWCWQ18BUw57lPCx4iMTUSQEmapuPNTW9rmNKmSF_ZVdXabaYr7YLkAEZyia5at6Wz7RW9VFaKaYwttIyjpiOYNiLpgABgTjMQbCC82bTTYhgeXEmoOzHYGySBME1eaE_AqyvEbvyKojuEl2jzNuBVGS-AjWQci2zRKvzuxA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
امروز یه عده کسخلِ پا شدن رفتن فرودگاه که از بازیکن‌های تیم میلی جمهوری اسلامی استقبال کنن. مثلا می‌خواستن شبیه هواداران تیم ملی نروژ به سبک وایکینگی تشویقشون کنن که اینطوری ریدن
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67154" target="_blank">📅 19:21 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67153">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nxk72Agjsr4p74oAXHLFoUrh4F1d2Agl2udvTh9pmJ-bH7tmxsjydqk4OfJ8jr09qTtE5JxOz3RQY3YQ1EunYeoL1JbS_nJxN0VMGkCBkKJL8RWRCCwYB63-s4e_jkMl1BIbi28hO_W2EcGbnRafPa3v6sSu7Slts-5mpL567bei8qw4vLGEtiNOM8DMFL9_uwNFhk_oZX4nM7QmO3G-b-hXkVvOf3gU5OdeTk3kAuYQCLQ68gMIEAdfVP9C9Nk7VQhhHT05aKUm6m4pWx5B141Bb6LubEVXIU79eDzxzOoJpYO-UGnOT5HzCoSRImqKa16ZmGJBWseLljxpY8nTyg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
پزشکیان:
به اعضای تیم ملی فوتبال کشورمان که امروز به ایران عزیز بازگشتند، خداقوت می‌گویم.
تلاش و مبارزه با تمام وجود و تا آخرین لحظه، مهم‌تر از پیروزی است.
کار علمی، حفظ روحیه، رویکرد تحولی و انگیزه بالا شرط پیروزی در آینده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67153" target="_blank">📅 18:48 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67152">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ctIeKKbFZ88BOHQN39nNjeoGvwrcMOFRsQZgO26UqgVZVWx-ntD2xWk3AyMJlaz9rVYCVQwQ4sk3iVri2SnOzNeBi6kJnW0a5OAzORiyPtNQ-NpT_IsdLFvDRrfzGgSzjWCz_l7LKvg-Rk-9KAl9voe_gqHWI4zt-6yyibFPDYhxWckqxEnzAbSxmDTwq5l4phqXoX8C9lYDaSqmPp63Ot4CYoFfoUdPNwAgZNpGP6p2T6kv8Zbrf5R2prjce1UDm8eQ6LB9E_Wz-x4HcX5qDfMpFzxt5o0gtM99iczx_NGdtwFr_j2NYQXFhgmXypwzcTgw2eMoyNd9047ev7Zwkg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2b5b7ea7b3.mp4?token=ctIeKKbFZ88BOHQN39nNjeoGvwrcMOFRsQZgO26UqgVZVWx-ntD2xWk3AyMJlaz9rVYCVQwQ4sk3iVri2SnOzNeBi6kJnW0a5OAzORiyPtNQ-NpT_IsdLFvDRrfzGgSzjWCz_l7LKvg-Rk-9KAl9voe_gqHWI4zt-6yyibFPDYhxWckqxEnzAbSxmDTwq5l4phqXoX8C9lYDaSqmPp63Ot4CYoFfoUdPNwAgZNpGP6p2T6kv8Zbrf5R2prjce1UDm8eQ6LB9E_Wz-x4HcX5qDfMpFzxt5o0gtM99iczx_NGdtwFr_j2NYQXFhgmXypwzcTgw2eMoyNd9047ev7Zwkg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
جی‌دی‌ونس:
ترامپ میخواد با این تفاهم‌نامه با جمهوری اسلامی، بازارها و مخازن رو از نفت پر کنه،
و بازار سهام و اقتصاد رو درست کنه
بعد تصمیم بگیره با ج‌ا چه کنه!
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67152" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67151">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=c4H6NSswI10QRK6M4WxZ0gOaIilt74ve_fNhxpKSUdy4deMTv6K6tU5pNiN-0nQgiC6B2pe-mxqd503Ab0iy8kU2AFGc9axgHbOjekm2MbaILdfhWEZv-64EHsBNoQJJh_n4JUZx9ovtMt-FeGwIVLb6_1Q3l13IhTybRcmNHNxLwbinMIEaOtwZ1PJzD90rW-o6s35m05LbvTHIGU9AG-uoK7w8cJrGmW1g_SCEHB93SP1QNwnoeKVJ6hv_dQZLDj-ARInK3Zfdp1af2QkFKSSPnEOz5RNzasMtbmLoBMM2K_zSMVu9qsHF9RtPLLxa-KDa2MiwVVe9MU91Ary2vw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/5127a5f793.mp4?token=c4H6NSswI10QRK6M4WxZ0gOaIilt74ve_fNhxpKSUdy4deMTv6K6tU5pNiN-0nQgiC6B2pe-mxqd503Ab0iy8kU2AFGc9axgHbOjekm2MbaILdfhWEZv-64EHsBNoQJJh_n4JUZx9ovtMt-FeGwIVLb6_1Q3l13IhTybRcmNHNxLwbinMIEaOtwZ1PJzD90rW-o6s35m05LbvTHIGU9AG-uoK7w8cJrGmW1g_SCEHB93SP1QNwnoeKVJ6hv_dQZLDj-ARInK3Zfdp1af2QkFKSSPnEOz5RNzasMtbmLoBMM2K_zSMVu9qsHF9RtPLLxa-KDa2MiwVVe9MU91Ary2vw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇺🇸
پرزیدنت‌ترامپ :
روند خلع سلاح هسته‌ای ایران به‌خوبی
پیش می‌رود… بازار سهام تقریباً هر روز رکورد تازه‌ای ثبت می‌کند.
برای سه شب هم محکم بهشون حمله کردیم
الان هم روند مذاکرات خیلی خوبه.
قیمت نفت به‌شدت کاهش یافته، حتی نسبت به  زمانی که حمله به ایران را آغاز کردم ،
الان نفت رسیده به ۶۷ دلار،  پایین آمده.
هرگز به سلاح هسته‌ای دست پیدا نخواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67151" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67150">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromحاشیه نیوز</strong></div>
<div class="tg-poll">
<h4>📊 نظر شما راجع به عملکرد پزشکیان و دولت او حول و حوش مسائل جاری در کشور چیست؟</h4>
<ul>
<li>✓ بسیار ضعیف</li>
<li>✓ فاجعه بار</li>
<li>✓ شکست مطلق</li>
<li>✓ بعدها شاهد عواقب خوب و بد خواهیم بود</li>
</ul>
</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/news_hut/67150" target="_blank">📅 18:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67149">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">‼️
آخوند قاسمیان:
واشنگتن رو اشغال کنید؛ ترامپ رو دستگیر کنید و بیاریدش پیش مجتبی.
@News_Hut</div>
<div class="tg-footer">👁️ 18.5K · <a href="https://t.me/news_hut/67149" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67148">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=TZfmQMSjvWyuDfjtDzUDnPgEjx6GbUCTB0DdiuVC1eXA4s6z2y1z06ZetLlWi2AdMAQED9LNZ-e5Tr6zhN1cMQNQUGwGYEFyKqcsozcMvfsiii4ezKEGcYCTjVb3391Hc8pJd9L35KA-zdSlpzwE4Se9mFbr6SVTad6X7dzcApTLQINO45-1DFMa6SwPhcPocOfgt6a5ke1kxLegy4Udrhkm-iyUBs6SV1Ghqy2Bk8LlWLWX2nlnvFR9KhtCzlnTNOkEKzVyi5-H5CktkVk59o5J_LxNecKrTxEzMNxXZHG74jZwXLwThBXWckL-4Wc5laiNmQxAtu3kcvf7H2EuLg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/257f4db3ce.mp4?token=TZfmQMSjvWyuDfjtDzUDnPgEjx6GbUCTB0DdiuVC1eXA4s6z2y1z06ZetLlWi2AdMAQED9LNZ-e5Tr6zhN1cMQNQUGwGYEFyKqcsozcMvfsiii4ezKEGcYCTjVb3391Hc8pJd9L35KA-zdSlpzwE4Se9mFbr6SVTad6X7dzcApTLQINO45-1DFMa6SwPhcPocOfgt6a5ke1kxLegy4Udrhkm-iyUBs6SV1Ghqy2Bk8LlWLWX2nlnvFR9KhtCzlnTNOkEKzVyi5-H5CktkVk59o5J_LxNecKrTxEzMNxXZHG74jZwXLwThBXWckL-4Wc5laiNmQxAtu3kcvf7H2EuLg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
حمله امروز اوکراین به پالایشگاهی در حاشیه مسکو
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67148" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67147">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان  جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn @kaviani_vpn</div>
<div class="tg-footer">👁️ 17.4K · <a href="https://t.me/news_hut/67147" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67146">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/e4tBaRHexQlVSJRgJf61VseTBumrY35aXSH6buS6YWKGqrjISf9tfUMfcqzeDjS56PUC8B2VhE0xJRBMxC7kaOxcTEQhuw5lrMawKCN69WT_UC2iy-NkLc4Kj52p7FZaC1h4cBQYiqzJfAwVK2dHFzPI1FMD9NdJ2JmUsedXeIXFAlrMCYaATFDEP2q8iS9QuxPULnCRJ5Dd_s9NDz1jCUhJ960sjuUk1kjoDVDDC1Q9-mDQggN8dQPgcHrRG8DVbLMZFuH7d39m2Ooq9bIQ64R9DniH4iGKc6f_DcMy-poXlPff2rGe4CZYbuQ0JAIs30d97UYPPHiXD8URkPSvEQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
فروش کانفیگ‌های نامحدود
💵
قیمت: 380 تومان
✅
سازگار با تمام اپراتورها
✅
سرعت بالا و پایداری واقعی
✅
مناسب برای گیم
✅
تحویل آنی
❗️
پشتیبانی 24 ساعته
📣
همراه با تست رایگان
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 19K · <a href="https://t.me/news_hut/67146" target="_blank">📅 18:09 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67145">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=cHqZGf7o8R9Q6TJfRaWAue0qJmORFSNpAogjXSWw42dEbYynGwFcNoZSq6eEDY74s5ilMZ-8YMG7oxaXr6YMrFE_xiWr8N_4eoZksrmsrDyTqvgCPdk2yKDH10Jm4ylSuWBnjW10GjtENh4PyOpgUyB3Hm_bT4dlvK880-SNhSOWkWONteXK__ysX7kDAv-ZiO-Y5yZBYd5lwjiBUlOYpfP7jKr6xZ22mX8gdM9AYgkNFy9DbTZWpspOzgbHt1ZRlh98Lp6Vw0-2a9q76NCds44k6QHihTirQwvy7rzk2vauXvyuq-sp9TLWfgAc4EHnCqWVF9XhUoF1Hvjf_Dznbw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/158f79bda3.mp4?token=cHqZGf7o8R9Q6TJfRaWAue0qJmORFSNpAogjXSWw42dEbYynGwFcNoZSq6eEDY74s5ilMZ-8YMG7oxaXr6YMrFE_xiWr8N_4eoZksrmsrDyTqvgCPdk2yKDH10Jm4ylSuWBnjW10GjtENh4PyOpgUyB3Hm_bT4dlvK880-SNhSOWkWONteXK__ysX7kDAv-ZiO-Y5yZBYd5lwjiBUlOYpfP7jKr6xZ22mX8gdM9AYgkNFy9DbTZWpspOzgbHt1ZRlh98Lp6Vw0-2a9q76NCds44k6QHihTirQwvy7rzk2vauXvyuq-sp9TLWfgAc4EHnCqWVF9XhUoF1Hvjf_Dznbw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
لحظه تسلیم شدن قوی ترین ارتش جهان رایش سوم (نازی ها)
@News_Hut</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/news_hut/67145" target="_blank">📅 17:35 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67144">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=dtLEjJKBH0ycMf2gw5LEH2BQkY42NwH0BWysIDE-Gz9ipT7O2NDimMKGH1EBe06Bq84XKA1gSUZNbzQ3kh790fCLVzIy-S4QU0QErSwK5S5lTu2kgMOh5ssXfZgn9vmCbSq44Bkx3AukqGU3OygJs5UzzJDZZJP0Esf2mUZiQbm9497YM21LVeVSGtDA1RwTAjD6C1ARLWYqbzgB6UXinVwZL8lY3dM0YyOTgILODMNhg8Mr0Ap4S79N_K6_L-JTErlzAS9mC7Cp9vUth8Q07VcLwshXgz5G7NT7_8EAfzCLnfGfG5DfEidvtVP5TqQZE0C5PzlEVR9kczJSA4X1FA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/44f6e3950e.mp4?token=dtLEjJKBH0ycMf2gw5LEH2BQkY42NwH0BWysIDE-Gz9ipT7O2NDimMKGH1EBe06Bq84XKA1gSUZNbzQ3kh790fCLVzIy-S4QU0QErSwK5S5lTu2kgMOh5ssXfZgn9vmCbSq44Bkx3AukqGU3OygJs5UzzJDZZJP0Esf2mUZiQbm9497YM21LVeVSGtDA1RwTAjD6C1ARLWYqbzgB6UXinVwZL8lY3dM0YyOTgILODMNhg8Mr0Ap4S79N_K6_L-JTErlzAS9mC7Cp9vUth8Q07VcLwshXgz5G7NT7_8EAfzCLnfGfG5DfEidvtVP5TqQZE0C5PzlEVR9kczJSA4X1FA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
مصاحبه جالب و جنجالی یه پسر نوجوون ایرانی که در حال وایرال شدنه:
🔴
خبرنگار: اگه یه دزد خفتت کنه، موبایلتو میدی؟
🔴
پسر بچه: آره، جونم مهم تره
🔴
خبرنگار: خب اونطوری ساعت و دستبند و هر چی داری ازت میخواد.
🔴
پسر بچه: آره ولی جونم مهم تره، اگه ندم به قتل میرسونتم.
🔴
خبرنگار: فرض کنیم آمریکا خفتگیره، الان یعنی ما بیایم موشکی و هسته‌ای رو تحویل بدیم؟
🔴
پسر بچه: وقتی چاقو زیر گلوته و زورت به خفتگیر نمی‌رسه، باید هرچی میخواد بهش بدی، اگه ندی میکُشتت و بعدش خودش وسایلتو برمیداره.
@News_Hut</div>
<div class="tg-footer">👁️ 20K · <a href="https://t.me/news_hut/67144" target="_blank">📅 17:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67143">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/1012800172.mp4?token=qM_RJVhXZJ3lknjnx7cLE0EENGWY1aRmS43qke-p3-YoBq2F-rIwVCoac7Dm--v-NjavRwGT1aH4NBttxfYib7DOaJmXARzqLiWx3ogxAcmoTNjh3ds_7XKph35Ez6VfGdzTYWjppUVprNfFCpYhXpFyrYCCUlxA4R3r1TWctLiMveyqYO5ruDD19V69KgjphUh7KXmu7o7_zq27PFNmhnZU1nJ09NT8TIJJZjscdL1gkzc74ck7t7dPUtgw2JJLyZ1GJ8OPrje3Q55iQ6bpG3zccV8Npr7m1c3_oViIaVgTiK-ps4V7i3bi3Fn6_7SFCihtA0pIdfjOvMvDQVCRFw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/1012800172.mp4?token=qM_RJVhXZJ3lknjnx7cLE0EENGWY1aRmS43qke-p3-YoBq2F-rIwVCoac7Dm--v-NjavRwGT1aH4NBttxfYib7DOaJmXARzqLiWx3ogxAcmoTNjh3ds_7XKph35Ez6VfGdzTYWjppUVprNfFCpYhXpFyrYCCUlxA4R3r1TWctLiMveyqYO5ruDD19V69KgjphUh7KXmu7o7_zq27PFNmhnZU1nJ09NT8TIJJZjscdL1gkzc74ck7t7dPUtgw2JJLyZ1GJ8OPrje3Q55iQ6bpG3zccV8Npr7m1c3_oViIaVgTiK-ps4V7i3bi3Fn6_7SFCihtA0pIdfjOvMvDQVCRFw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
یک تحلیلگر ژئوپلیتیک چینی می‌گوید امضای تفاهم‌نامه توسط دونالد ترامپ، بیش از آنکه نشانه کاهش تنش باشد، تلاشی برای عبور از «گرمای تابستان» در منطقه است.
🔴
به گفته او، با وجود امضای این تفاهم، نشانه‌های میدانی حاکی از آن است که ایالات متحده همچنان در حال آماده‌سازی گزینه‌های نظامی است. این تحلیلگر معتقد است حدود ۶۰ هزار نیروی آمریکایی در منطقه مستقر شده‌اند و مقدمات لازم برای هرگونه اقدام احتمالی فراهم شده است.
🔴
و پیش‌بینی می‌کند در صورت ادامه روند کنونی، تحولات جدی ممکن است حداکثر تا مارس سال آینده اتفاق بیفتد یا حتی ممکن است از همین دسامبر شروع شود.
@News_Hut</div>
<div class="tg-footer">👁️ 19.8K · <a href="https://t.me/news_hut/67143" target="_blank">📅 16:30 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67142">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=DzpCmiouPzPLbG_YBleSkuSf5qpo3RPwJmwkUhIhLZpc_hjy1CaKXHY6EhdzHezfKphvzdRILZg-QytMfnZD0I-3uUufFRv45IgQ6qGz3XWOJb6UVsChif_4NN0ULBOfRZscypqq02vcHhRv4hGyGBghYs1NJ3ybWrGoTa7E1AkUSnVC29b3Ts3QQ2g0DIaDpv1-rlQAeP3lWUT3-AsyHxK46MMGWukMnSdrTLR0x7TBoNQcpvXI9KQgrGhISAj3z_0723kU0d-suGNfjaDgrfUno6KHeNnNVNOcfADMoIzoRM_Bfw9fUpe4SeLMC-UjASJoJoONcYY551gmuUXJBw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/b14da1a69e.mp4?token=DzpCmiouPzPLbG_YBleSkuSf5qpo3RPwJmwkUhIhLZpc_hjy1CaKXHY6EhdzHezfKphvzdRILZg-QytMfnZD0I-3uUufFRv45IgQ6qGz3XWOJb6UVsChif_4NN0ULBOfRZscypqq02vcHhRv4hGyGBghYs1NJ3ybWrGoTa7E1AkUSnVC29b3Ts3QQ2g0DIaDpv1-rlQAeP3lWUT3-AsyHxK46MMGWukMnSdrTLR0x7TBoNQcpvXI9KQgrGhISAj3z_0723kU0d-suGNfjaDgrfUno6KHeNnNVNOcfADMoIzoRM_Bfw9fUpe4SeLMC-UjASJoJoONcYY551gmuUXJBw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">مهریه‌خانم‌چیه؟یه‌پهباد‌ شاهد بخوره‌تو‌قلب تل‌آویو
😐
@News_Hut</div>
<div class="tg-footer">👁️ 20.1K · <a href="https://t.me/news_hut/67142" target="_blank">📅 16:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67140">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Mp0K3CQP9kYYxhwqQuvnWHk7zDk8B52yRNQNTYLIXt2lFhaOL5SomgCN_sAmP7CbvQu1CbRvvNYe0Jd4BecDjU0qqEycEmkITpNewVFNecJmEFPj44ojMb_yADckKh3FnnCMp14Vk_wgjaZMKfoxgvyjaWbn1g7RBB3ZIKRGQWPwGrpfLy8_d5YUWN-Yw7XdxkGn-kN3wmUcl9ww-ZPZgUmkXP4NLv16CYwxTcVQxJSKA6Tw8tZkNAVis-Y4lJ5WlUtVNWx7wvYV0gYQvmMhdX4QaTDf5Ev1xYHOTujJdb0T75Uw4_o8V9BfgQIvor_gQnwBs2HXKoE0r5YBpoGknQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FaM9kkpGOZKEecBpT7lAQheTXBdJT4kZ8RggOkZUtsowEeUXoIVo5chZRCxrmBJIMSN9BxBqIDq6XXx9A-fs21T8Um5APjCfvDJ64gz6k5jx-hkZEW9dU1b90vh4j9MX8DePqjDrZ2SqnD5KBQvksmkAoF0KMoMNKUavhx4PTVCeBDrTCaw6GnZNN9O6pAoevdUksYeVkTcIkIugc_Ck4ttAvPt60EpJkugWG5dkGoIkR47QpIIzWUUiUYfV6eBSHcSM4kB-0o5mDWTH5pRDcqi_wZqdvkpFQMIIxuet6fK-bvgd_CypWqVZAt0oi22I4aVlsx2yhiMMmPUI-jUWeA.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🇮🇱
کاتز وزیر دفاع اسرائیل:مجتبی خامنه ای برای کشته‌شدن نشان‌گذاری شده.
عباس عراقچی:هر تهدیدی علیه مردم و رهبری ما، پاسخی قدرتمند و فوری دریافت خواهد کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67140" target="_blank">📅 15:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67139">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/dOe1rSmrRrGf0bIx1B7mzJ2YWsoT3hZ3ZY1VSgeSv8htHJc4NHJMX3JxmxIRUfe4T2_HmXT8di4GlrGRtEUPtGUGqZt5_iB2JmHuEZyeNFHtfPWeUgMOKeUJCrFgzwJps4oIFTFkuhq5p6Ybknce8Lot_UUOx2ya0FYLq5PARZTAQe9UVHW0SfPRerQ1fxUnTUHNNcPsDSgYdl3rgYsa0G0Wz0fB0sV7EVacWBbTe8FSNOu1fbLaSnGUVyuSW--axHacVEr3bFEAsA2XJ_HeNlL5Ed8eQzS7-MXlUhD62birnigzeffwazUMDrt47mwdu-LnD2A14O9YovJlAk9_rQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
علاوه بر ناو باکسر، ناو USS Portland (LPD 27) نیز وارد غرب آسیا شد، کاربرد اصلی این ناو انتقال خودروهای نظامی و تفنگداران از دریا به ساحل است
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67139" target="_blank">📅 14:59 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67138">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j7rgTqRlzFlgtxsC3hhV6z_ovB4VJ4wToKuh4-DzvmJPKkgE9RvDSARB_LjJDj2UD-Hx1xHytVqY9Nb40QUck6GYXt_-s9Fwy2PiEZoavT7p6-Rfx0h1fhJg3Fytpu9CsZ0afF-edcjmRuy7m1kYWhCEvxsDDz0M_ljrPVIrzdO4zapjKZ_qY9RM0tz61XSRFpTttBfr1AIWw0c5F5k78AvsrmOlRsAk5X3vFmQy4SnfqaUVx_nT3yz5Tc1OdEqTwDyZawmaUdY_JgD4PBf-Fl6oJKmpMHdItx4Cz60jhC-VO1eRsubufBC9i_7un-UAw07na1Q2bOiaiyaQEVmbFA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
عراقچی:
مفاد تفاهم‌نامه اسلام‌آباد کاملاً واضح و برای همه قابل مشاهده است. رئیس‌جمهور آمریکا متعهد شده است که دست‌نشانده‌های خود در تل‌آویو را خفه کند. اگر آنها از ارباب خود سرپیچی کنند، ایران آنها را تربیت خواهد کرد. هرگونه تهدیدی علیه مردم و رهبری ما با پاسخ فوری و قدرتمند مواجه خواهد شد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.9K · <a href="https://t.me/news_hut/67138" target="_blank">📅 14:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67137">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/GBWI9fSRFurjZ_nkakV3SGv5TlTsyb65--1fMs9B9_4zODdffku-4-eUpcRJyz22JstUpxVeL1T9YOjgXnlz6zNNUuPXPpBrfDcR7GSm-7n70WVbRdizTHtu0EnMgPjqI7Kh6BJsyu8J-0JLS3SahABynDvSsF3POwWYvdVPWopPEezEe-5zufLHQ53CAy5_Kh0CpS3cQziYDGq2BAv9ln04ptTxRTtxDKFjnd1rwgu4AmNuCYcLST5InV-o_jpy6aidDkN-0iWSyYhaae8HMCIIwc5hb8AKkERU80bk1y0nMciE8nQfGOu2QBGwVMrjYvSzDMOgufeWvdXABftLaQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
مرندی:
ایران به سرعت در حال بازسازی زیرساخت‌های غیرنظامی خود، ذخیره سازی منابع حیاتی، پیشرفت سیستم‌های تسلیحاتی جدید، جایگزینی هزاران تله نابود شده، به کارگیری فناوری‌های نوظهور و گسترش شبکه پایگاه‌های زیرزمینی و مراکز فرماندهی و کنترل خود است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67137" target="_blank">📅 13:45 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67136">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">🚨
🚨
‏رویترز به نقل از یک منبع آگاه:
گفت‌وگوهای فنی غیرمستقیم میان آمریکا و جمهوری اسلامی در دوحه آغاز شده است
قطر و پاکستان میانجی این مذاکرات هستند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/news_hut/67136" target="_blank">📅 13:11 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67135">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=OjDJaIsOui6p_dNn6sXkK_kvI6QuCjSwa3waiYBBpJe8JV2ZKsr5FbZWLn251vhFvjYtmr3Y9WSw6zOY6hN8IrxvONiz-mm1ucKumL9n47IWSuRiWoGa7fjYhnBInBkYhASjhEQRt12Zg1yzslIRBpVSWKhclwUIvsfTRGHjd5IfmMs0xT2ff_S6vIMx_SX-AnuWs6hxp1889l9ontWBGfaC03ypYkIvnf4jle0ddX6-dr9W6rpbYXOnbex2X6iQseGAC_dvHtgVgq4FyrtGjyLjyQ4fiAlVnuLXL1WVqHIQiOK7fIkGMfTmfE0VD-tGxjrroqqn68JdzzaQejCrLA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dc573e7486.mp4?token=OjDJaIsOui6p_dNn6sXkK_kvI6QuCjSwa3waiYBBpJe8JV2ZKsr5FbZWLn251vhFvjYtmr3Y9WSw6zOY6hN8IrxvONiz-mm1ucKumL9n47IWSuRiWoGa7fjYhnBInBkYhASjhEQRt12Zg1yzslIRBpVSWKhclwUIvsfTRGHjd5IfmMs0xT2ff_S6vIMx_SX-AnuWs6hxp1889l9ontWBGfaC03ypYkIvnf4jle0ddX6-dr9W6rpbYXOnbex2X6iQseGAC_dvHtgVgq4FyrtGjyLjyQ4fiAlVnuLXL1WVqHIQiOK7fIkGMfTmfE0VD-tGxjrroqqn68JdzzaQejCrLA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
این کلیپای محرم چرا تموم نمیشن
😂
@News_Hut</div>
<div class="tg-footer">👁️ 23.7K · <a href="https://t.me/news_hut/67135" target="_blank">📅 12:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67130">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/WgHfYTRA7r6BVwECCg522WXLb1ghfaDSkjOQ0gBk-BNICve7towPGRAPC6NiYCawJqtmqF0yQXYt4vEAgVulMpLqge8c-D0sw5QkBvI08LC6b310_36tPYTYNLDqIIm0Oh97aTUotaNj_bykJnUQjGjlyiq_XFEV1_Bxo6aBYF86zFkflcMtnzqc6TQrdcNb7bcRYztgqDX8SBntKmAb0fU57WuDdd4Trdev3NSsMbveIZCS5FseDHoBo49osw5g2Q-XdyjJNSL0f_b2G7q07DY0TjQ3fi3iy0c_surPDQinPf4ZBs3UneOuIvE-WUOg1zNiXINAPncSfncZoKpoyQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/f2sEsy9z2-6rlaCVVCMorN69o0qKeu8b2CdGPDJ_7w0uCP8EbMEDUItfczUlDXNkjaec7CIMeVMd7yrdEaWR1jkXPPvQw2n1M3f5RrfCWafQm7SxExZ4q4cbtFWEbIe5lUhOVD-1X-rjB_6LqzDBSW3lynatHirDsdX_82zU1VNQUK11xFGy4PcNdUAxvP0BcMNbysBrGv3Tnp1zOj31Ecbpthn9RrvDAqJijc7YXIydBd5JAptAs63Maj1BjxKpj7BgE1P8VXw4Oz5_O-hWodyrm2xwO5PylPV4Jgt1m3SbAjrFjXQIMcwO5ByZoKE8I9TaLcJSh1PpX6DHjbxzHQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=Izk8JpayC207i5Y2158vkX8m7mX-Lfx1ZRRK6F02jzrNcnQmt4amZSIxANYz-U-ZIPzF-5OzNDJkFF5UPK2G_2rjf6QGIs7jgld2xS56yYlJQ3IopvUkU9DAVvnn_KIwWJf6kkDUrN9fyCsqtBzpkf0qzC-g4Qp4Ivjp-X-41Ll2AS-N2DnbI7sqYlXYgbb4P4TpRwBDig_e76ZeedpjtXJH5fP9rD-ErV4bRBC_DsNPI229DFqhhGOjy7OehB6Fa3cQ9Ki7Ud01_T-mymBAk1uK-Mn_XSZ-xI9ky55abLDP0Ky2T5yDBsxzp8s5i24Kk6fYr4Ihm2OqEkW46uPcBQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a1c8ffd601.mp4?token=Izk8JpayC207i5Y2158vkX8m7mX-Lfx1ZRRK6F02jzrNcnQmt4amZSIxANYz-U-ZIPzF-5OzNDJkFF5UPK2G_2rjf6QGIs7jgld2xS56yYlJQ3IopvUkU9DAVvnn_KIwWJf6kkDUrN9fyCsqtBzpkf0qzC-g4Qp4Ivjp-X-41Ll2AS-N2DnbI7sqYlXYgbb4P4TpRwBDig_e76ZeedpjtXJH5fP9rD-ErV4bRBC_DsNPI229DFqhhGOjy7OehB6Fa3cQ9Ki7Ud01_T-mymBAk1uK-Mn_XSZ-xI9ky55abLDP0Ky2T5yDBsxzp8s5i24Kk6fYr4Ihm2OqEkW46uPcBQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
تصاویر منتشرشده از پایتخت ونزوئلا، آسمان کاراکاس را در زمان غروب با رنگ سرخ و نارنجی پررنگ نشان می‌دهد؛ بر اساس‌گزارش‌ها، گردوغبار برخاسته از زمین پس از زمین‌لرزه‌های اخیر با پراکنده‌کردن نور خورشید،این منظره غیرمعمول را بر فراز شهر ایجاد کرده است
😂
😂
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67130" target="_blank">📅 11:58 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67129">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/c160c90364.mp4?token=vXD9rt2GjZsIYkFX0TNnU5RfYsssXvAJxFw3-v2uyIaXIWspZPbJavM_fWLWcMAXVvnxTlKSDMEtHSe_pxOSXoEvwu4jEX3a2ilnp-GwmyhHJKzmiLxm52SuGAY7JsrvKjTifkHGnfRh-reB1wDPp6TeKw-J4zxF1X3PEwE9_4D5MzPGxIbw3qmuNu1gRcw2Gc_bjAP5PRg2soA6DwkyFk1OoeBHhU7t-ZBcRD6oVFHRG_qHBP_ANyFX0gFmVfQpy9srDPmooR3Im3Vx-3qiA1UxCXMwTubi1JKldbMiaSesuz3jrygJx5Luy6jpqbBYaW7taHEHGcTwYuhyIGKDQQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/c160c90364.mp4?token=vXD9rt2GjZsIYkFX0TNnU5RfYsssXvAJxFw3-v2uyIaXIWspZPbJavM_fWLWcMAXVvnxTlKSDMEtHSe_pxOSXoEvwu4jEX3a2ilnp-GwmyhHJKzmiLxm52SuGAY7JsrvKjTifkHGnfRh-reB1wDPp6TeKw-J4zxF1X3PEwE9_4D5MzPGxIbw3qmuNu1gRcw2Gc_bjAP5PRg2soA6DwkyFk1OoeBHhU7t-ZBcRD6oVFHRG_qHBP_ANyFX0gFmVfQpy9srDPmooR3Im3Vx-3qiA1UxCXMwTubi1JKldbMiaSesuz3jrygJx5Luy6jpqbBYaW7taHEHGcTwYuhyIGKDQQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قلعه‌نویی
:
خوشحالم که بزرگان دنیا یعنی آقای مورینیو و
تریلی هانری
از تیمی که من ساختم تعریف کردن.
😆
😆
@News_Hut</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/news_hut/67129" target="_blank">📅 11:33 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67128">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Fe6x5I8AbHXRbs6NOXKX4T540TCO1Bcos27W-ywOjolq_Ok2QjkeWVQWXfKY-wVjnSH60yLcX0a-Ttou88PLxpQf5WAoZZ4jQrwQcgavvF3ppqgUsCpxAv0fRm5ffTvigAWffuYnZJZv43V1v_reSnGn2ewFMH0UdgCV-k2iINZZf72DyQAYPqxFJX9G6diClH47oXzI-X21Tym16uG8GlV_RWzRD6xL0B49onfbVWgUQduOqjewJZz4_OdlEN0nVJrliUCYlJY_MtZ4_4H9OW4bcC6yqbQzERgPQSakDmPCBSOrOG0ktG690aYxQ25YYUHPKfMnNexjj8yp8wHpmw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3408dd458e.mp4?token=Fe6x5I8AbHXRbs6NOXKX4T540TCO1Bcos27W-ywOjolq_Ok2QjkeWVQWXfKY-wVjnSH60yLcX0a-Ttou88PLxpQf5WAoZZ4jQrwQcgavvF3ppqgUsCpxAv0fRm5ffTvigAWffuYnZJZv43V1v_reSnGn2ewFMH0UdgCV-k2iINZZf72DyQAYPqxFJX9G6diClH47oXzI-X21Tym16uG8GlV_RWzRD6xL0B49onfbVWgUQduOqjewJZz4_OdlEN0nVJrliUCYlJY_MtZ4_4H9OW4bcC6yqbQzERgPQSakDmPCBSOrOG0ktG690aYxQ25YYUHPKfMnNexjj8yp8wHpmw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
یک آخوند:
سازمان انتقال خون باید خون‌های زنانه و مردانه را از هم جدا کند زیرا قاطی شدن این خون‌های نامحرم با هم در رگ‌ها موجب ازدیاد گناه می‌شود.
@News_Hut</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/news_hut/67128" target="_blank">📅 11:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67127">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4d22600661.mp4?token=lsj1QQsaKs_ALZ0d9IZ63SigcQU7eYjyuO9cscvqYi45cWnoiERFZZU3gYEdnSmhlPBQ8ZpbYuClEKx9sC8GeA2jyU66Ap_32ZvrFyGan4lFQN88Y93TTw4DHXyTXpm3fixeq7BoZF9wlbnEPpctMg19NEG-rNE9G2m2p2qNT54ZTSqEIkcJKjRvswf2PoRfIpFkc4CteAukXVoallyBod1svq0pMOExFaSUb7sYzu0OInxUnvlYzRDw5UUZ8ssHS0FtsdLbHgiv2yEWMmvrYM-F2TM54qhEQAtFInyxvdwrMQgyEveCC3BDW3MpjWwNxCf7q_FSkiC8mPjMIUal4w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4d22600661.mp4?token=lsj1QQsaKs_ALZ0d9IZ63SigcQU7eYjyuO9cscvqYi45cWnoiERFZZU3gYEdnSmhlPBQ8ZpbYuClEKx9sC8GeA2jyU66Ap_32ZvrFyGan4lFQN88Y93TTw4DHXyTXpm3fixeq7BoZF9wlbnEPpctMg19NEG-rNE9G2m2p2qNT54ZTSqEIkcJKjRvswf2PoRfIpFkc4CteAukXVoallyBod1svq0pMOExFaSUb7sYzu0OInxUnvlYzRDw5UUZ8ssHS0FtsdLbHgiv2yEWMmvrYM-F2TM54qhEQAtFInyxvdwrMQgyEveCC3BDW3MpjWwNxCf7q_FSkiC8mPjMIUal4w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
نظر ممدانی شهردار مسلمان نیویورک درباره مرگ خامنه‌ای
@News_Hut</div>
<div class="tg-footer">👁️ 21.4K · <a href="https://t.me/news_hut/67127" target="_blank">📅 10:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67126">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=B7DvkEMYkJAUEoMfEkgXFI3i17DFvyJhuRlMKuN7SRTlsVZ9M97kOZ52jQHfXqkCZIKDxN3uL44dytboXCMLlqNXLx-89d6WmIB43BRZ8m1thIFGGEMAnoMFJpsMT3-bbA4GnJ_KWv1yiBiiRqGZfBueYf73YZaDIXrSlTe_LthbyLYyjOlf4a7ikglqzezffjapmgCCQoWrofBUOk5j6bqSregGCUnQ5a4vNiGxPNsivwaTJpTIszdinXQ6zpifjdQMQLdJnmIJT-khuqaA3tx0OkVnfoiiiOlQi8L2qZUoOhqdrB-ltIwWQyr_8kGxFNHbvff6xPKNEX_O2UNjjw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8383f0c682.mp4?token=B7DvkEMYkJAUEoMfEkgXFI3i17DFvyJhuRlMKuN7SRTlsVZ9M97kOZ52jQHfXqkCZIKDxN3uL44dytboXCMLlqNXLx-89d6WmIB43BRZ8m1thIFGGEMAnoMFJpsMT3-bbA4GnJ_KWv1yiBiiRqGZfBueYf73YZaDIXrSlTe_LthbyLYyjOlf4a7ikglqzezffjapmgCCQoWrofBUOk5j6bqSregGCUnQ5a4vNiGxPNsivwaTJpTIszdinXQ6zpifjdQMQLdJnmIJT-khuqaA3tx0OkVnfoiiiOlQi8L2qZUoOhqdrB-ltIwWQyr_8kGxFNHbvff6xPKNEX_O2UNjjw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">😂
نمایشی که قراره بزودی از عرازشه ببینیم:
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67126" target="_blank">📅 10:00 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67125">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/m9s4ZLeidViouwspS29VZQWUb9OLmXq8TBiVblSvBCYAWUq0NQh2L8wX_mnciqU1oI6kq_5b_Mz86N29GFllemVM75psddktsGLlbqCsPMVO3_BjeC3mKyLGKdh7HYzHrR1vhuvdEzZwXnzwXGR2wtNSckHy3s-JmoFZAYRrskXqXsks575UDKyVHE_NZp-FaHwgCcij17Vq61IFD9yccHxzGbEHxdfEsSbnIdiUPutYPk9iENonxa3gtMCfV67R3byChbk93HqccHhZThn732JZOSlxAUcsKnDd7TXFJ8NMMmGAuhl8EucO6tjVu2DQKdfPrUmiGXeKZaxEAstaoQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
وال استریت ژورنال:
به گفته مقامات آمریکایی آشنا با این بحث، رئیس جمهور ترامپ بازگشت به جنگ تمام عیار با ایران را بررسی کرده و در روزهای اخیر چندین گفتگو با وزیر دفاع پیت هگست و رئیس ستاد مشترک ارتش ژنرال دن کین در مورد حملات بیشتر داشته است، اما تصمیم گرفته است که فعلاً به مذاکرات دیپلماتیک ادامه دهد.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67125" target="_blank">📅 09:28 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67124">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PXMg4jl6JTzkrJ_ke_Eu_HriC8fRS-7NUDcP1wCtIjyy1OYlzQac4QkR4mzXRn7BgN_JX1QuQjHd5EcmX4kDnKqm089UMIAg0RipG8BOp3_N_jJNBvdcxK9kSEmQjaK1w5JDwng4Ykk-SVl_BdcBfSG2zGUX8C38pAsdABolt7L4jdsgfggb8RCah-_TvKSaxpggAha1b5B1GI1BE_LmdWsSfYXykEjt0tl4ExyCyY2i8mXDv_zbcdPsubG04K6qC4HA63wOWP-Hdvwsb4b_AQzHdGyKEh4pRIVymlGoqQJHlRn2wDN2XhhPf3JTaSAN81nW-vTMwo6jOMmV57r-vg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
فرماندهی مرکزی ایالات متحده:ناو آبی خاکی USS Boxer آمریکا شامل ۲۲۰۰ تفنگدار دریایی وارد منطقه خاورمیانه شد.
گروه آماده به خدمت آبی-خاکی Boxer (ARG) و یازدهمین واحد اعزامی تفنگداران دریایی در حال حاضر به عنوان بخشی از یک استقرار برنامه‌ریزی شده در خاورمیانه فعالیت می‌کنند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.4K · <a href="https://t.me/news_hut/67124" target="_blank">📅 09:01 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67123">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید  با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67123" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67122">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/T7pF7U4OkTN8YDlHxlcsblBrSN0ior7u8u2cXoTff9TRb_2rxukTN_8_BpIVFUQUUFU4tFA4dIUn6bwD-egFdiNAGFwL_DkPkYRUidRPLNT3Aapw9fSPvnbTTTkxNiPh4XGflN76VFxb6SemFIlm8BNQOUbapxigBuOKgUlnxYHhdM2V6flwpdsTBVAJwt6KSjtdnJtt2v4yS4WMpkDRv1BzKorDMlwvZqkfVd8GkAKMjDo_AStvvBwwMoTJ3AS16NrTV2LQefk866aC5VdReDDhSIfBgbVxc8Ml6-8-XU4HyLa6q68iJfHSbPMpTrEGFebtS4bPpa-aFsVpKJSSIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">شایعه شده ایلان ماسک قبل اینکه میلیاردر بشه تو فاک بت جوین داده بوده
🔥
با آنالیز حرفه ای ادمین های فاک بت ، بصورت رایگان از فوتبال دیدن پول در بیارید
با فاک بت ، حرفه ای تر شرطبندی کنید
❤️
Join Join Join Join Join Join
Join Join Join Join Join Join</div>
<div class="tg-footer">👁️ 23.6K · <a href="https://t.me/news_hut/67122" target="_blank">📅 02:39 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67121">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=PMNi9GEVMoLPaK_Jl2SucfjC7T9SuNFfVXmWqSE3M0jwdPeqopUF7sY3abkf9johav0PiuYoWFW_CSOxj3ixUCAWScyjdNmCMtl5RW53wwmz5QlzyHLoESStwtUGakgmpXttLFO4eil1Io78ZcuGHHrsh4P5xRLXyKzGa0cuC8yLwDaC_yNutdeOCbTLzR7r2ef3OzvG39JjYG-tXTMTPWzL_5-rnQ7TFFRCC_Ui0e4oE3M8eraz_0NNmZdBVNGT2LZ0rGDmDqteYZpGUgmQ1Cg-8h5dwHoJdDoHYpyTyokzqOM6Y_LzlRik-68ee6i268cbq1r973FQCrqnWTkPcw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d6863c3306.mp4?token=PMNi9GEVMoLPaK_Jl2SucfjC7T9SuNFfVXmWqSE3M0jwdPeqopUF7sY3abkf9johav0PiuYoWFW_CSOxj3ixUCAWScyjdNmCMtl5RW53wwmz5QlzyHLoESStwtUGakgmpXttLFO4eil1Io78ZcuGHHrsh4P5xRLXyKzGa0cuC8yLwDaC_yNutdeOCbTLzR7r2ef3OzvG39JjYG-tXTMTPWzL_5-rnQ7TFFRCC_Ui0e4oE3M8eraz_0NNmZdBVNGT2LZ0rGDmDqteYZpGUgmQ1Cg-8h5dwHoJdDoHYpyTyokzqOM6Y_LzlRik-68ee6i268cbq1r973FQCrqnWTkPcw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
کریس رایت، وزیر انرژی ایالات متحده:
ایران هنوز به هیچ وجه همکاری نکرده است.
جریان نفت از طریق تنگه هرمز به لطف ارتش ایالات متحده است. هنوز هیچ همکاری از سوی ایران صورت نگرفته است.
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67121" target="_blank">📅 02:25 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67120">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RXPvhAXqs3XhWB8OZ6t4tQuqTy2H4YNmo9MVO0bYzg8LWk7znRTr3hRt56MIxtJXFSWknpSV_W-HGwRgaU6i6zxskqzIhEcpvcuIyo5r0uQzpj3N5_PVJyBo4uptoJtoABf4ETJpyUi6xewxNsfcxfJYKmzRXth8H4yP94s0cHuYZpzw915ByXKWStABglPlOZPVRRaaeWOcXd7ViAyGyDFfV5pCu5dSbIhi0PEDLEPm3Fr8G5-8-ZxtLnBO_eC8XbH_Rao38tnvSXMSYLCtXziWIJBYUlRDOBEljdZrsOnQfYdX5iv4SK9Un-HR1f9UZK3XC07q76pREIc6XnG3zg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">❌
تصویر منسوب به تابوت علی‌ خامنه‌ای و خانوادش
@News_Hut</div>
<div class="tg-footer">👁️ 23.4K · <a href="https://t.me/news_hut/67120" target="_blank">📅 01:31 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67119">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=UsQj7XY5z_WRaCFaydR3qVNQ7E41hmEYwKiVcS_WSV6zItfOfElF_NvS6-r__aRJdqtnkfI9Tz-lLqcwu-H0Rh2w_4YG5sglpAmSQ_fz9TC8iVjYXK1fpQVNq0R3W-lWmYhW6x_Vx0TKiSxena733yNMlrgTVuofJIDuxJ2dnDTKrWWOcFdEcR8xWLjcBFQW_fWUuqzahXVc7iO8d0afQN3IPTRI_v31X9corqXND7QaXhAi1fDNF68GL6dTsxvuYMTe-7-M7AdB3apK1frE1nwKB8bcxjuhwYzEjwQPGWvP2ekZj3YQhSYNpsHaMLAujravx_RBHg7sDG90qc25Tw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/387a5265c2.mp4?token=UsQj7XY5z_WRaCFaydR3qVNQ7E41hmEYwKiVcS_WSV6zItfOfElF_NvS6-r__aRJdqtnkfI9Tz-lLqcwu-H0Rh2w_4YG5sglpAmSQ_fz9TC8iVjYXK1fpQVNq0R3W-lWmYhW6x_Vx0TKiSxena733yNMlrgTVuofJIDuxJ2dnDTKrWWOcFdEcR8xWLjcBFQW_fWUuqzahXVc7iO8d0afQN3IPTRI_v31X9corqXND7QaXhAi1fDNF68GL6dTsxvuYMTe-7-M7AdB3apK1frE1nwKB8bcxjuhwYzEjwQPGWvP2ekZj3YQhSYNpsHaMLAujravx_RBHg7sDG90qc25Tw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⁉️
بخش سانسور شده صحبت‌های قالیباف در صداوسیما:
قالیباف در قسمت پخش نشده این سوال، می پرسد: خریدهای قبلی این اقلام که در طول ۱۵ سال گذشته انجام می‌شده، از کجا بوده؟ آیا ال‌سی اینها در لندن باز می شد یا نه؟ چرا الان مهم شد و این حرف‌ها را میزنند؟
🔴
چون نمی‌خواهند بپذیرند با مجوز اوفک صادرات نفت انجام می‌شود.
​
🔴
این قدرت جمهوری اسلامی است به آن افتخار کنید و پای آن بایستید. این سند شکست آمریکاست و ما با عزت آن را انجام دادیم.
​
🔴
گویا حداقل ۲۰دقیقه از این مصاحبه پخش نشده که نکات مهمی را در خود داشته است.
​
🔴
برخی قطع صحبت رییس مجلس را با بازگشت روزی‌طلب به معاونت سیاسی مرتبط می‌دانند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/news_hut/67119" target="_blank">📅 01:18 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67118">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=lryp4U30zitwUXKvfmE_3NeNzjMRStZLWETs9CtdehiCpEa6Je_TNy3rRS63qj38rQlOh1q_adZUQEPlqXhhA5RkHtli3qXWK3U8GS53EKKjlncjH_Dr-U3YqLeAD2ABhxztT93tdSB3JqqxR1i_lzbvxWysX7SCQ64Yg1MOoQ4ao4LINy0-iZFmzX9CimOwiCbh5mBrc5l1ZcJIgQnDqTfC2iMl9-Mie9Cxg4QSB770Kizwu2rmY_9L6YTzofiVRFwNmrMX8S3fTPQC2pnuZPTj2aWdfk6N8gtclZdFPNkjTguz-KC4cyXNyft46_g_oNHWQpmxE5Kh0-YlPcYeRQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce4a0d523c.mp4?token=lryp4U30zitwUXKvfmE_3NeNzjMRStZLWETs9CtdehiCpEa6Je_TNy3rRS63qj38rQlOh1q_adZUQEPlqXhhA5RkHtli3qXWK3U8GS53EKKjlncjH_Dr-U3YqLeAD2ABhxztT93tdSB3JqqxR1i_lzbvxWysX7SCQ64Yg1MOoQ4ao4LINy0-iZFmzX9CimOwiCbh5mBrc5l1ZcJIgQnDqTfC2iMl9-Mie9Cxg4QSB770Kizwu2rmY_9L6YTzofiVRFwNmrMX8S3fTPQC2pnuZPTj2aWdfk6N8gtclZdFPNkjTguz-KC4cyXNyft46_g_oNHWQpmxE5Kh0-YlPcYeRQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
❌
قالیباف وقتی گفت توافق خرید غلات و گندم در ازای پول های بلوکه شده برای دولت سیزدهم بوده است، مصاحبه اش در صداوسیما قطع شد
@News_Hut</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/news_hut/67118" target="_blank">📅 01:04 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67117">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/640225b559.mp4?token=sBVriiyV5oQEd_P8pm-ElTM61045Sj16rSrC8mrA6II4ncrNGU3oDl9hIcTRgbahqyXld-ud1tvY8G9WC3N1B3mY3-HwqJNtm3BbUIODvrGhu9TgQ2BnWL-gqdWyTCocU6Ct9h1PWX42CBXxDoGNKbHCh1rdEptJancjzRGPToDqd8YCkNHZysrbLI_b8uPNX6pX7HEuY-JhTcN0w0E8TiIEpVrI3F-fUMzVTm15ZfHpQsoiTQrJvDFmEyeBaX2gbfCmctbyNyekbebdMwL1oAC7jIoCX_ctMlnJrBSsM287CMFZgxtU41KKGS7pOThQqtjB6yQXkL6LVPJc86_bVQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/640225b559.mp4?token=sBVriiyV5oQEd_P8pm-ElTM61045Sj16rSrC8mrA6II4ncrNGU3oDl9hIcTRgbahqyXld-ud1tvY8G9WC3N1B3mY3-HwqJNtm3BbUIODvrGhu9TgQ2BnWL-gqdWyTCocU6Ct9h1PWX42CBXxDoGNKbHCh1rdEptJancjzRGPToDqd8YCkNHZysrbLI_b8uPNX6pX7HEuY-JhTcN0w0E8TiIEpVrI3F-fUMzVTm15ZfHpQsoiTQrJvDFmEyeBaX2gbfCmctbyNyekbebdMwL1oAC7jIoCX_ctMlnJrBSsM287CMFZgxtU41KKGS7pOThQqtjB6yQXkL6LVPJc86_bVQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
لحظه قطع شدن گفتگوی محمد باقر قالیباف، توسط صدا و سیما
@News_Hut</div>
<div class="tg-footer">👁️ 23K · <a href="https://t.me/news_hut/67117" target="_blank">📅 00:56 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67116">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e29288f186.mp4?token=tiz5BQz-IV4Wq0DAB9dLFsim65JxoT-07l-4cCmn1Hhysml_4AvSMVDoZaL-HINxits_qcmFXg9VMs6QFaWTaD9XI6EHmYggZMweUsNsQRdLr6gjlPSmpyH9b7saEj-WCFIYSwaD8qyJeVktk1lvEDgEMm7ymbLlFuxnaoBCR1t3TOY2LXx2s42-2gPLCXwCvmR7blZI3rFJCFKFafSO1SjNdw2w-FH8EGnK_LoV1nKwI31hGJrouVUZbRff8lDjS8rHUwe47IZLOFfnJ-CseiZqxAow5FW-9Z0o03ZysBb-DQo7c3MLeUuSdaBmfkXG88wVL-f-VPn7Yw2MLRJ2hg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e29288f186.mp4?token=tiz5BQz-IV4Wq0DAB9dLFsim65JxoT-07l-4cCmn1Hhysml_4AvSMVDoZaL-HINxits_qcmFXg9VMs6QFaWTaD9XI6EHmYggZMweUsNsQRdLr6gjlPSmpyH9b7saEj-WCFIYSwaD8qyJeVktk1lvEDgEMm7ymbLlFuxnaoBCR1t3TOY2LXx2s42-2gPLCXwCvmR7blZI3rFJCFKFafSO1SjNdw2w-FH8EGnK_LoV1nKwI31hGJrouVUZbRff8lDjS8rHUwe47IZLOFfnJ-CseiZqxAow5FW-9Z0o03ZysBb-DQo7c3MLeUuSdaBmfkXG88wVL-f-VPn7Yw2MLRJ2hg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">⚠️
این خانم، عالیه نصیف از چهره های وابسته به رژیم جمهوری اسلامی، شش دوره بدون وقفه نماینده پارلمان عراق است، او در رقابت‌های پارلمانی چند ماه پیش گفت: «کاری می‌کنیم فاسدان از پنجره فرار کنند». حالا خودش به دلیل فساد کلان دستگیر شد.
@News_Hut</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/news_hut/67116" target="_blank">📅 00:32 · 10 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67115">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e563023c29.mp4?token=G4yQIKL-eDV00T9TfTGIGTPZdIz8BpDXamCDhmEV3wuf3cQQbjpZFdXk_3xt7Bicxhq3eH7wPWA3-lDmCeSSeFQ6w05YygSv5uRhOjNg9f8q3KrHzRUwyEj7YiC7yqU21smMOQAdNRyk1KbRVK8fm6n1VrRPCSKrGw3h8kqedmgJE6w1SAJSCvSNKGETi1aRCDu1VYlBUQioCek72rTuC8PsghLHLtdRHXsAwFwBL3sq79Nhe7fFQyS6ER_fRDloVpMa5NJ9-pXJ63DpQVXgoP97SMQdlAF7Lyijv0NDEtnKa-PwNZKf_MFCLxedet8CaGdG0L-r-5oWFRD0cYoHfg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e563023c29.mp4?token=G4yQIKL-eDV00T9TfTGIGTPZdIz8BpDXamCDhmEV3wuf3cQQbjpZFdXk_3xt7Bicxhq3eH7wPWA3-lDmCeSSeFQ6w05YygSv5uRhOjNg9f8q3KrHzRUwyEj7YiC7yqU21smMOQAdNRyk1KbRVK8fm6n1VrRPCSKrGw3h8kqedmgJE6w1SAJSCvSNKGETi1aRCDu1VYlBUQioCek72rTuC8PsghLHLtdRHXsAwFwBL3sq79Nhe7fFQyS6ER_fRDloVpMa5NJ9-pXJ63DpQVXgoP97SMQdlAF7Lyijv0NDEtnKa-PwNZKf_MFCLxedet8CaGdG0L-r-5oWFRD0cYoHfg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
سعید آجرلو از اعضای تیم رسانه‌ای مذاکره‌کننده جمهوری اسلامی در اظهاراتی در پخش زنده شبکه خبر رویکرد علی خامنه‌ای رهبر کشته شده جمهوری اسلامی درباره مذاکرات را اشتباه خواند.
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67115" target="_blank">📅 23:52 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67114">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/l56Ld02TCPBDE0fpZWzhffAzUbhN8W38A9mwo04dYtaPk4_THCVV9tL59RUIAlEx1-mnCSmysi45YLfB5ma3G2MrvmuGAyZxguFk7CPslHn-t4OXS4jBATxHtxLpUUTKQu61bij1r438PPFV6KuDDDEs7RtW6Qdd_aAUwtPyDXB8Sxk62aYmFYwIHOmkq18IGWz7BZEFcdiYxVWnA1OyiHa8sqUPaAc_fmBtB8O_Ay728yYsESXeM_uQJSF9Wgtcq1jRMdjI5mDebGrkiaEZow6nj9DgGF8XINQ68-P7Y-CL7QQiM2PT_FCkWOncMu0a4v_iolI4pV_sWs5yMCoeVQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🌿
جدیدترین روش ترک اعتیاد  گیاهی
بدون درد، بدون خماری، با انگیزه‌ای نو برای زندگی
🌟
✅
ترک فقط در ۵ روز
✅
درمان کاملاً طبیعی
✅
بدون داروهای شیمیایی
✅
بدون بازگشت
✅
همراه با پشتیبانی روانی و انگیزشی
💚
بازگشت به آرامش، بازگشت به خود واقعی‌ات
💪
تو می‌تونی! ما کنارت هستیم تا دوباره بدرخشی…
♦️
جهت مشاوررایگان فرم زیررا پر کنید
👇🏻
https://app.epoll.ir/74570725
عدد 6 را به شماره زیر ارسال کنید
👇🏻
🆔
@Sahar77631
☎️
09923413672</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67114" target="_blank">📅 23:51 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67113">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1hrQMqdryH0DqDChc_Wk1wpxgefsJjCyxZavnJ2YlamnLMAZnO_DN7hn6UjlzgewQ8p58hjLHDR7tf0ue6DtDotIAV7pvfJCpAXJUSgiLk6kn1GAx1zZNAEmY7knPWOgakPW6ysMUaBQHSIy0Bh2H6lc-gcUlbW-7ewtYim1dmK0Yx9eK7F4DeRIzCXrccjSAKAXcSR_0xS7aD_nosdzef2sF19yvn5BM7sVoK1nz0ubGVEhgEI80YQUWHg_1uyX_ace7ZrOuAisFJKhxw8_9SY-Rfcjg-oyuE-rGMohcXW9KDB9MUlT_-pkZXXUdFzbL9oKXVaWU6m12Ms-uGQYOw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/706602e352.mp4?token=kJmG2bVxV7ql1lFGwsbJcGleg5mzPwNcJ31GTsv-oYGjwX7fxZUkfHAIDpVuhVloAedhgSx4qfaSGpIgly2TmM221LsIADL8T_2lExCm6rHaH588Qn2L5Rgf4JTz8WC-GO1DCYtUih1-iAT9ylwKnp3ScLid2Y_7XDdONsB3XXWDr7C6yFZXsaCBI6Hx0BiJmpgtRFEOAjQk2_gmtf17377j28wBwnBGRgmd_9Mt_ceTaBdMcSInYEGxfWxnKmQwrVFzOd4gO70qiCMHbCDXKgv4h2N4yMPE0JHhnathvBdGz7dH4frzSxquu1y4evIi-LI4x9_O4FC96iWN9CNSY1hrQMqdryH0DqDChc_Wk1wpxgefsJjCyxZavnJ2YlamnLMAZnO_DN7hn6UjlzgewQ8p58hjLHDR7tf0ue6DtDotIAV7pvfJCpAXJUSgiLk6kn1GAx1zZNAEmY7knPWOgakPW6ysMUaBQHSIy0Bh2H6lc-gcUlbW-7ewtYim1dmK0Yx9eK7F4DeRIzCXrccjSAKAXcSR_0xS7aD_nosdzef2sF19yvn5BM7sVoK1nz0ubGVEhgEI80YQUWHg_1uyX_ace7ZrOuAisFJKhxw8_9SY-Rfcjg-oyuE-rGMohcXW9KDB9MUlT_-pkZXXUdFzbL9oKXVaWU6m12Ms-uGQYOw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❌
❌
دو موشک فلامینگو اوکراینی به یک کارخانه تسلیحاتی روسیه در ولگوگراد اصابت کردند.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67113" target="_blank">📅 23:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67112">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=ovUQhbsBLl9q5JvKhC2HSYH-3DcbSSU8mKVVOX0PsqthHNIQO_lvMPxB_yl3A9MJ1f-CnhNgXjd9zP8cX-3Ofq3n6IgTsXTOvl3a47vh8zwLR3LB9-05-O6XG_mVRnNNcu8tCfxeBbpiyOQqXaeMqU5Fsaq1AP8UAl4aWt9WPSS0JPorCXnx12Rg5mM77R6lyZT9pgQ3BYWhkQsDjAjzXmpmEcz6prttr91nJUTe2nNkyeoIZ5EJhvBdS2bpr7Jgd9NZx4u1TWYuzaYJ5GwHqj812OMc484MBrFohpYgtvI3dRRF1--MV_rcZSNR4Nsjz4j21nMj1Y7zFQXIEF0UDw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/9a5fee32db.mp4?token=ovUQhbsBLl9q5JvKhC2HSYH-3DcbSSU8mKVVOX0PsqthHNIQO_lvMPxB_yl3A9MJ1f-CnhNgXjd9zP8cX-3Ofq3n6IgTsXTOvl3a47vh8zwLR3LB9-05-O6XG_mVRnNNcu8tCfxeBbpiyOQqXaeMqU5Fsaq1AP8UAl4aWt9WPSS0JPorCXnx12Rg5mM77R6lyZT9pgQ3BYWhkQsDjAjzXmpmEcz6prttr91nJUTe2nNkyeoIZ5EJhvBdS2bpr7Jgd9NZx4u1TWYuzaYJ5GwHqj812OMc484MBrFohpYgtvI3dRRF1--MV_rcZSNR4Nsjz4j21nMj1Y7zFQXIEF0UDw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
بازدید بنیامین نتانیاهو از منطقه امنیتی در جنوب لبنان
@News_Hut</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/news_hut/67112" target="_blank">📅 23:20 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67111">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=Caq0P7yDZJo2RIUefQ90uZp0X9-xpsxZ6B52qYX1WLy2gRLBedzOJPumNxN317o8Q-fJ221Fla4rlozQS46fPJfFKPWcaTF2mFxro-xsWEDH97WYT3uw_VbcAhhjJQrH5UEau_wRAaJgpw_NDEMEEe0EhnTXkewu00slrEm04rHLb6YUHANEYOp3-vevJtzRrs2Cw0zHCFdZVWVwIDrS5MOkYBEaJUFy9GNawIllrrRObZpCz8go2lOCmohNEOVRS5jI_iE8jZB5TfTzaS0i42YLr6srEs0YM2I4k0JwhhNYC9bweVwcM6bdvMPYslMH2RuhPEWQnZ7ndsy89cEqKY2o3h_g_pSVCxIaaCFWT2w8la7tJmMCndMbxhRGnK8eWkDnmRDTR1pUYBgOZl3eVAO3b7DxedkFoukkCjvFtceZR1VpokrhvbOU9cwxzkSJ9H65O7_L5Z0HHVURCwtSP3WPI43obJD9bEv0OaN2ORYkDwg_ru7G2hO9pyu1SZkaUD0t16lIfOhZejHrEzj8inWmpmX-2802fog2yVEIoQgZyVlmjveQQZqYht5-2gihPTTQt0RQzHhDxagX4_E1ZntvQxYFJ4kujlHUOxVBJ19SOjj0_F_TgyFcAjmmqhwQrHYSjVNYMcNkay_EVZ2-QumbNLswToHBoxlY3ruWYss" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6eaf19117f.mp4?token=Caq0P7yDZJo2RIUefQ90uZp0X9-xpsxZ6B52qYX1WLy2gRLBedzOJPumNxN317o8Q-fJ221Fla4rlozQS46fPJfFKPWcaTF2mFxro-xsWEDH97WYT3uw_VbcAhhjJQrH5UEau_wRAaJgpw_NDEMEEe0EhnTXkewu00slrEm04rHLb6YUHANEYOp3-vevJtzRrs2Cw0zHCFdZVWVwIDrS5MOkYBEaJUFy9GNawIllrrRObZpCz8go2lOCmohNEOVRS5jI_iE8jZB5TfTzaS0i42YLr6srEs0YM2I4k0JwhhNYC9bweVwcM6bdvMPYslMH2RuhPEWQnZ7ndsy89cEqKY2o3h_g_pSVCxIaaCFWT2w8la7tJmMCndMbxhRGnK8eWkDnmRDTR1pUYBgOZl3eVAO3b7DxedkFoukkCjvFtceZR1VpokrhvbOU9cwxzkSJ9H65O7_L5Z0HHVURCwtSP3WPI43obJD9bEv0OaN2ORYkDwg_ru7G2hO9pyu1SZkaUD0t16lIfOhZejHrEzj8inWmpmX-2802fog2yVEIoQgZyVlmjveQQZqYht5-2gihPTTQt0RQzHhDxagX4_E1ZntvQxYFJ4kujlHUOxVBJ19SOjj0_F_TgyFcAjmmqhwQrHYSjVNYMcNkay_EVZ2-QumbNLswToHBoxlY3ruWYss" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف: اگر می‌توان گره ای را با دست باز کرد چرا با دندان باز کنیم؟
🔴
کسی می تواند خوب مذاکره کند که برای جنگ آماده باشد.
🔴
مذاکره با آمریکا مذاکره با یک دشمن بد عهد است که هر لحظه فرصت پیدا کند علیه ما اقدام خواهد کرد.
🔴
ما در شرایطی با جنگ و آتش اقدامات تلافی جویانه ای را علیه رژیم انجام داده ایم.
🔴
خوب است ببینیم شیخ نعیم قاسم  و مردم لبنان درباره این تفاهم چه می گویند و برخی دوستان ما در داخل چه می گویند.
@News_Hut</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/news_hut/67111" target="_blank">📅 22:55 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67110">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3c10065584.mp4?token=ALrw1Wg1PrFhf1mO760EbWsdtK-GeuXjyayvIkCuqIDyt_G68PNH9a2ym3IN51118tt4Rk3evR_A40-gpQQfEmlbgo84NR0WHCzhKpaII3hqcpCQQ9GnbVE0kRmlvFBPf80I-qAveWCaDinaXRlQmSbTQFeeg54bWieGs_JQDuMywySGM24NIWELwRpMoLPgd-mlhf5MQ9t5Cb043KiQyngXsRq1i9azrMlltcxm0mGL42fcxWsENnCicwXURQlt5vct0_-KwMViAXXyZSjriOmZK9y75xsUYV1Q4xDK1EsUZC7KNsRwURyUpKBY5ZVRPrX6kTpn5BbzR5lLZZ7ECw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3c10065584.mp4?token=ALrw1Wg1PrFhf1mO760EbWsdtK-GeuXjyayvIkCuqIDyt_G68PNH9a2ym3IN51118tt4Rk3evR_A40-gpQQfEmlbgo84NR0WHCzhKpaII3hqcpCQQ9GnbVE0kRmlvFBPf80I-qAveWCaDinaXRlQmSbTQFeeg54bWieGs_JQDuMywySGM24NIWELwRpMoLPgd-mlhf5MQ9t5Cb043KiQyngXsRq1i9azrMlltcxm0mGL42fcxWsENnCicwXURQlt5vct0_-KwMViAXXyZSjriOmZK9y75xsUYV1Q4xDK1EsUZC7KNsRwURyUpKBY5ZVRPrX6kTpn5BbzR5lLZZ7ECw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
تعهد ما نسبت به باز کردن تنگه هرمز و ادامه مذاکرات منوط به پایان جنگ در لبنان است.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67110" target="_blank">📅 22:50 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67109">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">🚨
🚨
قالیباف:
غنی‌سازی حق ماست و خط قرمز ما در این زمینه مشخصه.
@News_Hut</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/news_hut/67109" target="_blank">📅 22:47 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67108">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=OWLy_iCPRWhjz_WOYJ3xQBjxVy69Anow88Ts9d8-OqBRa27GNrH0S0IPzMGf5-cSZX3BZU0v3TB3d-TBhAJ9xPNargygtGHKBT72P2Oty9qFWkSfY0IVL23br8y8b3BLrnOpgXks-OmlNx6_n5_cGwNny-9XcGyLagyF14q83cswfgQmIsCjUPUVQM13Rf-bdWB79oL7opjUOYL-BQmiwNfAqdxEV25gQ2-6bCc-Do26ecrYIYgLzIRPI5f5CuMmVcF08eOqZgbnm9fXJqZZGOPHMpSaU3yv__HiRwvrVv1EhtNY8XK7Pn-cDgppNlCgQByzQdfZangWZYcqYt4Htg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/205ddcc2be.mp4?token=OWLy_iCPRWhjz_WOYJ3xQBjxVy69Anow88Ts9d8-OqBRa27GNrH0S0IPzMGf5-cSZX3BZU0v3TB3d-TBhAJ9xPNargygtGHKBT72P2Oty9qFWkSfY0IVL23br8y8b3BLrnOpgXks-OmlNx6_n5_cGwNny-9XcGyLagyF14q83cswfgQmIsCjUPUVQM13Rf-bdWB79oL7opjUOYL-BQmiwNfAqdxEV25gQ2-6bCc-Do26ecrYIYgLzIRPI5f5CuMmVcF08eOqZgbnm9fXJqZZGOPHMpSaU3yv__HiRwvrVv1EhtNY8XK7Pn-cDgppNlCgQByzQdfZangWZYcqYt4Htg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
اگر نخواهند در گفت‌وگو به تعهدات خود عمل کنند، آماده جنگ هستیم.
🔴
اتفاقات شب‌های اخیر خلیج‌فارس را نقض آتش بس می‌دانیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21.8K · <a href="https://t.me/news_hut/67108" target="_blank">📅 22:45 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67107">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/745f2de194.mp4?token=q-Hi_6XYrFG60ZOBpvZHiu5SHsI3a9kyi3L4AiHGPCyaIhC-vDpaKGJftvC3tVesAiNqz4ecZzTw5DdTbW1Jd66iyMOjPoxqvPCDGm-FAGJlSkNv_XvbVvrP5RsWHXt2_DUa8rkpWKRtbajj72DXzo1jtb0gzWs0bx4s0_gDOHM3aombSGIP5ziql9x5OAb36GZHL6z-BUja1TS9f6RcT0CtsnhAum6__Eu5e35SzDu1iEm8CBPVWFNBxgwZKSkLDIrYuY_0vlCYO62x-SUXelL2i1OzbcwS3mbAr0Db202JrCzwa7I_dLokfcDWYoVHTMwxf3otrBznBTf_Cibd3Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/745f2de194.mp4?token=q-Hi_6XYrFG60ZOBpvZHiu5SHsI3a9kyi3L4AiHGPCyaIhC-vDpaKGJftvC3tVesAiNqz4ecZzTw5DdTbW1Jd66iyMOjPoxqvPCDGm-FAGJlSkNv_XvbVvrP5RsWHXt2_DUa8rkpWKRtbajj72DXzo1jtb0gzWs0bx4s0_gDOHM3aombSGIP5ziql9x5OAb36GZHL6z-BUja1TS9f6RcT0CtsnhAum6__Eu5e35SzDu1iEm8CBPVWFNBxgwZKSkLDIrYuY_0vlCYO62x-SUXelL2i1OzbcwS3mbAr0Db202JrCzwa7I_dLokfcDWYoVHTMwxf3otrBznBTf_Cibd3Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
قالیباف:
🔴
دو اقدامی که پس از امضای تفاهم‌نامه، در شامگاه ۲۴ خرداد رخ داد، اعلام پایان جنگ از سوی نخست‌وزیر پاکستان و توییت ترامپ درباره برداشته شدن محاصره دریایی بود که از اتفاقات مهم تفاهم‌نامه به شمار می‌رود.
ما در حال دنبال کردن دوران گفت‌وگو برای تحقق ماده ۱۳ تفاهم‌نامه هستیم.
@News_Hut</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/news_hut/67107" target="_blank">📅 22:41 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67105">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/GJusZV08c53TCbTJroswKUvGk_4TJohqYoOzIPwucHFkKajTmSwznHq3tCUV7vcsBD1aG3YL5xAnJQPdx_U1g66mjuNNFfWC5xKoHhvXV1ComQe-ddj8E94I4a_kS996TW3l4x29QqZYE2dgGJQ9dtskzYKT2sdDi117ziUanCOyiiQXTCMEC23zoiDwGi2pYwryIh-rZtTkkOMvo71kA_-l5RUHLFvPamvnBmxohDZSmxpsmYju36YK47IaVhlpQEjUdIi1v4AkQnu8ErhPQZJHv1FA2a4Zu2CN179sTsaS3grqhi_vP4vZMmuu9FW-c8K6Zatu0ne4n1gmeVSMog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/flKjEhR_OgOL5mqZ1BnRMDFlktdcIgJ9hQGASLINN2Ur6DjHM1-WPbooILAvL_lF910SmqxQmp4qBoyFhEi9Jg4Hy8BnkIjI13NyrmgAUxocOBEoEI6-fnC4DnrkVcSCMapDPZJ5Vg6bZn3qFommDTPzzkCgDS0vf_oM6QnK7zAf6wvDGoqQsEobs8dTTzybwbVdeljG9_laufgexhnWCtjSPwn-2VyPeYviZ_C8A3xN5FNvgjYat4U0k8r4_BzPZVhbjWV7VOfxDGdTiXXhmEOpLMaBSoGPkcEc7YmMRU_snhHUNUcQCm_hdx05-8wfKxHXb4wyxln8zUc3E1IVEQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
صفحه اسرائیل به فارسی:
چرا هر کجا این تصاویر به دیوار است، دزدی و فساد هم هست؟
@News_Hut</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/news_hut/67105" target="_blank">📅 22:18 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67104">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/lsOcJADRxuwkMnA7YLQWO3YvuYy3HRGfLNiXuGiVkKOCyNT0mPsaIUgK81PAE2MQwk-OwlQXKsfUUmGPPr8ogEHHn-qHJIzVfvVO48eApQMSFxNf23p2vOfxy2AqH6vQUlKssFit7naiqBirZipibMTGB3tAeacSKNyOulJqeotFUxU0gBV8UKgca6dXmCp7vcUBMXdlGgD1R5j5OHuCVAM_JhWA0cEtFmALMJlZV-xMkK4sgdI6FZ6Hmt2Jywd6GDLPecpgsrt9hddz-b_aONczLTCvXS0vRvTqhY4me7OnaiYEEjgYIsT7pGuNg7fvFw6ykf8JSDCIIGtrvO06og.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
وال استریت ژورنال:
اختلاف نظر میان میانه‌روها و تندروهای ایران بر سر اهدافشان در مذاکرات با آمریکا، پیشرفت آنها را کند کرده است.
@News_Hut</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/news_hut/67104" target="_blank">📅 21:54 · 09 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-67101">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rCZbmbtiTXj1aeMuPS_6gXMLD64PLgSbD_EBS3Uh6jmeuedYBy2HpQ0aUWPECM5bO4fMmT5NknWVTSJniRPu261DlQ9LD6ZsNtEADCPRxUsJ5uh2b3-scI4RDR8EBkOCjmlB98a8ZJpdOfaaY9ppvn6gEQGD3Tcrmf6LG7WmeZJ-xMXFuHgfvoWGKWbuWY5DRhPcMjSJY5B9W42Rg3gN1fDkzgl0asBoRG-tGFb9yj_nzYkNQVRcrMgjv0RQjpIFAdPVd9KSC0vgUOjnEgGd7ogfU5ZWoHb2-j10R9pblp_i1OFB7M7UofsGTO96N1vuRLzyycfE9ARKHqjAum6ikA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/e9jS8D2mL8ZTvHrw-G1fOWOD-wPtdkuIWFU_cvDQgyySDc1nsblcez-vdcaKqsCGGByFtIisPjqDDOy5l6j0L_ad1NyUcl_cmxd8YuGvgh_bV7_dESzFWqAb9ItYUkDOz676CR62JAPXYenmNy1HfVP9c0bg-fTI76MRxs252hl2YoDIfdcJ9fhKIEemkF-KR0s09p4CG9hQXlM-l5diodTe15xflB2I49K6NxKJpza5QHUHS1IQOYV4pk_s_Ql2KFA6YFKBeDtRwWxRpGsTgwkOHgcgO3SzDDmJqjfY4n-d7U7RZvPjt50kcVQOWenFtEyeUc58Y0vdYohFfNxK1A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/LUH9AxLoy65iCZWOz-42qGzEwUW-5vOG0Ipg1vTNY1XHXzGKrLBtLaCw735DZZruVMKrmNLAVQ9Wa_Qi5_2RL_ehbtOm6IpMIM0ddMUxyMskyIxNEUwiNfQEsBnKLGgtIvYaxCFq6sNiYLkTq-u2EwoBVwi9DTs8PkmuRQLpjIItVz6bccd81UjQ-0R5kxt7bftvNFhGAnuNV6WiwY7Bw7qFLCmQ-qTgq4Hy4U_wSZPRDi3w5i8OWApyzdF8cCg2Ezayu0HQV9F4sceOTYZvWjSgw6or-WVuut-o9ECG5F9i9ZNmO1xHV9kEk5AOinu02bwNdjJG8j0vHklJWrd04A.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
سنتکام تصاویری از آموزش شبانه تفنگداران دریایی ایالات متحده در جایی در خاورمیانه منتشر کرد.
@News_Hut</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/news_hut/67101" target="_blank">📅 21:13 · 09 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
