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
<img src="https://cdn4.telesco.pe/file/ErhpPt5WgizFglEtEZosEsqqoGc8CneqJQnSaNcOFM1QO7eniDBke0ZWkjVSzANW7DsWb_1di3F0I_xPFJAmT6FayXwiSgvCTCM0EG1UPj9bncNxyGGLHwkq3xvrK2u620tw2WTSAGwy7M_oG4y_tXuB5_0MaJWitfTuHNZnBba4iZ1uAGS1Ln31My230B6TCe8zZ80fYluYphLtGoyw-IPR9v8PxGt0sNvt8VtiLnI6sCSou2rL4Nr2fGptDIIULHzoah_yVcDQSp5Sx5k-1QzwnvQSrW4qSY5yUng0OP8mzIY5ILW1POXrsCMpVAO2wDU61jcjNgmbJ-iUnq3g_w.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 [ Fun HipHop ]</h1>
<p>@funhiphop • 👥 197K عضو</p>
<a href="https://t.me/funhiphop" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 «قدیمی ترین اجتماع فانِ هیپ هاپی»🟡صاحب سبک🟡Tb :@FunHipHopAdsContact :@Chaman_Dar_KhakFollowing Copyright Laws©</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-22 08:01:41</div>
<hr>

<div class="tg-post" id="msg-80190">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">یامال بالاخره ۱۹ سالش شد</div>
<div class="tg-footer">👁️ 5.66K · <a href="https://t.me/funhiphop/80190" target="_blank">📅 03:52 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80189">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">نه،تعویق نخورد امتحانت، بخواب ایرانی</div>
<div class="tg-footer">👁️ 6.99K · <a href="https://t.me/funhiphop/80189" target="_blank">📅 03:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80188">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">امشب با اختلاف سنگین ترین حملات از سوی امریکا رو شاهد بودیم
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.43K · <a href="https://t.me/funhiphop/80188" target="_blank">📅 02:43 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80187">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">سلام باز صدا پهپاد میاد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.74K · <a href="https://t.me/funhiphop/80187" target="_blank">📅 02:39 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80186">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">تایید نشده عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 9.06K · <a href="https://t.me/funhiphop/80186" target="_blank">📅 02:33 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80185">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/WLsdn-L-r61msSi8Y6fyEgEgYfvPMrrQPdzQAdj25FK7LNOoTG9puiWnuEJe9BgRo8rvJxmXph5sqWoMH5VDIqVZnLYVYBW3HojkJRDHAOhCFXA5wSR70m3843SsSsoEDNax9DqNzEpZMzl-vcTA_suqGHBuof5tr_6GSCNny0BNksIbMQKXFkxOAt87T5CuUpAMLrRhC_3d03OYcgE7tQXFuumTwXwctCQpqT96lxtJ9Po0HRn6AvsfqXItY9Gf7SFFYyVpXLFXITgDEytWui0REX4ZwVKmLvqJrrJWhVniBy-VC2GAsD1mhINiorJs7OExG0bWg3ezHOrQbuMCjQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">هوافضا سپاه بعد از اینکه همچین سرباز آماده ای پایان خدمت گرفت طول کشید خودشو پیدا کنه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 9.21K · <a href="https://t.me/funhiphop/80185" target="_blank">📅 02:30 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80184">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">راستی اینجا(شمالغرب) یه ساعت پیش داشت صدا پهپاد میومد  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 8.7K · <a href="https://t.me/funhiphop/80184" target="_blank">📅 02:28 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80183">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-text">تایید نشده
عمران عقیلی، رئیس واحد ارتباطات عملیات ویژه در فرودگاه اهواز ترور شد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 8.81K · <a href="https://t.me/funhiphop/80183" target="_blank">📅 02:27 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80182">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 8.37K · <a href="https://t.me/funhiphop/80182" target="_blank">📅 02:25 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80181">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">بچها شوخی نکردم اسمشو  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 8.57K · <a href="https://t.me/funhiphop/80181" target="_blank">📅 02:22 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80180">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kvhtgaXeLRXVE50qeq-HyZ6VuhRIvLI2DAu035G5E9RamDVWzawDG_UkO7xgHT2P8xxdYZ9oZtb1s-bro8QGdcfbpa7SEFglZcb5A78qtFNExH2q1NrpiiLRZPFT9D9kJC3rpAdwnf3kt2AlGZls4L5MZ3mcS3J47_9Pr43kwk2vLYqmIVoLP1hlSB6c8F5EOskf_buEl0IMhjQNPvDN2B-rSJW1IUC1hQZRfHLw3AIx7uXwx2GtvoODnBrjJ_BShZWolkUtJJT7QRApMA3voQvWgJxXgrGfscmNv_1j4-yBgIFcby84daDF-UZP0pisdWFy5tSNWBzyoh8N-VqqoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد  @Funhiphop | Mmd</div>
<div class="tg-footer">👁️ 8.56K · <a href="https://t.me/funhiphop/80180" target="_blank">📅 02:20 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80179">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">پدافند مجید در کرمانشاه فعال شد
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 8.33K · <a href="https://t.me/funhiphop/80179" target="_blank">📅 02:14 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80178">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">یزید تو چرا بیداری دیگه
معاون استاندار خوزستان:
در ساعت 1:40 بامداد امروز دوشنبه 22 تیرماه نقاطی در شهرستان‌های بهبهان و دزفول مورد اصابت پرتابه های دشمن آمریکایی قرار گرفت.
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 9.1K · <a href="https://t.me/funhiphop/80178" target="_blank">📅 02:04 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80177">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qHX5umPHRpS2atF-nHPSXIScgvqEOY-LcjDcoLGQeqBe2C-j0U484_Lqn5Yjaf_G8WB21fBNi8nrFEmbXPxwXaQ6o-9n6bm3VXz-pQwzZtpLQjaMb-Rz0-HGAN24X-wCnvSQ5gR7L_xiPpeK2c729SJweiB_wwSrxjyKQ1TTjGdoQRR4v4sqcrZHAqQ_q39XV8dCHpt2R6h5ph5WYUrjonrjF_5jCujRR67YOW8f5ol0nVCfmfgzq19WmLVhZlfeZmazaJtliEx3KlAvaXfUXAqxr5i9DO62uIGJS1v37Y5whmkaEi9XKpRw4QMcsXqyGgcxFoiCkA22ggaI6UKE9w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این هیمارس هیمارس که میگن این لانچره‌اس که خفن ترین موشکش 500 کیلومتر برد داره فقط و برای جنوب کشوره
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 9.39K · <a href="https://t.me/funhiphop/80177" target="_blank">📅 01:58 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80176">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/hp15-0ktuDFvTimLc-8kKF_NikkXdipDd74-Anatv5RH9GCbDq83I-T36XO5gL-b2-Uf9iM-p1M9eMTWccJNoSfNIZtUxW9dfkF5PRWeEuoOB2Bdtp3GeMNGVYxpO7zXLbKbXm9UU_0w1nc3ySkPqlwBLcnSOZ3uN9JCqA2KTFlbKP7-7rPx0BPGFJFaacwQmWpfMel6jWZGCz4ZEQ5Nim8k3DloqgRtdT7KbmDBU5QGG-jbVqHzXDyaKRjXyCZ6ebQeGbVtRf2gEwpaBJ1ayKpXgQ1QCvnXloBr7vvsozmeC5YMahCvgaTvIJm_eMK1MPNA4CIA3DNLaqf-M_hV9Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حاجی انگار باز داره جنگ میشه.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 10K · <a href="https://t.me/funhiphop/80176" target="_blank">📅 01:49 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80175">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">جنوب کشور عجیبه
روزا گرمه شبا جنگه
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 10.1K · <a href="https://t.me/funhiphop/80175" target="_blank">📅 01:42 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80174">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">دانش آموزای عزیز سریع بیاید چنلم سوالات امتحان پس فردا رو نذاشتم ولی میتونم دلداریتون بدم.
https://t.me/salamkhobichekhabarchekaramikoni</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/funhiphop/80174" target="_blank">📅 01:36 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80171">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">گویا اهوازو با سنگین ترین بمبا زدن
@Funhiphop
| Mmd</div>
<div class="tg-footer">👁️ 10.7K · <a href="https://t.me/funhiphop/80171" target="_blank">📅 01:34 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80169">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی   @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80169" target="_blank">📅 00:51 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80168">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">یه زمان به لبنان و سوریه و عراق و این کصشرات میخندیدیم که هر روز تو کشورشون یجا میخوره، الان وضعیت ما بدتر شده، ممنون از جمهوری اسلامی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.1K · <a href="https://t.me/funhiphop/80168" target="_blank">📅 00:50 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80166">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.3K · <a href="https://t.me/funhiphop/80166" target="_blank">📅 00:46 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80165">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">شب شد و همون همیشگی و تو همون شهر همیشگی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 11.9K · <a href="https://t.me/funhiphop/80165" target="_blank">📅 00:38 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80164">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">بعضی منابع هم میگن 3 تاشون کشته شده</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/funhiphop/80164" target="_blank">📅 00:23 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80162">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/UlTEibk3NNt11_nDpFPvtcQqFC78XLgEWDjGbbEHXHWWCVPUlz7cAmpEAiPbR0ZJjiTPcqcBup9sqN8q9VU_vY_plAMgnQI8JicoT_ztqchkyLiMMzDOf-RDu1fMRZsmP_Y5_MUPIHp_aecEllv54F3CAtVMWbiVtnz00SAVufPmw5MbO66_yso-egPq9xrRf2KOZY8toBNkDhT2_wuEbfdrC79hJ78JMkRjsHyc2iENXWSxk6LoqgM02InPeV78vQSduQV3n2t2qimWYZcIerXoVQ1p6NKMvg3IFHnEQ9H6i3qih3XVCq7aW9IEnjlI4D_utHQ-fAVcHp8pMRLS1Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80162" target="_blank">📅 00:00 · 22 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80161">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JErj-QzMO5DSzHUpaLnK2H8dUdkf-280ZYEDogWfVWE4jokOPiL848uGnFyEzEFbmYrZ1El5QY76WxPuawXSv4kT8fiph9yIn7IRFtWoN9cKsmTE1Mk7zrPdHIA9rtCCcMr5ObhCS8Sw2hRcbBxNVl2OijkA-dYg3hcV1InglxK8Auh31ZQKd2aELKNCnxhGV0X9-G9FJcIEuEyF0JBxnpj1FK6s8lNTvuS1XJvQHRMQigbKeQQ3OXO1kng-U-XhOBvYA8YGnT3CE19WSSz-6Nq-vZVo-CwCSO6uOUcluDVO7tQS_TSSkiJ-2voJH7uVQ78M0akPxDqfLisUpQJTKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مرینو کصکش فقط گلر واینستاده فک کنم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80161" target="_blank">📅 23:56 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80159">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/vZb1sOKp6IQ1O6TmLKqH3NEB2qteL99_EZ2WYusqMidS6YjEspjLpJfZOk34Hot_kOPU_5Ps6xogSX_tXw9WwDz_JDXsF1Orcgw2sab_FuFUmKfJKsDp0teUJBCvImwIqC3vpg9Da22V4ZexfrciWSOf7U1HT-TYoCxkR7TWyZgP2g7szToUl8yNfqcqoGZuRJwfb3fvqFeAWy0KMXiCFxi-Fu00pjLkMlE0zjA81mTwMftEA76JNkv7CRK9Pn3ss2moWEQbWyLCjUwj7BaHSf8W5tgxMw54tORbxwt2kmdixZY9rAdq7DDCW11xQ_LoOIScSnMVnipxQDZb59IOJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/CXUipmtb2degKroiOIGlwfAM0NF0eqSfu7_qQSi4a3YdaWUVS6bji-SaNAWv_cWQn2TTUOUOPxwULd9YHeTbYTg72lF4mb-7apHtFB1U_XcxL4unzY3LvIw0D4CIeZJ_C_sEgUzQTe-bjypCECbm6XL5oz2dphIMD73Tnv1ATkXnUdqGKSRs4s1DV9uvCBH5AaQDjrNgKsGpKgAK_g7MT-JPWtJDOJQMnkIC0YqxPj8nTINx681jtyI4-xfuFPDeyJ11s4BUAvE-n-HKh7tiQ3z0CZOv3EYSExGbABJbRXAYOX9oQaHgAycxN-6-F7mODvAii465BgY3muKNrpTUFg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">امشب بخوابید خیره
@Funhiphop
| Nima</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80159" target="_blank">📅 23:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80158">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">با اعلام دفتر رهبری، مجتبی خامنه‌ای روز سه شنبه در مصلی تهران برای مراسم پدرش حضور پیدا خواهد کرد.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80158" target="_blank">📅 23:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80157">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">راستی 021G زنده اس؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/funhiphop/80157" target="_blank">📅 22:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80156">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بچه ها یچی میگم نخندید، ویناک و منیجرش معتقدن مایی که زمان جنگ وصل بودیم به سپاه وصل بودیم و قراره بعد انقلاب اعداممون کنن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80156" target="_blank">📅 22:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80155">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته  @Funhiphop | Menot</div>
<div class="tg-footer">👁️ 16.7K · <a href="https://t.me/funhiphop/80155" target="_blank">📅 21:51 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80154">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">بازنده تمام بیفای دکی صدف بدبخته
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.2K · <a href="https://t.me/funhiphop/80154" target="_blank">📅 21:48 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80153">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ft2w_QIUMuf0ZaVWGsIpUxynWpNL6UmAMLYohlIZycAMO5GNVI2UBbbeTtV4mP00PJ-JImpRqN4iUkfgN23NTxuRxmoFQ3ZE1tX22rBZCxKWDj9a1BrTfeUPAX8yl4u_Wz72Szr4i40hTzf_8wvhupDEZmwpEVpqb7vMdNLPmaq5A8-GgfQz6QTf3pdyNg3TK45NQSeOrGuYLAsSMKPNRnR7XzzMUJlEWkn3ikCRly5XI2077oBmmUke_55S3Syi7QVLh6bgVg-4-3fP-9LknwelK5wMNEVMkIhGnEP3oGQ7o1DAlwVK4tX_rSj9yM-wADCrTALnn6L424uwm7sBAw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کیر تو جنگ و بیف بعد 6 7 ماه حضرت لنا رو بچسب پسر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 17.5K · <a href="https://t.me/funhiphop/80153" target="_blank">📅 21:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80152">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">این حرف ترامپ که میگه امشب بصورت ویران کننده ای ایرانو میزنیم فیکه هنوز چیزی نگفته
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80152" target="_blank">📅 20:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80150">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">14 تا سرباز امریکایی زخمی شدن 4 تاشون وضعشون خرابه بعضی منابع هم میگن 3 تاشون کشته شده اگه سرباز امریکایی کشته بشه احتمال گسترده تر شدن درگیری یا حتی از سرگیری جنگ زیاده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80150" target="_blank">📅 20:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80149">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=JoCblb5JP592G4adQflJa6nlniJgkLJy8S3jOg0KPp_h7Qkfv62IB6eEUksivYMezkDb7ZqoKJrFHlGungPn2utfHkEGvaOPy81QkEw3vJuhCd38czaiLJYPT_Ycec_00ImQmPWzVyBOqXsHLUqM5ciWKOuU290cU-6Jr7oXY5HJHohVPWK8vo0SUzBGeRRl0aPiEWfj_4YA5pTKP7SDbai1yWoxaUdedI00i7GLrQC-kpuX5tlUpTbS-BFz16a6i2WpbHBZBmReaJlupcDjIdE8fcSB7jG2LNYKeVj5AYBev20J5QEego_Z3JCMbppYclsZlDvXApwZrtLm5NU3Jw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/8e73f890bb.mp4?token=JoCblb5JP592G4adQflJa6nlniJgkLJy8S3jOg0KPp_h7Qkfv62IB6eEUksivYMezkDb7ZqoKJrFHlGungPn2utfHkEGvaOPy81QkEw3vJuhCd38czaiLJYPT_Ycec_00ImQmPWzVyBOqXsHLUqM5ciWKOuU290cU-6Jr7oXY5HJHohVPWK8vo0SUzBGeRRl0aPiEWfj_4YA5pTKP7SDbai1yWoxaUdedI00i7GLrQC-kpuX5tlUpTbS-BFz16a6i2WpbHBZBmReaJlupcDjIdE8fcSB7jG2LNYKeVj5AYBev20J5QEego_Z3JCMbppYclsZlDvXApwZrtLm5NU3Jw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">ریدم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.4K · <a href="https://t.me/funhiphop/80149" target="_blank">📅 20:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80148">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/B4ozkK1Q2MRN2geNRASj5cEDv8skDIqY9lv9AETpv772-LU84s2HwqamHebzjtvaad11gHlx1JM8gqgP09rkrtjJYHedmrmUXWlff1sYQTKq4Zxl1PrQIUoQ7ZhZdhhJaKUm_UIPVG-Aw9IIeB6dkW9HWltuOBOqMhday1FiCl65yKsi8S0d4bXOSTb8OsCDtzkB9hNkIzHfdoMRClHMxoyXD2nHXhvOFXBJ8IDKo60bXbOAdAhnkdoXWR80UJ1MoBjCwjVLScOSmqCtmypUU52sZ4KGCtxAkgQwZjZZtmwW_Yf_7vwUGmA8XlnLNB7aeVrEGykJvn0f5u11M25aDw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">آره داداش تو عضو بلادم نبودی.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80148" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80147">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
g21
💻
@BetForward</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80147" target="_blank">📅 20:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80146">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">سلام فرید جان ما قشمیم اینجا رگباری صدای انفجار میاد تموم هم نمیشه
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80146" target="_blank">📅 19:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80145">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">جنوب کشور درگیری بسیار شدید گزارش شده</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80145" target="_blank">📅 19:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80144">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">فارس: شنیده شدن صدای چند انفجار در بندرعباس و قشم.
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80144" target="_blank">📅 19:26 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80143">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">وضعیت طوریه که ممکنه جزایر نشینای ایرانی امشب تو ایران بخوابن صب تو آمریکا بیدار شن
@FuunHipHop
| Mmd</div>
<div class="tg-footer">👁️ 15.1K · <a href="https://t.me/funhiphop/80143" target="_blank">📅 19:21 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80142">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">خلاصه ترک:
کس ننت
کس زنت
بابات سپاهیه
پدرزنت سپاهیه
تو خایمالی
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80142" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80141">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80141" target="_blank">📅 18:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80140">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80140" target="_blank">📅 18:38 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80139">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80139" target="_blank">📅 18:36 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80138">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">بیت چرا داره هوس شد؟</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80138" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80137">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.9K · <a href="https://t.me/funhiphop/80137" target="_blank">📅 18:35 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80136">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80136" target="_blank">📅 18:34 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80135">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/funhiphop/80135" target="_blank">📅 18:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80134">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">این که همش ناموسی میده
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80134" target="_blank">📅 18:30 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80133">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اومدم ختم کاکولد
بجا تو میکنم ننتو بلاد
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80133" target="_blank">📅 18:29 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80132">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80132" target="_blank">📅 18:28 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80131">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">بیف سر دقایق بیشتر موزیکه نه پانچا، کصکشا مگه پادکسته</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80131" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80130">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80130" target="_blank">📅 18:27 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80129">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.   SoundCloud  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80129" target="_blank">📅 18:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80128">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/SD9MLc15fhwkklVpPRVYupZ5FdCmOR4-F8xgW7B-1QN3FINx-2gQnIOXHlykpwHWFUyxflJxzzf7bY-uV1ZMSrDFUcCjrF_h6gUtDpLz0T-cPa1dCX6yE6602mhSXORPdWRrMOMUZUD2euLNCYLzJAv0oB3jKxMq7vUZjbioh3gmEQJoT8JmqPFvnaSmPaROMPE9vfAx5MjyVPL82V_fkvj9DAl7CIwHem2AbD6G-dkkZ6gy1FbctHCFaBr4DINpItRWlinPTU589gKRyC0FwkzzbrMVO0AkP9Pmuw-a0wY9XKt4oK2ZdYHa46PvNhfLzQC7g4tkaiu6fuSL2rhhGA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دیس ترک جدید ویناک به نام موش زاده منتشر شد.
SoundCloud
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80128" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80127">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">ویناک کسکش بسه
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80127" target="_blank">📅 18:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80126">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/j9B9a8PrWx9NN71wTZbjKhRBHwdeaYUjsYNErN5V6H2qAgWABTQ80iNnm8v5MgPx_q6_y3q6CClx2gZa43MDOmgKfZXcbaC72jL5hJaLo-IFjH5Y7ofbNkmlNWwE9iMWT6z3KBYhO63KyjTttDjyej0c1fWbNNfdfDALyFjAUh3DJjozf6xc1T7-GsRedZTLmh6AafvrAfbg_h4IR7yXRgF8dNrLAcZrFcIodeE733ySwpWOEfMHIgTDBgD6msF4jp3GIIAh18638IognBK1zMv2btGkExQ116L_jRzeCEz91rQx6Lw5fVVImML3_DWCdLZnzUaQbdHfwGODw7kjAQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">زیر این پست عکسای رندوم بفرستید. ۳  @FunHipHop | Arash</div>
<div class="tg-footer">👁️ 13.7K · <a href="https://t.me/funhiphop/80126" target="_blank">📅 17:46 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80125">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">ویناک فک کنم داره موزیک یساعتی میبنده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 12.8K · <a href="https://t.me/funhiphop/80125" target="_blank">📅 17:33 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80124">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">حالا ما هیچی، کانر خودش خجالت نکشید بعد اینهمه تشریفات با مشت اول بگا رفت؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80124" target="_blank">📅 17:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80123">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/6869027e93.mp4?token=SSASZbXc1_h5JYLgUNjT7dJMoYu11XS1qBL3gS0FZ3LJhq-IQ8fZEJBOLji2Vs0hHr49VIDkEP14h0uja7diK-RX66-JT-IpRvH_nL_T3HhNkQD6dbuDIS90DKzd0nCgz2dhK8bMyn6eEBE9PUA1hop5cSjM2PAmviJX-w1OgdFwF5ghdy6t8EBiiQlA7VtNz3bYnnv1S_CqCZI480RDNkevD0g4zSlMcnBiOFjqKQhAdX0hm-3GKdmmUvucOYW7iNOVk4zkCxC1qo3VfdGojbyf41DtGSH9sfwSHJmjGIRixrh3fFMMUpsoGogni37L4bPC1lPDIoN8Y0KVJEI0TA" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/6869027e93.mp4?token=SSASZbXc1_h5JYLgUNjT7dJMoYu11XS1qBL3gS0FZ3LJhq-IQ8fZEJBOLji2Vs0hHr49VIDkEP14h0uja7diK-RX66-JT-IpRvH_nL_T3HhNkQD6dbuDIS90DKzd0nCgz2dhK8bMyn6eEBE9PUA1hop5cSjM2PAmviJX-w1OgdFwF5ghdy6t8EBiiQlA7VtNz3bYnnv1S_CqCZI480RDNkevD0g4zSlMcnBiOFjqKQhAdX0hm-3GKdmmUvucOYW7iNOVk4zkCxC1qo3VfdGojbyf41DtGSH9sfwSHJmjGIRixrh3fFMMUpsoGogni37L4bPC1lPDIoN8Y0KVJEI0TA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">یاشاسین تیراختور
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 14.7K · <a href="https://t.me/funhiphop/80123" target="_blank">📅 16:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80122">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PbFkH_j80uUcZjUxqHATH52Nn4uLEvBqcHNAbdrXuFpwCP4L9pj21PPg1nvSjKTDahiFG77UPdLSIFMQ0EfR2k0i7BCDcifdI7X0irFdU_GId33ENO7RzHdnmA4fzEDRt8sV16Qt643-C6QHCcYViWoaICeKODs2xgLCSsFyW8vYbSvunCbw5MNhYwDV86bMn8gho2eEHuX3SGhQDtcPwHeWrm52awQtKyBSV1UWGbIRNT9msH8q_rq2kWSbIdlxgWepgnULqxv4E0Ec8C8ln6ehfqs0r548VQKZ6yU52UceEXRFVTvIu8adOx3itkWj61waaNAaZgTwXK14d-gZTQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مادرجنده من تو این هوا بدون کولر چطوری زنده بمونم وقتی برقم قطع کردی
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/funhiphop/80122" target="_blank">📅 16:22 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80121">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">دشان از تاکتیک های ناشناخته فقط یچی شنیده ها، اومده خبر داده بیرون که سالیبا و اوپمکانو همزمان مصدوم شدن و نیمه نهاییو از دست میدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.6K · <a href="https://t.me/funhiphop/80121" target="_blank">📅 16:06 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80120">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i4XcySMJtpLr_mJO0o0AEhouOfYkZ_6e2SeyO5WwBGjp_DrzlN4ED0lK650Vy4_zQ-9VcdZSw7EDA68lPF2q7H7yQYLHRSFgWp8S8IXXAtU1vYtpYYROnnziO-LVBRN-GETjhCnF1aDrUYCa4vyDvqysMBLeI6dr-iOC8-mm3yDjBG1vjY9c-zWOEc1NoPuo0H-ZDuhUmLsHRScwGF6KZiawkQeeRkXrvdiBPuQj6xACk91Z2AVbOAHHB0oexLnavGwrfstiEA5F4UOjnkm_0d5jRc2m4xfgZZqOuJ8XB7_EbPwcr7d231wPaC6zOuDJdzay65i86v50-17faISguw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دریک جان کیرم تو ناموست
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.2K · <a href="https://t.me/funhiphop/80120" target="_blank">📅 16:05 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80119">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">دوستانی که امتحان دارید، فکر کنید موشکا ستاره ان
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80119" target="_blank">📅 15:50 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80118">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">امتحان چطور بود؟
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/funhiphop/80118" target="_blank">📅 15:40 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80117">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">این رونالدو فنایی که به مسیر راحت آرژانتین برا نیمه نهایی اشاره میکنن خبر دارن که اگه تو گروهشون اول میشدن همین مسیرو داشتن؟
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80117" target="_blank">📅 15:25 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80115">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">عجب امتحان پیام های آسمانی سختی بود.
@FunHipHop
| Arash</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80115" target="_blank">📅 14:16 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80114">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">شبکه کان اسرائیل:
ترامپ تصمیم گرفته که محاصره دریایی و عملیات نظامی‌ از سر گرفته بشه
@Funhiphop
| Farid</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/funhiphop/80114" target="_blank">📅 13:53 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80113">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">شبکه ۱۴ اسرائیل گفته سپاه به کارتل های مکزیک پول داده داخل آمریکا ترور انجام بدن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80113" target="_blank">📅 13:47 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80112">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded from[ Fun HipHop ](Mehdi)</strong></div>
<div class="tg-text">والا من هرچی لیست تیم ملی انگلیسو نگا میکنم تیم خوبیو جمع کرده، این بازیکنایی که دعوت نکرده فقط اسم داشتن وگرنه بازیکنایی که جاشون دعوت شدن سال بهتری داشتن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80112" target="_blank">📅 13:43 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80111">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">از ۴ تا تیم حاضر تو نیمه نهایی جام جهانی بارسلونا تو سه تا تیمش بازیکن داره و فقط تو آرژانتین بازیکن نداره
ولی بارساییا فن آرژانتینن
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.6K · <a href="https://t.me/funhiphop/80111" target="_blank">📅 13:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80110">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">میچ مک کانل یه سناتور دیگه هم سکته کرده و به بیمارستان منتقل شده
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 17K · <a href="https://t.me/funhiphop/80110" target="_blank">📅 12:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80109">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">اینطور که اینا گردن میگیرن، همین روزاس موساد ترامپو بزنه بیاد بگه خب اینم گردن بگیرید کار داریم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.1K · <a href="https://t.me/funhiphop/80109" target="_blank">📅 12:23 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80107">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/NU96eQkt2rbXzKwEOm5Igvc2XTdw2fPqVRfXERhiJ0_UJ2h-BA6aC5ZcGAMUqLjMyRPwqWY6PVrDPbEu6CEmP0mNzCKfCXrqIr4BaoU6SGqXKHo5obj_ytCLbG_LS67KfGmeGo6O2kira7lhIgf7ZBvAZwdQ6-DtzDmw-aldIRAdIhiRylGFRDi3IY8-gbryvKOvlglg4BiX9PdTnr9fWMdU-w15z4eD2simRKky6IYvYKS6mATuRfkTshmvH9ioTab-fx2AsTrsVpyc3pXLAoKBMrHBxhybDJHoLVEP2RgbyUt4DmfWnz8PCAfDeZDTbYFSu6Qd5wkUm5YuPrUwWQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=uvDhXhlP4MHN3Ms-16iO6qPmHvs3hYi0ZSdWneudZ7JkxXJrnCLYpeOimXsqLgwLlEA9fCiOvTeonC_Q30-aYNXJuyqZbJEZGdS-3RrNqMuzSiH07Q14UsKjZK6rTQ7bIPrxTfVe5tKx_ufRgAJYQF_pzTO6x-toFFL_Xi5aZc6QGquUXO8XqwdLo1Gjp78t5MNycJVYNDeqchSuF-POzeGcS02yQBuUmCGRogDaOS_VVqMw2US0alfm2GcGs8w-wTrQ--XuxfNJ3ilcQMq5it1xqlT-1X2iHkqJthnaEDwb8uMCEbFNheU990ILAXtu5h6CDm16pl_yahKA0GjSzw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/84de9e91b7.mp4?token=uvDhXhlP4MHN3Ms-16iO6qPmHvs3hYi0ZSdWneudZ7JkxXJrnCLYpeOimXsqLgwLlEA9fCiOvTeonC_Q30-aYNXJuyqZbJEZGdS-3RrNqMuzSiH07Q14UsKjZK6rTQ7bIPrxTfVe5tKx_ufRgAJYQF_pzTO6x-toFFL_Xi5aZc6QGquUXO8XqwdLo1Gjp78t5MNycJVYNDeqchSuF-POzeGcS02yQBuUmCGRogDaOS_VVqMw2US0alfm2GcGs8w-wTrQ--XuxfNJ3ilcQMq5it1xqlT-1X2iHkqJthnaEDwb8uMCEbFNheU990ILAXtu5h6CDm16pl_yahKA0GjSzw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">صداسیما گفت که گراهامو ما کشتیم
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/funhiphop/80107" target="_blank">📅 12:19 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80106">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">اینطور که داره پیش میره یه ده تا کشتی دیگه بزنن از جنوب کشور یه خاطره میمونه
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80106" target="_blank">📅 12:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80105">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=kCtlRqLvM9RPg4bmNkdJCtGn-oUrEuLIx-9e7vk5tjVe2O7bZ9QDKXKvGG5cO7YzsnjK0RMep6Tv4F68d674lQnmVWBDrGlo2u2ZArtD4Ybx8MipD4I_08QQMY5uWJ9IO-jg9oJpbFvFqFSXpHq743M1mGt5WLGERAhRLh3-FBGIHGJi4AjfKZaKNFyBnq6Op1wVQZIoj6mlFIZfZFRHhOXt-K-8AX2DaKa2TyP3_xrUjuSL4WyXoc3eQbp3Vd_nzm633l3nHmLx6K4pAzuCfMVieCgGK4pFUikf_0BIYItwPGRVBWcI_PsmESonRa4CDCIZpKEbh5fkn_gPIG5drg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d0f7af99a5.mp4?token=kCtlRqLvM9RPg4bmNkdJCtGn-oUrEuLIx-9e7vk5tjVe2O7bZ9QDKXKvGG5cO7YzsnjK0RMep6Tv4F68d674lQnmVWBDrGlo2u2ZArtD4Ybx8MipD4I_08QQMY5uWJ9IO-jg9oJpbFvFqFSXpHq743M1mGt5WLGERAhRLh3-FBGIHGJi4AjfKZaKNFyBnq6Op1wVQZIoj6mlFIZfZFRHhOXt-K-8AX2DaKa2TyP3_xrUjuSL4WyXoc3eQbp3Vd_nzm633l3nHmLx6K4pAzuCfMVieCgGK4pFUikf_0BIYItwPGRVBWcI_PsmESonRa4CDCIZpKEbh5fkn_gPIG5drg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">کانر هم صب همین که وارد قفس شد مصدوم شد و فایتو باخت.
@Funhiphop
| Menot</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80105" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80104">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">🧠
دستیار هوشمند پیش‌بینی بت‌فوروارد
✅
🔥
با قابلیت جدید هوش مصنوعی بت‌فوروارد، تجربه‌ای حرفه‌ای‌، دقیق‌ و سریع‌تر از پیش‌بینی‌های ورزشی داشته باشید. این سیستم با بهره‌گیری از AI امکان تحلیل بهتر مسابقات و تصمیم‌گیری هوشمندانه‌تر را برای شما فراهم می‌کند.
🎯
تحلیل دقیق مسابقات با هوش مصنوعی
📈
بررسی آمار، داده‌ها و اطلاعات بازی‌ها
⚡️
ثبت سریع پیش‌بینی تنها با یک کلیک
🧠
چت با هوش مصنوعی برای دریافت تحلیل حرفه‌ای
🔥
استفاده از ابزار پیش‌بینی‌ساز برای انتخابی دقیق‌تر
🎲
ترکیب قدرت هوش مصنوعی با هیجان پیش‌بینی ورزشی
⏩
با دستیار هوشمند بت‌فوروارد تحلیل کنید، سریع‌تر تصمیم بگیرید و حرفه‌ای‌تر پیش‌بینی ثبت کنید.
🌐
ورود به سایت با فیلترشکن
کلیک کنید
BetForward.com
کلیک کنید
BetForward.com
🅰
r21
💻
@BetForward</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/funhiphop/80104" target="_blank">📅 12:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80103">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">انفجار در فرودگاه بحرین.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80103" target="_blank">📅 10:55 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80102">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-text">لینزی گراهام درگذشت.
@FunHipHop
| Reza</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/funhiphop/80102" target="_blank">📅 10:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80101">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">آرژانتین هر مرحله که بالاتر میره بیشتر به هنر و توانایی پروردگار بی بدیل فوتبال جهان پی میبرم
با ۳۹ سال سن یک تنه این تیم رو تا این مرحله آورده
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/funhiphop/80101" target="_blank">📅 07:14 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80100">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">گل سوم و تمام
صعود آرژانتین به نیمه نهایی
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/funhiphop/80100" target="_blank">📅 07:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80099">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">لاپورتا ناموسا بخرش
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 16.5K · <a href="https://t.me/funhiphop/80099" target="_blank">📅 07:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80098">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-text">یا خدا این چی بود آلوارز زد
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/funhiphop/80098" target="_blank">📅 07:03 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80097">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-text">دوستان تازه بیدار شدم اتفاقی افتاده؟
@FunHipHop
| Farid</div>
<div class="tg-footer">👁️ 15.8K · <a href="https://t.me/funhiphop/80097" target="_blank">📅 06:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80096">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YDQKQiQOe7qN7AaJ3ICVlKFcNHPlValUVngpk2ES2X2eSL4WAgq5PHpcnl3Z2Rmc_Pk3bR2PmXK0OXtFIkh7-NUGqQ6C5bFcGJrxoJEHzjnZVL9n0kNOOduCCW8KKO96xJbRe9FQ74ghiTCsAXVApc6RF7m8-WJOI-FCIVUf1VYpOulXty3vAGSHDsgu-tKIzoeGrJjjPy1L9_WABVqZZR89G9mfPuz8rbxJtJP0qZkbqlUe-QW13wjCF254DiKvrQ4BrzSLD3CKwQQbNiv9gH6SmNLe5njpJdcgcj5q5EZ2mj94jpEMeasJ-0w5FBiUEuT-SiP1nVnZjy1NcTWYDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترکیب آرژانتین مقابل سوئیس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 16.8K · <a href="https://t.me/funhiphop/80096" target="_blank">📅 03:45 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80095">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">پیت هگست: ایران انتخاب بدی کرد، حالا تاوانشو پس میده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 15.4K · <a href="https://t.me/funhiphop/80095" target="_blank">📅 03:31 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80094">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">فعالیت پدافند ها تو تهران
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 15.5K · <a href="https://t.me/funhiphop/80094" target="_blank">📅 03:20 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80093">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=r577CR-j8NfohIOhfVyeqy6jfR3udAHx9LjWZBxFDO1gvoVjUOFSvyEr1Q-9b9bR1Hynx8PvFVot5H_sNv8ileM_ma_5uVXW_FQuD1yW17qT0KHXq-lMyfv3i0qjRhmUOK5W4HgVFsb2yPaUCc4OK7hiuWeSZemedfHsSXyiW1C31NlP37rKr_0TVsItz__z5QVhPPjH0hQvuGutmeuPVknxoqxtBqc4LJF_rOENBeWR7KhEVYN1HIKrPyCD1NPmfDmu7jKj_NX9yRyRHbUS9ZD0i_tqejzepg0R30aF-Emg8bl0tX8wimYnGz6M4rN-LPH9QafDKyxJMjCPhIgUmL6EyMSea8Wsv1GTbHd4j3g1N5AHWi1dFC77t5Qnugb7lP5TErcaPUmUx6k3SIiJUwjcZit7PkbCYAEU_aAFGUR3afxm8aKjDrHOA8YOZeD1dVHfkhE3WKGsANQOvO7RCAzuMiLIlAJxPKU-O87LqkWjv5rCZ0SfPKxrI1f7-PeimyI-tF-EJnkrhNVrPK5glaNPmUesrt-JKUdch612FQ3xQOLqMxYyonc3TFqciG4bM5-eynNg3jbIv1WJvNsjmOPsXrYxABRAsm-OKtlMjsjomtGfMvQDH6AQ9eDWIcin8_I_KnJipZQHMX9X7PKrU31TIX9f_NA2fIUz-yMCvf4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a009afea3d.mp4?token=r577CR-j8NfohIOhfVyeqy6jfR3udAHx9LjWZBxFDO1gvoVjUOFSvyEr1Q-9b9bR1Hynx8PvFVot5H_sNv8ileM_ma_5uVXW_FQuD1yW17qT0KHXq-lMyfv3i0qjRhmUOK5W4HgVFsb2yPaUCc4OK7hiuWeSZemedfHsSXyiW1C31NlP37rKr_0TVsItz__z5QVhPPjH0hQvuGutmeuPVknxoqxtBqc4LJF_rOENBeWR7KhEVYN1HIKrPyCD1NPmfDmu7jKj_NX9yRyRHbUS9ZD0i_tqejzepg0R30aF-Emg8bl0tX8wimYnGz6M4rN-LPH9QafDKyxJMjCPhIgUmL6EyMSea8Wsv1GTbHd4j3g1N5AHWi1dFC77t5Qnugb7lP5TErcaPUmUx6k3SIiJUwjcZit7PkbCYAEU_aAFGUR3afxm8aKjDrHOA8YOZeD1dVHfkhE3WKGsANQOvO7RCAzuMiLIlAJxPKU-O87LqkWjv5rCZ0SfPKxrI1f7-PeimyI-tF-EJnkrhNVrPK5glaNPmUesrt-JKUdch612FQ3xQOLqMxYyonc3TFqciG4bM5-eynNg3jbIv1WJvNsjmOPsXrYxABRAsm-OKtlMjsjomtGfMvQDH6AQ9eDWIcin8_I_KnJipZQHMX9X7PKrU31TIX9f_NA2fIUz-yMCvf4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">شلیک موشک  ATACMS/Prsm و HIMARS از خاک بحرین به سمت ایران
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/funhiphop/80093" target="_blank">📅 03:18 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80092">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Ln4v5IvmtOwXmxbbaZVVwzJhT6sVIKRCyedZtsBJ9LfVoCFcbP_rr6wP-8puTZ4PJvbrTlMGt78N9TqMJYj8K8rJJyDAd2GMQxStKOfta6gx5aI8oX9jUrU9fOYiPzhHMn1E-KCmROfK_ICgARj45o_0cgqCzruGmXo-RuZiERJ6Ug6R7AfozhQj84DlZcL04UNosjzsBtdrFw7dP01OAkZex7Q6DJWVKE1eoWGMdqrfjI-_mj1SVmSQw7zaAuJZ1FKsx9M2l1Jj3UQFk6C365f5iWElhVG9NsNisHjNoF1jirbky0faTZdI3d0KG9zytNZTYVd90ROtOKY-BfLuSg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">با این روش میتونید دینی رو تو یه ساعت تموم کنید و برید سر جلسه
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.8K · <a href="https://t.me/funhiphop/80092" target="_blank">📅 03:15 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80091">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">سنتکام: سومین دور از حملات خود علیه ایران در این هفته، پس از حمله سپاه پاسداران به کشتی GFS Galaxy در تنگه هرمز آغاز کردیم. یک غیرنظامی مفقود شده و کشتی آسیب دیده. هدف از این حملات، تضعیف توانایی ایران در هدف قرار دادن کشتی‌های تجاری است
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 12.9K · <a href="https://t.me/funhiphop/80091" target="_blank">📅 03:12 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80090">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/USShkVYZEfa7DwT8hEWILnyv95VOWSpJ1VEpaNo6OqtRPfLi3DtYL8at1PajOVXVH7DWgtVBJq0CfS6sRKJSxj1VB3ZZbEnKelbUafURTb76yV5gHpyKEdn6Hhlbu3y0Dxxw5-8r11zbZZGALCbnODwkvJ-cis0_r81fiHc8g-3Owk0X-SdfHUYPZndwpY2s4xPxXXijfBSpf6Zw8ZomYk9pcw0g8O4KNcizs4wdd6OxRl1wrCUoXLMQp0QlSaSNac_JwxZ7NzWbozVksp_XE5dR0i3PVmPspaCF_5QnYgj6opA9TvsRm5UzUqUyzYxJOzHlUgGejk6eQoa-4mwFew.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این است خاورمیانه
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 14K · <a href="https://t.me/funhiphop/80090" target="_blank">📅 03:09 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80089">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">شین: انفجار در بندرعباس
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/funhiphop/80089" target="_blank">📅 03:08 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80088">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">آمریکا تو حملات امشبش به جنوب ایران از موشکای هایپرسونیک استفاده کرده
@FunHipHop
| چمن در خاک</div>
<div class="tg-footer">👁️ 13.4K · <a href="https://t.me/funhiphop/80088" target="_blank">📅 03:07 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80087">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">رسانه CBS میگه تهرانو هم میزنن صبر کنید فقط
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/funhiphop/80087" target="_blank">📅 03:04 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80086">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">سلام اهواز انفجار  @FuunHipHop | FaRib</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/funhiphop/80086" target="_blank">📅 03:02 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80085">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZU_5xAcUkkw00CHfFO9RDANmJe2QxVZDAecpoocQa6Gy4UILWNm3lDSbt9kORNNSCeH-3Q90m7F4FwMmo2aHILql-3vTNHtikHjwxsqBXovZeenCrc1rVZxu1CBCe2zbJ74OpIJz08mvbSmm8HtOoQc4EPqJ6NdCJPpOq-178Opf9mEUBoNwWPMkLCuI3pDXWDPEzJURiOyTnW4TckRa4Q6UX54CzX-7ElfOinyf0DwBdS_woh4_QQqPnZ17lN6l5o_dGs2KoI7xKE3wfzltj1h_inHs7mefHTZiI1p94Z4ohh2q4-NCuusTIuvdp46fh_GhH--ccjRV4nWwd0Nymw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">بندر دیر
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/funhiphop/80085" target="_blank">📅 03:01 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80084">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-text">صدای انفجار در بندر دیر
@FunHipHop
| Taymaz</div>
<div class="tg-footer">👁️ 13K · <a href="https://t.me/funhiphop/80084" target="_blank">📅 02:58 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80083">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-text">سلام اهواز انفجار
@FuunHipHop
| FaRib</div>
<div class="tg-footer">👁️ 12.7K · <a href="https://t.me/funhiphop/80083" target="_blank">📅 02:57 · 21 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-80080">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-text">انفجار در کنگان  @FunHipHop | Taymaz</div>
<div class="tg-footer">👁️ 13.5K · <a href="https://t.me/funhiphop/80080" target="_blank">📅 02:51 · 21 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
