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
<img src="https://cdn5.telesco.pe/file/d8FMdeVjuv8LA-TrPQ7By5mi-gnmKO12JacByxiSGIREAuZl3OlK04IMWDx-HoZEd_-0vE5wW5hETgz9GIji41EZDVnR2FVOrPZy70IvNbEFVwTDQPfO7CkY-LkbehH9SwEv7ti9RPtVx-LDdO_0dWWP9bQIbfbUDtCJ-lqmpyiWDkYGMbZ52WPMKlfYtNGn3XMYt-YzZ6d2uXrERmdikaaM_knNDpjcCXfibgqACK9XL9tEgOqZLE0yViOirAroPwjhxQtu2O-cU2KtXn2MPq5ATvL8R4pLTCFW4dLLwUToIgWV-FBKzIqmrkat64yHmpqHnpR8H5U96IleP3o4Sg.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 688K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-06 00:32:49</div>
<hr>

<div class="tg-post" id="msg-96162">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">🚨
🏆
پایان‌بازی|گلباران وایکینگ‌ها با درخشش ستارگان پاری‌سن‌ژرمن در جنگ صدرنشینی
🇫🇷
فرانسه
😀
😃
نروژ
🇳🇴
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 3.04K · <a href="https://t.me/Futball180TV/96162" target="_blank">📅 00:29 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96161">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">دوئههههه</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/96161" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96160">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">فرانسه چهارمییییب</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/96160" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96159">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">گلگلگگاگلگل</div>
<div class="tg-footer">👁️ 4.05K · <a href="https://t.me/Futball180TV/96159" target="_blank">📅 00:27 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96158">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/5a0f064511.mp4?token=l6TVqUM8lbm34Md5YhevUXHhnliTRP5Zi_BqhVmsnGc6AVFazOwtcfVzyddIxEHYbKesSnhjXCMN7dAOAQj5hUeJsDZs-74h3eoAzMyFtxC7kVgKsuBpBQ36P7_zJiqpqr0rCbq6n5u7GmYPR2zrLMQdq4L8MYMi2h4SCjBVqFK7n0L6mYhpYJTf-xt7FEZYkzh-hgKwO2h5jTD9__SpysDgb3QFv2OsLSFOTCwMOgvDHpCv_QY7RzWgzf_BDcvI7vNfFU74QQv-mTPcK4-r1MGsmENxZeue1Be4DxuhiV7sGubyRXyr4MN8blDK6Htw4wIr9JxxGh5SvNB1s9vF2kjzCcsPb0O5fr14rtUpgzcEzpgX2umASqmx2Lu6WvgeyHLCi65y-e24rWBieUNaapQ2_OBgcMgtexfVdC3RpfWRV691SRKgrA1f3mTpSrijAp5qaZLG_8iX3kLUhmOJiMmpL4vsRegYqDVmMrlpVpGnAABx4ysMob4phOJ7Zt3ZcAuzXpBfWgDX_fbr80ccXUmNPlbejNMcNi4zk3ARpYoB9s0SJlBSQqc20nv_4Sq8DYaBziAh1at7rcZ_P9awKwGT9ucjk3thGX9ltOpGYUgQVQl0lCO93ALaqXrm3eC1eF8vKVXXFJbPo4KBwpKdWh9WcoGVaxCzpab5Kt9IJ90" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇸🇳
گل پنجم سنگال به عراق توسط اندیایه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 7.11K · <a href="https://t.me/Futball180TV/96158" target="_blank">📅 00:22 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96157">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">تجاوز سخت و خشن به عراق</div>
<div class="tg-footer">👁️ 8.12K · <a href="https://t.me/Futball180TV/96157" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96156">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">گل پنجممممم سنگال</div>
<div class="tg-footer">👁️ 8.13K · <a href="https://t.me/Futball180TV/96156" target="_blank">📅 00:20 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96155">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/O7vdl8Tl1Y8AM3ag2ztmmrtBdAFZeXJ6LQFT66zetJ7himNbQcelHHzcGiGKi9iDBTat1k9NUZDKMxLFM-AzYzU06aoQdX6p569ZN1B8ljCukmubiLXH2Cor_STqhsyVSEGt2fG37xIzTMZrYQihoaIRpQuu6L8JwMxJuTYwdj3UqBnJvVcD7CAQiw8tlUFlazvAfXIHnEwELMHOkr_Rm1R7P99RjgSGJKg7r4iRdPFpTDXRLa8Sbw1EzMcK86A1NJ2Vktcp6x-rOGe21k_DVaiE10w1JILMwE5zwR1-3T_Vj87x4kAiElfJdAbbtkIQDg1BLzdqmEmL4BSlBh1iZA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">این دو تا لبای همو ماچیدن و حلقه انداختن به هم محرم شدن.
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 9.13K · <a href="https://t.me/Futball180TV/96155" target="_blank">📅 00:19 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96154">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/9f26eabfb4.mp4?token=LNZCwLCHmWu6KKdf31F8Igq60yLL2jsDODsDKifTJYnrQzbKks-F_ei2XrXDet1wFNauJq0kzO5g4Zn0LoGNNVkAhHGF-v1MkCGp1ma-uaermZVPt3lkpz2W75wf-f6vAk5iSpkO5SgS0etlEN1CMHzDHxYE29CUO8F6nnHCEIW9Jo0o-lLRfPgQtPjxcOjtiAqeIEZTY2FMG9qWi8VgotM9Olu7A0jQR1suybAwDrkdgZTTS3eD-3_8VE8knfFDsl9cBLkIMCwAomXLkRCUyKpoD1yFu5upmehx4g_TYnDJHDLCJZVEqpoI7g_HZN-BvBYHe-e9pOg-d8ti_UkmUKPVgThF5GvCvJHRusf6Ob5mjzIImvrZP0wAJ5cjm3FwORC79vap77vp0Qg7MXxpO7TaCS02APzIuWmDuMvv-lYY4GdghgOWsPgiVdnUgNHRqYdIsupDmvZzJt3NeZPRRtlLp6ElxH5GNr0x3UOsyY1rDHMcj7W_ug6ihrV3UbjzNm6kXYq3D3lwoWf4gia2vzu1XjLuqlamH5IJ_0k5KvOX8HFLkDNZ5pxMArvXSSOrOhpOMQ8zE3Kr1juyaSQeTifm340F30ZUtKOhMl5-hYpEZff5FSRx_K7nOMeTV4vHHmvIocG4cw-tIn3mSRaKSz4qJGTUn7nNdx9JHaqUje0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌چهارم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.1K · <a href="https://t.me/Futball180TV/96154" target="_blank">📅 00:12 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96153">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">سنگال گل چهارممم زد</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/96153" target="_blank">📅 00:09 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96152">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a56fb088f1.mp4?token=qiw5sOE0VuoVX6wD7Y7gQP-g-xIDJa9fjk9PScP1yPX2tCLDwTwoI4cweEXdO4sJldbo734x7IVtwDEHngu_Gnf_-HiXVK-CCcrtTb7DRhe_RvqfA-c_oFVldtIUJitsmZs9hfxnQ5sWxSEQpATRUXwu2rQqiI4tDlMnyBGi3-mHYGzxYJ5NnlL1zLTrzkEuG99ExGzu5G9956QGGKfq190LZfweLkRsAvkrN8K4Jr91pYYyfgFSCCcmx2TLDbbG5OwXo7d4tb5Jq-75MjU_U5om9r6r2VD9gikRm9h-pVQk7F7y-MqV6gsK1pVn6IHNHVrIZCxN_u3WuxNWa9Rd-w" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
🔴
کنایه‌های تند کریم باقری به پیمان حدادی و بازیکنان پرسپولیس: بد بازی کردیم و باختیم
با صحبت حدادی شدیدا مخالفم. در یکی دو سال شرایطی خوبی نداشتیم. مذاکره با اسکوچیچ؟ این رفتار فقط در ایران است!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.1K · <a href="https://t.me/Futball180TV/96152" target="_blank">📅 00:08 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96151">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/a09e259859.mp4?token=k9CA43Ycz7IEHEugJlC8qiRINe3HnJPwtzN5RUEY8j4KSnWL81vZxxbdLQs3qUPZpnvmv6MltwDGIopaqLMsqhWOlENFYTpZRyiYN2pNqQTbSrcUmsjdHF8_FbHw6HWQgqZ4LW6OHtYnsOOSrjQrK7MNgCCxJJeXEhQ8D9f55cj8yYv4vim4_MM_tKxwXiv0Jgn-SjRJJxhcTQ0OkIk73sikmSfRM01VWmw6HpgUzcxl5eINrKBDsb_MoBykThsysF2NzqW7qUuo9HPDRBPINZnZxcH8muSLQJgPw16sHAb1C4T5pR4vWKMpAKvorCKXInHJ31ckL5Fx5Uy7l8Ping" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
❌
واکنش میثاقی به باخت پرسپولیس: مدیران پرسپولیس ابر و باد و ماه و فلک و خورشید را دیدند تا این تورنمنت برگزار شود که شاید سهمیه آسیا بگیرند و بعد به چادرملو باختند که این تیم حتی تمرین هم نکرده بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96151" target="_blank">📅 00:02 · 06 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96150">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/ea98176deb.mp4?token=movXN18faMWKeXGlNx8C9BPQnTYSt5WnJCzSfnoqwcrGG0BaLoeb4RBFiQa3Q4M06MxOccQ3HZoxTLLXL4TOMf_mgTHvzAgSyf4ZPWkREs_9b1FRluGGz-0s0P9x8raQb8zB0R7-rlBLJFhK3KU5mTYjDyzU4zHGzl-VHwQ5Wr2fa2YfMoTlXEgILJE08aVkc-tfxtdYpYm4u4WJ1pUI-bFFNdrJHsHmIsY_fqBgaKluNkS_lAvcnfMx98njESpv5HicHc0VCsiX02fDQBIdv95zoLHObCkaxK4WiiuJ46S4-Be8w2DSJYwEH9Jk-vtZwkRZCxh4aY-cOFN7Wj-urx5mdxvivYNXAQxh_pYXaMvqgtwkNmlbeb6LyMGQqtXcyde8cuAexTJ0uG4iEZRNJhF4vQ1_9wNg1SL3iN9LBA3jNPU_Zm0siVc1q6CbwaQ-HwJO63e9EkueN7wsT1sfGAkuk1OfrCFR-4PqAl22jxKnG6ePaue1WizIBPNVrex9tG9fOdsb25TimuEpFnLrgZHe1ethx5p4n373XeG2A5__C7ravlKAjexbgbyNDELWmpFKYLFPvoxiEBppDQQ8sCrCg9FH2XIt_qwibFWarPQ-4YqC4gULdvkMPmhxThlnXFVccbJ_L0d5gXsc-AdEcjbDE_6PN0CZM-0XWnI3WjA" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌سوم سنگال به عراق توسط پاپه‌گی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96150" target="_blank">📅 23:59 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96149">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/d1e0f39ac4.mp4?token=O6sNf7Zs0QPn4LaAspq2vAJrm_uC1OjZU3e3G5P0f3D1Azdq_bhZVNL8Bl6lYQ5wO3WdB8oNSJMm6K6Y9zkD2Cc0d8-WRD1QfzGyGLn59iDjvdF77-U_CLZJpuAXM_sfORKzXhPS4J1objR3OFfqXJA4BElBuZXbHJUenLpkhm_KM6oC_hla7QpG3yMMkGCNLnzm8Nr3jjLYXUqINOob_SeQdAiVI76uZsOnB730VpI1D2wM8xwGzbV_pfi5ZBgbsMAYKCRSugVXoOKjvdWqt0BEC0wFPm0nFzzP6tBoQGwpTYpu-MQfE87G8Rhw3zgzqGWaJXlJUVUOrvi6uBqknCfxx0PDUH9PHedLImBds2ztiBCZJ2SO0FXZwBcNjJyT8K04NbNO1Qudr9J1mibC9NW91MsctQ2BBvBi6xkxh1qbifhmBv73YleTxgMzNIxM4DfidlpHuEoinfOzXnlz2kVmgerVNPI0lWy_K7B8W9Gy7A670CLZuDmBO_asY5P0tmdgH-f-LatbTqAvn6vIAKU7vkcVLMQ8EgfQkChVyLVbW1XAF1MOp_pRA4pxurh0O43qEQ9XdETu-sgtXAax1pEHXeN9tSYMN_ulpynNRkX0pYs19R27Z_S-WxUuceBURG-yQT7g5saRu1QEtFolLF_Kmar4f4T4SHpHg9rZOdc" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🇸🇳
گل‌دوم سنگال به عراق توسط اسماعیل سار
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96149" target="_blank">📅 23:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96147">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">گللللللللللللل سنگال سومییییی</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96147" target="_blank">📅 23:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96144">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">سنگال دومی هم زد</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96144" target="_blank">📅 23:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96143">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/55ee125817.mp4?token=JvpOuJQfgMsjLQRVRmomcDtBBxTS-S1KWBwajpeSpDbF9O5787kgU2Galo1nJ_vsQykIykRREuOyOVTWOnDK4PwbCOhTjRYG0QIZrE7ZDFAHJnL5wzaF1HEQnWY3Uti5YyqcBhkU_KvJHFB1tH1lsrV7idfHmFZt6kboZx_aYbr0D9kpllPYxChpI9PxEchqtv1Jx7uMd-Ypajsd9mNFShfzGIxYPu6sYaGo1mVHasQywG12gYYnmObTgFDEeJGTeKhz5gJzVitiK08ZyXr52i9_13AnKN_o6TSIAUu8OVrvI3E2hvIxPgpX9iQK0Tbl1-sqrJD4RgcC50ywT2Cf6Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
⭕️
حمله شدید کریم‌باقری به بازیکنان پرسپولیس: خاک بر سرتون. لیاقت آسیا رو ندارید بی‌عرضه‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96143" target="_blank">📅 23:53 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96142">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">🚨
⭕️
حمله شدید حدادی به بازیکنان پرسپولیس
مدیرعامل پرسپولیس: این چه نوع بازی کردن است؟ مگر برایتان کم گذاشتیم؟‌بیشترین قرارداد را دارید و فقط دنبال اسم و رسم هستید؟ گاریدو، کارتال، وحید هاشمیان همگی مشکل داشتند؟  ما نتوانستیم چادرملو که سه جلسه تمرین کرده را ببریم. بدون سرمربی هم باید چادرملو را می‌بردیم. با این وضعیت بازیکنان باید بیایند فسخ کنند و بروند. قطعا خانه تکانی اساسی خواهیم داشت.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.4K · <a href="https://t.me/Futball180TV/96142" target="_blank">📅 23:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96141">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96141" target="_blank">📅 23:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96140">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96140" target="_blank">📅 23:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96139">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">پنالتی برای نروژ</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96139" target="_blank">📅 23:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96138">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">نیمه دوم بازی ها شروع شده</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96138" target="_blank">📅 23:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96137">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">🚨
فوووووووری گزارش چند انفجار در سیریک، استان هرمزگان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96137" target="_blank">📅 23:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96136">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96136" target="_blank">📅 23:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96135">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">🚨
❌
🤩
#فوری #اختصاصی_فوتبال‌180
🔻
اگر اتفاق خاصی رخ‌ندهد، اوسمار ویرا سرمربی پرسپولیس طی یک‌هفته تا ده روز آینده از هدایت سرخپوشان جدا خواهد شد. اوسمار بدلیل مشکلات خانوادگی و البته درخواست حقوق بیشتر نسبت به فصل‌قبل، موانع مهمی در مسیر تمدید قراردادش گذاشته…</div>
<div class="tg-footer">👁️ 28.4K · <a href="https://t.me/Futball180TV/96135" target="_blank">📅 23:24 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96134">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/2dd73927f8.mp4?token=BJnf2rPfoq5Lz2W2NiTxScPDiSI_Cq7q2IVW_zkUZEwDQTxoK_VuCaVm-G4UT9OVrnRbqe-WdaOK9s6Ap8Nc1MQJtKHSo_Y5IzcjAFRTzOv5Q7gFg1b-YqWzVqGPaC0mhgAVL8w5gq8q92inJ1ysQmx22yNSve4nsndOBV7CBs-QM1Xt50HGc2Vj1laHOutiKhppuOHqckl-oDY75H1oWGiUIIi6-TXgxaNLCfm0K0oX7eU_prnx8WWxmIBWYYoMbWQHuKRD-JSNqI5KXMoqAYeg3st5qWPZq8-zwqoHMZx3wuN8Tbo1_YZnkwlxEJyT-ExLF_FILqc60mE4aeyuaQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96134" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96133">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mH58lxztJ9-Aws7qDXfKEbZz5HL59mF16H89fJNtxhkIpx9WMpJHVeVMEMsaP8apdHS9jtGOPrRnD81qPqkpHX4HSJs6wM-t8JYNswACkcTDaIAFAOQVhKwqItBnNuqSqGwFCI8NIcGFJ3FKIWwSjZmPPklFaxWt2RKqSjCxZRrY_86Rrb0CbjQAniH-ePZ8wp4dXJBQhZq47VbHw-_UDYV410dV0ONAGFzaKW7n7noWBq8J_AUiBnLztZK4aw8vhOxM_flZjiVPogY1k72RFqwHekLi4mP7HjxyCBhwpuQZBjPx_H-_d3-vWYGkhELARyMPWpE-ZACaZWkqS7QKhg.jpg" alt="photo" loading="lazy"/></div>
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
جهت خرید اشتراک پیام بدید
⬇️
@kaviani_vpn
@kaviani_vpn</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96133" target="_blank">📅 23:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96132">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96132" target="_blank">📅 23:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96131">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">❤️
💙
پایان بازی پرسپولیس 1 _ 2 چادرملو
⚽️
گل‌ها: محمد امین کاظمیان( 27) برای پرسپولیس/سیروس صادقیان (56) برای چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96131" target="_blank">📅 23:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96130">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">🇫🇷
گل سوم فرانسه به نروژ هتریک دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.3K · <a href="https://t.me/Futball180TV/96130" target="_blank">📅 23:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96129">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">توپ طلای دمبوزو بدین بره</div>
<div class="tg-footer">👁️ 26.3K · <a href="https://t.me/Futball180TV/96129" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96128">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">چیکار میکنه این دمبله
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96128" target="_blank">📅 23:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96127">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">گللللللللللللل سوم فرانسه هتریککککک دمبله</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96127" target="_blank">📅 23:03 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96126">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/0786fc77e5.mp4?token=KHVgyZ4ooyccQTIBjsmsfW-uC4-xna1NT9GdOXf_iV-Ja0af7AQkpaD2e5mWu57TOvE4988-mahn-vfNh_DOFPtPS8l-2SAbt6jZqExnitN41tmcnIEorN8DtpGv8OH5N04x0e938ZoEHhylPsseBWPa_Tj4O794lgiGgebPB7aL92MZLdn1IBxde75EIxvE4UiK5i9dY39x8XTGF92-XY0Hu0GoQilyVdgu9QV-UHCKIV9EMgEkh753_KnYOSGymzLgQAQfoN_bTX5W0qigPONV_0ifqNIOZRTYZ_-rndzMncc15QFkZYq08GjIJ7vZIP0AU-7MNoAlz82hc298-n_b8kudpqfPOFINh86gg2qfEvEe41SO_r49aT8F_bTnMTcymd5YWzbwkxNmkebJOac2s_sfT8LBbVKMw76DZsXg6Wn5M1cbeIlyWjV-3hKCPfkjZr71ySGJ93ybPl1Wq5nrry5YWmVKwajhUegojksgGkQOubqemsFM4cZohvk30hssBTvRSw5j4H_Ik6bdMy6gFvy_KPd1TBcuvjduhzwKpqLD06X0fitmiUpRGqeZBU3kIC7u1iZQzAM-ER8tA_1TMmw6Y0QVGhwpUHQxfn49w_XyYu6Qyb1sAewTysLm-S2TW-7sZ5EUcx3AfMtMF8MVxwnIsZRaYLKYxH6OdLQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇳🇴
گل اول نروژ به فرانسه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.3K · <a href="https://t.me/Futball180TV/96126" target="_blank">📅 23:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96125">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/6bac1b0776.mp4?token=FSvXNOKvmsUyzy99XqfxnowKyILDr3PBa2MQ4YDKny-L-FJYZpStgZZ40Y5zh4pW6lI4RkKTetnt8Unyz8rU3dFs62FmQhG28q5_-Y6b3JtXsHcqBaskVuA62DfsoHHjgQMa7brD4YsN1Rwra7GSuTIN6I5FLYoiI-Y3lAPc4Oo5KK3R1I4VLV3HKujWlY5HAdPYtssv4q8zOitPZdxwkGNaXQUrVUk70SxLsQqejG9P2vh5W4y8uQBEZQ4ccgedDPUDR0H6uCtg5tqlB-p2NLqHk79QZrGiJsSAADtSBNylpg937Lh7-xHjoRfsyh91z-tZSZY-CBnlgIcnF61gdVJyQq-Dn55ZmjWit6SBSugoL-1ToIlKmRctRdghwUBfQKvPicErOV8satou4E2MWupR0o3ZXpXAjlf0zZRNs7m6kiPfmxMu6kA-HD9aGXcar2LGs6bFLtsIu9xziAvzYWiDBFt-jPhBCYBOQJ3nfIRDADNtqMwByxUfuq_PQcvzDewjacqeZwNd3OGnv_5KbOmOfhIJ5P-ln0xyCsvWxVMUVTrl6OBmJWers3CbTEOTeXf0ylExFccU1A2H5CvBnP7P8h8nUzS5RYWeaD_pvsDU8XAc7Km1eyTo7-s3LNbd1PCQ1x7eBNAFt9BV8dK-Br8NPaka5qYAwtYbAfULWUU" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🇫🇷
گل دوم فرانسه به نروژ دبل دمبله.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96125" target="_blank">📅 22:58 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96124">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">گللللللللللللل اول نروژژژژژ</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96124" target="_blank">📅 22:52 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96122">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">گللللللللللللل دوم فرانسهههه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96122" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96121">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">گلگلگلگلگلگلگغگ دبل دمبلهههههه</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96121" target="_blank">📅 22:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96120">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">عراق اخراجی داااددددد</div>
<div class="tg-footer">👁️ 24.3K · <a href="https://t.me/Futball180TV/96120" target="_blank">📅 22:45 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96119">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">گل اول فرانسه به نروژ توسط دمبله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 25.3K · <a href="https://t.me/Futball180TV/96119" target="_blank">📅 22:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96118">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" type="video/mp4">
</video>
<br>
<a href="https://cdn1.telesco.pe/file/dca6328400.mp4?token=myewQoUEoH8AVyfTnrcbUtUsJyiSnwHRetTC6vqQSXGJWBjLRMN7096PH5HBE-tZQxaLCqYIzrlb-Yb49QpIMMg6Qb-10QiYKyze0abD-WrFO6L0bNWQHBATEFwujqQQef6d9wezYKgGPuXjdaHscS-EmZ6bCKXWC0xR7iqcT12lKnWvd-qa68R6ZBWd6_hwESDGgKbBss4-vn4kociKu2oLRWmcIMyPGMczEt1Y99-V2Q7I0QdmIlxSCtjsAhlSHqnAWRGhDu4nm7nLAubfacS3oG5Yne11ROmLXkZJTt1YixFWwjy0IGZD7u7Ib10PU29j3DOp4u6VBlLzJRvkbawdVkKPA9I77XGjnd2AnIJhXtWDIy37061lpx-SxMyixVFiWGFxjW-s0FVas886RZFoaUUWb36jzhoaVG4sbecX6GucY-sW5MWXECCp8kdtYnsJH49VZGLnf6NADnkMfly8aO1iFOoY22YJsxmeICTpq-5nGDZVezoiKc9EiWiCqSYINE4LlzxcMjaSdVZ2haHES9HRbOx7lb0_xsg0U8BP0S5S3YkUpI8wkb5BWKpzRaB8td0xt_ZoELudmlGSeKr6OeOlkivRPcYKXPNGj2sJx5fK8GUKOjtsDJtfoUq8i3xinRkduM5R-_K4WVqvnrG_n8IE6ycj32kxno9C47c" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">گل اول سنگال به عراق
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96118" target="_blank">📅 22:39 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96117">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-text">فرانسه اولی رو زدددد دمبله</div>
<div class="tg-footer">👁️ 22.1K · <a href="https://t.me/Futball180TV/96117" target="_blank">📅 22:38 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96116">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-text">گللللللللللللل اول سنگااال زد به عراق</div>
<div class="tg-footer">👁️ 22.3K · <a href="https://t.me/Futball180TV/96116" target="_blank">📅 22:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96115">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">شروع بازی ها
نروژ و فرانسه
سنگال و عراق</div>
<div class="tg-footer">👁️ 22.8K · <a href="https://t.me/Futball180TV/96115" target="_blank">📅 22:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96114">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/HqJASjRc0G_7wy6F1LfRGXBcJxCv019XlvcDk7L-HZMsf1qlGU43u2Awsnr-hAXOND_IRQ3esVj-Rm5CxDoin3D84J_y9McVRSzJkx7RzpmZu-ZwirF-Z5enWGenrNHoBHdjvcW_-8iq9_WzEO9z0oBusYeLKSfiyRe6jhv_B8bOgy34hIdreY5Fs28o0V16Zqp_mD2LSRq9R9xlRyo-t9l6jVFwMAcMjid3B2eYm6zMJlqskKhP-Upfo5iB4hLqo17W2nMcmajXXTI5YpSBziadbVcA2XYBSAGDgQZxUav_QWebKtbIXio27M-ClXiGr3XweIUwNiXlyPgSyHBZ8w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">فک کن 15 دقیقه دیگه از این قاب جذاب سوئیچ‌ کنی رو اون قاب زشت و تکراری جام جهانی.
😂
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96114" target="_blank">📅 22:16 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96113">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/814f149c24.mp4?token=dn08eCI7db2S7-mapth74SVlOAwAJpxoqqhbVep0izAGg6oNKjewc9IBIN3T2jEFKcb8aJ5RmdFXJrJOU6Fvs5uucCrqWFi52IkuhvCG6JZd0qA2SVlVPYVVqdcVUIwuMmKe5f6rf9oOCnT_sm1JckcoGkWFLbyZ_ocrgCzP_55_iH9uXkU84I57Bg_oqYTgP0LJ0YkFgAKjhBWHFWjRTqs-Jg2itrZvAV5v57CLb-yNZhlb3URtJA2afjZc0v47rs019yeUuHNk3j41RtUXAs-3npP7PU_iLIjqThH2UsRQyfm3eG-B4cWL24sp-WfvGLDMp4tygIiKEHjj53RcLw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل اول چادرملو به پرسپولیس
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.1K · <a href="https://t.me/Futball180TV/96113" target="_blank">📅 21:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96112">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/e0b610b221.mp4?token=W9AjyscdJryL-iiJTsSQBXpoi3bPhEZZR5FqWbES3wFBl8AjvWVmdGynQL7WC-0m1MtliWSxx9M4ROnLM2VfVlxd8ujngbWAPBQNGwQqrNe3-5w1XVD-LsSxlRJOpXZgmUS2YUfVMaHzUcReQrbQFueSCphm5nHPKT2e2RVnP75a-VQJqtUCIOftp9hWBAz0xSbuRJE-DC2ZcXc7pGJ93kaXJUcyBCkSbW1A9E68JqZALqb4C9LyiAMfmEeBo0qytMbBdowuqcM7qGN7NZ_JnqinLMgy1gUK83x8uLvT1qVDYt28bJ30CR5oJcLu8BSlfb7zyO1K_O8kWKexMUvl0A" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">هوادار تیم ملی اسپانیا واسه بازی حساس با اروگوئه آماده میشه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96112" target="_blank">📅 21:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96111">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QMWUI330AA2tFW2Wpd5R18aGtlmwJmSmaAeklJ9Tc1zMlF5736HxprGrPnnD8ErmjN-cYbQ6NWdZxaxG5kKgSDnIJpVHyswL3sHo5VvRuSXutgaJ3Yx1HuZNQC3iexXjucX0R1ni4oZg_3Jlt--YqVxx1_WJKuyFvrWZd8DXVUvjkHL5PxHD-05kyvPQ3uZoVBVnmoSVwpqfrFkeExvu1Tm7j_l8p_9OyLc0Qln5Cx-0KFq05OXfmcp-3Ythh6LVK8xTQqqnC3_Y9KPNMYsUAR5gw7-dp72woIJkFhpj8vFT8Dqyv34NnviYSixWOXstV1faTLoqA7PEBPGyf6FBCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
آرسنال در حال آماده شدن برای ارائه پیشنهاد دوم به نیوکاسل برای برونو گیمارش است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.3K · <a href="https://t.me/Futball180TV/96111" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96110">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-forward">↪️ فوروارد از: <strong>Forwarded fromBetegram</strong></div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/P0GrYdVzH0SPa5bTtEqbL59nSjZWohGAeGoITM-E1j7LH2rxijAfxRkwYEq_MXsmKJDdy_yaShFzppVPsIWCU7UPzsJHzGOUyROF4LaMsna6zFoDfZ-elBqGPS85Hd38Z4eIiXZ2XUy2vTLuE8cydceOFEo991DZ2-KBP-fKVQlK6FVuRhCG1yQhYAJXx24g7FwnneWXkQ6dJi3hDq74_5MYCOZA91ekAmFya6MDBpH8KBZmSu372za8lhfTWbfpQH-7MHpwV5SXdV9zGY94VoXjiGT-z_5YeC1-gwOseG_X0U4aSsV8Qcx4oapcnSmC9sVPYvXY1G0KTuSNaRuaUA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
ایران - مصر | نبرد صعود
دو تمدن بزرگ، دو تاریخ کهن، یک میدان سرنوشت‌ساز…
این فقط یک بازی فوتبال نیست؛ جنگی برای بقا، افتخار و رسیدن به مرحله بعد است.
ایران اگر این بازی را ببرد، صعودش قطعی می‌شود؛ یعنی ۹۰ دقیقه تا یک جشن بزرگ ملی
🇮🇷
🎁
شرط رایگان ورزشی
💰
۲۶ میلیون تومان بونوس
🌍
فعالیت در ۴۹ کشور
📡
رسانه بین‌المللی
📺
پخش زنده بدون سانسور بازی داخل کانال تلگرام
📅
ششم تیر
⏰
ساعت ۶:۳۰ صبح
⚽
ایران vs مصر
صبح زود بیدار می‌شیم، چون بعضی بازی‌ها ارزش نخوابیدن دارن.
ایران برای صعود، ایران برای افتخار، ایران برای تاریخ
❤️
🇮🇷
http://betegram.com/affiliates?btag=3_l7</div>
<div class="tg-footer">👁️ 17.8K · <a href="https://t.me/Futball180TV/96110" target="_blank">📅 21:43 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96109">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/M9dqNa8RSiimuo3COOJmDcz9iPg-qdBGl9VM5ybv_L8Ou7OqKVEUUDKXcv2zidtU6ycdekZdVKKky0rHiSoUpWKD784p1xafeTTuwNynCX_c_VrKrfaDWGRFjfPcTnnxSmzGdPbd4kcQNxDcMjULjKZvDNrO9R14AWCsqb40udUUekwXP-Ot0kLZ4ULzC6Cv8yGoqYKEQhcW4P0XEbc7a3rowx4HGJebuFsqgbAM5MY38rV2T-SpXwwJUAQRoroovDnsREt9PEA6DlLXGApD-luQoq7lF_Kz4UOQGbuzX2Lf--gY1lLZOde7CSKEHD5HTjGADV-EP-P-ukw7sfq3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
رئال مادرید از فسخ قرارداد دنی سبایوس خبر داد.‌
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/96109" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96108">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/RpHk8EOKpEQHoQzQLQejpVfl83D5-DRMcvI96p1tgVE35fWgx-WmZlDpLeDzxasBZvX5ceXV3JnOp73LwGvadV_Fbes56JgPbxcuFYfOHI4hrzb6lQvTR4YzxwpFDN9vE8ekimQxhUPpJDcopVAPl2V-TRg7iwWZaO6wCVXrMxOLvikDViYz2yuqsWzcaShiNf4urNbi3H-mQ7sbrbhFjdWlRXBRF7XC2tBOQEI8b1nMrxPqUHi8gM6lk79-6MRlpIucYAHH97CQdaWmGZKUzD01_6FjaQ3o1gv1Sfb6brmBiRSx-eACTID3LaIvix4X9iL-F9rhoXIYUKK1GAzDdA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به…</div>
<div class="tg-footer">👁️ 17.1K · <a href="https://t.me/Futball180TV/96108" target="_blank">📅 21:36 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96107">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/i0QJcIWciH7Ah_oHW2JBpDdwjoThzMDdw34hOyhlzCKYXWdVoutjItV--dFvnD3A02GhxyyTawzHKiQi3hDXRdI0vQhYkLl5aV5NCpkY_z9MyvGJYgqIJm4YP9bHxlFFA64s5lqYIbTh6RbYHrM3sHDJu2Z3Zo83QxkR8vSD0Oofj24FbVDq9bdS_v5W__8F9OVtXBYDl1PeCFUVUc_Zb5QVNCtF9aUIbvYsq2fNf4guUzKP1QzWKvzZbgnWQ5VJ3-rjkYou5MV9Q8kSNpc3Rg-hLcUAeUlj7Q6o26sJrcpMGDJ73TduFST1JsjcwOgil7tuvNPPS_p5kWmC1DhMbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">مدل موی جدید پدری
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/96107" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96106">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/aAnXOpzTkQ9kQ98njGX4FYZad1t-k9easw9bLXEFXwB-fTvaL_KesSojTEofXB9tMMWOEva7bI6wRjU9C7ojkmCly7qhpWZYLHcw10Z-R6ky-Omb81qRkgYOHQtYRlAAKs7Qzgki4n0CwSuqPv25d7dozTtL5vVlQtSWcSEVxYdAy4CvsM-c43oUjrO6Y64zn3yYgvqSRI9t9g17Go078DaeTO5T9DJlGdQN0rOLzQ4OberPTPG5gTI5fDtK4Z4UNjd-sIV0pjnhCegyEwZaTHk735ifg9ag6gLOPUGBI0Fix5yai5nOHRFj4jLFSRakReJxM5yx3xMvwI4s2Z1opA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🥳
چیزی به شروع بازی
ایران
-
مصر
نمونده.
🇮🇷
⚽️
🇪🇬
⭐️
با پیش‌بینی این بازی، هم
۲ برابر
امتیاز
می‌گیری و هم وارد
قرعه‌کشی
iPhone 17
می‌شی.
📱
‌
🔥
با جمع کردن امتیاز این بازی، یک قدم به برنده شدن موتور، توپ طلا، PS5، iPhone17  و ده‌ها جایزه‌ی هیجان‌انگیز دیگه نزدیک‌تر شو.
🛵
📱
🎮
‌
فرصت رو از دست نده و همین حالا پیش‌بینیت رو ثبت کن
👇
🔗
روی «
لینک
» بزن!
@Snappofficial
🏆</div>
<div class="tg-footer">👁️ 17.9K · <a href="https://t.me/Futball180TV/96106" target="_blank">📅 21:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96105">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">🔥
🇫🇷
🏆
🇳🇴
تنها 60 دقیقه تا آغاز جدال تماشایی وایکینگ‌ها و دیکتاتور امباپه؛ از دستش ندید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.8K · <a href="https://t.me/Futball180TV/96105" target="_blank">📅 21:30 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96104">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Z7VmFu7mAdYRFepEIQ9AFt5N8QADWiOR6t-u8JvWqBIKhR5-3ohJLwB5ytPbUrxTbWCDSx4aM7UrCUn5ro1lkqwGRpltw3jHkLjeAC-peKSH9PuwIV80YtqGLiMJxg2q2s9b2Asce0Bi-iaiNuPfMkyQab4oYJ24CwuY8BJgY4ZLq_2IgcnaGAORu59Nu5yBPMKoP-Q0lOEbYkI_W8Mw-rUZ6v_EI354pEO3Yaiw82WxQ0qZcWYW71yDATwIx8f5ERPNBGlKpDNioLnkhigF3lTLb5-idC4P99q6QWY9q_mfs4L07rKEKKU1ra2lTPAe9ky2G4xR_AorVjo4UcfkKg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🔥
🇪🇸
#غیررسمی
؛ به ترتیب از چپ به راست: پیراهن‌های اول، دوم، سوم و چهارم بارسلونا برای فصل ۲۰۲۶/۲۷
⁉️
کدومش پسنده با ریکشن نشون بدید:
اول
❤️
دوم
👍
سوم
👏🏻
چهارم
🤯
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96104" target="_blank">📅 21:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96103">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">🏐
✔️
ست چهارم ایران برد.   ژاپن
2️⃣
-  ایران
2️⃣
🇯🇵
25 | 25 | 20 | 23 |
🇮🇷
19 | 19 | 25 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21K · <a href="https://t.me/Futball180TV/96103" target="_blank">📅 21:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96101">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/uROpMAOzzNZHfUmS6Ma7N0qBbFoJmf1aKHJtBYMoh5yBayiMBPvXxRqI7QwL8MCBccWkmJfqwZEoUWG_fbZZrgVxpkSLt8kvJm3goGHkABqI_ylEKxHGBNXo6qpr6zfFezbJ3jhodRnLhr_wEH7s-1GN9uRHD6vewou9RLveeNjGAmOD3EhirTEpl9mrAMqP9cYAsEp9vEJ6AuwoacGRz3tyBGXizOuTPQCYpOEiUy5b-pif8A53lMYnVfeB_0ZCTN4wFnvl_hElZ4IGAKkyqd5NEzhDmyg-DVovuzTtuR5IPV8-qXaASAMd_XqpW17APw_5JQzIImapSvp-Fn0PQg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/eIw8oXDJychXXI-W5Bao5BhqklYsWmPciFK9QDSWWvpDC96ZeO2IWZJeVnwcuPYTAwHruEGj8QqaK3_7G-Bahtf6F78xytMNbKbfSGZoehztvaLJfUUnx_YfZSCYTq3AS4q-_NSrej5W_1nUOTSUttndKP2eAh46uCcO43yIngaq3GMXGDfoSHCpI-rF0fdkWprWqNvOTDJ6XHKHpqduk2yFmilnXqB_kIL0tVEVlAK7su9QSoAlUUkHgbRizoW0d3S1xWQvfF9zSbSpzT-79IN4e26hoKqIPLPUR236G6Fhb70DxrhrIH6UvQ05ylJMHblqmNgX1s5Tm_wc96q73Q.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">🚨
🚨
🚨
🇫🇷
🏆
🇳🇴
ترکیب‌رسمی دو تیم فرانسه و نروژ با حضور نفرات ذخیره وایکینگ‌ها
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.7K · <a href="https://t.me/Futball180TV/96101" target="_blank">📅 21:07 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96100">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/u95lYFMbbhkr7ZJ6BGLc0RhSD6lZtpjlvQ3Kxbwgz3fOpfzv4sMURdVv8ClH1lPLW5vHn3bgmUVi0D0JgvPv2YDnB-XhOdOaAAefy0DszQ0967mBGgUtp5vJIGSJTl3Q56VglgJ9N0yD8AFH4J2wDwzCaTnaIw0EXbSK7KxaJSHZSXV__4wZspbhAevVG4Z2fYDejRmmP_VTFwnb8soOkk8DeJF6gu_a8Pk4HYDwzIv_WJ7quUPfwl-iTC52UFi6HteJmS5X3aPy42m2UrkjBsai4duextrtEZCCq1YHKrzauSdUdL046VlNDShPaQNa8kThk9ARPnnqqt76n-MnbA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26.8K · <a href="https://t.me/Futball180TV/96100" target="_blank">📅 21:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96099">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/PGyrIvokg3wK_IEwXmTt9nBuE8f9uPnpO5kBPQWKmQJTGIa9fsVwgbF4uhyG12mEql19b8MdwnNSk3hw7TPyTz9sYYIwolNduiR8aGNGmfF2EI0rdOaa1A8wTxxxh_mvVoF5fwNy9s-mYDzfMR48GO-vWtpZDAN9EWLmCvIdI3H4MVqwZbNPaNe1ffVEeqqc52X7hhPeqT9xohlwoKOiuKfVe-hGrCMjQFCyf7BeSrd-btWIa1GxUcgoAZNuMrbTisnqfUinNR8cLZP4VhIVBV2aVD7z0vgmF6vGYc1y5ezehZGMKcLW5qdXYkU4UURw4Czgw8zD2z8Rw3hDpN7drw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇶
🏆
ترکیب تیم‌ملی عراق مقابل سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.6K · <a href="https://t.me/Futball180TV/96099" target="_blank">📅 21:04 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96098">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=IC8th0KgvX9PKGKqBLNja1BRHb82kTobTRxhE5Q2tVodBiKTmvSd48SRC5zG37t2lM3YvC8diiG7DmEvNscF91SsRIsKnVYgkg_xHs12C7GbUlagJ1Lcck-qtVquRLrpGWit8Ua15WY6pcqFAVzINM6Hgr-LCa1xlDVP9-RyGdcCnO5ZSzzktAVV1WLOfh28dcdCVxKI_rZKb8Ynirhy1gOtVC8fvn2l4qaut1hfyF74mXoIAnqdW2AmhA3eOf1NAnNC3gI7cYeF3fbsVoLJ_-OmLvg0J-8lvLW6jYIAVhFiFVVRco8XJfbLg086UM0nFgE8mB5dOF4YqUgkh5sd0D529OT3P41zrA9Dv2A-gHYk282ilBVRIbG5Xmd6wjwnJTkUjwluVKhDcT8z0OD9mPiG4WRduyWOuqY-wALrKULJzxzL1YiL-9SVZAB5X75Yr__BOcKg7XmsRb7AIia4KWb_Y1_q7hmTLnv_gHkLqW4WjbcU1m2BoR64XRCY6Bcht2-OHuG4LPNR_3JiXSdgznxjDIguj-vNe-Ri44TnmKH8_y7KAA_5Ynr5McPyTgEbpfe6rm_rXWaoDouGEBoMbCFh2gmP-A764kbxDU0MiIXqThN6XNZ2h1WrKpJAj_51nbNNRDsuwCfQqwts5Z8OiW0qvT7STqDvjHcimHfwqB4" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/fc25ce70cb.mp4?token=IC8th0KgvX9PKGKqBLNja1BRHb82kTobTRxhE5Q2tVodBiKTmvSd48SRC5zG37t2lM3YvC8diiG7DmEvNscF91SsRIsKnVYgkg_xHs12C7GbUlagJ1Lcck-qtVquRLrpGWit8Ua15WY6pcqFAVzINM6Hgr-LCa1xlDVP9-RyGdcCnO5ZSzzktAVV1WLOfh28dcdCVxKI_rZKb8Ynirhy1gOtVC8fvn2l4qaut1hfyF74mXoIAnqdW2AmhA3eOf1NAnNC3gI7cYeF3fbsVoLJ_-OmLvg0J-8lvLW6jYIAVhFiFVVRco8XJfbLg086UM0nFgE8mB5dOF4YqUgkh5sd0D529OT3P41zrA9Dv2A-gHYk282ilBVRIbG5Xmd6wjwnJTkUjwluVKhDcT8z0OD9mPiG4WRduyWOuqY-wALrKULJzxzL1YiL-9SVZAB5X75Yr__BOcKg7XmsRb7AIia4KWb_Y1_q7hmTLnv_gHkLqW4WjbcU1m2BoR64XRCY6Bcht2-OHuG4LPNR_3JiXSdgznxjDIguj-vNe-Ri44TnmKH8_y7KAA_5Ynr5McPyTgEbpfe6rm_rXWaoDouGEBoMbCFh2gmP-A764kbxDU0MiIXqThN6XNZ2h1WrKpJAj_51nbNNRDsuwCfQqwts5Z8OiW0qvT7STqDvjHcimHfwqB4" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
🤩
گل‌اول پرسپولیس به چادرملو اردکان
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96098" target="_blank">📅 21:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96097">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kZzk8Jw5DMVbONB9zr9x2Ej9rvzAcokY4MUrYECab3FYm-dXsEStC3nhzmWL0-s13IceSYLER7Q_51akR4YgnU3tZo2M5PoYnRrjUqYoI-J_ICGmLiakvzvEXceCrngn2nG23v7kw1oY6kZipDTPo9EFNwr9QIJnBxqFsuYj27bil02bLw3YI_HGYrNu90bn9qUmJziCwprZjpNBpIg0wryHOS0vPaUvtlByrCGihR58cxKRWS4_jkvMHhTnmLzVb5NFmj2bAVD1z188Ir5wdub6qZB0JOvKV0oYPqRTINN5IV_IyGoFrC2APNPzIrxEx074FWFym14wYUjyAed5ig.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">جسیکا آلبای عزیز که اول صبحم تو استادیوم بودن مصداق بارز جمله مادرو ببین دخترو بگیر هستن. البته تو این مورد باید مادرم گرفت
🐸
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 26K · <a href="https://t.me/Futball180TV/96097" target="_blank">📅 21:00 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96096">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/rPetOGyMePb9gLzycnOyTKrMbdILIhsZVUokiUMOPpHb2chGAyRxElg-nEgESirmEv_64iPjFojIXWo6jcrP38Pz4r7clViGpCtmv-UNJdca9Ny5oQUFap3DTomJp8ej6LFT1RJn5aRkuEI3P5-2_90l6UEAn-_6kLwHdtOMkikE9LZJwvg9uoqG54_4SYcs-9mtYOJwbpD082jEjCug1CJirOYF7ddLJaaFzZuWwXTG1460eUtcrfPSUrXqxU-k87WGlGW8Br88Wow-sFooawUmKmRye8GjqID8xJ2Idy-B1EMHJivrdHO9gA2c7xbIiOwj9FfKoxoAmUcWCya3YQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
‼️
🇮🇶
عراقی‌ها در آستانه بازی با سنگال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.4K · <a href="https://t.me/Futball180TV/96096" target="_blank">📅 20:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96094">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-text">🏐
✔️
ست سوم ایران برد.   ژاپن
2️⃣
-  ایران
1️⃣
🇯🇵
25 | 25 | 20 |
🇮🇷
19 | 19 | 25 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 27.9K · <a href="https://t.me/Futball180TV/96094" target="_blank">📅 20:49 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96093">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/pbxjoNe4R28HVhkEcX7ljBj765X1MTOKW2m6oSHyt1p48YE21fpXDTqwR_zqGXROsfnsxi4xH9t2QF7Chulp6x-s-itJ_BcjctUeGHN_M82DB9svkqLBvKSk_ljkSr2eruGXABzIPvED3oqV1vYlLol4yR2F4A2juq3359OjSHkXoFb8f0-wk2JMjmYQnLpolTkp1bFU9aie8_FLlcjryNqCKriPkWOwzQ-Xg2n_01ZZk8b_to5ZYEgdLmSabySbKEdTrBgP90EWwNLhJRxXTVaE4AS9jqzKQYPFlutmTT0C3cvN-6pqr6VN3o2m4A5CZjthDOBGLXoIOaDfqb5upg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇮🇹
🇫🇷
💸
#تکمیلی؛ میلان برای تکمیل قرارداد رقم ۵۰ میلیون یورو پرداخت کرد و قرارداد تا سال ۲۰۳۱ خواهد بود
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.3K · <a href="https://t.me/Futball180TV/96093" target="_blank">📅 20:37 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96092">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.6K · <a href="https://t.me/Futball180TV/96092" target="_blank">📅 20:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96091">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A53f6AKXzEaEP69DSwDbPmcY-p_J6L7elAPp5LXY3AJj9sfiizj3WQre1vUMhFo85TvwE1QBFixzFzpGGbtJcs6BL7VVr3ZVtcbf9kG0Vh858cXZJcYBIoZAFDumT3LlBaQjhKXMp_fwK6HmihjamOcKVy9uDJvg-drYcC3x8tJLhg-zdieVcl424Lg37p3rz__AZVmMCBRLsSgFGQ4ur-iffVQwYiUudpbktWMJV8aW9Mt4mJqmDZ5JYCgp7i6rbQxemmWl5OkGD9770h97-gJS3vVSc5Wpgrin7yKl3d91-QSIpfXgo3soajR3ST2ykSi7oEFV6XO48vIqVHAIoA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
🇮🇹
#فوووووری
؛ با اعلام‌ رومانو گونزالو راموس مهاجم پرتغالی PSG به میلان پیوست
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 24.2K · <a href="https://t.me/Futball180TV/96091" target="_blank">📅 20:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96090">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/AXpswmY-IlhTY343ze_aW4gLFnmQwxsARDdHPyUDm4lvvKs6ufU3p8duRmr1XyuJAKHB78ml6QjF_Odfjl3jLlA2NML9OxtgYOSkrZQJH7aaSxJXHpzjXOzXpV2vwTUTT3s0wwQXgVKTD-SFPsgZaLjDWaG9OXDSX0IO_Qe-BkZXlg9xFNB1qQGHtcVh4DxPD6LLWoZXzLhe0p6k2uG-YtONFvbslby36e7zSMx8XSAEHkYTa87xtlW4HgblA3VwvDzGIU2CzAKne8MpozsMgFT_iwvGe8eBwGEhxJs15yfMSfZE13C7XLVSy25IoqgKG1cckhOgvd65V4r96lab2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
🔺
۱۰ سال پیش در چنین‌روزی لیونل مسی از تیم ملی آرژانتین خداحافظی کرد.
🎙
مصاحبه لئو مسی: «من تمام تلاشم رو کردم. چهار فینال بود و نتوانستم برنده شوم. هر کاری که در توانم بود انجام دادم. این بیشتر از هر کس دیگری مرا آزار می‌دهد. من بیشتر از هر کس دیگری می‌خواستم با تیم ملی قهرمان شوم، اما متأسفانه این اتفاق نیفتاد.»
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 28.6K · <a href="https://t.me/Futball180TV/96090" target="_blank">📅 20:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96089">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/OKop7afHF2K_bRlhLEd-He6GXFMGHX9UaiF4vaJhdI1uqnQCafWzaWXKfLsjGLFLQEKee3AiX3RoG3aRnHPn42lC1sUbRl53SAzWFstBW3OpyAyFtXnqp5ZAwWnQpxLW8kSFzqrLoJai3DU4612ovXXq8vwltqwPduHjnnrsqu7NilRhUd9JSjLPH92JkAwU6ivq8mjqTzL1GgG4yz1mTe4jhb0OC60s9wRvSew39Ge20E8OPAmO-8Q6YGgts6_3gHxziAR04CWIuSB26jwWnHXE3cBOjgNfj4rnIhp-9RAHOQhShCxNOg8dULV-j_VNap--qE55QGzDXl2bJaKVUg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🗞
🏴󠁧󠁢󠁥󠁮󠁧󠁿
#فوووووری
؛ نیوکاسل یونایتد با ارائه پیشنهادی به ارزش ۸۵ میلیون یورو بدنبال عقد قرارداد با انمچا ستاره تیم‌ملی آلمان است
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 36.7K · <a href="https://t.me/Futball180TV/96089" target="_blank">📅 20:23 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96088">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/XgPalmdBZ_Y652rNXy178GYE7hMjBAjgkkwoXpljKl5dz9wjZsuUxxLzed-z4X1R6O7ZCMiDy03vLzVEYa-roy7CA2zVWerDBAAbnYk-Gw2DUuAGzOGBlmzTEpesKYbb0AQujGFICNOo26Y9qsQLLn2QWQeV1KGDI_wGcooa0vUU4shMjuijfUlc-32wjHUKhPOTTQWwpR9c9xwlAJd-_2682X2e_bbI1zGi827TFbBR2fUaYT59s3Dpe2g2dv_ubx03o3N7Z9OKSW8ZJIuO2nCkl4OoFO8LCN20AjFOZxB5VXc2ZO1HqEZZw-mZfQvVMOBJV0yPgZ9g7LAyrIe0oQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤯
🇲🇽
پشماتوووون فر بخوره؛ یه‌زن مکزیکی برا اینکه شوهرش رو سوپرایز کنه و بلیت جام‌جهانی بخره، یک هفته قبل مسابقات عکس پاهای خودش رو‌ به مردان کشورهای مختلف می‌فروخته و از این طریق تونسته درآمد زیادی کسب کنه و علاوه بر کیر زدن به مردان هول خریدار، شوهرش رو به بازیای جام‌جهانی ببره
😂
😂
😐
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 41.1K · <a href="https://t.me/Futball180TV/96088" target="_blank">📅 20:13 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96087">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">🏐
❌
ست دوم هم ایران باخت.   ژاپن
2️⃣
-  ایران
0️⃣
🇯🇵
25 | 25 |
🇮🇷
19 | 19 |
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 38.7K · <a href="https://t.me/Futball180TV/96087" target="_blank">📅 20:09 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96085">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/XS8Z909ypHlHC6lTYVyKwKQ9c2LMyZXvl1tvSa9Peh8rmX-8OuoX2CkfkcdnkOIqMZm6YP_W5Rs9Hi4tLfclS190ZAWZAjkSW68ryXFFApVLS7VDr5dExgXrKmo77FiOHQhlMY3Vgs-yRHM4Ssq0W1alpCjvLIqEek51rskUYQtH1Snk30lKV6lpMISjWVKQzZ-CH3HdeowqCbDPyYkHY8re4XB9DqpV2tBcv8ZqmL-diG8orkLntYsED_DCmwberWw4MzBEPovKIKcm8iTklQ-hEn5yaP1WgfslMLYVy3PgP0imiksbcMzShP3puRe0K008_7S0GUPxNRzSJ-lwdw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/howNci1C8YQ2kiTBvEEmvWQmMko_twoMk7kYQXOn-x_s0iKBGGOwJsTHlcFL4TaJrXBfVJJ7Mj-yEliPu8Rm9a6p8VyKshf7zdELiLvrWl3Nod1Xb74AsXYw-RvkJMe-GbtiZpY_B6ad3HCobkH_SHF85ZF0DAAlGa5J_zKTXByWxNFCel3nVC7zaitXVVoMJjvHxHiGtBYfAzszsm7-xVz1M9_a_PSgGwZTwGfu3HJ0-V6qsMkJH6T4JkZdu4ENrDRgQDJkej49ILEY7BA0KdnyVxQyMMHvQwXJO-gf6WaukxFhphn-xkRCSuXt_ZEUQNr1XUu-kVmH_-F03tztBg.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">‼️
پشمامممممممم
برونا مندوزا مدل ترنس برزیلی گفته که حدود دو سال با یکی از بازیکنان تیم‌ملی برزیل به صورت مخفیانه رابطه داشته.
🔺
به گفته او این فوتبالیست ترس زیادی از افشای رابطش داشته در حدی که قراردادی 500 هزار دلاری بسته تا رابطشون محرمانه بمونه.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 33.4K · <a href="https://t.me/Futball180TV/96085" target="_blank">📅 20:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96079">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ZZFkZhsr39uLFmc5AP4FiM77aFR-7eZFWhlxNLx26PSzXAybOLTMQZOcomYiiyhW3VLLT39ziATYDioP4e2dlkVEhXBEdywWob5SvD8tC03LlY-ITLU39tPijouzzibBnSucUJLJK3OKPOQ7medQPxGC_g4ggb96_tPmqYRlGWGgBPOFDIpjbcUkwyB1e--mhK6ZvHXIU0LjIW5uGbO60FYhV098suGNXAoODriM1ZATvxE4OaHbdUves6YmvW98gmVjlViRLFpu7YyFINOeg-HElDuzK65guVmilXWjVoXXgAizqT06ZdCKbdK4eyj-mw9NWi3qbpCn4UjtSXsLCw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/FlTAHx_kSk7uKy9MWlMN8vTjIu2B0OecDMVzxRUymF88Sh3ZaVIyGdvTwBFKOXC6OF0WzMypp1tw34fjtaG5d0Zj11CXHwGb9rEiBgnoSqzkHjJIakuEu7jx3keNXn3cBplFoSg-Oi7GyI-k_A-VKzLpR0TUmIbBYrmVbGFmAP-POl8c-pB_hx8baqtXYUHsy3GSFQNrYLjT0R1wb5am3FU8eStCEDiiT2tIOhE2Ro6G2Ll-9oZPAX6NUdaMIc-7ux-gorg8FO6hoBdZN1ZVvBdoy9Nt-AgvXb5Yg3LJAaKdBI8EHky6eoFciZ3GWVPOe89k2QhWkpXY5JhYUlGQIA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/C8AIn9YzkfYkaMzxfzfnjmMir26iIywTlOXeu6tJm0ykiaH5RGFpn-KVYRXO3n7uflue_Z8-_07Oyh8D67o6fCjwtCUY5ZEWA8mGBPCyzqLmxP145JPnjb0Yu6LMJKjxVmf5f8pW0EdLBl-pIzH5KWX2REYw4a8a1_bsZMWS8yT41elbmgwyr_DjPc8RRGOwYHeJJKjdkTUegHqs1TYBDJNC0195g555XxQdhYXm2mbUe7ksk5JbOWY5VyIAK07aXemvd8fUaCQu2exLn_Mx4_FtGYrj9nOw6swsT0xGRC4GUVvdq6neIWotJy30X4WMxwGQ3vh6Q62BMpxxDAxK2g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/lCm9zY0WqTa0T2n_C_QXyGOFa-PINAck1nVBF4LhvRoEINHEMgsoRKg81v8l0vE1Z13MsmivGWJTDHGYGH0Sx0pYv83wJdbTKO1UZZlhmXNNHOjbyA6g0AffJMQJD3lo8xMiCKfI6BqDGWKgnQixavftrMUxqDZXSKsVQySbgyRFNqwoVAhWRhGS7jVCzoanhpKKfPEAWD_-zJDPri7jA97o4jiFSQ8TeEII1_L1qn-k3wqzOpSfrKrXT4_99KRUk2ljHwi9gZY4w8MBW0BvntolCjRqszcBwsIJqGE83DHYhC7mgKJbNLwkYf-GwKASvwSWwlrPk8390ZDJqLggDQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/3d565175c8.mp4?token=iW_ErVzodVI56hLeJgJwYLdyXiDHUQzsQEVkpOo5O6gprXUWNm0tNj-jI5aWmxmtQ9D3WGeBUnGFc0sBpNNBeS10W_TY0b3itWc9xNXfonCEjKMsjuryrMjvP3V0cvq7XJIc-AaFSYZhuvf7QUBEwaLcdQbJD2y6WiPb2w_PkyYYnU8EC1ATPI_tMg-6Bw_wq5yiPNtIyAaGd9d28bnBFBPtpFDFHlPhv7HiR1VNLJqxM7tllwfWrYQi-HpPPOa5DVUHLD3u3Uw2EEmxcPZr9pOywRQVuXjP84ZSMFWj9VLtPLzHJRe-CwpM4nxIQu2Zd5j26njVvceIlULkks8uHw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">✔️
👀
یکی از خفن‌ترین قابلیت‌های گرافیکی GTA 6 سیستم نورپردازی و بازتاب‌های واقع‌گرایانه‌شه.
نور خورشید، چراغ ماشین‌ها، بارون، شیشه‌ها و حتی آب، همشون فوق‌العاده طبیعی به نظر میان.
از اون طرف انیمیشن چهره و جزئیات محیط هم انقدر دقیق شده که بعضی صحنه‌ها بیشتر شبیه فیلمه تا بازی!
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 31.5K · <a href="https://t.me/Futball180TV/96079" target="_blank">📅 19:47 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96078">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96078" target="_blank">📅 19:34 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96077">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ibtkV2uMDKEJ9qkm1CO9eDfwbg_K9_3j3TwVnzQlKBITbPKnkeuQoXzeVuE-u1me8xmjAHF96qelD7ENe3Dzw0P4r1gIylA_C04Eh7iR_ANckD-Fzluhe3b91vzMDSofuVOU3VOgeBibQg58edGFvm5eszclF5uy5OGnCglACpdQIZJPu56hP-AbuMkntepdZcus6M4Dutez5_9y9brGRKYQrJfDvUA3cm9dW3qU9eQTd83u95L8mJ0BzasIAAfwNzSy_h54PKKVpJC58PMPJUmZdachZ5n-FCGAhkbzWSTmKBbzN7GzMYrE_IqbkjxIVcqMmg-7zjfsmY2-UlIqNQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🤩
🤩
لیست‌کامل بازی پرسپولیس و چادرملو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.9K · <a href="https://t.me/Futball180TV/96077" target="_blank">📅 19:27 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96076">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-text">🚨
🇮🇷
🇪🇬
فوری: تیم‌های ملی مصر و ایران اعلام کردند که در صورت مشاهده هرگونه شعار غیرمجاز یا نمایش مرتبط با جامعه همجنس‌گرایان برای بازیکنان یا کارکنانشان، از زمین مسابقه خارج خواهند شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96076" target="_blank">📅 19:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96075">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🏐
❌
ست اول والیبال؛ باخت ایران
🇮🇷
19
🇯🇵
25
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.9K · <a href="https://t.me/Futball180TV/96075" target="_blank">📅 19:01 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96074">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/gf4e52x9tU5EVT02h-wh96EIlMWfLrXnojOwOCS8QxDwM41Mi-Qo24hww0v5dP6LrW2iXDDgWGr8upG5ZkQWHxH4vemVaAkmh1TGfum3Bxs-Wo4u4groBm15pQxnM53470m6u8OBLvNGDf6W1l763wmG5KSzebK9SX4U3cBC3CMMqfNQoOH8RVYZed_GzC6DTXhNk_oiCM_1Hi19M_QcinnawUxTrRmVPz27Unp2bhn-QOGfhqokyu59YB12idbGfrWhVXMkPOJpsU3DR-mCi7-5T9y1fU3S_CCizbmwk2kFVoBRnID7KGsTq5d5QIyT1ZDgcaLW8Jz9k5HWupRUKw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇳🇴
اکیپ:
نروژ با ترکیب ذخیره مقابل فرانسه بازی خواهد کرد. 10 بازیکن از جمله هالند و اودگارد استراحت خواهند کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 30.6K · <a href="https://t.me/Futball180TV/96074" target="_blank">📅 18:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96073">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/nc5Ws6bF-3sFDFMdIch901h92ub0nI7qCi_nJHNuysnnAED7XfoIOw8W22CrLl07nxPsoPYzOzDo8SuxGnrd2TI1mbOST_5XWNwQ0wbdnEEG4ZPueZJdgQSWYVxpyoL6v0C2PSwlvStT2I0jgkducx8n7gFEjKlNG8PTzTLVlhGb7XzdwE44VOxhLRC8gHPsTGm8HRjYi6hpmdAAANE9PG3eSHrp8Qu8zax9lgjfUsfNXRJgEWXf3dis0CV0jhgjNZfuVsooozOsoTFYk1fNXEsljxbDM9vHxtDvVmtX0NtzIux-Pg7_gQLf64TYhmCXPWRhxwB2yDruoAcshZ3JDA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">لئو دیاز خبرنگار برزیلی : پدر رافینیا از حق‌وحقوق مربوط به تصویر و تبلیغات پسرش سوءاستفاده کرده و حدود 80 درصد درآمدهای اون رو دزدیده، ظاهراً این موضوع زمانی لو رفته که رافینیا و همسرش میخواستن یک عمارت بزرگ بخرن و متوجه شدن با مشکلات مالی روبه‌رو هستند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96073" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96072">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/Mhbax81DLv_bpHr_Pehqfg8e2ESIQzHkT2VMGpn77lGAJV1cD-lbOegqqEhGawpXC2AILBK_XyHK5LBsHZl7sN5niv0IAj33aBDwCKVCBebUYopLZXRS_3iooaPxZQqe_ufBknliT4S7ExepRrNWv_hlu5qbx1BZnVnEK_yGo8JVFONv3_LeKbV0-7ex9cJnS3VkAWAM0jVbyxSwIk3V7LoReBiFUtcYygs_gUqoq5jrIobVtkLpGtIrlV-GVRhaEVEmYwMeUcAEtft0k1NRfc4pz56W0FSXARum_CKcQogXNrPMub5joTnjrJfcyToar4QWT4aVbNPFewwdldg_5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🇦🇷
مسی
18 گل در 5 جام جهانی
5 گل در این جام
34% شانس بردن کفش طلا در پلی مارکت
⚡️
در برابر
⚡️
🇫🇷
امباپه
16 گل در 3 جام جهانی
4 گل در این جام
31.5% شانس بردن کفش طلا در پلی مارکت
⚽️
حالا پیش‌بینی کن چه کسی کفش طلا می‌بره؟
شرط بندی روی بازارهای پلی مارکت از تلگرام تو کمتر از 30 ثانیه
👇
https://t.me/PolyBaaz_Bot</div>
<div class="tg-footer">👁️ 21.2K · <a href="https://t.me/Futball180TV/96072" target="_blank">📅 18:55 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96071">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/BUAg6asPR-QTQcd1xyRRxR-jRht0ZzuQqJHvSo_-CXvqh9NJUDUC-fwmAH_ajha_ZvdwVloHRbU2_WLQc7My40eLjh2lGFXHHQkgQkjeG3et5zoiOqmWDq82q7Tmg8HW0FiBsNm4IB86VDwoVKm8juFM_GkiHG8arm2YVa1r-mKF96lb0JnVY2c_cWmF7atE2fKRh3t9m_Xr_oDc9rH5VnJ3W0nfPa1wyH--s9s54npSaI8GQSfvTaikU-WON18-JevKzQRnxNLKZyrjRXmMlvsCocqhw_1v_RGZpFN9C4PlMgwxyzHuY2dR2T_lcEbKiqra9F9HsUBBI_nAfQXMHw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">وضعیت ترکیه تو مرحله گروهی جام‌جهانی:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96071" target="_blank">📅 18:44 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96070">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=r-RC2ufTdi6-urvCsOxPyVkLCU8_W1_p9pWR6zCocGca8_gpe2CG6XicuuTlkAuOsVHHWIvYGe21hmhiXsU87jNQURjljBiYNYuoF5tOURTtFL5djyin2H4734aXus_p0beTypXiPMO-GhONOeSh2OXfHR1_Z4n1GVi4-29B-X80kNUht7n5Eo0Q9RCctFN6rogT0tCRe0b-GQOKHWhm-KF1JwlBTZc0Od6SAoDPZ1yWFoFHYKwpBIh5kVvls0h8geXIo1MN_siKD6bViVcwAYXVs_J-KtwJHio6Q0RQJPGIaJ48m-Jq9c4OlDq2O2LZQY6Cdf_h9NIo3L1Tra7AYg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/dd55ccb496.mp4?token=r-RC2ufTdi6-urvCsOxPyVkLCU8_W1_p9pWR6zCocGca8_gpe2CG6XicuuTlkAuOsVHHWIvYGe21hmhiXsU87jNQURjljBiYNYuoF5tOURTtFL5djyin2H4734aXus_p0beTypXiPMO-GhONOeSh2OXfHR1_Z4n1GVi4-29B-X80kNUht7n5Eo0Q9RCctFN6rogT0tCRe0b-GQOKHWhm-KF1JwlBTZc0Od6SAoDPZ1yWFoFHYKwpBIh5kVvls0h8geXIo1MN_siKD6bViVcwAYXVs_J-KtwJHio6Q0RQJPGIaJ48m-Jq9c4OlDq2O2LZQY6Cdf_h9NIo3L1Tra7AYg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
اکوادوریا به این شکل تانک آوردن کف خیابون تا صعودشون رو به مرحله بعدی جام‌جهانی جشن بگیرن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.1K · <a href="https://t.me/Futball180TV/96070" target="_blank">📅 18:33 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96069">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/n512GmOh7xRHIiQP9l1JDPw60Xa0U-_EgCFoD8TZR5X8jloabiTMt36j5Qxa26CeeGQ_NeisDYqH1wOTPS22g4FLJ1EAf-zIrR9rgSMORadVJx_bWZ2f1LyG-brJ2Hp8YSXvGY9FBq5iyyW7Ugx-DnTzftGej_fVChPp3IcGQ6ueKkUjslhYF6tCE381dQm-mN3Dl6772HT67Y3Tt5ecRuq4GzdfxsZDwmY0fBWn_WP_qCKjJzHy9YqRvBwAqDP75NUUpGPsUaBCvm5NzSm-1kzwfi_Cn9cdk5tS7HHRldP5onh-lL8zT5oOSSyAULbDkODL4BGu-a-GB7cSMKubag.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🏆
⬛️
🇺🇸
#فوووووری
؛ ایالات متحده آمریکا بزودی با ارائه برنامه‌هایش کاندید میزبانی جام‌جهانی ۲۰۳۸ خواهد شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.2K · <a href="https://t.me/Futball180TV/96069" target="_blank">📅 18:11 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96068">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/b6FgFHqiE6mJDUZXwTBoWTNSITdR5wlk7g8czFeLE2zSPMYAM62U9u_hY4TN38ypK31xICl1BOyDKCjvN11DxEbf6zopLhfaFDhsChG0DUktBHxFRH_6_1lhlzmRapXDOmnJ-3gAi0dSFbqriIg4O1MfASAomfX2OSec06TWygvFSsK-zGCRxd2SGbsKe_qXd_rWne6qIRam8vvQajoDy1T51q-XbQ_f4BmW6TPwxIitaTRoLk2hsTgQCbFMHORXXLf8XtpJ0ioHyOx83Mzoe2_A_VW8lISPfM8w-7G_Ujcr4tjB-mVZ-KeDs8RT0zVdrYjMzR_8IXU1WJxBhxDO5w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
هنوز کلی وقت تا شروع بازی ایران مونده ولی رژه همجنسگرایان شروع شده و هر خیابون رندوم تو سیاتل این شکلی شده:
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 23.2K · <a href="https://t.me/Futball180TV/96068" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96061">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Nej32h3pXDXdOBJ57iGfO4vPE0YbUTztKeaFJgxwKgE2S4xSAFw678SY6v99XIJtfQBlRGUilg6XejzEyL5ssUNoBRMWp-YKKwiq9bi7jRnSKA-64Ee-hzOulvWu5oc1DOEtGq6xj28rTiqITg_z-WnzCSrHqzpr5_oMBfeteZjswwIBVWGPrsz7DpXYbq7uSpoaSxEIaeSK0v_vkkZUDi-5Skg_Ha0mI8PU2IzpCxAcGzz1BF-0_vQp-a1f4anE9TNujBtiB2iYzr-Lt1auiQCh3HjN-hKx9bu3kf54fLPE-6dWC_YZy2HfW0unsH7aTcBEO5MHQzDWqX8h9_DFJw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ssSgPbvPbnfjUmYUDlnY4JQJgttqHnvB3ClhnvrWXYKSFMcttNqxsov8wDJK2VVJd-7rE81sndNYKKE-L2COKptub8v8DcPp2Hj7w7Ux6nZnA07iugC1XiIuCCG670b-Xz4I0cLcwfDTWIorRNwfF5CyXsfhIoi_HX2m4N0uv5q4H-ZkI-DnmgtfCyz1c1BM-5cFzHCFqjrg1uer1czR6o53Nm3sKJjSVyBeLg4zy589x9eAdN4g7xOrJxA1AafKasZgpyE4X1IJEcc2VgoYWQJo2OoRBMZPPBJiVABXD1HqFPsKWt-majGOW9WZxG9QDtJDiadNlmMXtFUqOTnaDQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/kAWA-X8ZIZQSw9IhyfPNdQY9fk5nR20Ud_GJjnmQxSuoBGwzPDSJx2lECovTbOn6IotsYIbRpDgF45TbdDc_yNBWVKPV-IYFIc3s0O_CkDnMVdhM37DOW7eK-xD1R7kL8USA5W1oVD4lIoGkUA6phvJ2fiyNjEjA_swaXqS_ndbdkjtyrV9OqXaoRaWQp_8px3uWUAcSc26SahB8963K1MzBKHh1Oa3xtoBFiuTzyP4SZ71v6VgG7L1_tquJyPhgT29k06vF2sD5rHB7ZLCv0nzxwsHLtxumvARjcvX20cLJ-kGwceM8vIQiye4hqwmWZ1t7bd93ySuIjBhkb3caJg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ihBPjy0PU3Ggb0Ai_mpu3RYncMy0PkpJVgzswlRD4XSuZdHBsG3G55XUdq3jBPX7pE29x0Yo7Vm3HIDSqs5limI0pBYsRhwSLO4vKGLXCaMy6UhqJK4dhuDuQSqNAfeU5lFZ2MspX8t6JMQrA3nkPOinfRigpWkw-6JwxZIdNZ183isxCjd2BgpIBYXAVlGU2u7fjUjz2ML6iU4jdB8UMtYcWZXXgZ7JD2JHNjQGUP3W7XhGEI5bSM_FKCfJs6v53MN4L0YdteaZhCRlK2IFkUmVXF9iCfA2RSCAN5gU75yTpLiHMeePMjFq-IQSO08WV_-Iwzsm6JNqCMgX9c7zlQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/bxlRQUIF1OoUThFxa2urbJkrec7gYB9bjEkyNGFYb27ToiGvbeH3IlqRDAWzOz5oECFZ4g9C3A878k_OxfocZfiiZheLFgTIx2gnuWklvCEeFR6FtNyJ81H4NG8iftAdwv_CGB-bzMQIlnTyYY6IjuvVPsNsEQr5ARt6AQwQXsmyCDrEk2WTHVAvCu9ET75b1r_HbboEhDZDna32EO-7owbfNz350pOCuucISpcDnqhErf7l6au0yyKLCcm875QDgffIe6rxDJi2HENQqmY6iERP3WGGAdTCRhe9oU4inUycMSIJ38pmWTNeTnw4svQ7VXESJZ3_TBtQVNe9pPBpzQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/cweO_ESVFlRr90RUDOxDxBHOGjEVVt20vvPReIUIZTzz_oNswcelIw8ZY7e2fb18tv26VDcyhICWmdTjX-jfLso7iK-ATXQeXF7fk0HAFV1WtVFdXInkTlRTXTG-p7jyZ-IdxYUOMddxSUATGWFto6BLB66fk1d5Qr5z-ugq7EfWwCFql4JzXd2FYYpJkH6A66kgkVuzBj1xerEua2A5k7HbEAtgkeg5ld4adcKfojWP4mxKNdhUdtqxLtEQJBh82OruVZSs92tISWxeahULi1KqTV8Ri_mAro7c0aeVxnY-q778ACnrjnQBTHNF37vQV4KD0qCC1LLi_Ild2Bc1Ow.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/AO0NIKtO-bwSH3CHJv97kWJOHLrHNMY2jjXAmqrhEexjQ4LutT05rZcOIkY0FEryJMD85ylOW3F3by9bGWj5a-8pRVmlAMy4ZwLKGydHO-wrBO1qn_nIMXbtj5Rh0J_fdTKIK0cug0SjJIayVGHNh6IKWbyzl3it9SAzbi5nK0949Zx9WmNwI9b8sUYhpW5J3LX1TuSJwI2DbFpd2BNb98ifegi4d8FN9SYWl_uC283O8M5gJQvpo_gHjFr10sd07XS6X_XISQFpOvcl-E6FcKmWyItOO9GX2eB3z8AECaUfkyVoSkQPzXvzbILT4FkIL3Tnf1Iq2yiFHwCQCQ3mhQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
🔥
بازیکنای نروژ - فرانسه و زیدیاشون هستن.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.7K · <a href="https://t.me/Futball180TV/96061" target="_blank">📅 17:56 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96058">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/ISGWfnjSo4em0noyRLbtPKELLK4avOoHnzfyyLjj6xeIeTJW5Ir6bD0HpNE28ZaiOZiQNp4XgQGcgzhUbNDQli20ixtyN5DHnmULZBxZiGDOO65HBASKEql4KF5zmsySJZt9pfgLP4k7iKYh8wNYddmPfz7Gs-cH_oqi5Ujc0xqmSDwQB9ODxDgBsuD7TArEdToLJ6UrXQfz0ITpkJWNBq839gb8toEdV3Vf6uvsMptqZBVNSRUSk_8VWRsOLsbFGY-PQxS8CeuP6kLArWPppHzoO3Pp9ZUeARBMoc87256ulFyERu7Cac8BM7R_hTr_bHA06ha_Zs5p5sAQSX_nEA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/Edaopic1hX0dk5d4FA_W-FLyyR43tRlwFoCepAd7qSqQa6-pZ6dVY4vVKPs_vFeEER11ce_Kwj6Wyg0pFzTEFHkvCNpyK5Ki_xwbY3F6Wwao_VfwRgDznYDo2gi1OrmJ_EWSO3uujFIGzdzXpeGoIIMGM8heiBh2aNWdetkOidZjE8K5ZlSxflHjjuUWUahORz-GWFHwL0T6voPXlASPf86pk_QLa3Co-9uKahWm1OEJm648mIZD2mf0Um9QvW9IvxrlrPICphjFfJVGXjQ_akMNZzzJI9C9tikcf-srNJUz1G935cbbvWWg26IOVOusb0vsSxWvgk9nNJTPBJr1QQ.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">👀
هینکاپیه بازیکن تیم ملی اکوادور مخ سابرینا کارپنتر خواننده معروف آمریکایی رو زده و تو بازی اکوادور - آلمان هم بازیو تو ورزشگاه تماشا کرد تا زیدیو تنها نزاره.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22.6K · <a href="https://t.me/Futball180TV/96058" target="_blank">📅 17:35 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96057">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=X7Ah9guq_30-U1JLlZdjxgtDVBaVvBRVMzDbNOAToZ9Z3RA04Sg7e0ovagxQ6CbkGuoS_6X2dnFCOg1BhOey7FdalMo_wqDgogggxMTHy_qG9HGVccik4J7Osn5rgSDp7JDxylxUBX22N2UEptV_zOzX5GGEA1bPeSn9q3cqnQ7Oo4fnhk82k5psvTsVSjiZgTLPumFhOLK7si_Dw4Q1On5_77WkAXig40Y7NXbRkWSnSh5O1Jj4wS0YWRnLOXDnms-Nj99fQ4n76Yya1XQCUoCVTRd-FND-O9OYZwLQqp-IiuaoxyPgRcJZ-uWQa0MVdDsT7KqP1Ncdb7mmpw2-6g" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/4f0cd7304b.mp4?token=X7Ah9guq_30-U1JLlZdjxgtDVBaVvBRVMzDbNOAToZ9Z3RA04Sg7e0ovagxQ6CbkGuoS_6X2dnFCOg1BhOey7FdalMo_wqDgogggxMTHy_qG9HGVccik4J7Osn5rgSDp7JDxylxUBX22N2UEptV_zOzX5GGEA1bPeSn9q3cqnQ7Oo4fnhk82k5psvTsVSjiZgTLPumFhOLK7si_Dw4Q1On5_77WkAXig40Y7NXbRkWSnSh5O1Jj4wS0YWRnLOXDnms-Nj99fQ4n76Yya1XQCUoCVTRd-FND-O9OYZwLQqp-IiuaoxyPgRcJZ-uWQa0MVdDsT7KqP1Ncdb7mmpw2-6g" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🎙
▶️
پیروز قربانی: احمدرضا عابدزاده و ناصر حجازی از لحاظ قبال اجتماعی متفاوت بودند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 22K · <a href="https://t.me/Futball180TV/96057" target="_blank">📅 17:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96056">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/eKSErLsFrsXKOPhem8iRZs08OF43Ef34l-jkRq9AnB2_Ro466sGUWEA2X3xCPu6DvMi6Hx5cWGP1jqv7utTy041W9amOPnqWuuJ6Kx16jf5zo1OOWJfmM0p-4A1yf7kFni1273n6XP83zoEldUZ6ntoVbDCoTz-FTsRrsdsNSG-FAOdIu3yq0cQqthoalYjNkWZQCQaPZDV06gRhYPc0vovZn2WqHMxbIUJ5qqT2WT-Gm9fKCB0_D9bntX_hfYSCQ13An8yCkGjuCuO97VDrRt8oSncEZFs6ZPpV9fXVhjxU1EuWf-hU8fyvACY4i84wso4sjOiRdX59KWf8DKPJQA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">رده بندی‌ خلاق‌ترین‌ بازیکنان جام جهانی 2026
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 21.9K · <a href="https://t.me/Futball180TV/96056" target="_blank">📅 16:54 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96055">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/d7pdcMopqTMMKLxQM7-CD6vEpe4hLEyG7qhdJ6P-35sJC13xfPNf5cSxhT6x5RDG89AUOqeUlguMSgiJxE_6mIpFGgMR23w_PDSgA6beU3fAMYMdCSdpKTCdFR_0uLRKTBxK_MYR0ie3KcyZZv_EU52TL6xm3cKtI66aeRTTa8-U21Lq89TqkFSCWAIU9JIT4b8wyTCPIPj23wOqlK1H1zyQ5ppcb5NPmeC5z6pkqe8_9uhJAnIdVx6idA-dducm0Mz-n6_xnhVw42eSp1GcpyAXAbnj_C5yxepHhOhM35TEk0R39V34w92RlNAGOdoHwiXgRduZ-TdKlko9KmSMzA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
پرجمعیت کشورهایی که هرگز به جام جهانی صعود نکردن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.7K · <a href="https://t.me/Futball180TV/96055" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96054">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/JvmapFwSKB-l3TDD5OsK3muaUUiH1lFXXis0F0Mj6B_e2Z-tejywfPu6MUiWXDdPiaMfjjaIuZsJ892lBUYNjOQNfNV-C6yDCyqcq8dkiboxIp8jqbAm44S9ZbYHAv4H_aRJSW80cH6BbHeICOpfgcL9I0WDUEn4-kywZ2adyALOo8ZMsOq77MUYjD6m_4TlaOETKS4sQyaEwBtjLo1b_5klyUk-raBvk42MW-iwCLIcefUC8kWZzhj8UJFLhKi_9mb9NBx8P1zHJJ_idrT68nEi5t6PxVfKvLfI4IbZWdeHdCN1ZaSH9L4UxGklpDpGGePJshrMZL4RMRbdV6cD-Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🎁
هدیه همراه اول به ایرانیان با صعود تیم ملی
همراه اول در اقدامی ویژه برای حمایت از تیم ملی فوتبال و همراهی هر چه بیشتر با تماشاگران بازی‌های جام‌جهانی، در صورت صعود از دور مقدماتی این رقابت‌ها، یک گیگابایت اینترنت رایگان به تمامی ایرانیان هدیه می‌دهد.
در صورت صعود تیم ملی فوتبال ایران، می‌توانید طی سه‌روز با مراجعه به اپلیکیشن «همراه من»، بسته اینترنت هدیه خود را فعال کنید.
تیم ملی ایران، شنبه ۶ تیرماه ساعت ۶:۳۰ صبح مقابل مصر صف‌آرایی می‌کند. برد در این دیدار، صعود مقتدرانه و صدرنشینی ایران را رقم می‌زند. در صورت تساوی نیز شانس صعود از مسیر تیم‌های سوم برتر، همچنان برای فوتبال‌دوستان ایرانی زنده باقی می‌ماند.
همراه اول ضمن آرزوی پیروزی برای ملی‌پوشان کشورمان، تمامی مشترکان را دعوت به مشارکت در پویش پیش‌بینی «جام‌جهانی ۲۰۲۶ در اپلیکیشن همراه من»، امتیازگیری و بالا بردن شانس برنده شدن مجموعه‌ای از جوایز متنوع کرده است.
http://mci.ir/-VK6ZFX</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96054" target="_blank">📅 16:51 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96053">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=Y8sgUXSZ9E6Hmgs-1MQDeoE6-wB4-Byf9OgbuanX6DSe-rQQ2YE0310u55B31bZnNf_4FrIq72zDy6YbIJ5nHd6_LyTQF7PE3jJExOkYoEHKkgLaCy8imGBH6Jwc5agi0IXitk-WTUZArGCd7lq__scQ-mQUm5npOtMjSiudoOduIgBBfG7P-mZqVwnRZWAM3pPve3xkGHINyDEpAsKnui_yC6t8CaV6swAHdteJlBOl_aSGiKJFsCoGoXW28W8nQvUwUvLJ9cwAVPbMlwuHa04pbCBwAmeG9oVE7iP0sq2C4nhp2VKgH3tz0ey-p592kkSMreLHXnr0ry4A9Xm6Sw" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ffafe3e9dd.mp4?token=Y8sgUXSZ9E6Hmgs-1MQDeoE6-wB4-Byf9OgbuanX6DSe-rQQ2YE0310u55B31bZnNf_4FrIq72zDy6YbIJ5nHd6_LyTQF7PE3jJExOkYoEHKkgLaCy8imGBH6Jwc5agi0IXitk-WTUZArGCd7lq__scQ-mQUm5npOtMjSiudoOduIgBBfG7P-mZqVwnRZWAM3pPve3xkGHINyDEpAsKnui_yC6t8CaV6swAHdteJlBOl_aSGiKJFsCoGoXW28W8nQvUwUvLJ9cwAVPbMlwuHa04pbCBwAmeG9oVE7iP0sq2C4nhp2VKgH3tz0ey-p592kkSMreLHXnr0ry4A9Xm6Sw" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">‼️
🎙
ژوزه مورینیو: دوست دارم بازیکنای رئال مادرید در جام‌جهانی ببازن
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.9K · <a href="https://t.me/Futball180TV/96053" target="_blank">📅 16:40 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96052">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/45704079cd.mp4?token=uzdCrK5Iu2Nsmetj2NK8ZNbpfURlyfhg4IB4STxF-qouQez0U6FowHgxR9901nVVpKN8VgT2-QvdPsobl1BCdtuRm-0O2LTPZCldB2ypcLkoNEkWthcbnUXCoV9D0BLbjsf-l5tH7Fl3zYit38QX9nmr-6_9M8Ys-9A-HUW-MWzN2ECLGBuNtATGiXiBWh-Fkl8yesHKyowJII-2RUCuJXDau9UTkgxVIrMElpf7iPAVqTYnfGCNGe1Dn6wKbGT9hKkSWGikRm_NAurOBHpnTKeIMr2NDtWceL9hpOYQUkwIVcp2-Kxa-SqGeSMAichoGcGpV1S8ekl6ce7rN-sqFQ" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/45704079cd.mp4?token=uzdCrK5Iu2Nsmetj2NK8ZNbpfURlyfhg4IB4STxF-qouQez0U6FowHgxR9901nVVpKN8VgT2-QvdPsobl1BCdtuRm-0O2LTPZCldB2ypcLkoNEkWthcbnUXCoV9D0BLbjsf-l5tH7Fl3zYit38QX9nmr-6_9M8Ys-9A-HUW-MWzN2ECLGBuNtATGiXiBWh-Fkl8yesHKyowJII-2RUCuJXDau9UTkgxVIrMElpf7iPAVqTYnfGCNGe1Dn6wKbGT9hKkSWGikRm_NAurOBHpnTKeIMr2NDtWceL9hpOYQUkwIVcp2-Kxa-SqGeSMAichoGcGpV1S8ekl6ce7rN-sqFQ" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">▶️
🇧🇷
🏴󠁧󠁢󠁳󠁣󠁴󠁿
اسکاتلند - برزیل و دوباره زلزله
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.6K · <a href="https://t.me/Futball180TV/96052" target="_blank">📅 16:20 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96051">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/cQh-31d7vLtyfIWlPqL_Al3N31My_Q7hPEBzX0ktpjHdgdPbQmZulMX9QDYspRSldwwmFGMmEt18G4YH9aDo5oo85I5h8EPtSPtGtjcA5UGXocqZNyxtAjg4kDfDx9vrnBP7fCSzRQvEtqCF9aYzzdvOhzEsY9YtVt1pIOMahExfYkg78cNv1qdHIhkB3XwXLuts3NVz0MJXnAAZwoA0hEhKnTvrZg4oMR_QHmHSOAOWftOnDBv-7cDhyrjXQVCEVXQtgUG2ePjZr_Bb4vruu83bgBni8UzXXSagvcbHyv6ThtOGcImfKlKHV-J1hSt1jDQ-rorFYi_DeT38wOo6yQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">یوتو ناگاتومو 39 ساله به اولین بازیکن آسیایی تاریخ تبدیل شد که تو 5 دوره جام جهانی حضور داشته و بازی کرده
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96051" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96050">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/iqJEsQcy02BMyPCyU3aLeyND46wefu4le-N-vEbuC00Sfj_1wETKgsLmVsSaICPcZwVlCaO6Wy0GhtQKDeX-jtI3iVK9I2dCx6O2exoiq4NTykwJ0vKZy80fArOBrpbbyTVt2pXfX4qkXJj7mASXJqxmWeRrk03xf0vhgU57EiT2hIQQUkXWfqv3sE-7UCGgOajCI61aPkaPoLVB9DqijOquKZ4il5GZFixYv1doyT2M0YWq0hZD4YAPixTD314H2Yl9P7AaRa_eou_co4qR2k-B6b3DF47BF5yYb3uRgdKN6MhXNetm5V8s7-GjjGgeoxcgX91mlOan9vyAvi5DyA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔝
💥
سرویس‌های مولتی‌لوکیشن موجود شد
💥
🔝
🛡
کیفیت - سرعت - قیمت اسثننایی
🦸‍♀️
❤️
🎁
فقط و فقط گیگی 8,000
10G
▶️
80,000
👑
20G
▶️
160,000
👑
50G
▶️
400,000
👑
🔥
بسته ویژه:
⭐️
100G
▶️
600,000
(فقط گیگی 6,000)
🛍
حداقل خرید: 10 گیگ
📍
لوکیشن‌های متنوع و پرسرعت
🔗
همراه با لینک ساب(برای دیدن حجم مصرفی)
👥
بدون محدودیت کاربر
متصل روی تمامی اپراتورها
🛜
🛜
🛜
متصل روی تمامی سیستم‌عامل‌ها
❤️
🤔
👩🏻‍💻
جهت ثبت سفارش و خرید:
✅
@Trust_VPN3
تست رایگان هم موجودِ
❤️</div>
<div class="tg-footer">👁️ 19.3K · <a href="https://t.me/Futball180TV/96050" target="_blank">📅 16:18 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96049">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/YcxgCxqGa0cQO46vg49kbhH0LA4mvXq2qJoO0LJ5Z0-RIqEI_0B5iw1XykdTp9BVVyS6wSQC4ty8HUwyZpBoG9XYEfL5WlUzzc-PRAbRawmWDgaiocDPupyOWsQRjSWRgqvKvRVKeYk3d7Ku39qj8VUWIWbVVCyTDr5rSP34KPU_PnZJAH1SrfQEvvlAvLSZOts1Qdx5lbOg3DnEqOX6n677kveMS268obiJR9n-1AhfAubnrbTUbtXQtpfFDeuLJl9b_ea9_pvjM7XdBgCw8LRVHpk9Nfuw6ttPTLRGNAk2dG4Fz8p_RIThmPyFGk4wHdRcr_vSdyasZlYQF1_3GA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">⚽️
جدول گلزنان جام جهانی 2026 تا پایان روز شانزدهم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.7K · <a href="https://t.me/Futball180TV/96049" target="_blank">📅 16:06 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96048">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/fdXDRQVQlV9K9jvSiFiPpndU5wQsu0L2Gx51hmkZ4BfeVsPt4XVXWPvZY_wPPoeHsWZE5l12oaME8qIfY0Lwy-B4niyvadPdVUiYxXuKCTESJQqd7siioQx8x5YSkSietIUbCfckyvuHi4xHaefmtIq6UESADBPsjqSN0w7m1-5s82b2iXHjbYyzhTgevxl5GQEWV7kp6pnnde0Gk1YWL5hf4maf7PcfPp5R8yBe4UMVgkXk_Lke6V7cz2wlR1W9nTxu7L4HP9FMSnxE30sp0KkQ2tHix7i3mZLHPo2c5mxBLHZ_PD1lliZytvC3d3gDVP_VKttCEsqGoLlvdmxO_A.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">کمیته سازماندهی جام جهانی، هتل تیم ملی مصر رو با پرچم رنگین کمان نورپردازی کرد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 19.4K · <a href="https://t.me/Futball180TV/96048" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96047">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-doc">
<span class="tg-doc-icon">📎</span>
<div class="tg-doc-info">
  <div class="tg-doc-title">1xbet_ir.apk</div>
  <div class="tg-doc-extra">53.8 MB</div>
</div>
<a href="https://t.me/Futball180TV/96047" class="tg-doc-link" target="_blank">دانلود</a>
</div>
<div class="tg-text">🔥
ورژن جدید اپلیکیشن وان ایکس بت بدون نیاز به فیلترشکن برای گوشی های آندروید
🎁
اپلیکیشن رو دانلود کردید موقع ثبت‌نام، کد هدیه 1x_1566529 رو وارد کن و تا
100یورو
هدیه بگیر!</div>
<div class="tg-footer">👁️ 18.6K · <a href="https://t.me/Futball180TV/96047" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96046">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=i1VW464Qx2mz9MJzH-lDKJkG2APM0ft6oW2sY95IWyRTcHryhGIKtS0L0drIvC9BYYKfOhnYA9_L8nZYRNBal0CCp_sn0IQqbXMnw4Pi0SZ2nD2zyL3ri0OpH7o7fcK5iTzqipb4sTN6dSVjdZZsQz-Vf3x8PNpZ05AaYlj8y99p23XNb8kCHw9vYW3tgfaEB6lZxLUs8cPy4RtQZyE5SIBdQTQHkjiHl8h3GJ69EWVPPuWYs48Lka2I4K3sQeT3Q9ZKx0Hj7pIBuHF7_ENbVX-tn_l9upWJ3mAbICLgt6nWkTS7PUgG-y8sXUfYG3b6Plj640pq418ydu7JxFZAylEof1qgQkYJFkVa5Eq5frk3ujbvXO7_SdUkxoFuyS6R4lWnKlZTxpjrwh3WKDZ5I6Hm2jwG0cvUamfWI7LTy9ZxHDlMQjAAz68K8WTRcrCRoHd0_clCENolVGTgZHys5v3-2nD7_YmRjTAeHBScQFVZ5HYTUkRVkSdYbG_S7py5N0wfb2mXKSrsLpx_eASixfmSpQ-tmqWL8q-puaF99hFyvo1QWHB2IO6ZisTDiAUlaYtX6P_boKQ8WArfN4yVG3W0IFUGjQqDFXNGjtJxprhhZtSYnAgRnWlyiN_pt1nddfynFIOUxcwXjY0IGPY3xyMZlFC1Q38Zbyenfyz717Y" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/17bdf5f245.mp4?token=i1VW464Qx2mz9MJzH-lDKJkG2APM0ft6oW2sY95IWyRTcHryhGIKtS0L0drIvC9BYYKfOhnYA9_L8nZYRNBal0CCp_sn0IQqbXMnw4Pi0SZ2nD2zyL3ri0OpH7o7fcK5iTzqipb4sTN6dSVjdZZsQz-Vf3x8PNpZ05AaYlj8y99p23XNb8kCHw9vYW3tgfaEB6lZxLUs8cPy4RtQZyE5SIBdQTQHkjiHl8h3GJ69EWVPPuWYs48Lka2I4K3sQeT3Q9ZKx0Hj7pIBuHF7_ENbVX-tn_l9upWJ3mAbICLgt6nWkTS7PUgG-y8sXUfYG3b6Plj640pq418ydu7JxFZAylEof1qgQkYJFkVa5Eq5frk3ujbvXO7_SdUkxoFuyS6R4lWnKlZTxpjrwh3WKDZ5I6Hm2jwG0cvUamfWI7LTy9ZxHDlMQjAAz68K8WTRcrCRoHd0_clCENolVGTgZHys5v3-2nD7_YmRjTAeHBScQFVZ5HYTUkRVkSdYbG_S7py5N0wfb2mXKSrsLpx_eASixfmSpQ-tmqWL8q-puaF99hFyvo1QWHB2IO6ZisTDiAUlaYtX6P_boKQ8WArfN4yVG3W0IFUGjQqDFXNGjtJxprhhZtSYnAgRnWlyiN_pt1nddfynFIOUxcwXjY0IGPY3xyMZlFC1Q38Zbyenfyz717Y" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
جام جهانی ۲۰۲۶ فقط یک تورنمنت نیست؛
جاییه که رویاها ساخته می‌شن، ستاره‌ها متولد می‌شن و تاریخ دوباره نوشته می‌شه…
🌍
⚽️
از نبرد غول‌های فوتبال تا شگفتی تیم‌های کوچک،
دنیا دوباره برای بزرگ‌ترین جشن فوتبال آماده می‌شه
🔥
┅━━━━━━━━━━━━┅
🟦
آدرس وان‌ایکس‌بت:
🌐
bitly.uk/connect1xbet
🌐
bitly.uk/connect1xbet
🔓
برای ورود به سایت از فیلترشکن کشور های اسیایی یا کانادا یا ترکیه استفاده کنید
⬇️
فایل نصب اندروید 1XBET
⬇️</div>
<div class="tg-footer">👁️ 20.8K · <a href="https://t.me/Futball180TV/96046" target="_blank">📅 16:05 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96045">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=I7j5uPjYrK_ayGS_Tn9fMUOe_d351Lr18lOQEwKpGGRdc9VxfgO2PTv166RRbUhL6mdLxqU2IV-MXSMKCmjSciaGczjt6JhizaemUvyB5ftnpe3UoQpld--MXU94zxvnpPHNc0c1p42SK180zVHnp828SbuaW4ZpGb4zrrN7kkojMRSAJZupKUtnAIZrO7DOmrYvNcigfataeXWf1wr3YpjA2P7QxUJSeSkKcRK9Y3Uw5PrA4Y-kzQP2itwBEgy3Xaa4zwRcRXl0oZ-kPoeUIog79B4BRXm18qshglHvDPAWuuaJFUx2CFj9Bmp-vfi_AUIRHO6PockPruoPkNHKczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/d15632d71c.mp4?token=I7j5uPjYrK_ayGS_Tn9fMUOe_d351Lr18lOQEwKpGGRdc9VxfgO2PTv166RRbUhL6mdLxqU2IV-MXSMKCmjSciaGczjt6JhizaemUvyB5ftnpe3UoQpld--MXU94zxvnpPHNc0c1p42SK180zVHnp828SbuaW4ZpGb4zrrN7kkojMRSAJZupKUtnAIZrO7DOmrYvNcigfataeXWf1wr3YpjA2P7QxUJSeSkKcRK9Y3Uw5PrA4Y-kzQP2itwBEgy3Xaa4zwRcRXl0oZ-kPoeUIog79B4BRXm18qshglHvDPAWuuaJFUx2CFj9Bmp-vfi_AUIRHO6PockPruoPkNHKczzoLYYGMqknLXWitR9ENcuYlvuH2_duRcW1gSNrDutwJRiNb4oohoOr2QiJZhWoYyGpijaw_6z9cGAq5qraeb67jIHbQJRGf3qFSIx1nXYKlYBH2IGEFbmyeDQT784STQ5YPI-eEt4U2NpNTzs5qqOhyJVQlX8AwFaoOXyE8JMF1U5N6F2kgYRk9lSL-fG7i4rS94h3rQJ8XKuOf9GXGF6tJT-wZRWgCS1AQJnzDxJQ0sz9GR52DM9Ho7mOsVJxsH0JrprSkZ-jLGCuNWz4izHcr0djjMAgjRxHVogYUkwXcmv5R27x7EdgEMGthHOr_gJwSqXM3BRMKCcD7HrBjy0" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🔥
ارتش هلندی‌ها در جام‌جهانی؛ حقیقتا پشماممم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.2K · <a href="https://t.me/Futball180TV/96045" target="_blank">📅 16:02 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96044">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/QZ9k9ZOFozTF4wzTWeJEk-htrH-kzfy_9Y_80NieYQ8rOsvaC3iu3wf9LzoqZORTs8bytE5_s53zB0MPMQKdxFIgp213KpHIj7rdwXKB_m86bsfDjy0yVUSHNe5SQvsObnGO0YScBfrxRvCPzWhkn3QXIdFPvMrRN26KuWeNy9o6aPUVSneDjcff6PuiCq-63bKZ054V5s9LMkOY4oC8mCpsg2mc2lsTUp9ETxS1clQFE6PiwnOLAXiwTQtc_GRLuyd0ZgcJojTNjyM6jrvZlXTzrZ0mz_JQ7kBU9DzhKByuGm69kH1wsj2zUCwL1eQcn9U8qzCXhm6HIYXxr0Tmog.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
فابریزیو رومانو:
کومو با رئال بر سر خرید دائمی نیکو پاز به توافق رسید
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.4K · <a href="https://t.me/Futball180TV/96044" target="_blank">📅 15:42 · 05 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-96043">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/MENiwNlibMHMjb5u461EpS78Dx-U3SqgKgfRpzn9KukUaFKQIul73b-kkIIBj1FBbB6aCkUCPlZhDlzxOHA4bjDnOn4nu5zq0VAQExV0OG7wHRsBI_0xRdXgZBatrItBTL9dZuwbrTmoDpCZzBkYkMozkvIQ-PwpcsKXBDhZfF7fQAtSy-hvmRMyVdFuQk6Nh0cd0I9ro_KRli5YL8ef488ohJbA9b7AcU_1Ed1zljknYjdrdwfLa172h2XAQHABFYKszk2dRJuFqQmMoFNXNCFYUDE-wXENw37hC1FwPUvRtK32QywWau9qa8ICfHJqnCYTPABXU3hMxJOmOPDfzg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🏆
بازیکنان کدام‌تیم ها در جام‌جهانی گل‌بیشتری زدن؟
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 20.5K · <a href="https://t.me/Futball180TV/96043" target="_blank">📅 15:40 · 05 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
