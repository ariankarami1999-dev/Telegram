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
<img src="https://cdn5.telesco.pe/file/S6hPPIUn8MKcCYJO4BYRBwmt2v8WL5tK-MeO3XvnJx6VXGmIvKs73K6whbguU45t3uC89LWRsADwWvhGCLvr-7UXzcgLgAY26Cv3fZl8rO4s8Y2RSHR-pviQ0uHwKQ24M16uI8EBod3zuKEw23BJvuCbYsvLEC8Oz95XDSFfFhTrLDRed85sCpNOeGHRDSuw8mgFPPwe-VHSaEdQwspRcHstzsXps6fnDbgFvoHJGpoJPLbDTsHmp3ypAalHeLnji-Eia74lpPvizKkh1LKuqSh1PTI1U9YmV85Gsv_IoUZghVoSvgHnPbBt8mRAhkZY4VC7I_5CKtrSfj9PKr1hjw.jpg" class="tg-avatar" alt="avatar"/>
<h1>📡 جام جهانی 2026 | فوتبال 180</h1>
<p>@Futball180TV • 👥 555K عضو</p>
<a href="https://t.me/Futball180TV" class="tg-telegram-btn" target="_blank">✈️ باز کردن در تلگرام</a>
</div>
<div class="tg-channel-desc">📝 In the name of God; The only popular sports channel on Telegram: All for Iran...🖤We respect the copyright laws and follow the laws, Mr.@Durov...🙏🌹Contact ads:@TivaAds</div>
<div class="tg-last-update">🕐 آخرین بروزرسانی: 1405-04-29 00:42:14</div>
<hr>

<div class="tg-post" id="msg-101135">
<div class="tg-post-header">📌 پیام #100</div>
<div class="tg-text">خطای خوووش جا واسه اسپانیاااا</div>
<div class="tg-footer">👁️ 1 · <a href="https://t.me/Futball180TV/101135" target="_blank">📅 00:43 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101134">
<div class="tg-post-header">📌 پیام #99</div>
<div class="tg-text">مسی: کوکوریا جلو دهنشو گرررفته</div>
<div class="tg-footer">👁️ 17 · <a href="https://t.me/Futball180TV/101134" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101133">
<div class="tg-post-header">📌 پیام #98</div>
<div class="tg-text">انزو رفت بیرون</div>
<div class="tg-footer">👁️ 1.03K · <a href="https://t.me/Futball180TV/101133" target="_blank">📅 00:42 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101132">
<div class="tg-post-header">📌 پیام #97</div>
<div class="tg-text">آرژانتین ده نفررررررره شدددددد</div>
<div class="tg-footer">👁️ 1.04K · <a href="https://t.me/Futball180TV/101132" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101131">
<div class="tg-post-header">📌 پیام #96</div>
<div class="tg-text">انزوووو اخراج شد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101131" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101130">
<div class="tg-post-header">📌 پیام #95</div>
<div class="tg-text">اخرااااج</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101130" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101129">
<div class="tg-post-header">📌 پیام #94</div>
<div class="tg-text">مارتینز گرررررفت</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101129" target="_blank">📅 00:40 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101128">
<div class="tg-post-header">📌 پیام #93</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/jXuJFhxb95JuYyB_IKg5hTTvwcjbPYqKBLZowtO2a0lF7meCbR8n_iQkRafVtVuw5334HXzJUeb6ujJF_VLmFGyT4Hbe50fNoM1Y0h_XkxrqvK-a72DjG7qyhjCI1dm_XKB04fN7tJSXIqm7MaOkpc2woN4HPZt99q_dvyWgJECqblVOiXF6lQbjb4TivP6lnGTSYv7-_2VXxz6k9b1df8JWQOA_KfZkWbICYDVuysWmh5iVp5ZkvDomD731xFOfqv3sD_aihedIiZA1Pf3ObuLoeCV9aJZGO8FBSRudGe4gLbxdcxQxXxgqgPFoNltLwmJTkpH2VDYQzJOLUKSupg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">قابو ببین
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/101128" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101127">
<div class="tg-post-header">📌 پیام #92</div>
<div class="tg-text">پا شد</div>
<div class="tg-footer">👁️ 2.04K · <a href="https://t.me/Futball180TV/101127" target="_blank">📅 00:39 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101126">
<div class="tg-post-header">📌 پیام #91</div>
<div class="tg-text">مسی افتادههه رو زمین</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/101126" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101125">
<div class="tg-post-header">📌 پیام #90</div>
<div class="tg-text">اوههههه</div>
<div class="tg-footer">👁️ 2.05K · <a href="https://t.me/Futball180TV/101125" target="_blank">📅 00:38 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101124">
<div class="tg-post-header">📌 پیام #89</div>
<div class="tg-text">۴ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/101124" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101123">
<div class="tg-post-header">📌 پیام #88</div>
<div class="tg-text">به به چه قابی دارن نشون میدن</div>
<div class="tg-footer">👁️ 3.05K · <a href="https://t.me/Futball180TV/101123" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101122">
<div class="tg-post-header">📌 پیام #87</div>
<div class="tg-text">آرژانتین واقعا هیچی نبوده</div>
<div class="tg-footer">👁️ 3.06K · <a href="https://t.me/Futball180TV/101122" target="_blank">📅 00:37 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101121">
<div class="tg-post-header">📌 پیام #86</div>
<div class="tg-text">کرنرررر</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/101121" target="_blank">📅 00:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101120">
<div class="tg-post-header">📌 پیام #85</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 4.07K · <a href="https://t.me/Futball180TV/101120" target="_blank">📅 00:34 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101119">
<div class="tg-post-header">📌 پیام #84</div>
<div class="tg-text">زرد واسه انزو</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/101119" target="_blank">📅 00:29 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101118">
<div class="tg-post-header">📌 پیام #83</div>
<div class="tg-text">چییییییی گرفت مارتینزززز</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101118" target="_blank">📅 00:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101117">
<div class="tg-post-header">📌 پیام #82</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 4.1K · <a href="https://t.me/Futball180TV/101117" target="_blank">📅 00:28 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101116">
<div class="tg-post-header">📌 پیام #81</div>
<div class="tg-text">عجب شاهکاریه امی مارتینز</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101116" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101115">
<div class="tg-post-header">📌 پیام #80</div>
<div class="tg-text">واااااای پشمام</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101115" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101114">
<div class="tg-post-header">📌 پیام #79</div>
<div class="tg-text">بازمممممم گرفتتتت</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101114" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101113">
<div class="tg-post-header">📌 پیام #78</div>
<div class="tg-text">پدری هم زد وسط دستای امی مارتینز</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/101113" target="_blank">📅 00:24 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101112">
<div class="tg-post-header">📌 پیام #77</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 5.11K · <a href="https://t.me/Futball180TV/101112" target="_blank">📅 00:23 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101111">
<div class="tg-post-header">📌 پیام #76</div>
<div class="tg-text">نیکو ویلیامز و مرینو اومدن
بائنا و اولمو رفتن</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/101111" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101110">
<div class="tg-post-header">📌 پیام #75</div>
<div class="tg-text">مرینو اومد تا کارو تموم کنه</div>
<div class="tg-footer">👁️ 5.12K · <a href="https://t.me/Futball180TV/101110" target="_blank">📅 00:22 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101109">
<div class="tg-post-header">📌 پیام #74</div>
<div class="tg-text">سیمئونه رید تو حمله آرژانتین</div>
<div class="tg-footer">👁️ 6.12K · <a href="https://t.me/Futball180TV/101109" target="_blank">📅 00:20 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101108">
<div class="tg-post-header">📌 پیام #73</div>
<div class="tg-text">آرژانتین هیچی نداشته و صفر شوت و ایکس جی صفر فاجعه</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/101108" target="_blank">📅 00:15 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101107">
<div class="tg-post-header">📌 پیام #72</div>
<div class="tg-text">بازمممممم گرفت مارتینز</div>
<div class="tg-footer">👁️ 7.18K · <a href="https://t.me/Futball180TV/101107" target="_blank">📅 00:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101106">
<div class="tg-post-header">📌 پیام #71</div>
<div class="tg-text">واااااای</div>
<div class="tg-footer">👁️ 7.17K · <a href="https://t.me/Futball180TV/101106" target="_blank">📅 00:14 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101105">
<div class="tg-post-header">📌 پیام #70</div>
<div class="tg-text">واقعا سگیییی دفاع میکنن آرژانتینیا</div>
<div class="tg-footer">👁️ 8.18K · <a href="https://t.me/Futball180TV/101105" target="_blank">📅 00:12 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101104">
<div class="tg-post-header">📌 پیام #69</div>
<div class="tg-text">اسپانیا سنگیییین فشار میاره</div>
<div class="tg-footer">👁️ 9.18K · <a href="https://t.me/Futball180TV/101104" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101103">
<div class="tg-post-header">📌 پیام #68</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/101103" target="_blank">📅 00:11 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101102">
<div class="tg-post-header">📌 پیام #67</div>
<div class="tg-text">اویارزابال و رویز بیرون رفتن تورس و و پدری اومدن</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/101102" target="_blank">📅 00:09 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101101">
<div class="tg-post-header">📌 پیام #66</div>
<div class="tg-text">خطای خووووش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 8.17K · <a href="https://t.me/Futball180TV/101101" target="_blank">📅 00:08 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101100">
<div class="tg-post-header">📌 پیام #65</div>
<div class="tg-text">خطای خووووش جا برای اسپانیا</div>
<div class="tg-footer">👁️ 8.16K · <a href="https://t.me/Futball180TV/101100" target="_blank">📅 00:06 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101099">
<div class="tg-post-header">📌 پیام #64</div>
<div class="tg-text">چه دفاعیییی میکنه آرژانتین</div>
<div class="tg-footer">👁️ 9.15K · <a href="https://t.me/Futball180TV/101099" target="_blank">📅 00:03 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101098">
<div class="tg-post-header">📌 پیام #63</div>
<div class="tg-text">چه موقعیتی داشت اسپانیا</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/101098" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101097">
<div class="tg-post-header">📌 پیام #62</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 9.17K · <a href="https://t.me/Futball180TV/101097" target="_blank">📅 00:02 · 29 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101096">
<div class="tg-post-header">📌 پیام #61</div>
<div class="tg-text">پارادس زرد گرفت</div>
<div class="tg-footer">👁️ 9.16K · <a href="https://t.me/Futball180TV/101096" target="_blank">📅 23:59 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101095">
<div class="tg-post-header">📌 پیام #60</div>
<div class="tg-text">شرووووع نیمه دوم</div>
<div class="tg-footer">👁️ 10.2K · <a href="https://t.me/Futball180TV/101095" target="_blank">📅 23:52 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101094">
<div class="tg-post-header">📌 پیام #59</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/d17Zws1tqIE62QO3kG78diqaSoReMwAC5rUR_ZHGtzA2612mK6Oi2jUFnBqf76dKLWa-THbcmZ1Rsq3tgmbkviFYVP9a31Arr-DXFYUNbz_1tr7dv4e1wWhdqRDMUBOYjVkWj5YpHiR3VrAOWMhW2AhY_dEu4wNXX2rjCQmtIaveOGHWYUkVGOxoUCO5hij6qHVqthRSAJQFMdMEE0TWECvtNCwzAaIW28YkjsaRmCXvYWadJyEaNJcCnhrgbrqN-hkofweTGf2WkyppZbc_2J3D0-oGeuBVE3Q4UyRrWxu3gePB45jMtpwwJ6g3Ia09kK8FLLOSIruBV6Of1_sdhg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">‼️
👀
آمریکا برای این مبل و کلاه‌های آفتابی که در استادیوم قرار داده شده رقم ناقابل یک میلیون دلار از تماشاگرانی که میخواستن استفاده کنن گرفته
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101094" target="_blank">📅 23:50 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101093">
<div class="tg-post-header">📌 پیام #58</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/qnoorC5yG1XZbu5mONBPir2lSioFnembCl1guFG30Ng2Uy6oXYenOVvG8aAE_SplUM6gEne-fqanNuMKmZFSHlzMFL73cGwodbFtfJ4Udk3Q7BQ8pOAvTfFbfoKYfNKbf_9QDJw2zYF9MgYZ3uUvDW9_hKWsdHlPHQMdUtwvKrOxJ59roNsSYuoS70-M1nZ46EK8u_proFYpUF0FOqDqKnJa-zG-DxEbxhMGUlUKPqaYs2GWvq6lmZeljDS6InqAo3L8-HXE-6eAhELxnMX9mQ9gqKGO4tURtaky1VXJBoBL2-c53Tx1MjLCnad0a2Q3sY0RA8BEMEQi7920_uReNw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">حداقل میتونم بگیم فینال و اختتامیه فوق العاده ای داشتن.
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101093" target="_blank">📅 23:49 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101092">
<div class="tg-post-header">📌 پیام #57</div>
<div class="tg-text">برررررریم سراغ نیمه‌دوم بازی فینال</div>
<div class="tg-footer">👁️ 11.2K · <a href="https://t.me/Futball180TV/101092" target="_blank">📅 23:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101091">
<div class="tg-post-header">📌 پیام #56</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/k5bPHkN1iKHcJbG76pvvAk6GzvHeVpaZ7SsM6F8iz_bHeyOhFmWTi_qoGUa37XfPO0FVL2n-kM9NsQ3yB9atrMXvOtLWtorGz69HwRoef90P1-pQ6sqrgiTEvSx_y3MCeHMnBv9XKFxrhOZKCTGyZKJx05ZtSc6tRlPa7WglnKh_fqlQg-djAFQ9pc4RFxDVWGhW_bFFIjJl03HdFfwumofKA_b1Kibi93MdZZp6AYo8XVuX9zSWaOsvIeaqBPSHGmoRNImC3OZuXdWu7zWSUsryV5GYYBu6eV9AACB0ggJoTLmFz3MSshfhLcvTMeGjy9SZK49dsiEpUknq4X2bIg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
😐
🇺🇸
بلاد کفر واقعا واسه فینال ترکووووند
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101091" target="_blank">📅 23:45 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101090">
<div class="tg-post-header">📌 پیام #55</div>
<div class="tg-text">شکیرا برامون بوس میفرسته
😂
😂
😍
😍
😍</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101090" target="_blank">📅 23:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101089">
<div class="tg-post-header">📌 پیام #54</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/De9WRVcC4pVS-V6r5A8az4UnWu3xn8WmKbWMbXv-XpxuLOTATV1DAQ3bvNF9PizVPfKCGIHHpC26NuF8oYydhhQe92JyjDFy7vqLNH5c4KYt0XG4im1xJOhypyuqAcRwc5-qdGW1UmsmdEU253B8V1M_wkxC0DbZEptH3gd_z_hSMwTNA3DXFhaAkgjCEIk5HgXPQIaXg5DFrMHY-v_Cu7H4uEkwscYbrcyEkScSCosUFM9u06rvorsTCF-fenKWnagXAhDHR2BfsGA0qsppyswhIyTAkULn12mccZwWfdR6eltv6CrGxwvedsYyqQ3gDa4A1MNR2wkWipooPX_jJA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">از دلایل جذابیت فینال
🔥
🔥
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101089" target="_blank">📅 23:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101088">
<div class="tg-post-header">📌 پیام #53</div>
<div class="tg-text">شکیرا ترکوند
😍
😍
😍
😍
🔥</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101088" target="_blank">📅 23:42 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101087">
<div class="tg-post-header">📌 پیام #52</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CU6xI-HqSTo8LAdygXmTME2vYZjsUdVdLSnD9d7bVToHjWpbA6OrvByrkBC_AJUsb1T5xa5_x8vK2k_34AhdpJp4rXPK3gsQAQ5dkPcceDL7kdhRuZQSdN-VGHWN0omgECR7DInm8QFAptdOIkwVCLQTzfxoigwk9w9qrW_nFRcZtfkKTgtmkr7BcxMDukUwLPErOhplmJPGT3uNaXBXSudIsb1u7zYBEBDVegb_mivYSVkZRzBEqf7RoReEWwqIGmMny6V__n7CPMojb3DqXmTDRRA0jzfbWavDyYzAXNBAUcbevEVI65Of0VSNAc5jlMJozIkwlWHWCA_5w0emCA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🔥
🔥
🔥
🔥
🔥
🔥
🔥
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101087" target="_blank">📅 23:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101086">
<div class="tg-post-header">📌 پیام #51</div>
<div class="tg-text">حاجی شکیرا ناموسا خیلی خفنه
😐
🔥</div>
<div class="tg-footer">👁️ 15.3K · <a href="https://t.me/Futball180TV/101086" target="_blank">📅 23:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101085">
<div class="tg-post-header">📌 پیام #50</div>
<div class="tg-text">اووووف شکیرا جون رو</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101085" target="_blank">📅 23:40 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101084">
<div class="tg-post-header">📌 پیام #49</div>
<div class="tg-text">🚨
🚨
🚨
🚨
🏆
لینک پخش زنده مراسم
(با فیلترشکن وارد بشید)
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101084" target="_blank">📅 23:39 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101083">
<div class="tg-post-header">📌 پیام #48</div>
<div class="tg-text">جاستین بیبرو</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101083" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101082">
<div class="tg-post-header">📌 پیام #47</div>
<div class="tg-text">جاستین بیبر رو فقط
😂
😂
🤣</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101082" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101081">
<div class="tg-post-header">📌 پیام #46</div>
<div class="tg-text">تدلاسووووو چی‌میگه اون وسط
😂
😂
😍</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101081" target="_blank">📅 23:38 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101080">
<div class="tg-post-header">📌 پیام #45</div>
<div class="tg-text">عجیبترین چیزی که دیدم بیژن درحال پارو زدن نروژی با ویولن سفید در کنار BTS بود</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101080" target="_blank">📅 23:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101079">
<div class="tg-post-header">📌 پیام #44</div>
<div class="tg-text">تدلاسو اومدددد</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101079" target="_blank">📅 23:37 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101078">
<div class="tg-post-header">📌 پیام #43</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/I4XOeSfxf-WATigwxceqsQ0MXth2pcYYXUd3XuvHJnT9hsR9tu4cKgiUQcPJRSxbZr9vur2N1cpETh-qFv29YSHZraB69ZXVEn_MoEZmri-wxPVHs-jOytueEWTrATohAj8lLMwcjzT1Di-_OSDmrpaCIlWJ8x09y3xg8rGB3-ZEB7AQXYumTlCe6nJsSD6MzcAciqgsC_9_Jb6GmYQWHd0w2zAW5b6-1ieOG5zz6bmFs9BWL3sVfoo5oMk18Y8RZ8hA0wzUAsTzZ6hCmButzhYWOlN8MSPppnQoEGWYZsQNBoRYqGvTHMde1ONUq_1xCcaAwc311ZOJj5TTSngAcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">اساطیر برزیل رو فقط
😂
😂
😂
😍</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101078" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101077">
<div class="tg-post-header">📌 پیام #42</div>
<div class="tg-text">پشماممممم خیلی باحاله مراسم
😂
😂
🤣
🤣</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101077" target="_blank">📅 23:36 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101076">
<div class="tg-post-header">📌 پیام #41</div>
<div class="tg-text">پشمامممممم بیژن‌مرتضوی داره مینوازع
😂
😂
😂
😂
😂</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101076" target="_blank">📅 23:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101075">
<div class="tg-post-header">📌 پیام #40</div>
<div class="tg-text">بیژن مرتضوی هم اومد
😂
😂
😂
🔥</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101075" target="_blank">📅 23:35 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101074">
<div class="tg-post-header">📌 پیام #39</div>
<div class="tg-text">مراسم اختتامیه رو ببینید عالیه
😂
😂
😂
😍</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101074" target="_blank">📅 23:34 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101073">
<div class="tg-post-header">📌 پیام #38</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/CYN9GrVuYYgrB64o6uSr8wAgyw7Qxua9HMeLee3hKQLkku9PECLCj1bebw_eYRqAOhViDQXASYTW-F9UIs5dCAbby8sD5DubbkkuDgXgsBfb8VlU-SkdW6-r0usAHfbu2-yE9Sz3nKjgV1Cg7rgrUjDUl0vykYDnCxNaMGqa0Mzv-XjOr1zNU1z9KpwkMAERxoRWKpX2z7TRRRwmjYQdW8uTxxnTbM5rNFtVU8pV-YVCciI85QyEpwcuEDm2OW92pxh98dFfAOmAEpMovf3Sq22WEhK4JEcnjf8NoD2yesX80hq6n4HPbAEn86LlCTYKvU8gz-grPcyN8MqIDKwYKQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">✔️
📊
رودری کاپیتان تیم‌ملی اسپانیا با کسب نمره 7.3 بهترین بازیکن نیمه‌اول شد
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101073" target="_blank">📅 23:32 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101072">
<div class="tg-post-header">📌 پیام #37</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/kJ6muQA9iXof6rAfclry2h-F6LFSAfOFvse4Ptam8GhpDx8YncWNvbvmCYao-FLdslrs1TyrF_hqFdRk9KHZGEUwv5YHkNNojUiIOCXyeXQx9oXar9JHy8t5IaJfzuVbAY6F51Su9DwminoDCBC2EVZGGqJCNWBgtwQfi7UXgBpoWMrauYLdUL4lhlO9RSlsI5eoLqrgHHqVZNKtCF6ywapWi02K7WTCVkgtxoDD77K9bYAmEz42vDwPuK7r8ERq4-Cm8DPLfIUEtNx8c65Z-k1DdPiR_-VBz388tDfrQzEptAtn98wyarKC__gCQZaKlLGqgvpl-2-hGO8m9bM95g.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">👀
🙂
لایی خوشکل لیونل‌مسی به لامین‌یامال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101072" target="_blank">📅 23:30 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101071">
<div class="tg-post-header">📌 پیام #36</div>
<div class="tg-text">🚨
🚨
‼️
اسپانیا مقابل تیم های مرحله حذفی
:
🇵🇹
پرتغال: مصدومیت نونو مندز
🇧🇪
بلژیک: مصدومیت کورتوا
🇫🇷
فرانسه: مصدومیت سالیبا
🇦🇷
آرژانتین: مصدومیت لیساندرو
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101071" target="_blank">📅 23:28 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101070">
<div class="tg-post-header">📌 پیام #35</div>
<div class="tg-text">اجرای بیژن مرتضوی احتمالا جذابیت بیشتری داشته باشه تا نیمه‌اول</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101070" target="_blank">📅 23:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101068">
<div class="tg-post-header">📌 پیام #34</div>
<div class="tg-text">🚨
پایان نیمه‌اول با تساوی بدون گل
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101068" target="_blank">📅 23:25 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101067">
<div class="tg-post-header">📌 پیام #33</div>
<div class="tg-text">۴ دقیقه وقت اضافه</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101067" target="_blank">📅 23:21 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101066">
<div class="tg-post-header">📌 پیام #32</div>
<div class="tg-text">لیساندرو مارتینز مصدوم شدددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101066" target="_blank">📅 23:20 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101065">
<div class="tg-post-header">📌 پیام #31</div>
<div class="tg-text">لیساندرو مارتینز مصدوم شدددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101065" target="_blank">📅 23:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101064">
<div class="tg-post-header">📌 پیام #30</div>
<div class="tg-text">کوکوریا داشت میزدددددد</div>
<div class="tg-footer">👁️ 17.3K · <a href="https://t.me/Futball180TV/101064" target="_blank">📅 23:19 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101063">
<div class="tg-post-header">📌 پیام #29</div>
<div class="tg-text">وااااااای</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101063" target="_blank">📅 23:18 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101062">
<div class="tg-post-header">📌 پیام #28</div>
<div class="tg-text">کارت زرد برای لیساندرو مارتینز</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101062" target="_blank">📅 23:16 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101061">
<div class="tg-post-header">📌 پیام #27</div>
<div class="tg-text">شوووت اسپانیا مارتینز میگیره</div>
<div class="tg-footer">👁️ 16.3K · <a href="https://t.me/Futball180TV/101061" target="_blank">📅 23:14 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101057">
<div class="tg-post-header">📌 پیام #26</div>
<div class="tg-album">
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/NoB2bKXxkPj1nDRpkCTduLX4aHykvKf4kKEYNQ--1jMl8Autqq_Vr7xiT6cqqmzSNQIlxJwxQYQaBx57fZ0mf3dcpE4fMfWCR7PbZVg3-RxrQikCw2gZzGtORgOzt2ucHkoIco_XN67B23HKx8WhnGdnV9aT34ILddO2IkTkP8dglYIoE01mTwAVuEE8uV9zMUiaGyFY_xG_ANK6QlHHqhMbJVItlmig7Ure-c-hWDX8vQrjw0qkseFpQql-sP2pKRn8umlRSFW56OfKEKqXIkJJLrlbLyHF3Qd-WIQ1_VXUxTh5Pum9nLWzoCHV7XcKjnz7vV5iXVfzKV74E0RCrg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/q7mzl-dKsathb4noYNILNySJCHMyhNEG-EJRUU71z0IprX6_wTU4TVY8CF40YDl4xyRnALfflZ2BqK8O4EG1HOBsxxYnR7VVJETpYDdhsyl42gw4MJeLXpaa3VFGAuPm1_OZqqx7ycn5VO4X3YY5KXSxcWUh1UYJlhEglWYIB8xhzENKlMJoylvjtCheHJ78FqDk2-xOTh5TmKw7itVvOIYrHTJew1GtUJgISgH4lBrFGY4jZ7axyzOf70_m-11PQPup5NeMk8uUJsCnA0MlFd-E36GgMJMwK1MIn1_WehJkJpdV23wwgHFQiPUxlOSCnHhYU5PRN-Ex-KBcPa2VcQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/rseO8J-25jKRabxCJ01qr6gMr8TGbXxQYhBhJQRCyVCPCa45abR7WfsdIlj6Ene5DmU01WmZr77PDZO2v-AmELW5ohAE9Vi44QkPLq1mgv4etPfyaMpr5CKvM-3RoT4IBTLzvLkkVYvn_rtsZo8S1sMLQYuOFGtcCLvMz2vGEfX6OqzKxmSAQdUPghXxu_korbX8JjBkfXXZr9iz3ZnrToq5VgGOUeO3snRsEE2lLYBoituGZZv9NqMeyYOgj-2lqPrWD3AwVr5zdW_Ek0-HQZFqnYAgotaiB0adaMVLrajxVKL2LXflxq0HabKtgKM9kMcAX7FXNlQSWgfE2zyf8Q.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-album-item"><img src="https://cdn4.telesco.pe/file/RZxp83miECakUxMGfCA_UuU1bi5JH52NL0GEcJdWXnd9fhYUE_YNZpiprGvRM9QpSLTgN-uQZSL2uWw5Y_tZcZyn_x08bTEJwWppSnTFDu8I_jjYMGNgbYs1sR7w7lHrFmFGw3ipDWKCT4_uQg48awAwsLnwYMLJwdKXTC70h1CN_eHLDWhwBl9UYjsxnMCNtd52GK77Om00H8NGsmtXEK-PhQPPL02ERYHC0QsBmT9S1MCkNWTdy4ar_Yc-47Va6uFnP11wdbXKhzPYAmm2TcDhZJgTIohz69Hviw7U3l14vpZxDbLGCnkC1X_H_jtsBiiJ29279zHIiiDP3za0iw.jpg" alt="photo" loading="lazy"/></div>
</div>
<div class="tg-text">قاب های بارسایی پسند
🔥
🔥
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.3K · <a href="https://t.me/Futball180TV/101057" target="_blank">📅 23:01 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101056">
<div class="tg-post-header">📌 پیام #25</div>
<div class="tg-text">🚨
سنتکام: در شمال عراق، یکی از نیروهای نظامی آمریکا در تاریخ ۱۸ ژوئیه، حین عملیات انفجار کنترل‌شدهٔ مهمات عمل‌نکردهٔ حاصل از یک پهپاد انتحاری ایرانی، کشته شد.
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101056" target="_blank">📅 22:56 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101055">
<div class="tg-post-header">📌 پیام #24</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/609dc84999.mp4?token=JhDrJjE_nBMji37olPIgEhBUUq8hpLq4BT5LBTthMMuYI5p0bNguScVcsYKGbuillUvkHR5QOjnpNY_vtcXL0l4CVF_gOPsWTWV7o3gJZjEfdgQjAfa14m2BAqL4uwmRVA7yp2c4l3hqkVzlenK3InvtWanPnHOjoYbh4iFWiBhRLwLg_PLRM4Ovy3-cXAbw6_q8kcJzjAxdyf0D21sE4QqmhEoQnREdt5tXsPr4PJF-9a3E-FfYG6Dc1XqMWmOqKqR8MpKtjJYS-07tBj9qAWuAGTRuBMLHVA8bdDHn5R4zyydQJsTRMTtp-pX02P1oIYi9kIl9apOQ6kKUBwQf_Q" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/609dc84999.mp4?token=JhDrJjE_nBMji37olPIgEhBUUq8hpLq4BT5LBTthMMuYI5p0bNguScVcsYKGbuillUvkHR5QOjnpNY_vtcXL0l4CVF_gOPsWTWV7o3gJZjEfdgQjAfa14m2BAqL4uwmRVA7yp2c4l3hqkVzlenK3InvtWanPnHOjoYbh4iFWiBhRLwLg_PLRM4Ovy3-cXAbw6_q8kcJzjAxdyf0D21sE4QqmhEoQnREdt5tXsPr4PJF-9a3E-FfYG6Dc1XqMWmOqKqR8MpKtjJYS-07tBj9qAWuAGTRuBMLHVA8bdDHn5R4zyydQJsTRMTtp-pX02P1oIYi9kIl9apOQ6kKUBwQf_Q" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🚨
👀
🏆
کایلی جنر و تیموتی تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101055" target="_blank">📅 22:54 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101054">
<div class="tg-post-header">📌 پیام #23</div>
<div class="tg-text">بازم مارتینزززززز گرفتتتتتت</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101054" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101053">
<div class="tg-post-header">📌 پیام #22</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101053" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101052">
<div class="tg-post-header">📌 پیام #21</div>
<div class="tg-video">
<video controls preload="metadata">
  <source src="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=YOy1WV6OXLfxG6CVVh3giZjexO978ITWk2rwJluJmQivJuaUItliRL2YCSfqM8ZrfDenzH-T6AJGl1exdgj3RnN2VMWqBfHC50-JZ8IZFMZX_zKFEJszFgAg4EpwZLoFjKYoZ-iTFlFRMhn3-SVuMpYSTc7wBbA9uiyc1kc72ishcNtM55IONb_Wv4DsNRFYzy6B_-l5eb_aDnd57vOezg9C2h_Uly69eJsLG9WgvGlzUp88F4Djp5Uyi85hJYAE4weuMAFe0TdhBAQ77xIiuqRHGEKs9A-KEtSiss6-FndjVSY1X_7eN9xMAwmnSqoB8dCR_pDOYEgnNZaf3folAa6Q0atg5uxMLNeugWLqSxot9bRuGem3Y_KHCVtBgFzm-TIt4Zs5uPQCrhBWmZt2A2URIskr1CivIUjjLhpRthcXzGmQ42Fhzr5JF8Uqw0x8wfNlO3oDTAK9PtPvSCptgRxTYCu3XdZkSszxZkahcoIIivN5MESpmQr-z4KMrtSPHCdm208opizffb_Rat6OeFhLNCmGtO-T3FugUrq3CipwfdwIo-jmkZj653BfPJw1vUhdIKGcwlQXKxXYooxILgZ_hTO-tN208GY-KNUjyDdz-X3c2sHEb2RncwNv-npvfjY8rV11wwClgfBs1vUb0HDgSYevffv7gyd5nGvThhg" type="video/mp4">
</video>
<br>
<a href="https://cdn4.telesco.pe/file/ce3cfd8ff5.mp4?token=YOy1WV6OXLfxG6CVVh3giZjexO978ITWk2rwJluJmQivJuaUItliRL2YCSfqM8ZrfDenzH-T6AJGl1exdgj3RnN2VMWqBfHC50-JZ8IZFMZX_zKFEJszFgAg4EpwZLoFjKYoZ-iTFlFRMhn3-SVuMpYSTc7wBbA9uiyc1kc72ishcNtM55IONb_Wv4DsNRFYzy6B_-l5eb_aDnd57vOezg9C2h_Uly69eJsLG9WgvGlzUp88F4Djp5Uyi85hJYAE4weuMAFe0TdhBAQ77xIiuqRHGEKs9A-KEtSiss6-FndjVSY1X_7eN9xMAwmnSqoB8dCR_pDOYEgnNZaf3folAa6Q0atg5uxMLNeugWLqSxot9bRuGem3Y_KHCVtBgFzm-TIt4Zs5uPQCrhBWmZt2A2URIskr1CivIUjjLhpRthcXzGmQ42Fhzr5JF8Uqw0x8wfNlO3oDTAK9PtPvSCptgRxTYCu3XdZkSszxZkahcoIIivN5MESpmQr-z4KMrtSPHCdm208opizffb_Rat6OeFhLNCmGtO-T3FugUrq3CipwfdwIo-jmkZj653BfPJw1vUhdIKGcwlQXKxXYooxILgZ_hTO-tN208GY-KNUjyDdz-X3c2sHEb2RncwNv-npvfjY8rV11wwClgfBs1vUb0HDgSYevffv7gyd5nGvThhg" class="tg-dl-btn" target="_blank">📥 دانلود ویدیو</a>
</div>
<div class="tg-text">🏆
🇺🇸
👤
پرزیدنت ترامپ و بانوی اول ایوانکا ترامپ در کنار اینفانتینو در بخش وی آی پی استادیوم
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101052" target="_blank">📅 22:53 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101051">
<div class="tg-post-header">📌 پیام #20</div>
<div class="tg-text">وینچیچ داره با آرژانتین راه میاد!!!</div>
<div class="tg-footer">👁️ 12.2K · <a href="https://t.me/Futball180TV/101051" target="_blank">📅 22:51 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101050">
<div class="tg-post-header">📌 پیام #19</div>
<div class="tg-text">اسپانیاااااا داشت میزدددددد</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101050" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101049">
<div class="tg-post-header">📌 پیام #18</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 13.3K · <a href="https://t.me/Futball180TV/101049" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101048">
<div class="tg-post-header">📌 پیام #17</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/bsFdeG0tB8mwgbSuzdaFuJOmCUHblKFJ3tqIef61WYvrfQv_MAV8odNaxo-04VZ84bjIj2syCZsp4u7oE4Vn1TJfvEcQuMHQAfbbkuAKZqG_CzmhjnO4ucMPOJvxICGKhwNQmKnVcpMd8o0WQve39wlyHFON3YQ_rzmezJwb7iGbmri5WXcAKJby7Cq4GCRug8UM2OV2qqVVOsHlDWohczjYSl8b-eKQYi_xPU2IQc344lJMnJsbhbz2vzVA0-99I7inVBrpaoNlq7N8qfJXXoR097m9vgUNfWjzwCPHY8iDpoiEabuRMB9Pyf9xhVRviDXOVjEPzVdUYw_QsDuinA.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">دونالد ترامپ و در آغوش گرفتن کاپ جام‌جهانی</div>
<div class="tg-footer">👁️ 14.3K · <a href="https://t.me/Futball180TV/101048" target="_blank">📅 22:48 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101047">
<div class="tg-post-header">📌 پیام #16</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/ZEoQi6cPBM9qq9shau-0CN_CMV18bMo3_FrU68k5nju1qpwCRrARcLtVxW25KkKGmKOnUlUTgDOjMYy5fnse8GyyB282mfuH1fZbUZEj9WSNMhQ4s6siuGnnKK6e35FAWzLpjvN1yJBc_q601IIT5acBkQ8B4MqJ1heuAr66cgGect347039b26DHtV90-se9nvJZh1AfETxVLHUNafHpT6mGuWiO7CMFy3ncVT8I7paiKjeNonRgDvPtLQ9LMrvvlPRsXHec2rfC3JEJyAzgQqP36jEJX0u0-k4BbPwefB1YnxuYxw2Eqi29DMREFK78Zz6nAmLWr795CN8o37HbQ.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">خوش و بش یامال و مسی
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 13.6K · <a href="https://t.me/Futball180TV/101047" target="_blank">📅 22:44 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101046">
<div class="tg-post-header">📌 پیام #15</div>
<div class="tg-text">اسپانیا تا اینجا سر بوده</div>
<div class="tg-footer">👁️ 13.1K · <a href="https://t.me/Futball180TV/101046" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101045">
<div class="tg-post-header">📌 پیام #14</div>
<div class="tg-text">قشنگ به نفع آرژانتین سوت زد
😐
😐
😐</div>
<div class="tg-footer">👁️ 13.2K · <a href="https://t.me/Futball180TV/101045" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101044">
<div class="tg-post-header">📌 پیام #13</div>
<div class="tg-text">داور ریددددد</div>
<div class="tg-footer">👁️ 14.2K · <a href="https://t.me/Futball180TV/101044" target="_blank">📅 22:43 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101043">
<div class="tg-post-header">📌 پیام #12</div>
<div class="tg-text">سیمون داشت سوتی میداااااد</div>
<div class="tg-footer">👁️ 14.5K · <a href="https://t.me/Futball180TV/101043" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101042">
<div class="tg-post-header">📌 پیام #11</div>
<div class="tg-text">وااااای</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101042" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101041">
<div class="tg-post-header">📌 پیام #10</div>
<div class="tg-text">اسپانیا فشااااعر آوردههههه</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101041" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101040">
<div class="tg-post-header">📌 پیام #9</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.7K · <a href="https://t.me/Futball180TV/101040" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101039">
<div class="tg-post-header">📌 پیام #8</div>
<div class="tg-text">مارتینز عالیییییی گرفتتتت</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101039" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101038">
<div class="tg-post-header">📌 پیام #7</div>
<div class="tg-text">یامال کسخللللل نزدددددددد</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101038" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101037">
<div class="tg-post-header">📌 پیام #6</div>
<div class="tg-text">واااای</div>
<div class="tg-footer">👁️ 15.9K · <a href="https://t.me/Futball180TV/101037" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101036">
<div class="tg-post-header">📌 پیام #5</div>
<div class="tg-text">اسپانیا حشررررری شروع کرده</div>
<div class="tg-footer">👁️ 14.9K · <a href="https://t.me/Futball180TV/101036" target="_blank">📅 22:41 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101035">
<div class="tg-post-header">📌 پیام #4</div>
<div class="tg-text">🔥
🔥
🔥
برررررریم سراغ حساس‌ترین بازی سال ۲۰۲۶ و فیناااااال جام‌جهانی فوتبال
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 14.8K · <a href="https://t.me/Futball180TV/101035" target="_blank">📅 22:33 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101034">
<div class="tg-post-header">📌 پیام #3</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/A8K1ShYRyQMVjLrhEzcCxpZgNHHvzT95snVR4tmn2JNZsICn3mJUEtkwpd0uN0ngDGzIAD2UvmgbtOvDICJBus8ffzAipnFu_ABxA_eM3CPcrRvTDaTQdPXWn0jvwuYxheUN3wnCqIcXmD0TF_tmZQDA8A3NLFpFdryKQ7oGMDZtgP-EwRts0d77uNdzfvY9Q3fl9cp2FZcmA9hR3MlyFF71KOyB-Un7OApwo5jMyg8RcYBtOAQbxrpotpMJ2Z98gKxkSVCg4MWLERaDckkNJFXgBh0eEjVg7u_MeW_ZZnJyjp_zgwmSJh_vwAzX_FS03t1Jgqd9wZ27g1qQelQ53w.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">ترامپ تو ورزشگاه
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 15.6K · <a href="https://t.me/Futball180TV/101034" target="_blank">📅 22:26 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101033">
<div class="tg-post-header">📌 پیام #2</div>
<div class="tg-photo"><img src="https://cdn4.telesco.pe/file/mgSzUeT6U0QdDVFo48gIqKW7S2JsaWHmI78oq5JuuUExjfVIvY3-dQOy_0ckS8n3RG5v4m7qs6xpYWO8xd0Ii_3LU063PI6dXB_l-zhoWgDYRgETJQqUppF6imuq-X27ISrfqaL-c7vijJ1A_PyWaiMIwUAc0LHvPxiLBfKlUs-j3YkRe2EZYbeo6RiihB0L8Z3y3i--UwzlIFd0whzv4ZNgCc1QvS0hpnlx7lal_pf2NBByZDpNzGK8S17sU5ouBsmxi_bd83HKw6haYqgpgzJT1H24gcCmu2rQ8cMOYLBeg66W60s2eDQkLamFA1Kc_WJSB4_MuxN6OxjQi3O5xg.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🇪🇸
ورود پادشاه اسپانیا به مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 17.2K · <a href="https://t.me/Futball180TV/101033" target="_blank">📅 22:07 · 28 Tir 1405</a></div>
</div>

<div class="tg-post" id="msg-101032">
<div class="tg-post-header">📌 پیام #1</div>
<div class="tg-photo"><img src="https://cdn1.telesco.pe/file/skHOmhxMRiYpsbbP9MIVS-sPrdxNFrhicKn4TM0BPwQ5kseQnXB1X1FqWcLj-Sg-PmR5Hz-ft7KcSBml-wUr1h46vgtXGdRotBkdo6tEX5t1B6GO6kTsp8bbF3PqDlrWYnJ655vNHRtYhhhB-h455AD7M9tifSc8cCdOTXKBCYAxR5UgdRmhQbeo9wA__4XbgpkYr4_u_MBQNertZeqzJZIsVgfVfCseTqHhWrN3OPy8xeFYJ2u8s5ACso6DYgndDa5xSFpxCj58QK-Vu7-EiRPJvowd0epmtS3MOb4UFCWYob7wHQrLEujWlT87TEsJEBm_anv_ZKrsAwl3kWnohw.jpg" alt="photo" loading="lazy"/></div>
<div class="tg-text">🚨
🚨
🚨
ورود ترامپ با هلیکوپتر به مت‌لایف
⚽️
@Futball180TV</div>
<div class="tg-footer">👁️ 18.2K · <a href="https://t.me/Futball180TV/101032" target="_blank">📅 22:04 · 28 Tir 1405</a></div>
</div>

<hr>
<p align="center"><small>✨ این صفحه به صورت خودکار از تلگرام بروزرسانی می‌شود</small></p>
</div>
</div>
